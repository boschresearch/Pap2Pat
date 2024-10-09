# DESCRIPTION

## GOVERNMENT LICENSE RIGHTS

- acknowledge government support

## BACKGROUND

- introduce feedback control in engineering and biology

## SUMMARY

- introduce feedback controller circuits for gene expression
- describe use of bacterial two-component signaling systems
- explain technical challenge of using bifunctional histidine kinases
- describe solution using separate kinase and phosphatase proteins
- detail design of strong phosphatase regulator
- describe incorporation of destabilization domain
- explain negative feedback signal and robustness to perturbations
- provide overview of feedback controller circuit components
- describe input circuit components
- describe tuning circuit components
- describe signal circuit components
- provide variations of phosphatase regulator design
- provide variations of kinase design
- provide variations of activator design
- describe cell state classifier embodiments
- describe applications of feedback controller circuits and cell state classifiers

## DETAILED DESCRIPTION

- introduce feedback controller circuits
- overcome technical challenge of bifunctional histidine kinases
- describe robustness of feedback controller circuit

### Phosphorylation-Based Feedback Controller Circuits

- introduce phosphorylation and kinases
- define feedback controller circuits
- describe input circuit components
- describe tuning circuit components
- describe signal circuit components
- explain phosphorylation-based regulation
- discuss embodiments of nucleotide sequence control
- introduce bacterial two-component systems
- describe phosphorylation-based feedback controller circuits
- introduce histidine kinase in bacterial two-component systems
- describe conserved amino acid sequence motifs
- list non-limiting examples of histidine kinases
- describe kinase and phosphatase activities separation
- describe kinase of input circuit with amino acid substitutions
- describe phosphatase of tuning circuit with amino acid substitutions
- describe EnvZ variants as kinase and phosphatase
- describe kinase and phosphatase with DHp domains
- describe phosphatase with truncated form
- describe phosphatase with mutation in CA domain
- describe phosphatase regulator with multimerization domain
- list non-limiting examples of multimerization domains
- describe GCN4 domain for self-assembly
- describe other multimerization domains
- define phosphatase regulator
- describe leucine zipper domain
- describe destabilization domain
- motivate DHFR destabilization domain
- motivate estrogen receptor destabilization domain
- motivate FKBP destabilization domain
- describe stabilization of destabilization domain
- describe small molecule interaction
- describe dissociation constant
- motivate trimethoprim interaction
- motivate 4-hydroxytamoxifen interaction
- motivate Shield ligand interaction
- describe PEST domain
- define phosphatase regulator
- describe phosphatase regulator structure
- specify phosphatase regulator components
- explain amino acid substitutions
- define identity of biological molecules
- describe activator structure
- specify activator components
- explain fusion proteins
- describe response regulators
- specify response regulator examples
- describe activatable promoter structure
- specify activatable promoter components
- explain response elements
- describe control circuit

### Genetic Elements of Feedback Controller Circuits

- define genetic element
- describe activator
- explain transcriptional regulation
- define activated expression
- provide examples of activators
- describe output molecule
- explain expression of output molecule
- provide examples of output molecules
- describe therapeutic molecule
- explain RNAi molecule
- provide examples of therapeutic molecules
- describe enzymes for operable linking
- provide examples of antibodies and fragments
- describe regulatory proteins and antigens
- define genetic elements of feedback controller circuits
- describe inducible promoters
- motivate inducer signals
- describe N-acyl homoserine lactone (AHL) as an inducer signal
- describe anhydrotetracycline (aTc) as an inducer signal
- describe isopropyl β-D-1-thiogalactopyranoside (IPTG) as an inducer signal
- describe other inducible promoter systems
- describe inducible promoters from prokaryotic cells
- describe nucleic acid molecules and vectors
- describe production of nucleic acids using GIBSON ASSEMBLY Cloning
- describe delivery of genetic circuits to a cell
- describe cells containing the feedback controller circuits
- define a cell
- describe prokaryotic cells
- describe eukaryotic cells
- describe diseased cells

### Cell State Classifiers

