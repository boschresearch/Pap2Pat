# DESCRIPTION

## TECHNICAL FIELD

- relate to dialogue state tracking

## BACKGROUND

- motivate neural networks
- advantages over other approaches

## DETAILED DESCRIPTION

- introduce dialogue state tracking
- describe dialogue state tracking applications
- motivate neural networks for dialogue state tracking
- describe limitations of current dialogue state trackers
- introduce FIG. 1A
- describe digital system 100
- describe user 110
- describe controller 120
- describe processor 122
- describe memory 124
- describe dialogue state tracker 130
- describe dialogue state 132
- describe context 134
- describe ontology set 140
- describe slots 142 and values 144
- describe scoring model 150
- describe model description 152
- describe model parameters 154
- describe response module 160
- introduce FIG. 1B
- describe example dialogue 170
- describe user communication column
- describe context column
- describe updates to dialogue state 132
- describe response dialogue generated by response module 160
- describe first exchange of example dialogue 170
- describe second exchange of example dialogue 170
- describe third exchange of example dialogue 170
- introduce FIGS. 2A-2C
- describe scoring model 200
- describe ontology member sequence 202
- describe user communication sequence 204
- describe context sequences 206
- describe member score 208
- describe input stages 212, 214, and 216
- describe encoder stages 232, 234, and 236
- describe user communication scoring stage 250
- describe attention layer 282
- describe feed-forward layer 286
- describe context scoring stage 260
- describe attention layer 292
- describe score combiner stage 270
- define scoring model
- describe computational graph
- explain tensor operations
- introduce encoder 300
- describe RNN layer 310
- explain self-attention layer 320
- discuss local trained parameters
- describe challenge of local trained parameters
- introduce global trained parameters
- describe global-local encoder 400
- explain global RNN layer 410
- explain local RNN layer 420
- describe merge module 430
- explain global self-attention layer 440
- explain local self-attention layer 450
- describe merge module 460
- introduce training configuration 500
- describe model 510
- explain learning objective 520
- describe optimizer 530
- introduce method 600
- update dialogue state
- provide system response
- introduce method 700
- predict cumulative goals and/or turn requests
- evaluate learning objective
- update model parameters
- describe experimental evaluation
- compare dialogue state trackers
- describe ablation study
- discuss global-local encoder
- discuss local trained parameters
- discuss global trained parameters
- discuss self-attention layers
- discuss recurrent layers
- discuss limitations of local trained parameters
- discuss benefits of global trained parameters
- discuss benefits of global-local encoder
- discuss importance of self-attention layers
- discuss importance of recurrent layers
- discuss experimental results
- conclude with scope of invention

