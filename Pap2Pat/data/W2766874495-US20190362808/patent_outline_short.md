# DESCRIPTION

## TECHNICAL FIELD

- relate to sequencing data processing and benchmarking

## BACKGROUND

- motivate somatic mutations in cancer
- limitations of current methods for detecting somatic variants

## BRIEF SUMMARY OF THE INVENTION

- introduce method for detecting somatic and germline variants
- receive aligned sequence data from tumor samples
- identify candidate variants and observe allelic fractions
- model copy number state estimates and tumor-cell fractions
- predict expected allelic fractions and determine variant status
- verify variant status using germline and somatic variant callers

## DETAILED DESCRIPTION

- define terms used in the invention
- describe background of somatic mutation detection
- motivate need for accurate somatic variant identification
- introduce Bayesian tumor-only somatic variant caller
- describe limitations of existing methods
- explain importance of considering private germline variants
- outline approach to reduce false positives due to private germline variants
- describe model of variant allele frequencies
- introduce LumosVar and LumosVarMulti embodiments
- outline advantages of multi-sample approach in LumosVarMulti
- describe features of LumosVarMulti, including subclonal event detection and spatial heterogeneity analysis
- highlight benefits of LumosVarMulti in detecting rare and non-coding variants

### EXAMPLES

- introduce nucleic acid isolation methods
- describe library preparation and sequencing
- outline software availability and requirements
- detail alignment and assembly pipeline
- explain in silico dilutions and downsampling
- summarize benchmark variant calling and filtering approaches
- introduce variant caller overview
- describe single-sample strategy
- describe multiple-sample strategy
- calculate position quality scores
- determine tumor quality metrics and filtering
- estimate copy number and clonal sample fraction
- model allelic copy number state and sample fractions
- determine allele frequencies
- estimate copy number and clonal sample fraction
- model somatic variant calling
- extend to multi-sample joint approach
- analyze dependence of private germline variation on ancestry
- extend analysis with additional exome sequenced tumor/normal sets
- summarize results of private variants by ancestry
- introduce framework for considering allele fraction shifts
- simulate single-sample approach for detecting somatic variants
- evaluate dataset for tumor only caller
- apply variant quality filtering
- evaluate somatic variant detection sensitivity and precision
- motivate LumosVar approach
- describe limitations of tumor-only sequencing
- introduce Bayesian calling strategy
- simulate multi-sample joint approach
- evaluate multi-sample joint approach
- apply multi-sample joint approach to archival samples
- compare results to standard somatic variant calling tools

