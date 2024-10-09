# DESCRIPTION

## TECHNICAL FIELD

- relate to sequencing data processing and benchmarking

## BACKGROUND

- motivate somatic mutations in cancer
- describe limitations of current methods
- highlight importance of archival tissue collections
- discuss challenges of identifying somatic variants
- introduce need for new bioinformatics methods

## BRIEF SUMMARY OF THE INVENTION

- introduce method for detecting somatic and germline variants
- describe receiving aligned sequence data
- identify candidate variant
- observe allelic fraction
- model copy number state estimate and tumor-cell fraction
- predict expected allelic fraction
- determine somatic or germline status
- describe archival samples
- describe matched normal sample
- describe macro-dissecting
- describe variant types
- describe verification methods

## DETAILED DESCRIPTION

- define terms used in the invention
- describe scope of the invention
- introduce detection of variants in DNA sequencing data
- define subject or patient
- define sample
- define nucleic acid
- define gene
- define coding and non-coding sequences
- define allele
- define variant
- define mutation
- define deletion and insertion mutations
- define isolated nucleic acid
- define sequencing
- define next-generation sequencing
- define genotype and phenotype
- define genome
- define chromosome
- define heterozygous and homozygous
- define exome
- define library
- define allelic fractions
- define tumor-cell fraction
- describe challenges in identifying somatic variants
- introduce Bayesian tumor-only somatic variant caller

### EXAMPLES

- introduce ethics approval and consent
- describe patient and sample information
- outline nucleic acid isolation methods
- detail DNA isolation from FFPE tissue
- describe DNA isolation from fresh frozen tissue
- outline DNA isolation from blood germline tissue
- describe RNA purification from FFPE tissue
- outline library preparation and sequencing
- describe software availability and requirements
- detail alignment and assembly pipeline
- outline in silico dilutions and downsampling
- describe benchmark variant calling and filtering
- introduce variant caller overview
- describe single-sample strategy
- describe multiple-sample strategy
- calculate position quality scores
- determine posterior probability of unreliable positions
- calculate tumor quality metrics and filtering
- train quadratic discriminant model
- determine posterior probability of trusted training group
- estimate copy number and clonal sample fraction
- model allele-specific copy number and sample fractions
- optimize clonal and subclonal sample fractions
- calculate likelihood of exon read depth
- calculate likelihood of heterozygous variant B allele read depth
- calculate likelihood of somatic variant B allele read depth
- describe prior distribution of f
- determine allele frequencies
- find most likely clone
- estimate copy number and clonal sample fraction
- model multiple samples and determine number of clonal variant groups
- calculate likelihood of detecting heterozygous variants
- calculate likelihood of detecting somatic variants
- determine optimal number of clonal variant groups
- call somatic variants in single-sample approach
- call somatic variants in multi-sample joint approach
- examine dependence of private germline variation on ancestry
- extend analysis with additional exome sequenced tumor/normal sets
- obtain high quality variant calls using strict thresholds
- limit to single nucleotide variants with defined impact on protein transcription or translation
- overlay ancestry by PCA on common coding variants
- summarize results in FIGS. 10B and 10C
- motivate using tumor only sequencing in precision medicine
- introduce framework for considering allele fraction shifts
- model allelic copy number and clonal sample fractions
- simulate single-sample approach
- evaluate dataset using tumor only caller
- perform variant quality filtering
- determine sample fraction and copy number calling
- evaluate somatic variant detection sensitivity
- evaluate somatic variant detection precision
- introduce LumosVar approach
- motivate tumor-only sequencing
- discuss limitations of tumor-only sequencing
- describe Bayesian calling strategy
- discuss importance of mutational burden
- compare LumosVar to database filtering
- describe LumosVar's capabilities
- introduce multi-sample joint approach
- simulate multi-sample joint approach
- evaluate multi-sample joint approach
- apply multi-sample joint approach to GBM samples
- apply multi-sample joint approach to breast and prostate samples
- compare joint approach to single-sample approach
- summarize results and benefits of LumosVarMulti

