# DESCRIPTION

## BACKGROUND

- introduce neural machine translation systems

## SUMMARY

- describe system for natural language translations using neural network translation models and rare word post-processing

## DETAILED DESCRIPTION

- introduce translation system 100
- describe neural network translation model 120
- describe rare word processing subsystem 130
- describe word dictionary 140
- describe neural network translation model 120 mapping source language sentences to target language sentences
- describe handling out-of-vocabulary (OOV) words
- describe training neural network translation model 120 to track origin of unknown words
- describe replacing pointer tokens with corresponding source words
- describe generating target sentence from source sentence
- describe FIG. 2, process 200 for training neural network translation model
- obtain parallel corpus
- derive alignment data from parallel corpus
- annotate sentences in parallel corpus according to alignment data
- describe copyable model annotation strategy
- describe positional all model annotation strategy
- describe positional unknown model annotation strategy
- train neural network translation model on training dataset
- construct word dictionary using alignment data
- describe FIG. 3, process 300 for generating target language sentence
- receive source language sentence
- process sentence using trained neural network translation model
- annotate source language sentence according to rare word model annotation strategy
- generate target language sentence
- replace pointer tokens with corresponding source words
- generate final translation for source language sentence

