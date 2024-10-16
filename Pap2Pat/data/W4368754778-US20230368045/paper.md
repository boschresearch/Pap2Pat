# Introduction

Many dynamical systems, such as traffic flow (Li et al., 2018;Yu et al., 2018), fluid dynamics (Ummenhofer et al., 2019) or human motion (Jain et al., 2016), involve interactions between agents. Graph Neural Networks (GNN) (Battaglia et al., 2018) have recently emerged as a powerful tool in these settings, since they allow learning the dynamics of interacting systems from data only. Recent research has made great advances for modeling deterministic complex systems by being able to extrapolate from systems with a small number of agents and short time horizons to systems with a high number of agents and long time horizons. These methods have been successfully applied to a number of physical systems covering fluids, rigid solids and deformable materials (Sanchez-Gonzalez et al., 2020). However, for many real-world applications, predicting a single future trajectory for each agent is not enough, since the stochasticity in the dynamical system has significant consequences. For instance, in autonomous driving, the driver's intention (e.g. overtaking, turning, lane changing) is a hidden factor that may induce different modes of driving trajectories.

Figure 1: We approximate the predictive distribution of a latent Graph Deep State-Space Model (GDSSM) as a Gaussian mixture distribution via deterministic moment matching rules. Given historical information in the form of observed trajectories (dashed lines), our proposed GDSSM architecture predicts the future dynamics while taking interactions between traffic participants into account. We present the true future trajectories (left-most plot) as solid lines. For each mode and traffic participant, we show the predicted 95% confidence interval of our model (three right-most plots). Our model accounts for interactions, for example, the brown vehicle is only entering the roundabout if the blue vehicle is staying in the roundabout (Mode 1). If the blue vehicle is leaving the roundabout, the entering lane for the brown vehicle is blocked by the blue vehicle (Mode 2, Mode 3) and the brown car has to wait. The ground truth data and the map come from the rounD dataset (Krajewski et al., 2020).

In the deep learning literature, multiple architectures have been successfully applied to time-series data with two prominent classes being a) recurrent methods that apply a fixed transition model repeatedly at each time step (e.g. Hochreiter (1991), Chung et al. (2014)), b) history-based methods that aggregate information from the past using either convolutional filters (e.g. Bai et al. (2018), Oord et al. (2016)) or attention modules (e.g. Vaswani et al. (2017), Li et al. (2019)). Recurrent methods capture the internal state of the system at each time point t in a latent state x t . Predicting the output in this manner respects the causal order of the dynamical system, i.e. the latent state x t of time point t is needed in order to compute the latent state x t+1 at the next time point t + 1. State-space models (e.g. Särkkä (2013)) belong to the class of recurrent methods. They are defined by two probability distributions: the transition model, p(x t+1 |x t ), that propagates the latent state forward in time and the emission model, p(y t |x t ), that maps the latent state into the observational space. Obtaining multistep-ahead predictions for state-space models requires propagating distributions in the latent space. For general transition models, this operation cannot be done in closed-form and existing methods either use numerical integration schemes (e.g. Solin et al. (2021), Look et al. (2022)) or Monte Carlo methods (e.g. Krishnan et al. (2017), Bayer et al. (2021)). For interacting systems, the latent space grows linearly with the number of agents, requiring a high number of MC samples, which can make these methods prohibitively slow. To the best of our knowledge, numerical integration schemes have not been explored for multi-agent dynamical systems. In contrast, probabilistic history-based methods directly predict the distribution over future trajectories, mitigating the sampling overhead. However, this approach make the learning problem hard as the model needs to learn the future distribution for multiple time steps ahead. To account for this, complex models (e.g. large neural networks) are often necessary. This can prevent their usage in embedded systems with limited memory capacity.

In this work, we present a novel approach for modeling stochastic dynamical systems with interacting agents that is able to generate expressive multi-modal predictive distributions over future trajectories in a runtime and memory efficient manner. We model the unknown stochastic dynamical system as a Deep State-Space Model (DSSM) in which the shared dynamics of all agents are modeled in a joint latent space using GNNs. Our model belongs to the family of recurrent neural networks and we replace the expensive MC operations during training and testing by introducing a novel deterministic moment matching scheme. Prior work (Look et al., 2022) on moment matching for dynamical systems does not consider interacting systems and is restricted to unimodal processes. We overcome the first limitation by applying GNNs in the transition model and the second limitation by placing a Gaussian Mixture Model (GMM) over the initial latent state. For each mixture component, we independently apply our moment matching rules in order to arrive at multimodal predictive distributions over future trajectories. In autonomous driving, the initial latent state is often estimated from historical information and can provide information about the drivers' intentions (Tang & Salakhutdinov, 2019). Conditioned on the initial latent state, the predictive distribution can often be accurately modeled with an unimodal distribution (Cui et al., 2019;Chai et al., 2019). Finally, as there exists a wide variety of dense traffic scenarios, the high number of agents can result in prohibitively large GMM covariance matrices as their size grows quadratically with the number of traffic participants. We address this problem by proposing structured covariance approximations.

We summarize our contribution as follows:

• We derive output moments for GNN layers, which makes GNNs applicable to moment matching algorithms. This leads to the first deterministic inference scheme for deep state-space models for interacting systems.

• We introduce a GMM distribution over the initial latent states that results in multimodal predictive distributions over future trajectories.

• We propose structured approximations to the GMM covariance matrices that can reduce the computational complexity of our approach from O(M 3 ) to O(M 2 ), where M is the number of agents.

In our experiments, we benchmark our proposed model on two challenging autonomous driving datasets.

Our results demonstrate that our deterministic model has strong empirical performance compared to stateof-the-art alternatives. We visualize the predictive output distribution for a real-world traffic scenario on a roundabout with multiple agents in Fig. 1. The future distribution is highly multi-modal, as traffic participants can leave the roundabout from several exits. Our model is capable of predicting multiple modes, which we efficiently approximate as a GMM, and takes interactions into account using GNNs.

To gain further insights into our model and inference scheme, we carefully examine the impact of the individual contributions of our work in an ablation study. Next, we provide an empirical runtime study of our covariance approximations. Our findings indicate that sparse covariance approximations reduce the computational complexity by a factor of up to 100, which makes them favourable for applications with limited computational resources. We conclude our experiments by studying the generalization capabilities of our model on out-of-distribution data, e.g. traffic environments that have not been observed during training.

# Background

In this chapter, we first provide background on (deep) state-space models for single-agent systems. We proceed by giving a small recap on moment matching rules that allow us to propagate the latent dynamics forward in time in a deterministic manner. Next, we review graph neural networks for interaction modeling. State-space models and graph neural networks form the basis for our new model for stochastic dynamical interacting systems, which we introduce in Sec. 3. The deterministic moment matching rules build the foundation of our training and testing routines that we describe in Sec. 4.

## Deep State-Space Models

State-Space Models (SSM) are a model class for dynamical systems (e.g. Schön et al. (2011), Särkkä (2013)) that assume that each D y -dimensional observed variable y t ∈ R Dy is emitted by a latent D x -dimensional latent variable x t ∈ R Dx . The latents are coupled via first-order Markovian dynamics, e.g. the state at time point x t only depends on the state of the previous time point x t-1 . Typically the observed state y t-1 does not contain all necessary information in order to reliably predict the next observed state y t . Consider the case of traffic forecasting in which the observed state y t contains the position of a vehicle but not its velocity or acceleration data. We can then supply the latent state x t with the missing information in order to allow for accurate forecasts about the next time point. Consequently, SSMs are a flexible model class that allows us to make reliable forecasts about complex systems.

