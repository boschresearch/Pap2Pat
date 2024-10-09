# INTRODUCTION

Information-theoretic studies in [4,5] showed that multipletransmit, multiple-receive-antenna MIMO systems offer potential for realizing high spectral efficiency in a wireless communications system. In [6,7], a practical MIMO configuration, a Bell Labs layered space-time (BLAST) system, is deployed to realize this high spectral efficiency for a narrowband TDMA system. MIMO schemes are also being considered for standardization in WCDMA/HSDPA, and may be considered for CDMA2000 as well in the near future. From the point of view of packet transmission with forward error-correction coding, MIMO schemes can be classified into two categories, namely, jointly encoded (JE) and separately encoded (SE). In a JE scheme, a single encoded packet is transmitted over multiple spatial streams, whereas in SE each spatial stream consists of a separately encoded packet. Coded-VBLAST and its variants [8], as well as space-time codes [9], fall under the JE category, while schemes such as per-antenna rate control (PARC) and its variants belong to the SE category [2,10,11].

For both JE and SE schemes, one key aspect of the MIMO-CDMA system study is to design receivers that can reliably decode the transmitted signals in a frequencyselective channel, where the signal is corrupted by both the interchip interference (ICI) and the cochannel interference (CCI). The linear minimum mean square error (LMMSE) or minimum variance distortionless response (MVDR) chip equalizers [12,13,14,15] are shown to be promising means of improving the receiver performance. The adaptive version of these algorithms can be found in [16,17]. Another alternative is the recursive Kalman filtering approach proposed in [18]. The study of advanced receivers also leads us to a better characterization of the MIMO-CDMA link. Such characterization of a wireless link, usually known as channel quality indicator (CQI), is very important from the overall system evaluation perspective, both in terms of link adaptation and link-to-system mapping [19]. In SISO systems, the CQI of a wireless link is usually reported to the base station (BS) in the form of the instantaneous SNR seen at the mobile station (MS). At the BS, the scheduler performs the link adaptation by comparing this CQI with some preset threshold to determine the proper modulation and coding scheme (MCS) for this MS. The CQI is also used in generating the so-called short-term frame error rate (FER) versus SNR curves, which provides a simple abstraction of the link for the purpose of system-level simulations. In SISO systems, the mappings of CQI to both MCS and FER, denoted as MCS(CQI) and FER(CQI), are single-dimensional mappings. For MIMO systems, if an SE MIMO scheme is used, the CQI of each coded stream can still be represented by a single SNR and hence, the single-dimensional mapping of both MCS(CQI) and FER(CQI), just as in the SISO case. However, for JE MIMO schemes, various portions of a packet see different SNRs, and hence the mapping is potentially a complicated multidimensional problem.

In this paper, we first derive a single CQI measure for the JE systems in frequency-selective channels, in order to avoid the complications of multidimensional mappings. The CQI proposed here is based on a so-called per-Walsh code joint detection structure consisting of a front-end linear filter followed by joint symbol detection among all the streams. We derive a class of filters that maximizes the so-called constrained mutual information, and show that the conventional LMMSE and MVDR equalizers belong to this class. Similar to the notion of generalized SNR (GSNR) [1], this constrained mutual information provides us with a CQI measure describing the MIMO link quality. Such a CQI measure is essential in providing a simple one-dimensional mapping for both link adaption and generating short-term curves for the purpose of link-to-system mapping for JE schemes. For the case of SE transmission, on the other hand, we extend the successive decoding algorithm of PARC [2,3] to multipath channels, and show that in this case successive decoding achieves the constrained mutual information mentioned earlier. We also derive the link quality measures for the SE transmission similar to those for JE transmission. We use these measures in simulations with link adaptation. The rest of the paper is organized as follows. Section 2 presents the MIMO signal model and notation, followed by the treatment of JE MIMO schemes in Section 3 and SE PARC-type schemes in Section 4. Finally, the simulation results are presented in Section 5.

# MIMO SIGNAL MODEL FOR CDMA DOWNLINK

Consider an M-transmit-antenna, N-receive-antenna MIMO CDMA system as illustrated in Figure 1. After channel coding (which can be either jointly encoded over antennas, or separately for different antennas), the modulated symbol streams are demultiplexed before transmission. We denote the number of active users in the system as U and the number of Walsh codes assigned to these users as K 1 , . . . , K U , where K U u=1 K u is the total number of active Walsh codes. Without loss of generality, we assume throughout this paper that the first user is the user of interest. As shown in Figure 2, the signal model at the mth transmit antenna is given as follows:

where G is the spreading gain of the system,1 and i, j, m, and k are chip, symbol, transmit antenna, and spreading code indices. Note that by definition, j = i/G , where • denotes ceiling operation. The base station scrambling code is denoted by c(i). Meanwhile, α k stands for the signal amplitude associated with spreading code k (we assume for simplicity that for a given Walsh code k, the amplitudes are the same for all antennas, extension to MIMO systems with uneven powers across antennas is possible), a k,m ( j) is the jth symbol transmitted at antenna m on Walsh code k, and

T is the kth Walsh code. Note that in this model we have implicitly assumed that the same set of Walsh codes is used across all the transmit antennas.

The transmitted signals propagate through the MIMO multipath fading channel denoted by H 0 , . . . , H L , where each matrix is of dimension N∆ × M, where ∆ is an integer that denotes number of samples per chip. The signal model at the receive antennas are thus given by the following equation, after stacking up the received samples across all the receive antennas for the ith chip interval:

(

Note that y i = [y T i,1 , . . . , y T i,N ] T is of length N∆, and each small vector y i,n includes all the temporal samples within the ith chip interval. Meanwhile, L is the channel memory length, T is the transmitted chip vector at time il, and n i is the ((N∆) × 1)-dimensional white Gaussian noise vector with n i ∼ N (0, σ 2 I N∆ ). Note that σ 2 denotes noise variance and I N∆ is the identity matrix of size N∆ × N∆. Furthermore, in order to facilitate the discussion on the linear filters at the receiver, we stack up a block of 2F + 1 small received vectors (note that the notation of 2F + 1 suggests that we are assuming the filters to be "centered" with F taps on both the causal and anticausal side):

where 2F +1 is the length of the LMMSE equalizing filter and

where the dimensions of the matrices are given next to them. Note that to keep the notation more intuitive, we keep the subscripts at a "block" level. For instance, y i+F:i-F is the vector that contains blocks y i+F , . . . , y i-F , where each block is a vector of size N∆ × 1. The transmitted chip vector d i+F:i-F-L is assumed to be zero-mean, white random vectors whose covariance matrix is given by R dd = σ 2 d bI 2F+L+1 . We further define some more notation for future use. We define dī =d i+F:i-F-L \d i , where d i+F:i-F-L \d i denotes the submatrix of d i+F:i-F-L that includes all the elements of d i+F:i-F-L except those in d i . With this definition, we rewrite the signal model (3) as

H 0 is the submatrix in H that is associated with the subvector d i and H0 = H\H 0 . Furthermore, we define the covariance matrix of the received signal

# RECEIVERS AND CQI MEASURES FOR JE SCHEMES

In this section, we first propose a suboptimal yet computationally feasible receiver structure, the per-Walsh code joint spatial detection structure consisting of a front-end linear filter followed by joint detection across all spatial streams. We derive a class of filters that maximize the so-called constrained mutual information and show that this mutual information can act as a single CQI that characterizes the JE MIMO link. Before we discuss the per-Walsh code joint detection structure, we note that at the first glance one may be tempted to use the instantaneous mutual information of the channel I(d i+F:i-F-L ; y i+F:i-F ) as the CQI of interest. While it is indeed a single quantity that fully characterizes the MIMO link at the moment, in a frequency-selective channel, the optimal decoding needed to achieve this mutual information requires a joint sequence detection algorithm known as vector Viterbi algorithm (VVA) [20]. Unfortunately, the VVA has a computational complexity that is exponential with both the number of transmit antennas M and number of Walsh codes K, which becomes prohibitively high as M or K grows. Therefore, the channel mutual information by itself is not a good CQI measure since its associated receiver cannot be implemented in a realistic system.

To avoid these complexity issues, in this paper, we focus on a class of suboptimal receivers with the so-called per-Walsh code joint detection structure, as illustrated in Figure 3. In this structure, a front-end linear filter bank W (of size (2F + 1)N∆ × M) converts the multipath MIMO channel into an effective single-path MIMO channel in some optimal fashion. That is,

Receive antennas

Chip-to-symbol down-conversion, descrambling, despreading

# H

Joint detection (walsh code 1)

Soft bits to the decoder Joint detection (walsh code K 1 ) where the

Our idea is to use the so-called constrained mutual information I(d i ; r i (W)) as the single CQI that characterizes the MIMO link. Let us verify if this is a valid choice, that is, if there is a computationally feasible receiver associated with this choice of CQI. To this end, we note that since r i (W) sees an effective single-path MIMO channel, the orthogonality of the Walsh codes allow us to separate symbols carried on different Walsh codes, and joint detection is only needed along the spatial dimension for each Walsh code, as shown in Figure 3. Therefore, the per-Walsh code joint detection structure is computationally feasible and I(d i ; r i (W)) is a valid choice of CQI to describe this MIMO link.

Since I(d i ; r i (W)) is dependent on the filter W, one would naturally want to design the filter W such that the constrained mutual information I(d i ; r i (W)) is maximized. In the following sections, we turn our attention to the problem of optimizing the filter W, and show that this solution coincides with the LMMSE or MVDR solutions. Before we proceed, we complete the description of the signal models in Figure 3. Recall that c(i) is the scrambling code and that j = i/G is the symbol index, we define C( j) =diag{c( jG), . . . , c( jG + G -1)} as the diagonal matrix that denotes the scrambling operation for the jth symbol interval. With this nomenclature, we arrive at the output signals of the composite operations of chip-to-symbol downconversion, descrambling, and despreading on the collection of chip vectors {r jG , . . . , r jG+G-1 }:

where a k ( j) =[a k,1 ( j), . . . , a k,M ( j)] T is the transmitted symbol vector carried on the kth Walsh code for the jth symbol interval and n ∼ N (0, (1/G)W H RW). Note that in (7) we have implicitly used the facts that (a) the Walsh codes are orthonormal, that is,

, where E[•] denotes expectation operation and (•) * denotes conjugate operation.

## Optimizing W by mutual information maximization

We proceed to obtain the filter W that maximizes I(d i ; r i (W)). In order to obtain a closed-form solution, we assume d i to be Gaussian and therefore we are really maximizing the (Gaussian) upper bound of this mutual information. Note that it is well understood that the MMSE receiver is mutual information maximizing in a more general context [21] and we provide the proof for the particular MIMO-CDMA system of interest for completeness. Theorem 1. Assuming d i to be Gaussian, the conditional mutual information I(d i ; r i (W)|H) is maximized by (MC stands for maximum capacity)

For the proof, see Appendix A.

### Connection to the LMMSE or MVDR chip MIMO equalizers

The idea of transforming a multipath channel to a singlepath channel is better known as chip-level equalization of CDMA downlink, mostly using LMMSE or MVDR algorithms. Defining an error vector of z = d i -W H y i+F:i-F and an error covariance matrix R zz = E[zz H ], the MIMO LMMSE chip-level equalizer W is the solution of the following problem:

whose optimal solution is given by

LMMSE y i+F:i-F as the estimated chip vector, it is easy to see that this estimate is biased, since

An unbiased estimate can be obtained by solving instead the MIMO MVDR problem:

whose solution is

Note that one can show that the MVDR solution is a special case of the so-called FIR MIMO channel-shortening filter [1]. We proceed to show in the following corollary that both LMMSE and MVDR solutions are actually mutual information maximizing. This result shows that one cannot do better than the simple LMMSE or MVDR filter, as long as these filters are followed by joint detection in the spatial dimension.

Corollary 1. Both the LMMSE and MVDR equalizer solutions, W LMMSE and W MVDR , are mutual information maximizing.

For the proof, see Appendix B.

## Two alternative CQI measures for JE MIMO

From the discussion above, it is clear that we can use I(d i ; y i+F:i-F ) as the single CQI to describe the MIMO link.

However, the constrained mutual information I(d i ; y i+F:i-F ) is obtained with the assumption that modulation and coding are applied directly on the chip signals d i . Since a realistic CDMA systems the modulation and coding are always applied on symbol signals a k ( j), we should instead use the symbol-level mutual information I(a k ( j); t k ( j)) as the CQI of the link. To this end, note that once the front-end filter

and consequently the single-dimensional mappings are defined as MCS(I(a k ( j); t k ( j))) and FER(I(a k ( j); t k ( j))), where β k =α 2 k G is a scalar factor that translates the chip-level SNR (SNR of d i ) to the symbol-level SNR (SNR of t k ( j)). Note that here we have implicitly assumed that α 1 = • • • = α K1 , which is a reasonable assumption for most practical situations.

Alternatively, we may also use another symbol-level CQI based on the so-called generalized SNR (GSNR) [1]:

where R zz is defined above (8). With this definition of GSNR, the single-dimensional mappings are defined as MCS(GSNR) and FER(GSNR).

Remark 1. The difference between chip and symbol mutual information suggests that we may combine the filter block W and the following block (down-conversion, etc.) in Figure 3 into a composite filter block, and then directly optimize this composite filter. However, a closer examination shows that doing so increases the complexity significantly without revealing much additional insightabout the problem. The chip versus symbol mutual information discussion is analogous to the chip versus symbol-level equalization problem discussed in [15].

# RECEIVERS AND CQIS FOR PARC-TYPE SE SCHEMES

We now turn our attention to PARC-type SE schemes. In this section, we extend the successive decoding algorithm of PARC [2,3] to multipath channels, and show that in this case successive decoding achieve the constrained mutual information mentioned earlier. We also derive the link quality measures for the SE transmission similar to those for JE transmission.

## Successive decoding in the presence of multipath

In [3], a capacity achieving successive decoding procedure is developed for a memoryless GMAC (Gaussian multipleaccess channel). Here we follow the treatment in [3] and derive the successive decoding procedure in the presence of multipath, and show that in this case the successive decoding achieves the constrained mutual information I(d i ; y i+F:i-F ) we discussed in Section 3.1. Again, in the information analysis we assume that modulation and coding are directly applied on the chip signals for ease of exposition. We will show in a later subsection the changes and additions necessary for a realistic CDMA system where successive decoding and cancellation occur at symbol level. We start by rewriting the signal model of (5) as y i+F:i-F = H 0 d i + n i , where n i ∼ N (0, R), to stress that successive decoding is intended for the elements of

To this end, let there be a successive decoding algorithm that decodes d i,1 → d i,m → d i,M in that order. At each stage m, assuming that all the previous symbols d i,1 , . . . , d i,m-1 are correctly decoded, a decision variable u i,m is generated as a linear combination of the output y i and the previously decoded signals:

for 1 < m ≤ M and 1 ≤ l ≤ m -1. Note here each f m is a (2F + 1)N∆ × 1 vector known as feedforward vector and each b * m,1 is a scalar feedback coefficient (the conjugate operation * is here only for notational convenience when we move to vector-matrix representation). At each stage m, we intend to maximize the mutual information I(u i,m ; d i,m ) by optimizing C m = max fm,bm,1,...,bm,m-1

where C m denotes the maximum mutual information obtained at each stage. To solve (13), we first rewrite (12) as

where [m] ={1, . . . , m -1} and (m) ={m + 1,. . . , M} are the indices before and after m within the set {1, . . . , M}, respectively. Accordingly, partitions of H 0 and d i are defined as H 0 = [H 0,[m] , h 0,m , H 0,(m) ] and

Defining the signalto-interference-plus-noise ratio (SINR) of the (14) as

where

)), the maximum mutual information C m is achieved by maximizing the SINR in (15). However, after the obvious step of set-

) is a generalized eigenproblem [22] whose solution is given by

