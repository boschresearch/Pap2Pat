# DESCRIPTION

## BACKGROUND

- introduce visual motion detection
- discuss biological and computer-based approaches

## SUMMARY

- outline motion detection method

## DETAILED DESCRIPTION

- introduce phase information in images
- motivate local phase information for motion detection

### Global Phase of Images.

- define global phase and amplitude of images

### Local Phase of Images

- introduce Short-Time Fourier Transform (STFT) for local phase analysis
- define local amplitude and phase of images
- relate STFT to Gabor receptive fields
- formulate local phase encoding of images
- derive local amplitude and phase equations
- interpret local phase and amplitude
- relate local phase to Gabor receptive fields

### The Global Phase Equation for Translational Motion

- derive global phase equation for translational motion

### The Local Phase Equation for Translational Motion

- derive local phase equation for translational motion
- interpret local phase change for motion detection
- discuss limitations of local phase for motion detection

### The Block Structure for Computing the Local Phase

- define Gaussian windows
- compute 2D Fourier transform of windowed video signal
- evaluate phase and phase change

### The Phase-Based Detector

- provide block FFT based algorithm to detect motion using phase information

### Radon Transform on the Change of Phases

- compute Radon transform of phase derivative
- define Radon transform
- compute correction term due to different length of line integrals
- compute Phase Motion Indicator (PMI)
- define PMI
- compute direction of motion
- define direction of motion
- explain separation of rigid motion from noise
- explain structure of phase change under motion
- explain structure of phase change under noise
- illustrate phase-motion detection algorithm
- illustrate operation of phase-based motion detection algorithm

### Examples of Phase-Based Motion Detection

- illustrate highway video
- illustrate train station video
- illustrate thermal video
- illustrate winterstreet video
- demonstrate motion detection under noisy conditions
- describe motion segmentation
- illustrate motion segmentation results
- discuss computer-implemented operations
- discuss scope and variations of embodiments

