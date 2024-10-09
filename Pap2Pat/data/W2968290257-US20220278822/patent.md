# DESCRIPTION

## TECHNICAL FIELD

Embodiments presented herein relate to a device, a method therein, a controller, a computer program, and a computer program product. Specifically, they relate to and are associated with the following technical areas/keywords: Advanced Encryption Standard, AES, SBox, hardware implementation, critical path.

## BACKGROUND

### Technical Background/Existing Technology

Advanced Encryption Standard (AES) is a cryptographic algorithm standardized by National Institute of Standards and Technologies (NIST), and it is one of the most widely used encryption algorithms today. It is used to secure web traffic in the TLS protocol, and also used in 3GPP LTE systems as one of the three air interface encryption methods.

Hardware implementations of AES are also very common, especially in high speed applications such as the LTE network, but also in Datacom the need for hardware accelerated crypto algorithms is essential for high load servers, terminating encrypted network traffic directly in the Network Interface Card (NIC), thereby reducing the load of the main CPU.

The AES encryption algorithm is described in detail in [1], but we will give a very brief introduction to it here. AES is a block cipher that takes two input variables; the plaintext (P) and the key (K), and produces a ciphertext (C) as output. The size of P and C determines the block size of the cipher, and in the case of AES this is 128 bits. So both P and C are of size 128 bits. The sized of the key K can be 128, 192, or 256 bits. The input P is divided into 16 bytes and arranged in a matrix form of 4×4 bytes, called the state matrix. The algorithm consists of a series of operation performed on the state matrix, scrambling the plaintext more and more into the final ciphertext output. The operations are grouped together in so called rounds. Each round in AES performs the following operations: SubBytes, ShiftRows, MixColumns, and AddRoundKey. Depending on the size of K, (128, 192, or 256 bits) the algorithm does 10, 12, or 14 of these rounds. For hardware implementations, the state matrix between each round is typically stored in some kind of registers (flip-flops, or latches). This means that the maximum clock speed by which we can clock the circuit, is determined by the speed by which the signal can move from one register to the next. The speed of a signal is mainly dependent on the number of gates the signal has to traverse between being stored in latches. The number of gates a signal traverses is usually called the depth of the signal, or the path depth. And the critical path for circuit is the longest path (most gates to traverse) for any of the constituent signals in the circuit.

For this disclosure the focus will be on the so called SBox, or substitution box of AES which is the fundamental building block of the SubBytes operation. It is also the operation that has the largest number of gates and the highest depth of the round function. Thus, it makes an interesting and valuable research goal to minimize the number of gates used to implement it, as well as the depth of this circuit. Minimizing the number of gates reduces the area and the power consumption of the circuit and, as explained before, minimizing the critical path increases the possible clock rate of the algorithm making the encryption/decryption faster.

Efficient hardware design of the AES SBox is a well-studied subject. If the absolute maximum speed is desired, a straightforward table-lookup implementation is most-likely used, which naturally leads to a large area.

In many practical situations the physical area of the cryptographic subsystem is limited, and the designer cannot afford to implement table-lookup for the SBoxes involved in an AES round, especially when implemented in an FPGA. For these situations, we need to study how to implement the AES SBox with logical gates only, focusing on both area and maximum clocking speed. The maximum clocking speed of a circuit is determined by the critical path or depth of the circuit; the worst case time it takes to get stable output signals from a change in input signals.

Another aspect when implementing AES is the need for the inverse cipher. Many modes of operation for a block cipher only use the encryption functionality and hence there is no need for the inverse cipher. In case you need both the forward and inverse SBox, it is often beneficial to combine the two circuits. This is because the main operation of the AES SBox is inverting a field element, which naturally is its own inverse, and it is expected that many gates of the two circuits can be shared.

FIG. 1 is a block diagram of an SBox circuit 101 that is advantageously used in an AES circuit for mapping an 8-bit input 103 to an 8-bit output 105.

At a circuit level, the SBox 101 defines 8 Boolean functions, each taking 8 bits as input. From a mathematical perspective, the forward AES SBox is defined as the composition of a non-linear function I(g) and an affine function A(g), such that SBox(g)=A(I(g)). The non-linear function I(g)=g−1 is the multiplicative inverse of an element g in the finite field GF (2{circumflex over ( )}8) defined by the irreducible polynomial x8+x4+x3+x+1. The circuit for building an inversion over GF(2{circumflex over ( )}8) is very large, and hence it is desirable to minimize it.

The first step towards a small area implementation was described by Rijmen [2]. The idea is that the inverse calculation in GF(28) can be reduced to a much simpler inverse calculation in the subfield GF(24) by doing a base change to GF((24)2).

In 2001, Satoh et al [3] took this idea further and reduced the inverse calculation to the subfield GF(22). This method is referred to as the Tower Field construction. In 2005, Canright [4] built on the work of Satoh et al and investigated the importance of the representation of the subfield, testing many different isomorphisms that led to the smallest area design. This construction is perhaps the most cited and used implementation of an area constraint combined AES SBox.

In a series of papers, Boyar, Peralta et al presented some very interesting ideas for both the subfield inverter as well as new heuristics for minimizing the area of logical circuits [8, 9, 10, 11]. They derived an inverter over GF(24) with depth 4 and a gate count of only 17. The construction in [10] is the starting point for this invention.

After Boyar, several other papers followed focusing on low depth implementations e.g., [5]. In 2018 two papers by Reyhani et al [12, 6] presented the best known implementation (up until now) of both the forward SBox as well as the combined SBox.

Comparing Results Theoretically

Firstly, the notations used herein are introduced. Gate names are written in capital letters GATE (examples: AND, OR). The notation mGATEn means m gates of type GATE, each of which has n inputs (example: XOR4, 8XOR4, NAND3, 2AND2). When the number of inputs n is missing then the assumption is that the gate has minimum inputs, usually only 2 (3 for MUX).

1. Standard Method

The basic cell elements that are considered in the standard method are: {XOR, XNOR, AND, NAND, OR, NOR, MUX, NMUX, NOT}.

Negotiation of NOT gates. In some places of the circuit there is a need to use the inverted version of a signal. There are, however, many ways to negotiate the need of using NOT gates. A few of them are listed here.

Method 1. One way to negotiate a NOT gate is to change the previous gate that generates that signal to produce an inverted signal, instead. For example, switch XOR into XNOR, AND into NAND, etc.

Method 2. In various technologies, some gates can produce both the straight signal and its inverted version. For example, XOR gates in many implementations produce both signals simultaneously, and thus the inverted value is available.

Method 3. It is possible to change the following gates after the inverted signal such that the following scheme would produce the correct result given the inverted input.

In view of the above, it is believed that NOT gates may be ignored while evaluating a circuit with the standard method; they can hardly be counted as a full gate in the standard method. However, for completeness, the number of NOT gates are included in the resulting tables. Some of them can further be negotiated though.

In the standard method, the circuit area is calculated by counting the number of basic cells, without any size distinction between them. The NOT-gates are ignored. The depth is counted in terms of the number of basic cells on the circuit path. The overall depth of a circuit is therefore the delay of the critical path. The NOT-gates are ignored.

2. Technology Method

Area. There exist many ASIC technologies (90 nm, 45 nm, 14 nm, etc) from different vendors (Intel, Samsung, etc), with different specifics. In order to develop an ASIC one needs to get a “standard cells library” of a certain technology, and that library usually includes much larger cells than the standard elements listed above, so that the design has a wider choice of building cells.

However, even if a standard cell is considered, for example XOR, then for different technologies that cell has different areas and delays. This makes it harder to compare two circuits of the same logic developed by two groups, when they chose to apply different technologies.

For a fair comparison of circuit area of various solutions in academia, one usually utilizes the term of Gates Equivalence (GE), where 1GE is the size of the smallest NAND gate. The size of a circuit in GE terms is then computed as Area(Circuit)/Area(NAND)→t GE. Knowing the estimated GE values for each standard or technology cell makes it possible to compute an estimated area size of a circuit in terms of GE. Although various technologies have slightly different GEs for standard cells, those GE numbers are still fairly close to each other. For this disclosure, it has been decided to use the GE values given in the data book by the Samsung's STD90/MDL90 0.35 μm 3.3V CMOS technology [7]. The cells to be used are without the speed x-factor.

Depth. Different cells, like XOR and NAND, not only differ in terms of GE but also differ in terms of the maximum delay of the gates.

Normally data books include the delays (e.g., in ns.) tPHL and tPLH for each gate, and for each input-output combinations. The switching characteristics {tPHL,tPLH} are computed as the difference between the time where the input is switched by 50% voltage threshold to the time where the output signal switches from high to low (tPHL) or from low to high (tPLH) by 50% of the voltage. It is proposed here to normalize the delays of all used gates by the delay of the XOR gate. I.e., the worst-case delay of the XOR gate is adopted as 1 unit in the measurements of the critical path. Then each standard cell is looked at and the maximum of the switching characteristics {tPHL,tPLH} is selected for all in-out paths of the cell. These are then divided by the maximum delay of the XOR gate, so that the normalized delay-units are obtained for each of the gates utilized.

For multiplexers (MUX and NMUX), propagation delays for the select bit to are ignored since in most cases, normally, the select bit is the input to the circuit. For example, in the combined SBox the select bit controls whether the forward or the inverse SBox is computed, and that selection is ready and not switching over the circuit signals propagation, so it is a stable signal.

The proposed above method is similar to the idea of GEs, but is adopted for computing the depth of a circuit, normalized in XOR delays. The reason to choose XOR as the base element for delay counting is that the circuits are most likely to have a lot of XOR gates, and thus, it now becomes possible to compare the depths between the standard and the technology methods.

Previous Work

1. Forward SBox

The most widely used design is from 2005 by Canright [4]. After 2005, there have been many attempts to improve the design, both in terms of speed and area of the forward SBox. Boyar et al constructed the previously smallest know implementation in 2012 [10] and Ueno et al from 2015 [5] has the record for the shortest critical path. Recently, Reyhani et al presented new constructions that better balance the area speed trade-off[12]. The previous results are summarized in Table 1.

2. Combined SBox

The most widely used design is from 2005 by Canright [4]. The main drawback of that design is the relatively large critical path (large depth). After 2005, there have been many attempts to improve the design, both in terms of speed and area, but almost everyone has been focusing on implementing the forward SBox only. This has relevance in certain modes of operation, where only the encryption part of the algorithm is used. In 2018, a new result on the combined SBox was published by Reyhani et al.[6]. This improves both the speed and the depth. The previous results are summarized in Table 2.

Problems with Existing Solutions

