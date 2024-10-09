# Introduction

When will quantum computers solve valuable problems that are out of reach for state-of-theart classical approaches? To understand this future moment of quantum advantage, we must identify what computational problems are most apt and determine what quantum algorithms will be able solve them in the nearest time frame. Despite some recent challenges being illuminated [1], estimating the ground state energy of quantum systems [2] remains one of the leading contenders for the first realization of practial quantum advantage. Solving this problem efficiently with a quantum computer would be of high value to areas including combustion [3], batteries [4,5], and catalysts [6]. Considering that the progress in quantum hardware has consistently improved, we are urged to investigate: what are the minimal quantum resources needed to realize quantum advantage with ground state energy estimation (GSEE)?

# Previous methods for ground state energy estimation

To estimate ground state energy on early quantum computers, researchers have designed more efficient algorithms using fewer qubits, gates, and ancillas. Most of these algorithms are based on the variational quantum eigensolver (VQE) [7]. These algorithms do not have performance guarantees and recent works have identified roadblocks for the practicality of such approaches through the measurement problem [3,8] and issues with optimization [9,10]. Yet, quantum algorithms with performance guarantees [2,11,12,13] demand unfortunately-large quantum resources, requiring hundreds of logical qubits and over billions of operations per circuit (e.g. greater than 10 10 T gates [4]). The error correction overhead needed to run such quantum circuits is far beyond what can be realized on today's hardware. Towards realizing practical quantum advantage sooner, we develop quantum algorithms in the goldilocks regime of having provable performance guarantees while also exponentially reducing the required number of operations.

The operations involved in many GSEE algorithms, including ours, are controlled time evolution operations, c-exp (iHt). For the algorithms considered, the total number of operations per circuit and the circuit depth are proportional (ignoring logarithmic factors) to the evolution time t. We will refer to this measure as the circuit depth. The circuit depth required by a GSEE algorithm is typically costed in terms of ϵ, the target accuracy of the ground state energy estimate, and η, a lower bound on the overlap of the input state ρ with the ground state 1 . In contrast to previous GSEE methods, the costs of our GSEE algorithms will depend on ∆, a lower bound on the energy gap (i.e. the difference between the smallest and next-smallest eigenvalue of H), typically governs the performance of ground state preparation methods [13]. With these parameters established we are able to describe the costs of previous methods for GSEE that aim to minimize the quantum resources. Recently, building upon the ideas of [14], Lin and Tong [12] designed a quantum algorithm for ground state energy estimation with circuit depths scaling as Õ(1/ϵ), which requires just a single ancilla qubit and involves no costly circuit operations beyond controlled time evolutions. This algorithm requires running the circuits of depth Õ(ϵ -1 ) multiple times, leading to a total runtime of Õ(ϵ -1 η -2 ). Later, Dong et al. [13] improved on this result, developing an algorithm with similar characteristics, yet achieving a runtime of Õ(ϵ -1 η -1 ). Both of these methods achieve the so-called Heisenberg-limited scaling in the runtime with respect to ϵ. Meanwhile, Wan et al. [15] combined the ideas in [12] with the principles of randomized Hamiltonian evolution (QDRIFT) [16] to propose a ground state energy estimation algorithm which trades off between number of non-Clifford gates and runtime. Ding and Lin [17] and Ni et al. [18] also discovered low-depth algorithms for phase estimation which achieve the Heisenberg-limited scaling of quantum runtime while having a diminishing prefactor for the maximum circuit depth when the initial state approaches the target eigenstate. There has also been progress in developing low-cost (or low-depth) quantum algorithms for simultaneous estimation of multiple eigenvalues in the past years [21,14,22,19,20]. Our work is mostly influenced by [14,12] which promoted the idea of using quantum circuits to general time signals and utilizing the tools from classical signal processing to analyze them. This time series analysis reveals the target property of the spectrum of the Hamiltonian.

All of the GSEE methods prior to ours employ quantum circuits whose depth scales inversely with ϵ the target accuracy 2 . In the early fault-tolerant setting, this circuit depth requirement may place a limit on the size of problem instances that such methods can accommodate. It is reasonable to assume that early fault-tolerant quantum computers will be limited in number of physical qubits. Larger problem instances require more logical qubits to be encoded in these physical qubits. This entails an increase in the error rate for logical operations (as the code distance has been reduced). This increase in error rate compromises the number of operations that can be implemented per circuit (assuming a fixed circuit error tolerance of the algorithm). To "unlock" larger instances requires running a GSEE algorithm that can succeed with fewer operations per circuit (or less circuit depth). Motivated by these considerations, the question addressed by this work is: is it possible to unlock larger problem instances for early fault-tolerant quantum computers through an exponential improvement in the accuracy-dependence scaling of circuit depth in ground state energy estimation?

# Summary of main results

We develop and analyze low-depth ground state energy estimation (GSEE) algorithms with high accuracy for which the circuit depth scales exponentially better than Õ(1/ϵ). As is typical, the circuit depth and quantum runtime of the algorithm is measured in terms of the number of controlled evolution operations c-exp (-2πiH) referred to as Hamiltonian evolution time.

# Theorem 1.1 (Low-depth GSEE, informal version of Theorem C.1).

Let H be a Hamiltonian with spectral gap at least ∆. Suppose we can prepare an initial state ρ such that the overlap with the ground state satisfies ⟨E 0 |ρ|E 0 ⟩ ≥ η. Given ∆, η, and sufficiently small ϵ, there exists an algorithm to estimate the ground state energy within accuracy ϵ with high probability such that:

• The circuit depth, measured in maximal Hamiltonian evolution time, is

(1)

• The quantum runtime, measured in total Hamiltonian evolution time, is

