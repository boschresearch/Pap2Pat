# II. DEFINITIONS AND BASIC CONSTRUCTION

Let be a state space, and let be a set of transition functions, where every is a function . A Gray code is an ordered list of distinct elements from such that for every , for some . If for some , then the code is cyclic. If the code spans the entire space we call it complete.

Let denote the set of integers . An ordered set of flash memory cells named , each containing a distinct charge level, induces a permutation of by writing the cell names in descending charge level , i.e., the cell has the highest charge level while has the lowest. The state space for the rank modulation scheme is therefore the set of all permutations over , denoted by .

As described in the previous section, the basic minimal-cost operation on a given state is a "push-to-the-top" operation by which a single cell has its charge level increased so as to be the highest of the set. Thus, for our basic construction, the set of minimal-cost transitions between states consists of functions pushing the th element of the permutation, , to the front Throughout this work, our state space will be the set of permutations over , and our set of transition functions will be the set of "push-to-the-top" functions. We call such a code a length-rank modulation Gray code ( -RMGC). where the permutations are the columns being read from left to right. The sequence of operations creating this cyclic code is: , , , , , . This sequence will obviously create a Gray code regardless of the choice of the first column.

One important application of the Gray codes is the realization of logic multilevel cells. The traversal of states by the Gray code is mapped to the increase of the cell level in a classic multilevel flash cell. As an -RMGC has states, it can simulate a cell of up to discrete levels. Current data storage schemes (e.g., floating codes [22]) can therefore use the Gray codes as logic cells, as illustrated in Fig. 1, and get the benefits of rank modulation.

We will now show a basic recursive construction for -RMGCs. The resulting codes are cyclic and complete, in the sense that they span the entire state space. Our recursion basis is the simple 2-RMGC: , . Now let us assume we have a cyclic and complete -RMGC, which we call , defined by the sequence of transitions and where , i.e., a "push-to-the-top" operation on the second element in the The second is realized by combining three flash cells with no thresholds and by using a rank-modulation scheme. The possible transitions between states are given by the 3-RMGC of Example 1.

permutation. 1 We further assume that the transition appears at least twice. We will now show how to construct , a cyclic and complete -RMGC with the same property.

We set the first permutation of the code to be , and then use the transitions to get a list of permutations which we call the first block of the construction. By our assumption, the permutations in this list are all distinct, and they all share the property that their last element is (since all the transitions use just the first elements). Furthermore, since , we know that the last permutation generated so far is . We now use to create the first permutation of the second block of the construction, and then use again to create the entire second block. We repeat this process times, i.e., use the sequence of transitions a total of times to construct blocks, each containing permutations. The following two simple lemmas extend the intuition given above.

## Lemma 2:

The second element in the first permutation in every block is . The first element in the last permutation in every block is also .

Proof: During the construction process, in each block we use the transitions in order. If we were to use the transition next, we would return to the first permutation of the block since are the transitions of a cyclic -RMGC. Since the element is second in the initial permutation of the block, it follows that it is the first element in the last permutation of the block. By the construction, we now use , thus making the element second in the first permutation of the second block. By repeating the above arguments for each block we prove the lemma.

Lemma 3: In any block, the last element of all the permutations is constant. The sequence of last elements in the blocks constructed is . The element is never a last element.

Proof: The first claim is easily proved by noting that the transitions creating a block, , only operate on the first positions of the permutations. Also, by the same logic used in the proof of the previous lemma, if the first permutation of a block is , then the last permutation in a block is , and thus the first permutation of the next block is . It follows that if we examine the sequence containing just the first permutation in each block, the element remains fixed, and the rest just rotate by one position each time. By the previous lemma, the fixed element is , and therefore, the sequence of last elements is as claimed.

Combining the two lemmas above, the blocks constructed so far form a cyclic (but not complete) -RMGC, that we call , which may be schematically described as as shown at the bottom of the page (where each box represents a single block, and denotes the sequence of transitions ).

