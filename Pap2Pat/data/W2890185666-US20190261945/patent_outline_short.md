# DESCRIPTION

## BACKGROUND

- motivate medical imaging for atrial fibrillation treatment

## SUMMARY

- introduce 3D segmentation from 2D ICE images

## DETAILED DESCRIPTION OF EMBODIMENTS

- integrate knowledge from 3D geometry and 3D image appearance
- motivate contouring performance with machine learning
- describe ICE imaging limitations and challenges
- introduce deep neural network for 3D segmentation and volume completion
- outline method for three-dimensional segmentation from two-dimensional intracardiac echocardiography imaging
- describe ICE volume formation from ultrasound data
- generate 3D segmentation from ICE volume using machine-learned multi-task generator
- detail machine-learned network architecture, including U-Net and GAN
- train multi-task GAN with unpaired data from different modalities and patients
- describe adversarial training and loss functions for generator and discriminators
- outline collaborative image inpainting model for cross-modality learning
- summarize machine training process with various optimizers and loss functions
- describe 3D segmentation and volume completion using multi-task GAN
- train network with adversarial and reconstruction losses
- apply network to ICE volume to generate 3D segmentation and complete volume
- project 3D segmentation to 2D plane for 2D ICE image
- refine 2D segmentation using 2D-RefineNet
- display 2D segmentation with ICE image
- combine 2D and 3D segmentations for ablation guidance
- describe medical imaging system for 3D segmentation from 2D ICE images
- detail components of medical imaging system
- describe training and application of machine-learned networks
- discuss variations and improvements of the method

