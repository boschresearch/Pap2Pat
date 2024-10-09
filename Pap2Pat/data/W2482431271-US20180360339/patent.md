# DESCRIPTION

## BACKGROUND

The brain's sensorimotor cortex, as a complex neural sensorimotor control system, inherently finds and accomplishes all of its tasks in an optimal manner in terms of speed, accuracy, and efficiency in a vast range of input conditions [3, 4]. Noises, nonlinearities, delays, uncertainties, and redundancies are among many major problems that a sensorimotor control system may experience [5].

A primate's sensorimotor controller is equipped with the ability to predict motor movements and to compensate for time delays. Time-delay estimation is a difficult problem to simulate because it renders even the simplest linear systems nonlinear; yet, biological control systems are robust enough to deal with time delays. It is unclear, however, how this is achieved in biological systems.

For example, vestibulo-ocular reflex (VOR), a motor control system that stabilizes vision during head movements, is not prone to occurrence of delay up to 10 milliseconds from the onset of stimulus [8]. Smooth pursuit, another efficient visual control system in humans for target tracking in the visual field, has the ability to process information with an 80-130 millisecond delay in the brain [25, 26]. Delays make control difficult because information about the current state of the motor system is outdated. A motor control system that does not have delay compensation mechanisms could not correct for errors, leading to potential inefficiencies and instability.

Currently available time-delay estimation techniques mainly cover linear systems including, for example, constant time delays, random time delay with specific noise characteristics, and restricted dynamic time delay [20-27]. Most biological systems, however, exhibit some degree of variability, nonlinearity, and uncertainty, which can render these methods inapplicable. Further, most delay estimation procedures are not used in the context of predictive control methodology. The Hilbert-Huang Transform-based method, for example, is found to be the most efficient delay estimation technique with a focus on practical applicability to the motor control. However, the process is a complex one [26]. As such, a comprehensive and predictive computational model to explain time-delay compensation in biological control is still lacking.

## BRIEF SUMMARY

Embodiments of the subject invention provide computational models and methods of using the same to estimate variable time delay in the sensorimotor system of a subject.

In some embodiments, the computational model can accomplish one or more of the following tasks: estimating variable time delays in the sensorimotor system; predicting sensory states based on delayed sensory feedback; and controlling the system in real time. Embodiments provide that the subject is a human or a primate.

In some embodiments, simulation experiments are used to show how the models provided herein can explain a sensorimotor system's ability to compensate for delays during online learning and control. Specifically, examples are provided to demonstrate the benefits of the time-delay estimation model and the application of the model to simulate a horizontal Vestibulo-Ocular Reflex (hVOR) system.

Systems, methods, and models provided herein are distinguished from prior art methods in that prior art computational models are only capable of simulating a sensorimotor control system in the presence of time delays and noise rather than predicting the dynamics of variable time delays and future sensory states from delayed sensory information.

Advantageously, systems, models, and methods provided herein can lead to a better understanding of the function of the human sensorimotor cortex, with practical applications in explaining the mechanisms underlying neurological disorders manifested as delays and faults affecting the brain (e.g., autism [28], Parkinson's disease, Alzheimer's disease, epilepsy [29]) and the eye. Further, the technology provided herein can be used to model behavior of a healthy sensorimotor system (e.g., parts or whole of a healthy brain) based on faulty information received from the system's neurons.

## DETAILED DESCRIPTION

Embodiments of the subject invention provide computational models and methods and systems of using the models to predict the dynamics of variable time delays and future sensory states from delayed sensory information.

The term “subject”, in the context of a subject being tested, examined, or the like, can refer to a human or a primate such as, for example, a baboon, a monkey, or a macaque.

In some embodiments, a “sensorimotor system” can be a combination of at least one sensory organ, associated muscle or muscle groups, and neural networks that control the organs and the muscles to accomplish a desired motion or task. Non-limiting examples of sensory organs include those that are capable of performing ophthalmoception (sight), audioception (hearing), gustaoception (taste), olfacoception (smell), and/or tactioception (touch), such as, e.g., eyes, ears, sensors in the head for vibration and proprioception; such organs can be monitored with, for example, blood pressure sensors, glucose sensors, temperatures sensors, and external vibration sensors.

In some embodiments of the subject invention, a sensorimotor system can execute one or more of the following processes: horizontal vestibule-ocular reflex, saccadic eye movement, smooth pursuit system, hand movements, hand-eye coordination, walking, running, skilled movements, opto-kinetic reflex, and balance tasks.

