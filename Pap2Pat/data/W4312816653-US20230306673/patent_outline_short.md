# DESCRIPTION

## FIELD OF THE DISCLOSURE

- relate to 3D character rendering

## BACKGROUND

- discuss prior art in 3D character rendering

## SUMMARY

- introduce 3D character cloning method
- describe application in person re-identification
- outline UV map generation method
- summarize 3D character rendering method

## DETAILED DESCRIPTION

- describe computing device hardware and software structures

### A. COMPUTING DEVICE HARDWARE AND SOFTER STRUCTURES

- introduce computing device components
- describe processing structure
- describe controlling structure
- describe memory and storage
- describe input/output interfaces

### B. HUMANOID RENDERING

- introduce humanoid rendering
- describe 3D humanoid structure and rendering
- describe clothing rendering
- introduce clothing-clone method
- describe homogeneous expansion method
- describe registered clothing-mapping method

### C. POSE DETECTION AND PERSON-VIEW QUALIFICATION

- detect person image using person-detection model
- estimate person pose using HRNet model
- classify person view based on keypoints and aspect ratio

### D. REGISTERED MAPPING METHOD

- map clothing texture to UV-map template using perspective homography
- generate first UV map using registered mapping method

### E. HOMOGENEOUS EXPANSION

- segment homogeneous area from clothing image
- expand homogeneous area to fill rear-view clothing area
- fill background area using homogeneous expansion method

### F. SIMILARITY-DIVERSITY EXPANSION

- introduce similarity-diversity expansion method
- describe clustering and sampling process
- motivate application in person re-identification
- describe various embodiments and extensions

