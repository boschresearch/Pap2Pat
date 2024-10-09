# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

The present disclosure relates to compositions of matter useful as nuclear spin wave quantum registers and systems for implementing the same.

### 2. Description of Related Art

Solid-state nuclear spins surrounding individual, optically addressable qubits provide a crucial resource for quantum networks [3-6], computation [7-11] and simulation [12]. While hosts with sparse nuclear spin baths are typically chosen to mitigate qubit decoherence [13], developing coherent quantum systems in nuclear spin rich hosts enables exploration of a much broader range of materials for quantum information applications. The collective modes of these dense nuclear spin ensembles provide a natural basis for quantum storage [14]. However, utilizing them as a resource for storing quantum bits has thus far remained elusive. The present disclosure satisfies this need.

## SUMMARY OF THE INVENTION

The present disclosure reports on a novel system for transferring quantum information using a qubit with zero magnetic dipole moment and indistinguishable register spins (e.g., nuclear) having an energy level structure which can be implemented in a variety of materials. The system further includes a novel protocol for controlling spin preserving interaction between the qubit and the register spins (surprisingly, despite the lack of magnetic dipole moment and the presence of noise in the system). Working embodiments described herein demonstrate the protocol can decouple the qubit from noise causing decoherence and uncontrolled/random interactions between the qubit and register, so that the spin preserving interaction can be configured to perform a variety of operations including:


- - Polarizing the register spins into a polarized state;
  - Generating a swap gate that transfers information between qubit and
    register, and store the quantum information in the qubit in a spin
    wave form described by basis states including the polarized state
    and a superposition state of the register spins; and
  - Generating a square root of swap gate used to prepare and measure
    Bell states.

Devices and methods according to embodiments described herein include, but are not limited to, the following.

1. A device for coupling a qubit to a register, comprising:

a circuit for controlling application of one or more cycles of a protocol, the protocol comprising a sequence of pulses synchronized with an RF field, a timing, a phase, and a duration of each of the pulses, and a period and amplitude of the radio frequency (RF) field, wherein:

application of the protocol controls a coherent spin exchange interaction between a register and a qubit having a zero magnetic dipole moment;

the qubit comprises a first spin state and a second spin state both of which have a zero magnetic dipole moment;

the register comprises multiple register spins having an energy level structure,

the register spins are indistinguishable so as to be configurable in basis states including a superposition state used for storing the quantum state of the qubit, and

the pulses each comprise an electromagnetic field tuned to excite a transition between the first spin state and the second spin state.

2. The device of example 1, wherein the protocol is configured to:

suppress or cancel one or more non-exchange interactions between the register and the qubit,

suppress or cancel noise coupled to the qubit and causing decoherence of a quantum state of the qubit,

enable the coherent spin exchange interaction that performs a quantum logic gate, coherently transferring a quantum state of the qubit between the register and qubit.

3. The device of example 1 or 2, wherein the circuit controls:

application of the period of the protocol within a time period shorter than a rate of change of a magnetic noise (e.g., Overhauser field), so that the magnetic noise is quasi static during the application of the period of the protocol, the magnetic noise causing qubit decoherence and inducing a second order interaction (incoherent interaction) between the qubit and the register; and

at least one of the phase, the duration, or a time spacing of the pulses in the period so that:


- - one or more spin exchange interactions induced by the RF field are
    preserved or maintained across the period;
  - one or more non-exchange interactions induced by the RF field are
    cancelled across the period (e.g., components of the non exchange
    interactions induced at different time instances in the period
    cancel each other, or average to zero, over the period);
  - one or more (or any) exchange and one or more (or any) non-exchange
    interactions induced by the magnetic noise are cancelled across the
    period (e.g., components of these interactions induced at different
    time instances in the period cancel each other, or average to zero,
    over the period); and
  - the qubit decoherence induced by the magnetic noise is cancelled
    over the period (e.g., decoherence induced at different time
    instances in the period cancel each other, or average to zero, over
    the period); and

the RF field toggling between two values of equal magnitude and opposite polarity such that:


- - the period is associated with a frequency of a precession of each of
    the multiple register spins about a predetermined quantization axis;
    and
  - the amplitude is selected for a predetermined magnitude of the
    coherent spin exchange interaction between the register spins and
    qubit; and

so as to form a predictable and coherent spin exchange interaction.

4. The device of any of the examples 1-3, wherein each of the single qubit gates comprises one of the pulses having the frequency and duration tuned to drive a transition between the first spin state and the second spin state.

5. The device of any of the examples claim 1-4 comprising a quantum memory, wherein the circuit:

controls application of a number of cycles the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized state;

controls application of one or more of the pulses to set a quantum state of the qubit; and

controls application of a number of cycles of the protocol so as to apply a first swap gate (two qubit gate) transferring the quantum state of the qubit from the qubit to the register, thereby changing the polarized state to a corresponding state of the register spins corresponding to the quantum state; and

controls application of a number of cycles of the protocol so as to apply a second swap gate retrieving the quantum state in the qubit from the register, thereby changing the corresponding state of the register spins to the polarized state.

6. The device of any of the examples 1-5, wherein configuring the register spins in the polarized state comprises polarizing the register, which is initially in an unpolarized state comprising any configuration of excitations of the register spins, by:

(a) initializing the qubit in the first spin state by controlling application of one or more initialization pulses of an initialization electromagnetic field having a frequency tuned to initialize the quantum state of the qubit in the first spin state;

(b) applying the protocol transferring a spin excitation from the register spins to the qubit; and

(c) repeating steps (a) and (b) until all excitations of the register spins are transferred from the register to the qubit and the register spins are initialized in the polarized state, as characterized by a measurement of the qubit remaining in the first spin state after step (b).

7. The device of example 5 or 6, wherein the circuit controls application of the protocol so as to apply the first swap gate mapping (via the coherent spin exchange interaction) between the qubit and the register, such that:

if the qubit is in the first spin state, the corresponding state of the register is the polarized state,

if the qubit is in the second spin state, the corresponding state of the register is a W state, and

if the qubit is in a superposition of the first spin state and the second spin state, the corresponding state of the register is a superposition of the polarized state and the W state, and

wherein the W state is a superposition of all single spin excitation states of the register spins.

8. The device of any of the examples 1-7, wherein the circuit:

controls application of the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized state;

controls application of one or more of the pulses to set a quantum state of the qubit;

controls application of the protocol so as to apply a first square root of swap gate entangling the qubit with the register so as to form a Bell state; and

controls application of the protocol so as to apply a second square root of swap gate interacting with the Bell state so as to perform a measurement of the Bell state.

9. A repeater in a quantum network comprising the device of example 8.

10. A system for coupling the qubit to the register comprising the device of any of the examples 1-9, further comprising:

a photonic cavity coupled to a solid state material comprising the qubit and the register;

one or more microwave sources coupled to the qubit via a microwave waveguide, the microwave sources outputting one or more first microwave pulses and/or one or more second microwave pulses;

a radio frequency source outputting the RF field; and

one or more laser sources outputting one or more laser pulses coupled to the qubit through the photonic cavity; and wherein:

the circuit controls the one or more laser sources and the one or more microwave sources so as to:

output initialization pulses comprising at least one of the one or more laser pulses or the one or more first microwave pulses having initialization frequencies for exciting one or more transitions initializing the qubit;

apply the protocol comprising the single qubit gates comprising the second microwave pulses in synchronization with the RF field; and

output one or more readout electromagnetic fields having a readout frequency for exciting a readout transition from the second spin state to a readout state, so as to stimulate output of third pulses from the readout state.

11. The device of any of the examples 1-10, wherein:

the pulses each comprise a pi pulse or a pi/2 pulse having at least one phase selected from +x. −x., +y, or −y and

the circuit controls:

the sequence such that the period of the RF field is 2τ, and a spacing of the pulses is τ/4, and

for a given magnitude of the spin exchange interaction determined by the amplitude of the RF field, a number of repeats of the protocol that applies at least one of a swap gate transferring a quantum state between the qubit and the register, a square root of a swap gate for forming or measuring a Bell state, or that can be used to polarize the spins into a polarized state in combination with an initialization of the qubit.

12. The device of any of the examples 1-11 wherein the circuit selects the duration and the timing of each of the pulses and a toggling of the RF field to engineer the coherent spin-exchange interaction comprising:

Ŝ+Î−+Ŝ−Î+,

where Î+=|↑↓|,Î−=|↓↑| are the raising and lowering operators in an effective nuclear two-level manifold of the multiple spins in the register and Ŝ+ are similarly defined for the qubit.

13. The device of any of the examples 1-12, wherein the RF field comprises a square wave and the sequence of pulses comprise:

in a first half period τ of the square wave a sequence of the second pulses comprising:

a first pi/2 pulse having a phase +Y followed by a first pi pulse having a phase +Y, the beginning of the first pi/2 pulse and the center of the first pi pulse separated in time by τ/4;

a second pi/2 pulse immediately followed by a third pi/2 pulse, the end of the second pi/2 pulse separated in time from the center of the first pi pulse by τ/4, wherein the second pi/2 pulse has a phase −Y and the third pi/2 pulse has a phase −X;

a second pi pulse having a phase −X and following the third pi/2 pulse, a center of the second pi pulse separated in time from the center of the first pi pulse by τ/2; and

a fourth pi/2 pulse having a phase −X, wherein the end of the fourth pi/2 pulse is w separated in time from center of the second pi pulse by τ/4; and

in a second half period τ of the square wave, a repeat of the sequence of second pulses but wherein the first pi/2 pulse, the first pi pulse, and the second pi/2 pulse have opposite phase as compared to the first pi/2 pulse, the first pi pulse, and the second pi/2 pulse in the first half period, respectively.

14. The device of any of the examples 1-13, wherein the protocol de-couples the qubit from decoherence noise and random interactions caused by a nuclear Overhauser field generated by a host lattice in which the qubit is located.

15. A system for implementing a quantum register comprising the device of any of the examples 1-14 coupled to:

a spin carrying defect in a host lattice, wherein the spin carrying defect comprises the qubit and the host lattice comprises the register, or

a quantum dot in a host lattice, wherein the quantum dot comprises the qubit and the host lattice comprises the register.

16. The system of example 15, wherein the spin carrying defect is a qubit ion comprising the qubit and the register comprises a lattice of register ions surrounding the qubit ion.

17. The device of any of the examples 1-16, wherein the multiple spins in the register comprise nuclear spins and the first spin state and the second spin state comprise hyperfine electron spin states.

18. A method for coupling a qubit to a quantum register, comprising:

controlling application of a protocol comprising a sequence of pulses synchronized with an RF field, the protocol further comprising a timing, a phase, and a duration of each of the pulses comprising a single qubit gate, a period and amplitude of the RF field, and a number of repeats of the sequence, wherein:

application of the protocol controls a coherent spin exchange interaction between a register and a qubit having a zero magnetic dipole moment;

the qubit comprises a first spin state and a second spin state having the zero magnetic dipole moment;

the register comprises multiple register spins having an energy level structure,

the register spins are indistinguishable so as to be configurable in basis states including a superposition state used for storing the quantum state of the qubit, and

the pulses comprise an electromagnetic field tuned to excite a transition between the first spin state and the second spin state.

19. The method of claim 18, wherein the controlling further comprises:

applying the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized state;

applying of one or more of the pulses to set a quantum state of the qubit;

controlling application of the protocol so as to apply a first swap gate (two qubit gate) transferring the quantum state of the qubit from the qubit to the register, thereby changing the polarized state to a corresponding state of the register spins corresponding to the quantum state; and

controlling application of the protocol so as to apply a second swap gate retrieving the quantum state in the qubit from the register, thereby changing the corresponding state of the register spins to the polarized state.

20. The method of claim 18, wherein the controlling further comprises:

controlling application of the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized state;

controls output of one or more of the pulses to set a quantum state of the qubit;

controls application of the protocol so as to apply a first square root of swap gate entangling the qubit with the register so as to form a Bell state; and

controls application of the protocol so as to apply a second square root of swap gate interacting with the Bell state so as to perform a measurement of the Bell state.

21. A device for controlling a coherent spin exchange interaction between a register and a qubit having a zero magnetic dipole moment, wherein the qubit comprises a first spin state and a second spin state having the zero magnetic dipole moment; and the register comprises multiple indistinguishable spins.

## DETAILED DESCRIPTION OF THE INVENTION

In the following description of the preferred embodiment, reference is made to the accompanying drawings which form a part hereof, and in which is shown by way of illustration a specific embodiment in which the invention may be practiced. It is to be understood that other embodiments may be utilized, and structural changes may be made without departing from the scope of the present invention.

Technical Description

The present disclosure describes a system and method for implementing a protocol for coupling a qubit to a register. The protocol comprises a sequence of pulses synchronized with an RF field, the protocol further comprising a timing, a phase, and a duration of each of the pulses comprising a single qubit gate, a period and amplitude of the RF field, and a number of repeats of the sequence, wherein application of the protocol controls a coherent spin exchange interaction between a register and a qubit having a zero magnetic dipole moment. The qubit comprises a first spin state and a second spin state both of which have a zero magnetic dipole moment and the register comprises multiple register spins having an energy level structure. The register spins are indistinguishable so as to be configurable in basis states including a superposition state used for storing the quantum state of the qubit. The system further typically includes a source of the pulses comprising an electromagnetic field tuned to excite a transition between the first spin state and the second spin state.

The quantum memory can be implemented using nuclear spin-wave like states that can be implemented in a variety of (e.g., solid state) material systems. In typical examples, the quantum register is implemented using utilizing high spin, spectrally-indistinguishable, dense, lattice nuclear spins surrounding solid-state qubits. The control protocols induce coherent interaction between a central solid-state qubit and surrounding lattice ion nuclear spins. Specifically, the protocols are used to generate entangled states between the solid-state qubit and local nuclear ensemble and to implement a deterministic quantum register using the same ensemble. These features are vital ingredients for building large-scale multi-node quantum networks.

The following examples demonstrate an embodiment of the auxiliary nuclear-spin-based quantum register using single rare-earth ion qubits, although other material systems (including non-nuclear spin systems) may be used.

### 1. First Example: System Implemented in Yb:YVO

FIGS. 1A-1E illustrate a highly coherent, optically addressed 171Yb3+ qubit doped into a nuclear spin-rich yttrium orthovanadate crystal [15] combined with a robust quantum control protocol to manipulate the multi-level nuclear spin states of neighbouring 51V5+ lattice ions. Via a dynamically-engineered spin exchange interaction, this nuclear spin ensemble is polarized to generate collective spin excitations, and subsequently used to implement a long-lived quantum memory. Unlike conventional, disordered nuclear spin based quantum memories [16-24], the platform is deterministic and reproducible, ensuring identical quantum registers for all 171Yb3+ qubits. The approach provides a framework for utilising the complex structure of dense nuclear spin baths, paving the way for building large-scale quantum networks using single rare-earth ion qubits [15,25-28].

The hyperfine levels of single 171Yb3+ ions doped into yttrium orthovanadate (YVO4), coupled to nanophotonic cavities, form high-quality optically addressable qubits [15]. The surrounding 51V5+ lattice ion nuclear spins generate a noisy magnetic field environment due to their large magnetic moment and high spin (I=7/2). Coherent 171Yb qubit operation is enabled by magnetically-insensitive transitions, leading to long coherence times (16 ms) and high gate fidelities (0.99975) (FIG. 6). Whilst decoupling from sources of magnetic noise achieves an excellent operating regime for the 171Yb qubit, the 51V nuclear spins also provide a readily accessible, local resource for quantum information storage due to their inherently weak interactions with the environment. To date, most research regarding host nuclear spin utilisation has focused on several spectrally distinguishable impurity nuclear spins coupled to a localised electronic spin, e.g. 13C coupled to colour centres in diamond or 29Si coupled to defects in silicon carbide, rare-earth ions, quantum dots or donor qubits in silicon [10,16-24]. Recently, a regime consisting of a large number of indistinguishable nuclear spins coupled to the delocalised electronic spin in a quantum dot has also been explored [29,30]. In contrast, the system described herein addresses a new regime where a small, deterministic cluster of spectrally indistinguishable nuclear spins are coupled to a single localized electronic spin. Specifically, the 171Yb electronic wavefunction is confined to the lattice site, and the YVO4 crystal consists of highly isotopically pure, 99.8% 51V, nuclear spins. This confined, dense nuclear spin ensemble could be used as a deterministic local quantum processor by creating and manipulating entangled states, such as collective spin wave-like excitations, for near-term quantum applications. Critically, interfacing with these nuclear spins whilst preserving high qubit coherence necessitates the development of novel quantum control protocols using magnetically insensitive transitions that are robust against environmental noise.

