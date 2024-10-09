# Introduction

Reinforcement learning (RL), especially with high-capacity models such as deep nets, has shown its power in many domains, e.g., gaming, healthcare, and robotics. However, typical training schemes of RL algorithms rely on active interaction with the environments. It limits their applications in domains where active data collection is expensive or dangerous (e.g., autonomous driving). Recently, offline reinforcement learning (offline RL) has emerged as a promising candidate to overcome this barrier. Different from traditional RL methods, offline-RL learns the policy from a static offline dataset collected without iterative interaction with the environment. Recent works have shown its ability in solving various policy learning tasks [1,2,3]. However, offline RL methods suffer from several major problems. One of them is distributional shift. Unlike online RL algorithms, the state and action distributions are different during training and testing. As a result, RL agents may fail dramatically after deployed online. For example, in safety-critical applications such as autonomous driving, overconfident and catastrophic extrapolations may occur in out-of-distribution (OOD) scenes [4].

Many prior works [5,6,7,8,9,10] try to mitigate this problem by handling OOD actions. They discourage the policies to visit OOD actions by designing conservative value functions, or estimating the uncertainty of Q-functions. Although constraining the policy can implicitly mitigate the problem of state distributional shift, few works have adopted measures to explicitly handle OOD states during the training stage. In this work, we propose the Pessimistic Offline Reinforcement Learning (PessORL) framework to explicitly limit the policy from visiting both unseen states and actions. We refer to the states or the actions that are not included in the training data as the unseen states or the unseen actions.

Our PessORL framework is inspired by the concept of pessimistic MDP in [11], where the reward is significantly small for unseen state-action pairs. We aim to limit the magnitude of the value function at unseen states, so that the agent can avoid or recover from unseen states. It is then crucial to precisely detect OOD states and shape the value function at those states. Since prior methods on OOD actions are derived from a similar concept, we can adapt their approaches to handle OOD states. There are 5th Conference on Robot Learning (CoRL 2021), London, UK. arXiv:2111.05440v1 [cs.LG] 9 Nov 2021 mainly two approaches in the literature. One is to estimate the epistemic uncertainty of Q-function and subtract it from the original Q-function to get a conservative Q-function [6,7,8,9,10]. The other is to regularize the Q-function during the learning process [5]. The first method is highly sensitive to the trade-off between the uncertainty estimation and the original Q-function [12,13] and the quality of uncertainty estimation [14].

Therefore, we follow the second approach, and add a conservative regularization term to the policy evaluation step of PessORL to shape the value function. We prove that PessORL learns a pessimistic value function that lower bounds the true value function, and forces the policy to avoid or recover from out-of-distribution states and actions. We evaluate the PessORL algorithm on various benchmark tasks. The performance of our method matches the state-of-the-art offline RL methods. In particular, we show that, by explicitly handling OOD states, we can further improve the policy performance compared to those methods merely considering OOD actions.

# Related Works

A big challenge for offline reinforcement learning methods is to deal with the problems caused by unvisited states or actions in training data, which is also known as distributional shift. In model-free offline reinforcement learning, some works used importance sampling to fill the gap between the learned policy and the behavior policy in the training dataset [15,16,17,18,19]. There are also many works constrained the learned policy to be similar to the behavior policy by explicit constraints in the training dataset [6,20,21,22,23], so that the agent can avoid out-of-distribution actions during test time. The work in [13] proposed a latent space to constrain the policy to avoid deviating from the training data support. One further step to make the agent avoid actions that may cause itself deviate from the training data support is to get a conservative value function and thus a conservative policy. The works in [7,8,6,9,10] estimate the uncertainty of the learned Q-function, and then directly subtract it from the Q-function to get a conservative Q-function. Another way to get a conservative Q-function is to regularize the Q-function in the optimization problem during the learning process [5]. In model-based reinforcement learning (MBRL), there are also many algorithms that constrain the exploitation in the environment with effective uncertainty estimation methods [24,25,26,27,28,11]. It is considered to be mature and reliable to detect OOD actions and states by methods from MBRL. Most of the aforementioned methods focus on OOD actions but not have explicit mechanism to deal with OOD states. In this paper, we focus on OOD states and propose a method to learn a pessimistic value function by adding regularization terms when updating Q-functions, and follow the works in the MBRL domain to establish the module to detect OOD states in our algorithm.

# Background

## Offline Reinforcement Learning

