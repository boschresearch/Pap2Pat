# DESCRIPTION

This application is the National Stage of International Application No. PCT/EP2018/069210, filed Jul. 16, 2018, which claims the benefit of European Patent Application No. EP17181687.9, filed Jul. 17, 2017. The entire contents of these documents are hereby incorporated herein by reference.

## BACKGROUND

The present embodiments relate to a method and a system for automatic discovery of topics within temporal ordered text document collections.

Topic detection and tracking systems perform natural language processing to find topics over time in a sequence of text collections that exhibit temporal relationships. Probabilistic topic models have been used in the past to extract semantic topics from text documents. Probabilistic topic models such as Latent Dirichlet Allocation LDA have been investigated to examine the emergence of topics from a sequence of text documents. These conventional methods compute a topic distribution on all text collections to detect and track different topics. However, these conventional methods do not take into account the dependencies between different text collections over time in an evolutional process. Accordingly, conventional methods do not take into account temporal latent topic dependencies between topic collections evolving over time and forming a temporal sequence of text document collections. Consequently, conventional methods cannot capture topic trends and/or keyword trends accurately.

## SUMMARY AND DESCRIPTION

The scope of the present invention is defined solely by the appended claims and is not affected to any degree by the statements within this summary.

The present embodiments may obviate one or more of the drawbacks or limitations in the related art. For example, I a method and system for providing a precise topic detection and tracking within temporal ordered text document collections are provided.

The present embodiments provide, according to a first aspect, a method for automatically performing a discovery of topics within temporal ordered text document collections. The method includes generating a bag of words vector for each text document collection using a predefined dictionary. Based on the generated bag of words vectors, a hidden topic vector representing topics of the respective text document collection is iteratively calculated for each text document collection using a calculated hidden state vector memorizing a hidden state of all previous text document collections.

In a possible embodiment of the method according to the first aspect, topic trends are derived from the calculated hidden topic vectors of the text document collections.

In a further possible embodiment of the method according to the first aspect, each text document collection includes one or more text documents published or output at the same time and including an associated time stamp indicating the time of publication or output.

In a further possible embodiment of the method according to the first aspect, a sequence of text document collections is sorted according to the associated time stamps to assign time steps to the text document collections.

In a further possible embodiment of the method according to the first aspect, a hidden topic vector ht representing topics of a text document collection at a time step t is calculated from the bag of words vector vt of this time step t and from the hidden state vectors ut-1 of the preceding time step t-1, which is computed from the hidden topic vector ht-1 at that preceding time step t-1 and a preceding hidden state vectors ut-2 at time step t-2.

In a further possible embodiment of the method according to the first aspect, the calculated hidden topic vector h of a text document collection includes a hidden topic probability vector indicating occurrence probabilities of different topics within the respective text document collection.

In a further possible embodiment of the method according to the first aspect, the generated bag of words vector of a text document collection indicates occurrence numbers of words within the respective text document collection.

In a still further possible embodiment of the method according to the first aspect, a two-layered recurrent neural network, RNN,-replicated softmax model, RSM, is used to calculate the hidden topic vectors for the text document collections of a sequence of text document collections.

In a still further possible embodiment of the method according to the first aspect, the two-layered RNN-RSM model includes an RSM layer including time-ordered hidden state vectors and associated bag of words vectors for text document collections and an RNN hidden layer including the hidden state vectors.

In a further possible embodiment of the method according to the first aspect, the discovered topics are automatically evaluated to control a process.

In a further possible embodiment of the method according to the first aspect, the text document collection includes text files including words of a natural language consisting of characters.

In a still further possible embodiment of the method according to the first aspect, the text document collection includes source code files written in a programming language.

In a still further possible embodiment of the method according to the first aspect, the text document of a text document collection describes features of a technical system.

The present embodiments further provide, according to a second aspect, a topic discovery system.

The present embodiments provide, according to the second aspect, a topic discovery system for automatic discovery of topics and trends within temporal ordered text document collections. The topic discovery system includes a repository that stores temporal ordered text document collections and a processor configured to generate a bag of words vector for each text document collection using a predefined dictionary. The processor is also configured to iteratively calculate for each text document collection a hidden topic vector representing topics of the respective text document collection based on the generated bag of words vectors using a calculated hidden state vector memorizing a hidden state of all previous text document collections.

In a possible embodiment of the topic discovery system according to the second aspect, the processor is further adapted to automatically derive topic trends from the discovered topics of the text document collections.

In a further possible embodiment of the topic discovery system according to the second aspect, the topic discovery system includes an interface to output the discovered topics and/or topic trends.

