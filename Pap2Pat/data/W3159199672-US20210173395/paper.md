# Introduction

Deep reinforcement learning algorithms [46] are effective at learning, often from raw sensor inputs, control policies that optimize for a quantitative reward signal. Learning these policies can require experiencing millions of unsafe actions. Even if a safe policy is finally learned -which will happen only if the reward signal reflects all relevant safety priorities -providing a purely statistical guarantee that the optimal policy is safe requires an unrealistic amount of training data [24]. The difficulty of establishing the safety of these algorithms makes it difficult to justify the use of reinforcement learning in safety-critical domains where industry standards demand strong evidence of safety prior to deployment [23].

Formal verification provides a rigorous way of establishing safety for traditional control systems [5]. The problem of providing formal guarantees in RL is called formally constrained reinforcement learning (FCRL). Existing FCRL methods such as [2, 7, 10, 15-17, 19, 20, 35] combine the best of both worlds: they optimize for a reward function while safely exploring the environment.

Existing FCRL methods suffer from two significant disadvantages that detract from their real-world applicability: a) they enforce constraints over a completely symbolic state space that is assumed to be noiseless (e.g. the position of the safety-relevant objects are extracted from a simulator's internal state); b) they assume that the entire reward structure depends upon the same symbolic state-space used to enforce formal constraints. The first assumption limits the applicability of FCRL in real-world settings where the system's state must be inferred by an imperfect and perhaps even untrusted perception system. The second assumption implies a richer symbolic state that includes a symbolic representation of the reward, which we argue is unnecessary and may require more labelled data. Furthermore, this means these approaches may not generalize across different environments that have similar safety concerns, but completely different reward structures.

The goal of this paper is to safely learn a safe policy without assuming a perfect oracle that identifies the positions of all safetyrelevant objects. I.e., unlike all existing FCRL methods, we do not rely on the internal state of the simulator. Prior to reinforcement learning, we train an object detection system to extract from RGB images the 2D positions of safety-relevant objects up to a certain precision. The pre-trained object detection system is used during reinforcement learning to extract the positions of safety-relevant objects, and that information is then used to enforce formal safety constraints. Absolute safety in the presence of untrusted perception is epistemologically challenging, but our formal safety constraints do at least account for a type of noise commonly found in object detection systems. Finally, although our system (called Verifiably Safe Reinforcement Learning, or VSRL) uses a few labeled data to pre-train the object detection, we still learn an end-to-end policy that may leverage the entire visual observation for reward optimization.

Prior work from the formal methods community has demonstrated that safe RL is possible with full symbolic characterization of the environment and precise observations of the entire state. However, this is not realistic for actual robotic systems which have to interact with the physical world and can only perceive it through an imperfect visual system. This paper demonstrates that techniques inspired by formal methods can provide value even in this situation. First, we show that by using existing vision techniques to bridge between the visual input and the symbolic representation, one can leverage formal techniques to achieve highly robust behavior. Under certain assumptions on the vision system, we prove that our approach will learn safely. Second, we propose a new method of enforcing constraints which refines the environment instead of the learning algorithm. We prove that all policies are safe in this refined environment and that learning in this refined environment preserves expected rewards.

We also show that our method is capable of optimizing for reward even when significant aspects of the reward structure are not extracted as high-level features used for safety checking. Our experiments demonstrate that VSRL is capable of optimizing for reward structure related to objects whose positions we do not extract via supervised training. This is significant because it means that VSRL needs pre-trained object detectors only for objects that are safetyrelevant.

Finally, we provide a novel benchmark suite for Safe Exploration in Reinforcement Learning that includes both environments where the reward signal is aligned with the safety objectives and environments where the reward-optimal policy is unsafe. Our motivation for the latter is that assuming reward-optimal policies respect hard safety constraints neglects one of the fundamental challenges of Safe RL: preventing "reward-hacking". For example, it is fundamentally difficult to tune a reward signal so that it has the "correct" trade-off between a pedestrian's life and battery efficiency. We show that in the environments where the reward-optimal policy is safe ("rewardaligned"), VSRL learns a safe policy with convergence rates and final rewards which are competitive or even superior to the baseline method. More importantly, VSRL learns these policies with zero safety violations during training; i.e., it achieves perfectly safe exploration. In the environment where the reward-optimal policy is unsafe ("reward-misaligned"), VSRL successfully avoids "reward-hacking" by violating safety constraints, optimizing only for the subset of reward that can be achieved without violating safety constraints.

Summarily, this paper contributes: (1) VSRL, a new approach toward formally constrained reinforcement learning that makes more realistic assumptions about access to symbolic features. This approach requires minimal supervision before reinforcement learning begins and explores safely while remaining competitive at optimizing for reward. (2) a new method of enforcing safety constraints by refining the environment so all policies are safe while preserving expected rewards (3) a novel benchmark suite for safe exploration in reinforcement learning with hard constraints that includes both properly specified and mis-specified reward signals.

# Problem Definition

A reinforcement learning (RL) system can be represented as a Markov Decision Process (MDP) (S, A,𝑇 , 𝑅, 𝛾) which includes a (possibly infinite) set S of system states, an action space A, a transition function 𝑇 (𝑠, 𝑎, 𝑠 ′ ) which specifies the probability of the next system state being 𝑠 ′ after the agent executes action 𝑎 at state 𝑠, a reward function 𝑅(𝑠, 𝑎) that gives the reward for taking action 𝑎 in state 𝑠, and a discount factor 0 < 𝛾 < 1 that indicates the system preference to earn reward as fast as possible. We denote the set of initial states as S 𝑖𝑛𝑖𝑡 ⊆ S.

In our setting, S are images and we are given a safety specification safe : O → {0, 1} over a set of high-level observations O, specifically, the positions (planar coordinates) of the safety-relevant objects in a 2D or 3D space. Since S ≠ O, it is not trivial to learn a safe policy 𝜋 such that safe(O) = 1 along every trajectory. We decompose this challenge into two well-formed and tractable subproblems:

1. Pre-training a system 𝜓 : S → O that converts the visual inputs into symbolic states using synthetic data (without acting in the environment); 2. Learning policies over the visual input space S while enforcing safety in the symbolic state space O.

This problem is not solvable without making some assumptions, so here we focus on the following:

Assumption 1 (𝜖-Bounded Detection Errors). The symbolic mapping 𝜓 is correct up to 𝜖. More precisely, the true position of every object 𝑜 𝑖 can be extracted from the image 𝑠 through the object detector 𝜓 (𝑠) 𝑖 so that the Euclidean distance between the actual and extracted positions is at most 𝜖, i.e. ∀𝑖 ||𝜓 (𝑠) 𝑖 -𝑜 𝑖 || 2 ≤ 𝜖.

Assumption 1 is strong for two reasons. First, there is currently no method for verifying that an object detector has 𝜖-bounded errors. Second, there is no compelling empirical evidence that 𝜖-bounded errors provide an exhaustive model of modern object detectors' failure modes. However, without any assumption on the fault model for the vision system, safety cannot be guaranteed. Our assumption that errors are 𝜖-bounded, although not exhaustive, does capture one of the most common failure modes for all object detection algorithms. We leave exploration of more sophisticated fault models for specific object detectors as future work, and note that the parametric nature of our approach allows us to integrate more complex and specific fault models into VSRL.

Assumption 2 (Liveness of Safe Action). Initial states, described by a set of properties denoted as init, are safe, i.e. ∀𝑠 ∈ S 𝑖𝑛𝑖𝑡 : safe(𝜓 (𝑠)) = 1 . Moreover, every state we reach after taking only safe actions has at least one available safe action.

# Assumption 3 (Correctness up to Simulation of Dynamical Model).

We are given a dynamical model of the safety-relevant dynamics in the environment, given as either a discrete-time dynamical system or a system of ordinary differential equations, denoted as plant. We assume that model is correct up to simulation; i.e., if 𝑇 (𝑠 𝑖 , 𝑎, 𝑠 𝑗 ) ≠ 0 for some action 𝑎, then the dynamical system plant maps 𝜓 (𝑠 𝑖 ) to a set of states that includes 𝜓 (𝑠 𝑗 ).

For example, the model may be a system of ODEs that describes how the acceleration and angle impact the future positions of a robot, as well as the potential dynamical behavior of some hazards in the environment. Note that this model only operates on O (the symbolic state space), not S (low-level features such as images or LiDAR).

The "up to simulation" portion of our assumption is simply a technical artifact that aligns the reachability structure of the dynamical system described by a hybrid program to the probabilistic structure of the dynamical system described by a Markov decision process. Up to simulation means that if there is a non-zero probability of action 𝑎 transitioning from 𝑠 𝑖 to 𝑠 𝑗 , then there is a flow of the ODEs from the state obtained by performing action 𝑎 in state 𝑠 𝑖 , to the state 𝑠 𝑗 . That is, the assumption that this model is correct up to simulation simply means that we assume the discrete transition relation 𝑇 is a subset of the relation obtained by following the flows of the ODEs in the dynamical model.

Assumption 4 (Correctness up to Simulation of Controller). We have an abstract model of the agent's behavior, denoted as ctrl, that is correct up to simulation: if 𝑇 (𝑠 𝑖 , 𝑎, 𝑠 𝑗 ) ≠ 0 for some action 𝑎, then 𝜓 (𝑠 𝑗 ) is one of the possible next states after 𝑎(𝜓 (𝑠 𝑖 )) by ctrl.

An abstract model of the agent's behavior describes at a highlevel a safe controller behavior, disregarding the fine-grained details an actual controller needs to be efficient. An example is a model that brakes if it is too close to a hazard and can have any other type of behavior otherwise. Note that ctrl is very different from a safe policy 𝜋, since it only models the safety-related aspects of 𝜋 without considering reward optimization.

Assuming a known and correct model for both the environment and the agent up to simulation is necessary to fully characterize safe actions. This assumption is reasonable whenever accurate dynamical models of the system under control are available, which is often the case in traditional control systems. The success of model-based approaches toward controller design provides evidence for the reasonableness of this assumption. Notice that the model only needs to accurately describe safety-relevant portions of the environment's dynamics; in particular, we make no assumption about the accuracy of the plant model for potions of the state space that aren't relevant to safety. This paper assumes accurate environmental models are given; learning or repairing a model of the environment during exploration is an interesting direction for future work.

# Background

The goal of an RL agent in an environment specified by an MDP (S, A,𝑇 , 𝑅, 𝛾) is to find a policy 𝜋 that maximizes its expected total reward from an initial state 𝑠 0 ∈ S 𝑖𝑛𝑖𝑡 :

where 𝑟 𝑖 is the reward at step 𝑖. In a deep RL setting, we can use the DNN parameters 𝜃 to parametrize 𝜋 (𝑎|𝑠; 𝜃 ). One particularly effective implementation and extension of this idea is proximal policy optimization (PPO), which improves sample efficiency and stability by sampling data in batches and then optimizing a surrogate objective function that prevents overly large policy updates [45]. This enables end-to-end learning through gradient descent which significantly reduces the dependency of the learning task on refined domain knowledge. Deep RL thus provides a key advantage over traditional approaches which were bottle-necked by a manual, timeconsuming, and often incomplete feature engineering process.

To ensure formal guarantees we use differential Dynamic Logic (dL) [36][37][38]40], a logic for specifying and proving reachability properties of hybrid dynamical systems, which combine both 