Given a Markov decision process (MDP), an RL agent aims to maximize the expectation of cumulative rewards. The MDP is represented by a tuple M = (S, A, P, r, γ), where S is the state space, A is the action space, P : S × A × S → [0, 1] is the transition function, r : S × A → R is the reward function, and γ is the discount factor. Typical RL algorithms optimize the policy using experience collected when interacting with the environment. Unlike those online learning paradigms, offline-RL algorithms rely solely on a static offline dataset, denoted by

In this work, we focus on dynamic-programming-based RL algorithms under the offline setting, where we extract a policy from a learned value function for the underlying MDP in the training data. Standard Q-learning method estimates an approximate Q-function parametrized by θ, i.e. Qθ (s t , a t ).

In each iteration, the Q-function is updated as follows:

where Bπ is the empirical Bellman update operator defined as:

For discrete action space, we define πk as the optimal policy induced by the learned Q-function, i.e. πk (a|s) = δ a = arg max a Qk θ (s, a) . In this case, Bπ collides into the Bellman optimality operator. When the action space is continuous, we follow actor-critic algorithms to approximate the optimal policy by executing a policy improvement step after policy evaluation in each iteration:

In the rest of the paper, we denote 

where Unc is defined to be some uncertainty estimation metric, and P D (Q) is the distribution over possible Q-functions. Because the uncertainty metric is directly subtracted, uncertainty-based methods is highly sensitive to the quality of uncertainty estimation. Meanwhile, it is difficult to find an ideal α to balance the original Q-function and Unc.

Another way is to regularize the Q-function at the step of policy evaluation. A representative example is Conservative Q-Learning (CQL) [5]. Assuming that the dataset D is collected with a behavior policy π β (a|s), and πk (a|s) is the learned policy at iteration k, the policy evaluation step in CQL becomes:

In the rest of the paper, we denote C(Q) as the cost term adopted from the CQL, i.e.,

It is worth noting that the aforementioned methods all focus on OOD actions, but they do not have an explicit mechanism to deal with OOD states, which motivates us to develop the PessORL framework in this work.

# Pessimistic Offline Reinforcement Learning Framework

In this section, we introduce the PessORL framework to mitigate the issue of state distributional shift.

In particular, we propose a novel conservative regularization term in the policy evaluation step. It can then be integrated into Q-learning or actor-critic algorithm, which will be described in Sec. 5.

## How To Deal With OOD States

Assuming the dataset D is collected with a behavior policy π β (a|s), and the states s are distributed according to a distribution d π β (s) in the dataset, we propose to solve the problem caused by state distributional shift by augmenting the policy evaluation step in CQL [5] with a regularization term scaled by a trade-off factor ε:

where d φ (s) is a particular state distribution of our choice.

The idea is to use the minimization term ε E s∼d φ (s),a∼π k (a|s) [Q(s, a)] to penalize high values at unseen states in the dataset, and the maximization term ε E s∼d π β (s),a∼π k (a|s) [Q(s, a)] to cancel the penalization at in-distribution states. The regularized Q-function could then push the agent towards regions close to the states from the dataset, where the values are higher. To achieve it, we need to find a distribution d φ (s) that assigns high probabilities to states far away from the dataset, and low probabilities to states near the training dataset. We will instantiate a practical design of d φ (s) in Sec. 5. For now, we just assume d φ (s) assigns high probabilities to OOD states.

## Theoretical Analysis

In this section, we analyze the theoretical properties of the proposed policy evaluation step. The proof and more details can be found in Appendix A.

We define k ∈ N as the iteration of policy evaluation, i.e. Qk denotes the optimized Q-function in the k-th iteration obtained by PessORL. Q π is defined to be the true Q-function under a policy π(a|s) in the underlying MDP without any regularization. The true Q-function can be written in a recursive form via the exact Bellman operator, B π , as

We define V k as the value function under a policy π(a|s), V k (s) = E a∼π(a|s) [ Qk (s, a)]. For the true value function V π in the underlying MDP, we also have

We first introduce the theorem that the learned value function is a lower bound of the true one without considering the sampling error defined in the Lemma A.1.

Theorem 4.1 Assume we can obtain the exact reward function r(s, a) and the transition function

Then ∀s ∈ S, the learned value function via Eqn. 5 is a lower bound of the true one, i.e., V π (s)

.

