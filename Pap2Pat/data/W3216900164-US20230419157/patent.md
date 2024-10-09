# DESCRIPTION

## FIELD OF THE INVENTION

The present invention relates generally to quantum computation. More specifically, it relates to fault-tolerant cluster state quantum computation devices and techniques.

## BACKGROUND OF THE INVENTION

In recent years, significant experimental progress has been made towards building a large-scale quantum computer. In platforms such as superconducting qubits and trapped ions, the error rates for small systems have been successfully suppressed below the threshold error rate of the surface code [1, 2, 3]. Using newly developed techniques for neutral atoms trapped in optical tweezer arrays, the coherence time, gate fidelity, and read-out fidelity for large assemblies of qubits are being rapidly improved [4, 5, 6, 7]. These advances give us hope that we will one day be able to perform fault-tolerant quantum computation by scaling up these systems while maintaining low error rates.

However, the scalability of leading approaches remains an important challenge. Current estimates suggest that the engineering effort needed to build even a single logical qubit with logical error rate low enough for useful quantum computation could be enormous [8]. Quantum algorithms with practical ramifications can involve applying at least ˜10−8 logical gates to ˜100 logical qubits [9, 10]. To ensure that the outcome of the computation is correct with high probability, the logical error rate would then need to be below ˜10−8. Based on the sub-threshold error scaling in Ref. [11], this would require at least ˜400 physical qubits per logical qubit if the physical error rate is half the threshold.

Manufacturing, calibrating and controlling physical qubits in such large numbers will be tremendously difficult. The fabrication process for components of solid-state quantum devices, such as quantum dots or superconducting circuits [1], is inevitably imperfect, leading to variations in the properties of individual qubits and their interactions. Even in systems where qubits are encoded in identical particles, e.g., trapped ions [2, 3, 12] or neutral atoms [4, 5, 6, 7], experimental control parameters such as the strengths of laser excitation pulses or trapping potentials may exhibit inhomogeneity. Thus, in order to control these qubits with high fidelity, an experimental system needs to be accurately calibrated across the entire quantum computer. In superconducting circuits, for instance, inhomogeneity is unavoidable, and stray couplings between ideally independent qubits are an experimental fact of life that must be mitigated through control logic (see e.g., [1].) The difficulty of doing so increases significantly with the number of qubits [13].

## BRIEF SUMMARY OF THE INVENTION

To circumvent these challenges, we provide a novel approach to fault-tolerant quantum computation, in which a well-protected logical qubit can be built using only a few physical components. Consequently, the engineering effort required to develop the computer's components is significantly reduced, providing a simpler and more easily scalable route to fault-tolerant quantum computation. At a high level, our approach succeeds by shedding the limitations implicit in two assumptions that usually guide fault-tolerant circuit design: first, that the computer's qubits are all of the same type so are fairly homogeneous, and second, that good fault-tolerant gates should not propagate errors.

Specifically, we provide a fault-tolerant protocol for generating the three-dimensional cluster state of Ref. [14], which can then be used to perform universal fault-tolerant computation via adaptive single-qubit measurements. While there is already a well-known procedure for preparing this state, our method has the advantage of being compatible with a much simpler physical realization than what was originally envisaged in Refs. [14, 15, 16]. We take an approach similar to existing proposals for building large one- and two-dimensional cluster states using a small number of physical components [17, 18, 19, 20, 21]. However, while two-dimensional cluster states are universal for quantum computation, they are not known to support fault-tolerant quantum computation. More precisely, two-dimensional cluster states of unprotected physical qubits are not known to be a particularly useful resource for fault-tolerant quantum computation. Two-dimensional cluster states can be used to perform local gates on a one-dimensional array of qubits [22], for which fault-tolerant quantum computing schemes have been developed [23, 24]. However, the threshold (in the circuit model) is likely prohibitively low (estimated to be 10−5 [24]). The step from universality to fault-tolerance is not obvious and, in fact, quite surprising considering the architecture of the system.

Our protocol is built around a special ancilla qubit, , which interacts sequentially with a stream of data qubits propagating through a delay line. These data qubits are encoded in degrees of freedom sharing a common physical implementation, e.g., different temporal modes of photons or phonons in a waveguide. The only interactions are between  and data qubits (and not between data qubits themselves), and these interactions are fixed and periodic, requiring a modest amount of calibration. We show, moreover, that all of the operations required in our protocol can be implemented using existing technologies in quantum photonic and phononic systems.

To demonstrate fault-tolerance, we analyze the robustness of our protocol against both circuit errors and memory errors. We use a standard depolarizing model to describe circuit errors, which are associated with imperfect gates, measurements, and state initialization. Memory errors refer to errors that occur while qubits are idle, for which we study the effect of dephasing and qubit loss.

In the absence of memory errors, there is a threshold of 0.39% for the circuit error rate, below which the logical error can be arbitrarily suppressed by increasing the number of physical qubits. In the presence of memory errors, the logical error rate cannot be arbitrarily suppressed. However, provided that the circuit error rate is below threshold, the logical error rate decays rapidly with the inverse of the memory error rate. More precisely, suppose that the coherence time of the data qubits is lower-bounded by T. Then for a sufficiently large but finite T, the logical error rate can be made exponentially small in . Here,  is the inverse of the frequency with which gates are applied, which is ultimately limited by the timescale for interactions between  and data qubits. The number of logical gates that can be reliably executed will therefore scale exponentially with .

A large separation between T and  is often observed in certain experimental platforms, such as trapped ions or neutral atoms utilizing atomic clock transitions [12, 4, 5, 6]. Indeed, because of the strict separation in the roles of  and the data qubits, maximizing the ratio T/ while maintaining high gate fidelity is an invitation to design a hybrid system having two types of qubits with different physical substrates. That is the context in which we expect our scheme to be the most promising. Photonic [25] and phononic [26] delay lines are known to be good quantum memories, and can be coupled to controllable qubits capable of playing the role of .

To illustrate the advantages of our scheme, suppose that memory errors are dominated by loss. Then, if the circuit error rate is 10−3 an aspirational but realistic target—our protocol can in principle attain a logical error rate of 10−8 for /T≈1.4×10−5, and 10−5 for /T≈3.2×10−6. These estimates suggest that extremely low logical error rates can be achieved by improving a very small number of experimental components. In particular, if the operations involving  can be calibrated such that circuit error rate is below the threshold value of 0.39%, incremental improvements of a single component—the delay line—can lead to drastic reductions in the logical error rate.

Although our scheme was primarily motivated by the aforementioned experimental considerations, it also has a novel feature that is counterintuitive from the point of view of fault-tolerance. The design of fault-tolerant protocols usually aims to prevent the propagation of single-qubit errors to many qubits. This is achieved, naturally enough, by applying gates that do not spread errors, e.g., transversal gates, or “long” gates that are interspersed with error correction steps, such as in lattice surgery [27]. In all of these methods, one actively avoids interacting one qubit with many others in a code block, since errors occurring on that qubit could propagate to the others, exceeding the error-correcting capabilities of the code.

In our protocol, we are actually deliberately taking this seemingly ill-advised approach: a single qubit () is coupled to every data qubit. The depth of the circuit scales linearly with the number of data qubits, and no error detection or correction is performed during the process. Nevertheless, the procedure is fault-tolerant in that any single-qubit error occurring in the circuit results in a constant-weight error on the final state. An interesting subtlety is that even though a single-qubit circuit-level error can in general be propagated by the subsequent gates to a highly nonlocal error, this nonlocal error is always equivalent under stabilizers of the prepared cluster state to some geometrically local error. More generally, we show that any m-qubit circuit-level error results in at most m geometrically local errors on the final state.

To summarize, we have discovered that fault-tolerant quantum computation can be achieved through the incremental improvement of a small number of key components, avoiding most of the systems engineering challenges inherent in leading approaches. This is possible because of three important features of our scheme. First, its physical realization only requires manufacturing and calibrating a constant number of experimental components, independent of the number of data qubits. Second, there are readily available physical platforms that can realize our protocol. Third, any constant-weight error occurring during our protocol results in a constant-weight error on the prepared cluster state.

In one aspect, the invention provides a device for fault-tolerant quantum computation comprising: a quantum emitter implementing a control qubit; a first router coupled to the quantum emitter; a second router coupled to the quantum emitter; a first delay line coupled to the first router and the second router, a second delay line coupled to the first router and the second router; and a detector coupled to the first router; wherein the first delay line, the second delay line, the first router, the second router, and the quantum emitter are configured to form two loops to support propagating modes implementing data qubits that passively interact multiple times with the control qubit to generate three-dimensional cluster states; wherein the quantum emitter implementing the control qubit is configured to generate the propagating modes implementing data qubits; wherein the first router and the second router are configured such that a propagating photon or phonon travels through each of the first delay line and second delay line a predetermined number of times before being measured by the detector; wherein the detector is configured to measure data qubits after multiple interactions with the control qubit.

In some embodiments, the first router and the second router may be configured such that a propagating photon or phonon travels through each of the first delay line and second delay line only once before being measured by the detector. In some embodiments, interactions of the data qubits with the control qubit are separated by time delays determined by the first delay line and the second delay line. In some embodiments, multiple interactions between the control qubit and data qubits are fixed and periodic. In some embodiments, each of the data qubits does not interact with other data qubits. In some embodiments, stable internal states of the quantum emitter encode qubit degrees of freedom for the control qubit, while radiative states of the quantum emitter that are coupled to the waveguides realize gates between the control qubit and a data qubit realized as a photon or phonon propagating in the waveguides. In some embodiments, the quantum emitter is an atom or an artificial atom, the first delay line and the second delay line are optical fibers, and the propagating modes are photons in the optical fibers. In some embodiments, interactions of the data qubits with the control qubit are implemented via resonant scattering. In some embodiments, the device is realized as an integrated superconducting circuit wherein the quantum emitter is a superconducting qubit, the first delay line and the second delay line are microwave waveguides, and the propagating modes are microwave photons. In some embodiments, the device is realized as a quantum acoustic system wherein the quantum emitter is a transmon qubit, and the first delay line and the second delay line are phononic waveguides. In some embodiments, the device has no more than one quantum emitter.

In another aspect, the invention provides a method for fault-tolerant quantum computation comprising: generating a three-dimensional cluster state using the device described above; and performing adaptive single-qubit measurements on the three-dimensional cluster state. In some embodiments, generating the three-dimensional cluster state comprises encoding multiple data qubits in a single waveguide by controlling the rate of the excitation pulses using a time multiplexing technique. In some embodiments, generating the three-dimensional cluster state comprises sequentially applying resonant coherent excitations to a quantum emitter. In some embodiments, generating the three-dimensional cluster state comprises applying a rapid resonant excitation pulses to a quantum emitter to induce spontaneous emission of a photon or phonon into a waveguide. In some embodiments, generating the three-dimensional cluster state comprises creating with a quantum emitter a propagating photon or phonon in a waveguide, routing the photon or phonon through a delay line, and scattering the propagating photon or phonon against the quantum emitter. In some embodiments, generating the three-dimensional cluster state comprises applying to a quantum emitter a sequence of resonant r pulses to induce transitions between internal states of the quantum emitter, where some of the states are stable and some are radiative. In some embodiments, the method includes performing measurements of a quantum emitter state via quantum non-demolition measurements.

## DETAILED DESCRIPTION OF THE INVENTION

We start by briefly reviewing the subject of fault-tolerant measurement-based quantum computation using cluster states, focusing on the aspects that are relevant to this invention.

### BACKGROUND

The cluster state |ψG corresponding to an undirected graph G=(V,E) is defined as

\(\begin{matrix}
{\left. {\left. \left| \psi_{G} \right. \right\rangle:={\left\lbrack {\prod\limits_{{({i,j})} \in E}Z_{i,j}} \right\rbrack\underset{i^{\prime} \in V}{\otimes}{❘ +}}} \right\rangle_{i^{\prime}},} & (1)
\end{matrix}\)

where each vertex i∈V is identified with a qubit, and Za,b denotes the controlled-Z gate on qubits a and b. The stabilizers of |ψG are generated by {Si:i∈V}, where [22]

\(\begin{matrix}
{{S_{i}:} = {X_{i}{\prod\limits_{j:{{({i,j})} \in E}}{Z_{j}.}}}} & (2)
\end{matrix}\)

Here, Xa, and Za denote Pauli X and Z on qubit a. Cluster states of the form of Eq. (1) are also referred to as graph states in the literature.

The importance of cluster states in the theory of fault-tolerant quantum computation was established by the seminal works of Raussendorf, Harrington, and Goyal [14, 15, 16], which demonstrated that universal fault-tolerant quantum computation can be performed via single-qubit measurements on a particular cluster state. This cluster state corresponds to the body-centered cubic (bcc) lattice shown in FIG. 3 and FIG. 5. Their scheme (for constructing this cluster state and extracting the syndrome) boasts a high threshold of pth≈0.58% [28] under the standard depolarizing model for circuit errors, making it one of the most promising approaches for building a large-scale quantum computer.

To prepare the cluster state |ψG corresponding to the bcc lattice Gbcc, Refs. [14, 28] consider a simple constant-depth circuit, which follows directly from Eq. (1). Each qubit is initialized in the state |+, and the controlled-Z gates in Eq. (1) for G=Gbcc are applied in four layers. It is straightforward to see that any single-qubit error in this circuit propagates to a constant-weight error on |ψG. Together with the fact that |ψG is a foliation of the surface code [29], this implies that there is a finite threshold for the circuit error rate below which the logical error rate decays exponentially with the system size.

