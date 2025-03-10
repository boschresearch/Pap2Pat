# DESCRIPTION

## BACKGROUND

Because cancer and many other diseases have a genetic basis, and because a patient's response to a particular drug or treatment can be influenced by the patient's genetic makeup, researchers have undertaken the task of genetically characterizing patient tissue samples (including tumor samples), cell lines, and xenografts.

A population of organisms will contain several variants (alleles) of a given gene. Alleles can differ from one another at single basepair. These single basepair differences are called single nucleotide polymorphisms (SNPs), and several can be present in a single gene. High-throughput genotyping methods using high-density nucleic acid arrays and other methods can accurately genotype (i.e., determine the nucleotide(s) present) hundreds or thousands of SNPs in a genetic sample in parallel to provide an unequivocal molecular fingerprint of the genetic sample. The somatic cells of diploid organisms have two copies of each autosomal gene and many high throughput genotyping techniques are be sensitive enough to analyze a SNP to determine if an individual is homozygous for a first allele, homozygous for a second allele, or heterozygous (i.e., possesses one copy of each allele). The results of this analysis can be used for research and for making diagnostic and therapeutic decisions.

The value of genetic analysis for research, diagnosis and treatment depends on the accuracy of the analysis. For example, potential therapeutic agents for treatment of cancer are sometimes identified by screening in cancer cells lines. Thus, it is crucial that the cell lines used in such analysis are properly identified. In addition, normal and tumor samples taken from cancer patient are used in staging, diagnoses, selecting treatments and monitoring the effect of treatments. Thus, the accurate identification of samples is extremely important because mis-identification can lead to an incorrect diagnosis or selection of a sub-optimal therapy.

Methods are available for genotyping hundreds or thousands of SNPs in parallel, and these methods can be used for proper identification of samples. However, particularly where a large number of samples must be analyzed, the genotyping of hundred or thousands of SNPs and the analysis of the resulting data can prove to be time-consuming and complex. Thus, it would be desirable to identify a manageable number of SNPs that, taken together, have the power to discriminate among and identify genetic samples.

## SUMMARY

Described herein are methods and tools for accurately identifying and/or distinguishing biological samples containing genetic material, e.g., cell lines, tissue samples, blood samples, and the like. The methods are based, at least in part, on statistical analysis of genetic data, e.g., SNP genotype calls. When applied to particular sample datasets, e.g., a particular group of genetic samples, the methods described herein permit the identification of a relatively small set of SNPs that can be used as a powerful tool for identifying and/or distinguishing samples containing genetic material. The methods described herein permit the identification of sets of SNPs that are far more useful for distinguishing biological samples than much larger sets of randomly selected SNPs that are commonly used for genetic analysis. Because the number of SNPs required for genetic analysis is relatively small when using SNPs selected as described herein, the genetic analysis is very cost effective, particularly when compared to analysis that uses many hundreds or thousands of randomly selected SNPs, most of which are essentially useless for identification and discrimination of samples.

The methods described herein for selecting SNPs are particularly powerful because they can be used to select a set (panel) of SNPs that are tailored to the type of samples being analyzed. In many cases the actual SNPs selected will depend on the samples one wishes to analyze (e.g., whether the samples are from normal tissue or tumor tissue, the characteristics of the population of individuals from which the samples are obtained). For example, the methods described herein can be used to identify a set of SNPs that are useful for discriminating among the various cell types in the NCI60 cell lines. The methods described herein can also be used to identify a set of SNPs that are useful for discriminating among many thousands of cancer tumor samples. It is possible that the sets of SNPs selected in these two cases will not completely overlap. Indeed, there might be little overlap. In the methods described herein, actual analysis of the samples to be analyzed (or a subset of the actual samples to be analyzed) is used to determine which SNPs should be used for discrimination and identification of samples. This is as opposed to many other techniques, which rely on a priori selection methods.

Because the number of SNPs used in a SNP panel identified as described herein is relatively small, analysis of a genetic sample at each of the SNPs in a panel produces a result that can be thought of as a genetic barcode that identifies the biological sample. The barcode itself is series of genotypes at the SNPs in the panel, e.g., homozygous T at SNP 1, homozygous G at SNP 2, heterozygous A/T at SNP 3, etc. This genetic bar code can be compared to other genetic barcodes stored in a database. Each stored (or reference) genetic barcode is generated by analysis of an associated genetic sample. The genetic barcode (SNP genotype pattern) generated from a test genetic sample can be compared to the reference barcodes in order to identify a reference genetic barcode that exactly matches (or nearly matches) the test barcode. The test sample is very likely to be identical to (or genetically very closely related to) the genetic sample associated with matching barcode. Of course, the degree of confidence in the determination can depend on the SNPs analyzed and the number of SNPs analyzed. For SNPs of equal ability to discriminate among genetic samples, the larger number of SNPs analyzed, the great the confidence that a perfect match between two SNP panels means that the associated genetic samples are identical.

