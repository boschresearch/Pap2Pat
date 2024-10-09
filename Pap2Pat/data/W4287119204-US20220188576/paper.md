# Introduction

Multi-agent reinforcement learning (MARL) has been applied to increasingly challenging domains such as Starcraft Vinyals et al. [2017] and DOTA OpenAI [2018]. In Hide-and-Seek Baker et al. [2019], MARL has been shown to produce complex emergent behavior, including the use of tools in order to accomplish goals. In many domains, it is possible for agents to communicate with each other over a network. By doing so, agents can discover performant joint strategies for achieving a shared goal.

In most real-world settings, communication must happen under constraints of bandwidth, power capacity, etc. In such settings, communicating agents have a dual objective -minimize communication and maximize a task objective. These opposing objectives create a challenging learning problem. A typical failure mode, as we observe and address in our experiments, results in agents shutting down communication at the start of learning before they have learnt to construct meaningful messages.

Prior works on learning efficient communications have significant limitations (more details in Section 2). In this work, we show that learnt communication models can be trained to minimize communication while still accomplishing a cooperative task with minimal or no performance loss. Our approach, Efficient Communication Net or ECNet, directly optimizes the weighted sum of the task reward and a communication cost by learning communication gates. We experiment with two methods of training these gates: the first is to use REINFORCE Williams [1992] in a manner similar to IC3Net Singh et al. [2019], the second is to employ the Gumbel-Softmax re-parameterization trick Jang et al. [2017] .

We find that it is necessary to employ two techniques to stabilize training. First, throughout training, we alternate between using the communication penalty and training without it to avoid failure modes like early termination of communication. Second, we find it helpful to forward a message from a previous time-step if no new message is received. Applying these techniques, we find that that both REINFORCE and Gumbel-Softmax-based gates are able to achieve efficient communication.

We also observe that communication resources can be further conserved by selecting only those recipients that can benefit from a message. We extend our gating system to generate a pairwise communication mask and show that the learnt mask captures the correct connectivity structure.

In summary, our key contributions in this paper are:

• We show that we can minimize communication without loss of performance using a simple technique: jointly optimizing task reward and a communication penalty.

• We introduce two stabilization techniques that significantly improve performance.

• We show that we can also learn pairwise communication gates that capture the connectivity structure required to solve a task.

# Related Work

Multi-Agent Reinforcement Learning: Our work is related to prior applications of reinforcement learning to solve multi-agent problems. We follow works such as Bansal et al. [2018], Baker et al. [2019], OpenAI [2018], Vinyals et al. [2017], Singh et al. [2019] in parameterizing each agent's policy as a deep neural network and using a policy gradient algorithm to optimize the networks. The choice of training algorithm differs across the literature, from Proximal Policy Optimization Schulman et al. [2017] to Multiagent Deep Deterministic Policy Gradients Lowe et al. [2017] and a combination of evolutionary optimization and policy gradients Khadka et al. [2020] . Similar to Sukhbaatar et al. [2016], Singh et al. [2019], we use a fully synchronous version of the A3C algorithm Mnih et al. [2016], referred to as A2C. Our work is similar to OpenAI [2018], Singh et al. [2019], Khadka et al. [2020] in sharing parameters across the agents' networks. We focus on cooperative problems with partial observability, which requires a high degree of interaction between the agents.

Multi-Agent Reinforcement Learning with Communication: Prior work Lowe et al. [2017], Sukhbaatar et al. [2016], Das et al. [2019] has shown that multi-agent reinforcement learning performance can be significantly improved by allowing a degree of communication between agents. The communication can be modeled either as part of a discrete action space Lowe et al. [2017], Wang et al. [2019], or as a continuous hidden layer within the agents' networks Sukhbaatar et al. [2016], Das et al. [2019], Rangwala and Williams [2020]. We follow the latter approach. Comm-Net Sukhbaatar et al. [2016], TarMAC Das et al. [2019], and SarNet Rangwala and Williams [2020] show that augmenting the communication mechanism with neural network modules such as attention and memory can help scale to more challenging tasks. We leverage these techniques by testing with both CommNet and TarMAC as the base architecture.

Learning when to Communicate in Multi-Agent Reinforcement Learning: A few recent studies have tackled the subject of deciding when to communicate in multi-agent settings. IC3Net Singh et al.

