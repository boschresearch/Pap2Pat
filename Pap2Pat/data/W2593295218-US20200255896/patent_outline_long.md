# DESCRIPTION

## TECHNICAL FIELD

- introduce non-invasive prenatal screening

## BACKGROUND

- limitations of current NIPS methods

## SUMMARY OF THE INVENTION

- detect false-positive diagnosis of chromosomal aneuploidy
- divide chromosome into bins
- obtain bin-specific test parameter
- plot ideogram of chromosome
- detect false-positive diagnosis
- repeat steps for confirming chromosome
- calculate substantial portion of chromosome
- obtain bin-specific parameter
- calculate chromosome representation value
- compare to references
- detect false-positive diagnosis
- improve positive predictive value

## DETAILED DESCRIPTION

- define karyotype
- describe normal human karyotypes
- define ploidy
- describe haploid and diploid organisms
- define aneuploidy
- describe causes of aneuploidy
- define trisomy
- define monosomy
- define mosaicism
- define fetal aneuploidy
- describe non-invasive prenatal testing (NIPT)
- describe invasive prenatal examination
- define chromosomal duplication
- define chromosomal deletion
- describe origins of chromosomal duplication or deletion
- define gene
- describe RNA or polypeptide production
- define chromosome variation
- describe copy number variation
- describe microduplication and microdeletion
- define cell-free DNA (cfDNA)
- describe cell-free fetal DNA (cffDNA)
- define fetal fraction (ff)
- describe next generation sequencing (NGS)
- define library
- describe adapter sequence
- define sequencing bin
- describe sequence read
- define reference genome
- describe Z-score
- define ideogram
- describe mapping of characteristic DNA sequences
- define positive predictive value (PPV)
- describe risks of invasive procedures
- introduce non-invasive prenatal screening methods
- describe maternal test sample
- describe cell-free fetal DNA in maternal test sample
- describe evaluation of fetal fraction
- exclude samples with low fetal fraction
- describe methods for quantifying cell-free fetal DNA
- describe establishing fetal fraction using NGS data
- estimate fetal fraction for male-bearing pregnancies
- estimate fetal fraction for female-bearing pregnancies
- describe regularized regression model
- describe estimation of fetal fraction using multiple methods
- analyze cell-free DNA for detection of fetal aneuploidy
- describe high-risk pregnancies
- sequence cell-free DNA with next generation sequencing
- describe alignment of sequence reads to bins of a reference genome
- describe bin read count scaling
- correct high order artifacts
- calculate bin-specific test parameter
- determine relative abundance of genetic materials
- calculate chromosomal representation
- compare chromosomal representation to reference
- calculate chromosome-specific Z-score
- interpret Z-score for aneuploidy detection
- attribute abnormalities to fetal genome
- use Z-score for detecting aneuploidy
- detect chromosomal trisomy or monosomy
- detect partial chromosomal duplication or deletion
- detect chromosomal mosaicism
- detect chromosome translocations
- provide effective option for detecting fetal aneuploidies
- improve positive predictive values
- consider maternal chromosome variations
- distinguish fetal aneuploidies from maternal variations
- examine fetal genome karyotype
- calculate chromosome-specific Z-score for multiple chromosomes
- recognize maternal contribution and exclude false-positives
- pinpoint source of genetic variations to discrete chromosomal region
- define bin-specific test parameter
- calculate bin-specific test parameter
- determine consistency of bin-specific test parameters
- detect maternal microduplication or microdeletion
- define large-scale difference
- detect fetal aneuploidy
- confirm fetal aneuploidy
- exclude false-positive diagnosis
- calculate chromosome-specific Z-score
- analyze ideogram for consistency
- determine substantial portion of chromosome
- calculate standard deviation of residues
- improve positive predictive value of NIPS
- perform ultra-sonographic diagnosis
- perform amniocentesis
- perform conventional first or second trimester screenings
- use next-generation sequencing methods
- use shotgun massively parallel sequencing
- use sequencing-by-synthesis with reversible dye terminators
- use sequencing-by-ligation
- use single molecule sequencing
- describe Ion Torrent sequencing system
- describe 454 sequencing system
- describe reversible dye-terminators sequencing
- describe Helicos single-molecule sequencing
- describe sequencing by synthesis
- describe MiSeq personal sequencing system
- describe sequencing by ligation
- describe SOLiD sequencing
- describe SMRT sequencing
- correct GC-sequencing biases
- provide example of correcting GC-sequencing biases
- describe use of various sequencing methods
- describe use of various sequencing technologies
- describe use of various sequencing platforms
- summarize methods for improving positive predictive value of NIPS

## EXAMPLES

### Example 1: Assay Development

- introduce patient sample collection
- describe sample collection process
- outline sample sources
- detail informed consent process
- introduce next-generation sequencing
- describe blood collection and processing
- outline plasma isolation and centrifugation
- detail cell-free DNA extraction
- describe library preparation and PCR
- outline PCR conditions and primer sequences
- detail PCR product purification and quantification
- introduce sequencing and library pooling
- describe sequencing conditions and data analysis
- introduce fetal fraction estimations
- describe X chromosome underrepresentation method
- outline Y chromosome overrepresentation method
- detail regularized regression model for female fetuses
- introduce GC correction
- describe GC content calculation and discretization
- outline local polynomial regression and loess function

### Example 2: Assay Verification and Validation

- introduce assay verification and validation
- describe verification sample set and results
- outline validation sample set and results
- detail effects of GC correction on performance
- describe analysis of twin gestation samples
- outline final validation for trisomy detection and fetal sex determination

### Example 3: Clinical Implementations

- describe clinical implementations of NIPS assay
- specify sample acceptance criteria
- report Z-score cutoffs for clinical implementation
- present results of first 10,000 clinical samples
- summarize abnormal NIPS results
- explain causes of unreported results
- introduce maternal microduplication issue
- describe method to identify maternal microduplications
- present results of maternal microduplication identification
- explain process of confirming suspected microduplications
- report PPV improvement after identifying maternal microduplications
- describe case of intermediate Z-scores
- use chromosomal ideograms to investigate intermediate Z-scores
- confirm maternal microduplications using microarray analysis
- report NPV for Trisomies 21, 13, and 18
- introduce maternal global copy number abnormalities issue
- describe method to identify maternal global copy number abnormalities
- present results of maternal global copy number abnormalities identification
- report cases of mosaicism and translocations
- describe detection of mosaic Down syndrome
- report analytical sensitivity of NIPS assay for mosaic Down syndrome
- introduce sex chromosome aneuploidies issue
- describe detection of fetal sex chromosome aneuploidy
- report cases of twins with elevated Z-scores
- describe results of twin pregnancy cases
- introduce PPV of previously available NIPS methods
- report PPV of previously available NIPS methods
- introduce PPV of present NIPS method
- report PPV of present NIPS method for Trisomies 21, 18, and 13
- report PPV of present NIPS method for sex chromosome aneuploidies and microdeletions

## EQUIVALENTS

- disclaim limitations
- define functionally equivalent
- interpret Markush groups
- define range boundaries
- incorporate prior art

