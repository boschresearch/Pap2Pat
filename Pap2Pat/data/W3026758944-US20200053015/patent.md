# DESCRIPTION

## TECHNICAL FIELD

The present disclosure relates to a method of data caching in delay tolerant network based on information centric network and a recording medium and a device for performing the same, and more particularly, to a data caching method that can be applied to the delay tolerant network environment having limited buffer capacity and a recording medium and a device for performing the same.

## BACKGROUND

Delay Tolerant Networking (DTN) is an approach designed to deliver a message between neighboring nodes in a store-carry-forward way in an environment where connectivity between a source node and a destination node is not guaranteed. In DTN, each node stores a message to transmit, and can forward the message to other nodes according to a preset condition when it encounters another node.

DTN attracts a lot of attention because it can overcome disconnection through opportunistic transmission between encountered neighboring nodes in an extreme environment where the communication infrastructure is destroyed by a disaster, such as earthquakes, floods and fires, and there is no stable routing path to connect many nodes due to low node density.

Meanwhile, the Information Centric Networking (ICN) is a communication approach based on a data name rather than an IP address. Currently, there are rapid increases in Internet usage in terms of the number of users and data capacity. According to the current IP address-based data transmission method, transmission is carried out using a receiver's IP address related to the physical location, and accordingly the same data is repeatedly transmitted through the network. Therefore, the current data transmission method is inefficient.

ICN is technology proposed to overcome a traffic bottleneck phenomenon which is a disadvantage of the conventional IP address-based communication method, and the ICN enables routers or nodes to store and distribute specified data to neighboring routers or nodes that request the corresponding data. In ICN, a message may be classified either into Interest and Data. A consumer or data requester that needs Data can disseminate Interest through the network. When receiving the Interest, a router, node or data provider that has the requested Data may deliver the Data to the consumer or data requester back through the same path from which the Interest delivered.

ICN is designed based on a network environment where connectivity is guaranteed, and enforces a caching policy based on various network information collected in the network environment.

However, because DTN where connectivity between nodes is not guaranteed has limited buffer capacity, when ICN is applied to DTN, it is impossible to apply the conventional caching policy as it is.

Additionally, multiple nodes may request the same data in ICN, and in view of this, there is a need for a new caching policy.

## SUMMARY

An aspect of the present disclosure provides a data caching method for controlling data caching or deletion according to a data caching or deletion policy using data information or node information defined in an information centric network in consideration of node buffer capacity, and a recording medium and a device for performing the same.

To achieve the above-described object, a data caching method of the present disclosure includes the step of checking a remaining buffer amount and a buffer usage amount of node, the step of caching data in the node which is received from another node according to a data caching policy, in case the remaining buffer amount of the node is greater than a preset remaining buffer amount threshold, the step of deleting data cached in the node from the node according to a data deletion policy, in case the buffer usage amount of the node is less than a preset buffer usage amount threshold and setting an initial Time-to-Live (TTL) value of the data received from another node or updating a TTL of the data cached in the node using information of the data received from another node or information of the node.

Meanwhile, the step of setting may include setting the initial TTL value of the data received from another node using one of data information including a number of requester nodes and priority of the data received from other node, or node information including delivery predictability of the data received from another node to requester node.

Additionally, the step of setting may include calculating a variation of one of data information including a number of requester nodes and a remaining delivery frequency of the data cached in the node or delivery predictability of the data cached in the node to requester node for a unit time, calculating a TTL increase and decrease value of the data cached in the node using the variation per the unit time, and updating the TTL of the data cached in the node by adding the TTL increase and/decrease value to a current TTL of the data cached in the node.

Additionally, the step of setting may include checking the TTL of the data cached in the node, and when the TTL of the data cached in the node is equal to or less than zero (0), deleting the data cached in the node from the node.

Additionally, the step of caching may include comparing data information including a number of requester nodes of the data received from other node or node information including delivery predictability of the data received from other node to requester node with a preset data caching threshold, and setting a remaining delivery frequency of the data received from other node according to a result of comparison between the data information or the node information and the data caching threshold, and caching in the node.

