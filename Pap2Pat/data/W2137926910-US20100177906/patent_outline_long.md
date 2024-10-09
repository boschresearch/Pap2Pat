# DESCRIPTION

## CLAIM OF PRIORITY UNDER 35 U.S.C. §119

- claim priority to provisional application

## BACKGROUND

- introduce signal processing
- describe sparse filtering operation

## SUMMARY

- introduce signal reconstruction method
- describe exploiting filter knowledge
- reconstruct signals using samples
- describe apparatus for reconstructing signals
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe apparatus for signal processing
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe apparatus for signal processing
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe computer-program product
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe headset
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe monitor for patient vital signs
- receive DFT coefficients
- compute filter DFT coefficients
- obtain filter impulse response
- reconstruct first signal
- reconstruct second signal
- describe method for signal processing
- sample and transmit DFT coefficients

## DFTAILED DESCRIPTION

- introduce various aspects of the disclosure
- describe the meaning of "exemplary"
- discuss incorporation of teachings into apparatuses
- describe impulse-based wireless communication link

### INTRODUCTION

- introduce two signals linked by unknown filtering operation
- describe distributed setup with sensors sending signal measurements
- relate to Slepian-Wolf problem in distributed source coding
- introduce novel correlation model for distributed signals
- describe two strategies for sampling system design
- establish achievability bounds on number of samples
- introduce concrete distributed sampling and reconstruction scheme

### Signal Model and Problem Statement

- introduce two signals x1(t) and x2(t) with x2(t) as filtered version of x1(t)
- define discrete version of model
- illustrate continuous-time sparse filtering operation and discrete-time counterpart
- sample original continuous signal x1(t) at uniform time interval T
- apply temporal window to obtain finite-length signal
- express discrete Fourier transform of finite sequence x1[n]
- omit windowing effect when N is large enough
- apply procedure to signal x2(t) and use model from equation (1)
- obtain relationship between finite-length signals x1[n] and x2[n]
- assume real-valued delays tk, k=1,..., K close to sampling grid
- represent filter h[n] as sparse vector with K nonzero elements
- define signals of interest as two vectors x1 and x2 linked through circular convolution
- consider problem of sensing xT in a distributed fashion
- illustrate measurement matrices and block-diagonal structure of matrix A

### Bounds on Achievable Sampling Pairs

- illustrate achievable sampling region for universal reconstruction
- define sampling pair (M1,M2) achievable for universal reconstruction
- prove that M1≧N and M2≧N for universal reconstruction
- illustrate achievable sampling pairs for almost sure reconstruction
- define sampling pair (M1,M2) achievable for almost sure reconstruction
- provide achievability bound of number of samples for almost sure reconstruction
- discuss correlation between signals providing saving in almost sure setup
- illustrate achievable bound for sampling pairs
- discuss centralized scenario requiring at least 2N measurements
- conclude that distributed nature of setup does not incur penalty

### Almost Sure Reconstruction Based on Annihilating Filters

- propose distributed sensing algorithm
- introduce frequency-domain representation
- define circular convolution
- outline two main steps of proposed approach
- determine filter h using K+1 DFT coefficients
- send remaining frequency indices among two sensors
- derive DFT coefficients of filter h
- introduce annihilating filter A[m]
- derive matrix form of annihilating filter
- show matrix is of rank K
- compute coefficients of matrix using conjugate symmetry property
- retrieve unknown positions nk
- recover filter weights ck
- describe distributed sensing scheme
- illustrate example operations for processing signals
- illustrate example operations for performing sensing and recovery
- discuss computational efficiency
- discuss robustness to noise and model mismatch

### Possible Extensions

- extend model to piecewise polynomial and piecewise bandlimited filters
- extend model to filters with sparse representation in arbitrary basis
- consider general linear transforms with sparse representation
- analyze multiframe scenario with inter-related sparse filters
- discuss various applications of techniques presented

### Numerical Experiments

- conduct numerical simulations
- divide simulations into three parts
- simulate using synthetic data and additive white Gaussian noise
- apply proposed sensing and recovery algorithm
- estimate acoustic room impulse response (RIR)
- evaluate performance in distributed audio processing application
- assume signal x1 is of length N=256
- assume sparse filter has K=3 or 5 non-zero coefficients
- choose elements of signal x1 and non-zero coefficients of filter randomly
- choose positions of non-zero coefficients of filter uniformly
- add independent white Gaussian noise to filter
- calculate normalized mean square error (MSE)
- illustrate normalized MSE on reconstruction of signals
- observe effect of oversampling on reconstruction performance
- estimate room impulse response in acoustic environment
- generate synthetic room impulse response using image-source model
- set up room dimensions and reflection coefficients
- locate sound source and microphone
- set sampling frequency and speed of sound
- synthesize RIR using fractional delay filters
- build signal x1[n] with i.i.d. elements
- add white Gaussian noise to x1[n]
- convolve noisy x1[n] with RIR
- add noise to x2[n]
- assume first sequence x1[n] is fully available
- estimate RIR using annihilating filter method
- test different oversampling factors
- illustrate original and reconstructed RIRs
- observe effect of oversampling on reconstruction quality
- estimate positions of reflections of originally synthesized RIR
- find closest estimated delay to true delay
- calculate error in position of each matched delay
- average results over 500 trials
- consider signals recorded by two hearing aids
- assume signals are related through a filtering operation
- assume binaural filter has sparsity factor K=1
- set up audio experiment
- record sound by microphones of two hearing aids
- retrieve binaural filter between two hearing aids
- localize sound source using main peak of binaural filter

## APPENDIX A

### The Achievable Bound for Almost Sure Reconstructions

- define spark of a matrix
- show achievability result for almost sure reconstruction
- introduce combinatorial search algorithm
- prove dimension of union of subspaces
- show linear independency of columns
- derive probability of intersection set
- prove one-to-one relationship between measurements and sparse vector
- divide sensing and recovery architecture into two parts
- define matrix M for odd K
- compute consecutive frequency components of h
- reconstruct sparse filter h almost surely
- send complementary subsets of frequency information
- calculate frequency content of other sequence
- show achievability region

## APPENDIX B

### Derivation of the Rank Property

- consider sequence h with K non-zero coefficients
- build Toeplitz matrix H
- write H as product of three matrices
- show rank of H is K