Cor 1.2 Thm 1.1 [12,15] [13] [13] Figure 1: This figure shows the landscape of early fault-tolerant GSEE algorithms plotted according to their runtime and circuit depth measured in terms of total evolution time (T tot ) and maximal evolution time (T max ), respectively. The green region indicates the new low-depth regime introduced in this work. The orange dot corresponds to the ∆ -1 -depth GSEE algorithm (Theorem 1.1) when ∆ = ∆ -1 true , and the curve shows the smooth trade off between T max and T tot described in Corollary 1.2. We also remark that the right-most dot which shows an algorithm in [13] requires multiple ancilla qubits and multi-qubit controlled operations, whereas the algorithms in this work and [12,15] only use a single ancilla qubit. For simplicity, we have ignored all the poly-logarithmic factors.

# Molecule

Gap Gap Lower Bound Gate Reduction [4] [4]. For these molecules in the cc-pVDZ basis, we can estimate the energy gaps using EOM-CCSD calculations with ORCA software [23,24]. The target accuracy considered in [4] was ϵ = 1 mHa. The standard approach to quantum phase estimation (ignoring the cost due to imperfect ground state preparation) uses a circuit with 2/ϵ applications of c-exp (2πiH) to achieve an ϵ accurate estimate with high probability. We include the various logarithmic factors (c.f. Algorithm 2) and set an input state overlap value of η = 1/1000, which is conservative (i.e. lower) relative to the values found in [25]. In the last column we give cost reductions relative to recent methods [12], which use 2/πϵ applications of c-exp (2πiH).

Using the costs established in Theorem 1.1, Table 1 provides resource estimates that show the reduction in gates per circuit for molecules of industrial interest. The reduction in gates per circuit affords a reduction in the fault-tolerant overhead required to implement ground state energy estimation. These reductions may help to bring such problem instances within reach of earlier fault-tolerant quantum architectures, potentially realizing quantum advantage sooner.

For some molecules, it might be the case that the runtime of this low depth algorithm is too high to outperform state-of-the-art classical methods for solving the same problem. Our second main result (c.f. Corollary C.2) is that we can trade circuit depth for total runtime reduction. This gives a means of speeding up the overall algorithm.

Corollary 1.2. Let H be a Hamiltonian with spectral gap ∆ true . Suppose we can prepare an initial state ρ such that the overlap with the ground state satisfies ⟨E 0 |ρ|E 0 ⟩ ≥ η. Then for arbitrary α ∈ [0, 1], given ∆ true , η and sufficiently small ϵ, there exists an algorithm to estimate the ground state energy within accuracy ϵ with high probability such that:

• The circuit depth, measured in maximal Hamiltonian evolution time, is

(3)

• The quantum runtime, measured in total Hamiltonian evolution time, is

Through the era of early fault-tolerant quantum computing, as quantum architectures are able to realize deeper quantum circuits, the trade-off in Corollary 1.2 may lead to a crossover point into quantum advantage.

# Low-depth ground state energy estimation

Before introducing the method, we define the ground state energy estimation problem. Suppose we are given a classical description of a quantum Hamiltonian H. This Hamiltonian has (unknown) spectral decomposition

are the eigenvalues of H, and the |E j ⟩'s are orthonormal eigenstates of H. Let ρ be an easy-to-prepare state (of the same dimension as H). Let p j := ⟨E j | ρ |E j ⟩ be the overlap between ρ and |E j ⟩, for 0 ≤ j ≤ N -1. We assume that two numbers η ∈ (0, 1) and ∆ > 0 are given such that p 0 = ⟨E 0 | ρ |E 0 ⟩ ≥ η and E 1 -E 0 ≥ ∆. Our goal is to estimate E 0 with accuracy ϵ and confidence 1 -δ, i.e. to output a sample from a random variable Ê0 such that the failure probability satisfies

for given small ϵ > 0 and δ ∈ (0, 1). Furthermore, we want to achieve this by using limiteddepth quantum circuits and classical post-processing of the quantum measurement outcome data.

Our algorithm does not require the Hamiltonian H to be normalized to work, i.e. it does not rely on an assumption like ∥H∥ ≤ 1. The circuit depth and quantum runtime of our  [12] (blue curve) and the method developed here (green curve). The blue curve is an example estimate of the approximate cumulative distribution function (see Eq. ( 16) in [12]), while the green curve is an example estimate of Eq. (15) as output from Step 3b in the algorithm below. The LT22 method uses a Heaviside convolution, while our method uses a Gaussian derivative convolution. Their method requires a steep jump in the convolution function, which necessitates Õ(1/ϵ)-depth circuits. Our method only requires that the contribution of the excited state energies to the convolution function does not interfere too much with that of the ground state energy. This affords the use of a less-steep convolution function, which only requires Õ(1/∆)-depth circuits. The trade-off is that our method requires more samples, leading to an increased total runtime. algorithm will be measured in the maximal and total evolution time of H, respectively. Note that the gate complexity of simulating e iHt is proportional to ∥H∥ t. Therefore, rescaling H, ∆ and ϵ by the same constant simultaneously does not change the number of elementary gates in our algorithm (see Theorem C.1).

# Time signals from Hadamard tests.

In our GSEE algorithm, the role of the quantum computer is simply to provide statistical estimates of tr ρe -iHτ . The quantum circuit we use to generate these estimates is known as a Hadamard test and is shown in Figure 3. Labeling this outcome b ∈ {+1, -1}, the average value of b output by the Hadamard test circuit is

when W = I and it is equal to the imaginary part when W = S † where S is the phase gate.

It is helpful to view the quantity tr ρe -iHτ as a complex-valued time signal, with τ being the time. This time signal encodes information about the eigenvalues of H and the density operator ρ. In particular, if we can determine how this signal depends on the ground state energy E 0 , then we might be able to estimate E 0 from the time signal. Although we are unable to exactly determine the time signal, we can estimate the real and imaginary parts of the signal at any time τ to within any desired accuracy using sufficiently many Hadamard test measurement outcomes as described above. The time cost of each Hadamard test is proportional to τ and the total time cost will depend on how many Hadamard tests, or samples, we take over the different chosen times τ .

Filtering the spectrum Here we introduce the method for estimating and processing the signals from the Hadamard test data. The Fourier transform (or frequency signal) of the ideal time signal tr ρe -iHτ is equal to the so-called spectral measure of H associated with the initial state ρ and is given by

