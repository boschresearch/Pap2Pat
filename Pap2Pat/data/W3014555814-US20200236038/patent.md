# DESCRIPTION

## FIELD

Embodiments of the invention relate to computerized systems and computerized methods configured to optimize data transmission paths in a large-scale computerized network relative to reliability and bandwidth requirements. Embodiments of the invention further relate to computerized systems and methods that direct and control physical adjustments to data transmission paths in a large-scale network's composition of computerized data transmission nodes in order to limit data end-to-end transmission delay in a computerized network to a delay within a calculated worst-case delay bound.

## BACKGROUND

The following description includes information that may be useful in understanding embodiments of the invention. It is not an admission that any of the information provided herein is prior art or relevant to the presently claimed invention, or that any publication specifically or implicitly referenced is prior art.

Large communication networks, such as T-Mobile's North American network or Microsoft's cloud network, are among the most complex industrial systems to be found anywhere in the world today. Managing these large communication networks efficiently while also satisfying all the demands placed on them is obviously not a trivial problem to solve. Many computer engineers and other technical experts have worked tirelessly to improve these systems so that they will continue to operate as intended while also being able to accommodate the increasingly complicated demands placed on them.

Computerized control planes are known for various types of communications networks, particularly large communications networks. A control plane comprises the portion of a router architecture that is concerned with drawing the network topology and/or the information in a routing table that defines what to do with incoming data packets. Control planes decide which routes go into a main routing table for unicast routes and into additional routing tables for multicast routes.

Control planes can be applied to access networks of nearly all types. Control planes offer well-known advantages including, among the others, significant operating expense saving, capital expense savings, and improved traffic restoration. However, the control plane technology provides some challenges as well, such as scalability issues and low control of the network operator on the paths used by the traffic in end-to-end services with consequent lack of resource optimization.

Prior art solutions for control plane scalability generally focus on aspects such as electronic aggregator-to-processing entity or processing entity-to-electronic aggregator delay reduction, computerized processing entity capacity and utilization optimization, flow setup time and communication overhead minimization. While these efforts in the prior art have been helpful, they have not yet provided an optimal solution for the problems they attempt to solve.

For large-scale programmable networks, flexible deployment of distributed control planes is essential for service availability and performance. However, the solutions available in the prior art only focus on placing controllers whereas the consequent control traffic is often ignored, leading to numerous drawbacks.

Similarly, the next generation of networked systems will likely include programmable and virtualized infrastructures. The accelerated development of network programmability and virtualization is a reasonable and expected development, as commodity hardware becomes increasingly cheaper and the demand for elastic cloud services continues to grow. In distributed and networked environments, deployment of virtual instances requires a robust deployment strategy to ensure service reliability and performance, such as bandwidth and flow delay. Here, virtual instances comprise physical hardware that has been configured in a logical (or virtual) configuration to perform as if the composition of physical hardware was an integrated unit. As cloud services become central to the digital transformation in research, industry, and finance, it becomes of increasing importance to consider the service performance within and across geo-distributed data centers. Addressing these challenges is fundamental to elastic services entailing effective resource usage and service performance requirements.

The ability to flexibly plan and deploy virtualized infrastructures with performance guarantees is relevant to many networked systems that rely on virtual entities requiring reliable data transactions, such as:


- - software defined networks (“SDN”) operating using distributed
    control planes;
  - network services implemented by virtual network functions (“VNF”);
    and
  - cloud computing services running in distributed system
    architectures.

Common to these networked systems is the deployment of virtual entities (a virtual machine, a network controller instance or a virtual network function) which implement a service (cloud application, control service or network service). Coupled with digital transformation, there is a drastic increase in services centered around reliable data transactions with performance guarantees on bandwidth and flow delay.

In particular, flow delay is of growing importance as more services (e.g., Intelligent Transportation Systems (“ITS”)) require short response times for close to real-time applications. Similarly, big data computations carried out across geo-distributed data centers may in many cases require guaranteed performance. Accordingly, the way cloud computing tasks have been planned and deployed will impact service performance with respect to how quickly and accurately a cloud computing result can be delivered (some results could get lost due to, e.g., link loss).

As networks and services grow more complex, automated deployment of virtualized infrastructures becomes essential. Methods and systems enabling automated deployment typically require the capability for taking performance guarantees and reliability requirements into account. Application areas or implementation of improved solutions include control plane deployments, cloud computing, and network function virtualization (“NFV”).

While network control systems and services have improved in recent years, there nevertheless exists a continuous need to improve the design and operation of network control systems and services, especially where such improvements can be accomplished in a commercially reasonable fashion.

## SUMMARY OF THE INVENTION

Embodiments of the invention provide an electronic data transmission scheduling system for a computer network having a plurality of computerized data transmission nodes and a plurality of electronic aggregators, wherein each computerized data transmission node of the plurality of computerized data transmission nodes has at least one data transmission link of a plurality of data transmission links to another computerized data transmission node of the plurality of computerized data transmission nodes, and wherein each electronic aggregator of the plurality of electronic aggregators forwards data to a set of computerized data transmission nodes of the plurality of computerized data transmission nodes, a configuration of the plurality of computerized data transmission nodes and the plurality of data transmission links collectively forming a network topology. Embodiments of the electronic data transmission scheduling system comprise an electronic reliability checker that examines possible data transmission routes between computerized data transmission nodes of the plurality of computerized data transmission nodes and data transmission links of the plurality of data transmission links to determine a network mapping reliability score for the network topology, wherein the reliable data transmission reliability represents a probability that an electronic aggregator of the plurality of the electronic aggregators connects to at least one computerized data transmission node of a set of computerized data transmission nodes given computerized data transmission node and data transmission link failure probabilities. Embodiments of the invention also include an electronic bandwidth checker configured to calculate bandwidth allocations for the network topology, wherein the electronic bandwidth checker develops calculated bandwidth allocations by testing different combinations of data transmission links from the plurality of data transmission links and different combinations computerized data transmission nodes of the plurality of computerized data transmission nodes. Embodiments of the invention further comprise an electronic resource planner that uses the network mapping reliability score from the electronic reliability checker, estimated traffic demands in the electronic resource planner and the calculated bandwidth allocations from the electronic bandwidth checker to develop a computer-implementable deployment strategy that directs rearrangement of the network topology by calculating a trade-off between the network mapping reliability score and the calculated bandwidth allocation that satisfies predetermined requirements for each of the network mapping reliability score and the bandwidth requirements.

Embodiments of the invention further comprise the electronic data transmission scheduling system described above that further comprises an electronic flow delay checker that determines an end-to-end delay of delivering a packet from a sending computerized data transmission node of the plurality of computerized processing nodes to a destination computerized data transmission node of the plurality of computerized processing nodes over at least one data transmission link of a plurality of data transmission links; wherein the electronic resource planner is further configured to use the end-to-end delay along with the network mapping reliability score from the electronic reliability checker and the calculated bandwidth allocations from the electronic bandwidth checker to develop a computer-implementable deployment strategy that directs rearrangement of the network topology by calculating trade-offs among the network mapping reliability score, the calculated bandwidth allocations, and the end-to-end delay that satisfies predetermined requirements for reliability, bandwidth and end-to-end delay.

Embodiments of the invention further provide a method for electronic data transmission scheduling for a computer network having a plurality of computerized data transmission nodes and a plurality of electronic aggregators, wherein each computerized data transmission node of the plurality of computerized data transmission nodes has at least one data transmission link of a plurality of data transmission links to another computerized data transmission node of the plurality of computerized data transmission nodes, and wherein each electronic aggregator of the plurality of electronic aggregators forwards data to a set of computerized data transmission nodes of the plurality of computerized data transmission nodes, a configuration of the plurality of computerized data transmission nodes and the plurality of data transmission links collectively forming a network topology. Embodiments of the method for electronic data transmission scheduling comprise examining possible data transmission routes between computerized data transmission nodes of the plurality of computerized data transmission nodes and data transmission links of the plurality of data transmission links by an electronic reliability checker that to determine a network mapping reliability score for the network topology, wherein the reliable data transmission reliability represents a probability that an electronic aggregator of the plurality of the electronic aggregators connects to at least one computerized data transmission node of a set of computerized data transmission nodes given computerized data transmission node and data transmission link failure probabilities. Embodiments of the method further comprise calculating bandwidth allocations for the network topology by an electronic bandwidth checker, wherein the electronic bandwidth checker develops flow routing plans and calculated bandwidth allocations by testing different combinations of data transmission links from the plurality of data transmission links and different combinations computerized data transmission nodes of the plurality of computerized data transmission nodes. Embodiments of the invention also comprise preparing a computer-implementable deployment strategy that directs rearrangement of the network topology by an electronic resource planner that uses the network mapping reliability score from the electronic reliability checker and the estimated traffic demands in the electronic resource planner to calculate trade-offs between the network mapping reliability score and the calculated bandwidth allocations, such that the computer-implementable deployment strategy satisfies predetermined requirements for reliability and bandwidth.

Embodiments of the invention comprise the method for electronic data transmission scheduling as described above and further comprise determining by an electronic flow delay checker an end-to-end delay of delivering a packet from a sending computerized data transmission node of the plurality of computerized processing nodes to a destination computerized data transmission node of the plurality of computerized processing nodes over at least one data transmission link of a plurality of data transmission links; wherein the electronic resource planner is further configured to use the end-to-end delay along with the network mapping reliability score from the electronic reliability checker, estimated traffic demands in the electronic resource planner and the calculated bandwidth allocation from the electronic bandwidth checker to develop a computer-implementable deployment strategy that directs rearrangement of the network topology by calculating trade-offs among the network mapping reliability score, the calculated bandwidth allocation, and the calculated end-to-end delay that satisfies predetermined requirements for reliability, bandwidth and end-to-end delay.

Embodiments of the invention further comprise a method for automatic monitoring and decision-making for dynamically triggering recalculations of the electronic data transmission scheduling determined by observed changes of the networking conditions. This automatic monitoring and decision-making method may be employed to further minimize time delays in data transmission. Further, embodiments of the invention comprise determining the power utilization of computerized data transmission processing nodes and computerized data transmission nodes, that are used or unused for electronic data transmission scheduling. Once the power utilization has been computed, then the power utilization data may be considered in the overall deployment of the data transmission scheme, according to an embodiment of the invention.

## DETAILED DESCRIPTION OF AN EMBODIMENT OF THE INVENTION

Embodiments of the invention entail a computerized method and system that automates operation of a large network of distributed computerized processing entities that exchange information with each other in line with defined policies on bandwidth constraints, flow delay bounds and/or service reliability. An example for such a large network would be T-Mobile's North American network or Microsoft's cloud network.

Embodiments of the invention provide a computerized network management system or a computerized tool that systematically analyzes the impact of different computerized network or service deployments with respect to characteristics such as reliability, bandwidth, and flow delay. The output comprises a computer-operable and/or computer-implementable deployment strategy (or plan) that can be realized by having additional computing elements (or software in a computing element) initiate processing entities at planned locations along with the data flows following performance guarantees and reliability guarantees. The computer-implementable deployment strategy defines network and/or service control operations in line with calculated performance guarantees. Embodiments of the invention further relate to computerized systems and methods that direct and control the physical adjustments to data transmission paths in a large-scale network's composition of computerized data transmission nodes in order to limit data end-to-end transmission delay in the computerized network to within a calculated worst-case delay bound.

