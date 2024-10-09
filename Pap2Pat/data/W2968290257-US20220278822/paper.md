# Introduction

Efficient hardware design of AES SBoxes is a well-known subject. If you want the absolute maximum clocking speed of the hardware, you'd probably use a straightforward tablelookup implementation, which naturally leads to a large area. In many practical situations the area of the cryptographic subsystem is limited, and the designer cannot afford to implement table-lookup for the 16 SBoxes involved in an AES round. For these situations, we need to study how to implement an AES SBox with logical gates only, focusing on both area and maximum clocking speed. The maximum clocking speed of a circuit is determined by the critical path or depth of the circuit; the worst case time it takes to get stable output signals from a change in input signals.

Another aspect when implementing AES is, in particular, the need for the inverse cipher. Many modes of operation for a block cipher only use the encryption functionality and hence there is no need for the inverse cipher. In case you need both the forward and inverse SBox, it is often beneficial to combine the two circuits. This is because the main operation of the AES SBox is taking the inverse of a field element, which naturally is its own inverse, and we expect that many gates of the two circuits can be shared.

From a mathematical perspective, the forward AES SBox is defined as the composition of a non-linear function I(g) and an affine function A(g), such that SBox(g) = A(I(g)).

The non-linear function I(g) = g -1 is the multiplicative inverse of an element g in the finite field GF (2 8 ) defined by the irreducible polynomial x 8 + x 4 + x 3 + x + 1. We will assume that the reader is familiar with the AES SBox, and refer to [oST01] for a more comprehensive description.

The first step towards a small area implementation was described by Rijmen [Rij00], where results from [IT88] was used. The idea is that the inverse calculation in GF (2 8 ) can be reduced to a much simpler inverse calculation in the subfield GF (2 4 ) by doing a base change to GF ((2 4 ) 2 ). In 2001, Satoh et al [SMTM01] took this idea further and reduced the inverse calculation to the subfield GF (2 2 ). In 2005, Canright [Can05] built on the work of Satoh et al and investigated the importance of the representation of the subfield, testing many different isomorphisms that led to the smallest area design. This construction is perhaps the most cited and used implementation of an area-constrained combined AES SBox.

In a series of papers, Boyar, Peralta et al presented some very interesting ideas for both the subfield inverter as well as new heuristics for minimizing the area of logical circuits [BP10a,BP10b,BP12,BFP18]. They derived an inverter over GF (2 4 ) with depth 4 and a gate count of only 17. The construction in [BP12] is the starting point for this paper.

After Boyar, several other papers followed focusing on low depth implementations [JKL10, NNT + 10, UHS + 15]. In 2018 two papers by Reyhani et al [RMTA18a,RMTA18b] presented the best known implementation (up until now) of both the forward SBox as well as the combined SBox. In [LSL + 19] the authors present a very nice way to include the depth into Boyar's SLP problem [BMP13]. But the algorithm does not work with multiplexers, and hence cannot be applied to the combined SBox.

As pointed out in [RMTA18a], there are misalignments between researchers in how to present and compare implementations of combinatorial circuits. One way is to simply count the total number of standard gates in the design and find the path through the circuit that contains the critical path to determine and compare the speed. In practice it is much more complicated than that. For this paper, we present both the simple measure using only the number of gates, as well as giving a Gate Equivalent (GE) number based on the typical area required for the gate compared to the NAND gate. So for example the 2-input NAND gate will have GE=1, while the XOR gate will have a GE=2.33. The relative numbers for the GE are dependent on the specific ASIC process technology used, as well as the drive strength needed from the gate. We have used the GE values obtained from the Samsung's STD90/MDL90 0.35µm 3.3V CMOS technology [Sam00]. A comprehensive discussion on our choices for circuits comparison can be found in Appendix A. Additionally, we propose to count technological depth of a circuit normalized in terms of the delays of a XOR gate, which makes it possible to compare depths and the speed of various academic results.

The rest of the paper is organized as follows. In Section 2 we introduce the standard hardware architecture for the AES SBox. In Section 3 we describe the fundamental problem we are addressing, together with improvements to previously known techniques for solving it. The new idea of considering "floating multiplexers" is introduced in Section 4, followed by architectural improvements to the AES SBox in Section 5. The results, both theoretical and practical synthesis results, are given in Section 6. The paper ends with some conclusions and acknowledgements in Sections 7 and 7.

# Preliminaries

We will follow the notation used in both [Can05] and [BP12] when we now construct our tower field representation. The irreducible polynomials, roots, and normal basis can be found in Table 1.

Table 1: Definition of the subfields used to construct GF (2 8 ).

Target Field Irreducible Poly. Root Coefficients in Field Normal Base GF (2 2 )

Following [Can05] and [BP12], we can now derive the expression for inverting a general element A = a 0 Y + a 1 Y 16 in GF (2 8 ) as

The element inversion in GF (2 8 ) can be done over GF (2 4 ) according to

where the result is obtained as A -1 = T 6 Y + T 7 Y 16 . In these equations we utilize several operations (addition, multiplication, scalar, and squaring) but only two of them are nonlinear over GF (2); multiplication and inversion. Furthermore, the standard multiplication operation also contains some linear operations. If we separate all the linear operations from the non-linear and combine the former with the linear equations needed to do the base change for the AES SBox input, which is represented in polynomial base using the AES SBox irreducible polynomial x 8 + x 4 + x 3 + x + 1, we will end up with an architecture of the SBox according to Figure 1, where we also indicate were the different parts of equations 1 are calculated. 

# T 3 and T 4 T 5 T 6 and T 7

Base back-conversion and the affine transformation of the AES SBox.

Figure 1: Architecture of the forward SBox according to [Can05] and [BP12].

In case we are dealing with the inverse SBox, we naturally need to apply the inverse affine transform to the top linear matrix instead of the bottom. This architecture will be our starting point, and we will now provide a set of new or enhanced algorithms for minimizing both the area and the depth of the two linear top and bottom matrices.

# Circuits for binary linear system of equations

In this section, we will recapitulate the known techniques for linear circuit minimization and propose a few improvements. We start by stating the objectives.

## Basic problem statement

Given a binary matrix M m×n and the maximum allowed depth maxD, find the circuit of depth D ≤ maxD with the minimum number of 2-input XOR gates such that it computes Y = M • X. In other words, given n bits of input X = (x 0 . . . x n-1 ), the circuit should compute m linear combinations Y = (y 0 . . . y m-1 ). Any circuit realization that implements a given system of linear expressions is called a solution.

The above problem is NP-hard [BMP08], and we have seen various heuristic approaches that help finding a sub-optimal solution in the literature. In all previous work we have studied, the assumption is that all input signals arrive in the same time, and all output signals are "ready" with delays at most maxD. In this paper we extend the original problem with AIR and AOR defined as follows.

