# Introduction

In many machine learning scenarios, a significant portion of the input features may be irrelevant to the output, especially with modern data management tools allowing easy construction of large-scale datasets by joining features from many different data sources. "Feature selection", or filtering the most relevant features for the downstream task, is an everlasting problem, with many methods proposed to date and used (Guyon & Elisseeff, 2003;Li et al., 2017;Dash & Liu, 1997).

Feature selection can bring a multitude of benefits. Smaller number of features can yield superior generalization and hence better test accuracy, by minimizing reliance on spurious patterns that do not hold consistently (Sagawa et al., 2020), and not wasting model capacity on less relevant features. In addition, reducing the number of input features can decrease the computational complexity and cost for deployed models, as the models need to learn from smaller dimensional input data, and hence require reduced infrastructure. Lastly, feature selection facilitates interpretability, as it sheds light on which features are most relevant for the downstream task.

Given the wide applicability of feature selection, how can one select the target number of features in an efficient, effective way? §2 summarizes numerous approaches. For superior task accuracy, one desired property is that the feature selection method should consider the predictive model itself, as the optimal set of features would depend on the mapping between the input data and output labels. Such end-to-end learning methods have been approached in different ways, such as via sparse regularization and its extensions (Lemhadri et al., and Perceiver (Jaegle et al., 2021), show strong results across many domains, with learnable key and query representations, whose alignment yields the masks that control the contribution of corresponding value representations. While these effectively reweigh the input, they typically do not completely mask out (i.e. yielding zero attention weight) any part of the input. Towards this end, various works have focused on bringing sparsity into masking, such as based on thresholding (Zhao et al., 2019) or sparse normalization (Correia et al., 2019). TabNet (Arik & Pfister, 2019) directly generates sparse attention masks and applies them sequentially to input data, which can perform sample-dependent feature selection. (Correia et al., 2020) achieves sparsity in latent distributions in neural networks, by using sparsemax and its structured analogs, allowing for efficient latent variable marginalization. (Lei et al., 2016) and (Bastings et al., 2019) learn Bernoulli variables, which are analogous to SLM's feature mask but in a local setting, for extractive rationale prediction in text. (Paranjape et al., 2020) extends these ideas by proposing to control sparsity by optimizing the Kullback-Leibler (KL) divergence between the mask distribution and a prior distribution with controllable sparsity levels. (Guerreiro & Martins, 2021) develops a flexible mask-based rationale extraction mechanism using a constrained structured prediction algorithm on factor graphs. All these perform sample-wise, not global, input selection. In this work, our goal is to explore global feature selection. When training and testing datasets perfectly align in distribution, local feature selection can give superior performance due to its input-dependence. However, there is rarely such perfect alignment, and global selection provides robustness benefits when there is distribution shift between training and test datasets, in addition to allowing more computational efficiency by globally removing features.

# Methods

Algorithm 1 describes SLM's end-to-end feature selection and task learning. The predictor f θ can be any gradient-descent based model, such as an MLP, with a task-specific loss function l such as the cross entropy for classification or mean absolute error (MAE) for regression. The following sections present SLM's key components in detail.

Notation. Throughout this work, we let X ∈ R n×d denote the input data, X sp ∈ R n×d the selected features, and m sp ∈ R d the learned sparse feature selection mask. We use to denote element-wise multiplication between each input sample and m sp : X sp = X m sp . We let F t denote the number of selected features at step t, and N the total training steps. Furthermore, I(X, Y ) denotes the mutual information between X and Y , and I q (X, Y ) is its quadratic relaxation. f θ denotes the task predictor used on the selected features.

Overview of SLM-based feature selection. As outlined in Algorithm 1, SLM first learns a non-sparse mask m ∈ R d , which is turned into a sparse vector by applying the sparsemax operator (Martins & Astudillo, 2016), described in §3.1. We present a novel application of sparsemax that provably achieves output sparsity at desired level exactly, for which we propose dynamically computing a scaling constant for the mask m, detailed in §3.2. SLM uses the resulting sparse mask to zero out non-selected features. The mask sparsity gradually increases throughout training to facilitate model convergence ( §3.3). Finally, a predictor model f θ on the selected features is trained using the dataset task loss and a novel mutual information (MI) loss, which is derived from first principles in §4. The following sections explain the important constitutents of SLM in detail.

## Mask sparsity via projection onto probability simplex

SLM selects features by learning a mask m sp ∈ R d , and zeroing out the features in the input X ∈ R n×d whose corresponding mask entries are zero. We use sparsemax normalization (Martins & Astudillo, 2016) to achieve sparsity in m. Sparsemax achieves sparsity in its output by returning the Euclidean projection of the input vector v ∈ R d onto the probability simplex ∆

We apply sparsemax to the mask argument m ∈ R d to obtain sparse feature mask:

(2) In particular m sp ∈ R d ≥0 . Compared to approaches like softmax normalization employed with thresholding, the probability simplex projection in sparsemax(v) scales the top values in v so they are more equidistributed over [0,1]. This equidistribution leads to greater feature weight separation, encouraging the model to discriminate amongst the features. Additional discussion on the properties of SLM sparsemax can be found in §A.5.

## Mask scaling to yield desired number of selected features

Following its formulation, sparsemax does not yield a predetermined number of non-zero elements, as the sparsity depends on the location on the probability simplex ∆ d-1 that v projects onto. For a non-uniform vector v ∈ R d , we can adjust its projection onto ∆ d-1 by multiplying v by a positive scalar. In particular, a sufficiently large scalar increases the sparsity, while a sufficiently small scalar decreases the sparsity. To illustrate this, we provide a simple example in Fig 1 . 
Example 3.1 (Adjusting sparsemax(v) sparsity by scaling). The probability simplex ∆ 1 in R 2 is the line connecting (0, 1) and (1, 0), with these two points as the simplex boundary. Let v = (x, y) be a point in R 2 , and (z, w) its projection onto ∆ 1 . We show that by varying multiplier m, sparsemax(mv) would have a varying degree of sparsity. The projection (z, w) = sparsemax((x, y)) is the unique point that satisfies (z, w) = argmin (z,w) ( y -w 2 + x -z 2 ), (z, w) element-wise positive, and z + w = 1. As we scale (x, y) with m, sparsemax(m(x, y)) = argmin (z,w) ( my -w 2 + mx -z 2 ). This projection distance expands to

Hence, d(0, 1) -d(0.5, 0.5) = mx -my + 0.5 (where (0.5, 0.5) is the midpoint of the simplex), which means that for any (x, y) and m with y > x, sparsemax(m(x, y)) is closer to (0, 1) ∈ ∆ 1 whenever m > 1/(2(y -x)), and closer to (0.5, 0.5) otherwise. Since projection is linear, this means varying the multiplier m varies the sparsity of sparsemax((x, y)). Figure 1 illustrates a concrete instance of scaling in the 2D case. This example conveys the intuition that larger multipliers lead to sparser outputs. More generally, one can show: The proof can be found in §A.3. Lemma 3.2 allows us to scale the mask to achieve the desired number of non-zero features. Note that since sparsemax has a particular Fenchel-Young loss (Blondel et al., 2020), scaling its argument by m is equivalent to scaling the regularizer by 1/m in the Fenchel-Young formulation (Blondel et al., 2020;Peters et al., 2019).

## Tempering feature sparsity to facilitate convergence

Starting training on only a randomly selected subset of features likely leads to suboptimal learning in the initial steps, and if feature selection converges before the predictor converges, the predictor would be trained with suboptimal features. To alleviate these and improve training stability, we propose gradually decreasing the number of features selected until reaching the target F N :

where F t is the number of selected features at step t, N tmp is the tempering threshold. In our experiments, we simply set N tmp = N/2 as it's observed to be a reasonable value across a wide range of datasets (as before N denotes the total number of training steps). To further stabilize training, instead of continuously decreasing the number of features, we decrease the number of features at five evenly spaced steps. This tempering allows the model to learn from more than the final target number of features during training -an advantage not shared by baseline methods. Furthermore, learning from all features initially likely provides a more robust initialization compared to starting learning with the target number of features, as the randomness in the initial selection is seldom optimal.

# Mutual information maximization

As an inductive bias to the model that accounts for sample labels during feature selection, we propose to maximize the mutual information (MI) between the distribution of the selected features and the distribution of the labels. Specifically, we condition the MI on the probability that a feature is selected, as given by the mask m. This stands in contrast to prior MI-based feature selection works such as (Fleuret, 2004;Bennasar et al., 2015), which yield binary decisions on whether to select a feature.

Let X denote the random variable representing the features, and Y the random variable representing the labels, with value spaces X ∈ X and Y ∈ Y. We let X and Y be discrete, following a long line of research on mutual information and entropy estimation that focuses on the case where the random variables live in the discrete space (Paninski, 2003;Kraskov et al., 2004;Valiant & Valiant, 2011;Han et al., 2015;Jiao et al., 2015;Wu & Yang, 2016), this is because 1) many variables in machine learning are indeed discrete, e.g. vocabulary index in NLP, categorical variables such as nationality, gender, etc, and 2) MI estimation in the continuous case can be reduced to the discrete case via binning and taking a limit (Paninski, 2003;Kraskov et al., 2004;Ross, 2004).

