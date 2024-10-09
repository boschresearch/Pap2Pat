# DESCRIPTION

## TECHNICAL FIELD

The present disclosure relates generally to natural language processing and more specifically to improving abstraction of text summarization.

## BACKGROUND

The subject matter discussed in the background section should not be assumed to be prior art merely as a result of its mention in the background section. Similarly, a problem mentioned in the background section or associated with the subject matter of the background section should not be assumed to have been previously recognized in the prior art. The subject matter in the background section merely represents different approaches, which in and of themselves may also be inventions.

In recent times, a fundamental change has occurred in the way that people take in new information. The bottleneck is no longer access to information; rather, it is the ability of people to keep up with all of the information directed to them, for example, through their jobs, the news, social media, etc. To help people with this information deluge, artificial intelligence techniques can be applied, for example, to perform text summarization.

Text summarization is the task of compressing a long sequence of text into a more concise version. For a text summary to be considered high quality, the summary should have certain characteristics: it should be shorter than the original document; it should convey only the most important information; it should accurately reproduce the factual information of the source document and not include any external knowledge; and it must be semantically and syntactically correct. The two most common approaches to text summarization are extractive and abstractive. With extractive text summarization, salient parts of the source document are extracted and included in the summary without change. With abstractive text summarization, not only are salient parts of the source document extracted, but they are also concisely paraphrased.

In the figures, elements having the same designations have the same or similar functions.

## DETAILED DESCRIPTION

This description and the accompanying drawings that illustrate aspects, embodiments, implementations, or applications should not be taken as limiting the claims define the protected invention. Various mechanical, compositional, structural, electrical, and operational changes may be made without departing from the spirit and scope of this description and the claims. In some instances, well-known circuits, structures, or techniques have not been shown or described in detail as these are known to one skilled in the art. Like numbers in two or more figures represent the same or similar elements.

In this description, specific details are set forth describing some embodiments consistent with the present disclosure. Numerous specific details are set forth in order to provide a thorough understanding of the embodiments. It will be apparent, however, to one skilled in the art that some embodiments may be practiced without some or all of these specific details. The specific embodiments disclosed herein are meant to be illustrative but not limiting. One skilled in the art may realize other elements that, although not specifically described here, are within the scope and the spirit of this disclosure. In addition, to avoid unnecessary repetition, one or more features shown and described in association with one embodiment may be incorporated into other embodiments unless specifically described otherwise or if the one or more features would make an embodiment non-functional.

Neural networks have demonstrated great promise as a technique for automatically analyzing real-world information with human-like accuracy. In general, neural network models receive input information and make predictions based on the input information. Whereas other approaches to analyzing real-world information may involve hard-coded processes, statistical analysis, and/or the like, neural networks learn to make predictions gradually, by a process of trial and error, using a machine learning process. A given neural network model may be trained using a large number of training examples, proceeding iteratively until the neural network model begins to consistently make similar inferences from the training examples that a human might make. Neural network models have been shown to outperform and/or have the potential to outperform other computing techniques in a number of applications. According to some embodiments, a neural network is employed to perform the task of abstractive text summarization.

Abstractive text summarization attempts to shorten (condense and rephrase) a long textual document into a human readable form that contains the most important facts from the original document. A high quality summary of a text document is usually shorter than the original document, conveys only the most important and no extraneous information, and is semantically and syntactically correct. Moreover, the summary should use novel phrases with words that do not necessarily appear in the source document in order to concisely paraphrase the meaning—in other words, abstractive. Existing abstractive text summarization techniques tend to replicate or copy long passages of the source document directly into the summary, thereby producing summaries that are not really abstractive.

In this disclosure, an approach is provided to improve the level of abstraction of summaries generated for respective text documents. According to some embodiments, systems and methods are disclosed herein for a neural network model generating an abstractive text summarization from a source document. The level of abstraction of the text summarization generated by this model is improved as compared to other text summarization models.

In some embodiments, the neural network abstractive summarization model comprises a decoder that is decomposed into a contextual model and a language model. The contextual model retrieves relevant parts of the source document, and is responsible for extracting and compacting the source document. The language model is responsible for the generation of concise paraphrases for the text summarization of the source document. The neural model can be pretrained so that it incorporates prior knowledge about language generation.