(m) h 0,m for any ν m > 0. Therefore, the solution of ( 13) is ) to arrive at C = M m=1 C m . What we have shown is that for MIMO-CDMA systems in a frequency-selective channel, if the transmitter can somehow have the feedback knowledge of the maximum mutual information C m for antenna m and assign a transmission rate of R m = C m on that antenna, we can design a successive decoding scheme similar to those in the memoryless channel [2,3], to achieve the constrained mutual information C = I(d i ; y i+F:i-F ). Before we proceed, we rewrite (12) in a more compact form:

where

and

and we denote the optimal solution of F and B as F SD and B SD .

### Connection between F SD and W MC

In this subsection, we show how the optimal feedforward filter F SD relates to the W MC we designed for joint detection a little earlier in Section 3.1. To this end, we note that instead of performing successive decoding directly on the received signal y i+F:i-F , we can first pass y i+F:i-F through W MC to get r i (W MC ), on which we then perform successive decoding. Similar to (17), we define the decision vector in this case as:

and find the optimal F and B (which we denote as F SD and B SD ) by maximizing C m = max F ,B I(u i,m ; d i,m ) for m = 1, . . . , M. From the derivation in Section 4.1, it is easy to see that C =I(r i (W MC ); d i ) = I(y i+F:i-F ; d i ) = M m=1 C m (note the second equality comes from Theorem 1), meaning that successive decoding after the filter W MC achieves the same constrained mutual information as direct successive decoding. In fact, we can further show in the following proposition that C m = C m and F SD = W MC F SD for certain situations. The proof is straightforward and is omitted here. Proposition 1. C m = C m . Furthermore, if the two sets of filters, (F SD , B SD ) and (F SD , B SD ), are chosen such that the decision vectors u i and u i are both unbiased2 , that is,