### DETAILED DESCRIPTION

As shown in the block diagram of FIG. 1, a topic discovery system 1 according to an aspect may include, in a possible embodiment, several (e.g., three or more) main components. The topic discovery system 1, as shown in FIG. 1, provides an automatic discovery of topics and trends within temporal ordered text document collections. In the illustrated embodiment of FIG. 1, the topic discovery system 1 includes a repository or database where the timestamped or temporal ordered text document collections are stored. In the illustrated embodiment of FIG. 1, the repository 2 includes a local memory or database that stores timestamped or already temporal ordered or sorted text document collections. In an alternative embodiment, the repository or database 2 may be a remote database connected to the topic discovery system 1. In the shown embodiment of FIG. 1, the topic discovery system 1 includes a processing unit or a processor 3 having access to the database or repository 2 where the timestamped or temporal ordered text document collections TDCs are stored. The processor 3 has further access in the illustrated embodiment to a memory 4 storing a two-layered RNN-RSM model that may be used for calculating hidden topic vectors h by the processor 3. The processor 3 is adapted first to generate a bag of words vector v for each text document collection TDC using a predefined dictionary. In a possible implementation, the predefined dictionary DIC may be stored in a further memory 5, as shown in FIG. 1. The processor 3 is further adapted to iteratively calculate for each text document collection TDC stored in the database 2 a hidden topic vector h representing topics of the respective text document collection TDC based on the generated bag of words vectors v using a calculated hidden state vector u memorizing a hidden state of all previous text document collections TDCs. In a possible embodiment, the processor 3 is further adapted to automatically derive topic trends from the discovered topics of the text document collections TDCs. In the illustrated embodiment of FIG. 1, the topic discovery system 1 further includes an interface 6 for outputting the discovered topics and/or topic trends.

Each text document collection TDC stored in the repository 2 may include one or more text documents or text files. Each text document may include a plurality of words, where each word may consist of characters. Each text document collection TDC includes one or more text documents that have been published or output by a system at the same time. Accordingly, each text document collection TDC includes, in an embodiment, an associated time stamp TS. This time stamp TS may be automatically generated in a possible embodiment when the text documents of the text document collection TDC are published or output by the system. In a further possible embodiment, the time stamps TS are assigned by a user when the text documents of the text document collection TDC are published or output. The time stamps TS indicate a time of publication or a time of outputting the text documents. Each text document collection TDC may include an individual plurality of different kinds of text documents. In a possible embodiment, the text documents include text files including words of a natural language, where each word consists of one or several characters (e.g., one or more characters). In a possible implementation, the text document collection TDC may also include source code files written in a programming language. Each text document of a text document collection TDC describes one or several features of a technical system in a possible implementation. This technical system may, for example, be a machine or a technical assembly of one or several (e.g., one or more) components. These components may include hardware components and/or software components.

In a possible embodiment, the text documents of a text document collection TDC are generated automatically by a text document generation unit. In an alternative embodiment, the text documents are generated by a user using a keyboard or by a voice recognition system. In a possible embodiment, the text documents are timestamped and temporally ordered. All text documents having the same time stamp TS belong to the same text document collection TDC. In a possible embodiment, the different text document collections TDCs each including one or several (e.g., one or more) text documents are sorted in a temporal order according to the corresponding time stamps TS. In a possible implementation, the text document collections TDCs are ordered according to the time when the text document collections TDCs have been published or output by a technical system. In an alternative embodiment, the text document collections TDCs are ordered according to the time when the text document collections TDCs have been generated or produced. The text documents belonging to the same text document collection TDC include the same time of production and/or the same time of publication. For example, a text document collection TDC may include a number N of text documents having been output or published by a system within the same day, week, or year. Further, each text document collection TDC may also include all text documents that have been output by a technical system within the same periodic time interval of, for example, within the same minute. Time stamps TS are automatically generated and assigned to the different text documents generated or output at the same time or within the same time period of a predefined time grid. Different text documents having the same time stamps TS are collected within a text document collection TDC. Further, the different text document collections TDCs each having an associated time stamp TS may be stored in the database 2 and may then be sorted or ordered according to the corresponding time stamps. In a possible implementation, text document collections TDCs may belong to a series of text documents published by the same medium such as a newspaper or a technical journal. For example, the different text documents may include different articles or files of a periodically published technical journal. However, the text documents may also belong to documentation documents documenting a technical system or a group of text documents generated by a machine for monitoring purposes. Another example for a series of text documents are reports generated by a user. For example, a doctor may document a healing process of a patient by generating associated text documents. For example, the doctor may dictate health reports that are converted automatically into associated text documents with corresponding time stamps. Text documents of the same day or week may be sampled to form part of a text document collection TDC. Accordingly, the text document collection TDC may include several (e.g., three or more) text documents describing a patient's progress over time.

