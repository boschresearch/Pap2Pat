# I. INTRODUCTION

Localization and tracking of acoustic sources underwater is an important task for environmental monitoring and surveillance applications. Passive sonar relies on an array of hydrophones to listen for acoustic signals and uses them to estimate the locations of the sources that generated them. Underwater source localization via passive sonar is, nevertheless, difficult due to the complex interactions that sound undertakes as it propagates underwater. In shallow-water propagation environments, mutipath propagation leads to constructive and destructive acoustic interactions at the hydrophones that further exacerbate the localization problem. However, it is the same multipath propagation that creates enough diversity in the set of received acoustic signals at the hydrophone array to enable localization in range, depth, and azimuth [10].

Matched-field processing (MFP) refers to classical underwater source-localization techniques that rely on an acoustic model for characterizing the acoustic propagation in the environment [10]. It uses the adopted model to predict acoustic pressures at the hydrophones, a.k.a. replicas, for sources located on a grid of tentative source locations. Then, it "matches" the replicas to the acoustic measurements gathered by the array in order to obtain acoustic-power estimates at all grid locations. The resulting power estimates are subsumed by the so-called ambiguity surface (or ambiguity volume if the This work was funded by the Naval Innovative Science and Engineering Program at the Space and Naval Warfare Systems Center Pacific. sources' azimuths are also unknown). Source localization, thus, becomes a peak-picking problem where source-location estimates are mapped to grid points having high acousticpower estimates. Despite the merits of MFP, the quality of its location estimates continuous to be challenged by the presence of multiple sources and mismatch between the true propagation environment and the acoustic model used. These challenges can cause artifacts on the ambiguity surfaces that conceal the true source locations.

Tracking of underwater acoustic sources using passive sonar has traditionally been relegated to a post-processing task under the name of matched-field tracking (MFT). MFT algorithms construct a sequence of ambiguity surfaces to enable source localization at each point of the acoustic sources' trajectories. Tracks are obtained by knitting peaks of consecutive ambiguity surfaces together. A directed graph constructed by connecting the largest peaks on neighboring ambiguity surfaces is used to construct the family of allowed tracks [14]. The number of tracks grows combinatorially with the number of peaks used and, thus, quickly renders this approach computationally intractable.

Assumptions on the kinematics of the acoustic sources, e.g., maximum source velocity, constant source-speed and constant depth-trajectories, are used to reduce the number of tracks to be considered. The surviving tracks are scored based on their average acoustic-power estimates. When tracking a single source, the track with the largest score is chosen to be the true trajectory. Bucker extended the previous approach to enable coherent processing of broadband data [3]. Weighted approaches for scoring the tracks obtained from the graph have been proposed in [6], [13]. A limitation common to all these approaches is that they do not use prior information when generating the ambiguity surfaces. Moreover, these approaches are not well-suited to process data online since they are required to construct a batch of ambiguity surfaces for generating tracks.

More recently, Bayesian approaches for joint tracking and parameter inversion in the context of underwater source localization have been proposed [4]. Due to the nonlinear relationship between source locations and replicas, they use computationally-taxing Markov Chain Monte Carlo methods for estimating posterior probability distributions and are, thus, prohibited in the context of online underwater tracking. Sparsity-driven Kalman-filter approaches can be used for tracking acoustic sources over a grid [5]. These approaches use the entire localization grid postulated in MFP to define their state variable. They presume that only those grid entries corresponding to the locations of the sources take nonzero values. Hence, the state variable has a sparse structure. Direct application of these methods for underwater source localization is impractical due to the high dimensionality of the grid, and hence that of the state variable. Bayesian methods for tracking a sparse signal that build on the relevance vector machine have also been proposed [7], [11]. However, their associated computational cost is also high due to the size of their state-space variable and their need to maintain a covariance-matrix estimate for it.

In this work, we propose a sparsity-driven framework for broadband source localization via passive sonar. Per time instant, source localization maps (SLMs), one per frequency, are constructed. Only those points on the map that correspond to source locations take nonzero values. All other points in the SLMs are set to zero. Motivated by the fact that the source locations are presumed to be independent of frequency, coherence across SLMs is enforced to guarantee that their support coincides. SLMs can be combined to construct a broadband SLM. Different from previous approaches to construct SLMs [8], this novel approach considers a regularizer that forces the SLM estimator to use both the previous SLM obtained and the new measurement available. An iterative solver based on the proximal gradient (PG) is developed for constructing the SLMs. Numerical examples on real data illustrate the performance of the proposed method.

# II. PROBLEM STATEMENT

Consider K broadband acoustic sources radiating sound under water at F frequencies {ω f } F f =1 . Sources are able to move and their position at time t is denoted by {r k (t) ∈ R d } K k=1 , where d = 2 or d = 3. An array of N hydrophones is used to collect a time series of acoustic pressure measurements per hydrophone. The acoustic time series data is transformed to the frequency domain via a discrete-time Fourier transform. The Fourier coefficients at frequencies {ω f } F f =1 across all hydrophones are collected per frequency to vectors y f (t

, where y n f (t) denotes the Fouriercoefficient estimate corresponding to ω f at time t obtained from data gathered by the n-th hydrophone, and denotes the transpose operator.

It is presumed that a model characterizing the acoustic propagation in the environment is available.

were known, one could use it to compute model-predicted Fourier coefficients at the array for each source location, i.e., replicas. Let pk,f denote the normalized replica for a source located at r k (t) transmitting at ω f , where the normalization implies that pk,f 2 = 1. Each y f (t) can be modeled as

where f (t) ∈ C N denotes a zero-mean additive noise component, and s k,f (t) the Fourier coefficient at ω f of the spectrum corresponding to the k-th source acoustic signature at time t. Although replicas have been defined as time invariant, (1) can be adapted to capture spatiotemporal changes in the model used to generate the replicas. Given K and {y f ( t), ∀f } t t=0 , the goal of our underwater broadband tracking algorithm is to find estimates for {r k (t)} K k=1 . Even if all s k,f (t) in (1) were known, finding estimates for the source locations is difficult due to the nonlinear relationship between r k (t) and pk,f , which in most cases of interest is not available in closed form [10]. A possible approach to circumvent this issue is to introduce a grid of tentative source locations G := {r g } G g=1 with G max{KF, N }. Now the y f (t)'s at time t can be modeled as

where p g,f denotes the normalized replica corresponding to a source located at r g ∈ G, and s g,f (t) the Fourier coefficient at ω f of the spectrum corresponding to the acoustic signature of the source located at r g ∈ G at time t.

Since G KF most of the s g,f (t)'s are expected to be zero. Only those few s g,f (t)'s that correspond to the true source locations should take nonzero values. Let

Once an estimate for S(t) is available, a broadband SLM can be obtained by plotting the pairs (r g , ς g (t) 2 ) for all r g ∈ G, where ς g (t) := [s g,1 (t), . . . , s g,F (t)] ∈ C F comprises the entries of the g-th row of S(t). Source location estimates {r k (t)} correspond to the location of the K-largest peaks in the broadband SLM. In the following section, an estimator for S(t) that captures the group sparsity inherent to the rows of S(t) and the temporal dependency between SLMs corresponding to consecutive time instances is proposed.

# III. SPARSITY-DRIVEN TRACKING OF ACOUSTIC SOURCES

An iterative estimator for S(t) is proposed in this section. The estimator uses the previously estimated S(t -1) to capture the temporal dependency between source locations at consecutive time instances. Per time t, an estimate Ŝ(t) = [ŝ 1 (t), . . . , ŝF (t)] for S(t) is obtained as

where S := [s 1 , . . . , s F ], ς g denotes the g-th row of S, P f := [p 1,f , . . . , p G,f ] ∈ C N ×G the matrix of replicas for ω f , and λ, μ > 0 tuning parameters. Note that (3) is a regularized least squares regression problem. The regularization term scaled by μ encourages group sparsity on the rows of Ŝ(t), with μ controlling the number of nonzero rows in Ŝ(t). The regularization term scaled by λ encourages estimates ŝf (t) to be close to ŝf (t -1), ∀f , with λ controlling the emphasis placed on ŝf (t -1) when estimating s f (t), ∀f .

Problem (3) can be written as a real-valued convex optimization problem after representing all complex-valued variables by the direct sum of their real and imaginary parts. To this end, let us introduce the following notation yf (t) := [Re{y f (t)} , Im{y f (t)} ] , sf := [Re(s f ) , Im(s f ) ] , S := [s 1 , . . . , sF ], and

where Re(•) (Im(•)) denotes the real-part (imaginary-part) operator. Matrix S can be alternatively viewed in terms of its rows as S = [ς 1 , . . . , ς2G ] where the first (last) G rows correspond to the real (imaginary) parts of the rows of S. Problem ( 3) is equivalent to the following convex optimization problem

(5)

where vg := [ς g , ς g+G ] ∈ R 2F (v g (t -1)) corresponds to the direct sum of the real and imaginary parts of ς g (ς g (t -1)). Note that the minimizer Ŝ(t) of ( 3) can be obtained as a function of S(t) as Ŝ(t) = S1:G (t) + j SG+1:2G (t), where j := √ -1 and Sg1:g2 (t) is a matrix which comprises rows

Although ( 5) is a convex optimization problem that can be solved via interior point methods, such a solver would entail high computational complexity due to the high dimensionality of S and fail to exploit the sparse structure of S. The ensuing section presents a PG solver for (5) that capitalizes its structure to obtain closed-form updates.

Remark 1 (Robustness to model mismatch): Problem (3) can be written as

where all terms independent of S have been removed from the cost. The terms λ/2 • sf 2 2 , f = 1, . . . , F , in the regularizer are known to induce resilience to model mismatch into the estimate S(t) [8], [9]. From this vantage point, λ > 0 corresponds to the variance of a random perturbation affecting each replica, which depends on the mismatch between the true propagation environment and the model used to generate the replicas. The linear terms -λv g v g (t -1) encourage estimates vg (t) to be close to vg (t -1). In particular, as the model mismatch increases, and thus the reliability of the replicas decreases, (6) naturally steers its attention towards the prior SLM estimates subsumed by the vg (t -1)'s.

# IV. PG SOLVER FOR SPARSE TRACKING

In this section a PG algorithm for solving (5) that capitalizes its sparse structure is developed. Problem (5) can be written as min S h( S) + μ G g=1 vg 2 , where h( S) := 1/2

] denotes the continuously differentiable portion of the cost. Note that the gradient of h( S) is Lipschitz continuous with Lipschitz constant L h := max f =1,...,F σ max (P f P f + λI 2G ), where σ max (P f P f ) denotes the largest singular value of P f P f . That is, ∇h( S1 ) -∇h( S2 ) 2 ≤ L h S1 -S2 F , where ∇h( Sl ) denotes the gradient of h with respect to S evaluated at Sl . Note that L h can be obtained at a reduced computational cost by using the singular values of the P f 's as

The PG method can be interpreted as a majorizationminimization method relying on a majorizer H( S; Z) for h, where Z := [z 1 , . . . , z F ] ∈ R 2G×F is an auxiliary matrix. The majorizer H satisfies: (i) H( S; Z) ≥ h( S), ∀ S; and, (ii) H( S; Z) = h( S) for Z = S. The specific H used by the PG method is

where

, and ∇h f (z f ) denotes the gradient of h f with respect to sf evaluated at z f . That the majorizer in (7) satisfies conditions (i) follows from the fact that the gradient of h is Lipschitz continuous [2, Prop. A.24], and that it satisfies (ii) follows after setting Z = S in (7). With i denoting the PG iteration index, the PG algorithm iteratively solves

where S[i] (t) denotes the PG estimate for S(t) at iteration i.

From an algorithmic viewpoint, it is convenient to write H as a function of the vg 's. After performing some algebraic manipulations on H and dropping all terms independent of S, (8) can be written as

where

is a gradient-descent step, with step-size 1/L h , for the g-th row of S, and the entries of d

, which correspond to those of the gradient of h f with respect to vg , are

Algorithm 1 PG solver for (5).

Require: Tuning parameters μ > 0 and S(t -1).

1: for i = 1, 2, . . . , do

## 2:

{These updates can be parallelized} 3:

for g = 1, . . . , G do 4:

Compute (11).

## 5:

Compute w

[i-1] g (t) via (10).

## 6:

Update v[i] g (t) via (13).

7:

end for 8: end for where r 9) is often called the proximal operator of μ vg 2 with parameter 1/L h .

