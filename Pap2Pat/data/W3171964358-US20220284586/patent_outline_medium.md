# DESCRIPTION

## FIELD OF THE INVENTION

- introduce CAD system for pulmonary function assessment

## BACKGROUND OF THE INVENTION

- describe COVID-19 symptoms and diagnosis
- discuss limitations of PCR test
- explain role of chest radiography in COVID-19 diagnosis
- discuss AI in COVID-19 diagnosis and patient selection
- highlight limitations of current CAD systems

## SUMMARY

- introduce novel CAD system for COVID-19 diagnosis

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- illustrate CAD system for assessment of pulmonary function in patients with Coronaviridae infection

### Data Preprocessing

- segment medical image to identify lung region
- apply regional dynamic histogram equalization and mask off healthy lung tissues

### Rotating, Scale, and Translation Invariant MGRF Model

- construct MGRF model to capture appearance of infected lung regions
- define neighborhood system and Gibbs potential functions
- calculate joint probability of object pixels according to Gibbs distribution
- approximate Gibbs potential functions using centered, training-set average, normalized histograms and co-occurrence matrices
- calculate Gibbs energy of infected lung region
- use CDF as new scale-invariant representation of estimated Gibbs energy

### NN-Based Fusion and Diagnostic System

- fuse diagnostic results from estimated Gibbs energy at different radii using NN system
- train NN-based diagnostic system using backpropagation approach and hyper-parameters estimation

### Experimental Results

- test and validate system using data from publicly available archive of COVID-19 positive cases
- illustrate estimated Gibbs energy for high and low severity lung infections
- compare accuracy of proposed NN-based fusion system with other classification approaches

## Automation

- implement steps in method 10 in automated fashion using computer or other electronic device
- describe exemplary apparatus for implementing steps in method 10
- outline hardware and software components of computer

## Discussion and Conclusion

- introduce ARDS and its effects
- describe respiratory support methods
- discuss ventilator shortage and risks
- motivate AI-based diagnosis
- summarize AI-based method benefits
- describe multimodal data fusion
- introduce embodiment X1
- introduce embodiment X2
- introduce embodiment X3
- list additional embodiment features