In some embodiments, the neural network abstractive summarization model implements or uses a novelty metric, which serves as a reinforcement learning reward to encourage summary abstraction by the neural network model. The novelty metric can be optimized directly through policy learning to encourage the generation of novel phrases for summarizing the text document. In some embodiments, the novelty metric can be used in conjunction with a policy that rewards word-overlap with the ground-truth summary to encourage correctness in the text summarization.

With these techniques, and others described herein, the neural model of this disclosure generates a concise summary of a source text document without replicating long passages from the source document. Summarization models can be evaluated using metrics for word overlap with ground-truth summaries, such as in the form of ROUGE scores, as described in further detail in Lin, “Rouge: A package for automatic evaluation of summaries,” in Proc. ACL workshop on Text Summarization Branches Out, 2004, p. 10, which is incorporated by reference herein. Because word-overlap metrics do not capture the abstractive aspect of high quality summaries, other metrics such as n-gram overlap can be applied to evaluate text summaries. Experiments and validation tests (for example, on the CNN/Daily Mail dataset) show that the neural network model of this disclosure achieves results comparable to the state-of-the-art models (as determined by the ROUGE metric) while achieving a significantly higher level of abstraction as measured by n-gram overlap with the source document. In other words, the abstractive summarization model of this disclosure generates summaries that are much more abstractive that previous approaches, while maintaining high ROUGE scores close to or above the state-of-the-art.

The neural network model of the present disclosure can be implemented in a computing device. FIG. 1 is a simplified diagram of such a computing device 100 according to some embodiments. As shown in FIG. 1, computing device 100 includes a processor 110 coupled to memory 120. Operation of computing device 100 is controlled by processor 110. And although computing device 100 is shown with only one processor 110, it is understood that processor 110 may be representative of one or more central processing units, multi-core processors, microprocessors, microcontrollers, digital signal processors, field programmable gate arrays (FPGAs), application specific integrated circuits (ASICs), graphics processing units (GPUs) and/or the like in computing device 100. Computing device 100 may be implemented as a stand-alone subsystem, as a board added to a computing device, and/or as a virtual machine.

Memory 120 may be used to store software executed by computing device 100 and/or one or more data structures used during operation of computing device 100. Memory 120 may include one or more types of machine readable media. Some common forms of machine readable media may include floppy disk, flexible disk, hard disk, magnetic tape, any other magnetic medium, CD-ROM, any other optical medium, punch cards, paper tape, any other physical medium with patterns of holes, RAM, PROM, EPROM, FLASH-EPROM, any other memory chip or cartridge, and/or any other medium from which a processor or computer is adapted to read.

Processor 110 and/or memory 120 may be arranged in any suitable physical arrangement. In some embodiments, processor 110 and/or memory 120 may be implemented on a same board, in a same package (e.g., system-in-package), on a same chip (e.g., system-on-chip), and/or the like. In some embodiments, processor 110 and/or memory 120 may include distributed, virtualized, and/or containerized computing resources. Consistent with such embodiments, processor 110 and/or memory 120 may be located in one or more data centers and/or cloud computing facilities. In some embodiments, memory 120 may include non-transitory, tangible, machine readable media that includes executable code that when run by one or more processors (e.g., processor 110) may cause the one or more processors to perform the methods described in further detail herein.

As shown, memory 120 includes a neural network 130. Neural network 130 may be used to implement and/or emulate any of the neural networks described further herein. In some examples, neural network 130 may include a multi-layer or deep neural network. In some embodiments, the neural network 130 is implemented with or incorporates a recurrent neural network (RNN), with encoder-decoder architecture. Each of the encoder and decoder modules may include or be implemented with Long Short-Term Memory (LSTM) units.

Neural network 130 implements or incorporates a system or model, and corresponding methods, for abstractive text summarization, as described herein. In some embodiments, the abstractive text summarization system or model of the neural network 130 may be used to provide an abstractive text summarization of a textual document. In some embodiments, the neural network 130 includes modules or processes to iteratively train and/or evaluate the system or model used to generate an abstractive text summarization of a textual document.

