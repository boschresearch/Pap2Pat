# I. INTRODUCTION

The performance of a wireless communication system can be greatly improved by making the channel state information (CSI) available at the transmitter and the receiver. In a massive multiple-input single-output (MISO) system, having CSI at the transmitter (CSIT) is especially This work was supported in part by the NSF Award ECCS-1611575. This work was presented in part at the IEEE International Symposium on Information Theory (ISIT) in July 2015 [1]. E. Koyuncu is with Department of Electrical and Computer Engineering, University of Illinois at Chicago (e-mail: ekoyuncu@uic.edu). X. Zou and H. Jafarkhani are with Center for Pervasive Communications & Computing, University of California, Irvine (e-mails: xzou4@uci.edu; hamidj@uci.edu). desirable as one can then fully exploit the performance gains promised by the large number of transmit antennas via CSI-adaptive transmission strategies such as beamforming. A typical way to acquire CSIT is channel estimation followed by (digital) feedback.

Channel training/estimation and feedback are traditionally viewed as two non-interleaving processes, as shown in Fig. 1. According to this traditional viewpoint, for each channel state, the transmitter first trains all of its antennas at once, so that the receiver acquires the entire CSI (or, in general, an erroneous version thereof.). This initial training phase is followed by the receiver feeding back a possibly-quantized version of the CSI. The receiver's feedback is then utilized at the transmitter side for data transmission (e.g., as a quantized beamforming vector.).

Designing such limited feedback systems is a fundamental problem of communication theory and has been the subject of many publications [2]. In particular, limited feedback beamforming [3] has been studied through several different approaches that utilize Grassmannian line packings [4], vector quantization [5], combinations with orthogonal [6] or quasi-orthogonal [7] space-time codes, variable-length coding [8], or other systematic constructions [9]. Conditions to achieve full diversity in a finite feedback scheme has been discussed in [10], [11]. Various distributed limited feedback schemes [12]- [16] provide generalizations to multi-user networks. The conventional scheme in Fig. 1 appears to be infeasible in the case of a massive MISO system. Even the channel training/estimation phase, by itself, would be very challenging to realize due to the large number of transmit antennas that need to be trained. Moreover, even if one assumes that the training stage somehow comes with no cost, feeding back the associated large number of channel values to the transmitter appears to be infeasible. Conventional limited feedback schemes also do not provide much hope in this context: The feedback rates required for even the simplest of the limited feedback schemes such as antenna selection grow without bound as the number of transmit antennas grows to infinity. In [17], it is analyzed in detail how many antennas per user terminal are needed to achieve some percentage of the ultimate performance limit with infinitely many antennas.

There has been some work on channel estimation and CSI feedback in massive MIMO systems; a survey can be found in [18]. In particular, [19] proposes a noncoherent trellis-coded quantization scheme, whose encoding complexity scales linearly with the number of antennas.

In [20]- [22], compressive sensing techniques are utilized to reduce the feedback overhead of the CSI estimation. In addition, several studies [23]- [26] have demonstrated that channel or antenna correlation can be exploited to reduce the overhead of the downlink training phase. A multi-beam selection scheme for massive MIMO is presented in [27]. The problem of designing training sequences with low overheads have been studied in [28]. There are also several other approaches proposed for resolving the challenges of training and limited feedback in the more general context of multi-user MIMO; see e.g., [29]- [32].

Our proposed solution is to interleave the training and feedback stages as shown in Fig. 2.

Unlike the conventional scheme in Fig. 1, the transmitter trains its antennas one by one and receives feedback information after training each one of its antennas. A feedback message may ask the transmitter to train another antenna (and also provide side information about the channel state), or it may result in the termination of the training phase, in which case it also provides the quantized codeword to be utilized by the transmitter for data transmission. An interleaved scheme offers the following unique opportunity: If the already-trained antennas provide sufficiently favorable conditions for data transmission, one can then terminate the training phase and thus avoid wasting more resources on training the rest of the antennas. One main message of this paper is that in certain scenarios, we can make use of this opportunity to design multi-antenna communication systems whose feedback and training overheads remain completely independent of the number of transmit antennas, and which, at the same time, can achieve the same outage performance as a system with perfect transmitter and receiver CSI. Specifically, we consider here a single-user point-to-point MISO system with the outage probability performance measure. Note that, while the "mainstream" use case of a massive transmitter antenna array is to support multiple users, a single-user system suffering from severe path loss may also greatly benefit from beamforming over a large number of antennas. Extensions to multiple-input multiple-output (MIMO) systems, or to multi-user scenarios with different performance measures (such as ergodic capacity) will thus be left as future work. In fact, after the publication of a preliminary version of this work [1], another paper [33] has studied the benefits of interleaving in hybrid single-user and multiple-user massive MIMO systems. The work [33] also considers a general channel model that can incorporate channel correlations. On the other hand, [33] ignores the feedback overhead of the interleaved scheme: It is assumed that the trained channel gains can be perfectly fed back to the transmitter, which requires an infinite number of feedback bits in practice. In contrast, we design interleaved schemes to minimize the training overhead as well as the feedback rate. In more detail, the main contributions of this paper are as follows:

• We propose a novel communication scheme which interleaves training and feedback stages.

In this scheme, the transmitter trains its antenna one by one while the receiver transmits the feedback information immediately after training each antenna. The feedback message may ask the transmitter to train another antenna or provide the quantized codeword to be utilized for data transmission. The latter event occurs if the already trained antennas can provide enough channel gain to avoid outage.

