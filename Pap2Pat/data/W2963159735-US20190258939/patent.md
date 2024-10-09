# DESCRIPTION

## PRIORITY APPLICATION DATA

This application claims priority to U.S. Provisional Application No. 62/634,151 filed on Feb. 22, 2018 and entitled “Question Answering from Minimal Context Over Documents”, which is incorporated by reference in its entirety.

## TECHNICAL FIELD

The disclosure generally relates to natural language processing and more specifically to answering natural language questions about a natural language context from a variable set of sentences.

## BACKGROUND

The task of textual question answering (“QA”), in which a machine reads a document and answers a question, is an important and challenging problem in natural language processing. Progress in neural QA models is largely due to the variety of available QA datasets.

Conventional neural QA models leverage a bidirectional attention mechanism that builds codependent representations of a document and a question. This is done by learning the context over different parts in the full document. But, learning the full context over the document is challenging and inefficient. This is particularly true when a conventional neural QA model is given a long document or multiple documents. In this case, the conventional neural QA model learning the full context is intractably slow and difficult to scale to large corpora.

Additionally, when conventional neural models are given adversarial inputs, such models tend to focus on wrong subsets of the context and produce incorrect answers as a result.

Accordingly, what is needed is a QA system that is scalable to large documents and is robust to adversarial inputs.

In the figures, elements having the same designations have the same or similar functions.

## DETAILED DESCRIPTION

The task of textual question answering (“QA”), in which a machine reads a document and answers a question, is an important and challenging problem in natural language processing. Because learning the full context of a document to answer a question is inefficient, the embodiments describe a QA system that is scalable to large documents and robust to adversarial inputs.

In some embodiments, the QA system may identify most answers to a passage in a document when asked a few questions and without considering an entire document. To identify an answer, a QA system may use a sentence selector. The sentence selector may identify a set of sentences from a document. The set of sentences can be a minimum set of sentences or sentences that have a score above a configurable threshold. The set of sentences from a document may vary from question to question. Once the sentence selector identifies a set of questions, a QA module in the QA system uses the set of sentences to determine an answer to a question.

FIG. 1 is a simplified diagram of a computing device 100 according to some embodiments. As shown in FIG. 1, computing device 100 includes a processor 110 coupled to memory 120. Operation of computing device 100 is controlled by processor 110. And although computing device 100 is shown with only one processor 110, it is understood that processor 110 may be representative of one or more central processing units, multi-core processors, microprocessors, microcontrollers, digital signal processors, field programmable gate arrays (FPGAs), application specific integrated circuits (ASICs), graphics processing units (GPUs) and/or the like in computing device 100. Computing device 100 may be implemented as a stand-alone subsystem, as a board added to a computing device, and/or as a virtual machine.

Memory 120 may be used to store software executed by computing device 100 and/or one or more data structures used during operation of computing device 100. Memory 120 may include one or more types of machine readable media. Some common forms of machine readable media may include floppy disk, flexible disk, hard disk, magnetic tape, any other magnetic medium, CD-ROM, any other optical medium, punch cards, paper tape, any other physical medium with patterns of holes, RAM, PROM, EPROM, FLASH-EPROM, any other memory chip or cartridge, and/or any other medium from which a processor or computer is adapted to read.

Processor 110 and/or memory 120 may be arranged in any suitable physical arrangement. In some embodiments, processor 110 and/or memory 120 may be implemented on the same board, in a same package (e.g., system-in-package), on the same chip (e.g., system-on-chip), and/or the like. In some embodiments, processor 110 and/or memory 120 may include distributed, virtualized, and/or containerized computing resources. Consistent with such embodiments, processor 110 and/or memory 120 may be located in one or more data centers and/or cloud computing facilities. In some examples, memory 120 may include non-transitory, tangible, machine readable media that includes executable code that when run by one or more processors (e.g., processor 110) may cause the one or more processors to perform the question answering methods described in further detail herein.

As illustrated in FIG. 1, memory 120 may include a question answering system 130 (or simply QA system 130). QA system 130 may be implemented using hardware, software, and/or a combination of hardware and software. Unlike conventional question answering systems, QA system 130 receives a natural language document 160 (or simply document 160) and a natural language question 170 (or simply question 170) about document 160. Document 160 may be a portion of a document, one or more paragraphs of a document or an entire document. After QA system 130 receives document 160 and question 170, QA system 130 may generate a natural language answer 180 (or simply answer 180) to question 170 without evaluating the entire document 160. Rather, QA system 130 uses document 160 to generate a variable set of sentences and uses the set of sentences to determine answer 180.

