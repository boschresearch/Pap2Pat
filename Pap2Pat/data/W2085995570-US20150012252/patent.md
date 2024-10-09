# DESCRIPTION

## TECHNICAL FIELD

Embodiments of the present disclosure generally relate to a method of determining whether copy number variation presents in a genome sample, and a system and a computer readable medium thereof.

## BACKGROUND

In fields of scientific research and application, problems of analyzing a single cell, a plurality of cells, or a trace of nucleic acid sample usually come out, for example, Pre-implantation Genetic Diagnosis (PGD) and Pre-implantation Genetic Screening (PGS) in a field of assisted reproductive technology involve analysis with a single germ cell, a single blastomeric cell or an embryonic cell; a field of non-invasive prenatal diagnosis technology involves problem of detecting a trace of fetal cells in maternal peripheral blood; Metagenomics involves analysis with a single or a trace of biological cell in environment; and disease or physical research involves analysis with a single cell in tissue or body fluid.

However, currently the method of determining copy number variation still needs to be improved.

## SUMMARY

Embodiments of the present disclosure seek to solve at least one of the problems existing in the related art to at least some extent.

Embodiments of a first broad aspect of the present disclosure provide a method of determining whether copy number variation presents in a genome sample. According to embodiments of the present disclosure, the method may comprise following steps: sequencing the genome sample, to obtain a sequencing result consisting of a plurality of reads; aligning the sequencing result to a reference genome sequence, to determine a distribution of the reads in the reference genome sequence; determining a plurality of breakpoints in the reference genome sequence based on the distribution of the reads in the reference genome sequence, wherein the number of reads has significance at both sides of the breakpoints; determining a detection window in the reference genome based on the plurality of the breakpoints; determining a first parameter based on reads falling in the detection window; and determining whether the copy number variation presents in the genome sample against the detection window based on difference between the first parameter and a preset threshold. By using the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, whether copy number variation presents in a genome sample may be effectively determined, which is suitable for various copy number variations, included but not limited to aneuploidy of chromosome, deletion of chromosome, and addition, micro-deletion and micro-repetition of chromosome fragments.

Embodiments of a second broad aspect of the present disclosure provide a system for determining whether copy number variation presents in a genome sample. According to embodiments of the present disclosure, the system may comprise:

a sequencing apparatus, configured to sequence the genome sample, to obtain a sequencing result consisting of a plurality of reads; an analysis apparatus, connected to the sequencing apparatus, configured to determine whether copy number variation presents in the genome sample based on the sequencing result, wherein the analysis apparatus further comprises: an aligning unit, configured to align the sequencing result to a reference genome sequence, to determine a distribution of the reads in the reference genome sequence; a breakpoint determining unit, connected to the aligning unit, configured to determine a plurality of breakpoints in the reference genome sequence, based on the distribution of the reads in the reference genome sequence, wherein the number of reads has significance at both sides of the breakpoints; a detection window determining unit, connected to the breakpoint determining unit, configured to determine a detection window in the reference genome based on the plurality of the breakpoints; a parameter determining unit, connected to the detection window determining unit, configured to determine a first parameter based on reads falling in the detection window; and a determining unit, connected to the parameter determining unit, configured to determine whether the copy number variation presents in the genome sample against the detection window based on difference between the first parameter and a preset threshold. By using the system for determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure may be effectively implemented, which is suitable for various copy number variations, included but not limited to aneuploidy of chromosome, deletion of chromosome, and addition, micro-deletion and micro-repetition of chromosome fragments.

Embodiments of a third broad aspect of the present disclosure provide a computer readable medium. According to embodiments of the present disclosure, the computer readable medium is configured to perform by a processor to determine whether copy number variation presents in a genome sample through following steps: aligning the sequencing result to a reference genome sequence, to determine a distribution of the reads in the reference genome sequence; determining a plurality of breakpoints in the reference genome sequence based on the distribution of the reads in the reference genome sequence, wherein the number of reads has significance at both sides of the breakpoints; determining a detection window in the reference genome based on the plurality of the breakpoints; determining a first parameter based on reads falling in the detection window; and determining whether the copy number variation presents in the genome sample against the detection window based on difference between the first parameter and a preset threshold. By virtue of the computer readable medium, the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure may be effectively implemented, so as to effectively determine whether copy number variation presents in a genome sample, which is suitable for various copy number variations, included but not limited to aneuploidy of chromosome, deletion of chromosome, and addition, micro-deletion and micro-repetition of chromosome fragments.

Additional aspects and advantages of embodiments of present disclosure will be given in part in the following descriptions, become apparent in part from the following descriptions, or be learned from the practice of the embodiments of the present disclosure.

## DETAILED DESCRIPTION

Reference will be made in detail to embodiments of the present disclosure. The same or similar elements and the elements having same or similar functions are denoted by like reference numerals throughout the descriptions. The embodiments described herein with reference to drawings are explanatory, illustrative, and used to generally understand the present disclosure. The embodiments shall not be construed to limit the present disclosure

In addition, terms such as “first” and “second” are used herein for purposes of description and are not intended to indicate or imply relative importance or significance. Thus, features defined with “first” or “second” may explicitly or implicitly include one or more of said feature. Furthermore, in descriptions of the present disclosure, unless otherwise specified, “a plurality of” refers to two or more. If not specified, in formula or signs used herein, the same alphabet represents a same meaning.

I. Method of Determining Whether Copy Number Variation Presents in a Genome Sample

According to a first aspect of the present disclosure, there is provided a method of determining whether copy number variation presents in a genome sample in the present disclosure. Term of “copy number variation (CNV)” used herein refers to abnormality of chromosome or chromosome fragment copy number, including but not limited to chromosome aneuploidy, chromosome fragment deletion, addition, micro-deletion and micro-repeat of chromosome fragment.

Referring to FIG. 1, the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure comprises:

S100: Sequencing the Genome Sample, to Obtain a Sequencing Result Consisting of a Plurality of Reads

