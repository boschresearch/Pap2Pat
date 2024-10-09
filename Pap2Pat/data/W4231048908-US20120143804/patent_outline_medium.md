# DESCRIPTION

## FIELD AND BACKGROUND OF THE INVENTION

- introduce electronic nose concept
- limitations of current eNose technology

## SUMMARY OF THE INVENTION

- motivate odor pleasantness prediction
- introduce perceptual axes approach
- describe method of assessing odors
- outline apparatus for assessing odors
- define axis of odor pleasantness
- provide embodiment details

## DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce tuning eNose to human odor pleasantness estimates
- predict pleasantness of novel odorants and odorant mixtures
- test predictions in naïve subjects
- suggest systematic predictable link between stimulus structure and stimulus pleasantness
- focus on perceptual axes
- define axis with part hardwired as unpleasant
- relate unpleasantness to specific molecules and compactness
- compute compactness using principal component analysis (PCA)
- characterize odor axis by examining single descriptors
- associate descriptors with atomic properties
- explain molecular surface area and VDW interactions
- describe apparatus and method
- illustrate method of assessing odors using electronic nose
- map odor information onto axis of odor preference
- provide output including assessment of odor pleasantness
- consider intensity in assessment
- obtain pre-learned axis of odor pleasantness
- train neural network to predict median pleasantness
- show results for prediction of odor pleasantness
- discuss power analysis and prediction rate
- test performance with novel odorants
- show correlation between machine prediction ratings and human ratings
- discuss binary cases of very pleasant against very unpleasant odors
- conclude that apparatus discriminates good odors from bad odors

### Materials and Methods

- describe eNose measurements
- introduce MOX and QMB sensors
- detail sample preparation
- outline eNose signal feature extraction methods
- extract parameters from sensor signals
- calculate ratios of sensor signals
- cluster eNose measurements into odorant classes
- remove signals that fail to cluster
- normalize feature values and odorant signatures
- introduce human subjects
- describe odor rating procedure
- rate pleasantness and intensity of odors
- calculate human to human ratings correlation
- verify results using category rating experiment
- model pleasantness prediction using neural network
- classify odors as pleasant or unpleasant
- conduct additional experiments
- correlate eNose predictions with human ratings
- validate results across cultures
- analyze algorithm power and outlier removal

