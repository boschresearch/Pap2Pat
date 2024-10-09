# DESCRIPTION

## PRIORITY APPLICATION DATA

This application claims priority to Application No. 62/675,170 filed on May 23, 2018, which is incorporated by reference in its entirety.

## TECHNICAL FIELD

The present disclosure relates generally to knowledge graph reasoning and more specifically to multi-hop knowledge graph reasons with reward shaping and active drop-out.

## BACKGROUND

Query answering (QA) over knowledge graphs (KGs) supports many natural language processing (NLP) applications, such as semantic search, dialogue response generation, and/or the like. Reasoning over multi-hop relational paths is a competitive approach for query answering over incomplete knowledge graphs, with the benefit of being trivially interpretable.

Accordingly, it would be advantageous to have improved systems and methods for performing multi-hop knowledge graph reasoning.

In the figures, elements having the same designations have the same or similar functions.

## DETAILED DESCRIPTION

Context specific reasoning, including context specific reasoning regarding the content of natural language information, is an important problem in machine intelligence and learning applications. Context specific reasoning may provide valuable information for use in the interpretation of natural language text and can include different tasks, such as answering questions about the content of natural language text, language translation, semantic context analysis, and/or the like. However, each of these different types of natural language processing tasks often involve different types of analysis and/or different types of expected responses.

The ability to perform multi-hop reasoning is important to knowledge graph based query answering in the following aspects: (1) inferring missing or new relational links by synthesizing information over the paths connecting a pair of entities, e.g., bornIn(Obama, Hawaii)∧located-in(Hawaii, US)=>bornIn(Obama, US) and (2) answering queries that are essentially multi-hop, e.g., “Which character does Benedict Cumberbatch play in Avengers?” Besides their competitive performance, multi-hop reasoning approaches can output human-readable answer sets which may make their results easy to interpret.

According to some embodiments, multi-hop reasoning may be formulated as a sequential decision problem, and leveraged deep reinforcement learning (DRL) to perform efficient search over large knowledge graphs. However, for an incomplete knowledge graph environment, a reasoning module receives low-quality reward corrupted by the false negatives, which harms its generalization at test time. Furthermore, because no golden action sequence is used for training, the reasoning module can be easily misled by non-logical search trajectories that leads to the correct results and stuck in the local minima.

According to some embodiments, non-logical search trajectories and local minima may be avoided by adopting a pre-trained one-hop embedding model to estimate the reward of unobserved facts.

According to some embodiments, non-logical search trajectories and local minima may be avoided by performing an action dropout which randomly masks some edges of a node in the knowledge graph during training, so as to enforce effective exploration of a diverse set of path types.

FIG. 1 is a simplified diagram of a computing device 100 according to some embodiments. As shown in FIG. 1, computing device 100 includes a processor 110 coupled to memory 120. Operation of computing device 100 is controlled by processor 110. And although computing device 100 is shown with only one processor 110, it is understood that processor 110 may be representative of one or more central processing units, multi-core processors, microprocessors, microcontrollers, digital signal processors, field programmable gate arrays (FPGAs), application specific integrated circuits (ASICs), graphics processing units (GPUs) and/or the like in computing device 100. Computing device 100 may be implemented as a stand-alone subsystem, as a board added to a computing device, and/or as a virtual machine.

Memory 120 may be used to store software executed by computing device 100 and/or one or more data structures used during operation of computing device 100. Memory 120 may include one or more types of machine readable media. Some common forms of machine readable media may include floppy disk, flexible disk, hard disk, magnetic tape, any other magnetic medium, CD-ROM, any other optical medium, punch cards, paper tape, any other physical medium with patterns of holes, RAM, PROM, EPROM, FLASH-EPROM, any other memory chip or cartridge, and/or any other medium from which a processor or computer is adapted to read. The tangible, machine readable media that include executable code that when run by one or more processors (e.g., processor 110) may cause the one or more processors to perform the processes of the methods and/or implement and/or emulate the models and systems described herein.

Processor 110 and/or memory 120 may be arranged in any suitable physical arrangement. In some embodiments, processor 110 and/or memory 120 may be implemented on a same board, in a same package (e.g., system-in-package), on a same chip (e.g., system-on-chip), and/or the like. In some embodiments, processor 110 and/or memory 120 may include distributed, virtualized, and/or containerized computing resources. Consistent with such embodiments, processor 110 and/or memory 120 may be located in one or more data centers and/or cloud computing facilities.

