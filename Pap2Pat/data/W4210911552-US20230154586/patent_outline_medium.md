# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- acknowledge government support

## FIELD

- define field of disclosure

## BACKGROUND

- describe limitations of Monte Carlo simulations

## SUMMARY

- introduce fast Monte Carlo dose calculation method
- describe receiving CT images and radiotherapy plans
- process images and plans
- build virtual source model
- simulate and transport external beams
- post-process images to obtain final report
- describe apparatus for fast Monte Carlo dose calculation
- describe non-transitory computer-readable storage medium
- summarize other aspects and features

## DETAILED DESCRIPTION

- introduce CT scanner system diagram
- describe CT scanner components
- introduce computing environment components
- describe processing component functions
- introduce GPU and memory components
- describe memory storage types
- introduce ASICs, DSPs, and PLDs
- describe fast MC dose calculation software
- introduce treatment head diagram
- describe treatment head components
- introduce flow chart of method 3000
- receive 3D CT images
- receive planned dose and segmentation contour images
- process images to uniform spatial resolution
- convert image HU voxels to densities
- parse radiotherapy plans
- build VSM using inverse CDF tables
- receive PSF and parse particle information
- calculate particle probabilities and build histograms
- convert probability densities to cumulative probabilities
- convert cumulative probabilities to inverse CDF tables
- simulate treatment beams and transport particles
- post-process and compare planned and simulated doses

