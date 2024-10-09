# DESCRIPTION

## TECHNICAL FIELD

- describe system and process for identifying and characterizing double-stranded DNA break repair sites

## BACKGROUND

- introduce CRISPR proteins and their function
- describe DNA DSBs and repair process
- discuss limitations of current methods
- motivate need for improved method
- summarize current state of the art

## SUMMARY

- introduce computer implemented process for identifying and characterizing double-stranded DNA break repair sites
- describe receiving sample sequence data
- analyze and merge sample sequence data
- develop target-site sequences
- bin merged sequences with target-site sequences
- re-align binned target-read alignments
- analyze final alignment and identify mutations
- output final alignment, analysis, and quantification results
- describe various aspects of the process

## DETAILED DESCRIPTION

- introduce CRISPAltRations analytical pipeline
- describe building merged R1/R2 consensus
- build target site reference
- optionally build target with expected outcome of HDR event
- align merged sequence reads to target reference sequences
- re-align reads using modified Smith-Waterman aligner
- characterize and quantify variants
- summarize results in tables and graphs
- describe improvements over prior methods
- describe use of minimap2
- describe constructing expected outcome of HDR event
- describe modified Needleman-Wunsch algorithm
- describe position-specific gap open and extension penalties
- describe collecting indels nearby nuclease cut site
- describe graphical visualization of allelic variation
- describe comparing predicted repair event to observed repair
- describe determining molecular pathways involved in repair
- describe utility of system and methods
- describe generating synthetic set of gRNA:amplicon pairs
- describe analyzing synthetic data using CRISPRAltRations system
- describe comparing results to CRISPResso1 and CRISPResso2 tools
- describe improved accuracy of CRISPRAltRations system
- describe another embodiment of computer implemented process
- describe receiving sample sequence data
- align sequence data to predicted target sequence
- output alignment results as tables or graphics
- describe another embodiment of method for identifying and characterizing double-stranded DNA break repair sites
- extract genomic DNA from population of cells or tissue
- amplify genomic DNA using multiplex PCR
- sequence amplicons and obtain sample sequence data
- execute on processor steps of receiving sample sequence data
- describe various arrangements of components and processes
- describe modifications and adaptations to compositions, formulations, methods, processes, and applications

### Computer Code

- provide exemplary code used to generate 1D scoring matrix for gap open bonus during alignment using psnw

