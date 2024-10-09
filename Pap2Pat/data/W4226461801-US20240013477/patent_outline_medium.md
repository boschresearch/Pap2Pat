# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate NeRF networks

## SUMMARY

- summarize scene modeling system

## DETAILED DESCRIPTION

- introduce scene modeling systems
- describe limitations of conventional scene modeling systems
- motivate neural point cloud for scene modeling
- describe conventional ray marching techniques
- highlight limitations of conventional NeRF-based scene models
- introduce scene representation model
- describe generating neural point cloud
- explain selecting shading points along rays
- describe advantages of scene representation model
- provide non-limiting example of scene modeling system
- describe receiving input 2D images and request to generate 3D scene
- explain applying scene representation model to input images
- describe generating view of 3D scene
- introduce example operating environment for generating 3D scene
- describe scene modeling system and its components
- explain training scene representation model
- introduce example of image modification model
- describe scene representation model components and process
- define neural point cloud
- derive point cloud generation model
- describe scene representation model
- illustrate rendering process
- motivate volume rendering loss
- describe training process
- outline process for generating 3D scene
- receive input images
- apply scene representation model
- transmit output image
- generate neural point cloud
- assign properties to points
- combine point clouds
- receive requested view for 3D scene
- conduct point-based neural rendering to generate view
- transform neural point cloud to view coordinates
- determine shading points along ray projected through neural point cloud
- project ray through neural point cloud for each pixel
- select set of shading points along ray
- query neighboring neural points around shading point location
- represent point-based radiance field as neural module
- perform regression using PointNet-like neural network
- process each neighboring neural point and aggregate multi-point information
- determine shading point features by aggregating neural point properties
- use inverse distance weighting method to aggregate neural features
- determine whether output image includes additional pixels
- repeat sub-blocks for each remaining pixel
- determine color value via volume rendering for each pixel
- use MLP to regress view-dependent radiance for shading point
- perform volume rendering to determine color value for pixel
- determine rendering loss by comparing pixel color value against ground truth
- aggregate neural point features for shading point
- construct grid index and identify grids with neural points
- place shading points inside grids with neural points
- identify neural points within radius of shading point
- retrieve information associated with each neural point
- execute program code to perform operations
- store program data in memory component

### General Considerations

- set forth specific details
- define computing terms
- describe computing devices
- discuss variations and equivalents