Additionally, the step of setting the remaining delivery frequency of the data received from other node may include when the data information or the node information is less than the data caching threshold, setting the remaining delivery frequency of the data received from other node to one (1), and caching in the node, and when the data information or the node information is equal to or greater than the data caching threshold, calculating the remaining delivery frequency of the data received from other node using the data information or the node information.

Additionally, the step of the setting the remaining delivery frequency of the data received from other node may include checking the remaining delivery frequency of the data cached in the node, and when the remaining delivery frequency of the data cached in the node is zero (0), deleting the data cached in the node.

Additionally, the step of deleting may include arranging at least one data cached in the node based on one of data information including a number of requester nodes, the TTL, a delivery frequency and a priority of the data cached in the node, and deleting the data cached in the node according to an order of arrangement of the at least one data cached in the node.

Additionally, the step of the deleting may include calculating a data information arrangement value representing a relationship between data information including a number of requester nodes, the TTL, a delivery frequency, and a priority of the data, cached in the node, arranging at least one data cached in the node based on the data information arrangement value, and deleting the data cached in the node according to an order of arrangement of the at least one data cached in the node.

Additionally, the step of the deleting may include arranging at least one data cached in the node based on delivery predictability of the data cached in the node to requester node, or calculating a node information arrangement value representing a relationship between delivery predictability of the data cached in the node to requester node and priority of the data cached in the node, and arranging at least one data cached in the node based on the node information arrangement value, and deleting the data cached in the node according to an order of arrangement of the at least one data cached in the node.

In addition, there is provided a computer-readable non-transitory recording medium having recorded thereon a computer program for performing the data caching method may include checking a remaining buffer amount and a buffer usage amount of node; when the remaining buffer amount of the node is greater than a preset remaining buffer amount threshold, caching data received from other node in the node according to a data caching policy;

when the buffer usage amount of the node is less dean a preset buffer usage amount threshold, deleting data cached in the node from the node according to a data deletion policy; and

setting an initial Time-to-Live (TTL) value of the data received from other node or updating a TTL of the data cached in the node using information of the data received from other node or information of the node

A data caching device of the present disclosure includes a processor and a memory; buffer check unit which checks a remaining buffer amount and a buffer usage amount of node, a caching policy unit which when the remaining buffer amount of the node is greater than a preset remaining buffer amount threshold, controls to cache data received from other node in the node according to a data caching policy, and when the buffer usage amount of the node is less than a preset buffer usage amount threshold, controls to delete data cached in the node from the node according to a data deletion policy, and a TTL setting unit which sets an initial TTL value of the data received from other node or updates a TTL of the data cached in the node using information of the data received from other node or information of the node.

According to the present disclosure, it is possible to allow for an efficient node buffer capacity management in a delay tolerant network having limited node buffer capacity, and provide a caching service in consideration of the presence of multiple requester nodes for the same data in a delay tolerant network environment.

## DETAILED DESCRIPTION OF EMBODIMENTS

The following detailed description of the present disclosure is made with reference to the accompanying drawings, in which particular embodiments for practicing the present disclosure are shown for illustration purposes. These embodiments are described in sufficient detail for those skilled in the art to practice the present disclosure. It should be understood that various embodiments of the present disclosure are different but do not need to be mutually exclusive. For example, particular shapes, structures and features described herein in connection with one embodiment can be embodied in other embodiment without departing from the spirit and scope of the present disclosure. It should be further understood that changes can be made for locations or arrangements of individual elements in each disclosed embodiment without departing from the spirit and scope of the present disclosure. Accordingly, the following detailed description is not intended to be taken in limiting senses, and the scope of the present disclosure, if appropriately described, is only defined by the appended claims along with the full scope of equivalents to which such claims are entitled. In the drawings, similar reference signs denote same or similar functions in many aspects

Hereinafter, the embodiments of the present disclosure will be described in more detail with reference to the accompanying drawings.

The term “Unit” is defined herein as having its broadest definition to an ordinary skill in the art to refer to a software including instructions executable in a non-transitory computer readable medium that would perform the associated function when executed, a circuit designed to perform the associated function, a hardware designed to perform the associated function, or a combination of a software, a circuit, or a hardware designed to perform the associated function.

