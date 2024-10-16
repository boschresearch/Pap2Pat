# DESCRIPTION

## FIELD OF INVENTION

The present invention relates to a method and a device for performing high resolution nuclear magnetic resonance (NMR) spectroscopy.

## BACKGROUND OF THE INVENTION

Nuclear magnetic resonance spectroscopy is usually carried out in homogeneous magnetic fields. In many cases however, the inherent heterogeneity of samples or living organisms under investigation, and the poor homogeneity of the magnets (particularly when bulky samples must be placed outside their bores), make it virtually impossible to obtain high-resolution spectra. Unstable power supplies and vibrations arising from cooling can lead to field fluctuations in time as well as space.

The present invention aims to improve the situation.

## SUMMARY OF THE INVENTION

To this end, the present invention firstly proposes a method for performing nuclear magnetic resonance spectroscopy, wherein at least one difference of precession frequencies of a homonuclear pair of spins are tracked in a single scan.

More particularly, the implementation of the invention results in that a field gradient echo is formed at an instant in time that is delayed in proportion to said difference of the frequencies of spins.

In an embodiment, the method comprises at least the steps of:


- - applying a first adiabatic radiofrequency pulse in the presence of a
    first field gradient followed by a coherent transfer step and
    applying a second adiabatic pulse with a second field gradient, for
    encoding resonance frequencies with said difference of frequencies
    of spins and said first field gradient with possible magnetic field
    inhomogeneities,
  - decoding resonance frequencies with a third field gradient having at
    least a same amplitude as said first field gradient, and
  - obtaining from said decoding step a gradient echo giving a spectrum
    of frequency differences in a time domain, in a single scan.

Preferably, the first and second field gradients are identical.

According to another particular feature of the invention, said first (and or second) adiabatic radiofrequency pulse(s) is (are) formed so as to optimise said encoding/decoding steps.

In an embodiment described in details below, the method according to the invention is combined to a J-modulated detection scheme to add a second dimension which can reveal multiplets due to scalar couplings.

The present invention aims also a nuclear magnetic resonance spectrometer, comprising means for performing the method according to the invention.

The present invention is also aimed at a computer program product, stored in a computer memory or on a removable medium able to cooperate with a computer reader, and comprising instructions for running the steps of the method within the sense of the invention.

The software product of the invention can advantageously comprise instructions for generating an adiabatic radiofrequency pulse adapted to optimise the aforesaid encoding/decoding steps.

Thanks to the implementation of the invention, high-resolution NMR spectra can be obtained in inhomogeneous fields with unknown spatiotemporal variations.

## MORE DETAILED SPECIFICATION

Nuclear magnetic resonance (NMR) is arguably one of the most versatile and ubiquitous forms of spectroscopy. Year after year, magnetic resonance imaging (MRI) reveals more surprising insights into morphology, function, and metabolism. Most applications, regardless of whether they are concerned with inanimate solids or liquids or with living organisms, rely on the use of very homogeneous magnetic fields B0 with spatial variations below about 10−9, so that subtle differences in the environment of various nuclei, leading to chemical shifts and couplings, can be made apparent. However, it is often not possible to work under ideal conditions. For example, sufficiently homogeneous fields are difficult to achieve in ex situ NMR where the object under investigation is placed outside the magnet (1, 2), in very high fields induced by resistive or hybrid magnets (3, 4), and in samples (including animals and human beings) which are moving because of pulsating arteries or respiration, not to mention the discontinuities of the magnetic susceptibility due to voids and surgical implants (5, 6).

Many techniques have been proposed to acquire high-resolution spectra under adverse conditions. Spin-echoes (7, 8) can refocus the effects of inhomogeneous B0 fields, and reveal couplings that lead to echo modulations (9-11). If the field's spatial distribution is known, the B0 inhomogeneity may be compensated by using a radio-frequency (rf) field designed to have a similar, spatially correlated profile. Two such approaches have been described. In the first one, the rf-field B1(r) profile is designed to match the B0(r) profile (12-14). The dephasing caused by the rf-field can then be refocused by rephasing in the main B0 field. In the second approach, the inhomogeneities are compensated by manipulating the phases of the magnetization vectors associated with different voxels in the presence of a known gradient, in the manner of multidimensional single-scan experiments (15, 16). In either case, the field B0(r) must be time-independent, and its spatial profile must be known, which constitutes a serious handicap.

In the present invention, high-resolution spectra in inhomogeneous fields are obtained by tracking the differences of the precession frequencies (17, 18) of two spins in a single scan, in a way that is closely related to the ultrafast multidimensional experiments developed by Frydman et al (19) and improved in reference (20) (the content of which is incorporated herein by reference thereto). The experiment functions regardless B0 field profile. Spatial inhomogeneities of at least 11 G/cm can be accommodated. This corresponds to a frequency distribution of about 42 kHz (or 70 ppm for a 600 MHz resonance frequency) for a spherical sample of 1 cm in diameter. Combining this technique with the J-modulated detection scheme of Giraudeau and Akoka (21) adds a second dimension which reveals multiplets due to scalar couplings.

