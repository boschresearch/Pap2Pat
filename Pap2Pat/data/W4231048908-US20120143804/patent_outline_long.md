# DESCRIPTION

## FIELD AND BACKGROUND OF THE INVENTION

- introduce electronic nose concept
- describe limitations of current eNoses
- motivate odor quality reporting
- summarize Burl et al.'s work
- highlight need for novel approach

## SUMMARY OF THE INVENTION

- introduce ideal artificial nose concept
- contrast with current eNose limitations
- focus on perceptual axes
- motivate odor pleasantness axis
- describe method of assessing odors
- extract odor information using eNose
- plot odor information to pleasantness axis
- output assessment based on pleasantness axis
- describe apparatus for assessing odors
- configure eNose to output structure identifying odor
- map structure to pleasantness axis using neural network
- output assessment based on pleasantness axis
- provide definitions and clarifications

## DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce tuning eNose to human odor pleasantness estimates
- predict pleasantness of novel odorants and odorant mixtures
- test predictions in naïve subjects
- suggest systematic predictable link between stimulus structure and stimulus pleasantness
- focus on perceptual axes
- define primary perceptual axis of human olfaction as odorant pleasantness
- relate odorant pleasantness to physicochemical structure of odorant molecules
- define axis with part hardwired as unpleasant
- relate unpleasantness to specific molecules and compactness
- compute compactness using principal component analysis (PCA)
- use compactness to tune odor measuring devices and odor generating devices
- characterize odor axis by examining single descriptors
- associate descriptors with atomic VDW volumes, polarizabilities, connectivity indices, and molecular branching
- relate molecular surface area to molecule's ability to form induced dipole
- describe sparse molecules as pleasant and tightly packed molecules as unpleasant
- introduce apparatus and method according to the present invention
- explain non-limiting nature of invention
- reference FIG. 1, illustrating method of assessing odors
- sample odor using electronic nose
- process output signals to find features characterizing odor
- map odor information onto axis of odor preference
- provide output including assessment of odor pleasantness
- consider intensity level in assessment
- obtain pre-learned axis of odor pleasantness
- correlate scores and fingerprints to form odor pleasantness axis
- use neural network to order odors according to scores
- obtain odor information from electronic nose using features of odor sensors
- use neural network to assess pleasantness of novel odor
- reference FIG. 2, illustrating apparatus for assessing odors
- describe electronic nose and mapping unit
- plot extracted structure to location on pre-learned axis of odor pleasantness
- use neural network to map signatures of odors to locations on axis
- provide output assessment of applied odor
- discuss implications for biology and biotechnology
- describe experiment measuring 76 odorants with Moses II eNose
- extract features from eNose signals
- normalize columns and rows of matrix
- ask subjects to rate pleasantness of each odorant stimuli
- remove odorants with variance of more than two standard deviations
- train neural network algorithm to predict median pleasantness
- reference FIG. 3, showing results for prediction of odor pleasantness
- discuss correlation values when using different numbers of odorants as test groups
- reference FIGS. 6A to 6D, showing similar experiment
- discuss classification success rate as a function of odors removed from test set
- show power analysis
- test performance with novel odorants
- reference FIG. 4, showing predicting pleasantness for novel odors
- discuss binary cases of very pleasant against very unpleasant odors
- conclude that apparatus discriminated good odors from bad odors

### Materials and Methods

- describe eNose measurements
- introduce MOX and QMB sensors
- detail sample preparation
- explain headspace sampler parameters
- describe blank vial and system cleaning procedures
- outline measurement protocol
- specify signal extraction methods
- introduce feature extraction methods
- describe signal max value and latency extraction
- extract time-dependent signal features
- calculate signal ratios
- cluster eNose measurements
- evaluate feature extraction method
- remove signals that fail to cluster
- normalize feature values and odorant signatures
- introduce human subjects
- describe subject demographics
- outline odor rating protocol
- detail visual analogue scale usage
- calculate pleasantness ratings
- evaluate between and within odor rating correlations
- describe category rating experiment
- compare VAS and category rating correlations
- calculate human to human correlation
- calculate human to group average correlation
- describe neural network modeling
- specify neural network architecture
- detail training function and parameters
- calculate prediction values
- describe classification algorithm
- classify odors as pleasant or unpleasant
- introduce additional experiments
- describe cross-cultural validation
- compare eNose and human pleasantness ratings
- evaluate cultural dependence of apparatus
- describe difficulties in conveying rating scale
- compare native Israeli and Ethiopian ratings
- evaluate correlation between machine and human ratings
- describe eNose algorithm power analysis
- discuss implications of results

