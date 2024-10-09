# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH OR DEVELOPMENT

This invention was made with government support under Grant No. FA9550-11-0014, awarded by the Air Force Office of Scientific Research. The government has certain rights in the invention.

## BACKGROUND

The disclosed subject matter relates to techniques for providing a frequency standard using spin states of a defect in a diamond structure.

Atomic clocks can serve as the basis for accurate systems in use for measuring time and frequency. They can be utilized in a number of applications, including communication, computation, mobile devices, sensors, autonomous vehicles, undersea oil/gas exploration, space navigation, aviation, cruise missiles, and navigation systems (e.g. global positioning systems (GPS)).

Certain frequency standards can derive their stability from hyperfine level splitting of energy states in atoms such as Cs, Rb, or H. When an oscillating magnetic field is resonant with the energy difference of these internal states, a change in population between levels changes the radiofrequency or optical absorption. Certain techniques can modulate the driving frequency and monitor the absorption as a correction for a tunable active reference oscillator, e.g. a quartz crystal, thus stabilizing it to the atomic line.

Single trapped ions and ensembles of atoms trapped in optical lattices can provide a frequency standard with accuracy exceeding the international cesium standard, and can enable the observation of general relativity corrections within a few meters. Such techniques, however, can require infrastructure that encompasses several tens of cubic meters of space.

Portable standards based on rubidium vapor cells can provide stability for time scales ranging from 1 s to 104 s and can be used in connection with satellites, laboratory equipment, and cellular communications. Mobile devices, which may not contain their own precision standards, can share GPS time signals for maintaining communication standards, but when the external lock signal is obstructed, a precise local frequency standard with minimal drift can be necessary to maintain synchronization.

Accordingly, there is a need for improved techniques for providing a frequency standard for time-keeping.

Nitrogen Vacancy Centers (NVC) are point defects in the diamond crystal structure. The substitution of a nitrogen atom for a carbon atom in the diamond structure can create a lattice vacancy that can be occupied by three unpaired electrons. In a neutral nitrogen vacancy defect, N—V0, two of the unpaired electrons can form a quasi covalent bond, while the third electron remains unpaired. However, the three electrons can exhibit axial symmetry, and the three continuously exchange roles. A negative nitrogen vacancy, N—V′, can have an additional electron associated with the vacancy which forms an S=1 structure that has a long-lived spin triplet in its ground state that can be probed using optical and microwave excitation. This can allow for spin manipulation of the NVC.

The NVC can have trigonal C30 symmetry and 3A2 ground state with total electronic spin S=1. Spin-spin interaction can lead to a zero-field splitting between the ms=0 and ms=±1 manifolds, where the quantization axis is along the NV-axis. NVCs can have a crystal field splitting frequency (Dgs) of, for example, 2.870 GHz in the absence of an external magnetic field and in the absence of other environmental factors, including strain. This zero-field splitting frequency can be changed by the application of magnetic fields in the direction of the NVC through the Zeeman effect.

## SUMMARY

In one aspect of the disclosed subject matter, a method of obtaining a frequency standard from the crystal field splitting frequency of a nitrogen vacancy center in a diamond structure is provided. In one embodiment, the method can include applying an initial, adjustable microwave field to a diamond structure. Optical excitation of the diamond structure can produce a detectable photoluminescent response, with that response being modulated in intensity by the frequency of the microwave field being applied. From the modulation of the photoluminescent response, the phase shift between the microwave field and the crystal field splitting frequency of the nitrogen vacancy center in the diamond structure can be determined. The frequency of the microwave field can be adjusted until the detected phase shift is below a predetermined threshold. That microwave frequency then can be used as the frequency standard.

In certain embodiments, the microwave field frequency can be tested continuously, even after the original determination of the frequency standard, to prevent drift of the frequency standard.

In one embodiment, an ensemble of nitrogen vacancy centers can be optically excited and probed with the microwave field to find the frequency standard. The use of multiple nitrogen vacancy centers can provide additional accuracy in the measurement of the frequency standard.

