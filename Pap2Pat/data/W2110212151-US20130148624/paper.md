# Introduction

The 3GPP long-term evolution (LTE) standard, which is a subset of the upgraded specifications of 3G network system, aims at the goals such as peak data rate of 100 Mbps in downlink and 50 Mbps in uplink, throughput increase at the cell boundary, spectral efficiency improvement, and scalable bandwidth [1][2][3]. As the 3GPP LTE was developed under the assumption of a packet-switching operation, the packet scheduler plays the central role in determining the overall system performance.

Several packet schedulers, focusing on fairness and throughput maximization, were introduced in [4][5][6][7][8][9] based on the round robin (RR), proportional fair (PF), and maximum throughput (MT) algorithms. To reduce the complexity, most schedulers operate in two phases: time domain packet scheduler (TDPS) followed by frequency domain packet scheduler (FDPS) [4,5]. The efficient FDPS in [6] showed drastic increase in system throughput and cell coverage. In [7,8], the authors proved significant improvement of spectral efficiency in 3GPP LTE downlink. Reference [9] showed that the PF algorithm provides fairness improvement but shows little decrease of throughput. Packet scheduling algorithms for mixed traffic system were also been proposed and evaluated in [10,11], but only the data rate was adopted in the scheduling metric.

In this paper, we propose a novel minimum transmit power-based (MP) packet scheduling algorithm that can achieve power-efficient transmission to the UEs while providing both system throughput gain and fairness improvement. The proposed algorithm is based on the ratio of the transmit power to the number of transmission bits. Thus, the proposed MP scheduler allocates the physical resource block (PRB) to the UE that requires the least ratio of the transmit power per bit. For this, it is assumed that the channel quality indication (CQI) information for all UE channels is available at the evolved Node B (eNB), with which the modulation and coding scheme (MCS) level and the UE transmit power are determined. The performance of the proposed MP algorithm is compared with the conventional algorithms through computer simulation, considering real-time and non-real-time traffic in multicell environments.

The rest of this paper is organized as follows. Sections 2 and 3 briefly describe the packet-scheduling model  and algorithms, respectively. Section 4 explains the simulation environment. The simulation results are discussed in Section 5, and we conclude this paper in Section 6.

# Packet Scheduling Models

The basic structure of downlink packet scheduler for RT and NRT traffics in eNB of the 3GPP LTE is depicted in Figure 1.

The packet scheduler is divided into two phases: TDPS and FDPS. In the TDPS, a small group of UEs are chosen as the scheduling candidate set (SCS) based on diverse metrics: buffer size, delay, CQI reports, and so forth. The TDPS does not allocate PRBs to the UEs, but it conveys the information of the UEs becoming scheduling candidates to the FDPS. In the FDPS, the PRBs at Layer 1 are directly allocated to the SCS received from the TDPS. In a mixed traffic system, a classifier is necessary for the efficiency of packet scheduling. The classifier sets independent queues based on traffic types, and each queue is given its own priority. Thus, each traffic type can be independently handled. With the classifier, the packet scheduler cooperates with the CQI manager, hybrid automatic repeat request (HARQ), link adaptation, and QoS manager. The link adaptation decides a proper MCS level for respective UE and PRB combinations based on the CQI which acts as the primary criterion [12]. The PRBs with good channel conditions are given a MCS level sending a lot of data [13]. The QoS manager checks UEs' QoS requirements and the packet scheduler calculates packet scheduling metrics.

## Classifier.

In Figure 1, the classifier classifies the mixed traffic at Layer 2 data buffer according to the type of traffic. Because each traffic type has its own QoS requirement, the classifier is necessary in a mixed traffic system for efficient packet scheduling. In this paper, we assume that RT and NRT traffics exist at the same time. The classifier is provided with traffic statements from L2 buffer and sets two independent queues for RT and NRT traffics assigning different priorities to the queues.

Under the consistent traffic environment, the most efficient resource allocation scheme is divided into two adaptations. First of all, voice streaming and WWW data service exemplify RT and NRT traffic in real systems. RT traffics such as voice streaming have constant bit rate (CBR) feature. Margin adaptation for OFDMA systems [14] is considered as the most efficient resource allocation scheme for power minimization of RT traffics. On the other hand, NRT traffics like WWW data service have best effort (BE) characteristic. Rate adaptation [14] is known as the most efficient resource allocation scheme for throughput maximization of NRT traffic with a power constraint.

Therefore, in order to maximize the system throughput and to minimize the transmit power of mixed RT as well as NRT traffics at the same time, efficient transmit power consumption becomes a key issue. Generally, RT traffics need to deal with a delay constraint, so the higher priority is essential [15]. Different priorities and power constraint influence the PRB allocation during one transmission time interval (TTI). Because the RT traffic features a delay constraint and CBR, the PRBs are firstly allocated to RT traffic UEs. After PRB allocation for the RT traffic, the NRT traffic UEs, having BE characteristic, consume the remaining transmit power for PRB allocation, aiming at bit rate maximization [15].

