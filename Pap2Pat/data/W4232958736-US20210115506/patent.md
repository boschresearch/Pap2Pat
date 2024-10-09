# DESCRIPTION

## FIELD OF THE INVENTION

This invention relates to methods and systems for measuring allograft or host injury. Specifically, the invention relates to methods and system of donor-derived (dd-cfDNA) monitoring using shotgun sequencing without donor genotype information.

## BACKGROUND OF THE INVENTION

Although solid-organ transplantation is now a common practice, the clinical outcomes remain poor with median survival rate (5.3 years for lung and 11 years for heart). Accurate monitoring of allograft health is essential for long-term survival of the transplant recipient. The current gold standard method of allograft rejection surveillance is the biopsy (transbronchial biopsy for lung transplant and endomyocardial biopsy for heart transplant), but this invasive technique suffers from high cost and myriad complications.

Current implementation of shotgun-based Genome Transplant Dynamics (GTD), which we will refer to as the “two-genomes” method, requires genotyping of both the donor and recipient. In contrast to the recipient genotype that is easy to obtain, the donor genotype is often unavailable. We therefore in this invention set out to develop a method that enables dd-cfDNA monitoring using shotgun sequencing without donor genotype information—a “one-genome” method. In this invention as exemplary embodiments, we apply the method to lung and heart transplant recipient cohort data and demonstrate that the performance of a one-genome method approaches the performance of the two-genome method.

## SUMMARY OF THE INVENTION

Quantification of cell-free DNA (cfDNA) in circulating blood derived from a transplanted organ is a powerful approach to monitoring post-transplant injury. Genome Transplant Dynamics (GTD) quantifies donor-derived cfDNA (dd-cfDNA) by taking advantage of single-nucleotide polymorphisms (SNPs) distributed across the genome to discriminate donor and recipient DNA molecules. In its current implementation, GTD requires genotyping of both the transplant recipient and donor. However, in practice, donor genotype information is often unavailable.

In this invention, we address this issue by developing an algorithm that estimates dd-cfDNA levels in the absence of a donor genotype. The method predicts heart and lung allograft rejection with an accuracy that is similar to conventional GTD. We furthermore refined the method to handle closely related recipients and donors, a scenario that is common in bone marrow and kidney transplantation. We show that it is possible to estimate dd-cfDNA in bone marrow transplant patients that are unrelated or that are siblings of the donors, using a hidden Markov model (HMM) of identity-by-descent (IBD) states along the genome. Last, we demonstrate that comparing dd-cfDNA to the proportion of donor DNA in white blood cells can differentiate between relapse and the onset of graft-versus-host disease (GVHD). These methods alleviate some of the barriers to the implementation of GTD, which will further widen its clinical application.

In an exemplary embodiment, the present invention provides a method of quantifying transplant-derived circulating donor-derived cell-free DNA in the absence of a donor genotype according to the following steps: (a) extracting a blood sample from a transplant recipient; (b)isolating circulating nucleotide acids from the plasma of the extracted blood sample; (c) performing an unbiased sequencing on the isolated circulating nucleotide acids using a first computer-implemented method; (d) estimating and quantifying the donor-derived cell-free DNA based on genotyping from only the transplant recipient using a second computer-implemented method; and (e) outputting the quantified transplant-derived circulating donor-derived cell-free DNA. Both computer-implemented methods and the outputting are executed by a computer device. It is noted that the method does not use targeted PCR amplification. The step of genotyping from only the transplant recipient could be based on genotyping array, cell-free DNA sequencing or low coverage whole genome sequencing followed by imputations.

Transplant recipients are solid-organ transplant recipients (e.g. heart, lung, kidney, liver, or the like), bone marrow transplant recipients or hematopoietic stem cell recipients.

Embodiments of this invention could be implemented as a method, computer-implemented method, software or system. Some method steps could be implemented as computer-implemented steps executable by computer hardware, device, chip, system and/or processor.

## DETAILED DESCRIPTION

### Quantifying Dd-cfDNA in Lung and Heart Transplant Recipients

