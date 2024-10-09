# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates to a method for generating extended sequence reads and in particular, but not exclusively, to a method for generating extended sequence reads of large genomes.

## BACKGROUND

The current maximum read length of next-generation sequencing technologies, such as those developed by Illumina® and Life Technologies™, is around 250 bases. The read length is one of the main factors that determine the quality of a genome assembly. In general, longer reads make better assemblies because they span more repeats.

Furthermore, increasing the read length of next-generation sequencing technologies enables broader applications such as being able to sequence larger genomes, generate extended sequence reads and be useful for long-range haplotype analysis on targeted genomic regions.

Therefore, there is a need for an approach to increase the read length of these commercially available sequencing platforms to several kilobases.

## SUMMARY OF THE INVENTION

In accordance with a first aspect of the present invention, there is provided a method for generating extended sequence reads of long DNA molecules in a sample, comprising the steps of:


- - (i) assigning a specific barcode sequence to each template DNA
    molecule in a sample to obtain barcode-tagged molecules;
  - (ii) amplifying the barcode-tagged molecules;
  - (iii) fragmenting the amplified barcode-tagged molecules to obtain
    barcode-containing fragments;
  - (iv) juxtaposing the barcode-containing fragments to random short
    segments of the original DNA template molecule during the process of
    generating a sequencing library to obtain demultiplexed reads; and
  - (v) assembling the demultiplexed reads to obtain extended sequence
    reads for each DNA template molecule.

Preferably, the method further comprises the step of labelling the amplified barcode-tagged molecules with biotin.

Preferably, wherein the step of fragmenting the amplified barcode-tagged molecules comprises the step of subjecting the amplified barcode-tagged molecules to unidirectional deletion from the barcode-distal end of the barcode-tagged molecules to obtain barcode-containing fragments.

Preferably, wherein the step of fragmenting the amplified barcode-tagged molecules comprises the steps of:


- - (i) creating a nick at the barcode-distal end of the amplified
    barcode-tagged molecules;
  - (ii) performing a nick translation towards the barcode-proximal end;
    and
  - (iii) treating with endonuclease the resulting molecules to generate
    blunt ends, to obtain barcode-containing fragments.

Preferably, wherein the step of fragmenting the amplified barcode-tagged molecules comprises the step of performing random fragmentation by a mechanical method or an enzymatic method to obtain barcode-containing fragments.

Preferably, the barcode-containing fragments have lengths ranging from about 300 base pairs to N base pairs, wherein N equals to the length of the original DNA template molecule.

Preferably, the method further comprises the step of purifying the barcode-containing fragments using streptavidin-coated paramagnetic beads.

Preferably, wherein the step of purifying the barcode-containing fragments comprises dissociating the biotin-labelled molecules from the streptavidin-coated paramagnetic beads.

Preferably, wherein the step of purifying the barcode-containing fragments comprises dissociating the biotin-labelled molecules from the streptavidin-coated paramagnetic beads, further comprises the step of circularizing the purified barcode-containing fragments by intramolecular ligation.

Preferably, the method further comprises the step of ligating sequencing adaptors onto the ends of the barcode-containing fragments prior to the step of juxtaposing the barcode-containing fragments to random short segments of the original DNA template molecule.

Preferably, the specific barcode sequence is assigned by linker ligation to each template DNA molecule.

Preferably, wherein the step of amplifying the barcode-tagged molecules is by circularizing the barcode-tagged molecules and performing rolling circle amplification.

Preferably, the extended sequences reads are compatible for sequencing on sequencing platforms.

In accordance with a second aspect of the present invention, there is provided a system for obtaining extended sequence reads from template molecules of a DNA sequence, comprising:


- - (i) a quality filtering module for filtering raw paired-end sequence
    reads from a sequencer by removing read-pairs with low quality
    scores, removing read-pairs with missing barcode sequences and
    trimming platform-specific adaptor sequences;
  - (ii) a barcode analysis module for identifying highly-represented
    barcodes and re-assigning sequences associated with
    poorly-represented barcodes;
  - (iii) a demultiplexing module for using barcode sequences as
    identifiers to obtain reads associated with individual template
    molecules and removing duplicate read-pairs; and
  - (iv) an assembly module for assembling demultiplexed reads to obtain
    extended sequence reads for each template molecule.

The system in accordance to the second aspect of the present invention wherein the DNA sequence is a known sequence, further comprising:

(i) a sequence alignment module for performing paired-end alignment to a reference sequence and removing disconcordant alignments;


