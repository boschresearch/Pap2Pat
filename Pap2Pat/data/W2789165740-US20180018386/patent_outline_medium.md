# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- disclose government support

## FIELD OF THE INVENTION

- define fields of data analysis and visualization

## BACKGROUND

- motivate need for sample comparison
- describe limitations of manual gating
- summarize existing cluster matching methods
- describe limitations of existing methods
- identify need for improved systems and methods

## BRIEF SUMMARY

- introduce multidimensional cluster matching
- introduce visualization of multidimensional data
- describe method for matching clusters in data
- describe obtaining first and second sample data
- describe identifying clusters in first and second sample data
- describe performing multivariate adaptive binning
- describe applying combined binning pattern to first and second sample data
- describe determining dissimilarity score for combinations of clusters
- describe identifying matched clusters and merging candidates
- describe determining whether merging candidate corresponds to split or missing cluster
- describe forming combined data set
- describe generating histograms for identified clusters
- describe determining dissimilarity score using quadratic form distance
- describe calculating spatial dissimilarity between bins
- describe identifying matched clusters and merging candidates based on dissimilarity scores
- describe determining distance between geometric means of matched clusters
- describe identifying unmatched clusters based on distance threshold
- describe system for matching clusters in data
- describe adaptive binning module
- describe dissimilarity module
- describe matching and merging candidate identification module
- describe determination module
- describe method for rendering graphical user interface
- describe displaying interactive displays for data visualization

## DETAILED DESCRIPTION OF THE INVENTION

### Definitions

- define item
- define gating
- define gate
- define marker
- define reagent
- define stain
- define staining reagent
- specify singular forms
- specify embodiment references
- introduce cluster matching
- describe clustering
- describe joint clustering and matching
- describe limitations of conventional methods
- introduce dissimilarity score criteria
- describe conventional dissimilarity measures
- introduce quadratic form distance measure
- describe QF dissimilarity score
- describe application of QF dissimilarity score
- describe two-dimensional density-based merging
- describe extension to high-dimensional data
- describe template formation
- describe meta-cluster matching
- describe higher-level template formation
- summarize method advantages
- define relative frequency
- introduce spatial dissimilarity matrix
- calculate QF dissimilarity score
- identify matched clusters
- determine merging candidates
- recalculate QF dissimilarity score
- identify split or missing clusters
- apply QF dissimilarity score to k-dimensional data
- calculate additional information for matched clusters
- compare matched clusters in multiple dimensions
- track population changes across samples
- verify QF dissimilarity score using synthetic datasets
- analyze sensitivity of QF dissimilarity score to binning parameter
- demonstrate invariance of QF dissimilarity score to sample size
- apply method to real datasets
- introduce guidance display for sequential gating
- render graphical user interface
- display two-dimensional plot of data
- display guidance window with single parameter charts
- update guidance window based on user selection
- display graphical indications of prior selections
- provide user-defined threshold for adjusting background staining
- define guidance window features
- describe image capture feature
- introduce look aside feature
- explain marker hiding
- describe guidance window controls
- introduce parameter selection
- describe threshold adjustment
- explain color-coded density distribution
- describe single parameter chart generation
- introduce interactive display synchronization
- describe guidance window functionality
- introduce FMO control method
- describe automatic background gating
- introduce systems and devices
- describe computing system architecture
- introduce network diagram
- describe system modules
- introduce adaptive binning module
- describe dissimilarity module
- introduce matching and merging candidate identification module
- define dissimilarity module
- describe adaptive binning module
- explain combined binning pattern
- introduce quadratic form distance
- derive dissimilarity score equation
- describe matching and merging candidate identification module
- explain determination module
- introduce first interactive display module
- describe second interactive display module
- define hardware module
- explain software module
- describe processor-implemented module
- introduce cloud computing environment
- explain software as a service
- describe digital electronic circuitry
- explain computer hardware
- introduce firmware
- describe software
- explain computer program product
- introduce non-transitory computer readable medium
- describe computer storage media
- explain communication media
- conclude with machine-readable medium

### Example 1—Workflow for Automated Clustering and Alignment of Cell Populations in Flow Cytometry Data

- demonstrate application of embodiments of the method
- describe data workflow for analyzing datasets

### Example 2—Matching of Basophil Populations Between Patient Samples, Even when Marker Expression Levels Vary Between Patients

- describe human and mouse datasets
- demonstrate matching of basophil populations using method 100

### Example 3—Detection of Missing Lymphocyte Populations in the Peritoneal Cavity of RAG Knockout (RAG−/−) Mice

- describe sample preparation and preprocessing
- demonstrate detection of missing lymphocyte populations using method 100

### Example 4—Cluster Matching of the Murine Lymphoid, Myeloid and Granuloid Lineages Between PerC and Spleen

- describe data collection and preprocessing
- demonstrate cluster matching of immune cell subsets using method 100

### Example 5—Guided Gating of SSc Eosinophil Data

- describe guidance window functionality
- demonstrate guided gating of SSc Eosinophil data using the guidance window

