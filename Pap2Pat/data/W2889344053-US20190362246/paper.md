# Introduction

Large-scale knowledge graphs (KGs) support a variety of downstream NLP applications such as semantic search (Berant et al., 2013) and dialogue generation (He et al., 2017). Whether curated automatically or manually, practical KGs often fail to include many relevant facts. A popular approach for modeling incomplete KGs is knowledge graph embeddings, which map both entities and relations in the KG to a vector space and learn a truth value function for any potential KG triple parameterized by the entity and relation vectors (Yang et al., 2014;Dettmers et al., 2018). Embedding based approaches ignore the symbolic compositionality of KG relations, which limit their application in more complex reasoning tasks. An alternative solution for KG reasoning is to infer missing facts by synthesizing information from multi-hop paths, e.g. bornIn(Obama, Hawaii) ∧ locatedIn(Hawaii, US) ⇒ bornIn(Obama, US), as shown in Figure 1. Path-based reasoning offers logical insights of the underlying KG and are more directly interpretable. Early work treats it as a link prediction problem and perform maximum-likelihood classification over either discrete path features (Lao et al., 2011(Lao et al., , 2012;;Gardner et al., 2013) or their hidden representations in a vector space (Guu et al., 2015;Toutanova et al., 2016;McCallum et al., 2017).

More recent work formulates multi-hop reasoning as a sequential decision problem, and leverages reinforcement learning (RL) to perform effective path search (Xiong et al., 2017;Das et al., 2018;Shen et al., 2018;Chen et al., 2018). In particular, MINERVA (Das et al., 2018) uses the RE-INFORCE algorithm (Williams, 1992) to train an end-to-end model for multi-hop KG query answering: given a query relation and a source entity, the trained agent searches over the KG starting from the source and arrives at the candidate answers without access to any pre-computed paths.  (Kok and Domingos, 2007).

We refer to the RL formulation adopted by MINERVA as "learning to walk towards the answer" or "walk-based query-answering (QA)". Walk-based QA eliminates the need to precompute path features, yet this setup poses several challenges for training. First, because practical KGs are intrinsically incomplete, the agent may arrive at a correct answer whose link to the source entity is missing from the training graph without receiving any reward (false negative targets, Figure 2). Second, since no ground truth path is available for training, the agent may traverse spurious paths that lead to a correct answer only incidentally (false positive paths). Because REINFORCE (Williams, 1992) is an on-policy RL algorithm (Sutton and Barto, 1998) which encourages past actions with high reward, it can bias the policy toward spurious paths found early in training (Guu et al., 2017).

We propose two modeling advances for RL approaches in the walk-based QA framework to address the aforementioned problems. First, instead of using a binary reward based on whether the agent has reached a correct answer or not, we adopt pre-trained state-of-the-art embeddingbased models (Dettmers et al., 2018;Trouillon et al., 2016) to estimate a soft reward for target entities whose correctness cannot be determined. As embedding-based models capture link semantics well, unobserved but correct answers would receive a higher reward score compared to a true negative entity using a well-trained model. Second, we perform action dropout which randomly blocks some outgoing edges of the agent at each training step so as to enforce effective exploration of a diverse set of paths and dilute the negative impact of the spurious ones. Empirically, our overall model significantly improves over state-of-the-art multi-hop reasoning approaches on four out of five benchmark KG datasets (UMLS, Kinship,WN18RR). It is also the first pathbased model that achieves consistently comparable or better performance than embedding-based models. We perform a thorough ablation study and result analysis, demonstrating the effect of each modeling innovation.

# Approach

In this section, we first review the walk-based QA framework ( §2.2) and the on-policy reinforcement learning approach proposed by Das et al. (2018) ( §2.3, §2.4). Then we describe our proposed solutions to the false negative reward and spurious path problems: knowledge-based reward shaping ( §2.5) and action dropout ( §2.6).

## Formal Problem Definition

We formally represent a knowledge graph as G = (E, R), where E is the set of entities and R is the set of relations. Each directed link in the knowledge graph l = (e s , r, e o ) ∈ G represents a fact (also called a triple).

Given a query (e s , r q , ?), where e s is the source entity and r q is the relation of interest, the goal is to perform an efficient search over G and collect the set of possible answers E o = {e o } where (e s , r q , e o ) / ∈ G due to incompleteness.

## Reinforcement Learning Formulation

The search can be formulated as a Markov Decision Process (MDP) (Sutton and Barto, 1998): starting from e s , the agent sequentially selects an outgoing edge l and traverses to a new entity until it arrives at a target. Specifically, the MDP consists of the following components (Das et al., 2018).

States Each state s t = (e t , (e s , r q )) ∈ S is a tuple where e t is the entity visited at step t and (e s , r q ) are the source entity and query relation. e t can be viewed as the state-dependent information while (e s , r q ) are the global context shared by all states.

Actions The set of possible actions A t ∈ A at step t consists of the outgoing edges of e t in G, i.e., A t = {(r ′ , e ′ )|(e t , r ′ , e ′ ) ∈ G}. To give the agent the option to terminat a search, a self-loop edge is added to every A t . When search is unrolled for a fixed number of steps T , the self-loop acts similarly to a "stop" action.

Transition A transition function δ : S × A → S is defined by δ(s t , A t ) = δ(e t , (e s , r q ), A t ). In walk-based QA, the transition is determined by G.

Rewards In the default formulation, the agent receives a terminal reward of 1 if it arrives at a correct target entity when search ends and 0 otherwise.

R b (s T ) = {(e s , r q , e T ) ∈ G}.

(1)

## Policy Network

The search policy is parameterized using state information and global context, plus the search history (Das et al., 2018). Specifically, every entity and relation in G is assigned a dense vector embedding e ∈ d and r ∈ d . A particular action a t = (r t+1 , e t+1 ) ∈ A t is represented as the concatenation of the relation embedding and the end node embedding a t = [r; e ′ t ]. The search history h t = (e s , r 1 , e 1 , . . . , r t , e t ) ∈ H consists of the sequence of actions taken up to step t, and can be encoded using an LSTM:

(2)

where r 0 is a special start relation introduced to form a start action with e s . The action space A t is encoded by stacking the embeddings of all actions in it: A t ∈ |At|×2d . And the policy network π is defined as:

where σ is the softmax operator.

## Optimization

The policy network is trained by maximizing the expected reward over all queries in G:

(5) The optimization is done using the REIN-FORCE (Williams, 1992) algorithm, which iterates through all (e s , r, e o ) triples in G 1 and updates 1 This training strategy treats a query with n > 1 answers as n single-answer queries. In particular, given a query (es, rq, ?) with multiple answers {et 1 , . . . et n }, when training w.r.t. the example (es, rq, et i ), MINERVA removes all {et j |j ̸ = i} observed in the training data from the possible set of target entities in the last search step so as to force the agent to walk towards et i . We adopt the same technique in our training.

θ with the following stochastic gradient:

(6)

## Knowledge-Based Reward Shaping

According to Equation 1, the agent receives a binary reward based solely on the observed answers in G. However, G is intrinsically incomplete and this approach penalizes the false negative search attempts identically to true negatives. To alleviate this problem, we adopt existing KG embedding models designed for the purpose of KG completion (Trouillon et al., 2016;Dettmers et al., 2018) to estimate a soft reward for target entities whose correctness is unknown.

Formally, the embedding models map E and R to a vector space, and estimate the likelihood of each fact l = (e s , r, e t ) ∈ G using f (e s , r, e t ), a composition function of the entity and relation embeddings. f is trained by maximizing the likelihood of all facts in G. We propose the following reward shaping strategy (Ng et al., 1999):

(7) Namely, if the destination e T is a correct answer according to G, the agent receives reward 1. Otherwise the agent receives a fact score estimated by f (e s , r q , e T ), which is pre-trained. Here we keep f in its general form and it can be replaced by any state-of-the-art model (Trouillon et al., 2016;Dettmers et al., 2018) or ensemble thereof.

## Action Dropout

The REINFORCE training algorithm performs onpolicy sampling according to π θ (a t |s t ), and updates θ stochastically using Equation 6. Because the agent does not have access to any oracle path, it is possible for it to arrive at a correct answer e o via a path irrelevant to the query relation. As shown in Figure 1, the path Obama -endorsedBy→ Mc-Cain -liveIn→ U.S. ←locatedIn-Hawaii does not infer the fact bornIn(Obama, Hawaii).

Discriminating paths of different qualities is non-trivial, and existing RL approaches for walkbased KGQA largely rely on the terminal reward to bias the search. Since there are usually more spurious paths than correct ones, spurious paths are often found first, and following exploration can be increasingly biased towards them (Equation 6). At each time step t, the agent samples an outgoing link according to πθ (a t |s t ), which is the stochastic REINFORCE policy π θ (a t |s t ) perturbed by a random binary mask m. The agent receives reward 1 if stopped at an observed answer of the query (e s , r q , ?); otherwise, it receives reward f (e s , r q , e T ) estimated by the reward shaping (RS) network. The RS network is pre-trained and doesn't receive gradient updates.

Entities with larger fan-in (in-degree) and fan-out (out-degree) often exacerbate this problem. Guu et al. (2017) identified a similar issue in RL-based semantic parsing with weak supervision, where programs that do not semantically match the user utterance frequently pass the tests. To solve this problem, Guu et al. (2017) proposed randomized beam search combined with a meritocratic update rule to ensure all trajectories that obtain rewards are up-weighted roughly equally.

Here we propose the action dropout technique which achieves similar effect as randomized search and is simpler to implement over graphs. Action dropout randomly masks some outgoing edges for the agent in the sampling step of REIN-FORCE. The agent then performs sampling 2 according to the adjusted action distribution

where each entry of m ∈ {0, 1} |At| is a binary variable sampled from the Bernoulli distribution with parameter 1α. A small value ϵ is used to smooth the distribution in case m = 0, where πθ (a t |s t ) becomes uniform. Our overall approach is illustrated in Figure 3.

# Related Work

In this section, we summarize the related work and discuss their connections to our approach.

2 We only modify the sampling distribution and still use π θ (at|st) to compute the gradient update in equation 6.

## Knowledge Graph Embeddings

KG embeddings (Bordes et al., 2013;Socher et al., 2013;Yang et al., 2014;Trouillon et al., 2016;Dettmers et al., 2018) are one-hop KG modeling approaches which learn a scoring function f (e s , r, e o ) to define a fuzzy truth value of a triple in the embedding space. These models can be adapted for query answering by simply return the e o 's with the highest f (e s , r, e o ) scores. Despite their simplicity, embedding-based models achieved state-of-the-art performance on KGQA (Das et al., 2018). However, such models ignore the symbolic compositionality of KG relations, which limits their usage in more complex reasoning tasks. The reward shaping (RS) strategy we proposed is a step to combine their capability in modeling triple semantics with the symbolic reasoning capability of the path-based approach.

## Multi-Hop Reasoning

Multi-hop reasoning focus on learning symbolic inference rules from relational paths in the KG and has been formulated as sequential decision problems in recent works (Xiong et al., 2017;Das et al., 2018;Shen et al., 2018;Chen et al., 2018). In particular, DeepPath (Xiong et al., 2017) first adopted REINFORCE to search for generic representative paths between pairs of entities. DIVA (Chen et al., 2018) also performs generic path search between entities using RL and its variational objective can be interpreted as model-based reward assignment. MINERVA (Das et al., 2018) first introduced RL to search for answer entities of a particular KG query end-to-end. MINERVA uses entropy regularization to softly encourage the policy to sample diverse paths, and we show that hard action dropout is more effective in this setup. Reinforce-Walk (Shen et al., 2018) further proposed to solve the reward sparsity problem in walk-based QA using off-policy learning. ReinforceWalk scores the search targets with a value function which is updated based on the search history cached through epochs. In comparison, we leveraged existing embedding-based models for reward shaping, which is much more efficient during training.

## Reinforcement Learning

Recently, RL has seen a variety of applications in NLP including machine translation (Ranzato et al., 2015), summarization (Paulus et al., 2017), and semantic parsing (Guu et al., 2017). Compared to the domain of gaming (Mnih et al., 2013) where RL is mostly applied for, RL formulations in NLP often have a large discrete action space. For example, in machine translation, the space of possible actions is the entire vocabulary of a language. Walk-based QA also suffers from this problem, as some entities may have thousands of neighbors (e.g. U.S.). Since often there is no golden path available for a KG reasoning problem, we cannot leverage supervised pre-training to initialize the path search following the common practice in RL-based natural language generation (Ranzato et al., 2015). On the other hand, the inference paths being studied in a KG are often much shorter (usually containing 2-5 steps) compared to the target sentences in the NL generation problems (often containing 20-30 words), which simplifies the training to some extent.

# Experiment Setup

We evaluate our modeling contributions on five KGs from different domains and exhibiting different graph properties ( § 4.1). We compare with two classes of state-of-the-art KG models: multi-hop neural symbolic approaches and KG embeddings ( §4.2). In this section, we describe the datasets and our experiment setup in detail.

## Dataset

We adopt five benchmark KG datasets for query answering: (1) Alyawarra Kinship, (2) Unified Medical Language Systems (Kok and  2007), (3) FB15k-237 (Toutanova et al., 2015), (4) WN18RR (Dettmers et al., 2018), and (5) NELL-995 (Xiong et al., 2017). The statistics of the datasets are shown in Table 1.

## Baselines and Model Variations

We compare with three embedding based models: DistMult (Yang et al., 2014), ComplEx (Trouillon et al., 2016) and ConvE (Dettmers et al., 2018). We also compare with three multi-hop neural symbolic models: (a) NTP-λ, an improved version of Neural Theorem Prover (Rocktäschel and Riedel, 2017), (b) Neural Logical Programming (Neu-ralLP) (Yang et al., 2017) and (c) MINERVA. For our own approach, we include two model variations that use ComplEx and ConvE as the reward shaping modules respectively, denoted as Ours(ComplEx) and Ours(ConvE). We quote the results of NeuralLP, NTP-λ and MINERVA reported in Das et al. (2018), and replicated the embedding based systems.3 

## Implementation Details

Beam Search Decoding We perform beam search decoding to obtain a list of unique entity predictions. Because multiple paths may lead to the same target entity, we compute the list of unique entities reached in the final search step and assign each of them the maximum score of all paths that led to it. We then output the top-ranked unique entities. We find this approach to improve over directly taking the entities ranked at the beam top, as many of them are repetitions.

KG Setup Following previous work, we treat every KG link as bidirectional and augment the graph with the reversed (e o , r -1 , e s ) links. We use the same train, dev, and test set splits as Das et al. (2018). We exclude any link from the dev and Model UMLS Kinship FB15k-237 WN18RR NELL-995 @1 @10 MRR @1 @10 MRR @1 @10 MRR @1 @10 MRR @1 @10 MRR DistMult (Yang et al., 2014)  Table 2: Query answering performance compared to state-of-the-art embedding based approaches (top part) and multi-hop reasoning approaches (bottom part). The @1, @10 and MRR metrics were multiplied by 100. We highlight the best approach in each category.

test set (and its reversed link) from the train set. Following Das et al. (2018), we cut the maximum number of outgoing edges of an entity by threshold η to prevent GPU memory overflow: for each entity we keep its top-η neighbors with the highest PageRank scores (Page et al., 1999) in the graph.

Hyperparameters We set the entity and relation embedding size to 200 for all models. We use Xavier initialization (Glorot and Bengio, 2010) for the embeddings and the NN layers. For ConvE, we use the same convolution layer and label smoothing hyperparameters as Dettmers et al. (2018). For path-based models, we use a three-layer LSTM as the path encoder and set its hidden dimension to 200. We perform grid search on the reasoning path length (2, 3), the node fan-out threshold η (256-512) and the action dropout rate α (0.1-0.9). Following Das et al. (2018), we add an entropy regularization term in the objective and tune the weight parameter β within 0-0.1. We use Adam optimization (Kingma and Ba, 2014) and search the learning rate (0.001-0.003) and mini-batch size (128-512).4 For all models we apply dropout to the entity and relation embeddings and all feed-forward layers, and search the dropout rates within 0-0.5. We use a decoding beam size of 512 for NELL-995 and 128 for the other datasets.  Das et al. (2018).

Our Pytorch implementation of all experiments is released at https://github.com/ salesforce/MultiHopKG.

# Results

## Model Comparison

Table 2 shows the evaluation results of our proposed approach and the baselines. The top part presents embedding based approaches and the bottom part presents multi-hop reasoning approaches. 5We find embedding based models perform strongly on several datasets, achieving overall best evaluation metrics on UMLS, Kinship, FB15K-237 and NELL-995 despite their simplicity. While previous path based approaches achieve comparable performance on some of the datasets (WN18RR, NELL-995, and UMLS), they perform significantly worse than the embedding based models on the other datasets (9.1 and 14.2 absolute points lower on Kinship and FB15k-237 respectively). A possible reason for this is that embedding based methods map every link in the KG into the same embedding space, which implicitly encodes the connectivity of the whole graph. In contrast, path based models use the discrete represen- tation of a KG as input, and therefore have to leave out a significant proportion of the combinatorial path space by selection. For some path based approaches, computation cost is a bottleneck. In particular, NeuralLP and NTP-λ failed to scale to the larger datasets and their results are omitted from the table, as Das et al. (2018) reported.

Ours is the first multi-hop reasoning approach which is consistently comparable or better than embedding based approaches on all five datasets. The best single model, Ours(ConvE), improves the SOTA performance of path-based models on three datasets (UMLS, Kinship, and FB15k-237) by 4%, 9%, and 39% respectively. On NELL-995, our approach did not significantly improve over existing SOTA. The NELL-995 dataset consists of only 12 relations in the test set and, as we further detail in the analysis ( § 5.3.3), our approach is less effective for those relation types.

The model variations using different reward shaping modules perform similarly. While a better reward shaping module typically in a better overall model, an exception is WN18RR, where ComplEx performs slightly worse on its own but is more helpful for reward shaping. We left the study of the relationship between the reward shaping module accuracy and the overall model performance as future work.

## Ablation Study

We perform an ablation study where we remove reward shaping (-RS) and action dropout (-AD) from Ours(ConvE) and compare their MRRs to the whole model on the dev sets. 6 As shown in Table 3, on most datasets, removing each component results in a significant performance drop. The exception is WN18RR, where removing the ConvE reward shaping module improves the performance. 7 Removing reward shaping on NELL-6 According to Table 3 andTable 2, the dev and test set evaluation metrics differ significantly on several datasets. We discuss the cause of this in § A.2.

7 A possible explanation for this is that as path-based models tend to outperform the embedding based approaches on WN18RR, ConvE may be supplying more noise than useful 995 does not change the results significantly. In general, removing action dropout has a greater impact, suggesting that thorough exploration of the path space is important across datasets.

## Analysis

### Convergence Rate

We are interested in studying the impact of each proposed enhancement on the training convergence rate. In particular, we expect reward shaping to accelerate the convergence of RL (to a better performance level) as it propagates prior knowledge about the underlying KG to the agent. On the other hand, a fair concern for action dropout is that it can be slower to train, as the agent is forced to explore a more diverse set of paths. Figure 4 eliminates this concern.

The first row of Figure 4 shows the changes in dev set MRR of Ours(ConvE) (green * ) and the two ablated models w.r.t. # epochs. In general, the proposed approach is able to converge to a higher accuracy level much faster than either of the ablated models and the performance gap often persists until the end of training (on UMLS, Kinship,. Particularly, on FB15k-237, our approach still shows improvement even after the two ablated models start to overfit, with -AD beginning to overfit sooner. On WN18RR, introducing reward shaping hurt dev set performance from the beginning, as discussed in § 5.2. On NELL-995, Ours(ConvE) performs significantly better in the beginning, but -RS gradually reaches a comparable performance level.

It is especially interesting that introducing action dropout immediately improves the model performance on all datasets. A possible explanation for this is that by exploring a more diverse set of paths the agent learns search policies that generalize better.

### Path Diversity

We also compute the total number of unique paths the agent explores during training and visualize its change w.r.t. # training epochs in the second row of Figure 4. When counting a unique path, we include both the edge label and intermediate entity.

information about the KG. Yet counter-intuitively, we found that adding the ComplEx reward shaping module helps, despite the fact that ComplEx performs slightly worse than ConvE on this dataset. This indicates that dev set accuracy is not the only factor which determines the effectiveness of reward shaping.   First we observe that, on all datasets, the agent explores a large number of paths before reaching a good performance level. The speed of path discovery slowly decreases as training progresses. On smaller KGs (UMLS and Kinship), the rate of encountering new paths is significantly lower after a certain number of epochs, and the dev set accuracy plateaus correspondingly. On much larger KGs (FB15k-237, WN18RR, and NELL-995), we did not observe a significant slowdown before severe overfitting occurs and the dev set performance starts to drop. A possible reason for this is that the larger KGs are more sparsely connected compared to the smaller KGs (Table 1), therefore it is less efficient to gain generalizable knowledge from the KG by exploring a limited proportion of the path space through sampling. Second, while removing action dropout significantly lowers the effectiveness of path exploration (orange vs. green * ), we observe that removing reward shaping (blue △) slightly increases the # paths visited if the action dropout rate is kept the same. This indicates that the correlation between # paths explored and dev set performance is not strictly positive. The best performing model is not always the model that explored the largest # paths. It also demonstrates the role of reward shaping as a regularizer which guides the agent to avoid noisy paths with its prior knowledge.

### Performance w.r.t. Relation Types

We investigate the behaviors of our proposed approach w.r.t different relation types. For each KG, we classify its set of relations into two categories based on the answer set cardinality. Specifically, we define the metric ξ r as the average answer set cardinality of all queries with topic relation r. We count r as a "to-many" relation if ξ r > 1.5, which indicates that most queries in relation r has more than 1 correct answer; we count r as a "to-one" relation otherwise, meaning most queries of this relation have only 1 correct answer.

Table 4 shows the percentage of examples of tomany and to-one relations on each dev dataset and the MRR evaluation metrics of previously studied models computed on the examples of each relation  type. Since UMLS and Kinship are densely connected, they almost exclusively contain to-many relations. FB15k-237 mostly contains to-many relations. In Figure 4, we observe the biggest relative gains from the ablated models on these three datasets. WN18RR is more balanced and consists of slightly more to-many relations than toone relations. The NELL-995 dev set is a unique one which almost exclusively consists of to-one relations. There is no common performance pattern over the two relation types across datasets: on some datasets all models perform better on tomany relations (UMLS, WN18RR) while others show the opposite trend (FB15k-237, NELL-995).

We leave the study of these discrepancies to future work.

We show the relative performance change of the ablated models -RS and -AD w.r.t. Ours(ConvE) in parentheses. We observe that in general our proposed enhancements are effective in improving query-answering over both relation types (more effective for to-many relations). However, adding the ConvE reward shaping module on WN18RR hurts the performance over both to-many and toone relations (more for to-one relations). On NELL-995, both techniques hurt the performance over to-many relations. Unseen Queries

Since most benchmark datasets randomly split the KG triples into train, dev and test sets, the queries that have multiple answers may fall into multiple splits. As a result, some of the test queries (e s , r q , ?) are seen in the training set (with a different set of answers) while the others are not. We investigate the behaviors of our proposed approach w.r.t. seen and unseen queries.

Table 5 shows the percentage of examples associated with seen and unseen queries on each dev dataset and the corresponding MRR evaluation metrics of previously studied models. On most datasets, the ratio of seen vs. unseen queries is similar to that of to-many vs. to-one relations (Table 4) as a result of random data split, with the exception of WN18RR. On some datasets, all models perform better on seen queries (UMLS, Kinship, WN18RR) while others reveal the opposite trend. We leave the study of these model behaviors to future work. On NELL-995 both of our proposed enhancements are not effective over the seen queries. In most cases, our proposed enhancements improve the performance over unseen queries, with AD being more effective.

# Conclusions

We propose two modeling advances for end-toend RL-based knowledge graph query answering: (1) reward shaping via graph completion and (2) action dropout. Our approach improves over state-of-the-art multi-hop reasoning models consistently on several benchmark KGs. A detailed analysis indicates that the access to a more accurate environment representation (reward shaping) and a more thorough exploration of the search space (action dropout) are important to the performance boost.

On the other hand, the performance gap between RL-based approaches and the embeddingbased approaches for KGQA remains. In future work, we would like to investigate learnable reward shaping and action dropout schemes and apply model-based RL to this domain.

# Acknowledgements

We thank Mark O. Riedl, Yingbo Zhou, James Bradbury and Vena Jia Li for their feedback on early draft of the paper, and Mark O. Riedl for helpful conversations on reward shaping. We thank the anonymous reviewers and the Salesforce research team members for their thoughtful comments and discussions. We thank Fréderic Godin for pointing out an error in Equation 8 in an early version of the paper.