We developed a statistical approach and computer-software method that quantifies donor- and recipient-derived cfDNA fragments in the absence of donor genotype information (see Methods Section infra for a formal description of the model). To quantify the observed abundance of alleles of each genotyped SNP in cfDNA sequences (FIG. 5), we first filter low quality reads, reads that are not mapped uniquely to the genome, and reads with potential for mapping biased by genetic variability. We then remove duplicated reads and count allele appearances of each genotyped SNP (SAMtools mpileup function). We use all genotyped SNPs, as opposed to the “two genomes” method that uses only SNPs that are homozygous but differ between recipient and donor. The observed allele appearances in cfDNA and the recipient genotype are the inputs for our “one-genome” model.

To calculate the probability of the observed cfDNA, we first calculate the probability of each possible donor and recipient genotype. Recipient genotype depends on the recipient measured genotype and the genotyping error rate. Vital organ transplants are rarely closely related. Therefore, for heart and lung transplants, our model assumes that the donor genotype is randomly selected from a human population. Given this assumption, the probability of a specific donor allele is its frequency in the population. Our algorithm iterates over 1000 Genomes Project populations and super-populations to detect the most likely ancestral population of the donor. This model achieves satisfying performance in lung and heart transplant but might need refinement for handling bone marrow transplant in which donor and recipients are often related.

Putting it together, the probability of observing a specific allele in a cfDNA fragment is computed by integrating over all possible recipient and donor genotypes and depends on the sequencing error rate, the fraction of dd-cfDNA in the recipient plasma and the probabilities of observing the allele conditioning on it being donor- or recipient-derived (FIG. 1A indicated (a)). Finally, we compute the log-likelihood of the data by summing log-likelihoods over all SNPs, assuming SNPs are independent (this assumption is also made by the two-genomes method). We use an optimization algorithm to find the maximum likelihood parameter values.

### Performance of Lung and Heart Rejection Predictions

To assess the performance of the one-genome model, we compare estimates of dd-cfDNA for the one and two-genome methods. We find that the predictions of dd-cfDNA level in lung recipients (51 patients, 382 samples) are highly correlated between the two methods (Pearson's R2=0.99, Spearman's ρ=0.94; FIG. 2A). Accordingly, the two methods also performed similarly in differentiating between different levels of organ rejection (as measured by biopsy; FIG. 2C). For heart transplant recipients (59 patients, 435 samples) dd-cfDNA level estimates of the two methods were highly correlated (Pearson's R2=0.99, Spearman's ρ=0.67; FIG. 2B). However, the agreement between the two methods is not as high as in the lung cohort, especially when dd-cfDNA levels are below ˜0.5%. This may be because samples that contain very low fractions of dd-cfDNA are less informative regarding the donor genotype, making the inference harder. The two-genome method performs slightly better in differentiating between grades of acute rejection, although the differences were mostly non-significant; therefore, its dd-cfDNA estimates may be slightly more accurate (FIG. 2D). We conclude that donor genotyping is not required for lung transplant recipients. Donor genotyping can also be avoided in heart transplant recipients, but the accuracy of the test may be reduced slightly.

Quantifying Donor-Derived cfDNA in Bone Marrow Transplant Recipients

Because bone marrow donors are often close relatives of the recipients, the assumption that the donor is randomly selected from the population no longer holds. Chromosomes of closely-related individuals contain long segments of identical genotype. These segments are said to be identical by descent (IBD). The abundance and length of the IBD segments depend on the number of meioses separating the two chromosomes and the recombination rate. Ignoring IBD may lead to under-estimation of dd-cfDNA level. We therefore extended our model account for possible IBD by learning recipient-donor relatedness. We implemented a Hidden Markov Model (HMM) with three states (FIG. 1; see Methods Section infra for details): when there is no IBD (IBD=0), the model emission probabilities are similar to the above unrelated donor-recipient model; when one pair of chromosomes is IBD (IBD=1), the genotype of one donor allele will be similar to one of the recipient alleles and the other donor allele likelihood depends on its abundance in the population (independently of the recipient genotype); lastly, when both chromosome pairs are in IBD (IBD=2) the recipient and donor genotypes are identical. In our model, transitions between IBD states can occur only between pre-calculated 2 centimorgan blocks. Transition probabilities depend on the recipient-donor relatedness, which is represented by the number of meioses separating each pair of donor-recipient chromosomes (FIG. 1B indicated by (b)). In other words, in our model, the donor genotype depends on the population allele frequency and the recipient genotype according to the local IBD state.

