# Introduction

While there is still considerable controversy over the root causes of the Financial Crisis of 2007-2009, there is little dispute that regulators, policymakers, and the financial industry did not have ready access to information with which early warning signals could have been generated. For example, prior to the Dodd Frank Act of 2010, even systemically important financial institutions such as AIG and Lehman Brothers were not obligated to report their amount of financial leverage, asset illiquidity, counterparty risk exposures, market share, and other critical risk data to any regulatory agency. If aggregated over the entire financial industry, such data could have played a critical role in providing regulators and investors with advance notice of AIG's unusually concentrated position in credit default swaps, as well as the exposure of money market funds to Lehman bonds. Of course, such information is currently considered proprietary and highly confidential, and releasing it into the public domain would clearly disadvantage certain companies and benefit their competitors. But without this information, regulators and investors cannot react in a timely and measured fashion to growing threats to financial stability, thereby assuring their realization.

At the heart of this vexing challenge is privacy. Unlike other industries in which intellectual property is protected by patents, the financial industry consists primarily of "business processes" that the U.S. Patent Office deems unpatentable, at least until recently [1]. Therefore, trade secrecy has become the preferred method by which financial institutions protect the vast majority of their intellectual property, hence their need to limit disclosure of their business processes, methods, and data. Forcing a financial institution to publicly disclose its proprietary information-and without the quid pro quo of 17-year exclusivity that a patent affords-will obviously discourage innovation, which benefits no one. Accordingly, government policy has tread carefully on the financial industry's disclosure requirements.

In this paper, we propose a new approach to financial systemic risk management and monitoring via cryptographic computational methods in which the two seemingly irreconcilable objectives of protecting trade secrets and providing the public with systemic risk transparency can be achieved simultaneously. To accomplish these goals, we develop self-regulated protocols for securely computing aggregate risk measures. The protocols are constructed using secure multi-party computation tools [2,3,4,5,6,7], specifically using secret sharing [8]. It is known from [6,2] that general Boolean functions can be securely computed using "circuit evaluation protocols". Since computing any function on real-valued data is approximated arbitrarily well by computing a function on quantized (or binary) data, such an approach can theoretically be used. However, for arbitrary functions and high precision, the resulting protocols may be computationally too demanding and therefore impractical. We show in this paper that for computing aggregate risk measures based on standard sample moments such as means, variances, and covariances-the typical inputs for financial risk measures-simple and efficient protocols can be achieved using secret-sharing over large finite fields or directly over the reals.

With the resulting measures, it is possible to compute the aggregate risk exposures of a group of financial institutions-for example, a concentration (or "Herfindahl") index of the credit default swaps market, the aggregate leverage of the hedge-fund industry, or the margin-to-equity ratio of all futures brokers-without jeopardizing the privacy of any individual institution. More importantly, these measures will enable regulators and the public to accurately measure and monitor the amount of risk in the financial system while preserving the intellectual property and privacy of individual financial institutions.

Privacy-preserving risk measures may also facilitate the ability of the financial industry to regulate itself more effectively. Despite the long history of "self-regulatory organizations" (SROs) in financial services, the efficacy of self regulation has been sorely tested by the recent financial crisis. However, SROs may be considerably more effective if they had access to timely and accurate information about systemic risk that did not place any single stakeholder at a competitive disadvantage. Also, the broad dissemination of privacy-preserving systemic risk measures will enable the public to respond appropriately as well, reducing general risk-taking activity as the threat of losses looms larger due to increasing systemic exposures. Truly sustainable financial stability is more likely to be achieved by such self-correcting feedback loops than by any set of regulatory measures.

# Secure Protocols

Many important statistical measures such as, mean, standard deviation, concentration ratios, pairwise correlations can be obtained by taking summations and inner products on the data. Therefore, we present secure protocols for these two specific functions.

