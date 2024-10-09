# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- introduce genetic testing
- describe high throughput sequencing
- discuss challenges in analyzing sequencing data
- describe limitations of current computational tools
- discuss importance of genotyping ADME genes
- describe existing array-based genotyping assays
- introduce targeted genotyping platforms
- discuss algorithmic challenges in ADME genotyping

## SUMMARY

- introduce methods and systems for genotyping
- describe receiving high throughput sequencing data
- align target sample reads to reference genome
- identify nucleic acid sequence variants
- detect structural variants
- identify gene-disrupting mutations
- select reference star alleles
- call genotype associated with selected star-allele
- refine genotype for multiple star-alleles
- describe genotyping ADME genes
- describe repeating method for multiple genes
- describe types of high throughput data
- describe system for predicting genotype

## DETAILED DESCRIPTION

- introduce tool and methods for allelic decomposition of genes
- describe limitations of existing structural variation discovery tools
- motivate need for new tool and methods
- introduce PGRNseq capture protocol
- describe advantages of PGRNseq over WGS and WES
- highlight challenges in genotyping ADME genes
- introduce CYP2D6 as example ADME gene
- describe limitations of existing CYP2D6 genotyping tools
- introduce star-allele nomenclature
- define gene-disrupting mutations
- define neutral mutations
- describe major star-alleles
- describe minor star-alleles
- outline steps for genotyping
- describe read alignment and mutation detection
- describe copy number and structural variation estimation
- describe major star-allele identification
- describe genotype refinement
- describe genotype calling
- introduce databases for gene information
- describe use of databases for star-allele discovery
- outline method for genotyping
- receive HTS data for gene from target sample
- align target sample reads to reference genome allele database
- determine whether alignment is acceptable for both alleles
- call genotype for each allele
- identify nucleic acid variants for each allele
- detect structural variants or lack thereof in each allele
- identify gene-disrupting mutations or lack thereof in each allele
- select set of reference star-alleles for each allele
- determine each allele of gene to have genotype associated with identified set of reference star-alleles
- describe genotype refining step
- rank each possible solution or identified star-allele
- identify one or more solutions with best ranking score as genotype for allele
- repeat method for each gene of interest
- perform one or more steps of method by suitably programmed computer
- genotype one or more genes of interest simultaneously
- describe FIG. 1
- describe FIG. 2A
- describe FIG. 2B
- introduce method for genotyping with acceptable alignment
- introduce method for genotyping without acceptable alignment
- describe reference-guided assembly of HTS data
- identify nucleic acid variants
- detect structural variants
- identify gene-disrupting mutations
- select set of reference star-alleles

### CYP2D6

- introduce CYP2D6 gene
- motivate genotyping of CYP2D6 and CYP2A6
- application of genotyping to other ADME genes
- flexibility of models and equations

### HTS Data

- receive HTS sequencing data
- generate HTS sequencing data
- align HTS sequencing data to reference genome allele database
- illustrate method of sequencing prior to analysis
- obtain reference genome allele database

### Alignment/Read Mapping

- align HTS data to each allele sequence of reference genome allele database
- map reads to reference genome
- perform local indel realignment
- select alignment algorithm
- perform reference-guided assembly
- achieve acceptable alignment
- identify nucleic acid variants
- use Genome Analysis Toolkit's Best Practices workflow
- confirm identified nucleic acid variants

### Sequence Variant Calling

- identify nucleic acid variants
- call nucleic acid variants
- use algorithms for calling nucleic acid variants
- confirm identified nucleic acid variants

### Detecting Structural Variants

- detect structural variants
- estimate gene copy number
- determine observed coverage
- identify optimal gene arrangement
- detect structural rearrangement
- obtain known possible gene arrangements
- use database for structural variant detection
- detect copy number variations
- detect gene deletions and duplications
- detect partial gene deletions and duplications
- define hybrid genes
- calculate aggregate copy number profile
- determine number of whole copies of genes
- determine number of copies of hybrid genes
- determine number of copies of structural variations
- estimate copy number of region
- solve Copy Number Estimation Problem

### Coverage Normalization

