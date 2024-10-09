# DESCRIPTION

## GOVERNMENT FUNDING

- state no government funding

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate indoor localization
- highlight FCC document
- describe limitations of current localization methods
- discuss challenges of indoor environments
- summarize research on wireless sensor networks
- highlight need for new localization methods
- introduce Ordinal UNLOC framework

## SUMMARY

- introduce Ordinal UNLOC framework
- describe use of ordinal data
- summarize rank aggregation step
- describe learning functions to transform dissimilarities
- summarize multidimensional unfolding optimization
- describe method for determining target location
- describe system for determining target location

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce indoor environments
- define sensor field and sensor types
- describe system model and notation
- introduce ordinal comparisons and binary outcomes
- define comparison function and thresholding
- summarize problem of localization from ordinal data
- outline Ordinal Unfolding-based Localization (Ordinal UNLOC) approach
- describe rank aggregation from ordinal data
- formulate least squares problem for spatial proximities
- partition proximity matrix
- outline function learning and distance estimation

### Rank Aggregation from Ordinal Data

- introduce rank aggregation problem
- describe HodgeRank or least squares (LS) ranking method
- formulate linear least squares problem
- solve for spatial proximities
- collect proximities into matrix
- partition proximity matrix
- describe LS ranking method

### Function Learning: Estimating Distances from Spatial Proximities

- introduce function learning problem
- describe basis expansion for function
- truncate series to first order
- solve for coefficients via linear regression
- compute preliminary estimate of anchor-to-target distances
- recalibrate estimated distances
- describe recalibration process

### Unfolding Localization from Distance Measures

- formulate unfolding optimization problem
- compute estimated location of targets

### Simulation Tests

- construct synthetic datasets via numerical simulations
- describe simulation test 1: typical localization outcome
- generate ordinal distance comparison data under noisy threshold model
- estimate target locations using Ordinal UNLOC
- describe simulation test 2: dependence of localization error on number of anchors
- vary number of anchors and perform independent numerical localization experiments
- compute localization error as distance between true and estimated target locations
- plot root mean squared error (RMSE) of localization as function of number of anchors
- describe simulation test 3: dependence of localization error on level of noise
- draw noise values independently from normal distribution
- plot RMSE of localization as function of noise standard deviation
- repeat simulation test 3 with double number of anchors
- discuss results of simulation tests
- introduce embodiments of the present disclosure
- describe scope of embodiments
- discuss equivalents to specific embodiments
- introduce Ordinal UNLOC implementation
- describe hardware and software implementation options
- list incorporated references
- introduce reference 1: Federal Communications Commission
- introduce reference 2: E9-1-1 location accuracy test bed report
- introduce reference 3: Consumer Reports Magazine
- introduce reference 4: Indoor location article
- introduce reference 5: Resolution reconfigurable systems
- introduce reference 6: Indoor positioning system based on WiFi router and FM beacons
- introduce reference 7: Indoor localization without pain
- introduce reference 8: Location fingerprinting with Bluetooth low energy beacons
- introduce reference 9: Indoor location position based on Bluetooth signal strength
- introduce remaining references

