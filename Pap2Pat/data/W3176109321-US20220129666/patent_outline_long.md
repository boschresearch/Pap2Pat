# DESCRIPTION

## TECHNICAL FIELD

- relate to anomaly detection

## BACKGROUND

- introduce human poses
- motivate anomaly detection
- limitations of training data
- need for efficient solution

## SUMMARY

- employ anomaly detector
- classify anomaly data
- recognize non-availability of training data
- use discriminative one-class classifier
- address non-linearity and complexity
- provide pair of complementary classifiers
- bound normal data within boundary
- represent complexity of distribution
- solve non-convex optimization problem
- use Riemannian conjugate gradient optimization
- learn in Hilbert space
- use kernel embedding
- choose kernel based on data distribution
- reduce computational complexity
- implement in vehicle driver assistance system

## DETAILED DESCRIPTION

- clarify purpose of description
- define terminology and scope

### Overview

- introduce anomaly detector
- detect anomaly in human poses
- classify anomaly from normal data
- use discriminative one-class classifier
- include pair of complementary classifiers
- bound normal distribution of pose sequences
- optimize pair of complementary classifiers
- implement in different applications
- show schematic diagram of anomaly detection
- obtain sequence of poses from image frames
- include normal poses in sequence of poses
- use normal data for classifying outliers
- discriminate normal data and anomaly data
- use arbitrarily shaped boundaries
- impact of complexity and non-linearity
- provide sequence of poses to anomaly detector
- produce anomaly pose as output
- describe block diagram of anomaly detector
- include input interface
- include memory
- include processor
- include output interface
- store discriminative one-class classifier
- embed input data into RKHS
- project normal distribution of pose sequences
- use infinite dimensional linear space
- address complexity and non-linearity
- use different kernels for different data
- bound normal data from different directions
- classify embedded data using classifier
- render classification result
- output notification to human
- show graphical representation of classifiers
- bound normal distribution of pose sequences
- train discriminative one-class classifier
- estimate data density of normal distribution
- define orthonormal frames
- formulate optimization problem P2
- rewrite P2 as P'2
- rewrite P'2 as P''2
- introduce permutation matrix
- rewrite P''2 as P'''2
- minimize Euclidean distance
- define discriminative one-class classifier
- address non-convex optimization problem
- compute Riemannian gradient
- train pair of hyperspheres
- rewrite optimization problem
- simplify optimization problem
- approximate pair of hyperspheres
- define mathematical equations for W1, W2, b1, and b2
- describe trained discriminative one-class classifier 206
- introduce anomaly detector 106
- describe pipeline 500 for anomaly detection
- provide input sequence of poses 102
- accept input data via input interface 202
- embed input data into kernel space
- obtain embedded data
- classify embedded data using trained discriminative one-class classifier 206
- render classification result via output interface 210
- describe graphical representation 600 of classification result
- introduce vehicle driver assistance system 702
- describe environmental representation 700 of anomaly detection
- capture sequence of image frames with poses of occupants
- filter poses of occupants
- perform pre-processing of image frames
- match poses in image frames
- generate pose sequences for each occupant
- describe block diagram 800 of anomaly pose detection
- detect anomaly poses in sequence of image frames
- overview of anomaly detector
- normalize pose sequences
- prune joints based on detection score
- prune joints based on visibility flag
- normalize joints between [0,1]
- generate vector representation for each pose
- embed vector representation into sequence representation
- map sequence representation into normalized histogram
- map normalized histogram into bag-of-poses
- accept input data indicative of pose sequence distribution
- embed input data into element of RKHS
- classify embedded data using discriminative one-class classifier
- train discriminative one-class classifier using classification model
- estimate data density of normal distribution using min-max optimization
- render classification result via output interface
- implement anomaly detector in vehicle driver assistance system
- detect anomaly poses of occupants in vehicle
- send alert notification based on detected anomaly poses
- implement anomaly detector in security surveillance system
- detect anomaly events based on anomaly poses
- notify operators of security surveillance system
- implement anomaly detector in different applications
- detect anomaly audio in audio-based input data
- detect anomaly texts in textual-based input data
- show overall block diagram of anomaly detector
- describe processor and memory of anomaly detector
- describe input interface of anomaly detector
- describe network interface controller of anomaly detector
- describe storage device of anomaly detector
- describe output interface of anomaly detector
- describe advantages of anomaly detector
- describe implementation of anomaly detector
- describe software code execution on processor
- describe method of anomaly detection

