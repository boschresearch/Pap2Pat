# DESCRIPTION

## TECHNICAL FIELD

- introduce remote-sensing images

## BACKGROUND OF THE INVENTION

- motivate massive remote-sensing image data
- limitations of traditional data storage systems
- limitations of traditional partitioning strategies

## SUMMARY OF THE INVENTION

- motivate parallel data access method
- define data storage method
- segment remote-sensing image
- collect data access log
- quantify load conditions
- select storage position
- write data block
- return data identifier
- store metadata
- define parallel data access method
- define parallel data access system

## DETAILED DESCRIPTION OF THE INVENTION

- introduce grid subdivision storage

### 1. Grid Subdivision Storage

- define grid subdivision system
- describe segmentation of remote-sensing image

### 2. Subdivision Data Warehousing

- describe data subdivision scheme
- detail data block storage in Ceph
- explain load balancing and data distribution
- outline data access path generation

### 3. Data Reading and Writing Interface

- introduce GDAL raster data interface
- describe librados-based reading and writing interface
- outline grid granularity task parallel access
- detail parallel reading and writing process
- introduce global scale data access
- describe hiding subdivision data blocks
- outline reading and writing process for global scale data access
- summarize data access modes

