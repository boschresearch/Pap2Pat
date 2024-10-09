# DESCRIPTION

- introduce disease-modifying antirheumatic drug (DMARD)
- motivate precision medicine approach
- limitations of current treatment methods
- summarize results of study on plasma lipid mediator concentrations
- explain significance of specialized pro-resolving mediators (SPMs)
- describe biosynthesis of SPMs
- suggest uncoupling of SPM biosynthetic pathways

## SUMMARY OF THE INVENTION

- outline method for assessing DMARD efficacy
- outline methods for predicting rheumatoid arthritis pathotype and DMARD response

## DETAILED DESCRIPTION OF THE INVENTION

- define method of assessing efficacy of DMARD
- introduce patients and diseases
- motivate inflammatory conditions
- specify rheumatoid arthritis
- describe advantages of personalized medicine
- introduce DMARDs
- list biological DMARDs
- list non-biological DMARDs
- describe methotrexate
- describe side effects of methotrexate
- describe sulfasalazine
- describe side effects of sulfasalazine
- describe hydroxychloroquine
- describe side effects of hydroxychloroquine
- describe leflunomide
- describe side effects of leflunomide
- describe azathioprine
- describe side effects of azathioprine
- introduce SPMs
- describe function of SPMs
- list EPA metabolites
- list n-3 DPA metabolites
- list AA metabolites
- list DHA metabolites
- describe measuring SPM
- specify D-series resolvins
- specify E-series resolvins
- list specific SPMs to be measured
- describe combinations of SPMs to be measured
- introduce method for measuring SPM levels
- describe measuring SPM levels in biological samples
- define DMARD responders and non-responders
- classify patients as DMARD responders or non-responders
- describe measuring ALOX5 and ALOX15-derived mediators
- describe measuring ALOX5-derived products of EPA
- describe measuring ALOX5-derived products of AA
- define samples as patient samples or biological samples
- describe obtaining samples prior to treatment
- describe sample collection
- describe treating samples with anticoagulant
- describe storing samples in organic solvent
- describe adding deuterium-labelled standards to samples
- describe measuring SPM levels using LC-MS/MS
- describe extracting SPMs from samples
- describe adding internal labelled standards to samples
- describe confirming SPM identity using retention time and diagnostic ions
- describe quantitating SPM levels using linear regression curves
- describe measuring SPM levels using immunoassay
- describe using homogeneous or heterogeneous immunoassay
- describe using labelled antibodies in immunoassay
- describe using surface-bound antibodies in immunoassay
- describe using competitive or non-competitive immunoassay
- describe using enzyme immunoassay (EIA)
- describe using ELISA immunoassay
- describe miniaturizing immunoassay on microfluidics device
- describe measuring SPM levels using device with internal channel
- describe detecting SPM or primary antibody using secondary antibody
- describe using microfluidics device for measuring SPM levels
- describe assessing efficacy of DMARD
- describe comparing SPM levels before and after DMARD administration
- describe increase in SPM level as indicative of DMARD efficacy
- describe decrease in SPM level as indicative of DMARD ineffectiveness
- describe expressing increase as percentage or fold change
- describe using terms "indicates" and "indicative" in assessing efficacy
- describe replacing terms with "determine" and "predict"
- describe classifying patients as DMARD responders or non-responders
- introduce DMARD efficacy assessment
- compare SPM levels before and after DMARD administration
- find difference in SPM levels before and after DMARD administration
- determine DMARD efficacy based on SPM levels
- determine DMARD ineffectiveness and modify treatment
- assess DMARD efficacy using multivariate analysis
- assess DMARD efficacy using machine learning model
- create SVM model using ClassyFire
- train SVM model using training data
- validate SVM model using validation cohort
- create random forest model using randomForest package
- train random forest model using training data
- validate random forest model using validation cohort
- input SPM levels into machine learning algorithm
- output DMARD efficacy based on machine learning algorithm
- treat inflammatory conditions including rheumatoid arthritis
- modify patient treatment based on DMARD efficacy
- terminate ineffective DMARD treatment
- start alternative DMARD treatment
- change DMARD dose
- combine DMARD with different DMARD
- predict rheumatoid arthritis pathotype
- measure SPM levels in DMARD-naive patient sample
- classify rheumatoid arthritis pathotype
- compare SPM levels with control
- identify Pauci-immune-fibroid pathotype
- classify rheumatoid arthritis pathotype using multivariate analysis
- classify rheumatoid arthritis pathotype using machine learning model
- input SPM levels into machine learning algorithm
- output rheumatoid arthritis pathotype
- select treatment based on rheumatoid arthritis pathotype
- administer selected treatment
- predict response to DMARD treatment
- measure SPM levels in DMARD-naive patient sample
- classify patient as DMARD responder or non-responder
- measure specific SPMs
- measure pro-inflammatory eicosanoids
- measure markers of ALOX5, ALOX12, and ALOX15 activity
- perform chiral analysis of markers
- predict DMARD response based on SPM levels and markers
- define ALOX5 markers
- describe measurement of ALOX5 markers
- define ALOX12 markers
- describe measurement of ALOX12 markers
- define ALOX15 markers
- describe measurement of ALOX15 markers
- describe method for predicting DMARD response
- define classifying patient as DMARD responder/non-responder
- describe method for diagnosing DMARD response
- describe increase in SPM levels
- describe fold change in SPM levels
- describe multivariate analysis for DMARD response
- describe machine learning model for DMARD response
- describe training machine learning model
- describe differential gene expression analysis
- describe comparing SPM levels to controls
- describe control samples
- describe control database
- describe classifying patient as DMARD responder/non-responder
- describe selecting treatment for patient
- describe administering treatment to patient
- describe comparing SPM levels to controls
- describe integrating DMARD response prediction with pathotype prediction
- describe method for predicting DMARD response and pathotype
- describe computer implementation of methods
- describe computer program for assessing DMARD efficacy
- describe computer apparatus for assessing DMARD efficacy
- describe computer implemented method for predicting pathotype
- describe computer apparatus for predicting pathotype
- describe advantages of invention
- describe clinical laboratory use of invention
- describe pharmaceutical use of invention
- describe preferred features of invention
- describe examples and drawings of invention
- conclude description of invention

