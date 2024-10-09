# DESCRIPTION

## FIELD

- relate to 3D reconstruction

## BACKGROUND

- limitations of standard 3D modeling methods

## SUMMARY

- outline computer-implemented method
- mention other aspects of disclosure

## DETAILED DESCRIPTION

### Overview

- introduce LASR pipeline for 3D shape reconstruction
- reconstruct models of rigid or nonrigid 3D shapes
- incorporate analysis-by-synthesis strategy
- forward-render silhouette, optical flow, and color images
- compare against video observations to adjust model parameters
- recover mesh of 3D model from one or more images
- build library of shape models from single set of images
- solve inverse graphics problem of recovering 3D object shape
- solve inverse graphics problem of recovering camera trajectories
- perform model-free approach for 3D shape learning
- obtain input image that depicts an object
- process input image with machine-learned camera model
- render image of object using differentiable rendering
- evaluate loss function to compare input and rendered images

### Example Devices and Systems

- introduce computing system for articulated shape reconstruction
- describe user computing device with processor and memory
- store 3D reconstruction models in user computing device
- describe server computing system with processor and memory
- store 3D reconstruction models in server computing system
- describe training computing system with processor and memory
- train 3D reconstruction models using training computing system
- describe model trainer with backwards propagation of errors
- train models based on set of training data
- personalize models based on user-specific data
- describe network for communication between devices
- illustrate example computing system with applications and machine learning library
- illustrate example computing device with central intelligence layer and machine-learned models

### Example Model Arrangements

- introduce 3D reconstruction pipeline with inverse graphics optimization

### Example Approach

- introduce analysis-by-synthesis task
- describe computing system steps
- outline optimization process

### Example Forward-Synthesis Model

- describe forward-synthesis model

### Example Deformation Modeling

- describe deformation modeling
- outline linear-blend skinning
- outline parametric skinning

### Example Self-Supervised Learning from a Video

- describe inverse graphics loss
- outline shape and motion regularization
- describe total loss function

### Example Implementation Details

- describe camera and pose implementation
- outline silhouette and flow measurements

### Example 2D Keypoint Transfer on Animal Videos

- introduce animal video dataset
- describe data derivation from video segmentation dataset
- define percentage of correct keypoint transfer (PCK-T)
- illustrate taxonomy of alternative methods for animal reconstruction
- describe LASR's ability to jointly recover camera, shape, and articulation
- show qualitative results of 3D shape reconstruction in FIG. 5
- compare LASR with UMR, A-CSM, and SMALify on bear and dog data
- show qualitative results of 3D shape reconstruction in FIG. 6
- present quantitative results of keypoint transfer in Table 2
- compare LASR with 3D reconstruction baselines
- show improvement of LASR compared to initial optical flow in FIG. 7
- describe example mesh reconstruction on articulated objects
- evaluate mesh reconstruction accuracy using video dataset
- describe bidirectional Chamfer distance as evaluation metric
- compare LASR with A-CSM, SMALify, UMR, SMPLify-X, VIBE, and PiFUHD
- show visual comparison on human and animals in FIG. 5 and FIG. 8
- present quantitative results in Table 3
- examine performance on arbitrary real-world objects
- compare LASR with COLMAP in FIG. 9
- investigate effect of different design choices in FIG. 10 and Table 4

## Additional Disclosure

- clarify flexibility of computer-based systems