It is now obvious that is not complete because it is missing exactly the permutations containing as their last element. We build a block containing these permutations in the following way: we start by rotating the list of transitions such that its last transition is . 2 For convenience, we denote the rotated sequence by , where

. Assume the first permutation in the block is . We set the following permuta-tions of the block to be the ones formed by the sequence of transitions . Thus, the last permutation in is . In , we look for a transition of the following form: . We contend that such a transition must surely exist:

does not contain permutations in which is last, while it does contain permutations in which is next to last, and some where is the first element. Since is cyclic, there must be at least one transition pushing an element from a next-to-last position to the first position. At this transition we split and insert as follows:

. . . . . . . . . . . .

where it is easy to see all transitions are valid. Thus, we have created and to complete the recursion we have to make sure appears at least twice, but that is obvious since the sequence contains at least one occurrence of , and is replicated times, . We therefore reach the following conclusion.

Theorem 4: For every integer there exists a cyclic and complete -RMGC.

Example 5: We construct a 4-RMGC by recursively using the 3-RMGC shown in Example 1, to illustrate the construction process. The sequence of transitions for the 3-RMGC in Example 1 is , , , , , . As described in the construction, in order to use this code as a basis for the 4-RMGC construction, we need to have as the last transition. We therefore rotate the sequence of transitions to be , , , , , . The resulting first three blocks, denoted , are To create the missing fourth block, , the construction requires a transition sequence ending with , so we use the original sequence , , , , , shown in Example 1. To decide the starting permutation of the block, we search for a transition of the form in . Several such transitions exist, and we arbitrarily choose seen in the fifth and sixth columns of . The resulting missing block, , is Inserting between the fifth and sixth columns of results in the following 4-RMGC given at the bottom of the page.

## III. BALANCED -RMGCS

While the construction for -RMGCs given in the previous section is mathematically pleasing, it suffers from a practical drawback: while the top-charged cells are changed (having their charge level increased while going through the permutations of a single block), the bottom cell remains untouched and a large gap in charge levels develops between the least charged and most charged cells. When eventually, the least charged cell gets "pushed-to-the-top," in order to acquire the target charge level, the charging of the cell may take a long time or involve large jumps in charge level (which are prone to cause write-disturbs in neighboring cells). The balanced -RMGC described in this section solves this problem.

### A. Definition and Construction

In the current models of flash memory, it is sometimes the case that due to precision constraints in the charge placement mechanism, the actual possible charge levels are discrete. The rank-modulation scheme is not governed by such constraints, since it only needs to order cell levels unambiguously by means of comparisons, rather than compare the cell levels against predefined threshold values. However, in order to describe the following results, we will assume abstract discrete levels, that can be understood as counting the number of push-to-the-top operations executed up to the current state. In other words, each push-to-the-top increases the maximum charge level by one.

Thus, we define the function , where is the charge level of the th cell after the th programming cycle. It follows that if we use transition in the th programming cycle and the th cell is, at the time, th from the top, then , and for , . In an optimal setting with no overshoots, . The jump in the th round is defined as , assuming the th cell was the affected one. It is desirable, when programming cells, to make the jumps as small as possible. We define the jump cost of an -RMGC as the maximum jump during the transitions dictated by the code. We say an -RMGC is nondegenerate if it raises each of its cells at least once. A nondegenerate -RMGC is said to be optimal if its jump cost is not larger than any other nondegenerate -RMGC.

Lemma 6: For any optimal nondegenerate -RMGC, , the jump cost is at least . Proof: In an optimal -RMGC, , we must raise the lowest cell to the top charge level at least times. Such a jump must be at least of magnitude . We cannot, however, do these jumps consecutively, or else we return to the first permutation after just steps. It follows that there must be at least one other transition ,

, and so the first to be used after it jumps by at least a magnitude of .