• We apply the interleaving scheme to a MISO system with t transmit antennas, a short-term power constraint P , and target data rate ρ. We show that our scheme is able to achieve the same outage probability as a system with perfect transmitter and receiver CSI while keeping the average feedback rate and the average number of training antennas independent of t and dependent only on P and ρ.

• We design a variable-rate quantizer to minimize the feedback rate in the MISO system while keeping the same outage probability as a full-CSI system. It is achieved by allocating a higher rate to a larger coefficient in a given channel state. We also discuss the latency costs associated with interleaving, and study antenna grouping schemes as a solution.

Part of this work has been presented in a conference [1]. Compared to [1], the current paper provides the proofs of technical results. It also describes a procedure to design optimal variable- rate quantizers of the feedback information. Here, we also provide numerical results that verify our analysis, and a discussion on the latency costs associated with interleaving and grouping.

The rest of the paper is organized as follows: In Section II, we describe the system model, and the full-CSI and open-loop systems. In Section III, we introduce the idea of interleaving and construct a simple interleaved scheme based on antenna selection. In Section IV, we show how to design an interleaved scheme that can achieve the full-CSI gains with low training length and low feedback rate. In Section V, we describe a variable-rate quantizer to further reduce the feedback rate. In Section VI, we discuss latency costs and study interleaved schemes with antenna grouping. Finally, we present the simulation results in Section VII and conclusions in Section VIII. Some of the technical proofs and extended discussions are provided in the appendices.

Notation: C m×n is the set of all m × n complex matrices with C m C m×1 and C C 1 . I m is the m × m identity matrix, and 0 m×n is the m × n all-zero matrix. CN(K) is a circularlysymmetric complex Gaussian random vector with covariance matrix K. P and E represent the probability and the expected value, respectively. o, O, and Θ are the standard Bachmann-Landau symbols. A T and A † are the transpose and the conjugate transpose of matrix A. • stands for the entrywise product. For x ∈ R, x + x if x ≥ 0, and x + 0, otherwise. For reader's convenience, we show the symbols that we will use for various schemes in the paper in Table I.

## II. PRELIMINARIES

We consider a MISO system with t transmit antennas. Denote the channel from transmit antenna i to the receiver antenna by h i , and let h = [h  For a fixed h, suppose that input symbol s is distributed as CN(K T ), where K is a covariance matrix with tr(K) ≤ 1. With perfect CSIR, the channel capacity under this strategy is log 2 (1 + h † KhP ) bits/sec/Hz. In this work, we consider a delay-constrained system where it is necessary and sufficient to sustain a certain fixed rate of data transmission at all times. Examples include video streaming for teleconferencing. In these so-called block-fading scenarios, averaging out a data codeword over infinitely many channel states is not feasible. The appropriate performance metric is the outage probability, which is the probability that the system will not be able to support a given target data rate [34], [35]. In our system, for a given target data transmission rate ρ = log 2 (1 + αP ), where α > 0 can be chosen arbitrarily, an outage event occurs if

We refer to the special case where K = xx † for some x ∈ C t with x ≤ 1 as "beamforming," in which case the outage event is | x, h | 2 < α. We assume that both the transmitter and the receiver agree upon a common transmission rate and power before any training or feedback communication takes place. This ensures that both terminals have perfect knowledge of α. We also assume that there are no CSI estimation errors: Once a transmitter trains a particular antenna, the receiver can acquire the corresponding CSI error-free. The results of this paper will thus serve as upper bounds on the performance of systems that take into account possible errors in CSI estimation.

For a random h, the transmitter can use different covariance matrices for different h. Let M : C t → C t×t be an arbitrary mapping, so that given h, the input symbol is distributed as

## CN([M(h)] T

). The outage probability with M is out(M) P(h † Mh < α). For a beamforming-only system with mapping N :

With perfect CSIT and CSIR (a "full-CSI" system), the optimal mapping is beamforming along h [36]. In other words, the mapping F(h) h h provides the minimum-possible outage probability out(F) = P( h 2 ≤ α). With perfect CSIR but no CSIT (an "open-loop" system), it is shown in [38] that the optimal mapping is G(h)

, where κ arg min k P( k i=1 |h i | 2 < kα). Hence, only κ out of the t antennas are used in general, and we have out(G) = P( h κ 2 < κα). Note that κ does not depend on the channel state h. Therefore, the open-loop mapping is also independent of the channel state. antenna selection schemes at α = 0.5 (left) and α = 2 (right). Note that a larger path loss exponent (due to higher frequency of transmission) or a greater transmitter-to-receiver separation translates to a higher α in practice.

Therefore, using as many as a hundred antennas may be necessary to achieve an acceptable outage probability even in a single-user system, as evidenced by the case α = 2 and antenna selection.

The outage performance of communication systems in terms of their α-asymptotic behaviors for a fixed t has been studied in the literature. For example, a full-CSI and an open-loop system, with t antennas, both provide a "diversity gain" of t [36]. In other words, given a fixed t, as α → 0, we have out(F) ∈ Θ(α t ) and out(G) ∈ Θ(α t ) so that the outage probabilities of a full-CSI and an open-loop system have the same α → 0 behavior. In contrast, in this work, we are primarily interested in the t-asymptotic behavior of outage probabilities for a fixed α, i.e., the behavior of the system for a massive number of antennas. The following proposition, whose proof can be found in Appendix A, provides a rough characterization in this context.

Proposition 1 As t → ∞, for a full-CSI system, we have out(F) ∈ Θ( α t t! ), ∀α > 0, whereas for an open-loop system, we have out

