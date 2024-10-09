# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate object detection

## SUMMARY

- motivate pose estimation
- introduce pose estimation method
- describe iterative optimization procedure
- define loss function
- describe renderer
- outline embodiments

## DETAILED DESCRIPTION

- introduce pose estimation method PEM
- provide initial multi-dimensional pose Tpr(0) of object of interest OBJ
- estimate refined object pose Tpr(NL) with NL≥1
- define loss function LF(k) for iterative optimization procedure IOP
- describe iterative optimization procedure IOP
- apply gradient-based method for object pose updates ΔT
- obtain segmentation mask SEGrend(k, i) for each rendered 2D-3D-correspondence map Ψrendk,i
- define loss function LF(k) as per-pixel loss function
- describe differentiable renderer dREND
- determine initial object pose Tpr(0) in step S0
- provide images IMA(i) of object of interest OBJ with known imaging parameters PARA(i)
- process images IMA(i) in determination step DCS to determine 2D-3D-correspondence maps Ψpri and segmentation masks SEGpr
- apply coarse pose estimation step CPES to determine initial object pose Tpr(0)
- describe Perspective-n-Point approach (PnP) and random sample consensus approach (RANSAC)
- introduce pose estimation system for refining initial multi-dimensional pose Tpr(0)
- summarize objective of presented solution
- describe multi-view refinement method
- provide publications for detailed explanation of teachings
- describe exemplary real-world scene with object of interest OBJ
- introduce pose estimation method PEM
- subdivide PEM into initial pose estimation procedure PEP and pose refinement procedure PRP
- describe initial pose estimation procedure PEP
- capture images IMA(i) with parameters PARA(i)
- process images IMA(i) to determine segmentation masks SEGpr(i) and 2D-3D-correspondence maps Ψpri
- apply DPOD approach to determine SEGpr(i) and Ψpri
- describe modified DPOD approach with two substeps DCS1 and DCS2
- apply NOCS parameterization
- perform coarse pose estimation step CPES
- apply Perspective-n-Point approach (PnP) and RANSAC
- summarize initial pose estimation procedure PEP
- introduce pose refinement procedure PRP
- describe iterative optimization procedure IOP
- render correspondence maps Ψrendk,i and segmentation maps SEGrend(k, i)
- determine loss function LF(k)
- update object pose Tpr(k) based on loss function LF(k)
- describe loss determination step LDS
- apply gradient-based method for object pose update ΔT
- conclude pose refinement procedure PRP

