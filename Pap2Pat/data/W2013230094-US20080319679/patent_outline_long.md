# DESCRIPTION

## FIELD OF THE INVENTION

- define field

## BACKGROUND OF THE INVENTION

- introduce microarrays
- describe experiment steps
- explain array types
- detail Affymetrix GeneChip
- discuss limitations
- describe block effect
- explain normalization
- discuss standard assumptions
- highlight need for improvement

## SUMMARY OF THE INVENTION

- introduce method
- describe normalization step
- outline subarray approach
- summarize expression profiles
- detect defective areas

## DETAILED DESCRIPTION

- introduce normalization problem in microarray analysis

### Overview

- motivate normalization
- describe problem of normalization
- introduce blind inversion approach
- discuss limitations of existing methods
- propose new approach using least trimmed squares algorithm
- consider spatial variations in arrays
- introduce subarray normalization
- discuss parameterization of function g
- describe simple least trimmed squares
- discuss multiple arrays and multiple references

### Statistical Principle of Normalization

- formulate normalization as blind inversion problem
- define system function h
- assume joint distribution of true concentrations
- estimate transformation h
- propose minimization problem
- discuss smoothness of g

### Differentiation Fraction and Undifferentiated Probe Set

- consider mixture distribution of input
- discuss separation of two components

### Spatial Pattern and Sub-arrays

- divide each chip into sub-arrays

### Parameterization

- parameterize function g by linear function

### Simple Least Trimmed Squares

- define LTS estimate
- discuss properties of LTS estimator

### Multiple Arrays and Multiple References

- discuss strategy of normalization
- propose method of summarizing multiple array experiments

### The Probe-Treatment-Reference (PTR) Summarization Model

- introduce PTR model
- discuss reference-effect
- describe PTR method
- discuss advantages of PTR method
- propose three-factor model
- discuss constraints on parameters
- describe LAD estimation
- discuss computation of LAD estimation
- propose median polish approach
- discuss strategy of normalization and summarization
- describe typical treatment-control case

### Least Absolute Deviations (LAD) Estimation and its Computation

- formulate LAD problem
- discuss LP algorithms
- propose median polish approach
- discuss property of LAD solution
- describe iteration process
- discuss convergence of iteration
- propose stopping criterion

## EXEMPLARY EMBODIMENTS

- introduce method of analyzing microarray data
- define microarray
- motivate normalization using regressional analysis
- describe least trimmed squares regression method
- specify computation algorithm
- describe subarray normalization
- discuss duplicate microarrays
- motivate trim fraction
- describe sub-dividing array into subarrays
- discuss normalization techniques
- describe analyzing normalized data
- introduce method for obtaining expression profiles
- describe PTR model
- introduce method for detecting defective areas
- describe computer systems for practicing methods
- discuss implementation approaches

## EXAMPLES

### Example 1

- introduce microarray data
- describe Affymetrix Spike-in dataset
- explain experimental design
- introduce SUB-SUB normalization
- describe implementation of SUB-SUB normalization
- discuss parameter selection
- recommend sub-array size and overlapping size
- discuss trimming fraction selection
- apply SUB-SUB normalization to Affymetrix Spike-in dataset
- show results of SUB-SUB normalization
- discuss spatial pattern of hybridization
- introduce perturbed Spike-in dataset
- apply SUB-SUB normalization to perturbed dataset
- show results of SUB-SUB normalization on perturbed dataset
- discuss Primate Brain Expression dataset
- apply SUB-SUB normalization to Primate Brain Expression dataset
- show results of SUB-SUB normalization on Primate Brain Expression dataset
- discuss variation reduction by sub-array normalization
- compare SUB-SUB normalization with other normalization methods
- discuss external controls
- discuss cases with large fractions of differentially expressed genes
- discuss nonlinear array transformation vs linear sub-array transformation
- discuss transformation
- discuss usage of MM probes
- discuss diagnosis
- discuss detection of bad arrays
- discuss reporting partial hybridization results
- discuss limitations of SUB-SUB normalization
- discuss future directions
- discuss advantages of SUB-SUB normalization
- conclude Example 1

### Example 2

- introduce microarray data sets
- describe Affymetrix HG-U133A data set
- describe Golden spike data set
- introduce perturbed data set
- apply PTR method to perturbed data set
- show results of PTR method on perturbed data set
- discuss variation reduction by PTR method
- compare PTR method with other normalization methods
- discuss improvement on detection of differentially expressed genes
- compute ROC curves
- compare PTR method with other pre-processing methods
- discuss results on HG-U133A data set
- discuss results on Golden spike data set
- discuss discussion
- discuss reference issue in pre-processing
- propose PTR method
- discuss advantages of PTR method
- discuss background correction issue
- discuss experiment design with replicates
- discuss reference and target selection
- discuss array quality evaluation
- conclude Example 2