Although p(x) itself cannot be determined exactly from Hadamard test data, we explain how to accurately estimate any convolution of p(x) with a filter function f (x). For our purposes, the filter function is used as a tool for organizing the time signal data from a limited time window into useful information about the spectrum of H. We briefly explain how to evaluate (or, rather, estimate) the complex number (f * p)(x) for any given value x using low-depth Hadamard test circuits.

Three key features make low-depth convolution estimation possible. First, the convolution can be expressed as a linear combination of p(t) = tr ρe -2πiHt ,

where f (t) denotes the Fourier transform of f (x). Second, these traces can be estimated from the Hadamard test data as shown in Eq. 6. Third, the circuit depth of each Hadamard test is proportional to t. We can limit the circuit depth used in the algorithm and still obtain an accurate estimate of the convolution by judiciously truncating the integral approximation

As explained in detail in Algorithm 1, the strategy we use to estimate (f * p)(x) uses a so-called multi-level Monte Carlo approach. An unbiased estimate of (f * p)(x) is constructed by first (classically) sampling a time t in [-T, T ] drawn from a distribution proportional to | fT (t)|.

Conditioned on this outcome t, a sample is then drawn from each of the real (W = I) and the imaginary (W = S † ) part Hadamard tests with time t, returning X and Y , respectively. From these outcome data (t, X, Y ), we construct a random variable whose average value is equal to

where e i2πϕ(t) = fT (t)/| fT (t)|. It is important to note that the samples can be generated ahead of time; the choice of where to evaluate (f * p)(x) can be made after this data is gathered.

# Designing the filters

The filter function plays two roles in determining the algorithm performance. First, the shape of the filter determines how easily the ground state energy can be determined from (f * p)(x). Second, the smoothness of the filter determines the severity of the truncation T that can be withstood, and therefore the minimal viable circuit depth. This second role is what affords the exponential reduction in circuit depth of our method.

Estimating the ground state energy from the convolution can be understood through an example. In [12] they choose f (x) to be a periodic Heaviside function 3 . As shown in Figure 2, this particular choice of convolution results in a series of steps, the first of which is located at the ground state energy E 0 . Their algorithm proceeds by using a binary search to locate this first step. The drawback of this approach is that in order to resolve this first step to accuracy ϵ, the truncation order must be Õ(1/ϵ). This means that the circuit depth of the Hadamard test scales as Õ(1/ϵ). We design a filter function and energy estimation strategy that requires a time window that scales as O(log (1/ϵ)). This corresponds to an exponential improvement in the circuit depth dependence on the accuracy.

The key observation for the design of low-depth filter functions is as follows. If a filter function satisfies the following properties, then it can isolate the minimum eigenvalue from the others well and the corresponding convolution can be evaluated easily:

1. The filter function f (x) has an exponentially-decaying tail, i.e., |f (x)| = exp (-Ω(|x|))

for sufficiently large x. This ensures that (f * p)(x) ≈ p 0 f (x -E 0 ) for x near E 0 (i.e. the interference from the excited states is negligible) and hence we can easily infer E 0 from the shape of f * p in this region.

2. The filter function's Fourier transform f (t) also has an exponentially-decaying tail, i.e., | f (t)| = exp (-Ω(|t|)) for sufficiently large t. This allows f to be well-approximated by a band-limited function, which means that the maximal evolution time in the Hadamard tests will be small.

Based on this observation, a natural choice is the Gaussian filter, defined as:

where σ > 0 is a parameter to be chosen later. Note that its Fourier transform is another Gaussian kernel (up to some scaling factor):

Thus, most of its mass is concentrated within |t| = O(σ -1 ). More importantly, by convolving f σ with the spectral measure p, we get:

which is a mixture of Gaussians. Since the Gaussian filter has an exponentially-decaying tail, if we zoom-in to a neighborhood of E 0 , the convolution value is dominated by the first Gaussian kernel p 0 f σ (x -E 0 ). Therefore, the first significant peak of f σ * p will be close to E 0 and GSEE is then reduced to a peak finding problem. Our approach to this problem is to first obtain some

] by using a previous algorithm [12]. Then we partition the interval [ Ẽ0 -O(σ), Ẽ0 + O(σ)] into a O(ϵ)-width grid, and estimate the convolution f σ * p at each grid point. Finally, we output the position of the grid point with maximum convolution value. The complexity of this algorithm depends on σ, the width of the Gaussian filter, since we can only truncate its spectrum to [-T, T ] for T = Θ(1/σ) in order to evaluate the convolution with enough precision. For sufficiently small ϵ > 0, one can take σ = O(∆/polylog(∆ϵ -1 η -1 )) such that the algorithm outputs an estimate of E 0 within ϵ-additive error. It implies that the maximal Hamiltonian evolution time of our algorithm is Õ(1/∆).

In Appendix B.1, we develop a method for evaluating the convolution of the spectral measure and any filter with bounded band-limit. We prove that if f T is a function such that fT has support in [-T, T ], then one can use the measurement outcomes of Õ(ϵ -2 1 ∥ fT ∥ 2 1 ) Hadamard tests to estimate (f T * p)(x) within accuracy ϵ 1 > 0 (for any given x), where ∥ fT ∥ 1 is the L 1 norm of fT .

We now apply this result to bound the total evolution time of our algorithm with the Gaussian filter. As we will see, its performance will be sub-optimal, so we will only analyze a more refined version with better performance in detail. For the truncated Gaussian filter

), and we need to evaluate the convolution within accuracy ϵ 1 = Õ(ηϵ 2 σ -3 ) 4 . Thus, by our choice of σ = Õ(∆), the sample complexity is 4 To see this, note that the Taylor expansion for the Gaussian density around 0 up to second order yields

This implies that the difference between the values of (fσ * p)(x) ≈ p0fσ(x -E0) for x = E0 and x = E0 + ϵ can be as small as O(ηϵ 2 σ -3 ).

