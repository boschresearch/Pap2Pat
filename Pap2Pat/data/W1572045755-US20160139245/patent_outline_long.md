# DESCRIPTION

## FEDERALLY-SPONSORED RESEARCH AND DEVELOPMENT

- disclose government rights

## BACKGROUND

- motivate acoustic source tracking

## DETAILED DESCRIPTION OF SOME EMBODIMENTS

- define embodiment notation
- explain "coupled" and "connected"
- define "comprises" and "includes"
- explain use of "a" and "an"
- introduce sparsity-driven approach
- motivate source location maps (SLMs)
- describe iterative solver based on proximal gradient (PG) method
- motivate localization and tracking of acoustic sources
- describe challenges of underwater source localization
- introduce matched-field processing (MFP)
- describe limitations of MFP
- introduce matched-field tracking (MFT)
- describe limitations of MFT
- introduce Bayesian approaches
- describe limitations of Bayesian approaches
- introduce sparsity-driven Kalman-filter approaches
- describe limitations of sparsity-driven Kalman-filter approaches
- introduce relevance vector machine
- describe embodiments of sparsity-driven framework
- introduce system 10 block diagram
- describe acoustic sensor array 50
- transform acoustic time-series data to frequency domain
- describe model characterizing acoustic propagation
- introduce spectral passive-acoustic tracking problem
- describe estimation of source locations
- describe signal transmission and processing
- introduce model-based prediction component
- illustrate operational environment and SLM
- propose model alleviating nonlinearities
- define equation for yf(t)
- explain group sparsity and temporal dependency
- propose iterative estimator for S(t)
- define equation for Ŝ(t)
- illustrate grid of tentative locations
- explain structure of regression coefficient matrix S
- construct SLM using whole rows of S
- write equation as real-valued convex optimization problem
- define notation for real and imaginary parts
- illustrate structure of {hacek over (S)}
- explain limitations of interior point methods
- propose PG solver for convex optimization problem
- rewrite equation to induce resilience to model mismatch
- introduce PG algorithm
- derive equation 8
- explain majorizer H
- illustrate majorizer H in FIG. 8
- describe PG iteration
- rewrite equation 9
- derive equation 10
- explain gradient-descent step
- derive equation 12
- describe proximal operator
- explain parallel update
- derive equation 14
- summarize PG algorithm
- describe algorithm termination
- discuss accelerated PG algorithm
- define grid of tentative locations
- estimate number of acoustic sources
- compute replicas using acoustic model
- collect time series data of actual acoustic measurements
- compute Fourier coefficient estimates using STFT
- construct set of Fourier coefficient vectors
- model Fourier coefficient vectors
- set to zero values associated to absent sources
- obtain estimate of acoustic source locations
- generate SLMs over grid per frequency
- implement method as series of modules
- store information on storage media
- provide information to device
- illustrate performance of broadband tracking algorithm
- describe environment of SWellEX-3 dataset
- define grid of locations
- compute replicas using KRAKEN normal-mode propagation model
- illustrate bathymetry and range trajectory of towed acoustic source
- describe use of matched-field tracking
- illustrate depth and range tracks obtained using matched-field tracking
- illustrate SLM obtained using PG solver
- compare convergence of PG and APG solvers
- simulate presence of two sources using SWellEX-3 dataset
- illustrate range tracks obtained for two sources
- discuss extension to other acoustic source localization environments
- discuss use of spatially distributed arrays for localization
- describe scope of claims