Feature selection methods based on maximizing either the conditional or the joint MI between selected features and labels require the computation of an exponential number of probabilities, the optimization of which is intractable (Fleuret, 2004). Therefore, we propose an end-to-end differentiable, quadratic relaxation for MI. When we model X and Y as random variables, their MI I(X, Y ) can be defined and reformulated as:

where the second step derives from marginalizing over X . Since the second term above does not depend on features X, it can be ignored during optimization.

## Quadratic relaxation

We propose a quadratic relaxation I q (X, Y ) of Eq 5 to simplify I(X, Y ) and its optimization, while retaining much of its properties:

Here, terms of the form p log q are relaxed to pq. Note that both p log q and pq are convex with respect to p and q, and hence have the same correlation behavior with respect to p and q. From an optimization perspective, I q (X, Y ) is a good approximation of I(X, Y ) where P X,Y (X, Y )/P X (x) and P Y (y) in Eq 6 lie in the neighborhood (1-δ, 1+δ). In this neighborhood, using Taylor expansion: log(q)= log(q 0 ) + (q-q 0 )/q 0 -(q-q 0 ) 2 /2q 2 0 + • • • When q 0 =1, this becomes log(q)≈(q-1)-(q-1) 2 /2= -3/2+2q-q 2 /2, hence, p log(q) has the second order approximation -3p/2+2pq (or -3p/2+2p 2 when p=q). Applying this to Eq 5, p is P X,Y (x, y) in the first term and P Y (y) in the second. Since both P X,Y (x, y) and P Y (y) are probabilities, and hence must sum to 1 across the label space for any given sample, the linear term -3p/2 does not affect gradient descent optimization. Normalization is a hard constraint enforced during training that supersedes this linear term in the objective. Therefore, during optimization, P X,Y (x, y) log(P X,Y (x, y)/P X (x)) and P X,Y (x, y) 2 /P X (x), and thus I q (X, Y ) and I(X, Y ), agree on their second order approximation. Note that the proposed relaxation is a variant of the commonly-used quadratic approximation based on Taylor's theorem (Shafer, 1974;Hsieh et al., 2011).

