# DESCRIPTION

## BACKGROUND

### Technical Field

- define technical field

### Related Art

- motivate high-fidelity representation
- limitations of classical discrete shape representations
- limitations of implicit 3D shape representation approaches
- need for new approach

## SUMMARY

- summarize invention

## DETAILED DESCRIPTION

- introduce computer vision systems and methods
- describe unsigned distance field (uDF) and normal vector field (nVF)
- illustrate system 10 embodiment
- describe database 14
- introduce system code 16
- describe shape representation engine 18a
- describe unsigned distance field (uDF) module 20a
- describe normal vector field (nVF) module 20b
- describe training engine 18b
- describe iso-surface extraction engine 18c
- describe shape rendering engine 18d
- describe evaluation engine 18e
- define open and closed shapes
- describe unsigned distance functions
- describe normal vector fields
- describe implicit shape representation
- describe robust loss function
- describe iso-surface extraction
- describe sphere tracing method
- compare system 10 with prior art systems
- illustrate overall processing steps
- receive data associated with 3D surface
- process data using computer vision models
- predict unsigned distance field and normal vector field
- describe unsigned distance function
- illustrate non-differentiability of uDF on surface
- describe normal vector field
- determine 3D surface representation
- model uDF+nVF pair using multilayer perceptron modes
- sample training pairs from noisy triangle soup
- construct set of training samples
- estimate unsigned distance and normal vector
- determine first and second losses
- describe modulo 180° representation
- define loss functions
- derive backpropagation
- describe software design of automatic differentiation
- illustrate visualization of uDF and nVF
- describe model architecture
- extract iso-surface of 3D representation
- create voxel grid for uDF
- hierarchically divide voxel grid
- convert selected voxels into mesh
- extract iso-surface of 3D representation
- render view of 3D representation
- cast rays from viewpoint
- process each ray using sphere tracing
- determine intersections of each ray and 3D surface
- estimate intersection of each ray and 3D surface
- render view of 3D surface representation
- evaluate 3D representation
- evaluate depth error
- evaluate normal map error
- evaluate IOU error
- compare with SAL and DeepSDF
- generate 3D representations for shapes
- train DUDE using samples
- illustrate visualizations of implicit 3D shape representations
- compare with DeepSDF and SAL
- illustrate ray casting using normals
- illustrate quantitative comparison of metrics
- evaluate sphere tracing
- compare with standard and resample methods
- illustrate graphs showing absolute depth error
- process point clouds to generate 3D representation
- illustrate results on surface reconstruction from point clouds
- describe computer hardware and network components
- illustrate system architecture
- describe computation servers
- describe data storage servers
- describe user device

