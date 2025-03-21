# INTRODUCTION

Sensor arrays play an important role in spatio-temporal signal processing with applications spanning across multiple fields such as electromagnetic, acoustics, ultrasonic and seismic processing systems. Fundamental technology used in some of those applications includes radar, sonar, navigation, wireless communications, electronic surveillance and radio astronomy [1][2][3]. By exploiting the diverse waveform from its multiple antennas, multiple-input multiple-output (MIMO) radar transmits a probing waveform that can be chosen at will to maximize the power around areas of interest. Antenna pattern design for MIMO radar has become a popular research topic in recent years [1][2][3][4][5][6][7][8]. There is a vast amount of applications in signal processing and communication systems where the discrete signal samples are sparse in some domain such as time, frequency, or space. However, novel methods seem to outperform conventional techniques, regarding both complexity and optimality [9].

Sparse antenna array has several advantages in the high resolution thinned configurations for phased array radar and MIMO radar. However, because of array thinning, the side lobe level increases and subsequently leads to the grating lobe [4]. In this case, maintaining the approximation performance and preventing the grating lobe present two major challenges for a MIMO radar with sparse antenna arrays [1, 4, and 10].

Each field has developed similar tools, algorithms, and reconstruction methods for sparse signal processing which are; sampling: random sampling of bandlimited signals, compressed sensing (CS) [11], channel Estimation in Orthogonal Frequency Division Multiplexing (OFDM) [11][12][13], and finally the calibration for the mutual couping between antenna elements [14][15][16][17][18].

In this work, without any loss of generality our focus is on automotive radars, for which in the last few years it have been transformed from being a niche sensor to becoming standard even in middle-class cars. With Euro-NCAP ratings now requiring automated braking and pedestrian safety functionality, radar is often identified as the best suited sensor for this purpose. A selection of technology trends addressing some common requirements can be found in [19, and 20] The remainder of this paper is organized as follows: In Section II, we derive the MIMO radar system model and extend the radiation and receiving mechanism of a radar formulated for sparse arrays. In Section III, classical Fourier based steering matrix formulation is derived for sparse arrays. In Section IV, multi-objective design and optimization of a sparse MIMO array is studied. Performance parameter definitions, smart initialization for fast convergence and minimization of mutual coupling effects are proposed. Finally, results and conclusions are drawn in Section V. Performance of the method is illustrated on four uniform sparse arrays, namely, AnkaraA/B and CoruhA/B arrays, and interesting directions for future work are pointed out.

## II. SPARSE MIMO RADAR SYSTEMS

For a multiple-input multiple-output (MIMO) radar system each transmitter (TX) signal is rendered distinguishable from every other TX by using appropriate differences in the modulation, such as, different digital code sequences. Each receiver (RX) correlates with each TX signal, producing a number of correlated outputs equal to the product of the number of RXs with the number of TXs. The outputs are deemed to have been produced by a number of virtual receivers (VRXs), which can exceed the number of physical RXs.

A transmit signal reflected from a reflecting object, and received and correlated by a receiver results in a digitized skin return signal that is the same as would have been produced by a transmit and receive antenna colocated at coordinates which are the sum of the actual transmit and receive antenna coordinates; such signals, called VRX signals, are further combined according to delay and doppler shift to resolve targets in the four dimensions of azimuth, elevation, range and doppler.

Antenna aperture and the desired field of view defined in the spherical coordinate system are illustrated in Fig. 1. Antenna aperture is generally shared by the individual transmitting and receiving elements. Their positions for the uniform linear and rectangular arrays are well-known. Sparse array (SA) elements in general can be located anywhere inside a given physical aperture. However, uniform sparse array (USA) elements, as the term proposed here, can only be located on the grid points defined by a reference fully populated uniform array with largest possible inter-element spacing values as shown in Fig. 2.

## A. A Radiating Antenna Aperture

Let us examine a radiating planar aperture where the radiated signal strength is proportional to the surface integral across the aperture of the current at each point weighted by a phase factor (with reference to the origin) that is a function of the position in the aperture and the field point for which the response is to be calculated. If the current distribution is r(y,z) then the relative gain in the field point , , is given by [21] , , ; = , ;

, ;

