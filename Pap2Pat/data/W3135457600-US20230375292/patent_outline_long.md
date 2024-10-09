# DESCRIPTION

## FIELD OF THE INVENTION

- define field

## BACKGROUND

- motivate boiling control

## SUMMARY OF THE INVENTION

- introduce smart boiling analysis
- identify bubble characteristics
- identify image features
- predict boiling heat characteristics
- control flow boiling system
- describe embodiments

## DETAILED DESCRIPTION

- introduce smart boiling method
- describe data-driven learning framework
- explain correlation of high-quality imaging with boiling curves
- introduce convolutional neural networks and object detection algorithms
- describe automatic extraction of hierarchical and physics-based features
- explain learning of physical boiling laws
- describe in situ boiling curve prediction
- introduce method for controlling boiling systems
- describe receiving and identifying bubble images
- explain identifying bubble characteristics and image features
- describe predicting boiling heat characteristics
- explain controlling boiling system based on predictions
- describe advantages of smart flow boiling
- explain energy efficiency and reduced greenhouse gas emissions
- describe computer vision assisted data analysis
- explain correlating bubble images with boiling conditions
- describe automatic extraction of hierarchical and physics-based features
- explain learning of physical boiling laws
- describe in situ smart control of boiling conditions
- introduce example of process for controlling flow boiling systems
- describe receiving and identifying bubble images
- explain identifying bubble characteristics and image features
- describe predicting boiling heat characteristics
- explain controlling boiling system based on predictions
- describe significance of boiling heat transfer
- explain limitations of current measurement setups
- introduce smart boiling systems and methods

### Hierarchical Feature Extraction

- employ convolutional neural networks to extract hierarchical image features
- describe recognition capability of CNNs
- explain use of deep CNNs and transfer learning technique

### Physics-Based Feature Extraction

- employ advanced object detection algorithms to extract physics-based features
- describe relationship between bubble statistics and heat flux
- explain use of instance segmentation models
- describe automatic detection and recording of bubble statistics
- show bubble parameters obtained from Mask R-CNN data analysis
- describe linear correlation between bubble size and boiling heat flux
- explain bubble size deviation and its correlation with boiling heat flux
- describe exponential decrease in bubble count with increasing heat flux
- explain use of MLP neural networks to process bubble statistics

### Hybrid Physics-Reinforced Framework

- describe coupling of deep learning models to predict boiling heat flux
- explain use of CNNs and MLPs to recognize visual and physics-based features
- describe hybrid physics-reinforced framework for predicting boiling heat flux

### Training Results

- show loss graphs for HyPR model
- compare training results for isolated image feature-based and bubble-statistic-based prediction models
- describe testing loss for HyPR, CNN, and MLP models
- explain use of validation dataset to evaluate HyPR model's real-time capability
- describe real-time prediction of boiling heat flux using trained deep learning models

### Real-Time Prediction of Boiling Heat Flux

- describe real-time boiling heat flux prediction using validation dataset
- compare prediction values of HyPR, CNN, and MLP models
- explain errors from thermocouple measurements and model predictions
- describe prediction fluctuations of HyPR and CNN models
- explain calculation of mean absolute percentage error (MAPE)
- show MAPE values for each model
- describe advantages of using hybrid physics-reinforced framework

## DISCUSSION

- discuss flexibility of deep learning techniques
- discuss surface structure correlation with boiling curves
- discuss resource effectiveness of deep learning framework
- discuss importance of image automation in heat transfer community
- discuss potential applications of deep learning framework

### Experimental Setup

- describe pool boiling rig components
- describe high-speed camera setup
- describe data acquisition device and boiling chamber

### Real-Time Data Acquisition

- describe high-speed camera settings
- describe image resolution and lighting setup
- describe randomized imaging technique

### Datasets

- describe dataset splitting and labeling

### Training Mask R-CNN

- describe Mask R-CNN architecture
- describe feature pyramid networks and regional proposal networks
- describe bilinear interpolation for pixel-accurate masks
- describe data augmentation techniques

### Training HyPR, CNN, and MLP Models

- describe fine-tuning and training settings for HyPR, CNN, and MLP models

### Fine-Tuning Deep CNN

- describe pre-trained VGG16 architecture
- describe custom fully connected layers for regression
- describe freezing early layers during training
- describe unfreezing layers after stabilization
- describe training settings and learning rates
- describe custom fully connected layers for output

### Uncertainty Analysis for Pool Boiling Experiment

- describe heat flux calculation
- describe uncertainty analysis using law of propagation
- describe thermocouple reading uncertainty
- describe thermal conductivity assumption
- describe positional error minimization
- describe uncertainty calculation for maximum heat flux
- describe calculated uncertainty value

## Systems for Smart Boiling Analysis

### Smart Boiling Analysis System

- describe smart boiling analysis system components
- describe server systems and cloud services
- describe personal devices and network connections
- describe mobile device and wireless connection
- describe imaging system and boiling rig
- describe flow control module
- describe smart boiling model and flow boiling system

### Smart Boiling Analysis Element

- describe processor and peripherals
- describe network interface and memory
- describe smart boiling analysis application
- describe model data and training data
- describe peripherals for capturing data
- describe network interface for transmitting data

### Smart Boiling Analysis Application

- describe image feature engine
- describe bubble characteristics engine
- describe analysis engine
- describe output engine
- describe various outputs and control signals

