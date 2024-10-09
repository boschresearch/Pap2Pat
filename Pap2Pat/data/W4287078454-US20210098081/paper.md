# I. INTRODUCTION

DNA storage is an exciting area because of its potential to provide both high information density and long-term stability [1]. To achieve a good trade-off between efficiency and reliability, DNA storage systems use error-correcting codes [2]- [9]. This paper considers the design and decoding of errorcorrection codes for the DNA storage channel (see Figure 1).

In this paper, the DNA storage channel is modeled as an insertion-deletion-substitution (IDS) channel and we focus on the case where a single encoded message is transmitted and multiple independent traces are observed [2]- [4], [7]. Sequence reconstruction methods for this problem date back to the 1980s [10]. This is closely related to the trace reconstruction problem in CS literature which asks how many traces (from a deletion channel) are needed to perfectly reconstruct the input message sequence, in the average or worst case. Many algorithms exist for trace reconstruction [11]- [17], a few of which (such as Bitwise Majority Alignment (BMA) [12]) can be modified for the IDS channel and have been used in DNA data storage systems [18], [19].

In practical systems, outer codes are used to code across multiple DNA strands in order to recover missing sequences and correct substitutions of individual symbols. Thus, we focus primarily on approximate reconstruction, as opposed to exact reconstruction. For IDS-like channels, one can compute exact posterior marginals by combining ideas from multiplesequence alignment [10] and the BCJR algorithm [20] (e.g., see [21]- [23]). Using these posterior marginals, it is easy to compute estimates that minimize additive distortion measures.

If the outer code uses hard-decision decoding, then a reasonable goal is to construct a practical estimator that, given a small number of traces, minimizes the expected Hamming distance to the input message. Strands may also use an inner code that is designed to provide additional protection [24], [25]. The inner code constraints can also be included in channel trellis [26] so that trellis-based methods can still be used for inference. In particular, for convolutional codes, it is possible to build a multidimensional trellis and perform symbolwise maximuma-posteriori (MAP) reconstruction, as observed in [23]. But, the complexity grows exponentially with the number of traces making exact inference infeasible.

## A. Contributions 1

• A low-complexity heuristic dubbed Trellis BMA is proposed that allows multiple single-trace trellis decoders to interact and estimate the input message on-the-fly. This is different from the approaches in [23], [27], [28] because each singletrace trellis decoder is influenced by the other decoders but it is related to the factor graph method in [22]. Our idea marries BCJR inference [20] for IDS channels [21] with the consensus approach of BMA, hence the name Trellis BMA. • A dataset of short strand DNA reads is generated that can be used to compare algorithms with actual DNA reads. This dataset will be released publicly to serve as a benchmark for coded trace reconstruction algorithms. • A new construction for the multi-trace IDS trellis is provided where the number of edges grows at a lower exponential rate (with the number of traces) than previous approaches.

Using BCJR inference to compute the symbolwise posterior probabilities for multiple traces is exponentially faster with this formulation.

### II. BACKGROUND A. DNA sequencing channel

The observed noise in DNA storage is a complicated combination of synthesis errors, amplification errors, and sequencing noise [29]. Even if we ignore the first two elements, the exact error profile of the noisy observations is dependent on the DNA sequencing technology used. However, exactly modeling this error profile is tedious and often impractical. Moreover, DNA sequencing technologies are evolving at a rapid pace and  Encoded DNA strands are read or "sequenced" using a sequencing technology, such as Illumina/Nanopore sequencers, and this outputs many noisy copies of the DNA sequence, from which the message vector in the data strand is recovered.

