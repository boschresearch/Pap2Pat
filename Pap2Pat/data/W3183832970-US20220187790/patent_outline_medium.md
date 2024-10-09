# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- introduce additive manufacturing
- describe voxelization challenges

## SUMMARY

- motivate voxelization
- introduce point cloud and mesh
- describe limitations of prior art
- introduce problem of incomplete approximations
- describe issue of geometric features smaller than voxel resolution
- introduce problem of scaling objects
- describe object of disclosure
- introduce novel voxelization approach
- describe displaced signed distance field
- explain advantages of displaced signed distance field
- describe robustness improvement
- introduce regularization of sign function
- describe filtering of sign function
- explain alternative regularization methods
- describe efficient determination of displacement information
- introduce method for selecting voxels
- describe receiving surface approximation data
- describe generating voxel-based approximation
- determine signed distance values
- select voxels based on signed distance values
- describe generating control signals
- describe producing an object with additive manufacturing device
- describe 3D printing process
- describe generation of successive slices
- describe modelling step
- describe encoding reproduction information
- describe computer device for generating manufacturing data
- describe outputting manufacturing data to 3D printer
- define coordinate system
- introduce surface approximation data
- describe voxel representation
- explain voxel selection for additive manufacturing
- generate control signals for additive manufacturing
- discuss voxelization procedure
- describe parallelization of voxel selection
- explain efficient memory management
- derive displacement values from displacement map
- discuss advantages of displacement map
- select voxels based on signed distance value
- filter sign function to smooth signed distance values
- determine sign of voxel based on orientation of voxel face
- discuss floodfill computation for self-intersection
- propose computer program product
- describe program storage medium
- discuss computer implemented method
- propose printing system for producing an object
- describe additive manufacturing device
- discuss printing object obtained by proposed method
- explain advantages of proposed method
- discuss embodiments of proposed solution
- provide background description

## DETAILED DESCRIPTION

- introduce computer device and 3D printer
- describe build space and voxel grid
- define object to be produced and surface approximation
- receive surface approximation data
- describe surface approximation data
- transform coordinates into reference coordinate system
- perform surface voxelization pre-process
- identify voxels containing points of point cloud
- identify voxels intersected by polygons
- determine displaced signed distance field
- define sign function
- compute signed distance value
- determine displacement map
- expand signed distance function
- determine sign s for each voxel center
- evaluate orientation of faces with respect to primitives
- incorporate weighting to consider relative distances
- compute signed distance for each primitive in a voxel
- evaluate change of signed distance when moving along directions
- sum up gradients of signed distance functions
- determine overall sign s
- regularize sign function
- perform floodfill computation
- select voxels based on displaced signed distance value
- generate manufacturing data set

