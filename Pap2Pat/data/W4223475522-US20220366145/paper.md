# Introduction

Sentiment analysis (Pang et al., 2002;Turney, 2002;Chevalier and Mayzlin, 2006;Bastan et al., 2020) aims at detecting the overall polarity of a user generated text, which describes the user opinion for an entity. However, user may express opinions about an entity at different granularity. For example, a user may give an overall rate about a restaurant service, and then explains fine-grained review about specific aspects, such as food quality, waiting time, waitress service, environment, etc. Aspect-based sentiment analysis task (Pontiki et al., 2014(Pontiki et al., , 2016) ) aims at addressing this problem, where user sentiment is annotated at coarse and fine-grained levels. Moreover, user can express conflicting opinions for different aspects of an entity.

Traditionally, neural-based models are employed as a single-task model for aspect-based sentiment analysis (ABSA) task, similar to Machine Reading Comprehension task (MRC) (Rajpurkar et al., 2016). For example, a pre-trained BERT language model is fine-tuned for ABSA term polarity prediction (single-task) as a classifier. In this approach, a task-specific layer is fine-tuned for each downstream task, such as a layer for aspect term polarity classification, and a different layer for aspect term span extraction (Xu et al., 2019).

Recently, generative language models with unidirectional self-attention, which are pre-trained by causal language modeling loss (predicting next word given the history), have shown promising performance when fine-tuned on the downstream tasks (GPT2) (Radford et al., 2018). Using this approach, the language model learns the downstream task as language generation, where the task is represented as a serialized text. Moreover, Brown et al. (2020) proposed GPT3, a large-scale generative language model with few-shot ability. GPT3 learns to solve the downstream task by conditioning on few examples in the prompt, without any parameter update (in-context learning).

Motivated by the ability of the pre-trained generative language model (GPT2) for solving the downstream tasks in a generative manner, we propose a generative language model for ABSA task. The evaluation results indicate that the proposed approach achieves better performance with significantly lower variance compared to the previous state-of-the-art models (which are based on BERT pre-trained model) on few-shot and full-shot settings, for single-task polarity prediction of aspect term and aspect category. For example, using 1% (20 examples) of training data on restaurant domain for aspect term polarity prediction task, our proposed GPT2 model outperforms BERT-PT (Xu et al., 2019) by 9 points on average accuracy and reduced standard deviation by 6.2 points, as shown in Figure 1(a). Moreover, when fine-tuned on multiple tasks, such as aspect term extraction, term polarity, aspect category detection, and category polarity, the proposed model improved single-task performance, such as aspect term extraction (measured by F1 score). 1The contributions of our proposed generative language model are,

• A robust generative model on few-shot aspectbased sentiment analysis by reformulating the task as language generation. This allows us to use uni-directional language model with no additional head for the downstream tasks, which outperforms the previous state-of-thearts on average performance by a large margin, with no additional pretraining on out-ofdomain data (such as BERT-PT (Xu et al., 2019)).

• Our proposed generative model reduces variance in polarity prediction, caused by low resource data and random noise, in all few and full-shot settings by large value.

• Joint and multi-task training can further improve the single-task few-shot performances, such as aspect term extraction.

• More evaluation on similar sentiment analysis tasks (SST-2, SST-5, OOS intent detection) provides further evidence of the superiority and robustness of generative language model.

In the next sections, we discuss the proposed model and presents the evaluation results. In section 2, the previous state-of-the-arts are described. Section 3 explains the task of aspect-based sentiment analysis (ABSA) (section 3.1) followed by reformulating ABSA task as language generation (section 3.2). In section 4, the evaluation results for single, joint and multi-task settings are presented for SemEval14 (Pontiki et al., 2014) and SemEval16 (Pontiki et al., 2016) and SST-2, SST-5 and OOS intent detection datasets.

# Related Works

Sentiment analysis is characterized by three categorizes, i.e. document, sentence, and aspect level (Liu, 2012;Liu and Zhang, 2012;Cambria and Hussain, 2012). In this section, we review the previous models developed for aspect-based sentiment analysis (ABSA) (Hu and Liu, 2004).

