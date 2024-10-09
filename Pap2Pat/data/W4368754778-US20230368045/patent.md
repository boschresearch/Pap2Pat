# DESCRIPTION

## CROSS REFERENCE

The present application claims the benefit under 35 U.S.C. § 119 of German Patent Application No. DE 10 2022 204 723.0 filed on May 13, 2022, which is expressly incorporated herein by reference in its entirety.

## FIELD

The present invention relates to a computer-implemented method for predicting a behavior of agents in a dynamic system with a multiplicity of interacting agents.

## BACKGROUND INFORMATION

Possibilities of predicting behavior in such systems are described in Charlie Tang and Russ Salakhutdinov, “Multiple Futures Prediction,” 2019, NeurIPS and in Sergio Casas and Cole Gulino and Simon Suo and Katie Luo and Renjie Liao and Raquel Urtasun, “Implicit Latent Variable Model for Scene-Consistent Motion Forecasting,” 2020 ECCV.

## SUMMARY

By the computer-implemented method and device according to the present invention, precise prediction of a behavior of agents is achieved at low cost with regard to the required computing resources.

According to an example embodiment of the present invention, a method for predicting the behavior of agents in a dynamic system with a multiplicity of interacting agents depending on the latent state thereof provides that for a plurality of components and for a plurality of time points up to a prediction time point, a value of a first moment of a first distribution, which models the latent state of the agents, is determined for each component, wherein a value of a second moment of the first distribution is determined, wherein an expected value for a first moment of a second distribution at the prediction time point is determined for each component depending on the value of the first moment of the first distribution at the prediction time point and depending on the value of the second moment of the first distribution at the prediction time point, wherein the second distribution models the behavior of the agents depending on the latent state thereof, wherein the expected value for the first moment of the second distribution defines a first moment of a third distribution, wherein a second moment of the third distribution is determined for each component, wherein a sum, in particular a sum weighted with at least one weight, of the third distributions of the component is determined, and wherein the prediction of the behavior is determined depending on the sum.

Preferably, according to an example embodiment of the present invention, it is provided that the value of the first moment of the first distribution is determined depending on a value of the first moment of the first distribution for a time point preceding the time point and on an expected value for a deterministic change of the first moment of the first distribution, and/or that the value of the second moment of the first distribution for the time point is determined depending on a value of the second moment of the first distribution for a time point preceding the time point and on a covariance of the deterministic change and on an expected value for a stochastic change of the second moment of the first distribution. This efficiently recursively determines the respective value.

The value of the second moment of the first distribution for the time point is preferably determined depending on the value of the second moment of the first distribution for the preceding time point and on the covariance of the deterministic change and on a covariance of the latent state at the preceding time point with the deterministic change and on a transpose of the covariance of the latent state at the preceding time point with the deterministic change and on the expected value for the stochastic change. This efficiently recursively determines the value.

Preferably, according to an example embodiment of the present invention, the expected value for the first moment of the second distribution is determined depending on the value of the first moment of the first distribution at the prediction time point. This efficiently determines the expected value.

Preferably, according to an example embodiment of the present invention, a covariance of the first moment of the second distribution is determined for each component depending on the value of the first moment of the second distribution at the prediction time point, wherein an expected value for the second moment of the second distribution at the prediction time point is determined for each component depending on a latent state at the prediction time point, wherein the second moment of the third distribution is determined for each component depending on the covariance of the first moment of the second distribution and on the expected value for the second moment of the second distribution at the prediction time point. The method can thus be performed particularly efficiently.

Preferably, according to an example embodiment of the present invention, a context variable is determined, which comprises an association, which associates at least one agent with another agent to be considered for predicting the behavior of this agent, and/or which characterizes a history of the dynamic system, wherein the first moment of the first distribution is determined depending on the context variable, and/or wherein the second moment of the first distribution is determined depending on the context variable, and/or wherein the expected value for the first moment is determined depending on the context variable, and/or wherein the first moment of the third distribution is determined depending on the context variable, and/or wherein the second moment of the third distribution is determined depending on the context variable, and/or wherein the at least one weight is determined for at least one component depending on the context variable. A neighborhood and/or a history of the agents is thereby considered.

According to an example embodiment of the present invention, the history is preferably determined depending on an observed behavior of the at least one agent, in particular a behavior which comprises the agent's position or movement, wherein the agent's position or movement is in particular acquired using a receiver for a satellite-based position determination system, or wherein at least one digital image is acquired, in particular using a sensor for digital images, preferably a camera, a LiDAR sensor, ultrasonic sensor, movement sensor, thermal imaging detector, and/or radar sensor, and the agent's position or movement is determined depending on at least one digital image, or wherein a signal is acquired using a speaker for receiving audible sound and the agent's position or movement is determined depending on the signal.