Embodiments of the invention may further provide a black-box optimization framework that provides a computerized method and system that quantifies the effect of the consequent control traffic when deploying a distributed control plane in a computerized network. Evaluating different computerized implementations of the framework over real-world computerized network topologies shows that close to optimal solutions may be achieved. Moreover, experiments using such large-scale network computerized systems indicate that applying a computerized method for controller placement without considering the control traffic, causes excessive bandwidth usage (worst cases varying between 20.1% to 50.1% higher bandwidth) and congestion when compared to various embodiments of the prior art, such as may be found in S. Liu, R. Steinert, and D. Kostic, “Flexible distributed control plane deployment,” in NOMS 2018-2018 IEEE/IFIP Network Operations and Management Symposium. Mini conference. IEEE, 2018, pp. 1-7. To ensure resource efficiency, service reliability and guaranteed performance, deployment of distributed control planes (fundamental for scalable management of traffic over physical and virtual data transmission nodes) takes both placement and control traffic properties into account.

Embodiments of the invention provide: 1) a novel formalization of the problem of distributed control plane optimization, enabling 2) tuning of reliability and bandwidth requirements. By analyzing the challenges and complexity of the computerized processing entity placement and traffic routability problem, embodiments of the invention introduce a generic black-box optimization process formulated as a feasibility problem. For embodiments of the invention, a computerized processing entity comprises a computer capable of executing computer instructions implementing the formulas detailed here, and especially a computer networked with other computers. Thus, embodiments of the invention provide computerized systems that specify each step of the process along with guiding implementations. Embodiments of the invention may be implemented as specialized electronic control systems configured for physical attachment to the other elements comprising a computer network. As such, embodiments of the invention can be used for planning a physical computer network with respect to bandwidth, reliability and delay requirements. Similarly, the specific components for directing and controlling such a physical computer network may comprise specialized hardware and other electronic devices that monitor the physical computer network, make physical adjustments to the flow of data through the network, and otherwise direct the operations for such a physical computer network.

In contrast to the prior art, an embodiment of the optimization process detailed here adds additional steps for quantifying the consequences of deploying a control plane solution that predetermines reliability and bandwidth requirements. As a powerful computerized prediction tool, service providers and operators can use embodiments of the invention to fine-tune control plane deployment policies for application in their systems. In combination with the generic design of the black-box optimization process, many existing computerized methods can be adapted and employed for control plane optimization and service management.

Embodiments of the invention also provide a computerized method and a computerized system that provides a capability for identifying how computerized processing entities and electronic aggregators in a network may be deployed and connected in a computerized network topology to implement a distributed service that satisfies reliability and performance requirements. Embodiments of the invention may comprise specialized electronic components, specialized electronic circuits, specialized hardware, computerized software and/or hardware that may identify in/for a large computer network:


- - 1. the set of computerized data transmission nodes operating as
    computerized processing entities;
  - 2. the set of computerized data transmission nodes operating only as
    electronic aggregators and their association to computerized
    processing entities;
  - 3. the connections between the computerized processing entities and
    the electronic aggregators; and
  - 4. the routes of expected data flows, meeting the requirements on
    reliability, bandwidth and flow delay.

Embodiments of the invention further enable automated deployment of computerized processing entities and electronic aggregators in a computerized network topology considering reliability, bandwidth and flow delay that:


- - 1. provides an optimized computer-implementable deployment strategy
    for the network in line with network operator specific requirements
    for flow delay, bandwidth or control service reliability;
  - 2. predicts the demands on flow delay for an estimated
    computer-implementable deployment strategy given a fixed control
    service reliability and a fixed limit on bandwidth and a network
    topology;
  - 3. predicts the demands on bandwidth for an estimated
    computer-implementable deployment strategy given a fixed control
    service reliability and a fixed limit on flow delay and a network
    topology;
  - 4. predicts the achievable control service reliability for an
    estimated computer-implementable deployment strategy given fixed
    limits on flow delay and bandwidth and a network topology.

Embodiments of the invention enable guaranteed reliability in line with predetermined requirements and computerized systems executing the embodiments of the invention may output a deployment strategy that provides congestion-free connections between associated computerized processing entities and electronic aggregators in a manner that cannot be performed using prior art methods.

### Relevant Terminology and Definitions

A computerized processing entity in a computerized network may be, e.g., a network controller; a computing unit (for example, a virtual machine “VM”); as well as a cluster of computerized processing entities (such as, a data center). A computerized processing entity may be virtual or physical. A virtual computerized processing entity comprises a collection of physical computerized processing entities configured to perform as if such systems comprises a unified entity. A network of distributed computerized processing entities may operate locally in a computerized network or computerized data center, or globally across geo-distributed computerized data centers.

An electronic aggregator comprises a computerized network entity processing that forwards network traffic (i.e., one or many network flows), e.g., a computerized gateway or a computerized network switch. An electronic aggregator may be, e.g., a computerized gateway, a computerized network switch, or a non-computerized device such as a field-programmable gate array (FPGA) that comprises an integrated circuit designed to be configured by a customer or a designer after manufacturing that contains an array of programmable logic blocks. An electronic aggregator may be virtual or physical. An electronic aggregator may include, for example, an OpenFlow switch in the context of Software-Defined Networks (“SDN”) or a radio access point in a Software-Defined Radio Access Network (“SoftRAN”) context. In any case, the electronic aggregator acts as a data forwarding device.

A data transmission node or network node or computerized data transmission node (the terms are synonymous) comprises a computerized network entity hosting an electronic aggregator. Suitable computerized network entities may include application-specific hardware. Put another way, a data transmission node includes at a minimum a central processing unit and related equipment (network connections, memory, etc.) needed for successful executing the programs to accomplish its predetermined tasks, such as hosting an electronic aggregator. A data transmission node may or may not host a computerized processing entity configured to perform additional tasks. A node may be virtual or physical. A virtual data transmission node nevertheless comprises a collection of physical entities configured to operate in a collective manner to perform a defined task.

A data transmission link or network link (the terms are synonymous) comprises a connection between computerized data transmission nodes and may be virtual or physical. A virtual network link nevertheless comprises a collection of physical computing devices that have been arranged to perform a collective task.

A network link propagation delay refers to the signal propagation delay of the link.

A network topology comprises a set of interconnected computerized data transmission nodes via network links. Of course, the network topology may also include data transmission nodes comprised of application specific hardware. In short, the network topology here comprises a physical structure or a virtual structure (comprised of physical structures), and in all cases represents a physical entity and not a mere mathematical calculation.

Bandwidth refers to the amount of data that can be transmitted by a link during a time unit.

An electronic bandwidth checker calculates a routability indicator λ in step 110 of FIG. 01B. In one embodiment of the invention, the electronic bandwidth checker may run algorithms such as FPTAS and estλ (described herein below) for this purpose. The electronic bandwidth checker outputs the routability indicator to the electronic resource planner. The electronic bandwidth checker can also output the corresponding flow routing plan along with the calculated bandwidth allocation per network link for routable solutions following the bandwidth requirements.

A network flow comprises a stream of data packets.

Flow delay represents the end-to-end delay of delivering a packet of a certain flow from the source node (sender) to the destination node (receiver) over one or several physical or virtual links. A virtual link nevertheless comprises a series of physical entities configured to perform a particular task, as if these entities comprised a single entity.

An electronic flow delay checker computes a routability indicator χ in the Delay and Backlog Verification step 111 of FIG. 01B. The electronic flow delay checker calculates Delay and Backlog bounds according to a network calculus model. The electronic flow delay checker outputs the delay and backlog bounds and a routability indicator to the electronic resource planner. The checker can also output the corresponding flow routing plan along with the calculated bandwidth allocation per network link for routable solutions following the flow delay requirements.

Reliability is defined as the probability that an operational electronic aggregator is connected to at least one operational computerized processing entity, given data transmission node and link failure probabilities. Reliability guarantee corresponds to guaranteeing (deterministically or probabilistically) that a service request can be delivered to and handled by at least one computerized processing entity.

An electronic reliability checker comprises tests and estimates the failure probabilities of the network. The electronic reliability checker calculates a reliability score R, which is input to the electronic resource planner.

A computer-implementable deployment strategy refers to setting up a network of distributed virtual or physical computerized processing entities exchanging data. Such a computer-implementable deployment strategy is the result of a multi-step process, including planning where in the physical network the computerized processing entities should perform their predetermined operations, as well as the flow paths among computerized processing entities across a physical network. Computer-implementable deployment strategies may be implemented by physical computing devices in an automated fashion. In such systems, the presence of a human is not required, and such systems may theoretically operate without intervention indefinitely.

An electronic resource planner executes Mapping (step 103), Association (step 105), Traffic estimation (step 107) and the condition test (step 117), given reliability and bandwidth and delay requirements and configuration and network topology input. Mapping and Association involve calculating cost functions based on achieved reliability, bandwidth and delay routability indicators. The cost functions are maintained throughout the iterative workflow process by the electronic resource planner. The electronic resource planner develops a computer-implementable deployment strategy based on evaluating the fulfillment of conditions from reliability/bandwidth/delay routability.

Limitations in the Prior Art

The early definition of the control plane in a software-defined network (“SDN”) setting assumes that one computerized processing entity (in this context an SDN controller or control instance) handles flow requests over a set of associated electronic aggregators (i.e. SDN switches). To improve reliability and scalability, more recent solutions propose a distributed control plane, consisting of multiple physically distributed but logically centralized control instances. Under distributed conditions, both placement and routing of data traffic between processing entities should be considered to avoid a dramatic increase in communication overhead. The prior art in distributed control plane deployment typically ignores control plane traffic routability (e.g. bandwidth constraint and flow delay limitations) and only considers placement optimized for scalability or reliability.

For example, the prior art in control plane scalability mainly focuses on aspects such as switch-to-computerized processing entity or computerized processing entity-to-computerized processing entity delay reduction, computerized processing entity capacity and utilization optimization, and flow setup time and communication minimization. Prior art examples having reliability models or measurements employ intuitive objective functions to obtain a placement solution, without providing an estimate of the achieved reliability. One prior art solution, for example, proposed a method for estimating the network reliability in polynomial time and provide a lower bound of the actual reliability, along with a heuristic algorithm to decide the number of processing entities and their locations, to guarantee a certain reliability requirement. However, the prior art does not address control traffic routability.

Cloud computing comprises shared pools of configurable computer systems and system resources and higher-level services that can be automatically and rapidly provisioned with minimal management effort, often over the Internet. Cloud computing relies on sharing of resources to achieve coherence and economies of scale, similar to a public utility.

In cloud computing, problems similar to the above-mentioned control plane deployment problem also exist. The placement of virtual machines (“VMs”) having an awareness of network resources and inter-VM traffic demands have been studied in the prior art. One prior art solution proposed VM placement approaches with the considerations on the inter-traffic between VMs, by assuming a very simple model of the underlying network (without network topology and routing considerations). In other prior art, methods for placing a fixed number of VMs with traffic consideration based on networks inside a data center have been proposed. For example, one on-demand VM placement solution in the prior art assumes a simple network model which is insufficient in real network applications

In the context of elastic network services, a virtual network function can be viewed as a VM with a point-to-point source destination traffic demand. Some prior art focuses on the placement and routing of a given set of VNFs inside a data center. One prior art solution proposes heuristic algorithms for dynamic on-demand placement and routing of VNFs.

Many existing solutions overlook the importance of considering the traffic as part of the solution. Dealing with the traffic associated with certain computer-implementable deployment strategies is typically ignored in the prior art, although traffic flows need to be forwarded timely and reliably through a network infrastructure having varying link capacities, availability, and other networking properties. Traffic congestion, for example, is especially destructive since it may degrade service performance, or worse, cause availability issues—the latter cannot be tolerated in services critical to human safety, for example.