Earlier works on ABSA task focused on developing feature engineered models (Samha et al., 2014). Xu et al. (2018) proposed a model based on using convolutional neural network (CNN) for aspect term extraction task only. The approach uses two types of pre-trained embeddings, a generalpurpose embedding and a domain-specific one. Then, a softmax classification layer is used to classify each word to identify aspect term start and end positions, or non-related words. Li et al. (2019) proposed Multi-granularity Alignment Network (MGAN), a coarse-to-fine approach for single-task aspect term polarity prediction using recurrent neural network (RNN) (Hochreiter and Schmidhuber, 1997). They defined aspect category as coarse-level and aspect term as fine-level sentiments, and further leveraged high-resource out-of-domain data for pre-training. This way, the knowledge is transferred from coarsegrain domains (single-opinion prediction) to multigrain domains (ABSA task).

With the advent of BERT (Devlin et al., 2018) as a pre-trained bidirectional language model, which presents a powerful contextualized word representation for the language understanding downstream tasks, several models are proposed for ABSA task using BERT as feature extraction. Xu et al. (2019) defined ABSA task as question answering (Rajpurkar et al., 2016), named Review Reading Comprehension (RRC), and used BERT as the base model, with separate heads for aspect term extraction (as span extraction) and term polarity prediction. To enhance RRC performance, they introduced a post-training algorithm, which additionally pre-train the model on out-of-domain data from Amazon and Yelp review datasets, and additionally on MRC question answering dataset (Rajpurkar et al., 2016). These result in additional training set of 1, 151, 863 for laptop domain, 2, 677, 025 more examples for restaurant domain, and 87, 599 training examples from MRC dataset. Karimi et al. (2020) proposed an approach based on conditional random field (CRF) (Lafferty et al., 2001), combined with BERT for aspect term extraction and term polarity prediction tasks. Two modules are employed for improving aspect term extraction and term polarity prediction of BERT model. First, a parallel approach is used which combines predictions for aspect term and polarity from last four layers of BERT in parallel. Moreover, a hierarchical aggregation module is also examined, where predictions of previous layers of BERT are fed into the next layer. Reddy et al. (2020) combines GLOVE pre-trained embedding (Pennington et al., 2014) with deep contextualized representation of BERT to enhance the representation of word vectors for predicting aspect term polarity. The proposed BERT-IL model predicts aspect term polarity by learning a similarity between GLOVE vector of aspect term and its contextualized representation extracted from BERT. First, the aspect term representations are extracted from multiple layers of BERT, and fed into a self-attention layer. Finally, it is further fine-tuned on ABSA task for performance improvement. Liu et al. (2021) proposed a model based on BART (Lewis et al., 2020) for aspect category detection. They rank all aspect categories with different polarities and select the pair with highest score. Seoh et al. (2021) proposed an NLI approach based on BERT for single task of polarity prediction only, using extra pretraining on review datasets. In section 4, evaluation of our proposed generative language model are compared with the recent BERT-based models.

# Model

This section describes aspect-based sentiment analysis task (ABSA), the proposed generative language model approach, details of the datasets, model training, and evaluation metrics.

## Aspect Based Sentiment Analysis

Aspect-based sentiment analysis (ABSA) is similar to sentiment analysis, in the sense that the task is to predict the polarity of an entity in a sentence. However, it is different, since the goal is to predict fine-grained sentiment of multiple aspect terms and categories of an entity. The task was first introduced in Semantic Evaluation Challenge (SemEval14) (Pontiki et al., 2014). It was then extended in SemEval16 challenge (Pontiki et al., 2016). The challenges comprise of two domains, restaurant and laptop, where each domain spans over four sub-tasks (SB1-4).

Aspect Term Extraction (SB1) For a given review sentence, this sub-task is about predicting all aspects terms (word span) that opinions are expressed. It requires that all aspect terms to be predicted, including those which no opinion is expressed (neutral sentiment). This sub-task (AE) corresponds to sub-task 1 (SB1) -single sentenceslot 2 in SemEval16 challenge, named as opinion target expression (OTE) (Pontiki et al., 2016).

Aspect Term Polarity (SB2) For a given review sentence and an aspect term, the goal is to predict the polarity of the expressed opinion (positive, negative, neutral, conflict). This subtask corresponds to SB1-Slot3 in SemEval16 challenge.

Aspect Category Detection (SB3) Given a set of pre-defined aspect categories (e.g.

# PRICE,

FOOD, SERVICE, AMBIENCE, ANECDOTE/MISCELLANEOUS), the goal is to predict all categories that an opinion is expressed about.

