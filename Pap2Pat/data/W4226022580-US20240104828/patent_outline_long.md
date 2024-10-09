# DESCRIPTION

## TECHNICAL FIELD

- relate to novel view and unseen pose synthesis

## BACKGROUND

- introduce NeRF
- motivate novel-view synthesis
- limitations of NeRF-based models
- describe NeuralBody
- identify need for improved method

## SUMMARY OF PARTICULAR EMBODIMENTS

- introduce improved method
- integrate observations across frames
- encode appearance at each frame
- learn shared latent codes
- learn appearance-dependent code
- integrate pose code and appearance code
- utilize temporal transformer
- recover non-visible regions
- generate three codes at training iteration
- encode appearance information
- encode pose information
- encode camera pose information
- feed codes into density and color model
- update NeRF-based model

## DESCRIPTION OF EXAMPLE EMBODIMENTS

- introduce 3D human digitization
- motivate limitations of existing approaches
- summarize NeRF-based models for static scenes
- explain NeRF's radiance field representation
- derive volume rendering integral equation
- motivate limitations of NeRF for dynamic videos
- introduce improved NeRF-based model for dynamic videos
- explain pose code and appearance code representations
- describe temporal transformer for aggregating trackable information
- outline training process for improved NeRF-based model
- highlight notable features and contributions of improved model
- summarize evaluation results against state-of-the-art techniques

### Training of Improved NeRF-Based Model

- illustrate overall training process
- generate appearance code
- access RGB-D image
- generate point clouds
- generate query pose
- extract features from query pose
- generate 3D feature volume
- cast camera rays
- extract subset of features
- encode subset of features into appearance code
- generate pose code
- access window or sequence of image frames
- access set of key frames
- generate point clouds for each frame
- generate query pose and key pose
- extract features from query pose and key pose
- generate 3D feature volumes
- cast camera rays
- extract subset of features
- perform point tracking
- determine first correspondence
- determine second correspondence
- feed into temporal transformer
- weigh input information
- combine results based on weightings
- generate pose code
- illustrate architecture of temporal transformer
- obtain corresponding pixels in key frame
- track points using body model
- obtain pose code from N frames
- employ transformer-based structure
- utilize multi-head attention component
- utilize feed-forward multi-layer perceptron
- apply self-attention mechanism
- compute attention weights
- produce output vector
- normalize features
- generate trainable associate memory
- define NeRF-based model
- formulate aggregated feature
- describe multi-head self-attention
- integrate features using average pooling
- generate pose code
- generate view and spatial code
- combine codes into density and color model
- predict volume density and color
- generate image from predicted density and color
- compute loss between generated and ground-truth images
- update model using loss
- define objective function
- compute reconstruction loss
- compute image loss
- describe training data
- outline training process

### Testing of Improved NeRF-Based Model

- introduce testing of improved NeRF-based model
- describe inference time process
- generate appearance code
- generate pose code
- generate view and spatial code
- feed codes into trained model
- generate color and density values
- combine pixels to generate image
- discuss differences between training and test time
- discuss pose code generation differences

### Example Test Results of Improved NeRF-based Model

- introduce example test results
- describe FIG. 3A
- compare outputs of improved and prior models
- discuss facial characteristics
- discuss cloth wrinkles
- describe FIG. 3B
- compare outputs of improved and prior models
- discuss facial characteristics
- discuss cloth wrinkles
- describe FIGS. 4A-4C
- compare outputs of improved and prior models
- discuss fine-level details
- discuss facial characteristics
- discuss cloth wrinkles
- discuss body details
- discuss limitations of prior model
- discuss importance of appearance code
- discuss importance of key frames
- discuss importance of temporal transformer
- discuss importance of depth information
- summarize results

### Example Method

- illustrate method for training NeRF-based model
- access image frame and depth information
- generate point cloud from depth information
- generate first latent representation (appearance code)
- access sequence of image frames and key frames
- generate sequence of query poses and key poses
- extract 3D features from query poses and key poses
- generate 3D volumes from extracted 3D features
- cast camera rays into 3D volumes
- perform point tracking
- generate second latent representation (pose code)
- access camera parameters for rendering
- generate third latent representation (view and spatial code)
- train NeRF-based model using latent representations
- generate color and density values for pixels
- generate image based on color and density values
- compare generated image with ground-truth image
- compute loss
- update NeRF-based model based on loss
- repeat steps for several iterations
- perform free-viewpoint rendering at inference time
- access single image and depth information
- generate latent representations for free-viewpoint rendering
- generate image from latent representations

### Example Computer System

- illustrate computer system
- describe computer system components
- introduce processor
- describe processor functionality
- introduce memory
- describe memory functionality
- introduce storage
- describe storage functionality
- introduce I/O interface
- describe I/O interface functionality
- introduce communication interface
- describe communication interface functionality
- introduce bus
- describe bus functionality
- describe computer system components interaction
- describe computer system functionality
- introduce computer system variations
- describe computer system variations
- introduce software running on computer system
- describe software functionality
- introduce computer system taking physical form
- describe computer system physical form
- introduce computer system including multiple components
- describe computer system including multiple components
- introduce computer system performing steps
- describe computer system performing steps
- introduce computer system performing steps in real-time
- describe computer system performing steps in real-time
- introduce computer system performing steps in batch mode
- describe computer system performing steps in batch mode

