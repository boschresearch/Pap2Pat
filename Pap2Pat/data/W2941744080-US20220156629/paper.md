# Introduction

Universal quantum computers promise speed-up in crucial areas like simulation of materials and molecules [1], search [2,3] and sampling [4,5], yet they all require high-precision control of quantum states. Quantum error correction codes allow us to trade qubit number for precision in controlling quantum states (mitigating both control errors and natural decoherence), with the surface code being particularly attractive due to its 2D structure, local checking operations and high error threshold close to 1% [6]. Surface code architectures have been proposed for leading quantum information processing platforms including superconducting qubits [7], trapped ions [8] and semiconductor spin qubits [9,10]. However, the qubit overheads can be significant: it is estimated that > 2 × 10 8 physical qubits with gate error rate 10 -3 might be needed to perform a non-trivial Shor's factoring algorithm using surface codes [11]. These considerations motivate the development of qubit implementations which offer the prospect for high-density 2D arrays. The high-qubit density offered by silicon-based spin (SS) qubits (as high as 10 9 cm -2 ) combined with the possibility of leveraging the con-ventional semiconductor integrated circuit industry [12] make this platform attractive for faulttolerant universal quantum computing. Like all qubit hardware approaches, scaling up SS qubits brings a number of practical requirements associated with qubit addressing for calibration, tuning, operation and readout. Indeed, the high qubit densities offered by SS qubits leads to challenges in routing classical control lines, while minimising cross-talk and managing heat dissipation [12]. A number of architectures for scaling up SS qubit arrays have been proposed to address such challenges: for example, Veldhorst et al. [13] proposed a compact quantum dot array controlled via a crossbar geometry, enabling N qubits to be controlled with √ N classical control lines, albeit using control transistors below the dimensions of current technology [12]. Li et al. [14] went further with a half-filled crossbar architecture that provides more space for classical control lines, though the use of shared control lines brings tight requirements for qubit homogeneity and limitations on the parallelisability of operations. Buonacorsi et al. [15] have suggested connecting many small quantum dot modules using electron shuttling in order to provide the space for individual control lines. Smaller quantum dot modules are also easier to calibrate and the operations within the modules may be expected to have higher fidelities. However, such shuttling architectures require distribution of entanglement between modules and this is likely to impact the fidelity and speed of inter-module operations.

While such influential architectures have been designed to accommodate error correcting codes that compensate for computational errors, they do not address so-called 'leakage errors' in which the quantum system escapes out of the computational subspace. For SS qubits, one form of leakage errors arises from the migration of charge: Controlling SS qubits involves tuning tunnelling barriers, changing on-site energies and/or shuttling electrons, and each of these operations may lead to electrons escaping out of the quantum dots. Since leakage errors of this kind cannot be corrected (and may even be exacerbated) by the usual quantum error correction protocols, they will accumulate and eventually corrupt the surface code even if the probability of these leakage errors is very small. Furthermore, unlike most of the other types of leakage errors [16][17][18][19][20][21] which occur as independent events, a leaked charge from one dot might propagate through the quantum dot surface code array and corrupt other dots. Charge leakage errors thus could be very damaging to the surface code due to the correlations in errors.

In this Article, we introduce a surface code architecture based on SS qubits that is designed to be robust against leakage errors. We first introduce the components of our hardware in Section 2, and then discuss leakage errors in our architecture in Section 3. Then, in Section 4, we describe how surface code stabiliser checks are performed, and obtain a threshold for the gate errors and leakage errors. Finally, we summarise the key features of this approach and discuss possible improvements and extensions.

# Physical Implementation

The physical layout of the silicon quantum dot surface code architecture we consider is shown in Figure 1. We have included elongated mediator dots [22] to provide the basic two-qubit gate operation while increasing the fundamental interqubit spacing to more readily accommodate measuring devices for ancilla readout, and electron reservoirs for initialisation and reset of quantum dots. Quantum information resides in the data dots, whose error information is extracted by the ancilla double-dots via interactions through the mediator dots.

## Data Qubits and Single-qubit Gates

Each data qubit is represented by the spin state of an electron within an electrostatically-defined quantum dot [23]. The lifting of the spin degeneracy via an applied magnetic field gives access to electron-spin resonance (ESR) [24][25][26] or electrically-driven spin resonance (EDSR) [27,28] techniques, which have been used to produce control fidelities of electron spin qubits in silicon of up to 99.6-99.9% [24,28]. As has been considered in several proposals [13,14,29,30], driving fields can be applied globally to all, or many, qubits [31,32] in order to avoid the problem of 'frequency crowding' [33,34]  Figure 1: Overall architecture layout, including (a) the arrangement of the key physical components of the system and (b) its correspondence to the components of the surface code. An X-stabiliser plaquette is highlighted in (a), which can be divided into two parts each interacting with one half of the double quantum dot ancilla in the centre.

can reach > 1 s [35][36][37] and using isotopically enriched 28 Si substrates [38], qubit coherence times can be extended up to the limits of the fluctuation timescales within the magnetic environment (e.g. T * 2 ∼120 µs [24]). Decoupling schemes can then be used to yield longer qubit operation times (T 2 ∼ 28 ms [39]), and these can be integrated into algorithms [30,40] or single qubit gates designed via gradient ascent pulsed engineering [41] to be inherently robust against environmental noise [26].

Qubits formed electrostatically in highly strained silicon also have the advantages of splitting off the excited states when quantum dots are strongly confined. Such systems often show valley excited states of ∼ 0.1 THz [24,35,42], and orbital energies of ∼ 1 THz [42], and such excited state energies can be electrostatically tuned via the Stark shift [35,39]. In a confined quantum dot with diameter, say 30 nm, a large Coulomb repulsion U ∼ 2 THz [42] is produced -this effectively prevents additional charges entering such dots during the execution of the code, leaving us to address the possibility of charge leakage out of the dot.

## Ancilla Qubits and Read-out

Our proposed ancilla qubit is represented by the spin state of a pair of electrons distributed across two quantum dots (each similar in size to the data dots). By initialising in a singlet state, a failed stabiliser check of its neighbouring data qubits transforms the ancilla spins into a triplet state [30], such that we can use Pauli spin blockade (PSB) and its effect on interdot tunnelling [43,44], to determine the outcome of the stabiliser cycle. PSB can be detected in singleshot through charge sensing [45], or via gatebased dispersive readout [46][47][48] as suggested by the measurement devices in Figure 1 [45,49]. The ancilla qubits are initialised via the (0,2) electron occupation state of the double quantum dot (or an equivalent (N , N +2) state), where the ground state is a singlet and can be rapidly prepared through 'hot-spot' relaxation near the (1,1):(0,2) charge transition [50].

