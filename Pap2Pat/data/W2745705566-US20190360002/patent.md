# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates to the field of genetic engineering and more particularly to nucleic acid editing and genome modification. The present invention concerns genetic engineering tools in the form of nucleases which can be configured for sequence-directed site-specific binding, nicking, cutting and modification of genetic material; also, ribonucleoproteins which exert activity, particularly nuclease activity, on sequence specific sites of genetic material, and modified nucleases and ribonucleoproteins for use as markers. The invention therefore also concerns associated expression constructs for delivery and expression of nucleases and guide RNAs within non-human cells. Further, the invention concerns the sequence-specific editing of nucleic acids in vitro or in vivo and methods used to achieve that. A particular area to which the invention relates is the genetic manipulation of thermophilic organisms, particularly microorganisms.

## BACKGROUND TO THE INVENTION

It was first demonstrated in 2007 that CRISPR-Cas is an adaptive immune system in many bacteria and most archaea (Barrangou et al., 2007, Science 315: 1709-1712), Brouns et al., 2008, Science 321: 960-964). Based on functional and structural criteria, two classes of CRISPR-Cas systems that each comprise three types have so far been characterized, most of which use small RNA molecules as guide to target complementary DNA sequences (Makarova et al., 2015, Nat Rev Microbiol 13: 722-736; Mahanraju et al., 2016, Science 353: aad5147).

In a recent study by the Doudna/Charpentier labs, a thorough characterization of the effector enzyme of the class 2/type II CRISPR-Cas system (Cas9) was performed, including demonstration that the introduction of designed CRISPR RNA guides (with specific spacer sequences) targets complementary sequences (protospacers) on a plasmid, causing double strand breaks of this plasmid (Jinek et al., 2012, Science 337: 816-821). Following Jinek et al., 2012, Cas9 is used as a tool for genome editing.

Cas9 has been used to engineer the genomes of a range of eukaryotic cells (e.g. fish, plant, man) (Charpentier and Doudna, 2013, Nature 495: 50-51).

In addition, Cas9 has been used to improve yields of homologous recombination in bacteria by selecting for dedicated recombination events (Jiang et al., 2013, Nature Biotechnol 31: 233-239). To achieve this, a toxic fragment (Targeting construct) is co-transfected with a rescuing fragment carrying the desired alteration (Editing construct, carrying point mutation or deletions). The Targeting construct consists of Cas9 in combination with a design CRISPR and an antibiotic resistance marker, defining the site of the desired recombination on the host chromosome; in the presence of the corresponding antibiotic, integration of the Targeting construct in the host chromosome is selected for. Only when the additional recombination occurs of the Editing construct with the CRISPR target site on the host chromosome, the host can escape from the auto-immunity problem. Hence, in the presence of the antibiotic, only the desired (marker-free) mutants are able to survive and grow. A related strategy to select for subsequent removal of the integrated Targeting construct from the chromosome is presented as well, generating a genuine marker free mutant.

It has been established in recent years that CRISPR-Cas mediated genome editing constitutes a useful tool for genetic engineering. It has been established that the prokaryotic CRISPR systems serve their hosts as adaptive immune systems (Jinek et al., 2012, Science 337: 816-821) and can be used for quick and effective genetic engineering (Mali et al., 2013, Nat Methods 10:957-963, for example), requiring only modification of the guide sequence in order to target sequences of interest.

However, there is a continuing need for the development of agents with improved sequence-specific nucleic acid detection, cleavage and manipulation under a variety of experimental conditions for application in the area of genetic research and genome editing. In particular, currently available sequence-specific genome editing tools, including Cas9, are not applicable for use in all conditions or organisms, for example, sequence-specific nucleases are relatively thermo-sensitive and therefore not applicable for use in strictly thermophilic microorganisms (which are capable of growth between 41° C. and 122° C. and grow optimally in the ranges of temperatures from >45° C. to 80° C. with hyperthermophiles capable of optimal growth above 80° C.), for example, microorganisms that are used in industrial fermentations or for in vitro laboratory processes conducted at elevated temperatures.

To date there is no experimental evidence for active Cas9 proteins in thermophiles. Based on a comparative genome screening by Chylinski et al. (2014; Nucleic Acids Research 42: 6091-61-05) on the presence of Cas9 in bacteria it was found that the Type II-C CRISPR-Cas system is only present in approximately 3.3% of all bacterial genomes. Among thermophilic bacteria, the Type II system is underrepresented based on statistical analysis (P=0.0019). In addition, no Type II system has been found in archaea however, this could possibly be due to the absence of the RNase III protein (involved in the Type II system) in archaea. Chylinski, et al., (2014; Nucleic Acids Research 42: 6091-6105) did describe the classification and evolution of type II CRISPR-Cas systems, in particular, two species are identified which exhibit these systems, however these species grow maximally at 55° C. and do not exhibit strictly thermophilic growth with optimum growth temperature 60-80° C., with hyperthermophiles capable of growing optimally above 80° C.

Despite the rarity of the CRISPR-Cas system in bacterial genomes and in particular the fact that Cas9 has been found only in bacteria (not archaea) with optimal growth temperatures below 45° C., the inventors have surprisingly discovered several thermostable Cas9 variants which enable genome editing to be carried out at elevated temperatures. The inventors have also discovered optimised protospacer adjacent motif (PAM) sequences that work with the thermostable Cas9 variants to enable genome editing to be carried out over a wide range of temperatures, including at the elevated temperatures. These Cas9 nucleases, and RNA molecules that are designed with knowledge of the associated PAM sequences, provide novel tools for genetic engineering at elevated temperatures and are of particular value in the genetic manipulation of thermophilic organisms; particularly microorganisms.

A phylogenetic re-assessment of the thermophilic genus Geobacillus has recently been performed, which resulted in the creation of a new genus, Parageobacillus. Consequently, some species previously of the genus Geobacillus have been systematically re-assigned to Parageobacillus and re-named accordingly (Aliyu et al., (2016) Systematic and Applied Microbiology 39:527-533).

Clustered Regularly Interspaced Short Palindromic Repeats (CRISPR) and the CRISPR-associated (Cas) proteins provide adaptive and heritable immunity in prokaryotes against invading genetic elements (Brouns et al. Science 321, (2008); Barrangou et al. CRISPR provides acquired resistance against viruses in prokaryotes. Science 315, (2007); Wright et al. Cell 164, 29-44 (2016); Mohanraju et al. Science 353, aad5147 (2016)). CRISPR-Cas systems are subdivided into two classes (1 and 2) and six types (I-VI), depending on their complexity and signature protein (Makarova et al. Nat. Rev. Microbiol. 13, 722-736 (2015)). Class 2 systems, including type-II CRISPR-Cas9 and type V CRISPR-Cas12a (previously called CRISPR-Cpf1) have recently been exploited as genome engineering tools for both eukaryotes (Komor et al. Cell 168, 20-36 (2017); Puchta, Curr. Opin. Plant Biol. 36, 1-8 (2017); Xu et al. J. Genet. Genomics 42, 141-149 (2015); Tang et al. Nat. Plants 3, 17018 (2017); Zetsche et al. Nat. Biotechnol. 35, 31-34 (2016)) and prokaryotes (Mougiakos, et al. Trends Biotechnol. 34, 575-587 (2016)). These systems are among the simplest CRISPR-Cas systems known as they introduce targeted double stranded DNA breaks (DSBs) based on a ribonucleoprotein (RNP) complex formed by a single Cas endonuclease and an RNA guide.

To date, Streptococcus pyogenes Cas9 (SpCas9) is the best characterized and most widely employed Cas9 for genome engineering. Although a few other type-II systems have been characterized, none of them is derived from a thermophilic organism (Nakade, et al. Bioengineered 1-9 (2017). doi:10.1080/21655979.2017.1282018). Characterization of such CRISPR-Cas systems would be interesting to gain fundamental insights as well as to develop novel applications.

Although basic genetic tools are available for a number of thermophiles (Taylor et al. Microb. Biotechnol. 4, 438-448 (2011); Olson, et al. Curr. Opin. Biotechnol. 33, 130-141 (2015); Zeldes, et al. Front. Microbiol. 6, 1209 (2015)), the efficiency of these tools is still too low to enable full exploration and exploitation of this interesting group of organisms. Based on our finding that SpCas9 is not active in vivo ≥42° C., we have previously developed an SpCas9-based engineering tool for facultative thermophiles, combining homologous recombination at elevated temperatures and SpCas9-based counter-selection at moderate temperatures (Mougiakos et al. ACS Synth. Biol. 6, 849-861 (2017)). However, a Cas9-based editing and silencing tool for obligate thermophiles is not yet available as SpCas9 is not active at or above 42° C. (Mougiakos et al. ACS Synth. Biol. 6, 849-861 (2017)) and to date no thermophilic Cas9 has been characterized.

## SUMMARY OF THE INVENTION

The inventors have discovered and characterised ThermoCas9: an RNA-guided DNA-endonuclease from the CRISPR-Cas type-IIC system of the thermophilic bacterium Geobacillus thermodenitrificans T12. The inventors have surprisingly shown its in vitro activity over a broad temperature range, demonstrated the importance of the sgRNA-structure for thermostability and applied ThermoCas9 for in vivo genome editing across a wide temperature range.

Accordingly, the present invention provides a method of modifying the genetic material of a eukaryotic cell, comprising (i) integrating a polynucleotide encoding a ThermoCas9 under the control of a first promoter into the genome of the cell, wherein the expressed ThermoCas9 comprises an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith, or an active fragment thereof; (ii) transforming the cell with an expression vector comprising a polynucleotide sequence encoding a guide RNA and under the control of a second promoter, wherein the guide RNA has a nucleic acid sequence which recognizes a nucleic acid sequence comprised at a desired target locus in the genome of the cell, and (iii) transforming the cell with a repair oligonucleotide.

The ThermoCas9 nuclease of the specified sequence and variant and fragments noted above is the ThermoCas9 of the aspects of the invention described hereinafter. The active fragments of the ThermoCas9 have guide RNA directed endonuclease activity with respect to target sequences in the genome of cells or organisms which are desired to be modified.

The genome of the cell may be modified first to express the ThemoCas9, whether constitutively or inducible, after which the cell is transformed with the expression vector for the gRNA; optionally at the same time or separately of transformation with the repair-oligo. In one possibility, the cell may be transformed simultaneously with all three elements, ThermoCas9 integration vector, gRNA expression vector and repair oligonucleotide.

In alternative aspect, the invention provides a method of modifying the genetic material of a eukaryotic cell, comprising (i) integrating a polynucleotide encoding a ThermoCas9 under the control of a first promoter into the genome of the cell, wherein the expressed ThermoCas9 comprises an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith, or an active fragment thereof; and (ii) transforming the cell with an expression vector comprising a polynucleotide sequence encoding a guide RNA under the control of the first or of a separate second promoter, wherein the guide RNA has a nucleic acid sequence which recognizes a nucleic acid sequence comprised at a desired target locus in the genome of the cell, and a repair oligonucleotide also under the control of the first or the second promoter, or a separate third promoter.

The repair oligonucleotide is preferably a double-stranded DNA repair oligo; optionally comprising a polynucleotide sequence for insertion into the genome of the cell by way of homologous recombination following guide RNA directed ThermoCas9 endonuclease cutting. Therefore, the repair oligo which does not contain and insert may be used to achieve a deletion of a desired locus or gene segment in the genome of the cell.

In some embodiments, the first promoter is a constitutive promoter, e.g. TEF1 promoter. In other embodiments, the first promoter may be a physical or chemically inducible promoter of the kinds described hereinafter in connection with other aspects of the invention.

Various combinations of promoter are possible in accordance with the invention such that the the second promoter may be a constitutive or inducible promoter. Any third promoter may be a constitutive or inducible promoter.

The cell may be transformed with the expression plasmid(s) and/or the repair-oligo by heat-shock or for example by electroporation.

Certain eukaryotic cells are able to grow at temperatures up to about 62° C.-63° C. Various fungi or algae or blue green algae, for example. Therefore the methods of the invention may be employed wherein the cell is transformed and/or grown following transformation at a temperature in the range 26° C.-63° C.; preferably 31° C.-61° C.; more preferably 35° C.-60° C.; even more preferably 34° C.-41° C., e.g. 37° C. Other temperatures may be used falling within the ranges selected from any of the following ranges, as shown by the upper and lower limit combinations marked “x” in the table below:

In some methods of the invention the eukaryotic cell is a fungus, particularly a yeast, e.g. Saccaharomyces sp., e.g. S. cerevisiae.

The present invention also provides a polynucleotide expression vector for modifying the genetic material at a target locus of a prokaryotic host organism which comprises the expression vector, the vector comprising:


- - a. a polynucleotide sequence encoding a Cas9 nuclease, wherein the
    Cas9 nuclease comprises an amino acid sequence of SEQ ID NO: 1 or a
    sequence of at least 77% identity therewith, or an active fragment
    thereof;
  - b. a polynucleotide sequence encoding a guide RNA, wherein the guide
    RNA has a nucleic acid sequence which recognizes a nucleic acid
    sequence comprised in the target locus;
  - c. a first promoter oriented with respect to polynucleotide
    sequences of (a) and (b) so as to drive expression thereof in the
    organism.

In preferred aspects, the prokaryotic organisms are thermophilic bacteria, as further defined hereinafter.

The expression vector of the invention may be used alone or in conjunction with a second expression vector.

Preferably, the sequence of (a) is 3′ of the promoter and the sequence of (b) is 3′ of the sequence of (b).

Additionally, the expression vector may further comprise a polynucleotide sequence which encodes an homologous recombination (HR) fragment under the control of the first promoter or a separate second promoter.

Where a single expression vector is used in methods of the invention described herein, and there are first and second promoters, the first promoter may be an inducible promoter. The second promoter may be a constitutive promoter or an inducible promoter. When the second promoter is an inducible promoter it may be the same or different as the first inducible promoter.

The inducible promoter(s) may be physically or chemically inducible. Some preferred chemically inducible promoters include a β-glucosidase promoter inducible with cellobiose or a Pm promoter inducible with 3-methylbenzoate. When the second promoter controlling the HR fragment is a constitutive promoter then this may be the P3 promoter.

The arms of the HR fragment may comprise a nucleic acid sequence which allows recombination upstream and downstream, respectively, of a locus of interest in the host organism. In operation, a double recombination event involving each arm (respectively) of the HR fragment, either side of a locus of interest, serves to replace the locus with the HR fragment. Therefore, expression of the guide RNA, the ThermoCas9 and the HR fragment by the vector results in the deletion of a locus of interest, e.g. gene of interest, from the genome of the prokaryotic organism.

The locus of interest herein comprises the target sequence recognized by the guide RNA.

The HR fragment may also comprise an insertion element between the upstream and downstream arms thereof. In this mode of operation, a vector of the invention when expressed in a transformed host cell results in a substitution at the locus of interest. When the insertion element is a gene of interest then expression of the vector in a transformed host results in a gene substitution, e.g. from a native gene in the organism to a new gene of interest, possibly an heterologous gene from another species or organism. In some instances, the new gene of interest may also be provided with a promoter, optionally an inducible promoter so that expression of the new gene can be switched on in the transformed organism as desired.

The locus of interest as described herein may comprise the PAM sequence 5′-NNNNCNN-3′ located 3′ of the target sequence; optionally at least 2, 3, 4, 5, 6 or more nucleotides from the target sequence.

In preferred vectors, the nucleotide sequence encoding the guide RNA preferably encodes a single guide RNA (sgRNA).

In another aspect, the invention provides methods employing any of the expression vectors of the invention described herein. Therefore, the invention provides a method of modifying the genetic material of a prokaryotic organism comprising transforming the organism with a first expression vector which comprises:


- - (a) a polynucleotide sequence encoding a Cas9 nuclease, wherein the
    Cas9 nuclease comprises an amino acid sequence of SEQ ID NO: 1 or a
    sequence of at least 77% identity therewith, or an active fragment
    thereof;
  - (b) a polynucleotide sequence encoding a guide RNA, wherein the
    guide RNA has a nucleic acid sequence which recognizes a nucleic
    acid sequence comprised in the target locus;
  - (c) a first promoter oriented with respect to polynucleotide
    sequences of (a) and (b) so as to drive expression thereof in the
    organism; and,  
    a second expression vector comprising a polynucleotide sequence
    which encodes an homologous recombination (HR) fragment under the
    control of a promoter.

In another aspect, the invention provides a method of modifying the genetic material of a prokaryotic organism comprising transforming the organism with a single expression vector comprising (a), (b), and (c) above and also a polynucleotide sequence which encodes an homologous recombination (HR) fragment under the control of the said first promoter or a separate second promoter.

The organism may be transformed e.g. using electroporation.

In methods of the invention, the transformed organism is cultured for a period at a first temperature, and then cultured at a second temperature before or during induction of the promoter of the Cas9 sequence. Advantageously to improve the recombination efficiency, an incubation step may be carried out at the elevated temperature, at which the plasmid cannot replicate.

The first temperature may be 60° C. or less and the second temperature is a higher temperature which may be at least 55° C. Alternatively, the first temperature may be 55° C. or less and the second temperature may be greater than 55° C. The different temperatures to be used may readily be selected by a person of average skill in the art, depending on the particular prokaryotic organism being modified, particularly a thermophilic bacterium.

In some preferred methods, the organism being modified is selected from Geobacillus thermoglucosidans, Bacillus coagulans or Pseudomonas putida.

Also provided by the invention is a prokaryotic cell, e.g. a bacterial cell, transformed with an expression vector of the invention as hereinbefore defined.

In accordance with the invention is a method of genetically modifying a thermophilic prokaryotic organism comprising transforming with a single expression plasmid as defined above at a first temperature and then subjecting the organism to an elevated temperature during which there is homologous recombination selected over plasmid multiplication. Such elevated temperatures may be in the range range 55° C. to 100° C., 60° C. to 100° C., 65° C. to 100° C., 70° C. to 100° C., 75° C. to 100° C., 80° C. to 100° C., 85° C. to 100° C., 90° C. to 100° C., 95° C. to 100° C.

Further, the present invention provides an isolated clustered regularly interspaced short palindromic repeat (CRISPR)-associated (Cas) protein or polypeptide comprising;


- - a. the amino acid motif EKDGKYYC \[SEQ ID NO: 2\]; and/or
  - b. the amino acid motif X₁X₂CTX₃X₄ \[SEQ ID NO: 3\] wherein X₁ is
    independently selected from Isoleucine, Methionine or Proline, X₂ is
    independently selected from Valine, Serine, Asparagine or
    Isoleucine, X₃ is independently selected from Glutamate or Lysine
    and X₄ is one of Alanine, Glutamate or Arginine; and/or
  - c. the amino acid motif X₅LKX₆IE \[SEQ ID NO: 4\] wherein X₅ is
    independently selected from Methionine or Phenylalanine and X₆ is
    independently selected from Histidine or Asparagine; and/or
  - d. the amino acid motif X₇VYSX₈K \[SEQ ID NO: 5\] wherein X₇ is
    Glutamate or Isoleucine and X₈ is one of Tryptophan, Serine or
    Lysine; and/or
  - e. the amino acid motif X₉FYX₁₀X₁₁REQX₁₂KEX₁₃ \[SEQ ID NO: 6\]
    wherein X₉ is Alanine or Glutamate, X₁₀ is Glutamine or Lysine, X₁₁
    is Arginine or Alanine, X₁₂ is Asparagine or Alanine and X₁₃ is
    Lysine or Serine.

For the avoidance of doubt proteins, polypeptides or nucleic acids coding for Cas proteins of the present invention may also be referred to as “GtCas9” or “ThermoCas9”. “GtCas9” and “ThermoCas9” are used interchangeably throughout the specification and have the same meaning.

A polypeptide in the context of this invention may be viewed as a fragment of the full length Cas protein. Such fragments may be inactive and used in ways and for purposes not associated directly with binding, editing and/or cutting of genetic material, for example for standards in assays or raising antibodies or the like.

In preferred embodiments however, the Cas protein or polypeptide is functional and capable of cleavage, binding, marking or modifying at a temperature in the range 20° C. and 100° C., inclusive, when associated with at least one targeting RNA molecule, and a polynucleotide comprising a target nucleic acid sequence recognised by the targeting RNA molecule.

Preferably the Cas protein or polypeptide is functional and capable of said cleavage, binding, marking or modifying at a temperature in the range 50° C. and 70° C., for example 55° C. or 60° C.

In particular embodiments, the invention may provide a Cas protein or polypeptide comprising the amino acid motif EKDGKYYC [SEQ ID NO: 2]. In other embodiments, the Cas proteins or polypeptides may further comprise the amino acid motif X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine.

In other embodiments the Cas proteins or polypeptides defined herein may additionally further comprise the amino acid motif X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine.

In other embodiments, the Cas proteins or polypeptides defined herein may additionally further comprise the amino acid motif X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