As also illustrated in FIG. 1, computing device 100 may receive document 160 and question 170 and may provide document 160 and question 170 to QA system 130. Once QA system 130 generates an answer 180, QA system 130 may provide answer 180 to computing device 100.

In some embodiments, QA system 130 may include a sentence selector 140 and a QA module 150. Together sentence selector 140 and QA module 150 may be used to implement and/or emulate the models described further herein and/or to implement any of the methods described further herein. In some examples, sentence selector 140 and QA module 150 may receive document 160 and question 170 and generate answer 180. In some examples, sentence selector 140 and QA module 150 may also handle the iterative training and/or evaluation of QA system 130.

FIG. 2 is a simplified diagram of the QA system 130, according to some embodiments. As discussed above, QA system 130 may include sentence selector 140 and QA module 150. Sentence selector 140 and QA module 150 may be implemented using neural networks.

In some embodiments, sentence selector 140 may receive question 170 and one or more sentences 210 from document 160. Sentences 210 may be sentences identified from an entire document 160, a portion of document 160, or a particular paragraph, such as a first paragraph, of document 160.

In some embodiments, sentence selector 140 may include an encoder 220 and a decoder 230 (shown as sentence selector decoder 230). Notably, unlike conventional systems, sentence selector 140 shares encoder 220 with QA module 150, which is discussed below.

FIG. 3 is a block diagram of encoder 220, according to some embodiments. Encoder 220 may receive question 170 and one or more sentences 210 as inputs. From sentences 210, encoder 220 may determine sentence embeddings DϵL×h(shown as 215) and from question 170, encoder 220 may determine question embeddings QϵL×h(shown as 225). Also, from sentences 210 and question 170, encoder 220 may determine question-aware sentence embeddings DqϵL×h, and where hd is the dimension of word embeddings, and Ld is a sequence length of document 160 and Lq is a sequence length of question 170.

In some embodiments, the dimension of the embeddings D may be 600 and h may be 200.

In some embodiments, encoder 220 may generate the question-aware sentence embeddings Dq as illustrated below:

αi,j=softmaxj(DiTQ1Q)ϵL  (Equation 1)

Diq=Σj=1L(αi,jQj)ϵh  (Equation 2)

In some embodiments, Diqϵhmay be a hidden state of sentence embeddings for the ith word and W1ϵhis a matrix of trainable weights. As illustrated in Equations 1 and 2 above, encoder 220 may generate question-aware sentence embeddings using sentence embeddings D and question embeddings Q.

In some embodiments, encoder 220 may obtain sentence encodings Denc (shown as 235) and question encoding Qenc (shown as 240) using a Bi-Directional Long Short-Term Memory or Bi-LSTM. Bi-STTM is a type of a recurrent neural network that may be used for sequential data. To determine sentence encodings Denc the input to a Bi-LSTM_D may be sentence embeddings D and question-aware sentence embeddings Dq. For example, sentence encodings Denc may be generated by solving the following equation:

Denc=BiLSTM([Di;Diq])ϵh)  (Equation 3)

To determine question encodings Qenc the input to a Bi-LSTM_Q may be question embeddings Q and question-aware sentence embeddings Dq. For example, question encodings Qenc may be generated by solving the following equation:

Qenc=BiLSTM(Qj)ϵh×L  (Equation 4)

In some embodiments, “;” denotes a concatenation of two vectors, and h is a hyper-parameter of the hidden dimension. In some embodiments, hyper-parameter may have a size of 200.

Going back to FIG. 2, in some embodiments, decoder 230 may compute a score 245 for sentence 210 that indicates whether question 170 is answerable by sentence 210. FIG. 4 is a block diagram of a decoder 230, according to some embodiments. Decoder 230 may determine score 245 by calculating bilinear similarities between sentence encodings Denc and question encodings Qenc as follows:

β=softmax(wTQenc)ϵL  (Equation 5)

qēnc=Σj=1L(βjQjenc)ϵh  (Equation 6)

{tilde over (h)}i=(DiencW2qēnc)ϵh  (Equation 7)