Problem ( 9) is decomposable across vg 's. Thus, per iteration i, the PG update in ( 8) can be performed in parallel for every pair of rows of S comprised in each vg via

The cost in ( 12) is convex, and non-differentiable due to vg 2 . Despite the non differentiability of its cost, ( 12) can be solved in closed form and its solution in this case is

where (•) + = max{0, •}. Equation ( 13) follows readily from the Karush-Kuhn-Tucker (KKT) conditions for (12) where the notion of subdifferential is used to characterize v[i] g (t) [2]. The resulting PG algorithm is summarized as Algorithm 1. Per iteration, the PG update entails O(NGF ) scalar operations required for computing d (11). The algorithm terminates when

• denotes the Frobenius norm and s is a small positive threshold, e.g., s = 10 -5 . Algorithm 1 converges to the solution of ( 5) and features a worst-case convergence rate of O(1/i) [1]. Thus, its convergence may be slow in practice, requiring up to several hundreds of iterations to achieve a highly accurate solution. Nevertheless, it has been observed that the support of S[i] (t) can be correctly identified using fewer iterations (in the order of 50 iterations). Moreover, it is possible to develop an accelerated version of Algorithm 1 featuring worst-case convergence rate of O(1/i 2 ), see [1] and references therein.

# V. NUMERICAL TESTS ON SWELLEX-3

