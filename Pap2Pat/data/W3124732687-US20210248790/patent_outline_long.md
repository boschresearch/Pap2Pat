# DESCRIPTION

## TECHNICAL FIELD

- introduce stereotactic body radiation therapy

## BACKGROUND

- describe SBRT for lung cancer
- explain FFF beam mode
- motivate precise positioning of FFF beams
- limitations of current CBCT systems

## SUMMARY

- introduce motion compensated 4D-CBCT image reconstruction
- describe technical solution
- define reconstruction method
- step 1: build motion compensated 3D-CBCT reconstruction model
- step 2: create iterative optimization procedure
- step 3: deform high quality phase 0% image
- describe mathematical model of motion compensated SART
- define energy function for DVF optimization
- describe inverse continuity of DVF
- define smoothing term
- describe bilateral filtering
- define φ(v)
- describe gradient of φ(v)
- calculate difference between central voxel and neighborhood
- obtain final high quality 4D-CBCT images
- describe mathematical description of deformation procedure
- define φ(v) without bilateral filtering and sliding motion
- describe benefits of present disclosure
- summarize advantages over prior art

## DETAILED DESCRIPTION

- introduce 4D-CBCT image reconstruction method
- describe step 1: collection of 4D-CBCT projections
- explain data pre-processing procedure
- describe Varian Respiration Positioning Management (RPM) system
- describe step 2: initial 4D-CBCT image reconstruction and initial 4D-DVF generation
- explain Total Variation (TV) minimization reconstruction method
- describe Demons registration algorithm
- describe step 3: iterative 4D-DVF optimization
- explain formula (2) for DVF optimization object function
- describe bilateral filtering kernels
- explain variance settings for bilateral filtering kernels
- describe algorithm verification on NCAT phantom
- describe iterative optimization estimation of DVF
- describe step 4: continuously iterative updating reconstruction at reference phase %
- explain motion compensated SART algorithm
- describe step 5: generation of a sequence of final high quality 4D-CBCT images
- explain equation (5) for final 4D-CBCT image reconstruction
- describe block diagram of technical route
- conclude detailed description

### EXAMPLE 1

- introduce example 1: verification on 4D NCAT phantom
- describe phantom settings
- explain simulation of projections
- describe image size and voxel size settings
- show reconstructed image of phase 40% with and without sliding motion constraint
- describe Region Of Interest (ROI) analysis
- explain difference between reconstructions of ribs with and without bilateral filtering
- describe 4D motion trajectory extraction
- explain Root Mean Square Error (RMSE) and Maximum motion Error (MaxE) calculations
- show results of RMSE and MaxE
- introduce preliminary clinical patient data test
- describe CBCT projections collection
- explain 4D phase segmentation
- describe high quality 4D-CBCT image reconstruction using TV minimization
- explain undersampling of projections
- describe parallel control 4D-CBCT reconstructions
- show results of reconstruction methods comparison
- describe boundary of pulmonary rib cage analysis
- conclude example 1