In other embodiments, the Cas proteins or polypeptides defined herein may additionally further comprise the amino acid motif X9FYX10X11REQX12KEX13[SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

In accordance with the present invention, it may be appreciated that a Cas protein or polypeptide of the invention may comprise any of the motifs of SEQ ID NOs 2 to 6, either alone or in combination. The following summarises each of the combinations of motifs which may characterize Cas proteins or polypeptides of the invention:

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine.

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine.

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine.

EKDGKYYC [SEQ ID NO: 2]; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

EKDGKYYC [SEQ ID NO: 2]; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

EKDGKYYC [SEQ ID NO: 2]; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

EKDGKYYC [SEQ ID NO: 2]; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

X1X2CTX3X4[SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13[SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine.

X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and X9FYX10X11REQX12KEX13[SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine.

In another aspect, the present invention provides an isolated Cas protein or polypeptide fragment thereof having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith, wherein the Cas protein or polypeptide fragment thereof comprises any of the following motifs or amino acids, either alone or in combination:

An RuvC-I domain comprising IGLDIGITSIG [SEQ ID NO: 23], preferably IGLDIGITSIGWAVINLD [SEQ ID NO: 24].

A Bridge domain comprising RSARR [SEQ ID NO: 25], preferably PRRLARSARRRLRRRKHRLERIRRL [SEQ ID NO: 26]; and/or

An α-helical/recognition lobe domain comprising WQLR [SEQ ID NO: 27]; and/or

An α-helical/recognition lobe domain comprising HLAKRRG [SEQ ID NO: 28], preferably LARILLHLAKRRG [SEQ ID NO: 29]; and/or

An α-helical/recognition lobe domain comprising IFAKQ [SEQ ID NO: 30], preferably EIKLIFAKQ [SEQ ID NO: 31]; and/or

An α-helical/recognition lobe domain comprising IWASQR [SEQ ID NO: 32]; and/or

KVGFCTFEPKEKRAPK [SEQ ID NO: 33]; and/or

FTVWEHINKLRL [SEQ ID NO: 34]; and/or

An RuvC-II domain comprising the motif IANPVVMRALTQ [SEQ ID NO: 35], preferably IANPWMRALTQARKVVNAIIKKYG [SEQ ID NO: 36]; and/or

An RuvC-II domain comprising the motif ELAR [SEQ ID NO: 37], preferably IHIELARE [SEQ ID NO: 38]; and/or

An HNH domain comprising the motif QNGKCAY [SEQ ID NO: 39], preferably IVKFKLWSEQNGKCAY [SEQ ID NO: 40]; and/or

An HNH domain comprising the motif VDHVIP [SEQ ID NO: 41], preferably VDHVIPYSRSLDDSYTNKVL [SEQ ID NO: 42]; and/or

An RuvC-III domain comprising the motif DTRYISRFLAN [SEQ ID NO: 43]; and/or An RuvC-III domain comprising the motif VYTVNGRITAHLRSRW [SEQ ID NO: 44]; and/or

An RuvC-III domain comprising the motif HHAVDA [SEQ ID NO: 45], preferably HHAVDAAIVA [SEQ ID NO: 46]; and/or

Preferably, the present invention provides an isolated Cas protein or polypeptide fragment thereof having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith, wherein the Cas protein or polypeptide fragment thereof comprises each of the amino acid motifs [SEQ ID NO: 23] to [SEQ ID NO: 46] in combination.

In another aspect, the present invention provides an isolated Cas protein or polypeptide fragment thereof having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith. Preferably the Cas protein or polypeptide is capable of binding, cleavage, marking or modifying at a temperature in the range 20° C. and 100° C. inclusive. Preferably the Cas protein or polypeptide is capable of said cleavage, binding, marking or modifying at a temperature in the range between 20° C. and 70° C., for example 25° C., 55° C., 60° C. or 65° C. Preferably the Cas protein or polypeptide is capable of said cleavage, binding, marking or modifying at a temperature in the range between 50° C. and 70° C., for example 55° C. or 60° C. Preferably the Cas protein or polypeptide is capable of said cleavage, binding, marking or modifying at a temperature in the range between 30° C. and 80° C., at a temperature between 37° C. and 78° C., preferably at a temperature above 55° C.; more preferably at a temperature between 55° C. and 80° C.; even more preferably at a temperature between 55° C. and 65° C. or 60° C. and 65° C.

The present invention also provides uses of a targeting RNA molecule and a Cas protein or polypeptide provided herein, for binding, cleaving, marking or modifying a target polynucleotide comprising a target nucleic acid sequence. The targeting RNA molecule recognizes the target nucleic acid sequence on a target nucleic acid strand of the polynucleotide.

The target polynucleotide that comprises the target nucleic acid sequence may be double stranded and so comprise a target nucleic acid strand, comprising said target nucleic acid sequence, and a non-target nucleic acid strand, comprising a protospacer nucleic acid sequence. The protospacer nucleic acid sequence is substantially complementary to the target nucleic acid sequence and pairs with it in the double stranded target polynucleotide. The non-target nucleic acid strand may further comprise a protospacer adjacent motif (PAM) sequence directly adjacent the 3′ end of the protospacer sequence. The PAM sequence may be at least 6, 7, or 8 nucleic acids in length. Preferably, the PAM sequence has a cytosine in the fifth position. Preferably the PAM sequence comprises the sequence 5′-NNNNC-3′, so that from the 5′-end the PAM sequence begins 5′-NNNNC-3′. Additionally or alternatively, the PAM sequence may have an adenine in the eighth position, so that the PAM sequence comprises the sequence 5′-NNNNNNNA-3′, and from the 5′-end the PAM sequence begins 5′-NNNNNNNA-3′. Additionally or alternatively, the PAM sequence may have a cytosine in one or more of the first, second, third, fourth, and sixth positions, such that from the 5′-end the PAM sequence begins 5′-CNNNN-3′, 5′-NCNNN-3′, 5′-NNCNN-3′, 5′-NNNCN-3′, and/or 5′-NNNNNC-3′. Optionally the PAM sequence comprises, so that from the 5′-end the PAM sequence begins, 5′-CCCCCCNA-3′ [SEQ ID NO: 10], and further preferably the PAM sequence comprises, so that from the 5′-end the PAM sequence begins, 5′-CCCCCCAA-3′ [SEQ ID NO: 11]. Other preferred PAM sequences include 5′-ATCCCCAA-3′ [SEQ ID NO: 21] and 5′-ACGGCCAA-3′ [SEQ ID NO: 22].

Preferably, the Cas protein or polypeptide is capable of the binding, cleaving, marking or modifying at a temperature in the range 40° C. to 80° C. inclusive, preferably in the range 45° C. to 80° C. inclusive, and further preferably in the range 50° C. to 80° C. inclusive. For example, the binding, cleaving, marking or modifying occurs at a temperature of 45° C., 46° C., 47° C., 48° C., 49° C., 50° C., 51° C., 52° C., 53° C., 54° C., 55° C., 56° C., 57° C., 58° C., 59° C., 60° C., 61° C., 62° C., 63° C., 64° C., 65° C., 66° C., 67° C., 68° C., 69° C., 70° C., 71° C., 72° C., 73° C., 74° C., 75° C., 76° C., 77° C., 78° C., 79° C. or 80° C. More preferably the Cas protein or polypeptide is capable of the binding, cleaving, marking or modifying at a temperature in the range 55 to 65° C. In preferred aspects, a Cas protein or polypeptide fragment of the invention may comprises an amino acid sequence of at least 75% identity; preferably at least 85%; more preferably at least 90%; even more preferably at least 95% identity to SEQ ID NO: 1.

The Cas protein or polypeptide may be used in combination with a targeting RNA molecule that recognizes a target nucleic acid sequence on the target nucleic acid strand, where the non-target nucleic acid sequence has a PAM sequence directly adjacent the 3′ end of the protospacer sequence on the non-target strand, as disclosed herein. Thus, the PAM sequence may comprise the sequence 5′-NNNNC-3′, and the Cas protein may bind, cleave, mark or modify the target strand at a temperature in the range 20° C. and 100° C. inclusive, preferably in the range 30° C. and 90° C. inclusive, in the range 37° C. and 78° C. inclusive, in the range 40° C. and 80° C. inclusive, in the range 50° C. and 70° C. inclusive, or in the range 55° C. and 65° C., inclusive. Preferably from the 5′-end the PAM sequence begins 5′-NNNNC-3′ and the Cas protein may bind, cleave, mark or modify the target strand at a temperature in the range 20° C. and 100° C. inclusive, preferably in the range 30° C. and 90° C. inclusive, in the range 37° C. and 78° C. inclusive, in the range 40° C. and 80° C. inclusive, in the range 50° C. and 70° C. inclusive, or in the range 55° C. and 65° C., inclusive. Preferably from the 5′-end the PAM sequence begins 5′-NNNNNNNA-3′ and the Cas protein may bind, cleave, mark or modify the target strand at a temperature in the range 20° C. and 100° C. inclusive, preferably in the range 30° C. and 90° C. inclusive, in the range 37° C. and 78° C. inclusive, in the range 40° C. and 80° C. inclusive, the range 50° C. and 70° C. inclusive, or in the range 55° C. and 65° C., inclusive. Further preferably the 5′-end of the PAM sequence begins 5′-NNNNCNNA-3′ [SEQ ID NO: 47] and the Cas protein may bind, cleave, mark or modify the target strand at a temperature in the range 20° C. and 100° C. inclusive, preferably in the range 30° C. and 90° C. inclusive, in the range 37° C. and 78° C. inclusive, in the range 40° C. and 80° C. inclusive, in the range 50° C. and 70° C. inclusive, or in the range 55° C. and 65° C., inclusive.

More particularly, a Cas protein or polypeptide of the invention may comprise an amino acid sequence with a percentage identity with SEQ ID NO:1 as follows: at least 60%, at least 61%, at least 62%, at least 63%, at least 64%, at least 65%, at least 66%, at least 67%, at least 68%, at least 69%, at least 70%, at least 71%, at least 72%, at least 73%, at least 74%, at least 75%, at least 76%, at least 77%, at least 78%, at least 79%, at least 80%, at least 81%, at least 82%, at least 83%, at least 84%, at least 85%, at least 86%, at least 87%, at least 88%, at least 89%, at least 90%, at least 91%, at least 92%, at least 93%, at least 94%, at least 95%, at least 96%, at least 97%, at least 98%, at least 99%, at least 99.5% or at least 99.8%. The percentage identity may be at least 89%. The percentage identity may be at least 90%. Preferably the percentage identity will be at least 95%, for example 98%.

The percentage amino acid sequence identity with SEQ ID NO: 1 is determinable as a function of the number of identical positions shared by the sequences in a selected comparison window, taking into account the number of gaps, and the length of each gap, which need to be introduced for optimal alignment of the two sequences.

A Cas protein or polypeptide fragment of the invention may be characterised in terms of both the reference sequence SEQ ID NO: 1 and any aforementioned percentage variant thereof as defined by percentage sequence identity, alone or in combination with any of the aforementioned amino acid motifs (i.e. SEQ ID NOS 2 and/or 3 and/or 4 and/or 5 and/or 6) as essential features.

The invention provides a use of a targeting RNA molecule as provided herein and a Cas protein or polypeptide of the invention for binding, cleaving, marking or modifying a target nucleic acid strand comprising a target nucleic acid sequence. Preferably said binding, cleaving, marking or modifying occurs at a temperature disclosed herein, for example at a temperature of between 20 and 100° C. The invention also provides a method of binding, cleaving, marking or modifying a target nucleic acid sequence in a target nucleic acid strand comprising designing a targeting RNA molecule as provided herein and forming a ribonucleoprotein complex comprising the targeting RNA molecule and a Cas protein or polypeptide of the invention. Preferably the ribonucleoprotein complex binding, cleaving, marking or modifying the target nucleic acid sequence at a temperature disclosed herein, for example at a temperature of between 37 and 100° C.

The uses and methods of the invention may be carried out, and the nucleoproteins of the invention formed and used, in vivo, for example in bacterial cells. The uses and methods of the invention may be carried out, and the nucleoproteins of the invention formed and used, in vivo, except in human cells. Alternatively the uses and methods of the invention may be carried out, and the nucleoproteins of the invention formed and used, in vitro. The Cas protein of the invention may be provided in isolated form, for example when used in vitro or when added to cells by transfection, the Cas protein may be heterologously expressed, for example following transient or stable transformation of the cell by nucleic acid encoding the Cas protein, the targeting RNA molecule may be transcribed from an expression vector following transient or stable transformation of the cell by nucleic acid encoding the RNA molecule, and/or the RNA molecule may be provided in isolated form, for example when used in vitro or when added to cells by transfection. In preferred embodiments, the Cas protein or polypeptide is expressed from the genome of a host cell, following stable intergration of a nucleic acid encoding the Cas protein or polypeptide in the genome of the host cell. Thus the Cas protein and/or RNA molecule may be added to the in vivo or in vitro environment using any artificial or contrived method for adding a protein or nucleic acid molecule to a cell in which it is not otherwise present.

The polynucleotide comprising the target nucleic acid sequence may be cleaved by the Cas protein, and optionally the cleavage may be DNA cleavage. The target nucleic acid strand comprising the target sequence may be double stranded DNA and the method or use may result in a double stranded break in the polynucleotide comprising the target nucleic acid sequence. The polynucleotide comprising the target nucleic acid sequence may be double stranded DNA, the Cas protein may lack the ability to cut the double stranded DNA and the use or method may result in gene silencing of the polynucleotide.

The Cas protein or polypeptide may be provided for the methods, uses and nucleoproteins of the invention at a concentration of 250 nM or less, for example at a concentration of 200 nM or less, 150 nM or less, 100 nM or less, 50 nM or less, 25 nM or less, 10 nM or less, 5 nM or less, 1 nM or less or 0.5 nM or less. Alternatively, the Cas protein or polypeptide may be provided at a concentration of at least 0.5 nM, at least 1 nM, at least 5 nM, at least 10 nM, at least 25 nM, at least 50 nM, at least 100 nM, at least 150 nM, at least 200 nM, or at least 250 nM. The PAM sequence of the invention may have an adenine in the eighth position, so that the PAM sequence comprises the sequence 5′-NNNNNNNA-3′, and the concentration of Cas protein or polypeptide may be 100 nM or less, 50 nM or less, 25 nM or less, 10 nM or less, 5 nM or less, 1 nM or less or 0.5 nM or less. The PAM sequence may comprise the sequence 5′-NNNNCNNA-3′ [SEQ ID NO: 47], and the concentration of Cas protein or polypeptide may be 100 nM or less, 50 nM or less, 25 nM or less, 10 nM or less, 5 nM or less, 1 nM or less or 0.5 nM or less. The PAM sequence may comprise the sequence 5′-CCCCCCNA-3′ [SEQ ID NO: 10], and the concentration of Cas protein or polypeptide may be 100 nM or less, 50 nM or less, 25 nM or less, 10 nM or less, 5 nM or less, 1 nM or less or 0.5 nM or less.

Also, the invention provides nucleic acids encoding any of the aforementioned proteins or polypeptides of the invention. The nucleic acids may be isolated or in the form of expression constructs.

In all aforementioned aspects of the present invention, amino acid residues may be substituted conservatively or non-conservatively. Conservative amino acid substitutions refer to those where amino acid residues are substituted for other amino acid residues with similar chemical properties (e.g., charge or hydrophobicity) and therefore do not alter the functional properties of the resulting polypeptide.

Similarly it will be appreciated by a person of average skill in the art that nucleic acid sequences may be substituted conservatively or non-conservatively without affecting the function of the polypeptide. Conservatively modified nucleic acids are those substituted for nucleic acids which encode identical or functionally identical variants of the amino acid sequences. It will be appreciated by the skilled reader that each codon in a nucleic acid (except AUG and UGG; typically the only codons for methionine or tryptophan, respectively) can be modified to yield a functionally identical molecule. Accordingly, each silent variation (i.e. synonymous codon) of a polynucleotide or polypeptide, which encodes a polypeptide of the present invention, is implicit in each described polypeptide sequence.

The invention provides a transformed cell, having a target nucleic acid sequence in a double stranded target polynucleotide, said cell comprising a Cas protein or polypeptide as provided herein and at least one targeting RNA molecule as provided herein, and an expression vector comprising a nucleic acid encoding at least one of said Cas protein and said targeting RNA molecule. The Cas protein and targeting RNA molecule may enable or permit binding, cleaving, marking or modifying of the target sequence to occur in the transformed cell at a raised temperature, or at a range of temperatures, for example between 37 and 100° C., as disclosed herein. The invention further provides a method of binding, cleaving, marking or modifying a target nucleic acid in a cell comprising either 1) transforming, transfecting or transducing the cell with an expression vector comprising a nucleotide sequence encoding a Cas protein or polypeptide of the invention and a nucleotide sequence encoding a targeting RNA molecule of the invention; or 2) transforming, transfecting or transducing the cell with an expression vector comprising a nucleotide sequence encoding a Cas protein or polypeptide of the invention and a further expression vector comprising a nucleotide sequence encoding a targeting RNA molecule of the invention; or 3) transforming, transfecting or transducing the cell with an expression vector comprising a nucleotide sequence encoding a Cas protein or polypeptide of the invention, and delivering a targeting RNA molecule as provided herein to, or into the cell. The Cas protein or polypeptide may be expressed from the genome of the transformed cell, for example following stable integration into the genome of a nucleotide sequence encoding the Cas protein or polypeptide.

The invention also provides kits comprising one or more of the reagents for carrying out the uses and methods of the invention, or for generating the transformed cells or nucleoprotein complex of the invention, said kits including: a Cas protein or polypeptide of the invention or an expression vector comprising a nucleic acid sequence encoding a Cas protein or polypeptide of the invention; and/or a targeting RNA molecule of the invention or an expression vector comprising a nucleic acid sequence encoding a targeting RNA molecule of the invention. The kits may further include instructions for carrying out the invention, for example instructions for how to design a targeting RNA molecule in accordance with the invention.

## RNA Guides and Target Sequences

Cas proteins of the invention allow for sequence-specific binding, cleavage, tagging, marking or modification of target nucleic acids at elevated temperatures. Target nucleic acids may be DNA (single-stranded or double-stranded), RNA or synthetic nucleic acids. A particularly useful application of the present invention is the sequence-specific targeting and modification of genomic DNA by one or more Cas proteins of the invention in complex with one or more guide RNAs (gRNAs) that complementarily bind to a targeted sequence of the genomic DNA. Consequently, the target nucleic acid is preferably double-stranded DNA. Such targeting may be performed in vitro or in vivo. Preferably such targeting is performed in vivo. In this way, Cas proteins of the invention may be used to target and modify specific DNA sequences located in the genomic DNA of a cell. It is envisaged that the Cas system may be used to modify genomes in a variety of cell types of and/or in different organisms.

The gRNAs, also called targeting RNA molecules, recognize the target nucleic acid sequence on the polynucleotide target strand. The RNA molecules may be designed to recognize a target sequence in a double stranded target polynucleotide, wherein the non-target strand comprises a protospacer adjacent motif (PAM) sequence directly adjacent the 3′ end of the protospacer sequence. Disclosed herein are PAM sequences that work in an optimal manner with the Cas proteins and polypeptides of the invention. With knowledge of these PAM sequences, gRNAs may be designed for use with the Cas proteins and polypeptides of the invention across the temperature ranges and increased temperatures of the invention.

Accordingly, the present invention provides a ribonucleoprotein complex comprising a Cas protein or a polypeptide of the invention as hereinbefore described, and further comprising at least one RNA molecule which has a targeting function in that it recognizes a particular nucleotide sequence in a target polynucleotide. The present invention also provides use of at least one targeting RNA molecule and a Cas protein or polypeptide for binding, cleaving, marking or modifying a target nucleic acid strand, and a method of binding, cleaving, marking or modifying a target nucleic acid sequence in a target nucleic acid strand using a ribonucleoprotein or nucleoprotein of the invention, as well as transformed non-human cells having the Cas protein or polypeptide and targeting RNA molecule. The target polynucleotide may further comprise a defined PAM sequence directly adjacent the 3′ end of a protospacer sequence, in accordance with a PAM sequence provided herein. The PAM sequence may be 6, 7, or 8 nucleic acids in length, or longer, preferably 8 nucleic acids in length. Preferably, the RNA molecule is a single-stranded RNA molecule, e.g. a CRISPR RNA (crRNA) and is associated, e.g. by hybridization with a tracrRNA. The targeting RNA may be a chimera of a crRNA and tracrRNA. The aforementioned RNA molecules may have a ribonucleotide sequence of at least 90% identity, or complementarity to a target nucleotide sequence. Optionally, the RNA molecule has a ribonucleotide sequence of at least 90%, at least 91%, at least 92%, at least 93%, at least 94%, at least 95%, at least 96%, at least 97%, at least 98%, at least 99% or 100% identity or complementarity to a target nucleotide sequence. The preferred target nucleotide sequence is a DNA.

In a preferred aspect, the present invention provides a ribonucleoprotein complex as hereinbefore described, wherein the at least one targeting RNA molecule is substantially complementary along its length to a target DNA sequence.

The targeting RNA molecule may be bound to or associated with the target sequence within the nucleoprotein complex, so that the target polynucleotide, comprising the target sequence and PAM sequence on the non-target strand, may be associated with and so form part of a nucleoprotein complex of the invention.

Alteration of the sequence of the RNA guide which associates with the Cas protein of the invention therefore allows the Cas protein to be programmed to mark or cut double-stranded DNA at sites complementary to the guide RNA.

Preferably, the length of the at least one targeting RNA molecule in a ribonucleoprotein complex of the invention is in the range 35 to 135 residues, optionally in the range 35 to 134 residues, 35 to 133 residues, 35 to 132 residues, 35 to 131 residues, 35 to 130 residues, 35 to 129 residues, 35 to 128 residues, 35 to 127 residues, 35 to 126 residues, 35 to 125 residues, 35 to 124 residues, 35 to 123 residues, 35 to 122 residues, 35 to 121 residues, 35 to 120 residues, 35 to 119 residues, 35 to 118 residues, 35 to 117 residues, 35 to 116 residues, 35 to 115 residues, 35 to 114 residues, 35 to 113 residues, 35 to 112 residues, 35 to 111 residues, 35 to 100 residues, 35 to 109 residues, 35 to 108 residues, 35 to 107 residues, 35 to 106 residues, 35 to 105 residues, 35 to 104 residues, 35 to 103 residues, 35 to 102 residues, 35 to 101 residues, 35 to 100 residues, 35 to 99 residues, 35 to 98 residues, 35 to 97 residues, 35 to 96 residues, 35 to 95 residues, 35 to 94 residues, 35 to 93 residues, 35 to 92 residues, 35 to 91 residues, 35 to 90 residues, 35 to 89 residues, 35 to 88 residues, 35 to 87 residues, 35 to 86 residues, 35 to 85 residues, 35 to 84 residues, 35 to 83 residues, 35 to 82 residues, 35 to 81 residues, 35 to 80 residues, 35 to 79 residues, 35 to 78 residues, 35 to 77 residues, 35 to 76 residues, 35 to 75 residues, 35 to 74 residues, 35 to 73 residues, 35 to 72 residues, 35 to 71 residues, 35 to 70 residues, 35 to 69 residues, 35 to 68 residues, 35 to 67 residues, 35 to 66 residues, 35 to 65 residues, 35 to 64 residues, 35 to 63 residues, 35 to 62 residues, 35 to 61 residues, 35 to 60 residues, 35 to 59 residues, 35 to 58 residues, 35 to 57 residues, 35 to 56 residues, 35 to 55 residues, 35 to 54 residues, 35 to 53 residues, 35 to 52 residues, 35 to 51 residues, 35 to 50 residues, 35 to 49 residues, 35 to 48 residues, 35 to 47 residues, 35 to 46 residues, 35 to 45 residues, 35 to 44 residues, 35 to 43 residues, 35 to 42 residues, 35 to 41 residues, 35 to 40 residues, 35 to 39 residues, 35 to 38 residues, 35 to 37 residues, 35 to 36 residues or 35 residues. Preferably, the length of the at least one RNA molecule is in the range 36 to 174 residues, 37 to 173 residues, 38 to 172 residues, 39 to 171 residues, 40 to 170 residues, 41 to 169 residues, 42 to 168 residues, 43 to 167 residues, 44 to 166 residues, 45 to 165 residues, 46 to 164 residues, 47 to 163 residues, 48 to 162 residues, 49 to 161 residues, 50 to 160 residues, 51 to 159 residues, 52 to 158 residues, 53 to 157 residues, 54 to 156 residues, 36 to 74 residues, 37 to 73 residues, 38 to 72 residues, 39 to 71 residues, 40 to 70 residues, 41 to 69 residues, 42 to 68 residues, 43 to 67 residues, 44 to 66 residues, 45 to 65 residues, 46 to 64 residues, 47 to 63 residues, 48 to 62 residues, 49 to 61 residues, 50 to 60 residues, 51 to 59 residues, 52 to 58 residues, 53 to 57 residues, 54 to 56 residues.

In preferred aspects, the present invention provides a ribonucleoprotein complex, wherein the complementary portion of the at least one RNA molecule is at least 30 residues long. Alternatively, the complementary portion of the at least one RNA molecule may be 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74 or 75 residues long.

The targeting RNA molecule will preferably require a high specificity and affinity for the target nucleic acid sequence. A dissociation constant (Kd) in the range 1 μM to 1 μM, preferably 1 nM to 1 pM; more preferably 1-100 pM is desirable as may be determined by native gel electrophoresis, or alternatively isothermal titration calorimetry, surface plasmon resonance, or fluorescence based titration methods. Affinity may be determined using an electrophoretic mobility shift assay (EMSA), also called gel retardation assay (see Semenova et al. (2011) PNAS 108: 10098-10103).

The targeting RNA molecule is preferably modeled on what are known from nature in prokaryotes as CRISPR RNA (crRNA) molecules. The structure of crRNA molecules is already established and explained in more detail in Jore et al., 2011, Nature Structural & Molecular Biology 18: 529-537. In brief, a mature crRNA of type I-E is often 61 nucleotides long and consists of a 5′ “handle” region of 8 nucleotides, the “spacer” sequence of 32 nucleotides, and a 3′ sequence of 21 nucleotides which form a hairpin with a tetranucleotide loop (FIG. 5). Type I systems differ from type II (Cas9) and details of different systems are described in Van der Oost 2014 Nat Rev Micr 12: 479-492. In type II (Cas9) systems there is a different processing mechanism, making use of a second RNA (tracrRNA) and two ribonucleases. Rather than a hairpin, the mature crRNA in type II remains attached to a fragment of the tracrRNA (FIG. 5). However, the RNA used in the invention does not have to be designed strictly to the design of naturally occurring crRNA, whether in length, regions or specific RNA sequences. What is clear though, is that RNA molecules for use in the invention may be designed based on gene sequence information in the public databases or newly discovered, and then made artificially, e.g. by chemical synthesis in whole or in part. The RNA molecules of the invention may also be designed and produced by way of expression in genetically modified cells or cell free expression systems and this option may include synthesis of some or all of the RNA sequence.

The structure and requirements of crRNA in type II (Cas9) has also been described in Jinek et al., 2012 ibid. In type I, there is a so-called “SEED” portion forming the 5′ end of the spacer sequence and which is flanked 5′ thereto by the 5′ handle of 8 nucleotides. Semenova et al. (2011, PNAS 108: 10098-10103), have found that all residues of the SEED sequence should be complementary to the target sequence, although for the residue at position 6, a mismatch may be tolerated (FIG. 5). In type II, there is a SEED of 10-12 nucleotides that is located at the 3′ end of the spacer (FIG. 5) (reviewed by Van der Oost 2014 ibid.). Similarly, when designing and making an RNA component of a ribonucleoprotein complex of the invention directed at a target locus (i.e. sequence), the necessary match and mismatch rules for the type II SEED sequence can be applied.

The invention therefore includes a method of detecting and/or locating a single base change in a target nucleic acid molecule comprising contacting a nucleic acid sample with a ribonucleoprotein complex of the invention as hereinbefore described, or with a Cas protein or polypeptide and separate targeting RNA component of the invention as hereinbefore described, and wherein the sequence of the targeting RNA (including when in the ribonucleoprotein complex) is such that it discriminates between a normal allele and a mutant allele by virtue of a single base change at, for example, position 6 of a contiguous sequence of 8 nucleotide residues.

Without wishing to be bound by a particular theory, a design rule which may be used in preparing a targeting RNA component of ribonucleoprotein complexes of the invention involves the so-called “PAM” (protospacer adjacent motif) sequence in a double stranded target polynucleotide. In the type I-E system of E. coli, the PAM sequence may be a conserved triplet of nucleotide residues, such as 5′-CTT-3′, 5′-CAT-3′, 5′-CCT-3′, 5′-CAC-3′, 5′-TTT-3′, 5′-ATT-3′, and 5′-AWG-3′, wherein W is A, T or U. In Type I, a PAM sequence located in the targeted strand is usually at a position corresponding to 5′ of the SEED. In Type II, however, the PAM is located at the other end, on the displaced, or non-target, strand close to the 3′ end of the crRNA spacer, at a position corresponding to 3′ of the seed (FIG. 5) (Jinek et al., 2012, op. cit.). For Streptococcus pyogenes Cas9, the PAM sequence has a conserved pair of nucleotide residues, 5′-NGG-3′. Recently, different Cas9 variants (Type IIA and Type IIC) (Ran et al., 2015 Nature 520:186-191)—FIG. 1A) have been characterized, and PAMs have been revealed (see Ran et al., 2015, ibid. —FIG. 10). Currently established Cas9 PAMs include: Type IIA 5′-NGGNNNN-3′ (Streptococcus pyogenes), 5′-NNGTNNN-3′ (Streptococcus pasteurianus), 5′-NNGGAAN-3′ (Streptococcus thermophilus), 5′-NNGGGNN-3′ (Staphylococcus aureus), and Type IIC 5′-NGGNNNN-3′ (Corynebacterium difteriae), 5′-NNGGGTN-3′ (Campylobacter lari), 5′-NNNCATN-3′ (Parvobaculum lavamentivorans), 5′-NNNNGTA-3′ (Neiseria cinerea). Cas9 of Geobacillus thermodenitrificans T12 (this invention) belongs to Type IIC (Ran et al., 2015, ibid.). The inventors have surprisingly found that the choice of PAM sequences for use with the invention can influence the temperature(s) at which the Cas proteins and polypeptides of the invention will interact with a target sequence. In particular, the inventors have found a preference for an 8-mer PAM sequence to confer activity across a broad temperature range, with a cytosine in the 5th position after the 3′ end of the target sequence, and/or an adenine in the 8th position. There is also a preference for cytosine in the 1st, 2nd, 3rd, 4th and/or 6th position of the PAM sequence after the 3′ end of the protospacer sequence.

In particular aspects, interaction with a target sequence within a broad temperature range of, for example 20° C. to 100° C., 20° C. to 80° C., 30 to 80° C., 20° C. to 70° C. or 25° C. to 65° C. may be achieved by utilizing a PAM sequence of 5′-NNNNCVAA-3′ [SEQ ID NO: 48]. There is no specific preference for the for the first 4 PAM positions. The first 4 nucleotides can therefore conveniently be any nucleotide (NNNN). Preferably, interaction with a target sequence within such a broad temperature range may be achieved by utilizing a PAM sequence of 5′-NNNNCSAA-3′ [SEQ ID NO: 49]. Optimally, the PAM may be of the sequence 5′-NNNNCGAA-3′ [SEQ ID NO: 50] or 5′-NNNNCCAA-3′ [SEQ ID NO: 51].

Where interaction with a target sequence is required at 30° C., e.g. 30° C. to 100° C., preferably in the range 30° C. to 70° C., 30° C. to 65° C., or 45° C. to 65° C. the PAM sequence may optimally be of the sequence 5′-NNNNCNAA-3′ [SEQ ID NO: 52] or 5′-NNNNCMCA-3′ [SEQ ID NO: 53]. There is no specific preference for the for the first 4 PAM positions. The first 4 nucleotides can therefore conveniently be any nucleotide (NNNN). Optionally, for example, the PAM sequence may be 5′-CCCCCNAA-3′ or 5′-CCCCCMCA-3′. Optionally, for example, the PAM sequence may be selected from 5′-CCCCCAAA-3′, 5′-CCCCCATA-3′, 5′-CCCCCAGA-3′, 5′-CCCCCACA-3′, 5′-CCCCCTAA-3′, 5′-CCCCCTTA-3′, 5′-CCCCCTGA-3′, 5′-CCCCCTCA-3′, 5′-CCCCCGAA-3′, 5′-CCCCCGTA-3′, 5′-CCCCCGGA-3′, 5′-CCCCCGCA-3′, 5′-CCCCCCAA-3′ [SEQ ID NO: 11], 5′-CCCCCCTA-3′, 5′-CCCCCCGA-3′, or 5′-CCCCCCCA-3′.

In embodiments of the invention, a targeting RNA molecule may have a length in the range of 35-200 residues. In preferred embodiments, the portion of the RNA which is complementary to and used for targeting a desired nucleic acid sequence is from 15 to 32 residues long. In the context of a naturally-occurring crRNA, this would correspond to the spacer portion as shown for example in FIG. 1 of Semenova et al. (2011 ibid.).

A ribonucleoprotein complex of the invention may have a targeting component comprising 8 residues derived from the CRISPR repeat 5′ to the RNA sequence which has substantial complementarity to the DNA target sequence. The RNA sequence having complementarity to the DNA target sequence would be understood to correspond in the context of a crRNA as being the spacer sequence. The 5′ flanking sequence of the RNA would be considered to correspond to the 5′ handle of a crRNA; as shown for example in FIG. 1 of Semenova et al. (2011 ibid.).

A ribonucleoprotein complex of the invention may have a hairpin and tetranucleotide loop forming sequence 3′ to the targeting RNA sequence which has complementarity to a DNA target sequence, i.e. 3′ to what would correspond to the 3′ handle flanking the spacer sequence in a crRNA; for example as shown in FIG. 1 of Semenova et al. (2011 ibid.).

Without wishing to be bound by a particular theory, in a preferred ribonucleoprotein complex and double stranded target polynucleotide, the non-target nucleic acid strand, which does not pair with the targeting RNA of the ribonucleoprotein complex, may comprise a directly 3′ adjacent PAM sequence selected from one or more of 5′-NNNNCNNA-3′ [SEQ ID NO: 47], 5′-CNNNCNN-3′, 5′-NNNCCNN-3′, 5′-NNCNCNN-3′, 5′-NNNNCCN-3′, and 5′-NCNNCNN-3′. Optionally, for example the PAM sequence may be selected from 5′-NNNNC-3′, 5′-NNNNCNNA-3′ [SEQ ID NO: 47], 5′-CNNNC-3′, 5′-CNNNCNNA-3′, 5′-NCNNC-3′, 5′-NCNNCNNA-3′, 5′-NNCNC-3′, 5′-NNCNCNNA-3′, 5′-NNNCC-3′, 5′-NNNCCNNA-3′, 5′-NNNNCC-3′, 5′-NNNNCCNA-3′, 5′-CCNNC-3′, 5′-CCNNCNNA-3′, 5′-CNCNC-3′, 5′-CNCNCNNA-3′, 5′-CNNCCN-3′, 5′-CNNCCNNA-3′, 5′-CNNNCC-3′, 5′-CNNNCCNA-3′, 5′-CCCNCN-3′, 5′-CCCNCNNA-3′, 5′-CCNCCN-3′, 5′-CCNCCNNA-3′, 5′-CCNNCC-3′, 5′-CCNNCCNA-3′, 5′-CCCCC-3′ [SEQ ID NO: 12], 5′-CCCCCNNA-3′ [SEQ ID NO: 13], 5′-CCCCCC-3′ [SEQ ID NO: 14], 5′-CCCCCCNA-3′ [SEQ ID NO: 10], 5′-NCCNC-3′, 5′-NCCNCNNA-3′, 5′-NCCCC-3′, 5′-NCCCCNNA-3′, 5′-NCCCCC-3′ [SEQ ID NO: 15], 5′-NCCCCCNA-3′ [SEQ ID NO: 16], 5′-NNCCC-3′, 5′-NNCCCNNA-3′, 5′-NNCCCC-3′, 5′-NNCCCCNA-3′, 5′-NNNCCC-3′, and 5′-NNNCCCNA-3′. The PAM sequence may be 5′-CNCCCCAC-3′ [SEQ ID NO: 17], 5′-CCCCCCAG-3′ [SEQ ID NO: 18], 5′-CCCCCCAA-3′ [SEQ ID NO: 11], 5′-CCCCCCAT-3′ [SEQ ID NO: 19], 5′-CCCCCCAC-3′ [SEQ ID NO: 20], 5′-ATCCCCAA-3′ [SEQ ID NO: 21], or 5′-ACGGCCAA-3′ [SEQ ID NO: 22]. Preferably the PAM sequence will be of the sequence 5′-NNNNCNNA-3′ [SEQ ID NO: 47]. However, it will be appreciated that other combinations of nucleotides may be used depending on the desired application and/or concentration of Cas protein or polypeptide. In particular, there is no specific preference for the for the first 4 PAM positions. The first 4 nucleotides can therefore conveniently be any nucleotide (NNNN). These sequences correspond to what is termed “protospacer adjacent motif” or “PAM” in the context of naturally occurring crRNAs. In type IIC CRISPR/Cas systems these PAM sequences facilitate stable interaction with the Cascade/crRNA complex with its dsDNA target, in order to ensure high degree of specificity of the crRNA—both in the natural system targets and therefore preferably also of the RNAs according to the present invention—for the target sequence. Preferably the sequence directly adjacent the protospacer will not be 5′-NNNCATN-3′.

Additionally, the PAM sequence may be of the sequence 5′-NNNNCNNA-3′ [SEQ ID NO: 47], for example 5′-NNNNCNAA-3′ [SEQ ID NO: 52], or 5′-NNNNCMCA-3′ [SEQ ID NO: 53].

One of the limitations of the mesophilic SpCas9 is that it only displays activity between 25 and 44° C.; above these temperatures SpCas9 activity rapidly decreases to undetectable levels (Mougiakos et al., 2017, ACS Synth Biol. 6: 849-861). In contrast to the 25-44° C. range of its mesophilic orthologue SpCas9, ThermoCas9 of the present invention is active in vitro in a much broader temperature range of 20-70° C. The extended activity and stability of ThermoCas9 allows for its application in molecular biology techniques that require DNA manipulation at temperatures of 20-70° C., as well as its exploitation in harsh environments that require robust enzymatic activity. ThermoCas9 may also therefore be used as a genome editing tool for both thermophilic and mesophilic organisms.

In addition to having a broad functional temperature activity range, that is, to be functional at both low and high temperatures, for example at both 20° C. and 70° C., or 20° C. and 65° C. or 25° C. and 65° C., the ability to manipulate the range of temperatures at which ThermoCas9 is capable of targeted cleavage or binding or at which targeted cleavage or binding takes place efficiently, by modifying structural features of ThermoCas9 or associated elements (such as, for example, the sgRNA or tracRNA), would enable a greater level of control to be exerted over nucleic acid sequence manipulation. However, until now little was known about the molecular determinants of Cas9 activity at particular temperatures.

The inventors have identified several factors that are important for conferring the thermostability of ThermoCas9, one of which is the PAM preferences of ThermoCas9. The PAM preferences of ThermoCas9 are very strict for activity in the lower part of the temperature range 30° C.), whereas more variety in the PAM is allowed for activity at the moderate to optimal temperatures (37° C. to 60° C.). As such, the PAM sequence may be altered to obtain the most efficient binding, cleavage, marking or modification of the target at a given temperature. This provides a great deal of flexibility in application of the ThermoCas9, depending on the particular application. For instance in some applications a very broad temperature range of target binding, cleavage, marking or modification may be desirable, for example 20° C. to 70° C., preferably 20° C. to 65° C. or 25° C. to 65° C. Binding, cleavage, marking or modification of a target sequence within such a broad temperature range may be achieved by utilizing a PAM sequence of 5′-NNNNCVAA-3′ [SEQ ID NO: 48]. Preferably, binding, cleavage, marking or modification of a target sequence within such a broad temperature range may be achieved by utilizing a PAM sequence of 5′-NNNNCSAA-3′ [SEQ ID NO: 49], for example 5′-NNNNCGAA-3′ [SEQ ID NO: 50] or 5′-NNNNCCAA-3′ [SEQ ID NO: 51]. There is no specific preference for the for the first 4 PAM positions. The first 4 nucleotides can therefore conveniently be any nucleotide (NNNN). Optionally, for example 5′-CCCCCGAA-3′ or 5′-CCCCCCAA-3′ [SEQ ID NO: 11].