Previous schemes [13,30] have employed a second quantum dot as part of the ancilla structure as a reference state which does not participate in the stabiliser check -the primary function being to enable measurement by PSB. In con-trast, in our proposal we treat both ancilla dots on an equal footing, allowing both dots in the ancilla pair to interact with data qubits. In addition to reducing complexity in connectivity, this approach enables interactions between the data qubits and ancillae to be performed in parallel using both of the ancilla dots, halving the time needed to perform a stabiliser cycle.

Operations that are symmetric under the exchange of the two spins cannot bring the quantum state out of the singlet (exchange-antisymmetric) or the triplet (exchange-symmetric) subspace. Hence, global ESR (single qubit gates) can be applied to all the data qubits without affecting the double-dot ancilla, which is useful when switching between X and Z stabiliser check cycles of the surface code.

The type of error (e.g. X or Z) detected by single-dot ancillae depends on the basis in which they are prepared and measured, while two-dot ancillae prepared in the singlet state can be used to detect both X and Z errors [30]. In standard parity check circuits, the X and Z errors in the data qubits will be transformed into Z errors in the ancilla qubits using CZ and CNOT respectively, which can be detected by preparing and measuring the ancilla in the X-basis. In the case of double-dot ancilla, this can be achieved by mapping the singlet state and the zero-spin triplet state of the two-dot ancillae to the X-basis eigenstates:

On the L.H.S. we have the state of the two physical spins within the ancilla double-dot and on the R.H.S. we have the corresponding state of the ancilla qubit.

From the mapping we can see that while Z gates on individual physical spin correspond to Z gates on the ancilla qubit, X and Y gates on the individual physical spin will take the spin pairs out of the zero-spin subspace, resulting in leakage errors on the ancilla qubit. The effect of such leakage errors will be detailed in Section 3.

## Mediators and Two-qubit Gates

When two-qubit gates are performed using direct exchange interactions between nearest-neighbour quantum dots, the resulting qubit pitch is typically on the scale of tens of nanometres. On the

Figure 2: Core two-qubit gate between data and ancilla qubits, achieved via a mediator. Three quantum dots with orbital L/R in the left/right dot, each of which is either a data dot or one half of an ancilla structure, and orbitals 1 and 2 in the middle mediator dot. We consider a total of four electrons in this three-dot system and assume the charging energy of the side dots is sufficiently large (due to their small size) to forbid further occupancy. Electrons may be excited to the mediator state 2 from any of L,R or 1 orbitals, with some energy cost indicated.

other hand, control and read-out electronics associated with each qubit are more comfortably accommodated with larger spacings at the level of at least several hundreds of nanometres. To extend the range of the exchange interaction, an elongated quantum dot can be used as a 'mediator' [51,52]. Our architecture employs effective two-electron (i.e. even-occupation) quantum dots as mediators for the exchange interaction between a data dot and one half of the ancilla double-dot as shown in Figure 2. For simplicity we assume two-electron occupation in the mediator, but in practice four-electron or other values may be preferable, for example to mitigate a small valley-orbit splitting [53].

The mediators do not themselves carry any quantum information and our computational subspace only consists of the spin states of the electrons in the two side dots. Ruderman-Kittel-Kasuya-Yosida (RKKY) exchange interactions communicated by the mediators occur between the spins in the two side dots, with a strength [51] given by:

where t ab is the tunnelling energy from orbital a to b and ∆ R,M,L are the energies associated with various electron hopping processes starting from the ground state as indicated in Figure 2. We consider mediator dots of dimensions 30 nm × 300 nm, which leads to ∆ M ∼ 10 GHz, and assume a tunnelling energy between the mediators and data/ancilla dots of t ∼ 1 GHz (corresponding to an interdot spacing of ∼ 10 nm). By tuning the on-site energy of the mediator dot, we can change the value of ∆ R/L and hence control the strength of the exchange interaction. ∆ R/L is bounded to be at least the tunnelling energy and at most the Coulomb repulsion energy in the data dots. Hence, we use ∆ R/L = ∆ on = 10 GHz to turn on the exchange interaction, and ∆ R/L = ∆ off = 1 THz to turn off the exchange interaction. Using (1), the strength of the exchange interaction is J on = t 4 ∆ 2 on ∆ M = 1 MHz when on, and has a residual value

= 100 Hz when nominally off. This level of residual exchange interaction leads to an expected error probability ( J off Jon ≈ 10 -4 ) well below the threshold of the surface codes and hence ignored in our discussion. We assume the mediated exchange is controlled through the detuning of the mediator dot under the fixed tunnel coupling naturally formed between adjacent dots [39] -it is also possible to use additional electrodes for controlling the tunnel coupling between adjacent dots [54], albeit at the cost of greater gate complexity.

A difference in g-factors or in z-magnetic field in the left and right (L/R) dots produces a difference in the Zeeman splitting between them, which we denote Ω. When the device is tuned to satisfy Ω J, the exchange interaction enables us to implement √ SWAP gates (see Appendix A for details). Along with single-qubit Z rotations, they can be used to create CZ gates as proposed by Loss and DiVincenzo [55]:

On the other hand, in the limit where Ω J, we can achieve a dipole-dipole like interaction between the two dots mediated by the exchange interaction, which can be used to implement S =

Along with single-qubit Z rotations, they can be used to create CZ gates as proposed by Meunier et al. [56]:

Two-qubit gates in silicon QDs based on direct exchange have been demonstrated [39,57], whose fidelity has been improved to 98% [58], fast approaching the fault-tolerant threshold. Mediated exchange using empty [59] or multi-electron [22] mediator dots has also been demonstrated in GaAs quantum dots. In our architecture, we use an effective two-electron mediator dot to provide exchange interactions that can be more readily to switched on and off than with empty mediator dots due to a lower virtual energy cost, noting also that keeping the occupancy low leads to higher expected fidelity than the multi-electron mediators due to the simpler electron environment in the mediators [51].

## Realisations of the Ω J and Ω J regimes

As explained above, the RKKY exchange operation produced by the mediator dot can be utilised to construct the CZ operation either directly via the S gate when Ω J, or indirectly via √ SWAP operations when in the Ω J regime. Embedding our device within a uniformly applied external magnetic field enables single qubit operations via ESR [24], while also accessing the Ω J regime through the natural variation in electron g-factor inherent to the qubit platform [39,60].

However, single-qubit gates achieved by ESR have relatively slow speed (∼ 1 MHz), limited by the magnitude of the oscillating magnetic field. An alternative method to implement single-qubit gates is EDSR [61], which can be achieved in a uniform magnetic field [62] by exploiting the spinorbit coupling in silicon [63,64]. More commonly, EDSR is achieved using a magnetic field gradient created at the quantum dot, usually by placing a micromagnet in proximity. In this way, when the electron is perturbed via an oscillating electric field, it experiences an effective oscillating magnetic field which drives the spin rotation. EDSR can be more than an order of magnitude faster (> 10 MHz [28]) than ESR, however, qubits capable of EDSR driving can be more susceptible to decoherence from charge noise of the control gates. A balance can be struck between the speed of the single-qubit gates and qubit decoherence to achieve single-qubit EDSR gates with fidelity of 99.9% [28].

