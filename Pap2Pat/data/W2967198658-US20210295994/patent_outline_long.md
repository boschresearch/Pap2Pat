# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior publication

## BACKGROUND

- introduce whole slide images
- describe digital pathology
- motivate machine learning
- explain stain normalization
- describe limitations of prior art
- highlight need for automated pipelines
- summarize importance of stain normalization

## SUMMARY

- introduce computer-implemented method
- estimate actual quantities
- assess actual quantities
- select effective quantities
- normalize images
- describe computerized system and program product

## DETAILED DESCRIPTION

- introduce normalization method for medical images

### 1. General Embodiments and High-Level Variants

- describe computer-implemented method for normalizing medical images
- introduce whole slide images (WSIs) as obtained with a slide scanner
- describe method steps, including estimating actual quantities and assessing quality
- introduce reference quantities and effective quantities
- describe normalization step based on effective quantities
- discuss advantages of proposed method
- introduce variants of the method
- describe computing RGB histogram to identify artifacts
- discuss limitations of prior art
- describe estimating actual quantities, including stain vectors and maximum stain concentrations
- describe assessing quality of actual quantities
- describe selecting effective quantities based on quality assessment
- describe normalizing images based on effective quantities
- discuss using reference quantities in normalization
- describe computing stain concentrations and maximum stain concentrations
- discuss using robust maxima of pixel stain concentrations
- describe selecting reference images for dataset
- describe estimating reference quantities for reference images
- describe obtaining reference data based on reference quantities
- describe using boundary values to define good-quality and bad-quality images
- describe assessing quality of actual quantities based on boundary values
- describe selecting effective quantities based on boundary values
- describe normalizing images based on effective quantities
- discuss using distance metrics to assess quality of actual quantities
- describe comparing actual quantities to reference quantities
- describe selecting effective quantities based on comparison
- describe normalizing images based on effective quantities
- discuss using mean or median values of actual H & E vectors
- describe selecting effective quantities based on mean or median values
- describe normalizing images based on effective quantities
- discuss using metadata to update reference data
- describe updating reference data based on outcomes of quality assessment
- describe skipping estimation of actual quantities for residual subset of images
- describe selecting reference quantities by default for residual subset of images
- describe normalizing images based on reference quantities
- discuss using cognitive algorithm on normalized images
- describe training convolutional neural network (CNN) model
- describe using CNN model for image analysis
- discuss benefits of proposed method for machine learning pipeline
- describe variants of the method
- discuss using different staining processes
- describe using different types of medical images
- discuss using different normalization techniques
- describe using different cognitive algorithms
- discuss using different machine learning models
- describe using different types of datasets
- discuss using different types of metadata
- describe using different types of storage means
- discuss using different types of processing means
- describe using different types of computerized systems

### 2. Specific Embodiments—Technical Implementation Details

- introduce stain normalization system
- describe Macenko's normalization method
- explain SVD approach
- discuss simplicity of algorithmic steps
- describe optimized multi-core implementation
- explain system-level optimizations
- discuss processing high-resolution images
- describe different image formats
- detect poor-quality images
- normalize images with artifacts
- increase accuracy of ML pipelines
- describe CNN for tumor detection
- normalize full images
- store normalized images
- pipeline with ML engine
- train CNN model
- predict tumor presence
- introduce computerized units
- describe non-interactive and automated methods
- implement in software or hardware
- execute by digital processing devices
- describe general-purpose digital computers
- introduce computerized unit 101
- describe hardware architecture
- explain processor and memory
- describe input/output devices
- discuss network interface
- describe IP-based network
- explain managed IP network
- introduce BIOS
- execute software stored in memory
- communicate data to and from memory
- control operations of computer
- read and execute methods
- store on computer readable medium
- describe computer program products
- introduce computer readable storage medium
- explain tangible device
- list examples of storage medium
- download instructions from network
- execute on computer or device
- implement functions and acts
- describe flowchart and block diagrams
- explain modules and segments
- discuss executable instructions
- describe special purpose hardware
- introduce cloud computing infrastructure
- define cloud computing
- describe on-demand self-service
- explain broad network access
- discuss resource pooling
- describe rapid elasticity
- explain measured service
- introduce service models and deployment models

