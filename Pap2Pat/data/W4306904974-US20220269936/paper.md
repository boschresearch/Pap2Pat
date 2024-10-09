# INTRODUCTION

Time series analysis is a problem central to finance and statistics [44]. In this paper, we consider the problem of modeling and forecasting in multivariate time-series panel data {𝒚 𝑡 } 𝑡 ∈ [𝑇 ] where, 𝒚 𝑡 ∈ R 𝑁 is a vector of panel measurements at time 𝑡 ∈ [𝑇 ] := {1, . . . ,𝑇 }. Our study is motivated by challenging financial timeseries forecasting problems (e.g., volatility, volume forecasting) characterised by relatively large panel-sizes, limited sample sizes than the number of nodes 𝑁 . We differ in that we use these models in the context of a joint mean and covariance learning framework and perform this joint learning in very limited sample regimes in the context of financial applications. We model the unexplained residuals 𝝐 𝑡 = 𝒚 𝑡 -𝒇 𝑡 via a multivariate Gaussian graphical model [25]. We model the precision matrix [31] or partial correlations of the errors to be sparse-the sparsity structure is partially (not fully) informed by KGs. Our framework GregNets extends the framework of [5] in multiple ways: we propose faster algorithms (100×-250×) for joint training, incorporate flexible GCN models for the panel component, and use KGs to inform the partial correlation matrices.

Joint training. Jointly training the conditional mean function and error correlation structure leads to algorithmic challenges. When 𝒇 𝑡 is a sparse linear model (e.g., sparse VAR), we present a joint proximal gradient descent algorithm [7,39] to simultaneously learn 𝒇 𝑡 and a sparse partial correlation matrix for 𝝐 𝑡 via a pseudolikeihood approach that results in improvements over the recently proposed algorithm of [5]. When 𝒇 𝑡 corresponds to a GCN or other generic temporal (graph) neural networks, we embed the partial correlation learning into our proposed pseudo-likelihood layer, append it to the temporal graph neural network layers, and train the time-series parameters as well as the partial correlation simultaneously via backpropagation with (adaptive) stochastic gradient descent.

Contributions. The key contributions can be summarized as follows: (1) we propose a joint modeling and training framework GregNets2 to learn the conditional mean function for the panels and the error correlation structure for the innovations -both of these incorporate KGs as structured priors. (2) Joint training leads to computational challenges. We address this by developing a pseudolikelihood layer that incorporates the KG information and can be easily appended to any existing multivariate time-series forecasting architecture trainable with (stochastic) gradient descent. (3) We demonstrate the usefulness of GregNets for S&P500/S&P1500 stock volatilities time-series analysis for improved prediction, reduced model complexity, faster optimization and better interpretability.

# RELATED WORK

There is an impressive literature on financial time-series modeling; we discuss work that is most closely related to the main topic of the paper. Recall that our goal is to simultaneously learn a model for 𝒇 𝑡 and a partial correlation structure for the error 𝝐 𝑡 within a joint training framework, using information from KG, in the context of financial time-series forecasting. Next we discuss related work pertaining to the individual components of our general model.

The partial correlation learning sub-problem is related to the rich literature on high-dimensional Gaussian graphical models [25,31], and central to the portfolio optimization in finance [36]. Given a data matrix, common approaches to learn a corresponding ℓ 1sparse precision matrix are the graphical lasso [21], row-by-row estimation methods [38], the pseudo-likelihood framework [8,42]. Recently, [3,45] propose the MTP 2 method to learn a precision matrix with nonpositive entries. For other methods on covariance matrix estimation, see [18] for a nice overview. The above methods focus on learning correlation matrices; and assume that the timeseries panel component 𝒇 𝑡 ≡ 0.

VAR is a popular linear modeling tool for modeling the dynamics of panel time series data, with wide applications in various domains [28,44]. However, the number of parameters in VAR grows quadratically with the number of time series components, hence regularization is called for. Common methods to reduce the complexity of VAR models include ℓ 1 -regularization [24], canonical correlation analysis, factor models [9], among others-see [40] for further discussions. Apart from VAR-based models, there are some other traditional statistical time series models in financial econometrics [4,19,43]. All of these models learn 𝒇 𝑡 ; but they do not directly learn the correlation structure of the residuals.

