# DESCRIPTION

## BACKGROUND OF THE DISCLOSURE

- motivate machine learning
- describe current state of chemical process development
- highlight limitations of current approaches

## BRIEF SUMMARY OF THE DISCLOSURE

- introduce methodology for predicting chemical mixture compositions
- describe training of linear regression and ANN models
- report R2 regression scores for LR and ANN models
- compare accuracy of LR and ANN models
- discuss relationship between model performance and training data set size
- report effect of experimental condition variations on model accuracy
- introduce method of training machine learning model
- describe obtaining spectra for mixtures
- extract features from spectra
- train machine learning model using extracted features
- set initial hyperparameters
- evaluate model performance using test set
- update hyperparameters
- introduce method of determining composition of multicomponent mixture
- obtain spectrum of multicomponent mixture
- extract features from spectrum
- provide features to trained machine learning model
- obtain concentration of constituent components
- introduce method of determining formation of product in reaction mixture

## DETAILED DESCRIPTION OF THE DISCLOSURE

- introduce autonomous chemical process development and optimization methods
- describe challenges of measuring multicomponent stream compositions
- introduce universal analytical methodology based on multitarget regression ML models
- describe simulated FTIR spectra for up to 6 components in water
- test seven different ML algorithms
- validate methodology with experimental data
- describe ML models trained using experimental data
- evaluate ML models for mixtures of up to 4-components
- describe linear regression models predicting concentrations
- describe artificial neural network models predicting concentrations
- motivate need for fast and inexpensive spectrochemical characterization tool
- introduce FTIR spectroscopy as a powerful analytical technique
- describe limitations of traditional FTIR-based methods
- introduce ML algorithms to enhance FTIR analysis
- describe previous studies on ML-enhanced FTIR analysis
- introduce universal algorithm for determining chemical species concentrations
- generate multicomponent mixture FTIR spectra using linear combination
- train ML algorithms using simulated multicomponent spectra
- validate ML algorithms using experimental mixtures
- describe reactants and products of two chemical reactions as model mixture components
- evaluate performance of ML algorithms
- describe method of training a machine learning model
- obtain spectra for each mixture of a plurality of mixtures
- extract features from each obtained spectrum
- train machine learning model using extracted features
- set initial set of hyperparameters
- evaluate performance of machine learning model
- update hyperparameters
- repeat evaluating and updating steps
- describe method of determining composition of a multicomponent mixture
- obtain spectrum of the multicomponent mixture
- extract features from the obtained spectrum
- provide extracted features to a machine learning model
- obtain concentration of one or more constituent components
- describe method of determining formation of a product in a reaction mixture
- obtain spectrum of the reaction mixture
- extract features from the obtained spectrum
- provide extracted features to a machine learning model
- obtain concentration of one or more constituent components
- repeat steps until concentration reaches a predetermined threshold
- quench the reaction mixture when concentration reaches a predetermined threshold
- describe apparatus for determining formation of a product
- describe reactor configured to contain the reaction mixture
- describe FTIR spectrometer configured to receive a sample of the reaction mixture
- describe processor in communication with the FTIR spectrometer
- describe processor configured to extract features from the spectrum
- describe processor configured to provide extracted features to a machine learning model
- describe processor configured to obtain concentration of one or more constituent components
- describe processor configured to determine formation of the product
- describe flow cell in fluid communication with the reactor
- describe processor configured to provide a product signal when concentration reaches a predetermined threshold

### Machine Learning Methodology Development

- develop robust ML approach
- evaluate model performance using absorbance and concentrations
- introduce model system with 6 components
- generate mixture FTIR spectra using Beer's Law
- introduce signal-to-noise ratio as a variable
- simulate noise in spectra
- preprocess data using principal component analysis
- reduce dimensionality of data set
- select regression models for evaluation
- evaluate performance of 7 ML algorithms
- select Linear Regression and Artificial Neural Networks for further evaluation
- evaluate effect of number of training points on model performance
- evaluate effect of simulated noise on model prediction accuracy
- evaluate effect of number of chemical components on model robustness
- evaluate effect of type of chemical system on model performance
- compare performance of LR and ANN models for different chemical systems

### Experimental Implementation of ML Methodology

- introduce experimental setup
- describe programmable pumps and transmission FTIR flow cell
- explain data collection process
- summarize ML model development
- motivate PCA for dimensionality reduction
- show example FTIR spectra of 3-component mixtures
- describe limitations of classical approaches
- introduce LR and ANN algorithms
- summarize performance metrics
- compare performances of LR and ANN
- show predicted and actual concentrations
- evaluate effect of number of training points
- describe experimental methods
- list materials used
- describe pumping system and FTIR spectrometer
- introduce simulated data generation
- describe Beer's law and concentration matrix
- introduce simulated noise introduction
- describe PCA for dimensionality reduction
- summarize ML algorithm training and evaluation
- describe FTIR experimental data collection
- conclude with general approach for developing ML regression models

