# Background

Fusion genes created by structural chromosomal rearrangements such as translocations, deletions, and inversions are often the pathogenetically essential feature of cancer genomes. They seem to be particularly characteristic of hematological malignancies and sarcomas, where their identification may be crucial for differential diagnosis and therapeutic decision-making. Fusion genes have so far been found less frequently in the common solid cancers, but recent reports on prostate and lung carcinomas show that fusion transcripts may contribute significantly also to the development of these malignancies [refs. [1-3]; reviewed in [4,5]].

The detection of fusion genes in cancer is laborious and time-consuming and usually includes chromosome banding analysis (karyotyping) followed by fluorescence in situ hybridization (FISH) studies and molecular analyses based on the reverse transcriptase polymerase chain reaction (RT-PCR). Karyotyping requires the availability of fresh, vital cells for short-term culturing to obtain metaphase chromosomes, and the success rate of this approach may be particularly low for solid tumors. In addition to taking a lot of time, the method also requires highly trained and experienced personnel to interpret the karyotypes correctly and identify whatever rearrangements may exist. The main advantage of the approach is that it is global in nature; it screens without prejudice for all rearrangements at the chromosomal resolution level. FISH with locus-specific probes and RT-PCR, on the other hand, are precise and highly specific methods used for the analysis of one or a few candidate fusion genes at predefined breakpoints; the approach is therefore dependent on prior knowledge of the suspected diagnosis. The specificity of these methods at the same time highlights their main limitation; they have no screening ability.

Recent developments of high-throughput sequencing technologies enable genome-wide identification of novel fusion transcripts at an unprecedented level of resolution [6-9], but these technologies are as yet limited by the number of samples that can be analyzed within a reasonable time-frame and at an acceptable cost. A few studies have utilized oligo microarrays targeting junction sequences to detect fusion transcripts [10-13]. They have then relied on preceding amplification of a small selection of fusion transcripts by RT-PCR, thus limiting the coverage offered by these approaches to a predefined set of fusion junction sequences.

In this report, we present a new oligo microarray-based approach for simultaneous analysis of all known or predicted fusion gene variants, with all possible chimeric exon-exon junction combinations. The analysis can be performed in a single experiment and does not include prior sequence-specific amplification.

# Methods

## Cell Lines And Biopsies

To test our novel method for fusion gene detection, we selected four prostate cancer samples (fresh frozen tissue obtained from prostatectomy specimens of four independent patients) and two leukemic cell lines, all known to harbor a specific fusion gene. The cell lines, RCH-ACV [14] and REH [15,16], are of human B-cell precursor leukemia origin and were provided by Dr. Edith Rian.

## Preparation Of Cdna For Microarray Analysis And Rt-Pcr

Total RNA was isolated using the Trizol reagent (Life Technologies, Rockville, MD, USA), and the RNA quality was evaluated by use of the Agilent 2100 Bioanalyzer (Agilent Technologies, Palo Alto, CA, USA). To enrich for messenger RNA, we used the RiboMinus kit (Invitrogen, Carlsbad, CA, USA) which subtracts ribosomal RNA from total RNA. To ensure detection of fusion junctions far away from the poly-A tail, the first strand cDNA was prepared by random priming to avoid the 3' end bias introduced by oligo-dT labeling. Double stranded cDNA was labeled and hybridized onto the oligo microarrays.

## Microarray Design

We set up a database with a broad coverage of the reported fusion genes in cancer (351 to date), including information on which of the fusion partners are up- and downstream in the majority of the resulting fusion transcripts. See Additional file 1 for the identities and orientation of the 275 fusion genes included in the pilot microarray design. We used public genome sequence information from Biomart to extract the exon sequences of all listed transcript variants [17].

