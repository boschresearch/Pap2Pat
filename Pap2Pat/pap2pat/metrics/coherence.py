from collections import defaultdict
import itertools
from pathlib import Path

import disco_score.metrics.discourse
import disco_score.metrics.sent_graph
import numpy as np
import pysbd
import spacy
import torch
from disco_score import DiscoScorer
from pyrootutils import setup_root

root = setup_root(__file__)
seg = pysbd.Segmenter(language="en", clean=False)


def load_samples(run_dir: Path, split: str):
    for sample_dir in run_dir.glob(f"predictions/{split}/*"):
        gen = sample_dir.joinpath("generated.md").read_text()
        ref = sample_dir.joinpath("reference.md").read_text()
        yield (sample_dir.name, gen, ref)


def bert_encode_sliding_window(bert, input, am, max_len=512, window_size=256):
    """
    Adds sliding window bert encoding to handle long documents
    """
    bert.eval()
    with torch.no_grad():
        seq_len = max(input.size(1), max_len)
        hidden_states = []
        for i in range(max_len, seq_len + window_size, window_size):
            if i == max_len:
                idx = 0  
            else: 
                idx = window_size

            start = i - max_len
            out = bert(input_ids = input[:, start:i], token_type_ids = None, attention_mask = am[:, start:i])
            hidden_states.append(out.last_hidden_state[:, idx:, :])

        out = torch.cat(hidden_states, dim=1)
        return out
    
disco_score.metrics.sent_graph.bert_encode = bert_encode_sliding_window


class CoherenceMetrics:

    def __init__(
        self, 
        device: str = 'cuda:0',
        model_path: Path | str = root / "MNLI_BERT"
    ):
        self.nlp = spacy.load(
            "en_core_web_sm", enable=["tok2vec", "attribute_ruler", "tagger", "lemmatizer"]
        )
        self.nlp.max_length = 3_000_000
        self.seg = pysbd.Segmenter(language="en", clean=False)
        self.discoscore =  DiscoScorer(device=device, model_name=str(model_path))
        

    def score(self, gen: str, ref: str) -> dict[str, float]:
        return {
            **self.score_lc_ttr(gen),
            **self.score_discoscore(gen, ref)
        }


    def score_lc_ttr(self, s: str) -> dict[str, float]:
        sents = self.seg.segment(s)
        lc_nouns_dict = defaultdict(list)
        all_lemmas = []

        for i, sent in enumerate(self.nlp.pipe(sents)):
            for token in sent:
                if token.pos_ in ["PROPN", "NOUN"]:
                    lc_nouns_dict[token.lemma_].append(i)

                if token.is_alpha:
                    all_lemmas.append(token.lemma_)
        
        lc_repetitions_token_cnt = len([k for k, v in lc_nouns_dict.items() if len(v) > 1])
        lc_score = lc_repetitions_token_cnt / len(lc_nouns_dict)

        ttr = len(set(all_lemmas)) / len(all_lemmas)
        
        return {"lc": lc_score, "ttr": ttr}

    def score_discoscore(self, gen: str, ref: str) -> dict[str, float]:
        return {"DS_SENT_NN": float(self.discoscore.DS_SENT_NN(gen, [ref]))}
