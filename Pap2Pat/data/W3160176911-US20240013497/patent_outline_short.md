# DESCRIPTION

## FIELD

- relate to 3D reconstruction

## BACKGROUND

- limitations of standard 3D modeling methods

## SUMMARY

- outline computer-implemented method for 3D object shape determination

## DETAILED DESCRIPTION

### Overview

- introduce LASR pipeline for 3D shape reconstruction
- describe analysis-by-synthesis strategy
- outline forward-rendering of silhouette, optical flow, and color images
- explain comparison against video observations to adjust model parameters
- describe recovery of 3D object shape and camera trajectories
- mention building a library of shape models from multiple images
- outline model-free approach for 3D shape learning from images

### Example Devices and Systems

- introduce user computing device and its components
- describe server computing system and its components
- outline training computing system and its components
- explain communication between devices over a network
- describe 3D reconstruction models stored at devices
- mention training of models using various techniques

### Example Model Arrangements

- introduce 3D reconstruction pipeline with inverse graphics optimization

### Example Approach

- solve nonrigid 3D shape and motion estimation problem

### Example Forward-Synthesis Model

- forward-render texture, optical flow, and silhouette images

### Example Deformation Modeling

- construct deformation modeling of object of interest

### Example Self-Supervised Learning from a Video

- exploit rich supervision signals from dense optical flow and raw pixels

### Example Implementation Details

- leverage camera and poses for implementation details

### Example 2D Keypoint Transfer on Animal Videos

- introduce animal video dataset
- describe data derivation and annotation
- define percentage of correct keypoint transfer (PCK-T)
- illustrate taxonomy of alternative methods for animal reconstruction
- show qualitative results of 3D shape reconstruction
- compare with UMR, A-CSM and SMALify on bear and dog data
- show quantitative results of keypoint transfer
- illustrate example keypoint transfers between frames
- compare with detection-based methods
- show improvement compared to initial optical flow

## Additional Disclosure

- clarify flexibility of computer-based systems