- - (ii) a demultiplexing module for using barcode sequences as
    identifiers to obtain alignments to individual template molecules
    and removing duplicate read-pairs in place of the demultiplexing
    module according to the second aspect of the present invention; and
  - (iii) a haplotyping module for obtaining pileup of aligned reads at
    each position along the reference sequence, determining consensus
    base-call at each position and assembling base-calls to obtain
    extended sequence reads for each template molecule in place of the
    assembly module according to the second aspect of the present
    invention.

In accordance with a third aspect of the present invention, there is provided a computer-readable medium with an executable programme stored thereon, the programme comprising instructions for obtaining extended sequence reads from template molecules of a DNA sequence, wherein the programme instructs a microprocessor to perform the following steps:


- - (i) filtering raw paired-end sequence reads from a sequencer by
    removing read-pairs with low quality scores, removing read-pairs
    with missing barcode sequences and trimming platform-specific
    adaptor sequences;
  - (ii) identifying highly-represented barcodes and re-assigning
    sequences associated with poorly-represented barcodes;
  - (iii) using barcode sequences as identifiers to obtain reads
    associated with individual template molecules and removing duplicate
    read-pairs; and
  - (iv) assembling demultiplexed reads to obtain extended sequence
    reads for each template molecule.

The computer-readable medium in accordance to the third aspect of the present invention wherein the DNA sequence is a known sequence, wherein the programme instructs the microprocessor to further perform the following steps:


- - (i) performing paired-end alignment to a reference sequence and
    removing disconcordant alignments at the step of identifying
    highly-represented barcodes and re-assigning sequences associated
    with poorly-represented barcodes;
  - (ii) replacing the step of using barcode sequences as identifiers to
    obtain reads associated with individual template molecules and
    removing duplicate read-pairs with the step of using barcode
    sequences as identifiers to obtain alignments to individual template
    molecules and removing duplicate read-pairs; and
  - (iii) replacing the step of assembling demultiplexed reads with the
    step of obtaining pileup of aligned reads at each position along the
    reference sequence, determining consensus base-call at each position
    and assembling base-calls to obtain extended sequence reads for each
    template molecule.

The present invention provides an approach that can: 1) increase the effective read length of these commercially available sequencing platforms to several kilobases and 2) be broadly applied to obtain long sequence reads from mixed template populations.

The present invention applies the concept of barcoding to generate long sequence reads by providing a technical advance in juxtaposing the assigned barcode to random overlapping segments of the original template.

The present invention relies on assigning barcodes to individual template molecules, allowing for unambiguous assembly of template sequences even for molecules with high sequence similarity. This also means that the present invention will work for sequencing targeted genomic regions or viral genomes.

Accordingly, aspect(s) of the present invention also includes: —

a) A method to assign unique DNA barcodes, i.e., a random string of DNA nucleotides, to individual long (>3 kilo bases (kb)) template molecules.

b) A method to juxtapose the assigned DNA barcode to random short segments of the original template molecule during the process of generating a sequencing library.

c) A method of using the DNA barcode associated with each molecule of a sequencing library to identify the template of origin.

d) A method of using DNA barcodes to substantially reduce the error rate of massively parallel sequencing.

e) A method for barcode-directed assembly of short sequence reads to obtain individual template sequences.

Other aspects and advantages of the present invention will become apparent to those skilled in the art from a review of the ensuing description, which proceeds with reference to the following illustrative drawings of preferred embodiments.

## DETAILED DESCRIPTION

The present invention applies the concept of barcoding to generate long sequence reads by providing a technical advance in juxtaposing the assigned barcode to random overlapping segments of the original template.

The present invention relies on assigning barcodes to individual template molecules, allowing for unambiguous assembly of template sequences even for molecules with high sequence similarity. This also means that the present invention will work for sequencing targeted genomic regions or viral genomes.

The current maximum read length of next-generation sequencing technologies, such as those developed by Illumina® and Life Technologies™, is around 250 bases. The present invention, also known as “Barcode-directed Assembly for Extra-long Sequences (BAsE-Seq)” provides an approach that can: 1) increase the effective read length of these commercially available sequencing platforms to several kilobases and 2) be broadly applied to obtain long sequence reads from mixed template populations. In brief, our method relies on assigning random DNA barcodes to long template molecules (FIG. 1A), followed by a library preparation protocol that juxtaposes the assigned barcode to random short segments of the original template (FIGS. 1B and 2). The resulting molecules are ligated with platform-specific adaptors for next-generation sequencing. Sequence reads are de-multiplexed using the barcode sequence and used to assemble long-range haplotypes that were present on the original template. In practice, we have applied this technology to perform single virion sequencing on the Hepatitis B virus, a DNA virus with a 3.2 kb genome. In general, we anticipate that this technology can be broadly applied to generate extended sequence reads and will be useful for long-range haplotype analysis on targeted genomic regions, or for improving de novo genome and transcriptome assemblies. A detailed description of our protocol is described in the following paragraphs.

