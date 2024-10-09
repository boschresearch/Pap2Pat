# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior publication

## BACKGROUND

- introduce whole slide images
- motivate stain normalization
- limitations of prior stain normalization methods

## SUMMARY

- outline computer-implemented method
- describe computerized system
- describe computer program product

## DETAILED DESCRIPTION

- introduce normalization method for medical images

### 1. General Embodiments and High-Level Variants

- describe computer-implemented method for normalizing medical images
- introduce whole slide images (WSIs) and slide scanner
- define present methods and system
- estimate actual quantities for each image
- compute stain vectors and maximum stain concentrations
- assess quality of actual quantities
- compare actual quantities to reference quantities
- select effective quantities for each image
- normalize images based on effective quantities
- describe advantages of present methods
- impose same staining process for images
- obtain images and compute RGB histogram
- identify artifacts and filter out image portions
- compute stain concentrations and maximum concentrations
- select effective quantities and normalize images
- describe variants of present methods
- compute maximum concentrations as robust maxima
- use boundary values to define good-quality and bad-quality images
- estimate reference quantities for good-quality images
- update reference data as images are processed
- assess actual quantities using distance metrics
- select reference quantities if distance is larger than threshold
- use boundary values to assess actual quantities
- skip estimation of actual quantities for residual subset of images
- perform cognitive treatment on normalized images

### 2. Specific Embodiments—Technical Implementation Details

- introduce stain normalization system
- describe Macenko's normalization method
- detail system architecture
- explain multi-core implementation
- discuss system-level optimizations
- describe processing of high-resolution images
- detail image format support
- describe method to detect poor-quality images
- explain normalization of poor-quality images
- describe application to ML pipelines
- detail CNN model training
- describe inference to predict tumor presence
- introduce computerized units
- describe non-interactive and automated methods
- explain software implementation
- detail hardware architecture
- describe processor and memory components
- explain input/output controller and peripherals
- describe network interface and transceiver
- detail network implementation
- introduce computer program products
- describe computer readable storage medium
- explain computer readable program instructions
- detail downloading and execution of instructions
- describe flowchart and block diagram illustrations
- explain cloud computing infrastructure
- describe deployment models

