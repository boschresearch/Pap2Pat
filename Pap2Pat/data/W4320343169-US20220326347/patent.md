# DESCRIPTION

## FIELD OF THE INVENTION

The present invention is directed to radar systems, and more particularly to radar systems for vehicles and robotics.

## BACKGROUND OF THE INVENTION

The use of radar to determine direction, range, and velocity of objects in an environment is important in a number of applications including automotive radar, robotic sensing, and positioning. The performance of high-resolution radars can be limited by the contrast ratio, accuracy, and presence of ghost targets experienced using standard processing chains.

Radar systems typically transmit a radio frequency (RF) signal and listen for the reflection of the radio signal from objects in the environment. A radar system estimates the location of objects, also called targets, in the environment by correlating delayed versions of the received radio signal with the transmitted radio signal. A radar system can also estimate the velocity of the target by Doppler processing. A radar system with multiple transmitters and multiple receivers (MIMO: Multi-Input Multi-Output) can also determine the angular position of a target. Depending on antenna scanning and/or the number of antenna/receiver channels, the number of antenna elements and their physical locations and their geometry, different angles (e.g., azimuth or elevation) can be determined.

A radar system consists of transmitters and receivers. The transmitters generate a baseband signal which is upconverted to a radio frequency (RF) signal that propagates according to an antenna pattern. The transmitted signal is reflected off of object or targets in the environment. The received signal at each receiver is the totality of the reflected signal from all targets in the environment. The receiver downconverts the received signal to baseband and compares the baseband received signal to the baseband signal at one or more transmitters. This is used to determine the range, velocity, and angle of targets in the environment.

A radar system utilizes multiple antenna elements to form antenna arrays for transmitting and receiving purposes. Radar systems often detect false targets due to antenna pattern side lobes which are artificially created targets due to geometry of antenna array.

## SUMMARY OF THE INVENTION

Methods and systems of the present invention provide for a radar system utilizing a sparse array antenna structure which provides an enhanced angular resolution to detect multiple targets with improved accuracy beyond the abilities of conventional radar.

A radar system for a robot or vehicle that uses such an enhanced resolution in accordance with the present invention includes multiple antenna array elements at least for transmission and/or receiving. The transmitter is operable to or configured to transmit radio signals. The receiver is operable to or configured to receive a reflected radio signal. The reflected radio signal is the transmitted radio signal(s) reflected from an object or multiple objects.

A radar system comprises an array of transmit antennas and receive antennas connected to a signal processing circuit. In one implementation the antenna arrays may be linear to provide radar target resolution only in azimuth (horizontal axis) while in other implementations the antenna arrays may be two-dimensional and provide target resolution in both azimuth and elevation (vertical axis), separately.

Each transmit array antenna is connected to an associated transmitter and each receive array antenna is connected to an associated receiver, each receiver comprising low-noise amplification, downconversion to the quadrature (IQ) baseband using I-Q mixers driven by a common local oscillator, baseband filtering as necessary, programmable gain adjustment as necessary, and digital-to-analog (D-to-A) conversion at an sampling rate adequate to capture all spectral components of interest.

After D-to-A conversion, each receiver's processing correlates its received signal samples with digital values representing each transmitter's modulation to produce a different number/set of correlations corresponding to different echo delays. There exists one set of such for each receiver-transmitter combination, a number in total equal to the product of the number of transmit antennas with the number of receive antennas.

A radar system utilizes an antenna array which is time shared between a transmitter and a receiver. Output of the receiver is utilized for control and processing and to produce display data.

Radar system utilizes antenna arrays for transmitting and receiving signals which together larger virtual arrays are formed. Virtual array geometry determines field of view (FOV) of radar. FOV defines the extent of the angular region of radar operation. FOV angles are measured with reference to broadside direction. FOV can be defined as a one-sided or two-sided angular extent from broadside in azimuth and elevation. One-sided FOV designated by simply FOV if side convention is not mentioned.

