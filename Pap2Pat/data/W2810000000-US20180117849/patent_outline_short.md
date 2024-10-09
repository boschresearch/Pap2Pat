# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- define field of invention

### 2. Brief Description of the Related Art

- limitations of 3D printing
- motivate joint color and translucency printing

## SUMMARY OF THE INVENTION

- introduce 3D joint color and translucency printing
- describe printing process using non-transparent and transparent materials
- motivate creation of model with desired color and translucency reproduction
- encode color and translucency information in RGBA signal
- generate control data for 3D printing device
- describe 3D joint color and translucency printing process
- determine arrangement of printing materials based on desired color and translucency reproduction
- generate machine-readable data to instruct printing device
- compare with prior art EP 3023229 A1 and GB 1512434.0
- describe voxel-based representation of printing object
- assign desired color and translucency information to voxels
- transform color value and translucency information into printer-specific printing material color and translucency vector
- summarize assignment of printing material to voxels
- motivate half-toning algorithm
- describe color quantization
- explain error diffusion
- outline transformation of color value and translucency information
- describe digital processing chain
- explain printing process control
- motivate RGBA value assignment
- describe voxel-based representation determination
- outline object prioritization
- summarize voxel classification
- introduce color and translucency assignment
- describe tie-breaking algorithm
- motivate near-surface interior voxel set
- explain two-step process for determining nearest surface voxel
- describe alternative methods for assigning color and translucency values
- introduce perceptually uniform color and translucency spaces
- describe transformation from non-uniform to uniform spaces
- motivate transformation into printer-specific printing material color and translucency vector
- describe adaptation of translucency component based on light transport effects
- explain assignment of color value and translucency information to printer-specific printing material color and translucency vectors
- describe determination of printer-specific printing material color and translucency vector based on predetermined assignment
- introduce color and translucency printing
- describe transformation from CIELABβ to CMYKγ space
- explain assignment of color value and translucency information
- detail predetermined assignment of printer-specific material color and translucency vector
- describe use of printer predicting function and gamut correction function
- explain smoothing of assignment to avoid color and translucency banding artifacts
- describe voxel-based representation of printing object
- detail assignment of printing material to voxel using error diffusion algorithm
- explain half-toning algorithm for assigning printing material to voxel
- describe replacement of non-transparent printing material with transparent printing material
- detail data processing system for three-dimensional joint color and translucency printing
- describe computer program product for three-dimensional joint color and translucency printing
- propose 3D joint color and translucency printing device and printing object

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- describe 3D joint color and translucency printing device
- illustrate printing object with transparent and non-transparent printing materials
- explain control unit for controlling print heads
- describe voxelization of printing object
- assign color value and translucency information to voxels
- transform color value and translucency information to printer-specific printing material color and translucency vector
- adapt translucency component as a function of light transport effects
- perform layer construction and half-toning
- replace non-transparent printing material with transparent printing material based on translucency parameter
- control printing process based on resulting assignment of printing materials to voxels