(

where S is the planar antenna aperture, A is the scaling constant, is the excitation current where , ; = | , ; | ! , ; with a phase " with respect to the origin, # = 0, , is the primed cartesian (source) coordinates, , , is the unprimed spherical (field) coordinates, is the wave vector where % = | | = |%& ' | = 2 / * = 2 + * /,, -and + * are the wavelength and the center frequency for the narrow band transmission respectively, & ' is the radial unit vector in the direction of ., / , ( is the scalar (dot) product operator, is the exact one way source to the field poin displacement vector, and dependence to the field point brings the variables , , to the left side.

For field points in the far field the vectors and are approximately parallel (Fig. 1)

and the radiated signal with respect to the reference phase at the origin (1) simplifies to

where the scaling factor is ignored. The above integral becomes

where A, B = sin sin , cos . Note that is the inverse Fourier transform of the aperture distribution , and r is the Fourier transform of the broadside pattern where this pattern is defined only for the real angles for which A G + B G < 1.

For a single infinitesimal current element at an arbitrary location # ; , ; on the aperture

the radiated field simplifies to

where the current source amplitude directly contributes to the field with its propagation delay.

Let us assume a rectangular aperture defined by 0 < y < N OPQ , and 0 < < R OPQ , and uniform spatial samples are at the source points S , n for S = 0, 1, 2, … U -1 , and V = 0, 1, 2 … W -1 , and N OPQ = U -1

and R OPQ = W -1 , and and are the horizontal and vertical sampling intervals (Fig. 2). The infinitesimal currents are located on the rectangular XU × WZ grid points

The superposition of individual contributions is accurate if mutual coupling between the source elements are ignored the radiated field can be calculated as follows,

where g, = /h, and g, = /h. For a uniform sparse array using the same physical antenna aperture

Oc* (10) where ; are the sparse samples of , and are non zero only at the physically available positions. For a non uniform sparse array those exponential coefficients are not the regular Fourier coefficients.

## B. A Receiving Sparse MIMO Antenna Array

For a single-input single-output (SISO) radar the induced current at the receiver, , due to multiple targets can be assumed to be in the form

where A is the two-way spread factor, , is the complex-valued skin return with real-valued radar cross section and the phase return for the t'th target at the field coordinates , , + Q and + "Q are the antenna patterns for the transmitting and receiving elements, Q and "Q are the exact transmitter to target and target to receiver displacement vectors forming the two-way propagation path, respectively and other parameters are defined in (1).

Assuming uniform antenna elements and no tapering over the elements, ignoring common terms, the received signal in the far field with respect to the reference phase at the origin (13) can be simplified similar to (4)

] , e !7 p j q 89: i 89: i > p j q ?@8 i k cb (12) where !,< is the received signal at the j'th RX due to the i'th transmitted signal, is the received signal at the p'th VRX where

VRX created by the i'th RX and j'th TX couple located at the points

! for 1 ≤ s ≤ U and 1 ≤ t ≤ W as illustrated in Fig. 2. In this fully populated uniform rectangular array (URA) all possible TX-RX couples create UW virtual elements located over a virtual aperture of 2N OPQ × 2R OPQ where a sorted list for those couples S, V can be created using an order number l where 1 ≤ l ≤ n = UW, and each l corresponds to a single S, V pair assuming no overlapping occurs. Note that for a sparse MIMO array the number of physical elements, n ; , could be much less than n (Fig. 2).

As an illustrative example let us set both inter-element spacings Q and to /2, and this column-wise vectorization of the received signal at P virtual elements yields the weighted sum of T vectors which are commonly referred to as the steering vectors

where we can define the steering vector, , as in general the phase distribution induced on virtual array elements for a single target in the far-field at a given target angle its elements are in the form

Once again for a uniform sparse MIMO array sharing the same grid space with a fully-populated array only a few number of VRXs could be available and (15) reduces to

### III. ANGLE BEAMFORMING FOR A SPARSE MIMO RADAR

Recalling the properties of Fourier transform and its inverse discussed in Section II. B and using (8), (10), and (11) the received signal pattern for a full-populated uniform array for some , can be calculated simply by

where the received signal at the virtual array elements form the received signal (column) vector r of length n, and v is the steering (column) vector for the same array evaluated at , . One can oversample A, B uniformly for the received signal pattern The corresponding non uniform samples in the angular domain calculated below are illustrated in Fig. 3.   

