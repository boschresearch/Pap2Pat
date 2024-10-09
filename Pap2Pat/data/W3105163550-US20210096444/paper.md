# Reprints and permissions information is available at www.nature.com/reprints

Competing interests: M. Z., C. W., and M. L. are involved in developing lithiumniobate technologies at HyperLight Corporation.

Correspondence and requests for materials should be addressed to M.L. at loncar@seas.harvard.edu

# Figures legends

Figure 1 | Resonator-enhanced electro-optic comb generator. a, Schematic of a canonical electro-optic (EO) comb generator comprising an EO (χ (2) ) phase modulator inside a Fabry-Pérot (FP) resonator. A continuous-wave (CW) laser is coupled into the resonator and an optical frequency comb is generated at the output b, EO comb generation principle. A microwave signal, with modulation frequency equal to the free spectral range (FSR) of the optical resonator, couples light between different resonator modes. As a result, the input-coupled CW light is modulated, giving rise to sidebands at the modulation frequency, which are then recirculated to be modulated again. The modulation index determines the strength of coupling between nearby frequency components after passing through the modulator. c, Integrated microring EO comb generator. The FP resonator can be replaced by a microring resonator that is EO modulated at a frequency matching the FSR of the ring. Similar to the FP resonator, a CW laser coupled into the ring resonator will be converted to a frequency comb in the output optical waveguide.

Figure 2 | Integrated electro-optic comb generator. a, Micrograph of a fabricated lithium niobate microring resonator (a shorter device is shown here for illustration purpose, see Methods for details). The black lines are etched optical waveguides and the yellow regions are gold microelectrodes. The gold electrodes are driven such that the phase shifts in the two sides of the microresonator are opposite, which is required to break the symmetry of different azimuthal order optical modes, enabling efficient frequency conversion. b, Measured output spectrum of the electro-optic comb generated from the microring resonator, demonstrating > 80 nm bandwidth and more than 900 comb lines with a slope of 1 dB/nm. The input optical power is 2 mW and the microwave peak driving amplitude is Vp = 10 V. Note that the signal-to-noise-ratio of the comb lines exceeds 40 dB but is limited by the noise floor and resolution of the optical spectrum analyzer. Insets: left, magnified view of several comb lines showing a line-to-line power variation of ~ 0.1 dB. Right, measured transmission spectrum for several different modulation indices (β). When the modulation is turned on, the optical resonance is broadened by twice the modulation index. This behaviour is predicted well by the round-trip phase model (see Methods). NT: normalized transmission. NOD: normalized optical detuning The light grey shaded region highlights the constructive interference condition region beyond which EO comb generation is suppressed. This region is bounded by ±𝛽𝛽, the round-trip modulation index. Insets show a zoomed-out view of the round-trip phase vs. wavelength. The calculated cut-off frequency matches well with experimental data, as shown by the dashed lines extending to (a). c, d, Measured and simulated comb spectrum and round-trip phase versus wavelength in presence of both optical and microwave detuning. Different comb shapes, such as a single-sided EO comb can be generated. e, Simulated round-trip phase versus wavelength for traditional bulk devices (black), the measured integrated device (blue), and dispersion-engineered integrated devices (orange). The simulations demonstrate that integrated EO combs can achieve larger dispersion-limited bandwidths than devices based on bulk crystals and dispersion engineering can enable octave-spanning EO combs. 

# Methods

## Fabrication details

All devices are fabricated on x-cut single crystalline thin-film lithium niobate (LN) wafers (NANOLN). The wafer stack consists of a 600 nm thin-film LN layer, a 2 µm thermally grown SiO2 layer and a 500 µm silicon handle layer. Standard electron-beam (e-beam) lithography is used to pattern optical waveguide and micro-racetrack resonators. The patterns are then transferred into the LN layer using argon (Ar + ) plasma etching in an inductively coupled plasma reactive ion etching (ICP-RIE) tool 34 . The etch depth is 350 nm, leaving a 250 nm thick LN slab behind, which enables efficient electric field penetration into the waveguide core. Gold contact patterns are then created using aligned e-beam lithography, and the metal is transferred using e-beam evaporation methods and lift-off processes. The chip is then diced and the facets are polished for end-fire optical coupling. A 10 GHz FSR micro-racetrack measures 200 µm by 6.2 mm. For illustration purposes, a 25 GHz FSR ring with otherwise the same design measuring 200 µm by 2.7 mm is displayed in Fig. 2a, where the straight section has a reduced length.

