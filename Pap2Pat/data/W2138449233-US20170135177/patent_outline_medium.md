# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- limitations of existing systems

## SUMMARY

- introduce smart lighting system
- describe light transport model
- summarize system aspects

## DETAILED DESCRIPTION

- introduce occupancy sensitive smart lighting system
- define occupancy
- describe control strategy module and occupancy sensing module
- illustrate smart lighting system with FIGS. 1 and 2
- describe sensing stage
- describe adjusting stage
- illustrate perturbation modulated light with FIG. 9
- describe computer system for implementing lighting control system
- describe control strategy module components
- describe occupancy sensing module components
- describe light transport model
- describe solving for light transport matrix A
- describe underdetermined system and sparsity assumption
- describe minimizing difference between A and A0

### Rank Minimization

- describe rank minimization problem
- solve rank minimization problem using SVD

### Perturbation-Modulated Lighting

- describe perturbation strategies
- discuss perturbation magnitude
- optimize perturbation sequence for comfort

### Analysis of the Light Transport Matrix

- introduce light transport matrix
- describe classification approach
- motivate classification problem examples
- describe classification method using supervised learning
- present experimental results
- discuss limitations of classification approach

### Volume Rendering

- introduce 3D scene estimation approach
- describe light blockage model
- aggregate difference matrix
- compute confidence of point being occupied
- define Gaussian kernel
- render 3D volume
- describe 3D confidence map
- discuss limitations of 3D scene estimation approach
- introduce occupancy map estimation approach
- describe light reflection model
- define luminous intensity and flux
- compute luminous flux arriving at sensor
- describe reflection kernel
- compute confidence map
- discuss limitations of occupancy map estimation approach
- introduce flow diagram of method
- set initial base light control values
- adjust base light based on estimated occupancy

