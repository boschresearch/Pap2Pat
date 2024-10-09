# DESCRIPTION

## TECHNICAL FIELD

- define technical field of biodegradation

## BACKGROUND

- introduce oil sands process-affected water
- describe contaminants in oil sands process-affected water
- discuss limitations of current remediation technologies
- motivate need for new bioremediation strategies
- summarize existing biodegradation approaches

## SUMMARY

- introduce gene expression profiling method
- describe RNA sample preparation
- summarize amplicon cDNA library construction
- outline sequencing and genome assembly
- annotate genome assembly to predict differentially expressed genes
- determine reads for differentially expressed genes
- introduce method for identifying genetic elements
- generate reconstructed metabolic pathways
- enrich and score reconstructed metabolic pathways
- analyze functional gene clustering
- identify genetic elements involved in degradation
- introduce method for extracting organic compounds
- describe method for identifying genes involved in degradation
- outline RNA expression analysis for identifying genes
- introduce method for generating gene expression profiles

## DETAILED DESCRIPTION

### a) Definitions

- define technical terms
- define "about", "approximately", and "substantially"
- define "a" and "an" in claims
- define "bacteria"
- define "composition"
- define "comprises", "comprising", "include", "includes", "including", "contain", "contains", and "containing"
- define "gene"
- define "genetic element"
- define "genetic engineering"
- define "include", "includes", and "including"
- define "polynucleotide(s)"
- define "preferred", "preferably", and variants
- define "recombinant"
- define "transformation"
- define "toxic organic compounds"

### b) Differential Gene Expression in Environmental Microbes

- introduce environmental bacterial species
- describe limitations of microbial isolations
- hypothesize microorganisms in OSPW degrade NAFCs
- describe RNA-seq as a tool for transcriptomic response
- describe contaminants in OSPW
- describe NAFCs and NAs
- describe isolation and selection of effective microbes
- describe changes in chemosphere during biodegradation
- describe transcriptomic response of Pseudomonas strains to NA exposure
- describe novel method of differential gene expression analysis

### c) Naphthenic Acids Fraction Compounds (NAFC) and Naphthenic Acid (NA) Characterization

- describe method for NA activity assessment
- describe OSPW sample preparation
- describe HPLC-Orbitrap mass spectrometry analysis
- describe component separation using HPLC
- describe mobile phase composition
- describe Orbitrap operation
- describe calibration curves and internal standard
- describe peak area ratio calculation
- describe HPLC-Orbitrap analysis results
- describe NAFCs analysis based on peak abundance

### d) Microbial Community Characterization

- describe 16S rRNA gene V4 variable region PCR primers
- describe sequencing and data processing
- describe analysis of whole microbes in OSPW samples

### e) NA-Degrading Strain Isolation and Biodegrading Experiment

- design selection method for NA-degrading bacteria
- isolate microbial populations from OSPW
- perform phylogenetic analysis using ETE3 pipeline
- prepare degradation samples using M9 media and OSPW
- extract and analyze degradation samples using LC-Orbitrap mass spectrometry
- filter OSPW to remove large particulates
- collect and homogenize biomass from filter
- inoculate biomass in M9 media with glucose and extracted NAs
- transfer culture to fresh medium with increasing NAs supplement
- isolate single colonies and identify using 16S rRNA gene sequencing
- analyze biodegradation patterns of isolated strains using HPLC Orbitrap spectrometry

### f) Bioinformatics and Genome Assembly

- select P. putida and P. fluorescens for RNA extraction
- develop systematic approach to investigate key enzymes and pathways
- inoculate tester samples with P. putida, P. fluorescens, and consortium
- isolate total RNA from testers and drivers using ThermoFisher PureLink RNA Mini Kit
- perform Suppression Subtractive Hybridization (SSH) analysis
- generate RNA-seq libraries using Clontech PCR-Select cDNA Subtraction Kit
- sequence libraries using next-generation RNA-Seq platform
- process raw reads using Trimmomatic and digital normalization
- assemble transcriptome using rnaSPAdes and predict open reading frames (ORFs)
- annotate ORFs using MetaPathways pipeline

### g) Differential Gene Expression (DEG) Analysis

- convert gene identities to Entrez Gene ID using Pathway Tools
- functionally cluster DEGs using DAVID Bioinformatics tool
- analyze physiological response of Pseudomonas spp. to NA exposure
- reconstruct general pathways using KEGG mapper tool
- enrich reconstructed pathways using DAVID Bioinformatics tool
- analyze degradation pathways using Pathway Tools software
- identify key enzymes in degradation pathways
- predict pathways using EAWAG-BBD/PPS and Swiss Federal Institute of Aquatic Science and Technology

