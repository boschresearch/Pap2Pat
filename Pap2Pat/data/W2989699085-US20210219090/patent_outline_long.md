# DESCRIPTION

## FIELD OF THE INVENTION

- relate to sound calibration

## BACKGROUND OF THE INVENTION

- motivate sound calibration
- describe current methods for RTF estimation
- limitations of current methods
- application of sound calibration
- types of excitation signals
- RTF estimation methods using non-dedicated source signals
- limitations of non-dedicated source signals
- need for automatic and perceptually-transparent RTF estimation
- introduce signal model
- derive dual-channel FFT analysis
- estimate RTF using auto and cross spectra
- limitations of dual-channel FFT analysis
- describe error in estimation
- object of the present invention

## SUMMARY OF THE INVENTION

- introduce method for perceptually-transparent RTF estimation
- describe spectral splitting
- construct filters for left and right loudspeakers
- generate calibration signals
- playback calibration signals
- record playback
- estimate two-channel RTF
- describe method for multiple-channel system
- describe system for transparent RTF estimation
- summarize advantages

## DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS

- propose RTF estimation method
- introduce calibration signals
- describe filter banks
- construct filters for left and right loudspeakers
- generate loudspeaker input signals
- calculate cross-spectrum between signals
- achieve decorrelation between signals
- describe RTF estimation with ideal filters
- define calibration signals for ideal filters
- describe system model for ideal filters
- illustrate system block diagram
- estimate RTFs using measured signals
- define RTFs between measured signals and calibration signals
- estimate RTFs for entire frequency range
- introduce practical (non-ideal) filters
- describe RTF estimation with practical filters
- present solution with practical filters
- define filters Bi(f) for generating calibration signals
- specify pass band and stop band of filters Bi(f)
- define union of all pass bands covering entire frequency range
- replace Bi*(f), Bj(f) with |Bi*(f)Bj(f)| ε in derivation of estimation method
- repeat RTF estimation for more band subsets
- implement filter banks using ½-octave FIR filters
- define center frequencies for two sets of filter banks
- construct filters bi[n] using DFT-based implementation
- calculate filters Bi(f) by applying DFT on bi[n]
- construct GL(f) and GR(f) using filters Bi(f)
- illustrate filter B4(f) from set 1
- illustrate filters GL(f) and GR(f) from set 1
- illustrate |GL*(f)GR(f)| for both sets of filters
- present pointwise minimum of |GL*(f)GR(f)| between both sets
- describe mapping of frequencies for constructing estimated RTFs
- describe experimental system for RTF estimation
- describe input signals used for RTF estimation
- describe method for measuring RTFs
- generate signals y1(f) and y2(f) using measured RTFs and calibration signals
- estimate HL1(f), HL2(f), HR1(f), and HR2(f) using tfestimate function
- estimate ĤL(f) and ĤR(f) for set 1 only
- estimate ĤL(f) and ĤR(f) using both sets
- define frequency-dependent error and total error
- show measured RIR hL[n] for left channel
- show measured RTF for left channel
- illustrate frequency-dependent error for left channel using set 1 only
- illustrate frequency-dependent error for left channel using both sets
- show normalized error averaged in ⅓ octaves for all input signals
- present total estimation error for left channel
- describe listening test for evaluating perceptual-transparency
- describe adaptation of proposed method for multiple-channel system

