# Introduction

Deep neural networks (DNNs) trained on large datasets provide state-of-the-art results on various NLP problems (Devlin et al., 2019) including text classification (Howard and Ruder, 2018). However, the cost and time needed to get labeled data and to train models is a serious impediment to creating new and/or better models. This problem can be mitigated by creating smaller representative datasets with active learning which can be used for training DNNs to achieve similar test accuracy as that using the full training dataset . In other words, the smaller sample can be considered a surrogate for the full data.

However, there is lack of clarity in the active learning literature regarding sampling bias in such surrogate datasets created using active learning (Settles, 2009): its dependence on models, functions and parameters used to acquire the sample. Indeed, what constitutes a good sample? In this paper, we perform an empirical investigation using active text classification as the application.

Early work in active text classification (Lewis and Gale, 1994) suggests that greedy query generation using label uncertainty may lead to efficient representative samples (Nonetheless, the same test accuracy). Subsequent concerns regarding sampling bias has lead to explicit use of expensive diversity measures (Brinker, 2003;Hoi et al., 2006) in acquisition functions or using ensemble approaches (Liere and Tadepalli, 1997;McCallum and Nigam, 1998) to improve diversity implicitly.

Deep active learning approaches adapt the discussed framework above to train DNNs on large data. However, it is not clear if the properties of deep approaches mirror those of their shallow counterparts and if the theory and the empirical evidence regarding sampling efficiency and bias translates from shallow to deep models. For example, (Sener and Savarese, 2018) and (Ducoffe and Precioso, 2018) find that uncertainty based strategies perform no better than random sampling even if ensembles are used and using diversity measures outperform both. On the other hand, (Beluch et al., 2018;Gissin and Shalev-Shwartz, 2019) find that uncertainty measures computed with ensembles outperform diversity based approaches while (Gal et al., 2017;Beluch et al., 2018;Siddhant and Lipton, 2018) find them to outperform uncertainty measures computed using single models. A recent empirical study (Siddhant and Lipton, 2018) investigating active learning in NLP suggests that Bayesian active learning outperforms classical uncertainty sampling across all settings. However, the approaches have been limited to rel-arXiv:1909.09389v1 [cs.CL] 20 Sep 2019 atively small datasets.

## Sampling Bias in Active Classification

In this paper, we investigate the issues of sampling bias and sample efficiency, the stability of the actively collected query and train sets and the impact of algorithmic factors -i.e. the setup chosen while training the algorithm, in the context of deep active text classification on large datasets. In particular, we consider two sampling biases: label and distributional bias, three algorithmic factors: initial set selection, query size and query strategy along with two trained models and four acquisition functions on eight large datasets.

To isolate and evaluate the impact of the above (combinatorial) factors, a large experimental study was necessary. Consequently, we conducted over 2.3K experiments on 8 popular, large, datasets of sizes ranging from 120K-3.6M. Note that the current trend in deep learning is to train large models on very large datasets. However, the aforementioned issues have not yet been investigated in the literature in such a setup. As shown in Table 1, the datasets used in latest such analysis on active text classification by (Siddhant and Lipton, 2018) are quite small in comparison. The datasets used by us are two orders of magnitude larger, our query samples often being the size of the entire datasets used by previous works, and the presented empirical study is more extensive (20x experiments).

Our findings are as follows:

(i) We find that utilizing the uncertainty query strategy using a deep model like FastText.zip (FTZ)1 to actively construct a representative sample provides query and train sets with remarkably good sampling properties.

(ii) We finds that a single deep model (FTZ) used for querying provides a sample set similar to more expensive approaches using ensemble of models. Additionally, the sample set has a large overlap with support vectors of an SVM trained on the entire dataset largely invariant to a variety of algorithmic factors, thus indicating the robustness of the acquired sample set.

(iii) We demonstrate that the actively acquired training datasets can be utilized as small, surrogate training sets with a 5x-40x compression for training large, deep text classification models. In particular, we can train the ULMFiT (Howard and Ruder, 2018) model to state of the art accuracy at 25x-200x speedups.

(iv) Finally, we create a novel, state-of-the-art baseline for active text classification which outperforms recent work (Siddhant and Lipton, 2018), using Bayesian dropout, utilizing 4x less training data. We also outperform (Sener and Savarese, 2018) at all training data sizes. The latter uses an expensive diversity based query strategy (coreset sampling).

