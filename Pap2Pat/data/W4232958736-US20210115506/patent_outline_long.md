# DESCRIPTION

## FIELD OF THE INVENTION

- relate to allograft injury measurement

## BACKGROUND OF THE INVENTION

- motivate allograft health monitoring
- limitations of current biopsy method

## SUMMARY OF THE INVENTION

- introduce Genome Transplant Dynamics
- motivate one-genome method
- describe algorithm for dd-cfDNA estimation
- application of method to transplant recipients
- embodiment of method as computer-implemented steps

## DETAILED DESCRIPTION

### Quantifying Dd-cfDNA in Lung and Heart Transplant Recipients

- develop statistical approach
- filter low-quality reads
- calculate probability of observed cfDNA
- compute log-likelihood of data

### Performance of Lung and Heart Rejection Predictions

- compare one-genome and two-genome methods
- assess correlation between methods
- evaluate performance in lung recipients
- evaluate performance in heart recipients
- compare accuracy of methods
- conclude on donor genotyping requirement

### Accuracy of Dd-cfDNA Level Estimations in Bone Marrow Transplant Recipients

- extend model to account for IBD
- evaluate performance of refined one-genome method

### Differentiating Between Relapse and Graft Versus Host Disease in Bone Marrow Transplant Recipients

- analyze cfDNA levels in patients
- hypothesize on differences in recipient-origin DNA
- demonstrate potential of GTD to distinguish between relapses and GVHD

### Methods Section

- introduce cfDNA sequencing and genotyping data collection
- describe dd-cfDNA measurements for bone marrow transplant patients
- outline cfDNA sequencing and genotyping methods
- filter low-quality reads
- map reads to human genome
- filter paired-end reads
- remove biased reads
- remove duplicated reads
- compute chromosomal coverage
- count cfDNA reads containing each SNP allele
- estimate cfDNA donor-derived in recipient unrelated to donor
- define model parameters
- model genotyping error rate
- model sequencing error rate
- model donor genotype dependency on population
- model probability of cfDNA containing specific allele
- define likelihood function
- assume uniform probability of recipient genotype
- define likelihood function for each SNP
- minimize negative log likelihood
- estimate donor-derived cfDNA in related recipient and donor
- model IBD using non-homogenous Hidden Markov Model
- define transition matrix for IBD states
- define emissions probabilities for each SNP in each IBD state
- estimate dd-cfDNA using Viterbi algorithm
- optimize likelihood using L-BFGS-B
- compare one-genome and two-genomes methods predictability
- compute area under ROC curve

## Data and Materials Availability

- provide data and materials sources

