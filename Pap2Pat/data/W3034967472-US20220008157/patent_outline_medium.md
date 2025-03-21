# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate augmented imaging
- describe tissue parameters
- limitations of existing methods
- application of multispectral imaging
- challenges in real-time estimation

## SUMMARY OF THE INVENTION

- introduce problem of functional imaging
- propose method and system for functional imaging
- define method of generating augmented images
- estimate spectral composition of light
- obtain multispectral images
- apply machine learning based regressor or classifier
- derive tissue parameters from multispectral images
- explain application of regressor or classifier
- describe three variants of applying regressor or classifier
- select regressor or classifier based on estimated spectral composition
- transform multispectral image based on estimated spectral composition
- retrain regressor or classifier using simulation data
- combine multiple variants of applying regressor or classifier
- define augmented imaging and tissue parameter
- provide examples of tissue parameters
- describe functional or physiological parameters
- describe tissue classification parameters
- describe event parameters
- describe prediction-of-event parameters
- estimate spectral composition of illuminating light
- identify regions of specular reflection
- transform multispectral image to lower dimensional color space
- separate specular and diffused reflection contributions
- estimate spectral composition based on selected pixels or pixel groups
- introduce multispectral imaging
- motivate CNNs for tissue parameter estimation
- describe neighborhood-based estimation
- define multispectral pixel and sensor
- train regressor or classifier using simulated data
- input reflectance values to regressor or classifier
- derive RGB image from multispectral image
- train regressor or classifier using forward model
- describe layered tissue model
- adapt spectral reflectance to imaging system
- select simulations based on real tissue measurements
- apply multiple regressors or classifiers
- provide confidence value with tissue parameter prediction
- handle low confidence values
- derive probabilistic distribution of tissue parameters
- generate new multispectral image with different setup
- determine suitable wavelength bands for oxygenation estimation
- describe out of distribution detection
- introduce OoD detection algorithm
- motivate neural networks
- describe autoencoder based anomaly detection
- explain OoD detection for regressor or classifier selection
- describe system for generating augmented images
- introduce apparatus for estimating spectral composition
- describe multispectral camera
- explain machine learning module
- describe tissue parameters
- introduce apparatus for estimating spectral composition
- describe estimation of spectral composition
- explain transformation of multispectral image
- describe sorting of regions of specular reflection
- explain morphologic dilation
- describe separation of specular and diffused reflection
- introduce lower exposure multispectral images
- describe estimation of spectral composition
- explain selection of pixels or pixel groups
- describe transformation to quasi-continuous spectrum
- introduce series of augmented images
- describe multispectral sensor
- explain regressor or classifier based on convolutional neural network
- describe application of regressor or classifier
- introduce simulated neighborhood
- describe obtaining reflectance values
- explain derivation of RGB image
- introduce forward model
- describe tissue model
- explain adaptation of spectral reflectance

## DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce multispectral imaging (MSI) and its potential
- describe challenges in deciphering MSI information
- introduce embodiments of the invention for video-rate estimation of physiological parameters
- describe the augmented imaging method according to an embodiment of the present invention
- outline the offline part of the method, including training
- describe the online part of the method, including real-time estimation
- introduce the concept of a forward model
- describe the layered tissue model used in the forward model
- define the optical and physiological parameters of the tissue model
- describe the calculation of the absorption coefficient
- describe the calculation of the reduced scattering coefficient
- describe the calculation of the scattering coefficient
- introduce the concept of pixel independence
- describe the calculation of spectral reflectance
- introduce the Monte Carlo method for simulating light transport
- describe the adaptation to the imaging system
- describe the simulation of image intensities
- introduce the concept of band reflectance
- describe the machine learning based inversion method
- outline the application of the trained regressor to in vivo recordings
- describe laparoscopic system
- introduce multispectral snapshot camera
- explain camera filter and data link
- describe machine learning module and computing device
- introduce display device and augmented image
- motivate convolutional neural networks
- describe offline training network
- explain data preparation module
- simulate local neighborhoods and mosaics
- incorporate spatial neighborhood into estimation
- describe normalization module
- demosaic and normalize mosaic images
- establish relationship between input data and tissue parameters
- describe functional estimation module
- apply machine learning based regressor to multispectral image
- define loss function
- motivate scaling of parameters
- describe calibration process
- introduce RGB estimation
- describe practical implementation
- present results of approach
- discuss limitations of Beer-Lambert approach
- compare performance of different methods
- introduce autocalibration step
- describe two variants of autocalibration
- explain transformation of multispectral image
- describe method for estimating light source from specular reflections
- identify specular highlights in MSI
- transform MSI to HSI color space
- segment HSI image into specular regions and non-specular regions
- sort specular regions by size
- deal with overexposed pixels using morphologic dilatation
- separate diffused and specular reflection components using PCA
- estimate spectrum of illumination light source
- derive quasi-continuous spectrum of actual light source
- describe color constancy method
- illustrate simpler variant for estimating spectral composition of light
- acquire low exposure images
- process low exposure images using specular highlight segmentation
- estimate illuminant based on specular highlight pixels
- validate approach using five different light sources
- quantify difference between two LS spectra using Euclidean angle
- generate in silico data for quantitative validation
- assess accuracy and robustness of approach
- analyze effect of errors in estimation of spectrum of LS on accuracy of functional parameter estimation
- determine optimal values for hyperparameters
- quantify impact of error in illuminant estimation on oxygenation estimation error
- perform qualitative validation using multispectral imaging stream
- confirm guiding hypothesis
- discuss robustness of estimation results
- describe embodiment with homogenous illuminant spectrum
- propose extensions to embodiment
- describe MSI-based augmented imaging system
- discuss association of camera with operating room light source
- describe computing device and display device
- introduce goggles embodiment
- describe data processing unit and augmented image display
- discuss autocalibration schemes
- describe gesture recognition and eye tracking
- introduce speech control
- discuss rearrangement of components
- describe connection to external database
- propose anatomic structure classification
- describe approach to anatomical structure classification
- introduce framework for performance assessment of multispectral cameras
- describe preferred embodiments
- propose integrating uncertainty quantification and compensation
- categorize main sources of uncertainty
- determine uncertainty of estimation
- describe measures of confidence
- describe probabilistic inference
- describe other probabilistic approaches
- use uncertainty in multiple ways
- describe mode-based post-processing
- address issue of out of distribution datasets
- propose multi-stage process for uncertainty handling
- describe information theory based approach
- define widely applicable information criterion (WAIC)
- compute WAIC with invertible neural networks

### EXAMPLES

- introduce in silico validation
- describe simulation framework
- generate data set Xraw
- split data set into training and test sets
- convert spectra to camera measurements
- train ensemble of INNs
- evaluate WAIC value
- investigate WAIC distribution
- introduce in vivo applications
- describe OoD detection for scene changes
- demonstrate automatic detection of illumination changes
- discuss practical implementation considerations