The performance of the proposed Algorithm 1 is illustrated using data from the third Shallow-Water Evaluation Cell Experiment (SWellEX-3) dataset. In SWellEX-3, a towed source transmitting at 10 frequencies {53+16k} 9 k=0 (all in Hertz) and a vertical line array with 64 hydrophones collecting acoustic data were used. In this analysis, the array was subsampled and only 9 hydrophones evenly spaced over the length of the array were used. These hydrophones were 11.25 m apart,  having a total aperture of 90 m with the bottom element 6 m above the seafloor. The acoustic environmental model, a short description of relevant environmental parameters, and the array configuration used in SWellEX-3 are given in Fig. 1. A grid with G = 20, 000 locations spanning radial distances 0-10 km and depths 0-198 m was used. The grid's radial and vertical spacing were 50 m and 2 m, respectively. All replicas were computed with the KRAKEN normal-mode program [12].

MFT was used as a baseline for comparison [13]. Despite its high computational complexity, MFT yields accurate track estimates for the single source case. Ambiguity surfaces generated via Bartlett MFP were used to construct partial linear trajectories, also known as tracklets. A total of 8 ambiguity surfaces were used to construct each tracklet. Each ambiguity surface accounts for 13.65 seconds of recorded data, and thus each tracklet corresponds to 109 seconds of recorded data. Note that there is a 50% overlap between consecutive tracklets. Figs. 2a and 2b illustrate the depth and range tracks obtained by MFT.

