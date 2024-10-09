# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce DNA analysis field
- describe limitations of DNA analysis
- discuss prior art in DNA analysis
- motivate need for new method

## BRIEF SUMMARY OF THE INVENTION

- introduce genotyping method
- describe obtaining DNA sequences
- calculate linkage disequilibrium scores
- prepare compilation of scores
- determine likelihood of single individual
- discuss various aspects of the method

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

### Overview

- introduce method for assessing consistency of two low-coverage libraries
- describe use of linkage disequilibrium information from reference panel
- mention robustness testing using coalescent simulations
- describe use of known, mapped SNPs
- introduce SNP genotyping and its applications
- describe next-generation sequencing methods
- introduce shotgun sequencing and its applications
- outline method for determining if two samples come from same or different people

### DEFINITIONS

- define ranges
- define "about"
- define linkage disequilibrium
- define polymorphic site or polymorphism
- distinguish polymorphism from mutation
- define single nucleotide polymorphism (SNP)
- define SNP site
- define SNP sequence
- define library
- define coverage
- define genotyping and related terms

### General Methods and Materials

- introduce method for analyzing nucleic acid molecules in a sample
- outline application of method to forensic situations

### Description of Analysis:

- introduce method using pairs of observations of neighboring SNPs
- derive probability formulas for observing two SNP alleles together
- explain linkage disequilibrium and its application
- describe approach using reference panel of phased haplotypes
- calculate log-likelihood ratio for linked pairs of SNPs
- aggregate LLRs for pairs of SNPs using sliding windows
- illustrate method schematically in FIG. 3
- apply method to sets of base observations within and between samples
- select informative SNPs for analysis
- perform coalescent simulations to test method
- construct reference panels using 1000 Genomes Project Phase 1 data set

## EXAMPLES

### Example 1: Results from Simulations

- simulate single allele observations
- test method under various demographic scenarios
- analyze results under different population models

### Example 2: Results from Read Data

- obtain read data from European male and female
- analyze read data at different coverage levels

## CONCLUSION

- summarize invention and scope

