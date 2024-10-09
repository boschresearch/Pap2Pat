# Introduction

This paper is motivated by a class of problems in graph deep learning, where the primary task is either graph classification or graph regression. In either case, the result should be invariant to arbitrary permutations of graph nodes.

As we explain below, the mathematical problem analyzed in this paper is a special case of the permutation invariance issue described above. To set the notations consider the vector space R n×d of n × d matrices endowed with the Frobenius norm X = trace(XX T ) 1/2 and its associated Hilbert-Schmidt scalar product, X, Y = trace(XY T ). Let S n denote the symmetric group of n × n permutation matrices. S n is a finite group of size |S n | = n!.

On R n×d we consider the equivalence relation ∼ induced by the symmetric group of permutation matrices S n as follows. Let X, Y ∈ R n×d . Then we say X ∼ Y if there is P ∈ S n so that Y = P X. In other words, two matrices are equivalent if one is a row permutation of the other. The equivalence relation induces a natural distance on the quotient space

This makes ( R n×d , d) a complete metric space.

Our main problem can now be stated as follows:

Problem 1.1. Given n, d ≥ 1 positive integers, find m and a bi-Lipschitz map α : ( R n×d , d) → (R m , • 2 ).

Explicitly the problem can be restated as follows. One is asked to construct a map α : R n×d → R m that satisfies the following conditions:

(1) If X, Y ∈ R n×d so that X ∼ Y then α(X) = α(Y ) (2) If X, Y ∈ R n×d so that α(X) = α(Y ) then X ∼ Y

(3) There are constants 0 < a 0 ≤ b 0 so that for any X, Y ∈ R n×d , (1.2)

Condition (1) allows us to lift α to the quotient space R n×d . Thus α( X) = α(X) is welldefined. Condition (2) says that α is injective (or, that α is faithful with respect to the equivalence relation ∼). Condition (3) says that α is bi-Lipschitz with constants a 0 , b 0 . By a slight abuse of notation, when α satisfies (1) we shall use the same letter to denote the map α : R n×d → R m as well as the induced map on the quotient space α : R n×d → R m . For X, Y ∈ R n×d , d(X, Y ) denotes the same quantity in (1.1) . In this case d is only a semi-distance on R n×d , i.e., it is symmetric, non-negative and satisfies the triangle inequality but fails the positivity condition.

One approach to embedding R n×d is to consider the convex set of probability measures on R d , P(R d ), and the map

where [x 1 , . . . , x n ] = X T , i.e., x k is the k th row of X reshaped as a vector, and δ denotes the Dirac measure. When P(R d ) is endowed with the Wasserstein-1 distance (the Earth Moving Distance), known also as the Kantorovich-Rubinstein metric,

x -y dπ(x, y)

the distance between a ∞ (X) and a ∞ (Y ) becomes

x k -(ΠY ) k .

By the Kantorovich-Rubinstein theorem ( [10]Theorem 1.14), d KR extends to a norm on the linear space of bounded signed Borel measures on R d , M b (R d ). It is easy to verify that

which proves that a ∞ provides an embedding into a normed linear space. Yet this embedding does not solve the problem since the linear space M b (R d ) is infinite dimensional. Instead of the previous infinite dimensional embedding, we consider two different classes of embeddings. To illustrate these two constructions, consider the simplest case d = 1.

(1) Algebraic Embedding. For x ∈ R n , x = (x 1 , . . . , x n ) T , construct the polynomial P x (z) = (z -x 1 ) • • • (z -x n ) and then expand the product:

. Using Vieta's formulas and Newton-Girard identities, an algebraically equivalent description of P x is given by the symmetric polynomials:

(1.4) α : R n → R n , α(x) = n k=1

x k , n k=1

x 2 k , . . . , n k=1

x n k .

It is not hard to see that this map satisfies Conditions (1) and (2) and therefore lifts to an injective continuous map α on Rn . Yet it is not Lipschitz, let alone bi-Lipschitz. The approach in [20] can be used to modify α to a Lipschitz continuous map, but, for the same reason as described in that paper, it cannot be "fixed" to a bi-Lipschitz embedding. In Section 2 we show how to construct an algebraic Lipschitz embedding in the case d > 1.

(2) Sorting Embedding. For x ∈ R n , consider the sorting map (1.5) ↓: R n → R n , ↓ (x) = (x π(1) , x π(2) , . . . , x π(n) ) T

where the permutation π is so that x π(1) ≥ x π(2) ≥ • • • ≥ x π(n) . It is obvious that ↓ satisfies Conditions (1) and (2) and therefore lifts to an injective map on R n×d . As we see in Section 3, the map ↓ is bi-Lipschitz. In fact it is isometric, and hence produces an ideal embedding. Our work in Section 3 is to extend such construction to the more general case d > 1.

The algebraic embedding is a special case of the more general kernel method that can be thought of as a projection of the measure a ∞ (X) onto a finite dimensional space, e.g., the space of polynomials spanned by {X, X 2 , • • • , X n }. In applications such kernel method is known as a "Readout Map" [40], based on "Sum Pooling".

The sorting embedding has been used in applications under the name of "Pooling Map" [40], based on "Max Pooling". A naïve extension of the unidimensional map (1.5) to the case d > 1 might employ the lexicographic order: order monotone decreasing the rows according to the first column, and break the tie by going to the next column. While this gives rise to an injective map, it is easy to see it is not even continuous, let alone Lipschitz. The main work in this paper is to extend the sorting embedding to the case d > 1 using a threestep procedure, first embed R n×d into a larger vector space R n×D , then apply ↓ in each column independently, and then perform a dimension reduction by a linear map into R 2nd . Similar to the phase retrieval problem ([2, 9, 4]), the redundancy introduced in the first step counterbalances the loss of information (here, relative order of one column with respect to another) in the second step.

A summary of main results presented in this paper is contained in the following result.

Theorem 1.2. Consider the metric space ( R n×d , d).

(1) (Polynomial Embedding) There exists a Lipschitz injective map

