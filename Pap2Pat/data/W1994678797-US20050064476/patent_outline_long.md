# DESCRIPTION

## FIELD OF THE INVENTION

- define genomic region estimation methods

## BACKGROUND OF THE INVENTION

- motivate genetic events in cancer cells
- describe DNA copy number changes
- summarize classical LOH studies
- describe approaches to measure genome-wide DNA copy number changes
- limitations of comparative genomic hybridization
- advantages of single nucleotide polymorphisms
- motivate need for improved molecular methods

## SUMMARY OF THE INVENTION

- describe method for estimating copy number
- summarize first embodiment of method
- summarize second embodiment of method
- summarize third embodiment of method

## BRIEF DESCRIPTION OF THE FIGURES

- describe accompanying drawings

## DETAILED DESCRIPTION OF THE INVENTION

### (A) General

- incorporate references by citation
- define singular and plural forms
- define individual
- describe range format
- specify default base for log function
- employ conventional techniques
- cite standard laboratory manuals
- describe solid substrates and arrays
- cite patents and applications for array synthesis
- describe gene expression monitoring and profiling
- describe genotyping and diagnostics
- describe sample preparation methods
- describe amplification mechanisms
- describe ligase chain reaction
- describe transcription amplification
- describe self-sustained sequence replication
- describe selective amplification of target polynucleotide sequences
- describe consensus sequence primed polymerase chain reaction
- describe arbitrarily primed polymerase chain reaction
- describe nucleic acid based sequence amplification
- describe signal detection of hybridization
- describe computer software products and systems

### (B) Definitions

- define nucleic acids
- describe types of nucleic acids
- introduce oligonucleotides and polynucleotides
- define polynucleotides
- describe types of polynucleotides
- introduce peptide nucleic acid (PNA)
- define fragment
- describe methods of fragmenting nucleic acid
- introduce chemical fragmentation methods
- introduce physical fragmentation methods
- describe size ranges of fragments
- define adaptor sequences
- describe characteristics of adaptors
- introduce uses of adaptors
- define genome
- describe characteristics of a genome
- define chromosome
- describe characteristics of a chromosome
- introduce chromosomal region
- define subset or representative subset
- describe partitioning of fragments into subsets
- define array
- describe characteristics of arrays
- introduce methods of producing arrays
- describe types of arrays
- define hybridization probes
- describe characteristics of hybridization probes
- introduce stringent hybridization conditions
- define allele
- describe characteristics of alleles
- introduce polymorphism
- describe characteristics of polymorphic markers
- define genotyping
- describe determination of genetic information
- introduce linkage disequilibrium
- describe characteristics of linkage disequilibrium
- define loss of heterozygosity
- describe genetic rearrangement
- define aneuploid

### (C) Detection of Changes in Copy Number

