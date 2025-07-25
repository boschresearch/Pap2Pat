from sacrebleu import BLEU as BLEU_

from pap2pat.clustering import ClusteredPatent


class BLEU:
    def __init__(self):
        self.bleu = BLEU_()

    @staticmethod
    def unpack_score(score):
        return dict(
            score=score.score,
            score_without_bp=score.score / score.bp if score.bp > 0 else score.score,
            precisions=score.precisions,
            ref_words=score.ref_len,
            gen_words=score.sys_len,
            bp=score.bp,
        )

    def compute(self, doc: ClusteredPatent) -> dict:
        return {
            "bleu": self.unpack_score(
                self.bleu.corpus_score(
                    [doc.gen_sections[heading] for heading in doc.headings],
                    [[doc.ref_sections[heading] for heading in doc.headings]],
                )
            ),
            "clustered_bleu": {
                cluster: (
                    {
                        **self.unpack_score(
                            self.bleu.corpus_score(
                                [
                                    doc.gen_sections[heading]
                                    for heading in cluster_headings
                                ],
                                [
                                    [doc.ref_sections[heading]]
                                    for heading in cluster_headings
                                ],
                            )
                        ),
                        "headings": cluster_headings,
                    }
                    if cluster_headings
                    else None
                )
                for cluster, cluster_headings in doc.clusters.items()
            },
        }
