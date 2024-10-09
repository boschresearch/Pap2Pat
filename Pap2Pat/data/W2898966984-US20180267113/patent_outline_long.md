# DESCRIPTION

## FIELD OF THE INVENTION

- define MR sensors

## BACKGROUND

- motivate MR sensors

## SUMMARY

- introduce CDS for MR sensors
- introduce modulation of magnetic field
- describe MR sensor arrays
- introduce multiplexing and demultiplexing
- describe per-sensor switch
- summarize advantages
- describe applications
- mention variations

## DETAILED DESCRIPTION

### A) Introduction

- introduce molecular diagnostics
- motivate high sensitivity sensing technologies
- describe limitations of conventional optical techniques
- introduce magnetoresistive sensors
- describe MR sensor operation
- show examples of biomarker detection
- discuss noise sources in MR sensors
- motivate frequency division multiplexing

### B) General Principles

- introduce exemplary embodiment of invention
- define magnetic field source
- define magnetoresistive sensors
- define electrical circuitry
- describe sampling of electrical signals
- describe measurement output
- define baseline signal
- describe noise reduction
- discuss modulation waveforms
- describe relation between sampling rate and modulation frequency
- introduce baseline suppressors
- discuss temperature compensation
- introduce bias circuitry
- describe sampling of electrical signals with bias
- describe temperature-corrected measurement
- describe magnetoresistive sensors in magnetic field

### C) Correlated Double Sampling (CDS)

- introduce CDS technique
- explain operation principle of CDS
- describe FIG. 4A
- describe FIG. 4B
- motivate CDS for magnetoresistive sensors
- describe conventional MR sensor and sandwich assay technique
- explain response of MR sensor to modulated magnetic field
- describe temporal difference between two measurements
- explain subtraction of two measured data
- describe resulting signal with reduced 1/f noise and offset
- introduce temperature correction
- explain temperature coefficient of resistance (TCR) and magnetoresistance (TCMR)
- describe need for temperature correction treatment
- introduce FIG. 5
- describe data acquisition system with CDS and TC techniques
- explain baseline suppressor
- describe output of baseline suppressor
- introduce correlated double sampling technique for 1/f noise and offset-reduced baseline signal
- describe FIG. 6A
- introduce correlated double sampling technique for 1/f noise and offset-reduced MR signal detection
- describe FIG. 6B
- explain virtues of correlated double sampling approach
- introduce new temperature correction algorithm
- define terms for temperature correction algorithm
- derive temperature correction equations
- describe resulting temperature insensitive magnetoresistive voltage output

### E) Experimental Work

- show experimental results of correlated double sampling
- demonstrate CDS effect on 1/f noise
- show experimental results of temperature correction technique
- demonstrate response of nominal resistance to temperature change
- demonstrate response of magnetic resistance
- show response of magnetic resistance with CDS
- demonstrate measured and corrected ΔMR ratio
- show results from a binding experiment using magnetic nanoparticles
- show SEM images of sensors with particle coverage
- confirm functionality of CDS and TC techniques
- compare results to earlier double modulation work
- discuss limitations of spectral analysis
- highlight importance of fast readout performance

### F) Low Noise MR Sensor Array Architecture

- introduce conventional MR sensor arrays
- discuss limitations of scaling up conventional arrays
- propose new MR sensor array architecture
- describe use of analog multiplexer and demultiplexer
- explain row and column selection inputs
- highlight benefits of Mux and deMux
- introduce switch S for each pixel
- demonstrate noise rejection with turned-off switches
- show simulation results of transimpedance amplifier

