# DESCRIPTION

## BACKGROUND

Quantum computing utilizes the laws of quantum physics to process information. Quantum physics is a theory that describes the behavior of reality at the fundamental level. It is currently the only physical theory that is capable of consistently predicting the behavior of microscopic quantum objects like photons, molecules, atoms, and electrons.

A quantum computer is a device that utilizes quantum mechanics to allow one to write, store, process and read out information encoded in quantum states, e.g. the states of quantum objects. A quantum object is a physical object that behaves according to the laws of quantum physics. The state of a physical object is a description of the object at a given time.

In quantum mechanics, the state of a two-level quantum system, or simply, a qubit, is a list of two complex numbers whose squares sum up to one. Each of the two numbers is called an amplitude, or quasi-probability. The square of an amplitude gives a potentially negative probability. Hence, each of the two numbers correspond to the square root that event zero and event one will happen, respectively. A fundamental and counterintuitive difference between a probabilistic bit (e.g. a traditional zero or one bit) and the qubit is that a probabilistic bit represents a lack of information about a two-level classical system, while a qubit contains maximal information about a two-level quantum system.

Quantum computers are based on such quantum bits (qubits), which may experience the phenomena of “superposition” and “entanglement.” Superposition allows a quantum system to be in multiple states at the same time. For example, whereas a classical computer is based on bits that are either zero or one, a qubit may be both zero and one at the same time, with different probabilities assigned to zero and one. Entanglement is a strong correlation between quantum particles, such that the quantum particles are inextricably linked in unison even if separated by great distances.

A quantum algorithm is a reversible transformation acting on qubits in a desired and controlled way, followed by a measurement on one or multiple qubits. For example, if a system has two qubits, a transformation may modify four numbers; with three qubits this becomes eight numbers, and so on. As such, a quantum algorithm acts on a list of numbers exponentially large as dictated by the number of qubits. To implement a transform, the transform may be decomposed into small operations acting on a single qubit, or a set of qubits, as an example. Such small operations may be called quantum gates and the arrangement of the gates to implement a transformation may form a quantum circuit.

There are different types of qubits that may be used in quantum computers, each having different advantages and disadvantages. For example, some quantum computers may include qubits built from superconductors, trapped ions, semiconductors, photonics, etc. Each may experience different levels of interference, errors and decoherence. Also, some may be more useful for generating particular types of quantum circuits or quantum algorithms, while others may be more useful for generating other types of quantum circuits or quantum algorithms. Also, costs, run-times, error rates, availability, etc. may vary across quantum computing technologies.

For some types of quantum computations, such as fault tolerant computation of large scale quantum algorithms, overhead costs for performing such quantum computations may be high. For example for types of quantum gates that are not naturally fault tolerant, the quantum gates may be encoded in error correcting code. However this may add to the overhead number of qubits required to implement the large scale quantum algorithms. Also, performing successive quantum gates, measurement of quantum circuits, etc. may introduce probabilities of errors in the quantum circuits and/or measured results of the quantum circuits.

While embodiments are described herein by way of example for several embodiments and illustrative drawings, those skilled in the art will recognize that embodiments are not limited to the embodiments or drawings described. It should be understood, that the drawings and detailed description thereto are not intended to limit embodiments to the particular form disclosed, but on the contrary, the intention is to cover all modifications, equivalents and alternatives falling within the spirit and scope as defined by the appended claims. The headings used herein are for organizational purposes only and are not meant to be used to limit the scope of the description or the claims. As used throughout this application, the word “may” is used in a permissive sense (i.e., meaning having the potential to), rather than the mandatory sense (i.e., meaning must). Similarly, the words “include,” “including,” and “includes” mean including, but not limited to. When used in the claims, the term “or” is used as an inclusive or and not as an exclusive or. For example, the phrase “at least one of x, y, or z” means any one of x, y, and z, as well as any combination thereof.

## DETAILED DESCRIPTION

The present disclosure relates to methods and apparatus for reducing cross talk errors in quantum circuits/quantum algorithms that are fault-tolerant and that efficiently use resources.

In order to perform quantum computations, universal fault-tolerant quantum computers may be required to be built with the capability of implementing all gates from a universal gate set with low logical error rates. Further, the overhead cost for achieving such low error rates may need to be low. In order to achieve fault tolerance, surface codes are often used. However, such surface codes must also be fault tolerant and efficiently use resources.

In some embodiments, efficiently implementing a universal gate set and/or surface codes may involve multiple layers of a quantum computer/quantum algorithm. For example at a lowest layer, building blocks of a quantum computer may include nano-mechanical resonators that are controlled using an asymmetrically-threaded superconducting quantum interference device (asymmetrically-threaded SQUID or ATS). The nano-mechanical resonators may be configured to resonate at one or more frequencies and may be coupled to the ATS, wherein the ATS controls the phonic modes. Also the ATS may be coupled to a bandpass filter and then an open transmission line that enables photons from the ATS to be adsorbed by the environment. At a next level, error correction may be implemented for the quantum computer comprising nano-mechanical resonators and an ATS. For example error corrected codes may be built that utilize the ATS and phononic modes of the nano-mechanical resonators to detect and/or correct errors. At yet another level, gates may be implemented for the quantum computer using the error corrected codes as inputs or outputs to the gates. Also, qubits of the gates may be error corrected. At yet a higher level logical gates may be built that utilize one or more of the physical gates.

In some embodiments, for qubits of a surface code, one or more spurious photon dissipation processes of multiplexed control circuits (e.g. multiplexed ATSs) that control multiple phononic modes for qubits of the surface code that are implemented using multiple ones of the nano-mechanical resonators coupled to the multiplexed control circuit may give rise to cross-talk. Such cross talk may lead to stochastic errors induced by effective dissipators (type I errors), stochastic errors induced by effective Hamiltonians (type II errors), and/or coherent errors induced by effective Hamiltonians (type III errors). In some embodiments, a filter bandpass range of a filter included in the multiplexed control circuit (e.g. multiplexed ATS) may be selected such that type I and type II errors are suppressed. Moreover, strategic selection of phononic mode frequencies and detunings of dump modes of the multiplexed control circuits (e.g. multiplexed ATSs) may effectively suppress type III errors.

In some embodiments, cross talk errors introduced into measurements of stabilizers of a surface code may be corrected when decoding a measurement history using a matching graph and minimum weight perfect matching (MWPM). For example, in some embodiments, additional edges are added to the matching graph to identify and correct for errors introduced due to cross-talk.

Also, in some embodiments, a hybrid Bacon-Shor surface code may be used instead of a traditional surface code. The hybrid Bacon-Shor surface code may only require four phonic modes per given multiplexed control circuit (e.g. four phononic modes coupled to a given multiplexed ATS). This is in comparison to a traditional surface code that couples five phononic modes per multiplexed control circuit (e.g. five phononic modes coupled to a given multiplexed ATS). The reduction in coupling ratio of phononic modes per multiplexed control circuit (e.g. multiplexed ATS) may reduce probabilities of cross talk errors as compared to traditional surface codes.

### Asymmetrically Threaded Superconducting Quantum Interference Device (ATS)-Phononic Hybrid System

In some embodiments, a circuit for use in a quantum computer may comprise nano-mechanical linear resonators and an asymmetrically threaded superconducting quantum interference device (SQUID, ATS). The nano-mechanical resonators and ATS may implement qubits that are hybrid acoustic-electrical qubits, for example as opposed to electromagnetic qubits. In some embodiments, both the nano-mechanical resonators and ATS may be situated on a same component and may provide for easily extending a system to include additional components with additional nano-mechanical resonators that implement additional hybrid acoustic-electrical qubits. This may also enable scaling of a number of qubits needed for a quantum computer by including more or fewer components. Such an approach may allow for simpler extension and scaling than a system wherein components that implement qubits are integrated into a single chip, and newly designed chips are required to extend or scale the system to have more or fewer qubits. As used herein, the terms “mechanical”. “acoustic”, “phononic”, etc. may be used to describe mechanical circuits as opposed to electromagnetic circuits.

In some embodiments, more phononic resonators (e.g. nano-mechanical resonators) may be connected to a same control circuit, such as an ATS, than is possible for electromagnetic resonators. This is due, at least in part, to the smaller size of the phononic resonators as compared to electromagnetic resonators. However, in such systems cross-talk between the phononic resonators coupled to the same control circuit must be addressed in order to avoid errors. Multiplexed control of phononic resonators using a common control circuit, such as an ATS, is further discussed in detail below.

In some embodiments, a structure of a chip comprising phononic resonators may take the form of a planar circuit with metal components that form superconducting circuits, such as the ATS. The ATS may be physically connected via wire leads to very small (e.g. micron-sized or nano-sized) suspended mechanical devices, such as a linear nano-mechanical resonator. The suspended mechanical devices may be located on a same chip with the ATS circuit or may by located on a separate chip that has been heterogeneously integrated via a flip chip, or similar component, with a bottom chip comprising the ATS and/or additional suspended mechanical devices, e.g. other mechanical resonators.

In some embodiments, electrical connections to the ATS may be laid on top of a piezoelectric material that has been etched into a pattern to form the nano-mechanical resonators. In some embodiments, different variables, such as piezoelectric coefficient, density, etc. may affect how strongly coupled the ATS is to the mechanical resonators. This coupling may be expressed in terms of a phonon coupling rate in the Hamiltonian for the system.

When coupling a nano-structure, such as a nano-mechanical resonator, to an electrical circuit, very small capacitors are required since the nano-structure components, e.g. nano-mechanical resonators, are also very small. Typically in an electrical circuit, such as an ATS circuit, there are other capacitances. Since the capacitor for the nano-structure is very small, these other capacitances in the circuit may lower the signal voltage and thus dilute a signal directed to one of the nano-components, such as a nano-mechanical resonator. However, to deal with this issue, a high-impedance inductor may be coupled in the control circuit between the ATS and the nano-mechanical resonator. The high-impedance inductor may have a very low parasitic capacitance, thus electrical fields directed at the nano-mechanical resonators may act on the nano-mechanical resonators with only minimal dilution due to capacitance of the inductor (e.g. parasitic capacitance). Also, the high impedance inductor may suppress loss mechanisms.

In some embodiments, the non-linear coupling of the nano-mechanical resonators may be given by g2â2{circumflex over (b)}†+h.c., where g2 is a coupling rate between a storage mode (a) and a dump mode (b). In some embodiments, the non-linearity may be implemented using an asymmetrically threaded SQUID (superconducting quantum interference device), also referred to herein as an “ATS.” The ATS may comprise a superconducting quantum interference device (SQUID) that has been split approximately in the middle by a linear inductor. In its most general form, the ATS potential is given by the following equation:

U({circumflex over (ϕ)})=½EL,b{circumflex over (ϕ)}2−2Ej cos(ϕΣ)cos({circumflex over (ϕ)}+ϕΔ)+2 ΔEj sin(ϕΣ)sin({circumflex over (ϕ)}+ϕΔ)

In the above equation, {circumflex over (ϕ)} is the phase difference across the ATS, ϕΣ:=(ϕext,1+ϕext,2)/2, ϕΔ:=(ϕext,1−ϕext,2)/2, and ϕext,1(ϕext,2) is the magnetic flux threading the left (right) loop, in units of the reduced magnetic flux quantum Φ02=h/2E. Here EL,b=Φ02/Lb; Ej=(Ej,1+Ej,2)/2; and