It may be provided that the context variable comprises a matrix, whose rows each represent one of the agents and whose columns each represent one of the agents, wherein at least one value, in particular a binary value, of an element of the matrix identified by a row and a column is determined and specifies whether or not the agent identified by the row is to be considered for the prediction for the agent identified by the column, or wherein at least one value, in particular a binary value, of an element of the matrix identified by a row and a column is determined and specifies whether or not the agent identified by the column is to be considered for the prediction for the agent identified by the row. The matrix represents a neighborhood to be considered. As a result, the calculation considers the most relevant agents in particular. As a result, the best possible prediction is calculated particularly efficiently.

Preferably, according to an example embodiment of the present invention, the first moment and the second moment of the first distribution are determined in iterations, wherein for a first one of the iterations for each component, a value of the first moment of the first distribution and a value of the second moment of the first distribution are determined, which depends on the context variable. The history is thereby considered particularly efficiently.

Preferably, according to an example embodiment of the present invention, it is provided that, for the prediction, latent states of an agent are modeled independently of one another and latent states of different agents are modeled independently of one another, or latent states of an agent are modeled independently of one another and corresponding elements of latent states of different agents are modeled dependently on one another, or different elements of a latent state of an agent are modeled dependently on one another and latent states of different agents are modeled independently of one another. This makes the calculation very efficient.

Preferably, according to an example embodiment of the present invention, at least one agent, in particular a computer-controlled machine, in particular a robot, preferably a vehicle, a household appliance, a driven machine, a manufacturing machine, a personal assistant, or an access control system is controlled depending on the prediction. This control is particularly robust.

The at least one agent may be an existing real object in the physical world.

According to an example embodiment of the present invention, the device comprises at least one processor and at least one memory, which are designed to perform the method. This device has advantages corresponding to those of the method.

According to an example embodiment of the present invention, a system comprises at least one agent, in particular a computer-controlled machine, in particular a robot, preferably a vehicle, a household appliance, a driven machine, a manufacturing machine, a personal assistant, or an access control system, wherein the agent or the system comprises the device, and wherein the device is designed to control the agent depending on the prediction. This system has advantages corresponding to those of the method.

According to an example embodiment of the present invention, a computer program comprises computer-readable instructions that, when executed by a computer, cause the method to run. This computer program has advantages corresponding to those of the method.

Further advantageous embodiments can be taken from the following description and the figures.

## DETAILED DESCRIPTION OF EXAMPLE EMBODIMENTS

FIG. 1 schematically shows a device 100 for predicting a behavior of agents 102 in a dynamic system 104 with a multiplicity of interacting agents 102. The dynamic system 104 in the example is a physical system, in particular a technical system. The agents 102 may be physical systems, in particular technical systems. The agents 102 may be an existing real objects in the physical world. The device 100 comprises at least one processor 106 and at least one memory 108. The device 100 is designed to perform a below described method for predicting the behavior of the agents 102 in the dynamic system 104. The device 100 optionally comprises an interface 110. The agents 102 optionally comprise an interface 112. The device 100 and the agents 102 are optionally designed to communicate via their interfaces, for example in order to transmit information about a behavior of the agents 102 from the agents 102 to the device 100 or to send information about a prediction of the behavior from the device 100 to the agents 102. A sensor system 114 may be provided that is designed to acquire information about the behavior of the agents 102 in the dynamic system 104. The sensor system 114 may be designed to measure a physical property of the agents 102. The agents 102 are optionally designed to provide information about their own behavior or about the behavior of other agents 102. For example, the information about their own behavior is acquired using the sensor system 114. For example, the sensor system 114 is arranged in one or more of the agents 102 and designed to acquire the information about the own behavior of the respective agent 102 and/or the behavior of the other agents 102. The sensor system 114 is, for example, designed to acquire a position or movement of the agents 102. The sensor system 114 may comprise a receiver for a satellite-based position determination system, e.g., a global positioning system, or a sensor for digital images, such as a camera, a LiDAR sensor, ultrasonic sensor, movement sensor, thermal imaging detector, and/or radar sensor. The sensor system 114 is, for example, designed to acquire a position or movement of the agents 102. The sensor system 114 may comprise a speaker for receiving audible sound and for generating audio signals. It may be provided that the sensor system 114 is arranged in an infrastructure 116 and is at least intermittently connected via a communication link 118 to the interface 110 of the device 100 in which the agents 102 can move. Instead of the sensor system 114, it may be provided that the data comprises information about the agents 102, in particular data structured in a graph.

The agents 102 are optionally designed to determine their own behavior depending on the prediction of the behavior of the other agents 102. For example, the agents 102 each comprise an actuator 120 that is designed to influence the behavior of the respective agent 102 depending on the prediction. It may also be provided that the device 100 is designed, instead of transmitting the prediction to the agents 102, to determine a control command for at least one agent 102 depending on the prediction and to transmit the control command to the agent(s) 102 to be controlled. In this case, the actuator 120 is designed to execute the control command. It may be provided that the device 100 is integrated in one or more of the agents 102.

Likewise provided is a computer program that contains instructions that, when executed by a computer, cause this method to run. For example, the at least one processor 102 executes the computer program.

