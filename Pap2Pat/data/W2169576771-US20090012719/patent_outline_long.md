# DESCRIPTION

## BACKGROUND

- introduce gene expression analysis
- limitations of traditional gene selection
- need for cooperative gene analysis

## SUMMARY

- introduce cooperative interaction analysis
- select factors from continuous measurements
- identify jointly associated factors
- analyze cooperative interactions
- apply to gene expression data
- identify high synergy genes
- model cooperative interactions
- describe system for gene selection
- describe system for factor selection

## DETAILED DESCRIPTION

- introduce method for selecting factors from continuous data set
- identify factors cooperatively associated with outcome
- analyze factors for cooperative interactions
- apply to various data sets, including biological and financial data
- describe limitations of previous techniques, such as discretization
- introduce continuous expression data
- define factors and outcomes
- describe measurements, including values of factors and outcomes
- identify two or more factors jointly associated with outcome
- analyze each factor for cooperative interactions
- introduce module of factors
- model cooperative interaction using Boolean function
- estimate uncertainty of predicting disease
- define cluster of samples
- calculate entropy of cluster
- define partition of full set of samples
- calculate entropy of partition
- introduce UPGMA clustering algorithm
- evaluate conditional entropy and synergy of two genes
- generalize UPGMA to more than two factors
- describe issues with discontinuity in UPGMA
- introduce measure of conditional entropy that averages H
- describe Chebyshev distance measure
- evaluate synergy according to technique
- introduce one-step evaluation approach
- evaluate H(C|G1, G2) in two-gene case
- estimate H(C|G1) and H(C|G2) in two-gene case
- generalize one-step evaluation approach to n factors
- describe second method of one-step evaluation approach
- assign cluster membership values in non-uniform way
- evaluate entropy H(C|G) for particular gene G
- identify module(s) or sub-module(s) of genes
- use module(s) or sub-module(s) to predict outcome
- identify smallest cooperative module of genes
- implement techniques using software
- describe system for identifying synergy among multiple factors
- illustrate embodiment of system
- identify synergy among multiple interacting factors
- provide example of disclosed subject matter
- obtain publicly available prostate cancer expression data
- rank genes in terms of conditional entropy H(C|Gi)
- identify genes individually most correlated with cancer
- rank gene pairs in terms of synergy I(Gi, Gj; C)
- identify genes producing highest synergy
- show scatter plot of gene expression data
- show corresponding dendrogram
- note high synergy reflected in scatter plot
- discuss choice of D* value
- estimate sensitivity to choice of D* value

