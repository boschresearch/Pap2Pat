# Introduction

Reverse transcription quantitative real-time polymerase chain reaction (RT-qPCR) tests that measure transcript abundance of selected genes in clinical specimens have been demonstrated to increase cancer diagnostic accuracy and enable “personalized medicine” through selection of the most effective treatment for each cancer [1]–[3]. However, a key challenge is that current clinical pathology sample collection and processing procedures focus on formalin fixation and paraffin embedding (FFPE) and fresh/fresh-frozen tissues rarely are available for molecular analysis. FFPE samples are difficult to work with because they yield RNA that 1) often contains PCR-interfering substances, and 2) is uniformly highly fragmented and often in low abundance [4]–[8]. Economic factors prevent changing this workflow to ensure collection of samples in a form more conducive to molecular genetic analysis, such as fresh frozen, therefore, there is a need to develop methods that are sufficiently robust to reliably conduct molecular genetic analysis in FFPE samples.

One way to address the challenge of interfering substances is to incorporate quality control in qPCR through measurement of each analyte relative to a known number of competitive template internal standard (IS) copies. This quality control method is recommended by regulatory agencies, including the EPA [9], ISO [10], and FDA [11], and is implemented in many FDA-approved single analyte RT-qPCR tests [12]–[14].

Multiple gene RT-qPCR tests present an even more complex quality control challenge that can be addressed by combining the IS for each of the genes into an internal standards mixture (ISM) and using an aliquot of this ISM in each experiment, as previously described [15]–[17]. Each target gene and loading control gene then is measured relative to a known number of its respective competitive template IS molecules in each PCR reaction [18], [19].

To address the challenge of analyzing clinical samples that yield a low amount of RNA, we previously described a competitive multiplex PCR method, in which all reference and target genes are first co-amplified with ISM in a first round of PCR, followed by amplification of individual gene in the second round [20]. This approach enables reliable measurement of many genes from the amount of RNA that, without pre-amplification, would be sufficient for measurement of only a single gene.

The primary goal of this study was to develop a robust RT-qPCR method for more reliable molecular diagnostic testing of FFPE samples including those stored in existing large archives. To meet this need, a method was designed with four elements: 1) Synthetic competitive IS formulated into an ISM to control for sub-optimal PCR, including interference with PCR caused by substances present in FFPE samples [21]–[23], sub-optimal quantity or quality of PCR reaction reagents, and inter-well and/or inter-platform variation in PCR conditions; 2) Fluorometric hydrolysis probe real-time PCR to enable quantification of short PCR amplicons (60–80 base pairs) that are optimal for reliable analysis of FFPE samples; 3) An external standards mixture (ESM) in each experiment to control for inter-lot and inter-experimental variation in probe fluorescence intensity; and 4) Reverse transcription with gene specific primers (GSP) followed by competitive multiplex pre-amplification to enable measurement of lowly expressed genes in pauci-cellular samples with degraded and limited amounts of RNA.

To validate this approach, we developed reagents for measurement of previously reported lung cancer diagnostic test (LCDT) comprising v-myc avian myelocytomatosis viral oncogene homolog (MYC), E2F transcription factor 1 (E2F1), and cyclin-dependent kinase inhibitor 1A (CDKN1A) genes measured relative to actin, beta (ACTB) [24]. These reagents were subjected to analytical validation using synthetic templates as test articles and fitness for the purpose of testing using surgical benign and malignant FFPE samples according to recommended practices [25].

# Materials And Methods

## Ethics Statement

Twenty archived surgical FFPE lung tissues that had been processed according to the standard University of Toledo Medical Center (UTMC) Department of Pathology practice between 2010 and 2012 were obtained for this study under UTMC IRB # 107790. According to the UTMC IRB # 107790 protocol, each FFPE sample was assigned a non-identifying number by the pathologist and transferred to the research laboratory. The link between the non-identifying number and identifying information was destroyed by the pathologist immediately following sample transfer. Accordingly, on March 27, 2013 the UTMC IRB #107790 protocol was approved by the Chair of the UTMC Biomedical Institutional Review Board as exempt research and the requirement to obtain a signed consent/authorization form for use and disclosure of protected health information was waived as this research was determined to be minimal risk.

