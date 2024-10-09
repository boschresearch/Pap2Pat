# DESCRIPTION

## BACKGROUND

- motivate cancer screening
- limitations of current cancer diagnostics
- need for new approaches

## BRIEF SUMMARY

- introduce machine learning approach
- describe non-cellular analytes
- motivate liquid biological samples
- describe classifier
- outline method steps
- describe feature vector
- describe machine learning model
- describe training process
- describe output classification
- provide examples of classes of molecules
- provide examples of assays
- describe specified property
- describe system for classification
- describe computer-readable medium
- describe system for multi-analyte analysis
- describe non-transitory computer-readable medium

## TERMS

- define "a", "an", "the" and "or"
- define "area under the curve" (AUC)
- define "biological sample"
- define "cancer" and "cancerous"
- define "cancer-free"
- define "genetic variant" (or "variant")
- define "germline variant"
- define "input features" (or "features")
- define "machine learning model" (or "model")
- define "marker" or "marker proteins"
- define "non-cancerous tissue"
- define "polynucleotides", "nucleotide", "nucleic acid", and "oligonucleotides"
- define "polypeptide" or "protein" or "peptide"
- define "prediction"
- define "prognosis"
- define "specificity"
- define "sensitivity"
- define "structural variation" (SV)
- define "subject"

## DETAILED DESCRIPTION

- introduce medical diagnostic methods using machine learning
- describe advantages of the present approach

### I. CIRCULATING ANALYTES AND CELLULAR DECONSTRUCTION WITH BIOLOGICAL ASSAYS

- motivate biological assays for health-related predictions
- define analytes and their sources
- describe DNA analytes
- describe RNA analytes
- describe protein analytes
- describe other analytes
- discuss combinations of analytes

### II. SAMPLE PREPARATION

- obtain biological sample
- process sample to purify nucleic acid molecule
- modify nucleic acid molecule
- separate sample into aliquots
- process sample to remove higher/lower molecular weight nucleic acid molecules
- centrifuge or filter sample
- tag or barcode nucleic acid molecule
- partition sample
- detect cellular components
- quantify nucleic acid molecules
- prepare library for sequencing
- add adapter sequences to nucleic acid molecules
- incorporate molecular barcodes
- sequence nucleic acid molecules
- treat nucleic acid molecules for methylation analysis
- prepare biological information for machine learning analysis
- introduce sample preparation
- motivate copy number variation
- describe copy number variation detection
- introduce somatic mutation analysis
- describe somatic mutation detection
- introduce transcription factor profiling
- describe transcription factor binding site analysis
- introduce method for diagnosing disease
- describe method for diagnosing disease
- introduce inferring chromosome structure
- describe chromatin state prediction
- motivate chromatin remodeling
- describe chromatin state inference
- introduce ATAC-seq and DNAse-seq
- describe Hi-C sequencing
- conclude cfDNA analysis
- introduce tissue of origin assay
- motivate cell-type-of-origin determination
- describe genetic features for cell-type-of-origin
- prepare arrays for cell-type-of-origin estimation
- estimate cell-type proportion using matrix multiplication
- provide method for processing sample
- introduce methylation sequencing
- describe bisulfite conversion for methylation analysis
- list methylation analysis methods
- describe machine learning approach for nucleosome positioning
- provide metrics for methylation analysis
- introduce differentially methylated regions analysis
- describe haplotype blocks and cfRNA assays
- introduce sample preparation
- describe cfRNA detection methods
- detail mRNA level assaying methods
- explain PCR reaction and amplification methods
- list RNA markers associated with cancer
- introduce poly-amino acid and autoantibody assays
- describe protein measurement methods
- list cancer-associated peptide and protein markers
- detail autoantibody detection methods
- explain metrics for autoantibody assay
- associate autoantibody markers with cancer subtypes
- list tumor-associated antigens
- introduce carbohydrate assays
- describe carbohydrate measurement methods

### III. EXAMPLE SYSTEMS

- introduce system architecture
- describe data analysis in measurement devices
- outline software organization
- detail data receiving module
- describe data pre-processing module
- outline data analysis module
- detail data interpretation module
- describe data visualization module
- introduce machine learning models
- describe computational analysis on nucleic acid sequencing data
- outline analysis methods
- detail variant identification
- describe system 100 components
- outline computer system 101 components
- describe network 130 functionality

### IV. MACHINE LEARNING TOOLS

- introduce machine learning for assay selection
- describe statistical learning and regression analysis
- outline machine learning techniques for commercial testing
- detail threshold checks for assay performance
- describe machine learning methods
- outline supervised and unsupervised machine learning methods
- describe training samples and quality metrics

### V. SELECTION OF INPUT FEATURES

- describe feature space generation
- list example features for genetic sequence data
- motivate feature selection for invariant features
- describe procedures for identifying invariant features
- describe statistical metrics for feature selection
- introduce feature vector creation
- describe feature vector structure
- motivate feature concatenation and merging
- describe weighting of features
- introduce iterative feature selection

### VI. USE OF MACHINE LEARNING MODEL FOR MULTI-ANALYTE ASSAYS

- introduce machine learning model for class distinction
- describe biological sample preparation
- identify features for machine learning model
- perform assays on biological sample
- form feature vector from measured values
- load trained machine learning model
- input feature vector to obtain output classification

### VII. CLASSIFIER GENERATION