### Connection to the constrained MIMO LMMSE equalizer

In Section 3.1.1, we showed the connection between the mutual information maximizing filter W MC and the conventional MIMO chip equalizers W LMMSE and W MVDR . In this section, we show that similar connection can be made between the successive decoding filter pair (F SD , B SD ) and the so-called constrained MIMO LMMSE equalizer presented in [24] for a more general EDGE MIMO system where the feedback channel includes more than one effective tap. On the contrary, the constrained LMMSE equalizer for a CDMA MIMO system has only one feedback channel tap and can be viewed as a special case of [24]. The constrained LMMSE for MIMO CDMA is given by the following optimization problem with a structural constraint requiring B H =B H + I M to be lower triangular with unit diagonals:

where the error vector is defined as

We show in the following proposition that the constrained LMMSE solution is indeed the same as the successive decoding solution with unbiased output.

# F r i

Chip-to-symbol down-conversion, descrambling, despreading Proposition 2. If the successive decoding filter pair (F SD , B SD ) is chosen such that the decision vector u i is unbiased, that is,

Proof. See [24] for details about the solution of (20).

Remark 2. Throughout our discussion, we have used the argument that as long as the rate assigned on antenna m is below C m : R m ≤ C m , we can provide the correct decision on d i,m to drive the successive decoding process. However, in a practical system many factors (such as Doppler shift, imperfect feedback, etc), can lead to decision errors on d i,m which propagates through the successive decoding process. From a receiver design point of view, the constrained LMMSE problem of ( 20) can be modified to mitigate the impact of error propagation. However, it is much harder to account for these error propagation effects in the information-theoretical analysis of the successive decoding approach.

