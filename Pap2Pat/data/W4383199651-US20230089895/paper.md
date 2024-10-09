# Introduction

In the past few years, real-time bidding (RTB) has quickly become a tens of billions of market in the globe (Google 2012;Yuan, Wang, and Zhao 2013). In RTB, a demandside platform (DSP) buys ad impressions in a programmatic manner on behalf of advertisers. The success of a DSP heavily relies on its bid optimization capability (Wu, Yeh, and Chen 2015), whose goal is to maximize the key performance indicator (KPI) agreed upon with advertisers (e.g., the total number of clicks or return on ad spend). In practice, bid optimization normally involves two steps, namely user response prediction and bid price determination (Wang and Yuan 2015). User response prediction is performed to estimate the true value of a potential ad impression. Taking the estimated value as an input, the bid price determination step aims to generate the optimal bid price for a bid request in a sequential decision making.

In practice, RTB is a highly competitive and dynamic marketplace. The prerequisite for a DSP staying competitive is the capability of accurately predicting user responses (Chapelle 2014;Ghosh et al. 2009), e.g., click-through rate (CTR) or conversion rate (CVR). A large number of prediction models (Zhang, Du, and Wang 2016;Shan et al. 2016;Guo et al. 2017;Xiao et al. 2017;Zhou et al. 2018;Feng et al. 2019) have been proposed in the literature. All of them return a point estimation for a bid request, which is then used to approximate the true value of the corresponding ad impression. Despite the substantial progress that has been made, their accuracy is still far from perfect. One major reason is due to incomplete data collection and unavoidable data noise (Punjabi and Bhatt 2018), which result in inherent uncertainties of estimated values. As indicated in (Zhang et al. 2017), explicitly factoring such uncertainties plays a critical role in optimizing a campaign's performance.

On the other hand, the dynamic nature of RTB requires modeling the correlations of bid requests under a given budget constraint in view of varying market competition. The latest research considers a DSP's bidding process as a sequential decision process and proposes model-based or model-free reinforcement learning based bidding strategies (Cai et al. 2017;Wu et al. 2018). While it lays a solid groundwork for bid optimization, these studies are based on the fundamental assumption that the estimations of ad impressions' values are accurate. Unfortunately, as explained before, this assumption can hardly hold in practice. We point out that a reasonable bid optimization solution needs to consider three inherently correlated components, including the uncertainties of estimations of ad impression values, the state of a DSP (e.g., remaining budget and future auction number), and market competition. The latter two components determine the DSP's risk tendency (e.g., take more risk by bidding more aggressively or reduce risks by bidding more conservatively).

Based on the above observations, we propose an adaptive risk-aware bidding algorithm via reinforcement learning, which, to the best of our knowledge, is the first work that simultaneously considers prediction uncertainty and the dynamic risk tendency of a DSP. We first theoretically unveil the intrinsic relation between prediction uncertainty and risk arXiv:2212.12533v1 [cs.IR] 6 Dec 2022 tendency, which helps generate a modified value of an ad impression. With this formulation of an ad impression value, it is critical to properly model a DSP's risk tendency. To this end, we propose two instantiations to model risk tendency, including an expert knowledge based formulation embracing three essential properties and an adaptive learning method based on self-supervised reinforcement learning. We summarize our key contributions as follows.

• We present an adaptive risk-aware bidding algorithm, which, for the first time, considers both prediction uncertainty and risk tendency to optimize bidding performance. This framework is based on a new formulation of an ad impression value by revealing the intrinsic relation between prediction uncertainty and risk tendency. We theoretically prove that this formulation allows achieving the optimal bid price based on VaR analysis. • We propose two ways to determine the risk tendency of a DSP. We identify three basic properties of risk tendency, which lead to an expert knowledge based instantiation.

To mitigate the extensive manual tuning efforts, we also design a self-supervised reinforcement learning method to learn the risk tendency based on experience. • We conduct extensive experiments on two public datasets to validate the superiority of our adaptive risk-aware bidding algorithm, and demonstrate the benefits of considering both prediction uncertainty and risk tendency.

