# DESCRIPTION

## FIELD

- relate to differentiable rendering

## BACKGROUND

- motivate accurate derivatives

## SUMMARY

- introduce computer-implemented method
- describe rasterizing three-dimensional mesh
- determine initial color value
- construct splat
- determine updated color value
- introduce computing system and media

## DETAILED DESCRIPTION

### Overview

- introduce differentiable rendering
- relate to splat-based forward rendering
- describe three-dimensional mesh
- explain rasterization
- generate coordinates for pixels
- determine initial color values
- construct splats for pixels
- determine updated color values
- generate two-dimensional differentiable rendering
- describe application in machine learning
- generate derivatives for splats
- process rendering with machine-learned model
- evaluate loss function
- adjust model parameters
- describe machine-learned pose estimation model
- describe machine-learned three-dimensional mesh generation model
- highlight limitations of rasterization
- highlight benefits of present disclosure
- introduce figures

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- detail processor 112 and memory 114
- explain instructions 118 for two-dimensional differentiable rendering
- describe machine-learned models 120
- discuss training of machine-learned models 120
- introduce server computing system 130
- describe processor 132 and memory 134
- explain instructions 138 for server computing system 130
- discuss machine-learned models 140
- introduce training computing system 150
- describe processor 152 and memory 154
- explain instructions 158 for training computing system 150
- detail model trainer 160
- discuss training data 162
- describe network 180
- illustrate alternative computing system
- depict block diagrams of example computing devices

### Example Model Arrangements

- illustrate splat construction for a one-dimensional line segment
- define splat position using barycentric coordinates
- compute weight of splat at pixel position
- generate derivative of weight with respect to vertex
- describe effect of vertex movement on weight
- illustrate data flow diagram for generating two-dimensional differentiable rendering
- obtain three-dimensional mesh
- rasterize three-dimensional mesh to obtain two-dimensional raster
- determine initial color values for each pixel
- construct splat for each pixel
- compute weight of splat at pixel position
- determine updated color value for each pixel
- generate two-dimensional differentiable rendering
- illustrate data flow diagram for training machine-learned model
- obtain two-dimensional differentiable rendering and 3D mesh training data
- generate derivatives for respective splats
- process two-dimensional differentiable rendering with machine-learned model

### Example Methods

- obtain three-dimensional mesh
- rasterize three-dimensional mesh
- determine initial color value for each pixel
- construct splat for each pixel
- determine updated color value for each pixel
- generate two-dimensional differentiable rendering
- generate derivatives at occlusion boundaries
- process two-dimensional differentiable rendering with machine-learned model
- evaluate loss function
- adjust parameters of machine-learned model
- generate machine-learned output
- depict entity represented by three-dimensional mesh
- generate second three-dimensional mesh
- fit mesh to depicted entity
- generate mesh from two-dimensional image data

### Additional Disclosure

- describe flexibility of computer-based systems