Two explicit constructions of this map are given in (2.8) and

(2.9). (2) (Sorting based Embedding) There exists a class of bi-Lipschitz maps

with m = 2nd, where each map βA,B is the composition of two bi-Lipschitz maps: a full-rank linear operator B : R n×D → R m , with the nonlinear bi-Lipschitz map βA : R n×d → R n×D parametrized by a matrix A ∈ R d×D called "key". Explicitly, β( X) =↓ (XA), where ↓ acts column-wise. These maps are characterized by the following properties: (b) For any matrix ("key") A ∈ R d×D such that the map βA is injective, then βA : ( R n×d , d) → (R n×D , • ) is bi-Lipschitz. Furthermore, an upper Lipschitz constant is given by s 1 (A), the largest singular value of A. (c) Assume A ∈ R d×D is such that the map βA is injective (i.e., a "universal key").

Then for almost any linear map B : R n×D → R 2nd the map βA,B = B • βA is bi-Lipschitz.

An immediate consequence of this result is the following corollary whose proof is included in subsection 3.5:

(1) For any continuous function f : R n×d → R invariant to row-permutation (i.e., f (P X) = f (X) for every X ∈ R n×d and P ∈ S n ) there exists a continuous function

Conversely, for any g : R m → R continuous function, the function f = g • β : R n×d → R is continuous and row-permutation invariant.

(2) For any Lipschitz continuous function f : R n×d → R invariant to row-permutation (i.e., f (P X) = f (X) for every X ∈ R n×d and P ∈ S n ) there exists a Lipschitz continuous function g : R m → R such that f = g•β. Conversely, for any g : R m → R Lipschitz continuous function, the function f = g • β : R n×d → R is Lipschitz continuous and row-permutation invariant.

The structure of the paper is as follows. Section 2 contains the algebraic embedding method and encoders α described at part (1) of Theorem 1.2. Corollary 2.3 contains part (1) of the main result stated above. Section 3 introduces the sorting based embedding procedure and describes the key-based encoder β. Necessary and sufficient conditions for key universality are presented in Proposition 3.8; the injectivity of the encoder described at part (2.a) of Theorem 1.2 is proved in Theorem 3.9; the bi-Lipschitz property of any universal key described at part (2.b) of Theorem 1.2 is shown in Theorem 3.10; the dimension reduction statement (2.c) of Theorem 1.2 is included in Theorem 3.13. Proof of Corollary 1.3 is presented in subsection 3.5. Section 4 contains applications to graph deep learning. These application use Graph Convolution Networks and the numerical experiments are carried out on two graph data sets: a chemical compound data set (QM9) and a protein data set (PROTEINS FULL).

While the motivation of this analysis is provided by graph deep learning applications, this is primarily a mathematical paper. Accordingly the formal theory is presented first, and then is followed by the machine learning application. Those interested in the application (or motivation) can skip directly to Section 4.

# Notations. For an integer

1.1. Prior Works. Several methods for representing orbits of vector spaces under the action of permutation (sub)groups have been studied in literature. Here we describe some of these results, without claiming an exhaustive literature survey.

A rich body of literature emanated from the early works on symmetric polynomials and group invariant representations of Hilbert, Noether, Klein and Frobenius. They are part of standard commutative algebra and finite group representation theory.

Prior works on permutation invariant mappings have predominantly employed some form of summing procedure, though some have alternatively employed some form of sorting procedure.

The idea of summing over the output nodes of an equivariant network has been well studied. The algebraic invariant theory goes back to Hilbert and Noether (for finite groups) and then continuing with the continuous invariant function theory of Weyl and Wigner (for compact groups), who posited that a generator function ψ : X → R gives rise to a function E : X → R invariant to the action of a finite group G on X, (g, x) → g.x, via the averaging formula

More recently, this approach provided the framework for universal approximation results of G-invariant functions. [27] showed that invariant or equivariant networks must satisfy a fixed point condition. The equivariant condition is naturally realized by GNNs. The invariance condition is realized by GNNs when followed by summation on the output layer, as was further shown in [21], [28] and [30]. Subsequently, [39] proved universal approximation results over compact sets for continuous functions invariant to the action of finite or continuous groups. In [16], the authors obtained bounds on the separation power of GNNs in terms of the Weisfeiler-Leman (WL) tests by tensorizing the input-output mapping. [35] studied approximations of equivariant maps, while [11] showed that if a GNN with sufficient expressivity is well trained, it can solve the graph isomorphism problem.

The authors of [36] designed an algorithm for processing sets with no natural orderings. The algorithm applies an attention mechanism to achieve permutation invariance with the attention keys being generated by a Long-Short Term Memory (LSTM) network. Attention mechanisms amount to a weighted summing and therefore can be considered to fall within the domain of summing based procedures.

In [24], the authors designed a permutation invariant mapping for graph embeddings. The mapping employs two separate neural networks, both applied over the feature set for each node. One neural network produces a set of new embeddings, the other serves as an attention mechanism to produce a weighed sum of those new embeddings.

Sorting based procedures for producing permutation invariant mappings over single dimensional inputs have been addressed and used by [40], notably in their max pooling procedure.

The authors of [31] developed a permutation invariant mapping pointnet for point sets that is based on a max function. The mapping takes in a set of vectors, processes each vector through a neural network followed by an scalar output function, and takes the maximum of the resultant set of scalars.

The paper [41] introduced SortPooling. SortPooling orders the latent embeddings of a graph according to the values in a specific, predetermined column. All rows of the latent embeddings are sorted according to the values in that column. While this gives rise to an injective map, it is easy to see it is not even continuous, let alone Lipschitz. The same issue arises with any lexicographic ordering, including the well-known Weisfeiler-Leman embedding [37]. Our paper introduces a novel method that bypasses this issue.

As shown in [28], the sum pooling-based GNNs provides universal approximations for of any permutation invariant continuous function but only on compacts. Our sorting based embedding removes the compactness restriction as well as it extends to all Lipschitz maps.