As in the two-dimensional single-scan experiments, the evolution under the chemical shifts needs to be intertwined with gradient encoding (22). Let S and I constitute a homonuclear pair of spins. When a linearly swept adiabatic refocusing pulse is applied in the presence of a gradient to a coherence S+ with coherence order p=+1 belonging to the manifold of S-spin transitions, as shown in FIG. 1A, the resulting phase at time t1 is given by (20):

φ1=α{ΩS+δω(r)+ΓE(r)}2  (1)

where ΩS is the chemical shift of the S spin, δω(r)=−γSB0(r) the (unknown) spatially dependent frequency induced by the inhomogeneous B0 field, ΓE(r)=γSGE·r the (known) frequency induced by the encoding gradient GE={GExk, GEyi, GEzj} and α=σad/Δωad the ratio of the duration σad and sweep width Δωad of the adiabatic inversion pulse. A second identical pulse combined with an opposite gradient then leads to a phase at time t2:

φ2=4α{ΩS+δω(r)}ΓE  (2)

In FIG. 1, filled and open vertical rectangles represent π/2 and π pulses. The rectangles with sloping arrows indicate adiabatic frequency swept refocusing pulses. GE and GD are encoding and decoding gradients. The gradients GA and GB of equal area serve to select the desired coherence pathways (they must be opposite for (B) and (C) and identical for (A)). The delay σC serves to compensate for the evolution under the inhomogeneous B0 field during GA and GB. Increasing GB and prolonging σC by σD/2 shift the signals at zero frequency toward the centre of the gradient GD. Sequences (D) and (E) are adaptations of (B) and (C), for situations where a permanent gradient is dominant. Adiabatic pulses with down-pointing arrows have reversed sweep directions. The phases of the n pulses during decoding are alternated between x to −x every two pulses (21). In these examples, π/2 pulses are used to achieve transfer of coherence, so that the spins need to be scalar coupled. Other sequences can be used, such as total correlation spectroscopy (TOCSY). The signals during even (or odd) decoding gradients are arranged in sequential order, to give a two-dimensional array. The gradient echoes that are formed during each decoding gradient appear in a temporal sequence that corresponds to the peaks in the spectrum. The scalar coupling pattern in the other dimension is obtained by performing a Fourier transformation as a function of the index of the decoding gradients.

The coherence can then be transferred (in the example of FIG. 1 by a simple π/2 pulse) from S+ to I− with coherence order p=−1 through any spin-spin coupling, exploiting for example a scalar interaction JIS. If there are no scalar couplings, it might be possible to use demagnetizing fields which can manifest themselves as intermolecular dipolar interactions (23, 24). After an identical block comprising two more pulses and gradients, the total accumulated phase at time t4 will be:

φ4=4α{ΩS+δω(r)}ΓE(r)−4α{ΩI+δω(r)}ΓE(r)=4α{ΩS−ΩI}ΓE(r)  (3)

This phase does not depend on the spatial variation δω(r) due to the inhomogeneous static field. The phase φ4 can be refocused by a decoding gradient GD. A gradient echo will be formed at an instant in time that will be delayed in proportion to the difference ΩS−ΩI between the frequencies of spins S and I. Although this feature is reminiscent of zero-quantum spectroscopy, it should be noted that the echoes arise simply from the differential evolution of two single quantum (SQ) coherences (18). During the decoding gradient GD in the scheme of FIG. 1A, the coherences will continue to precess under the field inhomogeneities, thus preventing complete refocusing. An improved scheme is shown in FIG. 1B. Instead of applying two adiabatic pulses before and after coherence transfer, only one is applied, which leads to a phase:

φ6=α{ΩS+δω(r)+ΓE(r)}2−α{ΩI+δω(r)+ΓE(r)}2=αΩS2−αΩI2+2α(ΩS−ΩI){ΓE(r)+δω(r)}  (4)

The difference ΩS—ΩI between the chemical shifts of spins I and S is now encoded not only by the gradient GE but also by the B0 inhomogeneity. During a decoding gradient GD with the same amplitude as the encoding gradient GE, the phase is then:

φD(tD)=αΩS2−αΩI2+2α(ΩS−ΩI){ΓE(r)+δω(r)}−tD{ΩI+ΓE(r)+δω(r)}  (5)

At tD=2α(ΩS−ΩI) an echo results because the phase is independent of δω(r). Thus a spectrum of frequency differences is obtained in the time domain in a single scan. The phase of this echo is