## Relating MI I

Next we connect I q (X, Y ) with the model's predictions using Lagrange multipliers. Let R(x, y) : X ×Y → [0, 1] denote the model's probability output for sample x and outcome y. Below, we model the discrete label case, e.g. for classification; the case where labels are continuous can be done by first discretizing the continuous label space (Fleuret, 2004), and then taking the limit as the discretization becomes infinitesimal. §A.4 contains further details. First, we define the quadratic error term E(X, Y ) in terms of R(x, y), and expand:

Theorem 4.1. Let X and Y denote the random variables representing the features and labels, respectively, and Y the value space for Y , then minimizing the optimum error E(X, Y ) in the model space {f : X → Y } is equivalent to maximizing the quadratic relaxation of mutual information I q (X, Y ). More specifically,

The proof utilizes Lagrange multipliers to solve for the optimal model predictions in terms of P X,Y (x, y) and P X (x), this can then be used to express the optimum objective E(X, Y ) as a function of I q (X, Y ). The full proof can be found in §A.4.

## Application to feature selection

Now, we apply this finding concretely to feature selection, by selecting a given number of features that minimize E(X, Y ). Given a dataset, let I denote the index set of the dataset samples, J the index set of the features, and L the set of possible labels. Let S ⊂ J denote the index set of features selected, X S i the random variable representing a selected subset of features for the i th sample, and Y i the random variable representing the label for the i th sample. Then, the joint probability can be written as

During training, Eq. 8 is minimized under the following consistency constraint: for two samples i 1 and i 2 that have the same values in the selected features, i.e. X S i1 = X S i2 , their model predictions must be the same

To encourage the model to satisfy this constraint, we turn it into a soft consistency regularization term r cs , converting constrained optimization to unconstrained optimization with regularization:

where P (X S i1 = X S i2 ) is the probability that the samples X i1 and X i2 take the same values in the selected feature set S.

Let the learned mask consists of probabilities m = {p j } j∈J , i.e. p j is the probability that feature j is selected, then

(1 -p j ), i.e. P (X S i1 = X S i2 ) is the product over probabilities that feature j is not selected, if X i1 and X i2 differ at feature j. (The difference in a feature that is not selected does not contribute to P (X S i1 = X S i2 )). In this probabilistic form, the consistency regularizer also encourages the selection of features with diverse ranges, since it encourages high p j for the features with many X

pairs. Therefore, the regularized objective to maximize the MI I(X, Y ) between the selected features and the labels becomes:

where

In practice, r cs can be enforced batch-wise, and can be efficiently vectorized for the parallel computation of all X (j)

i2 pairs per batch using tensor operations. Note that since R(X S i , Y i ) are just model predictions, and p j are learned feature mask probabilities, each component in E(X, Y ) is easily accessible. When the labels are in the continuous space, the minimization objective with the consistency regularizer is derived the exact the same way to yield:

Our analysis is done with random variables X and Y to apply tools from probability theory. The data samples X and labels Y can be thought of as samples drawn from the distributions to which X and Y belong, where in the limit with infinitely many samples X and Y perfectly reflect these distributions.

## SLM Computational complexity

As above, let h be the hidden dimension, n denote the number of samples, b the batch size, and N the total number of train steps; let F 0 be the total number of features, and F N the target number of features.

We first discuss the complexity of individual components. The sparsemax operation is dominated by sorting, and hence has complexity O(F 0 log F 0 ) per sample, with an overall complexity of O(nF 0 log F 0 ). The consistency regularizer r cs in the MI-maximizing objective E(X, Y ) has complexity O(nbF N ), as the calculation X (j)

