# DESCRIPTION

## FIELD OF THE INVENTION

- define field of cyber-physical systems

## BACKGROUND OF THE INVENTION

- motivate formal verification and validation

## SUMMARY OF THE INVENTION

- introduce ModelPlex method
- describe runtime model validation

## DETAILED DESCRIPTION OF THE INVENTION

### Preliminaries: Differential Dynamic Logic

- introduce differential dynamic logic

### ModelPlex Approach for Verified Runtime Validation

- motivate model-based verification
- introduce ModelPlex approach

### Relation Between States

- define state recall and lemma for loop prior and posterior state

### Example 1

- illustrate water tank example

### ModelPlex Monitor Synthesis

- introduce ModelPlex monitor synthesis

### Example 2

- illustrate water tank monitor synthesis

### Example 3

- illustrate proof steps for water tank monitor synthesis

### Example 4

- apply quantifier elimination

### Example 5

- re-introduce existential quantifier
- substitute logical variable
- derive controller monitor
- prove controller monitor correctness
- discuss controller switching

## A. Proofs

### A.1 Formal Semantics of

- define transition semantics of hybrid programs

### A.2 Soundness

- prove soundness of model, controller, and prediction monitors

### A.3 Decidability and Computability

- prove decidability of monitor correctness
- prove computability of monitor synthesis
- provide constructive proof of monitor synthesis

## B. Water Tank Monitor Specification Conjecture Analysis

- analyze water tank monitor specification conjecture

### Example 7

- handle differential inequalities in water tank monitor specification

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

- illustrate fallback controller behavior

