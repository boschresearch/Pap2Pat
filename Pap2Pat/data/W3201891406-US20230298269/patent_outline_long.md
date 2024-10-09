# DESCRIPTION

## FIELD

- relate to differentiable rendering

## BACKGROUND

- introduce limitations of contemporary solutions

## SUMMARY

- introduce method for differentiable rendering
- obtain three-dimensional mesh
- rasterize three-dimensional mesh
- determine initial color values
- construct splats
- determine updated color values
- introduce computing system
- obtain three-dimensional mesh
- rasterize three-dimensional mesh
- determine initial color values
- construct splats
- determine updated color values
- introduce non-transitory computer-readable media

## DETAILED DESCRIPTION

### Overview

- introduce differentiable rendering
- relate to splat-based forward rendering
- describe three-dimensional mesh
- explain rasterization
- generate coordinates for pixels
- determine initial color value
- construct splat for each pixel
- preserve derivatives for vertices
- compute splat center points
- apply perspective division and viewport transformation
- determine updated color value
- weight splats based on proximity
- generate differentiable two-dimensional rendering
- utilize rendering for smooth derivatives
- describe three-dimensional mesh generation
- relate to machine-learned model output
- explain rasterization scheme
- determine initial color value
- apply shading and/or texturing scheme
- construct splat with smooth falloff
- compute weight of splat
- determine updated color value
- select subset of splats
- weigh splats based on distance
- generate differentiable two-dimensional rendering
- utilize rendering for smooth derivatives
- describe machine-learned model training
- evaluate loss function
- adjust model parameters
- describe machine-learned pose estimation model
- generate image data
- describe machine-learned three-dimensional mesh generation model
- generate second three-dimensional mesh
- compare to point-based rendering
- explain limitations of rasterization
- describe technical effects and benefits
- enable generation of differentiable rendering
- reduce computational resources
- provide accurate derivatives

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- detail processor 112 and memory 114
- explain data 116 and instructions 118
- motivate two-dimensional differentiable rendering 124
- describe rasterization of three-dimensional mesh
- generate coordinates for pixels
- determine initial color value for pixels
- construct splat for each pixel
- determine updated color value for pixels
- generate two-dimensional differentiable rendering 124
- generate derivative for splat
- discuss server computing system 130
- describe processor 132 and memory 134
- explain data 136 and instructions 138
- introduce machine-learned models 120
- describe neural networks
- discuss training of machine-learned models 120
- introduce server computing system 130
- describe machine-learned models 140
- discuss training computing system 150
- describe processor 152 and memory 154
- explain data 156 and instructions 158
- introduce model trainer 160
- discuss training of machine-learned models 120 and 140
- describe backwards propagation of errors
- discuss generalization techniques
- introduce training data 162
- describe ground truth data
- discuss machine-learned pose estimation model
- evaluate loss function
- discuss personalizing model
- introduce network 180
- describe communication over network 180
- discuss alternative computing systems
- illustrate example computing devices

### Example Model Arrangements

- depict splat construction for a one-dimensional line segment
- define barycentric coordinates
- construct splat at splat position
- update pixel color value
- generate derivative from splat
- define derivative of weight of splat
- determine sign of derivative
- increase weight of splat
- decrease weight of splat
- generate derivative with respect to v2
- construct splat for pixel
- generate derivatives based on splat location
- depict data flow diagram of method for generating two-dimensional differentiable rendering
- obtain three-dimensional mesh
- rasterize three-dimensional mesh
- obtain two-dimensional raster
- determine initial color values for pixels
- apply shading data and/or texture data
- construct splat for each pixel
- compute coordinates at which splats are constructed
- determine updated color value for each pixel
- generate two-dimensional differentiable rendering
- find smooth derivatives at occlusion boundaries
- depict data flow diagram of method for training machine-learned model
- obtain two-dimensional differentiable rendering and 3D mesh training data
- generate derivatives for respective splats
- process two-dimensional differentiable rendering with machine-learned model
- generate machine-learned output
- evaluate loss function
- adjust parameters of machine-learned model
- generate machine-learned output using machine-learned model
- evaluate differences between machine-learned output and training data
- generate parameter adjustments to optimize machine-learned model
- depict entity represented by three-dimensional mesh

### Example Methods

- obtain three-dimensional mesh
- generate three-dimensional mesh using machine-learning techniques
- rasterize three-dimensional mesh
- obtain two-dimensional raster
- determine initial color value for each pixel
- apply shading and/or texture data
- construct splat for each pixel
- compute splat center points
- apply perspective division and viewport transformation
- determine updated color value for each pixel
- weight splats based on proximity
- generate two-dimensional differentiable rendering
- select subset of splats for each pixel
- weigh splats based on distance
- normalize weights
- compute updated color value
- generate derivatives at occlusion boundaries
- process two-dimensional differentiable rendering with machine-learned model
- generate machine-learned output
- evaluate loss function
- adjust machine-learned model parameters
- train machine-learned pose estimation model
- train machine-learned three-dimensional mesh generation model
- generate image data with second pose/orientation
- generate second three-dimensional mesh
- allow for training of machine-learned models
- make reference to servers, databases, software applications
- discuss actions taken and information sent to/from systems
- describe flexibility of computer-based systems
- provide variations and equivalents to embodiments

### Additional Disclosure

- discuss inherent flexibility of computer-based systems
- describe alterations, variations, and equivalents to embodiments
- intend to cover such alterations, variations, and equivalents