As is shown in Fig. 3, the outage probability of an open-loop system decays much slower than that of a full-CSI system. Proposition 1 brings both good and bad news. The good news is that for a full-CSI system, one can transmit with an arbitrarily large data rate (by choosing a sufficiently large α) with a fixed power consumption P and zero outage as t → ∞. The bad news is that it is not always possible to do the same in an open-loop system: When α ≥ 1, the outage probability does not decay to 0 with increasing t, and in fact, it saturates to a certain non-zero value. Also, for 0 < α < 1, even though we have out(G) → 0 as t → ∞, there is still room for improvement: As t increases, the outage probability of a full-CSI system decays much faster than that of an open-loop system.

In order to obtain a vanishing outage probability as t → ∞ for every α, one should thus utilize CSIT. The full-CSI system is impractical as it requires an "infinite" rate of feedback from the receiver to the transmitter. A more practical approach is to settle for quantized CSIT via finite-rate receiver feedback [3]. Another issue that is common to both a full-CSI and an open-loop system is the requirement of perfect CSIR, which may, by itself, not be feasible when t is large. In the following, we thus consider the design of partial CSIT, partial CSIR schemes that interleave the training and feedback processes as shown in Fig. 2.

### III. INTERLEAVED TRAINING AND LIMITED FEEDBACK

We begin with a simple example of an interleaved scheme that is based on antenna selection.

We first describe its conventional non-interleaved counterpart.

# A. The Conventional Antenna Selection Scheme

A well-known partial-CSIT scheme is what we shall refer to as the "conventional" antenna selection scheme: Given h, the transmitter first trains all of its antennas so that the receiver acquires the entire CSI. The receiver determines the antenna index τ arg max i |h i | with the highest channel gain and sends ⌈log 2 t⌉ feedback bits to the transmitter that can uniquely represent τ . The transmitter recovers τ from the feedback bits and transmits over antenna τ .

This scheme can be characterized by the mapping A(h) e τ , where

