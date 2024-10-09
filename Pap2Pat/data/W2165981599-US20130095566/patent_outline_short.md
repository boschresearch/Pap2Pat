# DESCRIPTION

## STATEMENT REGARDING FEDERAL FUNDING

- acknowledge government funding

## SUMMARY

- motivate systems biology
- introduce flux balance analysis
- describe limitations of FBA
- summarize method for optimizing biological activities
- describe application of method
- highlight advantages over existing methods
- outline embodiments of the invention

## DETAILED DESCRIPTION

- define terms and conventions
- introduce flux balance analysis for cell cultures
- describe limitations of prior methods
- introduce cytoplasmic molecular crowding and reaction kinetics
- derive mathematical framework for flux balance analysis with molecular crowding
- describe method for optimizing cell culture parameters
- provide example of implementation in computer
- describe biochemical reaction networks and their reconstruction
- introduce optimization methods for determining optimal properties
- describe use of reconstructed network for determining optimal properties
- discuss limitations of natural organisms in achieving optimal performance
- introduce methods for designing and constructing genetic makeup of cells
- describe perturbation of wild type network
- introduce in silico methods for optimization
- outline iterative design procedure for achieving desired performance
- describe computer system for optimization method
- detail database structure and content
- outline computer program product and its functions
- describe genetic makeup construction
- motivate optimization procedure
- describe optimization procedure
- describe cell culture optimization
- describe adaptive evolution
- describe culturing methods
- describe monitoring growth and metabolic behavior
- describe byproduct secretion monitoring
- describe computer-implemented method for optimal function
- describe computer-readable medium and device
- provide examples of implementation

## EXAMPLES

- provide abbreviations table

### Example 1

- study impact of limited solvent capacity on E. coli cell metabolism
- estimate crowding coefficients and perform metabolic flux predictions
- describe bacterial strain and general growth conditions
- detail metabolic enzyme activity assays
- provide enzyme assay protocols and calculate enzyme activities
- describe experimental setup
- perform flux measurements and analyses
- analyze glycogen glucose and RNA ribose
- determine lactate, glutamate, fatty acids, and TCA cycle activity
- describe flux data analysis and statistical methods
- describe RNA preparation for microarray analysis
- describe STEM clustering analysis
- describe querying expression data to identify specific expression profiles
- describe querying gene expression of operons in the central carbon metabolism
- present results of limited solvent capacity constraining metabolic rate
- describe FBAwMC predictions of metabolic fluxes and efficiency objective
- identify regulatory mechanism controlling metabolic switch
- discuss implications of solvent capacity constraint on metabolic modeling

### Example 2

- develop modified FBA model
- formulate optimization problem
- model crowding coefficients as noise
- estimate crowding coefficients from experimental measurements
- describe growth experiments and carbon substrate analyses
- detail microarray sample collection and analysis
- analyze microarray data from individual carbon source-limited media
- analyze microarray data from time series mixed-substrate experiment
- interpret results and discuss implications
- introduce querying expression data
- hierarchical clustering of time-series gene expression data
- probabilistic clustering of time-series data
- stress response analysis
- describe FBA with molecular crowding
- predict relative maximum growth of E. coli
- analyze substrate hierarchy utilization
- test FBAwMC E. coli model on mixed-substrate conditions
- correlate mode and sequence of substrate utilization
- analyze expression of genes participating in uptake modules
- discuss activation of stress programs upon switching metabolic phases
- discuss key findings and implications for systems biology

### Example 3

- motivate molecular crowding and kinetic modeling
- describe kinetic model of glycolysis
- provide rate equation models
- introduce experimental data
- describe catalytic constants and cell density
- define optimal metabolite concentrations
- derive limited solvent capacity constraint
- illustrate impact of limited solvent capacity constraint
- apply limited solvent capacity constraint to S. cerevisiae glycolysis
- predict optimal metabolite concentrations and enzyme activities
- discuss results and limitations of model
- conclude on importance of limited solvent capacity constraint

### Example 4

- introduce alternative glycolysis pathway with net zero ATP production
- motivate investigation of metabolic flux redistributions in proliferating cells
- describe genome-scale model of human cell metabolism
- formulate optimization problem to estimate metabolic fluxes and compartment densities
- discuss model parameters, including nutrient import costs and crowding coefficients
- predict changes in relative macromolecular densities with increased cell proliferation
- describe metabolic switch from low- to high-proliferation rates
- identify novel pathway for ATP generation involving serine biosynthesis and glycine cleavage systems
- analyze flux rates and ATP production in cells with net zero ATP glycolysis
- summarize results and implications for understanding cancer cell metabolism
- describe novel ATP-producing pathway
- model kinetic behavior of pathway
- analyze steady state of system
- determine feasibility of ATP production
- identify Myc as transcriptional regulator
- discuss regulation of novel pathway by Myc
- discuss implications of novel pathway on cell metabolism
- summarize advantages of novel pathway

## Materials and Methods

- define metabolic network reconstruction and crowding coefficients
- describe sensitivity analysis and simulations

