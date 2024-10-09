# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates to a method of operation of a quantum processing element and an advanced processing apparatus comprising a plurality of quantum processing elements operated in accordance with the method.

## BACKGROUND OF THE INVENTION

The power and capacity of computing components such as microprocessors and memory circuits has been increasing for the last 50 years, as the size of the functional units, such as transistors, has been decreasing. This trend is now reaching a limit, however, as it is difficult to make the current functional units (such as MOSFETs) any smaller without affecting their operation.

The technology employed to manufacture conventional silicon integrated circuits is today well established. Current microprocessors feature several hundreds of millions of transistors which are manufactured in high throughput lines.

Developments are ongoing to implement new types of advanced processing apparatuses that can implement powerful computations exploiting the rules of quantum mechanics. Such advanced processing apparatuses promise computational capacities well beyond current devices for a specific range of algorithms. Approaches to the realisation of devices for implementing quantum bits (qubits), the basic computational unit of a quantum processor, have been explored with different levels of success. A workable quantum processor needs to be able to perform two-qubit operations with low-error thresholds and be scalable. For example, semiconductor based qubits have been developed and described in a number of earlier patent publications, including U.S. Pat. No. 6,472,681 (Kane), U.S. Pat. No. 6,369,404 (Kane). The operation of these qubits is based on the exploitation of the quantum effects of a single dopant atom in a silicon crystalline lattice and the interaction between qubits is mediated by electron exchange coupling.

One of the problems related to this model is that the exchange interaction between electrons decays exponentially with donor separation and is highly dependent on the precise placement of the donors within a single lattice site, due to the oscillatory profile of the electron wave-function. The successful implementation of this architecture requires positioning of donors, separated by only 15 nm, with sub-nm precision. Such a level of precision makes the fabrication of the architecture very challenging, as discussed for example in U.S. Pat. No. 7,547,648 (Ruess et al.).

It has also been proposed to encode quantum information using the spin states of semiconductor quantum dots (Loss and DiVincenzo (Loss, DiVincenzo, DP quantum computation with quantum dots. Phys Rev. A56, 120; 1998).). This proposal primarily envisaged the use of quantum dots formed using electrostatic gates on a GaAs/AlGaAs heterostructure. However, the limited coherence time and the associated fidelity of the quantum state in these systems represent a significant hurdle to application of quantum dots in a quantum processor. Experimental work has been done in GaAs/AlGaAs on quantum dot qubits, but to realise large-scale arrays of such structures will require new manufacturing process technologies to be developed. More importantly, these materials suffer from problems with fidelity and dephasing time due to the presence of nuclear spins that are inherent to the GaAs crystal lattice.

Superconducting qubits have recently achieved low-error performance and a promising scalability. These qubits however have a macroscopic size (hundreds of micrometres scale) which prevents architectures from being fabricated with a large number of qubits within a small chip size. The large size, combined with the operation a GHz frequencies, can pose challenges in controlling the electromagnetic modes of a large number of qubits hosted in a cavity wider than the wavelength of the electromagnetic fields.

## SUMMARY OF THE INVENTION

Embodiments of the invention propose a method to manipulate spin qubits with electric fields. The qubits manipulated in accordance with the method can be separated by hundreds of nanometres while preserving coupling capabilities. This substantially relaxes the precision requirements for fabrication. Advantageously, the schemes are compatible with the accuracy in donor placement achieved with ion implantation, as well as with scanning tunnelling microscope lithography.

In accordance with a first aspect, the present invention provides a method of operation of a quantum processing element, the processing element comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a distance from the
    interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a magnetic field to the quantum processing element to
    separate the energy of the spin states associated with an electron
    and a nucleus of the donor atom; and
  - applying an electric field in the region between the interface and
    the donor atom to modulate a hyperfine interaction between the
    electron and the nucleus and control the quantum state of a quantum
    bit associated with a pair of electron-nuclear spin eigenstates of
    the electron and the nucleus.

The pair of electron-nuclear spin eigenstates comprises the ‘electron spin up-nuclear spin down’ and ‘electron spin down-nuclear spin up’ eigenstates. This type of qubit can be referred to as flip-flop qubit.

The electric field in the region between the interface and the donor atom may be applied by applying an oscillating electric signal to the electrode. The electrode may be an independent electrode or part of a structure suitable for addressing multiple processing elements.

In an embodiment, the frequency of the oscillating electric signal is selected based on the amplitude of the applied continuous magnetic field. This frequency may be also selected to be equal to an excitation frequency of the quantum bit and detuned from the orbital excitation frequency of the electron to prevent orbital excitation of the electron. The energy difference between the orbital states of the electron, and therefore the electron orbital excitation frequency, depends sensitively on the depth of the electron from the interface between the semiconductor and the dielectric material, because the electron can be displaced from the donor to the interface by the electric field applied in its vicinity.

In an embodiment, the oscillating electric signal and the magnetic field may be applied simultaneously to induce a transition in the quantum state of the quantum bit.

In an embodiment, the method further comprises the step of applying an oscillating magnetic field to the processing element to transfer the quantum state associated with the pair of electron-nuclear spin eigenstates to a quantum state associated with the nuclear spin to implement a nuclear spin quantum bit.

In accordance with a second aspect, the present invention provides a method of operation of a quantum processing element, the processing element comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a distance from the
    interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a continuous magnetic field to the quantum processing
    element to separate spin states associated with an electron and a
    nucleus of the donor atom;
  - applying an oscillating magnetic field which oscillates at a
    frequency close to a Zeeman frequency of the electron; and
  - applying an electric field in the region between the interface and
    the donor atom to modulate a hyperfine interaction between the
    electron and the nucleus and control the quantum state of a quantum
    bit associated with the spin of the nucleus;
  - wherein the frequency of the oscillating magnetic field is selected
    based on the frequency of the oscillating electric signal.

This type of qubit can be referred to as nuclear-spin qubit. One advantage of using the nuclear-spin as a qubit is that it has a long coherence time since it is less prone to electromagnetic interaction with the external environment.

In an embodiment, the frequency of the oscillating magnetic field is selected to be detuned from the electron spin excitation frequency to prevent flipping of the electron spin quantum state.

In an embodiment, the oscillating electric signal and oscillating magnetic field are applied simultaneously to induce a transition in the quantum state of the nuclear spin quantum bit.

In embodiments, the frequency of the oscillating magnetic field is selected to be smaller than the frequency of the oscillating electric signal by an amount equal to a nuclear spin Zeeman frequency.

Embodiments of the method of the first aspect or the method of the second aspect comprises the step of applying a biasing DC electric signal to the electrode to bias the electron in a region where the hyperfine interaction is highly sensitive to small variations in the electric field. This may be attained by displacing the electron wave function such that it spans an extended region between the donor nucleus and the interface between the semiconductor and the dielectric.

A biasing electric signal may be applied to the electrode to bias the electron in a region in proximity of the interface or in a region close to the nucleus to minimise an interaction of the quantum state of the quantum bit with an external electromagnetic environment.

