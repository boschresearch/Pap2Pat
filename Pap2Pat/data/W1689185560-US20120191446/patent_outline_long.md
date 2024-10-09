# DESCRIPTION

## THE NAMES OF PARTIES TO A JOINT RESEARCH AGREEMENT

- no joint research agreement

## FIELD OF THE DISCLOSURE

- introduce parsing problem
- motivate parsing importance
- describe parsing applications
- highlight parsing limitations

## BACKGROUND OF THE DISCLOSURE

- describe parsing process
- explain parser generator
- discuss context-free grammars
- highlight formal verification limitations

## SUMMARY

- introduce parser creation system
- describe grammar input module
- explain formalism module
- summarize semantic action module
- describe checking module
- introduce proof assistant module
- highlight security benefits
- describe parser generator method

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

### 1. Generals Principles of An Embodiment of the Invention

- introduce parser generator system
- describe grammar input module
- describe checking module for grammar verification
- describe checking module for well-formed grammar
- describe semantic action module
- describe formal module for parser generation
- motivate advantages of embodiment
- extend grammar with semantic actions
- prove termination of grammar
- introduce parsing expression grammars (PEGs)
- define parsing expressions
- define parsing expression grammar (PEG)
- provide example of simple grammar for mathematical expressions

### Example 1

- provide example of simple grammar for mathematical expressions

### 2. Description of Some Embodiments

- introduce system/method for creating parser generator
- extend PEGs with semantics actions
- define default semantic actions
- introduce new construction to convert semantic value
- define types (Type, True, char, list α, α*β)
- extend parsing expressions to incorporate semantic values
- define Δα (set of extended parsing expressions)
- define EPEG (extended parsing expressions grammar)
- prove termination for PEGs
- define expression set of PEG
- define three groups of properties over parsing expressions
- define inference rules for deriving properties
- summarize semantics of properties
- perform well-formedness analysis for G
- introduce set of well-formed expressions WF
- iterate to reach fixpoint
- say G is well-formed if E(G)=WF
- prove completeness of G
- provide example of extending grammar with semantic actions
- interpret PEGs
- develop formalization of PEGs in Coq
- develop procedure for checking well-formedness
- develop generic interpreter for parsing input
- prove termination of parsing process
- extract certified parser interpreter from Coq
- provide example of certified parser interpreter
- develop parser generator for PEGs
- extract parser generator from Coq
- develop parser for PEGs themselves
- develop parser for target language Q
- check well-formedness of grammar G
- check termination of semantic actions
- develop termination checker for Q
- choose language Qfin with terminating programs
- develop standard library for parsing
- prove total correctness of generated parsers
- summarize differences between TRX and other parser generators

### 3. Summary of Three Embodiments of the Invention

- introduce three embodiments of the invention
- define PA, FPG, Q, and G
- describe approach of specifying and developing a parser interpreter/generator in PA
- extract parser interpreter/generator with total correctness guarantees
- motivate first embodiment: parser interpreter with semantic actions
- define FPG and its formal semantics
- develop procedure for checking grammar feasibility
- develop parser interpreter with semantic actions
- prove correctness of parser interpreter
- prove termination of parser interpreter
- extract certified parser interpreter
- motivate second embodiment: parser generator with semantic actions
- define FPG and its semantics
- develop procedure for checking grammar feasibility
- define Q and its formal semantics
- develop library of basic datatypes of Q
- develop formally correct parser for Q
- develop formally correct parser for grammar in FPG format
- develop termination checker for semantic actions in Q
- develop parser generator
- prove correctness of generated parser
- prove termination of generated parser
- extract certified parser generator
- motivate third embodiment: parser interpreter with parsing traces
- define FPG extended with parsing tags
- develop parser interpreter with parsing traces
- prove correctness and termination of parser interpreter

