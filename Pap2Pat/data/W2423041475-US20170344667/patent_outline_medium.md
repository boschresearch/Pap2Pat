# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- summarize topology optimization

## SUMMARY

- motivate failsafe design
- identify challenges
- formulate failsafe design
- approximate problem
- disclose formula for material survival rate
- describe efficient computational scheme
- implement using MPI parallel implementation
- automate damage cube placement
- use HPC resources
- represent redundant load paths
- summarize various aspects of invention

## DETAILED DESCRIPTION

- motivate failsafe design concept
- define failure test for topology optimization
- introduce spherical damage model
- describe damage volume effect
- formulate topology optimization problem
- define objective function and constraints
- introduce SIMP topology optimization approach
- apply power law penalty to stiffness density relationship
- discuss damage population strategy
- introduce cube-shaped damage model
- describe Damage Series A (DS-A) and B (DS-B)
- formulate design problem for failsafe topology optimization
- simplify problem formulation for numerical examples
- discuss relationship between damage population size and material survival rate
- analyze geometric interaction of intersecting cubes
- discuss reliability of model for capturing random failure
- visualize damage population increase
- analyze sectional and volumetric survival rates
- discuss convergence of damage population series
- implement failsafe topology design framework using commercial FEA software
- describe iterative scheme of failsafe algorithm
- distribute models to computing nodes for analysis
- apply convergence and constraint screening
- conduct sensitivity analysis
- approximate and optimize design
- output final design and terminate optimization

### EXAMPLES

- introduce 2D examples
- describe rectangular plate under shear force
- illustrate finite element model
- show damage population PB1
- show damage population PB2
- illustrate optimum for standard problem
- show failsafe designs with PB1 and PB2
- provide compliances for standard and failsafe designs
- describe rectangular plate under bending force
- illustrate damage population for PB1 and PB2
- show final designs for standard and failsafe
- provide compliances for standard and failsafe designs
- describe 3D control arm example
- illustrate damage population for PB1 and PB2
- show optimal designs for standard and failsafe
- provide compliances for standard and failsafe designs
- discuss additional implementations