Where binding, cleavage, marking or modification of the target is required at 30° C., e.g. 30° C. to 100° C., preferably in the range 30° C. to 70° C., 30° C. to 65° C., or 45° C. to 65° C. the PAM sequence may optimally be of the sequence 5′-NNNNCNAA-3′ [SEQ ID NO: 52] or 5′-NNNNCMCA-3′ [SEQ ID NO: 53]. There is no specific preference for the for the first 4 PAM positions. The first 4 nucleotides can therefore conveniently be any nucleotide (NNNN). Optionally, for example the PAM sequence may be 5′-CCCCCNAA-3′ or 5′-CCCCCMCA-3′. Optionally, for example the PAM sequence may be selected from 5′-CCCCCAAA-3′, 5′-CCCCCATA-3′, 5′-CCCCCAGA-3′, 5′-CCCCCACA-3′, 5′-CCCCCTAA-3′, 5′-CCCCCTTA-3′, 5′-CCCCCTGA-3′, 5′-CCCCCTCA-3′, 5′-CCCCCGAA-3′, 5′-CCCCCGTA-3′, 5′-CCCCCGGA-3′, 5′-CCCCCGCA-3′, 5′-CCCCCCAA-3′ [SEQ ID NO: 11], 5′-CCCCCCTA-3′, 5′-CCCCCCGA-3′, or 5′-CCCCCCCA-3′.

The PAM sequences of the invention provided herein comprise the sequences disclosed herein, for example as 6-mer, 7-mer or 8-mer sequences. The 6-mer, 7-mer or 8-mer sequences may begin directly 3′ of the protospacer sequence on the non-target strand, with no additional nucleic acids interspaced between the protospacer sequence, complimentary to that bound by the target RNA, and the 5′ end of the PAM sequence. However, it will be appreciated that there may be additional nucleic acids forming part of the PAM sequence at the 3′ end of the 6-mer, 7-mer or 8-mer sequences. Additionally or alternatively, the non-target strand may comprise additional nucleic acids 3′ of the PAM sequence.

A nucleoprotein complex of the invention may comprise a ribonucleoprotein complex of the invention and the target nucleic acid strand of nucleic acid, with which the ribonucleoprotein is associated.

### Binding, Cleavage, Marking and Modifying Temperatures

The temperature range, including optimal temperature range of the activity, for example nuclease activity, of the Cas proteins of the present invention is significantly higher than that of known Cas9 proteins. Also, the upper extent of the range in which it retains activity is much higher than that of known Cas9 proteins. A higher optimal temperature and functional range provides a significant advantage in genetic engineering at high temperatures and therefore, for example, in the editing of the genomes of thermophilic organisms, many of which have utility in a range of industrial, agricultural and pharmaceutical processes conducted at elevated temperatures. Thus the methods, uses, nucleoproteins and transformed cells of the invention may be useful in industrial processes, for example providing genome editing for metabolic engineering purposes. The presence of the PAM sequences of the invention, directly adjacent to the protospacer sequence in the non-target strand, improve the specificity of the Cas proteins and polypeptides for the target sequences, and support the use of the Cas proteins and polypeptides at higher temperatures and across larger functional temperature ranges.

In accordance with a significantly greater thermostability, Cas proteins of the present invention retain function, for example nuclease activity, across a much greater temperature range of than that of known Cas9 proteins. Also, the upper extent of the range in which it retains activity is much higher than that of known Cas9 proteins. A higher optimal temperature and functional range provides a significant advantage in genetic engineering at high temperatures and therefore, for example, in the editing of the genomes of thermophilic and mesophilic organisms, many of which have utility in a range of industrial, agricultural and pharmaceutical processes conducted at elevated temperatures. The extended activity and stability of ThermoCas9 allows for its application in molecular biology techniques that require DNA manipulation within a broad range of temperatures, for example 20-70° C., as well as its exploitation in harsh environments that require robust enzymatic activity. ThermoCas9 may also therefore be used as a genome editing tool for both thermophilic and mesophilic organisms.

Advantageously, the inventors have also shown that Cas proteins of the invention can also be used to direct transcriptional control of target sequences, for example silencing transcription by sequence-specific binding to target sequences. ThermoCas9 may also therefore be used as a transcriptional control tool in both thermophilic and mesophilic organisms, for example in silencing or activating transcription of target genes. ThermoCas9 may also therefore be used as a gene-silencing tool in both thermophilic and mesophilic organisms.

Advantageously, Cas proteins or polypeptides of the invention are capable of nucleic acid binding, cleavage, marking or modifying at a temperature from 20° C. to 100° C. but are particularly useful at elevated temperatures, for example at a temperature between 41° C. and 122° C., preferably at a temperature between 50° C. and 100° C. Cas proteins and polypeptides of the invention are capable of binding, cleaving, marking or modifying DNA, RNA and synthetic nucleic acids. Cas proteins or polypeptides of the invention may also provide operability for nuclease activity, gene editing and nucleic acid marking applications at temperatures in the range 20 to 50° C., for example.

Where a temperature range is included herein, it is intended that the endpoints are included in the disclosed temperature range, i.e. that the range is “inclusive”. For example, where it is stated that there is activity at a temperature in the range between 20° C. and 100° C., the temperatures of 20° C. and 100° C. are included in said range.

Preferably, Cas proteins or polypeptides of the invention, when associated with suitable gRNA (guide RNA, also called targeting RNA molecule) which recognizes a target sequence in the polynucleotide molecule(s) to be bound, cleaved, marked or modified, does so at temperatures in the range 20° C. to 100° C., optionally in the range 20° C. to 70° C., 20° C. to 65° C., 25° C. to 70° C., 25° C. to 65° C., 55° C. to 100° C., 50° C. to 70° C., 55° C. to 70° C., or 55° C. to 65° C.

Preferably, Cas proteins or polypeptides of the invention, when associated with suitable gRNA (guide RNA, also called targeting RNA molecule) which recognizes a target sequence in the polynucleotide molecule(s) to be bound, cleaved, marked or modified, does so at temperatures in the range 50° C. to 100° C., optionally in the range 55° C. to 100° C., 60° C. to 100° C., 65° C. to 100° C., 70° C. to 100° C., 75° C. to 100° C., 80° C. to 100° C., 85° C. to 100° C., 90° C. to 100° C., 95° C. to 100° C. More preferably, Cas proteins of the invention cleave, mark or modify nucleic acids at temperatures in the range 51° C. to 99° C., 52° C. to 98° C., 53° C. to 97° C., 54° C. to 96° C., 55° C. to 95° C., 56° C. to 94° C., 57° C. to 93° C., 58° C. to 92° C., 59° C. to 91° C. 60° C. to 90° C., 61° C. to 89° C., 62° C. to 88° C., 63° C. to 87° C., 64° C. to 86° C., 65° C. to 85° C., 66° C. to 84° C., 67° C. to 83° C., 68° C. to 82° C., 69° C. to 81° C., 70° C. to 80° C., 71° C. to 79° C., 72° C. to 78° C., 73° C. to 77° C., 74° C. to 76° C., or at a temperature of 75° C. Preferably, Cas proteins of the invention bind, cleave, mark or modify nucleic acids at temperatures in the range 60° C. to 80° C., 61° C. to 79° C., 62° C. to 78° C., 63° C. to 77° C., 64° C. to 76° C., 60° C. to 75° C., 60° C. to 70° C. Optimally Cas proteins of the invention bind, cleave, mark or modify nucleic acids at temperatures in the range 60° C. to 65° C., preferably at 65° C.

Target RNA molecules may be designed for use with the Cas proteins and polypeptides of the invention, wherein the target RNA molecules bind to the target sequence in a target strand, and the non-target strand further comprises a PAM sequence provided herein immediately 3′ of the protospacer sequence. The PAM sequence may comprise 5′-NNNNNNNA-3′, preferably 5′-NNNNCNNA-3′ [SEQ ID NO: 47], optionally, for example 5′-CCCCCCNA-3′ [SEQ ID NO: 10] or 5′-CCCCCCAA-3′ [SEQ ID NO: 11], and the uses, methods, transformed cells, and nucleoproteins of the invention may provide binding, cleaving, marking and/or modifying of the target strand across the temperature range of from 55° C. to 65° C., preferably across the temperature range of from 50° C. to 70° C., from 40° C. to 65° C., from 45° C. to 75° C., from 37° C. to 78° C. and/or from 20° C. to 80° C.

The PAM sequence may be altered to obtain the most efficient cleavage of the target at a given temperature. This provides a great deal of flexibility in application of Cas proteins of the present invention, depending on the particular application. Where binding, cleavage, marking or modifying activity, for example cleavage activity is required within a temperature range of 20° C. to 100° C., preferably 20° C. to 70° C., or 20° C. to 65° C. or 25° C. to 65° C., then activity may be achieved by utilizing a PAM sequence of 5′-NNNNCVAA-3′ [SEQ ID NO: 48], preferably, activity within such a temperature range may be achieved by utilizing a PAM sequence of 5′-NNNNCSAA-3′ [SEQ ID NO: 49], for example 5′-NNNNCGAA-3′ [SEQ ID NO: 50] or 5′-NNNNCCAA-3′ [SEQ ID NO: 51]. Optionally, for example 5′-CCCCCGAA-3′ [SEQ ID NO: 52] or 5′-CCCCCCAA-3′ [SEQ ID NO: 11].

The inventors have found that thermostability of ThermoCas9 increases along with association of a guide (sgRNA) to form a ribonucleoprotein complex. The guide (sgRNA) may suitably comprise a tracrRNA and a crRNA. In such an arrangement, the guide may suitably comprise a crRNA which comprises a nucleotide spacer-fragment and repeat-fragment. The crRNA may suitably be 17-20 nt in length. Optionally, the crRNA may be 17 nt in length. Alternatively, the crRNA may be 18 nt in length, 19 nt in length or 20 nt in length. The guide may also comprise a tracrRNA (anti-repeat fragment (that base pairs with repeat fragment of crRNA)). The tracrRNA and crRNA can be separated by a synthetic linker. The following guide represents a preferred arrangement: 5′-[crRNA (17-20 nucleotide spacer-fragment & repeat-fragment)—(optional: synthetic loop to link the two RNAs)—tracrRNA (anti-repeat fragment (that base pairs with repeat fragment of crRNA) & some variable stem-loop structures (as to which see below), that may be truncated to some extent in some systems)]-3′.

Usually, the tracrRNA will be provided as part of a chimeric single-guide RNA (sgRNA), for example comprising a crRNA and a tracrRNA. The tracrRNA may consist of an anti-repeat region followed by one or more hairpin structures, preferably two or more hairpin structures or more preferably three or more hairpin structures. The presence of the full-length repeat/anti-repeat hairpin (formed by the 3′-end of the crRNA part (repeat) of the and the 5′-end of the complementary tracrRNA part (anti-repeat) in a synthetic sgRNA chimera fused by a 4-nucleotide linker, e.g. 5′-GAAA-3′)) at the spacer distal end functions as an anchor to the nuclease, but is not essential to target selection and cleavage activity. For example deletions at the spacer distal end of up to 50-nt long deletion of the tracrRNA part can be tolerated with little to no effect on the DNA cleavage efficiency. Accordingly, for example a deletion of the spacer distal end of the full-length repeat-anti-repeat hairpin may be made up to 50 nt, up to 45 nt, up to 40 nt, up to 35 nt, up to 30 nt, up to 25 nt, up to 20 nt, up to 15 nt, up to 10 nt, or up to 5 nt, without compromise in terms of target DNA cleavage efficiency.

Surprisingly, the inventors have also found that the structure of the tracrRNA influences thermostability of the ThermoCas9 and efficiency of activity, in particular cleavage activity. Specifically, the number of hairpin (or stem-loop) structures in the tracrRNA or the sgRNA can be modified in order to obtain the most efficient binding, cleavage, marking or modifying of the target at a given temperature. This provides a great deal of flexibility in application of Cas proteins of the present invention, depending on the particular application. Optionally, the tracrRNA or the sgRNA may be provided with a nucleic acid sequence which is capable of forming one or more stem-loop structures, two or more stem-loop structures or three or more stem-loop structures. Optionally, the tracrRNA or the sgRNA may be provided with a nucleic acid sequence which is arranged to form one or more stem-loop structures, two or more stem-loop structures or three or more stem-loop structures. Preferably, the sgRNA will be provided with a nucleic acid sequence which is capable of forming at least three stem-loop structures.

Optionally where binding, cleavage, marking or modifying activity, for example cleavage activity is required within a temperature range of 20° C. to 60° C., preferably 37° C. to 60° C., or 37° C., 40° C., 45° C., 50° C., 55° C. or 60° C. then activity may be achieved by utilizing a sgRNA sequence which is capable of forming one or more stem-loop structures.

Optionally where binding, cleavage, marking or modifying activity, for example cleavage activity is required within a temperature range of 20° C. to 65° C., preferably 37° C. to 65° C., more preferably 45° C. to 55° C. or 37° C., 40° C., 45° C., 50° C., 55° C. or 60° C. then activity may be achieved by utilizing a sgRNA sequence which is capable of forming two or more stem-loop structures.

Optionally where binding, cleavage, marking or modifying activity, for example cleavage activity is required within a temperature range of 20° C. to 100° C., preferably 20° C. to 70° C., more preferably 37° C. to 65° C. or 37° C., 40° C., 45° C., 50° C., 55° C., 60° C. or 65° C. then activity may be achieved by utilizing a sgRNA sequence which is capable of forming three or more stem-loop structures.

Preferably, the portion of the sgRNA corresponding to the tracrRNA will comprise the sequence; AAGGGCUUUCUGCCUAUAGGCAGACUGCCC [SEQ ID NO: 54] which exemplifies the 5′ hairpin. Preferably, the portion of the sgRNA corresponding to the tracrRNA will further comprise the sequence; GUGGCGUUGGGGAUCGCCUAUCGCC [SEQ ID NO: 55], which exemplifies the ‘middle’ hairpin. Preferably, the portion of the sgRNA corresponding to the tracrRNA will further comprise the sequence; CGCUUUCUUCGGGCAUUCCCCACUCUUAGGCGUUUU [SEQ ID NO: 56], which exemplifies the 3′ hairpin.

Preferably, the portion of the sgRNA corresponding to the tracrRNA will comprise the sequence;

AAGGGCUUUCUGCCUAUAGGCAGACUGCCCGUGGCGUUGGGGAUCGCCUAUCGCC [SEQ ID NO: 57] i.e. including the 5′ hairpin and the middle hairpin.

Preferably, the portion of the sgRNA corresponding to the tracrRNA may comprise the sequence;

AAGGGCUUUCUGCCUAUAGGCAGACUGCCCGUGGCGUUGGGGAUCGCCUAUCGCCC GCUUUCUUCGGGCAUUCCCCACUCUUAGGCGUUUU [SEQ ID NO: 58] i.e. including the 5′ hairpin, the middle hairpin and the 3′ hairpin.

The inventors have discovered that the number of predicted stem-loops of the tracrRNA scaffold plays a crucial role in DNA cleavage, in particular at elevated temperatures. They have determined that, although the presence of three stem-loops of the tracrRNA scaffold is not essential for cleavage activity, when all three loops are present, the cleavage is most efficient at all temperatures in the range indicating that a full length tracrRNA is required for optimal ThermoCas9-based DNA cleavage at elevated temperatures. In contrast, removal of the 3′ hairpin results in a decrease in efficiency of cleavage. Moreover, the inventors found that removal of both the middle and the 3′ hairpins, results in a drastically decline in the cleavage efficiency of ThermoCas9, particularly at the upper and lower extremes of the functional temperature ranges. Preferably, where binding, cleavage, marking or modification of a target sequence is required at elevated temperatures, for example 45° C. to 100° C., 50° C. to 100° C., 50° C. to 70° C., 50° C. to 65° C., 55° C. to 65° C. or within a broad temperature range such as 20° C. to 100° C., 20° C. to 70° C., 20° C. to 65° C. Preferably, ThermoCas9 associated with a sgRNA with three stem-loop structures will remain stable and capable of binding, cleavage, marking or modification of a target sequence for at least 1 min, at least 2 min, at least 3 min, at least 4 min or at least 5 min, preferably 5 min at a selected temperature in the range 20° C. to 100° C., 20° C. to 70° C., 20° C. to 65° C., 45° C. to 100° C., 50° C. to 100° C., 50° C. to 70° C., 50° C. to 65° C. or 55° C. to 65° C.

Additionally, the inventors have also discovered that the length of the spacer sequence of the sgRNA can be varied in order to manipulate the efficiency of ThermoCas9 activity, for example binding, cleavage, marking or modifying activity. Typically, the spacer sequence will be in the range 18 nt to 25 nt in length. Optionally the spacer sequence will be 18 nt, 19 nt, 20 nt, 21 nt, 22 nt, 23 nt, 24 nt or 25 nt in length. Preferably, spacer lengths of 19 nt, 20 nt, 21 nt or 23 nt will be used, since Cas9 proteins of the invention cleave target sequences with the highest efficiency when associated with sgRNAs with these spacer lengths. The cleavage efficiency drops significantly when a spacer of 18 nt is used. Preferably, the length of the spacer will be 23 nt.

In all aspects of the invention, Cas proteins or polypeptides may be obtained or derived from bacteria, archaea or viruses; or alternatively may be synthesised de novo. In preferred embodiments, a Cas protein or polypeptide of the invention is derived from a thermophilic prokaryotic organism, which may be classified as an archaea or bacterium, but is preferably a bacterium. More preferably a Cas protein or polypeptide of the invention will be derived from a thermophilic bacterium. Herein, the term thermophilic is to be understood as meaning capable of survival and growth at relatively high temperatures, for example in the context of the invention, capable of nucleic acid cleavage, binding or modification at a temperature between 41 and 122° C. (106 and 252° F.). Preferably a Cas protein or polypeptide of the invention may be isolated from one or more thermophilic bacteria and will function above 60° C.

Preferably a Cas protein or polypeptide of the invention may be isolated from one or more thermophilic bacteria and will function in the range 60° C. to 80° C. and optimally between 60° C. and 65° C. In preferred embodiments, a Cas protein or polypeptide of the invention is derived from Geobacillus sp. More preferably, a Cas protein of the invention is derived from Geobacillus thermodenitrificans. Even more preferably, a Cas protein of the invention is derived from Geobacillus thermodenitrificans T12. A Cas protein or polypeptide of the invention may be derived from a virus.

### Functional Moieties

Advantageously, the ability of Cas proteins, polypeptides and ribonucleoprotein complexes of the invention to target any polynucleotide sequence in a sequence-specific manner may be exploited in order to modify the target nucleic acid in some way, for example by cleaving it and/or marking it and/or modifying it. It will therefore be appreciated that additional proteins may be provided along with the Cas protein or polypeptide to achieve this. Accordingly, the Cas proteins or polypeptides of the invention may further comprise at least one functional moiety and/or the Cas proteins, polypeptides or ribonucleoprotein complexes of the present invention may be provided as part of a protein complex comprising at least one further protein. In a preferred aspect the present invention provides a Cas protein, polypeptide or a ribonucleoprotein complex wherein the Cas protein or at least one further protein further comprises at least one functional moiety. The at least one functional moiety may be fused or linked to the Cas protein. Preferably, the at least one functional moiety may be translationally fused to the Cas protein through expression in natural or artificial protein expression systems. Alternatively, the at least one functional moiety may be covalently linked by a chemical synthesis step to the Cas protein. Preferably, the at least one functional moiety is fused or linked to the N-terminus and/or the C-terminus of the Cas protein; preferably the C-terminus.

Desirably, the at least one functional moiety will be a protein. It may be a heterologous protein or alternatively may be native to the bacterial species from which the Cas protein was derived. The at least one functional moiety may be a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag.

In a particularly preferred aspect, the present invention provides a Cas protein, polypeptide, or a ribonucleoprotein complex, wherein the at least one functional moiety is a marker protein, for example GFP.

### Nuclease Activity

A Cas ribonucleoprotein of the invention has nucleic acid binding, cleavage, marking or modification activity at a temperature, preferably an elevated temperature, disclosed herein, for example at a temperature between 50° C. and 100° C. The ribonucleoproteins of the invention may be capable of binding, cleaving, marking or modifying DNA, RNA or synthetic nucleic acids. In preferred aspects Cas ribonucleoproteins of the invention are capable of cleaving DNA in a sequence-specific manner, in particular double-stranded DNA.

Cas proteins, polypeptides or ribonucleoproteins of the invention may have more than one nuclease domain. Site-specific nucleases can permit the generation of double strand breaks (DSBs) at selected positions along a strand of DNA. In a target host cell, this enables DSBs to be made at specific pre-selected positions in the genome. The creation of such breaks by site-specific nucleases prompts the endogenous cellular repair machinery to be repurposed in order to insert, delete or modify DNA at desired positions in the genome of interest.

One or more nuclease activity sites of the protein or polypeptide molecule may be inactivated, e.g. so as to allow the activity of another functional moiety linked or fused to the protein or polypeptide, e.g. a nuclease domain such as Fok1 nuclease.

Therefore notwithstanding the fact that the Cas proteins, polypeptides and ribonucleoproteins of the invention may have endogenous nuclease activity, for certain applications it may be desirable to inactivate the native nuclease activity of the Cas protein and provide a Cas protein or a ribonucleoprotein complex wherein the native Cas9 nuclease activity is inactivated and the Cas protein is linked to at least one functional moiety. Reducing the incidence of mis-targeting events by complementation of the native Cas9 nuclease activity is one such application. This may desirably be achieved by inactivation of the native Cas9 nuclease activity of the Cas protein or ribonucleoprotein complex and provision of a heterologous nuclease, preferably fused to the Cas protein. Accordingly, the present invention provides a Cas protein or a ribonucleoprotein complex, wherein the at least one functional moiety is a nuclease domain, preferably a FokI nuclease domain. In a particularly preferred aspect, the Cas protein or ribonucleoprotein complex of the invention fused to a FokI nuclease domain is provided as part of a protein complex, preferably comprising another Cas protein or ribonucleoprotein complex of the invention fused to a FokI nuclease domain and wherein the two complexes target opposite strands of the target genomic DNA.

For some applications it may be desirable to completely attenuate the nuclease activity of the Cas protein, polypeptide or ribonucleoprotein, for example in applications where the Cas protein or ribonucleoprotein complex is utilised to recognise and modify a specific target sequence in a nucleic acid, for instance to mark it as part of a diagnostic test. In such applications, the nuclease activity of the Cas protein may be inactivated and the functional moiety fused to the Cas protein may be a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag.

In a preferred aspect, a catalytically inactive, or “dead” Cas protein or polypeptide (dCas) lacking nuclease activity may be bound to a target nucleic acid sequence and thereby sterically repress activity of that sequence. For example, a target RNA may be designed that is complementary to a promoter or exonic sequence of a gene, so that binding of the dCas and target RNA to the gene sterically represses transcriptional initiation or elongation of the gene sequence, thereby repressing expression of the gene. Alternatively, the methods and uses described herein can use modified nuclease variants of gtCas9 that are nickases. A nickase can be created via a mutation in either one of the HNH or the RuvC catalytic domains of the gtCas9 nuclease. This has been shown for S. pyogenes Cas9 (spCas) with spCas9-mutants D10A and H840A, which have an inactive RuvC or HNH nuclease domain, respectively. The combination of these two mutations leads to a catalytically dead Cas9 variant (Standage-Beier, K. et al., 2015, ACS Synth. Biol. 4, 1217-1225; Jinek, M. et al., 2012, Science 337, 816-821; Xu, T. et al., 2015, Appl. Environ. Microbiol. 81, 4423-4431). Based on sequence homology (FIG. 3), these residues can be D8 (D17 in FIG. 3) and D581 or H582 (FIG. 3) in gtCas9.

Preferably, the mutations D8A and H582A in gtCas9 (ThermoCas9) can be used to create a catalytically inactive, or “dead” Cas protein or polypeptide variant of ThermoCas9 (dCas) which lacks nuclease activity. Such a dCas may usefully find application as, for example, an efficient thermoactive transcriptional silencing CRISPRi tool, being able to steadily and specifically bind to DNA elements without introducing dsDNA breaks. Advantageously, such a system could, amongst other things, greatly facilitate metabolic studies of thermophiles.

In a particularly preferred aspect, the present invention provides a Cas protein or a ribonucleoprotein complex, wherein the nuclease activity of the Cas protein is inactivated and the at least one functional moiety is a marker protein, for example GFP. In this way it may be possible to specifically target a nucleic acid sequence of interest and to visualize it using a marker which generates an optical signal. Suitable markers may include for example, a fluorescent reporter protein, e.g. Green Fluorescent Protein (GFP), Yellow Fluorescent Protein (YFP), Red Fluorescent Protein (RFP), Cyan Fluorescent Protein (CFP) or mCherry. Such a fluorescent reporter gene provides a suitable marker for visualisation of protein expression since its expression can be simply and directly assayed by fluorescence measurement. Alternatively, the reporter nucleic acid may encode a luminescent protein, such as a luciferase (e.g. firefly luciferase). Alternatively, the reporter gene may be a chromogenic enzyme which can be used to generate an optical signal, e.g. a chromogenic enzyme (such as beta-galactosidase (LacZ) or beta-glucuronidase (Gus)). Reporters used for measurement of expression may also be antigen peptide tags. Other reporters or markers are known in the art, and they may be used as appropriate.

Because the marker may be visualized, in certain embodiments where the target nucleic acid is RNA, specifically mRNA, it may be possible to quantify the transcriptional activity of a gene by detection and quantification of the optical signal provided by the marker, particularly where the optical signal generated by the marker is directly proportionate to the quantity of the expression product. Therefore in preferred embodiments of the invention, Cas proteins or ribonucleoproteins of the invention may be used to assay expression products of a gene of interest.

In one aspect, the gtCas9 described herein may be used in a homologous recombination (HR) mediated genome modification method in microbial cells. Such methods involve HR and site-directed gtCas9 activity, whereby counter selection occurs by the gtCas9 activity removing microbes which do not have a desired modification introduced by HR.

Thus the methods and uses provided herein allow the process of homologous recombination to be favoured during a first step such that the microbial genome can be modified with the desired mutation and a second step in which unmodified cells can be targeted by the gtCas9 ribonuclease complex to introduce a DSDB into the genomes of the unmodified cells. Due to an absence of an efficient non-homologous end joining (NHEJ) repair mechanism in the majority of microbes, DSDB typically leads to cell death. Thus, these methods and uses increase overall the population of microbial cells with the desired mutation whilst eliminating any unmodified microbial cells. Preferably, such methods and uses are used in microbes that have substantially no endogenous NHEJ repair mechanism. Alternatively, the methods and uses may be applied to microbes that have an endogenous NHEJ repair mechanism. The methods and uses described herein may be applied to microbes that have an endogenous NHEJ repair mechanism but wherein the NHEJ repair mechanism is either conditionally reduced or the NHEJ activity is knocked out.

The methods and uses provided herein may utilise a sequence of the homologous recombination polynucleotide that has at least one mis-match with the guide RNA, such that the guide RNA is no longer able to recognise the modified genome. This means that the gtCas9 ribonuclease complex will not recognise the modified genome. Therefore, no DSDB can be introduced by the gtCas9 ribonuclease complex and so the modified cells will survive. However, the cells with unmodified genomes will still have substantial complementarity to the guide RNA and consequently can be cleaved site-specifically by the gtCas9 ribonuclease complex.

In another aspect of the methods and uses of the invention, the way in which the gtCas9 ribonucleoase complex is prevented from acting to cleave the microbial genome is not so much to modify or eliminate the sequence targeted by the guide, but rather the PAM required by the gtCas9 ribonuclease complex. The PAM is either modified or eliminated in order to blind the gtCas9 ribonuclease complex to the specific cutting site. Therefore, methods and uses of the invention may include those using a sequence of the homologous recombination polynucleotide that does not include a PAM sequence recognised by the gtCas9 ribonuclease complex. Therefore, no DSDB can be introduced by the gtCas9 ribonuclease complex and so the HR modified cells will survive. However, the unmodified cells will still be recognised by the gtCas9 ribonuclease complex and its guide and so consequently are cleaved site-specifically.

Thus methods and uses are provided herein that rely on HR to modify the genome of the microbe. Preferably, the upstream flank and downstream flanks are 0.5 kilobases (kb) to 1.0 kb each in length. However, recombination using larger or shorter fragments is possible as well. The homologous recombination polynucleotide may further comprise a polynucleotide sequence between the upstream and downstream flanking regions. This polynucleotide sequence could for example contain a modification that is to be introduced into the microbial genome.

Whilst homologous recombination relies upon the upstream and downstream flanks having substantial complementarity to the target regions, mismatches can be accommodated as well. Therefore, in some embodiments, homologous recombination is known to occur between DNA segments with extensive homology to the upstream and downstream flanks. In alternative embodiments, the upstream and downstream flanks have complete complementarity to the target regions. The upstream and downstream flanks need not be identical in size. However, in some instances the upstream and downstream flanks are identical in size. The efficiency of homologous recombination will vary depending on the likelihood of homologous recombination of the smallest fragment length of the flank. However, even if the homologous recombination process is inefficient, advantageously the method described herein will select for any microbial cell that has the desired modification over the unmodified microbial cell. Homologous recombination also allows large deletions (e.g. 50 kb or more) to be made encompassing complete gene clusters. Homologous recombination is also used for recombineering, which is a well-known method to allow for recombination over smaller fragments (45-100 nt). The methods and uses described herein can optionally further comprise at least another homologous recombination polynucleotide or a polynucleotide comprising a sequence encoding a homologous recombination polynucleotide having a sequence substantially complementary to a second target region containing the target in the microbial genome.

In preferred embodiments, the methods and uses described herein utilise a homologous recombination polynucleotide that is DNA. In some embodiments the DNA is single stranded.

In other embodiments, the DNA is double stranded. In further embodiments, the DNA is double stranded and plasmid borne.

HR in the methods and uses provided herein may be used to remove a polynucleotide sequence from the microbial genome. Alternatively, HR in the methods and uses provided herein may be used to insert one or more gene(s), or fragment(s) thereof, in to the microbial genome. As a further alternative, HR in the methods and uses provided herein may be used to modify or replace at least one nucleotide in the microbial genome. Consequently, the methods and uses provided herein may be used for any desired kind of genome modification.

Alternatively, the gtCas9 described herein may be used in a HR mediated genome modification method in microbial cells, whereby the gtCas9 activity introduces DSDB and can induce cellular HR in microbial cells, as has been shown for spCas9 (Jiang et al. (2013) Nature Biotech, 31, 233-239; Xu et al. (2015) Appl Environ Microbiol, 81, 4423-4431; Huang et al. (2015) Acta Biochimica et Biophysica Sinica, 47, 231-243).