The essence of the technology described herein is that it can do much better in terms of critical path. Hence an implementation using the herein-disclosed optimization can be clocked at a higher frequency than previous implementations, thereby speeding up the encryption and decryption, or implemented using fewer cell in an ASIC or FPGA than e.g., a table look-up. This will become more and more critical as communication speeds increase and Internet of Things (IoT) devices getting smaller and smaller, demanding area-optimized encryption algorithms in hardware.

## SUMMARY

When implementing crypto algorithms in hardware, the main parameter that determines the possible clocking speed is the depth (or the critical path) of the design. For the Advanced Encryption Standard (AES)[1] this path is dominated by the SBox sub component. Hence, it is an object to find a Boolean expression for the SBox that gives as low depth as possible. For area-constrained ASICs, it is also important to keep the area of the SBox small.

In accordance with one aspect of the present invention, the foregoing and other objects are achieved in technology (e.g., methods, apparatuses, non-transitory computer readable storage media, program means) that implements SBox functionality, for example when comprised in cryptographic circuitry. In an aspect of some embodiments, an SBox circuit comprises a first circuit part, a second circuit part, and a third circuit part. The first circuit part comprises digital circuitry that generates a 4-bit first output signal (Y) from an 8-bit input signal (U). The second circuit part is configured to operate in parallel with the first circuit part and to generate a 32-bit second output signal (L) from the 8-bit input signal (U), wherein the 32-bit second output signal (L) consists of four 8-bit sub-results. The third circuit part is configured to produce four preliminary 8-bit results (K) by scalar multiplying each of the four 8-bit sub-results by a respective one bit of the 4-bit first output signal (Y), and to produce an 8-bit output signal (R) by summing the four preliminary 8-bit results (K). Furthermore, the first circuit part is configured to generate the 4-bit first output signal (Y) from the input signal (U) by performing a calculation that comprises a first linear matrix operation, a Galois Field (GF) multiplication, and a GF inversion; and the second circuit part is configured to generate the second output signal (L) from the input signal (U) by performing a calculation that comprises a second linear matrix operation.

In an aspect of some but not necessarily all embodiments consistent with the invention, the third circuit part comprises digital circuitry that performs a calculation according to:

R=Y0·M0·U⊕ . . . ⊕Y3·M3·U

wherein:

each Mi is an 8×8 matrix representing 8 linear equations on the 8-bit input U,

i=0 . . . 3,

L=M0·U∥M1·U∥M2·U∥M3·U

⊕ represents an exclusive OR, XOR, operation, and

∥ represents concatenation.

In another aspect of some but not necessarily all embodiments consistent with the invention, each of the first, second and third circuit parts is configured from digital circuits selected from any one or more of:

an XOR gate;

an XNOR gate;

an AND gate;

a NAND gate;

an OR gate;

a NOR gate;

a multiplexor, MUX;

an NMUX gate;

a NOT gate;

an And-Or-Inverter (AOI); and

an OR-And-Inverter (OAI).

In another aspect of some but not necessarily all embodiments consistent with the invention, the first circuit part and the second circuit part are configured to generate the 4-bit first output signal (Y) and the 32-bit second output signal (L) in accordance with a forward SBox operation.

In another aspect of some but not necessarily all embodiments consistent with the invention, the first circuit part (301, 503) and the second circuit part (303, 505) are configured to generate the 4-bit first output signal (Y) and the 32-bit second output signal (L) in accordance with an inverse SBox operation.

In another aspect of some but not necessarily all embodiments consistent with the invention, the first circuit part and the second circuit to part are configured to generate the 4-bit first output signal (Y) and the 32-bit second output signal (L) in accordance with a forward SBox operation; and the SBox circuitry further comprises a fourth circuit part, a fifth circuit part, and a selection circuit. The fourth circuit part comprises digital circuitry that generates an alternative 4-bit output signal (Yalt) from the 8-bit input signal (U) for use in an inverse SBox operation. The fifth circuit part is configured to operate in parallel with the fourth circuit part and to generate an alternative 32-bit second output signal (Lalt) from the 8-bit input signal (U) for use in the inverse SBox operation, wherein the alternative 32-bit second output signal (Lalt) consists of four 8-bit sub-results. The selection circuit is controllable to engage the first and second circuit parts when a forward SBox operation is selected, and to engage the fourth and fifth circuit parts when an inverse SBox operation is selected.

As mentioned above, aspects of embodiments consistent with the invention, such as those described above, can alternatively be embodied in other forms such as, but not limited to, methods, non-transitory computer readable storage media, and program means (e.g., computer program product).

## DETAILED DESCRIPTION

The embodiments describing methods and apparatus are valid for all technologies having the features and possibilities that are discussed in this disclosure. The embodiments described herein are used as non-limiting examples.

To facilitate a greater understanding of various aspects of the herein-described technology, this Description is divided into three parts. The first part (“Part A”) focuses on key aspects, and provides a complete description of these. The second part (“Part B”) describes these aspects and also goes beyond them to describe additional aspects of the technology. The third part (“Part C”) describes additional embodiments that are consistent with the technological aspects presented in Parts A to and B.

### PART A

The classical SBox architecture is built using Tower Field extensions. To build GF(2{circumflex over ( )}8) using the Tower Field construction, the teachings described in references [4,10] are followed, starting with the basic binary field GF(2) and building extension fields. Let us start with the irreducible polynomial f(x)=x{circumflex over ( )}2+x+1 over GF(2). Let W be a root of f(x) such that f(W)=0. A normal base is constructed from the conjugates of W, [W,W{circumflex over ( )}2]. Now every element k in GF(2{circumflex over ( )}2) can be expressed as k=k0W+k1W{circumflex over ( )}2, where k0 and k1 are elements in GF(2); i.e., 1 or 0.

Using the same technique, the field GF(2{circumflex over ( )}4) can be built from GF(2{circumflex over ( )}2), and from GF(2{circumflex over ( )}4) the target field GF(2{circumflex over ( )}8) can finally be built. The irreducible polynomials, roots, and normal bases used are summarized in Table 3.

Let A=a0Y+a1Y{circumflex over ( )}16 be a general element in GF(2{circumflex over ( )}8) with coefficients in GF(2{circumflex over ( )}4). The inverse of A can be written as

\(\begin{matrix}
{A^{- 1} = {\left( {AA}^{16} \right)^{- 1}A^{16}}} \\
{= {\left( {\left( {{a_{o}Y} + {a_{1}Y^{16}}} \right)\left( {{a_{1}Y} + {a_{o}Y^{16}}} \right)} \right)^{- 1}\left( {{a_{1}Y} + {a_{o}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{o}^{2} + a_{1}^{2}} \right)Y^{17}} + {a_{o}{a_{1}\left( {Y^{2} + Y^{32}} \right)}}} \right)^{- 1}\left( {{a_{1}Y} + {a_{o}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{o} + a_{1}} \right)^{2}Y^{17}} + {a_{o}{a_{1}\left( {Y + Y^{16}} \right)}^{2}}} \right)^{- 1}\left( {{a_{1}Y} + {a_{o}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{o} + a_{1}} \right)^{2}{WZ}} + {a_{o}a_{1}}} \right)^{- 1}{\left( {{a_{1}Y} + {a_{o}Y^{16}}} \right).}}}
\end{matrix}\)

And the element inversion in GF(2{circumflex over ( )}8) can be done in GF(2{circumflex over ( )}4) as

where the result is obtained as A−1=T6Y+T7Y16. In these equations several operations are utilized (addition, multiplication, scaling, and squaring) but only two of them are non-linear over GF (2): multiplication and inversion. Furthermore, the standard multiplication operation also contains some linear operations. If all the linear operations are separated from the non-linear ones and bundled together with the linear equations needed to do the base change for the AES SBox input, which is represented in polynomial base using the AES SBox irreducible polynomial x8+x4+x3+x+1, one ends up with a classical architecture (herein denoted “A”) of the SBox 201 as shown in FIG. 2. The Top Linear layer 203 of the circuitry performs base conversion and generates the linear parts of the inversion. The Bottom Linear layer 205 performs base back-conversion and affine transformation of the AES SBox.

Important Aspects of the Invention: “Architecture D”

The new architecture (herein referred to as “D” for Depth) is a new architecture in which the bottom matrix found in earlier designs has been removed, and as a result the depth of the circuit has been reduced as much as possible. The idea behind this is that the bottom matrix only depends on the set of multiplications of the 4-bit signal Y and some linear combinations of the 8-bit input U. Thus, the result R can be achieved as follows:

R=Y0·M0·U⊕ . . . ⊕Y3·M3·U

where each Mi is an 8×8 matrix representing 8 linear equations on the 8-bit input U, to be scalar multiplied by the Yi-bit. Those 4×8 linear circuits can be computed as a 32-bit signal L in parallel with the circuit for the 4-bits of Y. The result R is achieved by summing up four 8-bit sub-results. Therefore, in architecture D one gets the depth 3 after the inversion step (critical path: MULL and 8XOR4 blocks, see FIG. 5), instead of the depth 5-6 in the architecture A (see FIG. 4).

The new architecture D requires a few more gates, since the assembling bottom circuit needs 56 gates: 32NAND2+8XOR4. The reward is the lower depth.

A block diagram of one exemplary embodiment of the architecture D is depicted in FIG. 3A, and an alternative exemplary embodiment of the architecture D is depicted in FIG. 3B. The difference between the two embodiments is that, by using further techniques described later in this document, it was possible to reduce the signal Q from 22 bits down to 18 bits. In all other respects, the two embodiments are identical, and for this reason and for the sake of efficiency, the description will focus on the embodiment illustrated in FIG. 3B, with the understanding that the discussion is equally applicable to the embodiment of FIG. 3A.

As shown in FIG. 3B, an Sbox circuit 300 is arranged to perform an SBox computational step when comprised in cryptographic circuitry. The exemplary SBox circuit (300) comprises a first circuit part 301, a second circuit part 303, and a third circuit part 305. The first circuit part 301 comprises digital circuitry that generates a 4-bit first output signal (Y) from an 8-bit input signal (U).

The second circuit part 303 is configured to operate in parallel with the first circuit part 301 and to generate a 32-bit second output signal (L) from the 8-bit input signal (U), wherein the 32-bit second output signal (L) consists of four 8-bit sub-results.

The third circuit part 305 is configured to produce four preliminary 8-bit results (K) by scalar multiplying each of the four 8-bit sub-results (L) by a respective one bit of the 4-bit first output signal (Y), and to produce an 8-bit output signal (R) by summing the four preliminary 8-bit results (K).

Further in accordance with the exemplary embodiment, the first circuit part 301 is configured to generate the 4-bit first output signal (Y) from the input signal (U) by supplying the 8-bit input U to a first linear matrix circuit 307 that generates an output Q (22-bits in the embodiment of FIG. 3A, and 18 bits in the embodiment of FIG. 3B). The output Q is supplied to multiplication/summing circuitry 309 that performs a Galois Field (GF) multiplication 309 to generate a 4-bit signal, X, which is then supplied to an inverse Galois Field circuit (311), that performs a GF inversion to generate the 4-bit signal Y.

