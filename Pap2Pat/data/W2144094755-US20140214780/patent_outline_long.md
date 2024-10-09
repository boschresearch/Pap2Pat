# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce genome-wide association studies
- describe data management challenges
- discuss limitations of pedigree files
- mention existing compression solutions
- highlight need for efficient compression techniques

## SUMMARY

- introduce hybrid compression method
- describe advantages over PLINK or PBAT
- outline compression algorithm selection
- explain storage requirement computation
- describe compression of genetic data
- mention analysis of compressed data
- introduce first aspect of invention
- describe computer-implemented method
- outline compression algorithm options
- explain compression and storage
- mention analysis and query processing
- introduce second aspect of invention
- describe computer system for compression
- outline system components
- explain compression and analysis
- introduce third aspect of invention
- describe alternative compression method
- outline system and method for compression

## DESCRIPTION

### 1. Genetic Data Format

- introduce pedigree files
- describe LINKAGE format
- explain genetic data structure
- mention other formats (e.g., HapMat)

### 2. Compression Algorithms

- introduce compression algorithms
- describe hybrid algorithm
- motivate algorithm selection
- introduce algorithm I: binary encoding
- explain binary encoding process
- illustrate binary encoding example
- describe compression factor calculation
- introduce algorithm II: subject indices
- explain subject indices process
- describe compression factor calculation
- introduce algorithm III: binary encoding and subject indices
- explain algorithm III process
- describe compression factor calculation
- introduce hybrid compression method
- describe performance comparison
- illustrate performance plots
- explain performance dependence on MAF and number of subjects
- describe empirical testing of SpeedGene algorithm
- introduce example 1: GWAS SNP-chips
- describe example 1 results
- introduce example 2: sequence data
- describe example 2 results
- introduce example 3: 1000 genome data

### EXAMPLE 1

- describe example 1 results

### EXAMPLE 2

- describe example 2 results

### EXAMPLE 3

- describe example 3 results for populations
- describe example 3 results for chromosomes

### 3. Implementation

- introduce computer-executable instructions
- define program modules
- describe computer system configurations
- discuss distributed computing environments
- explain communication in the network
- describe LAN networking environment
- describe WAN networking environment
- discuss modem or other communication mechanism
- describe Internet, Intranet, Extranet, Ethernet connections
- list suitable communications protocols
- describe wireless communications protocols
- describe central computing device in a distributed computing environment
- describe general-purpose computer components
- discuss computer-readable media
- describe system memory components
- discuss BIOS and ROM
- describe RAM and data/program modules
- list operating systems
- describe other removable/nonremovable computer storage media
- discuss processing unit and technologies
- describe programming languages
- implement compression methods in C++ library
- describe classes for compressing and loading genetic data
- illustrate exemplary computer with features for genetic-data compression and storage