# Problem Formulation

In the RTB system, each bidder of a DSP acts on behalf of an advertiser and competes for advertisement auction every time a bid request is generated from a user visit. Given each auction opportunity, the bidder estimates the ad impression value and uncertainty, and then determines the bid price to maximize the cumulative ad impression value1 . We aim to obtain optimal bidding strategy under the second-price auction, i.e., the bidder with highest bid price win the auction with second highest price payment.

# Problem Definition

Considering budget constraint in real time bidding, we formulate the bid optimization problem as a Markov decision process (MDP) in the episode level, where each episode consists of T sequential bid auctions accompanied with a budget of B. For each auction, we consider three pieces of critical information: (i) the remaining auction number

(iii) the mean value of predicted CTR (pCTR) r mean (x t ) and the corresponding standard deviation r std (x t ) for a bid request with feature vector x t . Hence, the bidder's state s is defined as s (t, b, x t ). Our target problem is that, given the remaining action number t, remaining budget b, the mean value of pCTR r mean (x t ) and corresponding standard deviation r std (x t ) for current bid request features x t , how can we determine the optimal bid price a(t, b, x t ) to optimal cumulative ad impression value in a sequential decisionmaking process?

## MDP Formulation

Reinforcement learning can be represented by tuple (S, A s , P s sa , R s sa ), where S denotes the state space, A s denotes the action (i.e., bid price) space for state s, P s sa and R s sa represent the state transition probability and the immediate reward (i.e., pCTR) for transition from state s to s under action a. Note that t = 0 and b = 0 represent the end of an episode and the state with depleted budget, respectively.

In the episode level bidding process, the state space

where X denotes the set of bid request features. Given state s = (t, b, x t ), the action space A s consists of all possible bid prices in set {0, • • • , b}, since possible bid prices are constrained by the remaining budget b. Let p x (x t ) denote the probability of the bid request feature x t for a potential ad impression and m(δ|x t ) denote the probability of market price δ given feature x t . Similar to (Zhang, Yuan, and Wang 2014), we assume that market environment m(δ) m(δ|x t ) , i.e., the market price distribution is independent of the bid request feature. Such independent distribution assumption can be justified by empirical evaluation via comparing winning bid distribution against different features in real-world iPinYou dataset (Zhang, Yuan, and Wang 2014). For the state transition, if the bid price a is larger than the market price δ (highest bid price among other competitors), then the bidder wins the ad auction, and state (t, b, x t ) will transit to (t -1, bδ, x t-1 ) with probability p x (x t-1 ) a δ=0 m(δ). Otherwise, if a < δ, the bidder will lose the auction and transit to state (t -1, b, x t-1 ) with probability p x (x t-1 ) +∞ δ=a+1 m(δ). The immediate reward is given by r mean (x t ) for t-th auction if the bidder wins the auction; otherwise it is 0. Mathematically, the state transition probability and reward function are expressed as follows:

# Methodology

In this section, we introduce the Risk-aware Reinforcement Learning Bidding (RRLB) framework that effectively integrates prediction uncertainty and a bidder's risk tendency into a reinforcement learning framework. An overview of RRLB is illustrated in Figure 1. In the following sections, we first explain the uncertainties of CTR prediction with Bayesian logistic regression and then describe the riskaware bid optimization framework and two proposed instantiations to determine the risk tendency. Finally, we describe the model-based reinforcement learning method mapping the adjusted ad impression value to the final bid price. 

## Uncertainty of CTR Prediction

Similar to (Zhang et al. 2017), we adopt Bayesian logistic regression to explicitly measure the uncertainties of predicted CTR (pCTR) values. In Bayesian logistic regression, each weight w is treated as a random variable instead of a parameter, and the variance of the random variable represents the uncertainty of the corresponding feature (Please see Appendix A for more details). Assuming that the weight w follows a Gaussian distribution, Bayesian logistic regression aims to maximize the posterior weight distribution p(w|x, y) given a bid request's feature vector x and label y. The model output is a probability estimation of the occurrence of a click event, defined as ŷ = P (y = 1|x).

