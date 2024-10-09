# DESCRIPTION

## PRIORITY DATA

- claim priority

## FEDERALLY SPONSORED RESEARCH OR DEVELOPMENT

- acknowledge government support

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- describe limitations of conventional plate readers

## SUMMARY

- introduce imaging system
- describe imaging system components
- outline image acquisition and reconstruction process

## DETAILED DESCRIPTION

- provide context for disclosure

### I. Introduction

- introduce FP imaging
- motivate high-resolution imaging
- describe limitations of traditional imaging
- introduce FP technique
- summarize advantages of FP imaging
- reference prior art
- introduce imaging systems for parallel FP imaging

### II. Imaging System for Fourier Ptychographic (FP) Imaging and Fluorescent Imaging

- introduce imaging system 100
- describe illumination system 102
- describe sample loading system 104
- describe optical system 106
- describe image sensor system 108
- describe controller 110
- describe imaging process
- describe FP image processing
- describe fluorescence imaging
- describe parallel image processing
- describe controller 110 functionality
- describe internal memory device 120
- describe outputting image data
- describe communication interfaces
- introduce imaging system 200
- describe enclosure 202
- describe frame structure 204
- describe illumination system components
- describe optical system components
- describe sample loading system components
- describe illumination system
- detail light sources
- explain equation for number of light sources
- describe lens array
- illustrate optical arrangement
- detail optical filter
- describe lens characteristics
- explain use of multiple lens arrays
- describe fluorescence imaging application
- detail optical filter for fluorescence imaging
- explain bright field illumination
- describe image sensor system
- detail image sensor characteristics
- explain image data transfer

### III. Variable-Illumination Fourier Ptychographic Imaging Methods

- describe FP image acquisition process
- introduce illumination system and image sensor system
- explain initialization of illumination system and image sensor system
- describe sth scan operation
- illustrate first illumination pattern during first scan
- illustrate second illumination pattern during second scan
- illustrate seventh illumination pattern during seventh scan
- illustrate eighth illumination pattern during eighth scan
- illustrate 42nd illumination pattern during 42nd scan
- illustrate 49th illumination pattern during 49th scan
- describe reception and focusing of light during each scan
- describe image data acquisition during each scan
- describe storage of image data
- describe multiplexing approach to decrease total scan time
- determine whether all n scans have been completed
- perform parallel reconstruction process to reconstruct higher-resolution image
- describe FP reconstruction process using angular diversity
- illustrate FP reconstruction process 700
- describe low-pass filtering of high-resolution image
- describe digital wavefront correction in FP reconstruction process 800
- introduce variable-illumination Fourier ptychographic imaging methods
- initialize high-resolution image solution
- apply Fourier transform to obtain initialized Fourier transformed image
- perform low-pass filtering of high-resolution image
- replace computed amplitude component with square root of low-resolution intensity measurement
- multiply by inverse phase factor
- apply Fourier transform to updated target image
- update high-resolution solution
- determine whether operations have been completed for all uniquely illuminated low-resolution intensity images
- determine whether high-resolution solution has converged
- transform converged solution to spatial domain to recover high-resolution image
- describe calibration process for determining angles of incidence
- capture vignette monochromic image during illumination by central light element
- determine displacement of central light element based on x-shift and y-shift
- describe fluorescence imaging process for imaging multi-well plate
- initialize illumination system and image sensor system
- generate combined fluorescence and high-resolution bright-field image of sample

