# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate video compression
- limitations of sub-block based affine motion compensation

## SUMMARY

- introduce prediction refinement with optical flow (PROF) for affine coded block
- motivate PROF for better trade-off between complexity and accuracy
- define PROF process for sub-block of affine coded block
- describe performing PROF process with optical flow processing
- explain obtaining refined prediction sample values
- introduce constraint conditions for applying PROF
- describe determining constraint conditions
- explain first indication information for PROF
- explain second indication information for PROF
- describe fallbackModeTriggered variable
- explain obtaining second prediction matrix
- generate horizontal and vertical prediction gradient matrices
- calculate delta prediction value
- describe sub-block based affine motion compensation
- explain motion vector difference calculation
- describe representation of second prediction matrix elements
- describe representation of horizontal and vertical prediction gradient matrices
- introduce second aspect of disclosure
- describe performing PROF process with fulfilled optical flow decision conditions
- explain beneficial effects of PROF on compression performance
- summarize prediction refinement method
- introduce apparatus for prediction refinement
- describe determining unit of apparatus
- describe prediction processing unit of apparatus
- specify constraint conditions for applying PROF
- describe obtaining second prediction matrix
- describe generating horizontal and vertical prediction gradient matrices
- calculate delta prediction value
- introduce fourth aspect of disclosure
- describe apparatus for prediction refinement with optical flow
- specify optical flow decision conditions
- describe obtaining second prediction matrix
- describe generating horizontal and vertical prediction gradient matrices
- calculate delta prediction value
- introduce fifth aspect of disclosure
- describe encoder
- describe decoder
- describe computer program and computer-readable storage medium

## DETAILED DESCRIPTION OF THE EMBODIMENTS

- introduce video coding
- define video coding components
- describe video encoding and decoding
- motivate lossless and lossy video coding
- explain hybrid video codecs
- describe block-based video coding
- introduce video coding system 10
- describe source device 12
- describe picture source 16
- describe pre-processor 18
- describe video encoder 20
- describe communication interface 22
- describe destination device 14
- describe communication interface 28
- describe decoder 30
- describe post-processor 32
- describe display device 34
- describe encoder and decoder implementation
- describe video encoder 20 components
- describe residual calculation unit 204
- describe transform processing unit 206
- describe quantization unit 208
- define residual calculation unit
- describe transform processing
- motivate quantization
- describe quantization process
- explain inverse quantization
- describe inverse transform processing
- explain reconstruction
- describe filtering
- explain loop filter unit
- describe decoded picture buffer
- motivate mode selection
- describe partitioning
- explain inter-prediction
- describe intra-prediction
- explain prediction block generation
- describe rate distortion optimization
- explain tree-partitioning
- describe coding tree unit
- explain video encoder operation
- describe motion compensation unit
- perform inter prediction
- generate syntax elements
- apply entropy encoding
- bypass compression
- describe alternative encoder structures
- introduce video decoder
- receive encoded picture data
- parse bitstream
- perform entropy decoding
- apply inverse quantization
- apply inverse transform
- reconstruct residual blocks
- filter reconstructed blocks
- store decoded pictures
- output decoded picture
- perform prediction
- describe alternative decoder structures
- introduce video coding device
- introduce AMVP mode
- introduce merge mode
- describe candidate motion vector list
- describe pruning of candidate motion vector list
- motivate non-translational motion model
- introduce 4-parameter affine motion model
- describe 4-parameter affine motion model
- introduce 6-parameter affine motion model
- describe 6-parameter affine motion model
- introduce inherited control point motion vector prediction method
- describe inherited control point motion vector prediction method
- introduce constructed control point motion vector prediction method
- describe constructed control point motion vector prediction method 1
- describe combining motion vectors of neighboring encoded blocks
- describe combining motion vectors of top-left and top-right samples
- describe combining motion vectors of top-left, top-right, and bottom-left samples
- describe using motion vectors of two encoded blocks as candidate control point motion vectors
- describe using motion vectors of three encoded blocks as candidate control point motion vectors
- conclude constructed control point motion vector prediction method
- define motion vectors
- introduce control point motion vectors prediction method
- obtain motion information of control points
- combine motion information of control points
- construct affine motion models
- construct bilinear motion model
- traverse models in preset order
- scale control point motion vectors
- convert control points to same location
- provide conversion formulas
- define formulas for converting control points
- describe affine motion model-based advanced motion vector prediction mode
- construct candidate motion vector list
- determine optimal control point motion vector predictors candidate
- determine control point motion vectors
- describe affine merge mode
- construct control point motion vectors merge candidate list
- determine control point motion vectors candidate
- describe syntax elements for inter prediction mode
- define variables for maximum list length and prediction direction
- describe decoding method using inter prediction unit
- parse bitstream to determine inter prediction mode
- construct candidate motion vector list for affine motion model-based AMVP mode
- describe process of constructing candidate motion vector list using inherited control point motion vector prediction method
- describe affine motion model
- derive control point motion vectors
- construct candidate motion vector list
- parse bitstream and determine optimal control point motion vector predictors
- parse bitstream and determine control point motion vectors
- obtain motion vector of each sub-block
- perform motion compensation for each sub-block
- construct motion information candidate list
- derive candidate control point motion information using inherited method
- add candidate control point motion information to motion information candidate list
- derive candidate control point motion information using constructed method
- add candidate control point motion information to motion information candidate list
- prune and sort motion information candidate list
- truncate or pad motion information candidate list
- describe motion compensation unit
- describe motion information processing
- combine motion information
- add motion information to candidate list
- traverse combinations of motion information
- determine reference frame index
- scale control point motion vector
- parse bitstream and determine optimal control point motion information
- obtain motion vector of each sub-block
- perform motion compensation for each sub-block
- calculate gradient values of prediction signal
- perform prediction refinement with optical flow

