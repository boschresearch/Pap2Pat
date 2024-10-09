# DESCRIPTION

## BACKGROUND

### Field of the Technology Disclosed

The field of the disclosed technology is that of estimating ground state properties for molecules and materials using quantum computers.

### Description of Related Art

The subject matter discussed in this section should not be assumed to be prior art merely because of its mention in this section. Similarly, any problems or shortcomings mentioned in this section or associated with the subject matter provided as background should not be assumed to have been previously recognized in the prior art. The subject matter in this section merely represents different approaches, which in and of themselves may also correspond to implementations of the claimed technology.

Quantum computers have been improving at a rapid rate, increasing the demand for quantum algorithms with high-impact use cases. As quantum technology is commercialized, quantum computing technology will make possible the development of new molecules and materials, including new drug discovery. One of the primary applications of quantum computing is the simulation of materials and molecules, which are inherently quantum mechanical. Quantum algorithm development for quantum chemistry and materials has been focused on ground state energy estimation. This problem is mathematically formulated as estimating the lowest eigenvalue of the Hamiltonian matrix that characterizes the physical system. One of the  first quantum chemistry applications of quantum computers was the use of quantum phase estimation for estimating the ground state energy of small molecules.

However, in characterizing materials or analyzing small molecules for drug discovery, one often needs to estimate properties of the ground state beyond the ground-state energy. These estimates include the calculation of transport properties, electric dipoles, and molecular forces.

These ground state properties depend on expectation values of observables (O) with respect to the ground state of a Hamiltonian (H). The problem of estimating such ground state properties has been found to be significantly more complex, in the theoretical sense, than the ground state energy estimation problem in general.

One drawback of current quantum circuits and algorithms is that such algorithms were developed for ideal quantum computers. These algorithms require high-depth quantum circuits, having many quantum gates in which errors propagate more readily, making them impractical for implementation on present-day quantum computers.

One near-term approach has been to use the variational quantum eigensolver algorithm (VQE) to provide a means for preparing an approximation to the ground state, from which each ground state property can be estimated iteratively. However, recent research suggests that VQE alone is not practical for solving problems of industrial relevance, such as solving quantum chemistry problems with small molecules. Also, current published information suggests that VQE may not outperform state-of-the-art classical methods and cannot guarantee the accuracy of the ground state estimation. Furthermore, training quantum circuits becomes difficult because of barren plateaus and other factors. The disclosed technology overcomes many of the drawbacks of the VQE methods and its variants for estimating ground state properties.

## SUMMARY

The disclosed technology uses a different approach for estimating ground state properties, which can be used with near-term quantum computers. The disclosed technology is more accurate and more reliable than known variational quantum eigensolver (VQE) methods.

In one aspect, the disclosed technology provides a quantum-classical algorithm that estimates ψ0|O|ψ0 with high accuracy and low circuit depth. The disclosed algorithm and quantum circuit can be used to reliably estimate ground state properties of a Hamiltonian using early or near-term fault-tolerant quantum computers and may be implemented with a low-depth quantum circuit.

In another aspect, the maximal Hamiltonian evolution time is Õ(Δ−1), where Δ is the spectral gap of H. The total evolution time is Õ(Δ−1ϵ−2η−2), where ϵ is the additive error and η≤|ϕ0|ψ0|2. The number of times needed to run the quantum circuit is O (ϵ−2η−2).

In another aspect, the algorithm works for any observable. Also, the quantum circuit is a variant of the Hadamard test circuit ψ0|O|ψ0

The disclosed technology is particularly useful for applications in quantum chemistry, characterizing small molecules, and materials research. In a further aspect, the technology may be used for estimating transport properties via an estimation of Green's functions. The disclosed technology may also be useful for extracting quantities from the solution of a linear system of equations.

In one embodiment of the disclosed technology, a system is provided for ground state property estimation (GSPE) using a hybrid quantum-classical (HQC) computer system. The computer system comprises classical computer elements and quantum computer elements. The classical computer elements include at least one processor and a non-transitory computer-readable memory, the non-transitory computer-readable memory storing computer instructions. The instructions, when executed by the classical processor, perform the method of estimating a ground state property of an observable (O). In one aspect, the classical computer elements also provide instructions and parameterized data to the quantum computer elements for executing algorithms and setting the initial quantum state of the quantum computer elements. The quantum computer elements may include a number of qubits and quantum gates configured in a quantum circuit. As part of the disclosed GSPE method, the quantum computer elements run a ground state property estimation algorithm. In another aspect, the classical computer elements further provide postprocessing of the data received from the quantum computer elements and provide the actual computation of the ground state properties based on a plurality of runs of the GSPE algorithm.

In another embodiment, a method is provided for estimating a ground state property (GSPE) of an observable (O). The method operates on a hybrid quantum classical (HQC). In one aspect, an initial quantum state is prepared with qubit registers and, ideally, one ancilla qubit. The ground state energy of a Hamiltonian (H) matrix is first estimated that characterizes a physical system. In another aspect, a plurality of samples are generated from a parameterized Hadamard test circuit. The sample outcomes are then evaluated. An estimate is made for the expectation value (p0) of the observable (O) with respect to the ground state energy. Following this, an estimate is made for the weighted expectation value p0O0. An estimate of the ground state property ψ0|O|ψ0 is then computed.

In one aspect of the disclosed technology, the physical system may be a molecule. In another aspect of the disclosed technology, the method may be used for estimating ground state properties for Green's functions. Further, the disclosed method may be used with Green's functions for computing electron transport in materials. In a still further aspect of the disclosed technology, the Green's functions may be used for computing electric dipoles of molecules. The disclosed method may also be used for computing the charge density of a molecule. Also, the charge density may be determined from the one-particle reduced density matrix. In another aspect, the physical system may be a material.

In a further aspect of the disclosed technology, the ground state property estimation may use a low-depth quantum circuit with reduced error rates. In one aspect, circuit depth may be determined as the inverse spectral gap and poly-logarithmic in the inverse target accuracy and inverse initial overlap, which will be described further on.

The disclosed method may also be used as a quantum linear system solver for extracting quantities from the solution of a linear system of equations. The efficiency may be augmented using the filter diagonalization method, as described.

The disclosed technology is applicable to estimating ground state properties using known fault-tolerant computers.

In another aspect, the disclosed technology may be combined with other methods, such as the variational quantum eigensolver VQE or the quantum approximate optimization algorithm (QAQO).

In another embodiment of the disclosed technology, an algorithm is presented for estimating the ground state energy property of an observable (O), wherein the algorithm (1) estimates ground state energy, (2) estimates the expectation value of the observable (O) with respect to the ground state PP0, and (3) estimates the weighted expectation values p0O0.

In another embodiment, a system is provided for estimating ground state properties of an observable (O) comprising a hybrid quantum-classical computer (HQC), the computer comprising a quantum computing component having a plurality of qubits, and a classical computing component. The classical computer includes at least one processor and a non-transitory computer-readable memory, the non-transitory computer-readable memory storing computer instructions. The computer instructions, when executed by the classical processor, perform a method for estimating a ground state property of an observable (O). The system performs a method of first initializing the quantum component to an initial state with qubit registers. Next, the method estimates the ground state energy of a Hamiltonian (H) matrix that characterizes a physical system. The system then generates a plurality of samples from a parameterized Hadamard test circuit. The sample outcomes are evaluated, and an expectation value (p0) of the observable (O) is estimated with respect to the ground state energy. Finally, a weighted expectation value p0O0 it is estimated and used to derive an estimate of the ground state property ψ0|O|ψ0.

In further aspects, the qubit registers may include a single ancilla bit. The physical system may be a molecule. The disclosed system may be used to compute the charge density of a molecule. Also, the charge density of the molecule may be determined using the one-particle reduced density matrix. Alternatively, the physical system may be a material.

## DETAILED DESCRIPTION

The following detailed description is made with reference to the figures. Sample implementations are described to illustrate the technology disclosed, not to limit its scope, which is defined by the claims. Those of ordinary skill in the art will recognize a variety of equivalent variations on the description that follows.

Quantum computers have been proven useful in solving difficult computational problems that are difficult for classical computers. One of the areas of current interest is solving problems related to ground state properties, such as those that would be involved in molecular structure and material properties. Although advances in quantum computers will continue to develop in coming years, there is a need to solve problems with currently available quantum computer architecture hardware.

In one aspect of the disclosed technology, an algorithm is provided for calculating the ground state energy and ground state properties using present generation quantum technology. The disclosed technology includes an algorithm that operates with low depth quantum circuits. The present technology improves on these earlier algorithms and quantum circuits by providing a  highly accurate, high probability, low circuit depth solution for estimating ground state properties, which can be implemented on current or near-term fault-tolerant quantum computers.

Overview

FIG. 4 is a simplified illustration of a system for ground state property estimation (GSPE) using a hybrid quantum-classical (HQC) computer system. The computer system comprises classical computer 410 elements and quantum computer 420 elements. The classical computer 410 elements include at least one processor and a non-transitory computer-readable memory, the non-transitory computer-readable memory storing computer instructions. The instructions, when executed by the classical processor, perform the method of estimating a ground state property of an observable (O). The classical computer 410 elements also provide instructions and parameterized data to the quantum computer 430 elements for executing algorithms and setting the initial quantum state of the quantum computer 420 elements. The quantum computer 420 elements may include a number of qubits and quantum gates configured in a quantum circuit. As part of the GSPE method, the quantum computer 420 elements run a ground state property estimation algorithm 430. The classical computer elements 410 further provide postprocessing 440 of the data received from the quantum computer 420 elements, providing the actual computation of the ground state properties based on a plurality of runs of the GSPE algorithm.

Referring now to FIG. 5, a block diagram is shown of the disclosed method 500 for estimating a ground state property (GSPE) of an observable (0), 510, according to one embodiment of the present invention. In step 520, on the quantum computer, an initial quantum state is prepared with qubit registers and one ancilla qubit. In step 530, the ground state energy of a Hamiltonian (H) matrix is estimated that characterizes a physical system. In step 540, samples are generated from me parameterized Hadamard test circuit. In step 550, the sample outcomes are evaluated. In step 560, an estimate is made for the expectation value (Po) of the observable (0) with respect to the ground state energy. In step 570, an estimate is made for the weighted expectation value Po 00. Finally, in step 580, an estimate of the ground state property ψ0|O|ψ0 is computed.

### Reduced Depth of The Quantum Circuit

The maximal evolution time, which is the maximal length of time used to perform coherent time evolution, can roughly determine the depth of the quantum circuit. Hence, the disclosed algorithm has a great advantage when the Hamiltonian's spectral gap is much larger than the estimation accuracy, making it easier to be implemented in the early fault-tolerant devices.

In one embodiment, a quantum-classical hybrid algorithm is disclosed for estimating properties of the ground state of a Hamiltonian, such that the quantum circuit depth is relatively small. Therefore, the algorithm has a significant advantage in high-accuracy estimation, and may be implemented in early fault-tolerant devices. In practice, the disclosed algorithm can solve many important tasks by combining with some initial state preparation methods (e.g., those used for VQE or QAOA).

### Example Embodiment of The Algorithm

Theorem 1. Given a Hamiltonian H and an observable O. Assume access to a unitary UI that prepares a state |φ0 that has non-trivial overlap with the ground state |ψ0 of H. then, there exists an algorithm to estimate ψ0|O|ψ0 with high accuracy and low-depth: the maximal Hamiltonian evolution time is (γ−1), where y is the spectral gap of H.

First, it can be noted that the maximal evolution time, which is the maximal length of time needed to perform coherent time evolution, may roughly determine the depth of the quantum circuit. The result achieves a nearly-linear dependence on γ−1 and only poly-logarithmic on the accuracy ϵ−1, which improves the Õ(ϵ−1) maximal evolution time in the ground state energy estimation algorithms. Second, the result does not violate the Heisenberg limit because the total evolution time still depends on poly (ϵ−1). Third, similar to almost all prior works in ground state preparation and energy estimation, it is assumed that the initial state has some nontrivial overlap with the ground state; otherwise, the problem will be computationally intractable. Last, the Hamiltonian may be considered a black-box, which is a common model in this field. To implement the algorithm, for sparse local Hamiltonian, current state-of-the-art Hamiltonian simulation methods may be used, wherein gate complexity depends linearly in the evolution time and logarithmically in the accuracy.

### Comparison to the Straightforward Method

The disclosed algorithm may be compared with the straightforward approach of GSPE that first prepares the ground state and then applies quantum phase estimation (QPE) to estimate the ground state property.

In the first step, to achieve an E-accuracy for the estimation, the ground state needs to be prepared with fidelity at least 1−ϵ, using known methods, which have circuit depth Õ(γ−1η−1) where η is the overlap between the initial state and the ground state.

In the second step, QPE requires circuit depth Õ(γ−1) for an E-accuracy estimation for the ground state property.

Therefore, this straightforward approach has circuit depth Õ(γ−1η−1+ϵ−1) while the algorithm has circuit depth Õ(γ−1). Furthermore, many (e.g., ω(1)) additional ancilla qubits are needed for preparing the ground state, where the disclosed algorithm requires only one ancilla qubit. The disclosed algorithm is advantageous, for example, when the Hamiltonian's spectral gap is much larger than the estimation accuracy, making it easier to be implemented in the early fault-tolerant devices.

### Ground State Property Estimation Problem

The ground state property estimation problem is defined as follows: Problem 1. Approximate simulation (APX-SIM). Given a k-local Hamiltonian H, an -local observable O, and real numbers a, b, ϵ such that b-a≥1/poly (n), and ϵ≥1/poly (n), for n the number of qubits the Hamiltonian H acts on, decide:

Yes case: H has a ground state |ψ0 such that (ψ0|O|ψ0≤a,

No case: for any state |ψ with ψ|H|ψ≤λ0+ϵ where λ0 is the ground state energy of H, it holds that ψ0|O|ψ0≥b.

APX-SIM is shown to be PQMA[|og]-complete even for 5-local Hamiltonian and 1-local observable, and also for some physics models like 2D Heisenberg model and 1D nearest-neighbor, translationally invariant model. However, these previous studies focused only on the decision version of this problem. For the purpose of designing efficient algorithms, the “search version” of APX-SIM is defined as follows:

Problem 2. Search version of APX-SIM. Given a Hamiltonian H, an (local) observable O, and ϵ∈ (0,1), with Ω(1) probability, estimate ψ0|O|ψ0 with an additive/multiplicative error at most ϵ.

In general, Problem 2 will not be more tractable than Problem 1. Thus, prior information about the Hamiltonian H and its ground state may be needed. Motivated by the widely used variational quantum eigensolver(VQE) and the Hartree-Fock method in quantum chemistry, it is often the case that for many real-world Hamiltonians, an initial state |Φ0) may be efficiently prepared that has a nontrivial overlap with the ground state. Moreover, the Hamiltonian H may be assumed to have a nontrivial spectral gap, wherein a large family of Hamiltonians satisfy this condition. With these assumptions, the ground state property estimation problem may be defined as follows:

Problem 3. Ground state property estimation (GSPE). Given a Hamiltonian H with spectral gap γ and ground state |ψ0), an observable O, a unitary UI such that it prepares an initial state |Φ0) with |Φ0|ψ0|2≥η, and ϵ∈(0,1), estimate ψ0|O|ψ0 with an additive/multiplicative error at most ϵ with Ω(1) probability.

Remark 4. When O=H, Problem 3 becomes the ground state energy estimation problem. Moreover, prior knowledge of a large overlap for the initial state is required for all quantum algorithms with provable performance guarantees. It is also worth noting that even with these assumptions, it is unlikely to use a purely classical algorithm to estimate the ground state energy or property to high precision (unless P=BQP).

A high-accuracy, early fault-tolerant quantum algorithm for GSPE is disclosed that satisfies the following properties:

The maximal evolution time depends logarithmically on the accuracy ϵ and overlap η. In addition to the Hamiltonian evolution and observable implementation, it only uses one additional ancilla qubit.

### An Overview of the Low-Depth Ground State Energy Estimation

Following is a brief overview of a low-depth ground state energy estimation algorithm implemented according to one embodiment of the present invention.

Theorem 1. Given a Hamiltonian H with eigenvalues in the interval [−π/3, π/3] and its ground state |ψ0 has energy λ0. An initial state |Φ0) can be prepared such that p0≥η for some known η, where p0:=|ϕ0|ψ0|2. Then, for any ϵ, v∈(0,1), there exists an algorithm that estimates λ0 with an additive error ϵ with probability 1-v, by running a parameterized quantum circuit with the maximum quantum evolution time Õ(ϵ−1) and the expected total quantum evolution time Õ(ϵ−1η−2). Example pseudocode of the algorithm is illustrated shown in FIG. 6 as Algorithm 1. The main technique of the algorithm is a classical post-processing procedure that extracts information from the Hadamard test circuit shown in FIG. 7. FIG. 7 shows a quantum circuit parameterized by j. H is the Hadamard gate and W is either I or a phase gate.

Let the initial state |Φ0 be expanded as |Φ0=Σkαk|ψk in the eigen-basis of H and let pk:=I αk|2 be the overlap with the k-th eigenstate. The overlaps p0, p1, . . . are considered as a density function:

\(\begin{matrix}
{{p(x)}:={\sum\limits_{k}{p_{k}{\delta\left( {x - \lambda_{k}} \right)}{\forall{x \in {\left\lbrack {{- \pi},\pi} \right\rbrack.}}}}}} & (1)
\end{matrix}\)

Then, the cumulative distribution function (CDF) C(x):=f−πxp (t)dt can be expressed as a convolution of p(x) and the 2π-periodic Heaviside function H(x), which is 0 in [(2k−1)π, 2kπ) and 1 in [2kπ, (2k+1)π) for any k∈Z. Thus, C(x) is also a periodic function, which makes it convenient to apply the Fourier approximation. Therefore, H(x) can be approximated by a low-Fourier degree function F(x) in the intervals [-π+δ, -δ] and [δ, π-delta]. Then, the approximated cumulative distribution function (ACDF) can be defined as {tilde over (C)}(x):=(F*p)(x) and proved that

C(x-δ)-η/8≤{tilde over (C)}(x)≤C(x+δ)+η/8∀x∈[-π/3,π/3,π/3].  (2)

Moreover, for each x:

\(\begin{matrix}
{\left. {{{{\overset{\sim}{C}(x)} = {\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}{e^{ijx} \cdot \left\langle \phi_{0} \right.}}}}❘}e^{- {ijH}}{❘\phi_{0}}} \right\rangle,} & (3)
\end{matrix}\)

where {circumflex over (F)}j is the Fourier coefficient of F(x). Note that  Φ0|e−ijH|Φ0 can be estimated via the parameterized quantum circuit (FIG. 1). Hence, ACDF may be estimated at every point in [-π/3,π/3]. Moreover, a multi-level Monte Carlo method can be applied to save the number of samples needed to achieve a high-accuracy estimation. Therefore, the ground state energy λ0 can be estimated by locating the first non-zero point of the CDF C(x), which is π/8-approximated by the ACDF {tilde over (C)}(x). Since p0≥η can be assumed, the approximation error and the estimation error of {tilde over (C)}(x) can be tolerated, and λ0 can be found via a robust binary search.

The maximal evolution time of this algorithm corresponds to the Fourier degree of F(x), which is Õ(ϵ−1) by the construction, making their algorithm suitable for early fault-tolerant quantum devices.

### Example Algorithm for Commutative Case

Following is a consideration of an easier case, where O is unitary and commutes with the Hamiltonian H, giving a two-step quantum-classical hybrid algorithm for Problem 3. More specifically, suppose the initial state can be expanded in the eigenbasis as follows: |ϕ0=Σkck|ψk with pk:=|ck|2. It is noted that {|ψk} is also an eigenbasis of O since O and H commute. In Step 1, the algorithm is run to estimate the ground state energy λ0 and the overlap between the initial state and the ground state p0. In Step 2, a similar CDF function is constructed for the density ΣkOkpkδ(x-λk), where Ok:=ψk|O|ψk. By evaluating the CDF at λ0, an estimate O0 may be obtained.

Step 1: Estimate the Initial Overlap. First, the procedure EstimateGSE (Algorithm 1) is run to estimate the ground state energy λ0 with an additive error ϵ. Let x* be the output to x* satisfy C(x*+τϵ)≥p0 and C(x*-τϵ)=0. However, p0 can only be extracted from ACDF {tilde over (C)}(x), which satisfies:

C(x-τϵ)-η/8≤{tilde over (C)}(x)≤C(x+τϵ)+η/8∀x∈[-π/3,π/3].  (4)

If [xτϵ,x+τϵ] contains a “jump” of C(x), i.e., an eigenvalue λk, then the approximation error of {tilde over (C)}(x) will be large.

Hence, a point x is “good” for λk if [x-τϵ,x+τϵ] is contained in [τλk,τλk+1). It is easy to see that {tilde over (C)}(x) will be an η/8-additive approximation of Σj≤kpk if x is good. The goal is to find an xgood that is good for λ0, and estimating {tilde over (C)}(xgood) gives the overlap p0. The following claim (proposition) provides a way to construct xgood using the spectral gap of H.

Claim 1. (Construct xgood) Let γ be the spectral gap of the Hamiltonian H. For any ϵ∈E (0,γ/4), x*+τγ/2 is good for λ0, where x* is the output of ESTIMATEGSE (ϵ,η) (Algorithm 1).

Proof x* satisfies:

\(\begin{matrix}
{{x^{*} - {\tau\epsilon}} < {\tau\lambda_{0}} \leq {x^{*} + {\tau{\epsilon.}}}} & (5)
\end{matrix}\)
\({Thus}:\)
\(\begin{matrix}
{{x^{*} + {\tau\gamma/2}} > {{\tau\lambda_{0}} - {\tau\epsilon} + {\tau\gamma/2}} > {{\tau\lambda_{0}} + {\tau{\epsilon.}}}} & (6)
\end{matrix}\)
\({And}{also}:\)
\(\begin{matrix}
{{x^{*} + {\tau\gamma/2}} < {{\tau\lambda_{0}} + {\tau\epsilon} + {\tau\gamma/2}}} & (7)
\end{matrix}\)
\(\begin{matrix}
{{\leq {{\tau\left( {\lambda_{1} - \gamma} \right)} + {\tau\epsilon} + {\tau\gamma/2}}} = {{{\tau\lambda_{1}} + {\tau\left( {\epsilon - {\gamma/2}} \right)}} < {{\tau\lambda_{1}} - {\tau{\epsilon.}}}}} & (8)
\end{matrix}\)

Therefore, x* is good for λ0.

If the ACDF's approximation error is chosen to be η/8, It may be directly changed to ϵη/8 without significantly changing the circuit depth, since by Lemma 8 the degree of F can only blowup by a log factor of ϵ.

Lemma 2. (Estimating the overlap) For any ϵ0,v∈(0,1), the overlap p0:=|ϕ0d|ψ0|2 can be estimated with multiplicative error 1±O(ϵ0) with probability 1−v by running the quantum circuit (FIG. 1) Õ(on0−2η−2) times with expected total evolution time Õ(γ−1ϵ−2η−2) and maximal evolution time O(γ−1).

Proof By claim 1, if the additive error of ground state energy λ0 is set to be O(γ), then it is possible to construct an xgood that is good for λ0. By Theorem 1, it can be done with maximum quantum evolution time Õ(γ−1) and the expected total quantum evolution time Õ(γ−1η−2) . It is necessary to take d=O(δ−1 log (δ−1ϵ0−1η−1)) (Line 1 in Algorithm 1) to make {tilde over (C)}(xgood) be an O (ϵ0η)-approximation of p0, where δ=τγ.

Next, an estimate is made of {tilde over (C)}(xgood) with additive error ηϵ with probability 1-v with an unbiased estimator:

(x;Z,J)=Zeiθ+jx  (9)

for {tilde over (C)}(x), where Z:=X+iY is measured from the Hadamard test, and/ is a random variable for the Hamiltonian evolution time sampled proportional to the Fourier weight of F, i.e., Pr[j=j]=|{circumflex over (F)}j|/for -d≤jeqd and :=Σ|j|≤d|{circumflex over (F)}j|.

It can be shown that (x;Z,J) has variance

\({O\left( {\log\limits^{2}(d)} \right)},\)

and one estimate can be obtained with evolution time Õ(τd/log (d)) in expectation. If (x;Z,J) is repeatedly sampled, and the mean is taken of the samples, then by Chebyshev's inequality, the sample complexity is Õ(ϵ0−2η−2v−2) to have an additive error O(ϵ0η) with probability 1-v.

Alternatively, the so-called “median-of-means” trick may be used to reduce the sample complexity. More specifically, let Ng=O(log (1/v)) and K=O(ϵ0−2). First, m=NgK samples (Z1, . . . , (Zm,Jm) are partitioned into Ng groups of size K. Then, for any i ∈[Ng], the i-th group mean is

\(\begin{matrix}
{\overset{\_}{G_{i}}:={\frac{1}{K}{\sum\limits_{j = 1}^{K}{{\overset{\_}{G}\left( {{x;Z_{{{({i - 1})}K} + j}},J_{{{({i - 1})}K} + j}} \right)}.}}}} & (10)
\end{matrix}\)

The final estimator is given by the median of these group means, i.e.,

(x):=median(1, . . . , N).  (11)

By Chernoff bound, it is easy to see that (x) has an additive error at most (ηϵ0) with probability 1-v. It will imply that multiplicative error is at most 1±O(ϵ0) since p0=θ(η). And the sample complexity of G(x) is Ō(ϵ0−2η−2). Hence, the expected total evolution time is Ō(γ−1). The same quantum circuit is run to estimate (x), the maximal evolution time is still Õ(γ−1).

Step 2: estimate the O-weighted CDF. To estimate the expectation value of O, consider the following quantum circuit, illustrated in FIG. 8. The quantum circuit in FIG. 8 is parameterized by j. H is the Hadamard gate and W is either I or a phase gate S. Define the random variables Xj,Yj be as follows: for W=I, Xj:=1 if the outcome is 0, and Xj:=−1 if the outcome is 1. For W=S,Yj:=−1 if the outcome is 0, and Yj:=1 if the outcome is 1. The following claim on the expectation of the random variables Xj,Yj:

Claim 3. (A variant of Hadamard test) For any j∈Z, the random variable Xj+iYj is an unbiased estimator for ϕ0Oe−ijτH|ϕ0, which can be expanded in the eigenbasis of H (which is also an eigenbasis of O):

\(\begin{matrix}
{{\left. {{{\left. {{\left\langle \phi_{0} \right.❘}Oe^{{- {ij}}\tau H}{❘\phi_{0}}} \right\rangle = {\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}e^{{- {ij}}\tau\lambda_{k}}\left\langle \psi_{k} \right.}}}❘}O{❘\psi_{k}^{\prime}}} \right\rangle = {\sum\limits_{k}{p_{k}O_{k}e^{{- {ij}}\tau\lambda_{k}}}}},} & (12)
\end{matrix}\)

where the last step follows from the simultaneous diagonalization of O and H, and Ok:=ψk|O|ψk. An assumption is made that |Ok|≤1 for any k∈.

The O-weighted “density function” for the observable is defined as follows:

\(\begin{matrix}
{{p_{O}(x)}:={\sum\limits_{k}{p_{k}O_{k}{{\delta\left( {x - {\tau\lambda_{k}}} \right)}.}}}} & (13)
\end{matrix}\)

Note that p0 (x) can be negative at some points.

Suppose the eigenvalues of τH is within [−π/3,π/3]. Then, O-weighted CDF and ACDF for p0 (x) are defined as follows:

C0(x):=(H*p0)(x),(x):=(F*p0)(x),  (14)

where H is the 2π-periodic Heaviside function and F=Fd,δ is the Fourier approximation of H constructed by Lemma 8. It is easy to verify that C0(x) equals to ΣkpkOk1x≥pOfor any x∈[−π/3,π/3].

The following lemma gives an unbiased estimator for the O-weighted ACDF.

