# DESCRIPTION

## TECHNICAL FIELD

- relate to computerized diagnosis of ocular diseases

## BACKGROUND

- motivate early diagnosis of vision degradation diseases
- describe limitations of manual CDR calculation
- introduce OD and OC segmentation
- discuss challenges of deep learning in domain adaptation

## SUMMARY

- introduce method for training neural network
- draw mini-batch of labeled source domain samples
- initiate training of first network
- share training weights with second network
- initiate training of second network
- adjust training weights based on adversarial loss
- transfer average training weights to third network
- initiate training of third network
- compute mean square error loss
- adjust training weights of second network

## DETAILED DESCRIPTION

- introduce ocular cup and disc detection
- motivate domain shift challenge
- describe Collaborative Feature Ensembling Adaptation (CFEA) framework
- describe Collaborative Adversarial Domain Adaptation (CADA) framework
- motivate importance of optic disc and cup features
- describe Cup to Disc Ratio (CDR) calculation
- motivate automation of CDR calculation
- introduce image segmentation
- describe challenges of OD and OC segmentation
- motivate unsupervised domain adaptation
- describe existing works on unsupervised domain adaptation
- introduce adversarial learning
- describe self-ensembling
- describe steps for OD and OC detection
- describe pre-trained disc center localization method
- describe polar transformation
- describe encoder-decoder convolutional network
- motivate domain shift issue
- introduce unsupervised domain adaptation problem
- describe goal of unsupervised domain adaptation
- describe CFEA framework
- describe role of Source domain Network (SN)
- describe role of Target domain Student Network (TSN)
- describe role of Target domain Teacher Network (TTN)
- describe weight self-ensembling
- describe CADA framework
- describe multi-scale input layer
- describe feature interaction between encoder and decoder
- describe multiple discriminators
- describe adversarial losses for domain confusion
- describe MSE losses for encoder and decoder outputs
- describe output compression
- describe discriminator addition
- describe adversarial loss functions
- describe self-ensembling for domain adaptation
- describe EMA predictions and base predictions
- describe integration of adversarial domain confusion and self-ensembling
- define loss functions
- formulate self-ensembling loss
- describe spatial-challenging augmentation
- introduce Dice loss and cross-entropy
- formulate total loss function
- describe min-max problem
- summarize training procedure
- describe dataset and experimental setup
- report experimental results
- compare with baseline model
- analyze importance of encoder adaptation
- investigate effect of self-ensembling
- study multiple discriminators adaptation
- evaluate various combinations of lambda
- show qualitative results
- introduce CFEA and CADA systems
- describe collaborative learning process
- explain benefits of adversarial learning and self-ensembling
- discuss generalizability of CADA framework
- describe running time and computational costs
- summarize experimental results
- introduce interactive paradigms
- describe domain-invariance and model generalizability
- explain ensembling weights via EMA
- describe multiple adversarial losses
- summarize comprehensive experimental results
- introduce computing device architecture
- describe processor and memory components
- introduce GPU and its functions
- describe stored data and components
- introduce neural network models and training logic
- describe data store and operating system
- introduce I/O devices
- discuss hardware and software implementation
- describe discrete logic circuit and ASIC
- introduce PGA and FPGA
- emphasize variations and modifications
- conclude scope of disclosure

