# DESCRIPTION

## FEDERALLY SPONSORED RESEARCH AND DEVELOPMENT

- acknowledge government support

## BACKGROUND

- introduce immune system complexity
- motivate systems immunology approach
- limitations of current research tools
- importance of immune system modulation
- need for network analysis tools

## SUMMARY

- introduce ImmunoGlobe network
- define network nodes and edges
- categorize node types
- assign node subtypes
- associate nodes with standardized references
- describe edge attributes
- provide ontology for node relationships
- record additional edge information
- enable computational analysis methods
- convert to directed acyclic graph
- integrate with other databases
- build tools on top of ImmunoGlobe
- analyze immune function and dysfunction
- generate predictive diagnostics
- monitor disease activity
- identify targeted therapeutics
- input data for systems-level assessment
- analyze effects of combinatorial signaling
- generate quantitative graph-based knowledge

## DETAILED DESCRIPTION

- define scope of invention
- describe terminology
- explain singular and plural forms
- discuss ranges of values
- describe attributes of pathway elements
- explain assumed attributes
- discuss graphic representations
- describe cross-correlation techniques
- explain modification engine
- discuss inference reasoning
- describe influence levels
- explain assignment of influence
- discuss probabilistic pathway model
- describe integration of single study datasets
- explain standardization of data
- discuss matching data components to nodes
- describe calculation of association scores
- explain models for determining association scores
- discuss calculation of edge weights
- describe calculation of weighted interaction scores
- explain determination of activation state
- discuss measurement of gene expression
- describe various disease states
- explain comparison of analysis results
- discuss determination of difference values
- describe statistical analysis
- explain characterization of diversity
- discuss classification of results
- describe application of invention
- explain databases of network effects
- discuss computer-based systems
- describe data storage and transmission

### Databases

- describe databases of network effects
- explain recording of database information
- discuss computer readable media
- describe data storage structure
- explain data processor programs and formats
- discuss computer-based systems
- describe input and output means
- explain data analysis
- discuss Pearson correlation
- describe false discovery rate
- explain null distributions
- discuss permutation of values
- describe calculation of probability density function
- explain significance ordering
- discuss hierarchical clustering
- describe multidimensional scaling
- explain implementation in hardware or software
- discuss machine-readable storage medium
- describe computer programs
- explain output information
- discuss storage and transmission of data

## EXAMPLES

- introduce ImmunoGlobe: a manually curated intercellular immune interaction network

### Example 1

- motivate ImmunoGlobe
- describe ImmunoGlobe
- define immune interactome
- introduce Janeway's Immunobiology
- describe data extraction process
- record node attributes
- categorize node types
- visualize interactions
- describe edge types
- analyze network structure
- calculate degree distribution
- analyze node degrees
- describe cytokine nodes
- analyze cell node degrees
- describe antigen-presenting cells
- describe myeloid cells
- describe lymphocytes
- describe immune cell precursors
- analyze multi-step immune pathways
- describe Iwamoto et al. study
- describe Daftarian et al. study
- analyze network effects of immune stimuli
- describe mass cytometry experiment
- calculate composite activation score
- analyze activation scores
- describe correlation between distance and activation score
- describe correlation between number of shortest paths and activation score
- analyze species-specific differences
- categorize differences between mouse and human immune components
- describe Category 1 differences
- describe Category 2 differences
- describe Category 3 differences
- describe Category 4 differences
- analyze distribution of species-specific differences
- describe differences in innate immune functions
- describe differences in antigen presentation
- describe differences in immune cell ratios
- describe differences in surface markers
- analyze differences in B cells and NK cells
- describe differences in Toll-like receptors
- describe differences in antimicrobial molecules
- compare ImmunoGlobe and immuneXpresso networks
- visualize ImmunoGlobe subgraph
- visualize immuneXpresso network
- analyze differences between ImmunoGlobe and immuneXpresso
- generate adjacency matrix
- analyze edges unique to ImmunoGlobe
- analyze edges unique to immuneXpresso
- analyze shared edges
- compare number of references for edges
- motivate graph-based analysis
- describe paired source and target nodes with differing edge types
- analyze high-level features of ImmunoGlobe network
- describe applications of ImmunoGlobe in drug discovery
- describe future directions for ImmunoGlobe

### Example 2

- gather immunoprofiling data
- describe datasets and original studies
- standardize data
- motivate immune profiles varying widely across COVID patients
- describe heterogeneity in immune responses
- illustrate frequencies of immune cells and concentrations of cytokines
- show variability across ages and genders
- discuss individual variation in immune systems
- describe changes in immune cell frequencies
- focus on lymphopenia
- correlate lymphopenia with disease severity
- describe changes in immune cell populations
- show expansion of Th17 cells
- discuss polarization of adaptive immune response
- describe upregulation of inflammatory cytokines
- associate cytokine levels with disease severity
- illustrate impact of cytokine dysregulation
- describe activation of immune modules
- discuss concurrent activation of multiple modules
- identify correlations among immune components
- examine differences in immune activity
- identify statistically significant relationships
- trace shortest directional paths in immune network
- calculate weighted values for edges
- create network visualization
- run ranked edge enrichment analysis
- identify enriched immune processes
- visualize inferred edges on network diagram
- compare COVID patients and controls
- examine network differences between moderate and severe COVID
- identify gender differences in COVID-19 infection
- discuss implications of gender differences
- summarize immune response differences

### Example 3

- introduce applications of systems immunology to cancer
- describe complexity of cancer
- motivate systems biology approaches
- discuss interface between tumor and immune system
- describe immune response to radiation-induced tumor regression
- investigate role of immune system in radiation therapy
- test hypothesis on accelerated radiation treatment
- describe results of radiation treatment
- discuss immune-mediated nature of tumor remission
- examine antibody isotypes in antitumor immune response
- analyze IgG subtypes in serum
- identify Type 1 immune response
- discuss implications of Type 1 immune response
- describe strengths of systems immunology approach
- illustrate connections between cells and cytokines
- identify potential targets for immune modulation
- summarize value of systems immunology perspective

## Methods

- create edge list
- record interactions
- extract node attributes
- create node attributes table
- define node types
- link cell nodes to cell ontology
- link protein nodes to UNIPROT
- note species specificity
- build ontology
- standardize node names
- standardize immune process annotations
- standardize anatomical locations
- standardize disease annotations
- create edge list from ontology
- analyze network using igraph package
- generate network visualizations
- compare mouse and human networks
- extract differences between mouse and human immune systems
- classify differences
- assign differences to affected nodes
- compare with immuneXpresso network
- download edges from immuneXpresso
- merge and reformat edges
- compare edges between networks
- prepare mouse splenocytes for stimulation
- stimulate splenocytes with IFNγ, TNFα, or LPS
- perform mass-tag cellular barcoding
- stain cells with mass cytometry antibodies
- measure cell populations using mass cytometry
- normalize mass cytometry data
- gate cell populations
- acquire and standardize datasets
- measure immune cell populations
- measure cytokine data
- construct linear mixed effects models
- identify correlations that differ between COVID and healthy
- perform immune network pathway tracing

## Notes

- introduce node classification
- define naïve and activated/effector cells
- describe B cell node
- define antigen presenting cells
- review edge definitions
- summarize abstract of Iwamoto et al. study
- describe TNF-alpha differentiation pathway
- summarize abstract of Daftarian et al. study
- describe IL-10 production regulation
- compare ImmunoGlobe and immuneXpresso networks
- describe data download and processing
- define edge comparison criteria
- describe visual network representation
- outline limitations of comparison

