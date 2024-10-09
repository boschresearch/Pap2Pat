# I. INTRODUCTION

In 5G cellular networks, beamforming is necessary for overcoming large channel pathloss when a user equipment (UE) tries to establish a connection with a base station (BS) in millimeter wave (mmWave) bands such as the 28 GHz, 39 GHz, or 60 GHz bands [1]- [3]. To compensate for the smaller angular coverage due to the narrow analog beamwidth in mmWave, beam sweeping can be employed to enable wider angular signal reception or transmission coverage for the UE [4]- [6]. A beam codebook comprises a set of beams or codewords, where a codeword is a set of analog phase shift values, or a set of magnitude plus phase shift values, applied to the antenna elements, in order to form an analog beam. The 3rd Generation Partnership Project (3GPP) is the The associate editor coordinating the review of this manuscript and approving it for publication was Zhenyu Xiao.

5G standardization body that specifies the minimum peak equivalent isotropic radiated power (EIRP) and the spherical coverage requirements of UE defined as a certain percentile of thecumulative distribution function (CDF) over the full sphere around the UE. There are a total of four UE power classes defined for various use cases or deployment scenarios; and the minimum peak EIRP and the spherical coverage requirements are different for different UE power classes. For example, it has been specified for the first generation (Release 15) of 5G mmWave handheld UE (power class 3) that the minimum peak EIRP is 22.4 dBm (20.6 dBm) and the minimum EIRP at the 50th percentile CDF over the full sphere around the UE is 11.5 dBm (8 dBm) for 28 GHz bands (39 GHz band) [7,. This paper describes a novel codebook generation procedure and algorithms to obtain a beam codebook given a set of requirements and performance criteria.

## A. RELATED WORK

Beam codebook design has been extensively considered in both academia and industry [5], [6]. A beam codebook design was provided in 802. 15.3c [8,Ch. 13], assuming 1-D and 2-D arrays with uniform spacing of half-wavelength. The beam searching or training process is divided into three stages, namely, link-level device discovery, sector-level alignment, and beam-level refinement. The omni or quasi-omni radiation pattern, wide beam, and narrow beam are designed respectively to fulfill the requirements of these three phases [9], [10]. The same 3-stage training process was adopted in [11] where codebooks for a 2-ring circular array were proposed. The inner small ring generates quasi-omni and sector radiation patterns while the outer larger ring generates the laststage directional beam patterns.

The idea of 3-stage codebook design was extended to general hierarchical codebook design where the number of stages or layer are not limited to be three. The analog codebook design was considered in [12] where the sub-array method used to generate a ''flatted'' wide beam. The paper [13] proposed a heuristic method where the uniform linear array is divided into 2, 3, or 4 sub-arrays and the steering direction and length of the sub-arrays are numerically optimized to maximize the minimum beamforming gain in the required coverage region. The work [14] proposed a deactivation approach where the antenna elements are adaptively deactivated to create beam with various beamwidth. Combined with the deactivation method, the sub-array based hierarchical codebook generation was optimized in [15] where either all or a half of the antenna elements are activated. The method of [15] was further enhanced in [16] where the deactivation method is dropped, and all the antenna are always activated to increase the maximal total transmission power. The subarray method was adopted in [17] to design a 3-D wide beam for uniform planar array. To design beams with a small ripple in both the main and side lobes, a beam pattern optimization problem was formulated in [18]. However, the optimization problem considered the total power constraints rather than the individual antenna power constraint, thereby the resultant beam has a large peak-to-average-power ratio, which implies low power efficiency.

Besides analog precoding, hierarchical codebook design for hybrid analog-digital precoding was considered in [19]- [21]. Given the required angular region to cover, the analog and digital precoder design was formulated in [19] as a sparse approximation problem, and solved by a variant of of orthogonal matching pursuit algorithms. The authors of [21] proposed a DFT-based multilevel codebook design where the adjacent phase-shifted DFT beams are summed up to construct wide beams. Last, the subarray method was altered in [20] to support the hybrid precoding.

Considering the high cost, power consumption and form factor of radio frequency (RF) chain, the mmWave terminals are not likely to adopt hybrid or fully digital beamforming where more than one RF chains are needed for a single array.

Therefore, analog beamforming for each antenna array is assumed throughout this paper.

In this paper, we focus on the beam codebook for data transmission, i.e, the third stage codebook in 802. 15.3c for beam searching [8], or the bottom layer fine codebook in a hierarchical codebook design [14], [15], [21]. In 802.15.3c, the codebooks are generated with 2-bit phase shifters without amplitude adjustments for the consideration of the hardware complexity. To reduce the gain loss at the intersections of two beams, the number of beams should be twice the number of array elements [22]. In the 802.11ad document [23, Section 6.6], the beam codebook design is formulated as a geometric problem to cover the sphere sector with circles by assuming that the main lobe of the beam has a circular shape. The assumption of circular shape, however, does not hold when a beam is beamforming towards directions away from the broadside direction and therefore results in coverage gaps between beams. In [14], [15], [19], and [21], the last layer beams are pointing to directions uniformly distributed in the angular domain or spatial frequency. In such cases, the beamforming vector is just the steering vector for a given beamforming direction (or an approximation of it if there is a phase shifters resolution constraint). For example, for a simple linear array with spacing d, the beamforming weights would have the progressive phases as 2πi λ d cos θ where λ is the wavelength, i is the antenna index, and θ is the beamforming direction with respect to the axis of the array. The codeword for 2-D planar array is then the Kronecker product of two codewords for 1-D linear arrays, as done in [17] and [24].

All these work [8]- [24] assumed an ideal isotropic radiation pattern and considered rather regular antenna setup, i.e., uniform linear, uniform planar or uniform circular array. We call these designs, which are based on simple theoretical assumptions, as model-based approach hereafter. Such designs, however, ignore many practical issues as described next.

Antenna for mmWave bands is intrinsically directional. For example, the patch antenna usually has a high front-toback ratio and consequently can cover at most half-sphere [25]. The directional element radiation pattern will also result in the drift of the peak gain direction from the intended one if the beamforming vector is merely designed based on the steering vector. In addition, when placed inside mobile handsets, the radiation gain of the mmWave antenna is less than the free-space case due to blockage loss and the radiation pattern shape is also changed [26].

Antenna placement and antenna spacing may not be regular. For example, the planar array may not have the half-wavelength spacing between adjacent elements due to form-factor constraints. Another reason is related to the multi-frequency bands that the mmWave terminal has to support. The mmWave bands for 5G deployment in US will include 24 GHz, 28 GHz and 39 GHz, etc. 1 The same antenna arrays, however, are likely to be used at all these carrier frequency bands. Therefore, a half-wavelength spacing at a frequency band will result in less than (or more than) halfwavelength spacing at other lower (or higher) frequency bands.

A 5G mmWave capable UE is typically equipped with multiple antenna arrays. For example, in a design given in [27], there are at most four mmWave modules mounted on the top, bottom, left and right edges of the phone, respectively. Multiple mmWave antenna arrays are necessary to enable a good spherical coverage over the whole sphere and to circumvent human body blocking. In a benchmark codebook design, the beam codewords are designed independently for each array as assumed in [27], which is a suboptimal solution since the interaction and coordination between the arrays are ignored.

### B. CONTRIBUTIONS

A practical beam codebook design should at least take into account the following factors, 1) Antenna element type and gain (e.g. isotropic, dipole, microstrip patch); 2) Array layout (e.g. linear, rectangular, circular, cylinder) and placement if there are multiple arrays; 3) Requirements of codebook (e.g. codebook size, required coverage regions, phase shifter resolution); 4) Consideration about UE housing (e.g., display screen, battery); 5) The coordination among different arrays mounted on the same terminal. Although it might be able to model the antenna element type by approximation models [25], it is difficult, if not impossible, to analytically model the other factors, including the housing effects caused by a plurality of components inside the mmWave terminal with various size, shape and electromagnetic properties. Faced with aforementioned challenges, it is generally difficult to find an analytical method to generate the codebook. It is also impossible to find the optimal codebook by an exhaustive search because of its exponential complexity as O 2 bLK where b is the phase shifter resolutions, L is the antenna array size, and K is the codebook size. For instance, for a small array where b = 2, L = 4 and K = 4, there are 2 32 possible codebooks assuming that the analog beamforming codewords are ordered.

