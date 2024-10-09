# DESCRIPTION

## BACKGROUND

- motivate protein structure prediction

## SUMMARY

- outline protein structure prediction solution

## DETAILED DESCRIPTION

- introduce example implementations
- define neural network and its components
- describe protein structure and its levels
- explain fragment assembly and its limitations
- introduce solution for protein structure prediction

### Example Environment

- describe computing device 100
- list components of computing device 100
- explain processing unit 110
- describe memory 120 and sample processing modules 122
- explain storage device 130
- describe communication unit 140
- list input devices 150
- list output devices 160
- explain cloud computing architecture
- describe how computing device 100 can be used for protein structure prediction

### Structural Properties of Proteins and Fragments

- describe inter-residue distances
- explain inter-residue orientations
- describe torsion angles φ, ψ, and ω
- explain backbone angles θ and τ
- describe other structural properties

### Evaluation of Fragment Library

- evaluate performance of fragment libraries
- introduce evaluation metrics
- define accuracy of secondary structure
- define error of angles φ, ψ, ω, θ and τ
- define error of inter-residue distances
- describe evaluation process
- select algorithm based on evaluation
- summarize evaluation metrics

### Prediction of Protein Structure

- predict protein structure using fragment library
- extract structural properties from fragment library
- process initial fragment library
- generate feature representation of structural property
- describe Gaussian mixture models
- assign weights to fragments
- build weighted Gaussian mixture models
- determine probability distribution of structural property
- generate potential function from Gaussian distribution
- combine potential functions
- determine target function for structure prediction model
- predict protein structure by minimizing target function

### Prediction of Protein Structural Properties

- utilize fragment library for structural property prediction
- extract structural properties from fragments
- encode structural properties using feature encoder
- generate fragment library feature set
- input feature set into property predictor
- predict structural properties of target protein
- describe process of encoding structural information
- illustrate process of predicting structural properties
- detail property predictor architecture
- summarize advantages of using implicit features

### Example Method and Example Implementations

- describe method for protein structure prediction
- determine fragments for each residue position
- generate feature representation of fragment structures
- predict structure or structural property of target protein
- detail generating feature representation
- determine property values of structural property
- generate probability distribution of structural property
- predict structure of target protein
- generate potential function
- determine target function of structure prediction model
- predict structure of target protein by minimizing target function
- describe alternative method for generating feature representation
- encode structural properties using trained feature encoder
- predict structural property of target protein
- determine second feature representation of amino acid sequence
- select target algorithm for building fragment library
- summarize example implementations