FIG. 1 is a block diagram of a device of data caching in a delay tolerant network based on the information centric network according to the embodiment of the present disclosure.

The data caching device 1000 according to the embodiment of the present disclosure may be equipped in each node in a network environment to control caching of data received from another node or deletion of data cached in nodes.

In the present disclosure, the network environment may be a Delay Tolerant Networking (DTN) environment based on Information Centric Networking (ICN).

ICN is a networking approach based on data information such as the name of content or data rather than an IP address. In ICN, a message may be classified into Interest and Data. A data requester that needs Data can disseminate Interest through the network, and when receiving the Interest, a data provider that has the corresponding Data can deliver the Data to the data requester along the same path in reverse.

DTN is an approach designed to deliver a message between neighboring nodes in a store-carry-forward way in an environment where connectivity between a source node and a destination node is not guaranteed. In DTN, each node stores a message to transmit, and can forward the message to another node according to a preset condition when it encounters another node.

The data caching device 1000 according to the embodiment of the present disclosure may control data caching or deletion according to a data caching or deletion policy using data information or node information defined in ICN in consideration of node buffer capacity.

Referring to FIG. 1, the data caching device 1000 according to the embodiment of the present disclosure may include a buffer check unit 10, a caching policy unit 20, a Time-To-Live (TTL) setting unit 30, a data caching unit 40 and a data deletion unit 50.

The buffer check unit 10 may check a remaining buffer amount bremN and a buffer usage amount buseN of node.

The buffer check unit 10 may compare the remaining buffer amount bremN of node with a preset remaining buffer amount threshold bremthr. When data is received from another node, the buffer check unit 10 may check the remaining buffer amount bremN of node, and compare the remaining buffer amount bremN of node with the remaining buffer amount threshold bremthr. When the remaining buffer amount bremN of node is greater than the remaining buffer amount threshold bremthr, the buffer check unit 10 may control to cache the data received from another node in the node.

The buffer check unit 10 may compare the buffer usage amount buseN of the node with a preset buffer usage amount threshold busethr. When the buffer usage amount buseN of node is less than the buffer usage amount threshold busethr, the buffer check unit 10 may control to delete the data cached in the node.

As described above, the buffer check unit 10 may check the remaining buffer amount bremN and the buffer usage amount buseN of the node to support data caching or deletion control in the caching policy unit 20 as described below, thereby allowing for efficient management of node buffer capacity.

The caching policy unit 20 may control to cache the data received from another node according to the data caching policy. Additionally, the caching policy unit 20 may control to delete the data cached in the node according to the data deletion policy.

Specifically, the caching policy unit 20 may control to cache the data in the node received from another node according to the data caching policy using data information or node information. When data is received from another node and the buffer check unit 10 identifies that the remaining buffer amount bremN of the node is greater than the remaining buffer amount threshold bremthr, the caching policy unit 20 may control to cache the data received from other node according to the data caching policy.

In the following description, the data information may include the number of requester nodes Ndi, TTL Tdi, delivery frequency fdi, the remaining delivery frequency Fdi and priority Ydi of data.

Additionally, the node information may include delivery predictability Pdi of data from the node to requester node. The delivery predictability Pdi may be set as a maximum value Pdimax or a minimum value Pdimin of delivery predictability of data from the node to at least one requester node. Alternatively, the delivery predictability Pdi may be set as a difference Pdimax−Pdimin, a sum Pdisum or an average Pdiavg of the maximum value Pdimax and the minimum value Pdimin of delivery predictability of data from the node to at least one requester node.

According to the data caching policy, the caching policy unit 20 may compare a value Idi obtained from the data information or node information with a preset data caching threshold IC.

For example, the caching policy unit 20 may compare the number of requester nodes Ndi of data received from other node with a preset requester node number threshold NC. Alternatively, the caching policy unit 20 may compare the delivery predictability Pdi of data received from other node to requester node with a preset delivery predictability threshold PC.