## Ffpe Sample Preparation

Microtome sections (10 micrometre thickness) were obtained from each sample. Six strips per sample (1 strip = 4 sections) were obtained, and each strip was put in one 1.5 ml micro-centrifuge tube for RNA extraction. Therefore, 24 sections (240 micrometres) of each sample block were collected for RNA extraction.

## Rna Extraction And Reverse Transcription

RNA was extracted from the surgical FFPE samples using the RNeasy FFPE Kit (Qiagen, Valencia, CA). RNA was treated with DNase in the RNeasy FFPE Kit RNA extraction protocol in order to minimize the effect of contaminating genomic DNA. RNA purity and integrity were assessed using absorbance at 260/280 nm ratios and RNA integrity number (RIN) scores as detected on the Agilent 2100 Bioanalyzer (Agilent Technologies, Santa Clara, CA). The effect of different conditions on reverse transcription (RT) efficiency, including priming with random hexamer primers (RHP) or GSP and use of 1 or 5 µg of RNA in the 30 µl RT reaction, was assessed with three FFPE samples. A previously described test using the External RNA Control Consortium (ERCC) standards was used to measure RT efficiency [26]. After completion of these studies, optimal RT conditions were selected consisting of a 30 µl RT reaction with 1 µg of RNA, gene-specific RT primer (the PCR reverse primer) (3 µM), and SuperScript III First Strand Synthesis System (Life Technologies, Grand Island, NY).

## Primer Design And Testing Of Efficiency And Specificity

For each gene (MYC, E2F1, CDKN1A and ACTB) primers were designed to 1) amplify the shortest possible PCR product size (60–80 base pairs) and 2) span intron/exon splice junctions to minimize the effect of residual genomic DNA contamination (Table 1).

Each candidate primer pair was assessed for efficiency in a serially diluted mixture of H23 cell line cDNA and ISM using endpoint PCR. After 35 PCR cycles, products were electrophoretically separated on an Agilent 2100 Bioanalyzer (Agilent Technologies, Santa Clara, CA), the electropherogram was inspected for presence or absence of non-specific products, and appropriately sized peaks were quantified by densitometry.

## Design Of Probes And Is Templates

For each gene target, after native template (NT) primers with sufficient efficiency and specificity were identified, we developed real-time PCR assays using fluorometric hydrolysis probes [27]. First, a probe for the NT was designed followed by the design of an IS probe for the same DNA region but with 4–6 base pair alterations from the NT probe sequence. An IS template with corresponding alterations was synthesized as described in the synthesis and purification of standards section below. Use of multiple base changes in the IS probe ensured specificity of NT probe (FAM labeled) for the NT and IS probe (Quasar 670 labeled) for the IS. Probes with a fluorescent label at the 5′ end and a Black Hole Quencher at the 3′ end (BHQplus, Biosearch Technologies, Novato, CA) were designed using real-time design software from the Biosearch Technologies web site (Figure 1A, Table 1).

## Synthesis And Purification Of Standards

For each gene, we synthesized an NT (to be used in the ESM) and an IS via commercial vendor (Life Technologies, Grand Island, NY). The products of such syntheses are single-stranded and contain a significant fraction of incompletely synthesized (less than full-length) molecules. Thus, we PCR-amplified each synthesized NT or IS with GSP to generate completely synthesized, double-stranded nucleic acid templates. This was followed by electrophoretic separation of the PCR products on agarose gel, selection of the correct size band, and purification from agarose using QIAX II gel extraction kit (Qiagen, Valencia, CA) (Table 1).

## Probe Specificity Test

Specificity of each probe was tested by including it in PCR assays containing the synthetic NT or IS serially diluted from 10−11 M to 10−15 M. For each probe, at each NT or IS dilution, the signal (Cq value: quantification cycle) [28] observed with amplification in the presence of the non-homologous template was compared to Cq value observed with amplification in the presence of the homologous template. The non-specific binding rate was calculated using 2(−delta Cq) (delta Cq = non-homologous template Cq – homologous template Cq) at each dilution. If, at any concentration, the number of input non-homologous molecules detected by the probe was more than 10% of the number of homologous molecules detected, then the probe was re-designed.

