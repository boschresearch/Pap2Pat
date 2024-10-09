# DESCRIPTION

## STATEMENT REGARDING FEDERALLY FUNDED RESEARCH

- disclose government funding

## BACKGROUND

- introduce CAR T cell therapy
- limitations of current methods

## SUMMARY

- introduce T cell classifying device
- describe device components
- explain single-cell autofluorescence image sensor
- describe processor and non-transitory computer-readable medium
- outline method of characterizing T cell activation state
- outline method of sorting and/or classifying T cells
- outline method of administering activated T cells
- summarize device and method aspects

## DETAILED DESCRIPTION

- define scope of invention
- describe terminology used
- introduce modifying biological molecules
- describe functional components and processing steps
- contemplate various methods and systems
- describe various aspects of the invention
- provide examples of the invention
- describe the scope of the invention

### Methods

- provide a method of sorting T cells
- receive a population of T cells
- acquire an autofluorescence intensity image
- pre-process the autofluorescence intensity images
- physically isolate a portion of the population of T cells
- generate a report including an activation prediction
- compute activation status using a convolutional neural network
- pre-train the convolutional neural network
- fine-tune the convolutional neural network
- train the convolutional neural network with autofluorescence intensity images
- sort CD4+, CD3+, and/or CD8+ T cells
- provide surprising accuracy of classifying T cells
- perform the method without a fluorescent label
- perform the method without immobilizing the T cell
- identify outlier images
- provide a method of administering activated T cells
- modify the population of T cells
- administer the population of T cells to a subject
- harvest T cells from the subject
- modify the sorted T cells or the population of T cells
- administer an unsorted population of T cells
- provide surprising results
- describe the efficacy of the method

### Systems

- provide a T cell sorting device
- describe the cell analysis pathway
- describe the inlet
- describe the observation zone
- describe the outlet
- describe the cell sorter
- describe the single-cell autofluorescence image sensor
- describe the processor and non-transitory computer-readable medium
- describe the light source
- describe the cell size measurement tool
- describe the electronic communication between components
- describe the instructions stored on the non-transitory computer-readable medium
- describe the trained convolutional neural network
- describe the device as substantially free of fluorescent labels and immobilizing agents

### Example 1

- introduce cell preparation and imaging study
- describe informed consent and Institutional Review Board approval
- summarize NAD(P)H intensity image creation
- detail CD3 and CD8 T cell isolation
- describe T cell population culture
- outline NAD(P)H intensity image acquisition
- specify image processing software
- describe image segmentation using CellProfiler
- filter out non-T cells using fluorescence lifetime
- remove dim images and images with no cells
- pad images with black borders
- augment dataset with image rotations and flipping
- implement image processing pipeline using OpenCV
- introduce nested cross-validation
- describe leave-one-donor-out test principle
- outline hyper-parameter tuning and model selection
- apply nested cross-validation scheme
- evaluate model performance using multiple metrics
- introduce linear classifiers
- describe frequency classifier
- outline logistic regression with Lasso regularization
- detail Lasso logistic regression model features
- introduce simple neural network classifiers
- describe fully-connected neural network
- outline LeNet CNN architecture
- introduce pre-trained CNN classifiers
- describe pre-trained CNN off-the-shelf model
- outline pre-trained CNN with fine-tuning
- introduce dimension reduction
- motivate UMAP
- describe UMAP parameters
- perform feature extraction and dimension reduction
- exclude donor 4 from dimension reduction analyses
- introduce saliency maps
- describe backpropagation
- describe guided backpropagation
- generate saliency maps
- interpret saliency maps
- introduce classification goal
- describe frequency classifier
- describe Lasso logistic regression approaches
- describe fully connected neural network
- describe LeNet CNN architecture
- describe pre-trained CNN with fine-tuning
- describe overall workflow
- describe training procedure
- introduce subject-wise cross-validation
- describe nested cross-validation scheme
- plot evaluation metrics
- compare pre-trained CNN models
- describe frequency classifier results
- describe logistic regression results
- describe fully connected neural network results
- describe LeNet CNN results
- describe pre-trained CNN with fine-tuning results
- introduce confirmatory experiment
- describe confirmatory experiment results
- inspect misclassified images
- visualize misclassified images
- describe temperature scaling
- visualize T cell dataset in 2D
- describe UMAP results
- compare alternative image representations
- describe saliency map results
- interpret saliency maps

## DISCUSSION

- demonstrate machine learning models
- compare CNN with logistic regression
- fine-tune pre-trained CNN
- compare fine-tuning with off-the-shelf CNN
- analyze effect of fine-tuning more layers
- discuss computational costs
- recommend fine-tuning last few layers
- recognize image attributes
- interpret logistic regression model
- interpret fine-tuned CNN
- analyze saliency maps
- discuss limitations of interpretation
- discuss limitations of study
- discuss potential for improvement
- discuss potential applications
- discuss misclassified images
- discuss image cropping quality
- discuss potential for future work
- summarize results
- introduce T cell classifying device
- describe cell analysis pathway
- describe single-cell autofluorescence image sensor
- describe processor and computer-readable medium
- describe instructions for processor
- describe optional pre-processing
- describe inputting image into CNN
- describe producing activation prediction
- describe additional embodiments
- describe microfluidic or nanofluidic pathway
- describe flow regulator
- describe light source
- describe wavelength of light source
- describe repetition rate of image sensor
- describe pixel-by-pixel intensity measurements
- describe charge collection device array
- describe detector-side filter
- describe cell size measurement tool
- describe cell imager
- describe pre-processing steps
- describe outlier detection
- describe additional embodiments

