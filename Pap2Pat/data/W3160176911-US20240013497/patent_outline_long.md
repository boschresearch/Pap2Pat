# DESCRIPTION

## FIELD

- relate to 3D reconstruction

## BACKGROUND

- introduce 3D modeling
- limitations of standard methods

## SUMMARY

- introduce method for 3D object shape
- process input image with camera model
- evaluate loss function
- modify camera model and mesh model

## DETAILED DESCRIPTION

### Overview

- introduce 3D shape reconstruction
- describe LASR pipeline
- define analysis-by-synthesis strategy
- describe forward-rendering of images
- compare rendered images with video observations
- adjust internal parameters of model
- recover mesh of 3D model
- describe machine-learned mesh model
- describe machine-learned camera model
- evaluate loss function
- describe loss function evaluation
- include camera pose in loss function
- include rotations of bones in loss function
- include vertex 3D coordinates in loss function
- describe motion regularization terms
- describe shape regularization terms
- describe polygon mesh
- describe linear blend skinning algorithm
- describe learnable joints and blend skinning weights
- describe object-to-camera transformation
- describe convolutional neural network
- describe camera pose estimation
- describe camera extrinsics prediction
- describe intrinsic camera parameters
- describe dynamics of skeleton sharing
- describe keypoint constraints
- describe shape template priors
- summarize technical effects and benefits

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- describe server computing system 130
- describe training computing system 150
- describe network 180
- describe user computing device components
- describe 3D reconstruction models 120
- describe machine-learned models
- describe neural networks
- describe model implementation
- describe user input component 122
- describe server computing system components
- describe 3D reconstruction models 140
- describe model training
- describe training computing system components
- describe model trainer 160
- describe training data 162
- describe backwards propagation of errors
- describe truncated backpropagation through time
- describe generalization techniques
- describe model personalization
- describe network communication
- describe alternative computing system arrangements
- describe FIG. 1B components
- describe application communication
- describe central intelligence layer

### Example Model Arrangements

- describe 3D reconstruction pipeline 200

### Example Approach

- introduce analysis-by-synthesis task
- input monocular video into computing system
- solve inverse graphics problem to recover object shape and motion
- forward-render texture, optical flow, and silhouette images
- evaluate loss function to generate gradients
- update camera, shape, and articulation parameters using gradient descent

### Example Forward-Synthesis Model

- forward-render texture, optical flow, and silhouette images
- synthesize measurements of frame pair
- represent object shape as mesh with colored vertices and fixed topology

### Example Deformation Modeling

- construct deformation modeling of object
- leverage linear-blend skinning and parametric skinning
- analyze number of unknowns and constraints
- model deformation as per-vertex motion
- constrain vertex motion by blending bone transformations
- learn skinning weights and time-varying bone transformations jointly

### Example Self-Supervised Learning from a Video

- exploit rich supervision signals from dense optical flow and raw pixels
- leverage shape and motion regularizers
- define inverse graphics loss
- compute silhouette loss, texture loss, and optical flow loss
- apply shape and motion regularization
- leverage soft-symmetry constraints
- apply canonicalization term

### Example Implementation Details

- leverage camera and poses for implementation details
- parameterize time-varying parameters as predictions from convolutional network
- leverage silhouette and flow measurements
- utilize coarse-to-fine reconstruction strategy
- initialize rest shape and rest bones

### Example 2D Keypoint Transfer on Animal Videos

- introduce animal video dataset
- describe data derivation
- explain PCK-T metric
- illustrate taxonomy of alternative methods
- describe SMALST model-based regressor
- describe UMR category-specific shape estimator
- describe A-CSM category-specific canonical surface mapping
- describe SMALify model-based optimization approach
- describe OJA detection-based method
- illustrate example qualitative results of 3D shape reconstruction
- compare LASR with UMR-horse
- compare LASR with A-CSM (camel template)
- compare LASR with SMALify horse
- illustrate shape reconstruction results from LASR
- illustrate shape reconstruction results from UMR-horse
- illustrate shape reconstruction results from A-CSM (camel template)
- illustrate shape reconstruction results from SMALify horse
- illustrate shape reconstruction results from LASR (humanoid figure)
- illustrate shape reconstruction results from PIFuHD
- illustrate shape reconstruction results from SMPLify-X
- illustrate shape reconstruction results from VIBE
- describe LASR's ability to jointly recover camera, shape, and articulation
- illustrate example qualitative results of 3D shape reconstruction (bear and dog data)
- compare LASR with UMR on bear and dog data
- compare LASR with A-CSM on bear and dog data
- compare LASR with SMALify on bear and dog data
- illustrate shape reconstruction results from LASR (bear and dog data)
- illustrate shape reconstruction results from UMR horse
- illustrate shape reconstruction results from A-CSM (wolf template)
- illustrate shape reconstruction results from SMALify dog
- describe quantitative results of keypoint transfer
- compare LASR with 3D reconstruction baselines
- compare LASR with detection-based methods
- illustrate example keypoint transfers between frames
- describe LASR's improvement compared to initial optical flow
- describe mesh reconstruction accuracy evaluation
- describe bidirectional Chamfer distance metric
- compare LASR with A-CSM, SMALify, and UMR for animal reconstruction
- compare LASR with SMPLify-X, VIBE, and PiFUHD for human reconstruction
- describe visual comparison on human and animals
- describe quantitative results of mesh reconstruction

## Additional Disclosure

- discuss system flexibility
- clarify non-limiting examples
- allow for variations