We call an -RMGC with a jump cost of a balanced -RMGC. We now show a construction that turns any -RMGC (balanced or not) into a balanced -RMGC. The original -RMGC is not required to be cyclic or complete, but if it is cyclic (complete) the resulting -RMGC will turn out to be also cyclic (complete). The intuitive idea is to base the construction on cyclic shifts that push the bottom to the top, and use them as often as possible. This is desirable because does not introduce gaps between the charge levels, so it does not aggravate the jump cost of the cycle. Moreover, partitions the set of permutations into orbits of length . Theorem 7 gives a construction where these orbits are traversed consecutively, based on the order given by the supporting -RMGC.

Theorem 7: Given a cyclic and complete -RMGC, , defined by the transitions , then the following transitions define an -RMGC, denoted by , that is cyclic, complete and balanced: otherwise for all . Proof: Let us define the abstract transition , , that pushes to the bottom the th element from the bottom:

Because is cyclic and complete, using starting with a permutation of produces a complete cycle through all the permutations of , and using them starting with a permutation of creates a cycle through all the permutations of with the respective first element fixed, because they operate only on the last elements. Because of the first element being fixed, those permutations of produced by , also have the property of being cyclically distinct. Thus, they are representatives of the distinct orbits of the permutations of under the operation , since represents a simple cyclic shift when operated on a permutation of .

Taking a permutation of , then using the transition once, , followed by times using , is equivalent to using Every transition of the form , , moves us to a different orbit of , while the consecutive executions of generate all the elements of the orbit. It follows that the resulting permutations are distinct. Schematically, the construction of based on is

The code is balanced, because in every block of transitions starting with a , we have: the transition has a jump of ; the following transitions have a jump of , and the rest a jump of . In addition, because is cyclic and complete, it follows that is also cyclic and complete.

Theorem 8: For any , there exists a cyclic, complete, and balanced -RMGC.

Proof: We can use Theorem 7 to recursively construct all the supporting -RMGCs, , with the basis of the recursion being the complete cyclic 2-RMGC: , .

A similar construction, but using a more involved secondorder recursion, was later suggested by Etzion [9].

Example 9: Fig. 2 shows the transitions of a recursive, balanced -RMGC for . The permutations are represented in an matrix, where each row is an orbit generated by . The transitions between rows occur when is the top element. Note how these permutations (the exit points of the orbits), after dropping the at the top and turning them upside down, form a 3-RMGC:

This code is equivalent to the code from Example 1, up to a rotation of the transition sequence and the choice of first permutation. Fig. 3 shows the charge levels of the cells for each programming cycle, for the resulting balanced 4-RMGC.

#### B. Successor Function

The balanced -RMGC can be used to implement a logic cell with levels. This can also be understood as a counter that increments its value by one unit at a time. The function takes as input the current permutation, and determines the transition to the next permutation in the balanced recursive -RMGC. If , the next transition is always (line 2). Otherwise, if the top element is not , then the current permutation is not at the exit point of its orbit, therefore the next transition is (line 5). However, if is the top element, then the transition is defined by the supporting cycle. The function is called recursively, on the reflected permutation of (line 7). An important practical aspect is the average number of steps required to decide which transition generates the next permutation from the current one. A step is defined as a single query  The function is asymptotically optimal with respect to this measure: Theorem 10: In the function , the asymptotic average number of steps to create the successor of a given permutation is one.

Proof: A fraction of of the transitions are , and these occur whenever the cell is not the highest charged one, and they are determined in just one step. Of the cases where is highest charged, by recursion, a fraction of the transitions are determined by just one more step, and so on. At the basis of the recursion, permutations over two elements require zero steps. Equivalently, the query "is equal to " is performed for every permutation, therefore times; the query "is equal to " is performed only for permutations, therefore times, and so on. Thus, the total number of queries is . Since , the asymptotic average number of steps to generate the next permutation is as stated.

#### C. Ranking Permutations

In order to complete the design of the logic cell, we need to define the correspondence between a permutation and its rank in the balanced -RMGC. This problem is similar to that of ranking permutations in lexicographic order. We will first review the factoradic numbering system, and then present a new numbering system that we call b-factoradic, induced by the balanced -RMGC construction.