There is described a method for generating extended sequence reads of long DNA molecules (>3 kb), in a sample. The method comprises the steps of: (i) assigning a specific barcode sequence to each template DNA molecule in a sample to obtain barcode-tagged molecules; (ii) amplifying the barcode-tagged molecules; (iii) fragmenting the amplified barcode-tagged molecules to obtain barcode-containing fragments; (iv) juxtaposing the barcode-containing fragments to random short segments of the original DNA template molecule during the process of generating a sequencing library to obtain demultiplexed reads; and (v) assembling the demultiplexed reads to obtain extended sequence reads for each DNA template molecule.

a) Barcode Assignment.

In the first step, individual template molecules are assigned with a unique DNA barcode. In our example, two rounds of PCR amplification are performed using primers with template-specific sequence from opposite ends of the molecule (FIG. 1A). This will generate uniquely tagged template molecules for preparing libraries and can be broadly applied for assigning barcodes to targeted genomic regions. Both primers contain a universal sequence on their 5′-ends and one of them contains a barcode, i.e., a string of 20 random nucleotides (encodes for >1012 sequences). To ensure that each template molecule is uniquely assigned, the template should be diluted to obtain a relatively small number of genomes (<109) compared to unique barcode sequences.

Subsequently, barcode-tagged molecules can be clonally amplified by PCR using universal primers and the PCR product can be used to prepare sequencing libraries. In other manifestations where the template sequence is unknown, the barcode can be assigned by ligation of double- or single-stranded DNA linkers carrying a random string of nucleotides flanked by universal sequences.

The use of unique barcodes to tag individual template molecules has been shown to greatly reduce the error rate of massively parallel sequencing. Using this strategy, mutations that pre-existed on the template and errors introduced during barcode assignment will be found in all daughter molecules.

In contrast, errors introduced in subsequent steps of library preparation, sequencing, or base-calling can be easily removed because they will only be present in a minority of daughter molecules (FIG. 1A). Based on the published error rate of the DNA polymerase used in our protocol, this translates to one error in every 50 template sequences for template molecules that are 3 kb in size. Furthermore, by using barcodes as unique identifiers for individual genomes, sequences associated with each barcode can be assembled into a complete template sequence.

b) Library Preparation.

The goal of library preparation is to tag overlapping fragments of each template molecule with its assigned barcode in order to obtain uniform sequence coverage. This concept is illustrated in FIG. 1B and a detailed outline of the protocol is shown in FIG. 2.

Firstly, clonally amplified barcode-tagged molecules are deleted from the barcode-distal end to achieve a broad size distribution of fragments ranging from ˜300 bp to N bp, where N equals the length of the template molecule. Unidirectional deletion can be achieved by protecting the barcode-proximal end with nuclease-resistant nucleotides or a 3′-protruding overhang, and performing time-dependent digestion from the barcode-distal end using a 3′ to 5′ exonuclease (such as Exonuclease III), followed by treatment with an endonuclease (such as S1 Nuclease or Mung Bean Nuclease) to generate blunt-ends.

Barcode-containing fragments are purified using streptavidin-coated beads, and these biotinylated fragments will be dissociated and subjected to end repair, such that both ends of the molecules are blunt and 5′-phosphorylated. The end-repaired molecules are circularized by intramolecular ligation using a DNA ligase (such as T4 DNA ligase). Uncircularized molecules will be removed by nuclease treatment (such as a combination of Exonuclease I and Lambda Exonuclease).

After circularization, different regions from the original template will be juxtaposed to its barcode. The circularized molecules will be used as template for random fragmentation and adaptor tagging using a transposome-based method, such as the Nextera XT kit (Illumina®).

Importantly, the primers used during PCR enrichment of the sequencing library will be designed such that the second sequencing read will be anchored by the barcode sequence. Thus, this PCR generates double-stranded DNA molecules that are “sequencing-ready”. Finally, the PCR products are subjected to size selection before sequencing. A custom sequencing primer that anneals to the forward priming sequence is used for the second sequencing read.

