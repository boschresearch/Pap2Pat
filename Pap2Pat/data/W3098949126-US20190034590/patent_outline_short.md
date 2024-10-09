# DESCRIPTION

## BACKGROUND

- motivate need for efficient information management in healthcare

## RELATED ART

- summarize existing approaches to predictive modeling in healthcare

## SUMMARY

- introduce system for predicting and summarizing medical events
- describe data storage component
- describe machine learning model component
- describe provider-facing interface component
- detail aggregated health records
- describe deep learning models
- describe attention mechanisms
- describe display of results
- summarize system components

## DETAILED DESCRIPTION

### A. Overview

- introduce EHR data configuration method
- motivate deep learning application
- describe predictive models and user interface

### B. Consolidation of Electronic Health Records into a Single Format for Model Generation

- describe EHR data aggregation and conversion
- detail data sets used for model development
- explain FHIR resource conversion and data structure

### C. Deep Learning Models for Predicting Health Events from Medical Records

- introduce deep learning models for predicting health events
- describe system architecture using three models: LSTM, FFM, and embedded boosted time-series model
- motivate use of attention mechanisms in deep learning models
- describe five prediction tasks: inpatient mortality, long length of stay, 30-day unplanned readmission, diagnoses, and billing codes
- outline inclusion and exclusion criteria for study cohort
- describe model design and training process
- detail architecture of FFM, embedded boosted time-series model, and LSTM model
- describe use of attention mechanisms to visualize weights of tokens in EHR data
- illustrate attention mechanisms in patient timeline and note excerpts
- summarize model performance and results in retrospective study
- highlight four key findings: scalability, excellent predictive performance, harnessing value from full sequence of data, and interpretability
- discuss limitations of approach

### D. Provider Interface for Clinical Predictions and Understanding Through Deep Learning

- present predictions and relevant past medical events to healthcare provider
- provide interface for exploring predictions and related medical events

### Example 1—What Happens Today without the Benefit of this Disclosure

- illustrate difficulty in patient care without predictive models
- describe patient's hospitalization and treatment
- highlight mistakes made by healthcare provider

### Example 2—Predicted Clinical Event of ICU Transfer and Delayed Discharge

- illustrate benefits of predictive models in patient care
- describe interface for tracking data and risks in real time
- show how predictive models help healthcare provider understand patient's condition

### Example 3—Outpatient Alerts of Risk of ER or Hospitalization

- describe use of predictive models in outpatient setting

### Example 4—A Busy Emergency Department

- illustrate use of predictive models in emergency department

