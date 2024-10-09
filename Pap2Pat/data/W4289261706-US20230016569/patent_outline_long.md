# DESCRIPTION

## BACKGROUND

- motivate machine learning

## SUMMARY

- define computer-implemented method
- define non-transitory computer readable medium
- define computing system

## DETAILED DESCRIPTION

- introduce patent application and its purpose

### I. OVERVIEW

- motivate accurate diagnosis in healthcare
- describe limitations of current diagnosis methods
- introduce chest radiographs as low-cost diagnostic
- describe embodiments for predicting comorbidity classes
- list examples of comorbidity classes
- describe predicting risk adjustment factors
- describe using historical chest radiographs for training
- describe updating or auditing diagnoses with trained models
- describe using models for treatment planning
- describe using models for identifying patients for studies
- describe using artificial neural networks (ANNs)
- describe common layers and output heads in ANNs
- describe predicting multiple outputs with ANNs
- describe using outputs to determine course of treatment
- describe using outputs to indicate relevant areas of chest radiograph
- describe predicting further outputs with additional models
- describe predicting outcomes related to specified conditions
- describe using weighted sums and generalized linear models
- describe predicting need for dialysis, claim fraud, and other outcomes
- describe predicting patient-specific drug efficacy
- describe predicting risk and presence of emphysema and other conditions
- describe using models with limited data for rare diseases
- describe augmenting outputs with additional models
- describe demonstrated utility of methods
- describe high AUC values for predicting dementia and renal failure

### II. EXAMPLE SYSTEMS

- introduce example system 100
- describe communication interface 102
- describe user interface 104
- describe processor(s) 106
- describe data storage 108
- describe system bus, network, or other connection mechanism 110
- describe communication interface 102 functions
- describe user interface 104 functions
- describe processor(s) 106 functions
- describe data storage 108 functions
- describe program instructions 118
- describe operating system 122
- describe application programs 120
- describe data 112
- describe stored models 116

### III. EXAMPLE METHODS

- describe receiving target radiographic image and applying ANN
- describe generating target outputs and detecting comorbidities

### IV. DETECTION OF DIABETES FROM FRONTAL CHEST RADIOGRAPHY

- describe using multitask deep learning model
- describe training and testing model on large clinical dataset
- describe validating model on out-of-fold predictions
- describe evaluating discriminatory ability of model
- describe clinical relevance of detecting diabetes from chest radiography

### V. PREDICTION OF MORTALITY AND COMORBIDITIES FROM CHEST RADIOGRAPHS IN COVID-19

- introduce deep learning model for predicting comorbidities and mortality from chest radiographs in COVID-19 patients
- describe model training and testing on frontal CXRs from 2010 to 2019
- motivate use of hierarchical condition category (HCC) mortality outcomes in COVID-19
- explain limitations of current value-based care (VBC) models
- describe role of radiologists in VBC systems
- introduce risk adjustment factor (RAF) score and its significance
- explain how RAF score is calculated
- describe importance of comorbidity data in predicting mortality
- motivate use of convolutional neural network (CNN) to link HCCs and RAF scores to radiographs
- describe application of VBC data and CXRs to train deep learning model
- outline image selection, acquisition, and preprocessing
- describe CXR dataset development
- explain image resizing and base weight generation
- describe sanity checks and pre-processing techniques
- introduce internal and external validation sets
- describe clinical data and inclusion criteria
- outline deep learning model architecture
- describe technical and hyperparameter details
- explain data augmentation techniques
- describe occlusion-based attribution maps
- outline statistical analysis methods
- describe comparison of demographic characteristics and clinical findings
- explain evaluation of model performance using AUC ROC
- describe multivariable logistic regression analysis
- outline feature selection and backward elimination
- summarize results of mortality prediction model
- describe patient characteristics
- introduce training cohort
- describe DL CNN analysis
- summarize AUC predictions
- discuss recall and precision
- analyze correlation coefficient
- describe comparative CXRs
- perform paired t-testing
- depict Spearman's rank correlation coefficients
- discuss univariate and multivariate analysis
- describe outcome modeling on external validation cohort
- discuss logistic regression model
- discuss model calibration
- apply logistic regression model
- discuss ROC AUC
- introduce discussion
- discuss DL model development
- discuss external validation
- discuss potential benefits
- discuss radiology's role in VBC
- discuss challenges in US healthcare system
- discuss clinical models of outcomes in COVID-19
- discuss DL model performance
- discuss occlusion maps
- discuss logistic regression on DL model predictions
- conclude DL model's ability to predict comorbidities and mortality

### VI. DETECTING RACIAL/ETHNIC HEALTH DISPARITIES USING DEEP LEARNING FROM FRONTAL CHEST RADIOGRAPHY

- introduce value-based care
- describe deep learning chest radiograph classifier
- present associations with race/ethnicity and social deprivation index
- train and validate CNN model on two cohorts
- calculate and analyze atherosclerosis diagnosis discrepancy
- determine associations with covariates using linear and logistic regression
- present results of CNN prediction and radiologists' reading
- discuss implications for value-based healthcare

### VII. PREDICTING PROLONGED HOSPITALIZATION AND SUPPLEMENTAL OXYGENATION IN PATIENTS WITH COVID-19 INFECTION FROM AMBULATORY CHEST RADIOGRAPHS USING DEEP LEARNING

- introduce multi-task deep learning with convolutional neural networks (CNNs)
- describe predicting comorbidities from frontal chest radiographs
- motivate predicting comorbidities from radiographs
- describe predicting hospitalization and supplemental oxygenation
- introduce clinical prognosis of outpatients with COVID-19
- describe study design and patient cohort
- define full admission
- describe patient demographics
- describe image acquisition and analysis
- introduce deep learning
- describe multi-task CNN architecture
- describe training and testing data sets
- describe ground truth labels
- describe data augmentation
- describe image normalization
- describe model training
- introduce multi-task learning (MTL)
- describe MTL framework
- describe explicit parameter sharing
- describe implicit parameter sharing
- describe positive transfer
- describe negative transfer
- introduce COVID-Net program
- describe geographic extent and severity of opacity scores
- describe clinical data
- describe statistical analysis
- describe logistic regression
- describe t-test
- describe ROC curve analysis
- describe fit of radiographic features to outcome data
- describe machine learning models
- describe recursive feature elimination
- describe model development process
- describe patient characteristics
- describe CNN analysis
- describe training and testing CNN model
- describe predicting age and comorbidities
- describe saliency maps
- describe imaging characteristics of COVID+ cohort
- describe univariate and multivariate analysis
- describe binary classification logistic regression
- describe ROC curve analysis
- describe final model development
- summarize results and discussion

### VIII. CONCLUSION

- summarize arrangements described
- describe scope of claims

