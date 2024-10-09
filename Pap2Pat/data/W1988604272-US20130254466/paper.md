# I. INTRODUCTION

The application of the rank-modulation scheme for flash memories was proposed by Jiang et al. in [10]. The main idea of this modulation scheme is to represent the information by the relative levels of the flash memory cells, rather than by their absolute levels. Given a set of flash cells with distinct levels, the levels induce a permutation, which represents the stored data. The motivation for the scheme comes from the physical and architectural properties of flash memories. While injecting charge into a flash cell is a simple operation, removing it can by done only by the removal of the entire charge from a large block of cells, a process called block erasure. In conventional Multi-Level Cell (MLC) flash systems, the information is represented by the quantization of the cells' levels. Since the charge injection operation is a noisy process, it is often done iteratively, in order to avoid undesired block erasures in case of overshoots. It was suggested in [10] that the rank-modulation scheme speeds up data writing by eliminating the over-shooting problem in flash memories. In addition, it also increases the data retention by mitigating the effect of charge leakage. A hardware implementation of the scheme was recently designed to demonstrate those properties [12].

The work on rank modulation coding for flash memories paved the way for additional results in this area. First, errorcorrecting codes in the rank modulation setup attracted a lot of attention; see e.g. [2], [7], [11], [16]. In addition, other variations of rank modulation were proposed and studied, such as [6], [17].

In this work we focus on the notion of rewriting codes, that were proposed for the rank-modulation scheme in [10], in order to reuse the memory between block erasures. Since block erasures are slow, power consuming and are reducing the device reliability, it is desirable to minimize their usage. This is especially important in applications that require a large number of writes, such as enterprise storage systems. In order to minimize block erasures, the proposed approach is to rewrite the memory without erasing it, by injecting charge to the cells such that they induce a desired new permutation, and thus represent a new user message. After a number of rewriting cycles, the cells reach their maximal level, and block erasure is unavoidable. The aim of rewriting codes is to maximize the number of writes between block erasures.

In rank-modulation, each cell has a certain rank, according to its relative level in the permutation. Depending on the resolution of charge detection and the noise magnitude, a certain gap is needed between cells of adjacent rank, to avoid errors. Therefore, it was proposed in [4] to use a discrete model for the design and analysis of rewriting codes, despite the fact that the information is only based on the relative analog levels of the cells. The approach taken in [4] is to focus, in every rewrite, on the difference between the levels of the top cell in the permutation, before and after the rewrite. This difference is defined as the cost of rewrite. The reason for this focus is that writing with high cost gets the memory closer to the point where block erasure is required. Under this model, the goal of this work is to design codes that guarantee that, in every rewrite, the cost is at most 1. That way, the code supports a large number of writes before block erasure. It was shown in [4] that codes with worst-case cost of 1 allows the writing of at most 1 bit per cell in each writing cycle.

A further generalization of the model was proposed in [5]. In this model, the cells need to induce a permutation of a given multiset. That is, each rank is occupied by a pre-determined number of cells, according to a specific multiset. For that model, it was shown in [5] that code with cost 1 can store up to 2 bits per cell in each cycle. Notice that this generalization doubles the amount of information storage for codes with cost 1. In addition, the generalization allows the rate to approach that of the non-binary write-once-memory model [8], when the number of writes and cell levels is high. In this work, we design rewriting codes with cost 1, that allow the writing of nearly 2 bits per cell in each cycle, and thus approach the limit of the model. Our construction takes advantage of the recently discovered polar codes, which were recently used in the construction of write-once-memory codes in [3].

The rest of the paper is organized as follows. In section II, we formally present the problem we study in this paper. In section III we give a background on polar WOM codes that serve in our construction. Section IV describes our construction of rank modulation codes. Finally, in section V, we give some concluding remarks.

## II. NOTATIONS AND MODEL