A script was written in the programming language Python for design of the oligos. For genes that constitute the 5' portion of fusion genes, we used the 3' end-sequences of the exons when constructing chimeric fusion junction oligos. For genes that are the 3' portion of fusion genes, we used the 5' start-sequences of the exons. Thus, for each fusion gene, we joined and listed all combinations of end-sequences and start-sequences. These chimeric sequences served as input for the design of chimeric fusion junction oligos, enabling detection of any breakpoint combination in the fusion genes. Chimeric oligos were constructed targeting all possible combinations of chimeric exon junctions between the up- and downstream partners of 275 known fusion genes. For a set of fusion genes, including the ones known to be present in the control samples, we extended the design to include four replicates of each of the exon-exon junctions, as well as altogether four extra control oligos for each exon-exon junction (oligos up- and down-shifted by two nucleotides as compared to the standard ones). Furthermore, a series of intragenic oligos were designed for measurements of longitudinal profiles of each of the fusion gene partners of altogether 115 genes, including all the positive control fusion genes. These were oligos targeting the start, mid, and end part of all exons and all introns, as well as oligos targeting the exon-exon, exon-intron, and intron-exon junctions. The exon-intron junctions and intron-exon junctions are also included among the single-gene oligos, as the pre-mRNA processing machinery may alter the splicing pattern following removal or introduction of cis-acting splicing regulatory sequences.

The constructed microarray included a design with 68,861 oligos, including 59,381 chimeric oligos (of which 55,482 were unique), which were synthesized onto custom-produced NimbleGen microarray slides (Roche NimbleGen, Inc., Madison, WI, USA). The chimeric oligos were designed to optimize for similar melting temperatures on each side of the junctions, thus reducing half-binder effects.

Two versions of the microarray were designed, differing as to the probe lengths. The set of shorter oligos, with lengths ranging from 34 to 40-mers, had a Tm optimum of 72°C. The set of longer oligos, with lengths ranging from 44 to 50-mers, had a Tm optimum of 75°C. All samples, except the REH cell line, were hybridized onto the short-oligo microarray, whereas the RCH-ACV and REH cell lines were hybridized onto the long-oligo microarray. The cell line RCH-ACV was analyzed by both microarray designs, and data from its positive control gene, TCF3:PBX1, demonstrated best performance of the short oligos due to substantial half-binder signals with the longer oligos (data not shown).

Because of the relatively short length of the sequences on each side of the junction, the binding may be sensitive to single nucleotide polymorphisms (SNPs). Thus, at known SNP positions, we created extra sets of probes, accounting for each of the SNP variants.

## Data Preprocessing And Annotation

Data preprocessed by NimbleGen were further normalized by dividing all individual probe intensity values for each of the samples by the median of the three leukemia cell lines. We normalized based on these three samples (instead of all samples) because when the majority of the samples contain the same fusion gene and breakpoint (TMPRSS2:ERG, e1:e4), normalizing on all samples would level out the appearance of this fusion event in the dataset.

All oligonucleotide probes were mapped to their one or two respective genomic loci. For each locus, the Ensembl identifiers for exon (ENSE), transcript (ENST), and gene (ENSG) identities were used.

Raw and processed data were deposited to the Gene Expression Omnibus public repository for microarray data [accession number GSE14435] according to the MIAME, minimum information about a microarray experiment, recommendations for recording and reporting microarray-based gene expression data [18].

## Automated Scoring Algorithm

Downstream fusion partners will generally have higher expression values for exons downstream of the fusion breakpoint. For each exon-exon junction of downstream fusion partner genes, two probabilities were calculated. One probability was based on a t-test for whether values from all upstream and all downstream exons are likely to belong to different populations. A second probability was based on a t-test for whether the values from the immediate up- and downstream exons are likely to belong to different populations.

A fusion score was calculated as the product of the normalized expression value for the chimeric oligo and the probabilities of the exon-exon junction of the corresponding position in the downstream fusion partner being a breakpoint in the longitudinal profile [Fusion score = Chimeric junction score * P(B-gene transcript) * P(B-gene exon)].