In another embodiment, a sequence of light and microwave pulses can be used. For example, the diamond structure can be first subjected to optical pumping to drive the spin state of a plurality of nitrogen vacancy centers to the |0> state. After optical pumping ceases, a first microwave pulse of flip angle π/4 can be applied to the diamond structure. After a time T, a second microwave pulse of flip angle π can be applied in the opposite phase of the first pulse. After a second time T, a third microwave pulse identical to the first microwave pulse can be applied. Following the third microwave pulse, the transient fluorescent response of the diamond structure can be measured by applying an optical pulse. The measurement of the transient fluorescent response can be used to calculate the phase shift of the initial microwave pulse frequency from the crystal field splitting frequency.

In an embodiment, two diamond structures can be tested at the same time in order to stabilize the measurements against temperature dependence. In another embodiment, a single diamond structure can be placed in a clamp to engineer strain upon the diamond structure, in order to stabilize the measurements against temperature dependence.

In another aspect of the disclosed subject matter, a system for obtaining a frequency standard based on the crystal field splitting frequency of nitrogen vacancy centers in a diamond structure is provided. One exemplary system can include a dielectric cavity adapted to at least partially encompass the diamond structure, a light source configured to optically excite the nitrogen vacancy center and thereby allow the nitrogen vacancy center to emit a photoluminescent response, a photodetector configured to detect photoluminescence, a stripline configured to emit a microwave field upon the diamond structure, a processor to calculate the phase shift between the microwave emission frequency and the crystal field splitting frequency of the nitrogen vacancy center in the diamond structure, and a controller to adjust the frequency of the microwave emissions.

In an embodiment, the photodetector can be a silicon photodiode. The dielectric cavity can include a pair of Bragg reflectors placed on opposite sides of the diamond structure and outside the plane of the stripline for microwave emissions. The Bragg reflectors can create a 532 nm resonant cavity encompassing the diamond structure. The light source can be a surface emitting laser adapted for generation of a doubled 1064 nm beam.

In an embodiment, the light source and the microwave stripline can be configured to apply pulsed emissions upon the diamond structure. The photodetector can be configured to measure the photoluminescent response after an optical pulse.

In an embodiment, two diamond structures can be placed in two systems in the dielectric cavity, the light source, the photodetector, and the stripline. The processor can be configured to detect the phase shift for both diamond structures and thereby stabilize the measurements for temperature dependence. In a further embodiment, the two diamond structures can be clamped to two substrates with different thermal expansion coefficients. The diamond structure can be coupled to a single clamp to engineer strain upon the diamond structure.

Throughout the drawings, the same reference numerals and characters, unless otherwise stated, are used to denote like features, elements, components or portions of the illustrated embodiments. Moreover, while the disclosed subject matter will now be described in detail with reference to the Figs., it is done so in connection with the illustrative embodiments.

## DETAILED DESCRIPTION

Techniques for providing a frequency standard using spin states of a defect in a diamond structure are disclosed herein. Diamond structures can have many desirable characteristics for providing a frequency standard. For example, a single crystal diamond can be grown into a micron-scale, radiation hard chip, which makes it portable and well-suited for integration in a semiconductor fabrication process. Additionally, a frequency standard derived from the spin lifetime of the nitrogen vacancy center (NVC) can resemble atomic and molecular systems. The optical detection of the NVC can also increase the signal-to-noise ratio for a solid-state standard. A sufficiently high density of NVCs in a chip can allow for comparable frequency stability in smaller sensor volumes.

In one aspect of the disclosed subject matter, techniques for obtaining a frequency standard from the crystal field splitting frequency of a nitrogen vacancy center in a diamond structure can include continuously applying an initial, adjustable microwave field to a diamond structure concurrently with optical excitation to produce a detectable photoluminescent response. In another aspect of the disclosed subject matter, techniques for obtaining a frequency standard from the crystal field splitting frequency of a nitrogen vacancy center in a diamond structure can include a pulsed technique, applying one or more microwave pulses to a diamond structure, and then observing the transient photoluminescent response by applying an optical pulse. In yet another aspect of the disclosed subject matter, techniques for obtaining a frequency standard from the crystal field splitting frequency of a nitrogen vacancy center in a diamond structure can include using temperature stabilization techniques to improve the accuracy of the frequency standard.

An exemplary embodiment of a system for obtaining a frequency standard using spin states of defects in diamond will now be described with reference to FIG. 1. and FIG. 4, for purposes of illustration and not limitation.

