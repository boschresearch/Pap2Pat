# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce gene regulation
- describe limitations of current methods
- explain epigenomic signatures
- discuss experimental dissection of enhancer and promoter regions
- describe high-throughput reporter assays
- highlight need for improved methods

## SUMMARY

- introduce HiDRA method
- describe genome-wide selection of accessible regions
- explain use of ATAC-Seq
- describe fragmenting genomic DNA
- amplify and enrich fragments
- integrate fragments into vector
- transfect or transduce cell line
- sequence transcripts
- identify enhancer regulatory elements
- describe SHARPR2 machine learning model
- map enhancer function
- enrich for endogenous active histone marks
- discover high-resolution driver elements
- predict causal genetic variants
- describe method of identifying genomic enhancer regulatory elements
- fragment genomic DNA
- amplify and enrich fragments
- integrate fragments into vector
- transfect or transduce cell line
- sequence transcripts
- identify enhancer regulatory elements
- describe variations of method
- describe high-resolution mapping of driver elements
- identify driver element variants

## DETAILED DESCRIPTION OF THE EXAMPLE EMBODIMENTS

### General Definitions

- define technical terms
- provide references for molecular biology techniques
- define singular and plural forms
- define "optional" and "optionally"
- define numerical ranges
- define "about" and "approximately"
- define "biological sample"
- define "subject", "individual", and "patient"
- describe embodiment structure
- describe feature combinations
- incorporate publications by reference

### Overview

- introduce HiDRA approach
- describe HiDRA method
- highlight advantages of HiDRA
- describe application of HiDRA
- provide example results of HiDRA
- summarize HiDRA benefits

### Nucleic Acids Fragmentation

- describe fragmenting nucleic acids
- provide example protocol for fragmenting

### Materials

- list materials needed

### Cell Preparation

- describe cell preparation steps

### Transposition Reaction and Purification

- describe transposition reaction and purification steps

### PCR Amplification

- describe PCR amplification steps
- highlight importance of initial extension step
- describe qPCR quantification
- determine optimal PCR cycles
- describe final PCR amplification steps

### Type of Nucleic Acids

- describe types of nucleic acids used

### Methods of Fragmentation

- introduce fragmentation methods
- enzymatic cleavage
- chemical cleavage
- endonuclease selection
- 5′ overhang generation
- blunt end generation
- different fragmentation techniques
- different fragmentation patterns
- different nucleic acid ends
- fragmenting sample yields ends
- ends capable of being joined
- isolate nuclei from cells
- isolate nuclei before fragmentation
- isolate nuclei from frozen or fixed tissue
- process nuclei to obtain genomic fragments
- ATAC-seq protocol for genomic fragments
- buffer for crude nuclei preparation
- fragment length from 50 to 5000 bp
- fragment length from 100 to 1000 bp
- specific fragment length examples
- fragment length selection
- overhang generation
- 5′ overhanging end
- 3′ overhanging end
- multiple overhanging ends
- fill in overhanging ends
- fill in with labeled nucleotide
- blunt ended fragments
- join overhang ends
- ligation using nucleic acid ligase
- alternative joining methods
- end joined fragments
- junction with labeled nucleic acid
- label and cross-link
- cross-linking agents
- reversible crosslinking agents
- non-reversible crosslinking agents
- chemical crosslinkers
- no crosslinking agent
- non-crosslinking means
- isolate joined fragments
- capture with labeled nucleotide
- amplify fragments
- describe methods of fragmentation
- integrate nucleic acid fragments into vector
- define vector
- describe types of vectors
- describe viral vectors
- describe episomal vectors
- describe integrating viral vectors
- describe expression vectors
- describe reporter genes
- encode reporter gene and untranslated sequence
- describe detectable markers
- describe cell surface markers
- measure enhancer activity
- describe untranslated region (UTR)
- integrate nucleic acid fragment into UTR
- introduce nucleic acids to cells
- describe methods of introducing nucleic acids
- describe cells
- describe cell lines
- describe tissue samples
- describe immune cells
- describe cancer cells
- describe leukemia
- describe carcinomas
- describe other types of cancer cells
- motivate methods of fragmentation
- introduce sequencing
- describe sequencing technologies
- define depth and coverage
- explain importance of high coverage
- introduce deep sequencing
- define low-pass sequencing
- describe Nuc-seq
- introduce high-resolution mapping
- define driver elements
- describe fragment enrichment enhancer activity
- introduce algorithm for identifying driver elements
- describe use of computing system
- introduce identifying sequence variants
- describe correlating variants with disease
- introduce identifying driver element variants
- describe associating variants with disease
- introduce identifying regulatory elements
- describe identifying sequence variants in regulatory elements
- introduce identifying functional consequences
- describe identifying regulatory elements for disease
- introduce identifying genes contributing to disease risk
- describe identifying alleles or polymorphisms associated with disease
- introduce identifying phenotypic traits
- describe method of identifying genomic enhancer regulatory elements
- introduce fragmenting genomic DNA
- describe amplifying genomic DNA fragments
- introduce enriching amplified fragments
- describe integrating enriched fragments into vector
- introduce transfecting or transducing cell line
- describe sequencing transcripts
- introduce identifying integrated fragments with enhancer activity
- describe removing mitochondrial DNA
- introduce using CRISPR system
- describe integrating enriched fragments into UTR
- introduce using plasmid or viral vector
- describe identifying integrated fragments with enhancer activity
- introduce comparing sequenced genomic fragment to chromatin state
- describe comparing sequenced genomic fragment to LTR retrotransposon sequences
- introduce detecting expression of reporter gene
- describe sorting cells based on expression levels
- introduce obtaining population of cells