As shown in Section 2.2 and further discussed in Section 4.1, we do not need to apply singlequbit gates to our ancillae, and so there is no advantage in furnishing them with micromagnets. This fact, together with the additional spacing between qubits afforded by the mediator dots, facilitates the ability to deposit a micromagnet array such that each data qubit is located in the vicinity of a magnetic field gradient. This local field gradient observed by the data qubits facilitates EDSR, and also produces the offset field between data and ancilla qubits attaining the Ω J regime. A second regime in which the qubit array can be operated is the Ω J regime. In order to achieve this regime, no field gradients due to micromagnets are utilised and the external magnetic field must be low, such that Ω attributed to the variation in the electron g-factor is minimal. Given current disorder levels within Si QDs, the use of an applied field of ∼30 mT (enabling ESR at ∼1 GHz) would yield in Ω ∼ J. To push into the Ω J regime, the platform could be further engineered for larger J values, or for the reduction in disorder levels giving rise to variation of electron g-factors such that they can be mitigated effectively using the Stark shift.

## Charge Reservoirs and Initialisation

Charge reservoirs remain an integral component of modern test-bench quantum devices as they are used to supply electrons to quantum dots, facilitate traditional spin-to-charge readout [65] or more recent improved methods [66,67], as well as providing a relaxation path for rapid spin initialisation [50]. However, modern concepts of scaled qubit platforms that exploit CMOS technology typically envisage larger devices with denselypacked quantum dots, leading to reservoirs being pushed to the borders of large 1D [30] or 2D [13] arrays. Other architectures have the capacity for reservoirs to be located in specialised modules where spins could then be shuttled into arrays through the use of long-distance highways [14]. With the relative absence of reservoirs in many modern architectures, spin initialisation and readout relies predominantly on Pauli spin blockade methods, with some schemes also utilising thermal relaxation as an initialisation method [12].

In the architecture presented here, we strive to maintain the advantages of having integrated spin reservoirs, without compromising the advantages of CMOS as a platform capable of realising arrays of densely-packed qubits. This is achieved through the spatial separation afforded by the larger scale mediator dot between each data/ancilla dot as seen in Figure 1. With a gate pitch of 30-40 nm [24,35] in recent 2D planar SiMOS QD designs, and with the possibility of reducing this through the use of smaller length scales (e.g. more recent CMOS technology nodes), the indicated 300 nm separation due to the mediator generates enough space for the integration of the reservoirs as well as the planar fan-out of metallic gate structures required to define/confine the 2D quantum dot structures. Specifically, this facilitates the ability to maintain gated connections between the reservoir and the mediator dot, meaning the tunnel rate can be tuned or made switchable for either rapid interaction as required during initial population of a qubit array, or appropriately tuned for slow reset of mediator dots during periods of inactivity.

The smallest energy scale for the mediator system is ∆ M ∼ 10 GHz, which remains ∼ 5× larger than conservative electron temperatures of ∼ 100 mK. Couplings required for Elzerman readout [65] are ∼ 100 µs in typical CMOS systems [24], which is long compared to the CZ execution time, however dispersive sensing has seen device operation with tunnel couplings on the order of tank circuit frequencies of 1-10 MHz, which would place the mediator reset, or initialisation protocols within an appreciable time budget with respect to the error correction scheme. This is made possible because this scheme does not utilise the reservoir for coherent operations such as readout, and hence the tunnel rate can be made larger than timescales required for high fidelity single-shot detection via classical electronics.

3 Leakage errors

## Background

A leakage error, in which the state of the quantum system escapes out of the computational subspace, is not corrected by typical quantum error correction protocols. If left uncorrected, even low-probability leakage errors may accumulate and eventually corrupt the logical qubits. Wood and Gambetta have presented an recent overview on leakage error models and how they can be quantified [68]. To correct leakage errors, we need to first reduce them to errors that fall within the computational space, which can then be handled by the quantum error correction scheme. This can be achieved by detecting the leakage errors [69,70] and replacing the leaked qubits with fresh qubits, or employing leakage reduction protocols [71][72][73] to all qubits without the need of leakage detection. In practice, the sources of, effects of, and solutions to leakage errors are strongly hardware-dependent.

In our architecture, we use the term qubit dots to refer both to data dots and ancilla dots in which quantum information resides. Within our computational subspace, all qubit dots will be in the ground charge configuration. The electrons in the data single-dots are allowed to have any spin configurations while the electron pairs in the ancilla double-dots are restricted to the spin-zero subspace. The wrong spin or charge configuration of the system will leads to spin leakage or charge leakage errors respectively.

## Robustness Against Spin Leakage Errors

Spin leakage error means the spin configuration of the system go out of the spin subspace that defines the computational subspace, given the right charge configuration. There is no spin leakage for the data qubits in our case since all of their spin configurations are within the computational subspace. Hence, the only spin leakage in our architecture will be the ancilla qubits escaping out of the spin-zero subspace. Ancilla spin leakage cannot spread to the data qubits via interactions (since there is no data spin leakage), which means that spin leakage cannot propagate in our architecture. Furthermore, the spin leakage errors of the ancilla qubits will be removed in every new round of stabiliser checks when we reinitialise the ancilla. These properties ensure spin leakage will not lead to spatially or temporally correlated errors in our architecture, permitting robustness against spin leakage. Now if we take a look at the stabiliser check circuit in Figure 3, we can see that before the readout, the stabiliser check process can be viewed as two non-interacting halves. Within each half, there will be two data qubits interacting with one spin within the ancilla spin pair in the same way as interacting with a single-spin ancilla qubit. Hence, before the readout, we can study all the errors on an ancilla qubit simply by treating each spin within the ancilla spin pair as an individual qubit. The spin leakage errors of the ancilla qubits can be taken into account in this way because they can be represented by unitaries applied on the ancilla spin-pair, e.g. X and Y gates on individual spins are two possible forms of ancilla spin leakage errors as mentioned in Section 2.2. Hence, we can see that the effect of spin leakage errors on our double-dot ancillae should be similar to the effect of computational errors in some alternative schemes using two single-dot ancillae.

In the readout stage, we need to consider the errors on both spins together. The double-dot ancilla singlet-triplet readout may fail when there are non-symmetric errors occurring on the two spins, compared to the single-dot ancilla X-basis readout which will fail under any non-X errors.

## Robustness Against Charge Leakage Errors

Charge leakage error means the charge configuration of the qubit dots moves away from the ground charge configuration that our computational subspace resides in. In our architecture, the electron-electron repulsion energies in the qubit dots are much higher than any other energy in our system, thus we do not consider the charge leakage errors due to extra electrons entering the qubit dots. Instead, we will focus on the charge leakage errors due to electrons escaping out of the qubit dots. Possible sources of such charge leakage errors include decoherence of charge eigenstates during exchange interactions [74] (see also Appendix F) or electrons escaping out of the 2D electron gas confinement.

