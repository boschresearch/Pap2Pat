# DESCRIPTION

## STATEMENT AS TO RIGHTS UNDER FEDERALLY-SPONSORED RESEARCH

- acknowledge government rights

## FIELD OF THE INVENTION

- relate to titanium alloys

## BACKGROUND OF THE INVENTION

- discuss limitations of Ti alloys
- motivate need for new Ti alloy

## SUMMARY OF THE INVENTION

- introduce computational design method
- tailor thermodynamic database
- obtain overall composite
- specify transformation dilatation
- specify β-phase fraction
- determine annealing temperature
- specify annealing temperature
- specify cooling rate
- calculate normalized rate constant

## DETAILED DESCRIPTION OF THE INVENTION

- provide context for invention disclosure

### Definitions

- define terms used in specification
- discuss ordinary meanings of terms
- highlight certain terms
- provide synonyms for terms
- discuss use of examples
- define "a", "an", and "the"
- define "on" and "directly on"
- define "and/or"
- discuss use of "first", "second", etc.
- define "around", "about", and "approximately"

### Overview of the Invention

- motivate Ti alloy design for naval structural applications
- introduce TRIP and toughening
- discuss system design approach
- link processing, structure, properties, and performance
- use mechanistic quantitative models
- enable computational Ti alloy design
- discuss primary method to improve yield strength and fracture toughness
- discuss TRIP and toughening caused by β-to-α′/α″ martensitic transformation
- create thermodynamic database for martensitic transformations
- tailor data for martensitic transformations near room temperature
- establish molar volume database for β, α′, and α″ phases
- predict stable martensitic structure
- explain physical origin of α″ orthorhombicity
- input invariant-plane shear magnitude and dilatation
- model critical driving force for martensitic nucleation
- calculate MSσ
- calibrate MSσ for Ti-1023 alloy
- demonstrate transformation toughening effect
- design near-α TRIP Ti alloy
- predict MSσ(ct) and transformation dilatation
- discuss objectives of present invention
- quantify fracture toughness-yield strength relationship
- discuss use of TRIP and transformation toughening
- illustrate fracture toughness and yield strength of Ti alloys

### IMPLEMENTATIONS AND EXAMPLES OF THE INVENTION

