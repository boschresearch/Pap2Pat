# DESCRIPTION

## STATEMENT REGARDING FEDERALLY FUNDED RESEARCH

- disclose government funding

## BACKGROUND

- motivate CAR T cell therapy

## SUMMARY

- describe T cell classifying device
- outline methods for T cell activation state

## DETAILED DESCRIPTION

- define terminology and scope
- describe various aspects of the invention

### Methods

- introduce method of sorting T cells
- describe acquiring autofluorescence intensity images
- describe optional pre-processing and physically isolating T cells
- describe generating a report and computing activation status
- describe training and fine-tuning convolutional neural network

### Systems

- introduce T cell sorting device
- describe components of the device
- describe operation of the device

### Example 1

- describe cell preparation and imaging
- summarize image processing pipeline
- outline nested cross-validation scheme
- introduce linear classifiers
- motivate simple neural network classifiers
- describe pre-trained CNN classifiers
- interpret pre-trained CNNs
- motivate dimension reduction
- describe UMAP algorithm
- apply UMAP to CNN features
- introduce saliency maps
- describe classification approaches
- evaluate classification models
- perform cross-validation across donors
- confirm generalization with new donor
- interpret pre-trained CNN with fine-tuning

## DISCUSSION

- demonstrate machine learning model accuracy
- compare fine-tuning CNN with off-the-shelf CNN
- analyze effect of fine-tuning more layers
- discuss limitations of fine-tuning all layers
- recommend fine-tuning last few layers
- recognize image attributes reflecting biological domain knowledge
- interpret logistic regression model
- analyze saliency maps of fine-tuned CNN
- discuss limitations of assessing statistical significance
- identify limitations of image cropping quality

