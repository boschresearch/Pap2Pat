# Introduction

Stochastic processes play a fundamental role in mathematics, physics, engineering, and finance, modeling time varying quantities such as the motion of particles in a gas, the annual water levels of a reservoir, and the prices of stocks and other commodities. One potential application of quantum computation is to better estimate properties of stochastic processes or random variables derived therefrom. A long line of works have shown that one can quadratically improve the precision of estimating expectation values of random variables, using quantum amplitude estimation and variants thereof [AW99, Hei02, HN02, Hei03, BDGT11, Mon15, HM18, Ham21, KO22]. For example, if one wishes to estimate the expectation value of a random variable that one can efficiently classically sample, then classical Monte Carlo methods require Θ(1/ 2 ) samples toapproximate the mean, while quantum algorithms can do so using only Θ(1/ ) calls to the classical sampling algorithm in superposition. These algorithms are optimal in a black-box setting [BBBV97,NW99]. Such algorithmic approaches have received much attention as a potential application of quantum computation. For example, there has been much excitement about the possibility of using this approach for the Monte Carlo pricing of financial derivatives and risk analysis, e.g. [RGB18, WE19, BvDJ + 20, EGM + 20, SES + 20, EGMW20, CKM + 21, DLB + 21, DLB + 22].

However, achieving a practical quantum speedup for estimation of expectations over stochastic processes is challenging, even with potential future improvements in quantum hardware. This is for two reasons. First, in these algorithms one must simulate the underlying random variable/stochastic process in quantum superposition. That is, one needs to coherently prepare a quantum state which encodes the randomness used to generate the trajectory as well as a trajectory of the stochastic process under consideration. While in principle this can always be done in the same amount of time to classically simulate the process -for example by compiling the classical simulation down to Toffoli gates with uniform random seeds as input -in practice this can result in prohibitively large gate counts in the simulation circuit. Second, one must not only simulate the above simulation circuit once, but (O(1/ )) in series in order to achieve the quadratic quantum speedup1 . The depth for the simulation circuit is therefore another bottleneck in obtaining speedups for quantum Monte Carlo methods. Due to these constraints, it has recently been noted that in certain future projections of quantum hardware development, the clockspeed overheads of quantum error correction might overwhelm the quadratic speedups for relevant parameter regimes [BMN + 21, Tro21]. For example, recent estimates of the effective error rate needed to implement financial derivative pricing in a practical setting using state of the art algorithms has revealed it might require many orders of magnitude improvements over existing hardware [CKM + 21].

Fortunately, these quantum Monte Carlo algorithms naturally compound with any speedup in the process simulation. Therefore, a critical goal is to find a quantum speedup for simulating stochastic processes, or at the very least a more gate-efficient method of simulating such processes, to render these techniques practical in the future. Indeed, [Mon15] noted that quantum walk methods can achieve such a speedup in certain cases, and used this to show a quantum algorithm for estimating the partition function of the Ising model exhibiting a quadratic speedup in both the error parameter -1 and the mixing time of the corresponding random walk over classical methods. In a similar spirit there has been interest in efficient loading of particular probability distributions, such as the Gaussian distribution [RSMP21], into quantum registers for future use in finance algorithms.

## Our results

In this work we study the quantum simulation of stochastic processes for use in Monte Carlo algorithms. We focus on two questions: first, beyond quantum walks, are there scenarios can one create a coherent quantum simulation of a stochastic process using significantly fewer gates than trivially "quantizing" a classical simulation algorithm (i.e. compiling to Toffolis)? And second, could this create an end to end algorithm for an any potentially relevant applications which surpasses classical Monte Carlo?

We answer both questions in the affirmative. First, we introduce a new notion of stochastic process simulation which we call the analog simulation of a process, as opposed to the digital simulation obtained by "quantizing" a classical algorithm. We then show that one can create a highly efficient analog simulation for Brownian motion (BM) and a generalization thereof known as fractional Brownian motion (fBM). In particular we show how to -approximately simulate a T -step Brownian motion process in merely Õ(polylog(T ) poly( -1 )) qubits and even shorter circuit depth.

Theorem 1.1 (Main Theorem, informal2 ). There is a quantum algorithm to produce an -approximate analog simulation for fractional Brownian motion with Hurst parameter H ∈ (0, 1], using a quantum circuit with O(polylog(T )+poly( -1/2H )) gates, O(polylog(T )+polylog( -1/2H )) depth, and O(polylog(T )+O( -1/2H )) qubits.

Here the input to the algorithm is a description of the parameters of the fractional Brownian motionnamely the drift, variance and the "Hurst parameter" which describes the amount of correlation or anticorrelation between subsequent steps of the Brownian motion. We define this more formally in Section 2.1. Our algorithm makes critical use of the quantum Fourier transform and spectral properties of fractional Brownian motion, as well as a recursive application of data loading algorithms which uses special properties of this spectrum. Additionally, we generalize these methods to a broader class of stochastic processes known as Lévy processes, albeit with weaker simulation guarantees.

Second, we show how to use this new representation to obtain an end to end quantum algorithm for estimating properties of stochastic processes, which is faster than classical Monte Carlo. This is not straightforward, as our analog simulation makes use of the exponential size of Hilbert space to efficiently encode the stochastic process trajectories. This does not allow one to directly measure quantities readily available in the digital simulation. For example, one cannot easily read out the value of the process at a particular time, similar to how the HHL algorithm does not allow one to extract individual entries of the solution vector of a linear system [HHL09,Aar15]. Therefore, some work must be done to identify properties of stochastic processes which are easily extractable from this analog representation.

To this end, we describe two quantities which are time averages of the stochastic processes which meet this criteria, which can be efficiently estimated by combining our analog simulation algorithm with quantum mean estimation algorithms [BDGT11,Mon15,Ham21,KO22]. For example, we show that one an efficiently price a certain over-the counter financial option currently traded -in particular, an option on realized varianceunder a particular assumption about the evolution of the asset. We also show that one can create an efficient statistical test for anomalous diffusion in fluids. The first algorithm runs in time O(polylog(T ) -c ) where 3/2 < c < 2 is a constant depending on certain parameters of the stochastic process. This is an improvement over classical Monte Carlo which runs in time O(T -2 ), and incomparable3 to standard quantum mean estimation which runs in time O(T -1 ). Our algorithm therefore creates a black-box quantum speedup compared to the best black-box classical algorithm.

We leave open the question of whether our techniques can generate a genuine (white box) quantum speedup for estimating certain properties of stochastic processes. Here the central questions are a) to characterize what sorts of properties of fBM we can estimate with our methods and b) to determine if there exist faster classical methods for computing such properties than classical Monte Carlo sampling. For the particular quantities we consider here, there exist closed-form analytical formulae for these quantities, and therefore our results do not represent white-box speedups over the best possible classical algorithm. However, our technique easily generalize to (mildly) postselected subsets of the process trajectories, which quickly allow one to depart from the regime of closed-form analytical formulae. Therefore we expect that our techniques can easily price certain options or evaluate properties of sub/super diffusive fluids which do not have closedform analytical formulae, and therefore could possibly represent white-box quantum speedups. As with all black-box speedups (including standard quantum mean estimation algorithms), the central question is whether or not faster classical algorithms exist beyond classical Monte Carlo despite the non-existence of closed form solutions. We discuss this further, as well as additional open problems, in Section 1.4.

## Analog vs digital simulation

A discrete-time stochastic process S(T ) is a description of a probability distribution over values v 1 , v 2 , . . . v T of a particular quantity at specified times 1, 2, . . . T . The differences between successive values v i+1 -v i are referred to as the increments of the processes, which might be dependent on one another. For example, the stochastic process describing a particle subject to diffusion will have independent increments, while the process representing the annual water level in a reservoir will have positively correlated increments due to long-term drought cycles [HBS65].

We say one can perform a quantum simulation of a stochastic processes if one can coherently produce a quantum state ψ representing the stochastic process. The complexity of this task might depend on the quantum representation of the stochastic process. For example, a commonly used representation (e.g. as mentioned in [KO22]) is to consider the quantum state

where p v1,v2,...v T is the probability the process takes values v 1 , v 2 , . . . v T , |g is a garbage state entangled with the values, and the sum is taken over all possible values of the tuples v 1 . . . v T . In other words, the ket of the state encodes the trajectory of the process (i.e. the tuple of values v 1 , v 2 , . . . v T ), and the amplitude stores the probability that trajectory occurs. If one traces out the garbage qubits, the diagonal entries of the reduced density matrix are precisely the probability distribution of the stochastic process.

We call this the digital representation of the stochastic process, because it meshes well with classical digital simulation algorithms. Namely, if one has a classical algorithm to sample from v 1 , v 2 , . . . v T in time f (T ), then it immediately implies a quantum algorithm to produce the digital representation in time O(f (T )) -simply by compiling the algorithm down to Toffoli gates, and replacing its coin flips with |+ states 4 . Therefore there is no quantum slowdown for the digital simulation task in general. To the best of our knowledge, the best type of quantum speedup for digital simulation occurs via quantum walk algorithms as noted in [Mon15], where f (T ) goes to f (T ) in certain cases.