Given a cluster state on an L×L×N bcc lattice, one can perform fault-tolerant quantum computation by adaptively measuring the qubits in one of three bases (the eigenbases of the operators X, Z, and

\(\left. {e^{i\frac{\pi}{8}Z}Xe^{{- i}\frac{\pi}{8}Z}} \right),\)

depending on the logical gates that are to be executed. Note that a qubit can be measured before the full cluster state has been prepared, provided that all of the controlled-Z gates in Eq. (1) involving that qubit have been applied. Thus, the cluster state could alternatively be prepared and measured in such a way that only O(L2) physical qubits are in use at any given time. Roughly speaking, L determines the number of logical qubits that can be encoded and the distance of the underlying code, while N is related to the length of the logical computation. We refer the reader to Refs. [8, 14, 16, 15] for further details.

Even though fault-tolerant computation can be in principle performed on such a cluster state, in this paper, we focus on realizing a fault-tolerant quantum memory. In particular, we consider using a cluster state on an L×L×L bcc lattice to store a single logical qubit. From the perspective of quantum error correction, this cluster state can be viewed as a space-time history of the surface code [30, 31] with L rounds of syndrome measurements, the bottom and the top boundaries of the cluster state corresponding to the surface codes at the initial and the final step of the error-correction protocol. Our estimates for the logical error rate, which decays exponentially with L under local noise models, quantifies the probability that there is a logical bit or phase flip between the bottom and the top layer.

The leading architecture for implementing this scheme is based on a two-dimensional array of physical qubits [16, 15, 11]. This approach suffers from an important practical problem, however. The space overhead, which is the ratio between the number of physical qubits and the number of logical qubits, is quite large in practice. For instance, the space overhead for running Shor's algorithm [32], assuming a physical error rate of 10−3, is estimated to be at least a few hundred [8, 33]. Thus, building even a single logical qubit with low enough error rate will require hundreds if not thousands of physical components. Moreover, these components will need to be carefully calibrated to ensure that the physical error rates across all of the qubits are sufficiently low. While this is not impossible, it certainly requires a Herculean effort.

### Main Results

Generally speaking, large space overhead is undesirable because the effort to build a fault-tolerant quantum computer may grow proportionately with the number of physical qubits. However, for the purpose of assessing the feasibility of a given architecture, it is important to distinguish the mathematical definition of space overhead from the engineering difficulty of building a quantum computer. We believe that a useful figure of merit for the latter is the component overhead, which is the number of basic experimental components used to build a single logical qubit. Of course, the precise definition of “experimental component” depends on the degrees of freedom that encode the quantum information. Once those degrees of freedom are identified, one can compare different protocols in terms of the required experimental components. This information can be related more directly to the feasibility of the protocol.

Component overhead can be an informative metric because the basic building blocks that constitute a large-scale fault-tolerant quantum computer may be difficult to mass manufacture. Even though there are several experiments that report error rates below the thresholds of various fault-tolerant quantum computing schemes [14, 16, 15, 8, 34], these numbers are often obtained in a manner that is incompatible with scalability. This is due to the practical reality that when the components are manufactured, they have sample-to-sample variations which lead to imperfect gates. Often, the reported numbers come from the very best of those samples, but if the variation is not negligible, many of the other samples will generally suffer from higher error rates. Therefore, given that high-quality components are difficult to come by, scalable fault-tolerant quantum computing protocols should aim to minimise the number of such components.

Motivated by this observation, we construct simple abstract protocols for fault-tolerant quantum computation that are amenable to extremely low component overhead. We also present concrete experimental proposals for realizing the protocols using a single transmon qubit interacting with a stream of phonons, or alternatively, an atom interacting with a stream of photons. Our protocols may be applicable more generally, e.g., to systems implemented using ions or neutral atoms. There are two distinguishing features of all these systems that are crucial. First, the degrees of freedom that encode the quantum information are either identical by nature or can be made to be nearly identical. Second, the qubits have long coherence times, leading to low memory error rates.

For systems that fulfill these conditions, we describe a simple method for preparing cluster states corresponding to the bcc lattice. FIG. 1 is a schematic illustration of a physical device for implementing our protocols. A quantum emitter 100 implementing a control qubit  generates propagating modes, e.g., photons or phonons, which implement data qubits. These data qubits are stored in delay lines 106 and 108 between their interactions with the control qubit . These interactions of the quantum emitter on the returning propagating modes implement quantum gates acting on the data qubits. After propagating through the delay line(s), resulting in a constant number of interactions with , each qubit is measured by a detector 110. Routers 102 and 104 are configured to route the qubits through the delay lines a constant number of times before they are sent to the detector. The device may be coupled to a digital controller that controls the operation of the detectors and control qubit in order to implement the methods described herein.

The section below on cluster state preparation provides the abstract description of our protocols, and the experimental realization section provides details of its various physical realizations. For example, the routers may be implemented using commercially available optical switches, superconducting circuits that guide the propagation of microwave photons, or one or more multi-mode mechanical oscillators with engineered phonon band structure such that the oscillators guide the propagation of phonons. In optical platform realizations, the detector may be implemented as one or more beam splitters coupled to one or more additional detectors such that photons or phonons in different frequency modes or polarization modes are separated into different spatial modes before detected by the additional detectors. The detectors may be implemented as one or more single photon detectors detecting or distinguishing one or more photons in different frequency modes, polarization modes, or spatial modes. The detectors may be implemented as one or more photon number counters detecting or distinguishing different numbers of photons in a mode. In microwave platform realizations, the detectors may be implemented as one or more microwave cavities coupled to one or more superconducting qubits such that the number of photons, the frequency modes of photons, or the spatial modes of photons in the cavities are identified by measuring the states of the qubits. In some quantum acoustic implementations, the detectors may be implemented as one or more mechanical oscillators coupled to one or more superconducting qubits such that the number of phonons, the frequency modes of phonons, or the spatial modes of phonons in the mechanical oscillators are identified by measuring the states of the qubits. In some implementations, the detectors comprise one or more mechanical oscillators coupled to optical resonators such that the number of phonons, the frequency modes of phonons, or the spatial modes of phonons in the mechanical oscillators are identified by measuring the states of photons from the optical resonators.

The procedure for implementing fault-tolerant quantum computation using the device of FIG. 1 involves two types of qubits, a single actively controlled qubit  and a large number of data qubits. Each data qubit interacts with  several times, and these interactions are separated by time delays determined by the size of the bcc lattice being implemented. The data qubits do not interact with each other. The gates applied between  and the data qubits are specified as described below in the section on cluster state preparation, and experimental techniques for realizing these gates are described in the experimental realization section below. The procedure is an extension of the photonic machine gun proposal of Ref. [35] and variants thereof [20]. These works advocated methods for creating cluster states on one- and two-dimensional lattices, respectively, neither of which are known to be useful resources for fault-tolerant quantum computation. In contrast, our protocol prepares the cluster state on the bcc lattice, which (as discussed in the background section above) can be straightforwardly used as a resource state for fault-tolerant measurement-based quantum computation.

Independent of the precise sequence of gates between the control qubit  and the data qubits, any protocol implemented on the device depicted in FIG. 1 is at risk of being strongly susceptible to noise. There are two potential sources of concern. The first is that  interacts with every single data qubit, without any intermediate syndrome measurements being performed. This creates the danger that an error occurring on  could propagate to all of the data qubits that subsequently interact with . The second issue is that there is a time delay between successive interactions of the same data qubit with . For generating an L×L×N bcc lattice, the total time delay is proportional to L2. Thus, the total memory error accumulated during these time delays may be significant.

The first of these is actually a non-issue. As discussed in the error analysis section, an important feature of our protocols is that even though single-qubit errors, including those on , may propagate to highly nonlocal errors, the effect of these errors on the prepared cluster state is always equivalent to that of geometrically local errors. Hence, using the standard depolarizing noise model for circuit errors and the usual minimum-weight perfect matching decoder, there is a finite threshold for the circuit error rate. We find threshold values of 0.23% and 0.39%, depending on the details of the protocol (see the section on 3D cluster states and the section below on thresholds). Therefore, if memory errors are negligible, the logical error rate can be arbitrarily suppressed by increasing L.

In contrast, for non-negligible memory error rates, the logical error rate cannot be made arbitrarily small, since increasing L also leads to an increase in the total error incurred during the time delays. We study these effects in the section on the effect of delay line errors by assuming a nonzero error rate r, per time step. As long as the circuit error rate is below threshold, we argue that by judiciously choosing L, the logical error rate can be made exponentially small in η−1/2. We perform extensive numerical simulations, whose results show excellent agreement with this prediction. Since the logical error rate decays significantly faster than η for small values of η, the effect of memory error can be mitigated.

The fact that our scheme leads to small but not arbitrarily small logical error rates is reminiscent of the fault-tolerant quantum computing schemes using anyons [30, 36, 37, 38] or 0-π qubits [39, 40, 41]. In these approaches, the logical error rate is exponentially small in some large physical parameter. In ours, this parameter is η−1/2.

### Cluster State Preparation

In this section, we present a general algorithm for preparing cluster states associated with arbitrary graphs G=(V,E). We then apply this algorithm in two different ways to prepare cluster states on the bcc lattice of Ref. [14].

The standard procedure for preparing cluster states is to initialize each qubit in the |+ state and apply controlled-Z gates according to Eq. (1). Since a controlled-Z gate between qubits a and b is required for every (a, b)∈E, this approach involves |E| distinct gates. All of these gates must be carefully calibrated and implemented, making the experimental realization of this protocol daunting.

In contrast, our protocols bypass the need to calibrate and implement a large number of physically distinct operations, allowing for simple experimental realizations, as explained in the experimental realization section below. In our algorithm, there is a single ancilla  that interacts with the data qubits (which correspond to the vertices V of G) one by one. Physically,  is an actively controlled qubit, while the data qubits are identical degrees of freedom (e.g., phonons or photons generated from a single source, ions, or neutral atoms) that passively interact with . The data qubits do not ever need to interact with each other. In this setting, one can simply tune a constant number of interactions between the controllable qubit and the physical system representing the data qubits to calibrate every gate.

**Algorithm for Arbitrary Graphs**

In this section, we provide an algorithm, Algorithm 1, for preparing cluster states |ψG on arbitrary graphs G. The correctness proof for this algorithm is given in the section below on the correctness of Algorithm 1.

First, we define some notation. Here and throughout the paper, Ha denotes the Hadamard gate acting on qubit a, and Pa the Pauli operator P∈{X, Y, Z} on qubit a. We write Xa,b to represent the controlled-X gate with control qubit a and target qubit b, and Za,b the controlled-Z gate between qubits a and b, with ≡I for any i∉V.

We also use the convention that the operators Aj in the product Πj=1kAj are ordered as AkAk−1 . . . A1, and that an empty product of operators acts as the identity.

The main idea behind Algorithm 1 is to generate progressively larger cluster states related to subgraphs of G=(V,E) by adding in one qubit at a time. Specifically, let n:=|V| be the number of data qubits and fix an ordering of the qubits by labelling them from 1 to n. For a given ordering, the qubit labelled 1 is added first, followed by the qubit labelled 2, and so on.

To explain the algorithm, it will be convenient to define graphs G[k]′ as follows. For each k∈[n]:={1, . . . , n}, let E[k] denote the set of edges in the subgraph of G induced by the vertex subset [k], i.e.,

E[k]:={(i,j)∈E:i,j∈[k]}.  (3)

Then, let

G[k]′:=([k]∪{},E[k]∪{(,k)})  (4)

be the graph with vertex set [k]∪{} and edge set E[k]∪{(,k)}.

FIG. 2A shows an example of a simple graph G=(V,E) and an ordering of its n=5 vertices, along with the corresponding graphs G[k]′ (see Eq. (4)) for k∈[5]. (The grey vertices and edges in G[k]′ for k∈[4] are not part of the graph.) Note that G[k]′ differs from the subgraph of G induced by [k] only in that it contains an extra vertex  and an extra edge (,k). For each k∈[n], the state of and the first k data qubits at the end of Line 4 in the kth for loop iteration in Algorithm 1 is the cluster state |ψG[k]′.

The cluster state |ψG[k]′ corresponding to G[k]′ is defined via Eq. (1). In the section below on the correctness of Algorithm 1, we prove that for each k∈[n], after Line 4 in the kth iteration of the for loop has been executed, the state of  and the first k data qubits is |ψG[k]′. Thus, Algorithm 1 prepares |ψG by introducing a new data qubit in each iteration, sequentially generating |ψG[1]′, |ψG[2]′, . . . , |ψG[n]′. The main steps are illustrated schematically in FIG. 2B. Since (3, 4)∉E in this example, the if condition of Line 5 is satisfied in the j=3 iteration, and Lines 6-9 are executed, shown in the figure for the third iteration as 200. Then, in the next iteration (j=4), Lines 3 and 4 change the state to |ψG[4]′, shown in the figure for the fourth iteration as 202. Note that  has the effect of swapping the state of  onto qubit i and adding an edge between  and i; see Eq. (24) in the section below on correctness of Algorithm 2.

