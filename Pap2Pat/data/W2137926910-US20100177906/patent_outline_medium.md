# DESCRIPTION

## CLAIM OF PRIORITY UNDER 35 U.S.C. §119

- claim priority to provisional application

## BACKGROUND

- introduce signal processing and sparse filtering operation

## SUMMARY

- introduce signal reconstruction method
- describe sparse filtering operation
- describe signal sampling and transmission
- describe signal reconstruction using filter
- describe apparatus for signal processing
- describe method for signal processing
- describe computer-program product for signal processing
- describe headset for signal processing
- describe monitor for patient vital signs
- describe method for signal processing with DFT
- describe apparatus for signal processing with DFT
- describe computer-program product for signal processing with DFT
- describe sensing device for signal processing
- describe method for signal estimating
- describe apparatus for signal estimating
- describe computer-program product for signal estimating
- describe headset for signal estimating
- describe monitor for patient vital signs with signal estimating
- describe method for signal processing with filter matrix
- describe apparatus for signal processing with filter matrix

## DFTAILED DESCRIPTION

- introduce various aspects of the disclosure
- describe the scope of the teachings herein

### INTRODUCTION

- introduce signal model with unknown filtering operation
- describe distributed source coding setup
- introduce novel correlation model for distributed signals

### Signal Model and Problem Statement

- introduce signal model with sparse filtering operation
- describe finite-dimensional discrete version of the model
- derive discrete-time filtering operation
- assume sparse filter h[n] with K nonzero elements
- describe circular convolution of signals x1 and x2
- introduce distributed sensing problem with two independent sensors
- formulate problem of reconstructing signals from observed samples

### Bounds on Achievable Sampling Pairs

- introduce achievable sampling region for universal reconstruction
- prove that M1≧N and M2≧N for universal reconstruction
- introduce almost sure reconstruction with weaker requirement
- derive achievability bound for almost sure reconstruction
- illustrate achievable sampling pairs for almost sure reconstruction

### Almost Sure Reconstruction Based on Annihilating Filters

- propose distributed sensing algorithm
- introduce frequency-domain representation
- derive filter h using annihilating filters
- describe matrix form of annihilating filter
- compute coefficients of annihilating filter
- illustrate distributed sensing scheme
- describe sensing and recovery of signals
- discuss computational efficiency
- discuss robustness to noise and model mismatch

### Possible Extensions

- extend model to piecewise polynomial and piecewise bandlimited filters
- consider general linear transforms with sparse representation

### Numerical Experiments

- conduct numerical simulations
- simulate synthetic data with additive white Gaussian noise
- apply sensing and recovery algorithm to estimate acoustic room impulse response
- evaluate performance in distributed audio processing application
- assume signal x1 has length N=256 and sparse filter has K=3 or 5 non-zero coefficients
- choose elements of signal x1 and non-zero coefficients of filter randomly
- add independent white Gaussian noise to filter to meet desired signal-to-noise ratio
- assume first sensor sends whole signal x1
- calculate normalized mean square error on reconstruction of signals
- illustrate normalized MSE as function of SNR using TLS approach
- observe effect of oversampling on reconstruction performance
- estimate room impulse response in acoustic environment using image-source model
- generate synthetic room impulse response using image-source model
- set up simulation scenario with sound source and microphone
- add noise to signal x1 to simulate imperfections in sending sequences
- convolve noisy version of x1 with RIR and add noise to x2
- reconstruct RIR using annihilating filter method
- illustrate original RIR and reconstructed RIRs for different oversampling factors
- calculate average error in estimating positions of reflections
- illustrate effect of higher oversampling on performance of recovery algorithm

## APPENDIX A

### The Achievable Bound for Almost Sure Reconstructions

- define spark of a matrix
- motivate almost sure reconstruction
- derive combinatorial search algorithm
- prove achievability result for almost sure reconstruction
- describe sensing and recovery architecture
- derive matrix M for odd K
- derive matrix M for even K

## APPENDIX B

### Derivation of the Rank Property

- motivate rank property of Toeplitz matrices
- derive rank property of Toeplitz matrices

