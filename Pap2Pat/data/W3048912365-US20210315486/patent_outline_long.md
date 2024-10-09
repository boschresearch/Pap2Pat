# DESCRIPTION

- acknowledge government support

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate gait analysis
- limitations of current methods

## SUMMARY OF THE INVENTION

- introduce motion evaluation system
- identify keypoint trajectories
- predict motion evaluation score
- provide output based on score
- embodiment of keypoints identification
- embodiment of score prediction
- various applications of output

## DETAILED DESCRIPTION

- introduce motion evaluation system
- describe process for evaluating gait
- define keypoints and their identification
- describe keypoint trajectories and their extraction
- train model to evaluate keypoint trajectories
- generate evaluation scores
- provide outputs based on generated scores
- describe systems for clinical gait evaluation
- illustrate motion evaluation system architecture
- describe motion evaluation element components
- illustrate motion evaluation application components
- describe evaluation engines and their components
- illustrate CNN architecture example

### Systems for Clinical Gait Evaluation

- describe motion evaluation system architecture
- illustrate network and server systems
- describe personal devices and image capture devices
- describe motion evaluation element components
- illustrate motion evaluation element architecture
- describe processor and image capture device functions
- describe network interface and memory components
- describe motion evaluation application components
- illustrate motion evaluation application architecture
- describe image receiver functions
- describe joint analysis engine functions
- describe evaluation training engine functions
- describe evaluation engine functions
- describe output engine functions
- describe evaluation engines and their components
- describe support vector regression
- describe ridge regression
- describe convolutional neural networks
- illustrate CNN architecture example
- describe activation functions and batch normalization
- describe max pooling and dropout
- describe training and optimization of CNN models

### Evaluation Engines

- describe evaluation engines and their components
- describe support vector regression
- describe ridge regression
- describe convolutional neural networks
- illustrate CNN architecture example
- describe activation functions and batch normalization
- describe max pooling and dropout
- describe training and optimization of CNN models
- describe filtering or dropping noisy coordinates
- describe random search for tuning learning rate
- describe early stopping and L2 regularization
- describe ensembling multiple CNN models
- illustrate another CNN architecture example

### Training for Clinical Gait Evaluation

- receive input images or video
- use images from single video or multiple videos
- receive input images from multiple perspectives
- use images from multiple videos captured at different times
- process input images to normalize for analysis
- convert videos to specific resolution and frame rate
- process training data with additional data
- augment data to increase accuracy and generalization
- divide existing data into multiple samples
- filter extracted keypoint trajectories to remove missing data
- remove extraneous frames from extracted trajectories
- generate features of user's motion
- engineer summary statistics of raw and derived time series
- derive time series to improve CNN performance
- center and scale bivariate time series
- smooth univariate time series and impute missing values
- augment time series data using window slicing
- extract overlapping segments from input time series
- label each segment with associated evaluation score
- drop segments with more than 50% missing data
- modify L2 loss function to account for varying segment counts
- extract trajectories of keypoints using OpenPose or other methods

### Applications of Motion Evaluation

- apply motion evaluation to various fields
- modify system for different types of movement
- support physical therapy with motion evaluation scores