Figs. 2c and 2d illustrate the tracks obtained after Algorithm 1 to construct the SLMs. Per time t, the ranges and depths of all peaks are plotted. In this particular tests, the trajectory was broken to three different intervals for which different (λ, μ) pairs were chosen. Although the tracks obtained give a coarse approximation to those followed by the source, we expect that by dynamically adjusting the selection of, e.g., μ the gaps in the tracks can be removed. Note that these gaps appear because the choice of μ at those particular time instances was too high. Note that both MFT and the proposed method fail to track the source after t = 65 min. due to the severe mismatch between  the environment and the model used to generate the replicas (see [9]).

In order to simulate the presence of two sources using the SWellEX-3 dataset, data corresponding to the portions of the trajectory between 0-25 mins. and 40-65 mins. were combined after being rescaled to compensate for the signal-to-noise ratio difference between the two portions of the trajectory. In this case, the computational complexity of MFT, and correspondingly its execution time, increased dramatically since the algorithm connected all combinations of pairs of peaks across ambiguity surfaces. MFT was not able to distinguish the two sources possibly due to the width of the peaks on the ambiguity surfaces. Fig. 3 illustrate the performance of the proposed algorithm when used to track the location of the two sources. Similarly to the one-source case, different (λ, μ) pairs were chosen for different intervals of the trajectory. Although the trajectories of the two sources can be observed in range, it is difficult to separate the two sources in depth. As in the one source case, dynamic adjustment of the parameters is expected to help improve on the quality of the tracks obtained.

# VI. CONCLUSIONS

This work proposed a tracking algorithm for multiple acoustic sources using passive sonar. The tracks are constructed based on SLMs that reveal the locations of the sources over a grid of tentative source locations. The proposed estimator for the SLMs performs coherent processing of broadband acoustic measurements, capitalizes on the sparse structure of the SLMs, and uses the prior SLM estimate as a means to capture temporal information about the locations of the sources. The dynamic selection of tuning parameters for the estimator remains as an open challenge. The proposed algorithm was used to localize a towed broadband source in data collected during SWellEX-3. Numerical experiments on a simulated two-source case using SWellEX-3 data were also shown. 