While this paper is primarily mathematical in nature, methods developed here are applied to two graph data sets, QM9 and PROTEINS FULL. Researchers have applied various graph deep learning techniques to both data sets. In particular, [17] studied extensively the QM9 data set, and compared their method with many other algorithms proposed by that time.

# Algebraic Embeddings

The algebraic embedding presented in this section can be thought of a special kernel to project equation (1.3) onto.

2.1. Kernel Methods. The kernel method employs a family of continuous kernels (test) functions, {K(x; y)

The embedding problem 1.1) can be restated as follows. One is asked to find a finite family of kernels {K(x; y)

is injective, Lipschitz or bi-Lipschitz. Two natural choices for the kernel K are the Gaussian kernel and the complex exponential (or, the Fourier) kernel:

where in both cases Y ⊂ R d . In this paper we analyze a different kernel, namely the polynomial kernel

2.2. The Polynomial Embedding. Since the polynomial representation is intimately related to the Hilbert-Noether algebraic invariants theory [18] and the Hilbert-Weyl theorem, it is advantageous to start our construction from a different perspective. The linear space R n×d is isomorphic to R nd by stacking the columns one on top of each other. In this case, the action of the permutation group S n can be recast as the action of the subgroup I d ⊗ S n of the bigger group S nd on R nd . Specifically, let us denote by ∼ G the equivalence relation

induced by a subgroup G of S nd . In the case G = I d ⊗ S n = {diag d (P ) , P ∈ S n } of block diagonal permutation obtained by repeating d times the same P ∈ S n permutation along the main diagonal, two vectors x, y ∈ R nd are ∼ G equivalent iff there is a permutation matrix P ∈ S n so that y(1 + (k -1)n : kn) = P x(1 + (k -1)n : kn) for each 1 ≤ k ≤ d. In other words, each disjoint n-subvectors in y and x are related by the same permutation. In this framework, the Hilbert-Weyl theorem (Theorem 4.2, Chapter XII, in [25]) states that the ring of invariant polynomials is finitely generated. The Göbel's algorithm (Section 3.10.2 in [18]) provides a recipe to find a complete set of invariant polynomials. In the following we provide a direct approach to construct a complete set of polynomial invariants.

Let R[x 1 , x 2 , ..., x d ] denote the algebra of polynomials in d-variables with real coefficients. Let us denote X ∈ R n×d a generic data matrix. Each row of this matrix defines a linear form over x 1 , ...

the algebra of polynomials in variable t with coefficients in the ring R[x 1 , . . . ,

by rearranging the terms according to degree in t.

can be encoded as zeros of a polynomial P X of degree n in variable t with coefficients in R[x 1 , . . . , x d ]:

(2.2)

x d ] denote the vector space of homogeneous polynomials in d + 1 variables of degree n with real coefficients. Notice the real dimension of this vector space is

By noting that P X is monic in t (the coefficient of t n is always 1) we obtain an injective embedding of (1.4). This is summarized in the following theorem:

Specifically, for X ∈ R n×d expand the polynomial (2.4)

where the index set is given by

The map α0 : R n×d → R m-1 is the lifting of α 0 to the quotient space.

# Proof

Since for any permutation π with associated permutation matrix Π ∈ S n ,

it follows that α 0 is invariant to the action of S n , α 0 (X) = α 0 (ΠX). Thus α 0 lifts to a map α0 on R n×d . The coefficients of polynomial P X depend analytically on its roots (Vieta's formulas), hence on entries of matrix X.

The only remaining claim is that if X, Y ∈ R n×d so that α 0 (X) = α 0 (Y ) then there is Π ∈ S n so that Y = ΠX. Assume P X = P Y . For each choice (x 1 , x 2 , . . . , x d ) = (f (1), . . . , f (d)) in R d , the n real zeros of the two polynomials in t, P X (t, f (1), . . . , f (d)) and

)n! and choose F ∈ R d×D so that each subset of d columns are linearly independent, in other words, the set F = {f 1 , f 2 , . . . , f D } formed by the D columns of F is a full spark frame in R d , see [1]. As proved in [1], almost every such set is a full spark frame. Then for each 1

The set of invariants produced by map α 0 are proportional to those produced by the Göbel's algorithm in [18], §3.10.2. Indeed, the nd primary invariants are given by

corresponding to the elementary symmetric polynomials in entries of each column. The secondary invariants correspond to the remaining coefficients that have at least 2 nonzero indices among p 1 , . . . , p d .

The embedding provided by α 0 is analytic and injective but is not globally Lipschitz because of the polynomial growth rate. Next we show how a simple modification of this map will make it Lipschitz. First, let us denote by L 0 the Lipschitz constant of α 0 when restricted to the closed unit ball

be a Lipschitz monotone decreasing function with Lipschitz constant 1.

Corollary 2.3. Consider the map:

(2.8)

The map α 1 lifts to an injective and globally Lipschitz map α1 :

is the nearest-point map to (or, the metric projection map onto) the convex closed set

(ii) The nearest-point map to a convex closed subset of a Hilbert space is Lipschitz with constant 1, i.e. it shrinks distances, see [29].

These two observations yield:

This concludes the proof of this result.

A simple modification of φ 0 can produce a C ∞ map by smoothing it out around x = 1.

On the other hand the lower Lipschitz constant of α1 is 0 due to terms of the form X k i,j

with k ≥ 2. In [20], the authors built a Lipschitz map by a retraction to the unit sphere instead of unit ball. Inspired by their construction, a modification of α 0 in their spirit reads:

(2.9)

It is easy to see that α 2 satisfies the non-parallel property in [20] and is Lipschitz with a slightly better constant than α 1 (the constant is determined by the tangential derivatives of α 0 ). But, for the same reasons as in [20] this map is not bi-Lipschitz. 

# 2

-1. On the other hand, consider the following approach. Each row of X defines a complex number

that can be encoded by one polynomial of degree

The coefficients of Q provide a 2n-dimensional real embedding ζ 0 ,

), Im(q n-1 ), . . . , Re(q 0 ), Im(q 0 ))

