# DESCRIPTION

- claim benefit of European Patent Application

## TECHNICAL FIELD

- introduce people counting based on radar measurements

## BACKGROUND

- motivate people counting

## SUMMARY

- summarize people counting based on radar measurements
- describe advantages of radar-based people counting
- introduce computer-implemented method
- determine 1st range-Doppler measurement map
- determine 2nd range-Doppler measurement map
- estimate people count
- input measurement maps into neural network algorithm
- process outputs in regression block
- output people count
- introduce alternative output
- describe micro-Doppler range-Doppler measurement map
- describe macro-Doppler range-Doppler measurement map
- introduce computer program or computer-program product

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

- introduce electrical devices and circuits
- describe functionality of electrical devices and circuits
- explain limitations of electrical devices and circuits
- motivate people counting based on radar measurements
- describe radar measurement operation
- explain radar sensor and its functionality
- describe Doppler frequency shift and its application
- motivate machine-learning algorithm for people counting
- describe preprocessing of radar measurement data
- explain range-doppler measurement maps and their application
- describe micro-Doppler and macro-Doppler features
- explain multiple data-processing pipelines in ML algorithm
- describe neural network architecture and its components
- motivate joint training of macro-Doppler and micro-Doppler data processing pipelines
- introduce people counting using radar sensor
- motivate correlation between macro-Doppler and micro-Doppler features
- describe connecting sections for robust people counting
- implement connecting sections using combination layer
- implement connecting sections using concatenation layer
- describe regression block for people count output
- describe postprocessing techniques for accurate people count
- apply smoothing filter to avoid artificial changes
- apply tracking filter to track embedding output
- describe system architecture for people counting
- describe radar sensor and its components
- illustrate data processing for people counting
- describe preprocessing to obtain macro-Doppler and micro-Doppler RDIs
- illustrate 2-D fast Fourier transformation for macro-Doppler preprocessing
- describe radar measurement data
- explain structure of raw data in radar measurement frame
- define fast-time dimension and slow-time dimension
- describe macro-Doppler data processing pipeline
- describe micro-Doppler data processing pipeline
- illustrate connecting sections of convolutional NN
- describe output section of convolutional NN
- illustrate regression block
- describe training of NN
- explain triplet-type loss
- describe LAR loss
- illustrate training using LAR loss
- describe inference of people count using NN
- illustrate preprocessing of radar measurement dataset
- describe input to NN
- describe output of regression block
- illustrate tracking filter
- describe embedding space
- illustrate regions in embedding space
- describe use cases