To keep the values within scale, the following thresholds were applied: when the normalized values for chimeric oligos were larger than 5, they were set to 5 (approximately 5 per 10,000 values). Similarly, when probabilities for a breakpoint in the longitudinal profiles were < 0.10, they were set to 0.10. When the values from the downstream exons were lower than the values from the upstream exons, the probability was set to 0.10 as well.

## Experimental Validation Of Fusion Transcript Breakpoints

We used RT-PCR followed by DNA sequencing to validate the actual fusion junctions in the positive control fusion genes. The following primers were applied: TCF3:PBX1: TCF3, exon 15, forward, 5'-CACCCTCCCTGACCTGTCT-3', and PBX1, exon 3, reverse, 5'-TGCTCCACTGAGTTGTCTGAA-3'; yielding a chimeric fusion product of 218 basepairs. ETV6:RUNX1: ETV6, exon 5, forward, 5'-CACTCCGTGGATTTCAAACA-3', and RUNX1, exon 2, reverse, 5'-CGTGGACGTCTCTAGAAGGA-3'; yielding a chimeric fusion product of 204 basepairs. TMPRSS2:ERG [as published in ref. [19]]: TMPRSS2, exon 1, forward, 5'-TAGGCGCGAGCTAAGCAGGAG-3', and ERG, exon 6, reverse, 5'-CTGCCGCACATGGTCTGTAC-3'; yielding a chimeric fusion product of 597 basepairs. The PCR products were separated by gel electrophoresis in a 2% agarose gel. For all fusion genes, DNA was isolated from the appropriate PCR bands (MiniElute Gel Extraction kit, Qiagen Co., Valencia, CA, USA) and sequenced in both directions using the same primers as for the RT-PCR (ABI Prism 3730; Applied Biosystems, Foster City, CA, USA).

## Cytogenetics

Cell cultures from the leukemia cell lines were harvested for chromosome banding analysis. Chromosome preparations were made and G-banded using trypsin (DIFCO Laboratories, Detroit, MI, USA) and Leishman staining (BDH, Poole, England). For metaphase FISH, commercially available probes for the TCF3:PBX1 (TCF3 FISH DNA probe, split signal, DAKO Denmark A/S, Glostrup, Denmark) and ETV6:RUNX1 (dual color, Dual Fusion Translocation Probe Set; Vysis, Abbott Laboratories, Abbott Park, IL, USA) fusion genes were used. The denaturation and hybridization conditions as well as the subsequent detection procedures were in accordance with the manufacturers' protocols. Two hundred successive, whole, and single nuclei were examined through a Zeiss fluorescence microscope (Zeiss Axioplan, Oberkochen, Germany) for each FISH experiment.

# Results

We have developed a novel strategy for the detection of oncogenic fusion transcripts enabling simultaneous analysis of all known or predicted fusion gene variants, with all possible chimeric exon-exon junction combinations targeting each possible fusion gene junction on the processed mRNA level (Figure 1). We combine the use of chimeric oligos, spanning the two potential fusion gene partners, with the use of single-gene oligos that provide measurements along the length of each individual partner.

We analyzed cDNA from a set of six positive control samples with known presence of one fusion gene in each. This included two leukemia cell lines, RCH-ACV and REH, known to carry the TCF3:PBX1 and ETV6:RUNX1 fusion genes, respectively, and four prostate cancer samples positive for the TMPRSS2:ERG fusion gene.

To combine the information from the chimeric junction measurements with that of the longitudinal intragenic profiles, a fusion score was calculated for all fusion transcripts and their respective breakpoints (details in Materials and Methods). This enabled an objective and automated evaluation of the presence of fusion genes, and the fusion score was calculated for 10,297 possible fusion events. The positive control fusion transcripts, with their correct breakpoint positions, was ranked as the number one hit in four out of the five samples run on the short-oligo microarray (Figures 2A and 3A), thus validating the concept. For prostate cancer sample P140, the expected TMPRSS2 exon 1:ERG exon 4 fusion gene was assigned a fusion score rank of 95 within the 10,297 fusion breakpoints (and number one within the 154 measured junctions of TMPRSS2:ERG). When dissecting the values behind the fusion score for this positive control, we see that the intensity of the chimeric oligo was particularly low. This is also in compliance with RT-PCR results from the prostate cancer samples, demonstrating that this sample had a low expression level of the fusion gene as compared to the other samples (data not shown).

