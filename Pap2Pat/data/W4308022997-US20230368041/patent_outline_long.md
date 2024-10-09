# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Field of the Invention

- relate to reinforcement learning methods

### 2. Description of Prior Art and Related Information

- describe limitations of experience replay
- motivate prioritized experience replay
- highlight need for improved methods

## SUMMARY OF THE INVENTION

- introduce event tables and SSET
- describe SSET algorithm
- motivate fast-lane intuition
- provide theoretical underpinning
- describe empirical results
- compare to uniform sampling and PER
- describe combination with PER
- describe combination with reward shaping
- mitigate catastrophic forgetting
- introduce event tables and SSET framework
- derive theoretical guarantees
- demonstrate empirical advantages
- compare to classical RL and deep RL
- compare to Topological Experience Replay
- generalize multi-table partitioning schemes
- connect to initial state selection and reward shaping

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS AND BEST MODE OF INVENTION

- define terminology
- introduce computer and computing device
- define software and application
- describe computer program instructions
- discuss process steps and method steps
- introduce processor and computer-readable medium
- describe commercial implementation considerations
- introduce Stratified Sampling from Event Tables (SSET)
- describe experience replay (ER) buffer
- discuss uniform sampling limitations
- introduce theoretical advantage of SSET
- describe empirical results in MiniGrid domains
- describe empirical results in benchmark RL environments
- describe empirical results in high-fidelity car racing simulator
- provide references to algorithms, propositions, definitions, and lemmas
- define reinforcement learning agent and episodic Markov Decision Process
- describe value function and Q-learning update
- introduce event specification and event condition
- discuss importance of event conditions and histories
- describe Stratified Sampling from Event Tables (SSET) algorithm
- introduce theorem and proof sketch for SSET sample complexity

### Terminology

- define reinforcement learning agent
- define episodic Markov Decision Process
- describe value function
- describe Q-learning update
- introduce event specification
- define event condition
- discuss importance of event conditions
- discuss importance of histories
- describe terminal goal states
- describe high reward states
- describe bottleneck states
- describe important rare states
- discuss negatively rewarding states
- describe experience replay (ER) buffer
- describe deep reinforcement learning
- describe model-free off-policy methods

### MiniGrid Experiments

- introduce SSET in MiniGrid domain
- define dense neural net architecture
- describe E-greedy behavior policy
- compare SSET with Uniform ER and Reverse-sweep*
- show sample complexity speedup of SSET
- illustrate learning stability of SSET
- compare SSET with PER
- show SSET outperforms PER in terms of variance
- combine SSET with TD-error prioritization
- show best of both worlds with combined approach
- compare SSET with shaping rewards
- show SSET outperforms shaping rewards
- combine SSET with shaping rewards
- show even better performance with combined approach
- evaluate SSET with badly designed event conditions
- compare good and bad event conditions
- show performance varies with default buffer's sampling probability
- introduce obstacle course environment
- describe agent's observation and action space
- use event conditions with history length
- compare SSET with reverse-sweep and uniform ER
- show improved efficiency and stability of SSET
- compare SSET with TD-error prioritization
- show SSET performs equally well with or without PER
- introduce randomized multi-skill setup
- show SSET acquires and maintains all skills
- illustrate catastrophic forgetting in obstacle course
- show SSET avoids catastrophic forgetting
- compare SSET with different sampling weights
- show similar performance with different weights
- introduce Conflict-Averse Gradient Descent with SSET

### Lunar Lander and Mujoco Experiments

- introduce LunarLanderContinuous-v3 and MuJoCo suite
- describe event conditions and history lengths
- compare SSET with uniform experience replay and PER
- show SSET improves sample efficiency and stability
- illustrate SSET is robust to non-optimal history lengths

### Simulated Car Racing Experiments

- introduce Gran Turismo Sport racing simulator
- describe environment, features, and training details
- introduce "slingshot" passing scenario
- define two events: slipstream and won
- compare SSET with uniform sampling
- show SSET learns to win consistently
- illustrate SSET's robustness to event threshold
- show SSET's performance with less informative events
- illustrate SSET's variance with hard-to-find events
- introduce time-trial setting on Lago Maggiore GP track
- describe re-establish event and history length
- compare SSET with uniform sampling
- show SSET mitigates catastrophic forgetting
- illustrate consistent on-course laps with SSET

### Recommendations on How to Pick Helpful Events

- provide guidelines for specifying domain knowledge
- discuss limitations of poorly chosen events
- describe event table implementation
- motivate learning helpful events online

### Summary

- summarize SSET algorithm and benefits

### Definitions, Lemmas, Propositions Used Above

- introduce event tables and SSET
- prove sufficient conditions for improvement of convergence speed
- define state probability distribution
- define event conditions
- define event sections
- define event tables
- provide overview of base algorithm and existing results
- state assumptions
- define Bellman operator
- define Q-learning loss function
- define constants CB and LB
- derive convergence rate
- quantify over-sampling of experience in event tables
- derive bias correction procedure
- show improvement over uniform sampling
- define trajectory
- define state density
- define state density disparity from optimal
- define mathematical notation
- state lemma 1
- prove lemma 1
- state proposition 3
- prove proposition 3
- discuss bias in event-table sampling
- state lemma 2
- prove lemma 2
- state theorem 1
- prove theorem 1
- discuss application of theorem 1
- provide disclaimer on alternative features
- discuss claim elements and steps
- provide disclaimer on alterations and modifications
- discuss definition of words and elements
- provide disclaimer on equivalent substitutions
- discuss insubstantial changes to claimed subject matter
- provide disclaimer on obvious substitutions
- discuss scope of claims
- provide disclaimer on conceptual equivalence
- discuss incorporation of essential idea
- conclude scope of invention

