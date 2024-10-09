# Introduction

Modeling real scenes from image data and rendering photo-realistic novel views is a central problem in computer vision and graphics. NeRF [35] and its extensions [29,32,64] have shown great success on this by modeling neural radiance fields. These methods [35,38,64] often reconstruct radiance fields using global MLPs for the entire space through ray marching. This leads to long reconstruction times due to the slow per-scene network fitting and the unnecessary sampling of vast empty space.

We address this issue using Point-NeRF, a novel pointbased radiance field representation that uses 3D neural points to model a continuous volumetric radiance field. Unlike NeRF that purely depends on per-scene fitting, Point-NeRF can be effectively initialized via a feed-forward deep neural network, pre-trained across scenes. Moreover, Point-NeRF avoids ray sampling in the empty scene space by leveraging classical point clouds that approximate the actual scene geometry. This advantage of Point-NeRF leads to more efficient reconstruction and more accurate rendering than other neural radiance field models [8, 35,53,63].

Our Point-NeRF representation consists of a point cloud with per-point neural features: each neural point encodes the local 3D scene geometry and appearance around it. Prior point-based rendering techniques [2] use similar neural point clouds but perform rendering with rasterization and 2D CNNs operating in image space. We instead treat these neural points as local neural basis functions in 3D to model a continuous volumetric radiance field which enables high-quality rendering using differentiable ray marching. In particular, for any 3D location, we propose to use an MLP network to aggregate the neural points in its neighborhood to regress the volume density and view-dependent radiance at that location. This expresses a continuous radiance field.

We present a learning-based framework to efficiently initialize and optimize the point-based radiance fields. To generate a initial field, we leverage deep multi-view stereo (MVS) techniques [59], i.e., applying a cost-volume-based network to predict depth which is then unprojected to 3D space. In addition, a deep CNN is trained to extract 2D feature maps from input images, naturally providing the perpoint features. These neural points from multiple views are combined as a neural point cloud, which forms a pointbased radiance field of the scene. We train this point generation module with the point-based volume rendering networks from end to end, to render novel view images and supervise them with the ground truth. This leads to a generalizable model that can directly predict a point-based radiance field at inference time. Once predicted, the initial point-based field is further optimized per scene in a short period to achieve photo-realistic rendering. As shown in Fig. 1 (left), 21 minutes of optimization with Point-NeRF outperforms a NeRF model trained for days.

Besides using the in-built point cloud reconstruction, our approach is generic and can also generate a radiance field based on a point cloud of other reconstruction techniques. However, the reconstructed point cloud produced by techniques like COLMAP [44], in practice, contain holes and outliers that adversely affect the final rendering. To address this issue, we introduce point growing and pruning as part of our optimization process. We leverage the geometric reasoning during volume rendering [13] and grow points near the point cloud boundary in high volume density regions and prune points in low-density regions. The mechanism effectively improves our final reconstruction and rendering quality. We show an example in Fig. 1 (right) where we convert COLMAP points to a radiance field and successfully fill large holes and produce photo-realistic renderings.

We train our model on the DTU dataset [18] and evaluate on DTU testing scenes, NeRF synthetic, Tanks & Temples [23], and ScanNet [11] scenes. The results demonstrate that our approach can achieve state-of-the-art novel view synthesis, outperforming many prior arts including pointbased methods [2], NeRF, NSVF [29], and many other gen-eralizable neural methods [8, 53,63] (see (Tab. 1 and 2)).

# Related Work

Scene representations. Traditional and neural methods have studied many 3D scene representations, including volumes [19,25,41,46,56], point clouds [1,40,51], meshes [20,52], depth maps [17,28], and implicit functions [9,33,37,60], in diverse vision and graphics applications. Recently, various neural scene representations have been presented [4, 30,47,67], advancing the state of the art in novel view synthesis and realistic rendering, with volumetric neural radiance fields (NeRFs) [35] producing high fidelity results. NeRFs are often reconstructed as global MLPs [35,38,64] that encode the entire scene space; this can be inefficient and expensive when reconstructing complex and large-scale scenes. Instead, Point-NeRF is a localized neural representation, combining volumetric radiance fields with point clouds that are classically used to approximate scene geometry. We distribute fine-grained neural points to model complex local scene geometry and appearance, leading to better rendering quality than NeRF (see Fig. 6,7).