where the above equation is valid only for real angles for which A G + B G ≤ 1 is satisfied, and where x and x are positive integer oversampling factors for -and -axes, respectively (Fig. 3). Now let us sort those angular samples into a single (row) vector, and evaluate the steering vector at each row yielding the angle beamforming matrix B, the received signal pattern can be calculated

where ‡ is the column vector for the received signal pattern, u is calculated in ( 16), w is defined in (15), and where B is the angle beamforming matrix with a size X U -1 W -1 x x Z by n.

For the hardware implementation of a multi-resolution B, both oversampling ratios, x and x , can be set to be multiples of 2 and the largest of those can be used to calculate a vector look-up table for the list of orthogonal set of Fourier coefficients.

To obtain a 2D pattern with 512 azimuth and 256 elevation angle samples, ‡ should have 131,072 row elements. For a virtual array of 192 elements B is expected to have 25,165,824 complex coefficients to be calculated or stored in the radar hardware for a general sparse array. However, for a USA those exponential coefficients become regular, and the number goes down to only 512 values. This brings a great advantage to USAs for their hardware implementations.

### IV. MULTI-OBJECTIVE DESIGN AND OPTIMIZATION OF UNIFORM SPARSE ARRAYS

For a uniform sparse array both the physical and virtual array elements are thinned and l is non zero only for its n ; elements where n ; < n [10]. Deleting the zero equations ( 21) simplifies to ‡ ; = ˆ;w ; (22) where both columns of ˆ;, and rows of w ; are reduced to n ; , and the thinning/sparsity ratio is defined as = n ; /n ≤ 1, and where a fully populated array this thinning ratio is 1.

## A. Optimizing Parameters

In practice radar design engineers more than often need to satisfy multiple contradicting objectives for the same desired antenna array. The main optimization constraints are; 1) usable field of view (uFOV), 2) beamwidth (BW), 3) the total number of physical elements (N), and 4) the peak-to sidelobe ratio (PSLR). In addition to those here are some additional practical considerations.

## Physical size limitations:

The TX and the RX antenna elements in practice have finite physical dimensions, namely their width and heights which limit the minimum inter-element spacing values, and those spacing values limit the horizontal and vertical uFOV values, respectively. A densely packed ULA and URA are directly affected by this limitation. This is effective whenever any size dimension is larger than λ/2.

## Mutual coupling:

The TX and the RX groups should often be physically separated by defining group separation distance to decrease the inter-group mutual coupling [1]. Here we assume that the mutual coupling among the same type of elements are calibrated digitally.

## Antenna element sharing of different arrays:

For multi-functional radars some of the TX and the RX elements are often shared between different scan modes. The antenna array design and optimization for all scans need to be done simultaneously. As a practical approach, the physical elements for a simpler scan mode could be forced to be used on some other complicated antenna configuration. This provides an effective utilization of the array aperture by an initial enforcement of some of the element positions in the design and optimization of a sparse array accordingly.

Hardware implementation constraints: Antenna elements are fed by transmission lines or waveguide structures whose layouts are usually implemented on a separate neigboring hardware board. The transmitted and received signals' layout should also be fed from another layer. As a design choice a central region can be preferred to keep all the transmission lines approximately equal in length. Then, this central region needs to be defined as a forbidden zone for the array elements.

In this work, thinning of fully populated uniform MIMO antenna arrays to form effective sparse arrays are examined as for their capability of improving usable field of view (uFOV), beamwidth (BW), and peak-to-side lobe-ratio (PSLR) using fewer physical antenna elements, simultaneously. The detailed definitions for those parameters are given in the following sub-sections.

## i. Peak-to-side lobe ratio (PSLR):

Further to this discussion for a given target range and velocity the peak-to-side lobe-ratio (PSLR) should be considered. Maximum skin-return for a target is given by

where , is the direction of the brightest signal observation in the FOV, and the maximum side lobe level is given by

where ; , ; is the direction of the largest side lobe in the uFOV, and where ‡ • ' is obtained by setting ‡ ; to zero inside its main lobe region. This side lobe have the potential to create false targets even this side lobe is outside of the (operational) FOV when FOV ≤ uFOV.

The peak-to-side lobe ratio (PSLR) can be calculated by n'" , ; ; , ; = 20 ""u b* y u m‰P7 u O;•• z.

(25)

Note that for uniform and isotropic elements, assuming mutual coupling to be shift-invariant, and (in the presence of multi-targets) ignoring the interference between the skin returns of neighboring targets the PSLR becomes independent of the target direction.

