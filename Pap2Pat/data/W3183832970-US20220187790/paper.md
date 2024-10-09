# INTRODUCTION

This paper presents a unified framework for 3D printing highly detailed and smooth surfaces from compact representations by robustly and efficiently computing displaced signed distance fields, which represent the shape implicitly as the composition of a discrete signed distance field and a displacement field. The displacement field encodes the offset from a discrete voxel approximation to the true surface. We show how this formulation allows the use of efficient, streaming algorithms operating on discrete voxel grids while maintaining sub-voxel accuracy, and show how to use this framework to 3D print coarse tessellations with displacement maps encoding mesoscopic detail, curved surfaces, and incomplete or self-overlapping surfaces.

As the resolution and accuracy of 3D printers increase, accurate reproduction of finely detailed and smoothly curved surfaces becomes increasingly realizable from a hardware perspective. Representing surfaces with polygonal meshes to an accuracy on the order of modern 3D printers requires a large number of polygons, correspondingly increasing requirements for storage and bandwidth for transmission. Further, the same approximation accuracy requires different levels of tessellation for different print sizes.

With increasing use of graphical 3D printing in the entertainment sector, for films or 3D printing content from game engines, automated and efficient processing of graphical 3D content from these applications becomes increasingly important. Such models often reduce polygon counts by encoding mesoscopic geometric detail in displacement maps, topographic textures or height maps applied to a low-poly mesh. Thus, it is advantageous to directly support this type of input (Fig. 1, center) without computationally demanding tessellation, which can introduce further errors in the form of self-intersections and inverted surfaces. Since they are designed for on-screen display, not physical fabrication, such models are often composed of open, overlapping surfaces and decals. The mesh in Fig. 1 (center) is comprised of disjoint patches with small gaps in between. Thus, robust processing is key to automation.

Over half of parts produced by additive manufacturing are either functional parts or functional prototypes [Wohlers et al. 2020]. These are often designed and represented by parametric patches, rather than polygonal meshes. The typical workflow still involves tessellating these surfaces into polygonal meshes, which in general introduces a discretization error. Tessellation into meshes of curved triangles is an alternative, which scales much better in terms of making the approximation error significantly less sensitive to the scale of the printed part. Existing approaches to fabrication with curved triangles are based on subdivision, again requiring different amounts of subdivision for different print sizes. This paper shows how displaced signed distance fields can realize curved trianglebased shapes to printer resolution without tessellation (Fig. 1, right).

Making a 3D copy of a real object involves scanning that object, the output of which often comes in the form of a point cloud, and typically there are portions of the surface which cannot be scanned, resulting in an incomplete surface (Fig. 1,left). Directly processing such data for 3D printing can also streamline workflows.

For applications in graphical 3D printing, including rapid prototyping and entertainment, the build volumes and resolutions of modern devices mean any method needs to scale up to nearly 10 12 voxels [Mimaki 2017;Stratasys 2016]. This constrains us to algorithms that have complexity linear in the number of voxels, or constant time per voxel. More restrictively, it constrains us to so-called streaming compatible algorithms, which require a peak storage less than 1 byte per voxel for large prints. We define such algorithms formally in Section 3.

In this paper, our primary technical contribution is a unified implicit formulation and resulting algorithmic framework to robustly and efficiently

• produce highly detailed surfaces from low-polygon meshes with an attached displacement map, • produce smooth surfaces from low-polygon meshes of higher order primitives.

We further propose a technique for representing surface structures with local feature size on the order of, and even below, the voxel size. Our formulation gives rise to algorithms with the following advantages:

• it combines the efficiency of discrete voxel distance computations, running in 𝑂 (1) time per voxel, with sub-voxel accuracy and bounded error w.r.t. the true signed distance; • it is streaming compatible, requiring less than 1 byte per voxel for large prints; • it supports unbounded displacement and performs no further tessellation or refinement; • and it robustly handles incomplete, non-manifold and selfoverlapping input.

In particular, if we consider as an alternative computing the true signed distance field (SDF), we would encounter the following problems. In the case of displacement maps or curved higher-order primitives, we would need to first tessellate to a desired tolerance (thus introducing some error anyways), along with the associated problems of potential self-intersection. Doing this on-the-fly within a streaming context would require bounded displacements. To compute the exact distance field w.r.t. the tessellation would need a bounding volume hierarchy (BVH) or similar space partitioning, resulting in running time logarithmic in the number of primitives, which would be large in the case of refined tessellation. Our displaced SDF provide an good approximation of the true SDF, and allows more efficient and robust processing.

# RELATED WORK 2.1 Robust Voxelization

For sufficiently clean data, i.e. watertight and manifold, conversion to a solid voxel representation can be done very efficiently, in particular leveraging parallelism on the GPU [Eisemann and Decoret 2008;Schwarz and Seidel 2010].

The more challenging problem of converting surface data that does not represent the boundary of a volume, whether corrupt, incomplete, or intentionally designed so by an artist, has also been studied. Nooruddin and Turk [Nooruddin and Turk 2003] propose a "ray-stabbing" technique to convert a polygonal model to voxels. This technique is limited to a small voxel grid as it requires the full voxel grid in memory simultaneously.

The generalized winding number [Jacobson et al. 2013] provides a way to robustly determine whether a point lies inside or outside a curve of surface by extending the winding number to open curves and surfaces. This inherits the winding number's natural handling of self-overlapping surfaces, behaves smoothly in holes, and degrades gracefully in the presence of noise or inconsisten surface orientation. Barill et al. [2018] provided a fast approximate evaluation for triangle soups and point clouds based on a multipole expansion, and showed some robust voxelization examples. Schmidt [2019] describes converting an unsigned distance field into a SDF using a flood fill approach, starting at one or more voxels known to be outside the surface and stopping at inversions of the gradient. It is not clear that this technique can work for large holes, or is practical for large voxel grids. Another technique [Stevens and McKenna 2018] computes a SDF of a polygon mesh by generating multiple layered depth images [Shade et al. 1998], and using them to resolve tessellation inconsistencies to compute signed distances. Krayer and Müller [2019] propose a GPU-based approach based on ray-maps, which is both fast and robust, but does not appear to scale well to large voxel grids.