- introduce CALPHAD community
- describe Gibbs energy of pure solid and solid-solution phases
- define standard equation of molar Gibbs energy of pure elements
- express molar enthalpy, entropy, and specific heat
- describe Gibbs energy of a random, substitutional solution
- introduce Redlich-Kister polynomial with Muggianu extrapolation
- explain limitations of thermodynamic optimization
- describe extrapolation to higher-order systems
- introduce martensitic transformations at low temperatures
- describe first-principles calculations of total energies
- introduce density functional theory (DFT)
- describe Hohenberg-Kohn theorems
- explain Kohn-Sham equation
- introduce pseudopotential
- describe virtual crystal approximation (VCA)
- introduce muffin-tin (MT) potential
- describe Korringa-Kohn-Rostoker (KKR) method
- introduce exact muffin-tin orbital (EMTO) method
- describe coherent potential approximation (CPA)
- introduce local self-consistent Green's function (LSGF) method
- describe Quantum Espresso (QE) package
- introduce ultra-soft pseudopotentials (USPP)
- describe VCA implementation in QE
- calculate bcc-hcp energy difference
- generate VCA potentials for Ti—V/Mo/Nb systems
- show total energies of Ti—V/Mo/Nb systems
- describe EMTO-LSGF calculations
- generate slope matrices, shape functions, and supercells
- calculate bcc-hcp and bcc-omega energy differences
- compare with CALPHAD results
- describe relationship between FP and SGTE phase stabilities
- introduce dynamic instabilities of phases
- describe lattice vibrations and phonons
- explain discrepancy between FP and SGTE phase stabilities
- prepare experimental alloys
- describe arc melting and homogenization/solution treatment
- prepare samples for calorimetry and dilatometry
- describe differential scanning calorimetry (DSC)
- measure transformation temperature, enthalpy change, and specific heat
- show heat flow curves of martensitic Ti—V—Al—Fe alloys
- describe thermal cycles of Ti-Nb based alloys
- analyze attenuation of martensite formation and reversion processes
- introduce martensitic transformation
- describe dilatometry measurement
- show dilatometric curves
- explain martensite formation/reversion
- introduce optimization process
- describe pure elements
- derive molar Gibbs energy equation
- explain Cp(T) data of omega-Zr
- determine free parameters and constraints
- solve nonlinear equations
- present results of Gmω−Gmα and Gmβ−Gmω
- describe binary systems
- explain formation temperature of athermal ω phase
- introduce TiGen database
- show Ti—V system
- show Ti—Mo system
- show Ti—Nb system
- show Ti—Ta system
- show Ti—Fe system
- show Ti—Fe phase boundaries
- show Ti—Al, Ti—Sn and Ti—Zr systems
- introduce ternary systems and performance evaluation
- describe Ti—Nb—Al/Sn/Zr systems
- describe Ti—V—Sn system
- show Ti—Nb—Al/Sn/Zr systems
- show Af temperatures of Ti—V—Al—Fe alloys
- describe optimization of G(hcp,Al,V;0) and G(hcp,Al,Fe;0)
- explain reproduction of experimental Af data
- discuss limitations of DSC
- discuss importance of rapid cooling
- explain motivation for dilatometry
- describe application of TiGen database
- discuss future work on ternary systems
- discuss potential of TiGen database
- explain importance of CALPHAD method
- describe Quantum Espresso and USPP
- explain EMTO-LSGF method
- conclude optimization process
- introduce EMTO-LSGF method
- apply EMTO-LSGF to Ti-V system
- describe martensitic transformation
- introduce invariant-plane strain
- motivate short-range ordering
- describe computational approach
- report lattice parameters of martensites
- analyze α′/α″ transition
- describe X-ray diffraction experiments
- analyze lattice parameters of α″ phases
- model orthorhombicity of α″ phase
- introduce molar volume modeling
- describe BCC phase molar volume modeling
- describe HCP phase molar volume modeling
- describe orthorhombic α″ phase molar volume modeling
- calculate martensitic dilatation
- calculate IPS shear magnitude
- introduce heterogeneous nucleation theory
- describe martensitic nucleation in ferrous systems
- evaluate critical driving forces for Ti alloys
- describe frictional work in solid solutions
- model ΔGcrit of Ti alloys
- describe contributions of Sn and Zr to ΔGcrit
- calculate MS temperatures of Ti-V-Al-Fe alloys
- describe mechanical driving force
- analyze stress-assisted nucleation region
- describe transformation stress
- calculate mechanical driving force for uniaxial tension
- calculate mechanical driving force for crack-tip stress state
- introduce Ti-1023 alloy
- describe β phase stability
- calculate β transus
- discuss annealing effects
- describe MSσ(ut) measurement
- introduce Patel-Cohen model
- calculate transformation stress
- discuss limitations of Patel-Cohen model
- describe fracture toughness measurement
- introduce JIC fracture toughness
- describe heat treatment conditions
- discuss superelasticity
- introduce Example Five
- describe Ti-5111 alloy
- discuss conventional heat treatment
- describe β annealing
- discuss α+β annealing
- describe cooling rates
- discuss final amount of β phase
- introduce DICTRA software
- discuss β→α diffusional transformation
- describe roles of alloying elements
- discuss preventing Ti3Al and grain-boundary α
- describe Ti3Al formation temperature
- discuss grain-boundary α formation
- introduce normalized rate constant
- describe design integration
- introduce objective of design
- describe calculation process
- discuss iterative process
- describe final design composition
- discuss predicted transformation dilatation
- describe Fe—Mo crossplot
- estimate yield strength
- estimate fracture toughness
- discuss TRIP effect
- describe method of computationally designing near-α TRIP Ti alloy
- discuss applications of near-α TRIP Ti alloy
- describe scope of invention
- discuss alternative embodiments
- describe incorporated references
- discuss appended claims

