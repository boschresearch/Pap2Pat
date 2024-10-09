# DESCRIPTION

## BACKGROUND

- motivate labor management problem
- describe Friedman curve
- limitations of WHO partogram
- describe Zhang et al. partogram
- summarize ineffectiveness of existing approaches

## SUMMARY

- introduce system for predicting labor outcomes
- describe feature vector generation
- describe machine learning model training
- describe risk prediction output
- describe optional baseline model
- describe optional graph plotting
- describe optional updated risk prediction
- describe method for predicting labor outcomes
- describe non-transitory computer readable medium

## DETAILED DESCRIPTION

- introduce intrapartum prediction mechanisms
- describe individualized labor chart establishment
- motivate patient counseling and decision making
- define unfavorable labor outcomes
- train intrapartum models using machine learning
- generate Labor Risk Score (LRS)
- incorporate dynamic labor variables
- adjust dynamic confounders in data
- compare machine learning with traditional statistical approaches
- describe Data and Specimen Hub (DASH) database
- train incremental gradient boosting machine (GBM) model
- execute models using processor
- describe "Consortium on Safe Labor" database
- generate predictions using machine-learning techniques
- describe system for intrapartum prediction of unfavorable labor outcomes
- describe hardware components of computing device 110
- describe hardware components of server 120
- illustrate system for predicting intrapartum risk of unfavorable labor outcomes
- describe baseline model for predicting risk of unfavorable outcomes
- describe use of output from baseline model
- describe 4 cm dilation model for predicting risk of unfavorable outcomes
- describe use of output from 4 cm dilation model
- describe additional models for predicting risk of unfavorable outcomes
- describe use of new data to generate new or updated risk scores
- illustrate flow for training and using mechanisms for intrapartum prediction of unfavorable labor outcomes
- describe labeled data used to train machine learning models
- describe data from DASH database used to generate labeled data
- describe removal of data associated with certain patients from training data
- describe characteristics of patients included in training data
- describe demographic and clinical characteristics of population represented in training and validation data
- motivate use of machine learning models for predicting intrapartum risk of unfavorable labor outcomes
- describe limitations of existing approaches to predicting intrapartum risk of unfavorable labor outcomes
- describe advantages of using machine learning models for predicting intrapartum risk of unfavorable labor outcomes
- describe application of machine learning models to real-world data
- describe potential impact of using machine learning models for predicting intrapartum risk of unfavorable labor outcomes
- summarize benefits of using machine learning models for predicting intrapartum risk of unfavorable labor outcomes
- define unfavorable labor outcomes
- describe data used for training
- motivate imputation of missing values
- describe gradient boosting machine (GBM) model
- format patient data as vectors
- code outcomes for patients
- group training data into folds
- describe cross-validation approach
- conduct grid search for hyperparameters
- generate first tree using training data
- generate additional trees to increase accuracy
- aggregate individual trees into final model
- evaluate performance of each model
- generate final trained model using best hyperparameters
- use final trained model to make predictions
- train multiple prediction models for different points during labor
- describe process for training machine learning model
- describe process for generating groupings of folds
- find highest performing hyperparameters
- perform search over hyperparameters
- select best performing hyperparameters
- train final model
- generate and select training data
- describe process for using machine learning model
- receive novel data
- provide novel data to trained GBM model
- receive output from trained GBM model
- plot outcome on curve of predicted risks
- cause curve to be presented to user
- show trends in average risk scores

### Further Examples Having a Variety of Features

- define method for predicting risk of unfavorable labor outcomes
- specify machine learning model and training data
- describe baseline model and output
- specify cervical dilation range for model training
- list static and dynamic variables used in model
- describe graph plotting and presentation
- define second feature vector and updated risk calculation
- describe system and computer readable medium embodiments