Voxel grids with per-voxel neural features [8, 16,29] are also a local neural radiance representation. However, our point-based representation adapts better to actual surfaces, leading to better quality. Also, we directly predict good initial neural point features, bypassing the per-scene optimization that is required by most voxel-based methods [16,29].

Multi-view reconstruction and rendering. Multi-view 3D reconstruction has been extensively studied and addressed with a number of structure-from-motion [43,49,50] and multi-view stereo techniques [10,14,25,44,59]. Point clouds are often the direct output from MVS or depth sensor, though they are usually converted to meshes [21,31] for rendering and visualization. Meshing can introduce errors and may require image-based rendering [6, 12,66] for highquality rendering. We instead directly use point clouds from deep MVS to achieve realistic rendering.

Point clouds have been widely used in rendering, often via rasterization-based point splatting, and even differentiable rasterization modules [26,55]. However, reconstructed point clouds often have holes and outliers that lead to artifacts in rendering. Point-based neural rendering methods address this by splatting neural features and using 2D CNNs to render them [2, 24,34]. In contrast, our point-based approach utilizes 3D volume rendering, leading to significantly better results than previous point-based methods.

Neural radiance fields. NeRFs [35] have demonstrated remarkably high-quality results for novel view synthesis. They have been extended to achieve dynamic scene capture [27,39], relighting [3,5], appearance editing [57], fast rendering [16,62], and generative models [7,36,45]. However, most methods [3,27,39,57] still follow the original NeRF framework and train per-scene MLPs to represent radiance fields. We make use of neural points with spatially varying neural features in a scene to encode its radiance field. This localized representation can model more complex scene content than pure MLPs that have limited network capacity. More importantly, we show that our pointbased neural field can be efficiently initialized via a pretrained deep neural network that generalizes across scenes and leads to highly efficient radiance field reconstruction.

Prior works also present generalizable radiance fieldbased methods. PixelNeRF [63] and IBRNet [53] aggregate multi-view 2D image features at every sampled ray point to regress volume rendering properties for radiance field rendering. In contrast, we leverage features in 3D neural points around the scene surface to model radiance fields. This avoids sampling points in the vast empty space and leads to higher rendering quality and faster radiance field reconstruction than PixelNeRF and IBRNet. MVSNeRF [8] can achieve very fast voxel-based radiance field reconstruction. However, its prediction network requires a fixed number of three small-baseline images as input and thus can only efficiently reconstruct local radiance fields. Our approach can fuse neural points from an arbitrary number of views and achieve fast reconstruction of complete 360 radiance fields which MVSNeRF cannot support.

# Point-NeRF Representation

We present our novel point-based radiance field representation, designed for efficient reconstruction and rendering (see Fig. 2 (b)). We start with some preliminaries.

Volume rendering and radiance fields. Physically-based volume rendering can be numerically evaluated via differentiable ray marching. Specifically, a pixel's radiance can be computed by marching a ray through the pixel, sampling M shading points at {x j | j = 1, ..., M } along the ray, and accumulating radiance using volume density, as:

Here, τ represents volume transmittance; σ j and r j are the volume density and radiance for each shading point j at x j , ∆ t is the distance between adjacent shading samples.

A radiance field represents the volume density σ and view-dependent radiance r at any 3D location. NeRF [35] proposes to use a multi-layer perceptron (MLP) to regress such radiance fields. We propose Point-NeRF that instead utilizes a neural point cloud to compute the volume properties, allowing for faster and higher-quality rendering.

Point-based radiance field. We denote a neural point cloud by P = {(p i , f i , γ i )|i = 1, ..., N }, where each point i is located at p i and associated with a neural feature vector f i that encodes the local scene content. We also assign each point a scale confidence value γ i ∈ [0, 1] that represents how likely that point is being located near an actual scene surface. We regress the radiance field from this point cloud.

Given any 3D location x, we query K neighboring neural points around it within a certain radius R. Our pointbased radiance field can be abstracted as a neural module that regresses volume density σ and view-dependent radiance r (along any viewing direction d) at any shading location x from its neighboring neural points as:

We use a PointNet-like [40] neural network, with multiple sub-MLPs, to do this regression. Overall, we first conduct neural processing for each neural point and then aggregate the multi-point information to obtain the final estimates.

