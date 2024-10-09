# INTRODUCTIONS

Recently, the integration of deep learning and computer graphics has achieved significant advances in lots of computer vision tasks, e.g., pose estimation Wang et al. (2020a), 3D reconstruction Zhang et al. ( 2021), and texture estimation Bhattad et al. (2021). Although the rendering quality of has significant improved over decades of development of computer graphics, the differentiability of the rendering process still remains to be explored and improved. Specifically, differentiable renderers compute the gradients w.r.t. the image formation process, and hence enable to broadcast cues from 2D images towards the parameters of computer graphics models, such as the camera parameters, and object geometries and textures. Such an ability is also essential when combining graphics models with deep neural networks. In this work, we focus on developing a differentiable renderer using explicit object representations, i.e.Gaussian reconstruction kernels, which can be either used separately for image generation or for serving as 3D aware neural network layers.

The traditional rendering process typically involves a naive rasterization Kato et al. (2018), which projects geometric primitives onto the image plane and only captures the nearest primitive for each pixel. However, this process eliminates the cues from the occluded primitives and blocks gradients toward them. Also the rasterization process introduces a limitation for differentiable rendering, that rasterization assumes primitives do not overlap with each other and are ordered front to back along the viewing direction Zwicker et al. (2001). Such assumption raise a paradox that during gradient based optimization, the primitives are necessary to overlap with each other when they change the order along viewing direction. Liu et al. (2019) provide a naive solution that tracks a set of nearest primitives for each image pixel, and blending them based on the viewing distance. However, such

# VOLUME RENDERER FOR GAUSSIAN ELLIPSOIDS

In this section, we describe VoGE rendering pipeline that renders 3D Gaussians Ellipsoids into images under a certain camera configuration. Section 3.1 introduces the volume rendering. Section 3.2 describes the kernel reconstruction of the 3D volume using Gaussian ellipsoids. In Section 3.3, we propose the rendering pipeline for Gaussian ellipsoids via an approximate closed-form solution of ray tracing volume densities. Section 3.4 discusses the integration of VoGE with deep neural networks.  ∂M red .

## VOLUME RENDERING

Different from the surface-based shape representations, in volume rendering, objects are represented using continuous volume density functions. Specifically, for each point in the volume, we have a corresponded density ρ(x, y, z) with emitted color c(x, y, z) = (r, g, b), where (x, y, z) denotes the location of the point in the 3D space. Kajiya & Von Herzen (1984) propose using the light scattering equation during volume density, which provides a mechanism to compute the observed color C(r) along a ray r(t) = (x(t), y(t), z(t)): where τ is a coefficient that determines the rate of absorption, t n and t f denotes the near and far bound alone the ray, T (t) is the transmittance.

## GAUSSIAN ELLIPSOID RECONSTRUCTION KERNEL

Due to the difficulty of obtaining contiguous function of the volume density and enormous computation cost when calculating the integral, Westover (1990) introduces kernel reconstruction to conduct volume rendering in a computationally efficient way. The reconstruction decomposes the contiguous volume into a set of homogeneous kernels, while each kernel can be described with a simple density function. We use volume ellipsoidal Gaussians as the reconstruction kernels. Specifically, we reconstruct the volume with a sum of ellipsoidal Gaussians:

where K is the total number of Gaussian kernels, X = (x, y, z) is an arbitrary location in the 3D space. The M k , a 3 × 1 vector, is the center of k-th ellipsoidal Gaussians kernel. Whereas the Σ k is a 3 × 3 spatial variance matrix, which controls the direction, size and shape of k-th kernel. Also, following Zwicker et al. (2001), we assume that the emitted color is approximately constant inside each reconstruction kernel c(r(t)) = c k .

The VoGE mesh converter creates Gaussian ellipsoids from a mesh. Specifically, we create Gaussians centered at all vertices' locations of the mesh. First, we compute a sphere-type Gaussians with same σ k on each direction, via average distance l from the center vertex to its connected neighbors,

