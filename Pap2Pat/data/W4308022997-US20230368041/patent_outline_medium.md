# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- relate to reinforcement learning methods

### 2. Description of Prior Art and Related Information

- describe limitations of existing ER methods

## SUMMARY OF THE INVENTION

- introduce event tables and SSET
- motivate SSET for off-policy RL
- describe theoretical underpinning for SSET
- summarize empirical results
- describe combination with PER and reward shaping
- describe application to multiple skills and catastrophic forgetting
- compare with classical RL and deep RL
- describe generalization to multi-table partitioning schemes

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS AND BEST MODE OF INVENTION

- define terminology
- introduce computer and computing device
- describe software and application
- explain computer-readable medium
- discuss various forms of computer-readable media
- describe apparatuses for performing operations
- explain processing, computing, calculating, and determining
- discuss commercial implementation considerations
- introduce Stratified Sampling from Event Tables (SSET)
- provide overview of SSET advantages and empirical results

### Terminology

- define reinforcement learning agent
- introduce episodic Markov Decision Process
- define value function of a policy
- explain model-free off-policy methods
- introduce Q-learning's gradient-style update
- define experience replay
- explain event specification
- discuss event conditions and histories

### MiniGrid Experiments

- introduce SSET in MiniGrid domain
- define event conditions for SSET
- compare SSET with uniform ER and reverse-sweep
- compare SSET with TD-error prioritized experience replay
- evaluate SSET with different event conditions
- analyze SSET performance with bad event conditions
- study SSET performance with varying default buffer sampling probability
- apply SSET to obstacle course environment
- compare SSET with uniform ER and PER in obstacle course
- evaluate SSET in randomized multi-skill setup
- demonstrate SSET avoids catastrophic forgetting
- analyze effect of intermediate events and histories on SSET
- compare SSET with different sampling weights
- apply Conflict-Averse Gradient Descent to SSET
- evaluate CAGrad with SSET in randomized multi-skill setup

### Lunar Lander and Mujoco Experiments

- apply SSET to Lunar Lander and Mujoco domains
- compare SSET with uniform ER and PER in Lunar Lander and Mujoco

### Simulated Car Racing Experiments

- apply SSET to Gran Turismo Sport racing simulator
- evaluate SSET in "slingshot passing" scenario
- analyze effect of slipstream event threshold on SSET
- evaluate SSET in cases with frequent or hard-to-find events
- apply SSET to time-trial scenario on Lago Maggiore GP track
- evaluate SSET in maintaining multiple skills in time-trial setting
- illustrate event tables from storage and sampling perspectives

### Recommendations on How to Pick Helpful Events

- provide guidelines for specifying domain knowledge
- discuss limitations of learning helpful events online

### Summary

- summarize SSET algorithm and its benefits

### Definitions, Lemmas, Propositions Used Above

- introduce Q-learning with target function
- derive finite-time convergence results
- define state probability distribution
- define event conditions
- define event sections
- quantify over-sampling of experience
- derive convergence rate
- correct bias
- show improvement over uniform sampling
- define mathematical notation
- state lemma 1 and its proof
- state proposition 3 and its proof
- discuss bias introduced by weighted sampling
- state lemma 2 and its proof
- state theorem 1 and its proof
- discuss scope of invention
- discuss claim elements and steps
- discuss alterations and modifications
- discuss definition of words and elements
- discuss scope of claims