In some embodiments, the method further comprises the step of applying an electric bias to the conductive electrode to displace the electron and create an electric dipole associated with the processing element. The dipole created can interact with another electric dipole of another processing element via dipole-dipole interaction to allow interaction of the quantum states of two processing elements and coupling of two qubits. In order to allow controllable coupling, the electrical bias may be maintained for a predetermined period of time, and then switched off.

In some embodiments, the method further comprises the steps of confining electromagnetic field modes into a spatial region in proximity of the processing element. An arrangement for confining electromagnetic modes may be disposed in proximity of the processing element. The electromagnetic field modes may be quantized to comprise zero, one, or more photons. The interaction of the quantized electromagnetic field modes and the electron may be used to enable coupling of the zero, one or more photons to the quantum state of the quantum bit.

The arrangement used for confining electromagnetic modes may be a resonator, such as a microwave resonating cavity or a coplanar waveguide resonator. The state of the quantum bit may be read-out by measuring the shift in the resonance frequency of the resonator caused by the coupling of the photon(s) to the qubit.

The quantized modes of the zero, one or more photons may be spatially extended through the resonator, such that the electromagnetic fields associated with the photon modes overlap with multiple quantum bits, enabling long distance quantum bit coupling. This coupling mechanism, intermediate by a photon, may be used to couple qubits which are at least 1 μm from each other, and up to a distance comparable with the wavelength of the photon.

In an embodiment, the method further comprises the step of detuning the processing element from the resonator modes to prevent decay of the quantum state of the quantum bit into a photon.

In accordance with the third aspect, the present invention provides a method of coupling quantum states of two processing elements, each of the processing elements comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a continuous magnetic field to the quantum processing
    elements to separate spin states associated with an electron and a
    nucleus of the donor atoms; and
  - applying an electric signal to each of the conductive electrodes to
    displace the electrons and create two electric dipoles associated
    with the respective processing elements to enable coupling of the
    quantum states of the two quantum bits associated with the two
    processing elements.

In accordance with the fourth aspect, the present invention provides a method of coupling quantum states of two processing elements, each of the processing elements comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a continuous magnetic field to the quantum processing
    elements to separate spin states associated with an electron and a
    nucleus of the donor atoms;
  - applying an oscillating magnetic field which oscillates at a
    frequency close to a Zeeman frequency of the electron to each of the
    processing elements; and
  - applying an electric signal to each of the conductive electrodes to
    displace the electrons and create two electric dipoles associated
    with the respective processing elements to enable coupling of the
    quantum states of the two quantum bits associated with the two
    processing elements.

In some embodiments, the two processing elements are disposed at least 150 nm apart.

In accordance with the fifth aspect, the present invention provides a method of coupling quantum states of two processing elements, each of the processing elements comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a continuous magnetic field to the quantum processing
    elements to separate spin states associated with an electron and a
    nucleus of the donor atoms; and
  - confining electromagnetic field modes into a spatial region in
    proximity of the processing elements in a manner such that a
    quantized electric field is induced in the region between the
    interface and the donor atom to modulate a hyperfine interaction
    between the electron and the nucleus of each processing element and
    couple the quantum state of a quantum bit associated with a pair of
    electron-nuclear spin eigenstates of one processing element to a
    quantum bit associated with a pair of electron-nuclear spin
    eigenstates of the other processing element.

In accordance with the sixth aspect, the present invention provides a method of coupling quantum states of two processing elements, each of the processing elements comprising:


- - a semiconductor and a dielectric material forming an interface with
    the semiconductor;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface; and
  - a conductive electrode disposed on the dielectric material; the
    method comprising the steps of:
  - applying a continuous magnetic field to the quantum processing
    elements to separate spin states associated with an electron and a
    nucleus of the donor atoms;
  - applying an oscillating magnetic field which oscillates at a
    frequency close to a Zeeman frequency of the electron to each of the
    processing elements; and
  - confining electromagnetic field modes into a spatial region in
    proximity of the processing elements in a manner such that a
    quantized electric field is induced in the region between the
    interface and the donor atom to modulate a hyperfine interaction
    between the electron and the nucleus of each processing element and
    couple the quantum state of a quantum bit associated with a nuclear
    spin of one processing element to a quantum bit associated with a
    nuclear spin of the other processing element;
  - wherein a frequency of the oscillating magnetic field is selected
    based on a resonance frequency of the quantized electromagnetic
    field.

In the fifth and sixth aspect, the two processing elements may be disposed at least 1 μm apart. The two processing elements may be disposed in the proximity of a resonator and be tuned in resonance with each other while detuned from the resonator mode. In this way respective quantum bits are coupled via virtual photons.

The quantum state of the two quantum bits can be controlled by of applying an electrical signal to the electrodes. The electrical signal may be applied simultaneously for the two processing elements or sequentially to one qubit before the other, to set the two quantum states.

Conductive electrodes may be used to bias the electrons in a region in proximity of the interface or close to the nucleus to minimise the interaction of the quantum state of each quantum bit with an external electromagnetic environment and minimise coupling between the two quantum bits. The biasing electrodes may be separate electrodes to the electrodes used to control the quantum states.

The biasing of the electrons may be performed before or after the coupling takes place. In some embodiments the electrons are normally kept at the interface between semiconductor and dielectric, away from the donor, unless a coupling operation is being performed.

In accordance with a seventh aspect, the present invention provides an advanced quantum processing apparatus, comprising a plurality of processing elements disposed in an electromagnetic resonator; each of processing elements comprising:


- - a semiconductor and a dielectric material forming an interface;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface;
  - a conductive electrode disposed on the dielectric material;
  - wherein each processing element is disposed in relation to the
    electromagnetic resonator in a manner such that an electromagnetic
    field mode in the resonator induces a quantized electric field in
    the region between the interface and the donor atom and couples to
    the quantum state of a quantum bit associated with a pair of
    electron-nuclear spin eigenstates of the electron and the nucleus.

In accordance with an eight aspect, the present invention provides an advanced processing apparatus, comprising a plurality of processing elements disposed in an electromagnetic resonator; each of processing elements comprising:


- - a semiconductor and a dielectric material forming an interface;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface;
  - a conductive electrode disposed on the dielectric material;
  - wherein each processing element is disposed in relation to the
    electromagnetic resonator in a manner such that an electromagnetic
    field mode in the resonator induces a quantized electric field in
    the region between the interface and the donor atom and couples to
    the quantum state of a quantum bit associated with a nuclear spin of
    one or more of the processing elements.

In an embodiment, each processing element is disposed in relation to the electromagnetic resonator in a manner such that an electromagnetic field mode in the resonator induces a modulation of the hyperfine interaction between the electron and the nucleus of one or more of the processing elements.

In embodiments, the two processing elements are disposed at least 1 μm apart. The resonator may comprise a microwave resonating cavity or a coplanar waveguide resonator.

In embodiments, the coplanar waveguide resonator comprises one or more discontinuities and the distance between the discontinuities is selected based on the desired frequency of the quantized electric field induced the region between the interface and the donor atom.

