# DESCRIPTION

## BACKGROUND

- motivate unknown interventions
- illustrate unknown interventions

## SUMMARY

- introduce analytics system
- determine intervention tuples
- solve system of equations
- match samples to interventions

## DETAILED DESCRIPTION

### Definitions

- define notation for random variables
- define probability notation
- define causal graph
- define Bayesian Network
- define causal Bayesian Network
- define intervention
- define interventional distribution
- define mixture of interventions
- define intervention tuple
- define sample
- define set of intervention tuples

### Overview

- introduce causal graphs and Bayesian Networks
- motivate interventions in causal Bayesian Networks
- describe limitations of current analytics systems
- illustrate example of email marketing system
- describe unintended intervention in email marketing system
- illustrate example of gene knockout experiments
- describe unintended intervention in gene knockout experiments
- describe existing solutions for unintended interventions
- describe limitations of existing solutions
- introduce embodiments of the present invention
- describe conditions for determining interventions
- describe positivity condition
- describe exclusion condition
- describe receiving set of samples with interventions
- describe receiving causal graph and baseline samples
- describe determining set of intervention tuples
- describe iterative process for determining intervention tuples
- describe generating and solving system of equations
- describe enforcing positivity and exclusion
- describe matching individual samples to interventions

### Example System for Identifying Interventions

- introduce system architecture
- describe user device and analytics system
- explain communication via network
- outline analytics system components
- introduce intervention identification module
- describe intervention assignment module
- outline user interface module
- define causal graph
- explain set of baseline samples
- explain set of samples with interventions
- illustrate causal graph for email marketing scenario
- define variables in causal graph
- explain positivity assumption
- explain exclusion assumption
- estimate marginal and conditional probabilities
- enforce positivity on estimates
- determine set of intervention tuples
- explain single variable case
- set up system of equations
- enforce exclusion
- compare candidate sets of intervention tuples
- select set of intervention tuples
- explain multiple variables case
- reduce problem to single variable
- lift solution to multiple variables
- marginalize on variable
- construct new causal graph
- recursively call algorithm
- lift solution for N variables to N+1 variables
- evaluate equation at different settings
- simplify system of equations
- enforce exclusion
- compare candidate sets of intervention tuples
- select set of intervention tuples
- map samples to interventions
- find intervention that maximizes probability
- return indication of intervention
- provide user interface
- receive input and provide output
- interact with analytics system

### Example Methods for Identifying Interventions

- introduce method 300 for determining intervention tuples
- receive input, including causal graph and samples
- determine estimated probability distributions
- perturb estimated probability distributions to ensure positivity
- determine candidate sets of intervention tuples
- enforce exclusion and solve system of equations
- compare candidate sets and select final set
- introduce method 400 for determining intervention tuples with multiple variables
- receive input, including causal graph and samples
- iteratively determine intervention tuples for N variables
- lift solution to N+1 variables
- determine final set of intervention tuples
- introduce method 500 for matching sample to intervention
- determine set of intervention tuples
- select sample and determine matching intervention
- match sample to intervention

### Performance Evaluation

- introduce two experiments to evaluate performance
- compare approach to brute force baseline
- generate causal graph and samples for experiment
- apply algorithms and compare accuracy metrics
- introduce simulation study for larger graphs and sample sizes
- generate directed acyclic graph and CPD for simulation
- generate samples and create mixture model
- set parameters for algorithm
- introduce evaluation metrics: recall, RMSE, false-positive RMSE, false-negative RMSE
- plot recall as sample size increases
- plot RMSE as sample size increases
- plot false-positive RMSE as sample size increases
- plot false-negative RMSE as sample size increases
- compare performance for different graph models
- plot average recall and RMSE as number of nodes increases
- discuss results and trends
- discuss sample complexity and dependence on number of nodes
- conclude performance evaluation

### Exemplary Operating Environment

- describe computing device
- introduce bus
- describe memory
- introduce processors
- describe presentation components
- introduce I/O ports
- describe I/O components
- describe power supply
- clarify bus representation
- discuss computing device categories
- introduce computer-readable media
- describe computer storage media
- describe communication media
- discuss memory types
- describe processor functionality
- describe presentation components
- describe I/O components
- discuss natural user interface
- describe gesture detection
- discuss alternative embodiments
- clarify scope of invention

