# DESCRIPTION

## STATEMENT REGARDING FEDERAL FUNDING

- acknowledge government support

## SUMMARY

- motivate systems biology
- introduce flux balance analysis
- describe limitations of FBA
- summarize technologies described
- describe method for optimizing biological activities
- calculate optimal cell culture parameters
- initiate optimal cell culture parameters
- calculate maximum metabolic rate
- calculate optimal metabolite concentration
- calculate enzyme activity
- describe method for achieving optimal function
- calculate optimal properties of biochemical reaction network
- alter list of reactions
- repeat until desired optimal function
- describe computer-implemented method

## DETAILED DESCRIPTION

- define terms used in patent
- introduce flux balance calculations for cell cultures
- describe use of cytoplasmic molecular crowding in flux balance calculations
- describe use of reaction kinetics parameters in flux balance calculations
- outline applications of flux balance analysis
- introduce flux balance model of cellular metabolism
- describe stoichiometric matrix and reaction rates
- introduce enzyme concentration constraint
- describe effect of enzyme concentration constraint on metabolic fluxes
- outline method for optimizing biological activities in cell culture
- describe use of optimization method to calculate optimal cell culture parameter
- outline steps for initiating and maintaining optimal cell culture parameter
- reference prior art for flux balance analysis
- describe implementation of methods in computer
- outline design of biochemical reaction network for computer simulation
- describe optimization of cell growth and/or production of cellular constituent
- outline construction of genetic makeup of cell
- describe cultivation of cell to achieve desired performance
- outline types of biochemical reaction networks
- describe reconstruction of comprehensive biochemical reaction network
- outline determination of optimal properties of biochemical reaction network
- describe use of optimization methods to determine optimal properties
- outline simulation of metabolic network under varying environmental conditions
- describe assessment of metabolic capabilities of reconstructed metabolic network
- introduce in silico methods
- motivate optimization of biochemical reaction networks
- describe iterative design procedure
- outline optimization method
- describe computer system architecture
- detail database structure and content
- describe database annotations and sequence information
- outline biochemical genotype identification
- describe database types and external databases
- detail user interface and functionality
- describe computer program product and processing unit
- outline program code functionality and interactions
- mention adaptive evolution of cultured strains
- describe genetic makeup of cell
- introduce biochemical reactions
- motivate optimization procedure
- describe optimization procedure
- introduce iterative optimization
- describe cell culture optimization
- introduce specified environment
- describe optimal cultural parameters
- introduce glucose concentration
- describe culture conditions monitoring
- introduce computerized system
- describe adaptive evolution
- introduce natural or engineered strains
- describe selection pressure
- introduce extended cultivation
- describe acceleration of evolutionary process
- introduce culturing methods
- describe directional evolution
- introduce computer-implemented method
- describe flux balance analysis
- introduce solvent capacity
- describe computer-readable medium
- introduce device for achieving optimal function

## EXAMPLES

- provide abbreviations table

### Example 1

- study impact of limited solvent capacity on E. coli cell metabolism
- demonstrate relevance of constraint for fast growing cells
- predict metabolic switch between low and high nutrient abundance
- carry out flux measurements of several reactions
- perform gene expression and enzyme activity measurements
- discuss potential relevance of limited solvent capacity constraint
- estimate crowding coefficients for E. coli proteins
- implement Flux Balance analysis with Molecular Crowding
- describe bacterial strain and general growth conditions
- detail metabolic enzyme activity assays
- provide equations for calculating enzyme activities
- define flux measurements
- describe sample preparation
- outline GC-MS and NMR metabolome mapping platform
- explain mass isotopomer analysis
- detail glycogen glucose and RNA ribose stable isotope studies
- describe lactate, glutamate, and fatty acid analysis
- outline GC/MS settings and conditions
- summarize 13C, 1H and 31P NMR studies of intracellular metabolites
- describe flux data analysis and statistical methods
- describe RNA preparation for microarray analysis
- describe STEM clustering analysis
- describe querying expression data to identify specific expression profiles
- describe querying gene expression of operons in the central carbon metabolism
- state results
- describe limited solvent capacity constraining metabolic rate of fast growing E. coli cells
- estimate crowding coefficients using data from experimental reports
- describe FBAwMC predicting change of effective metabolic efficiency objective
- describe FBAwMC-predicted metabolic fluxes being within range of experimental values
- identify regulatory mechanism(s) controlling action of metabolic switch
- measure in vitro activity of selected enzymes catalyzing reactions in central carbon metabolism
- correlate changes in growth conditions with adjustments in cellular metabolism
- discuss regulatory mechanism(s) controlling action of metabolic switch
- discuss developing modeling framework to describe and predict experimentally observed behavior of organism
- discuss physicochemical constraints exerting main influences on cellular metabolism
- discuss incorporation of solvent capacity constraint into FBA modeling framework
- discuss flux predictions for several reactions of E. coli metabolism
- discuss interpretation of metabolic switch taking place between slow and fast growing E. coli cells