The bottleneck of our total evolution time is the normalized convolution evaluation accuracy ϵ 1 /∥ fT ∥ 1 which scales as O(ηϵ 2 σ -2 ) for the Gaussian filter f σ . To improve this factor, we switch to the Gaussian derivative filter g σ which is defined as follows:

Since the Gaussian derivative filter has an exponentially-decaying tail, (g σ * p)(x) resembles p 0 g σ (x -E 0 ) in a neighborhood of E 0 . In particular, the unique zero point of g σ * p in this region is close to E 0 . The Gaussian derivative filter allows for a more favorable normalized convolution evaluation accuracy. On the one hand, the difference between the values of |(g σ * p)(x)| for x that is ϵ/2-close to E 0 and for x that is ϵ-far from E 0 is Ω(ηϵσ -3 ) (see Lemma A.2). So it suffices to pick ϵ 1 = O(ηϵσ -3 ). On the other hand, it is easy to show that ∥ĝ σ,T ∥ 1 = Θ(σ -2 ). This implies that the required normalized convolution evaluation accuracy for g σ is ϵ 1 /∥ĝ σ,T ∥ 1 = O(ηϵσ -1 ). Moreover, our GSEE and convolution evaluation approaches are general so that they can be easily adapted to the Gaussian derivative filter function with almost the same parameters (i.e., σ = Õ(∆) and T = Õ(1/σ)). Therefore, using g σ in our algorithm, the maximal evolution time remains to be T max = Õ(∆ -1 ) and the total evolution time is reduced to

Ground state energy estimation algorithm Using the Gaussian derivative filter, we describe the algorithm for ground state energy estimation that proves Theorem 1.1. This is the first GSEE algorithm that uses Õ(∆ -1 )-depth quantum circuits to achieve accuracy ϵ. A detailed presentation of the algorithm can be found in Algorithm 2. This algorithm makes use of the data structure for convolution evaluation in Algorithm 1.

The inputs to Algorithm 2 include the Hamiltonian H and initial state ρ, a lower bound ∆ on the spectral gap E 1 -E 0 of H, a lower bound η on the overlap between ρ and the ground state |E 0 ⟩ of H (i.e. η ≤ ⟨E 0 | ρ |E 0 ⟩), the target accuracy ϵ and confidence 1 -δ. The output of the algorithm is an estimate of the ground state energy E 0 of H. The steps of the algorithm are as follows:

1. Roughly locate E 0 : Run the algorithm of [12] to obtain an estimate Ẽ0 of E 0 such that 

# C(H, ρ, t, W )

▷ Run the circuit in Figure 3 with τ = 2πt and W = I or S † 10:

FilterSampler FS ▷ Filter function's sampler 12: end members 13: 14: procedure Init(H, ρ, f T , ϵ, δ, M ) ▷ ϵ is the target accuracy, δ is the tolerable failure probability, M is the maximal number of points at which the convolution is evaluated 15:

FS.Init(f T )

16:  for i ← 1, 2, . . . , S do 19:

x (i) ← C(H, ρ, t (i) , I) ▷ Hadamard test 21:

end for 24: end procedure 

28:

return Z 29: end procedure 30: end data structure 4. Estimate zero-crossing: Among the M convolution estimates, find the estimate closest to zero and report the corresponding energy as the ground state energy estimate.

To realize the results in Corollary 1.2, we choose ∆ between ∆ true and 1/ϵ. Furthermore, we can easily parallelize our algorithm to reduce the runtime in the regime where ∆ ≫ ϵ. Indeed, as we do a Monte Carlo evaluation of the convolution, we can use several quantum computers in parallel to generate samples and reduce the runtime of the computation. In contrast, in the regime ∆ ≃ ϵ it is unclear how to speed up the computation by resorting to parallel quantum computers, as we essentially sample from the distribution a constant number of times. Thus, as the total number of gates required to implement the algorithm in the ∆ ≫ ϵ regime is smaller than the usual QPE, we envision that it will be possible to run the algorithm reliably in error-corrected devices with a smaller code distance, which Algorithm 2 Low-depth ground state energy estimation algorithm.

, 0.2∆

# 3:

Run the algorithm in [12] on H and ρ to obtain an estimate Ẽ0 of E 0 such that Ẽ0 is σ/4-close to E 0 with probability at least 1 -δ/2 4:

6:

▷ Filter band-limit (Lemma A.4)

ConvEval.Init(H, ρ, g σ,T , ε/2, δ/2, M ) ▷ Algorithm 1

8:

for j = 1, 2, . . . , M do 9:

x j ← E 0 -0.25σ + (0.5σ/M ) • (j -1)

10:

end for 12:

j * ← arg min 1≤j≤M |h j |.

13: return x j * 14: end procedure translates to a smaller number of physical qubits. And by running the algorithm on various smaller quantum processors in parallel, it will be possible to offset some of the additional cost incurred by the quadratically worse dependency on the precision. By combining these two observations, we believe that it will be possible to obtain quantum advantage earlier with the approach advocated by this paper when compared to traditional QPE.

One may wonder if Algorithm 2 still works if ∆ is larger than the spectral gap E 1 -E 0 . Unfortunately, this is not always the case. To see this, recall that we infer E 0 from the shape of the convolution of the spectral measure p and a Gaussian derivative filter g σ . We need the filter g σ to be narrow enough so that (p * g σ )(x) ≈ p 0 g σ (x -E 0 ) in a neighborhood of E 0 . Then the unique zero point of p * g σ in this region is close to E 0 . If ∆ > E 1 -E 0 , then since σ = Õ(∆), the filter g σ could be too wide for our purpose, and the functions p 0 g σ (x -E 0 ) and p 1 g σ (x -E 1 ) might have significant overlap. Consequently, we can no longer guarantee that (p * g σ )(x) ≈ p 0 g σ (x -E 0 ) for x near E 0 . In other words, p * g σ might have a different shape from g σ in the neighborhood of E 0 . Thus, the current strategy will not work in general. In practice, it may be difficult to decide whether a given ∆ is smaller or larger than E 1 -E 0 , and this could pose a problem for the application of Algorithm 2. In a recent work [34], we proposed a method to certify the correctness of the outputs of GSEE algorithms (without assuming ∆ ≤ E 1 -E 0 ) to mitigate this problem. We leave it as future work to fully resolve this issue. in establishing upper bounds over a range of circuit depths, an important future direction is to establish lower bounds on depth-limited ground state energy estimation. This would deepen our understanding of the capabilities and constraints of using depth-limited quantum computers for simulating quantum systems. To this end, one might draw inspiration from Section 2.2 of [22] which derives Cramer-Rao lower bounds on the scaling of the error versus the total quantum cost for estimating a single eigenvalue phase given an eigenstate input. It might be possible to generalize the result to the case where the input state is just close to an eigenstate and a spectral gap of the Hamiltonian is promised.