In accordance with the ninth aspect, the present invention provides an advanced processing apparatus, comprising a plurality of processing elements disposed in a two-dimensional arrangement; each of processing elements comprising:


- - a semiconductor and a dielectric material forming an interface;
  - a donor atom embedded in the semiconductor at a given distance from
    the interface;
  - a conductive electrode disposed on the dielectric material;
  - wherein one or more processing elements are operated in accordance
    with the method of the first aspect.

In embodiments, the processing elements may coupled to each other in accordance with the method of the second, third or fourth aspect.

Embodiments of the apparatus can be manufactured using a CMOS process.

Advantageous embodiments of the present invention provide methods to couple spins to electric fields, mediated by the charge state of an electron in an advanced processing apparatus comprising MOS-like processing elements including a buried donor atom.

The spin qubits can be controlled using electrical means. Qubits can be associated electron-nuclear spin states of the dopant atom or nuclear spin states. Nuclear spin qubits can be defined using an oscillating magnetic field. Using isotopically enriched 28silicon as semiconductor substrate for the processing elements, the method allows the combination of long coherence times of nuclear-spin qubits with fast manipulation speeds of charge qubits. Advantageously, 2-qubit coupling can be implemented via direct electric dipole-dipole interaction between processing elements. This interaction can reach longer distances than direct spin-spin interaction and drastically relaxes the fabrication precision demands for developing a spin-based quantum computer. Electric dipoles for the processing elements are created using an electrical biasing signal which can be applied via the same electrode which is used to manipulate the quantum state or a separate biasing electrode.

Another advantage of the method is provided by the possibility of coupling the quantum states of qubits to single microwave photons, including the nuclear-spin qubit. This is a remarkable advantage given the small magnetic dipole and gyromagnetic moment of nuclear spins and their usual insensitivity to electric fields. The method opens new possibilities for coupling nuclear-spin qubits at long distances and also for non-demolition read-out via a microwave resonator.

An advantageous architecture to implement the method is also disclosed. In this architecture a microwave resonator is coupled to the processing elements. The microwave resonator may function as main electrical electrode to control the quantum state of the qubits. It also allows coupling the quantum state of the microwave photons with the quantum state of the qubit, and to use the photons to mediate the coupling between several quantum bits throughout the architecture.

## DETAILED DESCRIPTION OF EMBODIMENTS

In the following description a method for operating a processing element or a pair of processing elements in accordance with embodiments is described.

Referring to FIG. 1, there is shown a processing element 10 which can be operated using a method in accordance with embodiments. FIG. 1(a) is a top view of the processing element and FIG. 1(b) is a side cross-section. The processing element 10 may be used as a qubit element for a quantum computer comprising a plurality of these processing elements. Processing element 10 comprises a semiconductor substrate 12 and a dielectric 14, in this example being 28silicon and silicon dioxide respectively and forming a Si/SiO2 interface 17. A donor atom 18 is located within the substrate 12 inside region 19 under gate 16. The donor can be introduced into the substrate using nano-fabrication techniques, such the hydrogen lithography provided by scanning-tunneling-microscopes, or the industry-standard ion implantation techniques. Processing element 10 includes a single atom 18 embedded in the silicon crystal. However, the methods described herein may be applied to processing elements including clusters of more than one embedded atom.

A gate electrode 16 is located above region 19 and is operable to interact with the donor atom 18. For example, gate 16 may be used to induce an AC electric field in the region between the interface 17 and the donor atom 18 to modulate a hyperfine interaction between the electron and the nucleus.

The electric field can be used to control the quantum state of a quantum bit associated with the pair of electron-nuclear spin eigenstates ‘electron spin up-nuclear spin down’ and ‘electron spin down-nuclear spin up’. This type of qubit is referred to herein as ‘flip-flop qubit’.

Alternatively, the AC electric field can be used to control the quantum state of a quantum bit associated with a spin of the nucleus, ‘nuclear-spin’ qubit herein. In this case the AC electric filed works in synergy with an applied oscillating magnetic field.

FIG. 2 shows a plot 25 of the hyperfine interaction between the electron and the nucleus as a function of the electric field resulting from the voltage applied to electrode 16. Insets 22, 24 and 26 show the electron wavefunction, inside region 19, under different vertical electric fields, arising from an electrical signal applied to gate 16. Electrode 16 therefore controls the position of the electron in the region between the nucleus and the interface 17.

A biasing electric signal can be applied to bias the electron in a region in proximity of the interface (as shown in inset 22), or in a region close to the nucleus (as shown inset 26), to minimise an interaction of the quantum state of the quantum bit with an external electromagnetic environment.

Furthermore a biasing electric signal can be applied to position the electron in a region of high sensitivity of the hyperfine interaction to the electric field. In this region, approximately half of the electron density resides at the interface, and the other half at the embedded donor atom (as shown in inset 24).

Electrode 16 may be used to apply an AC electrical signal to interact with the quantum state of the qubit.

Processing element 10 only shows one electrode 16 used to apply the biasing electrical signal and the AC electrical signal. However, in a variation of processing element 10 separate electrodes can be used.

Donor atom 18 may be a phosphorous atom embedded in an isotopically pure 28Si crystal at a depth zd from the interface with a thin SiO2 layer. The orbital wave-function W of the donor-bound electron can be controlled by a vertical electric field Ez applied by metal gate 16. It changes from a bulk-like donor state at low electric fields to an interface-like state at high-fields.

The hyperfine interaction A(Ez), proportional to the square amplitude of the electron wave-function at the donor site, changes accordingly from the bulk value A≈117 MHz to A≈0 when the electron is fully displaced to the interface. At the ionization point, where the electron is shared halfway between donor and interface, A(Ez) can vary strongly upon the application of a small voltage on the top gate. Shifting the electron wave-function from the donor to the interface also results in the creation of an electric dipole μe=ed, where e is the electron charge and d is the separation between the mean positions of the donor-bound and interface-bound wave-functions. The induced electric dipole is one of the important features exploited in embodiments of the invention described herein.

Referring now to FIG. 3 there is shown a flow-diagram 30 with the basic steps used for operating the quantum processing element. At step 32 a magnetic field is applied to the quantum processing element to separate spin states associated with an electron and a nucleus of the donor atom. At step 34 an electric field is induced in the region between the interface and the donor atom to modulate a hyperfine interaction between the electron and the nucleus and control the quantum state of a quantum bit associated with a pair of electron-nuclear spin eigenstates of the electron and the nucleus.

FIG. 4(a) shows a Bloch sphere 40 of an electron-nuclear spin system coupled to an electric field via hyperfine interaction A(E). To perform quantum state manipulations a magnetic field is also applied to the processing element to separate spin states associated with an electron and a nucleus of the donor atom. Under an applied magnetic field B0, the spin Hamiltonian reads:

spin=B+A  (1)

B=B0(γeSz−γnIz)  (2)

A=AS·I  (3)