The variance of weight is lower when the associated feature emerges more frequently, which means that such a model can measure the data completeness for each feature. Via updating the mean and covariance matrix of the weight w, the distribution of CTR p ŷ|x (ŷ) can be obtained. Subsequently, we define the mean and standard deviation of CTR as r mean (x) = E p ŷ|x [ŷ] and r std (x) = D p ŷ|x [ŷ], where

denote the expectation and variance over the CTR distribution p ŷ|x . The standard deviation of CTR reflects the uncertainties of pCTR values. How to obtain uncertainties of other prediction models is beyond the scope of this paper.

## Theoretical Relation Between Uncertainty and Risk Tendency

The key intuition of RRLB is to decompose the value of an ad impression θ(t, b, x t ) as the weighted sum of two parts: the mean pCTR and a compound term that simultaneously reflects prediction uncertainty and a bidder's risk tendency. Formally, the ad impression value is defined as follows:

where β(t, b) denotes the bidder's risk tendency at resource state (t, b), which is a subset of bidding state (t, b, x t ), which represents the intrinsic status of a bidder in terms of remaining auction number t and remaining budget b in an episode.

Next we provide a theoretical motivation for the formulation of Eq. ( 1). The core idea is based on the value at risk (VaR) theory borrowed from finance (Rockafellar, Uryasev et al. 2000;Linsmeier and Pearson 2000), where VaR estimates how much the predicted CTR under/over-estimates with a given probability. Note that the goal of a bidding strategy is to improve the cumulative ad impression value. Given the current bid request feature vector x t , remaining budget b and remaining auctions number t, let V a (t, b, x t ) and V a std (t, b, x t ) be the cumulative estimated impression value and uncertainty of the winning ads with the bidding strategy a(t, b, x t ). Then we define VaR of the cumulative ad impression value with the bidding strategy a(t, b, x t ) as follows:

where state-associated coefficient λ(t, b) is the risk preference that balances the cumulative estimated impression value and uncertainty. Note that β(t, b) and λ(t, b) balance the estimated value and uncertainty for the current auction and all the remaining auctions, respectively. The optimal VaR bid price a V aR maximizes the VaR of the cumulative ad impression value V λ (t, b, x t ) as follows,

The theorem below shows that the linear combination in Eq. ( 1) can achieve the optimal VaR bid price a V aR .

Theorem 1 (Risk Tendency Optimality). The RRLB framework adopting the linear formulation in Eq. ( 1) can achieve the optimal VaR bid price a

See Appendix B for the proof. Intuitively, a rational risk tendency should be a function of the resource state, defined by (t, b), of a bidder. A budget-restrained/abundant bidder would act very differently in taking risks during the bid. However, we deem that the risk tendency is independent of a random bid request x.

## Expert Knowledge Based Risk Tendency

We leverage expert knowledge on RTB to design the first instantiation of risk tendency β(t, b) to reveal the intrinsic risk preference of a rational bidder. We distill three key rules as follows. (i) The sufficiency of the remaining budget b determines the sign of risk tendency β(t, b), where a positive risk tendency indicates a strong preference to win auctions. (ii) The partial derivative of risk tendency β(t, b) w.r.t. remaining budget b (remaining auction number t) should be positive (negative) because more budget naturally allows the bidder to take the risk of bidding more ad impressions. (iii) When the remaining budget b and remaining auction number t are relatively large (e.g., the beginning of an ad campaign), risk tendency β(t, b) depends on the ratio of b to t and the extent of market competition. Formally, we express the three rules as follows.

(i) Sign of risk tendency:

(ii) Monotonicity of risk tendency:

(iii) Approximation for the scenarios of large remaining budget and auction number:

Before elaborating the exact formulation of β(t, b), we have to quantify the sufficiency of the budget as pointed out in the first rule. In practice, the budget richness is highly related to the level of market competition. Given a certain market price distribution m(δ) and resource state (t, b), let U (t, b) denote the expected bid price for an auction such that the remaining budget will be depleted in the remaining future auctions. Supposing that budget b is evenly allocated to the remaining t auctions, we can calculate U (t, b) through the following formula:

Since the bidder wins an auction only if bid price U (t, b) is higher than market price δ, the left side of Eq. ( 5) represents the expected actual cost, which should be the same as b t based on the assumption of even budget allocation. Based on the above intuition of budget richness, we formally define risk tendency as follows:

where α is a positive hyperparameter that controls the slope of risk tendency, Û is the budget richness threshold tuned from historical data, and function tanh(•) confines risk tendency within the range (-1, 1). It can be observed that the proposed risk tendency formulation satisfies all the three expert knowledge based rules. First, the expected bid price U (t, b), which measures the amount of budget richness, determines the sign of risk tendency β(t, b), which is nonnegative only if U (t, b) ≥ Û as required in rule (i). Second, both U (t, b) and β(t, b) increase with budget b, and decrease with t as required in rule (ii). Third, the expected cost is proportional to the ratio b t as shown in Eq. ( 5), which helps the subsequent design of risk tendency to meet rule (iii).

## Self-Supervised Risk Tendency

Although the above knowledge-driven design of risk tendency may capture a bidder's intrinsic risk preference well, it requires a careful selection of hyperparameters α and Û through many trials. To avoid such manual efforts, we propose a self-supervised reinforcement learning bidding (ss-RLB) method as shown in Figure 2 to automatically generate risk tendency via a multi-layer perceptron (MLP). The pseudo code of ssRLB is summarized in Appendix C.

Self supervised by the bidding history, we update the mapping function β mlp (t, b) = M LP (t, b; W mlp ) generated from an MLP to approximate the risk tendency at resource state (t, b) with trainable weight W mlp . The ssRLB framework consists of a Gaussian exploration block, an experience buffer, an MLP mapping function, and a batch sampling. We explain the details of each component as follows. Experience buffer. Motivated by experience replay optimization in reinforcement learning (Zha et al. 2019), we adopt the experience buffer to store good experiences represented by a quaternary set B = (t, b, β(t, b), V episode ) from the bidding history, where V episode denotes the cumulative reward for the entire episode. A "good" experience means that a larger reward V episode is obtained by using risk tendency β(t, b). Let N be the buffer's total length. The samples with the lowest reward will be removed if the buffer is full. In this way, the experience buffer could always provide the best samples explored so far for training the MLP.

Batch sampling. Batch sampling is responsible for sampling batch B batch from the buffer. We apply a simple uniform sampling to generate B batch .

Training MLP mapping function. Given the experience batch B batch , we update the weight in the MLP mapping function by minimizing the mean square loss function:

Since we only preserve the experiences with larger rewards in the buffer, the mapping function will be updated under supervision toward learning a good risk tendency.

## Bid Price Determination

Previous sections introduce how to modify the ad impression value with prediction uncertainty and risk tendency. Next, we explain how to calculate the final bid price. We adopt the model-based reinforcement learning bidding strategy (Cai et al. 2017) to maximize the cumulative reward. Specifically, we regard the pCTR r mean (x t ) as the immediate reward for t-th auction, and cumulative reward V (t, b, x t ) is defined as the expected cumulative reward starting from state (t, b, x t ) with the optimal bid price. By definition, we have V (0, b, x t ) = V (0, b) = 0 since there is no available auction. Similar to (Cai et al. 2017), the updated policy for the cumulative reward is given by:

where X represents the entire feature vector space, the two integrations represent the immediate reward for winning and losing cases. Furthermore, the cumulative reward without observation on x can be obtained by integrating over bid request feature vector x. Formally, the cumulative reward