### Accuracy of Dd-cfDNA Level Estimations in Bone Marrow Transplant Recipients

To evaluate the performance of the refined one-genome method, we applied it to 76 samples from 8 bone marrow transplant recipient patients (FIGS. 3A-B, FIG. 5). Two of the donors (for patients I4 and I5) were unrelated to the recipients and six were siblings of the recipients. As expected, the naïve implementation of the one-genome method underestimates dd-cfDNA in sibling donors (FIGS. 3A-B) that share about 50% of their genotype due to IBD (FIGS. 3A-B), but not in unrelated donors. When our model is set to learn the relationship between the donor and the recipient, its dd-cfDNA level estimates match the two-genomes method (Pearson's R2=1, Spearman's ρ=0.99; FIG. 3A). Reassuringly, these predictions strongly correlate with the fraction of reads originating from the X chromosomes when the donor and recipient sex is different (FIGS. 6A-D). We conclude that accurate estimation of dd-cfDNA in bone marrow recipients does not require donor genotyping. These results may also apply to other settings, such as kidney transplants.

### Differentiating Between Relapse and Graft Versus Host Disease in Bone Marrow Transplant Recipients

The success of bone marrow transplants is often impaired by cancer relapses and graft versus host disease (GVHD). Diagnosing and differentiating between the two remains a major challenge in the field. The current gold standard for a successful engraftment is absolute neutrophil count greater than 500 for three consecutive days. This corresponds to 47-82% dd-cfDNA in our patients (FIGS. 6A-D). We notice that in patients who relapse (patients I3) or have acute GVHD (patients I1 and I8) or chronic GVHD (patients I2), the level of cfDNA drops after reaching its peak (24%, 33%, 11% and 24%, respectively). Although our cohort is too small to assess significance, this observation suggests that GTD can be used to monitor bone marrow transplant health.

What are potential explanations for an increase in the level of cfDNA from recipient origin? In the case of a cancer relapse, the fraction of lymphocytes of recipient origin increases. The cfDNA will therefore reflect increasing levels of recipient-origin lymphocytes. On the other hand, in the case of GVHD, the fraction of lymphocytes from recipient origin does not increase. In this case, the increase in dd-cfDNA is caused by injury to recipient tissues. We therefore hypothesized that differences in the recipient-origin DNA in the cellular and plasma (cell-free) fractions can distinguish between relapse and GVHD. As a proof of principle, we sequenced both the cfDNA and the cellular fraction in patient I8. In agreement with our hypothesis, the two values match until the onset of the acute GVHD (since most cfDNA originates from lymphocytes) and then diverge—after the onset of GVHD, the cellular fraction remains low and cfDNA level increases (FIG. 4). This “N of one” experiment demonstrates the great potential of GTD to distinguish between relapses and GVHD—an urgent unmet need in the field.

### Methods Section

cfDNA Sequencing and Genotype Data Collection

The cfDNA sequencing and genotyping data for heart and lung transplant recipients was available from our previous studies [8,9]. Additional dd-cfDNA measurements were performed for bone marrow transplant patients (8 patients, 76 samples), using methods previously described [8,9]. In short, recipient plasma was collected at several time points before the transplant procedure (two time points) and at several time points after transplantation sequenced. cfDNA was purified from plasma and sequenced (Illumina HiSeq 200 or HiSeq 2500 1×50 bp or 2×100 bp). Donor and recipient genotyping was performed using Illumina whole-genome arrays HumanOmni2.5-8 or HumanOmni1 prior to the transplant.

Estimating Allele Representation in cfDNA Fragments