There is a large body of recent literature on GCNs. The fundamental GCN idea was formulated by [30] and originally studied for author citation networks [2,30]. The idea has been extended to time-series modelling by combining graph convolution operation with recurrent/1D convolution architectures to capture dynamics in [34,35,46,48]. These networks have been primarily explored in the context of traffic forecasting datasets where the number of samples is very large compared to number of nodes. Some recent financial literature uses variation of these modelling ideas in the context of stock prediction [20,37]; see also [29] for a nice review of different applications of deep learning for stock market prediction.

Our work is most related to [5] who consider joint learning of an ℓ 1 -sparse VAR model in addition to a sparse partial correlation matrix of residuals 𝝐 𝑡 . However, our work differs in that (i) we use KG information to aid learning of the partial correlation matrix and/or a NN-based model for 𝒇 𝑡 , (ii) we allow for a GNN model for 𝒇 𝑡 while [5] considers VAR models, (iii) our proposed algorithm for joint training is more general; and when specialized to the specific task considered in [5], our proposed algorithms are much faster.

Our proposals are evaluated on knowledge graphs, some of which are close in spirit to those used in financial econometrics literature. Existing modelling approaches with financial KGs have explored different forms of connectivity information such as industrysector classification [20] and first and second order relationships from text data [11,20,37]. We explore a new KG, proposed in [33], constructed on the basis of aggregated co-search of financial information by analysts, which is described in more detail in section 5.1. We also consider KG created using one type of financial indicator (e.g. returns) to improve prediction/correlation structure estimation for another financial indicator (e.g. volatilities).

# GREGNETS: STATISTICAL FRAMEWORK

We present the general modeling framework for GregNets.

Model. Given multivariate time-series data {𝒚 𝑡 } 𝑇 1 , we consider the following model

where, the conditional mean function 𝒇 𝑡 = E(𝒚 𝑡 |F 𝑡 -1 ) is given by 𝒇 ({𝒚 𝑡 } 𝑡 -𝑝 𝑡 -1 ) ∈ R 𝑁 which depends upon 𝒚 𝑡 for the past 𝑝 timepoints; and the error vectors {𝝐 𝑡 } 𝑇 1 are independent and assumed to follow a multivariate Gaussian distribution with stationary covariance matrix 𝚺 = 𝑪 -1 ∈ R 𝑁 ×𝑁 , where 𝑪 denotes the precision matrix. Both 𝒇 (•) and 𝑪 are unknown and need to be estimated from the data under suitable structural constraints. In addition to the data {𝒚 𝑡 }, we will also be using KGs to inform the estimation of 𝒇 and 𝑪, as discussed below.

Illustration. We present some examples of the different components of (1) that can be addressed by GregNets. The conditional mean function 𝒇 can be taken to be a linear model (e.g. VAR) or some nonlinear NN-based models (e.g. LSTMs, GCNs). We will also use KGs to incorporate prior information into some of these models. At the same time, we learn the precision matrix 𝑪 through the partial correlation 𝝆 under a pseudo-likelihood framework (See Section 4.2). This can avoid lack of scalability issues arising from the likelihood method and is more amenable to joint training with the deep learning APIs (e.g. Tensorflow [1]). Further details are presented in Section 4.

As an illustration, we can consider the target variable 𝒚 𝑡 to be stock returns, stock volatilities, trading volume or bond yields of 𝑁 different companies over a certain time horizon 3 .

# KG based regularization.

A key challenge in learning model (1) lies in suitably constraining the number of parameters associated with 𝒇 and 𝑪, within our joint learning framework. Figure 1 shows a schematic picture of using KG within our joint learning framework. Specifically, given a knowledge graph 𝑮, we extract a sparse connectivity information matrix E from 𝑮 (Section 4.3.1), and create masking matrices based on E and 𝑮 (Section 4.3.2). The masking matrices will be used in some regularizer Ω 𝝆 , which further guides the learning of 𝝆. In Section 4.3.3, we also discuss how to extend this to using multiple KGs. At the same time, the KG can also be used as an input for some graph neural network architectures to guide the learning of the time series part 𝒇 . In the next section, we will provide details of the components of GregNets and show the details of using the KG information. 

# LEARNING THE MODEL COMPONENTS

A principal challenge in learning model (1) lies in its joint training. Here, we discuss the details of the individual components: the mean function 𝒇 (Section 4.1), the long-term residual correlation structure 𝑪 (Section 4.2), KG-based prior regularization (Section 4.3). The joint training algorithm is discussed in Section 4.4.2.

## Learning the conditional mean function 𝒇

We discuss two major classes of the conditional mean function 𝒇 : the sparse VAR model; and the NN models (e.g. LSTMs, GCNs).