where 𝑓 , 𝑔 are polynomials over the state variables, 𝜙 and 𝜓 are formulas of the state variables, ∼ is one of {≤, <, =, >, ≥}. The formula [𝛼]𝜑 means that a formula 𝜑 is true in every state that can be reached by executing the hybrid program 𝛼.

Given a set of initial conditions init for the initial states, a discrete-time controller ctrl representing the abstract behaviour of the agent, a continuous-time system of ODEs plant representing the environment and a safety property safe we define the safety preservation problem as verifying that the following holds:

Intuitively, this formula means that if the system starts in an intial state that satisfies init, takes one of the (possibly infinite) set of control choices described by ctrl, and then follows the system of ordinary differential equations described by plant, then the system will always remain in states where safe is true.

Example 1 (Hello, World). Consider a 1D point-mass 𝑥 that must avoid colliding with a static obstacle (𝑜) and has perception error bounded by 𝜖 2 . The following dL model characterizes an infinite set controllers that are all safe, in the sense that 𝑥 ≠ 𝑜 for all forward time and at every point throughout the entire flow of the ODE:

and where 𝑥 is the 1D coordinate of the point-mass under control, 𝑣 is the velocity of 𝑥, 𝑎 is the acceleration action taken by 𝑥, 𝐵 is the maximum deceleration (i.e., maximum braking force), 𝐴 is the maximum acceleration, 𝑇 is the maximum time between control decisions, 𝑡 is the time elapsed during the current control step, and 𝑜 is the 1D coordinate of the obstacle.