Our work helps to establish the paradigm of developing quantum algorithms using the tools of classical signal processing [12,26,27]. In this approach, the quantum computer produces stochastic signals that encode characteristics of a matrix. This stochastic signal can be processed to learn the matrix properties of interest. The signal processing paradigm is well-suited to developing algorithms for early fault-tolerant quantum computers. Quantum computations with such architectures will be error prone, generating noisy signals. The tools of classical signal processing have been designed to handle such noisy signals and can aid in the design and analysis of robust quantum algorithms [28,29,30].

One requirement of the algorithm is that a lower bound on the energy gap must be specified. There exist quantum chemistry methods for estimating the gap (e.g. using the ORCA software [23,24] as we did for our numerical comparisons). However, such estimates can become inaccurate for large systems. It may be helpful to incorporate a step into the quantum algorithm that estimates this gap. Although this estimation is computationally hard in general [31], many physical systems of interest have structure that make the estimation feasible.

In this work, we did not consider the impact of implementation error on the performance of the algorithm. We expect that our algorithm is able to tolerate some degree of variation between the ideal Hadamard tests and the implemented Hadamard tests. Building off of recent work [30], we believe the algorithm can be operated so as to accommodate such deviations. We leave for future work the investigation of robust quantum algorithms for ground state energy estimation.

The methods introduced here may help to bring the target of useful quantum computing closer to the present. Yet, there is still much work needed to carry out detailed resource estimations that predict the onset of quantum advantage using methods such as those we have introduced. More broadly, our hope is that this work contributes to the general understanding of how to use quantum computers given practical constraints on their capabilities and might inspire the development of quantum algorithms in other application domains.

One may have noticed that GSEE can be also solved by preparing a high-fidelity approximation of the ground state and estimating its energy with respect to the Hamiltonian somehow. However, it is unclear whether such methods can have the same circuit depth and quantum runtime as ours. Specifically, our method requires only Õ(∆ 2 /ϵ 2 ) quantum circuits where each circuit evolves H for Õ(1/∆) time (ignoring η-dependence). Note that ∆ ≤ E 1 -E 0 is always no larger than ∥H∥. We will consider two state-preparation-based strategies below, and both of them require Ω(∥H∥ 2 /ϵ 2 ) copies of the state to reach accuracy ϵ, which is more costly than our method, especially when ∥H∥ ≫ ∆. In both strategies, let |ψ⟩ be the output of a ground state preparation algorithm. We leave it as an open question to find a state-preparation-based strategy with Õ(∆ 2 /ϵ 2 ) sample complexity.

In this work, we have focused on estimating a single eigenvalue of the Hamiltonian H. But it is likely that our method can be extended to estimate multiple eigenvalues of H simultaneously, under appropriate assumptions about the gaps among the eigenvalues and the overlaps between an input state and the eigenstates. The reason is as follows. One can use the data from the Hadamard tests to construct the convolution of the spectral measure and a Gaussian filter, and under proper conditions, the peaks of this convolution will be close to the eigenvalues of H. Then our problem is reduced to finding the peaks of this function. Furthermore, perhaps we can replace the Gaussian filter by a Gaussian derivative filter to gain better efficiency, as in GSEE. In that case, one would need to search for the zero points of the convolution instead of its peaks. We leave it as future work to fully develop this algorithm for simultaneous estimation of multiple eigenvalues of a given Hamiltonian.

[34] Guoming Wang, Daniel Stilck França, Gumaro Rendon, and Peter D. Johnson. Faster ground state energy estimation on early fault-tolerant quantum computers via rejection sampling. arXiv preprint arXiv:2304.09827, 2023.

# A Estimating ground state energy via Gaussian derivative filtering

In this appendix, we propose a strategy for GSEE based on Gaussian derivative filtering. In Appendix A.1, we define the Gaussian derivative function and prove a nice property of the convolution between this filter and the spectral measure p. In Appendix A.2, we show how this property leads to a strategy for GSEE. In Appendix A.3, we prove that the Gaussian derivative function can be approximated by a band-limited function, which is crucial for efficient evaluation of the convolution.

# A.1 Convolving the spectral measure with a Gaussian derivative filter

Let us start by defining the Gaussian derivative function and demonstrating its properties.

Specifically, let σ > 0 be arbitrary, and let

Now consider the derivative of f σ , i.e.,

Then the Fourier transform of g σ is

The following properties of g σ and ĝσ will be useful:

Fact A.1 (Properties of the Gaussian derivative function).

1. g σ (0) = 0.

# |g σ (x)| is even, increases monotonically in (-∞, -σ] ∪ [0, σ], and decreases monotonically in

3. g σ (x) decays exponentially to 0 as x → ±∞.

4. ĝσ (ξ) decays exponentially to 0 as ξ → ±∞. Now let us consider the convolution between the filter g σ and the spectral measure p:

It turns out that if σ is appropriately chosen, then |(g σ * p)(x)| is small only if x is close to E 0 , assuming x is at most O(σ)-away from E 0 :

Lemma A.2. Let c = 2 ln (10/9) ≈ 0.45904, and let ∆ and η be as in the problem formulation in the main text. Suppose ϵ > 0 is small enough such that ϵ ≤ c•min

, 0.2∆ .

