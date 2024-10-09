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
- upload new encrypted document
- determine if document identifier exists
- update identifier OKVS
- increment keyword count
- insert into document OKVS
- handle query count
- access counts OKVS
- access deletion OKVS
- handle updated encrypted document
- handle deletion request

## DETAILED DESCRIPTION

- introduce searchable encryption
- motivate searchable encryption
- describe limitations of current searchable encryption schemes
- describe response-revealing searchable encryption schemes
- describe attacks on response-revealing schemes
- motivate response-hiding searchable encryption schemes
- describe current response-hiding schemes
- introduce oblivious random access memory (ORAM)
- describe ORAM implementations
- introduce searchable encryption manager
- describe searchable encryption manager functionality
- describe document data store
- describe searchable encryption manager query processing
- describe document oblivious key-value storage (OKVS)
- describe OKVS functionality
- describe document retriever functionality
- describe document insertion process
- describe counts OKVS functionality
- describe query count functionality
- describe list generator operation
- describe deletion OKVS operation
- describe SE manager operation
- describe document OKVS operation
- describe counts OKVS operation
- describe deletion request operation
- describe system architecture
- describe method for providing response-hiding searchable encryption
- describe data processing hardware operation
- describe document oblivious key-value storage operation
- describe computing device architecture
- describe processor operation
- describe memory operation
- describe storage device operation
- describe high-speed interface/controller operation
- describe low-speed interface/controller operation