Once we have the state |ψG[n]′ (at the end of Line 4 in the last iteration), the desired state |ψG can be easily obtained. Since the only difference between the two states is that |ψG[n]′ has an extra edge between  and n, i.e., |ψG[n]′=, we can either apply  or measure  in the Z-basis (and apply Zn if the outcome is |1).

As shown in the section below on the correctness of Algorithm 1, the purpose of applying Zj in Line 8 is to “fix” the cluster state in the case where  is measured in Line 6 of the jth iteration and the outcome is |1. Observe that all of the necessary Zj corrections could be deferred to the end of the procedure, instead of being implemented immediately. Alternatively, the Zj need not be applied at all if we keep track of all of the measurement outcomes and the modified cluster state stabilizers in the subsequent computation.

Note that different orderings of the qubits (i.e., different assignments of the labels 1 through n to the vertices in V) give rise to different circuits via Algorithm 1, but every such circuit correctly produces the same state |ψG. One may choose an ordering that is more conducive to experimental realization of the algorithm. Furthermore, in the case where G contains a Hamiltonian path, Algorithm 1 does not require any intermediate measurements of . By ordering the qubits such that (i,i+1)∈E for all i∈[n−1], Lines 6-9 are skipped in every iteration of the main loop, which simplifies the procedure.

**3D Cluster States**

In this section, we describe two protocols, Protocols A and B, for preparing cluster states on the bcc lattice Gbcc of Ref. [14]. FIG. 3 shows an elementary cell of the bcc lattice Gbcc=(Vbcc,Ebcc). FIG. 5 shows an example of a bcc lattice Gbcc, with L=M=5, and an ordering of its vertices.

Protocol A involves first using Algorithm 1 to prepare the cluster state on a cubic lattice, then measuring out certain qubits to obtain |ψG. Protocol B applies Algorithm 1 to Gbcc directly. We propose experimental implementations of both protocols in the experimental realization section.

These protocols have different strengths and weaknesses. Unlike Protocol B, Protocol A requires no intermediate measurements of the controllable qubit , and is therefore expected to be simpler to implement. However, as we show below in the section on thresholds, the error threshold of Protocol A is lower than that of Protocol B.

**Protocol A**

Protocol A has two main steps. First, we use Algorithm 1 to prepare the cluster state |ψG on a certain cubic lattice Gc, defined below, that contains Gbcc as a subgraph (Line 1). Second, we obtain |ψG) from |ψG by removing the qubits that are not in Gbcc via single-qubit Z-measurements (Lines 2-5).

The cubic lattice we consider is the graph Gc=(Vc,Ec) with vertex set Vc=[n] and edge set Ec, defined for L, M∈by

Ec:={(i,i+1):i∈[n−1]}

∪{(i,i+L):i∈[n−L]}

∪{(i,i+LM):i∈[n−LM]}.  (5)

If n=LMN for some N∈N, then Gc is a L×M×N cubic lattice with shifted periodic boundary conditions; Gc differs from a standard cubic lattice with open boundary conditions only in that Gc has various additional edges between vertices on the boundary.

Note from Eq. (5) that for every i∈[n−1], (i,i+1) is an edge in Gc. Consequently, when we apply Algorithm 1 to Gc the if condition of Line 5 is never satisfied and Lines 6-9 are not executed, except in the very last iteration (j=n) of the for loop. Thus, Algorithm 1 reduces to a unitary circuit that prepares |ψG[n]′, together with a single measurement of  at the end to change |ψG[n]′ to |ψG. This circuit is shown in FIG. 4, which illustrates how Algorithm 1 is applied to the cubic lattice Gc (see Eq. (5)) for L=3, M=2, and n=2LM. This circuit prepares |ψG on the data qubits, and is the first step of Protocol A. The top row of the circuit of FIG. 4 illustrates the operations of the emitter, or control qubit 400. The twelve rows below illustrate the data qubits of the cluster state being generated. The top row, from left to right, shows the control qubit 400 generating twelve qubits in sequence with Hadamard operations H between each emission. After a delays of three, the control qubit also interacts with one or more previously generated data qubits. These interactions between the control qubit and the data qubits are represented by vertical lines in the circuit. For example, the first generated data qubit is generated 402, then after a delay of three interacts 404 with the control qubit. It interacts again 406 after a second delay of three. Analogous interactions take place for subsequent data qubits in rows below, but shifted in sequence. The last operation could be replaced by .

Since the bcc lattice Gbcc is a subgraph of Gc, we can then measure the qubits of |ψG that are not in Gbcc in the Z-basis to remove them. We also need to measure all of the qubits on the boundary in Gc in the Z-basis, in order to get rid of the shifted periodic boundary conditions. Therefore, to prepare the cluster state on a L×M×N bcc lattice using Protocol A, we would generate the cluster state on a (L+2)×(M+2)×(N+2) cubic lattice in Line 1. After applying the appropriate Pauli corrections based on the outcomes of these measurements, we obtain the desired cluster state |ψG.

**Protocol B**

Protocol B prepares |ψG by directly applying Algorithm 1 to Gbcc.

Protocol B: prepare the cluster state |ψG on the bcc lattice Gbcc=(Vbcc, Ebcc) of Ref. [14]

**1: Apply Algorithm 1 to Gbcc**

For notational convenience, we adopt the following convention for the bcc lattice. We label the qubits of an L×M×N bcc lattice as we would an L×M×N cubic lattice, omitting the numbers corresponding to the cubic lattice sites that are “missing”—see FIG. 5 for an example illustrating this convention. FIG. 5 shows an example of a bcc lattice Gbcc, with L=M=5, and an ordering of its vertices. Certain qubit labels (e.g., 6, 8, 10, 16, 18, 20, 27, 29) are skipped, so that the neighbors of vertex i are given by {i±1, i±L, i±LM}∩Vbcc. Labels after 30 have been omitted for clarity of illustration only. This is a slight departure from the notation in Algorithm 1 (which assumes that the qubits are numbered from 1 through n), but the instructions of Algorithm 1 can be adapted straightforwardly. FIG. 6 shows part of the resulting circuit for the bcc lattice in FIG. 5 using Protocol B. The first row of FIG. 6 shows the operations of the control qubit, and the rows below show the data qubits. Vertical lines show interactions between the control qubit and the data qubits. Only the first 10 iterations of the for loop in Algorithm 1 are shown. This abridged circuit prepares |ψG[12]′ (see Eq. (4)). Note that all Pauli Z corrections conditioned on the outcomes of the measurements of  can be deferred to the end of the circuit.

Using our labelling convention, the nearest neighbors of a qubit i are simply {i±1, i±L, and/or i±LM}∩Vbcc. Each of the qubits, except those on the boundary, has four nearest neighbors, all of which lie in the same plane. Thus, we divide the qubits into three groups, Vxy, Vyz, and Vzx, where qubit i is in Vxy (resp. Vyz, Vzx) if the nearest neighbors of i are in the xy (resp. yz, zx) plane. Letting Nbcc(i) denote the set of nearest neighbors of i in Gbcc, we have (see FIG. 5)

\(\begin{matrix}
{{N_{bcc}(i)} \subseteq \left\{ {\begin{matrix}
\left\{ {{i \pm 1},{i \pm L}} \right\} & {i \in V^{xy}} \\
\left\{ {{i \pm L},{i \pm {LM}}} \right\} & {i \in V^{yz}} \\
\left\{ {{i \pm {LM}},{i \pm 1}} \right\} & {i \in V^{zx}}
\end{matrix}.} \right.} & (6)
\end{matrix}\)

For qubits i that are in the bulk of the lattice, the above holds with equality.

### Error Analysis

The protocols described earlier in the section on cluster state preparation are useful only insofar as they are fault-tolerant. The operations used in the protocols will generally be noisy, resulting in the preparation of imperfect cluster states. Since the ancilla qubit  interacts with every data qubit in Algorithm 1, single-qubit errors occurring during the procedure may propagate through the subsequent operations to highly nonlocal errors. We show, however, that the effect of these errors on the target cluster state is always equivalent to that of geometrically local errors. This allows us to demonstrate that for both Protocols A and B, there is a threshold for the circuit error rate below which the logical error rate rapidly decays with the system size.

To make our reasoning precise, let g1, . . . , gD denote the sequence of Clifford gates in Algorithm 1, and for j, k∈[D], let Cjk:=Πi=jkgi. (Note: Lines 6-9 of Algorithm 1 have the same combined effect as that of a deterministic Clifford gate, and can be treated as such for this discussion. A Pauli error occurring between Lines 6 and 9 is equivalent to a Pauli error occurring after these steps.) Then, if a Pauli error Pa occurs on some qubit a between the gates  and , the erroneous circuit implements . The prepared state is

|ϕinitial=Q|ϕfinal,  (7)

where |ϕinitial is the input state, |ϕfinal=C1D|ϕinitial denotes the state prepared by the error-free circuit, and Q:=. In other words, the circuit-level error Pa propagates to an error Q, which may be highly nonlocal in general. In fact, for certain choices of Pa and , it the weight of Q scales with the total number of qubits.

However, Eq. (7) holds for arbitrary |ϕinitial, with Q independent of the initial state. The fact that errors propagate nonlocally for generic input states is not necessarily an issue the purpose of Algorithm 1 is not to perform some computation on arbitrary inputs, but rather, to prepare a fixed resource state. Therefore, the only relevant analysis is that for the particular input state |ϕinitial:|+⊗i=1n|0i to Algorithm 1, which leads to the particular output state |ϕfinal=|+|ψG. Clearly, Q|ϕfinal=QS|ϕfinal for any stabilizer S of |ϕfinal. Therefore, even if Q is a high-weight operator, it may have the same effect on |ϕfinal as a low-weight operator.

It will hence be useful to define the notion of effective errors. We say that a circuit-level Pauli error Pa occurring at depth  results in an effective error E if

|initial=E|ϕfinal).  (8)

This definition generalizes straightforwardly to arbitrary circuit-level errors. Note that unlike Eq. (7), Eq. (8) is not a gate identity, as it may depend crucially on the input state |ϕinitial. Note also that E is not unique.

If multiple Pauli errors occur in the circuit, their joint effect is multiplicative up to a sign. To see this, consider two Pauli errors Pa and Pb occurring at depths  and 2, respectively, with 1≤2. Suppose that the circuit-level error Pa (at depth 1) results in an effective error E1, in the sense of Eq. (8), and Pb (at depth 2) results in an effective error E2. Then, the circuit containing both errors prepares

\(\begin{matrix}
\begin{matrix}
\left. {\left. {C_{\ell_{2}}^{D}P_{b}C_{\ell_{1}}^{\ell_{2} - 1}P_{a}C_{\ell_{2}}^{\ell_{1} - 1}{❘\phi_{initial}}} \right\rangle = {\left\lbrack {C_{\ell_{2}}^{D}{P_{b}\left( C_{\ell_{2}}^{D} \right)}^{\dagger}} \right\rbrack C_{\ell_{1}}^{D}P_{a}C_{\ell_{1}}^{\ell_{1} - 1}{❘\phi_{initial}}}} \right\rangle \\
\left. {= {\left\lbrack {C_{\ell_{2}}^{D}P_{b}\left( C_{\ell_{2}}^{D} \right)^{\dagger}} \right\rbrack E_{1}C_{1}^{D}{❘\phi_{initial}}}} \right\rangle \\
\left. {= {\left( {- 1} \right)^{s}E_{1}C_{\ell_{2}}^{D}P_{b}C_{1}^{\ell_{2} - 1}{❘\phi_{initial}}}} \right\rangle \\
{\left. {= {\left( {- 1} \right)^{s}E_{1}E_{2}{❘\phi_{initial}}}} \right\rangle,}
\end{matrix} & (9)
\end{matrix}\)

where the second and fourth equalities use Eq. (8), and the phase (−1)s is either +1 or −1 depending on whether E1 and  (which are both Pauli products) commute or anticommute. Thus, the two circuit-level errors collectively result in an effective error E1E2, up to a sign. Analogous results hold for more than two errors.

It follows that in order to study a stochastic noise model involving Pauli errors, it suffices to analyze the effective errors resulting from single-qubit circuit-level errors. The effect of multi-qubit circuit-level errors can then be inferred from Eq. (9).

As we discuss below in the section on effective errors, any single-qubit error occurring during Protocols A or B results in a local effective error on the final state. This is a special case of the more general result, proven in the section on error analysis for Algorithm 1, applied to arbitrary graphs. In the section below on thresholds, we estimate the threshold circuit error rates for both protocols, obtaining 0.23% for Protocol A and 0.39% for Protocol B.

**EFFECTIVE Errors**

In this section, we consider the effect of errors that occur during Protocols A and B, both of which prepare the cluster state |ψG on the bcc lattice Gbcc. These protocols both apply Algorithm 1 (but to different graphs). In the section on error analysis for Algorithm 1, we prove that for any graph G=(V,E), any single-qubit error occurring between the elementary operations of Algorithm 1 results in an effective error (see Eq. (8)) that is geometrically local, in the sense that it is supported within {i}∪N(i) for some data qubit i∈[n], where N(i):={j: (i,j)∈E} denotes the nearest neighbors of i in G.

The proof uses the following key observations.


