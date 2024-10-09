# DESCRIPTION

## FIELD

This application concerns quantum computing.

## SUMMARY

In this disclosure, example circuit implementations of Szegedy's quantization of the Metropolis-Hastings walk are presented. This quantum walk is usually defined with respect to an oracle. A direct implementation of this oracle requires costly arithmetic operations. As discussed herein, and in accordance with the disclosed technology, the quantum walk can be reformulated in a way that circumvents the problems of any previous approach. Also disclosed herein are heuristic quantum algorithms that, use the quantum walk in the context, of discrete optimization problems. Numerous studies of the resulting performances are also presented. The numerical results indicate polynomial quantum speedups in heuristic settings.

In certain disclosed embodiments, a quantum walk procedure of a Markov chain Monte Carlo simulation is implemented in which a quantum move register is reset, at every step in the quantum walk. In further embodiments, a quantum walk procedure of a Markov chain Monte Carlo simulation is implemented in which an underlying classical walk is obtained using a Metropolis-Hastings rotation or a Glauber dynamics rotation. In some embodiments, a quantum walk procedure is performed in the quantum computing device to implement a Markov Chain Monte Carlo method: during the quantum walk procedure, an intermediate measurement is obtained: and a rewinding procedure of one or more but not, all steps of the quantum walk procedure is performed if the intermediate measurement, produces an incorrect outcome.

Any of the disclosed embodiments can be performed by one or more computer-readable media storing computer-executable instructions which when executed by a computer cause the computer to perform any of the disclosed methods.

Any of the disclosed embodiments can also be implemented in a system, comprising a quantum computing device; and a classical computer in communication with and configured to control the quantum computing device, wherein the quantum computing device and the classical computer collectively operate to perform any of the disclosed methods.

## DETAILED DESCRIPTION

### I. Introduction

The disclosed technology involves the issue of accelerating Markov chain Monte Carlo (MCMC) simulations on a quantum computer using quantum walks. More generally, MCMC simulations are used in sampling from arbitrary distributions, Gibbs sampling, optimization, simulated annealing, and related methods. Quantum computers accelerate MCMC simulations by implementing them as quantum walks. In order to accomplish this acceleration, a Markov transition matrix is desirably implemented in embodiments of the disclosed technology as a walk oracle.

Embodiments of the disclosed technology concern the implementation of such oracles for accelerating MCMC algorithms in which the random walk might stay at the same location in one time step. Detailed example implementations of such oracles have heretofore been unknown. This disclosure presents examples that provide efficient ways to implement, such oracles. This allows for acceleration of MCMC simulations on quantum computers

In some embodiments, a notable aspect of the technology is how to efficiently implement a quantum walk oracle of an MCMC algorithm to accelerate the random walk as a quantum walk. Choosing a random move in a quantum walk uses a random choice, which turns into a quantum move register in the quantum walk case. This quantum move register can be uncorrupted (reset) at every step in the quantum walk, which is not efficiently possible in previous naive solutions.

A further issue that, the disclosed technology addresses is a quantum walk for states where updates are rejected—that is, one stays in the original state. Previous solutions follow the original mathematical proposal and need to undo the proposed update in that case. In certain embodiments of the disclosed technology, however, this expensive step can be omitted by an operation controlled by a coin register in the case of rejected moves.

### II. General Considerations

As used in this application, the singular forms “a,” “an,” and “the” include the plural forms unless the context clearly dictates otherwise. Additionally, the term “includes” means “comprises.” Further, the term “coupled” does not exclude the presence of intermediate elements between the coupled items. Further, as used herein, the term “and/or” means any one item or combination of any items in the phrase.

Although the operations of some of the disclosed methods are described in a particular, sequential order for convenient presentation, it should be understood that this manner of description encompasses rearrangement, unless a particular ordering is required by specific language set forth below. For example, operations described sequentially may in some cases be rearranged or performed concurrently. Moreover, for the sake of simplicity, the attached figures may not show the various ways in which the disclosed systems, methods, and apparatus can be used in conjunction with other systems, methods, and apparatus. Additionally, the description sometimes uses terms like “produce” and “provide” to describe the disclosed methods. These terms are high-level abstractions of the actual operations that are performed. The actual operations that correspond to these terms will vary depending on the particular implementation and are readily discernible by one of ordinary skill in the art.

### III. Example Embodiments

**A. Introduction**

Szegedy presented a general method to quantize reversible walks, resulting in a unitary transformation  (See, e.g., M. Szegedy, in Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science (2004).) The eigenvalues eiθj of a unitary matrix lie on the unit complex circle. One can choose θ0≤θ1≤θ2≤ . . . . In this example, the steady state |π of the quantum walk has θ0=0 and is essentially a coherent version |π=Σx √{square root over (πx)}x of the classical equilibrium distribution n. One of the main features of the quantum walk is that its spectral gap δ:=θ1≥√{square root over (Δ)} is quadratically larger than the one of the corresponding classical walk that would be Δ. Combined to the quantum adiabatic algorithm, this yields a quantum algorithm to reach the steady state that scales quadratically faster with Δ than the classical MCMC algorithm. (See, e.g., E. Farhi, J. Goldstone. S. Gutmann, and M. Sipser, “Quantum computation by adiabatic evolution,” (2000), quant-ph/0001106; D. Aharonov and A. Ta-Shma, Proc. 35th Annual ACM Symp, on Theo. Comp., 20 (2003); S. Boixo, E. Knill, and R. D. Somma, “Fast quantum algorithms for traversing paths of eigenstates,” (2010), 1005.3034; S. Boixo, E. Knill, and R. D. Somma. “Fast. quantumn algorithms for traversing paths of eigenstates,” (2010), 1005.3034.)

The time required to implement a single step U. of the quantum walk was traditionally large. With the disclosed technology, however, the time can be significantly reduced. Example quantum steps in accordance with the disclosed technology are shown as single steps W of the classical walk. With embodiments of the disclosed technology, quantum walks are more likely to offer advantages in situations with extremely long equilibration times. Moreover, classical walks are often used heuristically out of equilibrium. When training a neural network for instance, where a MCMC method called stochastic gradient is used to minimize a cost function, it is in practice often not necessary to reach the true minimum, and thus the MCMC runs in time less than its mixing time. Similarly, simulated annealing is typically used heuristically with a cooling schedule far faster than prescribed by provable bound. Such heuristic applications further motivate the constructions of efficient implementations of , and the development of heuristic methods for quantum computers.

This disclosure addresses several points. For example, a detailed realization and cost analysis of the quantum walk operator is presented for the special case of a Metropolis-Hastings walk and a Glauber walk. There are widespread reversible walk, whose implementation only requires knowledge of the relative populations πx/πy, of the equilibrium distribution. While Szegedy's formulation of the quantum walk builds on a classical walk oracle, it requires costly arithmetic operations. In this disclosure, example embodiments are presented in which one can directly construct a related but different quantum unitary walk operator with substantially reduced circuit depth.

**1. Quantum Walk Test**

