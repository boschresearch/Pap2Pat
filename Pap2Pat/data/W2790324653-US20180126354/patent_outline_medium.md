# DESCRIPTION

## INTRODUCTION

- introduce multiple myeloma
- describe genetic alterations
- discuss prognostic models
- motivate targeted sequencing

## SUMMARY

- introduce capture-based sequencing approach
- describe advantages over existing methods
- motivate personalized treatment plans
- design oligonucleotide probes
- select genes for sequencing
- describe platform design for discovery
- outline method for identifying variants
- detail sequencing library preparation
- describe hybridization and sequencing steps
- identify somatic mutations in multiple myeloma
- list genes mutated in multiple myeloma
- describe array or set of oligonucleotides for IgH locus
- describe array or set of oligonucleotides for MYC locus
- describe array or set of oligonucleotides for specific genes
- describe array or set of oligonucleotides for additional specific genes
- introduce DNA capture array
- describe array composition
- specify target genes
- list gene examples
- provide gene count variations
- describe probe tiling
- specify probe targets
- list additional gene examples

## DETAILED DESCRIPTION

- introduce DNA capture array
- define oligonucleotide probe
- describe method of identifying multiple myeloma mutations
- outline steps of sequencing library preparation
- describe hybridization and sequencing process
- identify variants in genomic DNA
- compare array to whole-exome sequencing
- describe advantages of array over I-FISH
- outline analysis of tumor mutations for prognosis and therapy
- describe gene expression profiling
- test mutual exclusivity/co-occurrence of multiple myeloma mutations
- perform integrative analysis

### DETAILED DESCRIPTION

- design custom capture sequencing platform
- describe probe set design for IGH and MYC loci
- outline capture sequencing of 95 tumor/normal pairs
- detail sequencing library preparation and hybridization
- describe sequencing data analysis and variant calling
- outline deep capture sequencing of 15 tumor/normal pairs
- calculate sequencing coverage and on-target efficiency
- describe capture sequencing-based copy number detection
- detail CopyCAT2 parameterization and gaussian mixture model
- outline CNV calling and filtering criteria
- detect CNVs using CopyCAT2
- annotate CNVs with amplifications, deletions, and genes
- detect translocations using LUMPY
- filter translocations using machine learning approach
- parse putative translocations involving IGH or MYC
- filter IGH translocations using SVM
- filter MYC translocations using manual decision boundary
- map IGH constant, switch, and enhancer regions
- identify switch regions using tandem repeats
- confirm switch regions using BLAT
- determine 3' enhancer region coordinates using BLAT
- validate novel t(14,22) translocation
- perform PCR on genomic DNA
- validate t(14;22) translocation
- validate t(13;14) translocation
- detect somatic single nucleotide variants
- compare initial capture and deep sequencing
- filter variants for biological importance
- downsample sequencing data
- compare capture and exome sequencing
- enrich for c-AID signature amongst IGLL5 mutations
- analyze mutual co-occurrence and mutual exclusivity
- perform IGLL5 survival analysis
- perform fluorescence in situ hybridization
- analyze RNA-seq expression data

## EXAMPLES

- illustrate design and application of oligonucleotide probe array for targeted sequence capture

### Example 1

- design oligonucleotide probes for MM-specific custom capture sequencing platform

### Example 2

- sequence 95 paired tumor and normal cell DNA samples using the platform

### Example 3

- identify copy number alterations with prognostic significance
- detect chromosome-level, arm-level, and focal CNVs
- identify deleterious mutations in genes including ATM, BRCA2, and CCND1

### Example 4

- detect IGH translocations using LUMPY and filtering strategy

### Example 5

- prioritize novel IGH translocations as potential driver mutations
- analyze complex translocation involving chromosomes 11, 13, and 14
- validate t(14,22) translocation using PCR
- identify overexpression of DERL3 in MM via IGH translocation

### Example 6

- detect intra- and inter-chromosomal MYC translocations using machine learning approach

### Example 7

- identify non-silent single nucleotide variants in all tumor samples

### Example 8

- determine whether MM is characterized by deeply subclonal variants of biological significance
- compare allele frequencies of variants discovered during original and subsequent deep sequencing

### Example 9

- facilitate integrative analysis across mutation types
- identify patterns of mutual exclusivity and co-occurrence within and across mutation types
- detect cross-mutation type exclusivity between CNVs and SNVs
- identify IGLL5 mutations associated with disease progression