In some embodiments, the neural network 130 implements a mixed objective that jointly optimizes the n-gram overlap with the ground-truth summary while encouraging abstraction. This can be accomplished by combining maximum likelihood estimation with policy gradient. The policy is rewarded with the ROUGE metric, which measures word-overlap with the ground-truth summary to encourage correctness, as well as a novel abstraction reward that encourages the generation of words not in the source document.

As shown, computing device 100 receives a textual document 140, which is provided to neural network 130. Neural network 130 then generates an abstractive text summarization 160 based on the textual document 140. The neural network 130 can be trained on various datasets, as described below in more detail. According to some embodiments, also as described in further detail below, a novelty metric is employed or implemented to reward the neural network model 130 for generating words for the summary that are not in the source document.

FIG. 2 is a simplified diagram of an architecture for a neural network model 200 generating abstractive text summarization according to some embodiments. The neural network model 200 of FIG. 2 can be an implementation of the neural network 130 (FIG. 1). As shown in FIG. 2, the neural network 200 includes an encoder 210, a decoder 220, and a fusion layer 250. And FIG. 3 shows a corresponding method 300 for the neural network model illustrated in FIG. 2.

With reference to FIGS. 2 and 3, the method 300 starts with a process 310. At process 310, the neural model 200 receives as input a source textual document (e.g., textual document 150). The source document henc comprises a number (n) of words (e.g., “An unusual event took . . . ”).

At a process 320, the encoder 210 of the neural model encodes or embeds the words of the source document 150, for example, by mapping each word in the document to a vector space or matrix. In some embodiments, to accomplish the encoding or embedding, the encoder 210 is implemented with or incorporates one or more long-term short-term memory (LSTM) encoders 212. In some embodiments, the encoder 210 encodes the input sequence, for example, with each LSTM 212 taking in a respective word of the source document and outputting a respective vector 214. The encoder 210 is run forward so that information generated by an LSTM encoder 212 operating on a word appearing earlier in the source document is passed to an LSTM encoder 212 operating on a word appearing later in the sequence. This allows the hidden vectors of the later LSTM encoders 212 to incorporate information for the earlier words. In some embodiments, the encoder 210 is also run backwards so that the LSTM encoders 212 can generate or output vectors that incorporate information from words that appear later in the sequence. These backwards output vectors can be concatenated with the forward output vectors to yield a more useful hidden vector. Each pair of forward and backward LSTM encoders can be treated as a unit, and is typically referred to as a bidirectional LSTM. A bidirectional LSTM encoder incorporates information that precedes and follows the respective word.

The encoder 210 with bidirectional LSTMs 212 takes in a sequence of words from the source document 150, runs a forward and a backward LSTM operation, concatenates the outputs corresponding to the same input, and returns the resulting sequence of vectors or encodings h.

Let Eϵn×d denote the matrix of demb dimensional word embeddings of the n words in the source document. The encoding of the source document henc is computed via BiLSTM whose output has dimension dhid.

henc=BiLSTM(E)∈d  (1)

Encoder 210 generates a temporal attention context at time t, cttmp. The output or final states from encoder 210 are passed or provided to decoder 220.

In order to produce an abstractive summarization of the source document, the neural network model 200 cannot exclusively copy from the text document. Instead, the model should parse chunks of the source document and create concise summaries using phrases not in the source document. To accomplish this, the decoder 220 operates to extract relevant parts of the source document through the pointer network as well as to compose paraphrases from a fixed vocabulary. According to embodiments of the present disclosure, these two operations or responsibilities are decoupled or separated.

Thus, as shown in FIG. 2, the decoder 220 is factorized into separate models—a contextual model 222 and a language model 224. The language model 222 assumes responsibility of generating words for the summary from the fixed vocabulary, thus allowing the contextual model 224 of the decoder 220 to focus on attention and extraction of words from the source document. This decoupling or decomposition of operations in the decoder 220 also allows the may have the language model 224 to be pre-trained on other large scale text corpora, thus providing the added benefit of incorporating into the neural model 200 external knowledge about fluency or domain specific styles.

