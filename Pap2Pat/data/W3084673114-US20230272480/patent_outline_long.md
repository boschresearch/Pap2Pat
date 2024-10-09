# DESCRIPTION

## FIELD

- relate to classifying cancer

## BACKGROUND

- motivate NEN classification
- describe NEN diversity
- introduce miRNA expression profiling
- discuss limitations of current approaches

## SUMMARY

- introduce method for classifying cancer
- describe obtaining miRNA expression data
- use discriminator function
- train classifier with miR-375 and miR-7
- classify NEN or non-NEN
- train classifier with miR-200a and miR-10b
- classify epithelial NEN
- train classifier with miR-30a
- classify parathyroid adenoma
- train classifier with miR-10a and miR-212-3p
- classify pituitary adenoma
- train classifier with miR-15b and miR-660
- classify Merkel cell carcinoma
- train classifier with miR-29a, miR-335-5p, and miR-222
- classify medullary thyroid carcinoma
- train classifier with miR-760, miR-1224-5p, miR-139, miR-205, and miR
- classify gastroenteropancreatic neoplasm
- train classifier with miR-615 and miR-92b
- classify midgut neoplasm
- train classifier with miR-149, miR-192, and miR-125b
- classify ileal neoplasm
- train classifier with miR-487b and miR-429
- classify rectal neoplasm
- train classifier with miR-18a and miR-155
- classify lung neoplasm
- train classifier with miR-93
- classify neuroblastoma
- train classifier with miR-10b and miR-379
- classify pheochromocytoma or paraganglioma
- describe preprocessing data
- evaluate NEN cancer status
- measure expression levels of miRNAs
- determine NEN cancer status
- describe constructing discriminator function
- select features and evaluate
- construct individual classifiers
- combine classifiers into hierarchical classifier
- describe non-transitory computer readable media

## DETAILED DESCRIPTION OF EMBODIMENTS

- classify neuroendocrine neoplasm (NEN) in a subject
- generate reference miRNA expression profiles for multiple NEN pathological types
- identify candidate category and type specific miRNAs for classification
- develop multilayer classifier for discriminating NEN pathological types
- compare multiple NEN pathological types and site-matched non-NEN controls
- employ advanced computational approaches for miRNA feature selection
- assess data reliability through knowledge of miRNA cluster composition
- evaluate classifier performance and transferability
- assess impact of miRNA cluster substitutions on accuracy
- assess abundance of selected classificatory miRNAs
- use miRNA clusters as a measure of data quality and transferability
- build streamlined NEN classification tool
- determine expression levels of at least two selected miRNAs
- subject expression levels to discriminator function
- classify cancer according to expression levels of at least two miRNAs
- use miR-375 as a biomarker in NEN cancer
- add additional miRNAs to the biological sample
- compare expression levels of at least two miRNAs
- determine prognosis, response to a treatment, and/or effectiveness of a treatment
- measure miRNA expression levels using real-time quantitative polymerase chain reaction
- generate expression level based on comparison to at least a second miRNA
- use delta-Ct method to generate expression level
- provide methods and discriminator constructs for discriminating between two or more conditions of interest
- construct discriminator function for use with a dataset
- preprocess data to improve overall rigor of the discriminator function
- select features using one or more feature selection algorithms
- evaluate features using domain knowledge and/or consideration of significance
- identify key features in the dataset
- construct a generalizable classifier
- implement hierarchical classification for each condition of interest
- perform feature selection and ranking for each condition of interest
- evaluate features for each condition of interest
- classify samples according to each condition of interest
- construct layered discriminator function with feature selection and ranking, feature evaluation, and classification functions
- apply discriminator function to another dataset of the same type of data
- provide software products and programmed media for use with a processor

### ABBREVIATIONS

- define abbreviations used throughout the description
- list abbreviations used throughout the description

### EXAMPLE 1

- introduce study design and clinical materials
- describe RNA isolation and quantitation
- outline small RNA sequencing and sequence annotation
- detail data preprocessing and filtering
- perform unsupervised hierarchical clustering
- assess and compare abundant miRNAs in NEN and non-NEN samples
- discover miRNA-based NEN classification
- construct and cross-validate multilayer classifier
- assess classifier performance and transferability
- perform statistical analyses
- describe anatomical distribution and histopathological diagnoses of study samples
- generate comprehensive miRNA expression profiles
- analyze abundant miRNA composition in NEN and non-NEN samples
- compare abundant miRNAs in NEN and non-NEN samples
- perform unsupervised hierarchical clustering of filtered miRNA expression profiles
- identify candidate miRNA markers for NEN classification

### RESULTS

- characterize and compare miRNA expression between NEN and non-NEN samples
- generate comprehensive miRNA expression profiles
- analyze abundant miRNA composition in NEN and non-NEN samples
- compare abundant miRNAs in NEN and non-NEN samples
- perform unsupervised hierarchical clustering of filtered miRNA expression profiles
- identify candidate miRNA markers for NEN classification
- construct and cross-validate multilayer classifier
- assess classifier performance and transferability
- detect histological misidentification by miRNA-based NEN classifier
- describe anatomical distribution and histopathological diagnoses of study samples
- generate comprehensive miRNA expression profiles
- analyze abundant miRNA composition in NEN and non-NEN samples
- compare abundant miRNAs in NEN and non-NEN samples
- perform unsupervised hierarchical clustering of filtered miRNA expression profiles
- identify candidate miRNA markers for NEN classification
- construct and cross-validate multilayer classifier
- assess classifier performance and transferability
- detect histological misidentification by miRNA-based NEN classifier
- summarize results

### DISCUSSION

- discuss unsupervised hierarchical clustering of filtered miRNA expression profiles
- motivate NEN grouping
- describe epithelial and non-epithelial NENs
- discuss miR-375 and miR-10b expression
- summarize similarities in abundant miRNA composition
- highlight differences in abundant miRNA composition
- identify new and confirm known miRNA markers
- discuss miR-375 as a universal marker of neuroendocrine cell differentiation
- describe feature selection algorithm
- construct and validate multilayer classifiers
- evaluate classifier performance and transferability
- provide anatomical location and diagnostic histopathological information
- discuss sample abbreviations
- summarize miRNA expression profiling results

### EXAMPLE 2.

- preprocess expression data for miRNAs
- determine NEN or non-NEN using miR-375 and miR-7
- determine non-epithelial or epithelial using miR-10b and miR-200a
- identify neuroblastoma using miR-93
- determine pheochromocytoma or paraganglioma using miR-379 and miR-10b
- identify parathyroid adenoma using miR-30a
- identify pituitary neuroendocrine tumour using miR-212-3p and miR-10a
- identify merkel cell carcinoma using miR-15b and miR-660

### EXAMPLE 3

- collect and process plasma, serum, and/or other biofluids
- obtain demographic and clinical information
- isolate and quantify total extracellular RNA
- prepare exRNA sequencing libraries
- perform exRNA sequencing and sequence annotation
- preprocess and filter data
- perform unsupervised hierarchical clustering
- identify features for classification
- construct and cross-validate decision-layer and multilayer classifiers
- assess classifier performance and transferability
- evaluate impact of miRNA cluster member substitutions
- inspect expression levels of selected miRNAs

### EXAMPLE 4

- measure miR-375 in NEN patient plasma using real-time quantitative PCR
- spike in ath-miR-159a into plasma samples
- isolate cell-free total RNA and prepare cDNA
- perform miR-375 and ath-miR-159a real-time PCR

## EQUIVALENTS

- acknowledge variations in embodiments

