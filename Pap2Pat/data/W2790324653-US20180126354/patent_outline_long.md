# DESCRIPTION

## INTRODUCTION

- introduce multiple myeloma
- describe premalignant phase
- discuss genetic alterations
- summarize primary subtypes
- describe secondary genetic events
- introduce prognostic model
- discuss targeted sequencing approaches
- summarize existing studies

## SUMMARY

- introduce capture-based sequencing approach
- describe advantages over existing methods
- motivate personalized treatment plans
- design oligonucleotide probes
- select genes for probe design
- describe gene selection criteria
- motivate discovery platform
- describe platform design
- compare to previous targeted platforms
- describe translocation detection
- outline method steps
- prepare DNA sequencing library
- provide DNA capture array
- hybridize sequencing library
- sequence library to maximum depth
- repeat steps for non-tumor cells
- identify variants
- identify somatic mutations
- describe method variations
- provide alternative probe configuration
- summarize method outcomes
- list mutated genes in multiple myeloma
- describe gene configurations
- introduce oligonucleotide array or set
- tile probes around IgH locus
- target exonic regions of IGH translocation partners
- tile probes across MYC locus
- hybridize to specific genes
- hybridize to additional specific genes
- summarize gene targets
- conclude gene list
- introduce DNA capture array
- describe array composition
- specify oligonucleotide probes
- detail probe hybridization
- list genes detected by probes
- specify canonical IGH translocation partners
- describe MYC locus probes
- list additional genes detected by probes
- specify ATM, BRCA2, and other genes
- describe CLIP1, CSMD3, EP400, and other genes
- specify at least 400 genes detected
- specify 465 genes detected
- specify 467 genes detected
- specify less than 500 genes detected
- specify range of genes detected
- provide additional gene specifications
- conclude gene specifications

## DETAILED DESCRIPTION

- introduce DNA capture array
- define oligonucleotide probe
- describe method of identifying multiple myeloma mutations
- prepare DNA sequencing library from tumor cells
- prepare DNA sequencing library from non-tumor cells
- provide DNA capture array
- hybridize sequencing library from tumor cells to DNA capture array
- sequence library from tumor cells to maximum average depth
- hybridize sequencing library from non-tumor cells to DNA capture array
- sequence library from non-tumor cells to maximum average depth
- identify variants in genomic DNA from tumor cells compared to non-tumor cells
- describe advantages of arrays and methods over whole-exome sequencing
- describe detection of single nucleotide variants, copy number changes, and translocations
- describe data capture using array
- describe analysis of tumor mutations for prognosis and therapy selection
- describe combination with gene expression profiling
- describe custom capture of genes
- describe methods of determining mutual exclusivity/co-occurrence of Multiple Myeloma
- test mutual exclusivity of NRAS, KRAS, and IGLL5
- test mutual exclusivity of hyperdiploid and non-myc IGH translocations
- test co-occurrence of other relations between CNA and SNVs
- test co-occurrence of IGLL5 with del(13q) and DNA repair/B-cell mutations
- test pairwise relationships between two specified genes
- describe integrative analysis

### DETAILED DESCRIPTION

