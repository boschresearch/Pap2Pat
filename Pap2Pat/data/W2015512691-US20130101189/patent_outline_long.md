# DESCRIPTION

## TECHNICAL FIELD

- relate to image intensity standardization

## BACKGROUND

- introduce MRI intensity variation problem
- describe ADNI initiative
- motivate intensity standardization
- limitations of prior art techniques
- describe prior art method flowchart

## SUMMARY

- introduce STI technique
- compare STI to prior art techniques
- describe qualitative results
- describe quantitative results
- introduce object of invention
- describe method embodiments
- describe apparatus and system embodiments

## DETAILED DESCRIPTION

- introduce automated technique for standardization of intensities (STI)
- describe pre-processing of MRI images
- explain intensity standardization using joint intensity histograms and spatial correspondence
- compare STI to other standardization techniques (PCT-10 and PCT-1)
- discuss results and limitations of STI

### Pre-Processing

- correct raw scanner intensity inhomogeneity
- remove noise and scale grey level intensities
- register image to standard image space

### Intensity Standardization

- compute joint intensity histogram for each tissue type
- find maximum in joint histogram for each tissue type
- use maximum as control point in intensity mapping function
- linearly interpolate intensities between control points

### Comparison Measures

- visually inspect standardized images
- compute Kullback-Leibler divergence (KLD) with respect to standard
- compute mean absolute error (MAE) with respect to standard
- compute normalized mutual information (NMI) with respect to input
- compute joint-histogram diagonal sum (JHDS) with respect to standard
- compare STI to PCT-10 and PCT-1 using KLD
- compare STI to PCT-10 and PCT-1 using MAE
- compare STI to PCT-10 and PCT-1 using NMI
- compare STI to PCT-10 and PCT-1 using JHDS
- perform two-sample t-tests between standardization methods
- discuss limitations of KLD and MAE measures
- discuss advantages of JHDS measure
- show qualitative results for E-ADNI dataset
- show quantitative results for E-ADNI dataset
- show qualitative results for ADNI dataset
- show quantitative results for ADNI dataset
- discuss performance of STI on E-ADNI dataset
- discuss performance of STI on ADNI dataset
- compare STI to PCT-10 and PCT-1 on E-ADNI dataset
- compare STI to PCT-10 and PCT-1 on ADNI dataset
- discuss advantages of STI over PCT-10 and PCT-1
- discuss limitations of STI
- show example of intensity histogram after standardization
- show block diagram of apparatus for image intensity standardization
- show block diagram of physical setup of the invention
- show images for one subject at a specific MRI imaging site
- show images for the same subject at another specific MRI imaging site
- show ADNI images sorted according to MAE percentiles
- discuss MAE values for foreground, WM, and GM
- compare MAE values for L4 and STI
- discuss use of fuzzy logic for generating tissue-specific masks
- discuss use of fuzzy logic classification for intensity standardization