According to embodiments of the present disclosure, types of the genome samples with which the method of the present disclosure are not subjected to special restrictions, which may be a whole genome or a part of a genome, for example, chromosome or chromosome fragment. Besides, according to embodiments of the present disclosure, prior to the step of sequencing the genome sample, the method of determining whether copy number variation presents in a genome sample may further comprise a step of extracting the genome sample from a biological sample. Accordingly, the biological sample may be directly used as raw material, for obtaining information regarding whether the biological sample has copy number variation, so as to reflect health status of organisms. According to embodiments of the present disclosure, the used biological sample is not subjected to special restrictions. According to some specific examples of the present disclosure, the biological sample is any one selected from a group consisting of blood, urine, saliva, tissue, germ cells, oosperm, blastomere and embryo. It would be appreciated by those skilled in the art that different biological samples may be used for analyzing different diseases. Accordingly, these samples may be conveniently obtained from organisms, and different samples may be used specifically directing to certain diseases, so as to selecting specific means for analyzing the certain diseases. For example, for a subject possibly suffering a certain cancer, a sample may be collected from cancerous tissue or juxtacancerous tissue, from which cells are further isolated for analysis, accordingly, whether such tissue become cancerous may be accurately determined as early as possible. According a specific example of the present disclosure, a single cell may be used as the biological sample. According to embodiments of the present disclosure, methods and devices of isolating a single cell from a biological sample are not subjected to special restrictions. According to some specific examples of the present disclosure, a single cell may be isolated from a biological sample using at least one of dilution, mouth-controlled pipette, micromanipulation (micro-dissection is preferred), flow cytometry isolation, microfluidics. Accordingly, a single cell may be effectively and conveniently obtained from a biological sample, to implement subsequent steps. Then, efficiency of determining whether copy number variation presents in a genome sample may be further improved.

