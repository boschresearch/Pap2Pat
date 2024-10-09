# DESCRIPTION

## BACKGROUND

- motivate synthetic lethality analysis

## SUMMARY

- introduce synthetic lethality identification method
- describe biological network model framework
- outline method for predicting synthetic lethality
- detail normalizing network parameters
- describe training synthetic lethality model
- outline method for selecting cancer drug treatment
- describe filtering synthetic lethality pairs

## DETAILED DESCRIPTION

- introduce method for identifying SL
- use biological network connectivity profiles
- translate parameters for comparison
- construct model on source species
- apply model to target species
- predict SL pairs in target species
- generate biological networks
- describe network parameters
- normalize network parameters
- train species-independent model
- apply model to normalized target networks
- predict SL pairs
- choose source species based on known SL information
- define connectivity homologous relationship
- represent connectivity profiles as vectors
- determine network parameters
- prune networks to contain one connected component
- normalize network parameters
- perform entropy analysis
- train models of synthetic lethality
- select SL and NSL pairs
- evaluate model performance

### EXAMPLE 1

- predict SL in S. pombe
- compare untranslated and normalized parameters
- evaluate model performance

### EXAMPLE 2

- predict SL in M. musculus

### EXAMPLE 3

- apply SL model to human network parameters
- generate score for human gene pairs
- compile database of severe, tolerated, homozygous, deleterious co-mutations
- evaluate all gene pairs
- filter false positives
- determine false discovery rate
- show putative synthetic lethal pairs in same pathway
- analyze protein complexes
- plot scores of associated genes
- show enrichment for higher scores
- explore context-specific SL pairs
- identify tissue- and cell-line-specific lists of SL pairs
- filter SL pairs based on tissue expression
- compare SL prediction with Syn-Lethality database
- compare SL prediction with DAISY method
- select SL gene pairs involving genetic deficiency
- predict genes present in both DAISY and Syn-Lethality datasets
- analyze landscape of human synthetic lethality
- categorize predicted SL gene pairs using biological pathway data
- present network diagram of SL pairs
- analyze function-specific mechanisms of synthetic lethality
- annotate putative SL gene pairs for mechanisms
- identify enrichments for particular mechanisms of SL
- identify novel cancer therapies using putative synthetic lethal pairs
- illustrate application of disclosed subject matter in cancer treatment

