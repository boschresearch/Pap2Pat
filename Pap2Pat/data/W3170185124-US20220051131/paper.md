# INTRODUCTION

In online advertising, inventories that are not directly sold are primarily auctioned programmatically in real-time bidding (RTB). Before 2018, second-price was the dominant form of auction for RTB, where the winner only needs to pay the second highest bid price. However, starting in 2017, all the major exchanges/SSPs including AppNexus, Index Exchange, OpenX, Rubicon Project, and Pubmatic, with the exception of Google AdX, were rolling out or testing first-price auctions, where the winner must pay whatever bid it submitted, in varying degrees [35]. Google transitioned to first-price auctions in 2019 [4]. Several motivations were behind the transition away from second-price auctions. Firstly, first price auctions provided greater transparency and accountability for bidders, since the bidder was always charged exactly what they offered [9,14,32,36]. Secondly, the unmodified second price auctions proved to be incompatible with the widespread and popular practice of Header Bidding [21].

For demand-side platforms (DSPs), which are the bidders in the auctions, transitioning from second-price auctions to first-price auctions meant that bidding strategies would need to be dramatically adjusted. In second-price auctions, auction theory states that it is a dominant strategy for a bidder to bid truthfully [12], namely it is the optimal strategy for a DSP to compute the value of the inventory being auctioned and submit this value as the bid price, regardless of the other bidders' behavior. However, for first-price auctions such a strategy would cause DSPs to overbid and thus lose money. This comes from the fundamental difference in the payment between second-price and first-price auctions.

Unlike in second-price auctions, in first-price auctions a DSP must incorporate other bidders' behavior, more precisely its estimates of other bidders' bid prices, into its own bidding strategy. If the competing bidders' prices were known in advance, which is impossible in practice, the optimal bidding strategy would be to submit a bid price that is slightly higher than the highest competing bid price so as to win the auction with the lowest price possible. In reality, a DSP has to estimate the minimum winning price as best as it can, and lower its original bid price intended for second-price auction, i.e., shade the truthful value of the inventory, accordingly. This process is known as bid shading. Bid shading is relatively new to online advertising, but it has been used in auctions from other industries [7,8,11,20].

The most important aspect of bid shading is a trade-off between the winning rate and (Return On Investment) ROI. The more the bid price is shaded, namely the lower the final bid price, the better the ROI if the bid is won. However, lower bid price also lead to lower probability of wining a bid. The buyer or bidder surplus [20,21] is the shaded amount, namely the difference between the bid price before shading and the final bid price if the bid is won. The surplus is 0 if the bid is lost. The quantitative objective of bid shading is thus to maximize the surplus, either directly or implicitly.

In the first price auction, an important piece of information is the minimum winning price, which is the highest competing bid, inclusive of the floor price, if provided. However, it's up to an SSP to decide whether to provide the minimum winning price to the participating DSPs after the auction. Open (non-censored) first price auctions refer to the auctions where feedback including minimum winning price are shared to all participants regardless of auction outcome while in closed (censored) auction, only the win or loss feedback is available.

In this paper, we propose a deep distribution network to learn the distribution of minimum winning price for both censored and non-censored first price auctions, as well as for efficient search of the optimal bid price to maximize the profit in the real-time serving. The model has the flexibility of explicitly choosing the distributions of the minimum winning price and the structures of the network. Comprehensive experiments have been conducted and the model has been successfully deployed in one of the biggest DSPs in the world. We demonstrate the effectiveness of the algorithm by showing its performance lift compared to the existing models in offline and online setting.

To summarize, the main contributions of this study are the following:

• We propose a novel framework for bid shading that, to the best of our knowledge, is the first unified distribution-based bid shading method can be applied for both censored and non-censored first-price auctions. • We mathematically prove that an efficient search algorithm can be used to find the optimal bid price that maximizes surplus given the distributions. This allows the model to be deployed online under strict latency constraints. The rest of the paper is organized as follows: In Section 2, we discuss related work in bid shading and online auctions. In Section 3, we describe the formulation of our bid shading algorithms, including details on how we train models to estimate the distributions of minimum winning price and how to search for the optimal bid price efficiently on both censored and non-censored first-price auctions. In Section 4, we show the comprehensive experiments of different choices of distributions and network structures compared to the current state-of-art bid shading algorithms for both censored and non-censored first price auctions. In Section 5, we briefly introduce the online deployment of deep distribution network in the serving system of our DSP and show the online ROI improvements compared to productions. Finally we conclude in Section 6.