ii. Beamwidth for uniform arrays:

The first-null-, and the half-power-beamwidth can be calculated as follows [22] •--= = sin b y 1 " z (27)

where W is the number of uniform linear array (ULA) elements, •-˜m and •--= are the half power beam width (HPBW), and the first null beamwidth calculated in radians, and where and " = W -1 are inter-element spacing and aperture length in terms of wavelength, respectively. Eqns ( 27) and ( 28) are valid for the cross sections of uniform rectangular (URA) arrays for their horizontal and the elevation cross sections, separately.

## iii. Side lobes, Grating lobes and Usable FOV:

ULA and URAs, by definition, have constant inter-element spacings, and at any target angle the inter-element phase differences are also constant which are ideally zero at the target angle and all elements contribute constructively. However, for field angles retreating from the main lobe moving along one of the axes, these phase differences with respect to the array center begin to rotate for the furthest elements the fastest. First null occurs when the two elements furthest to the array center are out-of phase with respect to this center by approximately ± yielding the first minimum. Those far elements are W -1 /2 meters away from the array center with a phase difference of ±oe g W -1 the first null is observed approximately at ± sin b 1/ g W -1 radians, respectively. This approximation is accurate within 0.6, 0.4, 0.2, and 0.1 degrees for W = 15, 18, 25, and 35, respectively. Retreating further from the broadside angle while furthest elements' phase rotations turning back to in-phase, we observe the second to the last elements to be approximately out-of phase creating the second minimum. In this narrow angular region bounded by those two minima all except the last two elements are mostly in-phase causing the largest side lobe. Side lobes gradually decrease due to increasing incoherence between the elements until we reach the half way to the first grating lobe. For an odd numbered ULA all radiations cancel each other completely leaving the only one in the center to yield the minimum side lobe level of 1/W. This phenomenae occurs independent of the number of elements or their spacings, and this first side lobe sets the PSLR approximately to -13.8 dB. Fig. 4. Uniform linear arrays (ULA), g = 0.5, (dashed) W = 8, (dashed dot) W = 16, and some examples to (cross) a sparse array (SA) with g = 0.5, and W = 8 with nonuniform positions g = 0, 1.07, 2.52, 3.79, 4.48, 4.98, 5.86, 7.5, and (plus) a uniform sparse array (USA) with g = 0.5, and W = 8 using the positions of (dashed dot) as reference for which are thinned to 0, 3, 5, 7, 8, 10, 14, and 15.

Simple heuristics helping us to understand the interactions between ULA and URA elements also help us to understand why sparse arrays have much lower skin-return near (and even inside) the expected main lobe. Due to the irregularity of sparse element positions we expect more than just two elements to be out of phase away from the main lobe as illustrated in Fig. 4. In-phase interactions between elements become rapidly incoherent yielding a much smaller beamwidth. However, due to the conservation of radiated power the side lobes cannot be supressed but spread across the half-hemisphere, or can be optimized to be pushed outside of a given FOV. Grating lobes occur at angles when all of the array elements are perfectly in-phase, and they are constructively contributing to the received signal pattern equivalent to the main lobe. Large side lobes, however, are not grating lobes, they require only the complex sum of all the contributions to be comparatively large, allowing some inter-element phase mismatching, and even some distructive interferences between the elements.

No grating lobe appears for g ≤ h/2. Otherwise, for larger spacing values each target creates its own false target image(s) for which each image corresponds to a wrapped phase difference of some multiples of ±2oe. False target images, or equivalently the grating lobes of a target, occur at angles with respect to its source target angle. The number of observable grating lobes increases as the inter-element spacing increases as shown in Fig. 5.

Usable FOV (uFOV) can be defined as the maximum grating lobe-free angular extend around broadside where outside of the uFOV a flipped (with respect to the origin) replica of the interior pattern which carries no additional information. For a fully populated ULA a target located at creates grating lobes at angles ¢• = sin b = , for V: -1 < = ≤ 1, and for V = 0, ±1, ±2 … (29) 1 One sided angular extend. 