with properties similar to those of α 0 . One can similarly modify this embedding to obtain a globally Lipschitz embedding ζ1 of R n,2 into R 2n+1 . It is instructive to recast this embedding in the framework of commutative algebras. Indeed, let x 1 -1, x 2  2 + 1 denote the ideal generated by polynomials x 1 -1 and

]) denote the vector space projected through this quotient map. Then a basis for S is given by {1, t, . . . , t n , x 2 , x 2 t, . . . ,

denote the set of polynomials realizable as in (2.4). Then the fact that ζ0 : R n×2 → R 2n is injective is equivalent to the fact that σ| S : S → S is injective. On the other hand note

where the last linear subspace is of dimension 2n.

In the case d = 2 we obtain the identification R Remark 2.4. One may ask the question whether the quaternions can be utilized in the case d = 4. While the quaternions form an associative division algebra, unfortunately polynomials have in general an infinite number of factorization. This prevents an immediate extension of the previous construction to the case d = 4.

Remark 2.5. Similar to the construction in [20], a linear dimension reduction technique may be applicable here (which, in fact, may answer the open problem above) which would reduce the embedding dimension to m = 2nd + 1 (twice the intrinsec dimension plus one for the homogenization variable). However we did not explore this approach since, even if possible, it would not produce a bi-Lipschitz embedding. Instead we analyze the linear dimension reduction technique in the next section in the context of sorting based embeddings.

# Sorting based Embedding

In this section we present the extension of the sorting embedding (1.5) to the case d > 1. The embedding is performed by a linear-nonlinear transformation that resembles the phase retrieval problem. Consider a matrix A ∈ R d×D and the induced nonlinear transformation:

where ↓ is the monotone decreasing sorting operator acting in each column independently. Specifically, let Y = XA ∈ R n×D and note its column vectors Y = [y 1 , y 2 , . . . , y D ]. Then

for some Π 1 , Π 2 , . . . , Π D ∈ S n so that each column is sorted monotonically decreasing:

Note the obvious invariance β A (ΠX) = β A (X) for any Π ∈ S n and X ∈ R n×d . Hence β A lifts to a map βA on R n×d .

Remark 3.1. Notice the similarity to the phase retrieval problem, e.g., [4], where the data is obtained via a linear transformation of the input signal followed by the nonlinear operation of taking the absolute value of the frame coefficients. Here the nonlinear transformation is implemented by sorting the coefficients. In both cases it represents the action of a particular subgroup of the unitary group.

In this section we analyze necessary and sufficient conditions so that maps of type (3.1) are injective, or injective almost everywhere. First a few definitions.

In general we refer to A as a key for encoder β A .

In other words, βA -1 ( βA ( X)) = { X}. We let A D (X), or simply A(X), denote the set of admissible keys for X.

For a key A, we let S n (A), or simply S(A), denote the set of matrices separated by A. Thus a matrix X ∈ S n (A) if and only if, for any matrix

Thus a key A is universal if and only if S n (A) = R n×d . Our goal is to produce keys that are admissible for all matrices in R n×d , or at least for almost every data matrix. As we show in Proposition 3.6 below this requires that D ≥ d and A is full rank. In particular this means that the columns of A form a frame for R d .

3.1. Characterizations of A(X) and S(A). We start off with simple linear manipulations of sets of admissible keys and separated data matrices. Proposition 3.5. Fix A ∈ R d×D and X ∈ R n×d .

(1) For an invertible

In other words, if X is separated by A then XT -1 is separated by T A.

(2) For any permutation matrix L ∈ S D and diagonal invertible matrix Λ ∈ R D×D ,

In other words, if X is separated by A then X is separated also by ALΛ as well as by AΛL.

In other words, if A is an admissible key for X then T -1 A is an admissible key for XT .

# Proof

The proof is immediate, but we include it here for convenience of the reader.

(

The reverse include follows by replacing A with T A and T with T -1 . Together they prove (3.2).

(

where L 0 is the permutation matrix that has 1 on its main antidiagonal.

Either way, ↓ ((XA) j ) =↓ ((Y A) j ). Hence ↓ (XA) =↓ (Y A). Therefore X ∼ Y and thus X ∈ S n (ALΛ). This shows S n (A) ⊂ S n (ALΛ). the reverse inclusion follows by a similar argument. Finally, notice {LΛ} forms a group since L -1 ΛL is also a diagonal matrix. This shows S n (AΛL) = S(ALΛ ) for some diagonal matrix Λ , and the conclusion (3.3) then follows.

( 

(2) The set B is generic with respect to Zariski topology, i.e., open and dense. Specifically, its complement is the zero set of the polynomial

(3) For an invertible matrix A ∈ R d×d ,

. Hence almost every matrix (w.r.t. Lebesgue measure) X ∈ R n×d is not separated by A.

# Proof

(1) We need to show that any matrix X that on some columns k and l has distinct elements on same row positions is not separated by I d . Indeed if X is such a matrix, let Y denote a copy of X except on those 4 entries where we set

Note X ∼ Y yet ↓ (X) =↓ (Y ). Hence such matrices are not separated by I d .

(2) By negation, the complement of B is given by

)} This shows B c is the zero set of polynomial P as claimed. Thus B c is a closed Zariski set. Its complement is generic with respect to the Zariski topology since B c = R n×d .

(3) The inclusion is immediate. Density claim follows from this inclusion.

On the other hand, extending the identity matrix by only one column produces an almost universal key: Proposition 3.7. Assume d ≥ 2 and n ≥ 3.

Let a ∈ R d be a vector with non-zero entries, i.e.,

be a key. Then S n (A) is generic with respect to the Zariski topology (i.e., open and dense), however S n (A) = R n×d . In particular, its complement S n (A) c := R n×d \ S n (A) is non-empty but has Lebesgue measure zero. Thus almost every matrix X ∈ R n×d is separated by A.

# Proof

First we show that S n (A) = R n×d . Consider the matrices X, Y ∈ R n×d full of zeros except for the 3x2 top left corner where:

the two left columns and the last column contain 1, 0 repeated n -2 times and -1) and yet X ∼ Y .

Next we show that S n (A) c is included in a finite union of linear spaces each of positive codimension. This proves the clam.

To simplify notation we introduce the following two operators. Let Π, Π 0 , Π 1 , • • • , Π d ∈ S n denote permutation matrices of size n. For X ∈ R n×d denote by x 1 , . . . , x d its columns. Thus

This is equivalent to say: 

This show that ker L Π0,Π1,...,Π d = R n×d and hence it is a subspace of positive codimension. We obtain:

This shows that S n (A) c is included in a finite union of proper subspaces of R n×d which in turn is a closed set with respect to the Zariski topology of empty interior. This ends the proof of this result.

The next result provides a characterization of the set S n (A). To do so we need to introduce additional notation that extends the operators L Π0,...,Π d and M Π,...,Π d defined in the proof of Proposition 3.7. For where δ k = (0, . . . , 0, 1, 0, . . . , 0) T has only one 1 on the k th position.

# Proof

The proof is a consequence of linear algebra analysis of map β A .

(1) Assume X is not separated by A. Then there is

implies that there are permutation matrices Π 1 , . . . , Π d , Ξ 1 , . . . , Ξ D-d ∈ S n so that:

Substituting the expressions for y 1 , . . . , y d provided by the first d equations into the latter D -d equations, we obtain part 1.(a).

For same Y , the condition X ∼ Y implies that for every Π ∈ S n , Y -ΠX = 0. Thus part 1(b) is proved.

(3) Equation (3.9) is a transcription of part 1.

(2) Equation (3.8) follows from (3.9) by taking the complement.

3.2. Construction of universal keys. In this subsection we construct universal keys. Proposition 3.8 provides us with an algorithm to check whether a key A is universal. Unfortunately the algorithm has an exponential complexity in data size.

If the key A ∈ R d×D is universal then A must have full rank. Therefore there are permutation matrix L ∈ S D and invertible T ∈ GL(d, R) so that A = T I d Ã L, with Ã ∈ R d×(D-d) . Proposition 3.5 shows that A is a universal key if and only if I d Ã is a universal key. This observation allows us to prove the main result of this subsection stated earlier as part b of Theorem 2.1. Recall a set of vectors {f 1 , . . . , f m } in a linear space V of finite dimension n ≤ m is called a full spark frame if any subset of n vectors is linearly independent. See [1,26] for more information and explicit constructions of full spark frames. Theorem 3.9. Consider the metric space ( R n×d , d). Set D = 1 + (d -1)n! and let A ∈ R d×D be a matrix whose columns form a full spark frame, i.e., any subset of d columns is linearly independent. Then the key A is universal and the induced map βA : 

where all norms are Frobenius norms.

# Proof

Let a 1 , . . . , a D denote the columns of

Fix X, Y ∈ R n×d two matrices. Then there are permutation matrices P 0 , Π 1 , . . . , Π D , Ξ 1 , . . . , Ξ D ∈ S n so that d( X, Ŷ ) = P 0 X -Y and

Permutations Π k and Ξ k satisfy the optimality condition:

where we obtain the upper bound in (3.10). The lower bound in (3.10) follows from the pigeonhole principle similar to the one employed in the proof of Theorem 2.1. In equation (3.11) there are D = 1 + (d -1)n! terms. Since only n! permutations are distinct, there is a permutation Q that repeats at least d times.

The lower bound in (3.10) implies that βA : R n×d → R n×D is injective and hence A is a universal key. This ends the proof of Theorem 3.9.

# 3.3.

Bi-Lipschitz properties of universal keys. In this subsection we prove that any universal key defines a bi-Lipschitz encoding map, regardless of D.

Theorem 3.10. Assume the key A ∈ R d×D is universal, i.e., the induced map βA : R n×d → R n×D , X → β A (X) =↓ (XA) is injective. Then βA is bi-Lipschitz, that is, there are constants a 0 > 0 and b 0 > 0 so that for all X, Y ∈ R n×d ,

where all are Frobenius norms. Furthermore, an estimate for b 0 is provided by the largest singular value of A, b 0 = s 1 (A).

# Proof

The upper bound in (3.13) follows as in the proof of Theorem 3.9, from equations (3.11) and (3.12). Notice that no property is assumed in order to obtain the upper Lipschitz bound.

The lower bound in (3.13) is more difficult. It is shown by contradiction following the strategy utilized in the Complex Phase Retrieval problem [6].

# Assume inf X ∼Y

Step 1: Reduction to local analysis. Since d( t X, t Y ) = t d( X, Ŷ ) for all t > 0, the quotient

is scale invariant. Therefore, there are sequences (X t ) t , (Y t ) t with Y t ≤ X t = 1 and d( Xt , Ŷ t ) > 0 so that lim t→∞

= 0. By compactness of the closed unit ball, one can extract convergence subsequences. For easiness of notation, assume (X t ) t , (Y t ) t are these subsequences. Let X ∞ = lim t X t and Y ∞ = lim t Y t denote their limits. Notice lim

This means that, if the lower Lipschitz bound vanishes, then this is achieved by vanishing of a local lower Lipschitz bound. To follow the terminology in [6], the type I local lower Lipschitz bound vanishes at some Z 0 ∈ R n×d , with Z 0 = 1:

Note that, in general, the infimum of the type I local lower Lipschitz bound over the unit sphere may be strictly larger than the global lower Lipschitz bound (see Theorems 2.1 and Theorem 2.2 in [6] and Theorem 4.3 in [5]). The compactness argument forces the local lower Lipschitz bound to vanish when the global lower bound vanishes.

. This is immediate after squaring (b) and simplifying the terms.

Consider now sequences ( Xt ) t , ( Ŷ t ) t that converge to Ẑ0 and achieve lower bound 0 as in (3.14). Choose representatives X t and Y t in their equivalence classes that satisfy the hypothesis of Lemma 3.11 so that

for some Π j,t ∈ S n . In fact Π j,t ∈ argmin Π∈Hj U t -ΠV t )a j 2 . Pass to sub-sequences (that will be indexed by t for an easier notation) so that Π j,t = Π j for some Π j ∈ S n . Thus

