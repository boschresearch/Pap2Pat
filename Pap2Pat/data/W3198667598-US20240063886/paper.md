# I. INTRODUCTION

The use of millimeter wave (mmWave) carrier frequencies is one of the main pillars of current and future cellular wireless system [1], [2]. Indeed, the large bandwidths available at mmWave can greatly contribute to provide the huge data rates that are requested to implement current and future ultra-broadband mobile services. In cellular generations prior to 5G, mmWaves had not been considered due to the increased path loss with respect to the sub-6GHz frequencies, which made them clearly unsuited for communication over distances typical of wireless cellular systems. Additionally, propagation at mmWave happens only through direct links and/or onehop reflections, and this poses another further challenge for their use with respect to sub-6 GHz frequencies, where instead multiple reflections and diffraction take place. Despite these difficulties, in recent years mmWave carrier frequencies have been considered for adoption in wireless cellular communications mainly for two reasons: (a) the use of radio cells of small size has made shorter the typical distance of a wireless cellular link, thus implying that the increased path-loss introduced at mmWave carrier frequencies may become manageable; and (b) the development of multiple antenna communications has led to antennas with an effective aperture that can be practically independent of the wavelength, thus potentially overcoming the path-loss limitation. However, in order to be able to really overcome the large path loss and make mmWave links work reliably, narrow beams must be used so as to concentrate radiated energy along those spatial directions associated with the existing line of sight path and/or one hop reflected paths. Otherwise stated, while at sub-6GHz frequencies communication may get started even with fairly broad beams, at mmWave narrow beams are to be used along some channel and geometry dependent directions. The problem of finding those beamforming directions is called beam alignment (BA). More precisely, BA is a task that must be accomplished at mmWave in order to ensure that an active link with a sufficiently high signal strength can be established between the intended transmitter and the intended receiver. It is a necessary task that must be executed before actual data communication takes place.

The fifth generation of wireless networks has also seen the introduction of the so-called massive MIMO technology [3], which enables the simultaneous transmission to several UEs using the same time-frequency slot, and with a minimum amount of interference. Although providing excellent multiplexing gains, unfortunately this technology does not solve the "cell-edge" problem: when a UE is located in between the reference base station (BS) and an interfering BS, it experiences a poor signal-to-interference-plus-noise ratio (SINR), and, thus, interference management algorithms are to be run, which eventually decrease the spectral efficiency. One solution aimed at overcoming this problem is the so-called cell-free massive MIMO (CF-mMIMO) network deployment, where the macro-BSs are substituted by several APs, having a lower number of antennas and lower complexity [4]- [6]. The APs are assumed to be connected to a central processing unit (CPU) through some wired or wireless connection, and can jointly serve the UEs using the same time-frequency slot. A wise association between the APs and the UEs can be realized, letting each UE be served by a certain number of APs, typically the ones that are closer to the UE of interest or the ones with the highest large scale fading coefficient. This latter deployment is called also "user-centric", since the set of APs serving a particular UE forms a cluster with the UE at its center. CF-mMIMO user-centric deployments permit to alleviate the aforementioned cell-edge problem, since, given the large number of distributed APs, there is large likelihood that each UE happens to be located very close to at least one AP, which ensures thus a good SINR and a reliable connection. CF-mMIMO architectures are currently widely investigated and are credited to be one of the key network architectures for beyond-5G wireless networks [7].

Most of the research on CF-mMIMO has been so far mainly carried with reference to sub-6 GHz frequencies, while fewer studies (such as, for instance, [8]- [10]) have addressed CF-mMIMO systems operating at mmWave carrier frequencies. Nonetheless, it is anticipated that in crowded areas with high-demand for mobile broadband services both a large number of distributed antenna (such as CF-mMIMO) and high-carrier frequencies will be needed, thus implying that CF-mMIMO at mmWave will be one of the typical deployments for future beyond-5G and 6G scenarios. This paper investigates the problem of BA in a scenario wherein multiple APs and multiple UEs use the same frequency band. As illustrated in the following review of the state of the art, the vast majority of existing papers on BA algorithms assume single-user settings wherein a single UE and a single AP (or BS) have to align their beams: applying such procedures in a multi-UE, multi-AP setting would results in a lengthy and non-feasible procedure where each AP-UE pair should align the beams with the remaining devices being silent. In this paper, instead, a procedure for simultaneous BA for multiple UEs and multiple APs is proposed and analyzed.

