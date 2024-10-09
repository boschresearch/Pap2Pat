# DESCRIPTION

## FEDERAL FUNDING

None

## BACKGROUND

Existing missile guidance methods—such as proportional navigation (PN), augmented proportional navigation (APN), ad-hoc filters, and single loop integrated guidance and control systems—are not optimal to intercept maneuvering targets.

Using proportional navigation, a commanded acceleration is perpendicular to the instantaneous pursuer-target line of sight (LOS) and is proportional to the line-of-sight angular rate and closing velocity. Using augmented proportional navigation, the commanded acceleration from proportional navigation is augmented with an additional term that is a function of the estimated target acceleration. Although augmented proportional navigation works well with targets maneuvering with a constant acceleration, its performance can actually be worse than standard proportional guidance for weaving targets and other more complex target maneuvers. Moreover, augmented proportional navigation requires an estimation of target acceleration, which is still an open problem for passive seekers that cannot measure range and range rate. To intercept weaving targets, ad-hoc filters and other solutions have been proposed that attempt to estimate the weave frequency and amplitude. However, those solutions rely on the target maintaining a constant weave frequency and amplitude. Finally, while single loop integrated guidance and control systems have the potential to significantly improve missile performance by reducing flight control response time, those systems map navigation system outputs directly to commanded fin deflections. Because there is no commanded acceleration to augment, those single loop integrated guidance and control systems are incompatible with augmented proportional navigation.

Accordingly, there is a need for improved missile guidance to intercept maneuvering targets.

## SUMMARY

In order to overcome those and other drawbacks of the prior art, a missile guidance system and method are disclosed. A curvature parameterization is applied to a line-of-sight unit vector between a missile and a target and a line-of-sight rotation rate is derived from the line-of-sight unit vector with the applied curvature parameterization. In some embodiments, the curvature parameterization is learned by a deep learning network (e.g., a deep neural network that includes a recurrent layer). The deep neural network may be optimized using meta reinforcement learning over an ensemble of engagement scenarios with varying target behavior.

In some embodiments, for example, the deep learning network generates a policy for generating a rotational velocity vector and a line-of-sight bias network integrates the rotational velocity vector to create an attitude parameterization, uses the attitude parameterization to create a rotation matrix, and uses the rotation matrix to apply the curvature parameterization to the line-of-sight unit vector. In other embodiments, the deep learning network may learn a policy for generating a curvature parameterization to apply to a relative velocity unit vector.

## DETAILED DESCRIPTION

Reference to the drawings illustrating various views of exemplary embodiments is now made. In the drawings and the description of the drawings herein, certain terminology is used for convenience only and is not to be taken as limiting the embodiments of the present invention. Furthermore, in the drawings and the description below, like numerals indicate like elements throughout.

FIG. 1A is a diagram illustrating a prior art navigation system 120 of an air-to-air missile 101. FIG. 1B is a planar representation of an engagement between the missile 101 and a target 109. As shown in FIG. 1B, the missile 101 is represented by a missile position vector FM indicative of position of the missile 101 relative to an origin of a coordinate system and a missile velocity vector vM indicative of the amplitude and direction of the instantaneous velocity of the missile 101. Similarly, the target 109 by a target position vector rT and a target velocity vector vT. The relative position vector is defined as rTM=rT−rM and the relative velocity vector is defined as vTM=vT−vM.

In the planar representation of FIG. 1B, the relative position vector rTM forms a line-of-sight angle λ relative to an axis of the coordinate plane. The rate of change of the line-of-sight angle λ as the missile 101 travels along the target velocity vector vT and the target 109 travels along the target velocity vector vT is referred to as the line-of-sight rotation rate Ω. The planar representation of FIG. 1B can easily be extended to a three-dimensional representation.