## Time Domain Packet Scheduling.

The main purpose of the TDPS is to set the SCS. The TDPS does not directly allocate the PRBs, but it restricts the number of UEs for the FDPS to reduce the scheduling complexity. The SCS is chosen based on a computed metric such as the CQI, throughput, delay, and so forth. The SCS information is conveyed to the FDPS and only the UEs restricted by the TDPS are qualified as the FDPS candidates. The TDPS should concern the data in L2 buffer and HARQ, simultaneously. When retransmission is requested through HARQ, UEs requesting HARQ are automatically comprised in the SCS.

## Frequency Domain Packet Scheduling.

In the FDPS phase, the PRBs are directly allocated to the UEs and their data are transmitted. It delivers the allocated data after packet scheduling to physical level (L1) devices, and then the L1 devices send the data by modulated signal through physical channel. The FDPS considers only the SCS during one TTI. The FDPS is completed when all transmit power is consumed. A UE can load the information on the plural PRBs, but a PRB cannot be shared by more than one UEs at the same time.

# Packet-Scheduling Algorithms

3.1. Conventional Packet-Scheduling Algorithms. Diverse packet scheduling algorithms were introduced and their performances were evaluated in terms of system throughput and fairness [16][17][18]. For the best fairness, the RR algorithm can be applied. In the RR algorithm, the scheduler at time t uses the information on the elapsed time since the latest scheduled time (t s ) for each UE s as the scheduling metric [10]: that is,

where s denotes the selected UE index. The MT algorithm focuses on the spectral efficiency and achieves the best system throughput. In 3GPP LTE system, data rate to be transmitted is affected by the MCS level decided by the link adaptation based on the CQI reported from the corresponding UE.

For the higher CQI, the link adaptation selects a higher MCS level with more bits per symbol. The data rate D s,n is calculated based on the recommended MCS level. Thus, the MT scheduler is expressed as

where n is the index of the selected PRB, and Q s,n denotes the CQI of the PRB n reported from the UE s. In other word, the UE with the highest data rate acquires the highest priority.

The PF algorithm was introduced to solve monopolized situation in the MT algorithm. Scheduling metric is defined as the data rate divided by the past average user data rate. Thus, the scheduling metric is equal to the ratio of D s,n to the average past user data rate R s as

3.2. Proposed MP Packet-Scheduling Algorithm. In order to improve the fairness and throughput, most of conventional algorithms including the MT and PF consider the instantaneous channel condition and throughput as key factors of scheduling metric. However, new factors should be considered to enhance the system performance. One of them is the ratio of the transmit power per bit, which has not been considered yet for packet scheduling. The transmit power is insufficient when the radio resources are fully utilized, huge amount of data are required to be transmitted, and most UEs have poor channel conditions. In this case, if scheduling metric of a packet scheduling algorithm considers the ratio of the transmit power to the number of transmission bits, more improvement in the system performance is expected. For this reason, in a system with limited transmit power, it is the most efficient to allocate PRBs to the UEs that requires the least ratio of the transmit power to the number of transmission bits. Thus, in the proposed MP scheduling algorithm, the scheduling metric selects the UEs to be allocated in ascending order of the ratio of the transmit power P s,n to the number of transmission bits b s,n as follows:

where g s,n is the channel power of the PRB n of the UE s. In (4), assuming that the same MCS level is used for all subcarriers in a PRB, the minimum transmit power f (b s,n ) 

where σ 2 s,n is the noise variance for the subcarriers in the PRB n at the UE s, and

Assuming that the link adaptation is employed and that the maximum transmit powers of the eNB are large enough, (4) can be rewritten as (see the appendix)

where the scheduling metric M(s, n) is expressed by

and Δ s,n denotes the excess channel gain defined by Δ s,n = g s,n -g min (b s,n ); g min (b s,n ) is the minimum channel gain required for the successful transmission of b s,n bits; b s,n is the maximum positive integer that satisfies Δ s,n ≥ 0. From (7), the MP scheduler assigns the PRB n to the UE with larger excess channel gain compared to the required received power per bit. For the UEs with equal value of excess channel gain, the MP scheduler assigns the PRB to the UE with smaller received power per bit. For example, consider UE k, j, and i in Figure 2 ranked on MCS level 1,2, and 3, respectively. In the figure, the MCS level 1 sends the highest data rate while the MCS level n transmits the lowest data rate. According to the 3GPP LTE AMC scheme, UE k is able to transmit more bits than UE j but UE k requires lower transmit power per bit than UE j. It is because the CQI of UE k is much larger than the minimum required CQI for the MCS level 1 which may require small transmit power, while the CQI for UE j is close to the minimum value for the MCS level 2 which requires larger transmit power than the other cases. Meanwhile, UE i has almost the same excess channel gain as UE k, but it requires less received power per bit, f (b s,n )/b s,n , than UE k because f (b s,n )/b s,n in (7) increases exponentially with b s,n ; hence, the value of f (b s,n )/b s,n for UE i is smaller than UE k having higher MCS level than UE i. Therefore, the MP scheduler selects the UEs to be allocated in order of UE i, UE k, and UE j. After all, for the efficiency of power consumption, the MP algorithm considers the transmit power and the number of transmission bits at the same time.

