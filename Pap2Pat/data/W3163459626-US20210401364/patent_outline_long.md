# DESCRIPTION

## FIELD OF THE INVENTION

- relate to machine learning for OSA classification

## BACKGROUND

- define OSA and its severity
- describe signs and symptoms of OSA
- discuss comorbidities of OSA
- highlight need for accurate OSA screening tool
- describe limitations of PSG assessment
- discuss portable monitoring devices for OSA
- introduce STOP-BANG questionnaire
- discuss tracheal breathing sound analysis for OSA screening
- highlight need for improved OSA screening techniques

## SUMMARY OF THE INVENTION

- introduce method for deriving OSA screening tool
- obtain initial dataset with OSA severity, anthropometric, and audio data
- extract spectral and bi-spectral features from audio data
- select training dataset and group subjects by OSA severity
- divide subject datasets into anthropometrically distinct subsets
- derive input for classifier training procedure
- train classifier for OSA classification
- introduce method for performing OSA screening test
- obtain patient dataset and trained classifier
- run trained classifier multiple times with different feature combinations
- derive final classification result
- store or display final classification

## DETAILED DESCRIPTION

### Systems & Processes

- introduce AWakeOSA algorithm
- describe anthropometric effects on breathing sounds
- record tracheal breathing sounds
- filter and amplify acoustic signals
- convert analog to digital signal
- store digital audio data
- record in supine and upright positions
- instruct subjects to breathe deeply
- record silent period
- mark inspiration phase
- record breathing sounds for test subjects and patients
- extract inspiratory and expiratory sounds
- investigate and exclude artifacts
- exclude signals with low SNR
- select 50% duration around maximum breathing phase
- store anthropometric data
- store STOP-BAND questionnaire answers
- store craniofacial measurements
- compute fractal dimensions
- filter breathing sound phases
- compute power spectrum and bi-spectrums
- normalize filtered signals
- calculate spectral data
- store spectral data and bi-spectral data
- store AHI assigned to each subject
- divide subject datasets into non-OSA and OSA groups
- divide initial dataset into training and blind testing datasets
- identify high-severity and low-severity groups
- exclude records with AHI between 10 and 20
- subdivide datasets into anthropometrically distinct subsets
- extract features from signal representations
- evaluate features using training data and blind testing dataset
- remove outliers from blind testing features
- scale response variable to achieve Gaussian distribution
- build linear model for AHI using features
- evaluate overall correlation between prediction model and AHI
- divide response variable into segments
- evaluate correlation coefficient for each segment
- retain models with high correlation coefficient
- evaluate segment overlap from AHI perspective
- evaluate segment overlap from model perspective
- filter down models based on overlap percentage
- evaluate models using training data and blind testing dataset
- validate models using training data
- test models using blind testing data
- filter down models based on evaluated performance
- run different model combinations
- calculate weighted classification decision per subject
- select best model combination

### Experimental Support

- introduce experiment A
- hypothesize upper airway deformities affect breathing sounds
- summarize prior works on proof of concept
- describe testing classification accuracy
- discuss limitations of prior works
- motivate need for quick screening with high sensitivity
- introduce AHI=15 as threshold for decision making
- describe prior techniques' limitations with AHI=15
- introduce AWakeOSA algorithm
- describe premise of AWakeOSA algorithm
- illustrate simplified AWakeOSA algorithm
- describe feature reduction and selection stage
- omit model-building, model-selection, and model-combining stages
- discuss challenges of heterogeneous OSA population
- describe grouping individuals into subgroups
- extract best sound features to predict AHI
- train classifier using training set of data
- use weighted average voting scheme for classification
- summarize procedure and results of experiment A
- describe data collection and participant demographics
- analyze breathing sounds data and anthropometric parameters
- report classification accuracy, specificity, and sensitivity
- motivate OSA diagnosis
- limitations of anthropometric measures
- correlation of anthropometric parameters with AHI
- application of breathing sounds analysis
- introduce simplified AWakeOSA algorithm
- describe anthropometric subsets
- explain effect of aging on voice
- explain effect of sex on voice
- explain effect of BMI on vocal quality
- explain effect of Mallampati score on upper airway
- explain effect of neck circumference on OSA risk
- analyze results of simplified AWakeOSA algorithm
- discuss correlation of selected features with AHI
- discuss importance of low-frequency components
- describe mean of spectral slope feature
- discuss implications of results on upper airway characteristics
- discuss final overall classification decisions
- analyze contribution of each subset to final vote
- discuss anthropometric parameters of misclassified subjects
- summarize results of Experiment A
- introduce Experiment A methodology
- describe data collection and recording protocol
- explain data selection and preprocessing
- describe feature extraction and classification process
- discuss training and testing datasets
- describe anthropometric subsets creation
- explain feature extraction from breathing sounds data
- describe spectral and bispectral features extraction
- discuss feature scaling and selection
- conclude Experiment A results
- introduce experimental support
- calculate p-value for each feature
- assign robustness score to each feature
- select features with high robustness score
- compute correlation coefficients between features
- remove features with high correlation
- evaluate feature combinations using Random-Forest classifier
- select best feature combinations
- evaluate overall classification using best feature combinations
- investigate misclassified individuals
- evaluate effect of neglecting subsets
- correlate AHI with anthropometric variables
- classify subjects using STOP-BANG variables
- correlate AHI with final selected sound features
- introduce Experiment B
- describe importance of feature reduction and selection
- introduce improved algorithm
- describe steps of improved algorithm
- demonstrate utility of improved algorithm
- describe dataset of Experiment B
- adopt features from Experiment A
- describe feature reduction and selection techniques
- evaluate classification results using five techniques
- compare results of improved algorithm with existing techniques
- describe methodology of Experiment B
- evaluate experimental results
- discuss advantages of improved algorithm
- describe response nature and methodology
- scale response to reduce skewness
- evaluate classification accuracies using three-feature models
- evaluate classification accuracies using four-feature models
- evaluate classification accuracies using five-feature models
- compare results of improved algorithm with existing techniques
- describe model combination stage
- evaluate results of model combination
- discuss importance of feature reduction and selection
- describe limitations of existing techniques
- introduce novel feature-combination selection
- describe advantages of improved algorithm
- evaluate results of improved algorithm
- discuss importance of modeling response
- describe scaling of response
- evaluate results of improved algorithm
- discuss advantages of improved algorithm
- describe handling of missing data
- evaluate results of improved algorithm
- conclude advantages of improved algorithm

### Microphone Coupler

- introduce respiratory sounds
- motivate microphone coupler
- describe air-chamber design criteria
- introduce novel coupler design
- describe material selection
- describe air-chamber geometry
- define dimensional properties
- select diameter at bottom of air-chamber
- select diameter at top of air-chamber
- select depth of air-chamber
- describe counter-bore hole design
- introduce rubber isolator ring
- describe microphone selection
- describe microphone specifications
- describe drive circuit design
- describe digitization hardware
- describe audio recording procedure
- describe data pre-processing
- describe normalization procedure
- describe filtering procedure
- describe power spectral estimation
- analyze response curves for inspiration
- analyze response curves for expiration
- analyze effect of rubber isolator ring
- explain acoustic resonance effect
- explain acoustic impedance effect
- explain sound capture effect
- summarize optimal air-chamber design

