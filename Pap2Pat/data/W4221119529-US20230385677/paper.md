# Introduction

Amplitude estimation [1] is a powerful algorithm that can achieve a quadratic quantum speedup over classical Monte Carlo (MC) methods [2]. It has a wide range of applications, e.g. in quantum chemistry [3,4], machine learning [5][6][7], and finance [8][9][10] where it can help with tasks such as risk analysis [11,12] and the pricing of financial derivatives [13,14].

The original amplitude estimation procedure [1] has hardware requirements that are challenging for current quantum devices and, therefore, reducing these requirements is currently an active area of research. Crucial breakthroughs were obtained in recent proposals which succeeded in replacing the hardwareintensive components of traditional amplitude estimation -controlled multi-qubit gates and quantum Fourier transform -by classical post-processing [15][16][17][18]. Alternatively, one can systematically reduce the circuit depth by interpolating between classical MC methods and amplitude estimation [19]. Additionally, classical pre-processing can replace costly quantum arithmetic [20] and Bayesian inference can be used to boost the algorithmic efficiency in the presence of device errors [21,22].

In this article, we address the question whether the quantum computational requirements for amplitude estimation can be further decreased by making use of Kirill Plekhanov: kirill.plekhanov@cambridgequantum.com Figure 1: Amplitude estimation error δθ as a function of the computational cost, i.e. the number of queries Nq. We compare adaptive VQAE (symbols with lines guide to the eye) to MLAE (dashed orange) and classical MC sampling (dotted blue). We calculate the rescaled mean value of a shifted Cauchy-Lorentz (red circles), Gaussian (green triangles), and log-normal (purple squares) probability distribution. In VQAE, the first 10 amplitude estimates are computed via MLAE, then one step of the variational optimization is performed, which is followed by the next iteration of 10 MLAE steps. This procedure of variational approximation followed by MLAE is repeated three more times, resulting in a final error δθ ≈ 6 • 10 -5 . We see that, for this error, Nq is up to an order of magnitude smaller in VQAE than in classical MC sampling. Throughout this calculation, VQAE's circuit depth is the depth of the initial state plus at most 10 times the depth of the query operator, whereas MLAE's circuits have the depth of the initial state plus, at the end, 50 times the depth of the query operator.

variational quantum algorithms [23][24][25]. We present variational quantum amplitude estimation (VQAE) in which the depth of the entire quantum circuit is always kept below a desired maximum value by means of variational optimization. VQAE is based on maximum likelihood amplitude estimation (MLAE) [15]. We present a naïve and an adaptive VQAE algorithm. Adaptive VQAE rescales the amplitude to reduce the cost of the variational optimization. The advantage of VQAE over MLAE is that the maximum circuit depth of VQAE is independent of the total number of MLAE steps, whereas in MLAE this depth grows linearly with the number of MLAE steps. The advantage of VQAE over classical MC sampling is that VQAE can have a lower computational cost. Figure 1 shows that, for the problems considered here, VQAE outperforms classical MC sampling and additionally keeps the overall circuit depth below a fixed value.

This article is organized as follows. Firstly, in Section 2, we define the problems considered here and explain the original quantum algorithm for amplitude estimation as well as the classical MC approach. Then, in Section 3 we present our variational methods, study variational errors of constant-depth quantum circuits, and develop naïve and adaptive VQAE. We conclude this article and discuss potential next steps in Section 4.

# Background

In this section, we first define the problem that we are interested in. Next, we explain quantum amplitude estimation and classical MC sampling.

## Problem definition

Throughout this article, we focus on the calculation of expectation values

where the sum runs over 2 n equidistant values of x ∈ [0, 1), p(x) represents a probability distribution and f (x) a real-valued function. Here n is the qubit count of the wave function that encodes p(x) and f (x) in its amplitudes. We consider three probability distributions: a Gaussian

and log-normal distribution

The normalization constants N G , N C-L and N l-n are chosen so that x p(x) = 1.

We choose the following parameters for our analysis. We fix the total number of qubits encoding f (x) and p(x) to n = 5. In our calculations with the Gaussian and Cauchy-Lorentz distribution, we use µ = 0.5 and σ = 0.1. In our calculations with the log-normal distribution, we use c 0 = 0, c 1 = 10, µ = 1.5, and σ = 0.2. For the function f (x), we use

with some C > 0. For this choice of parameters, the expectation value (1) is approximately E p [f ] ≈ 0.5 C for all distributions.

## Quantum amplitude estimation