The implementation complexity of the MP scheduling rule in (4) can be reduced as follows. Define

Then, ( 7) can be rewritten as

Because g min (b s,n ) and ω(b s,n ) can be precalculated for all possible values of b s,n , the calculation of the metric in ( 9) is much simpler than the metric in (4).

# Simulation Environment

The algorithm evaluation is based on the 3GPP LTE downlink specifications defined in [1] and the simulation scenario in [20]. The 19-cell model with wrap around is assumed, in which omnidirectional antennas are used and the UEs are uniformly distributed. Calls are generated based on Poisson arrival rate and a simple admission control is applied in order to prevent users from gathering in a few cells. The admission control blocks a new call into a cell when the number of users in the cell is equal to the limit. The other simulation parameters are described in Table 1.

One TTI is one subframe duration of 1 millisecond, during which 14 symbols are transmitted. Our simulation assumes 5 MHz transmission bandwidth, thus 25 PRBs are available during one TTI. The link adaptation selects the modulation mode for a user based on the CQI. An infinite buffer model is applied. We assume two different traffic types: RT traffic and NRT traffic. RT traffic needs to guarantee a target CBR for successful transmission hence, we set the guaranteed bit rate (GBR) as 64 kbps. Moreover, RT traffic has higher priority than NRT traffic because RT traffic is vulnerable to delay constraint. On the other hand, even though NRT traffic does not need to be guaranteed and is not sensitive to delay constraint, the remaining power after the transmit power consumption for RT traffic is used for NRT traffic since all transmission power must be spent during one TTI at eNBs in order not to waste spectrum. Note that the HARQ scheme is not applied in this paper since it is beyond the scope of this paper.

# Simulation Results

The proposed MP packet scheduling algorithm is compared with the conventional MT, RR, and PF packet scheduling algorithms. Among the conventional three algorithms, the MT algorithm shows the best throughput and the RR algorithm the worst throughput. However, in terms of fairness, the RR algorithm achieves the best performance and the MT algorithm shows the worst performance. The worst fairness of the MT algorithm is attributed to the monopolization of spectrum resource by only a few UEs with good CQIs. On the other hand, UEs with poor CQIs can be given a higher priority in the PF algorithm by using a different metric from the MT algorithm as divided by the past average data rate. Therefore, in despite of the poor channel states, the UEs can precede other UEs having good channel conditions. Monopolizing UEs tend to be located near eNBs at the center of the cells. By applying the PF and RR algorithms, user throughput at the cell edge can be increased.

In the following figures, the paired labels of the packet scheduling algorithms are applied for TDPS and FDPS in order. For example, the labeled MT-MT refers the MT algorithm used for both of the TDPS and the FDPS.

## Average User and Cell Throughput

Performance. Figure 3 shows the average user throughput, which is defined as the ratio of the total throughput in a cell divided by the total number of UEs, with different maximum number of UEs in a cell. From Figure 3, we find that the MP-MP algorithm achieves even better average UE throughput than the MT-MT algorithm. The MP algorithm's spectral efficiency seems to be more efficient than the other packet  scheduling algorithms as the maximum number of UEs in a cell increases. When maximum 25 users exist in a cell, the MP-MP algorithm achieves 18% increase of average user throughput compared to the MT-MT algorithm.

It is also found that most of the gain of average user throughput of mixed traffic UEs in Figure 3(a) comes from the NRT traffic UEs in Figure 3(b). It is because NRT traffic UEs having BE feature can receive as many available data as possible, while RT traffic UEs do not receive more data than their target data rates. In Figure 3(c), the MP algorithm also shows the best capacity of RT traffic because more capacity is provided when the algorithm is applied. Under the same maximum number of UEs in a cell, the MP-MP algorithm shows the best throughput per UE. This result indicates that better average user throughput occurs with more UEs. It is because of efficiency of transmit power consumption. Under the saturation of a cell, the transmit power consumption becomes a more critical issue because power is a limited resource. Therefore, from the results, the packet scheduling algorithm by the ratio of the transit power to the number of transmission bits provides a great increase of the average user throughput.  As call arrival rate increases, the MP-MP algorithm provides more eminent performance. For example, when call arrival rate is 10 -2 , the algorithm shows 6% gain in the average cell throughput for total UEs compared to the MT-MT algorithm.