Starting from any state that satisfies the formula init, the (abstract/non-deterministic) controller chooses any acceleration satisfying the SB constraint. After choosing any 𝑎 that satisfies SB, the system then follows the flow of the system of ODEs in plant for any positive amount of time 𝑡 less than 𝑇 . The constraint 𝑣 ≥ 0 simply means that braking (i.e., choosing a negative acceleration) can bring the pointmass to a stop, but cannot cause it to move backwards.

The full formula says that no matter how many times we execute the controller and then follow the flow of the ODEs, it will always be the case -again, for an infinite set of permissible controllersthat 𝑥 -𝑜 > 𝜖.

Theorems of dL can be automatically proven in the KeYmaera X theorem prover [8,9]. [33] explains how to synthesize action space guards from non-deterministic specifications of controllers (ctrl), and Fulton and Platzer [10,11] explains how these action space guards are incorporated into reinforcement learning to ensure safe exploration.

## Using Safe Controller Specifications to Constrain Reinforcement Learning

Hybrid programs have a denotational semantics that defines, for each program, the set of states that are reachable by executing the program from an initial state. A state is an assignment of variables to values. For example, the denotation of 𝑥 := 𝑡 in a state 𝑠 is:

= 𝑡 Composite programs are given meaning by their constituent parts. For example, the meaning of 𝛼 ∪ 𝛽 is:

A full definition of the denotational semantics corresponding to the informal meanings given above is provided by [39].

Given a hybrid program and proven dL safety specification, Fulton and Platzer [10] explains how to construct safety monitors (which we also call safe actions filters in this paper) for reinforcement learning algorithms over a symbolic state space. In this section, we summarize their algorithm.

As opposed to our approach, Fulton and Platzer [10] employs both a controller monitor (that ensures the safety of the controller) and a model monitor (that ensures the adherence of the model to the actual system and checks for model mismatch).

The meaning of the controller monitor and model monitor are stated with respect to a specification with the syntactic form 𝑃 → [{ctrl; plant} * ]𝑄 where 𝑃 is a dL formula specifying initial conditions, plant is a dynamical system expressed as a hybrid program that accurately encodes the dynamics of the environment, and 𝑄 is a postcondition. [10] assumes that ctrl has the form ?𝑃 1 ; 𝑎 1 ∪ • • • ∪ 𝑃 𝑛 ; 𝑎 𝑛 , where 𝑎 𝑖 are discrete assignment programs that correspond to the action space of the RL agent. For example, an agent that can either accelerate or brake has action space 𝐴 = {𝐴, -𝐵}. The corresponding control program will be ?𝑃 1 ; 𝑎 := 𝐴∪?𝑃 2 ; 𝑎 := -𝐵 where 𝑃 1 is a formula characterizing when it is safe to accelerate and 𝑃 2 is a formula characterizing when it is safe to brake.

Given such a formula, [10] defines the controller and model monitors using the following conditions:  1a); 2. learning policies over visual inputs, while enforcing safety in the symbolic state space (described in Section 4.2 and shown in Figure 1c). This latter task requires a controller monitor, which is a function 𝜑 : 𝑂 × 𝐴 → {𝑇𝑟𝑢𝑒, 𝐹𝑎𝑙𝑠𝑒} that classifies each action 𝑎 in each symbolic state 𝑜 as "safe" or not. In this paper this monitor is synthesized and verified offline following [10,11]. In particular, as discussed in the previous sections, the KeYmaera X theorem prover solves the safety preservation problem presented in Eq. ( 2) for a set of high-level reward-agnostic safety properties safe, a system of differential equations characterizing the relevant subset of environmental dynamics plant, an abstract description of a safe controller ctrl and a set of initial conditions init (shown in Figure 1b).

## Object Detection

In order to remove the need to construct labelled datasets for each environment, we only assume that we are given a small set of images of each safety-critical object and a set of background images (in practice, we use 1 image per object and 1 background). We generate synthetic images by pasting the objects onto a background with different locations, rotations, and other augmentations. We then train a CenterNet-style object detector [50] which performs multi-way classification for whether each pixel is the center of an object. For speed and due to the visual simplicity of the environments, the feature extraction CNN is a truncated ResNet18 [21] which only keeps the first residual block. The loss function is the modified focal loss [29] from [26]. See Appendix A of [22] for full details on the object detector. Detection adds some run-time overhead for all environments, but many object detectors run quickly enough for real-time control. Section 4.4 contains a detailed discussion of scalability issues with object detection.

## Enforcing Constraints

While VSRL can augment any existing deep RL algorithm, this paper extends PPO [44]. The algorithm performs RL as normal except that, whenever an action is attempted, the object detector and safety monitor are first used to check if the action is safe. If not, a safe action is sampled uniformly at random from the safe actions in the current state. This happens outside of the agent and can be seen as refining the environment using a safety check. Pseudocode for 