In this paper, we present a data-driven codebook design method. An important advantage of our method is that it can be applied agnostically with any antenna type, array layout and placement. The antenna information required for our method is simply the electrical field (E-field) response of each antenna element in a given layout, which can be obtained through electromagnetic simulation software (for example, high-frequency structure simulator (HFSS) by Ansys) or through measurements.

Our first algorithm is a Greedy algorithm, which sequentially selects the beam codewords to augment the spherical coverage. The performance of this algorithm relies on the quality of the candidate codewords pool as well as the codeword selection criterion. Our second algorithm is based on an unsupervised machine learning algorithm, namely, K-Means. In this algorithm, the angular directions are clustered based on their E-field response and then the beam codewords are optimized to improve the average gain of the clustered points. This clustering and optimization procedure is repeated until convergence.

The contributions of this paper are summarized as follows.

1) We formulate a beam codebook design problem from the perspective of maximizing the spherical coverage.

The optimization problem takes into account the amplitude and phase resolution constraint, as well as the codebook size. In addition, compared with the previous work (e.g., [27]), the two polarization components are both considered in the design. 2) We propose a data-driven approach for codebook design. The proposed approach, which takes as inputs the E-field response data from simulations or measurements, automatically generate the codebook without request of modeling the antenna element pattern, the housing effects, etc. 3) An upper bound of the composite radiation pattern is derived. The upper bound provides a reference for evaluating the performance of the designed codebook. 4) Comprehensive numerical simulations are provided to confirm the effectiveness and superiority of the proposed codebook design. The paper is organized as follows. In Section II, we formulate the problem of beam codebook design. In Section III, we present the design of a single beam with power and phase constraints, which lays the foundation for discussions of our algorithms. The upper bound of the composite radiation pattern is discussed in Section IV. Our two heuristic algorithms are provided in Section V and Section VI. The simulation results are shown in Section VII. Further discussions on the additional advantages of our algorithms are provided in Section VIII. A comparison with other modelbased method based on simplified E-field response data is given in Section IX. The paper is concluded in Section X.

Notation: Bold uppercase letter A and bold lowercase letter a represents a matrix and a column vector, respectively. A ≥ 0 implies that A is a positive semi-definite matrix. (•) T , (•) * , (•) H denotes the transpose, conjugate and Hermitian of a vector or matrix, respectively. a is the norm of the vector a. arg(•) ∈ [0, 2π) denotes the phase of a complexvalued input. mod(a, n) stands for the remainder of a divided by n.

## II. BEAM CODEBOOK DESIGN PROBLEM

The coordinate system used throughout this paper is shown in Fig. 1. The UE is placed around the origin. θ (φ) is defined as the zenith (azimuth) angle. Since the electrical field is a vector field, it is represented by three orthogonal components, denoted as (E R , E , E ), at each observation point on the surface of a sphere. We consider the E-field response in the far-field (Fraunhofer) region where the electromagnetic wave appears locally as a plane wave in any specified direction. As a result, the radial component, i.e., E R , is zero or vanishingly small compared to the other two components, i.e., E and E [25]. Therefore, for a given direction n, we only consider the E-field component and component, which are perpendicular to n as shown in Fig. 1.

Assume there are L antenna elements in an array. Let e (θ, φ) and e (θ, φ), ∈ {1, 2, • • • , L}, denote the complex-valued E-field response of the -th antenna element for the component and the component, respectively, at the direction (θ, φ). 2 Denote the E-field data in vectors as, e (θ, φ) [e 1 (θ, φ), e 2 (θ, φ), • • • , e L (θ, φ)] T , (1)