Besides, according to embodiments of the present disclosure, methods of sequencing the genome sample are not subjected to special restrictions. According to an embodiment of the present disclosure, the step of sequencing the genome sample further comprises following sub-steps of: firstly amplifying the genome sample, to obtain an amplified genome sample; secondly, constructing a sequencing-library with the amplified genome sample; finally sequencing the constructed sequencing-library, to obtain the sequencing result consisting of a plurality of reads. Accordingly, whole genome information of the sequencing result of the genome sample may be effectively obtained, and a single cell genome or a trace of nucleic acid sample may be subjected to effective sequencing, which may further improve efficiency of determining whether copy number variation presents in a genome sample. Those skilled in the art may choose different methods of constructing a sequencing-library in accordance with specific solutions used in genome sequencing techniques. A detailed process of constructing a genome sequencing-library may refer to a specification provided by sequencing-instrument manufacturer, such as Illumina Company, for example Multiplexing Sample Preparation Guide (Part#1005063; February 2010), which is incorporated herein by reference.

Optionally, for the step of extracting the genome sample from the biological sample when being a single cell, according to embodiments of the present disclosure, the method may further comprise a step of lysing the single cell, to release whole genome of the single cell. According to some examples of the present disclosure, methods of lysing the single cell to release whole genome are not subjected to special restrictions, as long as the single cell is lysed, preferably the single cell is fully lysed. According to specific examples of the present disclosure, the single cell is lysed using an alkaline lysate, to release whole genome of the single cell. Inventors of the present disclosure find out that the step of lysing the single cell may effectively lyse the single cell to release whole genome, and accuracy may be improved when subjecting the released whole genome to sequencing, which may further improve efficiency of determining whether copy number variation presents in a genome sample. According to embodiments of the present disclosure, methods of amplifying a single cell whole genome are not subjected to special restrictions, a PCR-based method may be used, for example PEP-PCR, DOP-PCR and OmniPlex WGA; a non-PCR-based method may be also used, for example Multiple Displacement Amplification (MDA). According to specific examples of the present disclosure, the PCR-based method is preferably used, for example OmniPlex WGA. A commercial kit, including but not limited to GenomePlex from Sigma Aldrich, PicoPlex from Rubicon Genomics, REPLI-g from Qiagen, illustra GenomiPhi from GE Healthcare and etc, may be used. According to specific examples of the present disclosure, prior to the sub-step of constructing a sequencing-library, the single cell whole genome may be amplified by OmniPlex WGA. Accordingly, the whole genome may be effectively amplified, which may further improve efficiency of determining whether copy number variation presents in a genome sample. According to embodiments of the present disclosure, the sub-step of sequencing the whole genome sequencing-library is performed by at least one selected from Next-Generation sequencing technology consisting of Hiseq system of Illumina Company, Miseq system of Illumina Company, Genome Analyzer (GA) system of Illumina Company, 454 FLX of Roche Company, SOLiD system of Applied Biosystems Company, Ion Torrent system of Life Technologie Company. Accordingly, characteristics of high-throughput and deep sequencing of these sequencing apparatus may be used, which further improves efficiency of determining whether copy number variation presents in a genome sample. Obviously, it would be appreciated by those skilled in the art that other sequencing methods and apparatuses may also be used for whole genome sequencing, for example Third-Generation sequencing technology (i.e., single molecule sequencing technology) such as any one of HeliScope system from Helicos BioSciences Company, RS system from PacBio Company and etc, as well as more advanced sequencing technology which may be developed later. According to embodiments of the present disclosure, lengths of sequencing data obtained by whole genome sequencing are not subjected to special restrictions. According to an specific example of the present disclosure, the plurality of sequencing data have an average length of about 50 bp. The inventors of the present disclosure surprisingly find out that sequencing data having a length of about 50 bp may greatly facilitate subjecting the sequencing data to analyzing, which improves analysis efficiency and significantly reduces cost for analysis, by which further improves efficiency of determining chromosome aneuploidy of a single cell and reduces cost of determining chromosome aneuploidy of a single cell. Term of “average length” used herein refers to a mean value of length values of every sequencing data.

S200: Aligning the Sequencing Result to a Reference Genome Sequence, to Determine a Distribution of the Reads in the Reference Genome Sequence

After completing the step of sequencing the genome sample, the obtained sequencing result includes a plurality of sequencing data. The obtained sequencing result is aligned to a reference genome sequence, so as to determine a location of the obtained sequencing result in the reference genome sequence. According to embodiments of the present disclosure, any known methods may be used to calculate the total number of these sequencing data. For example, software provided by sequencing instrument manufacturer may be used for analysis. Short Oligonucleotide Analysis Package (SOAP) and Burrows-Wheeler Aligner (BWA) are preferably used, which align reads to a reference genome sequence, to obtain a location of reads in the reference sequence. A default parameter provided by program of the software may be used in alignment, or a parameter may be selected by those skilled in the art as required. In an embodiment of the present disclosure, SOAPaligner/soap2 is used as alignment software.

According to embodiments of the present disclosure, the reference genome sequence may be a standard human genome reference sequence in NCBI database (for example may be hg18, NCBI Build 36); or may be a part of a known genome sequence, for example may be at least one sequence selected from a group consisting of human chromosome 21, chromosome 18, chromosome 13, chromosome X and chromosome Y.

According to embodiments of the present disclosure, by the step of aligning the sequencing result to a reference genome sequence, sequences which are uniquely aligned to the reference genome sequence may be selected for subsequent analysis. Accordingly, interference to analysis of copy number variation by repeat sequences may be avoided, which further improves efficiency of determining whether copy number variation presents in a genome sample.

S300: Determining a Plurality of Breakpoints in the Reference Genome Sequence Based on the Distribution of the Reads in the Reference Genome Sequence

Term of “breakpoints” used herein refers to such kind of sites in a genome, in which the number of the reads on either side of the site are significantly different between these two regions. As reads derive from the genome sample, when a certain region presents copy number variation in the genome sample, the number of the reads corresponded in the region also changes significantly. Accordingly, after determining a plurality of breakpoints, copy number variation probably presents in a region between two successive breakpoints may be preliminary determined.

According to embodiments of the present disclosure, the step of determining a plurality of breakpoints in the reference genome sequence further comprises following sub-steps:

Firstly, the reference genome sequence is divided into a plurality of primary windows having a predetermined length, and reads falling into the primary windows are determined. According to specific examples of the present disclosure, by conventional alignment programs, reads contained in the obtained sequencing result may be aligned to the reference genome sequence, by which reads falling into the primary windows may be determined, for example, it may be accomplished in the step S200 above-described. According to specific examples of the present disclosure, the reads falling into each of the primary windows are uniquely-aligned reads. Accordingly, interference to analysis of copy number variation by repeat sequences may be avoided, which further improves efficiency of determining whether copy number variation presents in a genome sample.

Secondly, for at least one site in the reference genome sequence, determining the number of reads falling in the primary windows having the same number at both sides of the site. According to embodiments of the present disclosure, correlation analysis may be performed with all sites in the reference genome sequence, or with interested chromosome, for example such correlation analysis is performed with all sites in at least one of human chromosome 21, chromosome 18, chromosome 13, chromosome X and chromosome Y. According to embodiments of the present disclosure, each of the primary windows may have same or different length; an overlap may present between primary windows, as long as information of each primary window is known; each of the primary windows is preferably has a same length. According to embodiments of the present disclosure, each of the primary windows may have a length of 100 to 200 Kbp, preferably 150 Kbp. According to embodiments of the present disclosure, the number of the primary windows located at both sides of the site is not subjected to special restrictions, according to a specific example of the present disclosure, 100 of the primary windows may be selected from either side of the site respectively.

Thirdly, by statistical analysis, p value of the site may be determined, in which the p value represents that the number of reads falling in either side of the site has significance. If the p value of the site is smaller than a final p value, that the site is the breakpoints is determined. According to embodiments of the present disclosure, a range of the final p value may be determined by subjecting a known sequence sample to parallel analysis, according to a specific example of the present disclosure, the final p value is 1.1×10−50.

According to an embodiment of the present disclosure, the sub-step of determining p value of the site further comprises:

For the selected site, primary windows having the same number at either side of the site are selected, the relative number of reads falling in each primary window Ri is calculated, in which i represents the No. of the primary windows,

the relative number of reads falling in all primary windows Ri are subjected to run test, to determine the p value of the site, in which

the relative number of reads is determined by following formula:

\(R_{i} = {\log_{2}\left( \frac{r_{i}}{\overset{\_}{r}} \right)}\)

in which ri represents the number of reads falling in the i-th primary window,

\({\overset{\_}{r} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}r_{i}}}},\)

n represents the total number of the primary windows.

In details, the step of subjecting the relative number of the reads falling in all primary windows to run test further comprises: subjecting the relative number of reads falling in each of the primary windows Ri to a correction of GC content, to obtain corrected relative number of reads {tilde over (R)}i; determining the normalized number of reads falling in each of the primary windows Zi based on the corrected relative number of reads; and subjecting all of the normalized number of reads falling in each of the primary windows Zi to run test.

More specifically, the corrected relative number of reads {tilde over (R)}i is obtained by following steps:

Firstly GC content of each primary window is calculated;

Secondly, the GC content is divided into a plurality of regions in accordance with a predetermined value, and a mean value Ms of the relative number of reads falling in each of the plurality of regions is calculated, in which s is No. of the plurality of regions, according to embodiments of the present disclosure, the predetermined value may be any numerical value in a range of 0.0005 to 0.01, of which a corresponding region has a length of 50 k to 300 k, 0.001 is preferred, by which may performing a correlation with an optimal power.

Thirdly, the corrected relative number of reads {tilde over (R)}i is determined based on the =following formula:

{tilde over (R)}i=Ri−Ms.

Lastly, the normalized number of reads Zi is determined based on the following formula, in which

