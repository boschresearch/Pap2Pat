# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior publication

## BACKGROUND

- motivate medical image normalization

## SUMMARY

- outline stain normalization method

## DETAILED DESCRIPTION

- describe general embodiments and high-level variants of the invention

### 1. General Embodiments and High-Level Variants

- introduce computer-implemented method for normalizing medical images
- describe steps of the method, including estimating actual quantities and assessing quality
- explain selection of effective quantities based on quality assessment
- describe normalization step based on effective quantities
- discuss advantages of the method, including alleviating normalization errors
- introduce variants of the method, including computing RGB histogram to identify artifacts
- describe computation of stain concentrations and maximum concentrations
- explain selection of reference quantities and updating of reference data
- discuss assessment of actual quantities based on boundary values or distance metrics
- describe use of boundary values to define subsets of good-quality and bad-quality images
- explain incremental update of reference data based on good-quality images
- discuss application of the method in a cognitive medical pipeline

### 2. Specific Embodiments—Technical Implementation Details

- introduce stain normalization system architecture
- describe multi-core implementation
- discuss processing high-resolution images
- describe method to detect poor-quality images
- describe normalization method for poor-quality images
- describe application of stain normalization in ML pipelines
- describe CNN model training and inference
- introduce computerized units
- describe hardware architecture of computerized unit
- describe software components of computerized unit
- describe computer program products
- describe computer readable storage medium
- describe cloud computing infrastructure

