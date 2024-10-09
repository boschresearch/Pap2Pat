# Introduction

In image-guided radiation therapy (IGRT), 3D Cone Beam CT (CBCT) is extensively applied to check patient positioning before a radiation beam is delivered. However 3D-CBCT is not capable to capture a dynamic moving target and reflect the respiration motion during radiation therapy. Nowadays SBRT (Stereotactic Body Radiotherapy) has been applied widely for lung cancer treatment due to its better treatment effect compared with conventional IMRT (Intensity Modulated Radiation Therapy). At the SBRT treatment stage for lung cancer cases, the patient usually will be performed with a 3D-CBCT to check positioning before SBRT beam on. However in this process, the physician cannot check again if the patient respiration matches with that of the 4D-CT, especially for the GTV region. To compensate for the deficiency, 4D-CBCT was proposed for accurate on board motion tracking. There are different categories of existed 4D-CBCT reconstruction schemes. The first category is employed to increase the acquired projection number under each gantry angle by performing multiple gantry rotation or reducing the gantry rotation speed (1, 2). But it prolongs the imaging time and increases the imaging dose. The second 4D-CBCT category is the non-local mean/Total Variation (TV)-based algorithms (3–5). The TV method supplies a qualified noise suppressed image but it over-smoothed tiny structures and further deteriorate the image quality of the low contrast region. The third category is the full data initialization-based reconstruction such as the McKinnon-Bates (MKB) algorithm (6, 7) and the prior image constrained compressed sensing (PICCS)-based algorithm (7, 8). However, the residual motion will transmit artifacts from the initial reconstruction to the final images. And the fourth category is the low-rank models (9) and the framelet (5, 10) based reconstruction. However, the low rank method cannot fully realize the time differentiation, and both of these two methods are lack of clinical supporting results feasibility check. In recent years, the Deformable Vector Field (DVF)-based 4D-CBCT image reconstruction algorithm has shown an advantage for high-quality 4D-CBCT reconstruction (11–14). However, most of those methods assume the lung moves along an uniform path and ignored the lung's non-average local motion (e.g. sliding motion). This assumption is not true since sliding motion exists widely at the interfaces between moving organs such as the lung and the chest wall's interface. A few studies have tried to model the sliding motion via lung boundary segmentation (12). But its clinical translation is hindered due to its ineluctable requirement of lung boundary half automatic segmentation.

In this study, we develop a fully automatic sliding motion compensated 4D-CBCT reconstruction algorithm in a fundamentally different way by using bilateral filtering. This algorithm performs bilateral filtering on the DVF during the motion optimization process. Bilateral filtering has been previously utilized for estimating sliding motion for 4D-CT (15). But here we adapt this technique to 4D-CBCT, which is a more challenging scenario. Accurate 4D-DVF estimation from 4D-CBCT imaging geometry, especially for sliding motion extraction, is more difficult than that of 4D-CT. This is not only because the acquired CBCT projections are contaminated with serious scatters but also because the available projection number per phase are quite limited due to conventional 1 min clinical scanning protocol. We estimate the 4D-DVF by matching the measured projection of each target phase with the deformed phase 0%'s Digital Reconstructed Radiography (DRR). Meantime we incorporate bilateral filtering into the 4D-DVF estimation process for sliding motion modeling. A non-linear conjugate gradient optimizer is used for this optimization process.

Our results indicate that the bilateral filtering-based motion modeling and reconstruction is capable of better sliding motion modeling. For algorithm validation, we applied a non-uniform rotational B-spline that is based on a cardiac-torso (NCAT) phantom. Subsequently, four patient data with IRB approval were used to perform an initial pilot clinical validation.

# Methods And Materials

## The Bilateral Filtering Based Simultaneous 4D-Cbct Image Reconstruction Algorithm

We first make a short review of the original simultaneous motion compensated reconstruction algorithm. There are two steps in the algorithm: 1) reconstruct a high quality phase 0% image using all acquired projections with motion compensated SART (Simultaneous Algebraic Reconstruction Technique, mSART). The motion compensated SART is mathematically described in equation (1). Then step 2): estimate the 4D-DVF by matching each phase's measured projection with the DRR (Digitally Reconstructed Radiography) of the deformed phase 0%. These two steps are performed in an interleaved fashion to allow a converged energy function curve. The loss function was designed into a symmetrical form to ensure an inverse consistent DVF solution, see equation (2). Once the 4D-DVF optimized solution were obtained it will be used to deform the final iterative reconstructed high quality phase 0% image to get the final high quality 4D-CBCT[see equation (6)]. Mathematically, the above mentioned steps can be expressed as follow:

Let \(p^{t} = \left( {p_{1}^{t},p_{2}^{t},\ldots p_{I}^{t}} \right)\)  denote the log-transformed 4D-CBCT projection (i.e., line integral) from phase t, and \(\mu^{t} = \left( {\mu_{1}^{t},\mu_{2}^{t},\ldots\mu_{J}^{t}} \right)\)  denote the attenuation coefficients of phase t image, the modified mSART is given by (1):

where k is the iteration step, j is the voxel index of phase 0%, n is the voxel index of phase t. ain is the intersection length of projection ray i with voxel n, which is obtained by a ray-tracing technique (16). \(d_{\text{jn}}^{t\rightarrow 0}\)  denotes the element of the inverse DVF that deforms phase t to phase 0. The initial image \(\mu_{j}^{0,(0)}\)  is first reconstructed by the TV minimization (17) reconstruction to achieve a noise suppressed initial 0% phase 0%. For projection matching, an inverse consistent DVF estimation is applied by designing a symmetric energy function:

f1 and f2 denote the symmetric energy function. 0 stands for phase 0%, t stands for any other phase t. A is the projection matrix. x stands for the voxel of image μ0 or μt.v0→t denotes the forward DVF element for each voxel, and vt→0 denotes the inverse DVF element for each voxel. \(\left\| {\text{pt} - A\mu^{0}\left( {x + v^{0\rightarrow t}} \right)} \right\|_{l_{2}}^{2}\)  and \(\left\| {p^{0} - A\mu^{t}\left( {x + v^{t\rightarrow 0}} \right)} \right\|_{l_{2}}^{2}\)  are the data fidelity terms of the inverse consistent loss function. φ(v0→t) and φ(vt→0) are the corresponding regularization terms. β controls the trade-off between the data fidelity term and smoothing regularization term φ(v). If the lung is supposed to have an isotropic motion mode, φ(v) will be designed by:

where (∂vi)/(∂xj) denotes the difference between neighboring voxels for each DVF component along three directions. Index “i” stands for the DVF component along x, y, and z direction. Index “j” stands for one of three Cartesian coordinates; “vi” stands for the DVF element along each Cartesian coordinate direction; “xj” stands for each image voxel along each Cartesian coordinate direction.

We take sliding motion into account and re-designed the bilateral filtering based regularization term:

with

Gx is the Gaussian kernel on the spatial domain with the variance \(\sigma_{x}^{2}\) ; Gμ is another image domain-based Gaussian kernel with the variance \(\sigma_{\mu}^{2}\) ; and Gv is the DVF domain Gaussian kernel with the variance \(\sigma_{x}^{2}\) . The index “i”, “j”, “vi”, and “xj” have the same meaning that mentioned in equation (3). Meantime “xj” is also the central voxel in each bilateral filter kernel. “yj” represents the neighborhood voxel surround xj, with a max number of N. k is the surround voxel index of “yj”. For implementation, the gradient ∇φ(v)|v is calculated within the 3x3x3 neighborhood that surrounds each voxel of interest. A nonlinear conjugate gradient optimizer was used to estimate the final DVF solution. We also give the gradient of φ(v):

When high quality phase 0% \(\mu_{j}^{2,(k)}\)  is finally obtained, each other 4D phase image \(\mu_{n}^{t,(k)}\)  can be obtained by deforming \(\mu_{j}^{0,(k)}\)  with the final optimized 4D-DVFs. See equation below:

To accelerate the energy function's convergence, we need to generate the initial 4D-DVF to start the optimization process. The measured CBCT projections are initially sorted into 4D for an initial 4D-CBCT TV reconstruction (3). A Demons registration algorithm (18) was then employed to obtain the 4D-DVF initials between each phase and the 0% phase.

The pseudo code of the algorithm is given as follows:

The loss function curve was draw with the DVF optimization iteration. And the optimization stops if the curve converges. For calculation acceleration, the code is run on a GPU card (Geforce GTX 980, NVIDA, Santa Clara, CA) for parallel computation. The data processing time will be discussed in the discussion part.