\(Z_{i} = {\left( {R_{i} - {\overset{\sim}{R}}_{i} - {mean}} \right)/{SD}}\)
\({mean} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}\left( {R_{i} - {\overset{\sim}{R}}_{i}} \right)}}\)
\({SD} = {\sqrt{\frac{1}{n - 1}{\sum\limits_{i = 1}^{n}\left( {R_{i} - {\overset{\sim}{R}}_{i} - {mean}} \right)^{2}}}.}\)

Accordingly, the number of reads may be subjected to correlation by GC content. Thus, an interference caused by bias of genome amplification may be eliminated, by which improves accuracy and efficiency of determining whether copy number variation presents in a genome sample.

After the plurality of breakpoints has been determined, a possibility that copy number variation presents in a region between two successive breakpoints may be preliminary determined. Accordingly such regions may be taken as the detection windows for further determining whether copy number variation presents. In the case of obtaining relative more breakpoints in the preliminary determination, the obtained breakpoints may be subjected to further screening. Accordingly, according to embodiments of the present disclosure, the step of determining a detection window in the reference genome based on the plurality of the breakpoints further comprises:

1) determining a plurality of candidate breakpoints, wherein other breakpoints present both before and after the candidate breakpoints;

2) determining p value of each candidate breakpoint, and removing a candidate breakpoint having the maximal p value;

3) performing the step 2) with rest of the candidate breakpoints until p values of the rest of the candidate breakpoints all smaller than the terminate p value, wherein the rest of the candidate breakpoints are taken as screened candidate breakpoints; and

4) determining a region between two successive screened candidate breakpoints as the detection window.

According to embodiments of the present disclosure, the p value of the candidate breakpoint is obtained by following steps:

selecting a region between the candidate breakpoint and previous candidate breakpoint as a first candidate region, and selecting a region between the candidate breakpoint and next candidate breakpoint as a second candidate region;

subjecting the normalized number of reads falling in the primary windows Zi which are included both in the first candidate region and the second candidate region to run test (The run test is a nonparametric test, evaluating significant difference between two populations using evenly distributed status of mixed elements with two populations. Details regarding such test may refer to Wald A. W J. On a Test Whether Two Samples are from the Same Population. The Annals of Mathematical Statistics 1940; 11:147-162, which is incorporated herein by reference), to determine the p value of the candidate breakpoints.

According to embodiments of the present disclosure, the final p value is obtained by following steps:

based on a sequencing result of a control sample, repeating the step of determining a detection window in the reference genome, and recording p values of the breakpoints which are removed each time until the number of the breakpoints is zero, in which term of “control sample” used herein refers to a sample of which copy number variation does not present in a known nucleotide sequence; and

based on a distribution of the p values of removed breakpoints, the final p value is determined, for example, a distribution diagram is plotted with the p values of removed breakpoints, a p value having a maximal changing trend is taken as the final p value (pfinal).

According to specific examples of the present disclosure, the final p value is 1.1×10−50.

S400: Determining a First Parameter Based on Reads Falling in the Detection Window

After the detection windows have been determined, reads contained in the detection windows may be subjected to statistical analysis, so as to determine whether copy number variation presents in the detection windows. According to an embodiments of the present disclosure, the step of determining the first parameter based on reads falling into the detection windows further comprises: determining a mean value of the normalized number of reads falling in all primary windows  which are included in the detection windows, in which the mean value of the normalized number of reads  is taken as the first parameter. The normalized number of reads has been specifically described above, which is omitted herein for brevity.

S500: Determining Whether the Copy Number Variation Presents in the Genome Sample Against the Detection Window Based on Difference Between the First Parameter and a Preset Threshold

According to embodiments of the present disclosure, the determined first parameter may be compared with a preset threshold, then based on difference between the first parameter and the present threshold, whether the copy number variation presents in the genome sample is determined regarding the specific detection window. Based on the sequencing result of the genome sample, the number of reads falling into a certain window is positively related to content of the certain window in chromosome or genome, accordingly by subjecting reads deriving from a certain window in the sequencing result to statistical analysis, whether the copy number variation presents in the genome sample may be effectively determined based on the certain window. Term of “preset threshold” used herein refers to relative parameter based on the certain window obtained by repeating the operations and analysis in the above embodiments using a normal genome sample having a known sequence. It would be appreciated that, relative parameter based on the certain window and relative parameter of normal cells may be obtained by same sequencing conditions and mathematics methods. Here, the relative parameter of normal cells may be used as the preset threshold. Besides, term “preset” used herein should be broadly understood, which may be predetermined by experiment, or may be obtained by parallel experiments when analyzing the biological sample. Term “parallel experiment” should be broadly understood, which may refer to sequencing and analyzing unknown and known samples at the same time, or may refer to performing the steps of sequencing and analyzing under same conditions successively. According to embodiments of the present disclosure, the preset threshold comprises a first threshold and a second threshold, by comparing the first parameter  to the first threshold and the second threshold, in the case of the first parameter  smaller than the first threshold, copy number reducing is determined (i.e., deletion), in the case of the first parameter  greater than the second threshold, copy number increasing is determined (i.e., addition), accordingly which type of the copy number variation may be determined. According to specific examples of the present disclosure, α=0.05 is set as a boundary of significance, by which type of the copy number variation is further determined.

