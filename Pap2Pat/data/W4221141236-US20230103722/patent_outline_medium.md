# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate ASR technology

## SUMMARY

- introduce guided data selection method
- process encoded representations
- generate probability distributions
- assign confidence scores
- select unmasked encoded representations
- generate masked encoded representations
- describe optional features
- pretrain audio encoder
- describe system implementation

## DETAILED DESCRIPTION

- introduce automated speech recognition (ASR) and text-to-speech (TTS) systems
- describe limitations of ASR models
- introduce pre-training ASR models with large amounts of unlabeled speech or text data
- describe masked speech modeling (MSM) pre-training technique
- motivate guided data selection for MSM
- introduce ASR system 100 and its components
- describe user device 102 and its components
- describe audio subsystem 108 and its function
- describe ASR model 200 and its components
- describe encoder network 210 and its function
- describe prediction network 220 and its function
- describe joint network 230 and its function
- describe Softmax layer 240 and its function
- introduce ask-to-mask (ATM) training process 300
- describe training data used in ATM training process 300
- describe text-to-speech (TTS) system 330 and its function
- describe synthesized speech representations 332
- describe data augmentation applied to synthesized speech representations 332
- introduce contrastive self-supervised loss part 300a
- introduce cross-entropy self-supervised loss part 300b
- introduce final training objective self-supervised loss part 300c
- describe audio encoder 210 and its components
- introduce masking module 400 and its components
- describe scorer model 410 and its function
- describe masker 420 and its function
- describe contrastive self-supervised loss part
- generate contrastive loss term
- derive diversity loss
- pre-train audio encoder
- describe cross-entropy loss part
- generate cross-entropy loss
- refine contrastive context vectors
- describe final training objective self-supervised loss part
- derive final training objective
- weight final training objective
- describe method of guided data selection
- obtain sequence of encoded representations
- process encoded representations
- assign confidence scores
- select unmasked encoded representations
- generate masked encoded representations
- describe computing device
- describe processor and memory
- describe storage device