Charge leakage is much more damaging than spin leakage in two ways. First of all, charge leakage can be transferred from one qubit to another via gate operations, which will lead to propagation of leakage errors in the qubit array. Secondly, it cannot be simply removed by reinitialisation of the spin configuration. The missing charge must be replenished using charge reservoirs, which can be hard to integrate into a densely-packed quantum dot arrays.

When an electron escapes from a qubit dot in our architecture, it can be restored via relaxation of electrons in the neighbouring mediator dots into the empty qubit dot. The time scale of such relaxation is indicated by the T 1 time of charge qubits in semiconductor quantum dots. Wang et al. [75] measured the charge relaxation time in Si/SiGe double quantum dots, showing strong dependence on the tunnelling energy between the orbitals and weak dependence on the detuning between the orbitals. For the tunnelling energy regime that we are interested in (t ∼1 GHz), the relaxation time was around 10 ns, which is much shorter than the other time scales in our systems (all the gates in our system operate at µs time scale). Hence, we can assume that once a charge leakage error occurs, a relaxation process quickly takes place, in which an electron in one of the adjacent mediator dots hops down to fill the empty qubit dot, restoring the charge configuration of the qubit dots. Therefore, even without any active leakage error detection and correction or applications of any leakage reduction protocols, our architecture has a useful inherent behaviour whereby charge deficit transfers from qubit dots to mediator dots.

The relaxation process that restores the charges in the qubit dots can, however, result in missing/extra charges in the mediator dots, which, uncorrected, would produce faulty exchange gates. This can be corrected by connecting all the mediators to the charge reservoirs that are used for the initial population of the quantum dot array. Since the mediators do not carry any quantum information, such connection to reservoirs should not introduce qubit errors.

Errors due to unwanted coupling between the charge reservoirs and the qubit array are minimised by decreasing the tunnelling energy between the reservoir and the mediators, though this produces a longer reset time for the mediators. As we will see in Section 4, our surface code is partitioned into regions which are active/inactive at different times during a full cycle. This provides an opportunity for a given mediator to reset with its nearby reservoir during an idle period, without adding delay to the error correction processes. The tunnel coupling between mediator and reservoir can be minimised to the level required to give a reliable state reset within the execution time of half of a stabiliser check, and thus minimise any charge noise injection into the mediator and rest of the circuit.

Without the use of mediators, leakage errors apply directly to the qubit dots and require leakage correction schemes to be applied. As discussed in Appendix D, such schemes would introduce large qubit/runtime overheads [71,73], limits on the choice of data/ancilla qubits [72] and/or require extra components for charge detection or reset introduced within a potentially dense qubit array. In contrast, in the architecture we propose here the leakage errors are addressed by the inherent charge deficit transfer from the qubits to the mediators and resetting the mediators using charge reservoirs. No additional components are needed since the reservoirs are also used for qubit initialisation and no additional runtime is introduced since the mediator resets can be carried out in parallel with other error checking cycles in the surface code.

# Surface code simulation 4.1 Surface Code Threshold and Stabiliser Check Circuit

For many quantum error correction codes, there exists a threshold such that if the error rate of the physical circuit components falls within this threshold, then the logical error rate can be indefinitely reduced by scaling up the code size. Such an error threshold is highly dependent on the precise implementations of the quantum error correction circuits and the errors associated with their component parts. By transforming all the noise channels into Pauli channels via twirling [76], we can efficiently simulate quantum error correction circuits using classical computers exploiting the Gottesman-Knill theorem [77,78] to obtain a reliable threshold for a given quantum error correction code [79][80][81]. The threshold sets a target error rate for the experimentalist to aim for in order to implement a given quantum error correction code, though operation well below the threshold is required for useful quantum computing to be performed.

The surface code is implemented by checking the X/Z parities of the data qubits spanned by each plaquette in Figure 1. These parities are the stabiliser generators of the surface code and are measured using the stabiliser-check circuits. Surface codes under depolarising gate noise using various stabiliser-check circuits can have a threshold in the range of 0.5% -1% [82].

Our stabiliser-check circuit is shown in Figure 3, where the CZ gates must be further decomposed into √ SWAP or S as outlined in Section 2.3. Besides √ SWAP or S, we also need single-qubit Z rotations to construct CZ. Z rotations can be implemented as a combination of X and Y rotations (which can be slow as noted in Section 2.4), or using the Stark shift whose speed is limited by the detuning range and whose accuracy relies on careful calibration. Fortunately, in our stabiliser-check circuit, most of the Z rotations on the data qubits can be implemented in a virtual way by shifting the phases of all the future single-qubit rotations pulses [83], and the Z rotations on the ancillae can be omitted since we are performing symmetric operations on the singlet subspace (see Appendix A.4 for details). The only Z rotation that we need to explicitly implement is the Z π sandwiched by the two √ SWAPs, applied to the data qubits. This optimisation to remove single qubit gates substantially reduces the runtime and depth of the stabiliser-check circuit.

As shown in Figure 3, our circuit applies √ Y to all data qubits to switch between X and Z stabiliser checks. Because the ancillae are initialised in singlet states, the √ Y operations can be achieved using global ESR operations applied to all spins 2.2, or through local operations applied only to the data qubits, using EDSR. Each plaquette is given one of four colours, such that plaquettes of the same colour share no data qubits between them. Stabiliser checks of all plaquettes of a given colour are carried out simultaneously, in the sequence indicated by the arrows.

## Stabiliser Cycle and Error Model

We divide all stabiliser checks into four disjoint partitions, performed in sequence, as shown in Figure 4. When one of the partitions become active, any two different stabiliser checks within it are separated by at least one inactive plaquette, across which leakage error cannot propagate. Hence, within each partition, errors (including leakage errors) of one stabiliser check are independent of that of another stabiliser check, such that there are no spatial error correlations beyond a given plaquette. During the stabiliser check of one partition, the mediator reset operation can be activated in the other partitions (see Section 3.3). In this way, leakage errors arising during the active cycle of a given partition do not survive to its subsequent cycle, removing the potential for temporal error correlations. Using this partitioning and sequence of stabiliser updates, the errors in each stabiliser check should be Markovian, removing the temporal and spatial correlations in noise that can be highly damaging to the surface code, and greatly simplifying our error simulation.

Within each stabiliser check, we assume the following error model:

• Two-qubit gates: Charge noise leads to fluctuations in the exchange strength J, which can lead to the following errors for the two-qubit gates that we are considering (shown in Appendix B):

-S gate has Z 1 Z 2 error with probability p 2 .

-√ SWAP gate has SWAP error with probability p 2 /2.

To allow a simple comparison of the thresholds of the two kinds of two-qubit gates, we formulate our simulations in terms of a twoqubit gate error rate p 2 equal to that of the S gate. Assuming that S gates take twice the time required by √ SWAP, the variance of the exchange phase Jt accumulated due to fluctuations in S is twice that of √ SWAP, and thus the error probability of S is twice of that of √ SWAP (see Appendix A.5.2).

