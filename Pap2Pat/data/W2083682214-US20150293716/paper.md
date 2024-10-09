# I. INTRODUCTION

Coding for rewriting is an important technology for flash memories. It has the potential to substantially increase their longevity, speed and power efficiency. Since its proposition in recent years [6], lots of works have appeared in this area [11]. The most basic model for rewriting is a write-once memory (WOM) model [8], where a set of binary cells are used to store data, and the cell levels can only increase when the data are rewritten. For flash memories, this constraint implies that the rewriting will delay expensive block erasures, which leads to better preservation of cell quality and higher performance.

There have been many techniques for the design of WOM codes. They include linear codes, tabular codes, codes based on projective geometry, coset coding, etc. [3], [8] Codes with substantially higher rates were discovered in recent years [11]. In 2012, WOM codes that achieve capacity were discovered by Shpilka et al. [9] and Burshtein et al. [2]. The latter code used a very interesting construction based on polar coding. It should be noted that polar coding is now also used to construct rewriting codes for the rank modulation scheme [4].

Compared to the many works on WOM codes, the works on WOM codes that also correct errors have been much more limited. Existing works are mainly on correcting a few errors (e.g., 1, 2, or 3 errors [12], [13]). However, for rewriting to be widely used in flash memories, it is important to design WOM codes that can correct a substantial number of errors.

In this paper, we present a new coding scheme that combines rewriting with error correction. It supports any number of rewrites and can correct a substantial number of errors. The code construction uses polar coding. Our analytical technique is based on the frozen sets corresponding to the WOM channel and the error channel, respectively, including their common degrading and common upgrading channels. We present lower bounds to the sum-rate achieved by our code. The actual sum-rates are further computed for various parameters. The analysis focuses on the binary symmetric channel (BSC). An interesting observation is that in practice, for relatively small error probabilities, the frozen set for BSC is often contained in the frozen set for the WOM channel, which enables our code to have a nested structure. The code can be further extended to multi-level cells (MLC) and more general noise models.

## II. BASIC MODEL

Let there be N = 2 m cells that are used to store data. Every cell has two levels: 0 and 1. It can change only from level 0 to level 1, but not vice versa. That is called a WOM cell [8].

A sequence of t messages M 1 , M 2 , • • • , M t will be written into the WOM cells, and when M i is written, we do not need to remember the value of the previous messages. (Let M j denote the number of bits in the message M j , and let M j ∈ {0, 1} M j .) For simplicity, we assume the cells are all at level 0 before the first write happens.

After cells are programmed, noise will appear in the cell levels. For now, we consider noise to be a BSC with error probability p, denoted by BSC(p). These errors are hard errors, namely, they physically change the cell levels from 0 to 1 or from 1 to 0. For flash memories, such errors can be caused by read/write disturbs, interference and charge leakage, and are quite common.

### A. The model for rewriting

A code for rewriting and error correction consists of t encoding functions

let s i,j ∈ {0, 1} and s i,j ∈ {0, 1} denote the level of the i-th cell right before and after the j-th write, respectively. We require s i,j ≥ s i,j . Let c i,j ∈ {0, 1} denote the level of the i-th cell at any time after the j-th write and before the (j + 1)-th write, when reading of the message M j can happen. The error c i,j ⊕ s i,j ∈ {0, 1} is the error in the i-th cell caused by the noisy channel BSC(p). (Here ⊕ is the XOR function.) For j = 1, 2, • • • , t, the encoding function E j : {0, 1} N × {0, 1} M j → {0, 1} N changes the cell levels from s j = (s 1,j , s 2,j , • • • , s N,j ) to s j = (s 1,j , s 2,j , • • • , s N,j ) given the initial cell state s j and the message to store M j .

(Namely, E j (s j , M j ) = s j .) When the reading of M j happens, the decoding function D j : {0, 1} N → {0, 1} M j recovers the message M j given the noisy cell state c j = (c 1,j , c 2,j , • • • , c N,j ). (Namely, D j (c j ) = M j .)

