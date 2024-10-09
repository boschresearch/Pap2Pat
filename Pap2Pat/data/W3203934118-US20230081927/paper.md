# Introduction

One of the primary applications of quantum computing is the simulation of materials and molecules, which are inherently quantum mechanical. It is hoped that future powerful quantum computers will be used in the development of materials and drug discovery [1]. Although they have yet to realize commercial application, quantum computers have been improving at a rapid rate, increasing the demand for quantum algorithms with highimpact use cases. To date, the main focus of quantum algorithm development for quantum chemistry and materials has been on ground state energy estimation [2]. This problem is mathematically formulated as estimating the lowest eigenvalue of the Hamiltonian matrix that characterizes the physical system. One of the first quantum chemistry applications of quantum computers was to use quantum phase estimation for estimating the ground state energy of small molecules [3]. More recently, the variational quantum eigensolver algorithm [4] was developed to use near-term intermediate-scale quantum (NISQ) computers to solve the ground state energy estimation problem.

However, in characterizing materials or analyzing small molecules for drug discovery, one often needs to estimate properties of the ground state beyond just the energy. These include transport properties [5], electric dipole moments [6], and molecular forces [7]. Such properties depend on expectation values of observables O with respect to the ground state of a Hamiltonian H. The problem of estimating such quantities was studied in [8,9,10], showing that it is even harder, in a complexity theoretic sense, than the ground state energy estimation problem in general. A straightforward approach to estimating ground state properties is to first (approximately) prepare the ground state, from which properties can be estimated. Many algorithms (e.g. [11,12,13]) have been developed for ground state preparation. However, these algorithms only work for idealistic quantum computers, and the quantum circuit depths involved in these methods are too deep to even be implemented on early fault-tolerant quantum computers. Another approach to preparing ground states that is more amenable to near-term quantum computers is to use the variational quantum eigensolver algorithm [14,7]. However, recent work has suggested that VQE alone is not practical for solving problems of industrial relevance [15]; estimation methods which are more efficient (e.g. [16]) than prepare and measure estimation, as used in VQE, seem necessary in order for quantum computers to compete with state-of-the-art methods in quantum chemistry and materials. Further issues with the variational quantum eigensolver and its variants are that there are no guarantees on the quality of the output ground state and that heuristic optimization methods struggle to prepare high-fidelity ground states.

This motivates the development of quantum algorithms for ground state property estimation (GSPE) which are both reliable and able to be run on near-term quantum computers (e.g. early fault-tolerant quantum devices) with the following characteristics: (1) The circuit depth (or the maximal Hamiltonian evolution time) is small even with the price of increasing the total circuit size (or evolution time). (2) The number of logical qubits is limited. The early fault-tolerant model captures the challenges of building a large-scale long-time coherent quantum device, while also being able to solve many important problems with provable performance guarantees [17,18,19,20,21]. The central question that this paper addresses is then:

Is it possible to estimate ground state properties of a Hamiltonian reliably using early fault-tolerant quantum computers?

In this paper, we provide an affirmative answer to this question. Furthermore, we propose an algorithm for the ground state property estimation using low-depth quantum circuits. The main theorem is stated as follows: Theorem 1.1 (Main theorem, informal). Given a Hamiltonian H and an observable O. Suppose we have access to a unitary U I that prepares a state |φ 0 that has non-trivial overlap with the ground state |ψ 0 of H. Then, there exists an algorithm to estimate ψ 0 | O |ψ 0 with high accuracy and low-depth: the maximal Hamiltonian evolution time is O(γ -1 ), where γ is the spectral gap of H.

We make a few remarks about our main result. First, we note that the maximal evolution time, which is the maximal length of time we need to perform coherent time evolution, can roughly determine the depth of the quantum circuit. Our result achieves a nearly-linear dependence on γ -1 and only poly-logarithmic on the accuracy -1 , which improves the O( -1 ) maximal evolution time in the ground state energy estimation algorithms [22,20,23,24]. Second, our result does not violate the Heisenberg limit because the total evolution time still depends on poly( -1 ). Third, similar to almost all prior works in ground state preparation and energy estimation (e.g. [22,13,20]), we need the assumption that the initial state has some nontrivial overlap with the ground state, as otherwise the problem will become computationally intractable. Last, we consider the Hamiltonian as a black-box, which is a common model in this field. To implement our algorithm, for sparse local Hamiltonian, we can use the current state-of-the-art Hamiltonian simulation methods [25,26,27,28] with gate complexity depending linearly in the evolution time and logarithmically in the accuracy.

Comparison to the straightforward method. We can compare our algorithm with the straightforward approach of GSPE that first prepares the ground state and then applies quantum phase estimation (QPE) to estimate the ground state property.

• In the first step, to achieve an -accuracy for the estimation, the ground state need to be prepared with fidelity at least 1 -using the methods in [12,13], which have circuit depth O(γ -1 η -1 ) where η is the overlap between the initial state and the ground state.

• In the second step, QPE [29,24] requires circuit depth O( -1 ) for an -accuracy estimation for the ground state property.

Therefore, this straightforward approach has circuit depth O(γ -1 η -1 + -1 ), while our algorithm has circuit depth O(γ -1 ). Furthermore, they also need many (i.e., ω(1)) additional ancilla qubits for preparing the ground state, while we only use one ancilla qubit.

Our algorithm has a great advantage when the Hamiltonian's spectral gap is much larger than the estimation accuracy, making it easier to be implemented in the early fault-tolerant devices.

Organization. In Section 2 we formally state the problem of ground state property estimation. In Section 3 we review the method developed in [20] for estimating ground state energies. In the next three sections we explain our main algorithms and give an analysis for their performances starting from the simplest case and building to the mostinvolved, general case. Section 4 presents the case of a unitary observable which commutes with the Hamiltonian. Section 5 presents the case of a unitary observable which does not necessarily commute with the Hamiltonian. Section 6 describes the case of a general observable. Then, Section 7 gives two applications of the ground state property estimation algorithm. Section 8 gives a discussion of the results and presents some open questions.

# Ground State Property Estimation Problem

In this section, we will formally define the ground state property estimation problem. This problem was initially studied by Ambainis [8] as the approximate simulation problem (APX-SIM), and he proved that APX-SIM is P QMA[log] -complete i .

Problem 2.1 (Approximate simulation (APX-SIM), [8]). 

In the follow-up works, APX-SIM was shown to be P QMA[log] -complete even for 5-local Hamiltonian and 1-local observable [9], and also for some physics models like 2D Heisenberg model and 1D nearest-neighbor, translationally invariant model [10,30]. However, these previous studies only focused on the decision version of this problem. For the purpose of designing efficient algorithms, we first define the "search version" of APX-SIM as follows:

# Problem 2.2 (Search version of APX-SIM). Given a Hamiltonian H, an (local) observable

O, and ∈ (0, 1), with Ω(1) probability, estimate ψ 0 | O |ψ 0 with an additive/multiplicative error at most .

In general, Problem 2.2 will not be more tractable than Problem 2.1. Thus, we may need some prior information about the Hamiltonian H and its ground state. Motivated by the widely used variational quantum eigensolver (VQE) [31,32] and the Hartree-Fock method [33] in quantum chemistry, it is often the case that for many real-world Hamiltonians, we are able to efficiently prepare an initial state |φ 0 that has a nontrivial overlap with the ground state. Moreover, we assume that the Hamiltonian H has a nontrivial spectral gap, where a large family of Hamiltonians in practice satisfy this condition. With these assumptions, we formally define the ground state property estimation problem as follows: Problem 2.3 (Ground state property estimation (GSPE)). Given a Hamiltonian H with spectral gap γ and ground state |ψ 0 , an observable O, a unitary U I such that it prepares an initial state |φ 0 with | φ 0 |ψ 0 | 2 ≥ η, and ∈ (0, 1), estimate ψ 0 | O |ψ 0 with an additive/multiplicative error at most with Ω(1) probability. Remark 2.4. We notice that when O = H, Problem 2.3 becomes the ground state energy estimation problem. Moreover, the prior knowledge of a large overlap for the initial state is required for all quantum algorithms with provable performance guarantees (e.g. [12,13,20]). It is also worth noting that even with these assumptions, it is unlikely to use a purely classical algorithm to estimate the ground state energy or property to high precision (unless P = BQP) [34].

We propose a high-accuracy, early fault-tolerant quantum algorithm for GSPE that satisfies the following properties:

• The maximal evolution time depends logarithmically on the accuracy and overlap η.

• In addition to the Hamiltonian evolution and observable implementation, it only uses one additional ancilla qubit.

# An Overview of the Low-Depth Ground State Energy Estimation

In this section, we provide a brief overview of the low-depth ground state energy estimation algorithm proposed by Lin and Tong [20]. Our algorithms are inspired by this algorithm and use it as a subroutine. More specifically, they showed that: 20]). Given a Hamiltonian H with eigenvalues in the interval [-π/3, π/3] and its ground state |ψ 0 has energy λ 0 . And suppose we can prepare an initial state |φ 0 such that p 0 ≥ η for some known η, where p 0 := | φ 0 |ψ 0 | 2 . Then, for any , ν ∈ (0, 1), there exists an algorithm that estimates λ 0 with an additive error with probability 1 -ν, by running a parameterized quantum circuit with the maximum quantum evolution time O( -1 ) and the expected total quantum evolution time O( -1 η -2 ).

The pseudo-code of their algorithm is given in Algorithm 1. 

# Algorithm 1 Ground State Energy Estimation

for i ← -d, . . . , d do 5:

Compute θ i , the phase angle of F i 7:

end for 8:

Sampling from the quantum circuit 

Measure (X k , Y k ) by running the quantum circuit with (Figure . 1) parameter k 14:

end for

# 16:

Classical post-processing 17:

x L ← -π/3, X R ← π/3 

end for 23:

else 26:

end if

# 28:

end while 29:

The main technique of their algorithm is a classical post-processing procedure that extracts information from the following Hadamard test circuit (Figure 1). Let the initial state |φ 0 be expanded as |φ 0 = k α k |ψ k in the eigen-basis of H and let p k := |α k | 2 be the overlap with the k-th eigenstate. They considered the overlaps p 0 , p 1 , . . . as a density function:

(1)

Then, the cumulative distribution function (CDF) C(x) := x -π p(t)dt can be expressed as a convolution of p(x) and the 2π-periodic Heaviside function H(x), which is 0 in [(2k -1)π, 2kπ) and 1 in [2kπ, (2k + 1)π) for any k ∈ Z. Thus, C(x) is also a periodic function, which makes it convenient to apply the Fourier approximation. They showed that H(x) can be approximated by a low-Fourier degree function F (x) in the intervals [-π+δ, -δ] and [δ, π -δ]. Then, they defined the approximated cumulative distribution function (ACDF) as C(x) := (F p)(x) and proved that

Moreover, for each x, we have

where F j is the Fourier coefficient of F (x). Note that φ 0 | e -ijH |φ 0 can be estimated via the parameterized quantum circuit (Figure 1). Hence, we can estimate the ACDF at every point in [-π/3, π/3]. Moreover, they showed that the multi-level Monte Carlo method can be applied here to save the number of samples needed to achieve a high-accuracy estimation (Line 21). Therefore, we can estimate the ground state energy λ 0 by locating the first non-zero point of the CDF C(x), which is η/8-approximated by the ACDF C(x). Since we assume that p 0 ≥ η, the approximation error and the estimation error of C(x) can be tolerated, and we can find λ 0 via a robust binary search (Line 18).

We note that the maximal evolution time of this algorithm corresponds to the Fourier degree of F (x), which is O( -1 ) by the construction, making their algorithm suitable for early fault-tolerant quantum devices. More details of this algorithm and the proofs are given in Appendix A.

# Algorithm for Commutative Case

In this section, we consider a easier case that O is unitary and commutes with the Hamiltonian H, and give a two-step quantum-classical hybrid algorithm for Problem 2.3. More specifically, suppose the initial state can be expanded in the eigenbasis as follows:

We note that {|ψ k } is also an eigenbasis of O since O and H commute. In Step 1, we run [20]'s algorithm to estimate the ground state energy λ 0 and the overlap between the initial state and the ground state p 0 . In Step 2, we construct a similar CDF function for the density k O k p k δ(x -λ k ), where O k := ψ k | O |ψ k . If we evaluate the CDF at λ 0 , we can obtain an estimate of O 0 .

## Step 1: estimate the initial overlap

We first run the procedure EstimateGSE (Algorithm 1) to estimate the ground state energy λ 0 with an additive error . Let x be the output. We remark that x satisfy C(x + τ ) ≥ p 0 and C(x -τ ) = 0. However, we can only extract p 0 from the ACDF C(x), which satisfies:

If [x -τ , x + τ ] contains a "jump" of C(x), i.e., an eigenvalue λ k , then the approximation error of C(x) will be large. Hence, we say a point x is "good" for