As noted above, the precise SNP panel used can vary from one application to another. Moreover, the number of SNPs in the panel can vary depending one the degree of confidence needed in the sample identification. For example, a first panel could be used to distinguish among NCI60 cell lines with a given degree of confidence. A second, larger panel could be used to distinguish among NCI60 cell lines with a far higher degree of confidence. The second panel could contain all of the SNPs in the first panel as well as additional SNPs. A different panel might be used to distinguish among samples in a collection of patient tissue samples, e.g., a collection of patient tissue samples used in a particular drug screening program.

Once a SNP panel has been identified, for example by analyzing a subset of a collection of biological samples, test biological samples can be analyzed to determine the genotype present at each SNP using techniques that are standard in the art. The vast majority of SNPs have two possible alleles and such SNPs are useful in the methods described herein. Thus, genetic material (DNA or cDNA) is obtained from a test biological sample and each selected SNP (i.e., each SNP in the panel) is analyzed to determine whether the test biological sample is homozygous for the first of the two possible alleles, homozygous for the second of the two possible alleles or heterozygous for the two possible alleles. In some cases, the analysis will not even require physically determining the genotype present at certain SNPs since the test biological sample will have been previously analyzed at some or all of the SNPs in the panel. Thus, the techniques described herein can be used to reanalyze samples that have already been genotyped at thousands of SNPs. In this reanalysis, only a subset of the informative SNPs, i.e., those identified by the techniques described herein are considered.

Described herein are methods for identifying at least one SNP useful for analyzing a genetic sample. The methods include:


- - (a) obtaining a population of selected genetic samples;
  - (b) separating, e.g., randomly dividing, the population of genetic
    samples into a first subpopulation of genetic samples including a
    portion of the genetic samples and a second subpopulation including
    the remaining genetic samples;
  - (c) analyzing the genotype at each SNP of a plurality of SNPs for
    each genetic sample in the first subpopulation of genetic samples to
    determine for each SNP:
    - i) N_(aa), the number of genetic samples in which the SNP is
      homozygous for a first allele,
    - ii) N_(bb), the number of genetic samples in which the SNP is
      homozygous for a second allele, and
    - iii) N_(ab), the number of genetic samples in which the SNP is
      heterozygous for a first and a second allele;
  - (d) for the genetic samples in the first subpopulation, ranking each
    SNP of the plurality of SNPs by how nearly the ratio
    N_(aa):N_(bb):N_(ab) matches the ratio 1:1:2 to provide a ranking of
    SNPs;
  - (e) analyzing the genotype at each SNP in the plurality of SNPs for
    each genetic sample in the second subpopulation of genetic samples
    to determine for each SNP:
  - i) N′_(aa), the number of genetic samples in which the SNP is
    homozygous for a first allele,
  - ii) N′_(bb), the number of genetic samples in which the SNP is
    homozygous for a second allele, and
    - iii) N′_(ab), the number of genetic samples in which the SNP is
      heterozygous for a first and a second allele;
  - (f) for the genetic samples in the second subpopulation, determining
    how closely the ratio N′_(aa):N′_(bb):N′_(ab) matches the ratio
    1:1:2 to provide a score for each SNP;
  - (g) designating a SNP that both ranks above a pre-determined cut-off
    in the ranking when analyzed in the first subpopulation and has a
    score above a pre-determined score when analyzed in the second
    subpopulation as a candidate SNP;
  - (h) repeating steps (b)-(g) at least two times, each time
    designating one or more SNPs as a candidate SNP to generate at least
    two groups of candidate SNPs; and
  - (i) identifying a SNP designated as a candidate SNP at least two
    times as a SNP useful for analyzing a genetic sample.

As noted above, the SNPs identified as useful for analyzing a genetic sample are particularly useful for analyzing a genetic sample that is (or is suspected of being) from the same biological source as a genetic sample in the population of selected genetic samples. Thus, the identified SNPs are particularly useful for determining whether a test genetic sample is from the same biological source as a genetic sample that is a member of the population of selected genetic samples. For example, the population of selected genetic samples can all be contributed by cancer patients at a particular institution. This population of genetic samples can be used to identify a group of SNPs, i.e., a SNP panel. The SNPs in this SNP panel will be particularly useful for determining whether a test genetic sample is from a patient that contributed to the population of genetic samples. In some cases, the identified SNPs can be used to analyze genetic samples that are not the same as or closely related to a genetic sample that is a member of the population of selected genetic samples.

Various statistical methods known to those of ordinary skill in the art can be used to score SNPs by how nearly the ratio Naa:Nbb:Nab matches the ratio 1:1:2. In addition, various statistical methods can be used to score SNPs by how nearly the ratio Naa:Nbb:Nab matches the ratio 1:1:2 to provide a ranking of SNPs. In both cases, the goal is to select those SNPs where the ratio Naa:Nbb:Nab is extremely close to or exactly 1:1:2. For example, the ratio can differ by less than 5%, 3%, 2%, 1%, 0.5%, 0.1%, 0.01% or 0.001%.

