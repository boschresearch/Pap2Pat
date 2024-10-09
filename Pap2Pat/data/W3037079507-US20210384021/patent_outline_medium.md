# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- describe limitations of chemical imaging

## BRIEF SUMMARY

- introduce correlative multimodal chemical imaging
- describe system with instrument and processor
- train machine learning model
- co-register spectral data cubes
- transform spectral data into abundance maps
- spatially correlate abundance maps
- generate high-resolution spectral data
- describe variations of system and method

## DETAILED DESCRIPTION

- introduce machine learning approach for high-spatial resolution molecular spectra
- describe combining images from two mass spectrometry imaging (MSI) techniques
- introduce first MSI technique with low spatial resolution but intact molecular spectra
- introduce second MSI technique with high spatial resolution but fragmented molecular signatures
- describe incorporating known relations between the two MSI techniques
- illustrate components of a machine learning system
- describe processor and memory device
- describe instrument with spectrometer capable of acquiring spectral image data
- describe receiving first-type spectral-data cube with two spatial dimensions and one spectral dimension
- describe receiving second-type spectral-data cube with two spatial dimensions and one spectral dimension
- describe training machine learning model
- co-register first-type spectral-data cube and second-type spectral data cube
- spatially establish one-to-one pairing of spectra
- transform first-type spectral-data cube into abundance maps of first components
- transform second-type spectral-data cube into abundance maps of second components
- spatially correlate first components' abundance maps with second components' abundance maps
- store resulting set of correlations as learned parameters of machine learning model
- describe non-negative matrix factorization (NMF) for data dimensionality reduction
- describe canonical correlation analysis (CCA) for identifying relations between datasets
- receive new second-type spectral-data cube with second-spatial resolution
- generate first-type spectral-data cube with second-spatial resolution
- transform new second-type spectral-data cube into second-spatial resolution abundance maps of second components
- determine second-spatial resolution abundance maps of first components from stored correlations
- recover first-type spectral-data cube with second-spatial resolution from abundance maps of first components
- describe using trained machine learning model for predicting high-spatial resolution molecular spectra
- describe storing data used by processor in storage devices
- describe user interface and display device for presenting images and analytics
- introduce machine learning model for correlative chemical imaging
- describe training of machine learning model
- summarize data acquisition and marking in SIMS imaging
- describe fiduciary marker etching
- summarize matrix application and MALDI imaging
- describe co-registration of MALDI and SIMS datasets
- summarize data processing and stitching
- describe application of non-negative matrix factorization (NMF)
- summarize generation of abundance maps
- describe correlation of abundance maps
- summarize processing of co-registered SIMS and MALDI datasets
- describe application of 2D Fourier filter and Gaussian smoothing
- summarize extraction of knowledge from dataset
- describe comparison of generated image with input new image
- summarize metrics for characterizing output of spectral datasets
- describe reconstruction of spatial maps of molecular species distribution
- summarize training of machine learning model and generation of first-type spectral data cube
- describe filtering and smoothing of second-type spectral dataset
- summarize dimensionality reduction of second-type spectral dataset
- describe correlation of abundance maps
- summarize generation of new first-type spectral data at higher spatial resolution
- describe components of system for training machine learning model
- summarize functionality of hardware processors and memory device
- describe input and output interfaces of system
- summarize computer program product and computer readable storage medium