It is easy to see that C(x) will be an η/8-additive approximation of j≤k p k if x is good. Our goal is to find an x good that is good for λ 0 , and estimating C(x good ) gives the overlap p 0 . The following claim gives a way to construct x good using the spectral gap of H. Claim 4.1 (Construct x good ). Let γ be the spectral gap of the Hamiltonian H. For any ∈ (0, γ/4), x + τ γ/2 is good for λ 0 , where x is the output of EstimateGSE( , η) (Algorithm 1).

Proof. We know that x satisfies:

x -τ < τ λ 0 ≤ x + τ .

(5)

Then, we have

We also have

Therefore, x is good for λ 0 .

We note that in [20], the ACDF's approximation error is chosen to be η/8. We may directly change it to η/8 without significantly changing the circuit depth, since by Lemma A.8 the degree of F can only blowup by a log factor of . Lemma 4.2 (Estimating the overlap). For any 0 , ν ∈ (0, 1), the overlap p 0 := | φ 0 |ψ 0 | 2 can be estimated with multiplicative error 1 ± O( 0 ) with probability 1 -ν by running the quantum circuit (Figure 1) O( -2 0 η -2 ) times with expected total evolution time O(γ -1 -2 η -2 ) and maximal evolution time O(γ -1 ).

Proof. By Claim 4.1, if we set the additive error of ground state energy λ 0 to be O(γ), then we can construct an x good that is good for λ 0 . By Theorem 3.1, it can be done with maximum quantum evolution time O(γ -1 ) and the expected total quantum evolution time O(γ -1 η -2 ). Notice that we need to take d = O(δ -1 log(δ -1 -1 0 η -1 )) (Line 3 in Algorithm 1) to make C(x good ) be an O( 0 η)-approximation of p 0 , where δ = τ γ.

Next, we estimate C(x good ) with additive error η with probability 1 -ν. We have an unbiased estimator

for C(x), where Z := X + iY is measured from the Hadamard test, and J is a random variable for the Hamiltonian evolution time sampled proportional to the Fourier weight of

We can show that G(x; Z, J) has variance O(log 2 (d)), and one estimate can be obtained with evolution time O(τ d/ log(d)) in expectation. If we repeatedly sample G(x; Z, J) and take the mean of them, then by Chebyshev's inequality, the sample complexity is O( -2 0 η -2 ν -2 ) to have an additive error O( 0 η) with probability 1 -ν. Instead, we can use the so-called "median-of-means" trick to reduce the sample complexity. More specifically, let N g = O(log(1/ν)) and K = O( -2 0 ). We first partition m = N g K samples (Z 1 , J 1 ), . . . , (Z m , J m ) into N g groups of size K. Then, for any i ∈ [N g ], the i-th group mean is

The final estimator is given by the median of these group means, i.e.,

# G(x)

By Chernoff bound, it is easy to see that G(x) has an additive error at most (η 0 ) with probability 1-ν. It will imply that multiplicative error is at most 1±O( 0 ) since p 0 = Θ(η).

And the sample complexity of G(x) is O( -2 0 η -2 ). Hence, the expected total evolution time is O(γ -1 -2 0 η -2 ). Since we run the same quantum circuit to estimate G(x), the maximal evolution time is still O(γ -1 ).

## Step 2: estimate the O-weighted CDF

To estimate the expectation value of O, consider the following quantum circuit: Define the random variables X j , Y j be as follows: for W = I, X j := 1 if the outcome is 0, and X j := -1 if the outcome is 1. For W = S, Y j := -1 if the outcome is 0, and Y j := 1 if the outcome is 1.

Then, we have the following claim on the expectation of the random variables X j , Y j :

# Claim 4.3 (A variant of Hadamard test).

For any j ∈ Z, the random variable X j + iY j is an un-biased estimator for φ 0 | Oe -ijτ H |φ 0 .

The proof is deferred to Appendix A.1. We can expand φ 0 | Oe -ijτ H |φ 0 in the eigenbasis of H (which is also an eigenbasis of O):

where the last step follows from the simultaneous diagonalization of O and H, and

Inspired by the ground state energy estimation algorithm in [20], we define the Oweighted "density function" for the observable as follows:

Note that p O (x) can be negative at some points. Suppose the eigenvalues of τ H is within [-π/3, π/3]. Then, we define the O-weighted CDF and ACDF for p O (x) similar to [20]:

where H is the 2π-periodic Heaviside function and

The following lemma gives an unbiased estimator for the O-weighted ACDF. Proof. C O (x) can be expanded in the following way:

where the third step follows from the Fourier expansion of F (x -y), the fifth step follows from the property of Dirac's delta function, and the last step follows from the definition of p k and the eigenvalues of matrix exponential.

Define an estimator G(x; J, Z) as follows:

where θ j is defined by F j = | F j |e iθ j , Z = X + iY measured from the quantum circuit (Figure 2) with parameter j = J, and

Then, we show that G(x; J, Z) is un-biased:

where the third step follows from Claim 4.3. Moreover, the variance of G can be upperbounded by:

where the third step follows from |e i(θ J +Jx) | = 1, and the last step follows from X j , Y j ∈ {±1}. By Lemma A.8, we know that

The expected total evolution time is

The lemma is then proved.

The following lemma shows that the O-weighted CDF C O (x) can be approximated by the O-weighted ACDF C O (x): Lemma 4.5 (Approximating the O-weighted CDF). For any > 0, 0 < δ < π/6, let F (x) := F d,δ (x) constructed by Lemma A.8 with approximation error η /8. Then, for any x ∈ [-π/3, π/3], it holds that:

The proof is very similar to Lemma A.9, so we omit it here. We can take δ := τ γ/5 and let x good := x + τ γ/2. Then, by Claim 4.1, we know that x good is good for λ 0 , i.e., [x good -τ γ, x good + τ γ] ⊂ (τ λ 0 , τ λ 1 ). Hence, C O (x good ) satisfies

The following lemma shows how to estimate C O (x good ), which is very similar to Lemma 4.2.

Lemma 4.6 (Estimating p 0 O 0 ). For any 1 , ν ∈ (0, 1), p 0 O 0 can be estimated with multiplicative error 1 ± O( 1) with probability 1 -ν by runs the quantum circuit (Figure 1)

) and maximal evolution time O(γ -1 ).

## Putting it all together

In this section, we will put the components together and prove the following main theorem, which gives an algorithm for the ground state property estimation. Theorem 4.7 (Ground state property estimation with commutative observable, restate). Suppose p 0 ≥ η for some known η, and let γ > 0 be the spectral gap of the Hamiltonian. Then, for any , ν ∈ (0, 1), the ground state property ψ 0 | O |ψ 0 can be estimated within additive error at most with probability 1 -ν, such that:

