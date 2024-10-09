# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- define field of invention

### 2. Brief Description of the Related Art

- introduce 3D printing
- limitations of existing 3D printing
- prior art on color reproduction
- prior art on translucency fabrication

## SUMMARY OF THE INVENTION

- propose 3D joint color and translucency printing method
- use non-transparent and transparent printing materials
- define printing object and its construction
- describe 3D printing process with successive slices
- create model of 3D printing object with color and translucency information
- encode color and translucency information in RGBA signal
- generate input data for proposed method
- describe possible data formats for input data
- provide texture image with color and translucency information
- generate control data for 3D printing device
- describe 3D joint color and translucency printing process
- use polymerisation-based process as example
- use support material with first support material color
- use multiple non-transparent printing materials with different colors
- determine arrangement of printing materials based on desired color reproduction
- determine arrangement of printing materials based on desired translucency reproduction
- reproduce desired color and translucency with voxel-based arrangement
- generate machine-readable data to instruct printing device
- compare proposed method with EP 3023229 A1 and GB 1512434.0
- describe technical challenges addressed by proposed method
- reproduce perceptual translucency cues instead of physical parameters
- determine voxel-based representation of printing object
- assign desired color and translucency information to each voxel
- convert desired color and translucency information into printing material color and translucency vector
- summarize assignment of printing material to voxels
- motivate half-toning algorithm
- describe printing material color quantization
- explain error diffusion step
- summarize transformation of color value and translucency information
- describe digital processing chain
- explain control of printing process
- describe construction of printing object
- assign RGBA value to each voxel
- describe determination of voxel-based representation
- test if voxel is intersected by surface of printing object
- assign desired color value and translucency information
- describe surface section determination
- determine voxel bounding box
- evaluate surface intersection criterion
- describe alternative surface intersection criterion
- determine color value and translucency information by interpolation
- perform object prioritization
- determine voxel-based representation for each object
- classify voxels as object voxels or exterior voxels
- determine surface layer voxel set and interior voxel set
- assign color value and translucency information to voxels of different voxel sets
- introduce method for assigning color values and translucency information to interior voxels
- describe tie-breaking algorithm for determining nearest surface voxel
- outline assignment of color value and translucency information to near-surface interior voxels
- describe assignment of preset color value and translucency information to remaining interior voxels
- motivate two-step process for determining nearest surface voxel
- describe first step of two-step process: determining z-distance to nearest surface voxel
- describe second step of two-step process: using 2D distance transformation
- outline alternative methods for assigning translucency values to interior voxels
- describe use of voxel arrays for fast computation of nearest surface voxel
- outline method for determining nearest surface voxel slice by slice
- describe independent invention of method for determining nearest surface voxel
- outline transformation of color value information into perceptually uniform color space
- describe transformation of translucency information into perceptually uniform translucency space
- motivate use of perceptually uniform spaces for color and translucency
- outline transformation from perceptually non-uniform space to perceptually uniform space
- describe adaptation of translucency component as function of light transport effects
- outline assignment of printer-specific printing material color and translucency vector
- describe determination of printer-specific printing material color and translucency vector
- outline use of physical or empirical model to obtain predicting function
- describe inversion of predicting function to obtain CMYKγ values
- outline use of gamut mapping transformation for non-reproducible CIELABβ values
- describe selection of CMYKγ value from multiple possible values
- conclude summary of invention
- introduce color and translucency printing
- define color-translucency space
- describe transformation from CIELABβ to CMYKγ
- introduce assignment of color value and translucency information
- describe mapping of color component into reference set of printable colors
- determine node-specific sets of printer-specific printing material color and translucency vectors
- assign printer-specific printing material color and translucency vector to node
- describe interpolation between nodes
- introduce printer predicting function
- describe gamut correction function
- apply gamut correction function
- smooth assignment of color value and translucency information
- introduce voxel-based representation of printing object
- assign printing material to voxel
- describe error diffusion algorithm
- describe half-toning algorithm
- describe layered half-toning algorithm
- describe nibbling half-toning algorithm
- describe contoning algorithm
- replace non-transparent printing material with transparent printing material
- describe data processing system
- describe computer program product
- describe program storage medium
- describe computer implemented method
- describe 3D joint color and translucency printing device
- describe printing object

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce 3D joint color and translucency printing device
- describe print heads and printing materials
- explain reference coordinate system
- describe control unit and its functions
- illustrate arrangement of printing materials for color and translucency reproduction
- show voxels of printing object
- define surface voxels and interior voxels
- explain near surface interior layer voxel set
- illustrate transparent printing material voxels
- show optical path to interior voxel
- introduce method for 3D joint color and translucency printing
- generate input data with shape- and texture-based representation
- perform voxelization and assign color values and translucency information
- determine bounding box and test for surface intersection
- assign object identifier and RGBA vector to voxels
- classify object voxels and object exterior voxels
- assign color values and translucency information to interior voxels
- transform color values and translucency information to CIELABβ space
- transform CIELABβ vector to printer-specific printing material color and translucency vector
- control printing process based on resulting assignment of printing materials

