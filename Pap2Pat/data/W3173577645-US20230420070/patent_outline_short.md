# DESCRIPTION

## BACKGROUND

- motivate protein structure prediction

## SUMMARY

- outline protein structure prediction solution

## DETAILED DESCRIPTION

- introduce neural networks and protein structure
- describe limitations of current protein structure prediction methods

### Example Environment

- describe computing device architecture
- explain components of computing device
- describe communication unit and input/output devices
- discuss cloud computing architecture
- illustrate computing device for protein structure prediction

### Structural Properties of Proteins and Fragments

- describe inter-residue distances and orientations
- explain torsion angles, backbone angles, and bond lengths/angles

### Evaluation of Fragment Library

- evaluate performance of fragment libraries built by different algorithms
- define evaluation metrics related to structural properties at fragment level
- calculate evaluation metrics for each reference fragment library
- select algorithm based on evaluation of fragment libraries

### Prediction of Protein Structure

- predict structure of target protein using structural information of fragment library
- extract structural properties of each fragment from fragment library
- determine probability distribution of structural property at each residue position
- build weighted Gaussian mixture models for each structural property
- generate potential function corresponding to structural property
- predict structure of target protein by minimizing target function

### Prediction of Protein Structural Properties

- utilize fragment library for structural property prediction
- extract structural properties from fragments
- encode structural properties using feature encoder
- predict structural properties using property predictor
- train feature encoder and property predictor jointly

### Example Method and Example Implementations

- determine fragments for each residue position
- generate feature representation of fragment structures
- predict structural property or structure of target protein
- determine property values of structural property
- generate potential function and target function
- determine prediction of structural property or structure
- select target algorithm for building fragment library
- provide computer-implemented method and electronic device

