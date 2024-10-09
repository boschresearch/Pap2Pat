# DESCRIPTION

## TECHNICAL FIELD

- introduce machine learning system

## BACKGROUND

- motivate Alzheimer's disease
- describe current diagnosis methods
- limitations of current diagnosis methods
- introduce retina as biomarker
- associate retinal vasculature with Alzheimer's disease
- limitations of previous retinal imaging studies
- motivate machine learning system

## SUMMARY

- introduce machine learning system
- describe system components
- describe trained machine learning model
- describe image acquisition
- process retinal fundus image
- classify retinal features
- predict Alzheimer's disease
- describe multi-stage pipeline architecture
- describe image quality selector model
- describe vessel map generator model
- describe Alzheimer disease classifier model
- describe saliency map generator
- describe training process
- describe vessel map generation
- describe Alzheimer disease classification
- describe saliency map generation
- describe multiple trained image quality selector models
- describe multiple-stage pipeline architecture
- describe computer instructions
- describe non-transitory computer-readable medium
- describe first computer code portion
- describe second computer code portion
- describe third computer code portion

## DETAILED DESCRIPTION

- introduce machine learning system for Alzheimer's disease prediction
- describe system components: processor, memory device, image acquisition system
- define terminology: "a", "an", "the" include singular and plural referents
- explain relative terms: "connected to", "coupled to", "electrically coupled to"
- define "memory" and "memory device"
- define "processor" and its functions
- describe system 100 and its components
- introduce FIG. 1: block diagram of system 100
- describe machine learning model(s) 120: classify retinal features, predict Alzheimer's disease
- explain training and testing of machine learning model(s) 120
- introduce representative embodiment of system 100
- describe UK Biobank database used for training and testing
- explain advantages of using UK Biobank database
- introduce FIG. 2: block diagram of machine learning model(s) 120 pipeline architecture
- describe three stages of pipeline architecture: image quality selection, vessel map segmentation, SVM-based classifier
- explain advantages of multi-stage pipeline architecture
- describe image quality selection stage 200
- explain image quality evaluation criteria
- introduce FIG. 3: flow diagram of image quality selection process
- describe training of image quality selectors 200a-200e
- introduce FIG. 4: examples of sufficient and insufficient fundus image quality
- describe selection of control subjects
- introduce FIGS. 6A and 6B: matching of control subjects
- describe experiments: five-fold cross-validation strategy
- introduce Table 2: performance comparison of AD group vs. normal controls group
- describe performance metrics: sensitivity, specificity, classification accuracy, F-1 score
- explain feature selection using T-test
- introduce Table 3: performance with T-test feature selection
- describe blind-test experiments
- explain data-reliance issue in machine learning
- describe remedy for small-database drawback
- introduce saliency map generator 240
- describe saliency map 241: interpretable features for Alzheimer's disease classification
- introduce FIG. 9: generated saliency map 241
- explain importance of small vessels in Alzheimer's disease classification
- describe vessel diameter narrowing and venular degeneration in Alzheimer's disease
- explain benefits of machine learning approach
- describe pre-symptomatic period of Alzheimer's disease
- explain need for in vivo image biomarker for timely routine screening
- describe limitations of previous research on retina and Alzheimer's disease
- explain benefits of machine learning-based approach
- describe automation of tasks in machine learning pipeline
- explain elimination of human error and bias
- describe generality of machine learning-based model
- explain domain barrier between developmental and testing datasets
- describe human interpretable biomarker features
- explain importance of venular vessel in Alzheimer's disease classification
- describe cerebral vascular contribution to Alzheimer's disease
- explain accumulation of toxic amyloid-beta in vessel
- describe morphological substrates of cerebrovascular diseases
- explain venular degeneration in Alzheimer's disease
- describe retinal venular vessels relation to diseases
- explain machine learning-based method for finding deeper level features
- describe importance of individual pixels in classification decision
- explain benefits of machine learning-based technique
- describe potential of retina as candidate site for Alzheimer's disease biomarker
- explain feasibility of discovering links between retina vasculature and Alzheimer's disease
- summarize benefits of machine learning-based approach for Alzheimer's disease diagnosis

### Image Quality Selection

- motivate image quality selection
- introduce image quality selector
- define insufficient quality factors
- train independent networks
- ensure sufficient quality images

### Vessel Map Generation

- introduce vessel map generator
- train and evaluate vessel map generator

### Alzheimer's Disease Classification

- introduce Alzheimer's disease classifier model
- describe input and output of SVM
- describe cross-validation protocol

### Attention Maps

- introduce attention maps
- describe generation of attention maps

### Treatment

- introduce treatment process
- describe role of machine learning system
- describe processing of fundus image
- describe prediction of Alzheimer's disease
- describe optimization of treatment
- introduce flow diagram of machine learning method
- describe processing of retinal fundus image
- describe prediction of Alzheimer's disease