Accordingly, each text document collection TDC may include one or more text documents generated or published at the same time or within the same time period and including an associated time stamp TS indicating the respective time of generation or publication. A sequence of text document collections TDCs may be sorted automatically according to the associated time stamps TS to assign time steps to the different text document collections TDCs.

The processor or processing unit 3 of the topic discovery system 1, as shown in FIG. 1, generates in a first processing act a bag of words vector v for each text document collection TDC by using a predefined dictionary DIC stored in the memory 5, as shown in FIG. 1. In a possible embodiment, the topic discovery system 1 uses a single dictionary (e.g., the dictionary of common English words including several thousand different common words used in the English language). This dictionary may, for example, include 65,000 common words used in the natural language English. The generated bag of words vector v of a text document collection TDC indicates occurrence numbers of different words within the respective text document collection TDC. For example, a word may be used a hundred times in the text document collection TDC, and another word has not been used at all. The corresponding entry within the bag of words vector v indicates how often the respective word has occurred within the text document collection TDC. In a further possible embodiment, several different dictionaries DIC may be stored in the memory 5. In a possible implementation, the dictionary DIC may be selected from a set of dictionaries stored in the memory 5 according to a topic domain and/or depending on the language of the text documents. For example, if the topic domain collection TDC includes only text documents in English, an English word dictionary DIC is selected. If the topic domain collection includes further natural languages, other dictionaries may be selected as well. Further, the text document collections TDCs may include natural language documents but also text documents written in predefined technical languages (e.g., programming languages). In a possible implementation, the type of the text documents forming part of the text document collections TDC is indicated, and a matching dictionary DIC is automatically selected. After one or several dictionaries (e.g., one or more dictionaries) have been selected, the processor 3 may automatically generate a bag of words vector v for each text document collection TDC using the selected dictionaries DIC. In a further processing act, the processing unit 3 may, based on the generated bag of words vectors v, calculate for each text document collection TDC read from the memory 2 iteratively a hidden topic vector h representing topics of the respective text document collection TDC using a calculated hidden state vector u that does memorize a hidden state representing previous text document collections TDC.

After having calculated the hidden topic vector for each text document collection TDC, the processing unit 3 may, in a further processing act, automatically derive topic trends from the calculated hidden topic vectors of the text document collections TDCs. In a possible embodiment, topic trends are output by the topic discovery system 1 via the interface 6 for further processing and/or for performing an automatic control of a system. In a possible embodiment, the discovered topics may be further automatically processed or evaluated to generate control signals output via the interface 6 to control actuators of a technical system. In a further possible embodiment, a text document of a text document collection TDC may also be input into the topic discovery system 1, as shown in FIG. 1, via the interface 6. The input text documents are stored in the database 2 according to corresponding assigned time stamps. In a further alternative embodiment, the text document collection TDC is not read by the processing unit 3 from a memory 2, as shown in FIG. 1, but is received via an interface in a text document collection data stream. In this alternative embodiment, timestamped text document collections TDCs may be received in a temporal order or sequence via a data network connected to the topic discovery system 1.

The processing unit 3 is adapted to calculate a hidden topic vector h representing topics of the different text document collections TDCs using a model stored in the local memory 4, as shown in FIG. 1. In a possible embodiment, a hidden topic vector ht representing topics of a text document collection TDC at a time step t is calculated from the bag of words vector vt of this time step t and from the hidden state vector ut-1 of the preceding time step t-1. The hidden state vector ut-1 of the preceding time step t-1 is computed in an exemplary embodiment from the hidden topic vector ht-1 at the preceding time step t-1 and a preceding hidden state vector ut-2 at a time step t-2. The calculated hidden topic vector h of a text document collection TDC includes, in a possible embodiment, a hidden topic probability vector indicating an occurrence probability of the different topics within the respective text document collections TDCs.

In a possible embodiment, the method uses a two-layered recurrent neural network, RNN-replicated softmax model RSM to calculate the hidden topic vectors h for the text document collections TDCs of a sequence of text document collections TDCs. This two-layered RNN-RSM model includes, in an embodiment, an RSM layer including time-ordered hidden state vectors and associated bag of words vectors v for all text document collections TDCs and also an RNN hidden layer including the hidden state vector u.

