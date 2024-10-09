# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- define field

### 2. Description of the Related Art

- motivate novel view synthesis

## SUMMARY OF THE INVENTION

- summarize invention

## DETAILED DESCRIPTION OF THE INVENTION

- define scope of invention
- introduce terminology
- describe prior art limitations
- introduce novel view synthesis (NVS) with sparse inputs
- describe advantages of NVS
- introduce Forward Warping features based on estimated Depths (FWD)
- describe estimating explicit depth for input views
- introduce differentiable point cloud renderer
- describe training with RGB data only
- describe training with noisy sensor depth data
- introduce flowchart of non-limiting example steps for NVS
- access or acquire input views
- estimate depths for each input image
- construct point cloud of image features
- synthesize novel views using point cloud renderer
- model view-dependent effects
- fuse multiple synthesized views
- in-paint missing regions
- describe sparse set of input images and camera poses
- estimate depths using a U-Net
- describe view-dependent feature MLP
- introduce point cloud renderer
- describe fusion Transformer module
- describe refinement module
- describe training of a model end-to-end with photometric and perceptual losses

### Example

- introduce novel view synthesis (NVS) task
- motivate NVS applications
- describe limitations of image-based rendering (IBR)
- describe limitations of Neural Radiance Fields (NeRF)
- introduce FWD-U method
- describe key insight of FWD-U
- describe FWD-U architecture
- describe depth estimation module
- describe point cloud construction
- describe differentiable point cloud renderer
- describe fusion module
- describe refinement module
- describe training losses
- describe experimental setup
- describe results
- conclude FWD-U method
- motivate novel view synthesis
- introduce refinement module R
- describe training and implementation details
- introduce experiments
- define metrics
- describe model variants
- evaluate on ShapeNet benchmarks
- evaluate on DTU MVS benchmarks
- show qualitative results
- show quantitative results
- evaluate baselines
- perform ablation study
- analyze depth estimation

## 5. CONCLUSION

- summarize method advantages

