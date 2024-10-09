# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- motivate genetic testing
- describe limitations of current genotyping methods

## SUMMARY

- summarize method for genotyping
- describe application of method
- outline system for genotyping

## DETAILED DESCRIPTION

- introduce HTS data analysis for allelic decomposition of genes
- describe limitations of existing structural variation discovery tools
- motivate need for new tool to genotype ADME genes based on PGRNseq and Illumina WGS data
- describe PGRNseq capture protocol and its advantages
- introduce star-allele nomenclature in pharmacogenomics
- define gene-disrupting and neutral mutations
- outline steps for genotyping, including read alignment, mutation detection, copy number estimation, and genotype refinement
- describe database structure for storing gene information and known star-alleles
- detail genotype refining step, including ranking possible solutions and identifying best scoring genotype
- illustrate genotyping method with FIG. 2A and FIG. 2B
- conclude with applicability of tool and methods to any gene or group of genes

### CYP2D6

- introduce CYP2D6 and its significance

### HTS Data

- receive HTS sequencing data for ADME genes

### Alignment/Read Mapping

- align HTS data to reference genome allele database
- perform local indel realignment and identify acceptable alignment

### Sequence Variant Calling

- identify nucleic acid variants by deviations in sequence relative to reference genome

### Detecting Structural Variants

- estimate gene copy number for regions of gene
- determine observed coverage for each region
- identify optimal gene arrangement by minimal difference between observed coverage and known possible gene arrangements
- detect structural rearrangement when optimal gene arrangement differs from reference genome arrangement

### Coverage Normalization

- motivate non-uniform coverage in PGRNseq platform
- describe method for characterizing depth of coverage
- illustrate examples of PGRNseq coverage rescaling

### Major Star-Allele Identification

- describe goal of genotyping and detection of major star-alleles
- formulate Major Star-Allele Identification Problem (MSAIP)

### Genotype Refining

- motivate need for genotype refining
- formulate Genotype Refining Problem (GRP)
- describe objective of GRP and its solution

## Complexity

- NP-hardness of CNEP and MSAIP

## Systems

- introduce genotype predictor system
- describe system components
- illustrate sample analyzer
- detail system controller and user interface
- describe modules for sequence alignment and variant identification
- outline genotype caller and refiner
- discuss system operation and output

## Examples

- present examples of genotyping tool and methods

### DISCUSSION

- discuss performance of ADME genotyping methods
- compare with existing genotyping panels
- highlight advantages of present methods
- discuss novel alleles detected by present methods
- conclude on the significance of present methods