Here γe and γn are the electron and nucleus gyromagnetic ratios, respectively, and A is the hyperfine coupling. S=(Sx,Sy,Sz) and I=(Ix,Iy,Iz) are the electron and nucleus spin operators, respectively. In silicon, γe≈28 GHz/T, whereas γn and A depend on the donor type according to Table 1.

For simplicity, we consider a nuclear spin I=½, which can be that of a 31P donor. The Hamiltonian Bdefines electron-nuclear spin eigenstates |↑>, |↓>, |↓> and |↑>, whereas A defines |↑>, |↓>, (|↓)−|↑))/√{square root over (2)} and (|↓+|↑))/√{square root over (2)}. Under strong enough magnetic fields (γ+B0>>A, where γ+=γe+γn), the subspace |↑> and |↓> are approximately eigenstates of the system, with frequency separation:

∈ff(A)=√{square root over ((γ+B0)2+[A(Ez)]2)}≈γ+B0  (4)

This subspace is referred to herein as the ‘flip-flop’ qubit.

The hyperfine interaction AS·I is a transverse term in the flip-flop basis. Controlling A via electrical means opens up new ways for electron-nuclear spins control. Modulating A(Ez) at the frequency ∈ff(A), causes an electric dipole spin resonance (EDSR) transition between the |↓>|, ↑> basis states. A conceptually similar mechanism is involved in the resonant drive of a 3-electron, 2-dot hybrid qubit.

In FIG. 1, the electrical signal applied to gate 16 can create a strong vertical electric field that pulls the electron wavefunction from the donor 18 towards interface 17. Since the hyperfine coupling is proportional to the electron orbital wavefunction |ψ|2 at the donor site, it abruptly shifts from its maximum value to zero when the electron is ionized to the interface, as shown in FIG. 2(b). The intermediate situation, in which the electron is equally shared between donor and interface, is the best point to control the spin state via an electrical signal applied to electrode 16. Here the hyperfine interaction has its strongest variation. FIG. 4 schematically depicts such an optimal operation.

The orbital wave function of the electron in this scenario can be approximated as a two level system, |d for the electron at the donor, and |i for the electron at the interface. At the intermediate location, the eigenstates |g=(|d−|i)/√{square root over (2)} and |e=(|d+|i)/√{square root over (2)} are separated by an energy difference equal to the tunnel coupling Vt, according to the Hamiltonian, in the |d, |ibasis:

\(\begin{matrix}
{{\mathcal{H}_{orb} = \frac{{v_{t}\sigma_{x}} - {\left\lbrack {{e\left( {E_{z} - E_{z}^{0}} \right)}d\text{/}h} \right\rbrack \sigma_{z}}}{2}},} & (5)
\end{matrix}\)

where σz and σx are Pauli matrices. The electron vertical position is represented by the Pauli σz operator, where we assume σz=−1 for the electron at the donor and σz=+1 for the electron at the interface. The hyperfine coupling is then dependent on the electron orbital position according to:

\(\begin{matrix}
{\mathcal{H}_{A}^{orb} = {{A\left( \frac{1 - \sigma_{z}}{2} \right)}{S \cdot I}}} & (6)
\end{matrix}\)

The electron ground |g and excited |e orbital eigenstates depend on Ez−Ez0 and have an energy difference given by:

∈o=√{square root over ((Vt)2+[e(Ez−Ez0)d/h]2)}

This results in a transverse coupling g, between the flip-flop qubit and the electron charge states:

\(\begin{matrix}
{g_{so} = {\frac{A}{4}\frac{V_{t}}{ɛ_{o}}}} & (7)
\end{matrix}\)

A vertical electric field of amplitude Eac, oscillating at a frequency νE equal ∈0, would drive transitions between the charge eigenstates at a rate (half Rabi-frequency).

\(\begin{matrix}
{g_{E} = {\frac{{eE}_{ac}d}{4h}{\frac{V_{t}}{ɛ_{o}}.}}} & (8)
\end{matrix}\)

An electrical modulating signal applied to electrode 16 that modulates A at a frequency equal to ∈ff(A) can be used to drive the qubit between |↑> and |↓>, at a Rabi frequency proportional to the modulation amplitude. This qubit gate can be achieved electrically by using an oscillating electric field, with frequency νE=∈ff(A), which periodically wiggles the electron between the donor and the interface. This orbital dynamics is described by the following Hamiltonian:

\(\begin{matrix}
{{\mathcal{H}_{E} = \frac{{eE}_{ac}d\; {\cos \left( {2\pi \; v_{E}t} \right)}\sigma_{z}}{2h}},} & (9)
\end{matrix}\)

where Eac is the electric field amplitude, d the donor-interface distance and h the Planck constant. The total Hamiltonian describing flip-flop drive by an AC electric field is:

drive=B+Aorb+orb+E  (10)

FIG. 4(c) shows and an energy level diagram of a ‘flip-flop’ qubit driven using an AC electric field. In order to prevent excitation of the electron orbital state, and therefore suppress relaxation due to coupling to phonons, the state |e is minimally excited, by choosing δso>>gso and δE>>gE, where δE=∈o−νE. Under these conditions, and if δE=δso, the ‘flip-flop’ qubit is driven at a rate (half Rabi frequency), to second order:

\(\begin{matrix}
{g_{E}^{ff} = {\frac{g_{so}g_{E}}{2}\left( {\frac{1}{\delta_{so}} + \frac{1}{\delta_{E}}} \right)}} & (11)
\end{matrix}\)

δE and δso may be selected to be large enough as to prevent electron orbital excitation, but not too large since this would reduce the flip-flop transition rate considerably. When a state excitation is to be prevented, the detuning (δE and δso) may be selected to be at least 10 times the coupling rates to it (gE and gso). This ensures less than 1% excitation probability of charge states.

As an example, for a 31P donor, A/4≈29 MHz, which sets δE=δso=290 MHz. If this donor is d=15 nm deep in the silicon, a maximum field of Eac=32 V/m can be applied while still preventing orbital excitation (gE=29 MHz). At this field, the flip-flop qubit is driven at a Rabi frequency of 1/tRabi=6 MHz.

The magnetic field and electric signal can be applied simultaneously to drive the state of the ‘flip-flop’ quantum bit.

Electric field noise during electric drive may affect the qubit states in the presence of electric field noise. If the noise is such to affect the qubit states, the qubits can be operated at bias points that render the qubit precession frequency highly robust against noise.

FIG. 5(a) shows a plot 50 with charge (∈0) and flip-flop (∈ff) qubits transition frequencies as a function of vertical electric field Ez. At the ionization point 56, the energy splitting of the charge qubit is minimum and equal to Vt (region 54 in FIG. 5(a)), therefore first-order insensitive to electric noise. Also around the ionization point, the flip-flop qubit energy depends strongly on Ez, through the combined effect of the hyperfine interaction A, and the orbital dependence of the electron gyromagnetic ratio, γe:

∈ff(A,γe)=√{square root over ([γe(Ez)+γn]2B02+[A(Ez)]2)},  (12)

