# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate super-resolution
- limitations of previous approaches
- need for improvement

## SUMMARY OF THE INVENTION

- introduce dynamic super-resolution
- describe mean-covariance approach
- application of demosaicing
- summarize advantages

## BRIEF DESCRIPTION OF THE FIGURES

- describe figures

## DETAILED DESCRIPTION OF THE INVENTION

- introduce image enhancement algorithm
- motivate MAP estimation technique
- describe two-step algorithm for translational motion
- define dynamic forward model for super-resolution problem
- derive state-space equations for system
- explain Kalman filter formulation for optimal estimates
- discuss assumptions about system components
- derive alternative model with state vector
- describe application of Kalman filter for optimal pilot fused image
- motivate diagonal matrix assumption
- derive simplified Kalman filter equations
- introduce notations for warp and downsampling matrices
- explain pixel-by-pixel implementation of Kalman filter
- describe update of covariance matrix
- describe update of mean vector
- outline dynamic shift-and-add process
- comment on initialization and propagated arrays
- describe data fusion method
- introduce smoothed dynamic super-resolution method
- outline two-pass algorithm for smoothed data fusion
- define MAP cost function for deblurring and interpolation
- introduce matrix A(t) and its relation to confidence in measurements
- motivate regularization term and its benefits
- discuss various regularization terms for monochromatic super-resolution
- define bilateral-TV regularization term
- formulate overall cost function for optimization
- describe steepest descent optimization method
- introduce color sequences and multiframe demosaicing problem
- explain fundamentals of color demosaicing and super-resolution
- motivate efficient dynamic method for multiframe demosaicing and color super-resolution
- describe two-step process of image fusion and simultaneous deblurring and interpolation
- define data fidelity penalty term and luminance penalty term
- formulate MAP cost function for color super-resolution and multiframe demosaicing
- introduce spatial luminance penalty term
- introduce chrominance penalty term
- introduce orientation penalty term
- define overall cost function
- describe optimization method
- describe experiment on synthetic data
- show results of experiment on synthetic data
- describe experiment on real-world data
- show results of experiment on real-world data
- describe third experiment on raw CFA images
- show results of third experiment
- introduce two-pass fixed-interval smoothing method
- define high-resolution image and covariance updates
- simplify update formulas
- conclude with interpretation of smoothed high-resolution pixel

