# Introduction

Semantic role labeling (SRL) is the task of identifying predicate-argument structures from a given sentence based on semantic frames and their roles (Jurafsky and Martin, 2008). It is a fundamental task for natural language understanding.

As shown in Fig. 1, SRL is typically decomposed into four sub-tasks: 1) predicate identification (e.g. issue); 2) sense disambiguation (e.g. issue.01); 3) argument identification for each predicate (e.g. a special edition); and 4) role classification of identified arguments (e.g. ARG1). A popular approach for SRL (Li et al., 2018) is to assume predicates are given and convert the argument prediction problem into a sequence tagging problem both for span and dependency type arguments. * b Work done while at IBM Research  Deep neural models achieve some of the best results in predicting semantic roles over standard benchmark datasets (He et al., 2017b;Tan et al., 2018a;Ouchi et al., 2018;Li et al., 2019;Kasai et al., 2019).Meanwhile, a very simple instancebased learning method, K-SRL (Akbik and Li, 2016a) has been shown strong performance using a distance function based on syntactic features. The semantic role of a candidate test word is determined by taking a majority vote of the labels of closest words present in a memory populated by words from the training set.

A natural question is whether one can apply such memory based methods with features derived from deep neural models. Memory based and memory adaptive learning methods have been successfully applied to language modeling and other problems e.g. the continuous cache model (Grave et al., 2016(Grave et al., , 2017)). The memory contains activations (e.g. from a RNN) observed during training and the associated labels. Sprechmann et al. (2018) propose an inference time memory based parameter adaptation method for language modeling. At each point during inference, they use its contextual representation to compute K nearest neighbors in the memory. The labels of the neighbors are then used to update the classification layer for final prediction.

In this paper, we propose a parameterized neighborhood memory adaptive (PNMA) method to exploit the information contained in the memory of activations. Our method proceeds in two phases.

• Memory Generation: We populate a mem-ory consists of each token representations from the training set and compute the K nearest neighbors for each token using Euclidean distance. We hypothesize and show empirically that the nearest neighbors contain valuable information about the correct label of w even when the base model prediction itself is wrong.

• PNMA: We then exploit the memory constructed earlier by computing a parameterized single vector representation n K (w) ∈ R d of the K nearest neighbors, which is then used to retrain the classification layers of the base model. Instead of a single representation h(w), the nearest neighbors define an ensemble of K representations close to h(w), which we combine using learned parameters into n K (w).

We show empirically that PNMA improves the performance of the base SRL model, both without and with the use of pretrained word embeddings. We further demonstrate that PNMA addresses the lowfrequency predicates in the training data and improves the base model prediction on low-frequency exceptions. Our best model combining PNMA and BERT achieves new state-of-the-art F1 scores on both datasets (for a single model), with a 2.0 point increase over existing methods on the outof-domain Brown test set in CoNLL2005 and 5.0 point increase on CoNLL2009.

In the rest of the paper, we describe the PNMA model in Sec. 2 and demonstrate its efficacy with extensive empirical evaluation in Sec. 3 and analysis in Sec. 4. We then review the existing literature in Sec. 5 and conclude in Sec. 6.

# Model

We formulate SRL as a sequence tagging problem both for span and dependency type arguments (Ouchi et al., 2018). For datasets with span style arguments, we convert the semantic role to BIO tags. We assume that the input to the model is a sentence S with n tokens. Knowing the predicate position in a sentence is previously known to improve the performance of argument classification (Li et al., 2018). Since all benchmark datasets have the marked predicate position, we use this information and assume that each token is tagged with a 0/1 bit indicating the predicate word. Our proposed method takes the base model representation for populating the memory.

## Base Model for SRL

We use an Alternating LSTM (He et al., 2017b;Ouchi et al., 2018) that has been successfully used for SRL as the base model. As shown in Fig. 2, the base model has the following main components. Word Embeddings: Word embeddings are the numerical vector representations of the textual words. Contextualized word embeddings derived from pretrained language models such as ELMo (Peters et al., 2018) and BERT (Devlin et al., 2018) (Zhou and Xu, 2015a), which produces predictions for each token. The CRF layer is trained end-to-end with the other layers.