For = /2, and = /2, the first grating lobe occurs for V = -2 at ¢• = -/2 allowing the usable angular extend with D--F = {-/2, /2} (Fig. 1). Similarly for = , = /6, the closest grating lobe occurs for V = -2 at ¢• = -/6, then the usable angular region becomes D--F = {-/6, /6} as suggested by (30). Here note that in practice, the physical size of elements limit the minimum possible inter-element spacing values both on the horizontal and the vertical. For an element width of two wavelengths azimuthal uFOV is approximately limited to 14.48 degrees as shown in Table I. All targets outside the uFOV are expected to create false images stacked inside the uFOV, this becomes a problem when the antenna gains for the individual elements do not attenuate outside the uFOV sufficiently.

Above discussion shows that ULA and URAs often become unpractical even under these two constraints. Additional degrees of freedom are necessary. Sparse arrays can be designed to provide optimum solutions both for avoiding the grating lobes by their irregular element positions. They also provide very high angular resolution by allowing much smaller inter-element spacing values.

In this section, a practical design procedure for grating lobe-free sparse array with high angular resolution is proposed.

# TABLE II

## Algorithm: Sparse array optimization desired parameters:

• array dimension (1D/2D/3D), and let us assume 1D as an example.

• available number of TX and RX elements, W Q , W "Q , respectively, • uFOV, and BW both for azimuth and elevation, constraints: 

## B. Design and Optimization of a Uniform Sparse Arrays

Examining Section (IV.A) it is safe to say that for uniform arrays a desired uFOV BW can be improved only by increasing the antenna length " , or the aperture size and so with a larger number of elements W . Thus, for given FOV and W, BW improvement is not possible with uniform linear and rectangular arrays. This is due to the fact that required FOV and BW values are sufficient to determine the size of the fully populated aperture and which could well be over the practical limits. Additional requirements for a specific implementation becomes even more stringent once the physical size of elements and the mutual coupling constraints are also to be considered. Therefore there is a need for an efficient way to design and construct TX/RX arrays utilizing thinning of arrays, and allowing larger apertures with much less elements, hopefully without receding the first two constraints considerably.

Let us assume that initial constraints are only the maximum number of elements and available physical antenna aperture, and all other parameters are to be optimized without any loss of generality. Radar scan type under consideration will determine the dimension of the array. Hardware constraints limit the available number of array elements. Further, operational environment might be requiring a minimum BW value. Operating frequency and the prefered implementations determine the element size requirements. Initial simulations for mutual couplings can provide insight about some horizontal and vertical separation distances, " O , , and " O , for the two axes to keep those coupling under some threshold. Physical and virtual element sharing of a previously designed array would enforce some positions as an initial value for the optimization (See Table II.) At this initial step, the desired BW and uFOV values determine the minimum aperture length/size and minimum inter-element spacing, respectively which yield the corresponding grid space for the reference fully populated virtual array using (27) through (30) (Table II). Reader can refer to the literature on various approaches in constructing of such virtual arrays. Available number of TX and RX elements determines the targeted thinning ratio as discussed in (22). Enforcement of initial element positions should be done on the same grid space.

As an iterative process, random or some type of preferred search algorithm is performed to determine successful arrays for their PSLR where each candidate is to satisfy all the constraints. Iteration is terminated if desired PSLR, or maximum number of iterations is reached. Further stopping criteria is met if last three PSLR values are withing significance (0.5 decibels).

The desired and the constructing parameters can also be optimized using an outer loop. In general, this optimization can well be constructed for a different set of constraining parameters. There is a vast amount of work offering improved convergence including, evolutionary algorithms and gradient descent type analytical approaches [23] which will be studied in the future. Here we propose a heuristic approach to illustrate fast convergence to a satisfactory 'locally optimum' array.

## iv. A heuristic initialization approach (HIA) for fast convergence:

Firstly, low PSLR requires the grating lobes to be moved outside of operational FOV. This sets the grid sizes using (30), and Table I. Secondly, element positions need to be optimized for smaller PSLR. For a large side lobe overall in-phase contributions are expected to be large, and this generally occurs when the frequency of a certain inter-element spacing value is much higher than others. Thus, large side lobes can be spread across the half-hemisphere by setting the spacing values to be irregular (Table II). However, the total radiated power being conserved the overall sidelobe levels are expected to rise. PSLR reduction becomes possible when the Empirical Cumulative Distribution Function (ECDF) is forced to a smooth. One can initialize the spacing values by forcing their ECDF to be linear (uniform distribution) as proposed below.

A linear USA with N elements has W -1 inter-element spacing values, = , which can be set to be empirically uniform [23].

where O<= is the minimum inter-element spacing, for W ≥ 3