## A. Previous contributions

The problem of BA for wireless networks operating at mmWave frequencies has received considerable attention in the recent past. Paper [11] considers the problem of BA in a scenario with a single transmitter and a single receiver. It exploits the use of dual-polarized antennas, so that orthogonal polarizations can be sounded in parallel, and proposes a soft-decision algorithm under the assumption that the channel is Ricean-distributed with large Ricean K factor and that there is a poor scattering environment. In [12] the authors propose a protocol for fast BA. The paper focuses on a single-user environment and, instead of sequentially scanning the space with narrow beams, exploits multi-finger beams so as to reduce the time needed to perform BA. A similar approach is also taken in [13], [14]; these papers focus on a system using a multi-carrier modulation and a single-carrier modulation, respectively, and propose to use compressive sensing to perform BA in a single UE, single BS scenario, using transmit and receive pseudo-random multi-finger beamformers. Paper [15] develops a theoretical performance analysis of the BA process for both exhaustive search and hierarchical search under the assumption of a single BS and a single UE. In particular, the asymptotic expression (in the limit of large length of the training period) of the misalignment probability is derived for both mentioned search scheme and under the assumption that both the UE and the BS have a finite cardinality beamforming codebook. In [16], authors consider the problem of robust BA based on the knowledge of the location of the AP and the UE. Since the location information can be affected by some estimation error, a robust algorithm based on Bayesian team decision is proposed. Specifically, the BA problem is recast as a decentralized coordination problem where both the BS and the UE try to achieve alignment on the basis of individual, but correlated, observations. Paper [17] considers the optimization of the share of time devoted to BA and the share of time dedicated to actual data communication, with the aim of maximizing the system throughput, and derives the optimal beam search parameters adopting the framework of Markov decision processes. The analysis reveals that the BA bisection search algorithm achieves better performance than BA iterative and exhaustive search algorithms. In [18] authors formulate the BA problem as a sparse encoding and phaseless decoding problem. The scenario that is here considered is with one BS and one AP, and the proposed algorithm can perfectly recover the support and magnitude of the sparse signal (uniquely associated to the beams' directions) in the noiseless case. In [19], instead, a two-stage procedure is proposed for BA. In the first stage, the algorithm explores and trains all candidate beam pairs, and, then, eliminates a set of less favorable pairs learned from the received signal profile. In the second stage, the algorithm takes an extra measurement for the each of the survived pairs and combines with the previous measurement to determine the best one. Also this paper, despite good performance, focuses however on a point-to-point single link. Papers [20], [21] are among the first to tackle the problem of BA in a multiuser scenario. However, only one BS is considered, and so the proposed procedures are not applicable in a scenario with multiple APs as in a CF-mMIMO deployment. Paper [22], instead, again for a point-to-point link, proposes to leverage knowledge of position and orientation of the transmit and receive antenna arrays to perform BA using machine learning. In [23], the related problem of beam switching is considered: beam switching happens when BA has been already accomplished, and, due to UE mobility and/or to changes in the surrounding scenario, a beam switch is required to ensure continuity of the communication.

### B. Paper contribution

This paper, whose preliminary, reduced-length, versions can be found in [24], [25], to the best of our knowledge, is the first to consider the problem of BA in a multi-UE multi-AP environment, proposing a BA procedure wherein all the UEs are capable of simultaneously estimating the direction of departure (DoD) and direction of arrival (DoA) of the strongest beam coming from the APs in the neighbors. The content of this paper thus enables cell-free coordinated multi-point transmission in a wireless network operating at mmWave and with several distributed APs. Specifically, the contribution of this work may be summarized as follows. First of all, a methodology for performing BA in a multi-AP, multi-UE setup, wherein all the APs and all the UEs operate using the same frequency band, is developed. The methodology consists of a protocol involving the CPU, the UEs, the APs and a macro-BS managing a reliable control channel at sub-6GHz frequency. The proposed BA procedure is based on a one-way transmission from the APs, with the UEs operating in listening mode and estimating the DoA and DoD of the strongest beam from the surrounding APs. This is in sharp contrast with the majority of existing BA procedures, that rely on several steps where the UE and the AP iteratively refine their beams.

In order to make the UEs capable to discriminate the signals coming from different APs, these must transmit on disjoint set of orthogonal channels. Since, in general, the number of APs is much greater than the number of available sets of orthogonal channels, a further contribution of this paper is an algorithm aimed at assigning the sets to the APs, with the objective of minimizing the mutual interference among APs using the same set of orthogonal carriers. Two different BA algorithms, to be implemented at the UE, are proposed, one inspired from [13], and one totally original. The study is finally completed by a thorough simulation-based performance study, in terms of probability of correct detection of the couple (DoA, DoD) of the strongest beams, and in terms of achievable spectral efficiency. The obtained results will show the effectiveness of the proposed procedure.

### C. Notation

In the following, lower-case and upper-case non-bold letters are used for scalars, a and A, lower-case boldface letters, a, for vectors and upper-case boldface letters, A, for matrices. The transpose, the inverse, the conjugate and the conjugate transpose of a matrix A are denoted as A T , A -1 , A * and A H , respectively. The i-th row and the j-th column of the matrix A are denoted as (A) (i,:) and (A) (:,j) , respectively. The norm of a vector a is denoted as a . The N -dimensional identity matrix is denoted as I N , the N × M matrix with all ones is 1 N ×M and the the N × M matrix with all zeros is 0 N ×M . The complex circularly symmetric Gaussian random variable with mean µ and variance σ 2 is denoted as CN (µ, σ 2 ). The set of the complex N -dimensional vectors is denoted as C N and i is the imaginary unit.

## II. SYSTEM DESCRIPTION

Consider a CF-mMIMO system where M APs simultaneously serve K UEs on a shared channel. We focus on the BA procedure and, for the sake of simplicity, consider a bi-dimensional layout 1 . We use the following notation:

-N UE denotes the number of antennas at the generic UE.

-N AP denotes the number of antennas at the generic AP.

n UE < N UE denotes the number of RF chains at the generic UE.

n AP < N AP denotes the number of RF chains at the generic AP.

The number of antennas and RF chains is taken constant for all the APs and all the UEs to simplify notation, but extension to the general case where each AP and UE has an arbitrary number of antennas and RF chains is straightforward. Both the APs and the UEs are equipped with uniform linear arrays (ULAs) with random orientations, and the steering angles are assumed to take values in the range [-π/2, π/2]. See Fig. 2 for a sample scenario realization. 

### A. Transmission format

It is assumed that the adopted modulation format is the orthogonal frequency division multiplexing (OFDM); the OFDM symbol duration is denoted by t 0 , B denotes the overall available bandwidth, while the subcarrier spacing for the OFDM signal is denoted by ∆f . This implies that the number of subcarriers is N C = B/∆f . The OFDM symbol duration is 1/∆f + τ CP , with τ CP the length of the cyclic prefix. The BA phase will span T beacon slots (a terminology borrowed from [13]), each made of S consecutive OFDM symbols. See also Fig. 1 for a graphical representation of the considered frame format.

### B. Channel model

The downlink channel between the m-th AP and the k-th UE in the s-th beacon slot is represented by an (N UE × N AP )-dimensional matrix-valued linear time invariant (LTI) system with impulse response

In the above equation, we have that -L k,m denotes the number of paths that contribute to the channel between the k-th UE and the m-th AP. This number depends on the geometry of the system. Usually in a poor scattering environment typical of mmWave frequencies we have that

k,m, is the complex gain associated to the -th path in the s-th beacon slot. We assume α a AP (•) and a UE (•) are the ULA array responses at the AP and at the UE, respectively.

Assuming half-wavelength spacing for the array elements, they are expressed as a AP (ϕ) = [1, e iπ sin ϕ , . . . , e iπ(N AP -1) sin ϕ ] T , a UE (θ) = [1, e iπ sin θ , . . . , e iπ(N UE -1) sin θ ] T , -τ k,m, is the propagation delay associated to the -th path.

Notice that while the complex gains α (s) k,m, depend on the beacon slot index s, this does not happen for the other parameters, such as the number of paths, their associated delays, and the corresponding DoAa and DoDs, which typically vary over much larger timescales than the complex gains associated with propagation paths. Otherwise stated, α (s) k,m, accounts for the fast small-scale fading, while the remaining channel parameters are tied to large-scale variations.

## III. BEAM ALIGNMENT PROCEDURE PRELIMINARIES

### A. The data-patterns

Before the BA procedure starts, a set of resources, referred to as data-patterns, are to be defined and assigned to the APs. Obviously, since in a large system the number of orthogonal data-patterns can be reasonably assumed to be smaller than the number of APs, the same datapattern is to be reused across the network. We will tackle later this issue.

Two different types of data-patterns will be considered in this paper. With regard to the former type, we define as data-pattern a set of subcarriers and beamforming vectors, which the APs use to transmit constant signals. Since each AP is equipped with n AP RF chains, i.e., it can simultaneously transmit n AP data streams using different beamforming vectors. In order to permit data stream separation at the UEs without having knowledge of the AP locations and antenna array orientation, it is needed that the transmitted data streams are orthogonal before beamforming. One way of achieving this is through the use of non-overlapping subcarriers for the parallel data-streams. Denoting by Q the number of subcarriers assigned to each AP RF chain, one can easily realize that the number of available different data-patterns is

the corresponding D data-patterns will be denoted by D 1 , . . . , D D . The generic set D d will thus specify the Q subcarriers and the beamformers to be used in each beacon slot on a certain RF chain of a certain AP. More precisely, letting L d,s,i and U d,s,i denote the set of Q subcarriers and the set of transmit beamformers, respectively, to be used by the APs that are assigned the d-th data-pattern on the i-th RF chain, the data-pattern D d is in this case formally described as

Since, as already highlighted, APs are assumed to transmit a constant signal using the above defined data-patterns, we refer to them as pilot-less data-patterns.

The latter definition of data-pattern, by allowing the transmission of modulated signals, leads to a larger number of orthogonal data-patterns, and permits to increase the distance between conflicting APs that will have to be assigned the same data-pattern, eventually resulting in better performance. Precisely, in each beacon slot, APs assigned the same pilot-less data-pattern may be differentiated by allowing them to transmit orthogonal pilots of length S. Since up to S different orthogonal pilots of length S can be generated, this strategy increases to SD the number of available orthogonal data-patterns. The -th pilot sequence, φ say, of length S is in particular defined as

and fulfills the relation φ H φ = Sβδ( -), with β > 0 the power transmitted by the APs in each beacon-slot and on each subcarrier. This latter type of data-pattern will be named pilot-based data-patterns. Clearly, the pilot-less definition can be seen as a particular case of the pilot-based definition where φ (i) = 0, ∀i = 1, . . . , S, = 1, . . . , S. For this reason, in the following we will describe the BA procedure assuming the more general case of pilot-based data-patterns and will assess the performance difference between the two types of data-patterns in Section VII.

### B. Location-based data-patterns assignment algorithm

We now discuss how the data-patterns are to be shared among the APs in the general case in which the number of APs is larger than the number of available data-patterns. In general, the distance between the APs using the same set of resources should be as large as possible. We thus propose a location-based (LB) data-pattern assignment in order to reduce the BA contamination in the system. The proposed procedure uses the well-known k-means clustering method [26],

i.e., an iterative algorithm that is able to partition APs into disjoint clusters. Defining the centroid of each cluster as the mean of the positions of the APs in the cluster, the algorithm, accepting as input the APs positions and the number of data-patterns that we generically denote as D, is summarized in Algorithm 1 and operates as follows:

a. M/ D centroids are chosen so that they approximately form a regular grid over the considered area. e. Once the AP clusters have been defined, data-patterns are to be assigned to the APs according to the following strategy. We characterize the APs in each cluster with their position relative to the centroid of the cluster to which they belong. Then, we assign the first data-pattern to the AP in each cluster that has the largest latitude (i.e. the most northern one); the second data-pattern to the AP in each cluster with the second largest latitude, and so on. The assignment procedure stops when all the the APs in the system have been assigned a data-pattern.

Note that D = D when pilot-less data-patterns are used, and D = SD for the case in which pilot-based data-patterns are adopted.

# Algorithm 1 Location-based data-patterns assignment algorithm

1: Allocate M/ D centroids so as to form an approximately regular grid over the considered area.

2: repeat 3:

Assign each AP to the nearest centroid with the constraint that no more than D APs are associated to the same centroid.

# 4:

Compute the new positions of the centroids averaging over the positions of the APs belonging to the same cluster.

5: until convergence of the positions of the centroids or maximum number of iterations reached.

6: Assign the first data-pattern to the AP in each cluster that has the largest latitude (i.e.

the most northern one); assign the second data-pattern to the AP in each cluster with the second largest latitude. Continue until all the the APs in the system have been assigned a data-pattern. 

## C. Timing of the beam alignment procedure

Similarly to many other papers dealing with the BA problem at mmWave, we assume that a general frame synchronization information is available in the system. This can be ensured by exploiting the fronthaul connection between the APs and the CPU, and by using a control-plane connection with the UEs at a sub-6 GHz carrier frequency. The BA procedure and the subsequent user association phase is made of the following steps: GHz control channel.

Refer to Fig. 3 for the temporal diagram of the proposed BA procedure.

## IV. BEAM ALIGNMENT SIGNAL MODEL

We are now ready to provide the full details about the signal model.

### A. Time-continous model

Let us focus on the signal transmitted in the s-th beacon slot, i.e. for t ∈ [st 0 , (s + 1)t 0 ]. The baseband equivalent of the signal transmitted in the s-th beacon slot by the m-th AP can be expressed through the following N AP -dimensional vector-valued waveform:

where x m,s,i (t) is the signal corresponding to the i-th data stream from the m-th AP in the s-th beacon interval; the N AP -dimensional vector u m,s,i is the corresponding transmit beamformer 3 .

2 Remember that the number of data-patterns is either D, if the pilot-less definition is used, or SD, if the pilot-based definition of data-pattern is used. 3 Notice that we are here implicitly assuming that the transmit beamformer is kept constant over an entire beacon slot, i.e. for S consecutive OFDM symbols.

The signal received in the s-th beacon slot at the k-th UE, before the receive beamformer is applied, can be easily shown to be written as

with g

k,m, ,s,i = a H AP (θ k,m, )u m,s,i and z k,s (t) an N M S -dimensional vector waveform representing the AWGN contribution at the k-th UE receiver in the s-th beacon interval.

The k-th UE can apply n UE different receive beamforming vectors to the received signal (5).

Denoting by v k,s,j the j-th beamformer (with j = 1, . . . , n UE ) used by the k-th UE in the s-th beacon slot, the following set of observables is available at the k-th UE after beamforming:

k,m, ,s,i g

for j = 1, . . . , n UE , with g

. The waveforms y k,s,j (t), for all j, undergo the usual OFDM receiver processing, and every OFDM symbol in y k,s,j (t) is converted into an N C -dimensional vector. Focusing on the generic p-th OFDM symbol, and letting s(p) = p/S denote the beacon slot index associated with the p-th OFDM symbol, the A/D conversion leads to the N C scalar entries Y k,p,j (0), . . . , Y k,p,j (N C -1).

In particular, it is easy to see that the q-th entry of such vector, corresponding to the discrete-time sample on the q-th subcarrier, is expressed as

where X m,p,i (q) is the q-th data symbol transmitted in the p-th OFDM slot on the i-th transmit RF chain, Z k,p,j,i (q) contains the AWGN contribution and H

k,m (q) is the matrix-valued Fourier transform of the channel impulse response H (s) k,m (τ ) computed at the frequency q/(t 0 ), i.e.,

As already said, during the BA phase with pilot-based data-patterns, each AP transmits a pilot sequence that allows to distinguish APs using the same data-pattern. Otherwise stated, the mth AP transmits X m,p,i (q) = √ βe i φ (m) (p mod s) , where (m) is the index of the pilot sequence assigned to the m-th AP, on its assigned subcarriers for T consecutive beacon slots. Assuming that m-th AP uses the data-pattern D d , this implies that q ∈ L d,s,i , with s = 1, . . . , T . Now, in order to perform direction estimation of the strongest beams from nearby APs, each UE can rely on the knowledge of the data-patterns D 1 , . . . , D D , and of the orthogonal pilot sequences φ 1 , . . . , φ S . Based on this information, it has to determine the DoA and DoD of the strongest multipath components to be used for data communication. Notice that no information on the APs location or on the network topology is needed at the UE. The UE will simply determine the strongest directions for the data sensed on each of the system defined data-patterns.

### B. Directions discretization and pseudo-random beamforming codebooks

The DoAs and DoDs, ϕ k,m, and θ k,m, in Eq. ( 1), respectively, take continuous values, but in the BA procedure we use the approximate finite-dimensional (discrete) beamspace representation [27]. We thus consider the discrete set of DoDs and DoAs

and use the corresponding array responses F AP = a AP ( θ) : θ ∈ Θ and F UE = {a UE ( ϕ) : ϕ ∈ Φ} as a discrete dictionary to represent the channel response. For the ULAs considered in this approach the dictionaries F AP and F UE , after suitable normalization, yield orthonormal bases corresponding to the columns of the unitary discrete Fourier transform (DFT) matrices W N AP and W N UE defined as

with N ∈ {N AP , N UE }. We thus introduce the notation:

The vector u m,s,i , to be used at the m-th AP in the s-th beacon slot and on the i-th RF chain, is defined by the data-pattern. More precisely, letting A d ∈ {1, 2, . . . , M } denote the set of APs that have been assigned the d-th data-pattern, u m,s,i follows

i.e., all the APs using the d-th data-patterns in the s-th beacon slot and on the i-th RF chain use the transmit beamformer d d,s,i . We will use pseudo-random multi-finger transmit and receive beamformers [12]- [14]. The pseudo-random beamformers transmitted by the APs in the system during the T beacon slots is defined as the collection of sets C AP = {U d,s,i , d = 1, . . . , D, s = 1, . . . , T, i = 1, . . . , n AP }, where U d,s,i is the angle domain support, i.e., the subset of quantized angles in the virtual beam space representation. We assume |U d,s,i | = ν AP ≤ N AP , ∀ d, s, i and

√ ν AP , where 1 U d,s,i is the N AP -dimensional vector with 1 at positions in the support set U d,s,i and 0 elsewhere. The pseudo-random beamforming codebook used at the UEs can be locally customized, i.e., the k-th UE can locally choose its own combining codebook defined by the collections of sets C

(k) UE = {V k,s,j , s = 1, . . . , T, j = 1, . . . , n UE }, where V k,s,j is the angle domain support defining the directions from which the k-th UE collects the signal power in the s-th beacon slot and on the j-th RF chain. We assume

√ ν UE , where 1 V k,s,j is the N UE -dimensional vector with 1 at positions in the support set V k,s,j and 0 elsewhere.

The main mathematical symbols used in this paper are summarized in Table I.

## V. SIGNAL PROCESSING AT THE UE FOR BEAM ALIGNMENT

Given the definitions in Section IV, Eq. ( 7) can be shown to be written as

k,m (q)u m,s(p),i X m,s(p),i (q) + Z k,p,j,i (q) .

Since each data-pattern adopts a disjoint set of subcarriers, the UE can operate on D different sets of observables, isolating the contribution from each AP transmit RF chain. The d-th set of observables at the k-th UE, that we denote by

k , is thus expressed as

Based on the above data, the following averaged quadratic observable is built:  Based on data in (14), two different algorithms are here proposed in order to extract the information on the DoA and DoD of the strongest path from the closest AP using the d-th data-pattern and the -th pilot sequence.

### A. Processing based on stacked collection of observables (SCO)

This algorithm is inspired by the one in [13] for a single-AP system. First of all, at the k-th UE the measurements in Eq. ( 14) are collected for all the values of i, j and s and grouped into the following vector:

and form the (n AP n UE T × N AP N UE )-dimensional matrix

Note that the matrix

k depends only on the beamforming vectors used in the d-th datapattern and not on the pilot sequences used by the APs.

Based on the above notation, the following optimization problem can be considered:

The solution ξ

to Problem ( 18) is a (N AP N UE )-dimensional vector that can be arranged in a can be associated to the second strongest path and so on. The (convex) optimization problem ( 18) is generally referred to as Non-Negative

Least-Squares (NNLS), and has been well investigated in the literature [28]- [30]. In terms of numerical implementation, the NNLS can be posed as an unconstrained LS problem over the positive orthant and can be solved by several efficient techniques such as Gradient Projection or Primal-Dual techniques with an affordable computational complexity, generally significantly smaller than compressed sensing techniques [31], [32].

### B. Processing based on matrix-valued collection of observables (MCO)

The measurements in ( 14) can be collected for all the values of i, j and s and grouped in the

whose generic entry is

where I h,h is one if the h -th transmit direction at the AP and the h-th receive direction are active when the measurements leading to c

k,i,j,s are made. Given the matrix C

, the positions of its largest entry is an indicator of the dominant path between the k-th UE and the AP using the d-th data-pattern and the -th pilot sequence; likewise, the second largest entry can be associated to the second largest path and so on. In the MCO algorithm, no optimization problem is to be solved to obtain the largest entry of matrix C (d, ) k

. The complexity of the MCO procedure is thus considerably lower than the SCO procedure.

## VI. DATA TRANSMISSION PHASE

Once the BA procedure detailed in Section III is over, each UE knows the estimates of the strongest (DoA, DoD) pairs, a strength indicator, the data-pattern and the pilot index on which each of these estimates were obtained. Otherwise stated, if pilot-less data-patterns are used, the k-th UE has the following information

where ρ 

d, is the strongest path strength indicator estimated at the k-th UE on the d-th datapattern and on the -th pilot sequence, and, again, h k,d, , h k,d, describe the position of this maximum. Now, association between the APs and the UEs is to be performed. Optimal association is a complicated combinatorial task that is out of the scope of this paper. We will thus use a simple association rule, by assuming that each UE is associated to the N D APs for which the largest strength indicators have been estimated. More precisely, when the BA procedure is over, each UE announces to the network, using a reliable sub-6GHz feedback channel, its position, its ID, and the IDs of the N D data-patterns corresponding to the N D largest estimated strength indicators. The network gathers such information and associates each UE to the N D closest APs that are using the data-patterns whose IDs have been announced by the UE. The UE-AP resulting association is broadcasted to the UEs using the downlink sub-6 GHz control channel and to the APs using the fronthaul connection with the CPU. Information on the beam to be used is also communicated to the APs. In particular, the AP in A d k,n using the k,n -th pilot sequence and nearest to the k-th UE, uses the h k,n -th column of the matrix W N AP to communicate with the k-th UE; similarly, the k-th UE uses the h k,n -th column of the matrix W N UE to communicate with the AP, and this assignment is made for n = 1, . . . , N D . Accordingly, if we denote by u k,m the beamforming vector used at the m-th AP to communicate with the k-th UE and by v k,n the n-th beamforming vector at the k-th UE, we have

with m is the index of AP using the d k,n -th data-pattern and the k,n pilot sequence which is the nearest to the k-th UE, and

For future reference, we also introduce the binary-valued association variable a k,m , which is 1 if the k-th UE is served by the m-th AP and 0 otherwise.

### A. Downlink data transmission

On the downlink, the signal transmitted by the m-th AP on the q-th subcarrier is the following

where η DL k,m is a scalar coefficient controlling the power transmitted by the m-th AP to the k-th UE, and s DL k (q) is the unit-energy data symbol to be sent to the k-th UE on the q-th subcarrier. Letting P DL m denote the overall transmitted power by the m-th AP, the normalized transmit power must satisfy the constraint

Subsequently, each UE receives contributions from all the APs. In particular, the k-th UE receives on the q-th subcarrier the N UE -dimensional signal

with z k (q) being the N UE -dimensional additive white Gaussian noise (AWGN) with entries CN (0, σ 2 z ). Based on (26), it is straightforward to express the downlink signal to interference plus noise ratio (SINR) of the k-th UE on the q-th subcarrier as follows:

### B. Uplink data transmission

In the uplink, UEs send their data symbols using the beamforming vectors v k,n , n = 1, . . . , N D in Eq. ( 23). Accordingly, the signal transmitted on the uplink by the k-th UE on the q-th subcarrier is

with η UL k,n the uplink transmit power of the k-th UE in the n-th direction and s UL k (q) the uplink data symbol of the k-th UE. Letting P UL k denote the overall transmitted power by the k-th AP, the normalized transmit power must satisfy the constraint

As a result, the N AP -dimensional signal y m (q) received at the m-th AP on the q-th subcarrier can be expressed as

with w m the AWGN vector with entries CN (0, σ 2 w ). Subsequently, the m-th AP which communicates with the k-th UE forms its local statistic

to be sent to the CPU for uplink data decoding. It is easy to show 4 that the resulting uplink SINR for the k-th UE on the q-th subcarrier can be written as

## VII. NUMERICAL RESULTS

We are now ready to show numerical results assessing the performance of the proposed BA procedures.

### A. Simulation setup

In our simulation setup, we assume a communication bandwidth W = 123 MHz centered over the carrier frequency f 0 = 28 GHz. The OFDM subcarrier spacing is 480 kHz and assuming that the length of the cyclic prefix is 7% of the OFDM symbol duration, i.e., τ CP ∆ f = 0.07,  1), if the rays between the mth AP and the n-th scatterer and the k-th UE and the n-th scatterer simultaneously exist. We assume a link exists between two entities, in our case one AP/UE and one scatterer, if they are 4 Details are omitted for the sake of brevity.