Radar system utilizes antenna array elements which are designed to have a minimum separation distance (spacing) which determines angular resolution of radar. Spacing values are limited by physical size of elements.

Usable field of view (UFOV) maximum angular extent with no grating lobe effects. In general sense, some radar specifications might use only a portion of available FOV for which actual FOV is selected to be smaller than usable FOV. However, without any loss of generality, herein all exemplary radars have FOVs equal to usable FOV to avoid any misunderstanding.

Radar performance deteriorates when there is mutual coupling between antenna array elements. Mutual coupling occurs when two array elements are physically close to each other which coupling among transmitters can be compensated digitally. Similar compensation is possible for receiver groups. Further mutual coupling occurs especially when transmitter element radiates, and neighboring receiver receives that signal in close range on array aperture.

In an aspect of the present invention, an exemplary radar system uses sparsely located antenna array elements allowing improved FOV, angular resolution, beam width, and side lobes using fewer physical antenna elements. Sparse antenna arrays allow the use of physically larger elements, larger separation between transmitter and receiver elements to reduce mutual coupling, and fewer elements to reduce necessary computations.

To improve radar performance parameters; FOV, BW, angular resolution, and maximum side lobe level for a given processing complexity according to one aspect of this invention, the transmit and receive antenna arrays are configured such that the corresponding virtual elements are spread irregularly in the azimuthal and elevation directions in order to minimize sidelobes. Spreading allows physically large elements to be positioned with no overlaps on grids formed by a minimum spacing value of design which could well be smaller than this physical size. Total number of virtual elements can be spread to a much larger aperture to increase angular resolution. Transmitter and receiver groups can be separated on antenna aperture to reduce mutual coupling.

## DETAILED DESCRIPTION

An exemplary radar system 100 with an antenna 102 is illustrated in FIG. 1A that is time-shared between a transmitter 106 and a receiver 108 via a duplexer 104. As also illustrated in FIG. 1A, output from the receiver 108 is received by a control and processing module 110 that processes the output from the receiver 108 to produce display data for the display 112. The control and processing module 110 is also operable to produce a radar data output that is provided to other control units. The control and processing module 110 is also operable to control the transmitter 106.

An alternative exemplary radar system 150 with a pair of antennas 102a, 102b is illustrated in FIG. 1B: an antenna 102a for the transmitter 106 and another antenna 102b for the receiver 108.

An exemplary MIMO radar system 200 with multiple antennas 202, 204, multiple transmitters 206, and multiple receivers 208 is illustrated in FIG. 2. Using multiple antennas 202, 204 allows an exemplary radar system 200 to determine the angle (azimuth or elevation or both) of targets in the environment. Depending on the geometry of the antenna system, different angles (e.g., azimuth or elevation) can be determined.

The radar system 200 may be connected to a network via an Ethernet connection or other types of network connections 214, such as, for example, CAN-FD and FlexRay. The radar system 200 may also have memory (210, 212) to store software used for processing the signals in order to determine range, velocity, and location of targets/objects. Memory 210, 212 may also be used to store information about targets in the environment. There may also be processing capability contained in the radar ASIC apart from the transmitters 203 and receivers 204.

With MIMO radar systems, each transmitter signal is rendered distinguishable from every other transmitter by using appropriate differences in the modulation, for example, different digital code sequences. Each receiver correlates with each transmitter signal, producing a number of correlated outputs equal to the product of the number of receivers with the number of transmitters. The outputs are deemed to have been produced by a number of virtual receivers, which can exceed the number of physical receivers.

A transmit signal echoed from a reflecting object, and received and correlated by a receiver results in a digitized radar echo signal that is the same as would have been produced by a transmit and receive antenna co-located at coordinates which are the sum of the actual transmit and receive antenna coordinates; such signals, called Virtual Receiver (VRX) signals, are further combined according to delay and Doppler shift to resolve targets in the four dimensions of azimuth, elevation, range, and Doppler. Denoting Ntx and Nrx for number of transmitters (TX), and receivers, respectively will create Nvrx=NtxNrx virtual receivers. An exemplary advanced driver-assistance systems (ADAS) coordinate reference system for an antenna array is given in FIG. 3. An exemplary physical and virtual positions for a linear array are illustrated in FIG. 4.

