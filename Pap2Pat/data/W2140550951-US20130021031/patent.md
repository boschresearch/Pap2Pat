# DESCRIPTION

This application claims Paris Convention priority of EP 11 174 360.5 filed Jul. 18, 2011 the entire disclosure of which is hereby incorporated by reference.

## BACKGROUND OF THE INVENTION

The invention concerns a method for high resolution NMR (=nuclear magnetic resonance) measurements comprising the application of excitation pulses and the acquisition of data points, whereby a dwell time Δt separates the acquisition of two consecutive data points. A method as described above is known from Andrew E. Derome, “Modern NMR Techniques for Chemistry Research”, Pergamon Press, 1987.

Double-resonance techniques were first introduced into high-resolution CW-NMR by Bloch in 1954.[1] Bloom and Shoolery[2] have shown that the application of an rf field B2 to 31P nuclei such that γB2>>2π|J| can lead to the collapse of the doublet in the 19F spectrum arising from a heteronuclear coupling J(31P-19F). Freeman and Anderson[3, 4]proposed a theoretical description that is applicable to spin systems with either homo- or heteronuclear couplings and explains the spectral complexities and multiplicities arising from the secondary rf field B2 while sweeping the frequency of the main rf field B1 to observe the response in CW (=continuous wave) fashion. In particular, information about the topology of non-degenerate energy levels and the relative signs of coupling constants can be extracted.[5, 6]A detailed discussion of these effects, which have later become known as “spin tickling” experiments, has been presented elsewhere.[7, 8] Ever since, the development of advanced methods for the characterization of more and more complex systems (often in biomolecules) has been accompanied by a desire to achieve a gain in resolution and spectral simplification. The removal of homonuclear scalar interactions can simplify assignments in overlapping regions in both 1D and 2D spectra, and a number of methods have been proposed to eliminate the fine structure due to J-couplings.[9-15] However, none of these methods appear to have found widespread applications. Moreover, they usually only achieve a decoupling effect in the indirect dimension of 2D spectra. A method similar to the above is known as homonuclear decoupling, where a weak rf field of constant amplitude is applied throughout the observation of the signal. This method suffers from problems of interference between rf irradiation and signal observation, and is difficult to extend to multiple frequencies.

The object of the present invention is to present an effective and fast method of decoupling of homonuclear couplings.

## SUMMARY OF THE INVENTION

This object is achieved by that one or more tickling rf (=radio frequency) pulses of duration τp are applied within each dwell time Δt, and that the average rf field amplitude of each of the tickling rf pulses is between ω1=ω1τp/Δt=π/10J and ω1=ω1τp/Δt=10πJ, wherein J being the scalar J-coupling constant and ω1=γB1 with γ being the gyromagnetic ratio and B1 being the strength of the magnetic component of each tickling rf pulse. Decoupling of homonuclear scalar interactions in J-coupled spin systems in high-resolution NMR spectra of solutions can be achieved by applying brief but fairly intense radio-frequency (rf) “tickling” pulses in the intervals (dwell times) between the acquisition of data points. The average rf field amplitude, i.e., the peak amplitude scaled by the duty cycle, should approximately satisfy the condition ω1≈πJ. It is considered sufficient if <ω1> is between (π/10)J and 10πJ for the method to work. The method is effective over a wide range of chemical shift differences between the J-coupled pairs of nuclei.

This invention presents a 1D technique to remove homonuclear scalar interactions by applying a train of brief rf-pulses. This method may be seen as a combination of Fourier and tickling spectroscopy. In the spirit of self-deprecating acronyms such as INEPT and INADEQUATE, we like to refer to our method as Window-Acquired Spin Tickling Experiment (WASTE). The new method has been tested on proton spectra of a series of samples ranging from moderately strongly- to weakly-coupled spin systems.

A preferred variant of the inventive method is characterized in that the average rf field amplitude of each of the tickling rf pulses fulfils the condition: ω1=ω1τp/Δt=πJ.

While the method seems to work properly with values of <ω1> only approximately reaching πJ, ω1=πJ is found to be the optimal condition.

A further advantageous variant of the inventive method is characterized in that the duration τp of the tickling pulses is between 0,1 μs and 20 μs, preferably about 1 μs. Tickling rf pulses of shorter or longer duration appear to lead to unwanted side effects.

It is advantageous if the data points, which are acquired once in every dwell time, are transformed into a spectrum by a Fourier transformation.

In another preferred variant of the inventive method M tickling rf pulses of duration τp are applied at will within each of multiple dwell times Δt, each tickling rf pulse within each dwell time Δt belongs to a different comb Cm of tickling rf pulses, with m being a positive integer and 1≦m≦M, and all tickling rf pulses belonging to the same comb Cm are equidistant to each other.

