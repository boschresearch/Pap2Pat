import numpy as np
import rouge_metric.py_rouge
from numba import jit
from rouge_metric.py_rouge import _lcs_elements
from rouge_metric import PyRouge

from pap2pat.clustering import ClusteredPatent


class Rouge:
    def __init__(self):
        patch_rouge()
        self.rouge = PyRouge(rouge_n=(1, 2, 3, 4))

    def compute(self, doc: ClusteredPatent) -> dict:
        result = {
            "rouge": self.rouge.evaluate(
                hypotheses=[doc.complete_gen],
                multi_references=[[doc.complete_ref]],
            ),
            "clustered_rouge": {
                cluster: (
                    {
                        **self.rouge.evaluate(  # type: ignore
                            hypotheses=[doc.gen_sections[heading] for heading in cluster_headings],
                            multi_references=[
                                [doc.ref_sections[heading]] for heading in cluster_headings
                            ],
                        ),
                        "headings": cluster_headings,
                    }
                    if cluster_headings
                    else None
                )
                for cluster, cluster_headings in doc.clusters.items()
            },
        }
        return result


def patch_rouge():
    """Monkeypatch JIT-compiled LCS computation"""
    rouge_metric.py_rouge._lcs_table = _lcs_table
    rouge_metric.py_rouge._lcs_union = _lcs_union


@jit(nopython=True)
def _lcs_table(a, b):
    m, n = len(a), len(b)
    table = np.zeros((m + 1, n + 1), dtype=np.int32)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table


def _lcs_union(hyps, ref):
    lcs_union = set()
    for hyp in hyps:
        if ref and hyp:  # numba cant handle empty lists ...
            lcs_elem = _lcs_elements(hyp, ref, _lcs_table(hyp, ref))  # type: ignore
        else:
            table = [[0.0 for _ in range(len(hyp) + 1)] for _ in range(len(hyp) + 1)]
            lcs_elem = _lcs_elements(hyp, ref, table)
        lcs_union = lcs_union.union(ref_idx for _, ref_idx in lcs_elem)
    return lcs_union
