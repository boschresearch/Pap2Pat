# DESCRIPTION

## FEDERAL FUNDING ACKNOWLEDGEMENT

- acknowledge government funding

## FIELD OF THE INVENTION

- introduce genomic DNA methylation loss

## BACKGROUND

- describe hypomethylation in cancer
- discuss conflicting evidence on PMD hypomethylation

## SUMMARY OF THE INVENTION

- introduce WGBS experiments
- identify local sequence signature
- determine PMD hypomethylation
- analyze CpGs in Solo-WCGW motif
- reveal PMD hypomethylation in healthy tissues
- show increase in PMD hypomethylation with age
- correlate PMD hypomethylation with somatic mutation density
- correlate PMD hypomethylation with cell-cycle gene expression
- provide method for determining replication-associated DNA methylation loss
- identify Solo-WCGW motif sequences
- determine mean CpG dinucleotide methylation value
- exclude non-intergenic Solo-WCGW motif sequences
- exclude H3K36me3 histone marked Solo-WCGW motif sequences
- define PMDs by late replication timing and nuclear lamina localization
- define PMDs by Hi-C-defined heterochromatic compartment B
- assess SD of solo-WCGW PMD hypomethylation
- identify common PMDs shared between cell or tissue types
- identify cell-type invariant PMDs
- identify cell-type specific PMDs
- reflect chronological age of cell or tissue sample

## DETAILED DESCRIPTION OF THE INVENTION

- identify four distinct features influencing DNA methylation levels
- describe the collective shaping of PMD/HMD structure
- show local sequence features influencing DNA methylation loss
- describe the role of DNMT1 in DNA methylation maintenance
- motivate the study of the WCGW motif
- describe the Solo-WCGW signature and its application
- identify replication timing as a major determinant of methylation levels
- propose a re-methylation window model
- describe the role of H3K36me3 in overriding replication-associated methylation loss
- discuss the relationship between PMD hypomethylation and LINE-1 insertions
- describe the effect of PMD hypomethylation on CpG to TpG mutation rates
- introduce the Solo-WCGW sequence motif for measuring genomic DNA methylation loss
- describe the definition and use of shared PMDs and HMDs
- show the consistency of PMD/HMD structure across tumor and normal samples
- describe the application of solo-WCGW CpGs in low-coverage WGBS studies
- show that most PMDs are shared across cancer and normal tissues
- describe the data showing that most PMDs are shared across developmental lineages
- describe the emergence of PMD hypomethylation during embryonic development
- show the association between PMD hypomethylation and chronological age
- describe the link between PMD hypomethylation and mitotic cell division in cancer
- show the effect of replication timing and H3K36me3 on methylation
- describe the materials and methods used in the work
- describe additional working examples and applications

### Terms (Definitions)

- define technical terms
- explain singular forms
- describe ranges and approximations
- define "optional" and "optionally"
- explain "comprise" and variations
- define "exemplary"
- describe "such as" usage
- explain range expressions
- define "first," "second," etc.
- describe "WCGW" sequence
- define "solo-WCGW" motif
- explain n(x)WCpGWn(x) genomic DNA sequence motif
- define "condition or state" of a cell or tissue
- explain "effective cell division" and "determining the number of effective cell divisions"
- define "mitotic clock"
- define terms
- describe method for developing mitotic clock
- motivate use of data processing apparatus
- describe implementation of subject matter
- describe computer program
- describe processes and logic flows
- describe processors and computer readable media
- describe interaction with user
- describe computing system
- provide genomic data
- provide exemplary probes and motif sequences
- provide tables of data
- provide general definitions and references

### Example 1

- define Solo-WCGW sequence motif
- describe TCGA tumors and adjacent normal samples
- apply Hidden Markov Model-based method
- determine local CpG density and tetranucleotide sequence contexts
- show hypomethylation pattern in human and mouse samples
- analyze solo-WCGW CpGs in various sequence contexts
- describe application for low coverage or single-cell WGBS studies
- illustrate PMD/HMD signal in high coverage WGBS data

### Example 2

- reveal concordance between PMD locations in all samples
- compare average solo-WCGW methylation of core tumors vs core normal
- analyze standard deviation of solo-WCGW methylation across samples
- illustrate rescaling of methylation values for individual samples

### Example 3

- investigate solo-WCGW PMD structure across developmental lineages
- analyze solo-WCGW methylation averages in human and mouse samples
- describe overlap of PMD definition with previous studies
- show PMD structure shared across 5 of 6 categories
- analyze methylation maintenance in embryonic and induced pluripotent stem cells
- describe PMD hypomethylation in various cell types
- illustrate shared PMD structure across developmental lineages

### Example 4

- investigate PMD hypomethylation in gametes and early developmental stages
- analyze solo-WCGW methylation in different stages of mouse spermatogenesis
- show PMD hypomethylation emerges during embryonic development

### Example 5

- investigate link between PMD-associated hypomethylation and chronological age
- analyze solo-WCGW methylation in different primary cell types and ages
- show PMD hypomethylation is associated with chronological age
- analyze effect of environmental exposure on PMD hypomethylation

### Example 6

- study landscape of cancer hypomethylation in TCGA tumors
- analyze solo-WCGW methylation in common PMDs in TCGA tumors
- compare PMD hypomethylation in cancer types and normal adjacent specimens
- show association between PMD hypomethylation and somatic mutation density
- analyze association between PMD hypomethylation and somatic copy number aberration density
- show enrichment of LINE-1 insertion breakpoints in PMD regions
- identify genes associated with PMD hypomethylation and cell proliferation
- show link between PMD hypomethylation and mitotic cell division in cancer

### Example 7

- analyze solo-WCGW CpG methylation and epigenomic features in IMR90 fibroblast
- show correlation between solo-WCGW CpG methylation and replication timing
- analyze contribution of H3K36me3 and replication timing to genome-wide DNA methylation
- show model of methylation maintenance at H3K36me3-marked regions
- illustrate relationship between major determinants of hypomethylation and 3D nuclear topology

### Example 8

- select cancer types for WGBS assay
- describe WGBS protocol adaptation
- outline DNA methylation rate calling
- define genomic binning parameters
- describe preliminary PMD/HMD domain definition
- outline final PMD/HMD definition based on solo-WCGW methylation
- describe HM450 analysis
- analyze IMR90 epigenome
- rescale methylation values based on PMD methylation
- stratify solo-WCGW CpGs in the genome
- describe statistical methods
- provide data availability
- provide code availability
- list URLs for data sources
- summarize workflow for preprocessing WGBS sequencing data
- introduce PMD structure analysis
- motivate solo-WCGW motif
- summarize PMD definition
- describe PMD overlap analysis
- discuss cell-type-specific PMDs
- motivate improved PMD detection
- introduce rank-based correlation analysis
- describe stability of rank-based correlation
- introduce alternative explanation of PMD hypomethylation
- discuss nuclear localization model
- assess relevance of PMD sequence signature
- study somatic and germline mutational landscape
- introduce sub-patterns of solo-WCGW motif
- describe covariance analysis of solo-WCGW motif
- discuss DNA shape features
- describe materials and methods for examples
- outline DNA methylation assay and beta calling
- introduce elastic net modeling strategy
- apply elastic net regression
- standardize PDL
- perform multi-tissue ENR modeling
- perform 10-fold cross validation
- select number of CpGs
- evaluate model performance
- suggest use of elastic net model
- introduce individual probe regression strategy
- apply simple linear regression
- evaluate model performance
- suggest use of individual probe regression model
- compare elastic net and individual regression models
- compare to existing methylation clocks

