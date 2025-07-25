from collections import defaultdict
import re
import logging

import bert_score.utils
import torch
import torch.nn.functional as F
import transformers

from pap2pat.clustering import ClusteredPatent

logger = logging.getLogger("bertscore")


class BERTScore:
    def __init__(
        self, device: str, model_id: str = "allenai/scibert_scivocab_uncased", patch: bool = True
    ):
        if patch:
            Patcher.patch_bertscore()
        else:
            Patcher.unpatch_bertscore()

        self.model = bert_score.BERTScorer(
            model_type=model_id,
            use_fast_tokenizer=True,
            batch_size=1,
            device=device,
        )
        if "scibert" in model_id:
            self.model._tokenizer.model_max_length = 512

    def compute(self, doc: ClusteredPatent, orig_patent: str, gen_patent: str) -> dict:
        def format_sections(sections, headings):
            s = ""
            for heading in headings:
                content = sections[heading]
                s += f"\n{heading}\n\n{content}\n"
            return re.sub(r"\n{3,}", "\n\n", s.strip())

        parts = ["All"]
        ref = [[orig_patent]]
        gen = [gen_patent]

        metrics = ("P", "R", "F1")
        all_scores = {part: {m: -1 for m in metrics} for part in ("All", *doc.clusters)}

        for part, cluster_headings in doc.clusters.items():
            ref_section = format_sections(doc.ref_sections, cluster_headings)
            gen_section = format_sections(doc.gen_sections, cluster_headings)

            if not ref_section:
                all_scores[part] = None  # type: ignore

            elif not gen_section:
                for m in metrics:
                    all_scores[part][m] = 0

            else:
                parts.append(part)
                ref.append([ref_section])
                gen.append(gen_section)

        for part, gen_, ref_ in zip(parts, gen, ref):
            scores = self.model.score([gen_], [ref_], batch_size=1)
            for metric, values in zip(metrics, scores):
                all_scores[part][metric] = values[0].item()  # type: ignore

        return {
            "BERTScore": all_scores["All"],
            "clustered_BERTScore": {cluster: all_scores[cluster] for cluster in doc.clusters},
        }


class Patcher:
    original_get_bert_embedding = bert_score.utils.get_bert_embedding
    original_greedy_cos_idf = bert_score.utils.greedy_cos_idf

    @staticmethod
    def patch_bertscore():
        bert_score.utils.get_bert_embedding = get_bert_embedding
        bert_score.utils.greedy_cos_idf = greedy_cos_idf

    @staticmethod
    def unpatch_bertscore():
        bert_score.utils.get_bert_embedding = Patcher.original_get_bert_embedding
        bert_score.utils.greedy_cos_idf = Patcher.original_greedy_cos_idf


