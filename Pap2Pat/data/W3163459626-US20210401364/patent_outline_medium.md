# DESCRIPTION

## FIELD OF THE INVENTION

- define OSA classification system

## BACKGROUND

- introduce OSA and its effects
- describe current diagnosis methods
- discuss limitations of current methods
- motivate need for improved OSA screening tool

## SUMMARY OF THE INVENTION

- introduce method for deriving OSA screening tool
- describe obtaining initial dataset
- extract features from audio data
- train classifier using filtered features
- introduce method for performing OSA screening test
- describe system for deriving or operating OSA screening tool

## DETAILED DESCRIPTION

### Systems & Processes

- introduce AWakeOSA algorithm
- describe tracheal breathing sounds recording
- detail audio signal processing
- describe data collection procedure
- motivate silent period recording
- explain breathing cycles recording
- describe data collection for test subjects and patients
- introduce data collection and classifier training procedure
- extract inspiratory and expiratory sounds
- investigate and exclude artifacts
- select breathing phase signals
- add information to datastore
- compute features from breathing sound signals
- filter breathing sound phases
- compute power spectrum and bi-spectrums
- divide subject datasets into two groups
- divide initial dataset into training and blind testing datasets
- identify high-severity and low-severity groups
- subdivide datasets into anthropometrically distinct subsets
- extract features for each subset
- evaluate and select features
- build linear model for AHI
- evaluate and select models
- validate and test models

### Experimental Support

- introduce experiment A
- motivate tracheal breathing sounds analysis
- summarize prior works
- describe experiment A procedure
- illustrate AWakeOSA algorithm
- explain feature extraction and reduction
- report anthropometric parameters
- describe classification results
- analyze feature combinations
- discuss overall classification results
- investigate misclassified subjects
- motivate OSA diagnosis
- limitations of anthropometric measures
- correlation of anthropometric parameters with AHI
- application of breathing sounds analysis
- describe simplified AWakeOSA voting algorithm
- explain subdivision of data into anthropometric subsets
- discuss effect of aging on voice and breathing sounds
- describe selection of anthropometric subsets
- analyze results of simplified AWakeOSA algorithm
- discuss correlation of selected sound features with AHI
- describe experimental setup and data collection
- explain data preprocessing and feature extraction
- discuss training and testing of classifier
- summarize results of Experiment A
- relate to more comprehensive embodiment of Experiment B
- introduce experimental support
- calculate p-value and robustness score
- select features using SVM classifier
- evaluate feature combinations using Random-Forest classifier
- select best feature combinations
- evaluate overall classification using feature combinations
- investigate misclassified individuals
- evaluate effect of neglecting subset results
- investigate correlation between AHI and anthropometric variables
- classify subjects using STOP-BANG variables
- investigate correlation between AHI and final selected sound features
- introduce Experiment B
- describe importance of feature reduction and selection
- describe improved algorithm for feature reduction and selection
- describe dataset and preprocessing
- describe feature reduction and selection techniques
- evaluate classification results using different techniques
- compare results of inventive methodology with existing techniques
- evaluate time complexity of inventive methodology
- describe model combination and results
- discuss importance of feature reduction and selection
- discuss limitations of existing techniques
- conclude effectiveness of inventive algorithm

### Microphone Coupler

- introduce respiratory sounds
- motivate microphone coupler design
- describe air-chamber design criteria
- detail novel coupler design
- explain conical air-chamber geometry
- specify air-chamber dimensions
- describe microphone selection
- detail signal processing and recording setup
- outline data pre-processing and normalization
- present power spectra results for inspiration
- present power spectra results for expiration
- analyze results and explain physical properties
- discuss benefits of rubber isolator ring
- conclude and discuss future applications

