# INTRODUCTION

Recommendation systems learn user preferences through user-item interactions such as user clicks. Usually, a user click is considered as a positive sample that indicates the user's interest in the clicked item while a no-click between a user-item pair is considered as a negative sample. A click-through rate (CTR) prediction model outputs click probabilities of user-item pairs, and such probabilities can be used to rank items upon a user's request. A CTR model is trained using data collected from online platforms, where user-item pairs with no-clicks dominate. The imbalance of the dataset [4] justifies negative sampling (NS), which down-samples negative samples and significantly reduces model training costs.

In contrast to treating all data points as equally important, nonuniform subsampling aims to obtain more informative samples. Previous model-based methods [8,9,14,32,34,35,40] utilize a pilot model to assess the importance of data. When the pilot model is correctly pre-trained, one can achieve the optimal sampling rate: the method is measuring the importance of data using pilot prediction scores together with first and second-order derivatives of the loss function [35]. Since optimal negative sampling rates are proportional to the pilot model's prediction score, a high sampling rate indicates an inaccurate model prediction. Thus, one can interpret the sampling strategy as using hard negative samples (HNS) [8,40].

We find that model-based sampling algorithms may not be applicable in real industrial scenarios. Figure 1 demonstrates how a real recommendation system deploys data subsampling. A user initiates a request to the online serving model and receives recommendations returned by the server. If the user clicks the recommended item, then a positive instance is collected. Otherwise, if the user does not click the item within a period of time, a negative instance is collected. Note that the pilot prediction score and other statistics are recorded in the instance to calculate the sampling rate. All instances are filtered by the data subsampling module before I/O to reduce the I/O and network bandwidth bottleneck. Offline models are trained with historical data before being deployed online.

In these scenarios, there are two unavoidable obstacles to the application of model-based sampling. First, offline model training Figure 1: A simplified recommendation system. A user initiates a request to the online serving model and receives recommendations returned by the server. User clicks will trigger positive instances, while non-clicks will trigger negative instances. All instances are filtered by the data subsampling module. For model-based methods, subsampling rates are determined by online models (e.g. model v1), thus sub-optimal for offline training (e.g. model v2) purposes. When model v2 is deployed online, data subsampling is affected, producing inconsistent subsampling rates.

is vulnerable to model misspecification, which leads to inferior results. Unfortunately, model misspecification is persistent due to online-offline discrepancy, especially in continuous integration and deployment (CI/CD) [28] in real systems. Second, coupling data subsampling and model training introduces extra dependencies across system modules, which increases system maintenance cost and brings about extra technical debt [27].

To maintain a scalable and sustainable data subsampling service, we propose model-agnostic data subsampling methods based on user-item bipartite graphs. In the bipartite graph, two sets of nodes represent users and items separately, and each edge represent interactions between a user and an item. Then we treat edges as instances to consider subsampling. In the context of a bipartite graph, we reinterpret the idea of HNS using effective conductance [7]. An edge is considered a hard instance if the effective conductance over its two nodes is high. With this notion of hardness, we assign high sampling rates to edges with high effective conductance. Additionally, we exploit the bipartite graph to propagate and refine the sampling rates. Since our proposed method is model-agnostic, we can marry the merits of both model-agnostic and model-based subsampling methods. Empirically, we show that combing the two consistently improves over any single method on the widely used datasets. To summarize our contribution:

• we propose a model-agnostic method to measure data hardness scores via effective conductance on the user-item bipartite graph; 

# PRELIMINARIES

We consider a binary classification problem and let D = {(x 𝑛 , 𝑦 𝑛 )} 𝑁 𝑛=1 be a training set of size 𝑁 . Here x 𝑛 and 𝑦 𝑛 are, respectively, the feature vector and label of instance 𝑛. We study the generalized logistic regression (GLM) model, where the target model corresponding to the offline model (e.g., model v2 before deployment in Figure 1) is represented as

