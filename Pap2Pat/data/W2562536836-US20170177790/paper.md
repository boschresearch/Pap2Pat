# Results

Many well-studied and known driver genes were originally identified by searching for higher than expected mutation rates. Thus, it is likely that the remaining uncharacterized driver genes exhibit infrequent or atypical mutation patterns (Fig. 1A, Supplementary Fig. 1). As driver genes are known to be enriched for specific properties12, methodical analysis of these traits can help focus the search on a smaller subset of candidate genes, and a machine learning approach that integrates both tumor data and other gene level traits may elucidate important driver gene traits.

## Gene Features

CARNAF uses a broad set of gene properties. We extracted tumor-derived and non-tumor based gene features spanning genomic, transcriptomic, proteomic, functional, and phenotypic categories (Fig. 1B, Table 1, Supplementary Tables 1 and 2, and Online Methods). The tumor genomics features consisted of copy number variation data and four gene mutation patterns that are highly predictive of TSG and OG function13. A total of 131 features remained after removal of sparse and inter-correlated features (Online Methods).

## Driver And Background Gene Datasets

Supervised machine learning methods require the construction of a labeled data set to train a classifier that can categorize new genes. For this, we defined three gene classes of interest: TSGs, OGs, and background genes (BGs) which are genes that are not known to act as drivers. As there is large variation among published lists of driver genes, we assembled 15 multi-tumor type driver gene sources to aid in label construction (Supplementary Tables 3 and 4). These studies included drivers present in at least one, and often more tumor types. From this set we selected 165 high confidence drivers with a known function that are present in at least one tumor type (84 TSGs, 81 OGs), 682 medium confidence drivers, 1,360 low confidence drivers, and 15,972 BGs (Fig. 1C and Online Methods).

## Carnaf Methodology

CARNAF performs multi-class classification using a random forest, a robust predictive model composed of an ensemble of decision trees, each of which is trained on a subset of the training data20. The training set consists of 165 high confidence driver genes labeled as TSGs or OGs, and 15,972 BGs (Fig. 1c). Genes in the medium confidence, low confidence, and other evidence sets were excluded from training, since they may contain false positive results and often cannot be functionally categorized as TSGs or OGs. After training, every gene in the genome is assigned a posterior probability of being a TSG, OG or BG, such that the probabilities sum to one. The use of a large set of negative examples that is likely to include a small subset of mislabeled examples (genes that are labeled as BGs but have the potential to become driver genes) is known as positive-unlabeled (PU) learning in machine learning literature21.

Each gene was ranked according to the posterior probability of being a TSG, OG, or a BG as computed according to all trees that did not use the specific gene for training, out of 100,000 generated trees. Driver gene probabilities were obtained via the summation P(driver) = P(TSG) + P(OG). As the training data contains 97-fold more BGs than high confidence driver genes, we employed a stratified resampling with replacement approach where each tree used a training set with 165 high confidence driver genes and 165 BGs, as is commonly done in PU learning22. Additional details are provided in the Online Methods.

## Non-Tumor Genomics Features Improve Detection Of Rare Drivers

As most computational methods identify driver genes by relying primarily on tumor data, we asked whether a large set of gene features beyond tumor data may be beneficial for detecting rare drivers. To this end, we compared CARNAF driver gene rankings using three different sets of features: all gene features, all gene features except tumor genomics, and only tumor genomics features (Fig. 2 and Supplementary Table 5). Prediction performance was evaluated as the ability to prioritize high, medium, and low confidence driver genes over BGs, with the medium and low sets expected to contain high false positive rates. As expected, precision at N shows that tumor genomics alone are ideal for detecting the highest confidence drivers, as these genes are frequently mutated (Fig. 2). In contrast, precision at N among the lower confidence sets corroborates that addition of non-tumor genomics features provides advantages when looking for infrequently mutated driver genes.