Let us present a way to encode the solution to (1) on a quantum computer. We assume f (x) and p(x) are functions that map [0, 1) to [0, 1]. We consider real numbers x ∈ [0, 1) that satisfy

and that we identify with n-bit strings {x i , i = 1, 2, . . . , n}. Each bit string shall correspond to a quantum state |x = |x 1 , x 2 , . . . , x n in the computational basis of a n-qubit register. Additionally we have a quantum circuit A that acts on a register of n + 1 qubits and produces a state |χ 0 n+1 = A |0 n+1 such that

Here |ψ bad n and |ψ good n are two normalized quantum states of a n-qubit register which is connected to one additional ancilla qubit. We define the good state

so that a = E p [f ] of Eq. (1) coincides with the probability of measuring the ancilla qubit in the state |1 .

To determine a, the amplitude estimation algorithm uses the Grover operator Q = -R χ R good [1,26,27] where

are reflections in a two-dimensional subspace H χ spanned by states |ψ bad n |0 and |ψ good n |1 . We define a = sin 2 (θ) and explicitly write out the action of Q:

Therefore, the subspace H χ is stable under the action of Q and the only effect of Q is to rotate by an angle of 2θ. The original amplitude estimation algorithm then uses quantum phase estimation to find the eigenvalues of Q equal to exp(±2iθ) and provides an estimate of a with an error

with a probability of at least 8/π 2 [1] where N q (2N q ) is the total number of times the operator A (Q) has to be applied.

Traditional amplitude estimation has high requirements on quantum hardware because it uses quantum phase estimation. This algorithm needs the quantum Fourier transform and multiple controlled Q m operations where {m = 1, 2, 4, . . . , 2 M }. The depth of the corresponding quantum circuit is mostly determined by the depth of the last controlled Q m operator for which m = 2 M . In general, the total circuit depth scales like the total number of queries O(N q ) ∼ O(1/ ) inversely proportional to the desired error .

To avoid these deep quantum circuits, several recent articles propose new ways to carry out amplitude estimation circumventing quantum phase estimation [15,17,18] and circuits of depth O(1/ ) [19]. One proposal is MLAE [15] in which one combines measurements of the states |χ m n+1 with a maximum likelihood estimation of a. For an exponential schedule {m = 1, 2, 4, . . . , 2 M }, this algorithm has the query cost N q ∼ O(1/ ). A linear schedule {m = 1, 2, 3, . . . , M } increases the query cost to N q ∼ O( -4/3 ). Note that in this case N q scales quadratically with the maximum circuit depth M . Following the same idea of reducing the hardware requirements, the authors of Ref. [19] present two algorithms with computational cost N q ∼ O(1/ β+1 ) for quantum circuits of reduced depth O(1/ 1-β ). These algorithms are controlled by an external parameter β which allows one to interpolate between the quantum regime at β = 0 and the classical MC regime at β = 1.

## Classical MC sampling

We perform classical MC sampling in the following way. We sample from the state |χ 0 n+1 of Eq. (7) and measure the ancilla qubit. We compute a as the relative frequency of measuring the ancilla qubit in the state |1 . This calculation of a has the error = a(1 -a)/N q so that the total number of queries required for a certain error is N q ∼ O(1/ 2 ) [28].

Comparing this query cost with the previous ones, we find that traditional amplitude estimation as well as MLAE with exponential schedule achieve a quadratic quantum speedup over classical MC sampling. Both MLAE with linear schedule and the algorithms in [19] obtain a reduced quantum speedup.

Note that, throughout this article, the query complexity is defined in terms of A operators, with two applications of A required per application of Q, see Eq. (9). Also, the depth of quantum circuits is measured in units of A, so that the depth of |χ 0 n+1 is equal to one and the depth of Q is equal to two. Additionally, in the following we assume that A and Q are given, i.e. we do not address questions e.g. relating to their efficient quantum circuit respresentation.

# Variational algorithms

Here we present our variational algorithms. We first explain the general VQAE formalism, then our naïve implementation, and finally the adaptive VQAE approach.

## General formalism

The VQAE algorithm is based on the maximum likelihood framework of Ref. [15] with linearly incremental sequence {m = 1, 2, 3, . . . , M }. In this framework, the depth of the quantum circuit implementing the state |χ m n+1 = Q m |χ 0 n+1 scales with m as 2m + 1.

