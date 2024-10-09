# Introduction

Topic Detection and Tracking (Allan et al., 1998) is an important area of natural language processing to find topically related ideas that evolve over time in a sequence of text collections and exhibit temporal relationships. The temporal aspects of these collections can present valuable insight into the topical structure of the collections and can be quantified by modeling the dynamics of the underlying topics discovered over time.

Problem Statement: We aim to generate temporal topical trends or automatic overview timelines of topics for a time sequence collection of documents. This involves the following three tasks in dynamic topic analysis: (1) Topic Structure Detection (TSD): Identifying main topics in the document collection. (2) Topic Evolution Detection (TED): Detecting the emergence of a new topic and recognizing how it grows or decays over time (Allan, 2002). (3) Temporal Topic Characterization (TTC): Identifying the characteristics for each of the main topics in order to track the words' usage (keyword trends) for a topic over time i.e. topical trend analysis for word evolution (Fig 1,Left).

Probabilistic static topic models, such as Latent Dirichlet Allocation (LDA) (Blei et al., 2003) and its variants (Wang and McCallum, 2006;Hall et al., 2008;Gollapalli and Li, 2015) have been investigated to examine the emergence of topics from historical documents. Another variant known as Replicated Softmax (RSM) (Hinton and Salakhutdinov, 2009) has demonstrated better generalization in log-probability and retrieval, compared to LDA. Prior works (Iwata et al., 2010;Pruteanu-Malinici et al., 2010;Saha and Sindhwani, 2012;Schein et al., 2016) have investigated Bayesian modeling of topics in time-stamped documents. Particularly, Blei and Lafferty (2006) developed a LDA based dynamic topic model (DTM) to capture the evolution of topics in a time sequence collection of documents; however they do not capture explicitly the topic popularity and usage of specific terms over time. We propose a family of probabilistic time series models with distributional estimators to explicitly model the dynamics of the underlying topics, introducing temporal latent topic dependencies (Fig 1,Right).

To model temporal dependencies in high dimen-  t) and h (t) are binary visible and hidden layers of RSM for a document collection at time, t. u is RNN hidden layer. k: dictionary index for a word w sional sequences, such as polyphonic music, the temporal stack of RBMs (Smolensky, 1986;Hinton, 2002) has been investigated to model complex distributions. The Temporal RBM (Taylor et al., 2007;Sutskever and Hinton, 2007), Recurrent Temporal RBM (RTRBM) (Sutskever et al., 2009) and RNN-RBM (Boulanger-Lewandowski et al., 2012) show success in modeling the temporal dependencies in such symbolic sequences. In addition, RNNs (Gupta et al., 2015a;Vu et al., 2016a,b;Gupta et al., 2016) have been recognized for sentence modeling in natural language tasks. We aspire to build neural dynamic topic model called RNN-RSM to model document collections over time and learn temporal topic correlations.

We consider RSM for TSD and introduce the explicit latent topical dependencies for TED and TTC tasks. Fig 1 illustrates our motivation, where temporal ordering in document collection V (t) at each time step t, is modeled by conditioning the latent topic h (t) on the sequence history of latent topics h (0) , ..., h (t-1) , accumulated with temporal lag. Each RSM discovers latent topics, where the introduction of a bias term in each RSM via the time-feedback latent topic dependencies enables to explicitly model topic evolution and specific topic term usage over time. The temporal connections and RSM biases allow to convey topical information and model relation among the words, in order to deeply analyze the dynamics of the underlying topics. We demonstrate the applicability of proposed RNN-RSM by analyzing 19 years of scientific articles from NLP research.

The contributions in this work are:

(1) Introduce an unsupervised neural dynamic topic model based on recurrent neural network and RSMs, named as RNN-RSM to explicitly model discovered latent topics (evolution) and word relations (topic characterization) over time.

(2) Demonstrate better generalization (logprobability and time stamp prediction), topic interpretation (coherence), evolution and characterization, compared to the state-of-the-art.

(3) It is the first work in dynamic topic modeling using undirected stochastic graphical models and deterministic recurrent neural network to model collections of different-sized documents over time, within the generative and neural network framework. The code and data are available at https://github.com/pgcool/RNN-RSM.  (t) depend on the output of a deterministic RNN with hidden layer u (t-1) in the previous time step, t-1. Similar to RNN-RBM (Boulanger-Lewandowski et al., 2012), we constrain RNN hidden units (u (t) ) to convey temporal information, while RSM hidden units (h (t) ) to model conditional distributions. Therefore, parameters (b v (t) , b h (t) ) are time-dependent on the sequence history at time t (via a series of conditional RSMs) denoted by Θ (t) ≡ { V (τ ) , u (τ ) |τ < t}, that captures temporal dependencies. The RNN-RSM is defined by its joint probability distribution:

