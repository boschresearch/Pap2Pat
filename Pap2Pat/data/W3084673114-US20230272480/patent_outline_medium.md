# DESCRIPTION

## FIELD

- relate to classifying cancer

## BACKGROUND

- motivate NEN classification
- introduce miRNA expression profiling

## SUMMARY

- introduce method for classifying cancer
- describe discriminator function
- classify NEN or non-NEN
- classify epithelial NEN
- classify parathyroid adenoma (PTA)
- classify pituitary adenoma (PitNET)
- classify Merkel cell carcinoma (MCC)
- classify medullary thyroid carcinoma (MTC)
- classify gastroenteropancreatic (GEP) neoplasm
- classify midgut neoplasm
- classify ileal neoplasm (INET)
- classify rectal neoplasm (RNET)
- classify lung neoplasm
- classify carcinoid (TC/AC)
- classify non-epithelial NEN
- classify neuroblastoma (NB)
- classify pheochromocytoma (PCC) or paraganglioma (PGL)
- describe preprocessing of data
- describe evaluating NEN cancer status

## DETAILED DESCRIPTION OF EMBODIMENTS

- classify neuroendocrine neoplasm (NEN) in a subject
- generate reference miRNA expression profiles for multiple NEN pathological types
- identify candidate category and type specific miRNAs for classification
- develop multilayer classifier for discriminating NEN pathological types
- compare multiple NEN pathological types and site-matched non-NEN controls
- employ advanced computational approaches for miRNA feature selection and classifier construction
- assess data reliability through knowledge of miRNA cluster composition
- evaluate classifier performance and transferability
- determine impact of miRNA cluster substitutions on accuracy
- assess abundance of selected classificatory miRNAs
- use miRNA clusters as a measure of data quality and transferability
- build streamlined NEN classification tool
- determine expression levels of at least two selected miRNAs in a biological sample
- subject expression levels to a discriminator function that classifies cancer
- construct discriminator function with multi-layer classifiers
- provide methods and discriminator constructs for discriminating between two or more conditions of interest
- preprocess data to improve overall rigor of the discriminator function
- implement hierarchical classification for each condition of the multiple conditions of interest

### ABBREVIATIONS

- define abbreviations used throughout the description

### EXAMPLE 1

- describe study design and clinical materials
- outline RNA isolation and quantitation
- detail small RNA sequencing and sequence annotation
- explain data preprocessing and filtering
- perform unsupervised hierarchical clustering
- assess and compare abundant miRNAs in NEN and non-NEN samples
- discover miRNA-based NEN classification
- construct and cross-validate multilayer classifier

### RESULTS

- describe anatomical distribution and histopathological diagnoses of study samples
- detail small RNA sequencing of study samples
- analyze abundant miRNA composition in NEN and non-NEN samples
- compare abundant miRNAs in NEN and non-NEN samples
- perform unsupervised hierarchical clustering of filtered miRNA expression profiles
- discover miRNA-based NEN classification
- construct and cross-validate multilayer classifier
- assess classifier performance and transferability
- detect histological misidentification by miRNA-based NEN classifier

### DISCUSSION

- discuss unsupervised hierarchical clustering of filtered miRNA expression profiles
- motivate miRNA markers for NEN diagnosis
- identify similarities in abundant miRNA composition between NEN samples
- identify differences in abundant miRNA composition between NEN and non-NEN samples
- propose miR-375 as a universal marker of neuroendocrine cell differentiation
- describe feature selection algorithm for identifying 17 miRNAs to discriminate 15 NEN pathological types
- evaluate classifier performance and transferability

### EXAMPLE 2.

- preprocess expression data for miRNAs in a biological sample
- determine NEN or non-NEN using miR-375 and miR-7 in a LDA classifier
- determine non-epithelial or epithelial using miR-10b and miR-200a as input for the cubic SVM classifier
- classify NEN samples into specific pathological types using a hierarchical classifier

### EXAMPLE 3

- collect and process plasma, serum, and/or other biofluids from NEN patients and non-NEN controls
- isolate and quantify total extracellular RNA (exRNA) from biofluids
- perform extracellular RNA sequencing and sequence annotation
- preprocess and filter data to remove lowly expressed miRNAs and batch effects
- perform unsupervised hierarchical clustering of filtered miRNA expression profiles
- construct and cross-validate a multilayer classifier for NEN liquid diagnostics

### EXAMPLE 4

- measure miR-375 in NEN patient plasma using real-time quantitative polymerase chain reaction
- demonstrate utility of miR-375 as a circulating marker of NEN tumor burden

## EQUIVALENTS

- acknowledge variations in embodiments

