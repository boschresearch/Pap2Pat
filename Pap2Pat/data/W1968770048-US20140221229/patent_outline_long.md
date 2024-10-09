# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define metastatic gene signatures

## BACKGROUND ART

- describe prostate cancer statistics
- discuss limitations of current prediction methods
- motivate need for robust risk model

## SUMMARY OF THE DISCLOSURE

- introduce method for determining metastasis risk
- define metastatic gene signature set
- describe embodiment with top 80 genes
- describe embodiment with top 40 genes
- describe embodiment with top 20 genes
- describe embodiment with top 12 genes
- explain copy number alteration determination
- describe correlation between copy number and metastasis risk
- introduce diagnostic kits for performing method

## DETAILED DESCRIPTION

- introduce risk model for predicting metastasis
- describe development of metastatic gene signature set
- summarize predictive accuracy of risk model

### Metastatic Gene Signature

- introduce metastatic gene signature set
- describe development of signature set from 294 primary prostate tumors and 49 prostate metastases
- identify 368 copy number alterations associated with metastasis
- define "clump" and "genomic region"
- describe Table 6
- introduce smaller metastatic gene signature sets
- describe top 80 genes and genomic regions
- describe top 40 genes and genomic regions
- describe top 20 genes and genomic regions
- describe top 12 genes and genomic regions
- define "non-overlapping" genes
- describe hierarchy of genes contributing to prediction
- introduce CDH13, CDH8, CDH2, and other genes
- describe direction of copy number alterations
- introduce PP3CC genomic region
- describe SLCO5A1 genomic region
- describe KCNB2 genomic region
- describe KCNH4 genomic region
- describe JPH1 genomic region
- describe NCALD genomic region
- describe YWHAG gene
- describe SLC7A5 genomic region
- describe CRISPLD2 genomic region
- describe other genes and genomic regions

### Determination of Risk

- introduce determination of risk of metastasis
- describe correlation of copy number alterations with risk
- introduce metastatic potential score
- describe formula for metastatic potential score
- describe logistic adjusted Z-scores
- describe reference distribution of samples
- introduce odds ratio for progression to metastasis
- describe significance of increase in metastatic potential score
- describe importance of predictor for diagnosis and treatment
- describe potential for individually tailored therapies
- describe potential for assessing intermediate endpoints
- describe potential for guiding development of therapies

### Diagnostic Kits

- introduce diagnostic kits for performing methods

## EXAMPLES

- introduce examples of predictive metastasis model

### Example 1

- describe predictive biomarkers
- introduce copy number alterations (CNAs) in prostate cancers
- describe sample processing (NYU cohort)
- outline study design
- describe metastasis prediction model statistics
- introduce case and control samples
- describe primary tumor and metastasis samples
- outline analytical pipeline
- describe copy number profile creation
- introduce weighted Z-score algorithm

### Example 2

- describe analytical pipeline for metastatic potential clinical risk model
- introduce copy number amplification and deletion events
- describe bootstrap clustering method
- outline quantitative copy number differences
- introduce enrichment score calculation
- describe relative enrichment modeling
- outline probe score aggregation
- describe Z-score calculation
- introduce Z-adjust transformation
- describe weighted-Z scoring risk model
- outline metastatic prediction risk model score calculation

### Example 3

- describe metastatic potential score distributions
- introduce significant differences in metastatic potential score
- describe lymph node positive primary tumors
- outline control primary tumors
- describe cross-validation analysis
- introduce Kaplan-Meier analysis
- describe biomarker functional significance
- outline molecular functions related to metastasis
- describe heat map of CNA events
- introduce mid-risk region
- describe genes within amplified or deleted regions
- outline solute carrier family SLC7A5 gene
- describe Cadherin family members
- introduce potassium channels
- outline BCL-2 and potassium channel transcription
- describe complete set of metastasis signature genes

### Example 4

- describe ranking metastasis genes on predictability
- introduce simulations to identify genes maximizing prediction accuracy
- outline non-parametric ranking method
- describe performance evaluation using extending window

### Example 5

- describe reporting prediction to patients
- introduce Cox proportional hazards ratio model
- outline Kaplan-Meier analysis of metastasis-free survival

### Example 6

- introduce Duke cohort
- process tissue samples
- validate MPS score