Additionally, the caching policy unit 20 may set the remaining delivery frequency Fdi of data received from other node according to the results of comparison between the value Idi obtained from data information or node information and the data caching threshold IC, and control to cache in the node.

When the value Idi obtained from data information or node information is less than the data caching threshold IC, the caching policy unit 20 may set the remaining delivery frequency Fdi of data received from other node to one (1) and control to cache in the node. In this case, the data received from another node may be only cached in the node until it is delivered to another node.

For example, when the number of requester nodes Ndi of data received from another node is less than the preset requester node number threshold NC, or the delivery predictability Pdi of data received from another node to requester node is less than the preset delivery predictability threshold PC, the caching policy unit 20 may set the remaining delivery frequency Fdi of data received from another node to one (1).

When the value Idi obtained from data information or node information is equal to or greater than the data caching threshold IC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi of data received from another node using the data information or node information as shown in the following Equation 1, and control to cache in the node:

Fd=cF×Id  [Equation 1]

In Equation 1, Fdi denotes the remaining delivery frequency of data, cF denotes the delivery frequency coefficient, and Idi denotes the value obtained from data information or node information.

For example, when the number of requester nodes Ndi of data received from other node is equal to or greater than the preset requester node number threshold NC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFN of the number of requester nodes and the number of requester nodes Ndi of the data as shown in Equation 1.

Alternatively, when the number of requester nodes Ndi of data received from another node is equal to or greater than the preset requester node number threshold NC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFY of priority and the priority Ydi of the data as shown in Equation 1. The priority Ydi of data may be expressed as a natural number of [1, Y] according to the grade.

Alternatively, when the delivery predictability Pdi of data received from another node to requester node is equal to or greater than the preset delivery predictability threshold PC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFP of delivery predictability and the delivery predictability Pdi as shown in Equation 1.

Additionally, the caching policy unit 20 may check the remaining delivery frequency Fdi of data cached in the node, and when the remaining delivery frequency Fdi of data cached in the node is zero (0), may control to delete the corresponding data from the node.

The caching policy unit 20 may control to delete the data cached in the node according to the data deletion policy using data information or node information. When the buffer check unit 10 identifies that the buffer usage amount buseN of the node is less than the buffer usage amount threshold busethr, the caching policy unit 20 may control to delete the data cached in the node from the node according to the data deletion policy.

According to the data deletion policy, the caching policy unit 20 may arrange at least one data cached in the node based on data information or node information of each of the at least one data cached in the node.

For example, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the number of requester nodes of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the TTL of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in descending order of the delivery frequency of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the priority of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the delivery predictability to requester node.

Alternatively, the caching policy unit 20 may calculate a data information arrangement value Idipl using data information or node information of each of at least one data cached in the node and arrange the at least one data cached in the node based on the data information arrangement value Idipl. Here, the data information arrangement value Idipl may be a value denoting the relationship between multiple data information. Alternatively, the data information arrangement value Idipl may be a value denoting the relationship between the node information and the priority of data.

For example, the caching policy unit 20 may calculate a delivery frequency ratio Wdif or the data information arrangement value Idipl that is calculated as a ratio of the number of requester nodes Ndi and the delivery frequency fdi of data as shown in the following Equation 2, and arrange at least one data cached in the node in descending order of the delivery frequency ratio Wdif:

\(\begin{matrix}
{W_{d_{i}}^{f} = \frac{f_{d_{i}}}{N_{d_{i}}}} & \left\lbrack {{Equation}\mspace{14mu} 2} \right\rbrack
\end{matrix}\)

In Equation 2, Wdif denotes the delivery frequency ratio, fdi denotes the delivery frequency of data, and Ndi denotes the number of requester nodes of data.

Alternatively, the caching policy unit 20 may calculate a priority multiple WdiY or the data information arrangement value Idipl that is calculated by multiplication of the number of requester nodes Ndi and the priority Ydi of data as shown in the following Equation 3, and arrange at least one data cached in the node in ascending order of the priority multiple WdiY:

WdY=Nd=Ydi  [Equation 3]

In Equation 3, WdiY denotes the priority multiple, Ndi denotes the number of requester nodes of data, and Ydi denotes the priority of data.

