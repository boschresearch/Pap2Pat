# DESCRIPTION

## BACKGROUND OF THE INVENTION

- relate to technical field
- describe CAD/CAM software tools
- describe finite element analysis
- limitations of CAE geometric representation
- describe trimmed NURBS
- limitations of mesh generation

## SUMMARY OF THE INVENTION

- introduce T-spline based isogeometric analysis

## DETAILED DESCRIPTION OF A PREFERRED EMBODIMENT

- motivate T-spline based isogeometric analysis
- describe limitations of traditional DTA approaches
- introduce T-spline and T-NURCC based isogeometric analysis method
- describe importance of tight integration of CAD, geometry, meshing, and analysis
- highlight limitations of traditional ASG
- describe significance of geometric accuracy in analytical results
- motivate need for accurate geometry and mesh adaptivity
- highlight importance of tightly integrated geometry, meshing, and analysis
- introduce T-spline and T-NURCC based isogeometric analysis as a viable alternative

### II. Background

- define notation for T-spline basis functions
- define quantities used in T-spline basis functions
- introduce T-splines and T-NURCCs
- describe advantages of T-splines and T-NURCCs over NURBS
- define T-spline basis function
- define geometric coefficient and weighing associated with control points
- define T-spline basis function in terms of geometric coefficient and weighing
- define T-spline
- introduce T-mesh
- describe T-mesh as a non-hierarchical approach
- describe local refinement using T-junctions
- infer basis functions from a T-mesh
- describe correlation between topological entities and basis functions
- describe inferring local knot vector structure for complete odd polynomial ordered basis function
- describe inferring local knot vector structure for mixed polynomial ordered basis function
- describe inferring local knot vector structure for complete even polynomial ordered basis function
- describe exact subdivision of T-spline basis functions
- describe exact local refinement
- generalize exact local refinement to multivariate case
- introduce T-spline volumes
- generalize local non-hierarchical refinement capability to T-spline volumes
- introduce T-NURCCs
- describe T-NURCCs as a generalization of T-splines to T-meshes of arbitrary topology

### 3.1 Overview

- introduce generating analysis suitable geometry from T-spline or T-NURCC CAD description
- define analysis suitable geometry (ASG)
- describe need to modify CAD description for analysis applications
- describe conversion of T-spline CAD descriptions into ASG
- highlight importance of boundary interpolation
- describe explosion into NURBS patches
- introduce transforming ASG into analysis ready data

### 4.1 Overview

- transform native geometric ASG data
- define abstractly native geometric data
- define abstractly analysis ready data
- note many possible instantiations
- motivate transformation
- describe limitations of computing with T-spline basis
- describe difficulty of automating discretization
- introduce Bézier decomposition
- describe benefits of Bézier decomposition
- note encapsulation property
- describe ease of adoption
- balance generality, efficiency, and adoption
- summarize transformation process
- describe exact geometric mapping
- conclude section

### V. Use ASG Analysis Ready Data in a T-Spline Based IGA Code Structure

- introduce IGA computational framework
- describe element stiffness matrices and force vectors
- relate kts,ε to kbb,ε
- relate fts,ε to fbb,ε
- describe assembly procedure
- introduce shape function subroutines
- compute local quantities
- compute global quantities
- describe adaptive refinement
- describe non-hierarchical refinement
- describe hierarchical refinement
- describe refined IGA element set
- conclude section

