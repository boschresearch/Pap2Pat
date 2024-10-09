# DESCRIPTION

## FIELD OF THE INVENTION

- relate to computer graphics

## BACKGROUND OF THE INVENTION

- introduce visualization and animation
- describe model-based rendering
- describe image-based rendering
- describe hybrid rendering
- limitations of parametric BRDFs
- limitations of image-based rendering
- describe surface light fields
- limitations of surface light fields
- describe surface reflectance fields
- prior art for 3D rendering
- describe lumigraph
- describe view-dependent texture mapping
- describe surface light fields and opacity light fields
- describe surface reflectance fields and interpolation
- prior art for animation of image-based data

## SUMMARY OF THE INVENTION

- provide method for rendering deformed and animated surface reflectance fields

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe figures of the invention

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

- introduce surface reflectance field
- define 3D model construction
- acquire reflectance images
- define shading operation
- motivate deformable surface reflectance fields
- define surface reflectance field notation
- outline animation process

### Approximate BRDF Preservation

- motivate BRDF preservation
- limitations of exact object geometry and material properties
- introduce local BRDFs
- define look-up function L
- enforce appearance preservation by three conditions
- motivate first condition: same surface point with same BRDF
- select p as approximation of q
- motivate second condition: same angle between lighting and surface normal
- preserve shape of reflectance lobes
- preserve azimuthal orientations
- motivate third condition: preserve effect of anisotropic BRDFs
- determine mapping (p*, l*, v*)(l, v)
- express mapping as locally affine
- enforce angle preservation
- enforce length preservation
- conclude isometry of function Lp*
- interpret as rotation or reflection
- assume rotation
- express total effect as rigid transformation
- restrict to rigid transformations mapping deformed normal to original normal
- introduce local model parameterization
- associate parameters with each point p*
- enable look-up function L without inverse deformation function
- store original position p0
- align deformed tangential system with acquisition frame
- provide two coordinate systems: R0 and (u, v)
- reconstruct rotation Lp* during rendering
- define normal and bisecting vector
- construct orthogonalized tangential system
- give rotation Lp*
- note approximation of tangential orientation preservation
- discuss rigid transformation for rigid object deformations
- discuss limitations of prior art
- introduce shading
- discuss problems with environment map filtering
- provide alternative method for shading
- simulate lighting with point light sources
- apply look-up scheme to reflectance query
- yield reflectance coefficients
- shade point with color
- discuss error in incident lighting direction
- discuss interpolation of novel lighting directions
- discuss environment mapping with point light sources
- discuss sub-sampling environment map
- conclude advantages of method

## EFFECT OF THE INVENTION

- summarize invention benefits