where r avg = X p x (x t-1 )r mean (x t-1 )dx t-1 is the average ad impression value over the entire feature vector space.

The cumulative reward V (t, b) can be iteratively updated given the average ad impression value and market price distribution. Note that ∞ δ=0 m(δ) = 1. The bid price at state (t, b, x t ) is calculated by:

The cumulative reward V (t, b) monotonically increases w.r.t. the remaining budget b, and g(δ) monotonically decreases. If g(b) < 0, there must exist an integer price A satisfying that 0 ≤ A ≤ b, g(A) ≥ 0 and g(A + 1) < 0. The optimal bid price is finally given by:

# Experiments

In this section, we conduct experiments to evaluate our RRLB framework with the two instantiations of risk tendency, namely expert knowledge based Compared methods. We compare ekRLB and ssRLB with two state-of-the-art baselines. Lin is a linear bidding strategy with bid price a Lin = b 0 θ(x), where parameter b 0 can be tuned on training data (Perlich et al. 2012). RLB is a model-based reinforcement learning bidding strategy (Cai et al. 2017). These two baselines only make use of r mean (x). Besides, we also consider two variants of our proposed reinforcement learning bidding framework, one based on constant risk tendency (CRTRLB) and the other based on constant uncertainty (CURLB), for an ablation study.

Evaluation sketch. Given a budget and episode length for each ad campaign, we evaluate different bidding strategies in terms of the total click number. In the experiments, the bidding data includes bid request feature vectors, market prices and user response (click) labels. The market adopts second-price auctions, meaning that a bidder pays only the second highest price instead of the actual bid price for a winning auction. Similar to (Zhang et al. 2017), we calculate the pCTR r mean (x) and corresponding uncertainty r std (x) for each bid request with feature vector x. We divide training and test datasets into episodes, each of which contains T = 1000 auctions. As for the budget constraints, we allocate the budget as follows: B = CP M train ×10 -3 ×T ×c 0 , where CP M train and c 0 are the cost per mille impressions in the training dataset and budget coefficient, respectively. We compare the models using the budget coefficient set {1/32, 1/16, 1/8, 1/4, 1/2}. For ekRLB, we tune the risk tendency hyperparameters α and Û in Eq. ( 6) on the training dataset to optimize the number of total clicks. For ss-RLB, the mapping function M LP (t, b; W mlp ) is realized by a four-layer MLP with 64 hidden units. Weight W mlp is trained with the Adam optimizer to minimize the mean square loss function at the learning rate of 1 × 10 -3 . The experience buffer size and batch size are 1 × 10 5 and 32, respectively. We update the buffer every 5 training episodes.

## Comparison Results

We present the total click number of different methods on the 9 campaigns of iPinYou and YOYI with budget coefficient c 0 = 1/2 in Table 1 to answer question Q1. On iPinYou, ekRLB obtains the best performance on most campaigns, achieving the largest average total click number of 244.2. On YOYI, both ekRLB and ssRLB outperform RLB, and ssRLB achieves the largest click number of 914. The two variants CRTRLB and CURLB obtain less clicks on both datasets, which validates the benefits of considering both uncertainty and risk tendency in Eq. ( 1). Note that ss-RLB obtains less clicks than ekRLB on iPinYou but more on YOYI probably because the training of self-supervised reinforcement learning is less stable. Nevertheless, we deem that ssRLB is still a valuable alternative since it does not require manual tuning of α and Û over a large volume of historical data. We leave the improvement on risk tendency learning for future work.

In the left part of Figure 3, we further show the performance improvements of RLB and ekRLB over Lin on iPinYou under the entire budget coefficient set. Two notable findings can be observed. First, the two reinforcement learning based strategies outperform Lin consistently over all budget settings, which validates the benefits of modeling the bidding process as an MDP. Given a specific budget constraint, all bid requests are inherently correlated instead of independent in Lin since previous bid prices determine the remaining budget. Second, ekRLB gets more clicks than the traditional RLB, especially in the cases with larger budgets, which demonstrates the advantage of explicitly modeling prediction uncertainty within a risk-aware reinforcement learning framework.