A classical walk is defined on a d-dimensional state space X={x} by a d×d transition matrix  where the transition probability x→y is given by matrix element yx. Thus, the walk maps the distribution py to the distribution p′y=Σxyxpx, or in matrix form p′=p. A walk is ergodic or irreducible if every state in X is accessible from every other state in X, which implies the existence of a unique equilibrium distribution π=Wπ. Finally, a walk is reversible if it obeys the detailed balance condition

yxπx=xyπy.  (1)

One can now explain how to quantize an reversible classical walk .

Szegedy's quantum walk is formulated in an oracle setting. For a classical walk , it assumes a unitary transformation W acting on a Hilbert space d⊗d with the following action

W|x⊗|0=|wx⊗|x=:|ϕx,  (2)

where |wx:=Σy√{square root over (yx)}|y. Define Π0 the projector onto the subspace ε0 spanned by states {|x⊗|0}x=1d. Combining W to the reflection R=2Π0−1 and the swap operator Λ, one can construct the quantum walk defined by

\(\begin{matrix}
{U_{}:={{RW}^{\dagger}\Lambda \; W}} & {{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}(3)} \\
{= {\left( {2{\prod_{0}{- 1}}} \right)W^{\dagger}\Lambda \; {W.}}} & {(4)}
\end{matrix}\)

Szegedy's walk is actually defined as ΛW(RW†ΛW)RW†, so it is essentially the square of the operator U previously defined, but this will have no consequence on what follows aside from a minor simplification.

To analyze the quantum walk U, let one define the state |ψx:=Λ|ϕx=|x|wx and consider the operator

{ X :=  Π 0  W †  Λ   W   Π 0  ( 5 ) =  ∑ xy  〈 φ y
\textbar{} ψ x 〉   y 〉  〈 x  ⊗  0 〉  〈 0   ( 6 ) =  ∑ xy 
xy  yx   y 〉  〈 x  ⊗  0 〉  〈 0  .
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ( 7 ) }

At this point, it is assumed that the walk is reversible and makes use of the detailed balance condition Eq. (1) to obtain

{ X = ∑ xy  π x π y  yx   y 〉  〈 x  ⊗  0 〉  〈 0  , ( 8 ) }

or, if one restricts the operator X to its support ε0, one gets in matrix notation X=diag(π−1/2) diag(π1/2). The matrices X and  are thus similar so they have the same eigenvalues. Define its eigenvectors

X|{tilde over (γ)}k=λk|{tilde over (γ)}k,  (9)

where λk are the eigenvalues of W. Because the operator X is obtained by projecting the operator W†ΛW onto the subspace ε0, its eigenvectors with non-zero eigenvalues in the full Hilbert space clearly have the form |γk=|{tilde over (γ)}k⊗|0.

If one considers the action of W†ΛW without those projections, one gets

W†ΛW|γk=λk|γk−βk|γk⊥  (10)

where

\(\gamma_{k}^{\bot}\rangle\)

is orthogonal to the subspace ε0, so in particular it is orthogonal to all the vectors |γk′. Finally, because W†ΛW is a unitary, one also obtains that the

\(\gamma_{k}^{\bot}\rangle\)

are orthogonal to each other and that βk=√{square root over (1−|λk|2)}. This implies that the vectors

\(\left\{ {{\gamma_{k}\rangle},{\gamma_{k}^{\bot}\rangle}} \right\}\)

are all mutually orthogonal and that W†ΛW is block diagonal in that basis.

Given the above observations, it follows that

\(\begin{matrix}
{{{\gamma_{k}\rangle}} = {{\lambda_{k}{\gamma_{k}\rangle}} + {\sqrt{1 - {\lambda_{k}}^{2}}{\gamma_{k}^{\bot}\rangle}}}} & (11) \\
{{{{\gamma_{k}^{\bot}\rangle}} = {{\sqrt{1 - {\lambda_{k}}^{2}}{\gamma_{k}\rangle}} - {\lambda_{k}{\gamma_{k}^{\bot}\rangle}}}},} & (12)
\end{matrix}\)

so the eigenvalues of Uk on the subspace spanned by

\(\left\{ {{\gamma_{k}\rangle},{\gamma_{k}^{\bot}\rangle}} \right\}\)

are e±iθwhere cos θk=λk with corresponding eigenvectors

\({\gamma_{k}^{\pm}\rangle} = {\frac{1}{\sqrt{2}}{\left( {{\gamma_{k}\rangle} \pm {i{\gamma_{k}^{\bot}\rangle}}} \right).}}\)

**C. Adiabatic State Preparation**

One can use quantum phase estimation to measure the eigenvalue of . In particular, it is desirable for the measurement to be sufficiently accurate to resolve the eigenvalue θ=0, or equivalently λk=1, from the rest of the spectrum. Assuming that the initial state is supported on the subspace ε0, the spectral gap of U is δ=θ1=arccos(λ1)=arccos(1−Δ)˜√{square root over (Δ)}, so one only needs about 1/√{square root over (Δ)} applications of U to realize that measurement. This is quadratically faster than the classical mixing-time 1/Δ, which is at the heart of the quadratic quantum speed up.

