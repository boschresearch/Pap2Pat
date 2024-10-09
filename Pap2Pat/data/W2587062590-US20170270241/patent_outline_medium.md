# DESCRIPTION

## GOVERNMENT FUNDING

- disclose government funding

## BACKGROUND

- motivate cellular differentiation

## SUMMARY

- introduce single cell RNA sequencing
- describe Etv2-EYFP transgenic embryos
- summarize metagene entropy concept
- outline dpath software embodiment

## DETAILED DESCRIPTION

### Definitions

- define terminology
- explain usage of articles
- define specific terms

### ASPECTS OF THE INVENTION

- introduce Etv2 and its role in development
- describe Etv2 mutants and overexpression
- explain Etv2 expression during embryogenesis
- introduce single-cell RNA-seq analysis
- describe technical hurdles in single-cell RNA-seq
- introduce wp-NMF method to address dropout events
- describe need for additional biological information
- introduce metagene entropy and SOM algorithm
- describe RWR algorithm for prioritizing genes
- introduce dpath program and its capabilities
- describe comparison with other factorization methods
- illustrate system 600 for single-cell RNA-seq analysis
- describe components of system 600
- illustrate machine 700 for executing methodologies
- describe components of machine 700
- illustrate flow charts of methods 800 and 900

### Materials and Methods

- isolate cells from embryos
- sort cells using FACS
- perform single-cell RNA sequencing
- analyze sequencing data using TopHat and Cufflinks
- filter out low-quality genes
- define weighted Poisson non-negative matrix factorization model
- derive optimization problem for model
- solve optimization problem using gradient ascent method
- initialize U and V using weighted NMF
- evaluate performance of factorization methods
- cluster cells into metacells using SOM
- partition SOM using PAM
- construct heterogeneous metagene-metacell graph

### Data Availability

- provide data availability statement

### Results

- introduce dpath pipeline
- decompose expression profile matrix using wp-NMF
- motivate use of non-negativity constraints
- describe simulation study
- apply wp-NMF to Etv2-EYFP cells
- analyze metagene basis and coefficients
- verify biological relevance of metagenes
- identify metagene signatures for endothelium, blood, and endocardium
- compare performance of wp-NMF with other methods
- introduce concept of metagene entropy
- apply metagene entropy to Etv2+ cells
- establish metacell landscape using SOM algorithm
- analyze metacell landscape for Etv2 derivatives
- identify progenitor and committed cells using dpath
- verify predictions from metacell landscape
- identify endocardial cushion progenitors
- identify two waves of haematopoiesis
- analyze endothelial differentiation
- identify pathways for haematoendothelial bifurcation
- discover trajectory from progenitor to committed state
- verify biological relevance of inferred progenitor and committed states

### DISCUSSION

- introduce dpath pipeline for single-cell RNA-seq data analysis
- motivate technical breakthroughs in single-cell analysis
- describe wp-NMF for matrix decomposition
- explain metagene entropy for measuring cellular plasticity
- visualize cellular states on 2D SOM
- apply dpath to Etv2-expressing cells during murine embryogenesis
- summarize significance of dpath pipeline

