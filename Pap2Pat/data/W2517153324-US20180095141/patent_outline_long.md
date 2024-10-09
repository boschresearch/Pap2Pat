# DESCRIPTION

## TECHNICAL FIELD

- relate to methods and apparatuses

## BACKGROUND

- motivate need for SOC determination
- introduce difficulty of measuring residual energy
- define state of charge and state of discharge
- provide SOC formula
- explain initial SOC setting
- introduce Lithium Sulfur cell challenges
- describe OCV curve of Lithium Sulfur cell
- discuss limitations of resistance and temperature measurements
- discuss limitations of coulomb counting

## BRIEF SUMMARY OF THE INVENTION

- introduce Lithium Sulfur chemistry limitations
- describe dynamic use conditions
- explain Qt parameter variation
- define state of health (SoH)
- motivate Lithium Sulfur batteries
- describe pouch cell format
- introduce memory effect problem
- describe invention context
- introduce apparatus for modelling SOC
- describe cell model module
- describe memory effect module
- explain apparatus configuration
- describe operational condition of cell
- introduce equivalent circuit network model
- describe parameterised physics-based cell model
- introduce parameter value resource
- describe memory model
- explain reaction rates
- introduce simplified physical model
- describe memory effect module configuration
- introduce apparatus for estimating SOC
- describe cell operational condition monitor module
- describe state estimator module
- describe state of charge estimator module
- introduce electrochemical cell chemistry
- describe state of health estimation
- introduce iterative feedback loop
- describe kalman-type filter
- introduce prediction error minimisation technique
- describe cell operational condition measurement means
- introduce invention
- define parameter values
- motivate battery management system
- describe apparatus for estimating range
- describe apparatus for planning route
- describe computer readable medium
- motivate method for generating model
- describe method for generating model
- describe alternative cell models
- describe equivalent circuit network model
- describe operational condition of cell
- describe generating data for model
- describe predicting terminal voltage
- describe controlled testing of cells
- describe applying current pulses
- describe identifying parameters of model
- describe using open circuit voltage
- describe using instantaneous voltage drop
- describe using gradual voltage drop
- describe refining parameter values
- describe storing parameter values
- describe fitting parameter values to functions
- motivate method for generating memory model
- describe method for generating memory model
- describe establishing rules for reactant species
- describe parameterising reaction rates
- describe identifying parameterised values
- describe simplified physical model
- motivate method for estimating state of charge
- describe method for estimating state of charge
- describe estimating internal state of cell
- describe estimating usable capacity of cell
- describe estimating range of electric vehicle

## DESCRIPTION OF THE EMBODIMENTS

- introduce Lithium Sulfur cells
- describe memory effect in Lithium Sulfur cells
- explain limitations of internal resistance for SOC estimation
- introduce apparatus for modelling and estimating SOC and SOH
- describe cumulative history data collection
- introduce terminal voltage estimation method
- describe cell operational condition measurement means
- explain internal resistance measurement
- introduce SOC model
- describe cell model module
- explain parameter value resource
- introduce memory effect module
- describe memory model
- explain reaction rates parameterisation
- introduce cell state estimator
- describe SOC estimation method
- explain alternative embodiments
- introduce apparatus for creating SOC model
- describe cell state estimator implementation
- explain SOC model implementation
- introduce battery management system
- describe energy system controller
- explain plural cells implementation
- introduce specific implementations of apparatus

### Generating the Cell Model Module—Equivalent Circuit Example

- introduce equivalent circuit model
- describe test data generation
- explain current load application
- describe terminal voltage measurement
- introduce equivalent circuit network model
- describe model structure selection
- explain parameterisation process
- introduce open circuit voltage calculation
- describe ohmic resistance calculation
- explain diffuse resistance calculation
- introduce fitting procedure
- describe non-linear least squares technique
- explain look up table creation
- describe curve fitting
- introduce fitted polynomials
- explain model validation

### Generating the Memory Effect Model

- introduce Lithium Sulfur memory effect
- motivate Qt variation
- describe capacity variation experiment
- illustrate capacity variation results
- define memory effect
- introduce memory model
- describe memory model functionality
- expand memory model for degradation
- define state of health
- describe memory model operation
- generate LiS model rules
- calculate cell voltage
- predict reaction rates
- describe simplified memory model
- adjust ECN model for memory effect
- illustrate adjustment mechanism
- show modelled discharge curves
- illustrate capacity loss
- parametrise simplified memory model
- describe complex memory model variation

### Parameterisation by Prediction Error Minimisation (PEM)

- introduce PEM method
- describe advantages of PEM
- outline PEM procedure
- describe model structure selection
- illustrate equivalent circuit model
- describe model structure selection criteria
- describe fitting parameters to the model
- define prediction error
- describe iterative minimization procedure
- define fitness function
- describe identification error minimisation
- define RMSE criterion
- illustrate RMSE values
- describe real-time state of charge estimation methods
- illustrate state of charge estimation method
- describe current, voltage, and temperature measurement
- describe updating state vector
- describe using equivalent circuit model
- describe predicting model parameters
- describe estimating state of health
- describe outputting measurable parameters
- describe feedback loop
- describe increasing accuracy
- describe deploying memory-aware model
- describe generating model from experimental data
- describe implementing equivalent circuit model
- describe using Kalman-type filter
- illustrate real-time SOC/SOH estimation
- describe receiving measured values
- describe updating state vector
- describe predicting internal cell state
- describe correcting predictions
- describe adapting ECN model
- describe algorithm architecture
- describe deployment architectures
- describe selecting prediction horizon

