# DESCRIPTION

## BACKGROUND

### Field of the Technology

The invention relates to the field of wireless communication and in particular with beamforming, feedback and channel training.

### Description of the Prior Art

The performance of a wireless communication system can be greatly improved by making the channel state information (CSI) available at the transmitter and the receiver. In wireless communications, channel state information (CSI) refers to known channel properties of a communication link. This information describes how a signal propagates from the transmitter to the receiver and represents the combined effect of, for example, scattering, fading, and power decay with distance. The CSI makes it possible to adapt transmissions to current channel conditions, which is crucial for achieving reliable communication with high data rates in multi-antenna systems. In a massive multiple-input single-output (MISO) system, having CSI at the transmitter (CSIT) is especially desirable as one can then fully exploit the performance gains promised by the large number of transmitter antennas via CSI-adaptive transmission strategies such as beamforming. A typical way to acquire CSIT is channel training followed by (digital) feedback.

Training and feedback are traditionally viewed as two non-interleaving processes, as shown in prior art FIG. 1. According to this traditional viewpoint, for each channel state, the transmitter first trains all of its antennas at once, so that the receiver acquires the entire CSI (or, in general, an erroneous version thereof.). This initial training phase is followed by the receiver feeding back a possibly-quantized version of the CSI. The receiver's feedback is then utilized at the transmitter side for data transmission (e.g., as a quantized beamforming vector.). Designing such limited feedback systems is a fundamental problem of communication theory and has been the subject of many publications and at least one survey.

The conventional scheme in prior art shown FIG. 1 appears to be infeasible in the case of a massive MISO system. Even the training phase, by itself, would be very challenging to realize due to the large number of transmitter antennas that need to be trained. Moreover, even if one assumes that the training stage somehow comes with no cost, feeding back the associated large number of channel values to the transmitter appears to be infeasible. Conventional limited feedback schemes also do not provide much hope in this context: The feedback rates required for even the simplest of the limited feedback schemes, such as antenna selection, theoretically grow without bound as the number of transmitter antennas grow to infinity.

## BRIEF SUMMARY

Our proposed solution is to interleave the training and feedback stages. Unlike the conventional scheme of the prior art, the transmitter trains its antennas one by one and receives feedback information after training each one of its antennas. A feedback message may ask the transmitter to train another antenna (and also provide side information about the channel state), or it may result in the termination of the training phase, in which case it also provides the quantized code word to be utilized by the transmitter for data transmission.

An interleaved scheme offers the following unique opportunity: If the already-trained antennas provide sufficiently favorable conditions for data transmission, one can then terminate the training phase and thus avoid wasting more resources on training the rest of the antennas. In certain scenarios, we can make use of this opportunity to design multi-antenna communication systems whose feedback and training overheads remain completely independent of the number of transmitter antennas, and which, at the same time, can achieve the same performance as a system with perfect transmitter and receiver CSI. Specifically, in the illustrated embodiment we consider a single-user point-to-point MISO system having an outage probability performance measure. Extensions to multiple-input multiple-output (MIMO) systems, or to multiuser scenarios with different performance measures are also within the scope and spirit of the invention.

We introduce and investigate the opportunities of multi-antenna communication schemes whose training and feedback stages are interleaved and mutually interacting. Specifically, unlike the traditional schemes where the transmitter first trains all of its antennas at once and then receives a single feedback message, we consider a scenario where the transmitter instead trains its antennas one by one and receives feedback information immediately after training each one of its antennas. The feedback message may ask the transmitter to train another antenna; or it may terminate the feedback/training phase and provide a quantized code word (e.g., a beamforming vector) to be utilized for data transmission.

As a specific application, we consider a multiple-input single-output system with t transmitter antennas, a short-term power constraint P, and a target data rate ρ. We show that for any t, the same outage probability as a system with perfect transmitter and receiver channel state information can be achieved with a feedback rate of R1 bits per channel state and via training R2 transmitter antennas on average, where R1 and R2 are independent of t, and depend only on ρ and P.

