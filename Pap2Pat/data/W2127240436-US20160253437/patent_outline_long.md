# DESCRIPTION

## FIELD OF THE INVENTION

- define field of cyber-physical systems

## BACKGROUND OF THE INVENTION

- motivate formal verification
- describe limitations of formal verification
- discuss importance of validation
- highlight challenges of validation

## SUMMARY OF THE INVENTION

- introduce ModelPlex method
- describe runtime model validation
- define runtime validation
- explain safety implications
- describe monitor synthesis
- discuss safety margins
- explain feedback control constraints
- summarize ModelPlex benefits

## DETAILED DESCRIPTION OF THE INVENTION

### Preliminaries: Differential Dynamic Logic

- introduce differential dynamic logic
- define syntax and semantics of hybrid programs

### ModelPlex Approach for Verified Runtime Validation

- motivate CPS verification
- introduce ModelPlex approach
- define formula (1) for CPS verification
- derive monitors from proofs
- introduce model monitor, controller monitor, and prediction monitor
- define prediction monitor 24
- assume bounded deviation plant model αδplant
- separate disturbance causes in models
- assume monitor evaluations are at most s time units apart

### Relation Between States

- define state recall
- introduce lemma 1 for loop prior and posterior state
- construct formula (2) for state transition relation
- simplify formula (2) using theorem proving
- evaluate resulting first-order real arithmetic formula
- remark on complexity of evaluating arithmetic formulas
- use interval arithmetic for reliable results

### Example 1

- illustrate concepts with a simple water tank example

### ModelPlex Monitor Synthesis

- introduce ModelPlex monitor specifications
- generate monitor specifications from hybrid system models
- define model monitor Xm
- prove theorem 1 for model monitor correctness
- outline approach to generate monitor specifications
- describe process of generating monitor conditions

### Example 2

- construct specification conjecture for water tank model
- analyze conjecture using theorem proving
- reveal monitor specification 104
- describe process of generating monitor conditions
- illustrate proof rules for nondeterministic assignment
- illustrate optimization 1 for instantiation trigger

### Example 3

- illustrate proof steps for water tank example
- handle differential equations
- introduce options for instantiating existential quantifier
- use quantifier elimination for equivalent quantifier-free result

### Example 4

- solve differential equations
- instantiate existential quantifier
- apply quantifier elimination

### Example 5

- introduce new logical variable
- re-introduce existential quantifier
- substitute logical variable
- derive controller monitor
- check controller monitor correctness
- assume canonical form
- prove invariant
- check post-controller state
- apply theorem 2
- discuss monitoring in presence of uncertainty
- model sensor uncertainty
- model actuator disturbance
- incorporate clock drift
- express expected deviation
- use differential inequalities
- analyze example 6
- apply proof rules
- turn differential inequalities into differential-algebraic constraints
- proceed with proof
- discuss finding model monitors
- use techniques for differential equations
- handle differential inequalities without polynomial solutions

## A. Proofs

### A.1 Formal Semantics of

- define transition semantics of hybrid programs
- define interpretation of dL formulas
- specify transition relation ρ
- define semantics of HP α
- define validity of dL formulas

### A.2 Soundness

- recall Lemma 1
- prove Theorem 1 (Model monitor correctness)
- prove Theorem 2 (Controller monitor correctness)
- prove Theorem 3 (Prediction monitor correctness)
- state assumptions for Theorem 1
- state assumptions for Theorem 2
- state assumptions for Theorem 3

### A.3 Decidability and Computability

- state decidability and computability problem
- split Theorem 4 into Theorem 5 and Theorem 6
- prove Theorem 5 (Monitor correctness is decidable)
- prove decidability of Xm, Xc, and Xp monitors
- prove Theorem 6 (Monitor synthesis is computable)
- give constructive proof of Theorem 6
- handle differential equations in αplant
- handle disturbance functions f(θ,δ) and g(θ,δ)
- use differential cut rule and differential invariant rule
- use differential weakening rule
- use quantifier elimination rule
- conclude decidability and computability

## B. Water Tank Monitor Specification Conjecture Analysis

- show proof rules applied to water tank specification conjecture
- define proof rules for hybrid programs
- define proof rules for differential equations
- analyze water tank monitor specification conjecture
- give example of monitor specification

### Example 7

- analyze water tank monitor specification conjecture using differential-algebraic constraints

## C. Monitor Synthesis and Fallback Controller Design

### C.1 Design-By-Contract Monitoring

- motivate monitors for CPS design
- describe monitor types and usage

### C.2 Monitor Synthesis

- describe monitor synthesis approach

### C.3 Designing for a Fail-Safe Fallback Controller

- motivate fail-safe fallback controller
- describe design requirements and properties

### D. Monitor Synthesis Algorithm

- outline monitor synthesis algorithm

### E. Simulation

- introduce simulation setup
- describe monitor Xm and Xc
- present simulation results
- discuss benefits of approach

