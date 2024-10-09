# DESCRIPTION

## STATEMENT OF GOVERNMENT LICENSE RIGHTS

- state government license rights

## BACKGROUND

- motivate protein structure determination
- limitations of current methods

## SUMMARY

- introduce protein structure determination method
- describe neural network-based approach
- outline molecular structure determination steps

## DETAILED DESCRIPTION

- introduce protein complex structure determination method
- describe cryo-EM density maps and amino acid sequences input
- outline method 100 for determining molecular structure
- describe pre-processing of voxel data
- outline use of deep convolutional neural networks
- describe first neural network for atom type likelihood
- describe second neural network for backbone atom likelihood
- describe third neural network for secondary structure likelihood
- describe fourth neural network for amino acid type likelihood
- illustrate U-Net architecture for neural networks
- describe training dataset collection and preparation
- describe training of neural networks
- describe subroutine for determining backbone structure
- describe mapping of amino acid sequences to backbone structure
- describe determining locations of carbon, nitrogen, and oxygen atoms
- describe determining side-chain atoms
- describe storing completed molecular structure
- illustrate procedure for determining backbone structure
- describe finding connected groups of voxels and identifying disconnected chains
- describe optimization of point cloud to determine backbone structure
- illustrate alignment technique
- motivate need for new alignment technique
- define reward function
- define gap penalty function
- describe dynamic algorithm for alignment
- illustrate procedure for determining atom locations
- determine initial positions for carbon and nitrogen atoms
- refine positions of carbon and nitrogen atoms
- further refine positions using molecular mechanics
- determine positions of oxygen atoms
- describe computing device architecture
- describe system memory and communication bus
- describe network interface and storage medium
- describe optional components of computing device

### Results

- compare performance with Phenix's map-to-model function
- introduce phenix.chain comparison tool
- calculate metrics for comparison
- analyze results for multiple test datasets
- apply Local-Global Alignment algorithm
- compare with Rosetta and MAINMAST
- illustrate molecular structures derived by embodiment
- test on SARS-CoV-2 related density maps
- analyze computation time used by embodiment
- discuss potential of embodiments