Lemma 4. (Estimating the O-weighted ACDF) For any x∈[−π,π], there exists an unbiased estimator (x) for the O-weighted ACDF (x) with variance Õ(1). Furthermore, (x) runs the quantum circuit (FIG. 2) with expected total evolution time O(τd/log (d)), where d is the Fourier degree of F.

Proof (x) can be expanded in the following way:

\(\begin{matrix}
{(x) = {\left( {F*p_{O}} \right)(x)}} & (15)
\end{matrix}\)
\(\begin{matrix}
{\left. {{{{\int_{- \pi}^{\pi}{{F\left( {x - y} \right)}{p_{O}(y)}{dy}}} = {{\sum\limits_{{❘j❘} \leq d}{\int_{- \pi}^{\pi}{{\hat{F}}_{j}e^{{ij}({x - y})}{p_{O}(y)}{dy}}}} = {{\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}e^{ijx}{\int_{- \pi}^{\pi}{{p_{O}(y)}e^{- {ijy}}{dy}}}}} = {{\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}e^{ijx}{\sum\limits_{k}{p_{k}O_{k}e^{{- {ij}}\tau\lambda_{k}}}}}} = {\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}{e^{ijx} \cdot \left\langle \phi_{0} \right.}}}}}}}❘}Oe^{{- {ij}}\tau H}{❘\phi_{0}}} \right\rangle,} & (16)
\end{matrix}\)

where the third step follows from the Fourier expansion of F(x-y), the fifth step follows from the property of Dirac's delta function, and the last step follows from the definition of pk and the eigenvalues of matrix exponential.

Define an estimator G(x;J, Z) as follows:

G(x;J,Z):=⋅Zei(θ+J)  ,(17)

where θj is defined by {circumflex over (F)}j={circumflex over (F)}j|eiθ,Z=X+iY measured from the quantum circuit (FIG. 2) with parameter j=J, and =ρ|j|≤d|{circumflex over (F)}j|.

Then, it is shown that that G(x;J, Z) is un-biased:

\(\begin{matrix}
{{E\left\lbrack {G\left( {{x;J},Z} \right)} \right\rbrack} = {\sum\limits_{{❘j❘} \leq d}{E\left\lbrack {\left( {X_{j} + {iY}_{j}} \right)e^{i({\theta_{j} + {jx}})}{❘{\hat{F}}_{j}❘}} \right\rbrack}}} & (18)
\end{matrix}\)
\(\begin{matrix}
{{\left. {{{= {{\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}{e^{ijx} \cdot {E\left\lbrack {X_{j} + {iY}_{j}} \right\rbrack}}}} = {\sum\limits_{{❘j❘} \leq d}{{\hat{F}}_{j}{e^{ijx} \cdot \left\langle \phi_{0} \right.}}}}}❘}Oe^{{- {ij}}\tau H}{❘\phi_{0}}} \right\rangle = {\overset{\sim}{C}(x)}},} & (19)
\end{matrix}\)

where the third step follows from claim 3. Moreover, the variance of G can be upper-bounded by:

\(\begin{matrix}
{{{Var}\left\lbrack {G\left( {{x;J},Z} \right)} \right\rbrack} = {{E\left\lbrack {❘{G\left( {{x;J},Z} \right)}❘}^{2} \right\rbrack} - {❘{E\left\lbrack {G\left( {{x;J},Z} \right)} \right\rbrack}❘}^{2}}} & (20)
\end{matrix}\)
\(\begin{matrix}
{{\leq {E\left\lbrack {❘{G\left( {{x;J},Z} \right)}❘}^{2} \right\rbrack} \leq {2\mathcal{F}^{2}}},} & (21)
\end{matrix}\)

where the third step follows from |ei(θ+Jx)|=1, and the last step follows from Xj, Yj ∈{±1}. By Lemma 8, it is known that |{circumflex over (F)}j|=0(1//|j|). Hence, it follows that =Σ|j|≤dO (1/|j|)=O(log d). Thue, Var {G(x;J,Z)}=O(log(d)). The expected total evolution time is

{ 𝒯 t ⁢ o ⁢ t := E {[} ❘ "\textbackslash{[}LeftBracketingBar{]}" J ❘
"\textbackslash{[}RightBracketingBar{]}" {]} = τ ⁢ ∑ ❘
"\textbackslash{[}LeftBracketingBar{]}" j ❘
"\textbackslash{[}RightBracketingBar{]}" ≤ d ❘
"\textbackslash{[}LeftBracketingBar{]}" j ❘
"\textbackslash{[}RightBracketingBar{]}" · ❘
"\textbackslash{[}LeftBracketingBar{]}" F j ˆ ❘
"\textbackslash{[}RightBracketingBar{]}" = O ⁡ ( τ ⁢ d / log ⁡ ( d ) ) . (
22 ) }

The lemma is then proved. The following lemma shows that the O-weighted CDF C0 (x) can be approximated by the O-weighted ACDF C(x):

Lemma 5. Approximating the O-weighted CDF For any ϵ>0, 0<δ<π/6, let F(x):=Fd,δ(x) constructed by Lemma 8 with approximation error ηϵ/8. Then, for any x∈[-π/3,π/3], it holds that:

C0(x−δ)−ηϵ/8≤(x)≤C0(x+δ)+ηϵ/8.  (23)

The proof is very similar to Lemma 9, so it is omitted it here.

Assuming δ:=τγ/5 and let xgood:=x*+τγ/2. Then, by claim 1, it is known that xgood is good for δ0, i.e., [xgood−τγ, xgood+τγ]bset (τλ0,τλ1). Hence, {tilde over (C)}O(xgood) satisfies

|{tilde over (C)}0(xgood)−p0O0|≤ηϵ/8.  (24)

The following lemma shows how to estimate (xgood), which is very similar to Lemma 2.

Lemma 6. (Estimating p0O0) For any ϵ1, v ∈(0,1), p0O0 can be estimated with multiplicative error 1±0 (ϵ1) with probability 1−v by runs the quantum circuit (FIG. 1) Õ(ϵ1−2η−2) times with expected total evolution time Õ(γ−1ϵ1−2η−2) and maximal evolution time O(γ−1).

### Summarizing the Main Theorem

In this section, the components of the Main theorem are treated together, giving an algorithm for the ground state property estimation.

Theorem 7. (Ground state property estimation with commutative observable) Suppose p0≥η for some known η, and let γ>0 be the spectral gap of the Hamiltonian. Then, for any ϵ,v∈ (0,1), the ground state property ψ0|O|ψ0 can be estimated within additive error at most n with probability 1−v, such that:


- - 1. the number of times running the quantum circuits (FIGS. **1** and
    **2**) is Õ(ϵ⁻²η⁻²),
  - 2. the expected total evolution time is Õ(γ⁻¹ϵ⁻²η⁻²),
  - 3. the maximal evolution time is Õ(γ⁻¹).

Proof By Lemma 2, an estimate  for p0 is obtained with the guarantee that

|−p0|≤O(ηϵ0),  25)

where ϵ0 will be chosen shortly.

By Lemma 6, an estimate  for p0O0 is obtained with the guarantee that

|−p0O0|≤O(ηϵ1),  (26)

where ϵ1 will be chosen shortly.

### Thus

\(\begin{matrix}
{❘{\left. {\frac{\overset{\_}{p_{0}O_{0}}}{\overset{\_}{p_{0}}} - O_{0}} \right| = {❘\left. {\frac{\overset{\_}{p_{0}O_{0}}}{\overset{\_}{p_{0}}} - \frac{p_{0}O_{0}}{\overset{\_}{p_{0}}} + \frac{p_{0}O_{0}}{\overset{\_}{p_{0}}} - \frac{p_{0}O_{0}}{p_{0}}} \right|}}} & (27)
\end{matrix}\)
\(\begin{matrix}
{\leq {\frac{❘{\overset{\_}{p_{0}O_{0}} - {p_{0}O_{0}}}❘}{\overset{\_}{p_{0}}} + {{❘{p_{0}O_{0}}❘}{❘{\left. {\frac{1}{\overset{\_}{p_{0}}} - \frac{1}{p_{0}}} \middle| {\leq {\frac{O\left( {\eta\epsilon}_{1} \right)}{p_{0} - {O\left( {\eta\epsilon}_{0} \right)}} + {{❘{p_{0}O_{0}}❘}{❘{\frac{1}{p_{0} - {O\left( {\eta\epsilon}_{0} \right)}} - \frac{1}{p_{0}}}❘}}} \leq {\frac{O\left( {\eta\epsilon}_{1} \right)}{\eta - {O\left( {\eta\epsilon}_{0} \right)}} + {{❘{p_{0}O_{0}}❘}{❘{\frac{1}{p_{0} - {p_{0}{O\left( \epsilon_{0} \right)}}} - \frac{1}{p_{0}}}❘}}} \leq {{{O\left( \epsilon_{1} \right)}\left( {1 - {O\left( \epsilon_{0} \right)}} \right)} + {{❘O_{0}❘}\left( {1 + {O\left( \epsilon_{0} \right)} - 1} \right)}} \leq {O\left( {\epsilon_{0} + \epsilon_{1}} \right)}} \right.,}}}}} & (28)
\end{matrix}\)

where the second step follows from the triangle inequality, the third step follows from Eqs. (25) and (26), the third step follows from p0≥η, the fifth step follows from

\(\frac{1}{1 - x} \leq {1 + {O(x)}}\)

for x∈(0,1). Hence, by taking ϵ0=ϵ1=O(ϵ), an additive error of at most ϵ is achieved.

For the success probability, Eq.(25) can be made with probability 1−v/2 in Lemma 2 and Eq.(26) hold with probability 1−v/2 in Lemma 6. Then, by the union bound, a good estimate is achieved with probability at least 1− v. The computation costs follow directly from Lemma 2 and Lemma 6. And the proof of the theorem is then completed.

FIG. 9 illustrates the ground state property estimation algorithm (commutative case) in pseudocode form.

### Algorithm for General Unitary Observables

In this section, the following theorem for unitary observables in the general case is proved:

Theorem 1. (Ground state property estimation with general unitary observable) Suppose p1≥η for some known η and the spectral gap of the Hamiltonian H is at least γ. For any ϵ,v∈ (0,1), there exists an algorithm for estimating the ground state property ψ0|O|ψ0 within additive error at most E with probability at least 1−v, such that:


- - 1. the expected total evolution time is Õ(γ⁻¹ϵ⁻²η⁻²)
  - 2. the maximal evolution time is Õ(γ⁻¹).

In the following discussion, the 2-d O-weighted density function and CDF are first introduced, which extend the commuting observables to the general case. Then, it is shown how to combine them with the overlap estimation in Section 4.1 for proving Theorem 1.

2-d O-weighted density function and CDF

Let |ϕ0=Σkck|ψk where |ck|2=pk. In general, O and H may not commute. Hence, a more symmetric form of expectation: ϕ0|e−ijτHOe−ij′τH|ϕ0 is considered, which can be expanded in the eigenbasis of H as follows:

\(\begin{matrix}
{\left\langle {\phi_{0}{❘{e^{{- {ij}}\tau H}{Oe}^{{- {ij}^{\prime}}\tau H}}❘}\phi_{0}} \right\rangle = {{\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}e^{{- {ij}}{\tau\lambda}_{k}}e^{{- {ij}^{\prime}}{\tau\lambda}_{k^{\prime}}}\left\langle {\psi_{k}{❘O❘}\psi_{k^{\prime}}} \right\rangle}} = {\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}e^{{- {ij}}{\tau\lambda}_{k^{\prime}}}\left\langle {\psi_{k}{❘O❘}\psi_{k^{\prime}}} \right\rangle}}}} & (29)
\end{matrix}\)

Similar to the commutative case, a 2-d O-weighted density function is defined as:

\(\begin{matrix}
{{{p_{O,2}\left( {x,y} \right)}:={\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}O_{k,k^{\prime}}{\delta\left( {x - {\tau\lambda_{k}}} \right)}{\delta\left( {y - {\tau\lambda_{k^{\prime}}}} \right)}}}},} & (30)
\end{matrix}\)

where Ok,k′:=ψk|ψk′ Then, define the corresponding 2-d O-weighted CDF function as follows:

C0,2(x):=(H2*p0.2)(x,y),  (31)

where H2 (x,y):=H(x)⋅H(y), the 2-d 2π-periodic Heaviside function.

It is justified that C0,2 is indeed a CDF of p0,2 in [−π/3,π/3]:

\(\begin{matrix}
{{C_{2}\left( {x,y} \right)} = {\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{H_{2}\left( {{x - u},{y - v}} \right)}{p\left( {u,v} \right)}{dudv}}}}} & (32)
\end{matrix}\)
\(\begin{matrix}
{= {{\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}{O_{k,k^{\prime}} \cdot {\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{H_{2}\left( {{x - u},{y - v}} \right)}{\delta\left( {u - {\tau\lambda_{k}}} \right)}{\delta\left( {v - {\tau\lambda_{k^{\prime}}}} \right)}{dudv}}}}}}} = {{\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}{O_{k,k^{\prime}} \cdot {H\left( {x - {\tau\lambda_{k}}} \right)}}{H\left( {y - {\tau\lambda_{k^{\prime}}}} \right)}}} = {{\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k^{\prime}}{O_{k,k^{\prime}} \cdot 1_{{x \geq {\tau\lambda_{k}}},{y \geq {\tau\lambda_{k^{\prime}}}}}}}} = {\sum\limits_{\substack{{k:{{\tau\lambda_{k}} \leq x}},{(33)} \\ k^{\prime}:{{\tau\lambda}_{k^{\prime}} \leq y}}}{c_{k}^{*}c_{k^{\prime}}{O_{k,k^{\prime}}.}}}}}}} & (34)
\end{matrix}\)

Hence, the definition of C0,2 is reasonable.

Then, it is shown that C0,2 can be approximated similar to the 1-d case. Let F2(x) be the 2-d approximated Heaviside function, i.e.,

F2(x,y):=F(x)⋅F(y).  (35)

The 2-d O-weighted approximated CDF (ACDF) is defined to be

(x,y):=(F2*p0,2)(x,y).  (36)

The following lemma shows that  (x, y) is close to C0,2(x′,y′) for some (x′,y′) close to (x, y).