The rest of the paper is organized as follows: in Section 2, the experimental methodology and setup are described. Section 3 presents the experimental study on sampling biases as well as the impact of various algorithmic factors. In Section 4, we compare with prior literature in active text classification. Section 5 presents a downstream use case -fast bootstrapping of the training of very large models like ULMFiT. Finally, we discuss the current literature in light of our work in Section 6 and summarize the conclusions in Section 7.

# Methodology

This section describes the experimental approach and the setup used to empirically investigate the issues of (i) sampling bias and (ii) sampling efficiency in creating small samples to train deep models.

## Approach

A labelled training set is incrementally built from a pool of unlabeled data by selecting & acquiring labels from an oracle in sequential increments. In this, we follow the standard approach found in the active learning literature. We use the following terminology:

Queries & Query Strategy: We refer to the (incremental) set of points selected to be labeled and added to the training as the query and the (acquisition) function used to select the samples as the query strategy.

Pool & Train Sets: The pool is the unlabeled data from which queries are iteratively selected, labeled and added to the (labeled) train set.

Let D S = (x i , y i ) denote a dataset consisting of |S| = n i.i.d samples of data/label pairs, where |.| denotes the cardinality. Let S 0 ⊂ S denote an initial randomly drawn sample from the initial pool. At each iteration, we train the model on the current train set and use a model-dependent query strategy to acquire new samples from the pool, get them labeled by an oracle and add them to the train set. Thus, a sequence of training sets: [S 1 , S 2 . . . , S b ] is created by sampling b queries from the pool set, each of size K. The b queries are given by

In this paper, we investigate the efficiency and bias of sample sets S 1 b , S2 b , . . . , S t b obtained by different query strategies Q 1 , Q 2 , . . . Q t . We exclude the randomly acquired initial set and perform comparisons on the actively acquired sample sets defined as Ŝi j = (S i j -S i 0 ).

## Experimental Setup

In this section, we share details of the experimental setup, and present and explain the choice of the datasets, models and query strategies used. Datasets: We used eight, large, representative datasets widely used for text classification: AG-News (AGN), DBPedia (DBP), Amazon Review Polarity (AMZP), Amazon Review Full (AMZF), Yelp Review Polarity (YRP), Yelp Review Full (YRF), Yahoo Answers (YHA) and Sogou News (SGN). Please refer to Section 4 of (Zhang et al., 2015) for details regarding the collection and characteristics of these datasets. Table 1 provides a comparison regarding the choice of datasets, models and number of experiments between our study and (Siddhant and Lipton, 2018) which investigates a variety of NLP tasks including text classification while we focus only on the latter.

Models: We reported two text classification models as representatives of classical and deep learning approaches respectively which were fast to train and also had good performance on text classification: Multinomial Naive Bayes (MNB) with TF-IDF (Wang and Manning, 2012) and Fast-Text.zip (FTZ) (Joulin et al., 2016). The FTZ model provides results competitive with VDC-NNs (a 29 layer CNN) (Conneau et al., 2017) but with over 15,000× speedup (Joulin et al., 2017). This allowed us to conduct a thorough empirical study on large datasets. Multinomial Naive Bayes (MNB) with TF-IDF features is a popularly claimed baseline for text classification (Wang and Manning, 2012).

Query Strategies: Uncertainty based query strategies are widely used and well studied in the active learning literature. cally use a scoring function on the (softmax) output of a single model. We evaluate the following ones: Least Confidence (LC) and Entropy (Ent). Independently training ensembles of models (Lakshminarayanan et al., 2017) is another principled approach to obtain uncertainties associated with the output estimate.Then, we tried four query strategies -LC and Ent computed using single and ensemble models and evaluated them against random sampling (chance) as a baseline. For ensembles, we used five FTZ ensembles (Lakshminarayanan et al., 2017). In contrast, (Siddhant and Lipton, 2018) used Bayesian ensembles using Dropout, proposed in (Gal et al., 2017). Please refer to Section 4 for a comparison.