where the log-odd 𝑔(x; 𝜃 ) is implemented by a predictive model. Denote 𝑁 0 as the number of negative instances and 𝑁 1 = 𝑁 -𝑁 0 as the number of positive instances. We study the case where D is imbalanced, i.e., 𝑁 0 ≫ 𝑁 1 . Since information is sparsely distributed over many negative instances [34], we often use NS to reduce the dataset size and boost training efficiency.    An NS algorithm weighs each negative instance x with some measurement of its importance 𝜋 (x). The importance 𝜋 (x) is used as the negative sampling rate (NSR) of x. The assignment of 𝜋 (x) follows a widely-used heuristic, which is exploiting "hard negative samples" [18,25]. Sampling rates are proportional to non-negative hardness scores ℎ(•):

where 𝛼 ∈ (0, 1] is a pre-set average subsampling rate of negative instances. Suppose we have a pilot model f (•) corresponding to online model v1 in Figure (2). When f (•) = 𝑓 (•; 𝜃 * ), that is f (•) has the same functional form as the target model, and 𝜃 * is the true parameter. Then we can set a model-based hardness score ℎ 𝑏 (x 𝑛 ) = f (x 𝑛 ) = 𝑓 (x 𝑛 ; 𝜃 * ) to get a near-optimal sampling rate 𝜋 (x 𝑛 ) by Eqn. (2) [35]. Intuitively, a negative instance predicted with a higher score by the pilot model f (•) is more "surprising" and thus is harder for the target model 𝑓 (•; 𝜃 ). Note that we use 𝜋 (x) for a positive instance to denote its counterfactual negative sampling rate. We demonstrate the HNS procedure in Algorithm 1.

Since data distribution shifts after subsampling, one needs to correct the log odds to get an unbiased estimation:

where 𝛿 𝑛 ∈ {0, 1} is the subsampling indicator and ℓ 𝑛 := log 𝜋 (x 𝑛 ).

[14] proves that log odds correction is more efficient than the IPW estimator [17]. However, when the pilot model is misspecified, optimal NS with pilot models is not achieved. In real scenarios, it may be error-prone to deploy model-based HNS methods since we persistently suffer from model misspecification problems due to online-offline model discrepancy and continuous integration and deployment. Thus, it is tempting to use model-agnostic hardness score ℎ 𝑎 (•) to maintain a scalable and sustainable data subsampling service.

# METHODOLOGY

An overview of our workflow is demonstrated in Figure 2. We introduce its technical details step by step.

## MA-EC: Model-agnostic Negative Hardness Estimation via Effective Conductance

In this section, we consider the subsampling problem in the context of a bipartite graph formed from a recommendation problem. Let the bipartite graph be (𝑈 , 𝑉 , 𝐸), where the node set 𝑈 = {𝑢 𝑖 } 𝑀 𝑖=1 represents 𝑀 users, the node set 𝑉 = {𝑣 𝑗 } 𝑄 𝑗=1 represents 𝑄 items, and the edge set 𝐸 = {(𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 )} 𝑁 𝑛=1 represent 𝑁 user-item pairs. For each node pair 𝑛, 𝑦 𝑛 ∈ {0, 1} represents whether there is a positive interaction between 𝑢 𝑖 𝑛 and 𝑣 𝑗 𝑛 .

In our classification problem, each feature x 𝑛 = (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 , c 𝑛 ), where c 𝑛 represent context features. And its label is 𝑦 𝑛 . We aim to compute the model-agnostic hardness ℎ 𝑎 (•) of negative samples without referring to a pilot model.

We relate sample hardness to graph topology. Imagine the useritem graph as an electricity network, where each edge (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) is a conductor with conductance 𝐺 (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ), which measures the edge's ability in transferring electrical current. We expect 𝐺 (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) to be large when user 𝑢 𝑖 𝑛 expresses direct preference of item 𝑣 𝑗 𝑛 . Particularly, we set

It means that the conductance is one if there is a direct preference or 0 otherwise. Then we consider the effective conductance 𝐺 eff (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) between 𝑢 𝑖 𝑛 and 𝑣 𝑗 𝑛 . It represents the network's ability to transfer current from 𝑢 𝑖 𝑛 to 𝑣 𝑗 𝑛 (or the opposite direction). The effective conductance  they are defined as follows [1].

