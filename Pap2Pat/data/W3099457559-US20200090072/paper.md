# Preliminaries 1.Quantum Walk

We define a classical walk on a d-dimensional state space X = {x} by a d × d transition matrix W where the transition probability x → y is given by matrix element W yx . Thus, the walk maps the distribution p to the distribution p = Wp, where p y = x W yx p x . An aperiodic walk is irreducible if every state in X is accessible from every other state in X , which implies the existence of a unique equilibrium distribution π = Wπ. Finally, a walk is reversible if it obeys the detailed balance condition

We now explain how to quantize a reversible classical walk W. Szegedy's quantum walk [28] is formulated in an oracle setting. For a classical walk W, it assumes a unitary transformation W acting on a Hilbert space C d ⊗ C d with the following action

where |w x := y W yx |y . Define Π 0 as the projector onto the subspace E 0 spanned by states {|x ⊗ |0 } d x=1 . Combining W to the reflection R = 2Π 0 -I and the swap operator Λ, we can construct the quantum walk defined by

Szegedy's walk is defined as ΛW (RW † ΛW )RW † , so it is essentially the square of the operator U W we have defined, but this will have no consequence on what follows aside from a minor simplification.

To analyze the quantum walk U W , let us define the state |ψ x := Λ|φ x = |x ⊗ |w x and consider the operator

At this point, in order to use detailed balance condition of Eq. (1), we need to assume that the walk is reversible to obtain

or, if we restrict the operator X to its support E 0 , we get in matrix notation

2 ). The matrices X and W are thus similar so they have the same eigenvalues. Define its eigenvectors

where λ k are the eigenvalues of W. Because the operator X is obtained by projecting the operator W † ΛW onto the subspace E 0 , its eigenvectors with non-zero eigenvalues in the full Hilbert space must have the form

If we consider the action of W † ΛW without those projections, we get

where |γ ⊥ k is orthogonal to the subspace E 0 , so in particular it is orthogonal to all the vectors |γ k . Finally, because W † ΛW is a unitary, we also obtain that the |γ ⊥ k are orthogonal to each other and that

k } are all mutually orthogonal and that W † ΛW is block diagonal in that basis.

Given the above observations, it is straightforward to verify that

so the eigenvalues of U k on the subspace spanned by {|γ k , |γ ⊥ k } are e ±iθ k where cos

## Adiabatic state preparation

We can use quantum phase estimation [16] to measure the eigenvalues of U W . In particular, we want this measurement to be sufficiently accurate to resolve the eigenvalue θ = 0, or equivalently λ k = 1, from the rest of the spectrum. Assuming that the initial state is supported on the subspace E 0 , the spectral gap of U W is δ = θ 1 = arccos(λ 1 ) = arccos(1 -∆) ∼ √ ∆, so we only need about 1/ √ ∆ applications of U W to realize that measurement. This is quadratically faster than the classical mixing time 1/∆, which is the origin of the quadratic quantum speed-up.

A measurement outcome corresponding to θ = 0 would produce the coherent stationary distribution |π ⊗ |0 :=

We can verify that this condition holds for |ψ = |π :

where we have used detailed balance Eq. (1) in the second step and x W xy = 1 in the last step.

From an initial state |ψ ⊗ |0 = k α k |γ k , the probability of that measurement outcome is

Therefore, the initial state |ψ must be chosen with a large overlap with the fixed point to ensure that this measurement outcome has a non-negligible chance of success. If no such state can be efficiently prepared, one can use adiabatic state preparation [1,9] to increase the success probability. In its discrete formulation [27] inspired by the quantum Zeno effect, we can choose a sequence of random walks W 0 , W 1 , . . . W L = W with coherent stationary distributions |π j . The walks are chosen such that |π 0 is easy to prepare and consecutive walks are nearly identical, so that | π j |π j+1 | 2 ≥ 1 -1 L [27]. Thus, the sequence of L measurements of the eigenstate of the corresponding quantum walk operators U W j all yield the outcomes θ = 0 with probability (1 -1 L ) L ∼ 1 e , which results in the desired state. The overall complexity of this al-gorithm is