At a process 330, the contextual model 222 of the decoder 220 extracts words from and compacts the source textual document 150. Contextual model 222 uses or incorporates an encoder which, in some embodiments, can be implemented as a single LSTM recurrent neural network (RNN) comprising encoders 226. LSTM RNN computes hidden states from the embedding vectors. The recurrent attentive decoder 220 is initialized with an ultimate hidden state from the encoder 210 and a special start-of-summary token to produce decoder hidden states at successive decoding steps.

In some embodiments, the contextual model 222 uses, incorporates, or implements an encoder temporal attention. The encoder temporal attention penalizes input tokens that previously had high attention scores. Let htdec denote the decoder state at time t. The encoder temporal attention context at time t, cttmp, is computed as:

\(\begin{matrix}
{s_{ti}^{tmp} = {{\left( h_{t}^{dec} \right)^{T}W^{tmp}h_{i}^{enc}} \in {\mathbb{R}}}} & (2) \\
{q_{ti}^{tmp} = {\frac{\exp \; \left( s_{ti}^{tmp} \right)}{\sum\limits_{j = 1}^{t - 1}{\exp \; \left( s_{ji}^{tmp} \right)}} \in {\mathbb{R}}}} & (3) \\
{\alpha_{ti}^{tmp} = {\frac{q_{ti}^{tmp}}{\sum\limits_{j = 1}^{n}q_{t_{j}}^{tmp}} \in {\mathbb{R}}}} & (4) \\
{c_{t}^{tmp} = {{\sum\limits_{i = 1}^{n}{\alpha_{ti}^{tmp}h_{i}^{enc}}} \in {\mathbb{R}}^{d^{bid}}}} & (5)
\end{matrix}\)

where qtitmp is set to exp(stitmp) for t=1.

The contextual model 222 also attends to the decoder's previous states via decoder intra-attention over the decoded sequence. The decoder intra-attention context at time t, ctint, can be computed as:

\(\begin{matrix}
{s_{ti}^{int} = {{\left( h_{t}^{dec} \right)^{T}W^{int}h_{i}^{dec}} \in {\mathbb{R}}}} & (6) \\
{c_{t}^{int} = {{\sum\limits_{i = 1}^{t - 1}{\left( \frac{s_{ti}^{int}}{\sum\limits_{j = 1}^{n}s_{tj}^{int}} \right)h_{i}^{dec}}} \in {\mathbb{R}}^{d^{bid}}}} & (7)
\end{matrix}\)

A reference vector 240 is generated, created, or derived from the temporal attention context vector cttmp (computed or generated by encoder 210), and the intra-attention context vector ctint and the hidden state of the contextual model htdec (both computed or generated by contextual model 222). The reference vector 240 relates to words that may be extracted from the source document for inclusion in a summarization.

In order to generate an abstractive summarization of the document, the words extracted from the source document are combined with paraphrases of other words or phrases from the document. To accomplish this, the decoder 220 generates tokens by interpolating between selecting words from the source document via a pointer network and selecting words from a fixed output vocabulary.

Thus, at a process 340, the language model 224 of the decoder 220 generates vectors for composing paraphrases of select words or phrases of the source document, the paraphrasing from the fixed vocabulary. In some embodiments, the language model 224 utilizes or incorporates an encoder which can be implemented as a three-layer unidirectional LSTM with weight-dropped LSTM units 228. In some embodiments, the architecture of the language model 224 is based on the model described in further detail in Merity, et al., “Regularizing and optimizing lstm language models,” in ICLR, 2018, which is incorporated by reference herein. In some embodiments, as described herein in further detail, the language model 224 is pre-trained on a training dataset (such as the CNN/Daily Mail dataset) before being used by neural network 200 for abstractive summarization.

In operation for the language model 224, let zt denote the ground truth label as to whether the tth output word of the summarization should be generated by the decoder 220 selecting from the fixed output vocabulary as opposed to from the source document. The probability p(zt) that the decoder 220 generates from the output vocabulary is computed as:

rt=[htdec;cttmp;ctint]∈3d  (8)

p(zt)=sigmoid(Wzrt+bz)∈  (9)

The probability of the language model 224 selecting the word yt from a fixed vocabulary at time step t is defined as:

pgen(yt)=softmax(Wgenrt+bgen)  (10)

The probability pcp(yt) of the decoder 220 copying the word yt from the source document is set to the temporal attention distribution αttmp. The joint probability p(zt, yt) of generating the word yt at time step t is then:

p(zt,yt)=p(yt|zt)p(zt)  (11)

the likelihood of which is

\(\begin{matrix}
{{\log \mspace{11mu} p\mspace{11mu} \left( {z_{t},y_{t}} \right)} = {{{\log \mspace{11mu} p\mspace{11mu} \left( y_{t} \middle| z_{t} \right)} + {\log \mspace{11mu} p\mspace{11mu} \left( z_{t} \right)}} = {{{z_{t}\mspace{11mu} \log \mspace{11mu} {p^{gen}\left( y_{t} \right)}} + {\left( {1 - z_{t}} \right)\mspace{11mu} \log \mspace{11mu} {p^{cp}\left( y_{t} \right)}} + {z_{t}\mspace{11mu} \log \mspace{11mu} p\mspace{11mu} \left( z_{t} \right)} + {\left( {1 - z_{t}} \right)\mspace{11mu} \log \mspace{14mu} \left( {1 - {p\mspace{11mu} \left( z_{t} \right)}} \right)}} = {{z_{t}\left( {{\log \mspace{11mu} {p^{gen}\left( y_{t} \right)}} + {\log \mspace{11mu} p\mspace{11mu} \left( z_{t} \right)}} \right)} + {\left( {1 - z_{t}} \right)\; \left( {{\log \mspace{11mu} {p^{cp}\left( y_{t} \right)}} + {\log \mspace{11mu} \left( {1 - {p\mspace{11mu} \left( z_{t} \right)}} \right)}} \right)}}}}} & (12)
\end{matrix}\)

The objective function combines maximum likelihood estimation with policy learning for the neural network model 200. Let m denote the length of the ground truth summary, maximum likelihood loss Lml is computed as:

\(\begin{matrix}
{L^{m\; 1} = {- {\sum\limits_{t = 1}^{m}{\log \mspace{11mu} p\mspace{11mu} \left( {z_{t},y_{t}} \right)}}}} & (13)
\end{matrix}\)

Policy learning for the neural network 200 uses ROUGE-L as its reward function and self-critical baseline using the greedy decoding policy, as described in further detail in Rennie, et al., “Self-critical sequence training for image captioning,” CoRR, abs/1612.00563, 2016, which is incorporated by reference herein. Let ysam denote the summary obtained by sampling from the current policy p, ygre and zgre the summary and generator choice obtained by greedily choosing from p(zt, yt), and R(y) the ROUGE-L score of the summary y, and Θ the model parameters. The policy learning loss is:

\(\begin{matrix}
{\hat{R} = {{R\left( y^{sam} \right)} - {R\left( y^{gre} \right)}}} & (14) \\
{{{L^{pg} = {{- _{z^{sam}}} \sim {p\mspace{11mu} (z)}}},\left\lbrack \hat{R} \right\rbrack}\mspace{104mu} {y^{sam} \sim {p\mspace{11mu} \left( y \middle| z \right)}}} & (15)
\end{matrix}\)

where greedy predictions are used by the model according to eq. (13) as a baseline for variance reduction.

In some embodiments, as described in further detail in Schulman, et al., “Gradient estimation using stochastic computation graphs,” in NIPS, 2015, which is incorporated by reference herein, the policy gradient is computed as:

\(\begin{matrix}
{{\nabla_{\ominus}L^{pg}} \approx {\hat{R}{\sum\limits_{t = 1}^{m}{{\nabla_{\ominus}\; \log}\mspace{11mu} p\mspace{11mu} \left( {z_{t}^{sam},y_{t}^{sam}} \right)}}}} & (16)
\end{matrix}\)

The final loss is a mixture between the maximum likelihood loss and the policy learning loss, weighted by a hyperparameter γ.

L=(1−γ)Lml+γLpg  (17)

At a process 350, the fusion layer 250 in conjunction with the language model 224 generates an abstractive text summarization of the source document. In particular, the fusion layer 250 fuses the reference vector 240 (composed of context vectors cttmp, ctint, and the hidden state of the contextual model htdec) with the hidden state vector of the last LSTM of the language model 224. In some embodiments, this can be done in a fashion similar to that described in further detail in Sriram, et al., “Cold fusion: Training seq2seq models together with language models,” CoRR, abs/1708.06426, 2017, which is incorporated by reference herein.