Also in accordance with the exemplary embodiment, the second circuit part 303 is configured to generate the second output signal L from the input signal U by performing a calculation that comprises a second linear matrix operation.

In order to facilitate a comparison between the conventional architecture, A, and the new architecture, D, a more detailed description and implementation size of the different blocks are shown in FIG. 4 (conventional architecture, A) and 5 (new architecture, D).

Looking first at FIG. 4, it is seen that the conventional SBox architecture 400 includes a top layer 401 that is alternatively configured either as a Forward SBox (FTopA), an Inverse SBox (ITopA), or as a Combined SBox (CTopA) that enables selection between forward and inverse computations). But a notable aspect is that the conventional SBox architecture 400 also includes a bottom layer 403 that is alternatively configured either for forward operation (FBotA), inverse operation (IBotA), or a combination that enables selection between forward and inverse operation (CBotA)).

The inventors have recognized that the bottom layer 403 of the conventional SBox architecture A 400 can be eliminated, and depth reduced, by redistributing many functional aspects of the bottom layer into upper layers. A result is the Architecture D 500, shown in FIG. 5.

The Architecture D 500 depicted in FIG. 5 has an organization that is equivalent to that shown in FIG. 3. Notably, it includes a top layer 501 that is alternatively configured either as a Forward SBox (FTopD), an Inverse SBox (ITopD), or as a Combined SBox (CTopD) that enables selection between forward and inverse computations. In the case of the Combined SBox (CTopD), selection between forward and inverse computations is in dependence on a received forward/inverse

A notable feature is that some functional aspects of the conventional bottom layer (see, e.g., bottom layer 403 in FIG. 4) have been redistributed into upper layers of the new architecture 500, so it now has a first circuit part 503 that operates in parallel with a second circuit part 505. The first circuit part 503 generates a 4-bit first output signal (Y) from the 8-bit input signal (U), and the second circuit part 505 generates a 32-bit second output signal (L) from the 8-bit input signal (U), wherein the 32-bit second output signal (L) consists of four 8-bit sub-results.

The output Y from the first circuit part 503 and the output L from the second circuit part 505 are processed together by a third circuit part 509 that is configured to produce four preliminary 8-bit results (K) by scalar multiplying each of the four 8-bit sub-results by a respective one bit of the 4-bit first output signal (Y), and to produce an 8-bit output signal (R) by summing the four preliminary 8-bit results (K).

Details of an exemplary gate configuration of the new SBox Architecture 500 are presented in the following.

Preliminaries

In the listings presented below, specifications for six circuits for the forward, inverse, and combined SBoxes in two architectures A(small) and D(fast) are described. The symbols used in the following listings are as follows, and have the indicated meanings:


- - \#comment—a comment line
  - @filename—means that the code from another file called ‘filename’
    should be included, the listing of which is then given in this
    section as well.
  - a{circumflex over ( )}b—is the usual XOR gate; other gates are
    explicitly denoted and taken from the set of {XNOR, AND, NAND, OR,
    NOR, MUX, NMUX, NOT}
  - (a op b)—where the order of execution (the order of gates
    connections) is important we specify it by brackets.

The inputs to all SBoxes are the 8 signals {U0 . . . U7} and the outputs are the 8 signals {R0 . . . R7}. The input and output bits are represented in Big Endian bit order. For combined SBoxes the input has additional signals ZF and ZI where ZF=1 if we perform the forward SBox and ZF=0 if inverse, otherwise; the signal ZI is the compliment of ZF. We have tested all the proposed circuits and verified their correctness.

The circuits are divided into sub-programs that correspond, respectively, to the functions/layers shown in FIG. 5. The discussion starts with a description of the common shared components, and then for each solution the components (common or specific) for the circuits are described.

Shared Components

The following bonus circuits are included to update the world record for the smallest SBox.

The new record is 108 gates with depth 24.

**Advantages of the Invention**

Having a design for a fast SBox is very important for certain classes of applications, for example AES hardware support in CPUs. In such a scenario it is likely that the SBox design is placed-and-routed with extreme care for the critical path. Having a very short critical path might speed up the possible clocking frequency considerably. Also in an FPGA where it is more difficult (than in an ASIC) to reach high clocking frequencies, it is important to have as few gates in the critical path as possible.

The tables from the Background section have been extended to now also include results of the new Architecture D described here. Note how the critical path has been substantially reduced compared to conventional SBox circuits.

1. Forward SBox

Results of New Architecture D

2. Combined SBox

A synthesis of the results has been performed and compared with other recent academic work.

The technology process is GlobalFoundries 22 nm CSC2OL [Glo19], and synthesis has been performed using Design Compiler 2017 from Synopsys in topological mode with the compile_ultra command. Also, the flag compile_timing_high_effort was turned on in order to force the compiler to make as fast circuits as possible. In the following graphs, the X axis is the clock period (in ps) and the Y axis is the resulting topology estimated area (in μm2). The number of available gates was not restricted in any way, so the compiler was free to use non-standard gates e.g., a 3 input AND-OR gate. To get the graphs in the following subsections, the clock period was started at a 1200 ps clock period (˜833 MHz) and was then reduced by 20 ps until the timing constraints could not be met. It is noted that that the area estimates by the compiler fluctuate heavily, and this is believed to be a result of the many different strategies the compiler had to minimize the depth of. One strategy might be successful for say a 700 ps clock period, but a different strategy (which results in a significantly larger area) could be successful for 720 ps. There is also an element of randomness involved in the strategies for the compiler.

The synthesis results for the forward SBox are shown in FIG. 6, and for the combined SBox in FIG. 7. To enable comparison, FIG. 6 shows graphs of synthesis results for the architectures of:


- - Ches18_fast **601**
  - Ches18_small **603**
  - “fast” circuit **605**, as described herein
  - “optimal” circuit **607**, as described herein
  - “bonus” circuit **609**, as described herein.

(The terms “Ches18_fast” and “Ches18_small” refer to the results in [12].)

In FIG. 6:


- - The curve **605** depicting the herein-described “fast” circuit is
    shown ranging from just under 650 ps up to approximately 1075 ps.
  - The curve **603** depicting “ches18_small” ranges from approximately
    780 ps up to approximately 1075.
  - The curve **601** depicting “ches18_fast” ranges from approximately
    800 up to approximately 1075.

To enable further comparison, FIG. 7 shows graphs of synthesis results for the architectures of:


- - canright **701**.
  - reyhani **703**.
  - “fast” circuit **705**, as described herein.
  - “fast-s” circuit **707**, as described herein.
  - “optimal” circuit **709**, as described herein.
  - “bonus” circuit **711**, as described herein.

(The term “Canright” refers to the results in [4] and the term “reyhani” refers to the results in [6].)

In FIG. 7:


- - The curve **707** depicting “ ”fast-s” is shown closest to the
    x-axis, and ranges from approximately 740 up to 1200.
  - The curve **705** depicting “fast” is shown second-closest to the
    x-axis, and ranges from approximately 740 up to 1200.
  - The curve **703** depicting “reyhani” ranges from approximately 900
    up to 1200.
  - The curve **701** depicting “canright” ranges from approximately
    1000 up to approximately 1200.

In each of FIGS. 6 and 7, the closer the curve is to the axes, the better the result in terms of area/speed trade-off.

Further aspects of the herein-described technology are now described with reference to FIG. 8, which is in one respect a flowchart of actions performed by embodiments consistent with the invention. In another respect, FIG. 8 can also be considered a block diagram of means 800 for performing SBox functionality, comprising the various component parts (801, 803, 805, 807, and 809) for mapping an input to an output in accordance with SBox functionality.

Actions begin with receiving an 8-bit input, U (step 801). The 8-bit input is supplied as an input to two further actions that operate in parallel with one another. A first of these is using a first linear matrix operation, a Galois Field (GF) multiplication, and a GF inversion to generate a 4-bit first output signal (Y) from the 8-bit input signal (U) (step 803).

And in parallel, a calculation is performed (step 805) that comprises a second linear matrix operation to generate a 32-bit second output signal (L) from the input signal (U), wherein the 32-bit second output signal (L) consists of four 8-bit sub-results.

Next, four preliminary 8-bit results (K) are produced by scalar multiplying each of the four-8-bit sub-results of the 32-bit second output signal (L) by a respective one bit of the 4-bit first output signal (Y) (step 807).

Then, an 8-bit output signal (R) is produced by summing the four preliminary 8-bit results (K).

In other aspects of embodiments consistent with the invention, as illustrated in FIG. 9, the architectures of the improved SBox as described herein can also be embodied in a number of other forms including a computer program 901 comprising a set of program instructions configured to cause one or processors to perform a series of actions such as those depicted in any of FIGS. 3A, 3B, 5, and 8 (for example, the computer program 901 when run on a processing device causes operation in accordance with the various embodiments described herein). Generally, program modules may include routines, programs, objects, components, data structures, etc. that performs particular tasks or implement particular abstract data types. Computer-executable instructions, associated data structures, and program modules represent examples of program code for executing steps of the methods disclosed herein. The particular sequence of such executable instructions or associated data structures represents examples of corresponding acts for implementing the functions described in such steps or processes.

Some other embodiments take the form of a computer readable storage medium 903 (or equivalently a set of media) comprising a computer program 901 as described above. A computer-readable medium 901 may include removable and non-removable storage devices including, but not limited to, Read Only Memory (ROM), Random Access Memory (RAM), compact discs (CDs), digital versatile discs (DVD), and the like.

Still other embodiments can take the form of a computer program product 905, embodied in a computer-readable medium 903, including computer-executable instructions, such as program code, executed by computers in networked environments.

Throughout this disclosure, the blocks in the various diagrams may refer to a combination of analog and digital circuits, and/or one or more controller units, configured with software and/or firmware, e.g. stored in the storage units (data base), that when executed by the one or more controller units perform as described above. One or more of these controller units, as well as any other combination of analog and digital circuits, may be included in a single application-specific integrated circuitry (ASIC), or several controller units and various digital hardware may be distributed among several separate components, whether individually packaged or assembled into a system-on-a-chip (SoC). The one or more controller units may be any one of, or a combination of a central processing unit (CPU), graphical processing unit (GPU), programmable logic array (PAL) or any other similar type of circuit or logical arrangement.

Advantages

A new architecture is disclosed herein that is faster (having shorter critical depth) than previously known results. In this new architecture, the bottom linear matrix that is present in conventional solutions (see, e.g., FIG. 2) has been removed, with most of the calculations instead being performed in the top linear matrix, parallel to the inversion circuit (see, e.g., FIGS. 3A and 3B). In this way the depth of the circuit is reduced by roughly 25%-30%. The resulting SBoxes are the fastest known.