N is called the rate of the jth write. R sum = ∑ t j=1 R j is called the sum-rate of the code. When there is no noise, the maximum sum-rate of WOM code is known to be log 2 (t + 1); however, for noisy WOM, the maximum sum-rate is still largely unknown [5].

### B. Polar codes

We give a short introduction to polar codes due to its relevance to our code construction. A polar code is a linear block error correcting code proposed by Arıkan [1]. It is the first known code with an explicit construction that provably achieves the channel capacity of symmetric binary-input discrete memoryless channels (B-DMC). The encoder of a polar code transforms

respectively. The channels are polarized such that for large N, the fraction of indices i for which I(W (i) N ) is nearly 1 approaches the capacity of the B-DMC [1], while the values of I(W (i) N ) for the remaining indices i are nearly 0. The latter set of indices are called the frozen set. For error correction, the u i 's with i in the frozen set take fixed values, and the other u i 's are used as information bits. A successive cancellation (SC) decoding algorithm achieves diminishing block error probability as N increases.

Polar code can also be used for optimal lossy source coding [7], which has various applications. In particular, in [2], the idea was used to build capacity achieving WOM codes.

Our code analysis uses the concept of upgrading and degrading channels, defined based on frozen sets. As in [10], a channel W : X → Z is called "degraded with respect to a channel W : X → Y" if a channel equivalent to W can be constructed by concatenating W with an additional channel Q : Y → Z, where the inputs of Q are linked with the outputs of W. That is, W (z|x) = ∑ y∈Y W(y|x)Q(z|y). We denote it by W W. Equivalently, the channel W is called "an upgrade with respect to W ", denoted by W W .

## III. CODE CONSTRUCTION

In this section, we introduce our code construction that combines rewriting with error correction.

A. Basic code construction with a nested structure 1) Basic concepts: First, let us consider a single rewrite step (namely, one of the t writes). Let s = (s 1 ,

the cell levels right before and after this rewrite, respectively. Let g = (g 1 , g 2 , • • • , g n ) be a pseudo-random bit sequence with i.i.d. bits that are uniformly distributed. The value of g is known to both the encoder and the decoder, and g is called a dither.

, 1} be the value of the i-th cell before and after the rewrite, respectively. As in [2], we build the WOM channel in Figure 1 for this rewrite, denoted by WOM(α, ). Here α ∈ [0, 1] and ∈ [0, 1  2 ] are given parameters, with α = 1 ∑ N i=1 s i N representing the fraction of cells at level 0 before the rewrite, and =

representing the fraction of cells that are changed from level 0 to level 1 by the rewrite. Let F WOM(α, ) ⊆ {1, 2, • • • , N} be the frozen set of the polar code corresponding to this channel WOM(α, ). In this subsection, we assume F BSC(p) ⊆ F WOM(α, ) , as illustrated in Figure 2(a). In this case, the code has a nice nested structure: for any message M ∈ {0, 1} M , the set of cell values V M ⊆ {0, 1} N that represent the message M is a linear subspace of a linear error correcting code (ECC) for the noisy channel BSC(p), and {V M |M ∈ {0, 1} M } form a partition of the ECC's codewords. Later we will extend the code to general cases.

stored message all 0s

stored in additional cells 2) The encoder: Let E : {0, 1} N × {0, 1} M → {0, 1} N be the encoder for this rewrite. Namely, given the current cell state s and the message to write M ∈ {0, 1} M , the encoder needs to find a new cell state s = E(s, M) that represents M and is above s (that is, cell levels only increase).

The encoding process is similar to [2], but with some difference in how to assign bits to F WOM(α, ) . For convenience of presentation, here we assume the polar code to be the original code designed by Arıkan [1]; however, note that it can be generalized to other polar codes as well. We present the encoding function in Algorithm 1. Here y and u are two vectors of length N; u F WOM(α, ) -F BSC(p) {u i |i ∈ F WOM(α, ) -F BSC(p) } are all the bits u i in the frozen set F WOM(α, ) but not F BSC(p) ; u F BSC(p) {u i |i ∈ F BSC(p) } are all the bits u i in F BSC(p) ; and