focusing on a particular error profile does not provide a futureproof approach to the problem. Instead, one typically considers a simplistic approximation and models the sequencing channel as an IDS channel (defined in the next subsection). Our ideas also extend naturally to more complex approximations for the channel model. For instance, insertions and deletions often occur in "bursts" and such events can be captured by a firstorder Markov model; our decoder can easily be modified to accommodate for such variations. Due to the difficulty of synthesizing and sequencing long DNA strands, DNA storage systems typically encode a single file into many different short strands. The Poisson nature of sampling short strands from the pool means that many of these strands will not be sequenced. Thus, an outer code is required and sequence numbers must be included for disambiguation [30]. This detail is sometimes neglected in simulation-based experiments (e.g., it seems a single long strand is used in [23]).

## B. Insertion deletion substitution channel

The insertion deletion substitution (IDS) channel is defined by its input/output alphabet Σ and four non-negative parameters p ins , p del , p sub , p cor with p ins + p del + p sub + p cor = 1. Given an N -length input sequence X = X 1 X 2 ...X N ∈ Σ N , the IDS channel sequentially takes in one input symbol at a time and constructs a variable length output Y = Y 1 Y 2 ... ∈ Σ * sequentially, where Σ * ∪ ∞ m=0 Σ m is the set of finite strings over Σ. Let the input pointer be i and the output pointer be j. Starting from i = j = 1, sample from the following events until i equals N + 1:

• Insertion (probability p ins ): choose Y j uniformly at random from Σ, increase j by 1, and leave i unchanged;

• Deletion (probability p del ): increase i by 1 and leave j unchanged;

• Substitution (probability p sub ): choose Y j uniformly at random from Σ \ {X i } . Increase both i and j by 1;

• Correct: (probability p cor ): Set Y j = X i . Increase i and j by 1.

## C. Trace reconstruction with and without coding

As discussed in the introduction, the trace reconstruction (TR) problem has been formalized in the CS literature as the question, "How many traces are required to exactly reconstruct X?" [12]- [17]. However, exact reconstruction is typically impossible from only a few traces [31]. Thus, we use the term TR algorithm for any algorithm that uses multiple independent traces

A more general formulation is to consider a code that maps a message sequence

This setup naturally fits the DNA storage architecture in Fig. 1.

## D. Error-correcting codes

For the inner code, this work considers marker repeat (MR) codes with the addition of a random scrambling vector to prevent shift invariance. Marker codes are synchronization codes where a short marker sequence is inserted periodically [32]. MR codes are a new variation where, periodically, a single input symbol is transmitted multiple times. For example, a length-N MR code with r length-2 repeats satisfies x n+1 = x n when n = iN/(r + 1) for i = 1, . . . , r. Results are given for MR codes with N = 110 and r = 6, 10. Rate-1/2 quaternary convolutional codes with memory 3-5 and puncturing were also tested and found to be inferior to MR codes above rate 3/4 (see Appendix D).

While this work focuses on the efficient decoding of the inner code when multiple traces are received, our analysis also assumes there will be an outer code. In particular, we target schemes where the inner codes are decoded first followed by the outer code. In contrast to [23], we do not consider iteration between the inner and outer decoder nor do we estimate the error rate after decoding of the outer code.

## E. Performance metrics and information rates

The choice of performance metric for BCJR inference depends crucially on how the outputs will be used. Different decoding methods for the outer code lead to different achievable rates. Any rate loss due to inner MR codes is included in these computations whereas rate loss due to sequence numbers, which are typically required by outer codes, is neglected.

For general trace reconstruction (or detection before hardinput decoding of an outer code defined over Σ), one typically chooses X to minimize the expected Hamming distance

and the optimal X is given by the symbolwise MAP estimate. Choosing X to minimize the edit distance has also been considered in [28], [33], [34]. For hard-decision decoding of an outer code defined by M symbols, the expected Hamming error rate is likewise minimized by choosing M to be the symbolwise MAP estimate of M.

For soft-decision decoding, the outer decoder uses the posterior marginals, U l (m) Pr(M l = m|Y 1:K ), whose uncertainty is quantified by the average symbolwise entropy