## Surface Repair

There are many existing methods for surface repair, both those specifically targeting 3D printing and those targeting more general application areas. Most of these operate directly on a mesh. Such methods benefit from local operations and are therefore quite efficient. Difficulties arise in simultaneously handling holes, nonmanifold edges and vertices, islands (disconnected pieces), and selfintersection. Most methods to convert arbitrary collections of polygons into surfaces do not robustly handle self-intersection [Guéziec et al. 2001;Hoppe et al. 1993;Kraevoy et al. 2003;Podolak and Rusinkiewicz 2005] in that they do not guarantee a watertight output. Methods that do offer guarantees typically fall into two categories: those that globally remesh the surface [Bischoff et al. 2005;Ju 2004] and those that remove parts of the mesh that are difficult to handle, either creating holes and refilling them [Attene 2010] or specifically removing parts causing self-intersections [Yamakawa and Shimada 2009]. In our application, global remeshing would be acceptable, and our surface voxelization stage can be seen as an approximate resampling of the surface. However, we are interested in obtaining an implicit representation, which we can combine with mesoscopic detail information.

## Surface Reconstruction and Meshing

Our approach is also related to surface reconstruction from point cloud data, although we do not propose our algorithm as a solution for surface reconstruction. We view our work as complementary, since the reconstructed mesh can also serve as an input to our framework. Berger et al. provide a comprehensive recent survey [2017]. We discuss the most closely related methods here.

Poisson [Kazhdan et al. 2006] and screened Poisson [Kazhdan and Hoppe 2013] surface reconstruction solve for an indicator or characteristic function, which can be seen as equivalent to our sign function, by observing that its gradient at the surface should align with the surface normal. For efficiency, they discretize using an octree to obtain a sparse linear system and to simultaneously avoid computations away from the surface. Implicit moving least squares [Kolluri 2005], its variant based on robust estimation [Oeztireli et al. 2008], and others, follow the gradient of an implicit function to the surface. These techniques reduce computational effort by evaluating only in the vicinity of the surface. To apply displacement, we need to consider possibly large distances from the surface, and for this reason we must compute a signed distance, and therefore a sign, at all voxels in our bounding volume. Given this restriction, sophisticated regularization, such as solving a PDE, is too costly.

## Deep Learning Methods

Recently a slew of new techniques propose to use deep neural network architectures to learn object-specific representations, which allow the approximate reconstruction of a SDF for that object. Erler et al. [2020] show robustness to severe noise levels by learning a global sign function and a local distance function, exploiting the generalizing power of local patches and the low complexity of sign information. Sign agnostic learning [Atzmon and Lipman 2020] provides indifference to errors in surface orientation, at the cost of limited detail preservation and robustness to thin structures. Including an Eikonal constraint in the loss improves reconstruction of sharp features and thin structures [Atzmon and Lipman 2021;Gropp et al. 2020]. Davies et al. [2021] propose to use an overfit neural network as a compact implicit shape representation. Sitzmann et al. [2020] also showed implicit shape encoding as an application. While this line of work present exciting results, these methods are too computationally intensive for our application. Even approaches using offline training [Erler et al. 2020] require a forward pass per signed distance evaluation, and shape representation/reconstruction approaches require training per object.

## Displacement Mapping

Displacement mapping [Cook 1984;Cook et al. 1987] is a common technique in rendering, particularly ray tracing and ray marching, with efficient GPU implementations [Szirmay- Kalos and Umenhoffer 2006]. A height field texture provides the meso-scale information about the surface, specifying the distance along the surface normal of the tessellation to the true surface.

OpenFab [Vidimče et al. 2013] applies displacement maps by first tessellating the models to facets on the order of the printer resolution, displacing the resulting vertices, and then voxelizing. For bounded displacements, by paying close attention to the order in which facets are processed, such a tessellation approach can be done on-the-fly within a streaming framework, and efficient GPU implementations exist. In contrast, our approach can apply unbounded displacements within a streaming computation, without affecting performance, while replacing the geometric operations of tessellation with sampling and writing of displacement values. We show the performance of our framework under displacements of various magnitudes in Section 8.2.

A non-streaming tessellation approach can be implemented in widely available modeling software, e.g. Blender [2020], by first refining the tessellation using subdivision, then displacing vertices. Commercial 3D printing software also displaces the vertices of a densely tessellated mesh [Stratasys 2020]. This leads to high polygon counts and can introduce self-intersections and inverted surfaces, particularly for larger displacements, as shown in Section 8.2. Our approach does not suffer from these problems. While one could leverage techniques from geographic information systems to convert digital elevation maps to meshes [Garland and Heckbert 1995], this would only provide a trade-off between approximation quality and compactness, and would not address self-intersections.

## Curved Triangles

Tessellating parametric surfaces to curved triangles instead of flat ones allows better approximation with fewer primitives. Pointnormal (PN) triangles [Vlachos et al. 2001] are a subset of Bézier triangles [de Casteljau 1959;Farin 1986], in which surface normals specified at each vertex control how the triangle is curved (by determining the control points of the Bézier triangle). In finite element analysis (FEM), Lagrange polynomials are the standard high-order basis for shape functions [Zienkiewicz et al. 2013], and high-order Lagrange polynomials on triangles [Berrut and Trefethen 2004] allow for curved triangles. Like the Bézier basis on triangles, first order Lagrange basis is equal to a barycentric basis.

