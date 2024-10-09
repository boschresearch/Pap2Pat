# DESCRIPTION

## TECHNICAL FIELD

- relate to self-supervised semantic learning

## DESCRIPTION OF RELATED ART

- introduce video labeling approaches
- motivate self-supervised methods
- limitations of current self-supervised methods
- summarize multi-view learning approaches
- limitations of multi-view learning approaches

## BRIEF SUMMARY OF THE DISCLOSURE

- introduce multi-view cooperative contrastive self-supervised learning
- describe method for receiving video sequences
- describe method for deriving embeddings
- describe method for determining distances
- describe method for detecting inconsistencies
- describe method for predicting semantics
- describe additional embodiments

## DETAILED DESCRIPTION

- introduce self-supervised visual representation learning
- describe data-driven sampling for leveraging implicit relationships
- introduce Cooperative Contrastive Learning (CoCon) technique
- motivate overcoming shortcomings of multi-view learning
- describe inter-view information utilization
- illustrate CoCon example with two images and multiple views
- describe view-specific deep encoders
- explain leveraging inconsistencies between views
- describe using cosine distance to determine embedding distances
- introduce contrastive loss learning for self-supervised training
- describe combining multiple views for better representation
- analyze each view to provide specific patterns
- leverage inter-view information to infer relationships
- describe using multiple embeddings to infer relationships
- motivate using available views of input data
- describe using high-level inferred semantics as additional views
- illustrate example process for cooperative contrastive learning
- compute features using view-specific encoders
- determine distances in resultant embeddings
- determine inconsistencies in distances
- encourage distances in all embeddings to become similar
- apply cooperative contrastive learning to video sequences
- construct binary classification task for self-supervised training
- partition video sequence into disjoint blocks
- transform each block into latent representation
- generate context representation
- predict future blocks to learn effective representations
- use dense predictive coding framework for self-supervised learning
- define prediction task to capture contextual semantics
- utilize different datasets for training and evaluation
- describe architectural representation for cooperative contrastive learning
- break up video sequence into blocks
- encode each block into latent representation
- aggregate latent representations into context representation
- compute Noise Contrastive Estimation (NCE) loss over feature embeddings
- synchronize distances across all views using consistency loss
- introduce cooperative loss function
- define similarity loss
- introduce contrastive predictive coding
- describe self-supervised learning framework
- introduce multi-view experiments
- describe dataset UCF101
- describe dataset HMDB51
- describe dataset Kinetics-400
- describe implementation details
- describe data augmentation
- describe training procedure
- evaluate performance on action classification
- describe fine-tuning procedure
- visualize learned representations
- analyze emergence of higher-order semantics
- study manifold consistency across views
- evaluate consistency of nearest classes
- describe soft alignment of videos
- illustrate alignment of videos
- discuss effectiveness of multi-view approach
- describe module implementation
- describe component implementation
- describe computing component architecture
- describe processor implementation
- describe memory implementation
- describe information storage mechanism
- describe media drive implementation
- describe storage unit interface
- describe communications interface
- describe channel implementation
- describe computer program medium
- describe computer usable medium
- describe computer program code
- describe computer program product
- discuss applicability of features
- discuss open-ended terms and phrases
- discuss conventional technologies
- discuss broadening words and phrases
- discuss component configuration
- discuss block diagram implementation
- discuss flow chart implementation
- discuss illustration implementation
- discuss architecture and configuration
- discuss implementation without confinement
- discuss exemplary embodiments
- discuss various alternatives