where ζ is a parameter controls the Gaussians size. Then, we flatten the spheretype Gaussians into ellipsoids with a flatten rate. Finally, for each Gaussian, we compute a rotation matrix via the mesh surface normal direction of the corresponded mesh vertex. We dot the rotation matrix onto the Σ k to make the Gaussians flatten along the surface. 

## RENDER GAUSSIAN ELLIPSOIDS

Figure 4 shows the rendering process for VoGE. VoGE takes inputs of a perspective camera and Gaussian ellipsoids to render images, while computing gradient towards both camera and Gaussian ellipsoids (shows in Figure 2 and3).

Viewing transformation utilizes the extrinsic configuration E of the camera to transfer the Gaussian ellipsoids from the object coordinate to the camera coordinate. Let M o k denote centers of ellipsoids in the object coordinate. Following the standard approach, we compute the centers in the camera coordinate:

where R and T are the rotation and translation matrix included in E. Since we consider 3D Gaussian Kernels are ellipsoidal, observations of the variance matrices are also changed upon camera rotations:

Perspective rays indicate the viewing direction in the camera coordinate. For each pixel, we compute the viewing ray under the assumption that the camera is fully perspective:

where p = (i, j) is the pixel location on the image, O x , O y is the principal point of the camera, F is the focal length, D is the ray direction vector.

Ray tracing observes the volume densities of each ellipsoid along the ray r respectively. Note the observation of each ellipsoid is a 1D Gaussian function along the viewing ray (for detailed mathematics, refer to Appendix A.1):

where

is the length along the ray that gives peak activation for m-th

Thus, when tracing along each ray, we only need to record l m , q m and σ m for each ellipsoid respectively. Blending via Volume Densities computes the observation along the ray r. As Figure 1 shows, different from other generic renderers, which only consider the viewing distance for blending, VoGE blends all observations based on the integral of volume densities along the ray. However, computing the integral using brute force is so computationally inefficient that even infeasible for concurrent computation power. To resolve this, we propose an approximate closed-form solution, which conducts the computation in both an accurate and effective way. We use the Error Function erf to compute the integral of Gaussian, since it can be computed via a numerical approach directly. Specifically, with Equation 2and Equation 5, we can calculate the transmittance T (t) as (for proof about this approximation, refer to Appendix A.2):

Figure 5: Comparison for rendering speeds of VoGE and PyTorch3D, reported in images per second (higher better). We evaluate the rendering speed using cuboids with different number of primitives (vertices, ellipsoids), which illustrated using different colors, also different image sizes and number of primitives per pixel.

Now, to compute closed-form solution of the outer integral in Equation 1, we use the T (t), t = l k at the peak of ρ(r(t)) alone the rays. Here we provide the closed-form solution for C(r):

Note based on the assumption that distances from camera to ellipsoids are significantly larger than ellipsoid sizes, thus it is equivalent to set t n = -∞ and t f = ∞.

Coarse-to-fine rendering. In order to improve the rendering efficiency, we implement VoGE rendering with a coarse-to-fine strategy. Specifically, VoGE renderer has an optional coarse rasterizing stage that, for each ray, selects only around 10% of all ellipsoids (details in Appendix A.3). Besides, the ray tracing volume densities also works in a coarse-to-fine manner. VoGE blends K ′ nearest ellipsoids among all traced kernels that gives e q k > thr = 0.01. Using CUDA from NVIDIA et al. ( 2022), we implement VoGE with both forward and backward function. The CUDA-VoGE is packed as an easy-to-use "autogradable" PyTorch API.

## VOGE IN NEURAL NETWORKS

VoGE can be easily embedded into neural networks by serving as neural sampler and renderer. As a sampler, VoGE extracts attributes α k (e.g., deep neural features, textures) from images or feature maps into kernel-correspond attributes, which is conducted via reconstructing their spatial distribution in the screen coordinates. When serving as a renderer, VoGE converts kernel-correspond attributes into images or feature maps. Since both sampling and rendering give the same spatial distribution of feature/texture, it is possible for VoGE to conduct geometry-based image-to-image transformation.