A diamond chip containing NVCs 110 on a substrate 119 can be exposed to optical and microwave emissions. The diamond chip can be grown onto the substrate, for example, via chemical vapor deposition (CVD). Alternatively, a pre-fabricated diamond chip can be implanted on or integrated with the substrate. The photoluminescent (PL) response from the optical excitation can be detected using a photodetector 140 and the phase shift between the microwave emission and the field-splitting frequency, Dgs, of the NVC can be determined using a processor 150.

The optical emissions can be created by a light source 120 arranged to illuminate one face of the diamond chip. The light source can be configured to produce, for example a laser beam 125 having a specific power level 121 and a specific wavelength 123. In one embodiment, the light source can be configured to produce a 1064 nm laser that is doubled prior to interacting with the diamond chip 125. Alternatively, the light source can be configured to produce approximately a 520-550 nm laser, and in certain embodiments can be configured to produce a 520 nm laser.

A dielectric cavity 115 can be placed around the diamond chip 110 to lower the power requirements for the laser beam 125. The dielectric cavity can be formed for example by a pair of Bragg reflectors, which can create a 532 nm resonant cavity around the diamond chip 110. One of the Bragg reflectors can be placed between the diamond chip 110 and the light source 120 and the second reflector can be placed on the opposite side. The Bragg reflectors can be made of a quarter wave stack of materials with different reflective indices, using for example, materials such as silicon dioxide, titanium dioxide, tantalum pentoxide, or the like. This can allow the laser beam 125 to resonate within the cavity and can cause optical excitation of the NVCs in the diamond chip 110.

The microwave field can be created by a planar stripline 131 that can encircle the diamond chip 110 on a single plane as seen in FIG. 4. Alternatively, the microwave field can be created by other suitable techniques, for example with other geometries and suitable antennas. The microwave cavity can also be fitted with reflectors to create a resonant cavity 111 for microwave emissions, for example at 2.87 GHz. A frequency controller 160 can determine the frequency of the microwave emissions based on input data from a microprocessor 150, and can report the frequency back to the microprocessor 151.

The optical emissions can excite the NVCs, to produce a photoluminescent (PL) response 127. NVCs can absorb green light and emit a PL response between, for example, 637-800 nm. As described in more detail below, the intensity of the PL response can correspond to the polarization of the spin states of the NVC, which can depend on the frequency of the microwave field. Thus, the processor 150 can determine, based on a signal from the photodetctor 140, when the PL response corresponds to an applied microwave field equal to a known field-splitting frequency of the NVC, and thus can lock the frequency controller 160 at such a frequency, thereby providing a frequency standard.

Exemplary embodiments of techniques for providing a frequency standard using spin states of a defect in diamond will be described in detail below. For purposes of illustration, and not limitation, the level structure and fluorescent properties of the nitrogen vacancy, as they relate to exemplary and non-limiting bases for a frequency standard disclosed herein (e.g., the zero-field splitting of the NV as a frequency standard), will first be described. However, one or ordinary skill in the art will appreciate that certain properties of the NV center in diamond are well known, and the following description is not intended to limit or otherwise narrow the scope of the disclosed subject matter. Additionally, throughout the following description, certain characterizations of stability and quality factor will be described for purposes of illustration, and not limitation. One of ordinary skill in the art will appreciate that such characterizations are not intended to limit or otherwise narrow the scope of the disclosed subject matter, but are provided as an exemplary method of describing the techniques disclosed herein.

Atomic clocks, generally, can drive their stability from a large quality factor (“Q-factor”), which can be given as Q=v/Δv, of the probed resonance, with narrow linewidth, Δv, being smaller than the resonant frequency v. The NYC in diamond can have a ground state spin triplet characterized by long coherence times (for example, greater than 1 ms), a ground state crystal field splitting with an intrinsic resonance frequency near 2.870 GHz, which can be independent, to lowest order, of applied magnetic field, and spin states that are optically polarizable and detectable on single defect length scales (for example, approximately 1 μm).

