# DESCRIPTION

## TECHNICAL FIELD

- relate to extending concept labels

## BACKGROUND

- define ontology
- application of ontology

## SUMMARY

- motivate ontology engineering
- limitations of existing ontologies
- need for multilingualism
- difficulties of translation
- limitations of current approaches
- need for efficient extension
- introduce embodiments

## DETAILED DESCRIPTION

- depict flowchart of acts for extending concept labels of an ontology
- introduce two major acts: extracting terms and extending concept labels
- extract terms in target language from representative corpus
- translate terms into source language and map to existing ontology concepts
- extend concept labels of ontology by terms in target language
- support universal, language-independent translation process
- assume vocabulary of ontology covers most relevant concepts of domain
- use corpus to determine most relevant concepts for translation
- reduce human interaction to minimum
- use linguistical analysis to rate linguistical relevancy of terms
- process corpus by linguistical analysis
- result in list of terms ordered by linguistical relevancy
- detail act of extracting terms in target language from representative corpus
- perform language analysis
- use statistical analysis in conjunction with language analysis
- process corpus by linguistical analysis
- extract terms exhibiting linguistical relevancy
- rank terms by linguistical relevancy
- apply filtering algorithm
- exclude terms from translation based on linguistical information
- exclude terms from translation based on statistical information
- exclude terms from translation based on additional information
- detail act of translating terms into source language
- use translation module to translate first terms into second terms
- provide human user feedback to increase quality of second term
- disambiguate second term
- provide ordered list of first terms associated by respective second term
- detail act of extending concept labels of ontology by terms in target language
- provide ontology matching
- retrieve matching concept within ontology
- provide manual user feedback to increase quality of mapping
- extend matching ontology concepts by first term
- include target language variants in extended ontology
- disclose embodiment using ontology with partially populated concept labels
- execute ontology-based concept annotation
- combine target-language vocabulary stems from ontology and corpus
- retrieve matches for listed ontology concepts
- annotate each matching stem with represented ontology concepts
- associate first term with target-language vocabulary stems of ontology
- compute occurrence count for each single word stem
- compute co-occurrence count for each single n-gram
- rank terms by linguistical relevancy
- apply filtering algorithm
- exclude terms from translation based on annotation information
- illustrate extension of concept labels of medical ontology RadLex
- detect sentence and word boundaries
- stem each word with specially tailored stemming algorithm
- apply stemming algorithm to existing German ontology concepts
- annotate radiology reports with RadLex concepts
- statistically analyze resulting stem-annotation occurrences
- provide ordered list of first terms as result of linguistical analysis