Alternatively, homologous recombination may be facilitated through recombineering, e.g., by introducing an oligonucleotide into a microbial cell expressing a gene coding for RecT or beta protein as reviewed by Mougiakos et al. ((2016), Trends Biotechnol. 34: 575-587). In a further embodiment, the Cas9 can be combined with Multiplex Automated Genome Engineering (MAGE) as exemplified by Ronda et al. ((2016), Sci. Rep. 6: 19452.)

Throughout, the reference sequences of the Cas proteins of the invention may be defined as a nucleotide sequence encoding the amino acid sequence. For example the amino acid sequence of the motifs defined in SEQ ID's 2 to 6 also includes all nucleic acid sequences which encode that amino acid sequence.

Accordingly, the present invention also provides an isolated nucleic acid molecule encoding a Cas protein comprising;


- - a. the amino acid motif EKDGKYYC \[SEQ ID NO: 2\]; and/or
  - b. the amino acid motif X₁X₂CTX₃X₄ \[SEQ ID NO: 3\] wherein X₁ is
    independently selected from Isoleucine, Methionine or Proline, X₂ is
    independently selected from Valine, Serine, Asparagine or
    Isoleucine, X₃ is independently selected from Glutamate or Lysine
    and X₄ is one of Alanine, Glutamate or Arginine; and/or
  - c. the amino acid motif X₅LKX₆IE \[SEQ ID NO: 4\] wherein X₅ is
    independently selected from Methionine or Phenylalanine and X₆ is
    independently selected from Histidine or Asparagine; and/or
  - d. the amino acid motif X₇VYSX₈K \[SEQ ID NO: 5\] wherein X₇ is
    Glutamate or Isoleucine and X₈ is one of Tryptophan, Serine or
    Lysine; and/or
  - e. the amino acid motif X₉FYX₁₀X₁₁REQX₁₂KEX₁₃ \[SEQ ID NO: 6\]
    wherein X₉ is Alanine or Glutamate, X₁₀ is Glutamine or Lysine, X₁₁
    is Arginine or Alanine, X₁₂ is Asparagine or Alanine and X₁₃ is
    Lysine or Serine;  
    wherein the Cas protein is capable of DNA binding, cleavage, marking
    or modification between 50° C. and 100° C. when associated with at
    least one targeting RNA molecule, and a polynucleotide comprising a
    target nucleic acid sequence recognised by the targeting RNA
    molecule.

In another aspect the present invention also provides an isolated nucleic acid molecule encoding a clustered regularly interspaced short palindromic repeat (CRISPR)-associated (Cas) protein having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith.

In another aspect the present invention also provides an isolated nucleic acid molecule, further comprising at least one nucleic acid sequence encoding a peptide which upon translation is fused to the Cas protein.

In another aspect the present invention also provides an isolated nucleic acid molecule, wherein the at least one nucleic acid sequence fused to the nucleic acid molecule encoding the Cas protein encodes a protein selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)-activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag.

**ThermoCas9 Nuclease Activity: Divalent Cations**

Previously characterized, mesophilic Cas9 endonucleases employ divalent cations to catalyze the generation of DSBs in target DNA. The inventors have shown that ThermoCas9 can mediate dsDNA cleavage in the presence of any of the following divalent cations: Mg2+, Ca2+, Mn2+, Co2+, Ni2+, and Cu2+.

**ThermoCas9 Nuclease Activity: Substrates**

