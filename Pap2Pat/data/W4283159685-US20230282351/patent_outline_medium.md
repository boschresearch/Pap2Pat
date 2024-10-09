# DESCRIPTION

## FIELD OF INVENTION

- relate to image processing

## BACKGROUND

- introduce medical imaging techniques
- limitations of structural images

## SUMMARY

- address technical problems
- provide method of predicting cognitive impairment
- identify image regions in brain images
- determine image metrics for each region
- determine indicator based on image metrics
- obtain reference data for cognitive impairment state
- predict or diagnose cognitive impairment
- use alternative image regions
- distinguish between Alzheimer's disease and non-Alzheimer's disease
- distinguish between Alzheimer's disease and prodromal Alzheimer's disease
- use predetermined method to determine indicator
- apply weighting to image metrics
- combine weighted image metrics
- use different image metrics for different regions
- filter image data to determine image metrics
- use fractal dimension maximum value
- use compactness measure
- use correlation measure of grey level co-occurrence matrix
- use run length non-uniformity measure
- provide computer program products and tangible non-transitory computer readable media
- summarize embodiments of disclosure
- motivate cognitive impairment diagnosis
- describe image acquisition
- specify image resolution
- introduce computer-implemented method
- identify image regions
- determine image metrics
- determine indicator
- obtain reference data
- predict or diagnose cognitive impairment
- describe variations of image metrics
- describe age normalizing
- introduce further aspect of disclosure
- describe differentiating between subjects
- describe method of differentiating between MCI and control subjects
- describe method of differentiating between AD and control subjects
- describe normalizing image data
- describe computer program product

## DETAILED DESCRIPTION

- introduce computer implemented method of predicting or diagnosing cognitive impairment
- describe apparatus for segmenting images and determining image metrics
- outline controller functionality for segmenting images and determining features
- define various image metrics and features, including morphological, grey level size zone matrix, grey level co-occurrence matrix, neighbourhood grey tone difference based
- provide examples of specific image metrics and features, such as sphericity, compactness, grey level non-uniformity, correlation, and texture strength

### Morphological Features

- define morphological features, such as surface area, volume, and sphericity

### Grey Level Size Zone Matrix Features

- define grey level size zone matrix and its features, such as grey level non-uniformity and large zone emphasis
- provide examples of grey level size zone matrix features, such as Fszm.glnu and Fszm.lze

### Grey Level Co-Occurrence Matrix (GLCM) Features

- define grey level co-occurrence matrix and its features, such as correlation and informational measures
- provide examples of GLCM features, such as Fcm.corr and Fcm.info.corr.2
- define auto correlation and difference variance of GLCM
- define sum average, sum variance, and entropy measures of GLCM
- provide examples of cluster based measures of GLCM, such as cluster tendency, cluster shade, and cluster prominence

### Neighbourhood Grey Tone Difference Based Features

- define neighbourhood grey tone difference matrix and its features, such as texture strength and contrast
- provide examples of neighbourhood grey tone difference based features, such as Fngt.strength and Fngt.contrast
- define busyness and complexity measures based on neighbourhood grey tone difference matrix
- provide examples of busyness and complexity measures, such as Fngt.busyness and Fngt.complexity

### Grey Level Run Length Matrix (GLRLM) Features

- define GLRLM
- calculate GLRLM measures

### Fractal Dimension Features

- define fractal dimension

### Spatial Filtering

- introduce wavelet transform
- define discrete wavelet transform
- apply wavelet filters

## IMPLEMENTATION

- segment image data into regions of interest (ROIs)
- determine features for each ROI
- store weightings for combining feature scores
- apply weightings to scale feature values and combine for indicator
- compare indicator with reference data for diagnosis

### The Use of Reduced Feature Sets

- determine predictive power of reduced feature sets
- compare full feature sets with incomplete versions
- test reduced feature sets using ROC analysis
- summarize results of reduced feature sets

### The Use of Sub-Regions of the Cortex

- introduce sub-regions of the cortex
- describe apparatus for visual output
- illustrate visual output with FIG. 6, FIG. 7, and FIG. 8
- define sub-regions of the cortex
- describe image metrics for each sub-region
- outline Table 9 with feature/region tuples
- describe predictive power of feature/region tuples
- illustrate ROC analysis with FIG. 9
- test hypothesis with reduced feature sets
- describe Table 10 with feature/region tuples
- test hypothesis with reduced feature sets
- illustrate ROC analysis with FIG. 10
- describe Table 11 with feature/region tuples
- test hypothesis with reduced feature sets
- illustrate ROC analysis with FIG. 11
- describe Table 12 with feature/region tuples
- test hypothesis with reduced feature sets
- illustrate ROC analysis with FIG. 12
- describe further investigation with additional dataset
- describe Table 13 with feature/region tuples
- illustrate ROC analysis with FIG. 13 and FIG. 14