As mentioned in the introduction, the E-field data can be obtained through electromagnetic simulation or measurement, which is usually sampled on a mesh grid, for example, [θ, φ] = [0 • : q θ : 180 • ] × [0 • : q φ : 360 • ), where q θ , q φ are the simulation or measurement step sizes.

Let w [w 1 , w 2 , • • • , w L ] T denote the complex-valued weights applied on the antenna elements. Without loss of generality, we will assume the beamforming codeword w always has unit-norm throughout this paper, i.e., w 2  = 1. According to the superposition principle, the E-fields for the and components after applying the beamforming weights are given by

2 The E-field response in this paper denotes a product, i.e., r • E X , where E X (X = , ) is the E-field strength measured at a distance r to the origin when the incident power to the antenna element is 1 Watt. Since E X ∝ 1 r in the far-field region [25], the E-field response is independent of the distance r. Note that the E-field response in this paper corresponds to the term 'rE' in HFSS.

The realized beamforming gain is the sum of the realized gains of the and components [25],

where η 0 ≈ 377 is the impedance of the free space, M(θ, φ) e (θ, φ)e H (θ, φ) + e (θ, φ)e H (θ, φ), and ( 6) is obtained by plugging in ( 3) and ( 4) and noticing the unit-norm assumption of w.

We assume that the phase shifters are constrained to b bits, and the codebook W c has a size limitation

A codebook of small size will help reduce the beam sweeping time, power consumption as well as the memory space in the modem. There is also a requirement on the composite radiation gain pattern, which is the maximum over all the gain patterns of the codewords and is denoted as S (W c , θ, φ). The composite radiation pattern indicates the wellness of the spherical coverage of the codebook. Specifically, it can be used to identify coverage holes. The beam codebook design problem is formulated as below.

where the last equation (8c) encapsulates the magnitude constraint

as well as the phase constraint arg

When there are multiple arrays, we assume that only one of the antenna arrays is activated at a given time, which is a typical implementation assumption. As a result, the problem formulation is similar to (P1) with the exception that the composite radiation pattern is the maximum over all the codewords of all the arrays.

The utility function U (•) can be defined as the average gain across the whole sphere, or the xth-percentile of the gain over the unit-sphere (e.g., x = 20, 50). As mentioned in the introduction, the 3GPP specifies the spherical converage requirement for handheld UE (power class 3) in terms of the 50th percentile EIRP [7, Table 6.2.1.3-3]. 3 Throughout this paper, the utility function is defined over a uniform sampling over the sphere or a specified angular region. In particular, the CDF of the gain over the sphere is defined as,

Maximizing a particular percentile value (e.g., 50% requested by 3GPP) of the distribution is not an easy task when considering the mathematical tractability. A more tractable utility function is the average gain over the sphere, which is defined as

where the approximation in (12) comes from a set of N p uniformly distributed sampling points on the sphere, which can be obtained through a Fibonacci grid [28].

The problem P1 is non-convex and NP-hard due to the constraint (8c). In this paper, we provide two heuristic algorithms. As verified through our simulation based on practical phone design, the proposed heuristic algorithms have low complexities and provide satisfactory performance.

In the problem formulation P1, the flatness of each beam is ignored for several reasons. First, we are designing highpeak-gain narrow beams for data transmission instead of quasi-omni or wide beam for initial device discovery and sector-level searching, therefore there is no flatness issue in our designed narrow beams. Second, to establish a successful mmWave connection, the spherical coverage of the composite radiation pattern is a more relevant and effective metric than the flatness of the individual beam. Last, but not least, if the radiation pattern is severely irregular due to element pattern or strong housing effects, then it is impossible to design a wide beam with flat gain.

## III. DATA-DRIVEN DESIGN OF A SINGLE BEAM

Before presenting our beam codebook design, we first present the approach on the design of a single beam, which will be used in the Greedy and K-Means algorithms.

It is noteworthy that the beam design in the data-driven codebook is quite different from the conventional modelbased method in two-fold. First, the beam codeword is designed based on the E-field data, instead of being a steering vector, 4 or a weighted sum of a few steering vectors [21], or a concatenation of steering vectors on sub-arrays [12], [13], [15], [17]. Due to the directional element pattern and housing exp j 2π λ n T x where n = (sin θ cos φ, sin θ sin φ, cos θ ) T (see the definition of θ and φ in Fig. 1), λ is the wavelength, and x is the 3-D coordinate of the -th element. effects, the beam radiation pattern may point away from the intended direction. Second, the beam is carefully designed to take into account two polarization components, which is not considered in the prior work, e.g., [27].

Given the E-field response matrix M (θ, φ) at a given direction (θ, φ), or the sum E-field response over a set of directions, i.e., M = (θ,φ)∈A M(θ, φ), we want to design a beamforming vector to maximize the beamforming gain w * Mw under different constraints.

First, consider a simple case with sum power constraint. The optimization problem is as follows.

where λ max represents the maximal eigenvalue and the optimal w is the eigenvector corresponding to the largest eigenvalue. The solution value is denoted as B 1 and 2π η 0 B 1 is the maximum achievable beamforming gain.

### A. CONTINUOUS-PHASE UNIMODULAR BEAM DESIGN

In our beam codebook design, the beam codeword is subject to per-element constant power constraints. The problem with such constraint can be formulated as,

First, it is not hard to see that the optimal w should fully utilize the power, i.e.,

. A proof can be found in [29, Corollary 2]. Second, if rank(M) = 1, i.e., M = mm H , then the optimal solution is the co-phasing beamforming, i.e.,

. However, since e (θ, φ) is not a scaled vector of e (θ, φ) almost surely, rank(M) is larger than one almost surely and thus there is no closed-form solution.

In fact, since both the objective function and the constraints (w * i w i = 1 L , ∀i) are quadratic functions and M is positive semi-definite, ( 14) is a non-convex quadratically constrained quadratic program (QCQP), which is in general an NPhard problem proved by reducing an NP-complete matrix partitioning problem [30]. An approximate solution can be found by using the prevailing semi-definite relaxation (SDR) method [31] as follows.