The inventors have discovered that the importance of considering reliability, bandwidth and delay of flows between networking entities (both physical and virtual), factors which have been severely overlooked in the prior art. Dealing with the traffic flows of certain infrastructure deployments is often ignored, although it is essential for most services that the network traffic is forwarded timely through networks exhibiting varying network properties related to service availability and bandwidth.

The inventors have further discovered that at best, the existing state of the art only partially deals with the problem, either by proposing solutions that deal with deployment without the proper consideration of all types of traffic flows, or only deployment without involving certain steps like determining the number of processing entities and data transmission paths. Besides, important aspects related to reliability, bandwidth and flow delay have not been properly modelled and studied until the inventors recognized their importance in developing an improved computerized solution to the problem.

Because of these shortcomings, prior art approaches fail to support reliable service elasticity, albeit being a fundamental feature for scalable network service operation and availability. Not considering reliability, flow delay and bandwidth aspects of the traffic exchanged between entities may consequently lead to serious scalability and service reliability issues in large-scale distributed systems.

It is worth noting that flow delay optimization based on empirical objectives are essentially different from embodiments of the present invention. The present invention is based on well-formulated theory and models, whereas much of the prior art is based on empirical objectives and cannot calculate and guarantee a worst-case flow delay bound.

Formal Problem Definition Associated with Embodiments of the Invention

Assumptions and Requirements

FIG. 01A illustrates an electronic data transmission scheduling system 160, according to an embodiment of the invention that operates with a computerized network 150 having a network topology, exemplified in the context of a distributed control plane. The electronic data transmission scheduling system 160 includes an electronic reliability checker 161, an electronic bandwidth checker 162, and an electronic resource planner 164, according to an embodiment of the invention. Some embodiments of the invention also include an electronic flow delay checker 163. The electronic data transmission scheduling system 160 may comprise one or more computers, a dedicated circuit, a field-programmable gate array (FPGA) and other suitable devices as known to a person of ordinary skill in the relevant field. The electronic data transmission scheduling system 160 may even be combined with other network devices in some embodiments of the invention.

An electronic automated rescheduling system 165, comprising an electronic network monitor 166 and an electronic change detector 167, can be used for initiating the calculation of an updated deployment plan upon changed network conditions of the computerized network 150 (e.g., changed traffic patterns or computerized node or link failures). The electronic power utilization manager 168 controls the energy usage of used and unused computerized data transmission nodes and links. While the electronic power utilization manager 168 is shown as being outside the electronic data transmission scheduling system 160, in some embodiments, the electronic power utilization manager 168 could be constructed inside the electronic data transmission scheduling system 160.

The computerized network 150 will first be described to illustrate the environment in which the electronic data transmission scheduling system 160 operates, according to an embodiment of the invention. The computerized network 150 has a network topology applicable for processing by embodiments of the invention.

The network 150 is the object that the electronic data transmission scheduling system 160 processes, according to an embodiment of the invention. Given a network topology with data transmission nodes and links (as defined herein), the electronic data transmission scheduling system 160 determines which data transmission nodes of 150 contains the processing entities, and which nodes are simply electronic aggregators.

The electronic data transmission scheduling system 160 may operate outside the network 150. The electronic data transmission scheduling system 160 controls, configures, deploys the control plane for the network 150. But, the electronic data transmission scheduling system 160 may typically not be a part of network 150, according to an embodiment of the invention. For example, electronic data transmission scheduling system 160 may operate remotely, or even offline (e.g., just used for booting up the network 150).

So, data transmission nodes (computerized processing entities) 171, 173, together with computer nodes 191-196, comprise a set of data transmission nodes.

Given the sample network 150 in FIG. 01A, by running the electronic resource planner 164, the electronic resource planner 164 determines (for example) the following mapping for the network 150 that it is better to launch processing entities in data transmission nodes 171, 173, in order to receive a desired network mapping reliability score as well as data end-to-end transmission delay. So, electronic resource planner 164 configures the network 150 and makes processing entities launched in data transmission nodes 171, 173. See, e.g., the description of the electronic resource planner 164 with respect to step 109 shown in FIG. 01B, as well as the definition provided for the electronic resource planner 164 hereinbelow.

Notice that mapping means which data transmission nodes are selected and configured to contain the processing entities. The configuration may happen either online or offline, according to an embodiment of the invention

After being processed by the electronic resource planner 160, the network 150 comprises a distributed control plane comprising two control planes 181, 183 that each comprise representative electronic aggregators 191-196 but could, of course, include a significantly greater number of electronic aggregators. Each control plane 181, 183 includes data transmission nodes 171, 173. The data transmission nodes 171, 173 comprise computerized devices and/or hardware that handle control traffic within their respective control planes 181, 183. The computer nodes 191-196 correspond to electronic aggregator entities and handle the data traffic in their respective control planes 181, 183.

The solid lines between the elements in the computer network 150 represent data transmission links. The dashed lines represent switch-control traffic, e.g., management instructions from a network manager to a given computerized node. The large solid line connecting the control planes 181, 183 represents control-to-control traffic, e.g., instructions between the two data transmission nodes 171, 173. The collective impact of these control instructions is to make the control planes 181, 183 function collectively as a distributed control plane in the computerized network 150.

The electronic reliability checker 161 examines possible data transmission routes between computerized data transmission nodes involving data transmission nodes 171-173 and computerized nodes 191-196 and the data transmission links to determine network mapping reliability scores for the network topology. The electronic resource planner 164 tests different mappings of processing entities based on reliability scores provided by the reliability checker 161, wherein the reliable data transmission reliability represents a probability that an electronic aggregator 191-196 connects to at least one processing entity 171-173 within a set of data transmission nodes (171, 173) or (193-196) given computerized data transmission node and data transmission link failure probabilities, according to an embodiment of the invention. The electronic reliability checker 161 calculates the measures described herein that pertain to its outputs. The electronic reliability checker 161 may comprise one or more computers, a dedicated circuit, a field-programmable gate array (FPGA) and other suitable devices as known to a person of ordinary skill in the relevant field.

The electronic bandwidth checker 162 calculates a flow routing plan along with the calculated bandwidth allocation per network link for routable solutions (indicated by λ) following the bandwidth requirements, wherein the electronic bandwidth checker 162 develops calculated bandwidth allocations by testing different combinations of data transmission links and different combinations computerized data transmission nodes 171-173 and 191-196, according to an embodiment of the invention. The electronic bandwidth checker 162 calculates the measures described herein that pertain to its outputs. The electronic bandwidth checker 162 may comprise one or more computers, a dedicated circuit, a field-programmable gate array (FPGA) and other suitable devices as known to a person of ordinary skill in the relevant field.

The electronic resource planner 164 uses the network mapping reliability score from the electronic reliability checker 161, the traffic estimates from the electronic resource planner 164 and the calculated bandwidth allocation from the electronic bandwidth checker 162 to develop a computer-implementable deployment strategy that directs rearrangement of the network topology by calculating a trade-off between the network mapping reliability score and the calculated bandwidth allocation that satisfies predetermined requirements for reliability and the bandwidth, according to an embodiment of the invention. The electronic resource planner 164 calculates the measures described herein that pertain to its outputs. The electronic resource planner 164 may comprise one or more computers, a dedicated circuit, a field-programmable gate array (FPGA) and other suitable devices as known to a person of ordinary skill in the relevant field.

The electronic flow delay checker 163 determines an end-to-end delay of delivering a packet from a sending computerized data transmission node 171-173 and 191-196 to a destination computerized data transmission node 171-173 and 191-196 over at least one data transmission link of a plurality of data transmission links, according to an embodiment of the invention. The electronic flow delay checker 163 will be described in further detail below. The electronic flow delay checker 163 calculates the measures described herein that pertain to its outputs. The electronic flow delay checker 163 may comprise one or more computers, a dedicated circuit, a field-programmable gate array (FPGA) and other suitable devices as known to a person of ordinary skill in the relevant field. For embodiments of the invention including the electronic flow delay checker 163, the electronic resource planner 164 is modified to include the end-to-end delay determination of the electronic flow delay checker along with the outputs of the electronic reliability checker 161, the traffic estimates from the electronic resource planner 164 and the electronic bandwidth checker 162 to develop a computer-implementable deployment strategy that directs rearrangement of the network topology by calculating trade-offs among the network mapping reliability score, the calculated bandwidth allocation, and the calculated end-to-end delay that satisfies predetermined requirements on reliability, bandwidth and end-to-end delay, according to an embodiment of the invention.

The electronic network monitor 166 of the electronic automated rescheduling system 165 is a computerized system that monitors the operational state and performance of the computerized network and the network traffic. The electronic change detector 167 of the electronic automated rescheduling system 166 comprises a computerized system that detects changes in the monitored operational state and performance of the computerized network and network traffic. The electronic change detector can detect changes in end-to-end transmission delays, flow demands, reliability, link or node failures, and/or any other change which influences the reliability and or performance requirements of the deployed control plane. When the electronic change detector 167 detects a change, the electronic rescheduling system 165 signals the electronic data transmission scheduling system 160 to calculate a new control plane deployment strategy, according to an embodiment of the invention.

The electronic power utilization manager 168 is a computerized system that automatically controls the energy usage of data transmission nodes and links. After the electronic data transmission scheduling system 160 has output a computer-implementable deployment strategy, according to an embodiment of the invention, the electronic power utilization manager 168 adjusts the energy levels of computerized data transmission nodes and links. The envisaged effect is that the energy level of computerized data transmission nodes and links is adjusted to the level of utilization, such that, e.g., unused links and nodes are powered off completely or operating at lower power levels.

As shown in FIG. 01A, G(V=TM, E) can be used to represent a graph of the computerized network topology 150, where V and E denote computerized data transmission nodes 191-194 and 171-173 and data transmission links between the computerized data transmission nodes 191-194 and 171-173, respectively. T denotes the set of nodes holding electronic aggregators and M represents a candidate set of nodes eligible for hosting a computerized processing entity. N⊆T denotes the set of electronic aggregators that needs to be associated to a computerized processing entity. Further, let each node n∈V have a given probability of being operational, denoted by pn. Analogously, data transmission links (u,v)∈E are operational with probability pu,v. Assume different Independent and Identically Distributed (“i.i.d.”) operational probabilities for network links and nodes. Note, that this probability can be predetermined based on expert knowledge or inferred by learning about the system performance over time.

A variety of methods may be employed for calculating the delay bound. For example, some embodiments of the invention may employ Network Calculus (“NC”) while other embodiments of the invention may employ queuing theory for calculating a stochastic delay bound. The examples herein employ NC, but the ordinary artisan will be aware that other techniques may be employed to calculate the delay bound. Network Calculus (“NC”) may be applied for calculating the worst-case delay and buffer space requirements of flows in a network, according to an embodiment of the invention. “NC”, a system theory for communication networks, is further described below in connection with FIG. 5. To apply NC, estimation (bf, df) of the arrival curve of each flow f is required, where bf denotes the burstiness, and df is the sustainable arrival rate (throughput). Besides, the computerized system also computes the Equivalent Service Curve (“ESC”) γf=(rf, Tf) offered by the network for the flow f, where rf is the service rate and Tf is the maximum service delay. With arrival curve and ESC, the computerized system can then derive the delay bound Df and buffer bound Bf of flow f.