[2019] learns discrete communication gates using A2C in order to maximize task performance in mixed cooperative-competitive settings. We also experiment with A2C as a means of training gates, but our tasks are fully competitive and our training objective takes into account the cost of communicating. We note that the use of gating in IC3Net may be regarded as a partial solution to a flaw in their design which causes agents to leak information to competing agents; this point is made more fully in Rangwala and Williams [2020].

a much simpler learning problem. Further, they cannot be applied to tasks in which the optimal messages are not known beforehand.

I2C Ding et al. [2020] is the work most similar to ours, learning both the messages and pairwise communication decisions. It differs from our work in several important ways. First, and most importantly, I2C does not use the delayed message delivery framework employed in previous models such as CommNet, IC3Net, and TarMAC. Instead, it uses a request-reply framework in which the entire round-trip takes place before the environment makes a transition. We note that this assumes fast communication latency, and may not always be practical in real-world settings. Second, I2C does not directly target reduced communication but obtains reduced communication as a by-product of optimizing for task performance. Third, the communication-gating network and the policies are trained in a two-phase manner rather than jointly.

Gated-ACML Mao et al. [2020] and ETC-Net Hu et al. [2021] learn global gates in a two-phase manner. ETC-Net, which is the work most similar to ours, can be seen as ECNet-REINFORCE trained in a two-phase manner. However, this is a critical deficiency, as it does not allow the messages to be adapted to the final gating policy, limiting the reduction in communication. In fact, as we show in our experiments, it is possible to achieve the same communication reduction as ETC-Net using a random gating policy, requiring no learning. ECNet, by contrast, achieves a much lower level of communication at which learning is essential.

Learning Latent Discrete Structures: The problem of learning discrete latent units has been extensively explored in the literature on generative models. Two main algorithms are used for this purpose: REINFORCE Williams [1992] and the more recent Gumbel-Softmax reparameterization trick Jang et al. [2017], also named Concrete Distribution Maddison et al. [2017]. We experiment with both of these methods. In the case of Gumbel-Softmax, we combine the reparameterized sampling with the straight-through estimator Bengio et al. [2013] to obtain samples that always lie on the one-hot simplex.

3 ECNet: Efficient Communication Network We first describe the policy network used in EC3Net focusing on the process by which agents generate actions at each time-step. We assume that the environment includes N controllable agents. The policy network for agent i receives three inputs at time-step t: the local observation o t i , its past hidden states h t-1 i , and incoming messages from all agents m t-1 j . It produces four outputs:

1. a t i ∈ |A|, a discrete action 2. m t i , the new message will be sent to all agents, including itself. 3. c t ij ∈ 0, 1, a mask indicating whether agent i will communicate with agent j 4. h t i , new hidden states.

The network consists of the following modules, as shown in Figure 1b:

1. Message Aggregation Module: combines the incoming messages m t-1 j into an aggregated communication vector x t i . 2. Encoder Module: combines the observation o t i , the aggregated communication vector x t i , and the previous hidden states h t-1 i and produces new hidden states. 3. Message Gating Module: receives the current observation o t i and the updated hidden states h t1 and computes a binary gate c t ij ∈ 0, 1 controlling the communication from agent i to agent j. As we discuss in subsequent sections, this module may be supplemented with additional inputs. 4. Message Generation Module: runs after the Encoder Module and Message Gating Module and receives the updated hidden state h t i . It generates new outgoing messages m t i . 5. Action Module: also receives the updated hidden state h t i and generates discrete environment actions a t i .

## Message Aggregation Module

Since the architecture of the Message Aggregation Module is coupled to the Message Generation Module, we will describe it in the latter section.

## Encoder Module

In all our experiments, the Encoder Module is an LSTM that receives its inputs as a concatenated vector.

## Message Gating Module

We explore two forms of gating. The gates are generated at each time step.

1. Global Gating. Each agent decides whether or not to communicate. The gate is generated by passing the current hidden state h t through a linear layer, followed by sampling from a Categorical or Gumbel-Softmax distribution. We show the operation of global gating in fig. 1 a. 2. Pairwise Gating. Each agent decides whether or not to communicate with every other agent. The gate generator receives the current observation along with environment-provided information about the other agents. Here, the gating network is a two-layer MLP.

For each type of gate, we explore two optimization methods:

1. Gumbel-Softmax (GS). The reparameterization trick allows us to optimize the gate by backpropating through the network from the policy loss. In order to discourage unnecessary communication, we optimize a weighted sum of the policy gradient objective and a communication loss. For agent i, our objective is:

The Gumbel-Softmax distribution computes a sample y from log-odds x ∈ R n as:

The sample y can be reparameterized in terms of the input and a noise term and can therefore be optimized using backpropagation. τ is a temperature hyperparameter which controls the smoothness of the distribution. As the temperature goes to zero, the output of the distribution approaches a one-hot vector. We use a modified version of the Gumbel-Softmax called the Straight-Through Gumbel-Softmax, which produces samples that are one-hot while still being differentiable:

The straight-through estimator allows us to reduce the discrepancy between training, in which we use the Gumbel-Softmax, and testing, in which we take the maximum value. 2. REINFORCE. Our second method of optimizing the gating mechanism is to treat the gates c ij as additional discrete actions and optimizing them using REINFORCE alongside the environment actions. The reward for the communication gates is a weighted sum of the environment reward and a communication penalty.

In order to account for the effect of communication on the recipient agents, we optimize the gates with a global reward, i.e. the mean of all agent rewards.

We note that the combination of global gating and A2C is introduced in IC3Net. Our work adds the communication penalty as well as the stabilization techniques introduced in the next section.

## Message Generation Module

We now describe the three communication architectures used in our experiments in terms of their generation and aggregation procedures. Two of the three communication architectures, CommNet and TarMAC, assume that they receive an incoming message from every other agent. If a message is absent, we fill in the message with a zero vector.

### CommNet

The Message Generation Module in CommNet is a linear layer:

The values v j received from other agents are aggregated by summing and dividing by the total number of agents:

In our experiments, the messages v j are vectors in R 64 .

### TarMAC

TarMAC divides the message into two components, a key k i and a value v i . In our experiments, we usek i ∈ R 16 and v i ∈ R 32 . Each is generated using a linear layer:

TarMAC's Message Aggregation Module uses attention to focus on messages that are important to a receiving agent. Each agent locally generates a query vector using a linear layer:

The query is multiplied against the incoming keys and passed through a softmax function to produce normalized attention weights:

The aggregated vector is a sum of the incoming values multiplied against the attention weights.

### TarMAC-Sigmoid