We further investigated several additional driver gene detection aspects. First, we verified that CARNAF results remained very similar when using slightly different training sets, indicating it is robust to the specific choice of training genes (Supplementary Table 6). Second, we verified that CARNAF accurately distinguished high confidence TSGs from OGs (Supplementary Fig. 2 and Supplementary Note). This was especially notable when using tumor genomics features (area under Receiver Operating Characteristic curve of 0.94 ± 0.02, out of bag estimation) since frequently mutated drivers have strong characteristic mutation patterns1. Third, the cumulative detection rate was superior when using non-tumor genomics features for all gene confidence sets (Supplementary Fig. 3). Fourth, we evaluated gene rankings in the absence of gene ontology features, as these can be biased towards well-studied genes. We observed a decrease in precision for low confidence genes (Supplementary Fig. 4 and Supplementary Table 5), suggesting that gene ontology features are useful for proposing rare drivers. Fifth, we demonstrated that although frequently mutated drivers are overrepresented among the high confidence drivers used for training (Fig. 1A), this has minimal impact on the top ranked genes (Supplementary Fig. 5, Supplementary Table 7, and Supplementary Note).

Finally, we performed manual literature curation of the top 15 ranked CARNAF driver genes (excluding the high confidence drivers) using all features and compared the results to 15 multi-tumor type cancer studies (Supplementary Tables 4 and 8). Strikingly, we found that the large majority of the 15 genes had substantial cancer-related evidence (Supplementary Table 8), often supported by genomics or functional assays. 4 (SIRT1, TGFBR1, CDK1, and SMAD1) of the 15 genes were not present in any of the multi-tumor type cancer studies. All of the latter 4 genes contain cancer-related evidence232425262728293031, with SIRT1 and TGFBR1 also having documented genomic alterations293031 (Supplementary Note).

## Contribution Of Individual Features To Driver Gene Detection

Random forests, which CARNAF uses for gene ranking, provide a measure of importance for each feature which quantifies its contribution to the classification process. The majority of top ranked features were confirmed to be those that are known to be cancer-related such as signal transduction, cell differentiation, cell proliferation, number of protein-protein interactions, predicted haploinsufficiency, specific phosphorylation events, and tumor mutation patterns (Supplementary Table 9). The total number of gene ontology terms also ranked high in feature importance, suggesting a potential bias towards high ranking of previously studied genes.

Comparison of feature distributions among TSGs, OGs, and BGs also identified known distinguishing features (Supplementary Tables 10 and 11), many of which were ranked as highly important for classification (Supplementary Table 9). Perhaps the most interesting finding is that TSGs encode significantly larger proteins than OGs (P = 1.27 × 10−5, Welch t-test). Among binary features, involvement in chromosome organization processes was a major differentiator between TSGs and OGs (P = 2.25 × 10−6).

## Tsgs Selectively Encode Very Large Driver Gene Proteins

The observation that TSGs and OGs encode large proteins had been previously noticed but not thoroughly characterized13 (Fig. 3a). Upon deeper investigation we detected a profound enrichment of TSGs and depletion of OGs, specifically among the largest proteins in the high confidence set (P = 8.56 × 10−6, hypergeometric test using the 30 largest driver proteins) (Table 2). This TSG enrichment among large driver proteins is particularly fascinating as it has been considered an artifact to some extent by previous studies10.

To alleviate the concerns that this observation is an artifact of previously suggested confounding factors, we evaluated several hypotheses as to why TSGs encode very large proteins, specifically in comparison to OGs, and found no association between any of the factors and protein size. Assessed explanations included expression levels, DNA replication timing, protein connectivity, gene deletion frequency, gene mode of inactivation, gene essentiality, gene duplications, and presence in specific gene ontology terms or pathways (Supplementary Figs 6–13, Supplementary Tables 12 and 13, and Supplementary Note).

## Large Tsgs Are Frequently Involved In Chromatin Modification