In FIG. 3 is a usable field of view (FOV) maximum angular extent with no grating lobe effects. In a general sense, some radar specifications might use only a portion of the available FOV for which actual FOV is selected to be smaller than usable FOV. However, without any loss of generality, herein all exemplary radar systems have FOVs that are equal to usable FOV to avoid any misunderstanding.

FOV of interest in the azimuthal direction (azimuth, horizontal axis) is a full 180 degrees, or smaller as necessary where FOV is defined as largest angular span with no grating lobes. For a FOV of 180 degrees, the largest possible inter-element spacing for VRX antennas is λ/2. For two-dimensional (2D) gridded rectangular arrays, horizontal and vertical spacings independently determine FOV along azimuth and elevation, respectively. If the selected value of spacings in any axis is larger than λ/2, the FOV on that axis is smaller than 180 degrees. In FIG. 3, the FOV is measured with reference to broadside direction. The FOV can be defined as a one-sided or two-sided angular extent from broadside in azimuth and elevation. A one-sided FOV designated by simply FOV if side convention is not mentioned.

In FIG. 5A, a rectangular virtual array with elements located at points is shown by the following exemplary mathematical model. Denoting (yr, zr) are the coordinates of virtual elements, yn and zm are available locations, and N and M are the number of grid points along the horizontal and vertical axes, respectively.


- - y_(n)=nd_(y) for n=0, 1, 2. . . (N−1)
  - z_(m)=md_(z) for m=0, 1, 2. . . (M−1)  
    A full-grid rectangular virtual array is shown in FIG. 4. A sparse
    array uses full-grid locations as a pool of possibilities. Denoting
    N_(vrx)^(f) for total number of virtual receivers for full-gridded
    rectangular array
  - N_(vrx)^(f)=NM.  
    Denoting N_(vrx)^(S) for total number of virtual receivers for
    sparse rectangular array with R virtual elements located on its
    reference full-grid locations
  - N_(vrx)^(S)=R\<NM=N_(vrx)^(f)

In FIG. 5B, an exemplary sparse array is illustrated using the full-grid positions but with few array elements. Sparsity ratio and sparsity percentage are exemplary measures and are defined by the following exemplary mathematical models. Denoting Sr and Sp are the sparsity ratio and sparsity percentages, respectively.

Sr=NvrxS/NvrxS=R/(NM), and Sp=100Sr%

Sparsity percentage for prior art (full-grid) antenna arrays is 100%. As sparsity ratio decreases, the number of total virtual elements decreases in comparison to its reference full-grid array.

An antenna pattern for a sparse array for detecting targets far from a radar system is calculated by the following exemplary mathematical model. Denoting P(ϕ, θ) for antenna pattern for angles (ϕ, θ) inside the FOV, R for total number of virtual receivers, (yr/λ,zr/λ) for virtual array element coordinates, dy/λ and dz/λ for inter-element spacing in terms of wavelength for horizontal and vertical axes (electrical length), respectively

u(ϕ, θ)=sin ϕ cos θ, and v(θ)=sin θ

\({P\left( {\phi,\theta} \right)} = {\sum\limits_{r = 1}^{R}e^{j2{\pi({{\frac{y_{r}}{\lambda}{u({\phi,\theta})}} + {\frac{z_{r}}{\lambda}{v(\theta)}}})}}}\)

Antenna patterns for exemplary array types are given in FIG. 6 where antenna patterns are for linear virtual receivers. The number of virtual receivers, inter-element spacings, and aperture lengths are: 121, λ/2, 60λ and 121, λ, 120λ and 61, λ, 60λ, for FIGS. 6A, 6B, and 6C, respectively.