In some of our experiments, we found that TarMAC had poor performance or failed to train. Empirically, we found improved performance we a modified architecture in which each message was processed independently, while retaining the ability to match queries against incoming keys while processing each message independently. Further, the modified architecture does not require knowledge of the total population size. TarMAC-Sigmoid differs from TarMAC only in its computation of attention weights. If a message is received by agent i from agent j, the attention weight is α ji = σ(w scale × (q T i k j ) + b scale . If no message is received, the attention weight is set to zero, i.e. the message is not added to the aggregated vector. w scale and b scale are trainable scalars. σ is the sigmoid nonlinearity.

## Action Module

The action module takes as input the current hidden state h t i . The action is computed using linear layer followed by sampling from a categorical distribution.

# Stabilization Techniques

We introduce two stabilization techniques that prevent model performance from collapsing when training with both task reward and a communication penalty.

1. Multitask Training: Our first stabilization method is to use construct two training tasks from environment: the first uses the communication penalty while the second has no communication penalty. We divide training episodes evenly between the two. A binary flag indicating whether the current episode uses the communication penalty is provided to the agent as part of its observation. This allows the agent to keep its communication gates open on the episodes that do not use the penalty, and therefore learn meaningful messages. 2. Message Forwarding: We also hypothesize that performance may be limited by the inability of agents to retain information from previously received messages. In order to alleviate this problem, we experiment with repeating the most recently received message. We test our models on four tasks in which communication is essential for obtaining good performance. The goal of our experiments is to assess how effective our methods are at decreasing communication overhead, while minimizing performance loss. In each of our experiments, we performed hyperparameter tuning to find communication penalties that achieve the desired performance and communication levels.

# Experiments

## Secret

The environment consists of 5 agents acting for 20 steps. The agents choose from 20 actions at each step. One of these actions is the secret and yields a reward of 1, while the others yield reward 0. The secret is fixed for the duration of the episode. It is given to one of the agents as its observation; the other agents need to communicate with the agent possessing the secret in order to solve the task.

In order to obtain maximum reward for all agents, the secret-holder needs to send only one message, while the other agents do not need to communicate. Our experiments investigate whether it is possible for agents to approach this protocol through reinforcement learning.

## Predator-Prey

Our second environment tests the ability of our models to tackle a larger-scale task. This environment consists of 10 agents that must reach a single, stationary prey, located in a 20x20 grid, within 80 steps. The prey yields a reward of 1 per step to each occupying agent. The agents only have visibility of the four adjacent grid cells to their position. Communication is therefore essential in order to locate the prey quickly. Unlike in Secret, it is difficult to specify a priori when agents should communicate. If an agent is the first to reach the prey, it should probably inform its teammates; however, agents might also want to communicate information about regions in which the prey is absent.

We measure performance using a success metric: an episode is successful if all agents are simultaneously occupying the prey's grid cell at the same time. We note that this is a considerably more demanding metric than the episode return, which can be significant even when some agents do not reach the prey.

## Secret Pairs

Our third environment tests the ability of agents to learn pairwise communication decisions. It involves 6 agents acting for 20 steps, choosing from 5 actions at each step. As in Secret, the agents must choose the correct action in order to obtain a reward of 1. Here, the agents are divided into pairs, identified by a pair id, and one agent in each pair is given the secret. Further, the secret changes every 5 timesteps.

The solution to this environment demands multiple messages to be sent, one for each change in the secret. However, the pattern of connectivity required is sparse: only the secret-holder in each pair needs to communicate, and it only needs to send a message to the other agent with the same id.

## Dynamic Cooperative Navigation

Our final environment is the dynamic cooperative navigation environment described in Hu et al. [2021]. This environment consists of two agents that each need to navigate to a destination. However, the destination is only provided to the other agent, making communication essential. Further, with a low probability, the destinations can move at each timestep, testing the ability of agents to respond dynamically. Results with all architectures are available in the Appendix.

# Results

## Secret

In Figure 3, we show the performance and communication levels of various gating methods with the TarMAC-Sigmoid architecture, which generally performs the best. We see that the model that does not gate communications obtains near-perfect task performance, but uses a large number of messages.

In contrast, the models that use global gating have somewhat lower task performance but use vastly fewer messages. The best performing gated model is ECNet-REINFORCE, which performs on par with the non-gated models but communicates only 10% of the time. We observe that ECNet-GS tends to perform worse than ECNet-REINFORCE. In addition, we note that TarMAC is the worst performing architecture, while our modified TarMAC-Sigmoid model is the best, lending support to our hypothesis that the softmax operation over attention scores might interfere with gating.

In order to ascertain whether the task reward might be sufficient to reduce communication, we implement the setup described in IC3Net, optimizing the global gate with reinforce without using a We see that while these models do not always communicate, they still send a large number of unnecessary messages. Therefore, the communication penalty is essential.

We also use the Secret environment to investigate the two stabilization techniques introduced above: multitask training and message forwarding. Figure 4 shows the effect of multitask training on the receiver return. We observe that adding multitask training consistently improves performance over the baseline across two architectures and optimization methods. In the case of CommNet with ECNet-GS, it is crucial in preventing the communication mechanism from switching off. Message forwarding (Figure 5) has a less dramatic impact but still provides a performance gain in most cases. In particular, the best-performing model is Tarmac-Sigmoid with message forwarding. Therefore, in subsequent experiments, we use both multitask training and message forwarding.

## Predator-Prey

In Predator-Prey, we similarly observe that our methods are effective at achieving a more efficient inter-agent messaging protocol. Communication is essential for this task: an independent model with no inter-agent communication is only successful in 14% of episodes, while the best-performing model, TarMAC, is successful in over 80%. For both ECNet-GS and ECNet-REINFORCE, we experiment with two penalty settings: a low-penalty setting, which reduces communication while retaining performance, and a high-penalty setting, which limits communication more severely but loses some performance. The best performing low-penalty model, TarMAC with ECNet-GS and penalty 1e-3, has over 80% success but sends messages on only 25% of steps. In contrast, the ECNet-REINFORCE models with high-penalty have 30% success but communicate only a few times each episode. These results indicate how the communicate penalty can be used to control the trade-off between task performance and communication.

In Figure 6, we plot the performance of runs using ECNet-GS and penalty 1e-3, with and without message forwarding. Once again, we see that message forwarding is effective at stabilizing training: most notably, TarMAC with message forwarding is the best-performing run while TarMAC without message forwarding does not train. However, the positive effect is not universal: CommNet performs better without message forwarding.  We next investigate whether it is possible to learnt pairwise gating by testing our models in the Secret Pairs environment. We found it helpful to make two changes to the models. First, we set the communication gates to be on when not using the communication penalty. Second, in the case of Gumbel-Softmax, we use a higher temperature value of 0.5.

We find that our best-performing model, ECNet-CS with CommNet, is able to achieve reasonable task performance while reducing communication. In order to understand the learnt communication pattern better, we plot the number of messages sent between each pairs of agents in Figure 7. We see that the model achieves the correct pattern of connectivity: only the agents that are given the secret communicate (agents 1-3) and they only send messages to the other agent with the same ID (agents 4-6).

We note that there are limitations to our current pairwise gating network. Specifically, since the gating module only receives the current observation, it cannot use the history of past timesteps to make the current gating decision. Finally, we compare ECNet to ETC-Net on the Dynamic Cooperative Navigation environment. In order to investigate the need for learnt communication decisions in this environment, we also train models that use random gating with various protocols. Our results are shown in table 2. First, we note that our best-performing model, EC-Reinforce with a penalty of 0.2, outperforms ETC-Net on both performance and communication usage. In particular, its communication probability of 0.29 is considerably lower than ETC=Net's probability of 0.46. Second, we observe that the random gating policy with probability of 0.5 has similar communication overhead as ETC-Net and only performs slightly worse. This indicates that it is not actually necessary to train a gating policy to achieve ETC-Net's reduction; instead, you can use random dropout during training time and allow the system to adapt. Third, at lower communication probabilities, EC-Net's training method is clearly necessary: EC-Net performs much better than the corresponding random gating policies at probabilities of 0.3 and 0.15. Thus, while ETC-Net could possibly be replaced with random gating, our method ETC-Net is still significantly superior.

# Conclusion

In this work, we have demonstrated that it is possible to minimize communication while maximizing performance in MARL with a simple method: directly optimizing both the task reward and a communication penalty. Further, we have shown that two techniques, multitask training and message forwarding, can significantly increase performance and stabilize training. Finally, we have shown that we can also learn the pairwise connectivity pattern required to solve a task. Our method opens several exciting possibilities for future research. An interesting future thread is to explore whether it is possible to train a single model to handle multiple communication penalty settings, allowing for deployments with different penalties without retraining.

Impact Multiagent Reinforcement Learning (MARL) may be used in systems that have positive and negative social effects. ECNet could be deployed in any such system. The core benefit of ECNET, reducing communication while retaining performance, will make MARL more accessible and reduce energy consumption. It will enable MARL to be deployed in regions with poor network infrastructure, where sending messages may be expensive. Therefore, it could allow applications such as delivery of supplies or mapping to be expanded. With each network architecture, we compare our method, ECNet, to baselines that do not use gating and IC3Net, which uses gating but does not use a communication penalty. We find that our best-performing method, ECNet-Reinforce with TarMAC-Sigmoid performs on par with prior methods while using fewer than 7 sender messages and no receiver messages. In comparison, both the non-gating baselines and IC3Net send over 50 messages.

# A.2 Computational Resources

Each of our experiments runs on a server with an Nvidia Tesla GPU and 18 Intel Xeon CPU cores.

The GPU is used for model inference during rollouts and for training. The CPU cores are used for parallel environment execution. Each experiment used 20 million environment steps and took under 12 hours.

# A.3 Algorithms

In this section, we sketches of the training algorithms used in ECNet-GS and ECNet-REINFORCE.

while Total Timesteps < Num Timesteps do Sample trajectories s t i , a t i , r 

# A.1 Complete Results

In this section, we report results for all the configurations we tested. In Secret and Predator-Prey, we compare the performance and communication levels of ECNet to the baseline networks and IC3Net. In Predator-Prey, we also illustrate the ability of ECNet to make different trade-offs between performance and communication by testing with low and high penalty settings. Our Secret-Pairs results focus on the ability of ECNet to learn pairwise gating. 