.

(Comment: Here

can be computed recursively using formulae ( 22), (23) in [1]).

3) The decoder: We now present the decoder D :

be the noisy cell levels after the message is written. Given c, the decoder should recover the message as D(c) = M.

Our decoder works essentially the same way as a polar error correcting code. We present it as Algorithm 2.

# Algorithm 2 The decoding function M = D(c)

View c ⊕ g as a noisy codeword, which is the output of a binary symmetric channel BSC(p). Decode c ⊕ g using the decoding algorithm of the polar error-correcting code [1], where the bits in the frozen set

, which denotes the elements of the vector v(G ⊗m 2 ) -1 whose indices are in the set F WOM(α, ) -F BSC(p) .

By [1], it is easy to see that both the encoding and the decoding algorithms have time complexity O(N log N).

4) Nested code for t writes: In the above, we have presented the encoder and the decoder for one rewrite. It can be naturally applied to a t-write error correcting WOM code as follows. For j = 1, 2, • • • , t, for the j-th write, replace α, , s,s ,v,v ,M,M,E,D,c,M, v by α j-1 , j , s j , s j , v j , v j , M j , M j , E j , D j , c j , Mj , vj , respectively, and apply the above encoder and decoder.

Note that when N → ∞, the values of

Optimizing the code means to choose optimal values for 1 , 2 , • • • , t that maximize the sum-rate.

## B. Extended code construction

We have introduced the code for the case F BSC(p) ⊆ F WOM(α, ) so far. Our experiments show that for relatively small p and typical values of (α 0 , 1 ), (α 1 , 2 ), • • • , (α t-1 , t ), the above condition holds. We now consider the general case where F BSC(p) is not necessarily a subset of F WOM(α, ) .

We first revise the encoder in Algorithm 1 as follows. After all the steps in the algorithm, we store the bits in u F BSC(p) -F WOM(α, ) using N additional,j cells (for the j-th write). (It is illustrated in Figure 2(b).) In this paper, for simplicity, we assume the bits in u F BSC(p) -F WOM(α, ) are stored using just an error correcting code designed for the noisy channel BSC(p). (It will not be hard to see that we can also store it using an error-correcting WOM code, such as the one presented above, for higher rates. However, we skip the details for simplicity.) Therefore, we can have

.

We now revise the decoder in Algorithm 2 as follows. First recover the bits in u F BSC(p) -F WOM(α, ) using the decoding algorithm of the ECC for the N additional,j additional cells. Then carry out all the steps in Algorithm 2, except that the bits in F BSC(p) -F WOM(α, ) are known to the decoder as the above recovered values instead of 0s.

## IV. CODE ANALYSIS FOR BSC

In this section, we prove the correctness of the above code construction, and analyze its performance.

### A. Correctness of the code

We first prove the correctness of our code. First, the encoder in Algorithm 1 works similarly to the WOM code encoder in [2], with an exception that the bits in F WOM(α, ) are not all occupied by the message M; instead, the bits in its subset F WOM(α, ) ∩ F BSC(p) are set to be constant values: all 0s. Therefore, it successfully rewrites data in the same way as the code in [2]. Next, the decoder in Algorithm 2 recovers the cell values from noise in the same way as the standard polar ECC. Then, the stored message M is extracted from it.