Noting that chromosome organization was the strongest feature associated with TSGs compared with OGs (Supplementary Table 10), we hypothesized that TSG protein size and chromosome organization are related. Indeed, involvement in chromosome organization was the feature most strongly associated with TSG size, with chromosome organization TSGs having a 3.8 fold-larger median coding sequence length than non-chromosome organization TSGs (P = 0.047, Welch t-test) (Fig. 3b, and Supplementary Figs 14 and 15).

The above suggests that the simple intersection of large protein size with a role in chromosome organization may pinpoint a small set of genes with potentially uncharacterized driver gene function. In fact, 19 out of the 84 high confidence TSGs (23%) are among the 92 genes that encode the top 5% largest proteins in the genome and are involved in chromosome organization (Fig. 4A). This is a 62-fold enrichment compared to TSG prevalence among the remaining genes (P = 2.3 × 10−27, hypergeometric test). In contrast, only a single high confidence OG is found among these 92 genes.

CARNAF as well as other pan-cancer/multi-tumor type studies predict an additional high concentration of putative driver genes among this focused gene set, primarily of TSG function (Fig. 4A, Supplementary Figs 16 and 17, Supplementary Tables 4 and 5, and Supplementary Note). Similar to the 84 high confidence TSGs, 13 out of the top 84 CARNAF TSG predictions encode large chromosome organization proteins, 8 of which are present in the medium confidence set (CHD8, KAT6A, KMT2A, KMT2B, KMT2E, NIPBL, NSD1, and TAF1). Two additional genes out of the 13 (INO80 and RERE) were detected as TSGs by TUSON13 (Supplementary Table 4), and the remaining 3 (PRKDC, PSME4, and SUPT6H) had little or no evidence among the 15 studies used in this work. PRKDC was only detected by the author implementation of a simple TSGs versus OGs mutation-based classifier1, PSME4 was not present in any source, and SUPT6H was ranked far below the significance threshold in TUSON (rank 709).

A review of literature for SUPT6H and PRKDC provides a degree of support for a potential driver gene role. SUPT6H encodes a histone chaperone that acts as a transcription elongation rate enhancer. The gene may suppress breast cancer as its protein levels are inversely correlated with breast cancer malignancy. It also promotes estrogen receptor-dependent transcription and chromatin structure maintenance32. PRKDC encodes a serine/threonine-kinase involved in DNA repair and recombination, with little current documentation for driver mutations within the gene. However, PRKDC inhibition sensitizes cells to irradiation33 and is synthetic lethal in MYC dependent cancers34 and with the mismatch repair gene MSH335. The latter studies suggest non-oncogene addiction to PRKDC.

The observation that a high percentage of very large chromosome organization proteins are driver genes, specifically TSGs, is consistent with the vastly growing appreciation of mutated epigenetic regulators as causal cancer drivers3637. Indeed, of the 92 genes in the above category, the majority (n = 66; 72%) are involved in chromatin modification according to gene ontology38 (Fig. 4B), with many (n = 39, 42%) specifically linked to various types of histone protein modification, primarily methylation and acetylation (Fig. 4C and Online Methods). Consistent with the above, the majority of high confidence TSGs (17 of 19) and top predicted TSGs (11 of 13) among very large chromosome organization proteins (top 5% in genome) are annotated as involved in chromatin modification. Among the 13 CARNAF predicted genes, there are 4 histone methyltransferases (KMT2A, KMT2B, KMT2E, and NSD1), 2 histone acetyltransferases (KAT6A and TAF1), and 5 genes involved in chromatin remodeling (CHD8, PSME4, RERE, SUPT6H, and INO80 which is also involved in DNA repair and chromosome segregation)38. The remaining 2 genes are involved in DNA repair (PRKDC) and chromosome segregation by loading the cohesion complex onto chromatin (NIPBL)38.

# Discussion