Here, U l is any approximate posterior marginal (e.g., due to channel mismatch or suboptimal processing) satisfying m∈Σ Ûl (m) = 1 for all l. For i.i.d. equiprobable inputs into a rate-R inner code, the quantity (2 -H)R (bits/base) is an overall achievable information rate (AIR) for separate detection and decoding, called the BCJR-once rate [35]- [37]. If a random outer code is used with joint decoding, then the AIR is the mutual information rate 1 N I(M; Y 1:K ) = R L I(M; Y 1:K ) which can be estimated using the BCJR algorithm [38]- [40].

In actual DNA storage systems, the number of traces K will be a random variable that is different for each observed cluster. In that case, a particular AIR for random K is given by averaging that AIR over the distribution of K.

### III. DATASET

The performance comparisons in this paper are based on a new dataset of 269,709 traces of 10,000 uniform random DNA sequences of length 110 that is now publicly available at: https://github.com/microsoft/clustered-nanopore-reads-dataset Our hope is that this dataset will enable further research progress by allowing objective comparisons between the algorithms. DNA sequences were synthesized by Twist Bioscience and amplified using polymerase chain reaction. The amplified products were ligated to Oxford Nanopore Technologies (ONT) sequencing adapters by following the manufacturer's protocol (LQK-LSK 109 kit). Finally, ligated samples were sequenced using ONT MinION. Clusters of noisy reads have been recovered using the algorithm from [41]. The insertion, deletion, and substitution rates for this dataset are roughly p ins = 0.017, p del = 0.02, and p sub = 0.022. Using the dataset for coded TR: The dataset is a collection of (x, y) pairs allowing one to estimate the expected performance of TR algorithms for uniform random DNA sequences. For coded TR, the problem is that one cannot estimate an expectation over codewords because the randomly generated DNA sequences are unlikely to be codewords in the code.

One can estimate the expected performance for a coded system with random scrambling. Assume Σ has an abelian group structure and let the code C ⊆ Σ N be a subset with encoder E : M L → C. Consider estimating a performance measure φ = E[Φ(Y 1:K ; M, Z)] for the scrambled encoder defined by X = E(M) + Z, where Z ∈ Σ N is a uniform random scrambling sequence. Since this induces a uniform distribution on X (see Appendix B for a proof), the dataset can be used to estimate φ. For an x in the dataset, let T (x) denote the set of y traces generated by x. Samples can be drawn as follows:

• Let x be the result of drawing a uniform random DNA sequence from the dataset, m be the result of choosing a uniform random message, and then compute z = x -E(m). • Compute the sample value Φ(y 1:K ; m, z) for K traces sampled randomly from T (x) without replacement.

To summarize, for an encoder E, we estimate the average of Φ over Z. Hence, there is a z that performs this well or better. In some cases, one might also expect the value of Φ to concentrate around its expectation and establishing this (e.g., sufficient conditions) is an interesting open question.

## A. Multi-trace trellis via hidden Markov model

Our discussion of algorithms begins with a brief description of a hidden Markov model (HMM) associated with the problem. The state diagram of this HMM implies a natural multi-trace IDS trellis that is different from previous methods [21]- [23]. This trellis has significantly fewer edges and this reduces the complexity of BCJR inference. However, the resulting trellis and BCJR definitions are a bit different from those typically used in coding theory. We refer the reader to Appendix C for a detailed description of trellis and BCJR inference.

In essence, our construction of the trellis describing the joint distribution of (M, X, Y 1 , Y 2 , ..., Y K ) avoids local exponential blow-up in the number of edges by

• modeling insertion events as vertical edges, thereby sequentially accounting for insertions. • modeling events in each trace sequentially. Consider a message sequence M = M 1 M 2 ...M L , where M l ∈ M, which is mapped onto a codeword X = X 1 X 2 ...X N , where X i ∈ X , using a (possibly time-varying) deterministic FSM encoder. Such an encoder takes as input a message symbol M i , transitions to state Q i and emits u codeword symbols X u(i-1)+1 X u(i-1)+1 ...X ui . The transition and codeword symbols emitted only depend on M i and its state Q i-1 before accepting input symbol M i . For simplicity, assume that the number of emitted symbols u is fixed for all i (N = Lu); our trellis can also account for cases where u varies with i.