shown in plot 50 (dashed line). The qubit transition frequency has an extra bend around the ionization point (full line in plot 50), when considering the dispersive coupling to the electron orbit. The resulting shift:

\(\begin{matrix}
{{D_{orb}\left( E_{z} \right)} = \frac{{{g_{so}\left( E_{z} \right)}}^{2}}{\delta_{so}\left( E_{z} \right)}} & (13)
\end{matrix}\)

reduces the flip-flop qubit frequency to:

∈ff(A,γe,Dorb)=∈ff(A,γe)−Dorb(Ez),  (14)

This dispersive shift is largest around the ionization point, since δso is lowest (i.e. the charge qubit frequency comes closest to the flip-flop qubit, see dotted line in plot 50) and gso is highest.

Most importantly, by tuning δso the flip-flop qubit frequency dependence on electric field can be tuned, up to level in which a plateau 52 is formed. Around this region the qubit precession frequency is highly insensitive to electric noise, a property similar to ‘clock transitions’ found in, for example, atomic clocks.

In some embodiments, all quantum operations can be operation points as close as possible to the plateau regions 52 and 54, in such a way that effects from electric noise is minimum.

In some embodiments, an oscillating magnetic signal can be applied to the processing element to transfer the quantum state associated with the pair of electron-nuclear spin eigenstates to a quantum state associated with the nuclear spin to implement a nuclear spin quantum bit.

By coupling the hyperfine interaction to the electron position, the nuclear spin can be driven using electrical means. As discussed above, this process also flips the electron spin. According to some embodiments of the method, the nuclear spin can be controlled independently from the electron spin so that the qubit for the processing element can be associated with the nuclear spin to implement a ‘nuclear-spin’ qubit. One of the main advantages of the nuclear-spin qubit is the longer coherence time.

The nuclear-spin qubit can be driven by electric fields after applying an oscillating magnetic field, with frequency close to the electron Zeeman frequency, to couple the spins states |↓> and |↑>.

Referring now to FIG. 6 there is shown a flow-diagram 60 with the basic steps used for operating the quantum processing element as a nuclear-spin qubit. At step 62 a continuous magnetic field is applied to the quantum processing element to separate spin states associated with an electron and a nucleus of the donor atom. At step 64 an oscillating magnetic field is applied to the processing element in a direction perpendicular to the continuous magnetic field. The magnetic field oscillates at a frequency close to a Zeeman frequency of the electron. At step 66 an electric field is induced in the region between the interface and the donor atom to modulate a hyperfine interaction between the electron and the nucleus and control the quantum state of the nuclear-spin qubit.

Referring now to FIG. 7 there is shown a simple schematic energy level diagram 70 of a nuclear-spin qubit driven using AC electric and magnetic fields. With the electron spin down, the nuclear spin transition frequency is

\(\begin{matrix}
{{ɛ_{ns}(A)} = {\frac{A\left( E_{z} \right)}{2} + \frac{\sqrt{\left( {\gamma_{+}B_{0}} \right)^{2} + \left\lbrack {A\left( E_{z} \right)} \right\rbrack^{2}} - {\gamma_{-}B_{0}}}{2}}} & (15)
\end{matrix}\)

Rather than using a simple AC magnetic field drive with frequency equal to ∈ns, the nuclear-spin qubit can be driven using a combination of AC electric and magnetic fields at much higher frequencies. The spatial representation 77 of such a drive is shown in FIG. 7(c). The magnetic drive Hamiltonian is:

ESR=Bac cos(2πνBt)(γeSx−γnIx)  (16)

The total Hamiltonian describing nuclear spin drive by AC electric and magnetic fields at microwave frequencies is:

drivenuc=B+Aorb+orb+E+ESR  (17)

With the nuclear spin down, the electron spin resonance (ESR) frequency is ∈ff−∈ns. In the drive process, excitation of the electron spin states is prevented by detuning the drives from the transition frequencies by an amount much larger than the coupling rates, i.e. δE−δso>>gEff (recall FIG. 4(c)) and δB>>gB. As before, electron orbital state is prevented if gso<<δso and gE<<δE where δB=∈ff−∈ns−νB. A more complete energy level diagram 75 is shown, for reference, in FIG. 7(b).

Under these conditions, the nuclear spin is coupled to the electric drive at a rate, to second order:

\(\begin{matrix}
{g_{E}^{ns} = {\frac{g_{B}g_{E}^{ff}}{2}\left( {\frac{1}{\delta_{B}} + \frac{1}{\delta_{E} - \delta_{so}}} \right)}} & (18)
\end{matrix}\)

Resonant Raman drive occurs when δB=δE−δso=δ (FIG. 7(a)). A schematic spatial visualization of such a Raman process is shown in FIG. 7(c). For example given earlier of a d=15 nm deep 31P donor, driven by Eac=32 V/m at a rate gEff=2.9 MHz, avoiding excitation of the electron spin requires δE−δso=29 MHz. Choosing gB=δB/10=2.9 MHz (Bac=0.4 mT), the nuclear spin is driven at a Rabi frequency of 2 gEns=0.6 MHz, with 1-qubit operations taking only 0.4 μs. This is two orders of magnitude faster than the typical Rabi frequencies obtained with standard (nuclear magnetic resonance) magnetic drive at radiofrequency.

Referring now to FIG. 8, there is shown a plot 80 of the nuclear spin qubit transition frequency as a function of the applied electric field, when subject to an AC magnetic drive, together with the corresponding energy level diagram 85. Without the AC drive, the bare nuclear spin transition frequency depends roughly linearly on A(Ez) (Eq. 15), which varies strongly with Ez around the ionization point (dashed line in plot 80 in FIG. 8(a)). However, the nuclear spin can also be made highly insensitive to electric noise around the ionization point. This is achieved by adding the AC magnetic field, close to the electron spin transition frequency. This magnetic drive AC-Stark shifts ∈ns by an amount dependent on Ez,

\(\begin{matrix}
{{{\epsilon_{ns}\left( {A,D_{{dri}\; {ve}}} \right)} = {{\epsilon_{ns}(A)} - {D_{drive}\left( E_{z} \right)}}},} & (22) \\
{{{D_{drive}\left( E_{z} \right)} = {\sum_{{i = 1},2,3}{\frac{\delta_{i}}{2}\left( {\sqrt{1 + \left( \frac{2g_{i}}{\delta_{i}} \right)^{2}} - 1} \right)}}},} & \left( {22a} \right) \\
{{g_{1} = {\alpha \; g_{B}}},{g_{2} = {\beta \; g_{B}}},{g_{3} = {g_{B}.}}} & \left( {22b} \right)
\end{matrix}\)

The level diagram 85 in FIG. 8(b) defines the detunings δ1, δ2 and δ3.

Most importantly, ∈ns(Ez) can be tuned in such a way that in the region 87, close to the ionization point 86, the qubit precession frequency is highly insensitive to electric field noise, again in a similar fashion to atomic clock transitions.

By displacing the electron wavefunction towards the interface, there is a concentration of positive charge at the donor location and negative charge at the interface. This electric dipole, with modulus ed, produces a vertical electric field on the horizontal plane around the donor.

