# INTRODUCTION

The machine learning community has greatly benefited from open and public datasets [Chapelle and Chang, 2011, Real et al., 2017, Fast and Horvitz, 2017, Kong et al., 2020]. Unfortunately the privacy concern of data release significantly limits the feasibility of sharing many rich and useful datasets to the public, especially in privacy-sensitive domains like health care, finance, and government etc. This restriction considerably slows down the research in those areas as well as the general machine learning research given many of today's algorithms are data-hungry. Recently, legal and moral concerns on protecting individual privacy become even greater. Most countries have imposed strict regulations on the usage and release of sensitive data, e.g. CCPA [Legislature, 2018], HIPPA [Act, 1996]  protecting privacy and promoting research drives the community as well as many ML practitioners into a dilemma.

Differential privacy (DP) [Dwork, 2011, Dwork et al., 2006, 2014, Sheffet, 2017, Lee et al., 2019, Xu et al., 2017, Kenthapadi et al., 2012] is shown to be a promising direction to release datasets while protecting individual privacy. DP provides a formal definition of privacy to regulate the trade-off between two conflicting goals: protecting sensitive information and maintaining data utility. In a DP data release mechanism, the shared dataset is a function of the aggregate of all private samples and the DP guarantees regulate how difficult for anyone to infer the attributes or identity of any individual sample. With high probability, the public data would be barely affected if any single sample were replaced.

Despite the ongoing progress of DP data release, the majority of the prior work mainly focuses on the single-party setting which assumes there is only one party that would release datasets to the public. However in many real-world scenarios, there exist multiple parties who own data relevant to each other and want to collectively share the data as a whole to the public. For example, in health care domain, some patients may visit multiple clinics for specialized treatments (Figure 1), and each clinic only has access to its own attributes (e.g. blood test and CT images) collected from the patients. For the same set of patients, attributes combined from all clinics can be more useful to train models. In general, the multi-party setting assumes multiple parties own disjoint sets of attributes (features or labels) belonging to the same group of data subjects (e.g. patients).

One straightforward approach to release data in a multi-party setting is combining data from all parties in a centralized place (e.g. one of the data owners or a third-party), and then releasing it using a private single-party data release approach. However, in a privacy-sensitive organization like a clinic, sending data to another party is prohibited by policy. An alternative approach is to let each party individually release its own data to the public through adding sample-wise Gaussian noise, and then ML practitioners can combine the data together to train models. However the resulting models trained on the data combined in this way would show a significantly lower utility compared to the models trained on non-private data (confirmed by experiments in Section 5).

To bridge this utility gap, we propose new algorithms specifically designed for multi-party setting.

In summary, we study DP data release in multi-party setting where parties share attributes of the same data subjects publicly through a DP mechanism. It protects the privacy of all data subjects and can be accessed by the public, including any party involved. To this end, we propose the following two differentially private algorithms, both based on Gaussian DP Mechanism [Dwork et al., 2014] within the context of linear regression. First, in De-biased Gaussian Mechanism for Ordinary Least Squares (DGM-OLS), each party adds Gaussian noise directly to its data. The learner with the public data is able to remove a calculated bias from the Hessian matrix. However, we show that bias removal brings the small eigenvalue problem. Hence, we propose the second method Random Mixing prior to Gaussian Mechanism for Ordinary Least Squares (RMGM-OLS).

A random Bernoulli projection matrix is shared to all parties, and each party uses it to project its data along sample-wise dimension before adding Gaussian noise. We prove that both algorithms are guaranteed to produce solutions that asymptotically converge to the optimal solutions (i.e. non-private) as the dataset size increases. Through extensive experiments on both synthetic and real-world datasets, we show the latter method achieves the theoretical claims and outperforms the first method that naively adapts Gaussian mechanism.

# PRELIMINARY

A sequence {X n } of random variables in R d is defined to converge in probability towards the random variable X if for all β > 0,

The norm notation • denotes 2 norm in our paper. We denote this convergence as plim n→∞ X n = X.

Differential privacy (DP; [Dwork et al., 2006[Dwork et al., , 2014]]) is a quantifiable and rigorous privacy framework, which is formally defined as follows.

Definition 1 ((ε, δ)-differential privacy). A randomized mechanism M : D → R with domain D and range R satisfies (ε, δ)-differential privacy if for any two adjacent datasets D, D ∈ D, which differ at exactly one data point, and for any subset of outputs S ⊆ R, it holds that