In this work we introduce a new representation of stochastic processes, which we call the analog representation. We first describe the analog encoding of a single trajectory (v 1 , v 2 , . . . v T ) of the stochastic process S(T ) is defined as,

Here the value of the process is encoded in the amplitude of the quantum state and the ket stores the time. This representation of the stochastic process manifestly takes advantage of the exponential nature of quantum states -as only O(log T ) qubits are required to represent a T -timestep process. It is an analog representation as the values are stored in the amplitude of the state, rather than digitally in the value of the ket. An -approximate encoding of the trajectory of the stochastic process trajectory is a state such that |ψ v1,v2,...v T -|ψ v1,v2,...v T 2 ≤ . Note that here the representation discards the normalization information, but we will later consider modifications of this formalism which keeps normalization information as well, at the cost of introducing an additional flag register which is 0 on the desired (sub-normalized) state.

Preparing the analog encoding of a single trajectory of S(T ) is equivalent to the task of preparing copies of a density matrix

. Such a density matrix represents a single trajectory of the stochastic process sampled according to the correct probabilities. However, for quantum Monte Carlo methods to estimate a function of a stochastic process, a stronger notion of coherent analog encodings for S(T ) is required.

The coherent analog representation of the stochastic process S(T ) is defined as follows

The coin flip registers then become the garbage register of the above state.

where |g is an orthonormal garbage register entangled with the trajectory v 1 . . . v T . In other words, we assume that tracing out the garbage register yields the state

The garbage register essentially encodes the randomness needed to sample from the process trajectories. The coherent analog representation |S(T ) of the stochastic process is compatible with quantum Monte Carlo methods and can be used as part of the simulation circuit/oracle for estimating a function of the stochastic process using the quantum amplitude estimation algorithm. An approximate analog encoding for |S (T ) is defined similarly where the trajectories generated are approximately correct. We note that a method of preparing ρ directly (e.g. by classically sampling random trajectories and then coherently preparing the trajectory states) is not compatible with amplitude estimation as it is not unitary.

## Proof sketch

Our first result is to show that the mathematical structure of fractional Brownian motion -a fundamental stochastic process that can be used to model diffusion processes like the motion of particles in a gas -is particularly amenable to efficient analog simulation.

# 1.3.1

Step 1: View in Fourier basis using the QFT Our algorithm is derived from combining spectral techniques with the quantum Fourier transform. The starting point is the classic spectral analysis of Brownian motion and its Wiener series representation as a Fourier series with stochastic coefficients. Brownian motion is a continuous time process, i.e. a probability distribution over continuous real-valued functions B(t) : [0, 1] → R, with Gaussian increments between distinct times. There are several mathematical definitions of Brownian motion, but the most helpful is a description of its Fourier series due to Wiener (1924). Wiener observed that Brownian motion5 with zero drift and variance σ on the interval [0, 1] can be written as

where the variables a k are independent identically distributed (i.i.d.) Gaussian variables with mean 0 and variance 1. In other words, when viewed in frequency space, Brownian motion is extremely simple -its frequency components decouple from one another. The Wiener series representation gives rise to a family of classical spectral algorithms for simulating Brownian motion, which are commonly used in computational finance [CDLMR10]. The basic idea is to discretize time to T timesteps, draw a set of random Gaussian variables a k of diminishing variances (typically imposing some cutoff on the maximum frequency considered), and take their Fourier transform to obtain a trajectory of B(t). Classically this takes time O(T log T ) via the fast Fourier transform algorithm [CT65].

Our first key observation is that this classical spectral algorithm offers an opportunity for a highly efficient quantum analog simulation for Brownian motion trajectories via the quantum Fourier transform (QFT). The QFT performs a Fourier transform over a vector of length T using only polylog(T ) qubits and quantum gates -essentially by exponentially parallelizing the FFT algorithm -and is at the is at the core of many quantum speedups, e.g. [Sho99]. Therefore, if one could efficiently prepare a quantum state encoding the Fourier transform of a stochastic process, then by taking its QFT6 one would obtain an analog simulation of the process. The problem of analog simulation therefore reduces to the problem of loading the stochastic coefficients of the processes' Fourier transform. This is the conceptual core of our quantum spectral algorithm.

For Brownian motion we therefore need to efficiently load a quantum state where the amplitudes are distributed as independent Gaussians of diminishing variances7 . As we discuss next, the symmetries of the Brownian motion and the decoupling of the stochastic coefficients allows us to obtain a very efficient quantum analog simulation algorithm for the Brownian motion. A similar analysis holds for fractional Brownian motion as well. Here the Fourier coefficients of the process decouple as well to independent Gaussians, but the functional form of the diminishing variances is given by a power low function of the Hurst parameter which controls the amount of correlation between steps. For simplicity of presentation, we will sketch our algorithm for standard Brownian motion. The extension to fractional Brownian motion will later be shown in Section 4.4 using similar ideas.

## Step 2: Efficient Gaussian loading

Via the QFT, we have shown that to produce an analog simulation of a single trajectory of Brownian motion, we need to show how to efficiently prepare a quantum state encoding its Fourier transform. In other words, we need to prepare the state,

where the a k ∼ N (0, 1) and the series coefficients are independent Gaussian variables of decreasing variance according the function f (k) = 1/k. We call this the "Gaussian loading problem" for the function f (k) = 1/k -and in general one can consider this problem with different decay functions of the variance. The first step of our algorithm is to truncate the Fourier series to a finite number of terms L. That is, we instead prepare the state

This introduces a small amount of error in our simulation algorithm. However, as the function 1/k is rapidly diminishing as a function of k, we show that this only introduces a small amount of error in our simulation. More generally in one wishes to find an -approximate simulation algorithm, this only requires setting L = poly( -1 ).

We then give an efficient quantum for solving this truncated Gaussian loading problem, which we believe may be of independent interest. Our algorithm uses only O(L + log T + log( -1 )) qubits and computation time. Our algorithm applies to a variety of decay functions for the variance -which will play a key role in our generalization to fractional Brownian motion. This algorithm is the technical core of our results.

The starting point for our Gaussian loading algorithm is highly efficient data loader circuits [JDM + 21] for particular quantum states. These are circuit realizations of previous recursive constructions that used specialized quantum memory devices such as those of Grover and Rudolph [GR02] and Kerenidis and Prakash [KP17]. For any fixed values of the a i , one can define a log-depth circuit to load the vector |φ a , by now standard recursive doubling tricks -one simply computes how much 2 mass is on the first vs second half of the state, hard-codes this as a rotation angle between the first and second halves, and recurses in superposition. This results in a log-depth circuit for loading the state, where k is represented in unary.

There are two issues which must be solved to apply this algorithm to our Gaussian loading problem. For one, this loading occurs in unary, and we are using a binary representations of k and T in our analog encoding, but this turns out to be a minor issue which can be solved with low-depth binary to unary converters (see Appendix C). The second and more fundamental issue is that this only describes how to efficiently load a single state, and we wish to load the analog representation of the Brownian motion |B(t) in order to be compatible with quantum Monte Carlo methods.

We solve this by applying the data loading algorithm twice recursively -which we call "data loading the data loader." The basic idea is that for any data loading algorithm A, it takes as input some rotation angles θ, and outputs a state |A( θ) . The data loading algorithms we consider are onto, in other words for any state |ψ , there exists a setting of the angles |θ such that A( θ) = |ψ . Thus, given any distribution D over quantum states, this induces a classical probability distribution D over vectors θ. Therefore, if we could only efficiently load the quantum state corresponding to D , i.e.

where D ( θ) is the probability of θ in D , then by feeding this state into A and tracing out the angle registers, this would efficiently allow us to prepare σ.

If one considers applying this technique directly, however, it turns out to produce highly complex quantum circuits. While there exists a distribution D over data loader angles to produce states of independent diminishing Gaussians, the joint distribution induced on angles is quite complicated. In particular, the angles are highly correlated with one another. In other words, the induced distribution on the angle θ i applied at a particular stage of the algorithm is dependent on the prior angles applied. Therefore, to load the probability distribution on angles D would be prohibitively costly -as it would require solving a highly correlated data loading problem across many qubit registers. This increases the complexity of the data loading circuit which reduces or eliminates our potential advantage from using the QFT.

We circumvent this obstacle in two steps. First, we show one can highly efficiently load large vectors of i.i.d. Gaussians, i.e. where the Gaussian entries all have the same variance. This is because the induced distribution on data loader angles is independent -we show the angles decouple due to symmetries of the high-dimensional Gaussian, which mesh particularly well with the binary tree data-loading circuits. In fact the distribution on data loader angles θ turn out to have a closed form given in terms of the β and γ distributions due to the fact that the sum of squares of k i.i.d. Gaussians are distributed according to the γ(k/2) distribution. Therefore, there is a highly efficient circuit to load these angles -one just loads each angle register separately, and feeds it into the [JDM + 21] circuits. This allows us to quickly prepare quantum states with i.i.d. Gaussian entries.

