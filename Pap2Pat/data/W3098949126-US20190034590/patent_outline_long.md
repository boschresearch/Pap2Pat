# DESCRIPTION

## BACKGROUND

- motivate need for efficient information management
- describe limitations of current information management
- highlight importance of attention allocation
- introduce predictive models for healthcare

## RELATED ART

- describe adoption of electronic health records
- discuss limitations of current predictive models
- highlight importance of data quality
- introduce machine learning for healthcare
- describe existing predictive models

## SUMMARY

- introduce system for predicting medical events
- describe aggregated electronic health records
- convert records to standardized format
- execute deep learning models
- predict future clinical events
- summarize pertinent past medical events
- describe provider-facing interface
- display predicted events and past medical events
- highlight attention mechanism results
- describe ensemble of deep learning models
- introduce LSTM model
- introduce time-aware feed-forward model
- introduce embedded boosted time-series model
- predict unplanned transfer to ICU
- predict length of stay in hospital
- predict unplanned hospitalization
- predict ER visit or readmission
- predict inpatient mortality
- predict primary diagnosis
- predict complete set of billing diagnoses
- predict atypical laboratory values
- describe attention mechanism
- display attention mechanism results
- highlight pertinent past medical events
- describe electronic device interface
- display predicted events and past medical events
- display inferred information
- display timeline of risk or probability
- permit user selection of key problems
- display further information on selected key problem
- describe system for predicting medical events
- aggregate electronic health records
- convert records to standardized format
- execute deep learning models
- predict future clinical events
- summarize pertinent past medical events
- describe method for generating training data
- describe method for predicting medical events

## DETAILED DESCRIPTION

### A. Overview

- introduce EHR data configuration method
- motivate deep learning for predictive models
- describe advantages of deep learning
- summarize applications of deep learning
- describe technical feasibility and clinical utility
- introduce predictive models for clinical tasks
- describe applications of predictive models
- introduce provider-facing user interface
- describe system components
- introduce computer memory for EHR storage
- describe EHR conversion process
- introduce deep learning models for prediction
- describe electronic device for healthcare provider
- introduce method for predicting medical events
- outline method steps

### B. Consolidation of Electronic Health Records into a Single Format for Model Generation

- describe raw EHR data formats
- motivate standardization of EHR data
- introduce converter for EHR standardization
- describe FHIR format for EHR standardization
- outline EHR data anonymization process
- describe data sets used for model development
- introduce UCSF, UCM, and MIMIC-III datasets
- describe Uranus claims dataset
- outline data de-identification process
- describe ethics review and institutional review board exemption
- introduce sandboxing infrastructure for data separation
- describe FHIR resource conversion process

### C. Deep Learning Models for Predicting Health Events from Medical Records

- introduce deep learning models for predicting health events
- describe system architecture
- explain use of three different models
- motivate attention mechanisms
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
- describe use of embeddings
- describe FFM architecture
- describe LSTM architecture
- describe embedded boosted time-series architecture
- explain attention mechanisms in FFM
- explain attention mechanisms in LSTM
- explain attention mechanisms in embedded boosted time-series
- describe baseline models
- explain statistical analyses
- describe alternative models
- introduce attention visualization
- describe display of attention results
- explain ranking of past medical problems
- describe generation of attention results
- explain use of attention mechanisms in provider-facing interface
- describe performance metrics
- summarize results of retrospective study
- describe scalability of results
- describe predictive performance across tasks
- compare results to existing literature
- describe modeling of full sequence of data
- describe interpretability of complex models
- discuss limitations of approach
- describe potential for overfitting
- describe use of held-out test set
- describe potential applications of models
- describe prediction of medications and dosages
- describe prediction of next words in physician notes
- describe prediction of life-threatening events
- describe prediction of physiological deterioration
- describe prediction of total cost of care
- describe prediction of admissions and census
- describe use of models for real-time prediction
- describe use of models for personalized medicine
- describe potential for models to improve healthcare outcomes
- conclude description of deep learning models

### D. Provider Interface for Clinical Predictions and Understanding Through Deep Learning

- describe provider interface for clinical predictions
- illustrate healthcare provider-facing interface for use in hospital setting
- display alerts for predicted clinical events
- provide graphical display of probabilities of different outcomes
- explain predictions with relevant past medical events
- display problem list associated with alerts
- show current laboratory results
- highlight key elements in medical notes
- display timelines of prior hospital admissions and outpatient activity
- illustrate intensity of healthcare utilization

### Example 1—What Happens Today without the Benefit of this Disclosure

- introduce hypothetical patient example
- describe patient's symptoms and hospital admission
- illustrate difficulties in patient care without predictive models
- describe physician's thought process and decision-making
- highlight importance of timely diagnosis and treatment
- illustrate consequences of delayed diagnosis and treatment
- describe patient's medical history and conditions
- highlight importance of considering multiple factors in diagnosis
- illustrate limitations of current healthcare system
- describe need for improved patient care
- highlight benefits of predictive models in patient care
- illustrate how predictive models can improve patient outcomes
- conclude example with need for improved patient care

### Example 2—Predicted Clinical Event of ICU Transfer and Delayed Discharge

- introduce hypothetical patient example
- describe predictive models and interface
- illustrate alerts for predicted clinical events
- explain predictions with relevant past medical events
- display problem list associated with alerts
- show current laboratory results
- highlight key elements in medical notes
- display timelines of prior hospital admissions and outpatient activity
- illustrate intensity of healthcare utilization
- describe physician's thought process and decision-making
- highlight benefits of predictive models in patient care
- conclude example with improved patient outcomes

### Example 3—Outpatient Alerts of Risk of ER or Hospitalization

- introduce hypothetical patient example
- describe predictive models and interface
- illustrate alerts for predicted clinical events
- explain predictions with relevant past medical events
- conclude example with improved patient outcomes

### Example 4—A Busy Emergency Department

- introduce hypothetical patient example
- describe predictive models and interface
- illustrate benefits of predictive models in emergency department

