# DESCRIPTION

## BACKGROUND

- introduce drug development process

## SUMMARY

- outline method for predicting effects of compounds on targets
- describe features of implementations
- outline alternative method for predicting effects
- describe various forms of implementation

## DETAILED DESCRIPTION

- define targets and compounds
- introduce network environment 100
- describe data repository 105 and server 110
- explain data engine 111 and experimental space 118
- describe executed and unexecuted experiments
- explain observations and annotations
- introduce experimental results 104
- describe initializing experimental space 118
- generate model to represent available data
- select additional experiments to increase model accuracy
- execute additional experiments and update experimental space 118
- continue until desired level of accuracy or budget exhaustion
- generate active learning model
- generate models independent of target and compound features
- generate clusters of compounds and targets
- generate predictive model using clusters
- generate models dependent on target and compound features
- calculate features of targets and compounds
- select experiments for execution using various techniques

### Detection of Hits

- define hit
- associate compounds and targets with feature vectors
- generate predictions of effects of compounds on targets
- correlate predictions with feature vectors
- compare correlated predictions and features to pre-defined events
- detect hit based on comparison
- select experiments independent of dynamic generation of a model
- retrieve information indicative of criteria for batches of experiments
- group compounds based on features
- select experiments based on sampling technique
- use statistical hypothesis testing guarantees
- determine distribution of probabilities of an experiment producing an effect
- select experiments from distribution to promote balanced distribution
- describe detection of hits
- select unexecuted experiments
- execute selected experiments
- update experimental space
- detect cease condition
- repeat active learning technique
- cease active learning technique
- implement batch selection
- generate predictions of effects
- generate model for predictions
- implement techniques for generating model
- describe computer device
- describe components of computer device
- describe mobile computer device
- describe components of mobile computer device
- describe implementation of systems and techniques
- describe variations of systems and techniques