Consider a set of N cells, each taking one of q levels. Denote c = (c 1 , c 2 , . . . , c N ), where c i ∈ {0, 1, . . . , q -1}, to be the cell-state vector. Denote a permutation of a multiset as a multipermutation, where the multiset is defined as following. Let m be the number of ranks, and let the number of cells in the i-th rank, 1 i m, be denoted by z i . z i is also called the multiplicity of that rank. In the case that all multiplicities are equal, denote this number by z. Note that N = ∑ m i=1 z i . Now let P m be the set of all N-cells multipermutations σ = (σ(1), σ(2), . . . , σ(N)) with m ranks. That is, for 1 j N, σ(j) ∈ {1, . . . , m}, and for 1 i m, σ -1 (i) is the set of all cells with rank i, i.e., σ -1 (i) = {j | σ(j) = i}. We call the vector z = {z 1 , z 2 , . . . , z m } a multiplicity vector. The set of all multipermutations of m ranks with multiplicity vector z is denoted by P m,z . Hence, σ = (σ(1), σ(2), . . . , σ(N)) ∈ P m,z if and only if for 1 i m, |σ -1 (i)| = z i . In case that z = z i for all 1 i m, we denote the set P m,z simply by P m,z , and we follow the same analogy in the other definitions in the paper which include the multiplicity vector z.

Given a cell-state vector c = (c 1 , c 2 , . . . , c N ) and a multiplicity vector z = {z 1 , z 2 , . . . , z m }, the multipermutation σ c,z = (σ(1), σ(2), . . . , σ(N)) is derived as follows. First, let i 1 , . . . , i N be an order of the cells such that c i 1

Then, the cells i 1 , . . . , i z 1 get the rank 1, the cells i z 1 +1 , . . . , i z 1 +z 2 get the rank 2 and so on. More rigorously, for 1 i m, the cells i m i , i m i + 1, . . . , i M i get the rank i, where

Note that a given cellstate vector can generate different multipermutations in case that there is equality between the levels of cells in adjacent ranks. In this case, we will define the multipermutation to be illegal and denote σ c,z = F. Given a multiplicity vector z = {z 1 , z 2 , . . . , z m }, we let Q z be the set of all cell-state vectors which result with a valid multipermutation, that is,

After a rewriting operation, the cell state is denoted as

The cost of the rewriting operation is defined as max i {c ′ i }max i {c i }, and the goal is to design a code that allows the writing of any information message with a rewrite cost of at most 1. We consider only the case where the encoder knows and the decoder does not know the previous state of the memory. The encoder and decoder use the same code for every cycle, and there are no decoding errors (zero-error case). For the cell states c and c ′ , we denote c c ′ if and only if

We are now ready to define the rewriting codes we study in this paper. Definition 1. An (N, q, r, D, z = (z 1 , z 2 , . . . , z m )) rankmodulation rewriting code is a coding scheme C( f , g) consisting of N q-level cells and a pair of encoding function f and decoding functions g. Let I = {1, • • • , D} be the set of input information symbols. The encoding function f :

and the decoding function g : Q z → I satisfy the following constraints:

1) For any

It was shown in [5] that the maximal rate in this model is 2 bits/cell. In this work, we propose codes that approach this rate, with low complexity of encoding and decoding. In the next section we bring a short background on polar write once memory codes, that form an important ingredient in our code construction.

# III. POLAR WOM CODES

The method of channel polarization was first proposed by Arikan in his seminal paper [1], in the context of channel coding. We describe it here briefly by its application for coding on a write-once-memory, as proposed by Burshtein and Strugatski [3]. This application is based on the use of polar coding for lossy source coding, that was proposed by Korada and Urbanke [15].

) , G ⊗n 2 be its n-th Kronecker product, and N = 2 n . Consider a memoryless channel with a binary-input and transition probability W(y|x). Define a vector u ∈ {0, 1} N , and let x = uG ⊗n 2 , where the matrix multiplication is over GF (2). The vector x is the input to the channel, and y is the output word. The main idea of polar coding is to define N sub-channels

where u j i , for 1 i < j N, denotes the subvector (u i , . . . , u j ). For large N, each sub-channel is either very reliable or very noisy, and therefore it is said that the channel is polarized. A useful measure for the reliability of a sub-channel

N is its Bhattacharyya parameter, defined by

