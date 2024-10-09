# DESCRIPTION

## TECHNICAL FIELD

- relate to 3D object editing

## BACKGROUND

- limitations of 3D object editing

## DETAILED DESCRIPTION

- introduce systems and methods
- describe editing module functionality
- explain MM generator usage
- identify challenge of building MM generator
- propose solution using VADs and VAEs

### Networked Computing Environment

- introduce messaging system 100
- describe client device 102
- describe messaging client 104
- describe applications 106
- describe messaging server system 108
- describe data exchange between messaging clients 104
- describe data exchange between messaging client 104 and messaging server system 108
- describe application servers 114
- describe database server 120
- describe web server 128
- describe API server 116
- describe functions supported by API server 116
- describe messaging server 118
- describe image processing server 122
- describe social network server 124
- describe entity graph 308
- describe external resource features
- describe launching external resources
- describe processing markup-language documents
- describe notifying users of external resource activity
- describe sharing items in external resources
- describe response messages in external resources
- describe presenting available external resources
- describe context-sensitive menu
- describe system architecture
- describe ephemeral timer system 202
- describe collection management system 204
- describe curation interface 206
- describe augmentation system 208
- describe map system 210
- describe game system 212
- describe external resource system 214
- describe cross-modal shape and color manipulation system 216
- describe user-based publication platform
- describe merchant-based publication platform
- describe map-based media content and messages
- describe displaying user icons on a map
- describe sharing location and status information
- describe game interface
- describe launching games
- describe in-game rewards
- describe external resource system 214
- describe third-party servers 110
- describe SDK
- describe integrating SDK into web-based resources
- describe communication between external resources and messaging client 104
- describe WebViewJavaScriptBridge
- describe limiting shared information
- describe adding visual representation of web-based external resources
- describe authorizing external resources to access user data
- describe cross-modal shape and color manipulation system 216

### Data Architecture

- define data structures
- describe database 126
- introduce message table 302
- detail message data
- describe entity table 306
- introduce entity data
- link entity table to entity graph 308
- describe entity graph 308
- store relationships and associations
- introduce profile data 316
- describe profile data
- store avatar representations
- introduce augmentation table 310
- describe augmentation data
- apply filters to images and videos
- introduce video table 304
- describe video data
- introduce image table 312
- describe image data
- store augmented reality content items
- describe real-time video processing
- perform object detection and tracking
- modify elements of objects
- transform frames of video stream
- use Active Shape Model (ASM) algorithm
- detect facial feature reference points
- align shapes to mean shape
- conform shape to global shape model
- capture image or video stream
- perform complex image manipulations
- introduce story table 314
- describe story data
- create personal story
- create live story
- create location story
- associate augmentations with images and videos
- store data in tables

### Data Communications Architecture

- introduce message 400
- describe message identifier 402
- detail message text payload 404
- describe message image payload 406
- describe message video payload 408
- describe message audio payload 410
- describe message augmentation data 412
- introduce message duration parameter 414
- introduce message geolocation parameter 416
- describe message story identifier 418

### Time-Based Access Limitation Architecture

- illustrate access-limiting process
- introduce ephemeral message with duration parameter
- describe message timer functionality
- introduce ephemeral message group with duration parameter
- describe group participation parameter
- illustrate group timer functionality
- describe overall lifespan control of ephemeral message group
- describe expiration of ephemeral message within group
- describe removal of ephemeral message from group
- describe removal of ephemeral message group
- introduce indefinite group duration parameter
- describe expiration of ephemeral message group
- describe communication with messaging system upon expiration

### Cross-Modal Shape and Color Manipulation

- illustrate system for cross-modal shape and color manipulation
- describe multi-modal generator architecture
- define latent space composition
- introduce variational auto-decoders (VADs)
- describe output of α VAD
- describe output of β VAD
- combine SDFs with 3D color
- generate 3D shape
- determine 2D sketches
- determine 2D RGB views
- train MM generator with ground truth
- illustrate system for training MM generator
- describe MM encoder architecture
- generate latent code z
- describe training module
- compare generated output with matched triplet
- define Evidence Lower Bound (ELBO)
- describe reconstruction loss
- estimate parameters of MM encoder
- learn three modalities
- define objective function for training
- define cross-modal shape and color manipulation
- introduce equation for latent code
- describe system for cross-modal shape and color manipulation
- explain editing module functionality
- describe generating 3D shape from latent code
- explain determining updated latent code
- describe generating multiple 3D shapes
- introduce mapping function for latent space
- explain learning mapping function
- describe generating 2D sketches and 2D RGB views
- illustrate example of cross-modal shape and color manipulation
- describe editing 3D shape by editing 2D sketch
- illustrate example of cross-modal shape and color manipulation
- describe editing 3D shape by editing 2D RGB view
- illustrate examples of cross-modal shape and color manipulation
- describe generating 3D shape from 2D RGB view
- illustrate examples of cross-modal shape and color manipulation
- describe editing 2D sketch and generating 3D shape
- illustrate examples of cross-modal shape and color manipulation
- describe editing 2D RGB view and generating 3D shape
- illustrate examples of cross-modal shape and color manipulation
- describe effects of occlusion on shape generation
- compare MM-VADs with encoder-decoders
- illustrate example of cross-modal shape and color manipulation
- describe generating 3D shape from 2D sketch
- describe coloring 2D RGB view
- describe generating 3D shape from colored 2D RGB view
- illustrate method for cross-modal shape and color manipulation
- access 2D sketch
- determine latent code corresponding to 2D sketch
- generate 3D shape from latent code
- display 3D shape on display of computing device

### Machine Architecture

- introduce machine architecture
- describe machine components
- illustrate machine 2100
- explain instructions 2110
- describe processors 2104
- detail memory 2106
- explain I/O components 2102
- describe user output components 2126
- describe user input components 2128
- introduce biometric components 2130
- describe motion components 2132
- describe environmental components 2134
- describe position components 2136
- explain communication components 2138
- describe network interface component
- describe wired communication components
- describe wireless communication components
- describe cellular communication components
- describe NFC components
- describe Bluetooth components
- describe Wi-Fi components
- describe other communication components
- describe RFID tag reader components
- describe NFC smart tag detection components
- describe optical reader components
- describe acoustic detection components
- describe IP geolocation
- describe Wi-Fi signal triangulation
- describe NFC beacon signal detection
- describe other location detection methods
- explain software storage
- describe transmission of instructions
- describe reception of instructions
- explain software execution

## Glossary

- define modules
- explain hardware modules
- introduce software modules
- define carrier signal
- explain transmission medium
- introduce client device
- describe mobile phone as client device
- describe desktop computer as client device
- describe laptop as client device
- describe communication network
- explain ad hoc network
- introduce intranet
- describe extranet
- explain virtual private network
- introduce local area network
- describe wireless LAN
- explain wide area network
- introduce wireless WAN
- describe metropolitan area network
- introduce component
- explain hardware component
- introduce software component
- define ephemeral message
- explain non-transitory computer-readable storage medium