where δ j is the spectral gap of the j-th quantized walk W j and C is the time required to implement a single quantum walk operator.

## Metropolis-Hastings Algorithm

The Metropolis-Hastings algorithm [12,23] uses a special class of Markov chains which obey detailed balance Eq. (1) by construction. The basic idea is to break the calculation of the transition probability x → y in two steps. First, a transition from x to y = x is proposed with probability T yx . Then, this transition is accepted with probability A yx and otherwise rejected, in which case, the state remains x. The overall transition probability is thus

The detailed balance condition Eq. (1) becomes

which in the Metropolis-Hastings algorithm is solved with the choice

We note that our quantum algorithm can also be applied to the Glauber, or heat-bath, choice [10,30]

The Metropolis-Hastings algorithm is widely used to generate a Boltzmann distribution with applications in statistical physics and machine learning. Given a real energy function E(x) on the configuration space X, the Boltzmann distribution at inverse temperature β is defined as x) where the partition function Z(β) ensures normalization. In this setting, it is common practice to choose a symmetric proposed transition probability T yx = T xy , so the acceptance probability depends only on the energy difference

Note that the Metropolis-Hastings algorithm can be applied to quantum mechanical Hamiltonians [29], where it can also benefit from a quadratic speed-up using Szegedy's quantization procedure [31].

# Circuit for Walk operator

Quantum algorithms built from quantization of classical walks [2,21,27,28] usually assume an oracle formulation of the walk operator, where the ability to implement the transformation W of Eq. ( 2) is taken for granted. As we discuss below in Appendix A, this transformation requires costly arithmetic operations. One of the key innovations of this article is to provide a detailed and simplified implementation of a walk operator along with a detailed cost analysis of Metropolis-Hastings walks. As it will become apparent, our implementation circumvents the use of W altogether.

For concreteness, we will assume a (k, d)-local Ising model, where X = {+1, -1} n , and the energy function takes the simple form

where Ω are subsets of at most k Ising spins, J are real coupling constants where ranges over all the possible couplings (from 1 to nd k ), and each spin interacts with at most d other spins. Note that for k = 2 and d ≥ 3, finding the ground state is an NP-hard problem [3].

As it is always the case for Ising models, we will assume that the proposed transitions of the Metropolis-Hastings walk are obtained by choosing a random set of spins and inverting their signs. In other words, T yx = f (x • y) where the product is taken bit by bit and where f (z) is some simple probability distribution on X -{1 n } (it does not contain a trivial move), so T yx is clearly symmetric. The distribution f (z) is sparse, in the sense that it has only N ∈ O(n) non-zero entries.

For concreteness, we will suppose that f is uniform over some set M of moves, with |M| = N :

The most common example consists of single-spin moves, where a single spin is chosen uniformly at random to be flipped. More generally, we will suppose that moves are sparse in the sense that each move z j ∈ M flips a constant-bounded number of spins and that each spin belongs to a constant-bounded number of different moves.

For j = 1, 2, . . . N , we use f (j) as a shorthand for f (z j ). With a further abuse of notation, we view z j ∈ M both as Ising spin configurations and as subsets of [n], where the correspondence is given by the locations of -1 spins in z j .

A direct implementation of the unitary W generally requires costly quantum circuits involving arithmetic operations. The complexity arises from the need to uncompute a move register and a Boltzmann coin when implementing W . This turns out to be non-trivial and costly if a move is rejected. Consequently, we do not implement W , but instead present a circuit which is isometric to the entire walk operator U W , thus avoiding the problem. In other words, we construct a circuit for

To minimize circuit depth, the second register above is encoded in a unary representation, so it contains N qubits and |z is encoded as |00 . . . 0100 . . . with a 1 at the z-th position.

