# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate speech therapy
- limitations of audio-only speech recognition

## SUMMARY

- summarize EEG-based speech prosthetics
- introduce first embodiment
- obtain audio signal
- obtain EEG signals
- obtain acoustic representations
- concatenate features
- provide features to ASR model
- obtain text-based output
- introduce second embodiment

## DETAILED DESCRIPTION

- illustrate device 100
- describe components of device 100
- introduce communication unit 110
- describe transmit processing circuitry 115
- describe microphone 120
- describe receive processing circuitry 125
- describe speaker 130
- describe main processor 140
- describe input/output interface 145
- describe input/output devices 150
- describe memory 160
- describe operating system program 161
- describe applications 162
- describe sensors 180
- describe EEG sensors 182
- describe microphone 184
- describe EMG sensors 186
- describe communication unit 110 operations
- describe TX processing circuitry 115 operations
- describe RX processing circuitry 125 operations
- describe main processor 140 operations
- describe I/O interface 145 operations
- describe input/output devices 150 operations
- illustrate server 200
- describe bus system 205
- describe processing device 210
- describe storage devices 215
- describe communications unit 220
- describe I/O unit 225
- describe memory 230
- describe persistent storage 235
- illustrate architecture 300
- describe deep learning regression stage 301
- describe speech recognition stage 351
- obtain EEG signals
- obtain audio signals
- obtain EMG signals
- remove EMG artifacts from EEG signals
- extract EEG features
- provide EEG features to deep learning model 303
- train deep learning model 303
- obtain acoustic representations from EEG signals
- train ASR model 360
- describe audio input processing
- obtain Mel frequency cepstral coefficients
- concatenate audio input with acoustic representations
- train ASR model
- describe ASR model architecture
- describe isolated speech recognition
- illustrate ASR model 400 architecture
- describe GRU layer
- describe dropout regularization function
- describe dense layer
- describe softmax activation function
- describe training process
- describe continuous speech recognition
- illustrate ASR model 500 architecture
- describe GRU layer as encoder
- describe dense layer with 4-gram language model
- describe softmax activation function
- describe CTC loss function
- describe training process
- describe speaker identification
- illustrate ASR model 600 architecture
- describe GRU layer
- describe dropout regularization function
- describe dense layer
- describe softmax activation function
- describe training process
- describe GRU architecture
- introduce dropout regularization
- describe dense layers
- introduce softmax activation function
- illustrate ASR architecture
- describe real-time speech recognition decoding pipeline
- introduce sensor signals
- describe dry EEG sensor signals
- describe ear EEG sensor signals
- describe dry EMG sensor signals
- describe audio signals
- introduce stream generation modules
- describe EEG and EMG data streams
- describe audio data streams
- remove EMG artifacts
- obtain EEG features
- obtain audio features
- reduce EEG feature dimensionality
- combine EEG features
- introduce deep learning model
- concatenate EEG and audio features
- introduce ASR models
- describe EEG-based speech recognition method
- receive audio signal
- obtain EEG signals
- obtain acoustic representations
- concatenate acoustic and audio features
- provide text-based output

