# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate augmented imaging
- limitations of existing methods

## SUMMARY OF THE INVENTION

- introduce problem of functional imaging
- propose method and system for functional imaging
- describe method of generating augmented images
- estimate spectral composition of light illuminating tissue
- obtain multispectral images of tissue
- apply machine learning based regressor or classifier
- describe three variants of applying regressor or classifier
- define augmented imaging and tissue parameter
- provide examples of tissue parameters
- describe estimation of spectral composition of illuminating light
- describe identification of regions of specular reflection
- describe preferred embodiments of the method
- motivate multispectral imaging
- describe CNN-based regressor for tissue parameter estimation
- detail training of regressor using simulated neighborhoods
- outline application of regressor to multispectral image
- describe forward model for tissue parameter estimation
- detail ensemble of regressors for improved tissue parameter estimation
- describe probabilistic distribution of tissue parameters
- outline out-of-distribution detection for machine learning algorithms
- detail WAIC-based out-of-distribution detection algorithm
- introduce OoD detection algorithm
- describe ensemble of neural networks
- motivate variational autoencoder
- summarize system for generating augmented images
- describe apparatus for estimating spectral composition
- outline machine learning module
- detail regressor or classifier
- explain tissue model
- describe forward model
- outline training of regressor or classifier
- describe application of regressor or classifier
- detail out of distribution detection
- describe selection of regressor or classifier
- outline repeated OoD detection

## DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce multispectral imaging (MSI) and its potential
- describe challenges in deciphering MSI information
- introduce embodiments of the invention for video-rate estimation of physiological parameters
- describe the offline part of the augmented imaging method
- explain the online part of the augmented imaging method
- introduce the layered tissue model
- describe the calculation of spectral reflectance
- explain the adaptation to imaging system
- describe machine learning based inversion
- apply the trained regressor to in vivo recordings
- describe laparoscopic system
- introduce multispectral snapshot camera
- explain machine learning module
- describe data preparation
- explain convolutional neural networks
- describe normalization module
- explain functional estimation module
- define loss function
- describe calibration process
- explain RGB estimation
- detail practical implementation
- describe autocalibration step
- describe method for estimating light source from specular reflections
- identify specular highlights in multispectral image
- transform multispectral image to HSI color space
- segment specular regions and non-specular regions
- sort specular regions by size
- dilate specular regions to include non-saturated pixels
- separate diffused and specular reflection components
- estimate spectrum of illumination light source
- describe alternative method for estimating spectral composition of light
- acquire low exposure images and process for specular highlight segmentation
- estimate illuminant based on specular highlight analysis
- summarize experimental results
- discuss limitations of current approach
- propose extensions to method
- describe MSI-based augmented imaging system
- detail various embodiments of system
- discuss autocalibration schemes
- introduce approach to anatomical structure classification
- propose framework for performance assessment of multispectral cameras
- motivate uncertainty quantification
- describe probabilistic inference methods
- discuss uncertainty-based value aggregation
- introduce mode-based post-processing
- describe out-of-distribution detection
- define widely applicable information criterion (WAIC)
- compute WAIC with invertible neural networks

### EXAMPLES

- validate OoD detection approach through in silico simulations
- describe in silico quantitative validation methodology
- present results of in silico validation, including WAIC distribution analysis
- demonstrate OoD detection in in vivo applications, including organ detection
- illustrate use of OoD detection for scene change detection, including illumination changes
- discuss practical considerations and potential improvements for OoD detection implementation