## Parameterized Neighborhood Memory

Adaptive (PNMA) Model

After we train a strong multilayer LSTM base model on the SRL dataset, in the first phase we generate the memory of activations and in the second phase we compute the parameterized vector representations of each token and retrain the classification layers of base model. Here we describe the two phases of our proposed model in detail.

### Phase 1: Memory Generation

Intuition: We hypothesize that the K nearest neighbors contain valuable information about the correct label of w even when h L (w) itself leads to an incorrect prediction. To test this hypothesis, we train a base SRL model on the CoNLL2005 training set (see details in Section 3) and compute the predicted labels for the sentences in the validation set. For each token w with a wrong predicted label, we compute its K = 64 nearest neighbors and find the rank (in order of increasing distance) of the first token with the correct label (of w ) among the neighbors. The distribution of these ranks, as shown in Fig. 3, is highly left skewed. Almost all tokens labeled incorrectly by the base model have a close neighbor in memory that has the correct label. The corresponding distribution for tokens correctly labeled by the base model is even more left skewed. However, it is not clear a-priori which neighbor of w should we trust. This observation motivates the second phase of training. Memory Generation: We use the trained base model to populate a memory M with activations h L (w) produced by the final LSTM layer on words 

) is a dense representation of the separation between w and its i-th nearest neighbor. The inner product with n i followed by the softmax computes a distribution over the neighbors {η i } K i=1 , which is then used to compute a compact weighted representation of N K (w).

The former is the representation of w produced by the base model, while the latter is derived from an ensemble of K representations that are close to h L (w) in M . By making n K (w) a function of |m i (w)-h L (w)| and learnable parameters, we aim to extract the most relevant information in N K (w).

We note that we observed consistently better performance by using a distinct n i for each neighbor instead of a single vector for all neighbors.

## PNMA Training

In the second training phase, we freeze the parameters associated with the LSTM, connection and embedding layers in the base model and update the neighborhood parameters {n i } K i=1 and the parameters in the classification and CRF layers using n K (w) and the label of w in the training set. We did not observe benefits by using h L (w) itself in the second training phase. At test time, we obtain the SRL label predictions by computing n K (w) for each token w in the test sentence, which itself requires the computation of N K (w) using the LSTM representations of w and M .

The updated base model after the second phase of training is the final SRL model, which we call the Parameterized Neighborhood Memory Adaptive (PNMA) model. By parameterizing the representation of N K (w) and retraining, we allow our model to make optimal use of the nearest neighbors of w in M . In contrast to Akbik and Li (2016a), we do not use handcrafted features or distance functions. Compared to Sprechmann et al. (2018), we do not update the classification and CRF layers for each token or sentence separately.

# Experiments

## Experimental Setup

Datasets: We evaluate PNMA on both span style and dependency style Propbank semantic parsing datasets. For span style SRL evaluation we present results on the CoNLL2005 shared task (Carreras and Màrquez, 2005) and the CoNLL2012 (Pradhan et al., 2012) datasets. We evaluate PNMA on the English subset of CoNLL2009 (Hajič et al., 2009) shared task dataset to present the applicability of PNMA to dependency style SRL datasets. Key statistics of these datasets is in Appendix A.

For the dependency SRL task, we follow the work of Marcheggiani and Titov (2017a) and use the off-the-shelf disambiguator for predicate sense disambiguation (Roth and Lapata, 2016). Word Embeddings: We experiment with randomly initialized embeddings and publicly available pretrained contextualized embeddings from ELMo and BERT (the large cased model). In both cases, we use a scaled convex combination of embeddings e CE i (w) produced by layer i of the underlying language model. Training Specifics: We use embeddings of size 50 to map the 0/1 predicate indicators. Each LSTM layer has a hidden dimension of 300. We largely follow the training procedure outlined in Ouchi et al. (2018). We optimize the loss function with the Adam optimizer (Kingma and Ba, 2015) for 100 epochs, with an initial learning rate of 1e-3, which is decreased by half after epoch 50 and 75. A L2 weight decay of 1e-4 is used for regularization.