A Deep State-Space Model (DSSM) is a non-linear SSM in which the transition model, that maps the latent state from the current to the next time point, and the emission model, that maps the latent state to the outputs, are realized by neural networks. They come in handy for applications in which the true underlying dynamics have an unknown non-linear functional form and must be estimated from data. Assuming additive Gaussian noise (e.g. Krishnan et al. (2017)), their generative model can be written down as follows

where I ∈ R D I is the context variable that encodes auxiliary information, such as historical or relational information. The mean update f (x t , I) : R Dx × R D I → R Dx , governing the deterministic component of the transition model, is parameterized by a neural net with an arbitrary architecture. Similarly, the variance update L(x t , I) : R Dx × R D I → R Dx + is parameterized by another neural net, which models the stochasticity of the system. Both f and L are neural networks, which are parameterized by θ f and θ L . The emission model follows a Gaussian distribution with mean g(x t ) : R Dx → R Dy and variance Γ(x t ) : R Dx → R Dy + , where g and Γ are both neural networks with arbitrary architecture and parameters θ g and θ Γ .

Assuming additive Gaussian noise allows us to interpret the transition model [Eq. ( 2)] as a discretized neural stochastic differential equation (Tzen & Raginsky, 2019;Look et al., 2022). While we do not pursue this line of work any further, we note that this connection allows for straight-forward extensions to irregularly sampled time series. Finally, there exists work that couples state-space models with recurrent neural networks (Chung et al., 2015;Fraccaro et al., 2016) whose gating mechanism can help in learning long-term effects.

## Transition Kernel

In this section, we provide background on how to compute the t-step transition kernel, p(x t |x 0 , I) with t > 1, which allows us to propagate the latent state forward in time for general state-space models. It is defined by the following recurrence

where p(x 0 |I) follows Eq. (1). It is worth noting that Eq. ( 4) cannot be computed in closed-form since the distribution p(x t-1 |x 0 , I) has to be propagated through the non-linear transition model p(x t |x t-1 , I) [Eq. 2].

### Overview

Various approximations to the transition kernel [Eq. ( 4)] have been proposed that can be roughly split into two groups: (a) MC sampling based approaches (Brandt & Santa-Clara, 2002;Pedersen, 1995;Elerian et al., 2001) and (b) deterministic approximations based on assumed densities (Särkkä et al., 2015). While MC based approaches can, in the limit of infinitely many samples, approximate arbitrarily complex distributions, they are often slow in practice and their convergence is difficult to assess. In contrast, deterministic approaches often build on the assumption that the t-step transition kernel can be approximated by a Gaussian distribution. This assumption can be justified if the transition model can be locally linearly approximated and the observations are sufficiently densely sampled. The transition kernel is then computed in an iterative manner by applying a Gaussian approximation at each time step and propagating the moments along the time direction using a numerical integration scheme (Särkkä & Sarmavuori, 2013;Särkkä et al., 2015).

Prior work in the context of neural SDEs (Look et al., 2022) proposes to first discretize the differential equations and afterwards apply moment matching through the neural network layers as numerical integration scheme. Since the resulting algorithm propagates moments through time and neural network layers, it is termed Bidimensional Moment Matching (BMM). This approach was shown to be superior over standard numerical integration schemes in terms of compute and accuracy. Since the transition model in SSMs can be interpreted as discretized SDEs (Särkkä et al., 2015), we build our work on their approach. Moment propagation through neural network layers has also been applied previously in the context of expectation propagation (Hernandez-Lobato & Adams, 2015;Ghosh et al., 2016), deterministic variational inference (Wu et al., 2019), and evidential deep learning (Haussmann et al., 2020).

### Bidimensional Moment Matching

In this section, we recapitulate the original Bidimensional Moment Matching (BMM) algorithm of Look et al. (2022) and its use for propagating the latent state forward in time [Eq. ( 2)]. BMM approximates the transition kernel p(x t |x 0 , I) by combining horizontal moment matching along the time axis with vertical moment matching across the neural network layers.

# Horizontal Moment Matching

In order to facilitate the computation of the transition kernel, we replace p(x t |x 0 , I) for all time steps t = 1, . . . , T with a Gaussian distribution

with mean µ t (I) and covariance Σ t (I). This approximation simplifies the problem to calculating the first two moments of the transition kernel and is assumed to work well if the dynamics can be locally approximated by a linear model, which is the case for many applications. Assuming that the one-step transition kernel p(x t |x t-1 , I) follows Eq. ( 2), the mean µ t (I) and covariance Σ t (I) can be computed as a function of prior moments µ t-1 (I) and Σ t-1 (I) (Look et al., 2022)

where Cov[x t-1 , f (x t-1 , I)] denotes the cross-covariance between the random vectors in the arguments.

# Vertical Moment Matching

The mean E[f (x t-1 , I)] and covariance Cov[f θ (x t-1 , I)] of the transition function, as well as the expected variance update E[L(x t-1 , I)], can be computed as a result of moment propagation through neural network layers. For many common layers, including affine transformations and ReLU activation functions, the corresponding output moments can be either computed in closed-form or good approximations are available in the literature (Wu et al., 2019). In contrast, approximating the crosscovariance Cov[x t , f θ (x t , I)] cannot be achieved using moment matching rules since we cannot decompose the cross-covariance term into layerwise operations. Instead, we resort to Stein's Lemma using

where the expected Jacobian can be approximated as (Look et al., 2022)

Above, J l t denotes the Jacobian of layer l at time step t. The expectation of the Jacobian is analytically available or can be closely approximated for common layer types.

## Graph Neural Networks

Graph neural networks (GNNs) have emerged as a powerful method for interaction modeling (Battaglia et al., 2018;Hamilton et al., 2017;Gilmer et al., 2017). Given a set of agents and relational information in form of a graph, each agent corresponds to one node in the graph that is equipped with a set of features. The relation between the agents is encoded via the edges and information exchange between the agents takes place by sending messages along the edges. By performing multiple rounds of message-passing, information can flow along the graph. This allows for interactions between non-adjacent agents, provided that a path between the agents exists.

More formally, we define the structure of our GNN as follows. For M agents, a GNN receives as inputs a set of node features x = {x m } M m=1 , where x ∈ R M Dx and x m ∈ R Dx , and a set of edges

which is part of the context variable I ∈ R D I . The edge attribute e m,m has a binary encoding, where e m,m = 1 if agent m and agent m are related. The GNN output is an update of the node features, i.e. z = GNN(x, I) with z ∈ R M Dz , and consists of the following two steps that may be repeated multiple times:

1. For each agent m, receive message x Nm ∈ R Dx by aggregrating information from neighboring agents:

where {x m |e m,m = 1} denotes the set of all neighbours of node m. The aggregation operation AGG is permutation invariant, i.e. it does not change when the ordering of the inputs is swapped and generalizes to a varying number of inputs. A commonly used aggregation operation that we also apply in our work is the mean function.

2. For each agent m, update the node information:

where UPDATE(x m , x Nm , I) : R Dx × R Dx × R D I → R Dz is typically implemented by a neural network.