Second, we show that we can efficiently convert such states into states with decreasing variances with a simple trick. The basic idea is to artificially inject diminishing variances with reversible addition -we first prepare prepare ranging over k have the same distribution as i.i.d. Gaussian amplitudes with decaying variances, irrespective of the value of l. The same technique works for a wide variety of functional forms of diminishing variances, which we discuss in detail in the main text, as it is key to generalizing our algorithm to fractional Brownian motion.

### Sketch of end to end applications

We also provide two end-to-end examples using our analog encoding which provide black-box speedups over classical Monte Carlo sampling.

The first example entails the pricing of a variance swap. A variance swap is a financial instrument which pays out proportional to the mean squared volatility observed in a stock price -so the more volatile the stock, the more it pays out. It can be used as a hedge against volatility, and is traded as an over the counter option in financial markets. We show that we can use our analog encoding to efficiently price a variance swap in certain conditions. At a high level, our algorithm is efficient because the price of a variance swap is naturally a time average of a square of values of the volatility, and it is particularly easy to extract time averages from our analog encoding (as they are certain amplitudes of our state which are relatively large). Our algorithm works under a particular assumption about the time evolution of the price of the underlying asset. In particular, the asset must evolve by Geometric Brownian motion with changing variance, and where the variance evolves by fractional Brownian motion. By combining our algorithm with quantum mean estimation, we can -approximate the value of the option in time O(polylog(T ) -c ) where 3/2 < c = 1+1/2H < 2 where H is the Hurst parameter of the fBM. Our algorithm works better with higher Hurst parameters of the volatility. See Section 6.1 for details. While this particular option has a closed-form analytical solution, we note we can easily apply post-selection on the fBM, for example over paths whose norm lies in a given interval, which would circumvent the possibility of an analytic solution.

Our second example involves a statistical test to distinguish between different diffusive regimes in singleparticle motion. While in ideal fluids particle positions evolve by Brownian motion, in particular sub or super-diffusive fluids, they evolve by fBM with a nontrivial Hurst parameter. We show that we can use our analog encoding for fBM to create a statistical test that distinguishes between a particle following an fBM with given Hurst parameter, or fBM with an alternative Hurst parameter, or even a simple case of a continuous-time-random walk. Our algorithm again runs in time Õ(polylog(T ) -c ), where c > 2 depends on the Hurst parameter of the fBM, rather than Õ(poly(T ) * N ) in the classical case, where N is determined by the discretization used to sample its characteristic function. Unlike our prior application, here we do not run quantum mean estimation, but rather use our simulation directly to produce estimates of the average meansquared-displacement of the particle under certain Hurst parameters, which is compared to the observed data. Therefore this application has a worse scaling in -1 compared to classical, but a better scaling in T . As we will discuss shortly, this could still possibly generate a faster black-box algorithm than classical Monte Carlo in situations with large T .

## Generalizations and Open Problems

There are many open problems remaining. Of course, the most direct one is whether or not our method can produce an end to end asymptotic speedup for computing properties of certain stochastic processes, as previously discussed. Here the basic issue is to identify interesting properties of fractional Brownian motion which are complicated enough to require classical Monte Carlo approaches. In this direction we believe considering functions of postselected subsets of trajectories is the most promising approach. Postselection typically takes one out of the regime of analytical formulae. For example, in computational finance, barrier options (which only can pay out if the price of the underlying asset breaches a certain value at some point in time) typically do not have analytical formulae and therefore are priced by Monte Carlo methods. Postselection slows both our quantum algorithm and classical Monte Carlo in unison, preserving the relative speedup of our method relatively to classical MC. Therefore, if one could find a postelected property of fBM for which the best classical estimation algorithm is classical MC, then this could yield a white-box speedup for our algorithm.

Another possible direction to search for speedups is to consider other inner products one could compute with respect to Brownian Motion. We generalize our algorithm to the following: given a function f (t), one can efficiently evaluate its inner product with BM, i.e. | f (T )|B(T ) | 2 , assuming that one can prepare a quantum state encoding f (t) (for details see Section 6). Our given applications are the special case where f is the indicator function between times t 1 and t 2 . One can ask if other functions might give a quantum speedup.

In any case, quantifying such a speedup would require careful work. For one, there are many parameters at play. To quantify an end to end speedup, one would need to take into account that the parameter T is implicitly a function of (see e.g. [MP16]). For example if one must set T = O( -1 ) vs T = O( -2 ) vs T = O( -1/2 ), then our method's black-box speedup becomes polynomial, but with differing degrees. We note that even if T = O( -1 ), our method's savings in T pushes our algorithms' performance beyond that of standard quantum mean estimation -and the gap only grows if T is larger. Other factors might also affect the apparent speedup -for example if the quantity being estimated is invariant to high-frequency components of the stochastic process (as with a time average), then our algorithms' omission of high-frequency content might result in a better error scaling than our naive bounds, and potentially result in a Õ(polylog(T ) -c ) algorithm where c < 1. For this reason we believe quantifying potential asymptotic speedups for potential problems of interest to be an interesting line of inquiry. More broadly, we leave open the question of whether our techniques can be "de-quantized" in a similar spirit to [Tan19, GLT18, Tan21, CGL + 22, GLG22], i.e. if it is possible achieve a similar polylog(T ) dependence for sampling from values/times of fBM trajectories8 .

Another interesting direction is to explore what other stochastic processes might be amenable to efficient analog simulation. For example, would it be possible to give an efficient analog simulation for Geometric Brownian motion? The case of Brownian motion is particularly nice because its Fourier spectrum decouples. For a general stochastic processes, there are non trivial dependencies between the stochastic coefficients and the resources required for loading the joint distribution of the Fourier coefficients may be prohibitive. However there are more general families of stochastic processes with well-behaved spectra, One reason the Fourier spectrum of Brownian motion is well-behaved it that it is a stationary process, i.e. the joint probability distribution does not change when shifted in time. This cyclic shift symmetry is precisely the symmetry of the QFT, and therefore it might be possible to give simulations for other stationary processes. In another direction, our results use the fact that Brownian motion can be expressed as an integral over white noisewhich is noise with i.i.d Gaussian Fourier components.

In this spirit, in Section 5 we generalize our algorithm to produce analog encodings of trajectories of Lévy processes. Lévy processes are stationary stochastic processes generalizing Brownian motion, which can be expressed as integrals over a linear combination of Poisson and Brownian noise. The quantum simulation method for Lévy process trajectories is obtained by quantizing the classical method that embeds the Toeplitz discrete integration operator into a circulant matrix [DM03]. The method remains efficient in the quantum setting with gate complexity O(poly(log T, 1/ )) as circulant matrices are diagonalized by the quantum Fourier transform and further the Fourier spectrum of Lévy noise is flat, similar to the spectrum of the white noise. However our simulation results for Lévy processes are weaker than those for fBM, as we can only provide an incoherent simulation of these processes due to the coupling of the Fourier coefficients, and therefore cannot combine this method with amplitude estimation. The stochastic integral method can be used to generate encodings of Itô processes that are defined as integrals over white noise and time. We leave open the question of whether the quantum spectral method can be generalized further to (fractional) integrals over white noise and Poisson shot noise-this family of stochastic processes includes Lévy and Itô processes as well as fractional Brownian motions. Indeed our extension to fractional Brownian motionwhich can be expressed as a fractional integral of Brownian motion -is a step in this direction.

There is also the more direct question of whether analog simulation results in smaller quantum circuits than digital simulation for stochastic processes of interest beyond Brownian motion, in a non-asymptotic setting relevant to potential future applications of error-corrected quantum computers. This was part of our original motivation for this line of work, and we hope our work spurs further efforts in this area.

# Preliminaries

We introduce some preliminaries on stochastic processes and quantum computing in this section. In subsection 2.1, we begin with the defining the Brownian motion. More generally, our techniques are applicable to stochastic processes that can be written as stochastic integrals over time and over Brownian motion, these processes include the fractional Brownian motion and Itô processes. Subsection 2.2 introduces the quantum Fourier transform and state preparation circuits that will be used for constructing the quantum encoding for the stochastic processes.

## Brownian motion and Itô processes

The stochastic processes considered in this work are Brownian motion and its generalization to Itô processes. We first introduce the Brownian motion and then the more general processes that can be represented as integrals over Brownian motion. The Brownian motion is defined as follows, Definition 2.1. The Brownian motion is a stochastic process B : R + → R such that:

1. B(0) = 0 and B(t + h) -B(t) ∼ N (0, h) for all t, h ∈ R + where N (0, h) is the normal distribution with mean 0 and variance h. 

# For any finite subdivision

The Brownian motion on R + is obtained by concatenating independent Brownian motions on intervals [kπ, (k + 1)π]. Discarding the drift term in the Wiener series, one obtains the Brownian bridge, which represents a Brownian path with the values at the start and end point fixed to 0. The Fourier series representation of the Brownian motion will also be used for the quantum simulation algorithm. More general stochastic processes can be defined as stochastic integrals over the Brownian motion. The stochastic integral

). An important class of processes defined as stochastic integrals over Brownian motion is the fractional Brownian motion (fBM), a one parameter extension of Brownian motion for a Hurst parameter H ∈ [0, 1]. The fBM with Hurst parameter H = 1/2 corresponds to standard Brownian motion. The fractional Brownian motion was first discussed by Lévy [Lév53] as an integral over the standard Brownian motion.

