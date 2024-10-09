# DESCRIPTION

## TECHNICAL FIELD

- relate to method and system

## BACKGROUND

- motivate need for improvement

## SUMMARY

- introduce method
- sequence genome sample
- align sequencing result
- determine breakpoints
- determine detection window
- determine first parameter
- determine copy number variation
- introduce system
- describe system components
- introduce computer readable medium
- describe computer readable medium function

## DETAILED DESCRIPTION

- define copy number variation
- introduce method of determining copy number variation
- describe sequencing genome sample
- explain extracting genome sample from biological sample
- detail types of biological samples
- describe isolating single cell from biological sample
- explain methods of sequencing genome sample
- detail constructing sequencing-library
- describe sequencing constructed sequencing-library
- explain lysing single cell to release whole genome
- detail methods of amplifying single cell whole genome
- describe sequencing whole genome sequencing-library
- explain lengths of sequencing data
- align sequencing result to reference genome sequence
- determine distribution of reads in reference genome sequence
- calculate total number of sequencing data
- select uniquely aligned reads
- determine breakpoints in reference genome sequence
- divide reference genome sequence into primary windows
- determine reads falling into primary windows
- determine number of reads at both sides of site
- perform correlation analysis
- determine p value of site
- determine final p value
- calculate relative number of reads
- perform run test
- correct relative number of reads for GC content
- determine normalized number of reads
- perform run test on normalized number of reads
- calculate GC content of each primary window
- divide GC content into regions
- calculate mean value of relative number of reads
- determine corrected relative number of reads
- determine normalized number of reads
- define formula for Z
- define formula for mean
- define formula for SD
- eliminate bias of genome amplification
- determine possibility of copy number variation
- determine detection windows
- determine candidate breakpoints
- determine p value of each candidate breakpoint
- remove candidate breakpoint with maximal p value
- perform step 8 until p values are smaller than terminate p value
- determine region between two successive screened candidate breakpoints as detection window
- obtain p value of candidate breakpoint using run test
- determine final p value
- determine first parameter based on reads falling in detection window
- determine whether copy number variation presents in genome sample
- compare first parameter to preset threshold
- determine type of copy number variation
- set boundary of significance
- determine copy number variation in genome sample
- solve problem of analyzing single cell or trace of nucleic acid sample
- avoid bias to analyzing copy number variation
- improve detection efficiency
- introduce different indexes during constructing sequencing-library
- improve efficiency of determining copy number variation
- provide genetic counseling and basis for clinic decision
- prevent implantation of embryo with lesion
- describe system for determining copy number variation
- configure sequencing apparatus
- extract genome sample from biological sample
- amplify genome sample
- construct sequencing-library
- sequence sequencing-library
- determine whether copy number variation presents in genome sample
- align sequencing result to reference genome sequence
- define detailed description
- describe breakpoint determining unit
- calculate GC content
- divide GC content into regions
- calculate mean value of relative number of reads
- determine corrected relative number of reads
- determine normalized number of reads
- determine detection window
- determine possibility of copy number variation
- screen breakpoints
- determine p value of candidate breakpoint
- remove candidate breakpoint with maximal p value
- repeat step 12 until p values of rest of candidate breakpoints smaller than terminate p value
- determine final p value
- determine detection window based on screened candidate breakpoints
- determine first parameter based on reads falling in detection window
- determine whether copy number variation presents based on difference between first parameter and preset threshold
- describe computer readable medium
- preserve order in computer readable medium
- align sequencing result to reference genome sequence
- determine distribution of reads in reference genome sequence
- determine breakpoints based on distribution of reads
- determine detection window based on breakpoints
- determine first parameter based on reads falling in detection window
- determine whether copy number variation presents based on difference between first parameter and preset threshold
- describe general method
- amplify whole genome sample
- sequence amplified whole genome
- align reads to standard human genome reference sequence
- calculate relative number of reads
- correct and normalize data
- determine breakpoints
- screen breakpoints
- determine final p value
- determine detection window and verify detection window
- describe example 1
- perform whole genome amplification
- perform sequencing and data analysis

### Example 2

- repeat experiment without amplification
- compare and discuss results

## INDUSTRIAL APPLICABILITY

- claim industrial applicability
- define embodiment scope