The inventors have also surprisingly shown that despite reports that certain type-IIC systems were efficient single stranded DNA cutters ((Ma, et al., Mol. Cell 60, 398-407 (2015); Zhang, et al., Mol. Cell 60, 242-255 (2015)), ThermoCas9 cannot direct cleavage of ssDNA. The nuclease activity of ThermoCas9 is limited to dsDNA substrates.

## Expression Vectors

Nucleic acids of the present invention may be isolated. However, in order that expression of the nucleic acid sensing construct may be carried out in a chosen cell, the polynucleotide sequence encoding the Cas protein or ribonucleoprotein will preferably be provided in an expression construct. In some embodiments, the polynucleotide encoding the Cas protein or ribonucleoprotein will be provided as part of a suitable expression vector. In certain embodiments an expression vector of the present invention (with or without nucleotide sequence encoding amino acid residues which on expression will be fused to a Cas protein) may further comprise a nucleotide sequence encoding a targeting RNA molecule as hereinbefore defined. Consequently, such expression vectors can be used in an appropriate host to generate a ribonucleoprotein complex of the invention which can target a desired nucleotide sequence. Alternatively, nucleotide sequences encoding a targeting RNA molecule as hereinbefore defined may be provided in a separate expression vector or alternatively may be delivered to a target cell by other means.

Suitable expression vectors will vary according to the recipient cell and suitably may incorporate regulatory elements which enable expression in the target cell and preferably which facilitate high-levels of expression. Such regulatory sequences may be capable of influencing transcription or translation of a gene or gene product, for example in terms of initiation, accuracy, rate, stability, downstream processing and mobility.

Such elements may include, for example, strong and/or constitutive promoters, 5′ and 3′ UTR's, transcriptional and/or translational enhancers, transcription factor or protein binding sequences, start sites and termination sequences, ribosome binding sites, recombination sites, polyadenylation sequences, sense or antisense sequences, sequences ensuring correct initiation of transcription and optionally poly-A signals ensuring termination of transcription and transcript stabilisation in the host cell. The regulatory sequences may be plant-, animal-, bacteria-, fungal- or virus derived, and preferably may be derived from the same organism as the host cell. Clearly, appropriate regulatory elements will vary according to the host cell of interest. For example, regulatory elements which facilitate high-level expression in prokaryotic host cells such as in E. coli may include the pLac, T7, P(Bla), P(Cat), P(Kat), trp or tac promoters. Regulatory elements which facilitate high-level expression in eukaryotic host cells might include the AOX1 or GAL1 promoter in yeast or the CMV- or SV40-promoters, CMV-enhancer, SV40-enhancer, Herpes simplex virus VIP16 transcriptional activator or inclusion of a globin intron in animal cells. In plants, constitutive high-level expression may be obtained using, for example, the Zea mays ubiquitin 1 promoter or 35S and 19S promoters of cauliflower mosaic virus.

Suitable regulatory elements may be constitutive, whereby they direct expression under most environmental conditions or developmental stages, developmental stage specific or inducible. Preferably, the promoter is inducible, to direct expression in response to environmental, chemical or developmental cues, such as temperature, light, chemicals, drought, and other stimuli. Suitably, promoters may be chosen which allow expression of the protein of interest at particular developmental stages or in response to extra- or intra-cellular conditions, signals or externally applied stimuli. For example, a range of promoters exist for use in E. coli which give high-level expression at particular stages of growth (e.g. osmY stationary phase promoter) or in response to particular stimuli (e.g. HtpG Heat Shock Promoter).

Suitable expression vectors may comprise additional sequences encoding selectable markers which allow for the selection of said vector in a suitable host cell and/or under particular conditions.

The invention also includes a method of modifying a target nucleic acid in a cell, comprising transfecting, transforming or transducing the cell with any of the expression vectors as hereinbefore described. The methods of transfection, transformation or transduction are of the types well known to a person of skill in the art. Where there is one expression vector used to generate expression of a ribonucleoprotein complex of the invention and when the targeting RNA is added directly to the cell then the same or a different method of transfection, transformation or transduction may be used. Similarly, when there is one expression vector being used to generate expression of a ribonucleoprotein complex of the invention and when another expression vector is being used to generate the targeting RNA in situ via expression, then the same or a different method of transfection, transformation or transduction may be used.

In other embodiments, mRNA encoding the Cas protein or polypeptide is introduced into a cell so that the Cascade complex is expressed in the cell. The targeting RNA which guides the Cas protein complex to the desired target sequence is also introduced into the cell, whether simultaneously, separately or sequentially from the mRNA, such that the necessary ribonucleoprotein complex is formed in the cell.

Accordingly, the invention also provides a method of modifying, i.e. cleaving, tagging, modifying, marking or binding, a target nucleic acid comprising contacting the nucleic acid with a ribonucleoprotein complex as hereinbefore defined.

In addition, the invention also includes a method of modifying a target nucleic acid comprising contacting the nucleic acid with a Cas protein or polypeptide as hereinbefore defined, in addition to a targeting RNA molecule as hereinbefore defined.

In accordance with the above methods, modification of target nucleic acid may therefore be carried out in vitro and in a cell-free environment. In a cell-free environment, addition of each of the target nucleic acid, the Cas protein and the targeting RNA molecule may be simultaneous, sequential (in any order as desired), or separately. Thus it is possible for the target nucleic acid and targeting RNA to be added simultaneously to a reaction mix and then the Cas protein or polypeptide of the invention to be added separately at a later stage.

Equally, the modification of the target nucleic acid may be made in vivo, that is in situ in a cell, whether an isolated cell or as part of a multicellular tissue, organ or organism. In the context of whole tissue and organs, and in the context of an organism, the method may desirably be carried out in vivo or alternatively may be carried out by isolating a cell from the whole tissue, organ or organism, treating the cell with ribonucleoprotein complex in accordance with the method and subsequently returning the cell treated with ribonucleoprotein complex to its former location, or a different location, whether within the same or a different organism.

In these embodiments, the ribonucleoprotein complex or the Cas protein or polypeptide requires an appropriate form of delivery into the cell. Such suitable delivery systems and methods are well known to persons skilled in the art, and include but are not limited to cytoplasmic or nuclear microinjection. In preferred modes of delivery, an Adeno-associated virus (AAV) is used; this delivery system is not disease causing in humans and has been approved for clinical use in Europe.

Accordingly the present invention provides a method of modifying a target nucleic acid comprising contacting the nucleic acid with:

a. a ribonucleoprotein complex as hereinbefore defined; or

b. a protein or protein complex as hereinbefore defined and an RNA molecule as hereinbefore defined.

In a further aspect the present invention provides a method of modifying a target nucleic acid in a cell, comprising transforming, transfecting or transducing the cell with an expression vector comprising nucleotide sequences encoding a ribonucleoprotein complex as hereinbefore defined; or alternatively transforming, transfecting or transducing the cell with an expression vector comprising nucleotide sequences encoding a protein or protein complex as hereinbefore defined and a further expression vector comprising a nucleotide sequence encoding a targeting RNA molecule as hereinbefore defined.

In a further aspect, the present invention provides a method of modifying a target nucleic acid in a cell comprising transforming, transfecting or transducing the cell with an expression vector comprising nucleotide sequences encoding a protein or protein complex as hereinbefore defined, and then delivering a targeting RNA molecule as hereinbefore defined into the cell.

In embodiments where the guide (i.e. targeting) RNA (gRNA) molecule and the Cas protein or polypeptide are provided separately rather than as part of a ribonucleoprotein complex, the gRNA molecule requires an appropriate form of delivery into a cell, whether simultaneously, separately or sequentially with the Cas protein or protein complex. Such forms of introducing RNA into cells are well known to a person of skill in the art and may include in vitro or ex vivo delivery via conventional transfection methods. Physical methods, such as microinjection and electroporation, as well as calcium co-precipitation, and commercially available cationic polymers and lipids, and cell-penetrating peptides, cell-penetrating (biolistic) particles may each be used. For example, viruses, particularly preferred is AAV, may be used as delivery vehicles, whether to the cytoplasm and/or nucleus, for example via the (reversible) fusion of Cas protein complex of the invention or a ribonucleoprotein complex of the invention to the viral particle.

In another aspect the present invention provides a method of modifying a target nucleic acid, wherein the at least one functional moiety is a marker protein or reporter protein and the marker protein or reporter protein associates with the target nucleic acid; preferably wherein the marker is a fluorescent protein, for example a green fluorescent protein (GFP).

In the aforementioned methods of modifying a target nucleic acid, the functional moiety may be a marker and the marker associates with the target nucleic acid; preferably wherein the marker is a protein; optionally a fluorescent protein, e.g. green fluorescent protein (GFP), yellow fluorescent protein (YFP), red fluorescent protein (RFP) or mCherry. Whether in vitro, ex vivo or in vivo, then methods of the invention can be used to directly visualise a target locus in a nucleic acid molecule, preferably in the form of a higher order structure such as a supercoiled plasmid or chromosome, or a single stranded target nucleic acid such as mRNA. Direct visualisation of a target locus may use electron micrography, or fluorescence microscopy. However, it will be appreciated that in the context of methods of the invention, other kinds of label may be used as the marker including organic dye molecules, radiolabels and spin labels which may be small molecules.

In methods of the invention for modifying a target nucleic acid wherein the target nucleic acid is dsDNA, the functional moiety may be a nuclease or a helicase-nuclease, and the modification is preferably a single stranded or a double stranded break at a desired locus. In this way unique sequence specific cutting of DNA can be engineered by using a suitable functional moiety fused to a ribonucleoprotein complex. The chosen sequence of the RNA component of the final ribonucleoprotein complex provides the desired sequence specificity for the action of the functional moiety.

Therefore, the invention also provides a method of non-homologous end joining of a dsDNA molecule in a cell at a desired locus to remove at least a part of a nucleotide sequence from the dsDNA molecule; optionally to knockout the function of a gene or genes, wherein the method comprises making double stranded breaks using any of the methods of modifying a target nucleic acid as hereinbefore described.

The invention further provides a method of homologous recombination of a nucleic acid into a dsDNA molecule in a cell at a desired locus in order to modify an existing nucleotide sequence or insert a desired nucleotide sequence, wherein the method comprises making a double stranded break at the desired locus using any of the methods of modifying a target nucleic acid as hereinbefore described.

The invention therefore also provides a method of modifying gene expression in an organism comprising modifying a target nucleic acid sequence according to any of the methods hereinbefore described, wherein the nucleic acid is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor.

The invention additionally provides a method of modifying gene expression in an organism comprising modifying a target nucleic acid sequence according to any of the methods hereinbefore described, wherein the nucleic acid is an mRNA and the functional moiety is a ribonuclease; optionally selected from an endonuclease, a 3′ exonuclease or a 5′ exonuclease.

The target nucleic acid may be DNA, RNA or synthetic nucleic acid. Preferably the target nucleic acid is DNA; preferably dsDNA.

However, the target nucleic acid can be RNA; preferably mRNA. Alternatively therefore, the present invention also provides methods of modifying a target nucleic acid, wherein the target nucleic acid is RNA.

In another aspect the present invention provides a method of modifying a target nucleic acid, wherein the nucleic acid is dsDNA, the at least one functional moiety is a nuclease or a helicase-nuclease, and the modification is a single-stranded or a double-stranded break at a desired locus.

In another aspect the present invention provides a method of modifying a target nucleic acid in a cell, wherein modification results in a silencing of gene expression at a desired locus; and wherein the method includes the steps of;

a. making double-stranded breaks in the dsDNA molecule; and

b. repair of the dsDNA molecule in the cell by non-homologous end joining (NHEJ).

In another aspect the present invention provides a method of modifying a target nucleic acid in a cell; wherein the existing nucleotide sequence is modified or deleted and/or a desired nucleotide sequence is inserted at a desired location wherein the method includes the steps of;

a. making a double stranded break at the desired locus; and

b. repair of the dsDNA molecule in the cell by homologous recombination.

In another aspect the present invention provides a method of modifying gene expression in a cell comprising modifying a target nucleic acid sequence as hereinbefore described; wherein the nucleic acid is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor.

In another aspect the present invention provides a method of modifying gene expression in a cell comprising modifying a target nucleic acid sequence as hereinbefore described, wherein the nucleic acid is an mRNA and the functional moiety is a ribonuclease; optionally selected from an endonuclease, a 3′ exonuclease or a 5′ exonuclease.

In another aspect the present invention provides a method of modifying a target nucleic acid as hereinbefore described, wherein the method is carried out at a temperature between 45° C. and 100° C. Preferably, the method is carried out at a temperature at or above 50° C. More preferably, the method is carried out at a temperature between 55° C. and 80° C. Optimally, the method is carried out at a temperature between 60° C. and 65° C. Alternatively, the method may be carried out at a temperature between 20° C. and 45° C. More preferably, at a temperature between 30° C. and 45° C. Even more preferably at a temperature between 37° C. and 45° C.

In any of the methods of modifying a target nucleic acid hereinbefore described, the cell may be a prokaryotic cell or alternatively, may be a eukaryotic cell.

## Host Cells

Advantageously, the present invention is of broad applicability and host cells of the present invention may be derived from any genetically tractable organism which can be cultured. Accordingly, the present invention provides a host cell transformed by a method as hereinbefore described. The invention provides a transformed cell, having a target nucleic acid sequence in a double stranded target polynucleotide, said cell comprising a Cas protein or polypeptide as provided herein and at least one targeting RNA molecule as provided herein, and an expression vector comprising a nucleic acid encoding at least one of said Cas protein and said targeting RNA molecule.

Appropriate host cells may be prokaryotic or eukaryotic. In particular, commonly used host cells may be selected for use in accordance with the present invention including prokaryotic or eukaryotic cells which are genetically accessible and which can be cultured, for example prokaryotic cells, fungal cells, plant cells and animal cells. Preferably, host cells will be selected from a prokaryotic cell, a fungal cell, a plant cell, a protist cell or an animal cell. Preferably, host cells will be selected from a prokaryotic cell, a fungal cell, a plant cell, a protist cell or an animal cell except a human cell. Preferably, host cells will not include human cells, including embryonic stem cells. Preferred host cells for use in accordance with the present invention are commonly derived from species which typically exhibit high growth rates, are easily cultured and/or transformed, display short generation times, species which have established genetic resources associated with them or species which have been selected, modified or synthesized for optimal expression of heterologous protein under specific conditions. In preferred embodiments of the invention where the protein of interest is eventually to be used in specific industrial, agricultural, chemical or therapeutic contexts, an appropriate host cell may be selected based on the desired specific conditions or cellular context in which the protein of interest is to be deployed. Preferably the host cell will be a prokaryotic cell. In preferred embodiments the host cell is a bacterial cell. The host cell may for instance be an Escherichia coli (E. coli) cell. Preferably the host cell will be a cell of a thermophilic bacterium.

Methods and uses of the invention described herein may be used to modify genomes of bacterial cells. In particular embodiments, the bacteria are thermophilic bacteria, preferably the bacteria are selected from: Acidithiobacillus species including Acidithiobacillus caldus; Aeribacillus species including Aeribacillus pallidus; Alicyclobacillus species including Alicyclobacillus acidocaldarius, Alicyclobacillus acidoterrestris, Alicyclobacillus cycloheptanicusl, Alicyclobacillus hesperidum; Anoxybacillus species including Anoxybacillus caldiproteolyticus, Anoxybacillus flavithermus, Anoxybacillus rupiensis, Anoxybacillus tepidamans; Bacillus species including Bacillus caldolyticus, Bacillus caldotenax, Bacillus caldovelox, Bacillus coagulans, Bacillus clausii, Bacillus hisashii, Bacillus licheniformis, Bacillus methanolicus, Bacillus smithii including Bacillus smithii ET138, Bacillus subtilis, Bacillus thermocopriae, Bacillus thermolactis, Bacillus thermoamylovorans, Bacillus thermoleovorans; Caldibacillus species including Caldibacillus debilis; Caldicellulosiruptor species including Caldicellulosiruptor bescii, Caldicellulosiruptor hydrothermalis, Caldicellulosiruptor kristjanssonfi, Caldicellulosiruptor kronotskyensis, Caldicellulosiruptor lactoaceticus, Caldicellulosiruptor obsidiansis, Caldicellulosiruptor owensensis, Caldicellulosiruptor saccharolyticus; Clostridium species including Clostridium clariflavum, Clostridium straminisolvens, Clostridium tepidiprofundi, Clostridium thermobutyricum, Clostridium thermocellum, Clostridium thermosuccinogenes, Clostridium thermopalmarium; Deinococcus species including Deinococcus cellulosilyticus, Deinococcus deserti, Deinococcus geothermalis, Deinococcus murrayi, Deinococcus radiodurans; Defluviitalea species including Defluviitalea phaphyphila, Desulfotomaculum species including Desulfotomaculum carboxydivorans, Desulfotomaculum nigrificans, Desulfotomaculum salinum, Desulfotomaculum solfataricum; Desulfurella species including Desulfurella acetivorans; Desulfurobacterium species including Desulfurobacterium thermolithotrophum; Geobacillus species including Geobacillus icigianus, Geobacillus caldoxylosilyticus, Geobacillus jurassicus, Geobacillus galactosidasius, Geobacillus kaustophilus, Geobacillus lituanicus, Geobacillus stearothermophilus, Geobacillus subterraneus, Geobacillus thermantarcticus, Geobacillus thermocatenulatus, Geobacillus thermodenitrificans, Geobacillus thermoglucosidans, Geobacillus thermoleovorans, Geobacillus toebfi, Geobacillus uzenensis, Geobacillus vulcanfi, Geobacillus zalihae; Hydrogenobacter species including Hydrogenobacter thermophiles; Hydrogenobaculum species including Hydrogenobaculum acidophilum; Ignavibacterium species including Ignavibacterium album; Lactobacillus species including Lactobacillus bulgaricus, Lactobacillus delbrueckii, Lactobacillus ingluviei, Lactobacillus thermotolerans; Marinithermus species including Marinithermus hydrothermalis; Moorella species including Moorella thermoacetica; Oceanithermus species including Oceanithermus desulfurans, Oceanithermus profundus; Paenibacillus species including Paenibacillus sp. J2, Paenibacillus marinum, Paenibacillus thermoaerophilus; Persephonella species including Persephonella guaymasensis, Persephonella hydrogeniphila, Persephonella marina; Rhodothermus species including Rhodothermus marinus, Rhodothermus obamensis, Rhodothermus profundi; Sulfobacillus species including Sulfobacillus acidophilus; Sulfurihydrogenibium species including Sulfurihydrogenibium azorense, Sulfurihydrogenibium kristjanssonii, Sulfurihydrogenibium rodmanfi, Sulfurihydrogenibium yellowstonense; Symbiobacterium species including Symbiobacterium thermophilum, Symbiobacterium toebfi; Thermoanaerobacter species including Thermoanaerobacter brockii, Thermoanaerobacter ethanolicus, Thermoanaerobacter italicus, Thermoanaerobacter kivui, Thermoanaerobacter marianensis, Thermoanaerobacter mathranii, Thermoanaerobacter pseudoethanolicus, Thermoanaerobacter wiegelii; Thermoanaerobacterium species including Thermoanaerobacterium aciditolerans, Thermoanaerobacterium aotearoense, Thermoanaerobacterium ethanolicus, Thermoanaerobacterium pseudoethanolicus, Thermoanaerobacterium saccharolyticum, Thermoanaerobacterium thermosaccharolyticum, Thermoanaerobacterium xylanolyticum; Thermobacillus species including Thermobacillus composti, Thermobacillus xylanilyticus; Thermocrinis species including Thermocrinis albus, Thermocrinis ruber; Thermodulfatator species including Thermodesulfatator atlanticus, Thermodesulfatator autotrophicus, Thermodesulfatator indicus; Thermodesulfobacterium species including Thermodesulfobacterium commune, Thermodesulfobacterium hydrogeniphilum; Thermodesulfobium species including Thermodesulfobium narugense; Thermodesulfovibrio species including Thermodesulfovibrio aggregans, Thermodesulfovibrio thiophilus, Thermodesulfovibrio yellowstonfi; Thermosipho species including Thermosipho africanus, Thermosipho atlanticus, Thermosipho melanesiensis; Thermotoga species including Thermotoga maritima, Thermotoga neopolitana, Thermotoga sp. RQ7; Thermovibrio species including Thermovibrio ammonificans, Thermovibrio ruber, Thermovirga species including Thermovirga lienfi and Thermus species including Thermus aquaticus, Thermus caldophilus, Thermus flavus, Thermus scotoductus, Thermus thermophilus; Thiobacillus neapolitanus.

In another aspect, a method or use described herein can be used to modify bacteria that are mesophilic. In preferred embodiments, the bacteria are selected from: Acidithiobacillus species including Acidithiobacillus caldus; Actinobacillus species including Actinobacillus succinogenes; Anaerobiospirillum species including Anaerobiospirillum succiniciproducens; Bacillus species including Bacillus alcaliphilus, Bacillus amyloliquefaciens, Bacillus circulans, Bacillus cereus, Bacillus clausii, Bacillus firmus, Bacillus halodurans, Bacillus hisashii, Bacillus lautus, Bacillus lentus, Bacillus licheniformis, Bacillus megaterium, Bacillus pumilus, Bacillus smithii, Bacillus subtilis, Bacillus thuringiensis; Basfia species including Basfia succiniciproducens; Brevibacillus species including Brevibacillus brevis; Brevibacillus laterosporus; Clostridium species including Clostridium acetobutylicum, Clostridium autoethanogenum, Clostridium beijerinkii, Clostridium carboxidivorans, Clostridium cellulolyticum, Clostridium ljungdahlii, Clostridium pasteurianum, Clostridum perfringens, Clostridium ragsdalei, Clostridium saccharobutylicum, Clostridium saccharoperbutylacetonium; Corynebacterium species including Corynebacterium glutamicum; Desulfitobacterium species including Desulfitobacterium dehalogenans, Desulfitobacterium hafniense; Desulfotomaculum species including Desulfotomaculum acetoxidans, Desulfotomaculum gibsoniae, Desulfotomaculum reducens, Desulfotomaculum ruminis; Enterobacter species including Enterobacter asburiae; Enterococcus species including Enterococcus faecalis; Escherichia species including Escherichia coli; Lactobacillus species including Lactobacillus acidophilus, Lactobacillus amylophilus, Lactobacillus amylovorus, Lactobacillus animalis, Lactobacillus arizonensis, Lactobacillus bavaricus, Lactobacillus brevis, Lactobacillus buchneri, Lactobacillus bulgaricus, Lactobacillus casei, Lactobacillus corynoformis, Lactobacillus crispatus, Lactobacillus curvatus, Lactobacillus delbrueckii, Lactobacillus fermenturn, Lactobacillus gasseri, Lactobacillus helveticus, Lactobacillus johnsonii, Lactobacillus pentosus, Lactobacillus plantarum, Lactobacillus reuteri, Lactobacillus rhamnosus, Lactobacillus sakei, Lactobacillus salivarius, Lactobacillus sanfriscensis; Lactococcus species, including Lactococcus lactis; Mannheimia species including Mannheimia succiniciproducens; Paenibacillus species including Paenibacillus alvei, Paenibacillus beijingensis, Paenibacillus borealis, Paenibacillus dauci, Paenibacillus durus, Paenibacillus graminis, Paenibacillus larvae, Paenibacillus lentimorbus, Paenibacillus macerans, Paenibacillus mucilaginosus, Paenibacillus odorifer, Paenibacillus polymyxa, Paenibacillus stellifer, Paenibacillus terrae, Paenibacillus wulumuqiensis; Pediococcus species including Pediococcus acidilactici, Pediococcus claussenii, Pediococcus ethanolidurans, Pediococcus pentosaceus; Propionibacterium species, including P. acidipropionici, P. freudenreichii, P. jensenii; Salmonella typhimurium; Sporolactobacillus species including Sporolactobacillus inulinus, Sporolactobacillus laevolacticus; Staphylococcus aureus; Streptococcus species including Streptococcus agalactiae, Streptococcus bovis, Streptococcus equisimilis, Streptococcus feacalis, Streptococcus mutans, Streptococcus oralis, Streptococcus pneumonia, Streptococcus pyogenes, Streptococcus salivarius, Streptococcus thermophilus, Streptococcus sobrinus, Streptococcus uberis; Streptomyces species including Streptomyces achromogenes, Streptomyces avermitilis, Streptomyces coelicolor, Streptomyces griseus, Streptomyces lividans, Streptomyces parvulus, Streptomyces venezuelae, Streptomyces vinaceus; Tetragenococcus species including Tetragenococcus halophilus and Zymomonas species including Zymomonas mobilis. Pseudomonas species including Pseudomonas putida, Pseudomonas aeruginosa, Pseudomonas alcaligenes, Pseudomonas anguilliseptica, Pseudomonas argentinensis, Pseudomonas borbori, Pseudomonas citronellolis, Pseudomonas flavescens, Pseudomonas mendocina, Pseudomonas nitroreducens, Pseudomonas oleovorans, Pseudomonas pseudoalcaligenes, Pseudomonas resinovorans, Pseudomonas straminea, Pseudomonas asplenii, Pseudomonas aurantiaca, Pseudomonas aureofaciens, Pseudomonas chlororaphis, Pseudomonas corrugate, Pseudomonas fragi, Pseudomonas lundensis, Pseudomonas taetrolens, Pseudomonas antarctica, Pseudomonas azotoformans, Pseudomonas blatchfordae′, Pseudomonas brassicacearum, Pseudomonas brenneri, Pseudomonas cedrina, Pseudomonas corrugate, Pseudomonas fluorescens, Pseudomonas gessardii, Pseudomonas libanensis, Pseudomonas mandelii, Pseudomonas marginalis, Pseudomonas mediterranea, Pseudomonas meridiana, Pseudomonas migulae, Pseudomonas mucidolens, Pseudomonas orientalis, Pseudomonas panacis, Pseudomonas protegens, Pseudomonas proteolytica, Pseudomonas rhodesiae, Pseudomonas synxantha, Pseudomonas thivervalensis, Pseudomonas tolaasii, Pseudomonas veronii, Pseudomonas denitrificans, Pseudomonas pertucinogena, Pseudomonas cremoricolorata, Pseudomonas entomophila, Pseudomonas fulva, Pseudomonas monteilii, Pseudomonas mosselii, Pseudomonas oryzihabitans, Pseudomonas parafulva, Pseudomonas plecoglossicida, Pseudomonas putida, Pseudomonas balearica, Pseudomonas luteola, Pseudomonas stutzeri, Pseudomonas amygdali, Pseudomonas avellanae, Pseudomonas caricapapayae, Pseudomonas cichorii, Pseudomonas coronafaciens, Pseudomonas ficuserectae, ‘Pseudomonas helianthi’, Pseudomonas meliae, Pseudomonas savastanoi, Pseudomonas syringae, ‘Pseudomonas tomato’, Pseudomonas viridiflava, Pseudomonas abietaniphila, Pseudomonas acidophila, Pseudomonas agarici, Pseudomonas alcaliphila, Pseudomonas alkanolytica, Pseudomonas amyloderamosa, Pseudomonas asplenii, Pseudomonas azotifigens, Pseudomonas cannabina, Pseudomonas coenobios, Pseudomonas congelans, Pseudomonas costantinii, Pseudomonas cruciviae, Pseudomonas delhiensis, Pseudomonas excibis, Pseudomonas extremorientalis, Pseudomonas frederiksbergensis, Pseudomonas fuscovaginae, Pseudomonas gelidicola, Pseudomonas grimontii, Pseudomonas indica, Pseudomonas jessenii, Pseudomonas jinjuensis, Pseudomonas kilonensis, Pseudomonas knackmussii, Pseudomonas koreensis, Pseudomonas lini, Pseudomonas lutea, Pseudomonas moraviensis, Pseudomonas otitidis, Pseudomonas pachastrellae, Pseudomonas palleroniana, Pseudomonas papaveris, Pseudomonas peli, Pseudomonas perolens, Pseudomonas poae, Pseudomonas pohangensis, Pseudomonas protegens, Pseudomonas psychrophila, Pseudomonas psychrotolerans, Pseudomonas rathonis, Pseudomonas reptilivora, Pseudomonas resiniphila, Pseudomonas rhizosphaerae, Pseudomonas rubescens, Pseudomonas salomonii, Pseudomonas segitis, Pseudomonas septica, Pseudomonas simiae, Pseudomonas suis, Pseudomonas thermotolerans, Pseudomonas toyotomiensis, Pseudomonas tremae, Pseudomonas trivialis, Pseudomonas turbinellae, Pseudomonas tuticorinensis, Pseudomonas umsongensis, Pseudomonas vancouverensis, Pseudomonas vranovensis, Pseudomonas xanthomarina. Preferably the mesophilic bacterium is Pseudomonas putida.

In a further aspect, methods or uses or uses of the invention defined herein could be used to modify the genome of yeast or fungi. In particular embodiments, the fungal species are mesophilic, preferably the fungi is selected from: an Aspergillus species including, but not limited to, Aspergillus nidulans, Aspergillus niger, Aspergillus oryzae and Aspergillus terreus, more preferably the Aspergillus species is Aspergillus nidulans or Aspergillus niger. Alternatively, the mesophilic fungal species could be a Candida species. A method or use defined herein could be used to modify the genome of yeast species including, but not limited to, Saccharomyces species including Saccharomyces cerevisiae, Schizosaccharomyces species including Schizosaccharomyces pombe, Pichia species including, but not limited to Pichia pastoris, Pichia stipitis. A method or use defined herein could be used to modify the genome of fungal species including, but not limited to, Hansenula species including Hansenula polymorpha, Penicillium species including, but not limited to P. brasilianum, P. chrysogenum, Yarrowia species including Yarrowia lipolytica.

The invention further relates to use of a method as defined herein to modify a yeast or fungal species that are thermophilic, preferably the fungi or yeast is selected from: Aspergillus species including Aspergillus fumigatus, Aspergillus nidulans, Aspergillus terreus, Aspergillus versicolor, Canariomyces species including Canariomyces thermophile; Chaetomium species including Chaetomium mesopotamicum, Chaetomium thermophilum; Candida species including Candida bovina, Candida sloofii, Candida thermophila, Candida tropicalis, Candida krusei (=Issatchenkia orientalis); Cercophora species including Cercophora coronate, Cercophora septentrionalis; Coonemeria species including Coonemeria aegyptiaca; Corynascus species including Corynascus thermophiles; Geotrichum species including Geotrichum candidum; Kluyveromyces species including Kluyveromyces fragilis, Kluyveromyces marxianus; Malbranchea species including Malbranchea cinnamomea, Malbranchea sulfurea; Melanocarpus species including Melanocarpus albomyces; Myceliophtora species including Myceliophthora fergusii, Myceliophthora thermophila; Mycothermus species including Mycothermus thermophiles (=Scytalidium thermophilum/Torula thermophila); Myriococcum species including Myriococcum thermophilum; Paecilomyces species including Paecilomyces thermophila; Remersonia species including Remersonia thermophila; Rhizomucor species including Rhizomucor pusillus, Rhizomucor tauricus; Saccharomyces species including Saccharomyces cerevisiae, Schizosaccharomyces species including Schizosaccharomyces pombe, Scytalidiurn species including Scytalidium thermophilum; Sordaris species including Sordaria thermophila; Thermoascus species including Thermoascus aurantiacus, Thermoascus thermophiles; Thermomucor species including Thermomucor indicae-seudaticae and Thermomyces species including Thermomyces ibadanensis, Thermomyces lanuginosus.

In the aforementioned lists, microbes identified in bold typeface have been found to be particularly suitable/applicable in use for the present invention.

Some preferred embodiments of the present invention include one or more thermophilic microbes selected from: Thermophilic bacilli, including Aeribacillus, Alicyclobacillus, Anoxybacillus, Bacillus, Geobacillus; Paenibacillus species; Thermophilic clostridia, including Anaerobacter, Anaerobacterium, Caldicellulosiruptor, Clostridium, Moorella, Thermoanaerobacter, Thermoanaerobacterium, Thermobrachium, Thermohalobacter species or one or more thermophilic Lactobacillus species and mesophilic bacteria selected from Bacillus species, Escherichia coli, Lactobacillus species Lactococcus species, Propionibacterium species and Pseudomonas species.

Below are polynucleotide and amino acid sequences of Cas proteins used in accordance with the invention.

## DETAILED DESCRIPTION

### Example 1: Isolation of Geobacillus thermodenitrificans

G. thermodenitrificans was surprisingly discovered during a search of a library of ±500 isolates for a thermophile capable of degrading lignocellulosic substrates under anaerobic conditions. At first a library of ±500 isolates was established which, after several selection rounds by isolation on cellulose and xylan, was trimmed down to 110 isolates. This library of 110 isolates consisted solely of Geobacillus isolates with G. thermodenitrificans representing 79% of the library.

The isolated G. thermodenitrificans strain has been named “T12”. The Cas9 protein from G. thermodenitrificans T12 has been named “gtCas9”.

### Example 2: Defining the Essential Consensus Sequences for Cas9 in Geobacillus thermodenitrificans

The following database searches and alignments were performed:

pBLAST and nBLAST were performed on the in-house BLAST server, in which either the protein or gene sequence of G. thermodenitrificans T12 was used as query sequence. This database was last updated May 2014 and therefore does not contain the most recently added Geobacillus genomes, but normal online BLAST was not used to prevent publication of the T12 sequence. Sequence identities found to be greater than 40% in the BLAST search are included in FIG. 1.

To include more recent sequence data, the sequence of Geobacillus MAS1 (most closely related to gtCas9) was used to perform a PSI-BLAST on the NCBI website (Johnson et al., 2008 Nucleic Acids Res. 36 (Web Server issue): W5-9). Two consecutive rounds of PSI-BLAST were performed, in which only sequences that met the following criteria were used for the next round: minimum sequence coverage of 96% in the first round and 97% in the second and third round, minimum identity 40%, only one strain per species.

The sequences resulting from the PSI-BLAST, as well as the sequences with more than 40% identity to T12 from the internal server pBLAST that did not appear in the PSI-BLAST were aligned together with currently well-characterized mesophilic sequences and all currently identified thermophilic sequences also if these were more distantly related, from which a Neighbour-Joining tree was constructed (see FIG. 1). Alignment was performed in Mega6 using ClustalW, after which a tree was constructed using the Neighbour-Joining method and bootstrap analysis was performed using 1000 replicates.

When BLASTn was performed using Geobacillus sp. MAS1 as the query sequence, only Geobacillus sp. JF8 Cas9 was identified with 88% identity, indicating very little homology at the gene level. FIG. 2 is a Neighbour-Joining tree of Clustal-aligned Cas9 gene sequences.

Protein sequences of G. thermodenitrificans T12, A. naeslundii and S. pyogenes were further analyzed for protein domain homology (see FIG. 3) by aligning them in CloneManager using BLOSUM62 with default settings.

### Example 3: Identifying Core Amino Acid Motifs which are Essential for the Function of CAS9 and Those which Confer Thermostability in Thermophilic Cas9 Nucleases

Percentages identity of the above described aligned protein sequences are provided in FIG. 1. gtCas9 belongs to Type II-C. The best-studied and recently crystallized structure of a Type II-C system is from Actinomyces naeslundii (Jinek et al., 2014, Science 343: 1247997). This protein sequence shows only 20% identity to gtCas9 but can be used to estimate highly conserved residues. Two well-characterized Type II-A systems (S. pyogenes and S. thermophilus) were also included in the analyses (Jinek et al., 2014, Science 343: 1247997; Nishimasu et al., 2014, Cell 156: 935-949). Alignments of these four protein sequences are shown in FIG. 3; FIG. 4 shows the protein architecture as determined for A. naeslundii (‘Ana-Cas9’) (Jinek et al., 2014, Science 343: 1247997). The length of Cas9 from t12 (gtCas9) and Actinomyces naeslundii is highly similar (A. naeslundii 1101 aa, gtCas9 1082 aa) and gtCas9 is expected to have similar protein architecture but this remains to be determined, as the overall sequence identity to cas9-Ana is only 20%. All active side residues described by Jinek et al. (Jinek et al., 2014, Science 343: 1247997) in Cas9 from A. naeslundii and S. pyogenes could be identified in gtCas9 (see FIG. 3). The PAM-binding domain has been determined for the S. pyogenes Type II-A system but not for any Type II-C system and is therefore only indicated in the S. pyogenes sequence. Moreover, the PAM-recognition site varies strongly, not only between CRISPR systems but also between species containing the same system.

### Example 4: Determination of the PAM Sequence of G. thermodenitrificans gtCas9

It has been established that the prokaryotic CRISPR systems serve their hosts as adaptive immune systems (Jinek et al., 2012, Science 337: 816-821) and can be used for quick and effective genetic engineering (Mali et al., 2013, Nat Methods 10: 957-963.).

Cas9 proteins function as sequence-specific nucleases for the type II CRISPR systems (Makarova et al., 2011, Nat Rev Micro 9: 467-477). Small crRNA molecules, which consist of a “spacer” (target) linked to a repetition region, are the transcription and processing products of a CRISPR loci. “Spacers” naturally originate from the genome of bacteriophages and mobile genetic elements, but they can also be designed to target a specific nucleotide sequence during a genetic engineering process (Bikard et al., 2013, Nucleic Acids Research 41: 7429-7437). The crRNA molecules are employed by the Cas9 as guides for the identification of their DNA targets. The spacer region is identical to the targeted for cleavage DNA region, the “protospacer” (Brouns et al., 2012, Science 337: 808-809). A PAM (Protospacer Adjacent Motif), next to the protospacer, is required for the recognition of the target by the Cas9 (Jinek et al., 2012, Science 337: 816-821).

In order to perform in vitro or in vivo PAM-determination studies for Type II systems, it is necessary to in silico predict the CRISPR array of the system, the tracrRNA-expressing module. The CRISPR array is used for the identification of the crRNA module. The tracrRNA-expressing sequence is located either within a 500 bp-window flanking Cas9 or between the Cas genes and the CRISPR locus (Chylinski, K., et al. (2014) Classification and evolution of type II CRISPR-Cas systems. Nucleic Acids Res. 42, 6091-6105). The tracrRNA should consist of a 5′-sequence with high level of complementarity to the direct repeats of the CRISPR array, followed by a predicted structure of no less than two stem-loop structures and a Rho-independent transcriptional termination signal (Ran, F. A., et al. (2015) In vivo genome editing using Staphylococcus aureus Cas9. Nature 520, 186-191). The crRNA and tracrRNA molecule can then be used to design a chimeric sgRNA module. The 5′-end of the sgRNA consists of a truncated 20 nt long spacer followed by the 16-20 nt long truncated repeat of the CRISPR array. The repeat is followed by the corresponding truncated anti-repeat and the stem loop of the tracrRNA module. The repeat and anti-repeat parts of the sgRNA are generally connected by a GAAA linker (Karvelis, T., et al. (2015) Rapid characterization of CRISPR-Cas9 protospacer adjacent motif sequence elements. Genome Biol. 16, 253).

The cas genes (the cas9 followed by the cas1 and the cas2 genes) of the G. thermodenitrificans T12 type IIc CRISPR system are transcribed using the antisense strand of the T12 chromosome. The cas2 gene is followed by a 100 bp long DNA fragment which upon transcription forms an RNA structure with multiple loops. This structure obviously acts as a transcriptional terminator.

A CRISPR array with 11 repeats and 10 spacer sequences is located upstream of the transcriptional termination sequence and the leader of the array is located at the 5′ end of the array. The DNA locus which is transcribed into the tracrRNA is expected to be downstream of the cas9 gene. The alignment of the 325 bp long sequence right downstream of the cas9 gene with the 36 bp long repeat from the CRISPR array revealed that there is a 36 bp long sequence in the tracrRNA locus almost identical to the repeat (shown in FIG. 6). This result led us to the conclusion that the direction of the transcription of the tracrRNA locus should be opposite to the direction of the transcription of the CRISPR array. Consequently the 5′-end of the tracrRNA will be complementary to the 3′-end of the crRNA, leading to the formation of the—required by the Cas9-dual-RNA molecule.

### Example 5: Target Generation with Randomized PAM

Two different spacers from the CRISPR II loci of the G. thermodenitrificans T12 strain were amplified by PCR using the G. thermodenitrificans T12 genomic DNA as template. Two pairs of degenerate primers were used for the amplification of each spacer:

Firstly, a pair that cause the introduction of six random nucleotides upstream of the “protospacer” fragment were used, leading to the production of a pool of protospacers with randomized PAM sequences.

Secondly, a pair that cause the introduction of six random nucleotides downstream of the “protospacer” fragment were used, leading to the production of a pool of protospacers with randomized PAM sequences.

The produced fragments were ligated to the pNW33n vector, producing 4 pools of “protospacer” constructs, with all the possible 4096 different combinations of 6-nucleotide long PAMs each. The assembled DNA was used for the transformation of G. thermodenitrificans T12 cells. The cells were plated on chloramphenicol selection and more than 2×106 cells from each protospacer pool will be pooled. The plasmid DNA was extracted from the pools, the target region will be PCR amplified and the products sent for deep sequencing. The PAMs with the fewest reads will be considered active and the process will be repeated only with pNW33n constructs that contain spacers with these PAMs. Reduced transformation efficiency of the G. thermodenitrificans T12 will confirm the activity of the PAMs.

### Example 6: In Vitro Determination of PAM Sequences for gtCas9

Construction of the pRham:Cas9gt Vector

The cas9gt gene was PCR amplified from the G. thermodenitrificans T12 genome, using the BG6927 and BG6928 primers, and combined with the pRham C-His Kan Vector (Lucigen) in one mixture. The mixture was used for transforming E. cloni thermo-competent cells according to the provided protocol. 100 μl from the transformation mixture were plated on LB+50kanamycin plates for overnight growth at 37° C. Out of the formed E. cloni::pRham:cas9gt single colonies 3 were randomly selected and inoculated in 10 ml LB medium containing 50 μg/ml kanamucin. Glycerol stocks were prepared from the cultures by adding sterile glycerol to 1 ml from each culture up to a final concentration of 20% (v/v). The glycerol stocks were stored at −80° C. The remaining 9 ml from each culture were used for plasmid isolation according to the “GeneJET Plasmid Miniprep Kit” (Thermoscientific) protocol. The plasmids were sent for sequence verification of the cas9gt and one of the plasmids was verified to contain the gene with the right sequence. The corresponding culture was further used for heterologous expression and purification of the gtCas9.

Heterologous Expression of gtCas9 in E. cloni::pRham:cas9gt Vector

An E. cloni::pRham:cas9gt preculture was prepared after inoculating 10 ml LB+50kanamycin with the corresponding glycerol stocks. After overnight growth at 37° C. and 180 rpm, 2 ml from the preculture were used for inoculating 200 ml of LB+50 kanamycin medium. The E. cloni::pRham:cas9gt culture was incubated at 37° C., 180 rpm until an OD600 of 0.7. The gtCas9 expression was then induced by adding L-rhamnose to a final concentration of 0.2% w/v. The expression was allowed to proceed for 8 h, after which the cultures were centrifuged for 10 minutes at 4700 rpm, 4° C. to harvest the cells. The medium was discarded and the pelleted cells were either stored at −20° C. or used for the preparation of the cell free extract (CFE) according to the following protocol:


- - 1. Resuspend the pellet in 20 ml Sonication Buffer (20 mM Sodium
    Phosphate buffer (pH=7.5), 100 mM NaCl, 5 mM MgCl2, 5% (v/v)
    Glycerol, 1 mM DTT)
  - 2. Disrupt 1 ml of cells by sonication (8 pulses of 30 seconds, cool
    for 20 seconds on ice in between)
  - 3. Centrifuge for 15 minutes at 35000 g, 4° C. in order to
    precipitate insoluble parts
  - 4. Remove the supernatant and store it at 4° C. or on ice  
    Designing and Construction of the PAM Library Targeting sgRNA Module
    for gtCas9

After in silico determination of the tracrRNA expressing DNA module in the genome of G. thermodenitrificans T12 strain (see Example 4 above), a single guide (sg)RNA expressing DNA module that combines the crRNA and tracrRNA modules of the CRISPR/Cas9 system in a single molecule was designed. The spacer at the 5′-end of the sgRNA was designed to be complementary to the protospacer of the plasmid library and the module was set under the transcriptional control of a T7 promoter. The pT7_sgRNA DNA module was synthesized by Baseclear and received in a pUC57 vector, forming the pUC57:pT7_sgRNA vector. DH5a competent E. coli cells (NEB) were transformed with the vector and the transformation mixture was plated on LB-agar plates containing 100 μg/ml ampicillin. The plates were incubated overnight at 37° C. Three of the formed single colonies were inoculated in 10 ml LB medium containing 100 μg/ml ampicillin. Glycerol stocks were prepared from the cultures by adding sterile glycerol to 1 ml from each culture up to a final concentration of 20% (v/v). The glycerol stocks were stored at −80° C. The remaining 9 ml from each culture were used for plasmid isolation according to the “GeneJET Plasmid Miniprep Kit” (Thermoscientific) protocol. The isolated plasmid was used as a PCR template for amplification of the pT7_sgRNA module. The 218 bp long pT7_sgRNA DNA module (of which the first 18 bp correspond to the pT7) was obtained using the primers BG6574 and BG6575. The complete PCR mixture was run on a 1.5% agarose gel. The band with the desired size was excised and purified according to the “Zymoclean™ Gel DNA Recovery Kit” protocol.

In vitro transcription (IVT) was performed using the “HiScribe™ T7 High Yield RNA Synthesis Kit” (NEB). The purified pT7_sgRNA DNA module was used as template. The IVT mixture was mixed with an equal volume of RNA loading dye (NEB) and heated at 70° C. for 15 minutes in order to disrupt the secondary structure. The heat treated IVT mixture was run on a denaturing Urea-PAGE and the resulting polyacrylamide gel was embaptised for 10 minutes in 100 ml 0.5×TBE buffer containing 10 μl of SYBR Gold (Invitrogen) for staining purposes. The band at the desired size (200 nt) was excised and the sgRNA was purified according to the following RNA purification protocol:


- - 1. Cut RNA gel fragments with a scalpel and add 1 ml of RNA elution
    buffer, leave overnight at room temperature.
  - 2. Divide 330 μl aliquots into new 1.5 ml tubes.
  - 3. Add 3 volumes (990 μl) of pre-chilled (−20° C.) 100% EtOH.
  - 4. Incubate for 60 minutes at −20° C.
  - 5. Centrifuge for 20 minutes at 13000 rpm in a microfuge at room
    temperature.
  - 6. Remove EtOH, wash pellet with 1 ml 70% EtOH.
  - 7. Centrifuge for 5 minutes at 13000 rpm in a microfuge at room
    temperature.
  - 8. Remove 990 μl of the supernatant.
  - 9. Evaporate the rest EtOH in a thermomixer at 55° C. for 15 to 20
    minutes.
  - 10. Resuspend pellet in 20 μl MQ, store at −20° C.

**Designing and Construction of a 7 nt Long PAM Library, and Linearization of the Library**

The design and construction of the PAM library was based on the pNW33n vector. A 20 bp long protospacer was introduced to the vector, flanked at its 3′ side by a 7 degenerate nucleotides long sequence; the degenerate sequence serves as the PAM and when the protospacer is flanked by a right PAM then it can be recognized as a target by an sgRNA loaded Cas9 and cleaved. The PAM library was prepared according to the following protocol:


- - 1. Prepare the SpPAM double stranded DNA insert by annealing the
    single stranded DNA oligos 1 (BG6494) and 2 (BG6495)
    - I. 10 μl 10×NEBuffer 2.1
    - II. 1 μl 50 μM oligo 1 (˜1.125 μg)
    - III. 1 μl 50 μM oligo 2 (˜1.125 μg)
    - IV. 85 μl MQ
    - V. Incubate the mixture at 94° C. for 5 min and cool down to
      37° C. at a rate of 0.03° C./sec
  - 2. Add 1 μl Klenow 3′-\>5′ exo⁻ polymerase (NEB) to each annealed
    oligos mixture and then add 2.5 μl of 10 μM dNTPs. Incubate at
    37° C. for 1 h and then at 75° C. for 20 min.
  - 3. Add 2 μl of the HF-BamHI and 2 μl of the BspHI restriction
    enzymes to 46 μl of the annealing mixture. Incubate at 37° C. for
    1 h. This process will lead to the SpPAMbb insert with sticky ends.
    Use the Zymo DNA cleaning and concentrator kit (Zymo Research) to
    clean the created insert.
  - 4. Digest pNW33n with the HF-BamHI and BspHI (NEB) and purify the
    3.400 bp long linear pNW33nbb fragment with sticky ends, using the
    Zymo DNA cleaning and concentrator kit (Zymo Research).
  - 5. Ligate 50 ng of pNW33nBB with 11 ng of the SPPAMbb insert using
    the NEB T4 ligase according to the provided protocol. Purify the
    ligation mixture using the Zymo DNA cleaning and concentrator kit
    (Zymo Research).
  - 6. Transform DH10b electro-competent cells (200 μl of cells with 500
    ng of DNA). Recover the cells in SOC medium (200 μl cells in 800 μl
    SOC) for an hour and then inoculate 50 ml of LB+12.5 μg/ml
    chloramphenicol with the recovered cells. Incubate overnight the
    culture at 37° C. and 180 rpm.
  - 7. Isolate plasmid DNA from the culture using the JetStar 2.0
    maxiprep kit (GENOMED).
  - 8. Use the SapI (NEB) restriction according to the provided protocol
    for linearizing the isolated plasmids.

**Designing and Execution of the PAM Determination Reactions**

The following cleavage reaction was set up for gtCas9-induced introduction of dsDNA breaks to the PAM library members that contain the right PAM downstream of the 3′ end of the targeted protospacer:


- - 1. 2.5 μg of *E. cloni*::pRham:cas9_(gt) CFE per reaction
  - 2. sgRNA to 30 nM final concentration
  - 3. 200 ng of linearized PAM library per reaction
  - 4. 2 μl of cleavage buffer (100 mM Sodium Phosphate buffer (pH=7.5),
    500 mM NaCl, 25 mM MgCl2, 25°(v/v) Glycerol, 5 mM DTT)
  - 5. MQ water up to 20 μl final volume

The reaction was incubated for 1 h at 60° C. and stopped after adding 4 μl of 6×gel loading dye (NEB). The reaction mixture was then loaded to a 1% agarose gel. The gel was subjected to an 1 h and 15 min long electrophoresis at 100V and then it was incubated for 30 min in 100 ml 0.5×TAE buffer containing 10 μl of SYBR Gold dye (ThermoFisher). After visualizing the DNA bands with blue light, the band that corresponded to the successfully cleaved and PAM containing DNA fragments was cut-off the gel and gel purified using the “Zymoclean™ Gel DNA Recovery Kit” according to the provided protocol.

Tagging of the PAM-Containing gtCAs9 Cleaved DNA Fragments for Sequencing

The Cas9-induced DNA breaks are usually introduced between the 3rd and the 4th nucleotide of a protospacer, proximally to the PAM sequence. As a result, it is not possible to design a pair of primers that can PCR amplify the PAM-containing part of the cleaved DNA fragments, in order to further on sequence and determine the PAM sequence. For this purpose, a 5-step process was employed:

Step 1: A-Tailing with Taq Polymerase

A-Tailing is a process to add a non-templated adenine to the 3′ end of a blunt, double-stranded DNA molecule using Taq polymerase

**Reaction Components:**

- - gtCas9-cleaved and PAM-containing DNA fragments—200 ng
  - 10× ThermoPol® Buffer (NEB)—5 μl
  - 1 mM dATP—10 μl
  - Taq DNA Polymerase (NEB)—0.2 μl
  - H₂O—up to 50 μl final reaction volume
  - Incubation time—20 min
  - Incubation temperature—72° C.

**Step 2: Construction of the Sequencing Adaptors**

Two complementary short ssDNA oligonucleotides were phosphorylated and annealed to form the sequencing adaptor for the PAM-proximal site of the DNA fragments from step 1. One of the oligonucleotides had an additional thymine at its 3′ end, in order to facilitate the ligation of the adaptor to the A-tailed fragments.

Adaptor Oligonucleotides phosphorylation (Separate phosphorylation reactions for each oligo)


- - 100 μM oligonucleotide stock—2 μL
  - 10×T4 DNA ligase buffer (NEB)—2 μL
  - Sterile MQ water—15 μL
  - T4 Polynucleotide Kinase (NEB)—1 μL
  - Incubation time—60 min
  - Incubation temperature—37° C.
  - T4 PNK inactivation—65° C. for 20 min

**Annealing of the Phosphorylated Oligonucleotides**

- - Oligonucleotide 1—5 μL from the corresponding phosphorylation
    mixture
  - Oligonucleotide 1—5 μL from the corresponding phosphorylation
    mixture
  - Sterile MQ water—90 μL
  - Incubate the phosphorylated oligos at 95° C. for 3 minutes. Cool the
    reaction slowly at room temperature for ˜30 min to 1 hr  
    Step 3: Ligation of the gtCas9-cleaved, A-tailed fragments with the
    sequencing adaptors The products of step 1 and 2 were ligated
    according to the following protocol:
  - 10×T4 DNA Ligase Buffer—2 μl
  - Product step 1—50 ng
  - Product step 2—4 ng
  - T4 DNA Ligase—1 μl
  - Sterile MQ water—to 20 μl
  - Incubation time—10 min
  - Incubation temperature—20-25° C.
  - Heat inactivation at 65° C. for 10 min

**Step 4: PCR Amplification of a 150-Nucleotides Long PAM-Containing Fragment**

5 μl from the ligation mixture of step 4 were used as template for PCR amplification using Q5 DNA polymerase (NEB). The oligonucleotide with the thymine extension from step 2 was employed as the forward primer and the reverse primer was designed to anneal 150 nucleotides downstream of the PAM sequence.

The same sequence was amplified using non-gtCas9 treated PAM-library DNA as template. Both PCR products were gel purified and sent for Illumina HiSeq 2500 paired-end sequencing (Baseclear).

**Analysis of the Sequencing Results and Determination of the Candidate PAM Sequences**

After analysing the sequencing results the following frequency matrices were constructed. The matrices depict the relative abundance of each nucleotide at every PAM position of the gtCas9 digested and non-digested libraries:

These results indicate a clear preference for targets with cytosine at the 5th PAM position and preference for targets with cytosines at the first 4 PAM positions.

### Example 7: In Silico PAM Prediction for gtCas9

In silico predictions of PAMs are possible if enough protospacer sequences are available in genome databases. The in silico prediction of gtCas9 PAM started with identification of hits of spacers from the CRISPR array in the genome of G. thermodenitrificans T12 strain by comparison to sequences in genome databases such as GenBank. The “CRISPR finder” (http://crispru-psud.fr/Server/) tool was used to identify candidate CRISPR loci in T12. The identified CRISPR loci output was then loaded into “CRISPR target” (http://bioanalysis.otago.ac.nz/CISPRTarget/_crispr_analysis.html) tool, which searches selected databases and provides an output with matching protospacers. These protospacer sequences were then screened for unique hits and for complementarity to spacers—for example, mismatches in the seed sequence were considered to be likely false positive hits and were excluded from further analysis. Hits with identity to prophage sequences and (integrated) plasmids demonstrated that the obtained hits were true positives. Overall, this process yielded 6 single hits (FIG. 7). Subsequently, the flanking regions (3′ for Type II gtCas nuclease) of the remaining, unique protospacer hits were aligned and compared for consensus sequences using a WebLogo (http://weblogo.berkeley.edu/logo.cgi) (Crooks G E, Hon G, Chandonia J M, Brenner S E WebLogo: A sequence logo generator, Genome Research, 14:1188-1190, (2004)) tool (FIG. 8).

The in silico results were comparable to the in vitro PAM identification experimental results (see Example 6) in which there was a bias for the identity of the 5th residue of the PAM sequence to be a cytosine.

### Example 8: Determination of 8 Nucleotide Long PAM Sequences for gtCas9

The in silico data from Example 8 suggested that gtCas9 had some preference for adenosine at the 8th position, therefore further PAM determination experiments were carried out where the 8th position of the PAM sequence was also tested. This is consistent with the characterisation of mesophilic Brevibacillus laterosporus SSP360D4 (Karvelis et al., 2015) Cas9 PAM sequence which was found to extend between the 5th and the 8th positions at the 3′ end of a protospacer.

Specific 8 Nucleotide-Long Sequence Variants of the PAMs were Trialed with gtCas9:

After performing an in vitro cleavage assay at 60° C. targeting these (non-linearized) plasmids with purified gtCas9 and the same sgRNA as before (see Example 6) an increased gtCas9 cleavage activity when the CCCCCCAA [SEQ ID NO: 11] sequence was employed as PAM was observed (FIG. 9). However, cleavage activity was clearly detectable for all the tested PAM sequences, even for the negative control PAM sequence a faint cleavage band was observed. Without wishing to be bound to a particular theory, it is possible that use of high gtCas9 concentration contributed to the cleavage observed with the negative control. It has been generally observed that high Cas9 concentrations in in vitro assays lead to Cas9-induced DNA cleavage without stringent PAM requirement.

Cas9 concentration in general is known to influence the efficiency of the Cas9 induced DNA cleavage (higher Cas9 concentration results in higher Cas9 activity). This was also observed when performing in vitro assays using the targeted plasmid with the CCCCCCAA [SEQ ID NO: 11] PAM sequence and different gtCas9 concentrations (FIG. 10)

The targeted plasmid with the CCCCCCAA [SEQ ID NO: 11] PAM sequence for in vitro assays as described above was conducted over a wide temperature range between 38 and 78° C. (FIG. 11). Surprisingly, gtCas9 was active at all the temperatures showing the highest activity between 40.1 and 64.9° C.

Thus, the optimal temperature range of Cas9 from Geobacillus species is much higher than that of Cas9 proteins which have been characterised to date. Similarly, the upper extent of the range in which it retains nuclease activity is much higher than that of known Cas9 proteins. A higher optimal temperature and functional range provides a significant advantage in genetic engineering at high temperatures and therefore in editing the genomes of thermophilic organisms, which have utility in a range of industrial, agricultural and pharmaceutical processes conducted at elevated temperatures.

### Example 9: In Vivo Genome Editing of Bacillus smithii ET138 with gtCas9 and 8 Nucleotide Length PAM Sequences

To confirm that the 8 nucleotide PAMs were also recognised by gtCas9 in vivo, an experiment was designed to delete the pyrF gene in the genome of Bacillus smithii ET138 at 55° C.

This method relies upon providing a homologous recombination template construct in which regions complimentary to the upstream and downstream of the target (pyrF) gene are provided to B. smithii ET 138 cells. Introduction of the template allows for the process of homologous recombination to be used to introduce the homologous recombination template (with no pyrF gene) into the genome such that it also replaces the WT pyrF gene in the genome of a cell.

Inclusion of a gtCas9 and a sgRNA in the homologous recombination construct can be used to introduce double stranded DNA breaks (DSDBs) into bacterial genomes that contain WT pyrF. DSDBs in a bacterial genome typically results in cell death. Therefore, a sgRNA that recognises a sequence in the WT pyrF could result in DSDB and death of cells containing the WT pyrF only. Introduction of DSDB is also dependent on a suitable PAM sequence being located downstream at the 3′ end of the protospacer that is recognised by gtCas9.

The pNW33n plasmid was used as a backbone to clone:


- i) the cas9_(gt) gene under the control of an in-house developed
  glucose repressible promoter; and
- ii) the 1 kb upstream and 1 kb downstream regions of the pyrF gene in
  the genome of *B. smithii* ET138 as a template for homologous
  recombination that would result in deletion of the pyrF gene from the
  genome of *B. smithii* ET138; and