Here e[•] ∈ {0, 1} 𝑀+𝑄 is the one-hot encoding of a node in the graph, and L + is the pseudo inverse of the Laplacian of the graph.

Intuitively, if there are many conductible paths between 𝑢 𝑖 𝑛 and 𝑣 𝑗 𝑛 , then the effective conductance 𝐺 eff (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) is large.

Estimating sample hardness via effective conductance. Figure 3 demonstrates that effective conductance positively relates to sample hardness. Define the hardness score as

For a negative sample, 𝐺 (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) = 0. The effective conductance 𝐺 eff (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) is high when there are multiple high-conductance paths from 𝑢 𝑖 𝑛 to 𝑣 𝑗 𝑛 , demonstrating user's indirect preference to the item. When the indirect preference is high but (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) turns out to be negative, we identify it as a hard negative sample. For a positive sample, ℎ 𝑎 (x 𝑛 ) denotes its counterfactual hardness score by subtracting the direct conductor 𝐺 (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) from 𝐺 eff (𝑢 𝑖 𝑛 , 𝑣 𝑗 𝑛 ) to eliminate the prior information given by the label. The hardness score is used to calculate the counterfactual NSR for log odds correction in Eqn. (3). We do not drop positive samples.

Implementation. Direct calculation of effective conductance is time-consuming. Instead, we first approximate the commute time distance comm(𝑢, 𝑣) through random walk using scientific computing tools [31]. Then we use the transformation 𝐺 eff (𝑢, 𝑣) = 2|𝐸|/comm(𝑢, 𝑣) [3] to convert the commute time into effective conductance.

## Smoothing Hardness Scores through Edge Propagation

The effective conductance derived from the sparsified graph is noisy, leading to an inaccurate estimation of hardness scores1 . We use the idea of graph propagation to smooth the hardness score. While existing machine learning literature focuses on propagating node attributes (e.g., node features or labels) to smooth out node-level uncertainty [19,20], propagating edge attributes is underexplored. We reduce edge propagation to node propagation by transforming user-item bipartite graph (𝑈 , 𝑉 , 𝐸) into its corresponding line graph 𝐿(𝑈 , 𝑉 , 𝐸) = (𝑉 𝐿 , 𝐸 𝐿 ), where 𝑉 𝐿 = 𝐸 and 𝐸 𝐿 is the collection of edge pairs that share the same node [15].

𝑛=1 ∈ {0, 1} 𝑁 to be the vector of the effective conductance scores and edge labels, respectively. Similar to [20], we normalize the effective conductance 𝐺 eff as the estimated score 𝑍 and calculate the uncertainty score 𝐵 as the absolute residual between 𝑍 and 𝑌

Here we use the min-max normalization to restrict the hardness score to be within the range

, where 𝐴 𝐿 , 𝐷 𝐿 are the adjacency matrix and the degree matrix of the line graph, respectively. We smooth the uncertainty by solving the following optimization problem [42]:

The first term in Eqn. (8) restricts the difference of uncertainties in neighboring nodes. And the second term constrains the smoothed uncertainty to be close to the initial uncertainty, with the coefficient 𝜇 controlling the strength of the constraint. With the smoothed uncertainty vector B, we correct the hardness estimation by reversing Eqn. ( 7)

[ 19,42] also introduced an iterative approximation approach. Let 𝛾 = 1/(1 + 𝜇) and

Then 𝐵 𝑡 → B when 𝑡 → ∞. However, this iterative approach is not scalable as the transformed line graph has

𝑁 edges in total, where Deg(•) represents node degree. Alternatively, we can directly propagate edge uncertainty along the original graph (𝑈 , 𝑉 , 𝐸), which only contains |𝐸| = ( 𝑢 𝑖 ∈𝑈 Deg(𝑢 𝑖 ) + 𝑣 𝑗 ∈𝑉 Deg(𝑣 𝑗 ))/2 edges in total. The propagation rule over edges is as follows