Implementation Details: We performed 2304 active learning experiments. We obtained our results on three random initial sets and three runs per seed (to account for stochasticity in FTZ) for each of the eight datasets. The query sizes were 0.5% of the dataset for AGN, AMZF, YRF and YHA and 0.25% for SGN, DBP, YRP and AMZP respectively for b = 39 sequential, active queries. We also experimented with different query sizes keeping the size of the final training data b × K constant. The default query strategy uses a single model with output Entropy (Ent) unless explicitly stated otherwise. Results in the chance column are obtained using random query strategy.

We used Scikit-Learn (Pedregosa et al., 2011) implementation for MNB and original implementation for FastText.zip (FTZ) 2 . We required 3 weeks of running time for all FTZ experiments on a x1.16xlarge AWS instance with Intel Xeon E7-8880 v3 processors and 1TB RAM to obtain results presented in this work. The experiments are deterministic beyond the stochasticity involved in Dsets Limit FTZ (∩Q) MNB (∩Q) FTZ (∩S) MNB (∩S) SGN 1.61 1.56 ± 0.03 1.15 ± 0.32 1.59 ± 0.01 1.57 ± 0.01 DBP 2.64 2.50 ± 0.02 2.27 ± 0.11 2.51 ± 0.0 2.58 ± 0.01 YHA 2.30 2.25 ± 0.01 2.22 ± 0.02 2.25 ± 0.0 2.28 ± 0.0 YRP 0.69 0.69 ± 0.0 0.56 ± 0.13 0.69 ± 0.0 0.69 ± 0.01 YRF 1.61 1.56 ± 0.02 1.42 ± 0.21 1.56 ± 0.0 1.57 ± 0.01 AGN 1.39 1.33 ± 0.04 1.13 ± 0.17 1.33 ± 0.0 1.35 ± 0.01 AMZP 0.69 0.69 ± 0.0 0.69 ± 0.0 0.69 ± 0.0 0.69 ± 0.0 AMZF 1.61 1.58 ± 0.02 1.6 ± 0.01 1.59 ± 0.0 1.61 ± 0.0   Table 2: Label entropy with a large query size (b = 9 queries). ∩Q denotes averaging across queries of a single run, ∩S denotes the label entropy of the final collected samples, averaged across seeds. Naive Bayes (∩Q) has biased (inefficient) queries while FastText (∩Q) shows stable, high label entropy showing a rich diversity in classes despite the large query size. Overall, the resultant sample (∩S) becomes balanced in both cases.

training the FTZ model, random initialization and SGD updates. The entire list of hyperparameters and metrics affecting uncertainty such as calibration error (Guo et al., 2017) is given in the supplementary material. The experimental logs and models are available on our github link3 .

# Results

In this section, we study several aspects of sampling bias (class bias, feature bias) and the impact of relevant algorithmic factors (initial set selection, query size and query strategy.

We evaluated the actively acquired queries and sample set for sampling bias, and for the stability as measured by %intersection of collected sets across a critical influencing factor. Higher sample intersections indicate more stability increase to the chosen influencing factor.

## Aspects of Sampling Bias

We study two types of sampling biases: (a) Class Bias and (b) Feature Bias.

### Class Bias

Greedy uncertainty based query strategies are said to pick disproportionately from a subset of classes per query (Sener and Savarese, 2018;Ebert et al., 2012), developing a lopsided representation in each query. However, its effect on the resulting sample set is not clear. We test this by measuring the Kullback-Leibler (KL) divergence between the ground-truth label distribution and the distribution obtained per query as one experiment (∩Q), and over the resulting sample (∩S) as the second. Let us denote P as the true distribution of labels, P the sample distribution and C the total number of classes. Since P follows a uniform distribution, we can use Label entropy instead (L = -KL(P || P ) + log(C)). Label entropy L is an intuitive measure. The maximum label entropy is reached when sampling is uniform, P (x) = P (x), i.e. L = log(C).

We present our results in Table 15. We observe that across queries (∩Q), FTZ with entropy strategy has a balanced representation from all classes (high mean) with a high probability (low std) while Multinomial Naive Bayes (MNB) results in more biased queries (lower mean) with high probability (high std) as studied previously. However, we did not find evidence of class bias in the resulting sample (∩S) in both models: Fast-Text and Naive Bayes (column 5 and 6 from Table 15).

We conclude that entropy as a query strategy can be robust to class bias even with large query sizes.

### Feature Bias

Uncertainty sampling can lead to undesirable sampling bias in feature space (Settles, 2009) by repeating redundant samples and picking outliers (Zhu et al., 2008). Diversity-based query strategies (Sener and Savarese, 2018) are used to address this issue, by selecting a representative subset of the data. In the context of active classification, it is good to pick the most informative samples to be the ones closer to class boundaries4 . Indeed, recent work suggests that the learning in deep classification networks may focus on small part of the data closer to class boundaries, thus resembling support vectors (Xu et al., 2018;Toneva et al., 2019). To investigate whether uncertainty sampling also exhibits this behavior, we perform below a direct comparison with support vectors from a SVM. For this, we train a FTZ model on the full training data and train a SVM on the resulting features (sentence embeddings) to obtain the support vectors and compute the intersection of support vectors with each selected set. The percentage intersections are shown in Table 3. The high percentage overlap is a surprising result which shows that the sampling is indeed biased but in  a desirable way. Since the support vectors represent the class boundaries, a large percentage of selected data consists of samples around the class boundaries. This overlap indicates that the actively acquired training sample covers the support vectors well which are important for good classification performance. The overlap with the support vectors of an SVM (a fixed algorithm) also suggests that uncertainty sampling using deep models might generalize beyond FastText, to other learning algorithms.

Experimental Details: We used a fast GPU implementation for training an SVM with a linear kernel (Wen et al., 2018) with default hyperparameters. Please refer to supplementary material for additional details. We ensured the SVM achieves similar accuracies as original FTZ model.  Chance). NaiveBayes shows significant dependency on the initial set sometimes, while other times performs comparable to FastText.

