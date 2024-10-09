# DESCRIPTION

## TECHNICAL FIELD

- relate to novel view and unseen pose synthesis

## BACKGROUND

- motivate NeRF and its limitations

## SUMMARY OF PARTICULAR EMBODIMENTS

- introduce improved method for novel view and unseen pose synthesis
- describe integration of observations across frames
- summarize benefits of improved method

## DESCRIPTION OF EXAMPLE EMBODIMENTS

- motivate 3D human digitization
- introduce NeRF-based models
- propose improved NeRF-based model

### Training of Improved NeRF-Based Model

- illustrate overall training process
- generate appearance code
- generate pose code
- generate view & spatial code
- feed codes into density and color model
- compare generated color and density with ground-truth image
- update model based on comparison
- generate 3D feature volumes for pose code
- integrate features using temporal transformer
- derive NeRF-based model equations
- describe multi-head self-attention mechanism
- outline training process for improved NeRF-based model
- specify training data and objective function

### Testing of Improved NeRF-Based Model

- describe testing process of improved NeRF-based model
- generate novel view and unseen pose synthesis

### Example Test Results of Improved NeRF-based Model

- compare outputs of improved NeRF-based model and prior NeRF-based model
- illustrate fine-level details in output images
- compare outputs across various poses, viewpoints, and subjects
- discuss limitations of prior NeRF-based model
- illustrate effect of using appearance code and temporal transformer

### Example Method

- access image frame and depth information
- generate first latent representation based on point cloud
- access sequence of image frames and key frames
- generate second latent representation based on tracking and combining temporal relationship
- access camera parameters and generate third latent representation
- train improved NeRF-based model for free-viewpoint rendering

### Example Computer System

- describe computer system architecture
- introduce processor and its functionality
- describe memory and its functionality
- describe storage and its functionality
- introduce input/output interface and its functionality
- introduce communication interface and its functionality
- describe bus and its functionality