1) Review of the Factoradic Numbering System: The factoradic is a mixed radix numbering system. The earliest reference appears in [26]. Lehmer [27] describes algorithms that make the correspondence between permutations and factoradic.

Any integer number can be represented in the factoradic system by the digits , where for , and the weight of is (with the convention that ). The digit is always , and is sometimes omitted Any permutation has a unique factoradic representation that gives its position in the lexicographic ordering. The digits are in this case the number of elements smaller than that are to the right of . They are therefore inversion counts, and the factoradic representation is an inversion table (or vector) [15].

There is a large literature devoted to the study of ranking permutations from a complexity perspective. Translating between factoradic and decimal representation can be done in arithmetic operations. The bottleneck is how to translate efficiently between permutations and factoradic. A naive approach similar to the simple algorithms described in [27] requires . This can be improved to by using merge-sort counting, or a binary search tree, or modular arithmetic, all techniques described in [25]. This can be further improved to [30], by using the special data structure of Dietz [7]. In [30] linear time complexity is also achieved by departing from lexicographic ordering. A linear time complexity is finally achieved in [28], by using the fact that the word size has to be in order to represent numbers up to , and by hiding rich data structures in integers of this size.

2) B-Factoradic-A New Numbering System: We will now describe how to index permutations of the balanced recursive -RMGC with numbers from , such that consecutive permutations in the cycle have consecutive ranks modulo . The permutation that gets index is a special permutation that starts a new orbit generated by , and also starts a new orbit in any of the recursive supporting -RMGCs, . The rank of a permutation is determined by its position in the orbit of , and by the rank of the orbit, as given by the rank of the supporting permutation of . The position of a permutation inside an orbit of is given by the position of . If the current permutation is and for , then the position in the current orbit of is (because the orbit starts with in position ). The index of the current orbit is given by the rank of the supporting permutation of , namely, the rank of (notice that the permutation of is reflected). Therefore, if , then

The above formula can be used recursively to determine the rank of the permutations from the supporting balanced -RMGCs, for . It now becomes clear what permutation should take rank . The highest element in every supporting RMGC should be in the second position, therefore, , , , , and so on, and . Therefore, gets the rank . See Example 9 for the construction of the recursive and balanced 4-RMGC where the permutation has rank . Equation (1) induces a new numbering system that we call b-factoradic (backwards factoradic). A number can be represented by the digits , where and the weight of is . In this case is always and can be omitted. It is easy to verify that this is a valid numbering system, therefore, any has a unique b-factoradic representation such that The weights of the b-factoradic are sometimes called "falling factorials," and can be represented succinctly by the Pochhammer symbol.

Example 11: Let and be the current permutation. We can find its b-factoradic representation as follows. We start from the least significant digit , which is given by the position of minus modulo , so (here we keep the elements of the permutation indexed from to ). We now recurse on the residual permutation of five elements, (notice the reflected reading of this permutation, from towards the left). Now is given by the position of ;

. The residual permutation is , therefore, . For the next step, and . Finally, and . As always . The b-factoradic representation is therefore , where the subscript indicates the position of the digit. Going from a b-factoradic representation to a permutation of the balanced -RMGC can follow a similar reversed procedure.

The procedure of Example 11 can be formalized algorithmically, however, its time complexity is , similar to the naive algorithms specific to translations between permutations in lexicographic order and factoradic. We can in principle use all the available results for factoradic, described previously, to achieve time complexity of or lower. However, we are not going to repeat all those methods here, but rather describe a linear time procedure that takes a permutation and its factoradic as input and outputs the b-factoradic. We can thus leverage directly all the results available for factoradic, and use them to determine the current symbol of a logic cell.