2 in Eq 10 occurs over the selected feature index set j ∈ S, and is done between each sample and others in its batch. The non-regularizer component in E(X, Y ) has complexity nc, where c is the constant for the number of discrete or binned labels. Assuming an MLP classifier with h hidden units, which has complexity O(nh 2 ), the overall algorithm has complexity O(nF 0 log F 0 + nbF N + nc + nh 2 ), making SLM amenable to scaling to a large number of features. In addition, SLM amortizes the cost of feature selection across batches throughout training, making it more scalable with respect to the number of samples. This is in contrast to PFA (Lu et al., 2007a) or many other MI-based methods such as CMIM (Fleuret, 2004) or JMIM (Bennasar et al., 2015), which place the memory and compute burden of selection for the entire dataset in the same step.

# Experiments

## Datasets and Settings

We present the efficacy of SLM in feature selection on wide range of datasets from numerous domains. For all experiments, we ensure fair comparison by employing similar hyperparameter search space and budgetto search for hyperparameters such as batch size and learning rate for each baseline method and dataset, we conduct an extensive random search within the search grid, by randomly generating a value within a conceivable range. We run a total of 300 trials for each method-dataset combination to ensure sufficient coverage, and tune all hyperparameters based on the validation accuracy. This process is chosen as it closely resembles model benchmarking and selection in real-world applications. The Appendix includes a myriad of additional experiments: selected feature interpretability ( §A.6), compute timings ( §A.7) and synthetic data experiments ( §A.9) to demonstrate SLM's scalability, using the Hilbert-Schmidt Independence Criterion (HSIC) in lieu of the MI regularizer to demonstrate the effectiveness of the learned sparse mask ( §A.8), as well as comparisons with further end-to-end baselines ( §A.10).

We benchmark on a variety of real-world datasets across many domains, including computer vision, biological data, financial data, etc. Concretely, we benchmark on Mice, MNIST, Fashion-MNIST, Isolet, Coil-20, Activity, Ames Housing, and IEEE-CIS Fraud datasets. We use a 70-10-20 train/validation/test split; and when available, we use the exact same train/validation/test samples as (Lemhadri et al., 2019) for fair comparison. We give further detailed descriptions in §A.1. Cross entropy is used as the optimization objective for classification tasks, and MAE is used as the optimization objective for regression.

We benchmark SLM against a variety of competitive methods. The mutual information (MI) based feature selection baseline uses entropy estimation from k-nearest neighbors distances as described in (Kraskov et al., 2004;Ross, 2014) to estimate MI. Tree-based methods yield Gini importance scores, which can be used for feature selection. For this we benchmark two commonly used methods: random forest (RF) (Breiman, 2001), an ensemble of independent trees, and XGBoost (Chen & Guestrin, 2016), a scalable end-to-end tree boosting system. We furthermore benchmark against methods as discussed in §2: LassoNet (Lemhadri et al., 2019), which uses residual connections to allow the network to learn whether to use any given feature in a particular layer; feature importance ranking based on the Fischer score (Gu et al., 2012); principal feature analysis (PFA) (Lu et al., 2007a), a PCA-based method; and HSIC-Lasso (Yamada et al., 2014), which uses kernel learning to find non-linear feature interactions. Lastly, we benchmark against linear regression, where feature importance is determined by the learned feature coefficients. When available, we use results from (Lemhadri et al., 2019). For consistency and fairness, each baseline method uses the same input as SLM to select features, which are then passed to an MLP to compute the task metric.  et al., 2017;Zintgraf et al., 2017;Chang et al., 2019). We consider feature importance to be measured by contribution towards the task metric, as accurate predictor performance is typically the end goal, and the importance of each individual feature is not always well-defined due to feature interactions. Therefore, we focus on benchmarking task predictive accuracy given the selected features as the metric.

# Method

First, we study selecting a fixed number of features across a wide range of high dimensional datasets (most with >400 features) and feature selection methods. We consistently choose 50 selected features, as this represents a small fraction of the total features for most datasets, as often done in practice. This number is kept consistent without tuning for any given method, to avoid favoring any given one. Table 1 shows that the SLM consistently yields competitive performance, outperforming all methods in all cases except on Mice and Ames, for which the performance is saturated due to small numbers of original features, making feature selection less relevant. Most feature selection methods are not consistent in their performance. On the other hand, SLM's strong performance is consistent -across a wide range of datasets, SLM selects the features accurately. Interestingly, we observe that there are cases where SLM even outperforms the baseline of using all features, which can likely be attributed to superior generalization when the limited model capacity is focused on the most salient features. Especially for datasets that are non i.i.d. in nature, feature selection can be a strong inductive bias integrated in the architecture, that can yield superior generalization. Next, we conduct further experiments on the Fraud Detection dataset (Kaggle, 2022), a large-scale dataset with many heterogeneous features. It is highly non i.i.d. (Grover et al., 2022), thus making feature selection important given that high capacity models can be prone to overfitting and poor generalization. Table 2 shows that SLM outperforms other methods consistently for different number of selected features, and its performance degradation with respect to reducing the number of features is much smaller. Indeed, the AUC with 20 features out of 432, is >10% better than using all features, indicating improved generalization.

