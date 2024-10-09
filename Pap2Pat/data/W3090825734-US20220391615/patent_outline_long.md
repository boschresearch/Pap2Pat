# DESCRIPTION

## FIELD OF INVENTION

- relate to agricultural technology and AI

## BACKGROUND

- introduce FCN for classification
- describe limitations of FCN for segmentation
- motivate use of dilated convolutions
- discuss YOLO and Mask R-CNN for instantiation
- describe R-CNN and its limitations
- introduce Mask R-CNN for pixel-wise segmentation

## SUMMARY OF THE INVENTION

- introduce plants analysis apparatus
- describe Mask R-CNN for object detection
- motivate mapping module for cell division
- describe output device for displaying results
- introduce method for computer analysis
- describe object detection using Mask R-CNN
- motivate object segmentation using pixel-level binary classification
- describe anchor box generation
- compare anchor boxes with ground truth bounding boxes
- select best-matching anchor boxes
- describe polygonal Non-Maximum Suppression algorithm
- feed different model parameters for different vegetables
- describe detection layer outputting regions of interest
- output pixel-level masks for each vegetable
- describe orthomosaicking procedure
- display results in map form

## DETAILED DESCRIPTION

- introduce UAV raw images
- define UAV flight metadata
- specify field boundaries
- describe orthomosaicking module
- split orthomosaic into non-overlapping images
- introduce Mask R-CNN algorithm
- describe Mask R-CNN parameters
- feed parameters into Mask R-CNN algorithm
- perform post-processing on Mask R-CNN output
- display output of post-processing module
- describe operation of UAV raw images and UAV flight metadata
- describe operation of orthomosaicking module
- describe operation of Mask R-CNN algorithm
- describe operation of post-processing module
- illustrate Mask R-CNN architecture
- describe images input to Mask R-CNN algorithm
- describe backbone network for visual feature extraction
- describe feature maps output from backbone
- describe region proposal network (RPN)
- describe anchor boxes for RPN
- describe RPN targets for training RPN
- describe proposal layer for filtering RPN output
- describe training path for Mask R-CNN
- describe detection target layer for filtering ROIs
- describe FPN classifier for object classification
- describe FPN mask graph for object segmentation
- describe inference path for Mask R-CNN
- describe FPN classifier for object classification in inference path
- describe detection layer for filtering proposals
- describe FPN mask graph for object segmentation in inference path
- describe challenges of using Mask R-CNN for plant counting and sizing
- describe need for fine-tuning Mask R-CNN parameters
- describe input images to backbone network
- describe feature maps output from backbone
- describe RPN targets for training RPN
- describe anchor box generation
- describe IoU calculation for anchor box filtering
- describe RPN training process
- describe proposal layer for filtering RPN output
- describe importance of fine-tuning Mask R-CNN parameters
- describe Mask R-CNN architecture
- detail FPN Classifier Graph
- explain Detection Layer block
- describe FPN Mask Graph
- discuss loss functions
- introduce Adam optimiser
- highlight importance of dataset size
- describe pre-training on COCO dataset
- discuss fine-tuning on smaller dataset
- explain parametrization setup of Mask R-CNN
- describe optimising ROI selection
- discuss pixel size and imagery resolution
- describe orthomosaicking process
- reconstruct flight path of UAV
- find raw images within field boundaries
- estimate field coverage percentage
- determine overlapping pairs of images
- run orthomosaicking software
- concatenate object masks
- perform gridded lettuce mask process
- measure lettuce positioning and size
- calculate total number of lettuces
- obtain lettuce size statistics
- generate colour-coded grid
- describe application layer process
- generate map for chemical application
- determine average size of lettuces in cell
- set Apply_Chemical parameter
- output colour-coded grid
- describe computer system architecture
- detail user input interface
- describe display interface
- explain main memory and secondary memory
- discuss communications interface
- describe software and firmware implementation
- discuss computer programs and model training data
- highlight scope of the invention

