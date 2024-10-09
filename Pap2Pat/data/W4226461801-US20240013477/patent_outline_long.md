# DESCRIPTION

## TECHNICAL FIELD

- relate to 3D scene modeling

## BACKGROUND

- introduce NeRF networks

## SUMMARY

- outline scene modeling system
- describe embodiments

## DETAILED DESCRIPTION

- introduce scene modeling systems
- describe limitations of conventional scene modeling systems
- motivate neural point cloud for scene modeling
- describe conventional ray marching techniques
- highlight limitations of conventional NeRF-based scene models
- introduce certain embodiments of scene representation model
- describe generating neural point cloud for scene representation
- explain selecting shading points along rays for output image generation
- describe advantages of certain embodiments
- introduce example of scene modeling system
- describe receiving input 2D images and request to generate 3D scene
- apply scene representation model to input 2D images
- generate view of 3D scene based on view coordinates
- describe transmitting output image to user computing device
- introduce example operating environment for generating 3D scene
- describe computing environment for generating 3D scene
- introduce scene modeling system and its components
- describe applying scene representation model to input images
- generate 3D scene using point cloud generation model and point-based neural rendering model
- describe model training subsystem for training scene representation model
- introduce scene representation subsystem and its components
- describe receiving input images and request to display 3D scene
- employ scene representation model to generate 3D scene
- describe generating 3D scene using volume rendering process
- introduce additional details about generating 3D scene
- describe training scene representation model using model training subsystem
- introduce example of image modification model
- describe scene representation model for generating 3D scene
- generate neural point cloud using point cloud generation model
- describe point cloud generation model
- render view of 3D scene using point-based neural rendering model
- describe point-based neural rendering model
- introduce example method for generating neural point cloud
- describe aggregating neural point features for shading point
- introduce example process for applying scene representation model
- describe generating output image defining view of 3D scene
- conclude detailed description of certain embodiments
- define neural point cloud
- derive equations for neural point cloud
- describe application of neural point cloud
- introduce scene representation model
- describe configuration of scene representation model
- describe training of scene representation model
- introduce process for generating 3D scene
- receive input images
- apply scene representation model
- transmit output image
- describe modification of online computing environment
- introduce user interface
- describe generation of neural point cloud
- generate point cloud for each 2D input image
- assign properties to points of point cloud
- combine point clouds
- describe neural point cloud properties
- illustrate generation of neural point cloud
- introduce method for rendering output image
- describe rendering of output image
- describe volume rendering process
- describe differentiable ray marching
- describe application of scene representation model
- describe transmission of output image
- describe modification of online computing environment
- describe user interface
- illustrate rendering of output image
- receive requested view for 3D scene
- conduct point-based neural rendering to generate view of 3D scene
- transform neural point cloud to view coordinates
- determine shading points along ray projected through neural point cloud
- project ray through neural point cloud for each pixel of output image
- select set of shading points along ray
- query neighboring neural points around location x within certain radius R
- represent point-based radiance field as neural module
- perform regression using PointNet-like neural network
- process each neighboring neural point and aggregate multi-point information
- predict new feature vector using MLP
- determine shading point features by aggregating neural point properties
- use inverse distance weighting method to aggregate neural features
- determine whether output image includes additional pixels
- repeat sub-blocks for each remaining pixel of output image
- determine color value via volume rendering for each pixel of output image
- use MLP to regress view-dependent radiance for shading point
- perform volume rendering to determine color value for pixel
- determine rendering loss by comparing pixel color value against ground truth pixel color value
- construct grid index and identify grids including neural points
- place shading points inside grids comprising neural points
- identify neural points within radius of shading point
- retrieve information associated with each neural point within radius of shading point
- execute computer-executable program code stored in memory component
- access information stored in memory component
- include any suitable non-transitory computer-readable medium for storing program code
- include any suitable processing device for executing program code
- include any suitable memory component for storing program data
- include any suitable network interface device for establishing data connection
- include any suitable input device for receiving input
- include any suitable presentation device for providing output
- offer service for providing view of 3D scene based on input images
- provide service under Software as a Service (SaaS) model
- store program code and program data in memory component of server computer
- execute program code that configures processing device to perform operations
- implement scene representation subsystem and model training subsystem
- store one or more datasets and models in memory component
- establish data connection to data network using network interface device
- communicate with user devices via data network
- include any suitable computer-readable medium for storing program code
- include any suitable processing device for executing program code
- include any suitable memory component for storing program data
- include any suitable network interface device for establishing data connection
- include any suitable input device for receiving input
- include any suitable presentation device for providing output
- offer service for providing view of 3D scene based on input images
- provide service under Software as a Service (SaaS) model
- store program code and program data in memory component of server computer
- execute program code that configures processing device to perform operations
- implement scene representation subsystem and model training subsystem
- communicate with user devices via data network

### General Considerations

- provide context for detailed description
- clarify terminology for computing actions
- describe flexibility of system architecture
- discuss software implementation options
- outline method embodiment variations
- clarify open-ended language usage
- explain communication techniques
- note non-limiting nature of disclosure

