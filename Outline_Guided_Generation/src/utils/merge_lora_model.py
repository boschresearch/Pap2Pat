from pathlib import Path

import torch
from hydralette import Config, Field
from peft.auto import AutoPeftModelForCausalLM
from transformers import AutoTokenizer

cfg = Config(checkpoint_dir=Field(type=Path))


def main(cfg: Config):
    model = AutoPeftModelForCausalLM.from_pretrained(
        cfg.checkpoint_dir, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True
    )
    merged_model = model.merge_and_unload()
    merged_model.save_pretrained(
        cfg.checkpoint_dir.parent / "checkpoint_merged",
        safe_serialization=True,
        max_shard_size="2GB",
    )
    tokenizer = AutoTokenizer.from_pretrained(model.name_or_path)
    tokenizer.save_pretrained(cfg.checkpoint_dir.parent / "checkpoint_merged")


if __name__ == "__main__":
    cfg.apply()
    main(cfg)
