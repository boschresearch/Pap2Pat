# DESCRIPTION

## SUMMARY

- introduce microphone system
- describe maximum likelihood method
- explain direction-of-arrival estimation
- introduce dictionary of relative transfer functions
- describe beamforming purposes
- estimate signal-to-noise ratio
- describe microphone system components
- introduce signal processor
- describe database of relative transfer functions
- determine posterior probability
- estimate direction-of-arrival
- describe advantages of proposed method
- introduce portable microphone system
- describe microphone system for hearing devices
- introduce signal model
- describe log likelihood calculation
- introduce adaptive covariance smoothing
- describe voice activity detector
- update inter microphone covariance matrices
- change dictionary size based on input sound level
- select dictionary elements based on calibration signal
- individualize dictionary elements to specific user
- estimate posterior probability in each frequency band
- utilize additional information for direction-of-arrival estimation
- describe hearing device with microphone system
- introduce hearing device
- describe signal path and analysis path
- detail analogue-to-digital conversion
- describe time-frequency representation
- detail signal processing in frequency domain
- describe detectors for physical environment and user state
- detail level detector and voice detector
- describe own voice detector and movement detector
- detail classification unit
- describe additional functionality
- describe use of microphone system
- introduce method of operating microphone system
- detail direction-of-arrival estimation
- describe computational complexity reduction
- detail posterior probability determination
- describe adaptive covariance smoothing
- introduce computer-readable medium
- introduce computer program
- introduce data processing system
- describe hearing system with auxiliary device
- introduce APP for hearing device or system

## Definitions

- define hearing device
- describe hearing device components
- specify hearing device configurations
- explain signal processing circuit
- describe output unit options
- define hearing system and binaural hearing system
- mention scope of applicability

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce hearing devices and microphone system
- outline assumptions and theoretical framework
- define signal model and noisy observation
- describe analysis filterbank and DFT coefficients
- outline independence assumption across time and frequency
- define relative transfer function and target DFT coefficient
- derive inter-microphone cross power spectral density matrix
- model temporal evolution of noise covariance matrix
- summarize covariance matrix of noisy observation
- derive maximum likelihood estimation of RTF vectors
- describe computing log-likelihood efficiently
- introduce ML estimate of RTF vector
- derive efficient computation of log-likelihood
- simplify expression for M=2 case
- compute output variances of beamformers
- compute log-likelihoods
- update CX and CV matrices
- illustrate SNR-dependent smoothing coefficients
- introduce constrained ML RTF estimators
- compute posterior DOA probabilities
- introduce additional modalities
- derive maximum likelihood estimates of dθ
- discuss joint estimation of RTF vectors
- discuss adaptive covariance smoothing
- discuss SNR-dependent smoothing schemes
- illustrate examples of SNR-dependent smoothing coefficients
- conclude efficient computation of log-likelihood

### Example

- derive maximum a posteriori estimates of dθ
- use additional information signal e(n) to determine prior probability P(dθ)

### Example

- illustrate scenario with two talkers and a listener wearing a hearing system
- show how eye gaze may be used to resolve left-right confusions
- illustrate distribution function for likely values of eye gaze angle
- use distribution function to qualify likelihood estimate of directional of arrival
- multiply distribution function and likelihood estimate to give improved likelihood estimate
- influence time constants of covariance matrices using eye gaze and head movement
- make joint direction-of-arrival decision across frequency
- find most likely direction-of-arrival from joint likelihood function
- apply non-uniform prior probability to favor certain directions
- maximize logarithm of posteriori probability
- make joint direction decision across both hearing instruments
- merge likelihood functions estimated at left and right instrument

## Examples of Implementation

- show graphical representations of dictionaries of relative transfer functions
- introduce uniformly distributed look vectors in the horizontal plane
- discuss pruning of dictionary elements
- motivate arccos-scale distribution of dictionary elements
- illustrate distribution of dictionary elements in the frontal half plane
- include "own voice" look vector in the dictionary
- apply non-uniform prior probability to each direction
- estimate own voice look vector during use
- include relative transfer functions measured at different distances
- reduce computational complexity in miniature hearing devices
- down sample to reduce computations
- reduce number of dictionary elements
- reduce number of frequency channels
- remove terms in the likelihood function with low importance
- evaluate likelihood function for different dictionary elements
- estimate reference direction of arrival
- divide calculations between left and right hearing instruments
- evaluate likelihood function sequentially
- apply log likelihood in fewer channels
- illustrate hearing device with directional microphone system
- discuss memory allocation for dictionary elements and weights
- derive MVDR beamformer weights
- implement GSC structure
- estimate adaptive parameter
- recall likelihood function
- obtain stable direction estimate
- illustrate processing flow
- describe adaptive covariance matrix smoothing
- define signal model
- define signal model
- derive target power spectral density
- derive noise spectral power density
- define inter-microphone cross-spectral covariance matrix
- define inter-microphone cross-power spectral density matrix
- estimate noisy input covariance matrix
- estimate noise covariance matrix
- propose adaptive smoothing scheme
- define normalized covariance measure
- calculate fast instance of normalized covariance measure
- calculate instance with variable update rate
- describe variable time constant covariance estimator
- illustrate covariance smoothing unit
- illustrate pre-smoothing unit
- illustrate variable smoothing unit
- describe goal of computation

