# DESCRIPTION

## FIELD OF THE INVENTION

- define medical imaging field

## BACKGROUND OF THE INVENTION

- motivate PCD-CT research
- describe typical PCD data processing
- limitations of sequential method

## SUMMARY OF THE INVENTION

- introduce joint estimation method
- describe material decomposition step
- describe simultaneous assessment step
- outline method advantages

## DETAILED DESCRIPTION

- introduce patent application
- describe accompanying Drawings
- explain non-limiting embodiments
- motivate MAP Bayesian estimation
- define Poisson likelihood models
- introduce Markov random field (MRF)
- describe statistical a priori information
- perform computer simulation
- motivate accurate regularization
- describe expected values of linear attenuation coefficients
- introduce Joint Estimation Maximum A Posteriori (JE-MAP)
- describe image reconstruction using prior information
- define characteristic coefficients
- introduce latent variable for tissue type
- define image and projection set
- describe forward projection process
- define photon counts in sinogram
- formulate MAP estimation problem
- define likelihood distribution
- describe Poisson distribution
- define prior distribution
- introduce voxel-based coupled MRF model
- describe geometrical continuity and discontinuity
- define multivariate Gaussian mixture model
- describe statistical relationship between W and Z
- introduce mixing coefficients
- describe conditional probability of wi given zi
- formulate multivariate Gaussian distribution
- motivate optimization
- approximate likelihood function
- initialize image set of characteristic coefficients and tissue types
- describe iterated conditional modes (ICM) algorithm
- terminate ICM algorithm
- approximate Poisson likelihood
- describe transformation between W and V
- summarize JE-MAP algorithm

### III. EXEMPLARY IMPLEMENTATIONS

- introduce exemplary implementation
- describe phantom and scan setup
- illustrate phantom images and graphical data
- perform reconstruction and tissue type classification
- explain material decomposition and image reconstruction methods
- evaluate impact of parameters on image quality
- quantify image noise and spatial resolution
- assess accuracy of CT images and tissue types
- illustrate images for quantitative evaluation

### IV. EVALUATION RESULTS

- illustrate estimated tissue types and monochromatic CT images
- compare noise levels of FBP, PML, and JE-MAP
- show limitations of PML in tissue type identification
- illustrate effect of smaller parameters on JE-MAP images
- illustrate effect of larger parameters on JE-MAP images
- show image results of 100 noise realizations with bias
- show image results of 100 noise realizations with noise of CT images
- show image results of 100 noise realizations with accuracy of tissue type identification
- illustrate bias and standard deviation of CT images and accuracy of tissue type identification

### V. DISCUSSION AND CONCLUSION

- introduce JE-MAP framework for photon-counting x-ray CT
- discuss advantages of JE-MAP over PML and FBP
- discuss potential problems of JE-MAP with current parameter setting
- conclude superiority of JE-MAP in noise-resolution tradeoff and tissue type identification

## APPENDIX

### A. Derivation of Equation (25), (26)

- derive minimization of Kullback-Leibler divergence
- calculate partial derivatives
- obtain equations (25) and (26)

### B. Convexity Proof for Equation (29)

- define Hessian matrix
- calculate Hessian matrix
- prove convexity of cost function
- describe computing device implementation
- discuss computer readable medium