- - 1) First, it is clear from FIG. **4** and FIG. **6** that any Z_(i)
    error on a data qubit i∈\[n\] either occurs before the
    gate and has no effect, as the initial state of i is \|0
    , or it occurs after the
    , in which case it commutes with all subsequent operations and ends
    up as a Z_(i) error on the final state. Thus, any single-qubit Z
    error on a data qubit results in either no error or a Z error on the
    same qubit.
  - 2) Second, the instantaneous state of the qubits at any point in the
    procedure is a cluster state, (up to a Hadamard
    on the ancilla
    ) as illustrated by FIG. **2**B. In the underlying graph of any of
    these intermediate cluster states, every edge between data qubits is
    also an edge in the graph G of the target state \|ψ_(G)
    , and the only edges involving the ancilla
    are between
    and j∈S for a subset S of N(i) for some i∈\[n\]. It then follows
    from the stabilizer condition, Eq. (2), that any single-qubit X
    error in the circuit has the same effect as a set of Z errors
    confined to the neighbors of some data qubit (and possibly
    ).  
    Combining these two observations with Eq. (9), it can be shown that
    any single-qubit Pauli error leads to an effective error of the form
    Π_(j∈S′)Z_(j), where S′⊂{i}∪N(i) for some i∈\[n\]. We fill in the
    details in the section on error analysis for Algorithm 1. Here, we
    simply summarize the results that are relevant to the threshold
    calculations in the following section.

We start by considering the effective errors in Protocol A. Recall that the first step (Line 1) applies Algorithm 1 to the cubic lattice Gc, defined by Eq. (5), yielding a circuit of the form of FIG. 4. Table 1 lists all of the X and Z errors that may occur in this circuit and the effective errors they give rise to. Note that it suffices to consider the effect of single-qubit X and Z errors, as the effect of arbitrary errors can then be inferred by decomposing them in terms of Pauli operators and using Eq. (9). To clearly distinguish between the gates in the circuit, we use Aj to denote the jth

“block” of gates (see Line 4 of Algorithm 1), Aj: =. (10)

Here and in Table 1, we have chosen to apply  before . The order of these controlled-Z gates could of course be changed, in which case the second and third entries in Table 1 would be slightly different (see Table 4 in the section on error analysis for Algorithm 1).

Spatially, circuit-level errors may occur on the ancilla  or a data qubit i∈[n], and temporally, they may be located between two blocks Aj and Aj+1, before the first block A1, after the last block An, or between two gates in the same block. Table 1 covers all of these possibilities.

By Eq. (5), the set Nc(i) of nearest neighbors of qubit i in Gc is

Nc(i)={i±1,i±L,i±M}∩[n].

Hence, we can see from Table 1 (and Eq. (2)) that any single-qubit X error results in an effective error of the form Πj∈SZj up to a sign, where S⊂Nc(i) for some i∈[n], while any Z error results in either no effective error or a single-qubit Z error. Moreover, X and Z errors occurring at the same spacetime location in the circuit result in effective (Z) errors supported within {i}∪Nc(i) for the same i, which implies that any single-qubit error occurring at that location leads to an effective error supported within {i}∪Nc(i). This is easily verified using Table 1. As an example, an X error on  between gates  and  in Ak results in an effective error Zk−LMZk−1, while a Z error at this location results in a Zk error, and k, k−LM, k−1∈{k}∪Nc(k).

Therefore, at the end of Line 1 of Protocol 1, the effective error induced by any single-qubit error can be decomposed into Z operators supported within some neighborhood of Gc. Note that the remaining steps, Lines 2-5, of Protocol A do not propagate this effective error further, as Z errors commute with Z gates and do not affect Z-measurements. By the same argument, a single-qubit Z error occurring during Lines 2-5 does not propagate to other qubits. It is also clear that a single-qubit X error on qubit i occurring during these steps is equivalent to Z errors on a subset of Nc(i). It follows that the effective error on |ψGbcc resulting from any single-qubit error in Protocol A is geometrically local with respect to Gc, i.e., supported within the neighborhood {i}∪Nc(i) of some qubit i∈[n]. Such an error is also geometrically local with respect to Gbcc if i∈Vbcc, while if i∉Vbcc, it is still confined to an elementary cell of Gbcc (see FIG. 3).

An even stronger result holds for Protocol B, which directly prepares |ψG using Algorithm 1. Table 2 lists the effective errors resulting from all possible single-qubit X and Z errors. In the table, Bj denotes the block of gates applied in the for loop iteration of Algorithm 1 (for G=Gbcc) corresponding to qubit j. Recalling the labelling convention for Gbcc described in Protocol B,

{ B j := \{ j ∈ V xy - LM j ∈ V yz j ∈ V zx ( 11 ) }

As shown in FIG. 6,  is measured and reset between certain gate blocks, and Table 2 includes the effects of measurement and reset errors as well. It is clear from Table 2 and Eq. (6) that the effective error induced by any single-qubit Pauli error is equivalent to a product of Z operators supported within {i}∪Nbcc(i) for some i∈Vbcc. Thus, single-qubit errors occurring at any spacetime location in Protocol B result in effective errors on |ψG that are geometrically local with respect to Gbcc.

Since all vertices in Gc and Gbcc have constant degree, it follows (from Eq. (9)) that any m-qubit circuit-level error results in an effective error of weight cm for some constant c independent of the system size. Standard arguments then imply that for both Protocols A and B, there is a finite threshold for the circuit error rate [42, 43]. We compute these thresholds in the following section.

We make a side remark on the role of intermediate measurements. It is tempting to guess that these measurements are responsible for the locality of the effective errors, but that is emphatically not the case. In Protocol A, no intermediate measurements are ever performed during the preparation of |ψG, yet all of the effective errors are geometrically local with respect to Gc (see Table 1). It is surprising that there is a nontrivial extensive-depth fault-tolerant protocol without intermediate measurements; the usual approach involves frequent intermediate measurements to extract syndrome information, so that one can catch the errors. In contrast, we only perform error correction at the very end, after an extensive-depth circuit has been executed. Finding necessary and sufficient conditions under which this is possible is an important open problem left for future work.

**Thresholds**

Using the results of the previous section, we can calculate error thresholds for our protocols via Monte Carlo simulations. In order to compare Protocols A and B to the standard cluster state preparation circuit in Ref. [14], we consider the standard depolarizing model (Error Model 1 below) and use the minimum-weight perfect matching (MWPM) decoder [14, 44]. We also study the effect of qubit loss (Error Model 2) using the decoder of Ref. [28], which is also based on MWPM.

For various values of the circuit error rate p, loss error rate ploss, and size L, we estimate the logical error rate  for generating an L×L×L cluster state |ψG

(storing one logical qubit). We average over at least 106 independent instances and at least 104 logical errors for each set of parameters. For each ploss, we then estimate the threshold circuit error rate pth by fitting the data to a quadratic scaling ansatz

=a+b(p−pth)d1/ν+c(p−pth)2d2/ν,  (12)

where d=(L+1)/2.

**Error Model 1**

Error Model 1 is the standard depolarizing model. In this model, every single-qubit gate on a qubit a is followed by a single-qubit depolarizing channel

{ a ( p ) ( ρ ) = ( 1 - p ) ⁢ ρ + p 3 ⁢ ∑ P ∈ \{ X , Y , Z \} P a ⁢ ρ ⁢ P a
( 13 ) }

on a. In addition, every (re-)initialization of a is followed by a(p), and every measurement of a is preceded by a(p). Here, measurements include not only those in Protocols A and B, but also the eventual X-measurements on data qubits that are required for extracting the syndrome. Similarly, every two-qubit gate on qubits a and b is followed by a two-qubit depolarizing channel

{ a , b ( p ) ( ρ ) = ( 1 - p ) ⁢ ρ + p 15 ⁢ ∑ P , P ′ ∈ \{ I , X , Y , Z
\} ( P , P ′ ) ≠ ( I , I ) P a ⁢ P b ′ ⁢ ρ ⁢ P a ⁢ P b ′ . ( 14 ) }

We refer to p as the circuit error rate.

For Protocols A and B, we can simulate the effect of each of these depolarizing errors on the final state using Tables 1 and 2. Our results (along with the fits to Eq. (12)) are shown in FIGS. 7A, 7B, which are plots of logical error rate  vs. circuit error rate p using Error Model 1 for Protocol A and Protocol B, respectively. Solid curves are fits to Eq. (12). The threshold circuit error rate pth is found to be 0.23% for Protocol A and 0.39% for Protocol B.

In comparison, the threshold for the scheme of Ref. [14] under the same error model is 0.58%. Refs. [16, 15] improve this to 0.75% by exploiting sublattice correlations, and Ref. [28] obtains 0.63% by accounting for the degeneracies of different matchings. We do not exploit correlations nor account for degeneracy in our decoder.

We surmise that the threshold for Protocol A is lower than that for Protocol B due to the following reasons. First, Protocol A uses substantially more qubits and operations than Protocol B to prepare a cluster state of the same size, giving rise to more error locations under Error Model 1. Second, all of the effective errors in Protocol B are geometrically local with respect to the bcc lattice Gbcc, whereas some of the effective errors in Protocol A are only geometrically local with respect to the cubic lattice Gc. For example, suppose that an X error occurs on a qubit i∈Vc\Vbcc immediately before the Z-measurement of i in Line 3 of Protocol A. By Eq. (2), this results in a Z error on all of the neighbors of i in Gc, which constitutes a weight-6 error on the face qubits of an elementary cell of Gbcc (see FIG. 3). In contrast, all of the effective errors resulting from single-qubit errors in Protocol B are geometrically local with respect to Gbcc, and, moreover, have weight at most 4 (when restricted to either the primal or dual lattice).

**Error Model 2**

Next, we add detectable loss errors to the standard depolarizing noise model. In Error Model 2, every elementary operation is followed or preceded by a depolarizing channel with error rate p in exactly the same way as in Error Model 1. In addition, each data qubit is lost by the end of the procedure with probability ploss. Hence, Error Model 2 reduces to Error Model 1 for ploss=0. We assume that if a qubit i is lost at some point, then any subsequent operation on i is replaced by the identity operator followed by depolarizing noise with rate p. The assumption that losses are detectable and that operations involving lost qubits implement the identity is consistent with the experimental setup considered in the experimental realization section.

FIGS. 8A, 8B shows our estimates for the threshold circuit error rate pth at various values of ploss in Error Model 2, for Protocol A and Protocol B, respectively. Squares indicate thresholds pth for the circuit error rate p at various loss rates ploss. Solid curves are quadratic fits to the data. The shaded region (p<pth) represents the correctable region of parameter space, in which the logical error rate can be suppressed by increasing the system size.

Extrapolating to pth=0, these fits give rough estimates for the loss threshold of 5.7% for Protocol A and 21.6% for Protocol B. Both plots have the same structure as FIG. 3 in Ref. [28], which provides thresholds for the circuit of Ref. [14] under the same error model (but using a slightly better decoder, as discussed above).

The loss threshold for Protocol A is significantly lower than that for Protocol B due to the fact that in our simulations, losing a qubit in Vc\Vbcc amounts to losing (up to) six qubits in Vbcc. This is because if a qubit i∈Vc\Vbcc is lost, we would not know whether the correction Πj∈N(i)Zj should be applied in Line 5 of Protocol A. Instead of simulating this as a weight-6 Z error (with probability 1/2), we simply treat all of the qubits in Nc(i) as having been lost in the decoding algorithm. Thus, the total probability of “losing” a qubit in Vbcc is greater than ploss for Protocol A.

While Error Model 2 allows for a direct comparison to Ref. [28], and may be an informative model for settings where the total loss probability is constant, it does not properly capture the structure of the noise expected when storing the data qubits in delay lines. Informed by the description of possible experimental implementations in the next section, we revisit the effect of delay line noise in the section on the effect of delay line errors.

### Experimental Realization

In this section, we describe experimental realizations of the protocols and devices described above, focusing on implementations in quantum nanophotonic and acoustic systems [45, 46]. Recent advances in the deterministic generation of single photons and single phonons [47, 48] and their coherent interactions with a single quantum emitter [49, 50, 51, 52, 53, 54, 26, 55] make these systems useful platforms for quantum information processing. Indeed, single and double chains of one-dimensional cluster states have already been produced in experiments using photons emitted from quantum dots [56]. These experiments implement modified versions of the circuit in Ref. [35], which is a specific instance of Algorithm 1. The techniques detailed in Refs. [20, 35] can be adapted to our more general protocols, to create cluster states on different graphs. In particular, the experimental setup considered in Ref. [20] can be directly extended to implement the first step of Protocol A (see FIG. 4), providing a simple procedure for preparing a three-dimensional cluster state on a cubic lattice. Universal fault-tolerant quantum computation can then be performed by making adaptive single-qubit measurements on this state [14].

There are several key ingredients used for realizing Protocols A and B. A first ingredient is to implement the elementary operations in these protocols, namely, the single-qubit operations on  the controlled-X gates  and controlled-Z gates  between  and data qubits, and single-qubit measurements of the data qubits. A second ingredient is to coordinate the interactions between  and the data qubits such that these operations are applied in the correct order. A third ingredient is to perform error correction when the loss rate is significant, which involves encoding the qubit states in such a way that losses are detectable.

These capabilities can be naturally achieved in a device having only a single quantum emitter (e.g., an atom, ion, transmon, or quantum dot) coupled to a photonic or phononic waveguide (see FIG. 9A). In such a system, any stable internal states of the emitter can be used to encode qubit degrees of freedom for , while any radiative states of the emitter that are coupled to the waveguide can be leveraged to realize certain gates between  and a photon or phonon propagating in the waveguide. We show below that the set of available gates is sufficient for Algorithm 1. Moreover, the routing of the photons or phonons required to realize the geometry of the target graphs of Protocols A and B is rather simple.

**Encoding Schemes and Elementary Gates**

In this section, we describe two encoding schemes and the gates in quantum photonic or acoustic systems that can be implemented in these schemes. We will refer to these as the single-rail and the dual-rail encoding schemes, summarized in FIGS. 9A, 9B, 9C and FIGS. 10A, 10B, respectively.

**Single-Rail Encoding**

FIG. 9A shows a quantum emitter 900 with three relevant quantum states: Two stable states, 902 and 904 (states |0 and |1, respectively), form a control qubit, while an extra unstable excited state 906 (state |e) is used to generate photons or phonons 908 propagating in a waveguide 910 in a guided mode to generate data qubits. Arbitrary single-qubit gates on  can be realized via resonant coherent excitations between |0 and |1.

In the single-rail scheme, the |0 (resp. |1) state of each data qubit i is encoded by the absence (resp. presence) of a photon or phonon. Multiple data qubits can be encoded in a single waveguide by controlling the rate of the excitation pulses, in the so-called time multiplexing technique. More specifically, if the pulse-to-pulse time separation  is sufficiently long compared to the temporal extent of an emitted photon/phonon mode, different modes separated by  have exponentially small over-lap [20]. We note that the temporal extent of each emitted mode, or equivalently the effective emission rate γ′, can be controlled using advanced techniques such as pulse shaping [20, 47].

Then, for the two-qubit gates  note that each  in Algorithm 1 is applied when data qubit i is in its initial state |0. This means that instead of implementing a controlled-X gate  that correctly transforms arbitrary states of i, we can use an operation  that has the same effect as  when i is in the specific state |0 (i.e., i=i for any state | of , potentially entangled th the rest of the system). As illustrated in FIG. 9B, the operation  912, which has the same effect as  when acting on |0i (see Eq. (15)), can be implemented via selective emission of a photon/phonon to the guided mode. In particular,  can be realized by applying to  916 a rapid resonant excitation pulse 920 causing a transition |1→|e, which is followed by the spontaneous emission 922 of a photon/phonon 918 into the waveguide 914.

This excitation-emission process deterministically generates a single photon/phonon in a particular temporal mode (controlled by the timing of the excitation pulse and the decay rate γ), conditioned on the state of  being |1. Thus, the net effect is

rest+|0i|ϕ1rest|0i|ϕ0rest+|1i|ϕ1rest,  (15)

where |ϕ0rest and |ϕ1rest are (unnormalised) states of the rest of the system.

As illustrated in FIG. 9C, the controlled-Z gate,  924, can be naturally realized by scattering a propagating photon/phonon 926 against the emitter  928 [50, 51, 52, 53, 54]. If  is in the state 10), the photon/phonon 926 propagating in the waveguide 930 remains unaffected due to the absence of any resonant couplings. On the other hand, if  is in the state |1, the propagating photon (phonon) is scattered by  owing to the resonant transition |1|↔|e, giving rise to a scattering phase eiθ. By engineering γ′<<γ, this scattering phase approaches eiθ≈−1, and this process effectively applies .