We start with a basic protocol to securely compute the sum of m secret numbers. This protocol result from an application of secret-sharing [8] and basic probability results. We assume that each number belongs to a known range, which we pick to be [0, 1] for simplicity. Recall that the operation a modulo m (written a mod m) produces the unique number a+km ∈ [0, m)

where k is an integer, e.g., 3.6 mod 2 = 1.6.

# Secure-Sum Protocol

For i = 1, . . . , m, each party i possesses the secret number x i ∈ [0, 1] as an input, and the output to each party is s = m i=1 x i (where the addition is over the reals). The protocol is as follows:

1. Each pair of parties exchange privately random numbers. Namely, for all i, j with i = j, party i provides to party j a random number R ij drawn uniformly at random in [0, m].

2. For each i, party i adds to its secret number the random numbers it has received from other parties and subtracts the random numbers it has provided to other parties. More formally, party i computes S i = x i + j∈{1,...,m} j =i R ji -j∈{1,...,m} j =i R ij mod m. Each party publicly reveals S i . In the second round, party i adds to its secret number the elements of the i-th column and subtract the elements of the i-th row (using modulo 3 arithmetic). Each party publishes the result S i :

Finally, the parties add these numbers (modulo 3) and compute the output sum: s = 3.6 mod 3 = 0.6.

Protocol correctness and secrecy. If the parties follow the protocol correctly, it is easy to check that the correct sum is always obtained, since each element R ij is added and subtracted once in S. In addition, we show that this protocol reveals nothing else about the secret numbers than their sum, even if the parties attempt to infer more from the exchanged data. For example, Party 1 may try to learn more about other parties' secret numbers by using the information gathered in S 1 , S 2 , S 3 . We state informally the secrecy guarantee in the following theorem and provide Figure 1: Each point in the plot is a realization of (S 1 , S 2 , S 3 ) (step 2 in the secure-sum protocol) for a drawing of the matrix R, keeping x 1 = 0.1, x 2 = 0.2 and x 3 = 0.3 fixed. As illustrated by the plot, the set of points (s 1 , s 2 , s 3 ) for which s 1 + s 2 + s 3 mod 3 = 0.6 is uniformly covered, suggesting that the S i 's do not carry any other information about the x i 's than their sum. m privately known real numbers and does not reveal any additional information about the individual numbers.

To compute securely the inner-product of two real vectors, a slightly more sophisticated protocol is developed, using secret-sharing (6), as employed in the protocols of (2,3). The obtained protocol, named secure-inner-product, is described in details in the appendix. We state here the security guarantee.

Theorem 2. The secure-inner-product protocol is a self-regulated protocol which outputs the inner-product of two privately own real vectors and does not reveal any additional information about the individual vectors.

Previous theorems hold provided that the parties follow the protocol requirements. Extensions to malicious parties or other type of functions can be considered but are not discussed here.

# 8

Figure 1: Each point in the plot is a realization of (S 1 , S 2 , S 3 ) (step 2 in the Secure-Sum protocol) for a drawing of the matrix R, keeping x 1 = 0.1, x 2 = 0.2 and x 3 = 0.3 fixed. As illustrated by the plot, the set of points (s 1 , s 2 , s 3 ) for which s 1 +s 2 +s 3 mod 3 = 0.6 is uniformly covered, suggesting that the S i 's do not carry any other information about the x i 's than their sum. a formal statement and proof in the appendix. We first illustrate a weaker fact here by plotting the values of S 1 , S 2 , S 3 for several realizations of the random numbers R ij , while keeping fixed x 1 = 0.1, x 2 = 0.2 and x 3 = 0.3. As shown in Figure 1, the realizations of (S 1 , S 2 , S 3 ) uniformly cover the set of points (s 1 , s 2 , s 3 ) for which s 1 +s 2 +s 3 mod 3 = 0.6, suggesting that there is no relevant information in the S i 's other than their sum.

The following is obtained assuming that parties follow the protocol requirements without deviating from it.

