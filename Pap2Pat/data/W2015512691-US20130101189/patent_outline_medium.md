# DESCRIPTION

## TECHNICAL FIELD

- define image intensity standardization

## BACKGROUND

- motivate intensity standardization
- limitations of prior art methods

## SUMMARY

- introduce STI technique
- compare STI to prior art
- outline objects of the invention

## DETAILED DESCRIPTION

- introduce automated technique for standardization of intensities (STI)
- describe method of image intensity standardization using spatial correspondences and available tissue masks

### Pre-Processing

- pre-process MRI volumes using MINC image processing toolbox

### Intensity Standardization

- compute joint intensity histogram and find intensity mapping function using tissue masks
- refine estimates using available BrainWeb tissue masks and linearly interpolate intensities between 2D points

### Comparison Measures

- introduce four measures to evaluate standardization techniques: KLD, MAE, NMI, and JHDS
- define Kullback-Leibler divergence (KLD) to evaluate histogram matching
- define mean absolute error (MAE) to evaluate spatial intensity correspondence
- define normalized mutual information (NMI) to evaluate information loss
- define joint-histogram diagonal sum (JHDS) to evaluate spatial intensity correspondence
- compare STI to PCT-10 and PCT-1 on E-ADNI dataset
- show qualitative results of standardization techniques on E-ADNI dataset
- present quantitative results of standardization techniques on E-ADNI dataset
- compare STI to PCT-10 and PCT-1 on ADNI dataset
- show qualitative results of standardization techniques on ADNI dataset
- present quantitative results of standardization techniques on ADNI dataset
- discuss limitations of KLD and MAE measures
- discuss advantages of JHDS measure
- perform two-sample t-tests between standardization methods
- discuss results of t-tests
- conclude that STI outperforms PCT-10 and PCT-1