To prevent the circuit depth from increasing indefinitely, we add to this framework a variational step during which states |χ m n+1 are periodically approximated by a variational quantum state of depth one. We note that this strategy will not always work and the corresponding approximation can have a large error. The variational approach, however, allows us to compute the approximation error so that we can identify when the strategy works. We perform the variational approximation every k-th power of Q, with 0 < k < M . For all the other iterations, we simply apply the corresponding power of Q to the variational state. This results in Algorithm 1.

# Algorithm 1 Variational quantum amplitude estimation

Require: functions f and p, integer k -Use f and p to encode |φ i=0 n+1 = |χ 0 n+1 and Q = -R χ R good according to Eqs. ( 7) and ( 9)

-Save the number of times the ancilla qubit is |1 in a variable h m end sampling variational approximation if j = k -1 then -Perform the variational approximation

end if end variational approximation end for -Use {h m } to carry out the maximum likelihood estimation Here • denotes the floor function and % the modulo operation. The resulting approximation of |χ m n+1 corresponds to the state Q j |φ i n+1 with i = m/k and j = m%k. The depth of this approximation reaches the minimum of one when j = 0 and the maximum of 2k -1 when j = k -1.

The maximum likelihood post-processing [15] consists in maximizing the likelihood function 

# L({h

so that the estimate of the phase θ becomes

Our implementations of the maximum likelihood estimation use h = 2 × 10 3 samples. The minimization of L({h m }, x) is accomplished by means of a brute-force search algorithm that uses 5 × 10 3 grid points. We variationally approximate states 2 which is equivalent to maximizing the objective function (14) with respect to the variational parameters λ. The optimal solution can be formally written as

We notice that the depth of the quantum circuit required to compute F(λ) is the largest circuit depth used by the algorithm. This quantum circuit is composed of the parts encoding |φ var (λ) n+1 and |φ i n+1 , each having depth one, and an operator Q k of depth 2k, resulting in a total depth of 2k +2. In general, the variational quantum state |φ var (λ) n+1 is a parameterized quantum circuit (PQC)

where G j are Hermitian operators acting on the (n + 1)-qubit register and |φ init n+1 is some initial state.

For our purposes, we are interested in hardwareefficient quantum circuits that produce real-valued quantum states. We use the PQC shown in Fig. 2 that is composed of d layers with 15 parameterized single-qubit rotation gates and 10 CNOT gates per layer.

One single variational update of a PQC consists of n s sweeps over all circuit parameters, during which all parameters are updated simultaneously. To perform the optimization, it is convenient to introduce a coordinate-wise version of Eq. ( 14) for the j-th parameter

The optimization of the parameterized state in Eq. ( 16) can then be performed via a particle swarm approach [29,30], the coordinate-wise update [31][32][33][34][35], or gradient based methods with the parameter-shift rule [36][37][38][39][40][41] 

We obtained the best results using the gradient based approach with the Adam optimizer [42]. Therefore this technique is being used throughout this article for the computation of all results. Each gradient calculation requires two evaluations of the coordinatewise objective function f j (λ j ± π/4). On a quantum computer, f j can be determined via the Hadamard test [43]. In our numerical simulations, we emulate the measurement of the Hadamard circuit by first evaluating the exact value of f j and then sampling it using a binomial distribution with the probability (1 + f j )/2 and n f independent Bernoulli trials [28].

The variational approximation step significantly affects the total number of queries N q used by VQAE. In MLAE with a linearly incremental sequence, the total number of queries is equal to

where 2m + 1 is the depth of the quantum circuit encoding |χ m n+1 = Q m |χ 0 n+1 . In VQAE, the total number of queries is composed of two separate contributions. The first one accounts for the sampling of the quantum circuits Q j |φ i n+1 and we denote it by N samp . The corresponding section in Algorithm 1 is labelled by "sampling". The second contribution corresponds to the variational approximation cost, which we denote by N var . It is associated with the section in Algorithm 1 labelled by "variational approximation". We assume that the number of queries required per variational approximation is independent of the iteration number m and changes only as a function of the desired variational error as well as the depth of the circuit for the objective function. We denote the cost of a single variational update as N var/1 (2k + 2), where (2k + 2) is the depth of the objective function F(λ) and N var/1 is the number of quantum circuits per variational update that need to be run by the algorithm. As a result, the total number of variational queries becomes

where M/k is the total number of variational updates required to approximate Q M . The number of sampling queries is equal to

where the last term accounts for the situation when k is not a divisor of M . In the limit M k, N var ∼ O(M ) and N samp ∼ O(kM ). Note that both contributions scale like O(M ) which is quadratically better than the scaling O(M 2 ) of MLAE in Eq. (19).