Alternatively, the caching policy unit 20 may calculate a delivery predictability multiple Pdipl or the data information arrangement value Idipl that is calculated by multiplication of the delivery predictability Pdi to data requester node and the priority Ydi as shown in the following Equation 4, and arrange at least one data cached in the node in ascending order of the delivery predictability multiple Pdipl:

Pdp;=Pd=Yd  [Equation 4]

In Equation 4, Pdipl denotes the delivery predictability multiple, Pdi denotes the delivery predictability of data to requester node, and Ydi denotes the priority of data.

As described above, the caching policy unit 20 may arrange at least one data cached in the node, and delete the data cached in the node in the order of arrangement.

The TTL setting unit 30 may set an initial TTL value of data received from other node and control to cache in the node. Additionally, the TTL setting unit 30 may update the TTL of data cached in the node.

Specifically, the TTL setting unit 30 may set the initial TTL value of data received from another node using data information or node information. When the caching policy of data received from another node is determined by the caching policy unit 20, the TTL setting unit 30 may set the initial TTL value of the corresponding data.

The TTL setting unit 30 may set the initial TTL value Tdiinit of data received from another node as the sum of the value Idi obtained from data information or node information multiplied by the TTL coefficient cT and the TTL constant CT as shown in the following Equation 5 and control to cache in the node. Here, the TTL coefficient cT may be set as a difference Tdimax−Tdimin of the maximum TTL value Tdimax and the minimum TTL value Tdimin, and the TTL constant CT may be set as the minimum TTL value Tdimin.

Tdinit=cT×Id +CT   [Equation 5]

In Equation 5, Tdiinit denotes the initial TTL value, cT denotes the TTL coefficient, Idi denotes the value obtained from data information or node information, and CT denotes the TTL constant.

For example, the TTL setting unit 30 may set the initial TTL value Tdiinit of data received from another node by applying the number of requester nodes Ndi of data received from another node to the value Idi obtained from data information or node information Equation 5.

Alternatively, the TTL setting unit 30 may set the initial TTL value Tdi init of data received from another node by applying the priority Ydi of data received from another node to the value Idi obtained from data information or node information in Equation 5.

Alternatively, the TTL setting unit 30 may set the initial TTL, value Tdiinit of data received from another node by applying the delivery predictability Pdi of data received from another node to requester node to the value Idi obtained from data information or node information in Equation 5.

When a unit time τ has elapsed, the TTL setting unit 30 may update the TTL of data cached in the node using data information or node information.

The TTL setting unit 30 may calculate a variation Idiτ of the value obtained from data information or node information for the unit time τ. The TTL setting unit 30 may calculate a TTL increase and decrease the value ΔTdi of data cached in the node by multiplication of the variation Idiτ of the value obtained from data information or node information for the unit time τ and the TTL increase/decrease coefficient cΔT as shown in the following Equation 6:

ΔTd=cΔT×Idτ  [Equation 6]

In Equation 6, ΔTdi denotes the TTL increase and decrease value, cΔT denotes the TTL increase and decrease coefficient, and Idiτ denotes the variation of the value obtained from data information or node information per the unit time τ.

For example, the TTL setting unit 30 may calculate a requester node number variation Ndi96  of data cached in the node per the unit time τ, and calculate a TTL increase and decrease value ΔTdi of data cached in the node by applying the requester node number variation Ndiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in Equation 6.

Alternatively, the TTL setting unit 30 may calculate a remaining delivery frequency variation Fdiτ of data cached in the node per the unit time τ, and calculate a TTL increase and decrease value ΔTdiof data cached in the node by applying the remaining delivery frequency variation Fdiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in Equation 6.

Alternatively, the TTL setting unit 30 may calculate a delivery predictability variation Pdiτ of data cached in the node to requester node for the unit time τ, and calculate a TTL increase and decrease the value ΔTdi of data cached in the node by applying the delivery predictability variation Pdiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in Equation 6.

The TTL setting unit 30 may update the TTL of data cached in the node by adding the TTL increase and decrease value ΔTdi to the current TTL Tdiold of data cached in the node as shown in the following Equation 7:

Tdnew=Tdold+ΔTd  [Equation 7]

In Equation 7, Tdinew denotes the updated TTL of data cached in the node, Tdiold denotes the current TTL of data cached in the node, and ΔTdi denotes the TTL increase and decrease value.

Meanwhile, the TTL setting unit 30 may check the TTL Tdi of data cached in the node, and when the TTL Tdi of data cached in the node is equal to or less than zero (0), may control to delete the data cached in the node from the node.

The data caching unit 40 caches data, for which the caching policy is determined the by caching policy unit 20 in the buffer of the node.

The data deletion unit 50 may delete data, for which the deletion policy is determined by the caching policy unit 20 from the buffer of the node.

As described above, the data caching device 1000 according to the embodiment of the present disclosure may control the data caching or deletion according to the data caching or deletion policy using data information or node information defined in ICN in consideration of node buffer capacity. Accordingly, it is possible to allow for efficient node buffer capacity management in DTN having limited node buffer capacity, and caching policy in consideration of the presence of multiple requester nodes for the same data in DTN environment.

Hereinafter, a method of data caching in delay tolerant network based on information centric network according to the embodiment of the present disclosure will be described.

The data caching method according to the embodiment of the present disclosure may be applied to each node in a network environment to control caching of data received from another node or deletion of data cached in node.

The data caching method according to the embodiment of the present disclosure may be performed in substantially the same configuration as the data caching device 1000 of FIG. 1. Accordingly, the same drawing signs are given to the same elements as the data caching device 1000 of FIG. 1, and repeated descriptions are omitted herein.

FIG. 2 is a flowchart of a congestion control method according to the embodiment of the present disclosure.

Referring to FIG. 2, the buffer check unit 10 may check a remaining buffer amount and a buffer usage amount of node (S100).

The buffer check unit 10 may compare the remaining buffer amount and the buffer usage amount with a preset remaining buffer amount threshold and a preset buffer usage amount threshold respectively (S200).

According to the results of comparison between the remaining buffer amount and the buffer usage amount and each threshold, the caching policy unit 20 may determine the caching policy of data received from another node or the deletion policy of data cached in node (S300). Its detailed description will be provided below with reference to FIGS. 3 and 4.

The TTL setting unit 30 may set the TTL of data received from another node or data cached in node (S400). Its detailed description will be provided below with reference to FIG. 5.

The data caching unit 40 may cache data received from another node in node according to the data caching policy, and the data deletion unit 50 may delete data cached in node according to the data deletion policy (S500).

FIG. 3 is a detailed flowchart when determining a data caching policy in the step of determining a data caching policy or a data deletion policy shown in FIG. 2.

Referring to FIG. 3, when data is received from another node (S210), and the remaining buffer amount bremN of the node is greater than the remaining buffer amount threshold bremthr (S230), the caching policy unit 20 may compare the value Idi obtained from data information or node information with the preset data caching threshold IC (S310).

For example, the caching policy unit 20 may compare the number of requester nodes Ndi of data received from another node with the preset requester node number threshold NC. Alternatively, the caching policy unit 20 may compare the delivery predictability Pdi of data received from another node to requester node with the preset delivery predictability threshold PC.

When the value Idi obtained from data information or node information is less than preset. data caching threshold IC (S310), the caching policy unit 20 may set the remaining delivery frequency Fdi of data, received from another node to one (1) (S311), and control to cache in the node (S510).

For example, when the number of requester nodes Ndi of data received from another node is less than the preset requester node number threshold NC, or the delivery predictability Pdi of data received from another node to requester node is less than the preset delivery predictability threshold PC, the caching policy unit 20 may set the remaining delivery frequency Fdi of data received from another node to one (1).

When the value Idi obtained from data information or node information is equal to or greater than the preset data caching threshold IC (S310), the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the value Idi obtained from data information or node information and the delivery frequency coefficient cF as shown in the above Equation 1 (S312), and control to cache in the node (S510).