The algorithm work flow chart is given below (Figure 1):

## Algorithm Validation Experiments Design

### The Digital Ncat Phantom Experiment

The NCAT phantom was first used to evaluate the performance of the bilateral filtering based sliding motion estimation algorithm. 10 breathing phase of 4D NCAT were simulated with respiration period of 4 s. The maximum diaphragm motion along Superior-Interior (SI) is 20 mm and the maximum chest Anterior-Posterior (AP) motion is 12 mm. The projections of 10 phases with 20 views per phase were used for the DVF estimation and 4D-CBCT reconstruction. The phantom image size is 256 x 256 x 150 with a voxel size of 1x1x1 mm3. The projection size is 300 x 240 x 20 view per phase with projection voxel size of 1x1 mm2. We compared the bilateral filtering reconstruction results with the lung segmentation based (12) algorithm, the original simultaneous reconstruction algorithm (11) and the ground truth reference for quantitative evaluation. For motion tracking comparison, the 4D NCAT motion trajectory along z-direction are extracted from the heart edge in the coronal view slice for quantitative evaluation.

### Pilot Patient Data Evaluation

Four sets of lung cancer patient data were used to perform an initial pilot clinical validation of the bilateral filtering-based 4D-CBCT reconstruction algorithm. Using an IRB approved protocol (MD Anderson with IRB# 00-202), the patients were scanned in full fan mode for 4–6 min to acquire approximately 2000 projections. The acquired projections were then sorted by phase binning into 10 phases. In this manner, the number of average projections per phase was approximately 200, and TV minimization reconstruction was applied to reconstruct the high-quality 4D-CBCT that can serve as the patient reference for clinical results quantification. To simulate an approximate 1-min CBCT data we down-sampled the acquired 4D full projections until the average projection number per phase decreased to ~40. We performed the original simultaneous reconstruction and the bilateral filtering-based sliding constrained reconstruction for quantitative comparisons with the ground truth. Here we need to clarify that although the down-sampling helps to mimic a 1-min CBCT, one still cannot getting a real 1-min CBCT data. Even with the same number of projection per phase, 6-min CBCT scan is still better than 1-min case because the projections are further spread out in 6-min case. Down-sampling only helps to mimic an approximate 1-min CBCT case for algorithm testing.

## Selection Of Σx, Σμ, And Σv

The selection criteria of σx, σμ, and σv will dramatically influence the final DVF solution. It's relatively easy to determine σx, σμ. Excessively large or small σx (spatial smoothness) will either over-smooth the image content or prevent it from sufficiently capturing the local sparse features. The voxel size is 1 mm3 for the NCAT phantom data and 2 mm3 for the patient data. Hence the reasonable spatial variance σx should not be smaller than 2 mm. With several round testing, we determined σx = 3 mm gives the best results for the reconstructed images both for the NCAT phantom and the patient data. The image will be over-smoothed if σx is larger than 3 mm. σμ controls the image intensity domain smoothness between the interface of the lung part and the chest wall. We set it equal to the difference between the lung tissue and the surrounding chest cavity tissue to retain the nature intensity transit from the chest cavity boundary to the lung inner part. For the NCAT phantom data, σμ = 0.03 mm-1 gives the best results, and for the patient pilot data, σμ = 0.02 mm-1 gives the best results. The most difficult part is to determine σv for extracting the sliding motion. Theoretically, σv should be larger than the DVF difference between two points at a distance smaller than σx. However at the pleural cavity region σv should be smaller than the DVF intensity difference (15) between the two points. To avoid motion over-segmentation, we set that only sharp discontinuities (e.g., large sliding motion) can be captured. In our former work (12), we compared the results obtained from the original simultaneous reconstruction method and the ground truth and discovered that the sliding motion estimation error at the heart edge site is approximately 7.5 mm. Hence, we suggest that 10 mm is a relatively large amount of sliding motion. With this assumption, we tested several σv values and determined that σv = 2.5 mm gives reasonable results for NCAT data.

For the patient pilot study, we also compared the original simultaneous reconstruction results with the high-quality patient reference. We discovered that the rib position has a maximum motion error of approximately 5~6 mm at the pleural cavity site. Hence, we suggest that 6 mm is a relatively large sliding motion amount. With this assumption, we establish 2 mm of σv for the patient pilot test and obtain the desired results.

## Evaluation Criteria

### Tumor Motion Accuracy

The tumor motion trajectory was extracted from the reconstructed images and the ground truth. The root mean square error (RMSE) of the estimated tumor position is analyzed to quantify motion estimation accuracy with sliding motion constraint.

where \({Pos}_{ph}^{R}\)  denotes the estimated image feature point position for the phth phase and \({Pos}_{ph}^{T}\)  denotes the corresponding position from the ground truth. MaxE is defined as the maximum error of the tumor position extracted from all 9 phases.

### Dice Coefficient

After the final 4D reconstruction is finished, we used the dice coefficient to measure the segmented lung boundary contours to see whether sliding motion compensated result have more contour similarity compared with the truth reference. The segmentation is performed via ITK snap software tool. Let A be the contour area obtained from result with or without sliding motion compensation, and B is the contour from the truth reference. The dice coefficient s given by:

In our study, we use the voxel number within the organ contour as a surrogate of the exact area.

### Relative Reconstruction Error

The relative error (RE) between the reconstructed 4D-CBCT with sliding modeling and the ground truth/reference was used to quantify the image reconstruction accuracy by defining

where uT(x) stands for the phantom ground truth, uR(x) is the reconstructed image.

### Parameter Sensitivity Σv For Ncat Phantom Experiment

Since the bilateral filtering kernels have multiple parameters (e.g., σx, σμ, and σv), a sensitivity analysis is necessary to clarify how these parameters influence the 4D-DVF estimation. The spatial domain parameter σx and the voxel intensity domain parameter σμ's selection criteria are simple and clearly decided. However, the most challenging parameter is σv. We performed a NCAT phantom test of the 4D-CBCT reconstruction algorithm with different σv values, which range from 1.0 to 5.0 per 0.5 step increase. The σx was set to 3 mm, and σμ was set to 0.03 mm-1. Since digital phantom data already eliminate contamination resources such as scattering and noise, the obtained reconstruction error is mainly caused by σv.

# Results

## Ncat Phantom Results

Figure 2 shows the 40% phase reconstructed images obtained from the original reconstruction (e.g. without sliding motion modeling), the segmentation based reconstruction, and the bilateral filtering based reconstruction. Figure 2A shows the sagittal view of the reconstructed 40% phase obtained from the original reconstruction; Figure 2B shows the same sagittal slice reconstructed from the segmentation based reconstruction; Figure 2C shows the sagittal slice reconstructed from the bilateral filtering reconstruction; Figure 2D shows the phantom ground truth; the white arrow labels the rib, which can be seen clearly in the bilateral filtering based reconstructed image and the ground truth. The rib is also partially visible in the segmentation based reconstructed image. But it is hardly visible in the original reconstructed image (e.g. without sliding motion modeling). The white arrows clearly labeled the rib comparison. Figures 2E–H are the regions of interest (ROI), where sliding motion exists at the heart edge and the vein site. The vein (indicated by a yellow dotted line) is more accurately reconstructed (e.g., vein length has been better reconstructed, see the white arrows) with bilateral filtering and the segmentation based reconstruction. Figures 2I–L show the rib position reconstruction differences between the original reconstruction, the segmentation based reconstruction, the bilateral filtering reconstruction and the ground truth. In Figures 2J, K, rib top edges 1 and 2 match the ground truth with Figure 2L compared with that of the original reconstruction in Figure 2I.

### Ncat Phantom Motion Trajectory Result

The 4D NCAT motion trajectory along the z-direction are extracted from the heart edge in the coronal view slice [refer to the dotted line position in Figure 2F]. The dotted line position is detected from a ROI binary image by establishing a uniform threshold for each phase. The detected dotted line positions are used to plot the motion trajectory. Figure 3 shows the 4D motion trajectory extracted from the original reconstruction without sliding motion modeling, the segmentation based sliding motion modeling, the bilateral filtering based sliding motion modeling, and the motion ground truth. The figure indicates that the trajectory extracted both with bilateral filtering and segmentation-based sliding motion modeling matches better with the ground truth. We consider each of the trajectory's motion amplitude for the RMSE calculation and determine that the trajectory's RMSE and MaxE are 0.796 mm and 1.02 mm for the bilateral filtering-based results. Meantime the segmentation based RMSE/MaxE are quite close to that of the bilateral filtering based results. The original reconstruction result’s RMSE and MaxE are 2.704 mm and 4.08 mm, respectively.

### Dice Coefficient

We extract the 4D lung boundaries (by ITK-SNAP software) from the original simultaneous reconstruction, the segmentation based and the bilateral filtering reconstruction. The 4D Dice coefficients extracted from the NCAT phantom experiment with each different motion modeling scheme are summarized in Table 1. Both of the segmentation based and the bilateral filtering-based Dice coefficients are consistently larger than that from the original simultaneous reconstruction. The results indicate that the lung boundary can be more accurately segmented with segmentation based and bilateral filtering based motion estimation compared with that of the original reconstruction.

### Parameter Sensitivity Σv For Ncat Phantom Experiment Analysis

The correspondence between the relative reconstruction error and σv is plotted in Figure 4. This figure indicates that the minimum relative reconstruction error can be obtained with σv = 2.5 mm.

### Profiles For Ncat Result

We plot the profiles for the NCAT phantom result in Figure 5. The profile is plotted by the yellow dot line in Figure 2C. Red line stands for the phantom profile reference (e.g. Truth); blue line stands for the bilateral filtering based profile, brown line stands for the profile obtained from the segmentation based reconstruction, and the green line stands for the original reconstruction based profile. The sharp peak in red line stands for the rib that the dot line comes across. The profile shows that the blue line keeps the same correspondence with the red line while the green line totally missed the rib.

## Patient Pilot Study

Corresponding patient results are shown in Figures 6–9.

Figure 6 shows the sagittal view of the reconstruction comparison of the 1st patient. Figure 6A shows the original reconstructed result; Figure 6B shows the bilateral filtering based result; Figure 6C shows the reference image reconstructed by TV reconstruction (3) using the fully sampled projections. The white arrow shows a tumor closely attached to the thoracic wall, and a small cavity exists between the tumor and the wall. The yellow arrow shows a side effect of bilateral filtering. And it will be discussed later in the discussion part. The corresponding reconstruction slice via TV and FDK are also listed in Figures 6D, E, respectively.

Figure 7 shows the reconstructed coronal view results for the 2nd patient. Figure 7A depicts the original simultaneous reconstructed image. Figure 7B shows the bilateral filtering reconstructed results. Figure 7C provides the patient reference. Figures 7D–F displayed the zoomed ROIs [refer to the ROI box in Figure 7A] from Figures 7A–C, respectively.

Figure 8 shows the 3rd patient reconstruction results. This patient case doesn't have visible sliding motion because the tumor located at the apex of lung. Hence the imaging ROI(Region of Interest) cannot observe visible sliding motion. The box ROI shows a bone structure comparison.

Figure 9 shows the 4th patient reconstruction results. The arrows labeled a fibrous structure comparison.

We summarized each patient's ROI based RE values for FDK, TV, the original simultaneous reconstruction, and the bilateral filtering based reconstruction methods in Table 2.

# Discussion And Conclusions

## Results Discussion On The Clinical Results

In Figure 6, compared with reference Figure 6C the arrow labeled small cavity in Figure 6A has been blurred more dramatically than that in Figure 6B. Meantime the image content structures in Figure 6D have been over-smoothed by TV reconstruction; and in Figure 6E all the image suffered from serious noise contamination by FDK reconstruction. The quantitative comparison in Table 2 indicate that bilateral filtering achieve the minimum RE value, which further confirms the above subjective description of the image.

In Figure 7, the lung-to-heart boundary (indicated by the arrow) in Figure 7E is more visible than that in Figure 7D compared with reference Figure 7F. And the quantitative comparison result in Table 2 also indicates the same trend.

The patient in Figure 8 is a special case. The tumor in this patient is very close to the apex of the lung. So the imaging region is set to the apex region. However sliding motion can hardly be seen in the region. And we didn't find any motion difference between Figures 8A, B. But as bilateral filtering is capable to smooth the image while keeping sharp edges, we found in the box region the bone structures have been better reconstructed with bilateral filtering with a sharper edge (e.g. see Figure 8B).

In Figure 9, we found the fibrous structure (labeled by the arrow) has been reconstructed clearer and sharper with bilateral filtering (e.g. Figure 9B) than that from the original reconstruction (e.g. Figure 9A) compared with the patient reference (e.g. Figure 9C).

## Σv Sensitivity Analysis For Fibrous Texture Over-Smoothing

We discovered an over-smoothing side effect for the fibrous texture in Figure 6, which is labeled by the yellow arrow. We made a σv sensitivity analysis to check whether this effect is caused by the DVF domain's filter kernel. We set σv to 2, 3, 4, and 5 mm to perform the 4D-CBCT reconstruction. We also removed the DVF domain sub-kernel (e.g., to set the DVF domain kernel to 1) from the entire bilateral filtering kernel to perform the reconstruction and eliminate the influence of σv. The corresponding reconstructed slices of the target phases are shown in Figure 10. The results indicate that regardless of how σv changes, the arrow-labeled fibrous structure is always over-smoothed. Hence, this over-smoothing effect is not directly caused by the DVF domain sub-filter kernel. This indicates that the over-smoothing can be caused by the conventional bilateral filter's texture smoothing feature. The bilateral filtering kernel that we employed is a 3D kernel in a cubic 3x3x3 voxel region. We checked the smoothed texture's adjacent slice region and found that the adjacent local region contains dense tiny fibrous textures (refer to Figure 10H). The 3D bilateral filter smoothed the texture not only in the adjacent slice (Figure 10I) but also spread it to the current slice (Figures 10A–D). This over-smoothing effect occurred where the tiny fibrous textures are located very close to each other. If we want to remove this excessive smoothing effect, one possible solution is to rely on more projections within this phase. More projections will supply additional information for better reconstruction. We can also increase the image resolution by using a smaller voxel size for reconstruction.

## Reconstruction Results Comparison Between Bilateral Filtering-Based Scheme Vs. Lung Segmentation-Based Scheme

To make a parallel performance comparison between bilateral filtering-based reconstruction and segmentation-based reconstruction, we performed an NCAT phantom experiment. The relative reconstruction error of the bilateral filtering reconstruction is 7.3% and 7.4% for the segmentation based reconstruction. However, differences in some image slices remain. In Figure 2 we already show that the rib can be better reconstructed with bilateral filtering reconstruction than that of segmentation result. Figure 11 also shows the coronal views obtained from bilateral filtering-based construction, segmentation-based reconstruction, and original simultaneous reconstructions. Both of these two algorithms have corrected the rib positions to match with the ground truth (rib #1 and #2's top edges). The vein length (represented by the yellow circles) has also been corrected by these two algorithms compared with the ground truth. The vein has even been reconstructed more clearly by the bilateral filtering reconstruction. The bilateral filtering-based scheme obtained better reconstruction results compared with the segmentation based reconstruction.

## Reconstructed Image Super-Positioned With The Solved Dvfs

To illustrate the DVF difference between the bilateral filtering-based reconstruction and the original simultaneous reconstruction, we super-positioned their reconstructed images with their corresponding DVFs. As the sliding motion mainly occurs at the interface between the lung and the chest wall, we only focus on this zoomed local region of interest to determine the DVF differences. Figure 12 shows the lung-chest wall ROI. Figure 12A is the ROI from the bilateral filtering-based result; Figure 12B is the corresponding ROI from the original reconstruction. The red dotted line gives the DVF flow trend. The bilateral filtering-based DVF flow (refer to red line in Figure 12A) drops downward from the rib side to the lung part. For the original case, the DVF flow slides straight from the rib side to the lung side. This DVF flow difference directly causes the rib position differences in the final reconstructed images. Hence, this finding reveals that bilateral filtering effectively corrected the rib position compared with the original reconstruction.

## Calculation Time

The convergence of the bilateral filtering reconstruction is similar to the original reconstruction where 200 total iterations in the DVF estimation are adequate to achieve good convergence. The computation time for one

DVF optimization iteration is 18 s for the presented algorithm to reconstruct an image with size of 200 x 200 x 150. Currently, DVFs for each phase were estimated sequentially and we partially implemented the algorithm on a GPU card (Geforce GTX 980, NVIDA, Santa Clara, CA). Only the forward projection for each view was parallel accelerated on GPU. To further speed up the calculation, possible strategy includes: 1) full GPU implementation and 2) running DVF estimation for different phases in a parallel fashion on multiple GPU cards. Recently a deep leaning based 4D-CBCT motion estimation algorithm (19, 20), was developed. In this paper a CNN model is constructed to predict a PCA (Principle Component Analysis) based DVF motion modeling. The PCA eigenvectors and the corresponding PCA coefficients are predicted to obtain the real time updated 4D-DVF. The training dataset is a pre-built projection based datasets with more than 1 × 106 simulated projections from the patient 4D-CT. Their reported calculation time cost is around 30~40 min for network training with a Intel Core i7-5960X CPU, 32 GB memory and NIVIDIA GTX 1080 Ti GPU. The advantage of this algorithm is that it realized real-time motion tracking. But one disadvantage is that the training data (e.g. the simulated projections that contains respiration motion) comes from 4D-CT but not the on board 4D-CBCT. Hence once the patient respiration mode changes between the 4D-CT scanning stage and the 4D-CBCT scanning stage the predicted real time 4D-CBCT will not reflect the true respiration at the treatment stage. As the 4D-DVF estimation principle of this algorithm is fundamentally different compared with our method. So it is not fair to make a parallel comparison between our results and their algorithms. Obviously deep learning based real-time 4D-CBCT is very promising for supplying quality 4D-CBCT. Once the patient on-board respiration projection dataset were built, the deep learning network will possibly be able to predict accurate on-board 4D-CBCT. This will be our next step research focus.

