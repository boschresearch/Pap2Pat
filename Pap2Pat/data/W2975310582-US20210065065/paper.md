# INTRODUCTION

Machine learning algorithms are a useful tool for system analytics applications such as diagnosis and prognostics. They are robust to system complexity but agnostic to the source of the training data. In addition, they typically require more complex models, e.g., neural networks (NN) with many layers. In many applications, we do have at least some partial knowledge about the system from which the training data originates. In several of our previous commercial projects Ion Matei et al. This is an open-access article distributed under the terms of the Creative Commons Attribution 3.0 United States License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

we encountered exactly this case: we had access to the specifications of only a subset of the system components due to proprietary reasons (Matei, Ganguli, Honda, & de Kleer, 2015). If full information about the system is available, a plethora of model-based methods for diagnosis and prognosistics can be used (de Kleer, Mackworth, & Reiter, 1992), (Gertler, 1998), (Isermann, 2005), (Patton, Frank, & Clark, 2000). These methods require some prior information about the fault rates, do not always scale with the system complexity and they work well for particular classes of systems. For example, Kalman filter-based methods (Kalman, 1960) are optimal for linear systems with Gaussian noise. Machine learning methods based on classifiers are more robust to system complexity, but they ignore the relations that exist in the data due to the physical laws governing the behavior of the system.

In this paper we discuss how (partial) knowledge about the system can be integrated in the classifier learning process. We focus on classification problems as they are suitable for diagnosis purposes. We address two main challenges: (i) representation and integration of the unknown behavior, and (ii) design of a training algorithm that considers the partial system knowledge. To address these challenges we build upon our previous work on learning acausal components in partially known physical systems (Matei, de Kleer, & Minhas, 2018). Unlike causal systems, their components do not have a fixed notion of inputs and outputs. They are characterized by ports through which energy is exchanged between components. Component behaviors are described by constitutive equations in terms of port and internal variables. The system behavior emerges from the composition of individual component behaviors through port connections. Acausal systems are typically represented as differential algebraic equations (DAEs). Under certain conditions, by employing index reduction techniques, they can be transformed into ordinary dif-ferential equations (ODEs) and solved using standard ODE solvers.

We address the first challenge (i) by bringing the system of equations into a block-lower-triangular (BLT) form. This form describes the causal relations between component variables: the equations from which variables are computed, and what variables need to be computed first in order to compute other variables. Hence, we can derive an input-output representation (e.g., a regression model, or a recurrent NN) to represent the unknown behavior, and more importantly we can compose this representation with the rest of the known components. The second challenge (ii) is addressed by showing that a cross-entropy optimization problem used for learning a classifier can be expressed as a set of regression problems in terms of the parameters of the model representing the unknown behavior, followed by a simpler classifier learning. Our approach amounts to deriving a formal approach to integrating partial system knowledge in classification-based diagnosis.

Paper structure: Section 2 describes the acausal model representation, the implications of a partially known model and the classification problem formulation. Section 3 presents the representation of the classifier in the full and partial model knowledge. Section 4 shows an illustrative example.

# PROBLEM SETUP

Our objective is to diagnose faults in a physical system. The nominal and the fault behaviors represent different operation modes. By diagnosing a fault we mean identifying an operation mode.

## Model representation

We assume that the behavior of the physical system is described by a hybrid differential algebraic equation (DAE). The typical mathematical model for describing the behavior of the system is

where x is the state vector, u is the vector of inputs, and w and v are process and measurement noise, respectively. The system output is denoted by y and θ is a variable that sets the mode of operation and takes values in the discrete set {1, 2, . . . , M }. It is sometimes more beneficial to work with discrete dynamics of the form

which can be obtained through approximations of the continuous dynamics, e.g., by approximating the state derivatives.

An example of an electric circuit whose behavior is described by a hybrid DAE is shown in Figure 1. The circuit has two In the nominal mode, the behavior of the system is given by

while in the fault mode we have

