# DESCRIPTION

## CROSS REFERENCE(S)

- claim priority

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate text summarization

## DETAILED DESCRIPTION

- introduce limitations of existing summarization systems
- motivate controllable summarization system
- describe controllable summarization system overview
- define controllable summarization system components
- describe neural network model for controllable summarization
- explain keyword manipulation mechanism
- describe user interaction with control center
- illustrate controllable summarization system workflow

### Controllable Summarization Overview

- introduce traditional unconstrained neural summarization methods
- describe controllable summarization system architecture
- explain probability distribution p(y|x, z)
- describe keyword extraction mechanism
- illustrate controllable summarization system workflow
- describe user interaction with control center
- explain control tokens and prompts
- describe flexibility of controllable summarization system
- illustrate example of controllable summarization system

### Computer Environment

- describe computing device architecture
- explain processor and memory components
- describe machine readable media
- illustrate computing device implementation
- describe controllable summarization module
- explain data interface and input/output
- describe sub-modules of controllable summarization module

### Controllable Summarization Work Flows

- describe training process for keywords-based summarization model
- receive input document and ground-truth summary
- select sentences from document that maximize ROUGE scores
- identify longest sub-sequences in extracted sentences
- remove duplicate words and stop words
- generate keyword sequence
- prepend keyword sequence to source document
- train summarization model to maximize p(y|x, z)
- describe keyword extraction strategy
- describe keyword dropout regularization
- describe inference stage for generating controlled summary
- receive input document
- extract keywords from input document
- receive user input of control token sequence
- modify set of keywords based on control token sequence
- generate summary based on customized set of keywords
- describe entity control and length control
- describe use of prompts for multi-purpose text generation
- illustrate example of controllable summarization system

### Example Performance

- provide qualitative examples of summaries
- show source document summarized into different versions
- illustrate re-summarization by prompts
- describe performance on distinct-domain summarization datasets
- detail conditional distribution p(y|x, z) in keyword-based model
- explain automatic keyword tagger at test time
- describe summarization model implementation
- detail automatic keyword extraction model
- evaluate ROUGE scores and BERTScore
- evaluate control-related performance
- simulate user preference for entity control
- test performance of entity control
- examine factual consistency of summaries
- report Success Rate and factual correctness evaluations
- illustrate example performance of keywords-based model
- compare CTRLsum with BART
- examine effect of oracle length signal
- measure length distance between decoded summary and reference
- assess summary variations as length signals change
- report Pearson Correlation Coefficient (PCC)
- evaluate contribution summarization of scientific papers
- extract contribution claims as reference summary
- evaluate purpose summarization on patent filings
- collect test dataset for purpose summarization
- show results of contribution and purpose summarization
- test question-guided summarization on reading comprehension benchmarks
- evaluate zero-shot performance on NewsQA and SQuAD 1.1
- show uncontrolled summarization performance
- evaluate human evaluation results for controlled summarization
- describe computing devices and machine-readable media

