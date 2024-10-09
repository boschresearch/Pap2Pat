# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- introduce renal cancer statistics
- discuss limitations of current imaging techniques
- motivate need for biopsy
- discuss challenges of needle biopsy
- introduce DNA methylation as potential solution
- discuss advantages of DNA methylation markers
- motivate investigation of DNA methylation markers

## SUMMARY OF THE INVENTION

- introduce method of classifying kidney tumors
- describe obtaining and isolating DNA sample
- determine methylation status of DNA
- compare methylation status to methylated biomarkers
- introduce methylated biomarkers
- describe methylation sensitive assays
- introduce embodiments of sample types
- introduce embodiments of methylated biomarkers
- introduce embodiments of sequence regions
- introduce method of identifying subjects with renal cancer
- introduce composition of methylated biomarkers

## DETAILED DESCRIPTION OF THE INVENTION

- define biomarker
- define cancer
- define subject
- describe use of DNA methylation data from The Cancer Genome Atlas (TCGA)
- describe building a classification model to predict subtypes of kidney tumor
- describe application of the classifier to predict malignancy and tissue subtype
- describe use of a computer to implement the invention
- describe system comprising a non-transitory computer readable medium
- describe generating a report based on the comparison
- describe preferred embodiment of the invention
- describe scope of the invention

### Development of a DNA Methylation Classifier to Subtype Kidney Tumors

- describe RCC and its subtypes
- describe building a classification model using Illumina Infinium HumanMethylation450 (HM450) DNA methylation data
- describe multidimensional scaling plot of the 697 training samples
- describe selecting features for each subgroup
- describe building a multi-group classifier to predict tissue subtype
- describe evaluating the classifier on the training data
- describe results of the classifier

### Using Ex Vivo SRM Needle Biopsies to Validate the Developed Classification Model

- describe obtaining ex vivo needle biopsy samples
- describe predicting probabilities for the six phenotypes
- describe evaluating classification error
- describe results of the classifier
- describe evaluating entropy
- describe results of entropy evaluation
- describe predicting malignancy and subtype
- describe results of prediction
- describe using multiple needle biopsies
- describe results of using multiple needle biopsies
- describe treatment decision making for SRMs
- describe limitations of needle biopsy
- describe combining molecular markers with histological results
- describe potential benefits of the invention
- describe American Urological Association recommendations
- describe using TCGA database
- describe results of the study

### Example 3—Methods

- describe patient material, samples, and marking
- describe collecting ex vivo samples
- describe collecting FFPE-microdissected samples
- describe training data
- describe DNA methylation profiling
- describe processing HM450 profiles
- describe correcting for background intensity
- describe pre-selecting DNA methylation markers
- describe creating MDS plot and heatmap
- describe L1-penalized classification model
- describe testing the model
- describe evaluating classification error rates