Definition 2.3. The fractional Brownian motion with Hurst exponent H ∈ [0, 1] is defined to be the stochastic process,

Mandelbrot and Van Ness [MVN68] provided an origin independent fractional Brownian motion given by the Weyl integral, this definition as well can be written in integral form as t 0 K H (s -t)dB s for a Kernel function depending only on the difference (s -t). The definition of fBM used for spectral simulation is that as a fractional integral of the white noise, the BM in turn can be viewed as integral of the white noise.

Stochastic processes that can written as a linear combination of a stochastic integral over Brownian motion and a stochastic integral over time are called Itô processes. An Itô process has a representation of the form,

In addition to fractional Brownian motion, we also develop quantum simulation methods for generating trajectories of Itô and Lévy processes that can be represented as stochastic integrals in section 5.

## Quantum computing preliminaries

We introduce in this section the quantum Fourier transform and logarithmic depth state preparation circuits that are components of the quantum stochastic process simulation algorithm. The quantum Fourier transform is defined as follows,

Definition 2.4. The quantum Fourier transform (QFT) is an N dimensional unitary matrix U with entries given by (U ) jk = e 2πijk/N = ω jk for 0 ≤ j, k ≤ n, where ω = e 2πi/N is an N -th root of unity.

The real and the imaginary part of the the quantum Fourier transform are known as the discrete cosine transform (DCT) and the discrete sine transforms (DST) respectively. It is well known that the quantum Fourier transform (QFT) can be implemented as a logarithmic depth circuit, an explicit implementation using Hadamard and phase gates is provided in Appendix A. It also follows that the logarithmic depth circuit for the QFT can be used to implement the discrete sine and cosine transforms.

The second quantum computing primitive that we use are the logarithmic depth state preparation circuits in quantum machine learning termed as data loaders [JDM + 21]. The data loader circuit is a parametrized circuit that prepares the amplitude encoding |x for a vector x ∈ R n . The data loader circuits are composed of recursive beam splitter (RBS) gates that are two qubit gates given as,

The logarithmic depth data loader circuit is illustrated in Figure 1, it outputs the state |x on input |0 n . The data loader can be viewed as a circuit based realization of binary tree data structure for state preparation. The angles for the beam splitter gates in the data loader are determined by the vector x that is being prepared by the circuit and are deterministic functions for quantum machine learning applications. For the quantum simulation of stochastic processes, the data loader is used with stochastic input, that is the input vector x is not fixed but drawn from a distribution over the unit sphere. The angles in the data loader circuit are thus drawn from a specific distribution, the explicit calculation of the angle distribution for the Haar random vector on the unit sphere will be an important part of the quantum algorithm for simulating Brownian motion trajectories.

More explicitly, the angles for the data loader for vector x ∈ R n are computed using a binary heap data structure where each node stores the sum of squares of the values in its subtree and an angle θ. Denoting the value stored at node j by r(j) and, the angle θ is given by θ = arccos( r(2j) r(j) ) where r(2j) is the sum of squares of the values stored in the left subtree for node j, that is cos 2 (θ) = r(2j) r(j) and sin 2 (θ) = r(2j+1) r(j) . This description is useful for computing the distribution on the data loader angles for a Gaussian random vector.

The data loader circuit produces a unary encoding for vector x using n qubits. It is further possible to convert the unary encoding into a binary encoding with a quantum circuit having depth poly-logarithmic in the dimension of the vector. The circuit for the unary to binary conversion is given in appendix C.

# Quantum encodings of stochastic processes

A discrete-time stochastic process S(T ) is a description of a probability distribution over values v 1 , v 2 , . . . v T of a particular quantity at specified times 1, 2, . . . T . The differences between successive values v i+1 -v i are referred to as the increments of the processes, which might be dependent on one another. A quantum simulation of a stochastic processes is a procedure to prepare quantum state ψ representing the stochastic process.

The complexity of this task depends on the quantum representation of the stochastic process. We recall first the commonly used digital quantum encoding for a stochastic process and then introduce two different types of analog encodings. Definition 3.1. A digital representation for a quantum stochastic processes is defined as the state,

where p v1,v2,...v T is the probability the process takes values v 1 , v 2 , . . . v T while |g is a garbage state entangled with the values, and the sum is taken over all possible values of the tuples v 1 . . . v T .

The registers in the digital encoding store the entire trajectory of the process (i.e. (v 1 , v 2 , . . . v T )), while the amplitude stores the probability that trajectory occurs. If one traces out the garbage qubits, the diagonal entries of the reduced density matrix are precisely the probability distribution of the stochastic process.

We call this the digital representation of the stochastic process, because it meshes well with classical digital simulation algorithms. Namely, if one has a classical algorithm to sample from v 1 , v 2 , . . . v T in time f (T ), then it immediately implies a quantum algorithm to produce the digital representation in time O(f (T )) -simply by compiling the algorithm down to Toffoli gates, and replacing its coin flips with |+ states. There is no quantum slowdown for the digital simulation task, but to the best of our knowledge, nor are there any quantum speedups.

In this work we ask if quantum computation might admit faster algorithms for stochastic simulation tasks. We begin by introducing the analog representation where the values of the stochastic process are stored in the amplitudes.

Definition 3.2. The analog encoding of a single trajectory (v 1 , v 2 , . . . v T ) of the stochastic process S(T ) is the quantum state,

An -approximate encoding of the trajectory of the stochastic process trajectory is a state such that |ψ v1,v2,..

Here the value of the process is encoded in the amplitude of the quantum state and the ket stores the time. This representation of the stochastic process manifestly takes advantage of the exponential nature of quantum states -as only O(log T ) qubits are required to represent a T -timestep process. It is an analog representation as the values are stored in the amplitude of the state, rather than digitally in the value of the ket.

Preparing the analog encoding of a single trajectory of S(T ) is equivalent to the task of preparing copies of a density matrix ρ = E v1,v2,...v T [|ψ v1,v2,...v T ψ v1,v2,...v T |]. Such a density matrix represents a single trajectory of the stochastic process sampled according to the correct probabilities. However, for quantum Monte Carlo methods to estimate a function of a stochastic process, a stronger notion of coherent analog encodings for S(T ) is required.

Definition 3.3. The coherent analog representation of the stochastic process S(T ) is a superposition analog representation of the corresponding trajectories,

Additionally, there is a garbage register |g that encodes the randomness used to generate the corresponding trajectory. An approximate analog encoding for |S (T ) is a superposition over approximate trajectories √ p v1,v2,...v T |ψ v1,v2,...v T with ψ v1,v2,...v T being approximate trajectories as in definition 3.2.

# Quantum simulation of Brownian Motion

The stochastic Fourier series representation of the Brownian motion (Theorem 2.2) provides a classical algorithm with complexity O(T log T ) for simulating a Brownian path over T steps using the fast Fourier transform. It also suggests a quantum algorithm for generating analog encodings of Brownian trajectories on a quantum computer. The quantum algorithm first prepares the state |W = i∈[L] ai i |i obtained by truncating the Wiener series to a fixed number of terms L using a data loader circuit and then applies the quantum Fourier transform circuit.

The number of terms L required to obtain an approximate representation of the Brownian path are much smaller than the number of time steps, for example taking L = 200 terms in the series leads to an 2 -norm error of 0.3 percent. The quantum simulation algorithms use O(L) gates and have complexity poly-logarithmic in T , and achieve a speedup over the classical simulator in the regime T L, We next describe an optimized algorithm for preparing analog encodings of Brownian motion with circuit depth O(log L) + log(T )), this algorithm will be used as a subroutine for generating the coherent analog encoding for fractional Brownian motions. The quantum algorithm for simulating Brownian paths is presented as Algorithm 4.1. We describe the implementation of the different steps and then establish correctness of the algorithm. reduce the number of qubits to O(log L). Subsequently, pad with 0 qubits so that the total number of qubits is log(T ). 5: The discrete sine transform matrix is the unitary matrix U ∈ R T ×T with U ij = sin(πij/T ). Apply the quantum circuit for U from Corollary A.2 to obtain

An efficient procedure for generating the random Gaussian state required for step 2 of algorithm 4.1 is described in Section 4.1, this procedure uses the data loader circuit but with angles drawn from a certain distribution to ensure that the vector prepared is the random Gaussian state. The discrete sine transform matrix can be implemented as a quantum circuit with depth O(log T ) as shown in appendix A. The total circuit depth for the algorithm is therefore O(log L + log T ), the number of qubits used is O(L + log T ) and the gate complexity is O(L + polylog(T )) as claimed. The correctness of the Algorithm 4.1 is established in Lemma 4.9. The dependence of the 2 approximation error on the number of terms L retained in the Wiener series is examined in Section 4.3.

## Gaussian state preparation

