# DESCRIPTION

- claim benefit of European Patent Application

## TECHNICAL FIELD

- relate to radar devices and methods

## BACKGROUND

- motivate millimeter-wave frequency regime
- describe radar systems
- limitations of tracking targets
- introduce digital filtering approach

## SUMMARY

- introduce radar device
- describe radar device components
- introduce method of operating radar device
- summarize embodiments

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

- introduce radar device with machine learning logic
- describe radar front end and processing circuitry
- explain digital filter and its parameters
- introduce machine learning logic for setting filter parameters
- describe policy network and critic network
- explain policy network outputting filter parameters
- describe critic network outputting reward values
- introduce concept of heads in critic network
- explain training of critic network
- describe out of distribution detection
- explain method of FIG. 3
- receive reflected radar signals
- process reflected radar signals to obtain digital signal
- set filter parameters based on digital signal
- filter digital signal to obtain information about objects
- provide reward values for filter parameters
- perform out of distribution detection
- introduce example implementation of radar front end
- describe millimeter-wave radar device
- explain transmitter and receiver antennas
- describe processing of reflected radar signals
- introduce ADC and processing system
- describe controller and its functions
- explain implementation of processing system
- describe RF and analog circuits
- explain VCO and PLL
- describe mixer and low-pass filter
- introduce ADC and its functions
- describe sampling of beat signals
- explain storage of raw digital data
- introduce sequence of chirps
- describe frame and pulse repetition time
- explain chirp time and bandwidth
- describe sampling frequency and number of samples
- introduce flow chart of processing system
- receive raw ADC data
- perform signal conditioning and filtering
- apply 2D moving target indication filters
- remove response from static targets
- perform FFTs on filtered radar data
- calculate range-Doppler images
- determine angle of arrival using MVDR technique
- generate range-angle image
- generate range-Doppler-angle data cube
- detect targets using OS-CFAR detector
- generate detection image
- cluster targets based on feature characteristics
- use k-means clustering for feature-based clustering
- use DBSCAN algorithm for clustering
- divide radar image into groups of cells with similar descriptors
- associate detected targets with respective tracks
- use feature-based template matching for track assignment
- use geometric features for template matching
- track targets over time using unscented Kalman filter
- perform track filtering
- perform track management tasks
- generate tracks and kill tracks
- set parameters of unscented Kalman filter using machine learning logic
- train policy network, critic network, and value networks using radar data
- use actor-critic approach for machine learning logic
- train policy network based on reward values from critic network
- train critic network simultaneously
- use reinforcement learning for optimizing tracking parameters
- introduce environment and scene
- define tracking performance
- motivate meta-reinforcement learning
- describe meta-reinforcement learning
- illustrate meta-reinforcement learning
- introduce soft actor critic approach
- describe machine learning logic
- illustrate machine learning logic
- define policy loss function
- define critic loss function
- define value loss function
- define context loss function
- describe training process
- initialize value network and target value network
- store trajectories in replay memory
- update critic network
- update policy network
- update value network
- illustrate out of distribution detection
- describe out of distribution detection
- illustrate out of distribution detection with radar data
- describe input noise
- illustrate out of distribution detection with input noise
- illustrate standard deviation of critic heads
- illustrate radar tracking parameters optimization
- describe radar device
- describe processing circuitry
- describe digital filter
- describe machine learning logic
- describe policy network
- describe reward value generating network
- describe out of distribution detection
- describe example 1
- describe example 2
- describe example 3
- describe example 4
- describe example 5
- describe example 6
- describe example 7
- describe example 8
- describe method of operating radar device
- describe method of training machine learning logic
- describe further training
- describe method of training machine learning logic

