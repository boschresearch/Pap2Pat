# DESCRIPTION

## FIELD OF THE INVENTION

- relate to cancer and methods for classifying patients

## BACKGROUND OF THE INVENTION

- introduce breast cancer
- describe current challenges in breast cancer treatment
- discuss recent advances in genomic characterization of tumors
- highlight need for new method to predict outcome recurrence

## SUMMARY OF THE INVENTION

- introduce laser capture microdissection (LCM) to isolate tumor-associated and matched normal stroma
- perform microarray analyses to identify gene expression signatures
- develop multivariate stromal derived prognostic predictor (SDPP)
- identify set of genes in tumor stroma predictive of outcome
- describe genes including pro-angiogenic and hypoxia-related factors
- describe genes including T-cell markers
- provide method for identifying gene expression signature
- provide method for predicting clinical outcome using SDPP
- describe method for predicting clinical outcome in breast cancer patient
- describe method for determining prognosis
- describe method for predicting disease outcome
- describe method for diagnosing poor prognosis breast cancer
- describe method for predicting probability of cancer recurrence
- describe method for predicting probability of cancer metastasis
- describe method for diagnosing tumor subtype
- describe method for assigning treatment or therapy
- describe method for optimizing treatment
- describe method for monitoring treatment
- describe method for assigning subject to clinical study
- integrate SDPP predictor with other predictors and signatures
- combine SDPP with other known predictors and signatures
- describe SDPP gene sets
- describe composition comprising nucleic acid sequences
- describe composition comprising binding agents
- describe method of identifying agents for use in treatment of cancer
- describe kits comprising nucleic acids and polypeptides
- describe arrays for detecting SDPP gene set expression levels
- describe computer systems and computer program products

## DETAILED DESCRIPTION OF THE INVENTION

- introduce breast cancer outcome predictor
- motivate stroma-derived predictor
- define stroma-derived prognostic predictor (SDPP)
- describe SDPP gene sets
- explain SDPP gene set selection
- provide examples of SDPP gene sets
- describe accuracy of SDPP gene sets
- define clinical outcome
- explain expression level of SDPP genes
- define reference expression profile
- describe sample types
- introduce class discovery
- describe class distinction
- explain class prediction
- motivate accurate prediction
- describe gene weighting
- provide method for predicting clinical outcome
- provide alternative methods for predicting clinical outcome
- describe method for identifying SDPP gene set
- provide alternative method for identifying SDPP gene set
- summarize SDPP gene set identification

### Identifying Classes and Genes for Predicting Clinical Outcome

- introduce class discovery
- describe microarray experiments
- identify top 200 most variable genes
- cluster tumor stroma
- assess cluster significance
- define class discovery
- introduce class distinction
- describe pairwise class distinction
- identify genes differentially expressed
- derive reference expression profile
- construct multivariate predictor
- train Bayes' classifiers
- describe class distinction
- define class prediction
- describe SDPP
- provide method for predicting clinical outcome
- describe gene weighting
- summarize class prediction

### Cancers

- introduce breast cancer
- describe breast cancer subtypes
- apply SDPP to breast cancer subtypes
- apply SDPP to other cancer types
- define cancer

### Nucleic Acid Compositions

- describe nucleic acid composition

### SDPP Genes and Nucleic Acids

- define SDPP gene set
- describe SDPP gene set composition
- introduce novel gene products correlating with disease outcome
- describe gene products THC2436642, A—24_P82805, ENST00000246228, and THC2269172
- define isolated nucleic acid
- describe polynucleotide sequence selection
- explain hybridization conditions
- define stringency conditions
- describe Tm calculation
- explain hybridization conditions selection
- define products of a gene of a SDPP gene set
- describe RNA and polypeptide products
- summarize SDPP gene set products

### Nucleic Acids, Primers and Probes

- describe composition of isolated nucleic acid sequences
- introduce use of primers for detecting SDPP genes
- define primer
- describe primer design for multiplex PCR
- introduce probes for detecting SDPP genes
- define probe
- describe probe design for detecting SDPP genes
- summarize probe use

### Polypeptide Binding Compositions

- describe polypeptide products of SDPP genes
- introduce composition of SDPP polypeptides
- describe polypeptide composition selection
- introduce binding agents for detecting polypeptide products
- define isolated polypeptides
- describe binding agents for detecting polypeptide products
- introduce antibodies and antibody fragments
- describe antibody production methods
- introduce peptide mimetics
- describe peptide mimetic design
- introduce binding agents fixed to a solid support
- describe ELISA plate use
- summarize polypeptide binding compositions

### Microarrays

- introduce microarrays for detecting gene expression
- describe DNA microarrays
- describe tissue microarrays
- introduce array composition
- describe array use for predicting clinical outcome
- summarize microarray use

### Methods of Diagnosis