It is worth noting that the learned value function still lower bounds the true value function for any state and action in the training datasets, i.e. s, a ∈ D, even when we consider the sampling error defined in the Lemma A.1. Further details are shown in Corollary A.1. We have no reward or transition pair collected at unseen states or actions outside the training dataset, so it is impossible to bound the error outside the training dataset when consider the sampling error introduced by the reward function and the transition function.

We can now step further and show that the values at OOD states are lower than those at in-distribution states based on the learned value function. The proof can be found in Appendix A.3.

Theorem 4.2 For any state s ∈ S, if ε > 0 is sufficiently large, then the expectation of the learned value function via Eqn. 5 under the state marginal d π β (s) in the training data is higher than that under d φ (s), i.e.,

During training time, we can at least evaluate Q-values of OOD actions based on in-distribution states. However, there is actually no information about immediate rewards at OOD states, thus no information about Q-values. Intuitively, under offline settings, the best we can do to mitigate the problem of OOD states is to suppress values at these OOD states, and raising values at in-distribution states, so that the agent can be attracted to the area where it is familiar near the training data. Thm. 4.2 indeed tells us PessORL models a value function that assigns smaller values to OOD states compared to those at in-distribution states. Optimizing a policy under such a value function is similar to forcing the policy to avoid unknown states and actions.

In summary, PessORL can learn a pessimistic value function that lower bounds the true value function. Furthermore, this value function assigns smaller values to OOD states compared to those at in-distribution states, which helps the agent avoid or even recover from OOD states.

# Implementing the Algorithm

In this section, we introduce a practical PessORL algorithm based on Eqn. 5. This algorithm simply modifies the policy evaluation step of Deep Q-Learning or Soft Actor-Critic algorithms, which is easy to implement.

## Detecting OOD states

In prior to designing the algorithm, we need to choose a proper d φ (s), which requires a tool for OOD state detection. Following [11,14,29], we use bootstrapping to detect OOD states. In particular, we train a bag of Gaussian dynamics models [29] { P1 , P2 , . . . , Pn } where each model is Pi (•|s, a) = N (s + fφi (s, a), Σφi ). The function fφi outputs the mean difference between the next state and the current state, and Σ φi models the standard deviation. OOD states are detected by estimating the uncertainty of bootstrap models at a given state s ∈ S. Concretely, we define

, where fφ (s, a) = 1 n n i=1 fφi (s, a) is the mean of outputs of all fφi , and the actions are drawn from a policy distribution π. A high u π (s) value indicates the state is more likely to be an unseen state. Given a set of sampled states {s 1 , s 2 , . . . , s n }, we can define a discrete distribution over it using u π (s):

, i = 1, 2, ..., n, which assign high probabilities to OOD states. In the following section, we will use it to construct the distribution d φ (s).

## Practical Implementation of PessORL

We now introduce a practical PessORL algorithm. In practice, to obtain a well-defined distribution d φ , we add an additional optimization problem over d φ into the original optimization problem. The resulting optimization problem for the policy evaluation step is:

where R(d φ ) is a regularization term inspired by [5] in order to stabilize the training. If we choose

, where ζ(s) is the distribution we obtained from uncertainty estimations, then   Update π ϕ according to the soft actor critic style objective and learning rate ϕ :

Eqn. 6, we obtain the following PessORL policy evaluation step:

The first term in Eqn. 7 is very similar to weighted softmax values over the state space. It penalizes the softmax value over the state space, but also considers the distances between sample points and the training data. The two terms following the trade-off factor ε is actually trying to decrease the discrepancy between the softmax value over OOD states and the average value over in-distribution states. Intuitively, it should enforce the learned value function to output higher values at in-distribution states, and lower values at out-of-distribution states. The logsumexp term in Eqn. 7 also mitigates the requirement for an accurate uncertainty estimation ζ(s) over the entire state space. Only those states with high values contribute to the regularization.

The complete algorithm is shown in Algorithm 1. We include the version for continuous action space which requires a policy network here, and note that if the action space is discrete, then we no longer need a policy network but just an implicit policy based on the learned Q-function. We implement PessORL on top of CQL [5], with its default hyperparameters. We also apply Lagrangian dual gradient descent to automatically adjust the trade-off factor ε. During the training process of offline reinforcement learning algorithms such as CQL and PessORL, we only have access to the dataset D instead of d π β (s) and π β (a|s). Therefore, we follow the convention in reinforcement learning community and approximated all expectations by Monte Carlo estimation in Eqn. 7.

# Experiments

