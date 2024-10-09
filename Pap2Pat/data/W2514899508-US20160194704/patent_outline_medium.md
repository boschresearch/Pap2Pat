# DESCRIPTION

## BACKGROUND OF THE INVENTION

- motivate whole-genome sequencing

## SUMMARY OF THE INVENTION

- introduce whole-genome sequencing method
- describe method's objective
- outline method's steps
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
- position sequence contigs onto clone contigs using sequenced paired-end information
- determine relative positions and directions of clone contigs by molecular markers
- connect sequences of clone contigs to obtain whole-genome sequences
- define k-mer set of mixing pool at κ-th dimension with index of λ
- calculate initial k-mer set of given clone
- calculate excluded union k-mer set of given clone
- calculate final k-mer set of given clone
- balance feature sequence set and k-mer set of mixing pool

## DETAILED DESCRIPTION OF THE EMBODIMENTS

- introduce whole-genome sequencing method
- construct BAC library
- number BAC clones
- construct clone mixing pool
- describe mixing pool construction strategies
- extract DNA of mixing pool
- sequence DNA of mixing pool
- scan sequencing results
- obtain feature sequence set of mixing pool
- analyze clone feature sequence set
- process feature sequence sets of mixing pools
- define feature sequence sets
- compute intersection set of feature sequence sets
- compute excluded union set of feature sequence sets
- compute final feature sequence set
- construct clone contigs
- scan sequencing results and get k-mer set
- analyze k-mer set of clone
- segment contigs
- assemble and integrate into physical map
- position sequences to contig blocks
- connect sequences through double end connection
- position and connect contig to chromosome
- claim invention scope

