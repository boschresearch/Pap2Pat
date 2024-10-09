# DESCRIPTION

## GOVERNMENT FUNDING

- disclose government funding

## BACKGROUND

- introduce cellular differentiation
- describe limitations of single cell RNA sequencing

## SUMMARY

- motivate molecular definition of differentiation
- introduce Etv2-EYFP transgenic embryos
- describe single cell transcriptome analyses
- introduce concept of metagene entropy
- describe analysis software 'dpath'
- outline machine readable medium with instructions
- describe decomposing expression profile matrix
- outline prioritizing genes for progenitor and committed states
- describe ranking cells with respect to specific cellular states

## DETAILED DESCRIPTION

### Definitions

- define terminology
- explain articles "a" and "an"
- define "about"
- define "cells"
- explain stem cell types
- define "self-renewal" and "expansion"

### ASPECTS OF THE INVENTION

- introduce Etv2 and its role in development
- describe Etv2 mutants and overexpression
- explain Etv2 expression during embryogenesis
- describe single-cell RNA-seq analysis
- introduce mathematical solutions to dropout events
- describe weighted Poisson non-negative matrix factorization (wp-NMF)
- introduce metagene entropy and self-organizing map (SOM)
- describe random walk with restart (RWR) algorithm
- explain dpath program and its functionality
- describe comparison with other factorization methods
- illustrate system 600 block diagram
- describe processor 620 functionality
- explain input 630 and output 640
- illustrate system 600 operation
- describe machine 700 block diagram
- explain hardware processor 702
- describe main memory 704 and static memory 706
- explain mass storage 716 and signal generation device 718
- describe network interface device 720 and sensors 721
- explain output controller 728
- describe machine readable medium 722
- explain instructions 724
- describe communications network 726
- illustrate method 800 flow chart
- describe decomposing expression profile matrix
- map cells into metacells using SOM
- prioritize cells using RWR algorithm
- rank genes for cellular states
- illustrate method 900 flow chart
- receive single cell RNA-seq
- model expected gene expression level
- determine metagene entropy

### Materials and Methods

- isolate cells from embryos
- screen for EYFP expression
- dissociate cells with TrypLE Express
- sort cells by FACS
- load cells onto Fluidigm 10-17 um integrated fluidics circuit
- capture, viability screen, lyse, and amplify libraries
- sequence libraries using MiSeq
- filter out low-quality reads
- estimate transcripts per million (TPM)
- fit noise model to TPM data
- remove genes with high technical noise
- remove ubiquitously expressed genes
- define weighted Poisson non-negative matrix factorization (wp-NMF) model
- derive objective function for wp-NMF
- optimize wp-NMF using gradient ascent method
- initialize U and V using weighted NMF
- define metagene entropy
- choose size of metagene K
- evaluate performance of factorization methods
- train linear support vector machine classifiers
- compute LOO-CV error
- compute WSS/TSS ratio
- cluster cells into metacells using SOM
- partition SOM using PAM
- construct heterogeneous metagene-metacell graph
- prioritize metacells with respect to cellular states

### Data Availability

- deposit single cell RNA-seq data in NCBI Sequence Read Archive (SRA) database

### Results

- introduce dpath pipeline
- decompose expression profile matrix using wp-NMF
- define metagene basis and coefficients
- verify biological relevance of metagenes
- identify metagene signatures for endothelium, blood, and endocardium
- compare wp-NMF with other factorization tools
- introduce metagene entropy concept
- apply metagene entropy to predict differentiation state
- establish metacell landscape using SOM algorithm
- visualize lineage structures on 2D map
- identify cell clusters using PAM algorithm
- characterize cell clusters based on metagene expression
- identify T+ cells as most immature progenitors
- analyze gene expression profiles of T+ cells
- identify Sox7 and Runx1 as progenitor markers
- analyze gene expression profiles of haematopoietic and endothelial lineages
- identify endocardial/cardiac mesodermal genes
- analyze expression of Cgnl1 and Dok4 in C2 population
- verify predictions from metacell landscape
- identify endocardial cushion progenitors
- analyze gene profile changes between C2 and C1
- confirm existence of C2 population using immunohistochemistry
- identify two waves of haematopoiesis
- analyze gene expression profiles of C5, C6, and C7
- identify Runx1 and Gata1 as haematopoietic markers
- analyze gene expression profiles of C4
- identify C4 as haemogenic endothelial lineage
- analyze endothelial differentiation
- identify pathways for haematoendothelial bifurcation
- identify upregulated genes in progenitor clusters
- enrich KEGG pathways in upregulated genes
- identify SHH pathway as key regulator
- verify role of SHH pathway in haemato-endothelial differentiation
- analyze effects of SHH agonist and antagonist
- discover trajectory from progenitor to committed state
- build heterogeneous metacell-metagene probability graph
- apply RWR algorithm to infer progenitor and committed states
- determine developmental trajectories on SOM
- verify biological relevance of inferred progenitor and committed states
- analyze gene expression profiles along developmental trajectories
- compare dpath with other pseudotime inference algorithms
- evaluate accuracy of inferred pseudotime

### DISCUSSION

- introduce dpath pipeline for single-cell RNA-seq data analysis
- describe three major technical breakthroughs
- motivate wp-NMF for matrix decomposition
- explain advantages of NMF over PCA
- define metagene entropy as a measure of cellular plasticity
- compare dpath with conventional programs
- describe 2D SOM for visualizing cellular states
- explain flexibility of modelling lineage hierarchies
- introduce subpopulation of Etv2-expressing cells for analysis
- describe high entropy progenitor cells of haematopoietic and endothelial lineages
- discuss signals specifying cell fate during gastrulation
- identify dynamic expression pattern of SHH signalling pathway
- summarize significance of dpath pipeline
- conclude with potential applications of dpath pipeline

