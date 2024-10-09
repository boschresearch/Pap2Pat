# DESCRIPTION

## BACKGROUND

- motivate cancer screening and diagnostics

## BRIEF SUMMARY

- introduce machine learning approach
- describe non-cellular analytes in circulation
- summarize method of using classifier
- outline steps of method
- describe classes of molecules
- provide examples of assays
- describe machine learning models
- summarize specified properties

## TERMS

- define terms for patent application
- specify meaning of "a", "an", and "the"
- define "area under the curve" and "AUC"
- define "cancer" and "cancerous"
- define "genetic variant" and "germline variant"
- define "input features" and "machine learning model"
- define "marker" and "non-cancerous tissue"
- define "polynucleotides" and "polypeptide"
- define "prediction", "prognosis", and other terms

## DETAILED DESCRIPTION

- introduce medical diagnostic methods using machine learning

### I. CIRCULATING ANALYTES AND CELLULAR DECONSTRUCTION WITH BIOLOGICAL ASSAYS

- define analytes for biological predictions
- describe types of analytes (nucleic acids, proteins, metabolites)
- provide examples of analytes (DNA, RNA, proteins, metabolites)

### II. SAMPLE PREPARATION

- obtain and process biological sample
- modify nucleic acid molecule or fragment
- prepare library for sequencing
- sequence nucleic acid molecules
- prepare biological information using sequencing
- perform biological assays on sample portions
- generate feature data for machine learning analysis
- integrate assays and features for machine learning model
- introduce sample preparation methods
- describe copy number variation detection
- explain somatic mutation analysis
- discuss transcription factor profiling
- infer chromosome structure/chromatin state
- describe chromatin state prediction
- explain chromatin remodeling and gene expression
- discuss chromosome conformation technologies
- motivate tissue of origin assay
- describe genetic features for cell-type-of-origin
- introduce methylation sequencing
- summarize methylation analysis methods
- describe differentially methylated regions analysis
- introduce cfRNA assays
- introduce sample preparation methods
- describe cfRNA detection methods
- outline mRNA level assaying methods
- summarize protein and peptide assays
- describe autoantibody detection methods
- outline carbohydrate assays
- discuss metrics for machine learning models

### III. EXAMPLE SYSTEMS

- introduce system architecture
- describe data analysis modules
- detail machine learning model implementation
- explain data visualization module
- illustrate system 100 components
- describe computer system 101 components
- outline network 130 capabilities

### IV. MACHINE LEARNING TOOLS

- apply machine learning to optimize assay selection
- describe machine learning techniques for data analysis
- outline supervised and unsupervised learning methods

### V. SELECTION OF INPUT FEATURES

- describe feature selection process
- introduce feature types (e.g., structural variations, mutations)
- explain feature engineering (e.g., concatenation, merging)
- discuss weighting of features
- outline iterative feature selection process

### VI. USE OF MACHINE LEARNING MODEL FOR MULTI-ANALYTE ASSAYS

- describe method for analyzing biological sample
- outline formation of feature vector from measured values
- explain input of feature vector into machine learning model

### VII. CLASSIFIER GENERATION

- define classifier generation
- motivate machine learning techniques
- describe classifier capabilities
- outline system for classifying subjects
- specify classification circuit options
- explain linear classifier operation
- discuss conversion of assay data into prognosis
- describe training step for prediction method
- outline advantages and applications of classifier

### VIII. CANCER DIAGNOSIS AND DETECTION

- motivate cancer diagnosis
- describe machine learning-based diagnosis
- train machine learning predictor
- generate diagnostic signature
- apply trained algorithm to generate likelihood of cancer
- motivate treatment responsiveness
- describe predictive classifiers for treatment responsiveness
- stratify population into responders and non-responders

### IX. INDICATIONS

- define biological condition
- specify examples of biological conditions
- describe application to colon cancer
- list conditions that can be inferred
- provide non-limiting examples of cancers
- provide non-limiting examples of gut-associated diseases
- provide non-limiting examples of other diseases
- introduce machine learning for commercial testing modalities
- describe hierarchical overview of multi-analyte approach
- outline iterative flow between wet lab and computer components
- specify initialization phase of assay design
- describe data filtering and feature extraction
- outline model selection and training
- detail assessment and iteration of assay design
- introduce multi-analyte assay design
- describe overall process flow for designing multi-analyte assay
- identify features operable to be input to machine learning model
- subject classes of molecules to different assays to obtain sets of measured values
- analyze sets of measured values to obtain training vector for training sample
- operate on training vectors using parameters of machine learning model
- compare output labels to known labels of training samples
- iteratively search for optimal values of parameters
- provide parameters of machine learning model and set of features
- identify cancer in subject using trained algorithm
- analyze individual assays for classification of biological samples
- describe results for different analytes and corresponding best performing model
- describe protein data normalization
- present protein biomarker distribution
- perform dimensionality reduction
- draw conclusions from lcWGS data
- identify Hi-C-like structure using covariance
- describe sample collection and preprocessing
- process whole genome sequencing data
- introduce tissue-of-origin analysis
- describe cfHi-C analysis
- quantify similarity between Hi-C and cfHi-C
- rule out technical bias and batch effects
- test robustness of approach
- apply approach to different cancer types
- quantify accuracy of approach
- describe detection of cancer using cfDNA
- annotate human genome regions
- generate feature set from annotated regions
- preprocess feature set via transformations
- perform cross-validation procedure
- mitigate confounding factors in cross-validation
- train model with transformed data
- evaluate model performance
- analyze feature importance
- evaluate performance across populations
- assess generalizability to new data
- evaluate performance on other cancer types
- discuss importance of controlling confounding factors
- conclude on cfDNA approach for cancer detection
- describe machine learning model training and validation
- illustrate classification performance and results
- introduce gene expression prediction model using cfDNA fragment coverage and length
- describe prediction model training and evaluation
- illustrate V-plot analysis and chromatin state identification
- describe computer system architecture and software implementation
- provide general description of embodiments and variations