A simple form of an interacting dynamical system takes the features of each agent at its current position and connects agents that are within a pre-defined radius with edges. The GNN operation updates the position and velocity information of each agent by taking information of the adjacent traffic participants into account.

# Graph Deep State-Space Models

We aim to model stochastic dynamical interactions between agents following complex behavioural patterns, such as road traffic interactions. We extend deep state-space models to interacting systems by proposing Graph Deep State-Space Models (GDSSM), which use graph neural networks in the transition model to capture interactions between agents. We define our probabilistic model in this section and then introduce a novel scheme for efficient and deterministic training and predictions in the subsequent section.

We are interested in modeling the dynamics of M interacting agents with deep state-space models by using a coupled latent space. In other words, instead of using a D x -dimensional latent space for each agent, we assume that the agents share a latent space of size M D x . Since (i) the number of agents can vary between scenes, (ii) the transition model should be agnostic to the order of the agents and (iii) it is challenging to parameterize high-dimensional latent spaces, we use GNNs in the transition model.

More formally, we denote the state of agent m at time step t as x m t ∈ R Dx and the set of all state variables as x t = {x m t } M m=1 . The dynamics of x t follow Eq. ( 2), where the mean update f (x t , I) :

The agent-specific mean update is denoted by f (

Both implement the update function in general graph neural networks [Eq. ( 10)], whereas , x Nm t contains aggregated information of the states from all neighboring agents [Eq.( 9)]. A deterministic variant of our model, e.g. setting L(x t , I) = 0, has been successfully used for learning surrogate models for complex physical systems (Sanchez-Gonzalez et al., 2020). We further assume that it is sufficient to couple the latent dynamics across the agents and keep the emission model [Eq. ( 3)] independent across agents. Note that our transition model consists of a single aggregation and update step which is sufficient if the data is densely sampled such that the information flow between agents is fast compared to the evolution of the state dynamics. However, it is also straight-forward to extend the model to multiple message-passing steps per time point by stacking multiple GNN layers in the mean and variance update function.

Furthermore, we note that although the transition noise factorizes across agents, correlations between agents emerge since the mean and the variance depend not only on the state of the m-th agent, but also on the states of all neighboring agents. After a aggregation steps, our GNN model accounts for correlations between agent m and agent m provided that they are connected by a path that is at most a steps long. In contrast, methods, that only take the state of the m-th agent into account, do not lead to any correlations, while methods, that take the state of all other agents into account, lead to a fully correlated covariance matrix after one time step.

In order to complete the probabilistic description of our model, we further specify the distribution of the initial latent state

where Cat([π 1 (I), . . . , π V (I)]) is a categorical distribution with V mixture components. Each component is specified by its weight π v (I) :

The weights π 1:V form a standard V-simplex. We use a GNN, which we refer to as the embedding function h(I) :

We assume that the context variable I contains relational information as a set of edges as well as historical information for each agent in the form of an observed trajectory. In a sense, the embedding function acts hereby as a filter, which learns a distribution over the initial latent state from past observations.

In autonomous driving, the initial latent state can be connected to the drivers' intention (Tang & Salakhutdinov, 2019). The context information I is often not sufficient to rule out different hypotheses about the future, e.g. does the car behind us want to overtake in the next five seconds or not. Using a mixture model allows us to incorporate different hypotheses into the model in a principled manner, which will ultimately lead to highly multimodal predictive distributions.

State-space models and graph neural networks have been previously combined for multi-agent trajectory forecasting by Yang et al. (2020). In contrast to our work, the authors (i) use a different model definition by applying recurrent neural networks and a non-Gaussian density in the transition model and (ii) perform Monte Carlo sampling during inference which can lead to slow convergence. In the next chapter, we show that our model definition allows for more efficient training by performing deterministic moment matching rules. We compare against Monte Carlo alternatives in our experiments.

# Deterministic Approximations for GDSSMs

In this chapter, we present our novel inference scheme for GDSSMs that enables efficient and deterministic training and predictions. In Sec. 4.1, we first give a short overview over existing inference techniques and compare it to our scheme which aims at directly maximizing the predictive log-likelihood of future trajectories. The predictive log-likelihood cannot be computed in closed-form. We propose an efficient and deterministic approximation to it in Sec. 4.2 that relies on bidimensional moment matching. Our moment matching rules necessitate the computation of output moments and expected Jacobians of graph neural network layers. We present ouput moments for commonly used layers in Sec. 4.3. As our algorithm approximates the output distribution at each time step with a Gaussian mixture distribution over all agents, the resulting covariance matrix for each mixture component can become computationally intractable for a large number of traffic participants. We address this pain point in Sec. 4.4 by proposing sparse approximations to the covariance.

## Parameter Inference

Classical inference methods for state-space models aim at directly maximizing the log-likelihood of the data

where p(x t |x t-1 , I) is defined in Eq. ( 2) and p(y t |x t ) in Eq. ( 3). This quantity can only be computed in closed-form if the emission and transition model are linear Gaussians. In our case, the transition model is parameterized by a graph neural network and the emission model by a standard neural network. Both functions are highly non-linear and render an analytical solution to Eq. ( 14) infeasible.

Therefore, most existing methods apply either a particle filter (Schön et al., 2015), variational inference (Krishnan et al., 2017;Bayer et al., 2021) or a combination of both (Naesseth et al., 2018;Maddison et al., 2017;Le et al., 2018) in order to approximate the log-likelihood. All of these approaches have in common that they require learning a proposal distribution q(x 0 , . . . , x T |y 1 , . . . , y T ). In particle filtering, the proposal distribution is recursively defined by the importance function q(x t |x 0 , . . . , x t-1 , y 1 , . . . , y t ) and is optimal in terms of variance by setting q(x t |x 0 , . . . , x t-1 , y 1 , . . . , y t ) = p(x t |x t-1 , y t ) (e.g. Doucet et al. (2000).

Variational inference aims to find the best approximation to the true posterior within the chosen variational family by minimizing the Kullback-Leibler (KL) divergence between the true and approximate posterior (Blei et al., 2017), while variational sequential Monte Carlo seeks to minimize the KL divergence on an extended sampling space (Le et al., 2018).

However, the proposal distribution is only used as an auxiliary tool during inference. For many prediction tasks (Djuric et al., 2020;Jain et al., 2019;Chai et al., 2019) where the transition kernel p(x t |x 0 , I) is defined in Eq. ( 4).

In contrast to the standard training objective, the predictive log-likelihood propagates the latent state forward in time without receiving any feedback from the observations; mimicking the behavior during test time. Since we want to use the same objective during training and test time, we opt for directly maximizing the predictive log-likelihood during training. The observation that using one-step ahead predictions in training is not sufficient in order to obtain reliable multi-step ahead predictions during testing has also been made in Bengio et al. (2015) where the authors propose a scheduled sampling strategy in order to gradually switch from single to multi-step ahead predictions during training. Multi-step ahead training has also been successfully applied for spatio-temporal forecasting (Pal et al., 2021) and model-based planning (Hafner et al., 2019).

The PLL aims at optimizing the average marginal log-likelihood log p(y t |I), while the standard objective aims at optimizing the joint likelihood log p(y 1 , . . . , y T |I). We deem the choice between the two objectives application dependent: The PLL is most useful for tasks that can be solved by assessing the marginal distributions only. An important and large application class that falls into this category is in the context of autonomous driving in which the marginal distributions of neighboring traffic participants at a given time horizon are often sufficient in order to control the car (e.g. Herman et al. (2022)). As a consequence, many papers in the autonomous driving literature report as evaluation metrics the performance of their method at fixed time intervals which matches our PLL objective (e.g.  2019)). In contrast, optimizing the joint log-likelihood is preferred for tasks that require sampling realistic looking trajectories, as it is done for instance in sentence generation (Vaswani et al., 2017).

## Approximating the Predictive Log-Likelihood using Bidimensional Moment Matching

We are interested in the predictive log-likelihood PLL(y 1 , . . . , y T |I), which describes the predictive loglikelihood of all traffic participants up to time step T . In order to calculate it, we need to solve the nested set of integrals given in Eq. ( 15). The BMM algorithm allows us to approximate the transition kernel p(x t |I) = p(x t |x 0 , I)p(x 0 |I)dx 0 in case that the initial state x 0 has a Gaussian distribution. However, in our model formulation, the initial latent state x 0 follows a GMM to allow for multimodality. In order to account for that, we approximate the marginal latent distribution p(x t |I) as

where each mixture component p(x 

where a t,v (I) and B t,v (I) are the mean and covariance of the v-th mixture component at the t-th time step. These two moments are available as

which is a direct outcome of the law of the unconscious statistician. We present the pseudocode for computing p(y t |I) using our method in Algorithm 1. Algorithm 2 further shows how we can optimize our model parameters employing the PLL [Eq. ( 15)] as a training objective.

In our method, we approximate p(x t,v |I) and p(y t |I) by applying moment matching to each Gaussian mixture component independently. We note that this approximation becomes exact for locally linear transition and emission functions as stated in Thm. 1.

Theorem 1. The marginal distribution p(y t |I) is analytically computed as

for a GDSSM with the below generative model 

GMM at initial step, Eq. 13

Eq. 18 end for return For general non-linear transition and emission functions, the quality of this scheme depends on two factors: (a) how well the transition and emission function can be approximated in a locally linear fashion and (b) if the covariance matrix Σ t,v is small enough over the time horizon t. We observe in our experiments that the approximation works well and further illustrate its behavior on a small toy dataset in Fig. 2. Finally, we note that Gaussian mixture models have also been successfully used for filtering problems (Alspach & Sorenson, 1972) where, similar as in our work, moment matching is performed for each component individually in the predict step.

## Output Moments of Graph Neural Network Layers

In order to use the the BMM framework, we need to be able to calculate the first two output moments as well as the expected Jacobian of graph neural network layers. In the following, we derive the analytic expression of the output moments and expected Jacobian for the common graph neural net layers: (i) node-wise affine transformation, and (ii) mean aggregation. Output moments for the ReLU activation are provided in Wu et al. (2019). For completeness, we also provide the output moments for the ReLU activation in App. B. Let x l,m t ∈ R D x,l be the node features at layer l of node m at time step t and x l t = {x l,m t } M m=1 the set of all node features with x l t ∈ R M D x,l . For the sake of brevity, we have omitted here the index of the mixture component v. We denote mean and covariance of a graph with M nodes at layer l and time step t as For our model, we report for each predicted mode the mean, 95% confidence interval and mixture weight. We set the dimension of the latent space to D x = 3 and vary (from left to right) the number of modes V in the model from 1 to 4. For V < 3, the number of modes is set too small, and we observe mode covering behavior. For V ≥ 3, our model can recover the ground truth dynamics. If the number of components is too high (V=4), the mixture weights of redundant components are set to zero.

where

3) consists of alternating aggregation steps, in which information of all neighbors is collected, and update steps, in which the features of the node are updated. For the aggregation step, we derive the output moments for the commonly used mean aggregation operation in Sec. 4.3.3. For the update step, we assume that the neural network is built as a sequence of affine transformations and nonlinearities. The output moments of nonlinear activations are applied independently across agents. As a consequence, their rules do not change when used in the GNN setting and we can use the derivations from Wu et al. (2019). Hence it remains open to derive the output moments for affine transformations, as they are used in GNN context, which we tackle in Sec. 4.3.2. The mean aggregation operation and the node-wise affine operation used in the update step are special cases of a standard affine layer, which we review in Sec. 4.3.1.

### Standard Affine Transformation

Suppose we apply an affine transformation to node m at layer l with state x l,m t

with weight matrix W l and bias b l . The output moments are analytically tractable as

The expected Jacobian of the affine transformation reads as J l t = W l .

### Node-Wise Affine Transformation

The node-wise affine transformation applies to each node m at layer l with state x l,m t the same transformation simultaneously with weight matrix W l and bias b l . The node-wise affine transformation can be interpreted as a standard affine transformation acting on the set of all nodes x l t as

where I M is the identity matrix with shape M × M , 1 M is a vector of ones with shape M × 1, and ⊗ is the Kronecker product. The output moments of node-wise affine transformation are

Similarly, as for the standard affine transformation, the expected Jacobian of node-wise affine transformation is analytically available as J l t = Ŵ l .

### Mean Aggregation

A commonly used aggregation operation is the mean aggregator, which calculates the message x l,Nm t to node m at time step t at layer l as

Let x l,N t be the set of all messages, i.e. x l,N t = {x l,Nm t } M m=1 . The mean aggregation can be equivalently written as a linear transformation

Above, A ∈ R M ×M denotes the row normalized adjacency matrix, which summarizes the edge information E in matrix format and I D x,l denotes the identity matrix with dimensionality D x,l × D x,l . The Kronecker product expands the adjacency matrix accordingly to the D x,l -dimensional node features. Hence, the mean aggregation corresponds to a linear transformation with a weight matrix consisting of M × M blocks, where each block is a diagonal matrix of shape D x × D x . Its moments are analytically available as

The expected Jacobian is available as J l t = Â.

## Sparse Covariance Approximation

For settings with a large number of agents M or with a high-dimensional state x l,m t , the application of the BMM algorithm can become computationally expensive. In the following, we review the computational complexity of the BMM algorithm. We assume that the GNN model consists of a mean aggregation step followed by multiple node-wise affine transformations and nonlinearities, which is the same architecture that we employ later on in our experiments. The mean aggregation is done for each of the D x latent states independently, and we denote the maximum hidden layer width with H.

Computing the nonlinearities is cheap as the operation acts elementwise and their effect on the runtime can be neglected during this analysis. The other two operations (see Sec. 4.3.2 and Sec. 4.3.3) can be described by affine operations for which the weight matrices are heavily structured; the mean aggregation step corresponds to a weight matrix consisting of M × M diagonal blocks, the node-wise affine transformation to a blockdiagonal weight matrix with M blocks of shape H × H. Propagation of the full covariance matrix through a neural network (forward cost) has the computational complexity of

, where the first term is due to the cost of the H × H-dimensional node-wise affine transformations in the hidden layers, the second and third term are due to the cost of the H × D-dimensional node-wise affine transformation after the aggregation operation, and the fourth term is due to the aggregation operation.

# The computational cost of the expected Jacobian is

x ) and we give its derivation in the following. Let the expected Jacobian of the aggregation operation be E[J 1 t ] and the product of the expected Jacobians of the subsequent neural net layers E

