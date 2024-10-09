# DESCRIPTION

## BACKGROUND

- introduce endomicroscopic imaging technologies
- describe advantages of endomicroscopic imaging
- describe difficulties in interpreting images
- describe limitations of current systems
- motivate need for image quality assessment
- describe challenges in image analysis

## SUMMARY

- introduce method for transforming digital image
- describe receiving first image
- describe providing first image to neural network
- describe receiving features from neural network
- describe receiving second image features
- describe generating loss value
- describe generating fourth image
- describe providing fourth image to neural network
- describe receiving features from neural network
- describe generating second loss value
- describe generating fifth image
- describe presenting fifth image
- describe optional embodiments
- describe using VGG-19 neural network
- describe generating Gram matrices
- describe using loss function
- describe optional weights and parameters
- describe optional image types

## DETAILED DESCRIPTION

- introduce systems, methods, and media for transforming digital images into simulated pathology images
- describe mechanisms for receiving digital images and transforming them into H&E style images
- motivate use of endomicroscopy devices for generating digital images
- describe limitations of endomicroscopy images compared to H&E slides
- introduce image style transfer techniques as a solution
- describe use of style reference images in image style transfer
- provide example of style reference image (FIG. 3)
- describe different procedures for creating H&E stained tissue samples
- compare advantages of endomicroscopy devices to conventional frozen section or FFPE procedures
- describe limitations of supervised learning for image style transfer
- introduce image style transfer techniques using feature maps
- describe use of convolutional neural networks (CNNs) for feature map extraction
- describe process for transforming digital images into simulated pathology images (FIG. 4)
- select and/or receive digital image to be transformed
- select and/or receive style reference image
- provide style reference image to trained model and receive style features
- describe extraction of style features from hidden layers of trained model
- conclude description of image style transfer techniques for transforming digital images into simulated pathology images
- extract style features from ReLU layers
- select trained model for feature extraction
- generate content features from original image
- extract content features from hidden layers
- generate initial target image
- generate style and content features for target image
- calculate loss value using loss function
- determine transformation completion
- modify target image using optimization algorithm
- output transformed image for evaluation
- perform multiple transformations with different parameters
- describe image analysis techniques
- motivate use of endomicroscopy device
- describe hardware components of endomicroscopy device
- describe computing device components
- describe server components
- describe communication network
- illustrate example of convolutional neural network
- illustrate example of target image color channel changes
- illustrate example of hardware components
- describe stylization process
- describe evaluation of stylized images
- describe scoring system for image quality
- illustrate example of subjective impact scores
- describe results of stylized image evaluation
- illustrate example of intensity map
- describe analysis of stylized image results
- illustrate example of removed critical structures
- illustrate example of added artifacts
- describe computer readable media
- define mechanism
- describe flexibility of process steps
- provide disclaimer and incorporate prior art

