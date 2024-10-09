# DESCRIPTION

- claim benefit of European Patent Application

## TECHNICAL FIELD

- introduce people counting based on radar measurements

## BACKGROUND

- motivate people counting
- limitations of image-based people counting

## SUMMARY

- summarize people counting based on radar measurements
- define 1st range-Doppler measurement map
- define 2nd range-Doppler measurement map
- estimate people count using neural network algorithm
- input 1st range-Doppler measurement map into 1st data processing pipeline
- input 2nd range-Doppler measurement map into 2nd data processing pipeline
- include range-Doppler convolutional layers
- process outputs in regression block
- output 1-dimensional value predicting people count
- include fully-connected layer with single neuron
- output higher-dimensional value
- predict people count based on position in embedding space
- define micro-Doppler range-Doppler measurement map
- define macro-Doppler range-Doppler measurement map
- determine velocity resolution
- include program code for computer-implemented method
- load and execute program code
- perform computer-implemented method
- determine 1st range-Doppler measurement map
- determine 2nd range-Doppler measurement map
- estimate people count
- input measurement maps into neural network algorithm
- apply tracking filter
- track evolution of output in embedding space
- obtain multiple training radar measurement datasets
- perform training of neural network algorithm
- use label-aware ranked loss

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

- introduce electrical devices and circuits
- describe functionality of electrical devices and circuits
- explain limitations of electrical devices and circuits
- motivate people counting based on radar measurements
- introduce radar measurement operation
- describe radar sensor and its functionality
- explain pulsed operation of radar sensor
- describe Doppler frequency shift and its application
- motivate machine-learning algorithm for people counting
- introduce range-doppler measurement maps
- describe 2-D Fourier transformation for obtaining RDIs
- introduce 2-D angular measurement maps
- describe beamforming algorithm for obtaining 2-D angular measurement maps
- introduce range-angle measurement maps
- motivate differentiation between micro-Doppler and macro-Doppler features
- describe macro-Doppler features and micro-Doppler features
- introduce first RDI for macro-Doppler features
- introduce second RDI for micro-Doppler features
- describe input to ML algorithm
- introduce macro-Doppler data processing pipeline
- introduce micro-Doppler data processing pipeline
- describe neural network architecture
- explain spatial contraction and expansion in encoder and decoder branches
- describe 2-D convolutional layers in macro-Doppler and micro-Doppler data processing pipelines
- introduce output section for processing combined outputs
- describe joint training of macro-Doppler and micro-Doppler data processing pipelines
- motivate separate processing of micro-Doppler and macro-Doppler features
- introduce connecting sections for joining macro-Doppler and micro-Doppler data processing pipelines
- describe feature fusion at connecting sections
- introduce people counting using radar sensor
- motivate correlation between macro-Doppler and micro-Doppler features
- describe use of connecting sections to capture correlations
- enhance robustness against variation in radar sensor pose
- provide options for implementing connecting sections
- describe combination layer with filter parameters
- describe concatenation layer and convolutional layer
- combine different implementations for combination layers
- include regression block in neural network
- describe output of regression block
- control dimensionality of output using fully-connected layers
- determine feature vector and people count
- describe postprocessing techniques for people counting
- apply smoothing filter to avoid artificial changes
- apply tracking filter to track evolution of embedding output
- predict position in embedding space using tracking filter
- use Kalman filter to track angular motions in embedding space
- order predefined regions in embedding space
- use label-aware ranked loss to achieve ordering
- describe system including radar sensor and processing device
- illustrate radar sensor and its components
- describe data processing for people counting
- illustrate data processing using neural network and smoothing filter
- preprocess radar measurement dataset to obtain macro-Doppler RDI and micro-Doppler RDI
- execute MTI filtering and 2-D FFT for macro-Doppler preprocessing
- implement high-pass filter to form macro-Doppler RDI
- integrate multiple frames for micro-Doppler preprocessing
- apply moving target indication filter and 2-D FFT for micro-Doppler preprocessing
- use Hamming window to reduce spectral leakage
- introduce radar measurement data
- explain structure of radar measurement frame
- describe fast-time and slow-time dimensions
- explain antenna dimension
- define duration of radar measurement frames
- describe chirps repetition time
- calculate maximum resolve Doppler velocity
- explain frequency range of chirps
- calculate range resolution
- describe frame repetition frequency
- illustrate neural network architecture
- explain encoder branch
- describe regression block
- illustrate example implementation of encoder branch
- describe macro-Doppler data processing pipeline
- describe micro-Doppler data processing pipeline
- explain connecting sections
- describe output section
- illustrate flowchart of people counting method
- train neural network
- determine people count without ground truth
- illustrate flowchart of training method
- obtain multiple sets of training radar measurement datasets
- preprocess training datasets
- input datasets to neural network
- compare prediction with ground truth
- explain triplet loss
- explain label-aware ranked loss
- illustrate flowchart of inference method
- obtain radar measurement dataset
- preprocess dataset
- input dataset to neural network
- output prediction of people count
- apply tracking filter
- illustrate tracking in embedding space
- define regions in embedding space
- explain constant velocity motion model
- illustrate use cases
- describe monitoring people entering and exiting doorways
- describe gathering customer traffic data
- describe counting people for energy savings

