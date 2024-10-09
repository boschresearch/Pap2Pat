# DESCRIPTION

## STATEMENT OF GOVERNMENT RIGHTS

- government rights in invention

## FIELD OF THE INVENTION

- non-invasive methods for detecting tumor-specific alterations

## BACKGROUND

- challenge of identifying patients with microscopic residual disease
- limitations of current imaging techniques and blood biomarkers
- importance of histopathological assessment

## SUMMARY

- new non-invasive methods for detecting tumor-specific alterations
- matched white-blood cell and cell-free DNA analyses
- detection of mutations in circulating tumor DNA
- methods useful for detecting and monitoring gastric cancer
- methods useful for detecting and monitoring colorectal cancer
- methods useful for detecting and monitoring lung cancer
- methods useful for detecting and monitoring esophageal cancer
- various embodiments of the method

## Definitions

- define terms used in the invention
- singular forms include plural forms
- "about" or "approximately" means within an acceptable error range
- "aligned", "alignment", "mapped" or "aligning", "mapping" refer to sequence matching
- "alternative allele" or "ALT" refers to an allele with one or more mutations
- "cancer" refers to a disease characterized by unregulated cell growth
- "candidate variant" refers to a detected nucleotide variant
- "cell free nucleic acid", "cell free DNA", or "cfDNA" refers to nucleic acid fragments in the bloodstream
- "circulating tumor DNA" or "ctDNA" refers to nucleic acid fragments from tumor cells
- "comprising" means including specified elements
- "diagnostic" or "diagnosed" means identifying the presence or nature of a pathologic condition
- "effective amount" means an amount providing a therapeutic or prophylactic benefit
- "genomic nucleic acid" or "genomic DNA" refers to nucleic acid from healthy cells
- "Next Generation Sequencing (NGS)" refers to massively parallel sequencing methods
- "optional" or "optionally" means an event or circumstance may or may not occur
- "or" means and/or unless the context clearly dictates otherwise
- "parenteral" administration includes subcutaneous, intravenous, intramuscular, or intrasternal injection
- "patient" or "individual" or "subject" refers to a mammalian subject
- "reference genome" refers to a digital or previously identified nucleic acid sequence database
- "read segment" or "read" refers to nucleotide sequences from a sample
- "sequence reads" refers to nucleotide sequences read from a sample
- "therapeutically effective" amount means an amount sufficient to produce a therapeutically desirable result
- "treat", "treating", "treatment" refer to reducing or ameliorating a disorder
- genes and gene products disclosed are intended to correspond to homologs from any species
- ranges are intended to encompass subranges and individual numerical values

## DETAILED DESCRIPTION

- introduce matched cfDNA and WBC sequencing approach
- motivate ctDNA detection after preoperative chemotherapy
- describe methods to identify ctDNA alterations
- summarize results of liquid biopsy analyses
- define candidate tumor-specific mutations in cfDNA
- outline criteria for considering an alteration a candidate somatic mutation
- classify candidate alterations as somatic hotspots

### Genomes and Cancer

