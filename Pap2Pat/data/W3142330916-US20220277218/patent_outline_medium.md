# DESCRIPTION

## STATEMENT RE: FEDERALLY SPONSORED RESEARCH/DEVELOPMENT

- state not applicable

## BACKGROUND

### Technical Field

- relate to transformer-based model

### Background

- motivate transformer-based models

## BRIEF SUMMARY

- introduce predictive model
- receive input image and text
- tokenize input text
- generate patch groups
- mask image patches and text tokens
- generate training embedding
- train cross modality transformer-based model
- align input text tokens with image patches
- mask aligned image patches and text tokens
- replace masked text tokens
- replace masked image patches
- mask aligned image patches from multiple patch groups
- preferentially mask aligned tokens and patches
- align tokens with image patches using attention map
- generate image embedding
- generate text embedding
- concatenate image and text embeddings
- train model with multiple loss functions
- define individual loss functions

## DETAILED DESCRIPTION

- introduce vision-linguistic models
- limitations of existing models
- propose domain-specific transformer-based model
- describe single-stream, two-stream, and three-stream models
- focus on single-stream model based on BERT framework
- introduce masking strategy at embedding level
- describe "kaleidoscope" patch strategy for images
- use attention information to build pre-alignments
- guide masking strategy with pre-alignment information
- pre-train model to learn fine-grained cross-modality information
- describe application of model in fashion product search system
- illustrate system architecture
- describe functionality of cross modality transformer-based model
- illustrate training system for domain specific transformer-based model
- describe patch generator
- generate image patches at different levels of granularity
- describe attention-based alignment generator
- generate alignment pairs between image patches and text tokens
- describe alignment guided masking functionality
- mask image patches and text tokens based on alignment pairs
- generate image embeddings and text embeddings
- describe pre-training tasks
- describe patch modeling training task
- describe image-text matching task
- describe masked word modeling functionality
- illustrate components of patch generator
- illustrate components of alignment guided masking functionality
- introduce rotation recognition task
- introduce jigsaw puzzle solving task
- introduce camouflage prediction task
- introduce grey-to-color modeling task
- introduce blank-to-color modeling task
- describe aligned kaleidoscope patch modeling
- describe fine-grained patch cross-modality transformer model
- evaluate model on four VL tasks
- describe image-text retrieval task
- describe text-image retrieval task
- describe category recognition and fashion captioning tasks
- summarize universal pre-trained vision-language understanding architecture

