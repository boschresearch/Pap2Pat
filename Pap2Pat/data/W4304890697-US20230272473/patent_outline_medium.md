# DESCRIPTION

## BACKGROUND

- introduce birth defects
- statistics of birth defects in China
- genetic factors of birth defects
- chromosomal abnormalities
- limitations of traditional screening methods
- advantages of non-invasive prenatal screening (NIPS)
- discovery of fetal cell-free DNA (cfDNA)
- development of NIPS technology
- limitations of whole genome sequencing (WGS) method
- advantages of single nucleotide polymorphism (SNP) method

### SUMMARY

- introduce method of analyzing nucleic acid molecules
- capture target nucleic acid molecule using capture probe
- analyze captured target nucleic acid molecule
- optional: isolate nucleic acid molecules from biological sample
- optional: amplify nucleic acid molecules
- determine pairing kinetics of capture probe
- optional: specify length and GC content of capture probe
- optional: specify target region in reference genome
- optional: specify configuration of capture probe
- analyze captured target nucleic acid molecule by sequencing
- optional: determine chromosomal abnormality in fetus
- design capture probe for target region
- provide capture probe with specific sequence
- analyze fetal-derived nucleic acids for chromosomal aneuploidy
- define chromosomal aneuploidy detection method
- introduce likelihood equations for aneuploidy detection
- describe method of analyzing fetal-derived nucleic acids
- determine likelihood of chromosomal microdeletion or microduplication
- introduce beta-binomial distribution for likelihood calculation
- describe method of determining fetal genotype in different euploid and aneuploid states
- introduce threshold range for karyotype determination
- describe method of analyzing fetal-derived nucleic acids for dominant monogenic variation
- determine likelihood of paternally inherited or de novo fetal mutation
- describe method of determining fetal fraction
- introduce capture probe for target region sequencing
- describe computer system and non-transitory computer-readable storage medium for method implementation
- provide system overview for chromosomal aneuploidy detection

## DETAILED DESCRIPTION

- relate to nucleic acid molecule analysis
- introduce non-invasive prenatal detection
- describe COATE method
- define capture probe
- explain pairing kinetics
- determine melting temperature
- specify capture probe length
- specify capture probe GC content
- apply method to target nucleic acid molecules
- capture multiple target nucleic acid molecules
- describe capture probe design
- provide capture probe sequences
- describe composition of capture probes
- analyze fetal-derived nucleic acids
- detect chromosomal aneuploidy
- determine chromosomal aneuploidy with one parental meiotic recombination
- determine chromosomal aneuploidy with two or more parental meiotic recombinations
- provide equations for determining chromosomal aneuploidy
- define likelihood equations
- specify parameters for likelihood equations
- determine chromosomal aneuploidy with two parental meiotic recombinations
- determine chromosomal aneuploidy with three parental meiotic recombinations
- determine chromosomal aneuploidy with four parental meiotic recombinations
- generalize method for any number of parental meiotic recombinations
- describe advantages of method
- outline method for detecting chromosomal microdeletion and/or microduplication
- specify likelihood equations for chromosomal microdeletion and/or microduplication
- describe method for detecting dominant monogenic variation
- specify likelihood equation for dominant monogenic variation
- describe method for determining fetal fraction
- specify equation for determining fetal fraction
- introduce non-invasive prenatal screening
- determine α based on systemic noise of sequencing procedure
- capture nucleic acid molecules using capture probe
- sequence captured nucleic acid molecules
- analyze sequence reads for chromosomal aneuploidy detection
- apply statistical methods to integrate multiple metrics
- describe whole genome low-depth random sequencing method
- describe high-depth targeted sequencing method
- introduce COATE technology for target capture probe design
- calculate difference in hybridization annealing temperature
- design probes for chromosome aneuploidy and monogenic target regions
- describe liquid-phase hybridization technique
- discuss advantages of COATE method over multiplex PCR technique
- introduce product for non-invasive detection of chromosomal aneuploidy and microdeletion/microduplication diseases
- describe product for non-invasive detection using SNP-based hybridization capture method
- introduce detection method for non-invasive prenatal screening of fetuses
- describe method of designing targeted capture probe
- introduce detection kit for non-invasive prenatal screening of fetuses
- describe device for non-invasive prenatal screening of fetuses
- introduce computer-readable storage medium for non-invasive prenatal screening of fetuses
- describe system for non-invasive prenatal screening of fetuses
- introduce targeted capture probe for non-invasive prenatal screening of fetuses
- outline operations for detection method for non-invasive prenatal screening of fetuses
- define calculation of fetal chromosome copy number variation
- derive equation for distribution difference
- explain detection threshold
- introduce detection method for chromosome microdeletion/microduplication
- derive equation for microdeletion/microduplication
- explain detection method for dominant monogenic variation
- derive equation for dominant monogenic variation
- describe combination of calculations
- explain use of targeted capture probe
- describe calculation of fetal fraction
- explain selection of SNP sites
- describe equations for chromosomal SNP sites
- discuss limitations of detection method
- summarize embodiments of detection method
- define equations for chromosomal aneuploidy detection
- introduce detection method for non-invasive prenatal screening
- describe targeted capture probe design
- specify SNP site selection criteria
- provide URLs of public databases used
- outline method for designing targeted capture probe
- calculate annealing temperatures for probe binding
- describe probe design and selection process
- specify probe length and design parameters
- outline detection method for chromosome copy number variation
- calculate fetal fraction and detect SNP sites
- calculate probability of normal or abnormal chromosome copy number
- interpret karyotype of fetus
- calculate karyotype probabilities at each SNP site
- calculate fetal chromosome copy number variation
- define detection method
- calculate fetal chromosome microdeletion/microduplication
- calculate dominant monogenic variation
- describe log function
- outline multiple embodiments of detection method
- describe calculation of fetal fraction
- outline multiple embodiments of calculation of fetal fraction
- describe selection of SNP site
- outline multiple embodiments of detection method
- describe equations for sum of probabilities
- outline multiple embodiments of targeted capture probe
- describe selection of genes for targeted capture probe
- describe selection of SNP sites based on human genome sequence
- describe use of public databases
- describe method of designing targeted capture probe
- define detection method
- describe targeted capture probe
- calculate annealing temperature
- design probes for SNP site
- calculate ΔTm values
- select optimal probe
- describe probe length
- describe method of designing targeted capture probe
- describe detection kit
- describe device for non-invasive prenatal screening
- describe computer-readable storage medium
- describe system for non-invasive prenatal screening
- calculate probability of normal/abnormal chromosome copy number
- calculate karyotype probabilities
- calculate fetal chromosome copy number variation
- define mathematical equations for chromosomal aneuploidy detection
- describe calculation of fetal chromosome microdeletion/microduplication
- derive equation for dominant monogenic variation
- calculate fetal fraction of cell-free nucleic acids
- describe system for non-invasive prenatal screening of fetuses
- calculate sum of probabilities at chromosomal SNP sites
- describe system for non-invasive prenatal screening of fetuses with chromosomal recombination
- describe targeted capture probe for SNP sites
- describe targeted capture probe for gene mutations
- describe length of targeted capture probe
- provide use of targeted capture probe for non-invasive prenatal screening
- describe method for non-invasive prenatal screening of fetuses
- define percent sequence identity
- describe algorithms for determining percent sequence identity
- describe hybridization conditions
- describe stringency degree of hybridization conditions
- provide examples of hybridization conditions