Additional Input Requirement (AIR). The problem may be extended with an additional requirement on input signals X, such that each input bit x i arrives with its own delay d i , in terms of XOR-gates delays. The resulting depth D ≤ maxD then includes input delays. For example, if some input x i has the delay d i > maxD then no solution exists. The AIR is useful while deriving the bottom matrix as described in Section 2, since after the non-linear part, the signals entering the bottom matrix will have different delays.

Additional Output Requirement (AOR). The problem may be extended by an additional requirement on the output signals. Each output signal y i may be required to be "ready" at depth at most e i ≤ maxD. This is useful when some output signals continue to propagate in the critical path and other signals may be computed with larger delays, but still at most maxD. The AOR is used while deriving the top matrix as described in Section 2, since when we introduce multiplexers for the combined SBox, the output signals of the top matrix will be required to have different delays.

## Cancellation-free heuristics

Cancellation-free heuristics are algorithms that produce linear expressions z = a ⊕ b, where both a and b are Boolean linear expressions in the input variables, and a and b share no common terms. In other words, as we add a and b we will not cancel out any term.

Paar [Paa97] suggested a greedy approach to solving the Basic Problem in 3.1. That solution starts with the matrix M and considers all pairs of columns (i, j) in M . Then a metric is defined (on the pairs of columns) as the number of rows where M r,i = M r,j = 1, i.e. where the input variables x i and x j both occur. For the column pair with the highest metric, we form a new variable x n = x i ⊕ x j and add that to the matrix (which now is of size m × (n + 1)), and set positions M r,i = M r,j = 0, and M r,n+1 = 1.

Canright [Can05] also used this technique but instead of using the metric function, he performed an exhaustive search over all possible column pairs. This was possible due to the fact that the target matrix in his case was the base conversion matrix only of size 8 × 8. As we saw in Section 2, our bottom matrix will be considerably larger, and hence we need to take another approach. We also need to consider the AIR and the AOR.

Satisfying the AIR. When performing the above algorithm we should keep track of the depth of the newly added XOR gates. This is done by having a vector D = (d 0 . . . d n-1 ) with the current depth of all inputs and newly added signals x i . When the new signal x n = x i ⊕ x j is added, the delay of x n is trivially d n = max(d i , d j ) + 1. We then also restrict the algorithm such that if d n > maxD then we are not allowed to add x n as a new input signal. The AIR is hereby satisfied automatically.

Satisfying the AOR. Similarly, when adding a new input variable x n , we need to check if a solution is theoretically possible. An elegant solution to this is presented in Theorem 2 in [LSL + 19] where they calculate the shortest circuit given additional delay constraints.

Probabilistic heuristic approach. Since we cannot perform a full exhaustive search on the bottom matrix due to its size, we need to confine the number of pairs to keep and further evaluate. We have found that keeping the K best candidates (based on the original metric by Paar) and then randomly selecting which one to pick for the next XOR gate is a good strategy. In our simulations, this probabilistic approach gave us much smaller circuits than only considering the best metric candidates. Naturally, the execution time will be too long if we pick a too large K, and conversely picking a too small K decreases the chances of deriving a good circuit. In practice we found that K = 2, . . . , 6 is a reasonable number of candidates to keep and try.

## Cancellation-allowed heuristic

The cancellation-free approaches give sub-optimal results, as it was shown by Boyar and Peralta in [BP10a], where they also introduced a new algorithm that allows cancellations. This was later improved by Reyhani et al in [RMTA18a]. Next, we briefly describe the basic idea of that heuristic.

### Basic cancellation-allowed algorithm [BP10a]

Every row of M is an n-bit binary vector. That vector can be seen as an n-bit integer value. We define that integer value as a target point. Thus, the matrix M can be seen as the column vector of m target points. The input signals {x 0 , . . . , x n-1 } can also be represented as integer values x i = 2 i , for i = 0, . . . , n -1.

Let the base set S = {s 0 , . . . , s n-1 } = {1, 2, 4, . . . , 2 n } initially represent the input signals. The key function of the algorithm is the distance function δ i (S, y i ) that returns the smallest number of XOR gates needed to compute a target point y i from the set of known points S. The algorithm keeps a vector ∆ = [δ 0 , δ 1 , . . . , δ n-1 ] which is initially set to the Hamming weight minus one of the rows of M , which would be the number of XOR gates needed without any sharing of intermediate gates.

The algorithm then proceeds by combining two base points s i and s j in the base set S, and xor them together producing a candidate point c = s i ⊕ s j . The selection of s i and s j is performed by an exhaustive search over all distinct pairs, and then for each candidate point, the sum of the distance vector δ i , for i ∈ [0, n -1], is calculated. Note that the distance functions δ i now is computed over the set S ∪ {c}. The pair which gives the smallest distance sum is picked and S is updated S = S ∪ {c}. In case there is a tie, the algorithm picks the pair that maximizes the Euclidean norm

If there is a tie after this step too, the authors in [BP10a] investigated different strategies and concluded that all strategies tested performed similarly, and hence a simple random selection can be used. The algorithm then repeats the step of picking two new base points and calculating the distance vector sum, until the distance vector is all-zeros and the targets are all found. In the original description, there is also a notion of "preemptive" choices. A preemptive choice is a candidate point c such that it directly fulfils a target row in the matrix M . If such a candidate is found, it is immediately used as the new point and added to S.

Reyhani et al [RMTA18a] improved the original algorithm from [BP10a] by directly searching for preemptive candidates in each round and add them all to the set S before the "real" candidate is added and the distance vector recalculated. They also improved the tie resolution strategy and kept all the candidates that were equally good under the Euclidean norm and recursively tried them all, keeping the one that was best in the next round.

When the maximum depth maxD is a required constraint, the newly proposed algorithm in [LSL + 19] can be used. However, in our simulations for bottom matrices, it didn't produce better results than the cancellation-free algorithm with randomization factor.

## Exhaustive search methods

In this section we present an algorithm for an efficient exhaustive search of the minimal circuit. The overall complexity is exponential in the number of input signals, and linear in the number of output signals. From our experiments we can conclude that this exhaustive search algorithm can be readily applied to circuits of up to approximately 10 input bits.

### Notations and data representation

Using the same integer representation of the rows of M , and the input signals x i as in Section 3.3.1, we can re-phrase the basic problem statement: given the set of input points x i we want to find the sequence of XORs on those points such that we get all the m wanted target points y i , the rows of the matrix M , with the maximum delay maxD. Input and output points may have different delays d i and e i , respectively.

For data structures, we can store a set of 2 n points as either a normal set, and/or as a bit-vector. The set makes it possible to loop through the points while the bit-mask representation is efficient to test set membership.

### Basic idea

The proposed exhaustive search algorithm is a recursive algorithm, iterating over the depths, starting at depth 1 and ending at maxD. At each depth D, we try to construct new points from the previous depths, thereby constructing circuits that are of exactly depth D. When all target points are found, we check the number of required XOR gates, keeping track of the smallest solution. We will need the following sets of points: known[maxD+1] -the set of known points at certain depth D. ignored[maxD+1] -the set of points that will be ignored at depth D. targets -the set of target points. candidates -the set of candidate points that can be added to the set known at the current recursion step.

