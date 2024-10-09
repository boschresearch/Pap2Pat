# DESCRIPTION

## BACKGROUND

- introduce quantum computing
- define qubits and quantum states
- explain superposition and entanglement
- describe quantum algorithms and circuits
- discuss types of qubits and limitations

## DETAILED DESCRIPTION

- introduce quantum computers and fault-tolerant quantum circuits
- describe surface codes and their limitations
- introduce ATS-phonic hybrid system for reducing cross-talk errors

### Asymmetrically Threaded Superconducting Quantum Interference Device (ATS)-Phononic Hybrid System

- introduce ATS-phonic hybrid system for quantum computing
- describe nano-mechanical resonators and ATS implementation
- explain hybrid acoustic-electrical qubits
- discuss scalability of ATS-phonic hybrid system
- introduce multiplexed control of phononic resonators
- describe structure of chip with phononic resonators and ATS
- explain electrical connections to ATS and piezoelectric material
- discuss phonon coupling rate and Hamiltonian for the system
- introduce non-linear coupling of nano-mechanical resonators
- describe ATS potential and its simplification
- explain control circuit and quantum information storage
- discuss autonomous error correction using two-phonon driving and decay
- introduce protected subspace for encoding qubits

### Multi-Mode Stabilization/ATS Multiplexing

- extend scheme to multi-mode setting
- introduce incoherent dissipator
- detune pumps to avoid simultaneous loss
- simulate master equation to determine detuning parameters
- discuss bandwidth limits for de-tunings
- use filters to alleviate bandwidth limits
- eliminate correlated errors in multiplexed stabilization

### Multi-Terminal Mechanical Resonators

- design nano-mechanical resonators with multiple terminals

### Example Physical Gate Implementations

- simplify Hamiltonian by neglecting frequency shifts
- realize linear drive on phononic mode
- implement compensating Hamiltonian for CNOT gate
- overcome frequency collision issues
- realize optomechanical coupling and selective frequency shift

### Example Processes for Implementing an ATS-Phononic Hybrid System

- stabilize nano-mechanical resonator using ATS
- stabilize multiple nano-mechanical resonators using multiplexed ATS

### Cross-Talk Suppression Via Filtering, Phononic Mode Frequency Selection, and Dump Mode Detuning Selection

- introduce cross-talk among cat qubits
- describe three mechanisms of cross-talk
- motivate filtering and phonon-mode frequency optimization
- explain decoherence associated with keff and γeff
- describe configuration of mode frequencies in FIG. 7C
- discuss optimization procedure for mode frequencies
- motivate focus on crosstalk errors induced by specific terms in Hamiltonian
- describe three types of correlated errors: Type I, Type II, and Type III
- derive effective operators for Type I errors
- describe correlated phase errors induced by Type I errors
- derive effective operators for Type II errors
- describe coherent errors induced by effective Hamiltonians
- motivate use of bandpass filter for cross-talk mitigation
- describe tight-binding model for filter
- illustrate suppression of Type I and Type II errors using filter
- introduce cross-talk suppression via filtering, phononic mode frequency selection, and dump mode detuning selection
- derive effective Hamiltonian and discuss limitations of adiabatic elimination
- motivate time averaging to study interplay of filter and effective Hamiltonian
- adiabatically eliminate buffer, filter, and excited states of storage mode
- calculate phase flip rate and show exponential suppression by filter
- introduce cross-talk mitigation using mode frequency optimization
- discuss constraints imposed by surface code architecture
- construct cost function to quantify cross-talk
- define conditions for large cost function
- quantify coherent Type III errors and define probabilities
- perform numerical search to minimize cost function
- discuss optimized results and robustness to deviations
- illustrate flowchart of multiplexed control circuit stabilizing phononic modes
- summarize steps of multiplexed control circuit operation
- introduce phononic mode frequency selection
- describe process for minimizing coherent errors
- motivate need for additional edges in decoding graph
- describe correlated error rates pdouble and ptriple
- illustrate logical Z failure rates with and without crosstalk
- describe adding edges for dealing with correlated errors
- illustrate fictitious two-qubit and three-qubit gates
- describe extra edges added to graph Gd(3D)
- define edge-weight probabilities for added edges
- outline process of decoding syndrome measurement history

### Hybrid Bacon-Shor Surface Code

- illustrate hybrid Bacon-Shor surface code
- describe SBS code implementation
- motivate SBS code advantages
- define SBS code stabilizer group
- explain SBS code error correction
- compare SBS code to thin-stripped surface codes
- highlight benefits of reduced modes per ATS
- discuss SBS code implementation advantages

## Illustrative Computer System

- illustrate computing device
- describe processor and system memory
- detail I/O interface and network interface
- explain system memory components
- describe network interface functionality
- define computer-accessible medium

## CONCLUSION

- summarize computer-accessible medium and method modifications