Suppose we observe K independent traces y 1 , ..., y K generated from X. Let

The trellis is a directed acyclic graph (DAG) with weighted edges where the vertices are ordered by "stages" -edges connect two vertices in the same stage or connect a vertex at stage t to a vertex at stage t + 1. We note that generalizes the standard notion of a trellis by allowing edges between vertices in the same stage. At stage t, vertex v t is defined by (q t , p Therefore, v t ∈ Q × P 1 t × P 2 t ... × P K t × M t × X t , where × denotes the Cartesian product. For clarity, we construct the trellis stage-by-stage, describing the stages corresponding to the first message symbol. Modeling the input. An edge connects vertex v 1 = (q init , 1, 1, ..., 1, , ) at stage 1 to v 2 = (q, 1, 1, ..., 1, m, x) at stage 2, where q init is the initial state of the encoder and encoder makes the transition q init → q when presented with input m, emitting first codeword symbol x. The edge weight is equal to Pr(M i = m) to model the input distribution. Modeling IDS events. An edge connects a vertex v 2 = (q, p 1 , p 2 , ..., p K , m, x) to v 3 = (q, p 1 , p 2 , ..., p K , m, x) with a weight equal to p del modeling a deletion event in the first trace. An edge connects a vertex v 2 = (q, p 1 , p 2 , ..., p K , m, x) to v 3 = (q, p 1 + 1, p 2 , ..., p K , m, x) with a weight equal to p cor if y 1 p 1 = x and p sub |X |-1 otherwise. This models a substitution/correct event in the first trace. An edge connects a vertex v 2 = (q, p 1 , p 2 , ..., p K , m, x) to v 2 = (q, p 1 + 1, p 2 , ..., p K , m, x) in the same stage with a weight equal to pins |X | , modeling an insertion event in the first trace. Notice how only the output pointer to the first trace changes in all cases. We construct K such stages for K traces. Updating on-deck codeword symbol. We have only considered the events corresponding to the first codeword symbol so far. Next, we update the output buffer to replace the first codeword symbol x by the second x , followed by K stages of IDS event modeling for the second codeword symbol.

Transitioning to the next input. The above two steps of modeling the IDS events and updating the output buffer are repeated until all codeword symbols for a given input symbol are processed. Then, the input and output buffer are cleared and the next message symbol is accepted.

The above steps comprise one input cycle. These steps are repeated until all message symbols are exhausted. Each path connecting (q init , 1, 1, ..., 1, , ) at the first stage to (q end , R 1 , R 2 , ..., R K , , ) at the final stage correspond to a message sequence and a sequence of events that resulted in the observed traces Y 1 = y 1 , ..., Y K = y K . The weight of this path is the joint probability of observing the message, the sequence of events and the traces. For this setup, one can use BCJR inference to compute the posterior probability that the true system passed through a given vertex at a particular stage. Then, one can compute Pr(M l = m|Y 1 = y 1 , ..., Y K = y K ) by summing the posterior probabilities of all vertices associated with message symbol m in the input cycle of stage l.

Time Complexity. Assuming the length of the traces R k = O(N ) ∀k, and Q is the state-space of the encoder FSM, the total number of edges in the trellis is O(N K+1 K|Q|), which is the time complexity to exactly compute the APPs. In practice, it is reasonable to assume that the output pointer does not drift too far from the input pointer for each IDS channel, i.e., at a given stage one assumes that |P t | = ∆ < N [21], [22], [28]. Using this assumption, the complexity to compute APPs is roughly O(N K|Q|∆ K ). Note that, for large K, this is significantly smaller compared to the complexity of computing APPs in [23] (which is at least Ω(N K|Q|∆ K u K )).

## B. Trellis BMA

Given the exponential growth of the multi-trace IDS trellis with the number of traces, we next describe a low-complexity heuristic that combines IDS trellises for individual traces to sequentially construct approximate posterior estimates, U = ( U 1 , U 2 , . . . , U L ), for each message symbol. This can be used to construct a hard estimate M = M 1 M 2 ... M L for the message.

a) Initialization: Following the steps outlined in the previous subsection, we first construct K independent trellises: one for each trace y k with k ∈ [K]. Then, we run BCJR inference on each of the K trellises with the corresponding traces as observations and compute F k (v) and B k (v), the forward and backward values of each vertex v in the trellis corresponding to trace k, for all k -these values will be updated using a consensus across traces.