Here we discuss how VoGE samples deep neural features. Let Φ denotes observed features, where ϕ p is the value at location p. Let A = K k=1 {α k } denotes the per kernel attribute, which we want to discover during sampling. With a given object geometry Γ = K k=1 {M k , Σ k } and viewing rays r(p). The the observation formulated with conditional probability regarding α k :

Since Φ is a discrete observation of a continuous distribution ϕ(p) on the screen, the synthesis can only be evaluated at discrete positions, i.e.the pixel centers. As the goal is to make Φ ′ similar as Φ on all observable locations, we resolve via an inverse reconstruction:

where W p,k = T (l k )e q k is the kernel-to-pixel weight as described in 3.1.  

# EXPERIMENT

We explore several applications of VoGE. In section 4.1, we study the object pose estimation using VoGE in a feature level render-and-compare pose estimator. In section 4.2, we explore texture extraction ability of VoGE. In section 4.4, we demonstrate VoGE can optimize the shape representation via multi-viewed images. Visualizations of VoGE rendering are included in Appendix B. Rendering Speed. As Figure 5 shows, CUDA-VoGE provides a competitive rendering speed compare to state-of-the-art differentiable generic renderer when rendering a single cuboidal object.

## OBJECT POSE ESTIMATION IN WILD

We evaluate the ability of VoGE when serving as a feature sampler and renderer in an object pose estimation pipeline, NeMo Wang et al. (2020a), an in-wild category-level object 3D pose estimator that conducts render-and-compare on neural feature level. NeMo utilizes PyTorch3D Ravi et al. (2020) as the feature sampler and renderer, which converts the feature maps to vertex corresponded feature vectors and conducts the inverse process. In our NeMo+VoGE experiment, we use VoGE to replace the PyTorch3D sampler and renderer via the approach described in Section 3.4. Dataset. Following NeMo, we evaluate pose estimation performance on the PASCAL3D+ dataset Xiang et al. (2014), the Occluded PASCAL3D+ dataset Wang et al. (2020b) and the ObjectNet3D dataset Xiang et al. (2016). The PASCAL3D+ dataset contains objects in 12 man-made categories with 11045 training images and 10812 testing images. The Occluded PASCAL3D+ contains the occluded version of same images, which is obtained via superimposing occluder cropped from MS-COCO dataset Lin et al. (2014). The dataset includes three levels of occlusion with increasing occlusion rates. In the experiment on ObjectNet3D, we follow NeMo to test on 18 categories. Evaluation Metric. We measure the pose estimation performance via accuracy of rotation error under given thresholds and median of per image rotation errors. The rotation error is defined as the difference between the predicted rotation matrix and the ground truth rotation matrix:  Experiment Details. Following the experiment setup in NeMo, we train the feature extractor 800 epochs with a progressive learning rate. During inference, for each image, we sample 144 starting poses and optimizer 300 steps via an ADAM optimizer. We convert the meshes provided by NeMo using the method described Section 3.2. Results. Figure 6 and Table 2 show the qualitative and quantitative results of object pose estimation on PASCAL3D+ and the Occluded PASCAL3D+ dataset. Results in Table 2 demonstrate 2020). Moreover, both qualitative and quantitative results show our method a significant robustness under partial occlusion and out distributed cases. Also, Figure 6 demonstrates our approach can generalize to those out distributed cases, e.g., a car without front bumper, while infeasible for baseline renderers. Table 3 shows the results on ObjectNet3D, which demonstrates a significant performance gain compared to the baseline approaches. The ablation study is included in Appendix C.1.

## TEXTURE EXTRACTION AND RERENDERING