As shown in FIG. 1A, the missile 101 includes a seeker 112 (e.g., an infrared seeker) protected by a radome, rate gyroscopes 114, and an accelerometer 116. The navigation system 120 identifies the line-of-sight unit vector A based on sensor data from a seeker 112 and outputs the line-of-sight unit vector A to a guidance/control system that outputs control signals to actuators to intercept the target 109. (The navigation system 120 also monitors the position, orientation, and translational and rotational velocity and acceleration of the missile 101 based on sensor data from rate gyroscopes 114 and an accelerometer 116.)

FIG. 2A is a diagram illustrating a line-of-sight bias network 200 according to exemplary embodiments. FIG. 2B is a simplified representation of an engagement by a missile 101 having the line-of-sight bias network 200 according to exemplary embodiments.

As described in detail below, the line-of-sight bias network 200 uses a line-of-sight curvature policy τ to apply a curvature parameterization to the line-of-sight unit vector λ provided by the navigation system 120. The curvature parameterization biases the line-of-sight rotation rate Ω that is derived from the line-of-sight unit vector λ. The line-of-sight bias network 200 outputs the curved line-of-sight unit vector λLOSC to the guidance/control system 160. The biased line-of-sight rotation rate ΩLOSC may be output to the guidance/control system 160 by the line-of-sight bias network 200 or derived from the curved line-of-sight unit vector λLOSC by the guidance/control system 160. The line-of-sight bias network 200 may be realized, for example, as software running on a central processing unit (CPU) or tensor processing unit (TPU), neuromorphic implementations, etc.

The line-of-sight curvature policy π: o→u maps observations o to actions u. The observations o, for example, may be given in Equation 1:

o=[{tilde over (λ)}{tilde over (Ω)}νcr]  [Eq. 1]

where {tilde over (λ)} is the three-dimensional line-of-sight unit vector, {tilde over (Ω)} is the line-of-sight rotation rate, νc is the closing velocity νc=−{tilde over (λ)}·vTM, and r is the relative range r=∥rTM∥.

The action u is used to compute a shaped line-of-sight direction vector λLOSC, which is used to construct a rotation vector QLOSC as shown in equation 2:

\(\begin{matrix}
{\Omega_{LOSC} = \frac{r_{TM_{LOSC}} \times v_{TM}}{r_{TM_{LOSC}} \cdot r_{TM_{LOSC}}}} & \left\lbrack {{Eq}.2} \right\rbrack
\end{matrix}\)

where rTM=λLOSCr.

By varying the action u during the engagement, the line-of-sight curvature policy π can curve the line-of-sight direction vector λLOSC, which is used to construct the line-of-sight rotation vector ΩLOSC. Both the curved line-of-sight direction vector λLOSC and the rotation vector ΩLOSC are used by the guidance/control system 160 to intercept the target 109. For example, the action u may be scaled and interpreted as a Euler 321 attitude θLOSC∈SO(3)=ku where k is a scaling factor (e.g., 2°). The Euler 321 attitude θLOSC may then be used to construct a direction cosine matrix C(θLOSC), which is used to compute the shaped line-of-sight direction vector as λLOSC=C(θLOSC){tilde over (λ)}, which is used to construct the line-of-sight rotation vector ΩLOSC.

A deep learning network, for example a reinforcement learning framework, may be used to simulate interactions between a missile 101 and a target 109 to learn the curvature parameterization to apply to the line-of-sight unit vector λ provided by the navigation system 120 and bias the line-of-sight rotation rate Ω. In other embodiments, the system may use other optimization algorithms to generate the line-of-sight bias.

FIG. 3 is a diagram of a reinforcement learning framework 300 according to exemplary embodiments.

In the reinforcement learning framework 300, an agent 360 learns through episodic interaction with a reinforcement learning environment 310 how to successfully complete a task using a policy function π that maps observations o to actions u. Reinforcement learning has been demonstrated to be effective in optimizing integrated and adaptive guidance and control systems 160 that generate direct closed-loop mapping from navigation system 120 outputs to actuator 180 commands (e.g., asteroid close proximity operations, planetary landing, exoatmospheric intercept, endoatmospheric intercept, and hypersonic vehicle guidance).

