# Introduction

The development of digital society is overwhelming because it can enrich peoples' life by serving Augmented Reality, Virtual Reality, smart city, robots, autonomous driving, etc. Humans and environments are two main components for creating the digital world. Current research works always separate dynamic human motions and static environments. Actually, taking account their interactions can help improve both capture accuracy. It is a trend to directly capture the whole scene with consecutive human activities.

To capture human motions, IMU sensors are widely used and always be mounted on different parts of the human body, like arms, legs, feet, head, etc. It can capture accurate short-term motions but suffer from severe drift with the acquisition time increasing. Some methods [6, 13,39,47,48] utilize extra external RGB or RGBD cameras as a remedy to improve the accuracy, but result in limited capture space, human activities, and interactions. HPS [9] uses a headmounted camera, which looks outwards like the human eyes, to complement IMUs in global localization. Without the constraint of external cameras, it can recover the fullbody pose and register the human in large 3D scan of real scenes. However, HPS requires pre-built maps and a huge image database for self-localization.

For accurate localization and mapping [51], LiDAR is the most applicable sensor in current days, which is popular for mobile robots and autonomous vehicles. LiDAR is also extensively used for large-scale scene scans. Although there are many LiDAR-captured datasets, including indoor scenes [4,30] and large-scale outdoor scenes [7,23], they focus on scene understanding and 3D perception, ignoring accurate human poses. PedX [16] provides 3D poses of pedestrians by using SMPL [22] parameterization for joint locations of instances on third-person-view images, which is not accurate as IMUs. Furthermore, it focuses on traffic scenes and is not applicable for generating diverse 3D human motions.

Taking advantage of IMUs-based motion caption and LiDAR-based localization and scene capture, we propose Human-centered 4D Scene Capture (HSC4D) to accurately and efficiently create a dynamic digital world with consecutive human motions in indoor-outdoor scenes. Using only body-mounted sensors, HSC4D is space-free and posefree, and the interaction between humans and the environment inside is also free, which makes it possible to capture most of the human-involved real-world scenes. Compared with camera-based localization, LiDAR is more precise for global localization, which dramatically reduces the drift of IMUs, and does not need pre-built maps. IMUs can improve the accuracy of LiDAR-captured local trajectories, where the error is caused by the jitter of the body. Making use of the complement of both sensors, we propose a joint optimization to improve the performance of motion estimation and human-scene mapping by considering several physical constraints.

To facilitate further research and down-stream applications, we propose a dataset containing three large scenes (1k-5k m 2 ) with accurate dynamic human motions and locations. As Fig. 1 shows, the dataset contains diverse scenarios, like climbing gym, multi-story building, slope, etc., and challenging human activities, such as exercising, walking up/down stairs, climbing, etc. Accurate human poses and natural interactions between human and the environ-ment demonstrate the effectiveness and the generalization ability of HSC4D.

Our contributions are summarized as follows:

• Based on body-mounted IMUs and LiDAR, we propose Human-centered 4D Scene Capture (HSC4D) for creating a human-centered dynamic digital world, which is space-free, pose-free, and interaction-free. 

# Related work

2.1. IMU sensors for human pose estimation IMU sensors have been widely used to capture human motions [11,29,38,41]. However, IMU-based methods suffer from severe drift over time. To improve the pose estimation accuracy, some methods [6, 13,24,39,40] utilize extra external RGB or RGBD cameras as a remedy. Helten et al. [10] combined two RGB-D cameras with IMUs to perform local pose optimization. Hybrid-Fusion [54] has achieved more accurate motion tracking performance by combining an RGBD camera with multiple IMUs. 3DPW [39] uses a single hand-held RGB camera and IMUs to optimize human pose for a certain period of frames simultaneously. Constraints from external cameras assist in recovering more accurate 3D poses but result in limited capture space, human activities, and interactions. HPS [9] uses a first-view head-mounted camera to self-localize the 3D pose from IMUs to the scene. However, HPS requires pre-built maps and an image database for selflocalization. Instead, we use only body-mounted IMUs and LiDAR. Without any external devices' constraints and any pre-built maps, we achieve promising results for long-term human motion capture.

## Human self-localization methods