# Sparse Vector Autoregression (VAR).

Vector autoregression models the function as a linear combination of all the time series at different lags upto 𝑝. This can be written as:

The number of parameters in the VAR models are of order 𝑛 2 𝑝 and typically the parameter tensor A := [𝑨 (1) , • • • , 𝑨 (𝑝 ) ] ∈ R 𝑁 ×𝑁 ×𝑝 is penalized with either ridge or lasso regularizers. If a good preestimator of the tensor is available, then the regularizer can be modified to the adaptive lasso [25] which takes the form:

where B is the element-wise reciprocal of the pre-estimator Â and ⊙ is the element-wise multiplication operation. The model complexity of the forecasting component 𝒇 grows quickly as we consider higher time lags in 𝒇 with VAR models. This curse of high-dimensionality, coupled with limited sample sizes may lead to severe overfitting in high-dimensional VARs (even if one imposes ℓ 1 -based sparsity). KGs can help reduce the large model complexity in VARs in a transparent way with the use of graph NN-based approaches, as we discuss next.

Graph Convolutional Networks. The knowledge graph information can be encoded as adjacency matrices in a different class of models which are referred to as GCNs [30]. In a special case for timeseries forecasting (single-layered GCN with a linear function on the graph Laplacian), this family nicely restricts the large number of parameters associated with higher-order VARs. GCNs process past time-samples of multivariate time-series with graph operations, e.g. graph convolutions, before feeding them into a linear model of significantly reduced model complexity. This model compression aspect of graph-based linear models over high-dimensional VARs appears to lead to improved forecasting performance in financial prediction tasks with large panels and limited data.

A single-layered GCN falls under the linear model class. We write the conditional mean function 𝒇 for GCN as 𝒇 𝑡 = Ĝ𝑿 𝑡 𝒘, where

D1/2 is the normalized graph matrix apriori defined based on the KG, D𝑖𝑖 = 𝑗 (𝑮 + 𝑰 ) 𝑖 𝑗 , and 𝒘 ∈ R 𝑝 is the weight vector to be estimated. We impose ℓ 2 regularization on 𝒘, i.e. Ω 𝒇 (𝒇 ) = 𝜆 𝒘 ∥𝒘 ∥ 2 2 . A single-layered GCN is a highly structured instance of a high-dimensional VAR model; the model complexity for the forecasting component reduces from 𝑁 2 𝑝 for VAR to 𝑝 in GCN because of parameter sharing and availability of (weighted) graph connectivity. The limited data sample scenarios benefit from this model compression as long as the KG has informative connectivity structure.

Higher-order Graph Convolutional Network. It has been shown in literature that higher-order GCNs improve the predictive performance in many classification tasks [2]. These networks learn from powers of adjacency matrix We consider the N-GCN [2] that feeds each power of the adjacency matrix into parallel GCN layers and processes the outputs through a fully connected layer. Both GCN and N-GCN models can be stacked to form two-layered networks with an intermediate non-linear activation function as done by [2,30]. Note that we adapt the GCN and N-GCN architectures to cater to time-series forecasting, where we use only the previous time-steps as covariates and aggregate loss over the (time) sample dimension. Both GCN and N-GCN models have very few parameters to learn and hence they serve as good candidate models to estimate conditional mean function 𝒇 in limited sample settings.

Temporal (Graph) Neural Network Models. We consider some temporal neural network architectures e.g. LSTMs, temporal GCNs which model the temporal dependence in the time-series. Multivariate LSTMs are good at capturing long short-term dependencies but lack the capacity to exploit graph-structured information and therefore tend to underperform when compared to the temporal GCNs. There are many temporal graph convolution variants. For instance, T-GCN follows graph convolution layers by gated recurrent units [48]; along the same spirit, a multitude of architectures such as dynamic graph convolutional networks [35], diffusion convolutional network [34], spatio-temporal graph convolutional networks [46] etc. model dynamic dependence with recurrent/convolutional layers with some intermediate graph convolution operations. All these models are highly over-parameterized and our empirical investigation showed they don't work well in the small sample regimes where 𝑇 ≤ 𝑁 and 𝑁 is even moderate as we consider.

## Learning the error precision matrix

The nonzero pattern of the precision matrix 𝑪 := ((𝑐 𝑖 𝑗 )) is closely related to Gaussian graphical model [38], which corresponds to the nonzero edges of the partial correlation matrix. Specifically, the partial correlation 𝜌 𝑖 𝑗 between 𝜖 𝑖𝑡 and 𝜖 𝑗𝑡 has the expression:

graphical lasso [21,47] which considers an ℓ 1 -regularized negative log-likelihood criteria, is a popular method to estimate 𝑪 under the sparsity assumption. However, this leads to a semi-definite optimization problem, which can be hard to scale for large panels. Furthermore, as our goal is to jointly learn 𝒇 (possibly a GCN) and 𝑪, using Tensorflow, we do not pursue this approach -instead, we use a pseudo-likelihood-based approach [8] outlined below.

For a multivariate Gaussian distribution, the conditional distribution of 𝜖 𝑖𝑡 given {𝜖 𝑘𝑡 : 𝑘 ≠ 𝑖} is given by:

The pseudo-likelihood [8] framework makes use of (4) to approximate the negative log-likelihood of 𝝐 𝑡 in (1) by the following expression (ignoring constants)

To learn a sparse 𝝆 (or sparse 𝑪), one can use a sparsity inducing penalty on 𝝆 [25]. Additionally, as we discuss in Section 4.3 we can use KG-based information to guide sparsity pattern discovery in 𝝆.

Following [5,42], we consider a slight reformulation of (5) leading to the weighted loss function

where 𝑤 𝑖 's are nonnegative weights, and 𝒄 ∈ R 𝑁 denotes the diagonal vector of 𝑪. When the weights 𝑤 𝑖 are taken to be equal to 𝑐 𝑖𝑖 , this loss ( 6) is equivalent to the pseudo-likelihood function (5) when 𝑐 𝑖𝑖 's are fixed. Therefore, we provide a statistical interpretation for (6) as an extension of pseudo-likelihood loss. Following [5], we will use 𝑤 𝑖 = 1/𝑁 for our loss function. With the weighted loss (6), we reduce the learning of 𝑪 to the learning of {𝝆, 𝒄}. However, since we learn 𝝆, 𝒄 (and 𝒇 ) at the same time, the optimal solution of {𝑐 𝑖𝑖 }'s to this formulation does not necessarily maximize the original pseudolikelihood loss (5), because of the missing logarithmic terms in (6). However, according to (4), 𝑐 -1 𝑖𝑖 is the conditional variance of 𝜖 𝑖𝑡 given 𝝐 -𝑖𝑡 . We make use of this relationship in Algorithm 1 while updating the parameter 𝑐 𝑖𝑖 's.

## Using knowledge graph information

In a nutshell, KGs provide us useful alternative connectivity/similarity information across time-series components. This can help in reducing the number of parameters in model (1) in the form of sparsitypriors on the components 𝑪 and 𝒇 (when 𝒇 is a GCN). This allows us to obtain good forecasting for the financial time-series applications discussed in our experiments especially for a large number of panels with limited training data.

### Nearest neighbors based KGs.

Given a KG 4 , we create a symmetric weight matrix 𝑮 so that each entry 𝐺 𝑖 𝑗 measures the strength of similarity between 𝑖 and 𝑗 in the KG. However, the weight matrix 𝑮 given by the KG is not always sparse. We use a "K-nearest neighbor" (KNN)-scheme to extract a sparse connectivity structure E from the dense graph. Specifically, given a pre-specified neighborhood sparsity-level 𝐾, for any company 𝑖, we can define its neighborhood 𝑁 𝐾 (𝑖), as those companies 𝑗's that have top 𝐾 weights 𝐺 𝑖 𝑗 among 𝑗 ≠ 𝑖. We denote by

the set of edges obtained by these 𝐾-nearest neighbors induced by the graph 𝐺. In our experimental section (Section 5), we apply nearest neighbor method to extract important connectivity from two different graphs-the EDGAR cosearch KG and the returns partial correlation, and demonstrate the gains of using KGs.

In passing we note that there may be other ways to extract a sparse-matrix E from 𝑮. For example, clustering techniques can help identify the clusters of firms, and E can be defined as the set of edges between firms within the same cluster. In our experience, these methods were less effective than the KNN method.

### Masking matrices.

After we extract the sparse connectivity structure E from 𝑮, we define two types of masking matrices (hard/soft) as follows. The hard masking matrix is defined as