where V = [ V (1) , ... V (T ) ] and H = [h (1) , ...h (T ) ]. Each h (t) ∈ {0, 1} F be a binary stochastic hidden topic vector with size F and

n=1 be a collection of N documents at time step t. Let

n observed binary matrix of the n th document in the collection where, D (t) n is the document size and K is the dictionary size over all the time steps. The conditional distribution (for each unit in hidden or visible) in each RSM at time step, is given by softmax and logistic functions:

where

n ) are conditional distributions for i th visible v n,i and j th hidden unit h n,j for the n th document at t. W k ij is a symmetric interaction term between i that takes on value k and j. v

n times with identical weights connected to binary hidden units, resulting in multinomial visibles, therefore the name Replicated Softmax. The conditionals across layers are factorized as:

Since biases of RSM depend on the output of RNN at previous time steps, that allows to propagate the estimated gradient at each RSM backward through time (BPTT). The RSM biases and RNN hidden state u (t) at each time step t are given by-

(1) t) in RNN portion of the graph using eq 2. 2: Compute bv (t) and b h (t) using eq 1. 3: Generate negatives V (t) * using k-step Gibbs sampling. 4: Estimate the gradient of the cost C w.r.t. parameters of RSM W vh , bv (t) and b h (t) using eq 5. 5: Compute gradients (eq 6) w.r.t. RNN connections (W uh , Wuv, Wuu, Wvu, u 0 ) and biases (bv, b h , bu). 6: Goto step 1 until stopping criteria (early stopping or maximum iterations reached)

where W uv , W uh and W vu are weights connecting RNN and RSM portions (Figure 2). b u is the bias of u and W uu is the weight between RNN hidden units. v(t) n is a vector of vk n (denotes the count for the k th word in n th document).

n refers to the sum of observed vectors across documents at time step t where each document is represented as-

n,i =1 if visible unit i takes on k th value. In each RSM, a separate RBM is created for each document in the collection at time step t with

n is the count of words in the n th document. Consider a document of D (t) n words, the energy of the state {V

Observe that the bias terms on hidden units are scaled up by document length to allow hidden units to stabilize when dealing with different-sized documents. The corresponding energy-probability relation in the energy-based model is-

where

is the normalization constant. The lower bound on the log likelihood of the data takes the form:

Year 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008  where H(•) is the entropy and Q is the approximating posterior. Similar to Deep Belief Networks (Hinton et al., 2006), adding an extra layer improves lower bound on the log probability of data, we introduce the extra layer via RSM biases that propagates the prior via RNN connections. The dependence analogy follows-

; ln P ( V

Observe that the prior is seen as the deterministic hidden representation of latent topics and injected into each hidden state of RSMs, that enables the likelihood of the data to model complex temporal densities i.e. heteroscedasticity in document collections ( V) and temporal topics (H).

Gradient Approximations:

) Due to intractable Z, the gradient of cost at time step t w.r.t. (with respect to) RSM parameters are approximated by k-step Contrastive Divergence (CD) (Hinton, 2002). The gradient of the negative log-likelihood of a document collection

The second term is estimated by negative samples

n and as follows-

Gradient approximations w.r.t. RSM parameters,

The estimated gradients w.r.t. RSM biases are back-propagated via hidden-to-bias parameters (eq 1) to compute gradients w.r.t. RNN connections (W uh , W uv , W vu and W uu ) and biases (b h , b v and b u ). For the single-layer RNN-RSM, the BPTT recurrence relation for 0 ≤ t < T is given by-

where u (0) being a parameter and ∂C T ∂u (T ) = 0. See Training RNN-RSM with BPTT in Algo 1.

# Evaluation

## Dataset and Experimental Setup

We use the processed dataset (Gollapalli and Li, 2015), consisting of EMNLP and ACL conference papers from the year 1996 through 2014 (Table 1). We combine papers for each year from the two venues to prepare the document collections over time. We use ExpandRank (Wan and Xiao, 2008) to extract top 100 keyphrases for each paper, including unigrams and bigrams. We split the bigrams to unigrams to create a dictionary of all unigrams and bigrams. The dictionary size (K) and word count are 3390 and 5.19 M, respectively.

We evaluate RNN-RSM against static (RSM, LDA) and dynamic (DTM) topics models for topic and keyword evolution in NLP research over time. Individual 19 different RSM and LDA models are trained for each year, while DTM 2 and RNN-RSM are trained over the years with 19 time steps, where paper collections for a year is input at each time step. RNN-RSM is initialized with RSM (W vh , bv, b h ) trained for the year 2014.

We use perplexity to choose the number of topics (=30). See Table 2 for hyperparameters.

## Generalization in Dynamic Topic Models

Perplexity: We compute the perplexity on unobserved documents ( V (t) ) at each time step as To further assess the dynamic topics models, we split the document collections at each time step into 80-20% train-test, resulting in 1067 held-out documents. We predict the time stamp (dating) of a document by finding the most likely (with the lowest perplexity) location over the time line. See the mean absolute error (Err) in year for the held-out in Table 3. Note, we do not use the time stamp as observables during training.

## TSD, TED: Topic Evolution over Time

Topic Detection: To extract topics from each RSM, we compute posterior P ( V (t) |h j = 1) by activating a hidden unit and deactivating the rest in a hidden layer. We extract the top 20 terms for every 30 topic set from 1996-2014, resulting in |Q| max = 19 × 30 × 20 possible topic terms.

Topic Popularity: To determine topic popularity, we selected three popular topics (Sentiment Analysis, Word Vector and Dependency Parsing) in NLP research and create a set 3 of key-terms (including unigrams and bigrams) for each topic. We compute cosine similarity of the key-terms defined for each selected topic and topics discovered by the topic models over the years. We consider the discovered topic that is the most similar to the key-terms in the target topic and plot the similarity values in Figure 3a, 3b and 3b. Observe that RNN-RSM shows better topic evolution for the three emerging topics. LDA and RSM show   2000, 2005, 2010, 2014}. The cosine similarity scores are computed between the topic sets discovered in a particular year and the years preceding it in the above set, for example the similarity scores between the topic-terms in (1996,2000), (1996, 2005), (1996, 2010) and (1996, 2014), respectively. Figure 3i, 3j, 3k and 3l demonstrate that RNN-RSM shows higher convergence in topic focus over the years, compared to LDA and RSM. In RNN-RSM, the topic similarity is gradually increased over time, however not in DTM. The higher similarities in the topic sets indicate that new/existing topics and words do not appear/disappear over time.

