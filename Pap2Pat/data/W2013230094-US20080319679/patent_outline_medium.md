# DESCRIPTION

## FIELD OF THE INVENTION

- define field

## BACKGROUND OF THE INVENTION

- introduce microarrays
- describe experiment steps
- discuss limitations of current methods
- motivate invention

## SUMMARY OF THE INVENTION

- summarize method
- summarize system

## DETAILED DESCRIPTION

- introduce normalization problem in microarray analysis

### Overview

- motivate normalization
- describe existing methods
- introduce blind inversion approach
- propose new approach using least trimmed squares algorithm
- highlight advantages of new approach

### Statistical Principle of Normalization

- formulate normalization as blind inversion problem
- derive statistical principle of normalization
- propose estimation method

### Differentiation Fraction and Undifferentiated Probe Set

- consider more complicated situation with differentially expressed genes

### Spatial Pattern and Sub-arrays

- propose stratification strategy for normalization

### Parameterization

- parameterize function g by simple linear function

### Simple Least Trimmed Squares

- adopt LTS to solve problem

### Multiple Arrays and Multiple References

- discuss strategy for normalization with multiple arrays and references

### The Probe-Treatment-Reference (PTR) Summarization Model

- propose PTR model for summarization
- describe model formulation
- discuss advantages of PTR model
- propose LAD estimation method
- describe computation of LAD estimation

### Least Absolute Deviations (LAD) Estimation and its Computation

- formulate LAD problem
- propose median polish approach
- discuss iteration process

## EXEMPLARY EMBODIMENTS

- introduce method of analyzing microarray data
- define microarray
- motivate normalization using regressional analysis
- describe normalization using least trimmed squares regression
- outline method for analyzing microarray data using subarrays
- describe method for obtaining expression profiles from microarray experiments
- outline method for detecting defective areas on a microarray
- describe computer systems and implementations for practicing the methods

## EXAMPLES

### Example 1

- introduce microarray data
- describe Affymetrix Spike-in dataset
- implement SUB-SUB normalization
- select parameters for SUB-SUB normalization
- investigate spatial pattern in HGU95 chip
- apply SUB-SUB normalization to eight arrays
- test trimming fraction in LTS
- analyze primate brain expression dataset
- compare SUB-SUB with quantile normalization
- reduce variation by sub-array normalization
- discuss external RNA controls
- mention cases with large fractions of differentially expressed genes
- compare nonlinear array transformation with linear sub-array transformation
- discuss transformation and variance stabilization
- diagnose bad arrays

### Example 2

- introduce microarray data sets
- analyze perturbed data set
- compare normalization methods
- test PTR method with different references
- reduce variation by PTR method
- compare PTR with other pre-processing methods
- improve detection of differentially expressed genes
- discuss reference issue in pre-processing
- propose PTR method for normalization and summarization
- discuss experiment design with replicates
- discuss background correction issue

