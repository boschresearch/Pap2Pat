# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce microbial metabolism
- motivate metabolic engineering
- describe recent advances in multiplex engineering
- describe recent advances in genome-editing
- describe recent advances in genome-wide regulation
- limitations of existing computational procedures
- describe linear programming approaches
- describe graph-based pathway design approaches
- limitations of existing approaches
- motivate overall stoichiometry

## SUMMARY OF THE INVENTION

- introduce computational framework
- describe selection of source and target metabolites
- describe combinatorial optimization
- describe search for intermediate biotransformations
- describe additional constraints
- describe case studies

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce computational framework
- motivate limitations of linear pathway designs
- formulate two-step computational procedure
- impose performance criteria on designed pathways
- illustrate implementation in pathway design studies

### 1.1 Material and Methods

- introduce optimization procedure
- describe step 1: determining optimal reactant and product combination
- introduce optimization task
- describe database of metabolites
- introduce parameters for elemental composition, charge information, and free energy of formation
- derive optimization formulation for step 1
- introduce performance criteria for overall conversion
- describe constraint for elemental and charge balances
- describe constraint for thermodynamic feasibility
- describe constraint for scaling decision
- extend optStoic formulation to account for more than two reactants and products
- describe impact of cellular growth requirements on flux allocation
- update overall stoichiometry to include biomass and growth associated maintenance ATP
- describe constraint for elemental and charge balances with biomass
- describe constraint for thermodynamic feasibility with biomass
- introduce profit margin considerations
- describe objective function for maximizing profit margin
- describe trade-offs between overall conversion stoichiometry and negativity of overall free energy of change
- introduce step 2: identifying reactions that conform to overall stoichiometry
- describe optimization formulation for identifying minimal number of reactions
- introduce parameters for stoichiometry matrix and free energy of each reaction
- describe bounds on flux of each reaction
- describe change in free energy of a reaction
- introduce reaction quotient
- describe minimum and maximum bounds on ΔG for each reaction
- determine reaction bounds
- introduce MILP problem for identifying minimal set of reactions
- describe objective function for minimizing sum of yj's
- describe constraint for stoichiometrically balanced manner
- describe constraint for flux of exchange reactions
- describe constraint for reaction bounds
- introduce integer cut constraints
- describe LP formulation as a surrogate of minRxn
- describe objective function for minimizing total metabolic flux
- describe constraints for LP formulation
- define optimization formulations
- introduce constraints for minRxn or minFlux optimization
- motivate limitations of reactions with positive standard free energy of change
- introduce binary variable uj
- define constraints for controlling number of organisms
- introduce parameter orgoj
- define constraint for selecting production host
- introduce results of case studies
- motivate case study 1: synthetic pathways for fully converting glucose to acetate
- introduce OptStoic step
- describe results of minRxn and minFlux optimization
- illustrate network designs for glucose to acetate conversion
- discuss limitations of NOG pathway
- introduce alternative network designs
- motivate case study 2: co-utilization of methanol and carbon dioxide to C2+ compounds
- introduce unknown product metabolite B
- discuss potential for higher carbon efficiency
- introduce exhaustive exploration of C2+ product metabolites
- summarize results of case studies
- conclude potential of optimization formulations
- define design objective
- introduce CO2 uptake
- discuss O:H ratio
- explain limitations of O:H ratio
- introduce four selected products
- describe network construction
- detail acetate production
- describe first module
- describe second module
- discuss alternative methanol condensation
- introduce second synthetic design
- describe histidine degradation metabolism
- introduce third design
- describe E. coli reactions
- detail glyoxylate shunt
- describe routes for C4, C5, and C6 products
- detail 3-hydroxybutyrate production
- detail 2-ketoisovalerate production
- detail phloroglucinol production
- highlight advantages of present invention
- introduce case study 3
- describe methane to acetate conversion
- discuss thermodynamic feasibility
- identify electron acceptors
- rank electron acceptors by carbon yield
- introduce material and methods
- select electron acceptors
- search for stoichiometry
- compare designs for electron acceptors
- analyze thermodynamic feasibility
- suggest minimal networks
- describe existing and novel routes
- identify cofactors
- analyze electron transfer
- describe alternate routes
- analyze cofactor balances
- describe existing strategies
- identify novel routes
- analyze carbon yields
- describe alternate pathways
- analyze energy efficiency
- describe shortest routes
- analyze ATP requirements
- describe unexplored pathways
- analyze TCA cycle
- describe 1,3-propanediol production
- analyze limitations of database
- introduce optStoic+minRxn/minFlux procedure
- discuss performance criteria
- discuss potential of procedure

### 2 Alternative Embodiments

- incorporate background references

## APPENDIX

- list abbreviations for terminal and intermediate metabolites
- define 10fthf
- define 13bpg
- define 23bdo
- list remaining abbreviations for metabolites
- conclude list of abbreviations for metabolites

### Abbreviation for the Reactions Described in the Minimal Networks

- list abbreviations for reactions
- define 3HBTDH
- define 3HPCH
- define 4HBTDH
- define 5MTHFRx
- list abbreviations for acetyl-CoA related reactions
- list abbreviations for acetoin related reactions
- list abbreviations for aconitase related reactions
- list abbreviations for aspartate related reactions
- list abbreviations for butanoyl-CoA related reactions
- list abbreviations for carbon monoxide related reactions
- list abbreviations for citrate related reactions
- conclude list of abbreviations for reactions