## Preparation Of Internal Standards Mixture (Ism)

Known quantities of the IS for each gene were combined into an ISM. Use of the ISM rather than individual IS in each experiment minimized inter-experimental variation [16] as described in Table S1A in File S1. Six different ISM were prepared (ISM A–F) containing different concentrations of target gene IS mixture (MYC, E2F1, CDKN1A) relative to the reference gene (ACTB) IS.

## External Standards Mixture (Esm)

Known quantities of purified synthetic NT and IS for each gene were combined into an ESM. The ESM was used to control for inter-experimental variation resulting from 1) instability or intensity differences of one fluor relative to the other and 2) software selection of Cq. We prepared a stock ESM with 10−11 M NT/10−11 M IS, and then diluted it to two working concentrations of 10−13 M NT/10−13 M IS and 10−14 M NT/10−14 M IS. Each of these two ESM concentrations was measured in each experiment and for each gene the average measured Cq difference [NT Cq - IS Cq] from the two ESM was used to correct the [NT Cq - IS Cq] value measured in each unknown sample (Table S1B in File S1, Figure S1 in File S1).

## Pre-Amplification (1St Round Pcr)

The pre-amplification reaction for each sample was prepared in a 20 µl volume and included 1) 2 µl primer mixture (ACTB, MYC, E2F1, CDKN1A) with concentration of each primer at 800 nM (final concentration of each primer in PCR of 80 nM), 2) 1 µl cDNA sample, 3) 1 µl ISM, and 4) 10 µl TaqMan Universal Master Mix II (No UNG: Uracil N-Glycosylase, Life Technologies, Grand Island, NY) with 6 µl RNase-free water. Probes were not used in the pre-amplification. Cycle parameters were 95°C for 10 min then 18 cycles at 95°C for 15 s and 60°C for 1 min. The ABI 7500 Fast real-time PCR system was used with standard mode (software v2.0.6, Life Technologies).

## Second-Round Pcr

Pre-amplified PCR products were diluted 1000-fold with TE buffer. A 20 µl reaction was prepared for each gene with 1) 1 µl of diluted pre-amplified product, 2) 2 µl of a primer mixture containing each primer for each gene at 8 µM (final concentration of each primer, 800 nM), 3) 2 µl of 2 µM NT probe and 2 µl of 2 µM IS probe (final concentration of each probe, 200 nM), 4) 10 µl TaqMan Universal Master Mix II (No UNG) with 3 µl RNase-free water, and subjected to 40 cycles of PCR using the same cycle parameters as in the pre-amplification. Automatic threshold was used to determine Cq values (Figure 1B, Figure S1 in File S1).

## Calculation Of Gene Expression

To quantify the copy number for each gene NT in a cDNA sample, 1) the [NT Cq - IS Cq]Sample for the unknown sample and the average [NT Cq - IS Cq] of two concentrations of ESM ([NT Cq - IS Cq]ESM) were calculated, 2) The corrected delta Cq was calculated as: [NT Cq - IS Cq]Sample - [NT Cq - IS Cq]ESM, 3) 2(−corrected delta Cq) was multiplied times the known number of input IS copies in the reaction to obtain the gene NT copy number, and 4) each target gene NT value was normalized to the ACTB loading control gene NT value, and presented as target gene NT molecules/106 ACTB molecules (Table 2, Table S1B in File S1).

## Accuracy