. The expected Jacobian of the neural net layers E[J net t ] is block-diagonal with M blocks of shape D x × D x and its computation takes

results in a fully populated matrix where each entry can be computed by a single dot product, due to the structure of its factors, and its computation contributes with O(M 2 D 2

x ) to the runtime. Consequently, the total cost is dominated by the forward cost,

,when using the full covariance matrix.1 Since the computational cost quickly becomes intractable due to the cubic dependence with respect to the number of agents in the forward pass, we next propose different sparse approximations to the covariance matrix. Independent of the chosen approximation, the cost of the expected Jacobian remains unchanged, as it does not depend on the covariance matrix.

• Full: Model the full covariance matrix.

Forward cost:

• Main Diagonal: Keep the diagonal entries in the covariance blocks, which corresponds to the blue line in Fig. 3.

• Main Blocks: Keep the block-diagonal blocks in the covariance matrix, which corresponds to the orange blocks and blue lines in Fig. 3.

• All Diagonals: Structure the covariance matrix in blocks of shape M × M and keep the diagonal entries in each block, which corresponds to the blue and red lines in Fig. 3.

Note that setting the off-diagonal blocks to zero, as done in Main Blocks and Main Diagonal, corresponds to an independence assumption between the agents and leads to a runtime reduction from

Finally, it is important to note that the covariance matrix only has the same structure as the graph after the first time step. Agents that are not connected via an edge can still have a non-zero cross-covariance at time step t, provided that they are connected by a path that is at most t steps long. In our applications, this leads to non-sparse covariances after a few time steps, since the number of agents is small compared to the time horizon. We present the covariance matrix at three different time steps for an exemplary scene in Fig. 4. For a short prediction horizon of one second, the covariance matrix has an approximately diagonal shape. As the prediction horizon increases, the covariance matrix becomes more complex and is no longer dominated by its diagonal entries. We remark that we could further increase the information spread across agents by using an architecture with multiple aggregation steps within the GNN module if required.  

