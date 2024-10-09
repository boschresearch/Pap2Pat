# DESCRIPTION

## BACKGROUND

- introduce digital PCR and its limitations
- discuss detrimental effects of partition size variation

## SUMMARY

- describe method for performing digital PCR
- describe system for performing digital PCR
- provide equations for concentration of target nucleic acids

## DETAILED DESCRIPTION

- provide overview of description

### INTRODUCTION

- introduce digital PCR method
- describe partitions and amplification
- mention Poisson statistics and limitations

### Implications of a Non-Mono-Dispersed Partition Size for Poisson Based Quantification

- discuss limitations of Poisson statistics
- investigate effect of volume variation on concentration estimation
- show impact of volume variation on precision

### Beyond the Poisson Model for Digital PCR Systems

- introduce volume variation method
- define concentration of target molecules
- apply Bayes' theorem
- derive joint probability distribution
- assume truncated normal distribution of partition sizes
- derive equation for P(neg)
- integrate out variable v
- provide final expression for P(neg)
- derive approximation for concentration C
- describe confidence intervals

### Results

- simulate impact of volume variation on dynamic range
- compare results from different models
- show remedial effects of alternate modeling
- discuss performance of different models
- conclude on importance of accurate modeling

## CONCLUSIONS

- summarize limitations of Poisson based quantification
- emphasize importance of accurate modeling

## Section A: Derivation of the Expression for the Probability of Negatives in the Variable λ Full Fidelity Model

- assume truncated normal distribution
- derive constant factor K
- obtain probability of negatives
- integrate probability distribution function
- substitute K into equation 5
- integrate probability of negatives
- derive integral I
- simplify integral I
- derive integral I'
- simplify integral I'
- obtain final expression for probability of negatives

## Section B: Derivation of the Expression for the Probability of Negatives in the Variable λ Approximation Model

- assume normal distribution of partition sizes
- define P(v) given in equation 4
- substitute P(v) in equation 5
- integrate variable v out
- define integral of exponential function
- solve for concentration C
- take natural logarithm of both sides
- rearrange equation to isolate C
- solve for C
- note that C can assume two values
- choose value with negative sign in front of square root
- illustrate improvement of results using volume variation model
- describe digital PCR experiments
- describe QuantStudio 3D chip
- filter out chips with artifacts
- use positive and negative counts to generate quantification result
- report mean result from each model
- show one standard deviation around mean value
- show percent prediction error based on annotations
- note that operations can be implemented using hardware, software, firmware, or combinations
- describe use of processors or other digital circuitry
- describe use of analog circuitry
- describe use of memory or other storage
- describe use of communication components
- illustrate computer system 400
- describe processor 404
- describe bus 402 or other communication medium
- describe memory 406
- describe storage device 410
- describe communications interface 418
- describe display 412
- describe input device 414
- describe cursor control 416
- describe data processing and confidence values
- describe computer-readable medium and computer program product
- describe various forms of computer-readable media

