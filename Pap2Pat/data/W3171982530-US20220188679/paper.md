# Introduction

A derivative contract is a financial asset whose value is based on (or derived from) the price of one or more underlying assets. Examples of these underlying assets include stocks, currencies, commodities, etc. A derivative contract is typically issued between an issuer and a holder, and is valid until its expiration date. Each derivative defines a payoff that quantifies what the holder stands to gain. Generically, payoffs depend on the value of the underlying asset(s) across the duration of the contract. Derivative contracts are ubiquitous in finance with various uses from hedging risk to speculation, and currently have an estimated global gross market value in the tens of trillions of dollars [1]. A more detailed introduction to derivatives with descriptions of some of the common derivatives used by financial institutions is given in Appendix A.

The goal of derivative pricing is to determine the value of entering a derivative contract today, given uncertainty about future values of the underlying assets and consequently the ultimate payoff. In many cases, the pricing of derivative contracts uses Monte Carlo methods which consume significant computational resources for financial institutions. Therefore, finding a quantum advantage for this application would be very valuable to the financial sector as a whole. This work gives the first detailed resource estimates of the required conditions for quantum advantage in derivative pricing. In doing so, it also introduces new methods for loading stochastic processes into a quantum computer.

The rest of the paper is structured as follows: Section 2 gives a brief background on classical Monte Carlo methods for pricing derivatives and summarizes our results: the resources required for the quantum algorithms for pricing some commonly traded derivatives. Then, in Section 3, we present our core approach to the quantum algorithm and discuss its error analysis. Section 4 covers subroutines to load a stochastic model of the underlying assets into a quantum state along with the resources required for these methods. Here, we introduce the re-parametrization method, a novel method that plays a crucial role in the first feasible end-to-end path to quantum advantage in derivative pricing. In Section 5 we discuss the subroutine that applies the payoff operator to the stored stochastic process. Finally, in Section 6, we end with a discussion on the implications of this work and potential future paths.

# Derivative Pricing and Summarized Results

The price of the underlying asset(s) of a derivative contract is typically modeled as a stochastic process under assumptions like no-arbitrage. 1 A common model, that we will use in this work, is that the underlying assets evolve under geometric Brownian motion [2]. Let S t ∈ R d + be a vector of values for d underlyings at time t. Let ( S 0 , ..., S T ) = ω ∈ Ω be a path of a discrete time multivariate stochastic process describing the values of those assets. We use both notations for a path in the text. The corresponding probability density function is denoted by p(ω). Let f (ω) = f S 0 , ..., S T ∈ R be the discounted payoff of some derivative on those assets. To price the derivative we calculate

The reason for having a discounted payoff is to take into account the opportunity cost of investing in a risk-free asset. For the rest of the paper all payoffs will be implicitly regarded as discounted, except in Section 5 and Appendix A where we will be explicit about whether payoffs are discounted or not. More details on the concept of discounted payoffs can be found in Appendix A. 3.

If the underlying stochastic processes are modeled with geometric Brownian motion then they have transition probabilities

where ln S t = (ln S t 1 , ln S t 2 , . . . , ln S t d ) µ t-1 = (µ t- 1  1 , µ t-1 2 , . . . , µ t-1 d ) µ t-1 j = r -0.5σ2 j ∆t + ln S t-1 j .

(3)

Note that Eq. (2) at time t has a dependency on the asset vector at time t -1 via ln S t-1 j in µ t-1 j . The parameters r and σ j are the risk-free rate 2 and the volatility of the j-th asset respectively, ∆t is the time duration between steps of the stochastic process, and Σ is the d × d positive-definite covariance matrix of the d underlyings

where -1 ≤ ρ ij ≤ 1 is the correlation between assets i and j. The probability of any particular path ω ∈ Ω is then

Classically, some simple derivatives under this model are easy to price, such as European call options that can be priced analytically using the Black-Scholes equation [2]. Easy to price derivatives are often path independent, i.e. where the payoff is only a function of the final prices at exercise time f (ω) = f ( S T ). This contrasts with path dependent derivatives that are more difficult to price. Path dependent derivatives are often priced in practice with classical Monte Carlo methods. More examples of standard and more complex derivatives are given in Appendix A.

When using classical Monte Carlo, the accuracy of derivative pricing converges as O(1/ √ M ), where M is the number of paths that are sampled. In general cases, Montanaro [3] showed that quantum algorithms based on amplitude estimation [4] can be used to improve this to O(1/M ). Recent work has considered how to specialize this advantage to options pricing (options are a subcategory of derivatives) [5][6][7] and risk analysis [8,9].

As this is only a quadratic speedup, it is important to focus on derivatives that are complicated enough to require a large M in practice. In this work we give end to end quantum resource estimates for two examples of such derivatives (autocallable options and TARFs) that are both computationally expensive, path-dependent derivatives. In doing so, we detail and optimize the loading into quantum states of the underlying distribution over asset paths. This loading step was left open in previous work [5,6], and we give the first account of the resources required for it. Although autocallables and TARFs are usually not well known derivatives to those outside the financial sector, they are very commonly traded derivatives, particularly among financial institutions. It is for this reason, in addition to their complexity, that we have chosen them as suitable examples for the end-to-end quantum resource estimates. A more detailed description of autocallables and TARFs can be seen in Appendix A.4 and Appendix A.5 respectively.

In addition to estimating the resources needed for path loading using known methods (an extension of [7] that we call the Riemann Sum method), we introduce several optimizations, including intentional shifts from price space to return space calculations and the new re-parameterization method. These methods reduce the required resources significantly and are summarized in Table 1. In this table, we quantify resource requirements in the fault tolerant setting where the number of T -gates, called the T-count dominates the computational requirements. The T-depth is the sequential depth that dominates the runtime. Logical qubits consist of physical qubits in a quantum error correcting code of sufficient distance to support the required number of operations. Table 1: Resources estimated in this work for pricing derivatives using different methods for a target error of 2 × 10 -3 . As representative use cases of business interest with non-trivial complexity, we consider a basket autocallable (Auto) with 3 underlyings, 5 payment dates and a knock-in put option with 20 barrier dates, and a TARF with one underlying and 26 payment dates. Detailed definitions of these contracts and their parameters can be found in Appendix A. 4. We find that Grover-Rudolph methods [10] are not applicable in practice (details in Appendix B) and that Riemann summation methods require normalization assumptions to avoid errors that grow exponentially in T . Even if those normalization issues were avoided, as detailed in the Riemann Sum (no-norm) row, the re-parameterization method still performs best. See Section 4.1 for a discussion of the Riemann summation normalization. The detailed resource estimation is discussed in Sections 4.1.2 and 4.2.3.

## Discretized Derivative Pricing

In order to map our derivative pricing problem into quantum states, we must discretize the values S t . Classically, this is not that important as high precision is available, but, in order to study the minimal qubit requirements, we need to consider discretization explicitly in the quantum case.

Let each value S t be discretized into a different n-qubit register, i.e., mapped to a regular grid. We then define ω ∈ Ω as the discrete space of paths. The price expectation is now a sum

where the probability p(ω) can be defined in multiple ways. For instance, one can take the midpoints of the grid cells so that p(ω) = T t=1 P ( S t | S t-1 ), (7) where the S t are restricted to discrete midpoints. Or p(ω) can be defined as an integral over the discrete cells. These representations are the same in the limit of fine grids and in the following we will choose the midpoint method.

## Price Space vs. Return Space

In Section 2, Eq. (2) introduces geometric Brownian motion to model the price on underlying assets. We call this the price space description of the underlying stochastic process. In price space, transition probabilities are given by a multivariate log-normal distribution. An alternative, but equivalent representation, is to consider the stochastic process on the logreturns of the underlying assets, and perform all calculations in return space. When asset prices obey a log-normal distribution, then the log-returns are distributed normally. We define a vector of underlying log-returns for d assets at time t as

At any time t we can calculate the price of asset j from return space using

The transition probabilities are then given by a multivariate normal distribution

where,

and σ, ∆t, Σ and r are the same Brownian motion parameters as in price space. Note that this is no longer conditioned on the value at the previous time step. In fact, the path distribution in return space consists of dT independent Gaussians. Note that we have overloaded the notation from the price space formulation as these representations are interchangeable via Eq. (8). This calculation is needed when the stochastic process has been modeled in return space but the payoff is defined in terms of asset prices. In the following sections, it will be made clear from the context which space we are operating in.

Switching between price space and return space changes from log-normal distribution loading to normal distribution loading. In general, the loading of normals is easier since their underlying stochastic evolution is independent of the price at a previous time step which can be seen by comparing Eq. (3) and (11). As such, the probability distribution P ( R 1 , R 2 , . . . , R T ) across all T timesteps of the stochastic process can be computed simultaneously with

This advantage can compensate for the quantum arithmetic needed to evaluate the exponentials in Eq. (8). We will leverage this advantage with the re-parameterization method in Section 4.2. Additionally, when working with derivatives that have payoffs defined in terms of log-returns directly and are independent of individual asset prices, this is another reason to work in return space.

# Algorithm 3.1 Core approach to derivative pricing

Require: Parameters n, d, and T that are all positive integers. Require: An operator P for loading a probabilistically weighted superposition of paths onto a register of ndT -qubits.

1. Apply operator P to prepare the quantum state

3. Introduce an ancilla qubit and rotate the value of the f (ω) register into its amplitude:

4. Use amplitude estimation to extract the probability of the ancilla being |1 .

# Core Approach

Our approach to derivative pricing extends the quantum mean estimation method from [3]. In this section we review this approach and introduce an error analysis for the discrete case of option pricing.

Let the normalized discounted payoff of any path ω be given by

where f max and f min are the maximum and minimum possible payoffs respectively across all paths. The algorithm proceeds in four key phases. First, a probability distribution is loaded in form of a superposition over all possible paths. Second, payoffs for all possible paths are calculated in quantum parallel. Third, the expected payoff is stored in the amplitude of a marked state. Fourth, amplitude estimation is used to read out the amplitude using O(1/ ) queries for a given target accuracy > 0. This approach is detailed in Algorithm 3.1.

Note that Steps 1-3 in the Algorithm 3.1 load the exact answer after a single execution. Were it possible to read out an amplitude directly, then we could compute the expectation over all paths in a constant number of queries. This is, unfortunately, not possible, and so amplitude estimation introduces a linear overhead to extract an answer to a given precision. This is a key conceptual difference from classical Monte Carlo where samples from paths are taken. In Algorithm 3.1, we compute all possible paths and take (amplitude estimated) samples of the expected payoff.