Theorem 1. The Secure-Sum protocol outputs the sum of m privately owned real numbers and does not reveal any additional information about the individual numbers.

This theorem follows directly from secret-sharing [8] and basic probability results. For convenience, we provide a proof in the Appendix.

# Secure-Inner-Product Protocol

To compute securely the inner product of two real vectors, slightly more sophisticated protocols are developed and presented in the appendix, using basic secret sharing [8], secret-sharing as employed in [7,3,4], and Oblivious Transfer [9,10]. The variants include information-theoretic and cryptographic protocols on quantized or real data, and have different attributes discussed in the appendix. We state here an informal result regarding one of these protocols which we call Secure-Inner-Product protocol 1.

Theorem 2. The Secure-Inner-Product protocol 1 outputs the sum of two privately owned quantized vectors and does not reveal any additional information about the individual vectors.

Note that the previous two theorems hold provided that the parties follow the protocol requirements (without colluding or cheating). Extensions to malicious parties or other type of functions can also be developed but are not discussed here.

# Illustrative Example

To illustrate the practical implementation of privacy-preserving measures, we provide a simple numerical example using publicly available quarterly data from June 1986 to December 2010 (released in arrears by the U.S. Federal Reserve) on the total amount of outstanding loans linked to real estate issued by three major bank holding companies: Bank of America, JPMorgan, and Wells Fargo [11]. Suppose that the aggregate value of these loans across the three banks is the risk exposure of interest, and the magnitude of outstanding loans for each bank is the proprietary data to be kept private. The historical time series of these data are displayed in Figure 2(a); the bar graph in blue is the aggregate risk exposure to be computed and the three line graphs are the proprietary inputs.

The desired result can be obtained with an application of the Secure-Sum protocol described above [12], which consists of two steps. In the first step, each institution produces two random numbers to be shared, one for each of the other two participating institutions. These numbers are shown in line graphs of Figure 2 In the second step of the Secure-Sum protocol, each institution uses its private data, the two numbers it receives from the other two participating banks, as well as the two numbers it sends to the other two institutions to produce a single value, which we refer to as the privacypreserving measure of its private data. This value will be revealed to the other two institutions.

While these privacy-preserving measures, shown in Figure 2(c), seem like a pure noise, they have just enough of the original data so that the sum of these three numbers under modulo arithmetic yields the correct sum of the original inputs. The key here is that the randomness produced in the first step, as shown in Figure 2(b), exactly cancels in the second step due to the way that the protocol in constructed. It is apparent that the aggregate loans outstanding in Figure 2(c) is identical to the corresponding graph in Figure 2(a), but the former graph has been computed using only the privacy-preserving measures of Figure 2(c).

Despite the fact that the underlying data used in this example is not confidential, even in this simple illustrative case privacy-preserving measures may still prove useful in providing financial institutions and regulators with an incentive to release the data without a lag. More timely releases would obviously benefit all stakeholders by allowing them to respond more nimbly to changing market conditions, but such releases could also disadvantage certain parties in favor of others if privacy were not assured. Moreover, this example underscores the simplicity with which more sensitive data such as leverage ratios, positions in illiquid assets, and off-balancesheet derivatives holdings can be shared regularly, securely, and in a timely fashion.

We consider only three institutions in this example because it is the simplest non-trivial case in which privacy-preserving measures of aggregate sums can be constructed. Clearly, the protocol is applicable for any number of participants greater than two, and implementation for even several thousand participants is extremely fast. More complex risk exposures such as Herfindahl concentration indices require two applications of the Secure-Sum protocol, but the computational burdens are still quite modest. The Secure-Inner-Product protocol can be used to construct multi-point statistical measures such as average correlations between changes in securities holdings or leverage across industry participants.

# Discussion

