# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- acknowledge government support

## FIELD

- define field of disclosure

## BACKGROUND

- describe limitations of Monte Carlo simulations

## SUMMARY

- introduce fast Monte Carlo dose calculation method
- describe computer-implemented method for fast MC dose calculation
- describe apparatus for fast MC dose calculation
- describe non-transitory computer-readable storage medium

## DETAILED DESCRIPTION

- introduce system diagram of CT scanner, controller, and computing environment
- describe components of computing environment
- illustrate example treatment head for medical linear accelerator
- outline steps of method for fast MC dose calculation
- describe processing of 3D images to have same spatial resolution and matrix size
- convert image HU voxels to densities using IVDT
- parse and convert radiotherapy plans to instructions for simulation
- build VSM using inverse CDF tables for simulation
- simulate treatment beams and transport using VSM to produce 3D images of simulated patient dose
- post-process 3D planned dose, organ segmentation contour, and simulated patient dose images
- validate fast MC algorithm using clinical cases and compare with measured doses

