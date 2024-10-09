# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce DNA analysis field
- describe limitations of DNA analysis
- discuss ancient DNA preservation
- explain low-coverage shotgun sequencing
- motivate need for new identification methods
- describe current identification methods
- discuss limitations of current methods
- introduce mitochondrial sequence analysis
- summarize need for new method

## BRIEF SUMMARY OF THE INVENTION

- introduce genotyping method
- describe obtaining DNA sequences
- calculate linkage disequilibrium scores
- prepare compilation of scores
- determine likelihood of single individual
- use uncharacterized genomic DNA
- determine whether sample contains DNA from multiple individuals
- select polymorphic sites
- use next-generation sequencing methods
- sequence genomic DNA
- calculate probabilities of linkages
- use hardware and software for method

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

### Overview

- introduce method for assessing consistency of two low-coverage libraries
- describe use of linkage disequilibrium information from reference panel
- mention robustness of method shown by coalescent simulations
- describe implementation using known, mapped SNPs
- provide source of SNP genotypes from 1000 Genomes Project
- define SNP genotyping
- describe importance of SNPs in genetic variation
- mention use of SNPs in HapMap project
- describe use of next-generation sequencing methods
- provide examples of NGS platforms
- describe shotgun sequencing
- mention use of random sequencing of samples
- describe comparison of DNA sequence using known patterns of linkage
- describe method for determining if two samples come from same or different people
- mention use of likelihood model to examine pairs of SNPs in linkage disequilibrium
- describe testing of method using simulated data and down-sampled high-coverage sequence data
- mention display of likelihood that a given sample originated from one individual or more than one individual

### DEFINITIONS

- define ranges
- define "about"
- define "linkage disequilibrium"
- define "polymorphic site" or "polymorphism"
- distinguish polymorphism from mutation
- define "single nucleotide polymorphism" or "SNP"
- define "SNP site"
- define "SNP sequence"
- describe length of SNP sequence
- define "library"
- describe preparation of genomic DNA library
- define "coverage"
- explain importance of coverage
- define "DNA sample"
- describe sources of DNA samples
- define "genotyping"
- define "VNTR"
- define "STR"
- define "first hypervariable region (HVI) and second hypervariable region (HVII)"
- describe uniqueness of human genome sequence
- define "massively parallel sequencing"
- describe next-generation sequencing (NGS)
- define "LOD score"

### General Methods and Materials

- describe problem of analyzing nucleic acid molecules in a sample
- introduce method for determining if two low-coverage libraries are consistent with originating from a single individual
- describe obtaining sequence information from known sequencing methods
- mention application of method to libraries made from extracts from several different samples

### Description of Analysis:

- introduce problem of autosomal genome analysis
- propose solution using pairs of neighboring SNPs
- define probability of observing two SNP alleles together
- derive formula 1A for probability of observing alleles from same individual
- derive formula 1B for probability of observing alleles from different individuals
- explain concept of linkage disequilibrium
- motivate use of reference panel of phased haplotypes
- describe approach to calculate log odds ratio for linked pairs of SNPs
- explain aggregation of LLRs for pairs of SNPs
- illustrate method schematically in FIG. 3
- describe application of method to sets of base observations
- explain within-sample comparisons
- explain between-sample comparisons
- describe selection of SNPs for analysis
- motivate use of SNPs with minor alleles at low to intermediate frequencies
- describe calculation of probability of observation under two models
- derive formula for log-likelihood ratio
- describe aggregation of log-likelihood ratios across genome
- introduce simulations to test method
- describe coalescent simulations
- describe construction of reference panels
- explain filtering of SNPs for reference panels
- summarize requirements for SNPs in reference panels

## EXAMPLES

### Example 1: Results from Simulations

- simulate single allele observations
- test method under demographic scenarios
- distinguish between same and different individuals
- simulate demographic model for humans
- test method on realistic demographic model
- discuss limitations of method

### Example 2: Results from Read Data

- obtain read data from Platinum Genomes
- sample reads to approximate coverage levels
- compare samples using SNP pairs
- discuss results of comparisons

## CONCLUSION

- conclude invention and scope of claims