### Computer System

- introduce computer system
- describe subsystems
- explain system bus
- list peripherals and I/O devices
- describe data collection device
- illustrate computer system 1101
- describe CPU 1105
- explain memory 1110
- describe electronic storage unit 1115
- explain communication interface 1120
- describe peripheral devices 1125
- illustrate network 1130
- explain CPU 1105 execution
- describe storage unit 1115
- explain machine-executable code
- describe user interface 1140

### Other Embodiments

- provide disclaimer
- describe variations and substitutions

## EXAMPLES

- illustrate various embodiments of the invention

### Example 1: Capture of DNA with the Target Probe

- separate plasma and extract cell-free DNA
- construct sequencing library
- enrich, hybridize, elute, amplify, and purify library
- perform quality inspection of library
- enrich target region
- perform PCR amplification
- purify library
- perform quality inspection of library
- elute captured DNA library
- perform PCR amplification
- purify library
- perform quality inspection of library
- analyze results

### Example 2: Sequencing

- perform sequencing using MGI high-throughput sequencing platform
- analyze sequencing data

### Example 3: The Coordinative Allele-Aware Target Enrichment Improves Capture Homogeneity of Alleles in Target Region

- design capture probe using COATE method
- compare capture homogeneity of alleles using COATE and traditional methods
- analyze results

### Example 4: Determination of the Negative Threshold of Trisomy 21 Syndrome

- extract free nucleic acid
- calculate fetal fraction
- select SNP sites
- calculate probability of chromosomal aneuploidy
- calculate chromosome copy number variation
- determine negative threshold

### Example 5: Determination of the Positive Threshold of Trisomy 21 Syndrome

- mix reference samples

### Example 6: Detection of Trisomy 21 Syndrome in Maternal Plasma

- analyze maternal plasma samples

### Example 7: Detection of Trisomy in which Homologous Chromosome Recombination has Occurred

- calculate likelihood value of fetal trisomy
- consider mixing mode of L(MI/MII)
- analyze samples having chromosome abnormality

### Example 8: Detection of Chromosome Microdeletion (Example of DiGeorge)

- analyze chromosome microdeletion-positive reference cell line

### Example 9: Detection of Dominant Monogenic Variation (FGFR3:.pG380R)

- mix fetal and maternal DNAs
- calculate probability of paternal or de novo mutations
- determine system error rate
- detect single gene mutation

