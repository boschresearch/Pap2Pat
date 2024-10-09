# DESCRIPTION

## BACKGROUND

- motivate protein structure prediction

## SUMMARY

- introduce protein structure prediction solution
- outline prediction process
- highlight benefits of solution

## DETAILED DESCRIPTION

- introduce example implementations
- define terms used in the disclosure
- describe structure of a protein
- describe fragment assembly for protein structure prediction
- describe limitations of current protein structure prediction methods
- introduce solution for protein structure prediction
- describe example environment for implementing the solution
- describe components of a computing device
- describe functions of components of the computing device
- describe cloud computing architecture
- describe use of computing device for protein structure prediction

### Example Environment

- describe computing device
- describe components of computing device
- describe processing unit
- describe memory
- describe storage device
- describe communication unit
- describe input device
- describe output device
- describe computing device in a networked environment
- describe external devices
- describe cloud computing architecture
- describe components of cloud computing architecture
- describe services provided by cloud computing
- describe data storage in cloud computing
- describe computing resources in cloud computing
- describe use of cloud computing for protein structure prediction
- describe input information for protein structure prediction
- describe amino acid sequence of target protein
- describe fragment library for target protein
- describe residue position of target protein
- describe template fragment

### Structural Properties of Proteins and Fragments

- describe structural properties of proteins
- describe inter-residue distances
- describe Cα-Cα distance
- describe Cβ-Cβ distance
- describe inter-residue orientations
- describe torsion angles φ and ω
- describe backbone angles θ and τ
- describe other orientations between atoms
- describe bond lengths and bond angles
- describe secondary structure of a fragment

### Evaluation of Fragment Library

- introduce fragment library evaluation
- define evaluation metrics
- describe precision and coverage metrics
- introduce structural property metrics
- define accuracy of secondary structure
- define error of angles φ, ψ, ω, θ and τ
- define error of Cα-Cα and Cβ-Cβ distances
- describe evaluation of fragment libraries built by different algorithms
- select algorithm based on evaluation metrics
- describe process of selecting algorithm
- calculate evaluation metrics for each fragment library
- compare evaluation metrics among fragment libraries
- select algorithm with best performance
- describe advantages of using evaluation metrics
- summarize evaluation metrics
- conclude evaluation of fragment library

### Prediction of Protein Structure

- introduce protein structure prediction
- describe prediction module
- extract structural properties from fragment library
- determine feature representation of structural properties
- describe process of predicting protein structure
- extract fragments from initial fragment library
- process initial fragment library
- generate fragments with same length
- determine probability distribution of structural properties
- describe Gaussian mixture models
- assign weights to fragments
- build weighted Gaussian mixture models
- determine feature representation of structural properties
- generate potential function from Gaussian distribution
- describe potential functions for different structural properties
- combine potential functions
- tune weights on reference dataset
- describe target function for structure prediction model
- minimize target function
- generate predicted structure of target protein
- describe advantages of using potential functions
- compare with other methods
- summarize protein structure prediction
- conclude protein structure prediction
- finalize protein structure prediction

### Prediction of Protein Structural Properties

- introduce protein structural properties prediction
- describe fragment library property set extraction
- extract structural properties for each residue position
- pad fragments to have a length of R residues
- represent fragment library property set as L×F×R×D tensor
- input fragment library property set to feature encoder
- generate fragment library feature set by encoding
- obtain structural feature at each residue position
- describe feature encoder architecture
- perform convolution process
- select implicit representation of one residue
- average all F fragments at the same residue position
- input fragment library feature set to property predictor
- input sequence feature set to property predictor
- predict structural properties of target protein
- describe property predictor architecture
- perform pre-processing on input features
- use two-dimensional residual neural network
- perform symmetrization operation
- predict different structural properties

### Example Method and Example Implementations

- describe method for protein structure prediction
- determine fragments for each residue position
- generate first feature representation of structures
- determine prediction of structure or structural property
- describe generating first feature representation
- determine property value of structural property
- determine probability distribution of structural property
- describe determining prediction of structure
- generate potential function
- determine target function of structure prediction model
- determine prediction of structure by minimizing target function
- describe determining plurality of fragments
- determine initial fragments
- generate fragments with predetermined number of residues
- describe structural property
- describe generating first feature representation
- determine plurality of structural properties
- encode structural properties according to feature encoder
- describe determining prediction of structural property
- determine second feature representation of amino acid sequence
- determine prediction of structural property
- describe selecting target algorithm
- determine reference property values
- determine true property value
- determine difference between reference and true property values
- select target algorithm based on differences
- describe electronic device
- describe processing unit and memory
- describe instructions stored in memory
- describe computer program product
- describe computer-readable medium
- describe hardware logic components
- describe program code
- describe machine-readable medium