FIG. 2 shows a behavior of agents 102 in an exemplary system 104. In the example, the behavior of the agents 102 is observed, wherein FIG. 2 shows trajectories on which the agents 102 have actually moved according to an observation of their behavior from a start time point of the observation to an end time point of the observation.

For example, the dynamic system 104 is a technical system in which the agents 102 are computer-controlled machines, e.g., robots, such as vehicles, household appliances, driven machines, manufacturing machines, personal assistants, or access control systems.

The dynamic system 104 may also be another system. For example, the dynamic system 104 is a molecular dynamics in which the agents 102 are atoms or molecules whose movements are being predicted. For example, the dynamic system is a game, such as a soccer, basketball, or American football game, in which the agents are people or game equipment, e.g., a ball, whose movements are being predicted.

The dynamic system 104 in the example is a roundabout 202. In the example, the roundabout 202 has a first entry 204, a second entry 206, a third entry 208, and a fourth entry 210. In the example, the roundabout 202 has a first exit 212, a second exit 214, a third exit 216, and a fourth exit 218. The agents 102 in the example include vehicles. It may be provided that the agents 102 include pedestrians. From the start time point, a first vehicle moves on a first observed trajectory 220 from the first entry 204 in the roundabout 202 and, at the end time point, is located in the roundabout 202 in the area of the second exit 214. From the start time point, a second vehicle moves on a second observed trajectory 222 from the area of the second exit 214 in the roundabout 202, exits the roundabout 202 via the third exit 216 and, at the end time point, is located outside the roundabout 202. From the start time point, a third vehicle moves on a third observed trajectory 224 from the second entry 206 in the roundabout 202 and, at the end time point, is located in the roundabout 202 in the area of the third exit 216. From the start time point, a fourth vehicle moves on a fourth observed trajectory 226 from an area in the roundabout 202 between the second exit 214 and the second entry 206 in the roundabout 202 and, at the end time point, is located in the fourth exit 218. From the start time point, a fifth vehicle moves on a fifth observed trajectory 228 from an area in the roundabout 202 between the third exit 208 and the fourth entry 218 in the roundabout 202 and, at the end time point, is located in the first exit 212. From the start time point, a sixth vehicle moves on a sixth observed trajectory 230 in the area of the fourth entry 210 until the end time point.

FIG. 3 shows a prediction of the behavior of the agents 102 in the dynamic system 104 using the example of the roundabout 202.

From the start time point, the first vehicle moves on the first observed trajectory 220 until an observation end time point. In the example, the first vehicle does not move but is located in the first entry 204 until the observation end time point. A first predicted trajectory 320 between the observation end time point and a prediction end time point is determined for the first vehicle. According to the prediction, the first vehicle moves from the first entry 204 in the roundabout 202 and, at the end time point, is located in the roundabout 202 in the area of the second exit 214.

From the start time point until the observation end time point, the second vehicle moves on the second observed trajectory 222 to an area in the roundabout 202 between the second entry 206 and the third exit 216. This portion of the second observed trajectory 222 is shown with dashed lines in FIG. 2 and in FIG. 3. A second predicted trajectory 322 between the observation end time point and the prediction end time point is determined for the second vehicle. According to the prediction, the second vehicle moves from the area in the roundabout 202 between the second entry 206 and the third exit 216 in the roundabout 202, exits the roundabout 202 via the third exit 216 and, at the end time point, is located outside the roundabout 202.

From the start time point until the observation end time point, the third vehicle moves on the third observed trajectory 224. In the example, the third vehicle does not move but is located in the second entry 206 until the observation end time point. A third predicted trajectory 324 between the observation end time point and the prediction end time point is determined for the third vehicle. According to the prediction, the third vehicle moves from the second entry 206 in the roundabout 202 and, at the end time point, is located in the roundabout 202 in the area of the third exit 216.

From the start time point until the observation end time point, the fourth vehicle moves on the fourth observed trajectory 226 to an area in the roundabout 202 between the third exit 216 and the third entry 208. This portion of the fourth observed trajectory 226 is shown with dashed lines in FIG. 2 and in FIG. 3. A fourth predicted trajectory 326 between the observation end time point and the prediction end time point is determined for the fourth vehicle. According to the prediction, the fourth vehicle moves from an area in the roundabout 202 between the third exit 216 and the third entry 208 in the roundabout 202 and, at the end time point, is located in the fourth exit 218.

From the start time point until the observation end time point, the fifth vehicle moves on the fifth observed trajectory 228 to an area in the roundabout 202 between the fourth exit 218 and the fourth entry 210. This portion of the fifth observed trajectory 228 is shown with dashed lines in FIG. 2 and in FIG. 3. A fifth predicted trajectory 328 between the observation end time point and the prediction end time point is determined for the fifth vehicle. According to the prediction, the fifth vehicle moves from an area in the roundabout 202 between the fourth exit 218 and the fourth entry 210 in the roundabout 202 and, at the end time point, is located in the first exit 212.