For example, when the number of requester nodes Ndi of data received from another node is equal to or greater than the preset requester node number threshold NC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFN of the number of requester nodes and the number of requester nodes Ndi of the data as shown in Equation 1.

Alternatively, when the number of requester nodes Ndi of data received from another node is equal to or greater than the preset requester node number threshold NC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFY of priority and the priority Ydi of data as shown in Equation 1. The priority Ydi of data may be represented as a natural number of [1, Y] according to the grade.

Alternatively, when the delivery predictability Pdi of data received from another node to requester node is equal to or more than the preset delivery predictability threshold PC, the caching policy unit 20 may calculate the remaining delivery frequency Fdi by multiplication of the delivery frequency coefficient cFP of delivery predictability and the delivery predictability Pdi as shown in Equation 1.

Meanwhile, when data is not received from another node (S210) and the buffer usage amount buseN of node is less than the buffer usage amount threshold busethr (S250), the caching policy unit 20 may check the remaining delivery frequency Fdi of data cached in the node (S350).

When the remaining delivery frequency Fdi of data cached in the node is zero (0) (S315), the caching policy unit 20 may control to delete the corresponding data from the buffer of the node (S520).

FIG. 4 is a detailed flowchart when determining a data deletion policy in the step of determining a data caching policy or a data deletion policy shown in FIG. 2.

Referring to FIG. 4, when the buffer usage amount buseN of node is less than the buffer usage amount threshold busethr (S250), the caching policy unit 20 may arrange at least one data cached in the node (S320).

For example, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the number of requester nodes of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the TTL of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in descending order of the delivery frequency of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the priority of data.

Alternatively, the caching policy unit 20 may arrange at least one data cached in the node in ascending order of the delivery predictability to requester node.

Alternatively, the caching policy unit 20 may calculate the data information arrangement value Idipl using data information or node information of each of at least one data cached in the node, and arrange at least one data cached in the node based on the data information arrangement value Idipl. Here, the data information arrangement value Idipl may be a value denoting the relationship between multiple data information. Alternatively, the data information arrangement value Idipl may be a value denoting the relationship between the node information and the priority of data.

For example, the caching policy unit 20 may calculate the delivery frequency ratio Wdif or the data information arrangement value Idipl that is calculated as a ratio of the number of requester nodes Ndi and the delivery frequency fdi of data as shown in Equation 2, and arrange at least one data cached in the node in descending order of the delivery frequency ratio Wdif.

Alternatively, the caching policy unit 20 may calculate the priority multiple WdiY or the data information arrangement value Idipl that is calculated by multiplication of the number of requester nodes Ndi and the priority Ydi of data as shown in the above Equation 3, and arrange at least one data cached in the node in ascending order of the priority multiple WdiY.

Alternatively, the caching policy unit 20 may calculate the delivery predictability multiple Pdipl or the data information arrangement value Idipl that is calculated by multiplication of the delivery predictability Pdi to data requester node and the priority Ydi as shown in the above Equation 4, and arrange at least one data cached in the node in ascending order of the delivery predictability multiple Pdipl.

The caching policy unit 20 may select data to delete from at least e data cached in the node according to the order of arrangement of the at least one data cached in the node (S321).

The caching policy unit 20 may control to delete the selected data from the buffer of the node (S520).

FIG. 5 is a detailed flowchart of the step of setting the TTL of data shown in FIG. 2.

Referring to FIG. 5, when data is received from another node (S210), the TTL setting unit 30 may set the initial TTL, value Tdiinit of the data received from another node as the sum of the value Idi obtained from data information or node information of the data received from another node multiplied by the TTL coefficient cT and the TTL constant CT as shown in the above Equation 5 (S410), and control to cache in the node (S510).

For example, the TTL setting unit 30 may set the initial TTL value Tdiinit of the data received from another node by applying the number of requester nodes Ndi of the data received from other node to the value Idi obtained from data information or node information in Equation 5.

Alternatively, the TTL setting unit 30 may set the initial TTL value Tdiinit of the data received from another node by applying the priority Ydiof the data received from another node to the value Idi obtained from data information or node information in Equation 5.