### h) Upper Pathways Analysis

- analyze transport of NA compounds across cell membrane
- identify outer membrane protein channels and porins
- analyze ABC transporter genes
- identify MFS transporters for NA compounds
- analyze efflux pumps for toxic compound tolerance
- identify secondary multidrug transporters
- analyze carbohydrate efflux transporter
- identify ABC transporter as efflux pumps
- analyze fusaric acid resistance protein
- identify multidrug efflux system
- analyze drug resistance proteins
- identify acriflavin resistance gene

### i) General Pathways Analysis

- utilize KEGG pathway reconstructions
- characterize physiological response of Pseudomonas spp. to NA compounds
- assign DEGs lists to KO numbers
- show purine metabolism pathway enrichment
- suggest modifications of flux through purine nucleotide pathway
- identify nicotinate and nicotinamide metabolism pathway
- upregulate pncB nicotinate phosphoribosyltransferase
- catalyze reaction EC 5.2.1.1 by nicE
- generate maleate when exposed to OSPW
- detect niacin existence in extracted OSPW
- show 2-oxocarboxylic acid metabolism pathway
- compare carbon metabolism global map of FS and PC
- shunt isocitrate to glyoxylate using PSF113_RS41305
- discuss alternative route consuming glyoxylate
- observe reactions in FIGS. 5A-5D for FS
- show more versatile carbon metabolism routes in FS
- identify significantly enriched pathways in aromatic heterocycles metabolism
- complete oxidative phosphorylation map in FS
- compare PS and FS carbon metabolism routes
- discuss limitations of KEGG pathways reconstructions
- use P. putida KT2440 and P. fluorescens F113 PGDBs in Pathway Tools
- reveal NA biodegradation pathways from experimental RNA-seq data
- discuss compounds entering degradation pathway
- propose β-oxidation pathways for commercial NAs
- discuss biodegradation of complex environmental extracts
- prevent β-oxidation and lead to dead-end compounds
- propose alicyclic NA compounds generate cyclohexane carboxylic acid
- discuss Arthrobacter identity in entire microbial community characterization
- predict CHAA conversion into CHCA via α-oxidation pathway
- degrade CHAA further by β oxidation pathway
- propose cyclohexanone oxidation to adipic acid
- discuss omega oxidation pathway for aromatic alkanoic commercial NAs
- identify DEGs in β-oxidation pathways
- analyze RNA-seq data for identification of degradation pathways
- introduce RNAseq libraries preparation
- detail Suppression Subtractive Hybridization steps
- describe cDNA libraries generation
- outline next-generation sequencing process
- introduce in silico genome assembly construction
- detail Trimmomatic processing
- describe digital normalization
- outline transcriptome assembly
- detail MetaPathways pipeline processing
- describe ORF predictions
- outline gene expression browsers generation
- introduce method for identifying genetic elements
- detail reconstructed metabolic pathways generation
- describe enrichment score assignment
- outline functional gene clustering
- introduce method for identifying genetic elements involved in degradation
- detail overlaying gene expression profiles onto pathway-genome database
- describe identifying pathways related to degradation
- outline functional clustering of gene expression profiles
- introduce clustering gene function determination
- detail identified genetic elements in Pseudomonas
- list enzymes for naphthenic degradation in Pseudomonas
- introduce general pathways analysis
- determine gene expression profiles
- identify genes predictive for response to degradation activity
- describe extraction methods
- remove particulate matter from OSPW
- acidify OSPW
- liquid extract OSPW with organic solvent
- evaporate organic solvent and dissolve remaining organic matter
- introduce polynucleotides
- describe enzymes with naphthenic acid degradation activity
- modify nucleic acid to increase NA degradation activity
- classify polynucleotides
- list enzymes encoded by polynucleotides
- introduce vectors
- describe vector expression system
- engineer host cells with vectors
- produce polynucleotides by recombinant techniques
- describe host cells
- introduce engineered microorganisms
- modify microorganisms to increase NA degradation activity
- degrade toxic organic compounds
- introduce gene expression profiling
- generate gene expression profiles
- identify genes involved in degradation activity
- introduce RNA expression analysis
- calculate Reaction Perturbation Score and Pathway Perturbation Score
- identify pathway enzymes and terminal catabolites
- introduce compositions
- describe composition for biodegradation
- introduce biodegradation method
- contact contaminated environment with microbial consortium
- maintain microbial consortium in contact with contaminated environment
- reduce concentration of toxic organic compounds
- provide general information on percentages and ratios
- provide general information on temperatures and dimensions
- provide general information on claims and jurisprudence