## Microwave driving circuitry

The 10 GHz microwave drive signal is generated by a radio-frequency (RF) synthesizer and amplified by an electrical power amplifier. The amplified electrical signal is passed through a microwave circulator and delivered to the microelectrodes. As the microelectrodes represent a capacitive load, most of the electrical driving signal is reflected back to the circulator and terminated at the circulator output by a 50-Ω load.

In the dual-drive EO comb generation experiment, two RF synthesizers are phase-locked via a common 10 MHz clock and are free to operate at different frequencies. The two sinusoidal microwave signals are power balanced and combined using an RF power splitter and passed through the amplifier-circulator circuitry described previously.

## Optical characterization and detection

Light from a tunable laser (SANTEC TS510) is launched into, and the comb output is collected from, the LN waveguides by a pair of lensed optical fibers. The output comb is passed to an optical spectrum analyser (OSA) having a minimum resolution of 20 pm. This finite resolution accounts for the limited signal-to-noise ratio observed in Fig. 2b (~ 20 dB). The shot-noise-limited signal-to-noise ratio is much higher, as the comb shot noise lies below the OSA noise floor. Although the measurement in the paper is chosen to center at 1600 nm, the frequency comb center wavelength can be flexibly chosen between 1500 nm to 1680 nm of the tunable laser's range without affecting much of the generated comb width.

In the dual-drive EO comb measurements, the modulated light is passed to a fast photodetector (New Focus 1544A) and the resulting electrical signal is sent to a RF spectrum analyzer to record the beating in the RF domain.

## Measurement and calculation of resonator parameters

As demonstrated by Equation (4) below, there are four resonator parameters that fully characterize the EO comb spectrum: the internal round-trip transmission coefficient 𝛼𝛼, the power coupling coefficient 𝑘𝑘, the coupler insertion loss of the coupler 𝛾𝛾, and the phase modulation index 𝛽𝛽 . Finding each of these four parameters by fitting to the comb spectrum of Equation ( 4) is difficult because the output comb can be fully determined by a subset of these independent parameters (e.g., increasing the modulation index has the same effect as decreasing the loss in the resonator). Instead, each of the parameters must be measured separately.

We find 𝛼𝛼 and 𝑘𝑘 by measuring the total transmitted power without phase modulation (Figure 2b right inset). By fitting to the expected transmission of an all-pass ring resonator, we find 𝑄𝑄 = 1.5 × 10 6 , 𝛼𝛼 = 0.95 and 𝑘𝑘 = 0.027. Then we perform a grid search optimization for 𝛾𝛾 and 𝛽𝛽 comparing the measured output spectrum (Fig 2b ) with the spectrum determined from the output time-domain electric field of Equation ( 3) below. We find a best fit for 𝛾𝛾 = -0.004 dB and 𝛽𝛽 = 1.2 𝜋𝜋, where the average difference between experimental and theoretical comb line power is 0.6 dB. The relative uncertainty in the measurement of 𝛽𝛽 in this case is ±4%, calculated by finding the furthest fit within a 95% confidence interval and calculating the resulting 𝛽𝛽.

The output power transmission for nonzero modulation indices (Figure 2b right inset) is calculated by sampling the output electric field with Equation (3) and averaging the power over more than 100 modulation periods.

## Dispersion engineering in thin-film LN waveguides

To achieve wide-spanning EO combs, the waveguide dispersion should be engineered such that the group velocity (or the FSR) of the ring is roughly a constant across the entire frequency range. We simulate the dispersion of the waveguide using finite element methods (LUMERICAL Mode Solutions). The simulation accounts for the LN material anisotropy and the finite waveguide etching angle (around 70° from horizontal). The round-trip phase of the light inside the resonator is calculated by integrating the simulated group velocity dispersion twice to determine the total frequency-dependent phase-shift.

For the device we demonstrate here, with a waveguide ridge height of 350 nm, waveguide width of 1.4 µm, slab thickness of 250 nm, and SiO2 top cladding of 1.5 µm the dispersion of the waveguide is weakly normal and supports an EO comb cut-off bandwidth of ~ 250 nm. We find that for an air-cladded waveguide with a 600 nm thin-film LN layer, 550 nm etch depth and 1.8 𝜇𝜇m waveguide width, a comb spanning ~1.3 octave can be generated with a round-trip modulation frequency of 50 GHz and strength of 1.2 Vπ, as shown in Fig 3e . The waveguide dispersion can be tailored for low microwave drive powers at the expense of a smaller comb span. For an air-cladded waveguide with a 650 nm thin-film LN layer, etch depth of 620 nm and width 2400 nm, an octave spanning comb can be generated with a phase modulation strength of only 0.3 Vπ. These results are presented in the accompanying extended data figure.

