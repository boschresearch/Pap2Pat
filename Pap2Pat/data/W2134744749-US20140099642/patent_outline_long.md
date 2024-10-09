# DESCRIPTION

## TECHNICAL FIELD

- introduce noninvasive fetal genetic abnormality detection

## BACKGROUND ART

- motivate noninvasive prenatal diagnosis
- describe limitations of conventional methods
- introduce noninvasive detection of fetal aneuploidy
- describe detection of fetal DNA in maternal plasma
- discuss limitations of circulating fetal DNA
- introduce GC bias in sequencing data
- describe methods to remove GC bias
- motivate need for improved method

## SUMMARY OF THE INVENTION

- introduce method for noninvasive detection of fetal genetic abnormalities
- describe removal of GC bias from sequencing results
- establish relationship between coverage depth and GC content
- obtain sequence information of polynucleotide fragments
- assign fragments to chromosomes
- calculate coverage depth and GC content
- determine relationship between coverage depth and GC content
- calculate fitted coverage depth
- calculate standard variation
- calculate student t-statistic
- describe GC content calculation
- describe use of multiple samples
- describe use of pregnant female subjects
- describe use of biological samples
- introduce method to determine fetal genetic abnormality
- obtain sequence information of polynucleotide fragments
- assign fragments to chromosomes
- calculate coverage depth and GC content
- calculate fitted coverage depth
- compare fitted coverage depth to coverage depth
- determine fetal gender
- estimate fetal fraction
- describe calculation of fetal fraction
- describe statistical hypothesis test
- introduce computer readable medium and system for determining fetal genetic abnormality

## DETAILED DESCRIPTION OF THE INVENTION

- introduce noninvasive detection of fetal genetic abnormalities
- describe method to remove GC bias from sequencing results

### I. DEFINITIONS

- define technical and scientific terms
- specify singular forms include plural references
- define chromosomal abnormality
- define reference unique reads
- define polynucleotide, oligonucleotide, nucleic acid, and nucleic acid molecule
- describe massively parallel sequencing
- define biological sample
- describe aspects and embodiments of the invention
- define monosomy X
- define XXY syndrome
- define XYY syndrome
- describe trisomy 13, trisomy 18, and trisomy 21
- define Turner syndrome
- define Klinefelter syndrome
- describe detection of fetal chromosomal aberration
- define terms related to nucleic acid molecules
- describe types of modifications to nucleic acid molecules
- describe other types of nucleic acid molecules

### II. ESTABLISHING A RELATIONSHIP BETWEEN COVERAGE DEPTH AND GC CONTENT

- obtain sequence information of multiple polynucleotide fragments
- assign fragments to chromosomes based on sequence information
- calculate coverage depth and GC content of a chromosome
- determine the relationship between coverage depth and GC content
- describe calculation of coverage depth
- describe normalization of coverage depth
- calculate relative coverage depth
- describe calculation of GC content
- establish a relationship between coverage depth and GC content
- use Loess algorithm to assess non-linear relationships
- describe use of multiple samples to establish a relationship

### III. DETERMINING A FETAL GENETIC ABNORMALITY

- obtain sequence information of multiple polynucleotide fragments
- assign fragments to chromosomes based on sequence information
- calculate coverage depth and GC content of a chromosome
- compare fitted coverage depth to coverage depth of a chromosome
- determine fetal genetic abnormality based on comparison

### IV. COMPUTER READABLE MEDIUM AND SYSTEM FOR DIAGNOSIS OF A FETAL GENETIC ABNORMALITY

- receive sequence information
- assign polynucleotide fragments to chromosomes
- calculate coverage depth and GC content of a chromosome
- compare fitted coverage depth to coverage depth of a chromosome

### V. EXAMPLES

- introduce example 1
- analyze factors affecting sensitivity of detection
- describe procedural framework for calculating coverage depth and GC content
- illustrate correlation between coverage depth and GC content
- explain influence of GC content on coverage depth
- describe composition of GC content in different chromosomes
- analyze influence of fetal gender on data
- introduce example 2
- describe statistical model for coverage depth and GC content
- apply loess algorithm to fit coverage depth with GC content
- calculate fitted coverage depth and standard variance
- introduce example 3
- estimate fetal fraction based on coverage depth of chromosome X and Y
- describe formulas for estimating fetal fraction
- introduce example 4
- calculate residual of every chromosome
- analyze standard variation of every chromosome
- introduce example 5
- distinguish fetal gender based on coverage depth of chromosome Y
- describe logistic regression for predicting gender
- introduce example cases
- describe maternal plasma DNA sequencing
- outline DNA library construction
- detail sequencing library preparation
- explain sequencing data analysis
- introduce GC-correlation t-test approach
- describe detection of trisomy 13, 18, and 21
- detail detection of XO, XXX, XXY, and XYY
- compare GC-correlation t-test approach to other methods
- evaluate performance of GC-correlation t-test approach
- introduce example 8
- describe detection of XO, XXX, XXY, and XYY
- detail detection results for XO, XXX, XXY, and XYY
- introduce example 9
- discuss theoretical performance of GC-correlation t-test approach
- analyze relationship between fetal DNA fraction and gestational age
- evaluate effect of sequencing depth on standard variation
- determine required sequencing depth for aneuploidy detection
- propose strategy for detecting aneuploidy with low fetal DNA fraction
- estimate theoretical sensitivity of GC-correlation t-test approach
- calculate theoretical sensitivity considering gestational age and sequencing depth
- discuss limitations of theoretical sensitivity estimation
- detail calculation of false negative rate
- compute theoretical sensitivity in each gestational age
- show resulting plots of theoretical sensitivity calculation
- discuss application of GC-correlation t-test approach
- summarize advantages of GC-correlation t-test approach
- compare GC-correlation t-test approach to other methods
- discuss limitations of GC-correlation t-test approach
- propose future directions for GC-correlation t-test approach
- conclude example 9
- finalize example section

