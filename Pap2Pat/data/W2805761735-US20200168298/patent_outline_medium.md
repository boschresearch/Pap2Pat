# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- motivate genetic testing
- describe limitations of current genotyping methods
- highlight challenges in analyzing HTS data
- introduce ADME genes

## SUMMARY

- summarize method for genotyping
- describe aligning target sample reads
- identify nucleic acid sequence variants
- detect structural variants
- identify gene-disrupting mutations
- call genotype

## DETAILED DESCRIPTION

- introduce tool and methods for allelic decomposition of genes
- describe limitations of existing structural variation discovery tools
- motivate need for new tool and methods
- introduce PGRNseq capture protocol
- describe advantages of PGRNseq over WGS and WES
- highlight challenges in genotyping ADME genes
- introduce CYP2D6 as example of difficult gene to analyze
- describe limitations of existing CYP2D6 genotyping tools
- introduce star-allele nomenclature
- define gene-disrupting and neutral mutations
- describe major and minor star-alleles
- outline steps for genotyping: read alignment, mutation detection, copy number and structural variation estimation, major star-allele identification, genotype refinement, and genotype
- describe primary input: HTS data and gene information databases
- outline steps for genotyping 200: receiving HTS data, aligning reads, determining alignment acceptability, calling genotype, and optional genotype refinement
- describe genotype refinement step
- outline steps for genotyping 200' (alternative embodiment)
- describe application to ADME genes
- highlight broad applicability of tool and methods
- describe reconstructing sequence content of gene copies
- define star-allele identification
- outline steps for inferring new star-alleles
- describe use of databases to guide star-allele discovery
- highlight ability to handle gene duplications, fusions, and genomic deletions

### CYP2D6

- introduce CYP2D6 gene
- application of genotyping

### HTS Data

- receive HTS sequencing data for ADME genes
- generate HTS sequencing data using PGRNseq protocol or WGS

### Alignment/Read Mapping

- align HTS data to reference genome allele database
- perform read mapping using various algorithms (e.g. BWA, Bowtie 2)
- perform local indel realignment
- achieve acceptable alignment relative to star-alleles

### Sequence Variant Calling

- identify nucleic acid variants by deviations in sequence relative to reference genome
- call variants using algorithms (e.g. FreeBayes, MuTect2)

### Detecting Structural Variants

- detect structural variants in ADME genes
- estimate gene copy number for regions of the gene
- determine observed coverage for each region
- identify optimal gene arrangement
- detect structural rearrangements
- consider gene duplications and deletions
- consider partial gene deletions and duplications
- estimate copy number of each exon and intron

### Coverage Normalization

- motivate non-uniform coverage
- introduce reference sample
- calculate sum of coverage depth
- rescale function Bs
- estimate η
- determine copy number status
- illustrate examples of PGRNseq coverage normalization

### Major Star-Allele Identification

- introduce goal of genotyping
- obtain sets of gene-disrupting mutations
- filter out alleles
- formulate MSAIP
- solve MSAIP

### Genotype Refining

- motivate genotype refining
- introduce GRP
- define minor star-alleles
- formulate GRP objective
- add constraints
- solve GRP

## Complexity

- NP-hardness of CNEP and MSAIP

## Systems

- introduce genotype predictor system
- describe system components
- illustrate system architecture
- detail sample generator
- detail sequencer
- detail databases
- detail sequence analyzer
- detail system controller
- detail user interface
- describe sequence aligner
- describe sequence variant identifier
- describe structural variant identifier
- describe gene-disrupting mutation identifier
- describe star-allele identifier
- describe genotype caller

## Examples

- introduce data sets
- describe genotyping methods performance

### DISCUSSION

- summarize genotyping results
- discuss discrepancies with validated genotypes
- motivate advantages over current genotyping panels
- discuss copy number results
- validate predictions with external sources
- compare with other genotyping methods
- discuss computational overhead
- summarize performance on whole set of ADME genes
- discuss novel alleles detection
- motivate importance of accurate genotype interpretation
- conclude on the potential of HTS technologies in clinical settings