We compare our algorithm to prior offline algorithms: two state-of-the-art offline RL algorithms BEAR [6] and CQL [5]; two baselines adapted directly from online algorithms, actor-critic algorithm TD3 [30] and DDQN [31]; and behavior cloning (BC). The TD3 baseline is applied when the action space is continuous, whereas DDQN is trained when the action space is discrete. We evaluate each algorithm on a wide range of task domains, including tasks with both continuous and discrete state and action space. All baselines are run with the default code and hyperparameters from the original repositories. In particular, we are interested in the comparison between our algorithm with CQL, because we essentially add an additional state regularization term to the original CQL framework.

## Performance on Various Environments

Pointmass Mazes. The task for the agent in this domain is to learn from expert demonstrations to navigate from a random start to a fixed goal. The expert dataset, which contains around 1000 trajectories all from the same start point to the same goal, is collected by online trained RL policy. During the test time of offline RL algorithms, we reset the start to a random point in the state space and the goal to the same fixed point as the dataset. In this way, the performance of the agent at unseen states are evaluated.

Before showing the performance, we first check if the OOD states detection is accurate, and hence, if we can successfully penalize high values at unseen states in training datasets. We evaluate the effectiveness of the OOD states detection method based on the accuracy of uncertainty estimation in the environment Pointmass. Figure 1(b) and(c) are visualizations of the training datasets and estimated uncertainty u π (s), both of which have the coordinate systems the same as that in the map (figure 1(a)). We use different colors in figure 1(b) and (c) to represent different values at each point in the map. The uncertainty estimations tend to be high (yellow areas in Fig. 1(c)) in area where the state density is low (blue areas in Fig 1(b)), and vice versa. This trend empirically shows that our uncertainty estimations are reasonable. We can trust them to detect OOD states when training offline RL algorithms. We include the learning curves in figure 1(d), in which we evaluate each algorithm based on 3 random seeds, and report the average return. The shaded area represents the standard deviation of each evaluation. As we can see in the figures, PessORL outperforms other baselines in both hard and super hard environments. PessORL benefits from the augmented policy evaluation step in Eqn. 7. The learned value function produces high values at areas that have low uncertainty estimations, and low values at highly uncertain areas (OOD states). Therefore, the agent can be "attracted" to the high value areas from low value and unfamiliar areas.

Gym Tasks. In this domain, we focus on the locomotion environments from MuJoCo, including Walker2d-v2, Hopper-v2, Halfcheetah-v2, and Ant-v2. Unlike Pointmass environment, we directly adopt the d4rl datasets [32] as our training data in the gym domains. We include four different types of datasets in our experiments, namely, "medium", "medium-expert", "random", and "expert". The "medium", "random", and "expert" dataset are all collected by a single policy, which is an either early-stopping trained, or randomly initialized, or fully trained expert policy. The "medium-expert" dataset is generated by mixing mediocre and expert quality data. We show the normalized scores averaged over 4 random seeds for all methods on gym domain in table 1. We directly ran all baselines from their original repositories with their default parameters, and we only report the average scores we actually obtained. As we can see in the table, PessORL outperforms all other offline RL methods on a majority of tasks on gym domains. PessORL works especially well with mediocre quality datasets according to the results. In fact, it is one of the advantages of offline RL methods over behavior cloning on medium quality datasets, because offline RL methods take advantage of the information both from the reward and the underlying state and action distributions in training datasets, instead of simply imitating behavior policies as behavior cloning. Medium quality datasets are also considered to be similar to real-world datasets. Therefore, it is important for an offline RL method to perform well in medium quality datasets. We also note that PessORL shares some good properties with CQL, such as satisfying performance on mixed quality datasets. PessORL and CQL both outperform other offline methods on medium-expert datasets with PessORL better between them. The reason is that offline RL methods can "stitch" [32] different trajectories from different policies together according to the information from the reward.