In some embodiments, the neural network 220 (with fusion layer 250 and language model 224) operates as follows to create the abstractive summarization for the source document on a word-by-word basis. Let et denote the embedding of the word generated during time step t. The hidden state vector of the language model 224 at the lth layer is:

hl,tlm=LSTM3lm(et-1,hl,t-1lm)  (18)

At each time step t, the hidden state vector (h3,tlm) of the last LSTM of the language model 224 is combined with rt defined in eq. (8) in a fashion similar to Sriram, et al., “Cold fusion: Training seq2seq models together with language models,” CoRR, abs/1708.06426, 2017, which is incorporated by reference herein. Let ⊙ denote element-wise multiplication. The fusion layer 250 uses a gating function whose output gt filters the content of the hidden state vector of the language model 224.

ft=sigmoid(Wlm[rt;h3,tlm]+blm)  (19)

gt=Wfuse([rt:gt⊙h3,tlm])+bfuse  (20)

htfuse=ReLU(gt)  (21)

The output distribution pgen(yt) of the language model 224 in eq. (10) is then replaced with:

pgen(yt)=softmax(Wgenbtfuse+bgen)  (22)

Thus, the neural network model 200 of the present disclosure generates an abstractive summarization for an input source document.

According to some embodiments, a novelty metric is employed or implemented to promote abstraction by rewarding the neural network model 200 for generating words for the summary that are not in the source document.

A “novel” phrase in the summarization may be defined as one that is not in the source document. Let ng (x, n) denote the function that computes the set of unique n-grams in a document x, xgen the generated summary, xsrc the source document, and II s II the number of words in s. The unnormalized novelty metric N is defined as the fraction of unique n-grams in the summary that are novel.

\(\begin{matrix}
{{N\left( {x^{gen},n} \right)} = \frac{{{{ng}\left( {x^{gen},n} \right)} - {{ng}\left( {x^{src},n} \right)}}}{{{ng}\left( {x^{gen},n} \right)}}} & (23)
\end{matrix}\)

To prevent the neural model 200 from receiving high novelty rewards by outputting very short summaries, the novelty metric is normalized by the length ratio of the generated and ground truth summaries. Let xgt denote the ground truth summary. The novelty metric is defined as:

\(\begin{matrix}
{{R^{nov}\left( {x^{gen},n} \right)} = {{N\left( {x^{gen},n} \right)}\frac{x^{gen}}{x^{gt}}}} & (24)
\end{matrix}\)

The neural network model 200 incorporates the novelty metric as a reward into the policy gradient objective in eq. (15), alongside the original ROUGE-L metric. By doing so, the neural network model 200 is encouraged to generate summaries that both overlap with human written ground-truth summaries as well as incorporate novel words not in the source document.

R(y)=λrouRrou(ysam)+λnovRnov(ysam)  (25)

where λrou and λnov are hyperparameters (parameters of a prior distribution) that control the weighting of each reward metric.

One or more of the processes 310-350 of method 300 described herein may be implemented, at least in part, in the form of executable code stored on non-transitory, tangible, machine-readable media that when run by one or more processors (e.g., processor 110 of computing device 100) may cause the one or more processors to perform one or more of the processes or methods. Some common forms of machine readable media that may include the processes or methods are, for example, floppy disk, flexible disk, hard disk, magnetic tape, any other magnetic medium, CD-ROM, any other optical medium, punch cards, paper tape, any other physical medium with patterns of holes, RAM, PROM, EPROM, FLASH-EPROM, any other memory chip or cartridge, and/or any other medium from which a processor or computer is adapted to read.