and where W -1 spacings are placed between N elements which are located between ¾ OPQ and ¾ O<= .

Let us first set the reference grid space to h/2 for a grating lobe-free pattern. Ignoring the element size constraint the minimum spacing can be set to the reference grid size, O<= = h/2. For " g = 11, and W = 5 we calculate Δ = 3h/2, and spacings are linearly increasing as given by 2 = /h = {1, 4, 7, 10} yielding element positions 2# = /h = {0, 1, 5, 12, 22} for ¾ O<= = 0. This yields a linear ECDF, À Á = = 2 + 2 = /h /12. All positions are in the reference grid space.

Secondly, using the same reference grid space, for an element size of 2h to avoid any overlapping we need O<= = 2h. Then, we calculate Δ = h/2, and spacings are linearly increased as 2 = /h = {4, 5, 6, 7} yielding positions 2# = /h = {0, 4, 9, 15, 22}. This also yields a linear ECDF, À Á = = -3 + 2 = /h /4. No grating lobes are expected since the ECDF is smooth, and the positions are located on a uniform grid size of h/2. Please note that in both examples a random shuffling of the spacing ordering will change the element positions but not the ECDF. Each alternative configuration will yield to a different signal-return pattern. This requires search iterations for the optimum spacing ordering for the best PSLR. Similar to the second example, let us now set " g = 10. We can recalculate Δ = h/3, and spacings are given by 3 = /h = {6, 7, 8, 9} with element positions, 3# = /h = {0, 6, 13, 21, 30} which do not coincide with the reference grid points. For a general sparse array there is no constraint on the element positions as proposed in Table II. However, a 'uniform' sparse array (USA), by definition which is proposed in this paper, requires all of its element positions to be in some uniform grid space. For this third example, we can change the reference grid size to h/3, or move the elements to some neighboring grid points without causing any overlapping. Both will provide the first group of initial array candidates for the optimization search. Element positions can further be perturbed further to move around the grids finding a better 'local optimum' PSLR value as described in Table II. The ECDF for the optimum spacings is expected to be a smooth function with minimal repetitive spacing values to spread the grating lobes into side lobes. Numerical examples of the ECDF are given Fig. ECDF in Section V.

## v. Sparse arrays with minimized mutual coupling:

Spare array design procedure described above allows TX and RX elements to be located anywhere inside a common aperture, preferably both expanding over the aperture for smaller BW. However, this could be a problem if the mutual coupling among the TX and RX groups is high, then the two element groups should be separated to use different sections of the aperture. We can study this case by modifying the beamforming equation ( 6) by taking the mutual coupling contributions into account

and physical aperture sparsing can be done as in ( 22)

