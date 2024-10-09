# DESCRIPTION

## TECHNICAL FIELD

Embodiments herein generally relate to the field of aerial vehicles, and, more particularly, micro-aerial vehicles using multiple absolute and relative sensors for state estimation.

## BACKGROUND OF THE INVENTION

Light weight Micro-Aerial Vehicles (MAVs) equipped with sensors can autonomously access environments that are difficult to access for ground robots. Due to this capability, MAVs have become popular in many robot missions, e.g., structure inspection, environment mapping, reconnaissance and large-scale data gathering. Compared with ground robots, there are two main challenges for MAV autonomous navigation: (1) limited payload, power and onboard computing resources, allowing only light-weight compact sensors (like cameras) to be integrated for MAV applications; and (2) MAVs usually move with fast and aggressive six degrees of freedom (DoF) motions. Accordingly, their state estimation, environment perception and obstacle avoidance are more difficult than ground robots.

For aerial vehicles, and, in particular, for micro-aerial vehicles (MAVs), state estimation is the most critical capability for localization, autonomous obstacle avoidance, robust flight control and 3D environmental mapping. There are three main challenges for a MAV state estimator: (1) it must be able to deal with aggressive 6 degree of freedom (DoF) motion; (2) it should be robust to intermittent global positioning system (GPS) situations, and even to GPS-denied situations; and (3) it should work well both for low- and high-altitude flight.

Robust, accurate and smooth high-rate state estimation is the most critical capability to realize truly autonomous flight of MAVs. The state estimator reports the six DoF MAV position, orientation and the velocity, so the output of the estimator serves as the input for environment mapping, motion planning and trajectory-following control. Global positioning system (GPS) combined with the inertial measurement unit (IMU) state estimation technique has been widely utilized for providing MAV high-rate state information. However, applications of low-rate GPS are limited to open environments. Furthermore, GPS cannot provide accurate positioning information for MAVs, especially in terms of altitude.

As a complimentary sensor for GPS, the IMU measures tri-axis accelerations and rotation rates in the IMU body frame, and the velocity and orientation are calculated as the integral of accelerations and rotation rates over time. For low-cost commercial IMUs, the inertia integral will drift very fast without global rectification information. As a result, the integration of additional sensing is a way to further improve state estimation redundancy, accuracy and robustness.

Because of the low cost, low energy consumption and satisfactory accuracy, camera-based visual odometry (VO) is an ideal choice for providing additional measurements. Stereo visual sensors reconstruct the environment features with the metric scale from the stereo baseline, so stereo-based VO easily generates six DoF pose measurements. The performance of stereo VO highly depends on the ratio between the stereo baseline and environmental depth, namely the baseline-depth ratio. The depth standard deviation from stereo is proportional to the quadratic of depth; thus, stereo VO is limited to short range measurements. At stereo disparities lower than 10 pixels, the depth triangulation from a single stereo rig tends to follow a non-Gaussian curve with a long tail. For cases with a large baseline-depth ratio (e.g., MAV high-altitude flights), the stereo effectively degenerates to a monocular system, thus losing the capability of pose measurements.

## SUMMARY OF THE INVENTION

A novel state estimation technique is presented herein that is capable of fusing long-range stereo visual odometry (VO), GPS, barometric and inertial measurement unit (IMU) measurements. The integration is performed by an onboard processor executing software embodying the present invention.

The state estimation system utilizes long-range stereo visual odometry that can degrade to a monocular system at high altitude and integrates GPS, barometric and IMU measurements. The estimation system has two main parts: an EKF estimator that loosely fuses both absolute state measurements (for example, GPS and barometer) and the relative state measurements (for example, IMU and VO). A long-range stereo VO is designed both for low- and high-altitude odometry calculations.

The odometry takes the EKF prediction information for robust camera pose tracking and feature matching, and the stereo VO outputs serve as the relative measurements for the update of the EKF state. There are three main highlights for the system:

(1) The state estimation system utilizes both absolute state measurement sensors (GPS, barometer), the relative six DoF pose state measurement provided by VO. To deal with both absolute and relative state measurements effectively, a new stochastic cloning EKF state estimator to generate accurate and smooth state estimation both for GPS-available and GPS-denied environments is presented.

(2) A robust long-range stereo VO that works well both for low- and high-altitude cases is presented. At low altitude, the VO utilizes stereo images where the features are directly triangulated by stereo pairs with a fixed static stereo baseline. At high altitude, the ratio between the scene depth and stereo baseline becomes large, and the stereo pair effectively degenerates to a monocular system. In this situation, the additional stereo observations over time are fused by both multi-stereo triangulation and a multi-view stereo inverse depth filter for long-range feature depth generation.

(3) The EKF estimator and long-range VO coordinate to improve the robustness of the system. The IMU integral prediction information from the EKF estimator is used both for guiding image-feature matching and long-range VO optimization. Additionally, the VO is utilized as the relative measurement for the update of the EKF state.

## DETAILED DESCRIPTION

The following description is presented to enable any person skilled in the art to make and use the invention. Various modifications to the disclosed embodiments will be readily apparent to those skilled in the art, and the general principles defined herein may be applied to other embodiments and applications without departing from the scope of the present invention. Thus, the present invention is not intended to be limited to the embodiment shown. Although the invention is described in terms of micro-aerial vehicles, one of skill in the art should realize that the invention is applicable to any aerial vehicle.

In some embodiments of the invention, a technique for state estimation by fusing long-range stereo visual odometry, GPS, barometric and IMU are provided. In one embodiment of the invention, the system is realized utilizing an onboard processor running software implementing the functions of the invention however, it should be realized that any system capable of implementing the functions of the invention could be used. There are two main parts to the system.

In a first aspect of the invention, the state estimation system utilizes both absolute state measurement sensors (GPS, barometer), and relative sensors, (IMU and the six DoF pose state measurement provided by VO). A block diagram of the system is shown in FIG. 1. To incorporate both absolute and relative state measurements effectively, a new stochastic cloning EKF state estimator to generate accurate and smooth state estimation both for GPS-available and GPS-denied environments is presented.