# RELATED WORK

Bid optimization is one of the most fundamental problems in online advertising [6,18,37,40,41]. Recently, bid shading [11,20,42] attracts much attention since most ad exchanges and SSPs are shifting from second to first price auctions. Bid Shading shares characteristics with the Seller's (Reserve) Price Optimization Problem [5,23,25,26,33,34], where sellers have a good with a manufacturing cost, and their task is to set their price above this cost to maximize their profit. However, a variety of constraints exist in the bid shading buyer problem that are unique: (i) Buyers need to predict the bidding behavior of competing buyers on each auction, leading to strategic considerations. (ii) Buyer Feedback is constrained in systematic ways, with censored and uncensored information provided. (iii) Buyers need to find a bid price for billions of auctions, each of which has combinatorial aspects; whereas sellers generally have a set of fixed inventory [1,3]. For these reasons, most authors talk about the Bidding problem as a Buyer specific activity, distinct from Seller reserve pricing, and we take the same approach in this paper.

There have been two general approaches for bid shading, depending on whether the minimum winning price is provided or censored. The first assumes that the minimum winning price is provided, and builds a machine learning algorithm to predict the optimal shading factor -the ratio of the minimum winning price to the bid price before shading. For instance, Logistic Regression (LogReg) and Factorization Machines (qFwFM) [15] have been used previously to predict the optimal shading factor, using an asymmetric loss function which penalizes losses. The drawback of these approaches is that they learn from the winnable bids only [15], ignoring a large portion of available data. This paper proposes an algorithm for modeling distributions over the entire bidding landscape which allows for learning from both won and lost auctions.

The other general approach tries to estimate the distribution of the minimum winning price at segment level, and then finds the optimal bid price by maximizing the expected surplus with respect to the estimated distribution. The NonLinear algorithm in [22] attempts to estimate the distribution using a non-linear approximation on a predefined segment. The main drawback of this method is that the distribution is estimated separately, and thus cross-segment information is not utilized. Furthermore, the segments must be explicitly defined and small segments must be manually grouped together. The recent WinRate model from [29] takes a similar approach but approximates the distributions, implicitly with log-logistic, for all segments simultaneously, while its drawback is that it doesn't utilize the minimum winning price information when available.

Outside of the problem of bid shading, there has been some related research trying to characterize winning prices on auctions. For example, in [38,39] the authors first estimate the winning price distribution, and then use it to do point-wise prediction of the winning price via a mixture model. The distribution implicitly assumes that the winning price follows logistic distributions, while a log-logistic distribution is used in [29]. Additionally, there has been prior work estimating the bidding landscape in second-price auctions [38,39], in which the minimum winning price feedback is only available while winning the auction. These approaches would need to be extended to work under first-price auctions, and the problem of surplus maximization.

Sell-Side Platforms are motivated to provide bid shading services to the bidders, especially during the transition period from secondprice to first-price auctions. Such services include Bid Translation Service from Google AdX [16], Estimated Market Rate from Rubicon Project [31], and Bid Price Optimization system from AppNexus [2]. However, these services are rather a transition tool in helping DSP's transition to first-price auctions, and many of them are being deprecated. For example, AdX deprecated its Bid Translation Service in May 2020 [19].

# ALGORITHMS

For the reader's convenience, we list some notations that will be used throughout the paper. First of all, we define surplus mathematically. Upon receiving a bid request for first-price auction, its value 𝑉 is estimated based on its event rate, such as click-through rate (CTR) or conversion rate (CVR), and a campaign level price control signal that helps to pacing campaign budget smoothly across the flight. Let 𝑏 be the bid price to be submitted, and b be the minimum winning price. I(𝑏 > b) equals 1 if 𝑏 > b and 0 otherwise, which indicates with bid price 𝑏 whether we win the auction. Then the surplus is defined as