This sub-task corresponds to SB1-Slot1 (single-sentence) in SemEval16 challenge, where the category is defined as the pair of entity and attribute, e.g. RESTAURANT#PRICE, FOOD#QUALITY, LAPTOP#GENERAL, LAPTOP#PRICE. Please refer to Table 4 in the appendix for the full list of categories for laptop and restaurant domains.

Aspect Category Polarity (SB4) Given a review sentence and a category, the goal is to predict the sentiment of the category (positive, negative, neutral, conflict). This subtask corresponds to SB1-Slot3 in SemEval16 (Pontiki et al., 2016).

## Generative Language Modeling

ABSA task comprises of four sub-tasks: aspect term extraction, aspect category detection, and aspect term and category polarity predictions. The dominant approach for solving ABSA task is to train separate classifiers for each sub-task (Xu et al., 2019). In this paper, we propose to solve all subtasks using a single auto-regressive (generative) language model, either using single-task or jointtask training.

### Language model

The goal of generative language modeling is to learn data distribution p(x), where x = (x 1 , . . . , x n ) is a sequence of n symbols. In order to model p(x), the language model factorizes the distribution of a single sequence p(x) using the chain rule of probability (Bengio et al., 2003), and training a neural network, which is parameterized by θ, by minimizing the negative log-likelihood,

(1)

During inference, the generative model sequentially generates tokens by conditioning on the input example x k , and the past generated tokens.

## ABSA task as generative language modeling

Each ABSA task training example, x k , contains a sentence S k , I pairs of aspect term and term polarity, and J pairs of aspect category and category polarity,

where t k i , pt k i , and T P k i are i-th aspect term, term polarity, and their pair. Moreover, c k j and pc k j , and CP k j are j-th aspect category, category polarity, and their pair of k-th sentence.

### Single-Task Polarity Prediction

This task consists of predicting the polarity of aspect terms or aspect categories only (named as SB2 and SB4 in section 3.1). To generate polarity during the inference, the input to the generative language model (LM) comprises of k-th sentence and the corresponding aspect term or category,

where LM term refers to a model that trained on aspect term dataset, and LM category refers to aspect category dataset, respectively. The details of training language model are described in section 3.3.3. Moreover, the details of input sequence formulation during training and inference are presented in Appendix A and Tables 3 and5.

### Joint and Multi-Task Prediction

This task includes generating pairs of aspect term and term polarity, or pairs of aspect category and their polarity. To jointly generate aspect terms and their polarities, the model input relies on the review sentence S k only, and the model outputs all aspect term and polarity pairs in token-by-token (autoregressive) generation,

where T k is the set of aspect term and polarity pairs, Eq. ( 3), and C k is the set of aspect category and polarity pairs, Eq. ( 4). The same method in jointtask prediction can be used to generate all pairs of aspect term and aspect category, i.e. multi-task prediction,

In this case, during training, the model learns to generate I pairs of aspect term and J pairs of aspect category via language model training, Eq. (1).

### Training

A training sequence for solving each sub-tasks (SB1-4) of section 3.1, consists of the review sentence, concatenated by the corresponding aspect term/category and its polarity. For example, in training LM term for predicting aspect term polarity (Eq. 5) and joint-task prediction of aspect term and polarity (Eq. 7), the training sequence comprises of the review sentence concatenated by aspect terms and their polarities,

as mentioned in Eq. ( 6) and ( 8). For more details on input sequence representation, see Appendix A, Tables 3 and5.

In order to train LM term , the model can be trained on different training sequences, where the review sentence S k needs to only be concatenated with a single pair of aspect term and polarity. In this case, multiple training sequences are created for the k-th sentence, i.e. {x k i = [S k ; T P k i ]; i ∈ I}. We will present an ablation study on these two methods of sequence creation for the language model training, and its effect on few-shot and full-shot performances, are presented in Appendix C and Figure 4.  

## Dataset

