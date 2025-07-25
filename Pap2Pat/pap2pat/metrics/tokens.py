from transformers import AutoTokenizer

from pap2pat.clustering import ClusteredPatent


class Tokens:
    def __init__(self, tokenizer_path: str = "meta-llama/Meta-Llama-3-8B-Instruct"):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

    def compute(self, doc: ClusteredPatent) -> dict:
        return {
            "tokens": {
                "generated": (gen := len(self.tokenizer.encode(doc.complete_gen))),
                "reference": (ref := len(self.tokenizer.encode(doc.complete_ref))),
                "fraction": gen / ref,
            },
            "clustered_tokens": {
                cluster: (
                    {
                        "generated": (
                            gen := len(
                                self.tokenizer.encode(
                                    "\n\n".join(
                                        [doc.gen_sections[heading] for heading in cluster_headings]
                                    )
                                )
                            )
                        ),
                        "reference": (
                            ref := len(
                                self.tokenizer.encode(
                                    "\n\n".join(
                                        [doc.ref_sections[heading] for heading in cluster_headings]
                                    )
                                )
                            )
                        ),
                        "fraction": gen / ref,
                        "headings": cluster_headings,
                    }
                    if cluster_headings
                    else None
                )
                for cluster, cluster_headings in doc.clusters.items()
            },
        }