In a second aspect of the invention, a robust long-range stereo VO that works well both for low- and high-altitude cases is provided. At low altitude, the VO utilizes stereo images, wherein features are directly triangulated by stereo pairs with a fixed static stereo baseline. At high altitude, the ratio between the scene depth and stereo baseline becomes large, and the stereo pair almost degenerates to a monocular system. In this situation, the additional stereo observations over time are fused by both multi-stereo triangulation and a multi-view stereo inverse depth filter for long-range feature depth generation.

A new stochastic cloning EKF system is presented to fuse both absolute measurements (GPS, and Barometer) and relative measurement (VO and IMU measurement) loosely for GPS-available and GPS-denied environments. To avoid the system state be overwhelmed by VO, a delayed pose and its covariance is kept in the EKF state estimation system, and the measurement Jacobian for VO measurement is derived and analyzed. As shown in FIG. 2(a-b), there are two key features for the system state after a relative VO update and a GPS (or barometer) absolute update, respectively.

FIG. 2a shows an EKF state estimation system updated by a relative measurement (e.g., VO relative measurement). After a VO relative measurement update, the updated covariance should have two important properties: (1) it should be lower than the IMU state propagation covariance, since VO information is available to the system; and (2) it must be increased compared with previous error covariance. Otherwise, the absolute measurement (GPS and barometer) will lose the ability to update the state estimation. Compared with pseudo absolute measurement VO update approaches, the covariance using delayed state cloning EKF can meet the two properties.

FIG. 2b shows an EKF state estimation system updated by absolute measurement (e.g., GPS measurement). After an absolute measurement update of the EKF state by the GPS or barometer, both the current pose covariance and the delayed pose covariance are decreased. Furthermore, the current pose covariance should be higher than the delayed pose covariance. Otherwise, the VO relative measurement will lose the ability to update the EKF state.

For IMU integral state prediction, the new uncertainty from the delayed pose to the current pose is Q. So, Q is expressed as:

FPlFT+Q=ΠFiPl(ΠFi)T+

For a relative measurement update, the VO covariance should be balanced with Q. The relationship between current pose covariance and the delayed pose covariance is given in the current state covariance. The new uncertainty Q from system covariance is calculated, as shown in FIG. 3.

The relationship between the current pose covariance and the delayed pose covariance is:

FPlFT+Q=Ps

For covariance Psl:

FPl=Psl

As a result, the new uncertainty Q is calculated as:

Q=Ps−Psl(Pl)−1PslT

On the basis of Q, the VO covariance is given by balancing the system “weight,” that is:

Rvo=kQ

where, k is a positive integer number, it can be initially set as k=1.

The Chi-square test at 0.95 is utilized to verify the compatibility of the VO relative measurement. If the test fails, that means VO covariance should be larger, and the VO covariance as can be smoothed as:

Rvo*=10

Current stereo VO algorithms are limited in short-range. In one embodiment provided herein a stereo VO implementation to make stereo VO robust for MAV long-range high-altitude applications is provided. The pipeline of the long-range stereo VO is shown in FIG. 4. It is a key-frame-based VO technique. The local map consists of a set of 3D sparse map points that is generated by selected key-frames. IMU information is integrated to improve the robustness for aggressive camera motion and repetitive texture environments. Based on the current stereo baseline-depth ratio, the VO system switches both key-frame and new map point generation strategies between stereo and monocular modes.

In short range mode (e.g., MAV low-altitude flight, as shown in FIG. 5a), the VO works in a stereo mode. For each new selected key-frame, most of the new features are directly triangulated by a stereo camera pair with a static stereo baseline. Some long-range points are triangulated using both the pseudo-baseline formed by the key-frame's poses and the static stereo baseline. In stereo mode, the environment structure is close to the camera; the image context easily changes, especially for camera rotation. Therefore, the key-frames and its features are inserted into the local map relatively densely.

In long range mode (e.g., high-altitude flight, as shown in FIG. 5b), the VO switches to monocular mode, as shown in FIG. 4. The key-frames are inserted sparsely to provide enough relative motion between the key-frames for long-range triangulation. When VO is in a long-range mode, no features will be directly triangulated by static stereo. Because most of the “short-range points” will be outliers due to an incorrect matching from a low or repetitive texture area, such as sky, cloud and trees, the new features will first be triangulated using both a dynamic pseudo baseline and a static stereo baseline (multi-view stereo triangulation). New features that cannot be triangulated by the pseudo baseline are inserted into a “candidate queue”. The feature depth will be iteratively refined by subsequently tracking stereo information with a multi-view inverse depth filter. If the inverse depth converges, the candidate feature will be added into the map and then used for camera pose tracking.

Long-range depth generation by multi-view stereo triangulation: New long-range points without depth will first be triangulated using both the pseudo-baseline and the static stereo baseline from multi-view stereo measurements. The pseudo baseline is formed by the “relative pose” between the neighboring key-frames. As shown in FIG. 6, the current left image feature is searched in the previous key-frame's left image feature set on the basis of an epipolar constraint, and for each key-frame, the matched feature pairs also have their own corresponding features in the right image. As shown in FIG. 6, between the two frames, the camera motions R and T provide a dynamic pseudo baseline, and for each stereo frame, the feature position is constrained by the static stereo baseline.

Long-range depth generation by multi-view stereo inverse depth filtering: The triangulation of the inter-key-frames is a delayed depth generation approach, as only features that can be viewed by at least two key-frames can be triangulated. For the exploration mode (e.g., the stereo moves forward), there are some new features that belong to the current key-frame. Thus, they cannot be triangulated in time. An illustrative example is shown in FIG. 7. To also apply these kinds of new features for subsequent camera pose tracking, an inverse depth filter is used for each new candidate.

FIG. 7 shows an example of the camera exploration mode. For the k-th key-frame; the dots indicate the “old” features that have been matched with the map; the triangles are the new features that await triangulation. For the (k+1)-th key-frame, triangle features can be triangulated, and some new features (red rectangle) wait for the next key-frame for triangulation. Between the (k+1)-th key-frame and the (k+2)-th key-frame, there is a set of tracking frames that also can provide useful measurements for the new features, represented by squares. All multi-view observations for the new feature are integrated using an inverse depth filter.

### Long Range Stereo Odometry Pipeline

