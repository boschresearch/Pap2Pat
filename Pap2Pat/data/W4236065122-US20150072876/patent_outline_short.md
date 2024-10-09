# DESCRIPTION

## CONTINUITY INFORMATION

- claim priority

## BACKGROUND

- motivate cell-type separation

## SUMMARY

- introduce blind separation approach

## DETAILED DESCRIPTION

- introduce algorithm for identifying cell-types in heterogeneous tissue samples

### Linear Model for Separation of Gene-Expression

- define linear model for separation of gene expression

### The Relation to Hyper Spectral Imaging

- relate gene-expression separation to nonnegative matrix factorization problems

### Algorithm

- outline three-part algorithm for estimating cell-type expression signatures and proportions
- describe initialization, evaluation, and estimation of matrices G and C

### Mining Purified Signatures

- discuss sourcing purified signatures from public repositories for algorithm input

### Example 1

- apply algorithm to controlled datasets
- describe liver-brain-lung dataset
- perform blind separation of liver-brain-lung dataset
- describe heart-brain dataset
- perform blind separation of heart-brain dataset
- describe T-B-Monocytes dataset
- perform blind separation of T-B-Monocytes dataset
- summarize results of blind separation on controlled datasets

### Example 2

- apply algorithm to semi-controlled prostate tumor dataset
- evaluate performance of algorithm on prostate tumor dataset

### Example 3

- demonstrate algorithm without cell-type determination
- show performance degradation without cell-type determination

### Example 4

- demonstrate algorithm without cell-type determination on T-B-Monocytes dataset

### Example 5

- introduce NNLS-based algorithm
- demonstrate algorithm without cell-type determination on liver-brain-lung dataset
- show performance degradation without cell-type determination
- highlight importance of cell-type determination step

## Discussion

- motivate gene-expression analysis
- limitations of existing separation methods
- introduce novel separation method
- demonstrate method's robustness and accuracy

## Example 7

### Application to Breast Cancer Microarrays

- apply separation algorithm to breast cancer microarrays