Note that the two set of equations describe two DAEs. However, by simple substitutions they can be converted into ODEs. For example the fault mode equation takes the form

We often prefer to preserve the algebraic equations as they can give us key insights into the behavior of specific components.

## Partially known behavior

In an ideal case, we know both the topological and behavioral representation of the system. In real scenarios however, this is rarely the case as we have discovered in one of our previous diagnosis projects described in (Matei et al., 2015). One common cause for lacking full system description is incomplete technical specifications: often, even the system manufacturers do not have access to the complete list of component specifications due to proprietary reasons. In the context of this paper, partial knowledge refers to having access to the behavioral description of a subset of the system components.

We do assume that the topological description of the system is known. To make it more concrete, let the behavior of resistor R2 be unknown. How to chose acausal mathematical component models was discussed in (Matei et al., 2018). The component model must contain two connectors, each connector having a current and a potential variable. For our example these are v 2 , i 2 , v 3 and i 3 , where the indices refer to the nodes 2 and 3 in the circuit shown in Figure 1. These variables are constrained by a vector valued function

, where β is a set of unknown model parameters. To simplify the model we can assume that i 2 + i 3 = 0. Therefore we are left with finding a function f R2 : R3 → R such that f R2 (v 2 , i 2 , v 3 ; β) = 0. This is not a causal representation. We further obtain a causal representation by leveraging the BLT form of the circuit shown in Figure 2, where we assumed some mockup constitutive equation for R2 for the purpose of performing the transform. The BLT form shows that the capacitor's potentials can be interpreted as inputs for the resistor model and the current is an output. This input-output mapping is particular to this circuit though. Therefore, the causal representation for the behavior of the circuit can be chosen as

There is no systematic way to chose a particular representation. We can chose a polynomial or a NN representation. The causal block representation has the advantage that enables us to model the behavior of the unknown component using an input-output map (or an ODE with inputs and outputs). This map is parameterized by β and the parameters are learned using training data. It has one important disadvantage though. The causal model for the unknown component is not necessarily generalizable. The reason is that the behavior of the component is not actually causal. In other configurations, the component may have a different causal representation, that is, the current may act as input and the potentials as outputs.

There is an additional challenge caused by the parameters of the map. Not all of them are feasible. For example, the resistance value is always positive. A negative value will result in an unstable system. Feasibility constraints can also be learned as discussed in (Matei et al., 2018) or derived from component properties such as dissipativity1 . Alternatively, we can just ignore the existence of constraints and perform unconstrained optimization since we expect the cost function to increase significantly for unstable cases. 

## Classification problem

In the classification problem, the objective is to determine the mode θ based on a set of observations. Without loss of generality, we assume that system has no exogenous inputs.

The type of observations we consider are time series of output measurements y 0:T = {y 0 , y 1 , . . . , y T }, where y k = y(t k ) and t k are sampling instants, assumed uniform. To simplify the notation we will generically denote a sequence y 0:T by y.

We will distinguish between time series sample by using the index i, that is y (i) . We will make the following assumption.

Assumption 2.1 The mode θ does not change for the duration [0, T ] and all time series correspond to the same initial condition.

This means that each data sequence y (i) corresponds to one mode only. The classification problem involves determining the current mode of operation based on a set of observation y. It is based on a probabilistic model p(θ = n|Y = y; β), where Y is a vector-valued random variable representing the observations (feature vector). The vector β represents the parameters corresponding to the model used for describing the conditional probability distribution. For example, we can use a NN model with a softmax function at the last layer.

The classification decision is the solution of the problem arg max j {p(θ = j|Y = y)}. The parameters β are learned by minimizing the cross-entropy between two probability distributions

where H is the cross entropy defined as H(q, p) = -E q [log(p)], and the probability distribution q(θ|y) is the "ground truth", assumed known. To evaluate the expectation (17) we need the unknown distribution of Y . This distribution is approximated using the training examples, resulting in