For a primate or a human subject, time delays can occur in various parts of the sensorimotor system. The value of time delay is dynamic and can vary with each specific sensory modality. The complexity of processing sensory information further depends on the nature of the task. For example, because there is a longer delay for vision than for proprioception, face recognition takes longer than motion perception.

Due to delays in information processing and transmission, simple feedback control is affected by significant temporal discrepancies between the target signal and the current state, suggesting that some form of predictive control must take place to achieve such a high performance in the system [15].

For example, the duration of saccadic eye movement, a fast eye movement produced by a visual system that directs the eyes to interesting visual stimuli, is shorter than the sensory delay [25]. This means that the sensory feedback about the current state of the eye and the visual field cannot be used to correct or guide the saccades because the sensory information regarding the movement itself arrives after the completion of the movement.

In a further example, the smooth pursuit eye movement allows a human subject to track targets in the visual field at a high speed of approximately 200° (degrees of field of vision) per second. However, the position of the eyes is ahead of the visual sensory feedback of the target position. As a result, this phenomenon cannot be achieved by solely implementing standard negative feedback methods based on visual error signals [12-14].

Primates have demonstrated this predictive nature of sensorimotor control systems in prior art experiments. For example, monkeys have the ability to conduct smooth pursuit movements with zero retinal slip [16, 17] and maintain smooth pursuit during blink periods (i.e., momentary disappearances of the target) [18]. Such predictive compensation was observed both in tracking moving targets with constant velocity or in sinusoidal moving objects. In a hand movement study, it was demonstrated that the cerebellum is involved in predicting the position of the hand during a movement [19]. The predicted state of the limb from the history of motor commands allows the motor control to act on this estimate of state rather than relying solely on a delayed sensory feedback. This suggests that cerebellar output is a signal that can be combined with delayed sensory feedback elsewhere in the brain in order to generate estimates of real-time states of motor control.

Embodiments of the subject invention address the abovementioned need for estimating time delays and predicting control solutions in a subject's sensorimotor system by providing a computational model that can be evaluated in real time, with online learning and control simulation processes.

In some embodiments, a computational model simulates a subject's brain as a sensorimotor control system and can accomplish one or more of the following tasks: 1) estimating variable time delay in the sensorimotor system; 2) predicting sensory states based on delayed sensory feedback; and 3) controlling the system in real time.

In order for the model to simulate the brain as a sensorimotor system, the following assumptions are incorporated herein: 1) the brain possesses a time-delay estimator circuit; 2) the brain uses the estimate of time delay to predict the current state; 3) the brain uses the current predicted estimate to control motor movements; and 4) the brain is a truly autonomous system and that it does not maintain an absolute time, but only what is perceived from external, periodic stimuli.

Referring to FIG. 1, in an embodiment, elements and connectivity between components of the computational model simulating the brain as a sensorimotor control system at a higher level can be as shown. Tables 1 and 2 explain each known and unknown variable of FIG. 1. Note that the “Delay Estimator,” the “State Predictor,” and the “Controller” represent the three tasks the model aims to accomplish and is each described in detail herein.

### Estimating the Time Delay

As provided herein, a sensorimotor system (e.g., the brain) can be approximated in a region of interest by a linear time-varying system, as stated in Equation (1):

{dot over (x)}(t)=A(t)x(t)+B(t)u(t)  (1)

where x(t) is the state vector (e.g., the position of the eye or hand in space, etc.), u(t) is the control vector or the neural motor commands (e.g., the firing of motor-neurons or muscle contractions), and A(t) and B(t) are time-varying matrices with appropriate dimensions. Also, r(t) is desired sensory outcome, x(t) represents current sensory state, and u(t) represents motor commands that try to bring current sensory state to desired sensory outcome.

Jacobian matrix A(t) represents the influence of the current state x(t) of the motor system to its future changes {dot over (x)}(t). Jacobian matrix B(t) is the sensorimotor controller gain, which determines how motor commands affect {dot over (x)}(t). In some embodiments, A(t) and B(t) can change over time. Non-limiting examples representing A(t) and B(t) include joint friction, viscosity, and elasticity of muscles, which can all change over time. A(t), G(t), B(t), and u(t) can be inferred or computed from sensory inputs; in simulation of a sensorimotor system, these matrices can instead be inferred from measured sensory signals.

The solution to the first order differential Equation (1) is given by