The initial set of known points is x i , for i = 0 . . . n -1, and the set of target points is y i , for i = 0 . . . m -1. AIR is met by initially placing the input point x i to the known set at depth d i . AOR is satisfied by setting the point y i with output delay e i to the ignore list on all depth levels that are larger than e i .

We will now explain the steps executed at each depth of the recursion, assuming that we currently are at depth D.

Step 1 -Preemptive points. Check the known[D] set to see if any pair can be combined (XOR:ed) to give a target point not yet found. If all targets are found, or if we have reached maxD, we return from this level of the recursion.

Step 2 -Collect candidates. Form all possible pairs of points from the known[0..D -1] sets, where at least one of the points is from known[D -1], and XOR the pair to derive a new point. If the derived point is in the set ignored[D] then we skip it, otherwise we add it to the candidate set.

Step 3 -In this step we try to add points from the candidate set to the known list, and call the algorithm recursively again. We start by trying to add 1 point and do the recursive call. If that's not solving the target points, we'll try to add 2 points, and so on until all combinations (or a maximum number of combinations) of the points in the candidate set have been tried.

### Ignored points and other optimizations

In step 2, we check the candidate set against the ignored[D] set, the set of ignored points at depth D. The ignored set is constructed from a set of rules; Intersection: A candidate point p should be ignored if for all target points w i we get (w i &p) = p. This means that the point p covers too many of the input variables, and is not covered by any of the points in the targets set; Forward Propagation: We can calculate all possible points on each level starting from the top level D = 0 with n known points and going down to D = maxD. Those points that can never appear at some level d are then included into the ignored[d] set. If some target point w has another desired maximum delay e i < maxD, then that point on the following depths should be ignored, i.e., we add w to ignored[e i + 1..maxD]; Sum of Direct Inputs: If any of the input signals x i , x j give the point p = x i ⊕ x j on level d, then all consecutive levels > d must have the point p in the ignored list; Backward Propagation: As a last check, we can go backwards level by level, starting from d = maxD and ending at level d = 1, and for each allowed (not ignored) point on the level d we check whether there is still a not-ignored pair a, b at the previous levels (one of a or b must be on the level d -1) such that it gives p = a ⊕ b. If not, then the point p should be added to the ignore[d] set; Ignore Candidates: dynamically add a point w to the ignore[d] set if w has been one of the candidates at previous levels < d.

## Remarks

Simulations show that regarding searching for the minimum solution the top matrix (with only 8 inputs) can be solved with the exhaustive cancellation-allowed search as in Section 3.4. The bottom matrix (with 18 inputs) is too large for a direct exhaustive search, and we should start with a probabilistic cancellation-free heuristic from Section 3.2, and then use a full exhaustive search for the ending part, when the Hamming weights of the remaining rows become small enough to perform the exhaustive search. This approach gave us the best result.

# System of linear circuits with multiplexers

Assume we want to find a solution for the combined AES SBox, where the top and the bottom linear matrices need to be multiplexed based on the SBox direction. This means that the circuit for the combined linear expressions is basically doubled in size, plus the set of multiplexers. In this section we will show how to deal with multiplexed systems of linear expressions. We will show that the MUX and XOR gates can be considered in a combined way in order to achieve a very compact circuit.

## Floating multiplexers

Consider that for some signal Y we have to compute two linear expressions Y F and Y I for the forward and the inverse SBoxes respectively. Then we apply a multiplexer so that only one of the signals continues as Y . Assume further that the signals Y F and Y I share some part of the expression. Then it may be better to push that shared part after the multiplexer, and the resulting solution can be simplified.

For example, let

, then normally we should spend 2 XOR gates and 1 multiplexer, so that we get Y = M U X(select, X 0 ⊕ X 1 , X 0 ⊕ X 2 ) with 3 gates. However, we can push the common part X 0 after the multiplexer as follows:

then we get a circuit with only 2 gates. In general, one can pick any linear combination ∆ on input signals and make a substitution:

where ∆ is then added to the linear matrix as an additional target signal to compute. If that substitution leads to a shorter circuit then we keep it. We should also choose such ∆ that the overall depth is not increased. Thus, various multiplexers will be "floating" over the depth of the circuit. Signals with ∆ = 0 should have their maximum depth decreased by 1.

### Metrics and linear expressions to solve

We have n input signals X 1 . . . X n and m output signals Y 1 , . . . , Y m , where each Y i is represented in its most general form as a triple (A i , B i , C i ) such that

where A i , B i , and C i are linear expressions on the input signals. We are allowed to modify the above expression as

Let ABC represents the linear matrix that describes all the rows A i , B i , and

gives the wanted linear system to realize using minimal number of gates and a given maxD.

By choosing favorable values of ∆ i , one can shrink the number of total gates, since some of the target points of ABC may become equal to each other, and hence ABC can be reduced by at least one row. Also, some of the targets may become 0 or having only one bit -i.e., they are equal to corresponding input signals. These targets are also removed from the linear system as they are trivial and cost zero gates. After the above reductions we get a system of linear expressions where all rows are distinct and have Hamming weight at least 2. As before, we interpret the rows of ABC as integers, and adding (XORing) a ∆ i to the three rows A i , B i , and C i will change those three target points, but not the resulting Y i . Metric. The search for a good combination of ∆s requires a lot of computations and it rapidly becomes infeasible to compute a minimal solution for each selection. Thus, we need to decide on a good metric that allows us to truncate the search space down to promising sets of ∆s. We propose to adopt a metric that is based on the lower bound of the number of gates of a fixed system (when ∆ values are selected), and define the metric to be the number of rows of the reduced ABC matrix, plus the minimum number of extra gates needed to complete the circuit, such as multiplexers.

In the following we present several heuristic approaches to finding a good set of ∆s while minimizing the metric.

### Iterative algorithms to find ∆s: metric→minimize

The below techniques only work for small n, but in our case they are readily applicable to the 8-input top matrix of the AES SBox.

Algorithm-A(k) -Select k triplets (A i , B i , C i ) and try to find k matching ∆ i s that minimize the metric. If some choice results in a smaller metric, we keep that choice and continue searching with the updated ABC matrix. The algorithm runs in a loop until the metric is not decreasing any more. Algorithm-A(1) is quite fast, and Algorithm-A(2) also has acceptable speed. For larger ks it becomes infeasible. Algorithm-A(k) works fine for a very quick/brief analysis of the given system but the result is quite unstable since for a random set of initial values of ∆ i s the resulting metric fluctuates heavily.

Algorithm-B -unlike Algorithm-A this algorithm is trying to construct a linear system of expressions, starting from an empty set of knowns S and then trying to add new points to S one by one, until all targets of ABC become included in the set S. While testing whether a new candidate c should be added to S we loop through all (A i , B i , C i ) and for each one try to find a ∆ i that minimizes the overall metric. This heuristic algorithm is a lot more stable and gives quite good results.

