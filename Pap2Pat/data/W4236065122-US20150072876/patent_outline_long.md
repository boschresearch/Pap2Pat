# DESCRIPTION

## CONTINUITY INFORMATION

- claim priority

## BACKGROUND

- motivate gene-expression profiling
- limitations of current methods
- describe existing solutions
- summarize current approaches

## SUMMARY

- introduce novel approach
- summarize algorithm capabilities

## DETAILED DESCRIPTION

- introduce algorithm for identifying cell-types in heterogeneous tissue samples
- describe three parts of algorithm: non-negative matrix factorization, estimation of true number of cell-types, and computation of cell-type proportions
- explain limitations of algorithm, including requirement for purified reference signatures and potential ambiguities in results
- discuss importance of a priori knowledge of tissue composition and potential for algorithm to detect unknown cell-types

### Linear Model for Separation of Gene-Expression

- introduce linear model for separation of gene expression
- define mixed expression matrix M and separated cell-type specific gene-expression matrix G
- explain assumption of linearity and its limitations
- discuss requirement for a priori knowledge of number of cell-types and their identities
- introduce hypothesis-testing problem and objective of algorithm
- explain importance of purified gene-expression reference signatures

### The Relation to Hyper Spectral Imaging

- introduce nonnegative matrix factorization (NMF) problems
- define end-members matrix G and relative proportions matrix C
- explain equivalence of NMF problem to linear model for separation of gene-expression
- discuss adaptation of NMF algorithm for spectral analysis to gene-expression analysis
- explain importance of prior knowledge in NMF algorithm
- discuss extensions to Piper et al.'s algorithm for gene-expression analysis

### Algorithm

- introduce three major parts of algorithm: initialization, estimation of true number of cell-types, and computation of cell-type proportions
- describe initialization of matrices H and W
- explain evaluation of H and W using NMF
- define estimation of true number of cell-types kCT
- explain use of symmetric Kullback-Leibler divergence (SKLD) as distance measure
- discuss estimation of cell-type expression signatures matrix G
- explain computation of cell-type proportions matrix C using NNLS
- introduce majority voting to improve robustness of algorithm
- explain use of classes to group reference signatures
- discuss pseudo code of algorithm
- explain output of algorithm: matrices C and G

### Mining Purified Signatures

- explain importance of purified signatures for algorithm
- discuss sources of purified signatures, such as GEO
- explain how to choose signatures for input to algorithm
- discuss limitations of algorithm, including requirement for a priori knowledge of tissue composition
- explain how to set parameters for majority voting and classes

### Example 1

- introduce application of algorithm to controlled datasets
- describe liver-brain-lung dataset
- specify parameters for algorithm run
- describe microarray data
- introduce blind separation of liver-brain-lung dataset
- describe purified cell-type reference signatures
- show heatmap of gene-expression signatures
- describe algorithm's success in identifying cell-types
- show correlations between estimated and purified cell-types
- show SKLD distances between estimated and purified cell-types
- describe algorithm's success in estimating cell-type proportions
- show correlations between estimated and known cell-type proportions
- show SKLD distances between estimated and known cell-type proportions
- describe advancement of input signatures
- introduce blind separation of heart-brain dataset
- describe heart-brain dataset
- specify parameters for algorithm run
- describe microarray data
- describe purified cell-type reference signatures
- show heatmap of gene-expression signatures
- describe algorithm's success in identifying cell-types
- show correlations between estimated and purified cell-types
- show SKLD distances between estimated and purified cell-types
- describe algorithm's success in estimating cell-type proportions
- show correlations between estimated and known cell-type proportions
- show SKLD distances between estimated and known cell-type proportions
- describe advancement of input signatures
- introduce blind separation of T-B-Monocytes dataset
- describe T-B-Monocytes dataset
- specify parameters for algorithm run
- describe microarray data
- describe algorithm's success in identifying cell-types and estimating proportions

### Example 2

- introduce application of algorithm to semi-controlled dataset
- describe prostate tumor dataset
- specify parameters for algorithm run
- describe microarray data
- describe purified cell-type reference signatures
- show heatmap of gene-expression signatures
- describe algorithm's success in estimating cell-type proportions
- show correlations between estimated and known cell-type proportions
- discuss limitations of algorithm's performance

### Example 3

- run algorithm without cell-type determination
- show results of run using six input cell-types
- calculate correlations between gene-expression
- determine identity of resulting cell-types
- show estimated cell-type proportions
- calculate average absolute error per sample
- compare error to complete algorithm
- highlight real proportions and mistakenly assumed cell-types
- illustrate correlations between gene-expression

### Example 4

- run algorithm without cell-type determination
- show results of run using six input cell-types
- calculate correlations between gene-expression
- determine identity of resulting cell-types
- show estimated cell-type proportions
- calculate average absolute error per sample

### Example 5

- run NNLS-based algorithm
- show results of run using six input cell-types
- calculate correlations between gene-expression
- determine identity of resulting cell-types
- show estimated cell-type proportions
- calculate average absolute error per sample
- compare error to complete algorithm
- highlight real proportions and mistakenly assumed cell-types
- illustrate correlations between gene-expression
- show results of run using five input cell-types
- calculate correlations between gene-expression
- determine identity of resulting cell-types
- show estimated cell-type proportions
- calculate average absolute error per sample
- compare error to complete algorithm
- highlight real proportions and mistakenly assumed cell-types

## Discussion

- introduce gene-expression analysis
- limitations of whole tissue analysis
- importance of individual cell-type profiles
- difficulties of separating cell-types
- existing separation methods
- limitations of existing methods
- introduce new separation method
- advantages of new method
- test new method on controlled datasets
- test new method on semi-controlled dataset
- demonstrate robustness to varying input signatures
- compare to existing algorithms
- emphasize importance of cell-type determination
- summarize new method's capabilities
- highlight advantages for re-analyzing existing data
- conclude new method's usefulness

## Example 7

### Application to Breast Cancer Microarrays

- download and prepare heterogeneous tissues dataset
- collect and prepare reference signatures
- prepare input files for separation algorithm
- run separation algorithm and analyze output

