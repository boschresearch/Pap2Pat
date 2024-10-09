# DESCRIPTION

## FIELD OF THE INVENTION

- relate to breast cancer classification

## BACKGROUND OF THE INVENTION

- introduce breast cancer statistics
- discuss detection and treatment advances
- summarize research on prognosis and therapeutic response
- describe conventional and molecular prognostic indicators

## SUMMARY OF THE INVENTION

- introduce classification and prognosis methods
- describe prediction model and compositions

## DETAILED DESCRIPTION OF THE INVENTION

### Overview

- introduce breast cancer treatment challenges
- define breast cancer
- describe breast cancer heterogeneity
- motivate gene expression profiling
- summarize intrinsic subtypes
- describe Luminal subtype
- describe ER-negative subtypes
- motivate supervised algorithm
- introduce PAM50 classification model
- describe gene selection
- define gene expression
- describe gene expression profile
- outline sample collection
- outline clinical applications

### Clinical Variables

- introduce clinical variables
- describe risk of relapse score
- outline clinical factors
- describe staging system

### Sample Source

- introduce subject samples
- describe biological samples
- outline sample collection methods
- describe breast tissue samples
- outline fixative and staining
- describe tissue sample transfer

### Expression Profiling

- introduce expression profiling
- describe pattern recognition algorithms
- outline multivariate statistical analysis
- describe supervised approach
- outline training set
- describe model evaluation
- outline cross-validation
- describe PAM50 classification model
- outline centroid-based prediction algorithm
- describe nearest centroid methodology

### Detection of Intrinsic Gene Expression

- define detecting expression
- list methods for detecting expression
- describe hybridization analysis
- describe sequencing of polynucleotides
- describe immunohistochemistry methods
- describe proteomics-based methods
- describe PCR-based methods
- describe array-based methods
- define microarray
- describe probes
- describe RNA extraction
- describe RNA isolation from paraffin-embedded tissues
- describe RNA isolation from tissue samples
- describe cesium chloride density gradient centrifugation
- describe single-step RNA isolation process
- describe hybridization or amplification assays
- describe contacting isolated RNA with a nucleic acid molecule
- describe immobilizing mRNA on a solid surface
- describe immobilizing probes on a solid surface
- describe quantitative PCR (QPCR)
- describe real-time PCR
- describe microarray technique
- describe PCR amplified inserts of cDNA clones
- describe dual color fluorescence

### Data Processing

- describe pre-processing gene expression data
- describe addressing missing data
- describe translation
- describe scaling
- describe normalization
- describe weighting
- describe mean centering
- describe unit variance scaling
- describe pareto scaling
- describe logarithmic scaling
- describe equal range scaling
- describe autoscaling
- describe Distance Weighted Discrimination (DWD)

### Calculation of Risk of Relapse

- describe predicting breast cancer outcome
- describe classifying subjects according to subtype
- describe calculating Risk Of Relapse (ROR) score
- describe using PAM50 bioinformatics model
- describe Cox Proportional Hazards Model Analysis
- describe calculating ROR using subtype distances
- describe calculating ROR using subtype distances and clinical variables
- describe using intrinsic gene list to develop prediction model
- describe constructing formula for calculating ROR
- describe calculating ROR-S using subtype distances
- describe calculating ROR-C using subtype distances and clinical variable

### Prediction of Response to Therapy

- introduce breast cancer management strategies
- motivate treatment decisions based on clinical factors
- summarize St. Gallen Conference guidelines
- introduce PAM50 model for risk stratification
- describe evaluating risk of relapse using PAM50
- motivate use of risk score for treatment decisions
- describe identifying high-risk patients for aggressive therapy
- discuss use of PAM50 with St. Gallen Conference guidelines
- introduce predicting response to therapy
- define positive and negative treatment outcomes
- discuss calculating PAM50-based risk score
- describe using proliferation-weighted PAM50 risk score

### Kits

- introduce kits for classifying breast cancer subtypes
- describe kit components: capture probes and primers
- discuss immobilizing capture probes on an array
- describe array fabrication techniques
- introduce oligonucleotide primers for detection and quantitation
- describe microplate format for primers
- discuss recording molecular signatures in a database
- define article usage and provide disclaimer

## EXPERIMENTAL

### Example 1

