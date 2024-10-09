# DESCRIPTION

## TECHNICAL FIELD

- introduce SpO2 measurement

## BACKGROUND

- define SpO2 level
- motivate SpO2 measurement
- limitations of current methods
- application of pulse oximetry
- describe clinical pulse oximeters

## DETAILED DESCRIPTION

- introduce hypoxemia
- describe limitations of pulse oximeters
- motivate smartphone-based SpO2 sensing
- describe benefits of smartphone-based SpO2 monitoring
- introduce examples of deep learning models
- describe data collection using varied FiO2 protocol
- summarize results of analysis on 6 subjects
- describe certain details of embodiments
- omit certain details for clarity
- describe modifications to embodiments
- introduce FIG. 1
- describe smartphone 102
- introduce wideband light source 104
- introduce wideband imaging sensor 106
- describe display 118
- describe circuitry for color channel gain 112
- describe processor(s) 108
- describe memory 110
- describe executable instructions for setting color gain values 114
- describe executable instructions for classification 116
- introduce deep learning model 120
- describe smartphones as consumer electronic devices
- describe models of smartphones
- describe wideband light source 104
- describe wideband imaging sensor 106
- describe positioning of wideband light source 104 and wideband imaging sensor 106
- introduce infrared (IR) source and sensor
- describe circuitry for color channel gain 112
- describe per-channel color gain values
- describe gain values for each color channel
- describe setting gain values based on model of smartphone
- describe setting gain values based on empirical study data
- describe processor(s) 108
- describe memory 110
- describe executable instructions for setting color gain values 114
- describe executable instructions for classification 116
- describe deep learning model 120
- describe training deep learning model 120
- describe predicting SpO2 levels
- describe predicting SpO2 levels below 85 percent
- describe predicting SpO2 levels between 85 and 100 percent
- describe operation of smartphone 102
- describe illuminating finger with wideband light source 104
- describe capturing pixel data with wideband imaging sensor 106
- describe gain-adjusting pixel data
- describe predicting SpO2 level of blood
- describe detecting excessive motion of finger
- describe providing feedback to user
- describe using predicted SpO2 level
- describe displaying SpO2 level
- describe using smartphone as at-home screening tool
- introduce pulse oximetry
- describe Beer-Lambert Law
- derive Equation 2
- explain oxyhemoglobin and deoxyhemoglobin extinction coefficients
- derive Equation 3
- discuss limitations of transmittance pulse oximetry
- introduce reflectance photoplethysmography
- discuss challenges of reflectance photoplethysmography
- describe validation of pulse oximeter system
- explain FiO2 experiments
- discuss breath-holding experiments
- introduce FIG. 3
- describe color gain settings
- explain effect of gain values on pixel data
- introduce FIG. 4
- describe data processing
- explain pixel data adjustment
- describe pre-processing operations
- generate PPG signals
- discuss feedback to set gain values
- introduce classification techniques
- describe logistic regression
- explain Equation 4
- introduce convolutional neural network
- describe training of convolutional neural network
- introduce FIG. 5
- describe logistic regression example
- describe convolutional neural network example
- introduce FIG. 6
- describe training of classifier
- explain sampling of training data
- describe normalization of training data
- train convolutional neural network
- calculate statistics of training data
- implement trained classifier
- evaluate performance of trained classifier
- sample user data
- normalize user data
- provide user data to classifier
- predict SpO2 level
- discuss operation of classifier
- obtain new user data
- sample new user data
- normalize new user data
- provide new user data to classifier
- output SpO2 prediction
- discuss use of statistics in normalization
- conclude operation of classifier

### IMPLEMENTED EXAMPLES

- perform varied FiO2 study
- administer controlled fractional mixtures of oxygen-nitrogen
- instrument subjects' fingers with transmittance pulse oximeter clips
- record ground truth data using multiple purpose-built pulse oximeters
- record subject characteristics and data statistics
- configure smartphone device for data collection
- set hardware camera settings to avoid data loss
- use clay ice packs to prevent device overheating
- determine manual hardware sensitivity, exposure, and whitebalance settings
- set color gains to avoid signal loss
- preprocess data by taking mean pixel values for each color channel
- treat each hand subject pair as a unique subject
- divide data into 1 sample per 1-second window
- perform pulse oximetry validation using regression analysis
- evaluate models using Leave-One-Subject-Out cross validation
- compare performance using Mean Absolute Error
- develop hypoxemia screening tool using classification analysis
- threshold ground truth recordings below different SpO2 levels
- vary decision boundary to bias towards recall vs. precision
- plot ROC curves for each subject using LOOCV