def get_bert_embedding(
    all_sens: list[str],
    model: transformers.PreTrainedModel,
    tokenizer: transformers.PreTrainedTokenizerBase,
    idf_dict,
    batch_size: int = -1,
    device="cuda:0",
    all_layers=False,
    stride: int = 128,
):
    """Monkeypatch for bert_score.utils.get_bert_embedding to allow arbitrary context lengths using chunks with stride"""

    def pad_inputs(encodings):
        max_len = max(sum(am) for am in encodings.attention_mask)
        input_ids = torch.tensor(
            [
                [*ids, *[tokenizer.pad_token_id for _ in range(max_len - len(ids))]]
                for ids in encodings.input_ids
            ],
            device=device,
        )
        am = torch.tensor(
            [
                [*mask, *[0 for _ in range(max_len - len(mask))]]
                for mask in encodings.attention_mask
            ],
            device=device,
        )
        return input_ids, am

    def pad_results(merged_embeddings, merged_attention_mask, merged_idf):
        max_len = max(len(emb) for emb in merged_embeddings)
        # emb_dim = len(merged_embeddings[0][0])
        emb_dim = model.config.hidden_size
        merged_embeddings = torch.stack(
            [
                F.pad(torch.tensor(emb), (0, 0, 0, max_len - len(emb)))
                if len(emb) > 0
                else torch.zeros(max_len, emb_dim)
                for emb in merged_embeddings
            ]
        )
        merged_attention_mask = torch.stack(
            [
                F.pad(torch.tensor(am), (0, max_len - len(am)))
                if len(am) > 0
                else torch.zeros(max_len, dtype=torch.int)
                for am in merged_attention_mask
            ]
        ).long()
        merged_idf = torch.stack(
            [
                F.pad(torch.tensor(idf), (0, max_len - len(idf)))
                if len(idf) > 0
                else torch.ones(max_len)
                for idf in merged_idf
            ]
        )
        return merged_embeddings, merged_attention_mask, merged_idf

    def rindex(seq, el):
        return len(seq) - 1 - seq[::-1].index(el)

    def merge_chunked_embeddings(
        embeddingss: list[torch.Tensor], attention_masks: list, sequence_idss: list
    ) -> tuple[torch.Tensor, list[int], list[int]]:
        filtered_embeddings_indices = []
        filtered_attention_mask = []
        filtered_idf = []

        for chunk_i, (embeddings, attention_mask, sequence_ids) in enumerate(
            zip(embeddingss, attention_masks, sequence_idss)
        ):
            filtered_embeddings_indices.append([])

            # the stride is truncated from the left, so in intermediate chunks
            # there will only be an eos token, no bos token
            eos_index = rindex(sequence_ids, None)
            bos_index = sequence_ids.index(None)
            if eos_index == bos_index:
                bos_index = None

            for token_i in range(len(embeddings)):
                # When attention mask is 0, there is only padding left
                if attention_mask[token_i] == 0:
                    break

                # We want to mimic the process when getting bert embeddings in a single
                # forward pass. Therefore, we need to remove the special tokens from intermediate chunks
                # ==> Only keep bos in first chunk and eos in last chunk
                is_bos = token_i == bos_index
                is_eos = token_i == eos_index
                is_first_chunk = chunk_i == 0
                is_last_chunk = chunk_i == len(embeddingss) - 1
                if (is_bos and not is_first_chunk) or (is_eos and not is_last_chunk):
                    continue

                filtered_embeddings_indices[-1].append(token_i)
                filtered_attention_mask.append(attention_mask[token_i])
                # original implementation also used idf values to mask special tokens from similarity calc
                filtered_idf.append(0.0 if is_bos or is_eos else 1.0)

        filtered_embeddings = torch.cat(
            [
                embeddingss[chunk_i][relevant_indices]
                for chunk_i, relevant_indices in enumerate(filtered_embeddings_indices)
                if relevant_indices
            ]
        )

        return filtered_embeddings, filtered_attention_mask, filtered_idf

    encodings = tokenizer(
        all_sens,
        max_length=tokenizer.model_max_length,
        return_overflowing_tokens=True,
        stride=stride,
    )
    input_ids, attention_mask = pad_inputs(encodings)

    if batch_size == -1:
        batch_size = len(input_ids)

    embeddings = []
    model.eval()
    with torch.no_grad():
        for i in range(0, len(input_ids), batch_size):
            batch_start = i
            batch_end = i + batch_size
            emb = model(
                input_ids=input_ids[batch_start:batch_end],
                attention_mask=attention_mask[batch_start:batch_end],
            )
            embeddings.extend(emb[0])
    attention_mask = attention_mask.tolist()

    data_per_sample = defaultdict(list)
    for chunk_id, sample_id in enumerate(encodings.overflow_to_sample_mapping):
        # if this chunk is the first of its sample, there is no stride to truncate
        if sample_id not in data_per_sample:
            data = (
                embeddings[chunk_id],
                attention_mask[chunk_id],
                encodings.sequence_ids(chunk_id),
            )
        else:
            data = (
                embeddings[chunk_id][stride + 1 :],
                attention_mask[chunk_id][stride + 1 :],
                encodings.sequence_ids(chunk_id)[stride + 1 :],
            )
        data_per_sample[sample_id].append(data)

    merged_embeddings = []
    merged_attention_mask = []
    merged_idf = []

    for data in data_per_sample.values():
        emb, am, idf = merge_chunked_embeddings(
            [chunk_embeddings for chunk_embeddings, _, _ in data],
            [am for _, am, _ in data],
            [sids for _, _, sids in data],
        )
        merged_embeddings.append(emb)
        merged_attention_mask.append(am)
        merged_idf.append(idf)

    # need to pad and stack results because outer function expects a tensor
    merged_embeddings, merged_attention_mask, merged_idf = pad_results(
        merged_embeddings, merged_attention_mask, merged_idf
    )

    return merged_embeddings, merged_attention_mask, merged_idf


