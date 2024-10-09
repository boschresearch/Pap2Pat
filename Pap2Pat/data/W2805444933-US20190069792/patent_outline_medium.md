# DESCRIPTION

## FIELD

- define field of invention

## BACKGROUND

- describe atrial fibrillation
- limitations of current methods

## SUMMARY

- introduce method for detecting abnormality
- extract features from intracardiac electrograms
- detect spatiotemporal heterogeneity
- output results graphically
- identify source of cardiac atrial fibrillation

## DETAILED DESCRIPTION

- describe methods for analyzing IEGMs to determine wavefront characteristics
- introduce framework for extracting regional features from IEGMs
- outline application of time-frequency analysis to detect changes in wavefront dynamics

### 1A. Regional Dominant Frequency and Wave Break Rate

- extract dominant frequency of each electrode of the catheter
- calculate regional dominant frequency from preprocessed IEGMs
- describe preprocessing steps for obtaining regional dominant frequency
- calculate instantaneous RDF and upper quartile of iRDF
- define wave break and calculate wave break rate

### 1B. Example of RDF-Based Wave Break Identification

- illustrate example of RDF-based wave break identification using IEGMs from a patient with persistent AF

### 1C. Minimum Required Segment Duration for Accurate RDF Estimation

- determine minimum segment duration required for accurate RDF estimation

### 1D. Minimum Required Segment Duration for Accurate WBR Estimation

- determine minimum segment duration required for accurate WBR estimation

### 1E. Statistics

- describe statistical methods used for data analysis

### 1F. Implementation

- describe software implementation of embodiments
- outline data processing system architecture
- describe user interface and input/output devices
- discuss memory and storage hierarchy
- outline network connectivity and communication
- describe database system and storage of programming information

### 1G. Results

- present patient demographics
- describe data collection and processing
- report RDF and WBR results
- analyze correlation between RDF and WBR
- discuss ablation results and termination sites

### 1H. Discussion

- introduce novel metric for AF investigation
- describe advantages of RDF and WBR methods
- discuss association between termination sites and wavefront dynamics
- propose WBR as a feature to quantify wavefront propagation
- suggest future directions and potential applications

## 2. Computer Modelling of Spiral Rotor and Associated Wave Break Analysis

- simulate spiral rotor using FitzHugh-Nagumo model
- generate electrograms and identify wave breaks

## 3. Clinical Example of an Identified Rotor During Wave Break

- illustrate rotational activity observed during wave break

## EQUIVALENTS

- describe scope of invention

