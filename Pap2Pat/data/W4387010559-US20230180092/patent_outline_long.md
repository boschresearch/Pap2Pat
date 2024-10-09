# DESCRIPTION

## BACKGROUND

### 1. Field of the Invention

- relate to vehicle edge computing technology

### 2. Description of the Related Art

- describe limitations of vehicle terminal
- introduce vehicle edge computing as solution

## SUMMARY

- provide data offloading method and apparatus
- increase efficiency of offloading for vehicle edge computing
- transmit input data to RSU closest to vehicle
- receive output data processed by RSU closest to vehicle
- compare location of vehicle with locations of candidate RSUs
- store data on locations of candidate RSUs
- calculate location of vehicle
- select RSU closest to vehicle
- transmit input data to RSU closest to vehicle through uplink
- receive output data processed by RSU closest to vehicle through downlink
- control input data transmission and output data reception
- identify lane to which vehicle belongs
- use FDD scheme for communication

## DETAILED DESCRIPTION

- describe environment of vehicle edge computing system
- assume K vehicles travel along one-way road with J lanes
- assume m RSUs disposed along one-way road with J lanes
- describe distance between RSUs and coverage radius of each RSU
- represent location of mth RSU using Equation 1
- assume K vehicles depart from start time point at different times
- assume vehicles present in same lane move at same speed
- represent speed of vehicles in each lane
- allocate at least one time frame for offloading task
- perform one-to-one connection with selected RSU during at least one time frame
- describe length of each time frame
- assume location of vehicle does not change during each time frame
- represent location of vehicle present in jth lane in nth time frame using Equation 2
- describe data offloading apparatus for vehicle edge computing
- include storage unit, controller, and communication unit
- store data on locations of RSUs in storage unit
- implement radio access technologies and communication protocols in communication unit
- control input data transmission and output data reception through communication unit
- compare location of vehicle with locations of RSUs
- identify RSU closest to vehicle
- control input data transmission to RSU closest to vehicle through uplink
- control output data reception from RSU closest to vehicle through downlink
- identify lane to which vehicle belongs
- calculate location of vehicle using Equation 2
- compare location of vehicle with locations of RSUs
- select RSU closest to vehicle
- describe data offloading method for vehicle edge computing
- transmit input data to RSU closest to vehicle through uplink
- receive output data processed by RSU closest to vehicle through downlink
- compare location of vehicle with locations of RSUs
- identify RSU closest to vehicle
- reduce energy consumption of vehicle