We apply a dropout of δ l ∈ {0.05, 0.1, 0.15} after each LSTM layer and a dropout of δ e ∈ {0.45, 0.5, 0.55} after the word embedding layer. We use 1024 dimensions for randomly initialized word embeddings, the same as ELMo and BERT. For the memory adaptive training phase, we compute K = 64 neighbors for each token and train for 20 epochs with a constant learning rate of 4e-4. For both the datasets, we populate a memory M with 15% of the tokens in the respective training sets. We did not observe significant performance differences by increasing memory size beyond this.

## Results

We evaluate our models using the official CoNLL SRL evaluation scripts. For a span style dataset we use the CoNLL 2005 SRL evaluation script and for a dependency SRL dataset we use the CoNLL 2009 SRL evaluation script. The results are averaged over five runs of model training with random seeds, as summarized in Table 1. We show results for the base models trained with randomly initialized word embeddings (Base-Rand in the table) and those with ELMo (Base-ELMo) and BERT (Base-BERT) embeddings and the gains obtained by using PNMA in each case. Span SRL Result: For CoNLL2005, the use of PNMA improves validation and in-domain WSJ test F1 scores for all cases, albeit by varying margins, ranging from 0.1 to 0.6 F1 points. In particular, we observe the highest gains of 0.9, 0.7 and 0.3 F1 points on the out-of-domain Brown test set for the three respective models. The consistent improvements confirm the effectiveness of our proposed PNMA model by exploiting information in the nearest neighbors of tokens in M . Coupled with the strong performance of Base-BERT, the Base-BERT+PNMA model improves upon syn- Although our model works independent of any kind of syntactic information, we also compare PNMA with models that are syntax aware and find that it is very competitive with syntax aware SRL models. This observation is important since syntax aware models assume the availability of a state-ofthe-art syntactic parser which is not always available, and may be challenging to obtain for new domains or languages.

The results for the CoNLL2012 dataset are also shown in Table 1. Here again, PNMA results in gains across the board with the best results achieved by Base-BERT+PNMA, improving upon the current state of the art by 0.3 and 0.4 F1 points for the validation and test sets. Dependency SRL Results: In Table 2 we present the PNMA results on the CoNLL2009 dataset and compare it with the state-of-the-art syntax aware and syntax agnostic SRL models. When compared to syntax agnostic models we observe a significant performance gain of 5.2 absolute F1 points on the out-of-domain Brown set. The results also show that PNMA is very competitive when compared with syntax aware models. Irrespective of whether the model is syntax agnostic or syntax aware, we obtain new state-of-the-art on the out-of-domain Brown set. Here again, we observe the performance gain with the PNMA over the base models.

Since we use an off-the-shelf sense disambiguator for all the experiments, we also present the results on argument classification alone in Table 2 (that is we do not evaluate the predicate sense disambiguation following (Marcheggiani and Titov, 2017b)) to show the actual performance gain by PNMA. In all the regimes PNMA outperforms the corresponding base model predictions. Computation Overhead: Depending on the size of M , the time required to compute N K (w) may vary. We utilize GPUs to do fast batched computation of distances which results in less than 10% overhead compared to training the base model with BERT. Since the LSTM layers are frozen, the second phase is significantly faster than the first.

# Analysis

We analyze factors that may impact the effectiveness of PNMA models. We focus on the models where PNMA alters the base model predictions the most: the Base-ELMo model for CoNLL20051 and the Base-Bert model for CoNLL2009 2 .  

## Role Level Analysis