{tilde over (h)}=max({tilde over (h)}1,{tilde over (h)}2, . . . ,{tilde over (h)}L  (Equation 8)

score=W3T{tilde over (h)}ϵ2  (Equation 9)

In some embodiments, wϵh, W2ϵh×h×h, W3ϵh×2 may be matrices having trainable weights. In some embodiments, each dimension of the score 245 means question 170 is answerable or not answerable given a particular sentence 210.

In some embodiments, sentence selector 140 may include a normalizer (not shown). Normalizer may be included in decoder 230 after the score is computer in Equation 9 and after the linear layer shown in FIG. 4. A normalizer may normalize scores 245 into normalized scores for sentences 210 from the same paragraph. Typically, normalized scores may have a value from 0 to 1.

Going back to FIG. 2, in some embodiments, sentence selector 140 may include a sentence score module 250. Sentence score module 250 may select sentences 210 into a set of sentences 255 based on scores 245. Set of sentences 255 may include sentences 210 that QA module 150 (described below) may use to determine answer 180 to question 170. In some embodiments, sentence score module 250 may select a minimum number of sentences 210 into set of sentences 255. A minimum number of sentences 210 is a number of sentences 210 that QA module 150 may use to generate answer 180. One way for sentence score module 250 to select a minimum number of sentences 210 is to use a hyper-parameter “th”. To select sentences 210 using a hyper-parameter, sentence score module 250 may receive scores 245 for all sentences 210 for document 160 as Sall={s1, s2, s3, . . . , sn}, where Sall is ordered according to scores 245 or normalized scores in, for example, a descending order. Next, sentence score module 250 may select sentences to be included in the set of sentences 255 (Sselected) as follows:

\(\begin{matrix}
{S_{candidate} = \left\{ {s_{i} \in S_{all}} \middle| {{{score}\left( s_{i} \right)} \geq {1 - {th}}} \right\}} & \left( {{Equation}\mspace{14mu} 10} \right) \\
{S_{selected} = \left\{ \begin{matrix}
S_{candidate} & {{{if}\mspace{14mu} S_{candidate}} = \varnothing} \\
\left\{ s_{1} \right\} & {otherwise}
\end{matrix} \right.} & \left( {{Equation}\mspace{14mu} 11} \right)
\end{matrix}\)

In some embodiments where score(si) is a normalized score, the “th” hyper-parameter may be between 0 and 1.

In some embodiments, Scandidate includes a set of sentences 210 that have a score greater than a “th” hyper-parameter when the hyper-parameter is subtracted from one as shown in Equation 10. Once sentence score module 250 determines the S candidate set, sentence score module 250 may determine that the S candidate set is not an empty set as shown in Equation 11. If the S candidate set is not an empty set, the S candidate set becomes the set of sentences 255 which is Sselected in Equation 11. Otherwise if S candidate set is an empty set, sentence score module 250 may include a first sentence s1 in the Sall. In this case, if sentences 210 in the Sall set are included by scores in the descending order, sentence score module 250 may select sentence s1, which has the highest score into the Sselected.

When the minimum set of sentences 255 uses a hyper-parameter, the size of set of sentences 255 may be dynamically controlled at an inference time by adjusting the value of the th hyper-parameter between 0 and 1. In this way, a number of sentences 210 that sentence selector 140 may select to answer question 170 may vary depending on the needs of accuracy and speed of QA system 130.

In some embodiments, sentence score module 250 may use a configurable threshold to select one or more sentences 210. For example, sentence score module 250 may select sentences 210 with scores 245 above a configurable threshold.

Going back to FIG. 2, in some embodiments, architecture for QA module 150 may be divided into encoder 220 and a QA model decoder 260 or simply decoder 260. Notably, QA module 150 may include encoder 220 that is included in sentence selector 140. FIG. 5 is a block diagram of QA module 150 according to some embodiments. As illustrated in FIG. 5, instead of receiving sentences 210 from document 160, encoder 220 may receive set of sentences 255 generated by sentence selector 140 and question 170. Using set of sentences 255 and question 170, encoder 220 may generate document embeddings DϵL×h(shown as 215), question embeddings QϵL×h(shown as 225) and question-aware document embeddings DqϵL×h, where Dq may be defined as in Equation 1. In some embodiments, encoder 220 may obtain sentence encodings Denc (shown as 235) and question encodings Qenc (shown as 240) as shown in FIG. 3. Encoder 220 may pass document encodings Denc and question encodings Qenc to QA Model decoder 260 (or simply decoder 260).

Going back to FIG. 2, in some embodiments, decoder 260 may obtain the scores for an answer span to question 170. FIG. 6 is a block diagram of decoder 260, according to some embodiments. Decoder 260 may determine scores for the start position 610 and the end position 620 of an answer span by calculating bilinear similarities between document encodings Denc and question encodings Qenc as follows:

β=softmax(w1TQenc)ϵh  (Equation 12)

qēnc=Σj=1L(βjQjenc)ϵh  (Equation 13)

scorestart=DencwstartqēncϵL  (Equation 14)

scoreend=DencwendqēncϵLd  (Equation 15)

where w1ϵRh, Wstart, Wendϵh×h are matrices that have trainable weights. The start position 610 and end position 620 may identify answer 180 to question 170.

FIG. 7 is a flowchart of a method for answering a question, according to some embodiments. One or more of the processes 702-710 of method 700 may be implemented, at least in part, in the form of executable code stored on non-transitory, tangible, machine-readable media that when run by one or more processors may cause the one or more processors to perform one or more of the processes 702-710.

At operation 702, a question and one or more sentences are received. For example, sentence selector 140 receives question 170 and one or more sentences 210 from document 160.

At operation 704, scores for the one or more sentences are generated. For example, encoder 220 and decoder 230 included in sentence selector 140 generate scores 245 for one or more sentences 210. FIG. 8 is flowchart that describes how scores are generated according to some embodiments and is described below.

At operation 706, a set of scores is generated. For example, sentence score module 250 included in sentence selector 140 may select a subset of sentences 210 into set of sentences 255. In some embodiments, set of sentences 255 may be based on a hyper-parameter. In some embodiments, set of sentences may include scores 245 that are above a configurable threshold.

At operation 708, the set of sentences and a question are received. For example, QA module 150 may receive set of sentences 255 and question 170.

At operation 710, an answer is generated. For example, encoder 220 that QA module 150 may share with sentence selector 140 and decoder 260 may generate answer 180 from set of sentences 255.

FIG. 8 is a flowchart of a method for determining a set of sentences, according to some embodiments. One or more of the processes 802-814 of method 800 may be implemented, at least in part, in the form of executable code stored on non-transitory, tangible, machine-readable media that when run by one or more processors may cause the one or more processors to perform one or more of the processes 802-814.

At operation 802, sentence embeddings are determined. For example, encoder 220 determines sentence embeddings D using dimension of word embeddings and sequence length of document 160.

At operation 804, question embeddings are determined. For example, encoder 220 determines question embeddings Q using dimension of word embeddings and sequence length of question 170.

At operation 806, question-aware sentence embeddings are determined. For example, encoder 220 determines question-aware sentence embeddings Dq using sentence embeddings D and question embeddings Q.

At operation 808, sentence encodings are generated. For example, encoder 220 generates sentence encodings Denc from sentence embeddings Dq and question-answer sentence embeddings Dq.

At operation 810, question encodings are generated. For example, encoder 220 generates question encodings Qenc from sentence embeddings Dq and question-answer sentence embeddings Dq.

At operation 812, scores for sentences are determined. For example, decoder 230 determines scores 245 for sentences 210.

At operation 814, a set of sentences is determined. For example, sentence score module 250 uses scores 245 to determine sentences 210 to be included in set of sentences 255. As discussed above, set of sentences 255 may include a minimum set of sentences that QA module 150 may use to determine answer 180 or a number of sentences 210 that have scores 245 above a threshold.

FIG. 9 is a flowchart of a method for answering a question, according to some embodiments. One or more of the processes 902-914 of method 900 may be implemented, at least in part, in the form of executable code stored on non-transitory, tangible, machine-readable media that when run by one or more processors may cause the one or more processors to perform one or more of the processes 902-914.

At operation 902, sentence embeddings are determined. For example, encoder 220 determines sentence embeddings D using dimension of word embeddings and sequence length of sentences 210 in set of sentences 255.

At operation 904, question embeddings are determined. For example, encoder 220 determines question embeddings Q using dimension of word embeddings and sequence length of question 170.

At operation 906, question-aware sentence embeddings are determined. For example, encoder 220 determines question-aware sentence embeddings Dq using sentence embeddings D and question embeddings Q.

At operation 908, sentence encodings are generated. For example, encoder 220 generates sentence encodings Denc from sentence embeddings Dq and question-answer sentence embeddings Dq.

At operation 910, question encodings are generated. For example, encoder 220 generates question encodings Qenc from sentence embeddings Dq and question-answer sentence embeddings Dq.

At operation 912, determine a start position and an end position for an answer. For example, decoder 260 uses sentence encodings Denc and Qenc and question encodings to generate start position 610 and end position 620 for answer 180 to question 170.

At operation 914, an answer is identified. For example, decoder 260 uses start position 610 and end position 620 to identify answer 180.

Going back to FIG. 2, in some embodiments, there may be several techniques to train sentence selector 140. In the first technique, QA module 150 may be trained on a single oracle sentence and weights from QA model trained on a single oracle sentence may be incorporated into encoder 220. An oracle sentence may be a sentence that includes a ground truth answer span. In the second technique, training data may be modified if sentence 210 receives a score of zero. In a third technique, score 245 for each sentence 210 may be normalized across sentences 210 from the same paragraph. Typically, a normalized score may be from 0 to 1.

In some embodiments, training data may be data from one or more existing QA datasets. The various data sets are discussed in the “Efficient and Robust Question Answering from Minimal Context over Documents,” Sewon Min, et. al, which is incorporated by reference in its entirety. Example datasets may be a SQuAD dataset from a large set of Wikipedia articles. The SQuAD dataset may provide a paragraph for each question 170. Another example of a dataset may be a NewsQA dataset that includes a large set of news articles and also provides a paragraph for each question 170. Typically, paragraphs in NewsQA dataset are longer than paragraphs in a SQuAD dataset. Another example of a dataset is a TriviaQA dataset that includes a large set of Wikipedia articles and web documents. In a TriviaQA dataset, each question 170 is given a longer context in the form of multiple documents. In yet another example, a dataset may be an open domain question answering dataset based on SQuAD. In a SQuAD-Open dataset, only the question and the answer may be given, and a model may identify the relevant context from the English Wikipedia articles or Wikipedia articles written in another language. In yet another embodiment, a SQuAD-Adversarial dataset may be another variant of a SQuAD dataset. For example, the SQuAD-Adversarial dataset shares the same training set as SQuAD, but also has an adversarial sentence that is added to each paragraph in a sub set of a development set. Table 1 below illustrates example datasets that may be used to train question answering system:

In the Table 1 above, “N word” may refer to the average number of words in document 160, “N sent” may refer to an average number of sentences in document 160, and “N doc” may refer to an average number of documents 160.

In some embodiments, several conventional QA models may be compared to QA system 130. Example conventional QA models may include a conventional full document model, a conventional oracle sentence containing the ground truth answer span model, and a conventional TF-IDF which is also discussed in the “Efficient and Robust Question Answering from Minimal Context over Documents,” which is incorporated by reference in its entirety. Results of a TF-IDF model against QA system 130 are replicated below in Table 2. Additionally, results illustrate QA system 130 where sentence score module 250 may select set of sentences 255 using a hyper-parameter in which case a number of sentences 210 in set of sentences 225 may vary from question to question. Also, results may illustrate a QA system 130 where sentence score module 250 may select set of sentences 255 using a preconfigured threshold, in which case set of sentences 255 may include sentences 210 with scores above the threshold.

With respect to the SQuAD and NewsQA datasets, Table 2 illustrates that question answer system 130 has a higher accuracy and mean average accuracy for determining answer 180 from document 160 and question 170, than the conventional TF-IDF system, and the Tan system discussed in the “Efficient and Robust Question Answering from Minimal Context over Documents,”, which is considered to be a state-of-the art system:

In some embodiments, the “T”, “M”, and “N” in Table 2 identify different training techniques discussed above: “T” is a weight transfer technique, “M” is a data modification technique, and “N” is the score normalization technique.

With respect to a SQuAD dataset, QA system 130 is more accurate than the conventional full document model. Table 3 illustrates three questions 170 (in italicized text), document 160, and the answers that QA system 130 and conventional model system determined from document 160 and question 170.

As illustrated in Table 3, QA system 130 selects a correct answer (underlined). The checkmarks (√) indicate sentences 210 that QA system 130 selected to answer the above questions. Further, given the same questions and text, the conventional full document model does not select a correct answer (bold).

This application is further described with respect to the attached document (“Efficient and Robust Question Answering from Minimal Context over Documents,” 16pp), which is considered part of this disclosure and the entirety of which is incorporated by reference.

Although illustrative embodiments have been shown and described, a wide range of modification, change and substitution is contemplated in the foregoing disclosure and in some instances, some features of the embodiments may be employed without a corresponding use of other features. One of ordinary skill in the art would recognize many variations, alternatives, and modifications. Thus, the scope of the invention should be limited only by the following claims, and it is appropriate that the claims be construed broadly and in a manner consistent with the scope of the embodiments disclosed herein.