Consider now a memory consists of N binary valued cells, such that a cell of state "0" can be changed into state "1", but a cell of state "1" cannot be changed. This model is called Write Once Memory (WOM), since each cell can only be written once. The traditional WOM problem is how to write multiple times on the memory, and achieve high sum-rate. Nonetheless, we only present here the case of a single write to the memory, where the initial state already has cells with values of '1'. Assume that a user wishes to store information in the memory, where the encoder knowns the initial state of the memory, while the decoder doesn't. We further assume that there is no noise in the model. Let s ∈ {0, 1} N be the initial cell-state, and let p be the fraction of 1's in s. That is, p = w(s)/N, where w(s) is the number of 1's in s. In addition, assume that a user wishes to store the message a ∈ {0, 1} k . Note that in the case that the decoder knows the initial state s, the communication rate of the memory is R = k/n = p. Therefore, when the decoder doesn't know s, the rate cannot exceed p. The following scheme allows a rate arbitrarily close to p for N sufficiently large.

Consider a binary erasure channel with erasure probability p. This channel is served as a test channel, in a compression scheme. Let X be a binary input to the channel, and (S, G) be the output, where S and G are binary variables as well.

In the case of a successful use of the channel, S = 1, and G = X. In the case of erasure, S = 0, and G is uniformly distributed. The probability transition function of the channel can be written as

The channel is polarized by the sub-channels

N , and a frozen set F is designed by

where δ N = 2 -N β /(2N), for any 0 < β < 1/2. It was shown in [15] that |F| = N(p -δ), where δ is arbitrarily small for N sufficiently large. Let ŝ = f WOM (s, a) be the WOM encoder. The encoder uses a common randomness source, also called dither, denoted by g, sampled from an N dimensional uniformly distributed random binary vector, and known both to the encoder and to the decoder. Let y j = (s j , g j ) and y = (y 1 , y 2 , . . . , y N ). The encoder creates a vector û ∈ {0, 1} N in the following way. First, it sets u F = a, where u F is the vector of the elements of the vector u in the set F. Then, it compresses the vector y by the following successive cancellation scheme.

, where

.

Finally, the encoder decompresses the resulting vector û into x = ûG ⊗n 2 , and sets ŝ = x + g to be the new cell-state vector. The decoder, a = g WOM (ŝ), calculates x = ŝ + g, and then recovers a = ( x(G ⊗n 2 ) -1 ) F , where, again, (b) F denotes the elements of the vector b in the set F. Both the encoding and the decoding complexities are O(N log N). In [3], a few slight modifications for this scheme are described, for the sake of the proof. Note that the encoder is using a randomized algorithm and it might fail with a small probability. We present the following Lemma from [3], as it will serve us in the construction of rank-modulation codes.

Lemma 1.

[3] Consider the scheme described above. Then for any ϵ > 0, 0 < β < 1/2 and N sufficiently large, the following holds w.p. 1 -2 -N β , 1) |{k : s k = 0 and ŝk = 1}| < (p/2 + ϵ)N, 2) {k : s k = 1 and ŝk = 0} = ∅.

## IV. CODE CONSTRUCTION

For the simplicity of the presentation, assume that the cells are placed in consecutive levels, starting from ℓ min . That is, for each rank 1 i m and cell j ∈ σ -1 (i), c j = ℓ min -1 + i. In addition, assume that for each rank i, z i = z.

An important property of the construction is the fact the cost of most rewrites is 1. That is achieved by the following encoding function. First, increase the levels of the cells in rank 1 by 1. Notice that now 2z cell are in level ℓ min + 1. Among these cells, choose z cells, according to some function of the input data, and increase their levels by 1. Now note that 2z cells are in level ℓ min + 2. Again, choose z cells among them, and increase their levels by 1. Continue this way, until z cell are chosen out of the 2z cells in level ℓ min + m -1, and their levels are increased to ℓ min + m, to finish the rewrite process. Notice that the level of the highest cells is now ℓ min + m, while before the rewrite it was ℓ min + m -1, meaning that the cost of rewrite is 1. This is the framework of the encoding function. Notice that there are m -1 selections, each time z cells are selected out of 2z candidate cells, according to some function of the input data. Our approach is to use a different part of the input data for each selection.