- describe patient cohorts
- introduce training and test sets
- detail nucleic acid extraction
- describe reverse transcription and real-time quantitative PCR
- introduce microarray
- pre-process microarray data
- identify prototypical intrinsic subtype samples and genes
- reduce gene set using prototype samples and qRT-PCR
- predict sample subtypes
- assess prognosis using clinical and molecular subtype data
- develop risk models with clinical and molecular data
- create new subtype model based on prototypical samples and genes
- distribute biological subtypes across ER positive and ER-negative tumors
- analyze subtypes and response to neoadjuvant T/FAC treatment
- predict risk based on biological subtype
- discuss PAM50 classifier
- validate PAM50 classifier
- apply PAM50 classifier to heterogeneously treated cohort
- compare PAM50 classifier to standard clinical markers
- discuss importance of molecular subtypes
- analyze HER2-enriched expression subtype
- analyze Normal-like subtype
- discuss therapeutic implications
- analyze Basal-like subtype
- discuss triple-negative phenotype
- analyze tissue microarray study
- discuss Basal-like diagnosis
- provide absolute subtype classification
- classify tumors into low-medium-high risk groups
- analyze ROR predictor
- identify LumA patients at low risk of relapse
- compare ROR predictor to OncotypeDx Recurrence Score
- discuss benefits of PAM50 based assay
- summarize subtype predictor and ROR classifier
- discuss molecular features in breast tumors
- discuss importance of prognosis and treatment
- introduce qRT-PCR assay
- discuss archived breast tissues
- discuss retrospective studies
- discuss prospective clinical trials
- conclude subtype predictor and ROR classifier
- finalize discussion

## Example 2

### Introduction and Background Data

- introduce PAM50-based intrinsic subtype classifier

### Summary

- summarize PAM50-based intrinsic subtype classifier
- describe predictive and prognostic properties
- introduce proliferation-weighted risk score
- summarize application to neoadjuvant endocrine therapy

### Methodology:

- describe National Cancer Institute sponsored Phase 2 trial
- outline gene expression analysis methods

### Results:

- describe changes in PAM50 intrinsic subtype and risk score
- summarize transitions between LumA and LumB subtypes
- correlate PAM50 proliferation weighted risk score with Ki67 values
- describe correlation between baseline and one month PAM50 risk scores
- summarize clinical correlations with PAM50 intrinsic subtype and risk score
- describe predictive properties of PAM50 intrinsic subtype and risk score
- summarize correlations with clinical response and relapse events

## Example 3

- introduce risk of relapse analysis

### Prognostic and Predictive Models Using Clinical and Molecular Subtype Data:

- describe univariate and multivariate analyses
- introduce ROR score and risk models
- summarize comparison of relapse prediction models

### Comparison of Relapse Prediction Models

- compare C-index of different models

### Risk of Relapse Models for Prognosis in Node-Negative Breast Cancer

- describe Cox models for prognosis
- summarize multivariable analyses
- describe relapse classifier and ROR model

### Subtypes and Prediction of Response to Neoadjuvant T/FAC Treatment

- describe relationship between subtypes and clinical markers
- summarize predictive properties of ROR-S model

## Example 4

- introduce study on PAM50 classifier in estrogen receptor positive breast cancer patients

### Patients:

- describe patient cohort
- outline clinical information linked to specimens
- specify patient selection criteria

### RNA Preparation:

- describe RNA isolation from pathologist-guided tissue cores
- outline RNA yield assessment and quality control

### Assignment of Biological Subtype to Clinical Samples:

- describe gene expression centroids construction and subtype assignment

### Relation of PAM50 Subtype to Clinical Outcome:

- outline statistical analyses of tumor subtype against breast cancer outcomes

### Relation of Risk-Of-Relapse (ROR) Score to Clinical Outcome:

- describe ROR score algorithm and its relation to clinical outcome

### Results

- summarize RNA extraction and PCR analysis results
- present clinical characteristics of patients
- describe PAM50 subtype assignment results
- outline Kaplan-Meier analysis results
- describe multivariate Cox model results
- present ROR score results
- outline ROR-C algorithm results
- describe interaction between ROR-C and nodal status
- present Cox model results with ROR-S
- describe comparison of qPCR and immunohistochemical subtyping
- outline concordance between qPCR and immunohistochemical subtyping
- present multivariate analysis results with qPCR and immunohistochemical subtyping
- describe Adjuvant! model predictions
- outline comparison of Adjuvant! and ROR models
- present Kaplan-Meier analysis results for Adjuvant! risk groups
- describe ROR-S results for Adjuvant! risk groups
- outline log-rank test results for ROR-S
- present Kaplan-Meier analysis results for low risk subgroup
- describe ROR-S results for intermediate risk groups
- outline ROR-S results for high risk subgroup

### Discussion

- summarize study findings
- discuss relevance of study to breast cancer treatment
- outline limitations of clinical measurements of ER and HER2 status
- describe advantages of PAM50 qPCR assay
- discuss comparison of PAM50 qPCR assay with immunohistochemical subtyping
- outline prognostic capacity of PAM50 qPCR assay
- describe identification of ER-negative biological subtypes
- discuss replacement of grade and HER2 status in multivariate models
- outline superiority of PAM50 qPCR assay over clinical risk classifiers
- describe potential applications of PAM50 qPCR assay
- discuss implications for therapeutic decision making
- outline potential benefits of PAM50 qPCR assay
- describe potential limitations of study
- discuss need for further validation of PAM50 qPCR assay
- outline future directions for research