## EXAMPLES

### Example 1—HiDRA Experimental Method Overview and Plasmid Library Construction

- introduce HiDRA method
- describe ATAC-seq and STARR-seq
- outline library construction process
- detail fragment length distribution
- describe library coverage of enhancers and promoters
- highlight library's ability to target regulatory regions

### Example 2—Identification of DNA Fragments with Transcriptional Regulatory Activity

- describe transfection and RNA sequencing
- quantify regulatory activity of fragments
- group fragments to boost read coverage
- identify active HiDRA fragments
- analyze active HiDRA fragments' input DNA levels
- validate HiDRA using immunoglobulin heavy chain enhancer

### Example 3—HiDRA Regulatory Elements are Enriched in Promoter and Enhancer Elements

- survey active HiDRA fragments for chromatin characteristics
- analyze enrichment of active fragments in promoter and enhancer states
- describe enrichment of "TSS Flanking Upstream" chromatin state
- compute enrichment of chromatin states by HiDRA activity strength
- analyze enrichment of individual histone marks
- study motif enrichment in active HiDRA regions
- compare motif enrichment in promoter and enhancer chromatin states
- highlight differences in motif content between promoter and enhancer regions
- discuss implications for regulatory architecture of genes

### Example 4—HiDRA Regulatory Activity Outside Promoter and Enhancer Regions

- analyze active HiDRA regions outside active chromatin states
- study binding of transcription factors in ChIP-seq experiments
- compare motif enrichment in active HiDRA regions
- analyze endogenous TF binding in active HiDRA regions
- study activity of HiDRA regions in another human tissue
- discuss enrichment of LTR retrotransposons in active HiDRA regions

### Example 5—High-Resolution Mapping of Regulatory Activity with HiDRA

- describe high-resolution mapping of regulatory activity
- analyze regulatory activity in a 3 kb region on chromosome 7
- develop SHARPR2 algorithm for high-resolution inferences
- apply SHARPR2 to predict driver elements
- analyze length of driver elements by coverage
- study enrichment of regulatory motifs in driver elements
- compare driver elements to shuffled controls
- discuss biological significance of high-resolution inferences

### Example 6—Prioritization and Characterization of GWAS Variants Affecting Regulatory Activity

- study overlap between genetic variants and driver nucleotides
- analyze overlap with fine-mapped SNPs associated with immune traits
- predict causal variant in IKZF3 locus
- discuss rs12946510 as a causal SNP
- infer genotype of RNA fragments
- use low-depth re-sequencing to determine allele-specific activity
- filter out false positives due to fragment end differences
- identify allelic HiDRA SNPs with differential activity
- analyze corresponding SNPs in allelic HiDRA regions
- study rs2382817 as an example of allelic HiDRA SNP
- discuss implications for disease-associated variants

### Example 7—Discussion

- present high-throughput experimental assay
- perform HiDRA mapping of regulatory activity
- analyze results of HiDRA fragments
- discuss applicability to other cell lines
- demonstrate proof-of-concept application
- discuss limitations of HiDRA
- propose improvements to the assay
- summarize HiDRA method and its potential applications

### Example 8—Methods

- perform HiDRA library construction
- introduce ATAC-seq reactions
- describe cell collection and lysis
- perform Tn5 digestion and cleanup
- split eluate into PCR reactions
- perform PCR using custom primers
- pool and clean up PCR reactions
- run on agarose gel and perform size selection
- purify DNA using MinElute Gel Extraction kit
- treat with anti-mitochondrial DNA CRISPR/Cas9 library
- clean up reaction and split into PCR reactions
- perform second round of PCR
- clean up PCR products using AMPure bead selection
- quantify using Qubit dsDNA HS Assay kit
- generate pSTARR-seq_human plasmid library
- perform cloning of fragment library into plasmid backbone
- transform into electrocompetent bacteria
- recover and incubate bacteria
- estimate number of clones in library
- collect and purify plasmids from bacteria
- quantify plasmid concentration using Nanodrop One machine
- ensure plasmid library quality and diversity
- amplify fragment library by PCR
- run on Illumina MiSeq machine
- align to human genome
- describe cell culture and transfections
- prepare GM12878 cells for transfection
- transfect cells with plasmid library
- recover and incubate transfected cells
- isolate RNA from transfected cells
- generate cDNA from mRNA
- perform qPCR to test amplification of cDNA
- perform PCR to amplify cDNA
- clean up and balance PCR reactions for sequencing
- sequence libraries on NextSeq 500 machine
- map reads to human genome
- identify unique fragments and filter reads
- group fragments into fragment groups
- identify significantly up-regulated fragment groups
- analyze active HiDRA regions
- provide URLs and data availability