According to this framework, the value of d,c) is encoded by a sequence of functions, each making a subset choice according to a different part of the input data d. Assume the input data d is partitioned into m -1 parts and let (d 1 , d 2 . . . , d m-1 ) be the data parts associated with each rank, where rank m doesn't represent any information. The first function determines the cells from σ -1 c,z (1) ∪ σ -1 c,z (2) which are assigned to be the set σ -1 c ′ ,z (1) as a function of the input data

), for some function f 1 . Similarly, for i = 2, 3, . . . , m -1, there exists a function f i such that

). The decoder will operate in a similar way which will be explained in the sequel as part of the construction details.

For each i = 1, . . . , m -1

Hence, in the encoding function f i , if we consider the cells in the set {∪ i+1 j=1 σ -1 c,z (j)} \ {∪ i-1 j=1 σ -1 c ′ ,z (j)} as binary cells of value zero and all other cells of value one, then we can only program the zero cells to be one. Therefore, the key point in designing these encoding functions is to observe the similarity to the WOM problem that was described in section III. However, there is an important difference between the WOM problem and our problem of encoding a single rank. While in a WOM code there is no significance to the number of cells that are written, in our codes we seek to write such that exactly z i of the cells will remain in level zero. Our approach to tackle that difference is to add extra redundancy cells in order to make the number of written cells exactly z i w.h.p.. The number of redundancy cells is kept small, such that the rate can still be arbitrarily close to the capacity of the memory. While the number of redundancy cells can be made small, we still keep them as part of the cells in the multipermutation. That is, we still want to have a predefined number of cells in each rank. We do this in the following manner. In rank i, for each index of a flipped cell we want to store, we assign n ′ redundancy cells, where half of them are in rank i, and the other half in rank i + 1.

Our construction uses an extension of Lemma 1. Note that according to Lemma 1, w(s ′ ) < (1p + ϵ)N, where w(s ′ ) is the weight of s ′ . It is possible to show, by the same proof used in this Lemma, that w(s ′ ) > (1p -ϵ)N also holds. Let us now describe the construction formally. To simplify the notation and representation of the construction we dropped all floors and ceilings, so some of the values are not necessarily integers as required. This may encounter a small lost in the rate of the code, but it will be minor and thus can be neglected. Construction 1. Let m, z, N be positive integers such that N = mz. Let p = 2/m and 0 < ϵ < p/2. Let N ′ = N + mϵNn ′ (the value of n ′ will be explained later). The first N cells are called the information cells and are denoted by c = (c 1 , . . . , c N ). The last r = mϵNn ′ cells are called the redundancy cells and are partitioned into mϵN vectors p k,j for 1 k m, 1 j ϵN, each of n ′ cells. We assume that there is a function h : {1, 2, . . . , N} → {0, 1} n ′ which receives an integer between 1 and N, and returns a balanced vector of length n ′ . h can be implemented, for example, by [14, pp. 5-6] or [13], where in both cases log N < n ′ < 2 log N. We also assume that this function has an inverse function h -1 : Im(h) → {1, 2, . . . , N}.

An (N ′ , q, 1, D, Z) rank-modulation rewriting code C is defined according to the following encoding function f RM and decoding function g RM . The number of messages on each write is D = 2 (2z-δN)(m-1) and each message will be given as m -1 binary vectors, each of length 2z -δN bits. The cost of each rewrite is 1, and Z = N ′ /m = z + ϵNn ′ .

On the encoding and decoding functions, on each write we have the following assumptions:

1) The information cells vector c and the redundancy cells vector r are multipermutations with m consecutive levels such that the number of cells in each level is the same. We let ℓ min be the minimum cell level and ℓ max be the maximum level (note that ℓ max -ℓ min = m -1).

2) We let σ c,z be the multipermutation derived from the information cells vector. For

3) There are ϵN(m -1) auxiliary variables, called index variables and are denoted by I k,j for 1 k m -1, 1 j ϵN. These index variables will be stored in the redundancy cells and they will indicate the information cells that their levels was intentionally changed during the encoding process. Encoding Function f RM (c, p, d) = (c ′ , p ′ ):

