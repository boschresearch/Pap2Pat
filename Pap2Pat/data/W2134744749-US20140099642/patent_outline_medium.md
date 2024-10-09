# DESCRIPTION

## TECHNICAL FIELD

- introduce noninvasive fetal genetic abnormality detection

## BACKGROUND ART

- motivate noninvasive prenatal diagnosis
- describe limitations of conventional methods
- summarize recent studies on noninvasive detection
- highlight need for improved methods

## SUMMARY OF THE INVENTION

- introduce method for noninvasive detection of fetal genetic abnormalities
- describe removal of GC bias from sequencing results
- establish relationship between coverage depth and GC content
- calculate coverage depth and GC content of chromosomes
- determine relationship between coverage depth and GC content
- calculate fitted coverage depth
- calculate standard variation
- calculate student t-statistic
- determine fetal genetic abnormality
- determine fetal gender
- estimate fetal fraction
- compare fitted coverage depth to coverage depth

## DETAILED DESCRIPTION OF THE INVENTION

- introduce noninvasive detection of fetal genetic abnormalities by large-scale sequencing of polynucleotide fragments from a maternal biological sample

### I. DEFINITIONS

- define chromosomal abnormality
- define reference unique reads
- define polynucleotide, oligonucleotide, nucleic acid, and nucleic acid molecule
- define massively parallel sequencing
- define biological sample
- define consisting and consisting essentially of aspects and embodiments
- provide examples of chromosomal abnormalities
- provide examples of biological samples
- provide examples of sequencing methods

### II. ESTABLISHING A RELATIONSHIP BETWEEN COVERAGE DEPTH AND GC CONTENT

- obtain sequence information of multiple polynucleotide fragments
- assign fragments to chromosomes based on sequence information
- calculate coverage depth and GC content of a chromosome
- determine the relationship between coverage depth and GC content
- normalize coverage depth based on another chromosome location

### III. DETERMINING A FETAL GENETIC ABNORMALITY

- calculate fitted coverage depth using GC content and established relationship
- compare fitted coverage depth to coverage depth to determine fetal genetic abnormality

### IV. COMPUTER READABLE MEDIUM AND SYSTEM FOR DIAGNOSIS OF A FETAL GENETIC ABNORMALITY

- provide computer readable medium with instructions for prenatal diagnosis
- provide system for determining fetal aneuploidy

### V. EXAMPLES

- illustrate GC-bias and gender effects on sensitivity of detection
- analyze factors affecting sensitivity of detection
- investigate GC content effects on coverage depth
- develop statistical model for coverage depth and GC content
- estimate fetal fraction using coverage depth of chromosomes X and Y
- calculate residual of every chromosome
- validate student-t calculation using Q-Q plot
- distinguish fetal gender using coverage depth of chromosome Y
- predict gender using logistic regression for gender dubious cases
- evaluate diagnostic performance of GC-correlation t-test approach
- introduce study participants
- describe maternal plasma DNA sequencing
- outline DNA library construction
- detail sequencing library preparation
- introduce GC-correlation t-test approach
- apply approach to detect trisomy 13, 18, and 21
- apply approach to detect XO, XXX, XXY, and XYY
- compare approach to other methods
- evaluate approach for sex-chromosome abnormalities
- discuss theoretical performance of GC-correlation t-test approach
- investigate relationship between fetal DNA fraction and gestational age
- evaluate fetal fraction estimation method
- discuss influence of sequencing depth on standard variation
- estimate required sequencing depth for aneuploidy detection
- propose strategy for detecting aneuploidy with low fetal DNA fraction
- calculate theoretical sensitivity of GC-correlation student t approach