φD{tD=2α(ΩS−ΩI)}=αΩS2+αΩI2−2αΩIΩS=α(ΩS−ΩI)2  (6)

A hybrid scheme is shown in FIG. 1C. A bipolar gradient pair with adiabatic pulses that is repeated nE times is inserted before each adiabatic pulse of FIG. 1B. The resulting phase at time t7 is:

\(\begin{matrix}
\begin{matrix}
{\phi_{7} = {{2n_{E}{\alpha \left( {\Omega_{S} - \Omega_{I\;}} \right)}{\Gamma_{E}(r)}} + {\alpha \; \Omega_{S}^{2}} - {\alpha \; \Omega_{I}^{2}} + {2{\alpha \left( {\Omega_{S} - \Omega_{I}} \right)}\left\{ {{\Gamma_{E}(r)} + {\delta \; {\omega (r)}}} \right\}}}} \\
{= {{\alpha \; \Omega_{S}^{2}} - {\alpha \; \Omega_{I}^{2}} + {2\; {\alpha \left( {\Omega_{S} - \Omega_{I}} \right)}\left\{ {{\left( {{2n_{E}} + 1} \right){\Gamma_{E}(r)}} + {\delta \; {\omega (r)}}} \right\}}}}
\end{matrix} & (7)
\end{matrix}\)

The decoding gradient should have an amplitude that is (2nE+1) times as large as the encoding gradient, i.e., GD=(2nE+1)GE, in order to cancel the effects of the inhomogeneities δω(r). The sequence of FIG. 1C is less sensitive to translational diffusion than the experiment of FIG. 1B (25).

As can be seen from Eq. 5, scheme (B) does not require any switched field gradients, provided the inhomogeneities are sufficiently large to cause sharp echoes. This could have implications for measurements in stray magnetic fields (26) or other permanent gradients. FIGS. 1D and 1E show adaptations of FIGS. 1B and 1C, for situations with a permanent gradient. In FIG. 1E the sweep direction of the second adiabatic pulse in each repeated block is inverted. Both schemes lead to a phase φ6 of Eq. 4, but the latter limits losses due to diffusion (25).

All schemes can be extended from one to two dimensions by appending nD repetitions of a block comprising a decoding gradient followed by a π pulse in order to observe a train of spin echoes (21). A Fourier transformation of this echo train reveals (convoluted) multiplets due to scalar couplings in a second dimension. This option requires ca. 500 instead of ca. 50 ms for the basic 1D experiment. The simplest one-dimensional spectrum corresponds to the signal acquired during the first decoding gradient.

Shapira et al, (4) proposed schemes for measurements in fluctuating resistive magnets. The resolution of correlation spectra can be improved, either by compensating for (known) inhomogeneities with tailored rf-fields, or by exploiting echoes following coherence transfer from carbon-13 to proton nuclei. The latter scheme is related to the method of the invention, although in their case the effects of inhomogeneities are cancelled only at one point in the acquisition period.

The experiments of FIG. 1C have been tested by applications to samples containing 5% 1-propanol (CH3CH2CH2OH) and 5% 3-buten-1-ol (CH2═CHCH2CH2OH, henceforth simply called butenol) in CDCl3.

FIG. 2 shows a two-dimensional spectra plotted in absolute value mode of (left) propanol CH3cCH2bCH2aOH and (right) butenol CH2b═CHaCH2dCH2cOH both taken in ca 500 ms with the single-scan method of FIG. 1C. (B) and (D) were obtained in homogeneous and inhomogenous B0 fields, respectively, as evidenced by the conventional proton spectra in (A) (with line-widths on the order of 2 Hz, recorded in a well-shimmed static field) and in (C) (where the line-widths were degraded to ca 4 ppm or 2.4 kHz at 600 MHz). The resonances of spins S and I, labeled a, b, c and d, correspond to single-quantum coherences that evolve during the encoding and decoding blocks of FIG. 1; their scalar coupling patterns appear along the horizontal dimension and carry the same labels (S→I). The arrows in (A) indicate all difference frequencies between scalar-coupled spins that can be observed. The top arrows correspond to the outer lines in the spectrum, the bottom arrows to the smallest frequency differences (inner lines). The line at zero frequency corresponds to coherences that are refocused but not transferred from one spin to another. Both spectra have been recorded with nE=1, gradients applied simultaneously along z and y with strengths GE=0.8 G/cm and GD=2.4 G/cm. The adiabatic pulses of 6 ms had a Wideband Uniform Rate and Smooth Truncation (WURST) profile (28), and sweep-widths of 14 and 20 kHz for propanol and butenol, respectively. (E) Columns taken parallel to the vertical t1 or ω1 domain, taken along the dotted lines of the 2D spectra of propanol in homogeneous (red lines) and inhomogeneous fields (black lines), showing differences of chemical shifts in the spectrum of propanol. (F) Rows taken parallel to the horizontal ω2 domain, showing a multiplet due to scalar couplings with a full width at half height of 3.5 Hz, for nD=64 (t2max=337 ms).