## Naïve VQAE

In our naïve implementation of the VQAE algorithm, the initial state of the PQC in Eq. ( 16) and Fig. 2 is

Let us first explore the expressive power of the corresponding variational state |φ var (λ) . To this end, we perform amplitude amplifications followed by variational approximations of the resulting state with k = 1 and M = 50. To evaluate the quality of the variational approximation, we calculate the infidelity (22) where for k = 1 we have j = 0 and i = m. Figure 3(a) shows the results of such calculations performed for different depths d of the PQC for m = 10 and Fig. 3(b) shows the infidelity as a function of m for d = 4. We observe that the accuracy of the variational ansatz increases with the depth and saturates at d ≈ 4. The infidelity increases linearly with m. This behaviour is seen for all probability distributions considered.

Next, we present the amplitude estimation results of naïve VQAE. Figure 4 shows the convergence of δθ as a function of N q , under the assumption that N var/1 = 0 and k = 1. The resulting error is compared with the one of classical MC sampling which scales like δθ ∼ O(N -1/2 q ) and the one of MLAE which scales like δθ ∼ O(N -3/4 q

). Interestingly, we find that the convergence of δθ changes as a function of M . For small values of M , it follows the ideal VQAE scaling δθ ∼ O(N -3/2 q ) as if the variational approximation is performed without error. We emphasize that this scaling is cubically better than the one of classical MC sampling. The second convergence regime is observed for larger values of M . In this regime, the error follows the MC scaling with δθ ∼ O(N -1/2 q ). To understand this behaviour, we first notice that the MLAE error decreases with M , while the variational error increases instead. In the regime when the MLAE error is larger than the variational error, the scaling of δθ is the best achievable MLAE scaling δθ ∼ O(N

When the MLAE error is smaller than the variational error, the convergence of δθ is dominated by the latter. The accumulation of the variational error can be modelled via a random process, in which each variational approximation results in a random error of zero mean and some variance σ 2 . After M steps of the algorithm, M/k = M (as k = 1 here) variational approximations were performed resulting in a final error of variance M σ 2 . Hence, an ideal MLAE estimation of the angle θ will produce a relative error √ M σ/[(2M + 1)θ] scaling as O(M -1/2 ). In our simulations, we find that the transition from the first regime -where δθ ∼ O(N -3/2 q ) -to the second regime -where δθ ∼ O(M -1/2 ) -occurs at M ∼ 20.

Finally, we take into account the cost of the variational approximation, to obtain a more complete assessment of the algorithmic performance of naïve VQAE. To estimate the cost of a single variational update, we write down the number of circuits needed to be run for each variational update as N var/1 = 2n f n s n p where n p is the number of parameters of a PQC, n s is the total number of sweeps through all the parameters of the PQC, and n f is the number of Bernoulli trials per evaluation of the objective function. The factor 2 comes from the fact that two evaluations of the objective function are required for each evaluation of the gradient in Eq. (18). For the PQC in Fig. 2 with d = 4, the number of parameters is n p = 60. Additionally, we choose n f ∼ n s ∼ 100 so that N var/1 ∼ 1.2 × 10 6 and N var ∼ 4.8 × 10 6 M . This large variational cost is the dominant part in the calculation of the total number of queries N q . Ultimately, it leads to a performance of naïve VQAE that is worse than the one of classical MC sampling. Reducing any of n f , n s , or n p decreases the variational cost but also increases the variational error which then leads to a worse final amplitude estimation error. We see that the infidelity decreases with increasing d, due to the corresponding increase of the expressive power of the PQC. The infidelity increases linearly as a function of m slowly with a slope of ≈ 0.00017 that is approximately the same for the three distributions. These results are obtained via naïve VQAE with k = 1, M = 50, and ns = 1000, using the numerically exact gradient without sampling and Adam with the initial learning rate β = 0.1. We consider 100 randomly initialized PQC and (a) shows one example calculation and (b) the average over all 100 calculations. Figure 4: Amplitude estimation error δθ as a function of the number of queries Nq obtained using naïve VQAE with k = 1 under the assumption of zero variational cost N var/1 = 0. We observe that for small M , the error follows the ideal VQAE scaling δθ ∼ O(N -3/2 q ) (solid gray line). For larger values of M , the scaling changes to the MC scaling δθ ∼ O(N -1/2 q ) (dotted blue line). The result is also compared to the MLAE scaling δθ ∼ O(N -3/4 q ) (dashed orange line). The legend as well as the simulation parameters are the same as in Fig. 3.

## Adaptive VQAE

To reduce the variational cost of VQAE, in the following we present the adaptive VQAE algorithm. In this algorithm, the function f is rescaled such that the k-th power of the Grover operator is close to the identity and only then the variational optimization is carried out. Then the PQC ansatz needs to be just slightly different from the initial state |φ init and the optimization needs fewer samples than naïve VQAE.

To introduce the adaptive VQAE algorithm, we first note that the amplitude a = E p [f ] -see Eq. (1) -is linear in f , meaning that rescaling the function f with a proportionality constant r also rescales the amplitude a:

The rescaled function f can then be used to encode a new quantum state |χ 0 n+1 and a new Grover operator Q , provided that 0 ≤ f (x) ≤ 1 for all x, which is required for the successful state preparation via Eq. (7). Restricted by this constraint, the rescaling factor has to satisfy 0 ≤ rf (x) ≤ 1 for all x.

To proceed further, we make the observation that the new Grover operator Q implements a rotation by an angle 2θ in the subspace H χ spanned by good and bad renormalized states, as shown in Eq. (9). Under the commensurability condition

applying the renormalized Grover operator Q k results in performing l full rotations in H χ . Such a commensurability condition can be achieved by fixing the renormalization factor as

where θ is uniquely determined by the choice of the desired power k and some integer number l. Hence, we conclude that for a proper choice of r satisfying 0 ≤ r ≤ 1/ max x f (x), it is possible to rescale the function f so that the k-th power of the corresponding Grover operator acts as identity in the subspace of good and bad states, i.e. Q k = I χ in theory.

In practice, however, looking at Eq. (25) we see that finding the exact renormalization factor r requires exact knowledge of the initial amplitude a which, of course, we do not have. However, as we show in the following, a loose estimate a l , obtained from a moderate number of MC samples of the initial state |χ 0 n+1 , is sufficient to get Q k ≈ I χ and use it in adaptive VQAE. Assuming that such a loose amplitude estimate is provided, a loose renormalization factor can then be expressed as r l = a /a l , with a defined as in Eq. (24). Because of this imprecise estimation, the actual value of the amplitude after rescaling becomes a l = sin 2 (θ l ) = r l a and the Grover operator performs l full rotations only approximately, i.e. the previous exact identity transforms into Q k ≈ I χ with a typical phase error per Grover rotation of

For an unbiased loose estimate with zero average, δθ can be interpreted as a random error of zero mean.

After k Grover rotations, this error becomes k times as large.

Next, we use the VQAE algorithm to estimate the amplitude a l by means of the Grover operator Q and the initial state |χ 0 n+1 . The variational approximation is performed at every k-th step, when the overlap

is expected to be the largest. Here we use that θ l + δθ = θ = πl/k. Additionally, we assume that the PQC has the initial state |φ init n+1 = |χ 0 n+1 so that the variational quantum state of Eq. ( 16) reads

Having the PQC initialized to the identity at the beginning of each optimization step, the only role of the variational quantum circuit is to correct the deviation of Eq. ( 26) originating from an imprecise value of the renormalization constant r l and to bring the overlap of Eq. ( 27) as close to one as possible. As a consequence, the variational optimization always starts from a good solution and therefore, in general, converges quicker to a better solution than naïve VQAE. This leads to a significant reduction in variational cost of adaptive VQAE compared to the naïve version of the algorithm. Finally, at the end of the calculation, a maximum likelihood estimation of a l = sin 2 (θ l ) = r l a is obtained. To go back to the original formulation of the problem and compare the results, we use the inverse transformation

where the renormalization constant r l has to be exactly the same as the one used for the function rescaling in order for the prior and posterior rescaling errors to cancel out. This last step concludes the adaptive VQAE algorithm which is summarized in terms of pseudocode as Algorithm 2. We analyze the performance of the adaptive VQAE algorithm with a simplified variational ansatz consisting of only six single-qubit rotation gates and four CNOT gates, as shown in Fig. 2 in dark blue color. This simplified ansatz has only six parameters in total, which significantly reduces the number of variational queries as well as the effects of the noise due to finite sampling. We determine the loose estimate of the amplitude a l via 5 × 10 5 MC samples. As a result, much smaller values of infidelity are achieved for n f being an order of magnitude smaller than in our naïve VQAE computations. We also note that for smaller values of a, the initial MC estimation of a gets worse and, as a consequence, more sweeps are required to ensure the convergence of the variational ansatz.

Our results for adaptive VQAE are presented in Fig. 1, where we show the convergence of δθ as a function of N q for k = 10. The simulations use Adam with the initial learning rate β = 10 -3 , n f = 100, n s = 100, and n p = 6, resulting in N var/1 = 2n f n s n p = 1.2 × 10 5 . As in Fig. 4 ). The major difference of the adaptive VQAE as compared to all previously studied methods is a large starting cost which corresponds to the amount of MC samples required for the evaluation of a l . This starting cost, however, represents only an additive contribution to N q and, hence, is insignificant in the regime of our interest when the number of queries gets large. Additionally, we find that, thanks to a significant improvement of the number of query calls and the overall precision of the variational state, the resulting final error δθ of the adaptive VQAE algorithm surpasses the classical MC error.

