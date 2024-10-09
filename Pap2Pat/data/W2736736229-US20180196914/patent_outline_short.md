# DESCRIPTION

## BACKGROUND

- introduce stem cells

## SUMMARY

- motivate virtual cell simulator
- outline method for generating 3D virtual cell model
- outline system for generating 3D virtual cell model

## DETAILED DESCRIPTION

- introduce cell behavior on substrates
- describe physical, chemical, and mechanical properties of ECM
- motivate development of virtual cell model
- introduce virtual cell model and its components
- describe applications of virtual cell model

### A. Theoretical Background

- describe triangulated membrane model
- model cytoskeleton as physical network
- model chromatin fibers using beads and springs
- describe interaction between cell and ECM
- introduce explicit solvent model (MPCD)

### B. Overview of the Software Architecture

- outline software architecture

### C. Details Regarding the Software Architecture

- configure virtual cell model
- input cell and substratum characteristics
- set cytoskeleton parameters
- import ECM configuration
- input chromatin fiber parameters
- set solvent parameters
- initialize simulation materials
- integrate equations of motion
- update system configuration
- calculate internal forces of cytoskeleton
- calculate internal forces of chromatin fibers
- calculate internal forces of ECM
- implement interactions between components
- update system configuration and perform post-processing

### Example 1: Prediction of Cell and Nucleus' Geometries on Grooved Substrates

- investigate cell elongation on grooved substrates
- analyze effect of substrate geometry on nuclear shape and chromatin reorganization

### Example 2: Cell-Substrate Stiffness Modeling Using a 3D-Elastic Network

- study virtual cell response to ECM elasticity using 3D-elastic networks

### Example 3: Prediction of Stem Cell Geometry and Chromatin Conformation on Cell-Imprinted Substrates

- predict stem cell geometry on cell-imprinted substrates
- analyze chromatin conformational changes during differentiation
- track variation of cell and nucleus shapes during differentiation
- understand mechanisms of shape-induced physical differentiation of stem cells
- implement virtual cell model through computer software
- describe computer system for implementing virtual cell model