# 𝑉

Let 𝒙 = (𝑥 1 , 𝑥 2 , . . . , 𝑥 𝑘 ) be the input feature vector derived from the current publisher and user attributes, such as top level domain, sub-domain, layout, day of week, etc. We calculate the optimal bid price 𝑏 * given the current input feature vector in two steps:

Distribution Estimation First we build a machine learning model to approximate the conditional distribution 𝐷 b |𝒙 of the highest competing bid price b by modeling its PDF or CDF.

Surplus Maximization Then we find the bid price 𝑏 = 𝑏 * that maximizes the expected surplus E b |𝒙 [𝑆]:

In the following sections, we describe in more details how the distribution estimation and surplus maximization are conducted.

## Inference of Distribution

Conditioning on input feature vector 𝒙 of a bid request, to find the optimal bid price b* that maximizes the expected surplus, modelling of winning probability Pr( b < 𝑏; b | 𝒙) for any intended bid price 𝑏 is the key. We assume that for given 𝒙, the minimum winning price follows a conditional distribution 𝐷 b |𝒙 . We further assume that each b is drawn independently from a probability distribution 𝐷 b;𝜶 (𝒙) that belongs to a family of known distributions, where 𝜶 = (𝛼 1 , 𝛼 2 , . . . , 𝛼 𝑚 ) is its m-parameters vector. Note that the parameter vector 𝜶 is a function of 𝒙, namely, bid samples with the same input feature vector follow the same distribution. We will discuss details about different distributions at greater length in Section 3.3 3.1.1 Minimum winning price is provided by SSPs. In non-censored first-price auctions, the minimum winning price b is provided by the SSP after the auction regardless of the outcome. We build a machine learning model to estimate the distribution of 𝐷 b |𝒙 . Let {(𝒙 (𝑖) , b𝑖 )} 𝑛 𝑖=1 be the training data set of bid samples, where 𝒙 (𝑖) is the input vector, b𝑖 the minimum winning price provided by the SSP, and 𝑛 is the total number of training samples. Let 𝑓 ( b; 𝜶 (𝒙 (𝑖) )) be the corresponding PDF. Then we estimate 𝜶 using maximum likelihood estimation (MLE):

where D is a predetermined distribution family. The model structure for maximizing the log-likelihood is illustrated in Figure 1.

Note that compared to 𝒙, 𝜶 is of much lower dimension, namely

Figure 1: Model structure for PDF estimation when the minimum winning price is provided by SSPs 3.1.2 Minimum winning price is censored by SSPs. If the SSP does not provide the minimum winning price after the auction, the previous MLE approach will not work. In this case, we use an approach similar to that in [29] to estimate the CDF of 𝐷 b |𝒙 , adding the flexibility of choosing the distribution family. Let {(𝒙 (𝑖) , 𝑏 𝑖 , ℓ 𝑖 )} 𝑛 𝑖=1 be the training data set of bid samples, where 𝒙 (𝑖) is the input feature vector, 𝑏 𝑖 is the submitted bid price, and ℓ 𝑖 ∈ {0, 1} indicates if the bid was won. Let 𝐹 (𝑏; 𝜶 (𝒙 (𝑖) )) = Pr( b𝑖 < 𝑏; 𝜶 (𝒙 (𝑖) )) be the CDF of 𝐷 b |𝒙 . Then the likelihood of winning the bid with submitted price 𝑏 𝑖 is 𝐹 (𝑏 𝑖 ; 𝜶 (𝒙 (𝑖) )). Since we know the result of the auction, we formulate it as a prediction problem. More precisely, we estimate 𝜶 by minimizing the loss between the likelihood of winning and the actual result:

where D is a predetermined distribution family, and 𝐿 is a loss function. In this paper, we use the well-known log loss:

The model structure for minimizing the log loss is illustrated in Figure 2. As can be seen, the win probability is first evaluated at bid price 𝑏 for given CDF and the loss is then calculated with the binary feedback 𝑙. In Section 4 we will compare models built on different distribution families D, as well as different structures of the block 𝜶 (𝒙).