# Experiments

We provide experiments on two challenging autonomous driving datasets. The first experiment (Sec. 5.1) conducts an ablation study, while the second experiment (Sec. 5.2) benchmarks our model against stateof-the-art methods. We provide a runtime analysis and a benchmark of our proposed sparse covariance approximations in Sec. 5.3. In Sec. 5.4, we analyse the generalization capabilities of our model by benchmarking it on novel unseen traffic environments.

We provide details about the training procedure in App. C, and the architecture for the embedding, transition, and emission functions in App. H. Accompanying code is available under https://github.com/ boschresearch/Deterministic-Graph-Deep-State-Space-Models.

As evaluation metrics, we use the Root-Mean-Square Error (RMSE) and the predictive negative log-likelihood (NLL) at fixed time intervals (1s, 2s, 3s, 4s, 5s). For more details about the evaluation, we refer to App. D.

## rounD

The rounD dataset (Krajewski et al., 2020) consists of vehicle trajectories recorded at different roundabouts in Germany. As the roundabouts involve many interactions among vehicles, we expect the predictive distributions to be multimodal and highly complex. We use the recordings from the roundabout in Neuweiler near Aachen for training and testing purposes. The dataset consists of 13,129 tracked objects recorded at 25 Hz in 22 sessions, amounting to a total recording time of 6.6 hours. We remove pedestrians, bicycles, as well as parked vehicles from the dataset, as their influence on the vehicle behaviour patterns in the roundabouts is negligible. After dataset curation, we are left with 12,715 tracked objects. We downsample the recordings by a factor of five and construct a dataset consisting of eight-second-long segments with 50 % overlap, resulting in 5405 snippets. We use the first three seconds as the track history, which is part of the context variable I, and the following five seconds as the prediction horizon. The first 18 recording sessions, corresponding to 4,314 snippets, are used for training and validation. The final four recording sessions, corresponding to 1,091 snippets, are used for testing.

We build the connection graph by connecting vehicles with an Euclidean distance of less than 30 meters.

The dataset has been recorded with drones and we keep the original global coordinate system.

### Baselines

We compare our method with multiple baseline models. For each baseline, we remove one key assumption of our model. We cite papers that employ similar ideas as appropriate. We did not reimplement these works but performed an ablation study in which we replaced specific components of our model in the interest of a fair comparison. Furthermore, we compare different training strategies as an alternative to maximizing the PLL and analyze the multimodality of our model.

(i) Model:

(i.i) GDSSM : Our model as proposed in Sec. 4.

(i.ii) Non Recurrent GNN (e.g. Casas et al. (2020); Herman et al. (2022)): This architecture receives the context variable I, performs one round of message passing, and subsequently outputs one normal distribution for each of the next five seconds without using a recurrent architecture.

(i.iii) No Latent Noise (e.g. Sanchez-Gonzalez et al. ( 2020)): We remove the noise from the latent dynamics [Eq. ( 2)] while keeping the emission model unchanged. The uncertainty can no longer be propagated forward in time as the emission model acts independently for each time point.

(i.iv) Linearity (e.g. Li et al. (2020)): We remove all non-linearities from the latent dynamics. Note that we keep the non-linear emission model in order to map the dynamics into a latent space in which the system can be linearly approximated.

(i.v) No Interactions (e.g. Krishnan et al. ( 2017)): Our model with a diagonal adjacency matrix, i.e. we remove all edges from the graphs. This model neglects interactions between traffic participants.

(ii) Modes:

(ii.i) V Modes: We vary the number of mixture components V in the GMM prior [Eq.( 12)] in order to test the effect of multimodality.

(ii.ii) ∞ Modes: This alternative does not follow an assumed density approach, i.e. the marginal latent distribution p(x t |I) is not approximated as a GMM with a bounded number of modes. Instead p(x t |I) is approximated by simulating a large number of trajectories, where each trajectory can follow a different mode (Brandt & Santa-Clara, 2002). We set the number of particles to 100.

(iii) Objectives:

(iii.i) PLL/Det.: We train the model on the predictive log-likelihood [Eq.( 15)] and use our deterministic approximations for GDSSM as proposed in Sec. 4.2 and Sec. 4.3.

(iii.ii) PLL/MC : We train the model on the predictive log-likelihood [Eq.( 15)] and take an assumed density approach by approximating the marginal distribution [Eq.( 17)] as a GMM. The intractable integrals are solved via Monte Carlo (MC) integration. One forward pass through our model amounts approximately to the computational cost of 12 Monte Carlo simulations. For a fair comparison, we use during training 16 particles, which is more costly than training with our proposed moment propagation algorithm, and test with 100 particles. We use the same amount of particles for all MC based methods.

(iii.iii) ELBO/MC (e.g. (Krishnan et al., 2017)): The model is trained by maximizing the Evidence Lower Bound (ELBO). We give a description of this loss function in App. E. The approximate posterior is a filtering distribution that models the latent state as a normal distribution. We propagate the latent state forward in time direction via Monte Carlo sampling.

(iii.iv) MCO/MC (e.g. (Maddison et al., 2017)): The model is trained by maximizing the Monte Carlo Objective (MCO), which combines particle filters with variational inference. We give a description of this loss function in App. E. The proposal distribution is a filtering distribution and we propagate the particles in time direction via Monte Carlo sampling.

### Results

