# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate ASR

## SUMMARY

- introduce joint speech and text streaming model
- receive unspoken textual utterances
- tokenize unspoken textual utterances
- generate textual feature representation
- receive input to first-pass decoder
- generate probability distribution over text units
- train encoder
- optional: receive input to non-causal audio-text encoder
- optional: generate second textual feature representation
- optional: receive input to second-pass decoder
- optional: generate second probability distribution over text units
- optional: train encoder with transcribed speech utterances
- optional: generate audio feature representation
- optional: train encoder with Hybrid Autoregressive Transducer Factorization

## DETAILED DESCRIPTION

- introduce automated speech recognition
- motivate sequence to sequence models
- describe limitations of deep learning-based ASR models
- introduce unpaired text data
- describe challenges of combining speech and text modalities
- introduce joint speech and text streaming model for ASR
- describe training process for joint model
- introduce speech environment
- describe user device and audio system
- introduce automated speech recognition system
- describe ASR model and speech recognition process
- introduce user interface generator
- describe example interaction with digital assistant application
- introduce natural language processing
- describe ASR model architecture
- introduce RNN-T model architecture
- describe components of RNN-T model
- describe output of joint network
- describe RNN-T model architecture
- detail encoder network structure
- explain prediction network structure
- describe joint network structure
- illustrate training process for encoder
- explain semi-supervised loss part
- explain supervised loss part
- describe alignment model architecture
- detail embedding extractor function
- explain duration predictor function
- describe upsampler function
- explain parameter-free duration model
- detail fixed-repetition model
- explain random repetition model
- describe sub-word distribution model
- describe semi-supervised loss part
- inject lexical information into encoder
- define text encoder
- generate higher order textual feature representations
- describe first-pass decoder
- determine unpaired causal loss term
- describe non-causal audio-text encoder
- generate second higher order textual feature representations
- describe second-pass decoder
- determine unpaired non-causal loss term
- describe supervised loss part
- inject lexical information into encoder
- define causal speech encoder
- generate higher order audio feature representations
- describe paired loss module
- determine paired causal loss term
- describe non-causal audio-text encoder
- generate second higher order audio feature representations
- determine paired non-causal loss term
- define equation 5
- describe training process
- motivate alternative uses of training process
- introduce method 500
- describe operation 502
- describe operations 504-510
- describe operation 512
- introduce computing device 600
- describe components of computing device 600
- describe memory 620
- describe storage device 630
- discuss various implementations