## Safety and Learning Results

We establish two theoretical properties about VSRL. First, we show that VSRL safely explores. Second, we show that using VSRL does not interfere with optimizing for the original reward objective.

If the object detector produces an accurate mapping, then Algorithm 1 will preserve the safety constraint associated with the 𝜑 monitor. We state this property formally in Theorem 1.

Theorem 1. VSRL will remain safe if the following conditions hold along a trajectory 𝑠 0 , 𝑎 0 , . . . , 𝑠 𝑛 with 𝑠 0 ∈ S 𝑖𝑛𝑖𝑡 : A1 Initial states are safe: 𝑠 ∈ S 𝑖𝑛𝑖𝑡 implies 𝜓 (𝑠) |= init. A2 The model and symbolic mapping are correct up to simulation:

If 𝑇 (𝑠 𝑖 , 𝑎, 𝑠 𝑗 ) ≠ 0 for some action 𝑎 then (𝜓 (𝑠 𝑖 ), 𝑎(𝜓 (𝑠 𝑖 ))) ∈ ctrl and (𝜓 (𝑠 𝑖 ),𝜓 (𝑠 𝑗 )) ∈ plant .

Proof. We begin the proof by pointing out that our assumption about how init → [{ctrl; plant} * ]safe was proven provides us with the following information about some formula 𝐽 :

Now, assume 𝑠 0 , 𝑎 0 , 𝑠 1 , 𝑎 1 , . . . , 𝑠 𝑛 with 𝑠 0 ∈ S 𝑖𝑛𝑖𝑡 is a trajectory generated by running an RL agent with actions selected by Algorithm 1 and proceed by induction on the length of the sequence with the inductive hypothesis that 𝜓 (𝑠 𝑖 ) |= 𝐽 .

If 𝑖 = 0 then 𝑠 0 ∈ S 𝑖𝑛𝑖𝑡 by assumption. Therefore, 𝜓 (𝑠 0 ) |= init by A1. We know by LI1 that ⊢ init → 𝐽 . Therefore, 𝜓 (𝑠 0 ) |= 𝐽 by Modus Ponens and the soundness of the dL proof calculus. Now, suppose 𝑖 > 0. We know 𝜓 (𝑠 𝑖 ) |= 𝐽 by induction. Furthermore, we know 𝑇 (𝑠 𝑖 , 𝑎 𝑖 , 𝑠 𝑖+1 ) ≠ 0 because otherwise this trajectory could not exist. By A2 and the denotation of the ; operator, we know (𝜓 (𝑠 𝑖 ),𝜓 (𝑠 𝑖+1 )) ∈ ctrl; plant . By LI3, we know ⊢ 𝐽 → [ctrl; plant] 𝐽 Therefore, 𝜓 (𝑠 𝑖 ) |= 𝐽 and (𝜓 (𝑠 𝑖 ),𝜓 (𝑠 𝑖+1 )) ∈ ctrl; plant implies 𝜓 (𝑠 𝑖 + 1) |= 𝐽 by the denotation of the box modality and the soundness of dL.

We have now established that 𝜓 (𝑠 𝑖 ) |= 𝐽 for all 𝑖 ≥ 0. By LI2, Modus Ponens, and soundness of the dL proof calculus, we finally conclude that 𝜓 (𝑠 𝑖 ) |= safe. □

Note that if all actions 𝑎 𝑖 along the trajectory are generated using Algorithm 1, and if the model is accurate, then A2 will hold.

### Learning with Safety.

In order to enforce safety, we refine the original environment to create an environment without unsafe actions. By not modifying the agent or training algorithm, any theoretical results (e.g. convergence) which the algorithm already has will still apply in our safety-refined environment, provided these do not rely on specific properties of the original MDP. However, it is still necessary to show the relation between the (optimal) policies that may be found in the safe environment and the policies in the original environment. We show that 1) all safe policies in the original environment have the same transition probabilities and expected rewards in the refined environment and 2) all policies in the refined environment correspond to a policy in the original environment which has the same transition probabilities and expected rewards. This shows that making progress (finding a policy with higher expected reward) in the safe environment leads to an equivalent amount of progress in the original environment. In particular, the optimal policies in the safe environment are optimal among safe policies in the original environment.