## Limitation Of The Patient Number For Statistical Testing

Another limitation of the current study is that the evaluation studies were performed on a limited number of patients. The CBCT scans with long acquisition times were performed under a previous institutional review board protocol. The limited number of study participants does not allow statistical testing. More patient data and statistical analysis are needed to further validate the clinical value of this method.

## How The Proposed Method Supports Clinical Translation In Igrt

Our proposed method does not need any hardware modification and employs the conventional 1 min clinical scanning protocol for imaging data acquisition. The algorithm offers physicians with high quality 4D-CBCT and it helps checking whether: 1) a patient’s respiration retains the same mode compared with his/her 4D-CT; and 2) if the tumor shape/motion mode changes obviously. This further helps the physician decide if it is safe to trigger on the SBRT beam for treatment.

# Conclusion

In this work, we proposed a bilateral filtering-based fully automatic sliding motion compensated 4D-CBCT reconstruction scheme. Both the digital NCAT phantom experiment and the pilot clinical validation demonstrated that this scheme is an effective simultaneous high-quality 4D-CBCT image reconstruction algorithm. The experiment also showed that the bilateral filtering-based algorithm outperforms the segmentation-based sliding motion modeling algorithm for 4D-CBCT reconstruction. The algorithm is a prospective 4D-CBCT tool for clinical translation in image-guided radiation therapy.