As previously discussed, stereo depth reconstruction with a fixed static baseline is limited to a short range. For static stereo triangulation, the feature depth z is associated with the stereo matching disparity d. Suppose the stereo matching disparity has variance σd2; the triangulated depth variance σd2 by stereo is as Equation (1). It is clear that the stereo depth standard deviation σz is proportional to a quadratic of depth z. The depth error increases very quickly for the small disparity, long-range stereo measurements and, thus, cannot be utilized for VO optimization.

\(\begin{matrix}
{\sigma_{z}^{2} = {{\left( \frac{\partial z}{\partial d} \right)^{2}\sigma_{d}^{2}} = {{\frac{f_{x}^{2}B^{2}}{d^{4}}\sigma_{d}^{2}} = {\frac{z^{4}}{f_{x}^{2}B^{2}}\sigma_{d}^{2}}}}} & (1)
\end{matrix}\)

Long-range stereo depth error (bias) can be effectively reduced by introducing additional stereo observation over time, namely multi-view stereo with a dynamic pseudo baseline. The pseudo baseline between the stereo frames can be used for the triangulation of the long-range stereo points. The fixed stereo baseline can provide an absolute scale constraint. Based on this idea, a sparse feature-based stereo VO both for short- and long-range cases was developed. The pipeline of the proposed long-range stereo VO is shown in FIG. 4. It is a key-frame-based VO technique. The local map consists of a set of 3D sparse map points that is generated by selected key-frames. Furthermore, IMU information is integrated to further improve the robustness for aggressive camera motion and repetitive texture environments. Based on the current stereo baseline-depth ratio, the VO system switches both key-frame and new map point generation strategies between stereo and monocular modes:

For a short range (e.g., MAV low-altitude flight, as shown in FIG. 5(a), the VO works with a stereo mode. For each new selected key-frame, most of the new features are directly triangulated by the stereo camera pair with the static stereo baseline. For some long-range points, they are triangulated using both the pseudo-baseline formed by the key-frame's poses and the static stereo baseline. In stereo mode, the environment structure is close to the camera; the image context easily changes especially for camera rotation. Therefore, the key-frames and its features are inserted into the local map relatively densely.

For a long range (e.g., high-altitude flight, as shown in FIG. 5(b), the VO switches to monocular mode. The key-frames are inserted sparsely to provide enough relative motion between the key-frames for long-range triangulation. When VO is in a long-range mode, no features will be directly triangulated by static stereo. Because most of the “short-range points” will be outliers due to an incorrect matching from a low or repetitive texture area, such as sky, cloud and trees, instead, the new will first be triangulated using both a dynamic pseudo baseline and a static stereo baseline. The new features that cannot be triangulated by the pseudo baseline are inserted into a “candidate queue”. The feature depth will be iteratively refined by subsequently tracking stereo information with a multi-view inverse depth filter. If the inverse depth converges, the candidate feature will be added into the map and then used for camera pose tracking.

**Long-Range Point Generation Using Multi-View Stereo Triangulation**

The most critical aspect for long-range stereo is feature depth generation. For each new key-frame, its features can be classified into three groups: (1) the features have been matched with the map. (2) new features with an effective stereo depth (i.e, short-range points, with enough stereo disparity). (3) new features with small disparities (long-range points).

The new long-range points without depth will first be triangulated using both the pseudo-baseline and the static stereo baseline from multi-view stereo measurements. The pseudo baseline is formed by the “relative pose” between the neighboring key-frames. As shown in FIG. 6, the current left image feature is searched in the previous key-frame's left image feature set on the basis of an epipolar constraint, and for each key-frame, the matched feature pairs also have their own corresponding features in the right image. To make the matching more robust, the epipolar constraint between right image features is also checked. As a result, for each new map point, four matched features can be obtained between two key-frames, and the map point is triangulated as the intersection point of the four rays in the sense of least-squares.

**Long-Range Point Generation by Multi-View Stereo Inverse Depth Filtering**

The inter-key-frames' triangulation is a kind of delayed depth generation approach because only features that can be viewed by at least two key-frames can be triangulated. For the exploration mode (e.g., the stereo moves forward), there are some new features that belong to the current key-frame itself; thus, they cannot be triangulated in time. An illustrative example is shown in FIG. 7. To also apply these kinds of new features for subsequent camera pose tracking, an inverse depth filter for each new candidate was designed. For stereo, the inverse depth

\(\rho = {\frac{1}{z} = \frac{d}{f_{x}B}}\)

is proportional to disparity d; as a result, the inverse depth uncertainty is easily modeled by a Gaussian distribution:

\(\begin{matrix}
{\sigma_{\rho}^{2} = {\frac{1}{f_{x}^{2}B^{2}}\sigma_{d}^{2}}} & (2)
\end{matrix}\)

For each long-range candidate feature that belongs to the new inserted key-frame, its initial inverse depth prior is directly obtained from noisy static stereo depth triangulation, denoted as

\(\left( {\rho_{0}\frac{1}{f_{x}^{2}B^{2}}\sigma_{d}^{2}} \right)\)

During the subsequent pose tracking, each new tracking frame is utilized to filter the initial distribution

\({\left( {\rho_{0}\frac{1}{f_{x}^{2}B^{2}}\sigma_{d}^{2}} \right)},\)

and the new feature candidate will be added to the map until its inverse depth variance is smaller than a given threshold. Ideally, for each new tracking frame, two new observations can be obtained for the candidate feature: (1) the inverse depth observation distribution for the candidate is calculated from the tracking frame static stereo matching; and (2) the inverse depth observation distribution can also be obtained by the dynamic pseudo baseline formed by the motion between the current tracking frame and its reference key-frame. Therefore, the filtered inverse depth distribution can be updated by the two new observations.

Denote as the 3D coordinate of a candidate feature with z0=1 as P0=(x0, y0, 1)T in the key-frame coordinate and its corresponding matching point in the current tracking frame with z1=1 as P1=(x1, y1, 1)T. The motion from the key-frame to the current tracking frame is R10, t10=(tx, ty, tz)T, so the relationship of the two points is:

\(\begin{matrix}
{{\frac{1}{\rho_{1}}P_{1}} = {{\frac{1}{\rho_{0}}R_{10}P_{0}} + t_{10}}} & (3)
\end{matrix}\)

where ρ0 and ρ1 represent the inverse depth measurements in the current tracking frame and key-frame, respectively.

For the current tracking frame, we observe the inverse depth stereo ρ1 with its variance. Therefore, the new measured inverse depth and its variance in the key-frame coordinate are calculated by projecting the new measurement

\(\left( {\rho_{1}\frac{1}{f_{x}^{2}B^{2}}\sigma_{d}^{2}} \right)\)

to the key-frame coordinate based on the last row of Equation (3):

\(\begin{matrix}
{{\rho_{0}^{s} = \frac{\frac{1}{\rho_{1}} - t_{z}}{\left| {{R_{10}(3)}P_{0}} \right.}}{\sigma_{\rho_{0}^{s}}^{2} = {\left( \frac{\rho_{0}^{s}}{\rho_{1}} \right)^{4}\left( \frac{1}{{R_{10}(3)}P_{0}f_{x}B} \right)^{2}\sigma_{d}^{2}}}} & (4)
\end{matrix}\)

where R10 (3) represents the third row of rotation matrix R10 and σd2 is the new stereo disparity variance in the current tracking frame (set σd2=1).

The inverse depth triangulation distribution using the motion from the key-frame to the current tracking frame is also derived from Equation (3) (with the first row and the last row):

\(\begin{matrix}
{{\rho_{0}^{e} = \frac{{{R_{10}(1)}P_{0}} - {{R_{10}(3)}P_{0}x_{1}}}{{t_{z}x_{1}} - t_{x}}}{\sigma_{\rho_{0}^{e}}^{2} = {\left( \frac{{{R_{10}(3)}P_{0}t_{x}} - {{R_{10}(1)}P_{0}t_{z}}}{\left( {{t_{z}x_{1}} - t_{x}} \right)^{2}f_{x}} \right)^{2}\sigma_{u\; 1}^{2}}}} & (5)
\end{matrix}\)

where R10 (1) represents the first row of rotation matrix R10 and σu12 describes the matching error variance along the epipolar line in the current tracking frame; for experimental purposes set σu12=4. To remove the outlier inverse depth measurements, the two new inverse depth hypotheses are further tested with prior (ρ0, σρ2) using X2 compatibility testing at 0.95. After passing the test, the posterior of the inverse depth distribution for the candidate feature is updated by multiplying the prior with the new measurements (ρ02, σρ2) and (ρ0e, σρ2), that is:

(ρ0+,σρ2)=(ρ0,σρ2)(ρ0s,σρ2)(ρ0e,σρ2)  (6)

**Local Bundle Adjustment for Multi-View Stereo Optimization**

The long-range stereo points generated by either triangulation or inverse depth filtering may still be noisy. An effective approach to further improve the feature 3D reconstruction accuracy is multi-view stereo local Bundle Adjustment (BA). During the local BA, the re-projection errors for both left and right images are considered. If the map points are reconstructed with an incorrect scale, the re-projection error on the right images will be large. Accordingly, the “weak” static stereo baseline can provide an absolute scale constraint for local BA optimization. The Jacobian Jpi of the rejection residual εreproj(i) w.r.t. the map point Pi=(Xi, Yi, Zi)T is:

\(\begin{matrix}
{{Jp}_{i} = {\begin{bmatrix}
{\frac{\partial{ɛ_{reproj}(i)}}{\partial u_{i}^{l}}\frac{\partial u_{i}^{l}}{\partial P_{i}}} \\
{\frac{\partial{ɛ_{reproj}(i)}}{\partial v_{i}^{l}}\frac{\partial v_{i}^{l}}{\partial P_{i}}} \\
{\frac{\partial{ɛ_{reproj}(i)}}{\partial u_{i}^{r}}\frac{\partial u_{i}^{r}}{\partial P_{i}}}
\end{bmatrix} = {{- {\frac{1}{Z_{c}}\begin{bmatrix}
f_{x} & 0 & {{- f_{x}}\frac{X_{c}}{Z_{c}}} \\
0 & f_{y} & {{- f_{y}}\frac{Y_{c}}{Z_{c}}} \\
f_{x} & 0 & {{- f_{x}}\frac{X_{c} - B}{Z_{c}}}
\end{bmatrix}}}R}}} & (7)
\end{matrix}\)

where Pc=(Xc, Yc, Zc)T is the map point 3D coordinate in the left camera frame system. The first two rows are the residual Jacobian w.r.t. the left image and the last row is for right image. R is the camera rotation matrix. The factor graph for the long-range stereo is shown in FIG. 8, and a unary edge I4×4 is added to each key-frame pose vertex. Consequently, the local BA will mainly focus on the map point optimization, and the key-frame's pose can only be changed in a small range. The factor graph is more like a structure-only bundle adjustment since the camera pose tracking has been fused with the IMU motion information).

**IMU Tightly-Coupled Odometry Calculation**

The integration of an IMU motion prior to stereo VO has two advantages: (1) it provides a good initial motion guess for feature guided matching; (2) it gives a motion prior constraint for odometry optimization. A tightly-coupled stereo VO was designed by adding an IMU integral constraint into the 3D-2D re-projection cost non-linear optimization framework. FIG. 9 shows the factor graph for the stereo VO; the camera pose tracking w.r.t. the local map can also be seen as a motion-only bundle adjustment. In this graph, map points and reference frame pose are fixed; only the current pose is set free for optimization. The cost function is:

\(\begin{matrix}
{\left. {\left( {R,t} \right) = {{argmin}\left( {{{w\left( {{\underset{i = 1}{\sum\limits^{¨}}{{I_{i} - {\pi^{t}\left( {{P_{i};R},t} \right)}}}^{2}} +} \right.}r_{i}} - {\pi^{r}\left( {{P_{i};R},t} \right)}} \right.}^{2}} \right) + {\left( {1 - w} \right)\left. \left( {I_{imu} - \left( {R,t} \right)^{T}} \right.^{2} \right)}} & (8)
\end{matrix}\)

where the current camera pose (R, t) is calculated by minimizing a non-linear re-projection error cost function. The 3D point in the local map is Pc=(Xi, Yi, Z1); its matched 2D features in the current stereo rig are li=(uil, vil) and ri=(uir, vir) for left and right images; πl and πr are the 3D-2D re-projection model for left and right cameras, respectively. N indicates the number of matched features. Iimu denotes the IMU motion integral between the current stereo frame and the reference stereo frame. The term ∥Iimu−(R, t)T∥2 represents the IMU integral residual. ω⊂[0,1] is the weight for the IMU integral constraint.

The optimal solution for the camera pose tracking is obtained by Levenberg-Marquardt iteration:

(JxTJx+λI)ΔX=−Jxεx  (9)

where Jx and εx are the Jacobian and residual at current pose x for the stereo pose tracking system. It has the form:

\(\begin{matrix}
{J_{x} = \begin{bmatrix}
{w\left( J_{reproj} \right)} \\
{\left( {1 - w} \right)\left( I_{6 \times 6} \right)}
\end{bmatrix}} & (10) \\
{ɛ_{x} = \begin{bmatrix}
{w\left( ɛ_{reproj} \right)} \\
{\left( {1 - w} \right)\left( ɛ_{imu} \right)}
\end{bmatrix}} & (11)
\end{matrix}\)

where I6×6 is a 6×6 unit matrix. Jreproj is the Jacobian for feature re-projection error. εreproj is feature re-projection error. εimu indicates the IMU integral residual. For each map point Pi=(Xi, Yi, Zi)T, its 3D-2D reprojection error εreproj(i) is calculated as:

\(\begin{matrix}
{{ɛ_{reproj}(i)} = {{m_{i} - {\pi \left( {{P_{i};R},t} \right)}} = {m_{i} - {{\frac{1}{Z_{c}}\begin{bmatrix}
f_{x} & 0 & u_{0} \\
0 & f_{y} & v_{0}
\end{bmatrix}}\left\lbrack {{R\begin{pmatrix}
X_{i} \\
Y_{i} \\
Z_{i}
\end{pmatrix}} + t - \begin{pmatrix}
B \\
0 \\
0
\end{pmatrix}} \right\rbrack}}}} & (12)
\end{matrix}\)

Where miεli, ri indicates the measured feature coordinate for the left or the right images. Zc is the feature depth by transforming the map point to the left camera coordinate frame. B=0 for the left camera, and B=−baseline for right camera. fx, fy, u0, v0 are the stereo intrinsic parameters. For the optimization, the minimal parametrization for the camera pose R, t in Lie manifold SE(3) denoted as: X=(θx, θy, θz, tx, ty, tz,)T was used. The Jacobian Jreproj(i) for the 3D-2D re-projection error εreproj(i) w.r.t. the camera pose X is:

\(\begin{matrix}
\begin{matrix}
{{J_{reproj}(i)} = \begin{bmatrix}
{\frac{\partial{ɛ_{reproj}(i)}}{\partial u_{i}^{l}}\frac{\partial u_{i}^{l}}{\partial X}} \\
{\frac{\partial{ɛ_{reproj}(i)}}{\partial v_{i}^{l}}\frac{\partial v_{i}^{l}}{\partial X}} \\
{\frac{\partial{ɛ_{reproj}(i)}}{\partial u_{i}^{r}}\frac{\partial u_{i}^{r}}{\partial X}}
\end{bmatrix}} \\
{= \begin{bmatrix}
{f_{x}\frac{X_{c}Y_{c}}{Z_{c}^{2}}} & {{- f_{x}}\frac{X_{c}^{2} + Z_{c}^{2}}{Z_{c}^{2}}} & {{- f_{x}}\frac{Y_{c}}{Z_{c}}} & {{- f_{x}}\frac{1}{Z_{c}}} & 0 & {f_{x}\frac{X_{c}}{Z_{c}^{2}}} \\
{f_{y}\frac{Y_{c}^{2} + Z_{c}^{2}}{Z_{c}^{2}}} & {{- f_{y}}\frac{X_{c}Y_{c}}{Z_{c}^{2}}} & {{- f_{y}}\frac{X_{c}}{Z_{c}}} & 0 & {{- f_{y}}\frac{1}{Z_{c}}} & {f_{y}\frac{Y_{c}}{Z_{c}^{2}}} \\
{{f_{x}\frac{X_{c}Y_{c}}{Z_{c}^{2}}} - {B\frac{Y_{c}}{Z_{c}^{2}}}} & {{{- f_{x}}\frac{X_{c}^{2} + Z_{c}^{2}}{Z_{c}^{2}}} + {B\frac{X_{c}}{Z_{c}^{2}}}} & {{- f_{x}}\frac{Y_{c}}{Z_{c}}} & {{- f_{x}}\frac{1}{Z_{c}}} & 0 & {{f_{x}\frac{X_{c}}{Z_{c}^{2}}} - {B\frac{1}{Z_{c}^{2}}}}
\end{bmatrix}}
\end{matrix} & (13)
\end{matrix}\)

where Pc=(Xc, Yc, Zc)T is the map point 3D coordinate in the left camera frame, i.e., Pc=RPi+t. The first two rows are the residual Jacobian w.r.t. the left image, and the last row is for right image.

As a result, for N stereo features, the final system Jacobian Jx has 3N+6 rows. Additionally, based on the incremental solution ΔX=(Δθ, Δt) from Equation (9), the update of the current camera pose is expressed as:

R=exp([Δθ]x)R

R=exp([Δθ]x)t+Δt  (14)

where [Δθ], is the skew-symmetric matrix of the incremental rotation vector Δθ and exp([Δθ]x) is an exponential map.

**Robust Multi-Sensor Fusion Base on a Stochastic Cloning EKF**

An EKF state estimator for the multi-sensor loosely-coupled state estimation is provided. In the EKF, IMU measurements are utilized to propagate the system state and covariance. For the update of the EKF state, both absolute measurements (GPS and barometer) and relative state measurements (stereo VO) are fused. The coordinate systems for the EKF estimator are shown in FIG. 10. The navigation frame is a local NED (North-East-Down) frame, and the initial position is determined by the first GPS measurement. The EKF estimates the IMU body frame pose w.r.t. the navigation frame. The transformation from the camera frame to the IMU body frame is denoted as Tis, and the GPS receiver coordinate in the IMU body frame is tig.

**IMU Integration**

The IMU sensor measures the tri-axis accelerations and tri-axis angular rates w.r.t. the IMU body frame. The measurements given by the IMU are corrupted by Gaussian noise and a slowly varying bias terms, which must be removed before state estimation processing. Furthermore, the IMU accelerometers measure the force, which must be compensated by gravity. The following continuous-time model expresses the relationship between the IMU measured signals and true ones:

ωm=ω+bg+ng

am=a+RTg+ba+na  (15)

where ωm ε3 and am ε3 are the measured acceleration and angular rate, respectively. ωmε3 and am ε3 indicate the true signals. ng and na are zero-mean Gaussian (0, θg2) and (0, θa2); bg ε3 and ba ε3 are slowly varying bias terms for the accelerometer and gyroscope, respectively.

Additionally, gε3 is gravity acceleration; the rotation matrix R εSO(3) indicates the current IMU pose w.r.t. the navigation frame. The estimated angular rate and acceleration rate are denoted as {circumflex over (ω)}ε3, ûε3 respectively. Additionally, the estimated bias terms for angular rate and acceleration are {circumflex over (b)}g and {circumflex over (b)}a:

{circumflex over (ω)}=ωm−{circumflex over (b)}g,â=am−{circumflex over (b)}a  (16)

Denote δbg=bg−{circumflex over (b)}g, δba=ba−{circumflex over (b)}a as the bias errors between the true bias bg, ba and the estimated bias {circumflex over (b)}g, {circumflex over (b)}a and the slowly varying motion for bias errors are modeled as:

δbg=rg,δba=ra  (17)

where rg˜(0,σrg2) and ra˜(0, σra2) are zero-mean Gaussian.

**EKF State Definition and Jacobians**

Based on the above IMU kinematic model, the discrete IMU integral equations are:

\(\begin{matrix}
{{{{p\left( {k + 1} \right)} = {{p(k)} + {{v(k)}{dt}} + {\frac{1}{2}\hat{a}\; {dt}^{2}}}}{v_{b}\left( {k + 1} \right)} = {{v_{b}(k)} + {\left( {\hat{a} - {\left\lbrack \hat{\omega} \right\rbrack_{\times}{v_{b}(k)}}} \right){dt}}}}{{R\left( {k + 1} \right)} = {{R(k)}{\exp \left( \left\lbrack {\hat{\omega}\; {dt}} \right\rbrack_{\times} \right)}}}} & (18)
\end{matrix}\)

where p(k)ε3 indicates the three DoF position w.r.t. the navigation frame at instant k. vb(k) is the velocity defined in the IMU body frame, and r(k)εSO(3) is the rotation matrix w.r.t. the navigation frame. [{circumflex over (ω)}dt]x is a skew-symmetric matrix of the angular rate integral rotation vector {circumflex over (ω)}dt; exp([{circumflex over (ω)}dt]x) is an exponential map in the Lie manifold SO(3). dt is the IMU sampling time. Based on the IMU integral equations and bias error model, the EKF system state S is defined as:

S=(p,δθ,vb,δbg,δba)Tε15  (19)

where pε3 indicates position w.r.t. the navigation frame, δθε3 is the error rotation vector w.r.t. the IMU body frame, vb ε3 is the velocity w.r.t. the IMU body frame and δbgε3, δbaε3 are the current bias error terms. The estimated rotation matrix is defined as {circumflex over (R)}εSO(3), so the true rotation matrix R εSO(3) after the rotation error compensation is calculated by matrix right multiplication:

R={circumflex over (R)}exp([δθ]x)  (20)

where [δθ]x is skew-symmetric matrix of error rotation vector δθ.

Based on the above system state definition, the system state dynamics {dot over (S)} is derived as:

{circumflex over (p)}={circumflex over (R)}exp([δθ]x)vb

δθ=exp([δθ]x)({circumflex over (ω)}−δbg−ng)

vb=−[{circumflex over (ω)}−δbg−ng]xvb+({circumflex over (R)}exp([δθ]x))Tg+â−δba−na

δbg=rg

δba=ra  (21)

Therefore, the Jacobian matrix

\(\frac{d\; \overset{.}{S}}{dS}{\varepsilon\mathbb{R}}^{15 \times 15}\)

for the system dynamics is obtained as:

\(\begin{matrix}
{\frac{\partial\overset{.}{S}}{\partial S} = \begin{pmatrix}
0_{3 \times 3} & {- {\hat{R}\left\lbrack v_{b} \right\rbrack}_{\times}} & {\hat{R}\; {\exp \left( \left\lbrack {\delta \; \theta} \right\rbrack_{\times} \right)}} & 0_{3 \times 3} & 0_{3 \times 3} \\
0_{3 \times 3} & {- \left\lbrack {\hat{\omega} - {\delta \; b_{g}} - n_{g}} \right\rbrack_{\times}} & 0_{3 \times 3} & {- {\exp \left( \left\lbrack {\delta \; \theta} \right\rbrack_{\times} \right)}} & 0_{3 \times 3} \\
0_{3 \times 3} & \left\lbrack {{\hat{R}}^{T}g} \right\rbrack_{\times} & {- \left\lbrack {\omega - {\delta \; b_{g}} - n_{b}} \right\rbrack_{\times}} & {- \left\lbrack v_{b} \right\rbrack_{\times}} & {- I_{3 \times 3}} \\
0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} \\
0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3}
\end{pmatrix}} & (22)
\end{matrix}\)

where I3×3 denotes the 3×3 identity matrix and 03×3 denotes the 3_3 zero matrix.

The system state noise input consists of IMU measurement noise and bias error noise, that is:

W=(ng,na,rg,ra)Tε12  (23)

As a result, the Jacobian matrix

\(\frac{d\; \overset{.}{S}}{dW}{\varepsilon\mathbb{R}}^{15 \times 12}\)

w.r.t. the system noise is:

\(\begin{matrix}
{\frac{\partial\overset{.}{S}}{\partial W} = \begin{pmatrix}
0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} \\
{- I_{3 \times 3}} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} \\
{- \left\lbrack v_{b} \right\rbrack_{\times}} & {- I_{3 \times 3}} & 0_{3 \times 3} & 0_{3 \times 3} \\
0_{3 \times 3} & 0_{3 \times 3} & I_{3 \times 3} & 0_{3 \times 3} \\
0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} & I_{3 \times 3}
\end{pmatrix}} & (24)
\end{matrix}\)

