# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce search engine
- describe digital data storage
- discuss limitations of search engines
- motivate need for relevance scoring
- describe existing search engines for MEDLINE

### Comparison of Information Retrieval Systems of MEDLINE

- list retrieval services for MEDLINE
- describe features of OVID
- describe features of PubMed
- discuss limitations of existing services
- motivate need for relationship detection

### Estimating Number of Words per Query in Queries Submitted to NLM's PubMed.

- analyze query logs from PubMed
- summarize query word count statistics

## SUMMARY OF THE INVENTION

- introduce information retrieval system
- describe system components and features

## DESCRIPTION OF THE DRAWINGS

- describe figures and charts

## DESCRIPTION OF THE INVENTION

### The Pre-Processing Component

- describe MEDLINE database
- extract fields from XML article records
- detect and separate sentences
- load sentences into database
- transform article contents into database
- identify biomedical concepts
- resolve term ambiguity and synonymy
- process compound sentences
- recognize relationships
- restrict problem domain and define sub-problems

### The User Interface

- implement software application to receive user query

### The Search Engine

- describe query composition
- implement Boolean operators
- use Unified Medical Language System for term mapping
- build search engine using open source software
- write query application
- implement database
- serve user's HTTP requests
- produce user interface and reports
- highlight matched keywords in HTML report
- add publication information and hyperlink

## EXAMPLE 1

### Role of ‘Infection’ in ‘Sudden Infant Death Syndrome’ (SIDS)

- introduce SIDS
- formulate search query
- compare search results between PubMed and ReleMed
- analyze precision of search results
- discuss false positive article

## EXAMPLE 2

### Finding ‘Questionnaires’ for Measuring ‘Health Literacy’

- compare search results between PubMed and ReleMed

## The Distributed Parallel Computing Architecture

- introduce distributed computing architecture
- describe clustering of servers
- explain data management and transmission
- discuss scalability of architecture
- outline user access and computation

