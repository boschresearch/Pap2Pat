# Introduction

Perceiving and modeling the geometry and dynamics of 3D entities is an open research problem in computer vision and has numerous applications. One fundamental challenge is the under-constrained nature of the problem: from limited 2D image measurements, there exist multiple interpretations of the geometry and motion of the 3D world.

A recent and promising trend for addressing this challenge is exploiting data priors, which have proven quite successful for high-level vision tasks, such as image classification and object detection [13,32]. However, in contrast to high-level vision tasks, it is often costly to obtain 3D annotations for real-world entities. For example, SMPL [34] is learned from thousands of registered 3D scans of human. SMAL [59] is learned from scans of animal toys and a manually rigged mesh model. It involves nontrivial efforts to collect such data for an arbitrary object category. Therefore, existing methods often fail to capture objects of novel or unknown classes, and hallucinate an average 3D structure based on the category shape prior, as shown in Fig. 1.

Interestingly, remarkable progress has been made in the field of SLAM and structure-from-motion without relying on strong shape priors by taking advantage of multiview data recordings. However, such results are limited to static scenes. We explore an intermediate regime between these two extremes: Can one reconstruct an articulated shape from video data without relying on template priors? Why videos? To reconstruct 3D object shape from images, prior work learns category-specific shape models either from 3D data [17,42] or from 2D supervision, such as object silhouette and keypoints in a large image collection [10,18,23,31]. However, 3D data are generally difficult to acquire at a large scale due to sensor design. Although it is easier to collect images of the same category, enforcing multiview constraints is often challenging, due to ambiguities of associating 2D observations across instances and under different viewpoints [11,40]. Video serves as an alternative to depth scans and image collections -videos are easier to acquire, and provide well-defined multiview constraints on the 3D shape of the same instance. Why optical flow? To solve the inverse problem, prior work discussed various forms of 2D constraints or supervision, such as object silhouette, texture, 2D keypoints, and semantic parts [4,18,23,31]. Why should motion be treated as a first-class citizen? Besides that optical flow naturally encodes correspondences, it provides more fine-grained information than keypoints as well as semantic parts. Different from long-range point tracks, which is the classic input for NRSfM [43], optical flow can be obtained more reliably [48,53] over two consecutive frames. Why not nonrigid SfM? NRSfM deals with a problem similar to ours: given a set of 2D point trajectories depicting a deformable object in a collection of images, the goal is to recover the 3D object shape and pose (i.e., relative camera position) in each view. Usually, trajectories of 2D points are factorized into low-rank shape and motion matrices [8,19,27] without using 3D shape templates. Although NRSfM is able to deal with generic shapes, it requires reliable long-term point tracks or keypoint annotations, which are challenging to acquire densely in practice [43,45,47]. Proposed approach: Instead of inferring 3D shapes from category-specific image collections or point trajectories, we build an articulated shape model from a monocular video of an object. Recent progress in differentiable rendering allows one to recast the problem as an analysis-by-synthesis task: we solve the inverse graphics problem of recovering the 3D object shape (including spacetime deformations) and camera trajectories (including intrinsics) to fit video observations, such as object silhouette, raw pixels, and optical flow. An overview of the pipeline is shown in Fig. 2. Contributions: We propose a method for articulated shape reconstruction from a monocular video that does not require a prior template or category information. It takes advantage of dense two-frame optical flow to overcome the inherent ambiguity in the nonrigid structure and motion estimation Table 1. Related work in nonrigid shape reconstruction. (1) Modelbased optimization and regression methods. (2) Category-specific mesh reconstruction. (3) Template-free approaches. S: single view. V: video or multi-view data. I: images. J2: 2D joints. J3: 3D joints. M: 2D masks. V3: 3D scans. C: camera matrices. F: optical flow. MF: multi-frame optical flow. quad: quadruped animals. 

SMPLify [7] human SMPL S:J2,M None VIBE [26] human SMPL V:I J2,J3 SMALify [6] quadx5 SMAL V:J2,M None SMALR [58] quadx12