## Algorithmic Factors

We analyze three algorithmic factors of relevance to sampling bias: (a) Initial set selection (b) Query size, and, (c) Query strategy.

### Initial Set Selection

To investigate the dependence of the actively acquired train set on the initial set, we compare the overlap (intersection) of the incrementally constructed sets from different random initial sets versus the same initial set. 3 and 5 present overlaps from different initial sets while 4 and 6 from same initial sets. We note from column 4 and 6 that due to the stochasticity of training in FTZ, we expect non-identical final sets even with same initial samples as well. The results demonstrate that samples obtained using FastText are largely initialization independent (low variation between columns 3 and 4) consistently across datasets while the samples obtained with Naive Bayes can be vastly different showing relatively heavy dependence on the initial seed. This indicates the relative stability of train set obtained with the posterior uncertainty of the actively trained FTZ as an acquisition function.

### Query size

Since the sampled data is sequentially constructed by training models on previously sampled data, large query sizes were expected to impact samples collected by uncertainty sampling and the performance thereof (Hoi et al., 2006). We experiment with various query sizes -(0.25%, 0.5%, 1%) for DBP, SGN, YRP and AMZP and (0.5%, 1%, 2%) for the rest corresponding to 9, 19 and 39 iterations. Figure 1 shows that FastText (top row) has very stable performance across sample sizes while MNB (bottom row) show more erratic performance. Table 5 presents the intersection of samples obtained with different query sizes across multiple runs. We observe a high overlap of the acquired samples across different query sizes indicating that the performance is independent of the query size (compare column 3 to column 4 where the size is held constant) while MNB results in lower overlap with more erratic behavior due to change in the query size (compare column 5 compared to column 6).

### Query strategy

We now investigate the impact of various query strategies using FastText by evaluating and comparing the correlation between the respective actively selected sample sets. Acquisition Functions: We compare four uncertainty query strategies: Least Confidence (LC) and Entropy (Ent), with and without deletion of least uncertain samples from the training set. Deletion of least uncertain samples reduces the dependence on the initial randomly selected set. The results are presented in Table 14. We present five Table 7: Intersection of query strategies across single and ensemble of 5FTZ models. We observe that the % intersection of samples selected by ensembles and single models is comparable to intersection among either. The 5-model committee does not seem to add any additional value over selection by a single model.

of the ten possible combinations and again observe the high degree of overlap in the collected samples. It can be concluded that the approach is fairly robust to these variations in the query strategy.

Ensembles versus Single Models: A similar experiment was conducted to investigate the overlap between a single FTZ model and a probabilistic committee of models (5-model ensemble with FTZ (Lakshminarayanan et al., 2017)) to identify comparative advantages of using ensemble methods. The results are presented in Table 7 showing little to no difference in sample overlaps. 5 We conclude that more expensive sampling strategies commonly used, like ensembling, may offer little benefit compared to using a single FTZ model with posterior uncertainty as a query function.

