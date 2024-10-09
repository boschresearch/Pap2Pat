# DESCRIPTION

## TECHNICAL FIELD

- introduce stereotactic body radiation therapy

## BACKGROUND

- motivate SBRT for lung cancer
- limitations of current CBCT systems

## SUMMARY

- introduce motion compensated 4D-CBCT image reconstruction
- define reconstruction method
- describe step 1 of reconstruction method
- describe step 2 of reconstruction method
- describe step 3 of reconstruction method
- introduce mathematical model of motion compensated SART
- describe DVF optimization by projection registration
- define energy function for DVF optimization
- summarize benefits of present disclosure

## DETAILED DESCRIPTION

- introduce 4D-CBCT image reconstruction method
- describe step 1: collection of 4D-CBCT projections
- describe step 2: initial 4D-CBCT image reconstruction and initial 4D-DVF generation
- describe step 3: iterative 4D-DVF optimization
- describe step 4: continuously iterative updating reconstruction at reference phase
- describe step 5: generation of a sequence of final high quality 4D-CBCT images
- illustrate block diagram of technical route
- provide example 1: verification of algorithm on 4D NCAT phantom
- provide clinical patient data test results

### EXAMPLE 1

- describe 4D NCAT phantom setup
- show reconstructed image of phase 40% with and without sliding motion constraint
- describe Region Of Interest (ROI) and sliding motions occurred at the edges of the heart and the veins
- show difference between reconstructions of ribs with and without bilateral filtering
- extract 4D motion trajectory in z-axis direction from the edge of the heart
- calculate Root Mean Square Error (RMSE) and Maximum motion Error (MaxE)
- compare results with and without bilateral filtering
- describe preliminary clinical patient data test
- show results of clinical patient data test