At zero-magnetic field the 171Yb ground state contains a pair of levels |0g and |1g, separated by 675 MHz, which form our qubit [31] (FIG. 1b). The |1g population is optically read out via a series of π pulses at 984 nm, each followed by time-resolved detection of resonant photon emission (FIG. 5). This is enabled by coupling the 171Yb ion to a nanophotonic cavity leading to high transition cyclicity, reduced optical lifetime and high photon collection efficiency [15]. The local crystalline environment consists of 89Y, 51V and 16O ions. Of these, 51V with nuclear spin 7/2 has the largest magnetic dipole moment and zero-field structure due to a quadrupole interaction with the lattice electric field [32]. This leads to four quadratically-spaced, doubly degenerate energy levels, {|±m1}={|±1/2, |±5/2, |±5/2, |±7/2}, and three magnetic-dipole allowed transitions between these levels ωa,ωb,ωc (FIG. 1b).

Local 51V ions are categorised into two complementary ensembles: the register and the bath. The register spins fulfil two conditions: (1) they are constituents of the frozen core: a set of 51V ions spectrally distinguished from the bath due to proximity to 171Yb; (2) the 171Yb51V interaction Hamiltonian can drive transitions between their quadrupole levels. As shown later, experimental evidence suggests that the register consists of four 51V spins, equidistant from the central 171Yb. At zero field, the 171Yb|0g, |1g states have no magnetic dipole moment and thus interactions with 51V register spins are forbidden to first order. However, a weak 171Yb dipole moment is induced by a random magnetic field originating from the bath (the nuclear Overhauser field, with z component BπOH), giving rise to an effective 171Yb-51V register interaction. Specifically, a second-order pertur-bation analysis yields the following Hamiltonian:

\({{\hat{H}}_{int} = {{\overset{\hat{\sim}}{S}}_{z}B_{z}^{OH}{\sum\limits_{i \in {register}}\left( {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right)}}},\)

where {tilde over (Ŝ)}π is the 171Yb qubit operator along the axis in a weakly perturbed basis, Îx,z(i) are the nuclear spin-7/2 operators along the x,z axes, and ax,z are the coupling coefficients (Supplementary Information). Note that BzOH varies randomly in time as the bath changes state in a stochastic fashion, rendering this interaction Hamiltonian unreliable for register quantum state manipulation and requiring an alternative approach. To this end, we develop a protocol to generate a deterministic 171Yb-51V interaction via Hamiltonian engineering, which will be elaborated later.

An additional challenge is presented by the spectral indistinguishability of the register spins, necessitating storage in collective states. As originally proposed for quantum dots [14], single spin excitations of a polarised nuclear spin ensemble can be used for quantum information storage. These states are often termed spin waves or nuclear magnons and are generated by spin-preserving exchange dynamics. Preparing these collective nuclear spin states relies firstly on initialising the thermal register ensemble into a pure state, |0v=|↓↓↓↓, where {|↑, |↓}={|±5/2, |±7/2} is a two-level sub-manifold of the nuclear spin-7/2 51V ion (FIG. 1c, d). Next, with access to exchange dynamics and 171Yb initialised |1a, we can transfer a single excitation from the 171Yb to the register. It is noted that the excitation is delocalised equally across the four register spins due to coupling homogeneity as determined by the lattice geometry, thus naturally realising the entangled four-body W-state |Wv [33] given by

\(\left. {❘W_{v}} \right\rangle = \frac{\left. {\left. {\left. {{\left. {❘\left. \uparrow\downarrow\downarrow\downarrow \right.} \right\rangle +}❘\left. \downarrow\uparrow\downarrow\downarrow \right.} \right\rangle + {❘\left. \downarrow\downarrow\uparrow\downarrow \right.}} \right\rangle + {❘\left. \downarrow\downarrow\downarrow\uparrow \right.}} \right\rangle}{2}\)

(FIG. 1C). If the 171Yb qubit is initialised into |0g there are no spin excitations in the system and the 51V register remains in |0v. Crucially, these dynamics realise a quantum swap gate between a target state prepared by the 171Yb qubit, |ψ=α|0g+β|1g, and the |0v state of the 51V register, leading to

(α|0g+β|1g)|0v→|0g(α|0v+β|Wv).

After waiting for a certain period of time, the stored quantum state can be retrieved from the nuclear register by applying a second swap gate (FIG. 1E). Note that the spin-wave like state |Wv of the nuclear ensemble is being utilized as a constituent of the quantum memory basis.

To realise this storage protocol, the 171Yb51V spin-exchange interactions are rendered independent from the random, bath-induced dipole moment (equation (1)). Established pulse-based methods used to generate such interactions, e.g. Hartmann Hahn [34] and PulsePol [35], do not suit the requirements of the present application as they are susceptible to random noise from the bath (FIG. 7). To this end, the present invention uses a framework for robust dynamic Hamiltonian engineering [36] to design a new sequence tailored for qubits with no intrinsic magnetic moment (subsequently referred to as ZenPol for ‘zero first order Zeeman nuclear-spin polarisation’). ZenPol comprises equidistant π/2 and π pulses combined with a synchronous, z-directed, square-wave RF magnetic field with tuneable amplitude, BRF, and period 2τ (FIG. 2a). The sequence is repeated M times leading to a total interrogation duration of tM=2τM. The RF field induces an alternating 171Yb magnetic dipole moment, thereby generating a similar 171Yb-51V interaction as BπOH in equation (1) but in a controlled manner. The sequence is synchronised with the 51V precession at one of the nuclear spin transition frequencies, ωi, by satisfying

\({\frac{1}{2\tau} = \frac{\omega_{j}}{2\pi k}},\)

with k an odd integer (FIG. 8). At this resonance condition the leading-order dynamics are understood by considering the temporal interference between time-varying 171Yb spin operators and 51V precession in the interaction picture (Methods). The ZenPol sequence is designed such that RF-induced spin-preserving dynamics interfere constructively, while all other dynamics, including the bath-induced incoherent interactions, undergo destructive interference. As a result, the 171Yb-51V interaction is governed by the following timeaveraged effective Hamiltonian

\({{\hat{H}}_{avg}b_{({k,\omega_{j}})}B^{RF}{\sum\limits_{i \in {register}}\left( {{{\overset{\hat{\sim}}{S}}_{+}{\overset{\hat{\sim}}{I}}_{-}^{(i)}} + {{\overset{\hat{\sim}}{S}}_{-}{\overset{\hat{\sim}}{I}}_{+}^{(i)}}} \right)}},\)

where b(k,ω) is a k-dependent prefactor for the ωi transition, Î+=|↑↓|, Î−=|↓(↑| are the raising and lowering operators in an effective nuclear two-level manifold and {tilde over (Ŝ)}+ are similarly defined for the 171Yb qubit (Methods). While the nuclear spin can stochastically occupy either the {|+mI} or {|−mI} manifold of states, the protocol described herein is insensitive to this sign. Moreover, this pulse sequence operates at zero magnetic field where a long 171Yb coherence time can be maintained; it is insensitive to the presence of random noise from the bath; and is also robust to experimental imperfections, e.g. pulse rotation errors.

### 2. Example Protocol for the First Example

The ZenPol sequence is used to perform spectroscopy of the 171Yb nuclear spin environment. FIG. 2b shows a ZenPol spectrum obtained by initialising the 171Yb into |0g, applying an M=30 period ZenPol sequence with variable inter-pulse spacing (τ/4) and reading out the 171Yb population. As a result of the engineered exchange interaction, the |0g population decreases significantly at expected τ values corresponding to the odd-k 51V resonances (red line, FIG. 2b). Even-k resonances are also observed even in the absence of the RF field, which are attributed to the incoherent interaction dominated by the random nuclear Overhauser field (blue line, FIG. 2b).

In particular, all the odd-k resonances are split near each isolated 51V transition (dotted boxes, FIG. 2b). For example, resonance frequencies of {660 kHz, 685 kHz} and {991 kHz, 1028 kHz} are identified around the ωb (k=3) and ωc (k=5) transitions, respectively. In both cases, the higher-frequency resonance agrees well with literature values extracted from NMR on YVO crystals (685 kHz, 1027 kHz) [32]. The presence of two nuclear spin ensembles is postulated: a distant large ensemble with unperturbed frequency (constituents of the bath) and a local small ensemble with a frequency shift due to crystalline strain in the vicinity of the 171Yb ion (the register).

Polarisation of the entire nuclear spin register relies on repeated application of the ZenPol sequence, resonant with a targeted transition, interleaved with reinitialisation of the 171Yb qubit leading to unidirectional transfer of 51V population. (FIG. 5c). Since a the spin-7/2 51V ions have four energy levels, high fidelity initialisation by independently polarising different transitions is achieved with different values of τ. For example, to prepare the register spins in |±7/2=|↓, a pair of ZenPol sequences is repeatedly applied which first polarise into |±5/2 using the ωb transition, and then subsequently into ±|7/2 using the ωc transition (FIG. 9). The data confirms that both ωb and ωc transitions of the 51V register are successfully polarised as indicated by the near-complete disappearance of the initial resonances (insets, FIG. 2b). Note that the resonances at 685 kHz and 1028 kHz are unaffected, corroborating the existence of two distinct 51V ensembles discussed above. The ωa transition is not directly addressed by the ZenPol sequence due to spectral overlap with other resonances, however, this does not limit our polarisation fidelity, estimated to be ≈84%, as discussed in Supplementary Examples.

After initialising all four register 51V spins into a polarized state |0v=|↓↓↓↓, the ZenPol sequence can also induce coherent oscillations of a single spin excitation between the 171Yb ion and the polarised 51V ensemble. FIG. 2c shows the 171Yb population as a function of sequence period, M, when the single-spin exchange is targeted at the ωc transition. With 171Yb initialised in |1g, the quantum state evolves according to:

\(\left. {\left. {{\left. {\left. {\left. {❘{\psi\left( t_{m} \right)}} \right\rangle = {❘1_{g}}} \right\rangle{❘0_{v}}} \right\rangle{\cos\left( {J_{ex}t_{m}/2} \right)}} - {i{❘0_{g}}}} \right\rangle{❘W_{v}}} \right\rangle{\sin\left( {J_{ex}t_{M}/2} \right)}\)

with spin-exchange rate Jex=4b(5,ω)BRF (red, FIG. 2c). Note that when JextM=π, the sequence realises a swap gate (black arrow, FIG. 2c), whereby a single-spin excitation is completely transferred to the register, i.e., |1g|0v→|0g|Wv. Furthermore, a can be accurately controlled by var in BRF, allowing for fidelity optimisation of the swap gate (inset, FIG. 2c). By contrast, with 171Yb initialised in |0g, exchange interactions are forbidden and thus oscillations are suppressed (blue, FIG. 2c).

The spin-exchange rate is collectively enhanced by a factor of √{square root over (N)}, where N is the number of indistinguishable spins forming the register. This is verified by controlling the number of spins in the ωc transition manifold and measuring the effect on Jex. This is implemented by first emptying the ωc manifold via the application of downward-polarising ZenPol sequences, thereby pumping all four spins to |±3/2 and |±1/2. Subsequently, a single excitation is performed on the ωb transition to flip one spin from |±3/2 to |↑(=|±5/2), leading to N=1 spins in the ωc manifold. Applying a ZenPol sequence resonant with the ωc transition, it is found that the resulting exchange frequency is reduced by a factor of ≈√{square root over (4)} (FIG. 2d); according to the YVO4 lattice structure, the register likely consists of the second-nearest shell of four equidistant 51V ions (Supplementary Examples). This assumption is supported by close agreement between experiment and numerical simulation in all cases (FIG. 10).

### 3. Example Implementation of the First Example as Quantum Memory

To evaluate the performance of the 51V register as a quantum memory, its information storage times are characterized under various conditions. Specifically, a superposition state is first transferred from the 171Yb qubit,

\(\left. \left. {\left. {\frac{1}{\sqrt{2}}\left( {❘0_{g}} \right.} \right\rangle + {i{❘1_{g}}}} \right\rangle \right),\)

to the 51V register via the ZenPolbased swap gate. Subsequently, the transferred state

\({\frac{1}{\sqrt{2}}\left( {❘0_{v}} \right)} + {\left. ❘W_{v} \right\rangle)}\)

is stored for a variable wait time, t, before being swapped back to the 171Yb and measured along the x-axis, thereby probing the coherence of the final state. As shown in FIG. 3a, there is a sinusoidal oscillation of the 171Yb population, modulated by a Gaussian coherence decay, whose contrast vanishes with a 1/e time of T2*=58±4 μs. This oscillation has a frequency of ωc/2π=991 kHz, originating from relative phase accumulation between |0v and |Wv during the wait time. The coherence time of the 51V register is predominantly limited by local magnetic field noise from two sources: a fluctuating 171Yb dipole moment (171Yb Knight field) and the nuclear Overhauser field (Supplementary Information). As shown in FIG. 3b, the noise created by 171Yb can be effectively decoupled from the register by periodically flipping the 171Yb magnetic dipole orientation via a series of π pulses. Similar to the motional narrowing effect [37], the neutralization of the dipole moment arrests undesired phase diffusion of the register, leading to an increased 1/e coherence time of T2*=225±9 μs. The coherence time can be further extended by performing dynamical decoupling on the 51V register to mitigate the decoherence effect of the nuclear spin bath. This relies on applying 51Vπ pulses resonant with the ωc transition whilst leaving the bath unperturbed (FIG. 11). In FIG. 3c, we apply two 51Vπ pulses with variable inter-pulse delay, combined with periodic pulses applied to the 171Yb qubit, significantly extending the the 1/e coherence time to T2=760±1.4 μs.

The population relaxation times of the |0v and |Wv states are characterized with measured lifetimes of T1(0)=0.54±0.08 s and T1(W):=39.5±−1.3 μs, respectively. Due to the entangled nature of the |Wv state, T1(W) is limited by dephasing and is extended to 127±8 μs and 640±20 μs by applying the same decoupling sequences as in FIG. 3b,c respectively (FIG. 12). These dephasing processes can be sensitive to the stochastic occupation of the |+ml and |−ml states, depending on the degree of noise correlation between the four register spins (See Supplementary Examples).

### 4. Example Bell State Generation Using the First Example

The multi-spin register is benchmarked by characterizing fidelities of 171Yb 51V Bell state generation and detection, serving as a vital component of the quantum repeater protocol [3]. In particular, the maximally entangled Bell state

\(\left. ❘\Psi^{+} \right\rangle = {{\frac{1}{\sqrt{2}}\left( 1_{g} \right\rangle\left. ❘\text{?} \right\rangle} - {\left. i❘0_{g} \right\rangle\left. ❘\text{?} \right\rangle)}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

can be prepared by initialising the system in |1g|0v and applying a √{square root over (swap)} gate based on the ZenPol sequence satisfying JextM=π/2 (equation (6)). The Bell state coherence is evaluated by monitoring the contrast of oscillation between a given Bell state and its parity conjugate [40]. In our system, the free evolution of |Ψ+ gives rise to a parity oscillation at frequency ωc with

\(\left. \left. {\left. {\left. {\left. {\left. {❘\Psi^{-}} \right\rangle = {\frac{1}{\sqrt{2}}\left( {❘1_{g}} \right.}} \right\rangle{❘0_{v}}} \right\rangle + {i{❘0_{g}}}} \right\rangle{❘W_{v}}} \right\rangle \right)\)

(See Supplementary Examples). This oscillation is read out by applying a second √{square root over (swap)} gate to the system, encoding the parity into 171Yb population. FIG. 4 shows the measured parity oscillations decaying with a 1/ε time of T2,Bell*=8.5±0.5 μs, limited by the T2* dephasing time of the 171Yb qubit [15]. To improve the coherence, an XY−8 decoupling sequence [38] is applied to the 171Yb, leading to an enhanced value of T2,Bell*=239±6 μs (FIG. 4b); this timescale is similar to that in FIG. 3b, indicating that the Bell state coherence is likely limited by the T2* dephasing time of the 51V register.

In order to estimate the Bell state preparation fidelity, defined as =(Ψ+|ρ|Ψ+), a sequential tomography protocol [39] is performed to reconstruct the system density matrix ρ in the effective manifold spanned by four states {|0g0v, |0gWv, |1g0v, 1gWv} (FIG. 13). Taking into account errors in state readout, a corrected Bell state fidelity of 0.76±0.01 is obtained, as summarized in FIG. 4c (the uncorrected fidelity is measured to be 0.61±0.01). Without being bound by a scientific theory, this may be limited by a combination of incomplete register initialisation, imperfect Hamiltonian engineering and detrimental dephasing of the register during Bell state generation. See Methods and Supplementary Examples for detailed discussions including error analysis.

Thus, the above described examples demonstrate a noise-robust control protocol to coherently manipulate the local 51V nuclear ensemble surrounding a single optically-addressed 171Yb spin, enabling the polarisation of the high spin

\(\left( {I = \frac{\text{?}}{2}} \right)\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

nuclear register, the creation of collective spinwave excitations, and the preparation of maximally entangled Bell states. Based on these capabilities, it is shown that the local nuclear spins realise an ensemble-based quantum memory exhibiting long coherence times. Crucially, this memory is deterministic and reproducible in that every 171Yb ion doped into a YVO4 crystal accesses a near-identical nuclear register in its local environment (FIG. 14). This resource will enable the implementation of multi-node quantum network architectures using rare-earth ions with both enhanced connectivity and large-scale entanglement [3]. Furthermore, realising coherent quantum systems using dense lattice nuclear spins demonstrates the possibility of implementation in other materials for quantum information applications [13]. These multi-level nuclear spin ensembles offer an attractive, highly controllable platform to investigate the many-body dynamics of a much larger Hilbert space, paving the way for application of solidstate, noisy intermediate-scale quantum (NISQ) devices in the context of quantum simulation [12,30]

### 5. Supplementary Example Methods for Implementing the First Example

a. Experimental Setup

FIG. 5 illustrates a schematic of the complete experimental setup used for characterization of the first example.

The YVO4 crystal used in this project was cut and polished from an undoped boule (Gamdan Optics) with a residual total 171Yb concentration of 140 ppb. Nanophotonic cavities were fabricated from this material using focused ion beam milling, see [41,42] for more detail on this process. The cavity used in this work has a Qfactor of ≈10,000 leading to Purcell enhancement and consequent reduction of the 171Yb excited state lifetime from 267μ to 23μ as described and measured in [15] and >99% of ion emission coupling to the cavity mode. The reduced optical lifetime enables detection of single 171Yb ions. The cavity is undercoupled with κin/κ≈0.14 leading to 14% of emitted light entering the waveguide mode. Waveguide-freespace coupling is achieved via angled couplers with an efficiency of ≈25% and the end-to-end system efficiency (probability of detecting an emitted photon) is ≈1%.

The device sits on the still-plate of a 3He cryostat (Bluefors LD-He250) with base temperature of 460 mK. Optical signals are fed into the fridge through optical fibre and focused onto the device with an aspheric lens doublet mounted on a stack of x-y-z piezo nanopositioners (Attocube). The device is tuned on-resonance with the 171Yb optical transitions via nitrogen condensation. Residual magnetic fields are cancelled along the crystal c≡z axis with a set of home-built superconducting magnet coils.

The various optical transitions of a single 171Yb qubit are employed for state readout and initialisation (FIG. 5a). Optical addressing of the A transition for readout is established with a continuous-wave (CW) titanium sapphire (Ti:Sapph) laser (M2 Solstis) which is frequency-stabilised to a high-finesse reference cavity (Stable Laser Systems) using Pound-Drever-Hall locking [43]. The laser double-passes through two freespace acousto-optic-modulator (AOM) setups leading to single-photon level extinction of the input beam, and pulse generation with ≈10 ns rise times. A second CW external cavity diode laser (Toptica DL-Pro) is used to address the F transition during initialisation. The laser passes through an identical AOM setup and is frequency stabilised via offset-frequency locking to the Ti:Sapph.

The light output from the cavity is separated from the input with a 99:1 fibre beamsplitter, and passed through a single AOM which provides time-resolved gating of the light to prevent reflected laser pulses from saturating the detector. The light is then sent to a tungsten-silicide superconducting nanowire single photon detector (SNSPD) (Photonspot) which also sits on the still-plate of the cryostat. Photon detection events are subsequently timetagged and histogrammed (Swabian Timetagger 20).

Microwave pulses to control the ground-state qubit transition (6.75 MHz) and square-wave RF to generate the 171Yb51V interaction (100-300 kHz) are directly synthesised with an arbitrary waveform generator (Tektronix 5204AWG) and amplified (Amplifier Research 10U1000). A second microwave path is used for the excited state microwave control (3.4 GHz) necessary for qubit initialisation. The control pulses are generated by switching the output of a signal generator (SRS SG386) and amplifying (Minicircuits ZHL-16 W-43-S+). The two microwave signal paths are combined with a diplexer (Marki DPXN2) and sent into the fridge to the device. A gold coplanar waveguide fabricated on the YVO4 surface enables microwave driving of the ions.

b. 171Yb Initialisation, Readout and Experiment Sequence

At the 500 mK experiment operating temperature and at zero magnetic field, the equilibrium 171Yb population is distributed between the |auxg, 0g and |1g states (FIG. 5a) All experiments start by initialising the single 171Yb, ion into |0g via a two-stage protocol [15]. Firstly the |auxg state is emptied with a series of 3 μs pulses applied to the optical F transition each followed by a 3 μs wait period. When the 171Yb ion is successfully excited from |auxg to |1g, the population in |1g will preferentially decay to |0g during the wait time via the cavity-enhanced E transition. Subsequently, the |1g state is also emptied by applying an optical π pulse to the A transition followed by a microwave π pulse to the fg transition in rapid succession, which similarly leads to excitation from |1g to |1e and decay into |0g. This process is repeated several times for improved fidelity.

Readout of the 171Yb|1g state is performed by applying a series of 100π pulses to the A transition, each of which is followed by a 10 μs photon detection window. This process is enabled by the cyclic nature of the A transition. To read out the |0g population we apply an additional π pulse to swap the |0g↔|1g populations before performing the same optical readout procedure.

FIG. 5c shows an exemplary pulse sequence used to store and retrieve a superposition state from the register consisting of four 51V lattice ions. The sequence starts with initialisation of the 171Yb qubit into |0g and the 51V register into |0v=|±7/2⊗4. A series of ZenPol polarisation operations are interleaved with 171Yb re-initialisation sequences and alternate between ωb and ωc transition control to sequentially polarize the spin-7/2 51V register towards the |±7/2 level. After the initialization sequence, a single π/2 pulse is applied to the 171Yb qubit to prepare a superposition state. Subsequently, the state is transferred to the 51V register using a swap operation resonant with the ωc transition as detailed in the main text. After a variable wait time, the superposition state is retrieved with a second swap gate and measured in the x-basis via π/2 pulse followed by optical readout on the A transition as detailed above.

c. ZenPol Sequence

Consider a system of a single 171Yb qubit coupled to four neighbouring nuclear spin-7/2 51V ions. This hybrid spin system is described by the effective Hamiltonian (setting ℏ=1):

\(\hat{H} = {{{\Delta(t)}{\hat{\overset{\sim}{S}}}_{z}} + {\sum\limits_{i \in {register}}{Q\left( {\hat{I}}_{z}^{(i)} \right)}^{2}} + {\sum\limits_{i \in {register}}{{{\hat{\overset{\sim}{S}}}_{z}\left\lbrack {B_{z}^{OH} + {B^{RF}(t)}} \right\rbrack}\left\lbrack {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right\rbrack}}}\)

where Δ(t)=γz2(BπOH+BRF(t))2/2ω01 is the effective energy shift due to both z-directed nuclear Overhauser (BπOH) and external RF(BRF(t)) magnetic fields, ω01/2π=675 MHz is the 171Yb qubit transition frequency, γz/27=8.5 MHz/G is the 171Yb ground-state longitudinal gyromagnetic ratio, Q/2π=165 kHz is the 51V register nuclear quadrupole splitting, {tilde over (Ŝ)}x is the 171Yb qubit operator along the z-axis, Îx,z are the 51V spin-7/2 operators along the x- and z-axis, and ax,z are the effective coupling strengths between 171Yb and 51V along the x- and z-axes. See Supplementary Information for a detailed derivation of this effective Hamiltonian.

As discussed in the main text, polarisation of the 51V register and preparation of collective spin-wave states relies on induced polarisation transfer from the 171Yb to 51V and is achieved via periodic driving of the 171Yb qubit. Specifically, periodic pulsed control can dynamically engineer the original Hamiltonian (equation (7)) to realize effective spin-exchange interaction between 151Yb and 51V ions of the form, {tilde over (Ŝ)}+Î−+{tilde over (Ŝ)}−Î+, in the average Hamiltonian picture [36],[44] One example of such a protocol is the recently developed PulsePol sequence [35], however, it relies on states with a constant, nonzero magnetic dipole moment and therefore cannot be used in our system since the 171Yb qubit has no intrinsic magnetic dipole moment. Motivated by this approach, we have developed a variant of the PulsePol sequence that accompanies a square-wave RF field synchronized with the sequence (FIG. 8a). The base sequence has a total of 8 free-evolution intervals with equal duration (τ/4) defined by periodically spaced short pulses and is repeatedly applied to 171Yb. Following the sequence design framework presented in Ref. [36], we judiciously choose the phase and ordering of the constituent π/2 and π pulses such that the resulting effective interaction has spin-exchange form with strength proportional to the RF magnetic field amplitude (BRF), whilst decoupling from interactions induced by the Overhauser field (BπOH). The sequence was designed to cancel detuning induced by both of these fields and to retain robustness against pulse rotation errors to leading order. We term this new sequence ‘ZenPol’ for ‘zero first-order Zeeman nuclear-spin polarisation’.

To understand how the ZenPol sequence works, one can consider a toggling-frame transformation of the 171Yb spin operator along the quantisation axis ({tilde over (Ŝ)}z,tog(t)): we keep track of how this operator is transformed after each preceding pulse. For example, the first π/2 pulse around the y-axis transforms {tilde over (Ŝ)}π into −{tilde over (Ŝ)}x and the subsequent π pulse around the y-axis transforms −{tilde over (Ŝ)}x into +{tilde over (Ŝ)}x. Over one sequence period, the toggling frame transformation generates a time-dependent Hamiltonian Ĥtog(t) that is piecewise constant for each of 8 free-evolution intervals, which can be expressed as

\({{\hat{H}}_{tog}(t)} = {{{\Delta(t)}\left\lbrack {{{f_{x}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{x}} + {{f_{y}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{y}}} \right\rbrack} + {\sum\limits_{i \in {register}}{Q\left( {\hat{I}}_{z}^{(i)} \right)}^{2}} + {\sum\limits_{i \in {register}}{{B_{z}^{OH}\left\lbrack {{{f_{x}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{x}} + {{f_{y}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{y}}} \right\rbrack}\left\lbrack {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right\rbrack}} + {\sum\limits_{i \in {register}}{{B^{RF}\left\lbrack {{{f_{x}^{RF}(t)}{\hat{\overset{\sim}{S}}}_{x}} + {{f_{y}^{RF}(t)}{\hat{\overset{\sim}{S}}}_{y}}} \right\rbrack}\left\lbrack {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right\rbrack}}}\)

Here fx,yOH(t) describes the time-dependent modulation of the 171Yb z-spin operator ({tilde over (Ŝ)}z.tog(t)=fxOH(t){tilde over (Ŝ)}x+fyOH(t){tilde over (Ŝ)}y) (FIG. 8a). Note that fπOH(t)=0 for all intervals. Since the externally-applied squarewave RF field is constant for each half-sequence period, we can replace BRF(t) with the amplitude BRF and transfer the time dependence to fx,yOH by applying sign flips, thus leading to redefined modulation functions fx,yRF (FIG. 8a).

The spin-7/2 51V ion exhibits three distinct transitions at frequencies ωa,b,c (FIG. 1b) In the following, we consider an effective spin-1/2 system for the 51V ions using the ωc manifold {|Î=|=5/2, |↓=|±7/2}, with

\({{\hat{\overset{\sim}{I}}}_{x} = {\frac{1}{2}\left( ❘\uparrow \right)\left( {\left. \downarrow ❘ \right. + \left. ❘\downarrow \right.} \right)\left( \uparrow ❘ \right)}},{{\hat{\overset{\sim}{I}}}_{y} = {{\frac{1}{2i}\left( ❘\uparrow \right)\left( {\left. \downarrow ❘ \right. - \left. ❘\downarrow \right.} \right)\left( \uparrow ❘ \right){and}{\hat{\overset{\sim}{I}}}_{z}} = {\frac{1}{2}\left( ❘\uparrow \right)\left( \uparrow{❘ - ❘}\downarrow \right){\left( \downarrow ❘ \right).}}}}\)

In a rotating frame with respect to the target frequency ωc, the nuclear spin operators become {tilde over (Î)}x→{tilde over (Î)}x cos(ωct)+{tilde over (Î)}y sin(ωct) and {tilde over (Î)}π→{tilde over (Î)}x. Thus, the leading- order average Hamiltonian,

\({{\hat{H}}_{avg} = {\text{?}{dt}{{\hat{H}}_{tog}(t)}}},\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

in the rotating frame is given by:

\({\hat{H}}_{avg} = {\sum\limits_{i \in {register}}{\frac{a_{x}\sqrt{7}}{2\tau}{\int_{0}^{2\tau}{{dt}{\left\{ {{{B_{z}^{OH}\left\lbrack {{{f_{x}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{x}} + {{f_{y}^{OH}(t)}{\hat{\overset{\sim}{S}}}_{y}}} \right\rbrack}\left\lbrack {{{\hat{\overset{\sim}{I}}}_{x}^{(i)}{\cos\left( \text{?} \right)}} + {{\hat{\overset{\sim}{I}}}_{y}^{(i)}{\sin\left( \text{?} \right)}}} \right\rbrack} + {{B^{RF}\left\lbrack {{{f_{x}^{RF}(t)}{\hat{\overset{\sim}{S}}}_{x}} + {{f_{y}^{RF}(t)}{\hat{\overset{\sim}{S}}}_{y}}} \right\rbrack}\left\lbrack {{{\hat{\overset{\sim}{I}}}_{x}^{(i)}{\cos\left( \text{?} \right)}} + {{\hat{\overset{\sim}{I}}}_{y}^{(i)}{\sin\left( \text{?} \right)}}} \right\rbrack}} \right\}.}}}}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

Here, various terms are excluded as they time average to zero (rotating-wave approximation). The √{square root over (7)} prefactor comes from mapping the original spin-7/2 operators to the effective spin-1/2 ones. Additionally, the energy shift induced by BπTH and time-dependent BRF is cancelled since we are using square-wave RF. The Fourier transforms of the modulation functions fx,y(t), termed the filter functions [45], directly reveal resonance frequencies at which equation (9) yields non-zero contributions (FIG. 8b). Resonant interactions with strength proportional to the nuclear Overhauser field are achieved at sequence periods 2τ which satisfy

\({\frac{1}{2\tau} = \frac{\text{?}}{2{\pi \times 2}}},\frac{\text{?}}{2{\pi \times 4}},\frac{\text{?}}{2{\pi \times 6}},{\cdots;}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

interactions proportional to the RF field occur at sequence periods satisfying

\({\frac{1}{2\tau} = \frac{\text{?}}{2{\pi \times 1}}},\frac{\text{?}}{2{\pi \times 3}},\frac{\text{?}}{2{\pi \times 5}},{\cdots.}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

These two sets of resonances occur at different values of 2τ, hence we can preferentially utilise the coherent, RF-induced interactions whilst decoupling from those induced by the randomised Overhauser field. This is experimentally demonstrated in FIG. 2b where the RF-induced resonances are spectrally resolved. In this measurement the linewidth of the register resonances are limited by that of the filter function. We also note that the transition cannot be independently addressed by the ZenPol sequence due to the multiplicity of the three 51V transitions determined by the quadratic Hamiltonian (ωa=ωb/2=ωc/3).

We use the RF-driven resonance identified at

\(\frac{1}{\text{?}} = \frac{\text{?}}{2{\pi \times 5}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

by setting the free-evolution interval to

\(\frac{\text{?}}{\text{?}} = {\frac{\text{?}}{\text{?}}.}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

Under this resonance condition, the average Hamiltonian (equation (9)) is simplified to

\({\hat{H}}_{avg} = {{{- \sqrt{7}}\left( \frac{1 + \sqrt{2}}{5\pi} \right)a_{x}{B^{RF} \times {\sum\limits_{i \in {register}}\left( {{\left( {{\hat{\overset{\sim}{S}}}_{x} + {\hat{\overset{\sim}{S}}}_{y}} \right){\hat{\overset{\sim}{I}}}_{x}^{(i)}} + {\left( {{- {\hat{\overset{\sim}{S}}}_{x}} + {\hat{\overset{\sim}{S}}}_{y}} \right){\hat{\overset{\sim}{I}}}_{y}^{(i)}}} \right)}}} = {{{- \sqrt{7}}\left( \frac{\sqrt{2} + 2}{5\pi} \right)a_{x}B^{RF}{\sum\limits_{i \in {register}}\left( {{{\hat{\overset{\sim}{S}}}_{x}^{\prime}{\hat{\overset{\sim}{I}}}_{x}^{(i)}} + {{\hat{\overset{\sim}{S}}}_{y}^{\prime}{\hat{\overset{\sim}{I}}}_{y}^{(i)}}} \right)}} = {\text{?}B^{RF}{\sum\limits_{i \in {register}}{\left( {{{\hat{\overset{\sim}{S}}}_{+}^{\prime}{\hat{\overset{\sim}{I}}}_{-}^{(i)}} + {{\hat{\overset{\sim}{S}}}_{-}^{\prime}{\hat{\overset{\sim}{I}}}_{+}^{(i)}}} \right).}}}}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

Here, going from the first to the second line, we change the local 171Yb basis by rotating 45 degrees around the z axis such that {tilde over (Ŝ)}x′=({tilde over (Ŝ)}x+{tilde over (Ŝ)}y)/√{square root over (2)}, {tilde over (Ŝ)}y′=(−{tilde over (Ŝ)}x+{tilde over (Ŝ)}y)/√{square root over (2)}, and from the second to the third line, {tilde over (Ŝ)}+′={tilde over (Ŝ)}x′±i{tilde over (Ŝ)}y′ and {tilde over (Î)}+′={tilde over (Î)}x′±i{tilde over (Ŝ)}y are used. We define the coefficient b(k,ω) which determines the interaction strength for the kth resonance addressing transition ωi (for example, b(5,ω)=−√{square root over (7)}(√{square root over (2)}+2)ax/10π). In the discussion in the first example above, we omitted the primes on the 171Yb spin operators for the sake of notational simplicity. The same analysis can be performed for other transitions, yielding a similar spin exchange Hamiltonian, albeit with different interaction 9) strength.

d. Direct Drive Gates for 51V Register

Performing dynamical decoupling on the register requires selective driving of the froze-core 51V nuclear spins without perturbing the bath and is achieved through a two-fold mechanism. Firstly we initialise the 171Yb qubit into |0g and apply a sinusoidal z-directed RF magnetic field at ωc/2π=991 kHz through the coplanar waveguide to induce an oscillating 171Yb magnetic dipole moment (FIG. 11a) This generates an x-directed field component at each 51V spin, where the driving Hamiltonian is given by Ĥdrive=μNqvxAxBπosc sin(ωct)Ĩx with Ax=3 ln μ0γz2/8πr3ω01. Here, μN is the nuclear magneton, gvx is the 51V directed g-factor, Bzosc is the sinusoidal RF magnetic field amplitude, Îx is the nuclear spin-7/2 operator along the x-axis, {l,n} are the {x,z} directional cosines of the 171Yb-51V displacement vector, μ0 is the vacuum permittivity, and r is the 171Yb-51V ion distance (Supplementary Information). The lattice symmetry of the host leads to equidistant spacing of the four proximal 51V spins from the central 171Yb qubit allowing homogeneous coherent driving of all register spins.

In this direct driving scheme, we note that the effect of Bzosc is amplified by a factor of Ax≈6.7 for the frozen core register spins at a distance of r=3.9 Å (Supplementary Information). Crucially, the amplification factor scales as Ax∝1/r3 with distance r from the 171Yb qubit, leading to a reduced driving strength for distant 51V bath spins. Moreover, the transition frequency of the bath, ωcbath/2π=1028 kHz, is detuned by 37 kHz from that of the register, ωc/2π=991 kHz, further weakening the bath interaction due to off-resonant driving provided that the Rabi frequency is less than the detuning.

In a rotating frame at frequency ωc, the driving Hamiltonian Ĥdrive gives rise to Rabi oscillation dynamics of the register spins within the ωc manifold, {|↑=|±5/2, |↓=|±7/2}. To calibrate 51V π pulse times, we initialise the register into |0v=|↓↓↓↓, drive the register for variable time, and read out the |0v population by preparing the 171Yb qubit in |1g and applying a swap gate to the ωc transition. If the final 51V spin state is in |↓(|↑) the swap will be successful (unsuccessful) and the 171Yb qubit will end up in |0g(|1g). Using this method, we induce resonant Rabi oscillations of the register at a Rabi frequency of 2π×(7.65±0.05) kHz (blue markers, FIG. 11c) which exhibit exponential decay on a 280±30 μs timescale, limited by dephasing caused by the fluctuating 171Yb Knight field. This can be decoupled using motional narrowing techniques whereby we periodically apply π pulses to the 171Yb every 6 μs during the drive period. In order to drive the 51V spins in a phase-continuous manner, we compensate for the inversion of the 171Yb magnetic dipole moment after each π pulse by applying a π phase shift to the sinusoidal driving field (FIG. 11b). This leads to an extended 1/e Gaussian decay time of 1040±70 μs (red markers, FIG. 11c). The arrow in FIG. 11c indicates the 69 μs 51Vπ pulse time used for dynamical decoupling. In contrast to the spin-preserving exchange interaction, this direct drive protocol provides independent, local control of the four 171V spins with no constraints on the number of excitations, thereby coupling the 51V register to states outside the two-level manifold spanned by |0v and |Wv. For example, at odd multiple π times, we find

\(\left. \left. {\left. {\left. \left. {❘0_{v}} \right\rangle\rightarrow \right.❘}\uparrow\uparrow\uparrow\uparrow \right\rangle{❘W_{v}}} \right\rangle\rightarrow\frac{\left. \left. {\left. {\left. {\left. \left( {❘\left. \downarrow\uparrow\uparrow\uparrow \right.} \right. \right\rangle + {❘\left. \uparrow\downarrow\uparrow\uparrow \right.}} \right\rangle + {❘\left. \uparrow\uparrow\downarrow\uparrow \right.}} \right\rangle + {❘\left. \uparrow\uparrow\uparrow\downarrow \right.}} \right\rangle \right)}{2} \right.,\)

both of which contain more than a single excitation. For this reason, we use an even number of π pulses in our decoupling sequences to always return the 51V register to the memory manifold prior to state retrieval.

e. Population Basis Measurements

We developed a sequential tomography protocol [39] to read out the populations of the joint 171Yb-51V density matrix ρ in the effective four-state basis, {|0g0v, |0gWv, |1g0v, |1gWv}. This is achieved using two separate sequences: Readout sequence 1 and Readout sequence 2, applied alternately, which measure the {|0g0v, |0gWv} and {|1g0v, |1gWv} populations respectively. As shown in FIG. 13a, these sequences are distinguished by the presence (absence) of a single π pulse applied to the 171Yb qubit at the start of the sequence. This is followed by a single optical readout cycle on the A transition; results are post-selected on detection of a single optical photon during this period. Hence the presence (absence) of the first π pulse results in |0g(|1g) state readout after post selection. Furthermore, in all post-selected cases the 171Yb qubit is initialised to |1g by taking into account this conditional measurement outcome. Subsequently, an unconditional π pulse is applied to the 171Yb, preparing it in |0g and a swap gate is applied, thereby transferring the 51V state to the 171Yb. Finally, we perform single-shot readout of the 171Yb state according to the protocol developed in [15]. Specifically, we apply two sets of 100 readout cycles to the A transition separated by a single π pulse which inverts the 171Yb qubit population. The 51V state is ascribed to |Wv(|0v) if ≥1(0) photons are detected in the second readout period and 0(≥1) photons are detected in the third. The possible photon detection events and state attributions are summarized in FIG. 13b.

This protocol was demonstrated by characterizing the state preparation fidelities of the four basis states, the measured histograms are presented in FIG. 13c alongside the respective gate sequences used for state preparation. The resulting uncorrected (corrected) preparation fidelities for these four basis states are:

|00=0.79±0.01(0.82±0.02),

|0W=0.50±0.02(0.64±0.02),

|10=0.79±0.01(0.82±0.02),

|1W=0.50±0.02(0.61±0.02)

The reduced fidelity of |0gWv and |1gWv relative to |0g0v and |1g0v arises from the swap gate used for the |Wv state preparation. Finally, we characterized the fidelity of the maximally entangled 171Yb-51V Bell state,

\({\left. ❘\Psi^{+} \right\rangle = {\left. \frac{1}{\sqrt{2}}\text{(}1_{g}\text{?} \right\rangle - {\left. i❘0_{g}W_{v} \right\rangle)}}},\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

prepared using a single √{square root over (swap)} gate as described in the first example (FIG. 13d). The corresponding uncorrected (corrected) populations for the four basis states, pij(cij) denoted are:

p00≡0g0v|ρ|0g0v=0.16±0.01(c00=0.07±0.02),

p01≡0gWv|ρ|0gWv=0.326±0.01(c01=0.41±0.02),

p01≡1g0v|ρ|1g0v=0.40±0.02(c10=0.41±0.02),

p11≡1gWv|ρ|1gWv=0.12±0.01(c11=0.11±0.01),

f. Swap Gate Fidelity Correction

Since 171Yb readout fidelity is >95% [15], the dominant error introduced during the population basis measurements arises from the swap gate. Its fidelity in the population basis was measured by preparing either the |0g0v state (zero spin excitations) or the |1g0v state (single spin excitation) and applying two consecutive swap gates such that the system is returned to the initial state. By comparing the 171Yb population before (ppre) and after (ppost) the two gates are applied, fidelity estimates can be extracted independently from the 51V state initialisation. Assuming the swap and swapback processes are symmetric, a gate fidelity sw=√{square root over ((1−2ppost)/(1−2ppre))} is obtained. This quantity is measured for zero spin excitations leading to sw,0=0.83 and with a single spin excitation leading to sw,1=0.52.

When measuring the joint 171Yb-51V populations {p00, p01, p10, p11}, these fidelities can be used to extract a set of corrected populations {c00, c01, c10, c11} according to the method described in [46,47] using

\(\begin{pmatrix}
c_{11} \\
c_{10} \\
c_{01} \\
c_{00}
\end{pmatrix} = {E^{- 1}\begin{pmatrix}
p_{11} \\
p_{10} \\
p_{01} \\
p_{00}
\end{pmatrix}}\)

where

\(E = {\frac{1}{2}{\begin{pmatrix}
{1 + \mathcal{F}_{{sw},1}} & {1 - \mathcal{F}_{{sw},0}} & 0 & 0 \\
{1 - \mathcal{F}_{{sw},1}} & {1 + \mathcal{F}_{{sw},0}} & 0 & 0 \\
0 & 0 & {1 + \mathcal{F}_{{sw},1}} & {1 - \mathcal{F}_{{sw},0}} \\
0 & 0 & {1 - \mathcal{F}_{{sw},1}} & {1 + \mathcal{F}_{{sw},0}}
\end{pmatrix}.}}\)

A similar approach to correct the √{square root over (swap)} gate was used to read out the Bell state coherence.

### 6. Supplementary Example Derivations for Interactions and Hamiltonians Described Herein

a. 171Yb-51-V Interactions

(i). Ground State 171Yb Hamiltonian

The effective spin-1/2 Hamiltonian for the zF7/2(0)171Yb3+ ground state is given by [1]:

Ĥeff=μBB·g·Ŝ+ÎVh·A·Ŝ

where B is the magnetic field, Ŝ and ÎYb are vectors of 171Yb electron and nuclear spin-1/2 operators respectively and we neglect the nuclear Zeeman term. The uniaxial ground state g tensor is given by:

\(g = {\begin{pmatrix}
g_{x} & 0 & 0 \\
0 & g_{x} & 0 \\
0 & 0 & g_{z}
\end{pmatrix} = \begin{pmatrix}
0.85 & 0 & 0 \\
0 & 0.85 & 0 \\
0 & 0 & {- 6.08}
\end{pmatrix}}\)

which is a uniaxial tensor with the extraordinary axis parallel to the c-axis of the crystal and the two ordinary axes aligned with the crystal a-axes. The ground state A tensor is given by:

\(A = {2{\pi \times \begin{pmatrix}
0.675 & 0 & 0 \\
0 & 0.675 & 0 \\
0 & 0 & {- 4.82}
\end{pmatrix}}{GHz}}\)

FIG. 5a shows the zero magnetic field energy level structure with hybridised 171Yb electron-nuclear spin eigenstates. Note that the zero-field 171Yb qubit states, |0g and |1g, have no magnetic dipole moment. See [1] for more details. Throughout this work we adopt ℏ=1 convention.

(ii). Local Nuclear Spin Environment

The 171Yb3+ ion substitutes for yttrium in a single site of the YVO4 crystal, furthermore naturally abundant Y and V contain 99.8% 51V and 100% 89Y isotopes. Hence each 171Yb ion experiences a near-identical nuclear spin environment. The 51V ions have nuclear spin-7/2 leading to electric quadrupole interactions that cause a zero-field splitting. The resulting zero-field energy level structure of the bath is given by:

Ĥv=QbathÎx2

with Qbath/2π=171 kHz measured using nuclear magnetic resonance (NMR) on bulk YVO4 crystals [2] and Îx the 51V nuclear spin-7/2 spin operator along the c≡z axis. Note that the local 51V register ions surrounding the 171Yb qubit experience a frozen-core detuning as discussed in the main text, leading to a smaller quadrupolar splitting with Q/2π=165 kHz. The energy level structure of these register ions is shown in FIG. 1b. The 89Y ion, on the other hand, has no zero-field structure.

The positions of the six nearest 51V ions are tabulated below, where r=[xyz] is the 171Yb-51V position vector with magnitude r and direction cosines {l,m,n}.

Note that the two nearest 51V ions (1 and 2) are located directly above and below the 171Yb qubit along the z-axis, due to their positions they cannot be driven by the induced 171Yb magnetic dipole moment and thus belong to the bath (Supplementary Information Section I C). In contrast, ions 3-6 are symmetrically positioned in the lattice with non-zero x/y and z coordinates, forming the frozen-core register spins utilized as a quantum memory. The 51V ions have a uniaxial g-tensor with form [3]:

\(g_{v} = \begin{pmatrix}
g_{vx} & 0 & 0 \\
0 & g_{vx} & 0 \\
0 & 0 & g_{vz}
\end{pmatrix}\)

(iii) 171Yb-51V Interactions

The magnetic dipole-dipole interaction between the 171Yb qubit and a single 51V ion can be described by the following Hamiltonian:

\({\hat{H}}_{dd} = {\frac{\mu_{0}}{4\pi}\left\lbrack {\frac{\mu_{Yb} \cdot \mu_{V}}{r^{3}} - \frac{3\left( {\mu_{Yb} \cdot r} \right)\left( {\mu_{V} \cdot r} \right)}{r^{5}}} \right\rbrack}\)

where μVh=−μBg·Ŝ, μV=μNgV·Î (note that Î is a vector of 51V nuclear spin operators), μB is the Bohr magneton, μN is the nuclear magneton, μ0 is the vacuum permeability and r is the 171Yb 51V displacement vector with magnitude r. Due to the highly off-resonant nature of the 171Yb51V interaction, a secular approximation would be appropriate. To first order, however, all secular terms involving the 171Yb qubit basis are zero, i.e., 0g|Ĥdd|0g=0, 1g|Ĥdd|1g=0

To proceed, consider that second-order effects which generally scale as ˜g2/ΔE, where ΔE is the energy separation between a pair of unperturbed eigenstates. By taking into account the fact that gz is roughly 7 times larger than gx,gy and Ŝπ terms in Ĥdd mix |0g and |1g with small ΔE whereas, Ŝx and Ŝy mix the 171Yb qubit states and |aux g with large ΔE, we restrict our consideration to the Ŝπ terms in Ĥdd:

\({\hat{H}}_{dd} \approx {\frac{\mu_{0}\mu_{B}\mu_{N}g_{z}}{4\pi r^{3}}{{\hat{S}}_{z}\left\lbrack {{3\ln g_{vx}{\hat{I}}_{x}} + {3{mng}_{vx}{\hat{I}}_{y}} + {\left( {{3n^{2}} - 1} \right)g_{vz}{\hat{I}}_{z}}} \right\rbrack}}\)

where {l,m,n} are direction cosines of the 171Yb51V displacement vector. Note that the Ŝx operator is the electron spin-1/2 operator defined as Ŝz=½(|0g1g|+|1g0g|) in the basis of the hybridised eigenstates of the 171Yb qubit.

(iv) Nuclear Overhauser Field

As discussed in the first example, the 51V spins can be divided into two ensembles: register spins and bath spins. The bath spins comprise 51V ions which are not driven by the 171Yb qubit for the following two reasons:

1 Ions which aren't driven due to position: certain ions (such as 1 and 2 in the above table) only interact via an Ising-type ŜxÎx Hamiltonian. Hence the 171Yb qubit cannot be used to drive transitions between the 51V z-quantised quadrupole levels.

2 Ions which aren't driven due to detuning: As observed in the ZenPol spectra (FIG. 2b in the main text), more distant spins are spectrally separated from the nearby ions comprising the register.

It is assumed that the bath spins are in an infinite-temperature mixed state: ρV=1V/Tr{1V}, where 1V is the identity matrix in the Hilbert space for the bath spins. In the mean field picture, their effect on the 171Yb can be approximated as a classical fluctuating magnetic field, commonly termed the nuclear Overhauser field. As mentioned previously, since gz2>>gx,y2, the z-component of the Overhauser field is dominant, given by

\({B_{z}^{OH} = {\sum\limits_{i \in {bath}}{\frac{\mu_{0}\mu_{N}g_{vz}}{4{\pi\left( r^{(i)} \right)}^{3}}\left( {{3\left( n^{(i)} \right)^{2}} - 1} \right)m_{I}^{(i)}}}},\)

where r(i) and n(i) are the distance and z-direction cosine between the 171Yb and ith bath spin, and ml(i)∈{−7/2, −5/2, . . . , 5/2, 7/2} is the nuclear spin projection at site i. Note that BπOH is randomly fluctuating due to the stochastic occupation of the 8 possible |mI states, however, it is quasi-static on the timescale of our control sequences, hence we do not label the time dependence. The nuclear Overhauser field generates some weak mixing between |0g and |1g leading to perturbed eigenstates |{tilde over (0)}g and |{tilde over (1)}g which have a small, induced, z-directed dipole moment. x These states have the form

\({\left. ❘{\overset{\sim}{0}}_{g} \right\rangle = {\left. ❘0_{g} \right\rangle + \left. \frac{\gamma_{z}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}{2\omega_{01}}❘1_{g} \right\rangle}}{\left. ❘{\overset{\sim}{1}}_{g} \right\rangle = {\left. ❘1_{g} \right\rangle - \left. \frac{\gamma_{z}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}{2\omega_{01}}❘0_{g} \right\rangle}}\)

where γz=gzμB is the longitudinal gyromagnetic ratio of the 171Yb qubit and ω01/2π=675 MHz is the unperturbed 171Yb|0g↔|1g transition frequency. Here we have added the effect of an externally applied, z-directed, square wave RF magnetic field BRF(t) with amplitude BRF used in the ZenPol sequence; note that this field is piecewise constant for each half-sequence period, hence the time dependence corresponds to periodic flips between ±BRF. In addition, these fields induce a detuning of the 171Yb|0g↔|1g transition, which can be calculated using second-order perturbation theory as Δ(t)=γx2(BπOH+BRF(t))2/2ω01.

(v) Interaction with Register Ions

We postulate that the second nearest shell of four 51V ions (ions 3-6 in the table above) comprise the register. These four ions are equidistant from the 171Yb and interact via both an ŜxÎx term and ŜzÎx or ŜzÎy terms. To identify an effective interaction Hamiltonian in the perturbed basis {|{tilde over (0)}g, |{tilde over (1)}g}, only secular matrix elements of Ĥdd (equation (S7)) are considered:

\({\hat{\overset{\sim}{H}}}_{dd} = {{\left\langle {\overset{\sim}{0}}_{g}❘{\hat{H}}_{dd}❘{\overset{\sim}{0}}_{g} \right\rangle\left. ❘{\overset{\sim}{0}}_{g} \right\rangle\left\langle {\overset{\sim}{0}}_{g}❘ \right.} + {\left\langle {\overset{\sim}{1}}_{g}❘{\hat{H}}_{dd}❘\overset{\sim}{1} \right\rangle\left. ❘{\overset{\sim}{1}}_{g} \right\rangle\left\langle {\overset{\sim}{1}}_{g}❘ \right.}}\)
\(where\)
\(\left\langle {\overset{\sim}{0}}_{g}❘{\hat{H}}_{dd}❘{\overset{\sim}{0}}_{g} \right\rangle = {+ {\frac{\mu_{0}\mu_{N}{\gamma_{z}^{2}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}}{8\pi{r}^{3}\omega_{01}}\left\lbrack {{3\ln g_{vx}{\hat{I}}_{x}} + {3{mng}_{vx}{\hat{I}}_{y}} + {\left( {{3n^{2}} - 1} \right)g_{vz}{\hat{I}}_{z}}} \right\rbrack}}\)
\(\left\langle {\overset{\sim}{1}}_{g}❘{\hat{H}}_{dd}❘{\overset{\sim}{1}}_{g} \right\rangle = {- {{\frac{\mu_{0}\mu_{N}{\gamma_{z}^{2}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}}{8\pi{r}^{3}\omega_{01}}\left\lbrack {{3\ln g_{vx}{\hat{I}}_{x}} + {3{mng}_{vx}{\hat{I}}_{y}} + {\left( {{3n^{2}} - 1} \right)g_{vz}{\hat{I}}_{z}}} \right\rbrack}.}}\)

Hence the effective interaction between the 171Yb qubit and the four register spins, Ĥint=Σi∈register{tilde over (Ĥ)}dd(i), can be described by

\({\hat{H}}_{int} = {{{\hat{\overset{\sim}{S}}}_{z}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}{\sum\limits_{i \in {register}}\left( {{J_{x}^{(i)}{\hat{I}}_{x}^{(i)}} + {J_{y}^{(i)}{\hat{I}}_{y}^{(i)}} + {J_{z}^{(i)}I_{z}^{(i)}}} \right)}}\)
\(with\)
\(I_{x}^{(i)} = \frac{{- 3}\mu_{0}\mu_{N}\gamma_{z}^{2}g_{vx}l^{(i)}n^{(i)}}{4{\pi\left( r^{(i)} \right)}^{3}\omega_{01}}\)
\(I_{y}^{(i)} = \frac{{- 3}\mu_{0}\mu_{N}\gamma_{z}^{2}g_{vx}m^{(i)}n^{(i)}}{4{\pi\left( r^{(i)} \right)}^{3}\omega_{01}}\)
\(J_{z}^{(i)} = \frac{{- 3}\mu_{0}\mu_{N}\gamma_{z}^{2}{g_{vz}\left( {{3\left( n^{(i)} \right)^{2}} - 1} \right)}}{4{\pi\left( r^{(i)} \right)}^{3}\omega_{01}}\)
\(and\)
\({\overset{\hat{}}{\overset{\sim}{S}}}_{z} = {\frac{1}{2}{\left( {{\left. ❘{\overset{\sim}{1}}_{g} \right\rangle\left\langle {\overset{\sim}{1}}_{g}❘ \right.} - {\left. ❘{\overset{\sim}{0}}_{g} \right\rangle\left\langle {\overset{\sim}{0}}_{g}❘ \right.}} \right).}}\)

Finally, local basis transformations of each 51V ion are performed to further simplify the Hamiltonian form. Specifically, we apply the following unitary rotation:

\(\left. {\hat{H}}_{int}\rightarrow{U{\hat{H}}_{int}U^{\dagger}} \right.{{U = {\prod\limits_{j \in {register}}{\exp\left\lbrack {i\theta^{(j)}{\hat{I}}_{z}^{(j)}} \right\rbrack}}},{{{where}\theta^{(j)}} = {\tan^{- 1}\left( {m^{(j)}/I^{(j)}} \right)}},{{which}{leads}{to}}}{{\hat{H}}_{int} = {{{\hat{\overset{\sim}{S}}}_{z}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}{\sum\limits_{i \in {register}}\left\lbrack {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right\rbrack}}}{{{with}a_{x}} = {{\sqrt{\left( J_{x}^{(i)} \right)^{2} + \left( J_{y}^{(i)} \right)^{2}}{and}a_{z}} = {J_{z}^{(i)}.}}}\)

Note that the coupling coefficients ax and az are homogeneous (i.e. independent of site index i) since the four register spins are equidistant from the central 171Yb and have directional cosine factors with equal magnitude.

The same result can also be derived using the Schrieffer-Wolff transformation [4, 5], where the interaction Hamiltonian obtained here corresponds to the dominant second-order perturbation terms. Hereafter notation can be simplified by using |0g and |1g without tildes to represent the weakly perturbed eigenstates in the presence of any small magnetic field.

(vi) Full System Hamiltonian

Combining the various energy and interaction terms, the full system Hamiltonian (in a 171Yb frame rotating at ω01/2π=675 MHz) becomes:

\({\hat{H}}_{full} = {{\frac{{\gamma_{z}^{2}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right)}^{2}}{2\omega_{01}}{\overset{\hat{}}{\overset{\sim}{S}}}_{z}} + {\sum\limits_{i \in {register}}{{Q\left( {\hat{I}}_{z}^{(i)} \right)}^{2}{+ {\overset{\hat{}}{\overset{\sim}{S}}}_{z}}\left( {B_{z}^{OH} + {B^{RF}(t)}} \right){\sum\limits_{i \in {register}}{\left\lbrack {{a_{x}{\hat{I}}_{x}^{(i)}} + {a_{z}{\hat{I}}_{z}^{(i)}}} \right\rbrack.}}}}}\)

b. Randomised Benchmarking and Dynamical Decoupling

High fidelity control of the 171Yb|0g↔|1g transition is essential for implementing the ZenPol sequence and enabling coherent 171Yb51V interactions. For example, a single swap operation realised by the ZenPol sequence contains 120 local 171Yb gates. Single qubit gate fidelity can be characterized using randomised benchmarking [6], which provides a value independent from state preparation or measurement (SPAM) errors. We apply randomly sampled single qubit Clifford gates constructed using π and π/2 rotations around the x and y directions followed by the single-gate inverse operation (FIG. 6a). When the number of gates, Mgate, increases, the sequence error accumulates and the probability of returning to the initial |0g state reduces according to an exponential decay:

P=0.5+PndM.

When ensemble-averaged over a sufficiently large number of random gate sets (in our case 100), f=½(1+d) becomes a reliable estimate of the average single-qubit gate fidelity. Measurement results are presented in FIG. 6a, leading to an extracted average single qubit gate fidelity of f=0.99975±0.00004.

The T2 coherence time of the qubit transition is measured using an XY-8 dynamical decoupling sequence [7]. Specifically, we work with a fixed inter-pulse separation of 5.6 μs and measure the coherence time by varying the number of decoupling periods, Mr (FIG. 6b). An exponential decay 1/e with time constant T2=16±2 ms is measured. This measurement uses the same method as in [8], however, we observe a factor of three improvement in coherence due to the improved microwave setup leading to correspondingly increased π gate fidelities.

c. Extra Register Detail

In this section additional technical details are provided related to the single excitation states used to store quantum information on the 51V spins.

The general form for the engineered spin-exchange interaction is:

\({{\hat{H}}_{avg} = {B^{RF}{\sum\limits_{i \in {register}}{b_{({k,\omega_{j}})}^{(i)}\left( {{{\overset{\hat{}}{\overset{\sim}{S}}}_{+}{\overset{\hat{}}{\overset{\sim}{I}}}_{-}^{(i)}} + {{\overset{\hat{}}{\overset{\sim}{S}}}_{-}{\overset{\hat{}}{\overset{\sim}{I}}}_{+}^{(i)}}} \right)}}}},\)

where, BRF is the square-wave RF magnetic field amplitude, b(k,ω)(i) is a k-dependent prefactor for transitions ωi of the ith register spin, {tilde over (Î)}+=|↑↓|, {tilde over (Î)}−=|↓(↑|, are raising and lowering operators in an effective nuclear spin-1/2 manifold and {tilde over (Ŝ)}+=|1g0g|, {tilde over (Ŝ)}−=|0g1g| are raising and lowering operators for the 171Yb qubit. Note, in this section, we do not assume homogeneous coupling to the register spins, hence the b(kωj)(i) coefficients depend on the register site index i. In addition, we consider an arbitrary number of register spins, N, that are spectrally indistinguishable.

When the 171Yb is initialised in |1g and the 51V register spins are polarised in |0v=|↓⊗N, this interaction leads to the following spin-exchange evolution [9]:

|ψ(t)=|1g|0v cos(Jext/2)−i|0g|1v sin(Jext/2)

where the spin-exchange frequency is given by:

\(I_{ex} = {2B^{rf}\sqrt{\sum\limits_{i \in {register}}{❘b_{({k,\omega_{j}})}^{(i)}❘}^{2}}}\)

and the resulting single-spin excited state generated by this interaction is:

\(\left. ❘1_{v} \right\rangle = {\frac{1}{\Sigma_{i}{❘b_{({k,{\omega}_{j}})}^{(i)}❘}^{2}}{\sum\limits_{i \in {register}}\left. b_{({k,{\omega}_{j}})}^{(i)}❘\downarrow\ldots\uparrow{}_{(i)}\ldots\downarrow{\rangle.} \right.}}\)

Based on the results presented in FIG. 2d and Supplementary Information Section VIII we postulate that for our system the register consists of the second nearest shell of four homogeneously coupled 51V ions. In this case we recover the expressions presented in the main text, namely, the single-spin excitation in the register realises an entangled four-body W-state, |Wv, as depicted in FIG. 1c:

\(\left. ❘1_{v} \right\rangle = {\left. ❘W_{v} \right\rangle = \frac{\text{↑↓↓↓〉+↓↑↓↓〉+↓↓↑↓〉+↓↓↓↑〉}}{2}}\)

and the spin-exchange rate is given by Jex=4BRFb(k,ω). In general, for N homogeneously coupled register spins, we expect that the spin-exchange rate is enhanced by a factor of √{square root over (N)}, leading to faster swap gate operation.

In this protocol it is possible to transfer a second spin excitation to the register. More specifically, the spin-preserving exchange interaction, {tilde over (Ŝ)}−{tilde over (Î)}++{tilde over (Ŝ)}+{tilde over (Î)}−, couples the state |1g|Wv to |0g|2v, where |2v is a 51V state with two spins in |↑. To avoid undesired excitation to states outside of the effective {0v, |Wv} manifold, the 171Yb qubit in |0g is always prepared before retrieving stored states from the 51V register. Hence the swap gate realised by this interaction operates on a limited basis of states.

Utilising the dense, lattice nuclear spins ensures near identical registers for all 171Yb ions. FIG. 14 shows ZenPol spectra near the ωc transition, collectively enhanced spin-exchange oscillations and motionally-narrowed T2* times for three 51V registers coupled to three different 171Yb ions. The 171Yb optical and microwave frequencies were re-calibrated for each ion, however, all aspects of the experimental sequences related to register control and readout were identical.

d. Simulation

We simulate our coupled spin system using the effective Hamiltonian derived in Supplementary Information, however we add three additional terms:

1 Nuclear Zeeman interactions of the 51V register spins with the Overhauser field from the bath: Since the energy levels are quantised along the z-axis, magnetic fluctuations along the z-direction dominate, which can be captured by the following Hamiltonian

\(\text{?} = {\sum\limits_{i \in {register}}{\mu_{N}g_{vz}{B_{z}^{OH}\left( r_{i} \right)}{\hat{I}}_{z}^{(i)}}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

where BπOH(ri) is the z-component of the Overhauser field evaluated at the position of the ith register ion, ri.

2 Nuclear magnetic dipole-dipole interactions of the register spins:

\(\text{?} = {\underset{i < j}{\sum\limits_{i,{j \in {register}}}}{\frac{\mu_{0}}{4\pi}\left\lbrack {\frac{\mu_{v}^{(i)} \cdot \mu_{v}^{(j)}}{r_{ij}^{3}} - \frac{3\left( {\mu_{v}^{(i)} \cdot r_{ij}} \right)\left( {\mu_{v}^{(j)} \cdot r_{ij}} \right)}{r_{ij}^{5}}} \right\rbrack}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

with rij the displacement vector between 51V register spins at site i and j. 3. 171Yb-enhanced register spin-spin interactions: These terms are derived by considering second-order perturbations using the Schrieffer-Wolff transformation [4,5]. For example, the dominant Ising-type terms take the form

\({{\hat{H}}_{edd} = {\sum\limits_{i,{j \in {register}}}{{\frac{1}{2\omega_{01}}\left\lbrack {\left( {{3n^{2}} - 1} \right)\frac{\mu_{0}\mu_{N}\gamma_{z}g_{vz}}{4\pi r^{3}}} \right\rbrack}^{2}{\hat{S}}_{z}{\hat{I}}_{z}^{(i)}{\hat{I}}_{z}^{(j)}}}},\)

where r and n are the magnitude and c-direction cosine of the 171Yb 51V register ion displacement vector. However, we note that the ZenPol sequence cancels these interactions to first order.

By simulating 171Yb Ramsey coherence times, gvz≈1.6 is extracted. Estimation of the bare 51V coherence time indicates a potential discrepancy in this value gvz by up to 25%, discussed further in Supplementary Information, however, this has a negligible impact on the ZenPol sequence simulations. An estimate for gvx≈0.6 is obtained by calibrating the RF field amplitude and comparing with the experimental results of direct 51V spin driving in FIG. 11.

The nuclear Overhauser field BπOH is computed according to equation (S8) by randomly sampling the bath states for each Monte-Carlo simulation repetition. A simple model of the bath dynamics is included by incorporating stochastic jumps of the bath spins on magnetic-dipole allowed transitions.

The register spin dynamics are simulated in a reduced Hilbert space by considering only the ωc manifold. This enables fast simulation of all four register spins plus the 171Yb qubit transition (Hilbert space with dimension 32). Imperfect polarisation of the 51V register into |↓=|±7/2 is categorised into two distinct types:

1 Imperfect polarisation within the ωc transition i.e. a small residual population ϵ1 in |↑=|5/2.

2 Imperfect polarisation outside the ωc manifold i.e. a small residual population ϵ2 in |±1/2 and |±3/2.

This leads to a |↓ population of 1−ϵ1−ϵ2. Incomplete polarization is incoporated by sampling different register initial states for each Monte-Carlo repetition. For case 1, this involves occasionally initialising a given 51V ion into |↑, while for case 2 this involves reducing the Hilbert space dimension by removing the 51V ion from the simulation. Finite pulse duration effects are taken into account by modeling the ZenPol sequence using 25 nsπ/2 and 50 nsπ pulses (FIG. 10a).

As shown in Extended Data FIG. 6d, the spin-exchange oscillations from numerical simulation (red dashed line) exhibit slower decay than the measured experimental results (red markers). A phenomenological exponential decay envelope, ce−M/τ, is added to the simulation results where c and τM are free parameters, and M is the ZenPol sequence period. The additional decay could be caused by heating due to the RF field, excess 171Yb dephasing or additional register spin interactions which we haven't considered here. This model is fitted by optimising multiple parameters: ϵ1,ϵ2,BRF,c and τM. The resulting values of ϵ1 and ϵ2 are 0.12 and 0.04, respectively, indicating ≈84% polarisation into |↓; the RF magnetic field amplitude is BRF≈1.6G and the phenomenological exponential decay parameters are c=0.8 and τM=90 leading to a close fit with the experimental results (red solid line, FIG. 2c and FIG. 10d). Additional simulation results following this methodology with varying BRF and τ are presented in FIG. 10.

Finally, the results are modeled with a single-spin excitation in the ωc-manifold by including the |±3/2 level in the simulation (FIG. 2d and Supplementary Information). The initial state used in this simulation is partially polarised between the |±3/2 level with population 1−ϵ and the |±1/2 level with population ϵ. We use the same value of BRF=1.6G as in FIG. 2c, and optimise the polarisation level leading to 1−ϵ=0.8. The close correspondence between the measured and simulated oscillation profiles suggests that the register consists of the second shell of four homogeneously coupled 51V ions.

e. Hartmann Hahn Spectroscopy

In addition to the ZenPol spectra discussed above, Hartmann-Hahn (HH) double resonance [10] is used to perform spectroscopy of the nuclear spin environment. This method enables spin exchange between two systems with different transition frequencies by resonantly driving a qubit with a Rabi frequency that matches the energy level splitting of the environmental nuclear spins. In our case, we resonantly drive the 171Yb at 675 MHz to generate a pair of dressed states

\(\left. ❘ \pm \right\rangle = {\frac{1}{\sqrt{2}}\left( {\left. ❘0_{g} \right\rangle \pm \left. i❘1_{g} \right\rangle} \right)}\)

with splitting Ω which we sweep over a range ≈2π×(0−2.3) MHz (FIG. 7). The 171Yb qubit is initialised into the |− dressed state by a π/2 pulse preceding the driving period. If resonant with a nuclear spin transition, the 171Yb qubit undergoes spin exchange at a rate dictated by the interaction strength. Finally we read out the 171Yb|+ dressed state population to determine whether spin exchange has occurred. FIG. 7b shows experimental results of Hartmann-Hahn spectroscopy where we vary both the HH drive Rabi frequency (Ω) and also the HH pulse duration (t). The counts plotted on the colour-bar are proportional to the |+ dressed state population. Three clear resonances are found at evenly spaced pulse amplitudes 0.15, 0.30 and 0.45 corresponding to the ωa, ωb and ωc 51V transitions; notably, unlike ZenPol, the HH sequence only has one harmonic leading to a single resonant interaction per transition. Also note the lack of oscillations when varying the pulse duration, t, on resonance with either of the three transitions: this is because the spin exchange is driven by the randomised, Overhauser field induced 171Yb dipole moment. For this reason, the HH sequence cannot be used to generate the coherent exchange interaction necessary to realise a swap gate for our system. In the case of no driving (Ω=0), the signal rapidly saturates as t increases as a result of Ramsey dephasing of the initial state. However, as Ω exceeds the 171Yb spin linewidth (˜50 kHz[8]), this effect diminishes due to the emergence of spin-locking effects and consequently leads to an increased saturation timescale when not resonant with the 51V transitions. The resolution of this measurement is also limited by the 171Yb spin linewidth, and we therefore cannot resolve the split-resonance structure observed in the ZenPol spectra. The results agree well with simulations (FIG. 7c) verifying that interactions with the 51V quadrupolar structure dominate these measurements.

f. Polarisation of Multi-Level Register Nuclear Spins

Polarisation dynamics are explored using the PROPI method (polarisation readout by polarisation inversion) [11]. This sequence uses the back-action of the 51V spins on the 171Yb to measure the register polarisation after successive ZenPol polarisation cycles. For instance, when polarising into |↑=|±5/2 on the ωc transition, the 171Yb is initialised into |1g and undergoes spin exchange with any 51V population in |↓=|±7/2. The 171Yb|0g population after interaction is therefore related to the residual 51V|↓ population. As presented in FIG. 9a, the 171Yb population is measured after each of 20 consecutive polarisation cycles and a saturation is observed after 10 cycles, indicating that the 171Yb polarisation has been transferred to the 51V register. The high-contrast signal obtained in this measurement is enabled by alternating the 51V polarisation direction, i.e. periods of polarisation into |↑ are interleaved with periods of polarisation into |↓. This mitigates the need to wait for slow register thermalisation (T1(0)≈0.5 s, see Supplementary Information Section X) between consecutive experiment repetitions. These measurements are repeated with ZenPol sequences on the ωb transition, demonstrating similar levels of polarisation saturation after approximately 10 cycles (FIG. 9b).

We also demonstrate the effect of incomplete register polarization on the spin-exchange oscillation by varying the number of polarisation cycles on the ωb and ωc transitions before each experiment (FIG. 9c). As expected, the coherent spin-exchange oscillations emerge as an increasing number of polarisation cycles are applied.

These results inform the design of polarisation sequences used in subsequent single-spin excitation experiments where 40 polarisation cycles interleaved between the ωb and ωc transitions are sufficient to polarise the register into |0v=|↓↓↓↓. Based on simulations discussed in Supplementary Information, we estimate this protocol achieves ≈84% polarisation into the |0v state. Note the ZenPol sequence is not used to directly polarise the ωa transition due to spectral overlap with ωb and ωc (FIG. 2b). We postulate that the high degree of polarisation can still be achieved even in the absence of direct ωa transition control due to two factors:

1 The thermalisation timescale of the ωa transition is significantly shorter than the interrogation time. Specifically, our experiments typically run for several minutes whereas the ωa thermalisation rate is likely similar to T1(0)=0.54 s. Thus, undesired population in the |±1/2 level can still pumped to |±7/2 once it relaxes to |±3/2.

2 Once successfully initialised into the ωc manifold the probability of shelving into the |±1/2 level is small as it necessitates two consecutive decays on the ωb and ωa transitions, both of which are considerably slower than our experiment/polarisation repetition rate (20 ms).

We tried to improve the polarisation fidelity by incorporating direct driving on the ωa transition during the polarisation protocol. This leads to fast population exchange between ±1/2 and |±3/2, however, there was no improvement to the contrast of the resulting spin exchange oscillations thereby indicating that shelving into |±1/2 is not a limiting factor in our experiments.

g. Analysis of Spin Exchange Dynamics

In this section, an analysis of the spin exchange dynamics on the ωc register transition is presented. The spin-exchange measurements in FIG. 2c are measured at a fixed ZenPol period of 2τ=5.048 μs leading to resonant interactions with the 991 kHz ωc-transition. However, analogous to the Rabi oscillations in a two-level system, the oscillation frequency and contrast of these spin transfer oscillations also depend on the detuning of the ZenPol sequence relative to the 51V transition. Specifically, we expect the following relations:

\({{J_{ex}(\delta)} = \sqrt{{J_{ex}(0)}^{2} + \delta^{2}}}{{C(\delta)} = \frac{{J_{ex}(0)}^{2}}{{J_{ex}(0)}^{2} + \delta^{2}}}\)

Here Jex and C are the spin-exchange frequency and oscillation contrast, respectively, and δ is the detuning of the ZenPol sequence resonance relative to a target nuclear spin transition. The register is polarized into |0v and FIG. 10C shows measurement of the frequency detuning dependence of the spin-exchange oscillations. These results agree well with the corresponding simulations shown in FIG. 10c.

Control of the spin exchange frequency by varying the RF magnetic field amplitude (BRF) is also demonstrated. FIG. 10D shows the spin-exchange dynamics for four different values of BRF=0.8G, 1.2G, 1.6G and 2.0G. The inset in FIG. 2C plots extracted spin exchange frequencies Jex for a range of different BRF demonstrating linear dependence as expected and leading to accurate control of the engineered interaction strength (see First Example for details).

h. Single Excitation in ωc Manifold

The ability to shelve populations in different quadrupole levels enables the operation of the 51V register with an alternative set of many-body states: |0v′ and |1v′. For this experiment the 51V spins are polarized down the energy ladder on the ωb and ωc transitions leading to polarisation primarily into the |±3/2 level, with a small residual population in |±1/2. For the purpose of this analysis, perfect polarisation into |±3/2 is assumed, however ωa transition polarisation/addressability would be required for this.

The register |1v′ state is prepared by injecting a single spin excitation on the ωb transition (i.e. from |±3/2→|↑=|±5/2), this is achieved using the corresponding ZenPol resonance at ωb,k=3:

\(\left. \left. {\left. {\left. {\left. {\left. {❘1_{v}^{\prime}} \right\rangle = {\frac{1}{2}\left( {❘\left. \uparrow,\frac{3}{2},\frac{3}{2},\frac{3}{2} \right.} \right.}} \right\rangle + {❘\left. \frac{3}{2},\uparrow,\frac{3}{2},\frac{3}{2} \right.}} \right\rangle + {❘\left. \frac{3}{2},\frac{3}{2},\uparrow,\frac{3}{2} \right.}} \right\rangle + {❘\left. \frac{3}{2},\frac{3}{2},\frac{3}{2},\uparrow \right.}} \right\rangle \right)\)

Here the ± sign is omitted in the state label for simplicity. Subsequently, the 171Yb in |0g and induce a spin exchange oscillation between |↑ and |↓=|±7/2 via a ZenPol sequence resonant with the ωc transition. The resulting time evolution is given by

\(\left. ❘{\psi(t)} \right\rangle = {{\left. ❘0_{g} \right\rangle\left. ❘1_{v}^{\prime} \right\rangle\cos\left( \frac{J_{ex}^{\prime}t}{2} \right)} - {\left. i❘1_{g} \right\rangle\left. ❘0_{v}^{\prime} \right\rangle\sin\left( \frac{J_{ex}^{\prime}t}{2} \right)}}\)
\(where\)
\(\left. \left. {\left. {\left. {\left. {\left. {❘0_{v}^{\prime}} \right\rangle = {\frac{1}{2}\left( {❘\left. \downarrow,\frac{3}{2},\frac{3}{2},\frac{3}{2} \right.} \right.}} \right\rangle + {❘\left. \frac{3}{2},\downarrow,\frac{3}{2},\frac{3}{2} \right.}} \right\rangle + {❘\left. \frac{3}{2},\frac{3}{2},\downarrow,\frac{3}{2} \right.}} \right\rangle + {❘\left. \frac{3}{2},\frac{3}{2},\frac{3}{2},\downarrow \right.}} \right\rangle \right)\)

and Jex′=2b(k,ω)BRF with k=5. Notice that the spin-exchange oscillation rate, Jex′, no longer has a √{square root over (N)} rate enhancement, this is because every ket in the |1v′ and |0v′ states contains only a single spin in the ωc-transition manifold. Using this manifold for information storage would have several benefits. For instance, direct microwave driving of the register ωc-transition would lead to Rabi oscillation between |0v′ and |1v′ and could therefore be used to realise local gates in this basis. Additionally, a second spin excitation is not allowed in this scheme, therefore the ZenPol sequence reproduces a complete two-qubit swap gate regardless of the 171Yb state. For these reasons, we believe that there may be some advantages to working with the {|0v′, |1v′} manifold if the state initialisation fidelity into |±3/2 can be improved via direct ωa transition polarisation.

i. T2* Coherence Discussion

Here we provide detailed discussions regarding the 51V register coherence decay processes described in the main text. There are two magnetic interactions which limit the T2* dephasing timescale: (1) the direct nuclear Zeeman interaction of each register spin with the Overhauser field (equation (S20)) and (2) a contribution from the 171Yb Knight field [12]. In the latter case, the bath-induced 171Yb dipole moment generates a randomly fluctuating magnetic field at each 51V ion, the Knight field, which is described by

\(\text{?} = {{\pm g_{vz}}\mu_{N}B_{z}^{OH}A_{z}{\hat{I}}_{z}}\)
\(with\)
\(A_{z} = \frac{\mu_{8}{\gamma_{z}^{2}\left( {1 - {3n^{2}}} \right)}}{8\pi r^{3}\text{?}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

Here, the + and − cases in equation (S28) correspond to 171Yb in |1g and |0g, respectively. The constants are defined in Supplementary Information Section. We note that Az corresponds to an effective local field amplification factor with value Az≈3.1 for the register spins. We define the 171Yb Knight field to be ±AπBπOH.

By applying periodic π pulses to the 171Yb, we flip its state between |0g and |1g, thereby switching the sign of the Knight field. This leads to the cancellation of V phase accumulation between successive free evolution periods, resulting in a longer coherence time. We numerically simulate the register coherence times using the method outlined in Supplementary Information Section IV. When limited by the 171Yb Knight field, simulation yields a Gaussian decay with a 1/e coherence time of 33 μs (equivalent to experimental results in FIG. 3a). We also predict an upper bound for the coherence time when decoupled from the 171Yb Knight field by turning off Hamiltonian terms associated with equation (S28), yielding an extended Gaussian decay of 417 μs (equivalent to experimental results in FIG. 3b). These simulated values are consistent with the corresponding experimental results (58±4 μs and 225±9 μs respectively) to within a factor of two. We note that this could indicate an error in our estimation of gvz by up to 25%, potentially caused by a small discrepancy in the position of the two 51V bath spins closest to 171Yb. Further analysis of these parameters is left for future work.

j T1 Lifetime Discussion

We measure the population decay of both the |0v and |Wv states (timescales T1(0) and T1(W) respectively) by preparing the 51V register in the appropriate state and waiting for a variable time, t, before swapping to the 171Yb for readout.

The |0v state exhibits slow exponential decay with 1/e time constant T1(0)=0.54±0.08 s (FIG. 12b). There are two contributions which could be limiting this decay:

1 Resonant population exchange between the register spins and unpolarised frozen-core ‘dark spins’. For instance, the two nearest 51V ions (ions 1 and 2 in the table in Supplementary Information Section) may interact resonantly with the neighbouring register spins. However, we cannot detect or polarise these dark spins since they only interact with the 171Yb via Ising-like ŜπÎπ terms.

2 Off-resonant population exchange between the register and detuned unpolarised bath spins.

As for the |Wv state, it exhibits a Gaussian decay with a much faster 1/e time constant of T1(W)=39.5±1.3 μs (FIG. 12a). This can be explained by considering the effect of dephasing on the register spins. Specifically, the |Wv state which our 171Yb qubit interacts with is given as

|Wv=½(↑↓↓↓+|↓↑↓↓+|↓↓|↓|↓↓↓↑).

Crucially, there are three additional orthogonal states required to span the 51V register single excitation subspace:

|αv=½(|↑↓↓↓+|↓↑↓↓−|↓↓↑↓−|↓↓↓↑)

|βv=½(|↑↓↓↓−|↓↑↓↓+|↓↓↑↓−|↓↓↓↑)

|γv=½(|↑↓↓−|↓↑↓↓−|↓↓↑↓+|↓↓↓↑)

We assume uncorrelated noise at each of the four 51V spins and apply a pure-dephasing master equation model. In the single excitation subspace, this becomes:

\(\text{?} = {2\Gamma\text{[𝒟(↑↓↓↓)(↑↓↓)+𝒟(↓↑↓↓)(↓↑↓↓)+}\text{𝒟(↓↓↑↓)(↓↓↑↓)+𝒟(↓↓↓↑)(↓↓↑)]ρ}}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

where the dephasing channel (Lindbladian) is given by)

(â)ρ=âρâ†−½{â†â,ρ}

and Γ is the dephasing rate on the ωc transition of a single 51V spin. We solve this equation for different initial states ρ(0). When ρ(0)=|0v0v|, dephasing does not contribute to T1(0), i.e. ρ(t)=ρ(0). However, when ρ(0)=|WvWv| the state evolves according to

ρ(t)=|WvWv|e−2Γt+¼(1−e−2Γt)1(SEM)

where 1(SEM) is the single excitation manifold identity operator:

1(SEM)=|WvWv|+|αvαv|+|βvβv|+|γvγv|

i.e. dephasing leads to decay of |Wv into 1(SEM) at rate 2Γ. For completeness we also consider the decay of the off-diagonal coherence term ρ01=0v|ρ|Wv and find that

ρ01(t)=ρ01(0)e−Γt.

Essentially, the pure dephasing model predicts T2*=2T1(W) for our system.

We verify that dephasing is the main source of |Wv population decay by demonstrating lifetime extension using the same motional narrowing approach employed to improve the coherence time. Specifically, during the wait time, we apply a series of π pulses to the 171Yb separated by 6 μs leading to an extended lifetime of T1(W)=127±8 μs (FIG. 12a). We note that both the bare and motionally-narrowed T1(W) and T2* times are close to the T2*=2T1(W) limit identified above. We further extend the T1(W) lifetime to 640±20 μs using two 51Vπ pulses applied during the wait time, thereby achieving dynamical decoupling from the nuclear Overhauser field (equivalent to the results in FIG. 3c).

Finally we note that if T1(W) is limited by the 171Yb Knight field as a common noise source, there may be some discrepancy in the predictions of this model due to a high degree of noise correlation between the four 51V register spins arising from lattice symmetry. However, when performing motional narrowing we decouple the 171Yb Knight field and are likely limited by the, considerably less correlated, local Overhauser field.

k. Parity Oscillations and Coherence

Here we derive an expression for the 171Yb 51V Bell-state coherence ρ01=1g0v|ρ|0gWv in terms of the parity oscillation contrast with a correction factor. In particular, when reading out this coherence, we apply a √{square root over (swap)} gate which maps |Ψ+=½(|1g0v−i|0gWv) to |0gWv and |Ψ−=½(|1g0v+i|0gWv) to |1g0v. Note that reading out the 171Yb state is sufficient to distinguish the |Ψ+ and |Ψ− states in this measurement. We can account for the readout fidelity of the |Ψ± states by using a √{square root over (,1)} factor (Methods), i.e. if the state |Ψ+(|Ψ− ) is perfectly prepared, 171Yb will be measured in state |0g(|1g) with probability ½(1+√{square root over (,1)}). To span the 171Yb-51V Hilbert space, we also need to consider the effect of the readout √{square root over (swap)} gate when the system is initialised into the other two states: |1gWv or |0g0v. To this end, we assign imperfect readout probabilities of q11 and q00 for |1gWv and |0g0v, respectively. Specifically, we can represent the dependence of the parity readout on the input state using the following matrix relation:

\(\begin{pmatrix}
p_{1,{Yb}} \\
p_{0,{Yb}}
\end{pmatrix} = {\mathcal{M}_{swap}{\mathcal{M}_{wait}\begin{pmatrix}
p_{11} \\
p_{\Psi^{+}} \\
p_{\Psi^{-}} \\
p_{00}
\end{pmatrix}}}\)
\(with\)
\(\mathcal{M}_{swap} = \begin{pmatrix}
q_{11} & {\frac{1}{2}\left( {1 - \sqrt{\mathcal{F}_{{sw},1}}} \right)} & {\frac{1}{2}\left( {1 + \sqrt{\mathcal{F}_{{sw},1}}} \right)} & {1 - q_{00}} \\
{1 - q_{11}} & {\frac{1}{2}\left( {1 + \sqrt{\mathcal{F}_{{sw},1}}} \right)} & {\frac{1}{2}\left( {1 - \sqrt{\mathcal{F}_{{sw},1}}} \right)} & q_{00}
\end{pmatrix}\)
\(\mathcal{M}_{wait} = {\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & {\cos^{2}\left( {\text{?}t/2} \right)} & {\sin^{2}\left( {\text{?}t/2} \right)} & 0 \\
0 & {\sin^{2}\left( {\text{?}t/2} \right)} & {\cos^{2}\left( {\text{?}t/2} \right)} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.}\)
\(\text{?}\text{indicates text missing or illegible when filed}\)

Here p1,Yb and p0,Yb are the probabilities of measuring the 171Yb qubit in |1g and |0g, respectively, and pΨ=Ψ±|ρ|Ψ± are the probabilities of being in the |Ψ± Bell states. The contrast Cparity of the parity oscillation between |105 + and |Ψ− is extracted by measuring the difference in the 171Yb|1g populations measured at t=0 and t=π/ωc, allowing us to estimate the Bell state coherence as |ρ01|=Cparity/2√{square root over (,1)}. This implies that uncorrected and corrected Bell state coherence values differ by a factor of √{square root over (,1)}=0.72. Using the results presented in FIG. 4b we obtain corrected and uncorrected estimates for |ρ01| of 0.35.2±0.004 and 0.254±0.003 respectively.

1. Bell State Fidelity Error Analysis

To extract the Bell state fidelity and uncertainty, we perform a maximum likelihood analysis of the population and parity oscillation measurements, adopting a similar approach as in [13]. The population measurement involves a series of n experiments with outcomes distributed between the four population states: {n00, n01, n10, n11} where n=00+n01+n10+n11. The likelihood function for the uncorrected populations, {p00, p01, p10, p11} has multinomial form:

\({\mathcal{L}\left( \left\{ p_{ij} \right\} \middle| \left\{ n_{ij} \right\} \right)} = {\frac{n!}{{n_{00}!}{n_{01}!}{n_{10}!}{n_{11}!}}p_{00}^{n_{00}}p_{01}^{n_{01}}p_{10}^{n_{10}}p_{11}^{n_{11}}}\)

where we have assumed a prior uniform over the physical values of {pij}, i.e. 0≤pij≤1 and Σpij=1. The likelihood function for the corrected populations, {c00, c01, c10, c11}, is obtained by substituting equation (11) into equation (S35) and assuming a prior uniform over the physical values of {cij}, i.e. 0≤cij≤1 and Σcij=1. Corrected populations are obtained by maximising this likelihood function. The error for a specific population (say c00) is obtained by marginalising ({cij}|{nij}) over the other three (c01, c10, c11) and taking a 68% symmetric confidence interval.

We extract a likelihood function for the coherence by considering the following model:

yi=0.5+√{square root over (,i)}ρ01 cos(ωcti)+ϵi

where {ti,yi} are the parity oscillation data at the ith point, ρ01 is the corrected coherence, sw,1 is the parity oscillation correction factor associated with the swap gate infidelity, and ϵi is the experimental error assumed to be normally distributed with μ=0 and unknown σ. The likelihood function is given by

\({\mathcal{L}\left( {\rho_{01},\left. \sigma \middle| \left\{ {t_{i},y_{i}} \right\} \right.} \right)} = {\prod\limits_{i}{\frac{1}{\sqrt{2\pi}\sigma}{{\exp\left\lbrack \frac{\left( {y_{i} - 0.5 - {\sqrt{\mathcal{F}_{{sw},1}}\rho_{01}\cos\left( {\omega_{c}t_{i}} \right)}} \right)^{2}}{2\sigma^{2}} \right\rbrack}.}}}\)

We obtain a likelihood for the corrected coherence, (ρ01|{ti,yi}) by marginalising over σ.

The likelihood function for the fidelity is obtained by taking a product of the likelihood function for the populations with the likelihood function for the coherence and evaluating a contour integral at constant , given as

\({\mathcal{L}(\mathcal{F})} = {\int_{\mathcal{F}}{{\mathcal{L}\left( \left\{ c_{ij} \right\} \middle| \left\{ n_{ij} \right\} \right)}{\mathcal{L}\left( \rho_{01} \middle| \left\{ {t_{i},y_{i}} \right\} \right)}d\rho_{01}{\prod\limits_{ij}{{dc}_{ij}.}}}}\)

The Bell state fidelity is extracted by maximising this likelihood and the error is evaluated as a symmetric 68% confidence interval.

Hardware Environment

FIG. 15 is an exemplary hardware and software environment 1500 (referred to as a computer-implemented system and/or computer-implemented method) used to implement one or more embodiments of the invention. The hardware and software environment includes a computer 1502 and may include peripherals. Computer 1502 may be a user/client computer, server computer, or may be a database computer. The computer 1502 comprises a hardware processor 1504A and/or a special purpose hardware processor 1504B (hereinafter alternatively collectively referred to as processor 1504) and a memory 1506, such as random access memory (RAM). The computer 1502 may be coupled to, and/or integrated with, other devices, including input/output (I/O) devices such as a keyboard 1514, a cursor control device 1516 (e.g., a mouse) a pointing device, pen and tablet, touch screen, multi-touch device, etc.) and a printer 1528. In one or more embodiments, computer 1502 may be coupled to, or may comprise, a portable or media viewing/listening device 1532. In yet another embodiment, the computer 1502 may comprise a multi-touch device, mobile phone, or other internet enabled device executing on various platforms and operating systems.

In one embodiment, the computer 1502 operates by the hardware processor 1504A performing instructions defined by the computer program 1510 under control of an operating system 1508. The computer program 1510 and/or the operating system 1508 may be stored in the memory 1506 and may interface with the user and/or other devices to accept input and commands and, based on such input and commands and the instructions defined by the computer program 1510 and operating system 1508, to provide output and results.

Output/results may be presented on the display 1522 or provided to another device for presentation or further processing or action. The image may be provided through a graphical user interface (GUI) module 1518. Although the GUI module 1518 is depicted as a separate module, the instructions performing the GUI functions can be resident or distributed in the operating system 1508, the computer program 1510, or implemented with special purpose memory and processors.

Some or all of the operations performed by the computer 1502 according to the computer program 1510 instructions may be implemented in a special purpose processor 1504B. In this embodiment, some or all of the computer program 1510 instructions may be implemented via firmware instructions stored in a read only memory (ROM), a programmable read only memory (PROM) or flash memory within the special purpose processor 1504B or in memory 1506. The special purpose processor 1504B may also be hardwired through circuit design to perform some or all of the operations to implement the present invention. Further, the special purpose processor 1504B may be a hybrid processor, which includes dedicated circuitry for performing a subset of functions, and other circuits for performing more general functions such as responding to computer program 1510 instructions. In one embodiment, the special purpose processor 1504B is an application specific integrated circuit (ASIC) or field programmable gate array (FPGA). In other examples, special purpose processor may comprise a graphics processing unit (GPU).

The computer 1502 may also implement a compiler 1512 that allows an application or computer program 1510 written in a programming language such as C, C++, Assembly, SQL, PYTHON, PROLOG, MATLAB, RUBY, RAILS, HASKELL, or other language to be translated into processor 1504 readable code. Alternatively, the compiler 1512 may be an interpreter that executes instructions/source code directly, translates source code into an intermediate representation that is executed, or that executes stored precompiled code. Such source code may be written in a variety of programming languages such as JAVA, JAVASCRIPT, PERL, BASIC, etc. After completion, the application or computer program 1510 accesses and manipulates data accepted from I/O devices and stored in the memory 1506 of the computer 1502 using the relationships and logic that were generated using the compiler 1512.

The computer 1502 also optionally comprises an external communication device such as a modem, satellite link, Ethernet card, or other device for accepting input from, and providing output to, other computers 1502.

In one embodiment, instructions implementing the operating system 1508, the computer program 1510, and the compiler 1512 are tangibly embodied in a non-transitory computer-readable medium, e.g., data storage device 1520, which could include one or more fixed or removable data storage devices, such as a zip drive, floppy disc drive 1524, hard drive, CD-ROM drive, tape drive, etc. Further, the operating system 1508 and the computer program 1510 are comprised of computer program 1510 instructions which, when accessed, read and executed by the computer 1502, cause the computer 1502 to perform the steps necessary to implement and/or use the present invention or to load the program of instructions into a memory 1506, thus creating a special purpose data structure causing the computer 1502 to operate as a specially programmed computer executing the protocol or method steps described herein. Computer program 1510 and/or operating instructions may also be tangibly embodied in memory 1506 and/or embodied in or coupled to source 1530 of the pulses 202 comprising electromagnetic fields (e.g., 1530 may comprise sources 500, 506), thereby making a computer program product or article of manufacture according to the invention. As such, the terms “article of manufacture,” “program storage device,” and “computer program product,” as used herein, are intended to encompass a computer program accessible from any computer readable device or media. Computer 1500 may comprise or be coupled to 1530.

Of course, those skilled in the art will recognize that any combination of the above components, or any number of different components, peripherals, and other devices, may be used with the computer 1502.

FIG. 16 schematically illustrates a typical distributed/cloud-based computer system 1600 using a network 1604 to connect client computers 1602 to server computers 1606. A typical combination of resources may include a network 1604 comprising the Internet, LANs (local area networks), WANs (wide area networks), SNA (systems network architecture) networks, or the like, clients 1602 that are personal computers or workstations (as set forth in FIG. 15), and servers 1606 that are personal computers, workstations, minicomputers, or mainframes (as set forth in FIG. 15). However, it may be noted that different networks such as a cellular network (e.g., GSM [global system for mobile communications] or otherwise), a satellite based network, or any other type of network may be used to connect clients 1602 and servers 1606 in accordance with embodiments of the invention.

A network 1604 such as the Internet connects clients 1602 to server computers 1606. Network 1604 may utilize ethernet, coaxial cable, wireless communications, radio frequency (RF), etc. to connect and provide the communication between clients 1602 and servers 1606. Further, in a cloud-based computing system, resources (e.g., storage, processors, applications, memory, infrastructure, etc.) in clients 1602 and server computers 1606 may be shared by clients 1602, server computers 1606, and users across one or more networks. Resources may be shared by multiple users and can be dynamically reallocated per demand. In this regard, cloud computing may be referred to as a model for enabling access to a shared pool of configurable computing resources.

Clients 1602 may execute a client application or web browser and communicate with server computers 1606 executing web servers 1610. Such a web browser is typically a program such as MICROSOFT INTERNET EXPLORER/EDGE, MOZILLA FIREFOX, OPERA, APPLE SAFARI, GOOGLE CHROME, etc. Further, the software executing on clients 1602 may be downloaded from server computer 1606 to client computers 1602 and installed as a plug-in or ACTIVEX control of a web browser. Accordingly, clients 1602 may utilize ACTIVEX components/component object model (COM) or distributed COM (DCOM) components to provide a user interface on a display of client 1602. The web server 1610 is typically a program such as MICROSOFT'S INTERNET INFORMATION SERVER.

Web server 1610 may host an Active Server Page (ASP) or Internet Server Application Programming Interface (ISAPI) application 1612, which may be executing scripts.

Generally, these components 1600-1616 all comprise logic and/or data that is embodied in/or retrievable from device, medium, signal, or carrier, e.g., a data storage device, a data communications device, a remote computer or device coupled to the computer via a network or via another data communications device, etc. Moreover, this logic and/or data, when read, executed, and/or interpreted, results in the steps necessary to implement and/or use the present invention being performed.

Although the terms “user computer”, “client computer”, and/or “server computer” are referred to herein, it is understood that such computers 1602 and 1606 may be interchangeable and may further include thin client devices with limited or full processing capabilities, portable devices such as cell phones, notebook computers, pocket computers, multi-touch devices, and/or any other devices with suitable processing, communication, and input/output capability.

Of course, those skilled in the art will recognize that any combination of the above components, or any number of different components, peripherals, and other devices, may be used with computers 1602 and 1606. Embodiments of the invention are implemented as a software protocol application on a client 1602 or server computer 1606. Further, as described above, the client 1602 or server computer 1606 may comprise a thin client device or a portable device that has a multi-touch-based display.

Process Steps

Method of Making a Register

FIG. 17A illustrates a method of making a system for implementing a quantum register. The method comprises the following steps.

Block 1700 represents obtaining or providing a device 1500 for coupling a qubit to a register. The device comprises one or more circuits or a computer 1502 configured to control a protocol 200 comprising a sequence 201 of pulses 202 synchronized with an RF field 204. Controlling the protocol comprises configuring (e.g., selecting, setting, or programming) a timing (e.g., spacing; σ/4 relative to other pukes and RF field), a phase (+/−x, +/−y), and a duration (pi, pi/2) of each of the pulses comprising a single qubit gate, a period τ, 210, and amplitude BRF of the RF field, and a number of cycles M of the sequence, so that application of the protocol 200 controls a coherent spin exchange interaction {tilde over (Ŝ)}+Î−+{tilde over (Ŝ)}−Î+ between a register 206 and a qubit 208 having a zero magnetic dipole moment.

In one or more embodiments, the device comprises at least one of a signal generator, arbitrary waveform generator (e.g., comprising FPGA and digital to analog converter), or amplifier comprising the one or more circuits (e.g., as an embedded circuit or processor) outputting control signals that are used to control the output of the pulses (comprising the electromagnetic fields) and the RF field from one or more sources (e.g., lasers, microwave sources, or RF generator). In one or more examples, the sources of the pulses and RF field (e.g., the lasers) and microwave source(s) and RF source) comprise the one or more circuits, e.g., as an embedded system or processor, e.g., so as to form smart or programmable sources. The one or more circuits may be in central controller or distributed among the sources. In one or more examples, the arbitrary waveform generator (AWG) comprises the microwave sources and RF sources outputting the microwave pulses and RF field, and the AWG outputs the timing control signals to the laser sources.

In one or more examples, the device comprises a computer comprising or coupled to one or more processors; one or more memories; and one or more programs stored in the one or more memories, wherein the one or more programs executed by the one or more processors control the implementation of the protocol.

In one or more examples, the device comprises an application specific integrated circuit or field programmable gate array controlling the implementation of the protocol. In one or more examples, the one or more circuits comprise one or more timing circuits or a clock or a clock signal generator.

Block 1702 represents optionally coupling the device to one or more sources of electromagnetic fields. The one or more sources output the pulses comprising an electromagnetic field having a frequency (e.g., fg in FIG. 5a) tuned to excite a transition between the first spin state and the second spin state.

Block 1704 represents optionally coupling the one or more sources to a photonic cavity.

Block 1706 represents optionally coupling the one or more sources to the qubit coupled to the register, e.g., via the photonic crystal. In one or more examples the qubit and the register are coupled, combined, or integrated with the photonic cavity.

The qubit comprises a first spin state (e.g., |0g>) having a zero magnetic dipole moment and a second spin state (e.g., |1g> having a zero magnetic dipole moment). The register comprises multiple register spins 100 having an energy level structure 102, wherein the register spins are indistinguishable so as to be configurable in basis states including a superposition state |Wv> used for storing the quantum state of the qubit.

A variety of systems including, but not limited to, solid state materials, can be used to implement the qubit and the register. In one example, the system comprises a spin carrying defect (e.g., an ion or nitrogen vacancy) in a host lattice (e.g., a crystal), wherein the spin carrying defect comprises the qubit and the host lattice comprises the register. Various rare earth doped crystals can be used. In one or more examples, the qubit ion comprising the qubit is Yb, Er, or Eu doped in a host crystal comprising register ions 122 surrounding the qubit ion. Examples include, but are not limited to, Yb:YVO (as described in the first example), Er:Y2SiO5, or Eu:Y2SiO5). In another example, the system comprise a quantum dot in a host lattice, wherein the quantum dot (e.g., InGaAs or other semiconductor quantum dot) comprises the qubit and the host lattice (e.g., InGaAs or other semiconductor) comprises the register.

Block 1708 represents optionally coupling the qubit to a detector.

Block 1710 represents the end result, a system for coupling the qubit to a register. The system can be embodied in many ways, including, but not limited to, the following examples.

1. FIG. 15, FIG. 2, and FIG. 1 illustrate examples of a means for, or a device 1500 for coupling a qubit to a register, comprising a circuit or computer 1502 controlling a protocol 200 comprising a sequence 201 of pulses 202 synchronized with an RF field 204. Controlling the protocol comprises configuring (e.g., selecting, setting, or programming) a timing (e.g., spacing τ/4 relative to other pulses and RF field), a phase (+/−x., +/−y), and a duration (pi, pi/2) of each of the pulses comprising a single qubit gate, a period T and amplitude BRF of the RF field, and a number of cycles M of the sequence, so that application of the protocol 200 controls a coherent spin exchange interaction (e.g., {tilde over (Ŝ)}+Î−+{tilde over (Ŝ)}−Î+) between a register 206 and a qubit 208 having a zero magnetic dipole moment: The qubit comprises a first spin state (e.g., |0g>) having a zero magnetic dipole moment and a second spin state (e.g., |1g> having a zero magnetic dipole moment. The register comprises multiple register spins 100 having an energy level structure 102, wherein the register spins are indistinguishable so as to be configurable in basis states including a superposition state |Wv> used for storing the quantum state of the qubit.

2. The device of example 1, wherein the protocol is configured to:

suppress or cancel one or more non-exchange interactions between the register and the qubit,

suppress or cancel noise coupled to the qubit and causing decoherence of a quantum state of the qubit,

enable the coherent spin exchange interaction that performs a quantum logic gate (e.g., a Clifford gate Ur as illustrated in FIG. 6), coherently transferring a quantum state of the qubit between the register and qubit.

The non-exchange interactions arise when the SxIx interaction is expressed in a form comprising spin preserving parts (spin exchange) and also non spin preserving parts (corresponding to the non-exchange interaction).

3. FIG. 17B illustrates an example wherein of the device of example 1 or 2, wherein the circuit controls:

application of a period of the protocol within a time period shorter than a rate of change of a magnetic noise (e.g., Overhauser field), so that the magnetic noise is quasistatic during the application of the period of protocol, the magnetic noise causing qubit decoherence and inducing a second order interaction (incoherent or random interaction) between the qubit and the register; and

at least one of a phase, duration, or time spacing of the pulses in the period so that:


- - one or more spin exchange interactions induced by the RE field are
    preserved or maintained across the period;
  - one or more non-exchange interactions induced by the RE field are
    cancelled across the period (e.g., components of the non exchange
    interactions induced at different time instances in the period
    cancel each other, or average to zero, over the period);
  - one or more (or any) exchange and one or more (or any) non-exchange
    interactions induced by the magnetic noise are cancelled across the
    period (e.g., components of these interactions induced at different
    time instances in the period cancel each other, or average to zero,
    over the period); and
  - the qubit decoherence induced by the magnetic noise is cancelled
    over the period (e.g., decoherence induced at different time
    instances in the period cancel each other, or average to zero, over
    the period);
  - the RE field toggling between two values **214** of equal magnitude
    and opposite polarity such that:
    - the period is associated with a frequency of a precession of each
      of the multiple register spins about a predetermined quantization
      axis (e.g., determined by an electric field gradient generated by
      the host lattice at zero magnetic field, or the application of a
      magnetic field); and
    - the amplitude is selected for a predetermined magnitude of the
      coherent spin exchange interaction between the register spins and
      qubit; and

so as to form a predictable (e.g., controllable, non random, deterministic) and coherent spin exchange interaction.

4. The device of any of the examples 1-3, wherein each of the single qubit gates comprises one of the pulses having the frequency (e.g., fg in FIG. 5a) and duration (e.g., pi or pi/2) tuned to drive a transition between the first spin state and the second spin state.

6. The device of any of the examples claim 1-5 comprising a quantum memory 104 wherein the circuit:

controls application of the protocol in combination with are initialization of the qubit so as to configure the register spins in a polarized state |0v>;

controls application of one or more of the pulses to set a quantum state 106 of the qubit; and

controls application of the protocol so as to apply a first swap gate 108 (two qubit gate) transferring the quantum state of the qubit from the qubit to the register, thereby changing the polarized state to a corresponding state 110 of the register spins corresponding to the quantum state; and.

apply a second swap gate 112 retrieving the quantum state in the qubit from the register, thereby changing the corresponding state of the register spins to the polarized state.

6. The device of any of the examples 1-5, wherein configuring the register spins in the polarized state comprises polarizing the register, which is initially in an unpolarized state comprising any configuration of excitations of the register spins, by:

(a) initializing the qubit in the first spin state by controlling application of one or more initialization pulses of one or more initialization electromagnetic fields having one or more frequencies e.g., A, F, and fe in FIG. 5a) and tuned to initialize the quantum state of the qubit in the first spin state;

(d) applying the protocol transferring a spin excitation from the register spins to the qubit; and

(e) repeating steps (a) and (b) until all excitations of the register spins are transferred from the register to the qubit and the register spins are initialized in the polarized state, as characterized by a measurement of the qubit remaining in the first spin state after step (b).

The device of example 5 or 6, wherein the circuit controls application of the protocol so as to apply the first swap gate mapping (via the coherent spin exchange interaction) between the qubit and the register, such that:

if the qubit is in the first spin state, the corresponding state of the register is the polarized state |0v>,

if the qubit is in the second spin state, the corresponding state of the register is a W state |Wv>, and

if the qubit is in a superposition of the first spin state and the second spin state, the corresponding state of the register is a superposition 110 of the polarized state and the W state, and

wherein the W state is a superposition of all single spin excitation states of the register spins.

8. The device of any of the examples 1-7, wherein the circuit:

controls application of the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized state;

controls application of one or more of the pulses to set a quantum state of the qubit;

controls application of the protocol so as to apply a first square root of swap gate entangling the qubit with the register so as to form a Bell state; and

controls application of the protocol so as to apply a second square root of swap gate interacting with the Bell state so as to perform a measurement of the Bell state.

9. A repeater in a quantum network comprising the device of example 8.

10. FIG. 1, FIG. 2, and FIG. 5 illustrate an example of a system 112 comprising the device 1500 of any of the examples 1-9, further comprising:

a photonic cavity 114 coupled to a solid state material comprising the qubit and the register;

one or more microwave sources 500, 502 coupled to the qubit via a microwave waveguide, the microwave sources outputting one or more first microwave pulses fe and/or one or more second microwave pulses fg;

a radio frequency source 504 outputting the RE field; and

one or more laser sources 506, 508 outputting one or more laser pulses coupled to the qubit through the photonic cavity; and wherein:

the circuit controls the one or more laser sources and the one or more microwave sources so as to:

output initialization pulses comprising at least one of the one or more laser pulses A, F, or the one or more first microwave pulses fe having initialization frequencies for exciting one or more transitions initializing the qubit;

apply the protocol 200 comprising the single qubit gates comprising the second microwave pulses in synchronization with the RE field; and

output one or more readout electromagnetic fields having a readout frequency A for exciting a readout transition from the second spin state to a readout state |0e>, so as to stimulate output of readout pulses 116 from the readout state.

11. The device of any of the examples 1-10, wherein:

the pulses each comprise a pi pulse or a pi/2 pulse having at least one phase selected from +x, −x, +y, or −y, and

the circuit controls:

the sequence such that the period of the RF field is 2τ and a spacing of the pulses is τ/4, and

for a given magnitude of the spin exchange interaction determined by the amplitude of the RF field, a number of repeats M of the protocol that applies at least one of a swap gate transferring a quantum state between the qubit and the register, a square root of a swap gate for forming or measuring a Bell state, or that can be used to polarize the spins into a polarized state in combination with an initialization of the qubit.

12. The device of any of the examples 1-11 wherein the circuit selects and sets the duration and the timing of each of the pulses and a toggling of the RF field to engineer the coherent spin-exchange interaction comprising:

{tilde over (Ŝ)}+Î−+{tilde over (Ŝ)}−Î+,

where {tilde over (Î)}+=|↑↓|,{tilde over (Î)}−=|↓↑| are the raising and lowering operators in an effective nuclear two-level manifold of the multiple spins in the register and {tilde over (Ŝ)}+ are similarly defined for the qubit.

13. The device of any of the examples, wherein:


- - the RF field induces an interaction between the qubit and the
    register comprising S_(z)I_(z) and at least one of S_(x)I_(x) or
    S_(y)I_(y) including exchange and non-exchange components, where Sx,
    Sy, Sx are the spin operators for the qubit ion and Ix, Iy, Iz are
    the spin operators for the register ions along the x, y, z cartesian
    axes respectively,
  - the control circuit applies the protocol that engineers the
    interaction comprising only the coherent spin exchange interaction
    by causing a cancelation of any non-exchange components over the
    period, and
  - the pulses are synchronized with a precession of the register ions
    about a predetermined quantization axis.

14. FIG. 2 illustrates an example of the device of any of the examples 1-13, wherein the RF field comprises a square wave and the sequence of pulses comprise:

in a first half period τ of the square wave a sequence of the second pulses comprising:

a first pi/2 pulse having a phase +Y followed by a first pi pulse having a phase +Y, the beginning of the first pi/2 pulse and the center of the first pi pulse separated in time by τ/4;

a second pi/2 pulse immediately followed by a third pi/2 pulse, the end of the second pi/2 pulse separated in time from the center of the first pi pulse by τ/4, wherein the second pi/2 pulse has a phase −Y and the third pi/2 pulse has a phase −X;

a second pi pulse having a phase −X and following the third pi/2 pulse, a center of the second pi puke separated in time from the center of the first pi pulse by τ/2; and

a fourth pi/2 pulse having a phase −X, wherein the end of the fourth pi/2 pulse is separated in time from center of the second pi pulse by τ/4; and

in a second half period τ of the square wave, a repeat of the sequence of second pulses but wherein the first pi/2 pulse, the first pi pulse, and the second pi/2 pulse have opposite phase as compared to the first pi/2 pulse, the first pi pulse, and the second pi/2 puke in the first half period, respectively.

15. The device of any of the examples 1-14, wherein the protocol de-couples the qubit from decoherence noise and random interactions caused by a nuclear Overhauser field generated by a host lattice 118 in which the qubit is located.

16. A system 112 for implementing a quantum register comprising the device of any of the examples claim 1-15 coupled to:

a spin carrying defect 120 in a host lattice, wherein the spin carrying defect comprises the qubit and the host lattice 118 comprises the register, or

a quantum dot in a host lattice, wherein the quantum dot comprises the qubit and the host lattice comprises the register.

17. The system of claim 16, wherein the spin carrying defect is a qubit ion comprising the qubit and the register comprises a lattice 118 of register ions 122 surrounding the qubit

18. The device of any of the examples 1-17, wherein the multiple register spins 100 in the register comprise nuclear spins and the first spin state and the second spin state comprise electron spin states.

19. The device of any of the examples, wherein the protocol controls oscillations between a first system state |1g>|0v>, representing a spin excitation in the qubit and register ions in the polarized state, and a second system state |0g>|W> where |W> is an entangled |W> spin state of the register comprising the spin excitation transferred from the qubit.

20. A protocol 200 for controlling a coherent spin exchange interaction between a register and a qubit having a zero magnetic dipole moment, wherein the qubit comprises a first spin state and a second spin state both having zero magnetic dipole moment; and the register comprises multiple indistinguishable spins. The protocol comprises a toggling RF field or magnetic field synchronized to a sequence of pulses, wherein a period (e.g. 2T) of the toggling RF field or magnetic field is matched to a spacing (e.g., T/4) of the pulses comprising single qubit gates (e.g., clifford gates performing unitary operations) and the protocol modulates the spin exchange interaction so as to transfer quantum information to or from the qubit.

21. The protocol of any of the examples, wherein the spin exchange interaction comprises an interaction between an electron spin of the qubit and a nuclear spin of the register (e.g., electron-nuclear dipole interaction) or an interaction between electron spins of the qubit and the register. Block 1712 represents optionally coupling the system in or to an application, e.g., in or to a quantum computer, in or to a quantum network, or in repeater for a quantum network.

22. The protocol of any of the examples 1-21, wherein the RE field comprises or is a magnetic field or the radio frequency (RF) field has a frequency in range 20 kHz-300 GHz.

Method of Performing: Qubit Operations with a Controlled Spin Exchange Interaction

FIG. 18 is a flowchart illustrating a method for coupling a qubit to a quantum register.

Block 1800 represents obtaining a protocol comprising a sequence of pukes synchronized with an RF field, the protocol further comprising a timing, a phase, and a duration of each of the pukes comprising a single qubit gate, and a period and amplitude of the RF field, wherein application of the protocol controls a coherent spin exchange interaction between a register and a qubit.

Block 1802 represents applying one or more cycles of the protocol to the qubit, so as to modulate the coherent spin exchange interaction transferring a spin excitation between the qubit and the register. The qubit comprises a first spin state and a second spin state both having a zero magnetic dipole moment, the register spins are indistinguishable so as to be configurable in basis states including a superposition state used for storing a quantum state of the qubit; and the pulses comprise an electromagnetic field tuned to excite a transition between the first spin state and the second spin state.

1. Quantum Memory

FIG. 19 illustrates a method of applying a number of cycles of the protocol so as transfer quantum information between the qubit and the register.

Block 1900 represents applying a first number of the cycles of the protocol to the qubit in combination with an initialization of the qubit so as to configure the register spins in a polarized state.

Block 1902 represents applying one or more of the pulses to the qubit to set a quantum state of the qubit.

Block 1904 represents applying a second number of the cycles of the protocol to the qubit so as to apply a first swap gate (two qubit gate) transferring a quantum state of the qubit from the qubit to the register, thereby changing the polarized state to a corresponding state of the register spins corresponding to the quantum state.

Block 1906 represents applying one or more cycles of the protocol to the qubit so as to apply a second swap gate retrieving the quantum state in the qubit from the register, thereby changing the corresponding state of the register spins to the polarized state.

2. Bell State measurement

FIG. 20 is a flowchart illustrating a method of forming and measuring Bell states. The method comprises the following steps.

Block 2000 represents applying a first number of the cycles of the protocol in combination with an initialization of the qubit so as to configure the register spins in a polarized w state.

Block 2002 represents applying one or more of the pulses to the qubit to set a quantum state of the qubit.

Block 2004 represents applying a second number of the cycles of the protocol to the qubit so as to apply a first square root of swap gate entangling the qubit with the register so as to form a Bell state.

Block 2006 represents applying one or more cycles of the protocol to the qubit so as to apply a second square root of swap gate interacting with the Bell state so as to perform a measurement of the Bell state.

## Definitions

As known to a person skilled in the art, a pi pulse may refer to a pulse of light (e.g., laser) or microwaves generally resonant with a transition between two levels, the pulse being calibrated via known methods to move the population/excitation fully from one level to another.

Accordingly, an optical pi pulse is a .pi. pulse in the optical (e.g., visible) domain/frequencies, and a microwave pi pulse is a .pi. pulse in the microwave domain/frequencies. It should be noted that a pi pulse can move (transfer) population/excitations with a probability of 1, so as to change the state of the qubit between the two spin states 0g and 1g, whereas as a non-pi pulse can transfer population/excitations with some probability between 0 and 1, and not necessarily 1, so as to form the qubit comprising a superposition of the spin states 0g and 1g.

In one or more examples, a spin-exchange interaction preserves total angular momentum of the system but may allow other aspects of the system to change. When two spins in the qubit and register experience a spin-exchange interaction, the total spin of the qubit-register system is preserved yet the orientation of the individual spins in the register and qubit may change. For example, if qubit A and register B are in opposite spin states, a spin-exchange interaction reverses the spins

A(↑)+B(↓)→A(↓)+B(↑)

## CONCLUSION

This concludes the description of the preferred embodiment of the present invention. The foregoing description of one or more embodiments of the invention has been presented for the purposes of illustration and description. It is not intended to be exhaustive or to limit the invention to the precise form disclosed. Many modifications and variations are possible in light of the above teaching. It is intended that the scope of the invention be limited not by this detailed description, but rather by the claims appended hereto.

