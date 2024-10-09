# I. INTRODUCTION

Quantum error correction (QEC) is an encoding-decoding procedure that protects quantum information from errors arising due to quantum noise. Similarly, as in classical computations, this procedure is essential to develop fully operational quantum computers [1]. The theory of QEC, initialized by the work of Shor [2], covers a wide range of coding techniques: Calderbank-Shor-Steane codes [3-5], stabilizer codes [6], topological codes [7], subsystem codes [8], entanglement-assisted quantum error-correcting codes [9, 10], quantum low-density parity-check (LDPC) codes [11], quantum maximum distance separable codes [12] and many more (for a review see [13]).

In this work, we study a particular QEC procedure called probabilistic quantum error correction (pQEC) [14-16]. To outline how pQEC procedure works, let us present an example of classical probabilistic error correction. Consider the scenario, when the encoded data is harmed by a single bit error, that is with the probability p ∈ [0, 1] an arbitrary bit will be flipped. To secure a one bit of information, we use two physical bits. If we expect that p ≤ 2 3 , then we can encode 0 → 00 and 1 → 11. If we receive information 00 at the decoding stage, we are certain the encoded message was 0 (and 1 for 11). We dismiss the cases 01 and 10 as they do not give conclusive answers. Otherwise, if p > 2 3 it would be beneficial to use encoding 0 → 00 and 1 → 01 with the accepting states 10 and 11. It is worth mentioning, that to secure a one bit of information perfectly, it is necessary to use three physical bits, for example 0 → 000, 1 → 111.

Let us return to the quantum case. The heart of pQEC procedure is the probabilistic decoding operation [17,18]. This operation uses a classical postselection to determine if the encoded information was successfully restored. The clear drawback is that the procedure may fail with some probability. In such case, we should reject the output state and ask for a retransmission [19]. In the context of QEC, probabilistic decoding operations have found application in stabilizer codes [20] especially for iterative probabilistic decoding in LDPC codes [11,21,22], error decoding [23,24] or environment-assisted error correction [25]. Moreover, it was noted that they have a potential to increase the spectrum of correctable errors [15] and are useful when the number of qubits is limited [14]. It is also worth mentioning, they were used with success in other fields of quantum information theory, e.g. probabilistic cloning [26], learning unknown quantum operations [27] or measurement discrimination [28].

Despite the fact that pQEC procedure has been studied in the literature for a while, there is lack of a formal description of its application for a general noise model. In this work, we fill this gap. Inspired by celebrated Knill-Laflamme conditions [29], we provide conditions (Theorem 1) to check, when probabilistic error correction is possible. We discover that optimal error-correcting codes are not always generated with the usage of isometric encoding operations. We give an explicit example of noise channels family (Section V), such that to maximize the probability of successful error correction we need to encode the quantum information into a mixed state. Moreover, we discuss the advantage of pQEC procedure over the deterministic one with a formal statement in Theorem 7. We show in Theorem 13 how *

# II. PRELIMINARIES A. Mathematical framework

In this section, we will introduce the notation and recall necessary basic facts of quantum information theory. We will denote complex Euclidean spaces by symbols X , Y, . . .. The set of linear operators M : X → Y will be written as M(X , Y) and M(X ) := M(X , X ). The identity operators will be denoted by 1l X ∈ M(X ). For any operator M ∈ M(X , Y) we will consider its vectorization |M ∈ Y ⊗ X , which is defined as

where |i are elements of computational basis. In the space M(X ), we distinguish the set of positive semi-definite operators P(X ), the space of Hermitian operators H(X ) and the set of unitary operators U(X ). We use the convention that for non-invertible operator M , by M -1 , we denote its Moore-Penrose pseudo-inverse [30]. We consider the set of quantum states D(X ), that is, the set of positive semi-definite operators with unit trace. We say that a quantum state ρ is a pure state if rank(ρ) = 1, otherwise, if rank(ρ) > 1, we say that ρ is a mixed state. The maximally mixed state will be denoted by ρ * X := 1 dim(X ) 1l X . We also consider transformations between linear operators. We denote by I X : M(X ) → M(X ) the identity map. Let us define the set of quantum subchannels sC(X , Y) [31]. A quantum subchannel Φ ∈ sC(X , Y) is a linear map Φ : M(X ) → M(Y), which is completely positive [30,Theorem 2.22], i.e.

(Φ ⊗ I X )(Q) ∈ P(Y ⊗ X ) for any Q ∈ P(X ⊗ X )

and trace non-increasing tr(Φ(ρ)) ≤ 1 for any ρ ∈ D(X ).

In particular, the subchannel Φ which is trace preserving, i.e.

tr(Φ(ρ)) = 1 for any ρ ∈ D(X )

will be called a quantum channel. We denote by C(X , Y) the set of quantum channels Φ : M(X ) → M(Y). We will also use the following notation, sC(X ) := sC(X , X ) and C(X ) := C(X , X ).

In this work, we will consider the following representations of subchannels:

• Kraus representation: Each subchannel Φ ∈ sC(X , Y) can be defined by a collection of Kraus operators (K i ) r i=1 ⊂ M(X , Y), such that Φ(X) = r i=1 K i XK † i for X ∈ M(X ) and r ∈ N. The operators K i satisfy the condition r i=1 K † i K i ≤ 1l X . We say that the subchannel Φ is given in a canonical Kraus representation (K i ) r i=1 , if it holds that tr(K † j K i ) ∝ δ ij and K i = 0 for each i ≤ r. To represent the subchannel Φ by its Kraus representation (K i ) r i=1 , we introduce the notation K : M(X , Y) ×r → sC(X , Y) given by Φ = K ((K i ) r i=1 ). • Choi-Jamiołkowski representation: Each subchannel Φ ∈ sC(X , Y) can be uniquely described by its Choi-Jamiołkowski operator J(Φ) ∈ M(Y ⊗ X ), which is defied as J(Φ) := (Φ ⊗ I X )(|1l X 1l X |). The rank of J(Φ) is called the Choi rank and it determines the minimal number r of Kraus operators K i needed to describe Φ in the Kraus form Φ = K ((K i ) r i=1 ). Therefore, if the Kraus representation (K i ) r i=1 is canonical, then r = rank(J(Φ)).