- introduce genetic instability
- describe high-density DNA array technology
- disclose methods for LOH and genomic amplifications/deletions detection
- specify high density array as genotyping array
- describe intensity of hybridization and log intensity vs log copy number relationship
- introduce methods for genotyping many polymorphisms in parallel
- describe complexity reduction methods
- introduce SNP genotyping via hybridization to high density oligonucleotide arrays
- describe algorithms for identifying regions of homozygous deletions or gene amplification
- introduce chip intensity normalization
- describe statistical significance of DNA copy number changes
- introduce likelihood of a contiguous stretch of homozygous markers
- describe allele frequencies from a publicly available database
- introduce whole genome sampling analysis (WGSA)
- describe SNP genotyping using WGSA
- introduce methods for identifying chromosomal gains and losses
- describe SNP genotyping using 10K or 100K SNP arrays
- introduce arrays with larger numbers of SNPs
- describe probe sets with perfect match probes
- illustrate computer system for executing software
- describe system block diagram of computer system
- introduce copy number estimation by comparing intensity measurements
- describe reference set of normal individuals
- introduce data points selection for reference samples
- describe steps of the method
- introduce deletion and amplification detection
- describe cross-hybridization and discrimination ratio
- introduce estimation of copy number change
- describe linear relationship between log intensity and log copy number
- introduce method for estimating genome-wide copy number
- describe analysis of LOH and DNA gains and losses
- introduce individual SNP analysis and meta-analysis
- describe issues with multiple hypothesis testing
- introduce alternative statistical methods
- describe regions that may have undergone LOH
- introduce identification of LOH in a mixture of tumor and normal cells
- introduce detection of changes in copy number
- combine transcriptional profiles with copy number profiles
- scale methods to accommodate SNP information
- describe feature extraction using Mapping 10K Array
- calculate log of arithmetic average of PM intensities
- scale S to have mean of zero and variance of one
- use discrimination ratio as supplementary metric
- estimate significance of copy number variation
- compare to normal reference set
- consider genotype of target cell line
- estimate distribution of reference samples
- calculate p-value
- perform meta-analysis
- calculate individual test statistic
- assume standard normal distribution
- define candidate stretch
- substitute meta p-value for individual p-values
- estimate loss of heterozygosity
- calculate probability of being homozygous
- analyze intensity information
- design array to detect presence or absence of fragments
- predict fragments present in amplified sample
- design probes for every 100 basepair region
- amplify and hybridize experimental sample
- identify regions missing from genomic sample
- detect rearrangements in genome
- track cell division
- track cross-over hybridization and genetic rearrangements
- predict patient outcome or prognosis
- select treatment regime for patient
- classify sample as cancerous
- diagnose cancers
- determine amount of gene amplification
- select probes according to probe hybridization model
- predict fragments present in reduced complexity sample
- design array depending on complexity reduction method
- use computer system to predict sequences present
- optimize amplification methods
- design array to detect presence or absence of fragments
- label fragments prior to hybridization
- hybridize sample to array without reducing complexity
- identify new homozygous deletions associated with cancer

## EXAMPLES

### Cell Lines and Nucleic Acid Isolation

- obtain cell lines
- grow cells under recommended culture conditions
- isolate genomic DNA
- perform WGSA assay
- quantify DNA amounts
- perform quantitative PCR

### Copy Number Estimation and Significance Calculation

- perform dosage response experiments
- verify algorithm results using PCR
- confirm known true positive regions
- test dosage response between copy number and chip intensity
- estimate log copy number
- determine slope and y-intercept
- compare results to 2X sample
- analyze log intensity ratio
- estimate copy number
- perform qPCR validation experiment
- determine ΔCt values
- analyze relationship between ΔCt and significance level
- survey breast cancer cell line panel
- analyze copy number changes in two regions
- perform qPCR to confirm copy number increase
- analyze SK-BR-3 chromosome 8 and BT-20 chromosome 9
- illustrate high resolution capabilities
- analyze correlation between log signal intensity and log copy number
- design array with probes optimized for copy number alterations

### Meta-Analysis

- detect homozygous deletions and amplifications
- analyze detection rate of regions with small copy number changes
- perform meta-analysis to improve detection rate
- analyze ROC curves
- compare individual analysis and meta-analysis
- analyze signal to noise ratio
- evaluate method using matched Hs578 pair
- capture traditionally defined LOH markers
- analyze probability model for LOH identification
- identify genomic regions with LOH
- determine copy number change of region and significance
- analyze LOH with either no copy number reduction or copy number increases

### Mixing Experiment

- assess tolerance of WGSA assay and algorithm to mixed DNA samples
- mix DNA from cancer cell line with normal matched DNA
- analyze changes in LOH and copy number alterations
- examine relationship between transition points of LOH detection and copy number
- compare detection of gains and losses in mixed samples
- analyze effect of mixed samples on detection of LOH and copy number alterations
- determine tolerance of detection of LOH and copy number alterations

### Measuring Copy Number Alterations in “Normal” Samples

- analyze reference samples for copy number alterations
- perform leave-one-out analysis
- evaluate frequency and significance of copy number alteration
- identify long stretches of homozygous calls
- provide example of WGSA
- describe DNA digestion protocol
- outline ligation and PCR protocols
- detail DNA fragmentation and labeling protocols
- describe hybridization and staining protocols

## CONCLUSION

- disclose methods for identifying genomic DNA copy number changes
- describe scope of invention
- emphasize importance of appended claims