In this study we used diverse gene properties beyond tumor genomes to detect cancer driver genes and classify their mode of action. This integrative approach enabled us to detect literature-supported driver genes that are not present among a large compendium of driver genes derived from over a dozen efforts. We show that the largest driver genes are almost exclusively TSGs, with a remarkably dense concentration of known and putative drivers among very large proteins involved in chromatin modification. These findings highlight a small subset of candidate genes for focused experimental investigation, specifically as driver genes that modify the cancer epigenome.

The use of non-tumor genomics gene-level knowledge has been previously shown to aid in driver gene detection; however, this was typically done using a small set of select features. For example, MutSigCV uses DNA replication timing and cell line expression levels10, ActiveDriver uses phosphorylation site knowledge39, and HotNet2 uses protein network knowledge15. One exception, MAXDRIVER, uses a larger set of features, although only to detect copy number-based drivers in select tissues19. By integrating diverse gene knowledge in a pan-cancer framework, CARNAF found additional putative driver genes beyond what was previously found by other computational efforts.

Our work argues for a deeper mechanistic investigation of the link between protein size and cancer driving potential. It appears that while driver genes have high protein-protein connectivity, protein network centrality is not associated with TSG protein size and does not explain why TSGs encode large proteins compared to OGs. Perhaps evolutionary considerations and alternative gene function hypotheses may offer insight. Functionally, large genes and proteins tend to be evolutionarily conserved40, exhibit increased essentiality41, and have less redundancy and gene duplications42 as there is selective pressure for proteins to be short in order to preserve resources43. The above may guide further exploration.

The focus on very large proteins involved in chromatin modification as an enriched pool of candidate TSGs targets roughly 0.3% of the protein-coding genes in the genome for potential validation. This emphasis is consistent with the recently increased appreciation of mutated epigenetic regulators as cancer drivers3637. The above gene pool, beyond containing characterized driver genes, contains many additional genes predicted as drivers by CARNAF and other methods. Thus, this suggests that our knowledge of cancer-causing mutations to epigenome modifiers is potentially far from complete.

The TSG predictions in this highly enriched set of genes, even if functionally incorrect, may still be important cancer driver genes. For example, CARNAF predicts that the very large (top 3% in genome) histone acetyltransferase encoded by KAT6A functions as a TSG (ranked 10th top TSG prediction, Supplementary Table 8). While it was hypothesized that KAT6A may suppress cancer in response to severe DNA damage44, stronger evidence suggests an OG role as it is very frequently amplified and has been experimentally shown to act as a breast cancer oncogene and senescence inhibitor44454647.

Machine learning methods such as CARNAF provide a major advantage by systematically integrating many features for gene ranking. Beyond this study, additional scenarios can be envisioned, for example by using alternative training sets (as done previously13), performing lineage specific rather than pan-cancer analysis (as done previously48), limiting use of features with missing data or bias (e.g. gene ontology annotations towards well studied genes), including additional gene features, using a different learning methodology, and modifying various other parameters.

In this study we used machine learning techniques on a large set of publically available data to highlight a targeted set of genes for further validation as cancer drivers. Ultimately, our work suggests the presence of numerous uncharacterized, epigenetics-based driver genes, most of which are predicted TSGs, among very large regulators of chromatin structure.

# Methods

## Data Preparation

### Selection Of Driver Genes To Be Used As Training Examples

We constructed an integrated list of high confidence, protein-coding driver genes covering both mutation-based and copy number alteration driver genes. The data sources used to compile this list and the background genes list consisted of over a dozen multi-tumor type studies and databases (Supplementary Tables 3 and 4). These sources included drivers present in at least one, and often more, tumor types. Considerations for inclusion comprised source reliability, presence in multiple sources, and source confidence in the given gene. The list does not consider driver genes resulting from chromosomal rearrangements. The high confidence set was built in several sequential steps as described below.

First, we included all of the mutation driver genes (71 TSGs, 54 OGs) and copy number alteration driver genes (3 TSGs, 10 OGs) reported in Vogelstein et al. as these represent well-known, manually curated driver genes1.