Denote D i as an L × L all-zero matrix except that the ith diagonal element is 1. We relax (14) as a semi-definite programming (SDP) as follows,

A standard interior point method [32] or a more efficient row-by-row block coordinate descend method [33], [34] can be applied to solve this convex SDP problem. The worst-case complexity to solve a SDP is O(L 4.5 ), while the customized Algorithm 1 Gaussian Randomization Procedure (GRP) [35] Inputs: SDP solution W 0 with rank(W 0 ) > 1, and the number of randomizations N G .

1) Compute the eigenvalue decomposition of W 0 , i.e.,

, where ξ (n)  ∼ CN (0, I) are complexed-valued Gaussian random vectors.

3) Construct N G feasible solutions,

row-by-row method has a complexity of O(L 3 ) [35]. If the obtained optimal solution W 0 is of rank one, then we can write W 0 = w 0 w H 0 , and w 0 is a feasible optimal solution. On the other hand, if the rank of W 0 is larger than one, then a random approximation procedure [30], [35], [36] can be used to find an approximate optimal solution. The details of the procedure is shown in Algorithm 1, where N G realizations of w ∼ CN (0, W 0 ) are generated and the best one is selected and denoted as w 0 . The theoretical approximation accuracy is π 4 , i.e., the expectation of w H 0 M w 0 is no less than π 4 of the global optimum [30], [36]. In our simulation setup where L = 4 and rank(M) = 2, a rank-one solution is obtained in more than 99% of the cases. That is to say, SDR provides the optimal unimodular beam in more than 99% of simulation cases.

Besides SDP-GRP, another sub-optimal but more timeefficient algorithm is to sequentially optimize the phase of each element [29, Table 1] [37, Algorithm 2]. The details of the iterative algorithm is given in Algorithm 2 for completeness. The solution of Algorithm 2 is guaranteed to converge to a stationary local optimal solution satisfying the Karush-Kuhn-Tucker (KKT) condition [29], but may not be the optimal solution. The performance of the iterative algorithm depends on the choice of the initialization in Step 1.

As an option, we can choose the initial w as the eigenvector associated with the largest eigenvalue of M to increase the likelihood of convergence to the global optimum. Another option is to set the solution from SDP-GRP as the initial w, i.e., concatenate SDP-GRP and Algorithm 2. By doing so, the sequential optimization method is used to further improve the quality of the SDP-GRP solution and therefore the chance of finding the global optimum. The complexity of the iterative algorithm is O(L 2 ) [37]. Another alternative of Algorithm 2 is the power method-like approach given in [38, Section III] which, however, has a higher complexity as O(L 3 ).

### B. DISCRETE-PHASE UNIMODULAR BEAM DESIGN

In practice, there is also a resolution constraint on the phase shifters. By taking into account both the per-element power Algorithm 2 Iterative Coordinate Descent Algorithm for Beamforming Design With Per-Element Power Constraint [29], [37] 1) Initialize w and i ← 1.

2) Update w i as

3) Check convergence of the beamforming gain. If yes, stop; if not, let i ← mod(i, L) + 1 and go back to Step 2.

and phase constraints, the beam design problem is,

If M is not rank-deficient, it is proven that ( 18) is also a NP-hard problem [30], since it includes the max-cut problem and max-3-cut problem which are known to be NP-hard. An approximate solution can be obtained by applying the SDP-GRP technique shown above but with minor modifications. First, in this discrete-phase case, we have to run the Gaussian randomization procedure even if W 0 is a rankone matrix because of the phase constraints. Second, when constructing feasible solutions inside the Gaussian randomization procedure, the phases need be quantized. This can be done by replacing (16) with the following equation,

where the function

The approximation accuracy of the SDP-GRP solution is

[36], which is same as the case of continuous phase, i.e., π 4 , when b → ∞. Similar to the case of continuous phase, the sequential optimization method can be used to improve the quality of the SDP-GRP solution. The iterative process is done in Step 2-3 in Algorithm 3. It is not hard to see that Algorithm 3 will definitely converge since in each iteration, the phase of w i is assigned as the optimal value from the discrete set 0, 2π

On the other hand, when M is rank-deficient, the problem (18) can be solved with polynomial complexity of L, i.e., O

2 rank(M) [39]. Unfortunately, such algorithms for discrete phases have exponential complexity with respect to b and cannot be extended to the continuous phase case in (14) where 2 b is approaching infinity. In addition, the runtime of the algorithm when b is larger, e.g., b = 5, is much longer than solving a SDP problem. Therefore, we do not adopt this method in this paper.

Algorithm 3 Algorithm for Beamforming Design With Per-Element Power and Phase Constraints 1) Solve the SDP given in (15) and perform the Gaussian randomization procedure shown in Algorithm 1 where ( 16) is replaced with (19) to obtain a discrete-phase solution w. 2) Update w i as

3) Check convergence of the beamforming gain. If yes, stop; if not, let i ← mod(i, L) + 1 and go back to Step 2.

Last, it is not hard to see that B 1 (M) ≥ B 2 (M) ≥ B 3 (M) since the set of feasible solutions shrinks from (13), to (14) and (18).

## IV. UPPER BOUND OF THE COMPOSITE GAIN PATTERN

In the prior work, the upper bound has a uniform gain across the whole sphere by assuming all the elements are omnidirectional. However, this is not the case at mmWave band where the antenna element has an inherent directional radiation pattern.

In this section, we provide an upper bound for the composite radiation pattern. The upper bound is directly derived from antenna element E-field response data (i.e., e and e ) and independent of codebook size K . It provides a good reference for evaluation of codebooks. For example, the number of beams required for the composite pattern to approach the upper bound can be evaluated.

Mathematically, the upper bound is obtained by solving the following problem over the whole sphere (θ, φ)