\(\begin{matrix}
{{x(t)} = {{e^{\int_{0}^{t}{{A{(s)}}{ds}}}x_{0}} + {\int_{0}^{t}{e^{\int_{s}^{t}{{A{(v)}}{dv}}}{B(s)}{u(s)}{ds}}}}} & (2)
\end{matrix}\)

where x0 is the initial state [30].

Let G(t)=e∫A(s)ds and Equation (2) written in terms of G(t) is

\(\begin{matrix}
{{x(t)} = {{{G(t)}x_{0}} + {{G(t)}{\int_{0}^{t}{{G^{- 1}(s)}{B(s)}{u(s)}{ds}}}}}} & (3)
\end{matrix}\)

where x(t) is the current state of the sensorimotor system measured by the sensor organs. The motor command vector is u(t).

Motor commands are usually sensed at the level of the effector by specialized sensory organs. In an embodiment, muscle spindles can measure the force generated in the muscle and communicate the information to the brain. As a result, it is assumed that x(t) and u(t) can be precisely measured by sensory organs represented by the “Plant” box as shown in FIG. 1.

As provided herein, the sensory time-delay vector is represented by τ=[τi] (i.e., the ith time delay value). In a preferred embodiment, it is assumed that τ=τi hereafter. The solution of Equation (2) incorporating the time delay is thus

\(\begin{matrix}
{{x\left( {t - \tau} \right)} = {{{G\left( {t - \tau} \right)}x_{0}} + {{G\left( {t - \tau} \right)}{\int_{0}^{t - \tau}{{G^{- 1}(s)}{B(s)}{u(s)}{ds}}}}}} & (4)
\end{matrix}\)

As an autonomous system, the brain perceives the sensation of time based on external periodic stimulation. In other words, the brain is a data-driven asynchronous collection of sensorimotor control systems. This feature distinguishes the brain from industrial control systems, which utilize synchronized clocks to count the ticking of time. As a result, the time variable t can be accessed directly in an industrial control system but not in the brain's sensorimotor control system.

