# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- disclose government support

## FIELD OF THE INVENTION

- define fields of data analysis and visualization

## BACKGROUND

- motivate need for sample comparison
- describe limitations of manual gating
- introduce automated clustering methods
- explain curse of dimensionality
- describe first approach to cluster matching
- discuss limitations of first approach
- describe second approach to cluster matching
- discuss limitations of second approach
- motivate need for improved cluster matching
- motivate need for user guidance in sequential gating

## BRIEF SUMMARY

- introduce multidimensional cluster matching
- introduce visualization of multidimensional data
- describe method for matching clusters in data
- describe obtaining first sample data and second sample data
- describe identifying clusters in first sample data and second sample data
- describe performing multivariate adaptive binning
- describe determining combined binning pattern
- describe applying combined binning pattern separately
- describe generating histograms for identified clusters
- describe determining dissimilarity score for combinations
- describe using quadratic form distance for multi-dimensional data
- describe identifying matched clusters and merging candidates
- describe determining lowest dissimilarity score for each cluster
- describe identifying matched clusters and merging candidates
- describe determining whether merging candidate corresponds to split or missing cluster
- describe combining merging candidate with nearest cluster
- describe calculating new dissimilarity score for combined cluster
- describe identifying merging candidate as split or missing cluster
- describe performing multivariate adaptive binning in k-dimensions
- describe dividing data into k-dimensional bins
- describe determining dissimilarity score for each combination
- describe using equation for dissimilarity score
- describe calculating aij
- describe identifying matched clusters and merging candidates
- describe determining distance between geometric means
- describe identifying unmatched clusters
- describe system for matching clusters in data
- describe memory and storage for data
- describe processor and modules
- describe adaptive binning module
- describe dissimilarity module
- describe matching and merging candidate identification module
- describe determination module
- describe applying combined binning pattern separately
- describe generating histograms for identified clusters
- describe determining dissimilarity score for combinations
- describe identifying matched clusters and merging candidates
- describe determining whether merging candidate corresponds to split or missing cluster
- describe method for rendering graphical user interface
- describe rendering first interactive display
- describe rendering second interactive display
- describe displaying two-dimensional plot
- describe displaying single parameter charts or graphs
- describe receiving user selection of guidance feature
- describe modifying second interactive display
- describe receiving user selection of portion of two-dimensional plot
- describe modifying single parameter charts or graphs
- describe displaying graphical indication of threshold

## DETAILED DESCRIPTION OF THE INVENTION

### Definitions

