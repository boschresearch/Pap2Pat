# DESCRIPTION

The present invention relates to a quantum computer implemented probabilistic error correction method for use in quantum circuits. Invention finds its application in quantum information systems in particular in a quantum communication channels.

In the prior art a number of quantum error correction technics is known.

Perfect reconstruction codes. In the publication of Knill Emanuel, Raymond Laflamme, and Lorenza Viola, “Theory of quantum error correction for general noise” Physical Review Letters 84.11 (2000): 2525. A general description of arbitrary system-environment couplings in terms of a graded interaction algebra is disclosed. The degree of an operator in this algebra both determines the temporal order and the extent to which the operator can affect the system, independent of the internal evolution of the environment. In the case of qubits with independent one-qubit interactions, this notion coincides with the usual concepts of “number of errors” or “error weight” used in combinatorial error analysis. It is disclosed that the generalization of minimum distance relates to error correction in the usual way and show that, irrespective of the nature of the environmental noise, large codes exist depending solely on the dimension of the linear space of errors of a given order. This publication discloses an error correction code that requires at least four qubits to work. The proof exists that in order work with probability of success equal to one and to recover information form the channel affected by the noise of Choi rank not greater than two, it needs to use more than two qubits.

Approximate error correction codes. The publication Berta Mario, et al. “Semidefinite programming hierarchies for constrained bilinear optimization.” Mathematical Programming (2021): 1-49, discloses asymptotically converging semidefinite programming hierarchies of outer bounds on bilinear programs of the form Tr [H(D⊗E)] maximized with respect to semidefinite constraints on D and E. Such hierarchies when applied to the problem of approximate error correction in quantum information theory, give hierarchies of efficiently computable outer bounds on the success probability of approximate quantum error correction codes in any dimension. The approximate error correction codes by design return approximate encoded state and they do not allow for perfect recovery of the initial state.

Probabilistic error correction codes. In the publication MacKay David J C, Graeme Mitchison, and Paul L. McFadden. “Sparse-graph codes for quantum error correction.” IEEE Transactions on Information Theory 50.10 (2004): 2315-2330 the authors explored the conjecture that the best quantum error-correcting codes will be closely related to the best classical codes. By converting classical low-density parity-check codes into quantum codes, the authors hope to find families of excellent quantum codes. The approach relies on further conjecture claiming that practical decoding algorithms have been found for classical low-density parity-check codes, it seems likely that a practical decoding algorithm will also exist for quantum low-density parity-check codes. It also discloses the stabilizer formalism for describing quantum error-correcting codes that encode a quantum state of K qubits in N qubits, and explains how a general stabilizer code is related to a classical binary code.

In the publication Koashi Masato, and Masahito Ueda “Reversing measurement and probabilistic quantum error correction.” Physical review letters 82.12 (1999): 2598, a general characterization of probabilistically reversible measurements is presented. Further it is proposed that such probabilistic reversal serves as a means of error correction in quantum computation, which would be particularly useful when the numbers of qubits and gate operations are limited.

The publication Fern, Jesse, and John Terilla “Probabilistic quantum error correction.” arXiv preprint quant-ph/0209058 (2002), examines, within the context of stabilizer codes, the conditions under which a code may correct errors on more qubits than it is guaranteed to fix and gives a framework in which to compute the probabilities that an arbitrary error will be corrected. During the course of quantum error correction, an error syndrome is measured and the correction procedure continues dependent on this measurement. As a second application of probabilistic error correction, the likelihood that error correction will succeed given that a particular syndrome is measured is analyzed. This likelihood, is called the syndrome quality, may enhance the effectiveness of a quantum information process for which quantum error correction plays a role. For example, it is conceivable that a quantum information process may benefit from aborting a subroutine if at some point a syndrome of especially low quality is measured.