- iii) single guide RNA (sgRNA) expressing module under the
  transcriptional control of a constitutive promoter.

Three separate constructs were generated in which the sequence of the single guide RNAs differed at the first 20 nucleotides, which correspond to the sequence that guides the gtCas9 to its specific DNA target in the genome (also known as the spacer). The three different spacer sequences were designed to target three different candidate protospacers all in the pyrF gene of B. smithii ET138. The constructs are herein referred to as constructs 1, 2 and 3 respectively.

The three different targeted protospacers had at their 3′-end the following candidate PAM sequences:


- 1. TCCATTCC (negative control according to the results of the in vitro
  assays; 3′-end of the protospacer targeted by the sgRNA encoded on
  construct number 3)
- 2. ATCCCCAA (3′-end of the protospacer targeted by the sgRNA encoded
  on construct number 1; \[SEQ ID NO: 21\])
- 3. ACGGCCAA (3′-end of the protospacer targeted by the sgRNA encoded
  on construct number 2, \[SEQ ID NO: 22\])

After transforming B. smithii ET 138 cells with one of the three constructs and plating on selection plates, the following results were obtained:


- - 1. When the cells were transformed with the construct targeting the
    protospacer that had the negative control TCCATTCC PAM sequence at
    the 3′ end (construct number 3) the transformation efficiency was
    not affected (FIG. 12 A). The number of colonies was in the same
    range as the number of colonies after transformation with the pNW33n
    positive control construct (FIG. 12 B). Of the 15 colonies that were
    subjected to colony PCR to screen for colonies in which the pyrF
    gene was deleted, none showed the deletion genotype −2.1 kb expected
    band size—, all were wild-type −2.9 kb expected band size—(FIG. 13).
    This indicates that the tested PAM was indeed not recognised by the
    gtCas9 in vivo.
  - 2. When the cells were transformed with construct number 1 only a
    few colonies were obtained (FIG. 12 C) when compared to the positive
    control (cells transformed with pNW33n). 20 colonies were subjected
    to colony PCR to screen for colonies in which the pyrF gene was
    deleted. The majority (19) of the colonies contained both the wild
    type and pyrF deletion genotype whilst one colonies had a pyrF
    deletion genotype (FIG. 14). This result indicated that the PAM
    sequence ATCCCCAA \[SEQ ID NO: 21\] is recognised in vivo by gtCas9
    because no WT only genotypes were observed. The reduced
    transformation efficiency is also indicative that a proportion of
    the cell population has been reduced, which could be attributable to
    cell death caused of WT only genotype cells by DSDB due to
    successful targeting by gtCas9.
  - 3. When the cells were transformed with construct number 2 no
    colonies were obtained (FIG. 12 D). The lack of colonies is
    indicative that all of the cell population had been successfully
    targeted by the gtCas9, which led to cell death caused by DSDB. This
    suggests that ACGGCCAA \[SEQ ID NO: 22\] PAM sequence is recognised
    by gtCas9.

These results indicate that gtCas9 is active at 55° C. in vivo with the above mentioned PAM sequences, a result that comes in agreement with the in vitro PAM determination results. Moreover it can be used as a genome editing tool at the same temperature in combination with a plasmid borne homologous recombination template.

**Example 10: ThermoCas9 Identification and Purification**

Geobacillus thermodenitrificans strain T12, a Gram positive, moderately thermophilic bacterium with an optimal growth temperature at 65° C. (Daas et al. Biotechnol. Biofuels 9, 210 (2016)) was isolated and sequenced. Contrary to previous claims that type II CRISPR-Cas systems are not present in thermophilic bacteria (Li et al. Nucleic Acids Res. 44, e34-e34 (2016)), the sequencing results revealed the existence of a type-IIC CRISPR-Cas system in the genome of G. thermodenitrificans T12 (FIG. 15A). The Cas9 endonuclease of this system (ThermoCas9) was predicted to be relatively small (1082 amino acids) compared to other Cas9 orthologues, such as SpCas9 (1368 amino acids). The size difference is mostly due to a truncated REC lobe, as has been demonstrated for other small Cas9 orthologues (FIG. 19) (Ran et al. Nature 520, 186-191 (2015)). Furthermore, ThermoCas9 was expected to be active at least around the temperature optimum of G. thermodenitrificans T12 (Daas et al. Biotechnol. Biofuels 9, 210 (2016)). Using the ThermoCas9 sequence as query, BLAST-P searches were performed in the NCBI/non-redundant protein sequences dataset, and a number of highly identical Cas9 orthologues were found (87-99% identity at protein level, Table 1), mostly within the Geobacillus genus, supporting the idea that ThermoCas9 is part of a highly conserved defense system of thermophilic bacteria (FIG. 15B). These characteristics suggested it may be a potential candidate for exploitation as a genome editing and silencing tool for thermophilic microorganisms, and for conditions at which enhanced protein robustness is required.

In silico prediction of the crRNA and tracrRNA modules of the G. thermodenitrificans T12 CRISPR-Cas system was performed using a previously described approach (Mougiakos et al. Trends Biotechnol. 34, 575-587 (2016); Ran et al. Nature 520, 186-191 (2015)). Based on this prediction, a 190 nt sgRNA chimera was designed by linking the predicted full size crRNA (30 nt long spacer followed by 36 nt long repeat) and tracrRNA (36 nt long anti-repeat followed by a 88 nt sequence with three predicted hairpin structures). ThermoCas9 was heterologously expressed in E. coli and purified to homogeneity. Hypothesizing that the loading of the sgRNA to the ThermoCas9 would stabilize the protein, incubated purified apo-ThermoCas9 and ThermoCas9 loaded with in vitro transcribed sgRNA were incubated at 60° C. and 65° C., for 15 and 30 min. SDS-PAGE analysis showed that the purified ThermoCas9 denatures at 65° C. but not at 60° C., while the denaturation temperature of ThermoCas9-sgRNA complex is above 65° C. (FIG. 15C). The demonstrated thermostability of ThermoCas9 implied its potential as a thermo-tolerant CRISPR-Cas9 genome editing tool, and encouraged us to analyze some relevant molecular features in more detail.

**Example 11: ThermoCas9 PAM Determination**

The first step towards the characterization of ThermoCas9 was the in silico prediction of its PAM preferences for successful cleavage of a DNA target. The 10 spacers of the G. thermodenitrificans T12 CRISPR locus were used to search for potential protospacers in viral and plasmid sequences using CRISPRtarget (Biswas et al. RNA Biol. 10, 817-827 (2013)). As only two hits were obtained with phage genomes (FIG. 20A), it was decided to proceed with an in vitro PAM determination approach. The predicted sgRNA sequence that contained a spacer for ThermoCas9-based targeting linear dsDNA substrates was transcribed with a matching protospacer. The protospacer was flanked at its 3′-end by randomized 7-base pair (bp) sequences. After performing ThermoCas9-based cleavage assays at 55° C., the cleaved members of the library (together with a non-targeted library sample as control) were deep-sequenced and compared in order to identify the ThermoCas9 PAM preference (FIG. 16A). The sequencing results revealed that ThermoCas9 introduces double stranded DNA breaks that, in analogy to mesophilic Cas9 variants, are located mostly between the 3rd and the 4th PAM proximal nucleotides. Moreover, the cleaved sequences revealed that ThermoCas9 recognizes a 5′-NNNNCNR-3′ PAM, with subtle preference for cytosine at the 1st, 3rd, 4th and 6th PAM positions (FIG. 16B). Recent studies have revealed the importance of the 81h PAM position for target recognition of certain Type IIC Cas9 orthologues (Karvelis et al. Genome Biol. 16, 253 (2015); Kim et al. Genome Res. 24, 1012-9 (2014)). For this purpose, and taking into account the results from the in silico ThermoCas9 PAM prediction, additional PAM determination assays were performed. This revealed optimal targeting efficiency in the presence of an adenine at the 8th PAM position (FIG. 16C). Interestingly, despite the limited number of hits, the aforementioned in silico PAM prediction (FIG. 20B) also suggested the significance of a cytosine at the 5th and an adenine at the 8th PAM positions.

To further clarify the ambiguity of the PAM at the 6th and 7th PAM positions, a set of 16 different target DNA fragments were generated in which the matching protospacer was flanked by 5′-CCCCCNNA-3′ [SEQ ID NO: 13] PAMs. Cleavage assays of these fragments (each with a unique combination of the 6th and 7th nucleotide) were performed in which the different components (ThermoCas9, sgRNA guide, dsDNA target) were pre-heated separately at different temperatures (20, 30, 37, 45, 55 and 60° C.) for 10 min before combining and incubating them for 1 hour at the corresponding assay temperature. When the assays were performed at temperatures between 37° C. and 60° C., all the different DNA substrates were cleaved (FIG. 16D, FIG. 21). However, the most digested target fragments consisted of PAM sequences (5th to 8th PAM positions) 5′-CNAA-3′ and 5′-CMCA-3′, whereas the least digested targets contained a 5′-CAKA-3′ PAM. At 30° C., only cleavage of the DNA substrates with the optimal PAM sequences (5th to 8th PAM positions) 5′-CNAA-3′ and 5′-CMCA-3′ was observed (FIG. 2D). Lastly, at 20° C. only the DNA substrates with (5th to 8th PAM positions) 5′-CVAA-3′ and 5′-CCCA PAM sequences were targeted (FIG. 21), making these sequences the most preferred PAMs. These findings demonstrate that at its lower temperature limit, ThermoCas9 only cleaves fragments with a preferred PAM. This characteristic could be exploited during in vivo editing processes, for e.g. to avoid off-target effects.

**Example 12: Thermostability and Truncations**

The predicted tracrRNA consists of the anti-repeat region followed by three hairpin structures (FIG. 17A). Using the tracrRNA along with the crRNA to form a sgRNA chimera resulted in successful guided cleavage of the DNA substrate. It was observed that a 41-nt long deletion of the spacer distal end of the full-length repeat-anti-repeat hairpin (FIG. 17A), most likely better resembling the dual guide's native state, had little to no effect on the DNA cleavage efficiency. The effect of further truncation of the predicted hairpins (FIG. 17A) on the cleavage efficiency of ThermoCas9 was evaluated by performing a cleavage time-series in which all the components (sgRNA, ThermoCas9, substrate DNA) were pre-heated separately at different temperatures (37-65° C.) for 1, 2 and 5 min before combining and incubating them for 1 hour at various assay temperatures (37-65° C.). The number of predicted stem-loops of the tracrRNA scaffold seemed to play a crucial role in DNA cleavage; when all three loops were present, the cleavage efficiency was the highest at all tested temperatures, whereas the efficiency decreased upon removal of the 3′ hairpin (FIG. 17B). Moreover, the cleavage efficiency drastically dropped upon removal of both the middle and the 3′ hairpins (FIG. 22). Whereas pre-heating ThermoCas9 at 65° C. for 1 or 2 min resulted in detectable cleavage, the cleavage activity was abolished after 5 min incubation. The thermostability assay showed that sgRNA variants without the 3′ stem-loop result in decreased stability of the ThermoCas9 protein at 65° C., indicating that a full length tracrRNA is required for optimal ThermoCas9-based DNA cleavage at elevated temperatures. Additionally, we also varied the lengths of the spacer sequence (from 25 to 18 nt) and found that spacer lengths of 23, 21, 20 and 19 cleaved the targets with the highest efficiency. The cleavage efficiency drops significantly when a spacer of 18 nt is used.

In vivo, the ThermoCas9:sgRNA RNP complex is probably formed within minutes. Together with the above findings, the activity and thermostability of the RNP was evaluated. Pre-assembled RNP complex was heated at 60, 65 and 70° C. for 5 and 10 min before adding pre-heated DNA and subsequent incubation for 1 hour at 60, 65 and 70° C. Strikingly, the ThermoCas9 RNP was active up to 70° C., in spite of its pre-heating for 5 min at 70° C. (FIG. 17C). This finding confirmed our assumption that the ThermoCas9 stability strongly correlates with the association of an appropriate sgRNA guide (Ma et al., Mol. Cell 160, 398-407 (2015)). It would be advantageous in some applications for the ThermoCas9 to have a broad temperature activity range, that is, to be functional at both low and high temperatures. Also, in some circumstances, it would be advantageous if the activity of the ThermoCas9 could be restricted to narrower temperature ranges, for example, active at only low or only high temperatures. Consequently, the ability to manipulate the range of temperatures at which ThermoCas9 is capable of targeted cleavage or binding or at which targeted cleavage or binding takes place efficiently, by modifying structural features of ThermoCas9 or associated elements (such as the sgRNA), would enable a greater level of control to be exerted over nucleic acid sequence manipulation. Hence, we set out to compare the ThermoCas9 temperature range to that of the Streptococcus pyogenes Cas9 (SpCas9). Both Cas9 homologues were subjected to in vitro activity assays between 20 and 65° C. Both proteins were incubated for 5 min at the corresponding assay temperature prior to the addition of the sgRNA and the target DNA molecules. In agreement with previous analysis, the mesophilic SpCas9 was active only between 25 and 44° C. (FIG. 17D); above these temperature SpCas9 activity rapidly decreased to undetectable levels. In contrast, ThermoCas9 cleavage activity could be detected between 25 and 65° C. (FIG. 17D). This indicates the potential to use ThermoCas9 as a genome editing tool for both thermophilic and mesophilic organisms.

Previously characterized, mesophilic Cas9 endonucleases employ divalent cations to catalyze the generation of DSBs in target DNA (Jinek et al. Science 337, 816-821 (2012); Chen et al. J. Biol. Chem. 289, 13284-13294 (2014)). To evaluate which cations contribute to DNA cleavage by ThermoCas9, plasmid cleavage assays were performed in the presence of one of the following divalent cations: Mg2+, Ca2+, Mn2+, Co2+, Ni2+, and Cu2+; an assay with the cation-chelating agent EDTA was included as negative control. As expected, target dsDNA was cleaved in the presence of divalent cations and remained intact in the presence of EDTA (FIG. 23A). Based on reports that certain type-IIC systems were efficient single stranded DNA cutters (Ma et al. Mol. Cell 60, 398-407 (2015); Zhang et al. Mol. Cell 60, 242-255 (2015)), we tested the activity of ThermoCas9 on ssDNA substrates. However, no cleavage was observed, indicating that ThermoCas9 is a dsDNA nuclease (FIG. 23B).

**Example 13: ThermoCas9-Based Gene Deletion in the Thermophile B. smithii**

ThermoCas9 is used as a genome editing tool for thermophilic bacteria. Here it is shown in Bacillus smithii ET 138 cultured at 55° C. In order to use a minimum of genetic parts a single plasmid approach was used. A set of pNW33n-based pThermoCas9 plasmids was produced containing the thermocas9 gene under the control of the native xylL promoter (PxylL), also a homologous recombination template for repairing Cas9-induced double stranded DNA breaks within a gene of interest, and a sgRNA expressing module under control of the constitutive pta promoter (Ppta) from Bacillus coagulans (FIG. 4A).

The first goal was the deletion of the full length pyrF gene from the genome of B. smithii ET 138. The pNW33n-derived plasmids pThermoCas9_bsΔpyrF1 and pThermoCas9_bsΔpyrF2 were used for expression of different ThermoCas9 guides with spacers targeting different sites of the pyrF gene, while a third plasmid (pThermoCas9_ctrl) contained a random non-targeting spacer in the sgRNA expressing module. Transformation of B. smithii ET 138 competent cells at 55° C. with the control plasmids pNW33n (no guide) and pThermoCas9_ ctrl resulted in the formation of ˜200 colonies each. Out of 10 screened pThermoCas9_ ctrl colonies, none contained the ΔpyrF genotype, confirming findings from previous studies that homologous recombination in B. smithii ET 138 is not sufficient to obtain clean mutants (Mougiakos et al. ACS Synth. Biol. 6, 849-861 (2017); Bosma et al. Microb. Cell Fact. 14, 99 (2015)). In contrast, transformation with the pThermoCas9_bsΔpyrF1 and pThermoCas9_bsΔpyrF2 plasmids resulted in 20 and 0 colonies respectively, confirming the in vivo activity of ThermoCas9 at 55° C. and verifying the above described broad in vitro temperature range of the protein. Out of ten pThermoCas9_ΔpyrF1 colonies screened, one was a clean ΔpyrF mutant whereas the rest had a mixed wild type/ΔpyrF genotype (FIG. 4B), proving the applicability of the system, as the designed homology directed repair of the targeted pyrF gene was successful. Nonetheless, in the tightly controlled SpCas9-based counter-selection system we previously developed the pyrF deletion efficiency was higher (Olson et al., Curr. Opin. Biotechnol. 33, 130-141 (2015)). The low number of obtained transformants and clean mutants in the ThermoCas9-based tool can be explained by the low homologous recombination efficiency in B. smithii (Olson et al., Curr. Opin. Biotechnol. 33, 130-141 (2015)) combined with the constitutive expression of highly active ThermoCas9. It is anticipated that the use of a tightly controllable promoter will increase efficiencies.

**Example 14: ThermoCas9-Based Gene Deletion in the Mesophile Pseudomonas putida**

To broaden the applicability of the ThermoCas9-based genome editing tool, and to evaluate whether in vitro results could be confirmed in vivo, its activity in the mesophilic Gram-negative bacterium P. putida KT2440 was evaluated by combining homologous recombination and ThermoCas9-based counter-selection. For this organism, a Cas9-based tool has not been reported to date. Once more, we followed a single plasmid approach. We constructed the pEMG-based pThermoCas9_ppΔpyrF plasmid containing the thermocas9 gene under the control of the 3-methylbenzoate-inducible Pm-promoter, a homologous recombination template for deletion of the pyrF gene and a sgRNA expressing module under the control of the constitutive P3 promoter. After transformation of P. putida KT2440 cells and PCR confirmation of plasmid integration, a colony was inoculated in selective liquid medium for overnight culturing at 37° C. The overnight culture was used for inoculation of selective medium and ThermoCas9 expression was induced with 3-methylbenzoate. Subsequently, dilutions were plated on non-selective medium, supplemented with 3-methylbenzoate. For comparison, a parallel experiment without inducing ThermoCas9 expression with 3-methylbenzoate was performed. The process resulted in 76 colonies for the induced culture and 52 colonies for the non-induced control culture. For the induced culture, 38 colonies (50%) had a clean deletion genotype and 6 colonies had mixed wild-type/deletion genotype. On the contrary, only 1 colony (2%) of the non-induced culture had the deletion genotype and there were no colonies with mixed wild-type/deletion genotype retrieved (FIG. 24). These results show that ThermoCas9 can be used as an efficient counter-selection tool in the mesophile P. putida KT2440 when grown at 37° C.

**Example 15: ThermoCas9-Based Gene Silencing**

An efficient thermoactive transcriptional silencing CRISPRi tool is currently not available. Such a system could be useful in a number of applications. For example, such a system would greatly facilitate metabolic studies of thermophiles. A catalytically dead variant of ThermoCas9 could serve this purpose by steadily binding to DNA elements without introducing dsDNA breaks. To this end, we identified the RuvC and HNH catalytic domains of ThermoCas9 and introduced the corresponding D8A and H582A mutations for creating a dead (d) ThermoCas9. After confirmation of the designed sequence, Thermo-dCas9 was heterologously produced, purified and used for an in vitro cleavage assay with the same DNA target as used in the aforementioned ThermoCas9 assays; no cleavage was observed confirming the catalytic inactivation of the nuclease.

Towards the development of a Thermo-dCas9-based CRISPRi tool, we aimed for the transcriptional silencing of the highly expressed ldhL gene from the genome of B. smithii ET138. We constructed the pNW33n-based vectors pThermoCas9i_ldhL and pThermoCas9i_ctrl. Both vectors contained the thermo-dCas9 gene under the control of PxylL promoter and a sgRNA expressing module under the control of the constitutive Pima promoter (FIG. 4C). The pThermoCas9i_ldhL plasmid contained a spacer for targeting the non-template DNA strand at the 5′ end of the 138 ldhL gene in B. smithii ET 138 (FIG. S7). The position and targeted strand selection were based on previous studies (Bikard et al. Nucleic Acids Res. 41, 7429-7437 (2013); Larson et al. Nat. Protoc. 8, 2180-2196 (2013)), aiming for the efficient down-regulation of the ldhL gene. The pThermoCas9i_ctrl plasmid contained a random non-targeting spacer in the sgRNA-expressing module. The constructs were used to transform B. smithii ET 138 competent cells at 55° C. followed by plating on LB2 agar plates, resulting in equal amounts of colonies. Two out of the approximately 700 colonies per construct were selected for culturing under microaerobic lactate-producing conditions for 24 hours, as described previously (Bosma et al. Appl. Environ. Microbiol. 81, 1874-1883 (2015)). The growth of the pThermoCas9i_ldhL cultures was 50% less than the growth of the pThermoCas9i_ctrl cultures (FIG. 4E). We have previously shown that deletion of the ldhL gene leads to severe growth retardation in B. smithii ET 138 due to a lack of Ldh-based NAD+-regenerating capacity under micro-aerobic conditions (Bosma et al. Microb. Cell Fact. 14, 99 (2015)). Thus, the observed decrease in growth is likely caused by the transcriptional inhibition of the ldhL gene and subsequent redox imbalance due to loss of NAD+-regenerating capacity. Indeed, HPLC analysis revealed 40% reduction in lactate production of the ldhL silenced cultures, and RT-qPCR analysis showed that the transcription levels of the ldhL gene were significantly reduced in the pThermoCas9i_ldhL cultures compared to the pThermoCas9i_ctrl cultures (FIG. 4E).

**Example 16: Summary**

Most CRISPR-Cas applications are based on RNA-guided DNA interference by Class 2 CRISPR-Cas proteins, such as Cas9 and Cas12a (Komor et al., Cell 168, 20-36 (2017); Puchta, Curr. Opin. Plant Biol. 36, 1-8 (2017); Xu et al. J. Genet. Genomics 42, 141-149 (2015); Tang et al. Nat. Plants 3, 17018 (2017); Zetsche et al. Nat. Biotechnol. 35, 31-34 (2016); Mougiakos et al., Trends Biotechnol. 34, 575-587 (2016)). Prior to this work, no Class 2 CRISPR-Cas immune systems were identified and characterized in thermophilic microorganisms, in contrast to the highly abundant Class 1 CRISPR-Cas systems present in thermophilic bacteria and archaea (Makarova et al., Nat. Rev. Microbiol. 13, 722-736 (2015); Weinberger et al., MBio 3, e00456-12 (2012)), a few of which have been used for genome editing of thermophiles (Li et al. Nucleic Acids Res. 44, e34-e34 (2016)). As a result, the application of CRISPR-Cas technologies was mainly restricted to temperatures below 42° C., due to the mesophilic nature of the employed Cas-endonucleases. Hence, this has excluded application of these technologies in obligate thermophiles and in experimental approaches that require elevated temperatures and/or improved protein stability.

The inventors have characterized ThermoCas9, a Cas9 orthologue from the thermophilic bacterium G. thermodenitrificans T12, a strain that we previously isolated from compost (Daas et al., Biotechnol. Biofuels 9, 210 (2016)). Data mining revealed additional Cas9 orthologues in the genomes of other thermophiles, which were nearly identical to ThermoCas9, for the first time showing that CRISPR-Cas type II systems do exist in thermophiles, at least in some branches of the Bacillus and Geobacillus genera. The inventors have shown that ThermoCas9 is active in vitro in a wide temperature range of 20-70° C., which is much broader than the 25-44° C. range of its mesophilic orthologue SpCas9. The extended activity and stability of ThermoCas9 allows for its application in molecular biology techniques that require DNA manipulation at temperatures of 20-70° C., as well as its exploitation in harsh environments that require robust enzymatic activity. Furthermore, the inventors have identified several factors that are important for conferring the thermostability of ThermoCas9. Firstly, the inventors have demonstrated that the PAM preferences of ThermoCas9 are very strict for activity in the lower part of the temperature range 30° C.), whereas more variety in the PAM is allowed for activity at the moderate to optimal temperatures (37-60° C.). Secondly, the inventors have demonstrated that ThermoCas9 activity and thermostability strongly depends on the association with an appropriate sgRNA guide. Without wishing to be bound by any particular theory, the inventors hypothesise that this stabilization of the multi-domain Cas9 protein is most likely the result of a major conformational change from an open/flexible state to a rather compact state, as described for SpCas9 upon guide binding (Jinek et al. Science 343, 1247997-1247997 (2014)).

Based on the here described characterization of the novel ThermoCas9, the inventors have successfully developed genome engineering tools for strictly thermophilic prokaryotes. We showed that ThermoCas9 is active in vivo at 55° C. and 37° C. and we adapted the current Cas9-based engineering technologies for the thermophile B. smithii ET 138 and the mesophile P. putida KT2440. Due to the wide temperature range of ThermoCas9, it is anticipated that the simple, effective and single plasmid-based ThermoCas9 approach will be suitable for a wide range of thermophilic and mesophilic microorganisms that can grow at temperatures from 37° C. up to 70° C. This complements the existing mesophilic technologies, allowing their use for a large group of organisms for which these efficient tools were thus far unavailable.

Screening natural resources for novel enzymes with desired traits is unquestionably valuable. Previous studies have suggested that the adaptation of a mesophilic Cas9 orthologue to higher temperatures, with directed evolution and protein engineering, would be the best approach towards the construction of a thermophilic Cas9 protein. Instead, we identified a Glade of Cas9 in some thermophilic bacteria, and transformed one of these thermostable ThermoCas9 variants into a powerful genome engineering tool for both thermophilic and mesophilic organisms. With this study, we further stretched the potential of the Cas9-based genome editing technologies and open new possibilities for using Cas9 technologies in novel applications under harsh conditions or requiring activity over a wide temperature range.

**Example 17: Materials and Methods**

a. Bacterial Strains and Growth Conditions