The procedure --exploits the fact that the inversion counts are already given by the factoradic representation, and they can be used to compute directly the digits of the b-factoradic. A b-factoradic digit is a count of the elements smaller than that lie between and when the permutation is viewed as a cycle. The direction of the count alternates for even and odd values of . The inverse of the input permutation can be computed in time (line 1). The position of every element of the permutation can then be computed in constant time (lines 2 and 5). The test in line 6 decides if we count towards the right or left starting from the position that holds element , until we reach position that holds element . By working out the cases when and we obtain the formulas in lines 7 and 9. Since this computation takes a constant number of arithmetic operations, the entire algorithm takes time. Unranking, namely, going from a number in to a permutation in balanced order is likely to never be necessary in practice, since the logic cell is designed to be a counter. However, for completeness, we describe the simplest procedure , that takes a b-factoradic as input and produces the corresponding permutation. The procedure uses variable to simulate the cyclic counting of elements smaller than the current one. The direction of the counting alternates, based on the test in line 4.

### IV. REWRITING WITH RANK-MODULATION CODES

In Gray codes, the states transit along a well-designed path. What if we want to use the rank-modulation scheme to store data, and allow the data to be modified in arbitrary ways? Consider an information symbol that is stored using cells. In general, might be smaller than , so we might end up having permutations that are not used. On the other hand, we can map several distinct permutations to the same symbol in order to reduce the rewrite cost. We let denote the set of states (i.e., the set of permutations) that are used to represent information symbols. We define two functions, an interpretation function, , and an update function, .

#### Definition 12:

The interpretation function maps every state to a value in . Given an "old state" and a "new information symbol" , the update function produces a state such that .

When we use cells to store an information symbol, the permutation induced by the charge levels of the cells represents the information through the interpretation function. We can start the process by programming some arbitrary initial permutation in the flash cells. Whenever we want to change the stored information symbol, the permutation is changed using the "push-to-the-top" operations based on the update function. We can keep changing the stored information as long as we do not reach the maximal charge level possible in any of the cells. Therefore, the number of "push-to-the-top" operations in each rewrite operation determines not only the rewriting delay but also how much closer the highest cell-charge level is to the system limit (and therefore how much the cell block is to the next costly erase operation). Thus, the objective of the coding scheme is to minimize the number of "push-to-the-top" operations.

Definition 13: Given two states , the cost of changing into , denoted , is defined as the minimum number of "push-to-the-top" operations needed to change into .

For example, , . We define two important measures: the worst case rewrite cost and the average rewrite cost.

Definition 14: The worst case rewrite cost is defined as . Assume input symbols are independent and identically distributed (i.i.d.) random variables having value with probability . Given a fixed , the average rewrite cost given is defined as . If we further assume some stationary probability distribution over the states , where we denote the probability of state as , then the average rewrite cost of the code is defined as . (Note that for all , .)

In this section, we present a code that minimizes the worst case rewrite cost. In Section IV-A, we focus on codes with good average rewrite cost.

#### A. Lower Bound

We start by presenting a lower bound on the worst case rewrite cost. Define the transition graph as a directed graph with , that is, with vertices representing the permutations in . For any , there is a directed edge from to iff

. is a regular digraph, because every vertex has incoming edges and outgoing edges. The diameter of is . Given a vertex and an integer , define the ball centered at with radius as , and define the sphere centered at with radius as . Clearly

By a simple relabeling argument, both and are independent of , and so will be denoted by and respectively.

Lemma 15: For any .

Proof: Fix a permutation . Let be the set of permutations having the following property: for each permutation , the elements appearing in its last positions appear Example 21: Let and , and let the prefix-free code be as shown in Fig. 4(b). We can map the information symbols to the prefix sequences as follows:

Then, the mapping from the permutations to the information symbols is

Assume that the current state of the cells is , representing the information symbol . If we want to rewrite the information symbol as , we can shift cells 3, 4 to the top to change the state to . This rewrite cost is , which does not exceed . In general, given any current state, considering all the possible rewrites, the expected rewrite cost is always less than , the average codeword length.