Per-point processing. We use an MLP F to process each neighboring neural point to predict a new feature vector for the shading location x by:

Essentially, the original feature f i encodes the local 3D scene content around p i . This MLP network expresses a local 3D function that outputs the specific neural scene description f i,x at x, modeled by the neural point in its local frame. The usage of relative position x -p makes the network invariant to point translation for better generalization.

View-dependent radiance regression. We use standard inverse distance weighting to aggregate the neural features f i,x regressed from these K neighboring points to obtain a single feature f x that describes scene appearance at x:

Then an MLP, R, regress the view-dependent radiance from this feature given a viewing direction, d:

The inverse-distance weight w i is widely used in scattered data interpolation; we leverage it to aggregate neural features, making closer neural points contribute more to the shading computation. In addition, we use the per-point confidence γ in this process; this is optimized in the final reconstruction with a sparsity loss, giving the network the flexibility of rejecting unnecessary points.

Density regression. To compute volume density σ at x, we follow a similar multi-point aggregation. However, we first regress a density σ i per point using an MLP T and then do inverse distance-based weighting, given by:  

Thus, each neural point directly contributes to the volume density, and point confidence γ i is explicitly associated with this contribution. We leverage this in our point removal process (see Sec. 4.2).

Discussion. Unlike previous neural point-based methods [2, 34] that rasterize point features and then render them with 2D CNNs, our representation and rendering are entirely in 3D. By using a point cloud that approximates the scene geometry, our representation naturally and efficiently adapts to scene surfaces and avoids sampling shading locations in empty scene space. For shading points along each ray, we implement an efficient algorithm to query neighboring neural points; details are in the supplemental material.

# Point-NeRF Reconstruction

We now introduce our pipeline for efficiently reconstructing point-based radiance fields. We first leverage a deep neural network, trained across scenes, to generate an initial point-based field via direct network inference (Sec. 4.1). This initial field is further optimized per scene with our point growing and pruning techniques, leading to our final high-quality radiance field reconstruction (Sec. 4.2). Figure . 3 shows this workflow with the corresponding gradient updates for the initial prediction and perscene optimization. 

## Generating initial point-based radiance fields

Given a set of known images I 1 ,...,I Q , and a point cloud, our Point-NeRF representation can be reconstructed by optimizing the randomly initialized per-point neural features and the MLPs with a rendering loss (similar to NeRF). However, this pure per-scene optimization depends on an exisiting point cloud, and can be prohibitively slow. Therefore, we propose a neural generation module to predict all neural point properties, including point locations p i , neural features f i and point confidence γ i , via a feed-forward neural network for efficient reconstruction. The direct inference of the network outputs a good initial point-based radiance field. The initial fields can then be fine-tuned to achieve high-quality rendering. In a very short period, the rendering quality is better or on par with NeRF which takes substantially longer time to optimize (see Tab. 1 and 2).

Point location and confidence. We leverage deep MVS methods to generate 3D point locations using cost volumebased 3D CNNs [10,59]. Such networks produce highquality dense geometry and generalize well across domains. For each input image I q with camera parameters Φ q at viewpoint q, we follow MVSNet [17] to first build a plane-swept cost volume by warping 2D image features from neighboring viewpoints and then regress depth probability volume using deep 3D CNNs. A depth map is computed by linearly combining per-plane depth values weighted by the probabilities. We unprojected the depth map to 3D space to get a point cloud {p 1 , ..., p Nq } per view q.

Since the depth probabilities describe the likelihood of the point being on the surface, we tri-linearly sample the depth probability volume to obtain the point confidence γ i at each point p i . The above process can be expressed by

where G p,γ is the MVSNet-based network. I q1 , Φ q1 , ... are additional neighboring views used in the MVS reconstruc-tion; we use two additional views in most cases.

Point features. We use a 2D CNN G f to extract neural 2D image feature maps from each image I q . These feature maps are aligned with the point (depth) prediction from G p,γ and are used to directly predict per-point features f i as:

In particular, we use a VGG network architecture for G f that has three downsampling layers. We combine intermediate features at different resolutions as f i , providing a meaningful point description that models multi-scale scene appearance. (See Fig. 2(a))