**Abbreviations**

AES: Advanced Encryption Standard

ASIC: Application Specific Integrated Circuit

FPGA: Field Programmable Gate Array

## PART B OF THE DISCLOSURE

Smallest, Optimal, and Fastest AES SBoxes

### 1 Introduction

Efficient hardware design of the AES SBox is a well-studied subject. If you want the absolute maximum speed, you'd probably use a straight forward table-lookup implementation, which naturally lead to a large area. In many practical situations the area of the cryptographic subsystem is limited, and the designer cannot afford to implement table-lookup for the 16 SBoxes involved in an AES round, especially when implemented in an FPGA. For these situations, we need to study how to implement the AES SBox with logical gates only, focusing on both area and maximum clocking speed. The maximum clocking speed of a circuit is determined by the critical path or depth of the circuit; the worst case time it takes to get stable output signals from a change in input signals.

Another aspect when implementing AES is the need for the inverse cipher. Many modes of operation for a block cipher only use the encryption functionality and hence there is no need for the inverse cipher. In case you need both the forward and inverse SBox, it is often beneficial to combine the two circuits. This is because the main operation of the AES SBox is inverting a field element, which naturally is its own inverse, and we expect that many gates of the two circuits can be shared.

From a mathematical perspective, the forward AES SBox is defined as the composition of a non-linear function I(g) and an affine function A(g), such that SBox(g)=A(I(g)). The non-linear function I(g)=g−1 is the multiplicative inverse of an element g in the finite field GF(28) defined by the irreducible polynomial x8+x4+x3+x+1. We will assume that the reader is familiar with the AES SBox, and refer to [oST01] for a more comprehensive description.

The first step towards a small area implementation was described by Rijmen [Rij00], where results from [IT88] was used. The idea is that the inverse calculation in GF(28) can be reduced to a much simpler inverse calculation in the subfield GF(24) by doing a base change to GF((24)2). In 2001, Satoh et al [SMTM01] took this idea further and reduced the inverse calculation to the subfield GF(22). In 2005, Canright [Can05] built on the work of Satoh et al and investigated the importance of the representation of the subfield, testing many different isomorphisms that led to the smallest area design. This construction is perhaps the most cited and used to implementation of an area constraint combined AES SBox.

In a series of papers, Boyar, Peralta et al presented some very interesting ideas for both the subfield inverter as well as new heuristics for minimizing the area of logical circuits [BP10a, BP10b, BP12, BFP18]. They derived an inverter over GF(24) with depth 4 and a gate count of only 17. The construction in [BP12] is the starting point for this disclosure.

After Boyar, several other papers followed focusing on low depth implementations [JKL10, NNT+10, UHS+15]. In 2018 two papers by Reyhani et al [RMTA18a, RMTA18b] presented the best known implementation (up until now) of both the forward SBox as well as the combined SBox. As pointed out in [RMTA18a], there are misalignment between researchers in how to present and compare implementations of combinatorial circuits. One way is to simply count the total number of standard gates in the design and find the path through the circuit that contains the critical path to determine and compare the speed. In practice it is much more complicated than that. For this paper, we present both the simple measure using only the number of gates, as well as giving a Gate Equivalent (GE) number based on the typical area required for the gate compared to the NAND gate. So for example the NAND gate will have GE=1, while the XOR gate will have a GE=2.33. The relative numbers for the GE are dependent on the specific ASIC process technology used, as well as the drive strength needed from the gate. We have used the GE values obtained from the Samsung's STD90/MDL90 0.35 μm 3.3V CMOS technology [Sam00]. A comprehensive discussion on our choices for circuits comparison can be found in Appendix A. Additionally, we propose to count technological depth of a circuit normalized in terms of the delays of a XOR gate, which makes it possible to compare depths and the speed of various academic results.

In the following disclosure, various new techniques to minimize a circuit realization of a linear matrix are presented and analyzed. Also, a novel approach to include multiplexers in the minimization is introduced, which is relevant for the combined SBox construction. Also, a new architecture is provided in which the bottom linear matrix (present in conventional circuits) is removed in order to get as small circuit depth as possible. These new techniques result in smaller and faster AES SBoxes than previously presented.

### 2 Preliminaries

We will follow the notation used in both [Can05] and [BP12] when we now construct our tower field representation. The irreducible polynomials, roots, and normal basis can be found in Table 1.

Following [Can05] and [BP12], we can now derive the expression for inverting a general element A=a0Y+a1Y16 in GF(28) as

\(\begin{matrix}
{A^{- 1} = {\left( {AA}^{16} \right)^{- 1}A^{16}}} \\
{= {\left( {\left( {{a_{0}Y} + {a_{1}Y^{16}}} \right)\left( {{a_{1}Y} + {a_{0}Y^{16}}} \right)} \right)^{- 1}\left( {{a_{1}Y} + {a_{0}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{0}^{2} + a_{1}^{2}} \right)Y^{17}} + {a_{0}{a_{1}\left( {Y^{2} + Y^{32}} \right)}}} \right)^{- 1}\left( {{a_{1}Y} + {a_{0}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{0} + a_{1}} \right)^{2}Y^{17}} + {a_{0}{a_{1}\left( {Y + Y^{16}} \right)}^{2}}} \right)^{- 1}\left( {{a_{1}Y} + {a_{0}Y^{16}}} \right)}} \\
{= {\left( {{\left( {a_{0} + a_{1}} \right)^{2}{WZ}} + {a_{0}a_{1}}} \right)^{- 1}{\left( {{a_{1}Y} + {a_{0}Y^{16}}} \right).}}}
\end{matrix}\)

And the element inversion in GF(28) can be done in GF(24) according to

where the result is obtained as A−1=T6Y+T7Y16. In these equations we utilize several operations (addition, multiplication, scaling, and squaring) but only two of them are nonlinear over GF(2); multiplication and inversion. Furthermore, the standard multiplication operation also contains some linear operations. If we separate all the linear operations from the non-linear and bundle them together with the linear equations needed to do the base change for the AES SBox input, which is represented in polynomial base using the AES SBox irreducible polynomial x8+x4+x3+x+1, we will end up with an architecture of the SBox according to FIG. 2.

In case we are dealing with the inverse SBox, we naturally need to apply the inverse affine transform to the top linear matrix instead of the bottom.

This architecture will be our starting point, and we will now provide a set of new or enhanced algorithms for minimizing both the area and the depth of the two linear top and bottom matrices.

### 3 Circuits for Binary Linear System of Equations

In this section, we will recapitulate the known techniques for linear circuit minimization and propose a few improvements. We start by clearly stating the objectives.

**3.1 Basic Problem Statement**

Given a binary matrix Mm×n and the maximum allowed depth maxD, find the circuit of depth D≤maxD with the minimum number of XOR gates such that it computes Y=M·X. In other words, given n bits of input X=(x0 . . . xn−1) the circuit should compute m linear combinations Y=(y0 . . . ym−1). Any circuit realization that implements a given system of linear expressions is called a solution.

The above problem is NP complete, and we have seen various heuristic approaches that help finding a sub-optimal solution in the literature. In all previous work we have studied, the assumption is that all input signals arrive in the same time, and all output signals are “ready” with delays at most maxD. In this paper we extend the problem with AIR and AOR defined as follows.

Additional Input Requirement (AIR). The problem may be extended with an additional requirement on input signals X, such that each input bit xi arrives with its own delay di, in terms of XOR-gates delays. The resulting depth D≤maxD then includes input delays. For example, if some input xi has the delay di>maxD then no solution exists. The AIR is useful while deriving the bottom matrix as described in Section 2, since after the non-linear part, the signals entering the bottom matrix will have different delays.

Additional Output Requirement (AOR). The problem may be extended by an additional requirement on the output signals. Each output signal yi may be required to be “ready” at depth at most ei≤maxD. This is useful when some output signals continue to propagate in the critical path and other signals may be computed with larger delays, but still at most maxD. The AOR is used while deriving the top matrix as described in Section 2, since when we introduce multiplexers for the combined SBox, the output signals of the top matrix will be required to have different delays.

**3.2 Cancellation-Free Heuristics**

Cancellation-free heuristics is an algorithm that produces linear expression z=a⊕b, where both a and b are Boolean linear expressions in the input variables, and a and b share no common terms. In other words, as we add a and b we will not cancel out any term.

Paar [Paa97] suggested a greedy approach to solving the Basic Problem in 3.1. That solution starts with the matrix M and considers all pairs of columns (i, j) in M. Then a metric is defined (on the pairs of columns) as the number of rows where Mr,i=Mr,j=1, i.e. where the input variables xi and xj both occur. For the column pair with the highest metric, we form a new variable xn=xi⊕xj and add that to the matrix (which now is of size m×(n+1)), and set positions Mr,i=Mr,j=0, and Mr,n+1=1.

Also Canright [Can05] used this technique but instead of using the metric function, he performed an exhaustive search over all possible column pairs. This was possible due to the fact that the target matrix in his case was the base conversion matrix only of size 8×8. As we saw in Section 2, our bottom matrix will be considerably larger, and hence we need to take another approach. We also need to consider the AIR and the AOR.

Solving the AIR. When performing the algorithm we should keep track of the depth of the newly added XOR gates. This is done by having a vector D=(d0 . . . dn−1) with the current depth of all inputs and newly added signals xi. When the new signal xn=xi⊕xj is added, the delay of xn is trivially dn=max(di, dj)+1. We then also restrict the algorithm such that if dn>maxD then we are not allowed to add xn as a new input signal. The AIR is hereby solved automatically.

Solving the AOR. Similarly, when adding a new input variable xn, we need to check if a solution is theoretically possible. We may do that using the function CircuitDepth (detailed as Algorithm 2 in Appendix B.1). If CircuitDepth returns a larger delay than ei we know that no solution exists, and that particular xn should be avoided.

Probabilistic heuristic approach. Since we cannot perform a full exhaustive search on the bottom matrix due to its size, we need to confine the number of pairs to keep and further evaluate. We have found that keeping the K best candidates (based on the original metric by Paar) and then randomly select which one to pick for the next XOR gate is a good strategy. In our simulations, this probabilistic approach gave us much smaller circuits than only considering the best metric candidates. Naturally, the execution time will be too long if we pick a too large K, and conversely picking a too small K decreases the chances of deriving a good circuit. In practice we found that K=2 . . . 6 is a reasonable number of candidates to keep and try.

**3.3 Cancellation-Allowed Heuristic**

Cancellation-free approaches are sub-optimal, as it was shown by Boyar and Peralta in [BP10a], where they also introduced a new algorithm that allows cancellations. This was later improved by Reyhani et al in [RMTA18a]. Next, we briefly describe the basic idea of that heuristic.

