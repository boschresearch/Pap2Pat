# DESCRIPTION

## TECHNICAL FIELD

- define image intensity standardization

## BACKGROUND

- limitations of prior art methods

## SUMMARY

- introduce novel standardization technique

## DETAILED DESCRIPTION

- introduce automated technique for standardization of intensities (STI) in MRI images

### Pre-Processing

- pre-process MRI volumes using MINC image processing toolbox

### Intensity Standardization

- compute joint intensity histogram and find intensity mapping function using tissue masks

### Comparison Measures

- introduce Kullback-Leibler divergence (KLD) for histogram matching
- introduce mean absolute error (MAE) for spatial intensity correspondence
- introduce normalized mutual information (NMI) for information loss
- introduce joint-histogram diagonal sum (JHDS) for spatial intensity correspondence
- compare STI to PCT-10 and PCT-1 using KLD, MAE, NMI, and JHDS
- evaluate performance of STI on E-ADNI dataset
- evaluate performance of STI on ADNI dataset
- discuss limitations of KLD and MAE measures