- define cell state classifiers
- describe microRNA profile
- motivate cell state classifiers
- describe genetic circuits
- introduce sensor circuits
- describe first sensor circuit
- describe second sensor circuit
- introduce signal circuit
- describe output molecule expression
- summarize applications
- define activatable promoter
- describe genetic elements of cell state classifiers
- define microRNA and microRNA target site
- explain mechanism of gene silencing by microRNAs
- provide information about known microRNAs
- list non-limiting examples of microRNAs
- list microRNA detected
- specify cell state classifier
- describe embodiments
- provide microRNA examples
- detail microRNA identifiers
- list microRNAs
- 
- 
- 

### Feedback Controller Circuit and Cell State Classifier Functionality

- describe delivery of feedback controller circuit
- describe maintaining cell containing feedback controller circuit
- describe cell state classifier detecting microRNAs
- describe logic function of cell state classifier
- describe additional functions of cell state classifiers
- describe detecting output molecule produced by cell state classifier

### Applications

- describe diagnostic purposes of feedback controller circuit or cell state classifier
- describe therapeutic purposes of feedback controller circuit or cell state classifier
- describe maintaining output molecule expression at consistent level
- describe tunable phosphatase regulator activity
- describe composition comprising feedback controller circuit or cell state classifier
- describe additional agents in composition
- describe pharmaceutically acceptable excipient
- describe effective amount of composition
- describe administration frequency
- describe dosage regimen
- describe subject in need thereof
- describe delivery methods
- describe examples of cancers that may be treated

## EXAMPLES

### Example 1: Robust and Tunable Signal Processing in Mammalian Cells Via Engineered Covalent Modification Cycles

- introduce synthetic signaling networks
- describe limitations of natural TCS systems
- engineer covalent modification cycle
- describe EnvZ-OmpR system
- implement negative feedback control
- describe design of circuits
- select HK-RR proteins
- improve kinase and phosphatase design
- tune phosphatase stability
- describe tunable input-output circuit
- tune kinase activity
- tune phosphatase activity
- modulate translation of phosphatase regulator
- modulate phosphatase regulator stability
- implement tunable feedback controller
- test robustness to perturbations
- test off-target regulation
- test resource competition
- analyze variability of output expression
- conclude robustness of feedback controllers

## CONCLUSIONS

- summarize applications of phosphorylation-based feedback controllers

## Modular Plasmid Cloning Scheme

- construct plasmids using Golden Gate strategy
- create basic parts (Level 0s) via standard cloning techniques
- assemble Level 0s into transcription units (Level 1s) and multi-TU plasmids (Level 2s)

### Cell Culture

- maintain cell lines in Dulbecco's modified Eagle media

### Transfections

- perform transfections using Lipofectamine 3000, PEI MAX, FuGENE6, or Viafect

### Luciferase Assays and Analysis

- measure RR-driven luminescence output using Promega Nano-Glo Dual-Luciferase Reporter Assay System

### Identification of Optimal Orthogonal TCS Pairs

- use MATLAB script to score combinations of HK—RR protein pairs

### Flow Cytometry

- prepare samples for flow cytometry
- collect samples on a BD LSR Fortessa
- analyze flow cytometry data using a MATLAB-based pipeline
- perform multi-dimensional binning of poly-transfection data
- calculate accuracy of cell classification

### Calculation of Fold-Changes and Robustness Scores

- calculate fold-changes and robustness scores from output levels

### Quantification of Cell-to-Cell Output Variance

- measure noise using interquartile range of output distributions

### Model Fitting

- fit models to data using MATLAB function ‘lsqcurvefit( )’
- compute goodness of fit using normalized root-mean-square error CV(RMSE)

### OTHER EMBODIMENTS

- describe alternative features and embodiments of the invention

### EQUIVALENTS

- describe equivalents to the specific inventive embodiments
- define terms and phrases used in the specification and claims
- incorporate references, patents, and patent applications by reference
- interpret the phrase “and/or” and other phrases
- describe the meaning of “at least one” and other phrases