- introduce cancer genome sequencing
- explain somatic mutations
- describe tumor tissues analysis
- introduce cell free circulating tumor DNA (ctDNA)
- explain liquid biopsy
- discuss limitations of liquid biopsy methods
- motivate need for improved sensitivity and selectivity
- introduce method of detecting tumor specific mutations
- describe sample preparation
- explain sequencing library preparation
- compare sequence variations between cfDNA and cellular DNA
- identify tumor specific mutations
- apply detection of mutations to surgical resection eligibility
- apply detection of mutations to therapy response monitoring
- apply detection of mutations to pathological response prediction
- apply detection of mutations to recurrence prediction
- apply detection of mutations to cancer-specific survival prediction
- apply detection of mutations to overall survival prediction
- apply detection of mutations to minimal residual disease detection
- apply detection of alterations to clonal hematopoiesis
- apply detection of mutations to neoadjuvant systemic treatment identification
- describe enzymatic steps for sequencing library preparation
- explain attachment of amplification adapters and barcode sequences
- discuss design of barcode sequences
- introduce sequencing of nucleic acid
- describe high-throughput sequencing methods
- list various DNA sequencing techniques
- detail sequencing-by-synthesis systems
- explain pyrosequencing
- describe SOLiD technology
- detail ion semiconductor sequencing
- explain Illumina sequencing
- describe single molecule, real-time (SMRT) technology
- detail nanopore sequencing
- explain chemFET array sequencing
- describe electron microscope sequencing
- define sequence reads
- explain FASTA and FASTQ file formats
- describe assembly of sequence reads
- detail alignment of sequence reads to a reference
- identify variant sequences
- describe Bayesian statistical model
- compute posterior probability of tumor-derived alterations
- analyze correlation coefficients of mutations
- compute probability of tumor-derived mutations
- describe Bayesian hierarchical model
- detail joint model
- determine quality score based on likelihood
- automate steps of the invention
- implement methods in existing sequence analysis platforms
- configure sequencer for next generation sequencing
- configure sequencer for massively parallel sequencing
- configure sequencer for sequencing-by-ligation
- configure sequencer for single molecule sequencing
- describe processing system for executing code
- store models in a database
- retrieve models for application post-training
- use parameters of the model to determine likelihood of true positives

## EXAMPLES

### Example 1: Matched White Blood Cell and Cell-free DNA Analyses for Prediction of Therapeutic Response in Patients with Cancer

- introduce study objective
- hypothesize ctDNA detection
- describe experimental study design
- outline CRITICS study
- detail patient selection
- describe cfDNA and WBC sequencing
- outline tumor-specific mutation detection
- describe patient characteristics
- outline pathological assessment
- describe mismatch repair status determination
- outline EBV status determination
- describe MSI analysis
- outline sample preparation
- describe next-generation sequencing
- outline targeted capture
- describe library preparation
- outline sequencing
- describe primary processing of NGS data
- outline identification of putative somatic mutations
- describe candidate tumor-specific mutation identification
- outline statistical analyses
- describe significance testing
- outline correlation coefficient determination
- describe survival analyses
- outline probability computation for tumor-derived mutations
- describe prior distribution for theta_plasma
- outline posterior odds calculation
- introduce study on matched white blood cell and cell-free DNA analyses for prediction of therapeutic response in patients with cancer
- describe CRITICS study and patient selection
- outline study design and methods
- detail sequencing approach and analysis of cfDNA and WBCs
- estimate theoretical sensitivity of detection of sequencing approach
- analyze mutant allele fractions at baseline
- compare levels of mutant allele fractions among well, moderately, or poorly differentiated tumors
- analyze event-free and overall survival
- detect clonal hematopoiesis and identify tumor-specific alterations
- analyze TP53 alterations in cfDNA and WBCs
- evaluate fragment length distributions of TP53 alterations
- analyze WBC variants in multiple time points
- evaluate ctDNA levels before and after preoperative chemotherapy
- analyze complete elimination of ctDNA levels after systemic treatment
- analyze association between ctDNA levels and pathological response
- analyze association between ctDNA levels and survival outcomes
- evaluate minimal residual disease after surgery
- analyze complete elimination of tumor-specific mutations in cfDNA
- analyze postoperative tumor-specific mutations
- analyze association between postoperative ctDNA levels and survival outcomes
- discuss limitations of current methods for estimating risk of disease recurrence
- introduce tissue-independent sequencing approach
- discuss perioperative strategies for gastric cancer
- highlight need for selecting patients who require adjuvant treatment
- discuss value of parallel deep sequencing of cfDNA and WBCs
- analyze association between Lauren's intestinal subtype and mutant allele fractions
- discuss challenge of distinguishing tumor-specific mutations from background changes
- highlight importance of WBC filters in liquid biopsy analyses
- discuss application of tissue-independent approach to predict treatment response
- compare results with recent ctDNA analyses in non-small cell lung cancer
- reinforce paradigm of using ctDNA analyses for response to therapy and minimal residual disease assessment
- discuss potential of noninvasive detection of ctDNA for early risk stratification
- highlight therapeutic decisions for novel interventions in clinical trials
- discuss limitations of study
- outline future directions
- summarize main findings
- discuss implications for clinical practice
- highlight need for further research
- discuss potential applications in other cancer types
- outline potential benefits of ctDNA analysis
- discuss potential challenges and limitations
- highlight importance of collaboration and data sharing
- conclude with final thoughts on the study