### Example 2

- develop modified FBA model
- predict maximum growth rate
- test model predictions
- obtain good agreement between model and experiment
- suggest macromolecular crowding constraint
- implement FBAwMC modeling framework
- model crowding coefficients as noise
- assign random value to crowding coefficients
- obtain results for different scenarios
- obtain maximum growth rate for each carbon source
- fit average crowding coefficient
- model temporal order of substrate uptake
- estimate crowding coefficients from experimental measurements
- define crowding coefficients
- estimate crowding coefficients from enzyme turnover numbers
- describe growth experiments and microarray analyses
- determine maximum growth rates experimentally
- analyze microarray data
- introduce querying expression data
- identify specific expression profiles
- hierarchical clustering of time-series gene expression data
- probabilistic clustering of time-series data
- stress response analysis
- biological functions of various genes
- results introduction
- FBA with molecular crowding predicts relative maximum growth
- substrate hierarchy utilization by E. coli cells
- FBAwMC E. coli model on mixed-substrate conditions
- surrogate markers of cellular metabolism
- mode and sequence of substrate utilization correlate with gene expression
- activation of stress programs upon switching metabolic phases
- hierarchical clustering with optimal leaf ordering
- principal component analysis
- probabilistic clustering method based on hidden Markov models
- discussion introduction
- identification of principles that define growth and substrate utilization mode
- experimental results indicate three major metabolic phases
- FBAwMC model captures main features of metabolic activities
- correlation between in vivo relative maximal growth rates and in silico predictions
- FBAwMC model predicts three metabolic phases and hierarchical mode of substrate utilization
- discrepancies of FBAwMC model predictions
- contribution of other cell components apart from metabolic enzymes
- constrained optimization approaches help understand regulatory mechanisms

### Example 3

- motivate molecular crowding and kinetic modeling
- introduce glycolysis pathway in S. cerevisiae
- describe kinetic model of glycolysis
- define optimization objective and crowding coefficient
- present rate equation models for glycolysis reactions
- provide mathematical equations for each reaction
- conclude with storage reaction equation
- introduce catalytic constants
- describe experimental data
- motivate optimal metabolite concentrations
- derive limited solvent capacity constraint
- define crowding coefficients
- analyze hypothetical three metabolites pathway
- describe reaction rates
- compute maximum metabolic rate
- apply to S. cerevisiae glycolysis
- investigate dependency of glycolysis rate
- perform global optimization
- predict optimal metabolite concentrations
- predict enzyme activities
- explore alternative optimization objectives
- compute maximum glycolysis rate
- discuss results
- summarize implications
- discuss limitations
- conclude

### Example 4

- introduce alternative glycolysis pathway with net zero ATP production
- motivate Warburg effect in cancer cells
- describe limitations of standard glycolysis pathway
- introduce genome-scale model of human cell metabolism
- define flux balance constraints
- describe minimum/maximum flux constraints
- describe minimum/maximum volume fraction constraints
- introduce molecular crowding constraints
- estimate model parameters
- discuss importance of effective turnover numbers
- describe sampling strategy for keff values
- introduce crowding coefficients for enzymes and ribosomes
- formulate flux balance equation for proteins
- describe protein synthesis and degradation
- model alternative glycolysis pathway
- predict changes in macromolecular densities with increased cell proliferation
- describe metabolic switch from low to high proliferation rates
- predict activation of glutamine uptake and α-ketoglutarate dehydrogenase activity
- identify novel pathway for ATP generation
- describe reactions involved in novel ATP generation pathway
- describe novel ATP-producing pathway
- illustrate reaction cycle with FIG. 29C
- model kinetic reactions
- analyze steady state of system
- determine maximum rate of ATP production
- discuss regulation of pathway by Myc
- identify transcription factors regulating pathway
- analyze gene expression data from Myc-driven liver cancer model
- discuss alternative glycolysis pathway with net zero ATP production
- describe anabolic requirements of cell growth and proliferation
- discuss molecular crowding as determinant of metabolic changes
- improve genome-scale metabolic model of human cell
- predict upregulation of glycolysis flux in highly proliferating cells
- support predictions with experimental observations
- discuss expression of genes in serine biosynthesis pathway
- describe novel ATP-producing pathway's endpoint
- discuss potential advantages of having two alternative glycolysis pathways

## Materials and Methods

- download metabolic network reconstruction data
- estimate crowding coefficients for mitochondria and ribosomes
- perform sensitivity analysis for enzyme turnover numbers
- estimate macromolecular composition and maintenance parameters
- describe simulation and microarray data analysis methods