As shown, memory 120 includes a reasoning module 130 that may be used to traverse the knowledge graph reasoning systems and models described further herein and/or to implement any of the methods described further herein. In some examples, reasoning module 130 may be used to answer a query 150 by traversing knowledge graph 140 or a model of knowledge graph 140. In some examples, reasoning module 130 may also handle the iterative training and/or evaluation of a system or model used for knowledge graph reasoning. As shown, computing device 100 receives knowledge graph 140 and query 150, which are provided to reasoning module 130, reasoning module 130 then generates a set of answers 160 that may answer query 150 based on knowledge graph 140.

As illustrated in FIG. 1, computing device 100 receives a knowledge graph or simply graph 140. A graph 140 includes nodes that store entries and that are connected by edges or links that show relationships between the entries. FIG. 2 is an example knowledge graph, according to some embodiments. As illustrated in FIG. 2, knowledge graph includes example nodes 202 that include entities. Example entities may be “Barack_Obama,” “John_McCain,” “U.S. Government,” “Hawaii,” etc. An entity may be a starting point for a search of set of answers 160 for query 150. Also one or more entities may include set of answers 160 to query 150.

In some embodiments, nodes 202 in graph 140 may be connected using directed edges or links 204. Links 204 and edges are used interchangeably throughout the specification. The edges or links 204 are directed from one node 202 to another node 202 and may show a relationship between two or more entities included in nodes 202. For example, node 202 that includes entity “John_McCain” has link 204 that is a relationship “belong_to” with node 202 that includes entity “U.S. Government.” In another example, node 202 that includes entity “Barack_Obama” has link 204 that is a relationship “belong_to” with node 202 that includes entity “U.S. Government.” As also illustrated node 202 that includes entity “Barack_Obama” has link 204 that is a relationship “born_in” to node 202 that includes entity “Hawaii”.

Going back to FIG. 1, in some embodiments, graph 140 may be represented as G=(ε, R), where ε is a set of entities and R is a set of relations. Graph 140 and G are referred interchangeably throughout the specification. The set of entities ε may be entities in nodes 202 in graph 140. There may be one entity per node 202 in some embodiments. The set of relations R may indicate a relationship between two or more nodes 202. For example, a pair of nodes 202 may have one or more relationships. Typically, set of relations R may be included in links 204. In some embodiments, link 204 between nodes 202 in graph 140 may be represented as l=(es, r, eo)∈G.

In some embodiments, graph 140 may be an incomplete graph. The incomplete graph may be graph 140 that contains missing links between two or more nodes 202 even though there exists a relationship between the entities in these two or more nodes 202. In FIG. 2, missing links 206 are links 206, illustrated with dashed arrows. Example missing link 206 may be a relationship “belong_to” from node 202 that includes entity “Rudy_Giuliani” to node 202 that includes entity “U.S. Government.” Another example missing link 206 may be a relationship “collaborate_with” from node 202 that includes entity “Barack_Obama” to node 202 that includes entity “Hillary_Clinton.”

Going back to FIG. 1, as discussed above, reasoning module 130 may traverse graph 140 to generate set of answers 160 to query 150. Query 150 may be a question received by computing device 100 from a user or generated by one or more applications that require an answer to a question. In some embodiments, query 150 may be represented as (es, rq, ?), where es is a source entity and r is a relation of interest. In other words, es may be node 202 from which reasoning module 130 begins to search for set of answers 160 over graph 140 and r may be link 204 that may lead to set of answers 160.

In some embodiments, once computing device 100 receives query 150 and graph 140, reasoning module 130 may perform a search over graph 140 to identify set of answers 160 for query 150. Set of answers 160 may be defined as Eo={eo}, and may include one or more nodes 202 that include entities that are answers to query 150. As discussed above, graph 140 may be an incomplete knowledge graph. In this case, the embodiments below describe how reasoning module 130 performs an efficient search of graph 140 and identifies set of answers 160 defined as Eo={eo} for where (es, rq, eo)∉G.

