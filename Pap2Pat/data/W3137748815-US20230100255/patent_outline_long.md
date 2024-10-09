# DESCRIPTION

## FIELD OF INVENTION

- relate to medical imaging and radiotherapy planning

## BACKGROUND OF INVENTION

### Image Segmentation

- motivate image segmentation
- describe applications of image segmentation
- define contour and contour set
- discuss limitations of manual contouring
- introduce atlas-based auto-segmentation
- discuss machine learning-based approaches
- highlight need for interactive segmentation

### The Need for Interactive Segmentation

- motivate interactive segmentation
- discuss limitations of fully automatic techniques
- introduce semi-automatic methods
- discuss benefits of interactive techniques
- highlight difficulty with interaction
- discuss 2D vs 3D interaction
- introduce contour-based interaction
- discuss stroke-based interaction
- motivate use of spatial context
- introduce concept of contextual information

### Application Examples of Segmentation:

- describe manual contouring process
- describe semi-automatic contouring process

## PRIOR ART

- introduce prior art in medical imaging and ML

### Fully Automated Segmentation Using ML

- describe fully automatic segmentation method by China et al.
- describe fully automatic segmentation method by WO2017/091833
- discuss limitations of fully automatic segmentation methods

### Interactive 2D Image Segmentation Approaches

- overview of interactive 2D segmentation approaches

### Interactive 3D Segmentation in Medical Images

- discuss interactive 3D segmentation techniques
- discuss limitations of interactive 3D segmentation techniques

### Interactive Contour Propagation Methods

- discuss interactive contour propagation methods
- discuss limitations of interactive contour propagation methods
- motivate need for interactive contouring method
- discuss ML models for slice-by-slice image segmentation
- discuss limitations of ML models
- discuss Léger et al.'s ML model
- discuss Zheng et al.'s ML model
- discuss limitations of Léger et al.'s and Zheng et al.'s ML models
- train ML model for heart segmentation
- test ML model on different organs
- discuss results of testing ML model
- discuss limitations of ML model
- motivate need for generalized approach
- discuss state-of-the-art tools for image segmentation
- discuss limitations of state-of-the-art tools
- motivate need for fast and intuitive interaction method
- discuss importance of contour quality and speed
- discuss benefits of automated deep learning contouring
- discuss limitations of automated deep learning contouring
- motivate need for interactive contouring method
- introduce disclosed interactive contouring method
- discuss receiving input 2D image slice and input contour
- discuss predicting target contour data
- discuss using machine learning model for prediction
- discuss providing contextual information
- discuss learning contextual information from training data set
- discuss using consecutive image slices
- discuss updating machine learning model based on user edits
- discuss creating 3D contour from predicted 2D contours

## DETAILED DESCRIPTION

- introduce deep learning contouring
- limitation of prior art methods
- introduce interactive contouring approach
- use contextual information
- train model on multiple organs
- predict contour of various structures
- describe medical image contouring system
- include medical image database
- include contour prediction engine
- receive input image slice and contour data
- predict target contour data
- example for contouring 3D medical image
- receive input 2D image slice and contour data
- identify target image to contour
- use machine learning model to generate target contour
- require model to identify structures
- handle unseen structures
- train model using various anatomical structures
- use convolutional neural network
- provide contextual information
- distinguish structures by label
- multi-structure training
- generalize learning of contextual information
- segment previously unseen structures
- demonstrate using input contours of diverse structures
- evaluate segmentation using Dice score
- compare single-structure and multi-structure models
- show failure of single-structure model
- show success of multi-structure model
- describe flow diagram of contouring system
- include contour prediction engine
- include manual contouring and editing tool
- include image rendering engine
- create and edit contours
- display contours and image data
- predict contours using contour prediction engine
- provide target image slice and contextual information
- describe different input variants
- provide one input image slice and contour
- provide multiple input image slices and contours
- include empty mask
- predict target contour
- describe structure of interest
- identify structure of interest
- require combination of input image slice and contour
- provide contextual information
- predict target contour
- add predicted contour to contour set
- manually edit contours
- create new contours
- add new contours to contour set
- describe interactive contouring application workflow
- load patient 3D image
- select initial 2D image slice
- choose target image slice
- illustrate iterative propagation approach
- show initial state
- describe contour prediction engine
- illustrate direct contour propagation
- describe training machine learning model
- illustrate process of training
- describe generalization of model
- illustrate generation of training data
- describe training with multiple structures
- illustrate contouring of unseen structures
- describe display of 2D image slices
- illustrate performances of model
- describe single-structure model
- illustrate results of single-structure model
- describe multi-structure model
- illustrate results of multi-structure model
- describe data augmentation approaches
- describe system and method
- describe application of invention
- describe computer program
- describe computer readable storage medium
- describe computer process
- describe operating system
- describe computer system
- describe modifications and changes
- describe logic blocks
- describe associated components
- describe operably connected components
- describe overlapping operations
- describe multiple instances of operations
- describe order of operations
- describe specifications and drawings
- describe reference signs
- describe claim limitations
- describe introductory phrases
- describe definite articles
- describe first and second elements
- describe mutually different claims
- describe combination of measures
- illustrate contouring of medical images
- describe contextual information
- describe machine learning model
- describe contour prediction engine
- describe iterative propagation
- describe direct propagation
- describe training set
- describe multiple structures
- describe single label
- describe spatial contextual information
- describe different medical imaging modalities
- describe simultaneous learning
- describe distinctly labelled structures
- describe unseen structures
- describe contour prediction

