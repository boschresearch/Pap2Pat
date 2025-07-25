from collections import Counter

from transformers import AutoTokenizer


class RR:
    def __init__(
        self,
        tokenizer_path: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        max_n: int = 4,
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.max_n = max_n

    @staticmethod
    def get_ngrams(tokens, n):
        i = 0
        while len(tokens) >= i + n:
            yield tuple(tokens[i : i + n])
            i += 1

    def get_rr_score(self, tokens: list[int]):
        rr = 1
        for n in range(1, self.max_n):
            n_gram_counts = Counter(self.get_ngrams(tokens, n)).most_common()
            n_singleton = sum(n == 1 for _, n in n_gram_counts)
            n_total = len(n_gram_counts)
            rrn = (n_total - n_singleton) / n_total
            rr *= rrn
        return rr ** (1 / self.max_n)

    def compute(self, gen: str, ref: str, paper: str) -> dict:
        return {
            "rr": {
                "generated": self.get_rr_score(self.tokenizer.encode(gen)),
                "reference": self.get_rr_score(self.tokenizer.encode(ref)),
                "paper": self.get_rr_score(self.tokenizer.encode(paper)),
            }
        }