• Readout: The current state-of-the-art µsscale readout scheme can achieve 98% fidelity [84], which is the same as the best twoqubit gate fidelity achieved [58]. Hence, here we will assume the readout error rate can be improved at the same pace as two-qubit gate error rate so that we have p readout = p 2 .

• One-qubit gates and initialisation are assumed to have a common depolarising error probability p 1 . The fidelity of one-qubit gates is typically more than one order of magnitude better than two-qubit gates [24,39,57], thus we assume p 1 p 2 = 0.1.

• Spin Leakage: As mentioned in Section 3.2, spin leakage in the ancilla qubits can be taken into account by considering all the possible errors on the individual spin within the ancilla spin pairs. Its effect on the measured parity can also be considered by flipping the parity result whenever there are asymmetric noise acting on the ancilla spin pairs. Note that is a more damaging noise model than the rigorous model 1 , thus should give us a lower bound on the threshold.

1 E.g. if the correct state before the readout is the spinzero triplet state, then even if leakage errors take our state into other triplet state, our readout result should still be correct even though a leakage due to asymmetric noise has happened

• Charge Leakage: When considering charge leakage errors, we first note that each stabiliser check can be divided into two noninteracting halves, each with one ancilla dot interacting with two data dots via two mediator dots as shown in Figure 1. Within each half of the stabiliser, when a leakage error occurs and get restored by the mediators, we will assume the worst-case left-over computational errors in which we have depolarising errors on the whole half (on both of the data qubit and the ancilla spin), so that the leakage error thresholds we derive below can be taken as a lower bound.

Charge leakage errors are most likely to occur during the tuning of potentials, thus we will assume here the charge leakages will only occur during the CZ gates in the stabiliser checks. If p leak is the probability that a charge leakage error occurs during a CZ gate, then needing to perform two CZ gates in each half of the stabiliser checks means that there is a 2p leak probability that the whole half of the stabiliser check will get depolarised in each round of error check.

## Surface Code Threshold Results

First we consider cases without charge leakage errors (p leak = 0). As shown in Figure 5 (a) and (b), the threshold for p 2 is 0.86% using S gates and 0.76% using √ SWAP. Both are comparable to the threshold 0.75% obtained using simple depolarising noise model [85]. The lower threshold for the architecture using √ SWAP is primarily due to the additional Z π needed to construct the CZ gate. Note that the gate errors here also include the spin leakage errors of the ancillae.

To achieve fault-tolerant quantum computation, our gate error rate need to be below the gate error thresholds. Suppose we manage to achieve a gate error rate below these thresholds at p 2 = 0.5%, then the level of charge leakage error we can tolerate with such a gate error rate are indicated by the p leak threshold in Figure 6 (a) and (b), which are 0.27% with S gates and 0.23% with √ SWAP. The charge leakage thresholds we obtained here are on the same order as the gate error rate we assumed here. The energy barrier of the charge leakage errors is usually higher than the errors in the spin space. Hence, we will expect 0.7% 0.75% 0.8% 0.85% 0.9% 0. the charge leakage error rate to be much lower than the usual gate error rate and thus below the charge leakage thresholds we obtained here.

If we can further push down the gate error rate (reducing p 2 ), the charge leakage error threshold will grow, and in the end bounded by the limit in the case of no gate errors (p 2 = 0) where the threshold for p leak is 0.66% (see Figure 6 (c)). The similarity of this pure charge leakage error threshold to that from depolarising noise threshold indicates that in our architecture charge leakage errors can be effectively reduced to computational errors (i.e. errors within the computational subspace) via charge relaxation. In other words, even though the resultant computational errors have strong correlations within a given stabiliser check, charge leakage errors can be limited to be no more damaging than other conventional gate errors. The trade-off between the charge leakage threshold and the gate error rates is further illustrated by additional threshold simulations in Appendix H. Overall, this architecture shows good tolerance towards the computational errors resulting from charge leakage errors, even with a reasonable amount of gate errors present.

## Decoherence Errors

We denote the characteristic time scale of the exchange interaction T J = π J , that of a Hadamard gate ( √ Y ) as T H and that of a Z gate as T Z . Using the stabiliser cycle outlined in Section 4.2 and the stabiliser circuit shown in Figure 3, the time needed for one stabiliser cycle is T cycle S = 8T J + 2T H assuming the use of S-gates and

We have not accounted for the time required for initialisation and readout of the ancillae and the mediator resets because they can take place in parallel with other operations of the stabiliser circle. Such operations only become significant to the rate of the stabiliser check once they become an order of magnitude slower than the quantum gates, which is not the case in the range of parameters that we are considering (see Section 2.2 and 2.5).

Using parameters outlined in Section 2.3, we expect T J ∼ 1 µs. Based on demonstrated electrical tuning of the g-factor, we estimate the duration of Z gates implemented using Stark shifts to be T Z ∼ 0.25 µs [86], while the time needed for a Hadamard gate is likely to differ depending on the use of ESR (T H ∼ 1µs) or EDSR (T H < 0.1µs). We can therefore consider two illustrative cases for the stabiliser cycle time. In one case, micromagnets are used to enable the use of S-gates and EDSR, giving T cycle fast ∼ 8 µs (limited by T J ).  isotopically-enriched silicon, decoherence times have been reported ranging from T * 2 = 20 µs and T 2,CPMG = 3 ms in systems with a micromagnet [28] to T * 2 = 120 µs and T 2,CPMG = 28 ms in systems without micromagnets [39]. The probability of phase flip error per stabiliser cycle using Carr-Purcell-Meiboom-Gill (CPMG) decoupling is hence T cycle 2T 2 ≈ 2 × 10 -4 to 10 -3 for the parameters we considered, well within the per gate error threshold we obtained in Section 4.3. We conclude that the finite decoherence time of spins in silicon measured in devices to date can be tolerated by our surface code architecture.

# Conclusions and Outlook

We have introduced a surface code architecture implemented using spin qubits in silicon quantum dots that is robust against spin leakage errors through its use of single-dot data qubit and robust against charge leakage errors through its use of multi-electron mediator dots. Our approach efficiently unifies the task of maintaining a proper charge distribution (essential for any SS quantum device) together with the task of performing the stabiliser cycles required by the surface code. Charge leakage from the qubit dots is transferred to the mediator dots via fast charge relaxation, and removed using charge reservoirs attached to the mediators, reducing the charge leakage errors to the level of standard computational errors that can be corrected by the surface code. We find that our stabiliser check cycle removes time and space correlations in the remaining computational errors, which can be highly damaging to surface codes. The depth of the stabiliser-check circuit was reduced by the symmetry of the double-dot ancillae and virtual Z gates. Through simulations, we find that the surface code threshold for the computational errors arising from charge leakage errors is 0.66% in the absence of gate errors, showing that its effect can be limited to that of standard depolarising gate errors. Under a reasonable gate error rate 0.5% (which includes ancilla spin leakage errors), we obtain a charge leakage error threshold of 0.23 ∼ 0.27%, showing good tolerance of our architecture towards charge leakage errors even under gate noise. The fidelity of two-qubit gates is expected to the principal bottleneck for reaching the fault-tolerant level, and experimentally demonstrating a high-fidelity mediated exchange interaction using isotopically enriched silicon will be a key step in validating this architecture.

