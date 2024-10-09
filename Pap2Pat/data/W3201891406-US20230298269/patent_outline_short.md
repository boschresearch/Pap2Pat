# DESCRIPTION

## FIELD

- relate to differentiable rendering

## BACKGROUND

- motivate accurate derivatives

## SUMMARY

- introduce computer-implemented method
- introduce computing system
- introduce computer-readable media

## DETAILED DESCRIPTION

### Overview

- introduce differentiable rendering
- describe splat-based forward rendering
- motivate smooth derivatives near occlusion boundaries
- describe three-dimensional mesh representation
- explain rasterization of three-dimensional mesh
- determine initial color values for pixels
- construct splats for each pixel
- determine updated color values using splat weighting
- generate differentiable two-dimensional rendering

### Example Devices and Systems

- introduce computing system architecture
- describe user computing device components
- explain machine-learned models in user computing device
- describe server computing system components
- explain machine-learned models in server computing system
- describe training computing system components
- explain model trainer and training process
- describe network communication
- illustrate alternative computing system architectures

### Example Model Arrangements

- illustrate splat construction for a one-dimensional line segment
- define splat position using barycentric coordinates
- compute weight of splat at pixel position
- generate derivative of weight with respect to vertex position
- describe application of splat to pixel
- illustrate data flow diagram for generating two-dimensional differentiable rendering
- describe rasterization of three-dimensional mesh to obtain two-dimensional raster
- construct splat for each pixel of two-dimensional raster

### Example Methods

- obtain three-dimensional mesh with texture and/or shading data
- rasterize three-dimensional mesh to obtain two-dimensional raster
- determine initial color value for each pixel of two-dimensional raster
- construct splat for each pixel of two-dimensional raster
- determine updated color value for each pixel using splats
- generate derivatives at occlusion boundaries of two-dimensional differentiable rendering
- process two-dimensional differentiable rendering with machine-learned model

### Additional Disclosure

- discuss flexibility of computer-based systems and variations of embodiments