In various embodiments of these methods, steps (b)-(g) can be repeated at least 5 or 10 or more times and wherein a SNP designated as a candidate SNP at least 10 times is identified as a SNP useful for analyzing a genetic sample. Of course, the steps can be repeated fewer or more times (e.g., 5, 20, 30, 40, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, or 1000 or more times), and a SNP designated as a candidate SNP fewer or more than 10 times (e.g., 5, 20, 30, 40, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, or 1000 or more times) is identified as a SNP useful for analyzing genetic samples. Generally, the number of times that the steps are repeated dictates how often a SNP must be designated as a candidate SNP. Thus, if the steps are repeated 1,000 times, SNPs designated as candidates 400, 500, 600, 800, or more times are identified as being useful. Generally, it will be desirable to use SNPs that are designated in at least 40%, 45%, 50%, 60%, 75%, 90%, or even 100% of the repetitions of the selection. A group of identified SNPs forms a potential SNP panel. Some or all of the SNPs in such a panel can be used together to analyze genetic samples.

The methods described herein can be used to identify multiple useful SNPs, e.g., at least 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, or 1000 useful SNPs. In general, when there are multiple rounds of steps (b)-(g), the SNPs designated most frequently are often the most useful for analyzing a genetic sample. Of course, this is not always the case. Some frequently designated SNPs are less useful for a variety of reasons. For example, a frequently designated SNP can be difficult or impractical to genotype. Thus, a SNP panel can exclude certain frequently designated SNPs.

Also described are methods for identifying a panel of SNPs useful for analyzing a genetic sample. The methods include:


- - (a) using a method described herein to identify a plurality of SNPs
    useful for analyzing a genetic sample;
  - (b) excluding at least one of the plurality of SNPs; and
  - (c) identifying the remaining SNPs as a panel of SNPs useful for
    analyzing a genetic sample.

In some cases at least one SNP located in an intron is excluded, at least one SNP located in a region subject to loss of heterozygosity is excluded, at least one SNP having a heterozygosity rate that differs more than 2% between Caucasian and Asian populations is excluded, at least one SNP having a heterozygosity rate that differs more than 2% between Caucasian and African American populations is excluded, and/or at least one SNP having a heterozygosity rate that differs more than 2% between Asian and African American populations is excluded.

Also described herein are methods for analyzing a genetic sample. The methods include:


- - (a) obtaining a first genetic sample;
  - (b) analyzing the genotype of the genetic sample at each SNP in a
    set of SNPs identified as useful for analyzing genetic samples,
    wherein each SNP in the set of SNPs was identified as useful using a
    method described herein; and
  - (b) comparing the genotype of the genetic sample at each SNP in the
    set of SNPs to the genotype of a second genetic sample at each SNP
    in the set of SNPs to determine if the first and second genetic
    samples are the same or different.

Described herein are methods for determining whether a test genetic sample is genetically related to a selected cell. The methods include:


- - (a) obtaining a test genetic sample;
  - (b) analyzing the test genetic sample to determine the genotype of
    at least 10 SNPs selected from the group consisting of rs967968,
    rs718015, rs654559, rs723725, rs487616, rs1935571, rs2414908,
    rs1890035, rs554653, rs2254896, rs722152, rs1951096, rs953654,
    rs1157158, rs953183, rs2203657, rs2249248, rs1515561, rs1564935,
    rs1876054, rs1342947, rs2868931, rs1543193, rs951300, rs3847126,
    rs3847896, rs1986626, and rs1509577 to generate a test SNP pattern
    including the identity of the genotype of the at least 10 SNPs;
  - (c) comparing the test SNP pattern to a plurality of reference SNP
    patterns to identify the reference SNP pattern that matches the test
    SNP pattern, wherein each reference SNP pattern is associated with a
    selected reference genetic sample and comprises the identity of the
    genotype of the at least 10 SNPs for the associated genetic sample;
    and
  - (d) determining that the test genetic sample is genetically related
    to a reference genetic sample associated with the reference SNP
    pattern that matches the test SNP pattern at a predetermined number
    of SNPs, e.g., at least 60%, 70%, 80%, 90%, or 100% of the SNPs, in
    the test SNP pattern. A match with a higher percentage of SNPs will
    provide a result of identity with greater confidence. In some
    embodiments, the reference SNP pattern matches at least 8 SNPs in
    the test SNP pattern.

In some cases, the methods include analyzing the nucleic acid sample to determine the genotype no fewer than 20 polymorphic sites selected from the group consisting of rs967968, rs718015, rs654559, rs723725, rs487616, rs1935571, rs2414908, rs1890035, rs554653, rs2254896, rs722152, rs1951096, rs953654, rs1157158, rs953183, rs2203657, rs2249248, rs1515561, rs1564935, rs1876054, rs1342947, rs2868931, rs1543193, rs951300, rs3847126, rs3847896, rs1986626, and rs1509577.

In most cases, it will be desirable to determine that a test genetic sample and a reference genetic sample are likely to be identical if all of the genotype calls for the SNPs in the panel are identical.

In various embodiments, the test genetic sample is determined to be genetically related to the reference genetic sample associated with the reference SNP pattern that matches the test SNP at all of the SNPs in the test SNP pattern; at least one of reference genetic samples includes genetic material from an NCI-60 cell line; and/or the reference genetic samples include genetic material from at least 40 of the NCI-60 cell lines.

Also described herein are methods for identifying at least one single nucleotide polymorphism (SNPs) useful for distinguishing genetic samples. The methods include:


- - (a) obtaining a population of genetic samples;
  - (b) analyzing each genetic sample at each SNP of a plurality of SNPs
    to determine:
    - i) N′_(aa), the number of genetic samples in which the SNP is
      homozygous for a first allele,
    - ii) N′_(bb), the number of genetic samples in which the SNP is
      homozygous for a second allele, and
    - iii) N′_(ab), the number of genetic samples in which the SNP is
      heterozygous for a first and a second allele; and
  - (c) identifying a SNP where the ratio N′_(aa):N′_(bb):N′_(ab) is
    approximately 1:1:2 as a SNP useful for distinguishing genetic
    samples.

Genetic material obtained from biological samples can be analyzed at the selected SNPs by any of a variety of methods. For example, pairs of PCR primers can be used to make allele calls at each of the selected SNPs. However, any method for genotyping SNPs can be used.

Because the methods described herein identify a relatively small number of SNPs that are useful for analyzing a group of biological samples, analysis of biological samples is rapid and cost effective. The number of SNPs analyzed is relatively small because the methods described herein are capable of identifying the SNPs that are most informative for a given set of biological samples.

The SNP panel identification assays (SPIAs) described herein can be used to solve a variety of problems, including, but not limited to: determining whether a given cell line is identical to another cell line; identifying identical samples in a set of patient samples; confirmation of the identity of passaged cell lines, confirmation of the identity of passaged xenografts; and matching normal and tumor cell samples from a single patient. Put simply, the methods and tools described herein can be used in any situation where it is necessary to identity a genetic sample. Thus, the methods described herein can be used to determine whether two test biological samples are the same or different. The methods described herein can be used to determine whether a test biological sample is identical to a reference biological sample. Thus, a set of biological samples can be analyzed to determine a genetic barcode for each sample, thereby creating a reference library of genetic barcodes. A test biological sample can be analyzed to produce a genetic bar code which can then be compared to a library of reference bar codes to identify the test biological sample.

In some cases a first, smaller SNP panel is used to analyze a sample or set of samples. If this first SNP panel proves to be adequate for sample identification, no further analysis need be conducted. However, if some of the results are ambiguous or if a higher degree of confidence is required, the samples can be analyzed with a larger SNP panel.

As explained in greater detail below, the analytical methods described herein were first applied to the analysis of NCI60 Cell Lines. These cell lines are very commonly used in cancer research. For example, The National Cancer Institute maintains a database of microarray expression data for NCI60 Cell Lines as well a database containing information on toxicity of approximately 70,000 compounds for cells of NCI60 cell lines. The analysis described below provides a means for identifying a relatively small number of SNPs that can be used to differentiate and identify cells of the NCI60 cell lines. This analysis revealed that MDA-MB435, which is identified as a breast cancer cell line is genotypically identical to the M14 melanoma cell line. In addition, at least two breast cancer cell lines among the NCI 60 Cell Lines exhibit genetic identity with the MCF-7 cell line. Such mis-identification, inadvertent cross-contamination or errors in sample identification can have a profoundly adverse effect on experimental results and their interpretation. For example, a search of the National Library of Medicine's PubMed database identified more that 400 publications that erroneously identify MDA-MB435 as a breast cancer cell line.

In another aspect, the present invention features a database comprising a plurality of records. Each record includes at least one, two or preferably all of the following: data on the identity of a number of SNPs, e.g., at least two, preferably at least three, four, or more SNPs, identified using a method described herein, and optionally a source identifier that indicates the cell, tissue, or subject from which the biological sample was taken.

Also included is a machine-readable medium that stores software implementing the methods described herein. As used herein, “machine-readable media” refers to any medium that can be read and accessed directly by a machine, e.g., a digital computer or analogue computer. Non-limiting examples of a computer include a desktop PC, laptop, mainframe, server (e.g., a web server, network server, or server farm), handheld digital assistant, pager, mobile telephone, and the like. The computer can be stand-alone or connected to a communications network, e.g., a local area network (such as a VPN or intranet), a wide area network (e.g., an Extranet or the Internet), or a telephone network (e.g., a wireless, DSL, or ISDN network). Machine-readable media include, but are not limited to: magnetic storage media, such as floppy discs, hard disc storage medium, and magnetic tape; optical storage media such as CD-ROM; electrical storage media such as RAM, ROM, EPROM, EEPROM, flash memory, and the like; and hybrids of these categories such as magnetic/optical storage media. A variety of data storage structures are available to a skilled artisan for creating a machine-readable medium having recorded thereon the data described herein. The choice of the data storage structure will generally be based on the means chosen to access the stored information. In addition, a variety of data processor programs and formats can be used to store the information of the present invention on computer readable medium.

Unless otherwise defined, all technical and scientific terms used herein have the same meaning as commonly understood by one of ordinary skill in the art to which this invention belongs. Methods and materials are described herein for use in the present invention; other, suitable methods and materials known in the art can also be used. The materials, methods, and examples are illustrative only and not intended to be limiting. All publications, patent applications, patents, sequences, database entries, and other references mentioned herein are incorporated by reference in their entirety. In case of conflict, the present specification, including definitions, will control.