To forward traffic with bounded delay, each node employs a certain guaranteed performance service discipline to schedule flows that require the same output link. For example, suppose the bandwidth and propagation delay of an output link e is (ue, te), and the reserved and guaranteed service rate of a flow is re, re≤ue. Then, if the electronic data transmission scheduling system 160 employs the Weighted Fair Queuing (“WFQ”) discipline, the service curve for the flow is γfe=(re, Lmax/re+Lmax/ue), where Lmax is the maximum packet size, re is the service rate, Lmax/re+Lmax/ue is the maximum service delay. Suppose the flow has an arrival curve of (bf, df), according to NC, the delay bound of the flow for traversing the link is Dfe=Lmax/re+Lmax/ue+te+bf/re, and the backlog bond Bfe=bf+(Lmax/re+Lmax/ue) df. If the electronic data transmission scheduling system 160 employs the Self-Clocked Fair Queueing (“SCFQ”) discipline, the service curve is γfe=(re, Lmax/re+Σm≠f Lmax/ue), where m denotes all the flows to the scheduler, f denotes the target flow. The ordinary artisan may find additional references for more guaranteed performance service disciplines and their corresponding service curves.

Formal Problem Solved by Embodiments of the Invention

The electronic reliability checker 161 shown in FIG. 01A determines the network mapping reliability score as follows, according to an embodiment of the invention. Let binary variables yi denote the computerized processing entity locations, where yi=1 if node i∈M hosts a computerized processing entity, and yi=0 otherwise. Define C={i|yi=1, i∈M} to denote the set of deployed computerized processing entities. Let binary variable aij=1 if electronic aggregator j∈N is associated with the computerized processing entity in i∈C, otherwise aij=0. Although each electronic aggregator j can only be associated with one computerized processing entity at a time, it may have multiple backup computerized processing entities (e.g., in the case of processing entities with Openflow V1.2 protocol). The distance between an electronic aggregator j and a computerized processing entity can be one network link hop or multiple hops. The reliability of node j is represented as R(G, j, C) (among |C| computerized processing entities), capturing the probability of node j connecting with at least one of the operational computerized processing entities. Solutions satisfying the constraints given topological conditions and reliability threshold β are found by R min=min(R(G, j, C), ∀j∈N)>β.

The electronic bandwidth checker 162 shown in FIG. 01A calculates the bandwidth allocations for the network topology as follows, according to an embodiment of the invention. Let (ue, te) represent the bandwidth capacity and propagation delay of each data transmission link e∈E. Let Γ=(ue, te); ∀e∈E. Suppose (sf, tf) being the (source, sink) of traffic flow f. Let (bf, df) denote the burstiness and demand (throughput) of f. Let F={f=(sf, tf, (bf, df))} be the set of all the traffic of the deployed infrastructure. Let Fc⊂F be the inter-traffic of computerized processing entities that Fc={f=(sf, tf, (bf, df))|sf∈C, tf∈C}. Let κf denote all the possible non-loop paths for f∈F, and let κ=∪fκf. Let binary decision variable δ(K), ∀K∈κ to denote whether path K is selected and used for the flow routing. Let variable X(K) denote the reserved guaranteed service rate for the flow f along path K, ∀K∈κ. There will be a sub-flow on path K if and only if δ(K)=1 and X(k)>0. Let Xf={X(K)|K∈κf} denote the reserved guaranteed service rates on all the paths of f. Let Dmax denote the delay bound constraint, and Bmax denote the backlog bound constraint. The electronic resource planner 164 shown in FIG. 01A may also compute some of the equations above as well, according to an embodiment of the invention.

The electronic flow delay checker 163 shown in FIG. 01A may calculate the delay bound of a flow described as follows, according to an embodiment of the invention. Embodiments of the invention assume a flow f can be split and routed on a list of selected paths κ′f={K|δ(K)=1, K∈κf}, with each path route a sub-flow f(k), K∈κ′f. Thus, to calculate the delay bound Df and buffer bound Bf of a flow f, a computerized method and system needs to calculate the delay and backlog bounds of sub-flow f(K), which are denoted as Df(K) and Bf(K), respectively, since one has Df=max {Df(K)} and Bf=max {Bf(K)}. Embodiments of the invention use (bf(K), df(K)) in computerized methods and methods to denote the burstiness and arrival rate (throughput) of the sub-flow f(K). The burstiness of each sub-flow should be less than or equal to the burstiness of the aggregated flow f, according to an embodiment of the invention. Considering the worst case, the computerized method and system can assume bf(K)=bf, ∀K∈κf, according to an embodiment of the invention. The computed summation of the arrival rates of all the sub-flows should equal to that of the aggregated flow, which means ΣK∈κ′fdf(K)=df.

For each sub-flow f(K), given X(K) and the output link bandwidth and flow delay (ue, te) at data transmission link e along the path, by applying Network Calculus (“NC”) and the corresponding service discipline, embodiments of the invention in the form of computerized methods and systems calculate the flow f(K)'s service curve at data transmission link e as δBf(K)=(X(K), Te). Suppose the path of f(K) have k nodes, then computerized methods and systems may calculate the total ESC of path K as δf(K)=(X(K), tsf(K))=δe1f(K)⊗δe2f(K) . . . δe1f(K), e1 . . . ek∈K, by applying the concatenation property of NC. Here ⊗ denotes the min-plus convolution operation in NC. Then, by applying NC, embodiments of the invention derive the delay bound of each sub-flow as Df(K)=ts(K)f+b(K)f/X(K)+Σe∈K te and Bf(K)=b(K)f++ts(K)f d(K)f, where ts(K)f is the service latency and which depends on the used service discipline (e.g., Weighted Fair Queueing). The delay bounded deployment problem requires that for all nonzero sub-flows Df(K)<Dmax, Bf(K)<Bmax, ∀K∈κf, ∀f∈F.

Using the above method, then embodiments of the invention operating as computerized systems formulate the problem to be solved by computerized methods and systems as follows:

\(\begin{matrix}
{{maximize}\mspace{14mu} 0} & \; \\
{{{{s.t.\text{:}}\mspace{14mu} {\sum\limits_{i \in C}a_{ij}}} = 1},{\forall{j \in N}}} & (1) \\
{{\sum\limits_{i \in M}y_{i}} \geq 1} & (2) \\
{{{R\left( {G,j,C} \right)} \geq \beta},{\forall{j \in N}}} & (3) \\
{y_{i},{a_{ij} \in \left\{ {0,1} \right\}}} & (4) \\
{{{\sum\limits_{K \in \kappa_{f}}{{X(K)}\delta^{(K)}}} \geq \; d_{f}},{\forall{f \in F}}} & (5) \\
{{{\sum\limits_{K:{e \ni K}}^{\;}{{X(K)}\delta^{(K)}}} \leq u_{e}},{\forall{e \in E}}} & (6) \\
{{{X(K)} \geq 0},{\forall{K \in \kappa}}} & (7) \\
{{{\sum\limits_{K \in K_{f}}d_{f}^{(K)}} = d_{f}},{\forall{f \in F}}} & (8) \\
{{{\delta^{(K)}\left( {{{ts}_{j}^{(K)}{X(K)}} + b_{f}^{(K)}} \right)} \leq {\left( {D_{\max} - {\sum\limits_{r \in K}t_{e}}} \right){X(K)}}},{\forall{K \in {\kappa_{f}{\forall{f \in F}}}}}} & (9) \\
{{{\delta^{(K)}\left( {b_{f}^{(K)} + {{ts}_{f}^{(K)}*d_{f}^{(K)}}} \right)} \leq B_{\max}},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (10) \\
{{d_{f}^{(K)} \leq {{X(K)}\delta^{(K)}}},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (11) \\
{{d_{f}^{(K)} \geq 0},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (12) \\
{{\delta^{(K)} \in \left\{ {0,1} \right\}},{\forall{K \in \kappa}}} & (13)
\end{matrix}\)

The electronic bandwidth checker 162 shown in FIG. 01A may be configured to execute equations (5), (6), and (7), according to some embodiments of the invention.

Processing components and workflow for embodiments of the invention.

Embodiments of the invention constructed as computerized methods and systems may solve two problems that arise during deployment: 1) determining the number of computerized processing entities, their location and relative connectivity; and, 2) information flow configuration across the infrastructure of deployed computerized processing entities relative to specific performance requirements on bandwidth, flow delay and reliability.

FIG. 01B illustrates a solution to the problems described above obtained in a series of interlinked, iterative optimization steps carried out in line with the computerized workflow 100, according to an embodiment of the invention. The computerized workflow 100 is suitable for implementation in computerized systems, according to an embodiment of the invention. In particular, the computerized workflow 100 is suitable for implementation via the architecture described in FIG. 01A, according to an embodiment of the invention.

The electronic resource planner 164 performs an initial configuration and input (Step 101) that comprises specifying a network topology and its networking properties for a large computerized system such as the computerized system 150 shown in FIG. 01A. The electronic resource planner 164 also inputs operator-specified constraints on the service to be deployed with respect to bandwidth, flow delay and reliability, according to an embodiment of the invention.

The electronic resource planner 164 next performs a mapping (Step 103) of the computerized processing entities in a large network, such as the computerized system 150 shown in FIG. 01A, given the configuration of and inputs to the large network, according to an embodiment of the invention. The electronic resource planner 164 outputs from Step 103 a computer-readable processing entity location map, according to an embodiment of the invention.

The electronic resource planner 164 next performs an association (Step 105) which defines the connectivity among computerized processing entities and electronic aggregators in the computerized system 150 shown in FIG. 01A. The electronic resource planner 164 outputs a computer-readable association plan, according to an embodiment of the invention.

The electronic resource planner 164 next performs a traffic estimation (Step 107) that computes the demand and burstiness of each flow according to the input association plan given a network-operator specified traffic model for the computerized system 150 shown in FIG. 01A, according to an embodiment of the invention.

The electronic bandwidth checker 162 next performs a routability check (step 109) that includes bandwidth verification (step 110) and may optionally include delay and backlog bound verification (step 111), according to an embodiment of the invention. The combined “bandwidth routability verification” (Steps 109/110) tests whether all flows can be routed without overloading any data transmission link relative to specified bandwidth constraints. The inputs to Steps 109/110 are the set of network topology properties and the estimated flow demand and burstiness previously calculated by the electronic resource planner 164 in the traffic estimation step 107. The output is a routability indicator 2. If (A 1) a flow routing plan can be retrieved from the bandwidth checker 162. When the bandwidth checker 162 has performed the bandwidth verification steps 109/110, operations may move to the next step 111. Note: executing step 111 is optional and only required if flow delays are to be accounted for in the deployment plan. If step 111 is not executed, the electronic resource planner will assess the conditions in step 117.

The electronic flow delay checker 163 performs a delay and backlog verification (step 111) that tests whether the estimated flows can be routed under given flow delay and buffer space requirements under the conditions defined by the deployment plan. The electronic flow delay checker 163 also calculates delay and backlog bounds based on the input from the traffic estimates previously calculated in the Traffic Estimation step 107 in the electronic resource planner. If the routability indicator from the previous step 110 in the electronic bandwidth checker is λ<1, then the routability indicator χ will be initialized to χ=λ, meaning that the step 111 will not be executed, and the operation move on to step 117. Otherwise, step 111 will be executed and the output of the electronic flow delay checker 163 will be the calculated routing indicator χ and a flow routing plan, followed by executing the step 117.

In the condition step 117 executed in the electronic resource planner 164, the electronic resource planner 164 determines whether the estimated flows are routable by inspecting a routability indicator. If routable, the electronic resource planner 164 outputs a computer-implementable deployment strategy that meets all requirements. If the electronic resource planner 164 determines that the estimated flows are not routable by inspection of a routability indicator, and the end-conditions are met (i.e. number of maximum iterations), the electronic resource planner 164 will output a null-deployment strategy (a form of computer-implementable deployment strategy), meaning that no satisfactory solution was found. Otherwise, the electronic resource planner 164 performs the association step (step 105) or the mapping step (step 103), according to an embodiment of the invention. The order for signaling the redoMapping (113) or redoAssociation (115) and the number of iterations for re-running step 103 and step 105 can be flexibly defined in an embodiment of the invention.

In various embodiments of the invention, the electronic resource planner 164 may flexibly specify the end-conditions. For example, the electronic resource planner may end the computerized method illustrated in FIG. 01B after a maximum number of iterations, or when all the routability and reliability requirements have been fulfilled. In case the identification of a feasible computer-implementable deployment strategy fails before the end-conditions are met, the electronic resource planner 164 has the following options:


- - change or redefine the topological properties, or
  - check the feasibility of the requirements on bandwidth, flow delay
    or reliability.

Embodiments of the invention may also employ the second option for optimization purposes, since computerized tools may fix two requirements of the three and optimize the remaining one using binary search. For example, embodiments of the invention can fix the flow delay and reliability requirements, and search for the minimum bandwidth needed to satisfy the flow delay and reliability requirements.

Some Practical Considerations

The computerized workflow 100 may be formally expressed mathematically in terms of a feasibility problem, according to an embodiment of the invention. The underlying routing mechanisms of the computerized infrastructure influence the formulation of the problem—if flows cannot be split and routed, then an additional constraint need to be added on the decision variables δ(K), e.g. ΣK∈κf δ(K)=1, ∀f∈F. Computerized systems, such as the computerized system 150 shown in FIG. 01A and mapped in FIG. 2, may be implemented in accordance with available computational resources and operational requirements, according to an embodiment of the invention.

Suitable computing equipment and methods, such as machine learning algorithms for graph problems using distributed computing platforms can process the computerized workflow 100, according to an embodiment of the invention.

One exemplary implementation of the computerized workflow 100 is provided below. For applying the exemplary computerized workflow 100 for deploying the control plane for Software Defined Networks, the computerized processing entities are network controllers. According to the mechanisms of the infrastructure, there are two ways to organize the control plane, which are in-band control and out-of-band control.

With out-of-band control all the computerized processing entities communicate with each other using dedicated networks (e.g., dedicated networks running in remote clouds), according to an embodiment of the invention. In contrast with in-band control, both computerized processing entity and electronic aggregator traffic share the same network. Embodiments of the computerized workflow 100 may be configured to support both cases, although the out-of-band case may additionally require that the paths for the inter-processing entity traffic Fc should be limited within the computerized control network. This limitation has already been implicitly included in the definition of the set κf. The κf is defined as the set of all the possible paths for a certain flow f. A possible path for flow f∈Fc in the out-of-band case can only be selected among data transmission links belonging to the control network.

Differences to the Known Prior Art

Some prior art comprises a heuristic computerized processing entity placement method but provides no considerations regarding control plane routability and reliability.

Other prior art focuses on the placement of SDN switches, rather than processing entities. Moreover, this prior art only tries to place a minimum number of SDN-enabled switches in a hybrid SDN network to achieve 100% single-link failure coverage. This prior art does not consider flow demands and link capacity constraints.

Still other prior art proposes a network controller placement and electronic aggregator association method configured to avoid single link/node failure, without the control plane traffic routability check and delay and backlog check steps.

Some other prior art describes a method for placing SDN controllers in a way that the delay may be optimized. Nevertheless, this prior art also does not take control plane traffic routability issue into consideration when doing the placement.

Still other prior art comprises allocating computing and network resource for a given number of VMs. However, this method does not have proper network flow delay estimations.

Finally, some prior art comprises a method for allocating processing entities to electronic aggregators. This prior art is similar to the association step 105 shown in FIG. 01B, but this prior art has neither a routability check step nor placement step.

To summarize, the prior art differs from embodiments of the present invention in mainly two ways: 1) the prior art solves the placement problem with methods significantly different from the invention; and 2) the prior art does not consider and address the reliability, bandwidth and flow delay aspects of a computer-implementable deployment strategy properly.

