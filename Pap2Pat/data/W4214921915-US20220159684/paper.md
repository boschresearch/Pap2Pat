# I. INTRODUCTION

In the millimeter wave band, antenna arrays are usually adopted by UE to generate high-gain beams than the single antenna, and thus resulting in higher SNR and throughput. For example, [1]- [4] presented possible antenna array setups for mmWave 5G phones, where 2 × 1, 4 × 1 or 2 × 2 arrays are adopted. One of the key challenges for 5G and beyond is the UE power consumption [5]. The battery life and temperature control issue aggravates in the mmWave bands compared to the sub-6 GHz band. When the phone is heating up quickly, one straightforward solution is to fall back to the sub-6 GHz and turn off the mmWave array. The LTE fallback is not desired in general. First, the maximum data rate decreases from Gbps to a few hundred Mbps or less. Second, the frequent turn off/on of the mmWave antenna module incurs additional latency, power consumption, and even service disruption.

Instead of falling back to LTE, an alternative solution is to reduce the number of activated antenna elements. Such kind of beam which only activates a part of the array is called 'subchain beam' in this paper, since the antennas on the same array are connected to the same RF chain. Meanwhile, the beam which activates the whole array is called 'full-chain beam'. Note that the deactivation approach has been used to create wide beams [6], [7] in hierarchical codebook design, but in this paper, it is utilized to save the power and prevent overheating, instead of broadening the beamwidth.

An example of the sub-chain beam operation is shown in Fig. 1, where UE activates only a portion of its antenna array for UL transmission, while still activating the full array for DL reception. This operation scheme is chosen since 1) the transmission consumes much more power than the reception, and 2) the downlink data rate requirement is usually higher than the uplink.

The 5G standard has defined the process of identifying and maintaining a suitable beam pair for the BS-UE link, which is known as beam management (BM) [8]- [11]. The above operation scheme could destroy the DL-UL beam correspondence in 5G BM, which refers to the assumption that the best beams in the downlink direction are also the best beams in the uplink direction. DL-UL beam correspondence is an important design criterion, since an additional separate UL 

## Beam index Full

beam management procedure will be required if there is no DL-UL beam correspondence.

In this paper, we propose methods to design the sub-chain beam codebook to maximally maintain the beam correspondence. That means that if the full-chain Beam B3 in Fig. 1(a) is the best Rx beam in the downlink, the corresponding subchain Beam B3 in Fig. 1(b) should be the best Tx beam too.

Another option of power saving is to scale down the transmission power level of all the antennas together. Although the total radiated power can be same between sub-chain and this option, the total power consumption is different. Activating a power amplifier (PA) requires a base power regardless of the power level. The option of reducing the power level still needs to turn on all the PAs, which means more base power consumption. In contrast, if we turn off some PAs (sub-chain beam), we can save not only the transmitted power but also the base power.

Notation: Bold uppercase letter A and bold lowercase letter a represents a matrix and a column vector, respectively.

### (•)

T , (•) * , (•) H denotes the transpose, conjugate and Hermitian of a vector or matrix, respectively. a 0 is the L0 norm of the vector a.

[a] m:n stands for the a sub-vector of a from the m-th entry to the n-th entry. 1{•} is the indicator function.

## II. SYSTEM MODEL

In this paper, we consider a UE equipped with 2 arrays on the left and right edge, respectively. In each array, there are L dual-polarization patch antennas. The 2L antenna elements are denoted as 1V, 2V, • • • , LV, 1H, 2H, • • • , LH. The beamforming vector is thus defined as

where the magnitude of the beamforming weights, i.e., |w | (1 ≤ ≤ 2L), is either 0 or 1. In other words, the antenna is either on or off, without the capability of fine magnitude tuning. The phase of w is also restricted to a few discrete values, since the finite-resolution phase shifters are used in practice. If b-bit phase shifters are adopted in the implementation, the constraint on a nonzero beamforming weight is w 2 b = 1.

The radiation pattern of a practical mmWave antenna, combined with the impact of terminal housing, is highly irregular [4], [12], [13]. We thus adopt the data-driven method for codebook design [1]. The E-field response data of each antenna element is obtained from the simulation or measurement. Note that the terminal housing effect are incorporated in the E-field data. The beam pattern is calculated as,

where M(θ, φ) consists of the E-field response of each antenna in the direction (θ, φ), and is usually a rank-2 matrix [1].

For the sub-chain beam, there could be additional design requirements based on the hardware implementation. In this paper, we consider a constraint that the number of activated antennas in the two polarizations are same, i.e.,

[w] 1:L 0 = [w] L+1:2L 0 , but the indices of the activated H and V-polarization antenna can be different. Note that it is straightforward to extend our design method to meet other constraints. For example, the indices of the activated antennas in the two polarizations should be same which means that

An example sub-chain beam codebook is provided in Table I where K is the codebook size. For simplicity, we only show single-array single polarization case in this table. When the UE switches between the full-chain operation to a sub-chain operation, or between two distinct sub-chain operations, it does not need to perform a new round of beam sweeping to identify the best beam if the beam correspondence has been maintained. Instead, it adopts the corresponding beam in the same row directly.

