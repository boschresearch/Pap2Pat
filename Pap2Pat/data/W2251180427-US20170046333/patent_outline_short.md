# DESCRIPTION

## BACKGROUND

- motivate personalized customer applications
- describe limitations of machine translation systems
- introduce need for personalized machine translation

## BRIEF DESCRIPTION

- outline method for predicting optimal machine translation system

## DETAILED DESCRIPTION

- introduce machine translation system for personalizing selection
- describe k-nearest-neighbors approach for user-user collaborative filtering
- outline system components, including user profile generator and prediction component
- describe user profile generator and user evaluations of translations
- outline collaborative filtering component and its sub-components
- describe prediction component and its output
- outline optional translation generator and output component
- describe computer system and its components, including memory and processor
- outline software and its various forms

### Collaborative Filtering

- describe collaborative filtering approach for recommending machine translation systems

### Generating User Profiles (S102)

- describe capturing subjective preferences of individual users
- outline generating user profiles, including user evaluations and ranking of translations

### Updating User Profiles (S106)

- compute similarity between users
- identify set of similar users
- update translational preferences for user
- compute weighted average of predictions
- identify nearest neighbors
- predict translational preferences for target user

### Predicting a Machine Translation System for the Target User (S1081

- generate factor matrices
- construct updated user preferences matrix

### Examples

- evaluate method using human pairwise-comparisons between automatic translations

### Evaluation Methodology

- compare prediction functions with user's pairwise system preference

### CTP Parameters

- set CTP parameters

### Other Prediction Methods

- describe alternative prediction methods

### Results

- present experimental results and compare CTP with other methods

