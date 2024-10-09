# DESCRIPTION

## BACKGROUND

- introduce chromosomal translocations
- describe Philadelphia chromosome
- discuss CML and its characteristics
- explain BCR-ABL1 fusion protein
- describe current methods for CML diagnosis
- discuss limitations of current methods
- highlight need for new methods
- mention genetic heterogeneity in CML
- summarize need for DNA-based biomarkers

## SUMMARY OF THE INVENTION

- introduce Anchored ChromPET method
- describe method for detecting structural variations
- explain capture of targeted region
- describe ChromPET sequencing
- discuss bar coding for multiplexing
- highlight high resolution of breakpoint identification
- describe production of patient-specific DNA biomarker
- discuss stability of DNA relative to RNA
- introduce method for detecting and monitoring structural variations
- describe method for identifying biomarkers
- explain algorithm for breakpoint prediction
- describe design of PCR primers
- discuss use of ChromPET technology
- highlight identification of chromosomal disruptions
- describe use of ChromPET in animals and microorganisms
- introduce parallel bioinformatics approach
- describe use of multiple independent paired-end tags
- explain calculation of tag density
- discuss identification of regions dense in abnormal tags
- describe method for monitoring disease progression
- highlight use of biomarkers for diagnostic purposes
- discuss use of biomarkers for prognostic purposes
- introduce kit for identifying and monitoring chromosomal structural variations
- describe components of the kit
- summarize invention

## DETAILED DESCRIPTION OF THE INVENTION

### Abbreviations and Acronyms

- list abbreviations and acronyms

## DEFINITIONS

- define terminology
- introduce articles "a" and "an"
- define "about"
- define "adjacent"
- define "alleviated"
- define "alterations in peptide structure"
- define "amino acids"
- introduce amino acid representation
- define "amplification"
- define "analog"
- define "analyte"
- define "anchor"
- define "Anchored ChromPET"
- define "antibody"
- define "synthetic antibody"
- define "antiparallel fashion"
- define "antisense oligonucleotide"
- define "antisense"
- define "basic or positively charged amino acid"
- define "biocompatible"
- define "biologically active fragments"
- define "biomolecule"
- define "cell, cell line, and cell culture"
- define "complementary"
- define "compound"
- define "conservative amino acid substitution"
- define "control"
- define "test"
- define "pathoindicative"
- define "normally comprises"
- define "detect"
- define "detectable marker"
- define "disease"
- define "disorder"
- define terms used in the specification and appended claims
- introduce examples of terms
- define "fragment" or "segment"
- define "functional" biological molecule
- define "genomic DNA"
- define "homologous"
- define "hybridization"
- describe determination of percent identity
- define "instructional material"
- define "isolated nucleic acid"
- define "junctional ChromPET"
- define "ligand"
- describe specific binding
- define "linkage" and "linker"
- define "mass tag"
- define "method of identifying peptides in a sample"
- define "nucleic acid"
- define "oligonucleotide"
- define "otherwise identical sample"
- describe arrangement of nucleic acid regions
- define "peptide"
- describe peptide mimetics
- define "peptide mass labeling"
- define "pharmaceutically acceptable carrier"
- define "polylinker"
- define "polynucleotide"
- define "polypeptide"
- define "protein"
- define "protecting group"
- describe protecting groups for terminal amino and carboxy groups
- define "purified"
- define "recombinant polynucleotide"
- define "recombinant polypeptide"
- define "sample"
- define "secondary antibody"
- define "solid support"
- define "specifically binds"
- define "standard"
- define "structural variation in a chromosome"
- define "subject"
- define "substantially homologous amino acid sequences"
- define "substantially homologous nucleic acid sequence"
- describe nucleic acid hybridization conditions
- describe computer algorithms for determining substantial similarity
- define "substantially pure"
- describe methods for determining purity
- describe methods useful for carrying out the invention
- conclude definitions

## EMBODIMENTS

