# DESCRIPTION

## BACKGROUND

Superconducting circuits are among the most promising of qubit technologies for scalable quantum computation due to their long coherence times, high gate fidelities, and processor size (i.e., the number of qubits that can be manipulated simultaneously).

## SUMMARY

Many prior-art superconducting quantum processors implement qubits as transmons, whose coherence times have improved by nearly an order of magnitude due to new methods that decrease the effects of environmental noise. One of the simplest of superconducting circuits, a transmon can be modeled as a weakly anharmonic oscillator whose energy states are joined via large transition dipole matrix elements. Transmons trade off decreased sensitivity to charge-induced-noise dephasing with increased sensitivity to decay.

Flux qubits, and in particular fluxonium, are promising types of superconducting circuits that offer many advantages over transmons. Some of the benefits of fluxonium include a rich energy-level structure, natural protection from charge-noise-induced relaxation and dephasing, and compatibility with circuit quantum electrodynamics (QED).

Fluxonium is created by shunting a flux qubit with a large inductance. Further shunting of the qubit with a large capacitance results in “heavy fluxonium”, which advantageously increases relaxation times. However, a challenge with using flux qubits in large-scale superconducting processors is that standard microwave control techniques result in slow gates that cannot complete before dephasing and relaxation take effect.

The present embodiments include fast methods for controlling superconducting qubits, and therefore may be used with superconducting quantum computers (e.g., those based on fluxonium qubits). Here, “fast” means that the methods complete in times much shorter than typical dephasing and relaxation times, and thus high fidelities (e.g., 99%) can be reliably achieved. Advantageously, these methods do not rely on a three-dimensional (3D) cavity for suppressing spontaneous emission, and therefore can be implemented using smaller two-dimensional (2D) architectures commonly used for superconducting circuits. The present embodiments include methods for initializing a superconducting qubit into a pure state (e.g., at the beginning of a quantum gate) and methods for reading-out the quantum state of the superconducting qubit (e.g., at the end of the quantum gate). Finally, the present embodiments also include methods based on fast pulses for arbitrarily rotating a single superconducting qubit into any quantum state, thereby providing universal single-qubit control.

Advantageously, the present embodiments can work when the energy spacing between the two quantum-computational states of the qubit is less than the equivalent mean thermal energy of a surrounding bath. Prior-art superconducting qubits are challenged by small energy spacings because the resulting thermal occupation of both quantum-computational states reduces fidelity. By overcoming the limitations of this thermal occupation, the present embodiments relieve the requirements for cryogenic cooling (i.e., the qubit does not need to be cooled to temperatures as low as those used in the prior art, while maintaining fidelity).

For clarity in the following discussion, examples are described with respect to fluxonium qubits. However, it should be appreciated that the present embodiments may be used with any kind of flux qubit, i.e., a “heavy” flux qubit, a “light” flux qubit, or any other type of qubit whose properties are controllable with an applied magnetic flux. Furthermore, the present embodiments may also be used with another type of qubit without departing from the scope hereof. For example, the present embodiments can be implemented with a charge qubit (e.g., a cooper pair box). The present embodiments can also be implemented with a qubit containing a voltage-controllable Josephson junction (e.g., a gatemon qubit, or flux-like qubits where the Josephson junction is voltage-controlled).

## DETAILED DESCRIPTION

FIG. 1 is a schematic diagram of a quantum system 100 in which a fluxonium qubit 120 is coupled, via a coupling capacitor 106, to a readout resonator 110. The fluxonium qubit 120 is an example of heavy fluxonium in which a small-area Josephson junction 122 with inductance LJ is shunted by a capacitor 124 with capacitance Cq. The fluxonium qubit 120 also includes a superinductor 126 formed from an array of large-area Josephson junctions that shunts the Josephson junction 122 with an inductance LJA. The superinductor 126 has a total Josephson energy EJA that is much larger than a total charging energy ECA of the superinductor 126 (i.e., EJA>>ECA) to ensure that charge dispersion for each junction of the superinductor 126 is small, and thus that the superinductor 126 serves only as an inductor.

A Hamiltonian Hf for the fluxonium qubit 120 is

\(\begin{matrix}
{{H_{f} = {{{- 4}E_{C}\frac{d^{2}}{d\varphi^{2}}} - {E_{J}{\cos\left( {\varphi - {2\pi\frac{\Phi_{ext}}{\Phi_{0}}}} \right)}} + {\frac{1}{2}E_{L}\varphi^{2}}}},} & (1)
\end{matrix}\)