Multiple tickling pulses can be applied within each dwell time and grouped into combs, within which the tickling rf pulses are equidistant to each other.

A further variation of this variant is characterized in that the phase of each tickling rf pulse belonging to the same comb Cm is shifted from one dwell time to the next by a constant factor. This variant allows for simultaneous decoupling of several spin systems.

The invention is shown in the drawing:

## DESCRIPTION OF THE PREFERRED EMBODIMENT

FIG. 1 shows a scheme for Fourier tickling experiments. The tall rectangle represents the initial excitation pulse whereas the small rectangle represents a tickling pulse of duration τp applied along the x axis. The black dot represents the acquisition of a single data point. If the receiver runs continuously, this data point is obtained by averaging over all data points acquired in the interval during which the receiver is activated. The Driven Induction Decay (DID) is built up by acquiring n data points through an n-fold repetition of the loop.

Decoupling of homonuclear scalar interactions JAX in coupled spin systems can be achieved by applying brief but fairly intense radio-frequency (rf) “tickling” pulses (typically with a duration τp=1 μs and an rf amplitude 2<ω1/(2π)<3 kHz) between the acquisition of data points. These are separated by intervals (“dwell times”) that may be typically Δt=100 μs if the desired spectral width is 10 kHz. As will be explained below, the average rf field amplitude ω1=ω1τp/Δt should approximately satisfy the condition ω1=πJ. If one “tickles” spin A by placing the carrier frequency of on the chemical shift ΩA, the fine-structure due to JAX collapses in both A and X multiplets. In “linear” AMX three-spin systems with JAX=0 Hz, tickling the central spin M eliminates both interactions JAM and JMX. As a result, all three multiplets collapse and the spectrum shows only three singlets at the isotropic chemical shifts ΩA, ΩM and •ΩX. However, in a general AMX three-spin system with if JMX≠0 where only spin M is tickled, the multiplicity due to JAX is retained for both non-irradiated A and X spins.

In the sequence shown in FIG. 1, we consider the case where the phases of the initial 90° pulse and the tickling pulses are along the y and x axes, respectively. As usual in Fourier spectroscopy, the signal is observed at regular intervals Δt (dwell times) that are inversely proportional to the desired spectral width, so as to fulfil the Nyquist condition. A tickling pulse of length τp and constant rf amplitude ω1=γB1 is applied near the middle of each Δt interval. A so-called Driven Induction Decay (DID) can be acquired by repeating the loop n times until one obtains the desired number of points. Numerical simulations have been performed with the SIMPSON program.[16] Relaxation effects have not been taken into account in this study. The rf carrier of the tickling pulses is set on resonance with the spin A, i.e. ωrf=ωA, so that its offset vanishes, ΩA=ΩA−Ωrf=0. Therefore, in the Zeeman frame rotating in synchronism with Ωrf=ΩA, the Hamiltonian is:

\({H_{Tot} = {{\Omega_{X}I_{z}^{X}} + {2\; \pi \; {JI}^{A}I^{X}} + {{\omega_{1}(t)}\left( {I_{x}^{A} + I_{x}^{X}} \right)}}},\)

where the third term vanishes except during the tickling pulse.

FIG. 2 shows a simulated tickling spectrum stacked from bottom to top as the pulse length τp is progressively increased in steps of 2 μs until continuous spin locking is achieved. The rf field strength is ω1/(2π)=2.5 kHz. The offsets are ΩA/(2π)=0 Hz and ΩX/(2π)=1 kHz, the coupling constant is JAX=10 Hz. The offset of spin X is indicated by a dashed line. All spectra were processed with 1 Hz line broadening because the on-resonance line would otherwise be very narrow and tall.

The evolution of the density matrix can be evaluated numerically using the Liouville-von Neumann equation.[17] In FIG. 2 we explored the effect of the length τp of the tickling pulses by progressively increasing the pulse length τp while keeping the dwell time Δt constant. As the length τp of the tickling pulse is increased, signals appear that are symmetrically disposed on either side of the signal of the on-resonance spin A at ΩA=0 Hz. The offset of the off-resonance spin X is also perturbed, and appears to be “pushed away” from the carrier frequency. This is a manifestation of the Bloch-Siegert effect.[18-20] The apparent chemical shift is:

\(\Omega_{X}^{App} = {\sqrt{\Omega_{X}^{2} + {\langle\omega_{1}\rangle}^{2}} = {\Omega_{X}{\sqrt{1 + \frac{{\langle\omega_{1}\rangle}^{2}}{\Omega_{X}^{2}}}.}}}\)