However, the smallest possible metric does not guarantee that the final solution will have the smallest number of gates, and the number of non-target intermediates needed is unclear. Thus, it would be a good idea to collect a number of promising systems whose metric is the smallest possible, then try to find the smallest solution amongst them. We will investigate this in the next section.

## New generic heuristic technique for linear systems with floating multiplexers

If we generalize the idea of floating multiplexers and let them float even higher up in the circuit, and also sharing them wider, we could achieve better results. In this section we propose a generic heuristic algorithm that finds good circuits for such systems.

### Problem statement

We are given n-bit input signal X n , binary matrices M F m×n and M I m×n , binary vectors

, and vectors of delays D X n and D Y m . We want to find a smallest and shortest solution that computes the m-bit output signal Y :

where each input signal X i has an input arrival delay D X i and each output signal Y j must have the total delay at most D Y j . A * and B * are constant masking vectors for the input and output signals respectively (NOT-gates). ZF is the mux selector, when ZF = 1 we pick the first (Y F = "forward") output otherwise the second (Y I = "inverse") output. We also assume there is a complement signal ZI = ZF ⊕ 1 that is also available as an input control signal.

### Preliminaries

Similar to our previous notation, we define a "point" to be tuple of a point value (.p) and a delay (.d):

with a total output delay point.d. I.e., F and I are linear combinations of the n-bit input X, and f and i are negate bits applied to the result in case the selector ZF is "forward" or "inverse", respectively. The n input points are then represented as:

and the target m points are:

We should also include the following 4 trivial points to the set of inputs: Given any two (ordered) points v and w there are at most 6 possible new points that can be generated based on the following gates:

where D new = max{v.d, w.d}+1. Note that the inclusion of the 4 trivial points is important, since then we can limit the number of gate types to be considered. For example, a NOTgate is then implemented as XOR(v, 1), AND gate with ZF can be implemented as MUX(v, 0), OR gate with ZI is MUX(v, 1), etc.

### The floating multiplexers algorithm

We start with the set S of input points (of size n + 4), and place all target points into the set T . At each step, we compute the set of candidate points C that is generated by applying the above 6 gates to any two points from the set S. Naturally, C should only contain unique points and exclude those already in S. We try to add one candidate point from C to S and compute the distances from S to each of the target points in T .

Thereafter we compare metrics to decide which candidate point will be included into S at this step, and start over by calculating the possible candidates. The algorithm stops when the overall distance δ-metric is 0.

The metric consists of several values. The distance δ(S, t i ) is the minimum number of basic gates (the above 6) required to get the target point t i from the points in S, such that the delay is at most D Y i . Subsection 4.2.5 discusses how to compute δ(S, t i ). The applied metrics and their order of importance are then as follows:

The metric γ is the projected number of gates in case there will be no more shared gates; that metric we should definitely minimize. In case there are several candidates that give the same value, then we look into the second metric δ. δ is the sum of distances excluding distances where only 1 gate is needed. Given the smallest γ, we must maximize δ. The larger δ the more opportunities to shrink γ. We exclude distances 1 because of the inclusion of the preemptive step that we will describe below. When we accept candidates to S one by one as described above, the metrics δ and γ are similar, but will become distinct when we, in the next subsection, introduce a search tree where the size of |S| may differ.

τ selects the candidate having the minimum depth in case the above two metrics showed the same values for two candidates. In case there are no maximum depth constraints for target points then this metric is not needed. ν is the Euclidean norm excluding the preemptive points (similar to δ). This is the last decision metric since it is not a very good predictor, a worse value may give a better result and vice versa. However, if there are two candidates with equal metrics δ, γ, and τ , then ordering of the two candidates may be done based on ν. An alternative approach in case of tie-candidates is to choose one of them randomly.

Preemptive points. If some distance δ(S, t i ) = 1 then we accept the point t i into S immediately without the search through the candidates C. The inclusion of this step in the algorithm forces us to exclude such points from the metrics δ and ν.

In [RMTA18a] preemptive points were included into the metric, but we believe it was not fully correct. E.g., when two distance vectors {1, 2, . . .} and {0, 2, . . .} have the same projected gates, then they fall into a totally equal situation in terms of possible shared gates, thus they should result in the same δ. The point with the distance 1 in the above vector will be included into the circuit immediately (preemptive point), and it does not give any advantage over the second choice where we have a point with the distance 0. Therefore, distances with the value 1 should be ignored in δ and µ, but they should be accounted in the projected gates γ, instead.

### Search tree

Additionally to the above algorithm, we propose to have a search tree where each node is a set S with metrics. Children of such a node are also nodes where S is derived from S by adding one of the candidate point S ← C. Thus, every path from the root node to a leaf represents a sequence of accepted candidate points to the root set S. If, at some point, a leaf has metric δ = 0 then that leaf represents a possible solution path.

We keep a number of children nodes (in our experiments we kept at least 20-50 best children) whose metrics are the best (they may even have different projected gates γ). We also define the maximum depth T D of the search tree (in our experiments we tried T D = 1, . . . , 20). When the tree at depth T D is constructed, we then examine the leaves and see where we get the best metric over all leaves at all different branches. Tracking back to the root, we then choose to keep the top branch that leads to the best leaf(s). Other top branches from the root are removed. We then advance the root node to the first child of the selected branch and try to extend the tree's depth again from the remaining leaves, thus, keeping the search tree at a constant depth T D.

If, at every depth of the tree, each leaf is extended with additional 20-50 sub-branches, then the number of leaves will increase exponentially. However, we can apply a truncation algorithm to the leaves before extending the tree to the next depth. We simply keep no more than a certain number of promising leaves that will be expanded to the next depth, and other, less promising leaves we just remove from the tree (in our experiments the truncation level was up to 400 leaves overall for the whole tree). This type of truncation makes it possible to select the best top branch of the root node by "looking further" basically at any depth T D. Notably, the complexity does not depend on the depth T D, but it depends on the truncation level.

Truncation strategy. In brief, we keep those leaves with the best metrics, but try to distribute nearly equal leaves among different branches, so that we keep as many diverted solution paths as possible.

### Computation of δ(S, t i )

The "heart" and the critical part of the algorithm is the subalgorithm to compute the distances δ(S, t i ), given a fresh S. There are many candidates to test at each step, and there are many branches to track, so we need to make this core algorithm as fast as possible.

Note that the length of a point (.p is an integer) is 2n + 2 bits, plus the delay value. We will ignore the delay (.d) value when doing Boolean operations over two points. Let us assign the number of possible points as:

corresponds to a (2n + 2)-bit point p represented as an integer index, and the value stored in the cell will be the minimum delay p.d of that point such that it can be derived from S with exactly k gates.