The upper bound can only be achieved by a beam codebook consisting of the maximal eigenvector of M(θ, φ) for every direction. In other words, we have to remove codebook size limitation, per-element power constraint, and the discretephase constraint to construct a codebook being able to attain the upper bound.

Last, the upper bound for a multi-array setup is simply taken as the maximum over the upper bounds of each individual array.

## V. GREEDY ALGORITHM

In this section, we present a Greedy algorithm for the beam codebook design. The proposed algorithm greedily selects codewords from a candidate set as shown in Algorithm 4.

In Step 1 of the Greedy algorithm, candidate beam codewords are generated. We provide two possible methods to 

Insert the selected beam codeword into the beam codebook,

3) Stop if a certain stopping criterion is met; go back to Step 2 otherwise.

generate the candidate beam codewords in Section V-A. In

Step 2, given certain performance criteria, a beam from the candidate set is selected. In Step 3, check if the stopping condition is met. If the answer is yes, the algorithm is terminated and the selected beam codewords constitute the final codebook. Otherwise, Step 2 is repeated. Denote the size of the candidate beam set as N d and the codebook size as K . The complexity of the Greedy algorithm is mainly from Step 2, whose runtime is proportional to

Along with the complexity of O(N d L 3 ) to generate N d candidate beams, the total complexity is O(N d (L 3  + K )). Fig. 2 shows an example of the Greedy algorithm operation. A linear 1 × 4 patch antenna array along the z-axis with broadside direction being (θ = 90 • , φ = 90 • ), according to the coordinate system in Fig. 1, is simulated by HFSS. The 5 codewords are selected one at a time from a candidate set of 363 codewords to boost the composite radiation pattern (see Fig. 2(a)-Fig. 2(e)). It is important to note that the main lobe of the selected beams shown in Fig. 2(f) are naturally pointing to different directions without explicit or manual enforcement. In each step, the selected codeword naturally targets the region with the poorest coverage thus far. It is observed in Fig. 2(g) that the spherical coverage improves with increasing number of beams. The composite radiation pattern is compared with the upper bound in Fig. 2(i). The gap is less than 2 dB excluding a coverage hole located around θ = 95 • . The codewords selected in the next iterations are expected to cover this hole.

Note that for this simulated patch array, the antenna elements do not assume omni-directional radiation patterns. As clearly seen from the upper bound shown in Fig. 2(h), the array can cover only a half sphere (0 • ≤ φ ≤ 180 • ) because of the high front-to-back ratio of the patch antenna. As seen in the CDF curve shown in Fig. 2(g), the dynamic range of the upper bound is from -15 dB to 10 dB, namely, the front-to-back ratio is around 25 dB. In addition, the 3-dB contour of Beam 1, which is pointing to the VOLUME 7, 2019 FIGURE 2. Greedy algorithm operation on a linear 1 × 4 patch antenna array with 5-bit phase shifters. In this example, the candidate codewords are phase-quantized and magnitude-normalized eigenvectors corresponding to the maximal eigenvalues, and the selection criterion is the mean gain. Note that the beamforming gain is plotted in the dB scale.

directions away from the broadside, does not have a regular circular or ellipsoid shape.

In the following subsections, we discuss more details on the candidate codewords generation in Step 1, selection criteria in Step 2 and the stopping condition in Step 3.

### A. CANDIDATE CODEWORDS GENERATION

We provide two methods to generate the candidate codewords based on the E-field data. We first pick a set of sampling points on the sphere. This can be done by generating a Fibonacci grid ( θ, φ) [28] and rounding the points to the nearest simulated (or measured) ones (θ, φ). Then we generate the beamforming vectors pointing to these points. One option is to find the optimal or near-optimal codewords according to Algorithm 3. The second option is to first find the eigenvector of M(θ, φ) corresponding to the maximal eigenvalue and then obtain the beamforming vector by scaling the magnitude and quantizing the phase of the eigenvector to meet the per-element power and phase constraint. We will compare the performances of these two candidate codewords generation methods in Section VII.

### B. CODEWORD SELECTION CRITERIA

Codeword selection is performed based on the performance optimization criterion which defines the utility function the algorithm tries to maximize.

A possible design goal is to maximize the mean gain, i.e. the average gain of the composite radiation pattern over a given spatial coverage region. In each step, the codeword that maximizes the improvement of the mean composite gain is selected, i.e., w = argmax

where A is the coverage region of interest on the sphere. Another option can be the maximization of gain value at one or more percentile points. For optimization with multiple percentile points, weighted average of percentile points of interest can be considered, i.e., i

where β i is the weight. Single percentile point optimization is a special case with all but one percentile point set to be zero weight.

In the simulations shown in Fig. 2, the mean gain over the whole sphere is assumed as the selection criterion. Generally, the performance optimization criterion is a design choice which depends on the spherical coverage CDF requirements and link budget analysis, etc.

### C. ALGORITHM STOPPING CONDITION

The algorithm stopping condition can be taken from the codebook requirements. If there is a limitation on the codebook size, then the algorithm stops picking new codeword once enough codewords are selected.

The Greedy algorithm can also generate codebooks with variable size. In this case, stopping conditions are based on the spherical coverage performance, i.e., the algorithm is terminated once a required spherical coverage has been reached. For example, the requirement could be the average gain over an angular region A,

where Y is a threshold that can be assigned. Another example of stopping condition is related to the spherical coverage CDF requirement, where the selection stops when the gain value at one (or more) X %-tile is larger than a threshold Y ,

## VI. K-MEANS ALGORITHM

For the Greedy algorithm, care is needed to ensure that the candidate codewords sufficiently cover the whole sphere (or the angular region of interest). If the set of candidate beam codewords offered for selection does not cover certain directions well, the resulting codebook performance can be poor, for example, coverage holes at certain directions. In this section, we propose another algorithm called K-Means, which does not require careful constructions of the candidate codewords. As the name suggests, the core idea of this algorithm is based on the K-Means clustering, which is an unsupervised machine learning algorithm [40].

Given an initial set of

