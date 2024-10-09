# I. INTRODUCTION

Flash memory is an electronic non-volatile memory (NVM) that uses floating-gate cells to store information [2]. In the standard technology, every flash cell has q discrete statesstate 0, 1, • • • , q -1 -and therefore can store log 2 q bits. The flash memory changes the state of a cell by injecting or removing charge into/from the cell. To increase a cell from a lower state to a higher state, charge (e.g., electrons for nFETs) is injected into the cell and is trapped there. This operation is called cell programming. To decrease a cell's state, charge is removed from the cell, which is called cell erasing. Flash memory is widely used in mobile, embedded, and mass-storage systems because of its physical robustness, high density, and good performance [2]. To expand its storage capacity, research on multi-level cells with large values of q is actively underway.

For flash memories, writing is more time-and energyconsuming than reading [2]. The main factor is the iterative cell-programming procedure designed to avoid overprogramming [1] (raising the cell's charge level above its target level). In flash memories, cells are organized into blocks, where each block has a large number (≈ 10 5 ) of cells [2]. Cells can be programmed individually, but to decrease the state of a cell, the whole block has to be erased to the lowest state and then re-programmed. Since over-programming can only be corrected by the block erasure, in practice a conservative procedure is used for programming a cell, where charge is injected into the cell over quite a few rounds [1]. After every round, the charge level of the cell is measured and the nextround injection is configured. The charge level of the cell is made to gradually approach the target state until it achieves the desired accuracy. The iterative-programming approach is costly in time and energy.

A second challenge for flash memory is data reliability. The stored data can be lost due to charge leakage, a long-term factor that causes the data retention problem. The data can also be affected by other mechanisms, including read disturbance, write disturbance [2], etc. Many of the error mechanisms have an asymmetric property: they make the numerous cells' charge levels drift in one direction. (For example, charge leakage makes the cell levels drift down.) Such a drift of cell charge levels causes errors in aging devices.

In this paper, we propose and study a new scheme for storing data in flash memories, the rank-modulation scheme. It aims at eliminating the risk of cell over-programming, and reducing the effect of asymmetric errors. Given a set of n cells with distinct charge levels, the rank of a cell indicates the relative position of its own charge level, and the ranks of the n cells induces a permutation of {1, 2, . . . , n}. The rank modulation scheme uses this permutation to store information. To write data into the n cells, we first program the cell with the lowest rank, then the cell with the second lowest rank, and finally the cell with the highest rank. While programming the cell with rank i (1 < i n), the only requirement is to make its charge level be above that of the cell with rank i -1.

The rank-modulation scheme eliminates the need to use the absolute values of cell levels to store information. Instead, the relative ranks are used. Since there is no risk of overprogramming and the cell charge levels can take continuous values, a substantially less conservative cell programming method can be used and the writing speed can be improved. In addition, asymmetric errors become less serious, because when cell levels drift in the same direction, their ranks are not affected as much as their absolute values. This way both the writing speed and the data reliability can be improved.

In this paper, we study error-correcting codes for rank modulation. Even though asymmetric drifts of cell levels are tolerated better by rank modulation, errors can still happen because the cell levels do not necessarily drift at the same rate. A companion paper [6] studies Gray codes and encoding/decoding algorithms for the rank modulation scheme.

We explore the properties associated with error-correcting rank-modulation codes. We show that the adjacency graph of permutations for n cells, which is induced by the error model, is a subgraph of a 2 × 3 × • • • × n linear array. This observation establishes a general method for designing error-correcting rank-modulation codes using Lee-metric error-correcting codes. We present a single-error-correcting code whose size is at least half of the maximum size. We also present results on additional error-correcting codes and some related bounds.

The rest of the paper is organized as follows. In Section II some notations are defined. We continue in Section III, to investigate properties associated with permutations and error correction. In Section IV some code constructions are presented, and in Section V, more results on codes are presented. In Section VI, the paper is concluded.

# II. DEFINITIONS AND NOTATION

Let n flash memory cells be denoted by 1, 2, . . . , n. For

Here the cell a 1 has the highest rank and the cell a n has the lowest rank.

A rank-modulation scheme uses the ranks (i.e, the permutation) to store information. Let S n denote the set of n! permutations. Let Q = {1, 2, . . . , q} denote the alphabet of the symbol stored in the n cells. The rank-modulation scheme defines a decoding function, D : S n → Q which maps permutations (induced by the relative charge levels of the cells) to symbols from the user alphabet.

Given a permutation, an adjacent transposition is the local exchange of two adjacent elements in the permutation: [a 1 , . . . ,

In this model of representation, the minimal change to a permutation caused by charge-level drift is a single adjacent transposition. We measure the number of errors by the minimum number of adjacent transpositions needed to change the permutation from its original value to its erroneous value. For example, if the errors change the permutation from [2,1,3,4] to [2,3,4,1], the number of errors is two, because at least two adjacent transpositions are needed to change one into the other: [2,1,3,4] 

For two permutations A and B, define their distance, d(A, B), as the minimal number of adjacent transpositions needed to change A into B. This distance measure is called the Kendall Tau Distance in the statistics and machine-learning community [7], and it induces a metric over S n . If d(A, B) = 1, A and B are called adjacent. Any two permutations of S n are at distance at most

from each other. Two permutations of maximum distance are a reverse of each other.

# III. PROPERTIES AND BOUNDS

In this section, we study the distance between permutations and the coordinate representation of permutations. We then study the sizes of balls, and derive an upper bound on the cardinality of error-correcting rank-modulation codes.

Proof: Let T be a sequence of d(A, B) adjacent transpositions that change A into B. Divide T into two subsequences T 1 and T 2 , such that T 1 contains those adjacent transpositions that involve a n , and T 2 contains those adjacent transpositions that do not involve a n . (For instance, let us use t(a i , a j ) to denote an adjacent transposition that exchanges the two numbers a i and a j . Suppose, for example,

and the minimum number of adjacent transpositions change

It is not hard to see that T 2 can also change A into B . That is because for any a i = a n and a j = a n , an adjacent transposition in T 1 , which involves a n , does not change the relative positions of a i and a j in A (and its changed version). Meanwhile, an adjacent transposition t(a i , a j ) in T 2 changes the relative positions of a i and a j the same way for A and A (and their changed versions). Therefore, |T 2 | d(A , B ). It can also be seen that |T 1 | np, because every adjacent transposition moves a n forward in the permutation by one position, and from A to B a n has moved np positions.

and the next np of them keep moving a n forward and thus

The above theorem shows a recursive algorithm for computing the distance between two permutations. Let A = [a 1 , a 2 , . . . , a n ] and B = [b 1 , b 2 , . . . , b n ] be two permutations. For 1 i n, let A i denote [a 1 , a 2 , . . . , a i ], let B i denote the subsequence of B that contains only those numbers in A i , and let p i denote the position of a i in B i . Then, since

We now define a coordinate system for permutations. We fix 3,4). The full set of coordinates for n = 3 and n = 4 are shown in Fig. 1 (a) and (c), respectively. 2

The coordinate system is equivalent to a form of Lehmer code (or Lucas-Lehmer code, inversion table) [9]. It is easy to see that two permutations are identical if and only if they have the same coordinates, and any vector (y 1 , y 2 , . . . , y n-1 ), 0 y i i for 1 i n -1, is the coordinates of some permutation in S n . So there is a one-to-one correspondence between the coordinates and the permutations.

Let A ∈ S n be a permutation. For any 0 r n(n-1) 2

, the set B r (A) = {B ∈ S n | d(A, B) r} is a ball of radius r centered at A. A simple relabeling argument suffices to show that the size of a ball does not depend on the choice of center. We use |B r | to denote |B r (A)| for any A ∈ S. We are interested in finding the value of |B r |. The following theorem presents a way to compute the size of a ball using polynomial multiplication.

Theorem 3. For 0 r n(n-1) 2

, let e r denote the coefficient of x r in the polynomial ∏ n-1 i=1

x i+1 -1

be a generic permutation. Let X B = (y 1 , y 2 , . . . , y n-1 ) be the coordinates of B. By the definition of coordinates, we get d(A, B) = ∑ n-1 i=1 y i . The number of permutations at distance r from A equals the number of integer solutions to ∑ n-1 i=1 y i = r such that 0 y i i. That is equal to the coefficient of x r in the polynomial

x-1 . Thus, there are exactly e r permutations at distance r from A, and |B r | = ∑ r i=0 e i . Polynomial multiplication is a well-studied area, and efficient algorithms exist. Theorem 3 induces an upper bound for the sizes of error-correcting rank-modulation codes. By the sphere-packing principle, for such a code that can correct r errors, its size cannot exceed n!/ |B r |.

# IV. ERROR-CORRECTING RANK-MODULATION CODES

In this section, we first study the topology of permutations, and use the result to derive a general construction for errorcorrecting rank-modulation codes based on Lee-metric codes. Next, we present a family of one-error-correcting codes whose size is at least half of the optimal size.

## A. Embedding of Permutation Adjacency Graph

Define the adjacency graph of permutations, G = (V, E), as follows. The graph G has |V| = n! vertices, which represent the n! permutations. Two vertices u, v ∈ V are adjacent if and only if d(u, v) = 1. G is a regular undirected graph with degree n -1 and diameter n(n-1) 2 . To study the topology of G, we begin with the follow theorem. 

### . , y n-1 ). A and B are adjacent if and only if they satisfy the following two conditions:

• Condition 1:

• Condition 2: There do not exist i, j ∈ {1, 2, . . . , n}, where i < j -1, such that (1) a i = b j , a j = b i ; (2) for any k where k = i and k = j, a k = b k ; (3) for any k where i < k < j, a k > b i and a k > b j .

Proof: The proof is by induction. When n = 2, the theorem is easily true. That serves as the base case. Now assume that the theorem is true for n = 2, 3, . . . , N -1. We will prove that it is also true when n = N. First, we will show that if the two permutations are adjacent, then

Suppose A and B are adjacent. Consider the two integers z 1 , z 2 such that the z 1 -th element in A and the z 2 -th element in B are both N. There are two cases. Case 1: z 1 = z 2 . In this case, x N-1 = y N-1 by definition. Since the two permutations are adjacent, which means that we can change one into the other by switching two numbers in adjacent positions, those two positions cannot include z 1 = z 2 . So if we remove the number N from the two permutations A, B, the two shorter permutations are also adjacent. The coordinates of those shorter permutations are (x 1 , x 2 , . . . , x N-2 ) and (y 1 , y 2 , . . . , y N-2 ). By induction, ∑ N-2 i=1 |x i -

In this case, since A, B are adjacent, A can be changed into B by switching the z 1 -th number and the z 2 -th number. Then |z 1z 2 | = 1, and therefore, |x N-1y N-1 | = 1, and for any z = z 1 , z 2 , we have

Thus, if the two permutations A and B are adjacent, Condition 1 is true.

If A and B are adjacent, then Condition 2 is also true, for the following simple reason: if the two integers i, j described in Condition 2 exist, then there would be no way to switch a i and a j with only one adjacent transposition in order to change A into B. That would be a contradiction. Now we prove the other direction: if the two conditions are true, then A and B are adjacent. Assume that the two conditions are true. Then, since ∑ N-1 i=1 |x iy i | = 1, there are two cases. Case 1: |x N-1y N-1 | = 1 and for any z < N -1, x z = y z . In this case, by switching the number N and a number beside it in the permutation A, we can get the permutation B. Hence, the two permutations are adjacent. Case 2: |x N-1y N-1 | = 0 and ∑ N-2 i=1 |x iy i | = 1. In this case, if we take away the number N from A and B, we get two shorter permutations satisfying the two conditions, so by induction, the two shorter permutations are adjacent. Assume that we can switch the k-th number and the (k + 1)th number in the first short permutation to get the second short permutation. For both A and B, since Condition 2 is true, the number N cannot be between those switched numbers. So we can still switch those two numbers as an adjacent transposition to change A into B. Thus A, B are adjacent, and the other direction of the conclusion is also true.

Let

Each vertex is assigned integer coordinates (x 1 , x 2 , . . . , x n-1 ), where 0 x i i for 1 i n -1. The distance between vertices of L n is the L 1 distance, and two vertices are adjacent (i.e., have an edge between them) if and only if their distance is one.

We now build a bijective map P : V → V L . Here V is the vertex set of the adjacency graph of permutations G = (V, E). For any u ∈ V and v ∈ V L , P(u) = v if and only if u, v have the same coordinates. By Theorem 4, if two permutations are adjacent, their coordinates are adjacent in L n , and we get: We show some examples of the embedding in Fig. 1. It can be seen that while each permutation has n -1 adjacent permutations, a vertex in the array can have a varied degree from n -1 to 2n -3. Some edges of the array do not exist in the adjacency graph of permutations because they violate condition 2 in Theorem 4.

#### Proposition 6

If two vertices are adjacent in the array L n , their distance in the adjacency graph of permutations, G, is at most 2n -3, and this bound is tight.

Proof: Let A and B be two permutations such that X A and X B are adjacent in L n . If they are not adjacent permutations, then they must violate condition 2 in Theorem 4. Without loss of generality, assume

Clearly, a minimum of ( ji) + ( ji -1) = 2 j -2i -1 adjacency transpositions are needed to switch a i and a j in order to change

The observation that the permutations' adjacency graph is a subgraph of a linear array shows an approach to design errorcorrecting rank-modulation codes based on Lee-metric codes. We skip its proof due to its simplicity.

## Theorem 7.

Let C be a Lee-metric error-correcting code of length n -1, alphabet size no less than n, and minimum distance d. Let C be the subset of codewords of C that are contained in the array L n . Then C is an error-correcting rankmodulation code with minimum distance at least d.

### B. Single-error-correcting Rank-Modulation Code

We now present a family of rank-modulation codes that can correct one error. The code is based on the perfect sphere packing in the Lee-metric space [4]. The code construction is as follows.

## Construction 8. (Single-error-correcting rank-modulation code)

Let C 1 , C 2 denote two rank-modulation codes constructed as follows. Let A be a general permutation whose coordinates are (x 1 , x 2 , . . . , x n-1 ). Then A is a codeword in C 1 if and only if the following equation is satisfied:

A is a codeword in C 2 if and only if the following equation is satisfied:

Between C 1 and C 2 , choose the code with more codewords as the final output.

2

We analyze the code size of Construction 8.

Lemma 9. The rank-modulation code built in Construction 8 has a minimum cardinality of (n-1)! 2 .

Proof:

× (2n -1) linear array. Every vertex in H has integer coordinates (x 1 , x 2 , . . . , x n-1 ), where 0 x i i for 1 i n -2, and -n + 1 x n-1 n -1.

Given any choice of (x 1 , x 2 , . . . , x n-2 ) of the coordinates, we would like to see if there is a solution to x n-1 (note that -n + 1 x n-1 n -1) that satisfies the following equation:

i=1 ix i , and n -1 and 2n -1 are co-prime integers, there is exactly one solution to x n-1 that satisfies the above equation. If x n-1 0, clearly (x 1 , x 2 , . . . , x n-1 ) are the coordinates of a codeword in the code

] ≡ 0 (mod 2n -1), so (x 1 , x 2 , . . . , x n-2 , -x n-1 ) are the coordinates of a codeword in the code C 2 .

Since 0 x i i for 1 i n -2, there are (n -1)! ways to choose x 1 , x 2 , . . . , x n-2 . Each choice generates a codeword that belongs either to C 1 or C 2 . Therefore, at least one of C 1 and C 2 has cardinality no less than

Lemma 10. The rank-modulation code built in Construction 8 can correct one error.

Proof: It has been shown in [4] that for an infinite kdimensional array, vertices whose coordinates (x 1 , x 2 , . . . , x k ) satisfy the condition ∑ k i=1 ix i ≡ 0 (mod 2k + 1) have a minimum L 1 distance of 3. Let k = n -1. Note that in Construction 8, the codewords of C 1 are a subset of the above vertices, while the codewords in C 2 are a subset of the mirrored image of the above vertices, where the last coordinate x n-1 is mapped to -x n-1 . Since the permutations' adjacency graph is a subgraph of the array, the minimum distance of C 1 and C 2 is at least 3. Hence, the code built in Construction 8 can correct one error.

Theorem 11. The code built in Construction 8 is a single-errorcorrecting rank-modulation code whose cardinality is at least half of optimal.

Proof: Every permutation has n -1 adjacent permutations, so the size of a radius-1 ball, |B 1 |, is n. By the sphere packing bound, a single-error-correcting rank-modulation code can have at most n! n = (n -1)! codewords. The code in Construction 8 has at least (n -1)!/2 codewords.

(0,0,0) (0,0,1) (0,0,2) (0,0,3) 

### V. MORE CODES AND BOUNDS

It has been shown that the single-error-correcting code built by Construction 8 has a size within half of optimal. There exist code constructions that can build larger codes in many cases. We report here some error-correcting codes built using ad hoc constructions, and compare them with the sphere-packing upper bound and the half-optimal code: • When n = 5, 6, 7, an ad hoc construction generates single-error-correcting codes with 18, 90, and 526 codewords, respectively. The codes output by Construction 8 have size 14, 66, and 388, respectively. The spherepacking upper bound is 24, 120, and 720, respectively. • When n = 5, 6, 7, there exist two-error-correcting codes of size 6, 23, and 110, three-error-correcting codes of size 2, 10, 34, and four error-correcting codes of size 2, 4, and 14, respectively. All the above codes have a size that is at least one half of the optimal size.

### VI. CONCLUSION

In this paper, we propose a novel data storage scheme for flash memories, the rank-modulation scheme. It can eliminate cell over-programming and also be more robust to asymmetric errors. A rank-modulation scheme uses a new tool -the permutation of cell ranks -to represent data. Consequently, new error-correcting techniques suitable for permutations are needed. We study the properties associated with error-correcting rank-modulation codes, and show that the permutation adjacency graph, which describes the topology of permutations, is a subgraph of a multi-dimensional linear array. As a result, the error-correcting codes for rank modulation can be designed using Lee-metric codes. We present a family of one-error-correcting codes whose size is within half of the optimal size, and also show the results of some other (more ad hoc) code constructions.

It will be interesting to extend the code construction in this paper to design codes that correct two or more errors, by using new Lee-metric codes or suitable lattice interleavers. The codes can also be improved by a better utilization of the sphere packing in the permutation adjacency graph, which is sparser than the array L n . Alternative embedding of the permutations, known as permutohedron, can be explored [3], [8]. (For example, the permutation adjacency graph for four numbers can be embedded as a truncated octahedron.) In addition, it will be interesting to combine the error-correcting codes with data rewriting schemes as in [5].