## Ablation Study

To answer Q2, we study the individual contributions of prediction uncertainty and risk tendency by comparing with constant uncertainty and risk tendency. Regarding ekRLB as the benchmark method, the right part of Figure 3 shows the performance degradation of the two variants CRTRLB and CURLB. Along with the results in Table 1, we can find that (i) both CRTRLB (with constant risk tendency) and CURLB (with constant uncertainty) perform worse than ekRLB, which proves that it is critical to consider both prediction uncertainty and risk tendency to achieve an optimal bid optimization framework. (ii) CURLB achieves better performance than CRTRLB, suggesting that modeling risk tendency is even more important than the prediction uncertainty. This is because risk tendency determines how to use (e.g., add or subtract) prediction uncertainty.

Hyperparameter Study

To answer Q3, we give a comprehensive hyperparameter study to investigate how hyperparameters slope α, constant uncertainty r 0 and constant risk tendency β 0 affect the performance of the methods ekRLB, CURLB and CRTRLB, respectively. Specifically, we report the experimental results on campaign 1458 of the iPinYou dataset with budget coefficient c 0 = 1/2 in Table 2. The performance metrics include click number and budget consumption ratio, where budget consumption ratio is defined as the cumulative cost over the overall budget. The detailed experimental results and analysis are summarized as follows.

Slope α for ekRLB. Hyperparameter α controls the slope of risk tendency, and then influences the bid price of ekRLB. Note that, in the case α = 0, we have 0 risk tendency based on Eq. ( 6) of the main text, and ekRLB degenerates to RLB. We can clearly observe that the total click number and profit reach the highest value at a medium slope scale of α = 0.1. This result implies that the total click number is not sensitive w.r.t α and that ekRLB is robust on the hyperparameter α.

Constant uncertainty r 0 for CURLB. The method CURLB achieves relative comparable performance with ekRLB even though a constant uncertainty is applied. We further study the influence of constant uncertainty r 0 by varying it in range [0, 1.8 × rstd ]. Here we set constant uncertainty r 0 as a constant coefficient multiplying with the average uncertainty rstd in the training dataset. For the case r 0 = 0, we have prediction uncertainty of 0 for all ad impressions, when CURLB degenerates to RLB. We observe that constant r 0 = 0.2 * rstd achieves the best performance in terms of both click number and profit, since higher/lower risks lead to ad impressions with overly large/small prices that decrease Constant risk tendency β 0 for CRTRLB. Compared with ekRLB, it can been observed that a random selection of constant risk tendency β 0 in CRTRLB greatly damages model performance. We further study its influences by considering β 0 within range [-0.5, 0]. We only use the negative risk tendencies since a positive one tends to overestimate an ad impression and usually results in worse performance. For the case β 0 = 0, we remove risk tendency and degenerate CRTRLB to RLB. We observe that β 0 = 0.0 achieves the most clicks and that when β 0 equals -0.4 to -0.5, CRTRLB extremely underestimates the ad impression value and bids with a small price, leading to losing almost all ad impressions and low budget consumption ratio.

## Visualization of Risk Tendency

Risk tendency reflects the risk preference of a rational bidder on given states. We designed two different methods to learn risk tendency, one based on expert knowledge and the other based on self-supervised learning. We visualize these two methods' risk tendencies for all states in Figure 4. It can be observed that both approaches have similar trends in mapping states to risk tendency, which suggests that our self-supervised learning algorithm aligns well with the expert knowledge. Specifically, risk tendencies are negative for those resource-limited states at the upper left corner, where a bidder has a small budget for a large number of remaining auctions. In such a state, the bidder prefers to bid with conservative prices. On the other hand, risk tendencies change to positive for those resource-rich states at the bottom right corner because the bidder has a sufficient budget for remaining auctions to support more aggressive bid prices.