**3.3.1 Basic Cancellation-Allowed Algorithm [BP10a]**

Every row of M is an n-bit vector of 0s and 1s. That vector can be seen as a n-bit integer value. We define that integer value as a target point. Thus, the matrix M can be seen as the column vector of m target points. The input signals {x0, . . . , xn−1} can also be represented as integer values xi=2i, for i=0 . . . n−1.

Let the base set S={s0, . . . , sn−1}={1,2,4, . . . ,2n} initially represent the input signals. The key function of the algorithm is the distance function δi(S,yi) that returns the smallest number of XOR gates needed to compute a target point yi from the set of known points S. The algorithm keeps a vector Δ=[δ0, δ1, . . . , δn−1] which is initially set to the Hamming weight minus one of the rows of M, which would be the number of XOR gates needed without any sharing.

The algorithm then proceeds by combining two base points si and sj in the base set S, and XOR them together producing a candidate point c=si ⊕sj. The selection of si and sj; is performed by an exhaustive search over all distinct pairs, and then for each candidate point, the sum of the distance vector Σδi, for i∈[0,n−1], is calculated. Note that the distance functions δi now is computed over the set S∪{c}. The pair which gives the smallest distance sum is picked and S is updated S=S∪{c}. In case there is a tie, the algorithm picks the pair that maximizes the Euclidean norm √{square root over (Σδi2)}, for i∈[0,n−1]. If there is a tie after this step too, the authors in [BP10a] investigated different strategies and concluded that all strategies tested performed similarly, and hence a simple random selection can be used. The algorithm then repeats the step of picking two new base points and calculating the distance vector sum, until the distance vector is all-zeros and the targets are all found. In the original description, there is also a notion of “preemptive” choices. A preemptive choice is a candidate point c such that it directly fulfils a target row in the matrix M. If such a candidate is found, it is immediately used as the new point and added to S.

Reyhani et al [RMTA18a] improved the original algorithm by directly searching for preemptive candidates in each round and add them all to the set S before the “real” candidate is added and the distance vector recalculated. They also improved the tie resolution strategy and kept all the candidates that were equally good under the Euclidean norm and recursively tried them all, keeping the one that was best in the next round. In our experiments we concluded that keeping two different candidates and recursively evaluating them gave good results.

Our improvement to this algorithm is a faster evaluation of the 5 values for moderate sized n-values. It can be found in Appendix B.2.

3.3.2 when the Maximum Depth maxD is a Required Constraint

Although the AIR problem can be solved simply by adding the vector of delays D of all known signals alongside with S, the problem of finding a short circuit with a fixed maxD is still quite difficult. Even if we limit every newly added signals in S to be of depth≤maxD, the resulting circuit becomes very large in terms of XOR gates, in fact much larger than what we could achieve with cancellation-free heuristic.

One idea is that if there is a tie with respect to the shortest distances δi=δ(S,yi), then we should take c with the smallest delay. But in our simulations it didn't produce better results than the cancellation-free algorithm, even if we add a randomization factor to both algorithms. We must conclude that adoption of the additional maxD-constraint to that cancellation-allowed heuristic algorithm is still an open question.

**3.4 Exhaustive Search Methods**

In this section we present an algorithm for an efficient exhaustive search of the minimal circuit. The overall complexity is exponential in the number of input signals, and linear in the number of output signals. From our experiments we can conclude that this exhaustive search algorithm can be readily applied to circuits of approximately 10-bits input.

**3.4.1 Notations and Data Representation**

Using the same integer representation of the rows of M, and the input signals xi as in Section 3.3.1, we can re-phrase the basic problem statement: given the set of input points xi we want to find the sequence of XORs on those points such that we get all the m wanted target points yi, the rows of the matrix M, with the maximum delay maxD. Input and output points may have different delays di and ei, respectively.

For data structures, we can store a set of 2n points as either a normal set, and/or as a bit-vector. The set makes it possible to loop through the points while the bit-mask representation is efficient to test set membership.

**3.4.2 Basic Idea**

The exhaustive search algorithm is a recursive algorithm, running through the depths, starting at depth 1 and running down to maxD. At each depth D, we try to construct new points from the previous depths, thereby constructing circuits that are of exactly depth D. When all target points are found, we check the number of required XOR gates, keeping track of the smallest solution. We will need the following sets of points:

known[maxD+1]—the set of known points at certain depth D.

ignored[maxD+1]—the set of points that will be ignore at depth D.

targets—the set of target points.

candidates—the set of candidate points to be added to the set known at the current recursion step.

The initial set of known points is xi, for i=0 . . . n−1, and the set of target points is yi, for i=0 . . . m−1. AIR is solved by initially placing the input point xi to the known set at depth di. AOR is solved by setting the point yi with output delay ei to the ignore list on all depth levels that are larger than ei.

We will now explain the steps executed at each depth of the recursion, assuming that we currently are at depth D.

Step 1—Preemptive points. Check the known[D] set to see if any pair can be combined (XOR:ed) to give a target point not yet found. If all targets are found, or if we have reached maxD, we return from this level of the recursion.

Step 2—Collect candidates. Form all possible pairs of points from the known[0 . . . D−1] sets, where at least one of the points is from known [D−1], and XOR the pair to derive a new point. If the derived point is in the set ignored[D] then we skip it, otherwise we add it to candidate set.

Step 3—In this step we try to add points from the candidate set to the known list, and call the algorithm recursively again. We start by trying to add 1 point and do the recursive call. If that's not solving the target points, we'll try to add 2 points, and so on until all combinations (or a maximum number of combinations) of the points in the candidate set have been tried.

**3.4.3 Ignored Points and Other Optimizations**

In step 2, we check the candidate against the ignored [D] set, the set of ignored points at depth D. The ignored set is constructed from a set of rules; Intersection: A candidate point p should be ignored if for all target points wi we get (wi&p)≠p. This means that the point p covers too many of the input variables, and is not covered by any of the points in the targets set; Forward Propagation: We can calculate all possible points on each level starting from the top level D=0 with n known points and going down to D=maxD. Those points that can never appear on some level d are then included into the ignored [d] set. If some target point w has another desired maximum delay ei<maxD, then that point on the following depths should be ignored, i.e., we add w to ignored [ei+1 . . . maxD]; Sum of Direct Inputs: If any of the input signals xi xj give the point p=xi⊕xjon level d, then all consecutive levels>d must have the point p in the ignored list; Backward Propagation: As a last check, we can go backwards level by level, starting from d=maxD and ending at level d=1, and for each allowed (not ignored) point on the level d we check whether there is still a not-ignored pair a,b on the previous levels (one of a or b must be on the level d−1) such that it gives p=a⊕b. If not, then the point p should be added to the ignore [d] set; Ignore Candidates: dynamically add a point w to the ignore [d] set if w has been one of the candidates on previous levels<d.

**3.5 Conclusions**

From our simulations we can conclude the following regarding searching for the minimum solution; the top matrix (with only 8 inputs) can be solved with the exhaustive cancellation-allowed search as in Section 3.4. The bottom matrix (with 18 inputs) is too large for a direct exhaustive search, and we should start with a probabilistic cancellation-free heuristic from Section 3.2, and then use a full exhaustive search for the ending part, when the Hamming weights of the remaining rows become small enough to perform the exhaustive search. This approach showed to give the best result.

4 System of Linear Circuits with Multiplexers

Assume we want to find a circuit for the combined SBox, where the top and the bottom linear matrixes need to be multiplexed based on the SBox direction. This means that the circuit for the combined linear expressions is basically doubled in size, plus the set of multiplexers. In this section we will show how to deal with multiplexed systems of linear expressions. We will show that the MUX and XOR gates can be resolved in a combined way in order to achieve a very compact circuit.

### 4.1 Floating Multiplexers

Consider that for some signal Y we have to compute two linear expressions YF and YI for the forward and the inverse SBoxes respectively. Then we apply a multiplexer so that only one of the signals continues as Y. Assume further that the signals YF and YI share some part of the expression. Then it may be better to push that shared part down under the multiplexer, and the resulting solution can be simplified.

For example, let YF=X0⊕X1 and YI=X0⊕X2, then normally we should spend 2 XOR gates and 1 multiplexer, so that we get Y=MUX(select,X0 ⊕X1,X0 ⊕X2) with 3 gates. However, we can push the common part X0 behind the multiplexer as follows:

Y=MUX(select,X1,X2)⊕X0,

then we get a circuit with only 2 gates. In general, one can pick any linear combination A on input signals and make a substitution:

Y=MUX(select,YF,YI)→MUX(select,YF⊕Δ,YI⊕Δ)⊕Δ,

Where Δ is then added to the linear matrix as an additional target signal to compute. If that substitution leads to a shorter circuit then we keep it. We should also choose such Δ that the overall depth is not increased. Thus, various multiplexers will be “floating” over the depth of the circuit. Signals with Δ≠0 should have their maximum depth decreased by 1.

**4.1.1 Metrics and Linear Expressions to Solve**

We have n input signals X1 . . . Xn and m output signals Y1 . . . Ym, where each Yi is represented in its most general form as a triple (Ai, Bi, Ci) such that

Yi=Ai⊕MUX(select,Bi,Ci)

where Ai, Bi, and Ci are linear expressions on the input signals. We are allowed to modify the above expression as (Ai⊕Δi, Bi⊕Δi, Ci⊕Δi) for any Δi, since the Boolean function of Yi would not change.

Let ABC represent the linear matrix that describes all the rows Ai, Bi, and Ci, for i=0 . . . m, such that

ABC×X

gives the wanted linear system to realize using minimal number of gates and a given maxD. By choosing favorable values of Δi, one can shrink the number of total gates, since some of the target points of ABC may become equal to each other, and hence ABC can be reduced by at least one row. Also, some of the targets may become 0 or having only one bit—i.e., they equal to corresponding input signals. These targets are also removed from the linear system as they are trivial and cost zero gates. After the above reductions we get a system of linear expressions where all rows are distinct and have Hamming weight at least 2. As before, we interpret the rows of ABC as integers, and adding (XOR:ing) a Δi to the three rows Ai, Bi, and Ci will change those three target points, but not the resulting Yi.

Metric. Search for a good combination of Δs requires a lot of computation and it rapidly becomes infeasible to compute a minimal solution for each selection. Thus, we need to decide on a good metric that allows us to truncate the search space down to promising sets of Δs. We propose to adopt a metric that is based on the lower bound of the number of gates of a fixed system (when Δ values are selected), and define the metric to be the number of rows of the reduced ABC matrix, plus the minimum number of extra gates needed to complete the circuit, such as multiplexers.

In the following we present several heuristic approaches to find a good set of Δs while minimizing the metric.

