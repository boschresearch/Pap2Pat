# DESCRIPTION

## FIELD OF THE DISCLOSURE

- relate to 3D character rendering

## BACKGROUND

- introduce 3D character generation
- limitations of existing methods

## SUMMARY

- motivate 3D character cloning
- introduce computerized method
- generate UV map
- render 3D character
- determine keypoints
- generate UV map using homography
- determine homogeneous block
- cluster and sample images

## DETAILED DESCRIPTION

- describe computing device hardware and software structures
- introduce humanoid rendering using application programs

### A. COMPUTING DEVICE HARDWARE AND SOFTER STRUCTURES

- introduce computing device
- describe processing structure
- describe controlling structure
- describe memory
- describe network interface
- describe input interface
- describe output interface
- describe other components
- describe system bus
- describe software architecture

### B. HUMANOID RENDERING

- introduce humanoid rendering
- describe 3D humanoid structure
- describe rendering process
- introduce clothing-clone method
- introduce homogeneous expansion method
- introduce registered clothing-mapping method
- describe process for cloning clothing image
- describe training subprocess
- describe rendering subprocess
- describe clothing & keypoint detection models
- describe UV-map templates
- describe generating UV map
- describe rendering 3D humanoid

### C. POSE DETECTION AND PERSON-VIEW QUALIFICATION

- detect person image using person-detection model
- crop and use for pose detection
- use person-pose estimation model for automatic pose estimation
- identify and exclude rear-view, side-view, and occluded images
- process person image to remove background content
- classify person image into front view, side view, rear view, or occluded view

### D. REGISTERED MAPPING METHOD

- apply nonoccluded front-view person image to clothing & keypoint detection models
- output annotated person image with clothing type, position, and keypoints
- select UV-map template based on clothing type
- use registered mapping method to generate front-view clothing area of UV map
- use perspective warping method to map each pixel of person image to UV-map template

### E. HOMOGENEOUS EXPANSION

- use cloth segmentation step to obtain realistic clothing cell
- use optimization method to find homogeneous area on clothing
- compute standard deviation of feature values within each block
- define ratio as objective function for optimization
- scale realistic clothing cell to align with front-view clothing area
- expand scaled clothing cell to fill rear-view clothing area

### F. SIMILARITY-DIVERSITY EXPANSION

- introduce similarity-diversity expansion method
- apply DBSCAN for clustering person images
- sample images per cluster and clone clothings
- generate similar and diverse characters
- use strategies for creating characters
- apply in person re-identification applications
- clone clothings from real-world person images
- describe computer network system for performing methods