1. the number of times running the quantum circuits (Figure 1 and2

# the maximal evolution time is O(γ -1 ).

Proof. By Lemma 4.2, we obtain an estimate p 0 for p 0 with the guarantee that

where 0 will be chosen shortly. By Lemma 4.6, we obtain an estimate p 0 O 0 for p 0 O 0 with the guarantee that

where 1 will be chosen shortly. Then, we have

where the second step follows from the triangle inequality, the third step follows from Eqs. ( 25) and ( 26), the third step follows from p 0 ≥ η, the fifth step follows from

Hence, if we take 0 = 1 = O( ), we will achieve additive error at most . For the success probability, we can make Eq.( 25) hold with probability 1 -ν/2 in Lemma 4.2 and Eq.( 26) hold with probability 1 -ν/2 in Lemma 4.6. Then, by the union bound, we get a good estimate with probability at least 1 -ν.

The computation costs follow directly from Lemma 4.2 and Lemma 4.6. And the proof of the theorem is then completed.

# Algorithm 2 Ground State Property Estimation (Commutative Case)

1: procedure EstimateGSProp( , τ, η, γ, ν)

Compute F j := F d,δ,j and θ j 5:

end for

# 6:

Estimate the ground state energy 7:

x ← EstimateGSE(γ/8, τ, η, ν/10) 8:

Generate samples from the Hadamard test circuits 10:

Sample (Z k , J k ) from the quantum circuit (Figure 1)

Sample (Z k , J k ) from the quantum circuit (Figure 2) 

end for 19:

end for 24:

return p 0 O 0 /p 0 26: end procedure 5 

# Algorithm for General Unitary Observables

In this section, we will prove the following theorem for unitary observables in the general case: Theorem 5.1 (Ground state property estimation with general unitary observable). Suppose p 0 ≥ η for some known η and the spectral gap of the Hamiltonian H is at least γ. For any , ν ∈ (0, 1), there exists an algorithm for estimating the ground state property ψ 0 | O |ψ 0 within additive error at most with probability at least 1 -ν, such that:

# the maximal evolution time is O(γ -1 ).

In the following parts, we will first introduce the 2-d O-weighted density function and CDF, which extend the commuting observables to the general case. Then, we will show how to combine them with the overlap estimation in Section 4.1 for proving Theorem 5.1.

## 2-d O-weighted density function and CDF

In general, O and H may not commute. Hence, we consider a more symmetric form of expectation: φ 0 | e -ijτ H Oe -ij τ H |φ 0 , which can be expanded in the eigenbasis of H as follows:

Similar to the commutative case, we define a 2-d O-weighted density function:

where

Then, define the corresponding 2-d O-weighted CDF function as follows:

where

Hence, the definition of C O,2 is reasonable. Then, we show that C O,2 can be approximated similar to the 1-d case. Let F 2 (x) be the 2-d approximated Heaviside function, i.e.,

The 2-d O-weighted approximated CDF (ACDF) is defined to be

The following lemma shows that C O,2 (x, y) is close to C O,2 (x , y ) for some (x , y ) close to (x, y).

# Lemma 5.2 (Approximation ratio of the 2-d O-weighted ACDF). For any

Proof. By (2) in Lemma A.8, we have

which implies that for all x, y ∈

where the last step follows from F (x) ∈ [0, 1] by (1) in Lemma A.8. Furthermore, we also have for

Let p 2 := p O,2 . Then, for any x, y ∈ [-π/3, π/3], we have

where the second step follows from Cauchy-Schwarz inequality, the third step follows from partitioning the integration region, the forth step follows from Eq. ( 43) and the fact that p(x, y) is supported in [-π/3, π/3] × [-π/3, π/3] and δ < π/6 (see Figure 3   Hence, we have

which proves the first inequality:

Similarly, we can define F R,2 := F 2 (x + δ, y + δ) and C R,2 (x, y) := (F R,2 * p 2 )(x, y). We can show that

which gives

The lemma is then proved.

## Estimating the 2-d ACDF

We use the following parameterized quantum circuit to estimate the 2  4) O( -2 η -2 log(1/ν)) times with maximal evolution time O(γ -1 ) and total expected evolution time O(γ -1 -1 η -1 ).

Proof. C O,2 (x, y) can be expanded in the following way:

To estimate φ 0 | e -ijτ H Oe -ij τ H |φ 0 , we use the multi-level Monte Carlo method. Define a random variables J, J with support

where

Then, let Z := X J,J + iY J,J ∈ {±1 ± i}. Define an estimator G 2 (x; J, J , Z) as follows:

where θ j is defined by F j = | F j |e iθ j , and similar definition for θ j . Then, we show that G 2 (x, y; J, Z) is un-biased:

= |j|≤d,|j |≤d

where the third step follows from Claim A.1. Moreover, the variance of G 2 can be upperbounded by:

where the third step follows from |e i(θ J +Jx) | = |e i(θ J +J y) | = 1, and the last step follows from X j,j , Y j,j ∈ {±1}. By Lemma A.8, we know that F = O(1). Hence, we have for all x, y ∈ [-π/3, π/3],

Then, using median-of-means estimator, we can obtain an -additive error estimate of

The maximal evolution time is 2d = O(γ -1 ). And the expected evolution time for one trial is

Hence, the total expected evolution time is

The lemma is then proved.

Similar to the 1-d case, we can construct a "good" point for (λ 0 , λ 0 ) via the following claim. And the blue square is the approximation region of (x good , y good ) such that C O,2 (x good , y good ) is close to some C O,2 (x, y) in this region.

Claim 5.4 (Construct 2-d good point). Let γ be the spectral gap of the Hamiltonian H. Let x good := x + τ γ/2 where x is the output of EstimateGSE(γ/8, τ, η, ν/10) (Algorithm 1). Then, (x good , x good ) is good for (λ 0 , λ 0 ). In particular, for any ∈ (0, 1), if the approximation error of F (x) is set to be η, then

Proof. By Claim 4.1, we know that x good is good for λ 0 , i.e., [x good -δ, x good + δ] is contained in [λ 0 , λ 1 ). It also holds in the 2-d case for (x good , x good ). Then, by Lemma 5.3, we have

The claim then follows from C O,2 (x, y) = C O,2 (λ 0 , λ 0 ) for any (x, y) ∈ [λ 0 , λ 1 ) × [λ 0 , λ 1 ).

## Putting it all together

The main algorithm for the ground state property estimation will first estimate the ground state energy λ 0 and the overlap p 0 , which are described in Section 4.1. Then, by Lemma 5.3 and Claim 5.4, the weighted expectation p 0 O 0 can also be estimated. Hence, we will obtain an estimate for O 0 = ψ 0 | O |ψ 0 .

# Algorithm 3 Ground State Property Estimation (General Case)

1: procedure EstimateGSProp( , τ, η, γ, ν)

))