End-to-end reconstruction. We combine point clouds from multiple viewpoints to obtain our final neural point cloud. We train the point generation networks along with the representation networks, from end to end with a rendering loss (see Fig. 3). This allows our generation modules to produce reasonable initial radiance fields. It also initializes the MLPs in our Point-NeRF representation with reasonable weights, significantly saving the per-scene fitting time. Moreover, apart from using the full generation module, our pipeline also supports using a point cloud reconstructed from other approaches like COLMAP [44], where our model (excluding the MVS network) can still provide meaningful initial neural features for each point. Please refer to our supplementary material for the details.

## Optimizing point-based radiance fields

The above pipeline can output a reasonable initial pointbased radiance field for a novel scene. Through differentiable ray marching, we can further improve the radiance field by optimizing the neural point cloud (point features f i and point confidence γ i ) and the MLPs in our representation, for that specific scene (see Fig. 3).

The initial point cloud, especially ones from external reconstruction methods (e.g., Metashape or COLMAP in Fig. 1), can often contain holes and outliers that degrade the rendering quality. During per-scene optimization, to solve this problem, we find that directly optimizing the location of the existing points makes the training unstable and cannot fill the large holes (see 1). Instead, we apply novel point pruning and growing techniques that gradually improve both geometry modeling and rendering quality.

Point pruning. As introduced in Sec. 3, we designed point confidence values γ i that describe whether a neural point is near a scene surface. We utilize these confidence values to prune unnecessary outlier points. Note that the point confidence is directly related to the per-point contribution in volume density regression (Eqn. 7); as a result, low confidence reflects low volume density in a point's local region indicating that it is empty. Therefore, we prune points that have γ i < 0.1 every 10K iterations.

We also impose a sparsity loss on point confidence [30]:

which forces the confidence value to be close to either zero or one. As shown in Fig. 4, this pruning technique can remove outlier points and reduce the corresponding artifacts.

Point growing. We also propose a novel technique to grow new points to cover missing scene geometry in the original point cloud. Unlike point pruning that directly utilizes information from existing points, growing points requires recovering information in empty regions where no point exists. We achieve this by progressively growing points near the point cloud boundary based on the local scene geometry modeled by our Point-NeRF representation.

In particular, we leverage the per-ray shading locations (x j in Eqn. 1) sampled in the ray marching to identify new point candidates. Specifically, we identify the shading location x jg with the highest opacity along the ray:

We compute jg as x jg 's distance to its closest neural point. For a marching ray, we grow a neural point at x jg if α jg > T opacity and jg > T dist . This implies that the location lies near the surface, but is far from other neural points. By repeating this growing strategy, our radiance field can be expanded to cover missing regions in the initial point cloud. Point growing especially benefits point clouds reconstructed by methods like COLMAP that are not dense (see Fig. 4). We show that even on an extreme case with only 1000 initial points, our technique is able to progressively grow new points and reasonably cover the object surface (see Fig. 5).

# Implementation details

Network details. We apply frequency positional encoding on the relative position and the per-point features for the per-point processing network G f , and the viewing direction for the network R. We extract multi-scale images features from three layers at different resolutions in network G f , leading to a vector with 56 (8+16+32) channels. We additionally append the corresponding viewing directions from each input viewpoint, to handle view-dependent effects. Therefore our final per-point neural feature is a 59channel vector. Please refer to our supplemental material for the details of network architectures and neural point querying during shading.

Training and optimization details. We train our full pipeline on the DTU dataset, using the same training and testing split as PixelNeRF and MVSNeRF. We first pretrain the MVSNet-based depth generation network using the ground truth depth similar to the original MVSNet paper [59]. We then train our full pipeline from end to end purely with a L2 rendering loss L render , supervising our rendered pixels from ray marching (via Eqn. 1) with the ground truth, to obtain our Point-NeRF reconstruction network. We train our full pipeline using Adam [22] optimizer with an initial learning rate of 5e -4 . Our feed-forward network takes 0.2s to generate a point cloud from three input views.

In the per-scene optimization stage, we adopt a loss function that combines the rendering and the sparsity loss

where we use a = 2e -3 for all our experiments. We perform point growing and pruning every 10K iterations to achieve our final high-quality reconstruction.

# Experiments

6.1. Evaluation on the DTU testing set.

