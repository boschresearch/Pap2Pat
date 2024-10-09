# DESCRIPTION

## BACKGROUND

- introduce information processing system
- motivate visual motion detection
- describe biological motion detection
- limitations of computer-based motion detection
- summarize existing biological models

## SUMMARY

- outline method for motion detection
- describe system and computer readable medium

## DETAILED DESCRIPTION

- introduce phase information in images
- motivate local phase information for motion detection
- define global and local phase of images
- discuss amplitude and phase representation of images

### Global Phase of Images.

- define global phase of images

### Local Phase of Images

- introduce Short-Time Fourier Transform (STFT)
- define local amplitude and phase of images
- relate STFT to Gabor receptive fields
- discuss reconstruction of images from local phase
- formulate local phase encoding of images
- define basis functions of Reproducing Kernel Hilbert Space
- represent bank of Gabor receptive fields
- compute responses of Gabor receptive fields
- extract local amplitude and phase information
- formulate reconstruction algorithm from local phase
- discuss orthogonality of image to space spanned by functions
- provide example of reconstruction from local phase
- discuss necessary condition for perfect reconstruction
- discuss alternative way to obtain unique reconstruction

### The Global Phase Equation for Translational Motion

- derive global phase equation for translational motion

### The Local Phase Equation for Translational Motion

- discuss local motion detection using STFT
- define local phase of u(x,y,t) using STFT
- relate change in local phase to visual motion
- discuss invariance of local phase to intensity scaling
- derive local phase equation for translational motion
- discuss added term in local phase equation

### The Block Structure for Computing the Local Phase

- define Gaussian windows
- compute 2D Fourier transform of windowed video signal
- evaluate integral using 2D FFT
- process each block independently
- discuss window size and object motion detection
- illustrate block structure with example
- describe de-noising of phase measurements

### The Phase-Based Detector

- provide embodiment of block FFT based algorithm

### Radon Transform on the Change of Phases

- compute Radon transform of phase derivative
- define Radon transform
- discuss linear structure of phase derivative
- compute Radon transform for blocks exhibiting motion
- define correction term
- compute PMI
- discuss PMI computation
- compute direction of motion
- discuss direction of motion computation
- illustrate phase-motion detection algorithm
- describe algorithm implementation
- discuss parallel computing capabilities
- illustrate algorithm operation
- divide algorithm into two parts
- discuss first part of algorithm
- apply Gaussian window
- compute local phase
- employ temporal high-pass filter
- discuss second part of algorithm
- evaluate PMI
- detect motion
- compute direction of motion
- discuss algorithm parallelization
- discuss extension to higher dimensions

### Examples of Phase-Based Motion Detection

- introduce highway video
- illustrate motion detection results
- discuss aperture problem
- introduce low-contrast video
- show motion detection results on low-contrast video
- introduce train station video
- illustrate motion detection results
- introduce thermal video
- show motion detection results on thermal video
- introduce winterstreet video
- illustrate motion detection results
- discuss noise suppression trade-off
- introduce motion segmentation
- discuss block size reduction
- illustrate motion segmentation results
- discuss applicability to various videos
- discuss computer-implemented operations
- discuss scope of disclosure