Adroit Tasks The adroit domain [33] provides more challenging tasks than the Pointmass environment and the gym domain. The tasks include controlling a 24-DoF simulated Shadow Hand robot to twirl a pen, open a door, hammer a nail, and relocate a ball. Similar to the datasets in the gym domain, we also directly use the d4rl datasets as the training datasets in our experiments. The performance of PessORL and all baselines is shown in table 1. The normalized scores of all methods are average returns on 5 random seeds. We note that PessORL has better performance than other baselines on adroit domains. It is a great advantage for PessORL to learn useful skills from human demonstrations on these high dimensional and highly realistic robotic simulations. The main contribution of this work is to explicitly limit the values at OOD states, so that the learned policy can act conservatively at OOD states and drives the agent back to the familiar areas near the training data. We are interested to see if our framework can indeed induce a different behavior on OOD states. We use ∆ k = max s∈S [V (s)] -E s∼D [V (s)] as a metric to evaluate it at each iteration. If ∆ k is close to zero, then intuitively it indicates the values at OOD states are lower than those at indistribution states. In Fig. 2, we plot ∆ k at each iteration in hopper-medium-v0. As is shown in the figure, PessORL successfully limits ∆ k to be non-positive, which meets our goal in this work and aligns with the statement in theorem 4.2.

## Discussions and Limitations

On the gym domain, we notice that the performance of PessORL and CQL on datasets containing expert trajectories is not satisfying, often not as good as BC. We believe it is because of overly conservative value estimation. In fact, it is widely believed that conservative methods suffer from underestimation [14]. The conservative objective function in Eqn. 7 sometimes assign values that are too low to OOD states and actions. Besides, the uncertainty estimation method cannot be guaranteed to be precise on high-dimensional spaces. It is actually a possible future work direction to solve the underestimation and uncertainty estimation problems in conservative methods.

# Conclusion

We propose a Pessimistic Offline Reinforcement Learning framework to deal with out-of-distribution states. In particular, we add a regularization term in policy evaluation step to shape value function, so that we can improve its extrapolation to OOD states. We also provide theoretical guarantees that the learned pessimistic value function lower bounds the true one and assigns smaller values to OOD states compared to those at in-distribution states. We evaluate the PessORL algorithm on various benchmark tasks, where we show that our method gains better performance by explicitly handling OOD states compared to those methods merely considering OOD actions.

# Appendix A Proof of Theorem

In this section, we provide the proofs of the theorems in this paper.

Remark. We provide the proofs under a tabular setting. Most continuous space can be approximately discretized to a tabular form, although the cordiality of the tabular form may be large. We define P π as the tabular transition probabilities under the policy π.

A.1 Proof of Theorem 4.1

In Eqn. 5, The Q-function update can be computed in a tabular setting, by setting the derivative of the augmented objective in Eqn. 5 with respect to Q to zero,

Therefore, we can obtain Qk+1 in terms of Qk by rearranging the terms,

for all s ∈ S, a ∈ A and k ∈ [0, +∞). For the state-action pair (s, a) such that d φ (s) < d π β (s) and π(a|s) < π β (a|s), the last two terms of Eqn. 8, -ε

is positive, so that we cannot simply lower bound the true Q-function Q k+1 (s, a) by the estimated one Qk+1 (s, a) point-wise. However, we can prove that the value function, which is the expectation of the Q-function, can be lower bounded. Taking the expectation of both sides of Eqn. 8 under the distribution a ∼ π(a|s), we have

The first goal is to prove that V k+1 ≤ B π V k which implies that each iteration introduces some underestimation, and V k could eventually converge to a fixed point. Therefore, we need to prove the last two terms on the right hand side of Eqn. 9 is negative. We denote ∆ to be the opposite of the last two terms on the right hand side of Eqn. 9, then

From the proof in [1], we know that the second term in Eqn. 10 is non-negative when α > 0, that is

Hence, when

then we have ∆ ≥ 0.

In summary, we have ∆ ≥ 0 when Eqn. 12 holds. Since the exact Bellman update operator B π is a contraction [4], we have

which implies that each value-function update V k+1 = B π V k -∆ is a contraction. According to the contraction mapping theorem, the recursive update in Eqn. 9 will always lead value function to converge to a fixed point V π . Now that V π = B π V π for the true value functions, by subtracting them from both side of Eqn. 9 and substitute V k+1 and V k with the fixed point V π , we have

when ε satisfies

In Eqn. 13, we stretch all notations to be vectors, which means V π ∈ |S| , V π ∈ |S| , and

∈ |S| are all vectors containing values for all states. Here, 1 denotes the vector in which the entries are all 1. The expectations and the operations inside

are all computed in a point-wise manner.

Therefore, we can conclude from Eqn. 13 that the estimated value function V π (s) is a lower bound of the true value-function V π (s) without considering any sampling error. Thus, we finish the proof of Thm. 4.1.

# A.2 Value Lower Bound in Existence of Sampling Errors

We now take sampling error into account. First, we introduce a lemma from [1]:

