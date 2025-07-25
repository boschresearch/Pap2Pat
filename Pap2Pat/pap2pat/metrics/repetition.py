from collections import Counter
import logging

import spacy
import spacy.tokens.doc
from transformers import AutoTokenizer, BatchEncoding


logger = logging.getLogger("bertscore")


class RepetitionScore:
    def __init__(
        self,
        tokenizer_path: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        window_size: int = 256,
        stride: int = 64,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.spacy = spacy.load("en_core_web_sm")
        self.spacy.max_length = 3_000_000
        self.window_size = window_size
        self.stride = stride

    def compute(self, text: str) -> tuple[list[dict], dict]:
        spacy_doc = self.spacy(text)
        enc = self.tokenizer(text, return_attention_mask=False, add_special_tokens=False)
        scores = list(self.get_sliding_window_scores(enc, spacy_doc))  # type: ignore
        return scores, {
            "rr": sum(score["rr"] for score in scores) / len(scores),
            "sentence-level": sum(score["rr"] > 0.8 and score["grammar"] >= 0.5 for score in scores)
            / len(scores),
            "word-level": sum(score["rr"] > 0.8 and score["grammar"] < 0.5 for score in scores)
            / len(scores),
            "rr>80": sum(score["rr"] > 0.8 for score in scores) / len(scores)
        }

    def get_sliding_window_scores(self, enc: BatchEncoding, spacy_doc: spacy.tokens.doc.Doc):
        tokens: list[int] = enc["input_ids"]  # type: ignore
        for i, tokens_window in sliding_window(tokens, self.window_size, self.stride):
            tokens_window = tokens[i : i + self.window_size]
            start_char = enc.token_to_chars(i).start
            end_char = enc.token_to_chars(i + self.window_size + 1)
            end_char = end_char.start if end_char is not None else len(spacy_doc.text)

            rr = compute_rr_score(tokens_window)

            spacy_span = spacy_doc.char_span(start_char, end_char, alignment_mode="expand")
            assert spacy_span is not None
            grammar = grammaticality_score(list(spacy_span.sents))  # type: ignore

            yield {"rr": rr, "grammar": grammar, "text": spacy_span.text, "char": start_char}


def sliding_window(values: list, size: int, stride: int):
    if len(values) < size:
        yield 0, values
        return
    for i in range(0, len(values) - size, stride):
        yield i, values[i : i + size]


def compute_rr_score(tokens: list[int]):
    rr = 1
    for n in range(1, 5):
        n_gram_counts = Counter(get_ngrams(tokens, n)).most_common()
        n_singleton = sum(n == 1 for _, n in n_gram_counts)
        n_total = len(n_gram_counts)
        rrn = (n_total - n_singleton) / n_total
        rr *= rrn
    return rr ** (1 / 4)


def get_ngrams(tokens, n):
    i = 0
    while len(tokens) >= i + n:
        yield tuple(tokens[i : i + n])
        i += 1


def grammaticality_score(sentences):
    points = 0
    total_possible_points = 0
    for sentence in sentences:
        # sent starts with upper case and ends with punctuation
        if sentence.text[0].isupper() and sentence.text[-1] in ".!?":
            points += 1
        total_possible_points += 1

        # sent contains noun phrase and verb
        has_noun = any(token.pos_ in ("NOUN", "PROPN") for token in sentence)
        has_verb = any(token.pos_ == "VERB" for token in sentence)
        if has_noun and has_verb:
            points += 1
        total_possible_points += 1

        # sent length is in a certain range
        if 10 < len(sentence.text) < 200:
            points += 1
        total_possible_points += 1

    if total_possible_points > 0:
        score = points / total_possible_points
    else:
        score = 0
    return score