We compute topic-term drift (T T D) to show the changing topics from initial to final year, as

where Q is the set of all topic-terms for time step t. Table 3 shows that T T D (where t=1996 and t =2014) are 0.268 and 0.084 for RNN-RSM and DTM, respectively. It suggests that the higher number of new topic-terms evolved in RNN-RSM, compared to DTM. Qualitatively, the Table 4 shows the topics observed with the highest and lowest cosine drifts in DTM and RNN-RSM.

In Figure 3g and 3h, we also illustrate the temporal evolution (drift) in the selected topics by computing cosine similarity on their adjacent topic vectors over time. The topic vectors are selected similarly as in computing topic popularity. We observe better TED in RNN-RSM than DTM for the three emerging topics in NLP research. For instance, for the selected topic Word Vector, the red line in DTM (Fig 3h) shows no drift (for x-axis 00-05, 05-10 and 10-14), suggesting the topicterms in the adjacent years are similar and does not evolve.  

## Topic Interpretability

Beyond perplexities, we also compute topic coherence (Chang et al., 2009;Newman et al., 2009;Das et al., 2015) to determine the meaningful topics captured. We use the coherence measure proposed by Aletras and Stevenson (2013) that retrieves co-occurrence counts for the set of topic words using Wikipedia as a reference corpus to identify context features (window=5) for each topic word. Relatedness between topic words and context features is measured using normalized pointwise mutual information (NPMI), resulting in a single vector for every topic word. The coherence (COH) score is computed as the arithmetic mean of the cosine similarities between all word pairs. Higher scores imply more coherent topics.

We use Palmetto 4 library to estimate coherence.

Quantitative: We compute mean and median coherence scores for each time step using the corresponding topics, as shown in Fig 3e and3f. Table 3 shows mean-COH and median-COH scores, computed by mean and median of scores from Fig 3e and3f, respectively. Observe that RNN-RSM captures topics with higher coherence. Qualitative: Table 5 shows topics (top-10 words) with the highest and lowest coherence scores.

## TTC: Trending Keywords over time

We demonstrate the capability of RNN-RSM to capture word evolution (usage) in topics over time. We define: keyword-trend and SPAN. The keyword-trend is the appearance/disappearance of the keyword in topic-terms detected over time, while SPAN is the length of the longest sequence of the keyword appearance in its keyword trend. Let

model } T t=1 be a set of sets5 of topic-terms discovered by the model (LDA, RSM, DTM and RNN-RSM) over different time steps. Let Q (t) ∈ Q model be the topic-terms at time step t. The keyword-trend for a keyword k is a timeordered sequence of 0s and 1s, as

And the SPAN (S k ) for the kth keyword is-