# Method

## Ablation studies

Figure 2: (1) and ( 2) show ablation studies on the effect of MI regularization and tempering the number of features. Both ablation studies have the same number (50) of selected features on all datasets. (3) shows the task accuracy as a function of the number of features selected on the activity dataset. The dark line shows the average of ten random hyperparameter trials, shown with light hue, demonstrating that task performance can be near-optimal even with a small subset of features.

We study the utility of SLM components, particularly the effects of the MI regularizer and tempering the number of features, which gradually decreases the number of selected features from the full feature set to the target number. The effects are measured by randomly selecting ten hyperparameter settings and a seed, and recording the average performance with or without either MI regularizer or tempering (without tempering refers to keeping the number of selected features constant throughout training.). Fig 2 shows that both MI regularization and tempering positively affect task performance. This is consistent with the theory developed in §3: the MI regularizer encourages maximal mutual information sharing between the labels and the selected features; and tempering allows the model to initialize learning based on all features, rather than a randomly selected subset.

# Discussion

Feature importance interpretability. SLM learns a sparse mask M that contains the feature selection coefficients. We show that this approach yields superior results with end-to-end learning by allowing a smooth transition between selecting and un-selecting features. In addition, SLM can also be used for interpretation of global feature importance during inference, yielding the importance ranking of selected features, similar to other commonly-used methods like SHAP (Lundberg & Lee, 2017). This can be highly desired in high-stakes applications such as healthcare or finance, where an importance score can be more useful than simply whether a feature is selected or not.

Feature interdependence during selection. Compared to prior MI-based feature selectors (Ding & Peng, 2005;Fleuret, 2004;Bennasar et al., 2015), SLM accounts for feature inter-dependence by learning inter-dependent probabilities {p j } j for the selected feature, where {p j } j jointly maximize the MI between features and labels. Furthermore, SLM learns feature selection and the task objective in an end-to-end way, which alleviates the selection of repetitive features that may individually be predictive, as gradient descent favors increasing the probability for a non-redundant and loss decreasing but less predictive feature over an individually predictive but redundant feature.

Improved model generalization via feature selection. Feature selection can help improve generalization beyond the training set, especially for high capacity models like deep neural networks, which can easily overfit patterns from spurious features that do not hold across training and test data splits (Arjovsky et al., 2019). For instance, Table 1 shows that on some datasets, especially with SLM, prediction on a subset of features can outperform that on all features. Furthermore, Fig 2 shows that task performance can reach near-optimum with even a small subset of all features. Therefore, feature selection is a potential alternative for alleviating compute cost during training and inference, without sacrificing on accuracy.

# Relation to other MI estimations in deep learning. MI-based objectives have been used in other deep

learning methods, such as InfoNCE (Oord et al., 2018), InfoGAN (Chen et al., 2016), and Deep Graph Infomax (Velickovic et al., 2019). To estimate MI, these typically train classifiers on samples drawn from the joint distribution and the product of the marginals, whose exact distributions can be intractable. In contrast, for feature selection, while the exact distributions of the features and the labels are known, the computation of their mutual information and its maximization is computationally intractable. To address this, SLM proposes a quadratic relaxation of MI optimization, applied to feature selection by converting MI maximization to minimizing a loss function. SLM does not need to sample from the joint or marginal distributions, a potentially computationally intensive process. Furthermore, prior works (Chen et al., 2016;Velickovic et al., 2019) often require a contrastive term in estimation of MI with negative sampling, a process that is not needed in SLM.

# Future work.

SLM can be integrated into unsupervised or semi-supervised learning, with modified objectives. In addition, our results indicate more significant outperformance for datasets with non i.i.d. characteristics as feature selection can effectively reduce the feature dimensionality and reduce the risk of overfitting to the spurious correlations of irrelevant features. Lastly, feature selection for data with structure (e.g. temporal or graph) is an interesting extension, which might be based on modifying SLM to apply masking to entire time-series or graph data.

# Conclusion

We introduce SLM, a sparse learnable mask based feature selection framework that maximizes the MI between features and labels, while optimizing the training objective end-to-end. Learning the feature masks allows a smooth, probabilistic selection of features as well as insights on feature importance. SLM demonstrates competitive performance against SOTA baselines, and opens door to future applications in domains such as graph or time series representation learning.

# A.1 Dataset Details