Based on the relationship between the continuous-time and discrete-time systems, the final Jacobians for state covariance propagation are:

\(\begin{matrix}
{{J_{S} = {{\frac{\partial\hat{S}}{\partial S}{dt}} + I_{15 \times 15}}},{J_{W} = {\frac{\partial\hat{S}}{\partial W}{dt}}}} & (25)
\end{matrix}\)

Treatment of VO Relative State Measurement Using Delayed State Stochastic Cloning

The state estimation system provided herein utilizes both absolute state measurements (GPS provides absolute position and velocity measurement in the NED coordinate system; the barometer provides absolute state measurement for altitude) and the relative six D.O.F pose measurement (between the two stereo frames) provided by long-range stereo VO. To deal-with both absolute and relative state measurements, the system state defined in Equation (19) is further augmented by stochastic cloning of a delayed pose p1, δθ1 which is updated with the previous VO measurement, namely:

{tilde over (S)}=(ST,pl,δθ1)Tε21  (26)

During the system state propagation, the delayed pose p1, δθ1 is kept as constant; that means {dot over (p)}l=0 and {dot over (δ)}θl=0. Therefore, the Jacobians for the augmented state {dot over (S)} are:

\(\begin{matrix}
{{\overset{\sim}{J}}_{S} = {\begin{pmatrix}
J_{S} & 0_{15 \times 6} \\
0_{6 \times 15} & I_{6 \times 6}
\end{pmatrix} \in {\mathbb{R}}^{21 \times 21}}} & (27) \\
{{\overset{\sim}{J}}_{W} = {\begin{pmatrix}
J_{W} \\
0_{6 \times 12}
\end{pmatrix} \in {\mathbb{R}}^{21 \times 12}}} & (28)
\end{matrix}\)