In FIGS. 6 and FIG. 7 spatial coordinates are denoted by u(ϕ, θ) and v(θ) is also called ‘sine’ domain. The mathematical model given below is a one-to-one transformation from spatial coordinates to spherical coordinates inside semispherical angular domain.

θ=sin−1 (v) and ϕ=sin−1 (u/cos θ),

where −90°<θ<90°, −180°<ϕ<180°, and sin2 (θ)+sin2 (ϕ) cos2 (θ)<1.

FIGS. 6A, 6B, and 6C are figures where horizontal axes are sine domain (u, v) with horizontal tick values that are converted to (ϕ, θ) for illustration purpose. Similarly, FIGS. 7A, 7B, and 7C are figures where both horizontal and vertical axes are sine domain (u, v) with tick values that are converted to (ϕ, θ) for illustration purpose.

In prior art multiple-input-multiple-output (MIMO) radars, the TX and RX antennas were located such that the VRX locations were as far as possible unique, that is, no repeated locations and the prior art sought to produce a VRX array that had no grating lobes within total angular span and field-of-view (FOV) of interest where no grating lobe region is angular region where the expected received phase delays do not vary larger than 180 degrees for a single object in FOV and in range to avoid warping of received phases. Due to phase warping, antenna pattern outside of the FOV generates a flipped-pattern of the inside providing no additional information. This usable region is called the usable field of view (UFOV). The UFOV is 90 degrees both sides of broadside with a UFOV of 180 degrees when inter-element spacing is of λ/2. An exemplary antenna pattern for 121 virtual receivers (VRX) with array element spacing λ/2 is illustrated in FIG. 6A. The UFOV reduces down to approximately to 60 degrees when spacing increases to λ. Two exemplary antenna patterns for 121 and 61 virtual receivers (VRX) both with array element spacing λ are illustrated in FIG. 6B and FIG. 6C, respectively.

Grating lobe angle is calculated in radians by the following exemplary mathematical model. Denoting ϕGL for observed grating lobes for a target at broadside, dλfor inter-element spacing in terms of wavelength

\({\phi_{GL} = {\sin^{- 1}\left( \frac{n}{d_{\lambda}} \right)}},{{{for}n: - 1} < \frac{n}{2d_{\lambda}} \leq 1},{{{and}{for}{}n} = {\pm 1}},{{\pm 2}\ldots}\)

where target is located at the angular location for n=0. All other values create flipped or warped copies of the target.

In FIGS. 6A, 6B, and 6C, antenna patterns show the number of virtual receivers, inter-element spacings, aperture lengths, FOV, and BW to be (A) 121, λ/2, 60λ, 180o, 0.3875, (B) 121, λ, 120λ, 90°, 0.1937, and (C) 61, λ, 60λ, 90°, 0.4039, respectively. Usable FOV, ϕFOV, is the angular region where no such copies of targets are present even if target is at edge of FOV.

\(\begin{matrix}
{{\phi_{{FOV},{twosided}} = {{2{\sin^{- 1}\left( \frac{n}{2d_{\lambda}} \right)}}❘_{\min}}},} \\
{{{{for}n:0} < \frac{n}{2d_{\lambda}} \leq 1},{{{and}{for}n} = 1},{2\ldots}}
\end{matrix}\)
\(\begin{matrix}
{{\phi_{{FOV},{onesided}} = {{\sin^{- 1}\left( \frac{n}{2d_{\lambda}} \right)}❘_{\min}}},} \\
{{{{for}n:0} < \frac{n}{2d_{\lambda}} \leq 1},{{{and}{for}n} = 1},{2\ldots}}
\end{matrix}\)

Required FOV and inter-element spacing are related and once one is set the other is constrained. In FIG. 6A, exemplary one-sided FOV (simply FOV) for 121 virtual elements is 90 degrees for spacing λ/2. In FIGS. 6B and 6C, the FOV is 30 degrees for spacing λ both for 121 and 61 virtual elements.