Lemma 2. Approximation ratio of the 2-d O-weighted ACDF For any ϵ>0,0<δπ/6, let F2(x,y):=Fd,δ(x)⋅Fd,δ(y) constructed by Lemma 8. Then, for any x, y ∈[−π/3,π/3], the 2-d O-weighted ACDF  (x,y)=(F2* p0,2) (x,y) satisfies:

C0,2(x−δ,y−δ)−2ϵ≥(x,y)≤C0,2(x+δ,y+δ)+2ϵ.  (37)

Proof By (2) in Lemma 8, it follows that:

|F(x)−H(x)|≤ϵ∀x ∈[−π+δ,−δ]∪[δ,π−δ],  (38)

which implies that for all x, y ∈[−π+δ, −δ]∪[δ,π−δ],

\(\begin{matrix}
{{{❘{{F_{2}\left( {x,y} \right)} - {H_{2}\left( {x,y} \right)}}❘} \leq {❘{{{F(x)}{F(y)}} - {{H(x)}{H(y)}}}❘}} = {{❘{{{F(x)}{F(y)}} - {{F(x)}{H(y)}} + {{F(x)}{H(y)}} - {{H(x)}{H(y)}}}❘} \leq {{{F(x)}{❘{{F(y)} - {H(y)}}❘}} + {{H(y)}{❘{{F(x)} - {H(x)}}❘}}} \leq {\left( {{F(x)} + {H(y)}} \right)\epsilon}}} & (39)
\end{matrix}\)
\(\begin{matrix}
{{\leq {2\epsilon}},} & (40)
\end{matrix}\)

where the last step follows from F(x)∈[0,1] by (1) in Lemma 8. Furthermore, for x ∈[−δ, δ], y ∈[−π+δ, −δ],

\(\begin{matrix}
{{{❘{{F_{2}\left( {x,y} \right)} - {H_{2}\left( {x,y} \right)}}❘} \leq {❘{{{F(x)}{F(y)}} - {{H(x)}{H(y)}}}❘}} = {❘{{F(x)}{F(y)}}❘}} & (41)
\end{matrix}\)
\(\begin{matrix}
{{H(y)} = {0 \leq {F(y)}}} & (42)
\end{matrix}\)
\(\begin{matrix}
{\leq {\epsilon.}} & (43)
\end{matrix}\)

Similarly, for x∈[−π+δ, −δ], y∈[−δ, δ],

|F2(x,y)−H2(x,y)|≤ϵ.  (44)

Define FL,2:=F2(x−δ,y−δ) such that

|FL,2(x)−H2(x)|≤2ϵ∀(x, y) ∈[−π+2δ,0]×[−π+2δ, π]∪[−π+2δ,π]×[−π+2δ, 0]∪[2δ,π]×[2δ,π].  (45).

For  (x, y):=(FL,2*p0,2)(x, y), if follows that  (x, y)= (x−δ,y−δ). Let p2:=p0,2. Then, for any x, y ∈[−π/3,π/3], it follows that

\(\begin{matrix}
{{❘{{C_{O,2}\left( {x,y} \right)} - \left( {x,y} \right)}❘} = {❘{\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{p_{2}\left( {{x - u},{y - v}} \right)}\left( {{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}} \right){dudv}}}}❘}} & (46)
\end{matrix}\)
\(\begin{matrix}
{{{{\left. {{\left. {{\left. {{\left. {{\leq {\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{p_{2}\left( {{x - u},{y - v}} \right)}{❘{{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}}❘}{dudv}}}}} = {\left( {\int_{- \pi}^{0}{\int_{- \pi}^{\pi}{+ {\int_{0}^{\pi}{\int_{- \pi}^{0}{+ {\int_{2\delta}^{\pi}\int_{2\delta}^{\pi}}}}}}}} \right){p_{2}\left( {{x - u},{y - v}} \right)}}} \right){❘{{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}}❘}{dudv}} + {\left( {\int_{0}^{2\delta}{\int_{0}^{\pi}{+ {\int_{0}^{\pi}{\int_{0}^{2\delta}{- {\int_{0}^{2\delta}\int_{0}^{2\delta}}}}}}}} \right){p_{2}\left( {{x - u},{y - v}} \right)}}} \right){❘{{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}}❘}{dudv}} \leq {{2{\epsilon \cdot \left( {\int_{- \pi}^{0}{\int_{- \pi}^{\pi}{+ {\int_{0}^{\pi}{\int_{- \pi}^{0}{+ {\int_{2\delta}^{\pi}\int_{2\delta}^{\pi}}}}}}}} \right)}{p_{2}\left( {{x - u},{y - v}} \right)}{dudv}} + {\left( {\int_{0}^{2\delta}{\int_{0}^{\pi}{+ {\int_{0}^{\pi}{\int_{0}^{2\delta}{- {\int_{0}^{2\delta}\int_{0}^{2\delta}}}}}}}} \right){p_{2}\left( {{x - u},{y - v}} \right)}}}} \right){❘{{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}}❘}{dudv}} \leq {{2\epsilon} + {\left( {\int_{0}^{2\delta}{\int_{0}^{\pi}{+ {\int_{0}^{\pi}{\int_{0}^{2\delta}{- {\int_{0}^{2\delta}\int_{0}^{2\delta}}}}}}}} \right){p_{2}\left( {{x - u},{y - v}} \right)}}}} \right){❘{{H_{2}\left( {u,v} \right)} - {F_{L,2}\left( {u,v} \right)}}❘}{dudv}} \leq {{2\text{⁠}\epsilon} + {\left( {\int_{0}^{2\delta}{\int_{0}^{\pi}{+ {\int_{0}^{\pi}{\int_{0}^{2\delta}{- {\int_{0}^{2\delta}\int_{0}^{2\delta}}}}}}}} \right)\text{⁠}{p_{2}\left( {{x - u},{y - v}} \right)}\text{⁠}{dudv}}}} = {{{2\epsilon} + {\left( {\int_{x - {2\delta}}^{x}{\int_{y - \pi}^{y}{+ {\int_{x - \pi}^{x}{\int_{y - {2\delta}}^{y}{- {\int_{x - {2\delta}}^{x}\int_{y - {2\delta}}^{y}}}}}}}} \right)\text{⁠}{p_{2}\left( {u,v} \right)}{dudv}}} = {{2\epsilon} + {C_{O,2}\left( {x,y} \right)} - {C_{O,2}\left( {{x - {2\delta}},{y - {2\delta}}} \right)}}}},} & (47)
\end{matrix}\)

where the second step follows from Cauchy-Schwarz inequality, the third step follows from partitioning the integration region, the forth step follows from Eq. (45) and the fact that p(x, y) is supported in

\({\left\lbrack {{- \frac{\pi}{3}},\frac{\pi}{3}} \right\rbrack \times \left\lbrack {{- \frac{\pi}{3}},\frac{\pi}{3}} \right\rbrack{and}\delta} < \frac{\pi}{6}\)

(see FIG. 3 (a)), the fifth step follows from p0,2(x) is a density function, the last step follows from C0,2(x) is the CDF of p0,2(x) in [−π, π]×[−π, π] and

\(x,{y \in {\left\lbrack {{- \frac{\pi}{3}},\frac{\pi}{3}} \right\rbrack.}}\)

FIG. 10(a) shows the integral region for Equation 44, where the integral in regions 1-6 can be upper bounded by Equation 43. FIG. 10(b) shows the integral region for equation 45(a) is the integral region for Eq. (46), where the integral in regions 1-6 can be upper bounded by Eq. (45).

Hence, it follows that:

\(\begin{matrix}
{{{\left( {x,y} \right) \geq {{C_{O,2}\left( {x,y} \right)} - \left( {{2\epsilon} + {C_{O,2}\left( {x,y} \right)} - {C_{O,2}\left( {{x - {2\delta}},{y - {2\delta}}} \right)}} \right)}} = {{C_{O,2}\left( {{x - {2\delta}},{y - {2\delta}}} \right)} - {2\epsilon}}},} & (48)
\end{matrix}\)

which proves the first inequality:

(x−δ,y−δ)≥C0,2(x−2δ, y−2δ)−2ϵ.  (49)

Similarly, it is defined that FR,2:=F2(x+δ, y+δ) and  (x, y):=(FR,2*p2)(x,y), and can be shown that

|C0,2(x,y)− (x,y)|≤2ϵ+C0,2(x+2δ,y+2δ)−C0,2(x,y)  (50)

which gives

(x+δ,y+δ)≤C0,2(x+2δ,y+2δ)+2ϵ.  (51)

The lemma is then proved.

Estimating the 2-d ACDF. The parameterized quantum circuit, shown in FIG. 11, is used to estimate the 2-d O-weighted ACDF  (x, y). In FIG. 11, the quantum circuit is parameterized by t1, t2. H is the Hadamard gate and W is either I or a phase gate S.

Lemma 3. (Estimate 2-d O-weighted ACDF) For any x,y ∈[−π/3,π3], for any ϵ,v ∈(0,1),  (x, y) may be estimated with additive error ηϵ with probability 1−v by running the quantum circuit (FIG. 4) O(ϵ−2η−2 log (1/v)) times with maximal evolution time Õ(γ−1) and total expected evolution time Õ(γ−1ϵ−1η−1).

Proof  (x, y) can be expanded in the following way:

\(\begin{matrix}
{{{\overset{\sim}{C_{O,2}}\left( {x,y} \right)} = {{\left( {F_{2}*p_{2}} \right)\left( {x,y} \right)} = {{\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{F_{2}\left( {{x - u},{y - v}} \right)}{p_{2}\left( {u,v} \right)}{dudv}}}} = {{\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}e^{{ij}({x - u})}e^{{ij}^{\prime}({y - v})}{p_{2}\left( {u,v} \right)}{dudv}}}}} = {{\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}e^{i({{jx} + {j^{\prime}y}})}{\int_{- \pi}^{\pi}{\int_{- \pi}^{\pi}{{p_{2}\left( {u,v} \right)}e^{{- i}ju}e^{{- i}j^{\prime}v}{dudv}}}}}} = {{\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}e^{i({{jx} + {j^{\prime}y}})}{\sum\limits_{k,k^{\prime}}{c_{k}^{*}c_{k}O_{k,k^{\prime}}e^{{- i}j\tau\lambda_{k}}e^{{- i}j^{\prime}\tau\lambda_{k^{\prime}}}}}}} = {\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}{e^{i({{jx} + {j^{\prime}y}})} \cdot \left\langle {\phi_{0}{❘{e^{{- i}j\tau H}{Oe}^{{- i}j^{\prime}\tau H}}❘}\phi_{0}} \right\rangle}}}}}}}}},} & (52)
\end{matrix}\)

To estimate  ϕ0|e−ijτH Oe−ij′τH|ϕ0, the multi-level Monte Carlo method is used and define random variables J, J′ with support {−d, . . . , d} such that

\(\begin{matrix}
{{{P{r\left\lbrack {{J = j},{J^{\prime} = j^{\prime}}} \right\rbrack}} = \frac{{❘\overset{\hat{}}{F_{j}}❘}{❘{\overset{\hat{}}{F}}_{j^{\prime}}❘}}{\mathcal{F}^{2}}},} & (54)
\end{matrix}\)

where  :=Σ|j|≤d|{circumflex over (F)}j|. Then, let Z:=Xj,j′+iYj,j′∈{±1+i}. Define an estimator  (x;j,j′, Z) as follows:

(x,y; j,Z):= 2⋅Zei(θ+jx)ei(θ+j′y),  (55)

where θj is defined by {circumflex over (F)}j=|{circumflex over (F)}j|eiθ, and similar definition for θj′. Then, it is shown that  (x, y; j, Z) is un-biased:

\(\begin{matrix}
{{E\left\lbrack {\overset{\_}{G_{2}}\left( {x,{y;J},J^{\prime},Z} \right)} \right\rbrack} = {{\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{E\left\lbrack {\left( {X_{j,j^{\prime}} + {iY}_{j,j^{\prime}}} \right)e^{i({\theta_{j} + {jx}})}e^{i({{\theta_{j}}^{\prime} + {j^{\prime}y}})}{❘\overset{\hat{}}{F_{j}}❘}{❘{\overset{\hat{}}{F}}_{j^{\prime}}❘}} \right\rbrack}} = {{\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}e^{ijx}{e^{ij^{\prime}y} \cdot {E\left\lbrack {X_{j,j^{\prime}} + {iY_{j,j^{\prime}}}} \right\rbrack}}}} = {\sum\limits_{{{❘j❘} \leq d},{{❘j^{\prime}❘} \leq d}}{\overset{\hat{}}{F_{j}}{\overset{\hat{}}{F}}_{j^{\prime}}e^{ijx}{e^{ij^{\prime}y} \cdot \left\langle {\phi_{0}{❘{e^{{- i}j\tau H}{Oe}^{{- i}j^{\prime}\tau H}}❘}\phi_{0}} \right\rangle}}}}}} & (56)
\end{matrix}\)
\(\begin{matrix}
{{= \left( {x,y} \right)},} & (57)
\end{matrix}\)

where the third step follows from claim 1. Moreover, the variance of  can be upper-bounded by:

\(\begin{matrix}
{{{Var}\left\lbrack {\overset{\_}{G_{2}}\left( {x,{y;J},J^{\prime},Z} \right)} \right\rbrack} = \ {{{{E\left\lbrack {❘{\overset{\_}{G_{2}}\left( {x,{y;J},J^{\prime},Z} \right)}❘}^{2} \right\rbrack} - {❘{E\left\lbrack {\overset{\_}{G_{2}}\left( {x,{y;J},J^{\prime},Z} \right)} \right\rbrack}❘}^{2}} \leq \ {E\left\lbrack {❘{\overset{\_}{G_{2}}\left( {x,{y;J},J^{\prime},Z} \right)}❘}^{2} \right\rbrack}} = {\mathcal{F}^{4} \cdot {E\left\lbrack {❘{X_{J,J^{\prime}} + {iY}_{J,J^{\prime}}}❘}^{2} \right\rbrack}}}} & (58)
\end{matrix}\)
\(\begin{matrix}
{{= {2\mathcal{F}^{4}}},} & (59)
\end{matrix}\)

