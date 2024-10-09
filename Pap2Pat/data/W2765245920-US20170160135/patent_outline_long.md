# DESCRIPTION

## FIELD

- define spectral imaging

## BACKGROUND

- introduce snapshot spectral imagers
- describe CTIS designs
- describe CS-SI approaches
- limitations of known solutions
- need for miniaturized snapshot spectral imagers

## SUMMARY

- introduce SSI based on compressed sensing
- describe apparatus for SSI
- define RIP diffuser
- describe digital camera with RIP diffuser
- describe dispersed image and reconstruction
- summarize embodiments

## DETAILED DESCRIPTION

- introduce SSI using digital camera and RIP diffuser
- describe optical properties of RIP diffuser
- explain CS theory for compressible images
- define sensing matrix and its operation
- describe reconstruction process using Bregman iteration
- illustrate method for SSI in FIG. 1A
- detail step 104 of FIG. 1A using Bregman iteration
- describe linearized Bregman iteration in FIG. 1C
- describe split Bregman iteration in FIG. 1D
- define spectral cube 3D matrix
- model imaging at spectral band λi
- describe linear transformation of dispersed image intensity
- define sensing matrix H and its properties
- relate to compressed sensing problem
- explain RIP condition for stable solution

### Diffuser Design Formulation

- define matrix X of size ML×N
- describe vectorization of X
- model imaging at spectral band λi
- describe linear transformation of dispersed image intensity
- define impulse response hλ
- describe digital processing of regular and dispersed images
- calculate PSF of incoherent imaging system hλ
- define matrix Hλ for 1D linear transformation
- relate to compressed sensing problem

### Finally

- describe dispersed image intensity
- define matrix H and its properties
- relate to compressed sensing problem
- define vectors yj and xj
- describe matrix H as sensing matrix
- relate to compressed sensing problem
- define sparsifying matrix ψ
- describe RIP condition
- explain incoherence condition
- describe deterministic sensing matrix
- describe random sensing matrix
- relate to RIP diffuser design

### Exemplary RIP Diffuser Implementation

- define RIP diffuser requirements
- design 1D RIP diffuser with random phase mask
- derive transfer function of diffuser
- describe wavelength dependence of diffuser
- provide discrete version of transfer function
- discuss limitations of RIP diffuser performance
- explain use of RIP diffuser in spectral imaging

### Apparatus Embodiments

- introduce snapshot spectral imager embodiment 200
- describe digital camera and RIP diffuser components
- explain optical path of embodiment 200
- introduce embodiment 200' with double-aperture camera
- describe optical path of embodiment 200'
- introduce embodiment 300 with reflective-refractive beam splitter
- describe optical path of embodiment 300
- introduce embodiment 400 with turning mirror
- describe optical path of embodiment 400
- introduce embodiment 500 with diffractive disperser
- describe optical path of embodiment 500
- introduce embodiment 600 with single posterior block
- describe optical path of embodiment 600
- explain use of band-pass filter
- describe image processing and spectral cube reconstruction
- discuss implementation of optical schemes
- explain use of conventional digital cameras

### Computer Simulations

- introduce simulation of CS algorithm
- describe source object and simulation setup
- explain formation of mixed matrix M
- apply framelet-based Split Bregman iteration scheme
- describe reconstruction results
- calculate PSNR and confirm accuracy
- introduce simulation of random Toeplitz matrix with Bregman CS algorithm
- describe source object and simulation setup
- form dispersed image with sensing matrix
- apply linearized Bregman iterations
- apply split Bregman iterations
- introduce simulation of spectral cube reconstruction
- describe source object and simulation setup
- apply linearized Bregman iterations and confirm perfect reconstruction