Gaussian mechanism [Dwork et al., 2014] is a post-hoc mechanism to convert a deterministic real-valued function f : D → R m to a randomized algorithm with differential privacy guarantee. It relies on sensitivity of f , denoted by S f , which is defined as the maximum difference of output f (D) -f (D ) . We define Gaussian mechanism for differential privacy as below.

Lemma 1 (Gaussian mechanism). For any deterministic real-valued function f : D → R m with sensitivity S f , we can define a randomized function by adding Gaussian noise to f :

where R is sampled from a multivariate normal distribution

To simplify notations, we define σ ε,δ := √ 2 log(1.25/δ) ε

.

Johnson-Lindenstrauss lemma (JL; [Johnson andLindenstrauss, 1984, Achlioptas, 2003]) is a technique to compress a set of vectors

it is able to approximately preserve the inner product between any two vectors in the set S with high probability. We specifically introduce the Bernoulli version of JL Lemma, which is extended from Theorem 1.1 in Achlioptas [2003].

Lemma 2 (JL Lemma for inner-product preserving (Bernoulli)). Suppose S is an arbitrary set of l points in R d and suppose s is an upper bound for the maximum 2 -norm for vectors in S. Let B be a k × d random matrix, where B ij are independent random variables taking value from 1 or -1 with probability 1/2 respectively. With the probability

# NOTATION AND PROBLEM SETUP

Notations. Denote D j , j = 1, • • • , m, as data matrices for m parties, where D j ∈ R n×dj and m ≥ 2. They are aligned by the same set of subjects but have different attributes and they have the same number of samples. Define d+1) as the collection of all datasets, where

We define d by subtracting 1 from the total number of attributes because one column is label which we need to treat separately. Define d max = max j∈[m] d j , and D i as the i-th row of D, we make the following assumption on data distribution:

Dataset release algorithm. A private multi-party data release algorithm needs to protect both inter-party and intraparty communications. The general workflow of our proposed algorithms is designed as the following:

1. Pre-generate random variable B. The pre-generated one or more random variables will be shared among parties. 2. Privatize the dataset locally with the algorithm A priv .

Each party applies the same privatizing algorithm A priv that takes the local dataset D j ∈ R n×dj and the random matrix B as the inputs and then outputs k (predefined) "encrypted" samples D pub j := A priv (D j ; B) ∈ R k×dj . 3. Release the dataset. All parties jointly release d+1) to the public.

Note that we need to specially design random variable B and the privatizing algorithm A priv , which we will introduce in the next section. In addition, the random variable B allows the dependencies between the randomized output from all parties, which can be utilized to guarantee the final utility.

Privacy constraint. Since the public will observe the released dataset D pub , for each j ∈ [m], D pub j should not leak the information of the private dataset D j . Formally we require ∀j ∈ [m], A priv (D j ; B) is differentially private, where two neighbouring datasets D j and D j differ at one row (sample).

However the multi-party setting requires more than the above guarantee because each party j = j not only observes D j but also the shared random variable B.

Thus we need to further require that given B, each party j cannot infer information about other private datasets D j . In terms of differential privacy, it is required that condition on B for any possible sample value I, A priv (D j ; B) is (ε, δ)-differentially private, i.e. for any two neighbouring datasets D j and D j and B, we have

Utility target. We aim to guarantee the performance of arbitrary linear regression task (arbitrarily selected label and features) on the joint released dataset

Out of the notation simplicity, we assume the label in the linear regression task is the last attribute, and the features are the rest of the attributes. Under this assumption, the joint private dataset D can be written as [X, Y ], where X ∈ R n×d is the private feature matrix and Y ∈ R n is the private label vector. Similarly the public dataset D pub can be written as [X pub , Y pub ], where X pub ∈ R k×d and Y pub ∈ R k .

We define the loss function by the expected squared loss:

where the data point is sampled from the distribution P in Assumption 1. We make two more assumptions for the distribution P: the standard normalization and the no perfect multicollinearity assumption. The latter is common in the literature of linear regression [Farrar andGlauber, 1967, Chatterjee andHadi, 2006].

Assumption 2. The absolute values of all attributes |D ij | are bounded by 1.

Assumption 3. E (x,y)∼P xx is positive definite.

