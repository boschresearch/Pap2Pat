# DESCRIPTION

## STATEMENT OF GOVERNMENT RIGHTS

- acknowledge government support

## BACKGROUND

- introduce deep brain stimulation
- describe limitations of DBS
- motivate need for artifact removal
- describe challenges in artifact removal
- summarize desire for efficient artifact removal

## SUMMARY

- introduce systems and methods for artifact removal
- describe initial guess for artifact period
- determine true period for artifacts
- remove artifacts based on true period
- introduce system for stimulation period-based artifact removal
- receive waveform data from iEEG device
- determine stimulation period relative to sampling rate
- identify stimulation artifact using Nadaraya-Watson kernel regression
- subtract identified artifact from waveform data
- generate filtered waveform data
- introduce method for period-based estimation of electrical stimulation artifacts
- describe packet loss estimation method

## DETAILED DESCRIPTION OF EXAMPLE EMBODIMENTS

- motivate artifact removal in DBS therapy
- describe limitations of existing methods
- introduce period-based artifact reconstruction and removal method (PARRM)
- describe PARRM's ability to remove high frequency DBS artifact
- discuss importance of concurrent sensing and stimulation
- describe challenges of artifact removal in low sampling rate recordings
- introduce periodic estimation of lost packets (PELP)
- describe PELP's ability to estimate packet losses in bidirectional recordings
- discuss importance of accurate packet loss estimation
- describe experimental results demonstrating PELP's effectiveness
- discuss applicability of PELP to other stimulating devices
- describe advantages of PELP over existing methods
- discuss potential applications of PELP in biomarker discovery
- describe use of PELP in ecologically valid environments
- discuss importance of streaming intracranial electrophysiology data
- describe limitations of existing data streaming methods
- introduce PELP as a solution to data streaming limitations

### Computer System

- introduce computer system 100
- describe computer system 100's functionality
- discuss computer system 100's physical form
- describe processor 106
- discuss processor 106's functionality
- introduce memory 104
- describe memory 104's functionality
- discuss storage 108
- describe storage 108's functionality
- introduce I/O interface 110
- describe I/O interface 110's functionality
- discuss communication interface 112
- describe communication interface 112's functionality
- introduce network 114
- describe network 114's functionality
- discuss bus
- describe bus's functionality
- introduce processor 106's internal components
- describe processor 106's instruction execution
- discuss memory 104's types
- describe storage 108's types
- introduce I/O devices
- describe I/O interface 110's functionality with I/O devices
- discuss communication interface 112's functionality with networks
- describe bus's functionality with computer system 100's components

### Period-Based Artifact Reconstruction and Removal for Deep Brain Stimulation

- motivate closed-loop electrical neuromodulation therapies
- introduce challenges in biomarker identification and development
- describe limitations of existing implantable DBS and SCS devices
- motivate need for stimulation artifact removal
- introduce Period-Based Artifact Reconstruction and Removal Method (PARRM)
- describe PARRM's superior performance to existing filters
- illustrate PARRM's application in deep brain stimulation
- describe PARRM's ability to recover obscured biomarkers
- illustrate PARRM's online biomarker detection capability
- describe various frequencies of deep brain stimulation
- illustrate control policy for closed-loop DBS
- describe PARRM's artifact estimation process
- introduce data-driven method for determining stimulation period
- illustrate PARRM's implementation as a linear filter
- describe design parameters for PARRM filter
- illustrate trade-offs in choosing design parameters
- describe method 300 of deep brain stimulation artifact identification and removal
- apply deep brain stimulation at patient-specific area of interest
- receive waveform data caused by deep brain stimulation
- determine stimulation period relative to sampling rate
- identify stimulation artifact in waveform data
- remove stimulation artifact from waveform data
- describe method 400 of determining stimulation period
- select candidate period
- estimate waveform template with candidate period
- quantify deviation from estimated template
- identify final estimate of period
- describe operations for method 400
- illustrate stimulation period determination
- illustrate stimulation artifact reconstruction
- illustrate stimulation artifact removal
- compare PARRM to conventional filters
- illustrate recovery of sinusoidal signals
- quantify filter performance
- compare PARRM to conventional filters in simulated data
- evaluate filter performance based on time domain RRMSE
- perform parameter sweep to test PARRM performance
- conclude PARRM's effectiveness in removing stimulation artifacts

