# DESCRIPTION

## TECHNICAL FIELD

- relate to methods and apparatuses

## BACKGROUND

- motivate need for SOC determination
- define SOC and SOD
- limitations of SOC determination in LiS cells
- prior art methods for SOC determination

## BRIEF SUMMARY OF THE INVENTION

- introduce Lithium Sulfur chemistry limitations
- describe dynamic use conditions affecting Qt
- explain mechanism of active cathode material dissolution
- define state of health (SoH) and its importance
- motivate need for accurate SoH calculation
- introduce Lithium Sulfur batteries' advantages
- describe memory effect in Lithium Sulfur batteries
- introduce apparatus for modelling state of charge (SOC)
- describe cell model module and its functionality
- describe memory effect module and its functionality
- explain how apparatus adjusts cell model module
- introduce optional operational condition parameters
- describe alternative models for internal state of cell
- introduce apparatus for estimating SOC and SoH
- describe state estimator module and its functionality
- introduce battery management system
- describe apparatus for estimating state of charge
- describe apparatus for estimating range of electric vehicle
- describe apparatus for planning route for electric vehicle
- describe computer readable medium
- describe method for generating cell model
- describe alternative cell models
- describe method for generating memory model
- describe method for estimating state of charge
- describe method for estimating range of electric vehicle
- describe method for planning route for electric vehicle
- describe optional features of method for estimating state of charge
- describe optional features of method for estimating range of electric vehicle
- describe optional features of method for planning route for electric vehicle
- describe operational conditions of cell
- describe prediction error minimisation technique

## DESCRIPTION OF THE EMBODIMENTS

- introduce Lithium Sulfur cells
- describe memory effect in Lithium Sulfur cells
- explain limitations of internal resistance for SOC estimation
- introduce apparatus for modelling and estimating SOC and SOH
- describe cumulative history data collection
- outline cell operational condition measurement means
- explain internal resistance measurement using balancing resistor
- describe SOC model implementation
- outline cell model module and memory effect module
- explain adjusting cell model module based on operational history
- describe cell state estimator and SOC estimator modules
- outline alternative embodiments using ASICs or FPGAs

### Generating the Cell Model Module—Equivalent Circuit Example

- generate equivalent circuit model for cell
- describe experimental test data collection
- explain parameterisation of equivalent circuit model
- outline model structure selection
- describe open circuit voltage and ohmic resistance calculation
- explain diffuse resistance component calculation
- outline parameterisation process using relaxation phase curve
- describe look up table creation for RC branch resistances and capacitances

### Generating the Memory Effect Model

- introduce Lithium Sulfur memory effect
- motivate Qt variation with prior history and environmental conditions
- describe capacity variation under dynamic cycling
- define memory model and its connection to equivalent circuit model
- summarize tracking of sulfur material manifestations
- expand model to include degradation due to loss of active material
- generate and operate LiS model for a given cell
- cast sulfur species and reactions into rules for charge and discharge
- adjust operation of cell model to compensate for memory effect
- describe parametrization of simplified and complex memory models

### Parameterisation by Prediction Error Minimisation (PEM)

- introduce PEM method
- identify parameter values for cell model
- describe model structure selection
- select equivalent circuit model
- describe fitting parameters to model
- define fitness criteria
- minimize prediction error
- describe identification error minimisation
- select identification error minimisation algorithm
- calculate root mean square error (RMSE)
- illustrate RMSE values at different charge levels
- introduce real-time state of charge estimation methods
- describe Kalman-type filter method
- illustrate state of charge estimation method
- describe memory aware model deployment
- generate model specific to Lithium Sulfur chemistry
- implement equivalent circuit model in real-time embedded system
- describe application of model in battery management system

