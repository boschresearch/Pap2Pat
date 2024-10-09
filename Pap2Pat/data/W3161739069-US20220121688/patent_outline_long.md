# DESCRIPTION

## TECHNICAL FIELD

- introduce remote-sensing images

## BACKGROUND OF THE INVENTION

- motivate massive remote-sensing image data
- describe limitations of traditional data storage
- describe distributed file system technology
- limitations of distributed file system for binary data
- describe partitioning strategy of spatial data
- limitations of partitioning strategy

## SUMMARY OF THE INVENTION

- motivate parallel data access method
- describe data storage method
- segment remote-sensing image
- collect data access log
- quantify load conditions
- select pool with minimum load
- write data block into pool
- return data identifier and access path
- store metadata
- parse data block into N-dimensional matrix
- write N-dimensional matrix into pool
- describe access path
- calculate pool load index
- determine grid system
- store data blocks in GeoTIFF format
- describe parallel data access method
- receive retrieval request
- retrieve data blocks
- determine access path
- perform projection transformation and resampling
- perform data cutting
- describe parallel data access system

## DETAILED DESCRIPTION OF THE INVENTION

- introduce invention with attached drawings and embodiments

### 1. Grid Subdivision Storage

- segment remote-sensing image according to spatial position
- define grid subdivision system for remote-sensing data
- calculate offset information for pixel point at upper left corner of grid
- segment original remote-sensing image into sub data blocks according to grid
- provide subdivision pseudo code of original remote-sensing image

### 2. Subdivision Data Warehousing

- update spatial information such as boundary range and central point
- store all metadata information in underlying distributed object storage system Ceph
- determine subdivision grid system according to projection coordinate system information
- cut original remote-sensing image according to scheme determined
- collect data access logs of underlying Ceph cluster
- analyze statistical information such as number of data requests processed
- quantify load conditions of each Ceph cluster and each pool
- select Ceph cluster with smallest current load and pool with smallest load

### 3. Data Reading and Writing Interface

- design and realize new GDAL raster data drive
- quickly access subdivision slices stored in Ceph cluster environment
- realize reading and writing interface for remote-sensing image data subdivision slicing
- design and development according to grid data format specification of GDAL
- register data type as required
- provide more detailed data access interface with higher concurrency
- expose underlying grid data blocks to user
- read and write access to each independent grid data block
- perform separate parallel reading and writing computation on each grid data block
- make intersect query for all data blocks with dataid in data block metadata database
- initiate parallel reading and writing request
- retrieve all data blocks related to reading and writing in metadata database
- determine specific access path of each data block in ceph
- return access paths of all data blocks to client
- construct data parallel reading and writing request
- perform projection transformation, resampling and other related operations
- feed relevant processing results back to client

