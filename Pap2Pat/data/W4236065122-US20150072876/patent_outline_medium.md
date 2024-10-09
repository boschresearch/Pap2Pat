# DESCRIPTION

## CONTINUITY INFORMATION

- claim priority

## BACKGROUND

- motivate cell-type separation
- limitations of existing methods

## SUMMARY

- introduce novel approach

## DETAILED DESCRIPTION

- introduce algorithm for identifying cell-types in heterogeneous tissue samples
- describe three parts of algorithm: non-negative matrix factorization, estimation of true number of cell-types, and computation of cell-type proportions

### Linear Model for Separation of Gene-Expression

- introduce linear model for separation of gene expression
- describe assumptions and limitations of linear model
- explain relation to nonnegative matrix factorization problems

### The Relation to Hyper Spectral Imaging

- introduce nonnegative matrix factorization problems
- describe application to hyper spectral imaging
- explain adaptation of NMF algorithm for gene-expression analysis

### Algorithm

- introduce initialization of algorithm
- describe evaluation of H and W matrices
- estimate true number of cell-types and cell-type expression signatures
- compute cell-type proportions matrix C
- describe majority voting and classes adjustments

### Mining Purified Signatures

- describe search for purified signatures in public repositories
- explain usage of classes and majority voting parameters

### Example 1

- introduce controlled datasets
- describe liver-brain-lung dataset
- specify algorithm parameters for liver-brain-lung dataset
- analyze blind separation of liver-brain-lung dataset
- show correlations between estimated and purified cell-types
- show correlations between estimated and known cell-type proportions
- describe heart-brain dataset
- specify algorithm parameters for heart-brain dataset
- analyze blind separation of heart-brain dataset
- show correlations between estimated and purified cell-types
- show correlations between estimated and known cell-type proportions
- describe T-B-Monocytes dataset
- specify algorithm parameters for T-B-Monocytes dataset
- analyze blind separation of T-B-Monocytes dataset
- show correlations between estimated and purified cell-types
- show correlations between estimated and known cell-type proportions

### Example 2

- introduce semi-controlled prostate tumor dataset
- specify algorithm parameters for prostate tumor dataset
- analyze blind separation of prostate tumor dataset
- show correlations between estimated and pathologist's cell-type proportions

### Example 3

- run algorithm without cell-type determination
- show results with six input cell-types
- show results with five input cell-types
- show results with four input cell-types

### Example 4

- run algorithm without cell-type determination
- show results with six input cell-types
- show results with five input cell-types

### Example 5

- introduce NNLS-based algorithm
- run algorithm with six input cell-types
- show results with six input cell-types
- run algorithm with five input cell-types
- show results with five input cell-types
- run algorithm with four input cell-types
- show results with four input cell-types
- compare errors with complete algorithm

## Discussion

- motivate gene-expression analysis
- limitations of existing separation methods
- introduce novel separation method
- describe advantages of novel method
- demonstrate method's accuracy
- show method's robustness to varying inputs
- compare method to existing algorithms
- summarize method's benefits

## Example 7

### Application to Breast Cancer Microarrays

- describe application of separation algorithm
- analyze algorithm output