There are several alternative approaches to generate a broad distribution of barcode-tagged molecules before circularization. One approach involves creating a nick at the barcode-distal end using a nicking endonuclease, nick translation towards the barcode-proximal end using DNA polymerase I, followed by treatment with endonuclease to generate a blunt end. Another approach involves performing random fragmentation using a mechanical method, such as using the Covaris instrument for focused-ultrasonication, or an enzymatic method, such as using the NEBNext dsDNA Fragmentase, followed by purification of barcode-containing fragments using streptavidin-coated paramagnetic beads.

An alternative, PCR-free approach to clonal amplification is contemplated, such as circularizing the barcoded template and performing rolling circle amplification using phi29 polymerase.

Barcodes can be assigned by linker ligation. Both linkers will contain universal sequences on their 5′-end to facilitate clonal amplification in the next step. The barcode-containing linker will also contain a unique universal sequence on its 3′-end for primer annealing during the PCR step at the end of the protocol.

Software packages for obtaining extended or extra-long sequence reads by reference-assisted assembly and for obtaining extended or extra-long sequence reads from template molecules of an unknown sequence are illustrated in FIGS. 3 and 4, respectively.

There is described hereinafter a system for obtaining extended sequence reads from template molecules of a DNA sequence. The system comprises (i) a quality filtering module for filtering raw paired-end sequence reads from a sequencer by removing read-pairs with low quality scores, removing read-pairs with missing barcode sequences and trimming platform-specific adaptor sequences; (ii) a barcode analysis module for identifying highly-represented barcodes and re-assigning sequences associated with poorly-represented barcodes; (iii) a demultiplexing module for using barcode sequences as identifiers to obtain reads associated with individual template molecules and removing duplicate read-pairs; and (iv) an assembly module for assembling demultiplexed reads to obtain extended sequence reads for each template molecule (FIG. 4). The template molecules are long, preferably >3 kb.

Where the DNA sequence is a known sequence, the system further comprises (i) a sequence alignment module for performing paired-end alignment to a reference sequence and removing disconcordant alignments; (ii) a demultiplexing module for using barcode sequences as identifiers to obtain alignments to individual template molecules and removing duplicate read-pairs in place of the demultiplexing module shown in FIG. 4; and (iii) a haplotyping module for obtaining pileup of aligned reads at each position along the reference sequence, determining consensus base-call at each position and assembling base-calls to obtain extended sequence reads for each template molecule in place of the assembly module shown in FIG. 4 (FIG. 3).

There is also disclosed a computer-readable medium with an executable programme stored thereon, the programme comprising instructions for obtaining extended sequence reads from template molecules of a DNA sequence, wherein the programme instructs a microprocessor to perform the following steps of (i) filtering raw paired-end sequence reads from a sequencer by removing read-pairs with low quality scores, removing read-pairs with missing barcode sequences and trimming platform-specific adaptor sequences; (ii) identifying highly-represented barcodes and re-assigning sequences associated with poorly-represented barcodes; (iii) using barcode sequences as identifiers to obtain reads associated with individual template molecules and removing duplicate read-pairs; and (iv) assembling demultiplexed reads to obtain extended sequence reads for each template molecule.

Where the DNA sequence is a known sequence, the programme instructs the microprocessor to further perform the following steps of (i) performing paired-end alignment to a reference sequence and removing disconcordant alignments at the step of identifying highly-represented barcodes and re-assigning sequences associated with poorly-represented barcodes; (ii) replacing the step of using barcode sequences as identifiers to obtain reads associated with individual template molecules and removing duplicate read-pairs described above with the step of using barcode sequences as identifiers to obtain alignments to individual template molecules and removing duplicate read-pairs; and (iii) replacing the step of assembling demultiplexed reads described above with the step of obtaining pileup of aligned reads at each position along the reference sequence, determining consensus base-call at each position and assembling base-calls to obtain extended sequence reads for each template molecule.

### Examples

Hepatitis B virus (HBV), which contains a 3.2 kb dsDNA genome, was used as a template for methodology development and generating proof-of-concept data. The results presented below demonstrate the use of BAsE-Seq to obtain long (˜3.2 kb) sequence reads from individual template molecules, thereby achieving single virion sequencing of HBV.

HBV DNA was isolated from a chronically infected patient, PCR-amplified to obtain full-length viral genomes, and cloned into a TOPO pCR2.1 vector (Life Technologies™). Sanger sequencing was performed across each clone to obtain full-length sequences, and two clones (Clone-1 and Clone-2) with 17 single nucleotide polymorphisms (SNPs) between them were used as input for barcode assignment. In the results presented hereafter, barcode-tagged whole-genome amplicons from 20,000 template molecules (HBV genomes) were used as input for library preparation using the BAsE-Seq protocol described above.