The experiments in this section demonstrate that uncertainty based sampling using deep models like FTZ show no class bias or an undesirable feature bias (and favorable bias to class boundaries). There is also a high degree of robustness to algorithmic factors, especially query size, a surprisingly high degree of overlap in the resulting training samples and stable performances (classification accuracy). Additionally, all uncertainty query strategies perform well, and expensive sampling strategies like ensembling offer little benefit. We conclude that sampling biases demonstrated in active learning literature do hold well with traditional models, however, they do not seem to translate to deep models like FTZ using (posterior) uncertainty.

# Application: Active Text Classification

Experimental results from the previous sections suggest that entropy function with a single FTZ Figure 2: Active text classification: Comparison with K-Center Coreset, BALD and SVM algorithms. Accuracy is plotted against percentage data sampled. We reach full-train accuracy using 12% of the data, compared to BALD which requires 50% data and perform significantly worse in terms of accuracy. We also outperform K-center greedy Coreset at all sampling percentages without utilizing additional diversity-based augmentation.

model would be a good baseline for active text classification. We compare our baseline with the latest work in deep active learning for text classification -BALD (Siddhant and Lipton, 2018) and with the recent diversity based Coreset query function (Sener and Savarese, 2018) which uses a costly K-center algorithm to build the query. Experiments are performed on TREC-QA for a fair comparison (used by (Siddhant and Lipton, 2018)). Table 8 shows that the results of our study generalize to small datasets like TREC-QA.

The results are shown in Figure 2 using the baseline with the query size of 2% of the full dataset (b=9 queries). Note that uncertainty sampling converges to full accuracy using just 12% of the data, whereas (Siddhant and Lipton, 2018) required 50% of the data. There is also a remarkable accuracy improvement over (Siddhant and Lipton, 2018) which can be largely attributed to the models used (FastText versus 1layer CNN/BiLSTM). Also, uncertainty sampling outperforms diversity-based augmentations like Coreset Sampling (Sener and Savarese, 2018) before convergence. Thus, we establish a new stateof-the-art baseline for further research in deep active text classification.

# Application: Training of Large Models

The cost and time needed to get and label vast amounts of data to train large DNNs is a serious Dsets Chance FTZ-Ent-Ent FTZ Ent-LC SV Chce% SV Com% TQA 15.1 ± 0.0 59.7 ± 0.5 56.3 ± 1.4 18.7 ± 6.1 79.0 ± 3.6    (Howard and Ruder, 2018) (%dataset in brackets). We observe that using our cheaply obtained compressed datasets, we can achieve similar accuracies with 25x-200x speedup (5x less epochs, 5x-40x less data). Transferability to other models is evidence of the generalizability of the subset collected using FTZ to other deep models.

impediment to creating new and/or better models.

Our study suggests that the training samples collected with uncertainty sampling (entropy) on a single model FTZ may provide a good representation (surrogate) for the entire dataset. Buoyed by this, we investigate if we can speedup training of ULMFiT (Howard and Ruder, 2018) using the surrogate dataset. We show these results in Table 10. We achieve 25x-200x speedup6 (5x fewer epochs, 5x-40x smaller training size). We also benchmark the performance against the state-ofthe-art on text classification as shown in Table 9.

We conclude that we can significantly compress the training datasets and speedup classifier training time with little tradeoff in accuracy.

Implementation Details: We use the official github repository for ULMFiT7 , use default hyperparameters and train on one NVIDIA Tesla V100 16GB GPU. Further details are provided in sup-

# Related Work

We now expand on the brief literature review in Section 1 to better contextualize our work. We divide the past works into (i) Traditional Models and (ii) Deep Models.

Sampling Bias in Classical AL in NLP: Active learning (AL) in text classification started with greedy uncertainty query strategy from a pool using decision trees (Lewis and Gale, 1994), which was shown to be effective and led to widespread adoption with classifiers like SVMs (Tong and Koller, 2001), Naive Bayes (Roy and McCallum, 2001) and KNN (Fujii et al., 1998). This strategy was also applied to other NLP tasks like parse selection (Baldridge and Osborne, 2004), sequence labeling (Settles and Craven, 2008) and information extraction (Thompson and Mooney, 1999). These early papers popularized two greedy uncertainty query methods: Least Confident and Entropy.