where Φ is the phase across the Josephson junction 122, EC=e2/(2Cq) is the charging energy of the capacitor 124 (e being the charge of the electron), EJ=Φ02/(2LJ) is the Josephson energy of the Josephson junction 122, EL=Φ02/(2LJA) is the inductive energy of the superinductor 126, Φext is external magnetic flux 130 threading a loop 132 formed by the superinductor 126 and the Josephson junction 122, and Φ=h/(2e) is the superconducting magnetic flux quantum (h being Planck's constant).

The readout resonator 110 is represented in FIG. 1 as a readout inductor 112 that resonates with first and second readout capacitors 114 and 116. An inductance LR of the readout inductor 112, and a parallel capacitance CR of the readout capacitors 114, 116, are selected such that the readout resonator 110 has a resonant frequency that is high compared to a temperature of an environment in which the quantum system 100 is located and operates. For example, the quantum system 100 may be mounted inside of a cryostat that cools the quantum system 100 to a temperature less than 50 mK. At 10 mK, the peak of the blackbody spectrum occurs near 600 MHz (as estimated using Wien's displacement law). Accordingly, the resonant frequency of the readout resonator 110 should be made higher than this value (e.g., 5 GHz, or more) to minimize excitation of the readout resonator 110 by thermal background photons. At temperatures less than 10 mK, the resonant frequency of the readout resonator 110 may be reduced accordingly.

To measure a state of the fluxonium qubit 120, the readout resonator 110 may be probed (e.g., via two-tone spectroscopy) using a first microwave transmission line 140 coupled to the readout resonator 110 via an input capacitor 104, and with a second microwave transmission line 142 coupled to the readout resonator 110 via an output capacitor 102. Each of the microwave transmission lines 140 and 142 may be a coaxial transmission line, or a planar transmission line (e.g., microstrip) co-fabricated with the quantum system 100 on a common substrate. The quantum system 100 may be alternatively or additionally coupled to one or more other superconducting quantum components (e.g., one or more additional resonators 110, one or more additional fluxonium qubits 120, one or more other additional superconducting qubits of another type, etc.).

FIG. 2 is a plot showing potential energy 202 and wavefunctions 210, 212, 214, and 216 of the fluxonium qubit 120 as a function of the junction phase φ, when the loop 132 is threaded with externally generated magnetic flux 130 equal to one-half of the superconducting magnetic flux quantum (i.e., φext=φ0/2, also referred to as the “flux-frustration point”). The potential energy 202, corresponding to the second and third terms on the right-hand side of Eqn. 1, exhibit a pair of potential-energy wells near ±π. The fluxonium qubit 120 has a ground state |g with a ground-state wavefunction 210 and a ground-state energy Eg, a first excited state |e with a first excited-state wavefunction 212 and a first excited-state energy Ee, a second excited state |f with a second excited-state wavefunction 214 and a second excited-state energy Ef, and a third excited state |h with a third excited-state wavefunction 216 and a third excited-state energy Eh. Each of the states |g, |e, |f, and |h is an energy eigenstate of the Hamiltonian Hf of Eqn. 1.

Quantum computation with the fluxonium qubit 120 may be implemented with the ground state |g and the first excited state |e. These states are also referred to herein as the quantum-computational states |g and |e. Tunneling through a center peak 218 of the potential energy 202 removes a degeneracy between these two states, resulting in an energy spacing Δ1=Ee−Eg. In the example of FIG. 2, Δ1 is only 14 MHz, much less than the frequency of the environmental temperature. To achieve such a small value for Δ1 (i.e., weak tunneling through the center peak 218), the height of the center peak 218 can be made large by selecting the ratio EJ/EC to be greater than one. In the example of FIG. 2, EJ/EC≈7. However, the fluxonium qubit 120 can be configured with a ratio EJ/EC that is even larger, wherein Δ1 decreases accordingly. Alternatively, the fluxonium qubit 120 can be configured with a smaller ratio EJ/EC without departing from the scope hereof. Alternatively, the fluxonium qubit 120 can be configured with an additional Josephson junction that allows EJ/EC to be electronically controlled.

Associated with small values of Δ1 is a suppression of transitions between the states |g and |e. That is, the transition dipole between the states |g and |e is nearly zero. Accordingly, the first excited state |e is metastable, which can be seen in FIG. 1 by the fact that the overlap of the wavefunctions 210 and 212, when integrated over all values of φ, is small. Transitions between |e and |g are fluxon-like inter-well transitions. Accordingly, the first excited state |e is also referred to herein as the metastable fluxon state |e.

Each of the two potential-energy wells in FIG. 2 is deep enough to support an additional eigenstate, shown in FIG. 2 as the second and third excited states |f and |h. Transitions between the ground state |g and the third excited state |h are intra-well transitions that are plasmon-like. Transitions between the first excited state |e and the second excited state |f are also plasmon-like. Unlike the suppressed fluxon transitions between the states |g and |e, each of these plasmon-like transitions is strong, and thus can be readily driven via applied microwave fields. As shown in FIG. 2, an energy spacing Δ2=Ef−Ee between the second excited state |f and the first excited state |e is larger than Δ1. Similarly, an energy spacing Δ3×Eh−Ef between the third excited state |h and the second excited state |f is greater than Δ1 due to the increasing tunneling between these states near the top of the center peak 218. Nevertheless, Δ3 is still less than Δ2. In the example of FIG. 2, Δ2 is 2974 MHz and Δ3 is 194 MHz. Accordingly, the second excited state |f is also referred to herein as the first plasmon excited state |f, and the third excited state |h is also referred to herein as the second plasmon excited state |h.

FIG. 3 is an energy-level diagram of the quantum system 100 of FIG. 1. In FIG. 3, each energy eigenstate of the quantum system 100 is a composite (i.e., tensor product) of one of the energy eigenstates of the fluxonium qubit 120 (i.e., one of the states |g, |e, |f, and |h) and a quantum state of the resonator 110 characterized by a number of photons in the resonator 110. Accordingly, FIG. 3 shows a composite state |g0 in which the fluxonium qubit 120 is in the ground state |g and there are no photons in the resonator 110. Similarly, FIG. 3 shows a composite state |e0 in which the fluxonium qubit 120 is in the first excited state |e and there are no photons in the resonator 110. FIG. 3 also shows composite states |f0 and |h0, which may be interpreted similarly.

FIG. 3 also shows a composite state |e1 in which the fluxonium qubit 120 is in the first excited state |e and there is one photon in the resonator 110. The resonator 110 has a relatively low Q (e.g., less than 1000) and thus, when the quantum system 100 is in the state |e1, the resonator 110 will rapidly decay, emitting a spontaneous photon 306 that leaves the quantum system 100 in the state |e0. Note that the quantum system 100, when in the state |e1, is highly unlikely to decay to the state |g0 since such a decay involves a fluxon-like transition for the fluxonium qubit 120. As described above, such fluxon-like transitions are highly suppressed.

While FIG. 1 shows the fluxonium qubit 120 coupled to the readout resonator 110, the fluxonium qubit 120 may be alternatively coupled to another type of energy-dissipating device that couples the energy of the spontaneous photon 306 into a surrounding cold bath to reduce the entropy of the fluxonium qubit 120. Other examples of such energy dissipaters include 3D microwave cavities and microwave transmission lines.

FIG. 3 also illustrates a reset method for initializing the quantum system 100 into a pure state. Since the quantum system 100 resides in an environment whose temperature is large compared to Δ1, yet smaller than Δ2, the fluxonium qubit 120, when thermally equilibrated with environment, will be in a nearly evenly mixed state (i.e., a nearly even statistical ensemble of the pure states |g and |e). Advantageously, the reset method described here transfers the fluxonium qubit 120 from the mixed state into a pure state (i.e., either one of the states |g and |e) that can be subsequently controlled to prepare the fluxonium qubit 120, with high fidelity, in whatever state is needed (as based on the quantum algorithm or gate at hand). Thus, the reset method may be used as a first step for universal single-qubit control.

The initial mixed state of the fluxonium qubit 120 can be described as an ensemble whose density matrix operator has the form ρ=pq|gg|+pe|ee|, where pg is the fraction of the ensemble in the state |g and pe is the fraction of the ensemble in the state |e. Thus, the operator ρ has a g-term and an e-term. As shown in FIG. 3, the quantum system 100 may be driven with a first microwave field 302 that couples the states |g0 and |h0. For example, a frequency of the first microwave field 302 may be selected to be resonant with the transition between the states |g0 and |h0. The first microwave field 302 excites the fraction pg of the ensemble in the state |g to the state |h, while leaving the fraction pe of the ensemble in the state |e undisturbed.

Also shown in FIG. 3, the quantum system 100 may also be driven with a second microwave field 304 that couples the states |h0 and |e1. For example, a frequency of the first microwave field 302 may be selected to be resonant with the transition between the states |h0 and |e1. The microwave fields 302 and 304 may be applied simultaneously. The second microwave field 304 excites the fraction pg of the ensemble previously transferred to the state |h0 up to the state |e1. Once excited, the fraction rapidly decays into the |e0 state by emitting the spontaneous photon 306. After the decay, all the ensemble is in the |e state of the fluxonium qubit 120, and thus the quantum system 100 is in a pure state. A third microwave field 310 may be subsequently applied to transfer the quantum system 100 into the pure state |g0. For example, the third microwave field 310 may be a π pulse that coherently transfers the quantum system 100 from the pure state |e0 into the pure state |g0.

A first speed with which the first microwave field 302 excites the fraction pg from the state |g0 to the state |h0 depends on a first Rabi frequency that is equal to the product of an amplitude of the first microwave field 302 and a transition dipole moment between the states |g0 and |h0. Similarly, a second speed with which the second microwave field 304 excites the fraction pg from the state |h0 to the state let) depends on a second Rabi frequency that is equal to the product of an amplitude of the second microwave field 304 and a transition dipole moment between the states |h0 and |e1. Thus, the amplitudes of the microwave field 302, 304 may be chosen such that the fraction pg is excited to the state |e1, and subsequently decays to the state |e0, in a time that is short compared to both a relaxation time T1 and a dephasing time T2 of the fluxonium qubit 120 (see experimental demonstration below). By contrast, the reset method was experimentally demonstrated by applying the microwave fields 302 and 304 to the fluxonium qubit 120 for 15 μs, followed by a 10 μs waiting period (i.e., in the absence of the microwave fields 302 and 304) to allow the spontaneous photon 306 to be emitted. A π pulse was the applied, after which a fidelity of 99% was obtained (i.e., 99% of the ensemble was in the state |g0, with the remaining 1% of the ensemble in other states). The corresponding temperature of the fluxonium qubit 120 was only 0.145 mK, lower than the ambient temperature by a factor of 100. Since it is experimentally challenging to produce a perfectly pure state, the reset method is described herein as generating an “approximately” pure state.

It is assumed in the previous discussion that the loop 132 of the fluxonium qubit 120 is continuously threaded by the external magnetic flux 130 during the entire reset method (and subsequent π pulse, if included), as the external magnetic flux 130 is needed to generate the energy-level structure shown in FIG. 3. While the above discussion describes the reset method with respect to the fluxonium qubit 120, those trained in the art will recognize that the reset method can be applied to another type of qubit, provided that the qubit has, or includes, a similar energy-level structure to that shown in FIG. 3. Thus, the reset method is not limited to fluxonium qubits, but may be used with other types of flux qubits, other types of superconducting-circuit qubits (e.g., phase qubits), and even non-superconducting-circuit qubits (e.g., ions, atoms, nitrogen-vacancy centers, etc.). In some of these other types of qubits, one or more of the microwave fields 302, 304, and 308 may need to be replaced with an oscillating electromagnetic field in a different part of the electromagnetic spectrum (e.g., infrared, visible, ultraviolet, etc.).

FIG. 3 also illustrates a readout method for distinguishing between the quantum-computational states |g and |e of the fluxonium qubit 120. The fluxonium qubit 120, when coupled with the readout resonator 110, dispersively shifts the resonant frequency of the readout resonator 110 by an amount that depends on the state (i.e., |g or |e) of the fluxonium qubit 120. Thus, the fluxonium qubit 120 induces, in the readout resonator 110, a first dispersive frequency shift when in the |g state, and a second dispersive frequency shift when in the |e state. A differential shift, equal to the different between the first and second dispersive frequency shifts, increases as the energies of the states |g and |e approach that of the excited resonator 110 (i.e., as the energies of the states |g0 and |e0 increase toward the energy of the state |e1).

For the quantum system 100, the energy gap between each of the lower-energy states |g0 and |e0, and the excited state |e1 is so large that the differential shift is too small to discern between the states |g0 and |e0. To enhance the interaction with the readout resonator 110, a π pulse 308 may be applied between the states |e0 and |f0, as part of the readout method, to coherently transfer the population of the state |e0 into the state |f0. The goal of discerning between the states |g0 and |e0 is now implemented by discerning between the states |g0 and |f0. Since the energy of the state |f0 is closer to that of the excited state |e1, the second dispersive frequency shift increases. This, in turn, increases the differential shift, making it easier to discern between the states |g0 and |f0 using dispersive readout via the readout resonator 110. The π pulse 308 may be alternatively configured to coherently transfer the population in the state |g0 state to the state |h0, wherein the readout resonator 110 is used to discern between the states |e0 and |h0.

One advantage of the readout method described above is that quantum computation is performed in the states |g0 and |e0, which benefits from the large detunings to the lowest excited states of the resonator 110. Thus, during quantum computation, heating of the fluxonium qubit 120 due to coupling with the resonator 110 is minimized, helping to preserve the long relaxation and dephasing times.

It is assumed in the previous discussion that the loop 132 of the fluxonium qubit 120 is continuously threaded by the external magnetic flux 130 during the entire readout method, as the external magnetic flux 130 is used to generate the energy-level structure shown in FIG. 3. However, the external magnetic flux 130 may be changed during the readout method. For example, a first magnetic flux 130 may be applied prior to and/or during the π pulse 308. Afterwards, a second magnetic flux 130 (with a magnitude different than that of the first magnetic flux 130) may be applied during sequent dispersive readout via the readout resonator 110.

While the above discussion describes the readout method with respect to the fluxonium qubit 120, those trained in the art will recognize that the readout method can be applied to another type of qubit, provided that the qubit has, or includes, a similar energy-level structure to that shown in FIG. 3. Thus, the reset method is not limited to fluxonium qubits, but may be used with other types of flux qubits, other types of superconducting-circuit qubits (e.g., phase qubits), and even non-superconducting-circuit qubits (e.g., ions, atoms, nitrogen-vacancy centers, etc.). In some of these other types of qubits, one or more of the microwave fields 302, 304, and 308 may need to be replaced with an oscillating electromagnetic field in a different part of the electromagnetic spectrum (e.g., infrared, visible, ultraviolet, etc.).

FIG. 4 is a plot of magnetic flux (I) as a function of time, illustrating a fast magnetic pulse 402 for single-qubit rotation of the fluxonium qubit 120. The fluxonium qubit 120 may begin (i.e., before an initial time t1) in any qubit state, i.e., any linear combination of the quantum-computational states |g and |e. The fluxonium qubit 112 is continuously threaded with externally generated magnetic flux 130 at a nominal value. Starting at the initial time t1, and lasting until a second time t2=t1+Δt, the pulse 402 is applied to the fluxonium qubit 120 by deviating the magnetic flux Φ away from the nominal value. In the example of FIG. 4, the magnetic flux Φ is increased above the nominal value by a pulse amplitude A. The value Δt is a pulse duration of the pulse 402. While FIG. 4 shows the magnetic flux Φ returning to the same nominal value after the pulse 402 (i.e., starting at time t2), the magnetic flux Φ may return to a different nominal value than that before the pulse 402 (i.e., prior to time t1).

The magnetic pulse 402 is “fast” in the sense that the pulse duration Δt is much less than the Larmor period (i.e., the inverse of the Larmor frequency ωq) of the fluxonium qubit 120. The Larmor frequency ωq is given by the energy splitting of the states |g and |e when the magnetic flux Φ is at the nominal value Φ0/2. In the experimental results presented below, ωq=14 MHz, corresponding to a Larmor period of 71 ns. A pulse duration Δt of approximately 2 ns was successfully demonstrated, more than an order of magnitude less than the Larmor period. In one embodiment, the pulse duration Δt is less than one-fourth of the Larmor period.

Representing the qubit state as a Bloch vector on the Bloch sphere, the pulse 402 rotates the Bloch vector by an angle θ about the x axis of the Bloch sphere (see FIG. 11D). Due to the finite value of the pulse duration Δt, the pulse 402 also rotates the Bloch vector about the z axis of the Bloch sphere, albeit at a slower rate than rotation about the x axis. The symbol Δ denotes the ratio of the rotation rate about the z axis to the rotation rate about the x axis, where only λ≤1 is considered herein. Thus, the pulse 402 rotates the Bloch vector about the z axis by λ|θ|, which is less than the angle θ by the factor λ. To minimize the rotation of the Bloch vector about the z axis, the pulse duration Δt should be made as short as possible.

At the nominal value Φ0/2, the quantum-computational states |g and |e are separated by a nominal energy splitting ΔE that is equal to the Larmor frequency of the fluxonium qubit 120. As the magnetic flux Φ deviates from the nominal value Φ0/2, the pulse 402 effectively acts as a transverse magnetic field that couples the states |g and |e, thereby increasing their energy splitting as the instantaneous flux Φ increasingly deviates away from the nominal value Φ0/2 (see FIG. 11B). The energy splitting will achieve a maximum energy splitting at the peak of the pulse 402. In one embodiment, the amplitude A is selected such that the maximum energy splitting is at least twice the nominal energy splitting.

While FIG. 4 shows the magnetic flux having a nominal value of approximately Φ0/2, the nominal value may be different than Φ0/2. In fact, FIG. 9A shows that the relaxation time T1 of the fluxonium qubit 120 is smallest for magnetic fluxes near Φ0/2. Accordingly, it may be advantageous to operate at magnetic fluxes away from Φ0/2. Operation at a magnetic flux away from Φ0/2 will decrease the dephasing time T2, which is largest at Φ0/2 (see FIG. 9B). However, the increase in T1 may be greater than the reduction in T2, giving rise to an optimal magnetic flux at which the coherence properties of the fluxonium qubit 120 are overall maximized.

While FIG. 4 shows the pulse 402 as being triangular with matched rising and falling edges (i.e., the slope of the rising edge equals the negative of the slope of the falling edge). However, the pulse 402 may have any other shape without departing from the scope hereof. For example, the pulse 402 may have a “simple” shape that monotonically deviates away from the nominal value Φ0/2 to a maximum deviation (either greater than or less than the nominal value), and then monotonically deviates from the maximum deviation back toward from the nominal value Φ0/2. The triangular pulse 402 shown in FIG. 4 is one example of a simple pulse shape that has no plateau (i.e., the pulse 402 does not “dwell” at any value of the flux). However, the pulse 402 may alternatively include one or more plateaus. The pulse may deviate linearly (e.g., rectangular, trapezoidal, triangular with unmatched rising and falling edges, etc.) or nonlinearly (e.g., Gaussian, Lorentzian, etc.). Alternatively, the pulse 402 may have a “complex” shape that changes slope any number of times, with or without one or more plateaus, before returning to the nominal value Φ0/2. For example, the pulse 402 may also cross the nominal value Φ0/2 one or more times before returning to the nominal value Φ0/2.

The pulse 402 can be advantageously generated using a commercial high-speed digital-to-analog converter (DAC), which is simpler to implement and requires fewer components than prior-art techniques in which superconducting-qubit control signals are generated by mixing an envelope function (e.g., as generated by an arbitrary waveform generator) with a high-frequency carrier. To increase stability, a DC power supply can be used to continuously output a DC current that generates the magnetic flux 130 at the nominal value. The DAC output may then be AC-coupled to the DC current such that the pulses 402 deviate the magnetic flux from the nominal value. Commercial DACs operate at speeds greater than 10 Gbps, and therefore can achieve pulse durations Δt less than 1 ns.

FIG. 5 is a plot of magnetic flux Φ as a function of time, illustrating a magnetic-pulse sequence 500 for universal single-qubit rotation of the fluxonium qubit 120. The magnetic-pulse sequence 500 uses two of the fast pulses 402 shown in FIG. 4. The fluxonium qubit 120 may begin in any qubit state, i.e., any linear combination of the quantum-computational states |g and |e. Before an initial time t1, the fluxonium qubit 120 is threaded with externally generated magnetic flux 130 at a nominal value. Starting at the initial time t1, and lasting until a second time t2=t1+Δt1, a first pulse 402(1) is applied to the fluxonium qubit 120 by deviating the magnetic flux 130 in a first direction away from the nominal value. In the example of FIG. 5, the magnetic flux Φ is increased above the nominal value Φ0/2 by a first pulse amplitude A1. The value Δt1 is a first pulse duration of the first pulse 402(1).

Starting at the second time t2, and lasting until a third time t3=t2+Δt1, the fluxonium qubit 120 idles with the magnetic flux Φ at the nominal value Φ0/2 for an idling time Δt1. Idling rotates the Bloch vector by a second angle θ2=Δt1/ωq about the z axis of the Bloch sphere. The second angle θ2 can be controlled by extending and/or shortening the idling time Δt1.

Starting at the third time t3, and lasting until a fourth time t4=t3+Δt2, a second pulse 402(2) is applied by to the fluxonium qubit 120 by deviating the magnetic flux 130 in a second direction, opposite the first direction, away from the nominal value Φ0/2. In the example of FIG. 5, the magnetic flux t is decreased below the nominal value Φ0/2 by a second pulse amplitude A2. The value Δt2 is a second pulse duration of the second pulse 402(2). The second pulse 402(2) rotates the Bloch vector by the negative of the first angle (i.e., −θ1) about the x axis of the Bloch sphere. Similar to the first pulse 402(1), the second pulse 402(2) also rotates the Bloch vector about the z axis of the Bloch sphere, due to the finite duration Δt2, by λ|θ1|. Note that the absolute value of θ1 arises from the always-on rotation about the z axis.

The pulse amplitudes A1, A2 and pulse durations Δt1, Δt2, may be selected such that a first area of the first pulse 402(1) and a second area of the second pulse 402(2) sum to zero, wherein the magnetic-pulse sequence 500 is a zero-area pulse sequence. Here, the first and second areas are measured relative to the nominal value Φ0/2. Thus, in FIG. 5, the first pulse 402(1) has a positive area, and the second pulse 402(2) has a negative area. In one embodiment, A1=−A2 and Δt1=Δt2, as shown in FIG. 5. However, the pulse amplitudes A1, A2 and pulse durations Δt1, Δt2 may have other values such that the first and second pulse areas sum to zero.

It may be beneficial to configure each pulse 402 to minimize high-order harmonics (i.e., Fourier components of the sequence 500) that can inadvertently affect the behavior of the fluxonium qubit 120. To create “sharp” pulses 402, Fourier components will be needed at frequencies above 1/Δts, where Δts=Δt1+Δt1+Δt2 is a duration of the sequence 500. However, at frequencies far above 1/Δts (e.g., ten times larger, or more), the amplitudes of the Fourier components may need to be attenuated. For this reason, triangular pulses 402 may be preferable to rectangular pulses 402 since the Fourier spectrum of a triangular pulse train decreases faster with increasing frequency than that of a rectangular pulse train.

As described in more detail below, values for each of the angles θ1 and θ2 may be selected, based on a given value of λ, such that the magnetic-pulse sequence 500 (i.e., the combined sequential effects of the first pulse 402(1), the idling, and the second pulse 402(2)) rotates the Bloch vector about they axis of the Bloch sphere by 90°. In this case, the magnetic-pulse sequence 500 can transform the fluxonium qubit 120 from one of the pure states |g and |e into an equal superposition of the states |g and |e (and vice versa). This version of the magnetic-pulse sequence 500 is functionally similar to a π/2 pulse, but can advantageously complete in a faster time. Accordingly, this version of the magnetic-pulse sequence 500 can replace any π/2 pulse used in any quantum gate or quantum-computation algorithm.

Also described below, values for each of the angles θ1 and θ2 may also be selected, based on a given value of λ, such that the magnetic-pulse sequence 500 rotates the Bloch vector about the y axis of the Bloch sphere by 180°. In this case, the magnetic-pulse sequence 500 can coherently transfer the fluxonium qubit 120 between the states |g and |e. This version of the magnetic-pulse sequence 500 is functionally similar to a π pulse, but can advantageously complete in a faster time. Accordingly, this version of the magnetic-pulse sequence 500 can replace any π pulse used in any quantum gate or quantum-computation algorithm (e.g., the π pulse 308, or the π pulse 310).

While FIG. 5 shows the first and second pulses 402(1), 402(2) as triangular, one or both of the first and second pulses 402(1), 402(2) may alternatively have a different shape without departing from the scope hereof. For example, one or both of the first and second pulses 402(1), 402(2) may have a simple pulse shape (e.g., rectangular, trapezoidal, Gaussian, etc.) or a complex pulse shape, as described above for FIG. 4.

While FIG. 5 shows the each of the pulse durations Δt1, Δt2 as being less than the idling time t1, one or both of the pulse durations Δt1, Δt2 may alternatively be greater than the idling time t1. For example, each of the pulse durations Δt1, Δt1 may equal twice the idling time t1, as may occur when each of the first and second pulses 402(1), 402(2) is rectangular. In some embodiments, there is no idling between the first and second pulses 402(1), 402(2), i.e., the second pulse 402(2) begins when the first pulse 402(1) ends, or t1=0.

In one embodiment, the magnetic-pulse sequence 500 is applied twice to the fluxonium qubit 120 to rotate the Bloch vector by an arbitrary angle ϕ about the x axis of the Bloch sphere. In a first sequence 500, the angles θ1 and θ2 are selected such that the first sequence 500 rotates the Bloch vector by −90° rotation about the y axis of the Bloch sphere. After the first sequence 500, the magnetic flux idles at the nominal value (e.g., Φ0/2), which rotates the Bloch vector by the arbitrary angle ϕ about the z axis of the Bloch sphere. After the idling, a second sequence 500 rotates the Bloch vector by +90° about the y axis of the Bloch sphere.

FIG. 6 shows one example of a complex pulse that crosses the nominal flux several times. This pulse rotates the fluxonium qubit 120 but without idling. Accordingly, in an embodiment, the magnetic-pulse sequence 500 is a complex pulse that crosses the nominal flux one or more times, with or without idling.

In some embodiments, a method for manipulating a fluxonium qubit state includes applying a flux pulse (e.g., the pulse 402 of FIG. 4) to the fluxonium (e.g., the fluxonium qubit 120 of FIG. 1). The fluxonium may be biased at or near a flux of one-half the superconducting magnetic flux quantum Φ0, i.e., Φ0/2. Alternatively, the fluxonium may be biased away from Φ0/2. Said manipulating may occur in less than N periods of the Larmor oscillation (e.g., N=2 periods or N=10 periods). The flux pulse may include any one or more of the following properties: (1) starts and stops at the same flux (which gives composability); (2) has a net zero area (cuts of sensitivity to low frequency line filtering, etc.); (3) first- and/or second-order order insensitivity to low-frequency flux noise; (4) first- and/or second-order insensitivity to small changes of tunnel splitting; (5) first- and/or second-order insensitivity to small changes in the flux bias; (6) is filtered and/or generated with limited power contained in high frequencies for a given length of pulse (makes it easier to calibrate lines); (7) is filtered and/or generated with little power at frequencies near other transitions in the fluxonium (i.e., no leakage).

In some embodiments, a measurement method for determining a fluxonium qubit state may operate in a z basis (i.e., symmetric/anti-symmetric), wherein the fluxonium is biased at or near a flux of one-half the superconducting magnetic flux quantum Φ0 (i.e., Φ0/2). Alternatively, the measurement method may operate in or an x basis (which well), wherein the fluxonium is biased away from Φ0/2. In either case, the method includes performing a quantum non-demolition (QND) measurement on the fluxonium qubit state in the corresponding basis. A duration of the QND measurement may be shorter than the coherence time of the fluxonium. The QND measurement may also be “latching”, i.e., is robust against qubit state changes during the measurement. When the QND measurement is latching, the duration of the QND measurement may be longer than the qubit coherence time.

The measurement method may use dispersive coupling of a fluxon state of the fluxonium to a structured radiation environment (e.g., a resonator, filter, cavity, etc.). In this case, active pulses may be used to probe the state-dependent change of the structured radiation environment. The measurement method may use shaped pulses. The measurement method may also use dispersive coupling of a plasmon state of the fluxonium to the structured radiation environment using one or more of the following: (1) direct occupation of the plasmon state; (2) virtual coupling to the plasmon state; (3) one or more active pulses to probe the state-dependent change of the structured radiation environment; (4) emission of energy of the plasmon state into a measurement apparatus; (5) one or more active pulses to probe the qubit state-dependence of plasmons; and (6) one or more shaped pulses. In some embodiments, a measurement method includes the manipulation method described above.

In some embodiments, an initialization method for cooling a fluxonium to a known state may use plasmons. For example, the initialization method may use one or more of plasmon dissipation, direct excitation of plasmons, and virtual excitation of plasmons to mediate coupling to a cold bath. The initialization method may also use radiative cooling. For example, the initialization method may implement radiative cooling using one or more of a transmission line, a structured radiation environment (e.g., a resonator, a bandpass filter, a high pass filter, a low-pass filter, etc.). Alternatively, the initialization method may use a combination of plasmons radiative cooling. The fluxonium (or another type of superconducting qubit) has a transition energy between its quantum-computational states that is small enough such that there is a significant equilibrium population of each of the quantum-computation states (i.e., hω<kBT, where ℏ is Planck's constant divided by 2π, kB is Boltzmann's constant, ω is the angular frequency corresponding to the transition energy, and T is the temperature of the environment). In one embodiment, hω<5kBT. In another embodiment, hω≤kBT.

In some embodiments, the initialization method uses the manipulation method(s) described above. In some embodiments, the initialization method uses the manipulation method(s) as well as the measurement method(s) described above.

In some embodiments, the measurement method is combined with the initialization method (e.g., the initialization method may be performed prior to the measurement method). Similarly, the initialization method may be combined with one or both of the measurement method and the manipulation method.

### Experimental Demonstration

Introduction

Superconducting circuits are among the fastest developing candidates for quantum computers due to steady improvements in coherence times, gate fidelities, and processor size. These developments have ushered the noisy intermediate-scale quantum era and demonstrations of quantum advantage over classical computing. Many superconducting quantum processors are based on the transmon circuit, which since its inception has seen improvements in coherence by nearly 4-5 orders of magnitude driven largely by decreasing environmental noise. While the transmon circuit has seen widespread use in quantum computation, fluxonium offers many advantages over earlier flux qubits, including a rich level structure, natural protection from charge-noise induced relaxation and dephasing, and reduced sensitivity to flux noise. One of the challenges in making fluxonium a building block for superconducting qubit processors arises from the slow gates using standard microwave control.

In this section, we demonstrate high-fidelity control of a fluxonium circuit using a universal set of single-cycle flux gates on a qubit whose frequency is an order of magnitude lower than the ambient temperature. In the process, we reimagine all aspects of how the circuit should be controlled and operated, and demonstrate coherence times and gate fidelities that match or exceed those of the best transmon circuits, with the potential for further improvements.

The transmon is one of the simplest in the family of superconducting circuits, realizing a weakly anharmonic oscillator with large dipole matrix elements. This circuit trades off increased sensitivity to decay, and a reduced anharmonicity for decreased sensitivity to charge-noise-induced dephasing. Despite the maximal susceptibility to relaxation, state-of-the-art transmons have relaxation (T1) times around 100 μs, corresponding to Qs of a few million. The gate speeds are, however, limited by the small anharmonicity, typically ˜5% of the qubit frequency ωq, resulting in a theoretical upper bound of ˜ωq/(Qα)˜10−5 and state-of-the-art values of ≲1-2×10−4 for the gate infidelity. This suggests that gate fidelities can be made to approach 1/Q by increasing the anharmonicity in comparison to the qubit frequency ωq, and performing gate operations within a few Larmor periods.

The flux qubit, another member of the superconducting circuit family, already has the desired level structure with a relative anharmonicity α/ωq>>1. The extreme sensitivity to flux noise of these qubits was mitigated by shunting the Josephson junction with a large superinductor, resulting in the development of the fluxonium. Further improvements in energy relaxation times were obtained by the realization of a heavy fluxonium, which additionally reduced the decay matrix elements using a large shunting capacitor. These variants of fluxonium are reported to have longer coherence times than transmons in 3D architectures. Even though heavy fluxonium has the desired level structure and large coherence times, fast manipulation of the metastable qubit states remains a challenge due to the suppressed charge matrix elements. While Raman transitions can be used for coherent operations, these protocols are still relatively slow and require high drive powers, while exposing the qubit to the higher loss rates of excited fluxonium levels involved during the gate.

In this work, we realize a heavy-fluxonium circuit in a 2D architecture with coherence times T1, T2e˜300 μs exceeding those of standard transmons. The frequency of the qubit transition is only 14 MHz, an order of magnitude lower than the temperature of the surrounding bath. Therefore, to initialize the qubit we develop and realize a reset protocol that utilizes the readout resonator and higher circuit levels to initialize the qubit with 97% fidelity, effectively cooling the qubit down to 190 μK. Lastly, we use flux pulses to realize high-fidelity single-qubit gates within a single period 2π/ωq of the Larmor oscillation.

The Heavy-Fluxonium Circuit

The circuit consists of a small-area Josephson junction (JJ) with inductance LJ shunted by a large inductance (LJA), and a large capacitor (Cq), as shown in FIG. 7A. The shunting inductance is realized by an array of 300 large-area JJs, each having a Josephson energy EJA and charging energy ECA. We make EJA/ECA>>1 to ensure that the charge dispersion for each array junctions is small, and the array can be regarded as a linear inductor. The corresponding effective circuit is shown in FIG. 7B, and the resulting Hamiltonian is given by Eqn. 1. The corresponding values for the reported device are: EC/h=0.479 GHz, EL/h=0.132 GHz, and EJ/h=3.395 GHz, where h is Planck's constant. The level structure of the fluxonium at the flux-frustration point (Φext=Φ0/2) is shown in FIG. 7C. There are two types of transitions of interest, the intra-well plasmons (|g↔h and |e↔|f) and the inter-well fluxons (|g↔|e and |f↔|h). The single-photon transitions |g↔|f and |e↔|h are forbidden at the flux-frustration point due to the parity selection rule. The qubit is comprised of the lowest two energy levels |gand |e, with the qubit transition being fluxon like, with a frequency ωq of 14 MHz.

Qubit Initialization and Readout

Due to its low transition frequency, the qubit starts in a nearly evenly-mixed state in thermal equilibrium. We first initialize the qubit in a pure state (|g or |e) using the reset protocol shown in FIG. 8A. In this protocol, we simultaneously drive both the |g0→|h0 and |h0→|e1 transitions for 15 μs. The high resonator frequency (5.7 GHz) in comparison to the physical temperature, and the low resonator quality factor Q=600 result in the rapid loss of a photon from |e1, effectively removing the entropy from the qubit. In conjunction with the large matrix element between |h0 and |e1, this steers the system into a steady state with over 95% of the population settling in |e0 in 5 μs. We subsequently perform an additional π pulse on the |g-|e transition to initialize the system in the ground state (|g0). The reset is characterized by performing a Rabi rotation between the |e ↔|f levels, as shown in FIG. 2(b). The Rabi contrast is doubled following reset, consistent with 50% of the population being in |e in thermal equilibrium. If we prepare the system in |g, the |e χ|f Rabi contrast indicates a 3±2% error in state preparation, depending on the |f state thermal population. Since the |f frequency is similar to the typical transmon frequencies, its thermal population is in line with that of most transmons. The effective qubit temperature following reset is ˜190 μK, lower than the ambient temperature by a factor of 100.

Readout of the fluxonium levels is performed using circuit quantum electrodynamics by capacitively coupling the fluxonium circuit to a readout resonator. Since the qubit states are far away in frequency from the readout resonator, the dispersive shift x of the resonator due to a change in the occupation of computational states is small (60 kHz). While the large detuning reduces the qubit heating through the resonator, it makes direct dispersive readout challenging. We circumvent this issue by utilizing the larger dispersive interactions χf, χh of the excited levels |f, |h, which are closer in frequency to the readout resonator. To improve readout fidelity, we thus perform a π pulse on the |e-|f transition in 80 ns, before standard dispersive readout. Since the population in |e is transferred to |f, the readout signal becomes proportional to (χf-χg), which is five times larger than (χe-χg). This plasmon-assisted readout scheme results in 50% single-shot readout fidelity, which can be further improved with a parametric amplifier, and by optimizing the resonator K and the dispersive shifts.

Characterizing Device Coherence

Having developed protocols for initialization and readout, we characterize the coherence properties of the qubit. The inset of FIG. 9A shows a T1=315±10 pts measured at the flux-frustration point following initialization of the qubit in either the |g or |e state. The qubit relaxes to a near equal mixture where the excited state population P(|e)=0.4955±0.0015, with the deviation providing an estimate of the temperature of the surrounding bath, T=42±14 mK. At the flux-frustration point, the wavefunctions are delocalized into symmetric and anti-symmetric combinations of the states in each well. As we move away from this degeneracy point, the wavefunctions localize into different wells resulting in a suppression of tunneling and an increase in the relaxation times, see FIG. 9A. Here, the qubit relaxation times were measured over a wide range of external flux by driving the |g-|h transition for 120 μs to pump the qubit into the |e state, and monitoring the subsequent decay. While moving away from the flux-frustration point, T1 increases to a maximum value of 4.3±0.2 ms, consistent with previous heavy-fluxonium devices, before subsequently decreasing.

To explain the measured relaxation times, we consider several avenues by which the qubit can decay, including Purcell loss, decay via charge and flux coupling to the control lines, 1/f flux noise, dielectric loss in the capacitor, and resistive loss in the superinductor. Conservative estimates of the flux noise induced loss are lower than the measured loss by nearly an order of magnitude. The loss near the flux-frustration point is believed to be largely due to dielectric loss in the capacitor. This can be thought of as Johnson-Nyquist current noise from the resistive part of the shunting capacitor, which couples to the phase matrix element g|{circumflex over (φ)}|e, and grows rapidly as we approach the flux-frustration point. Assuming a fixed loss tangent for the capacitor, this loss rate is inversely proportional to the impedance of the capacitor, and is given by:

\(\begin{matrix}
{\Gamma_{diel} = {\frac{\hslash\omega_{q}^{2}}{8E_{C}Q_{cap}}{\coth\left( \frac{{\hslash\omega}_{q}}{2k_{B}T} \right)}{{❘\left\langle {g{❘\hat{\phi}❘}e} \right\rangle ❘}^{2}.}}} & (2)
\end{matrix}\)

The T1 at the flux-frustration spot sets an upper bound of 1/Qcap=8×10−6 for the loss tangent of the capacitor, which is within a factor of three of the value reported in previous heavy-fluxonium devices, and results in the dashed curve in FIG. 9A. Since ωq is below the ambient temperature near the flux-frustration point, a combination of the temperature-dependent prefactor ˜2kBT/(ℏωq), and the relation between charge and phase matrix elements in fluxonium, g|{circumflex over (n)}|e=ω/(8Ec)g|{circumflex over (ϕ)}|e, results in the dielectric-loss scaling as 1/ω, which is consistent with the observed trend in the T1 near the flux-frustration point. The measured T1 at the flux-frustration point also sets an upper bound of 5×10−9 for the loss tangent of the inductor. The decay from inductive loss, however, increases more rapidly with frequency than dielectric loss (∝1/ω3) and is inconsistent with measured data. Our qubit operations are performed between 0.4Φ0-0.5Φ0 where the T1 is mainly limited by dielectric loss. As we move further away from the flux-frustration point (˜0.4Φ0), T1 starts to decrease. This additional loss is believed to be due to a combination of radiative loss to the charge drive line, and Purcell loss from higher fluxonium levels excited by heating from the |g and |e states. The Purcell loss calculated based on the coupled fluxonium-resonator system using a bath temperature of 60 mK results in the dotted blue curve shown in FIG. 9A. The enhanced loss near Φext=0.35Φ0 is suggestive that heating to higher levels may contribute as there are several near resonances of higher fluxonium levels with the readout resonator, which depend sensitively on the circuit parameters.

The dephasing is characterized using a Ramsey sequence with three echo π pulses, and found to be minimized at Φext=Φ0/2, where the qubit frequency is first-order insensitive to changes in flux. The dephasing rate near the flux-frustration point can be separated into two parts. The first is a frequency-independent term ΓC mainly composed of qubit depolarization, and dephasing from cavity photon shot noise and other flux insensitive white noise sources. The second arises from 1/f flux noise that is proportional to the flux slope as

\({\Gamma_{1/f} = {\frac{d\omega}{d\phi}\eta\sqrt{W}}},\)

where η is in the flux-noise amplitude and W depends on the number of π pulses in an echo experiment (W=4 ln 2−9/4 ln 3 for three π pulses). Thus, our spin-echo signal decays as exp(−t/TC)×exp(−Γ1/f2t2). Here TC=1/ΓC is the T2e value at the flux-frustration point. It is found to be ˜300 μs, much higher than the T2e values for state-of-the-art transmons, see inset of FIG. 9B. The T2e values around the flux-frustration point, defined as the time for the echo oscillation amplitude to decay to 1/e are shown in FIG. 9B. This value falls off rapidly as we move away from the flux-frustration point, consistent with the small tunnel coupling between levels. Away from the flux-frustration point, T2e is mainly limited by 1/f flux noise. The T2e far from the frustration point is projected to be ˜10 μs according to our model, which is consistent with other reported results.

Fast Single-Cycle Flux Gates

To maximize the advantage of the large anharmonicity of heavy fluxonium, we rethink the standard microwave-drive control of the circuit which is hindered by the suppressed charge matrix elements. We instead perform high-fidelity gates through fast flux pulses, similar to the control scheme used in the original charge qubit. Near the flux-frustration point where the fluxonium is operated, the Hamiltonian within the computational space can be idealized as a spin-½ system,

\(\frac{H}{h} = {{\frac{A\left( \Phi_{ext} \right)}{2}\sigma_{x}} + {\frac{\Delta}{2}{\sigma_{z}.}}}\)

Here Δ≈14 MHz is the splitting of |g and |e at the flux-frustration point, and corresponds to the qubit frequency ωq. The amplitude of the σx term is proportional to the flux offset δΦext from the flux-frustration point, and given by A=4πg|{circumflex over (φ)}|eELδΦext/h. The coefficient of the σx term can be much larger than the qubit frequency, with A˜300 MHz when δΦext=0.06Φ0, disallowing any rotating wave approximation.

FIG. 10A shows the protocol for a generic qubit pulse. We first rapidly move the flux-bias point away from the flux-frustration point in one direction and back, thus generating a rotation about the x axis through a large σx term in our computational basis. There is additionally a relatively small rotation about the z axis corresponding to the time Δtp of the triangular spike. We subsequently idle at the flux-frustration point for a duration Δtz, which results in a rotation by ωqΔtz about the z axis. Finally, we rapidly move the flux-bias point in the other direction and back, resulting in a −σx term and another small z rotation. We choose the two spikes to be exactly anti-symmetric, ensuring zero net flux, simultaneously minimizing the effect of microsecond and millisecond pulse distortions ubiquitous in flux-bias lines, and echoing out low-frequency noise. The pulse is also immune to shape distortions since the total σx and σz amplitudes depend only on the area of the spike and Δtz. By sweeping the amplitude A of the triangular spike and idling length Δtz of the pulse, and measuring the expectation value of the spin along each axis, we obtain the 2D Rabi patterns shown in FIG. 10C that provide a measure of our gate parameters. A vertical line cut of these graphs corresponds to Larmor precession in the lab frame, with an oscillation frequency of Δ=14 MHz. We thus obtain a Z/2 gate by idling at the flux-frustration point for Δtz=1/(4Δ). We obtain a Y/2 gate at the point indicated by a star 1002, with the corresponding trajectories on the Bloch sphere for three different cardinal states shown in FIG. 10D. Y/2 and arbitrary rotations about the z axis are sufficient for universal control. An X/2 gate, for instance, is performed through the combination (−Y/2)·(Z/2)·(Y/2).

We characterized the fidelities of our single-qubit gates through randomized benchmarking (RB) and interleaved RB (IRB). RB provides a measure of the average fidelity of single-qubit Clifford gates and is performed by applying sequences containing varying number of Clifford gates on the state |e. For a given sequence length, we performed 75 randomized sequences, each containing a recovery gate to the state |e before the final measurement. IRB allowed us to isolate the fidelities of individual computational gates and was performed by interleaving the gate between the random Clifford gates of the RB sequence. The averaged decay curves of P(|e) as a function of the sequence length for standard RB (black circles), and IRB for Z/2 (triangles), Y/2 (diamonds) and X/2 (squares) gates are shown in FIG. 10E. The infidelities thus extracted for the Y/2, Z/2, and X/2 gates are 8, 1, and 24×10−4, respectively. The X/2 gate infidelity is slightly worse than the combined infidelities from two Y/2, and one Z/2 gate. The durations for Y/2 and Z/2 are ˜20 ns, while that for the X/2 gate is ˜60 ns, and thus all the computational gates are performed within one qubit Larmor period 2π/ωq=70 ns, with all the operations occurring in the lab frame. The calculated decoherence limited errors of the Y/2, and X/2 gates are 6.67×10−5 and 2×10−4, suggesting that the major source of gate error arises from residual calibration errors in the pulse parameters, providing room for improvement even from these state-of-the-art values.

Experimental Setup

The experiment was performed in a Bluefors LD-250 dilution refrigerator with the wiring configured as shown in FIG. 11. The flux and charge inputs are attenuated with standard XMA attenuators, except the final 20 dB attenuator on the RF charge line (threaded copper). The DC and RF-flux signals were combined in a modified bias-tee (Mini-Circuits ZFBT-4R2GW+), with the capacitor replaced with a short. The DC and RF-flux lines included commercial low-pass filters (Mini-Circuits) as indicated. The RF flux and output lines also had additional low-pass filters with a sharp cutoff (8 GHz) from K&L microwave. Eccosorb (CR110) IR filters were added on the flux, and output lines, which helped improve the T1 and T2 times, and reduce the qubit and resonator temperatures. The device was heat sunk to the base stage of the refrigerator (stabilized at 15 mK) via an OFHC copper post, while surrounded by an inner lead shield thermalized via a welded copper ring. This was additionally surrounded by two cylindrical μ-metal cans (MuShield), thermally anchored using an inner close fit copper shim sheet, attached to the copper can lid. We ensured that the sample shield was light tight, to reduce thermal photons from the environment.

Device Fabrication

The device (see FIG. 7A) was fabricated on a 430 μm thick C-plane sapphire substrate. The base layer of the device, which includes the majority of the circuit (excluding the Josephson junctions), consists of 150 nm of niobium deposited via electron-beam evaporation, with features fabricated via optical lithography and reactive ion etch (RIE) at wafer-scale. 600 nm thick layer of AZ MiR 703 was used as the (positive) photoresist, and the large features were written using a Heidelberg MLA 150 Direct Writer, followed by RIE performed using a PlasmaTherm ICP Fluorine Etch tool. The junction mask was fabricated via electron-beam lithography with a bi-layer resist (MMA-PMMA) comprising of MMA EL11 and 950PMMA A7. The e-beam lithography was performed on a Raith EBPG5000 Plus E-Beam Writer. All Josephson junctions were made with the Dolan bridge technique. They were subsequently evaporated in Plassys electron beam Evaporator with double angle evaporation) (±19°. The wafer was then diced into 7×7 mm chips, mounted on a printed circuit board, and subsequently wire-bonded.

Deconstruction of Single-Qubit Gates

Modulation of the external flux drive with appropriate amplitude and duration is sufficient to perform arbitrary single-qubit rotations. The native gates available in our system are the arbitrary phase gate Rz(θ) which rotates the qubit by an arbitrary angle θ about the Z-axis and a combination of X- and Z-rotation Rxz(θ). Rz(θ) is realized by waiting for a period of Δtz=θ/ωq (since we are working in the lab frame) whereas Rxz(θ) is implemented by a flux-drive applied for a duration of Δtp=λθ/ωq. Here λ (λ≤1) is the ratio of Z-rotation to X-rotation rates. These rotation matrices can be expressed as,

\(\begin{matrix}
{{{R_{z}(\theta)} = e^{{- i}\sigma_{z}\theta/2}},} & ({C1})
\end{matrix}\)
\(\begin{matrix}
{{R_{xz}(\theta)} = {e^{{- {i({{\theta\sigma_{x}} + {\lambda{❘\theta ❘}\sigma_{z}}})}}/2}.}} & ({C2})
\end{matrix}\)
\(\begin{matrix}
{{{R_{z}(\theta)} = e^{{- i}\sigma_{z}\theta/2}},} & \text{?}
\end{matrix}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

The |θ| in Eqn. C2 arises due to the always-on Z-rotation which is unidirectional in the lab frame. A generic zero-flux-pulse can be constructed as,

(θ)=Rxz(−θx)·Rz(θz)·Rxz(θx)  (C3)

A π/2 rotation about the Y-axis (Y/2), i.e.,

\(\begin{matrix}
{{{R_{y}\left( {\pi/2} \right)} = {\frac{1}{\sqrt{2}}\begin{pmatrix}
1 & {- 1} \\
1 & 1
\end{pmatrix}}},} & ({C4})
\end{matrix}\)

is obtained using

\(\begin{matrix}
{{\theta_{x} = {\frac{1}{\sqrt{1 + \lambda^{2}}}{\cos^{- 1}\left\lbrack \frac{\lambda\left( {1 + \lambda} \right)}{- \left( {1 - \lambda} \right)} \right\rbrack}}},} & ({C5A})
\end{matrix}\)
\(\begin{matrix}
{\theta_{z} = {2{\tan^{- 1}\left\lbrack \frac{\sqrt{1 - {2\lambda} - {2\lambda^{3}} - \lambda^{4}}}{\left( {1 + \lambda} \right)\sqrt{1 + \lambda^{2}}} \right\rbrack}}} & ({C5B})
\end{matrix}\)

in Eqn. C3 provided 0≤λ≤√{square root over (2)}−1. Similarly, we can construct

\(\begin{matrix}
{{R_{y}(\pi)} = {\begin{pmatrix}
0 & {- 1} \\
1 & 0
\end{pmatrix} = {{- i}\sigma_{y}}}} & ({C6})
\end{matrix}\)

using

\(\begin{matrix}
{{\theta_{x} = {\frac{1}{\sqrt{1 + \lambda^{2}}}{\cos^{- 1}\left( \lambda^{2} \right)}}},} & ({C7A})
\end{matrix}\)
\(\begin{matrix}
{{\theta_{z} = {\pi - {2{\tan^{- 1}\left\lbrack \frac{\lambda}{\sqrt{1 - \lambda^{2}}} \right\rbrack}}}},} & ({C7B})
\end{matrix}\)

with 0≤λ≤1. An arbitrary rotation about X-axis can be constructed using

Rx(θ)=Ry(π/2)·Rz(θ)·Ry(−π/2).  (C8)

These gates are sufficient to construct any single-qubit unitary operation. We used the QuTiP python package to simulate the evolution of the computational levels under application of the pulse shown in FIGS. 9A and 9B, and obtained the gate parameters. We swept the drive amplitude A and idling period Δtz in our simulation to match the sweep performed in the experiment, as shown in FIG. 12. For all experiments and simulations reported herein, Δtp=4.76 ns.

Clifford Gate Lengths and Fidelities

A complete Clifford set includes the computational gates (exp(±iπσj/4), j=x, y) and the Pauli gates (exp(±iπσj/2), j=I, x, y, z). In this work, we constructed Y/2 and Z/2 gates, and used them as building blocks for the other gates in the Clifford Set. The total gate lengths, experimental infidelities (computational gates only), and gate compositions are shown in Table 1. The computational gate lengths range from 21-60 ns, and the longest Pauli gate (X) has a length of 78 ns. Since 2π/ωq≈70 ns, the computational gates are all within a single cycle of the qubit, and the longest gate is around one cycle as well. The microwave driving gates have lengths longer than ˜10×2π/ωq, so our gates are 10 to 30 times faster.

Fluxonium Matrix Elements and Reset Protocol

We derive the charge drive transition rates by simulating the full qubit-resonator dressed system. The drive power is normalized to 258 MHz so that the |g0→|h0 π pulse takes 80 ns, which corresponds to the typical experimental value. The simulated single-photon and two-photon transition rates (in MHz) are shown in Tables 2 and 3, respectively. The observed transition rates have additional contributions arising from the frequency dependence of the transmission through the drive line.

We utilized the |g0→|h0 and |h0→|e1 transitions for the reset protocol due their large matrix elements. While the |g0→|e1 two-photon process also has a relatively high rate, its use results in deleterious consequences since it lies in the middle of other transitions. The excited state population as a function of reset time is shown in FIG. 13. The majority of the population is pumped to state |e in 5 μs, which is mainly determined by the |h0→|e1 transition rate. We subsequently perform an additional π pulse on the |g-|e transition to initialize the system in the ground state |g0.

Plasmon-Assisted Readout

The resonator frequency shifts in increasing order are χe, χg, χh, χf. We selected the |g, |f states for plasmon-assisted readout since χf-χg is larger than χh-χe. This is reflected in the single-shot readout histogram data for |g, |e, |f, |h as shown in FIGS. 14A and 14B. The histograms in FIG. 14A are not well separated since the current sample is not optimized for high-fidelity readout.

Modeling Fluxonium Relaxation

To explain the measured relaxation times of the fluxonium, we consider decay via charge and flux coupling to the control lines, 1/f flux noise, dielectric loss in the capacitor, resistive loss in the superinductor, and Purcell loss. The decay rates arising from these loss mechanisms are derived using Fermi's golden rule, with the bath described using the Caldeira-Leggett model. For a noise source with amplitude f(t) and coupling constant α between the fluxonium qubit states, the interaction Hamiltonian can be written as H′=αf(t)σx in the qubit subspace. This results in a qubit depolarization rate,

\(\begin{matrix}
{\Gamma = {\frac{a^{2}}{\hslash^{2}}{\left( {{S_{f}\left( {+ \omega_{01}} \right)} + {S_{f}\left( {- \omega_{01}} \right)}} \right).}}} & \left( {G1} \right)
\end{matrix}\)

Here Sf(ω)=∫−∞∞eiωτ <f(τ)f(0) is the noise spectral density associated with the source. We note that at a finite bath temperature corresponding to an inverse temperature

\({\beta = \frac{1}{k_{B}T}},\)

detailed balance relates the positive and negative frequency components of the noise spectral density as Sf(−ω)/Sf(ω)=e−βℏω. Depending on the noise source f, the coupling constant α is proportional to the charge or phase matrix element of the fluxonium. Since the only term in the Hamiltonian that does not commute with {circumflex over (ϕ)} is the charging energy 4Ec{circumflex over (n)}2, and [{circumflex over (ϕ)}, {circumflex over (n)}]=i,

\(\begin{matrix}
{\ \begin{matrix}
{\left\langle {j{❘\left\lbrack {\overset{\hat{}}{\phi},\overset{\hat{}}{H}} \right\rbrack ❘}k} \right\rangle = {\left( {\omega_{j} - \omega_{k}} \right)\left\langle {j{❘\overset{\hat{}}{\phi}❘}k} \right\rangle}} \\
{= {{i\left( {8E_{c}} \right)}{\left\langle {j{❘\overset{\hat{}}{n}❘}k} \right\rangle.}}}
\end{matrix}} & \left( {G2} \right)
\end{matrix}\)

The matrix elements of the fluxonium circuit are thus related by

\({❘\left\langle {g0} \middle| \overset{\hat{}}{n} \middle| {g1} \right\rangle ❘} = {\left( \frac{\omega}{8E_{c}} \right){❘\left\langle {g0{❘\overset{\hat{}}{\phi}❘}g1} \right\rangle ❘}}\)

for all flux values.

Relaxation from Flux Noise

Flux noise couples to the phase degree of freedom with an interaction strength that depends on the inductive energy EL. Expanding the fluxonium potential to lowest order in flux results in a coupling constant of α=2πELg0|{circumflex over (φ)}|g1/Φ0. We consider flux noise contributions from current noise in the flux-bias line, as well as 1/f flux noise. In our experimental setup, the current noise is believed to be mainly due to resistive Johnson-Nyquist noise arising from a 10-dB attenuator with resistance R=26Ω (last resistor in T network) on the fast flux line, corresponding to current noise spectral density of

\({{S_{I}(\omega)} = {\frac{2}{R}\frac{\hslash\omega}{\left( {1 - e^{{- \beta}\hslash\omega}} \right)}}},\)

with the expected interpolation between quantum and thermal noise. This is related to flux noise by the mutual inductance M=θ0/1.6 mA between flux line and the qubit, obtained from the DC flux period. Therefore,

\({{{S_{f}(\omega)} + {S_{f}\left( {- \omega} \right)}} = {2\hslash\omega\frac{M^{2}}{R}{\coth\left( \frac{\beta\hslash\omega}{2} \right)}}},\)

and the decay rate

\(\begin{matrix}
{{\Gamma_{R} = \left. {{\pi^{3}\left( \frac{R_{Q}}{R} \right)}\left( \frac{M}{L} \right)^{2}\left\langle {g0{❘\overset{\hat{}}{\varphi}❘}g1} \right\rangle} \middle| {}_{2}{\omega{\coth\left( \frac{\beta\hslash\omega}{2} \right)}} \right.},} & \left( {G3} \right)
\end{matrix}\)

where RQ=h/e2 is the resistance quantum, and L is the fluxonium inductance.

For 1/f flux noise, the noise spectral density is of the form Sϕ(ω)=2πη2/ω, with the resulting decay rate,

\(\begin{matrix}
{\Gamma_{1/f} = {8{\pi^{3}\left( \frac{E_{L}}{\hslash} \right)}^{2}\left( \frac{\eta}{\Phi_{0}} \right)^{2}{\frac{{\left. {{❘\left\langle {g0} \right.❘}\overset{\hat{}}{\varphi}{❘{g1}}} \right\rangle ❘}^{2}}{\omega}.}}} & \left( {G4} \right)
\end{matrix}\)

The 1/f noise amplitude is fit from T2e data, and corresponds to η=5.21μΦ0. The suppression of the 1/f noise induced decay by EL2, results in a limit of T1=2.4 ms for the relaxation time at the flux-frustration point, which grows rapidly (∝ω3) as we move away from it.

Relaxation from Radiation Loss to the Charge Line

In addition to current noise, the fluxonium could also be affected by radiative loss arising from Johnson-Nyquist voltage noise

\(\left( {{S_{V}(\omega)} = \frac{2R\hslash\omega}{1 - e^{{- \beta}\hslash\omega}}} \right)\)

that couples to the qubit via spurious charge coupling, with the resistance R serving as a phenomenological parameter. In this case, the coupling constant is related to the charge matrix element as α=2eg0|{circumflex over (n)}|g1, and

\({{{S_{f}(\omega)} + {S_{f}\left( {- \omega} \right)}} = {2R\hslash\omega{\coth\left( \frac{\beta\hslash\omega}{2} \right)}}}.\)

The resulting decay rate is

\(\begin{matrix}
{{\left. {\Gamma_{c} = {\frac{\omega}{Q_{c}}{\coth\left( \frac{\beta\hslash\omega}{2} \right)}{❘\left\langle {g0} \right.❘}\overset{\hat{}}{n}{❘{g1}}}} \right\rangle ❘}^{2},} & \left( {G5} \right)
\end{matrix}\)

where

\({Q_{c} = \frac{R_{Q}}{16\pi R}}.\)

An upper-bound for the resistance R can be found using the plasmon T1 of 10 μs, corresponding to a total quality factor of 1.86×105, and Qc=7.4×104. This results in a fluxon T1 limit in excess of 60 ms at the flux-frustration point.

Relaxation from Dielectric Loss in the Capacitor

Dielectric loss associated with the capacitor can be thought of as Johnson-Nyquist current noise from the resistive part of the shunting capacitor, which couples to the phase matrix element g|{circumflex over (φ)}|e. This loss rate is therefore inversely proportional to the impedance of the capacitor, assuming a fixed loss tangent (1/Qdiel) for the capacitor. As a result,

\(\begin{matrix}
{{{{S_{f}(\omega)} + {S_{f}\left( {- \omega} \right)}} = {\frac{{\hslash\omega}^{2}C}{Q_{diel}}\coth\left( \frac{\beta\hslash\omega}{2} \right)}},{{{and}\Gamma_{diel}} = {\frac{{\hslash\omega}^{2}}{8E_{C}Q_{cap}}{\coth\left( \frac{\beta\hslash\omega}{2} \right)}{{❘\left\langle {{\mathcal{g}0}{❘\hat{\phi}❘}{\mathcal{g}1}} \right\rangle ❘}^{2}.}}}} & ({G6})
\end{matrix}\)

If the T1 at the frustration point were limited by dielectric loss, a bath temperature of 42 mK would result in Qcap=1/(8×10−6). This is close to the expected loss tangent and within a factor of two of that observed in similar fluxonium devices. This is believed to be the dominant loss channel near the frustration point, also capturing the flux/frequency dependence of the measured loss (∝1/ω).

Relaxation from Dielectric Loss in the Inductor

For inductive loss, we again assume a frequency independent loss tangent (L→L(1+i/Qind)), resulting in Johnson-Nyquist current noise that is inversely proportional to the impedance of the superinductor, i.e.,

\({{S_{f}(\omega)} + {S_{f}\left( {- \omega} \right)}} = {\frac{\hslash}{{LQ}_{ind}}{{\coth\left( \frac{\beta\hslash\omega}{2} \right)}.}}\)

the inductive loss is thus,

\(\begin{matrix}
{\Gamma_{ind} = {\frac{E_{L}}{\hslash Q_{L}}{\coth\left( \frac{\beta\hslash\omega}{2} \right)}{{❘\left\langle {{\mathcal{g}0}{❘\hat{\phi}❘}{\mathcal{g}1}} \right\rangle ❘}^{2}.}}} & ({G7})
\end{matrix}\)

The superinductor is extremely low loss, with a quality factor of Qind=5×109 resulting in a limit of T1=2 ms at the flux frustration point, growing as ω3 as we move away from the flux-frustration point.

Relaxation Rate Due to the Purcell Effect

We derive the Purcell relaxation rates of the fluxonium levels, arising from coupling to the resonator. We model this by assuming that the resonator is coupled to a bath of harmonic oscillators, whose Hamiltonian reads

\(\begin{matrix}
{{H_{bath} = {\sum\limits_{k}{{\hslash\omega}_{k}b_{k}^{\dagger}b_{k}}}},} & ({G8})
\end{matrix}\)

where bk is the lowering operator for mode k. The interaction Hamiltonian between the bath and the resonator is given by

\(\begin{matrix}
{{H_{int} = {\hslash{\sum\limits_{k}{\lambda_{k}\left( {{ab}_{k}^{\dagger} + {a^{\dagger}b_{k}}} \right)}}}},} & ({G9})
\end{matrix}\)

where a is the lowering operator for the resonator. Finally, the system under consideration is the fluxonium circuit coupled to the resonator, which we write in the dressed basis as

\(\begin{matrix}
{{{\left. {H_{{flux} + {res}} = {\sum\limits_{k}{E_{k}^{{flux} + {res}}{❘\psi_{k}^{{flux} + {res}}}}}} \right\rangle\left\langle \psi_{k}^{{flux} + {res}} \right.}❘}.} & ({G10})
\end{matrix}\)

We treat Hint as a perturbation which can induce transitions among the eigenstates of the Hamiltonian H=Hbath+Hflux+res, given by

\(\begin{matrix}
{\left. {\left. {\left. {❘\psi_{i}} \right\rangle = {❘\psi_{i}^{{flux} + {res}}}} \right\rangle\underset{k}{\otimes}{❘m_{k}}} \right\rangle.} & ({G11})
\end{matrix}\)

The transition rate under the action of a constant perturbation is given by Fermi's Golden Rule in the form

\(\begin{matrix}
{{\gamma_{i\rightarrow f} = {\frac{2\pi}{\hslash}{\delta\left( {E_{i} - E_{f}} \right)}{❘\left\langle {\psi_{f}{❘H_{int}❘}\psi_{i}} \right\rangle ❘}^{2}}},} & ({G12})
\end{matrix}\)

where Ei and Ef are the eigenenergies of the states |ψi and |ψf, respectively. These energies are

\(\begin{matrix}
{{E_{i} = {E_{i}^{{flux} + {res}} + {\hslash{\sum\limits_{k}{m_{k}\omega_{k}}}}}},} & ({G13})
\end{matrix}\)
\({E_{f} = {E_{f}^{{flux} + {res}} + {\hslash{\sum\limits_{k}{m_{k}^{\prime}\omega_{k}}}}}},\)

where {mk} denotes the initial configuration of the bath and {mk′} the final configuration. Inserting the form of Hint into Eqn. G12 and noting that cross-terms vanish leads to

\(\begin{matrix}
{\gamma_{i,{{\{ m_{k}\}}\rightarrow f},{\{ m_{k^{\prime}}\}}} = {2{{\pi\hslash\delta}\left( {E_{i} - E_{f}} \right)}{\sum\limits_{k}{{❘\lambda_{k}❘}^{2}\left( {{{❘\left\langle {\psi_{f}^{{flux} + {res}}{❘a^{\dagger}❘}\psi_{i}^{{flux} + {res}}} \right\rangle ❘}^{2}m_{k}\delta_{m_{k^{\prime}},{m_{k} - 1}}} + {{❘\left\langle {\psi_{f}^{{flux} + {res}}{❘a❘}\psi_{i}^{{flux} + {res}}} \right\rangle ❘}^{2}\left( {m_{k} + 1} \right)\delta_{m_{k^{\prime}},{m_{k} + 1}}}} \right){\prod\limits_{k^{\prime} \neq k}\delta_{m_{k^{\prime}}}}}}}} & ({G14})
\end{matrix}\)

To find the total transition rate, we must sum over all such initial and final configurations, taking into account the thermal probability of occupying a given initial configuration:

\(\begin{matrix}
{{\Gamma_{i\rightarrow f} = {\sum\limits_{{\{ m_{k}\}},{\{ m_{k^{\prime}}\}}}{{P\left( \left\{ m_{k} \right\} \right)}\gamma_{i,{{\{ m_{k}\}}\rightarrow f},{\{ m_{k^{\prime}}\}}}}}},} & ({G15})
\end{matrix}\)
\(where\)
\(\begin{matrix}
{{{P\left( \left\{ m_{k} \right\} \right)} = \frac{e^{- {\sum_{k}{\beta_{m_{k}}{\hslash\omega}_{k}}}}}{Z}},} & ({G16})
\end{matrix}\)

Z is the partition function of the bath and β=1/kBT. Performing the sums over all initial and final states yields

\(\begin{matrix}
{{\Gamma_{i\rightarrow f} = {{2{\pi\hslash}{\sum\limits_{k}{{❘\lambda_{k}❘}^{2}{\delta\left( {E_{i}^{{flux} + {res}} - E_{f}^{{flux} + {res}} + {\hslash\omega}_{k}} \right)}{❘\left\langle {\psi_{f}^{{flux} + {res}}{❘a^{\dagger}❘}\psi_{i}^{{flux} + {res}}} \right\rangle ❘}^{2}{n_{th}\left( \omega_{k} \right)}}}} + {2{\pi\hslash}{\sum\limits_{k}{{❘\lambda_{k}❘}^{2}{\delta\left( {E_{i}^{{flux} + {res}} - E_{f}^{{flux} + {res}} - {\hslash\omega}_{k}} \right)}{❘\left\langle {\psi_{f}^{{flux} + {res}}{❘a❘}\psi_{i}^{{flux} + {res}}} \right\rangle ❘}^{2}\left( {{n_{th}\left( \omega_{k} \right)} + 1} \right)}}}}},} & ({G17})
\end{matrix}\)
\(where\)
\(\begin{matrix}
{{n_{th}\left( \omega_{j} \right)} = {{\sum\limits_{\{ m_{k}\}}{{P\left( \left\{ m_{k} \right\} \right)}m_{j}}} = {\frac{1}{e^{{\beta\hslash\omega}_{j}} - 1}.}}} & ({G18})
\end{matrix}\)

We next take the continuum limit and define κ=2πℏρ(ωk)|λk|2 where ρ(ω) is the density of states of the bath. Introducing ωjj′flux+res=(Ejflux+res−Ej′flux+res)/ℏ leads to the expressions

Γi→f↑=κnth(ωfiflux+res)|ψfflux+res|a†|ψiflux+res|2,  (G19)

for upward transitions Efflux+res>Eiflux+res, and

Γi→f↓=κ(nth(−ωfiflux+res)+1)|ψfflux+res|a|ψiflux+res|2,  (G20)

for downward transitions Efflux+res≤Eiflux+res. The final step is to note that throughout this experiment, the fluxonium qubit is operated in the dispersive regime with respect to the frequency of the resonator. Therefore, we expect that the dressed eigenstates of Hflux+res can be labeled with quantum numbers  and n, with  labeling the fluxonium state and n the resonator state. When performing numerical simulations, this identification is based on which numbers  and n produce the maximum overlap of the dressed state |ψiflux+res= with the product state |,n. We are interested mainly in transitions among fluxonium states, where the quantum number  changes. We therefore define the total transition rate due to the Purcell effect among fluxonium states as a sum over all possible initial and final states of the resonator, weighting initial states by their probability of being thermally occupied Pres(n)=(1−exp(−βℏωr))exp(−nβℏωr). This yields

\(\begin{matrix}
{{\Gamma_{\ell\rightarrow\ell^{\prime}}^{{Purcell}, \uparrow} = {\sum\limits_{n,n^{\prime}}{{P_{res}(n)}\kappa{n_{th}\left( \omega_{\ell^{\prime},n^{\prime},\ell,n} \right)} \times {❘\left\langle {\overset{\_}{\ell^{\prime},n^{\prime}}{❘a^{\dagger}❘}\overset{\_}{\ell,n}} \right\rangle ❘}^{2}}}},} & ({G21})
\end{matrix}\)

for upward transitions, where =(−)/ℏ, and

\(\begin{matrix}
{{\Gamma_{\ell\rightarrow\ell^{\prime}}^{{Purcell}, \downarrow} = {\sum\limits_{n,n^{\prime}}{{P_{res}(n)}\kappa\left( {{n_{th}\left( {- \omega_{\ell^{\prime},n^{\prime},\ell,n}} \right)} + 1} \right) \times {❘\left\langle {\overset{\_}{\ell^{\prime},n^{\prime}}{❘a❘}\overset{\_}{\ell,n}} \right\rangle ❘}^{2}}}},} & ({G22})
\end{matrix}\)

for downward transitions. The direct Purcell loss (|e→|g) gives a T1 limit ˜100 ms, effectively negligible in our experiments. However, heating to the excited levels of fluxonium due to the finite bath temperature, results in enhanced Purcell loss. Some of these states (8th, 9th and 10th eigenstates) have transition frequencies from the logical manifold that are close to the resonator frequency, resulting in avoided crossings. While their exact location depends sensitively on the circuit parameters, these resonances are likely responsible for the decreased T1 observed near 0.35Φ0. The total Purcell relaxation rate for a bath temperature of 60 mK corresponds the dotted curve in FIG. 9A.

Modeling Fluxonium Dephasing

On the flux slope, the decay envelope of a Ramsey experiment is best approximated by a gaussian exp(−t2/Tϕ2), where Tϕ=Γϕ−1=(√{square root over (2)}η(∂ϕω01)√{square root over (ln ωirt)})−1 to first order. For the spin-echo experiments, low-frequency noise has a reduced weight in the noise spectrum, with Tϕ=(√{square root over (W)}η(∂ϕω01))−1. At the flux frustration point, the qubit is first-order insensitive to 1/f flux noise, and the spin-echo data can be explained with an exponential decay from white noise (T2e=TC=ΓC−1). In the regime of our spin-echo flux sweep, both noise sources contribute significantly. The data is therefore fit to a product of a gaussian and an exponential, with the T2e defined as exp(−T2e/TC−T2e2/Tϕ2)=1/e, i.e.,

\(\begin{matrix}
{T_{2e} = {\frac{\sqrt{{1/T_{C}^{2}} + {4/T_{\phi}^{2}}} - {1/T_{C}}}{2/T_{\phi}^{2}}.}} & ({H1})
\end{matrix}\)

## CONCLUSION

We have realized a heavy-fluxonium qubit with a 14 MHz transition frequency and coherence times exceeding those of state-of-the-art transmons, while demonstrating protocols for plasmon-assisted reset and readout of the qubit, and a new flux control scheme that performs fast high-fidelity gates. We have explored a new frequency regime in superconducting qubits and demonstrated the feasibility of a sub-thermal frequency qubit, providing a path for manipulating fluxonium qubits with computational frequencies in the range of several GHz at temperatures much higher than current dilution-refrigerator temperatures. Our new control scheme has dramatically improved the single-qubit gate speed of fluxonium qubits, making them a viable candidate for large-scale superconducting quantum computation. The gate pulses can be directly synthesized with inexpensive digital to analog converters, and are insensitive to shape distortions. Furthermore, the single-qubit gate scheme used in this work can be generalized to two inductively coupled fluxonium circuits, allowing for two-qubit gate operations without involving the participation of excited levels with more loss.

## COMBINATION OF FEATURES

Features described above as well as those claimed below may be combined in various ways without departing from the scope hereof. The following examples illustrate possible, non-limiting combinations of features and embodiments described above. It should be clear that other changes and modifications may be made to the present embodiments without departing from the spirit and scope of this invention:

(A1) A method for initializing a quantum system formed from a qubit coupled to an energy dissipater includes exciting the quantum system from a first quantum state to a second quantum state. The qubit has a qubit ground state, a qubit metastable state, a first qubit excited state, and a second qubit excited state lying above the first qubit excited state. The first quantum state is a composite of the qubit ground state and a dissipater ground state of the energy dissipater, and the second quantum state is a composite of the second qubit excited state and the dissipater ground state. The method also includes coupling the quantum system from the second quantum state to a third quantum state that is a composite of the qubit metastable state and a dissipater excited state of the energy dissipater. The quantum system decays from the third quantum state to a fourth quantum state that is a composite of the qubit metastable state and the dissipater ground state.

(A2) In the method denoted A1, the qubit may be a flux qubit.

(A3) In the method denoted A2, the flux qubit may be a fluxonium qubit.

(A4) In either one of the methods denoted A2 and A3, the flux qubit may be a fluxonium qubit.

(A5) In any one of the methods denoted A2 to A4, the qubit ground state and the qubit metastable state may be connected via a fluxon-like transition, the qubit ground state and the second qubit excited state may be connected via a plasmon-like transition, and the qubit metastable state and the first qubit excited state may be connected via a plasmon-like transition.

(A6) In any one of the methods denoted A2 to A5, the method further includes threading the flux qubit with magnetic flux to form the qubit ground state, the qubit metastable state, the first qubit excited state, and the second qubit excited state

(A7) In the method denoted A6, the magnetic flux may be one-half of a superconducting magnetic flux quantum.

(A8) In either one of the methods denoted A6 and A7, said threading, said exciting, and said coupling may occur simultaneously.

(A9) In the method denoted A8, a duration of said threading, said exciting, and said coupling may be less than both a qubit relaxation time and a qubit dephasing time of the flux qubit.

(A10) In any one of the methods denoted A1 to A9, the energy dissipater may be a resonator or a transmission line.

(A11) In any one of the methods denoted A1 to A10, said exciting may include driving the quantum system with a first microwave field having a first frequency that is resonant with a first transition between the first and second quantum states. Said coupling may include driving the quantum system with a second microwave field having a second frequency that is resonant with a second transition between the second and third quantum states.

(A12) In any one of the methods denoted A1 to A11, the method may further include transferring, with a pi pulse, the quantum system from the fourth quantum state to the first quantum state.

(A13) In the method denoted A12, a frequency of the pi pulse may be resonant with a transition between the fourth and first quantum states.

(A14) In any one of the methods denoted A1 to A13, the method may further include preparing, prior to said exciting and said coupling, the quantum system such that the qubit is in a thermal mixed state of the qubit ground state and the qubit metastable state. The quantum system, after subsequently decaying from the third quantum state to the fourth quantum state, may then be in an approximately pure quantum state.

(A15) In any one of the methods denoted A1 to A14, a qubit transition frequency between the qubit ground state and the qubit metastable state may be less than or equal to a temperature of a thermal bath surrounding the quantum system.

(A16) In any one of the methods denoted A1 to A15, the qubit metastable state may have a significant thermal occupation prior to said exciting.

(A17) In any one of the methods denoted A1 to A16, the method may further include cryogenically cooling the quantum system such that a temperature of a thermal bath surrounding the quantum system is greater than or equal to a qubit transition frequency between the qubit ground state and the qubit metastable state.

(B1) A method for initializing a quantum system formed from a qubit coupled to an energy dissipater includes exciting the quantum system from a first quantum state to a second quantum state. A qubit transition frequency between a qubit ground state of the qubit and a qubit metastable state of the qubit is less than or equal to a temperature of a thermal bath surrounding the quantum system. The first quantum state is a composite of the qubit ground state and a dissipater ground state of the energy dissipater, and the second quantum state is a composite of a second qubit excited state and the dissipater ground state. The method also includes coupling the quantum system from the second quantum state to a third quantum state that is a composite of the qubit metastable state and a dissipater excited state of the energy dissipater.

(B2) In the method denoted B1, the qubit may be a flux qubit.

(B3) In the method denoted B2, the flux qubit may be a fluxonium qubit.

(B4) In either one of the methods denoted B2 and B3, the flux qubit may be a heavy fluxonium qubit.

(B5) In any one of the methods denoted B2 to B4, the qubit ground state and the qubit metastable state may be connected via a fluxon-like transition. The qubit ground state and the qubit excited state may be connected via a plasmon-like transition.

(B6) In any one of the methods denoted B2 to B5, the method may further include threading the flux qubit with magnetic flux to form the qubit ground state, the qubit metastable state, and the qubit excited state.

(B7) In the method denoted B6, the magnetic flux may be one-half of a superconducting magnetic flux quantum.

(B8) In either one of the methods denoted B6 and B7, said threading, said exciting, and said coupling may occur simultaneously.

(B9) In the method denoted B8, wherein a duration of said threading, said exciting, and said coupling may be less than both a qubit relaxation time and a qubit dephasing time of the flux qubit.

(B10) In any one of the methods denoted B1 to B9, the energy dissipater may be a resonator or a transmission line.

(B11) In any one of the methods denoted B1 to B10, said exciting may include driving the quantum system with a first microwave field having a first frequency that is resonant with a first transition between the first and second quantum states. Said coupling may include driving the quantum system with a second microwave field having a second frequency that is resonant with a second transition between the second and third quantum states.

(B12) In any one of the methods denoted B1 to B11, the quantum system decays from the third quantum state to a fourth quantum state that is a composite of the qubit metastable state and the dissipater ground state. The method may further include transferring, with a pi pulse, the quantum system from the fourth quantum state to the first quantum state.

(B13) In the method denoted B12, a frequency of the pi pulse may be resonant with a transition between the fourth and first quantum states.

(B14) In any one of the methods denoted B1 to B13, the method may further include preparing, prior to said exciting and said coupling, the quantum system such that the qubit is in a thermal mixed state of the qubit ground state and the qubit metastable state. The quantum system, after subsequently decaying from the third quantum state to a fourth quantum state that is a composite of the qubit metastable state and the dissipater ground state, is in an approximately pure quantum state.

(B15) In any one of the methods denoted B1 to B14, the qubit metastable state may have a significant thermal occupation prior to said exciting.

(B16) In any one of the methods denoted B1 to B15, the method may further include cryogenically cooling the quantum system such that the temperature of the thermal bath surrounding the quantum system is greater than or equal to the qubit transition frequency.

(C1) A method for measuring a qubit state of a quantum system comprising a qubit coupled to a resonator includes coupling a first quantum state of the quantum system to a second quantum state of the quantum system. The qubit has a qubit ground state, a qubit metastable state, a first qubit excited state, and a second qubit excited state lying above the first qubit excited state. The qubit state is a linear superposition of the qubit ground state and the qubit metastable state, the first quantum state is a composite of the qubit metastable state and a resonator ground state of the resonator, and the second quantum state is a composite of the first qubit excited state and the resonator ground state. The method also includes dispersively reading the qubit state with the resonator. A resonant frequency of the resonator is greater than a transition frequency between the qubit metastable state and the first qubit excited state.

(C2) In the method denoted C1, the qubit may be a flux qubit.

(C3) In the method denoted C2, the flux qubit may be a fluxonium qubit.

(C4) In either one of the methods denoted C2 and C3, the flux qubit may be a heavy fluxonium qubit.

(C5) In any one of the methods denoted C2 to C4, the qubit ground state and the qubit metastable state may be connected via a fluxon-like transition, the qubit ground state and the second qubit excited state may be connected via a plasmon-like transition, and the qubit metastable state and the first qubit excited state may be connected via a plasmon-like transition.

(C6) In any one of the methods denoted C2 to C5, the method may further include threading the flux qubit with magnetic flux to form the qubit ground state, the qubit metastable state, the first qubit excited state, and the second qubit excited state.

(C7) In the method denoted C6, the magnetic flux may be one-half of a superconducting magnetic flux quantum.

(C8) In any one of the methods denoted C2 to C7, a qubit transition frequency between the qubit ground state and the qubit metastable state may be less than a temperature of a thermal bath surrounding the quantum system.

(C9) In any one of the methods denoted C2 to C8, said coupling may include applying a pi pulse.

(C10) In the method denoted C9, a frequency of the pi pulse may be resonant with a transition between the first and second quantum states.

(C11) In any one of the methods denoted C2 to C10, the method may further include preparing, prior to said coupling and said dispersively reading, the quantum system such that the qubit is in the qubit state.

(D1) A method for measuring a qubit state of a quantum system comprising a qubit coupled to a resonator includes coupling a first quantum state of the quantum system to a second quantum state of the quantum system. The qubit has a qubit ground state, a qubit metastable state, a first qubit excited state, and a second qubit excited state lying above the first qubit excited state. The qubit state is a linear superposition of the qubit ground state and the qubit metastable state, the first quantum state is a composite of the qubit ground state and a resonator ground state of the resonator, and the second quantum state is a composite of the second qubit excited state and the resonator ground state. The method also includes dispersively reading the qubit state with the resonator. A resonant frequency of the resonator is greater than a transition frequency between the qubit ground state and the second qubit excited state.

(D2) In the method denoted D1, the qubit may be a flux qubit.

(D3) In the method denoted D2, the flux qubit may be a fluxonium qubit.

(D4) In either one of the methods denoted D2 and D3, the flux qubit may be a heavy fluxonium qubit.

(D5) In any one of the methods denoted D2 to D4, the qubit ground state and the qubit metastable state may be connected via a fluxon-like transition, the qubit ground state and the second qubit excited state may be connected via a plasmon-like transition, and the qubit metastable state and the first qubit excited state may be connected via a plasmon-like transition.

(D6) In any one of the methods denoted D2 to D5, the method may further include threading the flux qubit with magnetic flux to form the qubit ground state, the qubit metastable state, the first qubit excited state, and the second qubit excited state.

(D7) In the method denoted D6, the magnetic flux may be one-half of a superconducting magnetic flux quantum.

(D8) In any one of the methods denoted D1 to D7, a qubit transition frequency between the qubit ground state and the qubit metastable state may be less than a temperature of a thermal bath surrounding the quantum system.

(D9) In any one of the methods denoted D1 to D8, said coupling may include applying a pi pulse.

(D10) In the method denoted D9, a frequency of the pi pulse may be resonant with a transition between the first and second quantum states.

(D11) In any one of the methods denoted D1 to D10, the method may further include preparing, prior to said coupling and said dispersively reading, the quantum system such that the qubit is in the qubit state.

(E1) A method for rotating a flux qubit in a linear superposition of first and second quantum-computational states includes threading the flux qubit with a magnetic flux at a nominal value such that the first and second quantum-computational states are separated by a nominal energy splitting. The linear superposition may be represented as a Bloch vector on a Bloch sphere. The method includes applying a first pulse to the flux qubit by momentarily deviating the magnetic flux away from the nominal value to rotate the Bloch vector about an x axis of the Bloch sphere.

(E2) In the method denoted E1, the first pulse may rotate the Bloch vector about the x axis by a first angle, and about a z axis of the Bloch sphere.

(E3) In either one of the methods denoted E1 and E2, a duration of the first pulse may be less than two periods of the energy splitting.

(E4) In any one of the methods denoted E1 to E3, the first and second quantum-computational states may be separated by a maximum energy splitting occurring at a peak of the first pulse, and an amplitude of the first pulse may be selected such that the maximum energy splitting is at least twice the nominal energy splitting.

(E5) In any one of the methods denoted E1 to E4, the nominal value of the magnetic flux may be one-half of a superconducting magnetic flux quantum, wherein the nominal energy splitting is equal to a Larmor frequency of the flux qubit.

(E6) In any one of the methods denoted E1 to E5, said applying the first pulse may rotate the Bloch vector about the x axis of the Bloch sphere by a first angle. The method may further include idling, after said applying the first pulse, with the magnetic flux at the nominal value to rotate the Bloch vector by a second angle about a z axis of the Bloch sphere. The method may also include applying, after said idling, a second pulse that rotates the Bloch vector by the negative of the first angle about the x axis of the Bloch sphere.

(E7) In the method denoted E6, an area of the first pulse and an area of second pulse may add to zero.

(E8) In either one of the methods denoted E6 and E7, a duration of the first pulse may equal a duration of the second pulse.

(E9) In any one of the methods denoted E6 to E8, the first and second pulses may deviate the magnetic flux away from the nominal value in opposite directions.

(E10) In any one of the methods denoted E6 to E9, a duration of each of the first and second pulses may be shorter than a duration of said idling.

(E11) In any one of the methods denoted E6 to E10, said applying the first pulse may additionally rotate the Bloch vector by the first angle about the z axis of the Bloch sphere. Said applying the second pulse may additionally rotate the Bloch vector by the first angle about the z axis of the Bloch sphere.

(E12) In any one of the methods denoted E6 to E11, the first pulse, the second pulse, and a duration of said idling may be configured such that the Bloch vector rotates about a y axis of the Bloch sphere by either positive ninety degrees or negative ninety degrees.

(E13) In any one of the methods denoted E1 to E12, the flux qubit may be a fluxonium qubit.

(E14) In any one of the methods denoted E1 to E13, the flux qubit may be a heavy fluxonium qubit.

(F1) A method for rotating a flux qubit by an angle includes threading the flux qubit with a magnetic flux at a nominal value such that first and second quantum-computational states of the flux qubit are separated by a nominal energy splitting. The flux qubit is in a superposition of the first and second quantum-computational states, and the linear superposition is represented as a Bloch vector on a Bloch sphere. The method also includes applying a first pulse to the flux qubit by momentarily deviating the magnetic flux away from the nominal value to rotate the Bloch vector by negative ninety degrees about a y axis of the Bloch sphere. The method also includes idling, after said applying the first pulse, the magnetic flux at the nominal value to rotate the Bloch vector by the angle about a z axis of the Bloch sphere. The method also includes applying, after said idling, a second pulse to the flux qubit to rotate the Bloch vector by positive ninety degrees about the y axis of the Bloch sphere. The Bloch vector is rotated by the angle about an x axis of the Bloch sphere.

(F2) In the method denoted F1, the flux qubit may be a fluxonium qubit.

(F3) In either one of the methods denoted F1, the flux qubit may be a heavy fluxonium qubit.

Changes may be made in the above methods and systems without departing from the scope hereof. It should thus be noted that the matter contained in the above description or shown in the accompanying drawings should be interpreted as illustrative and not in a limiting sense. The following claims are intended to cover all generic and specific features described herein, as well as all statements of the scope of the present method and system, which, as a matter of language, might be said to fall therebetween.