where AE ; is the square mutual coupling matrix of size n ; . The above equation can be simplified by ignoring the mutual couplings between TX and RX elements with separation distances larger than some O , and O for the horizontal and vertical, respectively. Under these assumptions, sparse array optimization can be forced to have an additional constraint by defining a 'forbidden zone' to push TX and RX elements away into separate regions which would simplify (34) to (

Fig. 6. Some example array structures with mutual coupling forbidden zones, (a -e) physical apertures, and (f -j) their virtual apertures. Physical and virtual apertures for; (a-f) fully-populated URA with no forbidden zones (co-located TX and RXs), (b-g) two-vertical, (c-h) two-diagonal, (d-i) four-corners and (e-j) improved four corner structures, respectively. Forbidden distances, O and O are selected to be 15h and 10h, respectively.

Alternative approaches to define forbidden zones for minimizing the mutual coupling between the TX and RX elements, and the formation of virtual apertures are illustrated in Fig. 6 for a physical aperture of 30h × 30h and a minimum element spacing of h/2. Mutual coupling zones are illustrated for a rectangular of size 15h × 10h along the azimuth and elevation. Consideration of the physical element sizes to avoid overlapping further causes some positions to be unusable. This will create aperture loss and beam width spreading which need careful consideration.

Let us define the performance metrics for virtual aperture and BW efficiency

where m˜ and F"Q are the physical and virtual aperture sizes, the virtual aperture gain, È F , is 2 and 4 for the 1D and 2D cases, respectively, the aperture loss factor, Ç Pm ≤ 1 and the BW spreading factor, Ç º» ≤ 1 which are calculated for the examples of Fig. 6 given in Tables III andIV.   Both the aperture loss and the BW spreading factors are unity for standard ULA and URAs when TX and RX elements can be co-located on a shared aperture and their physical sizes are ignored as shown in Table III and IV (a, f). The available physical apertures should be separated to TX and RX sub-apertures to minimize their mutual couplings. Defining sub-apertures is illustrated in (b -j) for two-vertical, two-diagonal, and four corner regions which all provide a pool of positions for the algorithm given in Table II. The efficiency of the better four corners case is further improved in (e, j). 

## C. Disadvantages of Sparse Arrays:

Optimum sparse array design of Section IV.B. illustrated in Fig. 3 suggests uniformly distributed inter-element spacings which in effect attenuates and spreads the grating lobes into side lobes, and thus, sparse arrays can offer solutions with no grating lobes. However, this grating lobe power is spread across the uFOV increasing the side lobe levels and lowering the PSLR. This becomes unavoidable especially for wide uFOV and very small thinning ratios, as expected. In general, sparse arrays often require effective sparse array processing to reduce PSLR especially for the multi-target case. Such practical approaches are possible but kept outside the scope of this work, and will be studied in our next paper.

### V. RESULTS AND CONCLUSION

A. Fullly populated uniform arrays: Ankara USAs are designed on a reference grid of size h/2 × h using physical element sizes 2h × 5h and are grating lobe-free only along the horizontal. The PSLR values are 11.23 dB, 8.64 dB, and one-sided azimuth and elevation HPBW values are [0.6 0 , 0.53 0 ], [0.5 0 , 0.5 0 ] for A, B arrays, respectively.  

## i. Simulated Mutual Coupling for Ankara A array:

The mutual coupling between TXs and RXs within the same type of elements can mostly be compansated based on laboratory measurements, and accurate calibration of signals are possible. However, coupling among those two groups strongly depends on the environment and the target angles. The simulated results for Ankara array shown in Table V and Fig. 11 show that horizontal and vertical distances of 15 h and 10 h can be defined as the separation distances to minimize the mutual coupling.

## i. USA with forbidden zones: Coruh A & B arrays

In this section the improved four-corners approach proposed in Fig. 11 (e andj) is illustrated in the design of Coruh arrays. Forbidden distances, O = 10h, and O = 15h are enforced to minimize the coupling effects. Version A and B elements, and physical element sizes are identical to Ankara USAs. They provide better array aperture and BW spreading efficiency as defined in Section (IV.B.v.) Coruh USAs are designed on a reference grid of size h/2 × h/2 using physical element sizes 2h × 5h and are grating lobe-free both along the horizontal and vertical as shown for a typical candidate array in Fig. 12 (ad). The optimized PSLR values are 11.10 dB, 9.14 dB, and onesided azimuth and elevation HPBW values are [0.4 0 , 0.76 0 ], [0.5 0 , 0.73 0 ] for A, B arrays, respectively. The novel USA design approach proposed in Section IV provides with effective array solutions for low number of elements with better FOV and BW. Both Ankara and Coruh arrays allow utilization of large element sizes, and providing the received signal patterns to be grating lobe-free in any desired axis. It is shown that PSLR > 11 dB, and •-< 0.5 @ is possible with only for W Q = 12, W "Q = 16, and W F"Q = 192. Other measured performance values are given in Table IV. The inter-element spacings for ULAs are constant as shown in Fig. 13 (a) for W = 16 and 64 which need to be h/2 or smaller in order to provide a grating lobe-free operation. However, when the physical size of elements are larger than this value the received signal pattern for ULAs will be the sum of all image replicas for each real-valued grating lobe angles at sin b V/2¬ shifted along the azimuth. Similarly for URAs, additional replica images will be added for each realvalued grating lobes at sin b V/2ℎ shifted along the elevation as discussed in (29). Further, avoiding large side lobes is only possible if the sparse array has irregular spacing values. This happens when the ECDF is a smooth function as shown in Fig. 13 (b). 

## B. Uniform Sparse Arrays with Large Antenna Elements:

Here are some numerical results to illustrate creating USAs with no grating lobes which are optimized with or without mutual coupling forbidden zones. For the optimization of Version A's 12 RXs Version B's 8 RX positions are enforced as the initial condition. Physical aperture size is limited to 35h × 35h and elements sizes are 2h × 5h both for Ankara and Coruh arrays and their versions A and B. 