• Stinespring representation: By the Stinespring Dilatation Theorem any subchannel Φ ∈ sC(X , Y) can be defined as Φ(X) = tr 2 AXA † for X ∈ M(X ), where A ∈ M(X , Y ⊗ C r ) and tr 2 is the partial trace over the second subsystem C r . The minimal dimension r of the auxiliary system is equal to the Choi rank. In particular, for Φ ∈ C(X ), the Stinespring representation of Φ can be written in the form Φ(X) = tr 2 U (X ⊗ |ψ ψ|)U † , where |ψ ψ| ∈ D(C r ) and U ∈ U(X ⊗ C r ).

# III. PROBABILISTIC QUANTUM ERROR CORRECTION

To inspect pQEC procedure, first, we should state conditions which determine when given noise channel is probabilistically correctable. For deterministic QEC, such conditions have been known for a long time and in the literature as the Knill-Laflamme conditions [29]. Let E = K ((E i ) i ) ∈ C(Y) be a given noise channel. Then, according to the Knill-Laflamme Theorem, E is perfectly correctable for X if and only if

for all i, j and some isometry operator S ∈ M(X , Y). In the following theorem we generalize the above, to cover probabilistically correctable noise channels.

Theorem 1 (Equivalent conditions for pQEC).

The following conditions are equivalent:

(A) There exist error-correcting scheme (S, R) ∈ sC(X , Y) × sC(Y, X ) and p > 0 such that

(D) There exist S * ∈ M(X , Y) and R * ∈ M(Y, X ) such that

and there exists i 0 , for which it holds R * E i0 S * = 0.

Moreover, if point (A) holds for S = K ((S k ) k ) and R = K ((R l ) l ), then R ∈ P(Y) from points (B) and (C) can be chosen to satisfy R = l R † l R l . It also holds that R l E i S k ∝ 1l X for any i, k, l. The proof of Theorem 1 is presented in Appendix A 2. Let us discuss the meaning of the conditions stated in Theorem 1. The condition (B) presents a general form of probabilistically correctable noise channels E. Such channels, after applying post-processing √ R behave as mixed isometry operations. They hide parts of an initial quantum information on orthogonal subspaces. The condition (C) may be used to calculate the maximum value of the probability p of successful error correction. For r = rank(J(E)) and d = dim(X ), s = dim(Y) we can introduce the optimization procedure: maximize: tr(M )

Moreover, one may get the form of a recovery subchannel R based on R, S = K ((S k ) k ) and M obtained from this optimization in the following way (see Appendix A 2):

1. Let M = U † DU be the spectral decomposition of M .

# For each

4. The recovery subchannel is given as

.

Finally, the condition (D) gives us a simple method to check if E = K ((E i ) r i=1 ) is probabilistically correctable for X . Let us compare the point (D) with Knill-Laflamme conditions. The latter, is a constraint satisfaction problem with r 2 quadratic constrains S † E † j E i S ∝ 1l X for the variable S ∈ M(X , Y), which satisfies S = 0. The parameters

In comparison, the conditions in the point (D) represent a constraint satisfaction problem with r bilinear constrains RE i S ∝ 1l X for the variables S ∈ M(X , Y) and R ∈ M(Y, X ). Additionally, it must hold RE i0 S = 0 for some i 0 ∈ {1, . . . , r}. In this problem, the parameters E i are arbitrary operators from M(Y), which satisfy span im(E † i ) : i = 1, . . . , r = Y (although a stronger condition holds i E † i E i = 1l Y , we will see in Section VI, it is more convenient to use the weaker version).

# IV. REALIZATION OF PQEC PROCEDURE

In this section, we will investigate the form of error-correcting scheme (S, R) which provides the maximal probability of successful error correction. For perfectly correctable noise channels, the encoding S can be realized by the isometry channel. This observation meaningfully reduces the complexity of finding error-correcting schemes -it is enough to consider a vector representation of pure states. Inspired by that, we ask if a similar behavior occurs in the probabilistic quantum error correction. The following proposition gives us some insight in the form of encoding and decoding.

Proposition 2. For a given channel E ∈ C(Y), let us fix an error-correcting scheme (S, R) ∈ sC(X , Y) × sC(Y, X ) such that RES = pI X , for some p > 0. Then, the following holds: The proof of Proposition 2 is presented in Appendix A 3. We may use Proposition 2 (A) to state a realization of pQEC procedure (see Figure 1). For a given noise channel E ∈ C(Y) let (S, R) ∈ C(X , Y) × sC(Y, X ) be an error-correcting scheme for which RES = pI X , where p > 0. The encoding channel S can be realized using the Stinespring representation given in the form S(X) = tr 2 U S XU † S . The state is then sent through E. The decoding subchannel R ∈ sC(Y, X ) can be realized by implementing the channel

In summary, the output of the whole procedure consists of a quantum state σ ∈ D(X ) and a classical label i ∈ {0, 1}. If the label i = 0 is obtained, we know that σ ∝ RES(ρ) = pρ, and hence, the output state can be accepted. Otherwise, if i = 1, the output state σ ∝ ΨES(ρ) should be rejected, as in general it may differ from ρ.

In Proposition 2 (C), we observed that using non-isometric channels S or formal subchannels R for perfectly correctable noise channels provides no advantage. Moreover, according to Theorem 1 (D), to predict if a noise channel is probabilistically correctable, we may consider only single Kraus encoding operations. However, among all conditions presented in Proposition 2 there is no condition, which in general allows us to restrict our attention to an isometry channel realization of S. Indeed, there is a class of noise channels E for which, in order to maximize the probability p of successful error correction, we need to consider a general channel realization of S. Paraphrasing, to obtain the best performance, we have to encode the initial state |ψ ψ| ∈ D(X ) into the mixed state S(|ψ ψ|). In Section V we will present a family of noise channels for which it is necessary to use mixed state encoding.

# V. NEED FOR MIXED STATE ENCODING

In this section, we provide an example of a parametrized family of noise channels {E R } R for which the mixed state encoding improves the probability of successful error correction. In our example we assume that X = C 2 and Y = C 4 . For each R ∈ P(C 4 ) satisfying R ≤ 1l C 4 let us define a noise channel E R ∈ C(C 4 ) given by the equation

We define the optimal probability p 0 of successful error correction as

We also define the optimal probability p 1 of successful error correction restricted to the pure state encoding:

Our claim, which we will present later, is that there exists a family of operators R for which p 0 (R) > p 1 (R).

We start with the following lemma, where we show the optimal error-correcting scheme (S, R) and a simplified version of the maximization problem p 0 (R).

Lemma 3. Let R ∈ P(C 4 ) and R ≤ 1l C 4 . Define Π R as a projector on the support of R. For E R defined in Eq. (11) we have the following simplified form of the maximization problem p 0 (R):