Other features and advantages of the invention will be apparent from the following detailed description and figures, and from the claims.

## DETAILED DESCRIPTION

To identify a reasonable number of SNPs (indexes) such that NSNP-nupla CallsIND is essentially unique for each sample it was first necessary to determine how many SNPs would be needed (NSNP). This, of course, depends on the number of samples one wishes to distinguish. Most SNPs have two possible alleles (i.e., one of two possible nucleotides are present at the polymorphic position). Thus, there are three possible states (allele calls) for each SNP. If one of the two possible nucleotides at a given SNP is referred to as “A” and the other is referred to as “B,” then there are three possible allele calls: AA, BB and AB. For simplicity in the formulas below, these genotypes are referred to as A, B and AB.

NSNP MIN, i.e., the minimum number of SNPs needed, depends on how many samples one aims to distinguish.

Nsample=NStatesN

NSNP=logN(NSample)=logN10*log10NSample

NStates=3, S={A, B, AB}.

The results of this calculation are shown in FIG. 2.

In some embodiments, the number of SNPs actually used in the analysis will not generally be a great as required for the highest level of certainty. Instead, the number of SNPs used will depend on the number which can be analyzed in an efficient manner and the degree of certainty required. However, the number of SNPs that should be analyzed will generally be somewhat larger than the theoretical minimum in order to take into account the occurrence of no calls and other vagaries of actual data

Desirable SNPs are those that are highly variable across the population of samples one wishes to analyze, e.g., those which have minor allele frequency equal to about 0.5 and heterozygosity equal to about 0.5. Thus, a SNP that can be G or C, but is homozygous G (i.e., G/G) in 90% of the samples is not particularly useful. However, a SNP that can be C or G and is homozygous G in more than ⅕ of the samples and homozygous C in more than ⅕ of the samples is more useful.

At the outset two selection criteria were considered. The first criteria was based on an equally weighted distribution (EWD), where ⅓ of the calls are A, ⅓ of the calls are B. and ⅓ of the calls are AB, and there is a lower boundary on the call rate. This criteria optimizes the probability of having different calls. The second criteria is based on the Harvey-Weinberg equilibrium (HWE) where ¼ of the calls are A, ¼ of the calls are B, and ½ of the calls are AB, there are elastic boundaries, and there a lower boundary on the call rate. This criteria respects expected biological distribution.

165 cell lines were selected to be analyzed using both techniques in order to determine which method yields more reliable results. The analysis was begun with this dataset of 165 cell lines. To eliminate pairs of cell lines that appeared to be duplicates, during the selection process of our SNP panel, the distance between all possible pairs of cell lines was evaluated using the Affymetrix, Inc. GeneChip® Human Mapping 50K Xba 240 array, which permits analysis of 50,000 SNPs.

A similarity measure was used to evaluate the distance between samples for identity measurements. The distance metric for this analysis is proportional to the number of mismatches. It is defined as:

\({{D\left( {{{CL}\; 1},{{CL}\; 2}} \right)} = {\frac{1}{{vN}_{SNPs}}{\sum\limits_{i = {1\mspace{11mu} \ldots \mspace{11mu} N_{SNPs}}}{d\left( {{{cl}\; 1_{i}},{{cl}\; 2_{i}}} \right)}}}},{where}\)
\({d\left( {{{cl}\; 1_{i}},{{cl}\; 2_{i}}} \right)} = \left\{ \begin{matrix}
{{1\mspace{14mu} {if}\mspace{14mu} {cl}\; 1_{i}} \neq {{cl}\; 2_{i}}} \\
{{{0\mspace{14mu} {if}\mspace{14mu} {cl}\; 1_{i}} = {{{cl}\; 2_{i}\mspace{14mu} {or}\mspace{14mu} {cl}_{i}} = {NoCall}}},}
\end{matrix} \right.\)

NSNPs is the number of SNPs you are considering, and

νNSNPs=Card(T), T={i:cl1i≠NoCall ∩cl2i≠NoCall}

### Therefore: νNSNPs<=NSNPs.

Different weights can be included for different type of mismatches:

\({d\left( {{{cl}\; 1_{i}},{{cl}\; 2_{i}}} \right)} = \left\{ \begin{matrix}
{{w_{ErType}*1{\mspace{11mu} \;}{if}\mspace{14mu} {cl}\; 1_{i}} \neq {{cl}\; 2_{i}}} \\
{{0\mspace{14mu} {if}\mspace{14mu} {cl}\; 1_{i}} = {{cl}\; 2_{i}}}
\end{matrix} \right.\)

Every mismatch counts 1, every match counts 0, and the distance is normalized over the number of available calls for each pair of samples. Min Distance=0, Max distance =1. FIG. 3 shows a simple example of the distance measure for four samples (S1, S2, S3 and S4) for five SNPs (each of which can be A, B or AB).

The implemented distance function returns: D, νNSNPs, NSNPs, number of SNPs with one NoCall, number of SNPs with both NoCall, number of mismatches of different homozygosity (A vs B or viceversa), number of mismatches of type homozygosity vs heterozygosity (all combinations), number of homozygous matches and number of heterozygous matches. The expected distance D of two random samples, accordingly to the Hardy-Weinberg equilibrium, is 0.625. In fact, for unrelated samples we can write the joint probabilities as shown below. This is where the joint probability of two events E1 and E2, P(E1,E2) or P(E1 AND E2) is P(E1,E2)=P(E1) * P(E2|E1) and P(E2|E1) is called the conditional probability of E2 given E1.

P(A,A)=P(A)*P(A|A)=P(A)*P(A)=0.0625

P(B,B)=P(B)*P(B|B)=P(B)*P(B)=0.0625

P(AB,AB)=P(AB)*P(AB|AB)=P(AB)*P(AB)=0.25

The match probability P_pm is P(A,A)+P(B,B)+P(AB,AB).

The mismatch probability P_mm is: P_mm=1−P_pm=1−0.375=0.625.

This similarity analysis identified several pairs of cell lines that were very close to each other. All of these pairs are listed in TABLE 1. Some, the positive controls, were already known to be very similar or identical. Other pairs were not expected to be so similar or identical.

FIG. 4 is a graphical representation of the distance between all pairs excluding the cell lines in Table 1. Eliminating all cell lines having a distance, D, less than 0.2, left 155 cell lines with average distance of 0.383 (median=0.385, min=0.26 and max=0.48).

Next a subset of the 50,000 SNPs present in the GeneChip® Human Mapping 50K Xba 240 Array (Affymetrix, Inc.) was identified for use in further analysis. Although a variety of selection criteria are reasonable, those SNPs were used that: 1) had an assigned RS number in the NCBI SNP database; 2) were present in the Affymetrix, Inc. GeneChip Mapping 10K Array; and 3) were not located in an intron. This lead to the selection of about 5,300 SNPs that would be analyzed in the 155 selected cell lines.