By the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, whether copy number variation in the genome sample may be effectively determined, which is suitable for various variations, including but not limited to chromosome aneuploidy, chromosome fragment deletion, fragment addition, addition, micro-deletion and micro-repeat of chromosome fragment. Copy number variation is the major factor inducing birth defect, which is also very common in embryo cultured in vitro, being a major reason leading to failure of reproduction in vitro. Copy number variation is also a pathogenic factor to many diseases such as cancer. The whole genome amplification is technique which can perform amplification in a range of whole genome with a single cell, a plurality cells or a trace of nucleic acid sample, which may increase sample amount on the premise of maintaining representativeness of the whole genome, to achieve the required sample amount. However, in general, a problem of amplification bias presents in the whole genome amplification, which brings in deviation to subsequent analysis. The method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, after the single cell or a trace of nucleic acid sample has been subjected to whole genome amplification, data is obtained by sequencing technology for analysis of copy number variation. On one hand, a problem of having difficulties in analyzing with a single cell or a trace of nucleic acid sample is solved by the whole genome amplification, on the other hand, bias to analyzing copy number variation induced by the whole genome amplification is avoided, which makes detection more accurate and more comprehensive, particularly detection efficiency may be further improved by a correlation of GC content. Besides, according to embodiments, during the sub-step of constructing sequencing-library with different samples, different indexes are introduced, by which a plurality samples may be subjected to test at the same time, which further improves efficiency of determining whether copy number variation presents in a genome sample. Using the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, screening and diagnosing copy number variation prior to embryo implantation or noninvasive screening of fetal copy number variation may be determined, which is benefit to provide genetic counseling and basis for clinic decision; prenatal diagnosis may effectively prevent implantation of embryo with lesion, to present newborns with defects.

II System for Determining Whether Copy Number Variation Presents in a Genome Sample

According to a second aspect of the present disclosure, there is provided a system for determining whether copy number variation presents in a genome sample. Using the system may effectively implement the method of determining whether copy number variation presents in a genome sample above-described, so as to effectively determine whether copy number variation presents in the genome sample.

Referring to FIG. 2, according to embodiments of the present disclosure, the system 1000 for determining whether copy number variation presents in a genome sample comprises: a sequencing apparatus 100 and an analysis apparatus 200.

According to embodiments of the present disclosure, the sequencing apparatus 100 is configured to sequence the genome sample, to obtain a sequencing result consisting of a plurality of reads. According to embodiments of the present disclosure, the system 1000 for determining whether copy number variation presents in a genome sample may further comprise a genome extracting apparatus (not shown in Figs). The genome extracting apparatus is configured to extract the genome sample from a biological sample, and the genome extracting apparatus is connected to the sequencing apparatus 100 for providing the genome sample. Accordingly, the biological sample may be directly used as raw material, to obtain information whether copy number variation presents in the biological sample, so as to reflect health status of organisms. According to embodiments of the present disclosure, the sequencing apparatus 100 may further comprise: a genome amplifying unit, a sequencing-library constructing unit and a sequencing unit, in which the genome amplifying unit is configured to amplify the genome sample; the sequencing-library constructing unit, connected to the genome amplifying unit, is configured to construct a sequencing-library with the amplified genome sample; and the sequencing unit, connected to the sequencing-library constructing unit, is configured to sequence the sequencing-library. According to embodiments of the present disclosure, the sub-step of sequencing the whole genome sequencing-library is performed by at least one selected from Next-Generation sequencing technology (such as Hiseq system of Illumina Company, Miseq system of Illumina Company, Genome Analyzer (GA) system of Illumina Company, 454 FLX of Roche Company, SOLiD system of Applied Biosystems Company, Ion Torrent system of Life Technologie Company) and single molecule sequencing apparatus. Accordingly, characteristics of high-throughput and deep sequencing of these sequencing apparatus may be used, which further improves efficiency of determining whether copy number variation presents in a genome sample.

According to embodiments of the present disclosure, the analysis apparatus 200 is connected to the sequencing apparatus 100, to determine whether copy number variation presents in a genome sample based on the sequencing result. According to embodiments of the present disclosure, the analysis apparatus 200 further comprises: an aligning unit 201, a breakpoint determining unit 202, a detection window determining unit 203, a parameter determining unit 204 and a determining unit 205, in which the aligning unit 201 is configured to align the sequencing result to a reference genome sequence, to determine a distribution of the reads in the reference genome sequence. According to embodiments of the present disclosure, a known human genome sequence is preserved in the aligning unit 201 as the reference genome sequence, optionally, the reference genome sequence is at least one selected from human chromosome 21, chromosome 18, chromosome 13, chromosome X and chromosome Y. The breakpoint determining unit 202, connected to the aligning unit 201, is configured to determine a plurality of breakpoints in the reference genome sequence, based on the distribution of the reads in the reference genome sequence, as described above, the number of reads has significance between two sides of the breakpoints. The detection window determining unit 203, connected to the breakpoint determining unit 202, is configured to determine a detection window in the reference genome based on the plurality of the breakpoints. The parameter determining unit 204, connected to the detection window determining unit, is configured to determine a first parameter based on reads falling in the detection window. The determining unit 205, connected to the parameter determining unit 204, configured to determine whether the copy number variation presents in the genome sample against the detection window based on difference between the first parameter and a preset threshold.

According to embodiments, the breakpoint determining unit 202 further comprises a module for performing following sub-steps:

dividing the reference genome sequence into a plurality of primary windows having a predetermined length, and determining reads falling into the primary windows;

Firstly, the reference genome sequence is divided into a plurality of primary windows having a predetermined length, and reads falling into the primary windows are determined. According to specific examples of the present disclosure, by conventional alignment programs, reads contained in the obtained sequencing result may be aligned to the reference genome sequence, by which reads falling into the primary windows may be determined. According to embodiments of the present disclosure, each of the primary windows may have same or different length; an overlap may present between primary windows, as long as information of each primary window is known; each of the primary windows is preferably has a same length. According to embodiments of the present disclosure, each of the primary windows may have a length of 100 to 200 Kbp, preferably 150 Kbp. According to embodiments of the present disclosure, the number of the primary windows located at both sides of the site is not subjected to special restrictions, according to a specific example of the present disclosure, 100 of the primary windows may be selected from either side of the site respectively.

Secondly, p value of the site is determined; such p value may reflect significant difference of the number of reads between two sides of the site. Besides, the p value of the site is smaller than a final p value, the site is determined as the breakpoints. According to embodiments of the present disclosure, a range of the final p value may be determined by subjecting a known sequence sample to parallel analysis, according to a specific example of the present disclosure, the final p value is 1.1×10−50.