b) Decoding: We now compute U by iterating through the following two steps. Working inductively, we assume that we have already computed U 1 , U 2 ... U l-1 and we would like to compute U l .

• Combining beliefs from each trellis. First, we use the current values of F k (v) and B k (v) to compute a "belief" about symbol M l for each trellis, denoted by V k (M l = m). Recall that each M l is part of the trellis state in some stages (e.g., stages corresponding to input cycle l). Then, pick one of these (e.g., the last stage), call it stage t, and define      Fig. 2: Experimental results on real data. Note that Subfigures 2e and 2f include the rate loss of their MR codes.

where the sum is over stage-t vertices with on-deck message symbol M l = m and β b ≥ 0 reweights the backward values. The channel outputs are conditionally independent given M, so we have

The RHS likelihoods can theoretically be combined to compute the true posterior. However, BCJR inference outputs the marginals and multiplying them only gives the approximation

• Updating the forward values. For trellis k, the idea is to combine information from the other trellises to help maintain the correct synchronization on this trellis. To do this, the forward BCJR values in stage t are updated using the rule

where m(v) is value of M l associated with vertex v and γ k (m) acts as a "new prior" for M l in trellis k due to the other trellises. We also note that the sum m γ k (m) does not affect the answer and, thus, γ k (•) acts as an unnormalized probability.

To define γ k (•), we use the parametrized expression

This is motivated by the idea of extrinsic information processing [42], [43]. The parameter β e ≥ 0 controls the dependence induced between the separate strand detectors, while β i ≥ 0 controls the intrinsic bias in each strand. While β e = 1 is a natural choice, smaller values of β e reduce the dependence between strands and larger values push the γ k (•) distribution towards a hard decision. Similarly, β i = 0 is a natural choice but larger values can sometimes improve performance.

For the posterior estimate of M l given Y 1 , Y 2 , ..., Y K , we define U l (m) c l V (M l = m) βo for some β o > 0 and choose c l so the sum over m equals 1. To lower bound the AIR, we apply the RHS of (2) to U l . Choosing β o < 1 may mitigate overconfidence and increase the AIR lower bound.

Using the updated forward values at input cycle l, we then continue the forward pass to input cycle l + 1 and compute V k (M l = m). Then, this is used to update the forward values for the vertices of input cycle l + 1. This process repeats for the first half of the inputs. c) Estimating each half: Using this updating approach, we sequentially compute the estimates U 1 U 2 ... U L/2 . Analogously, we start from the end of the trellis and update the backward values to compute an estimate U L/2+1 U 2 ... U L which proceeds in the reverse order. For the reverse estimate, (3) should use the first stage with U l in the state.     Fig. 3: Experimental results on simulated data. Note that Subfigures 3e and 3f include the rate loss of their MR codes.

## d) Time Complexity:

The time complexity is K times the complexity of computing APPs using the multi-trace trellis with one trace, which is equal to O(KN |Q|∆).

### V. EXPERIMENTAL RESULTS