By construction, privacy-preserving measures of financial risk exposures cannot be "reverseengineered" to yield information about the individual constituents. Accordingly, there is no guarantee that the individual inputs are truthful. In this respect, the potential for misreporting and fraud are no different for these measures than they are for current reporting obligations by financial institutions to their regulators, and existing mechanisms for ensuring compliancerandom periodic examinations and severe criminal and civil penalties for misleading disclosuresmust be applied here as well.

However, unlike traditional regulatory disclosures, privacy-preserving measures will provide its users with a strong incentive to be truthful because the mathematical guarantee of privacy eliminates the primary motivation for obfuscation. Since each institution's proprietary information remains private even after disclosure, dishonesty yields no discernible benefits but could have tremendous reputational costs, and this asymmetric payoff provides significantly greater economic incentive for compliance. Moreover, accurate and timely measures of systemwide risk exposures can benefit the entire industry in allowing institutions and investors to engage in self-correcting behavior that can reduce the likelihood of systemic shocks. For example, if all stakeholders were able to monitor the aggregate amount of leverage in the financial system at all times, there is a greater chance that market participants would become more wary and less aggressive as they observe leverage rising beyond prudent levels. A related issue is whether participation in privacy-preserving disclosures of financial risk exposures is voluntary or mandated by regulation. Given the extremely low cost/benefit ratio of such disclosures, there is reason to believe that the financial industry may well adopt such disclosures voluntarily. A case in point is Markit, a successful industry consortium of dealers of credit default swaps (CDS) that emerged in 2001 to pool confidential pricing data on individual CDS transactions and make the anonymized data available to each other and the public so as to promote transparency and liquidity in this market [13]. According to Markit's website, the data of its consortium members are ". . .provided on equal terms to whoever wanted to use it, with the same data released to all customers at the same time, giving both the sell-side and buy-side access to exactly the same daily valuation and risk management information". From this carefully crafted statement, it is clear that equitable and easy access to data is of paramount importance in structuring this popular data-sharing consortium. Privacy-preserving methods of sharing information could greatly enhance the efficacy and popularity of such cooperatives.

The same motivation applies to the sharing of aggregate financial risk exposures, but with even greater stakes as the recent financial crisis has demonstrated. Once a privacy-preserving system-risk-exposures consortium is established, the benefits will so clearly dominate the nominal costs of participation that it should gain widespread acceptance and adoption in short order. Indeed, participation in such a consortium may serve as a visible commitment to industry best practices that yields tangible benefits for business development, leading to a "virtuous cycle" of privacy-preserving risk disclosure throughout the financial industry

# Conclusion

Privacy-preserving measures of financial risk exposures solve the challenge of measuring aggregate risk among multiple financial institutions without encroaching on the privacy of any individual institution. Previous approaches to addressing this challenge require trusted third parties, i.e., regulators, to collect, archive, and properly assess systemic risk. Apart from the burden this places on government oversight, such an approach is also highly inefficient, requiring properly targeted and perfectly timed regulatory intervention among an increasingly complex and dynamic financial system. Privacy-preserving measures can promote more efficient "crowdsourced" responses to emerging threats to systemic stability, enabling both regulators and market participants to accurately monitor systemic risks in a timely and coordinated fashion, creating a more responsive negative-feedback loop for stabilizing the financial system. This feature may be especially valuable for promoting international coordination among multiple regulatory jurisdictions. While a certain degree of regulatory competition is unavoidable given the competitive nature of sovereign governments, privacy-preserving measures do eliminate a significant political obstacle to regulatory collaboration across national boundaries.

# Privacy-preserving risk measures have several other financial and non-financial applications.

Investors such as endowments, foundations, pension and sovereign wealth funds can use these measures to ensure that their investments in various proprietary vehicles-hedge funds, private equity, and other private partnerships-are sufficiently diversified and not overly concentrated in a small number of risk factors. Financial auditors charged with the task of valuing illiquid assets at a given financial institution can use these measures to compare and contrast their valuations with the industry average and the dispersion of valuations across multiple institutions. Realtime indexes of the aggregate amount of hedging activity in systemically important markets like the S&P 500 futures contract may be constructed, which could have served as an early warning signal for the "Flash Crash" of May 6, 2010.