Under Assumption 3, derived by setting ∇ w L(w; P) = 0, the optimal solution w * to the loss in Equation 1 has the following explicit form:

The utility target (for the trained linear regression model) is determined by our release algorithm (B, A priv ). For a given public dataset D pub released by our algorithms, we define our utility target as the existence of a training algorithm A lr that achieves the asymptotic property for the trained model weights ŵn := A lr D pub as the dataset size n → ∞.

The asymptotic property is commonly studied in differential privacy [Chaudhuri and Hsu, 2011, Bassily et al., 2014, Feldman et al., 2020] and we restate it as follows: ŵn converges to w * in probability as the size of dataset n increases, i.e. ∀β > 0, lim n→∞ P [ ŵnw * > β] = 0. The randomness from the above property comes from data sampling P, dataset release algorithm (B, A priv ), and the training algorithm A lr .

# METHODOLOGY

We now describe our data release algorithms which both satisfy the differential privacy and yield asymptotically optimal solutions to the linear regression task. We start with the first algorithm De-biased Gaussian Mechanism for Ordinary Least Squares (DGM-OLS), which directly applies Gaussian mechanism when releasing the data and then de-biases

The party j computes D dgm j := D j + R j , where R j ∈ R n×dj is a random Gaussian matrix and elements in R j are i.i.d sampled from N 0, 4d max • σ 2 ε,δ . 4: end for 5: Return:

Training Algorithm

the Hessian matrix when training the model. However the de-bias operator introduces the possible inverse of a matrix with small eigenvalues, which severely hurts the performance of the learned model. We therefore propose a novel dataset release algorithm rather than the directly application to Gaussian mechanism -Random Mixing prior to Gaussian Mechanism for Ordinary Least Squares (RMGM-OLS).

The model learned from the corresponding released public dataset is also guaranteed to be asymptotically optimal, and, more importantly, avoids the problem of small eigenvalues.

## DE-BIASED GAUSSIAN MECHANISM (DGM-OLS)

The De-biased Gaussian Mechanism for Ordinary Least Squares (DGM-OLS) includes the dataset release algorithm and the corresponding training algorithm. Algorithm 1 shows the overview and we will introduce them next.

# Dataset release algorithm. Each party directly applies

Gaussian mechanism to their own dataset

to satisfy the differential privacy. Consider two neighboring data matrices D j and D j differing at exactly one row with the row index i. Implied by Assumption 2, we can compute the sensitivity of the data matrix D j :

Then each party independently adds a Gaussian noise R j to D j . Entries in R j are i.i.d sampled from Gaussian distribution N (0, 4d max σ 2 ε,δ ). The dataset release algorithm meets the privacy constraints in section 3. No random matrix B is shared among dif-ferent parties. Lemma 1 guarantees that D dgm j is (ε, δ)differentially private w.r.t. D j for any 0 < ε ≤ 1, δ > 0.

Training algorithm. Given the dataset released through the above algorithm, there exists an asymptotic linear regression solution. Denote the feature matrix and the label vector of the private and public joint dataset as d+1) and split R into R X and R Y representing the additive noise to X and Y respectively.

Consider the ordinary least square solution for the public data X dgm and Y dgm , whose explicit form is:

(2)

Compared with our target solution

by the concentration of bounded random variables and multivariate normal distribution. Nevertheless, there is a gap between plim n→∞ 1 n X dgm X dgm and E (x,y)∼P xx :

where the last equation again holds by the concentration of bounded random variables and multivariate normal distribution. To reduce the bias 4d max σ 2 ε,δ • I, we can revise the solution computation in Equation 2 to ŵdgm n defined as

The first term is estimated for the inverse of the Hessian matrix E (x,y)∼P xx , which we denote as ( Ĥdgm n ) -1 . The asymptotic optimality for the solution ŵdgm n is implied by the theorem below and the proof is in the Appendix.

Theorem 1. When β ≤ c for some variable c that is dependent of σ ε,δ , d, and P, but is independent of n,

Problem of small eigenvalues. The expectation of Ĥdgm n is a positive definite matrix given Assumption 3, but the sample of Ĥdgm n itself is not guaranteed. With a certain probability, it has small eigenvalues that might lead to explosion when computing its inverse. In our experiments (section 5), we find that Ĥdgm n suffers from the small eigenvalues even if n is as large as 10 6 . As a result, the model utility is much more inferior than what is guaranteed theoretically. This motivates us to design the second algorithm.

