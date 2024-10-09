# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate super-resolution

## SUMMARY OF THE INVENTION

- introduce dynamic super-resolution
- summarize invention's advantages

## BRIEF DESCRIPTION OF THE FIGURES

- describe figures

## DETAILED DESCRIPTION OF THE INVENTION

- introduce image processing problem
- derive dynamic super-resolution method
- describe Kalman filter framework
- apply method to color super-resolution
- motivate diagonal matrix assumption
- derive simplified Kalman filter equations
- introduce notations for pixel-by-pixel basis
- implement Kalman filter on pixel-by-pixel basis
- outline dynamic shift-and-add process
- introduce offline dynamic super-resolution method
- define matrix A(t) and its relation to measurements
- motivate regularization terms for monochromatic super-resolution
- introduce bilateral-TV regularization term
- describe multiframe demosaicing and color super-resolution problems
- motivate MAP estimation method for color image perception
- define cost function terms for data fidelity and luminance penalty
- define luminance and chrominance penalty terms
- introduce orientation penalty term
- formulate overall cost function
- describe steepest descent optimization
- present experimental results
- explain two-pass fixed-interval smoothing method
- summarize algorithm and variations

