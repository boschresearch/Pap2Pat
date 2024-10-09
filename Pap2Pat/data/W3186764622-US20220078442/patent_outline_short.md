# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate video compression

## SUMMARY

- introduce prediction refinement with optical flow (PROF) for affine coded block
- motivate PROF for better trade-off between coding complexity and prediction accuracy
- define PROF process for sub-block of affine coded block
- describe optical flow processing for current sub-block
- explain obtaining refined prediction sample values
- outline constraint conditions for applying PROF
- describe possible implementation forms of PROF
- detail generating second prediction matrix and prediction gradient matrices
- calculate delta prediction value based on prediction gradient values and motion vector difference
- summarize beneficial effects of PROF on compression performance
- define prediction refinement method
- describe apparatus for prediction refinement
- detail prediction processing unit
- explain optical flow processing
- describe alternative apparatus for prediction refinement
- detail alternative prediction processing unit
- describe encoder and decoder
- outline computer program and storage medium
- summarize video picture encoding and decoding methods

## DETAILED DESCRIPTION OF THE EMBODIMENTS

- introduce video coding and its components
- describe video coding standards and their characteristics
- motivate video coding system and its components
- describe source device and its components
- describe destination device and its components
- illustrate video coding system with FIG. 1A
- describe encoder and decoder implementation
- describe video encoder and its components
- describe picture partitioning and block structure
- describe residual calculation and processing
- describe entropy encoding and output
- describe residual calculation unit
- describe transform processing unit
- describe quantization unit
- describe inverse quantization unit
- describe inverse transform processing unit
- describe reconstruction unit
- describe filtering unit
- describe decoded picture buffer
- describe mode selection unit
- describe motion compensation unit
- describe entropy encoding unit
- describe decoder and decoding method
- describe entropy decoding unit
- describe inverse quantization unit
- describe inverse transform unit
- describe reconstruction unit
- describe filtering unit
- describe video coding device
- introduce AMVP mode
- introduce merge mode
- describe candidate motion vector list
- motivate non-translational motion model
- describe 4-parameter affine motion model
- describe 6-parameter affine motion model
- introduce inherited control point motion vector prediction method
- introduce constructed control point motion vector prediction method
- describe constructed control point motion vector prediction method 1
- define motion vectors
- obtain motion information of control points
- combine motion information to construct motion models
- convert motion models to standard representations
- scale control point motion vectors
- define affine motion model-based advanced motion vector prediction mode
- describe constructing candidate motion vector list
- determine optimal control point motion vector predictors candidate
- determine control point motion vectors
- describe affine merge mode
- explain syntax elements for inter prediction mode
- outline decoding method process
- describe affine motion model
- derive control point motion vectors
- construct candidate motion vector list
- parse bitstream and determine optimal control point motion vector predictors
- parse bitstream and determine control point motion vectors
- obtain motion vector of each sub-block
- perform motion compensation for each sub-block
- describe motion information processing
- detail candidate motion vector list construction
- outline motion compensation and prediction signal refinement
- explain gradient value calculation and prediction refinement
- summarize PROF process

### Embodiment 1

- constrain delta prediction method

### Embodiment 2

- propose gradient value calculation
- describe prediction refinement with optical flow
- determine optical flow decision conditions
- derive indication information for applying PROF
- specify conditions for using PROF
- define optical flow decision conditions
- describe PROF processing for sub-blocks
- calculate delta prediction value
- obtain refined prediction sample value
- determine whether to apply PROF
- set indicator based on optical flow decision conditions
- perform PROF processing or skip it
- provide alternative implementations
- describe PROF process
- calculate prediction matrices
- obtain delta prediction value matrix
- refine prediction matrix
- perform sub-block-based affine motion compensation
- calculate spatial gradients
- define embodiment 2
- derive Δv(x, y) equation
- describe apparatus 1500 for prediction refinement
- illustrate content supply system 3100
- describe capture device 3102 and terminal device 3106
- explain protocol proceeding unit 3202 and demultiplexing unit 3204
- describe video decoder 3206, audio decoder 3208, and synchronous unit 3212
- discuss subtitle decoder 3210 and video/audio/subtitle display 3216
- provide general information on implementation and scope