Taking the first two terms of a series expansion around ω/Ω=0 yields, since ω1<<ΩX:

\({{\Omega_{X}^{App} \approx {\Omega_{X}\left( {1 + {\frac{1}{2}\frac{{\langle\omega_{1}\rangle}^{2}}{\Omega_{X}^{2}}}} \right)}} = {\Omega_{X} + \frac{{\langle\omega_{1}\rangle}^{2}}{2\; \Omega_{X}}}},\)

where the ratio <ω1>2/(2ΩX) gives the systematic error in rad/s. Typically, we may have an rf duty cycle τp/Δt=0.01=1% if τp=1 μs and Δt=100 μs for a spectral width of 10 kHz. If we consider an rf amplitude ω1/(2π)=2.5 kHz and coupling partners with offsets ΩX/(2π)>1 kHz (i.e., above 2 ppm at 500 MHz, or beyond 1 ppm at 1 GHz), we have systematic errors:

0<ω12/(4πΩX)<0.3125 Hz.  (3)

In other words, the apparent offset of the off-resonance spin X is barely perturbed. If desired, the apparent chemical shifts observed in tickling spectra may be corrected for these Bloch-Siegert effects:

ΩX≈ΩXApp/[1+ω12/(2ΩX2)]≈ΩXApp/[1+ω12/(2(ΩXApp)2)],  (4)

where we have simply replaced ΩX by ΩXApp on the right-hand side. The signals that appear in a symmetrical position with respect to the carrier frequency in FIG. 2 can be explained by the fact that the projection of the trajectory of the magnetization on the equatorial plane of the rotating frame is elliptical (in contrast to the circular trajectory that prevails in the absence of a tickling field) so that is can be decomposed into two counter-rotating components with unequal amplitudes. If Ω1>>ΩX, the evolution of the magnetization associated with both spins would be completely suppressed in the limit of continuous irradiation when ω1=ω1 (spin-locking), so that one expects a single unmodulated signal at ΩA=0 Hz. The top spectra in FIG. 2 approach this limiting case, where the two spins are in effect magnetically equivalent.

As can be seen in FIG. 3, which shows a partial enlargement of FIG. 2, an ideal decoupling effect is achieved for both resonances when the tickling pulse length is τp=1 μs. If the pulses have a decreasing duration τp each singlet appears to be flanked by two “tickling sidebands” with increasing amplitude. Note that the multiplet structures of both on- and off-resonance spins A and X remain remarkably similar for 0≦τp≦2.25 μs.

The role of the rf field strength was further investigated by simulations, as shown in FIG. 4. The tickling pulse length was kept fixed at τp=1 μs and offset ΩX/(2π)=1 kHz while the field strength was progressively increased in the range 0≦ω1/(2π)≦50 kHz. While the A spin resonance appears neatly decoupled regardless of the rf field strength, the off-resonance X spin shows a misleading splitting as the rf field strength is increased beyond 12 kHz. The distortion of the X spin resonance becomes worse as the rf field strength is increased.

However, as may be appreciated in the blown-up view of FIG. 5, the tickling sidebands are largely suppressed in the range 2<ω1/(2π)<4 kHz if τp=1 μs and ΩX/(2π)=1 kHz. The efficiency of decoupling also depends on the offset of spin X. Numerical simulations indicate that decoupling fails in strongly-coupled spin systems, i.e., if the chemical-shift difference is smaller than, say, 10 Hz.

FIG. 6 shows a set of tickling spectra for offsets 50<ΩX/(2π)<600 Hz with an rf field strength ω1/(2π)=2.5 kHz. A progressive improvement in decoupling, i.e., an increase of the intensity of the X signal is observed as the chemical shift difference is increased. The decoupling efficiency seems to be compromised when this difference is smaller than 100 Hz, i.e., smaller than 0.2 ppm at 500 MHz (11.7 T).

In FIG. 7 similar simulations are shown for a lower rf field strength ω1/(2π)=800 Hz, again with a 1% duty cycle. Although the intensities of the tickling sidebands are much larger than in FIG. 6, adequate decoupling can be achieved for offsets as small as 50 Hz, or 0.1 ppm at 500 MHz. Thus, paradoxically, weak rf tickling strengths are required to achieve efficient decoupling in strongly-coupled spin systems.

The decoupling effect of spin tickling can be rationalized in terms of Average Hamiltonian Theory.[21] Simulations performed with Mathematica[22] show that the decoupling effect is already observed when only the zeroth-order term of the Magnus expansion that describes the pulse sequence of FIG. 1 is considered. The matrix representation of this term in the product base of a two-spin system is:

\(\begin{matrix}
{{\overset{\_}{H}}^{(0)} = {\begin{pmatrix}
a & c & c & 0 \\
c & {- a} & {a - b} & c \\
c & {a - b} & b & c \\
0 & c & c & {- b}
\end{pmatrix}.}} & (5)
\end{matrix}\)

The off-diagonal elements c=ω1τp/(2Δt)=ω1/2 correspond to tickling pulses with phase x and are proportional to the duty cycle τp/Δt. The other elements a=(ΩX+πJ)/2 and b=(ΩX−πJ)/2 describe the offset and J-coupling interactions and do not depend on the duty cycle since the evolution under these interactions occurs both during the free precession intervals and during the tickling-pulses. The eigenvalues of this matrix represent the energy levels of the two-spin system when the expectation values of the spin operators are sampled stroboscopically with a period Δt.

The transition frequencies are given by differences of eigenvalues. In the absence of tickling pulses, the frequency difference Δv between the two single-quantum transitions associated with each spin amounts to the coupling constant JAX, i.e., Δv=2πJAX. Identifying values of c which lead to a frequency difference Δv(c)=0 amounts to finding the condition where the JAX-splitting collapses. Although the eigenvalues of (0) are rather involved, solving the equation Δv(c)=0 yields a compact result:

\(\begin{matrix}
{{\langle\omega_{1}\rangle} = {{\omega_{1}\frac{\tau_{p}}{\Delta \; t}} = {{\pm \pi}\; {J_{AX}.}}}} & (6)
\end{matrix}\)

Thus, for a given coupling constant JAX, it is possible to choose an average rf field strength <ω1>, i.e., a peak rf field strength wand a duration of the tickling pulses τp so that the splitting vanishes, provided the observation is periodic and occurs at intervals Δt. Equation 6 can be recast to give β=ω1τp=±πJAX Δt. Thus, the flip angle β of each tickling pulse must be equal to half the angle through which the single-quantum coherences of the two components of each doublet would evolve with respect to each other in the absence of any rf perturbation under the J-coupling interaction in the dwell time Δt.

FIG. 8 shows numerical calculations of the multiplet of the off-resonance spin X using the average Hamiltonian of Eq.5 starting with an initial density operator IxA+IxX. The tickling pulse length was τp=1 μs and the coupling constant JAX=10 Hz. When ω1/(2π)=0 Hz, an unperturbed doublet is observed (black dotted line). The multiplet obtained when the condition of Eq.6 is met with τp=1 μs, Δt=100 μs and ω1/(2π)=0.5 kHz, is shown by a broken line: a central peak with an intensity comparable to the peaks of the unperturbed spectrum appears at ΩX=1 kHz, albeit slightly displaced by a small Bloch-Siegert effect. In addition, two tickling sidebands with intensities that are about half of the singlet peak appear. When the rf amplitude is increased to Ω1/(2π)=1.0 kHz (shown by a continuous line) the tickling sidebands move away symmetrically from ΩX and lose intensity.

Although the condition Δv(c)=0 of Eq. 6 is violated by a factor of 2, the intensity of the central peak is enhanced. Thus, when the rf amplitude ω1 is increased, the splitting between the single-quantum transitions induced by a violation of Eq. 6 does not significantly broaden the central line, while the tickling sidebands are reduced. The integrals of all three spectra are conserved.

The requirement that the scalar coupling term in the average Hamiltonian of Eq. (1) be made ineffective (on the condition that the sampling be stroboscopic) implies that the degrees of freedom of the evolution of the density operator must be severely curtailed. In simple terms, if we start with in-phase terms such as IxA, IyA, IxX and IyX, efficient decoupling means that it should be made impossible to convert these initial states into anti-phase terms such 2IxAIzX, 2IyAIzX, 2IzAIxX and 2IzAIyX. It turns out that, if we start with IxA, and if the offset ΩA vanishes, coherence transfer is constrained to a Liouville subspace spanned by a triad of non-commuting operators {IxA, 2IyAIzX, 2IzAIzX}.

