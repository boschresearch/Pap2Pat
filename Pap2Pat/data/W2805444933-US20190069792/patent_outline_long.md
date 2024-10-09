# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- introduce atrial fibrillation
- describe catheter ablation therapy
- discuss limitations of conventional methods
- highlight need for better understanding

## SUMMARY

- introduce method for detecting abnormality
- extract features from intracardiac electrograms
- use time-frequency analysis to detect heterogeneity
- combine features to extract regional feature
- exclude irrelevant signals
- output results graphically
- identify source of cardiac atrial fibrillation
- detect change in wavefront dynamics
- determine wave break rate
- display colour-coded map

## DETAILED DESCRIPTION

- describe methods for analyzing IEGMs to determine wavefront characteristics
- introduce block diagram of FIG. 1A
- describe feature extraction and fusion
- describe time-frequency and/or time-scale analysis of regional features
- describe embodiment of study with twenty patients
- describe data collection and processing
- describe correlation of MATLAB generated maps with procedural outcomes

### 1A. Regional Dominant Frequency and Wave Break Rate

- describe calculation of electrode dominant frequency (EDF)
- describe preprocessing of IEGMs
- describe calculation of regional dominant frequency (RDF)
- describe preprocessing steps for RDF calculation
- describe calculation of instantaneous RDF (iRDF)
- describe calculation of upper quartile of iRDF
- describe selection of time window T
- define wave break (WB) and wave break rate (WBR)
- describe calculation of WBR
- describe use of WBR as a feature to characterize wavefront propagation

### 1B. Example of RDF-Based Wave Break Identification

- describe example of RDF-based wave break identification
- illustrate example with plots of IEGMs and processing outputs

### 1C. Minimum Required Segment Duration for Accurate RDF Estimation

- describe aim to find minimum segment duration for accurate RDF estimation
- describe results of analysis and conclusion

### 1D. Minimum Required Segment Duration for Accurate WBR Estimation

- describe results of analysis and conclusion

### 1E. Statistics

- describe statistical methods used

### 1F. Implementation

- describe implementation of embodiments in software
- describe data processing system
- describe user interface
- describe input device
- describe central processing unit (CPU)
- describe memory
- describe display device
- describe interface device
- describe network connections
- describe database system
- describe computer executable programmed instructions
- describe graphical user interface (GUI)

### 1G. Results

- exclude patients due to poor data quality
- describe patient demographics
- summarize procedural duration
- report recording locations and duration
- administer Ibutilide to patients
- select segments for RDF and WBR estimation
- calculate RDF and WBR for all patients
- compare RDF and WBR for paroxysmal and persistent patients
- show scatter plot and histograms of WBR and RDF
- describe ablation results and termination sites

### 1H. Discussion

- introduce novel metric for AF investigation
- describe regional dominant frequency
- discuss advantages over traditional methods
- explain wave break rate quantification
- associate termination sites with wavefront dynamics
- discuss spatial distribution of WBR and RDF
- propose WBR as a feature for ablation target
- discuss data collection and regional features
- describe critical sites and evaluation methods
- discuss limitations and future directions

## 2. Computer Modelling of Spiral Rotor and Associated Wave Break Analysis

- simulate cardiac cells using computer model
- generate spiral rotor using modified FitzHugh-Nagumo model
- calculate unipolar and bipolar electrograms
- analyze iRDF-drop or WB using simulated electrograms

## 3. Clinical Example of an Identified Rotor During Wave Break

- illustrate rotational activity observed during wave break using propagation map

## EQUIVALENTS

- describe scope of invention

