# DESCRIPTION

## BACKGROUND

- introduce computer vision and graphics

## DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS

- introduce volume rendering approaches
- limitations of current volume rendering approaches
- introduce generic renderers
- advantages of generic renderers
- limitations of generic renderers
- introduce differentiable volume renderer using neural Gaussian Ellipsoids (VoGE)
- VoGE combines advantages of both volume and generic renderers
- explicit representation of object geometry in VoGE
- rendering using volume rendering formulation in VoGE
- approximate closed-form solution for volume density aggregation in VoGE
- various tasks performed by VoGE
- system integration of VoGE
- example system architecture
- client computing devices and cloud network
- plurality of computing nodes
- models for performing computer vision/graphics related tasks
- VoGE utilized by or integrated into various models
- example rendered surface normal with converted Stanford Bunny mesh
- example rendering pipeline of VoGE
- kernel reconstruction for volume rendering
- anisotropic Gaussian ellipsoid kernels for reconstructing arbitrary 3D shapes
- example process implementing VoGE
- define VoGE density function
- describe Gaussian ellipsoids reconstruction
- illustrate VoGE process
- reconstruct object into Gaussian ellipsoids
- sample viewing rays and compute volume density
- determine occupancy along viewing rays
- approximate volume density aggregation
- reweight Gaussian ellipsoids
- synthesize image using computed weights
- compare VoGE with other renderers
- evaluate pose estimation performance
- illustrate qualitative object pose estimation results
- demonstrate VoGE for neural view matching and texture extraction
- show shape fitting results using VoGE
- describe computing device architecture
- detail CPU and chipset functionality
- explain memory and storage components
- describe network connectivity options
- detail storage device and management component
- explain data transformation and storage
- describe access to computer-readable storage media
- detail operating system options
- explain computer-executable instructions
- describe input/output controller functionality
- discuss virtual machine instances
- clarify terminology and scope
- define "optional" and "comprise"
- explain exemplary and such as
- describe combinations of components
- discuss hardware and software embodiments
- explain computer program products
- describe block diagrams and flowcharts
- discuss scope and variations

