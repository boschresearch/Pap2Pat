# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce microbial metabolism
- motivate metabolic engineering
- summarize existing computational procedures
- limitations of existing approaches
- introduce overall stoichiometry importance

## SUMMARY OF THE INVENTION

- introduce computational framework
- describe optimization steps
- summarize case studies

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce computational framework
- limitations of available pathway-design procedures

### 1.1 Material and Methods

- introduce optimization procedure
- describe step 1: determining optimal reactant and product combination
- introduce optimization task for step 1
- define parameters for optimization problem
- formulate optimization problem (optStoic)
- describe constraints for elemental and charge balances
- describe constraint for thermodynamic feasibility
- describe constraint for scaling decision
- extend optStoic formulation to account for more reactants and products
- describe impact of cellular growth requirements on flux allocation
- update overall stoichiometry to include biomass and growth associated maintenance ATP
- describe step 2: identifying reactions that conform to overall stoichiometry
- extract set of mass and charge balanced reactions from MetRxn database
- define parameters for identifying minimal number of reactions
- formulate MILP problem (minRxn) for identifying minimal number of reactions
- describe LP formulation (minFlux) as surrogate of minRxn
- describe method for exploring alternate optimal and suboptimal solutions
- define optimization formulations
- motivate constraints on reaction flux
- derive binary variable for reaction selection
- introduce organism selection constraint
- describe case study 1: glucose to acetate conversion
- summarize results of case study 1
- introduce case study 2: methanol and CO2 to C2+ compounds
- motivate co-utilization of methanol and CO2
- describe design of overall conversion for case study 2
- summarize results of case study 2
- define design objective
- identify feasible products
- analyze CO2 uptake and O:H ratio
- select products for network construction
- construct networks for acetate production
- describe alternative routes for acetate production
- construct networks for other target products
- highlight advantages of present invention
- introduce case study 3
- identify electron acceptors for methane conversion
- rank electron acceptors by carbon yield
- analyze results of electron acceptor combinations
- select electron acceptors
- search for stoichiometry
- compare designs for electron acceptors
- suggest minimal networks
- describe existing and novel routes
- identify cofactors
- describe alternate routes
- show existing strategies and novel routes
- identify alternate pathways
- discuss limitations of existing databases
- propose expansion of network design
- suggest integration of kinetic and toxicity information

### 2 Alternative Embodiments

- provide background and scope

## APPENDIX

- define abbreviations for terminal and intermediate metabolites
- define abbreviations for reactions described in minimal networks
- list all abbreviations

### Abbreviation for the Reactions Described in the Minimal Networks

- define enzyme-catalyzed reactions
- describe reactions involving CoA
- describe reactions involving NAD(P)
- describe reactions involving ferredoxin
- describe reactions involving other cofactors
- list all enzyme-catalyzed reactions