According to embodiments of the present disclosure, the breakpoint determining unit 202 further comprises a module for performing following sub-steps:

For the selected site, the same number of the primary windows at either side of the site is selected respectively, and the relative number of reads falling in every primary window Ri is calculated, in which i represents No. of the primary windows,

the relative number of reads falling in all primary windows Ri is subjected to run test, o determine the p value of the site, in which

the relative number of reads is determined by following formula:

\(R_{i} = {\log_{2}\left( \frac{r_{i}}{\overset{\_}{r}} \right)}\)

in which ri represents the number of reads falling in the i-th primary window,

\({\overset{\_}{r} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}r_{i}}}},\)

n represents the total number of the primary windows.

According to embodiments of the present disclosure, the breakpoint determining unit 202 further comprises a module for performing followings to subject the relative number of the reads falling in all primary windows to run test:

subjecting the relative number of reads falling in each of the primary windows Ri to a correction of GC content, to obtain corrected relative number of reads {tilde over (R)}t;

determining the normalized number of reads falling in each of the primary windows Zi based on the corrected relative number of reads; and

subjecting all of the normalized number of reads falling in each of the primary windows Zi to run test.

According to embodiments of the present disclosure, the corrected relative number of reads {tilde over (R)}i is obtained by a module for performing following steps:

calculating GC content of each primary window;

dividing the GC content into a plurality of regions in a unit of 0.001, and calculating a mean value Ms of the relative number of reads falling in each of the plurality of regions, wherein s is No. of the plurality of regions;

determining the corrected relative number of reads {tilde over (R)}i based on the following formula:

{tilde over (R)}i=Ri−Ms;

determining the normalized number of reads Z, based on the following formula:

wherein

\({Z_{i} = {\left( {R_{i} - {\overset{\sim}{R}}_{i} - {mean}} \right)/{SD}}},{wherein}\)
\({{mean} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}\left( {R_{i} - {\overset{\sim}{R}}_{i}} \right)}}},{{SD} = {\sqrt{\frac{1}{n - 1}{\sum\limits_{i = 1}^{n}\left( {R_{i} - {\overset{\sim}{R}}_{i} - {mean}} \right)^{2}}}.}}\)

After the plurality of breakpoints has been determined, a possibility that copy number variation presents in a region between two successive breakpoints may be preliminary determined. Accordingly such regions may be taken as the detection windows for further determining whether copy number variation presents. In the case of obtaining relative more breakpoints in the preliminary determination, the obtained breakpoints may be subjected to further screening. According to embodiments of the present disclosure, based on the plurality of the breakpoints, the detection window determining unit further comprises a module for performing followings:

1) determining a plurality of candidate breakpoints, wherein other breakpoints present both before and after the candidate breakpoints;

2) determining p value of each candidate breakpoint, and removing a candidate breakpoint having the maximal p value;

3) performing the step 2) with rest of the candidate breakpoints until p values of the rest of the candidate breakpoints all smaller than the terminate p value, wherein the rest of the candidate breakpoints are taken as screened candidate breakpoints; and

4) determining a region between two successive screened candidate breakpoints as the detection window.

In which, according to embodiments of the present disclosure, the p value of the candidate breakpoint is obtained by following steps:

selecting a region between the candidate breakpoint and previous candidate breakpoint as a first candidate region, and selecting a region between the candidate breakpoint and next candidate breakpoint as a second candidate region;

subjecting the normalized number of reads falling in the primary windows Zi which are included both in the first candidate region and the second candidate region to run test, to determine the p value of the candidate breakpoints.

According to embodiments of the present disclosure, the final p value is obtained by following steps:

based on a sequencing result of a control sample, repeating the step of determining a detection window in the reference genome, and recording p values of the breakpoints which are removed each time until the number of the breakpoints is zero; and

determining the final p value, based on a distribution of the p values of removed breakpoints, for example, a distribution diagram is plotted with the p values of removed breakpoints, a p value having a maximal changing trend is taken as the final p value (pfinal).

According to specific examples of the present disclosure, the final p value is 1.1×10−50.

According to embodiments of the present disclosure, the parameter determining unit 204 further comprises a module for performing followings: determining a mean value of the normalized number of reads falling in all primary windows  which are included in the detection windows, in which the mean value of the normalized number of reads  is taken as the first parameter. Furthermore, a preset threshold is preserved in the determining unit 205, accordingly, the determining unit 205 may compare the first parameter determined in the parameter determining unit 204, so as to determine whether copy number variation presents in the obtained detection windows, in which according to embodiments of the present disclosure, the preset threshold comprises: a first threshold and a second threshold, by comparing the first parameter  to the first threshold and the second threshold, in the case of the first parameter  smaller than the first threshold, copy number reducing is determined (i.e., deletion), in the case of the first parameter Z greater than the second threshold, copy number increasing is determined (i.e., addition), accordingly which type of the copy number variation may be determined. According to specific examples of the present disclosure, α=0.05 is set as a boundary of significance, by which type of the copy number variation is further determined.

Accordingly, using the system for determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure may be effectively implemented, so as to effectively determine whether copy number variation presents in the genome sample, which is suitable for various copy number variations, included but not limited to aneuploidy of chromosome, deletion of chromosome, and addition, micro-deletion and micro-repetition of chromosome fragments.

It should note that, it would be appreciated by those skilled in the art that, the above-described characteristics and advantages of the method of determining whether copy number variation presents in a genome sample is also suitable to the system for whether copy number variation presents in a genome sample, which are omitted for convenience and brevity.

III. Computer Readable Medium

