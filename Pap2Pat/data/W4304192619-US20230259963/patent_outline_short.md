# DESCRIPTION

## BACKGROUND

- motivate unknown interventions

## SUMMARY

- outline intervention identification

## DETAILED DESCRIPTION

### Definitions

- define notation and terminology
- define key concepts (e.g., causal graph, Bayesian Network, intervention, mixture of interventions)

### Overview

- introduce problem of modeling interventions in causal Bayesian Networks
- describe limitations of current analytics systems
- illustrate problem with examples (e.g., email marketing, gene knockout experiments)
- describe existing solutions and their drawbacks
- introduce embodiments of the present invention

### Example System for Identifying Interventions

- introduce system architecture
- describe user device and analytics system components
- explain causal graph and sample sets
- define intervention identification module functionality
- describe positivity and exclusion assumptions
- outline estimation of marginal and conditional probabilities
- detail determination of intervention tuples for single variable
- describe lifting solution from N variables to N+1 variables
- outline intervention assignment module functionality
- describe user interface module functionality

### Example Methods for Identifying Interventions

- receive input and determine estimated probability distributions
- perturb estimated probability distributions to ensure positivity
- determine candidate sets of intervention tuples using estimated probability distributions
- select set of intervention tuples from candidate sets

### Performance Evaluation

- compare technology to brute force baseline on small graph
- evaluate performance on larger graphs and varying sample sizes
- analyze results using recall, RMSE, false-positive RMSE, and false-negative RMSE metrics
- discuss results and implications for sample complexity and graph topology

### Exemplary Operating Environment

- describe computing device
- define computer-readable media
- illustrate memory and processor components
- explain input/output components and natural user interface
- discuss scope and variations of the invention