## III. SUB-CHAIN BEAM CODEBOOK DESIGN

There could be different metrics and methods to design the sub-chain beam codebooks per different requirements and UE operation procedures. In this paper, we consider three different metrics, which are called, 1) 'similarity score (Sim)', which puts great emphasize on the beam mapping accuracy when activating/deactivating antennas (i.e., each row of Table I); 2) 'spherical coverage (SC)', which makes much account of the performance of fixed-antenna beam codebook (i.e., each column of Table I); 3) 'beam correspondence spherical coverage (BC-SC)', which is a trade-off between the first two metrics. We denote the method maximizing these metrics as 'Sim-Max', 'SC-Max' and 'BC-SC-Max', respectively.

### A. Similarity Score Maximization (Sim-Max)

In the first method, the sub-chain beams are designed to resemble the full-chain beams. In other words, the radiation pattern of each sub-chain beam is designed to be similar to the corresponding full-chain beam (one-to-one mapping). There could be different measures of similarity of two beam patterns. In one approach, assuming that there is a set of N p uniformly distributed sampling points on the unit-sphere (e.g., Fibonacci grid [14]), the similarity score is defined as,

where G i (θ, φ) is the i-th full-chain beam pattern, and B j (θ, φ) is the sub-chain beam pattern. The term Np n=1 G 2 i (θ n , φ n ) is to normalize the score, such that the score between a beam and itself is one. The candidate subchain beam with the largest similarity score is chosen. The candidate sub-chain beam could be from an available pool of beams. Alternatively, the sub-chain can be obtained by solving the following optimization problem,

where

is the number of activated antennas per polarization. The discrete phase constraint (5) and L0 norm constraints (6) (7) in P1 are both non-convex, making it difficult to solve P1. Since the array size L is usually small for the UE, we can exhaustively try all the possible activation of the antennas, and solve L L A 2 problems separately. For a given activation without L0 norm constraints, P1 can be solved efficiently by an iterative algorithm which optimizes the phase cyclically [1, Algorithm 3]. Although the iterative algorithm provides a local optimum, we can run it multiple times with different initial beams, and select the best local optimum as the final solution. Since there are still 2 2bL A possible beams given an activation, the iterative algorithm has much lower complexity than the exhaustive search when b and L A is not too small (e.g., b = 5 and L A = 4).

### B. Spherical Coverage Maximization (SC-Max)

In this method, the sub-chain codebook is designed to maximize the spherical coverage. There is no consideration on the one-to-one mapping between the sub-chain and full-chain beams, which implies that a fresh beam sweeping would be needed to determine the best beam if the UE switches from full-chain to sub-chain codebook (or switches between two sub-chain codebooks). This design could be adopted if the UE chooses to operate with same number of antennas for Tx and Rx, and thus DL-UL beam correspondence is maintained as in the conventional full-chain Tx-Rx case.

The codebook is designed to maximize the average beam gain over the whole sphere. The optimization problem is as follows,

# P2:

max

The K-Means algorithm [1] is adopted to solve P2. It iterates between two steps: i) assign each direction to the beam providing the largest gain, ii) optimize the beams to serve the assigned directions. In the beam optimization step, we solve L L A 2 K problems by exhausting all the possible antenna activation.

## C. Beam Correspondence Spherical Coverage Maximization (BC-SC-Max)

In the third method, the sub-chain beams are designed to maximize the radiation pattern over the full-chain beam's coverage region, which is a sub-region of the whole unitsphere. A fresh beam sweeping is not necessary in this option since the sub-chain beam is designed to cover an angular region similar to the full-chain beam. Therefore, for a given channel, the sub-chain beam is very likely to be the best one if the corresponding full-chain beam is the best. The design procedure is as follows.

1) Partition the unit-sphere into the coverage regions of the full-chain beams. If there are K beams, we have

where D k is the disjoint angular region covered by the full-chain beam wk ,

2) For each angular region covered by the full-chain beam, design the best sub-chain beam by solving the following problem,

s.t. (5), ( 6), (7).

The optimization problem P3 is similar to P1 and thus the same iterative algorithm is adopted with two minor modifications. First, the summation in P1 is over the whole unit-sphere, but P3 is only over an angular region. Second, the summation in P1 is weighted by the full-chain beam pattern while there is no weights in P3. Roughly speaking, when generating subchain beam resembling the full-chain beam, SC-Max method examines the similarity over the whole sphere, while BC-SC-Max method only considers the main lobe region. 

## IV. SIMULATION RESULTS

We simulated a 5G phone with two mmWave 1x5 arrays on the left and right edge by the electromagnetic simulation software. E-field data was generated for each antenna element. Each array has seven beams and the total number of beams is 14. The phase shifter resolution is 5-bit. We choose N p = 10001 when generating the uniformly distributed sampling points. The full-chain codebook is generated by the K-Means algorithm [1]. In the SC-Max method, we initialize the K-Means algorithm with a codebook obtained by a greedy algorithm [1, Section V].