in LoS, with a probability, P LOS (d) depending on the distance between the two entities, d say.

For P LOS (d) we use the model in [33], [34]:

with d the distance between the AP/UE and the intended scatterer. For the channel model in Eq.

(1) the variance of the complex gain associated to the -th path between the k-th UE and the m-th AP, γ k,m, is obtained as [33] γ k,m, = -20

where r k,m, is the length of the path, n is the path loss exponent, X SF is the zero-mean, σ 2 Xvariance Gaussian-distributed shadow fading term in logarithmic units, and λ is the wavelength.

We use the parameters of the Urban Microcellular (UMi) Street-Canyon environment, i.e., n = 3.19 , σ X = 8.2 dB [33]. The propagation delay associated with the -th path between the k-th UE and the m-th AP is written as τ k,m, = r k,m, /c, with c the speed of light. The total power transmitted by the APs over all the subcarriers during the BA phase is denoted as P BA , and consequently β = P BA /N C . In the following, we assume P BA = 10 dBW. For the data transmission phase, we assume equal stream power allocation both in uplink and downlink; in particular, denoting by P DL m and P UL k the available power at the m-th AP and at the k-th UE, the downlink and uplink power control coefficients are expressed as

and

respectively. In the simulations, we used P DL m = 10 dBW and P UL k = 3 dBW.