In order to prepare the Gaussian state in step 2 of the algorithm, we need to compute the distribution on the angles for a unary data loader for a uniformly random unit vector in S n according to the Haar measure. Recall that a Haar random unit vector is obtained by choosing i.i.d. N(0,1) Gaussian random variables for the coordinates and rescaling to unit norm. Further, we show that for Haar random vectors, the angle distributions for the different angles in the data loader are independent and that these distributions can be specified exactly in terms of the gamma and beta distributions. We begin by recalling some of the useful properties of the beta and gamma distributions and then establishing the independence of the angle distributions for a uniformly random vector and explicitly computing the angle distributions.

Definition 4.2. The Gamma distribution γ(a) has support R + , it is parametrized by a > 0 and has cumulative distribution function,

x 0 t a-1 e -t dt.

(5) Γ(a) is the Gamma function.

The Beta distribution can be defined in terms of the Gamma distribution, 

A sum of squares of k identically distributed N (0, 1) Gaussian random variables can be expressed in terms of the Gamma distribution.

Proposition 4.4. The sum of squares i X 2 i /2 where X i are k independent Gaussian random variables has distribution γ(k/2). This fundamental fact underlies the computation of the distribution for the data loader angles, a proof is provided in Appendix B for completeness. In addition to the above fact, we require a lemma that computes the distribution of θ if sin 2 (θ) has a β(a, b) distribution. Γ(a+b) sin 2a-1 (t) cos 2b-1 (t).