Techniques exist [Gohari et al. 2018;Starly et al. 2005] to directly slice NURBS surfaces. These are only practical for additive processes based on path following, e.g. fused filament fabrication (FFF), as they work by intersecting slicing planes with the NURBS surface.

## Streaming Distance Field Computation

Recently, Brunton et al. [2018] proposed a technique for unsigned distance field computation, which runs in 𝑂 (1) time per voxel while being streaming compatible, meaning the full voxel grid does not need to be kept in memory; we reproduce their formal definition in Section 3. Their technique involves pre-computing a sparse surface voxelization, also constructed in 𝑂 (1) per voxel with limited memory, stored in ascending order of 𝑧 for each 𝑥𝑦-column. This allows the unsigned distance to the surface voxels to be computed in constant time per voxel when processing slices in order, storing as little as a single slice in memory at once. Similar data structures have also been used for slice thickness optimization [Alexa et al. 2017] and morphological operations [Martinez et al. 2015]. While we use this technique to compute unsigned distances and to identify the nearest surface voxel to a given voxel, it does not address sign estimation, sub-voxel accuracy or displacement. We further reduce the memory footprint during construction by using a hash map on the voxel coordinates, rather than storing dense slices. Our implicit formulation, given in Section 3, makes possible the use of such fast, streaming, voxel-wise techniques for robust and precise fabrication.

# DISPLACED SIGNED DISTANCE FIELDS

Our framework exploits the relationship between implicit representations of a given approximate surface and the true shape. We consider how an incomplete approximation affects distance fields, signed and unsigned, w.r.t. the input and the true surface. We further consider that the approximation may be defined implicitly w.r.t. the true surface, and vice versa, via a displacement field.

In the context of additive manufacturing, we work with implicit representations sampled on a finite voxel grid partitioning the build volume of the device. Let B ⊂ R 3 denote the build volume of the 3D printer, and partition it into 𝑊 × 𝐻 × 𝐷 voxels of size 𝛿 𝑥 , 𝛿 𝑦 , 𝛿 𝑧 along the 𝑥-, 𝑦-and 𝑧-axes of the build space, corresponding to the native resolution of the printer. We further define C ⊂ B to be the set of voxel centers, and 𝑉 (u) ⊂ B to be the voxel containing u ∈ B. Typically, the shape we wish to manufacture fills only a fraction of the device's build volume, and we restrict B to be a padded bounding box of the input, reducing 𝑊 , 𝐻 and 𝐷 accordingly.

The core of our method lies in composing implicit representations of the approximate surface with implicit representations of the true surface w.r.t. the approximation in a way that allows to robustly and efficiently reproduce finely detailed and curved surfaces at device resolution from a compact input. Fig. 2 shows these two scenarios and how the quantities defined below relate to realize them.

Given the resolution and build volumes of modern 3D printers, doing this without storing the full sampling grid is critical. Therefore, in this paper, we concentrate on algorithms that are streaming compatible, which we define as follows in the context of additive manufacturing [Brunton et al. 2018]: Definition 3.1. Since the manufacturing process builds the object from bottom to top, we define streaming computation to proceed in ascending order of z. We further define that for a given print occupying a volume corresponding to a voxel grid of 𝑊 × 𝐻 × 𝐷 voxels, a streaming algorithm never exceeds 𝑂 (𝑊 𝐻 + 𝑁 ) storage, where 𝑁 ≪ 𝑊 𝐻 𝐷; i.e. a constant number of slices (2D array with constant 𝑧-coordinate) plus small auxiliary storage, relative to the size of the voxel grid.

Sections 4 and 7 give further details on how we robustly and efficiently represent shapes at device precision or better within a streaming compatible framework. However, the implicit formulation presented below is key to enabling this, and Section 3.1 discusses its advantages as an approximation versus computing the true SDF.

Given a shape S ⊂ R 3 s.t. |S| < ∞ and its boundary 𝜕S is a closed manifold embedded in R 3 , let

denote the unsigned distance of any point u ∈ R 3 to its nearest point in 𝜕S and

In practice, we consider an approximation 𝜕S of the true surface 𝜕S, which may differ in several ways. One possibility is an incomplete version or a point sampling of the true surface, 𝜕S ⊂ 𝜕S. Now, our unsigned distance

gives us only an upper bound, 𝑑 (u) ≥ |𝑓 (u)|, on the distance to the true surface. We can now compose the signed distance, 𝑓 , to 𝜕S, as

where

Further, 𝜕S may be locally displaced w.r.t. 𝜕S. In particular, we take 𝜕S to be a sparse voxel representation constructed from a set of input primitives P, which may be points or triangles. More precisely 𝜕S ⊆ C is the set of center points of those voxels. This introduces quantization error due to finite voxel resolution, which we model as the negative signed distance to the nearest point on a primitive 𝑝 ∈ P of the center of a voxel, 𝜙 P : 𝜕S ↦ → R. The advantage of working from voxel centers is that it enables efficient distance field computation at low memory cost. Section 4 goes into more detail.

Additionally, the true surface may be displaced w.r.t. the input primitives, e.g. due to the use of a coarse tessellation to approximate a detailed or smooth surface. We model this displacement as an offset along the outward normal n 𝑝 of primitive 𝑝,

where 𝜙 S : P ↦ → R is a displacement map giving the signed distance of the true surface w.r.t. the primitives. The full displacement field 𝜙 : 𝜕S ↦ → R from 𝜕S to 𝜕S is combined as in Section 4. Now we write our displaced SDF definition to be

where

is the nearest point on 𝜕S to u ∈ R 3 .

## Approximation Power of 𝑓

In general, 𝑓 ≠ 𝑓 , and is not a metric SDF satisfying the Eikonal equation due to the high frequency content and discontinuities potentially introduced by the term 𝜙 (u) in ( 6). This section shows under what conditions it shares the same 0-level set as 𝑓 ,

