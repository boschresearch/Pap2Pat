# DESCRIPTION

## FEDERAL FUNDING ACKNOWLEDGEMENT

- acknowledge government funding

## FIELD OF THE INVENTION

- relate to genomic DNA methylation loss measurement

## BACKGROUND

- introduce DNA methylation loss
- describe genomic studies on hypomethylation
- discuss conflicting evidence on PMD hypomethylation
- summarize previous studies on PMD hypomethylation
- highlight need for new methods

## SUMMARY OF THE INVENTION

- provide WGBS experiments
- identify local sequence signature
- determine PMD hypomethylation
- investigate dynamics of hypomethylation
- define relationship between PMDs and chromatin features
- derive mitotic age for each tissue type
- map tissue/cell-type variation
- profile primary tumors and adjacent tissues
- analyze WGBS datasets
- identify Solo-WCGW motif
- reveal PMD hypomethylation in healthy tissues
- show increase in PMD hypomethylation with age
- track accumulation of cell divisions
- correlate PMD hypomethylation with somatic mutation density
- correlate PMD hypomethylation with cell-cycle gene expression
- reflect mitotic history
- contribute to oncogenesis
- identify test cell or tissue sample
- obtain CpG dinucleotide sequence methylation data
- determine mean CpG dinucleotide methylation value
- provide measure of replication-associated DNA methylation loss
- reflect cumulative number of cell divisions
- exclude non-Solo-WCGW motif sequences
- exclude non-intergenic Solo-WCGW motif sequences
- exclude H3K36me3 histone marked Solo-WCGW motif sequences
- exclude cell type invariant proxies
- locate Solo-WCGW motif sequences on single chromosome
- locate Solo-WCGW motif sequences across multiple chromosomes
- vary x value
- define PMDs by late replication timing
- define PMDs by nuclear lamina localization
- define PMDs by Hi-C-defined heterochromatic compartment B
- assess SD of solo-WCGW PMD hypomethylation
- identify common PMDs across cell or tissue types
- identify cell-type invariant PMDs
- identify cell-type specific PMDs
- reflect cell-type specific replicative/mitotic turnover rate
- reflect chronological age of cell or tissue sample
- identify cancer cell or tissue sample
- obtain genomic DNA from tissue biopsies or cell-free DNA
- vary number of Solo-WCGW motif sequences

## DETAILED DESCRIPTION OF THE INVENTION

- identify four distinct features influencing DNA methylation levels
- describe sequence context, replication timing, and H3K36me3 marks
- explain how these features shape PMD/HMD structure
- describe the role of cumulative number of cell divisions
- discuss the influence of CpG density and WCGW sequence context
- describe the processive action of DNMT1
- discuss conflicting findings regarding CpG flanking positions
- motivate the need for mechanistic studies
- describe the Solo-WCGW signature and its application
- discuss the analysis of HMD/PMD structure
- describe the major determinant for methylation levels at H3K36me3-negative CpGs
- explain the re-methylation window model
- discuss the role of H3K36me3 in overriding late-replication associated methylation loss
- describe the genetic evidence for maintenance of DNA methylation
- discuss the resolution of the paradox concerning actively transcribed gene bodies
- describe the influence of nuclear territories on DNA methylation maintenance
- discuss the identification of specific CpGs predictive of chronological age
- describe the distinction between PMD hypomethylation and age-associated signatures
- discuss the role of DNA hypomethylation in cancer
- describe the association between PMD hypomethylation and LINE-1 insertions
- discuss the influence of PMD hypomethylation on methylation-dependent mutational processes
- describe the protection of solo-WCGWs from deamination
- discuss the application of solo-WCGWs in low-coverage or single-cell WGBS studies
- describe the definition and use of a Solo-WCGW sequence motif
- discuss the shared PMD/HMD structure across cancer and normal tissues
- describe the rescaling of methylation values based on sample-specific PMD hypomethylation
- discuss the shared PMD/HMD structure across developmental lineages
- describe the emergence of PMD hypomethylation during embryonic development
- discuss the association between PMD hypomethylation and chronological age
- describe the age-associated PMD hypomethylation in fetal tissues
- discuss the acceleration of PMD hypomethylation upon sun exposure
- describe the association between PMD hypomethylation and donor age in diverse hematopoietic cell types
- discuss the nearly universal PMD hypomethylation in cancer
- describe the variation in PMD hypomethylation across cancer types
- discuss the correlation between PMD hypomethylation and somatic copy number aberration density
- describe the association between PMD hypomethylation and LINE-1 insertions in cancer
- discuss the link between ongoing cell proliferation and PMD hypomethylation
- describe the association between PMD hypomethylation and cell-cycle dependent genes
- discuss the replication timing and H3K36me3 marks affecting methylation
- describe the correlation between Solo-WCGW CpG methylation and replication timing
- discuss the highly methylated H3K36me3-marked regions
- describe the model of highly effective methylation maintenance at H3K36me3-marked regions
- discuss the materials and methods used in the work
- describe the demonstration of PMD hypomethylation in immortalized cell lines
- discuss the improved analysis of HMD/PMD structure using solo-WCGWs
- describe the stability of rank-based correlation between methylomes

