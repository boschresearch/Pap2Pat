# DESCRIPTION

## TECHNICAL FIELD

- introduce masked autoencoders for computer vision

## BACKGROUND

- motivate deep learning
- limitations of autoencoding methods in vision

## SUMMARY OF PARTICULAR EMBODIMENTS

- pre-train machine-learning model using masked autoencoder approach
- apply pre-trained model to downstream tasks
- select visible and masked patches based on masking criteria
- generate latent representations and full set of tokens
- reconstruct masked patches using decoder
- update model parameters based on loss function
- apply pre-trained encoder to second model for computer vision task

## DESCRIPTION OF EXAMPLE EMBODIMENTS

- introduce masked autoencoder approach
- describe asymmetric encoder-decoder design
- explain masking process
- discuss masking criteria
- introduce masking ratio
- illustrate example input and output images
- discuss random sampling technique
- discuss block-wise sampling technique
- discuss grid-wise sampling technique
- illustrate example images and output images
- describe encoder operation
- explain positional encoding
- discuss transformer encoder architecture
- describe multi-head attention component
- discuss feed forward network
- explain residual connections and layer normalization
- discuss output of encoder
- describe adding mask tokens to latent representations
- discuss forming full set of tokens
- describe decoder operation
- discuss transformer decoder architecture
- describe masked multi-head attention component
- discuss output of decoder
- explain reconstructing image
- discuss updating model based on loss function
- illustrate example input and output images
- discuss applying pre-trained encoder to other models
- introduce refinement techniques
- define fine-tuning technique
- describe linear probing technique
- compare fine-tuning and linear probing techniques
- illustrate charts comparing accuracy
- discuss partial fine-tuning technique
- illustrate chart depicting accuracy of partial fine-tuning
- introduce method for pre-training machine-learning model
- describe accessing image for pre-training
- divide image into patches
- select visible and masked patches
- generate mask tokens and positional encodings
- process encoder and generate latent representations
- generate full set of tokens and apply decoder
- update machine-learning model based on loss function
- apply pre-trained encoder to second machine-learning model
- describe computer system 1000
- illustrate computer system 1000
- define computer system 1000
- describe processor 1002
- illustrate processor 1002
- describe memory 1004
- illustrate memory 1004
- describe storage 1006
- illustrate storage 1006
- describe I/O interface 1008
- illustrate I/O interface 1008
- describe communication interface 1010
- illustrate communication interface 1010
- describe bus 1012
- define computer-readable non-transitory storage medium