and gives bounds on the error of the 0-level of of 𝑓 , 𝜖 0 = 𝑓 (u) for u s.t. 𝑓 (u) = 0. To simplify the analysis, we assume an isotropic voxel grid with voxel size 𝛿 = 𝛿 𝑥 = 𝛿 𝑦 = 𝛿 𝑧 .

When 𝜙 = 𝜙 P captures just the distance from the voxel centers to the primitives and P ⊆ 𝜕S, then (8) holds for most orientations Fig. 2. An overview of our framework for two scenarios. In scenario (a), we are given a low-poly mesh with an albedo texture and a displacement map encoding mesoscopic surface detail. In scenario (b), we are given a polygonal mesh comprised of curved triangles, in this case point-normal triangles [Vlachos et al. 2001] with per-vertex normals. See Section 3 for definitions of the quantities in the boxes.

of planar surfaces and nearly holds for piecewise planar surfaces approximating smooth curved surfaces. For planar surfaces where the normal is nearly aligned with one axis, so that the voxelization is a single voxel thick, but not exactly aligned, we have a small error 𝜖 0 ≠ 0. In Appendix A we show that surface orientations, which result in surface voxels on both positive and negative sides of the surface result in 𝜖 0 = 0, and otherwise |𝜖 0 | < 0.029𝛿. This bound also holds when a planar surface is endowed with a non-zero displacement field 𝜙 S . In Appendix A we also analyze the error for voxels away from the surface.

For curved surfaces the analysis becomes more complex, but Fig. 3 shows empirically that the error of a surface extracted in this way remains near zero for low curvature regions and increases only to a small fraction of the voxel size for higher curvature regions.

We have shown that 𝑓 provides a high quality approximation of the true SDF 𝑓 , and in particular their 0-level sets are very close. And this approximation allows us to use efficient, streaming compatible algorithms operating on discrete grids. Computing the "true" SDF would require fine tessellation, followed by some kind of BVH to compute distances. This would introduce the potential for selfintersecting or inverted surfaces, complexity logarithmic in the number of primitives (after fine tessellation), and restrictions on the displacement magnitude. Displaced SDFs make a deliberate and bounded error in return for efficiency and flexibility.

# SUB-VOXEL BOUNDARY APPROXIMATION

We represent 𝜕S as a sparse set of voxels, per Brunton et al. [2018], allowing 𝑂 (1) per-voxel computation of 𝑑, and the nearest point u ∈ 𝜕S ∀ u ∈ C, which we reference with a globally unique index. A surface voxelization pre-process generates our sparse surface voxels 𝜕S from the input primitives P, which may be points or triangles. Section 7.1 goes into more detail on this process. Important for the present discussion is that we compute a conservative 26-separating surface voxelization of triangles, registering every triangle-voxel intersection. For background and terminology on surface voxelization, please refer to Cohen-Or and Kaufman [1995].

Compensating for the quantization error introduced by working on a discrete grid is important because the fine scale detail provided by a displacement map is given relative to the primitives, and not the surface voxel centers. We do so by storing the signed distance of the voxel center relative to the primitives incident to that voxel

where u ∈ 𝜕S, P (u) ⊆ P is the set of primitives with non-empty intersection with 𝑉 (u), n 𝑝 is the normal of primitive 𝑝, and c 𝑝 (u) is the centroid of the intersection 𝑝 ∩ 𝑉 (u) of the primitive and the voxel relative to u (i.e. shifted so that the voxel center u is at the origin). We also average displacements from the primitives to the true surface, such that

which can be combined in a single summation over in the incident primitives. This allows us to compute 𝜙 (u) incrementally as each primitive is voxelized, independent of the order.

In the case where P ⊆ 𝜕S, i.e. the flat input primitives are at least a subset of the true surface, we have 𝜙 (u) = 𝜙 P (u). Fig. 3 shows how this improves the precision of the voxel representation. Fig. 3a,b show iso-surfaces extracted from 𝑠 (u) 𝑑 (u) and 𝑓 (u), respectively, with 𝜙 (u) = 𝜙 P (u). Fig. 3a shows clear quantization error, whereas (b) closely matches the input (c). The respective errors 𝜖 0 are visualized in (d) and (e).

Human-created models and scaled versions of scanned objects will in general include structures with local feature size below the device resolution. While such features are not directly printable, we wish to preserve them since techniques exist to make them printable (see e.g. Reinhard [2017] and the references therein). Averaging surface normals when multiple primitives intersect the same voxel is numerically sensitive, and fails to properly model sharp edges or corners, crevices, or tubular structures. One could compute 𝑓 at a higher resolution, and downsample for printing, but this would correspondingly increase the computation time, without solving the problem for structures with feature size below the resolution of 𝑓 .

Instead, we propose to represent sub-voxel structures using a weighted sum of signed distance gradients. Informally, we determine whether each face of the voxel is "looking" out or in from the part of the surface contained within the voxel. Our approach is similar 2D vector glyph rendering [Nehab and Hoppe 2008;Qin et al. 2006], where multiple primitives are stored in a grid cell. One key difference is the fixed storage length of our representation.

Formally, to model how the SDF will change as we move from the voxel center along a given direction, we compute weighted averages of gradients of the SDFs defined by the primitives. Each primitive defines a linear SDF w.r.t. its plane, with its gradient defined by n 𝑝 . For a given direction 𝜔 ∈ 𝑆 2 , we define

where the weights are defined by

where 𝑎 𝑝 (u) is the area of 𝑝 ∩ 𝑉 (u), and 𝛿 𝜔 = [𝛿 𝑥 𝛿 𝑦 𝛿 𝑧 ]𝜔. The term c 𝑝 (u) 𝑇 𝜔 -𝛿 𝜔 /2 gives the distance of the centroid from the boundary of the voxel along the direction 𝜔 from its center, and 𝜎 is controls the fall-off rate of the weight as this term increases.