In the publication Delfosse, Nicolas, Ben W. Reichardt, and Krysta M. Svore “Beyond single-shot fault-tolerant quantum error correction.” IEEE Transactions on Information Theory (2021), in this publication, it is demonstrated that fault-tolerant quantum error correction can be achieved using O(d log(d)) measurements for any code with distance d≥Ω(nα) for some constant α>0. Moreover, we prove the existence of a sub-single-shot fault-tolerant quantum error correction scheme using fewer than r measurements. In some cases, the number of parity check measurements required for fault-tolerant quantum error correction is exponentially smaller than the number of parity checks defining the code.

Probabilistic codes are known as it is described above, however it is important to notice that these are mostly codes with stabilizers operating on a mesh of nine qubits in the Pauli basis. The noise models of known probabilistic codes do not allow for correction of all errors of Choi rank at most two.

The present invention is characterized in claims 1, 5 and 9, while the further preferable embodiments are described in dependent claims.

The present invention provides a probabilistic quantum error correction code that encodes one qubit of information, operates on two data qubits, corrects errors generated by noise channel of Choi rank not greater than two. Further the present invention provides an error correction procedure that has a positive probability that it will succeed, and in such a case, the procedure returns classical information indication showing its status. If the error correction procedure succeeds it perfectly recovers the initial state. This set of advantageous features is not known to exists in any of the know quantum error correction methods.

Further the present invention relates to an encoder and decoder that operate according to a probabilistic quantum error correction code.

Quantum computing systems incorporate a classical part of the system and a quantum part of the system. The classical part of the quantum system is responsible for setting up a quantum circuit and processing the output of the quantum circuit, while the quantum part of the system is responsible for running the quantum computation process. Both parts of the quantum computing system cannot be separated as the uncontrolled quantum circuit without a classic setup process would produce no meaningful results and classic part of the quantum computing system—without a quantum circuit—is not able to benefit from quantum effects present only in the quantum circuit. Technical effects observed in the quantum system can be classified as direct technical effects involving interaction between qubits, and further technical effects as seen from the perspective of a quantum communication system end expressing themselves in correction of errors and improved more reliable quantum communication system.

The language of the following disclosure is a quantum computing language and it is assumed the reader is familiar with mathematical notation involved in this field of technology, in particular with complex numbers, matrix linear algebra in Hilbert spaces, the notation of orthogonal vectors |·⊥, transposition T , and conjugate transposition †.

In the FIG. 1 a scheme representing QEC (Quantum Error Correction) procedure is shown, it is a quantum part of the quantum communication scheme. In the classic part the quantum error scheme requires preparation of unitary matrices UE, UD and VD. At the beginning of the procedure one has access to two data qubits. The first one is in a state |ψ. This qubit will be encoded with an information. The second qubit is put into a ground state |0. In the description we use the second qubit in a ground state |0 however the second qubit can be put into any arbitrary fixed state |d1without departing from the scope of the invention. In the next step the initial state of both qubits goes under two-qubit unitary operation UE, this means a rotation of a state vector in a four dimensional Hilbert space.

Then the encoded state UE(|Ψ⊗|0) is affected by the noise N. This procedure works with quantum circuits with a noise channel N(X) that has a Choi rank not greater than two, such as N(X)=N0XN0†+N1XN1†. This error noise cannot be corrected by any known probabilistic nor perfect QEC codes acting on two qubits only.

After that, we start the decoding procedure by implementing two-qubit unitary operation UD which is unitary rotation of an error affected vector state in a four dimensional Hilbert space. The next step of the procedure is measuring the second qubit in the standard basis to obtain a classical label i ∈{0,1}. In the description we use a measurement of the second qubit in a standard basis, however the measurement of the second qubit can be done by a projective measurement in arbitrary basis {|d2,|d2⊥}, without departing from the scope of the invention.

The next step of the procedure is preparing a third qubit in the ground state |10. The same as in the case of the second qubit, in the description we use the third qubit in a ground state |10 however the third qubit can be put into any arbitrary fixed state |d3, without departing from the scope of the invention.

