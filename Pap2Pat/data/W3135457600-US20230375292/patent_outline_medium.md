# DESCRIPTION

## FIELD OF THE INVENTION

- define field

## BACKGROUND

- motivate boiling control

## SUMMARY OF THE INVENTION

- introduce smart boiling analysis
- describe method embodiment
- describe system embodiment

## DETAILED DESCRIPTION

- introduce smart boiling method
- describe data-driven learning framework
- explain correlation of bubble images with boiling curves
- detail active control of boiling conditions
- describe process for controlling flow boiling systems
- discuss limitations of traditional boiling heat transfer studies
- introduce importance of image-based boiling physics
- describe role of deep learning in boiling analysis
- explain significance of boiling curves in thermal management
- discuss limitations of current measurement setups
- introduce non-destructive and automated optical method
- describe potential of image-based deep learning models
- highlight importance of linking bubble dynamics and boiling processes

### Hierarchical Feature Extraction

- employ convolutional neural networks to extract hierarchical image features

### Physics-Based Feature Extraction

- employ advanced object detection algorithms to extract bubble statistics
- describe relationship between bubble statistics and heat flux
- detail instance segmentation models for automatic bubble detection
- illustrate bubble parameters obtained from Mask R-CNN data analysis

### Hybrid Physics-Reinforced Framework

- predict boiling heat flux by extending and coupling deep learning models

### Training Results

- illustrate loss graphs for HyPR model
- compare training results for isolated image feature-based and bubble-statistic-based prediction models

### Real-Time Prediction of Boiling Heat Flux

- describe real-time boiling heat flux prediction using trained deep learning models
- compare prediction values of HyPR, CNN, and MLP models
- quantify prediction accuracy using mean absolute percentage error (MAPE)

## DISCUSSION

- discuss flexibility of deep learning techniques
- discuss resource effectiveness of deep learning framework

### Experimental Setup

- describe experimental setup for pool boiling experiments

### Real-Time Data Acquisition

- describe high-speed camera setup for pool boiling image capture

### Datasets

- describe dataset splitting for training and testing

### Training Mask R-CNN

- describe Mask R-CNN architecture
- describe data augmentation techniques

### Training HyPR, CNN, and MLP Models

- describe fine-tuning of HyPR, CNN, and MLP models

### Fine-Tuning Deep CNN

- describe VGG16 architecture
- describe custom FC layers for regression
- describe fine-tuning process for VGG16

### Uncertainty Analysis for Pool Boiling Experiment

- describe heat flux calculation
- describe uncertainty analysis using law of propagation of uncertainty
- describe calculation of uncertainty for maximum heat flux

## Systems for Smart Boiling Analysis

### Smart Boiling Analysis System

- describe smart boiling analysis system architecture
- describe server systems and cloud services
- describe personal devices and network connections

### Smart Boiling Analysis Element

- describe smart boiling analysis element architecture
- describe peripherals and network interface
- describe memory and smart boiling analysis application

### Smart Boiling Analysis Application

- describe image feature engine and bubble characteristics engine
- describe analysis engine and output engine

