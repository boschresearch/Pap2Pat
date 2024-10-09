# DESCRIPTION

## FIELD

- relate to medical imaging

## BACKGROUND

- introduce aortic aneurysm
- describe limitations of current diagnosis methods
- highlight need for automated aneurysm segmentation tools
- motivate accurate detection of aortic tissues

## SUMMARY

- introduce object of present technology
- describe improved patient outcomes
- motivate accurate diagnosis and evaluation of aortic wall
- describe challenges of analyzing aortic CT images
- introduce fully convolutional networks (FCN)
- describe advantages of dilated convolutions
- motivate accurate recognition and extraction of aorta
- describe method for segmenting aortic tissues
- extract region of interest from image
- determine presence of calcification
- output indication of calcification presence
- describe first deep learning model
- describe second deep learning model
- extract first image features
- segment region of interest
- detect aortic lumen
- describe second image features
- determine presence of calcification
- describe third deep learning model
- detect aortic lumen
- remove aortic lumen from region of interest
- describe system for segmenting aortic tissues
- receive image of body
- extract region of interest
- determine presence of calcification

## Definitions

- define server
- define electronic device
- define client device
- define computer readable storage medium
- define database
- define information
- define indication
- define communication network
- clarify use of "first", "second", etc.
- describe implementations of present technology
- describe objects and aspects of present technology
- describe additional features and advantages
- describe appended claims
- conclude description of present technology

## DETAILED DESCRIPTION

- introduce principles of present technology
- describe scope of present technology
- explain examples and conditional language
- describe simplified implementations
- provide modifications to present technology
- explain structural and functional equivalents
- describe block diagrams and flowcharts
- explain functions of various elements
- describe processor and hardware capabilities
- introduce software modules
- describe electronic device 100
- explain hardware components of electronic device 100
- describe communication between components
- explain input/output interface and touchscreen
- describe program instructions and machine learning models
- explain implementation of electronic device 100
- introduce system 200
- describe communication system 200
- explain modifications to system 200
- describe medical imaging apparatus 210
- explain acquisition of images
- describe workstation computer 215
- explain control of medical imaging apparatus 210
- describe reception and processing of images
- explain implementation of workstation computer 215
- describe server 230
- explain reception of input image
- describe access to deep learning models 250
- explain training of deep learning models 250
- describe segmentation of aortic tissues
- explain implementation of server 230
- describe DL model 260
- extract image features
- segment ROI and background
- define ROI and background
- describe training of DL model 260
- describe architecture of DL model 260
- describe dilated convolutions
- describe ResNet-based FCN architecture
- describe alternative embodiments of DL model 260
- describe DL model 270
- extract image features
- segment lumens
- describe training of DL model 270
- describe architecture of DL model 270
- describe subtraction unit 285
- remove lumen from ROI
- output background of ROI
- describe DL model 280
- extract image features
- classify input image
- describe training of DL model 280
- describe architecture of DL model 280
- describe alternative embodiments of DL model 280
- describe database 235
- store medical images
- store model parameters and hyperparameters
- store datasets for training and testing
- describe labelled training dataset 240
- describe communication network 220
- introduce aortic tissue segmentation procedure
- obtain input images
- describe image characteristics
- motivate use of deep learning models
- introduce first deep learning model
- describe feature extraction
- describe prediction network
- output region of interest
- introduce second deep learning model
- describe feature extraction
- describe prediction network
- segment lumen
- introduce subtraction unit
- remove lumen from region of interest
- introduce third deep learning model
- describe feature extraction
- describe prediction network
- identify calcified tissue
- describe implementation details
- introduce training procedure
- fine-tune deeper network layers
- describe learning parameters
- describe loss function
- evaluate model performance
- describe validation process
- calculate accuracy, sensitivity, specificity, and BF-score
- describe equations for performance metrics
- provide example implementation details
- conclude training procedure
- define accuracy metrics
- introduce equations for accuracy metrics
- present results of accuracy metrics in tables
- illustrate exemplary images of CT-scans
- illustrate exemplary images of results of segmentation
- motivate aorta extraction
- explain advantages of aorta extraction
- describe lumen segmentation
- describe thrombus and artery wall evaluation
- introduce CNN and feed forward neural network
- describe training process
- illustrate performance of network
- describe method for segmenting aortic tissues
- illustrate flowchart of method
- describe server configuration
- describe access to DL models
- describe method steps
- receive image of subject
- extract ROI from image
- determine presence of calcified tissue
- output indication of calcified tissue
- describe alternative embodiments
- illustrate method with three DL models
- receive image
- extract first set of image features
- obtain ROI
- extract second set of image features
- segment ROI and classify tissues

### BACKGROUND

- introduce segmentation model
- motivate clinical needs
- describe Resnet-based FCN architecture
- explain fine-tuning process
- discuss over-fitting concerns
- define optimal learning parameters
- describe up-sampling factor
- explain weighted loss functions
- apply Adam network optimizer
- outline training steps
- describe lumen/calcification network
- introduce DL model configuration
- analyze aortic walls
- retrain model on more patient data
- improve model in two steps
- validate segmentation model