Let the original environment be the MDP 𝐸 = (S, A,𝑇 , 𝑅) where S is the set of states, A the set of actions, 𝑇 the transition function, and 𝑅 the reward function. Recall that we have a controller monitor 𝜑 : S × A → {𝑇 𝑟𝑢𝑒, 𝐹𝑎𝑙𝑠𝑒} such that 𝜑 (𝑠, 𝑎) is 𝑇𝑟𝑢𝑒 if taking action 𝑎 is safe in state 𝑠 in 𝐸 and 𝐹𝑎𝑙𝑠𝑒 otherwise (for simplicity, we won't worry about extracting symbolic states from visual observations here; that can be seen as happening inside of 𝜑). When we refer to an action as safe or unsafe, we always mean in the original environment

The safety-refined environment will be 𝐸 ′ = (S, A,𝑇 ′ , 𝑅 ′ ) where the transition and reward functions will be modified to ensure 1) there are no unsafe actions and 2) expected rewards in 𝐸 ′ correspond with those from acting safely in 𝐸.

For actions that are safe in 𝑇 , we keep 𝑇 ′ identical. For actions that are unsafe in 𝑇 , we modify their effects in 𝑇 ′ to be the same as taking a safe action in 𝑇 . Without prior knowledge about which safe actions are better, we have 𝑇 ′ emulate the effects of uniformly sampling a safe action and following 𝑇 . Thus we set

if 𝜑 (𝑠, 𝑎) 𝑅 ′ is defined similarly so that it simulates the reward achieved by replacing unsafe actions with safe ones uniformly at random:

For every safe policy 𝜋 in E, following that policy in 𝐸 ′ leads to the same transitions with the same probabilities and gives the same expected rewards.

Proof. By definition of safety, 𝜋 has zero probability for any (𝑠, 𝑎) where 𝜑 (𝑠, 𝑎) isn't true. Thus actions sampled from 𝜋 lead to transitions and rewards from the branch of 𝑇 ′ and 𝑅 ′ where they are identical to 𝑇 and 𝑅. □ Lemma 2. For every policy 𝜋 ′ in 𝐸 ′ there exists a safe policy 𝜋 in 𝐸 such that 𝜋 ′ has the same transition probabilities and expected rewards in 𝐸 ′ as 𝜋 does in 𝐸.

Proof. For any 𝜋 ′ in 𝐸 ′ , let 𝑔(𝜋 ′ ) = 𝜋 be defined such that

where A 𝜑 (𝑠) = {𝑎 ∈ A | ¬𝜑 (𝑠, 𝑎)} is the set of unsafe actions in state 𝑠. This evenly redistributes the probability that 𝜋 ′ assigns to actions which would be unsafe in 𝐸 among the safe actions.

We show first that the transition probabilities of 𝜋 in 𝐸 and 𝜋 ′ in 𝐸 ′ are the same.

Let E 𝜋,𝐸 [𝑅 𝑠 ] be the expected reward of following the policy 𝜋 in environment 𝐸 at state 𝑠. The equality of the expected reward for 𝜋 in every state of 𝐸 and 𝜋 ′ in every state of 𝐸 ′ can be shown similarly:

𝜋 ′ (𝑎|𝑠)𝑅(𝑠, 𝑎)

𝜋 ′ (𝑎|𝑠)𝑅(𝑠, 𝑎)

Running Algorithm 1 on 𝐸 produces 𝐸 ′ , where 𝐸 ′ is as defined at the beginning of this section.

Proof. Trivial. □ Theorem 2. Let E 𝜋,𝐸 [𝑅] be the expected reward of following policy 𝜋 in environment 𝐸. Given two policies

# Proof. Trivial by Lemma 2 which gives us that

for any 𝜋 ′ . □ Theorem 3. Any optimal policy in 𝐸 ′ is optimal among the safe policies in 𝐸.

Proof. Let 𝜋 ′ * be an optimal policy in 𝐸 ′ and 𝜋 * be optimal among the safe policies in 𝐸. By Lemma 1, we know that the expected reward of 𝜋 * in 𝐸 ′ is the same as in

Theorem 3 shows that we can find the optimal policy in 𝐸 by learning the optimal policy in 𝐸 ′ . Theorem 2 means that any progress we make in finding a better policy in 𝐸 ′ translates to an equivalent amount of progress at optimizing for the objective in 𝐸. These results show that using 𝐸 ′ to safely learn a policy that optimizes reward in 𝐸 is reasonable.

A few notes regarding this approach:

• The intuitive approach to making an agent safe, if we know the set of safe actions in each state, might be to sample from the safe subset of the agent's policy distribution (after renormalization). Because this is not actually sampling from the distribution the agent learned, this may interfere with training the agent. • While we keep S the same in 𝐸 and 𝐸 ′ , there may be states which become unreachable in 𝐸 ′ because only unsafe transitions in 𝐸 lead to them. Thus the effective size of 𝐸 ′ 's state space may be smaller which could speed up learning effective safe policies. • Our approach can be viewed as transforming a constrained optimization problem (being safe in 𝐸) into an unconstrained one (being safe in 𝐸 ′ ).

## Scalability of VSRL

There are three sources of scalability concerns in VSRL: object detection, offline verification, and online controller monitoring. We use neural networks for object detection. Fast and real-time inference for neural networks operating on rich visual inputs is an active line of research. Note that many object detection papers do achieve excellent results on very complex visual environments including in 3D environments. For example, there are many object detection methods that are designed to run at over 100 frames per second. In this work we use CenterNet, which runs in between 52 and 142 frames per second (depending on the amount of preprocessing, the number of passes, the resolution of the input images, etc.). Centernet works on real world images.

A second source of scalability challenges is in offline verification of safety-relevant dynamics (Box b in Figure 1). The models that this paper are based on were verified by writing Bellerophon tactics in KeYmaera X [8]. The work in this paper assumes an a priori verified hybrid systems model. Naturally, applying this work to different environment requires first building and verifying a model of the environment. Verifying hybrid systems is undecidable in theory and difficult in practice.

Given a verified model, constraint checking is not a source of scalability issues. A larger state-space or 3-dimensional environment would have minimal impact on constraint checking at runtime due to the nature of the runtime monitors extracted from KeYmaera X. These monitors are quantifier-free formulas of real arithmetic; therefore, checking that the monitor evaluates to true in a specific state and for a given action involves simply evaluating a single boolean expression. The size of this safety check grows linearly in the number of types of objects, these checks are trivially parallelizable, and the constant time is quite small as it only requires plugging into and evaluating one quantifier-free expression.

Although checking constraints is not a significant source of scalability challenges, sampling points from an arbitrary set such that those points match the safety constraint can be challenging. In all of the environments considered in this paper, the action space constraints are simple enough that we can explicitly characterize the set of safe actions in each state and sample uniformly from that set. However, in environments with more complex constraints, efficiently sampling from arbitrary semi-algebraic sets becomes an important algorithmic consideration.

# Experimental Validation of VSRL

We evaluate VSRL on four environments: a discrete XO environment [13], an adaptive cruise control environment (ACC), a 2D goal-finding environment (GF) similar to the Open AI Safety Gym Goal environment [43] but without a MuJoCo dependency and with simpler dynamics, and a pointmesses environment that emphasizes the problem of preventing reward hacking in safe exploration systems (PM). VSRL explores each environment without encountering any unsafe states.

The XO Environment is a simple setting introduced by [13] for demonstrating symbolic reinforcement learning algorithms (the implementation by Garnelo et al. [13] was unavailable, so we reimplemented this environment). The XO environment, visualized in Figure 2(a), contains three types of objects: X objects that must be collected (+1 reward), O objects that must be avoided (-1 reward), and the agent (marked by a +). There is also a small penalty (-0.01) at each step to encourage rapid collection of all Xs and completion of the episode. This environment provides a simple baseline for evaluating VSRL. It is also simple to modify and extend, which we use to evaluate the ability of VSRL to generalize safe policies to environments that deviate slightly from implicit modeling assumptions. The symbolic state space includes the position of the + and the O, but not the position of the Xs because they are not safety-relevant. The purpose of this benchmark is to provide a benchmark for safe exploration in a simple discrete setting.

The remainder of our experimental environments consider control of a point mass in 1D or 2D space. We extract positions from RGB images, and also assume independent sensors for both velocity and heading of the agent, so that these values do not have to be inferred from visual inputs. Inferring this information from visual inputs is possible, but assuming separate sensors for velocity and heading is reasonable.

The adaptive cruise control (ACC) environment has two objects: a follower and a leader. The follower must maintain a fixed distance from the leader without either running into the leader or following too far behind. We use the verified model from [42] to constrain the agent's dynamics.

The 2D goal-finding environment consists of an agent, a set of obstacles, and a goal state. The obstacles are the red circles and the goal state is the green circle. The agent must navigate from its (random) starting position to the goal state without encountering any of the obstacles. Unlike the OpenAI Safety Gym, the obstacles are hard safety constraints; i.e., the episode ends if the agent hits a hazard. We use the verified model from [32] to constrain the agent's dynamics.

