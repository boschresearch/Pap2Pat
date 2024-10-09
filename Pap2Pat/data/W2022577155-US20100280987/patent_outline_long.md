# DESCRIPTION

- claim benefit of provisional patent application

## 1. BACKGROUND OF THE INVENTION

- motivate patient subpopulation identification
- limitations of current cancer therapies
- importance of response prediction
- gene expression signatures associated with response
- limitations of cytotoxic chemotherapies
- modulating cell signaling pathways
- aberrant signaling in cancer cells
- dependence on activation of one or two pathways
- inactivation of critical oncogene
- components of aberrant signaling pathways as targets
- identify gene expression profiles indicative of pathway activation
- current methods for assessing pathway activation
- RAS pathway regulation and deregulation
- aberrant RAS signaling in tumors
- inhibition of RAS or its upstream activators or downstream effectors
- accurate determination of RAS pathway activation

## 3. DETAILED DESCRIPTION OF THE INVENTION

- introduce invention embodiments

### 3.1 Introduction

- relate to genetic biomarkers
- split biomarkers into up and down arms
- correlate biomarkers with RAS signaling pathway
- classify tumors using biomarkers
- indicate therapy response using biomarkers
- provide methods and microarrays for biomarkers

### 3.2 DEFINITIONS

- define oligonucleotide sequences
- define bind substantially
- define hybridizing specifically to
- define biomarker
- define biomarker-derived polynucleotides
- define informative gene marker
- define gene
- define isolated gene
- define transcribed nucleotide sequence
- define 5' untranslated sequences
- define 3' untranslated sequences
- define signature
- define similarity value
- define measuring expression levels
- define patient
- define subject
- define pathway
- define RAS signaling pathway
- define RAS pathway signature
- define RAS pathway agent
- define growth factor signaling pathway
- define PI3K signaling pathway
- define growth factor pathway agent
- define PI3K agent
- define molecular targets of PI3K agents
- define examples of PI3K agents
- define deregulated signaling pathway
- define oncogenic pathway
- define treating
- define treatment of cancer
- define therapeutically effective amount
- define displaying or outputting a classification result
- define displaying or outputting a prediction result
- define displaying or outputting an efficacy result
- define computer readable medium
- define computer system
- define internal components
- define external components
- define carrier waves

### 3.3 BIOMARKERS USERFUL IN CLASSIFYING TUMORS AND PREDICTING RESPONSE TO THERAPEUTIC AGENTS

- provide biomarker sets for RAS signaling pathway regulation status
- list biomarkers for tumor classification and therapeutic response prediction
- describe up and down arms of biomarker sets
- provide subsets of biomarkers for RAS signaling pathway regulation status
- describe use of biomarkers for predicting response to RAS signaling pathway agents
- provide subsets of biomarkers for predicting response to RAS signaling pathway agents
- describe use of biomarkers for selecting RAS pathway agents for treatment
- provide subsets of biomarkers for selecting RAS pathway agents for treatment
- describe use of biomarkers for predicting resistance to PI3K signaling pathway agents
- provide subsets of biomarkers for predicting resistance to PI3K signaling pathway agents
- describe use of biomarkers for excluding PI3K pathway agents for treatment
- provide subsets of biomarkers for excluding PI3K pathway agents for treatment
- describe use of biomarkers for determining pharmacodynamic effect on RAS signaling pathway
- provide subsets of biomarkers for determining pharmacodynamic effect on RAS signaling pathway
- describe use of biomarkers in combination with other biomarkers
- identify biomarkers for cancer conditions or indications
- describe method for identifying biomarker sets
- extract and label target polynucleotides
- compare expression levels of biomarkers in sample and standard
- select biomarkers based on significant difference in expression
- calculate statistical significance of correlation between biomarker expression and condition
- use microarray to assess expression of all biomarkers
- select biomarkers based on both fold change and p-value
- use expression profiles to identify markers correlating with clinical categories
- calculate correlation coefficient between biomarker expression and clinical category
- identify biomarkers for which correlation coefficient exceeds cutoff
- evaluate significance of biomarker set
- use Monte-Carlo technique to randomize association between expression profiles and clinical categories
- generate control biomarker sets and probability distribution
- evaluate significance of biomarker set based on probability distribution
- rank-order biomarkers by correlation or significance of discrimination
- define biomarkers for classifying tumors and predicting response to therapeutic agents
- introduce error-weighted average of log ratio of transcript expression measurements
- derive t-value representing variance-compensated difference between two means
- identify set of genes for RAS pathway signaling status using iterative approach
- validate marker set using survival model
- calculate probability of tumor distant metastases as a function of time since initial diagnosis
- iterate biomarker identification process by excluding one or more samples
- split biomarkers into two opposing arms
- generalize methods to identify set of biomarker genes associated with any phenotype
- collect sample from individual afflicted with cancer or tumor cell lines
- extract target polynucleotide molecules from sample
- label and hybridize mRNA or nucleic acids to microarray
- prepare total and poly(A)+ RNA
- isolate RNA from eukaryotic cells
- remove DNA from RNA sample
- enrich mRNA with respect to other cellular RNAs
- elute poly(A)+ mRNA from affinity column
- specify embodiments of RNA sample composition