Since the state is already encoded in N qubits, unary encoding adds only a small multiplicative number of qubits compared to binary encoding. In addition to these two registers, the circuit acts on an additional coin qubit. Thus, we will denote the System, Move, and Coin registers with corresponding subscripts |x S |z M |b C , and they contain n, N , and 1 qubits respectively. Our implementation of the walk operator combines four components:

where

While these definitions differ slightly from the ones of Sec. 1.1, it can be verified straightforwardly that these realize the desired walk operator, similar to our discussion in Sec. 1.1. In what follows, we provide a complete description of each of these components, and their complexity is summarized in Table 1.

## Move preparation V

Recall that the Move register is encoded in unary. For a general distribution f , the method of [26] can be adapted to realize the transformation Eq. (26). Here, we focus on the case of a uniform distribution.

To begin, suppose that N is a power of 2. Starting in the state |000 . . . 01 M , the state 1 N j |j M (in unary) is obtained by applying a sequence of N gates √ SWAP in a binary-tree fashion. To see this, recall that

# The gate

√ SWAP is in the third level of the Clifford hierarchy, so it can be implemented exactly using a constant number of T gates. This represents a substantial savings compared to the method of [26] for a general distributions which requires arbitrary rotations obtained from costly gate synthesis.

When N is not a power of 2, in order to avoid costly rotations, we choose to pad the distribution with additional states and prepare a distribution 1 2 2 j |j M where = log 2 N . The states j = 1, 2, . . . N encode the N moves M of the classical walk x → y = x • z j , while the additional states j > N correspond to trivial moves x → x. This padding has the effect of slowing down the classical walk by a factor 2 /N < 2, and hence the quantum walk by a factor less than √ 2, which is less than the additional cost of preparing a uniform distribution over a range which is not a power of 2.

## Spin flip F

The operator F of Eq. (28) flips a set of system spins z j conditioned on the coin qubit and on the j-th qubit of the move register being in state 1. This can be implemented with at most N c Toffoli gates (controlled-controlled-NOT), where the constant c upper-bounds the number of spins that are flipped by a single move of M. The coin register acts as one control for each gate, the j-th bit of the move register acts as the other control, and the targets are the system register qubits that are in z j , for j = 1, 2, . . . N . No gate is applied to the padding qubits j > N .

This implementation has the disadvantage of being purely sequential. An alternative implementation uses O(N ) additional scratchpad qubits but is entirely parallel. The details of the implementation depends on the sparsity of the moves M, and in general there is a tradeoff between the scratchpad size and the circuit depth. When the moves consist of single-spin flips for instance, this uses N CNOTs in a binary-tree fashion (depth log 2 N ) to make N copies of the coin qubit. The Toffoli gates can then be applied in parallel for each move, and lastly the CNOTs are undone.

## Reflection R

The transformation R of Eq. ( 29) is a reflection about the state |00 . . . 0 M |0 C . Using standard phase kickback methods, it can be implemented with a single additional qubit in state

) and an open-control (N +1) -NOT gate. The latter can be realized from 4(N -1) serial Toffoli gates [4] and linear depth.

Since our goal is to minimize circuit depth, we use a different circuit layout that uses at most N ancillary qubits and 4N Toffoli gates to realize the (N + 1)-fold controlled-not. The circuit once again proceeds in a binary tree fashion, dividing the set of N + 1 qubits into (N + 1)/2 pairs and applying a Toffoli gate between every pair with a fresh ancilla in state 0 as the target. The ancillary qubit associated to a given pair is in state 0 if and only if both qubits of the pair are in state 0. The procedure is repeated for the (N + 1)/2 ancillary qubits, until a single bit indicates if all qubits are in state 0. The ancillary bits are then uncomputed. Thus, the total depth in terms of gates in 3rd level of the Clifford hierarchy is 2 log 2 N .

## Boltzmann coin B

The Boltzmann coin given in Eq. ( 27) is the most expensive component of the algorithm, simply because it is the only component which requires rotations by arbitrary angles. Specifically, conditioned on move qubit j being 1 and the system register being in state x, the coin register under-

# 3L count