where {y (i) } N i=1 is a set of realizations of Y (training examples). The cross-entropy can be explicitly written as

where q(θ = j|Y = y (i) ) = 1 if y (i) corresponds to mode j, and zero otherwise. In the machine learning community, the solution of Eq. ( 17) is typically obtained by using gradient descent algorithms, e.g., stochastic gradient descent, Adams (Kingma & Ba, 2014) or RMSProp (Ruder, 2016). The learning algorithm does not use any information about the origin of the data, or what information may be known about the system that generated it. One immediate consequence is that we may require a complex model for p(θ|Y ; β), and hence a large number of parameters to learn. This in turn induces the need for large training data sets. Another consequence is that we ignore relations that exist between the elements of the feature vectors. Such relations originate from the physical laws governing the behavior of the physical system.

# CLASSIFIER TRAINING THAT INCLUDES INFORMA-TION ABOUT THE SYSTEM

We distinguish two cases concerning what is known about the system generating the observations: (i) complete knowledge, and (ii) partial knowledge.

## Complete knowledge

In this scenario, a complete model of the physical system is available. This model accurately describes the behavior of the system up to some process and measurement noises. The objective is to find a representation of the probability p(θ|y). Using Bayes's rule, this probability can be expressed as

The computation of the probability p(θ = j|Y = y) can be done using the model of the system. Using the discrete dynamics shown in Eq. ( 3)-( 4), we have

The probability p(y T |x T , θ = j) is completely determined by the sensing model described by Eq. ( 4) and the distribution of the measurement noise v T . In the case v T is an additive Gaussian noise, p(y

is the prediction step in the state estimation procedure. It can be expressed in terms of the update step:

The probability p(x T |x T -1 , θ = j) is determined by the process model defined by Eq. ( 3) and by the distribution of the process noise w T -1 . The probability p

is the update step in the state estimation process. Therefore, we require M state estimation filters run in parallel, for each mode of operation. The complexity of evaluating the iterative convolution operations involving the probabilities at the prediction and update steps depend on the type of model. For linear systems with Gaussian noise these probabilities are Gaussian with statistics computed using the Kalman filter (Kalman, 1960) equations. For nonlinear systems, extensions of the Kalman filter such as the extended or unscented Kalman filter may be an option. Alternatively, provided sufficient computational resources are made available, we can use the particle filter (Arulampalam, Maskell, & Gordon, 2002). If unknown, the probability p(θ = j) can compute as proxy using the training examples. Namely, we have

). Alternatively, we can solve an optimization problem of the form defined by expression ( 17) with respect to the probabilities p(θ = j). We can model these probability using a softmax function, p(θ = j) = e η j M l=1 e η l , and solve the optimization problem with respect to parameters η j .

Figure 3 depicts the architecture of the classifier when the complete model of the system is known. It is composed of M filters that compute the probability distribution of the outputs given a mode of operation, followed by a fusion block, which determines the current model by computing the probability introduced in Eq. (20). 

## Partial knowledge

In the partial model knowledge case, the classification problem uses the same formula as in Eq. ( 20), and hence we need to evaluate the probabilities p(y|θ = j) and p(θ = j) if unknown. To evaluate p(y|θ = j) we need the complete model, which at this point is not available, since the parameterized maps modeling the unknown components are not tuned to match the observed behavior. One alternative is to augment the state of the system with the parameters of the unknown components and learn them as part of the state estimation problems. We would need to use a filter that is accurate enough for non-linear systems since the parameters may enter non-linearly in the behavioral equations. Another approach is to use an optimization based approach for learning the parameters. This fits more naturally with learning classifiers in machine learning approaches. We consider two strategies for learning the parameters of the unknown components and switching model. In the first strategy, we first learn separately the parameters of the unknown part of the system, followed by learning the switching model p(θ = j). In the second strategy we jointly learn the unknown component parameters and the switching parameters. The application of one or the other depends on particular assumptions we make. For both strategies we model the probability distribution p(y 0:T |θ = j) as a Gaussian multivariate distribution with unknown covariance matrix. Assuming independent, additive measurement noise, it is formally expressed as

