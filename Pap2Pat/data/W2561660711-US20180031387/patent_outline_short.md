# DESCRIPTION

## TECHNICAL FIELD

- define technical field of aerial vehicles

## BACKGROUND OF THE INVENTION

- motivate state estimation for micro-aerial vehicles

## SUMMARY OF THE INVENTION

- introduce novel state estimation technique

## DETAILED DESCRIPTION

- introduce state estimation technique
- describe system architecture
- explain stochastic cloning EKF state estimator
- detail long-range stereo VO implementation

### Long Range Stereo Odometry Pipeline

- motivate long-range stereo odometry
- describe pipeline structure
- generate long-range points using multi-view stereo triangulation
- generate long-range points by multi-view stereo inverse depth filtering
- perform local bundle adjustment for multi-view stereo optimization
- define long range stereo odometry pipeline
- integrate IMU motion prior into stereo VO
- describe robust multi-sensor fusion based on stochastic cloning EKF
- integrate IMU measurements into EKF state estimation
- define system state
- derive system state dynamics
- compute Jacobian matrices
- augment system state with delayed pose
- derive relative measurement model
- update EKF state using absolute and relative measurements