Interestingly, we observe that in the regime of small k, the performance of the adaptive VQAE algorithm decreases. This has several reasons. Firstly, the precision of the maximum likelihood estimation decreases when the angle θ = πl/k (where l = 1 in our case) becomes larger than π/4, i.e. for k ≤ 4. Hence, to perform an estimation with such small values of k, a different statistical inference technique has to be considered. Secondly, for small values of k, the rescaling factor can become much larger than one and then leads to more efficient classical MC sampling. Therefore, in calculations with C = 0.1 classical MC sampling performs better than adaptive VQAE for k ≤ 5, corresponding to r 7.508.

To understand how adaptive VQAE performs for increasing qubit counts n, we have run the same simulations as in Fig. 1 for n = 8, 10, and 12. The results for the Gaussian probability distribution are shown in Fig. 5. For the shifted Cauchy-Lorentz and lognormal probability distributions we obtained results (not shown) lying on top of the ones in Fig. 5. We find no significant dependence on n in any of our results. This is surprising as the cost function Eq. ( 14) is global and therefore the vanishing gradient problem [44] should lead to worse results for larger values of n. We conjecture that the equally good performance of adaptive VQAE for all considered values of n is due to the simple variational ansatz as well as the specific problems studied here. Adaptive VQAE uses the simple ansatz shown in Fig. 2 that consists of only 6 variational angles independent of n. Additionally, the ansatz is composed of nearest-neighbour CNOTs and single-qubit R y rotation gates, i.e. not exact local 2-designs as in [44]. The problems studied here are expectation value calculations where an increased qubit count n leads to an increased number of grid points 2 n for the discretized approximation, see Eq. (1). For the smooth functions considered here, we anticipate that the expectation value converges rapidly with increasing number of grid points.

