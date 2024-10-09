# DESCRIPTION

## BACKGROUND

- motivate crystal orientation mapping

## SUMMARY

- introduce system for orientation mapping
- outline method for orientation mapping
- highlight advantages

## DETAILED DESCRIPTION

- introduce existing crystal orientation mapping techniques
- limitations of EBSD and SACP systems
- describe EBSD system with external camera
- illustrate tilt dependence of BSE signal
- motivate proposed system
- advantages of proposed system over traditional systems
- describe new method and system for capturing ECPs
- capture full images at range of sample orientations
- raster-scanning image collection
- use computational methods to align images and reconstruct ECP
- index and map grain orientation
- apply machine learning algorithms for predictive sampling
- enable strain mapping and quality control
- analyze defects through ECCI
- detect higher-order Laue zone lines
- perform orientation mapping, phase identification, and grain size analysis
- describe proposed system without costly specialized hardware
- use stage with high precision
- apply technique to other orientation-dependent imaging techniques
- illustrate stage-rocked ECP generation system
- describe motorized sample stage
- establish variables for orientation mapping
- depict computing architecture
- describe measurement systems and computing device
- illustrate scanning electron microscope
- describe SEM components and operation
- convert image signal to digital signal
- describe reduction in acquisition time
- introduce computing system
- describe image capture unit
- describe machine-learning unit
- describe database
- describe alternative embodiments
- introduce flow diagram
- acquire images
- describe image capture process
- align and segment images
- analyze aligned and segmented images
- detect regions of interest
- construct ECPs
- assess quality of ECPs
- determine if quality threshold is satisfied
- repeat process if quality threshold not satisfied
- use machine-learning algorithm to predict new orientation values
- index ECPs
- construct orientation map
- introduce computing device
- describe processing unit
- describe data storage
- describe system bus
- describe computer-readable media
- describe user interface
- describe monitor
- describe network interface

### EXPERIMENTAL RESULTS & DATA

- show channeling contrast dataset
- plot dataset in 3D using equiangular projection
- plot dataset in 2D using equiangular projection
- depict orthographic projection of stage-rocked ECP
- reconstruct ECP from average contrast values
- depict orthographic projection of hybrid stage-rocked and beam-rocked ECP
- reconstruct ECP by binning ECCIs and correcting for beam divergence
- apply corrections to ECP for systematic contrast variations
- compare conventional EBSD techniques with OMEC ECP techniques
- depict aligned and perspective corrected BSE images
- depict Z-axis-referenced inverse pole figure map
- display relative orientations of member grains
- depict representative electron backscattering patterns
- depict representative indexed patterns
- depict representative OMEC electron channeling patterns
- use contrast invariant feature detectors for image registration
- simulate OMEC acquisition from calculated channeling patterns

