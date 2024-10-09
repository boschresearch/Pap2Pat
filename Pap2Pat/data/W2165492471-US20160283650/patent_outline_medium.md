# DESCRIPTION

## BACKGROUND

- motivate synthetic lethality analysis

## SUMMARY

- introduce synthetic lethality identification method
- describe method for predicting SL
- outline method for selecting cancer drug treatment

## DETAILED DESCRIPTION

- introduce method for identifying synthetic lethality
- describe flow chart of method
- motivate use of biological network connectivity profiles
- define connectivity homologous relationship
- represent connectivity profiles as vectors of network parameters
- describe protein-protein interaction networks
- normalize network parameters for interspecies comparison
- perform entropy analysis to verify parameter translation
- train models of synthetic lethality using logistic regression and random forests
- evaluate model performance using AUROC
- discuss limitations of network size and node popularity on prediction

### EXAMPLE 1

- predict synthetic lethality in S. pombe using rank normalization

### EXAMPLE 2

- predict synthetic lethality in M. musculus using trained model

### EXAMPLE 3

- apply SL model to human network parameters
- compile database of severe, tolerated, homozygous, deleterious co-mutations
- evaluate all gene pairs for SL scores
- filter false positives using score cutoff
- analyze putative SL pairs for pathway enrichment
- analyze protein complexes for SL enrichment
- explore context-specific SL pairs
- compare SL predictions to Syn-Lethality database and DAISY method
- analyze SL gene pairs involving genetic deficiency
- categorize predicted SL genes using biological pathway data
- analyze function-specific mechanisms of synthetic lethality
- identify putative SL pairs for novel cancer therapies