CMR [23] bird † SfM-hull S:I J2,M,C UCMR [18] bird † cate-mesh S:I M UMR [31] bird † None S:I M IMR [49] animals cate-mesh S:I M A-CSM [28] animals It combines coarse-to-fine re-meshing with soft-symmetric constraints to recover high-quality meshes. Our method demonstrates state-of-the-art reconstruction performance in the BADJA animal video dataset [6], strong performance against model-based methods on humans, and higher accuracy on two animated animals than A-CSM [28] and SMALify [6] that use shape templates.

# Related Work

Below and in Tab. 1, we discuss related work of nonrigid shape recovery according to priors being used (shape template, category prior, or generic shape and motion priors). Model-based reconstruction: Model-based reconstruction leverages a parametric shape model to solve the underconstrained 3D shape and pose estimation problem. A large body of work in 3D human and animal reconstruction uses such parametric shape models [34,36,52,58,59], which are learned from 3D scans of human or animal toys [34,59], and allow one to recover the 3D shape given very few annotations at test time (2D keypoints and silhouettes). Recently, model-based regression methods are developed to predict model-specific shape and pose parameters from a single image or video [3, 5, 26,  rich 3D data, it is challenging to apply to unknown object categories, or categories with limited 3D data.

Category mesh reconstruction: A recent trend is to reduce supervision from 3D or multi-view capturing to 2D annotations, such as keypoints and object silhouettes [18,23,31]. Such methods often take advantage of category priors, including a collection of images from the same category, and category-specific shape templates [28,49]. Recent progress makes single-view reconstruction of birds and other common categories possible without 3D annotation. However, the single view reconstruction is usually coarse and lacks instance-specific details. Recent work adapts categoryspecific models to a test-time video [30], but still does not handle objects of unknown classes.

Template-free reconstruction: Among the template-free methods, PIFu [41,42] learns to predict an implicit shape representation for clothed human reconstruction, but requires ground-truth 3D shapes to train. A3DC [39] reconstructs articulated animals from videos, but requires involved user stroke interactions. Without requiring 3D data or user interactions, NRSfM factorizes a set of 2D keypoints or point trajectories into the 3D object shape and pose in each view assuming "low-rank" shape or deformation [2, 12,19]. Recently, deep networks have been applied to learn such factorization of specific categories from 2D annotations [27,35,51]. Close to our approach, Neural Dense NRSfM (N-NRSfM) [45] learns a video-specific shape and deformation model from dense 2D point tracks. However, such methods are limited by the accuracy of 2D trajectory inputs, which is challenging to estimate in realworld sequences when large motion occurs [43,45,47].

# Approach

Problem: Given a monocular video {I t } with an object of interest (indicated by a segmentation mask {S t }), we tackle the nonrigid 3D shape and motion estimation problem, which includes estimating (1) S: the rest shape of the object, (2) D t : the time-varying articulations as well as the object root body transformations, and (3) K t : the camera intrinsics.

Overview: Figure 2 illustrates the overview of our method. Motivated by recent progress in differentiable rendering and self-supervised shape learning [23,33], we cast the nonrigid 3D shape and motion estimation problem as an analysis-by-synthesis task. Despite the under-constrained nature of this problem, we hypothesize that, by giving appropriate video measurements, a "low-rank" shape and motion can be solved up to an unknown scale. Model parameters X = {S, D t , K t } are updated (via gradient descent) to minimize the difference between the rendered output Y = f (X) and ground-truth video measurements Y * at test time (Sec. 3.1). To deal with the fundamental ambiguities in object shape, deformation and camera motion, we seek (1) a "low-rank" but expressive parameterization of deformation (Sec. 3.2), (2) rich constraints provided by optical flow and raw pixels, and (3) appropriate regularization of object shape deformation and camera motion (Sec. 3.3).

## Forward-synthesis model

We first introduce the forward synthesis model. Given a frame index t and model parameters X, we synthesize the measurements of the corresponding frame pair {t, t + 1}, including color images renderings { Ît , Ît+1 }, object silhou-ettes renderings { Ŝt , Ŝt+1 } and forward-backward optical flow renderings {û + t , û-t+1 }. Rendering pipeline: We represent object shape as a triangular mesh S = { V, C, F} with vertices V ∈ R N ×3 , vertex colors C ∈ R N ×3 and a fixed topology F ∈ R M ×3 . To model time-varying articulations D t , we have

where ∆V t is a per-vertex motion field applied to the rest vertices V , and G 0,t = R 0 T 0 t is an object root body transformation matrix (index 0 is used to differentiate from bone transformations indexed from 1 in Sec. 3.2). Finally, we apply a perspective projection K t before rasterization, where principal point (p x , p y ) is assumed to be constant and focal length f t varies over time to deal with zoom-in/out. Shaders: We render object silhouette and color images with a differentiable renderer [33]. Color images are rendered given per-vertex appearance C and constant ambient light.

To synthesize the forward flow u + t , we take surface positions V t corresponding to each pixel in frame t, compute their locations V t+1 in the next frame, then take the difference of their projections:

t Vt/P

(3)

where P (i) denotes the ith row of the projection matrix P.

## Articulation Modeling

Unknowns vs constraints: Similar to NRSfM, we analyse the number of unknowns and constraints to solve the inverse problem. Given T frames of a video, we have

which grows linearly with the number of vertices. Motivated by NRSfM [12] that uses low-rank shape and motion basis to deal with the exploding solution space, we seek an expressive but low-rank representation of shape and motion. Linear-blend skinning: Instead of modeling deformation as per-vertex motion ∆V t [18,23,31], we adopt a linearblend skinning model (LBS) [28,29] to constrain vertex motion by blending B rigid "bone" transformations

which reduces the number of parameters and makes optimization easier. Besides bone transformations, the LBS model defines a skinning weight matrix W ∈ R B×N that attaches the vertices of rest shape vertices V to the set of bones. Each vertex is transformed by linearly combining the weighted bone transformations in the object coordinate frame and then transformed to the camera coordinate frame,

where i is the vertex index, b is the bone index. Unlike A-CSM [28] that only learns articulation, we learn skinning weights and time-varying bone transformations jointly.

S1: {M=1600, B=20} S3: {M=2880, B=30} S2: {M=2240, B=25} S0: {M=1280, B=0}

Rest shape and bones 

where J b ∈ R 3 is the center of b-th Gaussian, Q b is the corresponding precision matrix that determines the orientation and radius of a Gaussian, and C is a normalization factor that ensures the probabilities of assigning a vertex to different Gaussians sum up to one. W → {Q, J} is optimized. Note that the mixture of Gaussian models not only reduces the number of parameters for skinning weights from N B to 9B, but also guarantees smoothness, the benefits of which are empirically validated in our experiments (Tab. 4). The number of shape and motion parameters now becomes

which grows linearly w.r.t. the number of frames and bones.

## Self-supervised Learning from a Video

We exploit rich supervision signals from dense optical flow and raw pixels, as well as shape and motion regularizers to further constrain the problem. Reconstruction Losses: The supervision for our analysisby-synthesis pipeline includes silhouette loss, optical flow loss, texture loss, and perceptual loss. Given a pair of rendered outputs ( Ŝt , Ît , ût ) and measurements (S t , I t , u t ), the inverse graphics loss is computed as,

where {β 1 , • • • , β 4 } are weights empirically chosen, σ t is the normalized confidence map for flow measurement, and pdist(•, •) is the perceptual distance [55] measured by an AlexNet pretrained on ImageNet. Applying L2 norm loss to optical flow is empirically better than squared L2 loss, and we hypothesize the reason being that the former is more tolerant to outliers in the observed flow fields. Shape and motion regularization: We exploit generic shape and temporal regularizers to constrain the problem. A Laplacian operator is applied to the rest mesh to enforce smooth surfaces,

Motion regularization includes an ARAP (as-rigid-aspossible) deformation term and a least deformation term.

The ARAP term encourages natural deformation [46,49],

The least deformation term encourages the deformation from the rest shape to be small [23],

which discourages arbitrarily large deformations and reduces ambiguities in joint object root body pose and articulation recovery.

Soft-symmetry constraints: To exploit the reflectional symmetry structure exhibited in common objects, we pose a soft-symmetry constraint along the symmetry plane (n * , 0) at an arbitrary frame t * . The symmetry plane is initialized from visual inspection and jointly optimized. We encourage the rest shape to be similar to its reflection,

where H = I-2n * n T * is the Householder reflection matrix, and the Chamfer distance (L cham ) is computed as bidirectional pixel-to-face distances. For the centers of Gaussian control points J, we also have

The total loss is a weighted sum of all losses with the weights empirically chosen and fixed for all experiments.

## Implementation Details

Neural basis for time-varying parameters: Instead of optimizing explicit time-varying parameters {D t , K t }, we parameterize those as predictions from a convolutional network (ResNet-18 [21]) given an input image I t ,

where one parameter is predicted for focal length, four parameters are predicted for each bone rotation parameterized by quaternion, and three numbers are predicted for each translation, adding to 1 + 7(B + 1) numbers in total at each frame. The weights are initialized with ImageNet [13] pretraining and then optimized by LASR for each test video. Intuitively, the network learns a joint basis for cameras and poses that is empirically much easier to optimize than the raw parameters (Tab. 4).

Silhouette and flow measurements Our approach assumes that a reliable segmentation of the foreground object is given, which can be manually annotated [37], or estimated using instance segmentation and tracking methods [25,56].

Our method requires reasonable optical flow estimation, which can be provided by state-of-the-art flow estimators [48,53] trained on a mixture of datasets [1]. Notably, LASR recovers from some bad flow initialization and obtains better long-term correspondences (Tab. 2).

Coarse-to-fine reconstruction We adopt a coarse-to-fine strategy to reconstruct high-quality meshes inspired by Point2Mesh [20]. S0: We first assume a rigid object and optimize the rest shape and cameras {S, G 0,t , K t } for 20 epochs. The rest shape is initialized from a subdivided icosahedron projected onto a sphere. S1-S3: We perform iso-surface extraction and re-meshing [22] to fix mesh selfintersections and long edges. After remeshing, the number of vertices and the number of bones increase, as shown in Fig. 3. The centers of Gaussian control points are initialized by running K-means on the vertices coordinates. We then jointly optimize all parameters {S, D t , K t } for 10 epochs. The above procedure is repeated three times (S1-S3).

# Experiments

Setup: Due to the difficulty of obtaining 3D ground truth for nonrigid objects in the real world, we evaluate 2D key- point transfer accuracy as a proxy of 3D reconstruction quality on real videos. We additionally evaluate 3D reconstruction accuracy on objects with ground-truth meshes.

## 2D Keypoint Transfer on Animal Videos

Dataset: We test our method on an animal video dataset, BADJA [6], which provides nine real animal videos with 2D keypoint and mask annotations, derived from the DAVIS video segmentation dataset [37] and online stock footage. It includes three videos of dogs, two videos of horsejump, and one video of camel, cow, bear as well as impala. We report quantitative results on one video per-category and show the reconstruction of the rest in the sup. mat. Metric: To approximate the accuracy of 3D shape and articulation recovery, we adopt percentage of correct keypoint transfer (PCK-T) [23,28,54] metric. Given a reference and target image pair with 2D keypoint annotations, the reference keypoint is transferred to the target image, and labeled as "correct" if the transferred keypoint is within some threshold distance d th = 0.2 |S| from the target keypoint, where |S| is the area of the ground-truth silhouette [6]. In practice, we transfer points by re-projection from the reference frame to the target frame given the articulated shape and camera pose estimations. If the back-projected keypoint lies outside the reconstructed mesh, we re-project its nearest neighbor that intersects the mesh. The accuracy is averaged over all T(T-1) pairs of frames.

Baselines: We compare with state-of-the-art methods for animal reconstruction and refer to Tab. 1 for a taxonomy. SMALST [57] is a model-based regressor trained for zebras. It takes an image as input and predicts shape, pose and texture for the SMAL [59] model. UMR [31] is a categoryspecific shape estimator trained for several categories, including birds, horses and other categories that have a large collection of annotated images. We report the performance of the horse model since the models of other animal categories are not available. A-CSM [28] learns a categoryspecific canonical surface mapping and articulations from an image collection. At test time, it takes an image as input Table 2. 2D Keypoint transfer accuracy on BADJA. (1) Modelbased regression.

(2) Category-specific reconstruction. (3) Free-form reconstruction. Methods with † do not reconstruct 3D shape. Results with * indicates the method is not designed for such category.

Best results are underlined, and bolded if reconstruct a 3D shape.

Method camel dog cows horse bear (1)  and predicts the articulation parameters of a rigged template mesh. It provides 3D templates for 27 animal categories and an articulation model for horses, which is used throughout the experiments. SMALify [6] is a model-based optimization approach that fits one of five categories (including cat, dog, horse, cow and hippo) of SMAL models to a video or a single image. We provide all the video frames with ground-truth keypoint and mask annotations. Close to our setup, N-NRSfM [45] trains a video-specific model for object shape, deformation and camera parameters from multiframe optical flow estimations [14]. Finally, we include a detection-based method, OJA [6], which trains an hourglass network to detect animal keypoints (indicated by Detector), and post-process the joint cost maps with a proposed optimal assignment algorithm. The results of PCK are taken from the paper [6] without recomputing PCK-T.

Results: Qualitative results of 3D shape reconstruction are shown in Fig. 1 and Fig. 6, where we compare with UMR, A-CSM and SMALify on the camel, bear and dog video. Quantitative results of keypoint transfer are shown in Tab. 2. Given that all 3D reconstruction baselines are categoryspecific and might not provide the exact model for some categories (such as camel), we pick up the best model or template for each animal video. Compared with 3D reconstruction baselines, LASR is better for all categories, even on the categories the baselines are trained for (e.g., LASR: 49.3 vs UMR: 32.4 on horsejump-high). Replacing the GT masks with an object segmentor, PointRend [25], the performance of LASR ('+Auto-mask' in Tab. 2) drops, but is still better than all the reconstruction baselines. Compared to detection-based methods, our accuracy is higher on the horsejump video, and close to the baseline on other videos. LASR also shows a large improvement compared to the initial optical flow (81.9% vs 47.9% for camel), especially between long-range frames as shown in Fig. 5.  

## Mesh Reconstruction on Articulated Objects

Dataset: To evaluate mesh reconstruction accuracy, we collect a video dataset of five articulated objects with groundtruth mesh and articulation, including one dancer video from AMA (Articulated Mesh Animation dataset) [50], one German shepherd video, one horse video, one eagle video and one stone golem video from TurboSquid. We also include a rigid object, Keenan's spot to evaluate performance on rigid object reconstruction and ablation for the S0 stage.

Metric: Most prior work on mesh reconstruction assumes given camera parameters. However, both the camera and the geometry are unknown in our case, which leads to ambiguities in evaluation, including scale ambiguity (exists for all monocular reconstruction) as well as the depth ambiguity (exists for weak perspective cameras as used in UMR, A-CSM, VIBE, etc.). To factorize out the unknown camera matrices, we align two meshes with a 3D similarity transformation solved by ICP. Then, the bidirectional Chamfer distance is adopted as the evaluation metric. We follow prior work [16,38] to randomly sample 10k points uniformly from the surface of predicted and ground-truth meshes, and compute the average distance between the nearest neighbor for each point in the corresponding point cloud.

Baselines: Besides A-CSM, SMALify, and UMR for animal reconstruction, we compare with SMPLify-X, VIBE, and PiFUHD for human reconstruction. SMPLify-X [36] Table 4. Ablation study with mesh reconstruction error.

# S0

ref. (1) w/o flow (2) w/o Lcan (3) w/o CNN spot 0.05 0.55 0.61 0.63 S0-S3 ref. (4) w/o LBS (5) w/o C2F (6) w/o GMM dog 0.28 0.68 0.59 0.34 is a model-based optimization method for expressive human body capture. We use the female SMPL model for the dancer sequence, and provide the keypoint inputs estimated from OpenPose [9]. VIBE [26] is a state-of-the-art modelbased video regressor for human pose and shape inference.

PIFuHD is a state-of-the-art free-form 3D shape estimator for clothed humans. It takes a single image as input and predicts an implicit shape representation, which is converted to a mesh by the marching cube algorithm. To compare with SMALify on dog and horse, we manually annotate 18 keypoints per-frame, and initialize with the corresponding shape template.

# Results

The visual comparison on human and animals are shown in Fig. 1 and Fig. 7 respectively. We report the quantitative results in Tab. 3. On the dog video, our method is better than all the baselines (0.28 vs A-CSM: 0.38), possibly because A-CSM and UMR are not trained specifically for dogs (although A-CSM uses a wolf template), and SMALify cannot reconstruct a natural 3D shape from limited keypoint and silhouette annotations. For the horse video, our method is slightly better than A-CSM, which uses a horse shape template, and outperforms other baselines. For the dancer sequence, our method is not as accurate as baseline methods (0.35 vs VIBE: 0.22), which is expected given that all baselines either use a well-designed human model, or have been trained with 3D human mesh data, while LASR does not have access to 3D human data. For the stone golem video, our method is the only one that reconstructs a meaningful shape. Although the stone golem has a similar shape to a human's, OpenPose does not detect joints correctly, leading to the failure of SMALify-X, VIBE and PiFUHD.

Qualitative results on DAVIS videos: To examine the performance on arbitrary real-world objects, we use five igure 8. Left: Ablation study on camera and rigid shape optimization (S0). Removing the optical flow loss introduces large errors in camera pose estimation and therefore the overall geometry is not recovered. Removing the canonicalization loss leads to worse camera pose estimation, and therefore the symmetric shape constraint is not correctly enforced. Finally, if we directly optimize the camera poses without using a convolutional network, it converges much slower and does not yield an ideal shape within the same iterations. Right: Ablation study on articulated shape optimization (S1-S3). We show the reconstructed articulated shape at the middle frame (t=8) from two viewpoints. Without LBS model, although the reconstruction looks plausible from the visible view, it does not recover the full geometry due to the redundant deformation parameters and lack of constraints. Without coarse-to-fine re-meshing, fine-grained details are not recovered. Replacing GMM skinning weights (9xB parameters) with an NxB matrix leads to extra limbs and tails on the reconstruction. DAVIS videos, including dance-twirl, scooter-board, soapbox, car-turn, mallard-fly, and a cat video captured by us and segmented by PointRend. The comparison with COLMAP [44], a template-free SfM-MVS pipeline, is shown in Fig. 4. More results are available in the sup. mat.

Ablation study: We investigate the effect of different design choices on the rigid "spot" and animated dog sequences. The videos are rendered into T=15 frames given ambient light and a camera rotating around the object by 90 degrees at zero elevation. Besides color images, we render silhouette and optical flow as the supervision. Results are shown in Fig. 8 and quantitative results are reported in Tab. 4. In terms of camera parameter optimization and rigid shape reconstruction (S0), we find it beneficial to use (1) optical flow as supervision signals, (2) canonicalization of symmetry plane, and (3) CNN as an implicit representation for camera parameters. For articulated shape reconstruction (S1-S3), it is critical to use (4) linear blend skin-ning, (5) coarse-to-fine re-meshing, and (6) parametric skinning model. Limitations: Empirically, LASR struggles to estimate surfaces that are not visible in any input view and fails at heavy occlusions that are missed by mask annotations. Its efficiency also needs improvement, as it takes less than one hour for rigid objects and a few hours for nonrigid shapes on a single GPU.

# Conclusion

We present LASR, a template-free approach for articulated shape reconstruction from a monocular video. LASR faithfully reconstructs individual objects from diverse categories (such as human, camel, dog, bear, etc.) without relying on category-specific shape templates, making it applicable to a wide range of scenarios. We hope that LASR will enable more progress in articulated shape reconstruction.

## Notations

A summary of the notations is listed in Tab. 6. Unit vector towards to the x axis

# Others S0

Training stage 0: optimize for {φ w (f t , G 0,t ), p x , p y , n * , V, C} S1-3

Training stage 1 to 3: optimize for {φ w (f t , G 0...B,t ), p x , p y , n * , V, C, J, Q}

