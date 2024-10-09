# DESCRIPTION

## RELATED APPLICATION INFORMATION

- claim priority

## BACKGROUND

### Technical Field

- relate to imaging

### Description of the Related Art

- motivate SfM

## SUMMARY

- introduce method
- input images
- geometric solver branch
- CNN branch
- fuse solutions
- provide computer program product

## DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS

- introduce embodiments of the present invention
- describe method for two-view relative pose estimation
- apply method in various platforms or systems
- use uncertainty-based probabilistic framework to fuse geometric and CNN prediction
- describe intuition underlying pipeline
- obtain geometric uncertainty via Jacobian of error functions
- design network to predict uncertainty associated with camera pose prediction
- fuse two predictions using Bayes' theorem
- describe novel network architecture with self-attention mechanism
- implement attention mechanism in graph neural network
- describe FIG. 1, block diagram of computing device 100
- describe computing device 100 components
- describe processor 110
- describe memory 130
- describe data storage device 140
- describe communication subsystem 150
- describe peripheral devices 160
- describe hardware processor subsystem
- describe data processing elements
- describe on-board memories
- describe software elements
- describe dedicated circuitry
- describe FIG. 2, block diagram of probabilistic fusion pipeline 200
- describe camera 210 and image capture
- describe 5-point solver and Bundle Adjustment module 230
- describe pose and uncertainty output from geometric method
- describe CNN 250 and pose and uncertainty output
- describe fused pose 270 output
- motivate present invention due to limitations of geometrical solver
- describe limitations of geometrical solver
- describe geometric uncertainty
- describe geometric solution
- describe uncertainty associated with optimum
- describe geometric-CNN pose fusion framework
- introduce ResNet architecture
- explain graph neural network and geometric feature
- motivate probabilistic geometric-CNN pose fusion
- derive Bayes law for sensor fusion
- define motion parameterization
- discuss translation parameterization
- introduce circular fusion
- discuss rotation parameterization
- describe self-attention graph neural network
- explain network architecture
- motivate self-attention mechanism
- describe message passing layers
- define query, key, and value
- compute message
- illustrate circular fusion
- describe method for fusing geometrical and CNN relative camera pose
- receive two images
- input images into geometric solver branch
- input images into CNN branch
- fuse first and second solutions
- perform action responsive to fused pose
- describe computer program product
- define computer readable storage medium
- explain computer readable program instructions
- describe network for downloading instructions
- explain computer readable program instructions execution
- describe flowchart and block diagrams
- explain implementation of systems, methods, and computer program products
- describe special purpose hardware-based systems
- explain reference to "one embodiment"
- describe use of "and/or" and "at least one of"
- explain scope of invention
- describe modifications without departing from scope
- explain feature combinations without departing from scope
- describe appended claims
- summarize invention
- conclude description