Second, we supplemented the TSGs that result from deletions. We added the two genes (FANCD2 and TSC2) that were labeled by the Cosmic Cancer Gene Census (CGC)49 and by at least two of the following three sources: TAG DB3, TSGene4, and our 20/20 classifier implementation, a mutation-pattern based classifier that labels genes as TSGs or OGs1 (briefly described in Supplementary Table 3). Next, we added the four remaining genes (CDKN1B, FAT1, IKZF2, MYCN, and PARK) that were curated by Zack et al.45 as known frequently deleted TSGs.

Third, we supplemented the OGs that result from amplification. We added the 12 remaining genes (BCL2L1, CCNE1, CDK4, CDK6, E2F3, IGF1R, MCL1, NEDD9, PAX8, SOX2, TERT, and ZNF217) curated by Zack et al. as known frequently amplified OGs. We then added the four remaining genes (AKT2, JUN, MITF, and REL) that were present in both in the CGC and Santarius et al.50.

Fourth, we supplemented the mutation-based drivers by curating the remaining genes that were identified by the highest amount of mutation-based methods. All genes present in six or seven mutation methods were already included. Of the four remaining genes present in five out of seven mutation methods, we assigned two (CDK12 and CTCF) as TSGs with sufficient confidence based on manual literature curation. Of the 15 remaining genes detected by four mutation-based methods, we assigned two (ELF3 and ZFHX3) as TSGs and two (RAC1 and TBX3) as OGs based on manual literature curation.

Finally, we removed MYCN from the list as it may serve as both a TSG and OG according to the literature. Thus, MYCN was not used as a driver gene in the high confidence set.

The resulting high confidence set consisted of 84 TSGs and 81 OGs for a total of 165 driver genes, which were present in at least one tumor type. TSG mode of inactivation consisted of 46 mutation-based TSGs, 7 deletion-based TSGs, and 31 TSGs spanning either form of inactivation. OG mode of activation consisted of 46 mutation-activated OGs, 23 amplification-activated OGs, and 12 OGs that can be activated by either method.

### Selection Of Background Genes

