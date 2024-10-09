# DESCRIPTION

## FIELD OF THE INVENTION

- define medical imaging field

## BACKGROUND OF THE INVENTION

- motivate PCD-CT technology

## SUMMARY OF THE INVENTION

- summarize joint estimation method
- outline method steps

## DETAILED DESCRIPTION

- introduce patent application structure
- describe patent application scope
- motivate image reconstruction method
- introduce MAP Bayesian estimation
- define characteristic coefficients
- introduce tissue type labeling
- define image and projection set
- formulate cost function
- define likelihood distribution
- introduce prior distribution
- define voxel-based coupled MRF model
- define Gaussian mixture model
- formulate statistical relation between W and Z
- introduce optimization method
- approximate likelihood function
- introduce ICM algorithm
- update parameters in ICM
- conclude optimization method

### III. EXEMPLARY IMPLEMENTATIONS

- introduce phantom and scan
- describe reconstruction and tissue type classification
- analyze impact of parameters
- perform quantitative evaluation

### IV. EVALUATION RESULTS

- illustrate evaluation results
- compare noise levels of FBP, PML, and JE-MAP
- show effect of parameter settings on JE-MAP images
- present bias and standard deviation of CT images and accuracy of tissue type identification

### V. DISCUSSION AND CONCLUSION

- discuss advantages of JE-MAP over PML and FBP
- discuss potential problems and future improvements of JE-MAP

## APPENDIX

### A. Derivation of Equation (25), (26)

- derive minimization of Kullback-Leibler divergence

### B. Convexity Proof for Equation (29)

- calculate Hessian matrix
- prove convexity of cost function