where

Using message passing mechanisms, we store the aggregated uncertainty 𝑚 𝑡 (𝑢) in 𝑢 and then update the uncertainty 𝐵 𝑡 +1 by applying the rule above.

Score propagation. Instead of propagating uncertainty, we can directly propagate the scores Ẑ by iterating

until convergence. After obtaining the final hardness scores, we rescale them to match the average subsampling rates 𝛼. We find that smoothing hardness scores benefits both model-agnostic and model-based methods.

## Combining Model-agnostic and Model-based Methods

We have described our model-agnostic data subsampling methods in previous sections. Some hard instances may be overlooked by model-agnostic methods while they can be captured by modelbased methods. Hence, in this section, we show how to combine these two methods to marry the merits of both and achieve a better sampling performance. Given a sample x, model-agnostic and model-based subsampling methods calculate their corresponding sampling rate 𝜋 D (x) and 𝜋 𝜙 (x) respectively. Particularly 𝜋 𝜙 (x) is the subsampling rate for x by using pilot model ℎ 𝑏 (•) := f (•; 𝜙), and 𝜋 D (x) is the subsampling rate using model-agnostic hardness score ℎ 𝑎 (•) in Eqn. ( 6):

(𝜚 𝜙 , 𝜚 D ) is the minimum sampling rate, and (𝜌 𝜙 , 𝜌 D ) are tuned to meet the average subsampling rate 𝛼.

We propose three simple yet effective heuristic strategies to combine these two methods and get the final sampling rate: maximum, mean, and product.

𝜋 mean (x) = (𝜋 D (x) + 𝜋 𝜙 (x))

# ;

𝜋 prod (x) = min max 𝜌 prod 𝜋 D (x)𝜋 𝜙 (x) , 𝜚 prod ), 1 .

Note 𝜚 prod is an extra hyperparameter when applying product combination. And (𝜌 max , 𝜌 prod ) are tuned to normalize the average sample rate to 𝛼. After the subsampling rate combination, each x will be sampled with probability in Eqn. (14). All the sampled instances will follow the normal training protocol to optimize the training objective as shown in Eqn. (3) which guarantees the final result to be wellcalibrated.

## Theoretical bottlenecks of model-based subsampling

Above, we propose a principled approach to determine the sample's hardness by analyzing graph structures within the data without referring to a pilot model. We advocate this model-agnostic sampling method due to the dilemma of unavoidable model misspecification in the online-offline discrepancy setup. a correctly specified pilot model is needed to derive a theoretically efficient data subsampling method. Under pilot model misspecifications, it is even non-trivial to guarantee model consistency (the subsampled estimator has the same limit as the full data estimator) for the log odds correction estimator (Eqn. 3) [9,14,29]. Therefore, pilot model misspecification is a realistic but underexplored problem in statistics.

# EXPERIMENTS

We compare various subsampling methods on downstream target model performance. First, for model-based sampling, we show that pilot misspecification will lead to discrepancies in model performance. Second, we report empirical results over two datasets to demonstrate the superiority of our model agnostic subsampling method. Third, we conduct extensive ablation studies to investigate the effectiveness of model-agnostic hardness score, score propagation, and the benefit of ensembling model-agnostic and model-based methods. Finally, we discuss effective resistance and its relationship to negative sampling.

## Datasets and data pre-processing

We demonstrate our empirical results using KuaiRec [10] and Microsoft News Dataset (MIND) [37]. The statistics of the pre-processed datasets are shown in Table 1. For both datasets, we use 80% of the data for training, 10% for validation, and 10% for testing. We report all experimental results for 8 runs with random initializations on one random data split. We set the average subsampling rate 𝛼 = 0.2 on training data for both datasets.

KuaiRec. KuaiRec is a recommendation dataset collected from the video-sharing mobile app "Kuaishou". The dataset is generally a sparse user-item interaction matrix with a fully-observed small submatrix. We crop the fully-observed submatrix and only consider the rest entries in the sparse matrix since those data are collected under natural settings. We use the label "watch_ratio", which represents the total duration of a user watching a video divided by the video duration. Since a user may watch a video multiple times, the watch ratio can be larger than 1. In the experiment, we consider a user like a video (positive) if the "watch_ratio" is larger than 3.

