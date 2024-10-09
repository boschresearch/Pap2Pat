# DESCRIPTION

## TECHNICAL FIELD

- introduce whole cell segmentation

## BACKGROUND

- motivate cell imaging
- describe cell segmentation
- limitations of existing techniques
- describe two-channel whole cell segmentation
- motivate single channel whole cell segmentation
- describe existing single channel techniques
- limitations of existing single channel techniques

## SUMMARY

- introduce computer-implemented method
- describe method steps
- introduce computer system

## DETAILED DESCRIPTION

- introduce in situ analysis of cells

### System Overview

- describe imaging system 10
- introduce imager 12 and its functions
- describe system control circuitry 16
- introduce data acquisition circuitry 18
- describe data processing circuitry 20
- introduce operator workstation 22
- describe computer 24 and its components
- introduce I/O and communication interfaces
- describe remote access and processing capabilities

### Development of a Training Model

- introduce deep learning model for whole cell segmentation
- describe network architecture and training process
- introduce loss function and its components
- describe training data and preprocessing steps

### Single Channel Whole Cell Segmentation Workflow

- illustrate single channel whole cell segmentation workflow
- preprocess sample image
- divide sample image into patches
- assign predicted labels to each pixel
- stitch patches to form full predicted image
- extract nuclei probability map and cell probability map
- generate binary nuclear mask from nuclei probability map
- identify nuclei with different sizes
- apply multi-level thresholding to identified nuclei
- assign binary value to each pixel
- extract binary nuclear mask
- transform binary nuclear mask into nuclei seeds map
- determine distance transform of binary nuclear mask
- apply extended h-minima transform
- extract regional minima
- apply seeded watershed transform
- extract nuclei seeds map
- enhance sample image using cell probability map
- apply seeded watershed segmentation to enhanced sample image
- generate segmented image with delineated cellular and/or subcellular regions

### Assessment of Segmentation Results

- perform quality control assessment using cell segmentation similarity metric

### Examples

- introduce dataset
- describe experimental conditions
- motivate automated ground truth segmentation
- describe semi-automated ground truth segmentation
- summarize experiment 1
- describe segmentation results of experiment 1
- evaluate segmentation quality of experiment 1
- summarize experiment 2
- describe cross-validation results of experiment 2
- summarize experiment 3
- describe model training of experiment 3
- evaluate segmentation quality of experiment 3
- illustrate comparison of segmentation results
- conclude improved technical solutions

