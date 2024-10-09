# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- relate to nuclear spin wave quantum registers

### 2. Description of Related Art

- describe limitations of solid-state nuclear spins

## SUMMARY OF THE INVENTION

- report novel system for transferring quantum information
- describe qubit with zero magnetic dipole moment
- describe indistinguishable register spins
- describe protocol for controlling spin preserving interaction
- describe decoupling qubit from noise
- describe polarizing register spins
- describe generating swap gate
- describe generating square root of swap gate
- describe device for coupling qubit to register
- describe controlling application of protocol
- describe suppressing non-exchange interactions
- describe suppressing noise
- describe enabling coherent spin exchange interaction
- describe controlling period of protocol
- describe controlling phase and duration of pulses
- describe preserving spin exchange interactions
- describe cancelling non-exchange interactions
- describe cancelling exchange and non-exchange interactions
- describe cancelling qubit decoherence
- describe toggling RF field
- describe selecting amplitude of RF field
- describe forming predictable spin exchange interaction
- describe using pulses for single qubit gates
- describe configuring register spins in polarized state
- describe applying first swap gate
- describe applying second swap gate
- describe applying first square root of swap gate
- describe applying second square root of swap gate
- describe using device in quantum memory
- describe using device in repeater in quantum network

## DETAILED DESCRIPTION OF THE INVENTION

- introduce system and method for implementing protocol for coupling qubit to register
- describe protocol comprising sequence of pulses synchronized with RF field
- motivate use of nuclear spin-wave like states for quantum memory
- introduce example of embodiment using single rare-earth ion qubits

### 1. First Example: System Implemented in Yb:YVO

- introduce Yb:YVO system with 171Yb qubit and 51V nuclear spins
- describe qubit operation and coherence times
- introduce local crystalline environment and 51V nuclear spin structure
- categorize 51V ions into register and bath
- describe register spins and 171Yb interaction Hamiltonian
- introduce challenge of spectral indistinguishability of register spins
- propose storage in collective states using spin waves
- describe preparation of thermal register ensemble into pure state
- transfer single excitation from 171Yb to register
- realise entangled four-body W-state
- describe quantum swap gate between 171Yb qubit and 51V register
- introduce ZenPol sequence for robust dynamic Hamiltonian engineering
- describe ZenPol sequence and its synchronisation with 51V precession
- derive time-averaged effective Hamiltonian for ZenPol sequence
- describe insensitivity of protocol to random noise from bath
- introduce example protocol for ZenPol sequence
- perform spectroscopy of 171Yb nuclear spin environment
- polarise entire nuclear spin register using ZenPol sequence
- induce coherent oscillations of single spin excitation
- verify collective enhancement of spin-exchange rate

### 2. Example Protocol for the First Example

- use ZenPol sequence for spectroscopy of 171Yb nuclear spin environment
- perform polarisation of entire nuclear spin register
- induce coherent oscillations of single spin excitation
- verify collective enhancement of spin-exchange rate
- control spin-exchange rate using RF field amplitude
- suppress oscillations with 171Yb initialised in |0g
- verify existence of two distinct 51V ensembles
- estimate polarisation fidelity of register spins
- discuss limitations of polarisation protocol

### 3. Example Implementation of the First Example as Quantum Memory

- transfer superposition state from 171Yb qubit to 51V register
- store transferred state for variable wait time
- measure coherence of final state
- decouple 171Yb dipole moment noise from register
- extend coherence time using dynamical decoupling on 51V register

### 4. Example Bell State Generation Using the First Example

- introduce Bell state generation
- describe multi-spin register benchmarking
- derive Bell state preparation using √{square root over (swap)} gate
- evaluate Bell state coherence
- apply XY−8 decoupling sequence to improve coherence
- estimate Bell state preparation fidelity
- discuss limitations and potential applications

### 5. Supplementary Example Methods for Implementing the First Example

- illustrate experimental setup
- describe YVO4 crystal preparation
- detail nanophotonic cavity fabrication
- explain cavity properties
- describe cryostat setup
- detail optical signal feeding
- describe device tuning
- explain magnetic field cancellation
- introduce optical transitions for state readout and initialisation
- describe Ti:Sapph laser setup
- detail AOM setup
- explain pulse generation
- describe light output separation
- detail time-resolved gating
- introduce SNSPD detector
- describe photon detection events
- introduce microwave pulses for qubit control
- detail arbitrary waveform generator setup
- describe microwave signal amplification
- introduce diplexer setup
- describe gold coplanar waveguide fabrication
- introduce 171Yb initialisation protocol
- describe readout of 171Yb|1g state
- introduce pulse sequence for storing and retrieving superposition state
- derive effective Hamiltonian for hybrid spin system
- introduce ZenPol sequence
- describe toggling-frame transformation
- explain average Hamiltonian in rotating frame
- define supplementary example methods
- derive average Hamiltonian
- simplify average Hamiltonian
- define coefficient b(k,ω)
- discuss direct drive gates for 51V register
- describe dynamical decoupling mechanism
- derive driving Hamiltonian
- discuss amplification factor
- describe Rabi oscillation dynamics
- calibrate 51V π pulse times
- discuss motional narrowing techniques
- describe phase-continuous driving
- discuss direct drive protocol
- describe population basis measurements
- develop sequential tomography protocol
- describe readout sequences
- discuss state preparation fidelities
- characterize maximally entangled Bell state
- discuss swap gate fidelity correction
- measure swap gate fidelity
- correct populations using swap gate fidelity

