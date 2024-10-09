# DESCRIPTION

## STATEMENT OF GOVERNMENT RIGHTS

- acknowledge government support

## BACKGROUND

- introduce deep brain stimulation
- motivate artifact removal systems

## SUMMARY

- introduce artifact removal systems
- describe system components
- outline artifact removal process
- describe stimulation period determination
- explain artifact removal using Nadaraya-Watson kernel regression
- summarize method for period-based estimation of electrical stimulation artifacts

## DETAILED DESCRIPTION OF EXAMPLE EMBODIMENTS

- motivate artifact removal in DBS therapy
- describe limitations of existing methods
- introduce period-based artifact reconstruction and removal method (PARRM)
- describe PARRM's advantages over existing methods
- explain PARRM's process for finding true period of stimulation
- describe application of PARRM to remove DBS artifacts
- introduce periodic estimation of lost packets (PELP) method
- describe PELP's application to estimate packet losses in bidirectional recordings

### Computer System

- introduce computer system 100
- describe computer system 100's functionality
- illustrate computer system 100's components
- describe processor 106's functionality
- explain processor 106's execution of instructions
- describe memory 104's functionality
- explain memory 104's storage of instructions and data
- describe storage 108's functionality
- explain storage 108's mass storage capabilities
- describe I/O interface 110's functionality
- explain communication interface 112's functionality
- describe bus's functionality in communicatively coupling components

### Period-Based Artifact Reconstruction and Removal for Deep Brain Stimulation

- motivate closed-loop electrical neuromodulation therapies
- introduce challenges in biomarker identification and adaptive neurostimulation system development
- describe limitations of existing stimulation artifact removal methods
- introduce Period-Based Artifact Reconstruction and Removal Method (PARRM)
- illustrate PARRM in FIG. 2
- describe example design of PARRM
- illustrate PARRM process in FIGS. 3-5
- describe method 300 of deep brain stimulation artifact identification and removal
- determine stimulation period relative to sampling rate
- identify stimulation artifact in waveform data
- remove stimulation artifact from waveform data
- describe method 400 of determining stimulation period
- select candidate period
- estimate waveform template with candidate period
- quantify deviation from estimated template
- identify final estimate of period
- illustrate stimulation period determination, artifact reconstruction, and artifact removal in FIG. 5
- compare PARRM to conventional filters in FIG. 6
- evaluate filter performance in FIGS. 7-8

### Comparison of PARRM to Conventional Filters

- compare PARRM to conventional filters in computer simulations
- evaluate filter performance based on time domain relative root mean squared error (RRMSE)
- perform parameter sweep to test effect of varying chirp length, amplitude, pulse width, and frequency on PARRM performance

### Periodic Estimation of Lost Packets From Deep Brain Stimulation Waveform Data

- introduce packet loss in waveform data
- describe packet loss estimation method (PELP)
- determine locations of packet losses and their sizes
- divide time series into continuous runs
- determine period of stimulation for each run
- fit harmonic regression model to longest run
- determine optimal size of packet loss
- apply harmonic regression model to other runs
- aggregate run-specific loss sizes
- illustrate PELP method

### Experimental Testing of the Period-Based Estimation of the Loss of Packets (PELP)

- describe experimental setup
- record EEG and LFP data
- simulate stimulation in DBS recordings
- model stimulation artifacts
- illustrate fitting of stimulation model to waveform data
- vary parameters in stimulation model
- perform Monte Carlo simulations
- illustrate results of stimulation model
- show accuracy of PELP estimates
- illustrate LFP data with packet losses
- discuss applicability of PELP

### Period-Based Estimation of Electrical Stimulation Artifacts in the Presence of Phase Shifts

- introduce problem of estimating electrical stimulation artifacts
- motivate need for systems and methods to address phase shifts
- describe limitations of existing methods
- introduce method 1600 for period-based estimation of electrical stimulation artifacts
- receive waveform data caused by deep neural stimulation
- model received waveform data
- generate initial estimates for periodic artifact and phase shifts
- optimize periodic artifact model using harmonic regression
- generate loss function model
- optimize loss function model to estimate periodic artifact and phase shifts
- remove periodic artifact from received waveform data
- illustrate effectiveness of method using graphs
- compare method with DFT-based frequency detection method
- describe iterative periodic artifact removal methods and systems
- outline initialization process for finding initial estimates of frequency and phase shifts
- define objective function
- model recovered signal
- describe harmonic regression
- minimize objective function
- compute gradient of objective function
- solve optimization problem
- describe initialization process
- define Fourier transform
- maximize energy of observed signal
- describe computer-readable non-transitory storage medium