Exemplary one-dimensional antenna patterns for two linear antenna arrays given in FIGS. 6A and 6C are for 121 and 61 virtual elements and for spacings λ/2, and λ, respectively.

Angular resolution along an axis is related to the physical extent of array elements (aperture) along that axis, a smaller angular resolution requires a larger extent of array elements where the extent is measured in terms of wavelength. Smaller angular resolution is better resolving ability of noticing/separating closely (angular) located targets. For a given spacing value, a larger extent requires a larger number of elements to fill full-grids (FIGS. 5A and FIG. 5C). The antenna pattern and angular beam width for linear virtual receivers can be compared with a similar 2D array (compare FIG. 6A and FIG. 6C with FIG. 7).

In FIG. 7, antenna patterns are for exemplary rectangular virtual receivers. The number of virtual receivers are 121 by 61 with a total of 7,381, and spacings are λ/2, λ for horizontal and vertical axes, respectively, (FIG. 7A) target is at (ϕ, θ)=(0°, 0°), (FIG. 7B) target is at (ϕ, θ)=(30°, 30°), and (FIG. 7C) close-up image of the target beamwidth (BW) region. Horizontal and vertical antenna pattern cross-sections of FIG. 7A are equal to 1D patterns in FIGS. 6A and 6C. The FOV values for rectangular exemplary 2D array are 90 and 30 degrees for spacings λ/2, and λ, respectively. In FIG. 7A and FIG. 7B, target is at (ϕ, θ)=(0°, 0°), and at (ϕ, θ)=(30°, 30°), respectively.

Angular resolution is related to the antenna beam width of the array. Antenna beam width is better (smaller) for an array with a larger extent. Half power beam width, BWhp, and first null beam width, BWfn, are calculated in radians approximately by the following exemplary mathematical model. Denoting N for number of linear array elements, dλand Lλfor spacing and extent (aperture length) in terms of wavelength respectively

\({BW}_{fn} = {{a{\sin\left( \frac{1}{{Nd}_{\lambda}} \right)}} = {a{\sin\left( \frac{1}{L_{\lambda}} \right)}}}\)
\({BW}_{hp} = {{0.886\left( \frac{1}{{Nd}_{\lambda}} \right)} = {0.886\left( \frac{1}{L_{\lambda}} \right)}}\)

In FIG. 6, antenna pattern has its largest value at target location. All other peak values are side lobes. Maximum side lobe level (SLL) is largest of all side lobes. SLL is constant for prior art 1D and 2D arrays using full-grid array locations. Change of inter-element spacing, number of elements, and element extent do not change SLL. SLL is always constant for full-grid arrays and cannot be changed without using tapering.

In prior art antenna arrays, larger FOV and smaller angular resolutions require larger element extents (apertures) and large number array elements. Number of elements, FOV and angular resolution are constrained, meaning that improvement in any one of them needs to be compensated by degradation of others. FOV will improve by degrading angular resolution (BW) when all other parameters are kept the same, and vice versa. To improve both FOV and BW simultaneously, the number of elements must be increased, which would increase computation complexity.

In engineering applications and implementations, there are a finite number of available transmitters and receivers, those elements have physical sizes which could limit spacing among them. Further, mutual coupling between transmitters and receivers could also require those groups to be separated physically. Under those constraints, for a full-grid array with spacing λ/2, further improvement of FOV, BW and SLL is not possible without increasing number and reducing the size of elements.

Therefore, there is need for an efficient way to design and construct TX/RX arrays. This invention can also be applied to and improves fundamental capacity of prior art antenna arrays, antenna arrays for communications systems, ground penetrating radars, and also transducer arrays for ultrasound imaging devices.

In prior art MIMO radars, only two of the values; FOV, angular resolution, and total number of array elements can be selected independently, the third is constrained by the first two values, often limiting the capability of radar. Exemplary embodiments with sparse arrays allow efficient use of array elements with larger apertures with wider FOV utilizing a reduced number of elements.

