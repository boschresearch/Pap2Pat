# DESCRIPTION

## TECHNICAL FIELD

- relate to self-supervised semantic learning

## DESCRIPTION OF RELATED ART

- motivate self-supervised video labeling
- limitations of prior self-supervised approaches

## BRIEF SUMMARY OF THE DISCLOSURE

- introduce multi-view cooperative contrastive self-supervised learning
- embodiment of method for multi-view cooperative contrastive self-supervised learning
- embodiment of system for multi-view cooperative contrastive self-supervised learning

## DETAILED DESCRIPTION

- introduce self-supervised visual representation learning
- describe Cooperative Contrastive Learning (CoCon) technique
- illustrate CoCon overview with example images
- explain multiple views creation and embeddings computation
- describe flow diagram for cooperative contrastive learning
- compute features using view-specific encoders
- determine distances in resultant embeddings
- determine inconsistencies in distances
- encourage distances in all embeddings to become similar
- apply CoCon to video sequences for self-supervised training
- receive video sequence and partition into disjoint blocks
- transform each block into latent representation
- generate context representation
- predict future blocks to learn effective representations
- describe dense predictive coding framework
- illustrate architectural representation for CoCon
- compute Noise Contrastive Estimation (NCE) loss
- synchronize distances across all views
- introduce cooperative loss function
- define similarity loss
- introduce contrastive predictive coding
- describe self-supervised learning framework
- introduce multi-view experiments
- describe data augmentation
- introduce 3D-ResNet encoder
- describe predictive task
- introduce evaluation of learned representations
- describe fine-tuning for action classification
- introduce t-SNE visualizations
- describe emergence of higher-order semantics
- introduce manifold consistency across views
- describe cosine similarities
- introduce soft alignment videos
- describe leveraging relationships across views
- introduce computing component
- describe processor and memory components
- introduce information storage mechanism
- describe communications interface
- introduce software and data transfer
- describe computer program medium
- provide disclaimer on applicability of features

