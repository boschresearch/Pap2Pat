# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce gene regulation
- describe limitations of current methods
- motivate need for new approach

## SUMMARY

- introduce HiDRA method
- describe genome-wide selection of accessible regions
- explain use of ATAC-Seq and STARR-Seq
- describe machine learning model SHARPR2
- summarize results of HiDRA method
- describe identification of enhancer function
- describe identification of driver elements
- describe prediction of causal genetic variants
- outline method of identifying genomic enhancer regulatory elements
- describe fragmenting genomic DNA
- describe integrating fragments into vector library
- describe sequencing transcripts

## DETAILED DESCRIPTION OF THE EXAMPLE EMBODIMENTS

### General Definitions

- define technical terms
- provide references for molecular biology techniques
- define singular and plural forms
- define "optional" and "about"
- define "biological sample" and "subject"

### Overview

- introduce HiDRA approach
- describe HiDRA method
- highlight advantages of HiDRA

### Nucleic Acids Fragmentation

- describe fragmenting nucleic acids

### Materials

- list materials needed

### Cell Preparation

- describe cell preparation steps

### Transposition Reaction and Purification

- describe transposition reaction and purification steps

### PCR Amplification

- describe PCR amplification steps
- describe qPCR quantification

### Type of Nucleic Acids

- describe types of nucleic acids

### Methods of Fragmentation

- introduce fragmentation methods
- describe enzymatic cleavage
- describe chemical cleavage
- specify endonuclease selection
- describe 5′ overhang generation
- describe blunt end generation
- discuss different fragmentation patterns
- describe fragment end capabilities
- introduce nuclei isolation
- describe pre-fragmentation nuclei isolation
- describe post-fragmentation nuclei isolation
- specify fragment length ranges
- describe overhang generation
- describe filling overhang ends
- describe end joining
- describe ligation junction creation
- introduce label and cross-linking
- describe labeled nucleotide incorporation
- describe cross-linking methods
- describe reversing cross-linking
- describe isolating joined fragments
- describe methods of fragmentation
- define vectors
- describe types of vectors
- describe reporter genes
- describe untranslated regions (UTRs)
- describe introduction of nucleic acids to cells
- describe methods of introducing nucleic acids
- describe cells
- describe cell lines
- describe tissue samples
- describe immune cells
- describe cancer cells
- motivate methods of fragmentation
- introduce sequencing
- describe sequencing technologies
- define depth and coverage
- explain deep sequencing
- explain low-pass sequencing
- introduce Nuc-seq
- describe high-resolution mapping of driver elements
- define driver elements
- explain fragment enrichment enhancer activity
- describe algorithm for identifying driver elements
- introduce identifying sequence variants
- describe identifying driver element variants
- correlate driver element variants with disease
- describe identifying regulatory elements associated with disease
- describe identifying sequence variants in regulatory elements
- describe identifying functional consequences of sequence variants
- introduce additional embodiments
- describe method of identifying genomic enhancer regulatory elements
- describe additional embodiments of method
- describe alternative method of identifying genomic enhancer regulatory elements

## EXAMPLES

### Example 1—HiDRA Experimental Method Overview and Plasmid Library Construction

- introduce HiDRA method
- describe plasmid library construction
- summarize library characteristics

### Example 2—Identification of DNA Fragments with Transcriptional Regulatory Activity

- describe transfection and RNA sequencing
- quantify regulatory activity of fragments
- identify active HiDRA fragments and regions

### Example 3—HiDRA Regulatory Elements are Enriched in Promoter and Enhancer Elements

- survey active HiDRA fragments for genomic characteristics
- analyze enrichment of active fragments in chromatin states
- study enrichment of individual histone marks
- discuss implications for regulatory architecture

### Example 4—HiDRA Regulatory Activity Outside Promoter and Enhancer Regions

- analyze active HiDRA regions outside active chromatin states
- study transcription factor binding in active regions
- discuss implications for endogenous repression and cell-type specificity

### Example 5—High-Resolution Mapping of Regulatory Activity with HiDRA

- describe SHARPR2 algorithm
- apply SHARPR2 to HiDRA data
- analyze predicted driver elements
- discuss biological significance of driver elements

### Example 6—Prioritization and Characterization of GWAS Variants Affecting Regulatory Activity

- study overlap between GWAS variants and driver nucleotides
- analyze example of IKZF3 locus
- discuss implications for causal variant identification
- describe approach to detect allelic activity
- analyze example of rs2382817 SNP

### Example 7—Discussion

- present high-throughput experimental assay
- discuss application and limitations of HiDRA
- propose improvements to HiDRA methodology
- summarize and envision future applications

### Example 8—Methods

- perform HiDRA library construction
- introduce ATAC-seq reactions
- describe cell collection and lysis
- outline Tn5 digestion and cleanup
- perform PCR and cleanup
- describe size selection of ATAC-seq fragments
- treat with anti-mitochondrial DNA CRISPR/Cas9 library
- perform second round of PCR
- describe plasmid library construction
- generate linear backbone
- perform InFusion HD cloning reactions
- transform into electrocompetent bacteria
- describe cell culture and transfections
- perform RNA isolation and cDNA generation
- generate cDNA from mRNA
- describe library construction and high-throughput sequencing
- perform qPCR to test amplification
- identify significantly up-regulated fragment groups
- analyze active HiDRA regions
- describe read mapping and data analysis for allele-specific regulatory activity