The dataset of 155 cell lines was divided into a training set (about 2/3 of the cell lines) and a test set (about ⅓ of the cell lines) and the two potential selection criteria (equally distributed calls and Harvey-Weinberg equilibrium) were applied separately for a small subset of SNPs. FIG. 5 shows the pair distance plotted as a function of pair index for the equally distributed call selection criteria using 31 SNPs, and FIG. 6 shows the pair distance plotted as a function of pair index for the Harvey-Weinberg equilibrium call selection criteria using 14 SNPs. In these figures the red dots indicate that both cells lines of the pair were part of the test set.

Next, the two selection criteria were analyzed in order to answer the following questions: 1) How stable is the selection criteria with respect to different training sets?; and 2) Given a certain number of samples and a confidence level, how can the proper cutoff for the distance measure be determined?

Stability of the Selection Criteria with Respect to Different Training Data Sets

A bootstrap analysis was run on the training data set for 100 rounds and at each round the unselected cell lines create the test set. At each round 100 cell lines were randomly selected, the selection criteria (EDC or HWE) was applied without any constraint on the number of SNPs, the selection equilibrium was verified on the test set, and the selected SNPs were stored. The selection of the SNPs for use in SPIA was based on two factors. First, the SNPs should be frequently selected in different runs (e.g., a selection rate of at least 40%). Second, the SNPs should be distributed across the genome.

FIGS. 7A-7C depict the results of this analysis for the HWE selection criteria (A=0.22, B=0.22, and AB=0.42 and the call rate is at least 0.8). FIG. 7A is a histogram showing the number of SNPs selected at each round. FIG. 7B is a histogram showing the heterozygous rate of each selected SNP evaluated on the test set. FIG. 7C shows the selection frequency of each SNP. The mean number of SNPs was 47.6 (std dev=8.1). The mean percentage of heterozygous in the test set was 0.374 (std dev=0.07). The total number of SNPs selected was 345.

FIGS. 8A-8C depicts the results of this analysis for the EWD selection criteria (A=0.33, B=0.33, AB=0.33, call rate is at least 0.9, and minimum frequency is 30). FIG. 8A is a histogram showing the number of SNPs selected at each round. FIG. 8B is a histogram showing the heterozygous rate of each selected SNP evaluated on the test set. FIG. 8C shows the selection frequency of each SNP. The mean number of SNPs was 46.1 (std dev=6.4). The mean percentage of heterozygous in the test set was 0.33 (std dev=0.075). The total number of SNPs selected was 430.

Comparing the HWE selection criteria and EWD criteria, it appears that the HWE criteria provides more stable results with respect to variations in the training set. The heterozygous call rate is well conserved in the test set whether the HWE criteria or the EWD criteria is used. However, when the heterozygous call rates evaluated on the test set are compared with the heterozygous call rates for Caucasian samples reported by Affmetrix, Inc., it appeared that samples from Caucasians are not well represented. When the SNPs selected using each criteria are ranked by selection rate and the 40 highest ranked SNPs are selected, the mean selection rate was 0.44 (std dev=0.09) for the EWD selection criteria and 0.55 (std dev=0.14) for the HWE selection criteria.

While it is desirable to select the SNPs with a highest selection rate, there are a number of other factors that should be taken into account when selecting a set of SNPs for identifying or comparing/distinguishing cells. For example: the heterozygosity rate is desirably similar for different population (African American, Asian, Caucasian); the SNPs are desirably in regions that are not commonly deleted; the SNPs are desirably within exons; the SNPs are preferably distributed across a plurality of chromosomes (e.g., across all chromosomes).