# MIND. MIND is a large-scale news recommendation dataset with binary labels indicating users' impressions of recommended news.

We do not use the content data in each news corpus during the experiment. The MIND dataset does not require extra pre-processing.

## Baselines and model selections

Baseline subsampling methods. We consider two baselines -the first baseline is the model-agnostic uniform negative sampling; the second is a model-based near-optimal sampling method (Opt-Sampling) [35], which relies on the prediction scores of a pilot model as the hardness score to calculate sample rates.  We study the scenario where data subsampling rates are pre-computed and do not change during model training. This scenario is aligned with industrial applications such as recommendation systems, where negative data are subsampled before saving in distributed storage to get rid of huge saving costs. Our method contrasts previous studies to re-compute and subsample data on the fly. For example, SRNS [8] quantifies sample hardness by estimating the variance of the model prediction along training epochs, which is dynamically updated each time model sees the sample. IRGAN [36] uses a GAN model where the generator draws negative samples from the negative pool and mixes them with positive samples. A discriminator classifies data and guides the generator to learn to sample hard negatives. These methods are not comparable to our work. To the best of our knowledge, Opt-Sampling [35] is the only representative method that allows for a fair comparison in the specific scenario considered by this work.

# W&D

Model architecture. We choose the wide and deep model (W&D) [6] as our training target model to validate the effectiveness of our model-agnostic method. For model-based subsampling methods, we need to pre-train a pilot model to estimate the sample hardness. To test the effect of pilot misspecification, we consider five types of pilot models: (1) W&D model [6]; (2) Linear logistic regression (LR); (3) Automatic feature interaction selection model (AFI) [22]; (4) Neural factorization machines (NFM) [16]; (5) Deep factorization machine (DFM) [12]. In the rest of the experiments, unless otherwise specified, W&D is used as the pilot model since it shares the same architecture as the target model (consistent pilot). All pilot models are trained using 10% of the training data.

## Pilot misspecification

Model-based subsampling methods can be sensitive to a misspecified pilot model. We fix the target model architecture and tune the pilot model architectures to study their effect on the KuaiRec dataset. Pilot models affect target model performance only through their generated samples. Figure 4  pilots. The AUC difference is significant since the standard deviation is around 0.001, demonstrating a potential loss in large-scale recommendation systems processing millions of data points daily. This result consolidates the negative effect of pilot misspecification, which justifies using model-agnostic subsampling approaches.

In Figure 4, there is a big difference in target models' test performance among misspecified pilot models. We further study the quality of pilot models w.r.t. their predictive performance. Table 2 demonstrates pilot models' training and testing AUC. Deep pilot models may overfit the training data since we use 1/10 data to pretrain pilot models. LR is less vulnerable to overfitting and achieves the highest test AUC. There is a caveat to using a misspecified pilot model, e.g. AFI in our case since the outcome can be worse than uniform sampling even when AFI can make reasonable predictions. Using a consistent pilot model (W&D) is a safer choice: even when its predictive performance is worse than a misspecified NFM pilot model, the target model can benefit from pilot model consistency and achieve better testing AUC.

Note that W&D is a strong architecture on the KuaiRec dataset. Table 3 shows that when using LR as the target model and trained on the same amount of data, its performance is worse than the one using W&D as the target model: W&D achieves 0.8553 in testing AUC with uniform sampling while LR gets 0.8474. Table 3 demonstrates both model-based sampling with a consistent pilot (Opt.Samp.) and model-agnostic sampling (MA-EC) can improve model performance. MA-EC consistently helps, disregarding the model specification.

## Experiment results on two datasets