Then for

we have

Proof. Note that our choice of σ and the condition on ϵ imply that ϵ ≤ cσ < 0.5σ. As a consequence, we do have E 0 -0.5σ < E 0 -ϵ and E 0 + ϵ < E 0 + 0.5σ. Thus, the interval in the second bullet is well-defined. Moreover, we have

in Eq. ( 16))

where the last step follows from p 0 ≥ η. We prove the first and the second parts of the lemma below.

Part I. For any x ∈ [E 0 -0.5ϵ, E 0 + 0.5ϵ], we have

(by Eq. ( 15))

The first term in Eq. ( 18) can be bounded as follows:

(by Eq. ( 13))

To upper bound the second term in Eq. ( 18), first note that for each j ≥ 1,

where the last step follows from the property σ ≤ 0.2∆ in Eq. ( 16). Then we obtain

(by Eq. ( 20) and Property 2 in Fact A.1)

where the second step follows from Eq. ( 17). Combining Eqs. ( 18), (19), and ( 21), we get that for x ∈ [E 0 -0.5ϵ, E 0 + 0.5ϵ],

Part II. For any

(by Eq. ( 15))

The first term in Eq. ( 23) can be lower bounded as follows:

(by Eq. ( 13))

(by the assumption ϵ ≤ cσ)

where the last step follows from c = 2 ln (10/9). To upper bound the second term in Eq. ( 23), note that for each j ≥ 1,

where the last two inequalities follow from the property σ ≤ 0.2∆ in Eq. ( 16). Then we obtain

(by Eq. ( 25) and Property 2 in Fact A.1)

where the last step follows from Eq. ( 17). Combining Eqs. ( 23), (24), and ( 26), we get that for

The lemma is thus proved.

A. 

Let M := ⌈σ/ϵ⌉ + 1, and let x j := Ẽ0 -0.25σ + (0.5σ/M ) • (j -1) for j ∈ [M ]. Suppose h 1 , h 2 , . . . , h M are random variables such that

Let j * = arg min 1≤j≤M |h j |. Then we have

Proof. By our assumptions about Ẽ0 and h 1 , h 2 , . . . , h M and the union bound, we get that the following events happen simultaneously with probability at least 1 -δ:

In this case, we have

Meanwhile, note that x 1 ≤ E 0 ≤ x M , and |x j+1 -

It remains to show how to generate the random variables Ẽ0 and h 1 , h 2 , . . . , h M that satisfy the conditions Eqs. ( 28) and (29) respectively. To obtain Ẽ0 , we use the GSEE algorithm in [12] which takes Õ(ϵ -1 ) maximal Hamiltonian evolution time to achieve ϵ-accuracy. Since Ẽ0 only needs σ 4 -accuracy, this step has Õ(σ -1 ) maximal evolution time. To obtain h 1 , h 2 , . . . , h M , we first introduce the band-limited version of g σ , denoted as g σ,T , in Appendix A.3, and prove that (g σ * p)(x) ≈ (g σ,T * p)(x) for a small T . Then we design a data structure ConvEval in Appendix B such that this data structure can evaluate g σ,T * p at the points x 1 , x 2 , . . . , x M with high accuracy and confidence after appropriate initialization.

# A.3 Gaussian derivative filters with bounded band-limits

In order to efficiently evaluate g σ * p at any given point, we truncate the spectrum of g σ and construct a T -bandlimit version g σ,T such that

Specifically, we define g σ,T by restricting ĝσ to [-T, T ] and performing the inverse Fourier transform:

Clearly, g σ,T → g σ as T → ∞. The following lemma shows how to choose T such that g σ,T can approximate g σ in L ∞ -norm:

Lemma A.4. Let ϵ 1 > 0 be arbitrary. Then for

we have

Proof. By the Fourier inversion theorem, we have

By solving the inequality

we get that it suffices to take

The following claim shows that the L ∞ -approximation for g σ implies the L ∞ -approximation for g σ * p. Claim A.5. Let T be defined as in Lemma A. 4. Then we have

Proof. For any x ∈ R, we have

where the first step follows from the definition of convolution, the second step follows from the triangle inequality, the third step follows from Lemma A.4, and the last step follows from the property of Dirac delta function.

Claim A.5 implies that in order to estimate (g σ * p)(x) within ϵ 1 -accuracy, it suffices to evaluate (g σ,T * p)(x) within 0.5ϵ 1 -accuracy, which can be achieved by the method in Appendix B.

# B Complexity of evaluating the convolution

In this appendix, we focus on evaluating the convolution between a filter function f and the spectral measure p to within ϵ-additive error. In Appendix B.1, we develop an evaluation method for general filter functions with bounded band-limits. Then in Appendix B.2, we apply the method to the Gaussian derivative filter used in our GSEE algorithm.

# B.1 Evaluating the convolution via Hadamard tests

For the sake of generality, we will not restrict to a specific filter f but consider arbitrary filters with bounded band-limits. Specifically, for a parameter T > 0, let f T be a function with band-limit T , i.e.,

where fT is the Fourier transform of f T and satisfies fT (t) = 0 for all t ∈ (-∞, -T )∪(T, +∞). Furthermore, we require that fT is either continuous in [-T, T ] or a weighted sum of Dirac delta functions (i.e., f T has a discrete spectrum). Here we will state the results for the former case, and the reader can easily generalize them to the latter case. Given such a function f T , we can define a probability density ν in terms of its Fourier weights:

Moreover, let ϕ(t) be the phase of fT (t), i.e., fT (t) = | fT (t)|e i2πϕ(t) . Then we have that

Now given a quantum state ρ, a Hamiltonian H and a parameter t ∈ [-T, T ], we define two random variables X t and Y t as follows. Let b I and b S † be the measurement outcome of the circuit in Figure 3 with τ = 2πt and W = I or S † (where S is the phase gate), respectively. Then we define X t = (-1) b I and Y t = (-1) b S † . As mentioned in the main text, we have that

Now given a point x ∈ R, we define the random variable Z(x) as follows. Let t be a random variable with probability density function ν. Then we define