## Surplus Maximization

Regardless of whether the SSP provides the minimum winning price, let

be the expected surplus function with respect to 𝐷 b |𝒙 , the distribution of the minimum winning price for the current input feature vector 𝒙. Given 𝒙 and the bid price before shading 𝑉 , the objective is to solve the following maximization problem: max 𝑏 ∈ (0,𝑉 ) 𝑠 (𝑏; 𝑉 , 𝒙).

If the underlying distribution 𝐷 b |𝒙 results in a surplus function that has a unique local extremum (maximum or minimum), we can adopt the golden section search algorithm [24] shown in Algorithm 3.1 which converges in logarithmic time. It is a more numerically stable approach for most distributions, especially for gamma distribution and log-normal distribution, since no calculation of gradient is needed. The golden section search is more versatile and robust than other algorithms that require the calculation of gradients, which makes it more suitable for online implementation.

# Algorithm 3.1 Golden Section Search for Surplus Maximization

Require:

1: • 𝑉 : estimated value of the current ad opportunity • 𝑠 (𝑏): expected surplus function;

• 𝜖 > 0: minimum valid interval length • 𝑁 : maximum number of search steps Ensure: 𝛽 > 0, 𝑉 > 0, and 𝑠 (𝑏) has exactly one local maximum and no local minimum in (0, 𝑉 ).

𝑥 2 ← 𝑏 min + (𝑏 max -𝑏 min )/𝑔𝑟 11: end for return (𝑏 min + 𝑏 max )/2

## Distribution Families

There are some constraints in choosing the distribution of minimum winning price to make economic sense. For example, its PDF should have a support between 0 and positive infinity. We mainly focus on truncated-normal, exponential, gamma, and log-normal distribution families and show that the surplus functions for them have a unique local extrema, so that Algorithm 3.1 is applicable to them all. We first introduce a few notations. Assuming that the minimum winning price b follows a probability distribution 𝐷 with CDF 𝐹 (𝑏) and PDF 𝑓 (𝑏), then expected surplus and its first and second derivatives can be calculated as

For simplicity, we don't explicitly write the above as functions of input feature vector 𝒙 and bid price before shading 𝑉 here. We first show that for all truncated-normal, exponential, gamma, and log-normal distributions, 𝑠 ′′ (𝑏) has at most one root in (0, 𝑉 ).

, where 𝜎 > 0 and

𝑓 𝑒 (𝑏) = 𝜆𝑒 -𝜆𝑏 , where 𝜆 > 0, (exponential)

𝑏 𝛼-1 𝑒 -𝛽𝑏 , where 𝛼 > 0, 𝛽 > 0, and (gamma)

, where 𝜎 > 0.

(log-normal)

Throughout this paper, we use the truncated-normal distribution with 𝐴 = 0 and 𝐵 = ∞. Thus, for all these four distributions, the support of 𝑏 are [0, ∞].

Lemma 1. For any truncated-normal, exponential, gamma, or lognormal distribution of the minimum winning price, 𝑠 ′′ (𝑏) has at most one root in (0, 𝑉 ). Furthermore, 𝑠 ′′ (𝑉 ) < 0.

Proof. Using Equation ( 7), we can calculate 𝑠 ′′ (𝑏) for each of the listed distributions.

• For truncated-normal distribution we can show that

Let 𝑔(𝑏) = (𝑉 -𝑏)(𝜇 -𝑏)𝜎 -2 -2. Note that 𝑔(𝑏) is quadratic and hence convex, and 𝑔(𝑉 ) = -2 < 0. Thus 𝑔(𝑏) has at most one root in (0, 𝑉 ), and so does 𝑠 ′′ (𝑏). • For gamma distribution we can show that

Let 𝑔(𝑏) = (𝛼 -1 -𝛽𝑏)(𝑉 -𝑏) -2𝑏. Again, 𝑔(𝑏) is quadratic and hence convex, and 𝑔(𝑉 ) = -2𝑉 < 0. Thus 𝑔(𝑏) has at most one root in (0, 𝑉 ), and so does 𝑠 ′′ (𝑏).