We train the target model with different data sampling strategies and evaluate the model performance based on the area under the receiver operating characteristic curve (AUC). The results of all training configurations are presented in Figure 5. The comparison between the methods shows that the MA-EC strategy consistently outperforms the uniform sampling baseline in both datasets. Furthermore, when applied to the KuaiRec dataset, the MA-EC strategy achieved comparable performance to the Optimal Sampling method. However, in the MIND dataset, the Optimal Sampling approach did not improve upon the uniform sampling baseline and was outperformed by the MA-EC strategy. These results demonstrate the effectiveness of the MA-EC method in achieving improved performance in different datasets. Additionally, the results were improved by incorporating a smoothing technique for hardness estimation through propagation. The performance of combining the model-agnostic and model-based methods using the maximum strategy was also reported. It was observed that the ensemble approach outperformed each individual method in both datasets. The smoothed scores from Opt-Sampling and MA-EC were also combined using the ensemble approach, resulting in the best performance as shown in the last column of the results. These findings highlight the benefits of combining multiple techniques to achieve even better performance in the target model training process. The use of smoothing and ensembling strategies demonstrates the potential for further improvements in data sampling methods and the effectiveness of combining multiple approaches to achieve better results.  4: Control experiment. Some negative samples have low subsampling rates in one method but have large subsampling rates in the other. Flipping those subsampling rates from small to large improves model performance.

# U n if

## Ablation studies

We use the KuaiRec dataset to conduct extensive ablation studies. First, we study if our method consistently outperforms baselines under different subsampling rates. Second, we show that MA-EC and Opt-Sampling can estimate sample hardness from different perspectives by designing a variable control experiment. And we investigate the effectiveness of different ensemble strategies. Third, we show how smoothing scores help further improve model performance.

Subsampling rate. We compare uniform sampling with the best of our methods by ensembling smoothed scores from Opt-Sampling and MA-EC. Figure 6 demonstrates our methods consistently outperform uniform sampling under different subsampling rates.

Ensemble strategies. To investigate whether hardness scores from MA-EC and Opt-Sampling complement each other, we design the following control experiment: (1) we assign instances with subsampling rates from each method; (2) for instances that have inconsistent subsampling rates between two methods, we flip their subsampling rates into the other method. For example, we assign instances that have 𝜋 D (x) < 0.2 and 𝜋 𝜙 (x) > 0.8 with the subsampling rate 𝜋 𝜙 (x), and the rest instances with 𝜋 D (x).   model performance by assigning most of the sample with one set of scores and flipping part of the sample scores. This verifies that some hard negative instances might be overlooked by one method and can be discovered by the other.

The control experiment justifies ensembling MA-EC and Opt-Sampling. We experiment with ensemble strategies (maximum, mean, and product). Figure 7(a) shows the box plot of the three ensemble methods. For each method, we present nine configurations of the hyperparameters (𝜚 D , 𝜚 𝜙 ), where 𝜚 D ∈ {0.1, 0.12, 0.14} and 𝜚 𝜙 ∈ {0.005, 0.01, 0.03}. For product strategy, we set hyperparameter 𝜚 prod = 0.005 for all experiments. We observe that the maximum strategy consistently gives comparable or better results than Opt-Sampling and MA-EC. While in mean and product strategies, we do not observe significant improvement. For the product strategy, the model performance even deteriorates. MA-EC needs to compute effective conductance to calculate subsampling rates. Effective conductance computation is not our bottleneck since it can be reused once computed. MA-EC is model-agnostic, and thus can support training with different target models. Score correction. We investigate the effectiveness of correcting the hardness scores via graph propagation. We are interested in applying score correction in Opt-Sampling and MA-EC and their ensemble. Additionally, in applying both score correction and score ensemble, we can try either ensembling corrected scores or correcting ensemble scores. As we find the latter consistently results in worse performance, we only present the result of the former in this work. Figure 7(b) reports the model performance of our ablation study. For the experiments of correcting scores estimated from Opt-Sampling and MA-EC, we explore the propagation coefficient 𝛾 ∈ {0.05, 0.1, 0.2, 0.3, 0.4}. For each coefficient, we iterate to smooth the scores until convergence. Uncertainty propagation significantly improves model performance for both subsampling approaches. In score propagation, which runs on scores corrected by uncertainty propagation, model performance slightly improves in Opt-Sampling and worsens in MA-EC. In the ensemble of corrected scores, we combine the hardness scores from the best configurations of both methods via maximum strategy. The reported result demonstrates that the ensemble strategy improves model performance over not only the original scores but also the corrected scores.