- introduce chromosomal translocations
- motivate paired end mapping techniques
- describe basic principle of paired-end-tag sequences
- explain mapping paired-end-tag sequences to genome
- identify aberrant ChromPETs
- generate PCR primers for junctional fragments
- introduce yeast genome analysis
- describe ChromPET technique in Saccharomyces cerevisiae
- motivate global approach for identifying chromosomal structural variation
- describe system for selecting gross chromosomal rearrangements
- summarize bioinformatic analysis procedure
- extract flanking sequences and identify unique ChromPETs
- map ChromPETs to yeast genome
- identify and characterize aberrant ChromPETs
- generate aberrant ChromPET profile
- exclude chimera products
- analyze chromosomal translocations
- address short length of tags and repeat sequences
- require multiple independent paired-end tags
- calculate distribution of ChromPET tags
- determine density of abnormal tags
- flag regions dense in abnormal tags
- lower cutoffs to obtain list of windows
- tabulate partner windows
- consider abnormal linkages
- relax threshold for selecting candidates
- apply new cutoff
- analyze aberrant ChromPETs for insertions
- analyze aberrant ChromPETs for deletions
- detect translocation in chromosome V reporter region
- detect HIS3 insertion in XRS2 coding region
- detect Ty element insertions
- confirm Ty element insertions using PCR
- analyze ChromPETs for identifying chromosomal translocations
- modify ChromPET to search for translocation junctions
- select area of interest for anchoring ChromPETs
- use array CGH to select area of interest
- purify area of interest by PCR
- convert area of interest into bait
- eliminate repetitive DNA
- hybridize bait to test genomic DNA
- purify double-stranded DNA
- convert purified DNA to double-stranded DNA
- use nanochip to select specific segments of genome
- elute trapped DNA from nanochip
- ligate selected DNA to sequencing adaptors
- subject DNA to paired-end sequencing
- analyze ChromPETs to identify aberrant links
- design PCR primers based on aberrant links
- amplify junctional fragment from test DNA
- compare results to identify biomarkers
- diagnose disease or disorder associated with biomarker
- provide kits for identification and diagnosis
- design primers specific to cancer
- use method for personalized medicine
- identify diseases and disorders with chromosomal structural variations
- provide numerical ranges for method
- provide kit for analyzing DNA according to method

## EXAMPLES

### Reagents

- list reagents used
- specify APex Heat-Labile Alkaline Phosphatase
- specify Biotin-16-UTP
- specify DNAZo1 reagent
- specify Dynabeads M-280 streptavidin
- specify End-It DNA end repair kit
- specify human Cot-1 DNA
- specify MAXlscript Kit
- specify MinElute Reaction Cleanup Kit
- specify pCR4-TOPO-TA vector
- specify QIAquick Gel Extraction Kit
- specify QIAquick PCR purification kit
- specify QuickExtract FFPE DNA Extraction Kit
- specify QuickExtract FFPE RNA Extraction Kit
- specify Quick Ligation Kit
- specify SuperScript III Reverse Transcriptase
- specify TaKaRa Ex Taq DNA Polymerase
- specify Taq DNA polymerase
- specify TRIzol
- specify TURBO DNase
- describe cell lines
- describe patient samples

### Table 1 (Comprising Tables 1A and 1B). Number of ChromPETs Sequenced, Mapped, Anchored to BCR and Junctional for Each Sample (A) Cell Lines and (B) Patient Samples

- present table 1A
- present table 1B
- describe table 2
- motivate prediction and validation of translocation breakpoints
- predict breakpoints in K562 cells
- validate breakpoints in K562 cells
- predict breakpoints in KU812 cells
- validate breakpoints in KU812 cells
- identify ABL1-BCR reciprocal translocation in KU812 cells
- predict breakpoints in patient samples
- validate breakpoints in patient samples
- design primer sets
- amplify junctional fragments
- confirm BCR-ABL1 and ABL1-BCR translocations
- discuss contamination in patient-3
- compare sensitivity of DNA and RNA biomarkers
- evaluate sensitivity of detection of DNA-based biomarkers
- evaluate sensitivity of detection of RNA-based biomarkers
- discuss advantages of Anchored ChromPET
- compare Anchored ChromPET with karyotyping
- compare Anchored ChromPET with RT-PCR
- discuss resolution of Anchored ChromPET
- discuss sensitivity of Anchored ChromPET
- discuss application of Anchored ChromPET
- discuss use of Anchored ChromPET in diagnosis and management of CML
- propose alternative strategy for Anchored ChromPET
- discuss advantages of Anchored ChromPET in solid cancers
- discuss potential of Anchored ChromPET for detecting minimal residual disease
- discuss potential of Anchored ChromPET for detecting early recurrence
- discuss computational prediction of breakpoint
- present table 2
- discuss results of computational prediction
- discuss other methods for sequencing DNA translocation junction
- discuss RNA bait preparation
- discuss translocation junctions
- analyze ends of chromosomes after break
- discuss DNA structure around BCR breakpoints

## CONCLUSIONS

- motivate BCR-ABL1 fusion gene detection
- describe advantages of paired-end sequencing
- summarize anchored chromosomal paired-end tags approach