More broadly, privacy-preserving measures of risk exposures may be useful in other industries in which aggregate risks are created by individual institutions and where maintaining privacy in computing such risks is important for promoting transparency and innovation, such as healthcare, epidemiology, and agribusiness. 

# Sum Protocols and Theorems

For convenience, we restate the Secure-Sum protocol.

Secure-Sum Protocol.

Inputs: for i = 1, . . . , m, party i possesses the secret number x i ∈ [0, 1].

Output: each party obtains s = m i=1 x i (where the addition is over the reals). Protocol:

1. Each pair of parties exchange privately random numbers. Namely, for all i, j with i = j, party i provides to party j a random number R ij drawn uniformly at random in [0, m].

2. For each i, party i adds to its secret number the random numbers it has received from other parties and subtract the random numbers it has provided to other parties. In formula, party i computes S i = x i + j∈{1,...,m} j =i R ji -j∈{1,...,m} j =i R ij mod m. Each party publicly reveals S i .

# Each party computes S = m

i=1 S i mod m, which equals s = m i=1 x i .

One can define other variants and extensions of this protocol, in which fewer random numbers are exchanged to minimize information flow, or in which more information is exchanged to check the correctness of parties computations (one may also use virtual parties for that).

Theorem 3. Let x 1 , . . . , x m be m privately owned real numbers. Let i ∈ {1, . . . , m} and View i denote the view of party i obtained from the Secure-Sum protocol with inputs x 1 , . . . , x m . The protocol outputs the sum s = m i=1 x i and the distribution of View i depends on x 1 , . . . , x m only through s and x i .

We provide first the proof argument for m = 3. Assume that party 1 collects all the data it possesses and received from other parties to try to learn something about their secret numbers.

That is, party 1 possesses its secret number x 1 , the numbers R 12 , R 13 , R 21 , R 31 exchanged in step 1, the numbers S 1 , S 2 , S 3 revealed in step 2 and the output sum s (whose information is already contained in the S i 's). From these, party 1 can subtract in S 2 , S 3 the terms depending on R 12 , R 13 , R 21 , R 31 and obtain the right-hand side of

(1)

and this is all the information party 1 can gather about other parties secret numbers. Adding Proof of Theorem 3. All the arithmetic in this proof is modulo m. We first check that the protocol computes indeed the sum. We set R ii = 0 for all i, to simply notations. This is straightfor-

Let View 1 be the protocol view of party 1, i.e.,

Party 1 can subtract the R ij 's it has access to in the S i 's, obtaining View 1 as a sufficient statistic for View 1 , where

and

, where R i contains all the R ji for which j = i (in increasing order). Note that Z and W are a random vectors of dimension respectively (m -1) × 1 and m(m -1) × 1. We then have that

where A is the (m -1) × m(m -1) matrix whose i-th row is filled with 0's except at columns

where it is 1, and Π is a permutation matrix. Note that the rank of A and the rank of

where

Therefore, for any z, d ∈ Σ m-1 , there exists w such that M w = d and

where the second equality uses the fact that W and Ww are both i.i.d. uniform over [0, m].

Therefore, the distribution of View 1 , and hence of View 1 , depends only on m i=2 x i = sx 1 and x 1 . By symmetry, the analogue conclusion holds for any parties, which concludes the proof of the theorem.

# Inner-Product Protocols and Theorems

We now present secure protocols to compute the sample correlation, or equivalently the inner product, between two real vectors. Recall that the sample correlation of two vectors x = {x i } t i=1 and y = {y i } t i=1 is given by

Definition 1. We denote by Z q the set {0, 1, . . . , q -1}, and by F q the same set equipped with the Galois field operations when q is a power of a prime. We define by Σ k (x, F q ) the sets of k-tuples in F q which add up to x, i.e.,

We may call the y i 's to be shares of x.

Secure-Inner-Product Protocol 1.

Common inputs: q ∈ Z + (the quantization level), n ∈ Z + (the vector dimensions) and p a prime larger than q 2 n.

Party 2 inputs: y 1 , . . . , y n ∈ Z q .

Party 3 inputs: none.

1. For i = 1, . . . , n, party 1 splits x i in three shares x i (1), x i (2) and x i (3) uniformly drawn in Σ 3 (x i , F p ) := {(a, b, c) ∈ F 3 p : a + b + c mod p = x i } and party 2 splits y i in three shares y i (1), y i (2) and y i (3) uniformly drawn in Σ 3 (y i , F p ). Party 1 provides privately to party 2 the shares x i (1), x i (2) and privately to party 3 the share x i (3). Party 2 provides privately to party 1 the shares y i (1), y i (2) and privately to party 3 the share y i (3).  

# Party 1 sets p

x n ] and y = [y 1 , . . . , y n ] be two privately owned vectors on F n q . Let View 1 denote the view of party 1 obtained from the Secure-Inner-Product protocol 1 with inputs x, y. The protocol outputs the inner product ρ = n i=1 x i y i and the distribution of View 1 depends on x, y only through ρ and x. The reciprocal result holds for party 2.

