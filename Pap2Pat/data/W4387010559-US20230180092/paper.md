# I. INTRODUCTION

With the rapid development of vehicular technology including autonomous driving, future vehicles are expected to play a role of providing various infotainment services to users as well as a simple means of transportation. Services such as voice recognition, autonomous driving, video streaming, and virtual reality/augmented reality (VR/AR) require significant computing resources and strict delay constraints, which might not be processed in on-board vehicles with limited computing and battery resources. Vehicular edge computing (VEC) [1][2][3][4] has emerged as an economical and scalable alternative to process offloaded data efficiently while providing improved quality of service (QoS) to vehicular users from anywhere and at any time at reduced costs [1].

In VEC systems, an edge server mounted on a road side unit (RSU) located nearest the vehicles can provide additional computational resources for high-complexity applications, which allows to reduce latency as well as save the energy required for offloading procedure. However, in general, the vehicular communication environment rapidly varies due to the high speed and mobility of vehicles, making it difficult to apply the traditional mobile edge computing (MEC)-based offloading method as it is. Therefore, further researches on efficient task offloading strategies suitable for the VEC systems are needed.

With the rapid spread of electric vehicles in recent years, efficient use of the vehicle's limited battery capacity has become very important. Due to the constrained energy budget of vehicles, several studies have been conducted on task offloading in VEC systems to minimize the energy consumption Fig. 1. Illustration of the task offloading in VEC systems. [2][3][4]. The authors in [2] study the energy-efficient workload offloading problem, and propose a low-complexity distributed solution based on consensus alternating direction method of multipliers, but only a single RSU is considered. In [3], a novel three-layered system, i.e., vehicular edge cloud computing (VECC), is proposed as a solution to energy conservation and computation augmentation for vehicular computing, and a deep learning-assisted energy-efficient task offloading algorithm is developed in [4]. However, [3] does not consider the partial offloading to offload the part of the task, and [4] only consider the user association without considering multiple access scheme, which can be further improved.

In this paper, we propose an energy-efficient task offloading strategy in VEC system with a one-by-one access [5] that is revealed to provide the better energy efficiency than the orthogonal access in MEC scenario considered in our previous study [6]. We jointly optimize the offloading ratio, bit allocation and offloading scheduling that minimize the total energy consumption of vehicles under a given deadline, whose solutions are verified to significantly reduce the total energy consumption of vehicles compared to the benchmarks via numerical results.

# II. SYSTEM MODEL

In this paper, we consider a VEC system including K vehicles and M RSUs as shown in Fig. 1. The RSUs are placed along the unidirectional road with J lanes, the distance between adjacent RSUs is d, and the coverage radius of each RSU is r RSU . We define M = {1, . . . , M } as the set of RSUs, where the location of RSU m in the xy-plane is calculated as p r m = (r RSU + (m -1)d, 0) for m ∈ M, with the height H. We assume that K vehicles arrive at the first RSU's coverage edge in time t k ∈ {t 1 , . . . , t K }, the set of which is defined as K = {1, . . . , K}. Also, the vehicles in the same lane have the same velocity, and the velocity of each lane j is assumed to be v j ∈ {v 1 , . . . , v J } [7].

Here, we develop the optimal offloading procedure with the aim of minimizing the total energy consumption of all vehicles. To enable the offloading of a given application of each vehicle, the following steps need to be performed. First, the vehicle k ∈ K transmits the input data to be computed at the nearest RSU via uplink transmission. Next, the RSU computes the received data. Lastly, the RSU transmits the output of application to vehicle k via downlink transmission. Frequency division duplex (FDD) is assumed, where equal bandwidth B is allocated for both uplink and downlink. Accordingly, there is no interference between uplink and downlink communication. For tractability, the time horizon T is equally divided into N frames as shown in Fig. 2, and each frame duration is ∆ with satisfying T = N ∆. The frame duration ∆ is supposed to be small enough so that the vehicle's position is approximately constant within each frame [8]. Under these circumstances, the position of the vehicle in the jth lane on the ground plane at the nth frame can be represented as p v j,n = (n∆v j , (j -1)d lane ), where j = 1, . . . , J , n ∈ N = {1, . . . , N } and d lane denotes the lane width. In each frame, the vehicle can communicate with the nearest RSU for offloading. Following [9], the channel gain between the vehicle k and the adjacent RSU at the nth frame is given by h

is the small-scale fading coefficient which follows Rayleigh distribution with unit variance, and the large-scale fading coefficient h l k [n] to reflect the path-loss is expressed as

• being the norm-2 function, m min ∈ M being the index of the closest RSU, α being the path loss exponent, and h 0 being the received power at the reference distance d = 1m for a transmission power of 1W. We assume that the channel noise is an additive white Gaussian with zero mean and power spectral density N 0 [dBm/Hz].

