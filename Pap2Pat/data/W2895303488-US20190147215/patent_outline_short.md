# DESCRIPTION

## TECHNICAL FIELD

- introduce whole cell segmentation

## BACKGROUND

- motivate cell segmentation
- limitations of existing techniques
- need for single channel whole cell segmentation

## SUMMARY

- describe single channel whole cell segmentation method

## DETAILED DESCRIPTION

- describe in situ analysis and whole cell segmentation

### System Overview

- introduce imaging system
- describe imager and system control circuitry
- explain data acquisition and processing
- outline operator workstation and display

### Development of a Training Model

- motivate deep learning model for whole cell segmentation
- describe training model architecture and process

### Single Channel Whole Cell Segmentation Workflow

- illustrate single channel whole cell segmentation workflow
- preprocess sample image
- transform sample image into cell probability map and nuclei probability map
- extract binary nuclear mask from nuclei probability map
- transform binary nuclear mask into nuclei seeds map
- perform cell enhancement transformation (optional)
- perform cell delineation transformation
- extract segmented image with one or more cells identified with delineated nuclei and cytoplasm regions
- perform quality control assessment of segmentation results
- provide quality score based on cell segmentation similarity metric

### Assessment of Segmentation Results

- perform quality control assessment of segmentation results

### Examples

- introduce dataset and experimental conditions
- describe automated ground truth segmentation
- describe semi-automated ground truth segmentation
- summarize Experiment 1: Segmentation
- summarize Experiment 2: Cross Validation
- summarize Experiment 3: Model or Network Training
- conclude with results and benefits of segmentation technique