With reference to FIG. 5(a), relevant spin sublevels of the NVC (0, 1, 2, 3 and S) are depicted. Optical absorption of green laser light can cause broadband photoluminescence (PL) of the NVC from, for example, 637-800 nm. A spin dependent intersystem crossing between the excited spin triplet 3 and the metastable, dark singlet level S can change the integrated PL for the spin states |0> and |±1. The deshelving from the singlet can occur primarily to the |0> spin state, providing a means to polarize the NVC. Microwave fields resonant between levels |0> and |1> can perturb the spin populations, and thus the PL response. This can be characterized, for example, in two ways: 1) by measuring a continuous wave response to simultaneous optical and microwave fields (for example, as demonstrated in FIG. 5(b), or 2) in a pulsed manner, by preparing a state using only microwaves, and observing the transient PL response.

For purposes of illustration, and not limitation, the relevant spin dynamics can be described by Hamiltonians for the lowest and first excited triplet state and two metastable singlet states. In an exemplary embodiment, as described below, the response of only the ground state triplet sublevels to resonant excitation can be monitored, yielding the ground state Hamiltonian:

Hgs=(Dgs+d∥σz)Sz2+gμb{right arrow over (S)}·{right arrow over (B)}+d195σ⊥(SxSy+SySz)+d⊥σ⊥(Sz2−Sy2)   (1)

where d¶,⊥ are the ground state electric dipole moment components along and perpendicular to the C30 symmetry axis of the defect. Dgs is the ground state crystal field splitting frequency (e.g., 2.870 GHz), μb is the Bohr magnetron, and g is the Uncle factor (assumed to be isotropic). Sk are spin-1 operators in the k={x, y, z} directions. The local electric field vector, induced by crystal strain, is {right arrow over (σ)}. In the limit of static magnetic and electric fields much smaller than Dgs, the eigenfimctions are those of the Sz operator, as shown in FIG. 5.

A driving field at frequency co can induce electron spin resonance (ESR) transitions between |0> and |±1>. On resonance (ω≈Dgs), the PL response can decrease and can provide a feedback signal as to lock co to Dgs. The dynamics can be viewed as a response to a time-varying magnetic field B1=2b1 cos(2πωt){circumflex over (x)}; transforming Hgs into an interaction frame defined by the operator V=e2xiωSis z. Under the rotating wave approximation, the Hamiltonian can be:

Hgs1=(Dgs+d∥σz−ω)Sz2+g μbBzSz+g μbb1Sz.   (2)

The relaxation rates of the excited triplet and singlet states, shown in FIG. 5, can play a role in the optical pumping and spin measurement. The total magneto-optical response can be modeled using a master equation approach, such as for example:

\(\begin{matrix}
{\rho = {{\frac{1}{ih}\left\lbrack {H_{gs}^{1},\rho} \right\rbrack} + {\sum\limits_{k}{L_{k}L_{k}^{\dagger}}} - {\frac{1}{2}L_{k}^{\dagger}L_{k}\rho} - {\frac{1}{2}\rho \; L_{k}^{\dagger}L_{k}}}} & (3)
\end{matrix}\)

where ρ is the density operator for the NVC ground, excited triplet, and effective singlet states. The jump operators, Lk, can have magnitudes corresponding to relaxation rates √{square root over (Tk)}. The solution to the equation can yield the total magneto-optical response for both continuous and pulsed excitation.

A first exemplary embodiment of a technique for providing a frequency standard using spin states of a defect in diamond will now be described in detail, for purposes of illustration and not limitation, with reference to FIG. 2. In connection with this description, reference will be made to FIG. 1 for purposes of illustration and not limitation, as one of ordinary skill in the art will appreciate that certain variations to the system depicted therein can be used.

This exemplary technique, which can be referred to as a “Continuous Wave” (CW) technique, can include continuously applying an initial, adjustable microwave field to a diamond structure concurrently with optical excitation to produce a detectable photoluminescent response. In this embodiment, a diamond chip containing NVCs 110 on a substrate 119 can be exposed to optical emissions and exposed to microwave emissions concurrently and continuously. That is, an optical beam can be generated (201) and directed (205) to the diamond structure. Concurrently, a microwave field can be generated (203) and directed (206) to the diamond structure. The optical beam and microwave field can be generated and can have characteristics as described herein above in connection with FIG. 1.

Under continuous excitation by a microwave field of intensity Ω=gμbb1, detuned from resonance of the NVC by an amount Δ=Dgs−ω, a broad, phonon-assisted PL response can occur following the equation:

\(\begin{matrix}
{{{PL}:{F\left( {I,\Omega,\Delta} \right)}} = {{\gamma\rho}_{22}^{ss} + {\frac{\gamma^{2}}{k + \gamma}{\rho_{33}^{ss}.}}}} & (4)
\end{matrix}\)

Here ρ22ss and ρ33ss can represent the population of the first excited state spin sublevels in the steady-state, as analytically derived from Equation 3. FIG. 5(b) shows an exemplary response for F for varied detunings, which can be approximated by the Lorentzian:

\(\begin{matrix}
{{F(\Delta)} = {{I_{0}\left( {1 - \frac{C\; \delta \; v^{2}}{\left( {\Delta/\pi} \right)^{2} + {\delta \; v^{2}}}} \right)}.}} & (5)
\end{matrix}\)

The PL response can be detected (211) using a photodetector 140. The photodetector can be, for example, a silicon photodiode placed adjacent to the diamond structure and opposite the light source. The photodiode can measure the intensity of the PL response and reports the intensity to the microprocessor 150.

By calculating the PL response, the phase shift A between the microwave field and Dgs can be determined (215) by the processor 150 by using Equation 5. The frequency of the microwave field can be varied (221) by the controller 160 until the phase shift is determined to be below the predetermined threshold (213). The frequency of the microwave field at that point 153 can be used as a frequency standard (220).

The stability of the frequency standard can be given by a derivation from the resonance curve by considering the Allan variance:

\(\begin{matrix}
{{\sigma_{y}(\tau)} = {\frac{1}{2\pi \; Q}\frac{1}{\left( {S/N} \right)}\frac{1}{\sqrt{\tau}}}} & (6)
\end{matrix}\)

where S/N is the signal to noise ratio, which can depend on both the photon shot noise as well as the imperfect modulation of the resonance (e.g., C≠1), and x is the averaging time. The intrinsic linewidth can be limited by the paramagnetic and nuclear spin environments which fluctuate during the measurement. This linewidth can broaden if the microwave and optical transitions are driven near saturation; however, higher pump powers can also increase the depth of the dip (C→1). Far below optical saturation, the PL rate can be sufficiently small, and the modulation depth (C) reduced, so as to cause a decrease in the stability per averaging time. A condition can exist which balances line broadening with the reduced signal, and in accordance therewith, the linewidth can be approximately 3.6 MHz (T2*=88 ns), and off-resonance fluorescence rate can be approximately 9400 photon/s (accounting for a finite detector efficiency), and a 17% modulation depth. With these parameters, the Allan variance can be, for example, σy(τ)=8.124×10−5τ−1/2 for a single NVC. That is, the laser excitation can be reduced far below saturation so that optical power broadening can reach the homogeneous linewidth. At such low pump powers, the fluorescent photon flux can be small such that the gains in Q-factor can be reduced by losses in signal to noise ratio S/N.

A second exemplary embodiment of a technique for providing a frequency standard using spin states of a defect in diamond will now be described in detail, for purposes of illustration and not limitation, with reference to FIG. 3 and FIG. 6. In connection with this description, reference will be made to FIG. 1 for purposes of illustration and not limitation, as one of ordinary skill in the art will appreciate that certain variations to the system depicted therein can be used.

This exemplary technique, which can be referred to as a “pulsed” technique, can include continuously applying a pulsed microwave excitation scheme, which can monitor transient fluorescence behavior. In this embodiment, optical pumping of the NVC can first prepare the initial state |ψ0=|m5=0. This optical pumping can cease before microwaves are emitted. That is, an optical pulse can be generated (301) and directed to the diamond structure.

A modified Hahn echo sequence can be used to yield a PL response and eliminate the effects of external magnetic fields on the spin response. First, a microwave pulse with a frequency close to 2.870 GHZ and a flip angle of π/4 around the x-axis of the NVC can be generated (310). After waiting (311) a period T (which can be, for example, about I ms), a second microwave pulse can be generated (313).