This section provides additional details on the experimental data. We first consider the real-world benchmark datasets in (Lemhadri et al., 2019). Mice consists of protein expression levels measured in the cortex of normal and trisomic mice who had been exposed to different experimental conditions. Each feature is the expression level of one protein. MNIST and Fashion-MNIST consist of 28-by-28 grayscale images of hand-written digits and clothing items, respectively. The images are converted to tabular data by treating each pixel as a separate feature. Isolet consists of preprocessed speech data of people speaking the names of the letters in the English alphabet with each feature being one of the preprocessed quantities, including spectral coefficients and sonorant features. Coil-20 consists of centered gray-scale images of 20 objects taken at certain pose intervals, hence the features are image pixels. Activity consists of sensor data collected from a smartphone mounted on subjects while they performed several activities such as walking or standing. For these datasets, we use the exact same data splits and preprocessing approaches with (Lemhadri et al., 2019) for fair comparison, as well as the same model hyperparameter search space.1 In addition, we consider the Ames housing dataset (Cock, 2011), with the goal of predicting residential housing prices based on each home's features; as well as the IEEE-CIS Fraud Detection dataset (Kaggle, 2022), with the goal of identifying fraudulent transactions from numerous transaction and identity dependent features. 

# A.2 Experimental details

As described, we use hyperparameter tuning based on the validation accuracy for all cases. We use the Adam optimizer for training, with exponential decay. For benchmarks from (Lemhadri et al., 2019), for a fair comparison, our hyperparameter search space is same as the original paper. For Fraud, which is larger and more complex, we extend the search space as in Table 4. For baselines such as LassoNet, we tune additional method-specific hyperparameters. For instance, for LassoNet, in addition to the hyperparameters, we also tune the 2 penalization on the skip connection, the hierarchy parameter, and the dropout rate. For XGBoost, we also tune the number of estimators and the maximum tree depth.

# Hyperparameter

A.3 Proof of Lemma 3.2 Lemma 3.2. Given a nonuniform vector v ∈ R K , to obtain F nonzero elements in sparsemax(v), v should be multiplied with the scalar

where v (1) ≥ v (2) . . . ≥ v (K) denote sorted elements of v in descending order.

Proof. We first show the case when |sparsemax(v) > 0| > F , i.e. the sparsity needs to be increased (the case where sparsity needs to be decreased works analogously). By (Martins & Astudillo, 2016), the projection of v onto ∆ K-1 in Eq 1 takes the form sparsemax(v) = [v -τ (v)] + , where [x] + = max{0, x}, and τ takes the

with k(v) defined as the index

Hence, increasing the sparsity such that sparsemax outputs only F nonzero elements, i.e. decreasing the index k(v) to F , requires finding the smallest m such that 1 + (F + 1)mv (F +1) > i≤(F +1) mv (i) does not hold, i.e. F + 1 must be the first k to fail the condition 1 + kv (k) > i≤k v (i) . Rewriting this condition in terms of F we obtain:

The smallest m such that condition Eq. 13 does not hold is m =

, which given Eq 12 implies mv has F nonzero elements. Analogously, to derive the multiplier for v to decrease sparsemax(v) sparsity, we need to increase the index k(v) to F . This requires finding the largest m such that 1 + F (mv F ) > i≤F mv (i) holds, which implies:

# A.4 Proof of Theorem 4.1

Theorem 4.1. Let X and Y denote the random variables representing the features and labels, respectively, and Y the value space for Y , then minimizing the optimum error E(X, Y ) in the model space {f : X → Y } is equivalent to maximizing the quadratic relaxation of mutual information I q (X, Y ). More specifically, min

During training, the model seeks to produce the optimal predictions R(x, y) that minimize E(X, Y ), while satisfying the constraint y∈Y R(x, y) = 1. Hence we can apply Lagrange multipliers to solve for the optimal R(x, y). Taking the derivatives of E(X, Y ) and the constraint g(X, Y ) = x∈X ,y∈Y R(x, y) -|X | with respect to R(x, y):

By Lagrange multiplier theory, for an optimum set of model predictions R * (X, Y ), there exists some λ such that

Therefore, by Eq 14, R * (x, y) = P X,Y (x, y)/P X (x). Plugging this into Eq 7, we obtain an expression relating the mutual information I q (X, Y ) and the optimum error E(X, Y ):

Since P Y (y) is fixed for a given dataset, minimizing E(X, Y ) across the model space is equivalent to maximizing I q (X, Y ).

# Continuous label space.

For the case with continuous labels (as occur for regression problems), the quadratic relaxation analogue of Eq 6 becomes:

Ĩq (X, Y ) :=

Let Y k be a discretization of the continuous labeling space Y with k intervals, i.e. we are turning the continuous labeling function X → Y into a piecewise constant one with k steps. Then, discretizing followed by taking the limit as k → ∞ (and all bin sizes tend to 0) yields, analogous to Eq 7:

Therefore following the same logic as in the proof above:

Plugging Eq 15 into this equation thus gives:

as desired. Thus, minimizing the optimum objective Ẽ(X, Y ) across the model space {f : X → Y } is equivalent to maximizing I q (X, Y ).

# A.5 Properties of sparsemax for SLM

This section further details the key aspects of utilizing sparsemax for SLM, in terms of how it compares with softmax with thresholding for feature selection, as well as how SLM avoids the sparsemax support collapse problem.