the algorithm proceeds by alternating between two steps: 1) Assignment step: Assign each direction to the beam, which provides the largest gain. Mathematically, this means partitioning the set of directions D into K subsets, denoted as

The set of directions D k is served by the beam w k and is defined as follows,

2) Update step: Optimize the beams to serve the directions in their associated subsets. This is done by solving the following optimization problem for 1 ≤ k ≤ K ,

Problem ( 30) is similar to the optimization problem (18) discussed in Section III. Hence, Algorithm 3 is adopted to solve this problem.

The algorithm is terminated when the average gain of the composite pattern no longer improves or assignments no longer changes.

The complexity of the K-Means algorithm concentrates on the Update step where the Algorithm 3 is run for K times in each iteration. Overall, the K-Means has a complexity of O(L 3 KN p N I ) where N I is the number of iterations needed until convergence [41]. As found in our simulations, the K-Means algorithm converges very quickly and N I is usually very small, i.e., less than 20.

Fig. 3 shows an example of the K-Means algorithm. The same linear 1 × 4 patch array considered in Fig. 2 is assumed. Each colored point in Fig. 3(a)-Fig. 3(b) represents one direction to cover. Note that for a uniform distribution of points on the sphere, there are less points around the polar regions than the equator region. The five different colors correspond to the five codewords. As seen in Fig. 3(a)-Fig. 3(b), the coverage regions change as the K-Means algorithm updates the codebook iteratively. Compared to the Greedy algorithm example in Fig. 2(i), there is no deep coverage hole in Fig. 3(f). There are some directions with gap as large as 4.5 dB. However, the directions fall within the back-of-the-panel regions, which has less gain as well as interest.

### A. CONVERGENCE OF THE K-MEANS ALGORITHM

The proposed K-Means algorithm is guaranteed to converge. This can be seen as follows. In the first step, the algorithm finds the best beam for each direction. In other words, the best assignment for a given beam codebook is obtained. Hence, the average gain increases (or keeps same) in this step. In the second step, for the directions served by the same beam, the algorithm finds out an optimal (or local optimal) beam to maximize the average gain over these directions. The average gain increases (or keeps same) in the second step as well.

Since the mean gain is monotonically nondecreasing in each iteration, and there is an upper bound on the mean gain, we can conclude that the K-Means algorithm always converges.

In the above example, Fig. 3(d) shows the convergence of the mean gain of the codebook. It is seen that the algorithm converges quickly within 4 iterations.

### B. INITIALIZATION OF THE K-MEANS ALGORITHM

For the initialization of the codebook {w 1 , w 2 , • • • , w K }, two options are considered. 1) 'Greedy': The initial codebook is generated from the Greedy algorithm shown in Section V. In other words, we concatenate the two algorithms. We first run the Greedy algorithm and then take the output of the Greedy algorithm as the initialization of the K-Means algorithm. 2) 'Uniform': First generate K uniformly distributed points on the sphere or the required coverage region. Then compute the codewords by normalizing the magnitude and quantizing the phase of the maximal eigenvector of the M matrix at these directions. This procedure is similar to one of the methods of generating candidate codewords given in Section V-A, but a small number of codewords are generated. The idea underlying this option is to ensure that the initial codewords are pointing to different and well-separated directions.

The 'Uniform' initialization is employed in the example shown in Fig. 3. Although the mean gain of this initial codebook is not good (see the mean gain at the 0-th iteration in Fig. 3(d)), the mean gain increases substantially with a single iteration comprising an assignment step and an update step. We will compare these two initializations in Section VII.

## VII. SIMULATION RESULTS

### A. SIMULATION SETUP AND DATA GENERATION

In the simulation, we consider a terminal operating at 28 GHz with three antenna arrays, where the first is placed on the left edge, the second is placed at the right edge and the third is placed at the back of the terminal as shown in Fig. 4. All the three arrays are 1 × 4 linear patch antenna arrays with half-wavelength spacing. Assume that the terminal is placed vertically in the y-z plane with the front facing +x direction. The three arrays are pointing to the -y, +y, -x directions, respectively. We assume that each antenna element is supplied with the same power, i.e. the per-element power constraint holds. The resolution of the phase shifters is assumed to be 5 bits. In addition, we assume that only one of the antenna arrays can be activated at a given time, which is a common practice.

The E-field data used in simulations is generated using finite-element electromagnetic simulator HFSS by Ansys. We assume the E-field data of each antenna element are available, i.e., e (θ, φ), e (θ, φ), in the form of discrete samples on a mesh grid, e.g. (θ, φ) = [0 • : q θ : 180 • ] × [0 • : q φ : 360 • ). We assume q θ = q φ = 1 • for results illustration in this paper; however it should be noted that this is not a necessary assumption for the algorithms, and other values of q can also be assumed, such as 5 • or 15 • . 

### B. PERFORMANCE OF THE PROPOSED ALGORITHMS

In this subsection, we compare the algorithms proposed in this paper. Depending on different initializations, we consider five implementations of the proposed algorithms as follows.

1) Greedy(Eigen): Greedy algorithm where the candidate codewords are phase-quantized and magnitudenormalized eigenvectors corresponding to the maximal eigenvalues. 2) Greedy(Iterative): Greedy algorithm where the candidate codewords are generated using Algorithm 3.

#### 3) K-Means(Greedy(Eigen)): K-Means algorithm ini-

tialized by the 'Greedy(Eigen)' algorithm.

4) K-Means(Greedy(Iterative)): K-Means algorithm initialized by the 'Greedy(Iterative)' algorithm. 5) K-Means(Uniform): K-Means algorithm where the initial codewords are beamforming to K uniformly distributed directions. For the two implementations of the Greedy algorithm listed above, the selection criterion is assumed to be the mean gain over the whole sphere, which is aligned with the optimization metric of the K-Means implementations for the sake of a fair comparison. 363 candidate codewords pointing to quasiuniformly distributed 363 directions are generated by either 'Eigen' or 'Iterative' approach. The angle separation of adjacent directions is around 10 • . The Greedy algorithms stop selecting new codewords when the codebook size limitation is reached. For the K-Means algorithm, the beams are updated by Algorithm 3 where the number of randomization in the first step is chosen as N G = 1000.

