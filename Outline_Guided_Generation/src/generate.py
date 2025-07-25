import re
import sys
from typing import TYPE_CHECKING

import rich.syntax
import sglang as sgl
from hydralette import Config, Field
from pyrootutils import setup_root
from tqdm import tqdm
from transformers import AutoTokenizer

from src.dataset.dataset import PatentDraftingDataset, PatentDraftingSample, data_cfg
from src.dataset.prompt import (
    format_outline_md,
    format_outline_ref,
    format_reference_patent,
    get_all_headings,
    iter_sections_with_next,
)
from src.utils.general import (
    get_logger,
    get_run_dir,
    launch_debugger,
    redirect_stdout_stderr,
    set_seed,
)
from src.utils.sgl import (
    MyProgramState,
    get_model_info,
    return_exception,
    run_program_batch_generator,
)

if TYPE_CHECKING:
    from pathlib import Path

    from src.dataset.chunk import PatentChunk

root = setup_root(__file__)
log = get_logger(__file__)
rich_console = rich.console.Console()


cfg = Config(
    port=59532,
    max_startup_time=120,
    model=Field(
        reference=lambda cfg: (
            get_model_info(cfg.port, cfg.max_startup_time)["model_path"]
            if cfg.port is not None
            else cfg.model
        ),
    ),
    debug=False,
    run_dir=Field(default_factory=lambda: get_run_dir("interactive")),
    seed=Field(default=42),
    data=data_cfg,
    temperature=0.6,
    # Default sampling params from sglang
    top_p=1.0,
    top_k=-1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)


def postprocess(fork_messages: list[list[dict[str, str]]], description: dict) -> str:
    responses = []
    for messages in fork_messages:
        # extract markdown block from state
        last_message = messages[-1]
        assert last_message["role"] == "assistant"
        response = re.findall(r"```md(.*)```", last_message["content"].strip(), re.DOTALL)[0]
        response = response.strip()
        if response:
            responses.append(response)
    response = "\n\n".join(responses)

    # filter out repeated headings from chunking
    all_headings: list[str] = list(get_all_headings(description, return_hashes=True))
    lines = []
    for line in response.split("\n"):
        is_repeated_heading = False
        if headings := re.findall(r"^(#+\s+.*)\s*$", line):
            heading = headings[0]
            if not all_headings or heading != all_headings[0]:
                is_repeated_heading = True
            else:
                all_headings.pop(0)

        is_ellipsis = line.strip() == "..."
        if not is_repeated_heading and not is_ellipsis:
            lines.append(line)

    # normalize spacing
    response = re.sub("\n{2,}", "\n\n", "\n".join(lines))
    return response


def format_ground_truth_patent_from_chunks(sample: PatentDraftingSample) -> str:
    messages = []
    for chunk in sample.chunks:
        s = "```md\n"
        for (level, section), _ in iter_sections_with_next(chunk.content, level=chunk.level):
            current_heading = f'\n\n{"#" * (level + 1)} {section["title"]}\n\n'
            s += current_heading
            if section["paragraphs"]:
                s += "\n\n".join(section["paragraphs"])

        s += "```"
        messages.append([{"role": "assistant", "content": s}])

    description = sample.patent_content["sections"][0]
    return postprocess(messages, description)