### Example 1—Plasma SPM Concentrations are Predictive of Responsiveness to DMARD Treatment in RA Patients

- introduce study objective
- describe patient selection and characteristics
- outline lipid mediator profiling methodology
- identify mediators from four essential fatty acid metabolomes
- apply OPLS-DA to assess differences in mediator concentrations
- use random forests to build models predicting treatment responsiveness
- evaluate model performance using ROC curves
- validate model using second cohort of patients
- conduct lipid mediator pathway analysis
- assess ALOX enzyme activity and protein translation
- measure plasma levels of monohydroxylated fatty acids
- conduct chiral analysis of monohydroxylated fatty acids
- summarize findings on SPM concentrations and DMARD responsiveness

### Example 2—Baseline RvD4, 10S, 17S-diHDPA, 15R-LXA4, MaR1n-3 DPA Concentrations are Predictive of DMARD-Treatment Outcome in RA Patients

- conduct random forest "importance" analysis
- identify key lipid mediators predicting treatment responsiveness
- build machine-learning models using identified mediators
- validate model performance using separate patient cohort

### Example 3— Pre-Treatment Lipid Mediator Profiles Identify Distinct Disease Pathotypes

- introduce concept of disease pathotypes in RA
- conduct lipid mediator profiling in patients with different pathotypes
- apply PLS-DA to identify distinct lipid mediator profiles
- assess variable importance in projection (VIP) scores
- identify upregulated pro-resolving mediators in Pauci-immune-fibroid pathotype
- summarize findings on lipid mediator profiles and disease pathotypes

### Example 4—Increased SPM in DMARD-Responders when Compared to Non-Responders 6 Months after Treatment

- introduce study objective
- conduct OPLS-DA analysis of lipid mediator profiles
- identify differentially expressed mediators between responders and non-responders
- assess VIP scores to identify key mediators
- identify upregulated SPM in responders
- assess ALOX enzyme activity and substrate conversion
- measure plasma levels of monohydroxylated fatty acids
- conduct chiral analysis of monohydroxylated fatty acids
- summarize findings on SPM concentrations and DMARD responsiveness

### Example 5—SPM Mediate the Protective Actions of MTX in Experimental Inflammatory Arthritis

- introduce study objective
- incubate human whole blood with MTX and assess SPM production
- administer MTX to mice and assess SPM production and joint disease activity
- test whether ALOX15 is required for MTX-mediated joint protection
- summarize findings on SPM and MTX-mediated joint protection

### Example 6— Activation of p-300 and MAPK by MTX Increases SPM Production and Protects During Experimental Inflammatory Arthritis

- implicate signalling pathways
- relate pathways to ALOX15 expression
- investigate MTX-induced upregulation of SPM
- test inhibitors of CBP/p300 and MAPK
- assess anti-arthritic actions of MTX
- conclude MTX regulates ALOX15 activity

### Example 7— Summary of Suitable Sample Processing Method

- collect plasma samples
- add deuterium labelled internal standards
- precipitate proteins
- perform solid phase extraction
- dry methyl formate fractions
- suspend products in water-methanol
- operate LC-MS-MS
- develop MRM method
- monitor lipid mediators
- identify lipid mediators
- obtain calibration curves
- measure lipid mediator levels
- compare to established database
- list materials
- describe LC-grade solvents
- describe Poroshell 120 EC-C18 column
- describe C18 SPE columns
- describe synthetic standards
- describe deuterated internal standards
- describe methotrexate
- describe Dulbecco's Phosphate-Buffered Saline
- describe Whole Blood Lysing Reagent Kit
- describe Pathobiology of Early Arthritis Cohort
- describe patient recruitment
- describe patient treatment
- separate data by pathotype
- build classification models
- calculate statistic scores
- determine statistical differences
- construct lipid mediator biosynthesis networks
- illustrate pathways
- obtain plasma samples
- extract samples using solid-phase extraction
- add deuterated internal standards
- quantify lipid mediators
- collect blood from healthy volunteers
- incubate whole blood with inhibitors
- procure mice
- initiate inflammatory arthritis
- administer MTX or vehicle
- monitor clinical scores
- extract RNA from whole blood
- perform RNA sequencing
- analyze differential gene expression
- isolate leukocytes from paws
- stain and analyze cells using flow cytometry
- perform statistical analysis