Fig. 2-Fig. 4 illustrate the generated sub-chain beam codebooks from the Sim-Max, SC-Max and BC-SC-Max method, respectively 1 . Subfigure (a)-(e) show the composite beam pattern B(θ, φ) = max 1≤i≤14 B i (θ, φ) and Subfigure (f)-(j) illustrate the best beam index distribution I(θ, φ) = argmax 1≤i≤14 B i (θ, φ). The radiation pattern of sub-chain codebooks are weaker than the 5-Ant full-chain codebook, since less antennas are activated. For the Sim-Max shown in Fig. 2, the pattern shapes and the best beam index distributions of the full-chain and sub-chain (especially 4-Ant and 3-Ant) codebooks are more or less similar, which implies the beam correspondence between the full-chain and sub-chain is preserved. The same observation holds for the BC-SC-Max codebooks shown in Fig. 4. In contrast, for the SC-Max method shown in Fig. 3, there is less similarity between the radiation patterns across the 5 codebooks, and the beam index distributions are also quite different across the 5 codebooks.

We quantify the beam correspondence by checking the probability that the best beam index distribution is same between two codebooks over the unit-sphere. If the best beam index is same at a location on the unit-sphere, it means that the beam correspondence is preserved for that particular direction,   and there is no need to perform another round of beam sweeping when deactivating or activating more antennas. Because of the random UE orientation, we can assume the channel path comes from all the directions with equal probability. Therefore, the proposed metric tells us how often skipping the beam sweeping does not incur performance loss in a singlepath channel. We call the metric 'best beam matching rate' and define it as,

where L 1 , L 2 are the number of activated antennas of two codebooks. The proposed metric for the three methods is shown in Fig. 5. First, we find that for the Sim-Max and BC-SC-Max codebooks, it is quite safe to switch among 5-Ant, 4-Ant and 3-Ant codebooks. The beam correspondence is preserved for more than 90% of the time. Second, BC-SC-Max is much better than Sim-Max when switching between 1-Ant codebook and another codebook. Third, SC-Max codebooks have very low matching rate (≤ 25%) because there is no consideration of beam mapping at all in the design procedure.

To improve the matching rate of SC-Max codebooks, we repair the beams rather than simply pairing the beams with same index. The procedure is as follows. We first identify the dominate sampling points of each beam,

We then find the intersection between two beams from different codebooks,

The cardinality of the intersection |C L1,L2 (i, j)| is treated as the benefit of pairing Beam i from L 1 -Ant codebook and Beam j from L 2 -Ant codebook. Then Hungarian algorithm is applied to find the best pairing maximizing the total benefit. Fig. 6 shows the best beam matching rate after repairing. It is much better than the previous results shown in Fig. 5(b), but is still clearly worse than the Sim-Max and BC-SC-Max method in Fig. 5(a) and Fig. 5(c). It implies that repairing is not a sufficient solution to maintain the beam correspondence. Last but not least, we compare the spherical coverage of those codebooks by checking the composite beam gain CDF on the unit-sphere. Fig. 7 shows the CDF curves for the fullchain, and sub-chain codebooks of the three methods. Note that the repairing does not change the spherical coverage of the SC-Max codebooks. First, as expected, the spherical coverage improves with the number of antennas and the 5-Ant case is the best one. Second, the spherical coverage of the Sim-Max codebooks are worse than the other two methods, especially in the low percentile region. Third, we find that the BC-SC-Max method achieves the similar spherical coverage as the SC-Max method! V. CONCLUSION In this paper, we proposed a practical beam operation scheme for mmWave 5G devices to increase the utilization of mmWave band. Because of the high power consumption and heating of mmWave antennas, mmWave devices frequently fall back to sub-6 GHz band, and sporadically utilize the mmWave band. We proposed a sub-chain beam operation which deactivates part of the mmWave antenna array in the uplink transmission when the device is overheating. The antenna deactivation, however, could destroy the downlinkuplink beam correspondence. The more the antenna deactivation, the worse the beam correspondence. We proposed three methods to carefully design the sub-chain codebooks. The Sim-Max method generates sub-chain beams resembling the shape of full-chain beams, the SC-Max method optimizes the spherical coverage of the sub-chain codebooks, and the BC-SC-Max method takes into account both the similarity and spherical coverage.

We performed extensive simulations of a real 5G phone to compare the performance of the three methods. We found that the BC-SC-Max method is the best one. It can achieve superior spherical coverage close to the SC-Max method which is dedicated to spherical coverage maximization. Meanwhile, it maximally maintains the beam correspondence. The beam correspondence holds for 90% of the time when switching among full-chain, 4-Ant and 3-Ant sub-chain beam codebooks. When UE chooses to use 1-Ant beam to save the power as much as possible, the BC-SC-Max method still preserves the beam correspondence for more than 60% of the time.