We set 𝜎 = 0.1 [𝛿 𝑥 𝛿 𝑦 𝛿 𝑧 ] 𝑇 2 . We treat point primitives as having a constant area. Barill et al. [2018] recommend non-uniform areas based tangent plane Voronoi cells, but we use this only for primitives within a single voxel, not to influence queries at a distance.

This approach to representing the geometry inside a voxel has the advantage that it disentangles geometric precision within the voxel (𝜙 P ) and sign information for other voxels ({𝜕 𝜔 𝑖 𝑓 }), which reflects the notion that if the surface intersect a voxel, the sign of that voxel is not unique. Further, this representation can be updated incrementally as primitives are processed, is compact, has fixedlength storage, and allows efficient sign evaluation.

# ESTIMATING SIGN

Having constructed our boundary approximation 𝜕S as in Section 4, we now turn to the problem of computing the sign 𝑠 (u) for all u ∈ C. We proceed in two steps: initializing from the nearest boundary voxel u, then regularizing based on the distance to boundary 𝑑 (u).

## Initialization

For voxel centers u ∈ (C \ 𝜕S) away from the boundary we obtain a sign value from the boundary as

where per (7) u is the nearest surface voxel to u, 1 R + is an indicator function equal to 1 when its argument is > 0 and 0 otherwise, and 𝑁 𝜔 denotes the number of directions along which the gradients are projected. According to (13), we sum up the projected gradients 𝜔 𝑖 𝜕 𝜔 𝑖 𝑓 (u), for which 𝜔 𝑖 • (uu) > 0. If the scalar product of the sum with uu is negative then 𝑠 (u) = -1, otherwise 𝑠 (u) = 1. For voxel centers v ∈ 𝜕S intersected by P, we initialize 𝑠 (v) = 0. Fig. 4 shows the quantities for sub-voxel structures (in 2D). This approach allows surface voxels containing thin walls or tubular structures to export different sign values in opposite directions, while for voxels containing a single primitive it behaves equivalently to sign(n 𝑇 𝑝 (uu)). In practice, we use 𝑁 𝜔 = 6 with 𝜔 1 and 𝜔 2 being the negative and positive 𝑥-axes, 𝜔 3 and 𝜔 4 the negative and positive 𝑦-axes, and 𝜔 5 and 𝜔 6 the negative and positive 𝑧-axes, respectively. This greatly simplifies the evaluation of ( 11) and (13).

Fig. 5 shows how this preserves geometric structures at or below the size of a voxel. The input (a) contains a glasses frame, which is sliced separately at the same scale and orientation in (e) and (f) with a subset of slices shown. Due to the scale it is thin enough to intersect single voxels and cause problems in resolving the sign for adjacent voxels. The evaluation of 𝑠 according to (13) preserves the correct sign for voxels not intersected by the primitives (e), and this is refined after applying sub-voxel displacement (f). This shows that (13) successfully models complex geometry with local feature size below the voxel size everywhere. Section 9 describes some limits on how far below the voxel size we can take this, and how complex the sub-voxel geometry can be.

Fig. 6c and7 show how the binary sign estimation based on the nearest surface voxel (13) extends sign information from incomplete surfaces to complete them. Note, however, the discontinuous distance fields and jagged isosurfaces that it creates.

## Regularization

While the sign evaluation given in ( 13) is robust to sub-voxel structures, for open surfaces it will simply continue the surface linearly from the nearest surface voxel. This results in jagged surfaces, as in Figs. 6c and7. We wish to regularize 𝑠 so that ( 4) is smooth and has equally spaced iso-surfaces.

We experimented with a number of different regularization techniques. For example, we found that Monte Carlo estimation of the Laplace equation Δ𝑠 (u) = 0; u ∉ 𝜕S, similar to [Sawhney and Crane 2020], to be effective in removing low-frequency discontinuities, but converged far too slowly to sufficiently remove high-frequency noise. Instead, we settled on the following efficient regularization.

Laplace regularization is equivalent to imposing the condition

, where 𝐵(u, 𝑟 ) denotes the ball centered on u of radius 𝑟 . The distance field 𝑑 gives us the maximum radius we can use without encountering 𝜕S. Rather than impose the mean value property over the full 3D ball 𝐵(u, 𝑑 (u)), we do so over the 1D axis aligned balls 𝐵 𝑥 (u, 𝑑 (u)), 𝐵 𝑦 (u, 𝑑 (u)) and 𝐵 𝑧 (u, 𝑑 (u)), where e.g.

This amounts to applying a sequence of adaptive 1D mean filters along the 𝑥-, 𝑦-and 𝑧-axes. We implement this using 1D integral images, allowing 𝑂 (1) computation at an additional storage of only 𝑂 (max{𝑊 , 𝐻, 𝐷 }). We experimented with iterating each 1D mean filter to approximate Gaussian filters, but this did not add much benefit for the additional cost. Figs. 6 and7 show the effect of this regularization compared to the unregularized sign function ( 13) for open surfaces. Fig. 8 shows how the regularization performs for further degraded input.

While this does not provide the same level of regularization as PDE-based methods [Barill et al. 2018;Kazhdan et al. 2006;Kazhdan and Hoppe 2013;Sawhney and Crane 2020] or neural architectures [Atzmon andLipman 2020, 2021;Erler et al. 2020;Gropp et 

# Input, slice No regularization Regularization

No regularization Regularization 2020], it is less computationally intensive to evaluate at every voxel, which we require to allow for arbitrarily large displacements. We found this regularization to work well when the hole diameter is below the local feature size. In Section 8.1, we describe how introducing an additional minimum threshold for surface extraction can help with larger holes and missing surface data. Appendix F shows examples of the limits of this approach.

