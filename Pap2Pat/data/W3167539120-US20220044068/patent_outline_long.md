# DESCRIPTION

## BACKGROUND

- introduce neural networks

## SUMMARY

- describe method of processing input data
- define perspective view range image
- describe first neural network
- define first perspective point-set aggregation layer
- describe geometry-dependent kernel
- describe object detection implementation
- describe LiDAR sensor implementation
- describe RGBD camera implementation
- describe two-dimensional convolutional layer
- describe obtaining validity data
- describe geometry-dependent convolution kernel
- describe self-attention kernel
- describe encoder neural network implementation
- describe down-sampling and up-sampling layers
- describe fusing camera image features
- describe system and computer storage media
- motivate 3D point cloud understanding

## DETAILED DESCRIPTION

- introduce system 100
- describe system 100 components
- explain input data 110
- describe perspective view range image 112
- explain features of perspective view range image
- describe range features
- explain generation of perspective view range image
- describe LiDAR sensor measurements
- explain computation of distance
- describe sweeping in azimuth
- explain 2D grid of perspective view range image
- describe RGBD camera measurements
- explain validity data 114
- describe handling of invalid pixels
- explain camera image data 116
- describe utilization of camera images
- explain output feature representation 130
- describe first neural network 120
- explain perspective point cloud (PPC) neural network
- describe perspective point-set aggregation layers 122
- explain input feature map
- describe output feature map
- explain geometry-dependent kernel 122a
- describe application of geometry-dependent kernel
- explain range-quantized convolution kernel
- describe self-attention kernel
- explain PointNet kernel
- describe edge convolution kernel
- explain importance of 3D point cloud understanding
- describe conventional 3D point cloud understanding approaches
- explain advantages of PPC neural network
- describe 2D convolutional layers 124
- explain down-sampling layers 126
- describe validity-dependent down-sampling strategy
- explain quantization and calibration artifacts
- describe missing returns in LiDAR data
- explain fixed stride down-sampling
- describe validity data in down-sampling
- explain output neural network 140
- describe processing of output feature representation
- explain generation of network output 150
- describe utilization of network output
- define down-sampling layer
- motivate valid pixel selection
- describe up-sampling process
- define up-sampling formula
- motivate fusing operation
- describe fusing camera image features
- describe neural network architecture
- describe perspective point-set aggregation layers
- describe optional CNN layers
- describe down-sampling and up-sampling layers
- describe backbone architecture
- describe output neural network
- describe network parameters training
- describe training process
- illustrate 3D grid-based process
- illustrate 3D graph-model based process
- illustrate PPC neural network process
- illustrate different kernels
- describe FE blocks
- describe FA blocks
- illustrate neural network backbone architecture
- illustrate detection results
- describe process for processing perspective view range image
- describe neural network architecture
- process perspective view range image
- generate output feature representation
- define perspective point-set aggregation layer
- apply geometry-dependent kernel
- obtain input feature map
- generate output feature vector
- describe range-quantized convolution kernel
- describe self-attention kernel
- describe PointNet kernel
- describe edge convolution kernel
- include 2D convolutional layers
- include down-sampling layers
- down-sample input feature map
- include up-sampling layers
- up-sample input feature map
- fuse feature vectors with camera image features
- process output representation using output neural network
- generate network output for neural network task
- define configured systems and computer program components
- describe digital electronic circuitry
- describe computer software or firmware
- describe computer hardware
- describe computer storage medium
- define database
- define engine
- describe processes and logic flows
- describe computers suitable for execution
- describe central processing unit
- describe memory devices
- describe mass storage devices
- describe computer-readable media
- provide for interaction with user
- describe data processing apparatus
- implement machine learning models
- describe computing system architecture