Set the initial vector V 0 as ∀p → V 0 [p] = p.d, if p ∈ S, and V 0 [p] = ∞, otherwise. Thereafter, the vector V k+1 can be derived from the previously derived vectors V 0 . . . V k by applying the allowed 6 gates to points from some level 0 ≤ l < k (V l ) and the level k -l (V k-l ), thus resulting in total l + (k -l) + 1 = k + 1 gates. After a new V k+1 is derived, we simply check if it contains new distance values for the targets from T , and we repeat the procedure until all distances δ(S, t i ) for all t i in T are found. A high-level description of the algorithm is given in Algorithm 1, and in Appendix B.1 we provide a more detailed description alongside multiple computational tricks that can be made.  

### Double and Useless points

"Double" points. When, at some step of the algorithm, we find a candidate point c that is already in S but now having a smaller depth, then the point c is kept in C and tested along with other candidates. If it turns that adding c to S gives the best metric, we add it to S. An alternative strategy would be to update the point c.p in S with the lower depth c.d and recalculate depths of dependent points. However, it is not clear what to do with the parent points that were used to generate that previous c.p in S. We leave this as an open question for further research.

"Useless" points. At the end of the algorithm (when δ = 0), it could happen that S contains points that can be safely excluded while a solution can still be derived. As a final step, we try to remove points from S one by one and test if every target is reachable from the remaining S under the given depth constraints. In our experience this situation is rare, but it helped to remove 1-2 gates, mainly caused by "double" points.

The above problems with "double" and "useless" points are generic for such class of algorithms where certain depth constraints should be met, and Algorithm 1 in [LSL + 19] also falls under this category.

# Architectural improvements

Most known AES SBox architectures look quite similar, consisting of the Top and Bottom linear parts, and the middle non-linear part, as previously described in Section 2. In this section, we take that classic design and propose a number of improvements, along with a completely new architecture that focuses on low depth solutions. 

# Mul-Sum

## Two SBox architectures -Area and Depth

Referring to Figure 2, the architecture A (Area) is the classical one that implements designs based on tower and composite fields. It starts with the 8-bit input signal U to the Top linear matrix, which produces a 22-bit signal Q (as in [BP12]). We managed to reduce the number of needed Q-signals to 18, and refactored the multiplication and linear summation block Mul-Sum to 24 gates and depth 3. (See Appendix D.2 for equations). The output from the Mul-Sum block is the 4-bit signal X which is the input to the inversion over GF(2 4 ). The output from the inversion, Y, is non-linearly mixed with the Q signals, derived in the top matrix, and produces 18-bit signal N. The final step is the Bottom linear matrix that takes 18-bit N and linearly derives the output 8-bit signal R. The top and bottom matrices incorporate the SBox's affine transformation that depends on the direction.

In the new architecture D (Depth) we tried to remove the "irregular" bottom matrix and as a result shrinking the depth of the circuit as much as possible. The idea behind is that the bottom matrix only depends on the set of multiplications of the 4-bit signal Y and some linear combinations of the 8-bit input U. Thus, the result R can be achieved as follows:

where each M i is a 8 × 8 matrix representing 8 linear equations on the 8-bit input U, to be scalar multiplied by the Y i -bit. Those 4x8 linear circuits can be computed as a 32-bits signal L in parallel with the circuit for the 4-bits of Y. The result R is achieved by summing up four 8-bit sub-results. Therefore, in the architecture D we get the depth 3 after the inversion step (critical path: MULL and 8XOR4 blocks), instead of the depth 5-6 in the architecture A. That new architecture D requires a bit more gates, since the assembling bottom circuit needs 56 gates: 32NAND2+8XOR4. The reward is the lower depth.

A more detailed sketch of the two architectures is given in Figure 3, that includes the components of the designs, delays and the number of gates. 

## Six different scenarios of MULN

In the MULN block, where the 18-bit N-signals are computed, we need as input the 18-bit Q-signals and the inversion result Y. But we also need the following additional linear combinations of Y:

. Thus, the Y vector is actually extended to 9 bits, and the delays of N bits become different, depending on which of the Y i is used in the multiplication. For example, in the worst case, the delay of Y 00 is +2 compared to the delay of Y 1 . Thus, the resulting signals N will have different output delays. However, it is possible to compute these 5 additional Ys in parallel with the base signals Y 0 , . . . , Y 3 . This will cost some extra gates, but then the +2 delay can either shrink down to +1 or +0. In general one can consider the following 6 scenarios: In the next subsection we show how to find Boolean expressions for the above scenarios.

## INV. Inversion over GF(2 4 )

The inversion formulae are as follows:

In [BP12] they found a circuit of depth 4 and 17 XORs, but we would like to shrink the depth even further by utilizing a wider range of standard gates.

We have adapted the algorithm from Section 4.2 to also find a small solution for the INV block. The idea is simple; each Y i is a truth table of length 16 bits, based on a 4-bit input X 0 , . . . , X 3 . We define our "point" to be a 16-bit value. All standard gates, AND, OR, XOR, MUX, NOT, including their negate versions, can be applied to any combination of "known" points (S), and distances to target points T can be computed in a similar manner as before. Using this slightly modified algorithm for floating multiplexers, we found a solution with only 9 gates and depth 3. The results are shown in Equation 2 and Table 2. The full listing of the formulae for scenarios S0-S5 can be found in D.2.  In our tradeoff circuits we have used scenario S1, as it showed best results with respect to the area and depth. For the bonus circuits, we used S0 as it has the smallest area. For the fast circuit, only the INV formulae are needed. We also derived an alternative circuit for the inversion block without multiplexers, the results and formulae are given in B.2.

## Additional Transformation Matrices (ATM)

We are solving the top matrices through exhaustive search and the bottom matrices with various heuristic techniques. The way those matrices look, naturally influence the final number of gates in the solution. Here we present a simple method to try different top and bottom matrices for the best solution.

Assume that the SBox is a black box and, when excluding the final addition of the constant, it performs the function:

where x -1 is the inverse element in the Rijndael field GF (2 8 ), and the matrix A 8×8 is the affine transformation. In any field of characteristic 2: squaring, square root, and multiplication by a constant -are linear functions, thus for a non-trivial choice (α, β) we have:

If the initial Top and Bottom matrices for the forward and inverse SBoxes were T F , B F , T I , F I , respectively, then one can choose any α = 1, . . . , 255 and β = 0, . . . , 7, and change the matrices as follows:

where: E -is the 8x8 matrix that switches bits endianness (in our circuits input and output bits are in Big Endian) A -is the 8x8 matrix that performs the SBox's affine transformation C α -is the 8x8 matrix that multiplies a field element by the selected constant α P β -is the 8x8 matrix that raises an element of the Rijndael field to the power of 2 β T F /T I -are the original (without modifications) 18x8 matrixes for the top linear transformation of the Forward/Inverse SBoxes, resp. B F /B I -are the original (without modifications) 8x18 matrixes for the bottom linear transformation of the Forward/Inverse SBoxes, resp. There are 2040 choices for (α, β) pair and each choice gives new linear matrices. It is easy to test all of them and find the best combination that gives the smallest SBox circuit. We have applied this idea to both the forward as well as the inverse SBox, for both architectures A and D. Note that a similar approach was recently and independently considered in [UHNA19] but in that work they only considered multiplication with a constant, and not squaring.

