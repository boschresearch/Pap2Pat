# DESCRIPTION

## PRIORITY APPLICATIONS

- claim priority applications

## BACKGROUND

- introduce LED volumes
- limitations of LED panels

## SUMMARY

- introduce color correction method
- generate pre-correction matrix
- generate post-correction matrix
- generate second pre-correction matrix
- apply correction matrices
- adjust pixel values by RGB offset
- solve for first 3x3 matrix
- generate color calibration image
- sample average pixel values
- solve for second 3x3 matrix
- generate calibration imagery
- describe system embodiment
- describe computer-readable instructions
- combine features from embodiments

## DETAILED DESCRIPTION OF EXEMPLARY EMBODIMENTS

- introduce virtual production stages
- describe LED volumes in media production
- motivate color rendition issues
- describe limitations of prior color calibration workflows
- introduce color rendition optimization system
- describe system's ability to correct color rendition
- summarize system's advantages
- describe generating calibration images
- describe using principal-photography camera to capture images
- describe solving for color correction matrices
- describe applying matrices to different components of LED volume
- describe resulting optimized color rendition
- introduce example RGB LED volume virtual production stage
- describe LED panels and pixels
- define out-of-camera-frustum pixels
- define in-camera-frustum pixels
- describe tracking camera movement
- describe determining pixel types on-the-fly
- describe final imagery captured by camera
- introduce color rendition optimization system operating within virtual production stage
- describe system receiving data from LED panels and camera
- describe system transmitting data to LED panels and server
- describe system's assumptions and prerequisites
- assume panel and camera linearity
- assume radiometric alignment of different panel types
- assume high dynamic range image map acquisition and display
- describe generating three matrices based on calibration imagery
- describe in-camera-frustum LED panel color calibration image
- describe out-of-camera-frustum color rendition calibration images
- describe generating out-of-camera-frustum images in different ways
- describe first pre-correction matrix for metameric illuminant matching
- describe extracting average pixel values from calibration image
- describe solving for first pre-correction matrix
- describe post-correction matrix for color rendition calibration
- describe simulating color chart appearance
- describe determining relationship between calibration images and full sphere of illumination
- describe defining scale factor for setup geometry
- describe constructing cube map environment
- describe computing diffuse convolution for frontal direction
- describe scaling calibration images by scale factor
- describe predicting color chart appearance with uniform illumination
- describe focusing on diffuse integral of illumination
- describe defining diffuse integral of high-dynamic range image map
- describe equaling wavg to pixel value of white square of color chart
- describe FIG. 1 illustrating RGB LED volume virtual production stage
- describe FIG. 2 illustrating environmental diagram of color rendition optimization system
- describe FIG. 3 illustrating additional detail associated with color rendition optimization system
- describe FIG. 4 illustrating method flow of color rendition optimization system
- describe combining features from different implementations
- describe storing digital media on storage media of motion picture camera
- describe embodiments of color rendition optimization system
- define color rendition optimization system
- describe virtual production stage
- introduce color chart
- explain calibration data
- define pre-correction matrix M
- describe estimation of color chart appearance
- define post-correction matrix Q
- explain solving for Q
- describe application of Q
- introduce second pre-correction matrix N
- explain solving for N
- describe application of N
- explain optimization of color rendition
- describe limitations of LED panels
- introduce RGB offset
- explain computation of black level
- describe alternative arrangements
- illustrate color rendition optimization system
- describe pre-correction matrix manager
- describe post-correction matrix manager
- describe calibration manager
- explain joint optimization approach
- describe constraints on white point
- describe other types of virtual production stages
- describe server architecture
- describe physical processor
- describe memory
- illustrate flow diagram of method
- describe generating first pre-correction matrix
- describe generating post-correction matrix
- describe generating second pre-correction matrix
- describe optimizing color rendition
- describe correcting color rendition
- describe advantages of color rendition optimization system
- describe limitations of existing systems
- describe importance of color rendition
- describe applications of color rendition optimization system
- describe future developments
- describe variations of color rendition optimization system
- conclude color rendition optimization system

### EXAMPLE EMBODIMENTS

- introduce example 1: computer-implemented method
- specify generating pre-correction matrices
- specify generating post-correction matrix
- specify utilizing correction matrices
- introduce example 2: solving for pre-correction matrix
- introduce example 3: solving for post-correction matrix
- introduce example 4: generating second pre-correction matrix
- introduce example 5: generating in-camera-frustum LED panel color calibration image
- introduce example 6: solving for post-correction matrix
- introduce example 7: generating calibration imagery
- introduce example 8: adjusting pixel values
- describe system embodiment
- describe non-transitory computer-readable medium embodiment
- define terms used in specification