Figure 5 shows the average cell throughput at the cell boundary with call arrival rate. In the simulation, 20% of the the UEs were located at the cell boundary in which the power-efficiency is particularly important. Compared to the RR-RR algorithm, 70% gain of the MP-MP algorithm at the cell boundary is obtained for the call arrival rate of 10 -2 . The improved spectrum efficiency comes because the proposed MP scheduling algorithm considers the ratio of the transmit power to the number of transmission bits.

Figure 6 shows the average cell throughput with the transmit power, where the maximum allowable transmit power is 46 dBm as given in the 3GPP LTE downlink specification [1]. From the figure, the MP-MP algorithm can sustain more than 10 Mbps average cell throughput with 30 dBm. In addition, the MP-MP algorithm can save the transmit power about 8 dBm than the MT-MT algorithm while sustaining the same cell throughput.

## Fairness Performance.

Figure 7 shows fairness and cell throughput. Here, the fairness is defined as the ratio of the best 5% UEs' throughput to the total cell throughput. The MT-MT algorithm shows the worst fairness as expected. In the MT-MT algorithm, the best 5% UEs occupy approximately 20% out of the whole cell throughput. On the other hand, in the RR-RR and PF-PF algorithms, although cell throughput shows less than 10 Mbps, the best 5% UEs occupy less than 10%. However, by the MP-MP algorithm, the cell throughput is more than 10 Mbps and the best 5% UEs occupy less than 10% of the cell throughput. As a result, the MP-MP algorithm provides better performance in terms of not only cell throughput but also fairness than the other algorithms.

Figure 8 shows the distribution of normalized throughput with respect to the UE index. Here, the normalized throughput is defined as the ratio of the throughput per UE to the total throughput in a cell. From the figure, it is found that large portion of normalized throughput is centralized in only a few UEs with good channel conditions by the MT-MT algorithm. However, the normalized throughput by the RR-RR, PF-PF, and MP-MP algorithms are fairly distributed. The normalized throughput by the MP-MP algorithm shows relatively equal transmission probabilities for all UEs.

Figure 9 shows the distribution of the normalized throughput of a UE with the distance from the serving eNB normalized by the cell radius. Because the distance is the most important factor which affects the channel condition, in the MT-MT and PF-PF algorithms, the normalized throughput is centralized and decreases as far from the center. However, normalized throughput in the RR-RR and MP-MP algorithms randomly spreads over the all region. The reason is because the MP algorithm considers the ratio of the transmit power to the number of transmission bits. From Figures 7,8, and 9, we find that the MP algorithm provides improved performance in terms of fairness and throughput. Specially, Figure 9 shows throughput increase at the cell boundary.

# Conclusion

In this paper, we presented the decoupled packet scheduling algorithms in 3GPP LTE systems and proposed a novel algorithm which considers the efficiency of transmit power consumption. The performance of the proposed algorithm was evaluated by comparing with the conventional algorithms: the maximum throughput (MT), round robin (RR), and proportional fairness (PF). From the simulation results, the MP-MP algorithm applying the proposed minimum transmit power-based packet scheduling (MP) algorithm to the time domain packet scheduler (TDPS) and the frequency domain packet scheduler (FDPS) in 3GPP LTE systems showed better throughput performances than the other conventional algorithms. Moreover, the MP-MP algorithm showed significant improvement of the fairness performance, which comes from the different packet scheduling metric regarding the ratio of the transmit power to the number of transmission bits. Conclusively, from the results, we confirm that the proposed scheduling metric successfully improves the system performance such as the fairness and throughput. Further work includes CQI reporting scheme because the performance of the proposed downlink scheduling algorithm, as well as the conventional ones, depends on the accuracy of the CQI information.

# Acknowledgment

This work was financially supported by the Grant from the Industrial technology development program (Project no. KI002143) of the Ministry of Knowledge Economy (MKE) of Korea.

# Appendix

Let P max s,n denote the maximum transmit power at the eNB that can be assigned for the UE s and the PRB n. Then, the minimum channel gain required for successful transmission of b s,n bits through the PRB n is given by g min (b s,n ) = f (b s,n )/P max s,n , where f (b s,n ) is defined in (5). Since we have g s,n = f (b s,n )/P s,n , the excess channel gain Δ s,n is written as

From (A.1), we get

Using (A.2) in ( 4), we get

and, when P max s,n is large enough, (A.3) can be rewritten as (6).