- design custom capture sequencing platform
- target 3.3 Mb of space including 465 genes and IGH region
- design probes for IGH locus and MYC locus
- facilitate detection of chromosome-level, arm-level, and focal copy number alterations
- design probes targeting exonic regions of canonical IGH translocation partners
- hypothesize endonucleolytic cleavage of free DNA ends prior to fusion with a partner chromosome
- design probes to lie entirely outside, entirely inside, or partially outside/inside genomic elements
- construct automated dual indexed libraries
- hybridize library pools with biotinylated Nimblegen probe set
- determine concentration of each captured library pool through qPCR
- sequence library pools on HiSeq2000 or HiSeq2500
- align reads against human reference genome GRCh37-lite using BWA
- call SNVs using samtools, SomaticSniper, MuTect, Strelka, and VarScan2
- call translocations using LUMPY with machine learning approach
- call CNVs using CopyCAT2 parameterized to detect copy number alterations
- perform deep capture sequencing of 15 tumor/normal pairs
- calculate average depth and on-target efficiency using Genome Modeling System's utilities
- calculate per-base coverage for each base in target space
- calculate percent on target efficiency at specified depth
- call CNVs using CopyCAT2 with gaussian mixture model
- exclude certain samples from copy number analysis
- invoke CopyCAT2
- set parameters for CopyCAT2
- annotate CNVs output by CopyCAT2
- define focal and arm-level CNVs
- annotate hyperdiploid events
- annotate focal CNVs with genes
- introduce LUMPY for translocation detection
- align FASTQ files against human genome
- calculate empirical insert size distribution
- invoke LUMPY for translocation detection
- annotate translocations with nearest cancer-associated gene
- parse out putative translocations involving IGH or MYC
- filter IGH translocations using SVM
- train SVM on available FISH data
- tune SVM parameters using grid search
- apply SVM to held-out test samples
- manually define decision boundary for MYC translocations
- filter MYC translocations using SVM
- introduce mapping of IGH constant, switch, and enhancer regions
- search for genes on Ensembl GRCh37
- identify switch regions using UCSC Genome Browser
- confirm validity of switch region approach using BLAT
- determine 3' enhancer region coordinates using BLAT
- validate novel t(14,22) translocation
- perform PCR on genomic DNA
- design primers to detect derivative chromosomes
- separate PCR products with DNA electrophoresis
- sequence PCR products
- map sequences to human genome
- validate t(13;14) translocation
- detect somatic single nucleotide variants
- align reads against human reference genome
- call SNVs using multiple tools
- integrate results from multiple tools
- filter SNVs by quality and annotation
- compare variants from initial and deep sequencing
- filter variants for comparison
- downsample deep sequencing data
- compare variants from downsampled data
- compare capture sequencing to exome sequencing
- reprocess exome sequencing data
- filter variants for comparison
- enrich for c-AID signature amongst IGLL5 mutations
- calculate probability of c-AID-induced mutations
- analyze mutual co-occurrence and mutual exclusivity
- perform survival analysis
- download clinical and variant data
- perform fluorescence in situ hybridization
- analyze RNA-seq expression data
- obtain RNA-seq expression data
- filter genes for inclusion on targeted capture panel

## EXAMPLES

- illustrate design and application of oligonucleotide probe array for targeted sequence capture

### Example 1

- design oligonucleotide probes for MM-specific custom capture sequencing platform
- detect CNVs, SNVs, and translocations in MM samples

### Example 2

- sequence 95 paired tumor and normal cell DNA samples using the platform

### Example 3

- identify copy number alterations with prognostic significance
- detect chromosome-level, arm-level, and focal CNVs
- filter CNV calls with ratios below noise level
- identify somatic mutations in tumor samples
- predict deleterious mutations using Poly-Phen2 and SIFT
- identify multi-hit genes with bi-allelic mutations

### Example 4

- detect IGH translocations using LUMPY
- filter putative translocations based on thresholds
- validate translocations using PCR and FISH data

### Example 5

- prioritize novel IGH translocations as potential driver mutations
- identify cancer-associated genes near chromosomal breakpoints
- validate translocations using PCR
- analyze breakpoints of highly-supported translocations
- identify genes within 1 Mb of breakpoint on der(14)
- validate translocation using PCR amplification
- search for additional IGLL5 translocations
- examine RNA-seq expression data for DERL3 overexpression

### Example 6

- detect intra- and inter-chromosomal MYC translocations
- filter putative MYC translocations using SVM

### Example 7

- identify non-silent single nucleotide variants in all tumor samples

### Example 8

- determine whether MM is characterized by deeply subclonal variants
- perform additional sequencing of tumor and normal samples
- compare allele frequencies of variants discovered
- focus on high-confidence events likely to be of biological relevance
- explore effects of sequencing depth on variant discovery

### Example 9

- facilitate integrative analysis across mutation types
- highlight patterns of mutual exclusivity and co-occurrence
- test for significance of patterns after excluding hypermutator sample
- detect mutation co-occurrence within CNVs
- detect mutual exclusivity between hyperdiploidy and t(11;14)
- detect cross-mutation type exclusivity between CNVs and SNVs
- detect IGLL5 mutations enriched for c-AID signature
- find IGLL5 mutations mutually exclusive of RAS mutations
- associate IGLL5 SNVs with disease progression