Human self-localization aims at estimating the 6-DoF of the human subject with carrying devices. The received signal strength (RSS) fingerprinting-based methodologies [1,2,18] are widely used for indoor human localization. However, these methods need external receivers and are limited to the indoor space. Some image-based methods [15, 28,42] regress locations directly from a single image with a pre-built map. Still, the scene-specific property makes them hard to generalize to unseen scenes. Some methods integrate IMU as an aid sensor [25,34] to improve accuracy. With robustness and low drift, LiDAR-based localization has been successfully applied in indoor [27,44] and outdoor [19,37,49,50] scenes. To localize the human subject, LiDAR are designed as backpacked [14, 21,46] and hand-held [3]. LiDAR-based localization systems are usually big pieces of equipment and would affect human motion. We design a lightweight hip-mounted LiDAR to rigidly connect with the human body, achieving human selflocalization in both large indoor and outdoor scenes.

## LiDAR-based mapping methods

LiDAR is currently the most applicable sensor for 3D mapping. As a pioneer, zhang et al. [51] proposed LOAM, a real-time odometry and mapping method using a LiDAR, greatly boosting the 3D mapping research. Some methods [12,20,33,43] further improve LOAM mapping for specific scenes and sensors. LeGo-LOAM [33] is a groundoptimized version, which requires to keep the LiDAR horizontal. LiDAR-based methods tend to fail when the Z-axis jitters severely. To address the drift problem and improve robustness, more sensors, such as visual sensors [32,36,52], IMU [8, 26,34], or both [5, 35,55], have been integrated in mapping task. To make the system lighter and able to work wirelessly, we propose a LiDAR-only method for localization and mapping in the scene. The joint optimization result with scene and IMU poses will further improve the LiDAR mapping result.

# System setup

## Notations and Task Description

The problem addressed in this paper is to estimate the 3D human motion with a 3D spinning LiDAR and IMUs in a large unknown scene and build a map for it, where human motion includes local 3D pose and global localization. Notations. The N frames human motion is represented as M = (T, θ, β), where T is the N × 3 translation parameter, θ is the N × 24 × 3 pose parameter, and β is the N × 10 shape parameter. We assume that β is constant during a data recording. The 3D point cloud scene is represented as S. We use right subscript k, k ∈ Z + to indicate the index of a frame. We use the Skinned Multi-Person Linear (SMPL) body model [22] 

Let us define three coordinate systems: 1) IMU coordinate system {I}: origin is at the hip joint of the first SMPL model, and X/Y /Z axis is pointing to the right/upward/forward of the human. 2) LiDAR Coordinate system {L}: origin is at the center of the LiDAR, and X/Y /Z axis is pointing to the right/forward/upward of the LiDAR. 3) Global coordinate system {W }: the first LiDAR frame's coordinate.

# Task definition.

Given a sequence of LiDAR sweep Hardware. We use a 64-beams Ouster LiDAR to acquire 3D point clouds P L k , and Noitom's inertial MoCap product PN Studio to obtain human motion M I k . The PN Studio uses 17 IMUs attached to the body limbs and a wireless receiver to acquire data. To make the LiDAR work wirelessly, we connect the LiDAR to a 9cm × 6cm × 3cm DJI Manifold2-C mini-computer and use a 24V mobile power to charge the LiDAR and the computer. To ensure a lightweight and precise capturing system, We modified all cables and designed a 10cm × 10cm L-shape bracket to mount the LiDAR package. The battery and Manifold2 are stored in a small bag on the human's back. The LiDAR is worn tightly close to the hip bone, making the origins of {I} and {L} as close as possible. Thus, we assume that LiDAR and IMUs have a rigid transformation.

The Ouster LiDAR has a 360°horizon view and a 45°v ertical view. However, due to the occlusion caused by back and swing arms, the horizon field of view is reduced, ranging from 150°to 200°. To avoid most laser points hitting the nearby ground, we tilt up the LiDAR for 30°to get a good vertical scanning view.

# Approach

We first obtain the 3D human motion output by the inertial MoCap system. Second, we estimate the ego-motion of LiDAR and build a 3D scene map S through point cloud data P I k . Then we perform a data initialization to prepare data for further optimization. Later we perform a graphbased optimization to fuse LiDAR trajectory and IMU trajectory. Finally, by combining the LiDAR data, IMUs data, and 3D scene, a joint optimization is performed to give the human motion M and an optimized scene. 

## LiDAR Localization and Mapping