### ATM approach for the combined SBox

For the combined SBoxes we can apply the ATM approach to the forward and the inverse parts independently. This means that we have 2040 2 = 4, 161, 600 variants of linear matrices to test. We have focused on the architecture D, since there is no bottom matrix and thus we can do a more extensive search. We searched through all those 4 million variants and applied the heuristic algorithm from the Section 4.1 as a quick analysis method to select a set of around 4000 promising cases. We then applied the algorithm given in Section 4.2 to find a solution with floating multiplexers. In our case we have n = 8 input bits and thus each point is encoded with 18 bits, and the complexity of calculating the distance δ(S, t i ) is quadratic over N = 2 18 points. In the search we used the search tree with the maximum depth T D ≤ 20 and the truncation level of 400 leaves. 

# Results and comparisons

In this section we present our best solutions for the AES SBox, both forward and combined. The stand-alone inverse SBox is perhaps not as widely used, and those results can be found in Appendix C. We compare our area and depth using the techniques described in Appendix A and where possible, we have recalculated the corresponding GE for other academic results for easier comparison. We present three different solutions for each SBox (forward, inverse, and combined): "fast", "tradeoff", and "bonus". The fast one is the solution with the lowest critical path, the tradeoff solution is a well-balanced trade-off between area and speed, and the bonus solution is given to establish a new record in terms of the smallest number of gates. Exact circuit expressions for all the derived solutions can be found in Appendix D, where we also indicate which algorithm was used in deriving the solution.

## Synthesis results

We have performed a synthesis of the results and compared with other recent academic work. The technology process is GlobalFoundries 22nm CSC20L [Glo19], and we have synthesized using Design Compiler 2017 from Synospys in topological mode with the compile_ultra command. We also turned on the flag compile_timing_high_effort to force the compiler to make as fast circuits as possible. In those graphs, the X axis is the clock period (in ps) and the Y axis is the resulting topology estimated area (in µm 2 ). We have not restricted the available gates in any way, so the compiler was free to use non-standard gates e.g., a 3 input AND-OR gate. To get the graphs in the following subsections, we have started at a 1200 ps clock period (∼833 MHz) and reduced the clock period by 20 ps until the timing constraints could not be met. We note that the area estimates by the compiler fluctuate heavily, and we believe that this is a result of the many different strategies the compiler has to minimize the depth. One strategy might be successful for say a 700 ps clock period, but a different strategy (which results in a significantly larger area) could be successful for 720 ps. There is also an element of randomness involved in the strategies for the compiler.    

## Forward SBoxes

We have included a number of interesting previous results for comparison in Table 4. The most famous design by Canright is widely used and cited. Our tradeoff SBox is both faster and smaller. We also included the work done by Boyar et al as their design was the starting point for our research. The two results from CHES'18 by Reyhani et al are the most recent, and our tradeoff SBox has a similar area as their "lightweight" version in terms of GE, but around 30% faster. The tradeoff SBox is both smaller and faster than their "fast" circuit. Also, our "fast" version is faster by 25% than their "fast" version, while maintaining a decent area increase. The currently fastest SBox done by Ueno has 270.71GE and 12.449XORs depth, while our fast version is only 243GE with depth 10.496XORs, outperforming the known fastest circuit by around 23%.

We also included the current known smallest circuit (in terms of standard gates) done by Boyar in 2016, which has 113 gates (220.73GE) and depth 27 gates. Our "bonus" circuit is even smaller with only 102 gates and depth 24, reaching as low as 195.10GE. Synthesis results are shown in Figure 4.

## Combined SBoxes

Table 5 shows our results compared to the three previously known best results. Our tradeoff combined SBox has a similar size to that of [Can05] and [RMTA18b], but its speed is a lot faster due to a much lower depth of the circuit. The tradeoff circuit has depth 16 (in reality only 14.305XORs) and 145 gates (297GE), while Canright's combined SBox is of size 150(+2) gates (298GE) and the depth 30 (25.644XORs). The bonus solution in this paper has slightly smaller depth than the most recent result [RMTA18b] but is significantly smaller in size (127 vs 149(+8) standard gates). Finally, the proposed "fast" design using Architecture D has the best currently known depth. Our synthesis results are shown in the comparison Figure 5.

# Conclusions

In this paper we have introduced a number of heuristic and exhaustive search methods for minimizing the circuit realization of the AES SBox. We have proposed a novel idea on how to include the multiplexers of the combined SBox in the minimization algorithms, and derived smaller and faster circuit realizations for the forward, inverse, and combined AES SBox. We also introduced a new architecture where we remove the "irregular" bottom linear matrix, in order to derive a faster solution than previously known.

# A Area and speed measurement methods

Firstly, we introduce some notations. Gate names are written in capital letters GATE (examples: AND, OR). The notation mGATEn means m gates of type GATE, each of which has n inputs (example: XOR4, 8XOR4, NAND3, 2AND2). When the number of inputs n is missing then the assumption is that the gate has minimum inputs, usually only 2 (3 for MUX).

Cells that are constructed as gates combinations can be described as GATES1-GATE2, meaning that we first perform one or more on the first level GATES1, then the result goes to the gate on the second level 2. Example: NAND2-NOR2, means that the cell has 3 inputs (a, b, c) and the corresponding Boolean function is NOR2(a, NAND2(b, c)).

We present two different methods of comparing circuits; the standard method and the technology method.

# A.1 Standard method

Cells. The basic elements that are considered in the standard method are:

{XOR, XNOR, AND, NAND, OR, NOR, MUX, NMUX, NOT}. Negotiation of NOT gates. In some places of the circuit there can be a need to use the inverted version of a signal. This can be done in several ways, without the explicit use of a NOT gate. Here we list a few of them.

Method 1. One way to implement a NOT gate is to change the previous gate that generates that signal to instead produce an inverted signal. For example, switch XOR into XNOR, AND into NAND, etc.

Method 2. In several technologies some gates can produce both the straight signal and the inverted version. For example, XOR gates in many implementations produce both signals simultaneously, and thus the inverted value is readily available.

Method 3. We can change the gates following the inverted signal such that the resulting scheme would produce the correct result given the inverted input, using e.g. De Morgan's laws.

Summarizing the above, we believe that NOT gates may be ignored while evaluating a circuit with the standard method, since it can hardly be counted as a full gate. However, for completeness, we will print out the number of NOT gates in the resulting tables.

Area. For area comparisons the number of basic elements is counted without any size distinction between them. The NOT-gates are ignored.

Depth. The depth is counted in terms of the number of basic elements on the circuit path. The overall depth of a circuit is therefore the delay of the critical path. The NOT-gates are ignored.

# A.2 Technology method

Cells. Some papers complement the standard cells with a few extra combinatorial cells, often available in various technologies. For example, the gates NAND2-NAND2, NOR2-NOR2, 2AND2-NOR2, XOR4 could be highly useful to improve and speed up our SBox circuits in this paper. However, for comparison purposes with previous academic results, we will stay with the set of standard cells in order to make a more fair comparison. In this method we do count NOT gates in both the delay and the area.