where the third step follows from |ei(θ+jx)|=|ei(θ+j′y)|=1, and the last step follows from Xj,j′, Yj,j′∈{±1}.

By Lemma 8, it is known that  =Õ(1). Hence, it follows for all x, y ∈[−π/3,π/3],

E[ (x, y)]= (x, y), and Var [ (x, y)]=Ō(1).  (60)

Then, using median-of-means estimator, an E-additive error estimate may be obtained of  (x, y) with probability 1−v using O(ϵ−2η−2 log (1/v)) samples. The maximal evolution time is 2d=Õ(γ−1). And the expected evolution time for one trial is

\(\begin{matrix}
{{\tau{\sum\limits_{{❘j❘},{{❘j^{\prime}❘} \leq d}}{\left( {j + j^{\prime}} \right)\frac{{❘\overset{\hat{}}{F_{j}}❘}{❘{\overset{\hat{}}{F}}_{j^{\prime}}❘}}{\mathcal{F}^{2}}}}} = {{2\tau{\sum\limits_{{❘j❘} \leq d}{j\frac{❘\overset{\hat{}}{F_{j}}❘}{\mathcal{F}}}}} = {{O\left( {\tau d/{\log(d)}} \right)}.}}} & (61)
\end{matrix}\)

Hence, the total expected evolution time is Õ(γ−1ϵ−2η−2). The lemma is then proved.

FIG. 12(a) shows a point that is good for λ0, where the interval enclosed by parentheses is the approximation region such that  (xgood) is close to C(x) for some x in this interval. FIG. 12(b) shows a good point in the 2-d case, wherein the larger square, the 2-d O-weighted CDF C0,2 takes the same value C0,2(λ0,λO). The smaller square with hatching defines the approximation region of (xgood, ygood) such that  (xgood, yfgood) is close to some C0,2(x, y) in this region. Similar to the 1-d case, a “good” point for (λ0,λ0) may be constructed via the following claim.

Claim 4. Construct 2-d good point Let y be the spectral gap of the Hamiltonian H. Let xgood:=x*+τγ/2 where x* is the output of EstimateGSE(γ/8, τ, η, v/10) (Algorithm 1). Then, (xgood, xmathsfgood) is good for (λ0,λ0). In particular, for any ϵ∈(0,1), if the approximation error of F(x) is set to be ϵη, then

(xgood,xgood)−C0,2(λ0,2,λ0)|≤2ϵη.  (62)

Proof By claim 1, it is known that Xgood is good for λ0, i.e., [xgood−δ, xgood+δ] is contained in [λ0,λ1). It also holds in the 2-d case for (xgood, xgood). Then, by Lemma 3:

\(\begin{matrix}
{{{C_{O,2}\left( {{x_{good} - \delta},{x_{good} - \delta}} \right)} - {2{\epsilon\eta}}} \leq \left( {x_{g{ood}},x_{good}} \right) \leq {{C_{O,2}\left( {{x_{good} + \delta},{x_{good} + \delta}} \right)} + {2{{\epsilon\eta}.}}}} & (63)
\end{matrix}\)

The claim then follows from C0,2(x, y)=C0,2(λ0,λ0) for any (x, y) ∈[λ0,λ1)×[λ0,λ1).

Ground State Property Estimation (General Case)

The main algorithm for the ground state property estimation will first estimate the ground state energy λ0 and the overlap l0. Then, by Lemma 3 and claim 4, the weighted expectation p0O0 may also be estimated. Hence, an estimate for O0= ψ0|O|ψ0 is obtained.

FIG. 13 illustrates the algorithm for ground state property estimation (general case) for Algorithm 3 in pseudocode.

Proof of Theorem 1. The estimation error of Algorithm 3 is first analyzed. By Lemma 2,  has additive error at most O (ηϵ). By Lemma 3 and claim 4,  has additive error at most O(ηϵ). Then, a similar error propagation analysis in Theorem 7 yields

\(\begin{matrix}
{{❘{\overset{\_}{\frac{p_{0}⁢O_{0}}{\overset{\_}{p_{0}}}} - O_{0}}❘} \leq {{O(\epsilon)}.}} & (64)
\end{matrix}\)

To maximize probability of success, Algorithm 3 has three components: estimate ground state energy, estimate p0, and estimate p0O0. Using this choice of parameters, each of them will fail with probability at most v/3. Hence, Algorithm 3 will succeed with probability at least 1−v. The maximal evolution time and the total expected evolution time follows from Theorem 1, Lemma 2, and Lemma 3.

Handling Non-Unitary Observables. Algorithm 3 works only for unitary observables because it needs to use the parameterized quantum circuit in FIG. 14 to estimate  ϕ0|e−itHOe−itH|ϕ0 for certain t1, t2 ∈, in which controlled-O must be a unitary operation. In this section, it is shown that under reasonable assumptions the disclosed algorithm can be modified to estimate the ground state property  ψ0|O|ψ0 where 0 is a general observable.

There may be a question as to why this method is necessary, since O may be decomposed into a linear combination of Pauli strings O=Σ{right arrow over (s)}w{right arrow over (s)}P{right arrow over (s)}, and Algorithm 3 used to estimate each term μψ0|P{right arrow over (s)}|ψ0 individually, and return Σ{right arrow over (s)}μ{right arrow over (s)} as the result. While this strategy works in principle, it may lack the efficiency to be practical, depending ending on the weights w{right arrow over (s)}'s of Pauli strings in the linear expansion of O.

Alternatively, the issue of Algorithm 3 may be fixed by designing a procedure for estimating  ϕ0|e−itHOe−itH|ϕ0 for arbitrary non-unitary O. Such quantities are utilized in the same way as before. This approach has been followed and found that it is possible when there is a block-encoding of O. Namely, suppose O is an n-qubit observable with ∥O∥≤1 and U is an (n+m)-qubit unitary operator such that

( 0m|⊗I)U(|0m ⊗I)=α−1O  (65)

for some α≥∥O∥. Then a Hadamard test for U may be performed to estimate  ϕo|e−it HOe−itH|ϕ0)  for arbitrary t1, t2 ∈. The main theorem of this section is stated below:

Theorem 1. Ground state property estimation with block-encoded observable. Suppose p0≥η for some known η and the spectral gap of the Hamiltonian H is at least γ. Assuming an access to the α-block-encoding of the observable O. For any ϵ,v ∈ (0,1), there exists an algorithm for estimating the ground state property  ψ0O|ψ0 within additive error at most ϵ with probability at least 1−v, such that:


- - 1. the expected total evolution time is Õ(γ⁻¹ϵ⁻²η⁻²α²),,
  - 2. the maximal evolution time is Õ(γ⁻¹).

Proof sketch of Theorem 1. The algorithm for handling non-unitary block-encoded observables is quite similar to Algorithm 5.3 for handling unitary observables, except that it relies on a different procedure to estimate  ϕ0|e−itHOe−itH|ϕ0 for arbitrary t1, t2 ∈. The procedure is described as follows:

Let C−V:=|00|⊗I+|11|⊗V be the controlled-V operation for arbitrary unitary operator V. Let |ϕ0) be an arbitrary n-qubit state.

Consider the following procedure as illustrated in FIG. 15. Quantum circuit parameterized by t1, t2. H is the Hadamard gate and W is either I or a phase gate S. U is the block-encoding of the non-unitary observable O.


- - 1. Prepare the state \|0
    \|0^(m)
    \|ϕ₀
    .
  - 2. Apply a Hadamard gate on the first register.
  - 3. Apply a C-e^(−iHt1) on the first and third registers.
  - 4. Apply C-U on the current state, obtaining

\(\begin{matrix}
{\left. \left. {\left. {\left. {\left. {\left. {\left. {\frac{1}{\sqrt{2}}\left( {❘0} \right.} \right\rangle{❘0^{m}}} \right\rangle{❘\phi_{0}}} \right\rangle + {❘1}} \right\rangle U{❘0^{m}}} \right\rangle e^{{- i}Ht_{1}}{❘\phi_{0}}} \right\rangle \right).} & (66)
\end{matrix}\)


- - 5.
  - 6. Measure the second register in the standard basis. If the outcome
    is not 0^(m), then this procedure fails; otherwise, continue. The
    probability of this step succeeding is

\(\begin{matrix}
{{p_{succ} = \frac{1 + {\alpha^{- 2}\left\langle {\phi_{0}{❘{e^{iHt_{1}}O^{2}e^{{- i}Ht_{1}}}❘}\phi_{0}} \right\rangle}}{2}},} & (67)
\end{matrix}\)


- - 7. and when this event happens, the state becomes

\(\begin{matrix}
{\left. \left. {\left. {\left. {\left. {\frac{1}{\sqrt{2p_{succ}}}\left\lbrack {❘0} \right.} \right\rangle{❘\phi_{0}}} \right\rangle + {\alpha^{- 1}{❘1}}} \right\rangle{Oe}^{{- i}Ht_{1}}{❘\phi_{0}}} \right\rangle \right\rbrack.} & (68)
\end{matrix}\)


- - 8.
  - 9. Apply a C-e^(−-iHt2) on the first and third registers. The state
    becomes

\(\begin{matrix}
{\left. \left. {\left. {\left. {\left. {\frac{1}{\sqrt{2p_{succ}}}\left\lbrack {❘0} \right.} \right\rangle{❘\phi_{0}}} \right\rangle + {\alpha^{- 1}{❘1}}} \right\rangle e^{{- i}Ht_{2}}Oe^{- {iHt}_{1}}{❘\phi_{0}}} \right\rangle \right\rbrack.} & (69)
\end{matrix}\)


- - 10.
  - 11. Apply W=I or phase gate S on the first register.
  - 12. Apply a Hadamard gate on the first register.
  - 13. Measure the first register in the standard basis. Then if W=I,
    the (conditional) probability of getting outcome 0 is

\(\begin{matrix}
{{{{\mathbb{P}}\left\lbrack {0❘{succ}} \right\rbrack} = \frac{p_{succ} + {\alpha^{- 1}{{Re}\left\lbrack \left\langle {\phi_{0}{❘{e^{{- i}Ht_{2}}Oe^{{- i}Ht_{1}}{❘\phi_{0}}}}} \right\rangle \right\rbrack}}}{2p_{succ}}};} & (70)
\end{matrix}\)


- - 14. if W=S, this probability is
  - 15.

\(\begin{matrix}
{{{\mathbb{P}}\left\lbrack {0❘{succ}} \right\rbrack} = {\frac{p_{succ} - {\alpha^{- 1}{{Im}\left\lbrack \left\langle {\phi_{0}{❘{e^{{- i}Ht_{2}}Oe^{{- i}Ht_{1}}{❘\phi_{0}}}}} \right\rangle \right\rbrack}}}{2p_{succ}}.}} & (71)
\end{matrix}\)

Two random variables X and Y are defined as follows. First, the above procedure is run with W=I in step 7. If step 5 fails, X=0; otherwise, if the measurement outcome is 0 or 1 in step 9, then X=α or −α, respectively. One can show that X is an unbiased estimator of Re [ ϕ0|e−iEtOe−iHt|ϕ0], i.e.

[X]=Re [ϕ0|e−iHTOe−iHt|ϕ0].  (72)

Y is defined similarly. The above procedure is run with W=S in step 7. If step 5 fails, Y=0; otherwise, if the measurement outcome is 1 or 0 in step 9, then Y=α or −α, respectively. Then Y is an unbiased estimator of Im [ϕ0e−iHtOe−iHt|ϕ0], i.e.

[Y]=Im[ϕ0|e−iHTOe−iHt|ϕ0].  (73)

It follows that Z:=X+iY is an unbiased estimator of ϕ0|e−iHtOe−iHt|ϕ0,i.e.

[Z]= ϕ0|e−iHtOe−iHt1|ϕ0.  (74)

Note that |Z|2=|X|2+|Y|2≤2a2 with certainty.

Equipped with the above method for estimating  ϕ0|e−iHtOe−iHt|ϕ0 for arbitrary t1, t2 ∈, the same strategy can be used as in Lemma 3 to estimate  (x, y). The other components of Algorithm 3 remain intact. The analysis of this modified algorithm is almost the same as before, except now:

Var| (x,y)|={tilde over (O)}(α2).  75)

As a consequence, compared to Theorem 1, the total evolution time of this modified algorithm is larger by a factor of O (a2), while its maximal evolution time is of the same order. W

**Applications**

In this section, example applications of the disclosed ground state property estimation algorithm are discussed. To define an application of the ground state property estimation algorithm, a Hamiltonian of interest H and an observable of interest O must be specified. An example application used in quantum chemistry and materials is the Green's function, where O=αi(z-(H−E0)−1)αj†.

The following two sections are from the fields of quantum chemistry and materials as well as an example of a linear algebraic subroutine.

Charge density. The primary application of the technique is the estimation of ground state properties of physical systems. The following describes how to compute the charge density of a molecule, which can be used to compute properties like electric dipole moments of a molecule. From a second-quantized representation of the electronic system (assuming fixed positions of the nuclear positions), the charge density is determined from the one-particle reduced density matrix as,

\(\begin{matrix}
{{{\rho\left( \overset{\rightarrow}{r} \right)} = {{- e}{\sum\limits_{p,q}{D_{p,q}{\phi_{p}\left( \overset{\rightarrow}{r} \right)}{\phi_{q}\left( \overset{\rightarrow}{r} \right)}}}}},} & (76)
\end{matrix}\)

where e is the electric constant, Dpq is the one-electron reduced density matrix (1RDM) of the ground state, and ϕq({right arrow over (τ)}) are the basis wave functions chosen for the second-quantized representation of the electronic system. The 1RDM of the ground state is a matrix of properties of the ground state with each entry defined as

Dp,q= ψ0|αp†αq|ψ0,  (77)

where αp are annihilation operators. The operators involved in the 1RDM can each be expressed as a linear combination of unitary operators using the Majorana representation αp=½(γ2p+iγ2p+1), where the γk are hermitian and unitary,

Dp,q=¼ ( ψ0|γ2pγ2q|ψ0-iψ0|γ2p+1γ2q|ψ0+iψ0|γ2pγ2q+1|ψ0+ψ0|γ2p+1γ2q+1|ψ0 ).  (78)