It is important to note that although physical noise acts on cell levels s = (s 1 , • • • , s N ), the ECC in our construction is actually for cell values v = (s 1 ⊕ g 1 , • • • , s N ⊕ g N ). However, the dither g has independent and uniformly distributed elements; so when the noisy channel for s is BSC(p), the corresponding noisy channel for v is also BSC(p). 3. Degrading the channel WOM(α, * ) to BSC(α * ). The two channels on the left and on the right are equivalent. We have seen that if F BSC(p) ⊆ F WOM(α, ) , the code has an interesting nested structure. In general, it is also interesting to understand how large F WOM(α, ) ∩ F BSC(p) can be. For easy presentation, we consider one rewrite as in Section III-A, where the parameters are α and (instead of α j-1 , j ). Proof: (1) In Figure 3, by setting * = p α , we see that BSC(p) WOM(α, p α ). Therefore F WOM(α, p α ) ⊆ F BSC(p) . (2) In Figure 4, we can see that WOM(α, ) WOM(α, p α ). Therefore, F WOM(α, p α ) ⊆ F WOM(α, ) . (3) In Figure 3, by setting * = , we see that BSC(α ) WOM(α, ). Therefore F WOM(α, ) ⊆ F BSC(α ) .

(4) Since p ≤ α , clearly BSC(α ) BSC(p).

We illustrate the meaning of Lemma 1 in Figure 5.

Fig. 5. The frozen sets for channels BSC(p), WOM(α, ), WOM(α, p ) and BSC(α ). 

) and the number of additional cells we use to store the bits in

.

Therefore, we get the sum-rate R sum Lower Bound to Achievable Sum-rate t Noiseless p = 0.001 p = 0.005 p = 0.010 p = 0.016 Fig. 6. Lower bound to achievable sum-rates given the error probability p. nested code structure. We search for the answer experimentally. Let N = 8192. Let the polar codes be constructed using the method in [10]. To obtain the frozen sets, we let |F WOM(α, ) | = N(α H( ) -∆R), where ∆R = 0.025 is a rate loss we considered for the polar code of the WOM channel [2]; and let F BSC(p) be chosen with the target block error rate 10 -5 .

The results are shown in Figure 7. The four curves correspond to α = 0.4, 0.6, 0.8, and 1.0. The x-axis is , and the y-axis is the maximum value of p we found that satisfies F BSC(p) ⊆ F WOM(α, ) , which, clearly, increases with both α and . And it has nontrivial values (namely, it is comparable to or higher than the typical error probabilities in memories).

### B. Achievable sum-rates

We search for the achievable sum-rates of the general code. Given p, we search for 1 , 2 , • • • , t that maximize the sum-rate R sum . We show the results for t-write errorcorrecting WOM codes-for t = 2, 3, 4, 5-in Figure 8. (In the experiments, we let N = 8192, ∆R = 0.025, and the target block error rate be 10 -5 .) The x-axis is p, and the y-axis is the maximum sum-rate found in our algorithmic search. We see that the achievable sum-rate increases with the number of rewrites t. And we comment that in most cases, the achievable rate of the general code is very close to that of a nested code (which is more restricted). This means the nested code is already performing well for this parameter range.

Note that the lower bound to sum-rate R sum in Figure 6 is actually higher than the rates we have found through experiments by now. This is because the lower bound is for N → ∞, while the codes in our experiments are still short so far and consider the rate loss ∆R. Better rates can be expected as we increase the code length and further improve our search algorithm due to the results indicated by the lower bound.

## ACKNOWLEDGMENT

This work was supported in part by the NSF CAREER Award CCF-0747415, the NSF Grant CCF-1217944, a grant from Intellectual Ventures, the ISF grant 480/08 and BSF grant 2010075. This work was done while Michael Langberg was at the California Institute of Technology.

## V. EXPERIMENTAL RESULTS

In this section, we study the achievable rates of our error correcting WOM code, using polar codes of finite lengths. In the following, we assume the noisy channel is BSC(p), and search for good parameters 1 , 2 , • • • , t that achieve high sum-rate for rewriting. We also study when the code can have a nested structure, which simplifies the code construction.

### A. Finding BSCs satisfying F BSC(p) ⊆ F WOM(α, )

The first question we try to answer is when BSC(p) satisfies the condition F BSC(p) ⊆ F WOM(α, ) , which leads to an elegant

