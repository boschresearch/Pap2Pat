# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- motivate additive manufacturing

## SUMMARY

- motivate voxelization
- introduce point cloud and mesh approximations
- describe limitations of prior art voxelization
- introduce novel voxelization approach
- describe displaced signed distance field
- outline advantages of displaced signed distance field
- describe regularization of sign function
- introduce method for selecting voxels
- describe generating control signals for additive manufacturing
- describe producing an object with additive manufacturing
- introduce computer device for generating manufacturing data
- describe receiving surface approximation data
- describe determining signed distance values
- describe generating manufacturing data
- define coordinate system
- describe surface approximation data
- represent voxel by center point coordinates
- determine distance to voxel-based approximation
- generate control signals for additive manufacturing
- perform voxelization procedure
- parallelize and distribute computational load
- manage memory efficiently
- derive displacement values from displacement map
- select voxels based on signed distance value
- filter sign function to improve robustness

## DETAILED DESCRIPTION

- introduce computer device and 3D printer
- describe build space and voxel grid
- receive surface approximation data
- perform surface voxelization pre-process
- determine displaced signed distance field
- determine sign s(u) for each voxel center
- compute displaced signed distance value f(u)
- regularize sign function (optional)
- compensate for self-overlapping portions (optional)
- perform voxel selection
- store attributes at surface voxels (optional)
- define manufacturing data set and send to 3D printer

