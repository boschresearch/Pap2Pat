# DESCRIPTION

## TECHNICAL FIELD

- relate to pose transfer

## BACKGROUND

- introduce pose transfer task
- limitations of prior art

## SUMMARY

- introduce pose transfer method
- learn shape code for character
- deform character into target pose

## DETAILED DESCRIPTION

- introduce method 100 for learning shape code for 3D character
- describe device and system for performing method 100
- process 3D character using machine learning model to learn latent shape code
- define 3D character and stylized character
- describe source pose of 3D character
- learn latent shape code using machine learning model
- include shape information in latent shape code
- include body part segmentation labels in latent shape code
- train machine learning model using supervised learning
- output latent shape code
- use latent shape code for pose transfer
- describe method 200 for transferring pose from source avatar to 3D character
- process 3D character using machine learning model to learn latent shape code
- output latent shape code to second machine learning model
- deform 3D character into target pose using second machine learning model
- define target pose and target pose code
- deform 3D character into target pose
- include MLP in second machine learning model
- train second machine learning model using supervised learning
- apply volume-preserving constraint to deformed 3D character
- preserve volume of each body part
- describe system 300 for transferring pose from source avatar to 3D character
- include shape understanding module 302 in system 300
- include implicit pose deformation module 304 in system 300
- include volume-based test-time training module 306 in system 300
- describe shape understanding module 400
- predict latent shape code using shape understanding module 400
- include occupancy prediction in shape understanding module 400
- include part segmentation prediction in shape understanding module 400
- train shape understanding module 400 using supervised learning
- describe pose deformation module 500
- deform 3D character into target pose using pose deformation module 500
- include neural implicit function in pose deformation module 500
- train pose deformation module 500 using supervised learning
- describe test-time training
- fine-tune pose deformation module 500 on unseen stylized characters
- use volume-preserving constraint during test-time training
- preserve Euclidean distance between pairs of vertices
- minimize change in distance between pairs of vertices
- use driving character in rest pose and deformed shape as paired training data
- minimize L2 distance between predicted movement and ground truth movement
- include edge loss in test-time training
- balance loss weights using hyper-parameters
- illustrate pose transfer from source avatar to 3D character
- deform 3D character into target pose

### Machine Learning

- introduce deep neural networks
- advantage over svm
- deep learning models
- self-driving cars
- drug development
- image captioning
- language translation
- neural learning process
- child learning analogy
- object recognition
- context assignment
- neuron functionality
- artificial neuron
- perceptron features
- weight assignment
- deep neural network model
- multiple layers
- input data processing
- pattern recognition
- object classification
- inference process
- handwritten number recognition
- image classification
- speech translation
- training complex neural networks
- parallel computing performance
- floating-point multiplications
- latency-sensitive process
- introduce inference and training logic
- data storage for forward propagation
- data storage for backward propagation
- separate storage structures
- same storage structure
- partially same storage structure
- arithmetic logic unit
- linear algebraic operations
- activation storage
- cache memory
- dram
- sram
- non-volatile memory
- application-specific integrated circuit
- central processing unit
- graphics processing unit
- field programmable gate arrays
- neural network training and deployment
- untrained neural network
- training dataset
- training framework
- supervised learning
- unsupervised learning
- semi-supervised learning
- data center infrastructure

