# DESCRIPTION

## BACKGROUND OF THE INVENTION

- define field of invention
- limitations of current strategies
- motivate new approach

## SUMMARY OF THE INVENTION

- introduce whole-genome sequencing method
- provide method for rapidly and accurately accomplishing whole-genome sequencing
- extract whole-genome DNA and construct BAC library
- construct BAC clone mixing pools
- extract DNA of BAC clone mixing pools
- perform pair-end sequencing for DNA extracted from BAC clone mixing pools
- scan sequences of each mixing pool to obtain feature sequence set and k-mer set
- analyze feature sequence set and k-mer set of each clone
- construct clone contigs according to feature sequence sets of clones
- divide k-mer sets of clones into small k-mer sets by clone contigs
- position small k-mer sets onto clone contigs
- assemble NGS sequences in mixing pool to yield sequence contigs
- position sequence contigs onto clone contigs
- determine relative positions and directions of clone contigs
- connect sequences of clone contigs to obtain whole-genome sequences
- define total number of clones of BAC library
- define total number of constructed mixing pools
- express k-mer set of mixing pool at κ-th dimension with index λ
- express k-mer sets of mixing pools comprising given clone
- calculate intersection set of k-mer sets of mixing pools
- calculate excluded union k-mer set of given clone
- calculate final k-mer set of given clone
- define basic operations of sets
- define frequency set or key-value set
- calculate union of frequency sets
- calculate difference of frequency sets
- calculate key of frequency set
- analyze feature sequence sets and k-mer sets of clones
- calculate k-mer set of clone
- calculate excluded union k-mer set of clone
- calculate final k-mer set of clone
- represent k-mer set of clones by graphs
- calculate intersection of k-mer sets of every three mixing pools
- calculate union of k-mer sets of all other clones in addition to given clone
- calculate intersection of excluded union k-mer sets
- calculate final k-mer set of clone by subtracting intersection
- filter k-mer set of mixing pool by frequency
- balance k-mer set of mixing pool
- segment clone contigs into blocks
- position sequence contigs onto blocks
- connect sequences after double end connection
- determine direction of sequence after connection

## DETAILED DESCRIPTION OF THE EMBODIMENTS

- introduce whole-genome sequencing method
- construct BAC library
- number BAC clones
- construct clone mixing pool
- determine clone position in cube
- construct multidimensional mixing pool
- describe perpendicular crossing pools
- describe oblique crossings pools
- describe angle crossings pools
- illustrate mixing pool construction
- explain pool dimension
- select clones for mixing pool
- construct 6D mixing pool
- extract DNA of mixing pool
- mix consecutive clones
- construct sequencing pool
- replicate base pools
- extract plasmid DNA
- sequence DNA of mixing pool
- scan sequencing results
- obtain feature sequence set
- analyze clone feature sequence set
- define feature sequence sets
- compute intersection set of feature sequence sets
- compute excluded union set of feature sequence sets
- compute final feature sequence set
- construct clone contigs
- compute union set of feature sequences
- construct index table for feature sequences
- replace feature sequences with index values
- sort index values
- export index values to ".size" file
- assemble clones using FPC
- set assembly parameters
- carry out initial assembly
- carry out DQer
- obtain clone contig
- scan sequencing results
- get k-mer set of mixing pool
- analyze k-mer set of clone
- segment contigs
- assemble NGS sequences
- filter assembled sequences
- combine filtered sequences
- reassemble combined sequences
- position sequences to contig blocks
- carry out double end comparison
- connect positioned sequences
- position and connect contigs to chromosome