Besides adding tolerance towards leakage errors, the elongated mediator dots in our structure also relax the density of the qubit dots, offering more space in-plane for the essential measuring devices, charge reservoirs and classical control lines, and facilitating fabrication using (e.g.) CMOS technology [12]. The extra space provided by the mediators and the unique properties of the double-dot ancilla enable more convenient integration of micromagnets which can increase the speed of both the single qubit rotations and stabliser check cycle.

We find that gate mechanisms and energy scales that have already been experimentally reported will suffice to realise a stabiliser cycle time approaching the MHz domain, and that this speed is sufficient to suppress environmental decoherence. This is not a fundamental limit to the operation speed of such a device, however, it makes use of a mediated exchange interaction, which is inherently slower than direct exchange. To push the speed further, data or ancilla spins could be shuttled onto the mediators for direct exchange with a neighbouring ancilla/data spins, and such exchange gates between a singleelectron dot and a multi-electron dot have been demonstrated [22,87]. Shuttling in combination with micromagnet-induced field gradients may introduce significant dephasing noise which may be challenging to correct (e.g. using calibration and single-qubit rotations). As in many approaches, there is a trade-off between speed and error rate to be carefully considered.

A second factor in the speed of the processor operation is charge relaxation, which we have assumed to be fast compared to the gates. If this were not the case charge leakage errors would not be rapidly transferred from the qubit dots to the mediators, and empty qubit dots may remain after a stabiliser cycle, leading to a nontrivial errors of a non-Markovian nature. Nevertheless, we would expect the charge leakage process and the relaxation restoring force to reach some equilibrium, leaving the proportion of the empty qubit dots in the surface code fixed. Further work could study the non-Markovian effects of the empty qubit dots, and the equilibrium value of the leaked qubit fractions under different charge leakage and relaxation models. Nevertheless, in cases where charge relaxation time was non-negligible, existing leakage correction protocols like active leakage detection and correction, or leakage reduction units could be adopted. Indeed, combining active methods with inherent robustness to leakage errors may be advantageous, especially if the native leakage rate is high.

Features from other silicon quantum computing architectures like shared control lines [12,14] and modularity [15] could also be adopted into our structure, if challenges around the inhomogeneity of quantum dots and shuttling noise can be minimised. Conversely, the introduction of additional quantum dots and electrons into a system to create accessible metastable charge states could be adopted in other approaches to offer robustness against charge leakage errors.

# A Two ways to achieve CZ between data and ancilla qubits A.1 Hamiltonian

The two-spin Hamiltonian is:

The Zeeman splitting H 0 can be further split into:

where

# A.2 Ω J: simple exchange interaction

Since Ω J, and

i.e. to perform the exchange interaction in the rotating frame is just the same as performing the exchange interaction in the lab frame.

The evolution operator due to H ex is given by: A CZ can be implemented using √ SWAP in the following way:

Following arguments from [56,57], without exchange interaction we have

We can see that E z determine the eigenenergies in the parallel spin subspace, while Ω determine the eigenenergies in the anti-parallel spin subspace. If we add in the exchange Hamiltonian

in the parallel spin subspace, the energy of both states will be shifted up by J 2 . In the anti-parallel spin subspace, if Ω J, then H ex can be treated as perturbation. Using first order perturbation theory, the shift in eigenenergies for the antiparallel spin states is 0.

Hence, to first order approximation, in which the eigenstate do not change and only eigenenergies change, the exchange Hamiltonian (which is to first order the shift in eigenenergies) becomes

This is just a dipole-dipole interaction, which, because it commutes with H 0 , has a rotating frame form identical to its lab form. Allowing this Hamiltonian to evolve for a time period π J , produces the following gate:

A CZ gate can be built from S using:

# Virtual Z gate and symmetric operations on ancilla

Whether using S or √ SWAP to construct a CZ, the only type of single-qubit gate needed is the Z rotation, which can be implemented in a virtual way by shifting the rotating reference frame by a given phase [83]. Such Z rotations are essentially error-free and require zero time. This corresponds to adding a phase offset to all subsequent X, Y gate pulses, and switching all subsequent two-qubit gates into the new rotating frame after the virtual Z rotation. Two-qubit gates whose Pauli components consist of only tensor products of I and Z are invariant under changing rotating reference frame, hence we do not need to modify these two-qubit gates after the virtual Z rotation. The other two-qubit gates usually have different forms in the shifted rotating frame and might not be achievable through our Hamiltonian.

Following such arguments, we find that for the CZ gate constructed using the exchangeinteraction, the Z π bracketed by the two √ SWAPs cannot be applied in a virtual way, while the two Z rotations outside the √ SWAPs can. For the dipole-dipole CZ gate, all the Z rotations can be applied in a virtual way.

However, there is another caveat. For the virtual Z rotation to work, we need to do the measurements in Z basis at the end, so that all the remnant Z rotation for compensating for the virtual Z gates will have no effect on the measurements (though we can use the shifted one qubit gate to change the measurement basis). Our ancilla measurement does not use a standard basis: our measurement only tells us whether the ancilla is in the singlet or triplet state, where the singlet state and the triplet states does not corresponds to a qubit representation. Thus, we cannot use virtual Z gates here for our ancilla qubits, but can instead permute all the Z rotations (besides the one bracketed by √ SWAP) to the position right after the initialisation of the singlet state. We then use the fact that the initial singlet state is invariant under symmetric gates operating on both ancilla dots, to see that there is no need to apply the Z rotations at the ancilla (besides the one bracketed by √ SWAP). Hence, under either approach to implement a CZ gate, the only single-qubit gate that we need to implement is the Z π bracketed by √ SWAPs. All the other Z rotations can be either implemented in a virtual way or can be omitted due to the property of our ancilla qubits.

# A.5.1 Operation time

We denote the characteristic time scale of exchange interaction as T J = π J , and that of Z gate as T Z . The time we needed to achieve a CZ using dipole-dipole like interaction is just T J , no singlequbit gates needed. On the other hand, the time we need to achieve a CZ using exchange interaction is T J + T Z . The extra term here is due to the Z π gate that we need to explicitly implement.

# A.5.2 Errors

Errors due to fluctuation of Jt:

The ideal exchange phase for √ SWAP is θ sw = Jt sw = π 2 . We will denote the variance in θ sw due to fluctuations in exchange strength J or operation time t as 2 sw . The ideal exchange phase for S is θ s = Jt s = π. If we divide the accumulation of phase θ s into two independent stages, with each stage accumulating phase π 2 = θ sw , then we have θ s = θ sw,1 + θ sw,2 . Hence, the variance of θ s is just 2 s = 2 2 sw . As shown in Appendix B, such fluctuations will lead to:

sw probability of having a swap error.

• S: p s = 2 s = 2p sw probability of having a Z 1 Z 2 error.

# Errors due to approximations made:

The main approximation made in deriving the exchange interaction is ignoring the higher order exchange terms which will not change the form of interaction (shift of energy in the singlet subspace w.r.t. the triplet subspace), but only shift the strength of exchange interaction. This is possible to overcome via careful calibrations. Of course there are also perturbations to the eigenstates that we have not considered, which might lead to leakage errors as shown in Appendix F.

Since both √ SWAP and S make use of exchange interactions, they are equally affected by the approximations made in the treatment of the exchange interaction. In addition, there are higher order corrections to the S gate due to the assumption J Ω of magnitude J Ω . Similarly, there are higher order corrections to the √ SWAP gate due to the assumption Ω J of magnitude

B Errors due to fluctuation in interaction strength and time

# B.1 General theory

Suppose the Pauli basis of Hamiltonian H is the set G H :

Then we can define the magnitude of H to be E, and the normalised version of H to be h where:

for α i = β i E and we have i α 2 i = 1. Now the evolution operator is just:

However, over-and under-rotations of θ occur in the experiment due to imprecise pulse timing t or fluctuation of interaction strength E. If there is a 50% percent chance of over and under rotation by 1, we have:

Then the effective operation is just

Similar channels are obtained for other symmetric over/under-rotation distributions that are centred on the correct rotation angles.

# B.1.1 h is unitary

If h is unitary (and remember it is also Hermitian since it is the normalised Hamiltonian), e.g. h is SWAP or Pauli, then (7) turns into

i.e. we have either perfect U (θ) or 2 probability of having a h error on top of U ex (θ).

# B.1.2 Twirling

Twirling is a technique use for transforming the given error channel into a Pauli channel to obtain a simpler description of the error channel.

The Pauli decomposition of I -

After twirling, the noise due to non-identity Pauli components scales as O( 4) in the Pauli channel, and hence is negligible. The Pauli decomposition of h is just (6). Hence, after twirling, the effective error channel we have is just:

i.e. it is an error channel with 2 α 2 i probability of the Pauli error g i happening on top of the perfect operation U (θ).

# B.2.1 Exchange Interaction

For an exchange interaction, we have:

We have fluctuation sw 1 in θ = Jt 2 and h = SWAP is unitary. Hence, using (8), we have:

i.e. we have either perfect U ex (θ) or 2 sw probability of having a SWAP error on top of U ex (θ).

# B.2.2 Dipole-dipole Interaction

For a dipole-dipole interaction, we have:

We have fluctuation s 1 in θ = Jt 2 and h = Z 1 Z 2 is unitary. Hence, using (8), we have:

i.e. we have 2 s probability of having a Z 1 Z 2 error.

# C Background exchange interaction

In our system, t ab and ∆ M are generally fixed in a given device, however, their values can be engineered in the device design. The mediated exchange coupling (and hence the CZ gate) can be turned on and off by shifting the detuning of the mediator dot with respect to the side dots to switch ∆ L/R between ∆ on and ∆ off . Since ∆ off is finite, there is a residual exchange interaction even in the off stage. Using (1), we obtain the strength of such residual exchange interaction compared to our intended exchange interaction:

If we look at the direct exchange interaction instead, we have J ∝ |t| 2 ∆ and hence J off Jon = ∆on ∆ off . Hence, we see that the residual exchange interaction of mediated exchange is more suppressed than direct exchange when only tuning the onsite energy of quantum dots.

An imperfect 'off' state also leads to nextnearest-neighbour interactions. For direct exchange interaction, the next nearest neighbour interaction is approximated as t ∆ off 2 of the nearest neighbour interaction. In the mediated exchange interaction however, the next nearest neighbour interaction is approximately t ∆ off 4 of the nearest neighbour interaction, which is again much more heavily suppressed than the direct exchange case.

Hence, by using mediated exchange interactions we can more confidently ignore the effect of residual exchange interactions and next nearest neighbour interactions in our analysis.

# D Comparison of leakage resilience to architectures without mediators

As mentioned before there are two general schemes to deal with leakage errors in qubits: using leakage reduction protocols or detecting leaked qubits and replacing them.

Using leakage reduction units [71,73] requires a large number of additional ancilla qubits, which can be hard to integrate due to space constraints in addition to the qubit overhead they bring. We can reuse some of the ancilla qubits to alleviate such challenges, but this in turn significantly increases the surface code runtime and circuit depth. Another way to achieve leakage reduction is by swapping the data and ancilla qubits at the end of every full stabiliser cycle [72], which does not require any additional ancilla qubits. However, such a scheme is not compatible with architectures that have single-dot data qubit and double-dot ancilla. Moreover, it assumes that the initialisation process of ancilla dots will fix the leakages. This will only be true if we use charge reservoirs for the initialisation of ancilla during the error correction cycle. To prevent the initialisation process of ancilla qubits from affecting other qubits, the charge reservoirs would need to be integrated into the structure and attached to every dot instead of placed at the boundary and relying on shuttling, which is challenging to achieve in a dense quantum dot array without mediators due to space constraints.

As with leakage reduction circuits, leakage detection circuits [69,70] also require a signifincant increase in ancilla number or bring a significant cost in surface code runtime and circuit depth. A more practical approach would instead be to use physical charge detectors for leakage detection. In architectures without mediators, the leading leakage errors are one missing or one extra charge in the quantum dot. Charge detectors would therefore need to be interpersed within a densely packed quantum dot array and capable of accurately distinguish between the three different charge states. Furthermore, after the detection of a charge leakage, we cannot correct them by simply shuttling the leaked charge back because charge leakage can propagate across the array of quantum dots. Overall, this leads to significant practical challenges and spatial constraints. Furthermore, the general leakage reduction/detection circuits described above assume the two-qubit gates in the leakage reduction/detection stage do not induce further leakage or transfer leakage and this is not the case for general two-qubit gates implemented in coupled quantum dot spins.

The practical challenges associated with integrating additional components or ancillae for leakage correction may be solved by using a modular structure [15]. However, such a scheme creates a new source of leakage errors since it involves shuttling electrons across dozens of quantum dots. To keep the leakage error rate of across-array shuttling low, we need to have an extremely low rate of between-dot shuttling leakage, which means that we need to tune the gate voltages very slowly to maintain excellent adiabaticity. This leads to a trade-off between leakage suppression and the processing speed of the architecture. In addition, additional schemes to cope of leakage errors from the shuttling itself would be needed.