While the apparatus and method has or will be described for the sake of grammatical fluidity with functional explanations, it is to be expressly understood that the claims, unless expressly formulated under 35 USC 112, are not to be construed as necessarily limited in any way by the construction of “means” or “steps” limitations, but are to be accorded the full scope of the meaning and equivalents of the definition provided by the claims under the judicial doctrine of equivalents, and in the case where the claims are expressly formulated under 35 USC 112 are to be accorded full statutory equivalents under 35 USC 112. The disclosure can be better visualized by turning now to the following drawings wherein like elements are referenced by like numerals.

The disclosure and its various embodiments can now be better understood by turning to the following detailed description of the preferred embodiments which are presented as illustrated examples of the embodiments defined in the claims. It is expressly understood that the embodiments as defined by the claims may be broader than the illustrated embodiments described below.

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

Our proposed solution is to interleave the training and feedback stages as shown in FIG. 2. Unlike the conventional scheme in FIG. 1, the transmitter trains its antennas one by one and receives feedback information after training each one of its antennas. A feedback message may ask the transmitter to train another antenna (and also provide side information about the channel state), or it may result in the termination of the training phase, in which case it also provides the quantized code word to be utilized by the transmitter for data transmission.

An interleaved scheme offers the following unique opportunity: If the already-trained antennas provide sufficiently favorable conditions for data transmission, one can then terminate the training phase and thus avoid wasting more resources on training the remaining antennas. As a result in certain scenarios, we can make use of this opportunity to design multi-antenna communication systems whose feedback and training overheads remain completely independent of the number of transmitter antennas, and which, at the same time, can achieve the same performance as a system with perfect transmitter and receiver CSI. Specifically, we consider here a single-user point-to-point MISO system having an outage probability performance measure. Extensions to multiple-input multiple-output (MIMO) systems, or to multiuser scenarios with different performance measures are within the scope and spirit of the invention.

Preliminaries

We consider a MISO system with t transmitter antennas. The channel from transmitter antenna i to the receiver antenna is denoted by hi, and let h=[h1 . . . ht]TεCt represent the entire channel state. We assume that h≈CN(It), where It is intensity of the transmitted signal and CN(.) is the circularly-symmetric complex normal distribution. The transmitted symbol sεCt and the received symbol yεC have the input-output relationship y=sT √Ph+η, where P is the short-term power constraint of the transmitter, and the noise term η˜CN(1) is independent of h.

For a fixed h, suppose that input symbol s is distributed as CN(KT), where K is a covariance matrix with tr(K)≦1. With perfect channel state information at the receiver, CSIR, the channel capacity under this strategy is log2 (1+h†KhP) bits/sec/Hz. For a given target data transmission rate ρ=log2(1+αP), where α>0 can be chosen arbitrarily, an outage event occurs if log2(1+h†KhP)<ρ, or equivalently if h†Kh<α. We refer to one special case where K=xx† for some XεCt with ∥x∥≦1 as “beamforming,” in which case the outage event is x, h2<α.

For random h, the transmitter can utilize different covariance matrices for different h. For this purpose, let M: Ct→Ct×t be an arbitrary mapping, so that given h, the input symbol is distributed as CN([M(h)]T). We define the outage probability with M as out(M)P (h†Mh<α). We often consider beamforming-only systems, so that for a mapping N: Ct→Ct, we define out(N)P|(N(h), h|2<α).

With perfect channel state information at the transmitter, CSIT, and CSIR (a “full-CSI” system), the optimal mapping that minimizes the outage probability is beamforming along h. In other words, the mapping F(h)h/∥h∥ provides the minimum-possible outage probability out(F)=P(∥h∥2≦α). With perfect CSIR but no CSIT (an “open-loop” system), it has been shown that the optimal mapping is

