# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate genetic interactions

## DETAILED DESCRIPTION

- introduce BridGE technique
- describe genome-wide association studies
- explain missing heritability problem
- define genetic interactions
- discuss challenges of detecting genetic interactions
- motivate use of GWAS for associating mutations in genetic interactions
- describe insights from yeast genetic interaction networks
- illustrate example of two distinct pathways
- explain between pathway model (BPM)
- explain within pathway model (WPM)
- discuss implications of BPM and WPM structures in human GWAS context
- describe method for detecting interactions and predicting phenotypes
- outline data processing operation
- describe construction of mutation-mutation interaction networks
- explain network thresholding and binarization
- describe testing for BPM or WPM enrichment
- outline sample permutation strategy
- describe quality control operation
- explain PLINK inclusion procedure
- describe removal of outlier samples
- explain mapping of mutations to Genome Reference Consortium GRCh37
- describe multi-dimensional scaling (MDS) analysis
- explain removal of related subjects based on IBD factor
- describe splitting of genes into case genes and control genes
- explain clustering of genes into groups of size 2
- describe filtering of mutations in linkage disequilibrium (LD)
- explain mapping of genes to pre-defined pathways
- describe estimation of interaction between mutations
- explain additive model for SNP-SNP genetic interaction estimation
- describe dominant and recessive models for SNP-SNP genetic interaction estimation
- explain estimation of interactions under different models
- describe hypergeometric-based measurement (hygeSSI) for estimating interactions
- outline calculation of hypergeometric p-value
- describe use of logistic regression-based model for interaction estimation
- explain use of explicit statistical tests for interaction estimation
- discuss advantages of different interaction estimation methods
- conclude description of BridGE technique
- define hygeSSI measure
- describe hygeSSI calculation
- explain significance of hygeSSI values
- introduce recessive-recessive and dominant-dominant interaction networks
- describe construction of hybrid genetic interaction network
- motivate pathway enrichment analysis
- describe differences from traditional GSEA approaches
- introduce pairwise pathway enrichment analysis
- describe binarization of hygeSSI values
- break down SNP-SNP interaction network into risk and protective networks
- remove common mutations between two pathways
- test observed SNP-SNP interaction density
- calculate chi-square statistics
- perform permutation tests
- derive empirical p-value
- describe BPM discovery
- correct for multiple hypothesis testing
- estimate false discovery rate
- describe simpler approach to estimate FDR
- introduce disease model selection
- describe pilot experiment
- prioritize disease model and density threshold
- run complete BridGE pipeline
- determine replication in independent cohort
- calculate fold enrichment
- evaluate significance of fold enrichment
- check SNP-SNP interactions supporting BPMs
- control redundancy in discovered BPMs
- introduce within-pathway models
- describe PATH discovery
- examine non-additive interactions
- check statistical significance of SNP-SNP interaction pairs
- characterize statistical power of approach
- generate synthetic interaction network
- embed BPMs into synthetic network
- assess significance of embedded patterns
- display output on graphical displays
- describe potential applications of disclosed methods

### EXAMPLES

- introduce examples of the present disclosure
- describe Example 1: Discovery of Between-Pathway Interactions in a Parkinson's Disease Cohort
- motivate Parkinson's disease study
- describe PD-NIA cohort
- filter gene sets
- apply BridGE to identify between pathway interactions
- report pathway-pathway interactions
- describe significance of vesicle biogenesis-FcεRI signaling BPM
- compare observed and expected SNP-SNP interactions
- show null distribution of SNP-SNP interaction density
- test individual SNP-SNP interactions
- explore BPM interactions at less stringent cutoff
- identify BPM interaction associated with increased PD risk
- describe FIG. 7: network representation of BPM and WPM interactions
- discuss ribosome's role in protein quality control
- implicate ribosomal proteins in PD risk
- describe TGF-β signaling pathway's role in PD
- discuss protective interactions with FcεRI
- describe Example 2: Evidence for within-Pathway Interaction Structures in Parkinson's Disease
- discover within-pathway interactions in PD-NIA cohort
- describe Example 3: Replication of Pathway-Level Interactions in an Independent Parkinson's Disease Cohort
- validate findings in PD-NGRC cohort
- replicate BPM and WPM interactions
- evaluate significance of replication
- show replication analysis in FIG. 8
- evaluate overlap of SNP-SNP interactions supporting replicated BPMs
- show scatter plot of SNP-SNP interaction overlap in FIG. 9
- motivate genetic interaction analysis
- introduce BridGE approach
- apply BridGE to Parkinson's disease
- analyze results of Parkinson's disease
- apply BridGE to other diseases
- analyze results of other diseases
- discuss significance of results
- discuss limitations of approach
- propose future directions
- introduce simulation study
- describe simulation methodology
- analyze simulation results
- discuss implications of simulation results
- describe machine 7000
- define module
- describe hardware components of machine 7000
- describe software components of machine 7000
- describe storage device 7016
- describe machine readable medium 7022
- describe instructions 7024
- describe transmission of instructions 7024
- describe communication networks
- describe network interface device 7020
- describe antennas
- describe MIMO techniques
- describe Multiple User MIMO techniques
- incorporate references
- discuss significance of genetic interactions
- discuss potential applications
- discuss limitations of current approach
- propose future directions
- discuss potential for expansion
- discuss potential for improvement
- discuss potential for integration
- conclude significance of BridGE approach

### Additional Embodiments

- provide computer implemented method
- provide method with quality control
- perform quality control with IBD score
- perform quality control with pathway mapping
- establish interaction with threshold value
- choose nucleic acid mutation type
- choose disease model
- provide non-transitory machine readable medium
- construct interaction network with phenotype
- perform quality control with machine readable medium
- map mutation to gene with machine readable medium
- provide system with processor and memory
- provide method for detecting disease

