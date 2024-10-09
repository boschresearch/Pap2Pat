# DESCRIPTION

## STATEMENT OF GOVERNMENT LICENSE RIGHTS

- state government license rights

## BACKGROUND

- introduce protein structure importance
- describe cryo-EM technology
- motivate need for automated structure determination
- limitations of existing tools

## SUMMARY

- introduce method for determining molecular structure
- receive voxel data
- predict likelihoods using neural networks
- determine backbone structure
- map amino acid sequences
- determine atom locations
- store molecular structure

## DETAILED DESCRIPTION

- introduce protein complex structure determination
- describe cryo-EM density maps and amino acid sequences
- illustrate method overview
- receive voxel data and amino acid sequences
- pre-process voxel data
- describe neural network architecture
- illustrate U-Net architecture
- describe training dataset collection
- describe training process
- create masks for neural networks
- describe atoms mask creation
- describe backbone mask creation
- describe secondary structure mask creation
- describe amino acid type mask creation
- predict atom types
- predict backbone structure
- predict secondary structure positions
- predict amino acid types
- determine backbone structure
- map amino acid sequences to backbone structure
- describe alignment technique
- determine locations of carbon, nitrogen, and oxygen atoms
- determine side-chain atoms
- complete molecular structure
- store completed molecular structure
- illustrate procedure for determining backbone structure
- round likelihoods to zero or one
- find connected groups of voxels
- identify disconnected chains of alpha atoms
- determine points in space for each alpha atom
- conduct optimization on point cloud
- describe modified traveling salesman algorithm
- describe confidence function
- combine metric values into confidence score
- provide backbone structures of disconnected chains
- illustrate U-Net architecture
- describe neural network training
- describe voxel data pre-processing
- describe neural network output
- describe post-processing of neural network output
- describe final molecular structure determination
- introduce alignment technique
- motivate alignment technique
- describe limitations of previous alignment techniques
- define reward function
- explain gap penalty
- define penalty function
- describe dynamic algorithm
- define recursive equation
- illustrate procedure for determining locations of carbon, nitrogen, and oxygen atoms
- determine initial positions for carbon and nitrogen atoms
- refine positions of carbon and nitrogen atoms
- further refine positions of carbon and nitrogen atoms
- describe planar peptide geometry
- construct virtual bond
- refine position of carbon atom
- refine position of nitrogen atom
- determine location of oxygen atom
- provide positions for oxygen atoms
- illustrate aspects of exemplary computing device
- describe processor
- describe system memory
- describe communication bus
- describe network interface
- describe storage medium
- describe optional storage medium
- describe input devices
- describe output devices
- conclude computing device description

### Results

- compare performance of embodiment with Phenix's map-to-model function
- introduce phenix.chain comparison tool
- define metrics calculated by phenix.chain comparison tool
- apply Local-Global Alignment algorithm
- calculate Global Distance Calculation score
- compare results of embodiment with Phenix's method
- summarize improvement in matching percentage
- analyze RMSD values
- discuss sequence matching percentage
- evaluate mean length of matched segments
- compare embodiment with Rosetta and MAINMAST
- illustrate molecular structures derived by embodiment and Phenix
- introduce SARS-CoV-2 related results
- compare evaluation results for SARS-CoV-2 related density maps
- analyze matching percentage for SARS-CoV-2 related density maps
- discuss RMSD values for SARS-CoV-2 related density maps
- evaluate sequence matching percentage for SARS-CoV-2 related density maps
- illustrate structures modelled by embodiment for SARS-CoV-2 related density maps
- discuss computation time used by embodiment versus Phenix
- analyze computational time for processing large protein complexes
- conclude advantages of embodiments of the present disclosure