Accordingly, the prior method may be used to estimate each entry of the 1RDM and then obtain the charge density function of the ground state. As a point of comparison, alternatively, the variational quantum eigensolver algorithm is used to prepare an approximation to the ground state and then directly estimate each of the Pauli expectation values. However, there is no guarantee on whether a target accuracy for the ground state approximation can be achieved. The disclosed methods may be used to ensure a target accuracy in the estimation regardless of the quality of ground state approximation, though possibly at the cost of an increase in runtime.

Quantum Linear System Solver. A quantum algorithm is proposed to generate a quantum state approximately proportional to the solution of a linear system of equations. Namely, given a linear system A{right arrow over (x)}={right arrow over (b)}, the algorithm produces a quantum state close to

\({\left. {❘x} \right\rangle:=\frac{\left. {\Sigma_{j}x_{j}{❘j}} \right\rangle}{\sqrt{\Sigma_{j}{❘x_{j}❘}^{2}}}},\)

where xj's are the entries of {right arrow over (x)}=A−1{right arrow over (b)}. In fact, in many cases, it is only necessary to know (x|M|x), where M is a linear operator. For example, in quantum mechanics, many features of |x can be extracted in this way, including normalization, moments, etc. One approach to solve this problem is first solving the linear system using any quantum linear system solver to obtain the state Ix) and then performing the measurement of M. However, a shortcoming of this method is that most of the quantum linear system solvers require deep quantum circuits. And hence, the needed quantum resources may not be accessible in the near future.

Recently, a few quantum algorithms were developed to solve linear systems of equations by encoding such a system into an effective Hamiltonian

HG:=A†(I−|b b|)A,  (79)

whose ground state corresponds to the solution vector ⊕x. This idea can be combined with the disclosed ground state property estimation algorithm to get a low-depth algorithm for estimating the properties of linear system solution. More specifically, suppose the Hamiltonian HG can be simulated for some specified time and the normalization factor τ is known such that the eigenvalues of τHG are in [−π/3,π/3]. For the operator M, assume that M can be decomposed into a linear combination of Pauli operators M= , or assume that M is given in the block-encoding form. The estimation algorithm has two steps:


- - 1. Run a quantum linear system algorithm with constant precision to
    prepare an initial state \|ϕ₀) such that
    ϕ₀\|x
    \|² is Ω(1).
  - 2. Using \|ϕ₀
    C)) from step 1 as the initial state, run Algorithm 3 to estimate
    x\|M\|x
    within ϵ-additive error for any ϵ∈(0,1).

Step 1 takes Õ(κ) time, where κ is the condition number of A. To analyze the computation cost of the second step, a lower-bound on the spectral gap of HG is needed. Since  x|A†(I−|bb|)A|x=0, the results in λ0(HG)=0. For the second smallest eigenvalue, since HG=A†A−Aeτ|b b|A, by Weyl's inequality, ga(κ−2).

\(\begin{matrix}
{{{{\lambda_{1}\left( H_{G} \right)} \geq {{\lambda_{0}\left( {A^{\dagger}A} \right)} - {\lambda_{1}\left( {A^{\dagger}{❘{bb}❘}A} \right)}}} = {\lambda_{0}\left( {A^{\dagger}A} \right)}},} & (80)
\end{matrix}\)

where the second step follows from A†|b b|A is rank−1. Due to the normalization, the smallest (normalized) singular value of A is Ω(κ−1). Hence, γ=Ω(κ−2). By Theorem 1, the maximal evolution time of the Hamiltonian will be Õ(κ2). To further improve the circuit depth, the gap amplification technique may be applied to quadratically increase the spectral gap of HG. Specifically, consider the following family of Hamiltonians:

{right arrow over (H)}′G(s):=σ+⊗Ā†(s)(I−| |)+σ−⊗(I−| |)Ā(s),  (81)

where 94 ±=(X±iY)/2, Ā(s):=(1−s)Z⊗I+sX⊗A, |:=|+|: and s ∈[0,1]. Note that these Hamiltonians act on the original system and two ancilla qubits. Then:

\(\begin{matrix}
{{\left( {{\overset{–}{H}}_{G}^{\prime}(s)} \right)^{2} = \begin{bmatrix}
{{\overset{–}{H}}_{G}(s)} & {0\left( {82} \right)} \\
0 & {\left( {I - {❘{\overset{\_}{b}\overset{¯}{b}}❘}} \right){\overset{\_}{A}(s)}{{\overset{\_}{A}}^{\dagger}(s)}\left( {I - {❘{\overset{\_}{b}\overset{\_}{b}}❘}} \right)}
\end{bmatrix}},} & (83)
\end{matrix}\)
\(\begin{matrix}
{{{\overset{¯}{H}}_{G}(s)}:={{{\overset{\_}{A}}^{\dagger}(s)}\left( {I - {❘{\overset{\_}{b}\overset{¯}{b}}❘}} \right){{\overset{\_}{A}(s)}.}}} & (84)
\end{matrix}\)

As shown, the eigenvalues of Ĥ′G(s) are

{0,0,±√{square root over (λ1)s),)} ±√{square root over (λ2(s),)}. . . },  (85)

where λj(s)'s are the nonzero eigenvalues of ĤG(s). Furthermore, let |x(s) be the unique ground state of ĤG (S) . Note that |x(0)=|-|b and |x(1)=|+ |x.)1x). Then the ground space of Ĥ′G (s) is spanned by {|0|x(s), |1 | }. In addition, for s=1, one can use Weyl's ineqality to show that λ1 (1)≥κ−2, which implies that the smallest nonzero eigenvalue of G′ (1) is (1) is Ω(κ−1), as desired.

The disclosed algorithm used to prepare a state that has Ω(1) overlap with |0|x(1) =|0 |+ |x in Õ(κ) time. Specifically, this algorithm starts with the state |0|x(0)=|(0 ||b , performs a sequence of unitary operations of form e−it′(s) on it, and outputs a state ϵ-close to |0)|x(1)) in Õ(κϵ−1) time. Here, ϵ=Θ(1) is set, and the time cost of this procedure is Õ(κ). After obtaining a state |ϕ0 that has Ω(1) overlap with |0 |+ |x, Algorithm 3 may be run on |ϕ0, ′G(1) and {tilde over (M)}:=|0  0|⊗|+ +|⊗M to estimate  0+, x|{tilde over (M)}|0,+,x =|M|.

Since the ground state energy of ′G(1) is zero, it is not needed to first estimate the ground state energy using Algorithm 1. Instead, direct evaluation may be used with O-weighted CDF at zero. Therefore, by Theorem 1, the following result is obtained.

Corollary 1. (Quantum linear system solution property estimation). For a linear system A{right arrow over (x)}={right arrow over (b)}, suppose A has singular values in [−1, −1/κ] ∪[1/κ,1] for κ>1, and the eigenvalues of ′G(1) (Eq. (81)) are in [−π/3,π3]. Furthermore, it is possible to implement e−-it′(s) (Eq. (81)) in Õ(t) time for all s∈[0,1].

Then, for any linear operator M given by its a-block encoding unitary UM, and for any ϵ∈(0,1), the expectation value  x|M|x can be estimated with ϵ-additive error with high probability such that:


- - the depth of each circuit is Õ(κ)
  - the expected total runtime is Õ(κϵ⁻²α²).

For comparison, the algorithm in needs Õ(κϵ−1) circuit depth to obtain a state that is ϵ-close to |x , which is larger than that of the disclosed algorithm. Moreover, to estimate  x|M|x, even with amplitude estimation, it still needs Ω(ϵ−1) copies of the state to achieve E-additive error. Hence, its total runtime will be Õ(κϵ−2), nearly matching the result of the disclosed algorithm (ignoring the dependence on the α factor).

A quantum-classical hybrid algorithm has been disclosed for estimating properties of the ground state of a Hamiltonian, such that the quantum circuit depth is relatively small and only poly-logarithmically depends on ϵ−1. Therefore, the algorithm has a significant advantage in high-accuracy estimation, and it is possible to be implemented in early fault-tolerant devices. In practice, the disclosed algorithm can solve many important tasks by combining with some initial state preparation methods (e.g., VQE or QAOA). Current applications include quantum chemistry and solving linear systems. More applications will be explored in the future.

Another important direction is to improve the total evolution time of the disclosed algorithm which quadratically depends on ϵ−1. The blowup comes from evaluating the O-weighted CDF in high precision and a trade-off between maximal evolution time and total evolution time. However, this does not meet the Heisenberg-limit of linear dependence on ϵ−1 for generic Hamiltonians. In the main result (Theorem 1), the ϵ−2η−2 factor comes from the number of samples needed to reduce the estimator's error to O (ϵη). Amplitude estimation can be used to reduce this number of samples and the total evolution time. However, this comes at the cost of significantly increasing the maximal evolution time, which could require large fault-tolerant overheads for reliable implementation.

If λ characterizes the fidelity decay rate of the circuit as deeper circuits are used, then it would be expected to require a maximal evolution time of O(ξ−1γ−1) and a total evolution time of O(λγ−1ϵ−2η−2). Note that because this approach incorporates the impact of error into the algorithm, the maximal evolution time is of no concern. Rather than being a cost that needs monitoring, the maximal evolution time is chosen by the algorithm to minimize the total evolution time. As the quality of devices improves, the performance of the algorithm improves proportionally. A similar approach can also be applied to improve the total evolution time in from Õ(ϵ−1η−2) to Õ(λϵ−1η−2).

In some embodiments, the techniques described herein relate to a method for estimating a ground state property of an observable (O), performed on a hybrid quantum-classical computer, the computer including a quantum computing component having a plurality of qubits, and a classical computing component including at least one processor and a non-transitory computer-readable memory, the non-transitory computer-readable memory storing computer instructions, which, when executed by the classical processor, perform the method, the method including: initializing the quantum component to an initial state with qubit registers; estimating the ground state energy of a Hamiltonian (H) matrix that characterizes a physical system; generating a plurality of samples from a parameterized Hadamard test circuit; evaluating the sample outcomes; estimating the expectation value ( ) of the observable (O) with respect to the ground state energy; estimating the weighted expectation value ; and from the weighted expectation value, deriving an estimate of the ground state property.

Initializing the quantum component to the initial state may include initializing the quantum component to the initial state with the qubit registers and a single ancilla qubit.

The method may further include computing Green's functions using the ground state property. Computing Green's functions may include computing Green's functions to compute electron transport in materials. Computing Green's functions may include computing Green's functions to compute electric dipoles of molecules.

The physical system may include a molecule. The method may further include computing the charge density of the molecule. Computing the charge density of the molecule may include computing the charge density of the molecule from the one-particle reduced density matrix.

The physical system may include a material.

Deriving the estimate of the ground state property may include deriving the estimate of the ground state property using a low-depth quantum circuit with reduced error rates. The quantum circuit depth of the low-depth quantum circuit may be linear in the inverse spectral gap and poly-logarithmic in the inverse target accuracy and inverse initial overlap.

The method may further include using the using the ground state property to generate a quantum state approximately proportional to a solution of a linear system of equations.

Initializing the quantum component to the initial state may includes executing a variational quantum eigensolver (VQE). Initializing the quantum component to the initial state includes executing a quantum approximate optimization algorithm (QAQO).

In some embodiments, the techniques described herein relate to a quantum-classical algorithm for estimating a ground state property of an observable (0), wherein the algorithm (1) estimates ground state energy, (2) estimates the expectation value of the observable (O) with respect to the ground state, and (3) estimates the weighted expectation values.

In some embodiments, the techniques described herein relate to a system for estimating a ground state property of an observable (O), the system including a hybrid quantum-classical computer (HQC), the HQC computer including a quantum computing component having a plurality of qubits and a classical computing component including at least one processor and a non-transitory computer-readable memory, the non-transitory computer-readable memory storing computer instructions, which, when executed by the classical processor, perform a method for estimating the ground state property of the observable (O), the method, including: initializing the quantum component to an initial state with qubit registers; estimating the ground state energy of a Hamiltonian (H) matrix that characterizes a physical system; generating a plurality of samples from a parameterized Hadamard test circuit; evaluating the sample outcomes; estimating the expectation value ( ) of the observable (O) with respect to the ground state energy; estimating the weighted expectation value ; and from the weighted expectation value, deriving an estimate of the ground state property

It is to be understood that although the invention has been described above in terms of particular embodiments, the foregoing embodiments are provided as illustrative only, and do not limit or define the scope of the invention. Various other embodiments, including but not limited to the following, are also within the scope of the claims. For example, elements and components described herein may be further divided into additional components or joined together to form fewer components for performing the same functions.

Various physical embodiments of a quantum computer are suitable for use according to the present disclosure. In general, the fundamental data storage unit in quantum computing is the quantum bit, or qubit. The qubit is a quantum-computing analog of a classical digital computer system bit. A classical bit is considered to occupy, at any given point in time, one of two possible states corresponding to the binary digits (bits) 0 or 1. By contrast, a qubit is implemented in hardware by a physical medium with quantum-mechanical characteristics. Such a medium, which physically instantiates a qubit, may be referred to herein as a “physical instantiation of a qubit,” a “physical embodiment of a qubit,” a “medium embodying a qubit,” or similar terms, or simply as a “qubit,” for ease of explanation. It should be understood, therefore, that references herein to “qubits” within descriptions of embodiments of the present invention refer to physical media which embody qubits.

Each qubit has an infinite number of different potential quantum-mechanical states. When the state of a qubit is physically measured, the measurement produces one of two different basis states resolved from the state of the qubit. Thus, a single qubit can represent a one, a zero, or any quantum superposition of those two qubit states; a pair of qubits can be in any quantum superposition of 4 orthogonal basis states; and three qubits can be in any superposition of 8 orthogonal basis states. The function that defines the quantum-mechanical states of a qubit is known as its wavefunction. The wavefunction also specifies the probability distribution of outcomes for a given measurement. A qubit, which has a quantum state of dimension two (i.e., has two orthogonal basis states), may be generalized to a d-dimensional “qudit,” where d may be any integral value, such as 2, 3, 4, or higher. In the general case of a qudit, measurement of the qudit produces one of d different basis states resolved from the state of the qudit. Any reference herein to a qubit should be understood to refer more generally to an d-dimensional qudit with any value of d.