Having such a circuit the next step of the procedure is to implement two qubit unitary operation VD on the first qubit and the third qubit, followed by measuring the third qubit in the standard basis to obtain a classical label j ∈ {0,1}. The same as in the case of the second qubit in the description we use a measurement of the third qubit in a standard basis, however the measurement of the third qubit can be done by a projective measurement in arbitrary basis {|d4,|d4⊥} without departing from the scope of the invention.

In the final step the procedure is conditioned by the classical labels i,j and when (i,j)=(0,0) accepting as an output δexp a decoded state of the first qubit, and when (i,j)≠(0,0) rejecting the output δexp of a decoded state of the first qubit.

Preferably when the output δexp is rejected the method further comprising a step of initiating an automatic resend request for the encoded state |ψ on the first qubit.

The encoding scheme according to the invention is described in detail below starting with the N to be a two-qubit noise channel, such that its Choi rank is no greater than two. Having this assumption a probabilistic quantum error correction code for noise N is proposed, which in the classical part of the procedure defines unitary matrices UE, UD, and VD.

The noise N can be written in the Kraus representation as

N(X)=N0XN0†+N1XN1†.

A four by two encoding matrix E can be found such that E†E=2 . Further a two by four decoding matrix D can be found, such that ∥D∥∞≤1 for which

DN0E ∝2,

DN1E∝2,

DN0E≠0V DN1E≠0.

The matrices E, D create a valid error correction scheme (E,D) for noise N as

D(N(EXE†))D†=pX.

For some p ∈ (0,1] and any two by two matrix X.

The matrix UE is the four by four unitary matrix that satisfies

UE(2⊗0)=E.

The matrix UD is the four by four unitary matrix that satisfies

UD|t1=|0,0,

UD|t2=|1,0.

for singular value decomposition of D=σ1|z1t1|+σ2|z2t2|.

For the matrix D′=DUD†(2⊗|0), one can define the matrix VD which satisfies

(2⊗0|)VD(2⊗|0)=D′.

Having defined unitary operations UE, UD and VD one can run the quantum part of the procedure as described in relation to FIG. 1 for initial state |ψ. Then having the output state δexp of the procedure from FIG. 1 in the post processing of the measurements outputs (i, j), when (i,j)=(0,0) then the output δexp is accepted and δexp=|ψψ|, and when (i,j)≠(0,0) the output δexp is rejected.

In the preferable embodiment of the invention matrices E and D are constructed as described in detail below.

In the first step calculate the singular decomposition of N0, and N1 in the form of

N0=U0λ0V,

N1=U1λ1V,

where U0, U1, V are unitary matrices, and λ2, λ1 are diagonal, positive semidefinite matrices.

Define ancillary vectors

|xi=(λ0)iiU0|i, i=0, . . . ,3,

|yi=(λ1)iiU1|i, i=0,. . . ,3,

Define vectors |E0, |E1, |D0, |D1 ∈ according to the construction, which depends on one of the following cases:

First case: There exists i3 ∈ {0, . . . , 3} such that vectors |xi, |yi) are linearly independent.

Define indices i0, i1, i2 ∈ {0, . . . , 3}, such that {i0, . . . , i3} covers the whole set {0, . . . ,3}. Let (α0, α1, α2)T ∈  be a normed vector orthogonal to vectors (yi|xi, yi|xi, Yi|xi)† and (xi|yi, xi|yi, xi|yi)†. Orthogonalization can obtained by the use of the Gram-Schmidt orthogonalization method. Take |E1=|i3 and |E0=α0|i0+α1|i1|i2.

Define |x=α0|xi+α1|xi+α2|xi and |y=α0|yi+α1|yi. If |x≠0 take |D0=|x, else take |D0=|Y.

Define