The spectra of FIGS. 2A and 2B have been obtained in a carefully shimmed homogeneous field. The resonances labeled a-d give rise to combination lines (differences in chemical shifts), i.e., 4 peaks in propanol and 8 in butenol. In the vertical dimension, the spectra are symmetric with respect to ω1=0, because each transfer from spin S to I is accompanied by a transfer in the opposite direction. The central peak at ω1=0 arises from magnetization that is refocused but not transferred from one spin to another.

FIGS. 2C and 2D show spectra obtained with the same method in an inhomogeneous field after deliberately missetting the shim currents. Yet the results of the single-scan experiments according to the invention are virtually indistinguishable. The experiments have been repeated using several shim settings, invariably leading to similar spectra, as can be seen from the cross-sections in FIGS. 2E and 2F. As with all 2D single-scan experiments, the signal-to-noise ratio decreases in proportion to the square root of the number of points observed in the indirect dimension, when compared to a 1D spectrum taken under properly shimmed conditions. If the signal-to-noise ratio is poor, the experiments can be repeated for signal averaging, even if the B0 inhomogeneities vary in time, provided the fluctuations are slow compared to the time it takes to acquire each scan. For a simple one-dimensional spectrum, about 50 ms suffice. Thus, assuming that the information must be acquired within 10% of the period of the fastest fluctuations, the spectrum of the stochastic variations must be limited to 2 Hz. This should be useful for NMR spectra obtained in resistive Bitter or hybrid magnets, which suffer from random fluctuations due to the power supply and to low-frequency vibrations associated with the circulation of cooling water.

The resolution, as measured by the full line-width at half-height in the vertical (chemical shift) dimension (t1 or ω1) of 1-propanol in FIG. 2E is 60 μs, for a decoding gradient GD of 4 ms. This corresponds to a resolution of 76 Hz (0.13 ppm) over a frequency range of ±2500 Hz (±4.2 ppm). The resolution of the spectra can be improved by increasing the amplitudes of both encoding and decoding gradients (provided the frequency sweep of the adiabatic pulses covers the frequency range induced by the encoding gradients) or, as shown in FIG. 3, by increasing nE and the strength of the decoding gradients. The frequency range can be increased by extending the sweep width of the adiabatic pulses, albeit at the expense of the resolution, unless one also increases the strength of both encoding and decoding gradients (27—the content of which is incorporated herein by reference thereto). The resolution in the ω2 dimension is determined by the number nD of points acquired in the t2 dimension, like in other forms of 2D spectroscopy.

In order to mimic a gradient that cannot be switched off, the scheme of FIG. 1D has been applied, in the presence of a permanent gradient, or more accurately, a pulsed field gradient that was switched on before the experiment and stopped immediately after observing the signals has been applied. The echo corresponding to zero frequency appears at σC after the start of signal acquisition. Only one-dimensional spectra revealing combinations of chemical shifts in propanol have been recorded (to avoid using prolonged strong gradients). The sample height was decreased to 18 mm, so that the line-shape was further deteriorated by susceptibility effects at the edges. FIG. 4A shows the resulting spectra in the presence of a gradient Gz=2.75 G/cm (˜35 ppm or 21 kHz across the sample). Signals arising from coherence transfer are indicated by arrows. The duration of the adiabatic pulses was 18 ms and their sweep width 40 kHz. When the gradient strength is doubled to 5.5 G/cm (˜70 ppm or ˜42 kHz) together with a doubling of the adiabatic sweep width, there is some loss of intensity due to diffusion (FIG. 4B). These losses can be reduced with the scheme of FIG. 1E, as shown in FIG. 4C for a total of 6 adiabatic pulses of 6 ms duration (instead of two otherwise identical pulses of 18 ms each used for FIG. 4B). The line-width in FIG. 4C is about 70 Hz. Increasing the gradient strength further to 11 G/cm (˜140 ppm or ˜84 kHz) leads to the spectrum in FIG. 4D. In this case, the signal amplitude suffers not only from diffusion losses, but also from the limited rf amplitude (25 kHz) of the initial π/2 pulse. In stronger gradients, one should use a large number of short inversion pulses that cover a very broad bandwidth with the desired phase-profile. In addition, the (possibly frequency swept) π/2 pulses should excite the full bandwidth uniformly, bearing in mind that a linear dependence of the phase with respect to offset is allowed.