In Fig. 2, we provide experimental results, with and without coding, for the algorithm introduced in this paper. We also compare to previous approaches such as "separate decoding" using "multiply posteriors" from [23], BMALA (see Appendix A) from [44, pp. 6-7] [19], and to BCJR on the multi-trace IDS trellis from Section IV-A (see also [23]). Note that BMALA is a TR algorithm and does not give soft output. Hence, the BMALA-HD curve in Fig. 2(d) maps the harddecision symbol error rate into an achievable rate. We note that BMALA-HD beats Trellis BMA for more than 6 traces even though Trellis BMA has a lower error rate. This is because the soft outputs of Trellis BMA are not ideally calibrated. In future work, we will investigate learning-based methods to see if they can generate better calibrated output probabilities.

For coded TR, we use BMALA to give a hard estimate of the DNA sequence and treat this estimate as an observed trace for IDS trellis decoding of the message symbols; we call this BMALA-MAP. We also report the numbers for the multi-trace trellis only for TR with 3 or fewer; other experiments with the multi-trace trellis are computationally infeasible. Training is used to learn the IDS channel (p ins , p del , p sub ), validation is used to tune the hyperparameters (β e , β o , etc.) for Trellis BMA, and the test set is used for the reported results. We remark that multiply posteriors is an instance of Trellis BMA when β b = β o = 1 and β e = β i = 0. Now, wee briefly describe the steps in the Improved BMALA algorithm, which attempts to sequentially estimate each symbol of the DNA sequene X. For each of the traces, it uses a hard estimate of the input pointer and then estimates the next symbol of X using a vote of the current symbols implied by the hard input-pointer estimates. For the traces that do not agree with the plurality, it tries to infer the reason for disagreement (e.g., insertion, deletion, or substitution) by looking ahead a few symbols, and moves the corresponding pointers accordingly. If the algorithm cannot decide on any reason for disagreement, it discards the trace temporarily and attempts to brings it back at a later point in time.

## B. Random scrambling induces uniform distribution

Suppose Σ has an abelian group structure, and let code C ⊆ Σ N . Let C ∼ Uniform(C), Z ∼ Uniform(Σ N ) and X = C + Z, where + is defined as the coordinate-wise application of the group operation. We show here that X is uniformly distributed on Σ N . We do so by proving the following stronger claim

# As a result

Before proving our claim we first define v -1 ∈ Σ N to be the coordinate-wise inverse of v ∈ Σ N . Since Σ has a group structure, v -1 exists and is unique for every v ∈ Σ N . To prove our claim, we observe that

which concludes the proof.

## C. Trellis structure and BCJR inference

In this section, we outline the essential tools used in this work. Crucially, we describe our trellis structure. We remark that our trellis definition differs somewhat from standard definitions used in the coding theory literature. This variation is essential to efficiently represent a larger class of inputoutput distributions, such as the one that describes the IDS channel. In most standard applications, the states in a trellis are organized into distinct stages and edges may only connect states in adjacent stages. While it is possible to represent IDS channels in this fashion, it requires many more edges.

Our trellis is a directed acyclic graph (DAG) that describes the joint distribution for a collection of observed random sequences Y 1 , Y 2 , ..., Y K and a latent or hidden sequence of states. The state sequence is S = (S 1 , S 2 , ..., S L ), where the length L is a random variable satisfying L ≤ c for some constant c. We assume that S 1 alone is known apriori and fixed to be s 0 . The support of each symbol in Y k is a finite set Y. Likewise, the support of S i is a finite set S. Let y k = y k 1 y k 2 ..., y k R k denote the observed realization of Y k , where R k is the length of the k-th observable sequence and s = (s 1 , s 2 , . . . , s l ) denote a possible realization of S. The trellis describes the joint distribution

We now describe essential properties of the trellis DAG, and define some useful notation.