### Terms (Definitions)

- define technical terms
- explain singular forms
- describe ranges
- define "optional" or "optionally"
- explain "on the order of"
- define "comprise"
- explain "exemplary"
- describe "such as"
- define "WCGW" sequence
- explain solo-WCGW motif
- describe preferred solo-WCGW motifs
- define "condition or state"
- explain effective cell division
- describe determining effective cell divisions
- define "determining the number of effective cell divisions"
- explain methods for determining effective cell divisions
- describe calculating population doubling level
- explain total mitotic history
- define "conditions for the test cell to divide"
- explain in vitro conditions
- describe in vivo conditions
- define "cell passaging" or "passaging"
- explain "passage number" or "cell passage"
- define "timepoint" or "timepoints"
- explain statistical significance
- describe p-value
- define "mitotic clock"
- explain DNA replication-dependent manner
- describe loss of DNA following DNA replication
- define "mitotic clock" as DNA hypomethylation level
- define terms
- describe method for developing mitotic clock
- describe data processing apparatus
- describe implementation of subject matter
- describe computer program
- describe processes and logic flows
- describe processors
- describe computer readable media
- describe interaction with user
- describe computing system
- describe backend component
- describe middleware component
- describe frontend component
- describe communication network
- describe client and server
- describe human and mouse Genome Assemblies
- describe human and mouse n(x)WCpGWn(x) genomic DNA sequence motif species
- describe exemplary probes
- describe primary human cells
- describe elastic net regression
- describe predictive performance of methylation clocks
- describe 44-CpG model
- describe 75-CpG subset
- define WGBS
- define TCGA
- define Hi-C-defined heterochromatic compartment B
- describe components and methods

### Example 1

- define Solo-WCGW sequence motif
- describe TCGA tumors and adjacent normal samples
- introduce MethPipe27 method
- determine local CpG density and tetranucleotide sequence contexts
- show PMD calls by methpipe on tumor and adjacent normal samples
- show ROC curve for hypomethylation tendency
- show methylation average of CpG dinucleotides in 10 tetranucleotide sequence contexts
- find low CpG density and WCGW context contributing to hypomethylation
- show solo-WCGW CpGs prone to hypomethylation
- show same sequence dependencies in other tumor and adjacent normal samples
- show additional 390 human and 206 mouse WGBS samples exhibiting same pattern
- show solo-WCGW CpGs allowing accurate PMD structure determination
- show application for low coverage or single-cell WGBS studies
- describe FIG. 1A-C
- describe FIGS. 10A1-A3 and B1-B2
- describe FIGS. 11A-C and 12A-B

### Example 2

- show strong concordance between PMD locations in all samples
- compare average solo-WCGW methylation of core tumors vs core normal
- show PMDs ranging from 100 kb to 5 mb mostly overlapping between tumors and normals
- compare standard deviation of 100-kb bins across core normal tissues and core tumors
- show bimodal distribution of SD within 100-kb bins in both normal and tumor core groups
- use bimodal SD peaks as a classifier to segment genome into HMDs and PMDs
- show high degree of concordance in PMD/HMD structure across tumor and normal samples
- describe FIGS. 2A-F and 13-14

