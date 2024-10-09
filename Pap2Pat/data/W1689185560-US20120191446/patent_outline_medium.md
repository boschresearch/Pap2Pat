# DESCRIPTION

## THE NAMES OF PARTIES TO A JOINT RESEARCH AGREEMENT

- state no joint research agreement

## FIELD OF THE DISCLOSURE

- introduce parsing problem
- motivate formally-verified parsers

## BACKGROUND OF THE DISCLOSURE

- describe parsing process
- limitations of prior art techniques

## SUMMARY

- introduce system for creating parser
- describe grammar input module
- describe formalism module
- describe proof assistant module

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

### 1. Generals Principles of An Embodiment of the Invention

- introduce parser generator system
- describe system components
- motivate formal verification
- introduce parsing expression grammars
- define parsing expressions
- provide example grammar

### Example 1

- provide simple grammar example

### 2. Description of Some Embodiments

- introduce system/method for creating parser generator
- extend PEGs with semantics actions
- define default semantic actions
- introduce new construction to convert semantic values
- define types for semantic values
- extend parsing expressions to incorporate semantic values
- define formal definition of extended parsing expressions
- prove termination for PEGs
- define expression set of PEG
- define three groups of properties over parsing expressions
- define inference rules for deriving properties
- summarize semantics of properties
- perform well-formedness analysis for PEG
- introduce certified parser interpreter
- develop generic interpreter for parsing input
- prove termination of parsing process
- develop parser generator for PEGs
- extract certified parser generator from Coq development

### 3. Summary of Three Embodiments of the Invention

- introduce three embodiments of the invention
- define PA, FPG, Q, and G
- describe first embodiment: parser interpreter with semantic actions
- define FPG and its formal semantics
- develop parser interpreter with semantic actions
- prove correctness and termination of parser interpreter
- extract certified parser interpreter
- describe second embodiment: parser generator with semantic actions
- develop parser generator with semantic actions
- prove correctness and termination of parser generator
- extract certified parser generator
- describe third embodiment: parser interpreter with parsing traces
- develop parser interpreter with parsing traces