Issues of lack of diversity (large reduduncy in sampling) (Zhang and Oles, 2000) and lack of robustness (high variance in sample quality) (Krogh and Vedelsby, 1994) guided subsequent efforts. The two most popular directions were: (i) augmenting uncertainty with diversity measures (Hoi et al., 2006;Brinker, 2003;Tang et al., 2002) and (ii) using query-by-committee (McCallum and Nigam, 1998;Liere and Tadepalli, 1997). For a comprehensive survey of classical AL methods for NLP, please refer to (Settles, 2009).

Sampling Bias in Deep AL: Deep active learning approach adapt the above framework to the training of DNNs on large data. Two main query strategies are used: (i) ensemble based greedy uncertainty, which represents a probabilistic queryby-committee paradigm (Gal et al., 2017;Beluch et al., 2018), and (ii) diversity based measures (Sener and Savarese, 2018;Ducoffe and Precioso, 2018). Papers proposing diversity based approaches find that greedy uncertainty based sampling (using ensemble and single model) perform significantly worse than random (See Figures 4 and2 respectively in (Sener and Savarese, 2018;Ducoffe and Precioso, 2018)). They attribute the poor performance to redundant, highly correlated sampling selected using uncertainty based methods and justify the need for prohibitively expensive diversity-based approaches (Refer section 2 of (Sener and Savarese, 2018) for details on the expensiveness of various diversity sampling methods). However, K-center greedy coreset sampling scales poorly: we were only able to use it on TREC-QA (a small dataset). On the other hand, ensemble-based greedy uncertainty methods find that probabilistic averaging from a committee (Gal et al., 2017;Beluch et al., 2018) performs better than single model as with on diversity based methods like coreset (Gissin and Shalev-Shwartz, 2019;Beluch et al., 2018). Current approaches in text classification literature mostly adopt the ensemble based greedy uncertainty framework (Siddhant and Lipton, 2018;Lowell et al., 2018;Zhang et al., 2017). However, our work demonstrates the problems of sampling bias and efficiency may not translate from shallow to deep approaches. Recent evidence from image domain (Gissin and Shalev-Shwartz, 2019) demonstrates atleast a subset of our findings generalize to other DNNs (class bias and query functions). Uncertainty sampling using a deep model like FTZ demonstrates surprisingly good sampling properties without using ensembles or bayesian methods. Ensembles do not seem to significantly affect sampling. Whether this behavior generalizes to other deep models and tasks is yet to be seen.

Other Related Works: An interesting set of papers (Soudry et al., 2018;Xu et al., 2018) show that deep neural networks trained with SGD converge to the maximum margin solution in the linearly separable case. Several works investigate the possibility that deep networks give high importance to a subset of the training dataset (Toneva et al., 2019;Vodrahalli et al., 2018;Birodkar et al., 2019), resembling supports in support vector machines. In our experiments, we find that active learning with uncertainty sampling with deep models like FTZ has a (surprisingly) large overlap with the support vectors of an SVM. Thus, it seems to have a inductive bias for class boundaries, similar to the above works. Whether this property generalizes to other deep models is yet to be seen.

# Conclusion

We conducted a large empirical study of sampling bias and efficiency, along with algorithmic factors which impacting active text classification. We conclude that uncertainty sampling with deep models like FastText.zip exhibits negligible class bias, seems to be favorably biased to sampling data points near class boundaries, is robust to various algorithmic factors and expensive sampling strategies like ensembling offer little benefit. Also, we find a surprisingly large overlap of actively acquired points with supports of a SVM. We additionally show that uncertainty sampling can be effectively used to bootstrap the training of large DNN models by generating compact surrogate datasets (5x-40x compression). Finally, FTZ-Ent provides a strong baseline for deep active text classification, outperforming previous results by a margin of 4x less data.

The current work opens up several directions for future investigations. To list a few: (a) a deeper look into the nature of sampled data -their distribution in the feature space, as well as their importance for the task at hand; (b) the creation of surrogate datasets for a variety of applications, including hyperparameter and architecture search, etc; (c) an extension to other deep models (beyond FTZ) and beyond classification models; and, (d) an extension to semi-supervised, online and continual learning.  In this document, we present statistics, additional tables and hyperparameters left out of the main work due to lack of space.

