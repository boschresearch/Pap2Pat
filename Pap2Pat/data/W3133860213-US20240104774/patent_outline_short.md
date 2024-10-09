# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate object detection

## SUMMARY

- introduce pose estimation method
- describe iterative optimization procedure
- outline loss function

## DETAILED DESCRIPTION

- introduce pose estimation method PEM
- describe initial multi-dimensional pose Tpr(0) and 2D-3D-correspondence map Ψpri
- explain iterative optimization procedure IOP with loss function LF
- define loss function LF as per-pixel loss function
- describe renderer dREND and segmentation mask SEGrend
- explain determination of initial object pose Tpr(0) in step S0
- describe coarse pose estimation step CPES using Perspective-n-Point approach
- summarize pose estimation system for refining initial pose Tpr(0)
- outline multi-view refinement method for improving detectors trained on synthetic data
- introduce pose estimation method PEM
- describe initial pose estimation procedure PEP
- motivate DPOD approach for determining segmentation masks and 2D-3D-correspondence maps
- describe coarse pose estimation step CPES using PnP and RANSAC
- summarize initial pose estimation procedure PEP
- introduce pose refinement procedure PRP using differentiable renderer dREND
- describe iterative optimization procedure IOP for refining object pose
- detail loss function LF for assessing object pose correctness
- conclude pose refinement procedure PRP

