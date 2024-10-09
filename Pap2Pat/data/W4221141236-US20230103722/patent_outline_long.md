# DESCRIPTION

## TECHNICAL FIELD

- relate to guided data selection

## BACKGROUND

- introduce automatic speech recognition
- discuss challenges in developing ASR models

## SUMMARY

- introduce guided data selection method
- obtain sequence of encoded representations
- process encoded representations using scorer model
- assign confidence scores to encoded representations
- select unmasked encoded representations to mask
- generate masked encoded representations
- select top-K encoded representations to mask
- generate target context vectors for unmasked representations
- generate contrastive context vectors for masked representations
- generate contrastive loss for masked representations
- pretrain audio encoder using contrastive losses
- generate K-means clusters for unmasked representations
- generate cross-entropy loss for masked representations
- pretrain audio encoder using cross-entropy losses
- determine final training objective
- pretrain audio encoder using final training objectives
- determine utterance-level confidence score
- weight final training objective based on confidence score
- extract bottleneck features from contrastive context vectors

## DETAILED DESCRIPTION

- introduce automated speech recognition (ASR) and text-to-speech (TTS) systems
- describe limitations of ASR models
- motivate pre-training ASR models with large amounts of unlabeled speech or text data
- introduce masked speech modeling (MSM) pre-training technique
- describe limitations of MSM pre-training technique
- introduce guided data selection for MSM
- describe ASR system architecture
- introduce user device and remote computing device
- describe audio subsystem and input acoustic frames
- describe ASR model architecture
- introduce Recurrent Neural Network-Transducer (RNN-T) model architecture
- describe encoder network, prediction network, and joint network
- describe output distribution of joint network
- introduce Softmax layer
- describe beam search process
- introduce conformer blocks and transformer blocks
- describe prediction network architecture
- introduce joint network architecture
- describe softmax layer architecture
- introduce ask-to-mask (ATM) training process
- describe available training data
- introduce unspoken textual utterances
- introduce transcribed non-synthetic speech utterances
- introduce un-transcribed non-synthetic speech utterances
- introduce synthesized speech representations
- describe text-to-speech (TTS) system
- introduce speaker embedding
- describe data augmentation
- introduce contrastive self-supervised loss part
- introduce cross-entropy self-supervised loss part
- introduce final training objective self-supervised loss part
- describe audio encoder architecture
- introduce Conformer encoder
- describe convolution subsampling block
- introduce masking module
- describe scorer model
- introduce probability distribution over possible speech recognition hypotheses
- describe confidence score assignment
- introduce masker
- describe selection of unmasked encoded representations for masking
- describe generation of masked encoded representations
- introduce predetermined ratio of encoded representations to be masked
- describe training process using masked encoded representations
- introduce final training objective
- describe advantages of guided data selection for MSM
- introduce utterance-level confidence score
- describe weighting of final training objective
- introduce application of guided data selection for MSM
- describe benefits of guided data selection for MSM
- introduce future applications of guided data selection for MSM
- conclude guided data selection for MSM
- describe contrastive self-supervised loss part
- generate contrastive loss term
- derive contrastive training objective
- pre-train audio encoder
- describe cross-entropy loss part
- generate cross-entropy loss
- pre-train audio encoder
- describe final training objective self-supervised loss part
- generate refined contrastive context vectors
- derive final training objective
- pre-train audio encoder
- describe utterance-level confidence score
- weight final training objective
- describe guided data selection for masked speech modeling
- obtain sequence of encoded representations
- process encoded representations using scorer model
- assign confidence scores
- select unmasked encoded representations to mask
- generate masked encoded representations
- describe computing device
- describe processor
- describe memory
- describe storage device
- describe high-speed interface/controller
- describe low-speed interface/controller
- describe display
- describe input/output devices
- describe computer program product
- describe machine-readable medium
- describe computer-readable medium
- describe programmable processor
- describe data processing hardware
- describe special purpose logic circuitry
- describe mass storage devices
- describe computer readable media
- describe user interaction
- describe display device
- describe input devices
- describe feedback and input methods

