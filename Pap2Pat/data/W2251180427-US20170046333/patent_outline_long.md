# DESCRIPTION

## BACKGROUND

- introduce machine translation
- motivate personalization
- describe customer modeling
- discuss multilingual aspects
- introduce machine translation systems
- motivate domain adaptation
- describe data selection
- describe mixture models
- describe table fill-up
- discuss limitations of domain adaptation
- introduce user's personal translation preferences
- discuss user's glossaries and corpora
- motivate personalized machine translation

## BRIEF DESCRIPTION

- introduce method for predicting optimal machine translation system
- describe user profile
- update user profile
- predict optimal translation system
- describe system for predicting optimal machine translation system
- describe translation method

## DETAILED DESCRIPTION

- introduce machine translation system
- describe collaborative translational preferences method
- explain user preference prediction
- describe system components
- introduce user profile generator
- describe user evaluations of translations
- explain machine translation systems
- describe system types
- explain model training
- describe decoder
- introduce collaborative filtering component
- explain similarity computation
- describe nearest neighbor identification
- explain profile update
- introduce prediction component
- describe optimal translation system prediction
- introduce translation generator
- describe machine translation output
- introduce output component
- describe information output
- explain computer system components
- describe memory
- explain processor
- describe network interface
- explain digital processor device
- describe software
- illustrate machine translation system prediction method
- describe user profile provision
- explain request receipt
- describe user profile update
- explain optimal translation system prediction
- describe machine translation performance
- explain output
- describe rating request
- explain method repetition
- describe computer program product

### Collaborative Filtering

- introduce collaborative filtering
- describe k-nearest-neighbors CF
- describe collective matrix factorization method

### Generating User Profiles (S102)

- explain user preference capture
- describe machine translation system evaluation
- explain user ranking
- describe user preference vector creation
- explain equation for user preference calculation
- describe alternative equation
- explain user vector representation
- describe user preferences matrix

### Updating User Profiles (S106)

- compute similarity between users
- define cosine similarity function
- compute similarity scores
- identify set of similar users
- establish filtering criteria
- filter out candidate nearest neighbors
- compute weighted average of predictions
- define prediction function
- compute sign of weighted average
- normalize scores
- retain denominator for normalization
- compute similarity for each pair of users
- identify k nearest neighbors
- use cosine similarity as similarity measure
- compute similarity for user G and A
- compute similarity for user G and B
- compute similarity for user G and C
- compute similarity for user G and D
- compute similarity for user G and E
- identify k nearest neighbors for each translation pair
- compute prediction for each translation pair
- rank MT systems based on predictions
- suggest preferred MT system
- handle case with not enough information

### Predicting a Machine Translation System for the Target User (S1081

- use personalized CTP method
- combine with other methods
- aggregate scores
- evaluate prediction separately across translation quality
- use automated translation scoring system
- estimate post-editing effort
- obtain rankings implicitly
- use explicit feedback
- collect end-user feedback

### Examples

- compare method with other approaches
- use large set of human pairwise-comparisons
- evaluate method on WMT data
- show effectiveness of personalized method

### Evaluation Methodology

- perform leave-one-out experiment

### CTP Parameters

- define CTP parameters

### Other Prediction Methods

- introduce baseline method ALI
- describe rank-based method RANK
- explain expected wins method EXPT
- outline average user preference method AVPF
- contrast methods with CTP

### Results

- present experimental results in accuracy percentage
- show micro-averaged results in FIG. 8
- report statistical significance of CTP over other methods
- discuss global parameter settings
- suggest tuning parameters for improvement
- analyze weakness in predicting ties
- conclude on providing better translations with user feedback

