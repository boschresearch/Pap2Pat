# DESCRIPTION

## FIELD OF THE INVENTION

- define genetic analysis

## BACKGROUND OF THE INVENTION

- motivate genetic analysis
- limitations of current solutions

## SUMMARY OF THE INVENTION

- introduce methodology
- application of algorithm

## DETAILED DESCRIPTION OF THE INVENTION

- introduce computer system 100
- describe components of computer system 100
- explain data buses 116
- discuss future computer systems
- describe software languages
- explain compiling software source code
- provide overview of present disclosure

### INTRODUCTION

- introduce applications and data resources for predicting effects of individual nucleotide substitutions
- categorize resources into two groups
- describe first group of resources
- describe second group of resources
- highlight limitations of prior art
- introduce embodiments of present invention
- describe sequence-to-medical-phenotypes information
- show block diagram of method
- receive digitized genomic information
- receive variant call files and genomic feature format files
- reference against rare SNVs, SVs, and indels
- perform targeted genotype calling
- map computerized task to processors
- use GATK haplotype caller and unified genotype caller
- filter calls using hard filtering
- re-annotate calls to add dbsnp identifiers
- perform primary genotype annotation
- convert to annovar file input format
- identify protein coding changes
- create intermediate annotation files
- collect and reduce annotation files
- identify rare variants in inherited disease genes
- categorize rare variants into tiers
- filter variants using local allele frequency and genotype information
- identify known variants in inherited disease genes
- categorize known variants into tiers
- filter rare SVs in inherited disease genes
- perform haplotype assignment
- identify pharmacogenomics haplotypes and genotypes
- categorize pharmacogenomics haplotypes and genotypes into tiers
- provide drug response prediction information

### Alternative Embodiments

- introduce alternative embodiments
- describe FIGS. 1-3
- discuss whole genome sequencing
- perform primary sequence analysis
- perform basic annotation
- reference against rare SNVs, SVs, and indels
- generate rare/Mendelian disease risk candidates
- use manual literature review to generate Mendelian disease risk and carrier status information
- discuss pipeline fashion for efficient computerized processing
- balance computational resources among coprocessors
- describe discovery of variants from ethnically-matched reference sequence
- discuss high-throughput re-sequencing
- use major allele reference genomes
- perform targeted genotype calling
- use ethnicity-specific major allele reference
- standardize reference allele in variant call file
- discuss disease risk and drug response alleles
- perform targeted genotype calling of all loci
- provide metrics for coverage of loci
- facilitate downstream variant annotation
- minimize storage requirements for variant data
- retain BAM files for future analysis
- annotate genetic variants with respect to functional genetic and clinical phenotypes
- extend annovar framework
- provide rich gene-based, functional genomic, regulatory, allele frequency, and phenotypic annotation
- leverage gene coexpression network topology information
- identify genetic variation occurring in genes coexpressed with known disease genes
- prioritize candidate Mendelian disease risk variants
- use prioritization heuristic
- provide parsimonious set of candidates for manual review
- perform sequence validation
- generate high impact disease risk and carrier status information
- discuss pipeline fashion for efficient computerized processing
- balance computational resources among coprocessors
- reduce variants to set that occurs within ClinVar genes
- prioritize variants previously reported in HGMD
- categorize variants into tiers of potential pathogenicity
- prioritize rare and novel variants in monogenic disease genes
- incorporate consensus evidence for evolutionary constraint/conservation and pathogenicity prediction
- archive and categorize all other variants for review and potential reclassification
- annotate personal genetic variation associated with drug response
- generate best-guess haplotypes from short-read sequence data
- create skeleton haplotype pairs using confidently identified homozygous SNVs
- generate full set of complementary haplotypes using heterozygous variant calls
- perform perfect-match search for each haplotype and its complement
- report possible star allele combinations
- annotate and report single variant drug response associations
- categorize haplotypes for star allele assignment into tiers
- categorize individual genotypes for clinical annotations into tiers
- collect results into pharmacogenics report
- discuss disease associated variant discovery in father-mother-child trios
- use HMM-based classifier to identify regions with systematic artifact
- output apparent de novo events, compound heterozygosity, rare homozygous mutations, and instances of apparent hemizygosity
- leverage inheritance information to reduce number of gene regions queried
- discuss inputs, implementation, and parallelization