### B. Results and comments

The considered performance measure is the probability of correct detection at the UE of the  detection probability versus the number of beacon slots T used for the BA procedure. In Fig. 4, there are D = 8 different data-patterns, while in Fig. 5 the number of data-patterns is D = 16.

Each figure shows the performance for two different pairs of the parameters (ν AP , ν UE ), i.e. the number of active fingers in the beamformers used at the APs and at the UEs, respectively. The figures refer to the case of pilot-less data-patterns. In order to show the merits of the proposed location-based data-pattern assignment procedure, detailed in Section III-B, we also report the performance corresponding to the case in which a random assignment (RA) of the data-patterns to the APs is performed. Inspecting the figure, it is seen that for all the considered cases the detection probability increases with the number of beacon slots used for the BA phase, which confirms the validity of the proposed approach. Regarding the comparison between the MCO and SCO procedures for BA, we can see that the MCO, albeit being simpler, achieves much better performance than the SCO; moreover, results show that see that the increase in the parameter  D improves the detection capability of the system; however D cannot be increased too much since this corresponds to a smaller value of Q, the number of carriers assigned to each AP RF chain. Larger values for the parameters ν AP and ν UE also bring some performance improvement in the case of low values of T . Finally, the detection probability for N D = 1 is obviously larger than that for N D = 2, since in the latter situation two paths rather than one are to be correctly detected, which is more challenging. data-patterns are employed. Focusing on the pilot-based BA procedure, we can also note that in the case of D = 4, the orthogonality between the APs during the BA procedure is not preserved and so there is a performance degradation compared with the case D = 8.

