# DESCRIPTION

## FIELD OF THE INVENTION

- define field of cyber-physical systems

## BACKGROUND OF THE INVENTION

- motivate formal verification
- discuss limitations of models

## SUMMARY OF THE INVENTION

- introduce ModelPlex method
- describe runtime model validation
- explain monitor synthesis
- outline fail-safe actions

## DETAILED DESCRIPTION OF THE INVENTION

### Preliminaries: Differential Dynamic Logic

- introduce differential dynamic logic

### ModelPlex Approach for Verified Runtime Validation

- motivate CPS verification
- introduce ModelPlex concept
- derive three kinds of monitors
- explain monitor functionality

### Relation Between States

- define state recall
- prove lemma on loop prior and posterior state
- construct formula for compliance check

### Example 1

- illustrate water tank example

### ModelPlex Monitor Synthesis

- introduce ModelPlex monitor specifications
- generate monitor specifications from hybrid system models
- turn specifications into monitor code

### Example 2

- construct specification conjecture for water tank model
- analyze conjecture using theorem proving
- reveal actual monitor specification

### Example 3

- handle nondeterministic assignment
- handle differential equations

### Example 4

- apply quantifier elimination

### Example 5

- introduce new logical variable
- re-introduce existential quantifier
- substitute logical variable
- derive controller monitor
- prove controller monitor correctness
- define controller monitor
- discuss monitoring in presence of uncertainty
- model sensor uncertainty and actuator disturbance
- incorporate clock drift and actuator disturbance
- analyze model with differential inequalities
- use proof rules to turn differential inequalities into differential-algebraic constraints

## A. Proofs

### A.1 Formal Semantics of

- define transition semantics of hybrid programs
- define interpretation of dL formulas

### A.2 Soundness

- recall lemma 1 (loop prior and posterior state)
- recall theorem 1 (model monitor correctness)
- recall theorem 2 (controller monitor correctness) and theorem 3 (prediction monitor correctness)

### A.3 Decidability and Computability

- state decidability and computability problem
- split theorem 4 into theorem 5 (decidability) and theorem 6 (computability)
- prove theorem 5 (decidability)
- prove theorem 6 (computability) using decidability
- give constructive proof of theorem 6
- conclude decidability and computability of Xm, Xc, and Xp monitors

## B. Water Tank Monitor Specification Conjecture Analysis

- show proof 1 (analysis of water tank monitor specification conjecture)
- illustrate example 7 (handling differential inequalities)

### Example 7

- illustrate handling of differential inequalities

## C. Monitor Synthesis and Fallback Controller Design

### C.1 Design-By-Contract Monitoring

- motivate monitors for CPS design

### C.2 Monitor Synthesis

- synthesize monitor implementation

### C.3 Designing for a Fail-Safe Fallback Controller

- design fail-safe fallback controller

### D. Monitor Synthesis Algorithm

- outline monitor synthesis algorithm

### E. Simulation

- illustrate monitor behavior
- demonstrate simulation results