3:

for j ← -d, . . . , d do

# 4:

Compute F j := F d,δ,j and θ j 5:

end for

# 6:

Estimate the ground state energy 7:

x ← EstimateGSE(γ/8, τ, η, ν/10) 8:

Generate samples from the Hadamard test circuits 10:

11:

for k ← 1, . . . , BK do 12:

Sample (Z k , J k ) from the quantum circuit (Figure 1)

) from the quantum circuit (Figure 4)

end for 15:

Estimate p 0 16:

end for 19:

Estimate p 0 O 0 21:

x good , x good ; Z (i-1)K+j , J (i-1)K+j,1 , J (i-1)K+j,2 ) Eq. ( 53) 

For the success probability, Algorithm 3 has three components: estimate ground state energy, estimate p 0 , and estimate p 0 O 0 . By our choice of parameters, each of them will fail with probability at most ν/3. Hence, Algorithm 3 will succeed with probability at least 1 -ν.

The maximal evolution time and the total expected evolution time follows from Theorem 3.1, Lemma 4.2, and Lemma 5.3.

# Handling non-unitary observables

One may notice that Algorithm 3 works only for unitary observables because it needs to use the circuit in Figure 4 to estimate φ 0 | e -it 2 H Oe -it 1 H |φ 0 for certain t 1 , t 2 ∈ R, in which controlled-O must be a unitary operation. In this section, we show that under reasonable assumptions this algorithm can be modified to estimate the ground state property ψ 0 | O |ψ 0 where O is a general observable.

Before we present this result, one may wonder why it is necessary. After all, we can always decompose O into a linear combination of Pauli strings O = s w s P s , and use Algorithm 3 to estimate each term µ s := ψ 0 | P s |ψ 0 individually, and return s w s µ s as the result. While this strategy works in principle, it might be not efficient enough to be practical, depending on the weights w s 's of Pauli strings in the linear expansion of O.

Alternatively, one can fix the issue of Algorithm 3 by designing a procedure for estimating φ 0 | e -it 2 H Oe -it 1 H |φ 0 for arbitrary non-unitary O. Such quantities are utilized in the same way as before. We have followed this approach and found that it is possible when there is a block-encoding of O. Namely, suppose O is an n-qubit observable with O ≤ 1 and U is an (n + m)-qubit unitary operator such that

for some α ≥ O . More details about the block-encoding model can be found in [35,28,36,37]. Then we can still perform Hadamard test for U to estimate φ 0 | e -it 2 H Oe -it 1 H |φ 0 for arbitrary t 1 , t 2 ∈ R. The main theorem of this section is stated below: Theorem 6.1 (Ground state property estimation with block-encoded observable). Suppose p 0 ≥ η for some known η and the spectral gap of the Hamiltonian H is at least γ. Suppose we have access to the α-block-encoding of the observable O. For any , ν ∈ (0, 1), there exists an algorithm for estimating the ground state property ψ 0 | O |ψ 0 within additive error at most with probability at least 1 -ν, such that:

# the maximal evolution time is O(γ -1 ).

Proof sketch of Theorem 6.1. The algorithm for handling non-unitary block-encoded observables is quite similar to Algorithm 3 for handling unitary observables, except that it relies on a different procedure to estimate φ 0 | e -it 2 H Oe -it 1 H |φ 0 for arbitrary t 1 , t 2 ∈ R.