The time period T can be, for example, close to the electron spin coherence time, can be approximately 1 ms for high-purity diamond samples. This second pulse can have a flip angle of π. After waiting (312) a second period of time T, a third microwave pulse can be generated (315). This third pulse can be identical to the first pulse with a flip angle π/4. This modified Hahn echo sequence can extend the coherence time Tc (which in the diamond NV can be approximately tens of microseconds) to approximately T2 by, for example, removing slowly varying magnetic fields. In this manner, the modulation of the PL response can persist, as the Spin-1 nature of the NVC can allow for a PL signal proportional to the frequency drift. It should be noted that a conventional Hahn echo sequence can remove the phase accumulation associated with frequency drift with the additional π pulse therein.

Evolution under this drift echo sequence, Uecho, can follow the equation

\(\begin{matrix}
{\left. {{\psi_{f}\rangle} = {{U_{echo}{\psi_{0}\rangle}} = {{\frac{1}{\sqrt{2}}{\sin (\varphi)}{0\rangle}} - {\frac{1}{2}{\cos (\varphi)}\left( {{+ 1}} \right)} + {{- 1}\rangle}}}} \right),} & (7)
\end{matrix}\)

where φ=(Dgs−w)T=δwT. A transient fluorescence measurement can be recorded (305) immediately following the third pulse. For example, the response can be measured by recording the photocurrent with the photodetector 140 for about 300 ns timed with a pulse of green light (303) from the light source 120. In certain embodiments, the timing can be shorter than the electron spin reset time, which can be for example between approximately 200 ns and approximately 500 ns.

The transient PL response of the NVC can be modeled, for example, using projective measurements. The operator M can describe the spin expectation value for a PL measurement, M=α|00|+b(|+1)<+1|+|−1)<−1|), where a and b are independent Poisson random variables. The fractional frequency deviation can vary as the quantum observable, M for the state |ωf> according to:

\(\begin{matrix}
{{\frac{\delta \; w}{w_{0}} = {\frac{1}{w_{0}}\frac{\langle{\Delta \; \hat{M}}\rangle}{w_{0}{{{\partial{\langle\hat{M}\rangle}}/{\partial w}}}}}},} & (8)
\end{matrix}\)

where Δ{circumflex over (M)}2>=<{circumflex over (M)}2>−<{circumflex over (M)}>2 is the variance of th operator. For room temperature spin readout of the NVC, for example, 2a=3b. By calculating the moments of {circumflex over (M)} and assuming the results for total time τ=M′T are accumulated, the following equation can be derived:

\(\begin{matrix}
{{{\langle\frac{\delta \; w}{w_{0}}\rangle}_{M^{1}} = \frac{\xi}{D_{gs}\sqrt{T\; \tau}}},} & (9)
\end{matrix}\)

with ξ≈5 due to a combination of imperfect spin readout (i.e. b≠0), inefficient collection of photons (i.e. a<<1), and a small ratio of shelving state to radiative lifetime (λ/γ).

The predetermined threshold for the phase shift for an ensemble of NVCs can be predetermined, for example, by multiplying the deviation for a single NVC, 8.8×10−9/√τ by 1/√N, where N is the number of NVCs. N can be estimated by taking the density of pure diamond, 1.74×1023 C atoms/cm3, with the NV′ defect fraction at 0.01 parts per billion (ppb), which results in ˜1.74×1012 NVCs/cm3. For a diamond chip of cross-section area of 1 mm3 and a thickness of approximately 100 μm, this can result in a deviation of 2×10−13/√τ in accordance with this exemplary technique. Thus, a diamond film with thickness of approximately 100 μm can give an Allen variance σypulsed˜6.7×10−13 τ1/2.

If the determined phase shift is above the predetermined threshold (320), the microwave frequency can be adjusted (317) by the controller 160 and the pulse sequence can be repeated. If the detellnined phase shift is below the predetermined threshold (320), then the frequency of the microwave field determined by the processor 153 can be used as the frequency standard (330).

A third exemplary embodiment of a technique for providing a frequency standard using spin states of a defect in diamond will now be described in detail, for purposes of illustration and not limitation, with reference to FIG. 7. In this embodiment, techniques for obtaining a frequency standard from the crystal field splitting frequency of a nitrogen vacancy center in a diamond structure can include using temperature stabilization techniques to improve the accuracy of the frequency standard.

