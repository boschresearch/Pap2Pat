# DESCRIPTION

## BACKGROUND

- motivate physical attacks

## SUMMARY

- introduce tamper detection method
- describe on-chip circuit-based network analyzers
- application of impedance characterization
- validate via FPGA measurements

## DETAILED DESCRIPTION

- introduce problem of physical attacks on circuit boards
- describe conventional approaches to anti-tamper solutions
- motivate need for anti-tamper schemes with minimal changes to electronic boards
- introduce self-contained sensors for detecting physical anomalies
- describe conventional passive sensing methods
- describe limitations of conventional passive sensing methods
- introduce active sensing methods
- describe time-domain reflectometry (TDR) method
- motivate need for unified approach to detecting tampering
- introduce on-chip circuit-based sensor for monitoring physical integrity
- describe power integrity analysis and its application to physical integrity
- introduce self-contained tamper-evident sensor device
- describe characterization of impedance of power distribution network (PDN)
- explain how tampering attempts change PDN impedance
- describe emulation of network analyzer functionality on FPGAs
- describe electrically stressing PDN with various frequencies
- describe measuring voltage drop for impedance estimation
- show impact of different classes of tampering on PDN impedance
- describe using Wasserstein Distance as a metric
- demonstrate detection of sophisticated tampering and modifications
- describe power delivery on a printed circuit board (PCB)
- introduce impedance model of PDN on a circuit board
- describe storing impedance models as indicators of normal operation
- describe monitoring impedance and detecting changes
- describe comparing impedance models to detect tampering
- introduce FIG. 1, a schematic diagram for modeling PDN response
- describe forming RLC circuit indicative of PDN
- describe characterizing impedance of RLC circuit
- describe tamper detection device and its operation
- describe generating expected impedance signature
- describe determining presence of tampering event
- introduce FIG. 2, an equivalent RLC circuit response
- describe PDN model for a typical PCB
- describe contribution of each component to PDN impedance
- describe frequency response of PDN
- describe primary reason for impedance behavior
- describe generating equivalent RLC circuit from PDN
- describe identifying impedance model from equivalent RLC circuit
- describe detecting tampering based on received inputs
- describe Z- and S-parameters characterizing PDN impedance
- introduce FPGA-based VNA
- describe power wasting circuits
- explain sensing circuit and ADC types
- derive impedance equation using Ohm's law
- convert impedance to Cartesian representation
- approximate impedance magnitude
- estimate ION and IOFF on FPGAs
- relate RO frequency to voltage drop
- calculate impedance magnitude at given frequency
- discuss limitations of sinusoidal wave generation
- introduce statistical analysis of impedance values
- define random variables for impedance measurements
- describe empirical cumulative distribution function
- employ Wasserstein metric for comparing distributions
- discuss Gaussian and non-Gaussian distributions
- outline non-parametric statistical tests for tamper detection