### 3.4 METHODS OF USING RAS SIGNALING PATHWAY DEREGULATION BIOMARKER SETS

- introduce diagnostic/tumor classification methods
- describe biomarker sets for RAS signaling pathway deregulation
- explain expression analysis of biomarker genes
- compare expression levels to standard or control
- determine tumor-related status based on expression differences
- describe hybridization of target polynucleotides to microarray
- describe hybridization of standard or control polynucleotides
- determine difference in transcript levels between target and standard
- use artificially-generated pool of biomarker-derived polynucleotides as control
- use pool derived from normal or cancer cell lines as control
- compare expression levels to deregulated and regulated RAS signaling pathway controls
- calculate measure of similarity between expression profiles
- classify tumor cell sample based on similarity to templates
- display or output classification results
- use subsets of biomarkers for classification
- select biomarkers from Table 2b for subsets
- use differential expression profile for classification
- calculate similarity between expression profiles using equation (4)
- represent similarity as correlation coefficient
- set correlation threshold for classification
- represent similarity as distance between profiles
- set distance threshold for classification
- develop templates for sample comparison
- calculate classifier parameter using equation (5)
- use classifier parameters to measure similarity to templates
- classify sample based on similarity to templates
- use multiple classifier parameters for classification
- set multiple correlation thresholds for classification
- describe method for determining tumor-related status
- use microarray containing biomarker set for hybridization
- compare results to predefined templates for classification
- describe RAS signaling pathway deregulation biomarker sets
- introduce "up" and "down" arms of biomarkers
- calculate signature score using log(10) ratio
- determine significance of signature score using ANOVA
- rank order samples by RAS pathway deregulation status
- compare sample to reference template
- compare sample to pre-determined threshold
- rank order samples by signature score
- predict response to treatment with RAS signaling pathway modulator
- assign treatment based on RAS signaling pathway deregulation status
- use subsets of biomarkers for prediction and assignment
- generate template for classification
- classify sample as "predicted responder" or "predicted non-responder"
- use two "arms" of biomarkers for prediction and assignment
- calculate signature score using mean log(10) ratio
- determine significance of signature score using ANOVA
- apply biomarkers to various phenotypes or conditions
- distinguish phenotypes using biomarker sets
- introduce method of determining whether an agent modulates RAS signaling pathway
- describe RAS signaling pathway
- identify agents that modulate RAS signaling pathway
- include small molecule compounds as agents
- include proteins or peptides as agents
- include siRNA, shRNA, or microRNA molecules as agents
- define RAS pathway agent
- list molecular targets
- list RAS pathway inhibitors
- describe method for measuring effect of agent
- compare expression levels of biomarkers
- determine significant difference in expression levels
- use subsets of biomarkers
- calculate signature score
- perform ANOVA calculation
- determine significance of signature score
- use alternative differential expression values
- rank order agents by effect on biomarker sets
- describe method of measuring pharmacodynamic effect
- compare expression levels of biomarkers in treated sample
- determine significant difference in expression levels
- use subsets of biomarkers to monitor pharmacodynamic activity
- calculate signature score for pharmacodynamic activity
- perform ANOVA calculation for pharmacodynamic activity
- determine significance of signature score for pharmacodynamic activity
- apply biomarkers to various phenotypes or conditions
- use biomarkers to distinguish between phenotypes
- describe improving sensitivity to expression level differences
- normalize expression level values
- use control genes for normalization
- specify normalization methods
- introduce RAS signaling pathway deregulation biomarker sets
- increase sensitivity of biomarker-based assay
- compare expression levels to pool of samples
- normalize expression levels
- log transform expression levels
- classify cell or organism as having one of at least two different phenotypes
- compare expression levels to pool representing one phenotype
- use single-channel data without comparison to pool
- calculate similarity between expression profiles
- use classifier for predicting RAS signaling pathway regulation status
- train classifier with training data
- obtain biomarker profile using method known in the art
- use statistical pattern recognition methods
- construct classifier using biomarker profiles and RAS pathway signaling status data
- evaluate RAS pathway signaling status of patient based on biomarker profile
- identify biomarkers that discriminate between different RAS signaling pathway regulation status
- use profile matching
- compare biomarker profile to template profile
- calculate correlation coefficient
- use weighted dot product
- represent similarity by distance
- use Euclidian distance
- use Manhattan distance
- use Chebychev distance
- use power distance
- use percent disagreement
- use artificial neural network
- construct neural network for selected set of molecular markers
- use neural network for regression or classification
- train neural network with training patterns
- adjust weights to reduce error
- use stochastic, batch, or on-line training protocols
- consider starting values for weights
- standardize inputs
- choose optimal number of hidden units
- use regularization approach
- eliminate weights that are least needed
- use magnitude-based pruning
- use Wald statistics
- use Optimal Brain Damage algorithm
- use Optimal Brain Surgeon algorithm
- predict functional increase in error
- calculate saliency of weight
- update inverse Hessian matrix
- terminate algorithm when error is greater than criterion
- use support vector machine
- use logic regression
- use linear or quadratic discriminant analysis
- use decision trees, clustering, principal component analysis, or nearest neighbor classifier analysis
- introduce RAS signaling pathway deregulation biomarker sets
- use back-propagation neural network
- set parameter values in EasyNN-Plus program
- identify outlier samples
- introduce support vector machines
- describe SVM applications in biological systems
- standardize gene expression data
- divide training population into training and test sets
- train SVM with selected gene expression values
- determine SVM classification accuracy
- describe SVM decision function
- define margin and hyperplane
- describe kernel function and Mercer's theorem
- discuss soft-margin and margin-distribution classifiers
- introduce logistic regression model
- compute regression coefficients using maximum likelihood
- describe multicategory logit models
- introduce linear discriminant analysis
- describe LDA application to molecular biomarker data
- discuss quadratic discriminant analysis
- introduce decision trees
- describe decision tree derivation algorithm
- calculate information gain
- describe information content and entropy
- discuss decision tree classification
- describe advantages of decision trees
- discuss limitations of decision trees
- introduce other classification methods
- conclude classification methods
- define information gain
- calculate information gain
- describe decision tree algorithms
- introduce clustering
- describe clustering problem
- discuss similarity measures
- describe criterion functions
- list clustering techniques
- introduce principal component analysis
- describe principal component analysis
- create classifier using PCA
- plot vectors using PCA
- describe nearest neighbor classifier analysis
- compute Euclidean distance
- describe nearest neighbor rule
- refine nearest neighbor rule
- introduce evolutionary methods
- describe evolutionary methods
- score classifiers
- rank classifiers
- alter classifiers
- introduce bagging, boosting, and random subspace method
- describe bagging
- describe boosting
- illustrate boosting
- describe weighted majority vote
- modify observation weights
- update weights
- describe random subspace method
- combine classifiers
- introduce other algorithms
- describe pattern classification techniques
- describe statistical techniques
- combine techniques
- describe decision trees and boosting
- describe projection pursuit
- describe weighted voting
- list other techniques
- describe clustering algorithms
- describe hierarchical clustering
- describe k-means clustering
- describe fuzzy k-means clustering
- describe Jarvis-Patrick clustering
- conclude classifier construction