# SURFACE EXTRACTION

We can directly use the displaced SDF slices, e.g. for a preview. [ Lorensen and Cline. 1987] directly from slices of 𝑓 . However, to pair the displaced SDF directly with a device, without generating an intermediate high-poly mesh via marching cubes or other meshing algorithm, we instead extract a sparse set of surface voxels.

From our displaced SDF ( 6), we extract the same ordered-column surface representation [Brunton et al. 2018], which allows subsequent efficient slice-wise evaluation of the unsigned distance to the nearest surface point. In Appendix B, we show how this can be modified for direct slice-wise evaluation of the SDF. Formally, we seek to extract the true surface as the 0 level set of ( 6),

We extract voxels containing 𝜕S to be those with 𝑓 ≤ 0 that have at least one neighboring voxel satisfying 𝑓 > 0. We use a 6-neighborhood, which gives us a 6-separating voxel surface. This ensures a thin and sparse surface.

To address self-overlapping surfaces, we apply a simple floodfillbased hidden surface removal, which simultaneously identifies contiguous regions marked as outside the object according to ( 6) and ( 15), and labels those regions reaching the exterior of B, as exterior regions. A lightweight post-process performs a pass over the surface voxels and discards those not bordering on any exterior regions.

At self-intersections themselves, it can occur that no voxel in the immediate neighborhood has 𝑓 (u) ≤ 0, due to the discrete nature of the distance computation and arbitrary tie-breaking in determining u. To address this, we extract the surface at a small positive iso-level

We found using 𝜏 = max{𝛿 𝑥 , 𝛿 𝑦 , 𝛿 𝑧 } to be sufficient even for surfaces with many small multiply-overlapping components. To subsequently recover 𝜕S, we store 𝑓 (u) with the extracted surface voxels, which we can then use to displace the SDF. Fig. 5b-d shows isosurfaces 𝑓 = 0, 𝑓 = 𝜏 and the re-displaced iso-surface after hidden surface removal, respectively.

# IMPLEMENTATION

We implement our framework in standard C++14, using tbb [Intel 2020] for multi-threading. Algorithms that are streaming compatible according to definition 3.1 are scalable w.r.t. build size at high resolution, but also very limited in the quantities they can store per voxel and the number of dense slices of voxels they can store at once. In our implementation, we store three 4-byte quantities in dense slices of voxels: 𝑑, 𝑓 and an index to look-up the nearest surface voxel. The storage for 𝑓 is initially used to store 𝑠 for filtering before composition (6), and following extraction of 𝜕S 𝜏 the storage for 𝑑 is re-purposed for the floodfill-based hidden surface removal. We processes small chunks of slices at a time; 16 is a typical chunk size, though this is set based on the number of processing cores.

## Sparse Surface Voxelization

To ensure we capture even geometric features below the voxel resolution, we perform a conservative, 26-separating surface voxelization, registering every primitive-voxel intersection. This proceeds chunk wise, incrementally computing the surface voxels for small range along the 𝑧-axis. We do not store all voxels in this range, rather only those intersected by a primitive, using a look-up based on a hashmap of the voxel coordinates. Details on the surface voxelization algorithm are given in Appendix C. We batch primitive-voxel intersections, defined by voxel coordinates u, primitive normal n 𝑝 , c 𝑝 (u), 𝑎 𝑝 (u), along with quantities interpolated between vertices such as texture coordinates or color, together and upload the values to OpenGL textures. A fragment shader runs on the batch and computes the displacement 𝜙, per Sections 7.2 or 7.3, and performs additional processing, e.g., surface color assignment. This is the only part of our implementation that uses a GPU.

We then write the results to a sparse raster. For each slice within the chunk, we use std::unordered_map to compute a map (𝑥, 𝑦) ↦ → Σ, where Σ denotes a surface voxel element comprising the attributes needed for a surface voxel

where attribs indicates other attributes that may be of interest, such as color. For each primitive 𝑝 that intersects a voxel, the map retrieves the corresponding Σ and updates 𝜕 𝜔 𝑛 𝑓 per (11).

## Displacement Mapping

Displacement maps are topographic textures that specify a height map relative to the tessellation geometry along the direction of the surface normal vector. In contrast to bump maps or normal maps used for shading, a displacement map alters the topography of the object, adding detail to the tessellation. Adding detail by refining the tessellation results in high polygon counts, increasing the storage, transmission and processing costs. A displacement map is typically a much more efficient representation for geometric detail. In this section, we describe our implementation of applying a displacement map to a low-poly mesh that is then printed with high surface detail.

Our surface representation stores displacement, along with other attributes such as RGBA values, with each surface voxel; a unique index per surface voxel allows access to these attributes. Using the method of Brunton et al. [2018], we transfer this index to the discrete Voronoi cell of each surface voxel.

So far we have described 𝜙 in infinite precision. In practice, displacement maps are often given in fixed precision formats, with as few as 8-bits per pixel being typical. We interpret such displacement maps as φ (t) ∈ [0, 1], t ∈ R 2 , and apply a per-object displacement scale 𝜅 to convert this value into a metric distance. Specifically,

where t(v) are the texture coordinates interpolated at v within a primitive, and 𝜅 > 0 means 𝜕S lies within a dilation by 𝜅 of 𝜕S. To account for this dilation, we add a padding of sufficient voxels along the x-, y-, and z-axes. To avoid aliasing when sampling φ, which is typically a high-frequency texture, we apply mipmapping.

## Curved Surfaces

We implement curved triangles by computing the distance along the normal of the flat triangle to the curved triangle during surface voxelization, and store this as the displacement value of the surface voxel created by the surface voxelization of the flat triangle. For PN triangles, we convert them to general Bézier triangles [Vlachos et al. 2001], and evaluate the position of the Bézier triangle using the de Casteljau algorithm [de Casteljau 1959].