Several steps were applied to the cfDNA sequencing reads to achieve counts of allele representation for each genotyped SNP. First, low quality reads were filtered out (reads in which more than 50% of the base qualities are below 20). Second, reads were mapped to the human genome (UCSC version hg19) using bowtie2 [28] (with the following parameters: -D 20 -R 3 -N 0 -L 20 -i S,1,0.50 -I 20 -X 500 --no-mixed --no-discordant --no-unal -t) and SAMtools [29] was used to filter paired ends reads where one of the reads was unmapped (flags -f 3 -F 3852 for pair ends reads and -F 3844 for single end reads) or reads with P>0.05 to be mapped non-uniquely. Third, WASP [14] was applied to remove reads in which the mapping may be biased by the genotype. Fourth, duplicated reads (reads that map to the same exact location) were removed by scripts that selects randomly which of the duplicated reads to keep and is therefore not biased towards a specific genotype. Fifth, chromosomal coverage was computed using HTSeq [30]. Sixth, the number of cfDNA reads that contain each SNP allele was computed using SAMtools mpileup function. These counts were used as input for the model.

Estimating cfDNA Donor-Derived in Recipient that is Unrelated to the Donor

As vital organs such as heart and lungs are donated post-mortem, donors are usually unrelated to recipients. Therefore, our model assumes that the donor was randomly selected from some ancestral population. This is clearly an assumption—donors may have a mixed ancestry and their MHC is often matched to the recipient MHC—nonetheless we find that we can achieve good performance by making this assumption (we note that modeling of mixed ancestry did not improved the predictions). Given the population from which the donor was drawn, the prior probability of observing each allele in the donor is exactly the allele frequency in the population (assuming Hardy-Weinberg equilibrium). Since the donor population is unknown, the optimization function iterates over 1000 Genomes project populations and super-population [16] and selects the population that maximize the likelihood. The goal of the model is to estimate the fraction of cfDNA that is donor-derived (dd-cfDNA) given the recipient measured genotype and the cfDNA reads (FIG. 1 indicated by (a)).

Formally, let N be the number of bi-allelic SNP that were genotyped in the recipient; A and B denote the two possible alleles for SNP where i∈{1, 2, . . . , N}; (Ri, Ri) be the recipient true genotype in SNPi; (Ri*,Ri*) be the recipient observed (measured) genotype in SNPi; (Di, Di) be the donor true genotype in SNPi; fipopbe the frequency of allele A of SNPi in population m;

\(C_{i_{j \in {\{{1,2,\ldots,K_{i}}\}}}}\)

be the true SNPi allele in a cfDNA fragment that contains it; and

\(C_{i_{j \in {\{{1,2,\ldots,K_{i}}\}}}}^{*}\)

be the observed allele of SNPi from a sequencing read of this fragment. The observed data (R*, C*) is therefore the recipient measured genotype at N SNPs and the observed allele of these SNPs in cfDNA sequencing reads.

Lets also define the following model parameters (θ): d∈[0,1] is the fraction cfDNA fragments that are donor-derived (dd-cfDNA); es ∈[10−9,10−2] is the sequencing error rate; eg ∈[10−9,10−4] is the genotyping error rate; and Popm ∈{1, . . . , M} is one of M ancestral population and super populations of 1000 genomes project from which the donor is randomly drawn. The model sequencing and genotyping error rates were bound to technically realistic range. The goal of our model is to estimate d−the fraction of dd-cfDNA.

In our model, of the dependency of the observed recipient genotype of SNPi on the true genotype involves the genotyping error rate. So, for example:

\({P\left( {{\left( {R_{i_{1}}^{*},R_{i_{2}}^{*}} \right) = \left. {AA} \middle| \left( {R_{i_{1}},R_{i_{2}}} \right) \right.};e_{g}} \right)} = {{\left( {1 - e_{g}} \right)^{2}1\left\{ {{R_{i_{1}} = A},{R_{i_{2}} = A}} \right\}} + {2\left( e_{g} \right)\left( {1 - e_{g}} \right)1\left\{ {{R_{i_{1}} = A},{R_{i_{2}} = B}} \right\}} + {\left( e_{g} \right)^{2}1\left\{ {{R_{i_{1}} = B},{R_{i_{2}} = B}} \right\}}}\)