### 3.5 DETERMINATION OF BIOMARKER GENE EXPRESSION LEVELS

- introduce biomarker gene expression levels
- describe methods for determining expression levels
- isolate and determine nucleic acid levels
- determine protein levels translated from mRNA
- describe northern hybridization method
- describe dot-blot and slot-blot methods
- label polynucleotides using radiolabel or fluorescent label
- mention other methods of determining RNA abundance
- describe quantitative PCR methods
- describe Nanostring's NCOUNTERT Digital Gene Expression System
- assess protein expression using western blot
- describe two-dimensional gel electrophoresis systems
- analyze electropherograms using mass spectrometry
- describe antibody microarray method
- construct antibody microarray using monoclonal antibodies
- detect protein expression using immunohistochemical staining
- describe tissue array method
- introduce microarrays for measuring expression
- describe oligonucleotide or cDNA arrays
- construct microarrays with probes hybridizable to biomarkers
- describe scanning and screening arrays
- introduce commercially-available cDNA microarrays
- describe construction of microarrays
- select and immobilize probes to solid support
- describe characteristics of microarrays
- prepare probes for microarrays
- describe probe sequences and lengths
- introduce DNA extraction methods
- describe PCR amplification
- specify primer design
- introduce microarray technology
- describe probe synthesis methods
- specify probe length and composition
- introduce algorithm for probe selection
- describe control probes
- attach probes to solid surface
- describe microarray manufacturing methods
- introduce ink-jet printing method
- describe microarray density
- introduce target polynucleotide molecules
- describe RNA extraction methods
- specify RNA sources
- describe RNA fragmentation
- introduce normalization techniques
- describe labeling methods
- specify label types
- introduce differential labeling
- describe hybridization conditions
- specify hybridization temperatures
- describe wash conditions
- introduce denaturing conditions
- describe signal detection methods
- specify scanning confocal laser microscopy
- introduce simultaneous specimen illumination
- describe fluorescence laser scanning devices
- introduce signal analysis methods
- specify image despeckling
- describe image gridding program
- introduce correction for cross-talk
- calculate ratio of emission for each hybridization site