## Microwave driver power consumption

The current EO comb generator features a direct capacitive drive electrode design, where the electrical power consumption PE can be estimated as

Where C ~ 200 fF is the estimated capacitance 35 , Vp is the peak voltage and 𝜔𝜔 𝑀𝑀 is the microwave frequency. For the broad comb shown in Fig 2 ., the calculated electrical power consumption is ~ 630 mW.

There are several ways to reduce the electrical power consumption. Presently the electrode gaps are not optimized and can be reduced to directly increase the electro-optic efficiency. A microwave resonator with a quality factor of QM can be used to dramatically enhance the driving voltage, as only a narrow band microwave source is required. A microwave resonator has an enhanced voltage 𝑉𝑉 𝑝𝑝,𝑒𝑒𝑒𝑒𝑒𝑒 of

Comparing ( 2) with ( 1), the effective pumping power is increased by a factor of QM. This means for a moderate QM = 20 at 10 GHz, the power consumption can be reduced to ~ 30 mW.

To estimate the minimum electrical power required to generate an octave spanning EO comb, we consider the first case where the resonator is driven to 1.2 Vπ at 50 GHz FSR.

Here the capacitance of the device is reduced by a factor of 5 as the ring resonator becomes smaller to achieve a 50 GHz FSR. At the same time, the Vπ also increases by a factor of 5 due to the shorter electrodes. For QM = 20, the calculated power consumption is ~ 750 mW. Through dispersion engineering and higher optical Q microresonators, it is possible to achieve an octave spanning EO comb even at low drive voltages of Vp = 0.3

Vπ. In this case, the electrical power consumption is further reduced to only ~ 45 mW.

## Canonical EO comb generator design

The concept of a comb generator using a resonator to enhance frequency generation by an EO phase modulator dates to 1972 36 . Theoretical and experimental work 12,28 on these comb generators continued in the 1990s. Recent advances in low-loss integrated LN photonic platform 34 has motivated re-examination of these comb generators. This section provides details on important characteristics of these EO comb generators.

A canonical waveguide-based comb generator is shown in Fig. 1c of the main text. A single-frequency input with electric field 𝐸𝐸 𝑖𝑖𝑖𝑖 (𝑡𝑡) = 𝐸𝐸 � 𝑖𝑖𝑖𝑖 𝑒𝑒 𝑖𝑖𝜔𝜔 0 𝑡𝑡 is coupled, with power coupling coefficient 𝑘𝑘 and insertion loss 𝛾𝛾, to a resonator having round trip time 𝑇𝑇 at center frequency 𝜔𝜔 0 and round trip power loss 𝛼𝛼 . The resonator contains a phase modulator driven with modulation index 𝛽𝛽 and frequency 𝜔𝜔 𝑚𝑚 . The output electric field is 28

where 𝑟𝑟 = �(1 -𝛾𝛾)(1 -𝑘𝑘)𝛼𝛼 is the round trip electric field transmission and 𝐹𝐹 𝑖𝑖 (𝜔𝜔 𝑚𝑚 𝑡𝑡) =

is the modulator coherence function. The parameter 𝑙𝑙 = 1 -𝑟𝑟, corresponding to the round-trip electric field loss, is used in the main text for simplicity.

When the optical carrier is resonant in the resonator (𝜔𝜔 0 𝑇𝑇 = 2 𝜋𝜋 𝑚𝑚 1 ) and the microwave drive signal is resonant (𝜔𝜔 𝑚𝑚 𝑇𝑇 = 2 𝜋𝜋 𝑚𝑚 2 ), the modulator coherence function becomes 𝐹𝐹 𝑖𝑖 (𝜔𝜔 𝑚𝑚 𝑡𝑡) = 𝑛𝑛 sin 𝜔𝜔 𝑚𝑚 (𝑡𝑡 -𝑖𝑖𝑇𝑇) and the output electric field can be simplified to