- disclose SDPP gene sets for breast cancer subtypes
- predict breast cancer subtype based on SDPP gene expression
- predict prognosis based on SDPP gene expression
- predict recurrence based on SDPP gene expression
- predict metastasis based on SDPP gene expression
- define patient and diagnosis terms
- describe methods for detecting gene expression levels
- describe quantitative multiplex PCR method
- describe microarray method
- predict disease outcome using polypeptide products
- use antibodies to detect polypeptide products
- describe methods for determining protein product amounts
- detect multiple polypeptide gene products
- combine nucleic acid and polypeptide detection methods
- integrate with other gene sets or prognostic factors
- enhance accuracy of predicting disease outcome

### Methods of Assigning or Selecting Treatment

- assign treatment based on predicted clinical outcome
- tailor treatment for HER2 positive or negative breast cancer
- tailor treatment for ER positive or negative breast cancer
- monitor treatment efficacy using SDPP gene expression
- determine treatment effectiveness based on gene expression changes
- analyze SDPP gene sets for clinical outcome associations
- identify gene clusters associated with clinical outcome
- describe tumor associated stroma changes during breast cancer progression
- assign treatment based on transcriptional profile of tumor associated stroma
- target Th2 immune responses, angiogenesis, and hypoxic processes
- promote Th1 immune response
- inhibit Th2 immune response
- tailor treatment to biological responses activated in patient
- describe methods for identifying agents for cancer treatment
- monitor SDPP gene expression for treatment efficacy
- identify agents that inhibit hypoxia response genes
- identify agents that inhibit Th2 response genes
- identify agents that inhibit angiogenesis genes
- describe cell culture techniques for testing agents
- describe cell lines for testing agents
- identify agents that target deregulated pathways
- inhibit expression of genes associated with poor prognosis
- identify agents that promote good prognosis

## EXAMPLES

### Example 1

- describe tissue samples
- introduce laser capture microdissection
- describe RNA isolation and microarray hybridization
- identify tumor stroma subtype associated with recurrence and poor outcome
- define top 200 most variable genes
- cluster tumor associated stroma using genes
- test clusters for association with clinical variables
- identify genes differentially expressed between stroma subtypes
- construct predictor using logistic regression
- evaluate predictor using cross-validation
- compare predictor to other clinical risk factors
- perform gene ontology analysis
- compare to publicly available breast cancer datasets
- validate expression of selected genes by qRT-PCR
- analyze expression of macrophage, angiogenesis, hypoxia and immune markers
- functionally annotate unknown predictor genes
- validate protein expression by immunohistochemistry
- describe results of gene expression in breast tumor stroma
- identify clusters associated with outcome
- describe differences between good and poor outcome patient stroma
- identify genes differentially expressed between patient clusters
- cluster genes into distinct groups
- describe biological responses associated with each cluster
- analyze gene ontology of poor outcome cluster
- validate endothelial content by immunostaining
- describe matrix metalloproteinase genes
- analyze good outcome cluster
- describe Th1-type immune response
- validate CD8 and CD3Z expression by immunohistochemistry
- analyze mixed outcome cluster
- describe estrogen and androgen receptor activity
- construct stroma-derived prognostic predictor
- rank genes by independent prognostic ability
- train multivariate naive Bayes classifier
- evaluate classifier using cross-validation
- compare to other predictors
- validate expression of selected genes by qRT-PCR
- analyze performance in datasets derived from whole tissue
- test whether SDPP is an independent prognostic factor
- analyze composition of SDPP patient clusters
- perform multivariate Cox regression
- compare to previously described predictors and signatures
- analyze correlation with wound and hypoxia signatures
- compare to 70-gene predictor
- discuss biological processes reflected in SDPP
- describe immune response in good outcome cluster
- describe macrophage chemoattractants in poor outcome cluster
- analyze hypoxia-associated genes
- describe angiogenesis-related genes
- discuss integration of biological responses
- summarize SDPP as a robust predictor

### Example 2

- integrate multiple predictors
- construct Bayes' classifier
- estimate posterior probabilities
- test SDPP for added predictive value
- demonstrate increased accuracy of SDPP
- discuss interaction between biological processes
- highlight need for integrative approach

### Example 3

- describe samples
- perform LCM, RNA isolation, and microarray hybridization
- identify tumor stroma subtype associated with recurrence
- identify genes differentially expressed between subtypes
- construct predictor using logistic regression
- evaluate predictor using cross-validation
- perform gene ontology analysis
- validate protein expression using immunohistochemistry
- validate gene expression using Q-RT-PCR
- compare performance of SDPP in different tissues

### Example 4

- describe samples
- perform LCM and microarray hybridization
- identify tumor stroma subtype associated with recurrence
- identify genes differentially expressed between subtypes
- construct predictor using logistic regression
- evaluate predictor using cross-validation
- compare performance of predictor in tumor stroma and epithelium
- validate protein expression using immunohistochemistry
- test predictor in publicly available datasets
- perform survival analysis
- perform Cox proportional hazards regression
- analyze gene expression in tumor stroma
- discuss elevated angiogenic factors
- discuss decreased T-cell markers
- discuss combination of angiogenic factors and T-cell markers
- discuss implications of results