The coupling of two donor spin qubits via dipole-dipole interaction is an important feature of the scalable quantum processor envisaged by the Applicants.

Referring now to FIG. 9 there is shown a flow-diagram 90 with the basic steps used to couple two flip-flop qubits by using this electric dipole. At step 92, a continuous magnetic field applied to the quantum processing elements to separate spin states associated with an electron and a nucleus of two donor atoms in two processing elements. At step 94, an electric signal is applied to each of the conductive electrodes of the two processing elements to displace the electrons and create two electric dipoles associated with the respective processing elements to enable coupling of the quantum states of the two quantum bits associated with the two processing elements.

FIG. 10(a) shows a schematic 100 structure with two electric dipoles 101 and 102 for respective processing elements. Schematic 100 also shows electric field lines generated by dipole 101. The dipoles are controlled using electrodes 103a and 103b respectively through dielectric layer 104.

Electrons on the verge of ionization are displaced according to this electric dipole field, which is equivalent to a coupling term between the orbital states of both donors.

The interaction energy between two distant dipoles, μ1 and μ2, oriented perpendicularly to their separation, r, is Vdip=μ1/μ2/(4π∈r∈0r3) where ∈0 is the vacuum permittivity and ∈r the material's dielectric constant (∈r=11.7 in silicon). The electric dipole of each donor-interface state is μi=edi(1+σz,i)/2, implying that the dipole-dipole interaction Hamiltonian is:

\(\begin{matrix}
{\mathcal{H}_{dip} = {g_{dd}\left( {{\sigma_{z,1}\sigma_{z,2}} + \sigma_{z,1} + \sigma_{z,2}} \right)}} & (23) \\
{g_{dd} = {\frac{1}{16\; \pi \; ɛ_{0}ɛ_{r}h}\frac{{ed}_{1}{ed}_{2}}{r^{3}}}} & (24)
\end{matrix}\)

Since the flip-flop spin qubit is coupled to the electron orbital position, a natural way of coupling two distant donor spins is via this dipole-dipole interaction.

The coupling technique exploits the electric dipole that naturally arises when a donor-electron wave-function is biased to the ionization point, due to the fact that a negative charge has been partly displaced away from the positive 31P nucleus. The electric field produced by this induced dipole can, in turn, introduce a coupling term in a nearby donor which is also biased at the ionization point.

This electric dipole-dipole interaction is therefore equivalent to a transverse coupling term between the charge qubits plus a small shift in the equilibrium orbital position of both electrons. Most importantly, since each flip-flop qubit is transversely coupled to their electron position the electric dipole-dipole interaction provides a natural way to couple two distant qubits.

FIG. 10(b) shows an energy level diagram 105 of two ‘flip-flop’ qubits coupling via electric dipole-dipole interaction. The flip-flop qubits are coupled while keeping the orbital levels in their ground state. The Hamiltonian of the system reads:

flip-dip=dip-dip+Σi=1,2Bi+Aorb,i+orbi  (25)

Fastest coupling rates are achieved if all levels are in resonance, ∈ff=∈o. If ∈o>>gdd>>gso, electron orbital excitation is minimized and the flip-flop qubits are coupled at a rate, to second order:

g2qff=(gso)2/gdd  (26)

For a pair of 31P donors with d1=d2=15 nm, gdd≈10 gso requires r=180 nm. At this distance, 4=3 MHz and therefore a √{square root over (iSWAP)} gate takes only 40 ns.

Electric field noise during dipole-dipole coupling may affect the qubit states in the presence of electric field noise. If the noise is such to affect the qubit states, the qubits can be operated at bias points that render the qubit precession frequency highly robust against noise.

Referring now to FIG. 11 there is shown a flow-diagram 110 with the basic steps used to couple two nuclear-spin qubits via electric dipole-dipole interaction. At step 112, a continuous magnetic field applied to the quantum processing elements to separate spin states associated with an electron and a nucleus of two donor atoms in the two processing elements. At step 114, an oscillating magnetic field is applied in a direction perpendicular to the continuous magnetic field. The field oscillates at a frequency close to a Zeeman frequency of the electron to each of the processing elements. At step 116, an electric signal is applied to each of the conductive electrodes to displace the electrons and create two electric dipoles associated with the respective processing elements and enable coupling of the quantum states of the two nuclear-spin qubits associated with the two processing elements.

FIG. 12 is an energy level diagram 120 of two nuclear-spin qubits coupling via electric dipole-dipole interaction.

The oscillating magnetic field with frequency close to the electron Zeeman frequency couples the spin states |↓> and |↓>. The Hamiltonian representing the system dynamics reads:

nuc-nuc=dip-dip+Σi=1,2orbi+Aorb,i+Bi+ESRi  (27)

The driving frequency νB can be selected to be in resonance with the ESR transition and the flip-flop transition to be in resonance with the tunnel coupling, ∈o=∈ff=νB+∈ns Under the condition gB<<g2qff, the electron spins and orbital states are minimally excited and the SWAP rate between distant nuclear spins is, to second order:

\(\begin{matrix}
{g_{2q}^{ns} = {\left( \frac{g_{B}}{g_{so}} \right)^{2}g_{dd}}} & (28)
\end{matrix}\)

For the two 31P donors at d1=d2=15 nm and z=180 nm apart, g2qff=3 MHz imposes the maximum AC magnetic field to be Bac=40 μT. This yields g2qns=0.3 MHz and therefore a nuclear spin √{square root over (iSWAP)} gate time of 4 μs.

Nuclear spin SWAP takes place without excitation of the electron spin, and therefore there is no obvious reason to prevent flip-flop to orbital transitions by imposing gdd>>gso. There is one particular regime, in which gso=gdd, where nuclear spin SWAP is faster and moreover electron orbital and spin excitation is still prevented if gB<<(gso)2/gdd. This sets r=385 nm and Bac=0.4 mT (gB=gso/10), then g2qns=0.3 MHz. This yields a nuclear spin √{square root over (iSWAP)} gate time of 0.4 μs. This is a remarkable advantage over previously proposed architectures for which √{square root over (iSWAP)} gates between two 31P nuclear spins r=15 nm apart takes 3 μs.

FIG. 13 shows a schematic view of a structure 130 for coupling qubits (132 and 134) via a photonic link 136 and the energy level diagram 131 for flip-flop qubit coupling to photons via off-resonant charge states.

In order to couple a spin-qubit to a flying photon, the latter has to be confined to a spatial region, inside of which the qubit is located, for a time long enough as for the interaction to happen. Even though 3D cavities have the longest photon lifetimes, coplanar waveguide resonators (CPWRs) confine the photons into smaller volumes, increasing the magnitude of the vacuum field.

Distant donors may be subject to the vacuum electric field Evac of a shared microwave resonator, by placing them at regions where such a field is high, as for example at electric field antinodes, close to the center-line of ground-plane edges.