From the start time point until the observation end time point, the sixth vehicle moves on the sixth observed trajectory 230. In the example, the sixth vehicle does not move but is located in the fourth entry 210 until the observation end time point. A sixth predicted trajectory 330 between the observation end time point and the prediction end time point is determined for the sixth vehicle. According to the prediction, the sixth vehicle moves in the area of the fourth entry 210 until the end time point.

The predictions, i.e., the predicted trajectories in the example, are approximated as a Gaussian mixture distribution. The moments of the Gaussian mixture distribution are determined using the method described below depending on a portion of the behavior respectively observed for the individual agents 102, i.e., in the example, the observed portion, shown in dashed lines, of the respective observed trajectory.

In the example, 95% confidence intervals are visualized for the prediction with respect to the other portion shown of the observed trajectories.

The prediction of the trajectories, i.e., a time profile of positions of the agents 102, is an example. It may also be provided to determine the prediction for a distance between the agents 102, a velocity or an acceleration of the agents 102.

The behavior of the agents 102, in the example that of the vehicles, is observed for a specified time period. The prediction is determined depending on the behavior observed in the specified time period. In one example, at least one of the vehicles is an autonomous vehicle. The prediction represents a simulation of an environment of the at least one autonomous vehicle, wherein the at least one autonomous vehicle is controlled depending on the prediction.

The prediction is determined in the example by means of machine learning of a model, wherein the prediction is determined using the model.

This is described below for a latent variable X={xt}t=0T with xt∈RMDand an observed variable Y={yt}t=0T of dimension Dy, wherein xt∈RDis a set of M agents 102, and xtm∈RMDis a latent state of an agent m at a time point t, and ytm∈RMDis a state of the agents 102 at the time point t, which is defined by

x0˜p(x0|I)

xt=xt−1+ƒ(xt−1,I)+L(xt−1,I)wt−1,t=1, . . . ,T

yt˜N(yt|g(xt),QQT(xt))

wherein


- - x_(t) is a latent state of the agents **102**,
  - x₀ is an initial value for the latent state of the agents **102** at
    the start time point t=0,
  - ƒ(x_(t),I):R^(MDx)×R^(DI)→R^(Dx) is a deterministic change in the
    latent state x_(t) of the agents **102**, which change is modeled in
    the example as a neural network parameterized with parameters θ_(ƒ),
  - L(x_(t), I):R^(MDx)×R^(DI)→R^(Dx×Dx) is a stochastic change in the
    latent state x_(t) of the agents **102**, which change is modeled in
    the example as a neural network parameterized with parameters θ_(L),
    wherein θ={θ_(ƒ), θ_(L)} denotes these parameters,
  - I∈R^(DI) is a context variable that comprises an association N which
    associates each agent **102** with other agents **102** to be
    considered for predicting the behavior of this agent **102**, and
    that comprises a history that characterizes the behavior for each
    agent **102**,
  - w_(t)∈R^(MDx) is a random variable from a normal distribution
    w_(t)˜N(0,I) through which a disturbance variable is introduced,
  - N(y_(t)\|g(x_(t)),QQ^(T)(x_(t))) is a normal distribution whose mean
    value
  - g(x_(t)):R^(MDx)→R^(MDy×MDy) is modeled by a non-linear neural
    network parameterized with parameters ψ_(g), wherein the covariance
    thereof
  - QQ^(T)(x_(t)): R^(MDx)→R^(MDy×MDy) is determined by a variable Q,
    which is assumed to be constant or is modeled by a non-linear neural
    network parameterized with parameters ψ_(Q), wherein ψ={ψ_(g),ψ_(Q)}
    denotes these parameters.

The variable Y={yt}t=0T comprises the states of the dynamic system 104, in particular the states yt of the agents 102 at the time points t. In the example, the agents 102 are the vehicles and the variable Y comprises the observed portions of the trajectories. The variable X={xt}t=0T comprises the latent states of the dynamic system 104. In the example, the variable X comprises the latent states xt of the agents 102 at the time points t. The latent states xt comprise further information for a reliable prediction of a respective future state yt+1 of the agents 102. The latent state xt at the time point t comprises, for example, the accelerations or velocities of the vehicles at the time point t.

The prediction is determined below for a number M of agents 102 denoted hereinafter by m.

For them, the deterministic change is

\({f\left( {x_{t},I} \right)} = \begin{bmatrix}
{\overset{\_}{f}\left( {x_{t}^{1},x_{t}^{N_{1}},I} \right)} \\
 \vdots \\
{\overset{\_}{f}\left( {x_{t}^{M},x_{t}^{N_{M}},I} \right)}
\end{bmatrix}\)

and the stochastic change is

\({L\left( {x_{t},I} \right)} = {{diag}\begin{bmatrix}
{\overset{\_}{L}\left( {x_{t}^{1},x_{t}^{N_{1}},I} \right)} \\
 \vdots \\
{\overset{\_}{L}\left( {x_{t}^{M},x_{t}^{N_{M}},I} \right)}
\end{bmatrix}}\)

