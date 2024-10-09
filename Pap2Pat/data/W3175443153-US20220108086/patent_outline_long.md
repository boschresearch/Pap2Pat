# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate text summarization
- limitations of dialogue summarization
- challenges of dialogue summarization
- limitations of conventional systems

## DETAILED DESCRIPTION

- introduce CorDial model with granular controllability
- create summary draft with user intent information and key phrases
- finetune summary generator with summary draft
- train CorDial model to clip dialogue text with special tokens
- match each summary sentence to its corresponding clipped dialogue context
- generate single sentence for each clipped dialogue context
- enable dialogue summary at different granularity
- make dialogue summary more interpretable
- build CorDial model on top of pre-trained language model
- define "network" or "model" as hardware or software-based framework
- define "module" as hardware or software-based framework
- describe computing device 100 with processor and memory
- describe operation of computing device 100
- describe memory 120 as machine readable media
- describe processor 110 and memory 120 arrangement
- describe CorDial model 130 as neural network
- describe CorDial model 130 receiving input and generating output
- define dialogue conversational history 140
- describe dialogue summary 150 as M-sentence summary
- illustrate CorDial model 130 in inference stage
- describe pre-trained generative language model 205
- describe encoder 210 and decoder 215
- describe dialogue segments 202 and segment summaries 204
- describe concatenation module 220
- describe dialogue-turn-level classifier 225
- describe training CorDial model 130 using summary draft
- describe similarity module 235
- describe parser 240 and label module 245
- describe creating summary draft 250
- describe example action categories
- illustrate summary draft 250
- describe construction of summary draft 250
- explain use of summary draft 250 in training CorDial model 130
- describe training process of CorDial model 130
- explain generation of segment summaries 216
- describe control of number of sentences in dialogue summary 150
- explain identification of dialogue segments 202
- describe training of dialogue turn level classifier 225
- explain prediction of cutting points 208
- describe use of special tokens <hl> and </hl>
- explain generation of dialogue summary 150
- describe training of CorDial model 130 to control number of dialogue segments 202
- explain use of dialogue turn level classifier 225 in inference stage
- describe training of dialogue turn level classifier 225
- explain use of Equation 2
- describe use of BERT-base model as dialogue level turn classifier 225
- explain control of number of output summary sentences
- describe training of CorDial model 130 using oracle dialogue segmentation
- explain generation of segment summaries 316, 318, and 320
- describe method 400 for training CorDial model 130
- divide dialogue conversation history into dialogue segments
- generate summary draft 250
- generate segment summaries 216
- train dialogue turn level classifier 225
- describe method 500 for training CorDial model 130
- divide dialogue conversation history into multiple dialogue segments
- generate segment summaries 204
- concatenate segment summaries into dialogue summary 150
- describe computing devices that may include executable code
- explain machine-readable media that may include executable code
- describe disclaimer for limiting scope
- describe disclaimer for modifications and substitutions