### Example 3

- investigate solo-WCGW PMD structure across developmental lineages
- combine TCGA dataset with 343 previously published human and 206 mouse WGBS samples
- examine solo-WCGW methylation averages with human samples arranged into 6 groups
- examine solo-WCGW methylation averages with mouse samples arranged into 4 groups
- show PMD structure largely shared for 5 of the 6 categories
- show common PMDs overlapping lamina-associated regions and late replicating domains
- show germline and embryo category as the only exception
- show immortalized cell lines generally showing strongly hypomethylated PMDs
- show most disease-free post-natal tissues showing PMD structure shared with tumors and other groups
- show tissue types with high stem cell turnover displaying strongest PMD hypomethylation
- show all nucleated blood cell types showing shared PMD structure
- show B cells and T cells generally being divided into subgroups of strong vs weak hypomethylation
- show PMD hypomethylation already clearly evident by the naïve stage
- show PMDs occurring across all cell types of the myeloid lineage and being largely shared with other cell types
- describe FIGS. 3A-E, 4, 15A-C, and 16

### Example 4

- investigate PMD hypomethylation in gametes and early developmental stages
- analyze human sperm and mouse methylomes
- study PMD structure in human germinal vesicle oocytes
- examine demethylation in Inner Cell Mass and blastocyst samples
- analyze PMD structure in embryonic somatic tissues
- show progressive emergence of PMD/HMD structure along organismal development

### Example 5

- investigate link between PMD-associated hypomethylation and chronological age
- analyze solo-WCGW methylation level in CD4+ T cells from newborn vs. 103-year-old individual
- study age-related properties within larger studies using HM450 platform
- analyze PMD hypomethylation in PBMC samples from newborns and elderly donors
- examine PMD hypomethylation in fetal liver samples
- show nearly linear accumulation of hypomethylation from 9 weeks post-gestation to 22 weeks post-gestation
- analyze association between PMD hypomethylation and gestational age in mouse fetal tissue types
- study effects of environmental (UV) exposure on PMD hypomethylation in human skin samples
- show diverse hematopoietic cell types have significant association between donor age and degree of hypomethylation

### Example 6

- study landscape of cancer hypomethylation in 9,072 tumors from 33 cancer types
- analyze PMD hypomethylation in HM450 solo-WCGWs located within common PMDs
- compare PMD hypomethylation across cancer types to that of disease-free tissue of origin
- show association between PMD hypomethylation and somatic mutation density
- analyze association between PMD hypomethylation and somatic copy number aberration density
- study enrichment of LINE-1 insertion breakpoints in PMD regions
- analyze association between LINE-1 insertion density and PMD methylation
- identify genes most strongly associated with PMD hypomethylation
- determine enrichment of Gene Ontology functional terms associated with proliferation and mitotic cell division
- analyze enrichment of cell-cycle dependent genes from Cyclebase
- rank tumor samples by degree of PMD hypomethylation
- study expression of DNMT1 and DNMT3A/B in proliferative tumors
- analyze expression of UHRF1 in proliferative tumors
- investigate overexpression of TET genes in tumors with strongly hypomethylated PMDs
- show cumulative mitotic cell divisions as major driving force behind PMD hypomethylation accumulation
- analyze PMD methylation vs. somatic mutation density for all high purity TCGA cases
- study density of somatic LINE-1 insertions in non-overlapping 1-mb genomic bins

### Example 7

- analyze solo-WCGW based PMD definition in IMR90 cell type
- confirm coincidence of HMD/PMD structure with nuclear architecture
- study correlation between Solo-WCGW CpG methylation and replication timing
- analyze correlation between Solo-WCGW CpG methylation and H3K36me3
- disentangle contributions of H3K36me3 and replication timing to genome-wide DNA methylation levels and PMDs
- study methylation maintenance associated with early replication timing
- analyze relative contribution of replication timing vs. H3K36me3 in IMR90 and H1 cell lines
- support model of highly effective methylation maintenance at H3K36me3-marked regions
- show H3K36me3-linked maintenance acts independently from effect of replication timing on PMD methylation loss
- illustrate relationship between major determinants of hypomethylation and 3D nuclear topology

