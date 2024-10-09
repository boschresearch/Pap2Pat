# Introduction

Many websites and online communities publish FAQ to help their users find relevant answers to common questions. An FAQ consists of pairs of questions and answers {(q, a)}. The FAQ retrieval task involves ranking {(q, a)} pairs for a given user query Q.1 Searching over FAQ can leverage multifield indexing and retrieval (Karan and Šnajder, 2016). Hence, a user query Q may be matched with either the question field q, the answer field a or the concatenated field q+a (Karan and Šnajder, 2016).

The association of questions to answers in the FAQ pairs, can be utilized as weak supervision, for training neural models to predict the similarity between user queries and answers (i.e., Q-to-a matching) (Gupta and Carvalho, 2019;Karan and Šnajder, 2018;Sakata et al., 2019). However, FAQ pairs by themselves do not provide the required labeled data for training a model to predict the association between user queries and FAQ questions (i.e., Q-to-q matching). Thus, a labeled dataset with user queries Q and their matching {(q, a)} pairs is required for supervised learning (Gupta and Carvalho, 2019;Karan and Šnajder, 2018;Sakata et al., 2019). Such a dataset is usually manually generated or obtained from query-log mining. Yet, the construction of such a dataset either requires domain expertise (e.g., enriching the dataset with manually generated question paraphrases (Karan and Šnajder, 2018)) or assumes the availability of query-logs (Kim andSeo, 2006, 2008).

Whenever such a dataset is unavailable, one must resort to utilizing unsupervised retrieval models for Q-to-q matching. Previous unsupervised FAQ retrieval models (Burke et al., 1997;Brill et al., 2002;Karan et al., 2013;Karan and Šnajder, 2018;Wu et al., 2005) have utilized so far "traditional" information retrieval techniques, such as lexical and semantic text matching, query expansion, etc.

In this paper we overcome the aforementioned unsupervised gap, by using distant supervision to train neural models. Our method is composed of a combination of three unsupervised methods. Each method is utilized for re-ranking an initial pool of FAQ pairs obtained by a simple BM25 retrieval (Robertson and Zaragoza, 2009). The first method applies a focused-retrieval approach, utilizing passages for answer re-ranking (Bendersky and Kurland, 2008). Each one of the two other methods fine-tunes a BERT model (Devlin et al., 2019), one for matching Q-to-a and one for matching Q-to-q.

To overcome the lack of training data in the latter's case, we further implement a novel weaksupervision approach using automatically generated question paraphrases, coupled with smart filtering to ensure high-quality paraphrases. We then combine the outcome of the three methods using an unsupervised late-fusion method. Overall, we show that our unsupervised FAQ retrieval approach is on par and sometimes even outperforms state-ofthe-art supervised models.

# Related work

Several previous works have also utilized Deep Neural Networks (DNN) for FAQ retrieval. (Karan and Šnajder, 2016) used Convolution Neural Networks (CNN) for matching user queries to FAQ. (Gupta and Carvalho, 2019) used combinations of Long Short-Term Memory (LSTM) to capture Qto-q and Q-to-a similarities. Yet, those works are supervised and use user queries (Q) for training.

Following the success of BERT (Devlin et al., 2019) in NLP tasks, (Sakata et al., 2019) have recently used a search engine for Q-to-q matching and then combined its results with a supervised BERT model for Q-to-a matching. We use a similar BERT model for Q-to-a matching, but differently from (Sakata et al., 2019), we use it in an unsupervised way, and we further introduce a second unsupervised BERT model for Q-to-q matching.

A somewhat related area of research is Community Question Answering (CQA) (Patra, 2017;Zhou et al., 2015) and the related TREC tracks. 23  While CQA shares some common features to FAQ retrieval, in CQA there are additional signals such as votes on questions and answers, or the association of user-answer and user-question. Clearly, in a pure FAQ retrieval setting, such auxiliary data is unavailable. Hence, we refrain from comparing with such works.

# Unsupervised FAQ Retrieval Approach

Our proposed FAQ retrieval approach uses distant supervision to train neural models and is based on an initial candidates retrieval followed by a reranking step.

Recall that, the FAQ dataset is composed of {(q, a)} pairs. The initial candidate retrieval is based on indexing {(q, a)} pairs into a search engine index (Section 3.1) and searching against the index. The re-ranking step combines three unsupervised re-rankers. The first one (Section 3.2) is based on a focused-retrieval approach, utilizing passages for answer re-scoring. The two other rerankers fine-tune two independent BERT models.