We provide benchmark results of all methods in Tab. 1. First, we compare our deterministic training and testing scheme (GDSSM PLL/Det.) against its Monte Carlo alternative (GDSSM PLL/MC). Though Monte Carlo based training is more costly than training with BMM, the Monte Carlo results are significantly outperformed by our method. Our results indicate that our deterministic approach leads to more effective approximations compared to Monte Carlo sampling despite the approximation error we obtain by our deterministic moment matching scheme. One potential explanation for our finding is that the Monte Carlo approaches suffer under a high variance since the latent space for multi-agent space grows linearly with the number of agents.

When changing the training objective from the PLL to ELBO/MC or MCO/MC, we observe that the performance is comparable to PLL/MC for the prediction horizon of 1 second. For longer prediction horizons, the performance of the models that are trained on ELBO/MC or MCO/MC degrade quicker compared to the model trained on PLL. We believe that this behavior can be explained by the mismatch between training and testing objectives. When training on MCO/MC or ELBO/MC, the model obtains feedback from the observations via the proposal distribution, while during testing it has to produce multi-step ahead predictions without receiving any feedback from the observations.

Next, we study if our method can capture multimodality by increasing the number of components in the GMM prior. It is worth noting that GMMs can approximate arbitrarily complex distributions when the number of components is chosen high enough. In our experiments, we observe that an increase of components significantly decreases the NLL, making the GMM prior a vital ingredient of our method and suggesting that the true predictive distribution is highly multi-modal. If the number of components is chosen too small, our model adjusts its uncertainty predictions accordingly. For example, we observe in Fig. 1 the uncertainty of the orange agent to increase as the vehicle is close to the exit of the roundabout. The high predictive uncertainty can be explained by two potential future outcomes: the orange vehicle can leave the roundabout or stay inside. Consequently, our model learns to compensate if the number of components is picked too low, which in turn allows us to trade accuracy for computational runtime. When using tailored implementations, one can easily scale up to a larger number of components, since their computations can be parallelized without any hurdles. We further note that the RMSE is less affected by the choice of the number of modes and stays within two standard errors. Since the RMSE value measures the error between the true value and the expected value of the predictive distribution, this result suggests that the expected value can already be modeled well by predictive distributions with very few modes (actually, one mode seems to suffice for this). We further provide the minRMSE values in App.F that decrease with increasing number of modes, indicating that the different modes correspond to a diverse set of plausible trajectories.

Next, we compare our model to a simpler alternative in which the dynamics are assumed to be linear, which allows calculating the moments of the transition model exactly and in closed form (Särkkä & Solin, 2019).

In contrast, our approach, GDSSM, approximates the non-linear dynamics in a local linear way by using deterministic moment matching results. We find that our approach achieves lower RMSE and NLL, which can most likely be attributed to the higher modeling flexibility of our proposed model class.

Our ablation study further shows that discarding latent noise and removing interactions between traffic participants results in higher RMSE and NLL. Compared to modeling the dynamics in a non-recurrent manner, our model achieves a similar RMSE and outperforms its competitor in terms of NLL.

## NGSIM

The Next Generation Simulation (NGSIM) dataset (Halkias & Colyar, 2007) consists of vehicle trajectories recorded at 10 Hz at two different highways, US-101 and I-80, in the United States. The dataset is commonly used for benchmarking traffic forecasting methods and allows us to compare our method against prior art. We adopt the experimental setup of Deo & Trivedi (2018) and use both highway scenarios. As provided in the original publication, we employ a local coordinate system that is centered around an ego-vehicle.We split the scenarios into three 15 minute long time spans resembling mild, moderate, and congested traffic conditions and downsample each trajectory by a factor of two. The test set consists of a fourth of all trajectories randomly sampled from both locations. As in the rounD experiment, we split each trajectory into eight-second-long segments, where the first three seconds are used as the track history and the following five seconds as the prediction horizon.

Similarly, as in Diehl et al. (2019); Lenz et al. (2017); Wheeler & Kochenderfer (2016), we introduce a connection graph based on the lane position of each vehicle. Each vehicle has at most six connections to other vehicles, which are the nearest vehicles in front/behind on the same/left/right lane. The vehicles on the outermost lanes have a maximum of four neighbours, as there are no neighbours to the left or right.

### Baselines

We compare our approach with the following methods:

(i) Constant Velocity (Mercat et al., 2019): This method uses a linear state-space model together with a Kalman filter in order to make predictions. It does not take interactions between agents into account.

(ii) Convolutional Social (CS)-LSTM (Deo & Trivedi, 2018): Interactions between vehicles are modeled by introducing a grid and applying a convolutional layer on top. Dynamics are modeled by a deterministic LSTM, which predicts the mean and the variance of a normal distribution at each time step.

(iv) Spatio-Temporal (ST)-LSTM (Chen et al., 2020): Interactions are modeled with a spatio-temporal graph structure, i.e. a graph with a position and time depending component. Dynamics are modeled by a deterministic LSTM that predicts the mean and the variance of a normal distribution at each time step. To the best of our knowledge, this is the only GNN based method that also reports NLL.

(iv) Multiple Futures Prediction (MFP) (Tang & Salakhutdinov, 2019): A recurrent model with deterministic transition dynamics. Stochasticity is introduced via the initial state and noisy observations that are fed back into the dynamical model. Interactions are modeled by an attention module.

### Results

We provide benchmark results of our proposed model in Tab. 2. Similar to the experiments on the rounD dataset in Sec. 5.1, we observe that (i) deterministic training and testing is more efficient than its Monte Carlo based alternative and (ii) increasing the number of modes improves the performance.

Next, we compare our method, using one component in the GMM prior only, with all other unimodal prediction methods. We can observe that our approach outperforms its competitors in terms of NLL. Furthermore, our method gives similar RMSE as other methods and is only outperformed by MFP. However, and in contrast to the other methods in the benchmark, MFP reports the best RMSE over 5 Monte Carlo samples, which makes it difficult to draw a fair conclusion.

We subsequently increase the number of modes for our model and for MFP. In terms of NLL, our method achieves superior results when it comes to long-term predictions (3s, 4s, 5s), while MFP performs better for short-term predictions (1s, 2s). Accurate long-term prediction of the agents in a driving scene is crucial for high-level autonomous driving, as an accurate environment model is a prerequisite for precise planning of driving controls. For instance, advanced driver-assistance systems usually use time horizons between 3s and 5s for driver warnings and emergency brakes, while autonomous cars aim for a time horizon for 5s or longer in order to ensure safe and comfortable rides (Philipp & Goehring, 2019). We provide minRMSE values for different number of modes as a measure of predictive diversity in App. F. 

## Covariance Approximations

We provide a detailed runtime analysis for different covariance approximations in Sec. 5.3.1 and study their impact on the predictive performance in Sec. 5.3.2.

### Runtime

We visualize the runtime of different covariance approximations, as well as the runtime of the Monte Carlo alternative in Fig. 5 as a function of input dimensionality and number of agents. We use the same NSDE architecture as in our experiments on the rounD and NGSIM dataset. For the Monte Carlo alternative, we visualize the runtime for 16 particles, as we use the same number of particles for training in Sec. 5.1 and 5.2.

We first confirm that propagation of the full covariance matrix is more costly than any of the proposed approximations. In fact, our sparse covariance approximations can reduce the runtime up to a factor of 100 for systems with a large number of agents and a high input dimensionality. As we derived in Sec. 4.4, when using the BMM algorithm with a full covariance matrix or the all diagonals approximation, the computational cost shows a cubic dependence on the number of agents. In contrast, the main diagonal approximation, the main blocks approximation, as well as MC based predictions have a quadratic dependence on the number of agents. This makes these two approximations an attractive alternative to MC based predictions, when systems with a high number of agents need to be modeled with a limited computational budget.