### Example 8

- select cancer types for WGBS assay
- describe sample preparation for WGBS
- outline paired-end WGBS-PE protocol
- detail DNA methylation rate and SNP information calling
- exclude CpGs with low read coverage
- choose window size for genomic binning
- show megabase-scale HMD/PMD structures
- define preliminary PMD/HMD domains based on all CpGs
- profile methylation patterns of 40 tumors
- identify PMDs in each sample individually
- define shared MethPipe PMD set
- define shared MethPipe HMD set
- dichotomize 100-kb bins into PMD/HMD using Gaussian mixture model
- determine final threshold for classifying PMDs from HMDs
- define common PMDs and common HMDs
- measure overlap of PMD boundaries
- define mouse PMDs/HIMDs
- preprocess TCGA HM450 data sets
- mask probes with detection p-value<0.05
- classify HM450 probes based on neighboring CpGs and tetranucleotide sequence context
- retain probes targeting solo-WCGW CpGs
- remove probes falling into annotated CpG Islands
- analyze IMR90 epigenome
- cluster features using Spearman's correlation coefficient
- exclude centromeres from IMR90 analysis
- quantify histone mark signal
- extract gene bodies from GENCODE transcript annotation
- rescale methylation values within common PMD 100-kb bins
- stratify solo-WCGW CpGs by overlap with H3K36me3
- stratify solo-WCGW CpGs by relative position to gene structures
- compute statistics using one-tailed Wilcoxon's Rank Sum test
- introduce example 8
- define PMDs using SD method
- describe power of SD method
- show concordance of SD-based PMD definitions
- discuss importance of cell-type-specific PMDs
- describe deep PMD hypomethylation in T cells
- propose incorporation of solo-WCGW sequence features
- discuss challenges in detecting differential PMDs
- describe potential applications of PMD domain structure
- introduce example 11
- perform rank-based analysis of methylomes
- show stability of rank-based correlation
- introduce example 12
- propose alternative explanation of PMD hypomethylation
- discuss link between DNMT3B and H3K36me3
- introduce example 13
- assess relevance of PMD sequence signature
- study somatic mutations in gastric cancer
- study de novo CpG->TpG mutations in germline
- discuss protective role of solo-WCGW hypomethylation
- introduce example 14
- define sub-patterns of solo-WCGW motif
- perform covariance analysis
- identify hypomethylation prone sequences
- discuss role of DNA shape features
- analyze association of DNA shape with hypomethylation
- introduce example 15
- describe primary cell culture methods
- describe DNA methylation assay methods
- describe beta calling methods
- describe QA/NA removal methods
- describe solo-WCGW subsetting methods
- introduce example 16
- (no content provided)
- introduce elastic net modeling strategy
- standardize PDL
- perform multi-tissue ENR modeling
- perform 10-fold cross validation and probe reduction
- evaluate model performance
- suggest use of elastic net regression strategy
- introduce individual probe regression strategy
- apply simple linear regression to each prefiltered probe
- compare regression coefficients
- filter probes based on correlation criteria
- evaluate model performance
- suggest use of individual probe regression strategy
- compare elastic net model and individual regression model
- describe differences in probe landscapes
- compare correlation coefficients and intercepts
- introduce comparison to existing clocks
- describe Hannum clock
- compare solo-WCGW clock to Hannum clock
- describe DNAm Age
- compare solo-WCGW clock to DNAm Age
- describe Skin & Blood Clock
- compare solo-WCGW clock to Skin & Blood Clock
- describe DNAm PhenoAge
- compare solo-WCGW clock to DNAm PhenoAge
- describe epiTOC mitotic-like methylation clock
- compare solo-WCGW clock to epiTOC clock
- highlight unique features of solo-WCGW clock
- introduce additional exemplary methods
- describe various methods for determining chronological age, mitotic turnover history, and excessive replicative turnover