In Fig. 6(a), we compare the mean beamforming gain over the sphere. Our first observation is that the choice of the candidate codewords, i.e.,'Iterative' and 'Eigen', does not result in a significant performance difference. This can be explained by noting that, although an 'Iterative' codeword may be slightly better than the 'Eigen' codeword in a given direction, it may be worse than the 'Eigen' codeword when considering the average gain of the surrounding region of this direction. Our second observation is that there is nearly no performance difference across these implementations. Nevertheless, there may be meaningful performance difference for other antenna and terminal designs. Therefore, it is expected that the choice of the algorithm needs to be considered on a case-by-case basis. Finally, the mean gain increases with the codebook size and saturates when the codebook size is larger than 24. Actually, when the codebook size is 32, the mean gain is around 7.39 dB, which is very close to the mean gain of the upper bound, i.e., 7.56 dB.

In Fig. 6(b), we show the median gains produced by the algorithms since the 3GPP has defined the requirement of spherical coverage for handheld UE in terms of the median gain. Unlike the case with mean gains, there are more variations among different algorithms. This is reasonable since we set the mean gain as the common optimization metric and distributions with the same mean value could have very different median values. Furthermore, the difference in the median gains is very small when the codebook size is larger than 20, implying that all algorithms are converging to similar spherical coverage as the codebook size increases.

In our simulations, we find that the K-Means algorithm generally provides slightly better performance than the Greedy algorithm, but not in all cases. In particular, it is less likely to find coverage holes in the codebooks generated by K-Means algorithm than those by Greedy algorithm. However, the Greedy algorithm is much more flexible than K-Means algorithm. First, there are many possible choices about the utility function and stopping condition in the Greedy algorithm, while the K-Means has limited options. In this paper, we only consider the metric of mean gain for the K-Means algorithm. Second, the Greedy algorithm can generate variable-sized codebooks, whereas the codebook size has to be determined before running the K-Means algorithm. To sum up, the choice of the algorithm depends on the codebook requirements as well as the E-field data.

## VIII. ADVANTAGES OF THE PROPOSED METHOD

Our proposed method can be easily configured to deal with different antenna setups and to meet a variety of requirements on the beam codebook. In this section, we show several such cases.

In this subsection, we compare the proposed method with two other designs. The K-Means(Greedy(Iterative)) algorithm is assumed here for the performance comparison purpose.

The benchmark beams are designed to point to certain directions. In this paper, we assume that a benchmark codebook for a single linear array consist of K beams pointing to directions arccos -1 + 2k-1

# K

, where k = 1, 2, . . . , K [15], [16], [20]. For example, a beam codebook of size 4 consists of codewords pointing to 138.6 • , 104.5 • , 75.5 • , 41.4 • with respect to the array axis, respectively. The beam codewords are computed as, To have a fair comparison, we adopt its generalization to 2 bphase codebook shown as follows [42],

for 1 ≤ ≤ L, 1 ≤ k ≤ K , where x rounds x to the nearest integer less than or equal to x. The 802.15.3c codebook basically consists of K codewords having (approximately) progressive phases.

## A. JOINT DESIGN OF MULTI-ARRAY CODEBOOK

When there are multiple arrays mounted on the terminal, such as the three patch arrays as shown in Fig. 4, a conventional design may assume the same set of codewords for each array [27]. This assumption restricts the codebook size to be an integer multiples of the number of arrays. In contrast, there is no limitation on the choice of codebook size in our proposed algorithm, as seen in Fig. 6. More importantly, the conventional design does not take into account the possible overlapping of the coverage regions of different arrays and therefore the generated codebook may include codewords pointing to similar directions.

As shown in Table 1, the proposed codebook is better than benchmark and 802.15.3c codebooks in terms of the mean and median gains, in most of the cases. The advantage of the proposed algorithm is large especially when the codebook size is small, i.e, K = 12. When the codebook size increases, the performance of all the algorithms approach the upper bound and thus are similar to each other. The advantage of the proposed algorithm is clearly seen in Fig. 7 where the 3-dB beam contours are shown. In the benchmark codebook, beam 1 and beam 4 associated with the back array is pointing to the regions which are also partially covered by the beams from the other two arrays, i.e. beam 10-11 and beam 6-7. Similarly for the 802.15.3c codebook, beam 1 associated with the back array is pointing to the regions which are also  covered by the beams from the other two arrays, i.e. beam 6-8 and beam 10-12. By contrast, the proposed codebook displays a much better coordination among different arrays by automatically allocating different number of beams to the arrays and avoiding the beam overlapping.

### B. FLEXIBLE ADAPTATION TO REQUIRED COVERAGE REGION

In certain scenarios, the beam codebook is required to cover a part of the sphere rather than the whole sphere. For instance, when the user is holding the phone next to the head to make a call, the phone should not beam towards user's head, because of the high blockage loss of human body to mmWave signals and the radio frequency exposure compliance [43]- [45].

Our proposed method is capable of adapting to varying coverage region requirement. In the Greedy algorithm, we can define utility function U over the region interest instead of the whole sphere. For example, the over a region could be optimized as shown in (24). For the K-Means algorithm, we can the directions D to keep only directions within coverage region.  

respectively. The regions are highlighted by black boxes drawn in Fig. 8(a) and Fig. 8(d). As seen in the figures, the resulting beam codewords are naturally concentrated in the required region. As a result, the composite patterns in these two cases have a less than 2 dB gap to the upper bound in the required region in contrast to a more than 10 dB gap out of the required region. When the coverage region is the halfsphere 0 • ≤ φ ≤ 180 • , we find that the array on the left edge of the phone is turned off automatically as shown Fig. 8(d), since the required coverage region is at the back of it.