An optimal scheme (S, R) which achieves the probability p 0 (R), that is RE R S = p 0 (R)I C 2 , can be taken as

where P is an argument maximizing p 0 (R) in Eq. ( 14). Moreover, if there exists another optimal scheme ( S, R), that is RE R S = p 0 (R)I C 2 , then rank(J(S)) ≤ rank(J( S)).

The proof of Lemma 3 is presented in Appendix A 4. Let us separately consider two cases: rank(R) < 4 and rank(R) = 4. The first one will be discussed briefly as it will not support our claim.

Corollary 4. Let us take R ∈ P(C 4 ) such that R ≤ 1l C 4 and rank(R) < 4. Define Π R as a projector on the support of R. For the noise channel defined in Eq. (11) we have p 0 (R) = p 1 (R). Moreover, it holds

) where R -1 denotes Moore-Penrose pseudo-inverse.

The proof of Corollary 4 is presented in Appendix A 5. In the case when the operator R is invertible, the situation is more interesting. Let us focus on p 0 (R) obtained in Eq. ( 14). As Π R = 1l C 4 , the equation Π R (P ⊗ X)Π R = P ⊗ X is always satisfied. We can take P = tr(P )ρ, for ρ ∈ D(C 2 ). The inequality tr(P )

∞ . Hence, we get

To calculate p 1 (R) it will be sufficient to add the constraint S = K ((S)). According to Lemma 3 the optimal S is of the form

Then, we have

Proposition 5. Let us define an unitary matrix U ∈ U(C 4 ) which columns form the magic basis [32]

Let us also define a diagonal operator D(λ) := diag † (λ), which is parameterized by a 4-dimensional real vector λ = (λ 1 , λ 2 , λ 3 , λ 4 ), for which it holds 0 < λ i ≤ 1. For R = U D(λ)U † and the noise channel E R defined in Eq. (11) we have

The proof of Proposition 5 is presented in Appendix A 6. We can clearly see that in the case rank(R) = 4, there are operators R, for which the mixed state encoding improves the probability of successful error correction over the pure state encoding, p 0 (R) > p 1 (R). In general, the maximization problem in Eq. ( 17) intuitively supports the inequality

so it is possible, that the minimal value of it will be achieved for some mixed state ρ. We observed such behavior in Proposition 5 for R given in the spectral decomposition R = U D(λ)U † . The introduced family of noise channels is parameterized by a 4-dimensional vector λ = (λ 1 , . . . , λ 4 ), such that λ i ∈ (0, 1]. For almost all such λ we have p 0 (R) > p 1 (R). The only exception is the 3-dimensional subset defined by the relation

which describes the situation, when the pure state encoding match the mixed state encoding, p 0 (R) = p 1 (R). In an extremal case, e.g.

The family of parameters R introduced in Proposition 5 is not the only one for which the minimum value of

Therefore, the value of p 0 (R) is one-to-one related with the maximum value of the output min-entropy of the channel Φ (see for instance [33]). Especially, we can see, if the image of the Bloch ball under Φ is a three dimensional ellipsis and contains the maximally mixed state ρ * 2 in its interior, then the mixed state encoding provides benefits.

Finally, the noise channel E R defined for R from Proposition 5 is perfectly correctable for X = C 2 if and only if R = 1l C 4 . Interestingly, this suggests that perfectly correctable noise channels may constitute only a small subset of probabilistically correctable noise channels. This behavior will be the object of our investigation in the next section.

# VI. ADVANTAGE OF PQEC PROCEDURE

The goal of this section is to show that pQEC procedure corrects a wider class of noise channels than the QEC procedure based on Knill-Laflamme conditions Eq. ( 6). For any Euclidean spaces X , Y let us define two families of noise channels; these which are probabilistically correctable for X as ξ(X , Y), and these which are correctable perfectly for X as ξ 1 (X , Y):

We begin our analysis with some observations. Proposition 6. For any X , Y we have the following properties:

The proof of Proposition 6 is presented in Appendix A 7. We see that if dim(X ) = dim(Y), then there is no need to consider pQEC procedure. The situation changes if we encode the initial information into a larger space, dim(Y) > dim(X ). In the following theorem, we will show that ξ 1 (X , Y) ξ(X , Y) for dim(Y) > dim(X ). Theorem 7. Let X and Y be Euclidean spaces for which dim(X ) < dim(Y). Then, the set ξ 1 (X , Y) is a nowhere dense subset of ξ(X , Y).

The proof of Theorem 7 is presented in Appendix A 8.

# A. Choi rank of correctable noise channels

Intensity of a noise channel E can be connected with its Choi rank r = rank(J(E)). Given E in the Stinespring form, the Choi rank describes the dimension of an environment system which unitarily interacts with the encoded information. If the interaction is the weakest (r = 1) we deal with unitary noise channels, which are always perfectly correctable. The strongest interaction (r = dim(Y) 2 ) is a property of hardly correctable noise channels. For example, the maximally depolarizing channel E(Y ) = tr(Y )ρ * Y , which can not be corrected, has the maximal Choi rank. In the following theorem, we investigate the maximum Choi rank of probabilistically correctable noise channels ξ(X , Y) and compare it with the maximum Choi rank for ξ 1 (X , Y). Theorem 8. Let X and Y be some Euclidean spaces such that dim(Y) ≥ dim(X ). The following relations hold:

The proof of Theorem 8 is presented in Appendix A 9. In Proposition 6 we showed that if dim(X ) = dim(Y), then the pQEC procedure gives us no advantage. Indeed, the only reversible noise channels, in this case, are unitary noise channels. In the language of Choi rank, that means, if the Choi rank of a noise channel is equal to one, then it can be corrected. We can ask, what is the maximum value of r ∈ N, such that all noise channels which Choi rank is less or equal r, can be corrected perfectly or probabilistically, respectively. Formally speaking, for any X and Y we define the following quantities:

The quantity r 1 (X , Y) for a general noise model was studied in [34,35]. The authors of [34] calculated a lower bound for r 1 (X , Y) by using a technique of noise diagonalization along with Tverberg's theorem. They obtained the following result

It implies that 4 dim(Y) dim(X ) ≤ r 1 (X , Y). On the other hand, by using the Quantum packing bound [35] we may gain some insight of the upper bound for r 1 (X , Y). If we assume that we are allowed to use only non-degenerated codes, then for perfectly correctable E we have a bound of the form rank(J(E)) ≤ dim(Y) dim(X ) . In the next part of this section, we will improve the upper bound of r 1 (X , Y) without putting any additional assumptions. We also will estimate the behavior of r(X , Y). In the particular case X = C 2 and Y = C 4 , we will also show that r 1 (X , Y) < r(X , Y).

