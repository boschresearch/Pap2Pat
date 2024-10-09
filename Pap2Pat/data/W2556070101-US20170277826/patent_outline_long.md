# DESCRIPTION

## FIELD

- relate to gene signaling pathways

## BACKGROUND

- introduce chronic diseases
- motivate genomics and personalized medicine
- describe novel methods for drug screening
- introduce intracellular signaling pathways
- describe bioinformatics tools
- discuss proteomic and transcriptomic data
- introduce US2008254497A
- introduce U.S. Pat. No. 8,623,592
- discuss supervised learning algorithms
- describe challenges in transcriptomic data analysis
- introduce data normalization approaches
- discuss various transcriptomic data analysis algorithms
- introduce pathway-based methods
- describe limitations of current pathway-based methods
- motivate need for new analytical methodologies

## SUMMARY

- introduce iPANDA method
- describe receiving cell transcriptomic data
- calculate fold change ratio
- repeat steps for multiple genes
- group co-expressed genes into modules
- estimate gene importance factors
- obtain iPANDA value
- determine biological iPANDA
- provide classifier for treatment response prediction
- apply statistical filtering and threshold tests
- obtain bodily samples and apply drug
- determine responder and non-responder patients
- describe various embodiments of the invention

## DETAILED DESCRIPTION

- introduce detailed description
- reference prior art
- describe system for improving robustness of transcriptomic data analysis
- introduce server utility and database
- describe transcriptomic data sets
- describe mobile device connection to server utility
- describe sample analyzer and computer
- describe outputting module
- describe user communication with server
- describe system operation through communication protocols
- describe call and user support center
- introduce variations to system
- introduce method for improving robustness of transcriptomic data analysis
- describe steps of method
- describe iPANDA outputting step

### Results

- introduce iPANDA method
- describe gene importance factor (GIF)
- motivate different approaches for GIF calculation
- integrate statistical and topological weights for GIF estimation
- apply smooth threshold to gene expression values
- derive statistical weights from p-values
- obtain topological weights from pathway map decomposition
- introduce gene modules for coexpressed genes
- compute contribution of gene units to pathway activation
- calculate iPANDA values as linear combination of scores
- define pathway quality metrics
- motivate noise reduction in transcriptomic data
- introduce scalability as a hallmark of pathway analysis
- describe robustness of biomarker lists
- compare iPANDA with other pathway analysis algorithms
- apply iPANDA to breast cancer and MAQC datasets
- estimate noise reduction efficacy of iPANDA
- compare noise reduction of iPANDA with other algorithms
- identify biomarkers using iPANDA
- measure ROC AUC values for biomarkers
- rank pathways by average AUC values
- demonstrate scalability of iPANDA
- produce robust set of biomarkers using iPANDA
- apply CMP index to estimate robustness of biomarker lists
- analyze effect of gene grouping and topology coefficients on robustness
- apply iPANDA biomarkers as classifiers for treatment response prediction
- calculate pairwise distance matrices between samples
- perform hierarchical clustering using Ward linkage
- classify samples as responders or non-responders
- estimate false positive and false negative rates of predictions
- compare clustering results with other algorithms
- demonstrate cross-study validity of iPANDA biomarkers
- perform prediction using separate training and test data sets
- classify samples based on iPANDA scores for pathway markers
- compare results with actual treatment outcome
- discuss further perspectives of iPANDA application
- highlight advantages of iPANDA in noise reduction and biomarker identification
- mention high speed of iPANDA computation
- discuss limitations of microarray data analysis
- suggest application of iPANDA to GWAS data
- propose using iPANDA scores as input for deep learning methods
- describe preprocessing of transcriptomic data
- stratify breast cancer samples by HER2 receptor status
- describe MAQC data set
- overview pathway database
- describe estimation of pathway activation
- introduce gene grouping into modules
- calculate contribution of gene units to pathway activation
- define final function for obtaining iPANDA value
- compute gene importance factors
- derive topological weight
- calculate statistical weight
- obtain gene modules
- estimate statistical credibility of iPANDA values
- estimate algorithm robustness
- cluster data samples
- perform calculations using third-party algorithms
- describe GSEA package
- describe SPIA R package
- discuss limitations of invention
- discuss scope of invention
- discuss computer implementation
- discuss computer readable storage medium
- discuss general purpose computer
- discuss computer program
- discuss computer readable storage medium
- discuss electronic instructions
- discuss computer system bus
- discuss general purpose components
- discuss specialized apparatus
- discuss programming language
- discuss references cited in background
- discuss incorporation by reference
- discuss alternative embodiments
- discuss equivalent functionality
- discuss machine-readable memory
- discuss program of instructions
- discuss executable by machine
- discuss method of invention

