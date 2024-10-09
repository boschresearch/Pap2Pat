# DESCRIPTION

## BACKGROUND

- motivate unknown interventions

## SUMMARY

- outline analytics system
- describe intervention identification process

## DETAILED DESCRIPTION

### Definitions

- define notation for random variables
- define causal graph and Bayesian Network
- define intervention and causal Bayesian Network
- define mixture of interventions and intervention tuple
- define sample

### Overview

- introduce causal Bayesian Networks
- describe limitations of current analytics systems
- illustrate problem with email marketing example
- illustrate problem with gene-editing example
- describe existing solutions and their drawbacks
- introduce embodiments of the present invention
- describe conditions for determining interventions
- describe receiving samples and causal graph
- describe determining set of intervention tuples
- describe matching individual samples to interventions

### Example System for Identifying Interventions

- introduce system architecture
- describe user device and analytics system components
- explain communication between user device and analytics system
- outline analytics system functionality
- describe intervention identification module
- introduce causal graph example
- explain set of baseline samples and set of samples with interventions
- define intervention identification problem
- introduce positivity and exclusion assumptions
- estimate marginal and conditional probabilities
- enforce positivity on probability estimates
- determine set of intervention tuples for single variable
- set up system of equations for single variable
- enforce exclusion for single variable
- select set of intervention tuples for single variable
- lift solution from N variables to N+1 variables
- describe lifting process for multiple variables
- introduce intervention assignment module
- describe mapping samples to interventions
- outline user interface module functionality

### Example Methods for Identifying Interventions

- introduce method 300 for single variable
- receive input, including causal graph and samples
- determine estimated probability distributions
- perturb estimated probability distributions for positivity
- determine candidate sets of intervention tuples
- compare and select set of intervention tuples
- introduce method 400 for multiple variables
- lift solution to higher dimensions

### Performance Evaluation

- describe experiment 1: comparison with brute force baseline
- describe experiment 2: performance on larger graphs and varying sample sizes
- introduce simulation setup
- generate causal Bayesian network
- generate mixture model and samples
- set algorithm parameters
- define evaluation metrics: recall, RMSE, false-positive RMSE, false-negative RMSE
- present results: plots of recall, RMSE, false-positive RMSE, false-negative RMSE
- discuss results and implications

### Exemplary Operating Environment

- describe computing device 900
- introduce computer code or machine-useable instructions
- summarize system configurations
- describe bus 910 and its components
- explain computer-readable media
- detail memory 912 and its types
- describe presentation component(s) 916
- explain I/O ports 918 and I/O components 920
- discuss alternative embodiments and arrangements
- clarify scope and limitations of the invention

