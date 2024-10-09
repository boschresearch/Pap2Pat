# DESCRIPTION

## NOTICE

- disclose government support

## BACKGROUND

- introduce beamforming
- describe limitations of existing beamforming techniques
- motivate need for new solution

## SUMMARY

- introduce TX beamformer
- describe amplitude and direction control
- introduce multiphase beam steering transmitter
- describe multiphase controller
- describe vector addition of beam phase and amplitude
- describe array of transmitters
- describe multiphase clock generator and logic decoder
- describe beamforming method

## DETAILED DESCRIPTION

- introduce exemplary embodiments
- describe accompanying drawings
- explain purpose of detailed description
- introduce beamforming transmitters with multiphase beamforming
- describe simultaneous frequency translation, digital-to-analog conversion, and front-end power amplification
- introduce split-array multiphase (SAMP) switched-capacitor power amplifiers (SCPA)
- describe high resolution complex beamweighting
- explain beamweighting by leveraging control of clocking edges and/or control of the ratioed capacitance of a capacitor array of the SCPA
- describe output of desired amplitude and/or phase by SAMP-SCPA
- compare multiphase signaling with polar signaling
- describe linearity of SCPA compared to current-mode digital power amplifiers (DPAs)
- introduce FIG. 1, a block diagram of a multiphase beamforming transmitter system
- describe internal components of transmitters TX1-4
- explain phase modulated RF clock signal input to multiphase clock generator
- describe output of basis phases by multiphase clock generator
- introduce digital input code (Bin) and its effect on multiphase logic decoder (MLD)
- describe amplitude- and phase-weighting for desired beam output
- introduce FIG. 2, a schematic diagram of a multi-element beamforming transmitter
- describe internal components of transmitters TX1-4
- explain clock selection logic and multiphase logic decoder
- describe MP-SCPA and its operation
- introduce FIG. 3, a schematic diagram of a multi-element beamforming transmitter according to a second embodiment
- describe internal components of transmitters TX1-4
- explain phase injection locked ring oscillator and its operation
- describe multiphase logic decoder and its operation
- explain beamweighting and steering in two steps
- describe operation when control signal is disabled
- introduce SAMP-SCPA core and its operation
- describe output of reconstructed signal to RF matching network
- introduce SAMP-SCPA 400
- describe capacitor array 402
- detail C-2C portion and unary portion
- explain capacitor array configuration
- describe switch 410 and driver chains 412
- detail NOR logic circuit 416 and MUX 418
- explain output signal generation
- describe matching network 450
- introduce unary logic and driver
- detail driver chain 412 and level shifter 414
- describe inverter chains 502 and 504
- introduce unit inverter 600
- detail PMOS transistor 602 and NMOS transistor 604
- introduce output switch 410 and capacitor
- detail cascoded CMOS inverter
- introduce multiphase vector addition
- describe basis phase vectors in complex plane
- detail time domain waveforms
- explain basis phase weights calculation
- introduce MP-SCPA 900
- describe capacitor arrays 910 and 912
- detail weight control of capacitors
- explain sum of n1 and n2 bound
- describe application of MP-SCPA 900
- summarize SAMP-SCPA 400 operation
- conclude SAMP-SCPA 400 description
- define capacitor arrays
- derive weights n1 and n2
- calculate voltage amplitude Vout
- calculate output power Pout
- calculate input power Pin
- calculate drain efficiency η
- discuss SCPA operation
- discuss split-array techniques
- discuss series resonant circuit
- calculate inductance Lser
- discuss impedance matching network
- discuss drain efficiency η
- discuss multiphase technique
- discuss SAMP-SCPA operation
- discuss phase resolution
- discuss amplitude resolution
- discuss RMS amplitude error
- illustrate multiphase interpolation beamforming
- generate basis phases
- add modulation phase and beam phase
- determine total desired phase shift
- select adjacent phases
- determine weights n1 and n2
- apply weights to SAMP-SCPA