Such a two-layered RNN-RSM model is illustrated in FIG. 3. The model shown in FIG. 3 may be stored in a local memory 4 of the topic discovery system 1 and may include a two-layered model structure. The model shown in FIG. 3 includes an RSM layer and an RNN layer. The RSM layer includes the time-ordered hidden state vectors h and associated bag of words vectors v. The two-layered model further includes an RNN hidden layer including the hidden state vectors u, as shown in FIG. 3.

In the illustrated embodiment of FIG. 3, the model used by the processing unit 3 includes an RNN-RSM model, a sequence of conditional RSMs such that at any time step t, the bias parameters bv and bh of the RSM depend on the output of a deterministic RNN with hidden layer ut-1 in the previous time step t-1. The bag of words vectors v form visible portions. The V units are multinominal, while the h units are stochastic binary. The RNN hidden units u are constrained to convey temporal information, while the RSM hidden units h model conditional distributions. Consequently, parameters bv, bh Wvh are time-dependent on the sequence history at time t (e.g., via a series of conditional RSMs) noted by θt, where θt={vτ, uτ|τ<t}, which captures temporal dependencies. The

RNN-RSM model may be defined by a joint probability distribution:

\(\begin{matrix}
{{P\left( \left\{ {V,H} \right\} \right)} = {\prod\limits_{t = 1}^{\tau}\; {P\left( {v^{(t)},{h^{(t)}\theta^{(t)}}} \right)}}} & (1)
\end{matrix}\)

where V=[v1 . . . vt] and

H=[h1 . . . ht],

and where ht∈{0, 1} is a binary stochastic hidden topic and vt∈{1, . . . K}D is the discrete visible unit. K is a dictionary size, and D is the number of documents published at the same time.

The conditional distribution in each RSM at time step t may be given by a softmax and logistic functions as follows:

\(\begin{matrix}
{{p\left( {v_{i}^{k,{(t)}} = {1h^{(t)}}} \right)} = \frac{\exp \left( {b_{vi}^{k,{(t)}} + {\sum\limits_{j = 1}^{F}\; {h_{j}^{(t)}W_{ij}^{k}}}} \right)}{\sum\limits_{q = 1}^{k}\; {\exp \left( {b_{vi}^{q,{(t)}} + {\sum\limits_{j = 1}^{F}\; {h_{j}^{(t)}W_{ij}^{k}}}} \right)}}} & (2) \\
{{p\left( {h_{j}^{(t)} = {1v^{(t)}}} \right)} = {\sigma \left( {b_{h}^{(t)} + {\sum\limits_{i = 1}^{D}\; {\sum\limits_{k = 1}^{K}\; {v_{i}^{k,{(t)}}W_{ij}^{k}}}}} \right)}} & (3)
\end{matrix}\)

where p(ik,(t)=1|h(t)) and p(hj(t)=1|v(t)) define the conditional distributions for a visible unit, vi and hidden unit hj at time step t. vk,(t) is sampled D times with identical weights connecting to binary hidden units, resulting in multinominal visibles and, therefore, the name Replicated Softmax.

While biases b of RSM depend on the output of RNN at previous time steps that allows to propagate the estimated gradient at each RSM (with respect to biases) backward through time (BPTT), the RSM biases at each time step t are given by:

bv(t)=bv+Wuvu(t-1); bh(t)=bh+Wuhu(t-1)   (4)

where Wuv and Wuh are the weight parameters between hidden unit u and input v, and u and h, respectively. The RNN hidden state u(t) may be computed by:

u(t)=tanh(bu+Wuuu(t-1)+Wuvv(t))  (5)

where bu is the bias of u. Wuu is the weight parameter between RNN hidden units, while Wvu is the weight parameter between the visible unit v and hidden unit u.

RSM is an energy-based model, where energy of the state {v(t), h(t)} at time step t is given by:

E(v(t), h(t))=−Σj=1FΣk=1KhjWjk{circumflex over (v)}k−Σk=1K{circumflex over (v)}kbvk−DΣj=1Fbhjhj   (6)

{circumflex over (v)}k=Σi=1Dvik denotes the count for the kth word. The energy and probability are related by:

\(\begin{matrix}
{{P\left( v^{(t)} \right)} = {\frac{1}{Z}\Sigma_{h^{(t)}}\mspace{14mu} {\exp \left( {- {E\left( {v^{(t)},h^{(t)}} \right)}} \right)}}} & (7)
\end{matrix}\)

