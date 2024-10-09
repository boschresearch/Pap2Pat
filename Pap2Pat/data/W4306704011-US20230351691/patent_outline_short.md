# DESCRIPTION

## BACKGROUND

- motivate point cloud processing

## DETAILED DESCRIPTION

- introduce point cloud processing task
- describe limitations of existing techniques
- introduce system that uses multiple sparse window-based Transformer neural networks
- describe on-board system and its components
- describe point cloud processing system and its components
- describe voxel grid and assignment of points to voxels
- generate initial features for non-empty voxels
- process initial features to generate updated features using multiple sparse window Transformer neural network blocks
- fuse updated features to generate multi-scale features
- generate point cloud output using multi-scale features
- describe training system and its components
- describe process of training neural networks
- describe use of trained neural networks in point cloud processing system
- perform sparse partition of input voxel grid
- process scaled voxel grid using n-m-layer SWFormer block
- apply shifted sparse window partition and process shifted windows
- fuse multi-scale features to generate fused features
- perform point cloud processing task using fused features
- describe point cloud processing system
- detail voxel diffusion and segmentation
- explain decoder neural network and object detection
- define joint training of point processing neural network
- discuss system configuration and implementation
- describe data processing apparatus and computer program
- explain engine and computer-readable media
- discuss computing system and client-server interaction