Let us start with the following simple, but important properties, required to study r(X , Y). We will notice, that for a constant Choi rank of the noise, it is easier to construct error-correcting scheme, if the dimension of Y is large.

Directly from Lemma 9 we receive the monotonicity of r(X ,

There exist two projectors Π 1 , Π 2 ∈ P(Y ), such that rank(Π 1 ) = rank(Π 2 ) = dim(Y) and for F = K ((Π 2 E i Π 1 ) i ) we have rank(tr 1 (J(F))) = dim(Y). Hence, if there exists a scheme (S, R) such that 0 = RFS ∝ I X , then E ∈ ξ(X , Y ). Eventually, we have

# B. Schur noise channels

In this subsection, we restrict our attention to a particular family of noise channels whose Kraus operators are diagonal in the computational basis. In the literature, these channels are referred to as Schur channels [30,Theorem 4.19]. We use them to study an upper bound for r(X , Y) and r 1 (X , Y).

Lemma 10. Let X and Y be Euclidean spaces such that dim(Y) ≥ dim(X ). Then, there exists a Schur channel

The proof of Lemma 10 is presented in Appendix A 10. The bounds obtained in Lemma 10 are asymptotically tight for Schur noise channels with dim(Y) → ∞. To prove the tightness of the bound for perfectly correctable noise channels, we may use the construction provided in [34]. Hence, if we take a Schur channel

In the following proposition we will prove the tightness for probabilistically correctable Schur noise channels.

Proposition 11. Let X and Y be Euclidean spaces and dim(X ) ≤ dim(Y). For any Schur channels

The proof of Proposition 11 is presented in Appendix A 11. In the case of Schur channels we have a clear separation between probabilistically and perfectly correctable noise channels.

# C. From bi-linear to linear problem

In general, the difficulty of finding error-correcting schemes (S, R) comes from bi-linearity of the problem Eq. (10). However, there is a particular class of noise channels, for which we can easily rewrite the bi-linear problem as a linear one. In this subsection, we will focus our attention on noise channels E ∈ C(Y), such that rank(E(1l Y )) = dim(X ). Note, that this assumption implies dim(X )rank(J(E)) ≥ dim(Y).

Let E = K ((E i ) i ) and let Π be the projector on the image of E(1l Y ). Consider an associated channel

) is an isometry operator with the image on the subspace defined by Π. It is clear that E is probabilistically correctable for a given space X if and only if there exists a scheme (S, R), such that 0 = RFS ∝ I X . Hence, according to Theorem 1 we need to find S * ∈ M(X , Y), R * ∈ M(X ), such that R * F i S * = c i 1l X and c i0 = 0 for some i 0 . Interestingly, we can combine together an action of S * , R * as just the action of some pre-processing S * ∈ M(X , Y), that is

Therefore, we obtained a linear problem equivalent to Eq. ( 10). In the following proposition we will investigate consequences of a such simplification.

Proposition 12. Let X and Y be some Euclidean spaces and dim(X ) ≤ dim(Y).

(B) There exists a noise channel E ∈ C(Y) such that rank(E(1l Y )) = dim(X ) and rank(J(E)) ≥ dim(Y) dim(X ) dim(X ) 2 -1 , for which we have E ∈ ξ(X , Y).

The proof of Proposition 12 is presented in Appendix A 12. Eventually, it is worth mentioning that the QEC procedure based on Knill-Laflamme conditions works well with this class of noise channels. Consider the situation dim(X )rank(J(E)) = dim(Y). Then, if E ∈ C(Y) and rank(E(1l Y )) = dim(X ), it holds E ∈ ξ 1 (X , Y). To see this, take the Kraus decomposition of E = K ((E i )) and notice that operators E i are orthogonal pieces of some unitary operator.

# D. Correctable noise channels with bounded Choi rank

In this subsection we will study the behavior of r(X , Y) and r 1 (X , Y). We will state a lower and a upper bound for both quantities.

Theorem 13. Let X and Y be some Euclidean spaces such that dim(Y) ≥ dim(X ). Then, we have

The proof of Theorem 13 is presented in Appendix A 13. Unfortunately, according to this theorem, there is no clear separation of r(X , Y) and r 1 (X , Y) for arbitrary X and Y. The improvement of these bounds will be investigated in the future.

For now, we will calculate explicitly r(X , Y) and r 1 (X , Y) for X = C 2 and Y = C 3 , C 4 .

Proposition 14. For all E ∈ C(C 4 ) satisfying rank(J(E)) ≤ 2 we have E ∈ ξ(C 2 , C 4 ).

The proof of Proposition 14 is presented in Appendix A 14. By using Theorem 13 and Proposition 14 we get the following advantage of pQEC protocol for X = C 2 and Y = C 4 .

Corollary 15. For X = C 2 and Y = C 4 we have

In particular, it holds

# E. Random noise channels

In the last subsection, we will show the advantage of pQEC procedure for randomly generated noise channels. We will follow the procedure of sampling quantum channels considered in [36][37][38].

Let r ∈ N and let (G i ) r i=1 ⊂ M(Y) be a tuple of random and independent Ginibre matrices (matrices with independent and identically distributed entries drawn from standard complex normal distribution). Define

We define a random channel E r ∈ C(Y) given as

This sampling procedure induces the measure P on C(Y) whose support is defined on {E ∈ C(Y) : rank(J(E)) ≤ r}.

Theorem 16. Let E r ∈ C(Y) be a random quantum channel defined according to Eq. (32). Then, the following two implications hold

The proof of Theorem 16 is presented in Appendix A 15. To answer this question, observe that the channel E satisfies rank(J(E)) ≤ 2. In Proposition 14 we noticed that such channels are probabilistically correctable for a given input space C 2 , if dim(Y) = 4 (in fact, from monotonicity for dim(Y) ≥ 4). Therefore, to correctly transfer a qubit state through E, we may define an error-correcting scheme with only two physical qubits.

We provide the following pQEC procedure based on Proposition 14.

Algorithm 17: Probabilistic QEC qubit code Input: E ∈ C(C 4 ) such that rank(J(E)) ≤ 2. Output: pQEC procedure with success probability p > 0.

Run the QEC procedure presented in Figure 2 for |ψ , U S , U R , V R . 10 Let σ exp be the output state of the procedure presented in Figure 2. Use the post-processing of the measurements' output (i, j) according to the following table:

Figure 2: The circuit representing the pQEC procedure. We have access to two physical qubits. The first qubit is in the state |ψ . This state will be encoded. The second state we set |0 . We implement two-qubit, encoding unitary operator U S . Then, the encoded state U S (|ψ ⊗ |0 ) is affected by the noise channel E. After that, we start the decoding procedure. We implement two-qubit unitary rotation U R . We measure the second qubit in the standard basis and obtain a classical label i ∈ {0, 1}. We prepare a third qubit in the state |0 and implement two qubit unitary rotation V R . We measure the third qubit in the standard basis and obtain a classical label j ∈ {0, 1}. If (i, j) = (0, 0) we accept the output state, otherwise, we reject it.

# VIII. GENERALIZATION OF PQEC PROCEDURE

Let us denote by Υ an arbitrary family of noise channels, that is Υ ⊂ C(Y). In this section, we ask if there exists error-correcting scheme (S, R), such that all noise channels E ∈ Υ we have RES = p E I X , for some p E ≥ 0. Note, that p E may differ for different noise channels E, hence, we shall introduce a quantity to "globally" control the effectiveness of (S, R). We propose the following approach.

Let µ be some probability measure defined on the set Υ. We assume that noise channels E ∈ Υ are probed according to µ. The scheme (S, R) will be a valid error-correcting scheme for Υ and µ if in average, the probability of successful error correction is non zero, that is

Without loss of the generality we may assume that Υ is convex. Additionally, we assume that the support of µ is equal to Υ. Usually, we can take µ as the flat measure, representing the maximal uncertainty in the process of probing random noise channels E from Υ. Let us define the average noise channel of Υ with respect to µ

We will show that we can correct all noise channels from the family Υ, whenever Ē is probabilistically correctable for X . We put this statement as the following proposition.

Proposition 18. Let Υ ⊂ C(Y) be a nonempty and convex family of noise channels. Define µ to be a probability measure defined on Υ and assume that the support of µ is equal to

The following conditions are equivalent:

The proof of Proposition 18 is presented in Appendix A 16.

# IX. DISCUSSION

In this work, we analyzed pQEC procedure for a general noise model. We established the conditions to check if a given noise channel is probabilistically correctable. Moreover, we showed that mixed state encoding should be taken into account when maximizing the probability of successful error correction. Finally, we pointed the advantage of the probabilistic error-correcting procedure over the deterministic one. We saw a clear separation especially for a correction of Schur noise channels and random noise channels. We obtained the maximum value of Choi rank of probabilistically correctable noise channels. We also provide a method how to probabilistically correct noise channels with bounded Choi rank.

There are many directions for further study that still remain to be explored. It would be interesting to strengthen Theorem 13 and show the separation between r(X , Y) and r 1 (X , Y) by improving the proposed proof technique in Appendix A 13. We obtained such separation for X = C 2 and Y = C 4 in Corollary 15. Another promising direction is to propose tools for the numerical analysis of pQEC protocols, based on Theorem 1. Such tools would help us estimate the value of r(X , Y) and gain an insight into probabilistically correctable noises that require mixed state encoding. Last but not least, we would like to calculate the worst-case probability of successful error correction for a given noise intensity r ≤ r(X , Y). For example, as we showed in Proposition 14, the errors caused by a unitary interaction with an auxiliary qubit system (r = 2), can be corrected by using only two physical qubits (dim(Y) = 4). We can ask, how many times in average the procedure presented in Algorithm 17 needs to be repeated. and there exists i 0 , for which it holds R * E i0 S * = 0.

Moreover, if point (A) holds for S = K ((S k ) k ) and R = K ((R l ) l ), then R ∈ P(Y) from points (B) and (C) can be chosen to satisfy R = l R † l R l . It also holds that R l E i S k ∝ 1l X for any i, k, l. Proof. In order to show that (A) ⇐⇒ (B) ⇐⇒ (C), in all implications presented below, we will use the same encoding S = K ((S k ) k ) ∈ sC(X , Y). Hence, to simplify the proof, we introduce the notation of F := ES given in the form

We will check that R is a subchannel. First, from the definition of R, it follows that R is completely positive. Second, from the assumption (B), operators α -1 i A i A † i ∈ P(Y) are orthogonal projectors and hence

It means that R ∈ sC(Y, X ). Finally, it holds

Hence, we get S † k0 S k0 = p k0 1l X . Define S = 1

Therefore, for any |ψ ψ| ∈ D(X ) we get

Observe that RES = I X . The rest of the proof follows from (B).

# Proof of Lemma 3

Lemma 3. Let R ∈ P(C 4 ) and R ≤ 1l C 4 . Define Π R as a projector on the support of R. For E R defined as

we have the following simplified form of the maximization problem p 0 (R):

An optimal scheme (S, R) which achieves the probability p 0 (R), that is RE R S = p 0 (R)I C 2 , can be taken as

where P is an argument maximizing p 0 (R) in Eq. (A25). Moreover, if there exists another optimal scheme ( S, R), that is RE R S = p 0 (R)I C 2 , then rank(J(S)) ≤ rank(J( S)).

Proof. Let us investigate the form of an optimal scheme (S, R) that maximize the probability p of successful error correction, RE R S = pI C 2 . First, one can note that R must be of the form

We obtain pI C 2 = RE R S = RF. From Theorem 1 we have R k F i ∝ 1l C 2 and there are k 0 , i 0 such that R k0 F i0 = 0. Hence, for each k we have R k ∝ F -1 i0 . That implies the operation R can be written as R(X) = RX R † . Now, consider another scheme (S , R ), where

Therefore, the scheme (S , R ) is also optimal and rank(J(S )) ≤ rank(J(S)).

To sum up, from now, we will consider the optimal scheme (S, R), where R(Y ) = tr 1 (Y (|0 0| ⊗ 1l C 2 )). The equation RE R S = pI C 2 can be rewritten as

for any X ∈ M(C 2 ). According to Theorem 1 we have

Without loss of the generality we may consider S such that Π R S(X)Π R = S(X) (one can note that rank(J(S)) will not increase). Hence, the equation

Therefore, basing on Eq. (A28) we can express the probability p 0 (R) as:

= max tr(P ) :

(A29)

# Proof of Corollary 4

Corollary 4. Let us take R ∈ P(C 4 ) such that R ≤ 1l C 4 and rank(R) < 4. Define Π R as a projector on the support of R. For the noise channel defined as

we have p 0 (R) = p 1 (R). Moreover, it holds