The optimal prefix-free code cannot be constructed with a greedy algorithm like the Huffman code [19], because the internal nodes in different layers of the full permutation tree have different degrees, making the distribution of the vertex degrees in the code tree initially unknown. The Huffman code is a well-known variable-length prefix-free code, and many variations of it have been studied. In [20], the Huffman code construction was generalized, assuming that the vertex-degree distribution in the code tree is given. In [1], prefix-free codes for infinite alphabets and nonlinear costs were presented. When the letters of the encoding alphabet have lengths, only exponential-time algorithms are known, and it is not known yet whether this problem is NP-hard [12]. To construct prefix-free codes for our problem, which minimize the average codeword length, we present a dynamic-programming algorithm of time complexity . Note that without loss of generality, we can assume the length of any prefix sequence to be at most . The algorithm computes a set of functions , for , , and . We interpret the meaning of as follows. We take a subtree of that contains the root. The subtree has exactly leaves in the layers . It also has at most vertices in the layer . We let the leaves represent the letters from the alphabet with the lowest probabilities : the further the leaf is from the root, the lower the corresponding probability is. Those leaves also form prefix sequences, and we call their weighted average length (where the probabilities are weights) the value of the subtree. The minimum value of such a subtree (among all such subtrees) is defined to be . In other words, is the minimum average prefix-sequence length when we assign a subset of prefix sequences to a subtree of (in the way described above). Clearly, the minimum average codeword length of a prefix-free code equals . Without loss of generality, let us assume that . It can be seen that the following recursions hold.  The last recursion holds because a subtree with leaves in layers and at most vertices in layer can have leaves in layer . The algorithm first computes , then , and so on, until it finally computes , by using the above recursions. Given these values, it is straightforward to determine in the optimal code, how many prefix sequences are in each layer, and therefore determine the optimal code itself. It is easy to see that the algorithm returns an optimal code in time .

Example 22: Let and , and let us assume that . As an example, let us consider how to compute .

By definition, corresponds to a subtree of with a total of four leaves in layer 2 and layer 3, and with at most three vertices in layer 2. Thus, there are four cases to consider: either there are zero, one, two, or three leaves in layer 2. The corresponding subtrees in the first three cases are as shown in Fig. 5(a)-(c), respectively. The fourth case is actually impossible, because it leaves no place for the fourth leaf to exist in the subtree.

If layer 2 has leaves , then layer 3 has leaves and there can be at most vertices in layer 3 of the subtree. To assign to the four leaves and minimize the weighted average distance of the leaves to the root (which is defined as

), among the four cases mentioned above, we choose the case that minimizes that weighted average distance. Therefore Now assume that after computing all the 's, we find that That means that in the optimal code tree, there are two leaves in layer 1. If we further assume that we can determine that there are five leaves in layer 2, and the optimal code tree will be as shown in Fig. 4(b).

We can use the prefix-free code for rewriting in the following way: to change the information symbol to , push at most cells to the top so that the top-ranked cells are the same as the codeword .

#### B. Performance Analysis

We now analyze the average rewrite cost of the prefix-free code. We obviously have . When , the code design becomes trivial-each permutation is assigned a distinct input symbol. In this subsection, we prove that the prefix-free code has good approximation ratios under mild conditions: when , the average rewrite cost of a prefix-free code (that was built to minimize its average codeword length) is at most three times the average rewrite cost of an optimal code (i.e., a code that minimizes the average rewrite cost), and when , the approximation ratio is further reduced to .

Loosely speaking, our strategy for proving this approximation ratio involves an initial simple bound on the rewrite cost of any code when considering a rewrite operation starting with a stored symbol . We then proceed to define a prefix-free code which locally optimizes (up to the approximation ratio) rewrite operations starting with stored symbol . Finally, we introduce the globally optimal prefix-free code of the previous section, which optimizes the average rewrite cost, and show that it is still within the correct approximation ratio.