FIGS. 9A and 9B are histograms of selection rates stratified on chromosomes for the SNPs selected with EWD and HWE respectively. FIGS. 10 and 11 are the top 40 SNPs selected with EWD and HWD, respectively.

Determining Cut-off for the Distance Measure

A cut-off distance measure must be used when comparing the genotype analysis for two samples at the various selected SNPS. This cut-off is the distance measure below which it cannot be stated that two samples are not the same sample.

The distance of two test samples can be compared with the distance expected for two true paired samples. More precisely, it can be determined whether the distance between two test samples is within the distribution of distances of a population of true paired samples. Provided that the confidence limit needed is defined, if the distance between two test samples is not within the distribution of distances of a population of true paired samples, it can be determined with confidence that the two test samples are not paired and, of course, not the same sample. This approach includes the test against being exactly the same sample. Where the test result is uncertain, a second set of SNPs can be run.

To apply the test an estimate of the mis-match probability (or match probability) of true paired samples and the experimental error rate must be used, so that the distance distribution can be determined.

For each pair of samples distance D was evaluated, and, based on number of SNPs used (νNSNPs), the probability of getting the same distance for two true paired samples is tested. It is assumed that the SNPs (SNPs calls) are independent, i.e., the call at locus i does not depend on call at locus i-l. The probability of having k matches (successes) out of N SNPs (runs) follows the a binomial distribution:

\({p_{k} = {{\begin{pmatrix}
N \\
k
\end{pmatrix}p^{k}q^{N - k}} = {\frac{N!}{{k!}{\left( {N - k} \right)!}}p^{k}q^{N - k}}}},\)

where p=P_pm and q=P_mm are the probability of success (match) and non-success (mismatch) respectively.

Given N, the sum over all possible k is equal to

\(1{\left( {{\sum\limits_{k = 0}^{N}p_{k}} = 1} \right).}\)

A property of binomial distribution is that after many runs, the binomial distribution approximates the Gaussian distribution. That is useful in evaluating the probabilities. After many runs, the mean number of successes kmean is kmean=Np and Sd_kmean=sqrt(Np(1-p)). For a normal distribution, the probability that a measurement falls within n standard deviations of the mean (i.e., within the interval [kmean−n sd, kmean+n sd]) is given by the integral of the distribution function. Given two samples, the probability of matched (P_pm) and of mismatched (P_mm) calls at each SNP locus is known (or can be evaluated from data). The sum of the probability of match and mismatch for each SNP locus is always equal to 1: P_pm+P_mm=1.

The joint probability of two events E1 and E2, P(E1, E2) or P(E1 AND E2) is P(E1,E2)=P(E1)×P(E2|E1) and P(E2|E1) is called the conditional probability of E2 given E1. Thus, the joint probability here is the sum, P_pm, of the homozygous joint probabilities (i.e., P(A,A) and P(B,B)) and of the heterozygous joint probability: P_pm=P(A,A)+P(B,B)+P(AB,AB).

For paired samples, such as normal and tumor samples from the same patient: P_mm(Norm,Tum)=P(A,B)+P(B,A)+P(A,AB)+P(B,AB)+P(AB,A)+P(AB,B) P(A,B)=P(A)* P(B|A) and P(B,A)=P(B)* P(A|B) accounts for probability of double mutations; P(A,AB) and P(B,AB) are related to gain of heterozygosity; P(AB,A) and P(AB,B) are related to loss of heterozygosity.

FIGS. 12 and 13 show the probability distribution of being a pair versus the number of mismatches, assuming that the mis-match probability is 0.2 and 0.4, respectively. Distributions for different νNSNPs are reported. Green dots in the two last scatter plots identifies distances which did not passed the test (confidence 95%; p_mm=0.2).

FIGS. 14 and 15 depict certain SNPs that were selected using the studies described above. These SNPs are particularly useful for analyzing NCI60 cells lines.

Analysis of Samples

The nucleic acids analyzed can be genomic DNA, cDNA, mitochondrial DNA, or any other source of nucleic acid. The nucleic acid can be amplified using any suitable method, including PCR, ligase chain reaction, transcription amplification, and self-sustained sequence replication. The nucleic acid can be obtained from any of a variety of biological samples, e.g., tissue, body fluid (e.g., blood, peritoneal fluid, spinal fluid and pleural fluid) and cells. Biological samples can also include sections of tissues, such as formalin-fixed sections or frozen sections. Cultured cells can also be analyzed.

SNPs can be genotyped using any convenient methods. For example, GeneChip® arrays from Affmetrix, Inc. are capable of analyzing 500,000 different SNPs using arrays of hybridization probes with a reported accuracy of 99.6% for homozygous calls and 96.3% for heterozygous calls. The technique is described in Genome Res 11:1913 (2001) and Human Muta 19:402 (2002). While standard GeneChip® arrays are useful for analyzing many SNPs, custom arrays can be designed to analyzed any SNP or group of SNPs. SNPs can also be genotyped using allele-specific PCR using primers that include sequence tags.