Proof. The proof is based on Lemma 3. Let us investigate the value of p 0 (R). We will consider three cases depending on rank(R).

In the first case, we assume that rank(R) ∈ {0, 1}. Then, for P satisfying Π R (P ⊗ X)Π R = P ⊗ X we have

Hence, we obtain rank(P ) ≤ 1 2 which implies P = 0. In this case p 0 (R) = 0. In the second case, we assume that rank(R) = 2. Using the same argumentation for P as in the first case, we get rank(P ) ≤ 1. We can write P = |x x| for |x ∈ C 2 . Note that, if P = 0, then from the equality Π R |x, y = |x, y for |y ∈ C 2 we get Π R = |ψ ψ| ⊗ 1l C 2 , for |ψ = 1

x |x . Therefore, if for all

∞ . In the third case, we assume that rank(R) = 3. Again, P can be written in the form 

6. Proof of Proposition 5

Proposition 5. Let us define an unitary matrix U ∈ U(C 4 ) which columns form the magic basis

Let us also define a diagonal operator D(λ) := diag † (λ), which is parameterized by a 4-dimensional real vector λ = (λ 1 , λ 2 , λ 3 , λ 4 ), for which it holds 0 < λ i ≤ 1. For R = U D(λ)U † and the noise channel E R defined as

we have

Proof. First, we calculate p 0 (R). Let |x = (x 0 , x 1 ) . Then, we have

). Eventually, we obtain the following upper bound

That means, p 0 (R) ≤ 4 tr(R -1 ) -1 . To saturate this bound, we take the maximally mixed state ρ = ρ * 2 and by using Eq. (A36) we calculate

Therefore, we showed that p 0 (R) = 4 tr(R -1 ) -1 .

In the case of p 1 (R), to calculate the largest eigenvalue of tr

One may calculate that the largest eigenvalue minimized over α is given by

It turns out, there are only two situations when this expression is minimized:

• For |x 0 | = 0 and |x 1 | = 1 (or equivalently |x 0 | = 1 and |x 1 | = 0), we obtain

Hence, the optimal value p 1 (R) equals (A) Take E = K ((E i ) r i=1 ) ∈ ξ 1 (X , Y), where r = rank(J(E)). From Proposition 2 there exist S = K ((S)) ∈ C(X , Y) and R ∈ C(Y, X ) such that RES = I X . According to Theorem 1 it holds

If r < r, then let us define A i = 0 for i = r + 1, . . . , r. There exists the Kraus decomposition E = K ((E i ) r i=1 ) such that A i = E i S for each i ≤ r. For A i = 0 images of A i are orthogonal and rank(A i ) = d. Hence, r d ≤ s which is equivalent to r ≤ k. For i > r it holds 1l Y ⊗ S |E i = 0. Note that the Kraus operators E i are linearly independent and it holds 

where

, where r = rank(J(E)). According to Theorem 1 (D) there exist S * ∈ M(X , Y) and R * ∈ M(Y, X ) such that R * E i S * ∝ 1l X , and there exists i 0 for which it holds R * E i0 S * = 0. We may assume that R * ∞ ≤ 1 and S * ∞ ≤ 1. Hence, according to Theorem 1 (B) we get

If r < r, then let us define A i = 0 for i = r + 1, . . . , r. There exists the Kraus decomposition

Let Π be the projector on the support of R † * R * . Observe that rank(Π) = d. Then, for each i ≤ r we have ΠA i = A i and for i ≤ r we have rank(A i ) = d. The relation A † j A i ∝ δ ij 1l X implies that there exists exactly one A i = 0, hence, r = 1.  

for E a defined in Eq. (A58). Observe that F i are linearly independent. We have that l-1 i=0

Now, we introduce a Schur channel F = K (F i ) l-1 i=0 ∈ C(Y). Assume indirectly that F ∈ ξ 1 (X , Y). Then, according to Proposition 2 and Theorem 1 there exists S ∈ M(X , Y), which satisfies S † S = 1l X and M ∈ M(C l ), such that S † F † j F i S = M ji 1l X . Therefore, we get Proof. Let ∆ ∈ C(Y) be the maximally dephasing channel, that is ∆(Y ) = i |i i|Y |i i|. Let us fix r such that r < dim(Y) dim(X )-1 . We will show that if E = K ((E i )) ∈ C(Y), such that E i = ∆(E i ) for each i and rank(J(E)) ≤ r, then E ∈ ξ(X , Y). Observe that the thesis is true in two particular situations:

# ACKNOWLEDGMENTS

This work was supported by the project "Near-term Quantum Computers: challenges, optimal implementations and applications" under Grant Number POIR.04.04.00-00-17C1/18-00, which is carried out within the Team-Net programme of the Foundation for Polish Science co-financed by the European Union under the European Regional Development Fund.

# Proof of Theorem 1

Theorem 1. Let E = K ((E i ) i ) ∈ C(Y). The following conditions are equivalent:

(A) There exist error-correcting scheme (S, R) ∈ sC(X , Y) × sC(Y, X ) and p > 0 such that RES = pI X .

(A1) (B) There exist S = K ((S k ) k ) ∈ sC(X , Y) and R ∈ P(Y), such that R ≤ 1l Y , for which it holds

# A2)

(C) There exist S = K ((S k ) k ) ∈ sC(X , Y), R ∈ P(Y), such that R ≤ 1l Y and a matrix M = [M jl,ik ] jl,ik = 0, for which it holds

(D) There exist S * ∈ M(X , Y) and R * ∈ M(Y, X ) such that

where we introduced p := i α i > 0.

(A) =⇒ (B)

Define Π R to be the projector on the support of R. One can show that R k Π R = R k for each k. We define R = K R k k , where

we get pI X = RF = R • K ( √ RF i ) i . As we have p > 0, it follows that K ( √ RF i ) i = 0. Hence, there exists a canonical decomposition

From the relationship between Kraus representations, it follows that A i satisfy Π R A i = A i . Then, by Choi-Jamiołkowski isomorphism we have

Therefore, from the extremality of the point |1l X 1l X | in P(X ⊗ X ) we have

for any i, k. On the one hand we get

and on the other hand

The above conditions provide that A † j A i = c ji 1l X , for some c ji ∈ C. Then, for i = j we have 0 = tr(A † j A i ) = c ji dim(X ) and eventually

From the relationship between Kraus decompositions K ( √ RF i ) i and K ((A i ) i ), there exists isometry operator U , such that

Therefore, it holds

That implies M ≥ 0. Take the spectral decomposition M = U † DU and define

