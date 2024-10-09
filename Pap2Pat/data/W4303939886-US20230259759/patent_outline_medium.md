# DESCRIPTION

## FIELD

- relate to machine-learning

## BACKGROUND

- introduce sequence-to-sequence models

## SUMMARY

- motivate improved translation quality
- outline computer-implemented method
- outline computing system

## DETAILED DESCRIPTION

- introduce sequence-to-sequence modeling with neural quality metrics
- motivate neural sequence-to-sequence models for machine translation
- describe limitations of existing approaches using beam search
- explain problem of less-frequently used words scoring lower
- introduce example aspects of the present disclosure
- describe utilizing neural utility metrics for evaluating utility of candidate translations
- compare neural utility metrics to existing metrics
- introduce computer-implemented method for translating a source sequence
- obtain a plurality of candidate outputs based on a source sequence
- describe machine-learned translation model for estimating probability of a target segment
- determine a plurality of reference utilities for each candidate output
- introduce neural utility metric model for determining utility of a candidate translation
- describe examples of neural utility metric models (BLEURT, COMET)
- explain how neural utility metric models can include first and second generation models
- describe how BLEURT metric can be used as a reference metric
- determine an average utility of each candidate output
- determine an output sequence based on the average utility of each candidate output
- describe technical effects and benefits of the present disclosure
- introduce example embodiments of the present disclosure
- describe user computing device and its components
- describe server computing system and its components
- describe training computing system and its components
- define model trainer
- describe network
- introduce machine-learned models
- process text data
- process speech data
- process latent encoding data
- process statistical data
- process sensor data
- perform encoding task
- illustrate computing system
- describe user computing device
- depict block diagram of computing device
- illustrate applications
- describe central intelligence layer
- illustrate sequence-to-sequence model
- receive source segment
- estimate probability of target segments
- determine utilities of candidate translations
- produce average utility
- select output segment
- illustrate method for translating source sequence
- determine output sequence