FIG. 9 shows a simulation of the time dependence of these three product operators and of their norm, defined as N=(IxA2+2IyAIzX2+2IzAIzX2)1/2 (continuous line) during a typical tickling experiment. Since the norm of these three operators is constant, coherence transfer must be confined to the subspace spanned by the triad of non-commuting operators. If we start with the in-phase term IxA, the J-coupling tends to convert it into an anti-phase operator 2IyAIzX, but this process is stopped by the transformation of 2IyAIzX into longitudinal two-spin order 2IzAIzX due to the tickling pulses. As a result, the oscillations of the in-phase term IxA are kept to a minimum. This amounts to successful decoupling. Similar phenomena were observed in a different context and dubbed “stabilization by interconversion within a triad of coherences under multiple refocusing pulses” (SITCOM).[23, 24] Of course, in the tickling experiments presented here, the brief pulses do not have any refocusing effect, but the stabilizing effect is similar.

Although the analogies may seem far-fetched, Fourier tickling achieves similar effects as repeated projective measurements, where the system is not confined to a single state, but evolves under the action of its Hamiltonian in a multidimensional subspace of Hilbert space. It may be helpful to ponder about possible variants in the light of these analogies.[26-30]

All the experiments were carried out in a static field B0=11.7 T (500 MHz for proton). At this field, the two protons of 2,3-dibromothiophene in DMSO-d6 are weakly coupled with (ΩA−ΩX)/(2π)˜305 Hz and JAX˜5.8 Hz.

In FIG. 10, the unperturbed spectrum is compared with the best tickling spectrum. The carrier frequency was set on the left-hand resonance, as indicated by a wavy arrow. Good decoupling and minimal interference of tickling-sidebands is obtained with a tickling field strength that was empirically optimized to ω1/(2π)˜900 Hz.

FIG. 11 shows spectra of the strongly-coupled AB system of 2,3,6-trichlorophenol superimposed with a solvent peak marked with an asterisk.

In contrast to the AX system of FIG. 10, some tickling sidebands are clearly visible in the strongly coupled AB system of FIG. 11. This undesirable effect was highlighted in the numerical simulations of FIG. 7.

Nevertheless, a reasonable decoupling efficiency is achieved. A lower rf-field amplitude must be used for smaller differences in chemical shifts. Tickling also works if the molecule comprises magnetically-equivalent spins, as in the A2M2X3 system ofpropan-1-ol (HOCH2CH2CH3).

The conventional spectrum and the tickling spectra with carrier frequencies set on one of the three multiplets are shown in FIG. 12. If the carrier frequency is set on the chemical shift of A2, the multiplicity of the coupling partner M2 is simplified by decoupling of the 3JAM, though the fine structure due to the 3JMX is not affected, as shown in the inset. If the carrier frequency is set on the chemical shift of X3, the multiplicity of the coupling partner M2 is simplified by decoupling of 3JXM but the fine structure (triplet) due to 3JAM remains, as shown in the inset of FIG. 12 c. Clearly tickling can decouple all J-interactions between the irradiated spin and its J-coupling partners. Obviously, tickling does not affect couplings between spins that are not irradiated. In FIG. 12 d, the carrier frequency was set on the M2 resonance of the A2M2X3 system. Since the M2 spins are coupled to both A2 and X3, while 3JAX=0, all three resonances appear decoupled in this case. These results show that the presence of magnetically-equivalent spins does not compromise the performance of tickling experiments. Furthermore, in all three samples considered, we did not observe any anomalies of the integrals in the tickling spectra.

It is well known that the effective frequency of the centreband of a comb C of pulses can be shifted at will from the carrier frequency vrf to v=vrf+φ/(2πΔt) by advancing the phase of the kth pulse of the comb C in the kth dwell time Δt through a shift kΔφ. Such phase modulation schemes have been used in conjunction with so-called ‘delays alternating with nutation for tailored excitation’ (DANTE).[31-34] Since the position within the interval Δt of the tickling pulses of duration τp belonging to any one comb C is immaterial, one can readily superimpose several combs Cm of tickling pulses with m=1, 2, . . . M, each of which may be associated with its own phase shift kΔφm and hence its own frequency shift. Each dwell time Δt does contain only one tickling pulse per comb. The tickling pulses within a dwell time Δt which belong to different combs Cm do not need to be equidistant. This allows one in effect to irradiate simultaneously at a manifold of frequencies, as shown in the simulations of FIG. 13.

The method is effective over a broad range of chemical shifts. Groups of magnetically equivalent spins as occur in methylene and methyl groups can be decoupled efficiently. A considerable gain in resolution and spectral simplification can thus be obtained without distortion of signal integrals. We believe that this new experimental tool can aid the characterization of complex systems, including biological macromolecules. By inserting a manifold of polychromatic tickling pulses in each Δt interval, several subsystems can be decoupled simultaneously.

The new tickling method allows one to avoid interferences and allows irradiation at multiple frequencies to decouple several interactions simultaneously.