\(\left( {b_{0},b_{1}} \right)^{T} = {\begin{bmatrix}
\left. {\left. \left( x_{i_{3}} \middle| x_{i_{3}} \right. \right\rangle\left( y_{i_{3}} \middle| x_{i_{3}} \right.} \right\rangle \\
\left. {\left. \left( x_{i_{3}} \middle| y_{i_{3}} \right. \right\rangle\left( y_{i_{3}} \middle| y_{i_{3}} \right.} \right\rangle
\end{bmatrix} - {1\left( {\left\langle D_{0} \middle| x \right\rangle,\left\langle D_{0} \middle| y \right\rangle} \right)^{T}}}\)

Take |D1=0|xi+1|yi.

Second case: There exists a pair of vectors |yi, |yi for i≠i1, such that |yi=|yi=0.

Define |E0=|i0, |E1=|i1, |D0=|xiand |D1, =|xi.

Third case: For all i ∈ {0, . . . ,3} vectors |xi, |yi are not linearly independent and there is at most one zero vector |yi for some i3 ∈ {0, . . . , 3}.

Define indices i0, i1, i2 ∈ {0, . . . ,3}, such that {i0, . . . , i3} covers the whole set {0, . . . ,3}.

Define the matrix

\(M = {\begin{bmatrix}
\left\langle y_{i_{0}} \middle| x_{i_{0}} \right\rangle & \left\langle y_{i_{1}} \middle| x_{i_{1}} \right\rangle & \left\langle y_{i_{2}} \middle| x_{i_{2}} \right\rangle \\
\left\langle y_{i_{0}} \middle| y_{i_{0}} \right\rangle & \left\langle y_{i_{1}} \middle| y_{i_{1}} \right\rangle & \left\langle y_{i_{2}} \middle| y_{i_{2}} \right\rangle
\end{bmatrix}.}\)

Subcase a) rank (M)=1

\({b = \frac{\left. \left( {y_{i_{1}}1y_{i_{1}}} \right. \right\rangle}{\left. \left( {y_{i_{0}}1y_{i_{0}}} \right. \right\rangle}}{\left| E_{0} \right. = {\left| i_{o} \middle| E_{1} \right. = {\left| i_{1} \middle| D_{0} \right. = {\left| y_{i_{0}} \middle| D_{1} \right. = \left. \frac{1}{b} \middle| y_{i_{1}} \right.}}}}\)

Subcase b) rank(M)=2


- - Define indices j₁, j₂ ∈ {0, 1, 2} such that

\(\left( \begin{bmatrix}
M_{0j_{1}} & M_{0j_{2}} \\
M_{1j_{1}} & M_{1j_{2}}
\end{bmatrix} \right) = {2.}\)


- - Define j₀ ∈ {0, 1, 2}, as the remaining label, such that {j₀, j_(1,)
    j_(2}) covers the whole set {0,1, 2}.
  - Take \|E₀
    =\|i_(j0)
    ,

\(\left. {\left. {❘D_{0}} \right\rangle = {❘y_{i_{j_{0}}}}} \right\rangle.\)

## Define

\(\left. \left. {\left. {\left( {b_{1},\ b_{2}} \right)^{T} = {\begin{bmatrix}
\left. {\left. \left( y_{i_{j_{1}}} \middle| x_{i_{j_{1}}} \right. \right\}\left( y_{i_{j_{2}}} \middle| x_{i_{j_{2}}} \right.} \right\} \\
\left. {\left. \left( y_{i_{j_{1}}} \middle| y_{i_{j_{1}}} \right. \right\}\left( y_{i_{j_{2}}} \middle| y_{i_{j_{2}}} \right.} \right\}
\end{bmatrix} - {1\left( \left( y_{i_{j_{0}}} \middle| x_{i_{j_{0}}} \right. \right.}}} \right\},\ \left( y_{i_{j_{0}}} \middle| y_{i_{j_{0}}} \right.} \right\} \right)^{T}{\left| E_{1} \right. = {\left| {i_{j_{1}} +} \middle| i_{j_{2}} \middle| D_{1} \right. = \left. {\overset{¯}{b}}_{1} \middle| {y_{i_{j_{1}}} + {\overset{¯}{b}}_{2}} \middle| y_{i_{j_{2}}} \right.}}\)

Having the vectors |E0, |E1, |D0, |D1 ∈  constructed, define a four by two matrix E*=V†(|E0)0|+|E1)1|), and a two by four matrix D*=|0D0|+|1D1|.

Define

\({E = {E_{*}\left( {E_{*}^{\dagger}E_{*}} \right)}^{{- 0}5}}{D = \frac{\left( {E_{*}^{\dagger}E_{*}} \right)^{05}D_{*}}{{\|\left( {E_{*}^{\dagger}E_{*}} \right)}^{05}D_{*}\|_{\infty}}}\)

The matrices E and D allow to create unitary matrices UE, UD, VD according to the invention as it was described above.

To implement the error correction procedure according to the invention it is necessary to implement two qubit unitary matrix, ground state preparation and standard basis one qubit measurement. This can be implemented in a standard architecture provided by lonQ. Architecture provided by lonQ offers ground state |0 preparation., Z-basis measurement (measurement in Z axis of Pauli basis), and one qubit unitary gates, native gates

\({{{GPI}(\phi)} = \begin{bmatrix}
0 & {\exp\left( {{- i}\phi} \right)} \\
{\exp\left( {i\phi} \right)} & 0
\end{bmatrix}},\)
\({{{GPI}2(\phi)} = {\frac{1}{\sqrt{2}}\begin{bmatrix}
1 & {{- i}{\exp\left( {{- i}\phi} \right)}} \\
{{- i}{\exp\left( {i\phi} \right)}} & l
\end{bmatrix}}},\)

a virtual gate

\({G{Z(\theta)}} = \begin{bmatrix}
{\exp\left( \frac{{- i}\theta}{2} \right)} & 0 \\
0 & {\exp\left( \frac{i\theta}{2} \right)}
\end{bmatrix}\)

a two-qubit native Malmer-Sorenson gate

MS(0.25π)=exp(−0.25πi×σx⊗σx).

By using a composition of gates GPI (0)GPI(ϕ)GP12(0) it is possible to implement arbitrary rotation along Y-axis (in a Pauli basis). It is also possible to implement CNOT gate as it is shown in shown in technical documentation and examples at https://quantumai.google/cirg/tutorials/educators/ion_device. Therefore, the offered gates constitute universal set of quantum gates (see Eq. 5-7 in https://arxiv.org/pdf/2101.02993.pdf), especially this set is sufficient to implement any two-qubit unitary gate (see FIG. 5 in https://arxiv.org/pdf/2101.02993.pdf).

In the preferred embodiment the present invention was applied to the following noise channel

\(\begin{matrix}
{{{N(X)} = {{N_{0}XN_{0}^{\dagger}} + {N_{1}XN_{1}^{\dagger}}}}{N_{0} = {{{{diag}\left( {1,0,\frac{1}{\sqrt{2}},\ \frac{1}{\sqrt{2}}} \right)}N_{1}} = {{diag}\left( {0,1,\frac{1}{\sqrt{2}},\ {\frac{1}{\sqrt{2}}i}} \right)}}}} & (X)
\end{matrix}\)

We have that N0=U0λ0V and N1=U1λ1V for

\({V = 1_{4}},\)
\({U_{0} = 1_{4}},\)
\(U_{1} = {{diag}(i)}\)
\({\lambda_{0} = N_{0}},\)
\(\lambda_{1} = {{{diag}\left( {\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}} \right)}.}\)

We have that

\(\left. {\left. {\left. {\left. {\left. {\left. {\left. {❘x_{0}} \right\rangle,{❘x_{1}}} \right\rangle,{❘x_{2}}} \right\rangle,{❘x_{3}}} \right\rangle = {❘0}} \right\rangle,0,{\frac{1}{\sqrt{2}}{❘2}}} \right\rangle,{\frac{1}{\sqrt{2}}{❘3}}} \right\rangle,\)
\(\left. {\left. {\left. {{\left. {\left. {\left. {\left. {❘y_{0}} \right\rangle,{❘y_{1}}} \right\rangle,{❘y_{2}}} \right\rangle,{❘y_{3}}} \right\rangle = 0},{❘1}} \right\rangle,{\frac{1}{\sqrt{2}}{❘2}}} \right\rangle,{\frac{1}{\sqrt{2}}i{❘3}}} \right\rangle.\)

This is in the third case of the creation of E, D matrices, with (i3=0, i0=1, i1=2, i2=3) hence the matrix M is as follows

\(M = {\begin{bmatrix}
0 & 0.5 & {{- 0.5}i} \\
1 & 0.5 & 0.5
\end{bmatrix}.}\)

It is a subcase b) as rank (M)=2.