Proof. As sin 2 (θ) is distributed according to β(a, b), we have that Pr[sin 2 (θ

Substituting x = sin 2 (z) so that dx = 2 sin(z) cos(z)dz, the integral above reduces to,

It follows that the density function for θ is F (t) = Γ(a)Γ(b) Γ(a+b) sin 2a-1 (t) cos 2b-1 (t) as claimed.

Using the above probabilistic facts, we are now ready to compute the distribution of the data loader angles for a vector with coordinates given by i.i.d. Gaussian random variables.

Lemma 4.6. If the vector x ∈ R n stored in the binary data loader is uniformly random, the angle θ at node of height h has probability density function

Proof. The binary data loader for vector x ∈ R n uses a binary heap data structure where each node stores the sum of squares of the values in its subtree and an angle θ. Denoting the value stored at node j by r(j)

and, the angle θ is given by θ = arccos( r(2j) r(j) ) where r(2j) is the sum of squares of the values stored in the left subtree for node j, that is cos 2 (θ) = r(2j) r(j) and sin 2 (θ) = r(2j+1) r(j) . If x ∈ R n is a uniformly random vector then the values at the leaf nodes have distribution X 2 i where X i are independent N (0, 1) random variables. The sum of squares 1 2 i∈[k] X 2 i for a k independent N(0,1) random variables X i has distribution γ(k/2) by Proposition B.3. It follows from the definition of the beta distribution 4.3 that for a node at height h (with the convention that the leaf nodes are at height 1), sin 2 (θ) = r(2j+1) r(j) has distribution β(2 h-2 , 2 h-2 ). Applying Lemma 4.5, the angle θ for a node at height h has probability density function

We computed the distribution of the angles at the nodes for a for a uniformly random vector the angles at the nodes of the binary data loader. The next Lemma shows that these angles are in fact independent for uniformly random vectors. Lemma 4.7. If the vector x ∈ R n stored in the binary data loader is a Haar random unit vector, the angles θ i , θ j stored at different nodes i, j are independent.

Proof. If the nodes i, j are at the same height the angles are independent as they are functions of different i.i.d. Gaussian random variables. Without loss of generality let the h(i) ≤ h(j) where h is the height of the nodes. If j does not lie on the path from the root to i, then the angles at i, j are independent as they are functions of different i.i.d. Gaussian random variables. It therefore suffices to show that for a given node j, the angles in the left sub-tree rooted at j are independent of the angle at j.

The angles for the binary data loader are independent of the x , that is the angles are the same for x and cx for all c ∈ R. The angle at node j is a function ratio of the norms of the left and right subtrees, that is θ = arctan( r 2j+1 /r 2j ). It follows that for i in the left-subtree rooted at j, the density function f (θ i |θ j ) = f (θ i |r 2j ) = f (θ i ) establishing the independence of θ i and θ j .

We are now ready to provide the procedure for generating the random Gaussian state in step 2 of Algorithm 4.1.

Lemma 4.8. The quantum state |R = 1 Z2 i∈[L] a i |i where a i are independent N (0, 1) random variables can be prepared using the binary data loader construction with independent angles θ i at height h distributed according to the density function

Proof. The result follows from the distribution of the angles θ i at height h computed in Lemma 4.6 and the independence of the angles θ i established in Lemma 4.7.

### Correctness of the quantum algorithm

We have described the quantum circuits implementing the steps of Algorithm 4.1, we are now ready to show that the algorithm produces the quantum states corresponding to superpositions over Brownian paths as claimed. Proof. Algorithm 4.1 outputs the quantum state obtained by applying the discrete sine transform to the state 1

where j is the result of the measurement in step 3. The L dimensional vector a = (a 1 , a 2 , • • • , a L ) has i.i.d. coordinates distributed according to N (0, 1). The i.i.d. property is preserved if an arbitrary permutation σ ∈ S L is applied to a.

For all j ∈ [L] the mapping a k → a k⊕j is a permutation as k 1 ⊕ j = k 2 ⊕ j implies that k 1 = k 2 . The vector a j = (a 1⊕j , a 2⊕j , • • • , a L⊕j ) therefore has the same distribution as a for all j. By Wiener's Theorem, it follows that the discrete sine transform applied to 1

## Coherent analog encoding for Brownian motion

The coherent analog encoding for the Brownian motion is a superposition over the analog representation of the corresponding trajectories, along with the garbage register that encodes the randomness used for generating these trajectories,

The algorithm for generating the coherent analog encoding for Brownian motion is a two step procedure, the first step creates the angle distributions in Lemma such that angles from these distributions when used in a unary data loader generate a Haar random unit vector. As the angle distributions are independent, these distributions are created on independent registers using a unary data loader. After the first phase the following quantum state is obtained

The second step uses the angle registers to apply the rotations for a unary data loader in order to create the encoding of a L dimensional uniformly random vector on a second register. More precisely, the angles θ i are stored up to some qubits of precisions and controlled rotations conditioned on these bits are applied to get a uniformly random Gaussian vector on the second register. The algorithm can therefore be viewed as 'data loading the data loader', the first step generates the angle distributions and the second step uses these angles to prepare a Gaussian state on an independent register. In addition, the second step appends an independent register in state

1 k α |k with exponent α depending on the Hurst parameter. The quantum state is obtained after the second step is,

where the normalization factor 1 Z1 ensures that the last two registers are normalized quantum states with unit norm. Using this state in step 3-5 of Algorithm 4.1 generates an -approximate coherent analog encoding for Brownian motion, where depends on the number of terms L retained in the Wiener series. Assuming that the angles distributions for the θ i in step 1 of the algorithm are generated to a fixed K bits of precision, the number of qubits needed is O(2 K L) = O(L) and the asymptotic resource requirements for generating the coherent analog encoding of Brownian motion are the same as the requirements for generating a single trajectory, Theorem 4.10. There is a quantum algorithm for generating -approximate coherent analog encodings of Brownian motion with requires O(L+log T ) qubits, has circuit depth O(log L+log T ) and has gate complexity

The angle distributions for the θ i are heavily concentrated at the higher levels of the tree, this can be used to further reduce the resource requirements for near term instantiations of the coherent analog encoding preparation procedure for Brownian motion. The quantum Monte Carlo method for estimating expectations over Brownian paths using the coherent analog encoding is described in Section 6. We argue that choosing L to be a constant suffices to obtain good approximations of the Brownian path in the 2 norm. The expected 2 norm of the Brownian path E[

## Quantum runtime and error analysis

A more precise tail bound establishing the asymptotic rate of convergence of the ζ(2) series can be obtained as follows. The ζ(2) power series truncated at L terms can be approximated by the integral

when the Wiener series is truncated to L terms is O(1/L) and as the error is a weighted sum of squares of Gaussian random variables B(t)-B L (t) 2 is concentrated around O(1/L) with high probability. Thus L = O(1/ ) terms need to be retained to achieve -approximate analog encodings (Definition 3.2) for Brownian trajectories with high probability. The approximation of Brownian motion by a constant number of terms of the Wiener is illustrated in Figure 2. 

## Fractional Brownian motion

Algorithm 4.1 can be used to prepare quantum representations of Fractional brownian motion (Definition 2.3) with arbitrary Hurst parameter H ∈ [0, 1]. Wiener's Fourier series representation for the Brownian motion can be viewed as arising from the fact that Brownian motion is an integral over white noise where the white noise can be described as a stochastic Fourier series with i.i.d. Gaussian coefficients. Fractional Brownian motion in this view is a 'fractional' integral over the white noise, where the notion of fractional integral corresponds to the Lévy or the Mandelbrot definitions of the fBM given previously.

Fractional integrals can be given different formulations, it suffices to determine the fractional integral of sin(kt) and cos(kt) to define it for functions having a well defined Fourier series. It can be shown that in the Fourier domain, the fractional integral with parameter α corresponds to Hadamard product by k -1-α [Her11]. With the interpretation of fractional Brownian motion as a fractional integral over white noise it follows that the Fourier coefficients of the fractional Brownian motion with Hurst parameter H decay according to the power law with the k-th coefficient scaling as k -H-0.5 . The quantum algorithm for simulating Brownian motion 4.1 can be generalized to simulate fBM for an arbitrary Hurst parameter by changing the scaling of the power law exponent.

The number of terms L retained in the stochastic Fourier expansion for the fBM are given by the number of terms required to approximate the power series ζ(t) for t ∈ [1, 3]. For H = 0, the power series ζ(1) is divergent and thus an arbitrarily large number of terms would be needed, for other values of H the convergence rate is the number of terms needed to approximate the zeta power series. Comparing with the previous calculation for Brownian motion, for H > 1/2 fewer than 200 terms suffice to approximate the fractional Brownian motion up to 99.7% variance while for H < 1/2 the number of terms N required to achieve this accuracy will be larger. The exact number of terms needed can be calculated from the value of ζ(1 + 2H), Similar to the case of Brownian motion, the dependence of the approximation error in the 2 norm can be computed by approximating the tail probability for

). The asymptotic error dependence for fractional Brownian motion with H > 1/2 is better than O(1/ ). For example, only L = O(1/ 1/2H ) terms of the stochastic Fourier series need to be retained to approximate fBM with Hurst parameter H to 2 error of .

The quantum algorithm for simulating fractional Brownian motion with Hurst parameter H is identical to Algorithm 4.1 with the state k∈[L] 1 k H+0.5 |k in step 1 of the algorithm. Analogous to the results for Brownian motion (H = 1/2) in Theorem 4.1, we have the following result on the running time and resource requirements for simulating fractional Brownian motion. ) where H ∈ (0, 1] is the Hurst parameter.

Fractional Brownian motions for varying H parameters simulated using stochastic Fourier series with power law decay are illustrated in Figure 2. Fractional Brownian motion with H < 1/2 is an important process in quantitative finance. In [GJR18], it is determined that via estimation of volatility from high frequency financial data that log-volatility time series behave like a fractional Brownian motion, with Hurst parameter of order 0.1. Modeling volatility this way allows one to reproduce the behavior of the implied volatility surface with high accuracy. This result is robust and has been demonstrated with thousands of assets.

The truncated stochastic Fourier series captures the large scale variations on the Brownian path while filtering out the high frequency components.For most Monte Carlo estimation applications, the finer scale oscillations on the Brownian path can be safely ignored. The method of retaining only the leading coefficients of the Wiener series to get good approximations is an analogous to principal components analysis where only the leading eigenvalues of the covariance matrix are retained. The generalization of this method to arbitrary stochastic processes is formalized as the Karhunen-Loeve Theorem [Hac18] in the stochastic processes literature.

5 Quantum spectral method for stochastic integrals

## Lévy Processes

The most general formulation of the quantum spectral method is applicable to stochastic integrals over Lévy processes. We begin with a definition of Lévy processes and stating some theorems about them. We assume we are given a filtered probability space (Ω, P, F, F t ). An adapted stochastic process X is called a Lévy Process if it satisfies the following criteria:

2. X has stationary increments, i.e. X t -X s has the same distribution as X t-s , 0 ≤ s ≤ t<∞.

3. X is continuous in probability, i.e. lim t→s X t = X s , where the limit is taken in probability.

Theorem 5.1 (Lévy-Khintchine). The following theorem gives the characteristic function of any Lévy process:

Let X be a Lévy process with Lévy measure ν. Then,

where ψ(u) is given by:

It is a consequence of the Lévy-Khintchine Theorem that any Lévy process X can be decomposed in the following manner,

with B being a Brownian motion, Y being a pure-jump martingale with jumps bounded in absolute value by 1, and C t being a compound Poisson process, with jumps greater than absolute value 1. The approach to quantum simulation of Lévy processes is to generate first the Lévy noise and then to apply to it an integration operator, which is then implemented efficiently using the Quantum Fourier transform. The method is probabilistic and analysis requires bounds on the the Fourier spectrum of the Lévy noise, in particular it requires that the ratio of the maximum and the minimum Fourier coefficients is bounded.

Definition 5.2. Given a Lévy process X, we define Lévy white noise, Z, to be its generalized derivative:

Note that by the properties of Lévy processes, Lévy white noise is a zero-mean, stationary process, and Z t ||Z s for s = t.

In order to establish the flatness of the Fourier spectrum of Lévy noises, we use the Wiener-Khintchine Lemma stated below to relate the Fourier coefficients to the auto-correlation function for the process.

Lemma 5.3 (Wiener-Khintchine). Let F (ω) be the Fourier Transform of Z, and G(ω) be the Fourier Transform of its autocorrelation function, R(τ ).

# S(ω) = lim

Proof. We have

Now, we let T → ∞, arriving at

the Fourier transform of R.

The next claim shows that the Fourier transform Claim 5.4. The power spectrum S(ω) for Lévy white noise is flat, that is

Proof. To see this, recall the fact that the power spectrum S of Lévy White noise can be obtained by taking the Fourier transform of its autocorrelation function R:

The autocorrelation function R(τ ) of the process Z is given by

Now, given the properties of Lévy White noise, we have that

where

. Therefore, the power spectrum, S(ω), F[σ 2 δ 0 ], which is just the constant σ 2 , for all ω.

Applying Chebyshev's Inequality, we have the following bound on on the supremum of the Fourier coefficients of Lévy Noise, i.e. Ẑk :

where the constant C is given by

## Analog encodings for Lévy processes and stochastic integrals

We develop a quantum spectral method that can be used to prepare quantum states representing stochastic integrals, the method is applicable to generating analog representations of integrals over Lévy processes. This includes integrals over time or over Brownian paths and Itô processes that are linear combinations of such integrals. The quantum spectral method is obtained by quantizing the classical spectral method for generating trajectories for the fractional Brownian motion [DM03].

The spectral method for stochastic processes is based on the observation that the discrete analog of an integral kernel of the form t 0 K(t -s)f (s)ds corresponds to multiplication of the vector f (x) by a lower triangular Toeplitz matrix in the discrete setting . We recall the definition of Toeplitz matrices and the closely related circulant matrices. Definition 5.5. A Toeplitz matrix T ∈ R n×n is a matrix such that T ij = f (i -j) for some function f : R → R, that is the entries of T are constant along the main diagonals.

The integral t 0 K(t -s)f (s)ds can be approximated by discretizing the vector f (S) into T time steps and then multiplying the vector f (s) by the lower triangular Toeplitz matrix (T K ) ij := K(i -j) if i > j and 0 otherwise. Further, this is also equivalent to discretizing the Kernel into T time steps and then multiplying by the lower triangular Toeplitz matrix (T f ) ij := f (i -j).

In the quantum setting, we will be computing the stochastic integrals t 0 K(t -s)µ(s)ds against a Lévy noise µ(s). This is achieved by multiplying the state corresponding to the amplitude encoding of the discretized kernel against the Toeplitz matrix T µ . , that is |K = 1 K t K(t) |t by the Toeplitz matrix T µ generates the amplitude encoding for the function g(t) = t 0 K(t -s)µ(s)ds. Circulant matrices defined below 5.6 are matrices generated by the cyclic shifts of some vector c. The spectral method for simulating stochastic integrals is based on the observation that Toeplitz matrices can be embedded into circulant matrices and that circulant matrices are diagonalized by the Fourier transform and their eigenvalues can be computed explicitly.

Definition 5.6. A circulant matrix C ∈ R n×n is a matrix such that C ij = f ((i -j) mod n) for some function f : R → R, that is the rows of the matrix C are generated by applying cyclic shifts to its first row.

A Toeplitz matrix T µ of dimension n can be embedded into a circulant matrix C µ of dimension 2n as follows,

where T µ = (T µ R ) T where T µ R is the the reversed Toeplitz matrix with first column given by the reverse µ R of µ. (The reverse x R for x ∈ R n is the vector with entries (x R ) j = x n-j of the first column of T x ).

It is well known that circulant matrices are diagonalized by the Fourier transform, that is a circulant matrix C has a factorization of the form C = U diag( c)U -1 where U is the unitary matrix for the quantum Fourier transform and c = QFT(Ce 1 ) is the Fourier transform of the first column of C. The eigenvalues of the matrix C K are thus determined by taking the Fourier transform of the first column which by construction is the vector (K, 0 T ). 5: Apply the 2T dimensional quantum Fourier transform circuit to obtain an amplitude encoding of t 0 K(s, t)dµ s concatenated with its reversal. 6: Measure the auxiliary qubit added in step 2, if 0 then we have amplitude encoding of t 0 K(s, t)dµ s if 1 then we have the reversed amplitude encoding.

The quantum representation of the stochastic integral t 0 K(t -s)µ(s)ds is obtained by multiplying the initial state |(K(s), 0 T ) by the matrix C µ . Multiplication by the matrix C mu can be in turn implemented using the spectral decomposition C mu = U diag( µ)U -1 , the unitaries U correspond to the quantum Fourier quantum Monte Carlo method is more efficient for low degree functions and for Hurst parameters H > 1/2 for fractional Brownian motion.

A general setting for which quantum Monte Carlo methods are applicable is that in which the function to be estimated can be encoded as an amplitude. That is, there is a circuit for unitary U such that,

the quantum amplitude estimation algorithm can then be used to estimate α to additive error using O(1/ ) queries, and further low depth variants of amplitude estimation can obtain a speedup that is proportional to the depth D to which the quantum circuit for U can be run on the quantum hardware. The quantum Monte Carlo algorithm is given as Algorithm 6.1 where the goal is to estimate either

] or E B H (t) [ f (t)|B(t) ] where the expectation is over fractional Brownian motion trajectories and over trajectories B H (t) of bounded norm in the second case. Estimating

] requires less quantum resources but is likely to have an analytic closed form for simple functions f as this is equivalent to computing the Fourier transform for f and computing an inner product with the Wiener series in the Fourier domain. Estimating E B H (t) [ f (t)|B(t) ] requires an additional norm computation and conditional rotation step in Algorithm 6.1, however the estimate produced does not have a closed form solution as the process in addition post-selects over Brownian paths of a certain norm, thus additional eliminating the additional structure in the Fourier domain arising from the Wiener series expansion. Algorithm 6.1 Quantum Monte Carlo algorithm with coherent analog encodings. Require: Hurst parameter H, number of time steps T and terms L in the Wiener series, a function f :