We evaluate our model on the DTU testing set. We produce novel view synthesis from both direct network inference and per-scene fine-tuning optimization, and compare them with the previous state-of-the art methods including PixelNeRF [63], IBRNet [53], MVSNeRF [8], and NeRF [35]. IBRNet and MVSNeRF utilize similar per-scene finetuning; we fine-tune all methods with 10k iterations for the comparison. Additionally, we show our results with only 1k iterations to demonstrate the optimization efficiency.

Tab. 1 shows the quantitative results of all methods with PSNR, SSIM, and LPIPS; qualitative rendering results are shown in Fig. 6. We can see that our fine-tuning results after 10k iterations achieve the best SSIM and LPIPS [65], two out of the three metrics. These are significantly better than MVSNeRF and NeRF. While IBRNet produces slightly better PSNRs, our final renderings in fact recover more accurate texture details and highlights as shown Fig. 6. On the other hand, IBRNet is also more expensive to finetune, taking 1 hour-5x longer than ours for the same iterations. This is because IBRNet utilizes a large global CNN, whereas Point-NeRF leverages local point features with small MLPs that are easier to optimize. More importantly, our neural points lies near actual scene surfaces, thus avoids sampling ray points in the empty space.

Apart from the optimization results, our initial radiance field estimated from our network is significantly better than PixelNeRF. In this case, our direct inference is worse than IBRNet and MVSNet, mainly because these two methods are using more complex variance-based feature extraction. Our point features are extracted from a simple VGG network. The same design is used in PixelNeRF; we achieve significantly better results than PixelNeRF due to our novel surface-adaptive point-based representation.

While a more complex feature extractor as in IBRNet might improve quality, it will add burden to memory usage and training efficiency. More importantly, our generation network has already provided high-quality initial radiance field to support efficient optimization. We show that with even 2 min / 1K iterations of fine-tuning for our method leading to a very high visual quality comparable to MVS-NeRF's final 10k-iteration results. This clearly demonstrates the high reconstruction efficiency of our approach.

## Evaluation on the NeRF Synthetic dataset.

While our model is purely trained on the DTU dataset, our network generalizes well to novel datasets that have completely different camera distributions. We demonstrate such results on the NeRF synthetic dataset and compare with other methods with qualitative results in Fig. 7 and quantitative results in Tab. 2. We compare with a pointbased rendering model (NPBG) [2], a generalizable radiance field method (IBRNet) [53], and per-scene radiance field reconstruction techniques (NeRF and NSVF) [29,35].

Comparisons with generalizing methods. We compare with IBRNet, to the best of our knowledge, is the previous best NeRF-based generalizable model that can handle free-viewpoint rendering with any arbitrary numbers. Note that, this dataset has a 360 • camera distribution, which is much wider than the DTU dataset. In this case, methods like MVSNeRF cannot be applied, since it recovers a local perspective frustum volume from three input images, which cannot cover the entire 360 • viewing range. We, therefore, compare with IBRNet and focus on final results after per-scene optimization in this experiment. We use their released model to produce the results. Our results at 20k iterations (Point-NeRF 20K ) have already outperformed IBR-Net's converged results with better PSNR, SSIM, and LIP-IPS; we also achieve rendering quality with better geometry and texture details as shown in Fig. 7.

Comparisons with pure per-scene methods. Our results after 20K iterations are quantitatively very close to NeRF's results trained with 200K iterations. Visually, our model at 20K iterations already has better renderings in some cases, e.g. the Ficus scene (4th row) in Fig. 7. Point-NeRF 20K is optimized for only 40 minutes, which is at least 30× faster than the 20+ hours optimization time taken by NeRF. NSVF's [29] results are also from very long per-scene optimization and yet are only slightly better than our 40min results. Optimizing our model for 200K until convergence can lead to significantly better results than NeRF, NSVF, and all other comparison methods. As shown in Fig. 7, our 200K results contain the most geometry and texture details. Attribute to the point growing technique, our method is the only one that can fully recover details like the thin rope structure in the Ship scene (2nd row).

Comparisons with point-based rendering. Our results are significantly better than the previous state-of-the-art pointbased rendering methods. We run NPBG [2] using the same point cloud generated by our MVSNet-based network.  However, NPBG can only produce blurry rendering results with their rasterization and 2D CNN framework. In contrast, we leverage volumetric rendering technique with neural radiance fields, leading to photo-realistic results.