Algorithm 2 RMGM-OLS Dataset Release

The first party pre-generates a k × n random matrix B where all entries in B are i.i.d. sampled from the distribution with probability 1/2 for 1 and 1/2 for -1.

Then first party sends the random matrix sample B to all parties. 3:

The party j computes (D rmgm ) j := BD j / √ k+R j , where R j is a k × d j random matrix and all elements in R j are i.i.d. sampled from the multivariate normal distribution N 0, 4d max σ 2 ε,δ . 5: end for 6: Return:

Training Algorithm

## RANDOM MIXING PRIOR TO GAUSSIAN MECHANISM (RMGM-OLS)

In previous method's dataset release stage, when we directly add the Gaussian additive noise R to the data, in order to guarantee DP, the norm of the noise needed has to be the same order (in n) as the norm of the data matrix D. Both D and R have norm in Θ( √ n). Thus later in the training stage, the additive noise R when compared to the data matrix X would not diminish as n → ∞ and we have to subtract 4d max σ 2 ε,δ • I from X dgm X dgm to remove this additive noise in order to obtain the optimal model weights. This subtraction is the problematic part that brings training instability (small eigenvalues in the Hessian matrix).

Instead, we can avoid such subtraction in the training stage by imposing a smaller noise in the data release stage. If we can design the data release stage properly, so that the addictive noise has relatively smaller order in n than D, in the later training stage, the learner would no longer need the problematic de-biasing step.

Algorithm 2 shows the full details of Random Mixing prior to Gaussian Mechanism for Ordinary Least Squares (RMGM-OLS). We now explain the design of data release and training algorithm based on the above insights.

Dataset release algorithm. Suppose b is an ndimensional vector in {-1, 1} n . For any two neighbouring daasets D j and D j that are different at row index i, the sensitivity of b

Moreover, when B ∈ {-1, 1} k×n , BD j / √ k has sensitivity 2 √ d max as well.

We now introduce the data release algorithm. Suppose all parties are sharing a random matrix B ∈ {-1, 1} k×n , where all elements in B are i.i.d. sampled from the distribution with probability 1/2 for 1 and 1/2 for -1. Then we define the local computation for each party j:

where R j is a k × d j random matrix and all elements in R j are i.i.d. sampled from the multivariate normal distribution N 0, 4d max σ 2 ε,δ . Gaussian mechanism guarantees for any fixed B ∈ {1, -1}

k×n , (D rmgm ) j is (ε, δ)-differentially private w.r.t. the dataset D j for 0 < ε ≤ 1, δ > 0.

Importantly, now the addictive noise R j is relatively small than BD j / √ k. The order of R j is Θ(k) while the order

, the additive noise compared to the original data matrix D will diminish as n → ∞. This implies that the standard ordinary least square solution to the public dataset [X rmgm , Y rmgm ] would converge to the optimal solution w * without special subtraction.

Training algorithm. Given the feature matrix X rmgm and the label vector Y rmgm from the released dataset, we show that the vanilla ordinary least square solution

is asymptotically optimal, i.e. plim n→∞ ŵrmgm n = w * .

To prove the above asymptotic optimality, we show plim n→∞ (X rmgm ) X rmgm = E (x,y)∼P xx and plim n→∞ (X rmgm ) Y rmgm = E (x,y)∼P [x • y] respectively, and together they prove the optimality.

.

We informally show how each term converges to 0 as n → ∞:

ε,δ • I will converge to 0 as n → ∞. Notice that the above convergence relies on the proper selection of k. There exists a trade-off: larger k leads to better convergence rate of the first term, but worse rate for the diminishing of additive noise -the third term. The following theorem shows the exact asymptotic rate:

Theorem 2. When β ≤ c for some variable c that is dependent of d and P, but independent of σ ε,δ , n, we have

, then

• O (min {1, β}) + Õ(1) .

In the theorem, k is selected to balance kβ 2 d 2 and

To achieve the optimal rate for f (β) with any fixed β, the optimal k is chosen as

Comparison with DGM-OLS. The near-zero eigenvalue issue is solved since (X rmgm ) X rmgm 0 holds naturally by its definition. Moreover, although the convergence rate of n is sacrificed, the orders in d, d max and σ ε,δ are much improved. In section 5 we show that the RMGM-OLS outperforms DGM-OLS on both synthetic datasets even when n is as large as 3 × 10 6 .