The moderate thermophile B. smithii ET 138 ΔsigF ΔhsdR (Mougiakos, et al., (2017) ACS Synth. Biol. 6, 849-861) was used for the gene editing and silencing experiments using ThermoCas9. It was grown in LB2 medium (Bosma, et al. Microb. Cell Fact. 14, 99 (2015)) at 55° C. For plates, 30 g of agar (Difco) per liter of medium was used in all experiments. If needed chloramphenicol was added at the concentration of 7 μg/mL. For protein expression, E. coli Rosetta (DE3) was grown in LB medium in flasks at 37° C. in a shaker incubator at 120 rpm until an OD600 nm of 0.5 was reached after the temperature was switched to 16° C. After 30 min, expression was induced by addition of isopropyl-1-thio-β-d-gal-actopyranoside (IPTG) to a final concentration of 0.5 mM, after which incubation was continued at 16° C. For cloning PAM constructs for 6th and 7th, and 8th positions, DH5-alpha competent E. coli (NEB) was transformed according to the manual provided by the manufacturer and grown overnight on LB agar plates at 37° C. For cloning degenerate 7-nt long PAM library, electro-competent DH10B E. coli cells were transformed according to standard procedures (Sambrook, Fritsch & Maniatis, T. Molecular cloning: a laboratory manual. (Cold Spring Harbor Laboratory, 1989) and grown on LB agar plates at 37° C. overnight. E. coli DH5α λpir (Invitrogen) was used for P. putida plasmid construction using the transformation procedure described by Ausubel et al. (Current Protocols in Molecular Biology. (John Wiley & Sons, Inc., 2001). doi:10.1002/0471142727). For all E. coli strains, if required chloramphenicol was used in concentrations of 25 mg/L and kanamycin in 50 mg/L. Pseudomonas putida KT2440 (DSM 6125) strains were cultured at 37° C. in LB medium unless stated otherwise. If required, kanamycin was added in concentrations of 50 mg/L and 3-methylbenzoate in a concentration of 3 mM.

b. ThermoCas9 Expression and Purification

ThermoCas9 was PCR-amplified from the genome of G. thermodenitrificans T12, then cloned and heterologously expressed in E. coli Rosetta (DE3) and purified using FPLC by a combination of Ni2+-affinity, anion exchange and gel filtration chromatographic steps. The gene sequence was inserted into plasmid pML-1B (obtained from the UC Berkeley MacroLab, Addgene #29653) by ligation-independent cloning using oligonucleotides (Table 2) to generate a protein expression construct encoding the ThermoCas9 polypeptide sequence (residues 1-1082) fused with an N-terminal tag comprising a hexahistidine sequence and a Tobacco Etch Virus (TEV) protease cleavage site. To express the catalytically inactive ThermoCas9 protein (Thermo-dCas9), the D8A and H582A point mutations were inserted using PCR and verified by DNA sequencing.

The proteins were expressed in E. coli Rosetta 2 (DE3) strain. Cultures were grown to an OD600 nm of 0.5-0.6. Expression was induced by the addition of IPTG to a final concentration of 0.5 mM and incubation was continued at 16° C. overnight. Cells were harvested by centrifugation and the cell pellet was resuspended in 20 mL of Lysis Buffer (50 mM sodium phosphate pH 8, 500 mM NaCl, 1 mM DTT, 10 mM imidazole) supplemented with protease inhibitors (Roche cOmplete, EDTA-free) and lysozyme. Once homogenized, cells were lysed by sonication (Sonoplus, Bandelin) using a using an ultrasonic MS72 microtip probe (Bandelin), for 5-8 minutes consisting of 2 s pulse and 2.5 s pause at 30% amplitude and then centrifuged at 16,000×g for 1 hour at 4° C. to remove insoluble material. The clarified lysate was filtered through 0.22 micron filters (Mdi membrane technologies) and applied to a nickel column (Histrap HP, GE Lifesciences), washed and then eluted with 250 mM imidazole. Fractions containing ThermoCas9 were pooled and dialyzed overnight into the dialysis buffer (250 mM KCl, 20 mM HEPES/KOH, and 1 mM DTT, pH 7.5). After dialysis, sample was diluted 1:1 in 10 mM HEPES/KOH pH 8, and loaded on a heparin FF column pre-equilibrated in IEX-A buffer (150 mM KCl, 20 mM HEPES/KOH pH 8). Column was washed with IEX-A and then eluted with a gradient of IEX-C (2M KCl, 20 mM HEPES/KOH pH 8). The sample was concentrated to 700 μL prior to loading on a gel filtration column (HiLoad 16/600 Superdex 200) via FPLC (AKTA Pure). Fractions from gel filtration were analysed by SDS-PAGE; fractions containing ThermoCas9 were pooled and concentrated to 200 μL (50 mM sodium phosphate pH 8, 2 mM DTT, 5% glycerol, 500 mM NaCl) and either used directly for biochemical assays or frozen at −80° C. for storage.

c. In Vitro Synthesis of sgRNA

The sgRNA module was designed by fusing the predicted crRNA and tracrRNA sequences with a 5′-GAAA-3′ linker. The sgRNA-expressing DNA sequence was put under the transcriptional control of the T7 promoter. It was synthesized (Baseclear, Leiden, The Netherlands) and provided in the pUC57 backbone. All sgRNAs used in the biochemical reactions were synthesized using the HiScribe™ T7 High Yield RNA Synthesis Kit (NEB). PCR fragments coding for sgRNAs, with the T7 sequence on the 5′ end, were utilized as templates for in vitro transcription reaction. T7 transcription was performed for 4 hours. The sgRNAs were run and excised from urea-PAGE gels and purified using ethanol precipitation.

d. In Vitro Cleavage Assay

In vitro cleavage assays were performed with purified recombinant ThermoCas9. ThermoCas9 protein, the in vitro transcribed sgRNA and the DNA substrates (generated using PCR amplification using primers described in Table 2) were incubated separately (unless otherwise indicated) at the stated temperature for 10 min, followed by combining the components together and incubating them at the various assay temperatures in a cleavage buffer (100 mM sodium phosphate buffer (pH=7), 500 mM NaCl, 25 mM MgCl2, 25 (V/V %) glycerol, 5 mM dithiothreitol (DTT)) for 1 hour. Each cleavage reaction contained 160 nM of ThermoCas9 protein, 4 nM of substrate DNA, and 150 nM of synthetized sgRNA. Reactions were stopped by adding 6× loading dye (NEB) and run on 1.5% agarose gels. Gels were stained with SYBR safe DNA stain (Life Technologies) and imaged with a Gel Doc™ EZ gel imaging system (Bio-rad).

e. Library Construction for In Vitro PAM Screen

For the construction of the PAM library, a 122-bp long DNA fragment, containing the protospacer and a 7-bp long degenerate sequence at its 3′-end, was constructed by primer annealing and Klenow fragment (exo-) (NEB) based extension. The PAM-library fragment and the pNW33n vector were digested by BspHI and BamHI (NEB) and then ligated (T4 ligase, NEB). The ligation mixture was transformed into electro-competent E. coli DH10B cells and plasmids were isolated from liquid cultures. For the 7 nt-long PAM determination process, the plasmid library was linearized by SapI (NEB) and used as the target. For the rest of the assays the DNA substrates were linearized by PCR amplification.

f. PAM Screening Assay

The PAM screening of thermoCas9 was performed using in vitro cleavage assays, which consisted of (per reaction): 160 nM of ThermoCas9, 150 nM in vitro transcribed sgRNA, 4 nM of DNA target, 4 μl of cleavage buffer (100 mM sodium phosphate buffer pH 7.5, 500 mM NaCl, 5 mM DTT, 25% glycerol) and MQ water up to 20 μl final reaction volume. The PAM containing cleavage fragments from the 55° C. reactions were gel purified, ligated with Illumina sequencing adaptors and sent for Illumina HiSeq 2500 sequencing (Baseclear). Equimolar amount of non-thermoCas9 treated PAM library was subjected to the same process and sent for Illumina HiSeq 2500 sequencing as a reference. HiSeq reads with perfect sequence match to the reference sequence were selected for further analysis. From the selected reads, those present more than 1000 times in the ThermoCas9 treated library and at least 10 times more in the ThermoCas9 treated library compared to the control library were employed for WebLogo analysis (Crooks et al., Genome Res. 14, 1188-1190 (2004)).

g. Editing and Silencing Constructs for B. smithii and P. putida

All the primers and plasmids used for plasmid construction were designed with appropriate overhangs for performing NEBuilder HiFi DNA assembly (NEB), and they are listed in Table 2 and 3 respectively. The fragments for assembling the plasmids were obtained through PCR with Q5 Polymerase (NEB) or Phusion Flash High-Fidelity PCR Master Mix (ThermoFisher Scientific), the PCR products were subjected to 1% agarose gel electrophoresis and they were purified using Zymogen gel DNA recovery kit (Zymo Research). The assembled plasmids were transformed to chemically competent E. coli DH5a cells (NEB), or to E. coli DH5α Δpir (Invitrogen) in the case of P. putida constructs, the latter to facilitate direct vector integration. Single colonies were inoculated in LB medium, plasmid material was isolated using the GeneJet plasmid miniprep kit (ThermoFisher Scientific) and sequence verified (GATC-biotech) and 1 μg of each construct transformed of B. smithii ET 138 electro-competent cells, which were prepared according to a previously described protocol (Bosma, et al. Microb. Cell Fact. 14, 99 (2015)). The MasterPure™ Gram Positive DNA Purification Kit (Epicentre) was used for genomic DNA isolation from B. smithii and P. putida liquid cultures.

For the construction of the pThermoCas9_ctrl, pThermoCas9_bsΔpyrF1 and pThermoCas9_bsΔpyrF2 vectors, the pNW33n backbone together with the ΔpyrF homologous recombination flanks were PCR amplified from the pWUR_Cas9sp1_hr vector (Mougiakos, et al. ACS Synth. Biol. 6, 849-861 (2017)) (BG8191 and BG8192). The native PxylA promoter was PCR amplified from the genome of B. smithii ET 138 (BG8194 and BG8195). The thermocas9 gene was PCR amplified from the genome of G. thermodenitrificans T12 (BG8196 and BG8197). The Ppta promoter was PCR amplified from the pWUR_Cas9sp1_hr vector (Mougiakos, et al. ACS Synth. Biol. 6, 849-861 (2017)) (BG8198 and BG8261_2/BG8263_nc2/BG8317_3). The spacers followed by the sgRNA scaffold were PCR amplified from the pUC57_T7t12sgRNA vector (BG8266_2/BG8268_nc2/8320_3 and BG8210).

A four-fragment assembly was designed and executed for the construction of the pThermoCas9i_ldhL vectors. Initially, targeted point mutations were introduced to the codons of the thermocas9 catalytic residues (mutations D8A and H582A), through a two-step PCR approach using pThermoCas9_ctrl as template. During the first PCR step (BG9075, BG9076), the desired mutations were introduced at the ends of the produced PCR fragment and during the second step (BG9091, BG9092) the produced fragment was employed as PCR template for the introduction of appropriate assembly-overhangs. The part of the thermocas9 downstream the second mutation along with the ldhL silencing spacer was PCR amplified using pThermoCas9_ctrl as template (BG9077 and BG9267). The sgRNA scaffold together with the pNW33n backbone was PCR amplified using pThermoCas9_ctrl as template (BG9263 and BG9088). The promoter together with the part of the thermocas9 upstream the first mutation was PCR amplified using pThermoCas9_ctrl as template (BG9089, BG9090)

A two-fragment assembly was designed and executed for the construction of pThermoCas9i_ctrl vector. The spacer sequence in the pThermoCas9i_ldhL vector was replaced with a random sequence containing Bael restriction sites at both ends. The sgRNA scaffold together with the pNW33n backbone was PCR amplified using pThermoCas9_ctrl as template (BG9548, BG9601). The other half of the construct consisted of Thermo-dCas9 and promoter was amplified using pThermoCas9i_ldhL as template (BG9600, BG9549).

A five-fragment assembly was designed and executed for the construction of the P. putida KT2440 vector pThermoCas9_ppΔpyrF. The replicon from the suicide vector pEMG was PCR amplified (BG2365, BG2366). The flanking regions of pyrF were amplified from KT2440 genomic DNA (BG2367, BG2368 for the 576-bp upstream flank, and BG2369, BG2370 for the 540-bp downstream flank). The flanks were fused in an overlap extension PCR using primers BG2367 and BG2370 making use of the overlaps of primers BG2368 and BG2369. The sgRNA was amplified from the pThermoCas9_ctrl plasmid (BG2371, BG2372). The constitutive P3 promoter was amplified from pSW_I-SceI (BG2373, BG2374). This promoter fragment was fused to the sgRNA fragment in an overlap extension PCR using primers BG2372 and BG2373 making use of the overlaps of primers BG2371 and BG2374. ThermoCas9 was amplified from the pThermoCas9_ctrl plasmid (BG2375, BG2376). The inducible Pm-XylS system, to be used for 3-methylbenzoate induction of ThermoCas9 was amplified from pSW_I-SceI (BG2377, BG2378).

h. Editing Protocol for P. putida

Transformation of the plasmid to P. putida was performed according to Choi et al. (Choi et al., J. Microbiol. Methods 64, 391-397 (2006)). After transformation and selection of integrants, overnight cultures were inoculated. 10 μl of overnight culture was used for inoculation of 3 ml fresh selective medium and after 2 hours of growth at 37° C. ThermoCas9 was induced with 3-methylbenzoate. After an additional 6 h, dilutions of the culture were plated on non-selective medium supplemented with 3-methylbenzoate. For the control culture the addition of 3-methylbenzoate was omitted in all the steps. Confirmation of plasmid integration in the P. putida chromosome was done by colony PCR with primers BG2381 and BG2135. Confirmation of pyrF deletion was done by colony PCR with primers BG2381 and BG2382.

i. RNA Isolation

RNA isolation was performed by the phenol extraction based on a previously described protocol (van Hijum et al. BMC Genomics 6, 77 (2005)). Overnight 10 mL cultures were centrifuged at 4° C. and 4816×g for 15 min and immediately used for RNA isolation. After removal of the medium, cells were suspended in 0.5 mL of ice-cold TE buffer (pH 8.0) and kept on ice. All samples were divided into two 2 mL screw-capped tubes containing 0.5 g of zirconium beads, 30 μL of 10% SDS, 30 μL of 3 M sodium acetate (pH 5.2), and 500 μL of Roti-Phenol (pH 4.5-5.0, Carl Roth GmbH). Cells were disrupted using a FastPrep-24 apparatus (MP Biomedicals) at 5500 rpm for 45 s and centrifuged at 4° C. and 10 000 rpm for 5 min. 400 μL of the water phase from each tube was transferred to a new tube, to which 400 μL of chloroform-isoamyl alcohol (Carl Roth GmbH) was added, after which samples were centrifuged at 4° C. and 18 400×g for 3 min. 300 μL of the aqueous phase was transferred to a new tube and mixed with 300 μL of the lysis buffer from the high pure RNA isolation kit (Roche). Subsequently, the rest of the procedure from this kit was performed according to the manufacturer's protocol, except for the DNase incubation step, which was performed for 45 min. The concentration and integrity of cDNA was determined using Nanodrop-1000 Integrity and concentration of the isolated RNA was checked on a NanoDrop 1000.

j. Quantification of mRNA by RT-qPCR

First-strand cDNA synthesis was performed for the isolated RNA using SuperScript™ III Reverse Transcriptase (Invitrogen) according to manufacturer's protocol. qPCR was performed using the PerfeCTa SYBR Green Supermix for iQ from Quanta Biosciences. 40 ng of each cDNA library was used as the template for qPCR. Two sets of primers were used; BG9665:BG9666 amplifying a 150-nt long region of the ldhL gene and BG9889:BG9890 amplifying a 150-nt long sequence of the rpoD (RNA polymerase sigma factor) gene which was used as the control for the qPCR. The qPCR was run on a Bio-Rad C1000 Thermal Cycler.

k. HPLC

A high-pressure liquid chromatography (HPLC) system ICS-5000 was used for lactate quantification. The system was operated with Aminex HPX 87H column from Bio-Rad Laboratories and equipped with a UV1000 detector operating on 210 nm and a RI-150 40° C. refractive index detector. The mobile phase consisted of 0.16 N H2SO4 and the column was operated at 0.8 mL/min. All samples were diluted 4:1 with 10 mM DMSO in 0.01 N H2SO4.

**Example 18 Application of ThermoCas9 in Geobacillus thermoglucosidans**

ThermoCas9 is evaluated as counter selection tool in Geobacillus thermoglucosidans (also known as Bacillus thermoglucosidasius, Geobacillus thermoglucosidasius, and Parageobacillus thermoglucosidasius) at 55° C. A single-plasmid approach was applied, with the recombination arms and the thermoCas9 gene/sgRNA on the same plasmid. The thermoCas9 gene was placed under control of a β-glucosidase promoter that can be induced by cellobiose (Bartosiak-Jentys, J., Hussein, A. H., Lewis, C. J., Leak, D. J. (2013) Microbiology 159:1267-1275). To improve the recombination efficiency, an incubation step at elevated temperature, at which the plasmid cannot replicate, was added to the workflow. The G. thermoglucosidans DSM 2542T 960 bp ldhL gene (NCBI GeneID:29237966) was chosen as deletion target. Upstream and downstream fragments of 0.9 kb were generated by PCR using primer combinations:

both at an annealing temperature of 58° C. and by using chromosomal DNA of G. thermoglucosidans ΔsigF (see International (PCT) Application publication No. WO2016/012296) as a template. The vector backbone was amplified in two parts using pThermoCas9_ctrl, as described in Example 13, as a template, introducing the non-targeting spacer sequence (5′-TTATGTTTTCCGGACATAGTACA-3′). One fragment was generated using primer combination

The other fragment was generated using primer combination

The β-glucosidase promoter was amplified from G. thermoglucosidans ΔsigF (WO2016012296) chromosomal DNA as a template and primer combinations

The five PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions and assembled into a single plasmid by fusing the overlapping regions using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in non-targeting plasmid pRB061.

Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to electrocompetent E. coli TG90 (Gonzy-Treboul, G., Karmzyn-Campelli, C., Stragier, P. 1992. J. Mol. Biol. 224:967-979). Transformants were plated on LB agar plates supplemented with 10 mg/L chloramphenicol and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis.

The plasmid containing the targeting spacer (5′-ATAAGGGCAAATGCATAGCTGGC-3′) based on a genomic sequence with a PAM sequence of 5′-GGCCCCAA-3′ immediately downstream, was constructed by assembly of two fragments amplified by PCR with the non-targeting plasmid pRB061 as a template, using primer combination

Transformation and plasmid extraction were performed as described above resulting in targeting plasmid pRB063.

The plasmids pRB061 and pRB063 were transformed to G. thermoglucosidans ΔsigF (see International (PCT) Application publication No. WO2016/012296) by electroporation as described elsewhere (see WO2016/012296) and plated on TGP plates supplemented with 8 mg/L chloramphenicol. Plates were incubated overnight at 55° C. A single colony was selected and grown overnight at 55° C. in TGP broth supplemented with 8 mg/L chloramphenicol. Subsequently, 1 mL was transferred to 10 mL fresh prewarmed TGP medium supplemented with 8 mg/L chloramphenicol. After an incubation for 8 h to overnight at 68° C., for recombination to occur, 1 mL was transferred to 10 mL fresh prewarmed TGP medium supplemented with 8 mg/L chloramphenicol and 1% (w/v) cellobiose (D(+) cellobiose, Across), to induce the beta-glucosidase promoter, and incubated at 55° C. for 8 h. The cultures were plated at 55° C. on TGP plates containing 1% (w/v) cellobiose. Colony PCR was performed to confirm deletion of the ldhL gene using primers 629 (5′-GACTGGGCGCAAGCGGTGATG-3′) and 630 (5′-CCTGTTGCTGATACAAGGTCTAGC-3′). The construct containing the targeting spacer resulted in 16 knockouts out of the 36 colonies analyzed. The random spacer resulted in 1 knockout out of the 78 colonies analyzed. This demonstrates the efficiency of the counter-selection tool for gene deletion in G. thermoglucosidans.

**Example 19 Application of ThermoCas9 in Bacillus coagulans**

ThermoCas9 was evaluated as counter selection tool in Bacillus coagulans at 55° C. A single-plasmid approach was used, with the recombination arms and the thermoCas9 gene/sgRNA on the same plasmid. The thermoCas9 gene was placed under control of a β-glucosidase promoter that can be induced by cellobiose (Bartosiak-Jentys, J., Hussein, A. H., Lewis, C. J., Leak, D. J. (2013) Microbiology 159:1267-1275). To improve the recombination efficiency an incubation step at elevated temperature, at which the plasmid cannot replicate, was added to the workflow. The B. coagulans DSM 1T 759-bp sigF gene (NCBI GeneID: 29812540) was chosen as deletion target. Upstream and downstream fragments of 0.85 kb were generated by PCR using primer combinations

both at an annealing temperature of 58° C. and by using chromosomal DNA of B. coagulans DSM 1 as a template. The vector backbone was amplified in two parts using pBR061 as a template, introducing the targeting spacer sequence 5′-CGGGGATATGAACCGGATGACTT-3′, based on a genomic sequence with a PAM sequence of 5′-ATTTCAAA-3′. One fragment was generated using primer combination

The other fragment was generated using primer combination

The four PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions, and assembled into a single plasmid by fusing the 25-bp overlapping regions using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in targeting plasmid pMH247. Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to electrocompetent E. coli TG90 (Gonzy-Treboul, G., Karmzyn-Campelli, C., Stragier, P. (1992) J. Mol. Biol. 224:967-979). Transformants were plated on LB agar plates supplemented with 10 mg/L chloramphenicol and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis. The plasmid was transformed to B. coagulans by electroporation as described elsewhere (Kovacs, A. T., van Hartskamp, M., Kuipers, O. P., & van Kranenburg, R. (2010) Applied and Environmental Microbiology, 76(12), 4085-4088) and plated on BC plates supplemented with 7 mg/L chloramphenicol (Kovacs, A. T., van Hartskamp, M., Kuipers, O. P., & van Kranenburg, R. (2010) Applied and Environmental Microbiology, 76(12), 4085-4088). Plates were incubated overnight at 45° C. Two single colonies were selected and grown overnight at 45° C. in BC broth supplemented with 7 mg/L chloramphenicol. Subsequently, 1 ml was transferred to 10 ml fresh, prewarmed BC medium supplemented with 7 mg/L chloramphenicol. After an incubation for 4 h at 65° C., for recombination to occur, the cultures were incubated for 4 hours at 55° C. After this, 1 ml was transferred to 10 ml fresh, prewarmed BC medium supplemented with 7 mg/L chloramphenicol and 1% (w/v) cellobiose, to induce the β-glucosidase promoter, and cultures were incubated overnight at 55° C. The cultures were plated at 55° C. on BC agar plates containing 1% (w/v) cellobiose and colony PCR was performed to check for knockouts using primers 351 (5′-CACCATGTCCCGGACAGCAC-3′) and 352 (5′-GCGATGAAATTGGAACACTGAC-3′). For one culture 17 out of 17 tested colonies had the PCR fragment of 2.1 kb confirming the deletion. For the other culture 15 out of 18 tested colonies had the PCR fragment of 2.1 kb confirming the deletion, the other 3 had the PCR fragment of the wild type. This demonstrates the efficiency of the counter-selection tool for gene deletion in B. coagulans.

**Example 20 Application of ThermoCas9 in Pseudomonas putida Using a Two-Plasmid Approach**

ThermoCas9 is evaluated as counter selection tool in Pseudomonas putida at 30° C. A two-step approach is applied, first integrating the knock-out vector via a single-crossover event and subsequent introduction of the plasmid harbouring the thermoCas9 gene and the sgRNA containing the targeting spacer. The thermoCas9 gene was placed under control of the 3-methylbenzoate inducible Pm promoter. The P. putida KT2440, DSM-6125, 702 bp gene pyrF (NCBI GeneID: 1043286) was chosen as a deletion target, . For the construction of an integration vector the 0.5-kb upstream and 0.5-kb downstream regions of pyrF were amplified by PCR with primer combination

using the pThermoCas9_ppΔpyrF of Example 14 and FIG. 25 as a template. The vector backbone was amplified by PCR using primer combination

using the pEMG suicide vector (Martinez-Garcia, E., de Lorenzo, V. (2012) Methods Mol. Biol. 813:267-283) as a template. The two PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions, using a 58° C. annealing temperature for all reactions, and assembled into a single plasmid by fusion of the vector backbone overlapping regions added to the primers used for the amplification of the upstream and downstream regions, using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in the integration plasmid pRB051. Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to electrocompetent E. coli DH5α λpir (Invitrogen). Transformants were plated on LB agar plates supplemented with 50 mg/L kanamycin and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis. The integration plasmid was transformed to electrocompetent P. putida KT2440 cells as described elsewhere (see Choi, K. H., A Kumar, and H. P. Schweizer. (2006) J. Microbiol. Methods 64: 391-397). Transformants were plated on LB agar plates supplemented with 50 mg/L kanamycin and incubated at 30° C. A single colony was selected for analysis of genomic DNA, isolated using the MasterPure™ DNA Purification Kit (Epicentre). A plasmid integration in the downstream region of pyrF was confirmed by PCR analysis with primers

For a plasmid harboring the ThermoCas9 and corresponding sgRNA elements, a targeting spacer (5′-CCATACCCGCTTTTTCCGCCAGC-3′) based on a genomic sequence followed by a 5′-GCCGCCAA-3′ PAM sequence was selected. The vector backbone, including the 3-methylbenzoate-inducible

Pm-promoter was amplified by PCR with primer combination

using pSW(I-SceI) (Wong, S. M., Mekalanos, J. J. (2000) Proc. Natl. Acad. Sci. USA 97:10191-10196) as a template. The ThermoCas9 and corresponding sgRNA fragment were amplified by PCR with primer combinations

for both using pThermoCas9_ppΔpyrF as a template. The three PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions, using a 58° C. annealing temperature for all reactions, and assembled into a single plasmid by fusion of the overlapping regions, using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in the plasmid pRB054. Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to E. coli DH5a by heat shock (Sambrook, J., en D. W. Russell. (2001) Molecular cloning: a laboratory manual 3rd edition. Cold Spring Harbor Laboratory Press, Cold Spring Harbor, N.Y.). Transformants were plated on LB agar plates supplemented with 150 mg/L ampicillin and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis.

The pRB054 plasmid was transformed to electrocompetent P. putida KT2440 cells with confirmed pRB051 integration. Transformants were plated on LB agar plates supplemented with 50 mg/L kanamycin and 500 mg/L ampicillin and incubated at 30° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis. Also genomic DNA was isolated using the MasterPure™ DNA Purification Kit (Epicentre) and pRB051 integration reconfirmed by PCR analysis with primers 2381 (5′-ACACGGCGGATGCACTTACC-3′) and 2135 (5′-CCGCTTTCTTCGGGCATTCC-3′). Subsequently, 10 μL of an overnight culture of the strain with the targeting plasmid was transferred to 3 mL LB medium supplemented with 50 mg/L kanamycin and 500 mg/L ampicillin. After a shaking incubation (180 r.p.m.) of 2 hours at 30° C., 3-methylbenzoate was added to a final concentration of 3 mM. The cultures were incubated, shaking at 30° C. for an additional 4 hours. The culture was plated on LB agar supplemented with 50 mg/L uracil and incubated at 30° C. After overnight growth 96 colonies were transferred to a fresh LB agar plate supplemented with 50 mg/L uracil and incubated for another night at 30° C. Colony PCRs were performed on all grown colonies to check for knockouts using primers 2381 (5′-ACACGGCGGATGCACTTACC-3′) and 2382 (5′-TGGACGTGTACTTCGACAAC-3′). Of the 48 colonies that were tested, 32 colonies yielded a PCR product. All 32 had a fragment of 1112 bp, corresponding to a gene deletion. One of these colonies also gave a 1854 bp fragment indicating a mixed wild-type/deletion genotype in this colony. This demonstrates the efficiency of ThermoCas9 as a counter-selection tool for gene deletion in P. putida at 30° C.

**Example 21 Application of ThermoCas9 in Saccharomyces cerevisiae**

ThermoCas9 is used as a genome editing tool in the eukaryote Saccharomyces cerevisiae at 37° C. A two-step approach was used: first integrating ThermoCas9 for stable expression from the genome and subsequent introduction of a plasmid harbouring the sgRNA along with a linear double-stranded DNA repair-oligo. The ThermoCas9 gene was placed under control of the constitutive TEF1 promoter, the sgRNA under control of the SNR52 promoter and SUP4 terminator. The S. cerevisiae CEN.PK113-17A (Entian K D, Miner P (1998) Method Microbiol 26:431-449), 1773 bp gene CAN1 (YEL063C; NCBI GeneID: 856646) was chosen as a deletion target.

A ThermoCas9 integration fragment was maintained on a plasmid constructed by assembly of six fragments. The ThermoCas9 fragment was amplified with primer combination:

introducing a nuclear localization signal coding sequence (5′-CCCAAGAAGAAGAGGAAGGTG-3′) fused to the 3′ end of the ThermoCas9 gene prior to the stop codon using the previously described  (see Example 14) as a template. The CYC1 terminator was amplified with primer combination:

using pSF-TEF1-URA3 plasmid (OGS534; Sigma-Aldrich) as a template. The LEU2 locus (YCL018W, Gene ID: 850342) was amplified from genomic DNA of S. cerevisiae CEN.PK113-17A with a repaired LEU2 gene (OrganoBalance) with primer combination:

Alternatively, the gene can be amplified from synthetic DNA based on the S. cerevisiae S288C LEU2 locus (YCL018W, Gene ID: 850342) including the sequences 523 bp upstream and 104 downstream of the gene. The S. cerevisiae ARS replicon was amplified with primer combination:

using the Vector Conversion Cassette with Sapphire™ Technology (GeneArt Cat. no. A13291) as a template. The E. coli pUC replicon was amplified with primer combination:

using pSF-TEF1-URA3 plasmid (OGS534; Sigma-Aldrich) as a template. The fragment with kanamycin resistance marker and TEF1 promoter was amplified with primer combination:

using pSF-TEF1-URA3 plasmid (OGS534; Sigma-Aldrich) as a template. The six PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions and assembled into a single plasmid by fusing the overlapping regions using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in plasmid pRB021. Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to E. coli DH5α by heat-shock (Sambrook, J., en D. W. Russell. 2001. Molecular cloning: a laboratory manual 3rd edition. Cold Spring Harbor Laboratory Press, Cold Spring Harbor, N.Y.). Transformants were plated on LB agar plates supplemented with 50 mg/L kanamycin and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis.

The ThermoCas9 gene was integrated in the S. cerevisiae CEN.PK113-17A TDH1 locus (YJL052W) by amplification of the ThermoCas9-LEU2 fragment by PCR using primer combination:

both with 60 bp tails homologous to either the upstream or downstream region of the TDH1 locus, with pRB021 as a template. The amplified fragment was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O. Circa 500 ng of this fragment was transformed to S. cerevisiae CEN.PK113-17A by heat-shock as described elsewhere (R. Daniel Gietz, Robin A. Woods, Methods in Enzymology, Academic Press, 2002, Volume 350, Pages 87-96). Transformants were plated on SM agar plates (Verduyn, C., E. Postma, W. A. Scheffers, and J. P. van Dijken. 1990. J. Gen. Microbiol. 136:395-403.) supplemented with 150 mg/L uracil and incubated at 30° C. for three days. A single colony was selected for genomic DNA extraction using the YeaStar Genomic DNA Kit (Zymo Research) according to manufacturer's Protocol II. Fragment integration and ThermoCas9 sequence was confirmed by sequence analysis.

A S. cerevisiae CAN1 targeting gRNA with a targeting spacer sequence of 5′-GCACCTGGGTTTCTCCAATAACG-3′, based on a genomic sequence with a PAM sequence of 5′-GAATCCAA-3′ was expressed from a multi-copy plasmid constructed by assembly of three fragments. The SNR promoter was amplified from S. cerevisiae CEN.PK113-17A genomic DNA with primer combination:

The sgRNA cassette, including CAN1 targeting spacer, was amplified using primer combination:

with pThermoCas9_ppΔpyrF as a template. The multicopy backbone was amplified by PCR using primer combination:

using pSF-TEF1-URA3 plasmid (OGS534; Sigma-Aldrich) as a template. The three PCR fragments were created with Phusion Flash High-Fidelity PCR master mix (ThermoFisher) according to the manufacturer's instructions and assembled into a single plasmid by fusing the overlapping regions using the NEBuilder HiFi DNA Assembly Cloning Kit (New England BioLabs) resulting in multi-copy gRNA harbouring plasmid pRB089. Plasmid DNA was concentrated using a Zymo DNA Clean and Concentrator spin column (Zymo Research) and eluted into 10 μL H2O and transformed to E. coli DH5a by heat-shock (Sambrook, J., en D. W. Russell. 2001. Molecular cloning: a laboratory manual 3rd edition. Cold Spring Harbor Laboratory Press, Cold Spring Harbor, N.Y.). Transformants were plated on LB agar plates supplemented with 50 mg/L kanamycin and incubated at 37° C. A single colony was selected for plasmid extraction using the ZymoPURE™ Plasmid Midiprep Kit (Zymo Research). Plasmid integrity was confirmed by sequence analysis.

A repair-oligo consisting of 60 bp upstream and 60 bp downstream of the CAN1 ORF was constructed by annealing primer:

10 μL of 100 mM both primers was combined, boiled at 99° C. for 5 minutes and subsequently allowed to slowly cool down to room temperature.

Circa 100 ng of the sgRNA harbouring plasmid pRB089 was co-transformed with 200 nmol of the annealed CAN1 repair-oligo to the S. cerevisiae tdh1::ThermoCas9-LEU2 strain by heat-shock, with all steps usually performed at 30° C., now performed at 37° C. Transformants were plated on SM agar plates and incubated at 37° C. for four days. 44 colonies were picked and analyzed by colony PCR with primers 2223 (5′-GGTTGCGAACAGAGTAAACC-3′) and 2224 (5′-TCGGGAGCAAGATTGTTGTG-3′). This identified one colony with a 380 bp deletion product, while all other showed a 2153 bp wild-type fragment. This demonstrates ThermoCas9 endonuclease activity in S. cerevisiae and its use in genome editing.

The following section of the description consists of numbered paragraphs simply providing statements of the invention already described herein. The numbered paragraphs in this section are not claims. The claims are set forth below in the later section headed “claims”.

1. An isolated clustered regularly interspaced short palindromic repeat (CRISPR)-associated (Cas) protein or polypeptide comprising;

a. the amino acid motif EKDGKYYC [SEQ ID NO: 2]; and/or

b. the amino acid motif X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and/or

c. the amino acid motif X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and/or

d. the amino acid motif X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and/or

e. the amino acid motif X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine;

wherein the Cas protein is capable of nucleic acid cleavage between 50° C. and 100° C. when associated with at least one targeting RNA molecule, and a polynucleotide comprising a target nucleic acid sequence recognised by the targeting RNA molecule.

2. An isolated Cas protein or polypeptide fragment having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith, wherein the Cas protein is capable of binding, cleaving, modifying or marking a polynucleotide comprising a target nucleic acid sequence at a temperature between 50° C. and 100° C. when associated with at least one RNA molecule which recognizes the target sequence.

3. A Cas protein or polypeptide fragment as in numbered paragraph 1 or 2, wherein the Cas protein or fragment is capable of nucleic acid binding, cleavage, marking or modification at a temperature between 50° C. and 75° C., preferably at a temperature above 60° C.; more preferably at a temperature between 60° C. and 80° C.; more preferably at a temperature between 60° C. and 65° C.

4. A Cas protein or polypeptide fragment as in any of numbered paragraphs 1 to 3, wherein the nucleic acid binding, cleavage, marking or modification is DNA cleavage.

5. A Cas protein or polypeptide fragment as in any preceding numbered paragraph, wherein the amino acid sequence comprises an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith.

6. A Cas protein or polypeptide fragment as in any preceding numbered paragraph, wherein the Cas protein is obtainable from a bacterium, archaeon or virus.

7. A Cas protein or polypeptide fragment as in any preceding numbered paragraph, wherein the Cas protein is obtainable from Geobacillus sp., preferably from Geobacillus thermodenitrificans.

8. A ribonucleoprotein complex comprising a Cas protein as in any preceding numbered paragraph, and comprising at least one targeting RNA molecule which recognises a sequence in a target polynucleotide.

9. A ribonucleoprotein complex as in numbered paragraph 8, wherein the targeting RNA molecule comprises a crRNA and optionally a tracrRNA.

10. A ribonucleoprotein complex as in any of numbered paragraphs 7 to 9, wherein the length of the at least one RNA molecule is in the range 35-135 nucleotide residues.

11. A ribonucleoprotein complex as in numbered paragraph 8 or 9, wherein the target sequence is 31 or 32 nucleotide residues in length.

12. A Cas protein or polypeptide as in any of numbered paragraphs 1 to 7 or a ribonucleoprotein complex as in any of 8 to 11, wherein the protein or polypeptide is provided as part of a protein complex comprising at least one further functional or non-functional protein.

13. A Cas protein, polypeptide, or ribonucleoprotein complex as in numbered paragraph 12, wherein the Cas protein or polypeptide, and/or the at least one further protein further comprise at least one functional moiety.

14. A Cas protein or polypeptide, or ribonucleoprotein complex as in numbered paragraph 13, wherein the at least one functional moiety is fused or linked to the N-terminus and/or the C-terminus of the Cas protein, polypeptide or ribonucleoprotein complex; preferably the N-terminus.

15. A Cas protein or polypeptide, or a ribonucleoprotein complex as in numbered paragraph 13 or 14, wherein the at least one functional moiety is a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag.

16. A Cas protein or polypeptide, or a ribonucleoprotein complex as in numbered paragraph 15, wherein the native activity of the Cas9 nuclease activity is inactivated and the Cas protein is linked to at least one functional moiety.

17. A Cas protein or polypeptide, or a ribonucleoprotein complex as in numbered paragraph 15 or 16, wherein the at least one functional moiety is a nuclease domain; preferably a FokI nuclease domain.

18. A Cas protein or polypeptide, or a ribonucleoprotein complex as in any of numbered paragraphs 15 to 17, wherein the at least one functional moiety is a marker protein, for example GFP.

19. An isolated nucleic acid molecule encoding a Cas protein or polypeptide, comprising;

a. the amino acid motif EKDGKYYC [SEQ ID NO: 2]; and/or

b. the amino acid motif X1X2CTX3X4 [SEQ ID NO: 3] wherein X1 is independently selected from Isoleucine, Methionine or Proline, X2 is independently selected from Valine, Serine, Asparagine or Isoleucine, X3 is independently selected from Glutamate or Lysine and X4 is one of Alanine, Glutamate or Arginine; and/or

c. the amino acid motif X5LKX6IE [SEQ ID NO: 4] wherein X5 is independently selected from Methionine or Phenylalanine and X6 is independently selected from Histidine or Asparagine; and/or

d. the amino acid motif X7VYSX8K [SEQ ID NO: 5] wherein X7 is Glutamate or Isoleucine and X8 is one of Tryptophan, Serine or Lysine; and/or

e. the amino acid motif X9FYX10X11REQX12KEX13 [SEQ ID NO: 6] wherein X9 is Alanine or Glutamate, X10 is Glutamine or Lysine, X11 is Arginine or Alanine, X12 is Asparagine or Alanine and X13 is Lysine or Serine;

wherein the Cas protein or polypeptide is capable of DNA binding, cleavage, marking or modification between 50° C. and 100° C. when associated with at least one targeting RNA molecule, and a polynucleotide comprising a target nucleic acid sequence recognised by the targeting RNA molecule.

20. An isolated nucleic acid molecule encoding a clustered regularly interspaced short palindromic repeat (CRISPR)-associated (Cas) protein having an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith; or a polypeptide fragment thereof.

21. An isolated nucleic acid molecule as in numbered paragraph 19 or 20, further comprising at least one nucleic acid sequence encoding an amino acid sequence which upon translation is fused with the Cas protein or polypeptide.

22. An isolated nucleic acid molecule as in numbered paragraph 21, wherein the at least one nucleic acid sequence fused to the nucleic acid molecule encoding the Cas protein or polypeptide, encodes a protein selected from a protein selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag.

23. An expression vector comprising a nucleic acid molecule as in any of numbered paragraphs 19 to 22.

24. An expression vector as in numbered paragraph 23, further comprising a nucleotide sequence encoding at least one targeting RNA molecule.

25. A method of modifying a target nucleic acid comprising contacting the nucleic acid with:

a. a ribonucleoprotein complex of any of numbered paragraphs 6 to 11; or

b. a protein or protein complex of any of numbered paragraphs 12 to 18 and at least one targeting RNA molecule as defined in any of numbered paragraphs 6 to 11; and wherein said method is not used in human cells.

26. A method of modifying a target nucleic acid in a non-human cell, comprising transforming, transfecting or transducing the cell with an expression vector of numbered paragraph 24; or alternatively transforming, transfecting or transducing the cell with an expression vector of numbered paragraph 23 and a further expression vector comprising a nucleotide sequence encoding a targeting RNA molecule as defined in any of numbered paragraphs 6 to 11.

27. A method of modifying a target nucleic acid in a non-human cell comprising transforming, transfecting or transducing the cell with an expression vector of numbered paragraph 23, and then delivering a targeting RNA molecule as defined in any of numbered paragraphs 6 to 11 to or into the cell.

28. A method of modifying a target nucleic acid as in any of numbered paragraphs 25 to 28, wherein the at least one functional moiety is a marker protein or reporter protein and the marker protein or reporter protein associates with the target nucleic acid; preferably wherein the marker is a fluorescent protein, for example a green fluorescent protein (GFP).

29. A method as in any of numbered paragraphs 25 to 28, wherein the target nucleic acid is DNA; preferably dsDNA.

30. A method as in any of numbered paragraphs 25 to 28, wherein the target nucleic acid is RNA.

31. A method of modifying a target nucleic acid as in numbered paragraph 29, wherein the nucleic acid is dsDNA, the at least one functional moiety is a nuclease or a helicase-nuclease, and the modification is a single-stranded or a double-stranded break at a desired locus.

32. A method of silencing gene expression at a desired locus according to any of the methods in any of numbered paragraphs 26, 27, 29 or 31.

33. A method of modifying or deleting and/or inserting a desired nucleotide sequence at a desired location according to any of the methods as in any of numbered paragraphs 26, 27, 29 or 31.

34. A method of modifying gene expression in a non-human cell comprising modifying a target nucleic acid sequence as in a method of any of numbered paragraphs 25 to 29; wherein the nucleic acid is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor.

35. A method of modifying gene expression in a non-human cell comprising modifying a target nucleic acid sequence as in a method of numbered paragraph 30, wherein the nucleic acid is an mRNA and the functional moiety is a ribonuclease; optionally selected from an endonuclease, a 3′ exonuclease or a 5′ exonuclease.

36. A method of modifying a target nucleic acid as in any of numbered paragraphs 25 to 35, wherein the method is carried out at a temperature between 50° C. and 100° C.

37. A method of modifying a target nucleic acid as in numbered paragraph 36, wherein the method is carried out at a temperature at or above 60° C., preferably between 60° C. and 80° C., more preferably between 60° C. and 65° C.

38. A method as in any of numbered paragraphs 25 to 37 wherein the cell is a prokaryotic cell.

39. A method as in any of numbered paragraphs 25 to 38 wherein the cell is a eukaryotic cell.

40. A host cell transformed by a method as in any of numbered paragraphs 22 to 36; wherein the cell is not a human cell.

The following section of the description consists of further numbered paragraphs simply providing statements of the invention already described herein. The numbered paragraphs in this section are not claims. The claims are set forth below in the later section headed “claims”.

1. Use of at least one targeting RNA molecule and a Cas protein for binding, cleaving, marking or modifying a double stranded target polynucleotide comprising a target nucleic acid sequence, wherein:


- - the double stranded target polynucleotide comprises a target nucleic
    acid strand, comprising said target nucleic acid sequence, and a
    non-target nucleic acid strand, comprising a protospacer nucleic
    acid sequence complementary to the target nucleic acid sequence;
  - the Cas protein has an amino acid sequence of SEQ ID NO: 1 or a
    sequence of at least 77% identity therewith;
  - the at least one targeting RNA molecule recognizes the target
    sequence;
  - the non-target nucleic acid strand further comprises a protospacer
    adjacent motif (PAM) sequence directly adjacent to the 3′ end of the
    protospacer nucleic acid sequence, wherein the PAM sequence
    comprises 5′-NNNNCNN-3′; and wherein said use is not in a human
    cell.

2. A use as in paragraph 1, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 100° C., at a temperature between 30° C. and 80° C., at a temperature between 37° C. and 78° C., preferably at a temperature above 55° C.; more preferably at a temperature between 55° C. and 80° C.; even more preferably at a temperature between 55° C. and 65° C. or 60° C. and 65° C.

3. A use as in paragraph 1 or paragraph 2, wherein the polynucleotide comprising the target nucleic acid sequence is cleaved by the Cas protein, preferably wherein said cleavage is DNA cleavage.

4. A use as in any of paragraphs 1 to 3 wherein the target nucleic acid strand comprising the target sequence is double stranded DNA and said use results in a double stranded break in the polynucleotide comprising the target nucleic acid sequence.

5. A use as in paragraph 1 or paragraph 2 wherein the polynucleotide comprising the target nucleic acid sequence is double stranded DNA, the Cas protein lacks the ability to cut the double stranded DNA and said use results in gene silencing of the polynucleotide.

6. A use as in paragraph 5, wherein the polynucleotide comprising the Cas protein contains the mutations D8A and H582A.

7. A use as in any preceding paragraph wherein the PAM sequence comprises 5′-NNNNCNNA-3′ [SEQ ID NO: 47].

8. A use as in any preceding paragraph, wherein the PAM sequence comprises 5′-NNNNCSAA-3′ [SEQ ID NO: 48].

9. A use as in paragraph 8, wherein the PAM sequence comprises 5′-NNNNCCAA-3′ [SEQ ID NO: 50].

10. A use as in paragraph 8 or paragraph 9, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 70° C.

11. A use as in any of paragraphs 7 to 10, wherein binding, cleaving, marking or modifying occurs at a temperature between 25° C. and 65° C.

12. A use as in any preceding paragraph, wherein the Cas protein is obtainable from a bacterium, archaeon or virus, preferably from a thermophilic bacterium.

13. A use as in any preceding paragraph, wherein the Cas protein is obtainable from Geobacillus sp., preferably from Geobacillus thermodenitrificans.

14. A use as in any preceding paragraph, wherein the targeting RNA molecule comprises a crRNA and a tracrRNA.

15. A use as in any preceding paragraph, wherein the length of the at least one targeting RNA molecule is in the range 35-200 nucleotide residues.

16. A use as in any preceding paragraph, wherein the target nucleic acid sequence is from 15 to 32 nucleotide residues in length.

17. A use as in any preceding paragraph, wherein the Cas protein further comprises at least one functional moiety.

18. A use as in any preceding paragraph wherein the Cas protein is provided as part of a protein complex comprising at least one further functional or non-functional protein, optionally wherein the at least one further protein further comprises at least one functional moiety.

19. A use as in paragraph 17 or paragraph 18, wherein the Cas protein or further protein comprises at least one functional moiety fused or linked to the N-terminus and/or the C-terminus of the Cas protein or protein complex; preferably the C-terminus.

20. A use as in any of paragraphs 17 to 19, wherein the at least one functional moiety is a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-) activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag, for example a green fluorescent protein (GFP).

21. A use as in paragraph 20, wherein the native activity of the Cas9 nuclease is inactivated and the Cas protein is linked to at least one functional moiety.

22. A use as in paragraph 20 or paragraph 21, wherein the at least one functional moiety is a nuclease domain; preferably a FokI nuclease domain.

23. A use as in any of paragraphs 20 to 22, wherein the at least one functional moiety is a marker protein.

24. A method of binding, cleaving, marking or modifying a double stranded target polynucleotide, wherein the double stranded target polynucleotide comprises a target nucleic acid strand comprising a target nucleic acid sequence, and a non-target nucleic acid strand comprising a protospacer nucleic acid sequence complementary to the target nucleic acid sequence, said method comprising:

a. designing at least one targeting RNA molecule, wherein the targeting RNA molecule recognizes the target sequence in the target strand, and the non-target strand further comprises a protospacer adjacent motif (PAM) sequence directly adjacent the 3′ end of the protospacer sequence, wherein the PAM sequence comprises 5′-NNNNCNN-3′;

b. forming a ribonucleoprotein complex comprising the targeting RNA molecule and a Cas protein, wherein the isolated Cas protein has an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith; and

c. the ribonucleoprotein complex binding, cleaving, marking or modifying the target polynucleotide; and wherein said method is not used in human cells.

25. A method as in paragraph 24, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 100° C., at a temperature between 30° C. and 80° C., at a temperature between 37° C. and 78° C., preferably at a temperature above 55° C.; more preferably at a temperature between 55° C. and 80° C.; even more preferably at a temperature between 55° C. and 65° C. or 60° C. and 65° C.

26. A method as in paragraph 24 or paragraph 25, wherein the double stranded target polynucleotide comprising the target nucleic acid sequence is cleaved by the Cas protein, preferably wherein said cleavage is DNA cleavage.

27. A method as in any of paragraphs 24 to 26, wherein the target polynucleotide is double stranded DNA and said use results in a double stranded break in the polynucleotide.

28. A method as in paragraph 24 or paragraph 25, wherein the target polynucleotide comprising the target nucleic acid sequence is double stranded DNA, the Cas protein lacks the ability to cut the double stranded DNA and said method results in gene silencing of the target polynucleotide.

29. A method as in any of paragraphs 24 to 28 wherein the PAM sequence comprises 5′-NNNNCNNA-3′ [SEQ ID NO: 47].

30. A method as in paragraph 29, wherein the PAM sequence comprises 5′-NNNNCSAA-3′ [SEQ ID NO: 48].

31. A method as in paragraph 30, wherein the PAM sequence comprises 5′-NNNNCCAA-3′ [SEQ ID NO: 50].

32. A method as in paragraph 30 or paragraph 31, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 70° C.,

33. A method as in any of paragraphs 29 to 32, wherein binding, cleaving, marking or modifying occurs at a temperature between 25° C. and 65° C.

34. A method as in any of paragraphs 24 to 33, wherein the Cas protein is obtainable from a bacterium, archaeon or virus, preferably from a thermophilic bacterium.

35. A method as in any of paragraphs 24 to 34, wherein the Cas protein is obtainable from Geobacillus sp., preferably from Geobacillus thermodenitrificans.

36. A method as in any of paragraphs 24 to 35, wherein the targeting RNA molecule comprises a crRNA and a tracrRNA.

37. A method as in any of paragraphs 24 to 36, wherein the length of the at least one targeting RNA molecule is in the range 35-200 nucleotide residues.

38. A method as in any of paragraphs 24 to 37, wherein the target nucleic acid sequence is from 15 to 32 nucleotide residues in length.

39. A method as in any of paragraphs 24 to 39, wherein the Cas protein further comprises at least one functional moiety.

40. A method as in any of paragraphs 24 to 40, wherein the Cas protein is provided as part of a protein complex comprising at least one further functional or non-functional protein, optionally wherein the at least one further protein further comprises at least one functional moiety.

41. A method as in paragraph 39 or 40, wherein the Cas protein or further protein comprises at least one functional moiety fused or linked to the N-terminus and/or the C-terminus of the Cas protein or protein complex; preferably the C-terminus.

42. A method as in any of paragraphs 39 to 41, wherein the at least one functional moiety is a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-) activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag, for example a green fluorescent protein (GFP).