We take

\(\left. {\left. {\left. {\left. {\left. {{j_{1} = 0},{j_{2} = {2.{Define}{❘E_{0}}}}} \right\rangle = {❘3}} \right\rangle,{❘D_{0}}} \right\rangle = {❘y_{3}}} \right\rangle = {\frac{1}{\sqrt{2}}i{❘3}}} \right\rangle.\)

Now we calculate

\(\left. {\left. {\left. {\left. {\left. {\left. {\left( {b_{1},b_{2}} \right)^{T} = {{\begin{bmatrix}
0 & 0.5 \\
1 & 0.5
\end{bmatrix}^{- 1}\left( {{{- 0.5}i},0.5} \right)^{T}} = {{\left( {{0.5 + {0.5i}},{- i}} \right)^{T}.{Define}}{❘E_{1}}}}} \right\rangle = {❘1}} \right\rangle + {❘2}} \right\rangle{and}{❘D_{1}}} \right\rangle = {\left( {0.5 - {0.5i}} \right){❘1}}} \right\rangle + {\frac{1}{\sqrt{2}}i{❘2}}} \right\rangle\)

Take

\({E_{*} = \begin{bmatrix}
0 & 0 \\
0 & 1 \\
0 & 1 \\
1 & 0
\end{bmatrix}},{D_{*} = {\begin{bmatrix}
0 & 0 & 0 & {{- \frac{1}{\sqrt{2}}}i} \\
0 & {0.5 + {0.5i}} & {{- \frac{1}{\sqrt{2}}}i} & 0
\end{bmatrix}.}}\)