The sparse array technique provides array solutions for a desired reduced number of elements, FOV, and BW. Those three values are treated independently where FOV and BW determine element spacing(s) and antenna extent(s), respectively. An engineering objective is to obtain the widest FOV, the narrowest BW utilizing the minimum number of elements. The FOV values are considered one-dimensional for a linear array, and two-dimensional for rectangular arrays with two perpendicular axes (aperture). An exemplary antenna array geometry is depicted in FIG. 3.

FIG. 8 illustrates an exemplary method for arranging a sparse array. In step 802, an initialization step defines desired array properties: dimension, available number of elements, beam width, and maximum side lobe level. Further constraints on the array can also be added: physical sizes for TX and RX elements, forbidden mutual coupling zone between TX and RX elements, and priori list of element locations enforced to be utilized, if necessary. In step 803, inter-element spacings and aperture lengths for the array are calculated using desired FOV, and BW, respectively. The FOV and BW are used to calculate reference full-grid element locations.

In step 806, initial element positions are filled with the enforced locations if required. Further, uniform inter-element spacing can be created to be used in further steps for faster convergence to an optimum array. For this, non-repeating-spaced element positions are initially determined. Their ordering is randomly shuffled at each run to provide a good-initial array candidate.

In step 807, random element locations are found which satisfy both step 802 and step 803. For faster convergence, initial values offered in step 806 can be used here before random perturbation of locations. Perturbations are shifting of elements by multiples of minimum-inter-element spacing.

In step 808, maximum side lobe level (SLL) in FOV is calculated for candidate array which is proposed in step 807. Best value of SLL is updated if new SLL is lower (better).

Steps 806 through step 808 are repeated for each run until a stopping criterion is met in step 804. The Left loop is called an inner loop. An Exemplary stopping criterion is reaching a maximum iteration number. Each run finalizes iterations and output optimum sparse array solutions for that run to step 805. In step 805, optimum positions and SLL values for each run are monitored. Step 805 continues back to step 802 for another run if the last two SLL values are different enough. After a sufficient number of runs (e.g., a minimum of 5), the last two optimum SLL values are monitored. If their difference is lower than significance (an exemplary value of 0.5 decibels), the algorithm/method's outer (right) iteration loop is stopped. This finalizes all iterations. Sparse array locations corresponding to the lowest SLL yields an optimum sparse array.

In general, the sparse array algorithm/method (see FIG. 8) finds an optimum array solution for a sparse array with FOV, BW, number of elements, and SLL. The algorithm/method can be initialized by any three of those to optimize for the remaining fourth. Other criteria: mutual coupling and physical element size limitations can be taken into consideration during optimization iterations.

The exemplary algorithm of FIG. 8 provides improved arrays with the following properties: (1) independency between BW and total number of elements, (2) independency between FOV and total number of elements, (3) allows physically large elements to be used to form smaller inter-element spacings, (4) allows transmitter and receiver groups to be separated to avoid using mutual coupling zone, and (5) allows enforcement of the use of a priori list of element locations.

In FIG. 9A, an exemplary prior art rectangular 192 full-grid virtual array elements are created using 16 transmitter and 12 receivers. Inter-element spacings are λ/2 and λ for horizontal and vertical, respectively. Same virtual array locations can be formed using different transmitter and receiver formations. Inter-element spacings are λ/2 and λ for horizontal and elevation, respectively.

In FIGS. 10A, 10B, 10C, and 10D, antenna patterns, for example, prior art array in: (FIG. 10A) 3D, target angle=(0°, 0°); (FIG. 10B) 3D, target angle=(30°, 30°); (FIG. 10C) azimuth; and (FIG. 10D) elevation for target angle=(0°, 0°).

In FIG. 10, antenna patterns, compared to the prior art array of FIG. 9, show one-sided FOV are 90° and 30°, and BW are approximately 3° and 2° for horizontal and elevation, respectively.

