# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce sudden cardiac death
- describe ventricular fibrillation
- discuss limitations of defibrillation
- motivate need for predicting defibrillation success
- summarize prior art in VF waveform analysis
- highlight limitations of prior art

## SUMMARY OF THE INVENTION

- introduce integrative model for VF analysis

## DETAILED DESCRIPTION OF THE INVENTION

- introduce QRS complex and its limitations
- motivate feature extraction from ECG signals
- describe Decision Support System block diagram
- illustrate real-time system overview
- parse and preprocess ECG signal
- extract features from time domain
- calculate prototype distance with RPD-PD
- extract features with duel-tree complex wavelet decomposition
- illustrate high-level steps of the invention
- describe data collection and preprocessing
- apply Savitzky-Golay filter for noise reduction
- extract time-series features from cleaned signal
- perform dual-tree complex wavelet decomposition
- perform non-linear non-deterministic time-series analysis
- define cross-validation method
- calculate recurrence period density
- define metric KD for pairwise distances
- optimize sep for class separation
- calculate distance features sKDB and sKDW
- describe cross-validation with feature selection
- formulate new data matrix with selected features
- describe cost-sensitive feature selection
- employ Recursive Feature Elimination with SVMs
- extract time-series and complex wavelet features
- describe problem of VF to VF pre-shock comparison
- evaluate performance of machine learning approach
- describe decision support system for resuscitation
- discuss therapeutic alternatives and drugs as predictors
- highlight importance of VF duration and CPR effects
- discuss advantages of Complex Wavelet decomposition

