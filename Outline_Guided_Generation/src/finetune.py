# Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

import datasets
import rich.console
import rich.syntax
import torch
import transformers
import yaml
from alignment import (
    DataArguments,
    H4ArgumentParser,
    ModelArguments,
    get_checkpoint,
    get_kbit_device_map,
    get_peft_config,
    get_quantization_config,
    get_tokenizer,
)
from pyrootutils import setup_root
from transformers import PreTrainedTokenizerBase, set_seed
from trl import SFTConfig, SFTTrainer

from src.dataset import paper_extractor
from src.dataset.dataset import PatentDraftingDataset
from src.utils.general import get_logger, launch_debugger

root = setup_root(__file__)
log = get_logger(__name__)
rich_console = rich.console.Console()


@dataclass
class RunArguments:
    launch_debugger: bool = False


@dataclass
class DatasetArguments:
    data_dir: Path = root.parent / "Pap2Pat" / "data"
    outline_suffix: str = "long"
    paper_extractor: str = "AbstractOnly"
    do_chunk: bool = True
    tokenizer: PreTrainedTokenizerBase | None = None
    max_total_length: int = 8192
    max_instruction_length: int = 2048
    max_paper_length: int | None = None
    max_patent_length: int | None = None
    n_threads: int = 4
    exclude_splits: list[str] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        if isinstance(self.paper_extractor, str):
            self.paper_extractor = getattr(paper_extractor, self.paper_extractor)

        if self.max_paper_length is None:
            self.max_paper_length = int((self.max_total_length - self.max_instruction_length) / 2)

        if self.max_patent_length is None:
            self.max_patent_length = int(
                0.7 * (self.max_total_length - self.max_instruction_length) / 2
            )


def parse_args() -> tuple[RunArguments, DatasetArguments, ModelArguments, DataArguments, SFTConfig]:
    parser = H4ArgumentParser(
        (RunArguments, DatasetArguments, ModelArguments, DataArguments, SFTConfig)
    )  # type: ignore
    return parser.parse()


def main() -> None:
    run_args, dataset_args, model_args, data_args, training_args = parse_args()

    if run_args.launch_debugger:
        if training_args.local_rank == 0:
            launch_debugger()
        else:
            time.sleep(30)

    set_seed(training_args.seed)
    log_level = training_args.get_process_log_level()
    log.setLevel(log_level)
    datasets.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()
    log.info(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        f" distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )

    if training_args.local_rank in (-1, 0):
        config_yaml = yaml.dump(
            {
                "run_args": asdict(run_args),
                "dataset_args": asdict(dataset_args),
                "model_args": asdict(model_args),
                "data_args": asdict(data_args),
                "training_args": asdict(training_args),
            }
        )
        rich_console.print(rich.syntax.Syntax(config_yaml, "yaml"))
        run_dir = Path(training_args.output_dir).resolve()
        run_dir.mkdir(exist_ok=True, parents=True)
        run_dir.joinpath("config.yaml").write_text(config_yaml)
        log.info(f"Saving run to {run_dir.relative_to(root)}")

    last_checkpoint = get_checkpoint(training_args)  # type: ignore
    if last_checkpoint is not None and training_args.resume_from_checkpoint is None:
        log.info(f"Checkpoint detected, resuming training at {last_checkpoint=}.")

    log.info("*** Loading dataset ***")
    tokenizer = get_tokenizer(model_args, data_args)
    dataset_args.tokenizer = tokenizer
    dataset = PatentDraftingDataset(**asdict(dataset_args)).to_huggingface_dataset()

    log.info("*** Load pretrained model ***")
    assert model_args.torch_dtype is not None
    torch_dtype = (
        model_args.torch_dtype
        if model_args.torch_dtype in ["auto", None]
        else getattr(torch, model_args.torch_dtype)
    )
    quantization_config = get_quantization_config(model_args)

    model_kwargs = dict(
        revision=model_args.model_revision,
        trust_remote_code=model_args.trust_remote_code,
        attn_implementation=model_args.attn_implementation,
        torch_dtype=torch_dtype,
        use_cache=not training_args.gradient_checkpointing,
        device_map=get_kbit_device_map() if quantization_config is not None else None,
        quantization_config=quantization_config,
    )

    assert model_args.model_name_or_path is not None
    model = model_args.model_name_or_path

    log.info("*** Initializing Trainer ***")
    trainer = SFTTrainer(
        model=model,
        model_init_kwargs=model_kwargs,
        args=training_args,  # type: ignore
        train_dataset=dataset["train"],
        eval_dataset=dataset["val"],
        tokenizer=tokenizer,
        peft_config=get_peft_config(model_args),
    )

    log.info("*** Train ***")
    checkpoint = None
    if training_args.resume_from_checkpoint is not None:
        checkpoint = training_args.resume_from_checkpoint
    elif last_checkpoint is not None:
        checkpoint = last_checkpoint
    train_result = trainer.train(resume_from_checkpoint=checkpoint)  # type: ignore[reportCallIssue]
    metrics = train_result.metrics
    trainer.log_metrics("train", metrics)
    trainer.save_metrics("train", metrics)
    trainer.save_state()

    log.info("*** Save model ***")
    checkpoint_path = str(Path(training_args.output_dir) / "checkpoint")
    trainer.save_model(checkpoint_path)
    log.info(f"Model saved to {checkpoint_path}")
    if trainer.accelerator.is_main_process:
        trainer.model.config.save_pretrained(checkpoint_path)

    log.info("*** Running Evaluation ***")
    if training_args.do_eval and trainer.accelerator.is_main_process:
        trainer.args.remove_unused_columns = False
        for split, ds in dataset.items():
            if split == "train":
                continue
            log.info(f"*** Evaluate {split} ***")
            ds_tokenized = ds.map(
                lambda d: dict(input_ids=tokenizer.apply_chat_template(d["messages"])),
                remove_columns=ds.column_names,
            )
            metrics = trainer.evaluate(ds_tokenized, metric_key_prefix=split)  # type: ignore
            trainer.log_metrics(split, metrics)
            trainer.save_metrics(split, metrics)


if __name__ == "__main__":
    main()