Building a map using LiDAR data is challenging in this scene because the LiDAR jitters as the human walking and human body occludes the field of scanning view. By employing LiDAR-based SLAM methods [45,51], we estimate the ego-motion of LiDAR and build the 3D scene map S with P L k , k ∈ Z + in {L}. We first exact planer and edge feature points in every LiDAR scan P L k and keep updating the feature map. Similar to [45], we skip frame to frame odometry and only perform frame to map registration because the mapping process can run offline. Finally, Lidar's ego-motion T W and R W , and the scene map S are computed. The mapping function is denoted as:

## Optimization initialization

Coordinate calibration. To obtain the rigid offset from LiDAR to IMU and make all coordinate systems aligned, we perform following steps: First, the human stands as an A-pose before capture, and the human's face direction is regarded as scene's Y -axis direction. After capturing, we rotate the scene cloud Z-axis perpendicular to the starting position's ground. Last, we translate the scene to make its origin to the first SMPL model's origin on the ground. Li-DAR's ego motion T W and R W are translated and rotated as the scene does. To now, LiDAR data are calibrated to {W }. The pitch, roll, and translation of IMU are calibrated to the world coordinate. The IMU's yaw will be further refined in Sec. 4.4.

Time synchronization. Firstly, we ask the subject to jump at the starting place of every capture. Secondly, we automatically locate the peaks in both T W and T I based on their z value. Then, we can synchronize the LiDAR and IMU according to the two peaks' timestamps. Finally, we resample the IMU data (100Hz) to the same frame rate as LiDAR (20Hz).

## Graph optimization data fusion

As seen from Fig. 4, IMUs drift severely over time and fail when the scene's height change, while the LiDAR localizes correctly but jitters at local movement. To estimate a more smooth and stable trajectory, we utilize both data's advantages. Our strategy is presented as follows: 1) first mark the frame in T W that exceeds x (1.2∼2.0) times of IMU velocity and the local fitted value as the outliers, 2) treat the remained (R W , T W ) as landmarks, and then segment T I every five seconds, 3) The nodes (IMU or landmark poses) and edges (a relative transformation between two nodes) construct a graph, 4) finally perform a graph op- 

## Joint optimization

To obtain accurate and scene-natural human motion M = (T, θ), and a higher quality scene cloud S, we perform a joint optimization method by using scene S and physics constraints. Then we send T back to mapping function F as an initial value to create a new scene S opt . We use the following four constraints: the foot contact constraint L cont encouraging the human standing on the ground, the sliding constraints L sld eliminating the human walk sliding, the orientation constraint L ort from R I making the rotation smooth, and the smoothness constraint L smt making the translation smooth. The optimization is expressed as:

where λ cont , λ sld , λ ort , λ smt are coefficients of loss terms.

L is minimized with a gradient descent algorithm to iteratively optimize M (i) = (T (i) , θ (i) ), where (i) indicates the iteration. M (0) is set as (T W , θ I ), Plane detection. To improve validity of foot contact, we detect the planes near the human. We first use Cloth Simulation Filter (CSF) [53] to extract ground points S g in S. And then we search neighboring points of T W in S g . Unlike the dense mesh model, the discrete point cloud has empty areas, resulting in invalid foot contact constraints. To adress this, we use RANSAC [31] to fit planes for the neighboring points. We denote the plane fuction as p k . Foot contact constraint. The foot contact loss is defined as the distance from a stable foot to its nearest ground. Unlike HPS knowing the information about which foot is stepping on the floor, we detect the foot state based on the movements. First, we compare the left and right foot movement for every successive foot vertices in V I k = Φ(T I k , θ I k , β) from IMU. One foot is marked as a stable foot if its movement is smaller than 2cm and smaller than another foot's movement. The k-th frame's stable foot vertices index list in V j is denoted as S k and the foot contact loss L cont is written as:

is denoted as S j foot vertices in V j = Φ(M j ), which is from the motion to be optimized.

Foot sliding constraint. The foot sliding constraint reduces the motion's sliding on the ground, making the motion more natural and smooth. The sliding loss is defined as every two successive stable foot's distance:

where E(•) is the average function.

Orientation constraint. This constraint encourages the motion M to rotate as smooth as IMU and have the same orientation with the landmarks A described in Sec. 4.4. The orientation loss is written as follows:

(5)

Smooth constraint. This constraint encourages the human motion to move as smoothly as IMU motion, minimizing the difference between LiDAR and IMU sensors' translation distance. The smooth loss term is as follows:

(6)

# Experiments

This section introduces our dataset and evaluates HSC4D in large indoor-outdoor 3D scenes. The results demonstrate the effectiveness and the generalization ability of HSC4D. 

## Dataset