where Z=ΣvΣhexp(−E(v(t), h(t)) is a normalization constant.

In a further possible embodiment, the RNN-RSM model may be trained. In a possible embodiment, the RNN-RSM model may be trained with BPTT.

The cost function in RNN-RSM model is given by C≡−log P(v(t)). Training with respect to nine parameters (Wuh, Wvh, Wvu, Wuu, bv, bh, bv(t), bh(t), u(0)) may follow in a possible embodiment with the following acts at each iteration: 1. Propagate deterministic hidden units u(t) in RNN portion using equation (5); 2. Compute RSM parameters bv(t) and bh(t), dependent on RNN hidden units, in equation (4); 3. Reconstruct the visibles (e.g., negative samples v(t)* using k-step Gibbs sampling); 4. Estimate the gradient of the cost C using the negative samples as:

\(\begin{matrix}
{\frac{\partial C}{\partial\theta^{(t)}} \simeq {\frac{\partial{F\left( v^{(t)} \right)}}{\partial\theta^{(t)}} - \frac{\partial{F\left( v^{{(t)}*} \right)}}{\partial\theta^{(t)}}}} & (8)
\end{matrix}\)

where the free energy F(v(t)) is related to normalized probability of v(t) as P(v(t))≡exp−F(v)/Z and is given by:

F(v(t))−Σk=1Kvk(t)bvk−ΣFj=1log(1+exp(Dbhj+Σk=1Kvk(t)Wjk))   (9)

The gradient with respect to RSM parameters is approximated by Contrastive Divergence (CD); using equations (8) and (9):

\(\begin{matrix}
{\mspace{76mu} {{\frac{\partial C}{\partial b_{v}^{(t)}} \simeq {v^{{(t)}*} - v^{(t)}}}{\frac{\partial C}{\partial b_{h}^{(t)}} \simeq {{\sigma \left( {{Wv}^{{(t)}*} - b_{h}^{(t)}} \right)} - {\sigma \left( {{Wv}^{(t)} - b_{h}^{(t)}} \right)} - \frac{\partial C}{\partial W_{vh}}} \simeq {{\sum\limits_{t = 1}^{T}\; {{\sigma \left( {{Wv}^{{(t)}*} - b_{h}^{(t)}} \right)}v^{{(t)}*}}} - {{\sigma \left( {{Wv}^{t} - b_{h}^{t}} \right)}v^{t}}}}}} & (10)
\end{matrix}\)

At each iteration, the training may also include: 5. Back-propagate the estimated gradient with respect to RSM biases via hidden-to-bias parameters to compute gradients with respect to deterministic RNN connections (Wuv, Wuu, Wvu, u0) and biases (bv, bh).

In a possible implementation, an average span of selected keywords may be calculated as follows:

\(\begin{matrix}
{{{span}_{avg}(Q)} = {\frac{1}{Q}\Sigma_{i \in Q}\frac{{span}_{i}}{v^{i}}}} & (11)
\end{matrix}\)

where Q is the set of words appearing in topics over the years extracted by the topic model. The used RNN-RSM model captures longer spans for keywords or trends compared to conventional models. The RNN-RSM model may be used for temporal topic modeling and/or for trend analysis.

The method and system 1 according to one or more of the present embodiments may be used for a variety of use cases. The method and system 1 for providing automatic topic discovery of topics may be used for any kind of temporal ordered text document collections TDC published or generated over time. The method and system 1 may be used for detecting topics and for tracking different topics over time. The detected topic may trigger a control or monitoring routine for a technical system. Further, the detected topic or trend may trigger a process such as a repair or maintenance process for a machine. Further, the discovered topics may be evaluated or processed to calculate automatically trends within the text document collections TDC to make predictions for the future development within a technical domain or for an investigated technical system. The text documents sorted in the ordered sequence of text document collections TDC may originate from the same or different text-generating sources. The text documents may be produced by different users and/or generated by different technical hardware or software components of a technical system. The method and system 1 according to one or more of the present embodiments are able to capture longer trends of discovered topics over time, allowing to make more accurate predictions and to initiate more suitable measures or processes depending on the discovered topics.

The elements and features recited in the appended claims may be combined in different ways to produce new claims that likewise fall within the scope of the present invention. Thus, whereas the dependent claims appended below depend from only a single independent or dependent claim, it is to be understood that these dependent claims may, alternatively, be made to depend in the alternative from any preceding or following claim, whether independent or dependent. Such new combinations are to be understood as forming a part of the present specification.

While the present invention has been described above by reference to various embodiments, it should be understood that many changes and modifications can be made to the described embodiments. It is therefore intended that the foregoing description be regarded as illustrative rather than limiting, and that it be understood that all equivalents and/or combinations of embodiments are intended to be included in this description.

