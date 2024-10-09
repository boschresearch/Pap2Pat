# DESCRIPTION

## FIELD

- define field

## BACKGROUND

- limitations of image transformation

## SUMMARY

- introduce image-to-image translation
- application of machine-learned model
- embodiment of method

## DETAILED DESCRIPTION

### Overview

- introduce machine-learned model for image transformation
- describe user-specified conditioning vector
- motivate fine-grained control over image transformations
- describe limitations of existing image transformation models
- introduce adversarial training approach
- describe machine-learned generator model
- describe machine-learned discriminator model
- describe user-specified conditioning vector parameters
- describe degree of transformation control
- describe real and continuously valued vector
- describe transformation application to input image
- describe output image characteristics
- describe style characteristic transformation
- describe light characteristic transformation
- describe color characteristic transformation
- describe environmental characteristic transformation
- describe time of day transformation
- describe feature characteristic transformation
- describe encoder and decoder portions of generator model
- describe residual blocks in generator model
- describe mixing of image representation and conditioning vector
- describe decoding of combined data
- describe neural network architecture of generator model
- describe feed-forward neural network architecture
- describe convolutional neural network architecture
- describe residual neural network architecture
- describe connections between layers in generator model
- describe backpropagation of training signal
- describe discriminator model architecture
- describe target image selection
- describe discriminator output generation
- describe evaluation of different aspects of discriminator output
- describe mixing of image representation and conditioning vector in discriminator model
- describe classification score generation
- describe selection output generation
- describe training of generator and discriminator models
- describe adversarial training of generator and discriminator models
- describe backwards propagation of errors
- describe truncated backpropagation through time
- describe generative adversarial network architecture
- describe reconstructive transformations on output image
- describe removal of transformations applied to input image
- describe reconstructive discriminator output generation
- describe training of generator model based on reconstructive discriminator output
- describe enforcement of cyclic consistency
- describe enhancement of generative abilities of generator model
- describe technical effects and benefits of present disclosure
- describe significance of user-specified control over transformations
- describe elimination of paired training data requirement
- describe generalized machine-learned generator model
- describe application of multiple transformations to input image

### Example Devices and Systems

- introduce computing system 100
- describe user computing device 102
- specify user computing device components
- define machine-learned model(s) 120
- describe storage of machine-learned model(s) 120
- introduce server computing system 130
- describe server computing system components
- define machine-learned model(s) 140
- describe storage of machine-learned model(s) 140
- introduce image transformation computing system 150
- describe image transformation computing system components
- introduce model trainer 160
- describe training of machine-learned model(s)
- introduce image transforming model(s) 159
- describe image transformation process
- introduce network 180
- describe network communication
- illustrate alternative computing system
- introduce computing device 10
- describe applications on computing device 10
- introduce machine learning library
- describe communication between applications
- introduce computing device 50
- describe applications on computing device 50
- introduce central intelligence layer
- describe machine-learned models in central intelligence layer
- describe central device data layer

### Example Training Environment and Methods

- introduce machine-learned models for output image generation
- describe input image and user-specified conditioning vector
- define user-specified conditioning vector parameters
- describe degree of transformation application
- specify areas of input image for transformation
- introduce machine-learned generator models
- describe encoder and decoder portions
- detail residual blocks and neural networks
- describe transformation of input image
- generate output image with desired characteristics
- specify defined characteristics of output image
- describe style characteristic transformations
- detail light characteristic transformations
- describe color characteristic transformations
- introduce environmental characteristic transformations
- describe time of day transformations
- detail feature characteristic transformations
- introduce machine-learned discriminator models
- describe discriminator output generation
- detail target image selection
- describe discriminator model layers
- detail convolutional and fully connected layers
- describe mixing of representations
- generate classification score for output image
- obtain selection output
- introduce generative adversarial network (GAN)
- describe residual neural networks
- detail connections between layers
- describe backpropagation of training signal
- train machine-learned generator models
- detail objective function evaluation
- describe adversarial training
- introduce FIG. 5
- describe mirrored configuration of models
- introduce machine-learned generator models for reconstruction
- describe reconstructed output image generation
- detail reversing parameterized transformations
- describe reconstructed input image
- conclude example training environment and methods
- introduce training environment and methods
- describe reconstructive discriminator output
- explain optimization function
- detail backpropagation
- describe mirrored model architecture
- explain transformational model architecture
- formulate objective function
- define parametrizable transformation
- describe machine-learned generator model
- explain machine-learned discriminator model
- detail cyclic consistency
- describe loss signals
- explain scalar value
- describe graphical representation of day-to-night image transformation
- detail user-specified conditioning vector
- explain fine-grained control
- describe additional transformation
- explain summer-to-winter transformation
- detail light source image transformation
- describe graphical representation of light source image transformation
- explain three-dimensional specification
- describe graphical representation of day-to-night and weather transformations
- detail simultaneous application of transformations
- explain flowchart of method for training machine-learned models
- obtain machine-learned generator models
- receive input image and user-specified conditioning vector
- generate output image
- describe defined characteristics of output image
- explain style characteristic
- detail style transformation
- describe reverse style transformation
- explain degree of transformation application

### Additional Disclosure

- - discuss system flexibility
- - disclaim limitation of embodiments
- - allow for method variations