Lemma A.1 If with high probability δ the reward function r(s, a) and the transition function T (s |s, a) can be estimated with bounded error, then the sampling error of the empirical Bellman operator is also bounded:

where C r,T,δ is a constant related to r, T , and δ, and R max is the maximum possible reward in the environment.

Note that the bound of the error Bπ V (s) -B π V (s) in Lemma A.1 only holds for states and actions in the training datasets, i.e. s, a ∈ D. We have no reward or transition pair collected at unseen states or actions outside the training dataset, so it is impossible to bound the error outside the training dataset when consider the sampling error introduced by the reward function and the transition function. Therefore, we can lower bound the true value function by the learned value function at states and actions in the training datasets as in the following corollary.

Corollary A.1 When the sampling error defined in Lemma A.1, for any state and any action in the training dataset, s, a ∈ D, the learned value function via Eqn. 5 is a lower bound of the true one, i.e., V π (s) ≤ V π (s), if the trade-off factor ε and α satisfy the constraints

We now show the proof of Corollary A.1. From Eqn. 13, we can directly bound the estimated value function for any s, a ∈ D by

when ε and α satisfy the constraints in Eqn. 16. Note that in Eqn. 17, we use vector notations similar to those in Eqn. 13.

Therefore, when we consider sampling error introduced by the reward function and the transition pair, the learned value function by PessORL still lower bounds the true one for any states and actions in the training dataset. Thus, we finish the proof of Corollary A.1.

# A.3 Proof of Theorem 4.2

We begin the proof from Eqn. 9. We first take the expectation of both side of Eqn. 9 under the distribution d φ , then

Similarly, we take the expectation of both side of Eqn. 9 under the distribution d π β , then we have

If we subtract Eqn. 19 from Eqn. 18, we get

Therefore, we have

# A.4 Existence of Feasible Trade-off Factor

Note that both Eqn. 21 and Eqn. 16 put constraints on the trade-off factor ε. We show that we can choose an appropriate value of α to ensure that a feasible ε that satisfies both constraints exist.

Formally, we denote

for simplicity. From Eqn. 16 and 21, we have

Hence, there exists a feasible ε when (X -αY )Z -1 ≤ αW and α ≥ U . Thus, when

we can choose a feasible ε from the interval (X -αY ) Z -1 , αW .

the original PessORL, and discuss why we choose to obtain a pessimistic Q-function via adding a regularization term in policy evaluation step instead of directly subtracting an uncertainty term from the original learned value function.

We first introduce a variant of our algorithm, named PessORL-unc, in which the additional regularization term in the original PessORL policy evaluation step is removed. The policy evaluation step in PessORL-unc then becomes as follows:

Actually, Eqn. 26 is the same as the policy evaluation step in CQL. In the ablation studies, we use this optimization problem to learn a Q-function first, and then we directly subtract an uncertainty term from the learned Q-function to get the final Conservative Q-function to be used in the policy improvement step: 

where the uncertainty term Unc(s, a) is similar to the one in the original PessORL, but we no longer take the expectation over the action. Therefore, it becomes Unc(s, a) = . This term evaluates the uncertainty of the dynamics model about a state-action pair. If the sampled state is not in the training dataset, the uncertainty about it will be larger than those in the training data. Therefore, the Q-function is constrained to be lower at out-of-distribution states in this way.

Second, we introduce the variant PessORL-OPIQ. It is inspired by the work in [5], which uses a pessimistic initialization and an optimistic component on the Q-function. Since in the offline settings we need a pessimistic component in the Q-function, we set the PessORL-OPIQ uncertainty term Unc(s, a) to be the opposite of the optimistic component in OPIQ, i.e., Unc(s, a) = -C action (N (s, a) + 1) M , where C action and M are hyperparameters in OPIQ, and N (s, a) is the pseudo count of the state-action pair (s, a). Here, we use the continuous version of the OPIQ to obtain state-action counts. We adopt the pessimistic initialization from the OPIQ and update the Q function via similar policy evaluation step in Eqn. 26, but with an PessORL-OPIQ uncertainty term.