The concentration of each stock (purified) IS was determined using densitometric quantification of the appropriately sized peak after electrophoretic separation on the Agilent Bioanalyzer 2100. Then the appropriate volume of each IS was combined to make an ISM. After preparing the ISM, limiting dilution PCR and Poisson analysis were used to determine the true concentration of each IS in the ISM. Specifically, the stock ISM solution was serially diluted to a concentration expected to contain 40, 20, 10, 7, 4, 2, 1, 0.7, 0.4, 0.1 molecules of each IS in each microliter. The expected frequency of reactions with detectable PCR product at each dilution was tested with real time PCR using the pre-amplification method to increase the signal to background ratio (See the above section: Pre-amplification (1st round PCR) and second-round PCR. As an example, when 1 µl of the dilution expected to contain 0.7 molecules per microliter solution was included in the PCR, the expected frequency of positive reactions was 50.3% by Poisson analysis. The nine replicate samples of each dilution for each gene (ACTB, MYC, E2F1, CDKN1A) were measured. For each dilution the observed frequency of positive values (true concentration value) was plotted versus the frequency expected if the concentration determined by Agilent Bioanalyzer 2100 was correct [29].

## Linearity

For each gene, the linearity of the assay was assessed through serial 10-fold dilution of the external standard stock solution (10−11 M NT/10−11 M IS to 10−17 M NT/10−17 M IS) or serial dilution keeping IS constant and diluting NT up to 1/80-fold relative to IS and vice versa. For each dilution series, correlation coefficient (r2) and slope (linearity) were calculated.

## Imprecision

For each gene, the imprecision was measured as the coefficient of variation (CV) of the copy number measured at each dilution used in the linearity test. The CV was calculated as the standard deviation divided by the mean derived from multiple replicate measurements (at least three). The average CV across all dilutions for each gene, and the average CV across all four genes were calculated.

## Robustness And Interference Tests

The effect of intentionally perturbing PCR conditions was assessed. Conditions altered included PCR volume and concentration of primer, probe, or EDTA [30]. Samples used for this analysis were cDNA reverse transcribed from non-FFPE treated benign lung tissue RNA (Life Technologies, Grand Island, NY) or FFPE-processed, surgically-removed, malignant lung tissue sample 1 or 8 RNA (SM1, SM8).

### Edta Concentration Variation

The effect of variation in PCR EDTA concentration on MYC and ACTB measurement was assessed in triplicate 20 µl PCR assays containing non-FFPE, benign lung cDNA pre-amplified with ISM. EDTA concentrations tested were 0, 0.5, 1, 1.4, 1.8, 2.2, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6 and 4.0 mM.

## Effect Of Esm On Quality-Control

The effect of variation in fluorescence intensity on reliability of measurement was tested by varying ratio of [labeled probe]/[unlabeled probe] keeping [total probe] in the PCR constant at 200 nM. PCR assays were conducted for MYC and ACTB measurement in non-FFPE, benign lung cDNA pre-amplified with ISM. The IS labeled probe concentration in the PCR was kept constant while NT labeled probe was diluted with unlabeled probe to 200, 150, 100, 80, 40, 20, 10, 5, 0 nM or vice versa. Unlabeled probe was obtained from Life Technologies, Grand Island, NY.

Inter-day experimental variation without or with ESM was tested in FFPE sample SM8 cDNA in seven PCR reactions on five different days. The automatically selected Cq values were used to measure MYC/106 ACTB.

## Statistical Analysis

The transcript abundance value (target gene molecules/106 ACTB molecules) for each LCDT gene was measured in triplicate and variation was measured as the CV. We used the Student’s t-test to determine a significant (P<0.05) difference in mean LCDT value of the malignant group compared to the benign group. Levene’s test was used to assess the equality of variances in different samples for Student’s t-test using R program (v 2.15.2). The receiver operator characteristic (ROC) plot was generated by GraphPad Prism 6.

# Results

## Analytical Validation Of Primers, Probes, And Internal Standard Mixtures

### Primer Efficiency And Specificity

Primer efficiency was determined by PCR analysis of serially diluted IS. For each gene, at the dilution predicted to contain a single molecule of IS based on Agilent 2100 concentration analysis, the fraction of measured replicates that had detectable PCR product was consistent with the frequency predicted by Poisson analysis (see Accuracy section below). The Poisson analysis results support the conclusion that the IS concentration was accurate and that the primers had efficiency necessary to generate a detectable signal from a single molecule after 40 cycles [29].

### Probe Specificity

For the first E2F1 assay design, the NT probe had >10% non-specific binding, so it was re-designed to increase the number of changes in IS compared to NT from four to six base pairs. After the re-design of the E2F1 IS and its respective probe, non-homologous (non-specific) binding was <1% for both NT and IS probes for all genes, more than meeting our threshold acceptance criteria.

### Internal Standards Mixture Accuracy

After the IS were combined into the ISM, the ISM was serially diluted beyond the level expected to contain a single molecule in a PCR assay, and the IS for each of the four genes was PCR-amplified in the PCR assays containing each ISM concentration. The observed frequency of the positive result was highly correlated (R2 = 0.94) with the expected positive frequency predicted by Poisson analysis (Figure 2, Figure S2 in File S1), indicating that the intended concentration for each IS in the ISM was accurate.

## Analytical Validation Of The Competitive Multiplex Two Color Real-Time Method

### Linearity

The linearity of the two-color fluorometric assay was determined by analysis of serial dilutions of synthetic NT and IS for each gene. In a serial dilution of the stock ESM (a 1/1 mixture of NT/IS) over seven orders of magnitude (from 10−11  M through 10−17  M), the correlation coefficient for the measurement of each gene relative to its respective IS was >0.99, and the average slope for the signal-to-analyte response was 1.0±0.05 (Figure 3A, B, Figure S3 in File S1).

To more stringently assess linearity, the NT was serially diluted relative to a constant IS concentration of 10−12 M and the IS was diluted relative to a constant NT concentration of 10−13 M. In the dilutions with NT/IS or IS/NT ratio of <10, the average slope for the four genes (ACTB, E2F1, MYC, CDKN1A) was 1.0±0.10 in each set of dilution series. At dilutions with NT/IS or IS/NT >10, there was a slight deviation of the slope from 1.0 (Figure 3C–E, Figure S4 in File S1, S5 in File S1).

### Imprecision

The imprecision for measurement of the LCDT genes was measured among both the ESM dilution samples and the NT/IS dilution samples.

At each serial 10-fold dilution of ESM (10−11 M NT/10−11 M IS to 10−17 M NT/10−17 M IS), the average coefficient of variation (CV) for measurement of each of the four genes was <10% for >60 molecules input (10−11 M NT/10−11 M IS to 10−16 M NT/10−16 M IS) and <30% for >6 molecules input (10−11 M NT/10−11 M IS to 10−17 M NT/10−17 M IS) with little inter-gene variation (Table S2 in File S1).

Among the NT/IS dilution samples, the average CV among the four LCDT genes was calculated for different ranges of dilution. For an NT dilution from 1/1 to 1/10-fold relative to a constant IS, the average CV among the four genes was 12%. At dilutions beyond 1/10, the CV increased, but from 1/1 to 1/80 NT dilution the average CV was only 20% (Table S3 in File S1). Similar results were observed for an average CV for each of the four genes in the IS dilution relative to a constant NT.

### Robustness And Interference Testing

Changing the volumes and/or the concentrations of primers or probes did not lead to significant differences in expression measurement of MYC or ACTB in FFPE SM1 cDNA with or without pre-amplification (Figure S6 in File S1).

As EDTA concentration was increased, Cq value of each of the four analytes tested in non-FFPE, pre-amplified, benign lung cDNA (MYC IS and NT, ACTB IS and NT) increased, ultimately resulting in no signal (Figure 4). However, the MYC NT and ACTB NT values calculated relative to their respective IS were constant, and due to the loss of signal for IS at highest EDTA concentration, no false negative values were reported.

### Use Of Esm To Control For Variation In Fluorescent Labeling Of Probe And Selection Of Threshold

The specific activity of probe labeling with fluor (i.e., [labeled probe]/[total probe]) may vary between experiments due to freezing and thawing of probes or due to lot differences, the effect of variation in fluorescence specific activity on measurement of MYC in benign, non-FFPE lung cDNA was tested. As the labeled probe concentration decreased in the reaction, the Cq increased (Figure 5A, C). However, this potential source of analytical variation was controlled by correcting the measured lung sample [NT Cq - IS Cq] values relative to the ESM [NT Cq - IS Cq] values (Figure 5B, D). The ESM contained a known 1∶1 concentration of each NT and IS that was constant among experiments, any variation in the observed ESM [NT Cq - IS Cq] relative to the expected value of 0 was attributable to variation in experimental conditions, including fluorescence intensity.

Another potential source of inter-experimental variation is inter-experimental variation in selection of Cq threshold. Even when the Auto Cq mode is used to select automatically the optimal Cq threshold, there was large inter-experimental variation in NT/IS Cq difference based on amplification plot and amount of cDNA loaded (Figure 5E). Thus, whether the threshold was selected through the automatic method or the manual method, there was day-to-day variation in the selected Cq threshold setting. However, because the inter-experimental variation in the Cq threshold had the same effect on sample Cq and ESM Cq, inter-experimental variation in sample Cq was controlled by ESM Cq as described in the previous paragraph. For example, MYC/106 ACTB was measured in FFPE sample SM8 cDNA in seven PCR replicates on five different days and the Cq threshold value automatically selected in each PCR was different (Figure 5E) resulting in high CV of 0.99. However, with the ESM correction, the CV of measured MYC/106 ACTB was reduced to 0.32 (Table 2).

## Fitness For Purpose Testing In Ffpe Samples

The histomorphologic diagnosis of benign or malignant FFPE samples used in this study is presented in Table S4 in File S1. The RNA yield and purity are presented in Table S5 in File S1.

### Optimization Of Ffpe Reverse Transcription

Efficiency of RT with GSP or RHP was assessed in three (two malignant and one benign) surgical FFPE samples (SM1, SM2, SB1). The average yield of cDNA from 1 µg RNA was more than 50-fold higher with GSP. Based on this, analysis of FFPE samples was conducted with GSP in RT. The RT yield was increased another 4.6-fold by increasing RNA in RT to 5 µg.

### Effect Of Pre-Amplification

Results for analysis of LCDT genes in sample SM1 with or without pre-amplification were compared to quantify the increase in signal relative to background resulting from pre-amplification and to confirm that it did not significantly alter the result. Importantly, for each gene the signal was increased (Cq decreased) with pre-amplification. Specifically, Cq value decreased for ACTB, MYC, E2F1, and CDKN1A by 9, 10, 9 and 10, respectively, following pre-amplification and 1000-fold dilution of the pre-amplification product prior to second round amplification. Yet, because each target was measured relative to a known number of its respective IS molecules, the value measured with the pre-amplification method was not significantly different from that measured with the no pre-amplification (Figure S6 in File S1).

### Analysis Of Myc, E2F1, Cdkn1A And Actb In Ffpe Samples

The comparison of the LCDT index in benign and malignant surgical FFPE samples is presented in Figure 6A, and the ROC curve analysis is presented in Figure 6B. Based on the linearity and imprecision results, for analysis of clinical samples, we chose to restrict the conditions for calculation of results to1/10 to 10/1-fold difference between the NT and the IS.

The LCDT optimal cut-off value had 90% specificity and 90% sensitivity to classify samples as cancer or non-cancer, similar to previous reports with non-FFPE fine needle aspirate (FNA) samples [31], [32]. The ROC area under the curve was 0.93 with a 95% confidence interval of 0.82 to 1.04 and the P-value of Student’s t-test for stratification of malignant from non-malignant was 0.0061. The average CV among surgical FFPE samples for measurement of MYC, E2F1, and CDKN1A relative to ACTB was 0.27, 0.41, and 0.26, respectively (Table 3). These data confirm fitness for purpose of this optimized LCDT test in FFPE samples.

# Discussion

Here we report the analytical validation and fitness for purpose testing of an RT-qPCR method suitable for reliable analysis of FFPE samples. Key features of this optimized method are highlighted here.

## Internal Standards Provide Quality Control

The endogenous amount (NT) of each of multiple genes was measured relative to a known number of respective IS molecules. Each IS amplified with the same efficiency as the NT, and this controlled for inter-sample variation in PCR interfering substances and inter-experimental variation in PCR reagent quality or quantity or thermal cycling conditions as previously described [30], [33], [34]. Key to the elimination of inter-experimental variation when measuring multiple genes was use of the same ISM comprising a known concentration of IS for each of the genes to be measured [16]. The ISM was both stable and simple and inexpensive to prepare.

## Two-Color Fluorometric Real-Time Pcr

For reliable analysis of FFPE samples, it is important to use primers that yield short PCR products (e.g. 60−80 base pairs). Such products are readily quantified using real-time PCR. Competitive PCR analysis involves simultaneous quantification of each target gene NT and its respective IS. To do this by real-time PCR requires inclusion of two different sequence-specific probes in the same PCR reaction, each with a different fluor [12], [13], [35]. Calculating each NT analyte relative to its respective IS requires an additional measurement, and, in some studies, this may be associated with a tendency to increased imprecision [36]. However, as previously reported, the imprecision observed in this study was less than 10% except for the measurement of very low copy numbers (<60 copies), at which point imprecision is determined largely by the natural law governing stochastic sampling variation rather than method-specific characteristics [16].

## Esm Controlled For Inter-Run Variation In Probe Fluorescence

Multiple different factors may cause inter-experimental variation in fluor signal detection including variation in fluor concentration (Figure 5A–D), variation in cycle threshold setting (Figure 5E), and as yet unknown sources. The use of the ESM significantly reduced these sources of inter-experimental variation (Table 2). In addition to use in multiple analyte assays, such as the one presented here, this approach is applicable to single analyte two-color fluorometric assays [12], [13] and may demonstrate similar utility if so employed.

## Multiplex Pre-Amplification Was Enabled By Use Of Internal Standards

Using IS in conjunction with multiplex pre-amplification enabled reliable analysis of even lowly expressed genes in very small amounts of cDNA. Specifically, it was possible to determine the starting number of NT molecules, even after two rounds of PCR, by measuring the NT signal relative to the IS signal (Figure S6 in File S1). This is because a known number of its respective IS molecules was included in the pre-amplification reaction for each gene, and because the NT and IS amplified with the same efficiency [20].

Competitive multiplex pre-amplification improved measurement of FFPE samples in the following ways. First, cDNA consumption was reduced. In the multiplex pre-amplification, reduction in cDNA consumption depends on the number of targets and reference genes. Thus, in this study involving only three target genes and a single reference gene, cDNA consumption was reduced four-fold. We have previously conducted competitive multiplex pre-amplification with 96 genes, and this enabled a marked reduction in cDNA required for measurement of each gene [20], [37].

Second, pre-amplification markedly increased signal above the background signal typically observed in the no template control at 35 Cq. Specifically, with one round of PCR (no pre-amplification) the Cq for each NT and IS ranged from 20–35. In contrast, using pre-amplified and 1000-fold diluted samples, the Cq for each NT and IS after a second round of PCR ranged from 11–26. The amount of dilution of first round amplification product can be reduced if necessary to ensure sufficient signal in the second round for very low input of sample cDNA. Further, for analysis of FNA FFPE samples with very low input cDNA, the higher signal following pre-amplification is associated with better precision than no pre-amplification (data not shown).

## Gene Specific Reverse Transcription

We recently reported that use of gene specific priming in RT increases yield of cDNA by 10–100 fold compared to oligo dT or random hexamer priming when applied to RNA from human peripheral blood leukocytes [26]. Because FFPE treatment typically reduces yield of cDNA from RNA by 100-fold, we evaluated the utility of gene specific priming relative to random hexamer priming to increase signal. The more than 50-fold increase in cDNA yield with gene specific priming RT compared to random hexamer priming RT observed in this study is consistent with our results from the prior study with leukocytes.

## Fitness Of Method For Ffpe Sample Analysis

Fitness of this two color fluorometric method for analysis of FFPE samples was evaluated by measuring a previously described test for lung cancer diagnosis for non-FFPE FNA samples [31], [32] in a small number of surgical FFPE benign and malignant lung samples. The results support the utility of this optimized method for analysis of FFPE samples. Specifically, imprecision was acceptable, and the optimal cut-off for the LCDT had similar accuracy in separating benign from malignant compared to what was reported previously for fresh FNA samples [31], [32]. These results support the conclusion that the method presented here is suitable for use in a planned clinical validation trial in which the LCDT will be evaluated for utility to augment cytomorphology in analysis of FNA cell block FFPE samples.

## Summary

Successful analytical validation described here of the quality-controlled two-color fluorometric real-time PCR method for analysis of the LCDT in FFPE samples supports use of this approach in development and implementation of promising RT-qPCR based diagnostic tests that require analysis of RNA extracted from FFPE samples.