**Dual-Rail Encoding**

In the dual-rail scheme, a qubit degree of freedom is encoded in two distinct internal modes of a single photon/phonon, such as different polarizations or frequencies. When photon/phonon loss is the dominant source of error, the dual-rail scheme can be advantageous since the detection of a single photon/photon heralds the absence of loss errors (assuming no false-positive detections). As shown earlier in the section on thresholds, the threshold for loss errors is significantly higher than that for depolarizing noise, for both Protocols A and B.

FIG. 10A and FIG. 10B are schematic diagrams illustrating how to encode quantum information in two distinct modes of a single photon state (dual-rail schemes). As shown in FIG. 10A, an emitter 1000 has quantum states |0, |1, |e, |0′, and |e′ that allow the |0 state to be mapped into distinct photonic (phononic) modes in the waveguide 1002. In particular, application to the emitter 1000 of a resonant excitation 1004 or 1006 induces a transition |0→|1 or |0→|0′, respectively. Similarly, application to the emitter 1000 of a resonant excitation 1008 or 1010 induces a transition |1→|e or |0′→|e′, respectively. States |1 and |0′ are both stable, while states |e and |e′ are radiative, rapidly decaying back to |1 and |0′, respectively, by emitting a photon/phonon 1012 or 1014, respectively, into the waveguide 1002. In general, the photons/phonons emitted from |e and |e′ are distinguishable by their internal modes. We denote these modes using two distinct annihilation operators, b1 and b0.