For systems with a moderate input dimensionality (≈ 8) and number of agents (≈ 16), all of our proposed approximations require only up to 5 ms in order to compute the distribution at the next time point, which corresponds to the cost of 5-10 Monte Carlo simulations.

### Benchmark

Next, we study the effect of different covariance approximations on the performance. We report the results for the case of a unimodal GDSSM. The results are depicted in Tab. 3. We report here our main findings.

First, modeling the full covariance matrix results in the best performance in terms of lowest RMSE and NLL.

Second, the all diagonals covariance approximation performs the best among the covariance approximations. It achieves comparable RMSE as the full solution, but falls slightly behind in NLL when the system is highly interactive (see rounD dataset). In this setting, it outperforms the other two sparse approximations with respect to NLL. This behavior might be explained by the assumptions made in the covariance approximation: it is the only approximation that allows for correlations between agents as its structure only neglects dependencies between latent features.

Third, the differences in performances between the full solution and the different approximations with respect to RMSE lie between one and two standard errors. Modeling the main diagonal only can thus be sufficient Figure 5: Wallclock time for output moment calculation for the latent dynamics using GNNs with three hidden layers of size 24 for different covariance approximations (from left to right). For each approximation, we plot the runtime as a function of the input dimensionality D x and number of agents M . The GNNs are initialized at random and we report the average runtime over 100 repetitions.

for applications with low computational resources and a high demand for accuracy by accepting a slight loss in calibration. For these applications, the runtime can be reduced from O(M 3 ) to O(M 2 ). 

## Out-of-Distribution Testing

We analyze the generalization capabilities of our model by testing it on out-of-distribution data, e.g. traffic environments that have not been observed during training.

For this experiment, we reuse the rounD dataset (Krajewski et al., 2020) since it consists of recordings at three different roundabouts. Here, each roundabout corresponds to a separate traffic environment. We select one recording from each roundabout (Kackerstraße in Aachen, Thiergarten in Alsdorf and Neuweiler near Aachen) and apply the same data curation steps as in Sec. 5.1. In order to generalize between different traffic environements, we change the experimental setup as follows:

• Local coordinate system: We transform the data into a local coordinate system, which is centered at the ego-vehicle and is oriented to the heading direction of the ego-vehicle.

• Include map information to the context variable I. We extract a local map around the egovehicle, which spans a rectangle with a length of 74 meters and a width of 44 meters. Afterwards, we on the required calibration, our approximations can lead to a significant reduction of the runtime without impeding accuracy.

In future work, we seek to increase the robustness of our proposed model towards novel and unseen traffic scenarios. One way could be to incorporate epistemic uncertainty into our model formulation by placing a prior over the weights of the GNN. To achieve this, we could combine our model with recent advances in variational inference in order to find an approximation to the intractable weight posterior. Another research direction of interest is modeling of irregular and partially observed dynamical systems. Prior work uses continuous time encoder networks as well as a continuous time transition model in latent space (Rubanova et al., 2019;Brouwer et al., 2019). Following this vein of work, an extension of our model towards continuous time networks seems a promising direction for modeling interactive systems.

# A Proof of Theorem 1

Theorem 1. The marginal distribution p(y t |I) is analytically computed as

for a GDSSM with the below generative model 

The moments at time step t of a linear time-depending dynamical system are available as (Särkkä, 2013)

We obtain the same expression via the BMM algorithm, which is easy to prove by inserting the locally linear system into Eq. 6. Finally, mean a t,v (I) and covariance B t,v (I) of the output at time step t are available as (Särkkä, 2013)

# B Output Moments for the ReLU Activation Function

Suppose, we apply the ReLU activation function at layer l and time step t to the input x l t x l+1 t = max(0, x l t ).

# Output Moments

