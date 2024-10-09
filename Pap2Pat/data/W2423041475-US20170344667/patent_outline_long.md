# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- introduce topology optimization
- discuss reliability based design optimization
- motivate failsafe design

## SUMMARY

- introduce failsafe design challenge
- introduce computational scheme
- define failsafe design problem
- introduce finite damage population
- introduce simple formulae for material survival rate
- introduce efficient computational scheme
- discuss MPI parallel implementation
- introduce automatic damage cube placement
- discuss HPC resources
- introduce Level-1 damage population
- introduce Level-2 damage population
- introduce partial damage population
- discuss added damage layers
- introduce computer-implemented method
- define structural continuum
- define damage volume
- introduce computational optimization
- discuss finite damage population
- introduce analysis models
- discuss computational structural analysis
- introduce system
- introduce non-transitory computer readable medium

## DETAILED DESCRIPTION

- introduce failsafe concept
- define failure test for topology optimization
- describe spherical damage model
- illustrate damage model with FIG. 1A
- define damage volume
- describe effect of damage volume
- formulate topology optimization problem
- define objective function
- define constraints
- introduce SIMP topology optimization approach
- describe power law penalty
- apply lower bound on density variables
- discuss damage shape alternatives
- introduce cube-shaped damage
- illustrate cube damage with FIG. 1B
- discuss orientation of damage cubes
- introduce solution strategy for failsafe topology optimization
- describe random placement of damage
- introduce Damage Series A (DS-A)
- describe base damage population
- illustrate base population with FIG. 2A
- describe damage population increase
- formulate design problem for DS-A
- introduce Damage Series B (DS-B)
- describe partial set of DS-A
- formulate design problem for DS-B
- summarize population size in Table 1
- discuss reliability of model for capturing random failure
- introduce best hideout location concept
- calculate material survival rate
- discuss sectional survival rate
- illustrate best hideout locations with FIGS. 2B and 2C
- compare DS-A and DS-B
- discuss convergence of damage population series
- discuss practical application of failsafe analysis
- introduce finite element analysis
- describe optimization problem in Eq. 1
- discuss computational expense
- introduce parallel processing
- describe Message Passing Interface (MPI) parallel algorithm
- illustrate failsafe algorithm with FIG. 3
- describe master process
- describe damage population generation
- describe analysis and sensitivity analysis
- describe convergence and constraint screening
- describe approximation and optimization process
- describe output and optimization end
- discuss practical measures for damage zone generation
- discuss reducing computation cost
- discuss preserving load conditions
- introduce three-bar truss example
- formulate optimization problem for three-bar truss
- discuss failsafe design results

### EXAMPLES

- introduce 2D example 1: rectangular plate under shear force
- describe finite element model
- illustrate damage population PB1
- illustrate damage population PB2
- show optimum for standard problem
- show failsafe designs with PB1 and PB2 damage populations
- provide models for damage population PB1
- list compliances of standard and failsafe designs
- list compliances for damage population PB2
- discuss difference in compliances
- introduce example 2: rectangular plate under bending force
- describe design domain and FEA mesh
- optimize with 50% volume constraint
- show damage population for PB1 and PB2
- show final designs for standard and failsafe
- list compliances of standard and failsafe designs
- show active damage zones for PB1 and PB2
- discuss results for base damage population PB1 and increased population PB2
- introduce example 3: 3D control arm
- describe dimensions and model
- apply 30% volume fraction constraint
- consider two load cases
- show base layer damage population PB1
- show enrichment layer for PB2
- show optimal designs for standard and failsafe
- list compliances of standard and failsafe designs
- discuss maximum compliance of damaged structure
- discuss failsafe features
- discuss additional implementations
- discuss use in various design applications
- discuss functional operations
- discuss computer storage medium
- discuss data processing apparatus
- discuss computer program
- discuss computer readable media