Similarly, the dependency of the observed allele in a sequencing read that map to SNPi on the true allele of SNPi in the cfDNA fragment that was sequenced involves the sequencing error rate (this also capture PCR amplifications errors):

P(Ci*=A|Ci;es)=(1−es)1{Ci=B}+(es)1{Ci=A}

Following the assumption that the donor was randomly drawn from a population, the genotype of SNPi depends on SNPi alleles frequencies in the population and therefore on which ancestral population is used to achieve the SNPi alleles frequencies estimates:

\(P\left( {{\left( {{D_{i_{1}} = d_{1}},{{D_{i_{2}} = d_{2}};{pop}_{m}}} \right) = {f_{i_{d_{1}}}^{{pop}_{m}}*f_{i_{d_{2}}}^{{pop}_{m}}}},{{{where}\mspace{14mu} d_{1}} \in {\left\{ {A,B} \right\} \mspace{14mu} {and}d_{2}} \in \left\{ {A,B} \right\}}} \right.\)

Lastly, the probability that a cfDNA that maps to SNPi contains a specific allele of SNPi depends of the true genotype of the recipient and the donor and involves the fraction of donor-derived cfDNA (d); for example:

\(\left. {{P\left( {{C_{i_{j}} = \left. A \middle| R_{i_{1}} \right.},R_{i_{2}}} \right)},\; {\left( {D_{i_{1}},D_{i_{2}}} \right);d}} \right) = {{d*\begin{pmatrix}
{{1*1\left\{ {{D_{i_{1}} = A},{D_{i_{2}} = A}} \right\}} +} \\
{{0.5*1\left\{ {{D_{i_{1}} = A},{D_{i_{2}} = B}} \right\}} + {0.5*1\left\{ {{D_{i_{1}} = B},{D_{i_{2}} = A}} \right\}} +} \\
{0*1\left\{ {{D_{i_{1}} = B},{D_{i_{2}} = B}} \right\}}
\end{pmatrix}} + {\left( {1 - d} \right)*\begin{pmatrix}
{{1*1\left\{ {{R_{i_{1}} = A},{R_{1_{2}} = A}} \right\}} +} \\
{{0.5*1\left\{ {{R_{i_{1}} = A},{R_{i_{2}} = B}} \right\}} + {0.5*1\left\{ {{R_{i_{1}} = B},{R_{i_{2}} = A}} \right\}} +} \\
{0*1\left\{ {{R_{i_{1}} = B},{R_{i_{2}} = B}} \right\}}
\end{pmatrix}}}\)

Putting it together the likelihood of observing the recipient genotype and the sequencing reads that map to SNPi is:

\({P_{i}\left( {\left( {R_{i_{1}}^{*},R_{i_{2}}^{*}} \right),C_{i_{1}}^{*},{{\ldots \mspace{14mu} C_{i_{K_{i}}}^{*}};d},e_{s},e_{g},{pop}_{m}} \right)} = {\prod\limits_{j = 1}^{K_{i}}{\sum\limits_{c,r_{1},r_{1},d_{1},{d_{2,c} \in {\{{A,B}\}}}}{{\quad\quad}{\quad{\quad\left( \begin{matrix}
{{P\left( {{\left. C_{i_{j}}^{*} \middle| C_{i_{j}} \right. = c};s_{e}} \right)}*} \\
{{P\left( {\left. C_{i_{j}} \middle| \left( {R_{i_{1}},R_{i_{2}}} \right) \right.,{\left( {D_{i_{1}},D_{i_{2}}} \right);d}} \right)}*} \\
{{P\left( {{D_{i_{1}} = d_{1}},{{D_{i_{2}} = d_{2}};{pop}_{m}}} \right)}*} \\
{{P\left( {{R_{i_{1}} = r_{1}},{R_{i_{2}} = r_{2}}} \right)}*} \\
{P\left( {R_{i_{1}}^{*},{\left. R_{i_{2}}^{*} \middle| R_{i_{1}} \right. = r_{1}},{{R_{i_{2}} = r_{2}};g_{e}}} \right)}
\end{matrix} \right)}}}}}\)