### Comparison of PARRM to Conventional Filters

- compare PARRM to conventional filters in simulated data
- illustrate averaged time-voltage series
- illustrate windowed power spectral density
- evaluate filter performance based on time domain RRMSE
- perform parameter sweep to test PARRM performance
- conclude PARRM's effectiveness in removing stimulation artifacts

### Periodic Estimation of Lost Packets From Deep Brain Stimulation Waveform Data

- introduce packet loss in waveform data
- describe packet loss estimation method
- define Periodic Estimation of Lost Packets (PELP)
- illustrate packet loss in waveform data
- describe method 900 of PELP
- receive waveform data in real-time
- determine packet loss locations and sizes
- divide time series into continuous runs
- determine period of stimulation for each run
- fit harmonic regression model to longest run
- determine optimal size of packet loss
- apply harmonic regression model to other runs
- aggregate run-specific loss sizes
- illustrate PELP method
- describe experimental testing of PELP
- record neural data from participant
- simulate stimulation in DBS recordings
- model inaccuracies in period estimation
- perform Monte Carlo simulations
- illustrate results of stimulation model experiments

### Experimental Testing of the Period-Based Estimation of the Loss of Packets (PELP)

- describe experimental testing of PELP
- record neural data from participant
- simulate stimulation in DBS recordings
- model inaccuracies in period estimation
- perform Monte Carlo simulations
- illustrate results of stimulation model experiments
- show sinograms of stimulation model fitting
- vary amplitude ratio in stimulation model
- vary amplitude variability in stimulation model
- vary drift in stimulation model
- perform three sets of experiments
- simulate accuracy of loss estimation
- show graphs of stimulation model results
- illustrate features of Monte Carlo simulation
- show histograms of simulation results
- show heat maps of accuracy vs uncertainty
- discuss effects of amplitude ratio on accuracy
- discuss effects of amplitude variability on accuracy
- discuss effects of drift on accuracy
- show LFP data with packet losses
- estimate losses using PELP
- discuss applicability of PELP to other devices
- discuss limitations and potential extensions of PELP

### Period-Based Estimation of Electrical Stimulation Artifacts in the Presence of Phase Shifts

- introduce period-based estimation of electrical stimulation artifacts
- limitations of estimation due to phase shifts
- describe systems and methods for period-based estimation
- estimate multiple phase shifts simultaneously with stimulation artifacts
- estimate stimulation period of artifacts simultaneously with phase shifts
- introduce method 1600 for period-based estimation
- receive waveform data caused by deep neural stimulation
- characterize waveform data by multiple runs
- model waveform data with periodic artifacts and phase shifts
- generate initial estimates for periodic artifact and phase shifts
- define objective of method 1600
- reconstruct and remove periodic artifact from waveform data
- define loss function for reconstructing and removing artifact
- optimize periodic artifact model using harmonic regression
- model periodic artifact using parametric equation
- generate loss model based on waveform data and periodic artifact model
- compare with PELP method
- optimize loss function model to determine neural signal of interest
- simultaneously estimate multiple phase shifts
- illustrate effectiveness of method 1600
- show relative error of frequency plotted over relative RMSE
- discuss limitations of DFT-based methods
- compare frequency estimation using DFT-based method and method 1600
- introduce iterative periodic artifact removal methods and systems
- describe artifact removal process
- define model for waveform data
- assume energy of artifact is larger than energy of brain
- assume uniformly spaced sample times
- use harmonic regression for removing artifact
- define optimization problem for artifact removal
- define objective function g
- model recovered signal
- define a(t|ω, δi, α0, αk, βk, {circumflex over (K)})
- describe harmonic regression
- minimize α0
- compute g(ω, δi,..., δn)
- set gradient to zero
- solve linear system
- describe Newton's descent method
- analyze numerical complexity
- describe initialization process
- define Fourier transform F
- define energy E
- solve optimization problem
- describe modified Newton's ascent method
- approximate integrals
- describe periodic artifact removal process
- describe computer-readable non-transitory storage medium
- define "or" and "and"
- describe scope of disclosure