# EXPERIMENTAL EVALUATION

In this section, we evaluate DGM-OLS and RMGM-OLS on both synthetic and real world datasets. Our experiments on synthetic dataset are designed to verify the theoretical asymptotic results in section 4 by increasing the training set size n. We further justify the algorithm performance on five real-world datasets, four from UCI Machine Learning Repository 1 [Dua and Graff, 2017] and one from kaggle.

1 https://archive-beta.ics.uci.edu/ml/ datasets 5.1 EXPERIMENT SET-UP Algorithm set-up. We evaluate both DGM-OLS and RMGM-OLS. For k in RMGM-OLS, we set k = √ n σ ε,δ in synthetic dataset experiments and select the best k from {10 2 , 3×10 2 , 10 3 , 3×10 3 , 10 4 } in real-world dataset experiments. Because of the numerical instability of computing Hessian inverse mentioned early, we add small λ • I with λ = 10 -5 to all Hessian matrices.

Baseline. In addition, we consider the following baselines to help qualify the performance of proposed algorithms.

• OLS: The explicit solution for linear regression given training data (X, Y ) and serves as the performance's upper bound for private algorithms, i.e. non-private solution. 

X bgm Y bgm . In other words, it is DGM-OLS without training debiasing.

Evaluation metric. In the experiments on synthetic datasets, we estimate the probability of the 2 distance between the model weights ŵn from each algorithm or baseline and the ground truth model weight w * : P ( ŵnw * > β) .

We also evaluate the expectation of the 2 distance between weights for different algorithms:

If an algorithm is asymptotically optimal, we can see both P ( ŵnw * > β) and E ŵnw * converge to 0 when n increases.

For the experiments on real world datasets, we evaluate learned models ŵn by the mean squared loss on the test set.

## EVALUATION ON SYNTHETIC DATASETS

Data generation. We define the feature dimension d = 10. Each weight value of the ground truth linear model w * is independently sampled from uniform distribution between -1/d and 1/d. A single data point (x, y) is sampled as the following: each feature value in x is independently sampled from a uniform distribution between -1 and 1; label y is computed as (w * ) x. Two assumptions for the data distribution P, Assumption 2 and Assumption 3, can be verified. Moreover, we set 6 parties in total, 5 of which have 2 attributes and the remaining one has 1 attribute. Results. We vary the training set size n ∈ {10 4 , 3 × 10 4 , 10 5 , 3 × 10 5 , 10 6 , 3 × 10 6 } and privacy budget ε ∈ {1, 0.3, 0.1} with fixed δ = 10 -5 . We estimate the P [ w n -w * > β] and E w n -w * for different algorithms with 1000 random seeds. stays at 1 for all n. Such results are expected in BGM-OLS's convergence:

ε,δ • I, which introduces a non-diminishing bias 4d max σ 2 ε,δ • I. Next, we compare DGM-OLS and RMGM-OLS. RMGM-OLS outperforms DGM-OLS at both the convergence of probability P [ w n -w * > β] (the first three figures in Figure 2) and the expected distance E [ w n -w * ] (the last figure in Figure 2). RMGM-OLS shows the asymptotic tendencies in all values of β when ε = 1.0. Although DGM-OLS has better rate at n than RMGM-OLS theoretically, n = 3 × 10 6 is not large enough to show the asymptotic tendencies for DGM-OLS. DGM-OLS is even much worse than BGM-OLS, which is almost random guess. It is caused by the small eigenvalue issue discussed in section 4. To illustrate it, Figure 3 (a) shows the scatter plot, where the x-axis is minimum eigenvalues of the Hessian matrix Ĥn and y-axis is the distance between our solutions and the optimal solution ŵnw * . Each point is processed by a different random seed for DGM-OLS and BGM-OLS when n = 10 6 and ε = 1.0. ŵnw * and the minimum absolute eigenvalues of Ĥn have a strong positive correlation. With a certain probability, the minimum eigenvalue of DGM-OLS is smaller than 10 -2 and corresponding w n -w * is larger than 10.