A strong vacuum field, on the order of a few tens of V/m, can be obtained by using planar transmission-line superconducting resonators operating at ≈10 GHz, where the gap between the center-line and the ground planes is shrunk to ˜10−7 m in the area where the donors are located. The resonator can then be used as a quantum bus to couple two spin qubits separated by as far as 1 cm, as shown in FIG. 13(a). The distance is given by the mode wavelength.

FIG. 13(b) is an energy level diagram 130 of a ‘flip-flop’ qubit coupled to an electromagnetic field mode which is confined into a spatial region in proximity of the processing element. The electromagnetic field modes may be quantized to comprise one or more photons. In diagram 130 the flip-flop qubit is coupled to a single microwave photon. The interaction of the quantized electromagnetic field modes and the electron may be used to enable coupling of the one or more photons to the quantum state of the quantum bit.

Each resonator mode may contain a limitless number of photons. However, at low enough temperatures, kBT<<hνE (νE is the fundamental mode frequency), and without driving sources, the resonator is nearly in its ground state and contains no photons, having a vacuum energy of hνE/2. The resonator fundamental mode has then an energy that scales linearly with the number of photons according to the Hamiltonian:

ph=hνE(a†a+½),  (29)

where a† and a are the photon creation and annihilation operators, respectively. The vacuum energy is due to an oscillating vacuum voltage with amplitude Vvac=2νE√{square root over (hZ0)}, where Z0 is the line impedance. At νE=10 Ghz and Z0=50Ω, Vvac≈4 μV. Therefore, a donor placed under the resonator central line will experience a vertical electric vacuum field. The amplitude of such a field depends on the donor depth and the lateral dimensions of the waveguide, which can reach few tens of nanometers if fabricated using electron beam lithography. Vacuum fields of many tens of V/m are expected. Here we assume Evac=32 V/m, consistent with optimum values specified before.

This vacuum field displaces the electron wavefunction according to the orbital-photon coupling Hamiltonian:

\(\begin{matrix}
{{\mathcal{H}_{{orb}\text{-}{ph}} = \frac{{eE}_{vac}{d\left( {a^{\dagger} + a} \right)}\sigma_{z}}{4h}},} & (30)
\end{matrix}\)

Including electron and nuclear spins, the Hamiltonian describing the donor-resonator coupled system, in the absence of drive, reads:

flip-ph=B+Aorb+orborb-ph+ph  (31)

Excitation of the electron orbital state is prevented if δso>>gso and δE>>δE, for which an effective flip-flop-photon coupling via virtual orbital excitation is achieved at a rate, to second order:

\(\begin{matrix}
{g_{{flip}\text{-}{ph}} = {\frac{g_{so}g_{E}}{2}\left( {\frac{1}{\delta_{E}} + \frac{1}{\delta_{so}}} \right)}} & (32)
\end{matrix}\)

Following the same arguments discussed above, detunings of δE≈δso≈290 MHz yield a flip-flop-photon coupling rate of gflip-ph≈3 MHz, for a 31P donor d=15 nm deep. This is three orders of magnitude faster than the electron-spin coupling rate to a resonator via its magnetic vacuum field. The obtained rate is comparable to the coupling strength obtained by using strong magnetic field gradients but without the need to integrate magnetic materials within a superconducting circuit.

Coupling spin qubits to single microwave photons provides a natural way to transfer quantum information over long distances.

To avoid losses from photon decay, the qubits should be detuned from the resonator by an amount much greater than the qubit-photon coupling rates.

This means δEff>gflip-ph), where δEff=νE−∈ff=δso−δE. Two qubits are then coupled via a second-order process at a rate:

g2qff=(gflip-ph)2/δEff  (33)

For the previous 31P donor example, assuming δEff=10 gflip-ph yields an effective 2-qubit coupling g2qff≈0.3 MHz, with a √{square root over (iSWAP)} gate that taking only 0.4 μs. This is an outstanding result considering that the separation of the qubits can potentially reach several millimeters.

Moreover, in the dispersive regime (δso−δE>>gflip-ph), qubits can be non-destructively read-out via the resonator.

The resonance frequency of the CPW is slightly shifted by an amount that depends on the spin state,

\(\left. v_{E}\rightarrow{v_{E} \pm {\frac{\left( g_{{flip}\text{-}{ph}} \right)^{2}}{\delta_{so} - \delta_{E}}.}} \right.\)

This shift reaches 250 kHz for the flip-flop qubit, and can be easily detected for resonator Q-factors on the order of 103.

FIG. 14 is an energy level diagram 140 of a nuclear-spin qubit coupled to a photon in a resonator through the addition of an AC magnetic drive.

The coupling between a flip-flop qubit to a single microwave photon provides a way of coupling the latter to single nuclear spins, by adding an ESR field under conditions that prevent electron spin excitation. This is represented by the nuclear spin-photon coupling Hamiltonian:

nuc-ph=BAorb+orb+orb-ph+ph+ESR  (34)

The electron spin state could be minimally excited if gB<<δB, for the ESR transition, and gflip-ph<<δE−δso for the flip-flop transition. Excitation of the electron orbital state is prevented if gso<<δso and gE<<δE. Under these conditions, effective nuclear spin-photon coupling via virtual electron spin and orbital excitation occurs at a rate, to second order:

\(\begin{matrix}
{g_{{nuc}\text{-}{ph}} = {\frac{g_{B}g_{E}^{ff}}{2}\left( {\frac{1}{\delta_{B}} + \frac{1}{\delta_{E} - \delta_{so}}} \right)}} & (35)
\end{matrix}\)

For d=15 nm, Eac=32 V/m, Bac=400 μT) a gnuc-ph=0.3 MHz is obtained. This allows for √{square root over (iSWAP)} operations between distant 31P nuclei to be performed within only 4 μs.

In some embodiments, read-out can be performed in the flip-flop qubits subspace, without the addition of an AC magnetic field (note that the nuclear qubit state |↓> shift the resonator frequency mode by 250 kHz whereas the state |↓> does not produce any shift).

Referring now to FIG. 15 there is shown a flow-diagram 150 with the basic steps used to couple two flip-flop qubits via intermediate coupling with a microwave resonator quantized electromagnetic field mode. At step 152, a continuous magnetic field is applied to the quantum processing elements to separate spin states associated with an electron and a nucleus of the donor atoms. At step 154, electromagnetic field modes are confined into a spatial region in proximity of the processing elements in a manner such that a quantized electric field is induced in the region between the interface and the donor atom to modulate a hyperfine interaction between the electron and the nucleus of each processing element and couple the quantum state of the two flip-flop quantum bits.

Referring now to FIG. 16 there is shown a flow-diagram 160 with the basic steps used to couple two nuclear-spin qubits via intermediate coupling with a microwave resonator quantized electromagnetic field mode. At step 162, a continuous magnetic field is applied to the quantum processing elements to separate spin states associated with an electron and a nucleus of the donor atoms. At step 164, an oscillating magnetic field in a direction perpendicular to the magnetic field. The field oscillates at a frequency close to a Zeeman frequency of the electron is applied to each of the processing elements. At step 166, electromagnetic field modes are confined into a spatial region in proximity of the processing elements in a manner such that a quantized electric field is induced in the region between the interface and the donor atom to modulate a hyperfine interaction between the electron and the nucleus of each processing element and couple the quantum state of the two nuclear-spin qubits.

