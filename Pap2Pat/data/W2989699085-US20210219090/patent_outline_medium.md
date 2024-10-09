# DESCRIPTION

## FIELD OF THE INVENTION

- relate to sound calibration

## BACKGROUND OF THE INVENTION

- motivate sound calibration
- describe current methods for RTF estimation
- limitations of current methods
- application of RTF estimation
- introduce non-dedicated source signals
- limitations of non-dedicated source signals
- motivate need for automatic RTF estimation

## SUMMARY OF THE INVENTION

- introduce method for perceptually-transparent RTF estimation
- describe steps for RTF estimation
- introduce method for transparent RTF estimation for multiple-channel system
- describe steps for multiple-channel RTF estimation
- introduce system for transparent RTF estimation for multiple-channel system

## DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS

- propose RTF estimation method
- describe calibration signals generation
- define filter banks and filters
- construct filters for left and right loudspeakers
- generate calibration signals using filters
- estimate RTF with ideal filters
- describe system block diagram and processing
- estimate RTF with practical filters
- define filters Bi(f) for generating calibration signals
- specify pass bands and stop bands for filters Bi(f)
- describe implementation using ½-octave FIR filters
- construct filters bi[n] using DFT-based implementation
- calculate filters Bi(f) by applying DFT on bi[n]
- illustrate filter B4(f) from set 1 for ½-octave filters
- illustrate filters GL(f) and GR(f) from set 1 for ½-octave filters
- illustrate |GL*(f)GR(f)| for ½-octave filters with DFT-based implementation
- present pointwise minimum of |GL*(f)GR(f)| between both sets
- describe analysis of RTF estimation using proposed method
- describe experimental system setup
- describe input signals used for analysis
- describe methods for measuring RTFs and estimating RTFs using proposed method
- present results of frequency-dependent error and total error
- describe listening test for evaluating perceptual-transparency of calibration signals