Advantages and Applications

The most prominent feature of various embodiments of the invention is that can solve problems relevant to several practical applications in large distributed computing systems. Hence, embodiments of the invention are widely applicable to automated resource management problems requiring guaranteed performance and reliability of information flows.

Examples of applications that benefit from embodiments of the invention are many and include:


- - Distributed big data computations, where resource allocation and
    synchronization of partial results require data transactions under
    certain performance requirements and reliability guarantees.
  - Deployment of logically centralized control planes in
    Software-Defined Networks, where data transactions for synchronized
    information updates need to be carried out in line with specified
    performance requirements and reliability guarantees to maintain
    information consistency and service availability.
  - Self-organization of wired and wireless communication
    infrastructures (e.g. sensor networks) requiring multiple cluster
    heads selection and association of nodes and flows following
    performance and reliability requirements.
  - Scaling of virtualized network (“VN”) functions implementing elastic
    services, which require performance and reliability guarantees of
    deployed flows to ensure service availability and quality.
  - Organization of wireless access networks, associating access points
    and base stations as electronic aggregators with distributed
    computerized processing entity instances (computerized processing
    entities) as part of a distributed evolved packet core.
  - Cell association of wireless equipment (electronic aggregators) to
    dynamically deployed virtual access points or base stations
    (computerized processing entities), allowing for turning on and off
    access infrastructure relative to, e.g., changing user
    concentration, service usage intensity or energy efficiency
    requirements (note: this assumes fixed or close to fixed location of
    transceivers).

Embodiments of the invention not only provide computerized systems that calculate the worst-case delay, but also provide computerized systems based on mathematical models and theories that effectively guarantee that the affected data flow transmissions in the computerized network will not exceed such calculated worst-case delay.

Thus, embodiments of the invention may be considered to offer guarantees. In contrast, others in the prior art claims to delay reduction are only based on experience or experimental observations and cannot provide any theoretical guarantees. The prior art is not known to offer delay guarantees for all flows in the network.

Second, the delay in most queuing systems mainly comprises: queuing delay and propagation delay. The prior art only considers the propagation delay but not queuing delay.

Third, the proposed workflow has the delay and backlog check step together with the other four steps in one iterative process. It is not typically a good idea to running them separately, e.g., running a main iteration with the other four steps to determine mapping and association, and then running a separate iteration which only contains has the delay and backlog step to schedule flow paths to meet the worst-case flow delay constraints. This is due to that in order to find a flow scheduling that meets the worst-case delay constraints, the optimization procedure may have to alter the mapping and association plans. This is a complicated and non-trivial iterative optimization process.

Embodiments of the invention may be applied to problems of the same class independently of the specific properties of the underlying computerized network topology and networking conditions, allowing the system operator to specify traffic models, topological properties and end-conditions arbitrarily for execution by the computerized system. Furthermore, each step of the computerized workflow 100 shown in FIG. 01B enables a flexible implementation based on any suitable computerized method of choice (heuristic methods, machine learning, exhaustive search, etc.) and is hence adaptive to the computerized system at hand, in terms of computational capacity, platforms and software.

Moreover, embodiments of the invention offer flexible usage as an offline tool for analyzing and quantifying the effects of computer-implementable deployment strategies in a networked system, or as an integrated online process in a system implementing automated resource management. For example, embodiments of the invention can be used as a tool by a network operator to analyze and plan different computer-implementable deployment strategies fitted to different service availability scenarios with different requirements on reliability, bandwidth and end-to-end delay (see, FIG. 03 and FIG. 04). As an online process, embodiments of the invention may be integrated in computerized systems implementing service elasticity.

An application example of the computerized workflow 100 shown in FIG. 01B may comprise a distributed control plane deployment in SDN, according to an embodiment of the invention. This example demonstrates the applicability of embodiments of the invention to the distributed control plane deployment problem, which here encompasses computerized processing entity placement and associated control traffic of a distributed control plane that appears logically centralized. In this context, a computerized processing entity such as 173 in FIG. 01A corresponds to an SDN controller (or control instance), whereas an electronic aggregator corresponds to a network switch, such as 192 in FIG. 01A. The objective of the computerized workflow 100 here is to produce a computer-implementable deployment plan that identifies: (1) the control service infrastructure of processing entities (control instances); (2) the associated electronic aggregator connections; and, (3) the traffic flows relative to specified reliability, bandwidth and flow delay requirements.

This example presents three major challenges. First, the control instances should preferably be placed in a manner that satisfies the given constraints on reliability. This includes decisions on how many control instances to use, where to place them and how to define their control regions. The computerized processing entity (SDN controller) placement problem in general is NP-hard. Second, the computerized system must verify that the control traffic introduced by a placement solution can be scheduled on the underlying network without overloading any network link. Third, the computerized system as the electronic data transmission scheduling system in 160 must verify the control traffic flows can be routed in way that the required delay and backlog bounds are held.

To solve the first problem, the prior art offers a general resort to heuristics to reduce the search space as the computerized processing entity placement problem in general is NP-hard. The second problem can be modelled as a multi-commodity flow problem for the verification of the routability. The third problem is a Mixed Integer Programming (“MIP”) problem, which is NP-complete. This kind of problem may be generally solved by employing random search algorithms.

The following subsections illustrate how each step of an embodiment of the computerized workflow 100 shown in FIG. 01B may be applied to solve the distributed control plane deployment problem.

Details of the computerized workflow 100 used in this example

Recall, that embodiments of the invention operate in a workflow comprising six steps, as shown in FIG. 01B. The following subsections outline each step in detail with respect to the control plane deployment problem.

Mapping (Step 103) as Employed in this Example

The generality of the optimization process allows for a black-box implementation, expressed in this example using Simulated Annealing for Mapping (“SAM”). In short, the computer-implementable SAM algorithm (for a computer-implementable deployment strategy) executed in electronic resource planner 164 follows the standard simulated annealing template, except that the SAM algorithm generates a new solution and decreases the temperature T when receiving the redoMapping signal. A computerized method and system for generating a new solution is designed as randomly adding or removing a computerized processing entity based on the current mapping solution.

In some embodiments of the invention, the electronic resource planner 164 may calculate computer-implementable cost (energy) function for evaluating a mapping with respect only to bandwidth routability may be defined as:

\({cost} = {\min \left( {0,{\log_{10}\frac{1 - R_{\min}}{1 - \beta}},{\lambda - 1}} \right)}\)

In other embodiments of the invention, the electronic resource planner 164 may calculate the computer-implementable cost (energy) function for evaluating a mapping with respect to bandwidth and flow delay routability may be defined as:

\({cost} = {\min \left( {0,{\log_{10}\frac{1 - R_{\min}}{1 - \beta}},{\chi - 1}} \right)}\)

The electronic bandwidth checker 162 shown in FIG. 01A may calculate λ in the bandwidth verification (step 110), according to an embodiment of the invention. λ indicates whether control traffic is routable (λ≤1) under bandwidth and reliability constraints or not (λ<1). When bandwidth and reliability constraints are satisfied, the cost function calculated in the electronic resource planner 164 reaches its maximum value 0.

The electronic flow delay checker 163 shown in FIG. 01A may calculate χ in the delay and backlog bound verification step (step 111), according to an embodiment of the invention. χ indicates whether control traffic is routable (χ≥1) under the delay and backlog constraints or not (χ<1). When delay, backlog and reliability constraints are satisfied, the cost function calculated in the electronic resource planner 164 reaches its maximum value 0.

