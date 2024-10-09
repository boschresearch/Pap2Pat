# DESCRIPTION

## FEDERALLY-SPONSORED RESEARCH AND DEVELOPMENT

- disclose government rights

## BACKGROUND

- motivate acoustic source tracking

## DETAILED DESCRIPTION OF SOME EMBODIMENTS

- define terms and phrases used in the specification
- explain the meaning of "one embodiment" and "an embodiment"
- describe the use of "coupled" and "connected" in the specification
- define "comprises", "comprising", "includes", "including", "has", and "having"
- explain the use of "a" and "an" in the specification
- introduce the sparsity-driven approach for tracking broadband acoustic sources
- motivate the need for passive sonar in underwater source localization
- describe the challenges of underwater source localization via passive sonar
- summarize classical underwater source-localization techniques, including matched-field processing
- describe the limitations of matched-field tracking and Bayesian approaches
- introduce the sparsity-driven framework for broadband source localization via passive sonar
- describe the operational concept of a system for sparsity-driven passive tracking of acoustic sources
- explain the transformation of acoustic time-series data to the frequency domain
- introduce model-based prediction component
- illustrate operational environment and SLM
- propose model alleviating nonlinearities
- derive iterative estimator for S(t)
- illustrate grid of tentative locations
- describe structure of regression coefficient matrix S
- rewrite equation as real-valued convex optimization problem
- present alternative form of equation
- derive PG algorithm for solving equation 6
- define majorizer H for h
- describe PG iteration
- rewrite H as function of v_g's
- derive proximal operator
- describe parallel update of v_g's
- summarize PG algorithm
- define grid of tentative locations
- compute replicas using acoustic model
- collect time series data of actual acoustic measurements
- compute Fourier coefficient estimates using STFT
- construct set of Fourier coefficient vectors
- model Fourier coefficient vectors
- set to zero values associated to absent sources
- obtain estimate of acoustic source locations
- generate source location maps
- implement method as series of modules
- illustrate performance of broadband tracking algorithm
- discuss extensions to other acoustic source localization environments
- describe variations and modifications of the method