### 6. Supplementary Example Derivations for Interactions and Hamiltonians Described Herein

- define 171Yb-51V interactions
- derive ground state 171Yb Hamiltonian
- specify ground state g tensor
- specify ground state A tensor
- describe local nuclear spin environment
- derive zero-field energy level structure of bath
- tabulate positions of nearest 51V ions
- specify 51V g-tensor
- derive magnetic dipole-dipole interaction Hamiltonian
- apply secular approximation to interaction Hamiltonian
- describe nuclear Overhauser field
- derive z-component of Overhauser field
- describe perturbed eigenstates of 171Yb qubit
- derive detuning of 171Yb transition frequency
- derive interaction Hamiltonian
- express interaction Hamiltonian in perturbed basis
- simplify interaction Hamiltonian using local basis transformations
- derive full system Hamiltonian
- describe randomised benchmarking
- apply randomised benchmarking to characterise single qubit gate fidelity
- measure T2 coherence time using dynamical decoupling
- provide extra register detail
- express engineered spin-exchange interaction
- derive spin-exchange evolution
- express single-spin excited state
- postulate register composition
- recover expressions for single-spin excitation and spin-exchange rate
- describe possibility of transferring second spin excitation
- describe spin-preserving exchange interaction
- describe preparation of 171Yb qubit
- describe utilisation of dense lattice nuclear spins
- show ZenPol spectra
- show collectively enhanced spin-exchange oscillations and motionally-narrowed T2* times
- simulate coupled spin system
- introduce nuclear Zeeman interactions
- introduce nuclear magnetic dipole-dipole interactions
- introduce 171Yb-enhanced register spin-spin interactions
- extract gvz value from simulation
- estimate gvx value from calibration
- compute nuclear Overhauser field
- simulate register spin dynamics
- incorporate imperfect polarisation
- model finite pulse duration effects
- add phenomenological exponential decay envelope
- fit model to experimental results
- model single-spin excitation in ωc-manifold
- perform Hartmann-Hahn spectroscopy
- drive 171Yb qubit with Rabi frequency
- read out 171Yb dressed state population
- explore polarisation dynamics using PROPI method
- measure 171Yb population after polarisation cycles
- demonstrate effect of incomplete register polarisation
- design polarisation sequences for single-spin excitation
- estimate polarisation fidelity from simulations
- analyse spin exchange dynamics on ωc register transition
- measure spin-exchange frequency and contrast
- compare results with simulations
- demonstrate spin exchange frequency control
- describe single excitation in ωc manifold
- prepare |1v′ state
- induce spin exchange oscillation
- discuss benefits of ωc manifold
- discuss T2* coherence decay processes
- describe direct nuclear Zeeman interaction
- describe 171Yb Knight field
- simulate register coherence times
- discuss T1 lifetime of |0v state
- discuss resonant population exchange
- discuss off-resonant population exchange
- discuss T1 lifetime of |Wv state
- describe dephasing effect on register spins
- apply pure-dephasing master equation model
- solve equation for different initial states
- derive dephasing model
- verify dephasing model
- extend T1(W) lifetime
- note limitations of model
- derive parity oscillation contrast
- define readout fidelity
- represent parity readout matrix
- extract Bell state coherence
- estimate Bell state coherence
- perform maximum likelihood analysis
- extract Bell state fidelity
- evaluate error
- describe hardware environment
- illustrate computer-implemented system
- describe computer components
- describe input/output devices
- describe computer operation
- describe special purpose processor
- describe compiler
- describe external communication device
- describe computer-readable medium
- describe computer program product
- illustrate distributed/cloud-based computer system
- describe network
- describe clients and servers
- describe cloud-based computing system
- describe resource sharing
- describe client application
- describe web server
- describe ASP or ISAPI application
- define components of device
- describe data storage and communication
- introduce client and server computers
- describe software protocol application
- introduce process steps
- describe method of making a register
- obtain device for coupling qubit to register
- describe device components
- describe signal generator and arbitrary waveform generator
- describe computer and program control
- describe application specific integrated circuit
- describe timing circuits
- optionally couple device to sources of electromagnetic fields
- optionally couple sources to photonic cavity
- optionally couple sources to qubit
- describe qubit and register
- describe system implementation
- describe detector coupling
- describe system for coupling qubit to register
- describe protocol configuration
- describe suppressing non-exchange interactions
- describe controlling pulse application
- describe quantum memory and swap gates
- define device configuration
- describe polarizing register spins
- detail protocol for spin excitation transfer
- specify qubit and register states
- describe W state
- outline device operation
- describe repeater in quantum network
- illustrate system components
- detail circuit control
- describe pulse sequences
- specify pulse properties
- describe spin exchange interaction
- detail RF field interaction
- illustrate pulse sequence example
- describe decoherence noise reduction
- outline system for quantum register
- describe spin carrying defect
- specify register spin composition
- describe system state oscillations
- outline protocol for coherent spin exchange
- describe spin exchange interaction types
- specify RF field frequency range
- outline method for qubit operations
- describe quantum memory method
- outline Bell state measurement method

## Definitions

- define pi pulse
- explain spin-exchange interaction

## CONCLUSION

- conclude and disclaim