The first BERT model (Section 3.3), inspired by (Sakata et al., 2019), is fine-tuned to match questions (q) to answers (a). At run time, given a user query Q, this model re-ranks top-k {(q, a)} candidate pairs by matching the user query Q to the answers (a) only.

The second BERT model (Section 3.4) is designed to match user queries to FAQ questions. Here, we utilize weak-supervision for generating high quality question paraphrases from the FAQ pairs. The BERT model is fine-tuned on the questions and their generated paraphrases. At run time, given a user query Q, this model gets the topk {(q, a)} candidate pairs and re-ranks them by matching the user query Q to the questions (q) only.

The final re-ranking is obtained by combining the three re-rankers using an unsupervised latefusion step (Section 3.5). The components of our method are described in the rest of this section.

## Indexing and initial candidates retrieval

We index the FAQ pairs using the ElasticSearch4 search engine. To this end, we represent each FAQ pair (q, a) as a multifield document having three main fields, namely: question q, answer a, and the concatenated field q+a. Given a user query Q, we match it (using BM25 similarity (Robertson and Zaragoza, 2009)) against the q+a field5 and retrieve an initial pool of top-k FAQ candidates.

## Passage-based re-ranking

Our first unsupervised re-ranker applies a focused retrieval approach. To this end, following (Bendersky and Kurland, 2008), we re-rank the candidates using a maximum-passage approach. Such an approach is simply implemented by running a sliding window (i.e., passage) on each candidate's q+a field text, and scoring the candidate according to the passage with the highest BM25 similarity to Q (Gry and Largeron, 2011). We hereinafter term this first re-ranking method as bm25-maxpsg.

## BERT model for Q-to-a similarity

Among the two BERT (Devlin et al., 2019) rerankers, the first one, BERT-Q-a, aims at reranking the candidate FAQ pairs {(q, a)} according to the similarity between a given user query Q and each pair's answer a.

To this end, we fine-tune the BERT model from the FAQ pairs {(q, a)}, using a triplet network (Hoffer and Ailon, 2015). This network is adopted for BERT fine-tuning (Mass et al., 2019) using triplets (q, a, a ), where (q, a) constitutes an FAQ pair and a is a negative sampled answer as follows. For each question q we have positive answers {a i } from all the pairs {(q, a i )}. 6 Negative examples are randomly selected from those FAQ that do not have q as their question. To further challenge the model into learning small nuances between close answers, instead of sampling the negative examples from all FAQ pairs, we run q against the q+a field of the search index (from Section 3.1 above). We then sample only among the top-k (e.g., k = 100) retrieved pairs, that do not have q as their question.

Our BERT-Q-a is different from that of (Sakata et al., 2019) in two aspects. First, (Sakata et al., 2019) fine tunes a BERT model for Q-to-a matching using both FAQ (q, a) pairs as well as user queries and their matched answers (Q, a). This is, therefore, a supervised setting, since user queries are not part of the FAQ and thus require labeling efforts. Compared to that, we fine tune the BERT-Q-a using only FAQ (q, a) pairs. Second, unlike (Sakata et al., 2019), which fine-tunes BERT for a classification task (i.e., point-wise training) we train a triplet network (Hoffer and Ailon, 2015) that learns the relative preferences between a question and a pair of answers. Our network thus implements a pair-wise learning-to-rank approach (Li, 2011).

At inference time, given a user query Q and the top-k retrieved (q, a) pairs, we re-rank the (q, a) pairs using the score of each (Q, a) pair as assigned by the fine-tuned BERT-Q-a model (Mass et al., 2019).

## BERT model for Q-to-q similarity

The second BERT model, BERT-Q-q, is independent from the first BERT-Q-a model (Section 3.3) and is trained to match user queries to FAQ questions. To fine-tune this model, we generate a weakly-supervised dataset from the FAQ pairs. Inspired by (Anaby-Tavor et al., 2019), we fine-tune a generative pre-training (GPT-2) neural network model (Radford, 2018) for generating question paraphrases. GPT-2 is pre-trained on huge bodies of text, capturing the natural language structure and producing deeply coherent text paragraphs.