@sgl.function
def generate_patent(s: MyProgramState, sample: PatentDraftingSample) -> None:
    chunk_forks = s.fork(len(sample.chunks))

    for chunk, fork in zip(sample.chunks, chunk_forks):  # type: ignore
        chunk: PatentChunk
        fork: MyProgramState
        fork += sgl.system(chunk.prompt.system)  # type: ignore
        fork += sgl.user(chunk.prompt.user)  # type: ignore

        # Build assistant response
        token_limit_reached = False
        fork += sgl.assistant_begin()
        fork += "```md\n"
        for (level, section), (next_level, next_section) in iter_sections_with_next(
            chunk.content,
            level=chunk.level,
        ):
            # check if model has exceeded context window
            meta_info = fork.get_meta_info(None)
            if (
                meta_info is not None
                and "finish_reason" in meta_info
                and (
                    (
                        # finish reason used in older versions of sglang
                        isinstance(meta_info["finish_reason"], str)
                        and "FINISH_LENGTH" in meta_info["finish_reason"]
                    )
                    or (
                        # finish reason used in newer versions of sglang, same as openai
                        isinstance(meta_info["finish_reason"], dict)
                        and "length" in meta_info["finish_reason"]["type"]
                    )
                )
            ):
                log.warning(f"{sample.id}: Stopping early because context window is exceeded")
                token_limit_reached = True

            # Heading
            current_heading = f'\n\n{"#" * (level + 1)} {section["title"]}\n\n'
            fork += current_heading
            if next_section is not None and next_level is not None:
                next_heading = [f'\n\n{"#" * (next_level + 1)} {next_section["title"]}\n\n']
            else:
                next_heading = []

            # Content
            if section["paragraphs"] and not token_limit_reached:
                fork += sgl.gen(
                    max_tokens=cfg.data.max_total_length, stop=["<s>", "</s>", "```", *next_heading]
                )

        fork += "```"
        fork += sgl.assistant_end()

    chunk_forks.join()
    s.chunk_forks = chunk_forks  # Save forks for later
    description = sample.patent_content["sections"][0]
    messages = [chunk_fork.messages() for chunk_fork in chunk_forks]
    combined_patent = postprocess(messages, description)
    s += sgl.assistant(combined_patent)  # type: ignore


