# DESCRIPTION

## STATEMENT OF GOVERNMENT SPONSORED SUPPORT

- acknowledge government funding

## FIELD OF THE INVENTION

- relate to brain machine interfaces

## BACKGROUND OF THE INVENTION

- introduce brain machine interface challenges

## SUMMARY OF THE INVENTION

- introduce brain machine interface decoder
- describe neural to kinematic mapping function
- highlight advantages of the invention

## DETAILED DESCRIPTION OF THE INVENTION

- introduce Big-Data Multiplicative Recurrent Neural Network (BD-MRNN)

### MRNN Definition

- define recurrent network model
- describe multiplicative interaction
- introduce equation governing dynamics

### MRNN Output Definition

- define output of the network

### Network Construction for Cursor BMI Decoder

- describe network construction

### MRNN Initialization

- initialize network parameters

### Concatenating Neural Trials for Seeding the MRNN During Training

- concatenate neural trials

### Perturbing the Neural Input During Training

- introduce perturbations to neural spike trains
- describe global modulation
- describe channel by channel perturbations

### Using Many Days Training Data

- introduce using multiple days of training data
- describe nonlinear, multiplicative architecture

### Network Output

- train two MRNN networks
- combine position and velocity outputs

### Training and Running the Networks

- simulate network using Euler method
- evaluate network output
- train network offline
- use Hessian-Free optimization method
- set critical parameters
- copy network into embedded real-time environment
- run network in closed-loop
- receive binned spikes
- output hand position
- display cursor position
- initialize velocity values
- initialize MRNN hidden state
- describe model parameters
- remark on using multiple days of training data
- describe assumption of data distribution
- describe analogous example of handwritten letter classification