Although it is possible to model the probability of the recipient genotype (P(Ri,Ri))

using population allele frequency data, we assume here a uniform probability since, in practice the genotyping error is very low and therefore the measured recipient genotype is highly informative on the true recipient genotype.

Finally, assuming that SNPs are independent (this is reasonable assumption because we used only genotyped SNPs), the likelihood function is:

\(\mathcal{L}\left( {R^{*},{{C^{*}\left. \theta \right)} = {\sum\limits_{i = 1}^{N}{{P\left( {\left( {R_{i_{1}}^{*},R_{i_{2}}^{*}} \right),C_{i_{1}}^{*},{\ldots \mspace{20mu} C_{i_{K_{i}}}^{*}}} \right.}d}}},s_{e},g_{e},{pop}_{m}} \right)\)

where R*, C* are genome-wide measured recipient genotype and all mapped sequencing reads correspondingly.

We use L-BFGS-B to minimize the negative log likelihood for each possible donor ancestral population and select the population that obtains the minimal negative log likelihood.

Estimating Donor-Derived cfDNA in Related Recipient and Donor

In contrast to lung and heart, bone marrow and other organs such as kidney, are often donated by individuals that are closely related to the recipient. Therefore, the assumption that the donor is drawn randomly from the population is no longer valid. Closely-related individuals share stretches of identical haplotypes that were inherited from a recent common ancestor, a phenomenon known as Identity By Descent (IBD). For each pair of chromosomes, IBD segments' length distribution and total length depend on the number of meioses from their Most Recent Common Ancestor (MRCA). The model accounts for IBD using a non-homogenous Hidden Markov Model (HMM) in which each position in the genome can be in one of three states IBD=0, IBD=1 or IBD=2 in which 0,1, or 2 pairs of chromosomes are identical by descent (FIG. 1 indicated by “b”). For efficiency and to avoid strong effects of linkage disequilibrium (LD), transitions are allowed only between ˜2 cM blocks, which are pre-calculated using a recombination rate map [22]. In each block, each one of the two haploid pairs of donor-recipient genomes can be in IBD or no-IBD state. The transitions between the IBD states for each haploid pair depend on the average genetic distance between the blocks and the marginal probability of the pair to be IBD, similar to the plink method [13]. In short, considering two haploids (c1 and c2) that share a common diploid ancestor with c1 and c2 separated by m 2 meiosis events, m=1−log2(PIBD)) where PIBD ∈[0,1] is the marginal probability of the pair to be in IBD state. We define lb,b+1 to be the genetic distance between two neighboring loci b,b+1 (here, approximated by the average genetic distance between blocks in cMorgan units). The probability of an odd number of recombination events

\(\theta_{b,{b + 1}} = {\frac{1 - {e\frac{{- 2}*l_{b,{b + 1}}}{100}}}{2}.}\)

We also define y1(θb,b+1,m)=(1−θb,b+1)m−2 and y2(θb,b+1)=(1−θb,b+1)2+θb,b+12. The transition matrix for two haploids is:

\({T_{b,{b + 1}}\left( m_{i} \right)} = {\quad\begin{bmatrix}
{1 - \left( \frac{1 - {{y_{1}\left( {\theta_{b,{b + 1}},m_{1}} \right)}*{y_{2}\left( \theta_{b,{b + 1}} \right)}}}{2^{m_{i} - 1} - 1} \right)} & \frac{1 - {{y_{1}\left( {\theta_{b,{b + 1}},m_{1}} \right)}*{y_{2}\left( \theta_{b,{b + 1}} \right)}}}{2^{m_{i} - 1} - 1} \\
{1 - {{y_{1}\left( {\theta_{b,{b + 1}},m_{1}} \right)}*{y_{2}\left( \theta_{b,{b + 1}} \right)}}} & {{y_{1}\left( {\theta_{b,{b + 1}},m_{1}} \right)}*{y_{2}\left( \theta_{b,{b + 1}} \right)}}
\end{bmatrix}}\)