Intuitively, we would like to use the FAQ answers to generate paraphrases to questions. Unlike the work of (Anaby-Tavor et al., 2019) which fine tunes a GPT-2 model given classes, where each class has a title and several examples, here we consider each answer a as a class with only one example which is its question q.

We thus concatenate all the FAQ pairs into a long text U = a 1 SEP q 1 EOS • • • a n SEP q n EOS, where answers precede their questions,7 having EOS and SEP as special tokens. The former separates between FAQ pairs and the latter separates answers from their questions inside the pairs.

The GPT-2 fine-tuning samples a sequence of l consecutive tokens w j-l , • • • , w j from U and maximizes the conditional probability P(w j |w j-l , . . . , w j-1 ) of w j to appear next in the sequence. We repeat this process several times.

Once the model is fine-tuned, we feed it with the text "a SEP", (a is an answer in an FAQ pair (q, a)), and let it generate tokens until EOS. We take all generated tokens until EOS, as a paraphrase to a's question q. By repeating this generation process we may generate any number of question paraphrases. For example, the paraphrase "Is there a way to deactivate my account on Facebook?" was generated for the question "How do I delete my Facebook account?".

One obstacle in using generated text is the noise it may introduce. To overcome this problem we apply a filtering step as follows. The idea is to keep only paraphrases that are semantically similar to their original question (i.e., have similar answers). Let GT (q)={(q, a i )} be the FAQ pairs of question q (i.e., the ground truth answers of q). For each generated paraphrase p of q, we run p as a query against the FAQ index (See section 3.1), and check that among the returned top-k results, there are at least min(n, |GT (q)|) pairs from GT (q) for some n. In the experiments (see Section 4 below) we used k=10 and n=2.

To select the best paraphrases for each question q, we further sort the paraphrases that passed the above filter, by the score of their top-1 returned (q, a) pair (when running each paraphrase p as a query against the FAQ index). The motivation is that a higher score of a returned (q, a) for a query p, implies a higher similarity between p and q. 8 Similar to the BERT-Q-a, this model is finetuned using triplets (p, q, q ), where p is a paraphrase of q and q is a randomly selected question from the FAQ questions. At inference time, given a user query Q and the top-k retrieved (q, a) pairs, we re-rank the answers (q, a) answers, using the score of each (Q, q) pair as assigned by the finetuned BERT-Q-q model (Mass et al., 2019).

## Re-rankers combination

We combine the three re-ranking methods (i.e., bm25-maxpsg and the two fined-tuned BERT models) using two alternative late-fusion methods. The first one, CombSUM (Kurland and Culpepper, 2018), calculates a combined score by summing for each candidate pair the scores that were assigned to it by the three re-ranking methods.9 

Following (Roitman, 2018), as a second alternative, we implement the PoolRank method. PoolRank first ranks the candidate pairs using CombSUM. The top pairs are then used to introduce an unsupervised query expansion step (RM1 model (Lavrenko and Croft, 2001)) which is used to re-rank the whole candidates pool.10 4 Experiments

## Datasets

We use two FAQ datasets in our evaluation, namely: FAQIR (Karan and Šnajder, 2016) 11 and Stack-FAQ (Karan and Šnajder, 2018). 12 The FAQIR dataset was derived from the "maintenance & repair" domain of the Yahoo! Answers community QA (CQA) website. It consists of 4313 FAQ pairs and 1233 user queries. The StackFAQ dataset was derived from the "web apps" domain of the Stack-Exchange CQA website. It consists of 719 FAQ pairs (resulted from 125 threads; some questions have more than one answer) and 1249 user queries.

## Baselines

On both datasets, we compare against the results of the various methods that were evaluated in (Karan and Šnajder, 2018), namely: RC -an ensemble of three unsupervised methods (BM25, Vector-Space and word-embeddings); ListNet and LambdaMART -two (supervised) learningto-rank methods that were trained over a diverse set of text similarity features; and CNN-Rank -a (supervised) learning-to-rank approach based on a convolutional neural network (CNN).

On the StackFAQ dataset, we further report the result of (Sakata et al., 2019), which serves as the strongest supervised baseline. This baseline combines two methods: TSUBAKI (Shinzato et al., 2008) -a search engine for Q-to-q matching; and a supervised fine-tuned BERT model for Q-to-a matching. We put the results of this work (that were available only on the StackFAQ dataset), just to emphasize that our approach can reach the quality of a supervised approach, and not to directly compare with it.

