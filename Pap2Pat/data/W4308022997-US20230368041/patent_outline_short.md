# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- introduce reinforcement learning methods

### 2. Description of Prior Art and Related Information

- limitations of existing experience replay methods

## SUMMARY OF THE INVENTION

- motivate event tables and stratified sampling
- describe theoretical underpinning
- summarize empirical results
- outline contributions of the invention

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS AND BEST MODE OF INVENTION

- define terminology and conventions
- describe computer and software definitions
- outline process steps and algorithms
- explain computer-readable medium and transmission
- discuss commercial implementation considerations

### Terminology

- define reinforcement learning agent and Markov Decision Process
- explain value function and Q-learning update
- describe experience replay and event specification
- outline Stratified Sampling from Event Tables (SSET) algorithm

### MiniGrid Experiments

- introduce SSET in MiniGrid domain
- compare SSET with uniform ER and reverse-sweep
- compare SSET with reward shaping
- evaluate SSET with badly designed event conditions
- analyze SSET performance with varying default buffer sampling probability
- test SSET in obstacle course and randomized skill environments
- demonstrate SSET's robustness against catastrophic forgetting

### Lunar Lander and Mujoco Experiments

- evaluate SSET in Lunar Lander and Mujoco domains

### Simulated Car Racing Experiments

- demonstrate SSET's sample complexity benefits in "slingshot passing" scenario
- evaluate SSET's robustness to event choices
- show SSET's ability to remember to stay on course in time-trial setting

### Recommendations on How to Pick Helpful Events

- provide guidelines for specifying domain knowledge

### Summary

- summarize SSET algorithm and benefits

### Definitions, Lemmas, Propositions Used Above

- define event conditions and event tables
- derive convergence rate and bias correction procedure
- provide assumptions and overview of base algorithm
- prove sufficient conditions for improvement of convergence speed
- define mathematical notation and lemmas
- prove lemma 1 and proposition 3
- analyze bias introduced by weighted sampling
- state and prove theorem 1
- provide patent claim language and scope

