# DESCRIPTION

## FIELD OF THE INVENTION

- define invention scope

## BACKGROUND

- motivate phenocopy signatures

## SUMMARY OF THE INVENTION

- generate phenocopy signatures
- identify cells with phenocopy signatures
- predict and treat cells and subjects

## DETAILED DESCRIPTION OF THE INVENTION

- introduce phenocopy signature generation methods
- define biological pathway
- describe biological pathway databases
- introduce disease pathways
- exemplify diseases resulting from disease pathways
- define key driver gene
- introduce gene set identification
- describe gene set composition
- introduce training cell identification
- describe training cell composition
- obtain nucleic acid sequences for genes
- identify mutation set
- describe mutation types
- obtain gene expression profiles
- describe gene expression profile composition
- determine gene expression signatures
- describe gene expression signature composition
- predict mutation presence using gene expression signatures
- describe prediction accuracy
- introduce phenocopy signature determination
- describe phenocopy signature independence from drug-response data
- introduce methods of identifying cells exhibiting a phenocopy signature
- define phenocopy signature
- describe gene expression profile matching
- outline methods for identifying test cells
- specify test cell characteristics
- describe methods for identifying subjects with phenocopy signature
- outline methods for predicting subject sensitivity to drug treatment
- describe biological pathway targeting by drugs
- specify drug targeting mechanisms
- outline methods for identifying drugs targeting biological pathways
- describe phenocopy signature generation without empirical data
- outline methods for predicting cell sensitivity to drug treatment
- describe optional treatment steps
- provide general patent application information

### EXAMPLES

- hypothesize RNA phenocopy signatures of key cancer driver gene mutations
- introduce targeted therapies against oncogenic pathways
- motivate limitations of DNA mutations in predicting response to targeted therapies
- describe transcriptomic changes associated with oncogenic pathway activation
- introduce phenocopy signatures as a solution to improve predictions of response to targeted therapies
- describe the training of phenocopy signatures on DNA alterations in the TCGA dataset
- filter genes within the pathway of interest using the Reactome database
- apply gradient tree boosting approach to train phenocopy signatures
- describe the independent validation of phenocopy signatures in GDSC, CCLE, and DepMap
- assess response for drugs specifically targeting each pathway
- create linear models to compare phenocopy signatures and DNA mutations in predicting drug response
- perform likelihood-ratio test to assess significance of phenocopy signatures
- assess sensitivity and specificity of phenocopy signatures in predicting drug response
- stratify responders and non-responders based on top quartile vs. bottom three quartiles
- consider three subgroups: cell lines without mutations, with unknown significance mutations, and with pathogenic mutations
- describe data availability and processing
- introduce model design and phenocopy signature predictions
- investigate discordance between actual DNA mutation status and phenocopy predictions
- assess if phenocopy signatures improve pan-cancer drug response predictions across multiple pathways
- examine linear models of drug response to treatment targeting each pathway
- calculate multiple-testing FDR-corrected chi-squared statistic for each drug/gene combination
- evaluate sensitivity, specificity, PPV, and NPV of phenocopy signatures
- clinically validate phenocopy signatures in BRAF and mTOR pathways

## DISCUSSION

- motivate phenocopy approach
- describe advantages over DNA mutation status alone