## A note on effective resistance

The effective resistance 𝑅 eff (𝑢, 𝑣) = 1/𝐺 eff (𝑢, 𝑣) is often used for graph sparsification [30]. An edge with high effective resistance is considered important in maintaining graph topology. Since the definitions of edge importance using effective conductance and effective resistance run against each other, we demonstrate that defining edge importance with effective resistance is not applicable in our scenario. We compare two model-agnostic (MA) subsampling methods with effective resistance (MA-ER) and effective conductance (MA-EC) as the hardness scores. The effective resistance is computed on the graph where all edges have unit resistances. We demonstrate that MA-ER fails to capture hard negative instances. On the KuaiRec dataset, MA-ER yields an average test AUC of 0.8535, which is worse than uniform sampling (0.8553). To unravel how MA-ER and MA-EC affect model training, we randomly select a run from each method to visualize the model training metrics. In Figure 8, when using MA-ER, training AUC remains the same as testing AUC before convergence. Besides, the model converges earlier. In sharp contrast, in MA-EC, there is a huge gap between training AUC and testing AUC. The gap shows that training instances are overall harder than those in the test set. This verifies that MA-EC discovers hard negatives while MA-ER does not.

# RELATED WORKS

Negative sampling. Hard negative sampling is pervasively used in recommendation systems. PinSage [39] shows using curriculum learning with negative sampling is effective, implying hard negatives are helpful in the late stage of training. Metasearch offline datastream combines documents with in-batch mismatched queries with the highest similarity scores as hard negative samples [18]. Hard negative sampling is also justified in theory. Fithian and Hastie [9] uses a pilot model to select examples whose responses were rare given their features preferentially. Han et al. [14] explores local uncertainty sampling for multi-class classification. [34] proves that for generalized linear logistic regression models, the optimal negative sampling rate is proportional to the pilot prediction value. There are also approaches [5,38] that utilize item popularity to estimate the importance of negative instances.

Graph sparsification. Graph sparsification tries to drop nodes and edges while preserving the graph structure. Ghosh et al. [11], Spielman and Srivastava [30] studied edge sampling with effective resistance to preserve graph Laplacian. Satuluri et al. [26] used the Jaccard similarity score to measure node similarity and pick the top-K associated edges for each node by their similarity. Other methods include sampling edges by counting the number of its associate triangles [13], quadrangles [24], using local graph information [21], or using deep neural networks to coarsen the graph [2]. Graph sparsification has been explored to preserve or improve downstream task performance [33,41]. However, these method requires an endto-end training framework and thus cannot be used for continuous deployment where subsampling rates are static. To the best of our knowledge, model-agnostic methods based on graph sparsification are under-explored in the literature.

# CONCLUSION

We propose model-agnostic hard negative subsampling methods using the effective conductance on the user-item bipartite graph as the hardness score. We further exploit the graph structure by score propagation. Our model-agnostic complements model-based optimal sampling and provide a sustainable and consistent data subsampling solution to real-world recommendation systems with long-term impact. We discuss the cost upon deployment, its social impact, and future directions.

Deployment cost. Deploying a model-agnostic sampling service requires a database with graph computing engines that support effective conductance lookup given pairs of user-item ids, which is computationally cheap in practice. Online serving will not be affected, so there is no change in serving latency. Offline models are trained only on sub-sampled data to enjoy reduced computational costs. It takes 150 and 80 seconds to estimate the sampling rate for KuaiRec and MIND datasets, respectively. The cost of running MA-EC sampling is negligible compared to model training.

# Social impact.

With less data, one can train models with less GPU time and use less data storage. Given the quantity of data and the requirement to iterate the model periodically in the industry, the data subsampling method can significantly reduce the carbon footprint.