### C. STRAIGHTFORWARD EXTENSION TO DIFFERENT MODULE PLACEMENT

Our proposed method can deal with any kind of antenna type and placement on the terminal. Here, we show an example with the same antenna arrays as Fig. 4 but a different placement. Specifically, we assume the arrays are distributed on the left edge, right edge and top edge. As shown in Table 2, the proposed codebook provides better mean and median gains than the benchmark and 802.15.3c codebooks in all the cases. Fig. 9 compares the 3-dB beam contours when K = 12. We find that the beams of benchmark and 802.15.3c codebook are largely overlapping in the upper half-sphere (0 • ≤ θ ≤ 90 • ), which explains why their spherical coverage is worse than the proposed codebook which maintains a much better angle separation among 12 beams.

Last, comparing Table 1 and Table 2, we find that the first module placement results in better beamforming gains that the second placement. In other words, it is better to put the third array on the back than on the top edge, if the optimization target is the spherical coverage. 

## IX. FURTHER COMPARISONS WITH SIMPLIFIED E-FIELD DATA

To provide a comprehensive comparison with conventional model-based approach and illustrate the effectiveness of the proposed method in general cases, we perform more simulations based on simplified E-field response data besides HFSS data.

The uniform antenna array (ULA) with exactly same antenna element is assumed in the comparison. The E-field data are generated for the angular directions uniformly distributions over the spatial frequency, i.e., θ = arccos(x), where x = -1, -(a -1)/a, . . . , (a -1)/a, 1. In this section where 1 ×L ULA is assumed, we choose a = 30 L. The E-field data at the angle θ is,

and e (θ ) = 0, where θ is angle with respect to the axis of the linear array, p(θ) is the element radiation pattern. The K-Means algorithm is used for the comparison, and the K-Means algorithm is initialized by the benchmark codebook. In addition, 5-bit analog beamforming is assumed.

In the ideal case of omni-directional antenna and half-wavelength spacing, the codebook design has been well studied and our proposed method does not bring further improvements. However, our proposed method does bring large gain when designing a codebook for a practical antenna array where the ideal assumptions do not hold. 

### A. IRREGULAR ANTENNA SPACING

We first consider a scenario where the antenna array is not half-wavelength, which results from form-factor constraints or the multi-frequency bands the array has to support. In particular, a 1×4 ULA with d = 0.65λ is simulated. The number 0.65 is chosen by assuming that the antenna array has the antenna spacing of 5 mm (i.e., half wavelength at 30 GHz), and operates at the 39 GHz band. We want to generate a codebook of 4 beams. Fig. 10 illustrates the radiation pattern of the 4 beams of each codebook. As seen in Fig. 10, there are strong side lobes when the main lobe is pointing away from the broadside direction. The proposed method can adjust the beamforming direction of the beams to fully utilize the side lobes to achieve a better spherical coverage. It is worthy to note that the adjustment is done automatically by the proposed algorithm based on E-field response data. By contrast, the benchmark and 802.15.3c codebooks do not adapt well to the spacing change. The CDF curves of these three codebook is illustrated in Fig. 11. It is clear that the proposed codebook shows much better spherical coverage than the other two codebooks. The median gain values are 4.76, 5.09, 5.38 dB, respectively.

Last, the side lobes are also used in [10], [11] to achieve a good coverage. However, their handcrafted approach requires careful design of the beamforming weights and cannot apply to arbitrary antenna spacing.

### B. THE DIRECTIONAL ANTENNA RADIATION PATTERN

Now we consider another case where the antenna is directional. A simple model of directional radiation pattern is as follows.

p(θ) = sin q (θ ), (34) where q controls the directionality of the radiation pattern. A 1 × 4 ULA with half-wavelength spacing is considered here.

Fig. 12 shows the comparison of the beam patterns when q = 1 in (a)-(c) and q = 3 in (d)-(f). The dashed envelope represents the upper bound. As the parameter q becomes larger, the element pattern as well as the upper bound becomes more directional. As seen in the figure, as q increases, two out of the four beams in the benchmark codebook have diminishing gains and provide negligible contribution to the spherical coverage. Similarly, one of the 802.15.3c codewords has relatively small gain. By contrast, the proposed codebook is capable of tweaking the beam direction automatically. The beams are moving towards the broadside direction as the antenna element becomes more directional. The median gain of each codebook is listed below the figures. The proposed codebooks have the largest median gains.

## X. CONCLUSION

In this paper, we have formulated the beam codebook design problem to enhance the spherical coverage of the mmWave terminals. The codebooks designed based on the isotropic antenna assumptions will not work well for mmWave terminals, due to the inherent directional radiation pattern of the mmWave antenna element and the impact from housing components of the terminals, such as coupling, blockage, absorption, reflection, etc. We proposed a novel approach to automatically design the beam codebook solely based on the E-field response of each element. First, a flexible Greedy algorithm is proposed to choose a subset of the candidate codeword pool to form the final codebook according to any given criterion. Second, a machine learning based iterative algorithm is proposed to generate the codebook. Through simulations, we find out that the composite radiation pattern of the proposed codebook is better than the benchmark and 802.15.3c codebook. Actually, the performance of the proposed beam codebook is shown to be able to approach the upper bound as codebook size increases. Furthermore, the proposed data-driven method can be used for any kind of array layouts, placement and antenna type. It is a very generic method of designing good codebooks a wide range of practical scenarios where the conventional model-based method does not work well.

Note that the proposed method depends closely on the E-field data. There are several possible factors distorting the far-filed E-field response. For example, the protection case of the phone and the hand grip of the users [26], [46]. We model the hand grip impact on the E-field response and propose an adaptive beam codebook generation method in [47].

Last, even without the distortions by hand grip, the E-field response data from simulations or measurements may be different from the true response. For instance, there may be deviations between the antenna and phone model used in the simulations and the manufactured ones. The measurement data may also be inaccurate because of the heating of the phone in the measurement process. A future direction to improve the proposed method is to design a robust beam codebook taking into account these deviations.

