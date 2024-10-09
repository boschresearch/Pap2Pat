# DESCRIPTION

## TECHNICAL FIELD

- introduce technical field of invention

## BACKGROUND

- motivate state of charge determination
- limitations of existing methods

## BRIEF SUMMARY OF THE INVENTION

- motivate Lithium Sulfur batteries
- describe limitations of prior art
- introduce state of health calculation
- describe importance of considering history of cell
- outline apparatus for modelling state of charge
- describe memory effect module
- outline apparatus for estimating state of charge
- introduce battery management system
- describe apparatus for estimating state of charge
- describe apparatus for estimating range of electric vehicle
- describe apparatus for planning route for electric vehicle
- describe method for generating cell model
- describe method for generating memory model
- describe method for estimating state of charge
- describe method for estimating range and planning route

## DESCRIPTION OF THE EMBODIMENTS

- motivate Lithium Sulfur cells
- describe limitations of other battery systems
- explain memory effect in Lithium Sulfur cells
- introduce apparatus for modelling and estimating SOC and SOH
- describe components of the apparatus
- outline method for estimating SOC and SOH

### Generating the Cell Model Module—Equivalent Circuit Example

- generate equivalent circuit model for the cell
- describe experimental test method for parameterising the model
- explain parameterisation process for the model
- describe creation of look up tables for the model

### Generating the Memory Effect Model

- motivate memory effect
- describe memory model
- implement memory model
- apply memory model to SOC estimation
- parametrize memory model

### Parameterisation by Prediction Error Minimisation (PEM)

- introduce PEM method
- describe model structure selection
- explain fitting parameters to the model
- detail identification error minimisation
- introduce real-time state of charge estimation methods
- describe Kalman-type filter implementation
- explain state of health estimation
- detail deployment architectures
- discuss model applications

