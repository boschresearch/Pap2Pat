# DESCRIPTION

## BACKGROUND

- introduce machine translation
- motivate personalization
- describe multilingual customer modeling
- discuss domain adaptation
- limitations of current machine translation systems
- need for personalized machine translation

## BRIEF DESCRIPTION

- introduce method for predicting optimal machine translation system
- describe system for predicting optimal machine translation system
- outline translation method

## DETAILED DESCRIPTION

- introduce machine translation system for personalizing selection
- describe k-nearest-neighbors approach for user-user collaborative filtering
- explain prediction of user preference without assuming user has expressed preference
- describe system proposing translation system to user
- define user as receiver or author of text to be translated
- illustrate computer-implemented system for identifying machine translation system
- describe components of system: user profile generator, collaborative filtering component, prediction component, translation generator, output component
- explain user profile generator generating user profiles based on user evaluations
- describe collaborative filtering component updating user profile based on other users
- explain prediction component predicting optimal machine translation system
- describe optional translation generator outputting machine translation
- illustrate machine translation system prediction method
- describe providing user profiles
- explain receiving request for prediction of optimal translation system
- describe updating user profile using collaborative filtering
- explain predicting optimal machine translation system
- describe optional translation generation and output
- illustrate alternative method of updating user profile using collective matrix factorization

### Collaborative Filtering

- describe collaborative filtering approach for recommending machine translation system

### Generating User Profiles (S102)

- describe capturing subjective preferences of individual users
- explain user evaluating subset of machine translation systems
- describe creating user-preference vector with pairwise rankings
- explain alternative representation of user preferences matrix

### Updating User Profiles (S106)

- compute similarity between users
- identify set of similar users
- establish criteria for filtering out candidate nearest neighbors
- compute weighted average of predictions of top k most-similar-users
- use similarity score as weighting for respective other user's pairwise ranking
- compute prediction function for a given user and MT system pair
- identify nearest neighbors for each of remaining translation pairs
- compute cosine similarity between user and each of candidate nearest neighbors
- identify k nearest neighbors
- use Eqn. 2 to compute prediction for pair of MT systems
- round prediction to same number of decimal places as rankings
- suggest MT system as preferred system for user

### Predicting a Machine Translation System for the Target User (S1081

- use personalized CTP method or CMF method
- aggregate prediction with other scores, such as score based on content of sentence(s) to be translated
- evaluate prediction of preferences separately across different levels of translation quality
- use various modifications to system and method

### Examples

- compare method with other methods using large set of human pairwise-comparisons
- evaluate data from MT Shared Task in 2013 Workshop on Statistical Machine Translation

### Evaluation Methodology

- perform leave-one-out experiment to predict which of two translation systems would be preferred by a given user

### CTP Parameters

- set CTP parameters, such as similarity function, m, k, and similarity threshold

### Other Prediction Methods

- introduce alternative prediction methods
- describe mathematical formulations of each method

### Results

- present experimental results in accuracy percentage
- discuss statistical significance of results
- analyze limitations and potential improvements of CTP method