**4.1.2 Iterative Algorithms to Find Δs: Metric→Minimize**

The below techniques only work for small n, but in our case it is readily applicable to the 8-input top matrix of the AES SBox.

Algorithm-A(k)—Select k triplets (Ai, Bi, Ci) and try to find matching Δis that minimize the metric. If some choice results in a smaller metric, we keep that choice and continue searching with the updated ABC matrix. The algorithm runs in a loop until the metric is not decreasing any more. Algorithm-A(1) is quite fast, and Algorithm-A(2) also has acceptable speed. For larger ks it becomes infeasible. Algorithm-A(k) works fine for a very quick/brief analysis of the given system but the result is quite unstable since for a random initial values of Δis the resulting metric fluctuates heavily.

Algorithm-B—unlike Algorithm-A this algorithm is trying to construct a linear system of expressions, starting from an empty set of knowns S and then trying to add new points to S one by one, until all targets of ABC become included in the set S. While testing whether a new candidate C should be added to S we loop through all (Ai, Bi, Ci) and for each one try to find a Δi that minimizes the overall metric. This heuristic algorithm is a lot more stable and gives quite good results.

But the smallest possible metric does not guarantee that the final solution will have the smallest number of gates, and the number of non-target intermediates needed is unclear. Thus, it would be a good idea to collect a number of promising systems whose metric is the smallest possible, then try to find the smallest solution amongst them. We will investigate this in the next section.

4.2 New Generic Heuristic Technique for Linear Systems with Floating Multiplexers

If we generalize the idea of floating multiplexers and let them float even higher up in the circuit, and also sharing them wider, we could achieve better results. In this section we propose a generic heuristic algorithm that finds a nearly best circuit for such systems.

### 4.2.1 Problem Statement

We are given n-bit input signal Xn, binary matrices Mm+nF and Mm×nI, binary vectors AnF, AnI, BmF, BmI, and vectors of delays DnX and DmY. We want to find a smallest and shortest solution that computes the m-bit output signal Y:

YF=MF·(X⊕AF)

YI=MI·(X⊕AI)

Y=MUX(ZF;YF⊕BF;YI⊕BI),

where each input signal Xi has an input arrival delay Dix and each output signal Yj must have the total delay at most DiY. A* and B* are constant masking vectors for the input and output signals respectively (NOT-gates). ZF is the mux selector, when ZF=1 we pick the first (YF=“forward”) output otherwise the second (YI=“inverse”) output. We also assume there is a complement signal ZI=ZF⊕1 that is also available as an input control signal.

**4.2.2 Preliminaries**

Similar to our previous notation, we define a “point” to be tuple of a point value (.p) and a delay (.d):

point:={.p=[f(1 bit)IF(n bits)|i(1 bit)≡I(n bits)],.d=Delay}

which is then translated into a 1-bit signal circuit

signal:=MUX(ZF;F·X⊕f,I·X⊕i)

with a total output delay point.d. I.e., F and I are linear combinations on the n-bit input X, and F and I are negate bits applied to the result in case the selector is “forward” or “inverse”, respectively. The n input points are then represented as:

input point Xk:={.p=[AkF|2k|AkI|2k],. d=DkX}, for k=0, . . . ,n−1,

and the target m points are:

target point Yk:={.p=[BkF|YkF|BkI|YkI],DkY}, for k=0, . . . ,m−1.

We should also include the following 4 trivial points to the set of inputs:

signal ZF:={.p=[1|0|0|0],.d=0} signal 0:={.p=[0|0|0|0],.d=0}

signal ZI:={.p=[0|0|1|0],.d=0} signal 1:={.p=[1101110],.d=0}

Given any two (ordered) points v and w there are at most 6 possible new points that can be generated based on the following gates:

MUX(v;w):={.p=[v.f|v.F|w.i|w.I],.d=Dnew}

NMUX(v;w):={.p=[v.f⊕1|v.F|w.i⊕1|w.I],.d=Dnew}

MUX(w;v):={.p=[w.f|w.F|v.i|v.I],. d=Dnew}

NMUX(w;v):={.p=[w.f⊕1|w.F|v.i⊕1|v.I],.d=Dnew}

XOR(v;w):={.p=[w.f⊕v.f|w.F⊕v.F|w.i⊕v.i⊕w.I⊕v.I],.d=Dnew}

NXOR(v;w):={.p=[w.f⊕v.f⊕1|w.F⊕v.F|w.i⊕v.i⊕1|w.I⊕v.I],.d=Dnew}

where Dnew=max{v.d,w.d}+1. Note that the inclusion of the 4 trivial points is important, since then we can limit the number of gate types to be considered. For example, a NOT-gate is then implemented as XOR(v; 1), AND gate with ZF can be implemented as MUX(v;0), OR gate with ZI is MUX(v; 1), etc.

**4.2.3 The Algorithm**

We start with the set S of input points (of size n+4), and place all target points into the set T. At each step, we compute the set of candidate points C that is generated by applying the above 6 gates to any two points from the set S. Naturally, C should only contain unique points and exclude those already in S. We try to add one candidate point from C to S and compute the distances from S to each of the target points in T. Thereafter we compare metrics to decide which candidate point will be included into Sat this step, and start over by calculating the possible candidates. The algorithm stops when the overall distance δ-metric is 0.

The metric consists of several values. The distance δ(S,ti) is the minimum number of basic gates (the above 6) required to get the target point ti from the points in S, such that the delay is at most DiY. Subsection 4.2.5 discusses how to compute δ(S,ti). The applied metrics and their order of importance are then as follows:

\(\gamma = \left. {\left( {{❘S❘} - n - 4} \right) + {\sum\limits_{i = 0}^{m - 1}{\delta\left( {S,t_{i}} \right)}}}\rightarrow\min \right.\)
\(\delta = \left. {\sum\limits_{i = 0}^{m - 1}\left( {{\delta\left( {S,t_{i}} \right)} - \left( {{\delta\left( {S,t_{i}} \right)}==1} \right)} \right)}\rightarrow\max \right.\)
\(\tau = \left. {{delay}{of}{the}{recent}{candidate}{point}{from}C{added}{to}S}\rightarrow\min \right.\)
\(v^{2} = \left. {\sum\limits_{i = 0}^{m - 1}\left( {{\delta\left( {S,t_{i}} \right)} - \left( {{\delta\left( {S,t_{i}} \right)}==1} \right)} \right)^{2}}\rightarrow\max \right.\)

The metric γ is the projected number of gates in case there will be no more shared gates; that metric we should definitely minimize. In case there are several candidates that give the same value, then we look into the second metric δ.

δ is the sum of distances excluding distances where only 1 gate is needed. Given the smallest γ, we must maximize δ. The larger δ the more opportunities to shrink γ. We exclude distances 1 because of the inclusion of the preemptive step that we will describe below. When we accept candidates to S one by one as described above, the metrics δ and γ are similar, but will become distinct when we, in the next subsection, introduce a search tree where the size of ISI may differ.

τ selects the candidate having the minimum depth in case the above two metrics showed the same values for two candidates. In case there are no maximum depth constraints for target points then this metric is not needed.

v is the Euclidean norm excluding the preemptive points (similar to δ). This is the last decision metric since it is not a very good predictor, a worse value may give a better result and vice versa. However, if there are two candidates with equal metrics δ, γ, and τ, then ordering of the two candidates may be done based on v. An alternative approach in case of tie-candidates is to choose one of them randomly.

Preemptive points. If some distance δ(S,ti)=1 then we accept the point ti into S immediately without the search through the candidates C. The inclusion of this step in the algorithm forces us to exclude such points from the metrics δ and v.

In [RMTA18a] preemptive points were included into the metric, and we believe it was not correct. E.g., when two distance vectors {1,2, . . . } and {0,2, . . . } have the same projected gates, then they show a totally equal situation in terms of possible shared gates, and they should result in the same δ, because of the distance 1 will be included immediately (preemptive point), so it does not give any advantage over the second choice where we have the distance 0. Thus, distance 1 should not be counted in δ and μ, but it is accounted in the projected gates γ, instead.

**4.2.4 Search Tree**

Additionally to the above algorithm, we propose to have a search tree where each node is a set S with metrics. Children of such a node are also nodes where S′ is derived from S by adding one of the candidate point S ←C. Thus, every path from the root node to a leaf represents a sequence of accepted candidate points to the root set S. If, at some point, a leaf has metric δ=0 then that leaf represents a possible solution path.

We keep a number of children nodes (in our experiments we kept at least 20-50 best children) whose metrics are the best (they may even have different projected gates β). We also define the maximum depth TD of the search tree (in our experiments we tried TD=1 . . . 20). When the tree at depth TD is constructed, we then examine the leaves and see where we get the best metric over all leaves at all different branches. Tracking back to the root, we then choose to keep the top branch that leads to the best leaf(s).

Other top branches from the root are removed. We then advance the root node to the first child of the selected branch and try to extend the tree's depth again from the remaining leafs, thus, keeping the search tree at a constant depth TD.

If, at every depth of the tree, each leaf is extended with additional 20-50 sub-branches, then the number of leaves will increase exponentially. However, we can apply a truncation algorithm to the leaves before extending the tree to the next depth. We simply keep no more than a certain number of promising leaves that will be expanded to the next depth, and other, less promising leaves we just remove from the tree (in our experiments the truncation level was up to 400 leaves overall for the whole tree). This type of truncation makes it possible to select the best top branch of the root node by “looking further” basically at any depth TD. Notably, the complexity does not depend on the depth TD, but it depends on the truncation level.

Truncation strategy. In brief, we keep those leafs with the best metrics, but try to distribute nearly equal leafs among different branches, so that we keep as many diverted solution paths as possible.

**4.2.5 Computation of δ(S,ti)**

The “heart” and the critical part of the algorithm is the algorithm to compute the distances δ(S,ti), given a fresh S. There are many candidates to test at each step, and there are many branches to track, so we need to make this core algorithm as fast as possible.

Note that the length of a point (.p is an integer) is 2n+2 bits, plus the delay value. We will ignore the delay (.d) value when doing Boolean operations over two points. Let us assign the number of possible points as:

N=22n+2.

Let Vk[ ] be a vector of length N cells, each cell Vk[p] corresponds to a (2n+2)-bit point p represented as an integer index, and the value stored in the cell will be the minimum delay p.d of that point such that it can be derived from S with exactly k gates.

Set the initial vector V0 as ∀p→V0[p]=p.d, if p ∈ S, and V0[p]=∞, otherwise. Thereafter, the vector Vk+1 can be derived from the previously derived vectors V0 . . . Vk by applying the allowed 6 gates to points from some level 0≤I<k (VI) and the level k−I (Vk−I), thus resulting in total I+(k−I)+1=k+1 gates. After a new Vk+1 is derived, we simply check if it contains new distance values for the targets from T, and we repeat the procedure until all distances δ(S,ti) for all ti in Tare found. A high-level description of the algorithm is given in Algorithm 1, and in Appendix B.3 we provide a more detailed description alongside multiple computational tricks that can be made.