It turns out that Z(x) is an unbiased estimator of the convolution f T * p at point x:

Lemma B.1. For the random variable Z(x) defined as Eq. (45), we have that

Proof. Let us first consider the conditional expectation E[Z(x)|t = t] for some t ∈ [-T, T ]. By Eq. ( 44) and the definition of Z(x) in Eq. ( 45), we get

By the law of total expectation, we have

where the last step follows from the definition of ν in Eq. ( 42) and the definition of ϕ(t).

It remains to prove that the above expression indeed coincides with f T * p(x). Indeed, we have that:

By the definition of p(x) in Eq. ( 7), we have that

where the last step follows from the integration of Dirac delta function. Then, it implies that

where the last step follows from tr ρe -2πiHt = k≥0 p k e -2πitE k . Comparing Eqs. ( 48) and ( 51), we conclude that E [Z(x)] = (f T * p)(x) for all x ∈ R. The lemma is thus proved.

With Lemma B.1 established, it is now straightforward to analyze how many samples we need to estimate the function f T * p at various points within a target accuracy. Lemma B.2 (Sample complexity of the convolution evaluation). Let {(t (i) , X (i) , Y (i) )} S i=1 be S i.i.d. samples such that t (i) ∼ ν, X (i) ∼ X t i and Y (i) ∼ Y t i , where ν is defined as Eq. (42), and X t and Y t are the measurement outcome of the circuit in Figure 3 with τ = 2πt and We have given a data structure ConvEval in Algorithm 1 for evaluating the convolution f T * p at multiple points. Lemma B.2 immediately implies that: Corollary B.4. Let x 1 , x 2 , . . . , x M ∈ R be arbitrary. Suppose the data structure Con-vEval is initialized with parameters (f T , ϵ, δ, M ). Let h j be the output of the procedure ConvEval.Eval(x j ) for j ∈ [M ]. Then we have . Since the filter function f T has spectrum bounded in [-T, T ], the maximal evolution time is 2πT and the total evolution time is at most 4πST .

The ConvEval.Eval procedure then uses the S samples to compute the estimate of (f T * p)(x). Moreover, the computation is classical and elementary.

# B.2 Application to Gaussian derivative filters

In this appendix, we apply the data structure ConvEval to the band-limited Gaussain derivative filter g σ,T :

To apply Lemma B.2, we first bound the L 1 -norm of its spectrum.

Claim B.6. Let g σ,T be defined as Eq. (62). Then we have ∥ĝ σ,T ∥ 1 ≤ 4 πσ 2 . Proof. By the fact that ĝσ,T (ξ) = ĝσ (ξ)1 |ξ|≤T and direct calculation, we obtain

Then we get the following corollary on the sample complexity of evaluating g σ,T * p on M points.

Corollary B.7. Let ϵ 1 > 0, δ 1 ∈ (0, 1) and x 1 , x 2 , . . . , x M ∈ R be arbitrary. Suppose the data structure ConvEval is initialized with parameters (g σ,T , ϵ 1 , δ 1 , M ). Let h j be the output of the procedure ConvEval.Eval(x j ) for j ∈ [M ]. Then we have 

# C Main Theorem

In this appendix, we describe our main results about ground state energy estimation. Recall that we have presented a Õ(∆ -1 )-depth algorithm for GSEE in Algorithm 2.

# Theorem C.1 (Ground state energy estimation). Let

are the eigenvalues of H, and the |E j ⟩'s are orthonormal eigenstates of H. Suppose we are given access to the Hamiltonian evolution e iHt for any t ∈ R. Let ∆ > 0 be given such that ∆ ≤ E 1 -E 0 . Moreover, suppose we can prepare a state ρ such that ⟨E 0 | ρ |E 0 ⟩ ≥ η for known η > 0.

Let ϵ > 0 be small enough such that it satisfies the condition in Lemma A.2, and let δ ∈ (0, 1) be arbitrary. Then the output of Algorithm 2 (i.e. GSEE(H, ρ, ϵ, δ, ∆, η)) is ϵ-close to E 0 with probability at least 1 -δ. Furthermore, in this algorithm,

• The maximal Hamiltonian evolution time is Õ(∆ -1 );

• The total Hamiltonian evolution time is Õ(η -2 ϵ -2 ∆);

• The classical running time is Õ(η -2 ϵ -3 ∆ 3 ).

Proof. We first prove the correctness of Algorithm 2. By construction, Ẽ0 satisfies Eq. ( 28) in Lemma A.3. Meanwhile, by Claim A.5 and the choice of T in Algorithm 2, we have

Meanwhile, since ConvEval is initialized with parameters (H, ρ, g σ,T , ε/2, δ/2, M ) in Algorithm 2, by Corollary B.7, we get

Then it follows from Eqs. (65) and (66) and the triangle inequality that

which coincides with Eq. ( 29) in Lemma A.3, given the choice of ε in Algorithm 2. Now with both of its conditions met, Lemma A.3 implies that the output of Algorithm 2, i.e., x j * , is ϵ-close to E 0 with probability at least 1 -δ, as desired. Next, we analyze the cost of Algorithm 2. In Line 3 of the algorithm, we run the algorithm in [12] to obtain Ẽ0 . Since σ = Ω(∆), this step has maximal evolution time Õ(∆ -1 ), total evolution time Õ(∆ -1 η -2 ), and classical post-processing time Õ(∆ -1 η -2 ).

Then, in Line 7 of Algorithm 2, we run ConvEval.Init(H, ρ, g σ,T , ε/2, δ/2, M ) to initialize the data structure ConvEval in Algorithm 1. We choose the parameters as follows:

Thus, by Corollary B.7, we have

The for-loop in Procedure ConvEval.Init of Algorithm 1 draws S samples from the Hadamard test circuit. The sampling process has the maximal evolution time 2πT = Õ(∆ -1 ) and total evolution time at most O(T S) = Õ(ϵ -2 η -2 ∆). Next, in Line 8 of Algorithm 2, we call the procedure ConvEval.Eval M times to evaluate the convolutions at