We start by bounding from below the average rewrite cost of any code, depending on the currently stored information symbol. Suppose we are using some code with an interpretation function and an update function . Furthermore, let us assume the currently stored information symbol is in some state , i.e., . We want to consider rewrite operations which are meant to store the value instead of , for all . Without loss of generality, assume that the probabilities of information symbols are monotonically decreasing Let us denote by the closest permutations to ordered by increasing distance, i.e., and denote for every . We note that are independent of the choice of , and furthermore, that while . The average rewrite cost of a stored symbol using a code is the weighted sum This sum is minimized when are assigned the closest permutations to with higher probability information symbols mapped to closer permutations. For convenience, let us define the functions . Thus, the average rewrite cost of a stored symbol , under any code, is lower-bounded by We continue by considering a specific intermediary prefixfree code that we denote by . Let it be induced by the prefix sequences . We require the following two properties:

P.1 For every , , we require .

# P.2 .

We also note that is not necessarily a prefix-free code with minimal average codeword length.

Finally, let be a prefix-free code that minimizes its average codeword length. Let be induced by the prefix sequences , and let be any state such that . Denote by the average rewrite cost of a rewrite operation under starting from state .

## By the definition of and we have

### Since it follows that

Since the same argument works for every , we can say that (2) It is evident that the success of this proof strategy hinges on the existence of for every , which we now turn to consider.

The following lemma is an application of the well-known Kraft-McMillan inequality [29].

Lemma 23: Let be nonnegative integers. There exists a set of prefix sequences with exactly prefix sequences of length , for (i.e., there are leaves in layer of the code tree ), if and only if Let us define the following sequence of integers: , , . We first contend that they are all nonnegative. We only need to check and indeed

### It is also clear that

In fact, in the following analysis, represent a partition of the alphabet letters. 

## ACKNOWLEDGMENT

The authors would like to thank the anonymous reviewers, whose comments helped improve the presentation of the paper.

### B. Optimal Code

We now present a code construction. It will be shown that the code has optimal worst case performance. First, let us define the following notation.

### Definition 17:

A prefix sequence is a sequence of distinct symbols from . The prefix set is defined as all the permutations in which start with the sequence .

We are now in a position to construct the code. Finally, to construct the update function , given and some , we do the following: let be the first elements which appear in all the permutations in . Apply push-to-the-top on the elements in to get a permutation for which, clearly, . Set .

### Theorem 19:

The code in Construction 18 is optimal in terms of minimizing the worst case rewrite cost.

Proof: First, the number of length prefix sequences is . By definition, the number of prefix sequences of length is at least , which allows the first of the construction. To complete the proof, it is obvious from the description of that the worst case rewrite cost of the construction is at most

. By Lemma 16 this is also the best we can hope for.

Example 20: Let , . Since , it follows that . We partition the states into sets, which induce the mapping The cost of any rewrite operation is at most .

## V. OPTIMIZING AVERAGE REWRITE COST

In this section, we study codes that minimize the average rewrite cost. We first present a prefix-free code that is optimal in terms of its own design objective. Then, we show that this prefix-free code minimizes the average rewrite cost with an approximation ratio if , and when , the approximation ratio is further reduced to .

### A. Prefix-Free Code

The prefix-free code we propose consists of prefix sets (induced by prefix sequences ) which we will map to the input symbols: for every and , we set . Unlike in the previous section, the prefix sequences are no longer necessarily of the same length. We do, however, require that no prefix sequence be the prefix of another.

A prefix-free code can be represented by a tree. First, let us define a full permutation tree as follows. The vertices in are placed in layers, where the root is in layer and the leaves are in layer . Edges only exist between adjacent layers. For , a vertex in layer has children. The edges are labeled in such a way that every leaf corresponds to a permutation from which may be constructed from the labels on the edges from the root to the leaf. An example is given in Fig. 4(a). A prefix-free code corresponds to a subtree of (see Fig. 4(b) for an example). Every leaf is mapped to a prefix sequence which equals the string of labels as read on the path from the root to the leaf.