Overall RMGM-OLS has the best empirical performance across various settings of ε and n on the synthetic data, as its asymptotically optimality is verified and it consistently outperforms two other private algorithms when n is large enough. Though DGM-OLS seems to have stronger theoretical guarantee in the aspect of rate in n, its poor empirical performance comes from two aspects: 1. small eigenvalues occur due to the design of the training algorithm; 2. extremely large n is necessary to show the asymptotic optimality due to the worse rates of d, d max and σ ε,δ .

## EVALUATION ON REAL WORLD DATASETS

Dataset. We experiment with five datasets:

• Insurance [Lantz, 2019]: predicting the insurance premium from features including age, bmi, expenses, etc. • Bike [Fanaee-T and Gama, 2014]: predicting the count of rental bikes from features such as season, holiday, etc. • Superconductor [Hamidieh, 2018]: predicting critical temperature from chemical features. • GPU [Ballester-Ripoll et al., 2019, Nugteren andCodreanu, 2015]: predicting Running time for multiplying two 2048×2048. matrices using a GPU OpenCL SGEMM kernel with varying parameters. • Music Song [Bertin-Mahieux et al., 2011]: predicting the release year of a song from audio features.

We split the original dataset into train and test by the ratio 4 :

1. The number of training data n, the number of features d and the number of parties are listed in Table 1. The attributes are evenly distributed among parties. All features and labels are normalized into [0, 1].

Results. For each dataset, we evaluate OLS and three differentially private algorithms by the mean squared loss on the test split. Table 1 shows the results for ε ∈ {0.1, 0.3, 1.0} and δ = 10 -5 . We can check that the loss of DGM-OLS is usually much larger than others and RMGM-OLS achieves the lowest losses for most cases (12 out of 15). Moreover, Figure 3 (b) shows that DGM-OLS has the small eigenvalue problem as well in the real world dataset experiments. These results are consistent with the results on synthetic dataset. We therefore recommend RMGM-OLS as a practical solution to privately release the dataset and build the linear regression models.

# RELATED WORK

Differentially private dataset release. Many recent works [Sheffet, 2017, Gondara and Wang, 2020, Xie et al., 2018, Jordon et al., 2018, Lee et al., 2019, Xu et al., 2017, Kenthapadi et al., 2012] study the differentially private data release algorithms. However, those algorithms either only serve for data release from a single-party [Sheffet, 2017, Gondara andWang, 2020], or focus on the feature dimension reduction or empirical improvement [Lee et al., 2019, Xu et al., 2017, Kenthapadi et al., 2012], which is orthogonal to the study of asymptotical optimality w.r.t. dataset size. In Sheffet [2017] and Gondara and Wang [2020], the random Gaussian projection matrices in their method contribute to the differential privacy guarantee, hence the sharing of projection matrix would violate the privacy guarantee between parties. Nevertheless, without sharing this projection matrix, the utility cannot be guaranteed anymore. In Xie et al.

[2018] and Jordon et al. [2018], they train a differentially private GAN. However, it is not obvious to rigorously privately share data information during their training when each party holds different attributes but same instances. Lee et al. [2019] proposes a random mixing method and also analyzes the linear model. However, the way they mix only works for realizable linear data. It is not able to be extended to the general linear regression and the asymptotic optimality guarantee. Xu et al. [2017] and Kenthapadi et al. [2012] focus on the feature dimension reduction, which is orthogonal to the study of asymptotical optimality w.r.t. dataset size.

Asymptotically optimal differentially private convex optimization. A large amount of work study differentially private optimization for convex problems [Bassily et al., 2014, 2019, Feldman et al., 2020] or particularly for linear regression [Sheffet, 2017, Kasiviswanathan et al., 2011, Chaudhuri and Hsu, 2012]. They mainly differ from our work in the sense that their goal is to release the final model while ours is to release the dataset.

Linear regression in vertical federated learning. Linear regression is a fundamental machine learning task. Hall et al. [2011], Nikolaenko et al. [2013], Gascón et al. [2017] studying linear regression over vertically partitioned datasets based on secure multi-party computation. However, cryptographic protocols such as Homomorphic Encryption [Hall et al., 2011, Nikolaenko et al., 2013] and garbled circuits [Nikolaenko et al., 2013, Gascón et al., 2017] lead to heavy overhead on computation and communication.

From this aspect, DP-based techniques are more practical. Table 1: Mean squared losses on real world datasets. RMGM-OLS achieves the lowest losses in most settings (12 out of 15).