The resonance frequency corresponding to Dgs of an NV center can vary as a function of temperature, θ. At room-temperature, dDgs/dθ can be equal to approximately 74.2 kHz/K for mm-sized samples. At temperatures of approximately 5K, dDgs/dθ can be equal to approximately 100 kHz/K, and at higher temperatures (up to approximately 600K), dDgs/dθ can be equal to approximately 100 kHz/K. Thus, zero-field splitting temperature dependence can be nonlinear. This temperature dependence can be a result of thermal expansion of the diamond. For example, local lattice spacing of the NV center can be distorted, causing changes in the orbital overlaps which determine Dgs.

The temperature of the diamond chip can be stabilized, for example, using commercially available Peltier coolers with PID loops (for example to within 0.01K). This can allow, for example, 742 Hz uncertainty in the zero-field splitting, or a fraction frequency stability of approximately 2.58×10−7 at room temperature. However, in this case, ensemble averaging would not increase certainty, as all NV centers can shift equally due to isotropic expansion.

In accordance with this exemplary embodiment, anisotropy can be induced in the crystal's temperature response. Two different dependences can be identified, and can be locked in a feedback loop to enhance temperature stability. In this embodiment, two or more “clocks” (that is, the subject matter described herein), can have different temperature dependences. Different temperature dependences can be achieved, for example, by utilizing two distinct diamond slabs mounted on substrates with different thermal expansion coefficients.

For example, and with reference to FIG. 7, two diamond chips 815 and 825 can be clamped into two different substrates 810 and 820. The substrates can have different thermal expansion coefficients. One diamond chip 815 can be clamped in a stiff material 810 with Young's modulus Et and a high thermal expansion coefficient ηc1. This material can be, for example, brass. The second diamond chip 825 can be clamped in a different material 820 with Young's modulus E2 and a lower theiival expansion coefficient ηc2 where ηc2<ηc1. The second material can be, for example, tungsten. The cross-sectional area of the substrates can be much greater than that of the diamond chips. Both diamond chips and the substrates can be assumed to start at the same temperature θ. The change in strain imparted on the diamond can be approximated as Δε1,2≈ηd(1+ηc1,2Ec1,2/Ed) Δθ, where Δθ is the temperature difference between the initial set-point T0. This initial set-point can be determined at a point where the two clocks have the same initial frequency ω0 and can be adjusted by pre-loading strain within the samples, as seen in FIG. 7(a).

A conventional thermal feedback system using thermistors can maintain the system near T0 within ˜10−2-10−3 K. To compensate for smaller temperature drifts, the different temperature dependencies of the two diamond chips can be exploited to yield the equations:

ω1(T)=ω0+β1Δθ  (10)

ω2(T)=ω0+β2Δθ  (11)

where

\(\beta_{1,2} = {{\frac{ɛ}{\theta}\frac{D_{gs}}{ɛ}} = {{\eta_{d}\left( {1 + {\eta_{{c\; 1},2}{E_{{c\; 1},2}/E_{d}}}} \right)}{\left( {{D_{gs}}/{ɛ}} \right).}}}\)

At time τ=0, both clocks can be at the same temperature θ0, before the temperature is allowed to fluctuate within a small range around θ0. After time t, these clocks have acquired a phase:

φ1,2(t)=ω0t+∫01β1,2, Δθ(t)dt′±Δφ0   (12)

where Δφ0=ξ√{square root over (t)}/°{square root over (θ2,ensN)} is the phase uncertainty. The difference between the two phases can be recorded by mixing and low-pass filtering the two clock signals, giving Δφ(t)=φ2(t)−φ1(t)=∫01Δβ1,2Δθ(t′)dt′±√{square root over (2)}Δφ0, where β1,2=β2−β1 and an identical variance is assumed for φ1(t) and φ2(t).

The temperature fluctuations in clock ‘1’ can be corrected as follows:

\(\begin{matrix}
\begin{matrix}
{{\varphi_{1}^{\prime}(t)} = {{\varphi_{1}(t)} - {\int_{0}^{t}{\beta_{1}\Delta \; {T\left( t^{\prime} \right)}{t^{\prime}}}}}} \\
{= {{\varphi_{1}(t)} - {\left( {\int_{0}^{t}{\beta_{1,2}\Delta \; {T\left( t^{\prime} \right)}{t^{\prime}}}} \right) \cdot \frac{\beta_{1}}{{\Delta\beta}_{1,2}}}}} \\
{= {{\varphi_{1}(t)} - {\frac{\beta_{1}}{{\Delta\beta}_{1,2}}\left( {{{\Delta\varphi}(t)} \mp {\sqrt{2}{\Delta\varphi}_{0}}} \right.}}}
\end{matrix} & (13)
\end{matrix}\)

The phase can be divided by t to yield the frequency, from which the uncertainty of the new “synchronized composite” after a time t:

\(\begin{matrix}
\begin{matrix}
{\frac{{\Delta\omega}_{1}^{\prime}}{\omega_{1}^{\prime}} = {\frac{\xi}{\sqrt{T_{2}{Nt}}D_{gs}}\left( {1 + {2\left( \frac{\beta_{1}}{{\Delta\beta}_{1,2}} \right)^{2}}} \right)^{1/2}}} \\
{= {\left( \frac{\Delta\omega}{\omega_{0}} \right)_{T = T_{0}}{\left( {1 + {2\left( \frac{\beta_{1}}{{\Delta\beta}_{1,2}} \right)^{2}}} \right)^{1/2}.}}}
\end{matrix} & (14)
\end{matrix}\)

Thus, the uncertainty can be reduced when the temperature dependencies of the two clocks can be large. For example, with reference to equation 14, when Δβ2 >>β1, the performance of the composite clock can be similar to that of a bare temperature-insensitive NV clock. While the phase difference can be directly computed and the clock frequency corrected digitally, the phase difference can also be used to stabilize the temperature, particularly where the two clocks can be maintained at a frequency difference, vbeat˜10 kHz, so that the beat frequency can be locked to a high Q (˜106) quartz oscillator.

In another exemplary embodiment, the temperature dependence can be resolved in a single diamond system through the use of engineered strain. Within the ground state Hamiltonian, as expressed in equation 1, the strain dependence can be hidden in the effective electric field vector, {right arrow over (σ)}. In terms of the actual components of the strain tensor ε, perturbation to the spin Hamiltonian can take the form FijklSiSjεkl, where F is the forth order strain response tensor. Symmetries can reduce the number of allowed terms to eight totally symmetric combinations, and of these, only the terms with an Sz2 coefficient can be considered. Thus, the strain dependence of the zero-field splitting can generally be characterized as:

(Dgs+A1(εxx+εyy)+A2εzz)(Sz2−2/3),   (14)

where A1 and A2 are parameters which can require experimental input. In the case of isotropic expansion, εxx=εyy=εzz dDgs/dθ can be equal to 2A1+A2. By clamping the diamond along a specific director, an anisotropic lattice response can significantly reduce the effective temperature dependence of the zero-field splitting.

For example, with reference to FIG. 7 and FIG. 8, a small temperature shift Δθ, near θ0, can cause a diamond slab of length Ld to expand by ΔL=LdηdΔθ. If the diamond slab were instead clamped, this expansion can be modulated. For example, Material 2 830, which forms the bottom of the clamp, can have a low thermal expansion coefficient and a high Young's modulus. Material 1 832, which forms the sides of the clamp, can have a high thermal expansion coefficient and a high Young's modulus. With varying temperature, a pressure P=EdΔLd/L=Edεd=EdΔTηd can be exerted to compress the diamond chip 835 by −ΔL. For temperature changes 0.01K, this pressure is approximately 12.2 kPa.

In connection with this embodiment, the different temperature dependences of NVCs in different orientations within the diamond chip can be used. NVCs can have one of four directions within the crystal structure. Anisotropic strain can be induced in the diamond chip, for example by patterning slits into the diamond chip. For example, the slits may be patterned using optical or electron beam lithography, followed by plasma etching with gasses such as oxygen or chlorine.

The single diamond chip system can be measured by creating a microwave field to measure the transient photoluminescence response of NVCs in one orientation, then measuring the response of NVCs in another orientation that will have a different temperature dependence.

The foregoing merely illustrates the principles of the disclosed subject matter. Various modifications and alterations to the described embodiments will be apparent to those skilled in the art in view of the teaching herein. It will thus be appreciated that those skilled in the art will be able to devise numerous techniques which, although not explicitly described herein, embody the principles of the disclosed subject matter and are thus within the spirit and scope of the disclosed subject matter.

