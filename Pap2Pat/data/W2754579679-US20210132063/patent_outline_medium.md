# DESCRIPTION

## FIELD OF THE INVENTION

- introduce Plasmodium vivax and diagnostic test

## BACKGROUND OF THE INVENTION

- describe Plasmodium vivax life cycle
- explain liver-stage infection and relapse
- discuss diagnosis of P. vivax infections
- motivate need for accurate diagnosis
- summarize prior art diagnostic methods
- highlight limitations of prior art
- introduce proteins for diagnostic purposes
- discuss prior art protein characterization

## BRIEF SUMMARY OF THE INVENTION

- introduce system, method, apparatus and diagnostic test
- describe determination of infection timing
- explain identification of hypnozoites
- discuss determination of recent infections
- introduce antibody measurements
- estimate time since last infection
- determine medium-term serological exposure
- detect silent infections
- detect dormant infections
- determine progression of infection
- measure antibody levels
- select antibodies for measurement
- use biologically-motivated model for decay

## EXAMPLE 1

### Testing of Antigens

- introduce field sites and sample collection

### Materials and Methods

- ethics statement
- field sites and sample collection: antigen discovery study
- field sites and sample collection: validation study
- negative control samples
- protein expression
- AlphaScreen assay for antigen discovery study
- multiplexed bead-based assay for validation study
- statistical modelling

### Protein Expression.

- express full-length proteins
- express protein fragments
- confirm protein expression by western blot

### AlphaScreen® Assay for the Antigen Discovery Study.

- measure antibody responses using AlphaScreen assay

### Multiplexed Bead-Based Assay for the Validation Study.

- measure IgG levels using multiplexed bead-based assay

### Statistical Modelling.

- describe statistical models

### Statistical Analysis.

- perform statistical analysis using R, Prism, and Stata

### Results

- down-select candidate serological markers
- describe antibody kinetic profiles
- perform model-based down-selection
- rank antigens based on probability of inclusion
- exclude antigens with unfavorable production characteristics
- generate final list of candidate serological markers
- validate candidate serological markers geographically
- validate candidate serological markers in association with recent and past infection

## EXAMPLE 2

### Illustrative Diagnostic Test

- describe diagnostic test methods

## EXAMPLE 3

### Illustrative Software Process for Diagnosis

- introduce software process for diagnosis

### Section 1—Overview of Calibration Data and Algorithms

- motivate calibration and validation data
- describe algorithm inputs and outputs
- discuss factors for defining algorithm inputs and outputs
- outline decision making requirements

### Algorithms

- introduce classification and regression algorithms

### Section 2—Expanded Details of Algorithms

- introduce linear discriminant analysis
- describe quadratic discriminant analysis
- introduce decision trees
- describe random forests
- motivate modelling of antibody dynamics
- describe longitudinal antibody titers
- model antibody dynamics using mixed-effects linear regression
- estimate antibody decay rates
- describe estimation using antibodies to a single antigen
- derive probability distribution of expected antibody titer
- calculate probability distribution of time since infection
- introduce combined antibody dynamics
- describe estimation using antibodies to multiple antigens
- select optimal combinations of antigens
- apply simulated annealing algorithm