Since directly computing the reliability R(G, j, C) is NP-hard, the computerized approximation method and system in this example is applied for computing instead a lower bound:


- -

The electronic reliability checker 161 shown in FIG. 01A may be configured to perform the computations immediately above, according to an embodiment of the invention. An algorithm example is provided below, where the transition probability function P defines the probability with which a new mapping will be accepted and a computer function (getNextSolution function in Algorithm 1) generates a new mapping by randomly adding, removing or moving a control instance based on the previous mapping:

The electronic reliability checker 161 employs a computerized approximation method to first compute the set of the disjoint paths from an electronic aggregator j to all the processing entities C, noted as κj. Given the i.i.d operational probability of links/nodes on each disjoint path, this computerized method calculates the failure probability of each path, noted as Fk, k∈κj. Then, the electronic reliability checker 161 computes the:

=1−Πk∈κFk

Association (Step 105)

The electronic resource planner 164 employs a computerized algorithm the performs simulated annealing for association (SAA) and is similar to SAM, according to an embodiment of the invention. One difference relates to the cost function cost=min(0, λ−1) (or cost=min(0, χ−1)) maintained by the electronic resource planner 164. The other difference is that the electronic resource planner 164 may also generate a new solution by a random association of electronic aggregators and processing entities towards obtaining a satisfying solution. This procedure (getNextSolution for association) is exemplified in the algorithm description below by the computer function in Algorithm 2 (getNextSolution for association). The association step is executed after the Mapping step (step 103) or upon receiving the redoAssociation signal.

Traffic estimation (Step 107)

The electronic resource planner 164 estimates the bandwidth demands of electronic aggregator-processing entity and processing entity-processing entity flows, according to an embodiment of the invention. Let (sf, tf, df, bf) represent the source, sink, demand and burstiness of a flow f respectively. The objective of the electronic resource planner 164 here in this Traffic Estimation step is to estimate each (df, bf) while sf and tf are known from the mapping (step 103) and association steps (step 105). The result of the Traffic Estimation step is used as input for the routability check step 109, involving the bandwidth verification step 110 and possibly the delay and backlog verification step 111.

Since the optimization process performed by the electronic resource planner 164 process treats the model of control traffic as an input variable, embodiments of the invention may employ any known computerized traffic model for estimating each (df, bf). For example, embodiments of the invention can perform the modeling with either a simple linear modelling method or advanced machine learning techniques.

Here is a simple traffic estimation model suitable for the electronic resource planner 164, associated with an embodiment of the invention. First, for computerized demand estimation assume that the message sizes of electronic aggregator request and corresponding computerized processing entity response are Treq=128 and Tres=128 bytes, respectively. Furthermore, after dealing with a request, the computerized processing entity instance sends messages of size Tstate=500 bytes to each of the other |C|−1 control instances notifying about the network state changes. Note that, the computerized traffic model here is essentially in line with the ONOS traffic model. The electronic resource planner 164 sets message sizes according to various parameters known to an ordinary artisan but can also be set arbitrarily. With these parameter settings and given the request rate rj, j∈N of each electronic aggregator, embodiments of the invention can simply estimate the flow demand between electronic aggregator j and its associated computerized processing entity is rjTreq and rjTres, for electronic aggregator-processing entity direction and processing entity-electronic aggregator direction, respectively. A computerized simple linear model may estimate the outgoing inter-control flow demand from computerized processing entity i to another computerized processing entity, which is described as TresΣj∈N aijrj. Second, the computerized methods employed here may estimate the burstiness of a flow f as bratiodf, where br is a burstiness ratio. We assume the burstiness of a flow is proportional to its demand.

Bandwidth Verification (Step 110)

The electronic bandwidth checker 162 shown in FIG. 01A computerized step checks whether all flows can be routed without overloading any data transmission link relative to specified bandwidth constraints, with all the possible paths. As discussed, the electronic bandwidth checker 162 calculates the routability indicator λ (executing the estλ and FPTAS algorithms). Thus, computerized implementations of this step assume δ(K)=1, ∀K∈κ and checks whether constraints (5), (6), (7) (provided above) can hold, which may be solved using a computerized linear programming (LP) method. However, solving this routability problem using computerized methods still means dealing with an undesired large number of variables X(K), which scales up exponentially with the number of vertexes and edges with a graph. This issue can be circumvented by formulating in a computer a maximum concurrent flow problem (as (15), (16), (17), (18) suggest below), which is easier to solve and equivalent to the multi-commodity flow problem.

The electronic bandwidth checker 162 shown in FIG. 01A may calculate maximum concurrent flow in the network, according to an embodiment of the invention. The fundamental idea of the maximum concurrent flow problem is to keep the capacities of the data transmission link fixed while scaling the injected traffic so that all flows fit in the network. The optimization objective λ reflects the ratio of the traffic that can be routed over the current injected traffic. If the computerized methods obtain λ≥1, the current traffic is routable, and all data transmission link utilizations are less than one. The computerized interpretation is that more traffic variation can be tolerated with check larger λ.

\(\begin{matrix}
{{maximize}\mspace{14mu} \lambda} & (15) \\
{{{{s.t.\text{:}}{\sum\limits_{K:{ɛ \ni K}}^{\;}{X(K)}}} \leq u_{e}},{\forall{e \in E}}} & (16) \\
{{{\sum\limits_{K \in \kappa_{f}}{X(K)}} \geq {\lambda \; d_{f}}},{\forall{f \in F}}} & (17) \\
{{{X(K)} \geq 0},{\forall K}} & (18)
\end{matrix}\)

The dual of the above maximum concurrent flow problem, as specified in (19)-(20) below, where le,zf are the dual variables of edge constraints (16) and flow constraints (17), respectively, has a linear number of variables and an exponential number of constraints, according to an embodiment of the invention. This approach allows for a computerized solution to the problem to a desired level of accuracy using a primal-dual algorithm. A computerized method can perform the primal-dual algorithm based on Fully Polynomial Time Approximation Schemes (FPTAS). An embodiment of the invention may implement e.g. the “Fast Approximation Scheme” (FAS) algorithm by Karakostas [GKA08] as a computerized algorithm, in which case the computerized method can obtain the near-optimal λ, which is guaranteed within the (1+ε) factor of the optimal, within the time complexity of O(ε−2|E|2 logO(1)|E|). The Karakostas [GKA08] FAS algorithm is further detailed in “Faster approximation schemes for fractional multicommodity flow problems,” Transactions on Algorithms (TALE), vol. 4, no. 1, p. 13, 2008, which is incorporated fully herein by reference.

\(\begin{matrix}
{\mspace{79mu} {{{minimize}\mspace{14mu} {D(l)}} = {\sum\limits_{c \in E}\text{?}}}} & (19) \\
{\mspace{79mu} {{{s.t.}:{{\sum\limits_{c \in K}^{\;}l_{c}} \geq {zf}}},{\forall{f \in F}},{\forall{K \in \kappa_{f}}}}} & (20) \\
{\mspace{79mu} {{\sum\limits_{f \in F}{d\text{?}z_{f}}} \geq 1.}} & (21) \\
{\mspace{76mu} {{l_{c} \geq 0},{\forall{e \in E}}}} & (22) \\
{\mspace{76mu} {{{z_{f} \geq 0},{\forall{f \in F}}}{\text{?}\text{indicates text missing or illegible when filed}}}} & (23)
\end{matrix}\)

Another embodiment of the invention used for control plane deployment (or similar problems) may implement a faster variant of FAS based on FPTAS by only iterating the computation through controller nodes rather than through all nodes. This significantly reduces the total number of iterative steps and, hence, the computational complexity as the number of controllers are substantially fewer than the number of nodes in a computerized network. An example algorithm of FPTAS is outlined below:

The computerized bandwidth verification step (step 110) will ultimately output the optimal value of λ and the corresponding solution {X*(K)}.

In an embodiment of the invention, the electronic bandwidth checker 162 shown in FIG. 01A calculations for the bandwidth verification step (step 110 shown in FIG. 01B) can be accelerated by implementing the computerized algorithm estλ in the electronic bandwidth checker 162 that assesses if λ≥1. Such a computerized algorithm calculates λlow and λhigh. If both λlow>1 and λhigh<1, then a computerized FPTAS based algorithm may be executed to calculate λ. Otherwise, λ=(λlow+λhigh)/2.0 is returned without execution of a computerized FPTAS based algorithm. An example algorithm is provided below:

The combination of a computerized algorithm FPTAS based on a faster modified variant of FAS and the computerized algorithm estλ for assessing if λ≥1 may reduce the running time of the bandwidth verification step 110 by a level of 50× compared to the prior art implementation of FAS. In practice, this means for large topologies a reduced running time from days or hours down to minutes and seconds.

FIG. 01C Illustrates the optimization time with different implementations of the bandwidth verification when Simulated Annealing (denoted AA) is used for mapping and association, which are suitable for application with embodiments of the invention. The network topologies are from “The internet topology zoo. [Online]. Available: http://www.topology-zoo.org/” depicted on the x-axis are arranged in increasing size order.

As shown in FIG. 07A, when combining simulated annealing (AA) for the mapping and association steps with our estλ calling the FPTAS algorithm in one embodiment of the invention, the running time under all topologies is significantly reduced compared to using FAS for large networks. In another embodiment of the invention, the Mapping and the Association steps may be implemented by the use of the FTCP algorithm described in prior art “F. J. Rosand P. M. Ruiz, “On reliable controller placements in software-defined networks,” Computer Communications, vol. 77, pp. 41-51, 2016” in combination with the estλ.

FIG. 01D Illustrates the optimization time with different implementations of the bandwidth verification when the FTCP heuristics (FS) is used for mapping and association, which are suitable with embodiments of the invention. The network topologies are from “The Internet topology zoo. [Online]. Available: http://www.topology-zoo.org/” depicted on the x-axis are arranged in increasing size order.

FIG. 01D illustrates significant reduction in running time when FTCP (denoted FS) is combined with estλ or FAS, respectively.

Delay and backlog bound verification (Step 111)

The electronic flow delay checker 163 calculates the routability indicator χ with respect to delay. The computerized delay and backlog bound verification step (step 111) follows the bandwidth verification step (step 110). If λ<1, the computerized method returns with χ=λ. Otherwise, the electronic flow delay checker 163 shown in FIG. 01A may engage a computerized Genetic Algorithm or a Column Generation Heuristic Algorithm to determine whether there is a routing solution that satisfies the delay and backlog constraints, according to an embodiment of the invention. An example algorithm of the delay and backlog verification step 111 based on CGH is shown below:

An embodiment of a suitable computerized Genetic Algorithm uses {Xf, ∀f∈F} as the genes. The computerized Genetic Algorithm uses the solution {X*(K)} produced by the bandwidth verification step (step 110), to initialize its population (the initial population are generated by random permutations of {X*(K)}. The computerized Genetic Algorithm calculates the fitness of each individual as fitness=min(D max/D*, B max/B*), with D* and B* denoting the delay and backlog bound produced by the individual. After running a certain number of generations, the computerized Genetic Algorithm outputs the χ=max{fitnesses}.

Another embodiment of a suitable computerized Column Generation Heuristic (CGH) Algorithm formulates the delay and backlog verification problem as an optimal flow scheduling problem and checks whether it is possible to schedule all the flows under bandwidth, delay and backlog constraints. However, instead of considering all the possible paths set κ when scheduling flows, the CGH algorithm uses certain heuristic to select a small subset of paths κ′⊆κ. The key of CGH is to split the problem into a master problem and subproblem. The master problem is here the maximum concurrent flow problem but for a subset of the paths κ′⊆κ. The subproblem based on (20) is created to identify new variables that can improve the objective function of the master problem. The heuristic implemented by CGH is comprises three steps, iterated until no new variables can be found: 1) solving the master problem with a subset of the variables and obtaining the values of the duals; 2) considering the subproblem with the dual values and finding the potential new variable; and, 3) repeating step 1) with the new variables that have been added to the subset. This allows us to optimize flow scheduling only within this subset of paths rather than considering the whole set of the paths. By doing this, the search space can be greatly reduced, which can dramatically reduce the running time by the magnitude of 500× for uniform traffic patterns or 1000× for control traffic patterns compared to using MILP solvers such as CPLEX to directly solve the problem as shown in FIG. 01E.