wherein (xtm, xtN, I): RD×RD×RD→RDdenotes an update to the deterministic change,

wherein (xtm, xtN, I): RD×RD×RD→RDdenotes an update to the stochastic change,

wherein xtN∈RDis a message for the agent m at the time point t, which message is determined as

xtN=AGG(xt,ε)m

wherein Nm={em,m′|em,m′=1}m′=1M denotes the first information item N for the agent m and an operation AGG(xt,ε):RMD×RM×M→RMDhas an output m for each agent, wherein the m-th agent is associated with the m-th output, wherein ε∈RM×M denotes edges of a graph that define a relationship of the agents to one another. In the example, the relationship of the agents to one another is a binary value.

After t prediction steps, this model considers correlations between agents 102 that have a distance from one another of at most t steps. In one example, distance means how many edges have to be followed to get from an agent m to an agent m′. The distance may be infinite if an agent is not connected to any other agent.

The prediction for a prediction time point T is a marginal probability p(yT|I), which as a nested integral

p(yT|I)=∫p(yT|xT)p(xT|x0,I)p(x0|I)dxT,x0

with a probability p(yT|xT) a kernel p(xT|x0,I) and a Gaussian mixture model (GMM) p(x0|I).

The kernel p(xT|x0,I) is approximated for each time step t by a normal distribution N(xt|μt(I),Σt(I)) with a mean value μt(I) and a covariance Σt(I), wherein

μt(I)=μt−1(I)+E[ƒ(xt−1,I)]

Σt(I)=Σt−1(I)+Cov[ƒ(xt−1,I)]+Cov[xt−1,ƒ(xt−1,I)]+Cov[xt−1,ƒ(xt−1,I)]T+

E[LLT(xt−1,I)]

wherein E denotes the expected value, and Cov denotes the covariance, and wherein Cov[xt−1,ƒ(xt−1,I)] denotes the cross-covariance between random vectors in the arguments xt−1 and ƒ(xt−1, I).

The function ƒ(x,I) is implemented in the example as a neural network. The function L(x,I) is implemented in the example as a neural network. The function g(x) is implemented in the example as a neural network. The function Q(x) is implemented in the example as a neural network.

An expected value and a covariance for an output of the respective neural network is determined as described, for example, in Anqi Wu, Sebastian Nowozin, Edward Meeds, Richard E. Turner, Jose Miguel Hernandez-Lobato, and Alexander L. Gaunt: “Deterministic Variational Inference for Robust Bayesian Neural Networks,” in ICLR, 2019a (Anqi Wu).

The cross-covariance Cov[xt, ƒ(xt, I)] is approximated, for example, by

Cov[xt,ƒ(xt,I)]=Cov[xt]E[∀x,ƒ(xt,I)]

wherein the expected value for the Jacobi matrix is approximated as in Andreas Look, Jan Peters, and Melih Kandemir: “Deterministic Inference of Neural Stochastic Differential Equations,” arXiv, abs/2006.08973, 2020, (Andreas Look).

\({E\left\lbrack {\nabla_{x_{t}}{f\left( {x_{t},I} \right)}} \right\rbrack} \approx {\prod\limits_{l = 1}^{L}{E\left\lbrack J_{t}^{l} \right\rbrack}}\)

wherein Jtl is the Jacobi matrix in the layer l of the neural network at the time point t.

FIG. 4 shows steps in a method for the prediction p(yT|I) of a behavior yt={ytm}i=1M of agents m in the dynamic system 104 with a multiplicity M of interacting agents m.

The prediction p(yT|I) is determined depending on the latent state xt of the agents m. The method comprises two loops, an inner loop and an outer loop.

For a first one of the iterations, the initial latent state x0 it taken from a Gaussian mixture model with V components v, which is defined by the normal distribution N(x0|μ0(I),Σ0(I)).

The first moment μt and the second moment Σt of the normal distribution N(xt|μt(I),Σt(I)) is determined in the inner loop in iterations. Initially, for each component v, a value of the first moment μ0,v and a value of the second moment Σ0,v of the normal distribution N(x0,v|μ0,v(I)), Σ0,v(I)). In the example, these values depend on the context variable I.

The values of the moments μ0,v and Σ0,V are determined as a function of the context variable I by a further neural network. An example of this neural network with 30 fully connected layers and a tanh activation, which is followed by a layer for the operation AGG, which is followed by 64 fully connected layers and a tanh activation, which is followed by a fully connected layer for the values of the first moment μ0,v and which is followed by a further fully connected layer with exp activation, which is shown in FIG. 5a.

The inner loop is calculated for a plurality V of components v and for a plurality of time points t at a prediction time point T. The inner loop is calculated for the prediction time point T for the plurality V of components v.

The normal distribution N(xt|μt(I),Σt(I)) models the latent state xt of the agents m. The normal distribution N(yt|g(xt),QQT(xt)) models the behavior yt of the agents m depending on the latent state thereof xt.

