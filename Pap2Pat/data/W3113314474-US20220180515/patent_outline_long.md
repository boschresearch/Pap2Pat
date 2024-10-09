# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce leukocyte function
- motivate abnormal leukocyte counts
- describe cytometry techniques
- limitations of antibody labeling
- introduce label-free imaging methods
- describe Raman imaging
- introduce quantitative phase microscopy
- summarize QPM applications
- motivate AI-enabled QPM

## BRIEF SUMMARY OF THE INVENTION

- introduce AIRFIHA system

## DETAILED DISCLOSURE OF THE INVENTION

- define ranges
- define "reduction" and "increase"
- define "comprising", "consisting of", and "consisting essentially of"
- define "or" and "a", "and", "the"
- define "about"
- introduce sample preparation
- describe blood sample collection
- describe sample preparation for leukocyte analysis
- describe leukocyte isolation techniques
- describe flow cytometry for purity confirmation
- describe cell counting and suspension
- describe fluorophore-conjugated antibody addition
- prepare leukocytes for quantitative phase imaging
- describe sample preparation for imaging
- introduce diffraction phase microscopy
- describe quantitative phase microscopy methods
- describe diffraction phase microscopy system
- describe laser illumination
- describe objective lens selection
- describe sample beam processing
- describe diffraction grating and 4f system
- describe interferogram formation
- describe phase image processing
- describe phase retrieval and segmentation
- describe Fourier transform and bandpass filtering
- describe signal shift and inverse Fourier transform
- describe calibration and phase map calculation
- describe phase unwrapping and flattening
- describe cell segmentation algorithm
- describe thresholding and Gaussian filtering
- describe watershed segmentation and contour expansion
- describe cell phase map resizing
- introduce classification model training
- describe artificial neural network construction
- describe residual neural network framework
- describe multiple-step classification routine
- describe first ResNet for monocyte-granulocyte-lymphocyte classification
- describe second ResNet for B-T lymphocyte classification
- describe additional ResNets for granulocyte classification
- describe batch normalization and Rectified Linear Unit activation
- describe average pooling and flatten layer
- describe dense layer and Softmax activation
- describe probability calculation for leukocyte classification
- describe data cleaning and outlier removal
- describe tuning of neural network using precision-recall curve and F1 score
- describe applications of the subject methods

### Materials and Methods

- procure fresh blood samples
- isolate leukocytes from fresh blood
- describe isolation kits used
- outline immunomagnetic negative selection process
- detail phosphate-buffered saline preparation
- perform leukocyte isolation
- resuspend isolated leukocytes in PBS
- perform flow cytometry analysis
- check leukocyte viability with AO/PI staining
- count and resuspend leukocytes
- add fluorophore-conjugated antibody to leukocytes
- incubate and wash leukocytes
- prepare leukocyte samples for quantitative phase imaging
- add DNase solution to isolated cells
- sandwich leukocyte suspension between quartz coverslips
- train classification model
- obtain phase maps of leukocytes
- resize phase maps for network input
- describe training process with 5-fold cross-validation
- outline hyper-parameter tuning and model selection

### EXAMPLES

- introduce AIRFIHA system
- describe QPM system configuration
- explain imaging resolution and field of view
- describe leukocyte sample preparation
- motivate neural network for classification
- describe phase image dataset construction
- illustrate AIRFIHA system workflow
- describe neural network architecture
- motivate cascaded ResNet structure
- describe ResNet-10 architecture
- explain batch normalization and activation functions
- describe output layer and Softmax activation
- motivate fine-tuning for CD4 and CD8 classification
- describe training and validation of classification model
- evaluate classification results using recall, precision, and F1 score
- describe precision-recall curves
- visualize feature vectors using t-SNE
- compare ResNet with PCA method
- visualize output features of convolutional layers
- analyze classification errors
- determine optimal number of cells for training
- describe potential applications in immunodeficiency disease monitoring
- motivate label-free differentiation of CD4 and CD8 cells
- evaluate CD4 and CD8 classification results
- visualize feature vectors using t-SNE for CD4 and CD8 cells
- describe cross-donor and intra-donor validation experiments
- analyze distribution differences between donors
- evaluate classification results for cross-donor validation
- evaluate classification results for intra-donor validation
- describe importance of accurate separation kits
- motivate data cleaning to remove outliers
- describe data cleaning methods
- evaluate classification results after data cleaning
- compare results with other reported methods
- describe potential improvements using synthetic aperture phase imaging
- describe potential improvements using deconvolution
- describe potential improvements using 3D-resolved phase maps
- motivate expanding dataset and upgrading neural network model
- describe potential applications in disease diagnosis
- conclude with scope of invention

