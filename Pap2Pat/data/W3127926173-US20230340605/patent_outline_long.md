# DESCRIPTION

## FIELD OF THE INVENTION

- relate to biomarkers for predicting clinical response of VEGF-A inhibitory drug

## BACKGROUND

- introduce anti-angiogenic treatment
- describe VEGF-A as signaling molecule
- discuss importance of VEGF-A pathway in cancer cell growth
- introduce bevacizumab as anti-angiogenic agent
- summarize benefits of anti-VEGF-A therapies
- highlight limitations of bevacizumab treatment
- discuss need for novel biomarkers
- introduce plasma VEGF-A as biomarker
- summarize MERiDiAN trial results
- discuss other biomarkers at various molecular levels
- highlight need for improved methods for selecting biomarkers
- discuss drawbacks of existing methods

## SUMMARY

- define present invention
- introduce in vitro method for predicting response to VEGF-A inhibitory drug
- describe steps of method
- introduce ViRP score calculation
- discuss various embodiments of method
- introduce second aspect of invention
- describe method for treatment of solid malignant tumor
- discuss various embodiments of treatment method
- introduce third aspect of invention
- describe kit for use in method
- introduce fourth aspect of invention
- describe method for identifying other predictive signatures
- highlight novel approach of method
- introduce fifth aspect of invention
- describe composition comprising VEGF inhibitor drug
- discuss embodiment of composition

## DETAILED DESCRIPTION

- define method for predicting response to VEGF-A inhibitory drug
- introduce term "responsive to VEGF-A inhibitory drug"
- explain response evaluation criteria for solid tumors (RECIST)
- describe obtaining cancer cell samples from patients
- specify types of solid malignant tumors
- describe collecting and preserving gene-specific polynucleotides or proteins
- list types of tissue samples that can be used
- describe analyzing samples by measuring expression levels of genes
- list mRNA quantification methods
- list protein quantification methods
- describe normalizing measured values
- explain endogenous control
- describe global normalization
- introduce ViRP (VEGF inhibitory Response Predictor) signature
- describe calculating ViRP-score
- explain phosphorylated protein measurements
- describe normalizing Moleculei
- list housekeeping genes for normalization
- describe using RNAseq quantification
- describe using RPPA quantification
- introduce cutoff value for ViRP-score
- describe determining cutoff value using ROC curves
- explain using ViRP-score in treatment strategies
- describe advantages of the method
- introduce predictor model
- describe two-step process for selecting biomarkers
- explain using official gene and protein identifiers
- describe generating ViRP cutoff value
- explain using ViRP-score to predict response to treatment
- describe treatment regimens
- introduce neoadjuvant treatment setting
- introduce adjuvant treatment setting
- describe chemotherapy
- introduce anti-VEGF-A antibody
- describe relative importance of proteins
- model protein combinations

### Treatment Regimen

- describe neoadjuvant treatment setting
- describe adjuvant treatment setting
- introduce chemotherapy
- introduce anti-VEGF-A antibody
- describe NeoAVA study
- describe PROMIX study

### Relative Importance of Proteins and Modelling of Protein Combinations

- rank relative importance of proteins
- describe combining proteins in all possible configurations
- analyze protein signature score models

## EXAMPLES

- illustrate identification of ten protein prognostic signature

### Example 1: Identification of Ten Protein Prognostic Signature

- introduce patient cohort
- describe patient characteristics
- outline treatment arms
- explain primary endpoint analysis
- discuss clinicopathological characteristics
- introduce protein expression profiling by RPPA
- describe sample processing
- outline protein expression profiling
- explain data normalization
- introduce statistical analysis
- describe significance testing
- outline Fisher's exact test
- develop molecular signature predicting response to treatment
- filter out low variance proteins
- perform adaptive Lasso-regression
- determine penalty parameter lambda
- analyze ROC curves
- develop predictive protein signature score
- reduce original panel of proteins
- apply Lasso regression
- calculate ViRP-score
- evaluate ViRP-score using pCR and RCB
- establish mRNA as surrogate
- validate protein signature in external mRNA dataset
- evaluate predictive performance of ViRP-scores
- discuss potential clinical benefit of using ViRP-score