In the method, a normal distribution N(aT,v(I),BT,v(I)) models a behavior of individual components v.

In a step 402, the context variable I is specified. The context variable I comprises, in one example, the association Nm, which associates at least one agent m with another agent m to be considered for predicting the behavior of this agent m. The context variable I in the example is given.

The association Nm in one example is a matrix whose rows each represent one of the agents m and whose columns each represent one of the agents m.

In the example, a value, in particular a binary value, is determined for each element of the matrix.

In one example, the value of an element identified by its row and its column in the matrix specifies whether or not the agent m identified by the row is to be considered for the prediction for the agent m identified by the column.

In one example, the value of an element identified by its row and its column in the matrix specifies whether or not the agent m identified by the column is to be considered for the prediction for the agent m identified by the row.

For example, the relationships of the agents m to one another are modeled using the graph, wherein the values ε of the edges are determined such that, in the graph, agents m′ neighboring an agent m are considered for the prediction thereof.

The context variable I comprises, in one example, the history of the dynamic system 104.

The context variable I in the example is used to determine the moments, expected values and weights, the argument of which comprises the context variable I.

The plurality V of components v is determined in the example with a neural network whose input variables comprise the history of the dynamic system 104 and the edges E from the context variable I. In one example, the history of the system 104 is defined by the observed behavior of agents m, in particular the observed portion of the trajectories.

The edges in the example in the matrix Nm are binary values 0 or 1, which, for example, indicate with the value 1 that an edge exists between two nodes and are otherwise zero. The latent state xtm of an agent m at the time point t is represented by a node in the graph.

The trajectories are defined in one example by a temporal sequence of two-dimensional or three-dimensional geographic coordinates, which indicate a temporal sequence of positions of the vehicles.

Using the operation AGG in the example, the messages xtNare determined depending on the matrix Nm and the one-dimensional input variable. The messages xtNare concatenated the one-dimensional input variable and mapped using the neural network onto the values of the first moment μ0,v and the value of the second moment Σ0,v.

For example, the neural network is a graph neural network. The latter is designed, for example, as described in Peter W. Battaglia, Jessica B. Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinicius Flores Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner, Qaglar GiAlcehre, H. Francis Song, Andrew J. Ballard, Justin Gilmer, George E. Dahl, Ashish Vaswani, Kelsey R. Allen, Charles Nash, Victoria Langston, Chris Dyer, Nicolas Heess, Daan Wierstra, Pushmeet Kohli, MatthewBotvinick, Oriol Vinyals, Yujia Li, and Razvan Pascanu; “Relational inductive biases, deep learning, and graph networks;” arXiv, abs/1806.01261, 2018.

In a step 404, for the plurality V of components v and for the plurality of time points t=1, . . . T, in iterations, until the prediction time point T, for each component v, a value of the first moment μt of the normal distribution N(xt|μt(I),Σt(I)) is determined.

The value of the first moment μt is determined recursively in the example. This means that the value of the first moment μt at a time point t is determined depending on a value of the first moment μt−1 for a time point, e.g., t−1, preceding the time point t.

The following description is based on a tool which can be used to determine an expected value E[f(x)] of a function f(x), a covariance matrix Cov(f(x)) of the function f(x) and a cross-covariance matrix Cov(x,f(x)). For example, the expected value E[f(x)] and the covariance matrix Cov(f(x)) are determined, for example, as described in Anqi Wu. The cross-covariance matrix Cov(x,f(x)) is determined, for example, as described in Andreas Look.

The tool requires that layers, the moments of which can be calculated at the output, are used in the neural network to determine the expected value E[f(x)], the covariance matrix Cov(f(x)) and the cross-covariance matrix Cov(x,f(x)). The operation AGG(xt,ε) is used for this purpose.

The operation AGG(xt,ε) is implemented, for example, as a mean value aggregation in the respective neural network, wherein, for a layer l of the neural network, the message xtl,Nin the time step t for the agent m

\(x_{t}^{l,N_{m}} = {\frac{1}{❘N_{m}❘}{\sum\limits_{{m\prime} \in N_{m}}x_{t}^{l,{m\prime}}}}\)

is determined.

For example, for a set of messages xtl,N, the Kronecker product is used to determine, ⊗ depending on the E[xtl] for the message from a layer l, the expected value

E[xtl,N]=(A└ID)E[xtl]

and the covariance

Cov[xtl,N]=(A⊗ID)Cov[xtl](A⊗ID)T

wherein


- - A∈R^(M×M) is an adjacency matrix with normalized rows that comprise
    the information ε regarding the edges in matrix form, and I_(Dx,l)
    is an identity matrix of dimension D_(x,l)×D_(x,l). The Jacobi
    matrix is available as_J_(t)^(l)=A⊗I_(Dx,l).

The tool requires that for the layers l of the neural network, the same affine transformation with the same weight matrix Wl and the same bias bl is carried out. In one example, the calculation takes place for all layers together using a Kronecker product.

