# DESCRIPTION

## FIELD OF THE INVENTION

- relate to computer graphics

## BACKGROUND OF THE INVENTION

- introduce visualization and animation
- describe model-based rendering
- describe image-based rendering
- describe hybrid rendering
- motivate surface reflectance fields
- discuss limitations of prior art
- identify need for animating surface reflectance fields

## SUMMARY OF THE INVENTION

- introduce method for rendering deformed surface reflectance fields

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe figures of the invention

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

- illustrate surface reflectance field generation
- define 3D model and reflectance images
- explain deformation and shading operations

### Approximate BRDF Preservation

- motivate BRDF preservation
- limitations of exact object geometry and material properties
- introduce look-up function L
- enforce appearance preservation by three conditions
- condition 1: intersecting viewing rays
- condition 2: preserve reflectance characteristics
- condition 3: preserve anisotropic BRDFs
- decompose look-up function L into translation and rotation
- define local model parameterization
- associate parameters with each point p*
- determine function L without using closed form of Ψ−1
- store original position p0 and tangential system R0
- reconstruct rotation Lp* during rendering
- define tangential orientation R0
- map tangential system using directional derivatives
- reconstruct rotation Lp* using orthogonalized tangential system
- discuss rigid transformation of model
- shade deformed model point using point light source
- transform reflectance query from object space to acquisition space
- use SRF to shade point with color Ip
- discuss alternative method for shading deformed SRF
- reorder evaluation for efficient SRF look-up

## EFFECT OF THE INVENTION

- summarize invention benefits

