# DESCRIPTION

## TECHNICAL FIELD

- introduce searchable encryption

## BACKGROUND

- limitations of searchable encryption

## SUMMARY

- receive search query
- access document OKVS
- return list of document identifiers
- receive read request
- retrieve encrypted document
- return encrypted document
- receive new encrypted document
- determine if new document identifier exists
- update identifier OKVS
- increment keyword count
- insert keyword into document OKVS
- update deletion status
- discard new document identifier
- limit number of document identifiers
- append dummy document identifiers
- include unique numerical indicator
- access counts OKVS
- determine number of encrypted documents
- access deletion OKVS
- identify deleted document identifiers
- exclude deleted document identifiers
- update deletion OKVS
- receive updated encrypted document
- increment keyword count
- insert keyword into document OKVS
- update deletion status
- receive deletion request
- update deletion status
- include optional features
- include system for searchable encryption
- include data processing hardware
- include memory hardware
- perform operations

## DETAILED DESCRIPTION

- introduce searchable encryption
- motivate searchable encryption
- describe limitations of current searchable encryption schemes
- describe response-revealing searchable encryption schemes
- describe attacks on response-revealing schemes
- motivate response-hiding searchable encryption schemes
- describe current response-hiding schemes
- describe limitations of current response-hiding schemes
- introduce oblivious random access memory (ORAM)
- describe ORAM implementations
- introduce searchable encryption manager
- describe searchable encryption manager functionality
- introduce system architecture
- describe user device
- describe remote system
- describe document data store
- describe searchable encryption (SE) manager
- describe SE manager functionality
- introduce document oblivious key-value storage (OKVS)
- describe OKVS functionality
- describe key-value map
- describe keyword-keyword ID association
- describe SE manager query processing
- describe SE manager access to OKVS
- describe SE manager return of document IDs
- introduce document retriever
- describe document retriever functionality
- describe read request processing
- introduce new document upload
- describe SE manager processing of new document
- describe identifier OKVS
- describe SE manager update of identifier OKVS
- describe counts OKVS
- describe SE manager update of counts OKVS
- describe SE manager access to counts OKVS
- describe SE manager optimization using counts OKVS
- introduce query count
- describe list generator
- describe list generator functionality
- describe list generator
- describe dummy document identifiers
- describe deletion OKVS
- describe deletion flag
- describe SE manager
- describe updated encrypted document
- describe keyword count
- describe document OKVS
- describe deletion request
- describe OKVS initialization
- describe system efficiency
- describe system security
- describe response-hiding searchable encryption
- describe method for providing response-hiding searchable encryption
- describe receiving search query
- describe accessing document OKVS
- describe returning list of document identifiers
- describe computing device
- describe processor
- describe memory
- describe storage device
- describe high-speed interface/controller
- describe low-speed interface/controller
- describe display
- describe computing device implementation
- describe software application
- describe machine-readable medium
- describe computer program
- describe programmable processor
- describe data processing hardware
- describe computer readable media
- describe user interaction