A measurement outcome corresponding to θ=0 would produce the coherent stationary distribution |π⊗|0:=Σx√{square root over (πx)}⊗0. First note that for any |ψ such that X (|ψ⊗|0|0, Eq. (10) implies that U(|ψ|0)=|ψ⊗|0. One can verify that this condition holds for |ψ=|π:

{ X  ∑ x  π x   x 〉 ⊗  0 〉 =  ∑ xy  π x π y  yx  π y   y 〉
⊗  0 〉 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ( 13 ) =  ∑ xy  xy
 π y   y 〉 ⊗  0 〉  ( 14 ) =  ∑ y  π y   y 〉 ⊗  0 〉  ( 15
) }

where the detailed balance Eq. (1) has been used in the second step and Σxxy=1 in the last step.

From an initial state |ψ⊗0=Σkαk|γk, the probability of that measurement outcome is |ψ|π|2=α0|2, so the initial state |ψ can be chosen with a large overlap with the fixed point to ensure that this measurement outcome has a non-negligible chance of success. If no such state can be efficiently prepared, one can use adiabatic state preparation to increase the success probability. In its discrete formulation inspired by the quantum Zeno effect, one can choose a sequence of random walks 0, 1, . . . L= with coherent stationary distributions |πj. The walks are chosen such that |π0 is easy to prepare and consecutive walks are nearly identical, so that

\({{\langle\left. \pi^{j} \middle| \pi^{j + 1} \right.\rangle}}^{2} \geq {1 - {\frac{1}{L}.}}\)

Thus, the sequence of L measurements of the eigenstate of the corresponding quantum walk operators U, all yield the outcomes θ=0 with probability

\({\left( {1 - \frac{1}{L}} \right)^{L} \sim \frac{1}{e}},\)

which results in the desired state. The overall complexity of this algorithm is

\(\begin{matrix}
{C{\sum\limits_{j = 1}^{L}\frac{1}{\delta_{j}}}} & (16)
\end{matrix}\)

where δj is the spectral gap of the j-th quantized walk j and C is the time required to implement a single quantum walk operator.

**D. Metropolis-Hastings Algorithm**

The Metropolis-Hastings algorithm is a special class of Markov chains which obey detailed balance Eq. (1) by construction. The basic idea is to break the transition probability x→y into two steps. In a first step, a transition from x to y≠x is proposed with probability Tyx. This transition is accepted with probability Ayx, and if the transition is rejected the state remains x. The overall transition probability is thus

\(\begin{matrix}
{W_{yx} = \left\{ \begin{matrix}
{T_{yx}A_{yx}} & {{{if}\mspace{14mu} y} \neq x} \\
{1 - {\sum_{y}{T_{yx}A_{yx}}}} & {{{if}\mspace{14mu} y} = {x.}}
\end{matrix} \right.} & (17)
\end{matrix}\)

The detailed balance condition Eq. (1) becomes

\(\begin{matrix}
{{R_{xy}:={\frac{A_{yx}}{A_{xy}} = {\frac{\pi_{y}}{\pi_{x}}\frac{T_{xy}}{T_{yx}}}}},} & (18)
\end{matrix}\)

which in the Metropolis-Hastings algorithm is solved with the choice

Ayx=min(1,Rxy).  (19)

One can note that the quantum algorithm can also be applied to the Glauber. or heat-bath, choice

\(\begin{matrix}
{A_{yx} = {\frac{1}{1 + R_{yx}}.}} & (20)
\end{matrix}\)

The Metropolis-Hastings algorithm is widely used to generate a Boltzmann distribution as used in statistical physics and machine learning. Given a real energy function E(x) on the configuration space X, the Boltzmann distribution at inverse temperature β is defined as

\(\pi_{x}^{\beta} = {\frac{1}{Z(\beta)}e^{{- \beta}\; {E{(x)}}}}\)

where the partition function Z(β) ensures normalization. In this setting, it is common practice to choose a symmetrical proposed transition Tyx=Txy, so the acceptance probability depends on the energy difference

Ayx=min(1,eβ[|E(x)-E(y)]).  (21)

**E. Circuit for Walk Operator**

Quantum algorithms built from quanizatiation of classical walks usually assume an oracle formulation of the walk operator, where the ability to implement the transformation W of Eq. (2) is taken for granted. As is discussed below, this transformation requires costly arithmetic operations. One of the many innovations in this disclosure is to provide a detailed and simplified implementation of a walk operator along with a detailed cost analysis for Metropolis-Hastings walks. Some example embodiments of the disclosed technology circumvent the use of W altogether.

For concreteness, it will be assumed that a (k,d)-local Ising model, where X={+1, −1}n, and the energy function takes a simple form

\(\begin{matrix}
{{E(x)} = {\sum\limits_{}{J_{}{\prod\limits_{s \in \Omega_{}}\; x_{s}}}}} & (22)
\end{matrix}\)

where Ωl are subsets of at most k Ising spins and the Jl are real coupling constants, and each spin interacts with at most d other spins.

As is the case for Ising models, it will be assumed that the proposed transition of the Metropolis-Hastings walk is obtained by choosing a random set of spins and inverting their signs. In other words. Tyx=ƒ(x·y) where the product is taken bit, by bit and where ƒ(z) is a probability distribution on X−{1n} (it does not contain a trivial move), so Tyx is symmetrical. The distribution ƒ(z) is sparse, in the sense that it has only N<<2n non-zero entries.

It will be supposed that ƒ is uniform over some set M of moves, with ||=N:

\(\begin{matrix}
{T_{xy} = \left\{ {\begin{matrix}
\frac{1}{N} & {{{if}\mspace{14mu} z} = {{x \cdot y} \in \mathcal{M}}} \\
0 & {else}
\end{matrix}.} \right.} & (23)
\end{matrix}\)

One example comprises single-spin moves, where a single spin is chosen uniformly at random to be flipped. More generally, it will be supposed that moves are sparse in the sense that each move zj∈ flips a constant-bounded number of spins and that each spin belongs to a constant-bounded number of different moves zj∈. For j=1, 2, . . . , N, one can use ƒ(j) as a shorthand for ƒ(zj) where the zj are the N elements of . Here, zj∈ will be viewed as both as Ising spin configurations and as subsets of [n], where the correspondence is given by the locations of −1 spins in zj.

Because a direct implementation of the oracle W generally relies on costly quantum circuits realizing arithmetic operations, certain example embodiments of the disclosed technology do not implement W, but instead present circuits that are isometric to the entire walk operator . In particular implementations, example circuits are presented for :=Y†Y where Y maps

\(\begin{matrix}
{Y:\left. {{x\rangle} \otimes {y\rangle}}\rightarrow\left\{ \begin{matrix}
{{x\rangle} \otimes {{x \cdot y}\rangle}} & {{{if}\mspace{14mu} {x \cdot y}} \in \mathcal{M}} \\
0 & {{else}.}
\end{matrix} \right. \right.} & (24)
\end{matrix}\)

To reduce circuit depth, the second register above can be encoded in a unary representation, so it, contains N qubits and |z is encoded as |00 . . . 0100 . . .  with a 1 at the z-th position. In addition to these two registers, the circuit acts on an additional coin qubit. For purposes of illustration, the System, Move, and Coin registers will be denoted with the corresponding subscripts |xS|zM|b)C, and they contain n, N. and 1 qubits respectively.

Example implementation of the walk operator combine 4 components:

=RV†B†FBV  (25)

where

\(\begin{matrix}
{{V:\left. {0\rangle}_{M}\rightarrow{\sum\limits_{j}{\sqrt{f(j)}{j\rangle}_{M}}} \right.},} & (26) \\
{{B:\left. {{x\rangle}_{S}{j\rangle}_{M}{0\rangle}_{C}}\rightarrow{{x\rangle}_{S}{j\rangle}_{M}\left( {{\sqrt{1 - A_{{x \cdot z_{j}},x}}{0\rangle}} + {A_{{x \cdot z_{j}},x}{1\rangle}}} \right)_{C}} \right.},} & (27) \\
{{F:\left. {{x\rangle}_{S}{j\rangle}_{M}{b\rangle}_{C}}\rightarrow{{{x \cdot z_{j}^{b}}\rangle}s{j\rangle}_{M}{b\rangle}_{C}} \right.},{and}} & (28) \\
{{R:\left. {{0\rangle}_{M}{0\rangle}_{C}}\rightarrow{{- {0\rangle}_{M}}{0\rangle}_{C}} \right.},\left. {{j\rangle}_{M}{b\rangle}}\rightarrow{{{j\rangle}_{M}{b\rangle}\mspace{14mu} {for}\mspace{14mu} \left( {j,b} \right)} \neq \left( {0,0} \right)} \right.} & (29)
\end{matrix}\)

It can be verified that these realize the desired walk operator. The following paragraphs provide a more complete description of each of these components, and their complexity is summarized at Table I.

**1. Move Preparation V**

Recall that the Move register is encoded in unary. Here, the focus is on the case of a uniform distribution. To begin, suppose that N is a power of 2. Starting in the state |000 . . . 01M, the state

\(\frac{1}{N}{\sum_{j}{j\rangle}_{M}}\)

(in unary) is obtained by applying a sequence of N gates √{square root over (SWAP)} in a binary-tree fashion. Recall that

\({\sqrt{SWAP}{10\rangle}} = {\frac{1}{\sqrt{2}}{\left( {{01\rangle} + {10\rangle}} \right).}}\)

The gate √{square root over (SWAP)} is in the third level of the Clifford hierarchy, so it can be implemented using a constant number of T gates. This represents a substantial savings.

To avoid such costly rotations, even when N is not a power of 2, one can choose to pad the distribution with additional states and prepare a distribution

\(\frac{1}{2^{}}{\sum_{j}^{2^{}}{j\rangle}_{M}}\)

where ƒ=┌log2 N┐. The states j=1, 2, . . . N encode the N moves  of the classical walk x→y=x·zj, while the additional states j>N correspond to trivial moves x→x. This padding has the effect of slowing down the classical walk by a factor 2l/N<2, and hence the quantum walk by a factor less than √{square root over (2)}, which is less than the additional cost, of preparing a uniform distribution over a range which is not a power of 2.

**2. Spin Flip F**

The operator F of Eq. (28) flips a set of system spins zj conditioned on the j-th qubit of the move register being in state 1. This can be implemented with at most Nc Toffoli gates (control-control-not), where the constant c upper-bounds the number of spins that are flipped by a single move of . The coin register acts as one control for each gate, the j-th bit of the move register acts as the other control, and the targets are the system register qubits that are in zj, for j=1, 2, . . . N. No gate is applied to the padding qubits j>N.

This implementation is sequential, but can also be performed in parallel. In particular, one example implementation uses (N) additional scratchpad qubits but is parallel. In such implementations, the sparsity of the moves M can be considered, and (generally speaking) there is a tradeoff between the scratchpad size and the circuit depth. When the moves comprise single-spin flips, for example, this uses N CNOTs in a binary-tree fashion (depth log2 N) to make N copies of the coin qubit. The Toffoli gates can then be applied in parallel for each move, and lastly the CNOTs are undone.

**3. Reflection R**

The transformation R of Eq. (29) is a reflection about the state |00 . . . 0M|0C. Using standard phase kickback methods, it can be implemented with a single additional qubit in state

\(\frac{1}{\sqrt{2}}\left( {{0\rangle} - {1\rangle}} \right)\)

and a control(N+1)-not gate. The latter cart be realized from 4(N−1) serial Toffoli gates and linear depth.

In this disclosure, improved example circuit layouts are presented. In some examples, for instance, circuits that use at most N ancillary qubits and 4N Toffoli gates to realize the (N+1)-fold controlled-not. The circuit once again proceeds in a binary tree fashion, dividing the set of N+1 qubits into (N+1)/2 pairs and applying a Toffoli gate between every pair with a fresh ancilla in state 0 as the target. The ancillary associated to a given pair is in state 0 if and only if both qubits of the pair are in state 0. The procedure is repeated to the (N+1)/2 ancillary qubits, until a single bit indicates if all qubits are in state 0. The ancillary bits are then uncomputed.

**4. Boltzmann Coin B**

The Boltzmann coin Eq. (27) is an expensive component of the algorithm. In more detail, the Boltzmann coin is a component that desirably uses rotations of arbitrary angles. For example, conditioned on move qubit j being 1 and the system register being in state r, the coin register undergoes a rotation by an angle

θx,j=arcsin(√{square root over (min{e−βΔ(x),1})}  (30)

for Metropolis-Hastings or

\(\begin{matrix}
{\theta_{x,y} = {\arcsin \left( \frac{1}{1 + e^{{\beta\Delta}_{j}{(x)}}} \right)}} & (31)
\end{matrix}\)

for Glauber dynamics, where Δk=E(x·zj)−E(x). Given the sparsity constraints of the function E and of the moves zj∈, the quantity Δj can be evaluated from a subset of qubits of the system register, namely ={k: k∈Ωl&zj∩Ωl≠Ø, ∀l}. For single-spin flips on a (k,d)-local Hamiltonian. ||≤d by definition. For multi-spin flips zj, one can achieve ||≤|zj|d.

Thus, in such embodiments, the Boltzmann coin comprises a sequence of N conditional gates Rj, where Rj itself is a single-qubit rotation by an angle determined by the qubits in the set .

By contrast, example embodiments of the disclosed technology employ a new approach. Since each  are of constant-bounded sizes, and in accordance with example embodiments of the disclosed technology, each Rj can be realized from a constant number of T gates, so the entire Boltzmann coin can require

\(\left( {N\; \log \; \frac{1}{\epsilon}} \right)\)

T gates, where ε is the desired accuracy. In certain examples, because gates Rj act, on the Coin register, they are applied sequentially. An alternative to this comprises copying the coin register in the conjugate basis σy, i.e. |±i→|±i⊗N since a sequence of rotations eiθσis equivalent to a tensor product of these rotation under this mapping. Moreover, any set of gates Rj with non-overlapping  can be executed in parallel, so the total depth can be bounded by a constant at the expense of N additional qubits.

The complexity of the Boltzmann coin does scale exponentially with the sparsity parameters of the model—namely as (maxj 2). A circuit that achieves Rj comprises a sequence of 2|| single-qubit rotations by angle given by Eq. (30) or Eq. (31), conditioned on the bits in  taking some fixed value. These 2|| multi-controlled rotations typically use (||) Toffoli gates along with

\(\left( {\log \; \frac{1}{\epsilon}} \right)\)

T gates, for an overall circuit depth of

\(\left( {2^{_{j}}{_{j}}\log \; \frac{1}{\epsilon}} \right)\)

to realize Rj.

Another efficient way to realize the Boltzmann coin uses quantum signal processing methods. This is a method to constructs a unitary transformation S2=Σxƒ(eiϕ)|xx| from a controlled version of S1=Σxeiϕ|xx|. In the current setting. S1=ΣxeλiΔ(x)|xx| and one can choose ƒ(eiλΔ(x))=ei2θwhere θx,j is given at Eq. (30). Applying a Hadamard to the Coin qubit, followed by a controlled S2 with the Coin acting as control, and followed by a Hadamard on the Coin qubit again results in the transformation that we called Rj above and that, build up the Boltzmann coin transformation B.

Above, the constant λ is chosen in such a way that the argument of the exponential eiλΔ(x) is restricted to some finite interval which does not span the entire unit circle, say in the range [−π/2,π/2]. The exponential can be further decomposed as a product

\(\begin{matrix}
{e^{i\; {{\lambda\Delta}_{j}{(x)}}} = {\prod\limits_{\lambda:{{\Omega_{}\bigcap z_{j}} \neq \varnothing}}{\exp {\left\{ {i\; {\lambda 2}\; J_{}{\prod\limits_{s \in \Omega_{}}x_{s}}} \right\}.}}}} & (32)
\end{matrix}\)

Each of these components comprises a rotation by an angle 2Jl, whose sign is conditioned on the parity of the bits in Ωl. The parity bit can be computed using |Ωl| CNOTs, and the rotation is implemented using gate synthesis, with a T-gate count per transformation of

\({\left( {\log \; \frac{1}{\epsilon}} \right)},\)

which is dictated by the accuracy ∈. The complexity of quantum signal processing depends on the targeted accuracy. More precisely, it scales with the number of Fourier coefficients required to approximate the function ƒ(eiθ)=min(1,e−θβ/λ) or

\({g\left( e^{i\; \theta} \right)} = \frac{1}{1 + e^{{\theta\beta}/\lambda}}\)

to some constant accuracy on the domain θ∈[−π/2, π/2].

**F. Heuristic Use**

The Metropolis-Hastings algorithm is widely used heuristically to solve minimization problems using simulated annealing or related algorithms. The objective function is the energy E(x). Starting from a random configuration or an informed guess, the random walk is applied until some low-energy configuration x is reached. The parameter β can be varied in time, with an initial low value enabling large energy fluctuations to prevent the algorithm from getting trapped in local minimums, and large final value to reach a good (perhaps local) minimum.

In this section, example heuristics that use the quantum walk in the context of a minimization problem are introduced.

In certain example embodiments, schedules with a linearly increasing value of 3 in time are used up to a fixed final value of β.

**1. Total Time to Solution**

When a random walk is used to minimize some function E(x), the minimum x* is typically reached with some finite probability p. Starting from some distribution q(x) and applying the walk  sequentially t times, the success probability is p(t)=(tq)(x*). To boost this probability to some constant value 1−δ, it is helpful to repeat the procedure

\(L = \frac{\log \left( {1 - \delta} \right)}{\log \left( {1 - {p(t)}} \right)}\)

times. The total time to solution can then be defined as the duration of the walk t times the number of repetitions L,

In general, compromises can be reached between the duration of the walk t and the success probability p(t)—longer walks can reach a higher success probability and therefore be repeated fewer times, but increasing the duration t of the walk beyond a certain point has a negligible impact on its success probability p(t). Accordingly, and in some instances, one can define the minimum total time to solution as min(TTS)=mint TTS(t).

**2. Zeno with Rewind**

In zeno, it was explained how to prepare the eigenstate of U with eigenvalue 1 using a sequence of walks 0, 1, . . . , L=. In the setting of Metropolis-Hastings where  is the walk with parameter β, a natural choice of j are given by

\(\beta^{j} = {\frac{j}{L}{\beta.}}\)

An optimized β schedule is also possible, but for a systematic comparison with the classical walk, one can choose this fixed schedule, whose only parameter is the number of steps L.

Revisiting the argument of zeno it is helpful to establish some notation. Define the binary projective measurement

\(\left\{ {_{j},_{j}^{\bot}} \right\}:={\left\{ {{{\pi^{j}\rangle}{\langle\pi^{j}}},{I - {{\pi^{j}\rangle}{\langle\pi^{j}}}}} \right\}.}\)

This binary measurement can be realized from

\(\frac{1}{\delta_{j}}\)

uses of U, where δj denotes the spectral gap of U. Starting from the state |π0, the Zeno algorithm comprises performing the sequence of binary measurements {Qj, Qj⊥} in increasing value of j. The outcome Qj on state |πj-1 yields state |πj and occurs with probability Fj2:=|πj-1|πj2. The sequence of measurements succeeds if they all yield this outcome, which occurs with probability Πj=1LFj2 and requires

\(\sum\limits_{j = 1}^{L}\frac{1}{\delta_{j}}\)

applications of quantum walk operator. For the algorithm to be successful, the final measurement in the computational basis also yields the optimal outcome x*, which occurs with probability πL(x*). Thus, the total time to solution for an the L-step algorithm is

\(\begin{matrix}
{{{TTS}(L)} = {\frac{\log \left( {1 - \delta} \right)}{\log\left( {1 - {{\pi^{L}\left( x^{*} \right)}{\overset{L}{\prod\limits_{j = 1}}F_{j}^{2}}}} \right)}{\sum\limits_{j = 1}^{L}{\frac{1}{\delta_{j}}.}}}} & (33)
\end{matrix}\)

In the method outlined above, a measurement outcome Qj⊥ involves a complete restart of the algorithm to β=0. There exists an alternative to a complete restart, termed a “rewind”. It comprises iterating between the measurements

\(\left\{ {Q_{j - 1},Q_{j - 1}^{\bot}} \right\} \mspace{14mu} {and}\mspace{14mu} \left\{ {Q_{j},Q_{j}^{\bot}} \right\}\)

until the measurement Qj is obtained. It can be shown that a transition between outcomes Qj-1↔Qj or

\(\left. Q_{j - 1}^{\bot}\leftrightarrow Q_{j}^{\bot} \right.\)

is Fj2 while the probability of a transition between outcomes Qj-1⊥↔Qj or

\(\left. Q_{j - 1}\leftrightarrow Q_{j}^{\bot} \right.\)

is 1−Fj2. Given the cost

\(\frac{1}{\delta_{j}}\)

of each of these measurements, one can obtain a simple recursion relation for the expected cost of a successful |πj-1→|πj transition with rewind, and thus for the total time to solution for a L-Zeno protocol with rewind. The minimal total time to solution is obtained by minimizing over L. Rewinding yields substantial savings compared to the regular Zeno strategy for the preparation of quantum many-body ground states.

**3. Unitary Implementation**

In this section, a heuristic use of the quantum walk that does not use measurement is disclosed. Starting from state |π0, this embodiment comprises applying the quantum walk operators U, sequentially, resulting in the state

|ψ(L)= . . . |π0  (34)

and ending with a computational basis measurement. The algorithm is successful if a computational basis measurement yields the outcome x* on state |ψ(L) (rewind could be used otherwise), so the total time to solution for the L-step algorithm is

\(\begin{matrix}
{{{TTS}(L)} = {\frac{\log \left( {1 - \delta} \right)}{\log\left( {1 - {{{\langle x^{*}}U_{W^{L}}\mspace{14mu} \ldots \mspace{14mu} U_{W^{2}}U_{W^{1}}{\pi^{0}\rangle}}}^{2}} \right.}.}} & (35)
\end{matrix}\)

In S. Boixo, E. Knill, and R. D. Sonmma, “Fast quantum algorithms for traversing paths of eigenstates,” (2010), 1005.303-1, a protocol was proposed where each unitary was applied a random number of times. The motivation for these randomized transformations was to phase randomize in the eigenbasis of the instantaneous unitary operator. When the spectral gap of a unitary operator is 6 and that unitary is applied a random number of times in the interval

\(\left\lbrack {0,\frac{1}{\delta_{j}}} \right\rbrack,\)

then the relative phase between the eigenstate with eigenvalue 1 and the other eigenstates is randomized over the unit circle, thus mimicking the effect of a measurement (but with an unknown outcome). From this analogy, one could expect that the unitary implementation yields a minimal total time to solution roughly equal to the Zeno-based algorithm with no rewind. But as will be shown in the next section, its behavior is much better than anticipated—this method is more efficient than the Zeno algorithm with rewind, which itself is more efficient than Zeno without rewind.

**4. Numerical Results**

Three heuristic algorithms were numerically benchmarked: the classical walk with a variable-length linear interpolation between β=0 and β=2 and starting from a uniform distribution; the discrete, or Zeno-based adiabatic algorithm with rewind: and the unitary algorithm of the last subsection. The first system considered is a one dimensional Ising model. FIG. 1 shows the minimal total time to solution as a function of system size. In particular, FIG. 1 is a graph 100 that shows the minimum total time to solution (min(TTS)) as a function of system size for a one dimensional Ising model at β=2.

The results clearly indicate a polynomial advantages of the quantum algorithms over the classical algorithm. Surprisingly, the improvement exceeds the expected quadratic improvement, with a power law fit, going from 3.14 in the classical setting to 1.33 in the quantum setting using the unitary algorithm and 1.23 using the Zeno algorithm.

The second system considered is a sparse random Ising model: it has with gaussian random couplings Jl of variance 1 and Ωl comprises a random subset of 3.5n of all the n(n−1)/2 pairs of sites.

FIGS. 2 and 3 are graphs show minimum total time to solution as a function of the system size in, for a random ensemble of 100 systems of each sizes. In particular, FIGS. 2 and 3 show the minimum total time to solution (min(TTS)) as a function of system size for a sample of 100 random instances of the Ising model. Fits are obtained by least-mean-square. FIG. 2 shows the median TTS, whereas FIG. 3 shows the average of 10% hardest instances relative to the classical walk. All error bars are obtained from the bootstrap method and show a 95% confidence interval. Fit parameters are given at Table II.

In other words, FIGS. 2 and 3 show the the median min(TTS) as well as the hardest 10-percentile, where hardness is defined with respect to the classical algorithm. In all cases, the results indicate a polynomial advantage of the quantum methods over the classical method, but these advantages are much less pronounced than for the 1D Ising model.

In both the one-dimensional and the random graph Ising model, the unitary quantum algorithm achieves at least similar but often superior scalings than the Zeno with rewind algorithm.

**5. Cost Analysis and Simplifications**

First, the cost of gate V used to prepare the Move register will be analyzed. One of the most favorable cases to consider for the quantum oracle is when the proposed transitions ƒ(z) comprises all possible single-spin flips. In that

case, the move register is desirably prepared in a uniform superposition

\(\begin{matrix}
{\frac{1}{\sqrt{n}}{\sum\limits_{i = 1}^{n}{{i\rangle}.}}} & (36)
\end{matrix}\)

Assuming further that n=2k is a power of 2, the Move register can be prepared in the binary representation from k Hadamard gates acting in parallel on k qubits initialized to 10). In the unary representation, the state of the Move register can be prepared using n gates √{square root over (Λ)} acting sequentially on n qubits. The cost of applying a proposed transition to the Right register conditioned on the state of the Move register. When n is not a power of 2, one can use simple padding where all states i=n+1, n+2, . . . 2k encode the trivial move. At worst, this will slow-down the walk by a factor of 2.

Note that both operations described above use a number of elementary operations that scales with the system size, even though they are implementing a single step of the quantum walk and that on average, a single spin is modified per step of the walk. This contrasts with the classical walk. Indeed, when implementing a single step of the classical walk operator , a spin transition x→x·z is chosen with probability ƒ(z), the acceptance probability is computed, and the move is either accepted or rejected. Each transition x→x·z typically involve only a few spins (one in the setting that is being currently considering), so implementing such a transition in the classical walk does not require al extensive number of gates. The complexity in that case is actually dominated by the generation of a pseudo-random number selecting the location of the spin to be flipped.

The last item which determines the cost is the Boltzmann coin operation B. It is helpful to note that this operation is applied in quantum parallelism to all the proposed transitions, so its complexity is independent of the system size in contrast to the transformation V. A constituent of the Boltzmann coin transformation is the transformation G that evaluates the energy E(x) of a configuration x. This operation is required by both classical and quantum walks, so their cost should be relatively equal. Note that one does not need the energy of a configuration E(x) directly, but more accurately, one only needs to compute the energy difference of two configurations E(x)−E(x·z). When the proposed transitions z only affects a few spins and the Ising model is sparse, e.g. when the interactions ranges Ωl are restricted to constant-radius balls on the lattice, these calculations can be greatly simplified.

So the main cost of the Boltzmann coin B stems from the conditional rotation by angle θ=2 arcsin(eβE/2). This can be implemented either using a hard wired circuit, whose complexity scales exponentially with the number of bits representing E, or using a Taylor series of the function θ=2 arcsin(εβE/2) along with elementary controlled rotations. This cost should be compared to the classical cost of generating a random bit with probability eβE. Again, additional simplifications are possible in special cases, e.g. when the parameter Jl of the model Eq. (22) are restricted to a discrete set.

### IV. Example Computing Environments

FIG. 4 illustrates a generalized example of a suitable classical computing environment 400 in which several of the described embodiments can be implemented. The computing environment 400 is not intended to suggest any limitation as to the scope of use or functionality of the disclosed technology, as the techniques and tools described herein can be implemented in diverse general-purpose or special-purpose environments that have computing hardware.

With reference to FIG. 4, the computing environment 400 includes at least one processing device 410 and memory 420. In FIG. 4, this most basic configuration 430 is included within a dashed line. The processing device 410 (e.g., a CPU or microprocessor) executes computer-executable instructions. In a multi-processing system, multiple processing devices execute computer-executable instructions to increase processing power. The memory 420 may be volatile memory (e.g., registers, cache, RAM, DRAM, SRAM), non-volatile memory (e.g., ROM, EEPROM, flash memory), or some combination of the two. The memory 420 stores software 480 implementing tools for generating/synthesizing/controlling any of the disclosed quantum-circuit Markov chain Monte Carlo (MCMC) techniques as described herein. The memory 420 can also store software 480 for synthesizing, generating, or compiling quantum circuits for implementing any of the MCMC techniques as described herein.

The computing environment can have additional features. For example, the computing environment 400 includes storage 440, one or more input devices 450, one or more output devices 460, and one or more communication connections 470. An interconnection mechanism (not shown), such as a bus, controller, or network, interconnects the components of the computing environment 400. Typically, operating system software (not shown) provides an operating environment for other software executing in the computing environment 400, and coordinates activities of the components of the computing environment 400.

The storage 440 can be removable or non-removable, and includes one or more magnetic disks (e.g., hard drives), solid state drives (e.g., flash drives), magnetic tapes or cassettes. CD-ROMs, DVDs, or any other tangible non-volatile storage medium which can be used to store information and which can be accessed within the computing environment 400. The storage 440 can also store instructions for the software 480 implementing any of the disclosed MCMC techniques. The storage 440 can also store instructions for the software 480 for generating and/or synthesizing any of the described techniques, systems, or reversible circuits.

The input device(s) 450 can be a touch input device such as a keyboard, touchscreen, mouse, pen, trackball, a voice input device, a scanning device, or another device that provides input to the computing environment 400. The output device(s) 460 can be a display device (e.g., a computer monitor, laptop display, smartphone display, tablet display, netbook display, or touchscreen), printer, speaker, or another device that provides output, from the computing environment 400.

The communication connection(s) 470 enable communication over a communication medium to another computing entity. The communication medium conveys information such as computer-executable instructions or other data in a modulated data signal. A modulated data signal is a signal that has one or more of its characteristics set or changed in such a manner as to encode information in the signal. By way of example, and not limitation, communication media include wired or wireless techniques implemented with an electrical, optical, RF, infrared, acoustic, or other carrier.

As noted, the various methods, MCMC techniques, circuit design techniques, or compilation/synthesis techniques can be described in the general context of computer-readable instructions stored on one or more computer-readable media. Computer-readable media are any available media (e.g., memory or storage device) that can be accessed within or by a computing environment. Computer-readable media include tangible computer-readable memory or storage devices, such as memory 420 and/or storage 440, and do not include propagating carrier waves or signals per se (tangible computer-readable memory or storage devices do not include propagating carrier waves or signals per se).

Various embodiments of the methods disclosed herein can also be described in the general context of computer-executable instructions (such as those included in program modules) being executed in a computing environment by a processor. Generally, program modules include routines, programs, libraries, objects, classes, components, data structures, and so on, that perform particular tasks or implement particular abstract data types. The functionality of the program modules may be combined or split between program modules as desired in various embodiments. Computer-executable instructions for program modules may be executed within a local or distributed computing environment.

An example of a possible network topology 500 (e.g., a client-server network) for implementing a system according to the disclosed technology is depicted in FIG. 5. Networked computing device 520 can be, for example, a computer running a browser or other software connected to a network 512. The computing device 520 can have a computer architecture as shown in FIG. 5 and discussed above. The computing device 520 is not limited to a traditional personal computer but can comprise other computing hardware configured to connect to and communicate with a network 512 (e.g., smart phones, laptop computers, tablet computers, or other mobile computing devices, servers, network devices, dedicated devices, and the like). Further, the computing device 520 can comprise an FPGA or other programmable logic device. In the illustrated embodiment, the computing device 520 is configured to communicate with a computing device 530 (e.g., a remote server, such as a server in a cloud computing environment) via a network 512. In the illustrated embodiment, the computing device 520 is configured to transmit input, data to the computing device 530, and the computing device 534) is configured to implement an MCMC technique according to any of the disclosed embodiments and/or a circuit generation or compilation/synthesis methods for generating quantum circuits based on or in conjunction with any of the MCMC techniques disclosed herein. The computing device 530 can output results to the computing device 5320. Any of the data received from the computing device 530 can be stored or displayed on the computing device 520 (e.g., displayed as data on a graphical user interface or web page at, the computing devices 520). In the illustrated embodiment, the illustrated network 512 can be implemented as a Local Area Network (LAN) using wired networking (e.g., the Ethernet IEEE standard 802.3 or other appropriate standard) or wireless networking (e.g. one of the IEEE standards 802.11a, 802.11b, 802.11g. or 802.11n or other appropriate standard). Alternatively, at least part of the network 812 can be the Internet or a similar public network and operate using an appropriate protocol (e.g., the HTTP protocol).

Another example of a possible network topology 600 (e.g., a distributed computing environment) for implementing a system according to the disclosed technology is depicted in FIG. 6. Networked computing device 620 can be, for example, a computer running a browser or other software connected to a network 612. The computing device 620 can have a computer architecture as shown in FIG. 5 and discussed above. In the illustrated embodiment, the computing device 620 is configured to communicate with multiple computing devices 630, 631, 632 (e.g., remote servers or other distributed computing devices, such as one or more servers in a cloud computing environment) via the network 612. In the illustrated embodiment, each of the computing devices 630, 631, 632 in the computing environment 600 is used to perform at least a portion of an MCMC process and/or circuit generation or synthesis/compilation process. In other words, the computing devices 630, 631, 632 form a distributed computing environment in which the MCMC process and/or generation/compilation/synthesis processes are shared across multi pile computing devices. The computing device 620 is configured to transmit input data to the computing devices 630, 631, 632, which are configured to distributively implement such as process, including performance of any of the disclosed methods or creation of any of the disclosed circuits, and to provide results to the computing device 620. Any of the data received from the computing devices 630, 631, 632 can be stored or displayed on the computing device 620 (e.g., displayed as data on a graphical user interface or web page at, the computing devices 621)). The illustrated network 612 can be any of the networks discussed above with respect to FIG. 5.

With reference to FIG. 7, an exemplary system for implementing the disclosed technology includes computing environment 700. In computing environment 700, a compiled quantum computer circuit description (including quantum circuits for performing any of the MCMC techniques as disclosed herein) can be used to program (or configure) one or more quantum processing units such that the quantum processing unit(s) implement the circuit described by the quantum computer circuit description.

The environment 700 includes one or more quantum processing units 702 and one or more readout device(s) 708. The quantum processing unit(s) execute quantum circuits that are precompiled and described by the quantum computer circuit description. The quantum processing unit(s) can be one or more of, but are not, limited to: (a) a superconducting quantum computer; (b) an ion trap quantum computer; (c) a fault-tolerant architecture for quantum computing: and/or (d) a topological quantum architecture (e.g., a topological quantum computing device using Majorana zero modes). The precompiled quantum circuits, including any of the disclosed circuits, can be sent into (or otherwise applied to) the quantum processing unit(s) via control lines 706 at the control of quantum processor controller 721). The quantum processor controller (QP controller) 720 can operate in conjunction with a classical processor 710 (e.g., having an architecture as described above with respect to FIG. 4) to implement the desired quantum computing process. In the illustrated example, the QP controller 720 further implements the desired quantum computing process via one or more QP subcontrollers 704 that are specially adapted to control a corresponding one of the quantum processor(s) 702. For instance, in one example, the quantum controller 720 facilitates implementation of the compiled quantum circuit by sending instructions to one or more memories (e.g., lower-temperature memories), which then pass the instructions to low-temperature control unit(s) (e.g., QP subcontroller(s) 704) that transmit, for instance, pulse sequences representing the gates to the quantum processing unit(s) 702 for implementation. In other examples, the QP controller(s) 720 and QP subcontroller(s) 704 operate to provide appropriate magnetic fields, encoded operations, or other such control signals to the quantum processor(s) to implement the operations of the compiled quantum computer circuit description. The quantum controller(s) can further interact with readout devices 708 to help control and implement the desired quantum computing process (e.g., by reading or measuring out data results from the quantum processing units once available, etc.)

With reference to FIG. 7, compilation is the process of translating a high-level description of a quantum algorithm into a quantum computer circuit description comprising a sequence of quantum operations or gates, which can include the circuits as disclosed herein. The compilation can be performed by a compiler 722 using a classical processor 710 (e.g., as shown in FIG. 4) of the environment 700 which loads the high-level description from memory or storage devices 712 and stores the resulting quantum computer circuit description in the memory or storage devices 712.

In other embodiments, compilation and/or verification can be performed remotely by a remote computer 760 (e.g., a computer having a computing environment as described above with respect to FIG. 4) which stores the resulting quantum computer circuit description in one or more memory or storage devices 762 and transmits the quantum computer circuit description to the computing environment 700 for implementation in the quantum processing unit(s) 702. Still further, the remote computer 700 can store the high-level description in the memory or storage devices 762 and transmit the high-level description to the computing environment 700 for compilation and use with the quantum processor(s). In any of these scenarios, results from the computation performed by the quantum processor(s) can be communicated to the remote computer after and/or during the computation process. Still further, the remote computer can communicate with the QP controller(s) 720 such that the quantum computing process (including any compilation, verification, and QP control procedures) can be remotely controlled by the remote computer 760. In general, the remote computer 760 communicates with the QP controller(s) 720, compiler/synthesizer 722, and/or verification tool 723 via communication connections 750.

In particular embodiments, the environment 700 can be a cloud computing environment, which provides the quantum processing resources of the environment 500 to one or more remote computers (such as remote computer 760) over a suitable network (which can include the internet).

### V. Further Example Embodiments

FIG. 8 illustrates a method of operating a quantumn computing device in accordance with the disclosed technology. At 810, a quantum walk procedure of a Markov chain Monte Carlo simulation is implemented in which a quantum move register is reset at every step in the quantum walk. In certain implementations, the quantum walk procedure is performed without a measurement. In further implementations, the quantum walk procedure is performed using binary encodings of the move registers. In some implementations, the quantum walk procedure is performed using unary encodings of the move registers.

FIG. 9 illustrates a method of operating a quantum computing device in accordance with the disclosed technology. At 910, a quantum walk procedure of a Markov chain Monte Carlo simulation is implemented in which an underlying classical walk is obtained using a Metropolis-Hastings rotation or a Glauber dynamics rotation.

In some implementations, the method comprises any one or more of:

preparing a move register in a uniform superposition of all bit locations

\({{\varphi\rangle}_{M} = {\frac{1}{\sqrt{N}}{\sum\limits_{j = 1}^{N}{j\rangle}_{M}}}};\)

copying the state of the left register onto the right register, resulting in

|ϕM⊗|xL⊗|xR;

conditioned on the state of the move register, flipping the j-th bit, of the left register:

\({\sum\limits_{y}{\sqrt{T_{yx}}{{j\rangle}_{M} \otimes {y^{j}\rangle}_{L} \otimes {x\rangle}_{R}}}},\)

where yj is x with the j-th bit, flipped;


- - using the left and right registers to evaluate A_(xy) and prepare a
    coin register in state √{square root over (A_(yx))}\|0
    _(C)+√{square root over (1−A_(yx))}\|
    _(C);
  - uncomputing the move register by looking up the the coordinate where
    the left and right registers differ; and
  - implementing the transformation

\(\left. {\sum\limits_{y}{\sqrt{T_{yx}\left( {1 - A_{yx}} \right)}{{y\rangle}_{L} \otimes {x\rangle}_{R} \otimes {1\rangle}_{C}}}}\rightarrow{\sqrt{1 - {\sum\limits_{y}{T_{yx}A_{yx}}}}{{x\rangle}_{L} \otimes {x\rangle}_{R} \otimes {{0\rangle}_{C}.}}} \right.\)

In further implementations, the quantum walk procedure comprises any one or more of:

Ũ=RV†B†FBV 


- - where, V:−0
    _(M)→Σ_(j)√{square root over (ƒ(j))}\|j
    _(M),
  - B: −x
    _(S)\|j
    _(M)\|0
    _(C)→\|x
    _(S)\|j
    _(M)(√{square root over (1−A_(x·zj,x))}\|0
    +A_(x·zj,x)\|1
    )_(C)
  - F: −x
    _(S)\|j
    _(M)\|b
    _(C)→\|x·z_(j)^(b)
    _(S)\|j
    _(M)\|b
    _(C), and
  - R: −0
    _(M)\|0
    _(C)→−\|0
    _(M)\|0
    _(C), \|j
    _(M)\|b
    →\|j
    _(M)\|b
    for (j,b)≠(0,0)

In certain implementations, the quantum walk procedure is performed with only a logarithmic depth. In some implementations, the quantum walk procedure is performed using binary encodings of the move registers. In certain implementations, the quantum walk procedure is performed using unary encodings of the move registers. In certain implementations, the quantum walk procedure is performed using a Boltzmann coin having a coin register that is rotated using the Metropolis-Hastings rotation. In some implementations, the quantum walk procedure is performed using a Boltzmann coin having a coin register that is rotated using the Glauber dynamics rotation. In certain implementations, the quantum walk procedure comprises implementing a Boltzman coin using lookup tables and conditional quantum gates.

FIG. 10 is another flow chart 1000 illustrating a method of operating a quantum computing device in accordance with the disclosed technology. The particular operations and sequence of operations should not be construed as limiting, as they can be performed alone or in any combination, subcombination, and/or sequence with one another. Additionally, the illustrated operations can be performed together with one or more other operations.

At 1010, a quantum walk procedure is performed in the quantum computing device to implement a Markov Chain Monte Carlo method.

At 1012, (luring the quantum walk procedure, an intermediate measurement is obtained.

At 1014, a rewinding procedure of one or more but not all steps of the quantum walk procedure is performed if the intermediate measurement produces an incorrect outcome.

In certain implementations, the rewinding procedure comprises rewinding only a single step of the quantum walk procedure. In some implementations, the rewinding procedure is performed using a pair of binary projective measurements.

Any of the disclosed embodiments can be performed by one or more computer-readable media storing computer-executable instructions which when executed by a computer cause the computer to perform any of the disclosed methods.

Any of the disclosed embodiments can also be implemented in a system, comprising a quantum computing device; and a classical computer in communication with and configured to control the quantum computing device, wherein the quantum computing device and the classical computer collectively operate to perform any of the disclosed methods.

### VI. Concluding Remarks

Having described and illustrated the principles of the disclosed technology with reference to the illustrated embodiments, it will be recognized that the illustrated embodiments can be modified in arrangement, and detail without departing from such principles. For instance, elements of the illustrated embodiments shown in software may be implemented in hardware and vice-versa. Also, the technologies from any example can be combined with the technologies described in any one or more of the other examples. It will be appreciated that procedures and functions such as those described with reference to the illustrated examples can be implemented in a single hardware or software module, or separate modules can be provided. The particular arrangements above are provided for convenient illustration, and other arrangements can be used.