|t , the f is assumed to be a constant, power law parameter α = H + 0.5, an upper bound B max on the norm of the Brownian paths considered by the algorithm. Ensure: An additive error estimate for the expectation

] where the expectation is over Fractional Brownian motion paths with Hurst parameter H or an estimate for E B H (t) [ f (t)|B H (t) ] where the Fractional Brownian motion paths are have norm at most B max . 1: Prepare independently the angle distributions and the Gaussian states to obtain the quantum state in equation ( 9),

2: Apply CNOT gates to map |k → |k ⊕ i = |j to obtain,

3: Apply step 4 of Algorithm 4.1 so that the last register has log T qubits and apply V -1 (DST ) on the last register containing the Brownian path to obtain the state,

where the normalization factor 1/Z 1 = 1/ B H,j,θ (t) for B H,j,θ (t) = k a 2 k⊕j /k 2α 1/2 has been explicitly included. in an auxiliary register, append an extra qubit, apply a conditional rotation depending on the norm and uncompute the norm to obtain,

5: Perform quantum amplitude estimation (or a low-depth variant of amplitude estimation) to estimate either:

1. The amplitude for |0 log T in equation ( 15) to additive error f in order to estimate

] to additive error .

2. The amplitude for |0 log T +1 in equation ( 16) to to additive error B max f in order to estimate E B H,j,θ (t) [ f (t)|B H,j,θ (t) ] to additive error .

## Proof of correctness

The correctness proof shows that the estimates produced by algorithm 6.1 are close to the true values in additive error. The analysis proceeds by analyzing in turn the errors due to truncation of the Wiener series for L terms, tracing out the auxiliary registers and other sources of error due to finite precision that are poly-logarithmic. 

] is approximated to additive error O( ) for all test functions f (t).

The second claim for the correctness of the quantum Monte Carlo method shows that tracing out the θ and j registers does not affect the expectations. Claim 6.2. Tracing out the θ and j registers does not change the expectation of the quantity being estimated, that is,

Proof. The claim is equivalent to showing that after tracing out the θ and j registers, the states k∈[L] ãk /k α in the last register in equation ( 16) represent uniformly random fractional Brownian paths. As the θ are chosen so tracing out the θ registers ensures that the ãk are i.i.d. Gaussian, it suffices to show that tracing out the j registers, the distribution the ãk remains spherically symmetric,

It follows that the states in the last register in equation ( 16) when θ and j registers are traced out represent random fractional Brownian paths, so the quantity being estimated by the algorithm is

With these auxiliary claims, we can complete the runtime analysis of the quantum Monte Carlo method and resources required for it,

] to additive error using O(L + log T ) qubits,

) gates where G is the number of gates in the circuit V for preparing |f .

Proof. Claim 6.2 shows that that the amplitude being estimated by algorithm 6.1 is

]. There are two further sources of error, the first due to the finite precision for generating the distributions on the angles and the second due to truncation of the Wiener series to L terms, claim 6.1 shows that the truncation error is O( ) for L = O(1/ 1/2H ). Choosing log(1/ ) qubits to encode each angle further ensures that the errors due to the finite precision of the angle registers is O( ). Thus, the estimate obtained in step 5 of the algorithm is an O( ) additive error estimate for

].

The number of qubits used is O(L+log T ) where the O absorbs potential logarithmic factors due to higher precision on the angle registers. The oracle for the amplitude estimation circuit requires (L+polylog(T )+G) gates and the amplitude estimation algorithm needs to simulate the oracle 1/ f times in step 5 of the algorithm to get the desired estimate, and the gate complexity bound follows.

The classical Monte Carlo method for the task requires resources O(T / 2 ) while the quantum Monte Carlo method with using an oracle compiled from classical circuits would require O(T / ). The gate complexity of the quantum Monte Carlo method using the fBM simulator is O(polyLog(T )/ c ). It is incomparable to the black box quantum Monte Carlo method as it achieves an exponential speedup in T , the dependence is worse. It is more efficient than the classical Monte Carlo method in the regime c ∈ [1, 2], that is for estimating function averages over fractional Brownian paths with H > 1/2.

The analysis of the quantum Monte Carlo method covers case 1 where

]. The analysis of the post-selected quantum Monte Carlo method for estimating E B H (t) [ f (t)|B H (t) ] is not carried out explicitly as it depends on the post-selection procedure, however the post-selected variant is expected to be more useful in practice due to the lack of an analytic closed form solution for the quantity being estimated.

## Applications to Monte Carlo methods

In this section, we provide two further examples of applications of the analog encoding of fractional Brownian motion to Monte Carlo methods. The first application is for pricing variance swap options, while the second is for statistical analysis of anomalous diffusion processes. In these end-to-end examples, we harness the O(polylog(T )/ c ) speedup.

### Pricing Variance Swap options

In this section, we consider the problem of pricing a variance swap.

We assume we have a filtered probability space (Ω, F, F, P), where F = (F t ) 0≤t≤T . The filtration F represents the information available at a given time.

We consider a model such that the price S and volatility σ, under a risk neutral measure Q, are given by

and σ t = B H t for a Brownian motion B and an independent Fractional Brownian motion B H with Hurst parameter H.

The log returns, R i , are given by

.

A variance swap is an over-the-counter derivative that allows its holder to speculate on the future volatility of the asset price, without any exposure to the asset itself. In such a swap, one party pays amount that is based on the variance of the asset. The other party pays a fixed amount, i.e. the strike price, which is set so that the present value of the payoff is equal to zero. The realized variance of the asset price over a discretized time interval 0 ≤ t t ≤ t i+1 ≤ T is given by

where A is an annualization factor, and n + 1 is the number of observed prices. The payoff of a variance swap is given

In the above, N var is called the variance notional. If we assume that the volatility follows a Fractional Brownian motion, we can use our analog encoding of Fractional Brownian motion, to compute the strike price,

Let π denote the projective measurement onto time steps t 1 ≤ t ≤ t n = T. The expectation value of π is equal to n i=1 R 2 i . and is thus equal to E Q ][σ 2 realized |F t0 ] up to constant factors. Note that the above quantity can be computed using a quantum Monte Carlo method by modifying Algorithm 6.1 to tag the amplitudes for time steps 1 to T in step 3.

If the average is computed over all possible sample paths of the prices process S, then the realized variance has a closed form solution. Mild post-selection over the paths, for example choosing paths which whose norm is lies in the interval [B min , B max ] suffices to ensure that n i=1 R 2 i does not have a closed form solution. The method described above prices the variance swap option assuming the volatility is an fBM. Pricing an option on realized variance where the log volatility is a fractional Brownian motion would require efficient quantum algorithms for generating analog encodings of geometric Brownian motion and more generally exponentiated fractional Brownian motions. Generating such encodings is an important open question for quantum finance.

### Anomalous Diffusion of Particles

A second example is that of single-particle superdiffusion, an example of anomalous diffusion, in the context of molecular motion. Single-particle tracking is relevant for particles in microscopic systems as well as animal and human motion. Anomalous diffusion is common in (super)crowded fluids, e.g. the cytoplasm of living cells. We next define anomalous diffusion in terms of the mean square averages.

The time-averaged mean-square-deviation (TAMSD) of a particle is a measure of the deviation of the position of a particle with respect to a reference position over time. Let X t denote the position of the single particle at time t with t ∈ [T ]. The TAMSD is then defined as:

The mean-square-displacement (MSD) of a particle with position X t at time t and with PDF of displacement P (t, x) at time t is given by:

x 2 P (t, x)dx For a particle following a fractional Brownian motion trajectory, the mean TAMSD has the following scaling:

where H is the Hurst parameter of the fractional Brownian motion. The constant of proportionality is the diffusion coefficient, D. The TAMSD be used to classify anomalous diffusion behaviour of a single particle.

We write M T (τ, D, H)

to make explicit its dependence on the Hurst parameter H as well as D. We assume that D is known.

Calculating the TAMSD of the particles is telling of their diffusive behaviour; that is, it can distinguish between sub and super-diffusive behaviour. Superdiffusion is salient in the traveling behaviour of humans and spreading of infectious diseases [SBW17]. It corresponds to fBM H> 1 2 , and long-range correlations between displacements and is thus well modeled by Fractional Brownian Motion with H > 1/2. Sikora et. al in [SBW17] proposed a statistical test using the TAMSD to characterize anomalous diffusion. It is known that if the particle trajectory X t follows an fBM, (T -τ )M T is distributed as generalized chisquared, that is, as

where the U j are distributed as i.i.d χ 2 (1) or γ( 12 ). 

In the above, the Q α 2 are quantiles such that P r(Y <Q α 2 )< α 2 and Q 1-α 2 is such that P r(Y >Q 1-α 2 )< α 2 . The null hypothesis H 0 such that X t follows an fBM with given Hurst parameter, H test . The alternative hypothesis, H 1 , is such that the particle trajectory X t is an fBM with a different Hurst parameter, or that the trajectory follows a continuous-time random walk. H 0 is rejected if the test statistic M T (τ ) falls outside of the above confidence interval.

The authors in [SBW17] use Monte Carlo Methods to estimate the power of this statistical test-that is, the probability that it rejects the null hypothesis, given that the alternative hypothesis is true. The power of the test is defined as,

Such a Monte Carlo test hinges on the calculation of the empirical probability that the test statistic M T (τ ) does not lie in the above interval. We can use our analog encoding of Fractional Gaussian noise (using that its spectrum, f (ω), is proportional to ω 1-2H ) with given Hurst parameter H to output the following state:

(B H (j + τ ) -B H (τ )) |j .

(21)

If we assume the alternative distribution of X is a compound poisson process, a special case of a continous time random walk, we can use algorithm 5.1 to obtain as output its amplitude encoding.

Below is quantum Monte Carlo procedure to calculate the power of the statistical test, based on the method in [SBW17]:

1. Calculate the eigenvalues λ j for the Covariance matrix Σ.   5. Estimate the value of the test statistic M T (τ ), using (19) or (21).

6. Set a random counter z to 0. If the test statistic from the last step falls out of the interval (20) computed in step 3, then add 1 to z, else, add nothing to it.

7. Repeat the last 3 steps a total of L times, and the power of the test is given by z L .

Note that we can take a projective measurement, π, onto times t 1 ≤ t ≤ t n = T. The expectation value of π is equal to

that is, the TAMSD. We can then use a simple modification of the Quantum Monte Carlo algorithm in 6.1, to compute the expectation of (19).

Our analog encoding can be used to distinguish between diffusive regimes where both the H test and H under the alternative hypothesis are ≈ 0.4 and above, or if the alternative process is a Compound Poisson process. It is an open problem to use our analog encoding for very small H in order to detect subdiffusive regimes (e.g. as is the case with telomere motion).

Another characterization of of single particle dynamics is its ergodicity, or lack thereof. Ergodicity is characterised by the equivalence of the MSD and the TAMSD in the limit of long trajectory times. That is lim

We define

That is, the mean of the TAMSD over N trajectories of the process. We also define

The ergodocity of a stochastic process is characterized by the Ergodicity-Breaking parameter (EB), defined below:

We can use the algorithm in 6.1 via quantum amplitude estimation to estimate the EB for Levy Processes, as well as fBM for H> 1 2 . One can in turn use these calculations as benchmarks to characterize observed data, for example, via the distibution of ξ, or via large deviation statistics of ξ. (29)

The effect of the controlled swap gates is to move the index that is equal to 1 to the first n/2 qubits of the unary representation. The last n/2 qubits of the unary representation are equal to 0 following this step and are therefore erased at the end of the computation. The multiple controlled swap gates can be applied in parallel on n/2 qubits, this can be accomplished using the available O(n) ancilla qubits to copy the parity bits.

Following these computations, we have computed 1 bit of the binary representation and are left with a unary encoding of size n/2. Continuing iteratively, we obatin unary to binary conversion circuit with total depth 1≤i<(k-1) (k -i) = O(k 2 ) = O(log 2 n) is obtained. The number of gates needed for computing each bit of the binary representation is O(n), as there are O(log n) bits in the binary representation the total gate complexity is O(n log n). The maximum number of ancilla qubits O(n) are needed for computing the first bit of the binary representation, subsequent bits require fewer qubits. The claims on the resource requirements for the unary to binary conversion circuit follow.

# Acknowledgments

We thank Iordanis Kerenidis for helpful discussions and an anonymous referee for detailed feedback on the manuscript. Adam Bouland's contribution to this publication was as a paid consultant and was not part of his Stanford University duties or responsibilities.

# N

) controlled on qubit k transforms this state to j (U N/2 x e ) j |j, 0 + ω j N (U N/2 x o ) j |j, 1 . From equation ( 22) it follows that the application of H k transforms it to j (U N x) j |j, 0 + (U N x) j+N/2 |j, 1 . The permutation σ is a cyclic shift that moves the k-th qubit to the first position, this can be implemented by swapping the wires in the circuit. The final state is j (U N x) j |0, j + (U N x) j+N/2 |1, j which is the quantum Fourier transform of x.

As the phase gates can be applied in parallel by making O(log k) copies of the control qubits, the depth of the QFT circuit requires 2k qubits and has depth is O(k log k).

The discrete cosine and sine transforms are defined as DCT (x) =

x. The QFT circuit can be used to implement the DCT and DST with the same complexity.

Corollary A.2. The unitaries for the discrete cosine transform and the discrete sine transform can both be implemented as quantum circuits with 2k + 1 qubits and depth O(k log k).

Proof. The conjugate of the Fourier transform U N/2 can be applied by conjugating all the controlled phase gates in the QFT circuit. Starting with the state |0 |U N/2 x +|1 |U N/2 x and applying the iH gate the states corresponding to DCT (x) and DST (x) are each obtained with probability 1/2. As the success probability is known exactly, the probabilistic procedure can be made to succeed with probability 1 using the exact amplitude amplification [BHMT02].

# B The sum of squares of k Gaussian random variables

The distribution of the the sum of squares of Gaussian random variables can be expressed in terms of the Gamma function.

Lemma B.1. The random variable X 2 /2 where X ∼ N (0, 1) has distribution γ(1/2).

Proof. Let G(x) be the cumulative distribution function for X 2 /2 where X ∼ N (0, 1), then,

Making the substitution so that t 2 /2 = y and tdt = dy

Thus G(x) is identical to the cdf for the Gamma distribution with a = 1/2.

The sum of squares i X 2 i /2 where X i are k independent Gaussian random variables has distribution γ(k/2). This distribution is more commonly named as the χ 2 distribution with k degrees of freedom. This follows from the next lemma on the additivity of the gamma distribution under convolution.

Proof. The density function F for Y 1 + Y 2 is the convolution of the density functions for Y 1 and Y 2 , that is,

Introducing variable z = t/y so that ydz = dt,

The final step follows from the definition of the β(a, b) probability density function Γ(a)Γ(b) Γ(a+b) x a-1 (1 -x) b-1 . We showed that the density function for Y 1 + Y 2 is identical to the density function for γ(a + b).

The proposition below is an immediate consequence of Lemmas B.2 and B.1.

Proposition B.3. The sum of squares i X 2 i /2 where X i are k independent Gaussian random variables has distribution γ(k/2).

# C The unary to binary conversion circuit

We provide a logarithmic depth circuit that converts the unary amplitude encoding |x = i∈[n] x i |e i for a unit vector x ∈ R n , x = 1 to the binary encoding |x = i∈[n] x i |i . The unary encoding requires n qubits while the binary encoding uses only log n qubits, the convertor circuit operates on n + log n qubits. The action of the unary to binary convertor circuit on the n + log n qubits is given as,

The next proposition shows that the unary to binary conversion circuit can in fact be implemented with logarithmic depth.

Proposition C.1. The unary to binary conversion circuit in equation (28) can be implemented by a quantum circuit with depth O(log 2 n) and with O(n log n) gates and with O(n) ancilla qubits.

Proof. Without loss of generality, let n = 2 k be a power of 2. Given the unary encoding i∈[n] x i |e i , the first bit of the binary encoding is given by the parity of the last n/2 qubits of the unary representation. The parity of n/2 = 2 k-1 qubits can be computed by a circuit with n CNOT gates and with depth 2(k -1) using O(n) ancilla qubits. The ancilla qubits store the partial parities and are erased at the end of the computation.

Following the computation of the parity, apply controlled swap gates on qubits (i, i + n/2) for the unary representation with the parity qubit acting as control. Recall the two qubit swap gate has the following