We selected 19,486 protein-coding genes to be used in the study. The genes were derived by intersecting protein-coding genes from dbNSFP v2.4, the Gene Ontology Consortium51 (downloaded from http://geneontology.org on January 29th, 2015), and genes from Uniprot52 (http://www.uniprot.org/, downloaded on January 4, 2015) for which we could retrieve coding sequence lengths to ensure known proteins. The full list of genes can be found in Supplementary Table 1.

CARNAF requires a set of genes with little or ideally no cancer evidence to be used as negative examples. To this end, we removed the 165 high confidence driver genes and 3,349 additional genes that were reported in at least one source (Supplementary Table 4a) from the above. This resulted in 15,972 background genes (BGs) to be used as negative examples for classifier training.

### Selection Of Medium And Low Confidence Driver Gene Sets

We created medium and low confidence driver gene sets to evaluate CARNAF driver gene detection beyond high confidence drivers, the latter being the training set (n = 165). Both sets consist of non-consensus genes and are expected to contain high rates of false positives.

The medium confidence set (n = 682) includes all genes present in at least one of the following nine genomics-based sources: Zack et al. (deletion/amplification)45, CGC (deletion/amplification/mutation)49, Santarius et al. (amplification)50, Lawrence et al. (mutation)9, HotNet2 (mutation)15, MuSiC (mutation)53, OncoDriveClust (mutation)54, OncoDriveFM (mutation)55, and ActiveDriver (mutation)39. TUSON13 was not used in the above gene sets as it was the origin of our genomics features. Genes from the high confidence set were excluded.

The low confidence gene set (n = 1,360) includes genes present in at least one of the following sources and not in the medium and high confidence sets: TagDB3, TSGene4, our own 20/20 rule implementation1, and genes ranked high (absolute effect >3 in Supplementary Table 4b) as biomarkers in a high-throughput cell line study5.

### Feature Extraction-Data Sources

dbNSFP v3.0b2a was used to retrieve protein-protein interaction (PPI) data5657. PPI data included IntAct (downloaded on March 27, 2015) and BioGRID (version 3.3.122). dbNSFP v2.4 was used to retrieve GO slim terms. The GO slim terms had a Gene Ontology Consortium validation date of September 27, 2013. Full GO terms were not used as they are relatively sparse features. dbNSFP v2.4 was also used to retrieve an estimated probability of haploinsufficiency per gene58 and gene essentiality predictions based on homology with the Mouse Genome Informatics database41. Essentiality predictions had three categories: essential, non-essential but phenotype-changing, and all other genes. The coding sequence was determined as the longest isoform within the gene, as retrieved from UniProt on January 4, 2015. Ensembl BioMart was used on November 26, 2014 to retrieve the GC percent per gene and the number of transcripts per gene. Chromatin compartment and DNA replication time were retrieved from Lawrence et al.10. Duplicate gene data was retrieved from Ouedraogo et al.42. Healthy tissue gene expression data was derived by Fagerberg et al.59 and retrieved from EMBL-EBI ArrayExpress (http://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-1733/). Post-translational modification (PTM) data was downloaded from PhosphoSitePlus®, www.phosphosite.org, on September 24, 201460. All acetylation, SUMOylation, trimethylation, ubiquitination PTMs were chosen on lysine residues since such PTMs rarely occurred on other residues, thus using non-lysine residues would result in sparse features. Likewise, all tyrosine modifications were of phosphorylation type.

### Tumor-Derived Genomics Features

Four tumor mutation-pattern features were used in the study: (a) the entropy score (a measure of the randomness of mutation distribution across a gene), (b) the ratio of loss-of-function mutations to benign mutations per gene, (c) the ratio of splice site mutations to benign mutation per gene, and (d) the ratio of missense mutations predicted to have high functional impact by PolyPhen2 Hum-Var61 to benign mutations per gene. These four features were shown to be highly informative for TSG and OG classification, and were extracted from the original study13.

Somatic gene amplification and deletion frequency, specifically GISTIC2 p-values62, was extracted from the above study13.

### Feature Extraction-Computations

Several of the features we used required some computation, as detailed below.

Genomic density: The genomic density of a gene was determined as in previous work by quantifying the number of genes that reside within 4Mb upstream or downstream from the center chromosomal position of the gene, and then dividing by the mean of this number63.

Number of PPIs: The number of PPIs per gene was calculated as the average number of interactions present in both sources (BioGrid and IntAct) as retrieved from dbNSFP v3.0b2a.

Betweenness centrality: Betweenness centrality was calculated by running the Brandes algorithm64, using the iGraph R package65, on the BioGRID PPIs (Release: 3.2.111), which were accessed via the rTRM package66 for this purpose.

### Non-Tumor Genomics Features Considered But Not Used

An effort was made to reduce feature redundancy by avoiding the use of multiple data sources for the same feature type. For example, we did not use pathway data from the Kyoto Encyclopedia of Genes and Genomes to prevent redundancy with GO slim biological process terms.

In addition, we evaluated protein and mRNA stability data but ultimately did not include these features as the data was typically incomplete. Regarding mRNA turnover rates, human datasets have half-life data for only up to approximately 50% of protein-coding genes676869. Likewise, protein stability data exists for roughly 40% of genes7071. In contrast to humans, global mRNA stability data does exists for the majority of mouse genes in ES cells72.

We also evaluated InterPro protein features, retrieved from Ensembl BioMart on November 26, 2014. InterPro contains data on protein families, domains, and functional sites. However, as only 1 of the 7,132 extracted features passed feature selection due to high sparsity, we opted to omit InterPro features.

### Total Features Used And Feature Removal

A total of 131 features were used by CARNAF after two sequential feature removal steps: sparse feature removal and correlated feature removal.

### I) Sparse Features

Identification and removal of sparse features was performed using the R caret package73. Sparse features were defined as features satisfying two criteria: the ratio between the frequency of the first and second most common values was larger than 97/3, and the percentage of unique values out of the number of genes was smaller than 3%. A value of ‘unknown’ was also considered a unique value, thus leading to the omission of features with substantial levels of missing values.

### Ii) Removal Of Correlated Features

To avoid redundancy, features were omitted if they were highly correlated to other features using the R caret package. Two features were considered highly correlated if they had a Spearman correlation coefficient with an absolute value >0.95. For each pair of correlated features, the feature with the greater mean absolute correlation with the remaining features was removed. After this stage, 131 features remained for use by CARNAF.

### Missing Data Imputation

Missing values for features that were not omitted in the previous stage were imputed via the k-nearest neighbor procedure using the R caret package. For each gene, missing values were imputed according to the mean value of its 5 nearest neighbors, where similarity was measured using Euclidean distance. Features that could not be imputed because the same feature was missing in all 5 nearest neighbors were imputed as the median using all genes in the sample.

### Additional Data Sources Used In Study, But Not In Carnaf

Tissue expression data in binary format was used in Supplementary Table 12c-d. The expression data source GNF/Atlas (BioGPS) was downloaded from Ensembl BioMart on October 1, 2013 and retrieved via dbNSFP v3.0b2a. Cancer cell line expression data was retrieved from Lawrence et al.10. The data is presented in Supplementary Table 2.

## Carnaf Methodology

### Pu Learning

CARNAF employs PU learning207576, wherein genes without cancer evidence are treated as negative labels in an ensemble learning approach, where many classifiers are trained on different subsets of the data. This approach has been compared favorably with methods that do not make use of unlabeled or negative example genes, such as Endeavour17, Toppgene77, or density estimators78. The theoretical merits of this approach have been previously discussed22.

### Classification

Classification of genes as TSGs, OGs, or non-driver genes was performed using a random forest classifier21. Random forests enable multi-class classification and have been demonstrated to often outperform other well-known classifiers in a variety of predictive modeling domains79. Briefly, a random forest is an ensemble of a large number of decision tree classifiers, each of which is assigned to a random bootstrapped sample of the data as its training set. Random forest classifiers also compute feature importance, in addition to classification, by quantifying the mean decrease in node impurity (also known as Gini index) gained by splitting a node in a decision tree according to each feature. We employed the R randomForest package80 using 100,000 trees for each classification task and the caret R package for parameter tuning73. For each gene, the posterior probability of being a TSG, OG, or background gene was computed according to all the classifiers to which it was not assigned. This procedure is known as out of bag estimation.

### Unbalanced Classes

The training data contains 97-fold more background genes than driver genes. We used a stratified down-sampling approach to deal with this class imbalance, where each decision tree in the ensemble was assigned a random subset of the data. Data subsets consisted of the 165 high confidence driver genes and 165 randomly selected negative example genes, where each was sampled with replacement using the “sampsize” option of the R package randomForest. A similar approach was previously recommended in a PU learning setting22. We note that while the estimated posterior driver gene probabilities are useful for gene ranking, they should not be regarded as the true posterior probability of being a driver due to the down-sampling procedure.

### Receiver Operating Characteristic (Roc) Curve For Tsg Vs Og Classification

ROC curves were calculated using the 84 TSG and 81 OG driver genes. TSG labels were set to 1 and OG labels to 0. The probability of the label equaling one was defined as



# Additional Information

How to cite this article: Waks, Z. et al. Driver gene classification reveals a substantial overrepresentation of tumor suppressors among very large chromatin-regulating proteins. Sci. Rep. 6, 38988; doi: 10.1038/srep38988 (2016).

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

