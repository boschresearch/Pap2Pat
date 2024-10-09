# DESCRIPTION

## TECHNICAL FIELD

- define biometeorological sensing devices

## BACKGDROUND

- motivate extreme heat and heat waves
- summarize global temperature increase
- describe limitations of air temperature
- introduce Mean Radiant Temperature (MRT)
- discuss importance of MRT in urban climate research
- highlight need for accurate MRT measurements

## SUMMARY

- introduce novel IoT weather station (MaRTiny)
- describe MaRTiny's capabilities
- motivate need for hyperlocal meteorological conditions
- introduce biometeorological sensing devices
- describe device components
- explain MRT estimation
- describe person detection and shade identification
- introduce deep learning model for shade detection
- describe vision system capabilities
- summarize device functionality

## DETAILED DESCRIPTION

- introduce patent application scope
- define globe temperature measurement
- describe limitations of MRT measurement methods
- motivate need for low-cost MRT sensing platform

### Mean Radiant Temperature (MRT) Sensing

- introduce MRT concept
- describe 6-directional method for MRT measurement
- provide Stefan-Boltzmann Law equation
- discuss limitations of 6-directional method
- introduce black globe thermometer
- describe Thorsson's low-cost globe thermometer
- discuss albedo variations
- introduce convection coefficients for globe thermometers
- provide empirical model for acrylic gray globe temperature
- discuss limitations of existing MRT measurement methods
- introduce microclimate and radiation models
- discuss limitations of conventional models
- introduce pedestrian counting and crowd estimation techniques
- describe sensor-based techniques
- describe network-based techniques
- introduce machine learning techniques for crowd estimation
- describe low-level image feature extraction methods
- describe regression models and detectors
- introduce deep convolutional neural networks for crowd estimation
- describe perspective maps
- discuss analysis of crowd behavior in urban areas
- discuss relation with thermal comfort
- introduce MaRTiny system
- describe biometeorological sensing device
- introduce weather station
- describe vision system
- introduce machine learning module
- describe IoT weather station
- describe low-cost and compact vision system
- describe pedestrian detection and shade detection
- introduce machine learning model for MRT estimation
- describe error correction and prediction
- introduce FIG. 1
- describe BSD components
- describe camera and people detection system
- introduce data transmission to external server
- describe power source and cost-effectiveness
- introduce FIG. 2
- describe sensor configuration
- describe data collection and transmission
- introduce machine learning model for MRT estimation
- describe vision system capabilities
- introduce NVIDIA Jetson Nano
- describe MIPI camera and gstreamer pipeline
- introduce AWS database and MQTT protocol
- describe on-board machine vision capabilities

## EXAMPLES

### System Overview

- introduce MaRTiny system
- describe system functionality
- detail sensor components
- explain globe thermometer functionality
- describe anemometer functionality
- detail camera and vision system
- describe Jetson Nano and its functionality
- explain Arduino Uno and NodeMCU microcontrollers
- detail communication protocol between components
- describe data transmission to cloud database

### Machine Learning Algorithm Development

- motivate machine learning approach
- describe data collection for labeled dataset
- detail machine learning models (SVM and ANN)
- explain model evaluation and selection

### System Evaluation

- describe evaluation dataset
- detail paired MaRTy and MaRTiny setup
- explain MRT calculation and comparison
- describe error in MaRTiny MRT estimation
- motivate supervised learning approach
- detail training and testing datasets
- explain model evaluation metrics (RMSE)
- compare SVM and ANN performance
- describe object detection using YOLOv3
- detail shade detection using BDRAR
- explain evaluation metrics for object detection (mAP)
- describe evaluation metrics for shade detection (IOU)
- detail pedestrian in shade detection algorithm
- explain evaluation results for pedestrian in shade detection

### Discussion

- summarize MaRTiny system
- motivate empirical study
- discuss calibration requirements
- compare MRT estimation errors
- discuss limitations of globe thermometers
- motivate low-cost sensing
- describe edge device capabilities
- explain system deployment plans
- discuss privacy preservation
- describe potential system modifications
- conclude system implementation