## Successive decoding at symbol level

In the discussion of successive decoding above, we have assumed that modulation and coding are directly applied on the chip signals d i . In Figure 4, we show the changes necessary to perform successive decoding at symbol level for a realistic CDMA system. Here we assume

for simplicity of notation. In this case, the feedforward filter F still operates on chip signals y i+F:i-F whereas the feedback filter α 1 B (α 1 is needed to ensure correct symbol amplitude) operates on estimated symbol signals { a k,m ( j)} instead. Note that unlike Figure 3, the output of the despreading blocks v 1 ( j), . . . , v M ( j) is organized into M vectors of size K 1 × 1 along the spatial dimension.

## CQI measures for PARC-type systems

Since each antenna is separately encoded, the link-to-system mapping for PARC-Type systems is much easier than in the case of joint space-time encoding. Again we have two alternative CQIs for the link-to-system mapping purpose. One can use the symbol SINR given by

as the CQI to generate the mapping as FER(γ m,k ) for each antenna m. Recall from Section 3.2 that β k =α 2 k G is a scalar factor that translates the chip-level SINR to the symbol-level SINR. Alternatively, one can use the symbol-level mutual information given by

as the CQI to generate the mapping as FER(C m,k ) for each antenna m.

# SIMULATION RESULTS

The algorithms described in this paper are evaluated in a realistic link-level simulator conforming to the CDMA2000 1xEV-DV standard [19,25]. The simulation results are presented in three subsections. In the first subsection, we compare the performance results of different receiver algorithms assuming a simple coded VBLAST [8] transmission scheme.