Summary statistics from a typical single virion sequencing experiment of HBV are shown in Table 1, and coverage data per template molecule are illustrated in FIGS. 5 and 6. In this library, 18,143,186 read-pairs were obtained from the MiSeq sequencer (Illumina®), from which Ser. No. 12/004,237 read-pairs contained the barcode in the expected orientation. After trimming for adaptor, barcode tag and universal sequences, and removing reads shorter than 15 bp, 7,336,915 pass-filter read-pairs were used for alignment to a HBV reference genome. From these read-pairs, 97% read-pairs aligned concordantly, and were distributed across 4,294 individual template molecules, 2,717 of which were identified as “high coverage” and were used for constructing long reads.

To test the sensitivity and accuracy of our methodology in generating long sequence reads, Clone-1 and Clone-2 were mixed at different ratios to generate a mixed template population where Clone-1 is present at approximately 1% or 10% frequency in the sample. BAsE-Seq was performed on each mixed-template pool. Firstly, barcodes were removed from each read-pair prior to alignment and the resulting data was treated as a “bulk” sequencing experiment to determine overall allele frequencies at the SNP positions. The minor allele frequencies in both libraries were very close to the mixing ratio—0.98% for the “1% pool” (Lib—1:99) and 13.44% for the “10% pool” (Lib—1:9)—indicating that the mixed template pool was generated correctly and PCR bias was negligible (Table 2 and FIG. 7). Subsequently, the “bulk” sequence data was de-multiplexed using barcode sequences and sequence reads from individual template molecules were analyzed to obtain ˜3.2 kb reads. Using the long sequence reads, 17-SNP haplotypes were generated for each template molecule. In Lib—1:9, 240 molecules carried a Clone-1 haplotype and 1,639 molecules carried a Clone-2 haplotype, corresponding to a 12.77% minor haplotype frequency. In Lib—1:99, 20 molecules carried a Clone-1 haplotype and 1,912 molecules carried a Clone-2 haplotype, corresponding to a 1.04% minor haplotype frequency. Importantly, chimeric sequences where Clone-1 and Clone-2 SNPs were found on the same molecule were present at ≦0.1% frequency. Furthermore, the use of barcodes to correct for sequencing errors resulted in a very low error rate for BAsE-Seq, allowing for significant separation of true sequence variants from background noise in Lib—1:99 (Table 2 and FIG. 8).

Those skilled in the art will appreciate that the invention described herein is susceptible to variations and modifications other than those specifically described. The invention includes all such variation and modifications. The invention also includes all of the steps, features, formulations and compounds referred to or indicated in the specification, individually or collectively and any and all combinations or any two or more of the steps or features.

Each document, reference, patent application or patent cited in this text, if any, is expressly incorporated herein in their entirety by reference, which means that it should be read and considered by the reader as part of this text. That the document, reference, patent application or patent cited in this text is not repeated in this text is merely for reasons of conciseness.

Any manufacturer's instructions, descriptions, product specifications, and product sheets for any products mentioned herein or in any document incorporated by reference herein, are hereby incorporated herein by reference, and may be employed in the practice of the invention.

The present invention is not to be limited in scope by any of the specific embodiments described herein. These embodiments are intended for the purpose of exemplification only. Functionally equivalent products, formulations and methods are clearly within the scope of the invention as described herein.

The invention described herein may include one or more range of values (e.g. size, concentration etc). A range of values will be understood to include all values within the range, including the values defining the range, and values adjacent to the range which lead to the same or substantially the same outcome as the values immediately adjacent to that value which defines the boundary to the range.

Throughout this specification, unless the context requires otherwise, the word “comprise” or variations such as “comprises” or “comprising”, will be understood to imply the inclusion of a stated integer or group of integers but not the exclusion of any other integer or group of integers. It is also noted that in this disclosure and particularly in the claims and/or paragraphs, terms such as “comprises”, “comprised”, “comprising” and the like can have the meaning attributed to it in U.S. patent law; e.g., they can mean “includes”, “included”, “including”, and the like; and that terms such as “consisting essentially of” and “consists essentially of” have the meaning ascribed to them in U.S. patent law, e.g., they allow for elements not explicitly recited, but exclude elements that are found in the prior art or that affect a basic or novel characteristic of the invention.

Other definitions for selected terms used herein may be found within the detailed description of the invention and apply throughout. Unless otherwise defined, all other scientific and technical terms used herein have the same meaning as commonly understood to one of ordinary skill in the art to which the invention belongs.

While the invention has been described with reference to specific methods and embodiments, it will be appreciated that various modifications and changes may be made without departing from the invention.