Here we briefly describe this procedure and defer the detailed analysis to Appendix B. Let C-V := |0 0| ⊗ I + |1 1| ⊗ V be the controlled-V operation for arbitrary unitary operator V . Let |φ 0 be an arbitrary n-qubit state. Consider the following procedure (as illustrated in Figure 6: 2. Apply a Hadamard gate on the first register.

3. Apply a C-e -iHt 1 on the first and third registers.

4. Apply C-U on the current state, obtaining

5. Measure the second register in the standard basis. If the outcome is not 0 m , then this procedure fails; otherwise, continue. The probability of this step succeeding is

and when this event happens, the state becomes

6. Apply a C-e -iHt 2 on the first and third registers. The state becomes

7. Apply W = I or phase gate S on the first register.

8. Apply a Hadamard gate on the first register. 9. Measure the first register in the standard basis. Then if W = I, the (conditional) probability of getting outcome 0 is

if W = S, this probability is

Now we define two random variables X and Y as follows. First, we run the above procedure with W = I in step 7. If step 5 fails, X = 0; otherwise, if the measurement outcome is 0 or 1 in step 9, then X = α or -α, respectively. One can show that X is an unbiased estimator of Re[

Y is defined similarly. We run the above procedure with W = S in step 7. If step 5 fails, Y = 0; otherwise, if the measurement outcome is 1 or 0 in step 9, then Y = α or -α, respectively. Then Y is an unbiased estimator of Im[ φ 0 | e -iHt 2 Oe -iHt 1 |φ 0 ], i.e.

It follows that Z := X + iY is an unbiased estimator of φ 0 | e -iHt 2 Oe -iHt 1 |φ 0 , i.e.

Equipped with the above method for estimating φ 0 | e -iHt 2 Oe -iHt 1 |φ 0 for arbitrary t 1 , t 2 ∈ R, we can now use the same strategy as in Lemma 5.3 to estimate C O,2 (x, y). The other components of Algorithm 3 remain intact. The analysis of this modified algorithm is almost the same as before, except that now we have

As a consequence, compared to Theorem 5.1, the total evolution time of this modified algorithm is larger by a factor of O(α 2 ), while its maximal evolution time is of the same order.

# Applications

In this section, we discuss some applications of our ground state property estimation algorithm. To define an application of the ground state property estimation algorithm, we must specify a Hamiltonian of interest H and an observable of interest O. An example application used in quantum chemistry and materials is the Green's function (see, e.g. [38]), where O = a i (z -(H -E 0 ) -1 )a † j . In the following two sections we describe another example from quantum chemistry and materials as well as an example of a linear algebraic subroutine.

## Charge density

The primary application of the technique is the estimation of ground state properties of physical systems. Here we describe how to compute the charge density of a molecule, which can be used to compute properties like electric dipole moments of a molecule [39]. From a second-quantized representation of the electronic system (assuming fixed positions of the nuclear positions), the charge density is determined from the one-particle reduced density matrix as,

where e is the electric constant, D p,q is the one-electron reduced density matrix (1RDM) of the ground state, and φ q ( r) are the basis wave functions chosen for the second-quantized representation of the electronic system [40]. The 1RDM of the ground state is a matrix of properties of the ground state with each entry defined as

where a p are annihilation operators. The operators involved in the 1RDM can each be expressed as a linear combination of unitary operators using the Majorana representation a p = 1 2 (γ 2p + iγ 2p+1 ), where the γ k are hermitian and unitary ii ,

ii To implement this application on a quantum computer we must represent the unitaries as operations on qubits. For an n-electron system, using the Jordan-Wigner or Bravyi-Kitaev transformation [41], each Majorana operator, and products thereof, can be represented as a Pauli string.

Accordingly, we may use the method of Section 5 to estimate each entry of the 1RDM and then obtain the charge density function of the ground state. As a point of comparison, we could alternatively use the variational quantum eigensolver algorithm to prepare an approximation to the ground state and then directly estimate each of the Pauli expectation values. However, there is no guarantee on whether a target accuracy for the ground state approximation can be achieved. Remarkably, the methods introduced in this paper can be used to ensure a target accuracy in the estimation regardless of the quality of ground state approximation, though possibly at the cost of an increase in runtime.

## Quantum linear system solver

In the seminal [42] paper, a quantum algorithm is proposed to generate a quantum state approximately proportional to the solution of a linear system of equations. Namely, given a linear system A x = b, the algorithm produces a quantum state close to |x :=

, where x j 's are the entries of x = A -1 b. In fact, in many cases, we only need to know x| M |x , where M is a linear operator. For example, in quantum mechanics, many features of |x can be extracted in this way, including normalization, moments, etc. One approach to solve this problem is first solving the linear system using any quantum linear system solver [42,43,35,36] to obtain the state |x and then performing the measurement of M . However, a shortcoming of this method is that most of the quantum linear system solvers require deep quantum circuits. And hence, the needed quantum resources may not be accessible in the near future.

Recently, a few quantum algorithms [44,45,46] were developed to solve linear systems of equations by encoding such a system into an effective Hamiltonian

whose ground state corresponds to the solution vector |x . We can combine this idea with our ground state property estimation algorithm to get a low-depth algorithm for estimating the properties of linear system solution. More specifically, suppose we can simulate the Hamiltonian H G for some specified time and we know the normalization factor τ such that the eigenvalues of τ H G are in [-π/3, π/3]. For the operator M , we can assume that M can be decomposed into a linear combination of Pauli operators M = L =1 c σ , or we assume that M is given in the block-encoding form. The estimation algorithm has two steps:

1. Run a quantum linear system algorithm (e.g. [46], [47], or [48]) with constant precision to prepare an initial state |φ 0 such that

2. Using |φ 0 from step 1 as the initial state, run Algorithm 3 to estimate x| M |x within -additive error for any ∈ (0, 1).

Step 1 takes O(κ) time, where κ is the condition number of A. To analyze the computation cost of the second step, we need a lower-bound on the spectral gap of H G . Since x| A † (I -|b b|)A |x = 0, we have λ 0 (H G ) = 0. For the second smallest eigenvalue, since H G = A † A -A † |b b| A, by Weyl's inequality, we have

where the second step follows from A † |b b| A is rank-1. Due to the normalization, the smallest (normalized) singular value of A is Ω(κ -1 ). Hence, we have γ = Ω(κ -2 ).

By Theorem 5.1, the maximal evolution time of the Hamiltonian will be O(κ 2 ). To further improve the circuit depth, we may apply the gap amplification technique [49,46] to quadratically increase the spectral gap of H G . Specifically, consider the following family of Hamiltonians:

where

Note that these Hamiltonians act on the original system and two ancilla qubits. Then we have

where

As shown in [46], the eigenvalues of H G (s) are

where λ j (s)'s are the nonzero eigenvalues of HG (s). In addition, for s = 1, one can use Weyl's ineqality to show that λ 1 (1) ≥ κ -2 , which implies that the smallest nonzero eigenvalue of H G (1) is Ω(κ -1 ), as desired.

We can use the algorithm in [46] to prepare a state that has Ω( 1 G (1) is zero, we do not need to first estimate the ground state energy using Algorithm 1. Instead, we directly evaluate the O-weighted CDF at zero. Therefore, by Theorem 6.1, we get the following result: Corollary 7.1 (Quantum linear system solution property estimation). For a linear system

Then, for any linear operator M given by its α-block encoding unitary U M , and for any ∈ (0, 1), the expectation value x| M |x can be estimated with -additive error with high probability such that:

• the depth of each circuit is O(κ).

• the expected total runtime is O(κ -2 α 2 ).

For comparison, the algorithm in [46] needs O(κ -1 ) circuit depth to obtain a state that is -close to |x , which is larger than ours. Moreover, to estimate x| M |x , even with amplitude estimation, it still needs Ω( -1 ) copies of the state to achieve -additive error. Hence, its total runtime will be O(κ -2 ), nearly matching our result (ignoring the dependence on the α factor).

# Discussion and Outlook

We have shown a quantum-classical hybrid algorithm for estimating properties of the ground state of a Hamiltonian, such that the quantum circuit depth is relatively small and only poly-logarithmically depends on -1 . Therefore, the algorithm has a significant advantage in high-accuracy estimation, and it is possible to be implemented in early faulttolerant devices. In practice, our algorithm can solve many important tasks by combining with some initial state preparation methods (e.g., VQE or QAOA). In this paper, we provide two examples, one in quantum chemistry and another in solving linear systems. And we believe more applications will be explored in the future.

Another important direction is to improve the total evolution time of our algorithm which quadratically depends on -1 . The blowup comes from evaluating the O-weighted CDF in high precision and a trade-off between maximal evolution time and total evolution time. However, this does not meet the Heisenberg-limit of linear dependence on -1 for generic Hamiltonians [50]. In our main result (Theorem 5.1), the -2 η -2 factor comes from the number of samples needed to reduce the estimator's error to O( η). Amplitude estimation can be used to reduce this number of samples and the total evolution time. However, this comes at the cost of significantly increasing the maximal evolution time, which could require large fault-tolerant overheads for reliable implementation. A strategy to achieve improved performance that is more amenable to early fault tolerant quantum computers is to use recently introduced "enhanced sampling" techniques [16]. If λ characterizes the fidelity decay rate of the circuit as deeper circuits are used, then we would expect to need a maximal evolution time of O(λ -1 γ -1 ) and an total evolution time of O(λγ -1 -2 η -2 ). Note that because this approach incorporates the impact of error into the algorithm, the maximal evolution time is of no concern. Rather than being a cost that needs monitoring, the maximal evolution time is chosen by the algorithm to minimize the total evolution time. With this, we expect that as the quality of devices is improved, the performance of the algorithm improves proportionally. We note that a similar approach can also be applied to improve the total evolution time in [20] 

This work fits into the paradigm of "beyond the ground state energy" and studies more general properties of the ground state. Can we go further beyond the ground state? Some prior works have explored the estimation of such kind of properties of Hamiltonian. For example, Brown, Flammia, and Schuch [51] studied the density of states. Jordan, Gosset, and Love [52] focused on the energy of excited states. Gharibian and Sikora [53] identified the energy barriers. Watson and Bausch [54] explored detecting phase transitions via order parameters. In general, for an unknown Hamiltonian, these estimation problems will be hard. An interesting open problem is, given some prior knowledge of the Hamiltonian, can we design efficient or low-depth quantum algorithms for estimating Hamiltonian properties beyond ground state?

we have

For the imaginary part ( φ 0 | e -ijτ H |φ 0 ), we can set W to be the phase gate 1 0 0 -i and define the random variable Y j similarly. Then, we have

Therefore, Eqs. (84) and (85) implies the following claim:

Claim A.1 (Estimator of the Hamiltonian expectation). For any j ∈ Z, the random variable X j + iY j is an un-biased estimator for φ 0 | e -ijτ H |φ 0 .

# A.2 Classical part of the algorithm

Let τ be a normalization factor such that τ H ≤ π/3. Suppose the initial state |φ 0 can be decomposed in the eigenspace of H as |φ 0 = k √ p k |ψ k . Let p(x) be the following density function (spectral measure):

That is, p(x) is the distribution of the state energy with respect to τ H after we measure |φ 0 in the eigenbasis of H. Define the 2π-periodic Heaviside function by

Then, we define the 2π-periodic CDF of p as the convolution of H and p:

For any x ∈ [-π/3, π/3], for any w ∈ Z, we have

where the first step follows from the definition of convolution, the second step follows from Dirac delta function's property, and the third step follows from H has period 2π. We note that C(x) is right continuous and non-decreasing in [-π/3, π/3]. However, we cannot directly evaluate C(x), but we can approximate it! Define the approximate CDF (ACDF) as

where F (x) = |j|≤d F j e ijx is a low Fourier-degree approximation of the Heaviside function

The construction of F is given by Lemma A.8. Furthermore, the approximation error of C(x) is bounded by

for any x ∈ [-π/3, π/3], δ ∈ (0, π/6) and > 0.

# A.2.1 Estimating the ACDF

The goal of this section is to prove Lemma A.2, which constructs an estimator for C(x) (defined by Eq. (91)).

# Lemma A.2 (Estimating the ACDF).

For any σ > 0, for any x ∈ [-π, π], there exists an un-biased estimator G(x) for the ACDF C(x) with variance at most σ 2 . Furthermore, G(x) runs the quantum circuit (Figure 1) O( log 2 d σ 2 ) times with expected total evolution time O( τ d log d σ 2 ).

Proof. C(x) can be expanded in the following way:

F j e ij(x-y) p(y)dy

where the third step follows from the Fourier expansion of F (x -y), the fifth step follows from the property of Dirac's delta function, and the last step follows from the definition of p k and the eigenvalues of matrix exponential.

To estimate φ 0 | e -ijτ H |φ 0 , we use the multi-level Monte Carlo method. Define a random variable J with support {-d, • • • , d} such that

where F := |j|≤d | F j |. Then, let Z := X J + iY J ∈ {±1 ± i}. Define an estimator G(x; J, Z) as follows:

where θ j is defined by F j = | F j |e iθ j . Then, we show that G(x; J, Z) is un-biased:

where the third step follows from Claim A.1. Moreover, the variance of G can be upperbounded by:

where the third step follows from |e i(θ J +Jx) | = 1, and the last step follows from X j , Y j ∈ {±1}.

Hence, we can take N s := 2F 2 σ 2 independent samples of (J, Z), denoted by {(J k , Z k )} k∈[Ns] and compute

Then, we have

The expected total evolution time is

By Lemma A.8, we know that

Thus, the number of samples is

And the expected total evolution time is

The lemma is then proved.

# A.2.2 Inverting the CDF

We first define the CDF inversion problem:

Definition A.3 (The CDF inversion problem). For 0 < δ < π/6, 0 < η < 1, find x ∈ (-π/3, π/3) such that Then, we give an algorithm that solves the CDF inversion problem.

Lemma A.5 (Inverting the CDF, Theorem 2 in [20]). There exists an algorithm that solves the CDF inversion problem (Definition A.3) with probability at least 1 -ν such that:

1. the number of independent samples of (J, Z) is

# the expected total evolution time is

)) • (log(ν -1 ) + log log(δ -1 ))

# the classical running time is

O η -2 log(δ -1 ) • (log(ν -1 ) + log log(δ -1 )) • (log(δ -1 ) + log log(δ -1 η -1 )) 2 .

Proof. For any x ∈ [-π/3, π/3], at least one of the following conditions will hold:

Suppose we have a sub-routine Certify(x, δ, η, {J k , Z k }) such that if C(x + δ) > η/2, it returns 0; otherwise, it returns 1. Then, we can solve the CDF inversion problem via the binary search (Algorithm 4). In Line 3, x L and x R always satisfy the following conditions:

which is guaranteed by Certify(x M , (2/3)δ, η, {J k , Z k }). Then, when the while-loop ends, we have x R -x L ≤ 2δ. Let x := (x L + x R )/2 be the output of Algorithm 4. Then, we get that

Algorithm 4 Inverting the CDF

x L ← -π/3, X R ← π/3

3:

if u = 0 then 7:

x R ← x M + (2/3)δ 8: else 9:

x L ← x M -(2/3)δ return (x L + x R )/2 13: end procedure And it is easy to see that Algorithm 4 will call Certify L := O(log(1/δ)) times. Then, by Lemma A.6 and union bound, Algorithm 4 will be correct with probability at least 1 -ν. We note that different runs of Certify can share a same set of samples {J k , Z k }, which does not affect the union bound. Hence, the number of samples and the total evolution time follows directly from Lemma A.6 and d = O(δ -1 log(δ -1 η -1 )). Proof. To decide which one of the conditions holds for x, we can estimate the ACDF C(x). If we take = η/8 in Lemma A.8, then the constructed ACDF satisfies

Then, we can distinguish C(x) > (5/8)η or C(x) < (7/8)η by the estimator in Lemma A.2.

In Algorithm 5, we compute the estimator G(x) N b times independently, where each time we use N s samples of (J, Z). We note that an error occurs when C(x) > (7/8)η but G(x) < (3/4)η, or C(x) < (5/8)η but G(x) > (3/4)η (when (5/8)η ≤ C(x) ≤ (7/8)η, any Algorithm 5 Distinguish the two cases in Eq. ( 97)

Lemma A.   

# A.2.3 Estimating the ground state energy

Corollary A.7 (Ground state energy estimation, Corollary 3 in [20]). If p 0 ≥ η for some known η, then with probability at least 1 -ν, the ground state energy λ 0 can be estimated within additive error , such that:

1. the number of times running the quantum circuit (Figure 1) is O(η -2 ).

2. the expected total evolution time is O( -1 η -2 ). -1 ).

# the classical running time is

Proof. Suppose we can solve the CDF inversion problem (Definition A.3) for δ = τ and η, i.e., we find an x such that

Since C(x) cannot take value between 0 and p 0 , we have

The costs of this algorithm follows from Lemma A.5.

# A.3 Low Fourier degree approximation of the Heaviside function

We construct the low degree approximation of the Heaviside function in this section. iv Lemma A.8 (Constructing low degree approximation of H). Let H(x) be the 2π-period Heaviside function (Eq. (87)). For any δ ∈ (0, π/2) such that tan(δ/2) ≤ 1 -1/ √ 2, there exists a d = O(δ -1 log(δ -1 -1 )) and a 2π-period function F d,δ (x) of the form:

Proof. We first construct F d,δ (x) by mollifying the Heaviside function with M d,δ (x) in Lemma A.10:

We can verify that F d,δ has Fourier degree at most d. It follows from the Chebyshev polynomial T d (x) is of degree d. Hence, the Fourier coefficients of M d,δ (x):

and H, we have

Then, we define

iv The construction in [20] is not enough to prove Lemma A.9 because the range of F d,δ is [-/2, 1 + ] while Lemma A.9 requires the range to be [0, 1]. We fix this issue in Lemma A.8.

where

It is easy see that

Then, we will show that taking d = O(δ -1 log(δ -1 -1 )) is enough to satisfy (1)-(3).

# Part (1):

We first compute the range of F d,δ (x):

where the second step follows from (2) in Lemma A.10. On the other hand,

holds, we will have

Therefore, for all x ∈ R,

where the first step follows from (2) in Lemma A.10, and the second step follows from the triangle inequality.

where the last step follows from Eq. (106). Therefore,

where the second step follows from the triangle inequality, the third step follows from Eq. (107). By scaling for , we can make the approximation error at most .

# Part (3): Since

where the second step follows from (2) in Lemma A.10 and the last step follows from Eq. ( 106).

For | H j |, if j = 0, we have

Hence, for j = 0,

Then, by definition, we get that

The proof of the lemma is completed.

The following lemma shows the approximation ratio of the ACDF C(x) constructed from the low degree approximated Heaviside function F (x) by Lemma A.8. Lemma A.9 (Approximation ratio of the ACDF). For any > 0, 0 < δ < π/6, let F (x) := F d,δ (x) constructed by Lemma A.8. Then, for any x ∈ [-π/3, π/3], the ACDF C(x) = (F * p)(x) satisfies: 

where the second step follows from Cauchy-Schwarz inequality, the forth step follows from Eq. (120), the fifth step follows from p(x) is a density function, the sixth step follows from H(y) = 1 and F L (y) ∈ [0, 1] for y ∈ [0, 2δ], the last step follows from C(x) is the CDF of p(x) in [-π, π]. Hence, we have

which proves the first inequality:

Similarly, we can define

which gives

The lemma is then proved.

# A.3.1 Technical lemma

Lemma A.10 (Mollifier, Lemma 5 in [20]). Define M d,δ (x) to be

where T d (x) is the d-th Chebyshev polynomial of the first kind, and

The proof can be found in Appendix A in [20], and we omit it here.

# B Technical details of the Hadamard test of block-encoded observable

In this section, we give detailed analysis of the Hadamard test for block-encodings which plays a crucial role in the proof of Theorem 6.1. We first note that the quantum state before the final measurements is as follows: Notice that to make the Hadamard test work, we need the coefficient 4e iθ abpq α to be a real or an imaginary number. Now, we show how to choose the parameters to minimize the variance. Without loss of generality, we may assume a, b ∈ (0, 1) such that a 2 + b 2 = 1 and use p, q to cancel the phase factor, i.e., e iθ abpq = Now, define the random variable as follows:

if the outcome is (1, 0 m ),

if the outcome is (0, 0 m ), 0 otherwise.

(154)

Then, we have

And we have

The second term is fixed for any parameters. And for the first term, we have

where the minimizer is at a := Oe -iHt 1 |φ 0 α+ Oe -iHt 1 |φ 0 . However, since we do not know the value of Oe -iHt 1 |φ 0 , there are two approaches to resolve this issue: (1) use another quantum circuit to estimate Oe -iHt 1 |φ 0 and then set the parameters; (2) just take a := 

where the last step follows from α ≥ 1 and Oe -iHt 1 |φ 0 2 ≤ 1. Therefore, we can reduce the estimator's variance by choosing a = 1 α . Moreover, if α is large, the new variance is about half of the variance using the Hadamard gate.

Similar strategy can also be used to reduce the variance of the random variable Y .

# A Ground State Energy Estimation

In this section, we review the techniques in [20], which proposed a hybrid quantum/classical algorithm for estimating the ground state energy of a Hamiltonian. Compared with the algorithms in previous works, the algorithm in [20] uses fewer quantum resources and does not need to access the block-encoding of the Hamiltonian.

First of all, they assumed that the given initial state |φ 0 iii has a nontrivial overlap with the ground state of H.

# A.1 Quantum part of the algorithm

Fix j ∈ Z. Suppose we want to estimate ( φ 0 | e -ijτ H |φ 0 ). Then, we set W = I and define a random variable X j as follows:

Since the state before the measurement is

iii In [20], they allowed the initial state to be a mixed state. For simplicity, we still denote it as |φ0 .