### 5 Architectural Improvements

Most known AES SBox architectures look quite similar, consisting of the Top and Bottom linear parts, and the middle non-linear part, as previously described in Section 2. In this section, we take that classic design and propose a number of improvements, along with a completely new architecture that focuses on low depths solutions.

**5.1 Two SBox Architectures—Area and Depth**

Referring to FIG. 2, the architecture A (Area) is the classical one that implements designs based on tower and composite fields. It starts with the 8-bit input signal U to the Top linear matrix, which produces a 22-bit signal Q (as in [BP12]). We managed to reduce the number of needed Q-signals to 18, and refactored the multiplication and linear summation block Mul-Sum to 24 gates and depth 3. (See Appendix D.2 for equations). The output from the Mul-Sum block is the 4-bit signal X which is the input to the inversion over GF(24). The output from the inversion, Y, is non-linearly mixed with the Q signals, derived in the top matrix, and produces 18-bit signal N. The final step is the Bottom linear matrix that takes 18-bit N and linearly derives the output 8-bit signal R. The top and bottom matrices incorporate the SBox's affine transformation that depends on the direction. The new architecture D (Depth) (shown in FIGS. 3A and 3B) is a new architecture where we tried to remove the bottom matrix and as a result shrinking the depth of the circuit as much as possible. The idea behind is that the bottom matrix only depends on the set of multiplications of the 4-bit signal Y and some linear combinations of the 8-bit input U. Thus, the result R can be achieved as follows:

R=Y0·M0·U⊕ . . . ⊕Y3·M3·U

where each Mi is a 8×8 matrix representing 8 linear equations on the 8-bit input U, to be scalar multiplied by the Yi-bit. Those 4×8 linear circuits can be computed as a 32-bits signal L in parallel with the circuit for the 4-bits of Y. The result R is achieved by summing up four 8-bit sub-results. Therefore, in architecture D we get the depth 3 after the inversion step (critical path: MULL and 8XOR4 blocks), instead of the depth 5-6 in the architecture A. That new architecture D requires a bit more gates, since the assembling bottom circuit needs 56 gates: 32NAND2+8XOR4. The reward is the lower depth.

A more detailed sketch of the two architectures is given in FIGS. 4 and 5, respectively, that includes the components of the designs, delays and the number of gates.

**5.2 Six Different Scenarios of MULN**

In the MULN block, where the 18-bit N-signals are computed, we need as input the 18-bit Q-signals and the inversion result Y. But we also need the following additional linear combinations of Y: Y02=Y0⊕Y2, Y13=Y1⊕Y3; Y23=Y2 ⊕Y3, Y01=Y0 ⊕Y1, Y00=Y01⊕Y23—these correspond to the signals M41-M45 in [BP12]. Thus, the Y vector is actually extended to 9 bits, and the delays of N bits become different, depending on which of the Yi is used in the multiplication. For example, in the worst case, the delay of Y00 is +2 compared to the delay of Y1. Thus, the resulting signals N will have different output delays. However, it is possible to compute these 5 additional Ys in parallel with the base signals Y0, . . . , Y3. This will cost some extra gates, but then the +2 delay can either shrink down to +1 or +0. In general one can consider the following 6 scenarios:


- - S**0**. We compute only the base signals Y₀ . . . Y₃, and the
    remaining {Y₀₁, Y₂₃, Y₀₂, Y₁₃, Y₀₀} we compute with XORs as above.
    The delay is +2 but it has the smallest number of gates.
  - S**1**. Compute {Y₀₁, Y₂₃} in parallel, the delay is +1.
  - S**2**. Compute {Y₀₂, Y₁₃} in parallel, the delay is +1.
  - S**3**. Compute {Y₀₀} in parallel, the delay is +1.
  - S**4**. Compute {Y₀₁, Y₂₃, Y₀₂, Y₁₃} in parallel, the delay is +1.
  - S**5**. Compute {Y₀₁, Y₂₃, Y₀₂, Y₁₃, Y₀₀} in parallel, the delay is
    +0 as there is no signals left to compute afterwards.

In the next subsection we show how to find Boolean expressions for the above scenarios.

**5.3 INV. Inversion Over GF(24)**

The inversion formulae are as follows:

Y0=X1X2X3⊕X0X2⊕X1 X2⊕X2⊕X3

Y1=X0X2X3⊕X0X2⊕X1X2⊕X1 X3⊕X3

Y2=X0X1X3⊕X0X2⊕X0X3⊕X0⊕X1

Y3=X0X1X2⊕X0X2⊕X0X3⊕X1X3⊕X1

In [BP12] they found a circuit of depth 4 and 17 XORs, but we would like to shrink the depth ever further by utilizing a wider range of standard gates. Thus, we have considered each expression independently, using a general depth 3 expression:

Yi=((Xaop1Xb) op5 (Xcop2Xd)) op7 ((Xeop3Xf) op6 (Xg op4Xh)),

where Xa-h are terms from {0,1,X0,X1,X2,X3} and op1-7 are operators from the set of standard gates {AND, OR, XOR, NAND, NOR, XNOR}. Note that the above does not need to have all terms, for example, the expression AND(x, x) is simply x.

The exhaustive search can be organized as follows. Let us have an object Term which consists of a truth table TT of length 16 bits, based on the 4 bits X0 . . . X3, and a Boolean function that is associated with the term. We start with the initial set of available terms T(0)={0, 1, X0, . . . , X3}, and then construct an expression for a chosen Yi iteratively. Assume at some step k we have the set of available terms T(k), then the next set of terms and associated expressions can be obtained as:

T(k+1)={T(k),T(k) operator T(k)},

taking care of unique terms. At some step k we will get one or more term(s) whose TTs are equal to target TTs (Yis).

Since we could actually get multiple Boolean functions for each Yi then we should select only the “best” functions following the criteria: there is no NOT gates (due to a better sharing capabilities), there is a maximum number of gates that can be shared between the 4 expressions for Y0 . . . Y3, and the area/depth in terms of GE is small.

Using this technique, we have found a depth 3, 15 gates solution for the inversion. The equations are given below, where we also provide depth 3 solutions for the additional 5 signals {Y01, Y23, Y02, Y13, Y00} such that they can also share a lot of gates in the mentioned scenarios S0-S5.

Y0=(X0 and X2) xnor((X1 nand X2) nand (X2xor X3))

Y1((X2xor X3) nand X1) xor ((X0 and X2) nor X3)

Y2=(X0 and X2) xnor ((X0xor X1) nand (X0 nand X3))

Y3=((X0xor X1) nand X3) xor ((X0 and X2) nor X1)

Y01=((X2xor X3) nand X1) nand ((X0 nand X3) nand X2)

Y23=((X0xor X1) nand X3) nand ((X1 nand X2) nand X0)

Y13=((X0 and X2) nor (X1 xnor X3)) xor ((X0 nand X3) xor (X1 nand X2))

Y02=((X2xor X3) nand (X1 nand X2)) xor ((X0xor X1) nand (X0 nand X3))

Y00=((X0 and X2) nand (X1 xnor X3)) and ((X0nor X2) nor (X1 and X3))

When implementing the above circuits for the scenarios S0-S5, and to sharing the gates in a best possible way, we then got the following results:

In our optimal circuits we have used scenario S1, as it showed best results with respect to the area and depth. For the fast and bonus circuits, we used S0 as it has the smallest area.

**5.4 Alpha-Beta Approach for the Top and Bottom Linear Matrices**

We are solving the top matrices with exhaustive search and the bottom matrices with various heuristic techniques. The way those matrices look, naturally influence the final number of gates in the solution. Here we present a simple method to try different top and bottom matrices for the best solution.

Assume that the SBox is a black box and it performs the function (excluding the final addition of the constant):

SBox(x)=x−1·A8×8,

where x−1 is the inverse element in the Rijndael field GF(28), and the matrix A8×8 is the affine transformation. In any field of characteristic 2: squaring, square root, and multiplication by a constant—are linear functions, thus for a non-trivial choice (α,β) we have:

\({Z(x)} = \left( {\alpha \cdot x^{2^{\beta}}} \right)^{- 1}\)
\({{{SBox}(x)} = {\sqrt[2^{\beta}]{\alpha \cdot {Z(x)}} \cdot A_{8 \times 8}}},\)

If the initial Top and Bottom matrices for the forward and inverse SBoxes were TF, BF, TI, FI, respectively, then one can choose any α=1 . . . 255 and β=0 . . . 7, and change the matrices as follows:

T′F=TF·E·Cα·Pβ·E

B′F=E·A·Pβ−1·Cα·A−1·E·BF

T′I=TI·E·A·Cα·Pβ·A−1·E

B′I=E·Pβ−1·Cα·E·BI,

where:

E—is the 8×8 matrix that switches bits endianness (in our circuits input and output bits are in Big Endian)

A—is the 8×8 matrix that performs the SBox's affine transformation

Cα—is the 8×8 matrix that multiplies a field element by the selected constant α

Pβ—is the 8×8 matrix that raises an element of the Rijndael field to the power of 2β

TF/TI—are the original (without modifications) 18×8 matrixes for the top linear transformation of the Forward/Inverse SBoxes, respectively.

BF/BI are the original (without modifications) 8×18 matrixes for the bottom linear transformation of the Forward/Inverse SBoxes, respectively.

There are 2040 choices for (α,β) pair and each choice gives new linear matrixes. It is easy to test all of them and find the best combination that gives the smallest SBox circuit. We have applied this idea to both the forward as well as the inverse SBox, for both architectures A and D.

**5.4.1 Alpha-Beta Approach for the Combined SBox**

For the combined SBoxes we can apply the alpha-beta approach to the forward and the inverse parts independently. This means that we have 20402=4,161,600 variants of linear matrices to test. We have focused on the architecture D, since there is no bottom matrix and thus we can do a more extensive search. We searched through all those 4 million variants and applied the heuristic algorithm from the Section 4.1 as a quick analysis method to select a set of around 4000 promising cases. We then applied the algorithm given in Section 4.2 to find a solution with floating multiplexers. In our case we have n=8 bit input and thus each point is encoded with 18 bits, and the complexity of calculating the distance δ(S,ti) is quadratic over N=218 points. In the search we used the search tree with the maximum depth TD≤20 and the truncation level of 400 leaves.

**5.5 Q-Zero Points for the Top Matrices in the Combined SBox**