# A.5.1 Sparsemax vs softmax with thresholding

Softmax is the commonly used nonlinear normalization function. An alternative method for learning the sparse mask M sp would be to apply softmax normalization, followed by a top-k operation, and an additional normalization to render it a probability mask. This method is not only unwieldy with additional steps, but because the softmax-top-k normalization normalizes with respect to the absolute value of v, whereas sparsemax normalizes with respect to its relative values (by subtracting a v-dependent threshold), sparsemax(v) is more equi-distributed over the interval [0, 1] than softmax-top-k normalization (i.e. sparsemax(v) has lower entropy than softmax-top-k normalization), making it more discriminatory for feature selection. Furthermore, one gradient computation advantage of sparsemax(v) is that it allows a faster computation of the Jacobian-vector product -which typically suffices for backpropagation -in O(S(v)) time, S(v) being the support of v (Martins & Astudillo, 2016), compared with linear time (with respect to the size of v) for softmax.

# A.5.2 SLM avoids sparsemax support collapse

In practice, since the gradient of sparsemax is zero for elements outside its support (Martins & Astudillo, 2016), an element that initially falls outside its support would stay so throughout training. This would lead to sparsemax support collapse, i.e. the size of the support dwindles during training.

SLM avoids the sparsemax support collapse problem, due to its sparsemax argument scaling (Lemma 3.2).

In vanilla sparsemax, as the support of sparsemax is determined by the distances between the top-ranking elements, having non-zero gradients only for the elements in the support of sparsemax causes only those elements to drift. As the inputs to sparsemax can vary without bound, this drift becomes larger over time, i.e. the distance between the top elements, which are in sparsemax's support, becomes larger, making the sparsemax support smaller, and blocking new elements from entering the support. However, when the input to sparsemax is scaled as in Lemma 3.2, this drift is controlled, and can shorten the distances (in addition to lengthening them) between the top elements, hence the sparsemax support can acquire new elements, avoiding the collapse.

# A.5.3 Experimental analysis of the number of features in support

Experimentally, when training SLM feature selection with a single-layer MLP architecture, on a dataset of 1000 samples with 100 features each, using sparsemax with scaling to select 30 features consistently yields 30 features in the sparsemax support. In contrast, without scaling, the sparsemax support consistently dwindles to well below 10 features within 15 epochs.

# A.6 Feature Interpretability Results

While SLM optimizes feature selection for the task metric, the fact that the selected features are global readily opens the door for feature importance interpretability applications, as the chosen features can give insights about the task. To this end, we focus on the Ames housing dataset (Cock, 2011), as its features are easily understandable. As mentioned in §A.1, the features in the Ames dataset consist of characteristics of houses, and the prediction target is the house price. We use the model parameters found in the best validation trial reported in Table 1, and select the top ten out of the 81 features. To obtain importance scores of the selected features, we study the selection probabilities learned in the feature mask. Using this, the ten highest-probability features in terms of determining a house's prices are, with learned feature probabilities: 'OverallQual' (0.211), 'FullBath' (0.182), 'GarageCars' (0.124), 'BsmtFullBath' (0.0795), 'MSSubClass' (0.0758), 'GarageFinish' (0.0739), 'HalfBath' (0.0718), 'PoolArea' (0.0562), 'Fireplaces' (0.0473), 'HouseStyle' (0.0403).

Some aspects of this selection conform to common sense -the overall quality of the property, the number of bathrooms, and the size of the garage or pool are good predictors of housing value. Other aspects are more surprising, for instance the feature 'BedroomAbvGr' -the number of bedrooms above ground -is not selected, even though one would expect the number of bedrooms to be an important selling factor. However, on further thought, as the number of bedrooms is positively correlated with the number of bathrooms (Eggers & Moumen, 2013), SLM is avoiding feature redundancy by only selecting one of the correlated features. The same reasoning applies for the features 'OverallQual', the overall quality, which is selected, and 'OverallCond', the overall condition, which is not selected.

# A.7 Computational Complexity Experiments

As stated in § 4.4, let F 0 be the total number of features, and n the number of samples, SLM has O(nF 0 log F 0 ) dependence on F 0 . To test that this low complexity in theory translates to actual fast feature selection in practice, we present the wall clock timing of SLM. We compare specifically against LassoNet, a strong baseline that also selects features end-to-end. Furthermore, we discuss the computation of the MI objective in Eq 9. In particular, the consistency term r cs in Eq 10, which ensures that if two samples have the same values in their selected features, their model predictions are the same as well. In theory, if we imagine giving r cs a weight coefficient α in Eq. 9, with the interpretation that in the limit where α → ∞, this consistency is strictly enforced; and in the limit where α → 0, not at all. In practice, given that they have the same orders on terms such as model predictions R(X, Y ) by design, r cs and the remaining term in Eq 9 have the same order of magnitude. Furthermore, r cs indeed is the most compute-intensive part in Eq 9, as r cs requires pairwise comparisons within the batch (for each pair X i1 , X i2 it is computed over the feature indices j where X

). Experimentally, on the Ames dataset with a batch size of 128, the r cs computation takes up 1.51 ± 0.012 ms, out of 1.94 ± 0.017 ms for the entire MI regularizer computation in Eq 9. This reveals an interesting accuracy-compute trade-off, where users may want to skip the r cs computation for an even faster, approximate MI regularizer computation.