Since exponential distribution is a special case of gamma with 𝛼 = 1 and 𝛽 = 𝜆, the same proof holds for exponential distribution. • For log-normal distribution we can show that

Let 𝑔(𝑏) = (𝜇 -𝜎 2ln 𝑏)(𝑉 -𝑏) -2𝜎 2 𝑏. It's easy to verify that 𝑔 ′′ (𝑉 ) = (𝑏 +𝑉 )/𝑏 2 > 0, so 𝑔(𝑏) is convex. Since 𝑔(𝑉 ) = -2𝜎 2 𝑉 < 0, 𝑔(𝑏) has at most one root in (0, 𝑉 ), and so does 𝑠 ′′ (𝑏).

In summary, for all the listed distributions the corresponding 𝑠 ′′ (𝑏) has at most one root in (0, 𝑉 ), and 𝑠 ′′ (𝑉 ) < 0. □ Finally we show that for all the listed distributions the corresponding surplus function has one global maximum. Theorem 1. For any truncated-normal, exponential, gamma, or log-normal distribution of the minimum winning price, the surplus function 𝑠 (𝑏) has one global maximum and no local minimum in (0, 𝑉 ).

Proof. From Lemma 1, for any truncated-normal, exponential, gamma, or log-normal distribution, 𝑠 ′′ (𝑏) has at most one root in (0, 𝑉 ) and 𝑠 ′′ (𝑉 ) < 0. Then only one of the following two cases could happen:

• 𝑠 ′′ (𝑏) < 0 for all 𝑏 ∈ (0, 𝑉 ), in which case 𝑠 (𝑏) is concave and hence has at most one local maximum and no local minimum. • 𝑠 ′′ (𝑏) has a unique root 𝑏 0 ∈ (0, 𝑉 ) such that 𝑠 ′′ (𝑏) > 0 for all 𝑏 ∈ (0, 𝑏 0 ) and 𝑠 ′′ (𝑏) < 0 for all 𝑏 ∈ (𝑏 0 , 𝑉 ), in which case 𝑠 (𝑏) is convex in (0, 𝑏 0 ) but concave in (𝑏 0 , 𝑉 ). Note that 𝑠 (0) = 𝑠 (𝑉 ) = 0, then 𝑠 (𝑏) must have at most one local maximum in (𝑏 0 , 𝑉 ) and no local minimum.

In both cases, 𝑠 (𝑏) has at most one local maximum and no local minimum. Further, since 𝑠 (0) = 𝑆 (𝑉 ) = 0 and 𝑠 (𝑏) > 0 for all 𝑏 ∈ (0, 𝑉 ), 𝑠 (𝑏) must have one global maximum. □

# OFFLINE EXPERIMENTS

In this section, we present comprehensive offline experiments on our DSP private bidding dataset. The following questions would be answered in the following sub-sections:

• Q1: Does lower log-loss or better distribution fit results in a higher surplus? • Q2: How much is the surplus lift when minimum winning price is available in training the deep distribution network compared with when minimum winning price is not available? • Q3: Will performance be improved by using more powerful network structures (deepFM etc.) that capture high-order feature interactions compared to logistic regression or Factorization Machines (FM)?

## Dataset

The dataset we use for offline experiments is VerizonMedia DSP private bidding dataset on Adx exchanges. We extracted 12 fields through feature engineering, including exchange id, top level domain of the ad opportunity, sub domain, layout of the ad, position of the ad, device type, name of app, publisher id of the ad request, country, user local hour of the day, user local day of the week, if the user is new. There are billions of records, with millions of active features and minimum winning price available. We use 7 day's data to train the model and use 1 day's data to test. Notice that we train two types of models separately to simulate censored and non-censored first-price auctions. For the pdf estimation model which introduced in Fig. 1, minimum winning price are used as labels, while for the cdf estimation model in Fig. 2, the binary win or lose information (1/0) is used as label. We used the bid requests in the past 7 days for training to mitigate impact of the day of week pattern. Log-loss and surplus are the main two metrics we use in the offline experiment.

## Minimum winning price provided by SSPs

