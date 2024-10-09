# DESCRIPTION

## STATEMENT RE: FEDERALLY SPONSORED RESEARCH/DEVELOPMENT

- state not applicable

## BACKGROUND

### Technical Field

- relate to transformer-based model

### Background

- introduce transformer-based models
- describe limitations of current VL models

## BRIEF SUMMARY

- introduce method of pre-training predictive model
- receive input image and text
- tokenize input text
- generate patch groups of image patches
- mask image patches and input text tokens
- generate training embedding
- train cross modality transformer-based model
- align input text tokens with aligned image patches
- mask aligned image patches and input text tokens
- replace input text token with mask token or random word
- replace aligned image patches with similar patch or greyed/blank version
- mask aligned image patches from multiple patch groups
- preferentially mask aligned input text tokens and image patches
- generate text description of input image
- match tokens of generated text description with input text
- align matched tokens with image patches
- generate image embedding from image patches
- generate text embedding from input text tokens
- concatenate image and text embeddings
- add location and segment information to image patches
- add position and segment information to input tokens
- train transformer-based model with multiple loss functions
- define aligned masked language modeling task
- define image and text matching task
- define rotation recognition task
- define jigsaw puzzle solving task
- define camouflage prediction task
- define grey-to-color modeling task
- define blank-to-color modeling task
- minimize overall loss function
- define individual loss functions
- provide cross-entropy loss function
- provide cross modality transformer function
- provide hidden output of masked-out tokens
- provide hidden output of CLS token
- provide hidden output of image patches
- provide masked-out text sequence
- provide masked-out kaleidoscope patch sequence
- provide KL-divergence

## DETAILED DESCRIPTION

- introduce vision-linguistic models
- focus on fine-grained representation learning
- describe domain-specific transformer-based model
- pre-train model using multi-modal approach
- apply model to fashion domain
- train model on fashion-related images and descriptions
- use fine-grained image patches for image embeddings
- align image patches and text tokens
- use alignment guided masking approach
- mask one of image patch or text token from aligned pair
- use model for various applications
- categorize image-text pair models into single-stream, two-stream, or three-stream models
- describe single-stream model based on BERT framework
- focus on masking strategy at embedding level
- align embedding features between image and text
- develop "kaleidoscope" patch strategy for images
- extract multi-grained image patches for image-modality
- use attention information to build pre-alignments
- guide masking strategy with pre-alignment information
- force model to learn semantic information across modalities
- use kaleidoscope patch based training
- outperform other fixed-patch vision-linguistic models
- introduce pre-alignment strategy
- infer cross-modality mapping between kaleidoscope patches and text tokens
- use pre-alignment pairs in alignment-guided strategy
- obtain new state-of-the-art performance on four downstream tasks
- achieve 1st place on Fashion-Gen benchmark
- depict application of domain-specific transformer-based model
- describe fashion product search system or interface
- allow user to search for fashion products using text description
- return product images based on search terms
- provide computer system for fashion product search interface
- execute instructions to configure system
- use cross modality transformer-based model for search
- process and catalogue products/images using trained model
- rank collection data to determine products/images that match search text
- return top ranked results for display
- depict method of training domain-specific transformer-based model
- receive input image and input text
- process input image to generate image patches
- generate kaleidoscope patches at different levels of granularity
- tokenize input text
- mask one or more of image patches and text tokens
- generate training embedding using masked patches and tokens
- train transformer-based model using training embedding
- depict training system for domain-specific transformer-based model
- adopt standard transformer designed for NLP
- make cross-modality model scalable over varying number of tasks
- receive input image and input text
- generate image patches using patch generator
- generate alignment pairs between image patches and text tokens
- use alignment guided masking functionality
- generate masked image patches and masked text
- use masked patches and tokens to train cross-modality transformer model
- introduce rotation recognition task
- define objective of rotation recognition task
- introduce jigsaw puzzle solving task
- define objective of jigsaw puzzle solving task
- introduce camouflage prediction task
- define objective of camouflage prediction task
- introduce grey-to-color modeling task
- define objective of grey-to-color modeling task
- introduce blank-to-color modeling task
- define objective of blank-to-color modeling task
- describe aligned kaleidoscope patch modeling
- define total loss function
- describe application of subtasks to patch group levels
- depict graphs of training task losses
- evaluate fine-grained patch cross-modality transformer model
- describe settings for evaluation
- introduce image-text retrieval task
- introduce text-image retrieval task
- introduce category recognition task
- introduce fashion captioning task
- compare performance of current model to other models
- describe advantages of current approach
- describe universal pre-trained vision-language understanding architecture
- provide general statements on implementation and variations

