# DESCRIPTION

## STATEMENT OF GOVERNMENT RIGHTS

- acknowledge government support

## BACKGROUND

- motivate DBS and artifact removal

## SUMMARY

- introduce artifact removal system
- describe system components
- outline method for artifact removal

## DETAILED DESCRIPTION OF EXAMPLE EMBODIMENTS

- motivate artifact removal in DBS therapy
- describe limitations of existing methods
- introduce period-based artifact reconstruction and removal method (PARRM)
- describe applications of PARRM

### Computer System

- introduce computer system 100
- describe components of computer system 100
- detail processor 106
- detail memory 104
- detail storage 108
- describe I/O interface 110 and communication interface 112

### Period-Based Artifact Reconstruction and Removal for Deep Brain Stimulation

- motivate need for artifact removal in deep brain stimulation
- introduce Period-Based Artifact Reconstruction and Removal Method (PARRM)
- describe PARRM process: data-driven period finding, artifact estimation, and signal reconstruction
- illustrate PARRM process with flow diagrams and schematics
- detail method for determining stimulation period relative to sampling rate
- describe PARRM filter implementation and design parameters
- show example results of PARRM in removing stimulation artifacts
- compare PARRM to conventional filters in simulated data
- evaluate PARRM performance with varying stimulation parameters

### Comparison of PARRM to Conventional Filters

- compare PARRM to conventional filters in simulated data

### Periodic Estimation of Lost Packets From Deep Brain Stimulation Waveform Data

- introduce packet loss in waveform data
- derive PELP method for estimating packet loss
- apply harmonic regression model to estimate packet loss
- determine optimal size of packet loss
- aggregate run-specific loss sizes

### Experimental Testing of the Period-Based Estimation of the Loss of Packets (PELP)

- describe experimental setup for testing PELP
- simulate stimulation in DBS recordings
- model inaccuracies in period estimation
- perform Monte Carlo simulations to test PELP accuracy
- illustrate results of PELP testing

### Period-Based Estimation of Electrical Stimulation Artifacts in the Presence of Phase Shifts

- introduce problem of estimating electrical stimulation artifacts in presence of phase shifts
- describe limitations of existing methods
- present method 1600 for period-based estimation of electrical stimulation artifacts
- model received waveform data and periodic artifact
- optimize periodic artifact model using harmonic regression
- generate loss function model and optimize to determine neural signal of interest
- evaluate effectiveness of method using graphs and comparisons to DFT-based methods
- define objective function
- describe artifact removal process
- introduce initialization process
- discuss implementation details
- provide general statements on scope and claims