Then, the realization of the  gate (more precisely, the preparation of the state |0i, for arbitrary | in the dual-rail scheme can be achieved via a sequence of resonant π-pulses between the |0↔|0′, |1↔|e, and |0′↔|e′ transitions. FIG. 10B illustrates an example of the pulse sequence that effectively realizes the  gate acting on a quantum state with the 1th data qubit in |0 (see Eq. (16)). The bars in the figure represent resonant π-pulses. First, a rapid resonant excitation pulse 1016 is applied, inducing the transition |0→|0′, leading to the process

|øi|ϕ0rest+|øi|ϕ1rest→|øi|ϕ0rest+|øi|ϕ1rest,

where |øi is the vacuum initial state of the ith temporal bin in the waveguide and |ϕ0rest and |φ1rest are unnormalised states of the rest of the system. Second, resonant excitation pulses 1018 and 1020 are applied, inducing both the |1→|e and |0′→|e′ transitions, which is followed by the emission of a photon/phonon at the ith bin in b1 or b0, depending on the internal state of the emitter. The state of the system after this emission is

(b0†|øi)|ϕ0rest+(b1†|øi)|ϕ1rest.

Finally, another resonant π-pulse 1022 is used to move the population from |0′ to |0. The net effect of these processes is the map

|øi|ϕ0rest+|øi|ϕ1rest→(b0†|øi)|ϕ0rest+(b1†|øi)|ϕ1rest.  (16)

Hence, by identifying |0i≡b0†|øi and |1i≡b1†|øi, these operations achieve the desired effect.

The realization of the controlled-Z gate remains unmodified from that described in the section on single-rail encoding. That is,  can be implemented via a simple resonant photon/phonon scattering process, since a photon/phonon in the mode b0 does not interact with the |0 nor |1 states of the emitter.

**Implementation Details**

We now explain how to use the encoding schemes and elementary operations described in the above section on encoding schemes and elementary gates to implement Protocols A and B. On top of being able to realize the gates individually, the data qubits should be routed so that these gates are applied in the correct order. Moreover, for Protocol B, we perform intermediate measurements on the emitter .

For both protocols, we control the ordering of the sequential interactions between  and the photons/phonons representing the data qubits. This can be achieved by introducing time-delayed feedback. In the proposal of Ref. [20], a single delay line is used to generate a cluster state on a two-dimensional square lattice with shifted periodic boundary conditions. This procedure can be generalized to prepare the cluster state on the cubic lattice Gc defined in the section on Protocol A, by introducing two delay lines of appropriate lengths to realize the circuit of Line 1 of Protocol A (see FIG. 4).

Specifically, consider the setup illustrated in FIG. 1, which involves two routers 104, 102 and two delay lines 106, 108. The routers are configured such that a propagating photon/phonon travels through each delay line only once before being measured at the output port. By setting the delay times for Delay 1 and Delay 2 to D1= and D2=(3L(M−1)−1), respectively, where  is the pulse-to-pulse time separation between distinct data qubit modes, one obtains a cluster state on an L×M×N cubic lattice Gc. The multiplicative factor of 3 accounts for the fact that there are up to three interactions in every block (see Eq. (10)). The delay times D1 and D2 can be effectively tuned using well-established techniques such as electromagnetically induced transparency [57] for coherent atomic media or band-structure engineering for photonic/phononic crystals [58].

FIG. 11 shows the implementation of the circuit of Protocol A for L=3, M=N=2 implemented in a quantum nanophotonic or acoustic system in the single-rail encoding scheme. The data qubits are initialized in vacuum |ø=|0, and the  gates, as in FIG. 4, are implemented via selective photon/phonon emissions, represented here by b†. The diagram for the dual-rail scheme is analogous, with the controlled-b† operations replaced by the process in Eq. (16). As shown in the top row of the diagram, quantum emitter  1100 sequentially creates and interacts with the data qubits, whose states in the single-rail scheme are encoded by the absence or presence of a photon/phonon in a guided, propagating mode. For example, the emitter creates the first data qubit at node 1102 of the circuit diagram, then interacts with it at node 1104 after it has passed through the first delay line, and interacts with it again at node 1106 after it has passed through the second delay line. The generalization of this procedure to the dual-rail scheme is straightforward. As detailed in the section on encoding schemes and elementary gates, the  gates in FIG. 4 can be implemented via selective photon/phonon emission, while the  gates can be realized via resonant scattering.

Protocol B can be implemented in a similar way, with the following modifications. First, since the bcc lattice Gbcc is a subgraph of the cubic lattice Gc, a subset of the cubic lattice sites should not host data qubits. Second, one performs projective measurements on the emitter , followed by re-initializations of  in a predetermined state, e.g., |+. The first task can be easily achieved by simply skipping the excitation pulses for the  gates at the appropriate times. The data qubits at the corresponding locations then remain in the vacuum state, decoupled from the rest of the system throughout the procedure.

The measurements of  can be implemented via quantum non-demolition measurements. A practical challenge is that the time duration; meas of the measurement and re-initialization process can be substantial, constraining the minimum separation >meas/3 between the temporal modes of consecutive data qubits. In turn, a longer  implies that fewer data qubits can be stored in delay lines with non-negligible loss rates. It may therefore be more practical to use Protocol A in some settings, to avoid intermediate measurements of  altogether. (Further, for an alternative algorithm that prepares arbitrary cluster states without any measurements of , see the alternative algorithm described below.)

**Effect of Delay Line Errors**

In the experimental realization section earlier, the amount of time a photon/phonon spends in the delay lines grows with the size of the target cluster state (more precisely, with the cross-sectional area of the underlying bcc lattice). As a result, the cumulative effect of delay line errors may be non-negligible. If the cluster state size becomes too large, the total error incurred in the delay lines overwhelms the improved error correction properties due to the increased code distance, leading to high logical error rates. In this section, we study two phenomenological models that incorporate the effect of delay line errors, and determine how the optimal logical error rate depends on the delay line error rate in each model. These models address the increase in loss probability with delay line length as well as dephasing errors on the data qubits, two effects that were ignored in the error analysis section.

### Analysis

The dominant sources of error in delay lines (for photons and phonons) are dephasing and loss, which we consider in Error Models 3a and 3b, defined below. We parameterize these models using the delay line error per time step. Here, the time it takes to execute the block of gates in Line 4 of Algorithm 1 constitutes one time step, and the time to measure and reset  in Lines 6 and 9 constitutes another time step. We assume that the time steps are equal. (To elaborate, we assume that the operations are temporally arranged, by pulsing or measuring  at appropriately spaced intervals, such that these time steps are all of the same length. This allows for the geometry of the bcc lattice to be naturally realized in Protocol B, since the measurements of  coincide with the sites in the bcc lattice that are “missing” relative to the cubic lattice (see FIG. 5).) In Protocol B, for instance, each time step consists either of a controlled-X gate, a Hadamard gate, and up to two controlled-Z gates, or of a measurement and re-initialization of . Thus, for preparing a cluster state on an L×M×N lattice, there are L time steps in Delay 1 and L(M−1) time steps in Delay 2 (see FIG. 1 and FIG. 11). We will use ηZ and ηloss to represent the dephasing error and loss per time step, respectively.

Let us make a brief comment on how these delay line errors change the analysis in the error analysis section. Dephasing errors are generally equivalent to stochastic Pauli Z errors, while the effect of losing a qubit during the procedure depends on the encoding scheme and gate implementations. In the experimental setup described in the experimental realization section above, the loss of a data qubit simply results in any subsequent gates involving that qubit not being applied. This is because these gates are realized via interactions between a photon/phonon wavepacket with the emitter. If the wavepacket is not present, the interaction does not occur. Moreover, in the dual-rail scheme described above, losses are detectable. We can therefore use the decoder of Ref. [28] as we did in the section on thresholds.

For circuit errors, we use the same depolarizing noise model, Error Model 1, as earlier in the section on thresholds, but with one modification. We omit the depolarizing channel that occurs after the initialization of each data qubit. This is motivated by the fact that in our experimental setup, each photon/phonon is created by the process that implements the controlled-X gate (see Eq. (16)). Strictly, this differs from Algorithm 1 (as it is formally stated), in which a data qubit i is initialized first, before  is applied to it in a separate step. In order to be able to suppress error, the circuit error rate p should be below the threshold for this modified error model. Since the threshold for Error Model 1 was estimated to be pth=0.39% (for Protocol B), we will assume that p=10−3, which is a standard number used in the literature for studying the sub-threshold behavior of the surface code [11].

With the above considerations in mind, we define Error Models 3a and 3b as follows. We fix p=10−3. In both models, every single-qubit gate on a qubit a is followed by a single-qubit depolarizing channel a(p) (see Eq. (13)). Every measurement of a qubit a is preceded by a(p), and every (re-)initialization of  is followed by . Similarly, every two-qubit gate on qubits a and b is followed by a two-qubit depolarizing channel a,b(p) (see Eq. (14)). In Error Model 3a, in addition to these circuit errors, a dephasing channel

(η)(ρ)=(1−ηZ)ρ+ηZZρZ

is applied to every data qubit in each time step. In Error Model 3b, each data qubit is lost by the end of the procedure with probability 1−exp(−ηloss), where  is the total number of time steps the qubit spends in the delay lines. If a qubit i is lost at some point, then any subsequent operation on i is replaced by the identity operator followed by i(p). In the following discussion, we will often refer to the delay line error rate as η, where η is ηZ for Error Model 3a and ηloss for Error Model 3b. (In reality, one would expect both dephasing and loss errors to occur in an experiment. Analysing their effects separately greatly simplifies the numerics, however. In many circumstances, one form of noise will dominate, in which case the results for the corresponding error model should provide a good guide to the performance of the protocol.)

For each of these error models, we estimate the logical error rate  for generating a cluster state on an L×L×L bcc lattice (storing one logical qubit) using Protocol B, for various values of L and η. As in the section on thresholds, we infer the effect that each physical error has on the final state using Table 2 and Eq. (9), and we use the generalized MWPM decoder of Ref. [28] (without accounting for degeneracies) in our simulations. The results are shown in FIGS. 12A, 12B. In particular, FIG. 12A is a plot of the logical error rate  vs. ηZ for Error Model 3a (applied to Protocol B). FIG. 12A is a plot of the logical error rate  vs. ηloss for Error Model 3b applied to Protocol B. Each data point is an average of at least 106 independent instances and at least 104 logical errors.

For an L×L×L bcc lattice, the total number of delay line time steps is L2. Hence, as we increase L for a fixed delay line error rate q, there is a tradeoff between the better error suppression due to larger code distance, given by d=(L+1)/2, and the larger cumulative delay line error. Therefore, for each q, there is an optimal value L* of L that minimises the logical error rate . We find the minimum logical error rate, which we denote by *, by increasing L until  starts to increase.

While we do not have an analytic expression for L*, we can make an educated guess as to the scaling of * as a function of η. Since the circuit error rate p=10−3 in our models is well below threshold, there should be a threshold pdelay,th for the cumulative delay line error below which the logical error rate  decays exponentially with L. For small η, the cumulative error is ηL2 to leading order, so  decays exponentially with L for ηL2pdelay,th. In particular, provided that ηL*2pdelay,th, which can be achieved by L*=c(pdelay,th/η)1/2 for some constant c, we expect * to roughly scale as

ln(1/*)≈c′η−1/2+c″,  (17)

where c′ and c″ are constants.

Numerically, we observe excellent agreement with Eq. (17), as can be seen from FIGS. 13A, 13B. Fitting Eq. (17) to the data gives the following estimates for c′ and c″:

Error Model 3a: c′≈0.032, c″≈2.93

Error Model 3b: c′≈0.096, c″≈3.37  (18)

FIG. 13A is a plot of ln(1/*) vs. ηZ−1/2 for Error Model 3a (applied to Protocol B). FIG. 13B is a plot of ln(1/*) vs. ηloss−1/2 for Error Model 3b. Solid lines are fits to Eq. (17). The different stars indicate the value L* of L that achieves the minimum logical error rate *.

From Eq. (18), we can determine the “break-even point” beyond which it is advantageous to use the delay lines. That is, since the depolarizing noise rate is assumed to be p=10−3, using the experimental setup described in the experimental realization section would make sense only when the logical error rate p is below this value. If the delay line error is dominated by dephasing, the break-even point occurs at ηZ=6.5×10−5. If the delay line error is dominated by loss, the break-even point occurs at ηloss=7.4×10−4.

As discussed in the following section, current experimental estimates for delay line error rates are not below this break-even point. However, the above results show that small reductions in these error rates can lead to very large reductions in the logical error rate. As an example, consider Error Model 3b, in which delay line errors are dominated by qubit loss. For circuit error rates as high as 10−3, Eqs. (17) and (18) give logical error rates *=10−5, 10−10, 10−15 for ηloss≈1.4×10−4, 2.4×10−5, 9.5×10−6, respectively. Assuming that L*∝ηloss−1/2 as above, the values of L required can be estimated to be L*≈30, 75, 115, respectively. Thus, even if the circuit error rate is relatively high, with continued improvements in the error rates and storage capacities of delay lines, extremely low logical error rates can potentially be achieved using our protocol.

### Experimental Prospects

Three different experimental platforms are particularly appealing for physical implementations of the techniques discussed herein: 1) a system of optical photons in a waveguide coupled to an atom or an artificial atom, 2) an integrated superconducting circuit in which single microwave photons can be deterministically generated via a superconducting qubit, 3) a quantum acoustic system based on fabricated nanostructures coupled to a nonlinear quantum emitter, e.g., a transmon qubit piezoelectrically coupled to a phononic waveguide.

In the optical domain, commercially available optical fibers can provide excellent delay times, in principle allowing for an extremely large number of photons in the delay lines. For instance, Tamura et al. reported a loss rate of 1.4×10−4 dB/m [25]. Assuming that a single time step lasts 50 ns, we obtain a loss rate of 1.4×10−3 dB per time step, which amounts to ηloss≈9.6×10−4. This is close to the break-even point 7.4×10−4 estimated above.

However, weak coupling strengths between a quantum emitter and relevant photon modes can be a limitation of this approach. In particular, the cooperativity  is the ratio between the probabilities that  emits a photon into a guided mode versus into unwanted modes. In order to obtain logical error suppression,  needs to be sufficiently large, such that the total loss probability is below the loss thresholds found in the section on thresholds. Thus, it is important to achieve a high cooperativity, e.g., 100. Reducing photon loss at the interfaces of different optical elements and improving the qubit coherence time (in the case of quantum dots) is also important.

In microwave photonics with integrated superconducting circuits, a significantly higher cooperativity ≈172 has been achieved [59]. In fact, more recently, coherent interactions between a quantum emitter and a single time-delayed photon that has propagated through a waveguide have been demonstrated experimentally [60]. In Ref. [60], an array of microwave resonators is used to realize a one-dimensional waveguide with delay time ≈227 ns. The waveguide is coupled to a qubit with photon emission rate Γ1D2π×21 MHz. This capability implies that around Γ1D≈30 propagating photons can be stored inside the waveguide. Thus, integrated superconducting circuits are also a physical platform to implement our protocols.

Finally, quantum acoustic systems with phononic crystals are also rapidly emerging, and provide a physical platform for our scheme. A single-mode phononic waveguide [26] and an extremely long phonon lifetime (T1≈1.5 s and T20.3 ms) [55] have already been demonstrated in two separate experiments. Providing a strong coupling regime with a high cooperativity by fabricating integrated nanostructures (similar to superconducting circuits [59]), quantum acoustic systems can realize our protocols for reasonably large system sizes. For example, with optimistic but reasonable estimates T2≈1 ms and γ≈100 MHz, where γ is the coupling strength, one can choose a pulse-to-pulse time separation ≈160 ns to realize high-fidelity gates with error rates below our threshold of pth≈0.39%. (Here, we assumed that the gate fidelity scales as 1−1/(γ)2 based on symmetric wavepackets of phonons [20].) This choice of  would lead to a delay line error rate per time step of ηZ≈3/T2≈4.8×10−4. (Note: The logical error rates achievable for other values of /T2 are tabulated in Table 3.) Although this is above the break-even point 6.5×10−5, we note that the experimental technology for quantum acoustic systems is in its early stages and advancing rapidly. Through improving fabrication methods for integrated circuits and lowering the temperature, the coherence times of both qubits and a delay lines may be substantially increased.

### Discussion

We have described a method for preparing the three-dimensional cluster state of Ref. [14] using a simple device. The main advantage of our technique is that it has low component overhead, meaning that we only need a handful of experimental components to build a well-protected logical qubit. In contrast, standard protocols based on three-dimensional cluster states or the surface code [22, 16, 15, 11, 61] are expected to require hundreds if not thousands of experimental components.

If memory errors are non-negligible, our protocols do not have finite thresholds for the circuit error rate. Nevertheless, the logical error rate can be made exponentially

small in η−1/2, where η represents the memory error rate. Although our estimates suggest that the error rates that have been attained experimentally are not yet small enough, the low component overhead of our approach means that improvements in only a few physical components can lead to extremely large reductions in the logical error rate.

While the most mature approaches to quantum computation have high component overhead, ours is not the first proposal aiming to reduce component overhead.

For example, the promise of anyon-based quantum computation in topological materials [30, 36, 38] is that natural physical interactions would greatly reduce the component overhead. Likewise, the reader may wonder how our scheme fares in comparison to those based on the Gottesman-Kitaev-Preskill (GKP) code [62]. This quantum error-correcting code for a qubit in an oscillator was recently used to demonstrate error suppression [63] by coupling cavity modes that form a GKP code to a transmon. For the protocol used, the logical error rate is determined by (i) a number that decays exponentially with σ−2, where a is the standard deviation of the Gaussian displacement channel [64] modeling the dominant source of error on the modes, and (ii) the transmon error rate p. The dominant source of error in Ref. [63] limiting the logical error rate is (ii), leading to a logical error rate that is significantly higher than what (i) might naïvely suggest. The contribution from (ii) can be reduced to O(p2) by using a recently proposed fault-tolerant method for preparing GKP states [65], in which case we expect the logical error rate to be limited by O(p2).

In contrast, in an analogous setting, the logical error rate of our protocols decays exponentially with η−1/2, even if the transmon error rate is significantly higher. Specifically, it suffices for the transmon error rate to be lower than some threshold value, which we have estimated to be 0.39% in the standard depolarizing noise model for circuit errors. Therefore, while approaches based on the GKP code may seem advantageous at the moment, with improved gate fidelities our scheme may be able to outperform them in the future.

From a more theoretical perspective, our protocols have a remarkable fault-tolerance property. Even though there is one physical qubit that interacts with every other qubit during the preparation of the cluster state, the procedure is nonetheless fault-tolerant because any single-qubit circuit-level error results in a constant-weight error on the final state. What is interesting about this phenomenon is that the propagated error may actually be highly nonlocal, yet its effect on the specific state we wish to prepare is always the same as that of a geometrically local error. Similarly, the effect of any m-qubit circuit-level error on the final state is equivalent to that of at most m geometrically local errors. In fact, this applies not only to our protocols (Protocols A and B) for preparing the specific cluster state of Ref. [14], but to our general algorithm (Algorithm 1), which can be used to prepare the cluster state corresponding to any graph. (For general cluster states, geometric locality is defined with respect to the underlying graph; see the section below on error analysis for arbitrary graphs.)

By leveraging this fact, we were able to construct fault-tolerant quantum circuits whose depth necessarily scales with the total number of qubits. This is certainly unusual. Fault-tolerant quantum computing protocols usually avoid circuits structured like ours because of the danger that they will spread errors too widely. This often restricts the design of these protocols, leading them to rely on a small number of trusted and manifestly fault-tolerant building blocks, such as transversal gates or “catch-and-correct” [66]. Our work shows that there can be a subtle form of fault-tolerance in which physical errors spread but without adverse effects. This observation may prove useful for generalizing our methods to other fault-tolerance schemes. Indeed, Algorithm 1 can immediately be used to generate cluster states obtained by foliating arbitrary stabilizer codes [29, 67]. The fault-tolerance of the resulting protocols can be analyzed with the help of Table 4 in the section on error analysis for Algorithm 1.

There are several variations an alternate instantiations of the above that we envision. For one, the decoder we used in our simulations was the most basic MWPM decoder, which did not take into account matching degeneracies nor the anisotropy of the underlying error model. Thus, we envision the option of using decoders that exploit additional information to obtain better logical error rates and thresholds. Also, leveraging recent work on using so-called flag techniques to make error-correction schemes more efficient [68, 66, 69, 70], it is envisioned to use such techniques to improve our protocols as well. More generally, it could be advantageous to trade a slowly growing component overhead for improved error tolerance. For instance, one could adapt our protocols to build cluster states on an L×L×N lattice using O(L) emitters instead of the single emitter discussed here. Such a scheme would still have component overhead parametrically smaller than the O(L2) physical qubits live in the system. An analogous trade-off was found in [71] between the number of emitters and the entanglement generation rate in the context of quantum communication using cluster states [72, 73]. Another strategy would be to concatenate our scheme, replacing our bare single- or dual-rail qubits with qubits protected by error correction, using e.g., GKP [62] or binomial codes [74]. Conversely, our scheme could be used as the inner code, choosing a small value of L (e.g., 10 or less) to make the logical error rate sufficiently small, e.g., 10−5. We can then concatenate this with a lower-overhead outer code, which may have a low pseudo-threshold.

### Alternative Algorithm

In this section, we present an alternative algorithm, Algorithm 2, for preparing cluster states |ψG (see Eq. (1)) on arbitrary graphs G. Algorithm 2 is similar in structure to Algorithm 1. The main difference is that unlike Algorithm 1, Algorithm 2 does not require any intermediate measurements of the ancilla  for any G.

To understand the form of Algorithm 2, recall the definition of the graphs G[k]′ from Eq. (4). For each k∈[n], G[k]′ consists of the subgraph of G induced by the vertices [k] together with an additional vertex, , and an additional edge, (,k). The cluster state |ψG[k]′ is defined by Eq. (1). In the section below on correctness of Algorithm 2, we prove that for any k∈[n], |ψG[k]′ is equivalently given by

\(\begin{matrix}
{\left. {\left. {\left. {❘\psi_{{G\lbrack k\rbrack}^{\prime}}} \right\rangle = {\left\lbrack {\prod\limits_{j = 1}^{k}\left( {H_{Q}X_{Q,j}Z_{Q,{j - 1}}{\prod\limits_{{i:{({i,j})}} \in {E\lbrack j\rbrack}}Z_{Q,i}}} \right)} \right\rbrack{❘ +}}} \right\rangle_{Q}\underset{i^{\prime} = 1}{\overset{k}{\otimes}}{❘0}} \right\rangle_{i^{\prime}},} & (19)
\end{matrix}\)

where E[k]:={(i,j)∈E: i,j∈[k]}. Therefore, taking k=n in Eq. (19) yields a circuit that recursively generates |ψG[n]′, as described in the main loop of Algorithm 2. Once we have prepared |ψG[n]′, the target cluster state |ψG can then be obtained by applying  (or by measuring  in the Z-basis).

Observe that if for a given j, if (j−1, j) is an edge (Line 4 of Algorithm 2), then

\(\begin{matrix}
{{{Z_{Q,{j - 1}}{\prod\limits_{{i:{({i,j})}} \in {E\lbrack j\rbrack}}Z_{Q,i}}} = {\prod\limits_{\substack{i \neq {j - 1} \\ {({i,j})} \in {E\lbrack j\rbrack}}}Z_{Q,i}}},} & (20)
\end{matrix}\)

so we do not apply  at all (instead of applying it twice in succession).

Algorithm 2 correctly prepares |ψG for any ordering of the qubits, which is implicitly chosen by labelling the vertices in V from 1 to n. The proof of correctness is given in the section below on correctness of Algorithm 2.

**Correctness**

In this section, we prove that Algorithms 1 and 2 correctly prepare cluster states |ψG on arbitrary graphs G=(V,E). We begin with Algorithm 2.

**Correctness of Algorithm 2**

The correctness of Algorithm 2 follows immediately from Eq. (19), which we now prove. For any graph G, the cluster state |ψG[k]′ corresponding to G[k]′ is, by definition (see Eqs. (1) and (4)),

\(\begin{matrix}
{\left. {\left. {❘\psi_{{G\lbrack k\rbrack}^{\prime}}} \right\rangle = {{Z_{Q,k}\left\lbrack {\prod\limits_{{({i,j})} \in {E\lbrack k\rbrack}}Z_{i,j}} \right\rbrack}{\underset{i^{\prime} = 1}{\overset{k}{\otimes}}{❘ +}}}} \right\rangle_{i^{\prime}}.} & (21)
\end{matrix}\)

First, we prove by induction that

\(\begin{matrix}
{\left. {\left. {❘\psi_{{G\lbrack k\rbrack}^{\prime}}} \right\rangle = {\left\lbrack {\prod\limits_{j = 1}^{k}A_{{DD}_{j}}} \right\rbrack{\underset{i = 1}{\overset{k}{\otimes}}{❘ +}}}} \right\rangle_{i},} & (22)
\end{matrix}\)
\(where\)
\(\begin{matrix}
{A_{{DD}_{j}}:{Z_{Q,j}Z_{Q,{j - 1}}{\prod\limits_{{i:{({i,j})}} \in {E\lbrack j\rbrack}}.}}} & (23)
\end{matrix}\)

Here, Sa,b denotes the Sgate between qubits a and b. For the base case k=1, =I and E[k]=ø, so

\(\begin{matrix}
\left. {\left. {\left. {\left. {A_{{DD}_{1}}{❘ +}} \right\rangle_{Q}{❘ +}} \right\rangle_{1} = {Z_{Q,1}S_{{WAP}_{Q,1}}{❘ +}}} \right\rangle_{Q}{❘ +}} \right\rangle_{1} \\
\left. {\left. {= {Z_{Q,1}{❘ +}}} \right\rangle_{Q}{❘ +}} \right\rangle_{q} \\
\left. {= {❘\psi_{{G\lbrack 1\rbrack}^{\prime}}}} \right\rangle
\end{matrix}\)

since G[1]′ contains only the edge {Q, 1}. Assume that Eq. (22) holds for k−1. Then,

\(\begin{matrix}
\left. {\left. {\left. {\left\lbrack {\prod\limits_{j = 1}^{k}A_{{DD}_{j}}} \right\rbrack{\underset{i = 1}{\overset{k}{\otimes}}{❘ +}}} \right\rangle_{i} = {A_{{DD}_{k}}{❘\psi_{{G\lbrack{k - 1}\rbrack}^{\prime}}}}} \right\rangle{❘ +}} \right\rangle_{k} \\
{= {\left\lbrack \prod\limits_{{l:{({l,k})}} \in {E\lbrack k\rbrack}} \right\rbrack \cdot}} \\
\left. {\left. \left. {}\left\lbrack {\left( {\prod\limits_{{({i,j})} \in {E\lbrack{k - 1}\rbrack}}Z_{i,j}} \right){\underset{i^{\prime} = 1}{\overset{k - 1}{\otimes}}{❘ +}}} \right. \right\rangle_{i^{\prime}} \right\rbrack{❘ +}} \right\rangle_{k} \\
{= {{Z_{Q,k}\left\lbrack {\prod\limits_{{l:{({l,k})}} \in {E\lbrack k\rbrack}}Z_{k,l}} \right\rbrack}\left\lbrack {\prod\limits_{{({i,j})} \in {E\lbrack{k - 1}\rbrack}}Z_{i,j}} \right\rbrack}} \\
\left. {}{\underset{i^{\prime} = 1}{\overset{k}{\otimes}}{❘ +}} \right\rangle_{i^{\prime}} \\
\left. {= {{Z_{Q,k}\left\lbrack {\prod\limits_{{({i,j})} \in {E\lbrack k\rbrack}}Z_{i,j}} \right\rbrack}{\underset{i^{\prime} = 1}{\overset{k}{\otimes}}{❘ +}}}} \right\rangle_{i^{\prime}} \\
\left. {= {❘\psi_{{G\lbrack k\rbrack}^{\prime}}}} \right\rangle
\end{matrix},\)

where third equality uses the identity =Zk,lS for l≠k, and the fourth equality follows from the fact that E[k]=E[k−1]∪{(l,k)∈E[k]} (see Eq. (3)).

Next, we observe from Eqs. (23) and (22) that for every j∈[n], when  is applied to  and j the qubit j is in the fixed initial state |+. This implies that we do not need to implement a Sgate that works correctly on arbitrary states.

We can instead use an operation that has the same effect when one of the qubits is in the state |+. (Of course, if the Sgate were experimentally available, this transformation would be unnecessary. We were primarily motivated to replace the gates in Eq. (22) by ones that are more amenable to experimental implementation in the setup considered in the experimental realization section.) In particular, we use the identity

Sj=|0j,  (24)

for any arbitrary state | of  (potentially entangled with other qubits).

Substituting Eq. (24) into Eq. (22), we arrive at Eq. (19), which forms the basis for Algorithm 2.

**Correctness of Algorithm 1**

To prove the correctness of Algorithm 1, we show by induction that for every k∈[n], after Line 4 in the kth iteration of the for loop has been executed, the state of  and the first k data qubits is |ψG[k]′ (see Eq. (21)).

For the base case k=1, E[1]=ø so in Line 4, HX, 1 is applied to  and qubit 1, which are in their initial states |+ and |0, respectively. By Eq. (19) with k=1, this yields the state

|01=|ψG[1]′.

For the inductive step, there are two cases to consider, (k−1,k)∈E and (k−1,k)∉E. For both cases, it will be useful to observe from Eq. (19) that for any 1<k≤n,

\(\begin{matrix}
{\left. {\left. {\left. {❘\psi_{{G\lbrack k\rbrack}^{\prime}}} \right\rangle = {\left\lbrack {H_{Q}X_{Q,k}Z_{Q,{k - 1}}{\prod\limits_{{i:{({i,k})}} \in {E\lbrack k\rbrack}}Z_{Q,i}}} \right\rbrack{❘\psi_{{G\lbrack{k - 1}\rbrack}^{\prime}}}}} \right\rangle{❘0}} \right\rangle_{k}.} & (25)
\end{matrix}\)

Also note from the definition of E[j] in Eq. (3) that the controlled-Z gates applied in Line 4 can be equivalently written as

\({\prod\limits_{\substack{i < {j - 1} \\ {({i,j})} \in E}}Z_{Q,i}} = {\prod\limits_{\substack{i \neq {j - 1} \\ {({i,j})} \in {E\lbrack j\rbrack}}}{Z_{Q,i}.}}\)

In the first case (k−1,k)∈E, Lines 5-9 in the (k−1)th iteration are skipped, so by the inductive hypothesis, the state at the start of the kth iteration is |ψG[k−1]′. Then, Lines 3 and 4 in the kth iteration produce the state

\(\left. {\left. {\left. {\left\lbrack {H_{Q}X_{Q,k}{\prod\limits_{\substack{i \neq {k - 1} \\ {({i,k})} \in {E\lbrack k\rbrack}}}Z_{Q,i}}} \right\rbrack{❘\psi_{{G\lbrack{k - 1}\rbrack}^{\prime}}}} \right\rangle{❘0}} \right\rangle_{k} = {❘\psi_{{G\lbrack k\rbrack}^{\prime}}}} \right\rangle.\)

This follows from Eq. (25), noting that Eq. (20) holds since (k−1,k)∈E.

In the second case (k−1,k)∉E, the if condition of Line 5 is satisfied and  is measured in the Z-basis. By the inductive hypothesis,  and the first k−1 data qubits are in the state |ψG[k−1]′ immediately before this measurement. By Eqs. (2) and (4), the stabilizers of |ψG[k−1]′ are generated by {Zk−1}∪{Si: i∈[k−1]}, where

\(S_{i} = \left\{ {\begin{matrix}
{X_{i}{\prod\limits_{{j:{({i,j})}} \in {E\lbrack{k - 1}\rbrack}}Z_{j}}} & {i < {k - 1}} \\
{X_{k - 1}Z_{Q}{\prod\limits_{{j:{({j,{k - 1}})}} \in {E\lbrack{k - 1}\rbrack}}Z_{j}}} & {i = {k - 1}}
\end{matrix}.} \right.\)

Hence, the stabilizer generators of post-measurement state of the first k−1 data qubits are {Si′: i∈[k−1]}, where Si′=Si for i<k−1 and

\(S_{k - 1}^{\prime} = {{\pm X_{k - 1}}{\prod\limits_{{j:{({j,{k - 1}})}} \in {E\lbrack{k - 1}\rbrack}}{Z_{j}.}}}\)

Here, the + sign corresponds to the post-measurement state of  being |0, and the − sign to |1. If the outcome is |1, Line 8 applies Zk−1, which negates Sk−1′ and leaves the other stabilizer generators unchanged. Thus, the state of  (which is reinitialized in |+ by Line 9) and the first k−1 data qubits at the end of the (k−1)th iteration is the cluster state

{ {[} ∏ ( i , j ) ∈ E {[} k - 1 {]} Z i , j {]} ⁢ ❘
"\textbackslash{[}LeftBracketingBar{]}" + ⊗ i ′ = 1 k - 1 ❘
"\textbackslash{[}LeftBracketingBar{]}" + 〉 i ′ = - 1 ❘
"\textbackslash{[}LeftBracketingBar{]}" ψ G {[} k - 1 {]} ′ 〉 . ( 26 )
}

Applying Lines 3 and 4 in the kth iteration then leads to the state

{ {[} ∏ i ≠ k - 1 ( i , k ) ∈ E {[} k {]} {]} - 1 ❘
"\textbackslash{[}LeftBracketingBar{]}" ψ G {[} k - 1 {]} ′ 〉 ⁢ ❘
"\textbackslash{[}LeftBracketingBar{]}" 0 〉 k = ❘
"\textbackslash{[}LeftBracketingBar{]}" ψ G {[} k {]} ′ 〉 ⁢ by . Eq . (
25 ) }

In both cases, therefore, the state of  and the first k data qubits is |ψG[k]′ at the end of Line 4 of the kth iteration, as claimed. In particular, in the nth iteration, the state is |ψG[k]′ at the end of Line 4. G[n]′ differs from G by an extra edge {(Q,n)}, so by measuring  in the Z-basis and applying Z, if necessary in Lines 6-8, we obtain the desired state |ψG.

**Error Analysis for Arbitrary Graphs**

In this section, we analyze how errors propagate through Algorithms 1 and 2, both of which can be used to prepare cluster states |ψG defined by arbitrary graphs G=(V,E). We show that for any G, any single-qubit error occurring during either algorithm results in an effective error (see Eq. (8)) whose weight scales with the maximum degree of G. For Algorithm 1 and for certain instances of Algorithm 2, the effective error resulting from a single-qubit error is always geometrically local, meaning that it is supported on some subset of {i}∪N(i) for some qubit i∈V, where

N(i):={j:(i,j)∈E}  (27)

denotes the nearest neighbors of i in the graph G. (In the context of quantum error correction, the notion of geometric locality often applies only to graphs that can be embedded into finite-dimensional space. The definition we use here extends to arbitrary graphs, including e.g., expander graphs.)

An important feature of both algorithms—and one of the main intuitions behind the proof below—is that at any point in the procedure, the ancilla qubit  is entangled with a restricted number of data qubits (depending on the maximum degree of G). Moreover, all or almost all of the qubits with which  is entangled at a given point are close to each other in G. As a result, even though  interacts at least once with every data qubit in V, most (and in some cases, all) of the errors that could occur on  lead to effective errors on the final state that are localised to neighborhoods of G.

**Error Analysis for Algorithm 1**

In this section, we prove that for any input graph, single-qubit errors occurring during Algorithm 1 induce geometrically local effective errors.

Claim 1. Consider an arbitrary graph G=(V,E), and choose any ordering of the qubits in Algorithm 1 by labelling the vertices in V from 1 to n. Then, any single-qubit error occurring between the elementary operations in Algorithm 1 results in effective error (see Eq. (8)) that is supported on some (possibly empty) subset of {i}∪N(i) for some i∈[n].

Proof. For each j∈[n], let

\(\begin{matrix}
{\mathcal{B}_{j}:={H_{Q}X_{Q,j}{\prod\limits_{\substack{i < {j - 1} \\ {({i,j})} \in E}}Z_{Q,i}}}} & (28)
\end{matrix}\)

denote the block of gates applied in the jth iteration of the for loop in Algorithm 1 (Line 4). We consider the effect of all possible X and Z errors that could occur during Algorithm 1. (The support of arbitrary errors can then be deduced using Eq. (9).) Spatially, these errors may inflict the ancilla  or one of the data qubits 1, . . . , n, and temporally, they may occur between two blocks j and j+1, before the first block 1, after the last block n, or between two elementary gates in the same block. We do not consider where the errors occur relative to the Zj corrections that may be applied for certain j (Line 8), as a Pauli error P immediately before Zj is equivalent to P immediately after Zj up to a sign. (Note: Recall that if (j,j+1)∉E,  is also measured in the Z-basis and reset to |+ (Lines 6 and 9) in the jth iteration, between i and j+1. In this case, we consider errors (on ) both before the measurement (i.e., immediately after j) and after the re-initialization (i.e., immediately before j+1).)

**Zi Errors**

Suppose that a Z error occurs on a data qubit i∈[n]. Clearly, Zi commutes with every operation in Algorithm 1 except for the ,i gate in Bi. This ,i gate is the first gate that acts on qubit i, which is initially in the state |0. Therefore, if the Zi error occurs somewhere before the ,i, it has no effect, whereas if it occurs after the ,i, it is equivalent to a Zi error on the final state.

X Errors

We first show that an X error occurring immediately after k results in an effective error Zk on the final state, in the sense of Eq. (8). This is a consequence of the fact (proven in the section below on the correctness of Algorithm 1) that immediately after k has been applied,  and the first k data qubits are in the cluster state |ψG[k]′ (and the rest of the qubits are still in their initial state, |0⊗n−k). Recall from Eq. (4) that G[k]′ is the graph with vertices [k]∪ and edges E[k]∪{(,k)}. Importantly, k is the only qubit that shares an edge with  in G[k]′, so it follows from Eq. (2) that XZk is a stabilizer of |ψG[k]′, which implies

X|ψG[k]′=Zk|ψG[k]′.  (29)

Hence, an X error immediately after k is equivalent to a Zk error immediately after k, and we know from above that the latter results in a Zk error on the final state.

Trivially, an X error occurring at the beginning of the circuit, i.e., before 1, has no effect since the initial state |+ of  is stabilised by X. The same goes for X errors that occur immediately after the re-initialization of  (to |+) in the iterations where  is measured.

It remains to consider X errors that occur between two consecutive gates in the same block k. Suppose that an  error occurs somewhere in k before the ,k gate. At this point, the first k−1 iterations of the for loop have been performed, followed by some subset of the controlled-Z gates in k. To be precise, let J denote the subset of qubits j for which  is in k and is located before the X error. From Eq. (28), we have

J⊆C{j<k−1:(j,k)∈E}.  (30)

The qubits that are included in J depend on the location of the X error as well as on the order in which the controlled-Z gates in k are actually applied (since they mutually commute, they can be applied in any order).

As shown in the section below on the correctness of Algorithm 1, the state of the first k−1 qubits at the end of the (k−1)th iteration is |ψG[k−1]′ if (k−1,k)∈E, or Z,k−1|ψG[k−1]′ if (k−1,k)∉E (see Eq. (26)). Consider the case (k−1,k)∈E. The state of the first k−1 qubits at the point where the X error occurs is then [Πj∈JZ,j]|ψG[k−1]′. This state is a cluster state in which shares an edge with k−1 (see Eq. (4)) and with every j∈J, and is therefore stabilised by XZk−1Πj∈JZj. It follows that the X error is equivalent to Zk−1Πj∈JZj, which commutes with all subsequent operations in the circuit. The effective error on the final state is therefore Zk−1Πj∈JZj. Similarly, in the case (k−1,k)∉E, the state at the point where the X error occurs is [Πj∈JZ,j]Z,k−1|ψG[k−1]′. This is stabilised by XΠj∈JZj, so by the same argument, the X error results in an effective error Πj∈JZj.

The only other possibility is that an X error occurs after the X,k and before the  in k. Since HaXa=ZaHa, this is equivalent to a Z error occurring after the , i.e., immediately after k. As shown directly below, such an error results in a Zk+1 error on the final state if (k,k+1)∈E, and no error if (k,k+1)∉E.

Z Errors

The identities Za,bZa=ZaZa,b and HaZa=XaHa imply that a Z error occurring immediately before k or within k (i.e., between any two of the gates in k) is equivalent to an X error immediately after k, which in turn results in a Zk error on the final state (see Eq. (29)).

A  error could also occur immediately after k. If (k,k+1)∈E, this is equivalent to a  error immediately before k+1, and therefore results in a Zk+1 error on the final state. On the other hand, if (k,k+1)∉E,  is measured in the Z-basis before k+1 is applied. In this case, the  error has no effect since it directly precedes a Z-measurement.

**Xi Errors**

Finally, consider the effect of Xi errors. The only gates in Algorithm 1 (besides the Zj corrections) with which Xi does not commute are the Z,i. From Eq. (28), we see that a Z,i gate appears in block j for every j>i+1 such that (i,j)∈E. Hence, for each i∈[n], define the index set

Ii:={j>i+1:(i,j)∈E}  (31)

so that j includes a Z,i gate iff j∈Ii.

Suppose that an Xi error occurs before k (but after k−1) for some k. It can be checked using the identities Za,bXb=XbZaZa,b and HaXa=ZaHa that this is equivalent to an Xi error at the end of the circuit, along with an X error immediately after each block j for all j∈Ii such that j≥k. As proven above, X immediately after j results in an effective error Zj on the final state. Therefore, it follows from Eq. (9) that an Xi occurring immediately after k results in an effective error on the final state, up to a sign.

\(X_{i}{\prod}_{j \in {{I_{i}:j} \geq k}}Z_{j}\)

These results are summarized in Table 4. Note that the effect of any circuit-level Z error is at worst a single-qubit Z error, while the effective error resulting from any X error is (equivalent under stabilizers to) a product of Z errors supported within N(i). It can be verified using Table 4 that X and Z errors occurring at the same spacetime location in the circuit result in effective errors supported within {i}∪N(i) for the same i. This implies via Eq. (9) that any single-qubit error at that location leads to an effective error supported within {i}∪N(i), as claimed.

Tables 1 and 2, which are used in our simulations in the section on thresholds and the analysis section above, are both special cases of Table 4. Specifically, Table 4 reduces to Table 1 (which corresponds to the first step of Protocol A) for G=Gc

and j=Aj (see Eq. (10)), and to Table 2 (which corresponds to Protocol B) for G=Gbcc and j=Bj (see Eq. (11)).

We remark that unlike Algorithm 1, not all cluster state preparation circuits have the property that any single-qubit circuit-level error results in a geometrically local effective error. For instance, Algorithm 2 can likewise be used to generate |ψG for any graph G=(V,E). However, as discussed in the following section, there exist single-qubit errors in Algorithm 2 that lead to nonlocal effective errors unless the n qubits are ordered such that (i,i+1)∈E for every i∈[n−1]. (More precisely, since multiple operators fit the definition of an effective error resulting from a particular circuit-level error (see Eq. (8)), none of the effective errors corresponding to these single-qubit circuit-level errors are geometrically local.) It follows that for any graph that does not contain a Hamiltonian path, Algorithm 2 does not yield for any possible ordering of the qubits a preparation circuit for which the effective errors are all geometrically local. As another example, certain single-qubit errors occurring in the circuit given by Equation 2 of Ref. [20], which prepares a two-dimensional cluster state, would lead to nonlocal errors. This results from the inclusion of several redundant controlled-Z gates. (It should be noted, however, that the experimental protocol proposed in Ref. [20] does not actually apply these redundant gates.) More generally, by adding redundant controlled-Z gates, it is in fact possible to construct circuits in which certain single-qubit errors induce effective errors whose weights necessarily scale with the number of qubits.

**Error Analysis for Algorithm 2**

A similar result holds for Algorithm 2. However, in contrast to Algorithm 1, the effective errors resulting from single-qubit errors occurring during Algorithm 2 are not all geometrically local for every instance.

Claim 2. Consider an arbitrary graph G=(V,E), and choose any ordering of the qubits in Algorithm 2 by labelling the vertices in V from 1 to n. Then, any single-qubit error occurring between the elementary gates in Algorithm 2 results in an effective error (see Eq. (8)) that is supported on some (possibly empty) subset of {i}∪N(i)∪{i±1}, for some i∈[n].

Specifically, Table 5 gives the effect of all possible single-qubit X and Z errors that could occur during Algorithm 2. In this table, j is used to denote the jth block

of gates applied in Algorithm 2:

{ B \textasciitilde{} j := \{ ∏ i ≠ j - 1 ( i , j ) ∈ E {[} j {]} , i (
i , i + 1 ) ∈ E , j - 1 ∏ i : ( i , j ) ∈ E {[} j {]} Z Q , i ( i , i +
1 ) ∉ E . ( 32 ) }

The proof of Claim 2 is essentially the same as that of Claim 1, requiring only the following modifications. First, there are no intermediate measurements of  in Algorithm 2, so unlike for Algorithm 1 there is no need to consider errors occurring before a measurement or after a re-initialization of . Second, the index sets J and Ii (see Eqs. (30) and (31)) considered in the proof of Claim 1 are slightly different for Claim 2. Specifically, Ii should be replaced by its analogue Ĩi, defined as

\(\begin{matrix}
{{\overset{\sim}{I}}_{i}:=\left\{ {\begin{matrix}
\left\{ {{j > {i + {1:\left( {i,j} \right)}}} \in E} \right\} & {\left( {i,{i + 1}} \right) \in E} \\
{\left\{ {i + 1} \right\}\bigcup\left\{ {{j > {i:\left( {i,j} \right)}} \in E} \right\}} & {\left( {i,{i + 1}} \right) \notin E}
\end{matrix},} \right.} & (33)
\end{matrix}\)

so that the gate block j includes a ,i gate iff j∈Ĩi, as can be seen from Eq. (32). (Note that in contrast to Ii, which is always contained within the nearest neighbors N(i) of i, Ĩi may contain i+1 even if (i,i+1)∉E.) Similarly, if {tilde over (J)} is a subset of the controlled-Z gates in k, it follows from Eq. (32) that

\(\begin{matrix}
{\overset{\sim}{J} \subseteq \left\{ {\begin{matrix}
\left\{ {{j < {k - {1:\left( {j,k} \right)}}} \in E} \right\} & {\left( {{k - 1},k} \right) \in E} \\
{\left\{ {k - 1} \right\}\bigcup\left\{ {{j < {k:\left( {j,k} \right)}} \in E} \right\}} & {\left( {{k - 1},k} \right) \notin E}
\end{matrix}.} \right.} & (34)
\end{matrix}\)

It can then be verified using Table 5 (in conjunction with Eq. (9)) that any single-qubit error occurring in Algorithm 1 results in an effective error supported within {i}∪N(i)∪{i±1}. These effective errors are not geometrically local in general, as i−1 and i+1 are not necessarily nearest neighbors of i.

It is worth noting, however, that the effective errors would always be geometrically local if (i,i+1)∈E for all i∈[n−1]. This is possible iff


- - 1) the underlying graph G of the target cluster state contains a
    Hamiltonian path, and
  - 2) we use the ordering of the vertices along the Hamiltonian path as
    the ordering of qubits in Algorithm 2. (Recall that different
    orderings of the qubits in Algorithm 2 give rise to different
    circuits for preparing the same state.)  
    For instance, the cubic lattice G_(c) prepared in Protocol A
    contains a Hamiltonian path, and the vertices are ordered in Eq. (5)
    such that (i,i+1) is an edge for every i∈\[n−1\]. For G=G_(c),
    Algorithm 1 and Algorithm 2 reduce to the exact same circuit when we
    use this ordering of the vertices, and Table 1 shows that all of the
    effective errors are indeed geometrically local.

More generally, even if the graph G does not contain a Hamiltonian path, Claim 2 shows that every effective error has weight at most D(G)+3, where D(G) is the maximum degree of G, regardless of the ordering of vertices that we choose.