U.S. Pat. No. 6,709,816 (Affymetrix, Inc.) describes a high-throughput method for analyzing SNPs to determine if the sample is homozygous for a first allele, homozygous for a second allele or heterozygous at a give SNP. As explained in U.S. Pat. No. 6,709,816, SNPs can be accurately analyzed specificity by hybridizing uniquely tagged allele-specific nucleic acid sequences to corresponding tag probes in an array. Briefly, a nucleic acid sample is amplified using an allele-specific amplification such that uniquely tagged nucleic acids corresponding to different alleles of a polymorphic locus are generated. Nucleic acids corresponding to different alleles are linked to different tags. Each tag includes a sequence that is identical to all or part of a probe on a detection array. The method includes four steps: allele-specific amplification, labeling, hybridization, and detection. The allele-specific amplification employs allele- specific primers, each of which has an allele-specific 3′ portion and a 5′ portion that acts as a tag. The amplification products for each allele are labeled and hybridized to a solid support bearing appropriate probes in an array. Each probe in the array comprises the same or nearly the same sequence as the tag of an allele-specific primer.

The sequence tag is identical or nearly identical to the sequence of all or a portion of a respective probe in an array so as to allow specific binding between the complement of the tag and the probe. The sequence tags are selected so that they have similar hybridization characteristics and minimal cross-hybridization to other sequence tags.

Each pair of primers is designed to specifically amplify one allelic form of a polymorphic locus. The two primers in a pair of primers are complementary to opposite stands of the DNA region to be amplified. The first primer of the pair has a 3′ nucleotide which is complementary to a specific allelic form of the SNP but not complementary to other allelic form (or forms). The first primer includes a portion at its 3′ end which is complementary to the region of double stranded DNA to be amplified. The first primer also includes a portion at its 5′ end which is a tag. The tag has the same sequence as all or a portion of a probe on a solid support. The tag sequence is not complementary to any significant portion of the DNA being amplified. The second primer can include a tag or not. The two primers hybridize to a double stranded nucleic acid at position that are less than 1,000 (100 or even 10) bases apart. The amplification generates a first amplified strand and a second amplified strand. The first strand includes a portion identical to all or part of the probe on the solid support and the second strand comprises a 5′ portion complementary to all or part of the probe.

The amplified DNA is labeled before it is hybridized to a probe on a solid support. The amplified DNA is hybridized to probes which are immobilized to known locations on a solid support, e.g., in an array, microarray, high density array, beads or microtiter dish. The presence of labeled amplified DNA products hybridized to the solid support indicates that the nucleic acid sample contains at the polymorphic locus a nucleotide which is the same as the 3′ terminal nucleotide of the first primer. The quantities of the label at distinct locations on the solid support can be compared, and the genotype can be determined for the sample from which the DNA was obtained.

Two or more pairs of primers can be used for determining the genotype of a sample. Each pair of primers specifically amplifies a different allele possible at a given SNP.

The hybridized nucleic acids can be detected, e.g., by detecting one or more labels attached to the target nucleic acids. The labels can be incorporated by any convenient means. For example, a label can be incorporated by labeling the amplified DNA product using a terminal transferase and a fluorescently labeled nucleotide. Useful detectable labels include labels that can be detected by spectroscopic, photochemical, biochemical, immunochemical, electrical, optical, or chemical means. Radioactive labels can be detected using photographic film or scintillation counters. Fluorescent labels can be detected using a photodetector.

Implementation

The methods, equations and algorithms described herein can be easily implemented in hardware or software, or a combination of both. The methods can be implemented in computer programs using standard programming techniques following the steps, algorithms, equations, and figures disclosed herein. The programs can be designed to execute on programmable processors or computers, e.g., microcomputers, each including at least one processor, at least one data storage system (including volatile and non-volatile memory and/or storage elements), at least one input device, such as a keyboard or push button array, and at least one output device, such as a monitor, e.g., a CRT or LCD monitor, or a printer. Program code is applied to input data to perform the functions described herein. The output information is applied to one or more output devices such as a printer, or a monitor, or a web page on a computer monitor with access to a website, e.g., for remote monitoring.

Each program used in the new system is preferably implemented in a high level procedural or object oriented programming language to communicate with a computer system. However, the programs can be implemented in assembly or machine language, if desired. In any case, the language can be a compiled or interpreted language.

Each such computer program is preferably stored on a storage medium or device (e.g., ROM or magnetic diskette) readable by a general or special purpose programmable computer, for configuring and operating the computer when the storage media or device is read by the computer to perform the procedures described herein. The system can also be considered to be implemented as a machine or computer-readable storage medium, configured with a computer program, where the storage medium so configured causes a computer to operate in a specific and predefined manner to perform the functions described herein.

Although any communications network can be used to obtain results from remote monitoring, the Internet or wireless systems provide useful choices to transmit data.

### Other Embodiments

It is to be understood that while the invention has been described in conjunction with the detailed description thereof, the foregoing description is intended to illustrate and not limit the scope of the invention, which is defined by the scope of the appended claims. Other aspects, advantages, and modifications are within the scope of the following claims.