43. A method as in paragraph 42, wherein the native activity of the Cas9 nuclease is inactivated and the Cas protein is linked to at least one functional moiety.

44. A method as in paragraph 42 or paragraph 43, wherein the at least one functional moiety is a nuclease domain; preferably a FokI nuclease domain.

45. A method as in any of paragraphs 42 to 44, wherein the at least one functional moiety is a marker protein.

46. A use as in paragraph 20 or method as in paragraph 42, wherein the double stranded target polynucleotide is dsDNA, the at least one functional moiety is a nuclease or a helicase-nuclease, and the modification is a single-stranded or a double-stranded break at a desired locus.

47. A use as in paragraph 20 or method as in paragraph 42, wherein the double stranded target polynucleotide is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor and the binding, cleaving, marking or modifying results in modification of gene expression.

48. A use as in paragraph 20 or method as in paragraph 42, wherein said binding, cleaving, marking or modifying occurs in vivo.

49. A use or method as in paragraph 48, wherein said binding, cleaving, marking or modifying occurs in a thermophilic organism, preferably a thermophilic prokaryotic organism, more preferably Geobacillus sp.

50. A use or method as in paragraph 48, wherein said binding, cleaving, marking or modifying occurs in a mesophilic organism, preferably a mesophilic prokaryotic organism, more preferably Pseudomonas sp.

51. A use as in any of paragraphs 1 to 4, 7 to 23 or 46, or a method as in any of paragraphs 24 to 27, 29 to 46 wherein the binding, cleaving, marking or modifying results in modifying or deleting and/or inserting a desired nucleotide sequence at a desired location, and/or wherein the binding, cleaving, marking or modifying results in silencing gene expression at a desired locus.

52. A transformed non-human cell, having a double stranded target polynucleotide comprising a target nucleic acid sequence, wherein the double stranded target polynucleotide comprises a target nucleic acid strand, comprising said target nucleic acid sequence, and a non-target nucleic acid strand, comprising a protospacer nucleic acid sequence complementary to the target nucleic acid sequence, said cell comprising:


- - a clustered regularly interspaced short palindromic repeat
    (CRISPR)-associated (Cas) protein having an amino acid sequence of
    SEQ ID NO: 1 or a sequence of at least 77% identity therewith;
  - at least one targeting RNA molecule which recognizes the target
    nucleic acid sequence in the target nucleic acid strand, wherein the
    non-target strand further comprises a protospacer adjacent motif
    (PAM) sequence directly adjacent the 3′ end of the protospacer
    sequence, wherein the PAM sequence comprises 5′-NNNNCNN-3′; and
  - an expression vector comprising a nucleic acid encoding at least one
    of said Cas protein and said targeting RNA molecule.

53. A transformed cell as in paragraph 52, wherein the Cas protein and targeting RNA molecule enable binding, cleaving, marking or modifying of the target polynucleotide in the cell and the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 100° C., at a temperature between 30° C. and 80° C., at a temperature between 37° C. and 78° C., preferably at a temperature above 55° C.; more preferably at a temperature between 55° C. and 80° C.; even more preferably at a temperature between 55° C. and 65° C. or 60° C. and 65° C.

54. A transformed cell as in paragraph 52 or paragraph 53, wherein the target nucleic acid strand comprising the target nucleic acid sequence is cleaved by the Cas protein, preferably wherein said cleavage is DNA cleavage.

55. A transformed cell as in any of paragraphs 52 to 54, wherein the target polynucleotide comprising the target sequence is double stranded DNA and said binding, cleaving, marking or modifying results in a double stranded break in the target polynucleotide.

56. A transformed cell as in paragraph 52 or paragraph 53, wherein the target polynucleotide comprising the target nucleic acid sequence is double stranded DNA, the Cas protein lacks the ability to cut the double stranded DNA and said binding, cleaving, marking or modifying results in gene silencing of the target polynucleotide.

57. A transformed cell as in any of paragraphs 52 to 56, wherein the PAM sequence comprises 5′-NNNNCNNA-3′ [SEQ ID NO: 47].

58. A transformed cell as in paragraph 57, wherein the PAM sequence comprises 5′-NNNNCSAA-3′ [SEQ ID NO: 48].

59. A transformed cell as in paragraph 58, wherein the PAM sequence comprises 5′-NNNNCCAA-3′ [SEQ ID NO: 50].

60. A transformed cell as in paragraph 58 or paragraph 59, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 70° C.

61. A transformed cell as in any of paragraphs 57 to 60, wherein binding, cleaving, marking or modifying occurs at a temperature between 25° C. and 65° C.

62. A transformed cell as in any of paragraphs 52 to 61, wherein the Cas protein is obtainable from a bacterium, archaeon or virus, preferably from a thermophilic bacterium.

63. A transformed cell as in any of paragraphs 52 to 62, wherein the Cas protein is obtainable from Geobacillus sp., preferably from Geobacillus thermodenitrificans.

64. A transformed cell as in any of paragraphs 52 to 63, wherein the cell is a prokaryotic cell.

65. A transformed cell as in any of paragraphs 52 to 63, wherein the cell is a eukaryotic cell.

66. A transformed cell as in any of paragraphs 52 to 65, wherein the targeting RNA molecule comprises a crRNA and a tracrRNA.

67. A transformed cell as in any of paragraphs 52 to 66, wherein the length of the at least one targeting RNA molecule is in the range 35-200 nucleotide residues.

68. A transformed cell as in any of paragraphs 52 to 67, wherein the target nucleic acid sequence is from 15 to 32 nucleotide residues in length.

69. A transformed cell as in any of paragraphs 52 to 68, wherein the Cas protein further comprises at least one functional moiety.

70. A transformed cell as in any of paragraphs 52 to 69, wherein the Cas protein is provided as part of a protein complex comprising at least one further functional or non-functional protein, optionally wherein the at least one further protein further comprises at least one functional moiety.

71. A transformed cell as in paragraph 69 or 70, wherein the Cas protein or further protein comprises at least one functional moiety fused or linked to the N-terminus and/or the C-terminus of the Cas protein or protein complex; preferably the N-terminus.

72. A transformed cell as in any of paragraphs 69 to 71, wherein the at least one functional moiety is a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag, for example a green fluorescent protein (GFP).

73. A transformed cell as in paragraph 72, wherein the native activity of the Cas9 nuclease is inactivated and the Cas protein is linked to at least one functional moiety.

74. A transformed cell as in any of paragraphs 69 to 73, wherein the at least one functional moiety is a nuclease domain; preferably a FokI nuclease domain.

75. A transformed cell as in any of paragraphs 69 to 73, wherein the at least one functional moiety is a marker protein.

76. A transformed cell as in any of paragraphs 69 to 74, wherein the double stranded target polynucleotide is dsDNA, the at least one functional moiety is a nuclease or a helicase-nuclease, and the modification is a single-stranded or a double-stranded break at a desired locus.

77. A transformed cell as in any of paragraphs 69 to 73 or method as in paragraph 42, wherein the double stranded target polynucleotide is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor and the binding, cleaving, marking or modifying results in modification of gene expression.

78. A transformed cell as in any of paragraphs 69 to 74 wherein the Cas protein is expressed from an expression vector.

79. A transformed cell as in any of paragraphs 52 to 78 wherein the binding, cleaving, marking or modifying results in modifying or deleting and/or inserting a desired nucleotide sequence at a desired location, and/or wherein the binding, cleaving, marking or modifying results in silencing gene expression at a desired locus.

80. A nucleoprotein complex comprising a Cas protein, at least one targeting RNA molecule which recognises a target nucleic acid sequence in a double stranded target polynucleotide, and the target polynucleotide, wherein the Cas protein has an amino acid sequence of SEQ ID NO: 1 or a sequence of at least 77% identity therewith;


- - the double stranded target polynucleotide comprises a target nucleic
    acid strand, comprising said target nucleic acid sequence, and a
    non-target nucleic acid strand, comprising a protospacer nucleic
    acid sequence complementary to the target nucleic acid sequence and
    a protospacer adjacent motif (PAM) sequence directly adjacent the 3′
    end of the protospacer sequence, wherein the PAM sequence comprises
    5′-NNNNCNN-3′; wherein the nucleoprotein complex is not in a human
    cell.

81. A nucleoprotein complex as in paragraph 80, wherein the nucleoprotein complex occurs at a temperature between 20° C. and 100° C., at a temperature between 30° C. and 80° C., at a temperature between 37° C. and 78° C., preferably at a temperature above 55° C.; more preferably at a temperature between 55° C. and 80° C.; even more preferably at a temperature between 55° C. and 65° C. or 60° C. and 65° C.

82. A nucleoprotein complex as in paragraph 80 or claim 81, wherein the double stranded target polynucleotide comprising the target nucleic acid sequence is cleaved by the Cas protein, preferably wherein said cleavage is DNA cleavage.

83. A nucleoprotein complex as in any of paragraphs 80 to 82, wherein the target polynucleotide comprising the target sequence is double stranded DNA and said binding, cleaving, marking or modifying results in a double stranded break in the target polynucleotide.

84. A nucleoprotein complex as in paragraph 80 or paragraph 81, wherein the target polynucleotide comprising the target nucleic acid sequence is double stranded DNA, the Cas protein lacks the ability to cut the double stranded DNA and the presence of said nucleoprotein complex results in gene silencing of the target polynucleotide.

85. A nucleoprotein complex as in any of paragraphs 80 to 84, wherein the PAM sequence comprises 5′-NNNNCNNA-3′ [SEQ ID NO: 47].

86. A nucleoprotein complex as in paragraph 85, wherein the PAM sequence comprises 5′-NNNNCSAA-3′ [SEQ ID NO: 48].

87. A nucleoprotein complex as in paragraph 86, wherein the PAM sequence comprises 5′-NNNNCCAA-3′ [SEQ ID NO: 50].

88. A nucleoprotein complex as in paragraph 86 or paragraph 87, wherein the binding, cleaving, marking or modifying occurs at a temperature between 20° C. and 70° C.

89. A nucleoprotein complex as in any of paragraphs 85 to 88, wherein binding, cleaving, marking or modifying occurs at a temperature between 25° C. and 65° C.

90. A nucleoprotein complex as in any of paragraphs 80 to 89, wherein the Cas protein is obtainable from a bacterium, archaeon or virus, preferably from a thermophilic bacterium.

91. A nucleoprotein complex as in any of paragraphs 80 to 90, wherein the Cas protein is obtainable from Geobacillus sp., preferably from Geobacillus thermodenitrificans.

92. A nucleoprotein complex as in any of paragraphs 80 to 91, wherein the nucleoprotein complex is in a prokaryotic cell.

93. A nucleoprotein complex as in any of paragraphs 80 to 91, wherein the nucleoprotein complex is in a eukaryotic cell.

94. A nucleoprotein complex as in any of paragraphs 80 to 93, wherein the targeting RNA molecule comprises a crRNA and a tracrRNA.

95. A nucleoprotein complex as in any of paragraphs 80 to 94, wherein the length of the at least one targeting RNA molecule is in the range 35-200 nucleotide residues.

96. A nucleoprotein complex as in any of paragraphs 80 to 95, wherein the target nucleic acid sequence is from 15 to 32 nucleotide residues in length.

97. A nucleoprotein complex as in any of paragraphs 80 to 96, wherein the Cas protein further comprises at least one functional moiety.

98. A nucleoprotein complex as in any of paragraphs 80 to 97, wherein the Cas protein is provided as part of a protein complex comprising at least one further functional or non-functional protein, optionally wherein the at least one further protein further comprises at least one functional moiety.

99. A nucleoprotein complex as in paragraph 97 or 98, wherein the Cas protein or further protein comprises at least one functional moiety fused or linked to the N-terminus and/or the C-terminus of the Cas protein or protein complex; preferably the C-terminus.

100. A nucleoprotein complex as in any of paragraphs 97 to 99, wherein the at least one functional moiety is a protein; optionally selected from a helicase, a nuclease, a helicase-nuclease, a DNA methylase, a histone methylase, an acetylase, a phosphatase, a kinase, a transcription (co-)activator, a transcription repressor, a DNA binding protein, a DNA structuring protein, a marker protein, a reporter protein, a fluorescent protein, a ligand binding protein, a signal peptide, a subcellular localisation sequence, an antibody epitope or an affinity purification tag, for example a green fluorescent protein (GFP).

101. A nucleoprotein complex as in paragraph 100, wherein the native activity of the Cas9 nuclease is inactivated and the Cas protein is linked to at least one functional moiety.

102. A nucleoprotein complex as in any of paragraphs 97 to 101, wherein the at least one functional moiety is a nuclease domain; preferably a FokI nuclease domain.

103. A nucleoprotein complex as in any of paragraphs 97 to 101, wherein the at least one functional moiety is a marker protein.

104. A nucleoprotein complex as in any of paragraphs 97 to 102, wherein the nucleic acid is dsDNA, the at least one functional moiety is a nuclease or a helicase-nuclease, and the target polynucleotide has a single-stranded or a double-stranded break at a desired locus.

105. A nucleoprotein complex as in any of paragraphs 97 to 101, wherein the nucleic acid is dsDNA and the functional moiety is selected from a DNA modifying enzyme (e.g. a methylase or acetylase), a transcription activator or a transcription repressor and the nucleoprotein complex formation results in modification of gene expression.

106. A nucleoprotein complex as in any of paragraphs 80 to 105, wherein the nucleoprotein formation results in modifying or deleting and/or inserting a desired nucleotide sequence at a desired location, and/or wherein the nucleoprotein complex formation results in silencing gene expression at a desired locus.