We compute keyword-trend and SPAN for each term from the set of some popular terms. We define average-SPAN for all the topic-terms appearing in the discovered over the years,  where

}| is the count of unique topic-terms and vk = T t=1 Dt j=1 v k j,t denotes the count of k th keyword. In Figure 4, the keyword-trends indicate emergence (appearance/disappearance) of the selected popular terms in topics discovered in ACL and EMNLP papers over time. Observe that RNN-RSM captures longer SPANs for popular keywords and better word usage in NLP research. For example: Word Embedding is one of the top keywords, appeared locally (Figure 5) in the recent years. RNN-RSM detects it in the topics from 2010 to 2014, however DTM does not. Similarly, for Neural Language. However, Machine Translation and Language Model are globally appeared in the input document collections over time and captured in the topics by RNN-RSM and DTM. We also show keywords (Rule-set and Seed Words) that disappeared in topics over time.

Higher SPAN suggests that the model is capable in capturing trending keywords.  4 Discussion: RNN-RSM vs DTM Architecture: RNN-RSM treats document's stream as high dimensional sequences over time and models the complex conditional probability distribution i.e. heteroscedasticity in document collections and topics over time by a temporal stack of RSMs (undirected graphical model), conditioned on time-feedback connections using RNN (Rumelhart et al., 1985). It has two hidden layers: h (stochastic binary) to capture topical information, while u (deterministic) to convey temporal information via BPTT that models the topic dependence at a time step t on all the previous steps τ < t. In contrast, DTM is built upon LDA (directed model), where Dirichlet distribution on words is not amenable to sequential modeling, therefore its natural parameters (topic and topic proportion distributions) for each topic are chained, instead of latent topics that results in intractable inference in topic detection and chaining.

Topic Dynamics: The introduction of explicit connection in latent topics in RNN-RSM allow new topics and words for the underlying topics to appear or disappear over time by the dynamics of topic correlations. As discussed, the distinction of h and u permits the latent topic h (t) to capture new topics, that may not be captured by h (t-1) .

DTM assumes a fixed number of global topics and models their distribution over time. However, there is no such assumption in RNN-RSM. We fixed the topic count in RNN-RSM at each time step, since W vh is fixed over time and RSM biases turn off/on terms in each topic. However, this is fundamentally different for DTM. E.g. a unique label be assigned to each of the 30 topics at any time steps t and t . DTM follows the sets of topic labels: {T opicLabels (t) } 30 k=1 = {T opicLabels (t ) } 30 k=1 , due to eq (1) in Blei and Lafferty (2006) (discussed in section 5) that limits DTM to capture new (or local) topics or words appeared over time. It corresponds to the keywordtrends (section 3.5).

Optimization: The RNN-RSM is based on Gibbs sampling and BPTT for inference while DTM employs complex variational methods, since applying Gibbs sampling is difficult due to the nonconjugacy of the Gaussian and multinomial distributions. Thus, easier learning in RNN-RSM.

For all models, approximations are solely used to compute the likelihood, either using variational approaches or contrastive divergence; perplexity was then computed based on the approximated likelihood. More specifically, we use variational approximations to compute the likelihood for DTM (Blei and Lafferty, 2006). For RSM and RNN-RSM, the respective likelihoods are approximated using the standard Contrastive Divergence (CD). While there are substantial differences between variational approaches and CD, and thus in the manner the likelihood for different models is estimated -both approximations work well for the respective family of models in terms of approximating the true likelihood. Consequently, perplexities computed based on these approximated likelihoods are indeed comparable.

# Conclusion and Future Work

We have proposed a neural temporal topic model which we name as RNN-RSM, based on probabilistic undirected graphical topic model RSM with time-feedback connections via deterministic RNN, to capture temporal relationships in historical documents. The model is the first of its kind that learns topic dynamics in collections of different-sized documents over time, within the generative and neural network framework. The experimental results have demonstrated that RNN-RSM shows better generalization (perplexity and time stamp prediction), topic interpretation (coherence) and evolution (popularity and drift) in scientific articles over time. We also introduced SPAN to illustrate topic characterization.

In future work, we forsee to investigate learning dynamics in variable number of topics over time. It would also be an interesting direction to investigate the effect of the skewness in the distribution of papers over all years. Further, we see a potential application of the proposed model in learning the time-aware i.e. dynamic word embeddings (Aitchison, 2001;Basile et al., 2014;Bamler and Mandt, 2017;Rudolph and Blei, 2018;Yao et al., 2018) in order to capture language evolution over time, instead of document topics.

# Acknowledgments

We thank Sujatha Das Gollapalli for providing us with the data sets used in the experiments. We express appreciation for our colleagues Florian Buettner, Mark Buckley, Stefan Langer, Ulli Waltinger and Usama Yaseen, and anonymous reviewers for their in-depth review comments. This research was supported by Bundeswirtschaftsministerium (bmwi.de), grant 01MD15010A (Smart Data Web) at Siemens AG-CT Machine Intelligence, Munich Germany.

