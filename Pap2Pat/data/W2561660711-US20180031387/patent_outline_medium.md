# DESCRIPTION

## TECHNICAL FIELD

- define technical field of aerial vehicles

## BACKGROUND OF THE INVENTION

- motivate MAV applications
- describe challenges of MAV navigation
- summarize importance of state estimation

## SUMMARY OF THE INVENTION

- introduce novel state estimation technique
- outline system components and functionality

## DETAILED DESCRIPTION

- introduce invention scope
- motivate state estimation technique
- describe system architecture
- explain stochastic cloning EKF state estimator
- detail long-range stereo VO implementation
- illustrate key-frame-based VO technique
- explain short-range and long-range VO modes
- describe long-range depth generation methods
- illustrate inverse depth filtering

### Long Range Stereo Odometry Pipeline

- motivate long-range stereo odometry
- derive stereo depth error equation
- introduce multi-view stereo with dynamic pseudo baseline
- describe key-frame-based VO technique
- explain stereo mode for short-range points
- explain monocular mode for long-range points
- classify features for long-range point generation
- triangulate long-range points using multi-view stereo
- filter long-range points using inverse depth filtering
- optimize multi-view stereo using local bundle adjustment
- define long range stereo odometry pipeline
- integrate IMU motion prior into stereo VO
- formulate cost function for stereo VO
- derive optimal solution for camera pose tracking
- calculate 3D-2D reprojection error
- define robust multi-sensor fusion based on stochastic cloning EKF
- integrate IMU measurements into EKF state estimator
- model IMU measurements with Gaussian noise and bias terms
- define EKF state and Jacobians for discrete IMU integral equations
- define system state
- derive system state dynamics
- compute Jacobian matrix for system dynamics
- compute Jacobian matrix for system noise
- define augmented system state
- compute Jacobians for augmented system state
- define relative measurement model
- compute Jacobians for relative measurement
- define measurement residual
- update EKF state using relative measurement
- update EKF state using absolute state measurements
- define GPS measurement model
- define barometer measurement model