def main(cfg: Config) -> None:
    if cfg.debug:
        launch_debugger()

    # Print and save config
    rich_console.print(rich.syntax.Syntax(cfg.to_yaml(), "yaml"))
    cfg.run_dir.joinpath("config.yaml").write_text(cfg.to_yaml())
    cfg.run_dir.joinpath("overrides.txt").write_text("\n".join(sys.argv[1:]))
    set_seed(cfg.seed)

    # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")
    tokenizer = AutoTokenizer.from_pretrained(cfg.model)
    ds = PatentDraftingDataset(
        data_dir=cfg.data.papers_dir,
        outline_suffix=cfg.data.outline_suffix,
        do_chunk=True,
        add_claim=cfg.data.add_claim,
        tokenizer=tokenizer,
        max_total_length=cfg.data.max_total_length,
        max_instruction_length=cfg.data.max_instruction_length,
        max_paper_length=cfg.data.max_paper_length,
        max_patent_length=cfg.data.max_patent_length,
        paper_extractor=cfg.data.paper_extractor,
        exclude_splits=["train"],
    )

    # import pickle
    # with open("ds.pkl", "rb") as fp:
    #     ds: PatentDraftingDataset = pickle.load(fp)

    if cfg.port is None:
        log.info(f"Loading model from '{cfg.model}'")
        runtime = sgl.Runtime(model_path=cfg.model)
        log.info("Done.")
    else:
        log.info(f"Loading model from 'http://localhost:{cfg.port}'")
        runtime = sgl.RuntimeEndpoint(f"http://localhost:{cfg.port}")
        log.info("Done.")
    sgl.set_default_backend(runtime)  # type: ignore

    # monkeypatch sgl to yield one result at a time and add exception handling
    sgl.lang.interpreter.run_program_batch = run_program_batch_generator  # type: ignore
    sgl.lang.interpreter.run_program = return_exception(sgl.lang.interpreter.run_program)  # type: ignore

    for split, samples in ds.splits.items():
        args = [
            dict(sample=sample) for sample in samples
            if not cfg.run_dir.joinpath(f"predictions/{split}/{sample.id}").exists() 
        ]

        for inputs, gen_state in tqdm(
            generate_patent.run_batch(
                args,
                num_threads=1,
                temperature=cfg.temperature,
                top_k=cfg.top_k,
                top_p=cfg.top_p,
                frequency_penalty=cfg.frequency_penalty,
                presence_penalty=cfg.presence_penalty,
            ),
            desc=f"Generating {split}",
            total=len(samples),
        ):
            sample: PatentDraftingSample = inputs["sample"]
            log.info(f"Current sample: {sample.id}")

            # If generation failed, retry
            n_retries = 0
            while isinstance(gen_state, BaseException):
                if n_retries > 5:
                    raise gen_state
                log.error(f"Failed to generate. Retrying for the {n_retries + 1}'th time ...")
                gen_state = generate_patent.run(**inputs)
                n_retries += 1

            gen_patent = gen_state.messages()[-1]["content"].strip()
            pred_path: Path = cfg.run_dir.joinpath(f"predictions/{split}/{sample.id}").resolve()

            # Sanity checks that chunking hasnt altered patent content
            log.info("Running sanity checks")
            description = sample.patent_content["sections"][0]
            ref_patent_from_chunks = format_ground_truth_patent_from_chunks(sample).strip()
            ref_patent_from_complete = format_reference_patent([description]).strip()
            if ref_patent_from_chunks != ref_patent_from_complete:
                pred_path.joinpath("errors").mkdir(exist_ok=True, parents=True)
                pred_path.joinpath("errors/patent_from_chunks.md").write_text(
                    ref_patent_from_chunks
                )
                pred_path.joinpath("errors/patent_from_whole.md").write_text(
                    ref_patent_from_complete
                )
                log.error(
                    f"{sample.id}: Reference patent from chunks does not match reference patent created from whole description! "
                    f"See '{pred_path.joinpath('errors/patent_from_chunks.md').relative_to(root)}' "
                    f"and '{pred_path.joinpath('errors/patent_from_whole.md').relative_to(root)}'",
                )
            outline_from_complete = format_outline_ref([description]).strip()
            outline_from_chunks = format_outline_md(sample.chunks).strip()
            if outline_from_complete != outline_from_chunks:
                pred_path.joinpath("errors").mkdir(exist_ok=True, parents=True)
                pred_path.joinpath("errors/outline_from_chunks.md").write_text(outline_from_chunks)
                pred_path.joinpath("errors/outline_from_whole.md").write_text(outline_from_complete)
                log.error(
                    f"{sample.id}: Reference outline from chunks does not match reference outline created from whole description! "
                    f"See '{pred_path.joinpath('errors/outline_from_chunks.md').relative_to(root)}' "
                    f"and '{pred_path.joinpath('errors/outline_from_whole.md').relative_to(root)}'",
                )

            # Save generated patent, reference patent, outline and prompts
            log.info("Saving outputs")
            pred_path.mkdir(exist_ok=True, parents=True)
            pred_path.joinpath("generated.md").write_text(gen_patent)
            pred_path.joinpath("reference.md").write_text(ref_patent_from_complete)
            # pred_path.joinpath("outline.md").write_text(sample.patent_outline_md)

            prompts_path = pred_path / "conversations"
            prompts_path.mkdir(parents=True, exist_ok=True)
            for i, chunk_fork in enumerate(gen_state.chunk_forks):  # type: ignore
                system, user, assistant = chunk_fork.messages()
                prompts_path.joinpath(f"chunk-{i}-system.md").write_text(system["content"])
                prompts_path.joinpath(f"chunk-{i}-user.md").write_text(user["content"])
                prompts_path.joinpath(f"chunk-{i}-assistant.md").write_text(assistant["content"])

    runtime.shutdown()


if __name__ == "__main__":
    cfg.apply()
    cfg.run_dir.mkdir(parents=True, exist_ok=True)
    with cfg.run_dir.joinpath("output.log").open("w") as log_f, redirect_stdout_stderr(log_f):
        main(cfg)