where i∈{1,2}. The transition matrix for the IBD states of the two pairs of haploids is a simple combination of the two haploid pairs transition matrices and depends on their two IBD parameters: PIBDI and PIBDII. Similar to PLINK, we limit PIBDI and PIBDII to be at most 0.5. This excludes parent-child relations from the donor-recipient relationships. Although we did not address it in this work, dd-cfDNA of parent-child donor-recipient can be estimated by assuming that they are unrelated and accounting for the them sharing exactly 50% of their autosomal DNA by IBD (assuming that the parents are non-related).

The emissions probabilities of each SNP in each IBD state are similar to the likelihood function above with one difference—the probability of the donor genotype depends also on the recipient genotype (in addition to its dependence on the ancestral population):

\({P_{i}\left( {\left( {R_{i_{1}}^{*},R_{i_{2}}^{*}} \right),C_{i_{1}}^{*},\left. {\ldots \mspace{14mu} C_{i_{K_{i}}}^{*}} \middle| d \right.,e_{s},e_{g},{pop}_{m}} \right)} = {\quad {\quad{{\quad\quad}{\quad{\underset{j = 1}{\overset{K_{i}}{\prod}} \sum\limits_{c,r_{1},r_{1},d_{1},{d_{2,c} \in {\{{A,B}\}}}}}\quad}\left( \; \left. \quad \begin{matrix}
{{P\left( {{\left. C_{i_{j}}^{*} \middle| C_{i_{j}} \right. = c};s_{e}} \right)}*} \\
{{P\left( {\left. C_{i_{j}} \middle| \left( {R_{i_{1}},R_{i_{2}}} \right) \right.,{\left( {D_{i_{1}},D_{i_{2}}} \right);d}} \right)}*} \\
{{P\left( {{D_{i_{1}} = d_{1}},{D_{i_{2}} = {\left. d_{2} \middle| R_{i_{1}} \right. = r_{1}}},{R_{i_{2}} = r_{2}},{{IBD}_{i};{pop}_{m}}} \right)}*} \\
{{P\left( {{R_{i_{1}} = r_{1}},{R_{i_{2}} = r_{2}}} \right)}*} \\
{P\left( {R_{i_{1}}^{*},{\left. R_{i_{2}}^{*} \middle| R_{i_{1}} \right. = r_{1}},{{R_{i_{2}} = r_{2}};g_{e}}} \right)}
\end{matrix} \right) \right.}}}\)

The following tables show P(Di=d1, Di=d2|Ri=r1, Ri=r2, IBD; popm) for a bi-allelic SNPi, which has two possible alleles: A and B that are occur with frequency fA and fB in Popm respectively, for IBDi=0,1,2.

Conditioning on IBDi=0:

Conditioning on IBDi=1

Conditioning on IBDi=2

Putting it together the parameters of the model are: d−the fraction of dd-cfDNA, es sequencing error probability, eg genotyping probability and PIBDI and PIBDII IBD probability for the two haploid pairs. We used the Viterbi algorithm to calculate the likelihood of most likely path for specific parameter values, and optimize the likelihood using L-BFGS-B.

**Comparing One-Genome and Two-Genomes Methods Predictability of Organ Rejection**

To assess how well each method dd-cfDNA predictions can be used to discriminate between different levels of heart and lung rejection, we computed the area under the curve (AUC) of the receiver operating characteristic (ROC): the dd-cfDNA prediction of one lung donation were doubled to match the levels of two lungs donations and measurements previous to 14 and 60 days following heart and lung transplant correspondingly were removed from the analysis. A two-sided DeLong test [31] (Implemented in R pROC package [32]) was used to assess the significance of the difference between two corresponding ROC curves.

## Data and Materials Availability

The bone marrow cohort sequence data have been deposited in the Sequence Read Archive (temporary submission id: SUB2077093). Code is available on github https://github.com/eilon-s/cfDNAG1.

