# DESCRIPTION

## FIELD

- define MS interferometry and OCT embodiments

## BACKGROUND

- explain SD-interferometry and SD-OCT

## SUMMARY

- introduce OCT techniques
- describe SD methods
- explain spectrometer and tunable laser formats
- illustrate prior art SD-OCT system
- describe decoder and processor operations
- explain limitations of prior art FT-OCT
- introduce Master Slave interferometry and OCT method
- describe MS-OCT system architecture
- explain MS-calculator operation
- describe en-face OCT image production
- illustrate typical en-face and A-scans
- explain electrical signal representation
- describe MS procedure stages
- explain mask calculation and storage
- distinguish OCT applications
- describe axial movement correction methods
- explain post-acquisition methods
- describe post-acquisition methods with sensor information
- explain real-time tracking methods
- illustrate RTT system architecture
- describe limitations of RTT methods
- conclude prior art OCT techniques
- introduce prior art in OCT imaging
- limitations of prior art in tracking and correction
- need for faster tracking and correction methods
- problem of pulsatile blood movement in retina
- need to distinguish between axial movement and pulsatile blood movement
- application to imaging curved targets
- problem of en-face image fragmentation
- need for real-time en-face flattening
- need for efficient segmentation/edge detection methods
- need for versatile signal processing
- first aspect: Master Slave—OCT system with accessible Mask Selector
- second aspect: method for dynamic selection of masks
- third aspect: method for selection and swap of masks
- fourth aspect: devices and methods for flattening tissue
- additional aspects: devices and methods for edge detection, axial tracking, and en-face imaging

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce apparatus using single or two interferometers
- describe first embodiment of apparatus using single interferometer
- detail components of first embodiment, including Master Slave processor and sensor
- explain operation of corrector and Mask selector
- describe control of operational modes using mode switch
- detail interleaving of processes of acquisition, sensing, storage, and correction
- describe variations of sensor and MS-processor embodiments
- detail first embodiment of MS-processor for flattening of C-scans
- describe second embodiment of MS-processor for correction of axial movement in B-scans
- detail third embodiment of MS-processor employing stored masks
- describe fourth embodiment of MS-processor employing stored masks and dynamic swap of Q masks
- explain adjustment of range of masks depending on task of dynamic correction
- compare MS protocol with FFT in terms of operations required
- describe dynamic allocation of masks in MS-processor
- detail use of MS-processor in different scenarios, including selection of masks for B-scans and C-scans
- describe flattening process using embodiment in FIG. 6
- detail sensor embodiments using MS algorithm and FFT
- introduce modulus difference threshold
- describe single surface object contour
- explain thresholder operation
- detail mask index array generation
- describe corrector operation
- introduce alternative embodiment using stored channeled spectra
- explain Dynamic MS comparator operation
- describe FFT-based embodiment
- detail array population for different embodiments
- explain corrector operation for different embodiments
- describe flattening of T-scans and C-scans
- detail storage and transfer of channeled spectra
- explain corrector output and mask selection
- describe sequential regimes of operation
- detail practical implementation considerations
- explain acquisition and correction for stationary and moving objects
- describe parallel processing for faster operation
- detail results obtained with a proof of concept system
- show images from finger skin, coin, and retina
- describe segmentation operation
- discuss parallel processing
- introduce manual segmentation
- present preliminary results
- describe axial tracking using second interferometer
- detail sensor and MS-processor embodiments
- explain sensing axial position of object
- describe MS protocol for sensing
- discuss FFT-based sensing
- detail corrector operation
- explain axial distance correction
- discuss advantages of MS protocol
- introduce dynamic search in depth
- discuss tracking continuous drift
- summarize axial tracking embodiments
- describe ultra-fast sensing and parallel processing
- introduce dual sensor embodiment
- describe third embodiment of apparatus
- detail first stage of processing
- detail second stage of processing
- describe calculation of variance
- illustrate utilization of embodiments for OCTA images
- describe method for producing 2D map of OCTA en-face images
- describe method for producing Q C-scans
- describe calculation of differences
- describe co-registration of images
- describe method for producing C-scan OCTA image
- describe alternative method engaging MS-processors
- describe method for producing volume of OCTA data
- describe adaptability to variation of axial resolution
- describe proof of concept of axial tracking
- describe imaging system capable of compensating axial movements
- describe sensor system employed for axial sensing
- describe imaging system employed for imaging
- describe mechanical correction replaced with sliding mask indices
- describe en-face C-scan images acquired with and without axial motion compensation
- describe reduction of motion artefacts