As Figure 7 shows, we conduct the texture extraction on real images and rerender the extracted textures under novel viewpoints. The qualitative results is produced on PASCAL3D+ dataset. The experiment is conducted on each image independently that there is no training included. Specifically, for each image, we have only three inputs, i.e. the image, the camera configuration, the Gaussian ellipsoids converted from the CAD models provided by the dataset. Using the method proposed in 3.4, we extract the RGB value for each kernel on the Gaussian ellipsoids using the given groundtruth camera configuration. Then we rerender Gaussian ellipsoids with the extracted texture under a novel view, that we increase or decrease the azimuth of the viewpoint (horizontal rotation). The qualitative   results demonstrate a satisfying texture extraction ability of VoGE, even with only a single image. Also, the details (e.g., numbers on the second car) are retained in high quality under the novel views.

## OCCLUSION REASONING OF MULTIPLE OBJECTS

Figure 8 shows differentiating the occlusion reasoning process between two objects. Specifically, a target image, and the colored cuboid models and initialization locations, are given to the method.

Then we render and optimize the 3D locations of both the cuboids. In this experiment, we find both SoftRas and VoGE can successfully optimize the locations when the occludee (blue cuboid) is near the occluder (red cuboid), which is 1.5 scales behind the occluder as the thickness of the occluder is 0.6 scales. However, when the the occludee is far behind the occluder (5 scales), SoftRas fails to produce correct gradient to optimize the locations, whereas VoGE can still successfully optimize the locations. We think such advantage benefits from the better volume density blending compared to the distance based blender used in SoftRas.

## SHAPE FITTING VIA INVERSE RENDERING

Figure 9 shows the qualitative results of multi-viewed shape fitting. In this experiment, we follows the setup in fit a mesh with texture via rendering from PyTorch3D official tutorial Ravi et al. (2022a). First, a standard graphic renderer is used to render the cow CAD model in 20 different viewpoints under a fixed light condition, which are used as the optimization targets. For both baseline and ours, we give a sphere object geometry with 2562 vertices and optimize toward target images using the same configuration, e.g., iterations, learning rate, optimizer, loss function. During the shape optimization process, we compute MSE loss on both silhouettes and RGB values between the synthesized images and the targets. The vertices locations and colors are gradiently updated with an ADAM optimizer Kingma & Ba (2014). We conduct the optimization for 2000 iterations, while in each iteration, we randomly select 5 out of 20 images to conduct the optimization. In Figure 9 (e) and (f), we use the normal consistency, edge and Laplacian loss Nealen et al. (2006) to constrain the object geometry, while in (d) no additional loss is used. From the results, we can see that VoGE has a competitive ability regarding shape fit via deformation. Specifically, VoGE gives better color prediction and a smoother object boundary. Also, we observe the current geometry constrain losses do not significantly contribute to our final prediction. We argue those losses are designed for surface triangular meshes, that not suitable for Gaussian ellipsoids. The design of geometry constraints that are suitable for Gaussian ellipsoids is an interesting topic but beyond scope of this paper.

# CONCLUSION

In this work, we propose VoGE, a differentiable volume renderer using Gaussian Ellipsoids. Experiments on in-wild object pose estimation and neural view matching show VoGE an extraordinary ability when applied on neural features compare to the concurrent famous differential generic renderers. Texture extraction and rerendering experiment shows VoGE the ability on feature and texture sampling, which potentially benefits downstream tasks. Overall, VoGE demonstrates better differentiability, which benefits vision tasks, while retains competitive rendering speed.

# A ADDITIONAL DETAILS OF VOGE RENDERER

In this section we provide more detailed discussion for the math of ray tracing volume densities in VoGE (section A.1 and A.2), coarse-to-fine rendering strategy (section A.3), and the converters (section A.4).

# A.1 RAY TRACING

In this section, we provide the detailed deduction process for Equations 6 in the main text. First, let's recall the formula of Ray tracing volume densities Kajiya & Von Herzen (1984):

where

where T (t) is the occupancy function alone viewing ray r(t), as we describe in Equation 5in main text:

where D is the normalized direction vector of the viewing ray.

Also, as we describe in Section 3.2, we reconstruct the volume density function ρ(r(t)) via the sum of a set of ellipsoidal Gaussians:

where K is the total number of Gaussian kernels, X = (x, y, z) is an arbitrary location in the 3D volume. M k is the center of k-th ellipsoidal Gaussians kernel:

whereas the Σ k is the spatial variance matrix:

Note that Σ k is a symmetry matrix, e.g., covariance σ k,xy = σ k,yx .

Occupancy Function. Based on Equation 13and 11, T (t) can be computed via:

, where l k is a length along the viewing ray, V k = M k -l k D is the vector from location l k D on the ray to the vertex M k (we will discuss a solution for V k and l k later). Equation 16can be simplified as:

In order to further simplify T (t), we take V k that makes: 

)ds and the difference W (t) -W ′ (t). Since we use the infinite integral with t, only error at end of t axis need to be consider. (c) shows the accumulative

Interestingly, the final error gives a fix value which is independent from σ. Note that the final error is 0.0256 which can be ignored when compared to the integral result W = 1.

which can be solve using

Note that l k is also the length that gives the maximum density ρ k (r(t)) along the ray for k-th kernel.

To proof this, we compute:

Obviously, the solve for ∂ ∂t ρ k (r(t)) = 0 is:

Now the density function of the k-th ellipsoid along the viewing ray r(s) gives an 1D Gaussian function:

where

Thus, when tracing along each ray, we only need to record l k , q k and σ k for each ellipsoid respectively. A.2 BLENDING VIA VOLUME DENSITY Since q k is independent from t, the Equation 16 can be further simplified:

where erf is the error function, that concurrent computation platforms, e.g., PyTorch, Scipy, have already implemented.

Scattering Equation. Now we compute the final color observation C(r). As we describe in Section 3.2, we assume each kernel has a homogeneous C k . Thus, here we compute:

where X = tD. Similar to previous simplifications, we use q k and l k to replace M k in Equation 24:

Due to the error function is already a complex function, it is infeasible to compute the integral of T (t). We propose an approximate solution that we use T (l k ) to replace T (t) inside the integral. Now the final closed-form solution for W k (t) is computed by:

Because of the complexity when computing integral of the erf function, here we prove that in practice such approximate gives high enough accuracy. To simplify the problem, we study the case that the volume only contains a single Gaussian ellipsoid kernel. We further suggest that in the multikernel cases, the errors between different kernels introduced by the approximation will be lower. Because m-th kernel has a low ρ m (r(t)) at l k , which makes the corresponded T (t) more flatten, thus the approximation fits better. As Figure 10 (a) shows, we plot density function along the ray. Specifically, we sample 10k points on the ray, and for each point, we plot its density, the real occupancy, and the approximate occupancy. Figure 10 (b) shows the real weight W which is computed via the cumulative sum along the ray, and the approximate weight W ′ which is computed via our proposed approximate closed-from solution. We also show the difference between W ′ and W with the green line, which is significantly smaller compare to W . Interestingly, as Figure 10 (c) shows, we find the error W (t) -W ′ (t) is independent from Σ -1 and D, that always converge to a same value: 0.0256. Though we cannot give a mathematical explanation regarding this phenomenon, we argue the result is already enough to draw the conclusion that such approximation gives satisfying accuracy.

# A.3 COARSE-TO-FINE RENDERING WITH KERNEL SELECTION

As we discussed in Section 3.3 in the main text, in order to efficiently render Gaussian ellipsoids, we design the coarse-to-fine rendering strategy. Specifically, we gradually reduce the number of ellipsoids that interact with viewing rays. Following PyTorch3D, we develop a optional coarse rasterization stage, which select 10% of all ellipsoids and feed them into the ray tracing stage. Specifically, we project the center of each ellipsoid onto the screen coordinate via standard object-to-camera transformation, then for each ellipsoids, we compute the height b h and width b w of a maximum bounding box of the ellipsoids in 2D screen coordinate. The height and width are computed via:

where d z is the distance from camera to the center of ellipsoid, η is the threshold for maximum volume density, Ω is the projection matrix from camera coordinate to screen:

Then we rasterize the bounding boxes to produce a pixel-to-kernels assignment in a low resolution (8 times smaller compared to the image size), which indicates the set of ellipsoid kernels for each pixel to trace.

Similarly, the ray tracing stage is also select only part of all Gaussian ellipsoids to feed into the blending stage. When conducting ray tracing, we only trace K ′ nearest kernels that has non-trivial contributions regarding its final weight W k . Specifically, we first record all ellipsoids that gives a maximum density e q k > η. For all the recorded kernels, we sort them via the length to the 1D Gaussian center l k and select K ′ nearest ellipsoids. In the experiment, we find K ′ has a significant impact on the quality of rendered images, while the threshold η has relatively low impact, but needs to be fit with K ′ . Here we provide default settings that give a satisfying quality with low computation cost: K ′ = 20, η = 0.01.

Figure 11 shows the rendered cuboids using different K ′ and η. Here the results demonstrate that inadequate K ′ will lead to some dark region around the boundary of kernels, which we think is caused by the hard cutoff of the boundary. On the other hand, decreasing the threshold η could make the object denser (less transparent), but need more kernels (higher K ′ ) to avoid the artifacts.

# A.4 MESH & POINT CLOUD CONVERTER

We develop a simple mesh converter, which converts triangular meshes into isotropic Gaussian ellipsoids, and a point cloud converter. In the mesh converter, we retain all original vertices on the mesh and compute the Σ k using the distance between each vertex and its connected neighbors.

1.5 0 0 0 0.3 0 0 0 0.3 1 0.7 0.6 0.7 1 0.9 0.6 0.9 1 1 1.2 1.6 1.2 1 0.9 1.6 0.9 1 1 0 0.9 0 1 0 0.9 0 1 +0°azimuth +45°azimuth +90°azimuth Specifically, for each vertex, we compute the average length d k of edges connected to that vertex. Then Σ k is computed via:

where σ k is computed via the coverage rate ζ and d k ,

Similarly, in the point cloud converter, the Σ k is controlled with the same function, but the d k is determined by the distance to m nearest points of the target points.

Since the concurrent mesh converter does not consider the shape of the triangles, admittedly we think this could be improved via converting each triangle into an anisotropic Gaussian ellipsoid, which we are still working on.

# B.1 RENDERING ANISOTROPIC GAUSSIAN ELLIPSOIDS

As Figure 12 shows, VoGE rendering pipeline natively supports anisotropic ellipsoidal Gaussian kernels, where for each kernel the spatial variance is represented via the 3 × 3 symmetric matrix Σ k . Note that, the spatial covariances, e.g., σ k,xy , cannot exceed square root of dot product of the two variances, e.g., √ σ k,xx σ k,yy , otherwise, the kernel will become hyperbola instead of ellipsoids (as the last row in Figure 12 shows).

On the other hand, we suggest that ellipsoidal Gaussian kernels can also approximate the 2D Gaussian ellipses (the representation used in DSS Yifan et al. (2019)), which can be simply done by set det(Σ) → 0, where det is the determinant of matrix. Figure 13 shows the rendering result using flattened Gaussian ellipsoids. As we demonstrated in the third row, VoGE rendering pipeline allows rendering the surface-liked representations in a stable manner.

# B.2 RENDERING SURFACE NORMAL

As Figure 14 shows, we render CAD models provided by The Stanford 3D Scanning Repository Curless & Levoy (1996). Specifically, we use our mesh converter to convert the meshes provide by Figure 16 shows surface normal rendering quality of VoGE using different number of Gaussians. We also include comparison of rendering quality of VoGE vs PyTorch3D mesh renderer. In each image, we control a same number of Gaussians vs mesh vertices, which gives similar number of parameters that 9 * N Gauss vs 3 * N verts + 3 * N f aces . Here we observe that increasing number of Gaussians will significant improve rendering quality. Admittedly, VoGE renderer gives slight fuzzier boundary compare to mesh renderer.

