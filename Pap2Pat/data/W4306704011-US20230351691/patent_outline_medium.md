# DESCRIPTION

## BACKGROUND

- motivate point cloud processing

## DETAILED DESCRIPTION

- introduce point cloud processing task
- describe autonomous vehicles using on-board systems
- motivate sparse nature of point clouds
- describe limitations of existing techniques
- introduce SWTransformer neural networks
- describe system 100
- introduce on-board system 110
- describe sensor systems 130
- describe point cloud processing system 150
- describe voxel grid
- assign points to voxels
- determine non-empty and empty voxels
- generate initial features
- process initial features using SWFormer neural network blocks
- generate multi-scale features
- fuse features
- generate point cloud output
- describe planning system 160
- describe user interface system 165
- describe training system 120
- describe network parameters store 190
- describe training engine 180
- describe loss functions
- describe process 200 for processing point clouds
- assign points to voxels in original voxel grid
- generate initial features for non-empty voxels
- generate multi-scale features of voxel grid
- define sparse partition
- motivate sparse representation
- describe sparse partition process
- explain region selection
- introduce n-m-layer SWFormer block
- describe self-attention mechanism
- explain shifted sparse window partition
- describe feature fusion process
- explain upsampling and concatenation
- describe 1-layer SWFormer block for fused features
- motivate point cloud processing task
- describe system for point cloud processing
- perform segmentation of voxels
- filter out background voxels
- perform voxel diffusion
- generate point cloud output using decoder neural network
- perform box regression
- jointly train point processing neural network
- determine foreground and background voxels
- train neural network using ground truth labels
- define segmentation loss function
- define total loss function for object detection
- backpropagate total loss to train SWFormer blocks
- describe configuration of systems and computer program components
- implement embodiments of subject matter
- describe data processing apparatus and computer programs
- provide for interaction with user