We evaluate the variants PessORL-unc and PessORL-OPIQ on two D4RL MuJoCo environments, and compare their performance to the original algorithm PessORL, CQL, BEAR, and BC based on the average returns on three random seeds. From Fig. 3(a) and (c), we can see that the variants PessORL-unc and PessORL-OPIQ both converge to similar returns which are lower than CQL and the original PessORL. Actually, the performance of these two variants are close to each other. We believe the reason is that they both require a super accurate uncertainty estimation and a stringent trade-off factor β. A rough uncertainty estimation may sometimes be harmful to the performance. As we discussed in Sec. 6.2, our uncertainty estimation method based on bootstrapped dynamics models still cannot guarantee an extremely precise estimation. Therefore, directly subtracting the uncertainty term from the learned Q-function to obtain a conservative Q-function may cause the algorithm to perform poorly. On the other side, the original PessORL mitigates the requirement of an accurate uncertainty estimation method because of the additional regularization term in Eqn. 7. We also noticed that PessORL-unc and PessORL-OPIQ still outperform the BEAR algorithm. The reason is that we implement PessORL-unc and PessORL-OPIQ on top of CQL, which is a strong offline RL method, so we can attribute most of their good performance to CQL. From Fig. 3(b) and (d), we can see that PessORL-unc maintains a value gap that is among the highest. PessORL-OPIQ is not pessimistic enough as shown in Fig. 3(b), but is too pessimistic as shown in Fig. 3(d). This indicates that they cannot effectively control the gap and thus cannot assign lower values to out-of-distribution states. The original PessORL algorithm can successfully maintain a value gap that is close to zero, indicating that it shape the value function to be the desired shape.

# Appendix B Implementation Details of the Algorithm

The implementation of our algorithm is based on the original implementation of CQL: https:// github.com/aviralkumar2907/CQL. We first train a bag of dynamics models {P 1 , P 2 , . . . , P n }, and then train the Q-network and policy network. When we train the Q-network and policy network, the uncertainty estimation model u π (s) is induced by the pre-trained dynamics models. We found in the experiments that a fixed trade-off factor ε would cause the learned value function to be too conservative and hence the learned policy to fail, so we choose to use a varying ε which is adjusted by dual gradient-descent. Following the implementation of CQL, we introduce a "budget" parameter τ to automatically control ε as below:

) From Eqn. 24, we can see that if the discrepancy between values is less than τ , then ε will be set to zero. When the discrepancy is larger than the threshold τ , ε will be increased to a large value to penalize harder on the value function. This automatic mechanism ensures a reasonable choice of ε, and reduce the tedious procedure to tune the hyperparameter ε. In the Gym MuJoCo domain, we choose τ = 0.0 for the Hopper environment, and τ = 10.0 for the Walker2d, Halfcheetah and Ant environment. In the Adroit domain, we choose τ = 20.0 for all four environments.

For the dynamics models learning part, we follow the convention in model-based reinforcement learning domain, and adopt a four layers MLP with a size of 400 each. We choose to train five bootstrap models and collect them in a bag to estimate uncertainty later in the policy evaluation and improvement steps. Each dynamic model is a Gaussian model which outputs the mean and the logstd of the next state deviation. When we train the models, we iterate through all training data for 10 epochs with a learning rate of 1e -4 and a batch size of 256.

For the Q-function learning part of the algorithm, we inherit the twin Q-function trick and soft target updates from the original SAC implementation on D4RL tasks. The Q-functions are optimized by Adam with a batch size of 256, and the learning rate is chosen to be 3e -4 across the environments. We design the Q-functions to have three layers with a size of 256 each. When we evaluate the logsumexp term in Eqn. 24, we need to sample states from the state space. However, the state space is unbounded on the gym domain and Adroit domain, so we set the sample range to be [µ -10 * σ, µ + 10 * σ], where µ and σ are the mean and the standard deviation of the current batch sampled from the training dataset.

For the policy learning part of the algorithm, we do not need an explicit policy network to model the policy, but just an implicit argmax policy in discrete settings such as Pointmass environment. In continuous settings on the Gym and the Adroit domain, we adopt a Tanh-Gaussian policy structure by the rlkit repository: https://github.com/vitchyr/rlkit. Since the action spaces in these domains are all bounded by -1 and 1, the Tanh-Gaussian policy can capture this constraint naturally. The policy network is designed to have three layers with a size of 256 each. The policy network is also optimized by Adam with a batch size of 256, with a learning rate of 3e -4 for the Pointmass and the Gym domain, and 3e -5 for the Adroit domain.

# Appendix C Ablation Studies

C.1 What if d φ (s) is induced by a uniform distribution?

In Sec. 5, we introduced a practical method to construct d φ (s). Alternatively, we may simply set ζ(s) as a uniform distribution, which also satisfies our requirement and leads to d φ (s) ∝ exp V πk (s) .