Let u ∈ 𝜕S and n 𝑝 be the normal of a primitive 𝑝 intersecting the 𝑉 (u). We have

for v ∈ 𝑝, where q(v) is the point on the curved primitive constructed from v. Combining with (9) gives

n 𝑇 𝑝 (q(c 𝑝 (u))u).

(20)

# APPLICATIONS AND EVALUATION

In this section we apply our displaced SDFs to different tasks in additive manufacturing, and evaluate its performance. To evaluate the robustness and performance of our algorithm, we used a subset of 50 models from the Thingi10K [Zhou and Jacobson 2016] To evaluate displacement mapping, we used a different set of four texture-mapped models as described in Section 8.2. We created printed examples by pairing our framework with the implementation provided by the Cuttlefish SDK [IGD 2020] for color gamut mapping, separation, halftoning, and printer-specific output.

We printed examples on a Mimaki 3DUJ-553 [Mimaki 2017].

## Robust voxelization and fabrication

In this section, we evaluate the robustness of our approach to corrupted data. We show some visual results for real-world data in Figs. 1a, 9 and 10. Fig. 1a shows an open surface as a result of a scan, which our method is able to voxelize for printing. To obtain a near-constant thickness, we set a minimum level set value, -0.8 cm, and extract a surface at that iso-level in addition to the 0-level. Fig. 9 shows the result of printing a multi-view stereo reconstruction [Waechter et al. 2014] of a statue of Copernicus. Due to the many occluding surfaces, the scan has many holes, small and large with complex boundaries, and some floating triangles. The bottom of the model is completely open, since it is the ground surrounding the statue. Our approach preserves the detail of the textured surfaces and completes the model without introducing extraneous surface features. Fig. 10 shows a point cloud [Rodrigues et al. 2014] and the 3D printed result. The model includes colors and normals at each point. Again, the model is completely open on one side, and to print with a near-constant thickness, we use a second iso-level of -0.8 cm.    11 shows the Hausdorff distance for different numbers of holes, for an average hole radius of 0.02 (left), and for different hole sizes for a 100 holes. We see that the error increases gradually as the number of holes increase, but that the variance also increases. A similar behavior can be observed for increasing hole size. Additional results can be found in Appendix E. All lengths (radii, Hausdorff distance) are given as a fraction of the model's bounding box diagonal. 

## Displacement mapping

In this section, we compare the displacement mapping performance of our approach to that of vertex displacement, which was performed using Blender [2020]. A displacement map can be applied to a model in Blender using the Subdivision Surface and Displace modifiers to subdivide the surface and displace the vertices, respectively. We compare this method to ours in terms of geometric compactness, and processing efficiency. We also verify that with increasing subdivision, vertex displacement converges toward our displaced result. We use a test set of four models with displacement maps, shown in Fig. 14 and in Appendix D. Right: Setup time, including reading from disk, parsing, and placing the model in the printer's build space, with increasing surface subdivisions for different models. The 0-level subdivision refers to the original tessellation with a displacement map applied to using our method. Fig. 12 (left) shows the exponential increase in the number of triangles for increasing subdivision levels. Fig. S6 in Supplemental Appendix D shows the corresponding exponential increase in file size. In Fig. 12 (right), we compare the time required to load and parse the input mesh, and position it in the printer's build space for different subdivision levels, where level 0 indicates the original mesh with displacement map. For higher subdivision levels the time is dominated by file parsing. This is clearly dependent on the file format; we used the OBJ format, since it supports displacement maps, and is more widely supported by 3D printing software than other formats. Fig. 17a shows the processing time of our method for different levels of subdivisions. Again, 0 indicates the original mesh with displacement map. We see that the processing time for a fixed number of voxels does not change significantly (note the compressed range on the vertical axis). We choose this measure since the different subdivision levels result in different numbers of voxels to process (the object becomes bigger).

To compare the level of detail obtained using vertex displacement vs. our method, we look at the Hausdorff distance 𝑑 𝐻 between our method and the different levels of subdivision. Fig. 13a shows both 𝑑 𝐻 and the one-sided variant 𝑑 𝐻 * (𝐷,𝑇 ), measuring the distance of 𝐷 to 𝑇 , such that 𝑑 𝐻 (𝐷,𝑇 ) = max(𝑑 𝐻 * (𝐷,𝑇 ), 𝑑 𝐻 * (𝑇 , 𝐷)), where 𝐷 denotes the surface generated using the original tessellation with displacement map, and 𝑇 denotes the surface generated by subdivision. We can see that in general both decrease as the tessellated versions are refined. Self-intersections created by vertex displacement result in inside-out surfaces in some locations, which causes 𝑑 𝐻 to increase for higher subdivision levels. However, 𝑑 𝐻 * continues to decrease showing that with higher subdivision, the vertex displaced models approach the shape of applying displacement using our method.

(a) (b) Fig. 13. Hausdorff distance between a low poly mesh with displacement and high-poly meshes subdivided and displaced using the same displacement map in Blender (a), and root mean squared error of a unit sphere represented using displaced SDF generated from flat and curved triangles (b).

Fig. 14 gives a visual comparison between the two methods for the teapot model, as does Fig. S1 in Appendix D for the earth model. The left and middle prints use vertex displacement after 1 and 5 subdivisions, respectively. The prints on the right were displaced using our method with the same displacement map. Our method attains the quality of 5 subvisions with a smaller file size than 1 subdivision. Figs. 1 (center) and 15 (left) show the benefits of displacement mapping in terms of visual realism.

## Direct fabrication of curved surfaces