According to a third aspect of the present disclosure, there is provided a computer readable medium. According to embodiments of the present disclosure, an order is preserved in the computer readable medium, the order is configured to perform by a processor to determine whether copy number variation presents in a genome sample through following steps: aligning the sequencing result to a reference genome sequence, to determine a distribution of the reads in the reference genome sequence; determining a plurality of breakpoints in the reference genome sequence based on the distribution of the reads in the reference genome sequence, wherein the number of reads has significance at both sides of the breakpoints; determining a detection window in the reference genome based on the plurality of the breakpoints; determining a first parameter based on reads falling in the detection window; and determining whether the copy number variation presents in the genome sample against the detection window based on difference between the first parameter and a preset threshold. Using the computer readable medium, the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure may be effectively implemented, so as to effectively determine whether copy number variation presents in the genome sample, which is suitable for various copy number variations, included but not limited to aneuploidy of chromosome, deletion of chromosome, and addition, micro-deletion and micro-repetition of chromosome fragments.

It should note that, it would be appreciated by those skilled in the art that, the above-described characteristics and advantages of the method of determining whether copy number variation presents in a genome sample is also suitable to the computer readable medium, which are omitted for convenience and brevity.

Reference will be made in detail to examples of the present disclosure. It would be appreciated by those skilled in the art that the following examples are explanatory, and cannot be construed to limit the scope of the present disclosure. If the specific technology or conditions are not specified in the examples, a step will be performed in accordance with the techniques or conditions described in the literature in the art (for example, referring to J. Sambrook, et al. (translated by Huang PT), Molecular Cloning: A Laboratory Manual, 3rd Ed., Science Press) or in accordance with the product instructions. If the manufacturers of reagents or instruments are not specified, the reagents or instruments may be commercially available, for example, from Illumina.

General Method

Referring to FIG. 3, the method of determining whether copy number variation presents in a genome sample used in examples comprises:

Firstly, a whole genome sample is subjected to amplification, and then the amplified whole genome is sequenced to obtain reads (sequencing data);

Secondly, the obtained reads are aligned to a standard human genome reference sequence in NCBI database by SOAP2, to obtain location information of the reads in the genome. To avoid interference to analysis of copy number variation by repeat sequence, reads which are uniquely aligned to the human genome reference sequence are only selected for subsequent analysis.

Thirdly, a site of which the number of reads falling in two sides respectively having a statistical significance is found, which comprises following steps:

a) calculating the relative number of reads of the testing sample (a plurality of samples may be analyzed at the same time):

a window having a length of w is selected in the human genome reference sequence (w may be any integer greater than 1, for example 10 K to 10 M bp, 50 K to 1 M bp is preferred, 100 K to 300 K bp is more preferred, such as 150 K bp), the number of reads falling into each window ri,j is calculated in al obtained reads, in which subscript i represents No. of the windows, subscript j represents No. of the samples, GC content of each window GCi,j is also calculated, then the relative number of reads is calculated by

\({R_{i,j} = {\log_{2}\left( \frac{r_{i,j}}{{\overset{\_}{r}}_{j}} \right)}},\)

in which the average number of reads is

\({{\overset{\_}{r}}_{j} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}r_{i,j}}}},\)

b) data correlation and normalization

in a coordinate system taking GC content as X-coordinate and the relative number of reads R as Y-coordinate, GC is divided into regions having same size from small to large, a mean value Ms of R in every region is calculated, s is No. of GC region;

for every window of the sample, the corrected relative number of reads is calculated by {tilde over (R)}i,j=Ri,j−Ms, GC content of window is in the s-th GC region;

for every window of the sample, the normalized relative number of reads Zi,j is calculated by,

\({{Z_{i,j} = {\left( {R_{i,j} - {\overset{\sim}{R}}_{i,j} - {mean}_{j}} \right)/{SD}_{j}}},{{in}\mspace{14mu} {which}}}\mspace{11mu}\)
\({{mean}_{j} = {\frac{1}{n}{\sum\limits_{i = 1}^{n}\left( {R_{i,j} - {\overset{\sim}{R}}_{i,j}} \right)}}},{{SD}_{j} = \sqrt{\frac{1}{n - 1}{\sum\limits_{i = 1}^{n}\left( {R_{i,j} - {\overset{\sim}{R}}_{i,j} - {mean}_{j}} \right)^{2}}}},\)

c) determining and screening breakpoints

determining breakpoints: for each site in the reference genome sequence, n windows (for example 100 windows) are selected respectively from two sides of the site as two populations for statistical test, one p value corresponding to each site is obtained by calculating difference between two sides of the site, m sites (such as 3000 sites) having the minimum p value as breakpoint

screening breakpoints: all arranged breakpoints are recorded as Bc={b1, b2, . . . bs}, each breakpoint presents between two successive fragments, in which such two fragments are regions respective from a previous breakpoint to said breakpoint and from said breakpoint to the a next breakpoint, all Zi,j in such two fragments are subjected to statistical test (such as subjected to run test, which is a nonparametric test, evaluating significant difference between two populations using evenly distributed status of mixed elements with two population). The obtained p value (pk) is regarded as “bk is taken as significance of breakpoint”. A candidate breakpoint having the maximum p value pk is removed, which are repeated until all p value smaller than a final p value pfinal of such chromosome;

obtaining the final p value: during detection, the above step of determining a plurality breakpoint is performed with a control sample as the testing sample, all arrange candidate breakpoints in whole genome are recorded as Bc={b1, b2, . . . bs}, each candidate breakpoint bk presents between two successive fragments, all Zi,j in such two fragments are subjected to statistical test, the obtained p value (pk) is regarded as “bk is taken as significance of breakpoint”. A candidate breakpoint having the least significance p value pk is removed, which are repeated until the number of the candidate breakpoints is zero. A distribution diagram is plotted with the removed candidate breakpoint, a p value having a maximal changing trend is taken as the final p value (pfinal);

determining a detection window and verifying the detection window: after the screened breakpoints have been obtained, the detection window is determined. To further determining the detection window, a mean value of Zi,j in such fragment is calculated, which is recorded as . If  exceeds a threshold, then copy number variation is determined presenting in such fragment, in which the threshold is determined as followings:

for each fragment after connecting windows, a mean value and a standard error of the normalization number of reads Zi,j in such fragment of all control samples are calculated. As  in each fragment fits normal distribution, a range of threshold of such fragment when a cumulative probability is 0.05 is calculated according to the calculated mean value and standard error obtained in above steps, in which the range of threshold is used as the threshold filtering whether copy number variation presents in the fragment.

Example 1 Copy Number Variation Detection of Fetal Fragments with an Embryo Single Cell Sample, and Chromosome Aneuploid Detection with an Embryo Single Cell Sample

1. whole genome amplification: GenomePlex® Single Cell Whole Genome Amplification Kit from Sigma Aldrich Company was used in whole genome amplification with the two embryo single cell samples in the current example. The embryo single cell sample was trophoblast cell of the fifth day blastocysts, which was isolated from blastaea by a laser capture microdissection method. After the two embryo single cell samples were lysed, the whole genome amplification was performed in accordance with instructions for kit provided by manufacturer.

2. sequencing: in the current example, Hiseq2000 sequencing platform from Illumina Company was used in sequencing the amplified whole genome DNA from the two embryo single cell sample. According to instructions provided by Illumina Company, sequencing-library construction and sequencing on computer were performed, by which generated about 0.36 G data volume of each sample, distinguished by different index sequences. Using alignment software SOAP2, the reads obtained by sequencing were aligned to human genome reference sequencing in NCBI database, Build 36, to locate the obtained reads in the human genome reference sequence.

3. Data analysis

a) calculating the relative number of reads of a testing sample and a control sample (the control sample referred to a sample had normal karyotype)

The human genome reference sequence was divided into a plurality of windows having a length of 150K bp. The number of the reads obtained in step 2) falling in each window ri,j was calculated, in which the subscript i represented No. of the plurality of windows, j represented No. of samples. GC content was also calculated for each window. The relative number of reads was calculated in accordance with the formula given in General Method.

b) data correction and normalization

in a coordinate system taking GC content as X-coordinate and the relative number of reads R as Y-coordinate, GC content was divided into a plurality of regions in a unit of 0.001, from small to large. A mean value Ms of R in every region was calculated, s was No. of GC region, which were shown in Table.1. The obtained reads were subjected to correction and normalization in accordance to the formula given in General Method.

c) Connecting windows

determining breakpoint, for each site in the reference genome sequence, 100 windows located at either side of the site were selected respectively from two sides of the site as two populations for run test, one p value corresponding to each site was obtained by calculating difference between two sides of the site, 3000 sites having the minimum p value as breakpoint.

screening breakpoint: all arranged breakpoints were recorded as Bc={b1, b2, . . . , bs}, each breakpoint presented between two successive fragments, in which such two fragments were regions respective from a previous breakpoint to said breakpoint and from said breakpoint to the a next breakpoint, all Zi,j in such two fragments were subjected to run test. The obtained p value (pk) was regarded as “bk was taken as significance of breakpoint”. A candidate breakpoint having the maximum p value pk was removed, which were repeated until all p value smaller than the final p value pfinal of such chromosome being as 1.1×10−50.

d) after the breakpoints were screened out, a region between two successive breakpoints was determined as a detection window, so as to connect windows. To further filter fragments obtained by connecting windows, a mean value of Zi,j in such fragment was calculated, which was recorded as . If  exceeded a threshold, then copy number variation was determined presenting in such fragment. −1.645 was used as the first threshold, and 1.645 was used as the second threshold.

4. Result

Table.2 showed a detection result list of copy number variation after whole genome amplifying the embryo single cell sample in current example.

It could be seen from Table.2 that using the method of determining whether copy number variation presents in a genome sample according to embodiments of the present disclosure, various types of copy number variation could be effectively determined.

### Example 2

Using the embryo single cell sample same as that in Example 1, all steps were rereated as Example 1 except the genome DNA was directly subjected to sequencing (without firstly subjected to whole genome amplification). Comparison result between Example 1 and Example 2 was shown in Table 3, FIG. 4 and FIG. 5.

It could be seen from data in Table.3 and images of chromosome karyotype in FIG. 4 and FIG. 5 that the detection results of reads copy number variation between the genome DNA sample which was subjected to whole genome amplification and the genome DNA sample which was not subjected to whole genome amplification were consistent. For difference of staring and terminating points of “deletion” or “repeat” in Table.3, as the boundary of copy number variation was hard to be accurately determined, in general for the primary window having a length of about 150K, two boundaries having difference within a range of 100 to 300 Kb could be determined as being fully consistent, two boundaries having difference within a range of 300 Kb to 1 Mb could be determined as being quite consistent. Since the difference between boundaries of copy number variation determined by the two methods in Table 3. was within the range of 100 to 300 Kb or within the range of 300 Kb to 1 Mb, it could determine that the boundaries of copy number variation determined by the two methods were consistent.

## INDUSTRIAL APPLICABILITY

The method, system and computer readable medium of determining whether copy number variation presents in a genome sample of the present disclosure may be effectively used to determine whether copy number variation presents in a genome sample.

Reference throughout this specification to “an embodiment,” “some embodiments,” “one embodiment”, “another example,” “an example,” “a specific examples,” or “some examples,” means that a particular feature, structure, material, or characteristic described in connection with the embodiment or example is included in at least one embodiment or example of the present disclosure. Thus, the appearances of the phrases such as “in some embodiments,” “in one embodiment”, “in an embodiment”, “in another example, “in an example,” “in a specific examples,” or “in some examples,” in various places throughout this specification are not necessarily referring to the same embodiment or example of the present disclosure. Furthermore, the particular features, structures, materials, or characteristics may be combined in any suitable manner in one or more embodiments or examples.

Although explanatory embodiments have been shown and described, it would be appreciated by those skilled in the art that the above embodiments cannot be construed to limit the present disclosure, and changes, alternatives, and modifications can be made in the embodiments without departing from spirit, principles and scope of the present disclosure.