A uniform distribution could be more convenient if it is time consuming to construct d φ (s) from data.

Formally, if we choose d φ (s) ∝ exp V πk (s) which is induced by a uniform distribution, then the practical PessORL policy evaluation step becomes:

We name this variant of PessORL as PessORL-uniform. We evaluate the variant PessORL-uniform on two D4RL MuJoCo environments, and compare its performance to the original PessORL algorithm, CQL, BEAR, and BC based on the average returns over three random seeds. In Fig. 3, we show the learning curves and the value gap ∆ k in hopper-medium-v0 and walker2d-medium-v0. The value gap

follows the same definition in Sec. 6.2, which evaluates whether a method can assign high values at the states in the training data and low values at the out-of-distribution states.

In Fig. 3(a) and (c), we can see that the average return of PessORL-uniform is lower than those of CQL and PessORL. Fig. 3(b) and (d) show that the value function learned by PessORL-uniform is either not pessimistic enough or too pessimistic, causing the average return to be lower than the other two rivals. We believe the reason is that a uniform distribution in PessORL-uniform does not discriminate between OOD states and in-distribution states, so the objective function in Eqn. 25 works differently from the original one in PessORL. Eqn. 25 increases the values at in-distribution states, instead of penalizing the values at OOD states as before. This mechanism cannot guarantee an accurate penalization on most OOD states, so we observe different gaps ∆ k in different environments.

In conclusion, constructing d φ (s) via a uniform distribution leads to worse performance, but it could be a cheap alternative in terms of computational cost.

C.2 What if an uncertainty term is directly subtracted from the learned Q-function?

In Sec. 1 and Sec. 3.2, we discussed two main categories of method to obtain pessimistic value functions. Besides adding a regularization term in policy evaluation step as in the proposed PessORL, we can also improve the policy by a pessimistic estimate of Q-function. This pessimistic Q-function can be obtained by directly subtracting an uncertainty term from the learned value function, i.e., Qc θ (s, a) = Qk θ (s, a) -βUnc(s, a), where we use the superscript c to denote a conservative Qfunction, and β is a trade-off factor that makes the scale of the Q-function and the uncertainty term comparable. In this section, we first introduce two variants of the proposed PessORL algorithm, named PessORL-unc and PessORL-OPIQ, in which we used the aforementioned pessimistic Qfunction to improve the policy. Then we compare the variants PessORL-unc and PessORL-OPIQ to  Although the Adroit environments are robotic manipulation simulations, they are considered to be complex enough so that the performance of an offline RL method on these tasks can be viewed as a strong evidence of how the performance will be on real robots. There are actually prior works [2] that use Adroit environments to demonstrate the ability of RL algorithms to adapt to complex tasks. The Adroit environments, as shown in Fig. 4, contains four challenging dexterous robot manipulation tasks, which include controlling a 24-DoF simulated manipulator to twirl a pen, open a door, hammer a nail, and relocate a ball. The simulator of Adroit environments provides carefully modeled kinematics, dynamics, and sensing details of the physical hardware to encourage physical realism. The observations contain joint angles, position and orientations of the hand, the object and the target. The actions include the desired position of hand joints. These are all considered to be highly realistic. Therefore, the performance of our proposed PessORL on the Adroit domain compared to other offline RL methods can indicate a good evidence of how it will behave when transferred to real robots. Besides, our proposed method PessORL matches the simulation results of prior methods that have been demonstrated to work on real robots. Singh et al. [3] showed that CQL can chain behaviors from data and the learned policy can work on a real robot WidowX. From Fig. 1, Fig. 2, and Tab. 1, we can see that PessORL achieves similar or higher performances on all three domains. Therefore, we believe our proposed method should not be too hard to achieve good performance on real robots. Furthermore, a big advantage of offline reinforcement learning methods is that unlike online RL methods, they are designed to learn policies from pure data and then can be deployed to real robots. Learning directly from previously collected data can dramatically reduce the safety risk in the learning process in safe-critical tasks, such as robotic manipulation and autonomous driving. Actually, it can be a major block for online reinforcement learning to be deployed on real-world scenarios, because online interaction can be impractical in many settings. We show the performance of our proposed PessORL algorithm learned from human demonstrations in Sec. 6. These experiments align with the motivation of developing offline reinforcement learning methods, and we believe they can provide a good evidence of the transfer-ability of our method to real-robots.