In architectures without mediators, if the parameters of direct exchange are chosen such that they have similar speed as mediated exchange, then the probability of leakage under direct exchange will be smaller than that using mediated exchange due to the higher energy of the excited charge state. However, if we did not take any active measures against the leakage errors, regardless of how small the leakage error probability is (as long as it is non-negligible), the leakages will keep accumulating until they break our code. As seen from above, active leakage correction schemes lead to a large runtime/qubit overhead. For a dense array of quantum dots, the reservoirs needed for leakage reset or the charge detectors needed for leakage detection are challenging to integrated due to space constraints, while in the modular scheme, the required elec-tron shuttling creates a new source of leakage. In contrast, to handle leakage in our architecture, there are no additional components nor complex schemes required. We merely reset the mediators when they are idle, making our architecture more robust against charge leakage errors compared to the other quantum dot architectures.

# E Resultant Computational Error from Leakage and Restoration

For our system, there is no reason to assume that either the leakage event or the restoring charge relaxation are spin-conserving. Hence when a spin in a qubit dot is leaked and restored, we can assume that all the spin information is lost, which is equivalent to a depolarising error. When we look at the exchange interaction between qubit A and B via a mediator. If qubit A has leaked and been restored, it will be depolarised. Before the leakage, qubit B interacts with the original qubit A, and after the leakage qubit B interacts with the depolarised qubit A (via a mediator that might be faulty). The leakage and restoration can happen at any point during the exchange interaction, such uncertainty leads to a random depolarising error on the qubit B as well.

Besides the depolarisation of the data qubit and the ancilla qubit involved in the exchange interaction, a leakage error may also lead to faulty mediator dots and hence affect the subsequent gates. Each stabiliser check cycle can be divided into two halves (interacting only inasmuch as they each include one dot of an ancilla doubledot pair): a five-dot system with one ancilla dot (A) connecting to two data dots (D1 and D2) via two mediators (M1 and M2). A interacts with D1 first via M1 in stage 1, then with D2 via M2 in stage 2. An error in stage 1 only affects stage 2 if A has leaked and been restored using an electron from M2. In such a case, the left-over electron in M2 will be in a random state, thus when the electrons in A and D2 interact with the left over electrons in M2 in stage 2, they will also be depolarised regardless of whether further leakages and restorations happens in stage 2 or not.

Hence, we have the following leakage error table for the five-dot system with a exchange gate leakage probability p: 

A and D1 depolarised p : Any leakages All depolarised Hence, we can see here we have (1 -p) 2 = 1 -2p + p 2 probability of having no leakage, and otherwise we will have partial or full depolarisation errors to the three qubits. In the calculations described in the main text, we have assumed an error model where we have 1 -2p probability of having no leakage and otherwise have full depolarisation errors on all three qubits, which is a more severe error model than the more detailed one we describe here.

# F One possible leakage mechanism F.1 Three-dot system

With reference to Figure 2 in the main text, the charge configuration of the ground state is (1, 2, 1). In the exchange Hamiltonian, the charge ground state is connected to the excited state charge states (0, 3, 1) and (1, 3, 0) via the tunnelling energies t L2 and t R2 . Hence, the eigenstates of the exchange Hamiltonian are a superposition of the ground and excited state charge configurations. As noise causes such a superposition to decohere, there is a possibility that the exchange eigenstates will collapse into the excited state charge configuration, bringing the three dot setup out of the computational subspace, and leading to leakage errors.

The probability of such a leakage error is related to the amplitude of the excited state in the coupled system eigenstate. Using perturbation theory, such an amplitude has a magnitude of t ∆ , where t is the tunnelling energy between the high energy state and the ground state while ∆ is the energy difference between them. Hence, the possibility of our ground charge configuration (1, 2, 1) escaping into the high energy charge configuration (0, 3, 1), (1, 3, 0) will be on the or-

, which means that such leakage process will only be significant during the exchange interaction (when |∆ L,R | is small). Below we present a detailed analysis for the two-dot case, which can be easily generalised to our case.

# F.2.1 Hamiltonian

For our two-dot system, we denote |T as the triplet state with zero z-component, |S as the singlet state, |ion + as the state that has two electrons in one dot that can be reached by |S via hopping, and |ion -as the other state with two electrons in one dot but is orthogonal to |ion + .

We divide the Hamiltonian H into two parts, a dominating diagonal part H (0) :

|ion -= 3 (0)   and a small off diagonal (tunnelling) part rH (1) .

rH (1)  |ion + = 2 (0)

r here is the ratio between the off-diagonal tunnelling energy t and the diagonal detuning energy ∆:

Here we see that rH (1) only mixes |S and |ion + and leaves |T and |ion -unchanged.

Starting from the eigenstates and the eigenenergies of H (0) , we can obtain the eigenstates and the eigenenergies of H using perturbation theory: H = H (0) + rH (1)   |n = n (0) + r n (1) + r 2 n (2) 

n + rE (1)  n + r 2 E (2)  n + • • • the superscript (m) denotes the m th -order correction.

# F.2.2 Perturbation theory

• Change in states ⇒ leakage error:

n (0) rH (1) 1 (0)

2 (0) rH (1) 1 (0)

n (0) rH (1) 2 (0)

Hence

• Change in the ground state energy ⇒ exchange interaction:

The leading non-vanishing order of energy shift is

# Leakage oscillation

Now if we start in the state of |S = 1 (0) the probability of leaking into |ion + = 2 (0) is:

= n e -iEnt 2 (0) n n 1 (0)

= e -iE 1 t 2 (0) 1  

# G Threshold Simulation Details

Based on the circuit and the error model outlined in Section 4, we can obtain two error tables that outlines the probabilities of all possible error patterns (including both the errors on data qubits and the parity errors of the measurement results) when performing the X and Z stabiliser checks respectively. This will enable us to perform a Monte Carlo simulation of the stabiliser check process with errors arising according to the probability obtained from the error tables. Each round of stabiliser checks will give rise to a 2D grid of parity check results. For a distance-d surface code, we will repeat our stabiliser measurement for d times to fight with measurement errors, which can be viewed as stacking up d layers of 2D parity result grid, giving rise to a 3D grid with one of the dimension being time [82]. We can then try to match the failed parity checks to the boundary or to any change in the parity results in the time direction using minimum-weight perfect matching(MWPM), which is carried out using the Blossom V package [88]. The surface code threshold simulation module we used is published on Github [89]. For simplicity, in our simulation we have the same weight for the edges in the spatial direction and the edges in the time direction. However, threshold improvements can be gained by optimising the weight ratios between them due to the different probabilities of failure. Further improvements of the threshold can be achieved by using more advance decoders, e.g. the maximum likelihood decoder [90]. 

# Acknowledgements

This work has been supported by Quantum Motion Technologies Ltd. SS and SF acknowledge the Engineering and Physical Sciences Research Council (EPSRC) through the Centre for Doctoral Training in Delivering Quantum Technologies (EP/L015242/1) and SCB acknowledges support from ESPRC grant EP/M013243/1 (the NQIT Quantum Hub).