The production bid shading algorithms for non-censored first-price auctions is Factorization Machine based point estimation algorithm. It uses Field-weighted Factorization Machine (FwFM) as the model structure and learns the optimal shading factor for each bid request with an asymmetric loss function (penalize more when losing the bid) [15]. To have a fair comparison with the baseline, we uses same model structure: FwFM as the model structure in Figure 1, and conduct experiments of different distributions we introduced in Section 3.3. For surplus metric, we only show the percentage of lift compared to the production model for privacy reason. Table 1 summarizes the results and we do observe the correlation between log-loss and surplus, in the sense that lower log-loss results in higher surplus. Among all the distributions, log-normal has the best performance with 9.7% surplus lift compared to the current production algorithm possibly due to its capability to better model the long-tail distribution of the minimum winning price. 

# Model

## Minimum winning price not provided by SSPs

To simulate the censored first-price auctions where minimum winning price feedback is not available. We train the deep distribution network on the same dataset while not using minimum winning price information during training. The loss function is defined in Section 3.1.2. The production algorithm on censored SSPs is winrate distribution algorithm, in which winning probability function is estimated as a sigmoid function [29]. The results are presented in Table 2, and we observe the same correlation between log-loss and surplus again, which answers Q1. Notice that the log-loss is not applicable to the production algorithm since its definition of loss function is different from our model. Additionally, in comparison with non-censored training results in Table 1, there is a slightly drop in surplus performance lift for all distributions. This shows the importance of minimum winning price feedback in deep distribution network training which answers Q2.

# Model

As can be seen from the offline results corresponding to the cases with minimum winning price in Table 1 and the cases without minimum winning price in Table 2, log-normal distribution results in the lowest log-loss and the highest surplus. It indicates that among all the above distributions that we considered so far, lognormal fits the minimum winning price better. Therefore, we will choose log-normal as the output layer distribution in the online A/B test in Section 5.

## Network structure comparison

In this subsection, we present the results on comprehensive experiments on applying well-known click-through rate prediction models like FM, FwFM, DeepFM, Wide & Deep [10,13,17,27,28,30], to deep distribution network, as the deep distribution network structure, in learning the distribution of minimum winning price . The results are shown in Table 3 3: Performance of different network structures with lognormal as pre-defined distribution Based on the offline experiments results and online latency constraint, we eventually decide to use FwFM as the network structure and log-normal distribution for online experiments. However, we show the potential of more complex deep network structure, if the online latency requirements can be satisfied.

# ONLINE EXPERIMENTS

In this section, we will briefly introduce the real-time bid shading serving module we implemented, which serves billions of bid requests per day in one of the world's largest DSP. The online experimental results, including Return on Investment (ROI) for advertisers, are also presented, which further prove that deep distribution network outperforms other existing bid shading algorithms in literature.

## Bidding System Overview

Our DSP is a single platform that brings programmatic, premium, and its native marketplace inventory, formats, targeting and measurement together. We provide an overview of the bid shading aspects of the system, as illustrated in Figure 3.

When a user visits a web page with an ad opportunity, an ad request is sent to the SSP responsible for selling it. The SSP then packages available user and page information into bid requests and send them to multiple DSPs for auction. Upon receiving a bid request, within hundreds of milliseconds our bidding system goes through various stages such as fetching user profiles, ads targeting, For second-price auctions, this true value would be the bid price. For first-price auctions, we have an additional bid shading module, as shown on the right-hand side of the flow chart. In this bid shading module, historical bid information, including impressions and bid feedback from SSPs, are used to generate features and train bid shading models. The model is periodically updated and loaded into the real-time bidding system, and used to shade the true value to produce the final bid price, which, as part of the bid response, is sent back to the SSP.

The SSP collects bid responses from all participating DSPs, determines the winner, and sends an ad response to the web page. If our DSP wins the auction, an impression with the selected ad would be shown on the user's web page, and relevant user information would be sent back to us. The SSP also sends bid feedback to its bidders, but it may or may not include the minimum winning price.

## Online Evaluation Metrics