Overall, the shown results prove that the proposed procedures are effective and permit realizing BA in multi-AP multi-UE environments with good performance. The introduction of the orthogonal pilot sequences helps to further increase the detection capability performance of the algorithms.

We now consider the performance during the data transmission phase. Fig. 7 reports the empirical CDF of the SINR per user on each subcarrier, evaluated as in Section VI, for the downlink and the uplink. We compare the performance obtained with the proposed BA procedure based on the MCO technique, with the case of perfect knowledge of the directions of strongest paths. The beamformers at the APs and UEs are thus obtained following Eqs. ( 22) and ( 23), respectively. We can see that, especially in the case of pilot-based data-patterns, the BA procedure is very effective in finding the strongest beams and these beams can be efficiently used both for the uplink and downlink communication. The obtained SINRs is just few dBs far from the one corresponding to the ideal case of known channel. This is a further confirmation of the effectiveness of the BA procedure here proposed.

## VIII. CONCLUSIONS

This paper has considered the problem of performing BA in a CF-mMIMO network operating at mmWave frequencies. The proposed BA procedure amounts to a protocol involving the CPU, the UEs, the APs and a macro-BS managing a control channel at sub-6 GHz frequency. It enables simultaneous BA of each UE with the strongest beams coming from a pre-defined number of strongest APs. A procedure to assign the data-patterns across the APs has also been proposed.

Two different algorithms, to be run at the UE, have been proposed. Of these, the MCO has been shown to achieve better performance with smaller complexity than the other proposed algorithm, the SCO one. Numerical results have confirmed the effectiveness of the proposed approach both in terms of detection probability and in terms of UL and DL SINR, confirming that BA can be performed in a shared frequency band with a simultaneous operation of several APs and several UEs.