We first analyze how the effectiveness of PNMA differ across individual argument role labels. Fig. 4 shows a heatmap produced by plotting the difference between the confusion matrices of Base-ELMo+PNMA and Base-ELMo on the Brown test set in CoNLL2005. As can be seen, PNMA improves the prediction of role labels for almost all types in various degrees, except for LOC. In particular, PNMA considerably improves the prediction of the core role A2, mainly by reducing misclassification to A1 and LOC. Similarly, it evidently improves the prediction of A1 by reducing misclassification to A0, A2 and LOC. However, its somewhat poorer performance on the prediction for LOC indicts slight over-correction of misclassification to LOC. Among adjunct roles, ADV benefits the most from PNMA thanks to reduced confusion with DIR, MOD and A2. We lists example instances from the CoNLL2005 datasets where PNMA corrects the base model's predictions in Appendix B.

We further analyze how PNMA leads to better prediction of argument role labels. Taking the core role A2 as an example. As pointed out in He et al. (2017b), A2 shows semantic relations with the adjuncts such as location and direction, often leading to confusion in base model. For instance, for the sentence "His father would come upstairs and stand at the foot of the bed and look at his  son", the span at the foot of the bed is classified as LOC by our base model. However, PNMA is able to correctly classify this span with the help of the nearest neighbors (Table 3), which contains the valuable information about the correct label and hence improves this confusion over base model.

## Instance Level Analysis

For all the datatsets, it is almost four times more likely for PNMA to change a wrong prediction of the base model into a correct prediction than it is for it to change a correct prediction of the base model into a wrong prediction. Furthermore, focusing on the the samples where PNMA's prediction differs from that of the base model, we find that in most cases PNMA's prediction is correct: for the CoNLL2005(CoNLL2009) datasets, out of the cases where the models disagree, PNMA is correct in 68%(48%) whereas the base model is correct in only 20%(12%) (both are wrong for the rest of these disagreement cases). This shows that the nearest neighbors indeed contain valuable information about the correct label of the test token even when the base model prediction itself is wrong. Fig. 5 plots the two dimensional representation of a test sample for each scenario, before and after applying PNMA along with the computed nearest neighbors: 1) the base model argument role prediction is wrong; PNMA corrects it in Fig. 5a; 2) the base model argument role prediction is wrong; PNMA does not alter it in Fig. 5b; 3) the base model argument role prediction is correct; PNMA fails to alter it in Fig. 5c; 4) the base model argument role prediction is correct; PNMA alters it to a wrong prediction in Fig. 5d.

As can be seen in Figs. 5a and5c, PNMA effectively moves the base model's representation of the test sample to an area that is denser in examples with the correct label. In this area, the likelihood of the classifier to predict the correct label is higher. Thus, PNMA enables to correct wrong labels. In Fig. 5b the correct label is B-A4, but all neighbors are of other labels and hence both models are wrong. There are around 10% of the total samples that lie in this category. Our investigation reveals that most of these samples are not well represented in the memory similar to the situation shown for the example in column (d). That is, for these instances there are a very small number of samples in the neighborhood which have the same label as that of the true label of the current instance. Low-Frequency Exceptions: As noted in Akbik and Li (2016a), low-frequency exceptions are important in many real use cases, in which argument roles may be context specific and hence difficult to learn by generalization from the entire training data. Fig. 6 shows how the number of samples on which PNMA disagrees with the base model varies by predicate frequency in the training data. As can be seen, the disagreement between PNMA and the base model is higher in low-frequency predicates. As noted above, when the two models disagree, PNMA is correct most of the time for both CoNLL2005 and CoNLL2009. This observation confirms the effectiveness of PNMA in addressing low-frequency exceptions, similar to instancelearning based K-SRL (Akbik and Li, 2016a).

## Error Analysis

For PNMA to work, two conditions must be met. First, there should be samples in the neighborhood of the test sample whose gold label matches that of the test sample. Second, enough of those neighboring samples should have representations that results in correct label predictions so as to help PNMA translate the test sample representation to an area which results in a correct label.

