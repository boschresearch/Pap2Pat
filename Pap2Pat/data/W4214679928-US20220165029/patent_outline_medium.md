# DESCRIPTION

## BACKGROUND

### Technical Field

- define technical field

### Related Art

- limitations of classical shape representations
- limitations of implicit shape representations

## SUMMARY

- summarize invention

## DETAILED DESCRIPTION

- introduce computer vision systems and methods
- describe unsigned distance field (uDF) and normal vector field (nVF)
- illustrate system 10 embodiment
- describe database 14
- introduce system code 16
- describe uDF module 20a
- describe nVF module 20b
- describe training engine 18b
- describe iso-surface extraction engine 18c
- describe shape rendering engine 18d
- compare system 10 with prior art systems
- illustrate overall processing steps 50
- describe processing data
- describe predicting uDF and nVF
- describe determining 3D surface representation
- describe training processing steps 80
- describe estimating unsigned distance and normal vector
- define loss functions
- train DNNs
- visualize uDF and nVF
- extract iso-surface
- create voxel grid
- hierarchically divide voxel grid
- convert voxels to mesh
- extract iso-surface
- render view of 3D representation
- cast rays from viewpoint
- process each ray using sphere tracing
- determine intersections of each ray and 3D surface
- render view of 3D surface representation
- evaluate 3D representation
- compare with SAL and DeepSDF
- generate 3D representations for shapes
- evaluate sphere tracing
- process point clouds to generate 3D representation

