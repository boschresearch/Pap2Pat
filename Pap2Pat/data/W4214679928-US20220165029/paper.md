# High idelity

Figure 1: Our novel implicit shape representation can model complex surfaces with high-fidelity. Row 1: Recovering visually pleasing surfaces in comparison to prior state-of-the-art SAL [2] and NDF [8]. Row 2: Results on a representative open shape, where we correctly model the shape, as opposed to SAL [2], which closes up regions that are meant to be open.

# Introduction

High fidelity representation and rendering of potentially open 3D surfaces with complex topology from raw sensor data (images, point clouds) finds application in vision, graphics and animation industry [20]. Therefore, in recent years deep learning based methods for 3D reconstruction of objects have garnered significant interest [38,34,31].

Explicit 3D shape representations such as point clouds, voxels, triangles or quad meshes pose challenges in reconstructing surfaces with arbitrary topology [33]. Moreover, the ability to capture details of such representations are limited by predefined structure (like number of vertices for meshes) or memory and computational footprint (for voxels and point clouds). Several implicit shape representations using deep neural networks have been proposed [34,31,14,6,2,8] to alleviate these shortcomings.

Recent approaches use a distance function as the implicit representation. For example, DeepSDF [34] use a Signed Distance Function (SDF) as the implicit representation where the sign represents the inside/ outside of the surface being modeled. Not only does this limit DeepSDF to modeling closed surfaces, the ground truth needs to be watertight (closed) as well. Since most 3D shape datasets [5] have non-watertight (open) shapes, preprocessing is needed to artificially close such shapes and make them watertight [31] -a process which is known to result in a loss of fidelity [22]. To overcome this problem, methods such as SAL [2] seek to learn surface representations directly from raw unoriented point clouds. However, such methods also make an assumption that the underlying surface represented by the point cloud is closed, leading to learnt representations necessarily describing closed shapes [3].

NDF [8] overcomes this limitation by using an unsigned distance function (UDF) based implicit representation and achieves state-of-the-art performance on 3D shape representation learnt directly from the unprocessed ShapeNet dataset. However, UDFs have a fundamental limitation. Since the gradient of the UDF vanishes on the surface, direct estimation of local, differential geometric properties like the tangent plane and the surface normal becomes noisy and loses fidelity. This results in a loss of performance on downstream tasks like rendering and surface reconstruction [24] as well as those like registration [36] and segmentation [18] where normal estimates play a vital role.

An additional issue is that for the above methods, the estimation of differential geometric properties needs a backward pass leading to increased memory footprint and time complexity which becomes a challenge for applications which require fast rendering on devices with limited memory (e.g. tiled rendering on hand-held devices [12]), or for robotics tasks such as real-time path planning where fast normal estimates in 3D space play an essential role [15,32].

To address these challenges, we introduce a novel implicit shape representation called the Closest Surface-Point (CSP) function, which for a given query point returns the closest point on the surface. We demonstrate that CSP can model open and closed shapes of arbitrary topology, and in contrast to NDF, allows for the easy computation of differential geometry properties like the tangent plane and the surface normal. Moreover, as opposed to existing implicit representations and demonstrated later, it can efficiently recover normal information with a forward pass. A comparative summary of the properties discussed above for CSP and the most related art is presented in Table 1. We also present a panel of illustrative results in Fig. 1 which clearly demonstrates the higher fidelity with which complex surfaces are represented by CSP when compared with SAL and NDF.

Finally, we show that due to the above benefits, CSP is not only a potential method of choice for learning high fi-  delity 3D representations of complex topologies (open as well as closed) from the raw data, but also for many downstream applications. For this, we present (a) a fast and memory efficient rendering algorithm using an adaptation of sphere-tracing for CSPs that leverages the accurate surface normal estimates that CSP provides, and, (b) since it's often required to extract an explicit surface representation [1], we present a coarse to fine meshing algorithm for CSPs, that can recover high-fidelity meshes faster than prior methods [8]. To summarize, our contributions are: 

# Related Work