Since the above sequence must converge to 0 as t → ∞, while U t , V t → 0, it follows that necessarily Π j ∈ H j and the expressions simplify to

Thus equation (3.14) implies that for every j ∈ [D], (3.15) lim

where Π j ∈ H j , U t , V t → 0, and U t , V t are aligned so that U t , V t ≥ P U t , V t for every P ∈ G. Equivalently, relation (3.14) can be restated as:

for some permutations Π j ∈ H j , j ∈ [D]. By Lemma 3.11 the constraint in the optimization problem above implies U -V = min P ∈G U -P V . Hence (3.16) implies:

for same permutation matrices Π j 's. While the above optimization problem seems a relaxation of (3.16), in fact (3.17) implies (3.16) with a possibly change of permutation matrices Π j , but remaining still in H j .

Step 3. Existence of a Minimizer. The optimization problem (3.16) is a Quadratically Constrained Ratio of Quadratics (QCRQ) optimization problem. A significant number of papers have been published on this topic [7,8]. In particular, [3] presents a formal setup for analysis of QCRQ problems. Our interest is to utilize some of these techniques in order to establish the existence of a minimizer for (3.16) or (3.17). Specifically we show: Lemma 3.12. Assume the key A has linearly independent rows (equivalently, the columns of A form a frame for R d ) and the lower Lipschitz bound of βA is 0. Then there are Ũ , Ṽ ∈ R n×d so that:

(1) Ũ = P Ṽ , for every P ∈ G;

(2) For every j ∈ [D], ( Ũ -Π j Ṽ )a j = 0.

# Proof of Lemma 3.12

We start with the formulation (3.17). Therefore there are sequences (U t , V t ) t≥1 so that U t = P V t for any P ∈ G, t ≥ 1, and yet for any P ∈ G,

} denote the null space of the linear operator

associated to the numerator of the above quotient. Let F P = {(U, V ) ∈ R n×d × R n×d , U -P V = 0} be the null space of the linear operator

A consequence of (3.17) is that for every P ∈ G, E\F P = ∅. In particular, F p ∩E is a subspace of E of positive codimension. Using the Baire category theorem (or more elementary linear algebra arguments), we conclude that

Let ( Ũ , Ṽ ) ∈ E \ (∪ P ∈G F P ). This pair satisfies the conclusions of Lemma 3.12.

Step 4. Contradiction with the universality property of the key. So far we obtained that if the lower Lipschitz bound of βA vanishes than there are Z 0 , Ũ , Ṽ ∈ R n×d with Z 0 = 0 and Ũ = P Ṽ , for all P ∈ G that satisfy the conclusions of Lemma 3.12. Notice Z 0 , Z 0 = P Z 0 , Z 0 for all P ∈ G and (Z 0 -Π j Z 0 )a j = 0 for all j ∈ [D]. Choose s > 0 but small enough so that s Ũ , s Ṽ < 1 4 δ 0 with δ 0 = min P ∈Sn\G (I n -P )Z 0 . Let X = Z 0 + s Ũ and Y = Z 0 + s Ṽ . Then Lemma 3.11 implies d( X, Ŷ ) = min P ∈G Ũ -P Ṽ > 0. Hence X = Ŷ . On the other hand, for every j ∈ [D], Xa j = Π j Y a j . Thus βA ( X) = βA ( Ŷ ). Contradiction with the assumption that βA is injective.

This ends the proof of Theorem 3.10.

3.4. Dimension Reduction. Theorem 3.9 provides an Euclidean bi-Lipschitz embedding of very high dimension, D = 1 + (d -1)n!. On the other hand, Theorem 3.10 shows that any universal key A ∈ R d×D for R n×d , and hence any injective map βA is bi-Lipschitz. In this subsection we show that any bi-Lipschitz Euclidean embedding βA : R n×d → R n×D with D > 2d can be further compressed to a smaller dimension space R m with m = 2nd thus yielding bi-Lipschitz Euclidean embeddings of redundancy 2. This is shown in the next result.

Theorem 3.13. Assume A ∈ R d×D is a universal key for R n×d with D ≥ 2d. Then, for m ≥ 2nd, a generic linear operator B : R n×D → R m with respect to Zariski topology on R n×D×m , the map

is bi-Lipschitz. In particular, almost every full-rank linear operator B : R n×D → R 2nd produces such a bi-Lipschitz map.

Remark 3.14. The proof shows that, in fact, the complement set of linear operators B that produce bi-Lipschitz embeddings is included in the zero-set of a polynomial.

Remark 3.15. Putting together Theorems 3.9, 3.10, 3.13 we obtain that the metric space R n×d admits a global bi-Lipschitz embedding in the Euclidean space R 2nd . This result is compatible with a Whitney embedding theorem (see §1.3 in [19]) with the important caveat that the Whitney embedding result applies to smooth manifolds, whereas here R n×d is merely a non-smooth algebraic variety.

Remark 3.16. These three theorems are summarized in part two of the Theorem 2.1 presented in the first section.

Remark 3.17. While the embedding dimension grows linearly in nd, in fact m = 2nd, the computational complexity of constructing βA,B is NP due to the 1 + (d -1)n! intermediary dimension.

Remark 3.18. As the proofs show, for D ≥ 1 + (d -1)n!, a generic (A, B) with respect to Zariski topology, A ∈ R d×D and linear map B : R n×D → R 2nd , produces a bi-Lipschitz embedding ( βA,B , d) of R n×d into (R 2nd , • 2 ).

# Proof of Theorem 3.13

The proof follows a similar approach as in Theorem 3 of [20]. See also [13].