The reinforcement learning environment 310 of FIG. 3 is an abstraction of the environment in which a missile 101 intercepts a target 109. The reinforcement learning framework 300 utilizes meta-reinforcement learning, which differs from generic reinforcement learning in that the agent 360 learns over an ensemble of environments 310. Accordingly, the reinforcement learning environment 310 of FIG. 3 includes an engagement scenario generator 320, a dynamics model 332, an ensemble of target behavior models 334, a radome model 336, a guidance law 340, and a reward function 350. The dynamics model 332 is a model of the properties of moving air and the interaction between the air and the missile 101 and target 109 moving through that air. Each target behavior model 334 randomly selects and simulates maneuvers (e.g., weave, bang-bang, jinking maneuvers) that may be performed by the target 109 to avoid interception. The radome and seeker model 336 is a model of the noise that is typically present in the observations o, for example due to refraction of the look angle through the radome, Gaussian white noise, gimbal lag of the seeker 112, etc. The guidance law 340 may be any system used to control the movement of the missile 101 (e.g., proportional navigation, augmented proportional navigation, etc.). Using the engagement scenario generator 320 and the models 332, 334, and 336, the environment 310 of FIG. 3 varies the engagement scenarios, dynamics, aerodynamic coefficients, radome parameters, and other factors. Optimization within the meta-reinforcement learning framework 300 results in an agent 360 that can quickly adapt to novel environments 310, often with just a few steps of interaction with the environment.

The engagement scenario generator 320 initializes an episode by randomly generating a ground truth state x. The state xk at each time index k may include, for example, the missile position vector rM, the missile velocity vector vM, the target position vector rT, the target velocity vector vT, etc. The environment 310 maps each state xk to an observation ok indicative of the sensor data that may be output by the seeker 112 (e.g., closing velocity νc and relative range ∥rTM∥) at the state xk and passes each observation ok to the agent 360.

The agent 360 uses each observation ok to generate an action uk that is sent to the environment 310. The environment 310 then uses each action uk and the current ground truth state xk to generate the next state xk+1. The environment also uses the reward function 350 described below to generate a scalar reward signal r(xk, uk) based on the state xk and the action uk generated by the agent 360. The reward r(xk, uk) and the observation ok+1 corresponding to the next state xk+1 are then passed to the agent 360. The process repeats until the environment 310 terminates the episode, with the termination signaled to the agent 360 via a done signal.

By receiving rewards r in response to actions u, the agent 360 learns from the consequences of the selected action u rather than from being explicitly taught. The agent 360 selects actions u on basis of its past experiences (exploitation) and also by new choices (exploration), which is essentially trial and error learning. The rewards r(xk, uk) encode the success of each action uk and the agent 360 seeks to learn a policy function πθ(uk|ok) that selects actions u that maximize the accumulated reward r over time. To minimize the convergence time to learn the optimal policy function πθ(uk|ok), the agent 360 may also learn the value function Vwπ(ok) describing, for every observation o, how much future reward r can be expected when performing actions u.

In the embodiment of FIG. 3, a trajectory accumulation module 370 collects observations o, actions u, and rewards r over a set of episodes (referred to as rollouts) simulating interaction between the agent 360 and environment 310. The collected observations o, actions u, and rewards r are used to update the policy function πθ(uk|ok) and value function Vwπ(ok). In the air-to-air missile environment 310, for example, an episode terminates when the closing velocity

\(v_{c} = {- \frac{r_{TM} \cdot v_{TM}}{r_{TM}}}\)

turns negative. Each rollout may consist of 60 episodes. The reinforcement learning framework 300 may be optimized for 90,000 episodes.

The reward function 350 maps observations o and actions u to a scalar reward signal r. For example, the reward function 350 may include two terminal rewards rterm1 and rterm2 and a curvature penalty rcurve, for example as shown in equation 3:

r=rterm1+rterm2−rcurve  [Eq. 3]