Finally, A i = 0 if and only if D ii > 0 and by the fact M = 0 we conclude the set {A i : A i = 0} is not empty.

Using the Choi-Jamiołkowski isomorphism we get

Therefore, from the extremality of the point |1l X 1l X | in P(X ⊗ X ) we obtain R l E i S k ∝ 1l X . There exist l 0 , i 0 , k 0 such that R l0 E i0 S k0 = 0. We can take S * = S k0 and R * = R l0 .

(D) =⇒ (A) There exist q 0 , q 1 > 0 for which S := q 0 K ((S * )) ∈ sC(X , Y) and R := q 1 K ((R * )) ∈ sC(Y, X ). One may note that 0 = RES ∝ I X .

# Proof of Proposition 2

Proposition 2. For a given channel E ∈ C(Y), let us fix an error-correcting scheme (S, R) ∈ sC(X , Y) × sC(Y, X ) such that RES = pI X , for some p > 0. Then, the following holds:

Using Theorem 1 one can show that there exists k 0 for which rank(S k0 ) = dim(X ). Hence, S is invertible. Define S ∈ C(X , Y), R ∈ sC(Y, X ) given by the equations

From Theorem 1 there exists k 0 such that RES k0 = p k0 I X , for some p k0 > 0. For any |ψ ψ| ∈ D(X ) it holds then

and there exists i 0 for which it holds R * E i0 S * = 0. It implies that R * and S * are invertible, so for all i we have

# Proof of Theorem 7

Theorem 7. Let X and Y be Euclidean spaces for which dim(X ) < dim(Y). Then, the set ξ 1 (X , Y) is a nowhere dense subset of ξ(X , Y).

Proof. First, we will prove that ξ

As dim(X ) < dim(Y), there exists |y y| ∈ D(Y) such that y|A 1 = 0. Let us define a sequence of channels

given by

One can note that lim n→∞ E n = E. We take S n = S and R n = K (A † 1 ) for n ∈ N and obtain

Hence, we obtain E n ∈ ξ 1 (X , Y).

# Proof of Theorem 8

Theorem 8. Let X and Y be some Euclidean spaces such that dim(Y) ≥ dim(X ). The following relations hold:

We may assume that rank(J(E)) = r. Therefore, there exists a projector Π ∈ P(Y), such that rank(Π) = r and ∆(Π) = Π, and for which the operators ΠE i Π are linearly independent. Let us consider the operation

. By the recurrence and Theorem 1 for operation F there exist S * ∈ M (X , Y) and R * ∈ M (Y, X ), such that R * Π ⊥ E i Π ⊥ S * = c i 1l X and c i0 = 0 for some i 0 . Let |s ∈ C(Y) be the flat superposition. As ΠE i Π are diagonal and linearly independent, there exists the vector |r such that r|ΠE i Π|s = c i . We may define an encoding operator S * by adding a column Π|s to the operator Π ⊥ S * . In the same manner, we may construct R * by adding a row r|Π to the operator R * Π ⊥ . It is easy to check that S * , R * satisfy Theorem 1 (D), so E ∈ ξ(X , Y).

12. Proof of Proposition 12 Proposition 12. Let X and Y be some Euclidean spaces and dim(X ) ≤ dim(Y).

, where r = rank(J(E)). Assume that rank(E(1l Y )) = dim(X ) and r < dim(Y) dim(X ) dim(X ) 2 -1 . We can consider the equivalent form of the problem by taking the associated channel

As rank(F ) = dim(Y), the subspace {(F ⊗ 1l X )|S : |S } has the dimension dim(Y) dim(X ). On the other hand, the subspace {|c ⊗ |1l X : |c } has the dimension r. Therefore, as long as

there exists non-zero solution S ∈ M(X , Y) and |c ∈ C r , such that

we obtain E ∈ ξ(X , Y).

(B) In the part (A) of the proof we showed that

Therefore, in this proof, we will construct appropriate operator F , such that the latter condition holds. It would imply that the associated channel E is not probabilistically correctable. Formally, the operator F should be an isometry operator, but by Lemma 9, it is enough to define F such that rank(F ) = dim(Y). Let d = dim(X ), s = dim(Y) and fix r ∈ N, such that r ≥ sd d 2 -1 . We start with the case s = kd for k ∈ N. Consider the decomposition F = r-1 i=0 |i ⊗ F i , where F i ∈ M(Y, X ). For i = 0, . . . , k -1 we define

⊂ M(X ) be a basis of M(X ). For each i = k, . . . , r -1 we define

Observe, that rank(F ) = s. Let us take S which satisfies F i S ∝ 1l X for each i. Basing on the equations with indices i = 0, . . . , k -

hence, all entries c j are zeroed. It implies S = 0.

The case s = kd + l for l = 1, . . . , d -1 is more technically engaging than the previous case but it is based on the same idea. It will be only briefly discussed. For i = 0, . . . , k -1 we can define F i similarly as in the previous case, that is

where the image of N is contained in span(|j : j ≥ l). Here, the operator S which satisfy F i S ∝ 1l X has the form S ∼ |c ⊗ 1l X for some |c = k j=0 c j |j . We can choose N such that d(d -l) entries c j will be zeroed if F k S ∝ 1l X . Finally, operators F i for i = k + 1, . . . , r -1 has the analogous form as Eq. (A66) -each nullify (d 2 -1) entries. In total, the number of entries c j which can be zeroed is not less than k + 1. Indeed, it holds

Therefore, S = 0, which ends the proof.

# Proof of Theorem 13

Theorem 13. Let X and Y be some Euclidean spaces such that dim(Y) ≥ dim(X ). Then, we have

Proof. The inequality 4 dim(Y) dim(X ) ≤ r 1 (X , Y) follows directly from [34]. The inequalities

follow from Lemma 10 and Proposition 12, respectively. Now, we will show that dim(Y) dim(X )-1 -1 ≤ r(X , Y). Take arbitrary E ∈ C(Y) such that rank(J(E)) 2 (dim(X ) -1) < dim(Y). We will show E ∈ ξ(X , Y). Let us denote r = rank(J(E)). Consider a Kraus representation E = K (E j ) r j=1 and define the following set

Observe that dim(Y) ∈ A and if some s ∈ A, then sr ≥ dim(Y). Define s 0 = min(A) and consider a corresponding projector Π s0 ∈ P(Y), such that rank(Π s0 ) = s 0 and rank(E † (Π s0 )) = dim(Y). Let us take a orthonormal collection of vectors |v i , where i = 1, . . . , s 0 for which we have