In this paper, we adopt an one-by-one access introduced in [5], a simple but powerful scheduling method, where only one vehicle can be served at each frame (c.f., Fig. 2(b)). Compared to a conventional orthogonal multiple access (c.f., Fig. 2(a)), where one frame is equally divided and assigned to all vehicles so that each vehicle can communicate with RSU within a single time slot of duration δ = ∆/K per each frame, the oneby-one access scheme is verified to be superior by numerical results in Sec. V. This is because the remaining vehicles except the closest vehicle to RSU keep "mute", which can save the energy. The further discussions are shown in the later part of this paper. To adopt the one-by-one scheduling mechanism, the time-varying wake-up scheduling variables are defined as

, where q = u and q = d stand for uplink and downlink, respectively. If a q k [n] = 1, the vehicle k offloads to the nearest RSU, otherwise a q k [n] = 0. The task of the vehicle k ∈ K can be quantified with the number L k of input bits, the number C k of CPU cycles per input bit for computation, and the number κ k of output bits produced by computation per input bit. The size of input data is in general much larger than the output data, i.e., 0 < κ k < 1. All tasks offloaded by vehicles need to be computed within the deadline T for the completion.

For offloading procedure, the computation energy consumption to execute the application of vehicle k with l input bits when the CPU operates at frequency f is calculated by where f [CPU cycles/s] represents the operating frequency of the processor, and γ denotes the effective switched capacitance of the processor related to the chip architecture [10].

According to standard information-theoretic arguments, when the vehicle k transmits l u k [n] bits in uplink during the nth frame of duration ∆, the communication energy consumption of the vehicle k in one-by-one access scheme is given as

It is noticed in (2) that the communication energy consumption depends on the scheduling variables a u k [n], the number of transmission bits l u k [n], and the channel condition h k [n] affected by the communication distance. As comparison, in orthogonal access [6], all the vehicles transmit the input data during the allocated slot duration δ with satisfying δ = ∆/K at each frame, which yields the communication energy consumption of the vehicle k at time slot n as

# III. ENERGY-EFFICIENT OFFLOADING WITH ONE-BY-ONE ACCESS

In this section, we formulate the problem to minimize the total energy consumption of K vehicles by jointly optimizing the bit allocation, offloading ratio and scheduling for one-byone access scheme. For reference, the total energy consumption of vehicles in local execution and offloading case with the orthogonal access [6] are briefly discussed first.

## A. Energy Consumption for Local Execution

In this part, we consider the total energy consumption of overall vehicles when all the applications are processed locally. In order to process L k bits within T seconds, the CPU frequency of vehicle k needs to be selected as (1), the total energy consumption for local execution is obtained by

, where γ v k is the effective switched capacitance of the vehicle k's processor.

## B. Minimal Energy Consumption for Orthogonal Multiple Access (Our Previous Work [6])

In our previous work [6], an orthogonal access scheme is developed for VEC systems to minimize the total energy consumption of vehicles. To this end, the joint optimization of bit allocation and offloading ratio between local execution and RSU execution is studied, where the vehicle k offloads the ratio ρ k of the input bits to the RSU and locally computes the remaining portion (1 -ρ k ) of the input bits. At the nth frame, we denote l u k [n] as the number of uplink bits transmitted from the vehicle k to the RSU, l c k [n] as the number of bits computed for the task of the vehicle k at the RSU, and l d k [n] as the number of downlink bits transmitted from the RSU to the vehicle k. Since, in the orthogonal access, the offloading process is analyzed in frame-by-frame manner [6], [8], the energy consumption of the vehicle is expressed as

To minimize the total energy consumption of the vehicle, the joint optimization problem of bit allocation and offloading ratio can be formulated as (8) in [6], whose solutions are detailed in [6].

## C. Minimal Energy Consumption for One-by-one Access

We now formulate the optimization problem when adopting the one-by-one access scheme [5] for VEC systems, and then propose Algorithm 1 to resolve the formulated problem. Herein, we consider not only the bit allocation and the offloading ratio between local execution and RSU execution, but also the scheduling variables for one-by-one access. To this end, the total energy consumption of vehicles is given by

, ρ k } as the set of optimization variables, and therefore the optimization problem for one-by-one access is formulated as

where the constraints (4b) and (4c) guarantee that the achievable rates in uplink and downlink are larger than or equal to the number of transmitted bits in the corresponding links. Also, an equality constraint (4f) is for scheduling of one-by-one access to satisfy that the only one vehicle can communicate with RSU in each frame.

Since the problem ( 4) is non-convex and mixedinteger optimization problem which cannot be directly solved by using standard convex optimization techniques. To address the non-convexity, we adopt the corresponding Lagrange dual problem of (4). Let us define

as the set of Lagrange dual variables corresponding to (4b)-(4e), (4g) and (4h), respectively. Then, the Lagrangian of problem ( 4) is defined as (5), where

and