Alternatively, the TTL setting unit 30 may set the initial TTL value Tdiinit of the data received from another node by applying the delivery predictability Pdi of data received from another node to requester node to the value Idi obtained from data information or node information in Equation 5.

Meanwhile, when data is not received from another node (S210), the TTL setting unit 30 may check if the unit time τ has elapsed (S420).

When the unit time τ has elapsed (S420), the TTL setting unit 30 may update the TTL Tdinew of data cached in the node by adding a value obtained by multiplying the variation Idiτ the value obtained from data information or node information per the unit time τ by the TTL increase and decrease coefficient cΔT to the current TTL Tdiold of the data cached in the node as shown in the following Equation 8 (S421), and control to cache in the node (S510).

Tdnew=Tdold+cΔT×Idτ  [Equation 8]

In Equation 8, Tdinew denotes the updated TTL of data cached in the node, Tdiold denotes the current TTL of data cached in the node, cΔT denotes the TTL increase and decrease coefficient, and Idiτ denotes the variation of the value obtained from data information or node information per the unit time τ.

For example, the TTL setting unit 30 may calculate the requester node number variation Ndiτ of data cached in the node per the unit time τ, and calculate the TTL increase and decrease value ΔTdi of data cached in the node by applying the requester node number variation Ndiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in the above Equation 6.

Alternatively, the TTL setting unit 30 may calculate the remaining delivery frequency variation Fdiτ of data cached in the node per the unit time τ, and calculate the TTL increase and decrease the value ΔTdi of data cached in the node by applying the remaining delivery frequency variation Fdiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in the above Equation 6.

Alternatively, the TTL setting unit 30 may calculate the delivery predictability variation Pdiτ of data cached in the node to requester node per the unit time τ, and calculate the TTL increase and decrease the value ΔTdi of the data cached in the node by applying the delivery predictability variation Pdiτ to the variation Idiτ of the value obtained from data information or node information per the unit time τ in the above Equation 6.

Additionally, the TTL setting unit 30 may update the TTL of data cached in the node by adding the TTL increase and decrease the value ΔTdi to the current TTL Tdiold of data cached in the node.

Meanwhile, when the unit time τ has not elapsed (S420), the TTL setting unit 30 may check the TTL Tdi of data cached in the node (S423).

When the TTL Tdi of data cached in the node is equal to or less than zero (0) (S423), the TTL setting unit 30 may control to delete the data cached in the node from the node (S520).

Accordingly, the data caching method according to the embodiment of the present disclosure can control data caching or deletion according to a data caching or deletion policy using data information or node information defined in an ICN in consideration of node buffer capacity. Accordingly, it is possible to allow for efficient node buffer capacity management in a DTN having limited node buffer capacity, and provide a caching service in consideration of the presence of multiple requester nodes for the same data in a DTN environment.

The above-described method of data caching in DTN based on ICN may be implemented as an application or in the form of program commands that are executed through various computer components, and recorded in computer-readable recording media. The computer-readable recording media may include program commands, data files and data structures, alone or in combination.

The program commands in recorded in the computer-readable recording media may be specially designed and configured for the present disclosure and may be known and available to those having ordinary skill in the field of computer software.

Examples of the computer-readable recording media include hardware devices specially designed to store and execute program commands, such as magnetic media such as hard disk, floppy disk and magnetic tape, optical recording media such as CD-ROM and DVD, magneto-optical media such as floptical disk, and ROM, RAM and flash memory.

Examples of the program commands include machine codes generated by a compiler as well as high-level language codes that can he executed by a computer using an interpreter. The hardware device may be configured to act as one or more software modules to perform processing according to the present disclosure, or vice versa.

While the present disclosure has been hereinabove described with reference to the embodiments, it will be apparent to those skilled in the corresponding technical field that a variety of modifications and changes may be made thereto without departing from the spirit and scope of the present disclosure set forth in the appended claims.

### DETAILED DESCRIPTION OF MAIN ELEMENTS

- **1000**: Data caching device
- **10**: Buffer check unit
- **20**: Caching policy unit
- **30**: TTL setting unit
- **40**: Data caching unit
- **50**: Data deletion unit

