# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate multi-object 3D shape reconstruction

## SUMMARY

- introduce single-shot multi-object 3D shape reconstruction
- describe system components
- explain heatmap and 3D parameter map inference
- summarize advantages over other approaches

## DETAILED DESCRIPTION

- introduce 3D shape reconstruction and 6D pose and size estimation
- motivate instance-level and category-level 6D pose estimation
- describe limitations of two-stage pipeline approach
- introduce single-shot approach for 3D shape reconstruction and 6D pose and size estimation
- describe system configuration for 6D pose and size estimation
- obtain RGB-D image as input
- extract RGB features and depth features using residual neural network
- concatenate RGB features and depth features
- generate feature pyramid using FPN backbone
- infer heatmap based on feature pyramid
- identify peaks in heatmap corresponding to object centers
- infer 3D parameter map based on feature pyramid
- sample 3D parameter map at peak locations
- generate point clouds based on latent shape codes, 6D poses, and 1D scales
- describe application of point clouds in robotic device control and simulation
- illustrate robotic device with 6D pose and size estimator system
- describe 6D pose and size estimator system architecture
- describe 6D pose and size estimator module functionality
- outline database components for 6D pose and size estimation
- illustrate process overview
- represent objects by 2D locations
- generate RGB and depth features
- generate feature pyramid
- predict heatmap
- compute ground truth heatmaps
- represent 3D information as parameter maps
- train encoder-decoder network
- infer 3D parameter map
- define 6D pose and size estimator module
- motivate auxiliary depth reconstruction loss
- describe joint optimization for detection, reconstruction, and localization
- outline inference process for 6D pose and size estimator module
- generate concatenated features from RGB and depth features
- predict heatmap and identify peaks corresponding to object centers
- associate heatmap probabilities with detection confidence
- infer 3D parameter map and sample object 3D map
- generate point clouds based on latent shape codes, 6D poses, and 1D scales
- utilize point clouds for robotic device navigation or computer simulation
- illustrate flowchart of method for single-shot multi-object 3D shape reconstruction and categorical 6D pose and size estimation
- define robotic device
- describe vehicle systems
- introduce autonomous vehicle
- describe processor and data store
- describe map data
- describe terrain map
- describe static obstacle map
- describe sensor data
- describe sensor system
- describe robotic device sensor
- describe environment sensor
- describe radar, LIDAR, sonar, and camera sensors
- describe input and output systems
- describe communication between processor and robotic device systems
- describe modules and artificial intelligence
- describe flowcharts and block diagrams
- describe hardware and software implementation
- describe computer-readable storage medium
- describe scope of invention

