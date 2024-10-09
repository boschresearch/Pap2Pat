# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate super-resolution
- limitations of imaging devices
- early works on super-resolution
- limitations of static super-resolution
- limitations of dynamic super-resolution
- need for improvements

## SUMMARY OF THE INVENTION

- introduce dynamic super-resolution
- motivate mean-covariance approach
- decompose problem into two disjoint pieces
- address super-resolution and demosaicing jointly
- provide dynamic super-resolution algorithm
- improve visual quality and efficiency
- introduce advanced priors
- provide non-causal processing mode
- summarize key advantages

## BRIEF DESCRIPTION OF THE FIGURES

- describe FIG. 1
- describe FIG. 2
- describe subsequent figures

## DETAILED DESCRIPTION OF THE INVENTION

- introduce image processing problem
- motivate MAP estimation technique
- describe hybrid method of dynamic super-resolution and multiframe demosaicing
- justify two-step algorithm for translational motion and common space-invariant motion
- describe Kalman filter framework for fusing low-resolution images
- explain penalty terms for deblurring and interpolating missing values
- define general linear dynamic forward model for super-resolution problem
- describe state-space equations for forward model
- explain underscore notation for vector derived from image
- describe system noise and its covariance matrix
- explain camera's point spread function and downsampling operation
- describe noise vector and its covariance matrix
- assume knowledge of various components of the current invention
- derive alternative model with state vector
- decompose solution into subtasks of fusing images and deblurring/interpolation
- explain application of Kalman filter to estimate optimal pilot fused image
- describe limitations of Kalman filter for superresolved image
- summarize current invention's method for video-to-video dynamic super-resolution
- motivate diagonal matrices
- derive diagonality of matrices
- introduce simplifications
- define warp matrix
- define downsampling and upsampling operators
- illustrate matrix operations
- introduce notations
- implement Kalman filter equations
- simplify propagated covariance matrix
- update mean vector
- describe update process
- outline algorithm
- comment on initialization
- discuss propagated arrays
- describe data fusion method
- discuss recursive estimation algorithm
- introduce smoothing operation
- describe offline dynamic super-resolution method
- outline smoothed data fusion method
- discuss forward-backward algorithm
- improve high-resolution estimates
- obtain smoothed mean-covariance pairs
- discuss computationally efficient methods
- define MAP cost function
- define desired solution
- introduce matrix A(t) and its relation to confidence in measurements
- define regularization parameter λ and regularization cost function Γ(X)
- motivate Tikhonov total variation (TV) and bilateral-total variation (BTV) regularization terms
- define BTV regularization term ΓBTV(X(t))
- introduce overall cost function as summation of data fidelity penalty term and regularization penalty term
- describe steepest descent optimization to minimize cost function
- introduce color sequences handling in two-step process of image fusion and simultaneous deblurring and interpolation
- describe fundamentals of multiframe demosaicing and color super-resolution problems
- introduce method of current invention for optimal reconstruction of superresolved color images
- describe color image representation and color filter array (CFA)
- illustrate fusion of low-resolution images with relative translational motion
- describe limitations of single-frame demosaicing methods
- introduce multiframe demosaicing and its challenges
- describe color super-resolution problem and its limitations
- motivate efficient dynamic method for multiframe demosaicing and color super-resolution
- describe two-step process of image fusion and simultaneous deblurring and interpolation
- illustrate overall block diagram of dynamic super-resolution process
- define data fidelity penalty term J0(X(t))
- describe luminance penalty term J1(X(t))
- define luminance image XL(t) and luminance regularization term
- describe application of bilateral-TV regularization to luminance component
- introduce chrominance penalty term J2(X(t))
- describe chrominance regularization term
- introduce spatial smoothness term J3(X(t))
- describe overall cost function ε(X(t))
- introduce spatial luminance penalty term
- introduce chrominance penalty term
- introduce orientation penalty term
- define overall cost function
- describe optimization method
- describe experiment on synthetic data
- show results of experiment on synthetic data
- describe experiment on real-world data
- show results of experiment on real-world data
- describe third experiment
- show results of third experiment
- discuss initialization of deblurring-demosaicing step
- introduce two-pass fixed-interval smoothing method
- define high-resolution image and covariance updates
- compute Kalman smoothed gain matrix
- update mean and covariance
- simplify update formulas
- describe block diagram of update equations
- interpret smoothed high-resolution pixel
- discuss estimation of high-resolution smoothed images
- outline overall procedure using update equations
- discuss applicability to general motion and blur models
- discuss variations in detailed implementation
- discuss scope and spirit of the present invention
- describe first pass of two-pass fixed-interval smoothing method
- describe second pass of two-pass fixed-interval smoothing method
- discuss covariance propagation matrix
- discuss prediction error
- discuss smoothed covariance matrix update
- discuss pixelwise update formulas
- conclude description of the present invention

