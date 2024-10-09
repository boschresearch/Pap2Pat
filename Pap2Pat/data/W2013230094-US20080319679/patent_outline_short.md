# DESCRIPTION

## FIELD OF THE INVENTION

- define field

## BACKGROUND OF THE INVENTION

- describe microarray technology
- discuss limitations of current methods

## SUMMARY OF THE INVENTION

- summarize invention

## DETAILED DESCRIPTION

- introduce normalization problem in microarray analysis

### Overview

- motivate normalization as comparing apples to apples
- introduce blind inversion approach to normalization

### Statistical Principle of Normalization

- formulate normalization as blind inversion problem

### Differentiation Fraction and Undifferentiated Probe Set

- consider mixture distribution of input variables

### Spatial Pattern and Sub-arrays

- propose stratification strategy for normalization

### Parameterization

- parameterize function g by simple linear function

### Simple Least Trimmed Squares

- adopt LTS to solve problem

### Multiple Arrays and Multiple References

- discuss strategy of normalization for multiple arrays

### The Probe-Treatment-Reference (PTR) Summarization Model

- propose PTR method for normalization and summarization
- describe PTR model and its implementation

### Least Absolute Deviations (LAD) Estimation and its Computation

- describe LAD estimation and its computation

## EXEMPLARY EMBODIMENTS

- introduce microarray data analysis method
- motivate normalization using least trimmed squares regression
- describe subarray analysis and normalization
- outline computer system implementation

## EXAMPLES

### Example 1

- introduce microarray data
- implement SUB-SUB normalization
- select parameters for SUB-SUB normalization
- apply SUB-SUB normalization to Affymetrix Spike-in dataset
- apply SUB-SUB normalization to Primate Brain Expression dataset
- reduce variation by sub-array normalization
- discuss external controls and transformation

### Example 2

- introduce microarray data sets
- analyze perturbed data set
- reduce variation by PTR method
- improve detection of differentially expressed genes
- discuss PTR method