In the second subsection, we present some preliminary link throughput results for both coded VBLAST and PARC schemes with link adaptation. Lastly, we show the effectiveness of the two CQI measures discussed in Section 3.2 when coded VBLAST scheme is used at the transmitter. Note that although we have focused on the coded VBLAST and PARC schemes in this paper, the algorithms and concepts described here can be extended to other more complicated MIMO transmission schemes.

## Receiver performance comparison

We assume the coded VBLAST [8] scheme at the MIMO transmitter. In the coded VBLAST scheme, the coded frame is simply split across the M transmit antennas after modulation, therefore it can also be viewed as a simple form of space-time code. Here we compare three receivers: LMMSE with separate detection, LMMSE with joint detection, and constrained LMMSE as shown in (20) with separate detection. Note that, in this case, successive decoding is not possible since the transmit signals are coded across all antennas. Therefore, the symbol estimates { a k,m ( j)} in Figure 4 cannot be reconstructed from decoder outputs and should be regenerated successively from the signals v 1 ( j), . . . , v M ( j).

Without going into too much detail, we state that there are two approaches for generating these symbol estimates: harddecision or soft-decision estimates. In the simulation results presented here, we have used conditional mean-based soft estimates that are similar to those used in [26]. THE simulation parameters are tabulated in Table 1 and the simulation result is shown in Figure 5. Note that the traffic Ec/Ior on the x-axis stands for the percentage of the transmit power that is assigned to each active Walsh code. Not surprisingly, the LMMSE filter followed by joint detection performs the best, since it retains the constrained mutual information as we discussed earlier. Meanwhile, even though in this case the constrained LMMSE filter as defined in (20) does not achieve the maximum mutual information without successive decoding, it loses only about 0.5 dB against the joint detector.  

## Link throughput with link adaptation

In order to demonstrate the performance of MIMO schemes with link adaptation, we derive the parameters of each packet transmission from a table consisting of 4 sets of parameters, each set being known as a modulation and coding scheme (MCS). This is illustrated in Table 2. Table 2 is a subset of the 5-level table used in HSDPA [27]. In order to achieve these spectral efficiencies approximately, we use the set of parameters shown in Table 3 in the context of the 1X-EVDV packet data channel. Note that we have taken necessary measures to make sure the comparison is fair in the sense that the throughput results of the two schemes are obtained with the same allocated bandwidth and transmission time.  The throughput comparison between coded VBLAST and PARC is shown in Figure 6. For the coded BLAST scheme, the per-Walsh code joint detection is used at the receiver and, on the other hand, the successive decoding method is used for the PARC scheme. Note that most of the other simulation parameters are the same as those in Table 1, except that here we fixed the traffic Ec/Ior and let the Geometry vary. Of course, the MCS is also a variable in this case due to link adaptation. Perfect feedback with no delay is assumed for the link adaptation, that is, the transmitter changes the MCS instantaneously at the end of every frame. The results show that coded VBLAST outperforms PARC slightly in these simulations. On the other hand, PARC has more flexibility with respect to link adaptation, which is not fully utilized in this simulation, where only a small set of MCS schemes is used. More granularity in the link adaptation might lead to different results. Another advantage of PARC is that the existing HARQ mechanisms in 1xEV-DV are readily applicable in PARC, as shown in [28].

Remark 3. In Sections 3 and 4, we have assumed Gaussian modulation in calculating the mutual information-based CQI. However, since 16-QAM or QPSK modulation is used in practice, using the Gaussian mutual information (here we denote as C Gau ) may portray an overly optimistic picture of the channel and thus mislead the BS in transmitting at a rate that is above the "true" information rate of the channel under the additional constraint of the practical constellation. To see this, we assume a measured C Gau = 3.3 bps/Hz at the MS. According to Table 2, we can support the fourth MCS scheme (MCS4) which has a coding rate of 0.75 and a 16-QAM modulation. However, if we recalculate the mutual information of the channel under the additional constraint of 16-QAM modulation (here we denote as C QAM ) [29], it may happen that C QAM = 2.8 bps/Hz, which means that transmitting with MCS4 will always result in a packet error and we should be using MCS3 instead.

In the simulation, we have devised two mechanisms to avoid the negative effects of the overly optimistic Gaussian CQI measure.

(i) By simply multiplying C Gau with a scaling factor α < 1, we can make the CQI estimate a bit more conservative. This scaling can also account for other practical imperfections such as channel estimation error, Doppler, and so forth. Typically α = 0.8 to 0.9.

