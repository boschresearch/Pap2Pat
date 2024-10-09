# DESCRIPTION

## PRIORITY DATA

- claim priority to previous applications
- incorporate previous applications by reference

## FEDERALLY SPONSORED RESEARCH OR DEVELOPMENT

- disclose government funding

## TECHNICAL FIELD

- define technical field of digital imaging

## BACKGROUND

- describe limitations of multi-well plate readers
- motivate need for image information
- describe conventional imaging techniques

## SUMMARY

- introduce imaging system
- describe illumination system
- describe optical system
- describe imaging system
- describe plate receiver system
- describe controller and image reconstruction process

## DETAILED DESCRIPTION

- introduce purpose of description

### I. Introduction

- introduce imaging systems and methods
- motivate high resolution FP imaging
- describe limitations of traditional imaging systems
- introduce FP imaging technique
- describe advantages of FP imaging
- cite prior art
- introduce imaging systems for FP processing
- describe components of imaging systems
- describe sample loading system
- describe illumination system
- describe optical system
- describe imaging system
- describe image acquisition phase
- describe Fourier ptychographic reconstruction process

### II. Imaging System for Fourier Ptychographic (FP) Imaging and Fluorescent Imaging

- introduce imaging system 100
- describe illumination system 102
- describe sample loading system 104
- describe optical system 106
- describe image sensor system 108
- describe controller 110
- describe illumination patterns
- describe image data output
- describe processing of raw image data
- describe FP image processing operations
- describe generation of high resolution image
- describe fluorescence imaging
- describe processing of fluorescence image data
- describe parallel image processing
- describe processor and memory
- describe communication interfaces
- describe output of raw and processed image data
- describe external computing device or system
- describe external memory device or system
- describe network communication interface
- describe additional interfaces
- describe multiplexing of image data
- describe demultiplexing of image data
- introduce imaging system 200
- describe housing or enclosure 202
- describe frame structure 204
- describe alignment through-holes 205
- describe frame alignment rods 206
- describe physical support of components
- describe substrates with through-holes
- describe illumination system components
- describe optical system components
- describe image sensor system components
- describe sample loading system components
- describe sample platform 215
- describe aperture slot 214
- describe multi-well plate 208
- describe wells 209
- describe sample platform guides
- describe automatic loading and ejecting mechanism
- describe sample platform 305
- describe illumination system
- introduce light sources
- describe LED matrix
- explain RGB LED
- discuss LED footprint
- describe well arrangement
- derive equation for light sources
- calculate number of light sources
- introduce side-mounted light sources
- describe lens array
- explain multi-lens-array arrangement
- discuss lens characteristics
- describe optical arrangement
- introduce optical filter
- explain fluorescence imaging
- describe GFP imaging
- discuss optical filter placement
- explain bright field illumination
- describe removable optical filter
- introduce image sensor system
- describe image sensor array
- explain image sensor capabilities
- discuss image sensor orientation
- describe data transfer
- introduce liquid cooling system
- describe image sensor system components
- explain image sensor system operation
- summarize imaging system

### III. Variable-Illumination Fourier Ptychographic Imaging Methods

- describe FP image acquisition process
- introduce illumination system and image sensor system
- explain initialization of illumination system and image sensor system
- describe calibration operation
- introduce sth scan
- describe illumination pattern during sth scan
- show example arrangement of light sources and wells
- describe reception and focusing of light
- describe image data acquisition
- describe storage of image data
- explain multiplexing approach
- describe separation of intensity data
- determine whether all n scans have been completed
- incrementally update s for next scan
- perform parallel reconstruction process
- describe iterative combination of intensity images
- apply filter in Fourier domain
- apply inverse Fourier transform
- replace intensity with measurement
- apply Fourier transform
- update region in Fourier space
- describe phase retrieval technique
- describe recovery process
- introduce FP reconstruction process 700
- initialize high-resolution image solution
- apply Fourier transform
- describe low-pass filtering
- generate low-resolution image
- propagate low-resolution image to in-focus plane
- replace amplitude component with measurement
- back-propagate to sample plane
- update high-resolution solution
- determine whether operations have been completed for all images
- repeat operations for next image
- determine whether high-resolution solution has converged
- repeat operations until convergence
- transform converged solution to spatial domain
- introduce FP reconstruction process 800
- model connection between sample profile and captured intensity data
- invert connection to achieve aberration-free reconstructed image
- describe digital wavefront correction
- introduce variable-illumination Fourier ptychographic imaging methods
- initialize high-resolution image solution
- apply Fourier transform to obtain initialized Fourier transformed image
- determine initial high-resolution solution
- multiply by phase factor in Fourier domain
- perform low-pass filtering of high-resolution image
- generate low-resolution image for particular plane wave incidence angle
- filter low-pass region from spectrum of high-resolution image
- replace computed amplitude component with square root of low-resolution intensity measurement
- multiply by inverse phase factor in Fourier domain
- apply Fourier transform to updated target image
- update high-resolution solution in Fourier space
- determine whether operations have been completed for all uniquely illuminated low-resolution intensity images
- repeat operations for next image
- determine whether high-resolution solution has converged
- compare previous high-resolution solution to present high-resolution solution
- repeat operations until solution converges
- transform converged solution to spatial domain to recover high-resolution image
- describe calibration process for determining angles of incidence
- illuminate central light element
- capture vignette monochromic image
- determine center of image
- measure shift of center of image
- determine displacement of central light element using lookup table
- determine precise values of illumination angles
- describe fluorescence imaging process
- load multi-well plate into imaging system
- initialize illumination system and image sensor system
- illuminate multi-well plate with excitation light
- receive and focus light emitted by samples
- filter light to only allow light emitted by fluorophore
- acquire fluorescence image data
- store image data in memory
- generate combined fluorescence and high-resolution bright-field image