The most important key performance metrics for campaign delivery that the DSP system seeks to optimizes towards are CPM (Cost per thousand impressions), CPC (Cost per click) and CPA (Cost per action). For our online A/B test experiments of the bid shading algorithms described in this paper, we mainly focus on campaigns with one of those 3 optimization goal types, which cover more than 80% of total DSP revenue. For a given campaign spend budget, the DSP optimization system seeks to minimize the campaign's CPM, CPC or CPA as indicated by its optimization goal. For convenience, we use the term effective cost per event (eCPX) to denote either CPM, CPC or CPA. Since optimization goals are defined at the campaign level, there is a need to define metrics to measure impact of algorithm improvements (in our case bid shading) across multiple campaigns. Simple aggregations of events (e.g. actions) and cost across campaigns to define a simple aggregated eCPX metric are not good metrics, since a few campaigns can dominate such metrics if it turns out they have orders of magnitude more events than the rest of the campaigns, even though their cost (campaign spend) is as high as any other campaign's spend. Moreover, it's not fair to compare two algorithms when their spends are different since the one with more spend tends to have higher eCPX. Thus, we are going to introduce two novel online DSP business-related metrics: campaign level eCPX statistics, and Bidder Performance Index (BPI), which can be used to measure improvements in campaign performance and ROI for our advertisers.

### Campaign Level eCPX statistics.

A natural way to put together eCPX metrics across campaigns is to generate statistics on improvements measured at the campaign level, i.e. based on the eCPX of control and test buckets for each campaign. To avoid the asymmetry implied by the usual percentage difference in eCPX between control and test, we define the log of eCPX ratio for each campaign as the following, 

### Bidder Performance Index (BPI).

Minimizing eCPX for a given spend amount is equivalent to maximizing value or Return to advertisers under the same amount of spend (Cost), where Return to advertisers is the monetary value of the events (impressions, clicks or actions) driven by the campaign. This motivates the so-called BPI metric, defined as:

where Return and Cost can be aggregated across campaigns. The numerator shows the extra Return the new algorithm brings to the advertiser compensated by the extra cost it may also incur. Notice that it can be negative if the test algorithm is no better than the control one. The BPI metric is an aggregation-based type of metric that is less prone to be dominated by campaigns with very large number of events as explained before.

## Online A/B test results

After rolling out the deep distribution network algorithm with FwFM network structure and log-normal distribution on Adx, one of the largest SSPs, we were able to monitor its online performance by maintaining a percentage of traffic that was randomly allocated to each algorithm. There are thousands of campaigns running everyday in our DSP, the summary of these campaigns under our A/B test environment during 3 consecutive days is shown in Table 4.

It can be seen that for all goal types, the median of 𝑟 𝑒𝑐𝑝𝑥 are negative values, showing a overall better performance of our proposed algorithm. The weighted median, where the weights are the spend of each campaign, are also negative across all goal types. A majority of campaigns have a better eCPX performance on test bucket as can be seen from the third row of better campaign percentages. And These campaigns take up to 70% to 80% of the total spend. In all, from the online A/B test results, it can be shown that our proposed bid shading algorithm generates a significantly better performance than the current model in production. 

# CONCLUSIONS

In this work, we propose the deep distribution network for bid shading, which can be applied for both censored and non-censored first-price auctions. The parametric conditional distribution of minimum winning price is learnt through a FwFM network based on selected features of the bid request. For several well-known distributions, we proved that the resulting surplus function has a unique local maximum. Based on such property, an efficient golden-section search algorithm was applied at the real-time in finding the optimal bid price that maximizes expected surplus. In offline experiments, the proposed model out-performed existing state of the art bid shading algorithm on both censored and non-censored scenarios with respectively 9.7% and 5.3% surplus lift. Online A/B test showed that the proposed algorithm increases surplus by +14.3% and brings +2.4%, +2.4%, +8.6% ROI lift for impression based (CPM), click based (CPC), and conversion based (CPA) campaigns respectively. The deep distribution network has been successfully deployed in one of the biggest DSPs in the world, serving billions of bid requests every day. Another major advantage of our framework is that, the overall structure with a deep neural network and a parametric distribution output layer, can be easily generalized. In the future, we will continue exploring more powerful and run-time efficient neural network structures, combining with other single or multi mode distributions for further improved performance.