# Data Availability Statement

The data analyzed in this study is subject to the following licenses/restrictions: The dataset were from MD Anderson, and the author got the permission to use the data for this paper. The author has acknowledged the permission in the Acknowledgments. Requests to access these datasets should be directed to Prof. Tinsu Pan, tpan@mdanderson.org.

# Ethics Statement

The studies involving human participants were reviewed and approved by MD Anderson with IRB# 00-202. The patients/participants provided their written informed consent to participate in this study.

# Author Contributions

JD wrote the manuscript and developed most of the algorithm codes. TY is in charge of the patient data analysis and part of the manuscript revision before submission; WS developed part of the algorithm codes; HX discussed the algorithm details and revised the revision manuscript; XC and YS do the proofreading for revision. LL analyzed the patient study results; YL helped with allocating manuscript time from clinical duty of the authors; DC and TZ revised the manuscript. All authors contributed to the article and approved the submitted version.

# Funding

This work is supported by a grant from Varian Medical System, a grant from the Chongqing Municipal Human Resources and Social Security Bureau (cx2018147), a grant from Chongqing Natural Science Foundation (cstc2020jcyj-msxm2928), a seed grant from the First Affiliated Hospital of Chongqing Medical University (PYJJ2019-208); a Key Medical Projects of Jiangsu Commission of Health (No. ZDB2020022); a Key Project of Chongqing Yuzhong District Science and Technology (No.20190101); The National Natural Science Foudation of China (No. 61971078, 61501070); and The Science and Technology Foundation of Chongqing Education Commission (No. CQUT20181124).

# Conflict Of Interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

