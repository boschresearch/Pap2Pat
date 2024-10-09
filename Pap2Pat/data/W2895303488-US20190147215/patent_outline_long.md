# DESCRIPTION

## TECHNICAL FIELD

- introduce whole cell segmentation

## BACKGROUND

- motivate cell imaging
- describe cell structure
- explain importance of cell analysis
- introduce high-resolution fluorescent microscopy
- describe advancement in computing capabilities
- explain development of image processing techniques
- define cell segmentation
- describe challenges in cell segmentation
- introduce whole cell segmentation process
- describe cell analysis workflow
- explain limitations of existing cell analysis workflows
- introduce two-channel whole cell segmentation
- describe limitations of two-channel whole cell segmentation
- introduce single channel whole cell segmentation
- describe limitations of existing single channel cell segmentation techniques

## SUMMARY

- introduce computer-implemented method
- describe model generation
- explain accessing model and sample image
- describe generating probability maps
- explain extracting binary nuclear mask and nuclei seeds map
- describe applying nuclei seeds to sample image
- summarize transforming sample image into segmented image

## DETAILED DESCRIPTION

- introduce in situ analysis
- describe benefits of whole cell segmentation

### System Overview

- introduce imaging system
- describe imager operation
- define biological sample
- describe system control circuitry
- describe data acquisition circuitry
- describe data processing circuitry
- describe operator workstation
- describe display and input devices
- describe network and communication interfaces
- describe multiple operator workstations
- describe remote image processing
- describe output metrics
- introduce computing apparatus
- describe computer readable medium
- describe processor-executable instructions
- describe memory and storage devices
- describe input/output devices
- describe user interface
- describe system components implementation

### Development of a Training Model

- introduce deep learning model
- describe network architecture
- describe training environment
- describe training process
- describe U-net architecture
- describe convolution and pooling steps
- describe loss function
- describe training data preprocessing
- describe training data augmentation

### Single Channel Whole Cell Segmentation Workflow

- illustrate single channel whole cell segmentation workflow
- provide input and transformed images
- transform sample image into cell probability map and nuclei probability map
- divide sample image into patches
- assign predicted labels to each pixel
- stitch patches to form full predicted image
- extract nuclei probability map and cell probability map
- generate binary nuclear mask from nuclei probability map
- identify nuclei with different sizes
- perform blob detection
- apply multi-level Laplacian of Gaussian filter
- apply multi-level thresholding
- assign binary value to each pixel
- extract binary nuclear mask
- transform binary nuclear mask into nuclei seeds map
- determine distance transform of binary nuclear mask
- apply extended h-minima transform
- extract regional minima
- apply seeded watershed transform
- extract nuclei seeds map
- perform cell enhancement transformation
- apply pixel-level weighting
- generate enhanced sample image
- perform cell delineation transformation
- apply nuclei seeds to sample image
- determine image background
- assign background labels
- apply seeded watershed segmentation
- identify and separate cells
- transform sample image into segmented image
- provide processor with improved capabilities
- solve technical challenges
- eliminate need for nuclei-specific cell marker stain
- maximize use of limited channels
- avoid toxic effect of nuclear cell marker stain
- provide significant technology improvements
- define nuclei-specific cell marker stain
- define non-nuclear cell marker stain
- provide examples of non-nuclear cell marker stains
- provide benefits of present disclosure

### Assessment of Segmentation Results

- perform quality control assessment
- generate cell segmentation quality score

### Examples

- introduce dataset
- describe experimental conditions
- explain use of fluorescent dyes
- describe image acquisition process
- specify image size and resolution
- explain selection of images for experiments
- illustrate example images
- introduce concept of ground truth segmentation
- explain process of generating training model
- describe automated ground truth segmentation
- explain semi-automated ground truth segmentation
- summarize three experiments
- introduce Experiment 1: Segmentation
- describe dataset division for Experiment 1
- explain evaluation of segmentation results
- illustrate segmentation results for Experiment 1
- apply cell segmentation similarity metric
- determine segmentation quality scores
- show histogram of cell-level segmentation quality scores
- introduce Experiment 2: Cross Validation
- describe 10-fold cross validation process
- assess Area Under Curve and Accuracy
- show results of cross validation experiment
- introduce Experiment 3: Model or Network Training
- describe model training process
- evaluate segmentation results for Experiment 3
- illustrate comparison of segmentation results
- summarize results and benefits of disclosed technique