To investigate further, we analyze the predictions of the model as a function of the number of neighborhood samples and the predicate frequency, as shown in Fig. 6. These plots show that the PNMA model mostly improves the samples associated with low-frequency predicates and which have moderate representation in the memory, i.e. intermediate number of neighborhood samples (10-40). However, there are some samples that lie in moderate predicate frequency and moderate neighborhood sample regime which are predicted wrong by both models. Although these samples do have a good amount of neighbors that belong to the same category as that of the true label, they are still wrongly predicted by the PNMA model. This is because some of these neighbors have a wrong prediction by the base model, which means that the base model representation in the memory is such that it leads to a wrong prediction. When many neighbors have such representations, PNMA will translate the test sample representation into an area which will result in a wrong prediction. This possibly cause the PNMA to misclassify the arguments roles which are correctly classified by the base model. Therefore, to further improve our method, better memory generation techniques are required to cover such cases. This will be explored in future work.

# Related Work

Recently, a great attention is paid on the use of deep neural network for the semantic role labeling task (Tan et al., 2018b;He et al., 2018a). These networks largely fall into two broad categories: syntaxagnostic and syntax-aware. Syntax-aware models are known to perform better on SRL task (Roth and Lapata, 2016;He et al., 2017a;Strubell et al., 2018a) and for a long time syntax was considered a prerequisite for better SRL performance (Pun-yakanok et al., 2008;Gildea and Jurafsky, 2002). These performance gains are due to the availability of high-quality syntax parser (Marcheggiani and Titov, 2017a;Li et al., 2018). However, several works (Zhou and Xu, 2015b;Marcheggiani et al., 2017;Tan et al., 2018b;He et al., 2018a) show that the deep networks can extract useful discriminatory features even without the syntactic information.

Span based SRL, formulated as a sequence tagging problem (Villodre et al., 2005), lends itself to end-to-end deep learning models (Zhou and Xu, 2015a). Using more sophisticated encoders such as LSTMs and Transformers has lead to improved accuracy (He et al., 2017b;Tan et al., 2018a;Zhao et al., 2018;Strubell et al., 2018b). An alternate method of directly predicting the spans also achieves comparable results (He et al., 2018b;Ouchi et al., 2018). In general, context sensitive word embeddings such as ELMo and BERT leads to better performance.

Our model using memory adaptation is inspired by the success of similar techniques in neural models for language modeling e.g. neural cache (Grave et al., 2016(Grave et al., , 2017) ) and memory based methods for few-shot learning (Sprechmann et al., 2018;Rae et al., 2018). These methods shown to capture the more long range dependencies. Recently, (Guan   (Guan et al., 2019) in the sense that in PNMA nearest neighbors don't need to be labeled and hence can be applied to large unlabeled corpora.

# Conclusion

To conclude, we propose a Parameterized Neighborhood Memory Adaptive (PNMA) method to exploit information contained in the nearest neighbors of token representations derived from deep LSTM models for SRL. Combined with contextualized word embeddings from BERT, we achieve new state-of-the-art results for single models on both span and dependency style datasets. Our experimental results indicate that PNMA improves over various argument roles and correct most of the sample where PNMA disagree with the base model. For the samples predicted wrongly by both models, we plan to investigate in the future better form of memory or multi-layered representations in the base model to compute better neighborhoods to better handle such cases.

# A Dataset

The key statistic of the datasets is shown in Table 4. For both the span style datasets we convert the semantic predicates and arguments roles to BIO boundary-encoded tags. There are 28 and 42 distinct role types in CoNLL 2005 and CoNLL2012 datasets which were converted to 126 and 129 distinct BIO tags, respectively.

# B PNMA Corrections

Here we lists the example instances from the CoNLL2005 datasets where PNMA corrects the base model's predictions. PNMA improves the prediction of role labels for almost all types in various degrees. In particular, PNMA considerably improves the prediction of the core roles.

Base → PNMA

# S1

I can fix him something later in the afternoon when we get home . A1 → A2 I can fix him something later in the afternoon when we get home .

A2 → A1

# S2

The patrol snaked around in back of the cave , approached it from above and dropped in suddenly with wild howls . A1 → A2

# S3

" Will you please wait in here " .

# AM-MOD → AM-ADV S4

The fear of punishment just did not bother him . AM-DIS → AM-ADV 