- define item
- define gating
- define gate
- define marker
- define reagent
- define stain
- define staining reagent
- note on singular forms
- note on "one embodiment"
- introduce cluster matching
- describe clustering
- describe aligning cell subsets
- introduce population matching
- describe separate clustering and matching
- describe joint clustering and matching
- criticize conventional methods
- introduce dissimilarity measure
- describe criteria for dissimilarity measure
- describe distance metrics
- criticize Earth Mover's Distance
- introduce quadratic form distance measure
- describe QF dissimilarity score
- describe QF score properties
- describe QF score advantages
- describe multi-dimensional cluster matching
- describe high-dimensional cluster matching
- describe two-dimensional density-based merging
- describe cluster identification methods
- describe template formation
- describe meta-cluster formation
- describe higher-level template formation
- describe resulting template
- describe problems with conventional clustering
- describe QF distance metric
- describe multivariate QF distance metric
- describe cluster matching method
- describe method advantages
- describe example method 100
- obtain sample data sets
- identify clusters in sample data sets
- perform multivariate adaptive binning
- apply combined binning pattern
- generate histograms
- calculate dissimilarity scores
- describe quadratic form distance equation
- describe method for forming template
- describe method for matching meta-clusters
- describe resulting template
- define relative frequency
- introduce spatial dissimilarity matrix
- derive QF dissimilarity score
- describe application of QF dissimilarity score
- identify matched clusters
- determine merging candidates
- recalculate QF dissimilarity score
- identify split or missing clusters
- describe multidimensional application
- calculate additional information
- describe cluster matching
- track population changes
- verify QF dissimilarity score
- demonstrate sensitivity to binning parameter
- demonstrate invariance to sample size
- introduce visualization of multivariate data
- describe guidance for sequential gating
- render graphical user interface
- describe first interactive display
- describe second interactive display
- display single parameter charts
- convert logical scales
- arrange bar charts
- label y-axis
- indicate prior selections
- depict density of measurements
- indicate current markers
- include user-defined threshold
- adjust visual representation
- display additional information
- reset threshold
- display median value
- describe embodiments
- describe flow cytometry data
- describe cytometry system
- describe multidimensional alignment
- describe sequential gating
- describe guidance display
- describe plot editor window
- describe look ahead/look aside window
- describe selection of subset
- describe update of guidance window
- describe conversion of logical scales
- describe arrangement of bar charts
- describe embodiments of guidance window
- define guidance window
- describe features of guidance window
- introduce image capture feature
- describe look aside feature
- describe hiding markers in guidance window
- describe controlling plot editor window
- describe navigating gating sequence
- describe graphical features for selection
- describe adjusting threshold line
- describe histogram selection feature
- describe color-coded density distribution
- describe generating single parameter charts
- describe synchronizing interactive displays
- describe rapid visualization of staining dimensions
- describe guiding two-dimensional clustering sequences
- describe controlling changing parameters
- describe storing adjustments in analysis template
- describe method for automatic background gating
- describe overlaying fully stained sample with FMO control
- define cut-off percentile value
- describe ruling out events from gating selections
- describe example method using guidance window
- describe systems and devices
- describe computing system or computing device
- describe fixed media program component
- describe information appliance or digital device
- describe CPU and input devices
- describe storage media and monitor
- describe communication port and fixed media
- describe microscope or viewer or detector
- describe sampling handling and light source
- describe filters and CCD camera
- describe network diagram
- describe devices and servers
- describe database and database server
- describe system implemented in modules
- describe adaptive binning module
- describe dissimilarity module
- describe matching and merging candidate identification module
- describe determination module
- define dissimilarity module
- describe adaptive binning module
- introduce matching and merging candidate identification module
- explain determination module
- describe first interactive display module
- describe second interactive display module
- define hardware module
- explain software module
- describe processor-implemented module
- introduce cloud computing environment
- describe software as a service (SaaS)
- explain digital electronic circuitry
- describe computer hardware
- introduce firmware
- describe software
- explain computer program product
- describe machine-readable medium
- introduce computer storage media
- describe communication media
- explain computer program
- describe stand-alone program
- introduce module, subroutine, or other unit
- describe special purpose logic circuitry
- explain client and server
- describe programmable computing system
- introduce hardware architecture
- describe software architecture
- explain machine
- describe computer system
- introduce processor
- describe main memory
- explain static memory
- describe bus
- introduce video display unit
- describe alphanumeric input device
- explain user interface (UI) navigation device
- describe disk drive unit
- introduce signal generation device
- describe network interface device
- explain machine-readable medium
- describe instructions
- introduce data structures
- describe transmission medium
- explain communications network
- describe functional units or processors
- summarize modifications and changes

### Example 1—Workflow for Automated Clustering and Alignment of Cell Populations in Flow Cytometry Data

- introduce example 1
- describe data preprocessing
- apply method 100 for cluster matching
- discuss results of cluster matching

### Example 2—Matching of Basophil Populations Between Patient Samples, Even when Marker Expression Levels Vary Between Patients

- introduce example 2
- describe data collection and preprocessing
- apply method 100 for cluster matching
- discuss results of cluster matching

### Example 3—Detection of Missing Lymphocyte Populations in the Peritoneal Cavity of RAG Knockout (RAG−/−) Mice

- introduce example 3
- describe data collection and preprocessing
- apply method 100 for cluster matching
- discuss results of cluster matching

### Example 4—Cluster Matching of the Murine Lymphoid, Myeloid and Granuloid Lineages Between PerC and Spleen

- introduce example 4
- describe data collection and preprocessing
- apply method 100 for cluster matching
- discuss results of cluster matching
- highlight unmatched cell subsets

### Example 5—Guided Gating of SSc Eosinophil Data

- introduce example 5
- describe guidance window functionality
- apply guidance window for gating
- discuss results of gating
- describe overlay of sample data with FMO control sample data

