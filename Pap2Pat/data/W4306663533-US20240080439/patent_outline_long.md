# DESCRIPTION

## BACKGROUND

### Technical Field

- define technical field

### Description of Related Art

- motivate VR videos
- limitations of VVC

## SUMMARY

- motivate disclosure
- introduce intra-frame predictive coding method
- define coding unit feature
- define texture feature
- define 360-degree video feature
- describe S1 step
- describe S2 step
- describe S3 step
- describe S4 step
- define block shape ration
- define texture factors
- define sampling factor
- describe RMD candidate list
- describe intra-frame angle mode decision
- describe intra-frame block partition
- summarize method

## DESCRIPTION OF THE EMBODIMENTS

- introduce neural networks
- motivate 360-degree video coding
- define coding unit feature
- define texture feature
- define 360-degree video feature
- describe intra-frame predictive coding method
- introduce FIG. 1
- describe operation S1
- input features into neural network
- skip partition mode based on output threshold
- perform intra-frame block partition
- obtain intra-frame block partition schemes
- describe QT, BTH, BTV, TTH, and TTV partition modes
- define coding unit feature
- describe width, height, depth, quadtree depth, multi-tree depth
- describe block shape ratio
- describe quantization parameter
- describe horizontal angle mode type
- describe vertical angle mode type
- correct angle mode determination
- describe texture feature
- describe variance of pixel value
- describe normalized mean square error
- describe horizontal texture factor
- describe vertical texture factor
- describe weight between horizontal and vertical textures
- describe directional complexity
- describe 360-degree video feature
- describe latitude of CU block
- describe sampling factor at each latitude
- construct classifier model based on neural network
- input features into classifier model
- obtain output to determine whether to skip partition mode
- introduce multi-layer perceptron
- describe schematic diagram of neural network
- describe output of neural network
- set output threshold value
- fine-tune output threshold value
- perform CU partitioning
- determine whether to skip partition mode
- perform intra-frame block partition
- generate intra-frame block partition schemes
- describe operation S2
- determine length of RMD candidate list
- decide intra-frame angle mode
- obtain intra-frame angle mode
- fill pixels in each intra-frame block partition scheme
- describe operation S3
- calculate RDO loss
- perform intra-frame coding predictive coding