### 3.6 COMPUTER-FACILITATED ANALYSIS

- introduce kit with biomarker sets and software
- describe computer system components
- specify internal components
- specify external components
- describe network link
- list software components
- specify operating system
- describe programming languages
- outline software for data analysis
- exemplify implementation of methods

## EXAMPLES

### Example 1

- introduce RAS pathway activity biomarkers
- describe Bild et al. study
- describe Sweet-Cordero et al. study
- describe Blum et al. study
- derive RAS signature using supervised analysis
- identify up and down arms of RAS signature
- describe core set of up genes
- describe down arm of RAS signature

### Example 2

- assess coherency of RAS signatures
- describe coherence analysis
- calculate correlation coefficients
- perform Fisher exact test
- refine signatures by filtering genes
- calculate RAS signature score
- describe initial signature coherence analysis
- perform pairwise comparison of cell lines
- check coherence of signatures on additional datasets
- describe microarray analysis

### Example 3

- assess consensus of different signatures
- perform pairwise scatter plots
- analyze correlations between signatures
- discuss significance of correlations

### Example 4

- predict RAS mutations in cell lines
- calculate RAS pathway signature score
- classify samples based on signature score
- analyze results in different cell line panels
- discuss limitations of signature

### Example 5

- assess coherence of RAS signature in tumors
- rank tumors based on RAS signature score

### Example 6

- predict prevalence of RAS deregulation in tumor subtypes
- analyze RAS signature in ovarian tumors
- analyze RAS signature in non-small cell lung tumors

### Example 7

- knockdown K-RAS using siRNA

### Example 8

- analyze association of RAS signature with resistance to AKT inhibitor
- generate resistant cell lines using AKT compound

### Example 9

- predict response to MEK inhibitor
- analyze RAS signature in lung cancer cell lines
- determine sensitivity to MEK inhibition
- analyze relationship between RAS signature and MEK inhibition
- analyze results in KRas mutant cell lines
- analyze results in KRas wildtype cell lines

