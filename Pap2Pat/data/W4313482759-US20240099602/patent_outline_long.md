# DESCRIPTION

## FIELD

- define field of disclosure

## BACKGROUND

- motivate epilepsy diagnosis
- highlight importance of early treatment

## DETAILED DESCRIPTION

- introduce SOZ localization algorithm (EPIK) for children with DRE
- describe phased approach of EPIK
- evaluate performance of EPIK on pediatric DRE dataset
- compare EPIK with state-of-art techniques

### Introduction and Technical Problems

- introduce epilepsy and DRE
- describe surgery for DRE
- discuss brain imaging for pre-surgical screening
- distinguish between epileptic network and SOZ
- describe various brain imaging techniques for SOZ identification
- discuss limitations of traditional analysis of PET, SPECT, or SEEG
- introduce rs-fMRI as a promising method for SOZ localization
- discuss limitations of expert interpretation of ICs
- highlight need for automated whole-brain data-driven SOZ-localizing IC identification technique

### Proposed Solution to Technical Problems

- introduce fMRI-based screening
- describe removal of noise and head motion artifacts
- explain ICA for decoupling effects of noise, RSN, and SOZ
- categorize ICs into RSN, SOZ, and noise
- describe manual sorting of ICs by neurosurgeon
- highlight limitations of manual sorting
- introduce automation of fMRI-based screening
- describe two automation objectives with rs-fMRI
- focus on SOZ localization
- discuss supervised ML and DL for automated classification of rs-fMRI ICs
- highlight limitations of current automated approaches
- discuss challenges in pediatric DRE patients
- introduce EPIK as an unsupervised technique
- describe differences between EPIK and supervised ML
- illustrate EPIK approach
- describe purging ICs with noise markers
- classify ICs into RSN and SOZ using maximum likelihood-based clustering
- highlight innovation in EPIK
- replicate shallow ML and implement CNN-based DL technique
- provide preliminary comparative study of all three approaches

### Materials and Methods

- define inclusion criteria
- describe data collection method
- outline rs-fMRI data acquisition
- detail propofol infusion for sedation
- describe inpatient video EEG and anatomical MRI
- outline MRI image acquisition parameters
- describe rs-fMRI pre-processing
- detail linear registration and ICA
- outline expert RS-fMRI evaluation methodology
- categorize ICs into noise, RSN, and SOZ
- define noise category criteria
- define RSN category criteria
- define SOZ category criteria
- describe spatial features of SOZ
- describe temporal features of SOZ
- outline EPIK method
- apply rules for IC noise markers
- describe voxel cluster detection algorithm
- detail brain boundary/periphery detection
- describe white matter detection
- describe blood vessel detection
- classify noise ICs
- describe BOLD signal feature extraction
- evaluate sparsity in activelet coefficients
- evaluate sparsity in matching pursuit
- classify SOZ ICs
- describe likelihood-based classification
- formulate optimization problem
- describe DL strategy for SOZ localization
- outline hyperparameter tuning process
- describe shallow learning strategy

### Overall Identification Results

- compare performance of EPIK with LS-SVM and CNN

### Performance Variation with Age and Gender

- evaluate variation of performance metrics with age
- evaluate variation of performance metrics with gender
- describe statistical significance of results

### Performance on Subjects Undergoing Surgery

- evaluate agreement between EPIK and expert hand classification
- compare performance of EPIK and LS-SVM
- describe ROC curve for EPIK and LS-SVM

### Reduction in IC Sorting Effort for the Neurosurgeon/Neurologist

- describe reduction in IC sorting effort

### Discussion

- discuss strengths of EPIK
- compare performance of EPIK with LS-SVM and CNN
- discuss avenues for future research

### Additional Directions

- specify evaluation metrics
- discuss sedation methods
- propose future study on sedation effects
- suggest alternative head motion reduction methods
- highlight importance of live motion monitoring
- emphasize elimination of head movement artifacts
- summarize EPIK SOZ identification accuracy
- describe time commitment reduction for neurosurgeons
- highlight unsupervised nature of EPIK
- emphasize consistent performance across age groups
- highlight validation with surgical outcomes
- compare EPIK performance to shallow and deep learning systems
- illustrate computing device configuration
- describe predictive method translation to software
- specify computing device components
- detail system bus architecture
- describe main memory components
- explain BIOS functionality
- detail data storage components
- describe user interface components
- specify input device options
- describe networked environment implementation
- detail remote device connections
- explain logical connection establishment
- describe hardware-implemented module configuration
- highlight tangible unit capabilities
- explain programmable circuitry configuration
- discuss hardware-implemented module communication