FIG. 11A illustrates exemplary improved physical TX/RX array positions, while FIG. 11 B illustrates the resulting sparse array with 12×16=192 virtual elements, and with the same spacings as of FIG. 9.

FIGS. 12A, 12B, 12C, 12D, and 12E illustrate exemplary antenna patterns for an improved optimum sparse array with the new sparse array design technique using 2.6% sparsity is given. FIGS. 12A and 12 illustrate a 2D plot, target angle=(0°, 0°); FIG. 12C illustrates a 2D plot, target angle=(30°, 30°); while FIGS. 12D and 12E illustrate 1D plots along azimuth and elevation with target angle=(0°, 0°), respectively. For all figures, except FIG. 12A, axes are spatial variables, (u, v) with tick values converted to degrees for clarification. For FIG. 12A, both axes are (ϕ, θ) given in degrees. Using exemplary sparse array FOV for vertical is improved to be 90°. BW for horizontal and vertical are both decreased to be below 0.55°.

FIG. 13 illustrates exemplary antenna patterns with differential beamforming, which is used to further reduce SLL. Exemplary differential beamforming is done for a vertical FOV of 15° degrees. Antenna patterns for an improved optimum sparse array with the new sparse array design technique has 2.6% sparsity with target angle=(0°, 0°) as illustrated in FIG. 12. FIGS. 13A and 13B illustrate the results of beamforming as illustrated in FIG. 12; FIGS. 13C and 13D illustrate the antenna pattern using differential beamforming for a FOV set to 90° and 15° for horizontal and vertical, respectively.

FIG. 14A illustrates an exemplary transmitter and receiver element grouping with mutual coupling distance restrictions of 20λ and 10λ for horizontal and vertical, respectively, FIG. 14B illustrates an exemplary sparse array's physical 12 transmitter and 8 receiver element positions as initial restriction to sparse array design, FIG. 14C illustrates an exemplary sparse array's physical 12 transmitter and 12 receiver element positions, which only 8 receivers are optimized for reducing mutual coupling, 8 receivers are forced by as the initial setting, FIG. 14D depicts the antenna pattern from the resulting sparse virtual array with 12×8=96 virtual elements; with FIGS. 14E, 14F, and 14G illustrating 2D, 1D-azimuth and 1D-elevation antenna patterns for exemplary mutual coupling restricted sparse array for a target at broadside, respectively. Side lobes can further be reduced using differential beam forming.

FIG. 15A illustrates and exemplary transmitter and receiver element grouping with mutual coupling distance restrictions of 15λ and 10λ for horizontal and vertical, respectively, FIG. 15B illustrates an exemplary initial enforcement of 12 transmitters and 8 receivers, FIG. 15C illustrates the sparse array's physical 12 transmitter and 16 receiver element positions with restricted by mutual coupling distance, FIG. 15D illustrates the resulting sparse virtual array with 12×16=192 virtual elements, FIG. 15E illustrates the antenna pattern for exemplary mutual coupling restricted sparse array, FIGS. 15E and 15F illustrate exemplary horizontal and vertical cross sections of antenna pattern of target angle at the broadside. Side lobes can further be reduced using differential beam forming.

Accordingly, an exemplary radar sensing system utilizing a sparse array antenna structure provides an enhanced angular resolution to detect multiple targets with improved accuracy beyond the abilities of conventional radar. The exemplary radar system uses sparsely located antenna array elements allowing improved FOV, angular resolution, beam width, and side lobes using fewer physical antenna elements. Sparse antenna arrays allow the use of physically larger elements, larger separation between transmitter and receiver elements to reduce mutual coupling, and fewer elements to reduce necessary computations.

Changes and modifications in the specifically-described embodiments may be carried out without departing from the principles of the present invention, which is intended to be limited only by the scope of the appended claims as interpreted according to the principles of patent law including the doctrine of equivalents.

