# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate robotics and prosthetics
- limitations of traditional sensors
- importance of object manipulation

## SUMMARY

- introduce multi-modal fingertip sensors
- describe sensor components
- explain proximity sensor function
- explain pressure sensor function
- describe circuit function
- mention computer-readable storage media

## DETAILED DESCRIPTION

- introduce robotics and prosthetics
- describe limitations of traditional tactile sensors
- motivate multi-modal fingertip sensors
- describe application of sensors in robotics and prosthetics
- introduce infrared emitter-detector and barometer sensor
- describe integration of sensors into prosthetic finger
- explain use of I2C communication between sensors and controller
- describe synthesis of multi-modal sensory information
- introduce Gaussian processes for calibrated force measurements
- describe supervised machine learning approaches
- list technical effects, advantages, and improvements
- describe embodiment as special-purpose hardware
- describe embodiment as programmable circuitry
- describe machine-readable medium for storing instructions
- explain use of phrases "in some embodiments"
- describe FIG. 1: hand with multi-modal tactile sensors
- describe assembly of sensor
- describe use of barometric pressure sensor and infrared proximity sensor
- describe substrate and cavity formation
- describe 3D printing of fingers
- describe overmolding of elastomer
- describe logic circuit for multiplexing communication signals
- describe use of microcontroller for multiplexing
- describe firmware for proximity calculation and calibration
- describe custom LabView program for visualizing signals
- describe FIG. 3: digit of prosthetic hand
- describe FIG. 4: portion of thumb
- describe cavity formation in digit and thumb
- describe experimental characterization of sensor performance
- describe Instron material testing machine
- describe application of calibrated loads
- describe data collection procedure
- describe spatial and angular conditions
- describe sensor fusion study
- describe dynamic loading and unloading cycles
- describe data collection for classifying direction of probing
- describe data collection for determining spatial location of impact
- describe calibration of multi-modal fingertip data
- describe use of Gaussian process in regression setting
- describe supervised learning problems
- describe use of support vector machine and convolutional neural network
- describe FIG. 6: block diagram of fingertip sensor
- describe components of fingertip sensor
- describe pressure sensor and analog to digital converter
- describe IR or distance sensor and analog to digital converter
- describe microprocessor and I2C communications port
- describe FIG. 7: block diagram of centerboard
- describe components of centerboard
- describe outputs providing control actions for actuators
- show Gaussian process regression fit
- present individual curve fits
- discuss interaction between elastomer shell and sensors
- frame problem as classification in supervised learning framework
- collect data for probing direction classification
- preprocess data
- standardize individual loading and unloading curves
- use SVM as baseline classifier
- explore variations of barometer and IR sensor values
- include data points of maximum force and minimum force
- use polynomial kernel with penalty factor
- perform cross validation
- train small neural network to classify probing direction
- feed raw data into network
- include two 2D-convolution layers and dense output layer
- perform cross validation on training and testing dataset
- determine spatial location of impact on finger
- use same supervised learning models with different parameters
- collect data by probing finger at different locations
- use custom-made 3D-printed pillows to align/offset finger
- segment data into single combination of loading and unloading curves
- standardize data before feeding into models
- extract features for training SVM
- use radial basis function kernel with penalty factor
- perform cross validation
- discuss applications in robotic/prosthetic grasping and manipulation
- fuse pressure and proximity sensor data to force
- discuss limitations of proposed methods
- discuss potential of sensor assembly in neural interfaces
- illustrate flowchart for producing force, proximity, and contact signals
- collect raw pressure and distance data
- filter and smooth raw data
- apply calibration offsets or modifications
- generate force signal and proximity signal
- detect contact event
- illustrate flowchart for identifying contact event
- receive raw distance signal
- compute derivative of raw distance data
- determine whether derivative exceeds threshold
- generate contact signal
- illustrate block diagram for integration of machine learning engine
- collect raw barometer and IR data
- communicate data to machine learning engine
- compute total force signal, position of force signal, and angular orientation of force signal
- illustrate flowchart for generating biomimetic response
- collect raw barometer and IR data
- monitor for initial physical contact
- generate biomimetic signals

## CONCLUSION

- define terms and phrases
- specify word meanings
- describe interpretation of lists
- disclaim limitations of description
- discuss modifications and variations
- describe applicability to other systems
- discuss combining elements and acts
- describe flexibility of implementation
- discuss claim forms and scope

