# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- introduce chemical imaging
- describe limitations of existing techniques

## BRIEF SUMMARY

- introduce correlative multimodal chemical imaging
- describe system with instrument and processor
- acquire first-type spectral image data
- acquire second-type spectral image data
- train machine learning model
- co-register spectral data cubes
- down-sample second-type spectral data cube
- transform first-type spectral data cube
- transform second-type spectral data cube
- correlate abundance maps
- store learned parameters
- receive new second-type spectral data cube
- generate first-type spectral data cube
- describe alternative system
- describe alternative training method
- describe computer-implemented method
- describe computer readable storage medium

## DETAILED DESCRIPTION

- introduce machine learning approach
- combine images from two MSI techniques
- predict molecular MSI spectra with high spatial resolution
- describe MSI technique with low spatial resolution
- describe MSI technique with nanometer spatial resolution
- incorporate known relations between two imaging techniques
- illustrate components of machine learning system
- describe processor and memory device
- describe instrument with spectrometer
- receive first-type spectral-data cube
- describe first-type spectral-data cube
- receive second-type spectral-data cube
- describe second-type spectral-data cube
- train machine learning model
- co-register first-type and second-type spectral-data cubes
- spatially establish one-to-one pairing of spectra
- down-sample second-type spectral-data cube
- transform first-type spectral-data cube into abundance maps
- transform second-type spectral-data cube into abundance maps
- spatially correlate abundance maps
- store resulting set of correlations
- describe non-negative matrix factorization (NMF)
- perform NMF on first-type spectral-data cube
- perform NMF on second-type spectral-data cube
- decompose spectra into linear combinations
- determine abundance maps
- illustrate NMF method
- receive data
- set initial number of endmembers
- initialize matrix of endmembers
- compute matrix of weights
- compute approximation error
- determine if computation is less than threshold
- alter values of endmembers
- repeat until maximum number of iterations
- change number of endmembers
- reset number of iterations
- describe abundance maps
- perform canonical correlation analysis (CCA)
- find correlation between abundance maps
- store correlation weights matrices
- describe spatial correlation between abundance maps
- receive new second-type spectral-data cube
- generate first-type spectral-data cube
- transform new second-type spectral-data cube into abundance maps
- determine abundance maps of first components
- recover first-type spectral-data cube
- describe inverse CCA transformation
- describe inverse NMF transformation
- store generated data
- provide presentations of input and output data
- describe user interface and display device
- train machine learning model on co-registered datasets
- use trained model to predict new image
- describe different processors for training and reconstructing
- introduce machine learning model for correlative chemical imaging
- describe training of machine learning model
- transform spectral-data cubes into abundance maps
- correlate abundance maps of first and second components
- store correlations as learned parameters of machine learning model
- receive new second-type spectral-data cube
- generate first-type spectral data cube having second-spatial resolution
- up-sample or down-sample data cube to match spatial resolution
- motivate use of co-registered multimodal imaging
- describe example experiment using MALDI and SIMS imaging
- detail data acquisition and marking of sample
- describe SIMS imaging process
- detail fiduciary marker etching process
- describe matrix application and MALDI imaging process
- co-register MALDI and SIMS datasets
- process co-registered datasets
- apply 2D Fourier filter to reduce distortion
- apply 2D Gaussian smoothing to eliminate noise
- extract knowledge from dataset using non-negative matrix factorization
- compare generated image with input new image
- describe metrics for characterizing output of spectral datasets
- illustrate training of machine learning model and generation of high-spatial resolution molecular spectra
- receive dataset of second-type spectral data
- filter dataset to reduce distortion
- smooth dataset to eliminate noise
- receive dataset of first-type spectral data
- smooth dataset to eliminate noise
- perform dimensionality reduction on datasets
- correlate abundance maps of datasets
- store correlations as learned parameters of machine learning model
- receive new second-type spectral dataset
- transform dataset using dimensionality reduction algorithm
- generate abundance maps associated with new dataset
- infer abundance maps associated with first-type spectral data
- generate first-type spectral data at higher spatial resolution
- describe system for training machine learning model
- detail components of system
- describe memory device and storage device
- describe network interface and input/output interface
- describe instrument interface
- describe prediction model generation
- describe image reconstruction
- describe program storage device
- describe computer readable storage medium
- describe computer system and computer network
- describe module and device
- define terminology
- describe singular and plural forms
- describe inclusive operator
- describe phrases "in an embodiment" and "in one embodiment"
- describe corresponding structures and equivalents

