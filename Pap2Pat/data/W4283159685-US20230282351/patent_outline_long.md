# DESCRIPTION

## FIELD OF INVENTION

- relate to image processing

## BACKGROUND

- introduce medical imaging techniques
- describe structural imaging
- limitations of functional neuroimaging
- variability in human anatomy
- introduce cognitive disorders

## SUMMARY

- address technical problems
- provide method of predicting or diagnosing cognitive impairment
- identify image regions in brain images
- determine image metrics for each region
- determine indicator based on image metrics
- obtain reference data
- predict or diagnose cognitive impairment
- use alternative image regions
- distinguish between Alzheimer's disease and non-Alzheimer's disease subjects
- determine first image metrics
- determine first indicator
- distinguish between subjects
- determine second image metrics
- determine second indicator
- distinguish between subjects
- provide method of distinguishing between Alzheimer's disease and non-Alzheimer's disease subjects
- determine image metrics
- determine indicator
- predict or diagnose cognitive impairment
- provide method of distinguishing between Alzheimer's disease and mild cognitive impairment
- determine image metrics
- determine indicator
- predict or diagnose cognitive impairment
- apply weighting to image metrics
- combine weighted image metrics
- use first set of weights and image metrics
- use second set of weights and image metrics
- determine image metrics for left amygdala
- filter image data
- determine image metrics for left hippocampus
- determine image metrics for left cerebral cortex
- determine image metrics for right hippocampus
- determine image metrics for right cerebral cortex
- determine image metrics for left inferior lateral ventricle
- provide method of predicting or diagnosing cognitive impairment
- identify image regions
- determine image metrics
- determine indicator
- predict or diagnose cognitive impairment
- provide method of predicting or diagnosing cognitive impairment
- provide computer program products
- summarize patent application
- provide computer apparatus
- diagnose cognitive impairment
- select subjects for clinical trials
- classify subjects and identify cohorts
- treat cognitive impairment
- describe image characteristics
- specify image resolution
- list anatomical features
- describe imaging techniques
- predict or diagnose cognitive impairment
- identify image regions
- determine image metrics
- determine indicator
- obtain reference data
- compare indicator with reference data
- specify metrics for entorhinal cortex
- specify metrics for fusiform gyrus
- specify metrics for temporal pole
- specify metrics for transverse temporal cortex
- specify metrics for insula
- specify metrics for lateral occipital lobe
- specify metrics for banks of superior temporal sulcus
- specify metrics for caudal middle frontal cortex
- specify metrics for isthmus cingulate
- specify metrics for rostral middle frontal cortex
- age normalize images
- specify metrics for left inferior parietal lobe
- specify metrics for lateral occipital lobe
- specify metrics for pars triangularis
- specify metrics for rostral middle frontal cortex
- specify metrics for superior temporal lobe
- specify metrics for supramarginal cortex
- specify metrics for temporal pole
- diagnose cognitive impairment using different image regions
- differentiate between subjects with MCI and control subjects
- provide computer program product

## DETAILED DESCRIPTION

- introduce computer implemented method of predicting or diagnosing cognitive impairment
- describe apparatus for segmenting images to identify anatomical features in the brain
- outline components of apparatus, including subject image data obtainer and controller
- describe functionality of controller, including image processing and feature determination
- introduce brain atlas model for segmenting images of the human brain
- list examples of atlases used, including Desikan-Killiany and Destrieux
- describe morphological features, including surface area and volume of regions
- introduce grey level size zone matrix features, including grey level non-uniformity measure
- describe grey level co-occurrence matrix features, including correlation and informational measures
- introduce neighbourhood grey tone difference based features, including texture strength and contrast
- describe additional features, including busyness, complexity, and coarseness measures

### Morphological Features

- define sphericity and compactness measures
- introduce asphericity and spherical disproportion measures

### Grey Level Size Zone Matrix Features

- define grey level non-uniformity measure
- introduce large zone emphasis measure
- describe GLSZM variance measure
- outline additional GLSZM features

### Grey Level Co-Occurrence Matrix (GLCM) Features

- introduce GLCM and its calculation
- define correlation measure
- introduce informational measure of correlation
- describe auto correlation measure
- define GLCM difference variance measure
- introduce sum average measure
- describe sum variance measure
- define entropy measure
- introduce inverse variance measure
- describe cluster based measures, including cluster tendency, shade, and prominence

### Neighbourhood Grey Tone Difference Based Features

- introduce neighbourhood grey tone difference matrix (NGTDM)
- define texture strength measure
- introduce contrast measure
- describe busyness measure
- define complexity measure
- introduce coarseness measure
- outline calculation of NGTDM
- describe neighbourhood size calculation
- define grey level probabilities pi

### Grey Level Run Length Matrix (GLRLM) Features

- define grey level run length matrix
- derive GLRLM measures
- calculate grey level non-uniformity
- calculate run length non-uniformity

### Fractal Dimension Features

- define fractal dimension

### Spatial Filtering

- introduce wavelet based filters
- define continuous wavelet transform
- define discrete wavelet transform
- explain wavelet analysis
- describe perfect reconstruction
- perform one-dimensional wavelet transform
- discuss alternative spatial filters

## IMPLEMENTATION

- segment image data into regions of interest (ROIs)
- determine features for each ROI
- store weightings for each feature
- apply weightings to feature scores
- combine scaled feature values to provide an indicator
- compare indicator value with reference data
- determine cognitive impairment diagnosis
- age normalise image data
- correlate reference data with cognitive testing scores
- estimate or predict cognitive testing score

### The Use of Reduced Feature Sets

- identify most strongly weighted contributions
- determine predictive power of reduced feature sets
- conduct comparative studies
- select and test feature-region tuples
- perform ROC analysis
- summarize ROC data using AUC
- identify effective combinations of features
- conclude on predictive power of reduced feature sets

### The Use of Sub-Regions of the Cortex

- introduce sub-regions of the cortex
- application in cognitive impairment diagnosis
- describe apparatus for visual output
- illustrate visual output in FIG. 6, FIG. 7, and FIG. 8
- define sub-regions of the cortex
- identify sub-regions in image data
- employ image metrics in each sub-region
- use age normalised image data
- describe Table 9
- illustrate ROC analysis in FIG. 9
- test reduced feature set
- describe Table 10
- test reduced feature sets in FIG. 10
- describe Table 11
- test reduced feature sets in FIG. 11
- describe Table 12
- test reduced feature sets in FIG. 12
- summarize consistent findings
- describe further investigation
- develop predictors for control subjects and group ADrp
- describe Table 13
- illustrate ROC analysis in FIG. 13
- test reduced feature sets in FIG. 13
- describe Table 14
- illustrate ROC analysis in FIG. 14
- test reduced feature sets in FIG. 14
- employ methods sequentially
- use methods for stratifying patients
- use methods for assessing treatment effectiveness
- describe reference data store
- describe training data set
- generalize embodiments
- remove or replace features
- describe functional block diagrams
- describe controller functionality
- provide digital logic
- store data and program instructions
- provide tangible storage media
- describe analogue control circuit
- provide technical advantage
- stratify subjects for clinical trials
- process clinical measurement data
- offer new method of physiological measurement