Take

\({E = \begin{bmatrix}
0 & 0 \\
0 & \frac{1}{\sqrt{2}} \\
0 & \frac{1}{\sqrt{2}} \\
1 & 0
\end{bmatrix}}{D = {\begin{bmatrix}
0 & 0 & 0 & {{- 0.5}i} \\
0 & {0.5 + {0.5i}} & {{- \frac{1}{\sqrt{2}}}i} & 0
\end{bmatrix}.}}\)

The probability of successful error correction is equal to p=0.25 and the unitary matrices are as follows

\({U_{E} = \begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\
0 & {- \frac{1}{\sqrt{2}}} & \frac{1}{\sqrt{2}} & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}},{U_{D} = \begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & {{- \frac{1}{\sqrt{2}}}i} & {0.5 - {0.5i}} & 0 \\
0 & {0.5 + {0.5i}} & {{- \frac{1}{\sqrt{2}}}i} & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}},{V_{D} = {\begin{bmatrix}
{{- 0.5}i} & {0.5\sqrt{3}} & 0 & 0 \\
{0.5\sqrt{3}} & {{- 0.5}i} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}.}}\)

Below it is described how to implement the encoder and decoder according to the invention.

A quantum computer implemented encoder for a probabilistic error correction method for use with quantum circuits with a noise channel N(X) that has a Choi rank not greater than two, such as