For , let denote the prefix sequence representing , and let denote its length. For example, the prefix sequences in Fig. 4(b) have minimum length and maximum length . The average codeword length is defined as Here, the probabilities are as defined before, that is, information symbols are i.i.d. random variables having value with probability . We can see that with the prefix-free code, for every rewrite operation (namely, regardless of the old permutation before the rewriting), the expected rewrite cost is upper-bounded by . Our objective is to design a prefix-free code that minimizes its average codeword length. When respectively. Thus, for all . We now show that when , monotonically decreases in . Substituting into (3) we get After some tedious rearrangement, for any integer Hence, monotonically decreases for all which immediately gives us for all . By Lemma 23, the proof is complete.

We are now in a position to show the existence of , , for

. By Lemma 24, let be a list of prefix sequences, where exactly of the sequences are of length . Without loss of generality, assume Remember we also assume We now define to be the prefix-free code induced by the prefix sequences that is, for all , .

Note that for all , the prefix sequence represents the information symbol , which is associated with the probability in rewriting.

Lemma 25: The properties P. 1  . Intuitively speaking, we can map the indices for which to distinct prefix sequences of length , the indices for which to distinct prefix sequences of length , and so on.

Since the prefix sequences are arranged in ascending length order it follows that for every , Hence, property P.1 holds.

We can now state the main theorem.

Theorem 26: Fix some and let be a prefix-free code over which minimizes its average codeword length. For any rewrite operation with initial stored information symbol i.e., the average cost of rewriting under is at most three times the lower bound.

Proof: Define and consider the input alphabet with input symbols being i.i.d. random variables where symbol appears with probability . We . Let be a prefix-free code over which minimizes its average codeword length.

A crucial observation is the following: , the lower bound on the average rewrite cost of symbol , does depend on the probability distribution of the input symbols. Let us therefore distinguish between over , and over . However, by definition, and by our choice of probability distribution over for every . Since is a more restricted version of , it obviously follows that for every

. By applying inequality (2), and since by Lemma 25, the code exists over , we get that for all .

Corollary 27: When , the average rewrite cost of a prefix-free code minimizing its average codeword length is at most three times that of an optimal code.

Proof: Since the approximation ratio of holds for every rewrite operation (regardless of the initial state and its interpretation), it also holds for any average case.

With a similar analysis, we can prove the following result:

Theorem 28: Fix some , , and let be a prefix-free code over which minimizes its average codeword length. For any rewrite operation with initial stored information symbol i.e., the average cost of rewriting under is at most twice the lower bound.

Proof: See the Appendix.

Corollary 29: When , , the average rewrite cost of a prefix-free code minimizing its average codeword length is at most twice that of an optimal code.

## VI. CONCLUSION

In this paper, we present a new data storage scheme, rank modulation, for flash memories. We show several Gray code constructions for rank modulation, as well as data rewriting schemes. One important application of the Gray codes is the realization of logic multilevel cells. For data rewriting, an optimal code for the worst case performance is presented. It is also shown that to optimize the average rewrite cost, a prefix-free code can be constructed in polynomial time that approximates an optimal solution well under mild conditions. There are many open problems concerning rank modulation, such as the construction of error-correcting rank-modulation codes and codes for rewriting that are robust to uncertainties in the information symbol's probability distribution. Some of these problems have been addressed in some recent work [24].

## APPENDIX

In this appendix, we prove Theorem 28. The general approach is similar to the proof of Theorem 26, so we only specify some details that are relatively important here.

We define the following sequence of numbers: , , .

As before, we contend that they are all nonnegative. We only need to check and indeed, for

We now prove the equivalent of Lemma 24.

Lemma 30: When , , there exists a set of prefix sequences that contains exactly prefix sequences of length , for . Proof: Let us denote (4) When respectively. Thus, for all . We now show that when , monotonically decreases in . Substituting into (4) we get After some tedious rearrangement, for any integer Hence, monotonically decreases for all which immediately gives us for all . By Lemma 23, the proof is complete.

The remaining lemmas comprising the rest of the proof procedure are similar to those of Section V-B.

