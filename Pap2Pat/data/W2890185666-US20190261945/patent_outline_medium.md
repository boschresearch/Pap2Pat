# DESCRIPTION

## BACKGROUND

- motivate medical imaging for atrial fibrillation treatment

## SUMMARY

- introduce 3D segmentation from 2D ICE images
- describe machine-learnt multi-task generator
- outline applications of 3D segmentation

## DETAILED DESCRIPTION OF EMBODIMENTS

- integrate knowledge from 3D geometry and 3D image appearance
- use machine learning for multi-task network
- provide cross-modality volume completion and 3D+2D segmentation
- use ICE information for initial 3D contour
- use full volume from other modality for accurate 3D contour
- perform contouring despite sparseness and noise in ICE images
- leverage database of diagnostic images for anatomy segmentation
- use deep neural network with 3D geometrical and image appearance information
- form 3D sparse volume from 2D ICE images
- perform cross-modality volume completion and 3D segmentation
- generate refined 2D segmentation from original ICE image and preliminary 2D segmentation
- describe method for three-dimensional segmentation from two-dimensional ICE imaging
- form ICE volume from ultrasound data for scan planes
- map 2D ICE images to 3D space using sensed positions
- generate 3D segmentation from input of ICE volume to machine-learned multi-task generator
- describe machine-learned network architecture
- use U-Net or fully convolutional network for image-to-image translation
- train GAN with generator and discriminators
- describe training of machine-learned network
- assign CT volumes as ground truth volumes for ultrasound imaging
- pair CT volumes with ICE imaging samples
- create samples for training with Procrustes analysis and mesh pairing
- train generator and discriminators adversarially
- use collaborative image inpainting for cross-modality volume completion
- train network to segment left atrium of 3D ICE volume
- introduce 3D segmentation and volume completion using machine-learned multi-task generator
- describe training of 3D-SCNet with adversarial and reconstruction losses
- detail application of 3D-SCNet to estimate 3D segmentation and complete volume
- describe display of 3D segmentation
- introduce 2D segmentation refinement using machine-learned 2D-RefineNet
- describe training of 2D-RefineNet with adversarial and reconstruction losses
- detail application of 2D-RefineNet to refine 2D segmentation
- describe display of 2D segmentation
- describe ablation procedure guided by 3D and/or 2D segmentation
- detail data collection and annotation for training
- describe 3D network architecture and training
- describe 2D network architecture and training
- show example outputs of 3D network
- show example outputs of 2D network
- compare performance of different models
- describe cyclic image-to-image generative model
- describe medical imaging system for 3D segmentation from 2D ICE imaging
- detail components of medical imaging system
- describe image processor and its functions
- describe memory and storage of data and instructions
- describe display of images to guide ablation
- discuss variations and improvements of the invention
- conclude with scope and spirit of the invention