Area. There exist many ASIC technologies (90nm, 45nm, 14nm, etc) from different vendors (Intel, Samsung, GlobalFoundries, etc), with different specifics. In order to develop an ASIC one needs to get a "standard cells library" of a certain technology, and that library usually includes much more versatile cells than the basic elements listed above, so that the designer has a wider choice of building blocks.

However, even if we take a standard cell, for example XOR, then for different technologies that cell has different areas and delays. This makes it harder to compare two circuits of the same logic developed by two academic groups, when they chose to apply different technologies.

For a fair comparison of circuit area of various solutions in academia we usually utilize the term of gates equivalence (GE), where 1GE is the size of the smallest NAND gate. The size of a circuit in GE terms is then computed as Area(Circuit)/Area(NAND) → t GE. Knowing the estimated GE values for each standard or technology cell makes it possible to compute an estimated area size of a circuit in terms of GE. Although various technologies have slightly different GEs for standard cells, those GE numbers are still pretty close to each other.

We have studied several technologies, where data books are available, and came to the decision to utilize GE values given in the data book by the Samsung's STD90/MDL90 0.35µm 3.3V CMOS technology [Sam00]. The cells to be used are without the speed x-factor.

Other data books that we checked include IBM's 0.18µm [Int01], WPI 0.5mm [MNG00], FARADAY's 90µm [FAR06], TSMC 0.18µm [Art01], Web resource [Pet], etc.; we verified that GE numbers given in [Sam00] are quite fair and close to the reality. This makes it possible to have an approximated comparison of the effectiveness of different circuits, even though they may be developed for different technologies.

Depth. Different cells, like XOR and NAND, not only differ in terms of GEs but also differ in terms of the maximum delay of the gates.

Normally data books include the delays (e.g., in ns.) for each gate, and for all inputoutput combinations.

We propose to normalize the delays of all used gates by the delay of the XOR gate. I.e., we adopt the worst-case delay of the XOR gate as 1 unit in our measurements of the critical path. Then we look at each standard cell and pick the maximum of the switching characteristics for all in-out paths of the cell and divide it by the maximum delay of the XOR gate, so that we get the normalized delay-units for each of the gates utilized.

For multiplexers (MUX and NMUX), we ignore propagation delays for the select bit since in most cases, the select bit is the input to the circuit. For example, in the combined SBox the select bit says if we compute the forward or the inverse SBox, and that selection is ready as an input signal and not switching over the circuit signals propagation, so it can be regarded as a stable signal.

The proposed above method is similar to the idea of GEs, but is adopted for computing the depth of a circuit, normalized in XOR delays. The reason to choose XOR as the base element for delay counting is that circuits often have a lot of XOR gates, and thus, it now becomes possible to compare the depths between the standard and the technology methods as well. For example, in our SBox the critical path contains 14 gates, most of which are XORs, but in reality the depth would be equivalent to only 12.26 XOR-delays, due to the critical path contains also faster gates.

The area and delays for the Samsung's STD90/MDL90 0.35µm gates are summarized in Table 6. 

# B Algorithmic details and improvements

In this section we present some more details to various algorithms previously described in the paper.

# B.1 On the computation of δ(S, t i ) in Section 4.2.5

In this section we give a more detailed presentation on how the computation of δ(S, t i ) can be done. A slightly re-organized set of algorithms for computing δ(S, t i ) is given by Algorithms 2, 3, and 4.

# Algorithm 2 Computation of all distances

Init k = 0 5: while true do 6: 

# Algorithm 3 Convolution of XOR gates