If 𝐺 max denotes the maximum entry of 𝑮, we define the soft masking matrix 𝑴 soft as follows

) These masking matrices -𝑴 ∈ {𝑴 hard , 𝑴 soft } -are used to impose modified regularization penalty on 𝝆. As the masking entry becomes larger, the penalty imposed on the corresponding entry of 𝝆 increases. A large entry essentially zeros out the corresponding element in 𝝆, reducing model complexity. With these additional masking weights, we re-define our new masked regularizers as follows: Lasso:

where 𝒓 is the element-wise reciprocal of the prior knowledge/preestimator of 𝝆.

In our experience, the masked regularizers were found to be effective from the perspective of learnability in small sample settings. The model complexity for partial correlation only grows as O (𝐾𝑁 ) as opposed to O (𝑁 2 ) without any KG. This reduced model complexity for 𝝆 becomes even more crucial when the conditional mean function 𝒇 is over-parameterized. The reduced parameter space for 𝑪 leads to improvements in predictive performance and sparsity of the network structure induced by 𝑪-as we consistently observe in our empirical results.

# 4.3.3

Using multiple knowledge graphs. Sometimes we may have multiple KGs encoding complementary side-information on the panel components. We present a simple but useful strategy to extend GregNets to handle multiple KGs. For simplicity, we assume that we have weight matrices 𝑮 (1) and 𝑮 (2) from two KGs. Let E (𝑘 ) be the sparse structure extracted from 𝑮 (𝑘 ) , 𝑘 = 1, 2, and G (𝑘 )

be the graph matrix of 𝑮 (𝑘 ) restricted to the edges E (𝑘 ) , i.e. for (𝑖, 𝑗) ∈ E (𝑘 ) ,

𝑖 𝑗 ; for (𝑖, 𝑗) ∉ E (𝑘 ) , G (𝑘 ) 𝑖 𝑗 = 0. For a given weight 𝛼 ∈ (0, 1), we define the new graph matrix 𝑮 as the convex combination of the restricted matrices, i.e. 𝑮 = (1 -𝛼) G (1) +𝛼 G (2) , and we define the sparse structure E as the union of E (1) and E (2) . With the new graph 𝑮 and the sparse structure E, we can create the soft and hard masking matrices and their corresponding masked regularizers induced by the new graph. Note that hard masking matrix only looks at the union of the individual components; and remains the same for all 𝛼 ∈ (0, 1). The soft masking matrix considers a weighted combination of the constituent graphs, and changes with 𝛼. In the experiments section (Section 5), we demonstrate that the combined graph can outperform the constituent graphs individually.

## Joint Training

Finally, we present the joint training algorithm. This is given by the following optimization problem:

where, the optimization variables are (𝝆, 𝒇, 𝒄), with

and Ω 𝑓 , Ω 𝜌 are regularizers that control the model complexity of the conditional mean and the partial correlation structure. Ω 𝑓 can be an explicit regularizer (e.g., ℓ 1 -penalty) as in the case of VAR model or an implicit regularization (e.g. dropout) in the context of

# Algorithm 1 Algorithm for optimizing VAR-PC

Require: Learning rate 𝛾, Initialization A [0] , 𝝆 [0] , 𝑪 [0]  1: for 𝑘 = 0, 1, 2 . . . do 2:

Update 𝒘

, 𝝆 [𝑘+1] ) by solving min

where w = 𝒘 [𝑘 ] -𝛾 ∇ 𝒘 𝐿(A [𝑘 ] , 𝝆 [𝑘 ] , 𝒄 [𝑘 ] )

Compute 𝜖

Compute 𝑢

GCNs. Ω 𝜌 are regularizers with/without KG-based masking that induce the sparsity structure of 𝝆 (i.e. that of 𝑪). We first outline our algorithm for joint optimization when the conditional mean function is taken to be the 𝑝th-order VAR and the partial correlation regularizers are taken to be as those in (9). We denote this model as VAR-PC (VAR with partial correlation). In Section 4.4.2, we describe our joint optimization setup when conditional mean function is any multivariate time-series forecasting model with deep learning APIs via the implementation of a pseudo-likelihood layer.

## Proximal Gradient Descent Algorithm for optimizing VAR-PC.

We develop a custom algorithm for (10) when 𝒇 is a VAR model ( 2) parameterized by the tensor A ∈ R 𝑁 ×𝑁 ×𝑝 , and the corresponding Ω 𝒇 (𝒇 ) becomes Ω A ( A). In brief, our algorithm is alternately updating 𝒘 = ( A, 𝝆) by proximal gradient descent [7,39] and a model-based update for 𝒄 (in line 5 of Algorithm 1). For the latter, we make use of the fact that each 𝑐 𝑖𝑖 is the reciprocal of the conditional variance of 𝜖 𝑖𝑡 given 𝝐 -𝑖𝑡 (see (4); and also Section 4.2 for further details). The algorithm is detailed in Algorithm 1.