N(X)=N0XN0†+N1XN1†

and the encoder comprises an encoding module adapted to encode a first qubit into an encoded state |ψ, and put a second qubit into a ground state |0. This encoding module may be embodied in a standard architecture provided by lonQ. Architecture provided by lonQ offers ground state |0 preparation and an encoded state |ψ preparation.

As it was indicated earlier by using a composition of gates GPI(0)GPI(ϕ)GPI2(0) it is possible to implement arbitrary rotation along Y-axis (in a Pauli basis). It is also possible to implement CNOT gate as it is shown in shown in technical documentation and examples at https://quantumai.google/cirg/tutorials/educators/ion_device. Therefore, the offered gates constitute universal set of quantum gates (see Eq. 5-7 in https://arxiv.org/pdf/2101.02993.pdf), especially this set is sufficient to implement any two-qubit unitary gate (see FIG. 5 in https://arxiv.org/pdf/2101.02993.pdf). Hence using the universal set of gates it is possible to achieve an encoder adapted to implement two qubit unitary operation UE on the first qubit and the second qubit to obtain an encoded state UE(|ψ⊗|0), such as

UE(2⊗|0)=E 


- - while E is an encoding matrix, and D is a decoding matrix such as

DN0E∝2,

DN1E∝2,

DN0E≠0VDN1E≠0.

The encoder according to the invention is preferably also adapted to receive an automatic resend request for the encoded state |ψ on the first qubit, and further adapted to produce the encoded state |ψ on the first qubit in response to the automatic resend request. This adaptation requires classic feedback loop between the decoder and the encoder.

In particular, the encoder is adapted to implement two qubit unitary operation characterized by UE as below:

\(U_{E} = {\begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\
0 & {- \frac{1}{\sqrt{2}}} & \frac{1}{\sqrt{2}} & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}.}\)

The same basic lonQ architecture can be used to implement a quantum computer implemented decoder for a probabilistic error correction method for use with quantum circuits with a noise channel N(X) that has a Choi rank not greater than two, such as

N(X)=N0XN0†+N1XN1†

the decoder is adapted to receive a first qubit in an encoded state |ψ , and a second qubit into a ground state |0 after the encoded state and ground state are affected by the noise N(X), further the decoder is adapted to implement two qubit unitary operation UD, such as

(2⊗0|)VD(2⊗|0)=DUD†(2⊗|0)

further the decoder is adapted to measure the second qubit in the standard basis to obtain a classical label i ∈{0,1}, and prepare a third qubit in the ground state |0, and implement two qubit unitary operation VD on the first qubit and the third qubit. Further the decoder is adapted to measure the third qubit in the standard basis to obtain a classical label j ∈{0,1}, and when (i,j)=(0,0) to accept as an output δexp a decoded state of the first qubit, and when (i,j)≠(0,0) reject the output δexp of a decoded state of the first qubit.

Preferably the decoder according to this invention is adapted to initiate an automatic resend request for the encoded state |ψ on the first qubit wherein the output δexp is rejected via classic feedback communication channel.

As the universal set of gates implemented in lonQ architecture is capable of implementing any unitary rotation lonQ architecture is sufficient to support adaptation of the decoder to implement two qubit unitary operations UD, and VD such as

\({U_{D} = \begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & {{- \frac{1}{\sqrt{2}}}i} & {0.5 - {0.5i}} & 0 \\
0 & {0.5 + {0.5i}} & {{- \frac{1}{\sqrt{2}}}i} & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}},{V_{D} = {\begin{bmatrix}
{{- 0.5}i} & {0.5\sqrt{3}} & 0 & 0 \\
{0.5\sqrt{3}} & {{- 0.5}i} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}.}}\)

It shall be noted that despite the implementation of 2 qubit gates for unitary operations in lonQ architecture is preferable way of putting the invention into practice, any other gate-based quantum computer architecture is feasible to embody the presented invention.

