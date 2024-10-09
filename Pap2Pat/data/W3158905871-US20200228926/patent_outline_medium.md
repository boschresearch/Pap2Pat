# DESCRIPTION

## GOVERNMENT FUNDING

- state no government funding

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND

- motivate indoor localization
- highlight limitations of current methods
- emphasize need for accurate indoor localization

## SUMMARY

- introduce Ordinal UNLOC framework
- describe advantages of Ordinal UNLOC
- outline steps of Ordinal UNLOC method

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce indoor environments and sensor fields
- define system model and notation
- describe ordinal comparison data and its representation
- formulate problem of localization from ordinal data
- outline Ordinal Unfolding-based Localization (Ordinal UNLOC) approach

### Rank Aggregation from Ordinal Data

- introduce rank aggregation method for inferring spatial proximities
- describe HodgeRank or least squares (LS) ranking method
- formulate linear least squares problem to obtain spatial proximities

### Function Learning: Estimating Distances from Spatial Proximities

- introduce function learning to estimate anchor-to-target distances
- describe basis expansion and linear function representation
- formulate linear regression problem to determine function coefficients

### Unfolding Localization from Distance Measures

- formulate unfolding optimization to infer target locations from estimated distances

### Simulation Tests

- describe simulation test setup
- demonstrate typical localization outcome
- generate ordinal distance comparison data
- estimate target locations using Ordinal UNLOC
- vary number of anchors to test localization accuracy
- perform 5000 independent numerical localization experiments
- compute localization error as RMSE
- plot RMSE as a function of number of anchors
- test dependence of localization error on noise level
- vary noise level to test impact on localization
- plot RMSE as a function of noise level
- compare results with double number of anchors
- discuss results and implications
- conclude on effectiveness of Ordinal UNLOC

