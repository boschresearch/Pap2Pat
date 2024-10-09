# DESCRIPTION

## BACKGROUND

- introduce computer vision in retail settings
- describe limitations of current object detectors

## SUMMARY

- disclose system and method for object detector with non-AABB regions

## DETAILED DESCRIPTION

- develop quadrilateral training dataset
- describe features of quadrilateral training dataset
- collect images from multiple sources
- annotate products with quadrilateral bounding boxes
- split dataset into training, validation, and testing sets
- design quadrilateral detector
- extend localization subnet to output quadrilateral boxes
- describe base network architecture
- define quadrilateral ground-truth assignment strategy
- calculate quad-centerness
- describe cross-pyramid assignment strategy
- introduce soft scale assignment strategy
- describe corner refinement module
- define losses for training
- describe two-stage testing process
- discuss additional losses for corner refinement module

### Alternate Embodiments

- describe elliptical or circle bounding shape
- describe triangular bounding shape
- describe 3D bounding boxes with arbitrary poses