The proposed generative language model is evaluated on the two datasets proposed for ABSA task. SemEval14 challenge (Pontiki et al., 2014) consists of four sub-tasks as described in section 3.1. We also evaluate the proposed model on task 5 of Se-mEval16 (Pontiki et al., 2016), which contains two sub-tasks for sentence and text level review data in multiple languages. In this paper, we only focus on the English language of sub-task 1 (sentence level) to be able to compare with the prior arts. Moreover, we evaluate on Stanford Sentiment Treebank (SST) dataset (Socher et al., 2013) for binary (SST-2) and fine-grained (SST-5) sentiment classification of movie reviews domain. Since intent detection is a similar task to sentiment analysis, the evaluation is also performed on out-of-scope (OOS) intent detection dataset (Larson et al., 2019) which created for chatbot systems.

To evaluate the performance on few-shot setting, we sub-sample training set for aspect term and aspect category domains. For aspect term, the train set is randomly sub-sampled to the smaller sizes, [1%, 5%, 10%, 20%]. For example, 1% few-shot train set contains only about ≈ 20 sentences. For aspect category, since there is the predefined set of categories, we randomly sub-sample examples for each category, with different number of examples of [1,5,10,20].

The distribution of the train, dev and test splits for each domain are shown in Table 1. It is noteworthy that the previous baselines have created customized validation set from train set. Since no official validation set is released for SemEval14 and SemEval16, and in order to have a unified evaluation, we used the official trial set (part of train set) for validation, and exclude those examples from the train set. Moreover, prior works excluded examples with conflict polarity from their evaluations, since it is considered a difficult prediction task. However, for more accurate evaluation, these examples are retained in our evaluation.

## Evaluation

Performance evaluation of aspect term polarity (SB2) and aspect category polarity (SB4) singletasks in Eq. ( 5) and Eq. ( 6) are based on accuracy metric. It is measured by counting the number of aspect term and aspect category polarities which are correctly predicted. The evaluation of aspect term extraction (SB1) and aspect category detection (SB3) are measured by F1 metric (Pontiki et al., 2014) computed on the overlap of the ground-truth and generated sequences. The evaluation of SST-2, SST-5 and OOS datasets are measured by accuracy metric. On OOS dataset, full accuracy on indomain and out-of-scope examples are measured.

Evaluation of joint and multi-task models in Eq. ( 7)(8)(9) are measured by joint accuracy. This means that for an example sentence S k , if all the aspect term and term polarity predictions are correct, it is assumed as a correct prediction.

The restaurant domain contains both aspect term and aspect category annotations for SemEval14 and SemEval16. However, the laptop domain only contains aspect term annotation for SemEval14, and aspect category annotation for SemEval16. Therefore, single-task evaluation on laptop domain is constrained and multi-task prediction performance can only be evaluated on restaurant domain.

# Experiments

The proposed generative language model is evaluated on five tasks. Single-task setting includes aspect term polarity and aspect category polarity prediction, Eq. ( 5)(6), for restaurant and laptop domains. Joint-task includes a) aspect term extraction and polarity Eq. ( 7) and b) aspect category detection and polarity Eq. ( 8). Finally, multi-task setting comprises all sub-tasks, i.e. aspect term extraction (SB1), aspect category detection (SB3), and their polarity predictions (SB2 and SB4), Eq. ( 9).

The evaluation of our proposed generative language model is compared with recent BERT-PT (Xu et al., 2019) model. We have reproduced results of BERT-PT on full-shot settings, since we include examples with conflict polarity. Other BERT-based models such as BERT-IL (Reddy et al., 2020) has not open-sourced code, and therefore they are not included in few-shot evaluation.

## Single-Task Polarity evaluation

In this section, the proposed generative language model is evaluated on aspect term and aspect category polarity prediction for both restaurant and laptop domains. As shown in Figure 1, the proposed model, based on GPT2-base, outperforms BERT on few-and full-shot settings on all sub-tasks (SB2 and SB4) for SemEval14 and SemEval16. More importantly, GPT2 model has lower variance than BERT, especially in 1% or 1-shot setting.

It is shown that BERT average performance drops by a large margin on low-resource regimes (< 5% or < 5 shot) and with increased variance, whereas our proposed generative model shows robust performance on few-shot setting with small variance. Compared to BERT-PT (Xu et al., 2019), which exploits additional pre-training on review data from Amazon and Yelp datasets, and using auxiliary tasks of MRC, generative model with more layers (GPT2-medium) and no additional pretraining matches or outperforms BERT-PT average performance in few-shot setting with smaller variance. Interestingly, GPT2-base model (12 layers) outperforms BERT-PT average performance in some cases, including all 1% and 1-shot settings with reduced variance. For example, GPT2-base outperforms by a large margin, 16.75 points on average accuracy and reduces standard deviation by 8.8 points on 1%-shot setting of category polarity prediction in restaurant domain of SemEval16, Figure 1(e). Moreover, GPT2-base outperforms BERT-PT in all few-and full-shot settings on aspect category polarity prediction task (SB4) of restaurant domains in SemEval16 dataset, Figure 1(f).