# CONCLUSION

We propose and analyze two differentially private algorithms under multi-party setting for linear regression, and theoretically both of them are asymptotically optimal with increasing dataset size. Empirically, RMGM-OLS has the best performance on both synthetic datasets and real-world datasets, while extremely large training set size n is necessary for DGM-OLS. We hope our work can bring more attention to the need for multi-party data release algorithms and we believe that ML practitioners would benefit from such effort in the era of privacy.

Future work. We focus on linear regression only, and one future direction is to extend our algorithm to classification, e.g. logistic regression, while achieving the same asymptotic optimality. In addition, we assume different parties own the same set of data subjects. Another future direction is to relax this assumption: the set of subjects owned by different parties might be slightly different.

# A PROOFS OF USEFUL LEMMAS

Lemma 1 (Gaussian mechanism). For any deterministic real-valued function f : D → R m with sensitivity S f , we can define a randomized function by adding Gaussian noise to f :

where N 0, S 2 f σ 2 • I is a multivariate normal distribution with mean 0 and co-variance matrix S 2 f σ 2 multiplying a

Lemma 2 (JL Lemma for inner-product preserving (Bernoulli)). Suppose S be an arbitrary set of l points in R d and suppose s is an upper bound for the maximum L2-norm for vectors in S. Let B be a k × d random matrix, where B ij are independent random variables, which take value 1 and value -1 with probability 1/2. With the probability at least

where

Proof. Hoeffding inequality and union bound together imply that with prob.

We further have

and replace β by b -1 β, we have that when

Lemma 5. If r is a random variable sampled from standard normal distribution, we have following concentration bound:

Proof. It's shown in page 2 in Pollard [2015].

Lemma 6. If r 1 , r 2 are two independent random variables sampled from standard normal distribution, r 1 r 2 can be written as c1-c2 2 , where c 1 , c 2 are independent two random variables sampled from chi-squared with degree 1. Moreover, n i=1 r 1,n r 2,n can be written as c1,1:n-c2,1:n 2

, where c 1,1:n , c 2,1:n are independent two random variables sampled from chi-squared with degree n.

. Because r 1 , r 2 are two independent standard normal random variables, r1+r2 √ 2 , r1-r2 √ 2 are two independent standard normal random variables as well. c 1 := r1+r2 √ 2 and c 2 := r1-r2 √ 2 complete the proof for the first part. 

# B PROOFS IN SECTION 4

We restate the assumptions and theorems for the completeness. Theorem 1. When β ≤ c for some variable c that depends on σ ε,δ , d and P, but independent of n,

is sampled from chi-square distribution with degree n. From the cdf of chi-square distribution, we have following concentration:

, where c 1,1:n , c 2,1:n are independent two random variables sampled from chi-squared with degree n. Thus

, implied by Lemma 5.

# P

, implied by Lemma 5.

# P

, implied by Lemma 5.

# Similar to 1,

With the application of Lemma 4: when

where h(β) is:

Theorem 2. When β ≤ c for some variable c that depends on d and P, but independent of n and σ ε,δ ,

Then we can make the analysis one by one.

1. JL-lemma applied by Bernoulli random variables implies that with probability 1

This further implies that

β 1 = 4 √ dβ helps finish the proof.

2. JL-lemma applied by Bernoulli random variables implies that with probability 1 -(d + 2) 2 exp k -

Proof. To simplify the proof, let's assume R X is a standard gaussian matrix. Because P

Plug-in the variance of R X leads to the targeted inequality. 

nd max σ ε,δ .

Then

Similarly,

Union bound gives the conclusion.

5. With prob. 1 -2

which is implied similar to 4.

6. With prob. 1 -2k(d + 1)

Proof. To simplify the proof, let's assume R X and R Y is a standard gaussian matrix first. Because P

Plug-in the variance of R X and R Y leads to the targeted inequality.

Define

The above analysis implies that, with prob. • O (min {1, β}) + Õ(1) .

# Acknowledgements

The authors thank Xiaowei Zhang for drawing pictures in Figure 1. RW and KQW are supported by grants from the National Science Foundation NSF (IIS-2107161, III-1526012, IIS-1149882, and IIS-1724282), and the Cornell Center for Materials Research with funding from the NSF MRSEC program (DMR-1719875), and SAP America.