The combined SBox needs to have a number of multiplexes for both the top and bottom linear transformations. The top linear matrixes of the forward and inverse SBoxes produce 18-bit signals QF and QI, respectively. This means that normally we should apply 18 multiplexers to switch between the Q-signals, based on the selected direction signal ZF. However, there is a set of Q-triples that are always zero, which are valid for both the forward and the inverse SBoxes:

We can use that knowledge to compute only a subset of Q-signals, then multiplex them and compute the remaining Q-signals using the above zero-points.

For example, we can compute 10 bits: {Q1, Q6, Q8, Q9, Q10, Q12, Q14, Q15, Q16, Q17} for both forward and inverse SBoxes, then apply 10 multiplexers and after that derive the remaining 8 signals as: Q0=Q14+Q15, Q2=Q8+Q9, Q3=Q6+Q8, Q4=Q9+Q10, Q5=Q15+Q17, Q7=Q6+Q10, Q11=Q16+Q17, Q13=Q14+Q16.

Thus, we could save 8 multiplexers and, 2×8 rows of the combined top matrix can be removed. However, we should make sure that exemption of the above 8 bits outside the multiplexers would not increase the depth of the top linear transformation. Note that some of the signals, Q1 and Q12 in the example above, do not participate in computing the final 8 signals, hence those two signals are allowed to have+1 extra depth. I.e., before applying the circuit solver algorithm, we should carefully derive individual maximum delays for each output signal as constraint for a search algorithm.

We have tested 59535 variants of utilizing Q-Zero points, in addition to the above mentioned 2040 choices of (α,β). We applied this method only to the architecture A.

### 6 Results and Comparisons

In this section we present our best solutions for the AES SBoxes, both forward and combined. The stand-alone inverse SBox is perhaps not as widely used, and those results can be found in Appendix C. We compare our area and depth using the techniques described in Appendix A and where possible, we have recalculated the corresponding GE for other academic results for easier comparison. We present three different solutions for each SBox (forward, inverse, and combined): “fast”, “optimal”, and “bonus”. The fast one is the solution with the lowest critical path, the optimal is a well-balanced trade-off between area and speed, and the bonus solution is given to establish a new record in terms of the smallest number of gates. Exact circuit expressions for all the derived solutions can be found in Appendix D, where we also indicate which algorithm was used in deriving the solution.

**6.0.1 Synthesis Results**

We have performed a synthesis of the results and compared with other recent academic work. The technology process is GlobalFoundries 22 nm CSC20L [Glo19], and we have synthesized using Design Compiler 2017 from Synopsys in topological mode with the compile_ultra command. We also turned on the flag compile_timing_high_effort to force the compiler to make as fast circuits as possible. In those graphs, the X axis is the clock period (in ps) and the Y axis is the resulting topology estimated area (in μm2). We have not restricted the available gates in any way, so the to compiler is free to use non-standard gates e.g., a 3 input AND-OR gate. To get the graphs in the following subsections, we have started at a 1200 ps clock period (˜833 MHz) and reduced the clock period by 20 ps until the timing constraints could not be met. We note that the area estimate by the compiler fluctuate heavily, and we believe that this is a result the many different strategies the compiler has to minimize the depth. One strategy might be successful for say a 700 ps clock period, but a different strategy (which results in a significantly larger area) could be successful for 720 ps. There is also an element of randomness involved in the strategies for the compiler.

**6.1 Forward S Boxes**

We have included a number of interesting previous result for comparison in Table 3. The most famous design by Canright is widely used and cited. Our optimal SBox is both faster and smaller. We also included the work done by Boyar et al as their design was the starting point for our research.

The two results from CHES′18 by Reyhani et al are the most recent, and our “optimal” SBox has a similar area as their “lightweight” version in terms of GE, but around 30% faster. The optimal SBox is both smaller and faster than their “fast” circuit. Also, our “fast” version is faster by 25% then their “fast” version, while maintaining a decent area increase. The currently fastest SBox done by Ueno has 286GE and 13.772XORs depth, while our fast version is only 248GE and depth 10.597XORs, outperforming the known fastest circuit by around 23%.

We also included the current world smallest circuit (in terms of standard gates) done by Boyar in 2016, which has 113 gates (231.29GE) and depth 27 gates. Our “bonus” circuit is even smaller with only 108 gates and depth 24, reaching as low as 200.10GE. Synthesize results are shown in FIG. 6.

**6.2 Combined SBoxes**

Table 4 shows our results compared to the two previously known best results. Our optimal combined SBox has a similar size to that of [Can05] and [RMTA18b], but the speed is a lot faster due to a much lower depth of the circuit. The optimal circuit has depth 16 (in reality only 14.413XORs) and 151 gates (296GE), while Canright's combined SBox is of size 150(+2) gates (298GE) and the depth 30 (25.644XORs). The bonus solution in this paper has slightly smaller depth than the most recent result [RMTA18b] but is significantly smaller in size (133 vs 149(+8) standard gates). Finally, the proposed “fast” designs using Architecture D has the best currently known depth, and we include also the one that provided the best synthesis results shown in the comparison in FIG. 7.

### CONCLUSIONS

In this Appendix B we have introduced a number of heuristic and exhaustive search methods for minimizing the circuit realization of the AES SBox. We have proposed a novel idea on how to include the multiplexers of the combined SBox in the minimization algorithms, and derived smaller and faster circuit realizations for the forward, inverse, and combined AES SBox. We also introduced a new architecture where we remove the bottom linear matrix, in order to derive as fast solutions as possible.

## PART C OF THE DISCLOSURE

The results from Part A and Part B can be further extended by a closer investigation of the inversion circuit. The resulting embodiments of the SBox are circuits having an even shorter critical path.

Inversion over GF(24)

The inversion formulae are as follows:

Y0=X1X2X3⊕X0X2 ⊕X1X2⊕X2⊕X3,

Y1=X0X2X3⊕X0X2 ⊕X1X2⊕X1X3⊕X3,

Y2=X0X1X3 ⊕X1X2 ⊕X0X3 ⊕X0⊕X1,

Y3=X0X1X2 ⊕X0X2 ⊕X0X3 ⊕X1X3 ⊕X1.

In [BP12] a circuit of depth 4 and 17 XORs was found, but it is desired to shrink the depth even further by utilizing a wider range of standard gates.

Accordingly, the algorithm from Part B, section 4.2 has been adapted to also find a small solution for the INV block. The idea is simple; each Yi is a truth table of length 16 bits, based on a 4-bit input X0, . . . ,X3. We define our “point” to be a 16-bit value. All standard gates, AND, OR, XOR, MUX, NOT, including their negate versions, can be applied to any combination of “known” points (S), and distances to target points T can be computed in a similar manner as before. Using this slightly modified algorithm for floating multiplexers, a solution was found having only 9 gates and depth 3. The results are shown in Equation 2 and the improved circuits are given in Appendix E.

In case it is desired to avoid multiplexers in the INV block then there is an alternative set of equations that are also presented in this section. Each expression has been considered independently, using a general depth 3 expression:

Yi=((Xaop1Xb) op5 (Xcop2Xd)) op7 ((Xeop3Xf) op6 (Xgop4Xh)),

where Xa-h are terms from {0,1,X0,X1,X2,X3} and op1-7 are operators from the set of standard gates {AND, OR, XOR, NAND, NOR, XNOR}. Note that the above does not need to have all terms, for example, the expression AND(x, x) is simply x.

The exhaustive search can be organized as follows. Let there be an object Term which consists of a truth table TT of length 16 bits, based on the 4 bits X0, . . . ,X3, and a Boolean function that is associated with the term. Starting with the initial set of available terms T(0)={0,1,X0, . . . ,X3}, an expression for a chosen Yi is constructed iteratively. Assume at some step k one has the set of available terms T(k), then the next set of terms and associated expressions can be obtained as:

T(k+1)={T(k),T(k) operator T(k)},

taking care of unique terms. At some step k one will get one or more term(s) whose TTs are equal to target TTs (Yis).

Since it is possible to actually get multiple Boolean functions for each Yi, one should select only the “best” functions following the criteria: there are no NOT gates (due to better sharing capabilities), there is a maximum number of gates that can be shared between the 4 expressions for Y0, . . . , Y3, and the area/depth in terms of GE is small.

Using this technique, we have found a depth 3, 15 gates solution for the inversion. The equations are given below, where depth 3 solutions are also provided for the additional 5 signals {Y01, Y23, Y02, Y13, Y00} such that they can share a lot of gates in the mentioned scenarios S0-S5 in Part B.

Y0=xnor(and(X0,X2),nand(nand(X1,X2),xor(X2,X3)))

Y1=xor(nand(xor(X2,X3),X1),nor(and(X0,X2),X3))

Y2=xnor(and(X0,X2),nand(xor(X0,X1),nand(X0,X3)))

Y3=xor(nand(xor(X0,X1),X3),nor(and(X0,X2),X1))

Y01=nand(nand(xor(X2,X3),X1),nand(nand(X0,X3),X2))

Y23=nand(nand(xor(X0,X1),X3),nand(nand(X1,X2),X0))

Y13=xor(nor(and(X0,X2),xnor(X1,X3)),xor(nand(X0,X3),nand(X1,X2)))

Y02=xor(nand(xor(X2,X3),nand(X1 nand(xor(X0,X1),nand(X0,X3)))X2))

Y00=and(nand(and(X0,X2),xnor(X1nor(nor(X0,X2), and(X1,X3)))X3))

### APPENDIX E

In this section, circuits using the improved inversion formula presented in Part C are presented.

Preliminaries

In the listings presented below, specifications for three circuits for the forward, inverse, and combined SBoxes in the novel architecture D(fast) are described. The symbols used in the following listings are as follows, and have the indicated meanings:


- - \#comment—a comment line
  - @filename—means that the code from another file called ‘filename’
    should be included, the listing of which is then given in this
    section as well.
  - a{circumflex over ( )}b—is the usual XOR gate; other gates are
    explicitly denoted and taken from the set of {XNOR, AND, NAND, OR,
    NOR, MUX, NMUX, NOT}
  - (a op b)—where the order of execution (the order of gates
    connections) is important we specify it by brackets.

The inputs to all SBoxes are the 8 signals {U0 . . . U7} and the outputs are the 8 signals {R0 . . . R7}. The input and output bits are represented in Big Endian bit order. For combined SBoxes the input has additional signals ZF and ZI where ZF=1 if one performs the forward SBox and ZF=0 if inverse, otherwise; the signal ZI is the compliment of ZF. All the proposed circuits have been tested and their correctness verified.

The circuits are divided into sub-programs that correspond, respectively, to the functions/layers shown in FIG. 5. The discussion starts with a description of the common shared components, and then for each solution the components (common or specific) for the circuits are described.

Shared Components

The shared components are used in several implementations in the following and thus described only once here.

Forward SBox (Fast)

Combined SBox (Fast)

Inverse SBox (Fast)