Another important distinguishing feature of the quantum approach is that we must normalize the payoff in order to store it in the amplitude of a state. This normalization must be rescaled at the end and can have a critical impact on error scaling, as errors are also scaled up. In the Riemann summation method, discussed in Section 4.1, a version of this normalization rescaling can rapidly accumulate errors.

## Amplitude Estimation for Derivative Pricing

Typically, path-dependent derivatives like autocallables and TARFs are priced using Monte Carlo or quasi-Monte Carlo methods. Paths ω = ( S 0 , S 1 , ..., S T ) are generated by modeling the underlying stochastic process and then the expected payoff is calculated using the estimator

This estimator converges to the true expected value with error = O(M -1/2 ) by the Central Limit Theorem [11]. This convergence can be quadratically accelerated to = O(M -1 ) using quantum amplitude estimation [4] for Monte Carlo [3,5,6]. Amplitude estimation takes as input a unitary operator A on n + 1 qubits such that

where the parameter a is unknown. Here, the final qubit acts as a label to distinguish |ψ 0 states from |ψ 1 states. Amplitude estimation determines a by repeated applications of the operator3 Q = AS 0 A † S ψ0 , where S 0 = I -2|0 n+1 0| n+1 and S ψ0 = I -2|ψ 0 n |0 0| ψ 0 | n are reflection operators. By using phase estimation and the quantum Fourier transform a can be determined with accuracy O(M -1 ) [4]. Unfortunately, the required depth of the resulting quantum circuits scales as O(1/ ) and requires the use of a resource expensive quantum Fourier transform. Recent developments have introduced other approaches [12][13][14][15][16][17] that aim to reduce the resource requirements needed for amplitude estimation and can remove quantum phase estimation.

The most efficient variant of amplitude estimation known to date is Iterative Quantum Amplitude Estimation (IQAE) introduced in [14]. It has been shown empirically that IQAE outperforms the other known variants. Although it omits quantum phase estimation [18], it achieves a four times better performance than the canonical phase estimation approach. Further, it has been shown that for practical considerations, the following bound holds:

where N wc oracle denotes the worst-case number of oracle calls, i.e., applications of Q, to achieve an estimation error of > 0 with confidence level 1 -α, α ∈ (0, 1).

We use the performance estimates from Eq. (19) for IQAE for our resource estimates in this work. This approach gives a full quadratic speedup, however it requires a quantum processor to successfully execute programs of oracle depth O(1/ ). This large depth is a demanding requirement on QPU performance and is a dominant contributor to the required resources. Recent work [17,19] has shown that it is possible to use shorter depth quantum programs O(1/ 1-β ) in exchange for less quantum advantage in total oracle calls N oracle = O(1/ 1+β ) for β ∈ (0, 1]. Using shorter depth quantum programs means more tolerance to error and as such may result in less needed overhead for error correction. While there may be settings where this tradeoff is advantageous overall, we leave this analysis to future work.

## Path Distribution Loading

In order for Algorithm 3.1 to achieve a practical quantum advantage, the resources needed for path loading and payoff calculation need to be taken into account. In some cases, there is an analytic form that can simplify path loading. For example in the case of path-independent derivatives, a distribution over paths is not needed. All that is needed is a distribution over final underlying prices S T , such as the log-normal distribution given by the Black-Scholes model. This means that the distribution could be analytically computed and then loaded either variationally or explicitly into quantum states. Unfortunately for quantum advantage, the analytic form for this distribution means that these derivatives are typically easy to price classically. Thus it is critical to focus on path dependent derivatives where a superposition over paths needs to be computed.

While the loading of general distributions is exponentially hard [20], several methods have been proposed. If the distribution is efficiently integrable, then there does exist an efficient quantum algorithm for loading, the Grover-Rudolph method [10]. However, the algorithm has limited applicability in practice for derivative pricing, because the relevant probability distributions still require Monte Carlo integration (albeit quantumly) which is precisely what we are trying to avoid by using Amplitude Estimation. More details on the insufficiency of this method are detailed in Appendix B.

An alternative method for loading the path distribution, using a qGAN [21], was proposed in [6]. While this has appeal for lower overhead loading, it is not yet clear how to anticipate what the overhead from training a given qGAN will be in practice.

## Error Analysis

In this section, we investigate the various elements that contribute to the overall error in the quantum approach to derivative pricing. There are three main components that introduce error in Algorithm 3.1. Let

Truncation Error The price of a derivative is determined by an integral over all the possible values of the underlying price (or return). Given finite quantum memory, we cannot feasibly compute an integral over an infinite domain, and thus we restrict the domain of integration as follows: the prices/log-returns are restricted to a range [B l , B u ]. This restriction of the domain leaves out a probability mass of α. Given an upper bound of P max on the density functions at each step and an upper bound f δ on the discounted payoff, we incur a truncation error which we denote by trunc = P T max f δ α.

Discretization Error This error (denoted by disc ) arises from the use of a Riemann Sum over a finite grid of points to approximate the integral. This error can be reduced by increasing the number of qubits (n) to approximate the sum.

Amplitude Estimation Error Amplitude estimation incurs an error of amp when using 1/ amp repetitions of the state preparation procedure and price computation.

We now analyze the truncation and discretization errors in more detail.

### Truncation Error

We present the truncation error in return space as it then extends to price space straightforwardly. Denote the maximum eigenvalue of the covariance matrix Σ by σ max . Using Chernoff tail bounds on Gaussians, the probability that the log-returns for asset i lie outside of the interval [µ iwσ max , µ i + wσ max ] is upper bounded by 2e -w 2 /2 . By the union bound the probability that any log-return (d assets over T time steps) lies outside the interval [B l = (r-0.5σ 2 max )∆t-wσ max , B u = (r-0.5σ 2 max )∆t+wσ max ] is upper bounded by 2dT e -w 2 /2 . Let the initial asset prices lie in the range [S 0 min , S 0 max ]. Then the corresponding interval in price space is given by [S 0 min e B l T , S 0 max e BuT ]. We can then define the truncated window of values for our dT different n-qubit registers that are w standard deviations around the mean for each time step. The truncation error of the integral already normalized by P T max f δ is then given by trunc ≤ 2dT e -w 2 /2 . (20)

### Discretization Error

The final output of the amplitude estimation algorithm represents a Riemann Sum that approximates the truncated multidimensional integral. The integral is over dT variables corresponding to d assets over T time steps. We assume that each underlying asset/return is restricted to an interval [B l , B u ]. To compute the discretization error, we apply a multidimensional variation of the midpoint rule as follows: let there be n qubits used to represent each underlying asset, the domain is divided into 2 ndT cells, and corresponding to each value of the register we associate the value of the integrand at the midpoint of the corresponding cell. Assume that β provides an upper bound on the second derivatives of the integrand (this can be restated as saying that the deviation from linearity over a range of length l is bounded by βl 2 /2). We consider the error from discretization that accumulates over a single cell. Each cell has side length (B u -B l )/2 n and is a hypercube of dimension l. Note by symmetry that the linear component of the deviation from the value at the center of the cell integrates to 0 over the cell. The error in each cell can thus be bounded by the integral of the term βx 2 /2 over a dT -hypercube of side length l = (B u -B l )/2 n centered at the origin.

Aggregating the error over all the cells, we have

In terms of the number of standard deviations used in the discretization and the largest eigenvalue of the covariance matrix σ max , the total discretization error is bounded by

For a target discretization error, Eq. ( 23) also gives us the total number of qubits required to represent d assets for T timesteps, given by

The truncation and discretization errors apply in general to the methods we introduce, though each method has additional method-specific error sources which are discussed separately.

# Methods for Advantage in Quantum Derivative Pricing

In the following sections we introduce two approaches that can work effectively for quantum derivative pricing in practice: Riemann summation and re-parameterization. Riemann summation was introduced in [7], and we present the first resource analysis for its application for quantum advantage. This analysis uncovers limitations in error scaling due to normalization. We then introduce a new method called re-parameterization that avoids the downsides of other methods and offers the first end-to-end path to quantum advantage in practice.

## Riemann Summation

The Riemann summation method [7] gives an approach to construct the P path loading operator in Algorithm 3.1. Let N = 2 ndT be the size of the Hilbert space that contains all possible paths. Let Pmax be the maximum value of the d-asset multivariate transition probabilities from Eq. (2). Then P ( S t | S t-1 ) = P ( S t | S t-1 )/ Pmax ∈ [0, 1] are the normalized transition probabilities over all choices of S t and S t-1 . Let the asset price for each asset at each timestep be discretized in the interval [0, S max ]. The steps of the method summarized in Algorithm 4.1 calculate the price of the derivative with a normalization factor 1/P T max , with P max = Pmax S d max . Critically, we note that the normalization factor in the final step scales exponentially in T . If P max < 1 no normalization is needed, but this factor can be used to improve the performance. However, if P max > 1, the error increases exponentially, which renders this approach impractical.

The normalization factor P max is easier to handle in return space where the probability density function is given by Eq. (9). If we discretize the log-returns at each timestep for each asset to ±w times the asset's volatility σ j , we have Require: Access to operators W t , t = 1, . . . , T that apply the transition probabilities of the stochastic process into an ancilla via

1. Apply Hadamards to ndT qubits to prepare an equal superposition of all paths.

2. Load the initial prices S 0 into the zero-th nd-qubit register.

# Apply each of the T transition operators

where N = 2 ndT .

4. Calculate δ(ω) = arcsin f (ω) into a quantum register, obtaining 1

5. Introduce an ancilla qubit and rotate the value of the f (ω) register into its amplitude:

. . . + 1

6. Use amplitude estimation to extract the probability of the ancilla being |1 .

