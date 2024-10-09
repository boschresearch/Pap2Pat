# DESCRIPTION

## SUMMARY

- introduce microphone system
- describe maximum likelihood method for DOA estimation
- explain dictionary of relative transfer functions
- outline signal processor functionality
- describe advantages of proposed scheme
- define posterior probability and prior probability distribution
- explain signal model for received sound signal
- describe log likelihood calculation for dictionary elements
- outline voice activity detector functionality
- describe adaptive covariance smoothing
- explain individualization of dictionary elements
- outline hearing device embodiment
- introduce hearing device
- describe signal processing components
- detail time-frequency representation
- describe detectors for physical environment and user state
- describe classification unit and functionality
- describe use of microphone system
- outline method of operating microphone system
- describe computational complexity reduction
- describe computer-readable medium and computer program
- describe hearing system and auxiliary devices

## Definitions

- define hearing device
- describe components of hearing device
- define hearing system and binaural hearing system

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce hearing devices and microphone system
- outline signal model and assumptions
- derive equations for CPSD matrix and noise covariance matrix
- describe maximum likelihood estimation of RTF vectors
- compute log-likelihood function and ML estimate of dθ
- derive ML estimate of RTF vector
- simplify log-likelihood expression for M=2
- compute output variances of beamformers
- compute log-likelihoods by summing variances and determinant
- illustrate SNR-dependent smoothing coefficients
- describe constrained ML RTF estimators
- compute posterior DOA probabilities
- incorporate additional modalities into ML framework

### Example

- derive maximum a posteriori estimates of dθ

### Example

- motivate use of additional information signal e(n)
- derive prior probability P(dθ) from e(n)
- illustrate scenario with two talkers and a listener
- use eye gaze to resolve left-right confusions
- illustrate distribution function for likely values of eye gaze angle
- qualify likelihood estimate L(θ) with prior information

## Examples of Implementation

- illustrate dictionary of relative transfer functions
- motivate uniform distribution of look vectors
- describe pruning of dictionary elements
- introduce non-uniform prior probability distribution
- discuss reducing computational complexity
- evaluate likelihood function for different dictionary elements
- illustrate two-step procedure for evaluating likelihood function
- describe hearing device with directional microphone system
- illustrate frequency sub-band merging and distribution units
- discuss memory allocation for dictionary elements and weights
- derive MVDR beamformer weights
- implement GSC structure for two-microphone case
- optimize likelihood function for DOA estimation
- outline adaptive covariance matrix smoothing method
- define signal model
- derive target power spectral density
- derive noise spectral power density
- derive inter-microphone cross-spectral covariance matrix
- estimate noisy covariance matrix
- estimate noise covariance matrix
- propose adaptive smoothing scheme
- describe variable time constant covariance estimator