Proof of Theorem 4. The arithmetic is on F p in the following. We first check that the protocol computes indeed the inner product. For every i = 1, . . . , n, p i (1)

x i y i .

Let View 1 be the protocol view of party 1, which is a function of

where y(1) contains all components y i (1) for i = 1, . . . , n and similarly for the y(2). Note that for i = 1, . . . , n, (p i (1), p i (2), p i (3)) are independent and uniformly drawn in Σ 3 (p i , F p ), where 1. For i = 1, . . . , n, (a) party 1 splits x i in three shares by evaluating a random polynomial t → X i (t) at (t 1 , t 2 , t 3 ) = (1/4, 1/2, 3/4), where X i (t) = x i + a i t mod τ and where a i is uniformly drawn in [0, τ ]. Party 1 reveals X i (t j ) to party j for j = 2, 3, (b) party 2 splits y i in three shares Y i (t j ) = y i + b i t j mod τ , for j = 1, 2, 3, where b i is uniformly drawn in [0, τ ], and reveals Y i (t j ) to party j for j = 1, 3.

2. For j = 1, 2, 3, (a) party j computes P (t j ) = t i=1 X i (t j )Y i (t j ) mod τ , (b) party j draws α j , β j independently and uniformly at random in [0, τ ] and for k = 1, 2, 3, sets Z j (t k ) = α j t k + β j t 2 k mod τ and shares Z j (t k ) with party k, (c) ρ(t j ) = P (t j ) + 3 k=1 Z k (t j ) mod τ is made available to parties 1 and 2.

3. Party 1 and 2 compute ρ(0) by interpolating a degree 2 polynomial on ρ(t j ), j = 1, 2, 3, obtaining ρ(0) = n i=1 x i y i . We omit the proof of this theorem to conserve space since it does not concern the main scope of the paper. We refer to Theorem 4 for a proof of a Secure Inner-Product protocol, which can be used on real data via quantization.

We provide a third protocol to compute securely the inner-product function without using a third dummy party but ensuring only cryptographic security. This protocol uses the Oblivious Transfer (OT) protocol, developed by [9,10], which is an important protocol for multi-party computations as it allows to compute in particular secret shares of the product x • y of two bits x and y, and can then be used in the computation of more general circuit computations. The basic OT protocol allows a sender to transfer one of potentially many bits to a receiver; however, the sender remains oblivious as to what bit the receiver wants and the receiver remains oblivious about any other bits than the one he has requested. In other words, the functionality in the OT protocol takes the bits (b 1 , . . . , b k ) as inputs for the first party and the index i for the second party, and produces as output nothing for the first party and the bit b i requested by the second party. Formally,