It is important to highlight here that the VAR-PC model is considered in [5] and constitutes a special case of the modeling framework without any KG input. They propose a generalized active shooting algorithm to solve the joint optimization problem with VAR forecasting component. Their optimization algorithm is not scalable for even moderate number of multivariate time-series. In fact, our experimentation with their available nets package5 in R demonstrates our algorithm is 100 × -250× faster than their solver in optimizing the VAR-PC problem for 𝑁 = 403 firms in SP500 and 𝑇 = 504 samples 6 , and their final objective values are about 1%-17% higher than the objective values obtained by our algorithm.

## Joint optimization with

Pseudo-Likelihood Layer in Tensorflow Keras. For joint learning of a general multivariate time-series NN forecasting model e.g. GCNs along with the error correlation structure, we define a pseudo-likelihood layer that has two sets of trainable parameters {𝝆, 𝒄} to learn the correlation structure. The layer takes the prediction 𝒇 , the response variable 𝒚, and the KG masking matrix 𝑴 and sums the weighted loss ℓ given in (11) with the knowledge-graph based regularization Ω(𝝆). This loss is backpropagated to the conditional mean function 𝒇 as training proceeds. However, this loss definition alone is not sufficient to arrive at the interpretable correlation matrix with backpropagation as there is a non-identifiability problem with the correct scales of 𝒄 in the loss (11). We again use the fact that 𝑐 𝑖𝑖 is the reciprocal of the conditional variance of 𝜖 𝑖𝑡 given 𝜖 -𝑖𝑡 and use this to update the vector 𝒄 during backpropagation stage of the algorithm and let the deep learning API update the partial correlation via the backpropagated gradients. This ensures the interpretation of the two components isn't lost during training. This allows use of any SGD optimizer and its variants to jointly estimate both the conditional mean and the error correlation structure.

# EXPERIMENTAL RESULTS

In this section, we evaluate the performance of GregNets on a real-world financial application, and demonstrate the benefits of using KG information. In Section 5.1, we first introduce the time series data sets and the associated KGs. All the datasets used in our experiments are available in the public domain. We introduce the experimental setup in Section 5.2 and discuss the results in Section 5.3.

## Data

