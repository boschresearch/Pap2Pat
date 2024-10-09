# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate need for interactive prosthetics
- limitations of current prosthetics
- challenges of simulating musculoskeletal dynamics
- summarize prior art approaches

## DETAILED DESCRIPTION

- introduce musculoskeletal dynamics approximation method
- preselect polynomials for muscle moment arms and lengths
- generate lists of candidates for expanding polynomials
- select suitable candidates for expanding polynomials
- expand polynomials by selected candidates
- determine if further expansion is possible and beneficial
- estimate musculoskeletal dynamics based on polynomial structures
- define terminology for patent application
- describe relative terms for device relationships
- define "connected to" and "coupled to" terms
- define "memory" and "memory device" terms
- define "processor" term
- describe exemplary embodiments with reference to figures
- introduce OpenSim model of human right arm and hand
- describe model geometry and muscle paths
- describe model development and kinematic variables
- introduce polynomial structure for approximating muscle moment arms and lengths
- describe polynomial terms and coefficients
- introduce list of potential candidates for expanding polynomials
- describe plots of kinematic variables vs. radians
- introduce flow diagram of approximation method
- receive input dataset associated with muscle length and moment arms
- generate polynomials that approximate muscle length and moment arms
- generate lists of candidates for expanding polynomial structures
- select suitable candidates for expanding polynomial structures
- expand polynomial structures by selected candidates
- determine if further expansion is possible and beneficial
- estimate musculoskeletal dynamics based on polynomial structures
- constrain polynomial terms using relationship between muscle length and moment arms
- integrate moment arm polynomials
- join integrals with expanded muscle length polynomial
- differentiate new muscle length polynomial to produce new moment arm polynomials
- describe optimization algorithm based on forward stepwise regression
- calculate corrected Akaike Information Criterion (AICc)
- compare models corresponding to expanded polynomial structures
- choose best model based on AICc
- describe iteration of approximation method vs. precision of fit
- introduce similarity index for assessing polynomial structures
- conclude description of musculoskeletal dynamics approximation method

### Equation 4

- define similarity index
- illustrate search for polynomial terms
- introduce DOF-independent polynomial vector
- define Agnostic polynomial vector
- calculate structural difference of polynomials
- calculate memory required for spline approximation
- calculate memory required for polynomials
- evaluate time required for polynomial evaluation
- analyze composition of approximating polynomials
- test similarity of composition across multiple muscle groups

### Approximation of Muscle Lengths and Moment Arms

- illustrate histograms of error in estimation
- demonstrate similarity index vs. number of muscles
- show relationship between number of terms and DOFs
- demonstrate non-random structure in polynomial composition
- evaluate precision of spline and polynomial models
- compare AIC of polynomial and spline models
- discuss evaluation time and memory usage

### Structure of Approximating Polynomials

- examine difference in polynomial structure
- discuss relative complexity of polynomials

### Structure and Function

- develop DOF-independent vectors for muscle lengths
- generate heatmap and dendrogram of distances
- project vectors on two first principle components
- identify clusters of muscles based on function
- discuss internal organization of muscle polynomial vectors
- generate distributions of distances between muscles
- compare distances between muscles that share a DOF
- compare distances between muscles that do not share a DOF
- calculate difference in distance between muscles
- perform statistical tests on distributions
- discuss results of statistical tests
- generate distributions of distances between muscles with same function
- generate distributions of distances between muscles with different functions
- calculate difference in distance between muscles with same function
- perform statistical tests on distributions
- discuss results of statistical tests
- conclude that polynomial term composition captures anatomical and functional relationships
- discuss significance of results
- illustrate system for biomimetic processing of biological inputs
- show live physics model of human hand in simulated environment

### Inventive Aspects

- provide approximation method for generating model
- receive input dataset associated with muscle length and moment arm
- generate muscle length polynomial and moment arm polynomial
- expand muscle length polynomial by additional term
- expand moment arm polynomial by additional term
- approximate dynamics of device based on expanded polynomials
- receive input dataset associated with muscle length and moment arm
- generate muscle length polynomial and moment arm polynomial
- expand muscle length polynomial by additional term
- expand moment arm polynomial by additional term
- determine whether polynomials are further expandable
- approximate dynamics of device based on expanded polynomials
- reiterate expansion and determination steps
- generate lists of potential candidates for expansion
- select candidates for expanding muscle length and moment arm polynomials
- expand polynomials by selected candidates
- integrate expanded moment arm polynomial to produce integrals
- join integrals with muscle length polynomial to obtain constrained polynomial
- differentiate constrained polynomial to obtain constrained moment arm polynomials
- determine whether constrained polynomials are further expandable
- approximate dynamics of device based on constrained polynomials
- analyze candidates to determine greatest improvement in fitting
- calculate AIC for input dataset
- use AIC in analysis to determine greatest improvement
- receive input dataset associated with muscle length and moment arm
- generate muscle length polynomial and moment arm polynomial
- expand muscle length polynomial by additional term
- expand moment arm polynomial by additional term
- integrate expanded moment arm polynomial to produce integrals
- join integrals with muscle length polynomial to obtain constrained polynomial
- differentiate constrained polynomial to obtain constrained moment arm polynomials
- determine whether constrained polynomials are further expandable
- approximate dynamics of device based on constrained polynomials
- reiterate expansion and determination steps
- generate lists of potential candidates for expansion
- select candidates for expanding muscle length and moment arm polynomials
- expand polynomials by selected candidates
- analyze candidates to determine greatest improvement in fitting
- calculate AIC for input dataset
- use AIC in analysis to determine greatest improvement
- define inventive aspects
- introduce AIC calculation
- introduce polynomial equation
- describe muscle model
- introduce error-based term inclusion
- apply Shannon principal
- add polynomial term
- describe prosthetic
- store polynomial equations
- introduce movable part
- store computer software
- execute software
- define polynomial equations
- identify muscle structure
- determine muscle function
- emphasize embodiment variations