### Embodiment 1

- constrain delta prediction method

### Embodiment 2

- propose sub-block size selection
- discuss concurrency and accuracy of gradient calculation
- introduce gradient value calculation based on 16×16 granularity
- describe prediction refinement with optical flow (PROF) method
- determine optical flow decision conditions
- perform PROF process for current sub-block
- obtain refined prediction sample values
- list optical flow decision conditions
- derive indication information for PROF
- determine fallback mode triggered
- specify conditions for using PROF
- define embodiment 2
- specify optical flow decision conditions
- describe PROF processing for sub-blocks
- calculate delta prediction value
- obtain refined prediction sample value
- provide alternative implementation
- describe step 1102
- obtain second prediction matrix
- calculate horizontal and vertical prediction gradient matrices
- calculate delta prediction value matrix
- obtain refined third prediction matrix
- describe another method for PROF
- determine optical flow decision conditions
- perform PROF process or skip
- set first indicator based on optical flow decision conditions
- provide examples of optical flow decision conditions
- introduce embodiment 2
- describe PROF process
- calculate prediction matrices
- calculate gradient matrices
- calculate delta prediction value matrix
- obtain refined prediction matrix
- describe alternative designs for uni-prediction
- describe alternative designs for bi-prediction
- describe alternative designs for motion information
- describe alternative designs for prediction matrix
- describe four-step PROF process
- calculate spatial gradients
- define embodiment 2
- derive Δv(i, j)
- describe 4-parameter affine model
- describe 6-parameter affine model
- perform luma prediction refinement
- illustrate apparatus 1500 for prediction refinement
- describe determining unit 1501
- describe prediction processing unit 1503
- explain applications of encoding and decoding methods
- describe content supply system 3100
- explain capture device 3102
- explain terminal device 3106
- illustrate structure of terminal device 3106
- describe protocol proceeding unit 3202
- describe demultiplexing unit 3204
- describe video decoder 3206 and audio decoder 3208
- explain synchronous unit 3212
- discuss implementation of embodiments

