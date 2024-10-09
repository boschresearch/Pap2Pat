# DESCRIPTION

## TECHNICAL FIELD

- relate to neuropharmacology analysis

## BACKGROUND

- introduce drug screening

## SUMMARY OF THE INVENTION

- provide method for neuropharmacology analysis
- provide system for neuropharmacology analysis
- classify brain activity map using functional classifiers
- perform statistical analysis and/or machine learning
- identify relationship between brain activity maps and therapeutic function
- rank chemical compound based on identified relationship
- represent relationship as coefficients and/or factors
- determine standardized scores for regions of interest
- obtain score maps associated with standardized scores
- filter standardized scores with brain template
- apply principle component analysis to score maps
- generate functional classifiers using characteristic features
- generate brain activity maps from images
- construct brain activity maps from neural spikes
- process image raw data to generate images
- immobilize and orient living species
- use microfluidic device to load and orient living species
- specify living species and known drugs

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENT

- introduce CNS disorders
- limitations of current CNS pharmacopeia
- motivate novel paradigms for CNS drug discovery
- introduce whole-brain imaging of small animals
- describe method for analyzing neuropharmacology of a drug
- provide overview of system for analyzing neuropharmacology
- describe imaging module
- describe transformation module
- describe processing module
- introduce microfluidic device
- describe fabrication of microfluidic chip
- describe use of calcium sensitive fluorescent reporters
- describe autonomous system for high-throughput recording
- illustrate use of hydrodynamic force to load zebrafish larvae
- describe loading and aligning zebrafish larvae
- describe use of transgenic zebrafish with genetically encoded calcium indicator
- describe system for larvae loading and transportation
- illustrate flow direction-switching-loop
- describe automated control of larva handling cycles
- describe video detection module
- describe drug perfusion time
- describe generation of functional BAM
- describe transformation of image data
- describe construction of brain activity maps
- describe calculation of spike counts
- describe filtering of fluorescence signal
- describe visualization of spiking activities
- describe resizing and aligning of images
- describe removal of fish eye region
- describe calculation of brain activity map
- describe statistical comparison of BAMs
- describe generation of T-score maps
- describe filtering with uniform zebrafish brain template
- describe analytical workflow for generation of T-score BAMs
- describe calculation of T-score
- describe background T-score BAMs
- describe HT-BAMing technology
- describe application to library of clinically used CNS drugs
- describe observation of drug treatment effects
- describe example BAM patterns for different drugs
- describe association of BAMs with functional drug categories
- describe principle component analysis of T-score BAMs
- describe decomposition of T-score BAMs into characteristic features
- describe projection of T-score BAMs onto PC vector space
- describe identification of top PCs
- describe reconstruction of T-score BAMs
- describe conversion to dimensionality-reduced Pheno-Print
- describe Pheno-Prints of functionally related drugs
- generate functional classifiers using supervised or unsupervised clustering
- apply consensus clustering to detect intrinsic coherence among similar T-score BAMs
- identify BAM clusters using principal component analysis and consensus clustering
- calculate representative cluster patterns for each BAM cluster
- perform one-tailed Wilcoxon signed-rank test for each drug
- identify relationship between BAM clusters and therapeutic function of compounds
- perform hypergeometric test for over-representation of ATC categories in BAM clusters
- link identified phenotypic BAM clusters to therapeutic drug categories
- predict therapeutic function of non-clinical compounds using two-step prediction strategy
- classify non-clinical compounds into phenotypic BAM clusters using random forest classifier
- prioritize predictions based on Pearson correlation coefficient
- identify significant overlap between BAM clusters and ATC categories
- describe structurally similar compounds with different therapeutic functions
- separate compounds with similar chemical structures into distinct BAM clusters
- predict neuropharmacology of neuroactive compound based on association
- validate BAM cluster method using additional test set of compounds
- employ BAM-based phenotyping to predict therapeutic role of non-clinical compounds
- assign compounds to BAM clusters using random forest classifier
- prioritize compounds based on Pearson correlation coefficient
- observe predicted cluster enriched for potential anti-epileptics
- identify compounds with previously reported anti-epileptic activity
- predict novel anti-epileptic candidates
- test reliability of HT-BAMing-based compound screening strategy
- repeat analysis on small subgroup of compounds
- validate screening strategy and analysis using additional clinical anti-epileptics
- describe preferred embodiment
- validate machine learning-based therapeutic classification
- select top-ranked anti-epileptic candidates
- describe PTZ induced zebrafish seizure model
- conduct experiments with PTZ model
- analyze results of PTZ model experiments
- describe experimental protocol
- discuss pharmacological effects of NNC-711
- discuss pharmacological effects of GYKI-52466
- discuss non-obvious activities of predicted hits
- describe volinanserin
- describe yangonin
- describe Tubastatin-A
- discuss advantages of HT-BAMing technology
- compare with alternative methods
- describe novel strategy for CNS drug screening
- generate collection of BAMs
- analyze large-scale BAM dataset
- predict drug leads for neurological diseases
- discuss double-blind analysis of training set
- validate strategy in test set
- discuss association between BAM clusters and ATC categories
- discuss diversity of compounds within BAM clusters
- discuss potential of HT-BAMing for complex brain disorders
- discuss validation of prediction results
- discuss power of HT-BAMing based screening strategy
- discuss potential for novel pharmacological discovery
- discuss future refinements of HT-BAMing technology