According to some embodiments, the neural network model 200 (e.g., language model 224) is trained before being employed or used to generate abstractive text summarizations. For this training, various datasets can be used, such as the CNN/Daily Mail dataset, as described in more detail in Hermann, et al., “Teaching machines to read and comprehend,” in NIPS, 2015 and Nallapati, et al., “Abstractive text summarization using sequence-to-sequence rnns and beyond,” Proceedings of SIGNLL Conference on Computational Natural Language Learning, 2016, both of which are incorporated by reference herein. Previous works on abstractive summarization either use an anonymized version of this dataset or the full original article and summary texts. In order to compare against previous results, the neural network model 200 can be trained on both versions of this dataset and evaluated. For the anonymized version, in some embodiments, the pre-processing steps described in further detail in Nallapati, et al., “Abstractive text summarization using sequence-to-sequence rnns and beyond,” Proceedings of SIGNLL Conference on Computational Natural Language Learning, 2016, which is incorporated by reference herein, are followed. For the full-text version, the pre-processing steps in further detail in See, et al., “Get to the point: Summarization with pointer-generator networks,” in ACL, 2017, which is incorporated by reference herein, are followed.

Named entities and the source document are used to supervise the neural network model 200 regarding when to use the pointer and when to use the generator (e.g., zt in eq. (13)). Namely, during training, the neural model 200 is taught to point from the source document if the word in the ground truth summary is a named entity, an out-of-vocabulary word, or a numerical value that is in the source document. In some embodiments, the list of named entities can be obtained as described in further detail in Hermann, et al., “Teaching machines to read and comprehend,” in NIPS, 2015, which is incorporated by reference herein.

According to some embodiments, for each dataset version, a language model 224 comprising a 400-dimensional word embedding layer and a 3-layer LSTM (with each layer having a hidden vector size of 800 dimensions, except the last input layer which has an output size of 400) is trained. The final decoding layer shares weights with the embedding layer, for example, as described in further detail in Inan, et al., “Tying word vectors and word classifiers: A loss framework for language modeling,” in ICLR, 2017 and Press, et al., “Using the output embedding to improve language models,” arXiv preprint arXiv:160805859, 2016, both of which are incorporated by reference herein. The language model 224 can use DropConnect (the details of which are described in Wan, et al., “Regularization of neural networks using dropconnect,” in ICML, 2013, which is incorporated by reference herein) in the hidden-to-hidden connections, as well as the non-monotonically triggered asynchronous gradient descent optimizer (described in further detail in Merity, et al., “Regularizing and optimizing lstm language models,” in ICLR, 2018, which is incorporated by reference herein). In some embodiments, the language model 224 can be trained on the CNN/Daily Mail ground truth summaries only, following the same training, validation, and test splits as the main experiments.

Furthermore, in some embodiments, for training, the two LSTMs of bi-directional encoder 210 are 200-dimensional, and the LSTM of language model 224 of decoder 220 is 400-dimensional. The input vocabulary for the embedding matrix is restricted to 150,000 tokens, and the output decoding layer is restricted to 50,000 tokens. The size of input articles is limited to the first 400 tokens, and the summaries to 100 tokens. Scheduled sampling, as described in Bengio et al., “Neural machine translation by jointly learning to align and translate,” in ICLR, 2015, which is incorporated by reference herein, is used with a probability of 0.25 when calculating the maximum-likelihood training loss. Set n=3 when computing the novelty reward Rnov′(xgen, n). For final training loss using reinforcement learning, set γ=0:9984, μrou=0:9, and λnov=0:1. Finally, the trigram repetition avoidance heuristic, defined by Paulus, et al., “A deep reinforced model for abstractive summarization,” in ICLR, 2017, which is incorporated by reference herein, is used during beam search decoding to ensure that the model does not output twice the same trigram in a given summary, thus reducing the amount of repetitions.

In some embodiments, a novelty baseline is created for the neural network model 200 by taking the outputs of the base model, without ROUGE-L training and without the language model 224, and inserting random words not present in the article after each summary token with a probability r=0.0005. This baseline will intuitively have a higher percentage of novel n-grams than the base model outputs while being very similar to these original outputs, hence keeping the ROUGE score difference relatively small.

FIG. 4 is a table 400 showing example summaries generated by different models for the same original source document, e.g., an article from CNN/Daily Mail. The highlighted spans indicate phrases of 3 tokens or more that are copied word-by-word from the original article.

The advantages or improvements of the abstractive text summarization model of the present disclosure compared to other models are confirmed or validated by test results. A validation and test perplexity of 65.80 and 66.61 were obtained respectively on the anonymized dataset, and 81.13 and 82.98 on the full-text dataset with the language model 224 described herein.

