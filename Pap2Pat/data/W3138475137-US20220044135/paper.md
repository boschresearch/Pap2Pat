# Introduction

In recent years, significant progress has been made in the field of open-domain question answering (Chen et al., 2017;Wang et al., 2017Wang et al., , 2018;;Clark and Gardner, 2018;Min et al., 2018;Asai et al., 2019). Very recently, some works turn to deal with a more challenging task of asking complex questions (Welbl et al., 2018;Clark et al., 2018;Yang et al., 2018) from the open-domain text corpus. In the open-domain scenario, one critical challenge raised by complex questions is that each question may require multiple pieces of evidence to get the right answer, while the evidence usually scatters in different passages. Examples in Figure 1 shows two types of questions that require evidence from multiple passages.

To deal with the challenging multi-evidence questions, an open-domain QA system should be able to (1) efficiently retrieve a small number of passages that cover the full evidence; and (2) accurately extract the answer by jointly considering the candidate evidence passages. While there have been several prior works in the latter direction (Wang et al., 2017;Clark and Gardner, 2018; Figure 1: Examples of complex questions involving two facts of a person. Different facts are color-coded. P# are all relevant passages, while only the ones with solid-line boxes are the true supporting passages. Lin et al., 2018), the solutions to the first problem still rely on traditional or neural information retrieval (IR) approaches, which solely measure the relevance between the question and each individual paragraph, and will highly possibly put the wrong evidence to the top.1 For example in Figure 1 (top), P1 and P2 are two candidate evidence passages that are closely related to the question but only cover the same unilateral fact required by the question, therefore leading us to the wrong answer Newton.

This paper formulates a new problem of complementary evidence identification for answering complex questions. The key idea is to consider the problem as measuring the properties of the selected passages, more than the individual relevance. Specifically, we hope the selected passages can serve as a set of spanning bases that supports the question. The selected passage set thus should satisfy the properties of (1)relevancy, i.e., they should be closely related to the question; (2) diversity, i.e., they should cover diverse information given the coverage property is satisfied; (3) compactness, i.e., the number of passages to satisfy the above properties should be minimal. With these three defined properties, we hope to both improve the selective accuracy and encourage the interpretability of the evidence identification. Note that complementary evidence identification in QA is different from Search Result Diversification (SRD) in IR on their requirement of compactness. The size of the selected set is constrained in QA tasks by the capability of downstream reasoning models and practically needs to be a small value, whereas it is not the case in SRD.

To achieve the above goals, a straightforward approach is to train a model that evaluates each subset of the candidate passages, e.g., by concatenating passages in any subsets. However, this approach is highly inefficient since it requires to encode O(K L ) passage subsets, where K is the total number of candidates and L is the maximum size of subsets. Thus, a practical complementary evidence identification method needs to be computationally efficient. This is especially critical when we use heavy models like ELMo (Peters et al., 2018) and BERT (Devlin et al., 2018), where passage encoding is time and memory consuming.

To this end, we propose an efficient method to select a set of spanning passages that is sufficient and diverse. The core idea is to represent questions and passages in a vector space and define the measures of our criterion in the vector space. For example, in the vector space, sufficiency can be defined as a similarity between the question vector and the sum of selected passage vectors, measured by a cosine function with a higher score indicating a closer similarity; and diversity can be defined as 1 distance between each pair of passages. By properly training the passage encoder with a loss function derived by the above terms, we expect the resulted vector space satisfies the property that the complementary evidence passages lead to large scores. In addition, our method only encodes each passage in the candidate set once, which is more efficient than the naive solution mentioned above. To evaluate the proposed method, we use the multi-hop QA dataset HotpotQA (the full wiki setting) since the ground-truth of evidence passages are provided.

Experiments show that our method significantly improves the accuracy of complementary evidence selection.

2 Proposed Method

## Task Definition

Given a question q and a mixture set of paragraphs P = P + ∪ P -with some paragraphs p ∈ P + relevant to q and some p ∈ P -irrelevant. Our goal is to select a small subset of paragraphs P sel ⊂ P, such that every p ∈ P sel satisfies p ∈ P + (relevancy), and all p ∈ P sel can jointly cover all the information asked by q (complementary). The off-the-shelf models select relevant paragraphs independently, thus usually cannot deal with the complementary property. The inner dependency among the selected P sel needs to be considered, which will be modeled in the remaining of the section.

## Model and Training

Vector Space Modeling We apply BERT model to estimate the likelihood of a paragraph p being the supporting evidence to the question q, denoted as P (p|q). Let q and p i denote the input texts of a question and a passage. We feed q and the concatenation of q and p i into the BERT model, and use the hidden states of the last layer to represent q and p i in vector space, denoted as q and p i respectively. A fully connected layer f (•) followed by sigmoid activation is added to the end of the BERT model, and outputs a scalar P (p i |q) to estimate how relevant the paragraph p i is to the question. Note that in our implementation p i is based on both q and p i , but we omit the condition on q for simplicity.

Complementary Conditions Previous works extract evidence paragraphs according to P (p|q), which is estimated on each passage separately without considering the dependency among selected paragraphs. To extract complementary evidence, we propose that the selected passages P sel should satisfy the following conditions that intuitively encourage each selected passage to be a basis to support the question:

• Relevancy: P sel should have a high probability of p i ∈P sel P (p i |q);

• Diversity: P sel should cover passages as diverse as possible, which can be measured by the average distance between any pairs in P sel , e.g., maximizing i,j∈{i,j|p i ,p j ∈P sel ,i =j} 1 (p i , p j ). Here

• Compactness: P sel should optimize the aforementioned conditions while the size being minimal. In this work we constrain the compactness by fixing |P sel | and meanwhile maximizing cos( i∈{i|p i ∈P sel } p i , q). We use cos(•, •) to encourage the collection of evidence covers what needed by the question.

# Training with Complementary Regularization

We propose a new supervised training objective to learn the BERT encoder for QA that optimizes the previous conditions. Note that in this work we assume a set of labeled training examples are available, i.e., the ground truth annotations contain complementary supporting paragraphs. Recently there was a growing in such datasets (Yang et al., 2018;Yao et al., 2019), due to the increasing interest in model explainability. Also, such supervision signals can also be obtained with distant supervision.

For each training instance (q, P), we define

Denoting y p i = 1 if p i ∈ P + and y p i = 0 if p i ∈ P -, we have the following training objective function:

L({pi}; q; y) = Lsup({pi}; q; y)

where

where α and β are the hyperparameter weights and 1 (•, •) denotes L1 loss between two input vectors. Eq 5 is the cross-entropy loss corresponding to relevance condition; Eq 6 regularizes the diversity condition; Eq 7 is the cosine-embedding loss 2 for the compactness condition and γ > 0 is the margin to encourage data samples with better question coverage.

2 Refer to CosineEmbeddingLoss in PyTorch.

## Inference via Beam Search

Score Function During inference, we use the following score function to find the best paragraph combination:

where α and β are hyperparameters similar to Eq 4. Note that our approach requires to encode each passage in P only once for each question, resulting in an O(K) time complexity of encoding (K = |P|); and the subset selection is performed in the vector space, which is much more efficient than selecting subsets before encoding.

Beam Search In a real-world application, there is usually a large candidate set of P, e.g., retrieved passages for q via a traditional IR system. Our algorithm requires O(K) time encoding, and O(K L ) time scoring in vector space when ranking all the combinations in L candidates. Thus when K becomes large, it is still inefficient even when L = 2.

We resort to beam search to deal with scenarios with large Ks. The details can be found in Appendix A.

3 Experiments

## Settings

Datasets Considering the prerequisite of sentence-level evidence annotations, we evaluate our approach on two datasets, a synthetic dataset MNLI-12 and a real application HotpotQA-50. Data sampling is detailed in Appendix B.

• MNLI-12 is constructed based on the textual entailment dataset MNLI (Williams et al., 2018), in order to verify the ability of our method in finding complementary evidence. In original MNLI, each premise sentence corresponds to three hypotheses sentences: entailment, neutral and contradiction.

To generate complementary pairs for each premise sentence, we split each hypothesis sentence into two segments. The goal is to find the segment combination that entails premise sentence, and our dataset, by definition, ensures that only the combination of two segments from the entailment hypothesis can entail the premise, not any of its subset or other combinations. The original train/dev/test splits from MNLI are used.

• HotpotQA-50 is based on the open-domain setting of the multi-hop QA benchmark HotpotQA (Yang et al., 2018). The original task requires to find evidence passages from abstract paragraphs of all Wikipedia pages to support a multi-hop question. For each q, we collect 50 relevant passages based on bigram BM25 (Godbole et al., 2019). Two positive evidence passages to each question are provided by human annotators as the ground truth. Note that there is no guarantee that P 50 covers both evidence passages here. We use the original development set from HotpotQA as our test set and randomly split a subset from the original training set as our development set.

## Settings

Baseline We compare with the BERT passage ranker (Nie et al., 2019) that is commonly used on open-domain QA including HotpotQA. The baseline uses the same BERT architecture as our approach described in Section 2.2, but is trained with only the relevancy loss (Eq 5) and therefore only consider the relevancy when selecting evidence.

We also compare the DRN model from (Harel et al., 2019) which is designed for the SRD task. Their ensemble system first finds the most relevant evidence to the given question, and then select the second diverse evidence using their score function. The major differences from our method are that (1) they train two separate models for evidence selection; (2) they do not consider the compactness among the evidences. It is worth mentioning that we replace their LSTM encoder with BERT encoder for fair comparison.

Metric During the evaluation we make each method output its top 2 ranked results3 (i.e. the top 1 ranked pair from our method) as the prediction. The final performance is evaluated by exact match (EM), i.e., whether both true evidence passages are covered, and the F1 score on the test sets.

## Results

In the experiments, we have M = 3, N = 4 for MNLI-12 and M = 4, N = 5 for HotpotQA-50 with our method. The values are selected according to development performance. We follow the settings and hyperparameters used in (Harel et al., 2019) for the DRN model. many pieces of true evidences enclosed by the complete set of candidate passages where our proposed ranker selects from. For HotpotQA dataset, we use a bi-gram BM25 ranker to collect top 50 relevant passages and build the basis for the experiments4 , which inevitably leads some of the true evidences to be filtered out and makes its upper-bound less than 100%. For the artificial MNLI-12 dataset, all the true evidences are guaranteed to be included.

Table 1 shows that our method achieves significant improvements on both datasets. On HotpotQA-50, all systems have low EM scores, because of the relatively low recall of the BM25 retrieval. Only 35.49% of the samples in the test set contain both ground-truth evidence passages. On MNLI-12, the EM score is around 50%. This is mainly because the segments are usually much shorter than a paragraph, with an average length of 7 words. Therefore it is more challenging in matching the q with the p i s. Specifically, both our method and the BERT baseline surpass the DRN model on all datasets and metrics, which results from our question-conditioned passage encoding approach. Our defined vector space proves beneficial to model the complementation among the evidence with respect to a given question. The ablation study of our loss function further illustrates that the diversity and the compactness terms efficiently bring additional 20%/30% increase in EM score on two datasets and consequently raise the F1 score by about 8/6 absolute points.

Figure 2 gives examples about how our model improves over the baseline. Our method can successfully select complementary passages while the baselines only select passages that look similar to the question. A more interesting example is given at the bottom where the top-50 only covers one supporting passage. The BERT baseline selects two incorrect passages that cover identical part of facts required by the question and similarly the DRN baseline select a relevant evidence and an irrelevant evidence, while our method scores lower the second passage that does not bring new information, and reaches a supporting selection. A similar situation contributes to the majority of improvement on one-supporting-evidence data sample in HotpotQA-50.

Inference Speed Our beam search with score function brings slight overheads to the running time. On HotpotQA-50, it takes 1,990 milliseconds (ms) on average to obtain the embeddings of all passages for one data sample whereas our vector-based complementary selection only adds an extra 2 ms which can be negligible compared to the encoding time.

## Future Work

The latest dense retrieval methods (Lee et al., 2019;Karpukhin et al., 2020;Guu et al., 2020) show promising results on efficient inference on the full set of Wikipedia articles, which allows to skip the initial standard BM25 retrieval and avoid the significant loss during the pre-processing step. Our proposed approach is able to directly cooperate with these methods as we all work in the vector space. Therefore, the extension to dense retrieval can be naturally the next step of our work.

# Conclusion

In the paper, we propose a new problem of complementary evidence identification and define the criterion of complementary evidence in vector space. We further design an algorithm and a loss function to support efficient training and inference for complementary evidence selection. Compared to the baseline, our approach improves more than 20% and remains to scale well to the computationally complex cases.  

# A Complementary Evidence Selection via Beam Search

For efficient inference when L = 2, we start to select the top-N (N K) most relevant passages. Then we score the combinations between each passage pair in the top-N set and another top-M set. This reduces the complexity from O(K 2 ) to O(M N ). M is a hyperparameter corresponding to the beam size. In a more general setting with L ≥ 2, we have an algorithm with the complexity of O((L -1)M N ) instead of O(K L ), which is shown in algorithm 1.

# Algorithm 1: Complementary Evidence Selection via Beam Search

Data: Vector representation of question (q), vector representation of all the N passages {pn} ({pn}); the maximum number of passage to select (L); the beam size (M ); a vector of weights for all regularization terms λ. Result: The top ranked complementary passages. * Predict the probability P (p i ) of being a supporting passage for each passage B Data Sampling  In original MNLI, each premise sentence P corresponds to one entailment EP , one neutral NP and one contradiction CP . We take the premise P as q, and split each of its corresponding hypotheses into two segments with a random cutting point near the middle of the sentence, resulting in a total of 6 segments {E 1 P , E 2 P , N 1 P , N 2 P , C 1 P , C 2 P }. Mixing them with the 6 segments corresponding to another premise X, we can finally have P + = {E 1 P , E 2 P } and

Consequently, we sample one positive and eight negative pairs respectively from P + and P -. A pair like {E 1 P , C 2 X } is considered as negative. To ensure the segments are literally meaningful, each segment is guaranteed to be longer than 5 words.

HotpotQA In HotpotQA, the true supporting paragraphs of each question q are given. Therefore, we can easily form P + and P -and sample positive and negative pairs of paragraphs respectively from P + and P -. A special pair that contains one true supporting paragraph and one non-supporting paragraph is considered as a negative pair.