• Vertices: The vertices in the trellis are all possible state realizations. Each vertex is uniquely identified by a state s ∈ S. The trellis has exactly one origin s 0 (state with no in-neighbors) and a set of absorbing states S abs (states with no out-neighbors). • Edges: Suppose edge e connects vertex s to vertex s . Define f from (e) = s as the from vertex of e, f to (e) = s as the to vertex of e. • Edge labels: An edge can either have no label (unlabeled edge), or is labeled by the (trace, symbol) pair (k, j), corresponding to the observation y k j ; this edge is one explanation of the observed symbol y k j . Multiple edges can have the same label. Define f lbl (e) = (k, j) as the label of e. For an unlabeled edge f lbl (e) = φ.

• Edge weights: Every edge in the trellis is weighted. The weight of an unlabeled edge connecting vertices s and s is equal to Pr(s |s). For an edge with label (k, j) that connects the vertices s and s , the edge weight is equal to Pr(Y k j = y k j , s |s). For a vertex which is not an absorbing state, the weights of all its outgoing edges should sum to 1.

• Paths: For an edge path p = e 1 e 2 ...e L , define f from (p) f from (e 1 ) and f to (p) f to (e L ). For the trellis to describe the joint distribution Pr(S = s, Y 1 = y 1 , Y 2 = y 2 , ..., Y K = y K ), the following property needs to be satisfied: consider a path p = e 1 e 2 ...e L where f from (p) is the origin and f to (p) is an absorbing state (for every k, j, there exists exactly one edge e l in every such path such that f lbl (e l ) = (k, j)).

In other words, every path that connects the origin to an absorbing state must explain all the observed symbols exactly once.

Remark. One can verify that the IDS trellis described in section IV-A satisfies the above properties.

The weight w(p) of a path p is defined to be the product of weights of the constituent edges. Each path p = e 1 e 2 ...e L in the trellis connecting the origin to an absorbing state corresponds to a particular sequence of states S = (s 0 , f from (e 2 ), ..., f from (e L ), f to (e L )) with the given observations Y 1 = y 1 , ..., Y K = y K . Moreover, path weight w(p) of a path p = e 1 e 2 ...e L is w(p) = Pr(S = (s 0 , f to (e 1 ), ..., f to (e L ))

= Pr(S = (s 0 , f to (e 1 ), ..., f to (e L ))

where (a) follows since Pr(S 1 = s 0 ) = 1, as S 1 is known and fixed to be s 0 apriori. We next describe the forward-backward algorithm (also called the BCJR algorithm [20]) that computes the probability that the hidden state s was encountered during the output generation process [21]. Abusing notation, we denote this probability by Pr(s ∈ S, Y 1 = y 1 , ..., Y K = y K ) s:∃i∈{1,...,|s|},si=s

where |s| represents the length of s. For marginal inference of the input symbols, it is sufficient to compute Pr(s ∈ S, Y 1 = y 1 , ..., Y K = y K ) for all s ∈ S because the input symbols are deterministic functions of the state.

To compute this quantity, we interpret Pr(s ∈ S, Y 1 = y 1 , ..., Y K = y K ) as the sum of the weights of all paths that start at the origin, end at an absorbing state and pass through state s in the trellis. Then, the derivation of BCJR inference reveals this probability as the product of two terms via the decomposiiton

= p1,p2:

where in (a) we split each path p into two paths such that the first path ends at s and the second originates at s. For each state s ∈ S, we define the forward value to be

and the backward value to be

Together, these imply that

a) Computing the forward values for each state: We now present the dynamic program that computes F (s) for all s. But first some notation: define E in (s) as the set of edges whose tail is s. w(e)F (f from (e)),

where in (a), we split the path p as p e, where f to (e) = s.

To compute the forward values of all vertices, we first compute a topological ordering for the vertices of the trellis. Recall that the trellis is a DAG, so such an ordering always exists (see [45] and references therein). Next we initialize the forward values F (s 0 ) = 1. Since all paths begin there, this is sufficient. Next, we traverse the vertices in order and use the aforementioned sum-product update rule in (5) to compute F (s) for all vertices in the trellis. Since each edge in the trellis is traversed exactly once when computing the forward values, the complexity of computing the forward values is O(E), where E is the number of edges in the trellis. Moreover, a topological ordering (done once offline) can be accomplished by a bread-first search (whose complexity is O(E) as well) starting from the origin state, and hence does not affect the overall complexity of our algorithm.

b) Computing the backward values for each state: We next present the dynamic program that computes B(s) for all s. But first some notation: define E out (s) as the set of edges whose head is s. w(e)B(f to (e)),