Output: The (discretized) expected payoff E( f (ω)/P T max ) = 1/(P T max N ) ω p(ω) f (ω). We rescale this to obtain E(f

When the d assets are uncorrelated, we have

and therefore we need to choose w ≤ π/ √ 2 for P max ≤ 1. However, choosing a small discretization window w increases the truncation error discussed in Section 3.3.1, and for w ≤ π/ √ 2 we have trunc ≥ 2e -π 2 /4 ∼ 0.17, which increases proportionally to the number of assets and timesteps in the computation.

## Riemann Summation Error Analysis

In addition to the truncation and discretization errors from Section 3.3, the Riemann summation approach includes errors due to scaling considerations and quantum arithmetic. When working in return space, we only need one transition operator which computes Eq. ( 12) and performs the amplitude encoding of p(ω) in Eq. (26). Assuming the transition operator introduces a maximum additive error dens and the payoff operator computing Eq. (27) and Eq. (28) introduces payoff error f , the total arithmetic error of the quantity we estimate using amplitude estimation is

Ignoring quadratic error terms, we have

where we assume the payoff has been normalized to lie in [0, 1] and the log-returns for each asset and each timestep have been constructed to discretize the domain [-wσ max , wσ max ].

The probability density error dens arises from the computation of |arcsin P ( R) with P ( R) given by Eq. (12), and the ancilla rotation in Eq. (26). The term inside the exponential in Eq. (12) can be written as

where R = R -µ and C ij are classical variables containing volatility and correlation parameters from the correlation matrix Σ. In Eq. (33), each calculation of R thus incurs an error of A and there are (d+ d 2 )•T multiplications in total. Each R term is bounded by |w|σ max by construction, where each quantum register representing a log-return R is constructed to represent values in the window [-wσ max , wσ max ]. Using the error analysis for addition and multiplication in Appendix C.2, the total error in computing Eq. ( 33)

Then using the error propagation analysis in Appendix C.2 for computing the exponential, square root, arcsine and sine functions on quantum registers which already contain arithmetic errors, we can bound dens by dens ≤ sin + arcsin -arcsin(0.5 -

Each rescaling we perform to the input variables introduces a corresponding rescaling error. In addition to the the P max rescaling discussed in the previous section, we also need to scale the payoff by 1/f δ to lie in [0, 1]. The final answer thus needs to be multiplied by P T max f δ to account for these rescalings, and the error in the estimate of the truncated integral by amplitude estimation is therefore scaled by P T max f δ . We then can bound the error in the Riemann Summation approach

where trunc , disc , and amp are defined as in Section 3.3.

### Resource Estimates

As an example, we consider a basket autocallable with 5 autocall dates and parameters T = 20, d = 3, and target an error of total /f δ ≤ 2 × 10 -3 . We need to choose w ∼ 5 for the truncation error in Eq. ( 20) to be within the total target error, and Eq. (30) gives P max ≈ 4 3 . This makes the scaling factor prohibitively large with P T max ≈ 10 40 . However, there may be some methods to deal with this normalization issue, such as a method inspired by importance sampling and discussed in Appendix D.2. For the sake of argument, we continue the resource analysis assuming that some method could be invented to deal with the normalization, and set P max = 1.

Then, using resource calculations as discussed in Appendix D.1, we can bound arith ≤ 2 × 10 -3 with n = 34 and p = 2. Here p is the integer part of the fixed point representation as defined in Eq. (64). The Q operator in this case requires 23k qubits and has a T-depth of 26k, including the resources required to compute prices from log-returns using Eq. (8). For a choice of ∆t = 1/20 and σ min = 0.1 we compute that β ≈ 17. Choose σ max = 0.4 and w = 5. Thus for the choice of n, disc ≈ f δ 10 -5 and trunc ≤ f δ • 10 -4 . When the derivative is priced classically with Monte Carlo, we define the pricing error as the standard deviation of the calculated derivative prices over all simulated paths. We therefore pick 1 -α = 0.68 in Eq. (19) to calculate the number of oracle calls needed for a given target error at the same confidence level as classical Monte Carlo. Choosing a target amp for the amplitude estimation of 10 -3 , we then obtain N wc oracle ≤ 6k. This means that the total T-depth is about 1.5 × 10 8 .

Using the same analysis, for a TARF contract (see Section 5.2) with d = 1, T = 26 and ∆t = 1/26, assuming the underlying has annualized volatility σ = 0.4, a target error of total /f δ ≤ 2×10 -3 can be achieved with a total T-depth of 1.6×10 8 and 17k qubits. These resource estimates are summarized in Table 1.

## Re-parameterization Method

The limitations of normalization in Riemann summation motivate the need for a new method for loading stochastic processes. In the re-parameterization method, we shift to modeling assets in return space. As described in Section 2.2, in return space underlying assets consist of uncorrelated normal distributions. We recognize that these different distributions can be loaded by preparing, in parallel, many standard normals and then applying affine transformations to obtain the required means and standard deviations. This approach extracts a specific subroutine -loading a standard normal into a quantum state -and uses it as a resource to load the full distribution of underlying paths. The normal loading subroutine itself can then be precomputed and optimized using variational methods. This is an advantageous combination of fault-tolerant quantum computing with variational compilation and will be discussed in Section 4.2.1. Overall the re-parameterization method avoids the normalization issues in Riemann summation and reduces the computational requirements.

The steps in re-parameterization pricing are described in Algorithm 4.2. We note that a path ω R ∈ Ω R in this context refers to a series of log-returns R 1 , . . . , R T . The re-parameterization method removes the problematic dependence on P max , and the operators G j can be implemented with relatively few resources using variationally trained circuits as discussed in the following.

### Variationally Trained Gaussian Loaders

The standard Gaussian loading operator G can be pre-computed because in the re-parameterization method it is problem independent. In this section, we describe an approach to variationally optimize this operator. Let us consider the problem of preparing a standard normal distribution g(x i ) Algorithm 4.2 Re-parameterization method pricing Require: Parameters n, d, and T that are all positive integers. Require: Access to an operator G that loads a standard Gaussian distribution i √ g i |i into an n-qubit register. Let g i be the value of the probability mass function for a standard Gaussian distribution discretized into 2 n -bins.

1. Apply dT Gaussian operators G, to ndT qubits. This constructs

where ω R runs over all 2 ndT different realizations of this multivariate standard Gaussian, and p(ω R) denotes the corresponding probabilities.

2. Let Σ = LL be the Cholesky decomposition of the covariance matrix. Perform affine transformations R t = µ t + L Rt to adjust the center and volatility of each Gaussian. We denote the corresponding return paths and probabilities by ω R and p(ω R ), respectively.

3. If the payoff can be computed directly from the log-returns, then we directly calculate

If the payoff is defined in terms of prices and not just log-returns, then we first compute the price space path ω for each asset using

. This calculation can be done in parallel for each asset.

4. Introduce an ancilla qubit and rotate the value of the f (ω R ) register into its amplitude:

5. Use amplitude estimation to extract the probability of the ancilla being |1 .

We rescale this to obtain

defined on a discretized mesh of points

In the following example we fix the domain to w = 5, so that the full range of values considered is 2w = 10. This choice leaves outside the domain a probability mass of ∼ 5 × 10 -7 . We take into account the different metrics used for normalizing a function in real space and a wavefunction in a quantum register (which is normalized in such a way that the sum of its squared elements is one), and therefore the distribution we aim to load in the quantum register is

Notice that due to the finite truncation domain, the target distribution is normalized to 1 -α. In principle we can re-normalize the distribution to one in the chosen interval of width 2w. Either way this choice provides a negligible difference when compared with the error we observe in the training.

The variational ansatz of choice is represented by a so-called Ry-CNOT ansatz, with linear connectivity (see Appendix F). In this work we introduce a novel strategy to optimize the circuit in this context, which relies on a energy-based method [22], and is also detailed in Appendix F. In short, the target cost function is the energy of the associate quantum harmonic oscillator problem, whose ground state is naturally Gaussian [23]. Here, we must be careful because the squared modulus of the solution of the discretized quantum harmonic oscillator matches a normal distribution only in the limit of ∆x → 0. To fix this we perform a subsequent re-optimization targeting directly the infinity-norm between the two distributions.

where the quantum state encoded in the register is defined by coefficients g(x i ).

We notice that training directly with Eq. (41) as a cost function is not sufficient, and pre-training using the energy-based approach is needed to produce accurate results. We indeed observe how the L ∞ cost-function displays a much more corrugated landscape in the circuit parameter space compared to the energy of the associate quantum harmonic oscillator problem.

It is important to note that the circuits needed to encode these Gaussian states for different choices of the register size n can be pre-trained and used for any derivative pricing problem, and therefore the training cost is not included in our overall resource estimations. We show in Fig. 1 results for different register sizes and depths of the circuit ansatz. More details are provided in Appendix F.  This numerical study shows that the state we can prepare variationally, approaches the target exponentially fast in the depth, and hence in the number of gate operations. This observation is in good agreement with the expected behavior from the Solovay-Kitaev theorem [24], that provides an upper bound for the number of gates required to achieve a desired accuracy for a cost function. Indeed, for any target operation U ∈ SU (2 n ), there is a sequence of operators S = U s1 U s2 . . . U s D in a dense subset of SU (2 n ), such that error in the energy decreases exponentially with the depth D = O(log c (1/ε)). Although the subset of SU (2 n ) operations generated by the entangler blocks in our circuit does not generate a dense subset of SU (2 n ) arbitrarily close to the exact unitary U (the generator of the target state), we can numerically observe that the exponential decrease of the error with the number of gates still holds.

We end this section investigating the portability of these results in the fault-tolerant regime, which is necessary for the applicability of the derivative pricing algorithm. While our numerical results provide evidence for a rather efficient Gaussian state preparation in terms of circuit depth for an Ry-CNOT ansatz, an additional step has to be made in view of a fault-tolerant implementation of such circuits. In this new-framework, the continuous rotation Ry gate needs to be expanded as a finite product of discrete operations. Following again the Solovay-Kitaev theorem, or more specialized results [25], it is possible to also have an efficient representation of any SU (2) operator with a sequence of Clifford + T gates that scale logarithmically with the threshold error . We investigate how the results obtained before can be transferred in this regime where rotation angles can only take discretized values. We therefore assume that each parameter ϑ k qj can only be represented in the format j * 2π/M digit , where j is an integer. We numerically show in Appendix F that the error introduced by such digitization decreases systematically with the mesh size as O(1/M digit ).

### Error Analysis

The total error in the re-parameterization approach is

where trunc , disc , and amp are the truncation, discretization, and amplitude estimation error bounded in Section 3.3. Here, the term arith arises from the individual errors we introduce during the preparation of the Gaussians and the calculation of the payoff. Assuming that each Gaussian g(x i ) we prepare has L ∞ error dens and the payoff calculation introduces a max error of f , the total error will be

where x = (x 1 , x 2 , ..., x dT ). Expanding the integrand and keeping only the linear error terms, we get

where we use that w -w g(x) ≤ 1 due to truncation of the probability mass function.

### Resource Estimates

We calculate the resources required for the same basket autocallable as in Section 4.1.2, where d = 3, T = 20, ∆t = 1/20, σ max = 0.4, σ min = 0.1 and w = 5, and the contract has 5 autocall dates. We further assume that each Gaussian is prepared with n = 5 qubits, such that dens = 2 × 10 -6 , amp = f = 10 -4 , which gives us a total error of total /f δ ≈ 2 × 10 -3 . From Fig. 1 we observe that we can prepare Gaussian states with L ∞ ∼ 2 × 10 -6 using 5 qubits and circuit depth 6, requiring 7 layers of Ry gates. With these inputs and using the resource calculations described in Appendix E, constructing the Q operator using re-parameterization requires 8k qubits and has a T-depth of 9.5k, which includes the computation of prices from log-returns, Eq. (8). For a target confidence level of 1 -α = 0.68, the total T-depth is 5.4 × 10 7 . With the re-parameterization method, pricing the TARF of Section 4.1.2 with d = 1, T = 26, ∆t = 1/26 and σ = 0.4 to accuracy total /f δ ≈ 2 × 10 -3 requires total T-depth of 8.2 × 10 7 and 11.5k qubits. These resource estimates are summarized in Table 1.

# Payoffs

The previous sections analyzed methods for performing steps 1-3 in Algorithm 4.2. This results in a quantum state representing a superposition of all possible paths. In this section, we apply payoff functions to these superpositions (step 4) so that the normalized expected discounted payoff is stored in an amplitude of an accumulator qubit. This allows amplitude estimation to extract this amplitude to complete the pricing algorithm. We also analyze the additional errors introduced by the payoff function. We cover two example derivative cases: autocallables and TARFs. In addition, throughout this section (unlike in the other sections), we will assume that payoffs are not discounted unless explicitly stated.

## Autocallables

An autocallable contract is typically defined in terms of asset returns relative to predefined reference levels, and includes a notional value which is used to calculate the dollar value of the contract. For a single underlying, an autocallable consists of:

• a set of m binary options {(K i , t i , f i )} i=1...m each with strike returns K i , payment dates t i , and binary payoffs f i . Assume these are sorted so that t i < t i+1 .

• a short knock-in put with strike K put , barrier b and notional value k, and

• the condition that if any binary option has a non-zero payoff then all subsequent options at later times including the put option are knocked out.

The payoff f i of the binary options is equal to a fixed number p i when Rti c ≥ K and zero otherwise, where Rti c is the cumulative return of the underlying asset at timestep t i . The payoff of the put option is

A more detailed explanation of autocallable options and all the parameters mentioned above can be found in Appendix A.4. Note that the minimum payoff of the option occurs when the return of the underlying asset falls to zero. Therefore, we can compute the normalized discounted payoff fi from Eq (13) as

where f disc max is the maximum possible discounted payoff among the possible discounted payoffs across all the binary options and r is the risk-free rate. We now give a sketch of the algorithm used to implement the payoff for an autocallable shown in Algorithm 5.1. In steps 1-2, we compute the strike and put qubits that indicate s which of the payoffs f 1 , f 2 , ..., f m , f put are non-zero. In step 3, we control on the strike qubits to apply the appropriate rotation on the accumulator qubit corresponding to the normalized discounted payoff from the binary options. In parallel, we execute step 4 which stores the normalized discounted payoff from the put option into another register. Finally, in step 5, we use the previously computed register to apply the appropriate rotation on the accumulator qubit corresponding to the normalized discounted payoff from the put options. This procedure is illustrated in Fig. 2.

We elaborate on a few subtleties in Algorithm 5.1:

1. Throughout the algorithm, we can assume that we have access to | Ri c for all i. This is because these registers are set when computing the prices S i of the underlying when loading in the paths onto the quantum state (Appendix E).

2. Strictly speaking, the output register in step 4 is equal to |arcsin( fput ) only if the part of the |put qubit that is entangled to this final register is |1 . However, in the next step, the R y rotations that are controlled on this register are also always controlled on the |put qubit, so the instances when the register has an unknown value have no effect on the rotations applied to the accumulator qubit.

3. The autocallable can also be defined on a basket assets instead of just one. Typical examples include BestOf and WorstOf, where the return of the contract is based on the return of the best or the worst performing asset in the basket respectively. The only difference is that, in step 1, we would apply the comparators on all the assets and then compare the return of each asset | Ri c,j j=1...d to find the largest or smallest as necessary. We can then use the fact that if the worst performing asset is above the strike price, then so are all the other assets. Conversely, if the best performing asset is below the strike price, then so are all the other assets.

4. If we want to price an autocallable option that does not have a knock-in put, then, not only can skip steps 4-5 of the algorithm, but we can also perform the algorithm by just using the sum of log-returns instead of the sum of returns. Then it would be sufficient to have access to the registers | ti j=1 R j instead of | Rti c which would reduce the resources required in the loading of the paths in superposition into the quantum state.

We now discuss the error arising from Algorithm 5.1. Steps 1-2 are performed with logical operation circuits (Comparator, AND, OR) which introduce no error, while steps 3 and 5 require controlled-Ry rotations whose decomposition into T-gates is a function of an additive error , which we can choose depending on the desired accuracy of the calculation.

Step 4 is the most resource heavy component of the payoff circuit, which requires the computation of the quantum register | RT c -K put , the division of that register by the classical constant in the denominator of Eq. (46), as well as the computation of the square root and arcsine of the register. We describe in detail the resource requirements for all the above circuit components in Appendix C.1, and the corresponding arithmetic and gate synthesis error in Appendix C.2.

Consider again the autocallable contract from Section 4.1.2 and Section 4.2.3 with 5 autocall dates, defined on d = 3 assets and simulated using T = 20 timesteps. We target a total additive payoff error f which when distributed across the operations of steps 3, 5, 6 in Algorithm 5.1 determines the resources required by each component. For f = 10 -4 , the circuit computing the autocallable payoff requires 1.6k qubits and a T-depth of 3.2k, assuming we can parallelize computations wherever possible. These resources are included in the end-to-end summary estimates of Table 1.

## Target Accrual Redemption Forwards

In this section, we consider the payoff implementation for the second example derivative: TARFs. To simplify the discussion, we describe the TARF implementation for a single underlying in price space. TARFs are usually contingent on the price of the underlying asset rather than the return.

A TARF is:

# Algorithm 5.1 Autocallable payoff implementation

Require: An autocallable with parameters {(K i , t i , f i )} i=1...m , K put , b and k.

1. We apply in parallel a set of T comparators to obtain the register | Ri c < b T , a set of m comparators to obtain the strike register | Rti c ≥ K i m and a single comparator to obtain the qubit | RT c < K put . 2. We then apply the necessary AND and OR operations on all the registers from the previous step to obtain the |put qubit which is set to |1 if all of the conditions for the put option were fulfilled i.e. none of the binary options payed off, the put option was knocked in and RT c < K put .

3. Let θ i = arcsin( fi ). Serially, for each bit of the strike register we apply a controlled rotation of θ i on the accumulator qubit conditioned on all previous bits having been zero. This is illustrated in Figure 3.

4. We use the register | RT c to compute the arcsine of the the normalized expected payoff using quantum arithmetic and obtain the register |arcsin( fput ) where fput is defined in Eq. (46). 5. Finally we apply a rotation of θ put = arcsin( fput ) on the accumulator qubit on the condition that the put option is activated. This is done using a series of R y (2 i ) rotations

where each rotation is controlled on the ith qubit of the |arcsin( fput ) register and the |put qubit.

• A forward price F , payment dates denoted chronologically by timesteps t = 1, 2, ..., T , two strike prices K upper > F and K lower ≤ F , a knock-out price b, a constant α and an accrual cap C ∈ R + .

• At each timestep t the TARF has a payoff

and the contract is not knocked out ('upper condition') α(S t -F ) if S t < K lower and the contract is not knocked out ('lower condition') 0 otherwise.

• a knock-out condition that if at any time t the price is above b > F all payoffs that haven't been paid yet (including the one for the current time t) are knocked out. We will call this the 'barrier condition'.

• an accrual cap condition such that if the total gain accumulated by any payment date exceeds C the contract holder only receives a payoff such that the total gains equals C and the rest of the forward contracts are knocked out. We will call this the 'cap condition'.

A more detailed explanation of TARFs and all the parameters mentioned above can be found in Appendix A.5.

The minimum TARF payoff occurs when the price of the underlying asset falls to zero, and the maximum payoff occurs when the payoff at every payment date is b -F until the accrual cap is reached. Thus, we can compute the normalized discounted payoff f (ω) using Eq. (13) to be where f disc (ω) is the discounted payoff of the TARF for the path ω and r is the risk-free rate. Algorithm 5.2 details an implementation for a TARF payoff. In steps 1-3, we compute the 'partial conditional payoffs' f partial t at each timestep t, i.e. the payoff given that we ignore the cap condition. In steps 4-8, we compute whether the cap condition is fulfilled at each timestep and correct the partial conditional payoffs to take into account the cap condition (giving us the actual payoffs). Finally, in steps 9-11 we discount the payoffs, sum them up, normalize the result according to Eq. (48) and apply the appropriate rotation on the accumulator qubit. This procedure is illustrated in Fig 4. An interesting note is that were we to ignore the discount factor, this algorithm would be much simpler: we would add an extra step after step 5 in which we would set the payoffs for all the paths in which the cap condition was fulfilled equal to C and then to skip ahead to steps 10 and 11.

An error analysis for the TARF payoff is very similar to that described in the previous section for autocallables. There are 2 main differences. First, when computing the payoff f partial t for the lower condition, we require a multiplication. We set the error on this multiplication to be 10 times lower than our final desired error to make it negligible. Second, when discounting the payoffs, we have to ensure an error of 1 √ T times smaller than in the auto-callable case because we are adding the payoffs after discounting them, causing the errors to add in quadrature. For f = 10 -4 , the circuit computing the TARF payoff requires 9k qubits and a T-depth of 6k, assuming we can parallelize computations wherever possible.

# Algorithm 5.2 TARF payoff implementation

Require: A TARF with parameters (F, T, K upper , K lower , b, α, C).

1. We apply in parallel a set of comparators to obtain the registers |S t < K lower T , |S t > K upper T and |S t > b T .

2. We then apply the necessary AND and OR operations on all the registers from the previous step to obtain registers |upper T and |lower T where the tth qubit in each register represents whether the upper and lower conditions were partially fullfilled (not taking into account the cap condition).  

# Discussion

We provide a thorough resource and error analysis to price financial derivatives using quantum computers. In particular, we investigate autocallables and TARFs which are two important pathdependent options that are relevant in practice and computationally expensive to price classically. To achieve this we introduce the re-parameterization method: a new method to load stochastic processes that overcomes the limitations of existing approaches. Although we limit our analysis to geometric Brownian motion, our approach can be straightforwardly extended to other models e.g. to stochastic or local volatility methods by loading multiple independent stochastic processes and introducing a conditional or non-stationary re-parametrization.

Our resource estimates give a target performance threshold for quantum computers capable of demonstrating advantage in derivative pricing. Assuming a target of 1 second for pricing an autocallable option, the quantum processor would need to execute T-gates at a rate of 10MHz at a code distance that can support 10 10 logical operations. Further improvements in reducing the T-depth for this algorithm would linearly lessen this requirement.

The resource estimates in this work concur with recent work [26] that emphasizes the importance of going beyond complexity scaling in order to understand thresholds for quantum advantage. In particular, the quadratic speedup available in amplitude estimation-based algorithms could be lost in the constant factor overheads of error correction.

Although current estimates target logical clock rates around 10kHz [27] (i.e. orders of magnitudes slower than our requirement), we are optimistic that future work on algorithms, circuit optimization, error correction, and hardware will continue to improve the required resource estimates and runtimes. For example, in the case of Shor's algorithm, the estimated resource requirements have reduced by almost three orders of magnitude through careful analysis across several publications [28]. This work represents the first milestone on the journey towards quantum advantage for pricing financial derivatives and we are looking forward to future enhancements.

Further, we emphasize that the resource estimation approach here can be fruitfully applied to analyze thresholds in other financially relevant applications. As summarized in two recent reviews [19,29] there are many potential areas for quantum advantage in finance where advantage thresholds would provide useful targets for both industry and the research community.

# A Background on Derivatives

This section presents some examples of commonly used derivatives in the financial sector. Unlike in most other sections of this paper where all payoffs are assumed to be discounted payoffs, in this section they are by default not discounted unless explicitly stated.

# A.1 Forwards

An example of a derivative is a forward contract, often simply called a forward. Here, the holder promises to buy or sell a certain asset to the issuer on a specified date in the future at a fixed price F known as the forward price. A simple path-independent example is where the holder promises to buy x amount of an asset at F dollars per asset m months from now. Forwards are typically settled in cash i.e. instead of the money and asset exchanging hands on the expiration date, a payoff is determined based on the value of the asset and there is only an exchange of money determined by this payoff. For example, if the price at the expiration date T of the asset is S T , the payoff is given by f (S T ) = x(S T -F ), where if f (S T ) > 0, the contract holder makes a profit (and the issuer a loss) and the opposite if f (S T ) < 0.

# A.2 Options

Another example of a derivative is an option. Options can be viewed as conditional forwards. With an option contract, the holder has the option to buy or sell a certain asset to the issuer on some future date at a pre-determined price (unlike the foward where the issuer is obliged to buy or sell the asset). If the holder chooses to buy or sell the asset, we say that they have exercised the option. Similarly to the forwards, option contracts are usually settled in cash based on the value of the asset on the exercise date. An example of a path-independent option with a single underlying asset is a European call option, where the issuer has the option of buying an asset at a strike price K on expiration date. The payoff on expiration date can then be written as f (S T ) = max(S T -K, 0). A European put option is where the issuer has the option of selling an asset at a strike price K on expiration date, which gives a payoff of f (S T ) = max(K -S T , 0). Another example of a path-independent option is a binary option which has a fixed payoff if the underlying asset is above (or below) the strike at time T .

# A.3 Path-dependence and Discounted Payoffs

An example of a path-dependent derivative is a knock-out European call option. This is the same as a European call option, but with an additional knock-out price (or barrier ) b. If at any time from 0 to T the underlying asset goes above this value, then the contract is worth nothing. This path-dependent payoff function has the form

The inclusion of the value of the underlying at times other than T is what introduces path dependence. Another example is a knock-in put option which has payoff

Here the contract is knock-in because it only has non-zero payoff if the asset goes below some value b.

In the examples discussed so far, there has only been one payment date where an exchange takes place between the contract issuer and holder, at time T . It is possible (as we will see later) for some path-dependent options to have several payment dates, i.e. where several payments are made at different times throughout the course of the contract duration.

We now introduce the notion of a discounted payoff. As expected, the price today for any derivative is related to its expected payoff in the future. However we also want to take into account the time delay for the payoff to account for the opportunity cost of investing in a riskfree asset with interest rate r. If a contract has a payoff f i at time t i from today, we define the discounted payoff as e -rti f i .

The price of a derivatives contract is given by the expected value of the discounted payoff under the stochastic process for the underlying assets. In practice, path-dependent derivatives are much more difficult to price computationally and are often priced using Monte Carlo simulations of the paths. This is in contrast to some models for path-independent derivatives that can even have analytic solutions, such as the Black-Scholes model for European call options [2]. Path-dependent options present an opportunity to use quantum speedups for Monte Carlo to gain advantage. In this work, we will consider two specific examples of path-dependent derivatives: autocallables and target accrual redemption forwards (TARFs).

# A.4 Auto-callable Options

A typical example of an auto-callable ('automatically callable') option is a set of binary options, each of which pays different binary payouts at different payment dates and then knocks out the whole product (i.e. voids all future payoffs) if it makes a non-zero payout at any of the payment dates. Autocallables are typically contingent on the returns of the underlying asset (as opposed to directly on the price). More formally, let (K i , t i , f i ) be a binary option that has payoff f i defined as

where p i is a fixed dollar value and Rti c is the cumulative return of the underlying asset at time t i defined as the product of the returns Rtj for j = {1, 2, ..., i}. We have used the notation R to represent the return to differentiate from R which we have used previously to represent the log return. An autocallable is then a set

where {t i } and {p i } typically increase linearly. If any of the binary options (K i , t i , f i ) pays out a non-zero dollar amount (i.e. is in the money), then all subsequent options {(K j , t j , f j )} j>i are knocked out i.e. voided. In practice, these binary options are often bundled with a short knock-in put option i.e. a knock-in put option given to the issuer by the holder, which mitigates risk for the issuer and decreases the price for the holder. This put option is also typically contingent on the return space of the underlying asset. More formally, the payoff (to the holder) from the put option is defined as

where K put and b are the dimensionless put strike and barrier parameters respectively and k is a constant notional value. We note that in the case where RT c < K put , the payoff is negative, implying that the contract holder has to pay the contract issuer. As with the set of binary options, this put option is also knocked out if any of the binary options (K i , t i , f i ) is in the money. An example of the full payoff structure for an auto-callable option with a single underlying and 3 payment dates is given in Algorithm A.1.

# Require:

The following displays the payoff scheme of a 3-year auto-callable with yearly payment dates, binary option strike return of 1.1, a knock-in barrier of 0.7, a put option strike return of 1 and a notional value of $18. The timestep values i represents the elapsed time in years and the non-zero payoffs p i at each year from the binary option are $2i. Finally the cumulative return of the underlying asset at timestep i is denoted by Ri c . 1. For i in [1, 2, 3]:

• if Ri c ≥ 1.1: the contract holder receives $2i from the issuer and the contract is immediately ended.

2. After 3 years, if the contract was not previously ended and at any point in time in the last 3 years the cumulative return of the asset was less than 0.7:

It is possible (and simpler) to describe the autocallable option with a single underlying to be contingent directly on the price of the underlying asset as opposed to the return. However defining it as such does not allow us to to trivially generalize it to the case of multiple underlying assets. This is because it is typical to tie the overall option payoff to the best or worst performing asset, where performance is defined in terms of returns. In principle the different underlying assets could have independent put strike returns but this in not common.

The contingent payoffs and the knock-in put mean that autocallables have a payoff that is strongly path dependent. This means that they are computationally expensive to price in practice, sometimes taking five to ten seconds using classical Monte Carlo methods with at least forty thousand paths.

# A.5 Target Accrual Redemption Forwards

A target accrual redemption note (TARN) is any derivative whose payoff is capped at a specified target amount. 4 For the purposes of this paper, we will focus on a commonly used TARN called a target accrual redemption forward (TARF). A TARF is a set of forwards with a couple of knock-out conditions. Specifically, it is a derivative with a single underlying with several (typically 20-60) payment dates and a forward price F . Throughout the contract, we have two fixed strike prices K upper ≥ F and K lower < F . At each payment date t, the payoff is defined as:

where S t is the price of the underlying at the payment date t and α is a positive constant. We note that when S t < K lower , the payoff is negative and hence the holder of derivative makes a loss. The constant α makes this loss asymmetric if it happens and is often one or two.

In addition, a TARF will have two knock-out conditions based on a knock-out threshold b and accrual cap C. The first condition states that if at any payment date the price of the underlying is greater or equal to b, the derivative contract is immediately knocked out (without payment for that date). The second condition is if at any payment date t the total gains of the holder are going to exceed the accrual cap C due to the payoff f t , the contract holder instead only receives the amount such that their total gains sum up to C and the contract is then knocked out. An example of the full payoff structure for TARF with 52 payment dates is given in Algorithm A.2.

# Require:

The following displays the payoff scheme of a 1-year TARF with weekly payment dates, a forward price of $20, strike prices of K upper = $20 and K lower = $15, an α = 2, a knock-out threshold of $30 and an accrual cap of $5. The timestep values i represents the elapsed time weeks.. Finally the price of the underlying asset at timestep t is denoted by S t .

1. Total := $0 2. For t in [1, 2, ..., 52]:

• if S t ≥ $30: the contract is immediately ended.

• if $20 ≤ S t < $30: set f t = S t -$20.

• if S t < $15: set f t = 2(S t -$20) (this will be negative number).

• if Total + f t ≥ $5:

set f t = $5 -Total the contract holder receives f t from the issuer and the contract is ended.

• else:

the contract holder receives f t from the issuer (if f t is negative then the holder effectively gives money to the issuer)

# B Insufficiency of Grover-Rudolph Loading

The Grover-Rudolph algorithm [10] is often cited as a method to efficiently create quantum superpositions that correspond to classical distributions. For a given probability distribution {p i } of a random variable x, the algorithm creates a quantum superposition of the form

The algorithm is inductive in nature and starts by assuming that there is a way to divide the probability distributions into some number 2 m of regions in the domain of interest and create the state

where p (m) i

is the probability for the random variable to lie in region i. Then it aims to add one qubit to the state of Eq. (56), to further subdivide the 2 m regions into a 2 m+1 discretization of the probability distribution with an evolution of the form

where α i (β i ) is the probability for the random variable to lie in the left (right) half of region i. Letting x i L and x i R denote the left and right boundaries of region i, the function

is the probability that, given x lies in region i, it also lies in the left half of the region. If we can construct a circuit which performs the computation

with θ i = arccos f (i), then a controlled rotation of angle θ i on the m + 1th qubit yields

After uncomputing |θ i , we are left with

which is the extension of the state in Eq. (56) to one extra qubit. Performing this iteration n = log 2 N times, we will have a discretization of the distribution over N total number of points across n qubits.

In practice, the efficiency of the Grover-Rudolph method relies on the ability to perform the integrals in Eq. (58) in superposition. The argument in the original formulation in [10] is that probability distributions that can be integrated efficiently classically using probabilistic methods (e.g using Monte Carlo) can be equivalently efficiently integrated quantumly. However, since the ultimate goal in quantum derivative pricing is to provide a faster alternative to Monte Carlo integration over a probability distribution, performing this integral as part of our initial state preparation without any corresponding quantum speedup, nullifies the advantage offered by amplitude estimation as an alternative to Monte Carlo. While efficient from a complexity point of view, this means that Grover-Rudolph is insufficient as a method for quantum advantage in derivative pricing. 5More recently, an approximate method to implement the Grover-Rudolph algorithm for standard normal probability distributions was presented in [31], where the authors suggest the expression in Eq. (58), written as

can be approximated as

for small δ. As the δ parameter decreases with each iteration of the Grover-Rudolph algorithm adding a qubit to the discretization, the authors highlight that for m ≥ 7 the approximation in Eq. (63) becomes sufficiently accurate. However, because the Grover-Rudolph construction is iterative, the m < 7 terms need to be computed before the above approximation becomes possible. As such, the integrals in Eq. (58) are computed classically and then loaded into the corresponding quantum registers. While this approximation allows the simplification of the general Grover-Rudolph algorithm for standard normal distributions after a certain point in the iteration, it does not change the fact that it requires computing integrals over the entire domain of the probability distribution, thus making it practically infeasible for the same reason as the original Grover-Rudolph method.

# C Fixed-point Quantum Arithmetic Resources

This section reviews preliminaries for common quantum arithmetic operations and the synthesis of arbitrary rotations. These operations are used in resource estimation and error analysis. Quantum arithmetic is required for path loading using the Riemann summation method (Section 4.1) and the re-parameterization method (Section 4.2), as well as the payoff calculation described in Section 5.

For the Riemann sum method, we need to perform all the arithmetic operations involved in Eq. ( 12) as well as compute the arcsine and square root of a quantum register for the payoff calculation in Eq. (15). We identify algorithms for performing individual arithmetic operations efficiently, where resources are usually reported as a number of Toffoli gates or T-gates. In cases where we employ arithmetic algorithms from previous work in the literature, we report the gate cost in terms of the gate set reported by the authors.

As we are working in the fault-tolerant setting, we estimate the T-depth of the circuits in a Clifford + T gate set decomposition and assume Toffoli gates can be constructed with a T-depth of one using ancilla qubits [32]. For each operation we assume that we can parallelize the resulting circuits wherever possible.

# C.1 Resource Estimation

We perform all calculations in fixed-point arithmetic similarly to [33], which allows us to use the quantum algorithms for reversible function evaluation described therein. An n-bit representation of a number x is

where x i ∈ 0, 1 denotes the i-th bit of the binary representation of x and p denotes the number of bits to the left of the binary decimal point. The choice of n and p controls the error that we allow in each calculation as well as the resources required to perform arithmetic on the registers. Once we choose the values of (n, p) so that the overall arithmetic error is acceptable for the problem under consideration, we keep them constant throughout the analysis. It is possible that we can tailor these values for different components of the circuit and reduce the overall resources required, but for simplicity in this paper we ignore this potential optimization.

Let TF f and T f denote the number of Toffoli gates and the T-depth required to compute an arithmetic function or logical operation f . The estimates for the operations are functions of the fixed-point register size (n, p) that will be used to represent the underlying quantum states involved in the computations.

Addition/Subtraction Using the algorithm described in [34], we can perform addition of two n-qubit registers in place with a Toffoli cost of 10n -3w(n) -3w(n -1) -3 log 2 n -3 log 2 (n -1) -7 where w(n) denotes the number of ones in the binary expansion of n, and a Toffoli depth of

Note that subtraction is given by a -b = ∼ (∼ a + b) and so can be implemented as an addition with 2n extra X gates, which does not change the Toffoli count.

We can turn an addition gate into a controlled addition gate by using the method shown in Figure 3 in [35]. This requires an additional n-qubit ancilla register, along with two sets of n parallel controlled swap gates. Each individual controlled swap gate is comprised of 3 Toffoli gates in series.

Multiplication For multiplication we follow the method from [33], which uses the controlled addition circuit in [36] and requires a Toffoli count of

This method can also be used for division of a quantum register by a classical value, which we do by inverting the classical value and employing the multiplication algorithm. The controlled additions in the fixed-point multiplication method from [33] require ancilla qubits proportional to the register size, but the circuits include uncomputing the ancillas, meaning that they can be reused for each subsequent addition that is not done in parallel. Because we parallelize the computations across the d assets and T timesteps, we include an additional T * d * n qubits when we count the total to account for these required ancilla qubits.

We can additionally parallelize each multiplication circuit, by considering the register of one factor as z ≥ 1 independent registers of size n/z, and each controlled addition can happen in parallel for the z subregisters. This requires n • (z -1) extra qubits and z -1 additions to accumulate the z sub-results into the final result. z = 1 denotes that no extra parallelization is employed. If we can parallelize the pairwise accumulation additions as well, we arrive at a total T-depth cost of parallelized fixed-point multiplication given by

(T add + 6) is the T-depth of a controlled addition discussed in the Addition/Subtraction section.

# Square Root

We employ the square root algorithm described in [37], which we extend for quantum registers in fixed-point representation. For an (n, p)-sized number x, we can compute √ x by treating x as an n-digit integer, and then shifting the result to the right (n -p)/2 times. This amounts to performing

The Toffoli count of this square root algorithm is [37] TF

The T-depth of this algorithm as reported by the authors is given T sq (n) = 5n + 3 and requires 2n + 1 qubits.

# Logical Operations

For comparisons between quantum registers or between a quantum register and a constant, we use the logarithmic comparator from [34] with Toffoli/T-depth of 2 log 2 (n -1) + 5, which includes uncomputing the intermediate ancillas. The logical OR operation for a 2-qubit input can be performed with a Toffoli/T-depth of one [6].

Exponential In [33], the authors introduce a generic quantum algorithm to calculate smooth classical functions using a parallel piecewise polynomial approximation. We apply this to estimate the resources of computing exponentials. The algorithm takes parameters k and M , which control the polynomial degree chosen for the piecewise approximations and the number of domain subintervals respectively. The total number of Toffolis is given by

This algorithm, which we also use to compute the arcsine function, requires k iterations of a multiplication and an addition, where k-degree polynomials are used for the approximation. Additionally, for M chosen subintervals, it requires M comparison circuits between the n-qubit input register and a classical value. Using the comparator from [34] with T-depth of 2 log 2 (n -1) + 5, the T-depth of a parallel polynomial evaluation circuit is

where z is the optional parallelization factor introduced in the resource estimation above for the multiplication circuit. The qubit count for the parallel polynomial evaluation scheme for choices of the polynomial degree k and number of subintervals M is given by [33] 

Arcsine To calculate the arcsine we employ the algorithm from [33] just as we do for the exponential. However, because the derivative

diverges near ±1, the authors use the transformation

to handle the interval x ∈ [0.5, 1]. Since the computation of the arcsine requires a conditional square root evaluation of the argument and, whenever we need to calculate an arcsine, we have to calculate the square root as well (e.g Eq. ( 15)), we can instead use the transformation

The resource estimation considerations then follow similarly to those in Appendix D.1/D.2 of [33]. We need:

• A comparator to check if x < 0.25 ( √ x < 0.5) that indicates whether we need to apply the above transformation, which would require two Toffoli gates assuming the value in the quantum register is normalized.

• A conditional subtraction and conditional copy depending on the comparator value above to either prepare √ x or √ 1 -x. A conditional copy requires n Toffolis, a conditional subtraction requires TF add + n Toffoli gates [33].

• TF sq Toffoli gates for the square root computation [37].

• The Toffoli gates required for the polynomial evaluation from [33] to compute the arcsine.

• A conditional copy and conditional subtraction depending again on the comparator result from the first step, to get either arcsin( √ x) for x < 0.25 or π/2 -arcsin( √ 1 -x) otherwise.

With the above considerations and the Toffoli count for the polynomial approximation of arcsin(x) from [33], the total Toffoli count for computing |arcsin √ x is

(75) The T-depth for computing arcsin( √ x) of a number x represented in a register of size (n, p), calculated similarly to the exponential is

where T sq (n) = 5n + 3 is the T-depth for the square root algorithm from [37]. The operation will require q arcsq qubits, where the qubit requirements for the arcsine will be given by Eq. (71) for a choice of k and M , and 2n + 1 for the square root operation

R y We use R y (θ) rotations in the variational preparation of Gaussians discussed in Sec. 4.2.1 and controlled-R y rotations to encode the payoff into the amplitude of an ancilla in Eq. ( 16) as well as the transition probabilities in the Riemann summation method in Eq. (28). Using the method described in [38], an arbitrary single-qubit unitary can be performed within precision with a T-depth of approximately 3 log 2 (1/ ). 6When the angle θ we wish to rotate is stored in a separate register |θ , we require a series of R y (θ k ) rotations, each controlled on the kth qubit of |θ where

A single controlled-R n can be performed with an R n -depth of one, R n -count of 3 and with a single ancilla qubit using the decomposition from [40]. However each rotation contributes an error so if |θ is an n-qubit register (with p bits to the left of the binary point), the end-to-end operation can be performed to precision with T-depth of at most 3n log 2 (n/ ). We can reduce this depth slightly by noticing that the amplitude increase due to any controlled-R n rotation where θ k < arcsin( ) is less than and hence is unnecessary. Therefore using that observation and Eq. (78), we compute the total number of rotations required to be n -max( log 2 (arcsin( ) + (n -p), 0). This gives us a final T-depth for a controlled-Ry(θ) operation of

where ñ = n -max( log 2 (arcsin( ) + (n -p), 0).

# C.2 Error Analysis

Given the fixed-point representation of Eq. (64), each arithmetic operation involving registers results in some approximation error, depending on the specific method used. Here we outline the arithmetic error associated with each of the operations described in the previous section.

# Addition/Multiplication

We use the fixed-point addition and multiplication methods described in [33], where the addition of two (n, p)-sized registers introduces an error bounded by A = 1 2 n-p , and the error associated with multiplication is at most

For (n, p)-sized registers X and Y , where each register already contains additive errors X , Y and each factor X, Y is bounded above by b, the error in the computation of X • Y is given by

Exponential We employ the parallel polynomial evaluation methods from [33] to estimate the resources and associated error in computing exponentials. The error associated with the algorithm depends on choices for the degree of the polynomial approximation and the number of subintervals chosen, but the authors provide explicit error estimates and corresponding required resources in Table II for errors ranging from 10 -5 to 10 -9 . We use these in our overall error estimate. In our case, we compute the exponential of a register that itself contains arithmetic error ξ. Denoting the error in computing the exponential of a register exp , the total arithmetic error in computing the exponential of a register can be approximated to first order in ξ in the Taylor expansion of exp(-x + ξ) as

Square root As discussed in the previous section, for square root computations we consider the square root algorithm described in [37], extended for quantum registers in fixed-point representation. The mapping in Eq. (67) introduces a maximum error of sq = 1 2 .

(83)

When computing the square root of a register x which already contains (positive) additive error ξ, the total additive error from the square root operation is bounded by sq + √ ξ. This is easily seen by observing that if we have a square root algorithm which gives us an estimate x with | √ x -x| ≤ sq , then

where the first inequality follows from (

Arcsine For the arcsine calculation we again use the polynomial evaluation method from [33],

where the authors give sample resource estimates for error rates ranging from 10 -5 to 10 -9 . We want to bound the error from the computation of arcsine on a register containing an arithmetic error ξ to begin with. As discussed in Appendix C.1 we only need to compute arcsin(x) for x ≤ 0.5.

In addition, whenever we are computing the function arcsin(x) in our algorithms presented in the paper, we are only doing it for x ≥ 0. This gives us a domain of 0 ≤ x ≤ 0.5 for our arcsin(x) error calculation. Given this domain, we notice that the slope of arcsin(x) is always monotonically increasing with a maximum at x = 0.5. Therefore computing the error when x = 0.5 gives us the upper bound:

where arcsin is the error from the computation of the arcsine from [33], given a choice of polynomial degree and number of subintervals.

Sine As discussed in the previous section, we compute the sin(θ) function with a series of controlled-Ry rotations controlled on qubits from a register containing the angle θ. We can bound the error from the computation of sin(θ) when the register that is supposed to represent θ is actually representing θ + ξ due to an arithmetic error. To quantify the upper bound, we notice that in the domain of 0 ≤ θ ≤ π/2, the slope of sin(θ) is monotonically decreasing, and therefore has a maximum slope at θ = 0. Therefore computing the error when θ = 0 gives us the upper bound:

where we have used the inequality sin(a + b) ≤ sin(a) + b for b ≥ 0 and where sin is the error arising from the gate decomposition of the Ry operator discussed in Appendix C.1.

# D Riemann Summation D.1 Riemann Summation Path Loading Resource Estimates

In this section, we examine the T-depth and qubit count required to compute Eq. ( 12) in a quantum register, and encode that value into the amplitude of an ancilla qubit as described in Algorithm 4.1.

The calculation is done in log-return space (see Sec. 2.2) and it involves the resource estimates for the operations that we introduced in Appendix C.1.

Let T f and q f denote the T-depth and qubit count required for an operation f respectively. Assuming we can parallelize the computation across the d assets and T timesteps wherever possible, the contributions to the resources for computing |arcsin P ( R) with P ( R) given by Eq. ( 12) are • T add for computing the terms (R -µ) which can be done in parallel for d assets and T timesteps, where T * d * n qubits are used to hold the log-returns R for all assets and timesteps.

• T mul for all R 2 terms in the expansion of Eq. (33) (in parallel for all d and T ), requiring T * d * n additional qubits.

• T mul * d 2 /(d/2) for all R i R j terms in the expansion of Eq. (33) (parallel in d, T ) and T * d 2 * n qubits.

• T add * log d 2 + d to sum all the terms in Eq. (33) in parallel. The qubits from the previous step can be reused here.

• T exp to calculate the exponential in Eq. ( 9), requiring q exp extra qubits with q exp given by Eq. (71) for a choice of parameter values determined by the desired approximation accuracy.

• T arcsq to calculate the arcsin and square root in |arcsin P ( R) , with qubit resources given by Eq. (77). • T exp to calculate the prices across all assets and all timesteps in Eq. (8) in parallel, using q exp * d * T more qubits.

• A T-depth of 3n log 2 (n/ ) to perform the ancilla rotation in Eq. (28) to precision , controlled on the register where |arcsin P ( R) is computed This requires n ancilla qubits using the controlled-R y decomposition from [40].

Moreover, we will need an additional register of size T * d * n to implement the addition circuit used in [37] with constant T-depth and (z -1) * T * d extra qubits if we use the parallel multiplication scheme described in Appendix C.1 during the calculation of prices across assets and timesteps, where z ≥ 1 is the optional parallelization factor we choose. Note that we have not included extra qubit counts to compute the (R -µ) terms and the sum in Eq. (33) because we can do these in place using the existing registers we have to hold each R i . This is possible because after we compute the sums and exponentials in Eq. (8) (which we can do before computing the sums) we do not need the values of R i again.

The total T-depth of the Riemann summation path loading process to precision for d assets and T timesteps using registers of size (n, p) is then

) where the dependency of T exp and T arcsin on denotes that the polynomial approximation parameters k and M in Eq. (70) for each function will depend on the target accuracy of the process. The total number of qubits required is q RS (n, p, d, T, ) = T n 4d + d 2 + 3n + 1 + q exp (n, p, )(1 + dT ) + q arcsin (n, p, ).

# D.2 Importance Sampling for Normalization in Riemann Summation

Within this section, we introduce a technique closely related to classical importance sampling to overcome the problem of the exponentially increasing scaling shown in 4.1. The main idea is to approximate the target distribution by another distribution that can be loaded efficiently and then use quantum arithmetic only to adjust for the (multiplicative) error. Suppose a univariate probability density function f : [0, 1] → [0, P ], with P > 1 and 1 x=0 f (x)dx = 1 and a payoff function g : [0, 1] → [0, 1]7 . As introduced before, we can consider the scaled function f (x)/P and a corresponding operator F, as well as a corresponding operator G to prepare a state on n + 2 qubits given by

where we set x i = i/N . Then, the probability of measuring |11 in the last two qubits is given by

and when multiplied with P corresponds to the Riemann sum approximating

Further, let us consider a probability distribution h(x i ) ∈ [0, 1] that can be efficiently loaded into a quantum state, i.e., where we know how to efficiently construct a quantum operator H such that

Suppose now that we have h such that f (x)/(h(x)N ) ∈ [0, 1] for all x, then we can construct a new operator F h defined as

Combining H and F h leads to

which implies a probability of measuring |11 in the last two qubits given by

i.e., the Riemann sum approximating

] for X ∼ f . Thus, if we can find such a probability distribution h, we can construct a state that directly corresponds to E[g(X)] without the need to rescale by multiplying P . It can be easily seen that for P ≤ 1 we can set h(x) = 1/N to recover the original approach without importance sampling.

In case of multivariate probability density functions, we distinguish three cases. First, separable functions that we can write as a product of univariate functions f t for t = 0, . . . , T . In this case, the univariate approach can be applied directly and we need to find a corresponding h t for each f t . Second, non-separable multivariate probability density functions f : [0, 1] d → [0, P ], with P > 1 and x∈[0,1] d f (x)dx = 1. Suppose we discretize each dimension using n qubits, i.e., we have in total N d grid points. Then, we need to find a probability distribution h such that f (x)/(h(x)N d ) ∈ [0, 1] for all x, and the analysis is analog to the univariate case. Last, we consider the case of a multivariate probability density function coming from a stochastic process and given by

where x t ∈ [0, 1] d and f 0 (x 0 ), f t (x t | x t-1 ) ∈ [0, P ] for t = 0, . . . , T . Suppose a separable probability distribution

that can be loaded efficiently as well as a corresponding decomposition h t (x t ) = h t t (x t )h t+1 t (x t ), with h T +1 T (x) = 1. Then, we can write

Thus, if we find h such that the individual h t can be efficiently loaded and

∀x 0 (97)

then, we can efficiently load the stochastic processes without the exponential scaling overhead P T +1 . Again, it can be easily seen that for P ≤ 1 we can set h t (x t ) = h t t (x t ) = 1/N d and h t+1 t (x t ) = 1 to recover the original approach without importance sampling. Note that even though we may not always find an h that satisfies all requirements, this approach can still help to lower the overhead coming from scaling.

# E Re-parameterization Path Loading Resource Estimates

To prepare the standard normal distributions that we require in the re-parameterization loading approach, we can employ the variational method described in Sec. 4.2.1 and the corresponding gate/qubit cost depending on the desired accuracy of the approximation. In addition to that, we will also have to incur the cost of computing the affine transformation R t = µ t + L Rt as described in Algorithm 4.2. Note that the affine transformation is required when we need to calculate the asset prices from the log-returns, which for asset j at time t will be

The graphical representation of the circuit that performs this calculation is shown in Fig. 5 One complication in Eq. (99) is that we cannot compute each asset price fully in parallel across the d assets, because the log-returns of any correlated assets will contribute to the computation of each other's price. In the case where all assets are pairwise correlated, we will need to compute the contributions to each asset's price from the log-returns of all d assets at that timestep, requiring in total d 2 additions to compute all asset prices per timestep. We can however perform d additions in parallel where the contribution of asset j's return to the price of asset (j + i)%d is computed for a choice of i ∈ [0, d -1], since all d such operations have distinct source and target registers. Then d rounds of additions will compute the term d-1 i=0 L ji Rt i for all assets, and if we compute R(t = 1) + R(t = 2) + • • • + R(t = t ) in a separate register for each t and each asset, the above calculation can be also parallelized across all timesteps. This procedure is illustrated in Fig. 6.

The arithmetic error in computing Eq. (99) can be minimized by increasing the qubit register sizes to accommodate the largest values possible for the sums over the timesteps T and assets d. If each gaussian prepared in Eq. (37) is discretized using n qubits, then n + log 2 T qubits will be enough to hold the largest value of the sum represented by Rt i . An additional log 2 d qubits will achieve the same for d-1 i=0 L ji Rt i , assuming the coefficients |L ji | ≤ 1 for all i, j. This condition is not hard to satisfy for typical situations of practical interest, which we can argue by looking at the elements of the covariance matrix Σ ij = ∆tρ ij σ i σ j (where by definition |ρ ij | ≤ 1). Typically, annualized volatilities are smaller than 100% (i.e. σ i < 1) and the timestep usually satisfies ∆t < 1, meaning the price of the underlying assets needs to be sampled more frequently than just yearly. If neither condition is satisfied however, we can choose a smaller ∆t to ensure |Σ ij | < 1, at the cost of increasing the number of timesteps in the calculation.

The contributions to the T-depth and qubit count for loading the paths and computing the asset prices in the re-parameterization approach for a derivative defined on d assets T timesteps are • T Ry (n) • (L + 1) T-depth for loading the gaussian states in Eq. (37) using the variational method from Sec. 4.2.1, where each Gaussian is prepared in parallel and the variational ansatz has depth L. This step requires T * d * n qubits where n qubits are used to prepare each Gaussian state.

• T add * (T -1) for calculating all the component-wise sums

), requiring an extra T * d * (n + log 2 T ) qubits (see Fig. 5).

• T mul * d to compute all contributions to d-1 i=0 L ji Rt i in Eq. (99) and T * d * log 2 d more qubits.

• T add to compute the µ j t + ln S t=0 j contribution in Eq. (99) across assets and timesteps.

• T exp to compute the exponential in Eq. (99) across assets and timesteps, and q exp * d * T additional qubits with q exp given by Eq. (71).

All in all, the total T-depth for path loading using the re-parameterization method to precision for d assets and T timesteps is

with qubit count q RP (n, d, T ) = (n + n + q exp (n, )) dT,

where n = n + log 2 T + log 2 d .

# F Method for Gaussian Loader Training

In this section we illustrate an approximate method to initialize the quantum register using the Variational Quantum Eigensolver (VQE) approach [22]. This algorithm features a parametrized circuit which in turn produces a parametrized state |ψ({θ}) that approximately represents the target state |φ 0 and updates its parameters {θ} to optimize the expectation value of a suitable cost function. Here we show that the choice of the cost function to optimize is crucial for the success of the training.

# Energy based training

As a first method, we adopt a physics-based approach and define an operator H, such that its expectation value E assumes its lowest possible value, E 0 , when evaluated on the target state,

In physics applications, the operator H is usually called the Hamiltonian, E the energy, and |φ 0 the ground state. It is well known the Gaussian function is the ground state of the quantum harmonic oscillator Hamiltonian

where X is the position operator in real space, and P = -i d dx is the momentum operator [41,42]. m is a parameter that determines the variance of the desired Gaussian distribution, and x 0 is the center of gaussian distribution. In this case, as we seek to find a state φ 0 (x) such that φ 2 0 (x) = N (x 0 , σ), we have to set m = 1/(2σ 2 ). We notice that it is always possible to find a generating Hamiltonian function such that its ground state is the square root of the smooth distribution function that we aim to load.

To translate these considerations into an operational workflow we just have to define a way to compute the expectation value of Eq. (104) using a quantum computer. To this end we observe that the operator X 2 is diagonal in the computational basis, so it can be measured directly from the bit-string histogram counts N counts (j) generated by the repeated wavefunction collapses. The operator P 2 is diagonal in the momentum basis. This implies the addition of a centered Quantum Fourier Transform (QFT) circuit after the state preparation block. We use the centered Fourier transform to allow for negative momenta [23]. As introduced in the main text, we work in discrete position space x i = -w + i ∆x, with i = 0, • • • 2 n -1, and ∆x = 2w/2 n . Without loss of generality we choose the domain to be centered at zero. The energy, E = E X 2 + E P 2 , can be computed in the following way,

where N shots is the total number circuit repetitions for the spacial and momentum basis. N counts (j) (with 0 ≤ N counts (j) ≤ N shots , j N counts (j) = N shots ) is the number of measurements that collapsed onto the qubit basis state corresponding to the binary representation of integer j. This strategy bypasses the need to obtain a Pauli representation of Eq. (104), which would include an exponentially increasing number of Pauli strings to be measured with the qubit register size.

The first step of our program is to verify numerically the possibility to prepare a state that systematically converges to Eq. (103), using a quantum circuit. Adopting a variational approach

Figure 6: Circuits that compute asset prices |S t i in separate quantum registers for d assets at timestep t using Eq. (99). The top figure shows the circuit which takes the cumulative log-returns for each asset created by the circuit in Fig. 5  Rt i requires one extra addition and exponentiation to compute the asset price |S t i (bottom figure), which can also be applied in parallel for each asset. Both circuits can be applied in parallel across all timesteps T of the calculation. For more details on the ADD/MUL/EXP operators, see Appendix C.

will circumvent the need of costly quantum arithmetic operations at the expense of introducing sources of error which are always present in numerical variational approaches. The most trivial one concerns the possibility of getting trapped in local minima during the (classical) optimization procedure. The second, and more profound one, is linked with the representational power of trial states produced by the (shallow) quantum circuits.

Our main choice for the ansatz is the so-called R y -CNOT circuit [43]. The initial state, defined on an n-qubit register which we set to |0 ⊗n , is evolved under the action of a unitary U ( θ) to give the trial wave function |ψ( θ) . The circuit is made of a series of L blocks built from single-qubit rotations U R ( θ k ), followed by an entangler U ENT , that spans the required length of the qubit register. In our tests, we used the simplest choice of a ladder of CNOT gates with linear connectivity, such that qubit q i is target of qubit q i-1 and controls qubit q i+1 , with i = 1, • • • , n -2. One additional layer of U R gates is applied at the end, such that the number of variational parameters is n × (L + 1).

Since the single-qubit rotations are all local operations, U R ( θ k ) can be written as a tensor product of rotations of a single qubit:

where R y (ϑ k qi ) is a rotation on the Y-axis on the Bloch sphere of qubit q i , and k = 1, • • • , L + 1. The full unitary circuit operation is described by

and the parametrized state is

Note that the unitary U ( θ) describes the full circuit, but not the pre-measurement change of basis required to collapse the wavefunction in momentum space as explained above.

For each value of parameters n and L, we repeat the optimization runs eight times in order to gather sufficient statistics, as it may happen that the optimizations remain stuck in suboptimal minima. Since we use classical emulation of the quantum circuits the only source of error in the optimizations originates from the classical optimizer. In our runs we first perform a warm up run with the COBYLA optimizer, followed by a longer run using the BFGS optimizer. To enhance the efficiency of the optimizations, the starting point for the VQE run at depth L, uses the optimal parameters found at previous optimization at depth of L-2 or L-1 when available. We notice that the part of the algorithm that concerns the classical optimization feedback can be greatly improved, for example using gradient based methods [44] or imaginary-time inspired update schemes [45].

L ∞ training refinements As discussed in the main text we use pre-optimized circuits obtained using the energy optimization method as a starting guess, and then re-optimize using the L ∞ as the cost function. In Fig. 7 we show indeed how the direct L ∞ optimization consistently fails to provide accurate results.

We show the complete outcome of the optimizations in Fig. 8. This careful numerical study shows that the convergence to the exact ground state is exponential in the depth, and therefore the number of gate operations.

# Failure of the L ∞ norm direct optimization

We provide an empirical explanation concerning the observed failure of the direct norm optimization technique. To this end we probe the cost function landscape for both methods, the energy-based and the direct L ∞ optimization, We start from an optimized parameter configuration θ 0 and we perform a cut in the parameter space, using θ = θ 0 + λ η (110

where η is an vector containing uniformly distributed random numbers in the range [-1, 1], and λ ∈ [-π, π] is a scalar which parametrizes the deviation from the optimal solution.   We plot here the best of the eight independent optimizations for each parameter. Empty symbols correspond to optimizations performed using the energy of the quantum harmonic oscillator as a cost function, while solid symbols denote the refined optimizations using the L∞ as cost function. Right figure: we plot the difference in energy of the associated quantum harmonic oscillator model. As expected the refinement targeting the L∞ does not improve this quantity.  In Fig. 9 we probe the cost function landscape for three different cut direction (e.g. three different realizations of the vector η). We observe indeed that the cost function defined by the L ∞ norm is much more corrugated than the one defined by the energy E of the associate quantum mechanical toy problem, which instead displays a smoother surface. Crucially the basins of attraction of the energy cost-function and the L ∞ cost-function are overlapping (this happens because the ground state of the physical problem is very close to the Gaussian function we want to achieve), therefore the second optimization with the L ∞ norm does not remain stuck in high-cost local minima outside such basin.

Variational parameters digitization. While our numerical results provide evidence for a rather efficient Gaussian state preparation in terms of circuit depths for a parametrized circuit, an additional step has to be made in view of a fault-tolerant implementation of such circuits. In this new-framework, the continuous rotation R y gate needs to be expanded as a finite product of discrete operations. Following again the Solovay-Kitaev theorem, or more specialized results [25], it is possible to also have an efficient representation of any SU (2) operator with a sequence of Clifford + T gates that scale logarithmically with the threshold error . We investigate how the results obtained before can be transferred in this regime where rotation angles can only take discretized values. We therefore assume that each parameter ϑ k qi can only be represented in the format i * 2π/M digit , where i is an integer.

We adopt a simple protocol to optimize the parameters on an a grid. First we project the original continuous parameter values on the grid, choosing the closest grid point for each parameter. Subsequently, we perform a local search on the grid to find a better combination of the digitized parameters which minimize the L ∞ norm difference compared to the target distribution. We numerically show that the error introduced by such digitization decreases systematically with the mesh size. Interestingly, if we consider the error in the L ∞ norm difference introduced by this digitization, it decreases as O(1/M digit ). We observe that in all cases, we are able to obtain values comparable, or better, with the continuous solution, when the mesh size reaches M digit ∼ 10 5 , which is equivalent to discretizing the space using 2π/M digit ≈ 0.0001 rad.  

# Acknowledgments

We thank Paul Burchard for guidance on the derivative pricing problem domain and Thomas Häner for useful discussions regarding quantum arithmetic. We thank Graham Griffiths, Alex Hurst, Dunstan Marris and Elmer Tan for their technical and business insights on derivative products. We thank Ryan Babbush for suggesting clarifications to the manuscript. SC contributed to this work during his internship at Goldman Sachs.