# A Dataset Details

Details of the train, test sizes and number of classes for each dataset can be found in Table 11.

# B Experiment Hyperparameters

In this section, we detail the complete list of hyperparameters, for reproducibility. We will release our code on Github.

# B.1 Models

We describe the model hyperparameters used for 4 models: (i) FastText (ii) SVM (iii) ULMFiT (iv) Multinomial Naive Bayes for reproducibility.

# B.1.1 FastText

We use the original implementation8 . The hyperparameters used for each dataset can be found in Table 12. We chose to use the zipped version of FastText for optimized memory usage without loss of accuracy, or speed.

# B.1.2 ULMFiT

For ULMFiT, we used the default hyperparameters from the author's implementation9 , except the Dsets NLL BrierL ECE VarR ENT STD SGN 0.14 0.01 0.01 0.02 0.07 0.39 DBP 0.07 0.0 0.01 0.0 0.02 0.26 YHA 1.37 0.05 0.16 0.12 0.5 0.27 YRP 0.16 0.04 0.02 0.03 0.11 0.47 YRF 1.15 0.11 0.17 0.21 0.73 0.31 AGN 0.46 0.03 0.04 0.02 0.08 0.42 AMZP 0.26 0.05 0.04 0.02 0.08 0.48 AMZF 1.32 0.12 0.21 0.22 0.77 0.31 batch size which we set to 32. We recall that ULMFiT has two steps: the fine-tuning of the language model and the fine-tuning of the classifier. We initialized the language model with the pre-trained weights released by the authors. Results of a pre-training on Wikitext-103 consisting of 28,595 pre-processed Wikipedia articles and 103 million words. For each compressed datasets (small and very small), we fine-tuned the language model and the classifier for 10 epochs. For finetuning both language model and classifier, we used a NVIDIA Tesla V100 16GB.

The hyperparameters for the language model are: batch size of 32, learning rate of 4e-3, bptt of 70, embedding size of 400, 1150 hidden units per hidden layer and 3 hidden layers. Adam Optimizer with β 1 = 0.8 and β 2 = 0.99. The dropout rates are: 0.15 between LSTM layers, 0.25 for the input layer, 0.02 for the embedding layer, 0.2 for the internal LSTM recurrent weights.

The hyperparameters for the classifier are: batch size of 32, learning rate of 0.01, embedding size of 400, 1150 hidden units per hidden layer and 3 hidden layers. Adam Optimizer with β 1 = 0.8 and β 2 = 0.99. The dropout rates are: 0.3 between LSTM layers, 0.4 for the input layer, 0.05 for the embedding layer, 0.5 for the internal LSTM recurrent weights.

# B.1.3 Multinomial Naive Bayes (MNB)