Combining these steps together, we get that the whole GSEE algorithm takes:

• maximal evolution time Õ(∆ -1 ),

• total evolution time Õ(∆ -1 η -2 + ϵ -2 η -2 ∆) = Õ(ϵ -2 η -2 ∆), and

• classical post-processing time Õ(ϵ -3 η -2 ∆ 3 ), as claimed.

As described in the introduction, it is favorable to be able to reduce the maximal evolution time (or circuit depth) per circuit run at the cost of a larger total evolution time. If we accept that the maximal evolution time is a proxy for the number of gates required to implement a time evolution on a fault-tolerant device, a smaller maximal evolution time implies a smaller number of gates, which in turn means that the circuit can be run reliably with a higher noise rate per gate. Thus, running the circuit with a smaller code distance is possible, which translates to a smaller number of physical qubits, bringing this application closer to reality. However, note that, for the scope of this paper, we do not envision running this algorithm on NISQ devices, as we do not analyze the effect of noise on its performance.

This allows one to make the most use of the available circuit depth afforded by the quantum architecture. Such a feature is desirable in the era of early fault-tolerant quantum computing where there is likely to be a limit to the available coherence of the device [33]. Fortunately, this feature follows directly from the above theorem and we present it as a corollary below. Note that in Theorem C.1, ∆ is merely a lower bound on the true spectral gap ∆ true := E 1 -E 0 of Hamiltonian H, not necessarily ∆ true itself. In fact, ∆ can range from Õ(ϵ) (in order to satisfy the condition in Lemma A.2) to ∆ true . By setting ∆ = Õ(ϵ α ∆ 1-α true ) with α ∈ [0, 1], we obtain:

are the eigenvalues of H, and the |E j ⟩'s are orthonormal eigenstates of H. Let ∆ true = E 1 -E 0 be the spectral gap of H. Suppose we are given access to the Hamiltonian evolution e iHt for any t ∈ R. Moreover, suppose we can prepare a state ρ such that ⟨E 0 | ρ |E 0 ⟩ ≥ η for known η > 0.

Then for any α ∈ [0, 1], for sufficiently small ϵ > 0 and any δ ∈ (0, 1), there exists an algorithm that estimates E 0 within accuracy ϵ with probability at least 1 -δ such that:

• The maximal Hamiltonian evolution time is Õ(ϵ -α ∆ -1+α true );

• The total Hamiltonian evolution time is Õ(η -2 ϵ -2+α ∆ 1-α true );

• The classical running time is Õ(η -2 ϵ -3+α ∆ 3-α true ).

In particular, setting α = 0 or 1 leads to:

• ∆ = ∆ true , for which Theorem C.1 yields an algorithm with maximal evolution time Õ(∆ -1 true ) and total evolution time Õ(η -2 ϵ -2 ∆ true ); or

• ∆ = Õ(ϵ), for which Theorem C.1 yields an algorithm with maximal evolution time Õ(ϵ -1 ) and total evolution time Õ(η -2 ϵ -1 ) (i.e., the Heisenberg limit).

For general ∆ = Õ(ϵ α ∆ 1-α true ) with α ∈ [0, 1], Theorem C.1 yields an algorithm with maximal evolution time Õ(ϵ -α ∆ -1+α true ) and total evolution time Õ(η -2 ϵ -2+α ∆ 1-α true ). In other words, tuning ∆ between the two extremes gives a trade-off between the circuit depth and total runtime of the algorithm.

# D Comparison to the approach of Lin et al

The main advantage of our approach compared to [12] is in the minimal evolution time required to achieve a desired precision. Indeed, in their approach the evolution time scales inverse linearly with the desired precision. For our approach, the minimal evolution time is dictated by the reciprocal of the energy gap of the Hamiltonian and any additional precision we wish to attain only causes a poly-logarithmic factor in the evolution time. Of course, this comes at the expense of a higher sample complexity at smaller evolution times. This trade-off between the evolution time and the sample complexity is discussed in Corollary C.2.

Note that this improvement in the minimal evolution time comes from two conceptual differences in our approach compared to [12]: the choice of the filter function (Heaviside versus Gaussian derivative) and how we then infer the value of the ground state energy from the convolution (jump versus 0 of derivative).

Both our approach and that of [12] require a truncated approximation of the underlying filter function to implement the algorithm with only finite-time evolutions. However, as the Heaviside function has a jump at 0, the degree of the Fourier series necessarily has to increase the better we want the approximation outside a small neighborhood of 0 to be. For instance, in [12] they find an approximation F d,ϵ such that for d = O(ϵ -1 log ϵ -1 δ -1 ) and This scales logarithmically with the precision with which we approximate the Heaviside function outside of the intervals [-π + ϵ, -ϵ] ∪ [ϵ, π -ϵ] and inverse-polynomially in size of the interval around 0, (-ϵ, ϵ), where we are not guaranteed that the two functions are close. The approach of [12] consists of finding the smallest point x such that (p * F d,ϵ )(x) ≥ η. If we were convolving with the Heaviside function, this would correspond to the ground state energy. But we will now argue that the neighborhood around 0 for which we have the approximation can shift where the jump occurs. Indeed, note that for x ∈ [E 0 -ϵ, E 0 + ϵ] and ϵ ≤ ∆ we have that: (70)

However, as we only have the promise that -δ 2 ≤ F d,ϵ (x) ≤ 1 + δ for points in [-ϵ, ϵ], we will not be able to infer the precise point of the jump at a precision larger than O(ϵ) with this approach. This is because the residual integral term (i.e. the one over (-ϵ, ϵ) in Eq. (70)) will cause fluctuations in this interval and we will not be able to pin down the jump.

On the other hand, by choosing our filter to be Gaussian derivatives, we are able to obtain a good approximation everywhere on the real line. Furthermore, by choosing the zeros of the derivative as criteria, we only need to make sure that the standard deviation is small enough to separate different eigenvalues. This way we obtain a smaller maximal evolution time.