Given Y, the optimal offloading ratio ρ opt k can be obtained by applying Karush-Kuhn-Tucker (KKT) conditions. The Lagrange dual function of problem ( 4) is given by

In order to minimize dual function L(Z, Y), the stationary point ρ opt k to make the derivative of L with respect to ρ k equal to zero can be obtained as

where [c] b a = min{max{a, c}, b}. In a similar way, to minimize

, the optimal scheduling variables a u,opt k

[n] and a d,opt k

[n] for k ∈ K and n ∈ N are calculated by the following theorem.

Theorem 1: Given Y and l u k [n] for all k ∈ K and n ∈ Ñ , the optimal scheduling variables for Lagrange dual function are obtained as [n] and ρ opt k , the optimization problem ( 4) is simplified as minimize

Since the problem ( 11) is convex, we can solve this problem using standard convex optimization solver such as CVX [11].

After that, we can solve the dual problem as follows: max

Algorithm 1 Joint optimization of bit allocation, offloading ratio and scheduling for one-by-one access in VEC systems. Since the dual problem ( 12) is concave with respect to Y, the subgradient method is adopted so that converging the global point can be guaranteed [12]. Accordingly, the dual variables in each iteration are given by

where the superscript 'z' represents the iteration index, [c] + = max{0, c} and {π i } 7 i=1 are step sizes. The overall process is shown in Algorithm 1.

# IV. SIMULATION RESULTS

In this section, the simulation results are presented to evaluate the performance of our proposed Algorithm 1 in VEC systems. For simulations, we consider the VEC system including a one-way road with three lanes. Each vehicle randomly  arrives at the starting point, and it is assumed that the task deadline of all vehicles is equal to T . Also, Rayleigh fading is considered for small-scale fading, and 3GPP path loss model [13] is used for large-scale fading. The remaining parameters are shown in Table 1. As a benchmark, the three schemes are considered such as (i) local execution scheme, where all tasks are computed locally, (ii) orthogonal access scheme [6], where the same time slot is allocated to each vehicle, (iii) one-byone access scheme with an equal bit allocation that transmits the same number of bits to the uplink and downlink in each frame, without optimizing the bit allocation. Fig. 3 shows the total energy consumption of vehicles as a function of deadline T on a logarithmic scale, where the number of vehicles is set to 3, and the input bits of each vehicle are set to 75Mbits. It is observed that the proposed oneby-one access scheme consumes the least energy compared to other benchmarks. Furthermore, energy consumption of one-by-one access dramatically decreases around 10s, as it approaches the first RSU. This is because as the distance between the RSU and the vehicle gets closer, the vehicle can offload the larger amount of tasks to the RSU so as to consume the less communication energy. On the other hand, in orthogonal access, where the frame duration is divided and equally allocated for each vehicle, although the vehicle is close to the RSU, it cannot fully utilize the entire duration, yielding the higher energy consumption than one-by-one access scheme. Similarly, in the case of one-by-one with equal bit allocation, since the same amount of bits needs to be offloaded in each frame regardless of channel conditions, the vehicular energy consumption decreases when the vehicle approaches the RSU, and increases again when the vehicle moves away from the RSU. Additionally, at the deadline larger than 14s, the vehicular energy consumption is even higher than that of local execution, which shows that the optimal bit allocation plays an important role in the aspect of energy efficiency.

In Fig. 4, we compare the total energy consumption as a function of the number of input bits, where K = 3 and T = 25s. In local execution, since the computation energy consumption is proportional to the cube of the input bits, the energy consumption increases significantly as the number of input bits increases. Both orthogonal and one-by-one access scheme are designed to offload the most of tasks, resulting in the sizable energy reduction compared to local execution. In particular, in the case of one-by-one access, where the entire frame duration can be allocated to the vehicle closest to the RSU, it is robust against the large-scale input bits. Fig. 5 compares the total energy consumption as a function of the number of vehicles under T = 25s. In local execution, the vehicular energy consumption is highest as the number of vehicles increases, since the total energy consumption of vehicles is obtained by summing all the computational energy consumption of each vehicle. Also, in orthogonal access scheme, the available time duration at each vehicle becomes shorter with the increase on the number of vehicles, which results in the larger energy consumption. On the other hand, the one-by-one access scheme achieves the lowest energy consumption as the number of vehicles increases.

# V. CONCLUSION

In this paper, an energy-efficient task offloading scheme for VEC system with one-by-one access is proposed. To minimize the total energy consumption of vehicles, we jointly optimize the offloading ratio, bit allocation, and offloading scheduling under a given deadline. The non-convex and mixed-integer optimization problem is formulated and solved by adopting Lagrange dual problem. Via simulations, we verify that the proposed energy-efficient offloading scheme can significantly reduce the total energy consumption of vehicles compared to the benchmarks. As a future work, a scenario considering traditional non-orthogonal multiple access (NOMA) and ratesplitting multiple access (RSMA) can be studied.