E[xtl+1]=ŴlE[xtl]+{circumflex over (b)}l

Cov[xtl+1]=ŴlCov[xtl](Ŵl)T+{circumflex over (b)}l

with

\(x_{t}^{l} = \begin{bmatrix}
x_{t}^{l,1} \\
x_{t}^{l,2} \\
 \vdots \\
x_{t}^{l,M}
\end{bmatrix}\)
\({\hat{W}}^{l} = \begin{bmatrix}
W^{l} & 0 & \cdots & 0 \\
0 & W^{l} & \cdots & 0 \\
 \vdots & {\ddots} & & \vdots \\
0 & 0 & \cdots & W^{l}
\end{bmatrix}\)
\({\hat{b}}^{l} = \begin{bmatrix}
b^{l} \\
b^{l} \\
 \vdots \\
b^{l}
\end{bmatrix}\)

wherein the Jacobi matrix is available as Jtl=Ŵl.

The value of the first moment μt is determined in the example depending on the expected value E[ƒ(xt−1,I)] for the deterministic change ƒ(xt−1,I) of the first moment μt.

In one example, the value of the first moment μt is determined as follows:

μt(I)=μt−1(I)+E[ƒ(xt−1,I)]

The expected value E[ƒ(xt−1,I)], i.e., the change in the first moment μt, in one example, is comprised depending on the edges E from the context variable I and the distribution of the latent state xt−1 at the preceding time point, is determined as described in Anqi Wu by means of the tool.

The edges in the example in the matrix Nm are binary values 0 or 1, which, for example, indicate with the value 1 that an edge exists between two nodes and are otherwise zero. The latent state xtm of an agent m at the time point t is represented by a node in the graph.

Using the operation AGG in the example, the messages xtNare determined depending on the matrix Nm and the latent state xt−1 at the preceding time point. The messages xtNare concatenated with the state xt−1 at the preceding time point. The tool is used to determine the expected value E[ƒ(xt−1, I)].

An example of a neural network ƒ(xt−1, I) with a layer for the operation AGG, which is followed by 24 fully connected layers and a ReLu activation, which is followed by a fully connected layer and a ReLu activation, which is followed by another fully connected layer, is shown in FIG. 5b.

In a step 406, for the plurality V of components v and for the plurality of time points t=1, . . . T until the prediction time point T, for each component v, a value of a second moment Σt of the normal distribution N(xt|μt(I), Σt(I)) is determined.

The value of the second moment Σt is determined recursively in the example. This means that the value of the second moment Σt for the time point t is determined depending on a value of the second moment Σt−1 for a time point, e.g., t−1, preceding the time point t.

In one example, the value of the second moment Σt is determined depending on the covariance Cov[ƒ(xt−1, I)] of the deterministic change ƒ(xt−1, I) and on the expected value E[LLT(xt−1, I)] for the stochastic change L(xt−1, I) of the second moment Σt.

It may be provided that the value of the second moment Σt for the time point t is determined depending on the value of the second moment Σt−1 for the preceding time point, e.g., t−1, and the covariance Cov[ƒ(xt−1, I)] of the deterministic change ƒ(xt−1, I) and the covariance Cov[xt−1, ƒ(xt−1,I)] of the latent state xt−1 at the preceding time point tt−1 with the deterministic change ƒ(xt−1, I) and the transpose of the covariance Cov[xt−1, ƒ(xt−1, I)] of the latent state xt−1 at the preceding time point, e.g., tt−1, with the deterministic change ƒ(xt−1, I) and the expected value E[LLT(xt−1, I)] for the stochastic change L(xt−1, I):

Σt(I)=Σt−1(I)+Cov[ƒ(xt−1,I)]+Cov[xt−1,ƒ(xt−1,I)]+Cov[xt−1,ƒ(xt−1,I)]T+

E[LLT(xt−1,I)]

The expected value E[LLT(xt−1, I)], i.e., the change in the second moment Σt, in one example, is determined depending on edges ε from the context variable I and the latent state xt−1 at the preceding time point. In the example, the tool is used to determine E[L] and Cov[L] and thus E[LLT(xt−1, I)]=Cov[L]+E[L]E[L]T.

The edges in the example in the matrix Nm are binary values 0 or 1, which, for example, indicate with the value 1 that an edge exists between two nodes and are otherwise zero. The latent state xtm of an agent m at the time point t is represented by a node in the graph.

Using the operation AGG in the example, the messages xtNare determined depending on the matrix Nm and the latent state xt−1 at the preceding time point. The messages xtNare concatenated with the state xt−1 at the preceding time point and mapped onto the expected value E[LLT(xt−1, I)].

An example of a neural network L(xt−1,I) with a layer for the operation AGG, which is followed by 24 fully connected layers and a ReLu activation, which is followed by a fully connected layer and a ReLu activation, is shown in FIG. 5c.

The inner loop includes steps 404 and 406.