FIG. 5 is a table 500 comparing performance results of systems and models for abstractive text summarization according to embodiments of the present disclosure. This table shows the ROUGE scores and novelty scores of the final summarization model on both versions of the CNN/Daily Mail dataset, including comparisons to previous works on the these datasets. In particular, the table of FIG. 5 provides the ROUGE-1, ROUGE-2, and ROUGE-L F-scores as well as the percentage of novel n-grams, marked NN-n, in the generated summaries, with n from 1 to 4. Also included are the novel n-gram percentages for ground truth summaries as a comparison to indicate the level of abstraction of human written summaries. As seen in FIG. 5, the neural network model 200 of the present disclosure, including language model 224, provides a much higher percentage of novel n-grams than all the previous abstractive approaches. It also achieves state-of-the-art ROUGE-L performance on both dataset versions, and obtains ROUGE-1 and ROUGE-2 scores close to state-of-the-art results.

In order to evaluate the relative impact of each of individual contributions, ablation studies were run to compare ablations of the neural network model 200, including language model 224, against a novelty baseline. FIG. 6 is a table 600 comparing results of the ablation study for the model of the present disclosure and other abstractive summarization models. This table of FIG. 6, which are the results of the ablation study on the validation set of the anonymized CNN/Daily Mail dataset, shows that adding the language model 224 to the decoder 220 improves abstraction and novelty in all of the conducted experiments. Results show that the base model trained with the maximum-likelihood loss only and using the language model 224 in the decoder 220 (ML, with LM) has higher ROUGE scores, novel unigrams, and novel bigrams scores than the base model without the language model 224 (ML). The language model 224 in the decoder 220 (ML with LM) also provides better results for these metrics than the novelty baseline. When training these models with reinforcement learning using the ROUGE reward (ML+RL ROUGE and ML+RL ROUGE with LM), the neural network model 200 with language model 224 obtains higher ROUGE-1 and ROUGE-2 scores. Finally, using the mixed ROUGE and novelty rewards (ML+RL ROUGE+Novel) produces both higher ROUGE scores and more novel unigrams with the language model 224 than without it. This indicates that by providing the language model 224 in the decoder 220 and the novelty reward during training, the neural network model 200 produces more novel unigrams while maintaining high ROUGE scores.

FIG. 7 are charts 710, 720 plotting results on the anonymized validation set for different runs of the model of the present disclosure and other abstractive summarization models. The first chart 710 plots the ROUGE-1 and novel unigram scores for the five best iterations of each model type on the anonymized dataset, and the second chart 720 plots the ROUGE-2 and novel bigram scores. These charts show the correlation between ROUGE and novel n-gram scores across different architectures, and to help to identify the model type that gives the best trade-off between each of these metrics. Also shown in the novelty baseline for values of r between 0.005 and 0.035. For each model type, the Pareto frontier is indicated by a line plot, as described in more detail in Ben-Tal, “Characterization of pareto and lexicographic optimal solutions,” in Multiple Criteria Decision Making Theory and Application, pp. 1-11, 1980, which is incorporated by reference herein, illustrating which models of a given type give the best combination of ROUGE and novelty scores.

These plots show that the ROUGE scores are inversely correlated with novelty scores in all model types, illustrating the challenge of choosing a model that performs well in both. As can be seen in FIG. 7, the neural network model (ML+RL ROUGE+Novel, with LM) provides the best trade-off of ROUGE-1 scores compared to novel unigrams, indicated by the higher Pareto frontier in the first plot. Similarly, this model provides the best trade-offs of ROUGE-2 scores to novel bigrams. Thus, with reference to FIG. 7, the plots show that for each architecture, adding the language model 224 to the decoder 220 typically gives a better ROUGE score, a better novelty score, or both.

Although illustrative embodiments have been shown and described, a wide range of modification, change and substitution is contemplated in the foregoing disclosure and in some instances, some features of the embodiments may be employed without a corresponding use of other features. One of ordinary skill in the art would recognize many variations, alternatives, and modifications. Thus, the scope of the invention should be limited only by the following claims, and it is appropriate that the claims be construed broadly and in a manner consistent with the scope of the embodiments disclosed herein.