## Experimental setup

We used ElasticSearch to index the FAQ pairs. For the first ranker (Section 3.1) we used a sliding window of size 100 characters with 10% overlap. For fine-tuning the BERT-Q-a model, we randomly sampled 2 and 5 negative examples for each positive example (q, a) on FAQIR and Stack-FAQ datasets, respectively.

To fine-tune GPT-2 for generating the question paraphrases (Section 3.4), we segmented U into consecutive sequences of l = 100 tokens each. We used OpenAI's Medium-sized GPT-2 English model: 24-layer, 1024-hidden, 16-heads, 345M parameters. We then used the fine-tuned model to generate 100 paraphrases for each question q and selected the top-10 that passed filtering (as described in Section 3.4). Overall on FAQIR, 22,736 paraphrases passed the filter and enriched 3,532 out of the 4,313 questions. On StackFAQ, 856 paraphrases passed the filter and enriched 109 out of the 125 thread questions. Similar to the BERT-Q-a fine-tuning, we selected 2 and 5 negative examples for each (p, q) (paraphrase-question) pair on FAQIR and StackFAQ, respectively.

The two BERT models used the pre-trained BERT-Base-Uncased model (12-layer, 768-hidden, 12-heads, 110M parameters). Fine-tuning was done with a learning rate of 2e-5 and 3 training epochs. Similar to previous works, we used the following metrics: P@5, Mean Average Precision (MAP) and Mean Reciprocal Rank (MRR), calculated on an initial candidate list of 100 FAQs retrieved by the search engine using standard BM25.

## Results

Table 1 reports the results for the two datasets. 13 We compare the base BM25 retrieval (bm25(q+a)), our three proposed unsupervised re-ranking methods (bm25-maxpsg, BERT-Q-a and BERT-Q-q) and their fusion-based combinations (CombSUM and PoolRank) with the state-of-the-art unsupervised and supervised baselines. We also compare to PoolRank+, which is same as PoolRank except that the two BERT models (i.e., BERT-Q-a and BERT-Q-q) are fine-tuned on the union of the respective training sets of both the FAQIR and StackFAQ datasets.

We observe that, among our three re-rankers, BERT-Q-q was the best. For example, on FAQIR it achieved 0.67, 0.61 and 0.90 for P@5, MAP and MRR, respectively. This in comparison to 0.54, 0.50 and 0.81, obtained by bm25-maxpsg for P@5, MAP and MRR, respectively. This confirms previous findings (Karan and Šnajder, 2016), that Q-to-q matching gives the best signal in FAQ retrieval. Furthermore, on both datasets, the fusion methods achieved better results than the individual re-rankers, with better performance by the PoolRank variants over ComboSum.

An exception is FAQIR, where BERT-Q-q achieved same results as the ComboSUM fusion. As mentioned above, BERT-Q-q has a significantly better performance on FAQIR than the other two individual rankers, thus a simple fusion method such as CombSUM can not handle such cases well. PoolRank, which uses relevance model, is a better approach and thus gives better fusion results.

Further comparing with the baselines, we can see that, on FAQIR, our unsupervised PoolRank outperformed all other methods; including the supervised methods on all three metrics. On Stack-FAQ, PoolRank outperformed all other methods, except the supervised TSUBAKI+BERT (Sakata et al., 2019). We note that, our unsupervised results PoolRank+ achieved (0.75, 0.88 and 0.90 for P@5, MAP and MRR, respectively), which is quite close to the supervised results (0.78, 0.90 and 0.94 respectively) of (Sakata et al., 2019). 13 Similar to (Karan and Šnajder, 2018), the FAQIR initial retrieval is done against a subset of 789 FAQ pairs that are relevant to at least one user query. 

# Summary and Conclusions

We presented a fully unsupervised method for FAQ retrieval. The method is based on an initial retrieval of FAQ candidates followed by three rerankers. The first one is based on an IR passage retrieval approach, and the others two are independent BERT models that are fine-tuned to predict query-to-answer and query-to-question matching. We showed that we can overcome the "unsupervised gap" by generating high-quality question paraphrases and use them to fine-tune the query-toquestion BERT model. We experimentally showed that our unsupervised method is on par and sometimes even outperforms existing supervised methods.