Explicit Shape Representations. Explicit approaches primarily use voxels, meshes or point clouds for representing 3D shapes. Voxels provide a direct extension of pixels to 3D, allowing easier extension of image processing methods for 3D shape analysis. Several initial shape representation works are built upon this idea [30,9,40]. Drawbacks of using voxel representations are limited output resolution, and higher computational and memory requirements. Mesh representations address some of these issues [19,43,17  cates inside or outside. Hybrid explicit/implicit representations are proposed [6,14], where the implicit function is a union of inside/outside classifier hyper-planes. BSP-Net [6] uses a binary space partitioning network to model a convex decomposition of the 3D shape, the union of which defines a watertight separation of the inside/outside of the shape. CvxNet [14], also proposes a convex decomposition using hyper-planes but with a double representation of a complex primitive.

The methods described above [6,14,34,31,34] can only represent closed surfaces, with an additional requirement that the training data also comprises of closed watertight shapes, which often results in non-trivial loss of fine details [22]. SAL [2] provides a partial solution to this problem by proposing an unsigned similarity function to learn from ground truth unprocessed triangle soups, but eventually infers a shape representation which can only model closed shapes. NDF [8] overcomes this limitation by using a UDF to represent both open and closed shapes, but cannot easily provide high fidelity estimates of differential geometry (surface normal, tangent plane) due to the vanishing gradient of the UDF on the surface.

In contrast, CSPs can model arbitrary topologies (both open and closed) while also allowing for simple, efficient and high-fidelity computation of differential surface geometry as opposed to the prior art [8,2,6,31,34,14].

# Approach

In this section we present the proposed shape representation, and how it can be used for downstream applications. A schematic of the system architecture is presented in Fig. 2. We start below with first defining the proposed implicit shape representation (Sec. 3.1) and deep neural network model for the same (Sec. 3.1.1). Then, we present approaches to estimate the local geometric properties of the surface, e.g. the tangent plane and the surface normal (Sec. 3.2) and finally propose algorithms for using CSP for downstream applications like rendering (Sec. 3.3.1) and meshing (Sec. 3.3.2). (1

## Shape Representation

where p is the closest point on the surface S to the query point p. Given the closest surface-point, UDF can be trivially calculated as:

### CSPNet: A Deep Neural CSP Model

We model CSP using a deep neural network which we demonstrate to be robust to training with noisy data generated from a noisy triangle soup. We illustrate the complete architecture in Fig. 2. There are two main components of the proposed CSPNet.

Volume Encoder. For any input 3D shape, the volume encoder ψ produces a feature volume which is isotopic1 to the volume enclosing the input shape. Each feature voxel encodes properties of the surface from the vantage point of the voxel. For the implementation in this paper, we follow the architecture of Convolutional Occupancy Networks [35] for the volume encoder ψ. The encoder takes as input the entire point cloud for the input shape and produces a volumetric feature encoding. More specifically, PointNet [38] is used to encode point features. To get volumetric features, a voxel grid is constructed and voxel features are computed by (average) pooling features for the points that correspond to the voxel under consideration. This is followed by a 3D U-Net which produces the final encoding of the feature volume, resulting in a feature of dimension F for each voxel.

Shape Decoder. The feature corresponding to the input query point p is sampled from the 3D feature volume using trilinear interpolation, and passed into the shape decoder φ along with query point p. The shape decoder φ uses the features encoding the shape to predict the surface point closest to p. Here on, we will use f θ and g θ to denote the DNN approximations to the CSP and the UDF functions respectively, where θ denotes the union of parameters of both encoder and decoder. Note that the output of CSPNet, f θ , directly provides an estimate for CSP while the estimate for the UDF, g θ , is obtained as p -f θ (p) 2 using (2).

## Differential Surface Geometry

For any query point p, CSPNet directly provides us with an estimate of both the closest point on the surface f θ (p) as well as the unsigned distance to it, g θ (p). However, in addition, a variety of downstream applications in vision [24,36], robotics [15,32], graphics [12], and animation [42] need estimates of local differential properties of the surface like the tangent plane and normal at any surface point. We show below how we can easily estimate these properties.

### Using the Jacobian

Let p be any query point and p ∈ S be its closest point on the surface S. Further, let J f θ ( p) denote the Jacobian of f θ at p. Let δ be the unsigned distance from p to p and d be the surface normal at p. Then, we get the following approximation using the first-order Taylor series expansion:

The last equation shows that (to a first order approximation of the surface), the surface normal d lies in the null space of the Jacobian J f θ ( p) while the span of the Jacobian provides the tangent space of the surface. This is illustrated in the Fig. 2b and is intuitively clear since along the direction perpendicular to the surface, the CSP function does not change, giving the same closest surface point. The tangent space and the normal to the surface both can be estimated using singular value decomposition (SVD). However, computation of Jacobian requires a backward pass through CSPNet. Prior works which differentiate the distance function on the zero level-set (i.e the surface) [34] also need a backward pass. Even so, since the derivative of UDFs vanish at the surface, NDF estimates the normals close to the surface [8] leading to some loss in fidelity.

### Forward Mode Normal Estimation

In certain applications like rendering, sphere tracing is used to obtain a point on the surface and it is needed to quickly and efficiently estimate the normal at the point of intersection [12]. We can use the Jacobian approach presented in the previous section but it requires a backward pass.

An alternate approach for obtaining a fast approximation for the surface normal, using a forward pass from a query point p close to but not on the surface is by using the Normal Vector Field (NVF) defined as follows:

We represent the corresponding estimate for NVF by h θ as (p -f θ (p))/g θ (p). We refer to this method of estimating normals as forward-mode normal estimation. Since there is no backward pass involved, it is faster than the previous methods. We demonstrate the utility of this approach in Sec. 4.2 and validate its performance both in terms of accuracy and speed via extensive experimental evaluation. More generally, fast estimation of the NVF at off-surface locations is vital to robotics applications such as path planning in distance fields [15,32].

## Rendering and Meshing

In this section, we describe techniques for rendering surfaces and extracting topologically consistent meshes from the the learnt representation. Note that this process is important for many downstream vision applications such as shape analysis [26] and graphics applications such as rendering novel scenes under changed illumination, texture or camera viewpoints [37].

### Sphere Tracing CSP

Sphere tracing [21] is a standard technique to render images from a distance field that represents the shape. To create an image, rays are cast from the focal point of the camera, and their intersection with the scene is computed using sphere tracing. Roughly speaking, irradiance/radiance computations are performed at the point of intersection to obtain the color of the pixel for that ray.

The sphere tracing process can be described as follows: given a ray, r, originating at point, p 0 , iterative marching along the ray is performed to obtain its intersection with the surface. In the first iteration, this translates to taking a step along the ray with a step size of UDF(p 0 ) to obtain the next point p 1 = p 0 + r • g θ (p 0 ). Since g θ (p 0 ) is the smallest distance to the surface, the line segment [p 0 , p 1 ] of the ray is guaranteed not to intersect the surface (p 1 can touch but not transcend the surface). The above step is iterated i times till p i is close to the surface. The i-th iteration is given by p i = p i-1 +g θ (p i-1 ) and the stopping criteria g θ (p i ) ≤ .

Note that the above procedure can be used to get close to the surface but does not obtain a point on the surface. Once we are close enough to the surface, we can use a local planarity assumption (without loss of generality) to obtain the intersection estimate. This is illustrated in Figure 3 and is obtained in the following manner: if we stop the sphere tracing of the CSP at a point p i , we evaluate the NVF at that point as n = h θ (p i ), and compute the cosine of the angle between the NVF and the ray direction. The estimate is then obtained as p proj = p i + r • g θ (pi) r T n .

### From CSP to Meshes

Sphere tracing CSP, described in the previous section, can only be used to render a view of the shape. Thus, the extracted surface is immutable and cannot be used for applications such as 3D shape modeling, analysis and modification [26]. Explicit 3D mesh representations are more amenable for such applications. In this section, we propose an approach to extract a 3D mesh out of the learnt CSP.

A straightforward way to extract a mesh from an implicit representation is to create a high-resolution 3D distance grid and using the marching cubes algorithm [28] on this grid. However, as discussed in [31] this process is computationally expensive at high-resolutions, as we need to densely evaluate the grid. In [31] a method for multi-resolution surface extraction technique is proposed by hierarchically creating a binary occupancy grid by conducting inside/outside tests for a binary classifier based implicit representation.

However, CSPs cannot perform inside/outside tests. Hence we propose a novel technique to hierarchically divide the distance grid using edge lengths of the voxel grid cubes. We illustrate the procedure in Fig. 4. Starting with a voxel grid at some initial resolution, we obtain a high resolution distance grid and perform marching cubes on the grid using a small positive threshold to get the final mesh. A voxel is chosen for subdivision if any of its eight corners have the predicted UDF value g θ (x) < h i , where h i is the Step 3), and are pruned out by using a small positive threshold while meshing the distance-grid in the Marching cubes (MC) step. edge length of the voxel grid at the i th level. The voxels that are not chosen for subdivision are simply discarded in the next level. Using this procedure, we quickly obtain a high-resolution distance grid, which is converted to a mesh using marching cubes. Note that, our algorithm selects a few false positive voxels in the final resolution, but these are effectively pruned out in the final mesh by using a small positive threshold in the marching cubes [28] step.

# Experiments

In this section, we validate the different parts of our proposed system outlined in Fig. 2 against a selection of prior art. First we demonstrate the superiority of the proposed implicit shape representation (CSP: Sec. 3.1) on the task of surface reconstruction from point clouds. Next, we validate the proposed methods for extracting local surface properties such as surface normals (described in Sec. 3.2). Finally, we test the novel sphere-tracing algorithm for CSPs and the coarse to fine meshing algorithm (described in Sec. 3.3).

Baselines. Most existing methods such as Occupancy Networks [31], DeepSDF [34], Point-Set Generation Networks [16], Deep Marching Cubes [27] and IF-Net [7] only work on watertight (i.e. closed) shapes. We compare against these methods to verify that our method retains performance on closed shapes, in addition to being able to model open shapes. On the other hand, for comparing per-formance on raw/unprocessed shapes, we choose SAL [2] and NDF [8]. While these methods can work with nonwatertight (i.e. unprocessed) ground truth, they still require a backward pass to estimate surface normals, which leads to an added computational and memory footprint. Additionally, while NDF can reconstruct both open as well as closed shapes, it is unable to guarantee plane reproduction and accurate normal estimates on the surface of the shape. In the following sections, we show empirically that our method addresses these challenges.

## Shape Representation

In this section, we demonstrate the representational power of our model on ShapeNet dataset [5]. We consider the task of surface reconstruction from point clouds, and first evaluate on closed shapes to verify that our proposed generic shape representation yields comparable performance to state-of-the art methods which are solely meant to work on watertight shapes [34,31,16]. Second, we evaluate our method against NDF and SAL on raw, unprocessed shapes. Before describing the results, we present the evaluation metrics that we consider.

### Evaluation metrics

A common practice for evaluating 3D reconstruction pipelines is the chamfer distance metric [34, 2, 8]. However, as discussed in some prior work [44], this metric does not reflect the perceptual quality of the rendered image. Moreover, for applications such as relighting [29] it is desirable to obtain surface normal maps by directly rendering the iso-surface using sphere-tracing, as opposed to extracting a mesh. Clearly, there is a need to evaluate implicit shape representations on the perceptual quality of their iso-surfaces rendered via sphere-tracing. Therefore, in addition to the chamfer distance we propose new metrics (outlined below) which are designed to reliably capture these properties.

# Depth Error (DE).

First we evaluate the mean absolute error (MAE) between the ground truth and the estimated depth map obtained by sphere-tracing the learnt representation. This error is evaluated only on the "valid" pixels, which we define as the pixels having non-infinite depth (foreground) in both the ground truth and estimated depth map. This metric captures the accuracy of ray-surface intersection.

Normal Cosine Similarity (NCS). We also evaluate the cosine similarity between the sphere-traced normal map and the ground truth normal map for the valid pixels. Since the surface normals play a vital role in rendering, this metric is informative of the fidelity of the rendered surface.

Pixel-Space IOU. Finally, since both Depth Error and NCS are evaluated only on the valid pixels, they do not quantify whether the geometry of the final shape is correct. Therefore, we also evaluate Pixel-Space IOU,

Here the invalid pixels are those which have non-infinite depth (foreground) in either the ground truth depth map or the estimated depth map but not both. Note that for the proposed metrics, we render the shape from 6 views (uniformly sampled on sphere) to capture all the regions of the surface.

## Data creation

We normalize each mesh in the ShapeNet dataset to [-0.5, 0.5]. For each shape, we densely sample a set of 0.25M points, denoted by the set V, to represent the set of surface points. The training points P are obtained for each shape by uniformly sampling 0.025M points as well as perturbing the set V with a gaussian noise of 2.5e-4 and 2.5e-3. Finally, the ground truth for each of these training points p ∈ P is computed by finding the nearest surface point p ∈ V to construct the training pair (p, p).

### Training

Note that, we only train f θ , and g θ and h θ can be derived from it in the same way UDF and NVF can be derived from CSP in eq. 2 and eq. 4 respectively. Given f θ (p|X) = φ(ψ(X), p), as the training objective, we simply use the squared L 2 loss between the estimated closest surface-point f θ (p|X) and the ground-truth p(= CSP(p|X))

### Evaluation on closed shapes

We convert all the ShapeNet 3D models to closed shapes by following the steps in [39]. Following this, we run our data creation process (outlined in Sec. 4. 

### Evaluation on unprocessed shapes

In addition to closed shapes, CSP can also represent shapes of arbitrary topology. Therefore, we also train on unprocessed ShapeNet 3D models and evaluate performance using the metrics defined in Sec. 4.1.1. We compare against SAL and NDF, which are methods that can learn representations from raw/unprocessed ground truth. 1 This comparison is reported in Table 3. We find that CSP marginally outperforms NDF on chamfer, depth and IOU metrics, but yields a significant improvement on the surface normals metric owing to the useful plane reproduction property of CSP. Additionally, SAL clearly suffers on all metrics, given that it learns a signed distance function (closed shape) even for surfaces that are open. This behavior can also be confirmed in the qualitative results shown in row 2 of Fig.  

## Local Surface Properties

In Sec. 3.2, we described various strategies to estimate surface normals using the learnt implicit representation. We refer to the strategy using the Jacobian as CSP (jac.) and the one using the forward pass (eqn. 4) as CSP (fwd.).

Similar to NDF, this latter approach approximates surface normals using off-surface points close to the surface (where p ≈ p) by stepping back along the ray at its point of intersection with the surface. More concretely, given a ray r which intersects with the surface at p int (at the 1 Since both SAL and NDF do not provision a release of pretrained class-agnostic models, we retrain them using code provided by authors. end of sphere-tracing), the normal is computed by stepping back along the ray by some scalar value α. Thus, npint = ∇ pint g θ (p int -α • r). Note here that α is a hyperparameter which is sensitive to the curvature of the surface, and NDF chooses a constant α = 0.005. However, we observe that choosing a single α for all shapes is suboptimal given that surfaces can have varying curvatures.

To investigate the sensitivity of the system to varying α, we plot normal cosine similarity vs different values of α in Table 4. It can be clearly seen that CSP (jac.) has higher quality normal estimates for points on the surface (i.e. α = 0), given its tangent plane reproduction property, as opposed to NDF and CSP (fwd.) which do not. It is interesting to note that although SAL learns a signed distance function that is differentiable on the surface of the shape, it still performs poorly on this metric, owing to the instability of their unsigned similarity loss, and poor geometric reconstruction on open shapes. However, we find that both NDF and CSP (fwd.) yield comparable performance to CSP (jac.) if allowed to step back along the ray (α = 0.005). However, the normal cosine similarity is lower than CSP (jac.) at α = 0, which is a definite drawback. Moreover, we find that α = 0.005, CSP (fwd.) yields similar performance compared to NDF, even though it does not use a backward pass. We report rendering speeds and memory footprint for CSP (fwd.) and NDF in Table 5, and we immediately find that CSP is superior on both fronts.

Additionally, in Table 4 we find that although α = 0.005 yields reasonably good normals, the standard deviation is higher than those obtained by the tangent plane approximation. This clearly shows that choosing a single threshold for all shapes [8] is sub-optimal. Finally, we qualitatively compare various normal estimation strategies in Fig. 6. We find here too that CSP (fwd.) performs reasonably well for α = 0.005, with CSP (jac.) yielding the best performance at α = 0. Both visually and quantitatively, we find that our normal estimation strategies outperform NDF. Additionally, forward-mode surface estimates, Ours (fwd.) are faster than that of NDF while Ours (jac.) is comparable in speed (more analysis in supplementary).

# Method

Normal Map Similarity

0.84 ± 0.017 0.851 ± 0.014 0.871 ± 0.009 0.861 ± 0.01 NDF [8] 0.863 ± 0.01 0.882 ± 0.008 0.903 ± 0.006 0.891 ± 0.008 CSP (fwd.) 0.620 ± 0.12 0.873 ± 0.018 0.912 ± 0.006 0.91 ± 0.007 CSP (jac.) 0.913 ± 0.003 0.915 ± 0.003 0.920 ± 0.003 0.871 ± 0.01 Table 4: Normal estimation accuracy of various methods described in Sec. 3.2. Here α refers to the step-back distance along the ray. Comparison of our meshing algorithm with that of NDF. Note that NDF displays visible artifacts, whereas our strategy reconstructs a topologically consistent mesh.

## Rendering and Meshing

In this section, we validate our sphere-tracing strategy and meshing algorithm (Sec. 3.3) against various baselines.

Sphere Tracing CSP. We compare the sphere tracing strategy described in Sec. 3.3.1 to a baseline strategy when the projection step is excluded from the algorithm. Our proposed strategy yields better depth maps (MAE = 0.014) than the Vanilla Sphere tracing (MAE = 0.016) owing to more accurate ray-scene intersection. As expected, the qualitative results (depth error maps) shown in Fig. 5 also indicate the benefit of using projection step as a part of sphere tracing CSP. Refer supplementary material for more visualizations. Speed & memory footprint of rendering. In Table 5, we report the average time taken to render a 512×512 image using a memory budget of 8GiB. Since we do not rely on backward passes through the network (see definition of NVF in Sec. 3.2.2) higher batch sizes can be used on a fixed GPU budget, which leads to 20× faster rendering. In this manner, CSP provides a viable solution for applications which require real time, fast estimation of surface normals on small GPUs with limited memory [15,15,12]. Refer to supplementary material for more details on the specifics of the experimental setup. Meshing CSP. Our novel course-to-fine meshing algorithm allows for fast conversion of CSP to mesh, providing a viable and fast alternative to that proposed in NDF [8]. For the representative example shown in Fig. 5   takes 4.48s to generate the dense point cloud and an additional 104s for meshing using BPA [4]2 . On the other hand, our method takes a total of 2.50s for generating the final mesh. It is also important to note that although we use only 636k function evaluations, a higher quality mesh is recovered in comparison to NDF which uses 12M function evaluations. In Fig. 5 we show qualitative comparisons to NDF's meshing algorithm for UDFs. Note also that NDF's meshes display visible artifacts, given that it recovers the mesh after performing BPA on a dense point cloud (1M pts.) generated from the learnt representation. In contrast, our coarse-tofine meshing strategy enables the application of Marching Cubes, and reconstructs a topologically consistent and visually pleasing mesh. Refer supplementary for details on the hyperparameters used.

# Conclusion

In this work, we proposed a new class of implicit representations called CSP that can model complex 3D objects (both open and closed surfaces), with a fidelity surpassing the state of the art. We demonstrated that CSP also facilitates accurate and efficient computation of local geometric properties of the surface like the tangent plane and the surface normal which enables efficient algorithms for downstream applications like surface rendering and meshing -we presented novel algorithms for both. We further showed that CSP yields state-of-the-art performance on the unprocessed ShapeNet dataset, surpassing prior art such as SAL [2] and NDF [8]. In summary, this work provides a strong alternative to existing methods for 3D modeling and representation by addressing fundamental problems in representing complex shapes. In the future, we expect to extend this work to infer surface representations -both geometric and photometric -from single and multi-view 2D images.

# Acknowledgements

This research was supported in part by NSF award No. IIS-1925281.

# Lion

Figure 8: Single Shape reconstructions: Renderings from single shape architecture described in Sec. A. Here, we evaluate CSP independently on two shapes with complex structures. We show lighted normals (row 1 of each shape) as well as the raw normal map (row 2 of each shape) using both normal estimation methods (see Sec. 3.2 in main paper) and compare against the ground truth for the same. The CSP (jac.) results in higher quality normals compared to CSP (fwd.), which are reasonably comparable, but provide us with faster estimates (Highlighted in Red). More examples on next page.

We logged the time taken to estimate the Jacobian matrix for the experiments described in Sec. 4.3 of the main paper for CSP (jac.) and find that it takes on an average 0.08s for a 512×512 image. In comparison, NDF is faster and takes 0.063s. This is to be expected as NDF just needs 1 forward and 1 backward pass. However, given that the computational graph needs to be obtained only once, we only incur an additional 25% overhead (0.017s). Therefore, this is a reasonable trade-off for extracting high-fidelity surface normals.

On the other hand, we also proposed an extremely fast method, CSP (fwd.), which computes surface normals in a forwardmode taking only 0.003s for a 512×512 image and is of a quality surpassing that of NDF (See Table 4 of main paper).

# D. Meshing and Rendering: Experimental setup

Results for setup used for rendering and meshing are presented in Section 4.3 of the main paper. Here we provide details of the experimental setup. Figure 9: Single Shape reconstructions: Here, we show some results on a bathtub which has a high level of detail, with complex sub-structures, and a seifert surface which has complex topology (knots and holes).

Rendering. For a given input point cloud, we first compute the 3D feature volume from the encoder. We then render the learnt CSP representation (modeled using the decoder) from 3 different views. For doing so, we create a batch of rays from each viewpoint (3 views give us a total of 512×512×3=0.79M rays), and begin the sphere-tracing process (batched/parallel) for these set of rays. At the termination of sphere-tracing, we compute the surface normals for each ray (using gradients in case of NDF, and NVF in case of CSP). Since NVF does not require a backward pass, it can accommodate a batch of 0.5M rays on a 8GiB GPU. The corresponding batch size for NDF is much lower at 0.15M since it requires the computation of gradients. As reported in Table 5 of the main paper, the increased batch size leads to a significant improvement in the rendering speed (i.e. time taken to compute the surface normals).

Meshing. We present here additional details for meshing CSPs using the novel coarse-to-fine meshing strategy outlined in Sec. 3.3.2 of the main paper. We compute a 3D distance grid (of resolution = 256) using the proposed hierarchical space subdivision strategy, and perform meshing using Marching Cubes (using libmcubes [39]) with a small positive threshold of 0.006. For NDF, we use the code provided by authors to generate a dense point cloud (of 1M points) and mesh it using the ball-pivoting [4] tool in meshlab [10], using a ball-radius of 0.01.

In our experiments, we have found the ball-pivoting process to be very sensitive to this threshold, and in many cases it had to be tuned per-shape. On the other hand, our method uses a single threshold for all shapes, and generates high-fidelity meshes. Moreover, as reported in Sec. 4.3 of the main paper, our coarse-to-fine meshing strategy is significantly faster than that of NDF.

# E. Additional qualitative results

To supplement the qualitative results on the various sphere-tracing strategies (Fig. 5 of main paper), in Fig. 10, 11, we show additional results which compare depth maps generated using our novel sphere-tracing algorithm for CSP, against a vanilla sphere-tracing technique for unsigned distance functions. Further, in Fig. 12, 13, 14, 15, 16 we show additional examples of shape reconstruction which bolster the results shown in Fig. 1 of the main paper, and demonstrate the capability of our class-agnostic model to reconstruct shapes from any class of ShapeNet. All results are shown on a test-set of shapes (ShapeNet test-set used in [16]) not seen in training. Additionally, to reiterate the utility of meshes generated by our novel meshing algorithm for CSPs (Sec. 3.3.2 of main paper), we also show some representative meshes (compared against GT meshes) generated in Fig. 17.

# F. Off The Shelf Tools and Packages Used

In this work, we make use of a variety of off-the-shelf packages to run our experiments. For generating data, we use faiss [23], which is a library for performing fast nearest neighbour search on GPU. We compute GT normal and depth maps using the trimesh [13] with pyembree bindings viz. trimesh.ray.ray_pyembree.RayMeshIntersector. torch-scatter3 is used for trilinear interpolation of the 3D Feature Volume (See Fig. 2 of the main paper). For spheretracing CSP, we provision a custom implementation in PyTorch, which renders multiple images efficiently by batching rays across different views.   ) and CSP (fwd.) (α = 0.005) side-by-side, with the first row of each shape depicting a rendering of the sphere-traced surface normal map (shown in the second row) with directional light. We find that both methods (see Sec. 3.2 for a description of these methods, and Sec. 4.2 for some initial results reported in main paper) yield high-quality surface normals (with CSP (fwd.)) providing efficient forward-mode normal estimates. Note also that CSP (jac.) is marginally better in some regions (Highlighted in red.).   We also show the Ground Truth mesh on the right of each subfigure. Note that our algorithm generates structurally consistent meshes, which render visually pleasing images in Blender [11].

# Supplementary Material

In the paper, we presented results from the shape-agnostic CSP network (a single function for all shapes) which for a given encoded shape provided at the input, produced the closest surface point for the queried input point. Here, we first supplement those results with a single-shape CSP network. This is presented in (Sec. A) below.

Subsequent sections present additional details for the experimental evaluation in the main paper as follows:

• A. Single-shape CSP While the primary focus of this work was to build a single, shape-agnostic CSP model, we present here a model for a single-shape CSP implemented as follows: For any input point (or query point) in the 3D space, p, a 10-layer MLP estimates the closest point on the surface, p. Let fci denote a fully-connected layer with i output dimensions. Then the MLP is given by fc120, fc512, fc1024, fc2048, fc2048, fc1024, fc512, fc256, fc128, fc3

where the input dimension of fci is determined by the output dimension of the layer prior to it and every fc layer is followed by ReLU non-linearity, except the final layer. The architecture of the single-shape CSP is presented in Fig. 7. We present qualitative results for single shape reconstruction for a few complex shapes in Figures 8 and9, illustrating the ability of CSP to model complex shapes with high fidelity having either an open or a closed topology. It can be clearly seen that CSP is able to preserve surface details and accurately represent the surface orientations. In Figures 8 and9, we present results on complex shapes like (a) a dried rose, and, (b) a lion statute having an intricate design and regions of varying curvature (c) a bathtub, that has high levels of detail and complex sub-structures, (d) the seifert surface [41], that has complex topology (multiple holes and knots), .

# B. Training and architecture details

This section shares the network architecture modeling the shape representation in Section 4.1 of the main paper and details for training it.

We use the 3D volumetric encoder architecture proposed in [35] with a feature volume of resolution 64. Since our point estimation task is arguably more complex than binary occupancy prediction, we use a larger decoder, with 512 hidden units (with the same architecture as in [35]).

We train with a batch size of 32 on different shapes, with an input point cloud of size 3000 (we follow the setup in NDF [8]). For each shape in the batch, we use 10K points sampled from the training points, P (See Sec. 4.1.2 of the main paper). We train on an NVIDIA GeForce RTX 2080Ti GPU using an ADAM [25] optimizer and a learning rate of 1e-4. It takes ≈ 5 days to train on the full ShapeNet dataset.

# C. Jacobian Computation: Implementation Details

We now share the implementation details for the Jacobian computation as described in Sec. 3.2.1 of the main paper and discuss implications on its computational performance.

The Jacobian is computed using 1 forward pass and 3 backward passes (one for each row of the Jacobian) through the same network. For this, we use the autograd package in PyTorch and set retain_graph=True when computing the first row of the Jacobian. This caches the activations in the graph and makes them readily available for computing the subsequent rows, speeding up the computation of the Jacobian. 

