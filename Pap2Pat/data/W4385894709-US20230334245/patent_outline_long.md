# DESCRIPTION

## CROSS REFERENCE

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate text classification
- limitations of zero-shot models

## DETAILED DESCRIPTION

- define network
- define module
- introduce zero-shot classification models
- describe limitations of existing models
- motivate need for efficient zero-shot classification
- introduce Conformal Predictor (CP) framework
- describe CP framework components
- introduce fast base classifier
- describe calibration dataset
- generate predictions using base classifier
- compute non-conformity scores
- describe quantile computation
- generate reduced label set
- use reduced label set with zero-shot model
- describe ensemble of class label descriptions
- describe cosine-similarity-based non-conformity scores
- describe distilled BERT-base model
- describe another parameter-efficient NLI zero-shot model
- discuss model-agnostic nature of CP framework
- describe application to prompt-based few-shot classification models
- describe application to in-context learning
- describe application to image classification models
- introduce computing device for implementing CP framework
- describe efficient zero-shot classification module
- describe networked system for implementing CP framework

### Computer Environment

- introduce computing device
- describe processor and memory
- describe operation of computing device
- describe machine-readable media
- describe executable code
- introduce efficient zero-shot classification module
- describe data interface
- describe user interface
- describe communication interface
- introduce conformal prediction module
- describe NLI/NSP classifier module
- describe implementation of modules
- introduce networked system
- describe user device
- describe data vendor servers
- describe server
- describe network
- describe user interface application
- describe other applications
- describe database
- describe network interface component
- describe data vendor server
- describe database
- describe network interface component
- describe server
- describe efficient zero-shot classification module
- describe network interface component

### Work Flows

- introduce method for efficient zero-shot text classification
- receive calibration dataset with texts and labels
- generate predicted labels using base classifier model
- compute non-conformity scores by comparing predicted labels and calibration labels
- compute non-conformity threshold based on non-conformity scores and error rate
- generate predicted testing label using base classifier model
- generate second set of non-conformity scores by comparing predicted testing label and classification labels
- determine reduced set of classification labels based on non-conformity scores and threshold

### Example Data Experiment and Performance

- evaluate CP-based framework on intent classification datasets
- use moderately sized BART-large as zero-shot classification model
- use small BERT-base as base classifier in CP framework
- calibrate CP-Token, CP-Glove, and CP-Distil using training set and validation set
- train CP-CLS base classifier using training set and validation set
- show empirical coverage and average label set size of four base classifiers
- compare accuracy, average inference time, and average label set size of CP framework
- observe CP framework achieves valid coverage
- observe CP reduces average number of labels for zero-shot model
- observe fine-tuning base classifier reduces average number of labels
- observe CP-Token achieves best inference time on some datasets
- observe CP-Distil improves inference time on some datasets
- observe CP improves efficiency on datasets with many labels
- observe CP performs comparable to zero-shot model
- observe CP-based label filtering retains performance of corresponding models
- conclude CP framework is effective for efficient zero-shot text classification

