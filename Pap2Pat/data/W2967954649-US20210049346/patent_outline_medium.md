# DESCRIPTION

## STATEMENT REGARDING FEDERALLY FUNDED RESEARCH

- disclose government funding

## BACKGROUND

- introduce CAR T cell therapy

## SUMMARY

- describe T cell classifying device
- outline method of characterizing T cell activation
- outline method of sorting and/or classifying T cells
- outline method of administering activated T cells

## DETAILED DESCRIPTION

- define scope of invention
- describe terminology used
- provide functional components and processing steps
- describe various aspects of invention

### Methods

- introduce method of sorting T cells
- receive population of T cells
- acquire autofluorescence intensity images
- pre-process images
- physically isolate T cells based on activation prediction
- generate report
- compute activation status using convolutional neural network
- pre-train and fine-tune neural network
- train neural network with autofluorescence intensity images
- sort CD4+, CD3+, and/or CD8+ T cells
- provide accuracy of classifying T cells

### Systems

- introduce T cell sorting device
- describe cell analysis pathway
- describe single-cell autofluorescence image sensor
- describe processor and non-transitory computer-readable medium
- describe optional cell sorter and light source
- describe optional cell size measurement tool
- describe device operation

### Example 1

- introduce cell preparation and imaging
- describe cell isolation and culture
- explain NAD(P)H intensity image creation
- detail image acquisition parameters
- describe image processing pipeline
- segment cell images using CellProfiler
- filter out non-T cells and dim images
- pad and augment images
- implement nested cross-validation
- train and evaluate eight classifiers
- describe linear classifiers
- develop simple neural network classifiers
- train pre-trained CNN classifiers
- interpret pre-trained CNNs
- introduce dimension reduction
- motivate UMAP
- describe UMAP parameters
- apply UMAP to CNN features
- visualize UMAP results
- introduce saliency maps
- describe backpropagation
- describe guided backpropagation
- generate saliency maps
- interpret saliency maps
- introduce classification goal
- describe frequency classifier
- describe logistic regression models
- describe neural network models
- describe pre-trained CNN model
- describe cross-validation strategy
- present cross-validation results
- present results on new donor

## DISCUSSION

- demonstrate machine learning model accuracy
- compare CNN with logistic regression
- discuss fine-tuning pre-trained CNN layers
- analyze effect of fine-tuning more layers
- recommend fine-tuning last few layers
- discuss machine learning model recognition of image attributes
- interpret logistic regression model
- analyze saliency maps of CNN
- discuss limitations of model evaluation
- discuss misclassified images and image cropping quality
- suggest improving image segmentation approaches
- discuss feasibility of classifying T cells from autofluorescence images
- introduce T cell classifying device
- describe cell analysis pathway
- describe single-cell autofluorescence image sensor
- describe processor and non-transitory computer-readable medium
- describe instructions for processor
- describe optional pre-processing of autofluorescence intensity image
- describe determining if image is an outlier
- describe T cell classification device and method