(ii) Adopt a confirmation process such that after an MCS scheme is selected, the mutual information under the additional constellation constraint of that particular MCS is recalculated. If this constellation-constrained mutual information falls below the information rate prescribed by the current MCS scheme, move one grade up in the MCS table   and pick the next MCS scheme with lower information rate. This confirmation process repeats until the first MCS scheme in the table, or until we find an MCS scheme where the constellation-constrained mutual information is greater than the information rate associated with this MCS scheme.

## Short-term FER (CQI) curves

In this section, we use computer simulations to obtain the FER(CQI) curves as the first step of link-to-system mapping for the JE coded VBLAST scheme. As mentioned earlier, both the GSNR and the constrained mutual information I(d i ; y i+F:i-F ) measures enable us to characterize the MIMO link by a single CQI, so that a multidimensional mapping can be avoided. In the simulations, we assume the spatial channel model (SCM) specified by [30]. Particularly, the urban macro scenario [30] is implemented. In the SCM model, the channel delay profile itself is a random vector with a different multipath channel profile for each realization. In our simulation, we first generate 10 such independent realizations of delay profiles and then generate thousands of channel realizations for each delay profile.

At the receiver, we use the LMMSE receiver followed by the per-Walsh joint detection algorithm. The parameters of the link are illustrated in Table 1 (except we set Geometry = 0 dB in the simulations presented here). The modulation and coding scheme used is MCS1. Figure 7 plots the FER as a function of the instantaneous value of the GSNR, while Figure 8 provides a similar plot with respect to the constrained mutual information.

One observes that there are 10 curves in each of the plots, representing 10 independent realizations of channel delay profiles. Ideally, if a CQI measure perfectly characterizes the MIMO channel at the moment, then the FER(CQI) curved should be independent of the channel delay profile and all 10 curves should overlap. For practical CQI measures such as the GSNR and the mutual information measure proposed in this paper, we note that the lesser the variation of the curves with different realizations, the more effective the measure is as an indicator of link quality. Given this criterion, the constrained mutual information is seen to be more suitable than the GSNR. These are, however, preliminary results requiring further investigation since we have not accounted for other system-level issues such as HARQ in these simulations.

# CONCLUSION

In this paper, we investigate receiver designs for the jointly encoded (JE) and separately encoded (SE) types of MIMO transmission. For the JE transmission, we develop a per-Walsh code joint detection structure consisting of a frontend linear filter followed by joint symbol detection among all the streams. We derive a class of filters that maximize the so-called constrained mutual information, and show that the conventional LMMSE and MVDR equalizers belong to this class. This constrained mutual information also provides us with a quantity describing the link quality, similar to the notion of GSNR. For the case of SE transmission, we extend the successive decoding algorithm of PARC to multipath channels, and show that in this case successive decoding achieves the constrained mutual information. Finally, the algorithms and concepts developed in the paper are evaluated in a realistic CDMA 1xEV-DV link simulator with and without link adaptation.

# APPENDICES A. PROOF OF THEOREM 1

Since d i is Gaussian, r i (W) is also Gaussian. One can write out this mutual information as 3  where I M is the identity matrix of size M × M. The direct optimization of (A.1) is difficult, given that W is a (2F + 1)N∆ × M matrix. Here we resort to the data processing lemma [23] to provide an upper bound on I(d i ; r i (W)|H) and then show the bound is achievable. To this end, we note that since r i (W) = W H y i+F:i-F , d i → y i+F:i-F → r i (W) forms a Markov chain, conditioned on the knowledge of the channel H. Therefore, by the data processing lemma, the inequality 

# B. PROOF OF COROLLARY 1

It is obvious for W MVDR since all we need to do is to set A = (H H 0 RH 0 ) -1 and apply Theorem 1. On the other hand, with the help of matrix inversion lemma [31] one can rewrite W LMMSE as

and then set A = σ 2 d (I M + σ 2 d H H 0 R -1 H 0 ) -1 to complete the proof.

# ACKNOWLEDGMENTS

We would like to thank Dr. Dung Doan of Qualcomm for helpful discussions, and Chris Jensen of Nokia Research Center for proofreading the revised draft. We are also grateful to the anonymous reviewers whose comments greatly improved the presentation of this paper.