FIG. 01E illustrates a representative time reduction ratio when comparing the CGH algorithm with CPLEX for network topologies of increasing size for uniform traffic (left) and control traffic patterns (right), respectively, suited for embodiments of the invention. The network topologies are from “The internet topology zoo. [Online]. Available: http://www.topology-zoo.org/”.

In one embodiment of the invention implementing the CGH, we observe in FIG. 01E the aforementioned reduction for various topologies of increasing size. [SLI19].

Executing the entire process 100 as illustrated in FIG. 01B in an embodiment of the invention can for a mid-sized network topology yield a deployment plan within seconds, as illustrated in FIG. 01F. In an embodiment of the invention, applying CGH rather than CPLEX can lead to a reduction in running time by 80×, in comparison.

FIG. 01F illustrates the time total running time for calculating a deployment plan for combinations of algorithms implementing various embodiments of the invention. The network topology “InternetMCI” is available at “The internet topology zoo. [Online]. Available: http://www.topology-zoo.org/”.

Exemplary Use Cases Employing Embodiments of the Invention

One can apply at least two use cases to embodiments of the invention described herein.

Case 1: Computer-Implementable Deployment Strategy Output

FIG. 02 illustrates a computerized processing entity deployment strategy operating under certain constraints and a given network topology 200, according to an embodiment of the invention. FIG. 02 further illustrates a corresponding deployment plan employing computerized processing entity instances (201-204) of the computerized processing entity instances 201-219 and an association plan (denoted as Node ID/Associated Processing entity ID, e.g., for the computerized processing entity instance 205, the Node ID is 1 and the Associated Processing entity ID is 13, as shown in FIG. 2), in an instance when the minimum required reserved bandwidth is 36 MBits/s per data transmission link, given the reliability threshold β=0:99999 and requirement Rmin>β.

The network topology 200 is taken from the Internet topology Zoo (ITZ) known as “Internetmci”. For simplicity, the computerized method may assume an in-band control scheme that M=N=T, according to an embodiment of the invention.

The electronic data transmission scheduling system 160 may further assume that each node of the nodes 201-219 holds an electronic aggregator having a request rate of 500 requests/s and link propagation delay ranges [1 ms, 10 ms] and that the operational probability of each node 201-219, data transmission link and computerized processing entity is 0.9999. Given a reliability, bandwidth and backlog constraints as (β=0.9999, ue=400 Mbits/s, Bmax=10 MBytes), embodiments of the invention may output a computerized processing entity deployment solution that ensures worst case flow delay of 180 ms, as shown in FIG. 2.

Case 2: Analytic Tool

Embodiments of the invention may provide an electronic data transmission scheduling system 160 that provides a computerized analytic tool, possibly in the form of a physical simulator, configured to systematically assess the impact of a given computer-implementable deployment strategy relative to reliability, bandwidth and flow delay. For example, embodiments of the electronic transmission scheduling system 160 can quantify the influence on the achieved maximum reliability relative to an increasing data transmission link bandwidth constraint (see, FIG. 3). In this embodiment, given flow delay and backlog constraints fixed, by varying the bandwidth of data transmission links in a network, the computer-implemented method can test how good deployment solutions for the workflow 100 shown in FIG. 01B can found in terms of reliability. The electronic transmission scheduling system 160 may detect that when scaling up the data transmission link bandwidths in a network topology, the failure probability decreases, and hence Rmin increases. This example illustrates how service providers and operators can use embodiments of the invention as a practical tool for quantifying the trade-off between bandwidth and reliability. It may help them to make decisions such as how much investment should be put on upgrading the network infrastructure, and what is the expected gain on reliability.

FIG. 03 provides a graph of failure probability versus link bandwidth that may be used by the electronic data transmission scheduling system 160 may determine what are the minimum data transmission link bandwidths that a worst-case-delay-guaranteed deployment solution needs.

FIG. 04B provides a graph that quantifies the influence on the achieved reliability relative to the worst-case delay constraints of control traffic flows, according to an embodiment of the invention. Given the bandwidth and backlog constraints fixed, with different delay bounds requirement, a computerized system can determine what are the maximum reliability a deployment solution can achieve.

As the electronic data transmission scheduling system 160 reduces the delay bound, the required bandwidth for guaranteeing such a delay bound increases, as shown in FIG. 4A. The graph shown in FIG. 4A illustrates how service providers and operators can employ embodiments of the invention as a practical tool for quantifying the trade-off between the flow delay they want to guarantee and the bandwidths of the network infrastructure they should have, enabling development of flexible and fine-tuned computerized processing entity deployment policies.

### Example #2: Deployment of VMs for a Cloud Computing Task

Deploying and executing a computational task in a distributed big data framework and architecture (e.g., Apache Spark or similar), is essentially identical to deploying a distributed control plane. Such an architecture generally allows for distributing a computation task within or across geo-distributed data centers. Within the context of a cloud computing application of a distributed cloud computing architecture, a manager entity, such a computerized management function within data transmission node 171 shown in FIG. 01A carries out computational tasks by controlling one or many computerized worker entities. Each computerized worker entity (e.g., switches 192) may host one or several computerized distributed agents which each may handle one or several computation tasks.

In this context, the electronic data transmission scheduling system 160 may map the deployment of a distributed computational infrastructure (or application), by deciding the distributed set of managers (the number and location in a network topology) and the association of computerized worker entities, according to an embodiment of the invention. In the cases when the framework (or similar) allows for it, embodiments of the invention could also be applied to also associate worker entities (e.g., switches like 192) to distributed agents running on external nodes.

Such a deployment may be viewed as an abstract overlay representing the intercommunication necessary to solve a big data problem in a distributed manner and with guaranteed network reliability and performance. Embodiments of the invention may thus be used to deploy entities for executing cloud computations while accounting for reliability, bandwidth and flow delay, such that the requirements in critical cloud computing applications (e.g., to support decision-making in real-time services) can be adequately met.

Note that embodiments of the invention focus on network I/O constraints of a computing infrastructure and generally not on the computational resources of each computational entity. To accomplish this task, additional constraints like the computation capability of a computerized worker need to be considered, which decides how many executors can co-exist on a worker or on another host.

### Application Example #3: Deployment of a VNF Service Chain

Embodiments of the invention may be used to deploy service chains comprising a series of connected VNF instances. In this case, embodiments of the invention, namely the electronic data transmission scheduling system 160, essentially deploy computerized processing entities (e.g., data transmission nodes 171) (corresponding to the VNFs) without associating any electronic aggregator nodes—consequently, the reliability requirement becomes irrelevant.

Hence, computerized processing associated with this embodiment of the invention is simplified to placement of a given number of VNFs on a network topology while accounting only for bandwidth and flow delay requirements. In practice this is achieved by setting the reliability R(G, j, C)=1) and assuming N∈Ø. To solve the deployment problem, a computerized system executes the steps from Workflow 100 shown in FIG. 01B, except for the “Association” step (step 105 shown in FIG. 01B), according to an embodiment of the invention.

Additional Considerations Regarding Network Calculus

FIG. 05 illustrates an example of graphical computation of flow delay bound and backlog bound using network calculus concepts, according to an embodiment of the invention. The flow delay and backlog bounds respectively correspond to the maximum horizontal and vertical deviations between the arrival and service curves.

Network calculus (“NC”) comprises a system theory for communication networks. An NC system can range from a simple queue to a complete network. With the models of a considered flow and of the service a so-called system can offer, three bounds can be calculated by network calculus, which are (i) the delay bound the flow will experience traversing the system, (ii) the backlog bound the flow will generate in the system, and (iii) the output bound of the flow after it has passed the system. The theory is divided in two parts: deterministic network calculus, providing deterministic bounds, and stochastic network calculus, providing bounds following probabilistic distributions. The discussion here only considers the former.

As an explanation for the motivation behind the optimization formulation (discussed herein) that is behind the flow delay checker 163, note that the arrival curve 501 and service curve 503 are the two key concepts in the network calculus. Among other things, the electronic flow delay checker 163 shown in FIG. 01A employs the curve 501 and the curve 503 in optimizing delay and backlog bounds. The arrival curve α(t) 501 defines the upper bound of the injected traffic during any time interval. Suppose the total amount of data a flow sends during any time interval [t1, t2] is R(t2)−R(t1), where R(t) is the cumulative traffic function which define the traffic volume coming from the flow within the time interval [0, t]. A wide sense increasing function α(t) is the arrival curve of the flow if ∀t1, t2, 0≤t1≤t2, if it satisfies

R(t2)−R(t1)≤α(t2−t1)  (19)

In practice, a linear arrival curve is widely used to characterize the flow injection in a network. The modeling of a flow f uses a so-called arrival curve αf(t)=lbf′df=df t+bf, where df is the sustainable arrival rate and bf is the burst/ness. The linear arrival curve 501 shown in FIG. 5 can be interpreted as that the flow can send bursts of up to bf bytes but its sustainable rate is limited to df B/s. A flow can be enforced to conform to the linear arrival curve 501 by applying regulators, for example, leaky-buckets.

The Service Curve γ(t) 503 models a network element, e.g. a switch or a channel, expressing the service capability. Its general interpretation is less trivial than for the arrival curve 501. The service curve γ503 shown in FIG. 5 can be interpreted as that data of a flow has to wait up to T seconds before being served at a rate of at least r B/s. This type of service curve is denoted by γr,T and is referred to as a rate-latency service curve.

From the two curves 501, 503, the three above mentioned bounds can be calculated by the electronic flow delay checker 163, as shown in FIG. 5. The flow delay bound is graphically the maximum horizontal deviation between α(t) and λ(t). Its general interpretation is less trivial than for the arrival curve 501. As shown in FIG. 5, the backlog bound corresponds to the largest vertical distance between α(t) and γ(t). Consider the case with linear arrival curve 501 and rate-latency service curve 503, the flow delay bound can be calculated as

D*=T+b/r  (20)

and the backlog bound as

B*=b+Td.  (21)

Thus, D* and B* relate to each other as shown by equations (20), (21).

In the general case, the computation of the output bound α*, the arrival curve of the flow after traverse the system, is calculated by min-plus deconvolution between α(t) and γ(t), as α*

\(\begin{matrix}
{\alpha^{*} = {{\left( {\alpha \; \; \gamma} \right)(t)}=={\sup\limits_{u \geq 0}\left\{ {{\alpha \left( {t + u} \right)} - {\gamma (u)}} \right\}}}} & (22)
\end{matrix}\)

The computation is not straightforward, since it involves the deconvolution operation defined by min-plus algebra. However, in the case that a flow is modelled by a linear arrival curve and served by a rate-latency service curve, one simply has α*=lb+T, r=rT+b+rT.

Concatenation Property of Network Calculus

Assume a flow traverses two systems that provides service curve γ1 and γ2 respectively. Then, the Equivalent Service Curve (ESC) by the concatenated system is calculated by min-plus convolution between γ1 and γ2, as

