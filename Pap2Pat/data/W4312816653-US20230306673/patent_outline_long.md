# DESCRIPTION

## FIELD OF THE DISCLOSURE

- relate to 3D character rendering

## BACKGROUND

- introduce 3D character generation
- motivate limitations of existing methods
- summarize MakeHuman method
- summarize SMPL model method
- summarize texture transfer models

## SUMMARY

- introduce embodiments
- motivate computer graphics application
- describe computerized method
- generate UV map
- render 3D character
- determine keypoints
- generate UV map using keypoints
- determine homography matrix
- determine texture using homography
- interpolate textures
- determine homogeneous block
- render UV map using block
- scale and tile block
- cluster images
- sample clusters
- render 3D characters
- describe apparatus and storage devices

## DETAILED DESCRIPTION

- introduce computing devices and computer network systems
- describe hardware structures of computing devices
- describe software architecture of computing devices
- introduce application programs for establishing and rendering 3D human-like characters

### A. COMPUTING DEVICE HARDWARE AND SOFTER STRUCTURES

- introduce computing device hardware
- describe processing structure
- describe controlling structure
- describe memory
- describe network interface
- describe input interface
- describe output interface
- describe other components
- describe system bus
- describe processing structure components
- describe controlling structure components
- describe memory components
- describe network interface components
- describe input interface components
- describe output interface components
- describe other components
- describe system bus components
- illustrate computing device hardware
- illustrate software architecture
- describe application programs

### B. HUMANOID RENDERING

- introduce humanoid rendering
- describe establishing 3D human-like characters
- describe rendering 3D human-like characters
- illustrate 3D human-like characters
- describe rendering process
- describe clothing-clone method
- describe homogeneous expansion method
- describe registered clothing-mapping method
- describe combining methods
- describe executing process for cloning clothing image
- describe generating UV map
- describe using UV map for rendering
- describe training subprocess
- describe rendering subprocess
- describe training clothing images
- describe clothing & keypoint detection models
- describe clothing types and UV-map templates
- illustrate clothing image and UV-map template
- illustrate clothing images and UV-map templates
- describe keypoints on clothing image
- describe training clothing & keypoint detection models
- describe using trained models for rendering
- describe detecting person and pose
- describe detecting clothing and keypoints
- describe generating UV map for rendering
- describe rendering 3D humanoid
- describe generating synthesized images

### C. POSE DETECTION AND PERSON-VIEW QUALIFICATION

- detect person image using person-detection model
- crop person image for pose detection
- use HRNet model for automatic person pose estimation
- identify rear-view images based on shoulder keypoints
- identify side-view images based on width-to-height aspect ratio
- identify occluded front-view images based on hand and elbow keypoints
- expand upper-body and lower-body areas to determine occlusion
- classify person image into front view, side view, rear view, or occluded view
- accept front view as qualified person image
- reject side view, rear view, and occluded view
- define upper-body and lower-body areas using keypoints
- expand areas to check for occlusion

### D. REGISTERED MAPPING METHOD

- apply nonoccluded front-view person image to clothing & keypoint detection models
- output annotated person image with clothing type, position, and keypoints
- select UV-map template based on clothing type
- use registered mapping method to generate front-view clothing area
- define perspective homography to map real-world clothing texture to UV-map template
- calculate homography matrix by solving optimization problem
- refine homography matrix using Levenberg-Marquardt method
- use perspective warping method to map each pixel of person image to UV-map template
- traverse pixels of UV-map template to obtain texture values
- generate front-view clothing area of first UV map

### E. HOMOGENEOUS EXPANSION

- use homogeneous expansion method to render rear-view clothing area
- segment cloth to obtain realistic clothing cell
- extract feature map of clothing image using neural network model
- define square blocks on feature map as candidates for homogeneous area
- compute average and standard deviation of feature values within each block
- optimize objective function to select block with best trade-off between homogeneous and large areas
- locate and crop selected block to obtain realistic clothing cell
- scale clothing cell to align with front-view clothing area
- expand clothing cell to fill rear-view clothing area
- fill background area of UV-map template using homogeneous expansion method
- identify homogeneous area of clothing image
- obtain clothing cell from homogeneous area
- generate second UV map for lower-body clothing

### F. SIMILARITY-DIVERSITY EXPANSION

- introduce similarity-diversity expansion method
- motivate clustering person images
- apply DBSCAN for clustering
- sample images per cluster
- clone clothings for 3D humanoid rendering
- use clothing & keypoint detection models for feature extraction
- compute similarity scores for clustering
- iteratively apply DBSCAN with different eps parameters
- remove duplicated person images
- select images for character generation
- create characters with different UV maps
- discuss application in person re-identification
- motivate using synthetic person re-identification datasets
- clone entire clothings from real-world person images
- generate 3D characters with clear and sharp clothing textures
- discuss various embodiments of character generation
- describe computer network system for performing methods

