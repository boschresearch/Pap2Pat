# DESCRIPTION

## FIELD

- relate to medical imaging

## BACKGROUND

- motivate aortic aneurysm diagnosis
- limitations of current diagnosis methods

## SUMMARY

- introduce object of technology
- motivate accurate diagnosis
- describe imaging modalities
- challenges of analyzing CT images
- limitations of current approaches
- introduce fully convolutional networks
- describe dilated convolutions
- motivate reproducibility
- introduce method for segmenting aortic tissues
- describe region of interest extraction
- describe calcification detection
- describe aortic lumen detection

## Definitions

- define server
- define electronic device
- define computer readable storage medium
- define database
- define information
- define indication
- define communication network

## DETAILED DESCRIPTION

- introduce principles of present technology
- describe scope of present technology
- explain examples and conditional language
- describe simplified implementations of present technology
- provide examples of modifications to present technology
- describe equivalents of present technology
- illustrate electronic device 100
- describe components of electronic device 100
- illustrate communication system 200
- describe medical imaging apparatus 210
- describe workstation computer 215
- describe server 230
- describe deep learning models 250
- describe training of deep learning models 250
- describe use of deep learning models 250 for segmentations
- describe DL model 260
- motivate semantic segmentation
- describe ResNet architecture
- explain dilated convolutions
- describe alternative DL models
- describe DL model 270
- describe subtraction unit 285
- describe DL model 280
- describe alternative embodiment of DL models
- describe database 235
- describe labelled training dataset 240
- describe communication network 220
- describe aortic tissue segmentation procedure 300
- illustrate segmented tissues in aorta
- introduce aortic tissue segmentation procedure
- obtain input images
- describe image features
- extract features using first DL model
- segment ROI using first DL model
- extract features using second DL model
- segment lumen using second DL model
- subtract lumen from ROI
- extract features using third DL model
- identify calcified tissue using third DL model
- describe DL model architecture
- describe training procedure
- evaluate model performance
- calculate accuracy metrics
- define accuracy metrics
- present results of accuracy metrics
- illustrate exemplary images of CT-scans
- motivate aorta extraction
- describe lumen segmentation
- describe thrombus and artery wall evaluation
- describe calcification classification
- illustrate method for segmenting aortic tissues
- describe server configuration
- describe method for detecting calcification
- illustrate method for identifying lumen and calcification
- describe feature extraction and prediction
- describe classification of calcifications
- summarize technical effects

### BACKGROUND

- motivate segmentation model
- describe model development
- introduce Resnet-based FCN
- explain fine-tuning process
- define loss functions
- describe training process
- outline model improvements
- state objective of verification protocol