Let c be the current information cells vector, p = (p 1,1 , . . . , p m,ϵN ) be the current redundancy cells vector, and d = (d 1 , . . . , d m-1 ) be the information vector, where each d i is a vector of (p -δ)N = 2z -δN bits. The new updated information cells vector c ′ = (c ′ 1 , . . . , c ′ N ) is determined as follows. Let S ′ 1 be the set S ′ 1 = S 1 . Encoding of the k-th rank, 1 k m -1:

1) Let v k = (v k,1 , . . . , v k,N ) ∈ {0, 1} N be the vector defined as follows:

## The new redundancy cells vector p

) is determined as follows to store the (m -1)ϵn indices. For

Finally, for 1 j ϵn, p ′ m,j = p m,j + 1. Decoding Function g RM (c, p) = d ′ : Let c = (c 1 , . . . , c N ) be the information cells vector and p = (p 1,1 , . . . , p m,ϵN ) be the redundancy cells vectors. The information vector

) is decoded as follows. First the indices I k,j for 1 k m -1, 1 j ϵN, are decoded to be

Decoding of the k-th rank, 1 k m -1:

1) Let û′ k = (u k,1 , . . . , u k,N ) ∈ {0, 1} N be the vector defined to be û′ k,i = 0 if and only if i ∈ S k .

2) The vector ûk is defined as follows. For all 1 j ϵN, if

and for all other indices i, ûk,i = û′ k,i .

3) d ′ k = g WOM ( ûk ). By the construction, we get that r/N = ϵmn ′ . To make this ratio arbitrarily small, we must let ϵ be a function of N. However, it is assumed in Lemma 1 that ϵ is constant. For that reason, we extend the Lemma for the case of non-constant ϵ. Lemma 2. When ϵ(N) is a function of N, the results of Lemma 1 hold for any

The proof of Lemma 2 follows the same lines of the proof of Lemma 1, and is omitted for space limitations. This result allows us to prove the desired properties of Construction 1.

Theorem 1. For any 0 < β < 1/2 and m and z sufficiently large, the rank modulation rewriting code in Construction 1 can be used to write an arbitrary message of rate R < 2 with cost 1, w.p. at least 1 -2 -N β . The encoding and decoding complexities are O(mN log N).

### Proof:

By the construction, the cost of each rewrite is 1. We can express the rate in the following way:

Setting ϵ = 1/N 1/4 (the smallest possible by Lemma 2) and δ = 2/m 2 , and remembering that n ′ < 2 log N, we get that

Therefore, R can take any value below 2 for large enough m and z, if z/(m 3 log 4 (zm)) is large enough as well. The probability of writing failure is achieved by the union bound. Each time f WOM is applied, the probability of encoding failure is at most 2 -N β . f WOM is applied m -1 times in each operation of the rank-modulation encoding, and therefore, for large enough N, the rank-modulation encoding is successful w.p. at least 1 -2 -N β .

Finally, we prove the encoding and decoding complexities. According to [3], the complexities of f WOM and g WOM are both O(N log N). In each rank, we also apply h or h -1 , which can be performed in logarithmic time in N (see e.g. [14, pp. 5-6] and [13]). The functions h and h -1 are applied at most ϵN times on each rank, and thus don't affect the complexity. Finally, since f WOM and g WOM are applied for each rank, the encoding and decoding complexities are O(mN log N).

### V. CONCLUSIONS

In this paper we present a rewriting coding scheme for rank modulation. The construction allows to write arbitrary message with cost 1, where the rate is asymptotically optimal. There are several open problems that can improve the understanding of the proposed scheme. First, it is of interest to determine the relation between the rate and the number of cells. In order to determine this, it is required to characterize the relation between the rate of polar codes and the number of subchannels. In addition, the design of error correcting codes for this scheme is a broad open problem. A related attempt for the WOM model is proposed in [9].

### VI. ACKNOWLEDGMENTS

This work was partially supported by the NSF grants ECCS-0801795 and CCF-1217944, NSF CAREER Award CCF-0747415, BSF grant 2010075 and a grant from Intellectual Ventures.

