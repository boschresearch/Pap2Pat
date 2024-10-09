# DESCRIPTION

## TECHNICAL FIELD

- define technical field of aerial vehicles

## BACKGROUND OF THE INVENTION

- introduce micro-aerial vehicles
- motivate state estimation
- describe challenges of state estimation
- discuss limitations of GPS
- discuss limitations of IMU
- discuss limitations of stereo visual odometry

## SUMMARY OF THE INVENTION

- introduce novel state estimation technique
- describe system architecture
- highlight stochastic cloning EKF state estimator
- highlight robust long-range stereo VO

## DETAILED DESCRIPTION

- introduce invention scope
- motivate aerial vehicle application
- describe system overview
- introduce state estimation technique
- describe system block diagram
- motivate stochastic cloning EKF
- describe VO system for low-altitude cases
- describe VO system for high-altitude cases
- introduce delayed pose and covariance
- derive measurement Jacobian for VO
- describe EKF state estimation system update
- analyze covariance properties
- introduce IMU integral state prediction
- balance VO covariance with Q
- describe Chi-square test for VO measurement
- introduce long-range stereo VO pipeline
- describe key-frame-based VO technique
- summarize long-range depth generation approaches

### Long Range Stereo Odometry Pipeline

- introduce limitations of static stereo triangulation
- derive depth variance equation
- motivate multi-view stereo with dynamic pseudo baseline
- describe sparse feature-based stereo VO pipeline
- introduce key-frame-based VO technique
- explain local map generation
- integrate IMU information
- switch between stereo and monocular modes
- describe stereo mode operation
- describe monocular mode operation
- introduce long-range point generation using multi-view stereo triangulation
- classify features into three groups
- triangulate long-range points using pseudo-baseline and static stereo baseline
- introduce long-range point generation by multi-view stereo inverse depth filtering
- model inverse depth uncertainty
- design inverse depth filter for each new candidate
- update filtered inverse depth distribution
- introduce local bundle adjustment for multi-view stereo optimization
- consider re-projection errors for both left and right images
- derive Jacobian of rejection residual w.r.t. map point
- define long range stereo odometry pipeline
- introduce IMU tightly-coupled odometry calculation
- derive cost function for stereo VO
- formulate Levenberg-Marquardt iteration
- define Jacobian and residual for stereo pose tracking
- calculate 3D-2D reprojection error
- derive Jacobian for 3D-2D reprojection error
- introduce robust multi-sensor fusion based on stochastic cloning EKF
- define EKF state estimator for multi-sensor loosely-coupled state estimation
- describe IMU integration
- model IMU measurements with Gaussian noise and bias terms
- estimate angular rate and acceleration rate
- model bias errors for angular rate and acceleration
- define discrete IMU integral equations
- derive EKF state definition
- formulate Jacobians for EKF state
- describe EKF update process
- conclude EKF state estimation
- define system state
- derive system state dynamics
- obtain Jacobian matrix for system dynamics
- obtain Jacobian matrix for system noise
- derive final Jacobians for state covariance propagation
- augment system state with delayed pose
- derive Jacobians for augmented state
- define augmented state covariance
- derive covariance propagation for augmented system
- define initial system state covariance
- define relative measurement model
- derive Jacobians for relative translation
- derive Jacobians for relative rotation
- define VO relative measurement Jacobian
- define measurement residual
- update EKF state using VO measurement
- update delayed pose and covariance
- define GPS measurement model
- derive GPS measurement Jacobian
- define barometer measurement model
- derive barometer measurement Jacobian
- implement EKF using ring buffer
- re-integrate IMU data for VO measurement
- re-integrate IMU data for GPS and barometric measurements
- utilize IMU pre-integral technique
- conclude EKF implementation