Although GPT2-medium average performance mostly outperforms BERT-PT, there are some exceptions, such as Figure 1 On the other hand, BERT-PT has much larger variance and less robustness in all few-and fullshot settings. This is perhaps due to the use of out-of-domain data in additional pre-training of BERT-PT which results in higher variance, even than BERT baseline, when finetuned on few-shot downstream tasks. The goal of our proposed model is not to simply outperforms BERT-PT by additional pre-training, but to provide a robust model for few-shot setting.

More evaluation on sentiment polarity prediction on SST5, SST2 and OOS intent detection datasets are presented in Figure 2, Appendix G and Figure 8. They indicate that generative language model outperforms BERT-based classifier models. Overall, the results of single-task polarity prediction indicate that our proposed generative model based on language generation (uni-directional selfattention) have better performance than the discriminative models which uses BERT (bi-directional self-attention) as encoder.

## Joint and Multi-Task evaluation

In this section, the proposed generative model is evaluated for joint and multi-task prediction. It includes solving two sub-tasks jointly, e.g. aspect term extraction and term polarity prediction, or  2 indicate that although generative model is trained in joint-task manner, for predicting aspect term extraction and term polarity, it still outperforms BERT-PT and other BERT baselines which are trained to solve single-task aspect term extraction only, on aspect term extraction (SB1) metric, in restaurant domain. However, in laptop domain, the generative model underperforms BERT-based models on aspect term extraction (SB1) metric, perhaps due to less training data in laptop domain for joint-task loss. Aspect category sub-tasks improve aspect term extraction: In multi-task setting, where generative model is trained on all sub-tasks (SB1-4), the aspect term extraction (SB1) F1 metric is improved more, compared to when trained as a single-task model. This indicates that training the generative model using extra supervision (from aspect category) helps to extract multiple aspect terms in the review sentence more accurately.