In some embodiments, reasoning module 130 may use a reinforcement learning technique to identify set of answers 160 for query 150 when graph 140 is an incomplete graph. Reinforcement learning technique is a machine learning technique where reasoning module 130 may take actions in a search over graph 140 that may maximize some reward. In some embodiments, the reinforcement learning technique may be a Markov Decision Process, which is known in the art. In the Markov Decision Process, reasoning module 130 may begin the search for query 150 at node 202 that includes entity es, and the sequentially select outgoing edges (links 204) and traverse to a connected node 202 that includes another entity e until reasoning module 130 arrives at a target entity et. In some embodiments, the Markov Decision Process may include components such as states, actions, and transitions, which are described below.

In some embodiments, S may be a set of possible states in graph 140, where each state st may be defined as st=(et, (es, rq))∉S. In this case, each state st may be a tuple where et included in node 202 is an entity visited at step t, and (es, rq) is the source entity (es) and query relation (rq). In some embodiments, et may be viewed as state-dependent information while (es, rq) may be viewed as a global context that is shared by all states.

In some embodiments, A may be a set of possible actions that may occur at outgoing edges (links 204) of an entity included at node 202 at step t. For example, a set of possible actions At=∈A at step t may consist of the outgoing edges (links 204) of et (node 202) in G (graph 140). In some embodiments, a set of actions At may be represented as At={(r′, e′)|(et, r′, e′)∈G}. To terminate a search, the set of action At may include a self-loop edge that starts and ends at the same node 202 that has the same entity et. Accordingly, when reasoning module 130 encounters a self-loop edge, reasoning module 130 may terminate the search for set of answers 160.

In some embodiments, δ is a transition function. Example transition function may be δ: S×A→S and may be defined as δ (st, At)=δ (et, (es, rq) At). In some embodiments, reasoning module 130 may determine the transition function δ is based on G.

In some embodiments, reasoning module 130 may receive a reward. Conventionally, the reward may have a value of 1 if reasoning module 130 arrives at a correct target entity eT (entity that is an answer to query 150) when reasoning module 130 traverses graph 140. Otherwise, when reasoning module 130 does not arrive at a correct target entity eT when reasoning module 130 traverses graph 140, the reward may have a value of 0. In some embodiments, the reward may be defined as:

Rb(sT)=1{(es,rq,eT)∈G}  (Equation 1)

In some embodiments, reasoning module 130 may access or generate a policy network 170 to search graph 140 for set of answers 160 to query 150. Policy network 170 may be stored in memory 120 or within reasoning module 130. In some embodiments, policy network 170 may be implemented as a neural network. In some embodiments, policy network 170 may be parameterized using state information, global context, and search history.

In some embodiments, the state information and global context includes every entity and relation in G. For example, each entity e in G may be assigned a dense vector embedding e∈d, and each relation r may be assigned a dense vector embedding r∈d. In some embodiments, an action at=(rt+i, et+1)∈At in policy network 170 may be represented as at=[r; et′], which is a concatenation of the relation dense vector embeddings r and the end node entity dense vector embeddings et′.

In some embodiments, the search history may include a history of previous searches that reasoning module 130 performed on graph 140. For example, search history ht=(es, r1, . . . et)∈H may consist of a sequence of observations and actions that were taken at step t in previous searches. In some embodiments, the search history may be encoded using a long short-term memory (“LSTM”) units in policy network 170. Example LSTM units may be:

h0=LSTM(0,[r0;es])  (Equation 2)