Although certain descriptions of qubits herein may describe such qubits in terms of their mathematical properties, each such qubit may be implemented in a physical medium in any of a variety of different ways. Examples of such physical media include superconducting material, trapped ions, photons, optical cavities, individual electrons trapped within quantum dots, point defects in solids (e.g., phosphorus donors in silicon or nitrogen-vacancy centers in diamond), molecules (e.g., alanine, vanadium complexes), or aggregations of any of the foregoing that exhibit qubit behavior, that is, comprising quantum states and transitions therebetween that can be controllably induced or detected.

For any given medium that implements a qubit, any of a variety of properties of that medium may be chosen to implement the qubit. For example, if electrons are chosen to implement qubits, then the x component of its spin degree of freedom may be chosen as the property of such electrons to represent the states of such qubits. Alternatively, the y component, or the z component of the spin degree of freedom may be chosen as the property of such electrons to represent the state of such qubits. This is merely a specific example of the general feature that for any physical medium that is chosen to implement qubits, there may be multiple physical degrees of freedom (e.g., the x, y, and z components in the electron spin example) that may be chosen to represent 0 and 1. For any particular degree of freedom, the physical medium may controllably be put in a state of superposition, and measurements may then be taken in the chosen degree of freedom to obtain readouts of qubit values.

Certain implementations of quantum computers, referred to as gate model quantum computers, comprise quantum gates. In contrast to classical gates, there is an infinite number of possible single-qubit quantum gates that change the state vector of a qubit. Changing the state of a qubit state vector typically is referred to as a single-qubit rotation, and may also be referred to herein as a state change or a single-qubit quantum-gate operation. A rotation, state change, or single-qubit quantum-gate operation may be represented mathematically by a unitary 2X2 matrix with complex elements. A rotation corresponds to a rotation of a qubit state within its Hilbert space, which may be conceptualized as a rotation of the Bloch sphere. (As is well-known to those having ordinary skill in the art, the Bloch sphere is a geometrical representation of the space of pure states of a qubit.) Multi-qubit gates alter the quantum state of a set of qubits. For example, two-qubit gates rotate the state of two qubits as a rotation in the four-dimensional Hilbert space of the two qubits. (As is well-known to those having ordinary skill in the art, a Hilbert space is an abstract vector space possessing the structure of an inner product that allows length and angle to be measured. Furthermore, Hilbert spaces are complete: there are enough limits in the space to allow the techniques of calculus to be used.)

A quantum circuit may be specified as a sequence of quantum gates. As described in more detail below, the term “quantum gate,” as used herein, refers to the application of a gate control signal (defined below) to one or more qubits to cause those qubits to undergo certain physical transformations and thereby to implement a logical gate operation. To conceptualize a quantum circuit, the matrices corresponding to the component quantum gates may be multiplied together in the order specified by the gate sequence to produce a 2″X2″ complex matrix representing the same overall state change on n qubits. A quantum circuit may thus be expressed as a single resultant operator. However, designing a quantum circuit in terms of constituent gates allows the design to conform to a standard set of gates, and thus enable greater ease of deployment. A quantum circuit thus corresponds to a design for actions taken upon the physical components of a quantum computer.

A given variational quantum circuit may be parameterized in a suitable device-specific manner. More generally, the quantum gates making up a quantum circuit may have an associated plurality of tuning parameters. For example, in embodiments based on optical switching, tuning parameters may correspond to the angles of individual optical elements.

In certain embodiments of quantum circuits, the quantum circuit includes both one or more gates and one or more measurement operations. Quantum computers implemented using such quantum circuits are referred to herein as implementing “measurement feedback.” For example, a quantum computer implementing measurement feedback may execute the gates in a quantum circuit and then measure only a subset (i.e., fewer than all) of the qubits in the quantum computer, and then decide which gate(s) to execute next based on the outcome(s) of the measurement(s). In particular, the measurement(s) may indicate a degree of error in the gate operation(s), and the quantum computer may decide which gate(s) to execute next based on the degree of error. The quantum computer may then execute the gate(s) indicated by the decision. This process of executing gates, measuring a subset of the qubits, and then deciding which gate(s) to execute next may be repeated any number of times. Measurement feedback may be useful for performing quantum error correction, but is not limited to use in performing quantum error correction. For every quantum circuit, there is an error-corrected implementation of the circuit with or without measurement feedback.

Some embodiments described herein generate, measure, or utilize quantum states that approximate a target quantum state (e.g., a ground state of a Hamiltonian). As will be appreciated by those trained in the art, there are many ways to quantify how well a first quantum state “approximates” a second quantum state. In the following description, any concept or definition of approximation known in the art may be used without departing from the scope hereof. For example, when the first and second quantum states are represented as first and second vectors, respectively, the first quantum state approximates the second quantum state when an inner product between the first and second vectors (called the “fidelity” between the two quantum states) is greater than a predefined amount (typically labeled E). In this example, the fidelity quantifies how “close” or “similar” the first and second quantum states are to each other. The fidelity represents a probability that a measurement of the first quantum state will give the same result as if the measurement were performed on the second quantum state. Proximity between quantum states can also be quantified with a distance measure, such as a Euclidean norm, a Hamming distance, or another type of norm known in the art. Proximity between quantum states can also be defined in computational terms. For example, the first quantum state approximates the second quantum state when a polynomial time-sampling of the first quantum state gives some desired information or property that it shares with the second quantum state.

Not all quantum computers are gate model quantum computers. Embodiments of the present invention are not limited to being implemented using gate model quantum computers. As an alternative example, embodiments of the present invention may be implemented, in whole or in part, using a quantum computer that is implemented using a quantum annealing architecture, which is an alternative to the gate model quantum computing architecture. More specifically, quantum annealing (QA) is a metaheuristic for finding the global minimum of a given objective function over a given set of candidate solutions (candidate states), by a process using quantum fluctuations.

FIG. 2B shows a diagram illustrating operations typically performed by a computer system 250 which implements quantum annealing. The system 250 includes both a quantum computer 252 and a classical computer 254. Operations shown on the left of the dashed vertical line 256 typically are performed by the quantum computer 252, while operations shown on the right of the dashed vertical line 256 typically are performed by the classical computer 254.

Quantum annealing starts with the classical computer 254 generating an initial Hamiltonian 260 and a final Hamiltonian 262 based on a computational problem 258 to be solved, and providing the initial Hamiltonian 260, the final Hamiltonian 262 and an annealing schedule 270 as input to the quantum computer 252. The quantum computer 252 prepares a well-known initial state 266 (FIG. 2B, operation 264), such as a quantum-mechanical superposition of all possible states (candidate states) with equal weights, based on the initial Hamiltonian 260. The classical computer 254 provides the initial Hamiltonian 260, a final Hamiltonian 262, and an annealing schedule 270 to the quantum computer 252. The quantum computer 252 starts in the initial state 266, and evolves its state according to the annealing schedule 270 following the time-dependent Schrodinger equation, a natural quantum-mechanical evolution of physical systems (FIG. 2B, operation 268). More specifically, the state of the quantum computer 252 undergoes time evolution under a time-dependent Hamiltonian, which starts from the initial Hamiltonian 260 and terminates at the final Hamiltonian 262. If the rate of change of the system Hamiltonian is slow enough, the system stays close to the ground state of the instantaneous Hamiltonian. If the rate of change of the system Hamiltonian is accelerated, the system may leave the ground state temporarily but produce a higher likelihood of concluding in the ground state of the final problem Hamiltonian, i.e., diabatic quantum computation. At the end of the time evolution, the set of qubits on the quantum annealer is in a final state 272, which is expected to be close to the ground state of the classical Ising model that corresponds to the solution to the original computational problem 258. An experimental demonstration of the success of quantum annealing for random magnets was reported immediately after the initial theoretical proposal.

The final state 272 of the quantum computer 252 is measured, thereby producing results 276 (i.e., measurements) (FIG. 2B, operation 274). The measurement operation 274 may be performed, for example, in any of the ways disclosed herein, such as in any of the ways disclosed herein in connection with the measurement unit 110 in FIG. 1. The classical computer 254 performs postprocessing on the measurement results 276 to produce output 280 representing a solution to the original computational problem 258 (FIG. 2B, operation 278).

As yet another alternative example, embodiments of the present invention may be implemented, in whole or in part, using a quantum computer that is implemented using a one-way quantum computing architecture, also referred to as a measurement-based quantum computing architecture, which is another alternative to the gate model quantum computing architecture. More specifically, the one-way or measurement based quantum computer (MBQC) is a method of quantum computing that first prepares an entangled resource state, usually a cluster state or graph state, then performs single qubit measurements on it. It is “one-way” because the resource state is destroyed by the measurements.

The outcome of each individual measurement is random, but they are related in such a way that the computation always succeeds. In general the choices of basis for later measurements need to depend on the results of earlier measurements, and hence the measurements cannot all be performed at the same time.

Any of the functions disclosed herein may be implemented using means for performing those functions. Such means include, but are not limited to, any of the components disclosed herein, such as the computer-related components described below.

Referring to FIG. 1, a diagram is shown of a system 100 implemented according to one embodiment of the present invention. Referring to FIG. 2A, a flowchart is shown of a method 200 performed by the system 100 of FIG. 1 according to one embodiment of the present invention. The system 100 includes a quantum computer 102. The quantum computer 102 includes a plurality of qubits 104, which may be implemented in any of the ways disclosed herein. There may be any number of qubits 104 in the quantum computer 102. For example, the qubits 104 may include or consist of no more than 2 qubits, no more than 4 qubits, no more than 8 qubits, no more than 16 qubits, no more than 32 qubits, no more than 64 qubits, no more than 128 qubits, no more than 256 qubits, no more than 512 qubits, no more than 1024 qubits, no more than 2048 qubits, no more than 4096 qubits, or no more than 8192 qubits. These are merely examples, in practice there may be any number of qubits 104 in the quantum computer 102.

There may be any number of gates in a quantum circuit. However, in some embodiments the number of gates may be at least proportional to the number of qubits 104 in the quantum computer 102. In some embodiments the gate depth may be no greater than the number of qubits 104 in the quantum computer 102, or no greater than some linear multiple of the number of qubits 104 in the quantum computer 102 (e.g., 2, 3, 4, 5, 6, or 7).

The qubits 104 may be interconnected in any graph pattern. For example, they be connected in a linear chain, a two-dimensional grid, an all-to-all connection, any combination thereof, or any subgraph of any of the preceding.

As will become clear from the description below, although element 102 is referred to herein as a “quantum computer,” this does not imply that all components of the quantum computer 102 leverage quantum phenomena. One or more components of the quantum computer 102 may, for example, be classical (i.e., non-quantum components) components which do not leverage quantum phenomena.

The quantum computer 102 includes a control unit 106, which may include any of a variety of circuitry and/or other machinery for performing the functions disclosed herein. The control unit 106 may, for example, consist entirely of classical components. The control unit 106 generates and provides as output one or more control signals 108 to the qubits 104. The control signals 108 may take any of a variety of forms, such as any kind of electromagnetic signals, such as electrical signals, magnetic signals, optical signals (e.g., laser pulses), or any combination thereof.

For example:


- - In embodiments in which some or all of the qubits **104** are
    implemented as photons (also referred to as a “quantum optical”
    implementation) that travel along waveguides, the control unit
    **106** may be a beam splitter (e.g., a heater or a mirror), the
    control signals **108** may be signals that control the heater or
    the rotation of the mirror, the measurement unit **110** may be a
    photodetector, and the measurement signals **112** may be photons.
  - In embodiments in which some or all of the qubits **104** are
    implemented as charge type qubits (e.g., transmon, X-mon, G-mon) or
    flux-type qubits (e.g., flux qubits, capacitively shunted flux
    qubits) (also referred to as a “circuit quantum electrodynamic”
    (circuit QED) implementation), the control unit **106** may be a bus
    resonator activated by a drive, the control signals **108** may be
    cavity modes, the measurement unit **110** may be a second resonator
    (e.g., a low-Q resonator), and the measurement signals **112** may
    be voltages measured from the second resonator using dispersive
    readout techniques.
  - In embodiments in which some or all of the qubits **104** are
    implemented as superconducting circuits, the control unit **106**
    may be a circuit QED-assisted control unit or a direct capacitive
    coupling control unit or an inductive capacitive coupling control
    unit, the control signals **108** may be cavity modes, the
    measurement unit **110** may be a second resonator (e.g., a low-Q
    resonator), and the measurement signals **112** may be voltages
    measured from the second resonator using dispersive readout
    techniques.
  - In embodiments in which some or all of the qubits **104** are
    implemented as trapped ions (e.g., electronic states of, e.g.,
    magnesium ions), the control unit **106** may be a laser, the
    control signals **108** may be laser pulses, the measurement unit
    **110** may be a laser and either a CCD or a photodetector (e.g., a
    photomultiplier tube), and the measurement signals **112** may be
    photons.
  - In embodiments in which some or all of the qubits **104** are
    implemented using nuclear magnetic resonance (NMR) (in which case
    the qubits may be molecules, e.g., in liquid or solid form), the
    control unit **106** may be a radio frequency (RF) antenna, the
    control signals **108** may be RF fields emitted by the RF antenna,
    the measurement unit **110** may be another RF antenna, and the
    measurement signals **112** may be RF fields measured by the second
    RF antenna.
  - In embodiments in which some or all of the qubits **104** are
    implemented as nitrogen-vacancy centers (NV centers), the control
    unit **106** may, for example, be a laser, a microwave antenna, or a
    coil, the control signals **108** may be visible light, a microwave
    signal, or a constant electromagnetic field, the measurement unit
    **110** may be a photodetector, and the measurement signals **112**
    may be photons.
  - In embodiments in which some or all of the qubits **104** are
    implemented as two-dimensional quasiparticles called “anyons” (also
    referred to as a “topological quantum computer” implementation), the
    control unit **106** may be nanowires, the control signals **108**
    may be local electrical fields or microwave pulses, the measurement
    unit **110** may be superconducting circuits, and the measurement
    signals **112** may be voltages.
  - In embodiments in which some or all of the qubits **104** are
    implemented as semiconducting material (e.g., nanowires), the
    control unit **106** may be microfabricated gates, the control
    signals **108** may be RF or microwave signals, the measurement unit
    **110** may be microfabricated gates, and the measurement signals
    **112** may be RF or microwave signals.