# A.8 HSIC objective to demonstrate the effectiveness of the learned sparse mask

While the mutual information regularizer is an integral part of the SLM, in this section we show the effectiveness and generalizability of the learned feature selection mask approach, by replacing the MI regularizer with another measure of dependency between random variables: the Hilbert-Schmidt Independence Criterion (HSIC) (Gretton et al., 2005). Analogous to how we apply the mutual information regularizer, we consider the HSIC between the features random variable and the labels random variable distributions.

Concretely, for two random variables X and Y , the HSIC is the Hilbert-Schmidt norm of the covariance operator between these random variable distributions in the Reproducing Kernel Hilbert Space, defined as:

where k X and k Y denote kernel functions; F and G are the Hilbert spaces of functions on X and Y ; and Cov(X, Y ) denotes the cross-covariance operator F → G (Gretton et al., 2005). We experimented with different kernel functions for Eq. 16, and chose the Gaussian kernel based on final task performance: k(x, x ) := exp(-||x -x || 2 /(2σ 2 )), where x, x are samples drawn from the distribution P X , with σ being the standard deviation.

Unlike mutual information, HSIC is not a probabilistic measure, and does not have an interpretation in terms of information theoretic quantities (bits or nats) (Ma et al., 2020). On the other hand, HSIC does not require any probability density estimation, which can be a computational bottleneck in approximating mutual information. In our experiments, we compute the HSIC objective batch-wise between the features and the labels, conditioned on the learned feature selection mask. This conditioning is done by scaling the standard-normalized input features by the learned feature selection mask, before the mask is sparsified via sparsemax. Table 6 shows the results of our HSIC experiments. Overall, we observe the version of SLM with HSIC to be worse than the original version, but it does improve over the other baselines (and most notably, significantly better than HSIC-Lasso, a commonly-used feature selection method that integrates the HSIC objective as well). The hyperparameter tuning based on the validation set is performed similarly to the main experiments in §5.2. SLM learned feature mask combined with the HSIC objective perform very competitively compared to the myriad of strong baselines, demonstrating the effectiveness and generalizability of SLM's learn feature selection mask approach.

# A.9 Synthetic Data Experiments

We demonstrate the performance of SLM on a synthetic dataset that is specifically constructed such that only a small subset of features affect the output value while the vast majority are not useful for the task. All input features X i,j are sampled from the uniform distribution U [-1, 1] and the noise at the end i,j are sampled from standard Gaussian random variable with zero mean and unit variance. The input-output relationship are governed by the equations shown below:

exp(X i,j ), ( 17)

# T

(5)

deep neural network regularized with the reconstruction loss, with a focus on biological data, which are often high-dimensional with limited sample size. STG (Yamada et al., 2020) develops a fully embedded supervised method that learns stochastic gates with a probabilistic relaxation of the count of the number of selected features. While all these works selects features and learns task prediction end-to-end, given that SLM is a supervised model, with a general focus beyond the high-dimensionality and low-sample-size setting, STG (Yamada et al., 2020) is the strongest, most related baseline to compare SLM with. Table 10 shows the comparison between SLM and STG on the Isolet and Activity datasets with 50 selected features. There are certain similarities between how SLM and STG control which feature to select: SLM learns a sparse probability mask m for the features, whereas STG learns learn the parameters of the approximate Bernoulli distributions via gradient descent for each feature. While STG learns the parameters for each Bernoulli variable independently, one advantage SLM has is accounting for interdependence amongst selected features, through both the fact that the probabilities in m are interdependent, and through the MI regularizer (further details discussed in §6). The two methods are compared under the exact same conditions to the largest extent possible: using the same hidden dimension, number of epochs, batch size, learning rate, etc., all randomly generated from within a feasible range. The non-shared hyperparameters are also generated from random within a feasible range. The results are averaged over ten different runs. SLM is able to account for interdependence amongst selected features, through the learned mask m and the MI regularizer.

# Acknowledgment

We'd like to thank Tomas Pfister, Nate Yoder, and Jinsung Yoon for insightful discussions on this work.

# A.10 Further Comparison with End-to-end Baselines

One of SLM's strengths is end-to-end feature selection along with task learning, which allows the model to incorporate inductive biases from the task directly into feature selection. Therefore, we specifically focus on comparing SLM with additional end-to-end feature selection methods, beyond the results in Table 1. As discussed in §2, Concrete Autoencoder (Abid et al., 2019) proposes an unsupervised feature selector based on using a concrete selector layer as the encoder and using a deep neural network as the decoder. FsNet (Singh et al., 2020) uses a concrete random variable for discrete feature selection in a selector layer and a supervised