where p(y i |θ j , ŷj ;

is the noise covariance matrix, and ŷi is an entry in the simulated output sequence ŷ0:T using the model in mode j; model that dependents on the unknown vector of parameters β j . If the parameters of the component are mode independent, we can use the same parameters for each mode.

### Sequential parameter learning

We make the assumption that the process noise is negligible and that the variance of the measurement noise is unknown. The variance will be estimated as part of the learning process.

For each mode j, the parameters β j are learned by solving a minimum least square error problem of the form

where index i refers to a training example, and N j is the number of training examples corresponding to mode j. Any non-linear least square optimization algorithm can be used, the numerical complexity coming from the fact that the optimization algorithm requires simulating the model at each iteration and computing the gradient of the cost function, if a gradient-based algorithm is used. To obtain analytic formulas for the gradient of the cost function, we can use the autodifferentiation feature of deep learning platforms such as Tensorflow (Abadi et al., 2015), Pytorch (Subramanian, 2018), or Autograd (Maclaurin, Duvenaud, Johnson, & Adams, 2015). All three option support loss functions that can depend on ODE solutions. They do not support DAEs though for which a causal graph representation of the gradient computation scheme is not suitable. An alternative to automatic differentiation is using DAE solvers that support sensitivity analysis (e.g., CVODES, IDAS). An example of a Python package that implements DAE solvers featuring sensitivity analysis is DAETools (Nikolic, 2016a), where sensitivities of the DAE variables with respect to the system parameters can be computed numerically, but accurately at the same time with the DAE solution. Formulating the system dynamics in a deeplearning framework enables the use of GPUs that can prove beneficial for large scale problems and for large training data sets. Once the optimization problem is executed, we can use the empirical covariance as an approximation for Σ j , namely

where ŷ(i) l are functions of β * j , the optimal parameters as produces by the optimization problem. Next, we compute the probabilities p(θ = j; η). For this part we follow the same idea as in Section 3.1, where we solve an optimization problem shown in expression (17), in terms of a parameterized model p(θ = j; η). The sequential learning algorithm is summarized in Algorithm 1. One drawback of this approach is that any errors accumulated while learning parameters β j will affect the mode switching part of the algorithm. We address this in the second strategy.

Algorithm 1 Sequential learning 1: for j = 1 : M do 2:

Learn offline the parameters for the unknown components in mode j β * j = arg min

Estimate the error covariance matrix covariance matrix 

### Joint parameter learning

Here we assume that the variance of the measurement noise Σ j is known and hence we do not need to estimate it. This is the case when the precision of the sensors is available.

We maintain the same assumptions on the sensing model that induces a Gaussian distribution for the random vector y 0:T |θ = j. This way we can formulate an optimization problem where both the parameters of the unknown components and the switching parameters can be estimated simultaneously. This classification approach is summarized in Algorithm 2. As usual with non-convex optimization problems, convergence to the global minima is not guaranteed. Still, it is usually the case that the cost function has a rich set of local minima that provide satisfactory prediction accuracy.

# ILLUSTRATIVE EXAMPLE

To showcase our approach, we develop a diagnosis engine for detecting and isolating faults in a rail switch system. We consider a set of faults for which we build a hybrid classifier that uses that partial system knowledge and a NN-based classifier, for comparison purposes.

Algorithm 2 Joint learning 1: Solve offline the optimization problem

q(θ = j|y The first step in learning a model for the rail is choosing a representation that is compatible with the rest of the model: it must have an interface (port or connector) compatible with the mechanical domain. The interface is characterized by two variables: a flow variable (force) and a non-flow variable (velocity). The product between the flow and non-flow variables has the interpretation of instantaneous power. Next we choose a set of constitutive equations that constraint the interface variables. We chose to represent the map involving the interface variable as a NN. Since such a map has a input and output, the next steps is determining which is which. Following the step described in section 2.2, we use the BLT representation to determine the input and the output of the NN. Note that any map (even a linear one) is sufficient to perform the BLT transform. It should not come as a surprise that the BLT transform indicates that the force is an output. Hence, we model the rail behavior by using a causal map F = g(u; w), where g : R 3 → R is a map described by a NN with one hidden layer:

where, the input u = [x, ẋ, ẍ] is a vector containing the position, speed and acceleration, the output F is the force, and

} is the set of parameters of the map g.

## Fault modes

We consuder four fault operating modes: left and right misaligned adjuster bolts, obstacle and missing bearings. These fault modes were reported to be of interest by a rail system operator we collaborated with. Obviously there are many other fault modes of interest at the level of the point machine for example. Such faults are more readily detected due to the rich instrumentation present at the servo-motor.

Misaligned adjuster bolts: In this fault mode the bolts of the adjuster deviate from their nominal position. As a result, the instant at which the drive rod meets the adjuster (and therefore the instant at which the switch rail starts moving) happens either earlier or later. For example in a left-to-right motion, if the left bolt deviates to the right, the contact happens earlier. The reason is that since the distance between the two bolts decreases, the left bolt reaches the adjuster faster. As a result, when the drive rod reaches its final position, there may be a gap between the right switch blade and the right stock rail. In contrast, if the left bolt deviates to the left the contact happens later. The model of the adjuster includes parameters that can set the positions of the bolts, and therefore the effects of this fault mode can be modeled without difficulty. Figures 5 and6 show a comparison between the nominal behavior and the misaligned left and right bolts, respectively on the motor current and angular velocity. Missing bearings: To minimize friction, the rails are supported by a set of rolling bearings. When they become stuck or lost, the energy losses due to friction increase. A component connected to the rail was included to account for friction. This component has a parameter that sets the value for the friction coefficient. By increasing the value of this parameter, the effect of the missing bearings fault can be simulated.

Figure 7 shows a comparison between the nominal behavior and the missing bearing behavior on the motor current and angular velocity.  First we train the parameters of the rail model. Since the rail model is not directly impacted by the fault modes, we learn one single model that is valid for all modes. We chose the hidden layer dimension to be 20 for the NN modeling the rail. Hence we have a total of 100 parameters. To our knowledge, currently no deep learning platform supports DAE in the loop for the training process. The DAETools (Nikolic, 2016b) Python package does support DAE as dynamical models and enables gradient computations through sensitivity analysis. This requires though transforming the Modelica model into a form compatible with the DAETools formalism which is not a trivial process. Hence, we opted to use a gradient-free algorithm, and used a functional mockup unit (FMU) (Blochwitz et al., 2011) representation of the rail-switch model that was imported in Python and integrated in an least-square optimization process. In particular, we use Powell algorithm, which is the closest gradient-free optimization algorithm to gradient-based one. The training data corresponds to the nominal rail behavior, and consist in motor current, angle and angular velocity measurements. The inputs to the server motor are pre-designed reference signals that ensure a specific angular velocity profile for the rail. A 7 sec reference signal profile ensures the motion from left to right of the rail. A reversed reference profile, ensures the rail motion from right to left. The output measurements are time series over 14 sec, sampled at 0.05 sec time period.

Since the fault scenario does not directly affect the rail, only nominal data is used to train the rail model parameters. Using the Powell algorithm, we solved the following optimization problem:

min

subject to:

where F ( ż, z) = 0 is the DAE corresponding to the rail switch model that includes the rail representation shown in Eq. ( 26), and h(z) is the measurement model that selects the motor current, angle and angular velocity from the model variables. The variables y(t i ) and ŷ(t i ) are measured and simulated output measurements, respectively. The variances of the output prediction errors were estimated to be: 0.05, 0.74, and 0.57 for the motor current, angle and velocity, respectively.

Next we train the parameters of the classifier as described in Algorithm 1. For each of the fault modes we generated 1000 time series as training data. The fault data was generated by selecting some fault parameters and adding noise to the outputs. In particular, for the left bolt fault mode we set a deviation from its nominal value of 50 mm, for the right bolt fault mode we set a 200 mm deviation from its nominal value, for the bearing fault mode we the viscous coefficient at 5000 Ns/m, and we set an obstacle at 10 cm from the initial rail position, with a viscous coefficient equal to 10 5 Ns/m affecting the rail motion. The noise free faulty behavior corresponding to the four fault modes are shown in Figures 5678. The noise added to the outputs was chosen as zero mean Gaussian noise with variances determined by the trained model, as shown above.

We split the data into training (60%) and test (40%) data. The probabilities q(θ = j|y (i) 0:T ) follow from the time series labels: q(θ = j|y 

where Σ is a diagonal matrix with diagonal entries determined by the output noise variances, and |Σ| being the determinant of Σ. Let q ij = q(θ = j|y (i) 0:T ) and p ij = p(θ = j|y (i) 0:T ). The final step is the compute the switch parameters η j that minimizes the cross-entropy loss function:

where p ij = η j p(y   We trained a NN-based classifier using the same data set. In general, it is difficult to find the best and the most parsimonious NN architecture that generates good results. We used a trial and error process to converge to a NN architecture that gives accurate results. Using the 14 sec time series as input samples proved to be a bad idea. The 5000 sample were not enough for the ten of thousands of parameters of the NN. We recall that the number of columns of the first layer of the NN is given by the input size. Hence, we had to reduce the number of inputs. Instead of using an autoencoder which is typically greedy for data, we trained a random forest classifier and used its feature importance output to select 27 entries of the time series that contain relevant information for differentiating between the fault modes. We again employed a trial and error process to converge to the minimal number of features and a parsimonious NN architecture that is able to learn an accurate classifier. We ended up with a NN with one hidden layer of size 15 and with an output layer of size 5 that uses a softmax function as an activation function. Hence we have a total number of 500 training parameters. Although we cannot guarantee that there is no simpler NN architecture, empirically we have noticed that the prediction accuracy decreases for hidden layer sizes smaller than 15. After training the NN parameter we ended up with a classifier that has similar accuracy performance as the one shown in the previous section.

## Discussion

When including the partial model, the complexity of the classification is transferred from learning a potentially complex classifier to training a regression model for the missing com-ponent. Hence the potential to reduce complexity. The classification problem for the partial model knowledge case is much simpler and hence more easily to train. In addition, we escape the feature selection step that is typically an ad-hoc process. In addition, since we maintain the physical interpretation of the model (at least in part), there are opportunities to further investigate the consequences of faults to other system components as faults progress. That is, we can use the model for prognostics. Machine learning algorithms for prognostics are hungry for data; data that in many cases is not available. The partial model has a regularization effect on the learning algorithm, and hence it is an avenue for dealing with small data sets and limiting this way the overfitting. The classification results for both the hybrid and machine learning architecture were perfect. This is most likely due to the use of simulated data for the faults modes. Still, we expect our approach to give reasonable results on experimental data as well, using a complexity reduced classifier.

# CONCLUSIONS

In this paper we discussed the classification problem based on data generated by a partially known physical system. Unlike standard classification problems, where the classifier ignores any knowledge about the physical system, our goal was to integrated this information in the classifier design. We demonstrated that the classification problems can be converted into a set of regression problems and a set of dimensionally reduced classification sub-problems. We introduced two algorithms for learning a classifier, each one corresponding to an assumption on the measurement noise. We showcased our approach in the context of fault diagnosis for a rail switch system.

# ACKNOWLEDGMENT

This material is based upon work supported in part by the Defense Advanced Research Projects Agency (DARPA) Award HR00111890037 Physics of AI (PAI) Program.