Without loss of generality, assume m < nD. Notice β A : R n×d → R n×D is already homogeneous of degree 1 (with respect to positive scalars). Let ∆ :

for some P 1 , . . . , P D , Q 1 , . . . , Q D ∈ S n , so that for each k ∈ [D], P k , Q k are permutations that sort monotone decreasingly vectors Xa k and Y a k , respectively. In particular,

where the (n!) 2D linear operators L γ : R n×d × R n×d → R n×D , are defined by

Claim: We claim that, for m ≥ 2nd and a generic linear operator B : R n×D → R m we have ker(B) ∩ F = {0}. Such a generic linear operator has the kernel of dimension dim(ker(B)) = nD -m ≤ n(D -2d). It is therefore sufficient to show that, for a generic subspace V ⊂ R n×D of dimension r ≤ n(D -2d), for every γ ∈ (S n ) 2D , V ∩ F γ = {0}. This last claim follows from the observation dim(F γ ) ≤ 2nd.

We now show how this claim proves the Theorem. Let B be such a linear map, and let

Since βA is injective on R n×d it follows X = Ŷ . Thus βA,B is injective. On the other hand, for each γ = (P 1 , . . . ,

n , the restriction of B to the linear space Ran(L γ ) is injective, and thus bounded below as a linear map: there is a γ > 0 so that for every

bi-Lipschitz. By Theorem 3.10, the map βA is bi-Lipschitz. Therefore we get βA,B is bi-Lipschitz as well.

## Proof of Corollary 1.3. (1) It is clear that any continuous f induces a continuous

Then a consequence of Tietze extension theorem (see problem 8 in §12.1 of [33]) implies that ϕ admits a continuous extension g : R m → R. Thus g(β(X)) = f (X) for all X ∈ R n×d . The converse is trivial.

(2) As at part (1), the Lipschitz continuous function f induces a Lipschitz continuous function ϕ : F → R. Since F ⊂ R m is a subset of a Hilbert space, by Kirszbraun extension theorem (see [38]), ϕ admits a Lipschitz continuous extension (even with the same Lipschitz constant!) g : R m → R so that g(β(X)) = f (X) for every X ∈ R n×d . The converse is trivial.

# Applications to Graph Deep Learning

In this section we take an empirical look at the permutation invariant mappings presented in this paper. We focus on the problems of graph classification, for which we employ the PROTEINS FULL dataset [12], and graph regression, for which we employ the quantum chemistry QM9 dataset [32]. In both problems we want to estimate a function F : (A, Z) → p, where (A, Z) characterizes a graph where A ∈ R n×n is an adjacency matrix and Z ∈ R n×r is an associated feature matrix where the i th row encodes an array of r features associated with the i th node. p is a scalar output where we have p ∈ {0, 1} for binary classification and p ∈ R + for regression.

We estimate F using a deep network that is trained in a supervised manor. The network is comprised of three successive components applied in series: Γ, φ, and ζ. Γ represents a graph deep network [23], which produces a set of embeddings X ∈ R N ×d across the nodes in the graph. Here N ≥ n is chosen to accommodate the graph with the largest number of nodes. In this case, the last N -n rows of Y are filled with 0's. φ : R N ×d → R m represents a permutation invariant mapping such as those proposed in this paper. ζ : R m → R is a fully connected neural network. The entire end-to-end network is shown in Figure 1.

In this paper, we model Γ using a Graph Convolutional Network (GCN) outlined in [23]. Let D ∈ R n×n be the associated degree matrix for our graph G. Also let Ã be the associated adjacency matrix of G with added self connection: Ã = I + A, where I is the n × n identity matrix, and D = D+I. Finally, we define the modified adjacency matrix Â = D-1/2 Ã D-1/2 . A GCN layer is defined as H (l+1) = σ( ÂH (l-1) W (l) ). Here H (l-1) represents the GCN state coming into the l th layer, σ represents a chosen nonlinear element-by-element operation such as ReLU, and W (l) represents a matrix of trainable weights assigned to the l th layer whose number of rows match the number of columns in H l and number of columns is set to the size of the embeddings at the (l+1)'th layer. The initial state H (0) of the network is set to the feature set of the nodes of the graph H (0) = Z.

For φ we employ seven ( 7) different methods that are described next.

(1) ordering: For the ordering method, we set D = d+1, φ ordering (X) = β A (X) =↓ (XA) with A = [I 1] the identity matrix followed by a column of ones. The ordering and identity-based mappings have the notable disadvantage of not producing the same output embedding size for different sized graphs. To accommodate this and have consistently sized inputs for η, we choose to zero-pad φ(X) for these methods to produce a vector in R m , where m = N D = N (d + 1) and N is the size of the largest graph in the dataset. (2) kernels: For the kernels method, (φ kernel (X)

, where kernel vectors a 1 , . . . , a m ∈ R d are generated randomly, each element of each vector is drawn from a standard normal distribution. Each resultant vector is then normalized to produce a kernel vector of magnitude one.

When inputting the embedding X to the kernels mapping, we first normalized the embedding for each respective node. (3) identity: In this case φ id (X) = X, which is obviously not a permutation invariant map. (4) data augmentation: In this case φ data augment (X) = X but data augmentation is used. Our data augmentation scheme works as follows. We take the training set and create multiple permutations of the adjacency and associated feature matrix for each graph in the training set. We add each permuted graph to the training set to be included with the original graphs. In our experiments we use four added permutations for each graph when employing data augmentation. (5) sum pooling: The sum pooling method sums the feature values across the set of nodes: φ sum pooling (X) = 1 T n×1 X. (6) sort pooling: The sort pooling method flips entire rows of X so that the last column is ordered descendingly, φ sort pool (X) = ΠX where Π ∈ S n so that Π X(:, d) =↓ (X(: , d)). (7) set-2-set: This method employs a recurrent neural network that achieves permutation invariance through attention-based weighted summations. It has been introduced in [36].

For our deep neural network η we use a simple multilayer perceptron of size described below.

where B 0 = B t=1 1 pt=0 and B 1 = B t=1 1 pt=1 = B -B 0 . These four statistics predict Precision P (τ ), Recall R(τ ) (also known as sensitivity or true positive rate), and Specificity S(τ ) (also known as true negative rate) (4.5) P (τ ) = T P (τ ) T P (τ ) + F P (τ )

, R(τ ) = T P (τ ) T P (τ ) + F N (τ )

, S(τ ) = T N (τ ) T N (τ ) + F P (τ ) Accuracy (ACC) is defined as the fraction of correct classification for default threshold τ = 1  2 over the set of batch samples:

Area under the receiver operating characteristic curve (AUC) is computed from prediction scores as the area under true positive rate (TPR) vs. false positive rate (FPR) curve, i.e. the recall vs. 1-specificity curve

where K is the number of thresholds. Average precision (AP) summarizes a precision-recall curve as the weighted mean of precision achieved at each threshold, with the increase in recall from the previous thresholds used as the weight:

We track the binary cross entropy (BCE) through training and we compute it on the holdout set and a random node permutation of the holdout set (see Figures 2 and3). The lower the value the better.

We look at the three performance metrics on the training set, the holdout set, and a random node permutation of the holdout set: see Figures 4, and5 for accuracy (ACC); see Figures 6, and7 for area under the receiver operating characteristic curve (AUC); and see Figures 8, and9 for average precision (AP). For all these performance metrics, the higher the score the better.  The authors of [22] utilized a Support Vector Machine (1-layer perceptron) for classification and obtained an accuracy (ACC) of 77% on the entire data set using 52 features, and an accuracy of 80% on a smaller set of 36 features. By comparison, our data augmentation method for d = 100 achieved an accuracy of 97.5% on training data set, but dropped dramatically to 73% on holdout data, and 72% on holdout data set with randomly permuted nodes. On the other hand, both the kernels method and the sum-pooling method with d = 50 achieved an accuracy of around 79% on training data set, while dropping accuracy performance by only 2% to around 77% on holdout data (as well as holdout data with nodes permuted).

For d = 1, data augmentation performed the best on the training set with an area under the receiver operating characteristic (AUC) of 0.896, followed closely by the identity method with an AUC of 0.886. On the permuted holdout set however, sort-pooling performed the best with an AUC of 0.803. For d = 10, sum-pooling, ordering, and kernels performed well on the permuted holdout set with AUC's of 0.821, 0.820, and 0.818 respectively. The high performance of the identity method, data augmentation, and sort-pooling on the training set did not translate to the permuted holdout set at d = 10. By d = 100, sum-pooling still performed the best on the permuted holdout set with an AUC of 0.817. This was followed by the kernels method which achieved an AUC of 0.801 on the permuted holdout set.

For experiments where d > 1, the identity method and data augmentation show a notable drop in performance from the training set to the holdout set. This trend is also, to a lesser extent, visible in the sort pooling and ordering methods. In the holdout permuted set we see significant oscillations in the performance of both the identity and data augmentation methods.

## Graph Regression.

4.2.1. Methodology. For our experiments in graph regression we consider the qm9 dataset [32]. This dataset consists of 134 thousand molecules represented as graphs, where the nodes represent atoms and edges represent the bonds between them.

Each graph has between 3 and 29 nodes, 3 ≤ n ≤ 29. Each node has 11 features, r = 11. We hold out 20 thousand of these molecules for evaluation purposes. The dataset includes 19 quantitative features for each molecule.

For the purposes of our study, we focus on electron energy gap (units eV ), which is ∆ε in [14] whose chemical accuracy is 0.043eV and whose prediction performance of any machine learning technique is worse than any other feature. The best existing estimator for this feature is enn-s2s-ens5 from [17] and has a mean absolute error (MAE) of 0.0529eV which is 1.23 larger than the chemical accuracy. We run the end to end model with three GCN layers in Γ, each with 50 hidden units. η consists of three multi-layer perceptron layers, each with 150 hidden units. We use rectified linear units as our nonlinear activation function. Finally, we vary d, the size of the node embeddings that are outputted by Γ. We set d equal to 1, 10, 50 and 100.

For each method and embedding size we train for 300 epochs. Note though that the data augmentation method will have experienced five times as many training steps due to the increased size of its training set. We use a batch size of 128 graphs. The loss function minimized during training is the mean square error (MSE) between the ground truth and the network output (see Figures 10,11)

where B = 128 is the batch size of 128 graphs and ∆ε t is the electron energy gap of the t th graph (molecule). The performance metric is Mean Absolute Error (MAE)

We track the mean absolute error through the course of training. We look at this performance metric on the training set, the holdout set, and a random node permutation of the holdout set (see Figures 12,and 13).

4.2.2. Discussion. Numerical results at the end of training (after 300 epochs) are included in Tables 13, 14, 15 and 16. From the results we see that the ordering method performed best for d = 100 followed closely by the data augmentation method, while both the ordering method and the kernels method performed well for d = 10, though both fell slightly short of data augmentation which performed marginally better on both the training data and the holdout data, though with significantly more training iterations. For d = 1, the kernels method failed to train adequately. The identity mapping performed relatively well on training data (for d = 100 it achieved the smallest MAE among all methods and all parameters) and even the holdout data, however it lost its performance on the permuted holdout data. The identity mapping's failure to generalize across permutations of the holdout set is likely exacerbated by the fact that the QM9 data as presented to the network comes ordered in its node positions from heaviest atom to lightest. Data augmentation notably kept its performance despite this due to training on many permutations of the data. For d = 100, our ordering method achieved a MAE of 0.155eV on training data set and 0.187eV on holdout data set, which are 3.6 and 4.35 times larger than the chemical accuracy (0.043eV ), respectively. This is worse than the enn-s2s-ens5 method in [17] (current best method) that achieved a MAE 0.0529 (eV), 1.23 larger than the chemical accuracy, but better than the Coulomb Matrix (CM) representation in [34] 