where λ denotes the no information symbol. We now describe OT 2 1 .

OT 2 1 protocol

Sender inputs: (b 0 , b 1 ) ∈ {0, 1} 2 and a private key (n, d).

Receiver inputs: i ∈ {0, 1} and a public key (n, e).

Algorithm:

1. The sender generates two random numbers x 0 , x 1 and transmit them to the receiver.

2. The receiver generates a random number k, encrypts it with the public key and scrambles the outcome with x i to produce c = (x i + k e ) mod n 3. The sender decrypts the two numbers (cx 0 ) and (cx 1 ) to get k 0 and k 1 respectively (i.e., it computes k j = (cx j ) d mod n for j = 0, 1). Note that either k 0 or k 1 is equal to k, but these are equally likely for the sender, and reciprocally, k i⊕1 is not accessible to the receiver. The sender then transmits a 0 = b 0 + k 0 and a 1 = b 1 + k 1 .

# The receiver finds b

The OT k 1 protocol is easily obtained by extending previous protocol to multiple sender bits, ad similarly, one can extend the protocol to non binary fields.

We now present a cryptographic protocol for the inner product.

Secure-Inner-Product Protocol 3.

Common inputs: q (the quantization level), n (the vector dimensions). Party 1 inputs: x 1 , . . . , x n ∈ Z q . Party 2 inputs: y 1 , . . . , y n ∈ Z q .

1. For i = 1, . . . , n, (a) party 1 picks x i (2) uniformly at random in Z nq 2 and reveals it to party 2, who picks y i (1) uniformly at random in Z nq 2 and reveals it to party 1.

(b) party 1 picks a i (1) uniformly at random in Z nq 2 and sends {-a i (1), -a i (1)+x i (1), -a i (1)+2x i (1), -a i (1)+3x i (1), . . . , -a i (1)+(nq 2 -1)x i (1)} (all operations mod nq 2 ) with OT nq 2 1 to party 2 who picks the y i (2)-th element.

(c) party 2 picks b i (2) uniformly at random in Z nq 2 and sends

to party 1 who picks the y i (1)-th element.

(d) party 1 computes p i (1) = x i (1)y i (1) + a i (1) + b i (1) mod nq 2 and party computes

Note that these are shares of the product x i y i .

2. Party 1 computes ρ(1) = n i=1 p i (1) mod nq 2 and reveals it to party 2, who computes ρ(2) = n i=1 p i (2) mod nq 2 and reveals it to party 1.

# Each party computes

From the protocol construction, we have the following result.

Lemma 1. Secure-Inner-Product protocol 3 privately reduces the correlation computation to the OT protocol.

The notion of being "privately reducible" is formally defined in Section 2.2. of [15]. From the composition theorem for the semi-honest setting in Section 2.2. of [15], one obtains as a consequence of the previous lemma that Secure-Inner-Product protocol 3 privately computes k-bit mult.

k-bit mult.

k-bit mult.

k-bit mult.

k-bit mult.

k-bit mult.

k-bit mult.

# multioperand adder

Sunday, October 2, 2011 2. Party 1 computes ρ(1) = t i=1 pi(1) mod qt 2 and reveals it to party 2, who computes ρ(1) = t i=1 pi(1) mod qt 2 and reveals it to party 1.

3. Each party computes ρ(1) + ρ(2) mod qt 2 , obtaining the correlation.