The first terminal reward rterm1 is in response to a determination that the relative distance rTM between the missile 101 and the target 109 is less than a threshold distance rlim, for example as shown in equation 4:

\(\begin{matrix}
{r_{{term}1} = \left\{ \begin{matrix}
{\beta,{{{if}r_{TM}} < {r_{\lim}{and}{done}}}} \\
{0,{otherwise}}
\end{matrix} \right.} & \left\lbrack {{Eq}.4} \right\rbrack
\end{matrix}\)

where “done” indicates the last step of an episode.

However, even when the relative distance rTM at the last step of an episode is greater the threshold distance rlim, a second terminal reward rterm2 that is inversely proportional to the relative distance ∥rTM∥ is provided, for example as shown in equation 5:

\(\begin{matrix}
{r_{{term}2} = \left\{ \begin{matrix}
{\in {\exp\left( \frac{{r_{TM}}^{2}}{\sigma_{LOSC}^{2}} \right)}} \\
{0,{otherwise}}
\end{matrix} \right.} & \left\lbrack {{Eq}.5} \right\rbrack
\end{matrix}\)

The curvature penalty rcurve penalizes line-of-sight curvature, encouraging the agent 360 to curve the line-of-sight λ only when it results in higher terminal rewards rterm1 and rterm2, for example as shown in equation 6:

rcurve=α∥θLOSC∥  [Eq. 6]

The hyperparameters may be α=0.01, β=10, rlim=1m, ∈=20, and σLOSC=1.

The value function Vwπ(ok) may be learned by minimizing the difference the predicted value Vwπ(oki) and the actual sum of discounted rewards, for example as shown in the cost function L(w) of equation 7:

\(\begin{matrix}
{{L(w)} = {\frac{1}{2M}{\sum\limits_{i = 1}^{M}\left( {{V_{w}^{\pi}\left( o_{k} \right)} - \left\lbrack {\sum\limits_{\ell = k}^{T}{\gamma^{\ell - k}{r\left( {u_{\ell}^{i},o_{\ell}^{i}} \right)}}} \right\rbrack} \right)^{2}}}} & \left\lbrack {{Eq}.7} \right\rbrack
\end{matrix}\)

The discount rate γ of 0.95 may be used for the curvature penalty rcurve and the smaller terminal reward rterm2. A discount rate γ of 0.995 may be used for may be used for the larger terminal reward rterm1.

Deep reinforcement learning involves building a deep learning model which enables function approximation between the input features and future discounted rewards values. That map of input features and all possible future discounted rewards values at a given state enables the reinforcement learning agent 360 to get an overall picture of environment 310, which further helps the agent 360 in choosing the optimal path. To get to the optimal path, the agent 360 can use an advantage function Awπ(ok, uk), which is the difference of the possible future discounted rewards values and the average of actions u which the agent 360 would have taken given that observation ok. An example implementation of reinforcement learning framework 300 uses an approximation to the advantage function that is the difference between the empirical return and a state value function baseline, for example as shown in equation 8:

\(\begin{matrix}
{{A_{w}^{\pi}\left( {o_{k},u_{k}} \right)} = {\left\lbrack {\sum\limits_{\ell = k}^{T}{\gamma^{\ell - k}{r\left( {o_{\ell},u_{\ell}} \right)}}} \right\rbrack - {V_{w}^{\pi}\left( x_{k} \right)}}} & \left\lbrack {{Eq}.8} \right\rbrack
\end{matrix}\)

The reinforcement learning framework 300 may utilize any policy gradient method for reinforcement learning. For example, the reinforcement learning may be implemented using proximal policy optimization (PPO), which alternates between sampling data through interaction with the environment 310 and optimizing a “surrogate” objective function using stochastic gradient ascent. Proximal policy optimization has demonstrated state-of-the-art performance for many reinforcement learning benchmark problems.

Proximal policy optimization (PPO) approximates the Trust Region Policy Optimization method by accounting for the policy adjustment constraint with a clipped objective function. The objective function used with proximal policy optimization can be expressed in terms of the probability ratio pk(θ), for example given by equation 9:

\(\begin{matrix}
{{p_{m}(\theta)} = \frac{\pi_{\theta}\left( u_{k} \middle| o_{k} \right)}{\pi_{\theta_{old}}\left( u_{k} \middle| o_{k} \right)}} & \left\lbrack {{Eq}.9} \right\rbrack
\end{matrix}\)

The optimization objective function may be formulated to minimize miss distance while meeting path constraints (such as load, heating rate, and look angle), for example as described below. Two surrogate objectives may be created, the first surrogate objective being the probability ratio pk(θ) multiplied by the advantages Awπ(ok, uk), for example as shown in equation 10:

obj1=pm(θ)Awπ(ok,uk)  [Eq. 10]

The second surrogate objective is a clipped (using clipping parameter E) version of the probability ratio pk(0) multiplied by the advantages Awπ(ok, uk), for example as shown in equation 11:

obj2=clip(pm(θ)Awπ(ok,uk),1−∈,1+∈)  [Eq. 11]

The objective to be maximized J(θ) is then the expectation under the trajectories induced by the policy of the lesser of those two surrogate objectives, for example as shown in equation 12:

J(θ)=p(τ)[min(obj1,obj2)]  [Eq. 12]

Both the policy function πθ(uk|ok) and the value function Vwπ(ok) may be implemented using neural networks, for example four-layer neural networks with tan h activations on each hidden layer. In the embodiment of FIG. 3, the policy function πθ(uk |ok) is implemented using a policy network 380 and the value function Vwπ(ok) is implemented using a value network. The policy network 380 and the value network 390 may periodically update the policy function πθ(uk|ok) and the value function Vwπ(ok) during optimization, for example after accumulating trajectory rollouts of 60 simulated episodes.

An example network architecture is shown in the following table, where nhi is the number of units in layer i, obs_dim is the observation dimension, and act dim is the action dimension.

Both the policy network 380 and the value network 390 may contain one or more recurrent network layers. For example, hidden layer 2 above of both the policy network 380 and the value network 390 may be a recurrent layer implemented using gated recurrent units. For a given trajectory over observations o and actions u, the recurrent layer will evolve differently for different target maneuvers, allowing the policy network 380 to infer the nature of the maneuver. Because both the policy function πθ(uk|ok) and the value function Vwπ(ok) used to optimize the policy function πθ(uk|ok) contain a recurrent network layer, the policy function πθ(uk|ok) generates actions using the history of observations u, allowing the policy function πθ(uk|ok) to infer properties of the target maneuvers. Meanwhile, by optimizing over an ensemble of target behavior models 334, the agent 360 learns to adapt, using the recurrent layer's hidden state to infer the current target behavior model 334.

Once the policy network 380 of the reinforcement learning framework 300 converges on a policy function πθ(uk|ok), the optimized policy function πθ(uk|ok) may be used by the line-of-sight bias network 200 to apply a curvature parameterization to the line of sight unit vector λ. Additionally, to further enhance performance, the reinforcement learning framework 300 may also learn a curvature parameterization to apply to the relative velocity unit vector vTM.

When combined with proportional navigation, the line-of-sight bias network 200 significantly outperforms augmented proportional navigation with perfect knowledge of target acceleration, achieving improved accuracy with less control effort against a wide range of target maneuvers. For example, the disclosed method significantly outperforms augmented proportional navigation for the case of random weave and bang-bang target maneuvers. Additionally, the disclosed method can generalize to novel maneuvers. Furthermore, the path constraint specification of the disclosed method is a significant improvement compared to augmented proportional navigation. Finally, the disclosed method is compatible with both passive sensors (e.g., infrared seekers) and single loop integrated guidance and control.

While preferred embodiments have been described above, those skilled in the art who have reviewed the present disclosure will readily appreciate that other embodiments can be realized within the scope of the invention. Accordingly, the present invention should be construed as limited only by any appended claims.