There are two convolution algorithms, for XOR gates and for MUX gates, and they can be performed independently. The MUX-convolution can be done in linear time O(N ). We first collect the smallest distances for all possible F -values and I-values independently (each of which has √ N possible indexes), then the gate MUX can be applied to any of the combinations, so the convolution is O( √ N 2 = N ). The XOR-convolution is a bit more complicated and it has quadratic complexity O(N 2 ) in general case. Algorithmic improvements. Assume for some S we have already computed all distances δ i = δ(S, t i ). For each candidate c from C, we add it to S so that S = S ∪ c, then we need to compute all distances δ i = δ(S , t i ) in order to compute the metrics and decide on which c is good. Note that adding a single candidate c implies δ i ≤ δ i for every target t i . Therefore, we should modify the algorithm Distances(S', T, maxδ) such that we set maxδ = max{δ i } -1, and check in the end that if δ i == ∞ then δ i = maxδ. This Set ∀i = 0, . . . , 2 n+1 -1 :

high half of a related to F part 5:

Set i = a mod 2 n+1 low half of a related to I part 

This way we construct C with unique candidates and also having the smallest depths.

Architectural improvements. MUX(a, b) and MUX(b, a) can be combined in a single MUX-convolution function. In max{d 1 , d 2 } + 1, move the +1 operation outside the convolution functions, and do it after the convolutions, instead. p ⊕ {.p=[1|0|1|0], .d=0} is done in order to include gates with negated output; those can be moved outside the convolution functions as well and be performed in the main function Distances() in linear time. This helps to reduce the number of operations in the critical loop of the function ConvolutionXOR(), basically this doubles the speed. When A = B, then in ConvolutionXOR() we only need to run b starting from a. When B is not equal to V 0 , then ConvolutionXOR() can be done only on the half values of b, since we know that all vectors V k for k > 0 are symmetric in regards to NOT-gates. When A[a] = ∞ in ConvolutionXOR() then we do not need to enter the inner loop for b. The same check for B[b] = ∞ is not justified since it adds an unnecessary branching in the critical loop.

Leveraging SIMD (SSSE3). It is quite clear that ConvolutionMUX() can be easily refactored to utilize SIMD vectorized instructions and, for example, 128-bit registers (SSE). However, it is a bit tricky to find a way how to use SIMD instructions for the function ConvolutionXOR(). First of all, assume each cell A[a], B[b] are all of char type (byte), then we must start b aligned to 16 bytes, since our registers are 128-bit long. Secondly, the result of p = a ⊕ b for a = 0, . . . , 15 mod 16 will end up in a permuted location p, but that permutation would only happen in the low 4 bits. With the help of _mm_shuffle_epi8() we can make a permutation of the destination 16-byte block, where the permutation vector only depends on the value of a mod 16 (recall that b = 0 mod 16). Those permutation vectors can be hard coded in a constant table. Other operations within that ConvolutionXOR() are trivial to implement. One could also try to utilize 256-bit long registers, thus speeding up the algorithms even more.

# B.1.1 More on ConvolutionXOR()

One can notice that ConvolutionXOR() may be done with the help of the following convolution:

where the operation x•y → max{a, b}, and x+y → min{a, b}. Thus, we have a convolution to be done in the (min, max)-algebra. One could think of applying Fast Walsh-Hadamard Transform (FWHT) in O(N log N ) but the problem is that that algebra does not have an inverse element.

In [BHWZ94] there is an algorithm "MinConv" that can be converted into our convolution problem, and it is claimed to work "around and in average" O(N log N ) time. The idea behind MinConv is to sort A and B vectors, then we get the smallest delays in the beginning of the vectors A and B. Thus, we can enumerate the max{A[a], B[b]} delays starting from the smallest. Also, we should take care of the indexes while sorting A and B, so that we can find the destination point p = a ⊕ b. Every point p hit the first time will receive the smallest possible delay, and thus can be skipped later on. The idea is that the predicted number of hits to cover all N points of the result should be around N log N .

We have programmed that but it did not demonstrate a speed up on our input size (n=8, N=2 18 ) and actually performed slower than our SIMD-improved quadratic algorithm, at least on our input size. Also, the above algorithm cannot be parallelized.

# B.1.2 ConvolutionXOR() in O(maxDelay 2 • N log N ) time

Usually the delay values stored in V vectors are small. We can rely on that fact in order to develop an algorithm that may be faster than O(N 2 ).

The idea is simple. Construct two vectors A We should repeat the above for all combinations of x, y = 0, . . . , maxD, each step of which has the complexity O(N log N ). The value of maxDelay can also be determined in the beginning of the algorithm linearly. Also note that maxDelay may be different for A and B, so that x and y may have different ranges.

# B.1.3 ConvolutionXOR() in O(|S| 2 ) time

When constructing the vector V 1 from the initial V 0 is it worth to do the classical way and run through pairs of points of S, instead of doing the full scale convolution over N points. However, the number of newly generated points grows very rapidly and this method can only be applied to the very first V s (in our experiments we have seen some "win" only in V 1 , then for further V k , k > 1 we have used our SIMD optimized convolution algorithms).

# B.2 Alternative equations for INV block

In case we want to avoid multiplexers in the INV block then there is an alternative set of equations that we also present in this section. We have considered each expression independently, using a general depth 3 expression: Y i = ((X a op 1 X b ) op 5 (X c op 2 X d )) op 7 ((X e op 3 X f ) op 6 (X g op 4 X h )), where X a-h are terms from {0, 1, X 0 , X 1 , X 2 , X 3 } and op 1-7 are operators from the set of standard gates {AND, OR, XOR, NAND, NOR, XNOR}. Note that the above does not need to have all terms, for example, the expression AND(x, x) is simply x.

The exhaustive search can be organized as follows. Let us have an object Term which consists of a truth table TT of length 16 bits, based on the 4 bits X 0 , . . . , X 3 , and a Boolean function that is associated with the term. We start with the initial set of available terms T (0) = {0, 1, X 0 , . . . , X 3 }, and then construct an expression for a chosen Y i iteratively. Assume at some step k we have the set of available terms T (k) , then the next set of terms and associated expressions can be obtained as:

taking care of unique terms. At some step we will get one or more term(s) whose TTs are equal to target TTs (Y i s).

Since we could actually get multiple Boolean functions for each Y i , we should select only the "best" functions following the criteria: there are no NOT gates (due to better sharing capabilities), there is a maximum number of gates that can be shared between the 4 expressions for Y 0 , . . . , Y 3 , and the area/depth in terms of GE is small.

Using this technique, we have found a depth 3, 15 gates solution for the inversion. The equations are given below, where we also provide depth 3 solutions for the additional 5 signals {Y 01 , Y 23 , Y 02 , Y 13 , Y 00 } such that they can share a lot of gates in the mentioned scenarios S0-S5. Listing 1: INV refactored, without multiplexers. When implementing the above circuits for the scenarios S0-S5, and sharing the gates in a best possible way, we then got the results shown in Table 7. 

# C Inverse SBoxes

The stand-alone inverse SBox is as far as we know, not used very much. But we provide the comparison with previously known solutions in Table 8. 

# D.1 Preliminaries

In the below listings we present 9 circuits for the forward, inverse, and combined SBoxes that utilize two architectures A(small) and D(fast). The used symbols are:

• ##comment -a comment line

• @filename -means that we should include the code from another file filename , the listing of which is then given in this section as well.

• a ^b -is the usual XOR gate, other gates are explicitly denoted and taken from the set of {XNOR, AND, NAND, OR, NOR, MUX, NMUX, NOT}

• (a op b) -where the order of execution (the order of gate connections) is important we specify it by brackets.

The input to all SBoxes are the 8 signals {U0..U7} and the output are the 8 signals {R0..R7}. The input and output bits are represented in Big Endian bit order. For combined SBoxes the input has additional signals ZF and ZI where ZF=1 if we perform the forward SBox and ZF=0 if inverse, otherwise; the signal ZI is the complement of ZF. We have tested all the proposed circuits and verified their correctness.

The circuits are divided into sub-programs, according to Figure 3. In Section D.2 we describe the common shared components, and then for each solution we give components (common or specific) for the circuits. 

# Acknowledgements

We would like to thank the Ericsson Research Data Center team for their patience and help with the compute resources that made this work possible, and our colleague Ben Smeets and all reviewers for providing valuable comments to the manuscript.

# D.3 Forward SBox (fast)

# Forward (fast) @ftop.d @mulx.a @inv.a @mull.f @mull.d @8xor4.d # File: ftop.d # Exhaustive search

Listing 5: Forward SBox with the smallest delay (fast)

# D.4 Forward SBox (tradeoff)

# Forward (tradeoff) → @ftop.a @mulx.a @s1.a @muln.a @fbot.a # File: ftop.a # Exhaustive search 

# D.5 Forward SBox (bonus)

We include these bonus circuits just to update the world record for the smallest SBox.

The new record is 102 gates with depth 24.

# Forward (bonus) @ftop.b @mulx.a @s0.a @muln.a @fbot.b Listing 9: Combined SBox circuit with a good area/depth trade-off (tradeoff)

# D.8 Combined SBox (bonus)

# Combined (bonus) @ctop.b @mulx.a @s0.a @muln.a @cbot.b # Inverse (fast) @itop.d @mulx.a @inv.a @mull.i @mull.d @8xor4.d

Listing 11: Forward SBox with the smallest delay (fast)

# D.10 Inverse SBox (tradeoff)

# Inverse (tradeoff) → @itop.a @mulx.a @s1.a @muln.a @ibot.a # File: itop.a # Exhaustive search Listing 12: Inverse SBox circuit with good area/depth trade-off (tradeoff) Note: the above 'NOT(U2)' in the file 'itop.a' is removable by setting Q11=U2 and accurately negating some of the gates and variables downwards where Q11 is involved. For example, the variable Y01 should be negated as well due to: N0 = NAND(Y01, Q11); consequently, all gates involving Y01 should be negated, leading to negation of other Q variables, and so on.

# D.11 Inverse SBox (bonus)

# Inverse (bonus) @itop.b @mulx.a @s0.a @muln.a @ibot.b Listing 13: Inverse SBox circuit with the smallest number of gates (bonus)

