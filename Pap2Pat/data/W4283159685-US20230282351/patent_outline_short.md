# DESCRIPTION

## FIELD OF INVENTION

- relate to image processing

## BACKGROUND

- motivate medical imaging

## SUMMARY

- address technical problems of cognitive impairment diagnosis
- provide computer-implemented method of predicting cognitive impairment
- identify image regions in brain images
- determine image metrics for each region
- determine indicator based on image metrics
- obtain reference data for cognitive impairment state
- predict or diagnose cognitive impairment
- provide alternative image regions and metrics
- describe various embodiments of the method
- provide computer program products and tangible media
- summarize embodiments of disclosure
- motivate methods of diagnosing cognitive impairment
- describe image acquisition and processing
- outline computer-implemented method of predicting cognitive impairment
- detail image metrics and regions of interest
- describe alternative embodiments and variations
- outline methods of differentiating between subjects
- describe age normalizing and image processing
- provide computer program product and reference images

## DETAILED DESCRIPTION

- describe apparatus for predicting or diagnosing cognitive impairment
- outline components of apparatus, including subject image data obtainer, reference data store, and controller

### Morphological Features

- define morphological features, including surface area, volume, and sphericity

### Grey Level Size Zone Matrix Features

- define grey level size zone matrix features, including grey level non-uniformity and large zone emphasis

### Grey Level Co-Occurrence Matrix (GLCM) Features

- define GLCM features, including correlation and informational measures of correlation
- outline additional GLCM features, including auto correlation, difference variance, and sum average

### Neighbourhood Grey Tone Difference Based Features

- define neighbourhood grey tone difference matrix and texture strength
- outline additional neighbourhood grey tone difference based features, including contrast, busyness, complexity, and coarseness

### Grey Level Run Length Matrix (GLRLM) Features

- define GLRLM features

### Fractal Dimension Features

- introduce fractal dimension features

### Spatial Filtering

- describe wavelet-based spatial filtering

## IMPLEMENTATION

- segment image data into regions of interest (ROIs)
- determine features and weights for each ROI

### The Use of Reduced Feature Sets

- compare predictive power of full feature sets with reduced feature sets
- determine effective combinations of features and regions for predicting cognitive impairment

### The Use of Sub-Regions of the Cortex

- introduce sub-regions of the cortex for predicting cognitive impairment
- describe apparatus for visualizing results on brain images
- illustrate visual output of methods with examples
- identify sub-regions of the cortex and corresponding image metrics
- describe predictive power of combining image metrics from different regions
- test hypothesis of reduced feature sets for predicting cognitive impairment
- analyze performance of reduced feature sets using ROC analysis
- describe development of predictors for different data sets and patient groups
- demonstrate robustness of methods using additional data sets and patient groups
- summarize findings and potential applications of methods