The brain keeps an internal estimate of time delays, denoted as {circumflex over (τ)}, and is capable of using the estimated time delay to predict the current and future sensory states. The error signal between the delayed sensory signal x(t−τ) and the estimated delayed sensory signal x(t−{circumflex over (τ)}) is calculated as (=x(t−τ)−x(t−{circumflex over (τ)}). The delayed sensory signals are known to the brain, but the brain cannot access the time delay vector τ directly. On the other hand, x(t−{circumflex over (τ)}) is unknown since {circumflex over (τ)} is unknown. One skilled in the art would appreciate that the delayed sensory signal x(t−τ) can in fact be computed from the knowledge of G(t), B(t) and u(t) as provided by the model of the subject invention.

To compute {circumflex over (τ)}, a modified version of the gradient descends method is used:

\(\begin{matrix}
{\frac{d\; \hat{\tau}}{dt} = {{- {\eta\zeta}}\frac{\partial\zeta}{\partial\hat{\tau}}}} & (5)
\end{matrix}\)

where η is the learning parameter that represents how fast and effectively a person can learn; this parameter can be learned by neural mechanisms or programmed genetically, and it indicates how fast the synapses can adjust their strength. In simulation learning, it can be measured from the subject via experiments and programmed in a simulation system.

Using Equation (3), Equation (5) can then be written in a meaningful form as shown below

\(\quad\begin{matrix}
\begin{matrix}
{\frac{d\; \hat{\tau}}{dt} = {{{- {\eta\zeta}}\frac{\partial\left\lbrack {{x\left( {t - \tau} \right)} - {x\left( {t - \hat{\tau}} \right)}} \right\rbrack}{\partial\hat{\tau}}} = {\eta \; e_{m}\frac{\partial{x\left( {t - \hat{\tau}} \right)}}{\partial\hat{\tau}}}}} \\
{= {{{\eta\zeta}{\frac{\partial{G\left( {t - \hat{\tau}} \right)}}{\partial\hat{\tau}}\left\lbrack {x_{0} + {\int_{0}^{t - \hat{\tau}}{\left( {{B(s)}\text{/}{G(s)}} \right){u(s)}{ds}}}} \right\rbrack}} -}} \\
{{{\eta\zeta}\left\{ {{{B\left( {t - \hat{\tau}} \right)}{u\left( {t - \hat{\tau}} \right)}} - {{G\left( {t - \hat{\tau}} \right)}{B(0)}{u(0)}}} \right\}}}
\end{matrix} & (6)
\end{matrix}\)

While the time delay τ can be estimated using Equation (6), there are biological constraints that need to be considered. For example, Equation (6) requires the knowledge of x(t−{circumflex over (τ)}), G(t−{circumflex over (τ)}) and u for any 0≤{circumflex over (τ)}≤t−τ. But, this is impossible because it needs to store the full history of motor commands u(t) or all functions including G(t) and x(t). Therefore, assuming the biological plausibility of Equation (6) without boundedness assumptions on the maximum delay τ is not possible.

Thus, in order to guarantee stability and limit memory usage, the condition τ≤τmax is added, where τmax is the maximum possible delay after which the system becomes inoperable. This condition does not limit the generality of the method provided herein. Furthermore, this condition is reasonable because most human movements are either repetitive, e.g., walking, or intermittent with many pauses, e.g., reaching. In reaching, for example, at the beginning of the movement, the initial position of the arm is known, and the delay is not an issue because the arm is at rest. At the end of the movement, the arm is coming back to rest and the final state of the arm is known. Therefore, delays have no detrimental effects. However, during motion, the state of the arm keeps changing which causes the values communicated to the brain affected by variable delays. It is during the arm's motion that the delay estimation is paramount. Since movements are finite in time, applying a limit on the maximum number of delays is also reasonably justified.

In some embodiments, the history of constructed signals can be stored in a finite buffer for the purpose of hardware implantation. Similarly, the brain automatically stores history of signals such as u(t) (motor commands) and x(t) (actual sensory state) by, for example, learning the dynamics of G(t) and B(t) and thereby computing the dynamics of x and u for any time period. If in a computer system, these quantities can be stored in, for example, a hard drive, RAM, or other computer-readable storage media. If in the brain, then they can be stored in, for example, a network of neurons and synapses.

In accordance with embodiments provided herein, it is assumed that the brain stores u(t) from t to t−τmax, as well as G(t), B(t) and x. In the case that the time delay exceeds τmax, a complete open-loop control prevails.

### Predicting Current and Future Sensory States

Advantageously, the model provided herein can simulate and explain the predictive nature of a primate subject's sensorimotor system as demonstrated by, for example, the smooth pursuit system and the ability to compensate for long delays. In some embodiments, the model can also predict the future state of a sensorimotor system based on the system's delayed state and an estimate of the time delay using Equation (6) and boundary conditions provided herein. Specifically, by combining Equations (3) and (4) as follows

\(\begin{matrix}
{{x(t)} = {{{G(t)}{G^{- 1}\left( {t - \tau} \right)}{x\left( {t - \tau} \right)}} + {{G(t)}{\int_{t - \tau}^{t}{{B(s)}{G^{- 1}(s)}{u(s)}{{ds}.}}}}}} & (7)
\end{matrix}\)

the future state can be predicted using the time-delay estimate {circumflex over (τ)}

\(\begin{matrix}
{{\hat{x}(t)} = {{{G(t)}{G^{- 1}\left( {t - \hat{\tau}} \right)}{x\left( {t - \hat{\tau}} \right)}} + {{G(t)}{\int_{t - \hat{\tau}}^{t}{{B(s)}{G^{- 1}(s)}{u(s)}{{ds}.}}}}}} & (8)
\end{matrix}\)

Importantly, x(t−τ) is the variable that can be measured and delivered to the sensorimotor plant model in the brain, represented by Equation (4). However, G(t) and the integral over u(t) are both dependent on the estimate of the time delay {circumflex over (τ)}. When the error in the estimate of time delay ε={circumflex over (τ)}−τ decreases to zero, the predicted state approaches to the actual state x(t).

The variable that represents motor commands, namely u(t), combines the sensorimotor plant model (“Plant” in FIG. 1) with the motor controller (“Controller” in FIG. 1). As provided herein, the plant model symbolizes a higher level of sensorimotor system. In the case of hVOR, the plant model includes the eye, associated muscles, sensor, responses, goals, and objectives (e.g., to minimize retinal sip).

In order to calculate u(t), the difference between the desired sensory goal r(t) and current state x(t), i.e., the performance error e(t)=r(t)−x(t) must be calculated first, and then the estimated performance error ê(t)=r(t)−{circumflex over (x)}(t). Then, the proportional-integral-derivative (PID) controller input can be calculated in terms of the estimated error as [31, 32]:

\(\begin{matrix}
{{u(t)} = {{K_{P}{\hat{e}(t)}} + {K_{D}\frac{d{\hat{e}(t)}}{dt}} + {K_{I}{\int_{0}^{t}{{\hat{e}(s)}{ds}}}}}} & (9)
\end{matrix}\)

and the optimal feedback controller as

u(t)=Kê(t)  (10)

where KP, KD, KI and K are proportional gain, derivative gain, integral gain, and optimal gain, respectively.

The PID controller and the optimal feedback controller gains can be designed as if there was no delay with information about the predicted state. Because the controller depends on the estimated performance error ê(t) that results from the estimated current sensory state {circumflex over (x)}(t), as the estimated {circumflex over (x)}(t) converges to x(t), ê(t) converges to e(t).

In some embodiments, simulation experiments are used to show how the model can explain a sensorimotor system's ability to compensate for delays during online learning and control. Specifically, examples are provided to demonstrate the benefits of the time-delay estimation and prediction model and the application of the model to simulate a horizontal Vestibulo-Ocular Reflex (hVOR) system (see Example).

Importantly, without the time-delay estimate and sensory state predictor built into the model, the hVOR is unstable and can be affected by high frequency oscillations (see, for example, FIGS. 2A and 2B). Specifically, FIGS. 2A and 2B show a poor response of the eye rotation to head rotation with traditional controller. Because the eye is responding to a delayed head velocity, velocity of the eye (blue solid line) is oscillating around the head velocity (red dashed line) (FIG. 2B). This oscillatory behavior is as if the eye is executing a corrective movement (saccades) to compensate for the delayed head velocity. However, it often overshoots the target head velocity. This oscillatory behavior continues until the hVOR fails to do its job completely.

These oscillations are reminiscent of a fast correction mechanism, e.g., a saccade of events used to compensate for hVOR delays. This suggests that, on one hand, a hVOR system with impaired time-delay estimation and/or impaired sensory state predictor can mimic certain outcomes of sensorimotor diseases. On the other hand, if the control of a hVOR is augmented with the time-delay estimator and/or the predictor for eye position relative to the head as provided herein, the hVOR control is stable and smooth.

Behavior similar to that shown in FIGS. 2A and 2B could also be the result of a damaged sensory state predictor. In this case, even if the time-delay estimation is working properly the state predictors fails to predict the correct current state. As a result, the hVOR will be plagued with oscillations and instability. Thus, in some embodiments, the model provided herein can also be used to detect faulty sensorimotor systems resulted from neurological disorders affecting the brain or the eye. Non-limiting examples of neurological disorders affecting the brain include autism [28], Parkinson's disease, Alzheimer's disease, an epilepsy [29].

The methods and processes described herein can be embodied as code and/or data. The software code and data described herein can be stored on one or more computer-readable media, which may include any device or medium that can store code and/or data for use by a computer system. When a computer system reads and executes the code and/or data stored on a computer-readable medium, the computer system performs the methods and processes embodied as data structures and code stored within the computer-readable storage medium.

It should be appreciated by those skilled in the art that computer-readable media include removable and non-removable structures/devices that can be used for storage of information, such as computer-readable instructions, data structures, program modules, and other data used by a computing system/environment. A computer-readable medium includes, but is not limited to, volatile memory such as random access memories (RAM, DRAM, SRAM); and non-volatile memory such as flash memory, various read-only-memories (ROM, PROM, EPROM, EEPROM), magnetic and ferromagnetic/ferroelectric memories (MRAM, FeRAM), and magnetic and optical storage devices (hard drives, magnetic tape, CDs, DVDs); network devices; or other media now known or later developed that is capable of storing computer-readable information/data. Computer-readable media should not be construed or interpreted to include any propagating signals. A computer-readable medium of the subject invention can be, for example, a compact disc (CD), digital video disc (DVD), flash memory device, volatile memory, or a hard disk drive (HDD), such as an external HDD or the HDD of a computing device, though embodiments are not limited thereto. A computing device can be, for example, a laptop computer, desktop computer, server, cell phone, or tablet, though embodiments are not limited thereto.

Advantageously, models, methods, and systems provided herein can lead to a better understanding of the function of the human sensorimotor cortex, with practical applications in explaining the mechanisms underlying neurological disorders manifested as delays and faults affecting the brain (e.g., autism [28], Parkinson's disease, Alzheimer's disease, epilepsy [29]) and the eye. Furthermore, the technology provided herein can be used to model behavior of a healthy sensorimotor system (e.g., parts or whole of a healthy brain) based on faulty information received from the system's neurons.

The models, methods, and systems provided herein can be used to address sensory brain diseases, such as the one explained in reference [34], which is hereby incorporated by reference herein in its entirety (see, e.g., FIG. 3 of Reference [34]). The results provided in the Example below are like real data for a patient with this disease. Also, models, methods, and systems provided herein can be used, for example, to implement a correction tool through eye glasses to help patients with eye diseases. A patient can wear a virtual glass set of eye glasses with capability of measuring eye movement and/or head movement and measure the amount of delay. Then, the measurement can be used to stimulate sensory neurons to make them faster, and such virtual reality eye glasses can be used to show images (e.g., coming from a camera) with delay to relieve patient problems.

A greater understanding of the present invention and of its many advantages may be had from the following example, given by way of illustration. The following example is illustrative of some of the methods, applications, embodiments and variants of the present invention. They are, of course, not to be considered as limiting the invention. Numerous changes and modifications can be made with respect to the invention.

### Example 1

The time-delay estimation model provided herein was applied to simulate the vestibulo-ocular reflex (VOR) sensorimotor system. The model was implemented in MATLAB R2013a.

In the horizontal VOR (hVOR), x∈ is the eye position relative to the head, and u∈ is the net motor-neuron signal to the horizontal eye muscles. So, the hVOR system equation in its simplest form [1] is shown as:

\(\begin{matrix}
{\overset{.}{x} = {{{- \frac{\kappa}{\rho}}x} + {\frac{1}{\rho}u}}} & (11)
\end{matrix}\)

where κ is the coefficient of viscosity and ρ is the coefficient of elasticity, and both are constants. The retinal-image slip velocity is y∈, which is the sum of eye and head velocities,

y={dot over (x)}+{dot over (h)}  (12)

The goal of the hVOR is to make the retinal slip equal to zero, i.e., y=0. Here, the reference signal r is r=−h and the feedback error signal is e=x−r=x+h. Therefore, y=ė and the feedback control law is basically a derivative control given by

u(t)=KDė(t)  (13)

Choosing the appropriate KD results in ė=y=0.

With sensory delay τ, the measured state of the hVOR control system will be x(t−τ) instead of x(t), which is a form of time-delay estimation and a plant state predictor.

Based on the model provided herein, the time-delay estimator can be written as

\(\begin{matrix}
{\overset{.}{\hat{\tau}} = {{\frac{\eta}{\rho}{\zeta \left\lbrack {e^{{- {({\kappa/\rho})}}{({t - \hat{\tau}})}}\left( {{\rho \; x_{0}} + {\int_{0}^{t - \hat{\tau}}{e^{{- {({\kappa/\rho})}}{({s - \hat{\tau}})}}{u(s)}{ds}}}} \right)} \right\rbrack}} - {\frac{\eta}{\rho}\zeta \; {u\left( {t - \hat{\tau}} \right)}}}} & (14)
\end{matrix}\)

where it is assumed that u(0)=0. The state predictor can be found as

\(\begin{matrix}
{{\hat{x}(t)} = {{e^{{({\kappa/\rho})}\hat{\tau}}{x\left( {t - \tau} \right)}} + {\frac{e^{{- {({\kappa/\rho})}}t}}{\rho}{\int_{t - \hat{\tau}}^{t}{e^{{({\kappa/\rho})}s}{u(s)}{ds}}}}}} & (15)
\end{matrix}\)

Without time-delay estimation and prediction, the hVOR is unstable and could be affected by high frequency oscillations (see, for example, FIGS. 2A and 2B). These oscillations are reminiscent of a fast correction mechanism, e.g., a saccade to compensate for hVOR delays [33].

When compared with prior art findings [34], the simulation result shown in FIGS. 2A and 2B clearly demonstrates that the hVOR system with impaired time-delay estimation or impaired sensory state predictor can mimic certain outcomes of sensorimotor diseases. However, if the control of hVOR is augmented with a time-delay estimator (FIG. 4) and a predictor for eye position relative to the head, then hVOR control is stable and smooth (see FIGS. 3A and 3B). Specifically, FIGS. 3A and 3B demonstrate the hVOR performance under long time delay (10 ms) simulated using the model provided herein. The hVOR system is stable when the brain model is equipped with time-delay estimator and state predictor.

It should be understood that the examples and embodiments described herein are for illustrative purposes only and that various modifications or changes in light thereof will be suggested to persons skilled in the art and are to be included within the spirit and purview of this application.

All patents, patent applications, provisional applications, and publications referred to or cited herein (including those in the “References” section) are incorporated by reference in their entirety, including all figures and tables, to the extent they are not inconsistent with the explicit teachings of this specification.