def greedy_cos_idf(
    ref_embedding,
    ref_masks,
    ref_idf,
    hyp_embedding,
    hyp_masks,
    hyp_idf,
    all_layers=False,
    sequential_chunk_size=128,
):
    # Check for invalid arguments for this patched implementation
    batch_size = ref_embedding.size(0)
    if batch_size != 1:
        raise ValueError("Batching not supported in patched implementation")

    if all_layers:
        raise ValueError("'all_layers' not supported in patched implementation")

    hyp_zero_mask = hyp_masks.sum(dim=1).eq(2)
    ref_zero_mask = ref_masks.sum(dim=1).eq(2)

    if torch.any(hyp_zero_mask):
        raise ValueError(
            "Empty candidate sentence detected. Not supported in patched implementation"
        )

    if torch.any(ref_zero_mask):
        raise ValueError(
            "Empty reference sentence detected. Not supported in patched implementation"
        )

    # Should be given by batch_size = 1
    is_zero_hyp_mask = hyp_masks.eq(0).sum().item() > 0
    is_zero_ref_mask = ref_masks.eq(0).sum().item() > 0
    if is_zero_hyp_mask or is_zero_ref_mask:
        raise ValueError("Masking not supported in patched implementation")

    ref_embedding.div_(torch.norm(ref_embedding, dim=-1).unsqueeze(-1))
    hyp_embedding.div_(torch.norm(hyp_embedding, dim=-1).unsqueeze(-1))

    # Parallel execution
    # sim = torch.bmm(hyp_embedding, ref_embedding.transpose(1, 2))

    # word_precision = sim.max(dim=2)[0]
    # word_recall = sim.max(dim=1)[0]

    # hyp_idf.div_(hyp_idf.sum(dim=1, keepdim=True))
    # ref_idf.div_(ref_idf.sum(dim=1, keepdim=True))
    # precision_scale = hyp_idf.to(word_precision.device)
    # recall_scale = ref_idf.to(word_recall.device)

    # P = (word_precision * precision_scale).sum(dim=1)
    # R = (word_recall * recall_scale).sum(dim=1)
    # F = 2 * P * R / (P + R)

    # Sequential / chunked execution
    word_precision = torch.zeros_like(hyp_idf)
    word_recall = torch.zeros_like(ref_idf)
    for start_idx in range(0, hyp_embedding.size(1), sequential_chunk_size):
        end_idx = min(start_idx + sequential_chunk_size, hyp_embedding.size(1))
        hyp_embedding_chunk = hyp_embedding[:, start_idx:end_idx, :]
        sim_chunk = torch.bmm(hyp_embedding_chunk, ref_embedding.transpose(1, 2))
        word_precision[:, start_idx:end_idx] = sim_chunk.max(dim=2)[0]
        word_recall = torch.max(word_recall, sim_chunk.max(dim=1)[0])

    hyp_idf.div_(hyp_idf.sum(dim=1, keepdim=True))
    ref_idf.div_(ref_idf.sum(dim=1, keepdim=True))
    precision_scale = hyp_idf.to(word_precision.device)
    recall_scale = ref_idf.to(word_recall.device)

    P = (word_precision * precision_scale).sum(dim=1)
    R = (word_recall * recall_scale).sum(dim=1)
    F = 2 * P * R / (P + R)

    F = F.masked_fill(torch.isnan(F), 0.0)

    return P, R, F