# Related Work

User response prediction. User response prediction can be modeled as a probability estimation task, e.g., click-through rate (CTR) (Graepel et al. 2010), conversion rate (CVR) (McMahan et al. 2013). A series of prediction models have been proposed for user response prediction, including linear model (Lee et al. 2012), factorization machines (Oentaryo et al. 2014) and deep learning based models (Guo et al. 2017;Zhou et al. 2018;Feng et al. 2019). Bidding strategy. Truthful bidding is the most fundamental strategy that has been proven to be optimal in secondprice auctions with unlimited budget (Krishna 2009). In practice, every ad campaign has a budget constraint, where linear (Perlich et al. 2012) and model-based/model-free reinforcement learning based strategies (Cai et al. 2017;Wu et al. 2018) can be adopted to determine bid prices. (Zhang et al. 2017) is most relevant to our work, which proposes a risk management algorithm based on value at risk, but ignores intrinsic interactions between the market environment and the state of a bidder. In our work, we propose a riskaware reinforcement learning based bidding strategy that explicitly considers such interactions.

# Conclusion

In this paper, we investigated the bid optimization problem in RTB with the benefits of risk information. For the bid price determination with budget constraint, we, to the best of our knowledge, firstly consider both estimation uncertainty and the dynamic risk tendency. Specifically, we first theoretically analyze the relation between prediction uncertainty and risk tendency of a bidder, and then proposed an adaptive risk-aware bidding algorithm with budget constraint. Subsequently, we developed two instantiations to determine risk tendency based on expert knowledge or self-supervised learning. Experimental results on real datasets demonstrate that RRLB making use of both prediction uncertainty and risk tendency achieves better cumulative performance than representative competitors.

# Appendix A

VaR Introduction: Our risk-aware bidding strategy adopts the linear combination θ(t, b, x t ) = r mean (x t ) + β(t, b)r std (x t ) to adjust an ad impression value. In this section, we provide a theoretical motivation for such a linear combination between the pCTR and corresponding uncertainty. The core idea is based on the value at risk (VaR) borrowed from finance (Rockafellar, Uryasev et al. 2000;Linsmeier and Pearson 2000), where VaR estimates how much the predicted CTR under/over-estimates with a given probability. Formally, we provide a definition of VaR.

Definition 1. Let random variable X be the profit with cumulative distribution function F X (x). The VaR at level α ∈ (0, 1) is defined as the value such that the probability of a loss greater than VaR is (at most) α (Artzner et al. 1999)

Probability Guarantee of Linear Combination. Note that V a (t, b, x t ) and V a std (t, b, x t ) represent the cumulative estimated ad impression value and the uncertainty of the win ads given the current bid request feature vector x t , budget b, remaining impression number t and the bidding strategy a(t, b, x t ), Lemma 1 states that the linear combination between V (t, b, x t ) and V std (t, b, x t ) guarantee the probability of one-sided tail for random CTR distribution, which is consistent with VaR in finance.

Lemma 1 (Cantelli's inequality). For a real-valued random variable X with mean µ and standard deviation σ, the following inequality holds:

The above probability bounds motivate the definition of the VaR of cumulative ad impression value V a λ (t, b,

# Appendix B

The proof of Theorem 1 (Risk Tendency Optimality)

Proof. Note that the bidder wins an ad impression if the bid price a larger than the market price δ. The cumulative estimated ad impression value and the corresponding uncertainty should satisfy 

Combining Eq. ( 8) and Eq. ( 9), we have

By firstly setting θ(t, b, x t ) = r mean (x t ) + β(t, b)r std (x t ) and adopting the model-based method (Cai et al. 2017), it can be seen that the linear combination in θ(t, b, x t ) can achieve the optimal bid price a V aR (t, b, x t ), which maximizes the VaR of the cumulative ad impression value.

# Appendix C

Training Algorithm: The pseudo code algorithm for selfsupervised risk tendency learning is shown in Algorithm.1.

