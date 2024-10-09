# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce gene regulation
- motivate transcription factor binding sites
- limitations of current methods
- introduce Nkx2.2 transcription factor
- motivate new mechanisms

## SUMMARY

- introduce systems for identifying binding sites
- outline system components
- describe enrichment score calculation
- outline method for identifying binding sites
- describe computer readable media
- summarize output of method

## DETAILED DESCRIPTION

- introduce transcription factor Nkx2.2
- describe protein binding microarray (PBM) analysis
- explain enrichment score (E-score) calculation
- show E-score distribution table of octamers on Nkx2.2
- select octamers with E-score greater than 0.45
- remove octamers containing known core sequence
- identify alternative core sequence
- calculate average E-score for octamers containing AAGT and GAGT
- plot histogram of occurrences of each possible base in first position
- experimentally test alternative GAGT binding site using EMSA
- map PBM data to genome to identify putative binding sites
- use E-score to predict Nkx2.2 binding sites
- map single octamers with E-score greater than 0.4
- use moving average of seven octamers to predict binding affinity
- illustrate PBM-mapping process
- receive PBM data and genome sequence
- form array of seven overlapping octamers
- assign E-scores to octamers in array
- calculate average E-score for array
- determine if average E-score is above threshold
- update database of binding sites
- analyze complete genome using PBM-mapping
- search for sites in bound promoter regions
- test sites using EMSA
- confirm sites using ChIP
- perform EMSA analysis of selected predicted sites
- perform ChIP analysis of predicted sites
- quantify relative Nkx2.2 binding affinity
- graph E-score against relative binding affinity
- compare E-score to TRANSFAC PWM score and PBM seed and wobble matrix score
- test single E-scores and averages of overlapping octamers
- show highest correlation with relative binding affinity
- apply mechanism to other transcription factor binding sites
- generate composite transcription factor binding site maps
- identify promoters with significantly different predictions
- analyze NeuroD promoter
- identify novel site upstream of TRANSFAC predicted sites
- confirm binding to PBM mapping predicted site
- analyze insulin promoter
- identify Nkx2.2 binding site not predicted by PBM-mapping
- confirm Nkx2.2 occupancy using ChIP
- perform luciferase assays to assess Nkx2.2 function
- implement techniques in computer systems
- store instructions in computer readable media
- describe flexibility of the invention