where in (a), we split the path p as ep , where f from (e) = s.

To compute the backward values of all vertices, we use the reverse topological ordering for the vertices of the trellis. Next we initialize the backward values of the abosrbing states B(s) = 1 ∀s ∈ S abs . The complexity of computing the backward values is also O(E), since each edge is traversed exactly once. c) Output stage: Recall that in the IDS trellis, the states (vertices) are of the form (q t , p 1 t , p 2 t , ..., p K t , m t , x t ) where t designates the stage, q t is the state of the encoder, p k t are the pointer values, m t is the message symbol and x t is the codeword symbol. Therefore, the message symbol is itself a part of the state. To compute the posterior distribution of the i-th message symbol M i , we first compute Pr(s ∈ S, Y 1 = y 1 , ..., Y K = y K ) for all vertices s in the trellis.

Recall that there are multiple stages in the trellis for each input (e.g., the input stage and the stages associated with the outputs for each of the K traces). To compute the output, we focus on the last stage in the trellis associated with input i which is right before transitioning to message i+1. This stage has no intra-stage edges. For each m ∈ M, we define S m to be the subset of states in this stage associated with M i = m and compute

where c i is chosen so that m∈M V (M i = m) = 1. Then, V (M i = m) = Pr(M i = m|Y 1 = y 1 , ..., Y K = y K ).

d) Complexity analysis: The forward and backward passes traverse the trellis edges exactly once. Moreover, finding a topological order for the trellis vertices is O(E) and this is done once offline. The number of vertices is at most twice the number of edges. The time complexity of forwardbackward algorithm is O(E).

## D. Convolutional codes (CC) vs. Marker repeat (MR) codes

In Fig. 4 and Fig. 5, we compare the relative performance of CC and MR for a few different coding rates using the dataset and approach from Section III. The idea is to investigate which choice of code is appropriate given a fixed inner coding rate. For illustration purposes, we fix the number of observed traces to 2 and use the following set of β values to decode via Trellis BMA -β b = 1, β e = 0.1, β i = 0, β o = 1.0. We observed similar performance with other sets of β values and we strongly suspect that the relative performance of CC and MR codes is insensitive to the particular choice of βs.

The following plots illustrate that MR codes clearly outperform CC when the inner coding rate is 0.9 or more. For lower rates of inner codes, the MR codes are only marginally worse than CC. Moreover, the time taken to decode with MR codes is also lower, since the IDS trellis constructed with CC has a larger state-space.

## E. Visual example of an IDS trellis

Please see Fig. 6 for an example visualization of the IDS trellis. edges are drawn as curved lines. The arrows on the directional edges have been removed to declutter the graph and for aesthetics. The first stage models the input and appends the first codeword to the output buffer, next models all possible events with the first codeword symbol in the first trace, then models events in the second trace. Next, it replaces the codeword symbol in the output buffer and models the IDS events with the second codeword symbol in the two traces. Finally it models the IDS events with the third codeword symbol in the two traces before transitioning to the next input symbol.

### ACKNOWLEDGMENT

We thank Karin Strauss, Yuan-Jyue Chen, and the Molecular Information Systems Laboratory (MISL) for providing the DNA dataset released with this paper and useful discussions on this topic.

## A. BMALA for IDS channel

Consider the DNA storage architecture, shown in Figure 1 and described in [7]. Ignoring the outer code, this scheme uses an identity map to encode the message sequence into a DNA sequence. For the decoder, it uses the Improved BMALA TR algorithm to estimate the DNA sequence.  