# B.4 LIGHTING WITH EXTERNAL NORMALS

Although Gaussian ellipsoids do not contain surface normal information (since they are represented as volume), VoGE still can utilize surface normal via processing them as an extra attribute in an external channel as we describe in section B.2. Once the surface normals are rendered, the light diffusion method in the traditional shader can be used to integrate lighting information into VoGE rendering pipeline. Figure 15 shows the results that integrate lighting information when rendering the Stanford bunny mesh using VoGE. Specifically, we first render the surface normals computed via PyTorch3D into an image-liked map (same as the process in section B.2). Then we use the diffuse function (PyTorch3D.renderer.lighting), to compute the brightness of the rendered bunny under a point light. In the visualization, we place the light source at variant locations, while using a fully white texture on the bunny.

# B.5 RENDERING POINT CLOUDS

Figure 17 shows the point clouds rendering results using VoGE and PyTorch3D. We follow the Render a colored point cloud from PyTorch3D official tutorial Ravi et al. (2022b). Specifically, we use the PittsburghBridge point cloud provided by PyTorch3D, which contains 438544 points with RGB color for each point respectively. We first convert the point cloud into Gaussian ellipsoids using the method described in A.4. Then we render the Gaussian ellipsoids using the same configuration (Except the camera. As the tutorial uses orthogonal camera, which concurrently we don't support,  we alternate the camera using a PerspectiveCamera with a similar viewing scope). The qualitative results demonstrate VoGE a better quality with smoother boundaries.   C ADDITIONAL EXPERIMENT RESULTS

# C.1 IN-WILD OBJECT POSE ESTIMATION

Ablation Study. As Table 4 shows, we conduct controlled experiments to validate the effects of different geometric primitives. Using the method we described in 3.2, we develop tools that convert triangle meshes to Gaussian ellipsoids, where a tunable parameter, coverage rate, is used to control the intersection rate between nearby Gaussian ellipsoids. Specifically, the higher coverage rate gives the large Σ, which makes the feature more smooth but also fuzzy, vice versa. As the results demonstrate, increasing Σ can increase the rough performance under π 6 , while reducing it can improve the performance under the more accurate evaluation threshold. We also ablate the affect regarding block part of the gradient in Equation 8. Specifically, we conduct two experiments on all kernels, we block the gradient on T (l k ) and e q k respectively. The results show blocking either term leads significant negative impact on the final performance.

Additional Results. Table 5 shows the per-category object pose estimation results on PASCAL3D+ dataset (L0). All NeMo Wang et al. (2020a) baseline results and ours are conducted using the single cuboid setting described in NeMo. Specifically, Gaussian ellipsoids used in VoGE is converted from the same single cuboid mesh models provided by NeMo (coverage rate ζ = 0.5).  Figure 18 shows the additional qualitative results of the object pose estimation. In the visualization, we use a standard graphic renderer to render the original CAD models provide by PASCAL3D+ dataset under the predicted pose, and superimpose the rendered object onto the input image. 

# C.2 TEXTURE EXTRACTION AND RERENDERING

Figure 21 shows the additional texture extraction and rerendering results on car, bus and boat images from PASCAL3D+ dataset. Interestingly, Figure 21 (g) shows the texture extraction using VoGE demonstrate stratifying generation ability on those out distributed cases.

# C.3 SHAPE FITTING VIA INVERSE RENDERING

Figure 20 shows the losses in the multi-viewed shape fitting experiment. Specifically, we plot the losses regarding optimization iterations using the method provided by fit a mesh with texture via rendering from PyTorch3D official tutorial Ravi et al. (2022a). Note the geometry constraint losses except normal remain relatively low in VoGE without constraints experiment. We think such results demonstrate the optimization process using VoGE can give correct gradient toward the optimal solution effectively, that even without geometry constraint the tightness of the Gaussian ellipsoids is still retained. As for the normal consistency loss, since we use the volume Gaussian ellipsoids, the surface normal directions are no longer informative.