We propose an HSC4D dataset containing three large scenes: a rock climbing gym, a multi-story building, and an outdoor closed-loop road. The gym has a wall height of 20 meters, with a ground and climbing area size over 1200 m 2 . The building scene's indoor and outdoor area size is up to 5000 m 2 . The scenes have a diversity of heights and environments, including multi-story, slope, and staircase. The outdoor closed-loop road is 70m×65m with slope. In these scenes, captured human activities include walking, exercising, walking up/down stairs, rock climbing, speeching, etc. Since the 3D map from LiDAR lacks color information, we use a Terrestrial Laser Scanner (Trimble TX5) to scan the color scenes for better visualization. In summary, The HSC4D dataset provides 250K IMU frames (100Hz), 50k time-synchronized LiDAR frames (20Hz), our SLAM results, and colored ground truth point clouds of the scenes. 

## Comparison

The most related work to ours is HPS [9], which uses IMUs, a head-mounted camera, and NavVis M6 equipped with 6 cameras and 4 LiDARs for human-scene modeling. Besides, HPS also heavily records all images registered to the captured 3D map for localization. In contrast, We remove the tedious reliance on the pre-built map in HPS abtained using NavVis. Our approach is scene-prior-free and contributes a novel body-worn setting of LiDAR and IMUs for more practical human-scene modeling. (Tab. 1) Baselines. Since HSC4D is the first method in such scenes, there is no published baseline available to compare. For effective comparison, we name the IMU result as Baseline1 and IMU + LiDAR without any optimization as Baseline2. Global localization comparison. First, in the ground truth point clouds provided by Trimble TX5, we mark some locations on the ground as checkpoints. Then the subject steps on the checkpoint during capturing. At last, we measure the distance from the SMPL model estimated by the method to the checkpoint as global localization error. Local pose comparison. To evaluate the local pose accuracy and smoothness, we compare the foot contact loss L cont and the sliding loss L sld described in Sec. 4.5. The comparison is shown in Tab. 4.

Tab. 3 shows the localization error comparisons between our method and baselines. As the distance increases in the      Tab. 4 shows the comparison of local pose errors between our method and baselines. Baseline1's foot contact loss is much larger than other methods especially in scenes where height change. Baseline2's L sld is the largest among all methods. In the first three sequences where Baseline1 is not drift over height, Baseline2's L cont is much more larger than Baseline1. These cases indicate that LiDAR increases local errors. See from the last column, HSC4D significantly decreases L cont in all cases and achieve comparable smoothness on L sld compared to Baseline1. These comparisons reveal that HSC4D can achieve smooth results in local pose and is robust in various height diversity scenes.

## Evaluation

Quantitative evaluation. We evaluate our optimization method with ablating different loss terms by analyzing L cont and L sld . We also analyze two parameters of the optimization: the neighborhood radius r, which is used to crop the scene for foot contact constraint, and the subsequence length l of optimization. As shown in Tab. 2, without the foot contact constraint or the foot sliding constraint, L cont or L sld increases dramatically and has little impact on another term. Both L cont and L sld decrease without the smoothness constraint. However, the motion jitters more severely in 3D visualization. Overall, all loss terms are necessary to produce accurate and smooth human motion. We observe that both r and l have little impact on the result. In practice, to balance the computational resource and running time, we set l = 100. And to ensure we can detect points in the scenes, we set r = 0.6m. 

# Discussions

Limitations. First, HSC4D uses LiDAR SLAM results as the initial localization. Consequently, it is limited when Li-DAR mapping fails, such as crowded places, narrow areas, etc. Second, to avoid a large occlusion during LiDAR data capturing, some activities are limited in our system, such as sitting in a chair with a backrest, standing back against a wall. Besides, the optimization loss terms in our pipeline are hand-created. Some cases like rock climbing do not always work. It is promising to propose a more general loss term or a deep learning framework cooperating with the semantic information. Conclusions. We present a Human-centered 4D Scene capture method to accurately and efficiently create a dynamic digital world using only body-mounted IMUs and LiDAR. Our method is space-free, pose-free, and map-free. By integrating LiDARs and IMUs, our proposed joint optimization algorithm can obtain accurate global localization and smooth local poses in large scenes. Additionally, we provide a new dataset containing large scenes and diverse, challenging human motions. The experimental result demonstrates the effectiveness of HSC4D. Our work contributes to extending the motion capture to large dynamic scenes. We hope this work will foster the creation and interaction of the human-dynamic digital world in the future.