\(\mspace{20mu} {{G(h)}\overset{\Delta}{=}{\frac{1}{\kappa}\begin{pmatrix}
{I\text{?}} & 0_{\kappa \times {({t - \kappa})}} \\
0_{{({1 - \kappa})} \times \kappa} & {0\text{?}}
\end{pmatrix}}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

where κ=argmink P(Σk|hi|2<κα). Hence, only κ out of the t antennas are used in general, and we have out(G)=P(∥hκ∥2<κα).

The outage performance of two communication systems are usually compared in terms of their a-asymptotic behaviors for a fixed t. For example, given a fixed t, as α→0, we have out(F)ε⊖(αt) and out(G)ε⊖(αt) so that the outage probabilities of a full-CSI and an open-loop system have the same α→0 behavior (they both provide a “diversity gain” of t.). In contrast, we are primarily interested in the t-asymptotic behavior of outage probabilities for a fixed α. The following proposition, provides a rough characterization in this context.

Proposition 1 As t→∞, for a full-CSI system, we have

\({{{out}(F)} \in {\theta \left( \frac{\alpha^{t}}{t!} \right)}},\)

whereas for an open-loop system,

\(\begin{matrix}
{{{out}(G)} \in \left\{ {\begin{matrix}
{{\theta \left( \frac{\left( {t\; \alpha} \right)^{t}e^{{- \alpha}\; t}}{t!} \right)},} & {0 < \alpha < 1} \\
{{\theta (1)},} & {\alpha \geq 1}
\end{matrix}.} \right.} & (1)
\end{matrix}\)

Moreover, if 0<α<1, then κ=t for every sufficiently large t, but if α≧1, then κε⊖(1) as t→∞.

This result brings both good and bad news. The good news is that for a full-CSI system, one can transmit with an arbitrarily large data rate (by choosing a sufficiently large α) with a fixed power consumption P and zero outage as t→∞. The bad news is that it is not always possible to do the same in an open-loop system: When α>1, the outage probability does not decay with increasing t, and in fact, it saturates to a certain non-zero value. Also, for 0<α<1, even though we have out(G)→0 as t→∞, there is still room for improvement: As t increases, the outage probability of a full-CSI system decays much faster than that of an open-loop system.

In order to obtain a vanishing outage probability as t→∞ for every a, one should thus utilize CSIT. The full-CSI system is impractical as it requires an “infinite” rate of feedback from the receiver to the transmitter. A more practical approach is to settle for quantized CSIT via finite-rate receiver feedback. Another issue that is common to both a full-CSI and an open-loop system is the requirement of perfect CSIR, which may, by itself, not be feasible when t is large. In the following, we thus consider the design of partial CSIT, partial CSIR schemes that are based on the idea of interleaving the training and feedback processes as shown in FIG. 2.

Interleaved Training and Limited Feedback

We begin with a simple example of an interleaved scheme that is based on antenna selection. We first describe its conventional non-interleaved counterpart.

A. The Conventional Antenna Selection Scheme

A well-known partial-CSIT scheme is what we shall refer to as the “conventional” antenna selection scheme: Given h, the transmitter first trains all of its antennas to the receiver so that the receiver acquires the entire CSI. The receiver determines the antenna index arg maxi|hi| with the highest channel gain and sends ┌log2 t┐ feedback bits to the transmitter that can uniquely represent . The transmitter recovers from the feedback bits and transmits over antenna

This scheme can be characterized by the mapping A(h)⊖, where ei=[01×(i-1) 1 01×(t-1)]T, i=1, . . . , t are the standard basis vectors for Ct. We have out(A)=(1−e−α)t, which implies ∀α>0, limt→∞out(A)=0. Hence, for every α>0, we can obtain a vanishing outage probability as t→∞, as desired. Moreover, for any α and t, we have out(A)≦out(G), and in fact, it can be shown (e.g. by applying Stirling's approximation to (1)) that out(A)o(out(G)), ∀α(0, 1). Hence, relative to an open-loop system, antenna selection improves the t-asymptotic behavior of the outage probability for all α>0. On the other hand, to implement this scheme, one needs to train t scalar channels (one for each hi) and feed back |log2 t| bits for every channel state. Clearly, this is not feasible in the t→∞ regime.

B. A New Antenna Selection Scheme

The conventional antenna selection scheme is excessively precise in the sense that it always tries to select the antenna with the highest gain. On the other hand, without any loss of optimality in terms of the outage probability, we can in fact select any one of the antennas that avoid outage (not necessarily the antenna that provides the highest channel gain) whenever there is one. We use this observation to design an alternate antenna selection scheme that is based on the idea of interleaving training and limited feedback.

Our new antenna selection scheme operates as shown in FIG. 3. The transmitter first trains the channel h1 corresponding to the first antenna and waits for receiver feedback. The receiver, having acquired the knowledge of h1, sends the one-bit feedback message “1” if |h1|2≧α, i.e. if selecting the first antenna avoids outage. Otherwise, it feeds back a “0,” which indicates that selecting the first antenna will result in an outage. Now, if the transmitter receives a “1,” the training and feedback process can end; the transmitter starts data transmission over the first antenna only (without the need of training the remaining antennas) and outage is avoided. Otherwise, if the transmitter receives a “0,” it proceeds to training the channel state h2 corresponding to its second antenna. The process continues in the same manner until an antenna (selection vector) that avoids outage is found. If all the antennas result in an outage, then the transmitter can simply transmit over an arbitrary antenna.

Clearly, the new scheme achieves the same outage probability (1−e−α)t as the conventional scheme discussed above. Let us now define and calculate its training and feedback overheads. Note that the transmitter trains a different number of antennas for different channel states. Therefore, we define the “training rate” of the scheme (measured in antennas per channel state) as the expected number of antennas that the transmitter needs to train, where the expectation is over all the channel states. Also, the receiver feeds back a different number of feedback bits for different channel states, so that we may define the “feedback rate” of the scheme (measured in bits per channel state) as the number of receiver feedback bits averaged over all the channel states. Now, given 1≦i≦t−1, the transmitter trains only the first i antennas with probability e−α(1−e−α)i-1, and it trains all the t antennas with probability e−α(1−e−α)t−1+(1−e−α)t. The training rate is thus: Σi=1tie−α(1−e−α)t-1+t(1−e−α)t=eα(1−(1−e−α)t).

A similar calculation reveals that the feedback rate of the new scheme is actually (numerically) equal to its training rate. Hence, the training and the feedback rates of the new scheme are both given by the formula eα (1−(1−e−α)t). Note that for any t, the two rates are both upper bounded by eα, which is independent of t.

The significance of the new scheme is that it provides a vanishing outage probability as t→∞ with t-independent training and feedback rates. One can thus obtain the benefits of having infinitely many antennas with finite training and feedback overheads. For example, setting α=1, we can observe that if the transmitter has infinitely many antennas, then for any given power constraint P, we can transmit with rate log(1+P) bits/sec/Hz outage-free via training only e<3 antennas and feeding back 3 bits on average.

Also, comparison with an open-loop system (a system with perfect CSIR but no CSIT) leads to the following conclusion: It is much better to have a little bit of CSIT and a little bit of CSIR rather than to have perfect CSIR but no CSIT.

C. General Description of an Interleaved Scheme

So far, we have discussed many seemingly-different scenarios including non-interleaved or interleaved schemes, the full-CSI and the open-loop systems, and so on. All of these scenarios can in fact be viewed as manifestations of a single unifying framework of a scheme, which describes the rules of how the tasks of training and feedback are to be performed. The advantage of this viewpoint is that it will allow us to more meaningfully compare the different scenarios with respect to their outage probabilities and training/feedback rates.

One task of a scheme S is to specify a quantized covariance matrix S(h). The outage probability with S is thus given by out(S). A scheme S also describes which antennas are to be trained in which order, the corresponding feedback messages of the receiver, and how these messages are decoded at the transmitter. An example of these “inner workings” of a scheme can be found above for the special case of our new antenna selection scheme. The two important figures of merit of S is its training rate tr(S) and its feedback rate fr(S), which can be defined in the same manner as we have done above.

Using these definitions, we can now view a full-CSI system as one particular scheme F with out(F)=P(∥h∥2<α), tr(F)=t, and fr(F)=∞, an open-loop system as another scheme G with out(G)=P{∥h∥2<κα), tr(G)=κ, and fr(G)=0, and the conventional antenna selection as a scheme A with out(A)=(1−e−α)t, tr(A)=t, and fr(A)=[log2 t]. These extend the previous definitions in a consistent manner. Also, regarding the new antenna selection scheme described above, we have proved the following theorem: Theorem 1 There is a scheme B with out(B)=out(A)=(1−e−α)t and tr(B)=fr(B)=eα(1−(1−e−α)t)<eα.

Theorem 1 shows the existence of a “good” scheme that can achieve a vanishing outage probability as t→∞ with t-independent feedback and training rates. One fundamental question that immediately comes to mind is then to determine whether one can achieve the ultimate limit out(F) with again t-independent training and feedback rates. The answer is yes, and the construction of such a scheme will be provided next. Meanwhile, we note that even though antenna selection provides a reasonable performance, we still have out(F)εo(out(A)) as t→∞. In other words, the outage probability with a full-CSI system decays much faster than the one with antenna selection. This also provides a “practical motivation” for construction of schemes that achieve the full-CSI gains.

Achieving the Full-CSI Gains by Interleaving

A. Variable-Length Limited Feedback with Perfect CSTR

We begin by defining a simple dead zone scalar quantizer. For any given integer l≧0 and xε(−1, +1], let

\({q\left( {x;l} \right)}\overset{\Delta}{=}{{{sign}(x)}\frac{1}{2^{l + 1}}{\left\lfloor {{x}2^{l + 1}} \right\rfloor.}}\)

We can easily calculate q(x; l) by taking the most significant l+2 bits (b1, b2 . . . bt+1)2 of the binary representation (b1, b2 . . . )2 of |x, while preserving the sign of x. For example, we have q(±(0.101)2; 1)=±(0.10)2.

We extend the definition of the dead zone quantizer q to an arbitrary beamforming vector X=[x1 . . . xt]TCt with ∥x∥≦1 by setting q(x; l)=[q(Rx1; l)+jq(ℑx1; l) . . . q(Rxt; l)+jq(ℑxt; l)]TCt. We refer to the parameter l as the “resolution” of q. Note that by construction, ∥q(x: l)∥≦1, and therefore, q(x; l) is itself a feasible beamforming vector. Moreover, for a fixed l and t, each quantized vector q(x; l) can be uniquely represented by 2t(l+3) bits (For each of the 2t complex dimensions of x, we spend one bit for the sign, and l+2 bits for the most significant l+2 binary digits.).

Now, for an arbitrary channel state h with ∥h∥2>α, let

\({L(h)}\overset{\Delta}{=}{\max \left\{ {\left\lceil {\log_{2}\left( {4t} \right)} \right\rceil,\left\lceil {\log_{2}\frac{4t\; \alpha}{{h}^{2} - \alpha}} \right\rceil} \right\} {\mspace{11mu} \;}{and}}\)
\(\overset{\rightarrow}{h}\overset{\Delta}{=}{{F(h)} = {\frac{h}{h}.}}\)

We have the following proposition.

Proposition 2 Let hεCt with ∥h∥2>α for some t≧1. Then, q({right arrow over (h)};L(h)),h|2>α.

This result has the following interpretation. Suppose ∥h∥2>α and thus outage is avoidable with the beamforming vector {right arrow over (h)}. By construction, the sequence of quantized beamforming vectors q({right arrow over (h)};l), l≧0 (which are feasible since ∥q({right arrow over (h)}; l}∥≦∥{right arrow over (h)}∥=1) provide an increasingly finer approximation of as the resolution l grows to infinity. The proposition shows that for every given h with ∥h∥2>α, there is in fact a “sufficient resolution” L(h) (that depends only on ∥h∥) such that the quantized beamforming vector q({right arrow over (h)};l) can avoid outage.

Proposition 2 leads to the following limited feedback scheme under the assumption of perfect CSIR: If ∥h∥2>α, the receiver calculates the required resolution L(h) to avoid outage, and sends 2t(L(h)+3) feedback bits that represent the corresponding outage-avoiding beamforming vector q({right arrow over (h)}; L(h)). The transmitter, which we assume can perfectly know the length of the feedback code word that it has received, first recovers L(h), and then the beamforming vector q({right arrow over (h)}; L(h)). Otherwise, if ∥h∥2≦α, outage is unavoidable except for channel states ∥h∥2=α with zero probability. Ln this case, the receiver sends the one-bit feedback message “0” so that the transmitter can transmit with an arbitrary but fixed beamforming vector, say e1. We refer to this scheme as scheme Ct, where the subscript indicates the number of transmitter antennas. We have Ct(h)=q({right arrow over (h)}; L(h)). By construction, Ct achieves the full-CSI outage probability with the feedback rate

fr(Ct)=P(∥h∥2≦α)+Σl∞┌log(4t)┐∞2t(l+3)pl,  (2)

where plP (L(h)=l, ∥h∥2>α). As l→∞, pl can be shown to decay fast enough so that the resulting feedback rate is finite. Intuitively, instead of trying to pick the best beamforming vector that maximizes the signal-to-noise ratio in some given codebook, one spends just enough bits to describe a beamforming vector that avoids outage. This allows us to achieve the full-CSI performance with a finite feedback rate under the assumption of perfect CSIR.

B. Achieving Out{F) by Interleaving

We now return to our main goal of designing a scheme that can achieve the full-CSI outage probability with finite training and feedback rates. The scheme Ct as described above is not immediately applicable for our purposes as (i) it requires perfect CSIR and thus induces a training rate of t, and (ii) according to equation 2, its feedback rate grows at least as e(t) (We have fr(Ct)≧6tΣl∞┌log(4t)┐∞pl=6tP(∥h∥2>α)ε⊖(t).).

We can however incorporate the sequence of schemes Ci, i=1, . . . , t as sub-blocks of an interleaved training and limited feedback scheme D as shown in FIG. 4. In the figure, we use the notation hi[h1 . . . hi]T, i=1, . . . t to represent the first i components of the channel state h. Given h and a value of the variable iε{1, . . . , t} in the figure, suppose that the transmitter has “just” trained its ith antenna, so that the receiver has acquired the knowledge of hi. At this stage, the receiver knows the channel values h1, . . . , hi corresponding to the first i antennas of the transmitter, or equivalently, it knows hi. We consider the following two cases for the receiver's feedback and the corresponding transmitter action.

If ∥hi∥2≦α, as far as the channels that have been made available to the receiver are concerned, outage is unavoidable with probability 1. The receiver thus requests the transmitter to train the next antenna by sending the feedback bit “0,” and the transmitter complies. The case i=t is an exception: Outage is unavoidable with any beamforming vector with probability 1 (we have ∥ht∥2=∥h∥2≦α), and thus the transmitter transmits via the (arbitrarily chosen) beamforming vector e1.

On the other hand, if ∥hi∥2>α, the receiver feeds back the i-dimensional vector Ci(hi)=q({right arrow over (h)}i; L(hi)) using 2i(L(hi)+3) feedback bits. By Proposition 2, we have |Ci(hi),hi|2>α. This implies that the actual t-dimensional beamforming vector utilized at the transmitter, which is simply constructed by appending t−i zeroes to Ci(hi), will also avoid outage.

By construction, scheme D avoids outage for any channel state h with ∥h∥2>α. Hence, it achieves the full-CSI outage probability out(F). Calculations for the training and feedback rates of D are slightly more involved.

Theorem 2 We have out(D)=out(F) with tr{D)≦1+α and fr(D)≦86(1+α3).

We shall emphasize that Theorem 2 should be interpreted as “just” an achievability result. Its main message is that the full-CSI performance can be achieved with t-independent training and feedback rates. Hence, the α-dependent bounds in the statement of Theorem 2 are not necessarily the best-possible as far as a general scheme that can achieve out(F) is concerned (this can be observed from the proof of the theorem itself.).

Let us now first compare the results of Theorem 2 with what we have achieved by Theorem 1 using the antenna selection scheme B. For scheme B, we have tr(B), fr(B)εe⊖(eα) as a→∞, while for scheme D, we have tr(D)ε⊖(α) and fr(D)εO(α log α). Hence, there are certain values of t and α where the scheme D improves upon scheme B in every aspect. It should be clear why scheme D provides a better outage performance. Regarding the training rates, note that scheme B terminates only if the most-recently trained antenna avoids outage. On the other hand, scheme D terminates whenever the joint contribution of all trained antennas avoids outage. Therefore, for every channel state, scheme D always terminates before scheme B does, and thus, in fact, tr(D)≦tr(B). The efficiency of scheme D in terms of training also positively affects its feedback rate: The fewer the amount of antennas that one needs to train, the fewer the feedback messages spent requesting these antennas to be trained.

An interesting special case of Theorem 2 is to assume P is large (but still fixed), and choose α=Pm-1 for some m>1. Then, if the transmitter has infinitely many antennas (for a simpler discussion, we put the physical impossibility of such an assumption aside), Theorem 2 tells us that we can transmit with rate log(1+Pm)˜m log P (as P→∞) outage-free, and thus achieve a multiplexing gain of m. In other words, by using interleaving, one can also achieve “the MIMO effect” from a M ISO system with a very large number of antennas. The price to pay however is a training rate of O(Pm) and a feedback rate of O(P3m), which are both much larger than the data transmission rate m log P. Ideally, we would like the feedback and training rates in Theorem 2 (or in another scheme with a t→∞ vanishing outage probability) to be O(log α) as α→∞.

On the other hand, regarding the data rate log(I+αP), when P is small (a typical case of a low-power system), even slight increases in α significantly improves the data transmission rate. For example, for P=1, increasing α from 1 to 3 doubles the data rate. For such scenarios with small α, tighter bounds on the training and feedback rates and/or custom-made numerically-designed interleaved schemes are a necessity. In this context, finding an efficient scheme for the numerical design of interleaved schemes would prove to be a challenging network vector quantization problem, where one has to design several interdependent vector quantizers managing the multiple feedback phases of the interleaved scheme.

Many alterations and modifications may be made by those having ordinary skill in the art without departing from the spirit and scope of the embodiments.

Therefore, it must be understood that the illustrated embodiment has been set forth only for the purposes of example and that it should not be taken as limiting the embodiments as defined by the following embodiments and its various embodiments.

Therefore, it must be understood that the illustrated embodiment has been set forth only for the purposes of example and that it should not be taken as limiting the embodiments as defined by the following claims. For example, notwithstanding the fact that the elements of a claim are set forth below in a certain combination, it must be expressly understood that the embodiments includes other combinations of fewer, more or different elements, which are disclosed in above even when not initially claimed in such combinations. A teaching that two elements are combined in a claimed combination is further to be understood as also allowing for a claimed combination in which the two elements are not combined with each other, but may be used alone or combined in other combinations. The excision of any disclosed element of the embodiments is explicitly contemplated as within the scope of the embodiments.

The words used in this specification to describe the various embodiments are to be understood not only in the sense of their commonly defined meanings, but to include by special definition in this specification structure, material or acts beyond the scope of the commonly defined meanings. Thus if an element can be understood in the context of this specification as including more than one meaning, then its use in a claim must be understood as being generic to all possible meanings supported by the specification and by the word itself.

The definitions of the words or elements of the following claims are, therefore, defined in this specification to include not only the combination of elements which are literally set forth, but all equivalent structure, material or acts for performing substantially the same function in substantially the same way to obtain substantially the same result. In this sense it is therefore contemplated that an equivalent substitution of two or more elements may be made for any one of the elements in the claims below or that a single element may be substituted for two or more elements in a claim. Although elements may be described above as acting in certain combinations and even initially claimed as such, it is to be expressly understood that one or more elements from a claimed combination can in some cases be excised from the combination and that the claimed combination may be directed to a subcombination or variation of a subcombination.

Insubstantial changes from the claimed subject matter as viewed by a person with ordinary skill in the art, now known or later devised, are expressly contemplated as being equivalently within the scope of the claims. Therefore, obvious substitutions now or later known to one with ordinary skill in the art are defined to be within the scope of the defined elements.

The claims are thus to be understood to include what is specifically illustrated and described above, what is conceptionally equivalent, what can be obviously substituted and also what essentially incorporates the essential idea of the embodiments.