- introduce classifier generation
- describe machine learning techniques
- motivate disease class distinction
- specify cancer class distinction
- describe machine learning model
- outline feature vector generation
- train machine learning model
- describe system for classifying subjects
- specify classification circuit
- describe linear classifier
- optimize threshold of linear classifier
- describe interpretation of decision score
- outline methods for converting assay data
- describe training step
- specify transformation or pre-processing steps
- describe weighted sum of feature values
- outline non-linear transformation methods
- describe various classification methods

### VIII. CANCER DIAGNOSIS AND DETECTION

- introduce cancer diagnosis and detection
- describe predictive analytics using AI-based approaches
- train machine learning predictor using datasets
- generate features and labels for training datasets
- select training sets by random or proportionate sampling
- balance training sets across data corresponding to subjects
- train machine learning predictor until certain conditions are satisfied
- provide examples of diagnostic accuracy measures
- describe method for identifying cancer in a subject
- sequence cfNA molecules to generate sequencing reads
- align sequencing reads to a reference genome
- generate quantitative measure of sequencing reads at genomic regions
- apply trained algorithm to generate likelihood of subject having cancer
- describe monitoring disease progression in a subject
- describe determining tissue-of-origin of cancer in a subject
- describe estimating tumor burden in a subject

### IX. INDICATIONS

- define biological condition
- specify examples of biological conditions
- describe unknown biological condition
- motivate machine learning for unknown biological condition
- introduce colon cancer
- describe stages of colon cancer
- specify examples of conditions that can be inferred
- describe non-limiting examples of cancers
- describe non-limiting examples of gut-associated diseases
- describe non-limiting examples of immune-mediated inflammatory diseases
- describe non-limiting examples of neurological diseases
- describe non-limiting examples of kidney diseases
- describe non-limiting examples of prenatal diseases
- describe non-limiting examples of metabolic diseases
- introduce indications
- describe machine learning techniques
- outline threshold check
- describe assay engineering procedure
- motivate hierarchy of samples and portions
- describe multi-analyte approach
- outline stages of multi-analyte approach
- describe learning module
- outline iterative flow between modules
- describe initialization phase
- describe exploratory phase
- describe refinement phase
- describe validation/confirmation phase
- outline data filter module
- describe feature extraction module
- introduce multi-analyte assay design
- motivate iterative process for assay selection
- describe overall process flow for designing multi-analyte assay
- receive training samples with multiple classes of molecules
- identify features for each assay and training sample
- obtain measured values for each assay and training sample
- analyze measured values to obtain training vectors
- operate on training vectors using machine learning model
- compare output labels to known labels
- iteratively search for optimal parameters
- provide parameters and features for machine learning model
- identify cancer in subject using trained algorithm
- generate quantitative measures of cfNA sequencing reads
- apply trained algorithm to generate likelihood of cancer
- generate report with information indicative of likelihood
- generate recommended steps for treating cancer
- diagnose subject with cancer based on likelihood
- analyze individual assays for classification of biological samples
- describe analysis of multiple analytes and multiple assays
- perform low-coverage whole-genome sequencing
- perform whole-genome bisulfite sequencing
- perform small-RNA sequencing
- measure levels of circulating proteins
- analyze sequenced reads and measured values
- apply machine learning model to perform classification
- introduce protein data
- normalize protein data
- describe protein biomarker distribution
- motivate dimensionality reduction
- perform principal component analysis
- describe output of PCA analysis
- discuss conclusions
- introduce identification of Hi-C-like structure
- describe method of identification
- discuss correlation structure
- describe sample collection and preprocessing
- discuss whole genome sequencing data processing
- describe Hi-C library preparation and data processing
- discuss sequence composition and mappability bias analysis
- introduce tissue-of-origin analysis
- describe cfHi-C analysis
- perform paired-end whole genome sequencing
- calculate normalized fragmentation score
- quantify degree of similarity between Hi-C and cfHi-C
- call compartment A/B at Hi-C data and cfHi-C
- expand application of cfHi-C to single-sample level
- rule out internal library preparation bias and sequencing bias
- rule out technical bias caused by sequence composition
- perform negative control using genomic DNA
- elucidate effect of G+C % and mappability in two-dimensional space
- test robustness of approach
- understand effect of bin size
- understand effect of sequencing depth in single-sample cfHi-C
- determine whether observed signal varies at different pathological conditions
- determine whether in vivo chromatin organization measured through cfDNA may be used to infer cell types contributing to cfDNA
- describe detection of colorectal cancer, breast cancer, pancreatic cancer, or liver cancer
- annotate human genome regions
- generate feature set from annotated regions
- preprocess feature set
- perform k-fold cross-validation
- describe k-batch cross-validation
- describe balanced k-batch cross-validation
- describe ordered k-batch cross-validation
- illustrate training schemas
- apply k-batch with institutional downsampling
- transform data for model training
- train and evaluate classifiers
- report performance metrics
- assess generalizability to new data
- evaluate k-batch cross-validation
- evaluate balanced k-batch cross-validation
- evaluate ordered k-batch cross-validation
- analyze performance by population
- analyze performance by CRC stage
- analyze performance by tumor fraction
- analyze performance by age
- analyze performance by gender
- identify important features
- analyze feature importance
- evaluate performance on other cancer types
- discuss results and implications
- conclude on cancer detection using cfDNA
- extract reads from annotated protein-coding genes
- normalize read counts
- train machine learning models
- illustrate training schemas
- evaluate classification performance
- describe gene expression prediction model
- obtain de-identified plasma samples
- train prediction model
- analyze cfDNA fragment coverage and length
- evaluate classification accuracy
- describe computer system architecture
- implement control logic using hardware and software
- encode and transmit software components
- provide general description of embodiments