𝑟𝑟 𝑒𝑒 -𝑖𝑖𝑖𝑖 sin 𝜔𝜔 𝑚𝑚 𝑡𝑡 1 -𝑟𝑟 𝑒𝑒 -𝑖𝑖𝑖𝑖 sin 𝜔𝜔 𝑚𝑚 𝑡𝑡 � 𝐸𝐸 𝑖𝑖𝑖𝑖 (𝑡𝑡).

(

This output electric field corresponds to an optical frequency comb spaced at the modulation frequency. The power in the 𝑞𝑞th comb line away from the center frequency can be found by rewriting Equation (1) as

where 𝐽𝐽 𝑞𝑞 is the 𝑞𝑞th order Bessel function of the first kind. The power of the 𝑞𝑞th (nonzero) comb line is then

Kourogi et. al. 12 found an approximation for the power of the 𝑞𝑞th comb as 𝑃𝑃 𝑞𝑞 ∝ 𝑒𝑒 -|𝑞𝑞|(1-𝑟𝑟) 𝛽𝛽 .

In the presence of optical and microwave detuning from resonance, the comb spectrum can still be calculated. When the optical carrier is off resonance, the total round-trip phase is 𝜔𝜔 0 𝑇𝑇 = 2 𝜋𝜋 𝑚𝑚 1 + 𝜙𝜙 𝑜𝑜𝑝𝑝𝑡𝑡 . Similarly, when the microwave carrier is off resonance the total round-trip phase is 𝜔𝜔 𝑚𝑚 𝑇𝑇 = 2 𝜋𝜋 𝑚𝑚 2 + 𝜙𝜙 𝑚𝑚𝑖𝑖𝑚𝑚𝑚𝑚𝑜𝑜 . Using these expressions in Equation

(1), we can find the following expression for the power in the 𝑞𝑞th comb line:

The modified even and odd modulation indices (𝛽𝛽 𝑒𝑒 and 𝛽𝛽 𝑜𝑜 , respectively) are

𝛽𝛽 𝑜𝑜 (𝜙𝜙 𝑚𝑚𝑖𝑖𝑚𝑚𝑚𝑚𝑜𝑜 , 𝑛𝑛) = 𝛽𝛽 �-

It is clear here that in the regime of low optical detuning, the slope of the comb decreases by a factor of cos(𝜙𝜙 𝑜𝑜𝑝𝑝𝑡𝑡 ). This effect has been studied and reported in 37 . The effect of microwave detuning is harder to visualize, but results in a destructive interference condition for large values of 𝑞𝑞 in Equation ( 5). This effect is demonstrated experimentally and theoretically in Fig. 3a and 3b of the main text.

## Noise Properties

The optical phase noise of the comb lines is important in applications that require high optical signal-to-noise ratios, such as high-capacity optical communications. It is well known that the optical phase noise contribution from the pump laser does not increase with increasing comb line index 28 . By contrast, the phase noise contribution from the microwave modulation signal increases in power with comb line quadratically with q.

This can be shown by modifying the modulator coherence function to include the effects of microwave modulation phase noise 𝜃𝜃(𝑡𝑡):

.

The output optical field can then be written as:

The phase noise amplitude increases linearly with increasing comb line index q, corresponding to a quadratic increase in phase noise power.

For applications that require few comb lines, this increase in microwave phase noise is often negligible because quartz crystal oscillators have very low phase noise. For applications requiring many comb lines, however, the effect of microwave phase noise may be noticeable. Recently, there has been experimental evidence of microwave phase noise suppression in EO comb generators 32,38 . In these studies, the phase noise of freespace resonator-enhanced EO combs is measured and simulated. When the optical and microwave frequencies are resonant, higher order comb lines do not experience a quadratic increase in phase noise power. Instead, high frequency phase noise components are attenuated such that the high frequency phase noise is comparable for all comb lines.

Furthermore, detuning the optical and microwave frequencies from the resonator FSR can further reduce the phase noise power. These experiments suggest that EO comb generators can generate low-noise comb lines over their entire dispersion-limited bandwidth. Additionally, integrated platforms, such as the one presented in the main text, enable additional filtering cavities and structures to be readily included in the resonator structure.

## Round-Trip Phase Model

To include the effect of dispersion, we introduce a round-trip phase model. In particular, we consider the destructive interference that occurs due to the microwave detuning motivates a phase-based resonance approximation for the viable comb bandwidth.

Previous analytical work 29  In a resonator containing an EO phase modulator, the (now time-dependent) resonance condition becomes �Δ𝜙𝜙 𝑞𝑞 + 𝛽𝛽 sin 2𝜋𝜋𝜋𝜋 𝑚𝑚 𝑡𝑡� < 2l, where 𝛽𝛽 is the modulation index and 𝜋𝜋 𝑚𝑚 is the modulation frequency. Here, it is clear that the resonance condition can be satisfied for much larger round-trip phase offsets Δ𝜙𝜙 𝑞𝑞 because within the round-trip resonator propagation time, the modulation term oscillates between negative and positive 𝛽𝛽 (i.e.

-𝛽𝛽 < 𝛽𝛽 sin 2𝜋𝜋𝜋𝜋 𝑚𝑚 𝑡𝑡 < 𝛽𝛽). We can now determine the contributions to the optical phase offset Δ𝜙𝜙 𝑞𝑞 as a function of frequency. The optical phase offset, as discussed in the previous section, does not induce frequency-dependent phase shifts. However, microwave signal detuning and dispersion effects are frequency dependent.

Once the resonator has reached steady state, the output field is an EO comb spaced at the modulation frequency 𝜋𝜋 𝑚𝑚 , such that the 𝑞𝑞th comb line frequency is 𝜋𝜋 𝑞𝑞 = 𝜋𝜋 0 + 𝑞𝑞𝜋𝜋 𝑚𝑚 . A mismatch between the microwave frequency and the resonator free spectral range, Δ𝜋𝜋 𝑚𝑚 , results in a frequency-dependent phase offset 𝜙𝜙 𝑚𝑚𝑖𝑖𝑚𝑚𝑚𝑚𝑜𝑜 (𝑞𝑞) = 2 𝜋𝜋𝑞𝑞 Δ𝜋𝜋 𝑚𝑚 𝑇𝑇. With a 50 GHz microwave drive and β = 1.2π, an EO comb spanning over 1.3 octave can be generated. c, Simulated dispersion for an air-cladded LN waveguide with a different geometry optimized for octave spanning comb with small microwave driving amplitude.

# Extended data figure legends

d, An octave-spanning EO comb is shown with β = 0.3π. e, Another example of an aircladded LN waveguide with dispersion engineered for broad comb generation. f, Such EO comb generation features a flat response over 600 nm. A broad comb spanning less than an octave can be generated in devices with small microwave modulation amplitudes and high-Q factor optical resonators.

# Acknowledgements

This work is supported by: National Science Foundation award numbers ECCS-1609549, ECCS-1740291 E2CDA, ECCS-1740296 E2CDA, DMR-1231319; the Harvard University Office of Technology Development, Physical Sciences and Engineering Accelerator Award; and Facebook, Inc. Device fabrication is performed at the Harvard University Center for Nanoscale Systems, a member of the National Nanotechnology Coordinated Infrastructure Network, which is supported by the National Science Foundation under award number ECCS-1541959.

# Data availability

The data sets generated and/or analysed during the current study are available from the corresponding authors on reasonable request.

# Author information

For an arbitrary dispersion profile, it is possible to find the frequency-dependent phase offset by integrating the group velocity dispersion profile of the waveguide. However, if the dispersion is approximately linear with frequency, the dispersion-related phase offset is Δ𝜙𝜙 𝑑𝑑𝑖𝑖𝑑𝑑𝑝𝑝 (𝑞𝑞) = 2𝜋𝜋(𝑞𝑞 𝜋𝜋 𝑚𝑚 ) 2 𝛽𝛽 2 𝐿𝐿 where 𝛽𝛽 2 𝐿𝐿 is the round-trip group velocity dispersion in fs 2 /mm.

To first order we then have a model for the total phase offset as a function of frequency, Δϕ q = Δϕ opt + Δϕ micro (q) + Δ𝜙𝜙 𝑑𝑑𝑖𝑖𝑑𝑑𝑝𝑝 (𝑞𝑞). In fact, this model agrees exactly with the analytical model for the output comb shape developed in 12 . In the case of maximum comb bandwidth, corresponding to zero microwave detuning and optical detuning satisfying

, agreeing with up to a factor of √2 due to the difference in FSR of a Fabry-Pérot resonator and ring resonator of identical length 29 .

Using this model, it is a straightforward optimization problem to start with the frequencydependent round-trip resonance condition and alter the optical and microwave detuning so that the resonance condition is satisfied only for a desired frequency region, as is done to demonstrate the one-sided comb in Fig. 3c 

