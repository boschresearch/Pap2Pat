# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- acknowledge government support

## FIELD

- define field of disclosure

## BACKGROUND

- introduce Monte Carlo simulation
- describe limitations of phase space files
- motivate virtual source models

## SUMMARY

- introduce fast Monte Carlo dose calculation
- receive CT images and planned dose images
- process images to same spatial resolution
- convert image intensity to density
- process radiotherapy plans
- build virtual source model
- receive phase-space information
- calculate particle positions
- calculate Gaussian means and standard deviations
- determine particle source criteria
- calculate particle source probabilities
- calculate particle species probabilities
- bin position probability information
- bin direction cosine probability information
- bin kinetic energy probability information
- convert to cumulative probability densities
- invert cumulative probability densities
- simulate and transport external beams

## DETAILED DESCRIPTION

- introduce CT scanner system diagram
- describe CT scanner components
- introduce computing environment components
- describe processing component functions
- introduce processor and GPU components
- describe memory and storage components
- introduce ASICs, DSPs, and PLDs components
- describe fast MC dose calculation software
- introduce treatment head diagram
- describe treatment head components
- introduce phase space files
- describe moveable jaws and MLC leaves
- introduce flow chart of method 3000
- receive 3D CT images
- receive 3D planned dose and segmentation contour images
- process images to have same spatial resolution and matrix size
- resample images to match CT matrix size and field of view
- normalize image intensity
- convert image HU voxels to densities
- parse and convert radiotherapy plans
- build VSM using inverse CDF tables
- receive PSF containing phase-space information
- parse PSF and calculate particle probabilities
- determine particle source criteria
- calculate particle source probabilities
- calculate particle species probabilities
- bin particle inplane positions into histograms
- bin particle crossplane positions into histograms
- bin particle inplane direction cosines into histograms
- bin particle crossplane direction cosines into histograms
- bin particle kinetic energy into histograms
- convert probability densities to cumulative probability densities
- convert cumulative probabilities to inverse CDF tables
- validate VSM using χ2 test
- simulate treatment beams using VSM
- transport particles through virtual treatment machines
- produce 3D images of simulated patient dose
- post-process images to obtain final report
- calculate mean dose for regions
- perform 3D gamma index analysis
- validate fast MC algorithm using clinical cases
- compare VSM MC and planned doses to measured doses
- validate speed of fast MC algorithm
- compare VSM and PSF computation times
- illustrate best- and worst-case scenarios
- conclude VSM provides significant savings in computation time