## Evaluation on the Tanks & Temples and the ScanNet dataset.

We compare Point-NeRF with NSVF on the Tanks & Temples and the ScanNet dataset in Tab. 3. Please refer to the supplemental materials for more comparisons.

Tanks & Temples [23] ScanNet [ 

## Additional experiments.

Converting COLMAP point clouds to Point-NeRF Apart from using our full pipeline, Point-NeRF can also be used to convert standard point clouds reconstructed by other techniques to point-based radiance fields. We run experiments for this on the full NeRF synthetic dataset, using the point cloud reconstructed by COLMAP [44]. The quantitative results are shown as Point-NeRF col in Tab. 2. Since COLMAP point clouds may contain a lot of holes (as shown in Fig. 1) and noises, we optimize the model for 200K after the initialization to address the point cloud issues with our point growing and pruning techniques. Note that, even from this low-quality point cloud, our final results are still of very high quality with very high SSIM and LPIPS numbers compared to all other methods. This demonstrates that our technique can be potentially combined with any existing point cloud reconstruction techniques, to achieve realistic rendering while improving the point cloud geometry.

Point growing and pruning. To further demonstrate the effectiveness of our point growing and pruning modules, we show ablation study results with and without the point growing and pruning in the per-scene optimization. We conduct this experiment on the Hotdog and Ship scenes, using both our full model and our model with COLMAP point clouds. The quantitative results are shown in Tab. 4; our point growing and pruning techniques are very effective, significantly improving the reconstruction results on both cases. We also show the visual results of the Hotdog scene in Fig. 4. We can clearly see that our model is able to prune the point outliers on the left and successfully fill the severe holes on the right in the original COLMAP point cloud.

We also manually create an extreme example to show our point growing technique in Fig. 5, where we start from a very sparse point cloud with only 1000 points sampled from our original point reconstruction. We demonstrate that our approach can progressively grow new point from the point cloud boundary until filling the entire scene surface through iterations. This example further demonstrates the effectiveness of our model, which has high potentials in using image data to recover the accurate scene geometry and appearance from low-quality point clouds.

Please find more results in the supplemental materials.  4. The quantitative results (PSNR / SSIM / LPIPSV gg ) of the Ship and Hotdog scene with or without point pruning and growing (P&G). The improvements are significant when using either our generated points or the point cloud generated by COLMAP [44].

# Conclusion

In this paper, we present a novel approach for highquality neural scene reconstruction and rendering. We propose a novel neural scene representation-Point-NeRFthat models a volumetric radiance field with a neural point cloud. We reconstruct a good initialization of Point-NeRF directly from input images via direct network inference and show that we can efficiently finetune this initialization for a scene. This enables highly efficient Point-NeRF reconstruction with only 20-40 min per-scene optimization, leading to rendering quality comparable to and even surpassing NeRF that requires substantially longer training time (20+ hours). We also present novel effective growing and pruning techniques for our per-scene optimization, significantly improving our results and making our approach robust with different point cloud quality. Our Point-NeRF successfully combines the advantages from both classical point cloud representation and neural radiance field representation, making an important step towards a practical scene reconstruction solution with high efficiency and realism. Figure 6. Qualitative comparisons of per-scene optimization on the DTU dataset [18]. Our Point-NeRF can recover texture details and geometrical structures more accurately than other methods. Point-NeRF also demonstrates superior efficiency. Within two mins, our model trained for 1K steps is already on par with the state-of-the-art methods such as MVSNeRF [8] and IBRNet [53] Figure 7. Qualitative comparisons on the NeRF Synthetic dataset [35]. The subscripts indicate the number of iterations. Our Point-NeRF can capture fine details and thin structures (see the rope on row 2). Point-NeRF also demonstrates superior efficiency. Our model trained for 20K steps already on par with NeRF with 30× faster training time. We conduct experiments to demonstrate the importance of our feature initialization. We compare our full model and our model initialized without using the extracted image features on the NeRF Synthetic dataset [35]. Without using the features from images, we randomly initialize the point features by using the popular Kaiming Initialization [15]. As shown in Table 5, the neural points with image features not only achieve better performance after convergence at 200K iterations but also converge much faster in the beginning. The randomly initialized neural points even cannot perform as well as our full model, still outperforms state-of-the-art methods such as NeRF and NSVF [29].

# B. Per-scene Breakdown Results of the DTU Dataset

We show the per scene detailed quantitative results of the comparisons on the DTU [18] dataset in Table 6 and additional qualitative comparisons in our video. Since our method also faithfully reconstructs the scene geometry, our method has the best SSIM scores in most of the cases. Our model also has the best LPIPS for most of the scenes and therefore, is more visually authentic, as shown in the Figure 6 of the main paper and the video. IBRNet combines the colors from the source views to compute the radiance colors during shading. This image-based approach results in better PSNR. However, as shown in our video, our method is more temporal consistent because the local radiance and geometries are consistently stored at each neural point location.

# C. Per-scene Breakdown Results of the NeRF Synthetic Dataset

We show the per scene detailed quantitative results of the comparisons on the NeRF Synthetic [35] dataset in of the scenes and outperforms state-of-the-art methods [2, 29,35,53] with a big margin. On the other hand, our method initiated with COLMAP points is on par with NeRF. Even starting from the unideal initial points, we still manage to improve the geometry reconstruction and generate a highquality radiance field with point pruning and growing. The fact that our model at 20K iterations matches the results of NeRF at 500K iterations clearly demonstrates our ability of fast convergence.

# D. Evaluation on Large-scale 3D Scenes (Scan-Net).

While our model is purely trained on a dataset of objects (the DTU dataset), our network generalizes well to large-scale 3D scene datasets. Following [29], we use two 3D scenes, scene 0101 04 and scene 0241 01, from Scan-Net [11]. We extract both RGB and depth images from the original videos and from which we sample one out of five frames as training set and use the rest for testing. The RGB images are scaled to 640 × 480. We finetune each scene for 300K steps with point pruning and growing.

We compare with 3 other state-of-the-art methods with quantitative results in Tab. 2. In particular, we compare with a scene representation model (SRN) [48], NeRF [35] [11] selected in NSVF [29]. RMSE is the Root Mean Square Error. Our method Point-NeRF outperforms all state-of-the-art methods in all metrics by substantial margins. We also report the (original/calibrated) SSIM. Our original SSIM uses the Skimage library with dynamic max signal value while several current papers use SSIM with as 1, therefore we also calibrate to their settings. Besides, per other authors' requests, we also add our method starting with the mesh instead of depth images, and report its results after 100K steps. Since the mesh of Scene 101 is extremely incomplete, we can observe tremendous quality loss.

sparse voxel-based neural radiance field, NSVF [29]. The qualitative comparison is shown in Tab. 8 and visual results are shown in Figure 8. Our Point-NeRF outperforms all these previous studies in all metrics by substantial margins.

Please find more visual results in our video.  

# E. The Tanks and Temple Dataset

We also experiment Point-NeRF on the Tanks and Temples dataset [23]. we reconstruct the radiance field of five scenes selected in NSVF [29] and compare our model with three models NV [30], NeRF [35] and NSVF [29]. We show the quantitative comparison in Tab. 9 and visualize quality results in Figure 9. Please find more visual results in our video.

# F. Initializing Neural Points from COLMAP Points

Point-NeRF can use the points of any external reconstruction method. For instance, the output of COLMAP [44] is a point cloud {(p i )|i = 1, ..., N }. We set γ i as 0.3 in the beginning. The confidence score of valid points will be pushed to 1 during the optimization process. To acquire point features f i for a point, We first rule out all the views where the point is occluded by other points, then we find the view of which the camera is the closest to the point. Then from that view, we can unproject the point onto the feature maps extracted by G f (see Figure 2(a) in the main paper) from the selected view and obtain the f i .

# G. Networks Architectures

Cost volume-based CNN G p,γ . Our cost volume-based CNN adopts the popular architecture of [59], which is simple and efficient. It includes three layers of depth features  extraction CNN, while the latter two layers down-samples the spatial dimension by 4 and output a feature map with 32 channels. Then, these features from each view will be warped according to camera pose and the variance will be computed. The variance features will go through a narrow U-Net [54] and output a 1-channel feature to calculate the depth probability.

Image Feature Extraction 2D CNN G f . The image feature extraction network takes inputs of RGB image and has three down-sampling layers, each output feature with channels of 8, 16, 32. We extract the point features by unprojecting a 3D point to each layer and taking the multi-scale features.

Point-based Radiance Fields MLP. We visualize the details of the point feature aggregation and radiance computation in Figure 10. In all of our experiments, we set c 1 = 56, c2 = 128. The MLPs F, R, T have 2, 3, 2 layers, respectively. The intermediate feature channels of F and T are 256, and 128 channels for R.

# H. Neural Point Querying

To efficiently query neural point neighbors for ray marching, inspired by the CAGQ point query introduced in [58], we implement a grid query method. Then we build grid-point indices which register each neural point to evenly spaced 3D grids. Since these grids in the perspective coordinate are cubic, in the world coordinate, they have shapes of spherical voxels.

With the grid-point indices, we can discover grids that have neural points and also their grid neighbors. These grid neighbors are the regions of interest since there should exist neural points within the query radius. If a ray crosses these regions, we can place shading points inside. Finally, we query neural points by directly retrieving the stored neural points according to the grid-point indices.

In all of our experiments, we query 8 nearest neural point neighbors for each shading location. Along each ray, we only search for neural point neighbors and compute radiance for shading locations in a grid that is occupied itself or nearby occupied grids. Therefore, our shading is much more efficient by skipping the empty space, unlike other radiance fields representations. This is one key advantage that enables fast convergence. Even NSVF [29], highperformance local radiance representation, has to probe the empty space in the beginning and gradually prune the voxels along its training process.

The benefit of this strategy is two-fold: First, we only place shading points in the area that exists neural points, so that we avoid radiance computation in the empty space. Second, the nearby points can be efficiently retrieved according to the indices, which substantially accelerate the point query speed.

# I. Limitations

Because we do not focus on the rendering speed and we have not optimized our implementation (point querying and point feature aggregation) for fast rendering. Although, our model is naturally faster than NeRF (3X) due to that we skip the shading in empty space. We believe future works on combining mechanisms introduced in current papers such as [42,62] with our point-based radiance representation would further benefit the neural rendering technology.

# J. Additional Discussion and Issues Need Attention

Processing the points generated by MVSNet We have received constructive feedbacks and hope to make it clear that when Point-NeRF uses MVSNet [59] to reconstruct point cloud, the point fusion after depth estimation by MVSNet will use the alpha channel in the NeRF-Synthetic Dataset (as our published code indicates). It is due to the fact that MVSNet cannot handle background very well and will create too many outlier points in the background areas. Since images in the Tanks and Temples Dataset [23] don't have a alpha channel, we filter out the MVSNet points that appear in the regions of the pure background color. On the NeRF-Synthetic Dataset, the methods we compared with [29, 32], used the inputs: RGB images with the knowledge of the pure color background. Therefore, To improve the fairness, on the NeRF-Synthetic Dataset, we include results of Point-NeRF with MVSNet when using background color for filtering (not the alpha channel anymore). Its results is shown in Table 10 and one can cite which ever set-ting one thinks is fair. Please note that, in our experiments, COLMAP doesn't use any filtering. Therefore, there is no impact on COLMAP results. When compare with NPGB [2], we use the same point cloud. Since it is more meaningful to rule out the impact of the point cloud quality, we advocate other point-based rendering works to use the same point cloud if willing to compare with our results. The point clouds are included in the checkpoints we published in the github repo.

Our original intention of using MVSNet is due to its simplicity and the fact that it is one of the earlies deep learningbased MVS model. We, thus, encourage users to try a more advanced MVS model so that no filtering is needed.

# ScanNet and Unbounded Scenes

We also receive comments about our ScanNet experiments, and we would like to state very clearly that we use the depth images from the ScanNet Dataset to initialize the point cloud. It is because NSVF is our major baseline on this dataset and it uses this setting. In our original paragraph Appendix D we have provided this information, and we hope this could clear the potential false expectation from readers.

Since Point-NeRF is a local radiance representation, without additional components, such as an additional background NeRF (used by Plenoxel [61]), it cannot handle background in Unbounded scenes (also known as insideout scenes). For ScanNet, there is not much of background since it is a indoor scene with noisy depth images, every parts in the room can be deemed as foreground.  10. We use MVSNet [59] to reconstruct the points and filter them by using background color, then initialize neural points and optimized our Point-NeRF model for 200 thousand iterations.

# Research.

projects/project_sites/pointnerf for code and more results.