From the assumption s 0 = min(A), for any i we get rank(E † (Π s0 -|v i v i |)) < dim(Y). Therefore, we may define vectors 0

Observe that for each i, there exists E j for which v i |E j |w i = 0. Let us define F j = [ v a |E j |w b ] a,b=1,...,s0 for j = 1, . . . , r. Note, that F j are diagonal operators and it holds j F † j F j > 0. From r 2 (dim(X ) -1) < dim(Y) and s 0 r ≥ dim(Y) we have

Utilizing Proposition 11, Lemma 9 and Theorem 1 there exist S * ∈ M(X , C s0 ) and R * ∈ M(C s0 , X ), such that R * F j S * ∝ 1l X and there exists j 0 , for which it holds R * F j0 S * = 0. That implies E ∈ ξ(X , Y).

# Proof of Proposition 14

Proposition 14. For all

we may write the singular decomposition of E 0 , E 1 in the form:

In order to show that E ∈ ξ(C 2 , C 4 ) we will use Theorem 1 (D). We will prove that there exist

for some c 0 , c 1 ∈ C satisfying (c 0 , c 1 ) = (0, 0). Let us introduce the following notation

Note that vectors |x i are orthogonal (the same holds for |y i ) and for each i = 0, . . . , 3 we have |x i = 0 or |y i = 0. We may write S * and R * in the following form

for some vectors |S 0 , |S 1 , |R 0 , |R 1 ∈ C 4 . The rest of the prove will be divided into three cases.

In the first case, we assume there exists i 3 ∈ {0, . . . , 3} such that vectors |x i3 , |y i3 are linearly independent. Define indices i 0 , i 1 , i 2 ∈ {0, . . . , 3} as the remaining labels, such that {i 0 , . . . , i 3 } covers the whole set {0, . . . , 3}. Let (a 0 , a 1 , a 2 ) ∈ C 3 be a normalized vector orthogonal to vectors ( y i3 |x i0 , y i3 |x i1 , y i3 |x i2 ) † and ( x i3 |y i0 , x i3 |y i1 , x i3 |y i2 ) † . Take |S 1 = |i 3 and |S 0 = a 0 |i 0 +a 1 |i 1 +a 2 |i 2 . Define |x = a 0 |x i0 +a 1 |x i1 +a 2 |x i2 and |y = a 0 |y i0 + a 1 |y i1 + a 2 |y i2 . We obtain 

Take |R 1 = b0 |x i3 + b1 |y i3 . Eventually, we may check that it holds

In the second case, we assume that there exists a pair of vectors |y i0 , |y i1 for i 0 = i 1 , such that |y i0 = |y i1 = 0. Then, the vectors |x i0 , |x i1 are orthonormal. We simply define

In the third case, for all i ∈ {0, . . . , 3} vectors |x i , |y i are not linearly independent and there is at most one zero vector |y i3 for some i 3 ∈ {0, . . . , 3}. Define indices i 0 , i 1 , i 2 ∈ {0, . . . , 3} as the remaining labels, such that {i 0 , . . . , i 3 } covers the whole set {0, . . . , 3}. Define the matrix

In the first sub-case we assume that rank(M ) = 1.

In the second sub-case we assume that rank(M ) = 2. Define indices j 1 , j 2 ∈ {0, 1, 2}, such that

Define j 0 ∈ {0, 1, 2} as the remaining label, such that {j 0 , j 1 , j 2 } covers the whole set {0, 1, 2}. Take |S 0 = |i j0 , |R 0 = |y ij 0 and define

We may take

15. Proof of Theorem 16

Theorem 16. Let E r ∈ C(Y) be a random quantum channel defined according to Eq. (32). Then, the following two implications hold

be a tuple of random and independent Ginibre matrices and Q

|i i| and consider the set

One can observe that P((G i ) r i=1 ∈ A) = 1. Let E r ∈ C(Y) be a random channel defined according to Eq. ( 32) for

Utilizing Lemma 9, Proposition 12 and Theorem 1 (D) for Ẽ = K ((ΠG i ) r i=1 ) ∈ sC(Y), there exist S, R, such that RΠG i S ∝ 1l X and RΠG i0 S = 0 for some i 0 . Eventually, E r ∈ ξ(X , Y). Now, for a given r ∈ N let us define B = {E r : E r ∈ ξ 1 (X , Y)}. From the assumption P(B) = 1, we obtain that B is a dense subset of {E ∈ C(Y) : rank(J(E)) ≤ r}. Imitating the proof of Theorem 7, we get that if E ∈ C(Y) and rank(J(E)) ≤ r, then E ∈ ξ 1 (X , Y). That implies r ≤ r 1 (X , Y). By using Lemma 10 we obtain the desired inequality.

# Proof of Proposition 18

Proposition 18. Let Υ ⊂ C(Y) be a nonempty and convex family of noise channels. Define µ to be a probability measure defined on Υ and assume that the support of µ is equal to Υ. Let Ē = Υ Eµ(dE) ∈ C(Y) and fix (S, R) ∈ sC(X , Y) × sC(Y, X ). The following conditions are equivalent:

(A) For each E ∈ Υ there exists p E ≥ 0 such that RES = p E I X and Υ p E µ(dE) > 0.

(B) It holds that 0 = R ĒS ∝ I X .

# Proof. (B) =⇒ (A)

Let us assume that R ĒS = pI X for p > 0. There exists a k dimensional affine subspace L such that Υ ⊂ L and int L (Υ) = ∅. Take arbitrary E 0 ∈ Υ. There exist E 1 , . . . , E k ∈ Υ such that convex hull of points E 0 , . . . , E k is a k-dimensional simplex ∆ k . For any state |ψ ψ| ∈ D(X ) it holds (A81)

Inside ∆ k each E can be uniquely represented as k i=0 q i (E)E i , where (q i (E)) k i=0 is a probability vector which depends on E. Hence,

# (|ψ ψ|).

(A82)

There exists small ball B around E 0 , such that for each channel E ∈ B ∩ ∆ k it holds q 0 (E) ≥ 1 2 . Hence, ∆ k q 0 (E)µ(dE) ≥ 1 2 µ (B ∩ ∆ k ) > 0, where in the last inequality we used the fact that the support of µ is equal to Υ. Therefore, it holds that for any |ψ ψ| ∈ D(X ) we have RE 0 S(|ψ ψ|) ∝ |ψ ψ| and from Lemma 19 there exists p E0 ≥ 0 such that RE 0 S = p E0 I X . The instant relation Υ p E µ(dE) = p > 0 ends the proof.

