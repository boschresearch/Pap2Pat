# DESCRIPTION

## TECHNICAL FIELD

- introduce machine learning system for Alzheimer's disease prediction

## BACKGROUND

- motivate Alzheimer's disease diagnosis
- limitations of current diagnosis methods
- potential of retinal fundus images for diagnosis

## SUMMARY

- introduce machine learning system for Alzheimer's disease prediction
- describe system components
- describe trained machine learning model
- describe multi-stage pipeline architecture
- describe image quality selector model
- describe vessel map generator model
- describe Alzheimer's disease classifier model
- describe saliency map generator
- describe method for predicting Alzheimer's disease
- describe computer instructions for machine learning model
- describe multiple embodiments of machine learning model

## DETAILED DESCRIPTION

- introduce machine learning system for Alzheimer's disease prediction
- describe system components and functionality
- define terminology used in the specification
- describe relative terms used to describe element relationships
- define "memory" and "memory device"
- define "processor"
- describe system 100 and its components
- describe machine learning model(s) 120 functionality
- describe image acquisition system 113 functionality
- describe system 100 training and testing process
- introduce UK Biobank database used for training and testing
- describe advantages of using UK Biobank database
- describe multi-stage pipeline architecture of machine learning model(s) 120
- describe advantages of multi-stage pipeline architecture
- describe image quality selection stage 200
- describe vessel map segmentation stage 210
- describe SVM-based classifier stage 220
- describe image quality selection process
- describe selection rate through each step of image quality selection process
- describe examples of sufficient and insufficient fundus image quality
- describe cohort characteristics of extracted groups
- describe control subject matching process
- describe performance evaluation of pipeline architecture
- describe feature selection using T-test
- describe performance improvement with feature selection
- describe blind-test experiments to validate pipeline effectiveness
- describe saliency map generation and interpretation
- describe importance of small vessels in Alzheimer's disease classification
- conclude on the feasibility of using retina vasculature as a biomarker for Alzheimer's disease

### Image Quality Selection

- motivate image quality selection
- embodiment of image quality selector

### Vessel Map Generation

- generate vessel maps using U-net

### Alzheimer's Disease Classification

- classify Alzheimer's disease using SVM

### Attention Maps

- generate attention maps using occlusion tests

### Treatment

- employ machine learning system for prediction
- process fundus image to obtain vessel map
- obtain Alzheimer's disease prediction using classifier model
- optimize treatment based on prediction

