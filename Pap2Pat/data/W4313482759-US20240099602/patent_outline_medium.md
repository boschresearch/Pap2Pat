# DESCRIPTION

## FIELD

- define field of disclosure

## BACKGROUND

- motivate diagnosis and treatment of epilepsy

## DETAILED DESCRIPTION

- introduce seizure onset zone (SOZ) localization problem in children with Drug Resistant Epilepsy (DRE)
- propose novel SOZ localization algorithm (EPIK) for children with DRE

### Introduction and Technical Problems

- describe limitations of current surgical treatment for DRE
- discuss brain imaging techniques for pre-surgical screening
- highlight drawbacks of manual sorting of independent components (IC) in resting state functional magnetic resonance imaging (rs-fMRI)
- emphasize need for automated, accessible, and accurate SOZ localization

### Proposed Solution to Technical Problems

- describe functional MRI (fMRI) based screening for SOZ detection
- explain independent component analysis (ICA) for decoupling effects of noise, RSN, and SOZ in rs-fMRI signals
- discuss limitations of manual sorting of ICs in rs-fMRI
- introduce automation of fMRI-based screening for SOZ localization
- summarize recent works on automated classification of rs-fMRI ICs
- highlight challenges in automated approaches for pediatric DRE patients
- describe differences between EPIK and supervised machine learning (ML) approaches
- illustrate EPIK's unsupervised technique for identifying SOZ localizing ICs
- compare EPIK with prior ML approaches
- hypothesize EPIK's performance in pediatric DRE population

### Materials and Methods

- define inclusion criteria for patients
- describe data collection method
- outline rs-fMRI data acquisition protocol
- detail rs-fMRI pre-processing steps
- explain expert RS-fMRI evaluation methodology
- categorize ICs into noise, RSN, and SOZ
- describe EPIK method for noise IC classification
- detail voxel cluster detection algorithm
- explain brain boundary/periphery detection
- describe white matter detection
- detail blood vessel detection
- outline noise IC classification
- describe BOLD signal feature extraction
- explain likelihood-based classification for SOZ ICs
- outline DL strategy for SOZ localization

### Overall Identification Results

- compare performance of EPIK with LS-SVM and CNN approaches

### Performance Variation with Age and Gender

- analyze variation of performance metrics with age and gender

### Performance on Subjects Undergoing Surgery

- evaluate performance of EPIK and LS-SVM on subjects undergoing surgery

### Reduction in IC Sorting Effort for the Neurosurgeon/Neurologist

- quantify reduction in IC sorting effort for neurosurgeon/neurologist

### Discussion

- discuss strengths and limitations of EPIK method

### Additional Directions

- specify study limitations
- propose future study on sedation effect
- suggest alternative methods for reducing head motion
- motivate integration of live motion monitoring
- summarize EPIK results
- highlight EPIK advantages
- describe EPIK performance across age groups
- compare EPIK with shallow and deep learning systems
- illustrate computing device configuration
- describe computing device components
- explain computer-readable media
- detail user interface and input devices
- describe networked and cloud-computing environment
- define hardware-implemented module