The 2D pointmesses environment consists of an agent, a set of obstacles, a goal state, and a set of pointmesses (blue Xs). The agent receives reward for picking up the pointmesses, and the episode ends when the agent picks up all messes and reaches the goal state. Unlike the 2D goal-finding environment, hitting an obstacle does not end the episode. Instead, the obstacle is removed from the environment and a random number of new pointmesses spawn in its place. Notice that this means that the agent may reward hack by taking an unsafe action (hitting an obstacle) and then cleaning up the resulting pointmesses. We consider this the incorrect behavior. We use the verified model from [32] to constrain the agent's dynamics.

We compare VSRL to PPO using two metrics: the number of safety violations during training and the cumulative reward. These results are summarized in Table 2. VSRL is able to perfectly preserve safety in all environments from the beginning of training even with the 𝜖-bounded errors in extracting the symbolic features from the images. In contrast, vanilla PPO takes many unsafe actions while training and does not always converge to a policy that entirely avoids unsafe objects by the end of training.

In some environments, preserving safety specifications also substantially improves sample efficiency and policy performance early in the training process. In the ACC environment, in particular, it is very easy to learn a safe policy which is reward-optimal. In the GF and PM environments, both the baseline agent and the VSRL agent struggle to learn to perform the task well (note that these tasks are quite difficult because encountering an obstacle ends the episode). However, VSRL remains safe without losing much reward relative to the amount of uncertainty in both policies.

# Related Work

Recently, there has been a growing interest in safe RL, especially in the context of safe exploration, where the agent has to be safe also during training. A naive approach to RL safety is reward shaping, in which one defines a penalty cost for unsafe actions. This approach has several drawbacks, e.g. the choice of the penalty is brittle, so a naive choice may not outweigh a shorter path to the reward, as shown by Dalal et al. [6]. Therefore, recent work on safe RL addresses the challenge of providing reward-agnostic safety guarantees for Table 2. Final reward (R; higher is better) and total number of unsafe actions (U; lower is better) on all environments. All results are the median over at least 4 replicates.

deep RL [12,47]. Many recent safe exploration methods focus on safety guarantees that hold in expectation (e.g., [1,44]) or with high probability (e.g., [3,4,6,25]. Some of these approaches achieve impressive results by drawing upon techniques from control theory, such as Lyapunov functions [3] and control barrier certificates. On the other hand, ensuring safety in expectation or with high probability is generally not sufficient in safety-critical settings where guarantees must hold always, even for rare and measure-zero events. Numerical testing alone cannot provide such guarantees in practice [24] or even in theory [41]. The problem of providing formal guarantees in RL is called formally constrained reinforcement learning (FCRL). Existing FCRL methods such as [2,7,10,15,[17][18][19][20]35] combine the best of both worlds: they optimize for a reward function while still providing formal safety guarantees. While most FCRL method can only ensure the safety in discrete-time environments known a priori, Fulton and Platzer [10,11] introduce Justified Speculative Control, which exploits Differential Dynamic Logic [39] to prove the safety of hybrid systems, systems that combine an agent's discrete-time decisions with a continuous time dynamics of the system.

A major drawback of current FCRL methods is that they only learn control policies over handcrafted symbolic state spaces. Relative to Fulton and Platzer [10,11], our primary contribution is that we learn end-to-end policies instead of assuming that an oracle extracts a state-space from visual inputs. This has two advantagesunlike the approach in Fulton and Platzer [10,11], VSRL considers the challenge of imperfect perception and is able optimize for latent features that are not in the symbolic safety model's state space. Similarly, while many methods extract a symbolic mapping for RL from visual data, e.g. [13,14,27,28,30,31,48,49], they all require that all of the reward-relevant features are explicitly represented in the symbolic space. As shown by the many successes of Deep RL, e.g. [34], handcrafted features often miss important signals hidden in the raw data.

Our approach aims at combining the best of FCRL and end-to-end RL to ensure that exploration is always safe with formal guarantees, while allowing a deep RL algorithm to fully exploit the visual inputs for reward optimization.

# Conclusion and Discussions

Safe exploration in the presence of hard safety constraints is a challenging problem in reinforcement learning. We contribute VSRL, an approach toward safe learning on visual inputs. Through theoretical analysis and experimental evaluation, this paper establishes that VSRL maintains perfect safety during exploration while obtaining comparable reward. Because VSRL separates safety-critical object detection from RL, next steps should include applying tools from adversarial robustness to the object detectors used by VSRL.