Future work. Our proposed sampling methods can be used to select better neighbors for learning graph embeddings. We can further improve MA-EC by (i) exploiting context information to identify hard negative samples. (ii) utilizing negative edges when calculating effective conductance. We leave those as future work.

# A IMPLEMENTATION DETAILS A.1 Dataset pre-processing

Here we demonstrate the data pre-processing of the two datasets. The KuaiRec dataset contains a sparse interaction matrix and a dense interaction matrix, where the dense interaction submatrix of the sparse matrix. The sparse matrix contains 7,176 users and 10,728 items, while the dense matrix contains 1,411 users and 3,327 items. As mentioned, the dense matrix is not collected under the natural recommendation setting, and shaving off the submatrix from the whole matrix is also unrealistic. Specifically, we create a submatrix by removing all the user columns from the sparse matrix if they appear in the dense matrix. The origin MIND-small dataset contains a training set and a validation set. In our setting, we first merge the two sets and re-split them into training, validation, and testing set. For both datasets, user-item pairs might appear multiple times in the dataset under a different context. When constructing the user-item bipartite graph, we treat them as one edge with a ACE measures whether the probabilities predicted by the classifier are calibrated [23], we can see that our model is well-calibrated even though the subsampled training set has a different population than the actual training set.

# B.2 Smoothness of propagated scores

For both datasets, we visualize the distributions of the corrected hardness scores for both MA-EC and Opt-Sampling methods. Specifically, we divide the instance scores into 50 bins and count the number of instances (both positives and negatives) for each bin. We generate the histograms and visualize them in Figure 10.

# A.2 Model specifications and hyperparameters

For pilot models, we adopt the default configuration in TorchFM 2 except for D&W. The training details of the pilot and the target models are shown in table 5. To compute effective conductance over the graph, we run random walk simulation until the update of commute time is smaller than 0.1. In edge propagation, the best results are reported with 𝛾 = 0.2 and 𝛾 = 0.4 for Opt-Sampling and MA-EC, respectively, in the KuaiRec dataset. And 𝛾 = 0.05 for both methods in the MIND dataset.

# A.3 Control experiment

We illustrate the control experiment in Figure 9. In each setting, one set of the scores is used as the major sampling scores, and only part of the instances will use the other ones. For example, when Opt-Sampling is used as major scores (red rectangle), instances whose scores lie in the upper left (blue rectangle) have inconsistent hardness over the two methods. And since MA-EC considers them hard negative samples, we "flip" the subsampling score of those instances from Opt-Sampling to MA-EC. 2 See https://github.com/rixwew/pytorch-fm

# Uniform

Opt-Samp. MA-EC ACE↓ 0.0070±0.0005 0.0073±0.0010 0.0071±0.0014 NDCG@5↑ 0.5209±0.0034 0.5342±0.0021 0.5390±0.0034 NDCG@10↑ 0.5223±0.0019 0.5375±0.0018 0.5403±0.0023 NDCG@30↑ 0.5221±0.0022 0.5364±0.0026 0.5397±0.0030

Table 6: Model performance on offline metrics

# A.4 Computing resources

For all the experiments, we train the models on NVIDIA A100 and NVIDIA V100 GPUs. For estimating the effective conductance on the graph, we utilize 16 CPU cores and 40 gigabytes of memory to run the simulations for both datasets. molecule generation tasks, the inference time of each model is measured on 1 TITAN RTX GPU and 20 CPU cores.

# B ADDITIONAL RESULTS B.1 Model performance on prediction tasks

We further investigate the performance gain of MA-EC in other offline metrics. Specifically, we consider Normalized Discounted Cumulative Gain (NDCG) scores and adaptive calibration error (ACE). We consider uniform sampling, Opt-Sampling, and MA-EC on the KuaiRec dataset in Table 6. We see that MA-EC and Opt-Sampling outperform uniform in all metrics by around 0.015 in terms of NDCG, illustrating the benefit of non-uniform sampling. As