- introduce non-uniform coverage in PGRNseq platform
- analyze 96 samples to discover depth of coverage shape
- use reference sample to characterize depth of coverage
- calculate sum of coverage depth for both chromosomal copies
- rescale function Bs to obtain reference coverage depth function Rs
- estimate η using region q of stable copy number
- illustrate PGRNseq coverage rescaling in FIGS. 4A-4C
- consider copy number status of smaller gene regions
- define binary vector v to characterize rearrangement configurations
- illustrate examples of PGRNseq coverage normalization in FIGS. 5A-5C
- identify optimal gene arrangement by minimizing difference between observed and known arrangements
- define function cns to denote normalized copy number at loci
- define function mutcn to denote estimated copy number of mutation
- account for both autosomes present in the data sets
- normalize number of reads that include mutation by expected coverage of locus

### Major Star-Allele Identification

- obtain sets of gene-disrupting mutations and corresponding star-alleles
- detect major star-allele for each gene copy
- identify set M of all gene disrupting mutations detected in sample
- filter out major star-alleles with mutations not present in M
- define set A of remaining major star-alleles
- utilize non-negative integer variables p1, p2, pt to represent number of copies
- define Em to denote difference between estimated and observed copy numbers
- add constraint to ensure presence of gene-disrupting mutation implies genotype contains major star-allele
- select set of major star-alleles that most closely matches observed set M
- formulate/solve Major Star-Allele Identification Problem (MSAIP) as ILP

### Genotype Refining

- resolve ambiguity in major star-allele identification step
- use neutral mutations to distinguish major star-alleles
- formulate Genotype Refining Problem (GRP)
- input to GRP is set of major star-alleles inferred in MSAIP
- goal is to extend each major star-allele definition to minor star-allele definition
- define mut(a) to denote set of all mutations defining minor star-allele a
- introduce binary variable xa,b to indicate whether a is correct extension of b
- introduce binary variables ea,b,m and fa,b,m to model mutation presence
- minimize weighted difference between fa,b,m and ea,b,m
- assign each observed mutation m to one or more major star-alleles
- ensure each major star-allele associated with minor star-allele is assigned all gene-disrupting mutations
- ensure no variation is over-called
- solve GRP as QIP to obtain final genotype

## Complexity

- NP-hardness of CNEP and MSAIP

## Systems

- introduce genotype predictor system
- describe system components
- illustrate system architecture
- describe sample generator
- describe sequencer
- describe databases
- describe sequence analyzer
- describe I/O devices
- describe storage system
- describe system controller
- describe user interface
- describe sequence aligner
- describe sequence variant identifier
- describe structural variant identifier
- describe gene-disrupting mutation identifier
- describe star-allele identifier
- describe genotype caller
- describe genotype refiner
- describe system operation
- describe user interaction
- describe data analysis
- describe genotype report generation
- describe report display
- describe report delivery
- define module and system
- describe software and firmware
- describe processing unit configuration
- describe memory storage
- describe communication links
- describe network types
- describe system accessibility

## Examples

- introduce three data sets
- describe data set 1: 96 Coriell cell line samples
- describe data set 2: 137 cell line samples sequenced on PGRNseq v1 platform
- describe data set 3: samples from Platinum Genome project and 1000 Genome project
- summarize performance of genotyping methods on these data sets

### DISCUSSION

- summarize predictions by ADME genotyping methods
- discuss discrepancies between predictions and validated genotypes
- explain incorrect calls by TaqMan assays
- discuss case (4) with samples NA19834, NA19835, and NA19836
- explain limitations of TaqMan assays
- discuss case (2) with copy number results for *13-like fusion allele *76
- validate predictions by additional methods
- discuss case of NA10860 with *4 allele duplication
- cross-validate prediction by running on Illumina HiSeq X WGS NA10860 sample
- analyze coverage of CYP2D6 region
- discuss no Mendelian inconsistencies on PGRNseq data
- compare with previous PGRNseq data analysis
- summarize genotype predictions on Illumina WGS data
- validate genotype predictions with literature
- discuss predictions on CEPH 1463 family
- illustrate genotype predictions with FIG. 6
- summarize predictions for CYP2A6 genotype
- discuss low computational overhead of present methods
- compare performance with other available methods
- discuss superior performance of present methods on CYP2D6 gene
- summarize performance on whole set of 10 ADME genes
- discuss novel major star-alleles detected by present methods
- conclude with advantages of present methods

