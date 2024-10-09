# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce technical field
- describe limitations of current CAD/CAE systems
- motivate need for improved method

## SUMMARY OF THE INVENTION

- outline preferred embodiment

## DETAILED DESCRIPTION OF A PREFERRED EMBODIMENT

- motivate T-spline based isogeometric analysis
- limitations of traditional DTA approaches
- introduce T-spline and T-NURCC based isogeometric analysis method
- overview of isogeometric analysis framework

### II. Background

- define notation for T-spline basis functions
- introduce T-splines and T-NURCCs
- define T-spline basis functions
- define T-spline
- introduce T-mesh
- infer basis functions from a T-mesh
- infer local knot vector structure for complete odd polynomial order
- infer local knot vector structure for mixed polynomial order
- infer local knot vector structure for complete even polynomial order
- introduce local T-spline basis function subdivision and exact refinement
- introduce T-spline volumes and T-NURCCs

### 3.1 Overview

- overview of generating analysis suitable geometry
- define analysis suitable geometry
- motivate conversion of T-spline CAD descriptions into ASG

### 4.1 Overview

- transform native geometric ASG data into analysis ready data
- define abstractly native geometric data
- define abstractly analysis ready data
- motivate transformation of basis
- discuss limitations of computing with T-spline or T-NURCC basis
- introduce Bézier decomposition
- highlight benefits of approach

### V. Use ASG Analysis Ready Data in a T-Spline Based IGA Code Structure

- overview of IGA code structure
- define IGA finite element
- generate element stiffness matrices and force vectors
- relate local T-spline and Bernstein basis functions
- discuss shape function subroutines
- introduce adaptive refinement