# Discussion

In this article, we provide numerical evidence that variational quantum algorithms based on constantdepth quantum circuits can be more efficient than classical MC sampling in the context of amplitude estimation. The quantum circuits used for our numerical demonstrations, however, are still challenging for this generation of gate-based quantum computers. Therefore, an exciting next step is to find other problems and applications for which VQAE has low quantum hardware requirements and can be realized on actual quantum devices.

We can imagine future applications for VQAE in several areas, including combinatorial optimization, quantum machine learning, and quantum chemistry. In the context of combinatorial optimization, VQAE enables us to use constant-depth quantum circuits to carry out Grover search, which can find the opti- mal solution with a quadratic quantum speedup over brute-force search. Here it is also enticing to study whether such a variational Grover search algorithm can benefit from filtering operators [45]. In relation to quantum machine learning, VQAE has the potential to make it possible for current quantum devices to accelerate inference in Bayesian networks [46], which can then be compared with state-of-the-art variational quantum algorithms for inference [47]. With regards to quantum chemistry, the concept of VQAE can be combined with variational quantum phase estimation (VQPE) [48][49][50] to realize VQPE with shallow circuits on actual quantum hardware. In this context, one interesting application is to use accurate quantum chemistry results obtained with a quantum computer to train an ansatz for the exchange-correlation energy in density functional theory by means of machine learning [51][52][53].

We anticipate that the efficiency of the VQAE algorithm can be further increased. Firstly, it would be interesting to analyse whether a local cost function exists -which can help mitigate the negative effect of barren plateaus [44] -that improves the variational optimization and reduces the required number of variational queries. Secondly, the performance of our variational algorithm crucially depends on the maximum likelihood estimation procedure. It would be interesting to investigate whether alternative approaches perform better, e.g. iterative QAE [18] or QoPrime AE [19].

# Acknowledgements

KP and ML are grateful to David Amaro and Marcello Benedetti for helpful discussions.