Stock Volatilities Time-Series. We evaluate the combination of timeseries prediction with KG in the context of market volatilities. Volatilities analysis has been previously studied in [5,[14][15][16]. We consider two different financial markets S&P500 and S&P1500 and define the daily volatility, as given in [5,14,41], using the daily high and low stock prices: σ2

and 𝑝 low 𝑖𝑡 denote the maximum and minimum price of stock 𝑖 on day 𝑡. There are some valuable insights in a large body of literature regarding the influence of common factors in the network on the sparsity level of correlation structure. In summary, [6] shows that it is necessary to remove the market-wide and sector-wide volatility factors to evaluate the idiosyncratic behavior in terms of correlation of firms. Following [5], we condition on the corresponding market index: S&P500 or S&P1500 and 9 sector indices This reduces the number of companies to 403 for S&P500 and 1, 072 for S&P1500 markets. More details about market and sector indices are given in the Appendix. Our target variable 𝒚 is the idiosyncratic volatility residuals computed via least squares adjustment.

Knowledge Graph using EDGAR Cosearch. We follow [33] to generate a KG between firms by collecting cosearch of peer firms by users of the EDGAR website (https://www.sec.gov). Analysts collectively search for financial data on economically-related firms. [33] explored how the cosearch of peer firms by users of EDGAR explains a degree of similarity between firms. Hence, we use cosearch for meaningful graph connectivity and construct a KG. Specifically, for each pair of firms (𝑖, 𝑗), the number of unique users searching for both firms 𝑖 and 𝑗 is used to define a daily co-search proportion, which we aggregate annually. These proportions reflect a collective view of similarity between firms across all users. We evaluate the effectiveness of this KG within the context of GregNets when used to learn (a) 𝑪 using KG-guided masked regularizers and (b) 𝒇 via GCNs with KG-guided adjacency matrices.

Returns partial correlation graph as KG (PC KG): In addition to the EDGAR co-search KG, we test our GregNets framework using another KG created from open-source data. This is based 𝑖 on day 𝑡. Following the same procedure used for processing of volatilities, we remove the market-wide and sector-wide factors of returns to get the idiosyncratic return residuals. We then compute the Ledoit-Wolf estimator of the covariance matrix [32], take the inverse, and get the partial correlation matrix via (3). We expect the conditional correlation structure of idiosyncratic return residuals may provide some information into the structure of volatility residuals. Therefore, we consider this as our second example of KG.

## Experimental Setup

Our experimental setup considers two financial markets S&P500 and S&P1500, using daily stock volatilities residuals from 2013-2016. This period was selected because EDGAR cosearch data is only publicly available till 2017 second quarter. We set 2013-2014 as the training period, 2015 as hyperparameter validation period and 2016 for final model evaluation. There are 504 days in the training period (as compared to the 403 companies for SP500 and 1,072 companies for SP1500) to evaluate our proposed methodology on small sample size regime. We evaluate our modelling approach in terms of 𝑅 2 performance and sparsity of partial correlation structure. We follow similar 𝑅 2 definition as used in [5] where the computation of 𝑅 2 uses zero-mean prediction in the denominator (as the market and sector factors have been accounted for). However, we consider the joint 𝑅 2 of the conditional mean and the partial correlation structure. We evaluate the utility of KG-based regularizers (constructed from two different KGs, in particular EDGAR Cosearch-based KG and returns PC KG) by comparison with various regularizers that do not use additional KG connectivity information. We perform the optimization for VAR-PC using the algorithm proposed in Section 4.4.1 and in this case the baseline scenario refers to non-masked regularized VAR-PC model optimized via our own algorithm. We also evaluate the effectiveness of the joint learning framework for NN-PC with KGs in the context of general multivariate time-series models (e.g. LSTMs, GCNs, N-GCNs, T-GCNs) with Keras using the optimization strategy outlined in section 4.1. Hyperparameter tuning details are given in the Appendix.

## Discussion of Results

VAR-PC using cosearch graph. We present our results for different regularizers in  defined in Section 5.1. We compare the joint learning framework with the two stage approach with VAR-ridge, followed by Ledoit-Wolf estimator for precision matrix on the residuals. We see large gains in 𝑅 2 with the joint framework over this baseline. We also compare our proposed KG-based regularizers with their vanilla lasso/adaptive lasso counterparts. We observe that KG-based regularizers outperform both in terms of improvement in 𝑅 2 and sparsity of the estimated error correlation structure. To test generalizability of our approach to other financial indicators, we also considered prediction of daily log trading volume -see Appendix. In Fig. 2, we display the test 𝑅 2 's of VAR-PC with soft masking of the cosearch graph with different number of nearest neighbors 𝐾, as well as the sparsity of the learned partial correlation 𝝆 for S&P1500. The dashed lines correspond to VAR-PC Lasso without using any KG. We note that we start to see improvement in 𝑅 2 by using KG from 𝐾 = 75; also, the KG-masked partial correlation structure is much sparser than the one learned with vanilla Lasso.

Moreover, in Fig. 3, we show the sparsity patterns of partial correlation along with the blocks of 9 sectors for two different algorithms, with/without use of cosearch KG information. For illustration purpose, we sample 40% random companies in S&P1500 from each sector (433 companies in total) to plot the heatmap. The figure indicates that even after removal of market and sector trends, the volatility residuals still tend to have more partial correlation connections within the sectors. Empirically, we observed that KGmasked regularization led to a higher precision in recovering the edges within the same sectors. See Appendix for more details.

VAR-PC using the combined graphs. In Fig. 4, we present the test 𝑅 2 of VAR-PC using convex combination of returns PC graph and the cosearch graph In the plot, we take 𝛼 ∈ {0, 0.1, 0.2, . . . , 0.9, 1} to show the performance of the different weighted graphs with both hard and soft masking matrices, where 𝛼 = 0 corresponds to the return PC graph, while 𝛼 = 1 corresponds to the cosearch graph. For both S&P500 and S&P1500 markets, we see a flat curve for hard masking when 𝛼 ∈ (0, 1), above the 𝑅 2 of both end points, which implies using the union of the sparse structure helps improve the performance. For the soft masking case, the best combination (𝛼 = 0.9) outperforms the test 𝑅 2 from hard masking. For S&P500, the test 𝑅 2 is 35.90%, which is even better than any results using the cosearch graph alone. For S&P1500, the test 𝑅 2 using the combination with 𝐾 = 75 is comparable to the cosearch graph masking with 𝐾 = 125. Compared to soft masking on cosearch graph, soft masking with 𝛼 = 0.9 may have almost the same effect on the edges from the cosearch graph, but it also allows for the edges from the return PC graph (with high penalties). Therefore, the superior performance of the combined graph over the cosearch graph implies that the strong partial correlation connections are mainly from the cosearch graph, but the return PC graph contains some important weak connections that can help improve the prediction.   Multivariate (Graph) Neural Networks with partial correlation using KGs. We present GregNets for the joint learning framework for various multivariate time-series with partial correlation in Table 2. For each model, we display the two cases corresponding to whether KG-based masking is used or not in definthe regularizer. We consistently see a gain in performance in terms of 𝑅 2 and sparser precision-matrix estimates with the use of KG-based regularizers. We highlight that VAR-PC models outperform both LSTM-PC and temporal graph convolution networks (T-GCN-PC) perhaps due to over-parameterization in these recurrent NN architectures; hence models tend to overfit severely when there are few to learn from. We see significant gains in predictive performance with simpler graph convolution architectures such as GCNs and N-GCNs. This confirms the effectiveness EDGAR cosearch graph as an adjacency matrix in the context of stock volatility with GCNs. We similarly observe better predictive performance by learning from graph with N-GCN as observed in applications (e.g. citation datasets [2]).

Fig. 5, we compare the test 𝑅 2 for each sector for both PC and N-GCN-PC models. We observe a gain in performance across all sectors with N-GCN-PC with the use of KG information for correlation estimation. We also include the two-stage baseline model VAR-Ridge for comparison.

# CONCLUSION

In summary, we propose a general framework GregNets for jointly learning multivariate time-series models (e.g. VARs, GCNs, LSTMs etc.) with their correlation structures using knowledge graphs with our proposed pseudo-likelihood layer. Based on empirical evidence, our approach leads to improved prediction, reduced model complexity, computational efficiency and interpretability.

# ACKNOWLEDGMENTS

This work is supported by the MIT-IBM Watson AI Lab, Refinitiv, an LSEG (London Stock Exchange Group) business, and Wells Fargo & Company through the Membership Program of the MIT-IBM Watson AI Lab. The views and conclusions are those of the authors and should not be interpreted as representing the official policies of the funding agencies. The authors acknowledge the MIT SuperCloud and Lincoln Laboratory Supercomputing Center for providing HPC resources that have contributed to the research results reported within this paper.

# A APPENDIX A.1 Experimental Setup

For the detrending step mentioned in Section 5.1, we use SP500 Index ETF (SPY) and SP1500 Index ETF (SPTM) as market indices for S&P500 and S&P1500 financial markets respectively. We use the following 9 sector indices: Consumer Discretionary (XLY), Consumer Staples (XLP), Energy (XLE), Financials (XLF), Health Care (XLV), Industrials (XLI), Materials (XLB), Information Technology (XLK), and Utilities (XLU), and we will use "Disc", "Stap", "Energy", "Fin", "HC", "Ind", "Mat", "IT", "Util" as abbreviations to denote these sectors in Table 3.

A.2 Tuning parameters for Section 5.2

# VAR-PC:

• 𝜆 𝐴 : Log uniform in the range [10 -9 , 10 -6 ],

• 𝜆 𝑝 for Lasso/Adaptive Lasso: Log uniform over the range 

# A.3 Additional Results

Sector recovery by 𝝆. In Table 3, we show the precision of recovering the edges within the same sectors. For each sector 𝑆 𝑘 , we consider the set of all edges from the sector, i.e. {(𝑖, 𝑗) : 𝑖 ∈ 𝑆 𝑘 }, as all samples, and report the precision metrics of whether the sparsity pattern given by learned 𝝆 can correctly recover the edges within the same sector, i.e. the set {(𝑖, 𝑗) : 𝑖, 𝑗 ∈ 𝑆 𝑘 }. The table indicates that for all the sectors, the 𝝆 learned using KG has higher recovering precision than the one learned without KG. Additional results of VAR-PC for S&P500 and S&P1500 volume. Finally, we evaluate our VAR-PC framework in predicting the S&P500 and S&P1500 daily trading volumes. We apply the same detrending process to the log trading volume time series, and use the EDGAR cosearch KG in GregNets. The results of VAR-PC are summarized in Table 4. The results still exhibit the 𝑅 2 boost and sparsity improvement when incorporating the KG information into the model. 

