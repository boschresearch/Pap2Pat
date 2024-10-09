# DESCRIPTION

## FIELD OF THE INVENTION

- define genetic analysis

## BACKGROUND OF THE INVENTION

- motivate genetic analysis

## SUMMARY OF THE INVENTION

- describe methodology

## DETAILED DESCRIPTION OF THE INVENTION

- describe computer system 100
- outline components of computer system 100
- discuss flexibility of computer system 100

### INTRODUCTION

- introduce problem of predicting effects of individual nucleotide substitutions
- categorize resources for predicting pathogenicity of genetic variants
- describe limitations of first set of resources
- describe limitations of second set of resources
- motivate need for comprehensive clinical interpretation of sequence variants
- introduce embodiments of the present invention
- describe sequence-to-medical-phenotypes information
- outline method for generating sequence-to-medical-phenotypes information
- receive digitized genomic information
- reference rare SNVs, SVs, and indels
- perform targeted genotype calling
- perform primary genotype annotation
- identify rare variants in inherited disease genes
- identify known variants in inherited disease genes
- perform haplotype assignment

### Alternative Embodiments

- describe alternative embodiments of the present invention
- introduce methods for clinical interpretation in the context of disease gene finding
- perform whole genome sequencing
- perform primary sequence analysis
- perform basic annotation
- reference against rare SNVs, SVs, and indels
- generate rare/Mendelian disease risk candidates
- use results of manual literature review to generate Mendelian disease risk and carrier status information
- reference against drug response genotypes and PharmaGKB information
- generate drug response information
- discuss pipeline architecture and balancing computational resources
- introduce discovery of variants from an ethnically-matched reference sequence
- discuss limitations of the NCBI reference genome
- develop major allele reference sequences for each of the three major HapMap populations
- use major allele reference genomes for variant identification
- discuss annotation of genetic variants with respect to functional genetic and clinical phenotypes
- extend annovar framework to provide rich gene-based, functional genomic, regulatory, allele frequency, and phenotypic annotation
- leverage gene coexpression network topology information to provide quantitative prior expectations about gene-level pathogenicity
- discuss bioinformatic prioritization of candidate Mendelian disease risk variants
- use prioritization heuristic to provide a parsimonious set of candidates for manual review
- categorize variants into tiers based on expected pathogenicity and allele frequency
- discuss annotation of personal genetic variation associated with drug response
- generate best-guess haplotypes from short-read sequence data
- report single variant drug response associations cataloged in the PharmGKB knowledgebase
- discuss disease associated variant discovery in father-mother-child trios with simplex phenotypes
- use HMM-based classifier to identify regions with systematic artifact
- output apparent de novo events, compound heterozygosity, rare homozygous mutations, and instances of apparent hemizygosity

