# DESCRIPTION

## FIELD

- define spectral imaging

## BACKGROUND

- motivate snapshot spectral imaging
- limitations of known designs

## SUMMARY

- introduce snapshot spectral imager
- application of compressed sensing
- embodiment of RIP diffuser

## DETAILED DESCRIPTION

- introduce SSI using digital camera and RIP diffuser
- describe underdetermined problem and CS theory
- explain sensing matrix and RIP condition
- outline reconstruction process using Bregman iteration
- describe FIG. 1A and steps for SSI
- detail FIG. 1B and 1C for linearized and split Bregman iteration
- describe FIG. 1D for split Bregman iteration

### Diffuser Design Formulation

- define spectral cube 3D matrix
- describe imaging at spectral band λi
- model mathematically with convolution and PSF
- define sensing matrix and RIP condition

### Finally

- summarize dispersed image intensity
- describe Toeplitz matrix for spatially invariant system
- define PSF of incoherent imaging system
- outline matrix multiplication for convolution
- describe sensing matrix and RIP condition
- discuss sparsifying matrices and K-SVD

### Exemplary RIP Diffuser Implementation

- define RIP diffuser requirements
- design 1D RIP diffuser with random phase mask
- derive transfer function of RIP diffuser

### Apparatus Embodiments

- introduce snapshot spectral imager with RIP diffuser
- describe digital camera with RIP diffuser
- describe double-aperture camera with RIP diffuser
- describe optical schemes with two-channels of imaging
- describe reflective-refractive beam splitter embodiment
- describe diffractive disperser embodiment
- describe single posterior block embodiment
- describe use cases for imagers

### Computer Simulations

- simulate mathematical aspects of CS algorithm
- simulate combination of random Toeplitz matrix with Bregman CS algorithm
- simulate spectral cube reconstruction for test source objects
- describe simulation setup for source object
- describe simulation results for Bregman iteration
- describe simulation results for split Bregman iteration
- describe simulation results for spectral cube reconstruction