The augmented state covariance is denoted as {tilde over (P)}(k+1|k)ε21×21. Accordingly, the covariance propagation for the state augmented system is given as:

{tilde over (P)}(k+1|k)=ÎS{tilde over (P)}(k){tilde over (J)}ST+ĴWQ(K)ĴWT  (29)

For the system initialization, the initial system state covariance is of the form:

\(\begin{matrix}
{{\overset{\sim}{P}(0)} = \begin{pmatrix}
\sum_{p}^{2} & 0 & 0 & 0 & 0 & \sum_{p}^{2} & 0 \\
0 & \sum_{\theta}^{2} & 0 & 0 & 0 & 0 & \sum_{\theta}^{2} \\
0 & 0 & \sum_{vb}^{2} & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & \sum_{bg}^{2} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & \sum_{ba}^{2} & 0 & 0 \\
\sum_{p}^{2} & 0 & 0 & 0 & 0 & \sum_{p}^{2} & 0 \\
0 & \sum_{\theta}^{2} & 0 & 0 & 0 & 0 & \sum_{\theta}^{2}
\end{pmatrix}} & (30)
\end{matrix}\)

Long-range stereo VO generates the relative six DoF motion measurement between the two visual frames. The relative measurement model is defined as:

Δp=exp(−[δθl]x)RlT(p−pl)

