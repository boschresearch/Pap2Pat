# DESCRIPTION

## FIELD OF THE INVENTION

- introduce CAD system for pulmonary function assessment

## BACKGROUND OF THE INVENTION

- describe COVID-19 symptoms
- classify COVID-19 types
- discuss laboratory confirmation
- describe chest radiography
- discuss radiological forms of COVID-19
- highlight importance of patient selection
- discuss role of AI in diagnosis
- describe advantages of AI
- discuss limitations of CAD systems
- highlight challenge of X-ray image quality

## SUMMARY

- introduce novel CAD system for COVID-19 diagnosis

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- illustrate CAD system for assessment of pulmonary function in patients with Coronaviridae infection
- describe method for assessing pulmonary function performed by the CAD system

### Data Preprocessing

- segment medical image to identify lung region
- apply regional dynamic histogram equalization to enhance lung tissue contrast
- identify and mask off healthy lung tissues from infected tissues
- describe algorithm for identifying dominant modes of empirical distribution of gray levels
- refine segmentation using MGRF model with analytically estimated potentials

### Rotating, Scale, and Translation Invariant MGRF Model

- construct MGRF model to grade severity of lung infection
- define central-symmetric system of pixel-pixel interactions
- specify neighborhood system corresponding to interpixel distances
- define Gibbs potential functions of gray value and gray value co-occurrences
- approximate joint probability of object pixels using Gibbs distribution
- deal with problem of zero empirical probabilities using pseudocounts
- modify empirical probability distributions using pseudocounts
- estimate Gibbs potential functions using centered, training-set average, normalized histograms and co-occurrence matrices
- calculate Gibbs energy of infected lung region
- summarize training approach
- calculate co-occurrence of image signal at different radii
- normalize co-occurrence frequency
- estimate Gibbs potential and calculate Gibbs energy for training subjects

### NN-Based Fusion and Diagnostic System

- perform classification steps using artificial intelligence
- describe NN system that fuses diagnostic results from estimated Gibbs energy at different radii
- train NN-based diagnostic system using backpropagation approach
- tune hyper-parameters using random values and training data
- describe optimal values for hyper-parameters

### Experimental Results

- test and validate system using data from publicly available archive of COVID-19 positive cases
- illustrate estimated Gibbs energy for high severity lung infections
- illustrate estimated Gibbs energy for low severity lung infections
- demonstrate advantage of proposed Gibbs energy as new discriminatory image marker
- compare output of CAD system with ground truth of clinical cases
- perform cross-validation approaches to confirm accuracy of proposed NN-based fusion system
- compare accuracy of proposed system with other classification approaches

## Automation

- implement steps in method 10 in automated fashion using computer or electronic device
- describe exemplary apparatus for implementing steps in method 10
- describe computer components, including CPU, memory, and user interface
- describe storage devices, including mass storage devices and network interfaces
- describe operating system and software applications
- describe distributed or client-server computing environment
- describe CAD system program and image database

## Discussion and Conclusion

- introduce ARDS
- describe symptoms of ARDS
- explain pathophysiology of ARDS
- discuss respiratory support methods
- highlight ventilator shortage
- describe risks of high-pressure ventilation
- discuss mortality rates of COVID-19 patients
- introduce AI-based diagnosis
- describe benefits of AI-based diagnosis
- discuss potential of AI in medical imaging
- introduce multimodal data fusion
- describe feasibility of AI-based diagnosis
- correlate severity of pneumonia with mortality
- introduce various embodiments
- describe method for assessing pulmonary function
- describe process for assessing pulmonary function
- describe computer-aided diagnostic system
- introduce additional features of embodiments
- describe modeling and classification techniques
- conclude with modifications and scope of invention

