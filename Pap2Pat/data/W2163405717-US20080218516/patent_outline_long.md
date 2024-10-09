# DESCRIPTION

## FIELD OF THE INVENTION

- relate to image processing

## BACKGROUND OF THE INVENTION

- define light field factorization
- motivate prior art limitations
- summarize surface light field decomposition
- describe inverse shade trees
- describe time-varying surface appearance
- motivate complexity of BRDF acquisition
- describe inverse rendering
- summarize photometric properties recovery
- describe separating light field components
- motivate time-lapse photography challenges
- describe intrinsic image representation
- summarize reflectance field determination

## SUMMARY OF THE INVENTION

- introduce factorization method
- describe application to outdoor scenes
- summarize shadow, sunlight, and skylight components
- motivate image editing and computer vision applications

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce camera acquiring image sequence
- describe scene with moving light source
- define lighting factors
- explain direct and indirect illumination
- introduce reflectance
- factor light field into sunlight, skylight, and shadow components
- construct appearance profiles
- factor appearance profiles into shadow, sunlight, and skylight components
- describe shadow component
- describe sunlight component
- describe skylight component
- outline method for factoring image sequence
- estimate shadow, skylight, and sunlight components
- subtract skylight to obtain sunlight component
- factor sunlight component
- describe image formation process
- factor transport matrix into shadow and skylight components
- approximate incident lighting
- estimate Isky, Ssun, and R from sequence of frames
- describe shadow estimation
- segment out sky portions
- use drastic variation in appearance profiles to estimate shadow profiles
- determine median value of smallest intensities
- set shadow profile to 'one' or 'zero'
- show shadow image
- use edge-preserving bilateral filter to produce final shadow image
- describe factorization
- assume similarly textured and oriented surfaces reflect light similarly
- estimate surface normals for complex outdoor scenes
- represent appearance profiles as linear combination of basis matrices
- determine basis profile
- store weights in sunlight image
- approximate surface normal of scene point
- show appearance profiles when pixels are in shadow
- show estimated skylight profiles
- show appearance profiles when pixels are in sun
- show estimated sunlight profiles
- describe factorizing appearance profiles
- apply ACLS to decompose appearance profiles
- describe skylight and sunlight images
- discuss reconstruction quality, compression, and editing capabilities

### Effect of the Invention

- show images processed according to the embodiment of the invention
- describe applications of the invention