Δθ=log(exp(−[δθl]x)RlT{circumflex over (R)}exp([δθ]x))  (31)

where Δpε3 is a position increment from the current pose p, {circumflex over (R)} to the delay pose pl, Rl and Δθε3 is the rotation increment. RlεSO(3) is the rotation matrix for previous visual updated orientation (i.e., the delayed state orientation), and δθl indicates the error rotation vector for the delayed state. {circumflex over (R)}εSO(3) is the rotation matrix for the current orientation, and δθ is the current error rotation vector. The matrix logarithm log(RlT {circumflex over (R)}) maps the rotation matrix RlT {circumflex over (R)} to a rotation vector. For Jacobians with a relative translation Δp w.r.t. system state S:

\(\begin{matrix}
{{{{\frac{{\partial\Delta}\; p}{\partial p} = {\exp \left( {- \left\lbrack {\delta \; \theta_{l}} \right\rbrack_{\times}} \right)}}}_{{\delta \; \theta_{l}} = 0}R_{l}^{T}} = R_{l}^{T}} & (32) \\
{{{{\frac{{\partial\Delta}\; p}{\partial p_{l}} = {- {\exp \left( {- \left\lbrack {\delta \; \theta_{l}} \right\rbrack_{\times}} \right)}}}}_{{\delta \; \theta_{l}} = 0}R_{l}^{T}} = {- R_{l}^{T}}} & \; \\
{{{{\frac{{\partial\Delta}\; p}{{\partial\delta}\; \theta_{l}} = \frac{\partial{\exp \left( {- \left\lbrack {\delta \; \theta_{l}} \right\rbrack_{\times}} \right)}}{{\partial\delta}\; \theta_{l}}}}_{{\delta \; \theta_{l}} = 0}\; {R_{l}^{T}\left( {p - p_{l}} \right)}} = \left\lbrack {R_{l}^{T}\left( {p - p_{l}} \right)} \right\rbrack_{\times}} & \;
\end{matrix}\)

where the derivative

\(\frac{{\partial\Delta}\; p}{{\partial\delta}\; \theta_{l}}\)

is derived based on the first-order Taylor expansion for the exponential map at δθl=0. Additionally, the anti-commutativity rule for skew-symmetric matrix, namely: [δθl]xRlT(p−pl)=−[RlT (p−pl)]xδθl.

The Jacobians for the Δθ are computed as:

\(\begin{matrix}
{{{{{{\frac{{\partial\Delta}\; \theta}{{\partial\delta}\; \theta} = \frac{\partial{\log \left( {R_{l}^{T}\hat{R}\; {\exp \left( \left\lbrack {\delta \; \theta} \right\rbrack_{\times} \right)}} \right)}}{{\partial\delta}\; \theta}}}_{{\delta \; \theta} = 0} = {{{Adj}\left( {R_{l}^{T}\hat{R}} \right)} = {R_{l}^{T}\hat{R}}}}{\frac{{\partial\Delta}\; \theta}{{\partial\delta}\; \theta_{l}} = \frac{\partial{\log \left( {{\exp \left( {- \left\lbrack {\delta \; \theta_{l}} \right\rbrack_{\times}} \right)}R_{l}^{T}\hat{R}} \right)}}{{\partial\delta}\; \theta_{l}}}}}_{{\delta \; \theta_{l}} = 0} = {{- {{Adj}\left( I_{3 \times 3} \right)}} = {- I_{3 \times 3}}}} & (33)
\end{matrix}\)