FIG. 17(a) shows a schematic representation 170 of two qubit gates between the nuclear spins 172 and 174. Arrow 176 can represent either the direct dipole-dipole or the photonic links. FIG. 17(b) shows level diagrams 175 for distant two-qubit (charge, 177, flip-flop, 173, or nuclear-spin, 171) coupling via virtual photons 170.

The nuclear spin is coupled to photons through the electric and magnetic dipole moments of the electron, and it precesses at GHz frequencies in the AC magnetic drive rotating frame, ∈ns+νB. The shared quantum electric field Evac is sufficient to provide long-distance coupling between nuclear spins, even though Bac is a classical drive. Photon creation is suppressed if δEns>>gEns, where δEns=νE−(∈E+νB) is the qubit detuning from the resonator, in the magnetic drive rotating frame.

Table 2 shows the qubit gate time for specified power, figures of merit for each distant coupling scheme, and expected qubit dephasing rates due to electric field fluctuations with rms amplitude Enoisez,rms=30 V/m. The optimal inter-qubit distance using dipole-dipole link is slightly larger when effects from image charges at the interface are considered.

FIG. 18(a) shows a schematic top view 180 of a possible implementation of a quantum computer consisting of a 2D array of single qubits, with a 200 nm pitch. FIGS. 18(b) and 18(c) show lateral cuts 181 and 182 corresponding to dashed lines in 180. This processor may be fabricated using standard CMOS industrial techniques. Structure 181 may constitute a single electron transistor. The substrate (183a, 183b) can be an isotopically purified 28Si crystal, with a thin oxide layer (189a, 189b) on top. Substrate regions 184a and 184b may be highly doped with donors to form an electron reservoir. Metallic contacts 186a and 186b may set the Fermi energy level of those reservoirs. Applying a highly positive voltage to gates 187a, 187b and 188 generates an electron gas at the interface underneath, which contacts both reservoir regions, in a process analogous to a MOSFET turn on. Lowering the voltage on gates 187a and 187b, which are disconnected from gate 188 by the dielectric barriers 185a and 185b, depletes the electron gas under those gates, creating henceforth two tunnel barriers. Conduction then happens via single electrons, in which case structure 181 may constitute a single electron transistor (SET).

Donors are placed, using for example ion implantation, under the metallic gates 188b. Each of those gates can be on top of one or a few donors. Gates 188b control the electron wavefunction, which can be displaced between donor and interface as described before. Single qubit operations may be performed by applying AC voltages to gates 188b. Two qubit operations are done via electric dipole-dipole coupling between nearby qubits, each of them belonging to different qubit units.

Uncertainties in vertical misplacement of each donor translate into uncertainties in the dipole moment ed and tunnel coupling Vt, whereas lateral placement uncertainties changes the electric dipole-dipole coupling gdd between neighboring qubits. The optimum conditions for two qubit coupling are not substantially modified if gdd is altered by an order of magnitude. This translates into a tolerance in donor placement of ˜8 nm vertically and many tens of nm laterally, below which the computer performance is not substantially affected. These limits are compatible with the uncertainty in donor placement achieved with ion implantation techniques.

The single donor qubit may be realised using counted ion implantation. In this case, individual extra gates 186c and 186d may be present at each qubit unit in order to tune the tunnel coupling to the interface. This is shown in detail in FIG. 19, where panels 192, 194 and 196 show electron wavefunction, shared between donor and interface, inside dashed rectangle in structure 182, for three different voltage combinations applied to gates 186c and 186d of FIG. 18(c). The interface state can be displaced laterally by many tens of nanometers, reducing the overlap between donor and interface wavefunctions, therefore reducing Vt by a few orders of magnitude. Another possibility to increase Vt is to keep an extra even number of electrons at the interface. In this way, the donor electron has a wider wavefunction extension when at the interface, which increases its tunnel coupling to the donor. Also, multiple donors can be implanted per processing element, in which case the most convenient the donor can be individually chosen.

Quantum processing may involve a great sequence of steps. While qubits are not being operated, the information can be ‘stored’ in the nuclear spin, which may be ionized by using top gates. Ionized nuclear spins are the most coherent of the available qubits used here, and among the most coherent of any quantum system. Loading an electron into the donor-interface system, therefore making it active to quantum operations, may be done by inducing an electron gas under gate 188, and then moving this gas closer to the qubit by changing the voltage on neighbouring gates 186c and/or 186d. In order to better electrically isolate qubits or pairs of qubits when performing operations, an electron gas can circumvent qubits or pairs of qubits and therefore screen is electric interaction with neighbouring stray qubits. Read-out of the qubit spin states may be performed by spin-dependent tunnelling to a reservoir, and detecting such a tunnelling event via a nearby SET.

If the nuclear spin is the one used for operations, the operation of the qubit (for 1- and 2-qubit gates) can be achieved by adiabatically pulling the electron wavefunction to the intermediate state between donor and interface using biasing conductive electrodes 188b.

If, instead, the flip-flop qubit is to be used for operations, the electron has to be pulled to the intermediate orbital position, and then an ESR it-pulse is applied at a frequency ∈ff−∈ns, which maps the nuclear spin state α|↓>+β|↓> into the flip-flop state α|↓>+β|↑>.

Referring now to FIG. 20, there is shown a schematic representation of an embodiment of quantum processor 200 comprising a plurality of qubits realised and coupled in accordance with the methods described above.

Quantum processor 200 comprises several qubit cells 205 coupled using a CPW resonators 207. Each cell may consist of a bilinear array containing a few qubits. The exploded view 205 of a qubit cell shows the internal architecture of the cell. A bottom view 201 of the cell, that does not show the substrate or interfacing oxide for clarity, shows the donor atoms 202 and a schematic representation of the respective electron wave functions. View 201 also shows all metallic gates that form single electron transistors 204, top-gate electrodes 206, confinement and tunnel coupling gates 208, electron reservoir 209 and CPW resonator 203. In this quantum processor, 2-qubit gates are performed within a cell via electric dipole-dipole interactions, where two qubit belonging to the extremities of different cells can be coupled via a common microwave resonator.

The methods and the quantum processor architectures described herein uses quantum mechanics to perform computation. The processors, for example, may be used for a range of applications and provide enhanced computation performance, these applications include: encryption and decryption of information, advanced chemistry simulation, optimization, machine learning, pattern recognition, anomaly detection, financial analysis and validation amongst others.

The term “comprising” (and its grammatical variations) as used herein are used in the inclusive sense of “having” or “including” and not in the sense of “consisting only of”.

It will be appreciated by persons skilled in the art that numerous variations and/or modifications may be made to the invention as shown in the specific embodiments without departing from the spirit or scope of the invention as broadly described. The present embodiments are, therefore, to be considered in all respects as illustrative and not restrictive.