We use the scikit-learn implementation of Multinomial Naive Bayes 10 with default hyperparameters: smoothing parameter α = 1.0, fit prior set to True and class prior set to None. As input to our Dsets Chance FTZ Ent-Ent FTZ Ent-LC MNB Ent-Ent MNB Ent-LC FTZ Ent-Ent FTZ Ent-LC MNB Ent-Ent MNB Ent-LC SGN 9.4 ± 0.0 81.6 ± 0.1 80.1 ± 0.3 52.9 ± 0.0 39.8 ± 0.0 74.8 ± 0.3 73.4 ± 0.6 35.0 ± 0.0 34.1 ± 0.0 DBP 9.3 ± 0.0 82.6 ± 0.2 82.2 ± 0.1 84.9 ± 0.0 69.8 ± 0.0 77.4 ± 0.1 76.6 ± 0.2 79.5 ± 0.0 64.1 ± 0.0 YHA 19.0 ± 0.0 75.0 ± 0.1 71.6 ± 0.1 90.9 ± 0.0 76.8 ± 0.0 66.1 ± 0.1 66.7 ± 0.1 86.4 ± 0.0 72.0 ± 0.0 YRP 9.3 ± 0.0 59.4 ± 0.3 59.6 ± 0.4 32.5 ± 0.0 32.5 ± 0.0 56.4 ± 0.7 56.4 ± 0.6 19.9 ± 0.0 19.9 ± 0.0 YRF 19.0 ± 0.0 75.1 ± 0.1 62.0 ± 0.1 69.6 ± 0.0 60.7 ± 0.0 67.2 ± 0.3 53.6 ± 0.1 55.5 ± 0.0 44.8 ± 0.0 AGN 19.1 ± 0.0 75.8 ± 0.3 75.1 ± 0.1 ?81.1 ± 0.0 71.5 ± 0.0 70.6 ± 0.2 69.1 ± 0.0 76.2 ± 0.0 67.3 ± 0.0 AMZP 9.5 ± 0.0 60.2 ± 0.1 60.2 ± 0.3 32.2 ± 0.0 32.2 ± 0.0 52.7 ± 0.6 52.7 ± 0.1 23.5 ± 0.0 23.5 ± 0.0 AMZF 19.0 ± 0.0 64.8 ± 0.3 58.5 ± 0.3 64.2 ± 0.0 57.4 ± 0.0 55.2 ± 0.1 48.4 ± 0.1 55.2 ± 0.0 50.4 ± 0.0 Table 14: Intersection across query strategies using 19 and 9 iterations (mean ± std across runs) and different seeds Datasets Limit FTZ (∩Q) MNB (∩Q) FTZ (∩Q) MNB (∩Q) FTZ (∩Q) MNB (∩Q) SGN 1.6 1.5 ± 0.1 1.4 ± 0.2 1.6 ± 0.0 1.3 ± 0.2 1.6 ± 0.0 1.2 ± 0.2 DBP 2.6 2.5 ± 0.1 2.3 ± 0.1 2.5 ± 0.1 2.3 ± 0.2 2.5 ± 0.1 2.3 ± 0.1 YA 2.3 2.3 ± 0.0 2.3 ± 0.0 2.3 ± 0.0 2.2 ± 0.0 2.3 ± 0.0 2.2 ± 0.0 YRP 0.7 0.7 ± 0.0 0.7 ± 0.1 0.7 ± 0.0 0.6 ± 0.2 0.7 ± 0.0 0.7 ± 0.0 YRF 1.6 1.6 ± 0.0 1.5 ± 0.1 1.6 ± 0.0 1.4 ± 0.2 1.6 ± 0.0 1.3 ± 0.2 AGN 1.4 1.3 ± 0.0 1.3 ± 0.1 1.3 ± 0.1 1.1 ± 0.2 1.3 ± 0.0 1.1 ± 0.1 AMZP 0.7 0.7 ± 0.0 0.7 ± 0.1 0.7 ± 0.0 0.7 ± 0.0 0.7 ± 0.0 0.7 ± 0.0 AMZF 1.6 1.6 ± 0.0 1.6 ± 0.0 1.6 ± 0.0 1.6 ± 0.1 1.6 ± 0.0 1.6 ± 0.0 MNB, we use the scikit-learn implementation of the TFIDF Vectorizer 11 . All default hyperparameters remain unchanged except that we use a maximum feature threshold of 50000, we remove all stop words contained in the default list 'english' and we set sublinear tf to True.

# B.1.4 SVM

To compute the support vectors of the datasets we used ThuderSVM, a Fast SVM library running on a V100 GPU. 12 . We used the SVC with a linear kernel, degree = 3, gamma = auto, coef0 = 0.0, C = 1.0, tol = 0.001, probability = False, classweight = None, shrinking = False, cachesize = None, verbose = False, max iter = -1, gpuid=0, maximum memory size = -1, random state = None and decision function = 'ovo'.

# C Experiments C.1 Class Bias

We provide in Table 15 the complete results of our class bias experiments with 39, 19 and 4 iterations using entropy query strategy.

# C.1.1 Results Across Iterations

We provide in 

# C.2 Metrics Affecting Uncertainty

We provide in Table 13 several metrics measured on the resulting samples of each dataset after 39 queries and using the entropy query strategy. NLL denotes the negative log-likelihood, BrierL denotes the Brier Score Loss, ECE denotes the expected calibration error, VarR denotes the variation ratio, ENT denotes the entropy, STD denotes the standard deviation. We measure these properties of the predicted sample and compute their average over the dataset. We observe that the Fast-Text model is well calibrated except for YRF and AMZF. Similar trends are observed in the average uncertainty measures.

# C.3 Accuracy Plots for Remaining Datasets

We show in Figure 3 the accuracy curves for Fast-Text and NaiveBayes, for 4, 9, 19 and 39 iterations using entropy query strategy vs random. 