### Example 2: Early Detection and Detection of Minimal Residual Disease in Stage II and III Colorectal Cancer Patients Using a Noninvasive, White Blood Cell-Guided Liquid Biopsy Approach to Identify Mutations as Biomarkers

- introduce colorectal cancer statistics
- describe current limitations of CRC screening and early detection
- motivate noninvasive liquid biopsy approach
- describe study design and patient enrollment
- analyze baseline and post-resection liquid biopsies using ultra-deep sequencing
- identify mutations in white blood cells
- remove hematopoietic and germline alterations from plasma analyses
- analyze matched tumor tissue using targeted sequencing
- confirm concordance between plasma and tumor alterations
- detect tumor-derived mutations in plasma
- describe mutant allele fractions at baseline and post resection
- discuss limitations of current CRC screening methods
- highlight importance of white blood cell-guided approach
- describe removal of alterations from white blood cells
- analyze matched white blood cells and plasma samples
- identify mutations in DNMT3A, TP53, APC, and KRAS
- observe correlation between mutant allele fractions in white blood cells and plasma
- discuss hematopoietic mutations in both baseline and post-resection plasma samples
- analyze matched tumor tissue using targeted sequencing
- confirm concordance between plasma and tumor alterations
- detect tumor-derived mutations in plasma
- describe mutant allele fractions at baseline and post resection
- discuss limitations of current CRC screening methods
- highlight importance of white blood cell-guided approach
- describe removal of alterations from white blood cells
- analyze matched white blood cells and plasma samples
- identify mutations in DNMT3A, TP53, APC, and KRAS
- observe correlation between mutant allele fractions in white blood cells and plasma
- discuss hematopoietic mutations in both baseline and post-resection plasma samples
- conclude feasibility of white blood cell-guided liquid biopsy approach

### Example 3. Matched Leukocyte DNA Guided Liquid Biopsy Approaches for Response Monitoring in the Context of Immunotherapy for Metastatic Lung Cancer Patients

- introduce immunotherapy for metastatic lung cancer
- motivate need for accurate response monitoring
- describe study design and patient enrollment
- perform deep targeted error correction sequencing of plasma and white blood cell DNA
- classify plasma variants as WBC or ctDNA variants
- filter out clonal hematopoiesis alterations
- interpret ctDNA molecular responses with respect to clinical phenotypes
- show representative example of patient responding to immunotherapy
- demonstrate predictive value of ctDNA dynamics
- investigate predictive and prognostic performance of ctDNA molecular responses
- compare performance with and without filtering out CH-derived mutations
- conclude importance of matched leukocyte DNA sequencing and analysis

### Example 4: Matched Leukocyte DNA Guided Liquid Biopsy Approaches for Response Monitoring in the Context of Immunotherapy for Early Stage Esophageal Cancer Patients

- introduce esophageal cancer treatment with immunotherapy and chemoradiation
- describe liquid biopsy approach using targeted error correction sequencing
- identify and exclude germline or clonal hematopoiesis derived variants
- analyze correlation between CH-derived mutations and patient age
- illustrate ctDNA dynamics using TP53 G245S mutation example
- associate detectable ctDNA with residual tumor and disease progression
- summarize clinical utility of matched plasma-leukocyte DNA sequencing approach
- reference clonal hematopoiesis in non-hematologic cancers
- reference age-related clonal hematopoiesis and adverse outcomes
- reference various studies on clonal hematopoiesis and cell-free DNA analyses

## Other Embodiments

- disclaim limitation of description
- incorporate prior art references