Although not shown explicitly in FIG. 1 and not required, the measurement unit 110 may provide one or more feedback signals 114 to the control unit 106 based on the measurement signals 112. For example, quantum computers referred to as “one-way quantum computers” or “measurement-based quantum computers” utilize such feedback signals 114 from the measurement unit 110 to the control unit 106. Such feedback signals 114 are also necessary for the operation of fault-tolerant quantum computing and error correction.

The control signals 108 may, for example, include one or more state preparation signals which, when received by the qubits 104, cause some or all of the qubits 104 to change their states. Such state preparation signals constitute a quantum circuit also referred to as an “ansatz circuit.” The resulting state of the qubits 104 is referred to herein as an “initial state” or an “ansatz state.” The process of outputting the state preparation signal(s) to cause the qubits 104 to be in their initial state is referred to herein as “state preparation” (FIG. 2A, section 206). A special case of state preparation is “initialization,” also referred to as a “reset operation,” in which the initial state is one in which some or all of the qubits 104 are in the “zero” state i.e. the default single-qubit state. More generally, state preparation may involve using the state preparation signals to cause some or all of the qubits 104 to be in any distribution of desired states. In some embodiments, the control unit 106 may first perform initialization on the qubits 104 and then perform preparation on the qubits 104, by first outputting a first set of state preparation signals to initialize the qubits 104, and by then outputting a second set of state preparation signals to put the qubits 104 partially or entirely into non-zero states.

Another example of control signals 108 that may be output by the control unit 106 and received by the qubits 104 are gate control signals. The control unit 106 may output such gate control signals, thereby applying one or more gates to the qubits 104. Applying a gate to one or more qubits causes the set of qubits to undergo a physical state change which embodies a corresponding logical gate operation (e.g., single-qubit rotation, two-qubit entangling gate or multi-qubit operation) specified by the received gate control signal. As this implies, in response to receiving the gate control signals, the qubits 104 undergo physical transformations which cause the qubits 104 to change state in such a way that the states of the qubits 104, when measured (see below), represent the results of performing logical gate operations specified by the gate control signals. The term “quantum gate,” as used herein, refers to the application of a gate control signal to one or more qubits to cause those qubits to undergo the physical transformations described above and thereby to implement a logical gate operation.

It should be understood that the dividing line between state preparation (and the corresponding state preparation signals) and the application of gates (and the corresponding gate control signals) may be chosen arbitrarily. For example, some or all the components and operations that are illustrated in FIGS. 1 and 2A-2B as elements of “state preparation” may instead be characterized as elements of gate application. Conversely, for example, some or all of the components and operations that are illustrated in FIGS. 1 and 2A-2B as elements of “gate application” may instead be characterized as elements of state preparation. As one particular example, the system and method of FIGS. 1 and 2A-2B may be characterized as solely performing state preparation followed by measurement, without any gate application, where the elements that are described herein as being part of gate application are instead considered to be part of state preparation. Conversely, for example, the system and method of FIGS. 1 and 2A-2B may be characterized as solely performing gate application followed by measurement, without any state preparation, and where the elements that are described herein as being part of state preparation are instead considered to be part of gate application.

The quantum computer 102 also includes a measurement unit 110, which performs one or more measurement operations on the qubits 104 to read out measurement signals 112 (also referred to herein as “measurement results”) from the qubits 104, where the measurement results 112 are signals representing the states of some or all of the qubits 104. In practice, the control unit 106 and the measurement unit 110 may be entirely distinct from each other, or contain some components in common with each other, or be implemented using a single unit (i.e., a single unit may implement both the control unit 106 and the measurement unit 110). For example, a laser unit may be used both to generate the control signals 108 and to provide stimulus (e.g., one or more laser beams) to the qubits 104 to cause the measurement signals 112 to be generated.

In general, the quantum computer 102 may perform various operations described above any number of times. For example, the control unit 106 may generate one or more control signals 108, thereby causing the qubits 104 to perform one or more quantum gate operations. The measurement unit 110 may then perform one or more measurement operations on the qubits 104 to read out a set of one or more measurement signals 112. The measurement unit 110 may repeat such measurement operations on the qubits 104 before the control unit 106 generates additional control signals 108, thereby causing the measurement unit 110 to read out additional measurement signals 112 resulting from the same gate operations that were performed before reading out the previous measurement signals 112. The measurement unit 110 may repeat this process any number of times to generate any number of measurement signals 112 corresponding to the same gate operations. The quantum computer 102 may then aggregate such multiple measurements of the same gate operations in any of a variety of ways.

After the measurement unit 110 has performed one or more measurement operations on the qubits 104 after they have performed one set of gate operations, the control unit 106 may generate one or more additional control signals 108, which may differ from the previous control signals 108, thereby causing the qubits 104 to perform one or more additional quantum gate operations, which may differ from the previous set of quantum gate operations. The process described above may then be repeated, with the measurement unit 110 performing one or more measurement operations on the qubits 104 in their new states (resulting from the most recently-performed gate operations).

In general, the system 100 may implement a plurality of quantum circuits as follows. For each quantum circuit C in the plurality of quantum circuits (FIG. 2A, operation 202), the system 100 performs a plurality of “shots” on the qubits 104. The meaning of a shot will become clear from the description that follows. For each shot S in the plurality of shots (FIG. 2A, operation 204), the system 100 prepares the state of the qubits 104 (FIG. 2A, section 206). More specifically, for each quantum gate Gin quantum circuit C (FIG. 2A, operation 210), the system 100 applies quantum gate G to the qubits 104 (FIG. 2A, operations 212 and 214).

Then, for each of the qubits Q 104 (FIG. 2A, operation 216), the system 100 measures the qubit Q to produce measurement output representing a current state of qubit Q (FIG. 2A, operations 218 and 220).

The operations described above are repeated for each shot S (FIG. 2A, operation 222), and circuit C (FIG. 2A, operation 224). As the description above implies, a single “shot” involves preparing the state of the qubits 104 and applying all of the quantum gates in a circuit to the qubits 104 and then measuring the states of the qubits 104; and the system 100 may perform multiple shots for one or more circuits.

Referring to FIG. 3, a diagram is shown of a hybrid quantum classical (HQC) computer 300 implemented according to one embodiment of the present invention. The HQC 300 includes a quantum computer component 102 (which may, for example, be implemented in the manner shown and described in connection with FIG. 1) and a classical computer component 306. The classical computer component may be a machine implemented according to the general computing model established by John Von Neumann, in which programs are written in the form of ordered lists of instructions and stored within a classical (e.g., digital) memory 310 and executed by a classical (e.g., digital) processor 308 of the classical computer. The memory 310 is classical in the sense that it stores data in a storage medium in the form of bits, which have a single definite binary state at any point in time. The bits stored in the memory 310 may, for example, represent a computer program. The classical computer component 304 typically includes a bus 314. The processor 308 may read bits from and write bits to the memory 310 over the bus 314. For example, the processor 308 may read instructions from the computer program in the memory 310, and may optionally receive input data 316 from a source external to the computer 302, such as from a user input device such as a mouse, keyboard, or any other input device. The processor 308 may use instructions that have been read from the memory 310 to perform computations on data read from the memory 310 and/or the input 316, and generate output from those instructions. The processor 308 may store that output back into the memory 310 and/or provide the output externally as output data 318 via an output device, such as a monitor, speaker, or network device.

The quantum computer component 102 may include a plurality of qubits 104, as described above in connection with FIG. 1. A single qubit may represent a one, a zero, or any quantum superposition of those two qubit states. The classical computer component 304 may provide classical state preparation signals 332 to the quantum computer 102, in response to which the quantum computer 102 may prepare the states of the qubits 104 in any of the ways disclosed herein, such as in any of the ways disclosed in connection with FIGS. 1 and 2A-2B.

Once the qubits 104 have been prepared, the classical processor 308 may provide classical control signals 334 to the quantum computer 102, in response to which the quantum computer 102 may apply the gate operations specified by the control signals 332 to the qubits 104, as a result of which the qubits 104 arrive at a final state. The measurement unit 110 in the quantum computer 102 (which may be implemented as described above in connection with FIGS. 1 and 2A-2B) may measure the states of the qubits 104 and produce measurement output 338 representing the collapse of the states of the qubits 104 into one of their eigenstates. As a result, the measurement output 338 includes or consists of bits and therefore represents a classical state. The quantum computer 102 provides the measurement output 338 to the classical processor 308. The classical processor 308 may store data representing the measurement output 338 and/or data derived therefrom in the classical memory 310.

The steps described above may be repeated any number of times, with what is described above as the final state of the qubits 104 serving as the initial state of the next iteration. In this way, the classical computer 304 and the quantum computer 102 may cooperate as co-processors to perform joint computations as a single computer system.

Although certain functions may be described herein as being performed by a classical computer and other functions may be described herein as being performed by a quantum computer, these are merely examples and do not constitute limitations of the present invention. A subset of the functions which are disclosed herein as being performed by a quantum computer may instead be performed by a classical computer. For example, a classical computer may execute functionality for emulating a quantum computer and provide a subset of the functionality described herein, albeit with functionality limited by the exponential scaling of the simulation. Functions which are disclosed herein as being performed by a classical computer may instead be performed by a quantum computer.

The techniques described above may be implemented, for example, in hardware, in one or more computer programs tangibly stored on one or more computer-readable media, firmware, or any combination thereof, such as solely on a quantum computer, solely on a classical computer, or on a hybrid quantum classical (HQC) computer. The techniques disclosed herein may, for example, be implemented solely on a classical computer, in which the classical computer emulates the quantum computer functions disclosed herein.

Any reference herein to the state 10) may alternatively refer to the state 11), and vice versa. In other words, any role described herein for the states 10) and11) may be reversed within embodiments of the present invention. More generally, any computational basis state disclosed herein may be replaced with any suitable reference state within embodiments of the present invention.

The techniques described above may be implemented in one or more computer programs executing on (or executable by) a programmable computer (such as a classical computer, a quantum computer, or an HQC) including any combination of any number of the following: a processor, a storage medium readable and/or writable by the processor (including, for example, volatile and non-volatile memory and/or storage elements), an input device, and an output device. Program code may be applied to input entered using the input device to perform the functions described and to generate output using the output device.

Embodiments of the present invention include features which are only possible and/or feasible to implement with the use of one or more computers, computer processors, and/or other elements of a computer system. Such features are either impossible or impractical to implement mentally and/or manually. For example, embodiments of the present invention initialize a quantum component to an initial state with qubit registers and estimate the ground state energy of a Hamiltonian (H) matrix that characterizes a physical system. Such functions are inherently rooted in quantum computing technology and cannot be performed mentally or manually.

Any claims herein which affirmatively require a computer, a processor, a memory, or similar computer-related elements, are intended to require such elements, and should not be interpreted as if such elements are not present in or required by such claims. Such claims are not intended, and should not be interpreted, to cover methods and/or systems which lack the recited computer-related elements. For example, any method claim herein which recites that the claimed method is performed by a computer, a processor, a memory, and/or similar computer-related element, is intended to, and should only be interpreted to, encompass methods which are performed by the recited computer-related element(s). Such a method claim should not be interpreted, for example, to encompass a method that is performed mentally or by hand (e.g., using pencil and paper). Similarly, any product claim herein which recites that the claimed product includes a computer, a processor, a memory, and/or similar computer-related element, is intended to, and should only be interpreted to, encompass products which include the recited computer-related element(s). Such a product claim should not be interpreted, for example, to encompass a product that does not include the recited computer-related element(s).

In embodiments in which a classical computing component executes a computer program providing any subset of the functionality within the scope of the claims below, the computer program may be implemented in any programming language, such as assembly language, machine language, a high-level procedural programming language, or an object-oriented programming language. The programming language may, for example, be a compiled or interpreted programming language.

Each such computer program may be implemented in a computer program product tangibly embodied in a machine-readable storage device for execution by a computer processor, which may be either a classical processor or a quantum processor. Method steps of the invention may be performed by one or more computer processors executing a program tangibly embodied on a computer-readable medium to perform functions of the invention by operating on input and generating output. Suitable processors include, by way of example, both general and special purpose microprocessors. Generally, the processor receives (reads) instructions and data from a memory (such as a read-only memory and/or a random access memory) and writes (stores) instructions and data to the memory. Storage devices suitable for tangibly embodying computer program instructions and data include, for example, all forms of non-volatile memory, such as semiconductor memory devices, including EPROM, EEPROM, and flash memory devices; magnetic disks such as internal hard disks and removable disks; magneto-optical disks; and CD-ROMs. Any of the foregoing may be supplemented by, or incorporated in, specially-designed ASICs (application-specific integrated circuits) or FPGAs (Field-Programmable Gate Arrays). A classical computer can generally also receive (read) programs and data from, and write (store) programs and data to, a non-transitory computer-readable storage medium such as an internal disk (not shown) or a removable disk. These elements will also be found in a conventional desktop or workstation computer as well as other computers suitable for executing computer programs implementing the methods described herein, which may be used in conjunction with any digital print engine or marking engine, display monitor, or other raster output device capable of producing color or gray scale pixels on paper, film, display screen, or other output medium.

Any data disclosed herein may be implemented, for example, in one or more data structures tangibly stored on a non-transitory computer-readable medium (such as a classical computer-readable medium, a quantum computer-readable medium, or an HQC computer-readable medium). Embodiments of the invention may store such data in such data structure(s) and read such data from such data structure(s).

Although terms such as “optimize” and “optimal” are used herein, in practice, embodiments of the present invention may include methods which produce outputs that are not optimal, or which are not known to be optimal, but which nevertheless are useful. For example, embodiments of the present invention may produce an output which approximates an optimal solution, within some degree of error. As a result, terms herein such as “optimize” and “optimal” should be understood to refer not only to processes which produce optimal outputs, but also processes which produce outputs that approximate an optimal solution, within some degree of error.