\({\Delta E_{j}} = \frac{\left( {E_{j,1} - E_{j,2}} \right)}{2}\)

is the junction asymmetry. This ATS potential can be further simplified by tuning ϕΣ and ϕΔ with two separate flux lines. For example, FIG. 1A illustrates ATS 102 included in control circuit 100, wherein ATS 102 includes separate flux lines 108 and 110. Note that FIG. 1A includes ATS 102 in control circuit 100 and also an enlarged depiction of ATS 102 adjacent to control circuit 102 that shows ATS 102 in more detail. The flux lines may be set such that:

\(\phi_{\Sigma} = {\frac{\pi}{2} + {{\epsilon_{p}(t)}\mspace{14mu}{and}}}\)
\(\phi_{\Delta} = \frac{\pi}{2}\)

In the above equations, ϵp(t)=ϵp,0 cos(ωpt) is a small alternating current (AC) component added on top of the direct current (DC) basis. At this bias point, and assuming that |ϵp(t)|<<1 then the equation above for U({circumflex over (ϕ)}) can be reduced to:

U(ϕ)=½EL,b{circumflex over (ϕ)}2−2Ejϵp(t)sin({circumflex over (ϕ)})+2ΔEj cos({circumflex over (ϕ)}).

Using the control circuit 100 shown in FIG. 1A, quantum information may be stored in a state of a linear mechanical resonator. For example quantum information may be stored in storage mode 106. The stored quantum information may also be autonomously error corrected by way of artificially induced two-phonon driving and two-phonon decay controlled by the ATS. These two phonon processes are induced through the non-linear interaction g2 â2{circumflex over (b)}†+h.c. between the storage mode a and an ancillary mode b, called the dump, such as dump mode 104 shown in FIG. 1A. The dump mode is designed to have a large energy decay rate Kd so that it rapidly and irreversibly “dumps” the photons it contains into the environment. If Kd is much larger (e.g. ˜10× or more) than the coupling rate g2, then the dump mode can be adiabatically eliminated from the Hamiltonian, for example as shown in FIG. 1B. For example, as shown on the right side of FIG. 1B, the emission of phonon pairs via g2â2{circumflex over (b)}† can be accurately modeled as a dissipative process described by a dissipator ˜D[a2]. Additionally, if the dump mode is linearly driven as ϵ*be−ωt+h.c. this provides the required energy to stimulate the reverse process g*2(a+2)b, which in the adiabatic elimination, as shown in FIG. 1B, can be modeled as an effective two-phonon drive. Altogether, the dynamics can be accurately modeled through the equation:

\({\frac{d\rho}{dt} = {K_{2}{D\left\lbrack {a^{2} - \alpha^{2}} \right\rbrack}}},{{{where}\mspace{14mu}\alpha} = {{\epsilon\text{/}g_{2}\mspace{14mu}{and}\mspace{14mu} k_{2}} = {4g_{2}^{2}\text{/}K_{d}}}}\)

The steady states of the dynamics of the system shown in FIG. 1B are the coherent states |α, |−α, or any arbitrary superposition of the two. This protected subspace can be used to encode a qubit through the following definition of a logical basis: |0L=|α, |1L=|−α. Qubits encoded in this way are effectively protected from X errors (e.g. bit flips) because the bit-flip rate decays exponentially with the code distance |α|2, as long as K2|α|2>>K1, wherein K1 is the ordinary (e.g. single-photon) decay rate of the storage mode. Since |α|2˜1, this condition is generally equivalent to K2/K1>>1. However, Z errors (e.g. phase flips) may not be protected by this code.

As discussed above, an ATS is formed by splitting a SQUID with a linear inductor. The magnetic flux threading of each of the two resulting loops of the ATS can be controlled via two nearby on-chip flux lines, such as flux lines 108 and 110 shown in FIG. 1A. These flux lines can be tuned to appropriate values and can send radio frequency (rf) signals at appropriate frequencies for a desired non-linear interaction to be resonantly activated in the nano-mechanical resonator. The dump mode 104, may further be strongly coupled to a dump line of characteristic impedance Z0, which induces a large energy decay rate as required.

In some embodiments, the nano-mechanical storage resonator (e.g. storage 106) may be a piezoelectric nano-mechanical resonator that supports resonances in the GHz range. These resonances may be coupled to superconducting circuits of the control circuit 100 via small superconducting electrodes (e.g. terminals) that either directly touch or closely approach the vibrating piezoelectric region of the nano-mechanical resonators. The values of the nonlinear coupling rate g2, the two-phonon dissipation rate k2, and the ratio K2/K1 can be calculated as follows:

First, compute the admittance Ym(ω) seen at the terminals of the nano-mechanical resonator using a finite element model solver. Next, find an equivalent circuit using a Foster synthesis algorithm (further discussed below). Then, diagonalize the combined circuit and compute the zero-point phase fluctuations ϕa,zp and ϕb,zp. Furthermore, compute the dissipation rates kb and k1 of the eigenmodes. Next compute

\({g_{2} = {\left( \frac{E_{j}}{h} \right)\epsilon_{0}\phi_{a,{zp}}^{2}{\phi_{b,{zp}}^{2}/2.}\mspace{20mu}{Also}}},{{{compute}\mspace{14mu} k_{2}} = {4{g_{2}^{2}/{k_{d}.}}}}\)

In some embodiments, a nano-mechanical element, such as the nano-mechanical resonator that implements storage mode 106 and dump mode 104 may be represented as an equivalent circuit that accurately captures its linear response. This can be done using Foster synthesis if the admittance Ym(ω) seen from the terminals of the mechanical resonator is known. For example, the admittance may be computed using finite element modeling. In some embodiments, a Foster network may be used to accurately represent a one-dimensional (e.g. linear) phononic-crystal-defect resonator (PCDR), which may be a type of nano-mechanical resonator used in some embodiments. In some embodiments, the dump resonator may be modeled as having a fixed impedance, such as 1 kilo ohms.

For example FIG. 2 illustrates a version of control circuit 100 that has been represented using a Foster network (e.g. equivalent circuit 200). In its simplest form, equivalent circuit 200 may be represented as ‘a DC capacitance’ in series with an LC block (e.g. L represents an inductor and C represents a capacitor for the LC block), wherein an additional resistor is inserted to include the effects of the loss in the resonator. For example, Foster network 210 is modeled to include capacitor 204, inductor 206, and resistor 208. The linear part of the dump resonator (including the inductor that splits the ATS) can also be represented as an LC block, such as LC block 212. In this representation the dump resonator (e.g. 212) and the storage resonator (e.g. 210) are represented as two linear circuits with a linear coupling and can therefore be diagnolized by a simple transformation of coordinates. For example, FIG. 2 illustrates a diagnolized circuit representation 214. The resulting “storage-like” (â) and “dump-like” ({circumflex over (b)}) eigenmodes both contribute to the total phase drop across the ATS. For example, {circumflex over (ϕ)}=φa, (â+â†)+φb({circumflex over (b)}+{circumflex over (b)}†). These modes therefore mix the via the ATS potential, which may be redefined as U({circumflex over (ϕ)})→U({circumflex over (ϕ)})−EL,b{circumflex over (φ)}2/2 because the inductor has already been absorbed into the linear network. The zero-point phase fluctuations of each mode are given by:

\(\varphi_{k,j} = {\sqrt{\frac{h}{2\omega_{k}}}\left( {C^{{- 1}/2}U} \right)_{jk}}\)

In the above equation C is the Maxwell capacitance matrix of the circuit. U is the orthogonal matrix that diagnolizes C−1/2L−1C−1/2, where L−1 is the inverse inductance matrix. The index k∈{a,b} labels the mode and j labels the node in question. Note that in some instances as described herein the notation of j may be omitted because it is clear from context, e.g. the node of interest is the one right above the ATS.

The way in which the ATS mixes the modes is explicit given the third-order term in the Taylor series expansion of the sin({circumflex over (ϕ)}) contains terms of the form â2{circumflex over (b)}†+h.c., which is the required coupling. This is a reason for using the ATS as opposed to an ordinary junction, which has a potential ˜cos({circumflex over (ϕ)}).

For analysis the pump and drive frequencies may be set to ωp=2ωa−ωb and ωd=ωb. This brings the terms g2â2{circumflex over (b)}†+h.c. into resonance and allows the other terms in the rotating wave approximation (RWA) to be dropped. The coupling is given by g2=∈0Ejφa2φb/2h. Additionally, a linear drive ∈*d{circumflex over (b)}+h.c. at frequency ωd=ωb is added to supply the required energy for the two-photon drive.

### Multi-Mode Stabilization/ATS Multiplexing

In some embodiments, the scheme as described above may be extended to be used in a multi-mode setting, in which N>1 storage resonators are simultaneously coupled to a single dump +ATS (e.g. multiplexed control circuit). This may allow for the cat subspaces of each of the storage modes to be stabilized individually. For example, a dissipator of the form ΣnD[an2−α2]. However, in order to avoid simultaneous or coherent loss of phonons from different modes (which fails to stabilize the desired subspaces), an incoherent dissipator is required. This can be achieved if the stabilization pumps and the drives for the different modes are purposefully detuned as follows:

H=Σm=(Σm(∈*m(d)(t)b†+h.c.)+Σm,i,j(g*ij(m)(t)aiajb†+h.c.), where ∈*m(d)(t)=ϵ*m(d)eiΔt and g*ij(m)(t)=g*2ei(2ω−ω+Δ)t

In the above equation ωm(p)=2ωm−ωb+Δm and ωm(d)=ωb−Δm are the pump and drive frequencies for mode m. By detuning the pumps, the pump operators of different modes can rotate with respect to each other. If the rotation rate is larger than k2 then the coherences of the form ai2ρ(aj†)2 in the Lindbladian vanish in a time averaged sense. The drive de-tunings allow the pumps and drives to remain synchronized even though the pumps have been detuned relative to one another.

In some embodiments, the modes a1 and a2 may be simultaneously stabilized using a multiplexed ATS (e.g. multiplexed control circuit), wherein the pumps have been detuned. Simulations may be performed to determine the detuning parameters using the simulated master equation, as an example:

\(\overset{\cdot}{\rho} = {{- {i\left\lbrack {{{\frac{\Delta}{2}a_{1}^{\dagger}a_{1}} + \ \left( {{\epsilon_{2}e^{i\Delta t}a_{1}^{\dagger 2}} + {\epsilon_{2}a_{2}^{\dagger 2}} + {h.c.}} \right)},\ \rho} \right\rbrack}} + {k_{2}{D\left\lbrack {a_{1}^{2} + a_{2}^{2}} \right\rbrack}(\rho)}}\)

**Bandwidth Limits**

The above described tuning works best when the detuning Δ is relatively small as compared to kb. This is due to the fact that, unlike the single-mode case, where k2=4g22/kb, the two-phonon decay of the multi-mode system is given by:

\(k_{2,n} = {\frac{4{g}^{2}}{k_{b}}\frac{1}{1 + {4\left( {\Delta_{n}/k_{b}} \right)^{2}}}}\)

The Lorentzian suppression factor can be understood by the fact that photons/phonons emitted by the dump mode as a result of stabilizing mode n are emitted at a frequency ωb+Δn and are therefore “filtered” by the Lorentzian line-shape of the dump mode which has linewidth kb. This sets an upper bound on the size of the frequency region that the de-tunings are allowed to occupy. Furthermore, in some embodiments, the de-tunings Δn may all be different from each other by amount greater than k2 in order for the dissipation to be incoherent. In a frequency domain picture, the spectral lines associated with emission of photons/phonons out of the dump must all be resolved. This, also sets a lower bound on the proximity of different tunings. As such, since an upper bound and lower bound are set, bandwidth limits for the de-tunings may be determined. Also, taking into account these limitations, an upper bound on the number of modes that can be simultaneously stabilized by a single dump can also be determined. For example, if de-tunings are selected to be Δn=nΔ, with Δ˜k2, then the maximum number of modes that may be simultaneously stabilized may be limited as Nmax˜kb/Δ˜kb/k2. As a further example, for typical parameters, such as kb/2π˜10 MHz and k2/2π˜1 MHz, this results in bandwidth limits that allow for approximately 10 modes to be simultaneously stabilized.

For example, FIG. 3 illustrates a control circuit 300 that includes a single dump resonator 302 that stabilizes multiple storage resonators 304.

**Use of a High-Impedance Inductor to Enhance Coupling Between a Dump Resonator and One or More Storage Resonators**

In some embodiments, the coupling rate g2 may be increased by using a high impedance inductor. This is because g2 depends strongly on the effective impedance Zd of the dump resonator. For example, g2˜Zd5/2. Thus, in some embodiments, using a large inductor in the ATS may result in a large effective impedance Zd. In some embodiments, the inductor chosen to be included in the ATS circuit may be sufficiently linear to ensure stability of the dump circuit when driven strongly during stabilization. For example, a high impedance inductor used may comprise a planar meander or double-spiral inductor, a spiral inductor with air bridges, an array with a large number of (e.g. greater than 50) highly transparent Josephson junction, or other suitable high impedance inductor.

**Filtering in Multi-Mode Stabilization/Multiplexed ATS**

In some embodiments, microwave filters (e.g. metamaterial waveguides) may be used to alleviate the limitations with regard to bandwidth limits as discussed above. Such filters may also be used to eliminate correlated errors in multiplexed stabilization embodiments. For example, FIG. 4 illustrates control circuit 400 that includes a single dump resonator 404, multiple storage resonators 406, and a filter 402.

More specifically, when stabilizing multiple storage modes with the same dump resonator and ATS device a number of cross-terms appear in the Hamiltonian that would otherwise not be there in the single-mode case. For example, these terms take the form of g2ajakb+e−ivt. After adiabatic elimination of the b mode (for example as discussed in regard to FIG. 1B), these terms effectively become jump operators of the form k2,effajake−ivt. Unlike the desired jump processes k2, aj2, which result in the individual stabilization of the cat subspace of each resonator, the correlated decay terms result in simultaneous phase flips of the resonators j and k. For example, these correlated errors can be damaging to the next layer of error correction, such as in a repetition or striped surface code.

In some embodiments, in order to filter out the unwanted terms in the physical Hamiltonian that give rise to effective dissipators that cause correlated phase flips, the de-tunings of the unwanted terms may be larger than half the filter bandwidth. This may result in an exponential suppression of the unwanted terms. Said another way, the de-tunings and filter may be selected such that detuning of the effective Hamiltonian is larger than half the filter bandwidth. Moreover, the filter mode (along with the dump mode) may be adiabatically eliminated from the model in a similar manner as discussed in FIG. 1B for the adiabatic elimination of the dump mode. This may be used to determine an effective dissipator for a circuit such as control circuit 400 that includes both dump resonator 404 and filter 402.

As discussed above, correlated phase errors may be suppressed by a filter if the corresponding emitted photons have frequencies outside of the filter pass bandwidth. In some embodiments, all correlated phase errors may be simultaneously suppressed by carefully choosing the frequencies of the storage modes. For example cost functions may be used taking into account a filter bandwidth to determine optimized storage frequencies. For example, in some embodiments a single ATS/dump may be used to suppress decoherence associated with all effective Hamiltonians for 5 storage modes. In such embodiments, all dominant sources of stochastic, correlated phase errors in the cat qubits may be suppressed. Cross talk suppression via selection of filter passband ranges and strategic selection of phononic mode frequencies and dump mode detunings is further discussed in detail below.

### Multi-Terminal Mechanical Resonators

In some embodiments, nano-mechanical resonators, such as those shown in FIGS. 1-4 may be designed with multiple terminals that allow a given nano-mechanical resonator to be coupled with more than one ATS/control circuit. For example a single connection ATS may include a ground terminal and a signal terminal, wherein the signal terminal couples with a control circuit comprising an ATS. In some embodiments, a multi-terminal nano-mechanical resonator may include more than one signal terminal that allows the nano-mechanical resonator to be coupled with more than one control circuit/more than one ATS. For example, in some embodiments, a nano-mechanical resonator may include three or more terminals that enable the nano-mechanical resonator to be coupled with three or more ATSs. If not needed an extra terminal could be coupled to ground, such that the multi-terminal nano-mechanical resonator functions like a single (or fewer) connection nano-mechanical resonator. In some embodiments, different signal terminals of a same nano-mechanical resonator may be coupled with different ATSs, wherein the ATSs may be used to implement gates between mechanical resonators, such as a CNOT gate. For example, this may allow for implementation of gates on the stabilizer function.

### Example Physical Gate Implementations

Recall the Hamiltonian of a system comprising of multiple phononic modes âk coupled to a shared ATS mode {circumflex over (b)}:

\(\hat{H} = {{\sum\limits_{k = 1}^{N}{\omega_{k}{\overset{\hat{}}{a}}_{k}^{\dagger}{\hat{a}}_{k}}} + {\omega_{b}{\hat{b}}^{\dagger}\hat{b}} - {2E_{j}{\epsilon_{p}(t)}{\sin\left( {{\sum\limits_{k = 1}^{N}{\hat{\phi}}_{k}} + {\hat{\phi}}_{b}} \right)}}}\)

wherein {circumflex over (ϕ)}k≡φk(âk+âk†) and {circumflex over (ϕ)}b≡φb({circumflex over (b)}+{circumflex over (b)}†). Also, φk and φb quantify zero-point fluctuations of the modes âk and {circumflex over (b)}. To simplify the discussion, neglect small frequency shifts due to the pump ϵp(t) for the moment and assume that the frequency of a mode is given by its bare frequency (in practice, however, the frequency shifts need to be taken into account; see below for the frequency shift due to pump). Then, in the rotating frame where every mode rotates with its own frequency, the following is obtained:

\({\hat{H}}_{rot} = {{- 2}E_{j}{\epsilon_{p}(t)}{\sin\left( {{\sum\limits_{k = 1}^{N}{\varphi_{k}{\hat{a}}_{k}e^{{- \omega_{k}}t}}} + {{h.c.{+ \varphi_{b}}}\hat{b}e^{{- \omega_{b}}t}} + {h.c.}} \right)}}\)

where φk and φb quantify zero-point fluctuations of the modes âk and {circumflex over (b)}. Note that the rotating frame has been used where each mode rotates with its own frequency.

First, a linear drive on a phononic mode, say âk, can be readily realized by using a pump ϵp(t)=ϵp cos(ωpt) and choosing the pump frequency ωp to be the frequency of the mode that is to be drive, that is, ωp=ωk. Then, by taking only the leading order linear term in the sine potential (e.g., sin({circumflex over (x)})≅{circumflex over (x)} we get the desired linear drive:

Ĥrot=2Ejϵpφk(âk+âk†)+H′

where H′comprises fast-oscillating terms such as −Ejϵp(φiâie−i(ω−ω)t+h.c.) with 1≠k and Ejϵp(φb{circumflex over (b)}e−i(ω−ω)t+h.c.) as well as other terms that rotate even faster. Since the frequency differences between different modes are on the order of 100 MHz but |ϵz|/(2π) is typically much smaller than 100 MHz, the faster oscillating terms can be ignored using a rotating wave approximation (RWA).

To avoid driving unwanted higher order terms, one may alternatively drive the phononic mode directly, at the expense of increased hardware complexity, instead of using the pump ϵp(t) at the ATS node.

Now moving on to the implementation of the compensating Hamiltonian for a CNOT gate. For example a compensating Hamiltonian for a CNOT gate may have the form:

\({\hat{H}}_{CNOT} = {\frac{\pi}{4\alpha T}\left( {{\hat{a}}_{1} + {\hat{a}}_{1}^{\dagger} - {2\alpha}} \right)\left( {{{\hat{a}}_{2}^{\dagger}{\hat{a}}_{2}} - \alpha^{2}} \right)}\)

Without loss of generality, consider the CNOT gate between the modes â1 (control) and â2 (target). Note that ĤCNOT comprises an optomechanical coupling

\({\frac{\pi}{4\alpha T}\left( {{\hat{a}}_{1} + {\hat{a}}_{1}^{\dagger}} \right){\hat{a}}_{2}^{\dagger}}{\hat{a}}_{2}\)

between two phononic modes, a linear drive on the control mode

\({{- \left( \frac{\pi\alpha}{4T} \right)}\left( {{\hat{a}}_{1} + {\hat{a}}_{1}^{\dagger}} \right)},\)

and a selective frequency shift of the target mode

\({- \left( \frac{\pi}{2T} \right)}{\hat{a}}_{2}^{\dagger}{{\hat{a}}_{2}.}\)

To realize the optomechanical coupling, one might be tempted to directly drive the cubic term â1â2†â2+h.c. in the sine potential via a pump ϵp(t)=ϵp cos(ωp t). However, the direct driving scheme is not suitable for a couple of reasons: since the term â1â2†â2 rotates with frequency ω1, the required pump frequency is given by ωp=ω1 which is the same pump frequency reserved to engineer a linear drive on the â1 mode. Moreover, the term â1â†â2 rotates at the same frequency as those of undesired cubic terms. Hence, even if the linear drive is realized by directly driving the phononic mode â1, one cannot selectively drive the desired optomechanical coupling by using the pump frequency ωp=ω1 due to the frequency collision with the other cubic terms.

In some embodiments, to overcome these frequency collision issues, the optomechanical coupling is realized by off-resonantly driving the term (â1+λ)â2{circumflex over (b)}†. For example, we use fact that a time-dependent Hamiltonian Ĥ=λÂ{circumflex over (b)}†eiΔt yields an effective Hamiltonian Ĥeff=(x2/Δ)Â†Â upon time-averaging assuming that the population of the {circumflex over (b)} mode is small (e.g. {circumflex over (b)}†{circumflex over (b)}<<1) and the detuning Δ is sufficiently large. Hence given a Hamiltonian Ĥ=x(â1+λ)â2{circumflex over (b)}†e−Δt=h.c., we get

\({\hat{H}}_{eff} = {\frac{x^{2}\lambda}{\Delta}\left( {{\hat{a}}_{1} + {\hat{a}}_{1}^{\dagger} + \lambda + {\frac{1}{\lambda}{\hat{a}}_{1}^{\dagger}{\hat{a}}_{1}}} \right){\hat{a}}_{2}^{\dagger}{\hat{a}}_{2}}\)

In particular, by choosing Δ=−2α, we can realize the optomechanical coupling as well as the selective frequency shift of the â2 mode, e.g. Ĥeff∝(â1+â1†−2α)â2†â2 up to an undesired cross-Ker term −â1†â1â2†â2/(2α). In this scheme, we have the desired selectivity because the term (â1+λ)â2{circumflex over (b)}† is detuned from other undesired terms such as (â1+λ)âk{circumflex over (b)}† with k≥3 by a frequency difference ω2−ωk. Thus, the unwanted optomechanical coupling (â1+â1†)âk†â2 can be suppressed by a suitable choice of the detuning Δ. It is remarked that the unwanted cross-Kerr term â1†â1â2†â2 can in principle be compensated by off-resonantly driving another cubic term â1â2 b† with a different detuning Δ′≠Δ.

Lastly, similar approaches as used in the compensating Hamiltonian for the CNOT gate can also be used for a compensating Hamiltonian for a Toffoli gate.

### Example Processes for Implementing an ATS-Phononic Hybrid System

FIG. 5 illustrates a process of stabilizing a nano-mechanical resonator using an asymmetrically-threaded superconducting quantum interference device (ATS), according to some embodiments.

At block 502, a control circuit of a system comprising one or more nano-mechanical resonators causes phonon pairs to be supplied to the nano-mechanical resonator via an ATS to drive a stabilization of a storage mode of the nano-mechanical resonator such that the storage mode is maintained in a coherent state. Also, at block 504, the control circuit dissipates phonon/photon pairs from the nano-mechanical resonator via an open transmission line of the control circuit that is coupled with the nano-mechanical resonator and the ATS.

FIG. 6 illustrates a process of stabilizing multiple nano-mechanical resonators using a multiplexed ATS, according to some embodiments.

At block 602, storage modes for a plurality of nano-mechanical resonators that are driven by a multiplexed ATS are chosen such that the storage modes are de-tuned. For example, block 602 may include detuning storage modes supported by a plurality of nano-mechanical resonators from a dump resonator containing an asymmetrically-threaded superconducting quantum interference device At block 604 phonon pairs are supplied to a first one of the nano-mechanical resonators at a first frequency and at 606 phonon pairs are supplied to other ones of the nano-mechanical resonators at other frequencies such that the frequencies for the respective storage modes of the nano-mechanical resonators are detuned. For example, blocks 604 and 606 may include applying a pump and drive to an ATS to activate two-phonon driven-dissipative stabilization to a first one of the nano-mechanical resonators and suppressing, via a microwave bandpass filter, correlated decay processes from the plurality of nano-mechanical resonators.

Additionally, the storage mode frequencies and a bandwidth for a filter of the control circuit may be selected such that de-tunings of unwanted terms are larger than half the filter bandwidth. Then, at block 608 a microwave filter with the determined filter bandwidth properties may be used to filter correlated decay terms from the plurality of nano-mechanical resonators.

### Cross-Talk Suppression Via Filtering, Phononic Mode Frequency Selection, and Dump Mode Detuning Selection

In acting as a nonlinear mixing element, the ATS (e.g. multiplexed control circuit) not only mediates the desired (g2ân2{circumflex over (b)}†+h.c.) interactions, but it also mediates spurious interactions between different storage modes. How such interactions can give rise to cross-talk among the cat qubits, and subsequently how this cross-talk can be mitigated is further discussed blow. Such as mitigation through a combination of filtering and phonon-mode frequency optimization. While most spurious interactions mediated by the ATS are far detuned and can be safely neglected in the rotating wave approximation, there are others which cannot be neglected. Most concerning among these are interactions of the form:

g2âiâj{circumflex over (b)}†eiδt+h.c.

for j≠k, where: δijk=ωk(p)−ωi−ωj+ωb. This interaction converts two phonons from different modes, j and k, into a single buffer mode photon, facilitated by the pump that stabilizes mode i. These interactions cannot be neglected in general because they have the same coupling strength as the desired interactions in the Hamiltonian (as discussed above), and they can potentially be resonant or near-resonant, depending on the frequencies of the phonon modes involved.

There are three different mechanisms through which the interactions can induce crosstalk among the cat qubits. These mechanisms are described in detail further below. First, analogously to how the desired interactions lead to two-phonon losses, the undesired interactions lead to correlated, single-phonon losses:

keffD[âjâk]→keff|α|4D[{circumflex over (Z)}j{circumflex over (Z)}k]

where the rate keff will be discussed shortly. The arrow denotes projection onto the code space, illustrating that these correlated losses manifest as stochastic, correlated phase errors in the cat qubits.

Second, the interplay between different interactions gives rise to new effective dynamics generated by the Hamiltonians of the form:

Ĥeff=xâi†âj†âmânei(δ−δ)t+h.c., →x|α|4{circumflex over (Z)}i{circumflex over (Z)}j{circumflex over (Z)}k{circumflex over (Z)}lei(δ−δ)t+h.c.

where the coupling rate x is further defined below. The projection onto the code space in the second line reveals that Ĥeff can induce undesired, coherent evolution within the code space.

Third, Ĥeff can also evolve the system out of the code space, changing the phonon-number parity of one or more modes in the process. Though the engineered dissipation subsequently returns the system to the code space, it does not correct changes to the phonon-number parity. The net result is that Ĥeff also induces stochastic, correlated phase errors in the cat qubits,

γeffD[{circumflex over (Z)}i{circumflex over (Z)}j{circumflex over (Z)}k{circumflex over (Z)}l]

where the rate γeff will be discussed shortly.

However, in some embodiments, all of these types of cross-talk can be suppressed through a combination of filtering and phonon-mode frequency optimization. For example it is possible to achieve keff≈0 and γeff≈0, provided

|δijk|>2J,

|δijk−δimn|>2J

respectively. This suppression can be understood as follows. The decoherence associated with keff and γeff results from the emission of photons at frequencies ωb+δijk and ωb±(δijk−δinn) respectively. When the frequencies of these emitted photons lie outside the filter passband, their emission (and the associated decoherence) is suppressed. Crucially, it can be arranged for all such errors to be suppressed simultaneously by carefully choosing the frequencies of the phonon modes, as shown in FIGS. 7A-7C. The configuration of mode frequencies in FIG. 7C was found via a numerical optimization procedure described in further detail below. The optimization also accounts for the undesired coherent evolution: the detunings δijk−δimn are maximized so that Ĥeff is rapidly rotating and its damaging effects are mitigated (this suppression is quantified further below). Additionally, it is noted that in FIG. 7B all emitted photon frequencies associated with crosstalk lie at least 10 MHz outside of the filter passband. As a result, the crosstalk suppression is robust to variations in the phonon mode frequencies of the same order. Larger variations in the phonon mode frequencies can be accommodated by reducing the filter bandwidth.

Thus it is demonstrated that crosstalk can be largely suppressed within the five-mode unit cells of the phononic architecture described herein.

With regard to FIGS. 7A-7C, FIG. 7A shows frequency multiplexing. The five lines shown in FIG. 7A are the five frequencies for the five phonon modes (ωα, ωβ, ωγ, ωδ, and ωρ). Because the desired couplings (g2ân2{circumflex over (b)}†eiΔt+h.c.) are detuned by different amounts, photons lost to the environment via the buffer have different frequencies. When the corresponding emitted photons (702) are spectrally well resolved, |Δn−Δm|>>4|α|2k2, the modes are stabilized independently. Dissipation associated with photon emissions at frequencies inside the filter passband (704) is strong, while dissipation associated with emission at frequencies outside the passband is (706) suppressed. In FIG. 7B the lines 708 denote photon emission frequencies associated with various correlated errors, calculated for the specific phonon mode frequencies plotted in FIG. 7C. The mode frequencies are deliberately chosen so that all emissions associated with correlated errors occur at frequencies outside the filter passband (e.g. none of the lines 708 fall within the filter passband box 704). In other words, Equations above are simultaneously satisfied for any choices of the indices that lead to nontrivial errors in the cat qubits.

As mentioned above, the predominant sources of crosstalk are undesired terms in the Hamiltonian of the form

g2âiâj{circumflex over (b)}†eiδt+h.c.

where: δijk=ωk(p)−ωi−ωj+ωb.

In this formulation, the dependence of g2 on the indices i,j has been neglected for simplicity. In contrast to the other undesired terms in the Hamiltonian, these terms have the potential to induce large crosstalk errors because they both (i) have coupling strengths comparable to the desired terms, and (ii) can be resonant or near-resonant. In particular, the undesired term is resonant (δijk=0) for 2ωk+Δk=ωi+ωj. This resonance condition can be satisfied, for example, when the storage modes have near uniformly spaced frequencies.

These unwanted terms may not be exactly resonant in practice, but it cannot generally be guaranteed that they will be rotating fast enough to be neglected in the RWA either. In contrast, all other undesired terms are detuned by at least minn|ωn−ωb|, which is on the order of ˜2π×1 GHz for the parameters considered herein. It is therefore useful to focus on crosstalk errors induced by the terms in the Hamiltonian directly above.

These terms can lead to three different types of correlated errors:

Type I: Stochastic errors induced by effective dissipators;

Type II: Stochastic errors induced by effective Hamiltonians; and

Type III: Coherent errors induced by effective Hamiltonians.

Without mitigation, these correlated phase errors could be a significant impediment to performing high-fidelity operations.

**Type I. Stochastic Errors Induced by Effective Dissipators**

The terms in the Hamiltonian above can lead to correlated photon losses at rates comparable to k2, resulting in significant correlated phase errors in the cat qubits. These deleterious effects manifest when one adiabatically eliminates the buffer mode. Applying effective operator formalism to the operators:

Ĥ(1)=g2âiâj{circumflex over (b)}†eiδt+h.c.

L(1)=√{square root over (kb)}{circumflex over (b)}

obtains the effective operators:

\({H_{eff}^{(1)} = {{{- \frac{{g_{2}}^{2}\delta_{ijk}}{\delta_{ijk}^{2} + \frac{k_{b}^{2}}{4}}}\left( {{\hat{a}}_{i}{\hat{a}}_{j}} \right)^{\dagger}\left( {{\hat{a}}_{i}{\hat{a}}_{j}} \right)} + {h.c.}}},{L_{eff}^{(1)} = {\frac{g_{2}\sqrt{k_{b}}}{\delta_{ijk} - {i{k_{b}/2}}}{\hat{a}}_{i}{\hat{a}}_{j}e^{i\;\delta_{ijk}t}}}\)

The effective Hamiltonian preserves phonon-number parity and thus does not induce phase flips. The effective jump operator {circumflex over (L)}eff describes correlated single-phonon losses in modes i and j at a rate:

\(k_{eff} = \frac{k_{b}{g_{2}}^{2}}{\delta_{ijk}^{2} + \frac{k_{b}^{2}}{4}}\)

which is comparable to k2 for δijk≲kb. These correlated single photon losses induce correlated phase flips in the cat qubits, which can be seen by projecting {circumflex over (L)}eff into the code space,

\(\left. L_{eff}^{(1)}\rightarrow{\sqrt{k_{eff}}\alpha^{2}{\hat{Z}}_{i}{\hat{Z}}_{j}{e^{i\delta_{ijk}t}.}} \right.\)

**Type II: Stochastic Errors Induced by Effective Hamiltonians**

The interplay of different terms of the form of the Hamiltonian can lead to further correlated errors. As an example, consider the operators:

Ĥ(2)=g2âiâj{circumflex over (b)}†eiδt+g2âlâm{circumflex over (b)}†eiδt+h.c.

{circumflex over (L)}(2)=√{square root over (kb)}{circumflex over (b)}.

Adiabatically eliminating the buffer mode yields,

\({\hat{H}}_{eff}^{(2)} = {\left\lbrack {{{x\left( {{\hat{a}}_{i}{\hat{a}}_{j}} \right)}^{\dagger}\left( {{\hat{a}}_{l}{\hat{a}}_{m}} \right)e^{i({\delta_{lmn} - {\delta_{{ijk})}t}}}} + {h.c.}} \right\rbrack + \ldots}\)
\({\hat{L}}_{eff}^{(2)} = {{\frac{g_{2}\sqrt{k_{b}}}{\delta_{ijk} - {i{k_{b}/2}}}{\hat{a}}_{i}{\hat{a}}_{j}e^{i\delta_{ijk}t}} + {\frac{g_{2}\sqrt{k_{b}}}{\delta_{lmn} - {i{k_{b}/2}}}{\hat{a}}_{l}{\hat{a}}_{m}{e^{i\delta_{lmn}t}.{where}}}}\)
\(x = {- {\frac{{g_{2}}^{2}}{2}\left\lbrack {\frac{1}{\delta_{ijk} - {i{k_{b}/2}}} + \frac{1}{\delta_{lmn} + {i{k_{b}/2}}}} \right\rbrack}}\)

and “ . . . ” denotes additional terms in the Hamiltonian that preserve phonon-number parity. Note that the effective dissipator {circumflex over (L)}eff2) leads to Type I correlated phase errors. Indeed, for sufficiently large |δijk−δlmn| the action of {circumflex over (L)}eff(2) can be approximated by replacing it with two independent dissipators of the form {circumflex over (L)}eff(1).

What is different about this example is that the effective Hamiltonian Ĥeff(2) contains terms ∝(âiâj)†(âlâm) that generally do not preserve phonon-number parity. Such terms can unitarily evolve the system out of the code space, changing the parity in the process. In turn, the engineered dissipation returns the system to the code space, but it does so without changing the parity. Therefore, the net effect of such excursions out of the code space and back is to induce stochastic parity-flips in the storage modes, which manifest as correlated phase errors on the cat qubits. The errors are stochastic even though the evolution generated by Ĥeff(2) is unitary because the stabilization itself is stochastic. Specifically, the errors are of the form D[{circumflex over (Z)}i{circumflex over (Z)}j{circumflex over (Z)}l{circumflex over (Z)}m], which one can show by adiabatically eliminating the excited states of the storage modes.

**Type III: Coherent Errors Induced by Effective Hamiltonians**

The parity-non-preserving effective Hamiltonian Ĥeff(2) also induces non-trivial coherent evolution within the code space. This can be seen by projecting Ĥeff(2) into the code space

Ĥeff(2)→(|α|4x{circumflex over (Z)}i{circumflex over (Z)}j{circumflex over (Z)}l{circumflex over (Z)}m)ei(δ−δ)t+h.c.

This undesired evolution does not decohere the system but can nevertheless degrade the fidelity of operations.

**Cross-Talk Mitigation Using Filtering**

In some embodiments, type I and type II errors can be suppressed by placing a bandpass filter (as described above and shown in FIG. 4, element 402) at the output port of the buffer mode. The purpose of the filter is to allow photons of only certain frequencies to leak out of the buffer, such that the desired engineered dissipation remains strong but spurious dissipative processes are suppressed. A crucial requirement of this approach is that the desired dissipative processes be spectrally resolvable from the undesired ones, which is shown to be achievable further below.

In some embodiments, a tight-binding model is used where the filter consists of a linear chain of M bosonic modes with annihilation operators ĉi, and each with the same frequency ωb. Modes in the chain are resonantly coupled to their nearest neighbors with strength J. The first mode in the chain couples to the buffer mode {circumflex over (b)}, which is no longer coupled directly to the open 50Ω. waveguide. Instead, the M-th mode is now the one which couples strongly to the waveguide, such that its single-photon loss rate is given by kc. The buffer-filter system is described by the Hamiltonian (in the rotating frame)

\(H_{{buffer} + {filter}} = {{J\left( {{{\overset{\hat{}}{c}}_{1}^{\dagger}\hat{b}} + {{\hat{c}}_{1}{\hat{b}}^{\dagger}}} \right)} + {\sum\limits_{i = 1}^{M - 1}{J\left( {{{\overset{\hat{}}{c}}_{i + 1}^{\dagger}{\overset{\hat{}}{c}}_{i}} + {{\overset{\hat{}}{c}}_{i + 1}{\overset{\hat{}}{c}}_{i}^{\dagger}}} \right)}}}\)

together with the dissipator kcD[ĉM]. These additional modes act as a ban pass filer, as further shown below, with frequency ωb and bandwidth 4J, and they suppress the emission of photons with frequencies outside of this passband.

**Suppression of Type I Errors**

To illustrate the suppression of Type I errors, consider the operators

Ĥ(3)=(g2âiâj{circumflex over (b)}teiδt+h.c.)+Ĥbuffer+filter

{circumflex over (L)}(3)=√{square root over (kc)}ĉM

where the first term in Ĥ(3) is the same as an unwanted term from Ĥ(1). In some embodiments, both the buffer and filter modes are adiabatically eliminated in order to obtain an effective dynamics for only the storage modes. It is noted that adiabatically eliminating the buffer and filter modes together is not fundamentally different from adiabatically eliminating the buffer. This yields the effective dissipator

{circumflex over (L)}eff(3)√{square root over (keff(M))}âiâjeiδt

In this regime, keff(M) is exponentially suppressed with increasing M via the factor (J/δijk)2M. These rates are plotted as a function of δijk in FIG. 8A (left side) where the exponential suppression of the decoherence rates outside the filter band is evident. FIG. 8A (right side) also shows the results of analogous master equation simulations. Because good quantitative agreement is observable with the analytical expression, it is concluded that Type I errors are indeed suppressed by the filter, provided |δijk|>2J.

**Suppression of Type II Errors**

To illustrate the suppression of Type II errors consider a toy model that both captures the relevant physics and is easy to study numerically. Consider the operators:

Ĥ(4)=(gâ{circumflex over (b)}†eiδt+g{circumflex over (b)}†eiδt+h.c.)+[g2(â2−α2){circumflex over (b)}†+h.c.]+Ĥbuffer+filter

{circumflex over (L)}(4)=√{square root over (kc)}ĉM

where â is the annihilation operator for the single storage mode considered in this model. In this toy model, the first portion of Ĥ(4) should be understood as analogous to Ĥ(2). Indeed the former can be obtained from the latter by replacing âiâj→â and âlâm→1.

Adiabatically eliminating the buffer and filter modes yields the effective operators

Ĥeff(4)=[xeff(M)âei(δ−δ)t+h.c.]+ . . . .

{circumflex over (L)}eff(4)=√{square root over (keff(δ)(M))}âeiδt+√{square root over (keff(0))}(M)(â2−α2).

Here “ . . . ” denotes a parity-preserving term (∝â†â) that is omitted. Also, keff(δ)(M) denotes the effective loss rate with the replacement δijk→δ, and

\({x_{eff}(M)} \approx {{- \frac{{g}^{2}}{2}}\left( {\frac{1}{\delta_{1}} + \frac{1}{\delta_{2}}} \right)}\)

is independent of M in the limit δ1,2>>J, kb. The first term in {circumflex over (L)}eff(4) gives rise to Type I errors that are suppressed by the filter.

It follows from energy conservation that Type II errors induced by Ĥeff(4) result in photon emissions at frequency ωb+δ2−δ1. Intuitively, such emissions should be exponentially suppressed when this frequency lies outside the filter pass band. However, this suppression is not apparent in the operators Ĥeff(4), because, in the course of deriving Ĥeff(4), the filter was already eliminated. After adiabatic elimination the only vestige of the filter is the term √{square root over (keff(0))}(M)(â2−α2), which embodies the behavior of the filter at frequency ωb, but not at frequency ωb+δ2−δ1. As such, proceeding to calculate the Type II error rate from these operators is not valid, and an alternate approach is required.

In order to properly capture the subtle interplay between the effective Hamiltonian, the stabilization, and the filter, the adiabatic elimination can be deferred. Focus is placed on the regime where the terms in the first portion of the Hamiltonian are rapidly rotating, so that evolution generated by Ĥ(4) is well approximated by its time average. The term {circumflex over (b)}†{circumflex over (b)} can be replaced with its expected value of 0. Doing so reveals that Ĥeff(4) can be understood as arising from the time averaged dynamics of the unwanted terms in Ĥ(4) in the limit of large δ1,2 In effect, time averaging provides a way of introducing Ĥ(4) into the dynamics without having to eliminate the filter, thereby allowing study of the interplay of the filter and effective Hamiltonian.

Begin by taking the operators Ĥ(4) and {circumflex over (L)}(4) and adiabatically eliminating the buffer, the filter, and all excited states of the storage mode, i.e. all states that do not lie within the code space. Adiabatically eliminating the storage mode excited states is valid in the regime where the engineered dissipation is strong relative to couplings that excite the storage mode (Ĥeff(4) in this case), such that these excited states are barely populated. It is found that the phase flip rate is exponentially suppressed by the filter,

\({\gamma_{eff}(M)} \approx {{\gamma_{eff}(0)}\left( \frac{J}{\delta_{1} - \delta_{2}} \right)^{2M}}\)

In FIG. 8B (left side), the rates γeff (M) as a function of δ1−δ2 are plotted, where the decoherence rates outside the filter band is again evident. FIG. 8B on the right side shows the results of corresponding master simulation equations. Thus it can be concluded that Type II errors are also suppressed by the filter, provided the effective Hamiltonian detuning lies outside the filter passband.

**Cross-Talk Mitigation Using Mode Frequency Optimization**

In addition to suppressing Type I and Type II errors via the filter, Type III errors can be suppressed by carefully selecting the of the phonon modes. In doing so, so, the effects of Type III errors can also be simultaneously minimized. Importantly, the phonon mode frequencies are chosen to be compatible with error correction in the surface code. However, the surface code architecture may constrain the choice of phonon mode frequencies. To understand the constraints imposed by the implementation of the surface code, recall that each ATS (e.g. multiplexed control circuit) is coupled to five phononic modes. Among the five modes, four modes (two data and two ancilla modes for the surface code) are stabilized in the cat-code manifold by an ATS. Another mode (readout mode) is dedicated to measuring cat qubits in the X basis and is not stabilized by any ATS. Since every data or ancilla mode couples to two ATSs, each ATS is only responsible for stabilizing two of the five phononic modes to which it couples. Thus, for each given ATS, it is necessary to determine which two phononic modes should be stabilized. An important consideration in deciding which phononic modes should be stabilized by a given ATS is that each ATS is used to realize four CNOT gates (performed in four different time steps) to measure the stabilizers of the surface code. While a CNOT gate is being performed, the target mode of the CNOT gate is stabilized by a rotating jump operator

\({{\overset{\hat{}}{L}}_{2}(t)} = {{\overset{\hat{}}{a}}_{2}^{2} - \alpha^{2} + {\left( \frac{\alpha}{2} \right)\left( {{\exp\left\lbrack \frac{2i\;\pi\; t}{T} \right\rbrack} - 1} \right)\left( {{\overset{\hat{}}{a}}_{1} - \alpha} \right)}}\)

that acts non-trivially both on the target mode (â2) and the control mode (â1). Thus, while a CNOT gate is being performed, the target mode must be stabilized by the ATS that also couples to the control mode.

FIG. 9 shows how these stabilization constraints can be satisfied. In the top panel of the figure, four time steps are shown of the surface-code stabilizer measurement (out of six, state preparation and measurement time steps are omitted) time steps. During each time step, different CNOT gates between data and ancilla cat qubits are applied. Data modes are labeled as α and γ and ancilla modes are labeled as β and δ. Ancilla modes labelled as β(δ) are used to measure the X-type (Z-type) stabilizers of the surface code. Black arrows indicate which phononic modes are stabilized by each ATS at each time step; each phononic mode at the tip of a black arrow is stabilized by the ATS at the arrow's tail. Importantly, every target mode of a CNOT gate is stabilized by an ATS that also couples to the corresponding control mode at all time steps. Note, however, that a given ATS stabilizes different modes at different time steps, as summarized in the bottom panel of FIG. 9. In particular, there are two stabilization configurations: in configuration 1 (2) modes α,β(γ,δ) are stabilized by the given ATS, and the remaining modes γ,δ(α,β) are stabilized by some other neighboring ATSs.

The goal is to choose the frequencies of the phonon modes and detunings of the pumps in order to minimize crosstalk. In order to ensure that the choice of mode frequencies is compatible with the surface-code stabilizer measurement, assign modes with the same label in FIG. 9 to have the same frequency. Thus, there are only five mode frequencies that must be chosen: the frequencies ωα, ωβ, ωγ, ωδ corresponding to the four labels in FIG. 9, plus the frequency of the readout mode (not shown in FIG. 9), which can be taken to be the same in each unit cell and denote by ωp. Similarly, there are four pump detunings, Δα, Δβ, Δγ, Δδ, that must be chosen. Here, as above, Δi denotes the detuning of the pump (and buffer drive) used to stabilize mode i.

A cost function C can be constructed that quantifies cross-talk as a function of these nine parameters (five mode frequencies and four pump detunings). Numerically minimizing C allows results in finding choices of the frequencies and detunings that minimize crosstalk.

First, C should be large if any emitted photons associated with Type I and II errors lie inside the filter's bandwidth 4J. Thus, take C=1 if any of the following conditions are met for either of the two stabilization configurations shown in FIG. 9:


- - \|δ_(ijk)\|\<2J (Type I errors not suppressed)
  - \|δ_(ijk)−δ_(lmn)\|\<2J (Type II errors not suppressed)
  - \|δ_(iii)\|\>2J (Desired dissipation suppressed)

In other words, set C=1 if any Type I or II errors are not suppressed by the filter, or if any of the desired engineered dissipation is suppressed by the filter. These conditions must be checked for both stabilization configurations shown in FIG. 9; checking both configurations is necessary in order to ensure that Type I and II crosstalk is suppressed by the filter at all time steps.

Second, C should be large if the coherent Type III errors have significant damaging effects. Recall that these errors are generated by effective Hamiltonian terms,

|α|4x{circumflex over (Z)}i{circumflex over (Z)}j{circumflex over (Z)}l{circumflex over (Z)}mei(δ−δ)t+h.c.

When these terms are rapidly rotating, e.g. when |α4x|<<|δijk−δlmn|, their effects are suppressed. Indeed, these terms effectively induce detuned Rabi oscillations between states of different parity, and the magnitude of these oscillations is small in the far-detuned limit. To quantify this suppression, note that these micro-oscillation errors remain coherent during gates but can be converted to incoherent, correlated {circumflex over ( )}Z errors when the X-type stabilizers are measured. The probability pijklmn of inducing a correlated phase error upon a such a measurement scales quadratically in the ratio of the coupling strength and detuning,

\({p_{ijklmn} = \left( \frac{{\alpha^{4}x}}{\delta_{ijk} - \delta_{lmn}} \right)^{2}}.\)

Among the various Type III errors, focus is placed on those that induce phase errors in both of the data modes α and γ since such errors are specific to the architecture described herein and not taken into account in the standard surface-code analysis.

In particular define pdouble as the total probability at least one Type III error ∝{circumflex over (Z)}α{circumflex over (Z)}γÎβ and ptriple as the total probability of at least one Type III error ∝{circumflex over (Z)}α{circumflex over (Z)}γ{circumflex over (Z)}β. Explicitly,

\({p_{double} = {\sum\limits_{{\{{ijklmn}\}} \in D}p_{ijklmn}}},{p_{triple} = {\sum\limits_{{\{{ijklmn}\}} \in T}p_{ijklmn}}},\)

where D and T denote sets of indices that give rise to errors a ∝{circumflex over (Z)}α{circumflex over (Z)}γÎβ and ∝{circumflex over (Z)}α{circumflex over (Z)}γ{circumflex over (Z)}β, respectively. For example, as shown in FIG. 10. Note that the {circumflex over (Z)} error on the ancilla mode β manifests as a flipped X-basis measurement outcome. On the other hand, {circumflex over (Z)} errors on the ancilla mode δ do not flip the measurement outcomes. This is because the mode δ is measured in the Z-basis, and Z-basis measurements commute with {circumflex over (Z)} errors.

For the cost function, take C=1 if Type I or II errors are not suppressed by the filter (see aforementioned conditions on the δijk) otherwise, take

C=½(pdouble(1)+ptriple(1)+pdouble(2)+ptriple(2))

where pdouble(i) and ptriple(i) denote the values for pdouble and ptriple for the i-th double triple double triple stabilization configuration. This equation represents the average probability of a Type III error occurring during one time step. Costs C<<1 are thus only achieved when both the probability of Type III errors is small, and all Type I and II errors are suppressed by the filter.

Having defined the cost function C, a numerical search can be performed for the values of the mode frequencies and pump detunings which minimize the cost. In performing this optimization, two additional restrictions may be placed on allowed frequencies and detunings. First, restrict the mode frequencies to lie within a 1 GHz bandwidth. This is done because the modes are supported by phononic crystal-defect resonators (PCDRs), and as such all mode frequencies must lie within the phononic bandgap, or at least within the union of two separate bandgaps each associated with different PCDRs. These bandgaps are typically not more than 500 MHz wide for the devices considered in the preceding sections. Second, restrict the values of the detunings to Δ=±J. This is done to maximize use of the filter bandwidth; emitted photons are detuned from one another by 2J and from the nearest band edge by J. Additionally, because the filter bandwidth restricts the maximum achievable k2, take J to be as large as possible while still allowing for C<<1.

Optimized results are shown in FIGS. 11A and 11B. For the optimal configurations, all Type I and Type II errors are simultaneously suppressed by the filter. Note also that all emitted photon frequencies associated with Type I or II errors lie at least 10 MHz outside the filter passband. As a result, the optimized configuration is robust to deviations in the mode frequencies of the same order, and larger deviations can be tolerated by decreasing the filter bandwidth. Moreover, for realistic values of |α| and g2C<<1, indicating that Type III errors are strongly suppressed. Therefore, all dominant sources of crosstalk are strongly suppressed. The top plot in FIG. 11B is for the case where modes α and β(γ and δ) are stabilized simultaneously. The lines outside of the filter pass band 1102 indicate photons emitted via parity non-preserving Type I and Type II processes. The filter pass band 1102 cover the region [−50,50] (2π×MHz), representing a bandpass filter with center frequency ωb and a 4J=2π×100 MHz passband. The five lines shown in FIG. 11A are the five optimized frequencies for the five phonon modes (ωα, ωβ, ωγ, ωδ, and ωρ).

Frequency optimization results are also shown in the following table. The parameters 4J and co are given in units of 2π×MHz. The Type III error probabilities and the cost C are expressed in terms of α and g2. For realistic choices of

\({\alpha } = {{\sqrt{8}\mspace{14mu}{and}\mspace{14mu}\frac{g_{2}}{2\pi}} = 2}\)

MHz, the cost function evaluates to C=1.05×10−4 and C=1.23×10−3 for the four- and five-mode configurations, respectively. For the analysis fixed values are used for the pump detunings, −Δα=Δβ=Δγ=Δδ=J.

FIG. 12 is a flowchart illustrating a multiplexed control circuit (e.g. multiplexed ATS) stabilizing phononic modes of cat qubits and also suppressing cross-talk, according to some embodiments.

At 1202, respective storage modes of mechanical resonators are driven by a multiplexed control circuit (e.g. multiplexed ATS). At 1204, phonons are dissipated from phononic modes of the mechanical resonators via the multiplexed control circuit (e.g. multiplexed ATS). At 1206, one or more filters suppress one or more spurious photon dissipation processes of the multiplexed control circuit (e.g. multiplexed ATS), wherein the one or more spurious photon dissipation processes lead to cross-talk between storage modes of the respective mechanical resonators coupled to the multiplexed control circuit (e.g. multiplexed ATS) if not suppressed.

FIG. 13 is a flowchart illustrating a process for selecting frequencies for phononic modes and detunings of pump modes such that probabilities that the effective Hamiltonians of the multiplexed control circuits (e.g. multiplexed ATSs) induce coherent errors (e.g. type III cross talk errors) is minimized, according to some embodiments.

At 1302, frequencies are selected for phononic modes of cat states of a surface code implemented using multiplexed control circuits (e.g. ATSs) that excite (and dissipate) mechanical resonators. At 1304, detunings of dump modes are selected, wherein (1306) the selecting of the frequencies and the detunings is performed such that probabilities of effective Hamiltonians of the multiplexed control circuits (e.g. ATSs) inducing coherent errors is minimized.

**Using Additional Edges in a Decoding Graph to Identify/Correct Errors Caused by Cross-Talk**

Recall that each ATS stabilizes multiple phononic modes. Since the ATS mediates various spurious interactions as well as desired interactions, phononic modes that are connected by the same ATS undergo crosstalk errors. While stochastic crosstalk errors can be strongly suppressed by filtering and careful choice of the frequencies of the phononic modes, coherent micro-oscillation errors cannot be eliminated by the filters. In particular, such residual crosstalk errors result in two non-trivial noise processes: every pair of data qubits that are connected by a shared ATS (hence aligned vertically) experiences a correlated Z error with probability pdouble and every triple of two data qubits and an ancilla qubit that measures an X stabilizer of the surface code experiences a correlated Z error with probability ptriple. In particular, the Z error on the ancilla qubit is realized in the form of a flipped measurement outcome of the corresponding X-type stabilizer (as shown in FIG. 14). Note the arrows in FIG. 14 show where the Z errors could occur.

As discussed in the previous section, the frequencies of the five phononic modes coupled to a shared ATS can be optimized to minimize pdouble and ptriple, assuming that the maximum frequency difference between different phononic modes is 2π×1 GHz.

With such an optimal choice of phononic mode frequencies, in some embodiments, it is found that the correlated error rates pdouble and ptriple are given by

\(p_{double} = {{1.8}29 \times 10^{- 8}{\alpha }^{8}\left( \frac{g_{2}\text{/}\left( {2\pi} \right)}{1\mspace{14mu}{MHz}} \right)^{4}}\)
\(p_{triple} = {{5.2}05 \times 10^{{- 1}0}{\alpha }^{8}\left( \frac{g_{2}\text{/}\left( {2\pi} \right)}{1\mspace{14mu}{MHz}} \right)^{4}}\)

As discussed above, g2 is the strength of the desired interaction â2{circumflex over (b)}† needed for the engineered two-photon dissipation. Note that ptriple is 35 times smaller than pdouble.

FIG. 15A logical Z failure rates of the thin surface code under the presence of the crosstalk errors described above are illustrated for various values of g2, where five modes are coupled to each ATS. It is noted that in the presence of crosstalk errors with probabilities pdouble and ptriple extra edges need to be added to the matching graphs of the surface code. Details of the modified graphs in addition to the edge weight calculations are provided below.

In FIG. 15B logical Z errors are illustrated in the presence of crosstalk where the X readout of the cat qubits is performed directly using an optomechanical coupling (so that the crosstalk error probabilities are reduced by only having 4 phononic modes coupled to an ATS instead of five. As can be seen from FIG. 15B, when g2/(2π)=1 MHz, the effects from crosstalk errors are negligible (the logical error rate curves with and without crosstalk almost perfectly overlap). When g2/(2π)=2 MHz, the effects are very small. However, if g2/(270=3 MHz, the difference between logical Z error rates of the surface code with and without crosstalk errors is large enough such that one would need to use larger code distances to achieve the target logical failure rates for the algorithms as described herein. Hence, to maintain the overhead results, it would be preferable to use values of g2/(2π)=2 MHz since in such a case, effects from crosstalk errors are very small.

Lastly, when only 4 modes are coupled to the ATS, the results from FIG. 15B indicate that g2/(2π) can go up to 4 MHz before effects from crosstalk become large enough such that one would need to use larger surface codes to achieve logical failure rates for the algorithms considered herein. In some cases, the maximum achievable g2 is fundamentally limited by 4J/(10α) due to the filter design and validity of adiabatic elimination. Here, 4J is the filter bandwidth which is given by 2π×100 MHz for 5 modes per ATS and 2π×180 MHz for 4 modes per ATS under the optimal choice of phononic mode frequencies. Hence, the maximum achievable g2/(2π) set by the filter design is given by 3.53 MHz and (6.36 MHz) for the setting with 5 and (4) modes per ATS. On the other hand, the crosstalk errors limit g2/(2π) to be bounded below 2 MHz (4 MHz). Thus, the crosstalk errors are currently a limiting factor and need to be further suppressed.

Adding Edges for Dealing with Correlated Errors

Extra edges are added to deal with two-qubit and three-qubit correlated errors arising from micro oscillations (e.g. cross-talk).

For the purposes of the edge weight analysis, FIG. 16A illustrates, fictitious two-qubit and three-qubit gates which act as the identity and which are applied immediately prior to the X-basis measurements of the light grey plaquettes. The two-qubit correlated errors can be viewed as an Z⊗I⊗Z-type error at a three-qubit gate location, where the Z errors act on the qubits adjacent to the small squares and small triangles of such gates. Such errors occur with probability Pcd. Similarly, the three-qubit correlated errors can be viewed as an Z⊗Z⊗Z-type error at a three-qubit gate location. Such errors occur with probability Pet. Additionally, there can be correlated errors occurring between the ancilla and data qubits at the top and bottom boundaries of the lattice in FIG. 16A. Hence, fictitious two-qubit gate locations are added at such boundaries as shown in FIG. 16A.

In order to incorporate the different types of correlated errors mentioned above into the MWPM decoding protocol, extra edges are added to the graph Gd(3D) as shown in FIG. 16B. The first type of extra edges are two-dimensional cross edges (1602) shown in that deal with two and three qubit correlated errors arising at the three-qubit fictitious gate locations of FIG. 16A. The edge-weight probabilities of such edges are labeled Pcross(bulk). Due to boundary effects, we also add dashed edges with edge-weight probabilities labeled Pcross(bound). Additionally, extra spacetime correlated edges (1604) are added at the bottom row of the graph in FIG. 16B with edge weight probabilities labeled by Pd(corr). Note that the two-qubit correlated errors arising at the top boundary of FIG. 16A result in space-time correlated edges which are already included in Gd(3D).

In addition to the extra edges added to Gd(3D), the edge-weight probabilities of a subset of the edges already included in Gd(3D) need to be renormalized. The edge-weight probabilities of the added edges in addition to the renormalized edges are given by:

Pcross(bulk)=Γ(PctPcd;2,2),

Pcross(bound)=Γ(PctPcd;1,1),

Pd(corr)=Pct

PTB2X=Γ(PZZCX(1),PIZCX(1),Pd(1),Pcd;1,1,1,1)

PTB1X=Γ(PZZCX(1),PIZCX(1),PIZCX(2),Pd(1),Pcd;2,1,1,1,1)

PC2X=Γ(PIZCX(3),PIZCX(2),PZZCX(1),Pd(1),Pcd;1,1,1,1,1)

PBB2X=Γ(PZZCX(1),PIZCX(1),Pd(1),Pcd;1,1,1,1)

PBB1X=Γ(PIZCX(1),PZZCX(1),PZICX(1),Pd(1),Pcd;2,1,1,1,1)

PC4X=Γ(PIZCX(3),PIZCX(1),PIZCX(1),Pd(1),Pcd,Pct;1,1,1,1,1,1)

PVX=Γ(PVCX,Ps,Pm,Pct;4,1,1,1)

For the space-time correlated edges, at the top row of the graph shown in FIG. 16B:

Pd,X(bound,top)=ΓPIZCX(1),PZZCX(1),PZICX(2),Pct;1,1,1,1).

Also, at the top row of FIG. 16B:

Pd,X(top)=Γ(PIZCX(1),PZZCX(1),Pct;1,1,1).

In the above equations the F function is defined as follows:

Γ(P1,P2, . . . ,Pj;n1,N2, . . . ,Nj)≡Σk=1jnkPk(1−Pk)n−1Πi=1,i≠kj(1−Pi)n.

FIG. 17 is a flowchart illustrating a process of decoding a syndrome measurement history using additional edges to correct for cross talk errors, according to some embodiments.

At 1702, a classical computer configured to decode syndrome measurement histories, such as computer system 23 illustrated in FIG. 23 storing program instructions for implementing syndrome measurement decoding, receives a syndrome measurement history for syndrome measurements of a surface code comprising qubits implemented using mechanical resonators controlled via a multiplexed control circuit (e.g. multiplexed ATS).

At 1704, the computer determines edges between vertices in the syndrome measurement history that correspond to stabilizer measurements of the surface code. The edges from which the computer may select edges to include the matching graph include vertical edges that identify measurement errors of the syndrome measurements, space-time correlated edges that identify CNOT gate failures of the surface code, two-dimensional cross-edges that identify correlated errors arising from spurious photon dissipation processes of a multiplexed control circuit that leads to cross-talk between storage modes of a set of the mechanical resonators controlled by the given multiplexed control circuit, and three-dimensional additional space-time correlated edges that identify space time errors arising from spurious photon dissipation processes of the given multiplexed control circuit or another given multiplexed control circuit that leads to cross-talk between storage modes of the set of the mechanical resonators controlled by the given multiplexed control circuit or the other given multiplexed control circuit.

At 1706, the computer determines weightings for the selected/determined edges. Also, at 1708, the computer applies a minimum weight perfect matching (MWPM) to the weighted edges to decode the syndrome measurement history for the surface code.

### Hybrid Bacon-Shor Surface Code

FIG. 18 illustrates an example hybrid Bacon-Shor surface code, according to some embodiments.

For example, in FIG. 18 the hybrid Bacon-Shor surface code (also referred to herein as a hybrid Surface/Bacon-Shor code or SBS code) has dimensions dx=5 and dz=7. The SBS code may be implemented using a bosonic architecture as described herein, such as system comprising mechanical resonators and multiplex control circuits, such as multiplexed ATSs. Each of the white boxes 1802 corresponds to an ATS. The darker grey squares (1804) and darker grey semi-circles (1806) correspond to Z-type gauge operators of the Bacon-Shor code portions of the SBS code. The lighter grey rectangles (1808) correspond to X-type gauge operators of surface code portions of the SBS code. The product of two X-type gauge operators between adjacent ATS's correspond to a stabilizer of the surface code. Data qubits are shown by the less densely hatched circles (1810). Ancilla qubits for the syndrome readout are shown by the more densely hatched circles (1812). The phononic readout modes are shown by the medium densely hatched circles. (1814). The white squares (1816) attached to the phononic readout modes show transom qubits associated with the phononic readout modes. The phononic readout mode (1814) can be used to directly measure the weight-two gauge operators. Ancilla qubits for the X-type gauge operators are initialized in the |+ state and measured in the X-basis. Ancilla qubits for the Z-type gauge operators are prepared in the |0 state and measured in the Z-basis. All the two-qubit gates (1818 for X-type gauge operators and 1820 for Z-type gauge operators) are CNOT gates. The numbers (1822) beside each operator indicate the time step in which it is applied.

In some embodiments, a hybrid Bacon-Shor surface code (SBS code) may reduce a number of modes coupled to an ATS, as compared to a traditional non-hybrid surface code. For example, a SBS code may only couple four phononic modes per ATS instead of five phononic modes per ATS as is the case for a traditional surface code. As discussed above in the section regarding Cross-Talk Mitigation Using Mode Frequency Optimization, having only four modes instead of five modes coupled to an ATS may reduce the probabilities of cross-talk, such as Type I, Type II, and Type III errors. Additionally, coupling fewer modes to an ATS may provide additional flexibility in selecting optimized frequencies and pump detunings to reduce Type III errors.

Hybrid Bacon-Shor surface codes (SBS codes) belong to a family of Compass codes, where stabilizers used to correct one type of Pauli error (say X-type errors) are the stabilizers of the Bacon-Shor code, and stabilizers used to correct the other type of Pauli error (say Z-type errors) are surface code stabilizers. SBS codes are subsystem stabilizer codes with the corresponding gauge group given by:

G=Xi,jXi+1,j,Zi,jZi,j+1Zi+1,jZi+1,j+1,Z1,2k−1Z1,2k,Zd,2kZd,2+1

where i∈{1, 2, . . . , dz−1},j∈{1, 2, . . . , dx−1} and

\(k \in {\left\{ {1,2,\ldots\mspace{14mu},\ \frac{d_{x} - 1}{2}} \right\}.}\)

Here dx corresponds to the minimum weight of a logical X operator (which consists of horizontal X strings) and dz corresponds to the minimum weight of a logical Z operator (which consists of vertical Z strings). An example of a dx=5 and dz=7 SBS code is shown in FIG. 18. The darker grey squares (1804) and darker grey semi-circles (1806) correspond to the Z-type gauge operators in the above equation and are used to detect X-type Pauli errors. The lighter grey rectangles (1808) correspond to the X-type gauge operators in the above equation and are used to detect Z-type errors.

The stabilizer group representing the logical subspace of SBS codes is given by:

\({S = \left\langle {{X_{i,j}X_{i,{j + 1}}X_{{i + 1},j}X_{{i + 1},{j + 1}}},{X_{{2t},d_{x}}X_{{{2t} + 1},d_{x}}X_{{{2t} - 1},1}X_{{2t},1}},{\prod\limits_{i = 1}^{d_{z}}{Z_{i,j}Z_{i,{j + 1}}}}} \right\rangle},\)

where

\(t \in {\left\{ {1,2,\ldots\mspace{14mu},\frac{d_{z} - 1}{2}} \right\}.}\)

The weight-four operator Xi,jXi,j+1Xi+1,jXi+1,j+1 in the bulk is a surface code stabilizer which can be measured by taking the product of the measured eigenvalues of the weight-two gauge operators Xi,jXi+1,j and Xi,j+1Xi+1,j+1. Furthermore, Πi=1dZi,jZi,j+1 is a Bacon-Shor type stabilizer whose eigenvalue is obtained by taking the product of the measured eigenvalue of weight-four and weight-two Z-type gauge operators along a vertical strip. It is noted that due to the non-commutation of Z and X-type gauge operators in the equation above for the gage groups (G), only stabilizer measurement outcomes are used to correct errors. The gate scheduling for the CNOT gates used to measure the gauge operators the equation above for the gage groups (G) are chosen to be symmetry in the bulk, which is contrary to the gate scheduling chosen in other Bacon Shor hybrid codes. Such a scheduling is chosen so that three parity measurements between the phononic readout mode and the transmon qubit can be implemented in one syndrome measurement cycle. The circuit for measuring the weight-two X-type gauge operators of the equation above for the gage groups (G) is shown in FIG. 20.

For example, in FIG. 20, phononic read out modes (1814) are shown with associated transmons (1816) and wherein CNOT gates (1820) are applied between the data qubits 1810 and the phononic readout modes 1814. Note that the CNOT gate scheduling is selected such that three (or more) parity measurements (2002) are performed in a given syndrome cycle before the phononic readout mode must be reset to the |+ state (2004).

Thin-stripped surface codes may require five modes per ATS to measure the surface code stabilizers. In particular, a crucial step when performing an X-basis measurement in a thin-stripped surface code is to swap ancillas (shown as the darker grey circles 1824) with other ancillas with associated transmons (e.g. ancillas 1814) (after all four CNOT gates have been applied) and perform repeated parity measurements between the ancillas (1814) and a transmon qubit (white square (1816) connected to the phononic readout mode ancilla (1814)).

However, in some embodiments, in order to improve the measurement fidelity, the SBS codes only require four modes per ATS. Such a reduction in the number of modes per ATS is shown in FIGS. 19A and 19B. For example in FIG. 19A the un-used phononic 1824 are highlighted and in FIG. 19B the unused phononic modes 1924 are omitted. In particular, due to the decomposition of the surface code stabilizers as a product of two weight-two X-type gauge operators in the equation above for the gage groups (G), the phononic readout mode can be used directly to measure such weight-two gauge operators. Furthermore, since the ancilla qubits for Z-type gauge operators are measured in the Z-basis, such measurements can be implemented directly without the use of a phononic readout. As such, all red vertices 1824 in FIGS. 18 and 19A can be removed as shown in FIG. 19B when implementing the SBS code.

As shown in the table discussed above with regard to the section Cross-Talk Mitigation Using Mode Frequency Optimization it can be seen that crosstalk errors are reduced by roughly one order of magnitude when only four modes are coupled to an ATS compared to five modes. As such, the hybrid Bacon-Shor surface code as described herein can correct both phase-flip and bit-flip errors while substantially reducing the effects of cross-talk errors as compared to the thin-stripped surface codes.

It is noted that other Bacon Shor surface codes may use flag qubits to measure the gauge operators of the code. However, the extra flag qubits and larger circuit depth required to measure such gauge operators contribute to an increase in logical failure rates for the same code parameters due to the larger number of fault locations. In contrast, the architecture proposed in this work has a circuit depth of 6 time steps compared to 11 time steps for measuring the stabilizers in other approached using flag qubits and does not require any flag qubits. The total qubit count ntot for the implementation of the SBS code considered in this work is:

\(n_{tot} = {\frac{{d_{x}\left( {{5d_{z}} - 1} \right)} - d_{z} - 1}{2}.}\)

Additionally, it is pointed out that because no flag qubits are required to measure the stabilizers of the SBS code, the MWPM decoder used to decode the error syndromes requires fewer operations as compared to MWPM decoders used to decode Bacon-Shor codes that include flag qubits. This at least in part because dynamical edge weight renormalization in each syndrome measurement round is not necessary when using a hybrid Bacon-Shor surface code (SBS code) as described herein.

## Illustrative Computer System

FIG. 23 is a block diagram illustrating an example computing device that may be used in at least some embodiments.

FIG. 23 illustrates such a general-purpose computing device 2300 as may be used in any of the embodiments described herein. In the illustrated embodiment, computing device 2300 includes one or more processors 2310 coupled to a system memory 2320 (which may comprise both non-volatile and volatile memory modules) via an input/output (I/O) interface 2330. Computing device 2300 further includes a network interface 2340 coupled to I/O interface 2330.

In various embodiments, computing device 2300 may be a uniprocessor system including one processor 2310, or a multiprocessor system including several processors 2310 (e.g., two, four, eight, or another suitable number). Processors 2310 may be any suitable processors capable of executing instructions. For example, in various embodiments, processors 2310 may be general-purpose or embedded processors implementing any of a variety of instruction set architectures (ISAs), such as the x86, PowerPC, SPARC, or MIPS ISAs, or any other suitable ISA. In multiprocessor systems, each of processors 2310 may commonly, but not necessarily, implement the same ISA. In some implementations, graphics processing units (GPUs) may be used instead of, or in addition to, conventional processors.

System memory 2320 may be configured to store instructions and data accessible by processor(s) 2310. In at least some embodiments, the system memory 2320 may comprise both volatile and non-volatile portions; in other embodiments, only volatile memory may be used. In various embodiments, the volatile portion of system memory 2320 may be implemented using any suitable memory technology, such as static random access memory (SRAM), synchronous dynamic RAM or any other type of memory. For the non-volatile portion of system memory (which may comprise one or more NVDIMMs, for example), in some embodiments flash-based memory devices, including NAND-flash devices, may be used. In at least some embodiments, the non-volatile portion of the system memory may include a power source, such as a supercapacitor or other power storage device (e.g., a battery). In various embodiments, memristor based resistive random access memory (ReRAM), three-dimensional NAND technologies, Ferroelectric RAM, magnetoresistive RAM (MRAM), or any of various types of phase change memory (PCM) may be used at least for the non-volatile portion of system memory. In the illustrated embodiment, program instructions and data implementing one or more desired functions, such as those methods, techniques, and data described above, are shown stored within system memory 2320 as code 2325 and data 2326.

In some embodiments, I/O interface 2330 may be configured to coordinate I/O traffic between processor 2310, system memory 2320, and any peripheral devices in the device, including network interface 2340 or other peripheral interfaces such as various types of persistent and/or volatile storage devices. In some embodiments, I/O interface 2330 may perform any necessary protocol, timing or other data transformations to convert data signals from one component (e.g., system memory 2320) into a format suitable for use by another component (e.g., processor 2310). In some embodiments, I/O interface 2330 may include support for devices attached through various types of peripheral buses, such as a variant of the Peripheral Component Interconnect (PCI) bus standard or the Universal Serial Bus (USB) standard, for example. In some embodiments, the function of I/O interface 2330 may be split into two or more separate components, such as a north bridge and a south bridge, for example. Also, in some embodiments some or all of the functionality of I/O interface 2330, such as an interface to system memory 2320, may be incorporated directly into processor 2310.

Network interface 2340 may be configured to allow data to be exchanged between computing device 2300 and other devices 2360 attached to a network or networks 2350, such as other computer systems or devices. In various embodiments, network interface 2340 may support communication via any suitable wired or wireless general data networks, such as types of Ethernet network, for example. Additionally, network interface 2340 may support communication via telecommunications/telephony networks such as analog voice networks or digital fiber communications networks, via storage area networks such as Fibre Channel SANs, or via any other suitable type of network and/or protocol.

In some embodiments, system memory 2320 may represent one embodiment of a computer-accessible medium configured to store at least a subset of program instructions and data used for implementing the methods and apparatus discussed in the context of FIG. 1 through FIG. 22. However, in other embodiments, program instructions and/or data may be received, sent or stored upon different types of computer-accessible media. Generally speaking, a computer-accessible medium may include non-transitory storage media or memory media such as magnetic or optical media, e.g., disk or DVD/CD coupled to computing device 2300 via I/O interface 2330. A non-transitory computer-accessible storage medium may also include any volatile or non-volatile media such as RAM (e.g. SDRAM, DDR SDRAM, RDRAM, SRAM, etc.), ROM, etc., that may be included in some embodiments of computing device 2300 as system memory 2320 or another type of memory. In some embodiments, a plurality of non-transitory computer-readable storage media may collectively store program instructions that when executed on or across one or more processors implement at least a subset of the methods and techniques described above. A computer-accessible medium may further include transmission media or signals such as electrical, electromagnetic, or digital signals, conveyed via a communication medium such as a network and/or a wireless link, such as may be implemented via network interface 2340. Portions or all of multiple computing devices such as that illustrated in FIG. 23 may be used to implement the described functionality in various embodiments; for example, software components running on a variety of different devices and servers may collaborate to provide the functionality. In some embodiments, portions of the described functionality may be implemented using storage devices, network devices, or special-purpose computer systems, in addition to or instead of being implemented using general-purpose computer systems. The term “computing device”, as used herein, refers to at least all these types of devices, and is not limited to these types of devices.

## CONCLUSION

Various embodiments may further include receiving, sending or storing instructions and/or data implemented in accordance with the foregoing description upon a computer-accessible medium. Generally speaking, a computer-accessible medium may include storage media or memory media such as magnetic or optical media, e.g., disk or DVD/CD-ROM, volatile or non-volatile media such as RAM (e.g. SDRAM, DDR, RDRAM, SRAM, etc.), ROM, etc., as well as transmission media or signals such as electrical, electromagnetic, or digital signals, conveyed via a communication medium such as network and/or a wireless link.

The various methods as illustrated in the Figures and described herein represent exemplary embodiments of methods. The methods may be implemented in software, hardware, or a combination thereof. The order of method may be changed, and various elements may be added, reordered, combined, omitted, modified, etc.

Various modifications and changes may be made as would be obvious to a person skilled in the art having the benefit of this disclosure. It is intended to embrace all such modifications and changes and, accordingly, the above description to be regarded in an illustrative rather than a restrictive sense.