. . , t are the standard basis vectors for C t . We have out(A) = (1e -α ) t , which implies ∀α > 0, lim t→∞ out(A) = 0. Hence, for every α > 0, we can obtain a vanishing outage probability as t → ∞, as desired, which is also shown in Fig. 3. Moreover, for any α and t, we have out(A) ≤ out(G), and in fact, it can be shown (e.g. by applying Stirling's approximation to the asymptotic formulae in Proposition 1) that out(A) ∈ o(out(G)), ∀α ∈ (0, 1). Hence, relative to an open-loop system, antenna selection improves the t-asymptotic behavior of the outage probability for all α > 0. This is shown for two values of α in Fig. 3. On the other hand, to implement this scheme, one needs to train t scalar channels (one for each h i ) and feed back ⌈log 2 t⌉ bits for every channel. Clearly, this is not feasible in the t → ∞ regime.

# B. A New Antenna Selection Scheme

The conventional antenna selection scheme is excessively precise in the sense that it always tries to select the antenna with the highest gain. On the other hand, without any loss of optimality in terms of the outage probability, we can in fact select any one of the antennas that avoids outage (not necessarily the antenna that provides the highest channel gain) whenever there is one. We use this observation to design an alternate antenna selection scheme that is based on the idea of interleaving training and limited feedback.

Set i ← 0.

TX begins data transmission via e i . b = 0, i < t? TX receives b.

## Yes

No Fig. 4: The new antenna selection scheme. Note that the variable i, i.e., the antenna number, can be thought to be "naturally available" to both the transmitter and the receiver: At both terminals, it can be initialized and updated throughout the multiple training and feedback stages without any extra overhead. Also note that the receiver is always aware of what the next action (training a new antenna or beginning the data transmission) of the transmitter is going to be so that there is no inconsistency. This is because it is the receiver itself that provides the feedback message, which uniquely determines the transmitter action.

Our new antenna selection scheme operates as shown in Fig. 4: The transmitter first trains the channel h 1 corresponding to the first antenna and waits for receiver feedback. The receiver, having acquired the knowledge of h 1 , sends the one-bit feedback message "

if selecting the first antenna avoids outage. Otherwise, it feeds back a "0," which indicates that selecting the first antenna will result in an outage. Now, if the transmitter receives a "1," the training and feedback process can end; the transmitter starts data transmission over the first antenna only (without the need of training the remaining antennas) and outage is avoided. Otherwise, if the transmitter receives a "0," it proceeds to training the channel state h 2 corresponding to its second antenna. The process continues in the same manner until an antenna (selection vector) that avoids outage is found. If all the antennas result in an outage, then the transmitter can simply transmit over an arbitrary antenna.

Clearly, the new scheme achieves the same outage probability (1e -α ) t as the conventional scheme discussed in Section III-A. Now, given 1 ≤ i ≤ t -1, the transmitter trains only the first i antennas with probability e -α (1e -α ) i-1 , and it trains all the t antennas with probability

(1e -α ) t-1 . The training length, which we define as the average number of antennas that are trained per channel state, is thus

A similar calculation reveals that the feedback rate of the scheme, which we define as the average number of bits that are fed back per channel state, is actually (numerically) equal to its training length. Hence, the training and the feedback rates of the new scheme are both given by the formula e α (1 -(1e -α ) t ). Note that for any t, the two rates are both upper bounded by e α , which is independent of t.

The significance of the new scheme is that it provides a vanishing outage probability as t → ∞ with t-independent training length and feedback rate. One can thus obtain the benefits of having infinitely many antennas with finite training and feedback overheads. For example, setting α = 1, we can observe that if the transmitter has infinitely many antennas, then for any given power constraint P , we can transmit with rate log(1 + P ) bits/sec/Hz outage-free via training only e < 3 antennas and feeding back 3 bits on average. Comparison with an open-loop system (a system with perfect CSIR but no CSIT) leads to the following conclusion: It is much better to have a little bit of CSIT and a little bit of CSIR rather than to have perfect CSIR but no CSIT.

We note that our interleaved antenna selection scheme can also be applied to the orthogonal frequency division multiplexing (OFDM) systems. The main challenge is that the best selection of antennas is likely to change with frequency. As is shown in [37], the antenna selection problem can be formulated as finding the antenna with the best channel averaged over all sub-carriers.

As a result, we may use the average channel gain over all sub-carriers to determine whether a specific antenna is outage-avoiding or not.

Several variations on our interleaved antenna selection scheme can be considered. For example, in order to avoid the possible implementation complexities and delays of training the antennas one by one, the transmitter may train all t antennas at once as in conventional antenna selection.

On the other hand, the receiver may now use variable-length feedback instead of the ⌈log 2 t⌉ bits of fixed length feedback in conventional antenna selection. In detail, suppose that selecting any of the first υ antennas results in an outage, but selecting Antenna υ + 1 avoids outage, where υ ∈ {0, . . . , t}. We let υ = t if selecting any of the t antennas results in outage. The receiver then feeds back the binary codeword 

# C. General Description of an Interleaved Scheme

So far, we have discussed many seemingly-different scenarios including non-interleaved or interleaved schemes, the full-CSI and the open-loop systems, and so on. All of these scenarios can in fact be viewed as manifestations of a single unifying framework of a generalized beamforming scheme, which describes the rules of how the tasks of training and feedback are to be performed.

The advantage of this viewpoint is that it will allow us to more meaningfully compare different scenarios with respect to their outage probabilities, training lengths, and feedback rates. We call this generalized beamforming scheme, as defined below, Scheme S.

One task of Scheme S is to specify the quantized covariance matrix S(h) to be utilized given channel state h. By the definitions in Section II, the outage probability with S is thus given by out(S). Scheme S also describes which antennas are to be trained in which order, the corresponding feedback messages of the receiver, and how these messages are decoded at the transmitter. Obviously, different choices result in different schemes and different performances.

An example of these "inner workings" of Scheme S can be found in Section III-B for the special case of our new antenna selection scheme. As such, while we use Scheme S to represent the general structure of our beamforming scheme, when the details of training, feedback, transmission and decoding are defined, i.e., a specific scheme is defined in details as done in Section III-B, we will use a specific name for the specific scheme. The two important figures of merit of Scheme S is its training length tl(S) and its feedback rate fr(S), which can be defined in the same manner as we have done in Section III-B.

We can now view a full-CSI system, called Scheme F, as an example of Scheme S. Operationally, a full-CSI system trains all its antennas and performs the optimal beamforming along the direction h h . As a result, we will have out(F) = P( h 2 < α) and tl(F) = t. Since representing an arbitrary beamforming vector requires an infinite rate of feedback, we have

Similarly, the open-loop scheme G trains the first κ antennas. Since there is no feedback, fr(G) = 0 and the transmitter sends independent Gaussian symbols with equal energy over the first κ antennas. Therefore, we have out(G) = P( h κ 2 < κα) and tl(G) = κ. Also, as

shown in Section III-A, the conventional antenna selection system, called Scheme A, will have out(A) = (1e -α ) t , tl(A) = t, and fr(A) = ⌈log 2 t⌉.

Clearly, Scheme S provides a framework to extend the previous definitions in a consistent manner and offers a set of quantities to compare the performance of different schemes. For example, we can summarize the performance metrics of our new antenna selection scheme in Section III-B, called Scheme B, in the following theorem:

These results lead to the following question: What is the best-possible outage probability for given constraints on training length and feedback rate? Unfortunately, this problem appears to be difficult in general, and we thus leave a detailed treatment as future work. In a related direction, Theorem 1 shows the existence of a "good" scheme that can achieve a vanishing outage probability as t → ∞ with t-independent feedback and training lengths. One fundamental question that immediately comes to mind is then to determine whether one can achieve the ultimate limit out(F) with again t-independent training length and feedback rate. The answer is yes, and the construction of such a scheme will be provided next. Meanwhile, we note that even though antenna selection provides a reasonable performance, we still have out(F) ∈ o(out(A))

as t → ∞. In other words, the outage probability with a full-CSI system decays much faster than the one with antenna selection. While we have shown this fact analytically, Fig. 3 demonstrates it numerically as well. This also provides a "practical motivation" for construction of schemes that achieve the full-CSI gains.

## IV. ACHIEVING THE FULL-CSI GAINS BY INTERLEAVING

Our construction here relies on our earlier work [8], which introduced the idea of variablelength feedback for a MISO system with perfect CSIR. We thus first recall some of the relevant technical tools and results.

# A. Variable-Length Limited Feedback with Perfect CSIR

We begin by defining a simple deadzone scalar quantizer. For any given integer ℓ ≥ 0 and

x ∈ [-1, +1], let q(x; ℓ) sign(x) 1 2 ℓ+1 ⌊|x|2 ℓ+1 ⌋. We can easily calculate q(x; ℓ) by taking the most significant ℓ + 2 bits

while preserving the sign of x. For example, we have q(±(0.101) 2 ; 1) = ±(0.10) 2 .

We extend the definition of the deadzone quantizer q to an arbitrary beamforming vector

We refer to the parameter ℓ as the "resolution" of q. Note that by construction, q(x; ℓ) ≤ 1, and therefore, q(x; ℓ) is itself a feasible beamforming vector. Moreover, for a fixed ℓ and t, each quantized vector q(x; ℓ) can be uniquely represented by 2t(ℓ + 3) bits (For each of the 2t complex dimensions of x, we spend one bit for the sign, and ℓ + 2 bits for the most significant ℓ + 2 binary digits.).

## Now, for an arbitrary channel state

We have the following proposition.

This result has the following interpretation. Suppose h 2 > α, and thus outage is avoidable with the beamforming vector -→ h. By construction, the sequence of quantized beamforming vectors q( -→ h; ℓ), ℓ ≥ 0 (which are feasible since q( -→ h; ℓ) ≤ -→ h = 1) provides an increasingly finer approximation of -→ h as the resolution ℓ grows to infinity. The proposition shows that for every given h with h 2 > α, there is in fact a "sufficient resolution" L(h) (that depends only on h ) such that the quantized beamforming vector q( -→ h; ℓ) can avoid outage.

As discussed in [8], Proposition 2 leads to the following limited feedback scheme under the assumption of perfect CSIR: If h 2 > α, the receiver calculates the required resolution L(h) to avoid outage, and sends 2t(L(h) + 3) feedback bits that represent the corresponding outage-avoiding beamforming vector q( -→ h; L(h)). The transmitter, which we assume can perfectly know the length of the feedback codeword that it has received, first recovers L(h), and then the beamforming vector q( -→ h; L(h)). Otherwise, if h 2 ≤ α, outage is unavoidable except for channel states h 2 = α with zero probability. In this case, the receiver sends the one-bit feedback message "0" so that the transmitter can transmit with an arbitrary but fixed beamforming vector, say e 1 . We refer to this scheme as Scheme C t , where the subscript indicates the number of transmit antennas. We have C t (h) = q( -→ h; L(h)). By construction, Scheme C t achieves the full-CSI outage probability with the feedback rate

where p ℓ P(L(h) = ℓ, h 2 > α). As ℓ → ∞, p ℓ can be shown to decay fast enough so that the resulting feedback rate is finite; we refer the interested reader to [8] for the details and formal calculations. Intuitively, instead of trying to pick the best beamforming vector that maximizes the signal-to-noise ratio in some given codebook, one spends just enough bits to describe a beamforming vector that avoids outage. This allows us to achieve the full-CSI performance with a finite feedback rate under the assumption of perfect CSIR.

# B. Achieving out(F) by Interleaving

We now return to our main goal of designing a scheme that can achieve the full-CSI outage probability with finite training length and feedback rate. Scheme C t as described above is not immediately applicable for our purposes as (i) it requires perfect CSIR and thus induces a training length of t, and (ii) according to (2), its feedback rate grows at least as Θ(t) (We have

). We can however incorporate the sequence of Schemes C i , i = 1, . . . , t as sub-blocks of an interleaved training and limited feedback Scheme D as shown in Fig. 5. In the figure, we use the

## . , t to represent the first i components of the channel state

h. Given h and a value of the variable i ∈ {1, . . . , t} in the figure, suppose that the transmitter has "just" trained its ith antenna, so that the receiver has acquired the knowledge of h i . At this stage, the receiver knows the channel values h 1 , . . . , h i corresponding to the first i antennas of the transmitter, or equivalently, it knows h i . We consider the following two cases for the receiver's feedback and the corresponding transmitter action.

Set i ← 0.

TX trains

sends b as feedback.

TX sets x ← e 1 if i = t, b = 0, and

It begins data transmission via x. b = 0, i < t? TX recovers b.

### Yes

No Fig. 5: Operation of scheme D. Due to the equivalence between C i (h i ) = q( -→ h i ; L(h i )) and its binary description (see Section IV.A), we use the same notation "C i (h i )" for the codeword of 2i(L(h i ) + 3) bits that represent C i (h i ).

If h i 2 ≤ α, as far as the channels that have been made available to the receiver are concerned, outage is unavoidable with probability 1. The receiver thus requests the transmitter to train the next antenna by sending the feedback bit "0," and the transmitter complies. The case i = t is an exception: Outage is unavoidable with any beamforming vector with probability 1 (we have

, and thus the transmitter transmits via the (arbitrarily chosen) vector e 1 .

On the other hand, if h i 2 > α, the receiver feeds back the i-dimensional vector C i (h i ) = q( -→ h i ; L(h i )) using 2i(L(h i ) + 3) feedback bits. By Proposition 2, we have

This implies that the actual t-dimensional beamforming vector utilized at the transmitter, which is simply constructed by appending ti zeroes to C i (h i ), will also avoid outage. We shall emphasize that Theorem 2 should be interpreted as "just" an achievability result. Its main message is that the full-CSI performance can be achieved with t-independent training length and feedback rate. Hence, the α-dependent bounds in the statement of Theorem 2 are not necessarily the best-possible as far as a general scheme that can achieve out(F) is concerned.

As can be observed from the proof of the theorem, we have not tried to optimize the bounds.

Let us now also compare the results of Theorem 2 with what we have achieved by Theorem affects its feedback rate: The fewer the amount of antennas that one needs to train, the fewer the feedback messages spent requesting these antennas to be trained. In both cases, same outage probability results in the same diversity.

An interesting special case of Theorem 2 is to assume P is large (but still fixed), and choose α = P m-1 for some m > 1. Then, if the transmitter has infinitely many antennas (for a simpler discussion, we put the physical impossibility of such an assumption aside), Theorem 2 tells us that we can transmit with rate log(1 + P m ) ∼ m log P (as P → ∞) outage-free, and thus achieve a multiplexing gain of m. In other words, one can achieve "the MIMO effect" from a MISO system with a very large number of antennas. The price to pay however is a training length of O(P m ) and a feedback rate of O(P 3m ), which are both much larger than the data transmission rate m log P . Ideally, we would like the feedback and training lengths in Theorem 2 (or in another scheme with a t → ∞ vanishing outage probability) to be o(log α) as α → ∞.

Whether this is possible or not will remain as an interesting open problem and shows the need for proving converse results for general interleaved schemes.

On the other hand, regarding the data rate log(1 + αP ), when P is small (a typical case of a low-power system), even slight increase in α significantly improves the data transmission rate.

For example, for P = 1, increasing α from 1 to 3 doubles the data rate. For such scenarios with small P , tighter bounds on the training lengths, feedback rates and/or custom-made numericallydesigned interleaved schemes are a necessity. In this context, tighter bounds are desirable as they will provide a more accurate estimate on the required training and/or feedback rates to achieve a certain outage probability. On the other hand, numerical designs are desirable as they may outperform the analytically-constructed schemes. Finding an efficient algorithm for the numerical design of interleaved schemes would prove to be a challenging network vector quantization problem [39], where one has to design several interdependent vector quantizers managing the multiple feedback phases of the interleaved scheme. In particular, given t transmitter antennas, one has to design t vector quantizers, Q 1 , . . . , Q t , where the domain of Q i depends the range of

An alternating optimization approach may then be taken where, for the infinite sequence i = 1, . . . , t, 1, . . . , t, . . ., one optimizes Q i while fixing Q j , j = i.

### V. QUANTIZATION RATE ALLOCATION

We now discuss how to further reduce the feedback rate of our proposed schemes using an optimized rate allocation strategy. Recall that in the construction in Section IV-A, one spends a fixed 2(L(h)+3) bits per antenna to encode each component of the beamforming vector. Different components of a beamforming vector have different weights in the array gain which is given as

A component with higher weight should be quantized more accurately, i.e., assigned a higher rate, to provide a better overall performance [40].

For a given beamforming vector x, we assign the optimal quantization rate to each component.

To accommodate a variable-rate for different components, we need to adjust the resolution ℓ of the deadzone quantizer. Instead of using the fixed resolution ℓ for all components, resulting in a fixed-rate system, we use the resolution

or imaginary (if j = 2) part of x i . This will result in a variable-rate deadzone quantizer q v to be defined for an arbitrary beamforming vector

where q is the deadzone scalar quantizer and ℓ is a t × 2 matrix representing the resolution of q for real and imaginary parts of different components in x. Note that by the definition of the deadzone quantizer q, |q(x; ℓ)| ≤ |x| for any x ∈ [-1, 1] and any positive ℓ. Therefore, q v (x; ℓ) ≤ 1, which means q v (x, ℓ) is also a feasible beamforming vector.

Algorithm 1 Rate-Allocation Algorithm 1: Set ℓ to be the k × 2 all-zero matrix, -→ h k = h k h k , and count = 0.

, where ∆ ∆J k×2 , and J k×2 is the k × 2 all-one matrix. 5:

Find the indices i and j corresponding to the maximum values of d 1 and d 2 , respectively. 7:

To formulate it as a classic rate-allocation problem in a rate-distortion set-up, we define

The optimal rate-allocation will be achieved by assigning the appropriate quantization rate ℓ to each component of -→ h k to minimize R a while satisfying the constraint on D a . This rate-allocation problem is the dual of the bitallocation problem in data compression, which is well studied [41]- [43]. Typically, the bitallocation problem is to minimize the overall distortion under some constraint on the total bit rate while the proposed rate-allocation problem is to minimize the total bit rate under some constraint on the overall distortion. As a result, the generalized Breiman, Friedman, Olshen, and Stone (BFOS) algorithm [43] can be utilized to solve our rate-allocation problem. We design Algorithm 1, based on the generalized BFOS algorithm in [43], to find the optimal rate-allocation to quantize a beamforming vector. The main idea behind the algorithm is as follows. At each step of the algorithm, we assign additional ∆ bits to the beamforming vector component that results in the maximum distortion reduction among all possible vector components. This will result in an increase of ∆ bits to the total quantization rate and a reduction in the total distortion, i.e., an increase in the array gain. After updating the rate and distortion of the chosen component, we continue the iterations until the overall distortion satisfies the constraint D a ≥ α or the total quantization rate is greater than that of the fixed-rate deadzone quantizer.

### VI. LATENCY CONSIDERATIONS AND ANTENNA GROUPING

Our formulations so far ignore the extra latency incurred by dividing the training and feedback stages to multiple stages, as in the proposed interleaved schemes. In this section, we study the latency/performance tradeoffs of interleaving by assuming that every stage of training and interleaving consumes an extra ǫ-fraction of the time that would otherwise be spent on data transmission. This ǫ-cost may, for example, stem from the propagation delays between the transmitter and the receiver during the training and feedback phase.

In such a scenario, training the antennas one by one, as in the previous sections, may be too costly, and thus suboptimal. For this reason, we consider an interleaved antenna selection with antenna grouping that trains antennas K by K, where K ≥ 1. For simplicity, we assume T is a multiple of K. The transmitter trains the first K antennas and the receiver acquires the CSI for the first K antennas h 1 , . . . , h K . The receiver sends ⌈log 2 (1 + K)⌉ bits of feedback that either selects the antenna that can avoid outage or tells the transmitter to train the next K antennas if no such antenna exists. The process continues in the same manner until an antenna that avoids outage is found. If all antennas result in an outage, then the transmitter can simply transmit over an arbitrary antenna. We call this Scheme B ′ . For the special case of K = 1, Scheme B ′ is exactly the same as the interleaved antenna selection B in Section III-B. Now, suppose that each training/feedback stage costs ǫ-fraction of the channel codeword time.

There are totally t K stages in Scheme B ′ so that the channel capacity is (1

Given the target data transmission ρ = log 2 (1 + αP ) as before, the outage probability is given by Prob

be considered to be a "modified outage threshold" that takes into account cost effects of the training/feedback stages. By the definition of Scheme B ′ , it follows that an outage occurs if and only if |h i | 2 ≤ β, ∀i, and therefore, we have out(B ′ ) = (1e -β ) t . After some straightforward calculations, we can also obtain the training length and the feedback rate of the scheme

in closed form. For the special case of K = 1, and β replaced by α, the formulae boil down to the ones provided in Section III-B. Formally analyzing the tradeoffs between out(B ′ ), tl(B ′ ), and fr(B ′ ) for given K and ǫ is not a straightforward task due to the complicated algebraic nature of expressions. Numerical results in the next section, however, suggest that training antennas  one by one is not an optimal strategy in general, and there is an optimal number of antenna groupings K that should be considered.

### VII. SIMULATION RESULTS

In this section, we provide simulation results to compare the performance of different schemes and quantizers. Using rate-allocation results in variable rates for different components of the beamforming vector. We use a Huffman code to send the length of each beamforming vector component. In other words, each resolution, ℓ ij , is Huffman coded and the corresponding prefix- Outage Probability Full-CSI, = 2 Full-CSI, = 1 q, interleaving, = 2 q v , interleaving, = 2 q, interleaving, = 1 q v , interleaving, 1

Conventional AS, = 1 Interleaving AS, 1 Conventional AS, 2 Interleaving AS, = 2 RVQ, 2 bits/antenna, = 2 RVQ, 2 bits/antenna, = 1

Fig. 8: Outage probability as a function of t for fixed-length and variable-length deadzone quantizers.

free binary codeword representation is sent to the transmitter. In addition, ℜx i is quantized by q(ℜx i ; ℓ i1 ) and ℑx i is quantized by q(ℑx i ; ℓ i2 ), as explained in Section V.

We first present the numerical simulation results of training length and feedback rate as functions of the number of transmit antennas t for different schemes in Section III in Figs.

6 and 7, respectively. We abbreviate antenna selection by AS in both figures. In our simulations, we set α = 1. Fig. 6 shows that as t increases, the average training length of the interleaving antenna selection scheme in Section III-B saturates and is lower than those of the full-CSI

system, the open-loop system, and the conventional antenna selection scheme in Section III-A.

The full-CSI system, the open-loop system, and the conventional antenna selection scheme need to estimate all t channels. Fig. 7 reveals that as t increases, the average feedback rate of the interleaving antenna selection scheme saturates and is lower than those of the full-CSI system and the antenna selection scheme. Note that the feedback rate of the full-CSI system is infinite.

For the interleaving antenna selection scheme in both figures, the simulation results align well with the analytical results provided in Theorem 1.

We provide simulation results of the outage probability, the feedback rate, and the average feedback rate as functions of t in Figs. 8,9, and 10, respectively. We consider the deadzone quantizer q( -→ h; ℓ) and the deadzone quantizer with rate-allocation q v ( -→ h; ℓ). The average feedback rate is calculated as the feedback rate divided by the number of transmit antennas. We set ∆ = 1 in the rate-allocation algorithm. Fig. 8 demonstrates that the interleaving scheme for both Feedback Rate (bit) q, interleaving, = 2 q, interleaving, = 1 q v , interleaving, = q v , interleaving, = 1

Fig. 9: Feedback rate as a function of t for fixed-length and variable-length deadzone quantizers. Average Feedback Rate (bit/antenna) q, interleaving, = 2 q v , interleaving, 2 q, interleaving, = 1 q v , interleaving, 1 Fig. 10: Average feedback rate as a function of t for fixed-length and variable-length deadzone quantizers.

quantizers can achieve the same outage probability as the full-CSI system. Fig. 8 also shows that the outage probability of the interleaving scheme is better than the outage probabilities of the antenna selection schemes, which is further better than the outage probability of random vector quantization [44] with 2 quantization bits per antenna. A smaller outage threshold α leads to a lower outage probability. Fig. 9 exhibits several important features: First, the feedback rate with interleaving saturates as t increases. Second, the variable-rate deadzone quantizer q v reduces the total feedback rate compared to the fixed-rate deadzone quantizer q. Third, for the interleaving scheme, the feedback rate decreases as α decreases. This is because a lower resolution for the beamforming vector is acceptable if the outage threshold decreases. According to Fig. 10, as the number of transmit antennas t increases, the average feedback rate increases when t is small and deceases when t is large. It is shown that the average feedback rates per antenna for both quantizers are approximately equal to or less than 2 bits/antenna when t is large.

According to Figs. 9 and 10, the feedback rates of both deadzone quantizers saturate as the number of transmit antennas increases. This is a key difference compared to the conventional CSI quantization techniques for massive MIMO systems. For example, using the method proposed in [19], the receiver sends back a binary feedback sequence of length Bt + q where B is the number of quantization bits used per transmit antenna and q is a small positive constant, which scales linearly with the number of transmit antennas. As a result, compared to the conventional CSI quantizers, the proposed deadzone quantizers can save a large amount of feedback overhead when the number of transmit antennas is large.

For Scheme B ′ of Section VI, we present the outage probability, the training length, and the feedback rate as functions of the number of trained antennas at a time, K, in Figs. 11, 12, and 13, respectively. We can observe that the analytical results match with the simulations in all cases. In Fig. 11, the outage probability decreases with K since the SNR threshold β is a decreasing function of K, and out(B ′ ) decreases as β decreases. expected, as the per-stage cost ǫ increases, the outage probability increases. Also, according to Fig. 12, as K increases from 1 to 30, the training decreases at first but then increases. The optimal value of K that minimizes the training length is 2 for ǫ = 0.01 and 3 for ǫ = 0.02. According to Fig. 13, the optimal value of K that minimizes the feedback rate is 3 for ǫ = 0.01 and 6 for ǫ = 0.02.

According to these results, it is suboptimal to train the antennas one by one for the particular choices of the system parameters in Figs. 11,12, and 13. Depending on design requirements, one should consider grouping the antennas in the training and feedback phases.

### VIII. CONCLUSION

We introduced and analyzed multi-antenna communication schemes whose training and feedback stages are interleaved and mutually interacting. We applied the interleaving scheme to MISO systems to achieve the same outage probability as the full-CSI system using partial CSIT and partial CSIR. We designed a deadzone quantizer and a rate-allocation algorithm to the feedback messages by a limited number of feedback bits. With t transmit antennas, the interleaving scheme with the deadzone quantizer can achieve a t-independent finite feedback rate which only depends on the power constraint and the target data rate. In addition, the rateallocation algorithm can further reduce the feedback rate by assigning distinct quantization rates to different components in a beamforming vector.

The idea of interleaving can also be used in conjunction with rate adaptation. Suppose the rate-adaptive system can support a number of rates, say, ρ 1 , . . . , ρ n , that one can choose from.

Receiver feedback will then be used to choose the beamforming vector as well as the transmission rate. An outage can be declared if the system cannot even support the minimum min i∈{1,...,n} ρ i of data rates. Given a certain outage probability, one can then study the tradeoff between the We first determine the t → ∞ asymptotic behavior of out(F). For this purpose, note that

which leads to an easy lower bound (by considering only the i = t term) out(F) ≥ α t e -α t! . For an upper bound, we can rewrite (3) as

Combining the upper and lower bounds, we have out(F) ∈ Θ( α t t! ), as desired. We now determine the outage probability of an open-loop system as t → ∞. We recall that out(G) = P( h κ(t)

2 ≤ κ(t)α), where κ(t) arg min k∈{1,...,t} P( h k 2 ≤ kα) with ties broken in favor of k with the smallest index. Then, either κ(t) = t for infinitely many t or ∃t 0 ≥ 1, ∀t ≥ t 0 , κ(t) = t 0 . For values of α that satisfy the latter scenario, we have out(G) = Θ(1).

Suppose 0 < α < 1. It follows from (3) that P( h 2 ≤ tα) ≥ (tα) t e -tα t!

. On the other hand, substituting tα instead of α to the expansion in (4), and using the bound (t+1) • • • (t+i) ≥ t i for the denominator of the fraction in summation, we obtain P( h 2 ≤ tα) ≤ (tα) t e -tα t!(1-α) . Combining the upper and lower bounds, it follows that we have out(G) = Θ( (tα) t e -tα t!

) for 0 < α < 1.  

We have P(h ∈ A 1 ) = e -α . For i ∈ {2, . . . , t -1}, we have

e -y e -x x i-2 (i -2)! dydx = e -α α 0 x i-2 (i -2)! dx = α i-1 e -α (i -1)! .

Also, since tP(h

i! , we have

as claimed in the statement of the theorem.

We now calculate the feedback rate fr(D) of Scheme D. Note that for any i = 1, . . . , t, if h ∈ A i , the receiver sends a total of (i -1) bits for requesting the transmitter to train the first i -1 antennas (via i -1 one-bit binary codewords "0"). In addition, it sends 2i(L(h i ) + 3) bits for the outage avoiding quantized beamforming vector, for a total of 2iL(h i ) + 7i -1 feedback bits. For h ∈ B, there are only t feedback bits. The feedback rate is thus given by fr(D) = We now evaluate the sum. For this purpose, we partition A 1 , . . . , A t via A ′ i {h ∈ C t : α < h i 2 < 2α, h i-1 2 ≤ α} and A ′′ i {h ∈ C t : h i 2 ≥ 2α, h i-1 2 ≤ α}, with the convention that h 0 = 0 is deterministic. Note that for any i ∈ {1, . . . , t}, if h ∈ A ′ i , then

while if h ∈ A ′′ i , then L(h i ) = ⌈log 2 (4i)⌉ ≤ 3 + 2 log i. Thus, fr(D) ≤ 7(1 + α) + 6

.

We now find upper bounds on S 1 , S 2 , and t i=1 S 3i . Regarding S 1 and S 2 , note that we have already evaluated the probabilities P(h ∈ A i ), i = 1, . . . , t in (6). Hence,

log(i + 2) ≤log(⌈α⌉+2)

≤ 4α log(α + 3). (10) For an upper bound on t i=1 S 3i , we consider S 31 , S 32 , and t i=3 S 3i separately. We have Substituting the bounds in ( 9), ( 10), ( 11), (12), and ( 13) to (8), we obtain fr(D) ≤ 13 + 23α + 16α log(3 + α) + 8α 2 + 6α 3 . Using the bound log(3 + α) ≤ α + 2, we obtain fr(D) ≤ 13 + 55α + 24α 2 + 6α 3 . Finally, the inequalities α 2 ≤ 1 + α 3 and α ≤ 1 + α 3 lead to fr(D) ≤ 92 + 85α 3 ≤ 92(1 + α 3 ), and this concludes the proof.