where Adj(R) is the adjoint map in RεSO(3), and it has the property of Adj(R)=R. The derivative for the matrix logarithm is derived by the first-order approximation of Campbell-Baker-Hausdorff formula. As a result, the VO relative measurement Jacobian is expressed as:

\(\begin{matrix}
{H_{vo} = \begin{pmatrix}
R_{l}^{T} & 0_{3 \times 12} & {- R_{l}^{T}} & \left\lbrack {R_{l}^{T}\left( {p - p_{l}} \right)} \right\rbrack_{\times} \\
0_{3 \times 3} & {R_{l}^{T}\hat{R}} & 0_{3 \times 12} & {- I_{3 \times 6}}
\end{pmatrix}} & (34)
\end{matrix}\)

Denote the VO relative measurement as (Δpvo, Δθvo)T; the measurement residual is given by:

\(\begin{matrix}
{\overset{\sim}{r} = \begin{pmatrix}
{{\Delta \; p_{vo}} - {\Delta \; p}} \\
{{\Delta \; \theta_{vo}} \ominus {\Delta \; \theta}}
\end{pmatrix}} & (35)
\end{matrix}\)

where the rotational vector residual Δθv0 ⊖Δθ is defined as log(ΔR−1ΔRvo). ΔR=exp ([Δθ]x) is the predicted rotation matrix from the current state to the delayed state. Additionally, the ΔR=exp([Δθ]x) is the VO easured one.

It is worthwhile to note that, after each VO relative measurement update, the delayed portion vector of the state pl, δθl is set equal to the current updated pose p(k+1), δθ(k+1), and the state covariance matrix is updated by “cloning” the corresponding covariance blocks from the current state covariance to delayed pose covariance. To update the EKF state, the VO measurement should be transformed from the visual frame to the IMU body frame using the visual-IMU relative pose Calibration Tis; suppose the VO measurement in visual frame is Zs; its corresponding measurement in the IMU body frame is:

Zi=TisZsTis−1  (36)

The update of the EKF state is standard, that is:

K={tilde over (P)}(k+1|k)HT({tilde over (P)}(k+1|k)HT+R)−1

{tilde over (S)}(k+1)={tilde over (S)}(k)+K{tilde over (r)}  (37)

The EKF covariance update uses Joseph's form to avoid the negative definition, that is:

{tilde over (P)}(k+1)=(I−KH){tilde over (P)}(k+1|k)(I−KH)T+KRKT  (38)

**Update of EKF State Using Absolute State Measurements**

GPS provides absolute position and velocity measurement in the NED frame system; suppose the heading of the initial EKF navigation frame is aligned with the NED frame; the GPS measurement model is:

\(\begin{matrix}
{Z_{gps} = \begin{bmatrix}
{p + {\hat{R}\; {\exp \left( \left\lbrack {\delta \; \theta} \right\rbrack_{\times} \right)}t_{ig}}} \\
{\hat{R}\; {\exp \left( \left\lbrack {\delta \; \theta} \right\rbrack_{\times} \right)}\left( {v_{b} + {\left\lbrack {\hat{\omega} - {\delta \; b_{g}}} \right\rbrack_{\times}t_{ig}}} \right)}
\end{bmatrix}} & (39)
\end{matrix}\)

where tigε3 is the translation from the GPS receiver to the IMU body frame, as explained in FIG. 10. The GPS measurement Jacobian is derived as:

\(\begin{matrix}
{H_{gps} = \begin{pmatrix}
I_{3 \times 3} & {- {\hat{R}\left\lbrack t_{ig} \right\rbrack}_{\times}} & 0_{3 \times 3} & 0_{3 \times 3} & 0_{3 \times 3} \\
0_{3 \times 3} & {- {\hat{R}\left\lbrack v_{b} \right\rbrack}_{\times}} & \hat{R} & \left\lbrack t_{ig} \right\rbrack_{\times} & 0_{3 \times 3}
\end{pmatrix}} & (40)
\end{matrix}\)

Since GPS measurement in altitude has a large uncertainty, the GPS height and velocity in altitude are not utilized to update the EKF state. Only the position and velocity for north and east are kept as GPS measurements, namely Zgps=(pn, pe, vn, ve)Tε4. Consequently, the third and the sixth rows for the GPS Jacobian Hgps are also removed.

The “GPS health status”, which reports how many satellites can be seen by the receiver, are utilized to determine the current GPS measurement covariance. For bad “GPS health status”, GPS will report a large covariance. It is worth mentioning that the X2 test at 0.95 is utilized to verify the compatibility between current GPS measurement and the system predicted state. If GPS measurement “jumps” due to perturbation (e.g., multipath), the system will reject the GPS measurement automatically. In fact, the sensor measurements are firstly checked by the X2 test before they are utilized for state estimation. As a result, the EKF state estimator is robust to any sensor failures.

The barometer provides absolute altitude measurements w.r.t. the navigation frame. The navigation frame is a local NED frame, so the barometer measures the negative altitude w.r.t. the NED coordinate. As a result, the barometer measurement model is:

Zbaro=−pd  (41)

where pd denotes the z component for current position. Its Jacobian is:

Hbaro=(0 0 −1 01×18)  (42)

For the EKF implementation, a ring buffer with a 2-s time is kept to save all of the incoming sensor data. As shown in FIG. 11, when a new VO measurement arrives, its time stamp is usually not the most up to date due to the image transmission and the stereo VO calculation delay. For this case, after the update of the EKF state on the VO time stamp, the subsequent IMU integral should be re-integrated to re-predict the current state. The same processing is also carried out for GPS and barometric measurements. To further decrease the computational cost of IMU re-integration, the IMU pre-integral technique in the IMU body frame can be utilized.

The foregoing descriptions of embodiments of the invention have been presented for purposes of illustration and description only. They are not intended to be exhaustive or to limit the invention to the forms disclosed. Accordingly, many modifications and variations will be apparent to the practitioner skilled in the art. The scope of the invention as defined by the appended claims not the preceding disclosure.