This protocol requires O(tq 2 ) OT protocols. This means a possibly high number of public and private encryptions/decryptions (e.g., with RSA). One can use (9) to improve the OT protocols running time. the inner product provided the existence of trapdoor one-way permutations. In particular, using RSA for the encryptions in OT, the protocol is secure provided that RSA cannot be broken. This protocol requires O(nq 2 ) OT protocols but only three communication rounds. This still means a possibly high number of public and private encryptions/decryptions (e.g., with RSA). One may use [16] to improve the OT protocols running time. Another approach consist in using a Boolean circuit for correlations as in Figure 3, using OT protocols to compute shares of the multiplication gates (and simply adding shares for the XOR gates). Such an approach, as developed in [2], or related approaches as in [6,5], may be particularly useful for other functions such as for the quantile function, which does not have the arithmetic structure of the summation or inner-product functions. In particular, [6,5] provide protocols with constant communication rounds which may matter for practical considerations, although for real data problems, the practicality of such algorithms need to be further investigated.

# Related literature on MPCs Theory

The problem of secure multi-party computation emerged with the work of Yao [6] in 1982, and with the work of Goldreich, Micali and Wigderson [2] in 1987. It is shown in [6] that any Boolean functionality can be computed without requiring an external trusted party for two parties, and [2] provides protocols for arbitrarily many parties. Since these papers, many have proposed variations of MPC settings, allowing different kinds of adversarial parties, security, and efficiency attributes. In particular, [5] introduces cryptographic protocols with bounded circuit depths (requiring finitely many communication rounds) and [7,3,4] develop informationtheoretic protocols. Homomorphic encryption has also been shown to provide another approach to secure multi-party computations [17,18], and more recently, Gentry [19] showed that fully homomorphic encryption schemes can be constructed, allowing addition and multiplication to be performed on encrypted data without having to decrypt it. This approach leads to MPC protocols that do not have communication rounds increasing with the circuit complexity, although fully homomorphic encryption is still considered impractical. For certain functionality, progress regarding practical fully homomorphic encryption have been achieved in [20] with somewhat fully homomorphic encryptions schemes using the learning-with-errors assumption.

# Applications

The main applications associated with MPCs in the literature include distributed voting [21], private bidding and auctions [22], data mining [23], and sharing of signature [24]. MPCs have been used for the first time in a real-world application only in 2008, when 1,200 farmers in Denmark employed an MPC protocol in a nation-wide auction to determine the market price of sugar-beets contracts without revealing their selling and buying prices [25]. The whole computation took about half an hour, a satisfactory time for this application. In a different context, [26] introduces "Patient Controlled Encryption" scheme, where an electronic health record system allowing searches to be done on encrypted data is developed.

# Appendix

In this appendix, we provide formal theorems and proofs of the security guarantees ensured by the Secure-Sum and three Secure-Inner-Product protocols, assuming semi-honest parties (possibly curious but following the protocol correctly). Extensions to malicious parties can be considered but are not discussed here.

Secure-Inner-Product protocols 1 and 2 use a third dummy party to help with the computations while Secure-Inner-Product protocol 3 does not. The dummy party does not possess inputs or receives meaningful information but simply helps with the computation (note that for the applications in mind, the use of a dummy party does not represent a significant obstacle). Secure-Inner-Product protocols 1 and 3 are defined on quantized data, while Secure-Inner-Product protocol 2 applies directly to real-valued data. Finally, Secure-Inner-Product protocol 1 provides information-theoretic security, Secure-Inner-Product protocol 2 provides 'almost' information-theoretic security (as defined in Theorem 5) and both protocols require only elementary operations at a computational level, while Secure-Inner-Product protocol 3 provides cryptographic security (i.e., it relies on computational-hardness assumptions) and uses OT protocols (hence non-elementary operations such as RSA [14] encryptions and decryptions).

An important benchmark for the practical consideration of secure protocols is the number of communication rounds, which require exchange of data over communications media such as the internet. With a standard internet connection and for arbitrary distances this can take no longer than 2-3 seconds but may also dominate the protocol running time. All protocols proposed here require few communication rounds. The following table summarizes these properties, where n denotes the vector dimension and q the quantization level.