We can approximate the output moments of x l+1 t as a function of the input moments (Wu et al.,   Expected Jacobian Since activation functions are applied element-wise, off-diagonal entries of the expected gradient are zero. The diagonal of the Jacobian of the ReLU function is the expected Heaviside step function Wu et al. (2019) diag E ∇ x l t max(0,

For a more detailed derivation, we refer to the work of Wu et al. (2019).

# C Training Details

We train all models with the ADAM optimizer and stochastic mini-batches. We use a batch size of 4 and a learning rate of 0.0001. In order to accelerate training of multi-modal GDSSMs we initialize the transition and observation neural nets with the pretrained versions of the uni-modal GDSSMs.

# C.1 rounD

We train deterministic models (GDSSM Det. and Non Recur. GNN) for 50k weight updates. For the MC based models (GDSSM MC) we use 100k weight updates. The dataset contains 4,314 training and 1,091 testing snippets. We do not use a separate validation dataset as we observed no overfitting. 

# G.1 Dataset Construction

We construct a dataset, which consists of three different traffic environments. We select one recording from the roundabout in Kackertstraße (K) in Aachen, one recording from the roundabout in Thiergarten (T) in Alsdorf, and one recording from the roundabout in Neuweiler (N) near Aachen. We use the same preprocessing procedure as in Sec. 5.1. We remove pedestrians, bicycles, and parked vehicles from each traffic environment. There remain 319/ 264/ 389 tracked objects over a time span of 0.3/ 0.3/ 0.15 hours at the traffic environments K/ T/ N. We downsample the recordings by a factor of 5 and then construct for each traffic environment a dataset which consists of 8 s long snippets with 50% overlap. The first three seconds are used as the track history and the following five seconds as the prediction horizon. We obtain 254/ 251/ 137 snippets for the traffic environments K/ T/ N. For each traffic environment we use the first 80% snippets for training and the remaining 20% snippets for testing.

# G.2 Map Processing

The map processing follows existing work in the domain of traffic forecasting Bansal et al. (2018); Herman et al. (2022). Given an ego-vehicle and its history, we first calculate the heading of the vehicle. The heading is calculated as the average heading direction over the last 0.2 observed seconds. The position and the heading direction jointly define the Region-of-Interest (ROI) on the map. The ROI is a rectangle with a length of 74 meters and a width of 44 meters, which is centered at the ego-vehicle and oriented according to the heading of the ego-vehicle. We further convert the RGB-image into a binary road image. We visualize the processed map information in Fig. 7b Ego Vehicle Heading Relevant Map Information  in Sec. 5.1 for the baselines that are trained on the ELBO or MCO. In contrast maximizing the PLL does not necessitate an approximate posterior. The approximate posterior network takes the previous state and the current observation in order to approximate the latent distribution at the current time step.

# H.2 Network Architectures with Map Information

These neural net architectures have been used in our experiments in Sec. 5.4. It closely follows the architectures in Sec. H.1. We add an additional neural net, which encodes the masked map of size 500x300 into a flattened 256-dimensional vector. This map embedding is used as an additional input to the embedding function. For fully connected layers we give the number of output neurons. For convolutional layers we give the number of input channels and output channels. We use a kernel size of 3 and stride 2. For MaxPool layers we use a kernel size of 2 and stride 2.

# State

## Results

Next, we analyze the generalization capabilities of our model by comparing the following strategies: (1) training on two traffic environments and testing on a third distinct traffic environment, (2) directly training the model on the test traffic environment and (3) training on all traffic environments. In order to enable a fair comparison, the data for each traffic environment is split into non-overlapping training and test sets.

We present the results for different traffic environments in Tab. 4. The first column in Tab. 4 describes the RMSE and NLL when we train our model on the traffic environments Thiergarten (T) and Neuweiler (N) and test it on the traffic environment Kackertstraße (K). The second column describes the predictive performance by using scenes from the same traffic environment (K) for training and testing. The third column describes the predictive performance by training on all three traffic environments (KNT) and testing on the traffic environment K. The remaining columns benchmark the generalization capabilities of our model on the traffic environments T and N and are set up in an analogous fashion.

In all experiments, we observe that the performance increases from (1) using different training environments for training and testing, to (2) using the same environment for training and testing and (3) using all environments for training. The difference in performance between (1) and ( 2) is moderate for the locations K and T demonstrating that our model is capable of generalizing to unseen traffic environments during testing. For location N, the performance difference is increased which can be explained by studying the locations in more detail: N is a multi-lane roundabout with congested traffic, the roundabouts K and T are single-lane with moderate traffic. In consequence, the out-of-domain test on the traffic environment N is more challenging. We visualize exemplary predictions of our model GDSSM in Fig. 6.

Table 4: Test performance on different traffic environments on the rounD dataset using our method GDSSM (1 mode). We vary for each test traffic environment the training traffic environments. We provide averages and standard errors over 10 runs. Kackertstraße=K, Thiergarten=T, Neuweiler=N. 

# Conclusion

In this work, we have proposed GDSSMs in which the latent dynamics of the agents are coupled via GNNs in order to capture interactions among multiple agents. We derived moment matching rules for GNN layers that allow for deterministic inference and introduced a GMM prior over the initial latent states in order to allow for multimodal predictions. Both together lead to an efficient and stable algorithm that is able to produce complex and nonlinear predictive distributions. We confirmed that our novel method shows strong empirical performance on two challenging autonomous driving datasets. Finally, we proposed sparse approximations to the covariance matrix considering the computational limits of real-world vehicle control units. Depending

# C.2 NGSIM

We train all models for 1000k updates on the NGSIM dataset. The dataset contains 5,922k/860k/1,505k train/validation/test snippets. We validate the models on 1k random minibatches from the validation dataset after every 10k weight updates.

# C.3 Out-of-Distribution Testing

We train all models for 50k weight updates. The dataset consists of three sub-datasets with 254/ 251/ 137 snippets, where 80% of each sub-dataset are used for training and the remaining 20% for testing. Due to the small size of the sub-datasets we observed overfitting. We address this by using the last 20% of each training sub-dataset for validation. We validate the model after every 1k weight updates.

# D Evaluation Metrics

In the following, we give a brief overview on different evaluation metrics. We provide the negative loglikelihood (NLL) and the Root-Mean-Square Error (RMSE) in the main of the paper, and minRMSE in App. F.

# Root-Mean-Square Error

The (root) mean-square error at time point t is defined as

where N is the number of snippets in the dataset, M (n) is the number of agents in the n-th snippet, y m t,n is the true location of the m-th agent at time point t of the n-th snippet, and ŷm t,n the corresponding predicted location. Unfortunately, it is not straight-forward to extend RMSE base to probabilistic forecasts. To the best of our knowledge, none of the existing variants is a strictly proper scoring rule (Gneiting & Raftery, 2007) where the latter is optimal if and only if the predictive distribution matches the true distribution. An example of a strictly proper scoring rule that we also provide in the paper is the predictive NLL:

For deterministic GDSSMs, we approximate p(y m t,n |I) directly with our method that we introduced in Sec. 4.2. For GDSSMs that do not follow an assumed density approach, we approximate p(y m t,n |I) via Monte Carlo integration. In the following, we discuss different RMSE variants in more detail.

# Bayes Predictor:

A common evaluation metric used in the ML community (e.g. Gal & Ghahramani (2016)) is to compute

where we assume that the probabilistic predictor will perform model averaging before making its final prediction. This score only evaluates the goodness of the first moment and does not take any information of higher moments into account. We provide its values in the main part of the paper.

Gibbs Predictor: An alternative way for extending deterministic loss functions to the probabilistic scenario can be found in the PAC-Bayes setting (e.g. Germain et al. (2016)) by considering the average loss in the risk function. In our case, this would lead to

where we take expectation with respect to the predictions ŷm t,n . However, we discourage to take this formulation as evaluation metric since it penalizes any form of variance in the predictor and favors a Dirac distribution around the expected value of the true distribution. Note that this result can be tightly linked to the bias-variance trade-off in statistical learning theory (e.g. Hastie et al. (2009)).

Min Predictor: A popular alternative in the traffic forecasting literature (e.g. Tang & Salakhutdinov (2019)) is to compute the minimal error over a set of S potential predictions

where (ŷ m t,n,s ) S s=1 is the set of S potential predictions. This score favors models that produce a set of diverse predictions where at least one candidate is close to the true outcome but ignores the goodness of the remaining S -1 predictors. While it gives some useful information about the model capacity, it does not give a complete representation of the test-time performance when the best mode is unknown. We provide its values in App. F.

# E Alternative Parameter Inference Methods

One commonly used inference method in the context of machine learning circumvents maximizing the loglikelihood and instead maximizes the Evidence Lower Bound (ELBO) ELBO(y 1 , . . . , y T |I) = E q(x0,...,x T ) log p(y 1 , . . . , y T , x 0 , . . . , x T |I) q(x 0 , . . . , x T ) , (

that involves learning an approximation q(x 0 , . . . , x T ) to the intractable smoothing distribution p(x 0 , . . . , x T |y 1 , . . . , y T , I) (Krishnan et al., 2017).

A tighter bound to the log-likelihood log p(y 1 , . . . , y T |I) can be obtained by calculating the importance weighted log-likelihood, which we refer to as the Monte Carlo Objective (MCO) (Maddison et al., 2017;Burda et al., 2016)

where K is the number of Monte Carlo samples and x t,k is the k-th sample at time step t. For state-space models, recent work combined the MCO with particle filters (Naesseth et al., 2018;Maddison et al., 2017;Le et al., 2018).

# F Extended Results

We provide minRMSE values for the rounD and NGSIM dataset. We set the proposal predictions to the mean values of each mode and the min operator selects for each agent the proposal that produces the lowest error per snippet over the complete prediction horizon. This score favors models in which the proposal predictions are diverse as long as at least one candidate is close to the true outcome.

As shown in Tab. 5, the minRMSE decreases as we increase the number of modes, which indicates that the different modes correspond to a diverse set of plausible trajectories.  The embedding function receives the history of all M agents. This history is 3 seconds long with a time step of 0.2 seconds and consists of two dimensional coordinates. After flattening, the input is a vector of size 30. The output of the embedding function is a GMM with V mixture components. We use the mean aggregator in the embedding, mean and variance update function. The mean aggregator calculates the message to agent m accordingly to Eq. 22. After the message x Nm t is calculated, it is concatenated with the state x m t . Mean and variance update functions are neural networks, which conduct at each prediction step one round of message passing and then calculate the output. Our emissions model uses a neural network for the mean function g(x t ) and a constant vector for Q(x t ). The emission model maps the state of each agent back to the observed space and does not depend on interactions. The approximate posterior is used

