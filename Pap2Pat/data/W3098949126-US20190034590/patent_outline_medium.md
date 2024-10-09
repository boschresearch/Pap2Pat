# DESCRIPTION

## BACKGROUND

- motivate need for efficient information management
- discuss limitations of traditional predictive models

## RELATED ART

- summarize adoption of electronic health records
- discuss limitations of existing predictive models

## SUMMARY

- introduce system for predicting and summarizing medical events
- describe computer memory storing aggregated EHRs
- describe conversion of EHRs into standardized format
- describe training of deep learning models
- describe prediction of future clinical events
- describe summarization of pertinent past medical events
- describe provider-facing interface
- describe display of predicted events and related medical events
- describe attention mechanism
- describe display of attention mechanism results
- describe ensemble of deep learning models
- describe LSTM model
- describe time-aware feed-forward model
- describe embedded boosted time-series model
- describe possible predictions of future clinical events
- describe display of key medical problems and notes
- describe inferred information and timeline of risk
- describe selection of key problems and display of related information
- describe system and method for generating training data

## DETAILED DESCRIPTION

### A. Overview

- introduce EHR data configuration method
- motivate deep learning for predictive models
- describe technical feasibility and clinical utility
- summarize predictive models for clinical tasks
- describe provider-facing user interface
- illustrate system for predicting medical events
- describe system components

### B. Consolidation of Electronic Health Records into a Single Format for Model Generation

- describe raw EHR data formats
- convert raw data into standardized format
- arrange data in chronological order
- describe data sets used for model development
- detail EHR dataset contents
- describe data de-identification and encryption

### C. Deep Learning Models for Predicting Health Events from Medical Records

- introduce deep learning models for predicting health events
- describe system architecture
- explain use of attention mechanisms
- motivate use of three different models
- describe Long-Short-Term Memory (LSTM) model
- describe time-aware Feed-Forward Model (FFM)
- describe embedded boosted time-series model
- explain prediction tasks
- define inpatient mortality prediction task
- define long length of stay prediction task
- define 30-day unplanned readmission prediction task
- define diagnoses prediction task
- describe inclusion and exclusion criteria
- explain model design and training
- describe embedding vectors
- illustrate FFM model architecture
- illustrate embedded boosted time-series model architecture
- illustrate LSTM model architecture
- describe alternative models
- explain attention mechanism visualization
- illustrate attention mechanism results
- describe model performance
- summarize findings
- discuss limitations
- describe potential future applications

### D. Provider Interface for Clinical Predictions and Understanding Through Deep Learning

- present predictions and relevant past medical events to healthcare provider
- display alert for predicted clinical events
- provide interface for exploring risks/probabilities and past medical events
- display problem list, laboratory results, medical notes, and vital signs
- visualize timelines of prior hospital admissions, ER visits, and outpatient activity

### Example 1—What Happens Today without the Benefit of this Disclosure

- describe patient care without the benefit of the present disclosure
- illustrate difficulty in patient care without the benefit of the present disclosure
- describe patient's symptoms and medical history
- illustrate physician's thought process and decision-making
- describe consequences of delayed diagnosis and treatment
- highlight need for improved patient care

### Example 2—Predicted Clinical Event of ICU Transfer and Delayed Discharge

- illustrate benefits of the system in the treatment of the patient
- describe physician's use of the interface to track data and risks
- explain how the system alerts the physician's attention early
- describe how the system helps the physician understand the patient's current condition
- illustrate how the system summarizes past medical events for the predicted current risk
- highlight how the system improves patient care

### Example 3—Outpatient Alerts of Risk of ER or Hospitalization

- describe use of the system in an outpatient setting
- illustrate how the system predicts risk of ER visit/hospitalization and presents relevant information

### Example 4—A Busy Emergency Department

- illustrate use of the features of this disclosure in an emergency department setting