ht=LSTM(htat,t>0  (Equation 3)

where r0 may be a special start relation introduced to a start action with the start entity es.

In some embodiments, an action space may be encoded by stacking embeddings of some or all actions in At: At∈|A|×d. Using the action space, policy network 170 (referred to as policy network π) may be defined as:

πθ(at|st)=σ(At×W2ReLU(W1[ett:htrq]))  (Equation 4)

where σ is a softmax operator. A softmax operator may be included in a last layer of a neural network and may generate a probability distribution of a number of different outcomes. The ReLU may be a rectified linear unit of neural network. As policy network 170 is a neural network, W1 and W2 are trainable weight matrices for the respective layers of neural network.

Accordingly, when reasoning module 130 traverses policy network 170 as represented above, reasoning module 130 may identify set of answers 160 to query 150.

In some embodiments, prior to using policy network 170 to identify expected set of answers 160 to query 150, policy network 170 may initially be trained. During training, set of answers 160 for each query 150 is known. Accordingly, policy network 170 is trained to maximize an expected reward over some or all queries 150 in G using the following equation:

J(θ)=(e,r,e)∈G[a, . . . a˜π[R(sT|es,r)]]  (Equation 5)

In some embodiments, the training strategy in Equation 5 may treat query 150 with set of answers where n>1 (n being an integer), as “n” single answer queries. In other words, each query 150 may have multiple sets of answers 160 and each set of answers 160 may include single answer.

In some embodiments, training of policy network 170 may be optimized using a REINFORCE algorithm. The REINFORCE algorithm may iterate through all (es, rq, et) triplets in G and update θ with the following stochastic gradient:

∇θJ(θ)≈∇θΣtR(ST|es,r)log πθ(at|st)  (Equation 6)

As discussed above, a reinforcement learning technique may award a conventional binary reward to reasoning module 130, shown in Equation 1. However, because graph 140 may be an incomplete graph, the binary reward approach may reward false negatives and true negatives. To reduce a reward for false negatives and true negatives, the reinforcement learning technique may use one-hop knowledge graph embedding model designed for completing the incomplete knowledge graphs and generating a soft reward for target entities whose correctness is known. The reinforcement learning technique may then award reasoning module 130 with a reward generated by the one-hop knowledge graph embedding model. In some embodiments, the one-hop knowledge graph embedding model may be reward shaping network 180, described below. Reward shaping network 180 may be a neural network and may be stored in memory 120, in some embodiments.

In some embodiments, reward shaping network 180 may map nodes 202 modeled as a set of entities E, and links 204 modeled as a set of relations R to a vector space. Reward shaping network 180 may then estimate the likelihood of each link l=(es, r, et)∈G using a composition function ƒ (es, r, et) over the entity and relation embeddings. In some embodiments, function ƒ may be trained by maximizing the likelihood of all facts in G. Once function ƒ is trained, reinforced learning technique may use the following reward function to generate a reward to reasoning module 130:

R(sT)=Rb(sT)+(1−Rb(sT))ƒ(es,rq,eT)  (Equation 7)

As illustrated in Equation 7, as reasoning module 130 traverses policy network 170 for set of answers 160 to query 150, reasoning module 130 may receive a reward of 1 if reasoning module 130 generates destination eT that is a correct answer to query 150. Otherwise, reasoning module 130 may receive a fact store that may be estimated by function ƒ (es, rq, eT), which is pre-trained.

As discussed above, policy network 170 be trained using a REINFORCE algorithm. The REINFORCE algorithm may perform on-policy sampling according to πθ(at|st) and update θ stochastically using Equation 6. In some embodiments, because reasoning module 130 does not have access to an oracle path, reasoning module 130 may arrive at a correct answer eo in set of answers 160 via a path that is barely relevant to query 150. For example, as illustrated in FIG. 1, the path “Obama-endorsedBy→McCain-liveIn→U.S.←locatedIn-Hawaii” cannot be used to infer that “bornIn(Obama,Hawaii)”.

In some embodiments, reasoning module 130 may incorporate an action drop-out technique 190 into policy network 170. Action drop-out technique 190 may eliminate or reduce traversal of non-relevant or barely relevant paths. In some embodiments, action drop-out technique 190 may randomly mask some outgoing edges of node 202 in graph 140 in the sampling step of the REINFORCE algorithm. Once the outgoing edges are masked, reasoning module 130 may traverse the remaining on unmasked outgoing edges from node 202. In some embodiments, reasoning module may perform sampling according to the adjusted action distribution:

πθ˜(at|st)=σ(πθ(at|st)·m+∈)  (Equation 8)

mi˜Bernoulli(1−∝),i=1, . . . ,|At|  (Equation 9)

where each entry of m∈{0, 1}|A|is a binary variable sampled from the Bernoulli distribution with parameter 1−∝, where ∝ is a random number between zero and 1. Further, a small value E may be used to smooth the distribution in case m=0, where πθ˜ (at|st) becomes uniform.

With reference to FIG. 2, suppose reasoning module 130 begins to traverse node 202 with an entity “Barack_Obama” to determine “bornIn(Obama,Hawaii)”. When action drop-out technique 190 is used, action drop-out technique 190 may mask links “collaborate_with” and “endorsed_by” from node 202. Once masked, reasoning module 130 may perform sampling on the remaining links 204 that include “born_in” and “belong_to.”

In some embodiments, once reasoning module 130 is trained, reasoning module 130 may traverse policy network 170 and identify set of answers 160 to query 150 received by computing device 100. After training, policy network 170 may not use reward sharing network 180 to determine a reward for reasoning module 130. Also, after training, policy network 170 may not use action drop-out technique 190 to mask edges (links 204) in graph 140. Instead, after training, reasoning module 130 may traverse across some or all (links 204) edges from nodes 202 that are in the path to set of answers 160.

is trained using reward sharing network 180 and action drop-out technique 190, policy network 170 may be used to determine set of answers 160 from query 150 as illustrated in equation 4. As

FIG. 3 is a block diagram 300 of a training approach for a policy network, according to some embodiments. As illustrated in FIG. 3, policy network 170 may be trained with action drop-out technique 190 and reward shaping network 180. As illustrated in FIG. 3, at each step t, reasoning module 130 samples an outgoing link (r′, et′) according to πθ˜ (at|st), which is a stochastic REINFORCE policy (πθ(at|st) that is perturbed by a random mask m. As also illustrated in FIG. 3, reasoning module 130 receives a reward of 1 if reasoning module 130 observes a correct answer in set of answers 160. Otherwise, reasoning module 130 receives a reward ƒ (es, rq, eT) that is estimated by reward shaping network 180.

FIG. 4 is a simplified diagram of a method 400 for training a policy network, according to some embodiments. One or more of the operations 402-412 of method 400 may be implemented, at least in part, in the form of executable code stored on non-transitory, tangible, machine-readable media that when run by one or more processors may cause the one or more processors to perform one or more of the operations 402-412.

At operation 402, a node is identified. For example, reasoning module 130 identifies node 202 that may be a start node to query 150 or one of the nodes in graph 140 along a path to set of answers 160.

At operation 404, one or more links are removed from the identified node. For example, action drop-out technique 190 may be used to mask one or more links 204 from the identified node 202 to other nodes 202, forming the remaining outgoing links 240 for the identified node 202.

At operation 406, a graph is traversed using the remaining outgoing nodes. For example, reasoning module 130 may use the remaining outgoing links 204 and policy network 170 to traverse the remaining outgoing links to determine set of answer 160 for query 150.

At operation 408, a determination is made whether a node with an observed answer is reached. For example, during training, query 150 may be associated with set of answers 160. If reasoning module 130 reaches node 202 that includes an entity that corresponds to an answer in set of answers 160, then reasoning module 130 reaches an observed answer. If reasoning module 130 reaches the observed answer, method 400 proceeds to operation 410. Otherwise, method 400 proceeds to operation 412.

At operation 410, rewarding the reasoning module with a reward of one.

At operation 412, rewarding the reasoning module with a reward identified by a reward shaping network. For example, reward shaping network 180 may identify a reward and award the identified reward to reasoning module 130.

In some embodiments, awarding a reward to reasoning module 130 using reward shaping network 180 and using action drop out technique 190 while training policy network 170 increases query answering performance over graph 140. This is illustrated in FIG. 5 that includes a table illustrating question answering performances on different knowledge graphs using different models. Example datasets represented as knowledge graphs in FIG. 5 are UMLS, Kinship, FB15k-237, WN18RR, and NELL-995. FIG. 5 also illustrated different models used to find an answer or set of answers 160 to query 150 using the above knowledge graphs. Example single-hop modes are Dist-Mult, ComplEx, ConvE, and example multi-hop models are NTP-λ, (which is an improved version of Neural Theorem Prover), Neural Logical Programming (NeuralLP), and MINERVA. Additionally, ComplEx and ConvE have been modified to include reward shaping network 180 and action drop-out technique 190 described above.

As illustrated in FIG. 5, ComplEx and ConvE that have been modified to include reward shaping network 180 and action drop-out technique 190 appear to have an increase performance for identifying an answer for query 150 across many of the UMLS, Kinship, FB15k-237, WN18RR, and NELL-995 graphs as compared to other models.

Although illustrative embodiments have been shown and described, a wide range of modification, change and substitution is contemplated in the foregoing disclosure and in some instances, some features of the embodiments may be employed without a corresponding use of other features. One of ordinary skill in the art would recognize many variations, alternatives, and modifications. Thus, the scope of the invention should be limited only by the following claims, and it is appropriate that the claims be construed broadly and in a manner consistent with the scope of the embodiments disclosed herein.