To evaluate the top fusion score hits and positive control fusion genes further, we visualized them via two independent paths, using either the chimeric probe set (Figures 2B and 3B) or the longitudinal intragenic probe set (Figures 2C and 3C). The positive control fusion genes were clearly visualized for all six analyzed samples.

# Discussion

A novel microarray-based strategy is presented to screen for all known oncogenic fusion transcripts in a given sample, combining measurements of chimeric transcript junctions with exon-wise measurements of individual fusion partners. This provides a viable alternative to the existing cytogenetic and PCR-based methods for fusion gene detection, as it enables an objective and automated genome-wide analysis in which all known as well as predicted fusion genes are assessed without requiring any a priori knowledge as to the likelihood of the clinical or genetic diagnosis. Furthermore, the precise mapping information on the fusion breakpoint is given within every positive hit. Finally, the method is carried out in a single experiment and does not include prior sequence-specific amplification.

Because fusion breakpoints mainly map to intronic sequences, the resulting fusion transcripts will, after pre-mRNA processing, consist of whole exonic building blocks. In fact, more than 90% of the mapped fusion breakpoints are located in intronic sequences [20]. Thus, independently of the intra-intronic location of the breakpoints, a detection of all exon-exon junctions between two fusion gene partners would in principle provide specific detection of fusion transcripts.

To our knowledge, this is the first time chimeric oligos targeting fusion gene junctions have been used in combination with measurements of longitudinal profiles of the individual fusion partners. Furthermore, the earlier publications on fusion gene measurements by oligo microarrays have not attempted to be genome-wide, restricting their use to either a few pre-defined fusion junctions and fusion genes [10-13] or to the exclusive use of intragenic oligos [21]. Our pilot experiment alone included 68,861 oligos, and the current version of the NimbleGen microarray platform enables analysis of up to 2.1 million oligos on a single microarray slide. Thus, scaling up to include all known fusion genes, as well as sets of novel candidate fusion genes detected by high-throughput sequencing strategies, can easily be achieved with the same resolution level as the genes included in our pilot run.

Next-generation sequencing approaches are beginning to provide numerous new pairs of fusion genes in individual biological samples [6-9]. However, this methodology is not feasible for screening purposes on large clinical sample series. The current microarray-based approach is suitable for assessing whether members of this growing set of novel fusion transcripts (alongside with the already known fusion genes) are indeed pathogenetic players in the various subgroups of cancer.

The reported fusion gene detection platform can be used irrespective of the tumor type in question. Detection of certain fusion genes has direct diagnostic implications in many leukemias and sarcomas, whereas other fusion genes are more promiscuous and can be found in several different cancer types. An example of the latter is the karyotypically cryptic translocation t(12;15)(p13;q25), resulting in the ETV6:NTRK3 fusion gene, which occurs in histologically and developmentally completely disparate tumors such as kidney and breast tumors, infantile fibrosarcoma, and acute myeloid leukemia [22].

# Conclusion

We have developed a novel high throughput method for detection of fusion genes with potentially significant applications in cancer diagnostics. Also, for research applications, there is a clear potential for detection of putative fusion genes and discovery of already known fusion genes in new cancer types.

# List Of Abbreviations

FISH: fluorescence in situ hybridization; RT-PCR: reverse transcriptase polymerase chain reaction.

# Competing Interests

A patent application has been filed for the fusion gene microarray methodology.

# Authors' Contributions

RIS coordinated the project and drafted the manuscript. GOST designed and programmed algorithms for oligo design and data analysis. ME, GEL, FM, FRR, and NC performed laboratory analyses. MRT, SH, TR, and RAL supervised parts of the project, and contributed to design of the study and discussion of results. All authors contributed to the writing, and have read and approved the final manuscript.