In a step 408, for each component v, an expected value E[g(xT,v)] for the first moment g(xT,v) of the normal distribution N(yt|g(xt), QQT(xt)) at the prediction time point T is determined. The distribution of yt, in one example, is approximated by a Gaussian mixture model (GMM) yT˜Σvπ(I)N(yT|aT,v(I),BT,v(I)).

In the example, for each component v, depending on the value of the first moment g(xT,v) at the prediction time point T, a covariance of Cov[g(xT,v)] of the first moment g(xT,v) is determined.

In a step 410, the expected value E[g(xT,v)] for the first moment g(xT,v) of the normal distribution N(yt,v|g(xt,v), QQT(xt,v)) is determined depending on the value of the first moment μT,v at the prediction time point T.

In a step 412, a first moment aT,v(I) of the normal distribution N(aT,v(I),BT,v(I)) is determined.

In the example, for each component v, depending on a latent state xT,v at the prediction time point T, an expected value E[QQT(xT,v)] for the second moment QQT(x(t)) of the normal distribution N(yt|g(xt), QQT(xt)) at the prediction time point T is determined as described in Anqi Wu as a function of xt˜N(x_t|μt,v,Σt,v) by the tool.

In the example, the expected value E[g(xT,v)] defines the first moment aT,v(I), e.g., by

aT,v(I)=E[g(xT,v)]

The expected value E[g(xT,v)] is determined in the example using the tool.

An example of a neural network g(xt,v) with 24 fully connected layers and a ReLu activation, which is followed by a fully connected layer, is shown in FIG. 5d. For Q(xt), a constant is assumed in the example, but more complex neural networks are also possible.

In a step 414, for each component v, a second moment BT,v(I) of the normal distribution N(aT,v(I),BT,v(I)) is determined.

In the example, for each component v, depending on the covariance Cov[g(xT,v)] of the first moment g(xT,v) and on the expected value E[QQT(xT,v)] for the second moment QQT(xT,v) at the prediction time point T, the second moment VT,v(I) of the normal distribution N(aT,v(I),BT,v(I)) is determined, e.g., by

BT,v(I)=COV[g(xT,v)]+E[QQT(xT,v)]

The Covariance Cov[g(xT,v)] and the expected value E[QQT(xT,v)] are determined in the example using the tool.

The outer loop includes steps 408 to 414.

In a step 416, in particular weighted by at least one weight πv(I), a sum Σv=1Vπv(I)N(aT,v(I), BT,v(I)) of the third normal distributions N(aT,v(I), BT,v(I)) of the components v is determined.

In a step 420, the prediction p(yT|I) of the behavior yT={ytm}t=1M is determined depending on the sum Σv=1Vπv(I)N(aT,v(I), BT,v(I)), e.g.,

p(yT|I)=Σv=1V(I)N(aT,v(I),BT,v(I))

v=1

In a step 422, the prediction is output and/or at least one agent 102 is controlled depending on the prediction.

For example, the computer-controlled machine, the robot, the vehicle, the household appliance, the driven machine, the manufacturing machine, the personal assistant, or the access control system is controlled.

For example, the prediction for the molecular dynamics is determined and output. For example, the prediction for the movement during the game is determined and output.

The covariances for the different combinations of the latent states can be processed as a matrix of dimension MDx×MDx, which comprises blocks which are respectively defined by one of the covariances. In one example, it is provided that the matrix is approximated as a thinly populated matrix.

FIG. 6 shows a schematic representation of approximations of a covariance matrix for five agents A, B, C, D, E.

The latent state of an agent m comprises several elements in one example. For example, for the trajectories, the latent state comprises an element for a velocity of the agent m and an element for an acceleration of the agent m. The elements do not have to be physical quantities but may also relate to other aspects of a state of an agent.

In a first approximation of the matrix, only elements from the matrix located on the major diagonal of the matrix are used for the prediction, wherein other elements of the matrix are not considered. This means that the latent states of an agent m are modeled independently of one another and the latent states of different agents m are also modeled independently of one another. For example, the velocity of the agent m is modeled independently of its acceleration, and both the velocities of the different agents m and their accelerations are modeled independently of one another.

The main diagonal is shown in FIG. 6 as a solid diagonal line. In a second approximation, the latent states of an agent are modeled independently of one another and corresponding elements of the latent states of different agents are modeled dependently on one another. For example, the velocity and the acceleration of the same agent are modeled independently of one another, and the velocities of the different agents are modeled dependently on one another, and the accelerations of the different agents are modeled dependently of one another. This is represented in FIG. 6 by the solid line and diagonal, dashed lines.

In a third approximation, different elements of the latent state of an agent are modeled dependently on one another and the latent states of different agents are modeled independently of one another. This is shown in FIG. 6 by the diagonal of the shaded blocks.

The parameters θ={θƒ, θL} and ψ={ψg, ψQ} of the neural networks parameterized therewith are determined in the example in a training with a data set D={Y,I}, in the example the observed trajectories, by minimizing the expected negative logarithmic probability:

argminθ,ψ−log E[P(yt|I)]