Fig. 16 shows a chess piece printed using flat and curved PN-triangles. The tessellation is no longer visible in the case of curved triangles. Fig. 1c shows how the same curved triangle tessellation scales to different print sizes while maintain precision to the native resolution of the device. No additional tessellation or subdivision is applied to the 5cm print (right) versus the 3cm print. Fig. 13b shows the 5.48 MB 1382.75 MB 4.25 MB Fig. 14. A printed 9-cm teapot with 1 surface subdivision (left), 5 surface subdivisions (center), and displacement map applied using our method (right). Under each image we give the file size used to encode the geometry, including the displacement map for our method. root mean squared error (RMSE) of a unit sphere represented using our displaced SDF generated from flat and curved (PN) triangles.

The RMSE is measure on vertices extracted on the 0-set of 𝑓 using marching cubes. The same number of curved triangles produces about two orders of magnitude lower error compare to flat triangles. 

## Performance

Our algorithm has asymptotic theoretical running time of 𝑂 (1) per voxel, or linear in the number of voxels. In this section, we show experimentally its independence w.r.t. the number of primitives |P |, its run-time in practice as the print size changes, and its low storage requirements, < 1 byte per voxel for moderate print sizes, decreasing for larger prints. We conducted all performance evaluations, including those for Section 8.2, on a laptop PC with an Intel i9 processor with 8 cores and 16 MB of cache, and 16 GB of memory.

To generate the data for Figs. 17b-d, we ran each of the 53 models from our test set at two print sizes chosen randomly from {3 cm, 5 cm, 10 cm, 15 cm, 20 cm}, where the print size is measured along the model's longest axis.

We see from Fig. 17a that the running time is independent of the number of primitives. Fig. 17b,c further shows that our implementation runs in constant time per voxel (linear in the number of voxels), and independent of the number of primitives. Each figure shows the running time, including surface voxelization, distance computation, sign estimation, evaluation of (6), surface voxel extraction and hidden surface removal. Over all 106 trials, the mean running time per million voxels was 0.0832 s.  storage per voxel is computed as

where 𝑡 is wall time during program execution, 𝐵 total (𝑡) is total storage in bytes allocated for our implementation at time 𝑡, and 𝑊 , 𝐻 and 𝐷 are the number of voxels along the 𝑥-, 𝑦-and 𝑧-axes, respectively. The total storage 𝐵 total (𝑡) is the sum at time 𝑡 of storage allocated for • temporary storage for surface voxelization (including overhead for hash maps), • sparse surface voxel storage (including overhead and, e.g., RGBA values not specific to our approach), and • dense voxel storage for a chunk of slices.

We compute 𝐵 total (𝑡) at the end of processing of each 𝐶 slices in both the surface voxelization process and the computation of 𝑓 . This account misses some small 1D temporary stores 𝑂 (max{𝑊 , 𝐻 }), which has a minimal effect on 𝐵 voxel .

# LIMITATIONS

Our approach assumes an oriented surface as input, and does not model errors or noise in normals (triangle vertex order). When such problems occur on a small scale, our approach handles them with only small artifacts, but will fail when large portions of a surface are flipped, or there is significant noise in point normals. Appendix F shows examples of the limits of our regularization scheme, w.r.t. flipped triangles and large holes. in arbitrary sign on each side, with the result that 𝑓 (left) has a arbitrary error vs. 𝑓 (right). We observed that for walls as thin as 10 -7 𝛿 the sign is correctly assigned, whereas for a wall of thickness 10 -8 𝛿 sign errors occur. Walls of 0 thickness are possible in artist-created models, so this is something to address in future work. Appendix A provides more analysis. Note that this discussion considers computing sign via (13) with no regularization.

The floodfill post-process for self-overlapping surfaces means internal voids are not possible. This is a relatively minor problem in the context of additive manufacturing. For processes that allow for internal voids, such as FFF/FDM, voxel-compatible techniques exist [Tricard et al. 2020] to generate internal support structures. For polyjet processes used in graphical 3D printing, internal voids are anyways filled with support material, and voxel-based hollowing or lattice generation to save build material is likely advantageous.

While our approach avoids the pitfall of self-intersecting surfaces that can arise with vertex displacement, it does not validate that the combination of macroscopic and mesoscopic geometry constitute a physically realizable shape. A large negative displace on a thin wall can cause the wall to locally disappear, and a positive displacement in a crevice can fill it in. Providing checks and feedback for such invalid input is an avenue for future work.

Using a single displacement value per surface voxel creates a problem for curved triangles when the corresponding flat triangles induce large dihedral angles across the edges between them. This results in a small bump along the edge.

# CONCLUSION

We have presented an efficient framework based on displaced signed distance fields for robust fabrication of finely detail and curved surfaces from compact representations. Our framework allows the augmentation of low-polygon tessellations with displacement maps for meso-scopic surface detail, and the direct fabrication of curved triangle surfaces. In both cases it does this without subdivision and the ensuing risk of creating self-intersecting surfaces. Our algorithms run constant time per voxel. We have verified the robustness, quality and performance qualitatively and quantitatively.

Looking forward, it would be interesting to combine our displaced SDF with neural implicit representations such as Davies et al. [2021]. Currently, displacement maps will scale with the object as it is scale, since the texture parametrization is fixed. Allowing the displacement signal to have a fixed scale would allow the mesoscopic information to maintain its frequency as the object changes in size. Including support for other types of curved triangles, e.g. Lagrange simplices, would simplify interfacing 3D printing with FEM analysis.

# ACKNOWLEDGMENTS

We thank Philipp Urban, Marco Dennstädt, Johann Reinhard and Mostafa Morsy for helpful discussions; Marketiger BV for printing; and the anonymous reviewers for insightful feedback. Lubna Abu Rmaileh was funded by EU Horizon 2020 ITN project ApPEARS no. 814158. Further information on the models and textures used in this paper can be found in the supplemental material.

