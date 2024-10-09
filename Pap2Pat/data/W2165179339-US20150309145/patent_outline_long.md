# DESCRIPTION

## BACKGROUND

- introduce MRI
- explain magnetic field and spin alignment
- describe radio-frequency magnetic field and emitted radiation
- introduce magnetic field gradients and spatial encoding
- describe MRI system components
- explain k-space data and Fourier transform
- introduce MRE and motion encoding gradients
- describe limitations of conventional MRE
- motivate need for improved MRE method
- summarize current challenges

## SUMMARY

- introduce SLIM-MRE method
- describe simultaneous encoding of three spatial components
- explain time discretization intervals and modulation
- summarize advantages of SLIM-MRE
- describe method for calculating mechanical property
- explain simultaneous acquisition and storage of 3D displacement data
- describe aspect of using different time discretization intervals
- describe aspect of storing components in same k-space
- summarize various aspects of example embodiments

## DETAILED DESCRIPTION

### 1. Overview

- derive analytical formulation of SLIM-MRE
- introduce MRE equation
- describe encoding of displacement in MR signal phase
- specify temporal resolution
- illustrate MEG start times
- describe discretization of MRE equation
- decompose individual components
- visualize MEG start times
- describe demonstration configuration
- compare SLIM-MRE with conventional MRE
- discuss wave images
- analyze wave amplitude
- discuss LFE-derived wave length
- compare wave images
- summarize SLIM-MRE advantages

### 2. Example Method

- introduce example embodiment of SLIM-MRE
- describe MRI system components
- apply MR signal to object
- induce mechanical vibration
- encode vibrational motion in MR signal phase
- acquire MRE data simultaneously
- generate magnetic resonance elastogram
- calculate mechanical property
- separate shear from compression wave
- encode displacement in each dimension
- acquire state of vibration with different sampling frequency
- apply MEG in each dimension
- determine start time of MEG application interval
- encode MR signal phase with vibrational displacement
- express encoded MR signal phase analytically
- derive expression from basic MRE equation
- specify sampling interval
- express MEG start time
- apply discrete Fourier transform
- decompose individual components

### 3. Example Analytical Description

- introduce MRE methods
- define basic equation of MRE
- reformulate equation with start time of MEG
- express harmonic vibration with amplitude and phase
- define magnetic field gradients with zero moment
- relate MEG duration to MEG periods
- derive general solution of integral equation
- consider case of sinusoidal MEGs with zero phase
- establish MR phase as harmonic oscillation
- calculate initial phase and amplitude of vibration
- discuss application of alternate forms of MEGs
- read MR phase in discrete steps for temporal resolution
- determine Fourier transform of real-valued displacement
- discuss conventional MRE approach
- introduce SLIM-MRE approach
- adapt MR phase to function of three variables
- solve for direction-specific MEG amplitudes
- modulate sampling intervals for phase shift of MEG
- discretize MR phase with respect to three directions
- illustrate MEG arrangement with separated samples
- relate modulation of sample interval to encoding
- discuss acquisition of eight samples for decomposition
- establish periodicity relation for minimizing echo time

### 4. Example Operation and Results

- introduce example embodiment of SLIM-MRE
- describe demonstration system and procedure
- specify experimental setup
- describe test object composition
- explain vibration device and mechanical actuation
- show vibration device and test tube in FIG. 5
- describe sample preparation
- specify image acquisition parameters
- explain MEG onsets and periodicity
- show MEG onsets in FIG. 8
- describe SLIM-MRE acquisition and processing
- compare SLIM-MRE with conventional MRE
- show complex wave images in FIG. 6
- describe wave amplitude variation
- show elastograms in FIG. 7
- compare stiffness values between SLIM-MRE and conventional MRE
- discuss advantages of SLIM-MRE
- explain susceptibility to image mis-registration artifacts
- discuss results of applying SLIM-MRE
- compare wave images and stiffness values
- discuss refraction of shear waves
- explain LFE technique and wavelength estimation
- discuss standard deviation of stiffness
- discuss concomitant field terms and correction
- explain extension of SLIM-MRE to more directions
- discuss applicability to different sequence types
- explain difference in MEG start times between SLIM-MRE and conventional MRE
- discuss TE-prolongation and reduction strategies
- explain symmetry of phase integral and TE reduction
- discuss TE-prolongation in high field scanners
- discuss compensation for decreased signal to phase ratio
- explain multidirectional data acquisition without TE increase
- discuss direction-dependent MEG start phase
- compare SLIM-MRE and conventional MRE on inhomogeneous gel sample
- conclude example embodiment of SLIM-MRE

