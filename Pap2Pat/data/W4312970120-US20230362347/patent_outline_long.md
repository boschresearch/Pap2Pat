# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- define field

### 2. Description of the Related Art

- summarize limitations of NVS

## SUMMARY OF THE INVENTION

- motivate novel view synthesis
- summarize method
- highlight advantages

## DETAILED DESCRIPTION OF THE INVENTION

- define scope of invention
- introduce terminology
- describe prior art limitations
- introduce novel view synthesis (NVS) with sparse inputs
- describe advantages of NVS
- introduce Forward Warping features based on estimated Depths (FWD)
- describe estimation of explicit depth for input views
- introduce differentiable point cloud renderer
- describe fast rendering speed and end-to-end training
- introduce training with RGB data only
- describe progressive enhancement with noisy sensor depth data
- introduce flowchart of non-limiting example steps for NVS
- access or acquire input view or multiple input views
- estimate depths for each input image
- construct point cloud of image features
- synthesize novel views using point cloud renderer
- model view-dependent effects
- fuse multiple synthesized views
- in-paint missing regions
- generate output pixels
- describe sparse set of input images and corresponding camera poses
- synthesize novel view with camera pose
- estimate depths of input images
- describe view-dependent semantics
- introduce differentiable neural point cloud renderer
- fuse rendered results at target view
- employ refinement module
- train end-to-end with photometric and perceptual loss
- describe point cloud construction
- estimate per-pixel depth and per-pixel feature vectors
- project feature vectors into 3D space
- describe spatial feature encoder
- map scene semantics to pixel-specific feature vectors
- describe depth network
- estimate depth from single image
- address scaling/shifting ambiguity
- apply conventional multi-view stereo algorithms
- cascade U-Net after MVS module
- refine depths with multiview stereo cues and image cues
- describe sensor depths
- input sensor depth to U-Net
- complete and refine depth estimation
- describe view-dependent feature MLP
- compute view-dependent spatial features
- translate scene semantics to target view
- describe point cloud renderer
- render point cloud at target view
- describe Transformer-based fusion module
- fuse feature maps from point clouds
- decode fused feature maps to RGB images

### Example

- introduce novel view synthesis (NVS) task
- motivate NVS applications
- describe limitations of image-based rendering (IBR)
- describe limitations of Neural Radiance Fields (NeRF)
- introduce FWD-U method
- highlight advantages of FWD-U
- describe explicit depth estimation
- describe differentiable point cloud renderer
- describe end-to-end training
- describe sensor depth integration
- describe growing prevalence of depth sensors
- describe method overview
- describe point cloud construction
- describe feature-dependent MLP
- describe Transformer-based fusion module
- describe refinement module
- describe training objectives
- describe validation on benchmarks
- describe user study
- describe main contributions
- introduce related work
- describe image-based rendering methods
- describe neural scene representations
- describe utilizing RGB-D in NVS
- describe differentiable rendering and refinement
- describe problem formulation
- describe point cloud construction
- describe spatial feature encoder
- describe depth network
- describe depth estimation with sensor depths
- describe view-dependent feature MLP
- describe point cloud renderer
- describe fusion and refinement
- motivate novel view synthesis
- limitations of rendered feature maps
- introduce refinement module R
- describe architecture of R
- introduce training and implementation details
- define loss function
- specify training settings
- introduce experiments
- state goal of experiments
- describe evaluation metrics
- introduce model variants
- describe FWD model
- describe FWD-U model
- describe FWD-D model
- introduce ShapeNet benchmarks
- describe evaluation protocol
- show qualitative comparisons
- show quantitative results
- introduce DTU MVS benchmarks
- describe evaluation protocol
- show qualitative results
- show quantitative results
- introduce ablation experiments
- evaluate effectiveness of fusion transformer
- evaluate effectiveness of view-dependent MLP
- analyze depth estimation

## 5. CONCLUSION

- summarize method advantages

