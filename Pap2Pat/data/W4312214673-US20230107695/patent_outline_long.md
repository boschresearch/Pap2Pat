# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate ASR systems

## SUMMARY

- introduce ASR model
- describe encoder network
- describe prediction network
- describe joint network
- fuse representations
- optional regularization method
- optional joint network structure
- optional audio encoder structure
- optional prediction network structure

## DETAILED DESCRIPTION

- introduce RNN-T architecture for streaming ASR
- describe RNN-T components: audio encoder, prediction network, joint network, output layer
- explain acoustic representations generated by audio encoder
- explain text representations generated by prediction network
- describe joint network fusing acoustic and text representations
- introduce Bayes' rule for decoding
- describe mathematical expression for P(y|x1:T)
- explain acoustic encoder, prediction network, and joint network equations
- introduce gating technique for fusing representations
- describe mathematical expression for gating
- introduce bilinear pooling technique for fusing representations
- describe mathematical expression for bilinear pooling
- compare gating and bilinear pooling
- introduce novel joint network combining gating and bilinear pooling
- describe benefits of combining gating and bilinear pooling
- explain prediction network regularization routines
- describe purpose of prediction network regularization routines
- introduce example speech environment
- describe user device and audio system
- explain ASR system and RNN-T model
- describe audio subsystem and input acoustic frames
- explain RNN-T model processing and output transcription
- introduce rescorer and final speech recognition result
- describe user interface generator and presentation of transcription
- explain digital assistant application and natural language processing
- describe response to user query
- introduce FIG. 1 and speech environment
- describe user device and audio capture device
- explain ASR system and RNN-T model on user device or remote server
- describe audio subsystem and input acoustic frames
- explain RNN-T model processing and output transcription
- introduce FIG. 2 and RNN-T model architecture
- describe encoder network and acoustic representations
- describe prediction network and text representations
- explain joint network and fusion of representations
- describe final Softmax output layer
- explain benefits of novel joint network
- describe applications of RNN-T model
- conclude description of RNN-T model and its components
- introduce RNN-T model
- describe prediction/decoder network
- describe joint network
- explain output distribution
- introduce novel structure
- describe bilinear pooling layer
- describe gating layer
- explain stacking of bilinear pooling and gating layers
- describe Softmax layer
- explain output label selection
- describe feature vectors
- describe encoder network
- describe conformer encoder blocks
- describe time reduction rate
- describe final linear normalization layer
- describe alternative encoder networks
- describe prediction network
- describe LSTM-based network
- describe joint network
- describe hidden units
- describe alternative prediction networks
- describe training imbalances
- describe prediction network regularization routines
- describe re-computing dense representation
- describe conformer block
- describe RNN-T model
- illustrate arrangement of operations for method 400
- receive sequence of acoustic frames
- generate higher order feature representation
- generate dense representation
- generate probability distribution over possible speech recognition hypotheses
- illustrate computing device 500
- describe processor 510
- describe memory 520
- describe storage device 530
- describe high-speed interface/controller 540
- describe low speed interface/controller 560
- describe display 580
- illustrate various implementations of computing device 500
- describe digital electronic and/or optical circuitry
- describe integrated circuitry
- describe specially designed ASICs
- describe computer hardware
- describe firmware
- describe software
- describe computer programs
- describe software application
- describe machine-readable medium
- describe computer-readable medium
- describe scope of disclosure