Total depth Qubits goes a rotation by an angle

for Metropolis-Hastings or

for Glauber dynamics, where

Given the sparsity constraints of the function E and of the moves z j ∈ M, the quantity ∆ j can actually be evaluated from a subset of qubits of the system register, namely Thus, the Boltzmann coin consists of a sequence of N conditional gates R j , where R j itself is a single-qubit rotation by an angle determined by the qubits in the set N j . Since each N j is of constant-bounded size, each R j can be realized from a constant number of T gates, so the entire Boltzmann coin requires O(N log 1 ) T gates, where is the desired accuracy for the synthesis of single-qubits rotations. It is likely that a high precision is needed to ensure the detailed balance condition. We leave for future research the numerical investigation of how low the precision can be without causing significant errors.

Because all gates R j act on the Coin register, they must be applied sequentially. An alternative consists in copying the Coin register in the conjugate basis of σ y , i.e. | ± i → | ± i ⊗N since a sequence of rotations e iθ j σx is equivalent to a tensor product of these rotations under this mapping. Moreover, any set of gates R j with nonoverlapping N j can be executed in parallel. Consequently, the total depth can be bounded by a constant at the expense of N additional qubits.

The complexity of the Boltzmann coin does scale exponentially with the sparsity parameters of the model however, namely as O(max j 2 |N j | ). A circuit that achieves R j consists of a sequence of 2 |N j | single-qubit rotations by an angle given by Eq. (30) or Eq. (31), conditioned on the bits in N j taking some fixed value. Each of these 2 |N j | multi-controlled rotations require O(|N j |) Toffoli gates along with O(log 1 ) T gates, for an overall circuit depth of O(2

Perhaps a more efficient way to realize the Boltzmann coin uses quantum signal processing methods [11,[18][19][20]. This is a method to construct a unitary transformation S 2 =

x f (e iφx )|x x| from a controlled version of S 1 = x e iφx |x x|. In the current setting, S 1 = x e λi∆ j (x) |x x| and we choose f (e iλ∆ j (x) ) = e i2θ x,j where θ x,j is given at Eq. (30). Applying a Hadamard to the Coin qubit, followed by a controlled S 2 with the Coin acting as control, and followed by a Hadamard on the Coin qubit again results in the transformation that we called R j above and that builds up the Boltzmann coin transformation B.

Above, the constant λ is chosen in such a way that the argument of the exponential e iλ∆ j (x) is restricted to some finite interval which does not span the entire unit circle, say in the range [-π/2, π/2]. The exponential can be further decomposed as a product

Each of these factors is a rotation by an angle 2J , whose sign is conditioned on the parity of the bits in λΩ . The parity bit can be computed using |Ω | CNOTs, and the rotation is implemented using gate synthesis, with a T -gate count per transformation of O(log 1 ), which is dictated by the accuracy . The complexity of quantum signal processing depends on the targeted accuracy. More precisely, it scales with the number of Fourier coefficients required to approximate the function f (e iθ ) = min(1, e -θβ/λ ) or g(e iθ ) = Quantum signal processing, or alternative methods, will offer an advantage on some models, when there are different couplings and a high number of body interactions for example. The scaling of these methods is case dependent. Indeed, it will highly depend on these couplings and the number of spin flips z j .

# Heuristic use

The Metropolis-Hastings algorithm is widely used heuristically to solve minimization problems using simulated annealing or related algorithms [15]. The objective function is the energy E(x). Starting from a random configuration or an informed guess, the random walk is applied until some low-energy configuration x is reached. The parameter β can be varied in time, with an initial low value enabling large energy fluctuations to prevent the algorithm from getting trapped in local minimums, and large final value to reach a good (perhaps local) minimum.

In this section, we propose heuristic ways to use the quantum walk in the context of a minimization problem. We first recall the concept of total time to solution [24] which we use to benchmark and compare different heuristics. We then present two quantum heuristics which we compare using numerical simulations on small instances.

Since the purpose of our study is to compare a classical walk to its different quantum incarnations -as opposed to optimizing a classical walk -we will use a schedule with a linearly increasing value of β in time up to a fixed final value of β in our comparison and expect our conclusions to hold if an optimized β schedule was used instead in both the classical and the quantum walks.

## Total time to solution

When a random walk is used to minimize some function E(x), the minimum x * is only reached with some finite probability p. Starting from some distribution q(x) and applying the walk W sequentially t times, the success probability is p(t) = (W t q)(x * ). To boost this probability to some constant value 1 -δ, it is sufficient to repeat the procedure L = log (1-δ)  log(1-p(t)) times. The total time to solution is then defined as the duration of the walk t times the number of repetitions L,

There is a compromise to be reached between the duration of the walk t and the success probability p(t) -longer walks can reach a higher success probability and therefore be repeated fewer times, but increasing the duration t of the walk beyond a certain point has a negligible impact on its success probability p(t). We thus define the minimum total time to solution as min(TTS) = min t TTS(t).

## Zeno with rewind

In Sec. 1.2, we explained how to prepare the eigenstate of U W with eigenvalue 1 using a sequence of walks W 0 , W 1 , . . . , W L = W. In the setting of Metropolis-Hastings where W is the walk with parameter β, a natural choice of W j is given by β j = j L β. An optimized β schedule is also possible, but for a systematic comparison with the classical walk, we choose this fixed schedule, whose only parameter is the number of steps L.

Let us revisit the argument of Sec. 1.2 to establish some notation. Define the binary projective measurement {Q j , Q ⊥ j } := {|π j π j |, I -|π j π j |}. This binary measurement can be realized from 1 δ j uses of U W j , where δ j denotes the spectral gap of U W j . Starting from the state |π 0 , the Zeno algorithm consists in performing the sequence of binary measurements {Q j , Q ⊥ j } in increasing value of j. The outcome Q j on state |π j-1 yields state |π j and occurs with probability F 2 j := | π j-1 |π j | 2 . The sequence of measurements succeeds if they all yield this outcome, which occurs with probability L j=1 F 2 j and requires L j=1 1 δ j applications of quantum walk operator. For the algorithm to be successful, the final measurement in the computational basis must also yield the optimal outcome x * , which occurs with probability π L (x * ). Thus, the total time to solution for an L-step algorithm is

(34) In the method outlined above, a measurement outcome Q ⊥ j requires a complete restart of the algorithm to β = 0. There exists an alternative to a complete restart which we call rewind. It was first described in the context of Zeno state preparation in Ref. [17], but originates from Refs. [22,29]. It consists of iterating between the measurements

Given the cost 1 δ j of each of these measurements, we obtain a simple recursion relation for the expected cost of a successful |π j-1 → |π j transition with rewind, and thus for the total time to solution for a L-step Zeno protocol with rewind. The minimal total time to solution is obtained by minimizing over L. In Ref. [17], it was found that rewinding yields substantial savings compared to the regular Zeno strategy for the preparation of quantum many-body ground states.

## Unitary implementation

We propose another heuristic use of the quantum walk which does not use measurement. Starting from state |π 0 , it consists in applying the quantum walk operators U W j sequentially, resulting in the state

and ending with a computational basis measurement. The algorithm is successful if a computational basis measurement yields the outcome x * on state |ψ(L) (rewind could be used otherwise), so the total time to solution for the L-step algorithm is

.

(36) While we do not have a solid justification for this heuristic use, in Ref. [7], a protocol was proposed which used a similar sequence of unitaries, but where each unitary was applied a random number of times. The motivation for these randomized transformations was to phase randomize in the eigenbasis of the instantaneous unitary operator. When the spectral gap of a unitary operator is δ and that unitary is applied a random number of times in the interval [0, 1 δ j ], then the relative phase between the eigenstate with eigenvalue 1 and the other eigenstates is randomized over the unit circle, thus mimicking the effect of a measurement (but with an unknown outcome). From this analogy, we could expect that the unitary implementation yields a minimal total time to solution roughly equal to the Zeno-based algorithm with no rewind. But as we will see in the next section, its behavior is much better than anticipated -this method is more efficient than the Zeno algorithm with rewind, which itself is more efficient than Zeno without rewind.

## Numerical results

We have numerically benchmarked three heuristic algorithms: the classical walk with a variablelength linear interpolation between β = 0 and β = 2 and starting from a uniform distribution; the discrete, or Zeno-based adiabatic algorithm with rewind; and the unitary algorithm of the last subsection. The first system considered is a one dimensional Ising model. Figure 1 shows the quantum versus classical minimal total time to solution. The results clearly indicate a polynomial advantage of the quantum algorithms over the classical algorithm. Surprisingly, both quantum approaches show a similar improvement over the classical approach that exceed the expected quadratic speedup, with a power law fit of 0.42 using the unitary algorithm and 0.39 using the Zeno algorithm.

The second system considered is a sparse random Ising model: it has gaussian random couplings J of variance 1, and the interactions sets Ω (c.f. Eq. (32)) consist of a random subset of 3.5n of all the n(n -1)/2 pairs of sites. Figure 2 shows quantum versus classical minimum total time to solution for a random ensemble of 100 systems of each sizes n = 4 to 14. We observe that the unitary algorithm is consistently faster than the classical algorithm, with an average polynomial speedup of degree 0.75, less than the expected quadratic gain. Moreover, the different problem instances are all quite clustered around this average behavior, suggesting that the quantum speedup is fairly general and consistent. In contrast the Zeno algorithm shows large fluctuations about its average, particularly on very small problem instances. The average polynomial speedup is of degree 0.92, far worse than the unitary algorithm. Overall, the results indicate a polynomial advantage of the quantum methods over the classical method, but these advantages are much less pronounced than for the 1D Ising model.

In both the one-dimensional and the random graph Ising model, the unitary quantum algorithm achieves very similar and sometimes superior scaling to the Zeno with rewind algorithm. This is surprising given the observed improvement obtained from rewind in Ref. [17] and our expectation that the unitary algorithm behaves essentially like Zeno without rewind.

# Discussion

Our conclusion, and perhaps one of the key messages of this Article, is that even though the quantum walk is traditionally defined with the help of a walk oracle, its circuit implementation does not necessarily require it, and this can lead to substantial savings. In Appendix A, we discuss the difficulty of implementing the quantum walk unitary W . Appendix B presents an improved parallelized heuristic classical walk for discrete sparse optimization problems which could potentially lead to significant improvements on a quan- tum computer. Unfortunately this walk is not reversible, which motivates further generalization of Szegedy's quantization to include irreversible classical walks. In the rest of this section, we discuss the prospect of using the quantum walk to outperform a classical supercomputer.

We have proposed heuristic quantum algorithms based on the Szegedy walk for solving discrete optimization problems. Theoretical bounds show that the quantum algorithm can benefit from a quadratic speed-up (x 0.5 ) over its classical counterpart. Our numerical simulations on small problem instances indicate a superquadratic speed-up (≈ x 0.42 ) for the Ising chain, see figure 1, and sub-quadratic speed-up (≈ x 0.75 ) for random sparse Ising graphs, see figure 2. It remains an interesting question to understand more broadly what type of problems can benefit from what range of speed-up and why. With these crude estimates in hand we can already look into the achievability of a quantum speed-up on realistic devices.

We will compare performances to the specialpurpose supercomputer "Janus" [13,14] which consists of a massive parallel field-programmable gate array (FPGA). This system is capable of performing 10 12 Markov chain spin updates per second on a three-dimensional Ising spin glass of size n = 80 3 . A calculation that lasts a bit less than a month will thus realize 10 18 Monte Carlo steps. On the one hand, assuming that the theoretically predicted quadratic speed-up holds and since the numerics show a constant factor around 1, the quantum computer must realize at least 10 9 steps per month in order to keep up with the classical computer. This requires that a single step of the quantum walk be realized in a few milliseconds. On the other hand, the super-quadratic speed-up we have observed would allow almost a tenth of a second to realize a single quantum step, while the sub-quadratic speed-up would require that a single step be realized within 0.1 microseconds.

Taking the circuit depth reported in Table 1 as reference with d = 6 for a three-dimensional lattice leads to a circuit depth of log( 803 ) × 2 6 ≈ 1000. To avoid harmful error accumulation, the gate synthesis accuracy should be chosen as the inverse volume (circuit depth times the number of qubits) of the quantum circuit, roughly -1 ≈ 80 3 × log(80 3 ) × 10 9 ≈ 10 16 , so on the order of 4 log 1 ≈ 200 logical T gates are required per fine-tuned rotation [5,25], for a total logical circuit depth of 200,000. With these estimates, the three scenarios described above require logical gate speeds ranging from an unrealistically short 0.5 picoseconds (sub-quadratic speed-up), to an extremely challenging 1 nanosecond (quadratic speed-up), and allow 0.5 microseconds (superquadratic speed-up).

We could instead compile the rotations offline and teleport them in the computation [8], which requires at least 4 log 1 ≈ 200 more qubits, but increases the time available for a logical gate by the same factor. Under this scenario, the time required for each logical gate would range from 0.1 nanoseconds (sub-quadratic speed-up), to 20 microseconds (quadratic speed-up), and to 1 miliseconds (super-quadratic speed-up). These estimates are summarized in Table 2. The latter is a realistic logical gate time for many qubit architectures, while there is no current path to achieve nanosecond logical gate times.

Given the above analysis, if a quantum computer is to offer a practical speed-up, we conclude that a better understanding of the class of problems for which heuristic super-quadratic speedups can be achieved is required, and that we need to optimize circuit implementations even further.

# Quantum speedup Synthesis online Synthesis offline

Sub-quadratic x 0.75 0.5ps 0.1ns Quadratic x 0.5 1ns 20µs Super-quadratic x 0.42 0.5µs 1ms 

# A Walk oracle

Our implementation of the walk operator does not make use of the walk unitary W of Eq. (2). Since the transition matrix elements W xy can be computed efficiently, we know that W can be implemented in polynomial time. But this requires costly arithmetics which would yield a substantially larger complexity than the approach presented above. To see how this complexity arises, consider the following implementation of W , which uses much of the same elements as introduced above. The computer comprises two copies of the system register, which we now label Left and Right. As before, it also comprises a Move register and a Coin register. Begin with the Left register in state x and all other registers in state 0. 

Using a version of the Boltzmann coin transformation on the Left, Right and Coin register yields

At this point, we swap the Left and Right registers conditioned on the Coin qubit being in state 1, resulting in the state

Finally, reset the move register to 0 using 2N CNOTS with controls from the Left and Right registers. At this point, the move register is disentangled and discarded, resulting in the state

The relative weights of the two branches are the same as the classical MCMC methods, which corresponds to an acceptance rate of approximately 1/2. This is quite similar to the state that would result from the quantum walk operator W of Eq. (2), save for one detail. When the acceptance register is in state 0, the state y =x f (x • y)(1 -A yx )|y R of the right register needs to be mapped to the state √ W xx |x R . Such a rotation clearly depends on all the coefficients A yx , and all implementations we could envision used arithmetic operations that compute A xy .

# B Irreversible parallel walk

Note that the Boltzmann operator B has a total number of gates that scales with the system size n, even though it is used to implement a single step of the quantum walk and that on average, a single spin is modified per step of the walk. This contrasts with the classical walk where in a single step of W, a spin transition x → x • z is chosen with probability f (z), the acceptance probability is computed, and the move is either accepted or rejected. Each transition x → x • z typically involves only a few spins (one in the setting we are currently considering), so implementing such a transition in the classical walk does not require an extensive number of gates. The complexity in that case is actually dominated by the generation of a pseudo-random number selecting the location of the spin to be flipped. As a consequence, the quantum algorithm suffers an n-fold complexity increase compared to the quantum algorithm.

This motivates the construction of a modified classical walk for the lattice spin model which also affects every spin of the lattice, putting the classical and quantum walks on equal footing in terms of gate count. For simplicity, suppose that the set of moves z i ∈ M consist in single-spin flips. We define a parallel classical walk with transition matrix

where

} and z i is the transition which consists of flipping the ith spin only, so only spin i differ in x and x • z i . The variable 0 ≤ q ≤ 1 is a tunable parameter of the walk.

In other words, a single step of this walk can be decomposed into a sequence over spins i, and consists of flipping i with probability q and accepting the flip with probability

Importantly, even if the moves are applied sequentially, the acceptance probability B i (x) is always evaluated relative to the state at the beginning of the step, even though other spins could have become flipped during the sequence. If instead the acceptance probability was evaluated conditioned on the previously accepted movesi.e. B i (x) = min{1, e β[E(x•z tot i )-E(x•z i )] } where z tot i is the total transition accumulated up to step ithen this acceptance probability would be the same as used in the Metropolis-Hastings algorithm. Note that for a local spin model with, e.g., nearest-neighbor interactions, the two acceptance probabilities only differ if a neighbor of site i has been flipped prior to attempting to flip spin i. Because a transition on each spin is proposed with probability q, the probability of having two neighboring spins flipped is O(q 2 ). Thus, we essentially expect a single step of this modified walk to behave like qn steps of the original Metropolis-Hastings walk, with a systematic error that scales like nq 2 . Moreover, this systematic error is expected to decrease over time since once the walk settles in a low-energy configuration, very few spin transitions will turn out to be accepted, thus further decreasing the probability of a neighboring pair of spin flips.

To verify the above expectation, we have performed numerical simulations on an Ising model

where J i,j were randomly chosen from {+1, -1}. Results are shown on Fig. 3. What we observe is that, for an equal amount of computational resources, the parallelized walk outperforms the original walk. This is true both in terms in reaching a quick pseudo minimum configuration at short times and in terms of reaching the true minimum at longer times. Thus, while this parallelization was introduced to ease the quantization procedure, it appears to be of interest on its own. In this case, the quantum walk unitary W can easily be applied. We first proceed as in the previous subsection and use CNOTs to copy the Right register onto the Left register, yielding state |x L ⊗ |x R . Then, sequentially over all spins i, apply a rotation to spin i of the Left register conditioned on the state of the spin i and its neighbors on the Right register. This rotation transforms |x i → 1 -qB i (x)|x i + qB i (x)|x i . Note that the function B i (x) only depends on the bits of x that are . The temperature was set to β = 3, so the fixed point should be a low energy state. Since each step of the parallelized classical walk requires n = 500 times as many gates as the original walk, the time label of the parallel walk has been multiplied by n so it adequately represent the number of computational resources. The parallel walk with q < 1 outperforms the original walk at long times (see inset with first 150,000 steps) and achieves similar performances at short times as q approaches 1.

adjacent to site i, so this rotation acts on a constant number of spins so requires a constant number of gates. Thus, the cost of the classical and the quantum parallel walks have the same scaling in n. Combined to its observed advantages over the original classical walk, the parallel walk thus appears as the ideal version for a quantum implementation.

Unfortunately, the parallel walk is not reversible -it does not obey the detailed-balance condition Eq. (1). Thus, it is not directly suitable to quantization à la Szegedy. While quantization of nonreversible walks were considered in [21], they require an implementation of time-reversed Markov chain W * defined from W and its fixed point π as

Unfortunately, we do not know how to efficiently implement a quantum circuit for the time-reversed walk W * , so at present we are unable to quantize this parallel walk.

# Acknowledgements

We thank Jeongwan Haah, Thomas Häner, Matt Hastings, Guang Hao Low and Guillaume Duclos-Cianci for stimulating discussions. JL acknowledges support from the FRQNT programs of scholarships.