\(\begin{matrix}
{{\gamma (t)} = {{\left( {\gamma_{1} \otimes \gamma_{2}} \right)(t)} = {\inf\limits_{0 \leq s \leq t}\left\{ {{\gamma_{1}\left( {t - s} \right)} + {\gamma_{2}(s)}} \right\}}}} & (23)
\end{matrix}\)

In particular, if both γ1 and γ2 are rate-latency service curves, e.g. γ1=γr1, T1 and γ1=γr2,T2, we can simply have γ=γ1⊗γ2=γmin(r1,r2), T1+T2. A computerized system can thus deduce the ESC for a given flow that traverses multiple network elements (e.g. switches) in a system by applying the concatenation property.

Applying Network Calculus for Calculating the Delay Bound of a Deployment Plan

A computerized system such as the electronic flow delay checker 163 can apply Network Calculus in computing the delay and backlog verification step (step 111 shown in FIG. 01B), as follows:


- - 1. Assume that each computerized node (and/or application specific
    hardware) uses a certain guaranteed performance service discipline
    to schedule flows that sharing a data transmission link. How to
    handle different guaranteed performance service disciplines and
    their corresponding service curves are known to those skilled in the
    art. Generally speaking, such a service curve is a function of the
    reserved guaranteed service rate (X(K)) of the flow.
  - 2. A path can traverse several nodes and data transmission links and
    can be viewed as a concatenation of systems. Thus, given the
    reserved service curve of a flow at each of such nodes, by applying
    the concatenation property, a computerized system can derive the ESC
    of the entire path for a target flow by applying equation (23). In
    general, the ESC of the path is still a function of reserved
    guaranteed service rate (X(K)) of the flow. However, X(K) needs to
    satisfy constraints (5) (6) (7) (9) (11).
  - 3. A computerized system such as the electronic flow delay checker
    **163** can split and route a flow on a list of selected paths
    κ′_(f). Suppose the arrival curve of a flow is α_(f)=l_(bf, df),
    after splitting, the computerized system such as the electronic flow
    delay checker **163** obtains a number of sub-flows {f^((K))}, with
    each one having the arrival curve α_(f(K))=l_(bf(K), df(K)). A
    computerized system such as the electronic flow delay checker
    **163** may assume b_(f(K))=b_(f) by considering the worst case. The
    computerized system such as the electronic flow delay checker
    **163** also has the Σ_(K∈k′f) d_(f(K))=d_(f) (constraints (8)),
    indicating that the summation of all the sub-flow demands should be
    equal to the demand of their aggregated flow.
  - 4. Now, given the arrival curve of a sub-flow and the corresponding
    service curve of the path for routing the sub-flow, the computerized
    system such as the **163** can calculate the delay bound (D\*) and
    backlog bound (B\*) for the sub-flow with equation (20), (21)
    respectively. Such bounds should satisfy the delay and backlog
    constraints (constraints (9) (10)).

One note regarding how burstiness relates to χ. The burstiness of a flow is calculated in the electronic resource planner 164 in the Traffic Estimation step according to the definition of the linear arrival curve mentioned above. The burstiness directly impacts the worst-case flow delay (D*) of a flow, see equation (20).

As noted above, in some embodiments of the invention and under certain circumstances, queuing theory, for example, may be also used for calculating a stochastic delay bound instead of Network Calculus.

Introduction of the column generation heuristic algorithm for delay and backlog verification.

The delay and backlog verification problem can be formulated as the Mixed Integer Linear programming (MILP) problem specified in (24)-(33). By solving the optimization problem, if we obtain χ≥1, it indicates that a feasible routing solution satisfy bandwidth, delay and backlog constraints is found. The number of binary variables δ(K) in the problem could be potentially very large, since it equals to the number of possible paths in a network topology, which increases exponentially with the size of the network topology.

\(\begin{matrix}
{{maximize}\mspace{14mu} \chi} & (24) \\
{{{{s.t.\text{:}}\mspace{11mu} {\sum\limits_{K:{ɛ \ni K}}^{\;}{X(K)}}} \leq u_{e}},{\forall{e \in E}}} & (25) \\
{{{X(K)} \geq 0},{\forall{K \in \kappa}}} & (26) \\
{{{{\sum\limits_{K \in \kappa_{f}}d_{f}^{(K)}} \geq {\chi \; d_{f}}},{\forall{f \in F}}}{{{{{ts}_{f}^{(K)}{X(K)}} + {b_{f}^{(K)}\delta^{(K)}}} \leq {\left( {D_{\max} - {\sum\limits_{e \in K}t_{e}}} \right){X(K)}}},}} & (27) \\
{{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (28) \\
{{{{b_{f}^{(K)}\delta^{(K)}} + {{ts}_{f}^{(K)}d_{f}^{(K)}}} \leq B_{\max}},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (29) \\
{{X(K)} \leq {M\; \delta^{(K)}}} & (30) \\
{{d_{f}^{(K)} \leq {X(K)}},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (31) \\
{{d_{f}^{(K)} \geq 0},{\forall{K \in \kappa_{f}}},{\forall{f \in F}}} & (32) \\
{{\delta^{(K)} \in \left\{ {0,1} \right\}},{\forall{K \in \kappa}}} & (33)
\end{matrix}\)

To solve such large-scale optimization problem, embodiment of the invention may perform computerized column generation in the electronic flow delay checker 163. The key idea of column generation is to split the original problem into two problems: a master problem and a subproblem. The master problem is the original problem but with only a subset of the variables being considered. The subproblem is created to find a new variable that could potentially improve the objective function of the master problem. Usually, the dual of the original problem is used in the subproblem with the purpose of identifying new variables. The kernel of the column generation method defines such an iterative process: 1) solving the master problem with a subset of the variables and obtaining the values of the duals, 2) considering the subproblem with the dual values and finding the potential new variable, and 3) repeating step 1) with the new variables that have been added to the subset. The whole process is repeated until no new variables can be found.

For the delay and backlog verification problem, intuitively, if the computerized system ignores the constraints on delay and backlog, the optimization problem would be reduced to a maximum concurrent flow problem as formulated in (15)-(18). And the dual problem is specified in (19)-(23). With the column generation method, the master problem is the maximum concurrent flow problem (specified in (15)-(18)) but with a subset of the paths κ′⊆κ. The corresponding subproblem can use (20) to identify the new potential paths: the potential paths are the ones that violates (20).

However, because of delay and backlogs constraints (9) and (10), the new potential path variables need to additionally obey tsf(K)≤Dmax−Σe∈K te and bf(K)≤Bmax. Otherwise, constraints (9) and (10) will certainly be violated if they are chosen for routing flows (δ(K)=1).

FIG. 06 illustrates a pseudo algorithm that will assist the potential path variables satisfy the delay and backlog constraints (9) and (10) while satisfying other appropriate conditions, according to an embodiment of the invention.

As shown in step 603, the algorithm run in the electronic flow delay checker 163 relaxes the delay and backlog verification problem (which is MILP) to linear programming problem (LP) by relaxing the binary variable δ(K) to [0, 1].

As shown in step 605, the electronic flow delay checker 163 initiates with a subset of paths κ′. For example, the electronic flow delay checker 163 can initiate the subset by using the link propagation delay te as edges weights and provide the corresponding shortest paths as κ′.

As shown in steps 607-621, the electronic flow delay checker 163 then begins a repetitive process for adding new paths:


- - 1) solve the relaxed master problem and obtain values of the duals
    of the constraints imposed on edges and flows (step **607**);
  - 2) check whether dual constraint (20) hold for all the paths (step
    **609**), if yes, add them into a set P (step **611**);
  - 3) remove the paths from P that would certainly violate delay and
    backlog constraints (step **613**);
  - 4) check (step **615**) if there are remaining paths in P. If yes
    (step **617**), add them to the subset κ′, and repeat the process
    again from 1) (step **605**).

Note that if the answer of step 609 and step 615 is no, it means no new paths can be found. In this case, we restrict the δ(K) variable back to binary values {0, 1} (step 619), and solve the delay and backlog verification problem with the subset of the paths κ′ found by the iterative process (step 621).

Note also that at step 609, when checking whether existing paths violate (20), the electronic flow delay checker 163 does not need to iterate over all the possible paths. The electronic flow delay checker can simply use le as edge weights and use Dijkstra's Shortest Path First algorithm to get all the shortest paths with le. If all the shortest paths satisfy (20) (that the distance of each path is larger than zf), then any path K∈κ must have Σe∈K le≥zf (20). Otherwise, the electronic flow delay checker 163 just adds the shortest paths that violate (20) to P, as the step 2) suggests.

Naturally, embodiments of the invention may employ MILP solvers, such as CPLEX, in the electronic flow delay checker 163 to directly solve the delay and backlog verification problem (24)-(33) (Step 621). The inventors refer to such an approach a CPLEX-direct method. However, using a CPLEX-direct method is very time consuming, since it needs to consider all the possible flow paths, the number of which increases exponentially with the size of the considered network topology. In comparison, the CGH algorithm described here uses much fewer paths. Usually, even for large network topologies, the iteration process terminates within a few hundred rounds. Therefore, the number of paths being considered in κ′ can be thousands of times less when compared to the number of paths used by the CPLEX-direct method, resulting in much shorter running time. Note that this computerized method is a heuristic algorithm, which means that there is no guarantee that the computerized method can find the optimal or approximate the optimal result. In one implementation of the algorithm, a running time reduction at the levels of 500× (or more) over the CPLEX-direct method can be achieved, while yielding nearly as optimal results as the CPLEX-direct method.

Further modifications of the invention within the scope of the appended claims are feasible. As such, the present invention should not be considered as limited by the embodiments and figures described herein. Rather, the full scope of the invention should be determined by the appended claims, with reference to the description and drawings.

Various embodiments of the invention have been described in detail with reference to the accompanying drawings. References made to particular examples and implementations are for illustrative purposes and are not intended to limit the scope of the invention or the claims.

It should be apparent to those skilled in the art that many more modifications of the computerized method and system described here besides those already described are possible without departing from the inventive concepts herein. The inventive subject matter, therefore, is not to be restricted except by the scope of the appended claims. Moreover, in interpreting both the specification and the claims, all terms should be interpreted in the broadest possible manner consistent with the context.

Headings and sub-headings provided herein have been provided as an assistance to the reader and are not meant to limit the scope of the invention disclosed herein. Headings and sub-headings are not intended to be the sole or exclusive location for the discussion of a particular topic.

While specific embodiments of the invention have been illustrated and described, it will be clear that the invention is not limited to these embodiments only. Embodiments of the invention discussed herein may have generally implied the use of materials from certain named equipment manufacturers; however, the invention may be adapted for use with equipment from other sources and manufacturers. Equipment used in conjunction with the invention may be configured to operate according to conventional methods and protocols and/or may be configured to operate according to specialized protocols. Numerous modifications, changes, variations, substitutions and equivalents will be apparent to those skilled in the art without departing from the spirit and scope of the invention as described in the claims. In general, in the following claims, the terms used should not be construed to limit the invention to the specific embodiments disclosed in the specification but should be construed to include all systems and methods that operate under the claims set forth herein below. Thus, it is intended that the invention covers the modifications and variations of this invention provided they come within the scope of the appended claims and their equivalents.

All publications herein are incorporated by reference to the same extent as if each individual publication or patent application were specifically and individually indicated to be incorporated by reference. Where a definition or use of a term in an incorporated reference is inconsistent or contrary to the definition of that term provided herein, the definition of that term provided herein applies and the definition of that term in the reference does not apply.

