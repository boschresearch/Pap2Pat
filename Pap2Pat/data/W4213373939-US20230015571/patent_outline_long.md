# DESCRIPTION

## BACKGROUND

### 1. Technical Field

- introduce technical field

### 2. Related Art

- describe colorectal cancer
- explain adenoma-carcinoma pathway
- explain serrated neoplasia pathway
- explain microsatellite instability
- describe DNA methylation
- discuss DNA methylation markers
- describe limitations of current biomarkers
- discuss methylation-specific PCR

## PRIOR ART DOCUMENTS

### Non-Patent Documents

- cite non-patent document

## SUMMARY

- introduce invention
- object of invention
- provide composition for diagnosing colorectal cancer
- provide nucleic acid molecule for detecting methylation
- define colorectal cancer
- define diagnosis
- define prognosis
- define disease-free survival rate
- define therapeutic responsiveness
- describe methylation in intragenic region of PDX1, EN2 and/or MSX1
- describe MSP primer set
- describe primer
- describe probe
- describe hybridization conditions
- describe intragenic CpG island of PDX1
- describe MSP primer set for PDX1
- describe intragenic CpG island of EN2
- describe MSP primer set for EN2
- describe intragenic CpG island of MSX1
- describe MSP primer set for MSX1
- describe nucleotide
- describe sequences substantially identical
- describe subject
- describe composition for diagnosing colorectal cancer
- describe expression levels of PDX1, GRIN2D, PITX1, TFAP2A, EN2 and MSX1 genes
- describe composition for predicting prognosis of colorectal cancer
- describe expression levels of PDX1, EN2 and MSX1 genes
- describe composition for predicting metastasis of colorectal cancer
- describe nucleic acid molecule for detecting methylation
- describe forward and reverse primers
- describe amplicon length
- describe total number of CpG sites
- describe melting temperature (Tm)
- describe primer set for measuring DNA methylation level
- describe regulation of gene expression
- describe methylation level in target region
- describe forward and reverse primers
- describe amplicon length
- describe melting temperature (Tm)
- describe primer set for measuring DNA methylation level
- describe methylation level in intragenic region of target gene
- describe methylation-specific PCR (MSP) primer set
- describe CpG sites in target gene-binding regions
- describe methylation level in intragenic CpG island
- describe disease
- describe cancer
- describe colorectal cancer
- describe methods for diagnosing or predicting prognosis of colorectal cancer
- describe methods for diagnosing colorectal cancer
- describe methods for predicting prognosis of colorectal cancer
- describe methods for treating colorectal cancer
- describe treatment strategy

## DETAILED DESCRIPTION

- describe experimental methods and results for targeted bisulfite sequencing and analysis of colorectal cancer tissues

### Experimental Methods

- analyze Infinium HumanMethylation450 BeadChip data from TCGA
- design hybridizing probe pool
- obtain colorectal tumor and adjacent healthy specimens
- prepare single targeted bisulfite sequencing library
- perform end repair, A-tailing, and sequencing adaptor ligation
- bisulfite-convert DNA library
- amplify library via precapture PCR
- capture bisulfite-converted library
- purify and amplify captured library
- sequence library on HiSeq 2500 instrument
- preprocess and screen targeted bisulfite sequencing data
- trim adaptor sequences from data
- align sequencing reads with Bowtie2
- extract methylation values of CpG sites
- filter out low-quality sequencing data
- perform hierarchical clustering with Canberra distance
- draw line graphs with ggplot2
- perform hierarchical clustering with Manhattan distance
- analyze TCGA colon adenocarcinoma RNA sequencing data
- integrate read count files into matrix format
- generate list of differentially expressed genes
- derive TPM value of each gene
- select genes with statistical significance
- design overexpression construct
- transfect construct into HCT116 cells
- verify transfection efficiency
- extract genomic DNA and total RNA from single sample
- perform qMSP and qPCR
- design MSP primers
- perform Western blotting

### Experimental Results

- identify differentially methylated regions in CRC tissues
- filter CpG islands based on methylation differences
- select candidate CpG islands
- perform targeted bisulfite sequencing
- analyze methylation values of CpG islands
- identify hypermethylated and hypomethylated regions
- analyze locations of differentially methylated CpG islands
- examine correlation between methylation and gene expression
- select candidate genes for developing CRC biomarkers
- analyze gene expression using TCGA RNA-seq dataset
- examine relationship between gene expression and survival rate
- focus on PDX1, EN2, and MSX1 genes
- overexpress PDX1, EN2, and MSX1 in HCT116 cells
- determine cell proliferation using CCK-8
- perform Transwell assay to determine cell migration

### Design of MSP Primers for Optimal Detection of Methylation Changes

- motivate MSP primer design
- introduce primer design criteria
- describe primer design process for PDX1
- present primer design results for PDX1
- describe primer design process for EN2 and MSX1
- present primer design results for EN2 and MSX1
- introduce MSP primer testing
- describe MSP primer testing methodology
- present MSP primer testing results
- quantify methylation levels using MSP primers
- introduce half-methylation primer testing
- present half-methylation primer testing results
- motivate dynamic methylation change detection
- introduce CRISPR/dCas9-TET1 system
- present dynamic methylation change detection results
- correlate methylation levels with gene expression
- summarize clinical implications of methylation levels