Generative language modeling is better for multi-task learning: Evaluation results on Se-mEval14 restaurant domain are shown in Appendix B Table 6. Combined with the results from Table 2, it indicates that the proposed generative language model performs well on solving all subtasks (SB1-4) using language generation. For example, compared to joint-task setting (  

## Ablation

In this section, the ablation study of proposed generative language model is studied on two aspects. First, using the language model (GPT2) as a discriminative classifier vs. for language generation. Second, we study the training convergence of generative model with two discriminative baselines, i.e. BERT and GPT2 as classifier to better understand few-shot performance.

# Generative vs. Discriminative training of unidirectional language model:

To analyze the benefit of fine-tuning GPT2 using language modeling loss, we also fine-tune it as a classifier. In the latter case, a classification layer is added, which uses the output of the last token of the input sequence for polarity prediction. As shown in Figure 3(c), GPT2-classifier under-performs BERT, when only trained with discriminative loss. We conjecture that since GPT2 uses uni-directional self-attention (leftto-right), it captures less contextualized representation, compared to bidirectional self-attention in BERT. On the other hand, when fine-tuning GPT2 using generative loss (next word prediction), unidirectional self-attention learns a better representa- GPT2 language model exploits more supervision than BERT in few-shot setting: To understand the training dynamics of generative language model and its relation to few-shot performance, we investigate the training convergence for GPT2, BERT, and GPT2-classifier. Results for SemEval14 restaurant aspect term polarity prediction are shown in Figure 3. It is indicated that BERT model converges faster than GPT2 in 1% few-shot settings, due to using a small classification head (fully-connected layer with 4 outputs) for the downstream task, which perhaps makes the model to overfits quickly to few-shot training data.

On the other hand, GPT2 converges more slowly, perhaps due to using language modeling loss, i.e. cross-entropy loss across all tokens of the input sequence, and also using output layer with size of the vocabulary. However, the cross-entropy loss on the position corresponding to predicting label, gpt2-generative (label position), converges faster than BERT, early in training, and the loss value is smaller than BERT between 40-90 steps, where the model has better validation accuracy than BERT. Later during the training, BERT training loss converges to smaller values, but its performance does not outperform GPT2. This is perhaps an evidence of BERT model overfitting due to using a small classification head which is specifically designed for the downstream task (4 output nodes).

Since the language modeling loss benefits GPT2 model to exploit more supervision during training (predicting next token for all input tokens), perhaps this helps GPT2 to be less prune to overfitting, and outperforms BERT in few-shot setting. Addition-ally, reformulating the task as natural text might benefits GPT2 to infer the sentiment polarity easier than BERT. Overall, GPT2 validation and test accuracy achieves higher performance. Analysis of training convergence on other tasks and domains are presented in Appendix E, Figures 5 and6.

We also investigates model weights change during fine-tuning by measuring the average of the normalized weight update, Eq. ( 10), for each layer (more details are presented in Appendix F and Figure 7). It is shown that gpt2-generative model has higher weight update in all layers at the end of training, and overall higher update in embedding layer (by one to two order of magnitude). This observation perhaps indicates that standard language modeling loss provides more supervision to GPT2 model, when finetuned on few-shot data.

# Conclusion

In this paper, we proposed a generative language model for aspect based sentiment analysis (ABSA). By reformulating the task as language generation, the model learns to predict aspects and their polarities via language generation. Evaluation results on single-task polarity prediction on few and full shot setting indicate that the proposed approach outperforms prior arts, which are based on discriminative classification using BERT as encoder, with higher average performance and lower variance. On jointask and multi-task settings, the proposed model shows better performance on single-task polarity prediction metrics. Additionally, evaluation results on coarse-grained (SST2), fine-grained (SST5) sentiment analysis datasets, and OOS intent detection dataset indicate the better and more robust few-shot performance of generative language model. Furthermore, qualitative analysis indicates that using multi-task setting improves model prediction via supervision across aspect term and category.

# Broader Impact

This work may have implications for the simplification of sentiment analysis using neural text generation. In the narrow sense, this work addresses aspect-based sentiment analysis. If so, the improvement of neural text generation systems and easier deployment would amplify both the positive and negative aspects of sentiment analysis. On the positive side, neural text generation models might play a role in automating user opinion mining, and thereby increasing efficiency of currently modular systems. On the negative side, it can dehumanize current systems, by automating systems towards multi-tasking, and reducing the level of human control on language generation. Moreover, this approach can introduce toxicity and biases into sentiment polarity predictions, such as gender, race, religious, and ethics (Kiritchenko and Mohammad, 2018;Park et al., 2018). This is due to biases which are learned during pretraining of neural text models on internet data (Sheng et al., 2019;Tan and Celis, 2019). These consequences are not specific to this work, but should be considered by the field of natural language processing more broadly.

# A Input Representation and Method Overview

As described in Section 3.3.3, a single training sequence consists of the concatenation of review sentence S k with the corresponding aspect terms and their polarities x k = S k ; T k , or aspect categories and their polarities

A schematic overview of each segment is shown in Table 3 together with special tokens marking transition points. The generative language model is optimized by minimizing the negative likelihood over the joint sequence. The output state associated with each input token is used to predict the next token. During inference, for single task polarity prediction of each aspect term (sub-task SB1), the language model input comprises the review sentence concatenated by the corresponding aspect term. The the model generates a single token, which assumed as predicted polarity. Same method is used for sub-task SB4 for aspect category polarity prediction. For joint-and multi-task prediction, the input sequence contains only the review sentence. The language model then generates aspect terms and aspect categories along with their polarities in single toke-by-token generation, until the end-of-sentence special token is generated.

Examples of different input sequence formatting for different datasets evaluated in the paper are presented in Table 5. We are using identifiers to separate different segments of the input sequence. For example, to separate review sentence from aspect term, we introduced identifiers <|review|> and <|term|> to separate them. each segment also ends with an end-of-segment identifier, such as <|end-ofreview|> and <|endofterm|> identifiers. It is noteworthy that these identifiers are not special token, similar to BERT, which introduces new embeddings into vocabulary. We have noticed that defining identifiers as special token will decrease the performance of generative language model, perhaps due to introducing randomly-initialized embedding vectors into vocabulary, which requires more training data to finetune them. However, since GPT2 did not use special tokens during pretraining, using identifiers which are combination of pretrained vocabulary tokens and special characters, such as {<, |, ,|, >}, helps GPT2 to understand different segments in the input sequence, to infer the sentiment polarity more accurately.

# B Multi-task prediction

In this section, evaluation results on SemEval 14 and SemEval16 restaurant domain are presented for multi-task learning using our proposed generative language model, based GPT2-base model, in Tables 6 and7. For more details, please refer to section 4.2.

# C Ablation: Model input sequence formatting

For a single review sentence with multiple aspect terms or categories, there are two ways to create input sequence for language model training, as described in section 3.3.3. First, the review sentence can be concatenated with each aspect terms separately (GPT2-Split), which results in better performance for few-shot setting (Figure 4) There are very few example in few-shot setting, such as 20 unique examples in 1% setting, and using split method increases training data and perhaps mitigates model over-fitting. However, when the review sentence is concatenated with all pairs of aspect terms or categories in a single sequence, performance is better for full-shot setting. There are few exceptions in Figure 4(a) for 1% and 5% shot settings. We observe that 1% few-shot contains 20, 14, 12 input sequences in Figure 4(a), (b), and (c), respectively, for the regular method. However, the split method increases input training sequences to 36, 23, 17. It means that when the number of training sequences are high enough, increasing number of training examples using split methods might deteriorates the few-shot performance, as shown in Figure 4(a). We guess that the better few-shot performance of the GPT2-Split method possibly depends on the number of unique training sequences when comparing to the regular method. In other words, the GPT2-Split methods might outperforms the regular method when the number of training sequences is very low.

# D Ablation: Generative vs. Discriminative language model

In this section, ablation analysis on using generative language model as a classifier are presented in Figures 5 and6. It is shown that when fine-tuning GPT2 model as a classifier on the downstream task using an classification layer, it under-performs BERT model on few and full-shot settings. For more details, please refer to section 4.3.    analysis. As shown in Figures 5 and6, GPT2 achieves higher validation accuracy, when its training losses, standard language modeling and loss corresponding to label position, have higher value  Table 7: Multi-task evaluation on SemEval16 restaurant domain (SB1-4) on few-shot settings using generative language model (GPT2).

than BERT and GPT2-classifier. This indicates that perhaps BERT and GPT2-classifier overfitted to the few-shot training data. On the other hand, GPT2 language model achieves more supervision via standard language modeling loss, which results in higher training loss, but better validation performance.

# F Ablation: Model weights update during training

In order to understand models behavior during training on few-shot data, we study the weight update at each layer of GPT2 and BERT models, during training on 1% few-shot data. For each layer, the mean normalized weight update is defined as,

where l indicate the layer index, i indicates training step, and w l 0 refers to initial weight value before training. The comparison between GPT2 as generative gpt2-generative, GPT2 as an ecoder for classification gpt2-classifier and BERT model when trained on 1% few shot data of SemEval14 restaurant domain are shown in Figure 7. The results indicate that Bert model has higher variance for all layers, especially for the randomly-initialized classification layer. Moreover, the mean normalized update of BERT model is larger that gpt2generative early during training, but is smaller at the end of training, where gpt2-generative achieves higher validation performance, as shown in Figure 3. Furthermore, the mean normalized update in embedding layer of gpt2-generative is significantly larger than BERT and gpt2-classifier by one order of magnitude early at training, which increased to two order of magnitude at the end. We conjecture that higher value in layer weights update at embedding layers, and at the end of training for other layers is perhaps due to using standard language modeling loss, which may provide more supervision signal for GPT2, compared to cross-entropy loss in BERT and gpt2-classifier models.

# G Ablation: Other Sentiment Analysis Tasks

In order to extend the investigate the performance of our proposed generative language model to other sentiment analysis tasks, we also evaluate few-shot performance on SST-5 sentiment analysis dataset (Socher et al., 2013) (binary and finegrained sentiment classification), and OOS (Larson et al., 2019) intent detection dataset. The results are shown in Figure 8, which indicate the superiority of generative model (GPT2) over discriminative BERT. On intent detection, Figure 8(c), GPT2 also outperforms TOD-BERT (Wu et al., 2020) which exploits extra pretraining on dialogue datasets to increase its few-shot performance.

# H Qualitative Analysis

As described in section 4.2 and       

