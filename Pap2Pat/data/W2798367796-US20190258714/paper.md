# Introduction

Task oriented dialogue systems can significantly reduce operating costs by automating processes such as call center dispatch and online customer support. Moreover, when combined with automatic speech recognition systems, task-oriented dialogue systems provide the foundation of intelligent assistants such as Amazon Alexa, Apple Siri, and Google Assistant. In turn, these assistants allow for natural, personalized interactions with users by tailoring natural language system responses to the dialogue context. Dialogue state tracking (DST) is a crucial part of dialogue systems. In DST, a dialogue state tracker estimates the state of the conversation using the current user utterance and the conversation history. This estimated state is then used by the system to plan the next action and respond to the user. A state in DST typically consists of a set of requests and joint goals. Consider the task of restaurant reservation as an example. During each turn, the user may inform the system of particular goals the user would like to achieve (e.g. inform(food=french)), or request for more information from the system (e.g. request(address)). The set of goal and request slot-value pairs (e.g. (food, french), (request, address)) given during a turn are referred to as the turn goal and turn request. The joint goal is the set of accumulated turn goals up to the current turn. Figure 1 shows an example dialogue with annotated turn states, in which the user reserves a restaurant.

Traditional dialogue state trackers rely on Spoken Language Understanding (SLU) systems (Henderson et al., 2012) in order to understand user utterances. These trackers accumulate errors from the SLU, which sometimes do not have the necessary dialogue context to interpret the user utterances. Subsequent DST research forgo the SLU and directly infer the state using the conversation history and the user utterance (Henderson et al., 2014b;Zilka and Jurcicek, 2015;Mrkšić et al., 2015). These trackers rely on handcrafted semantic dictionaries and delexicalization -the anonymization of slots and values using generic tags -to achieve generalization. Recent work by Mrkšić et al. (2017) apply representation learning using convolutional neural networks to learn features relevant for each state as opposed to hand-crafting features.

A key problem in DST that is not addressed by existing methods is the extraction of rare slotvalue pairs that compose the state during each turn. Because task oriented dialogues cover large  (Wen et al., 2017), outperforming prior best by 3.7% and 5.5%. On DSTC2 (Henderson et al., 2014a), we achieve 74.5% goal accuracy and 97.5% request accuracy, outperforming prior best by 1.1% and 1.0%.

2 Global-Locally Self-Attentive Dialogue State Tracker

One formulation of state tracking is to predict the turn state given an user utterance and previous system actions (Williams and Young, 2007). Like previous methods (Henderson et al., 2014b;Wen et al., 2017;Mrkšić et al., 2017), GLAD decomposes the multi-label state prediction problem into a collection of binary prediction problems by using a distinct estimator for each slot-value pair that make up the state. Hence, we describe GLAD with respect to a slot-value pair that is being predicted by the model. Shown in Figure 2, GLAD is comprised of an encoder module and a scoring module. The encoder module consists of separate global-locally self-attentive encoders for the user utterance, the previous system actions, and the slot-value pair under consideration. The scoring module consists of two scorers. One scorer considers the contribution from the utterance while the other considers the contribution from previous system actions.

## Global-Locally Self-Attentive Encoder

We begin by describing the global-locally selfattentive encoder, which makes up the encoder module. DST datasets tend to be small relative to their state space in that many slot-value pairs rarely occur in the dataset. Because each state is comprised of a set of slot-value pairs, many of them rare, poor inference of rare slot-value pairs subsequently results in poor turn-level tracking. This problem is amplified in joint tracking, due to the accumulation of turn-level errors. In developing this encoder, we seek to better model  rare slot-value pairs by sharing parameters between each slot through global modules and learning slot-specific features through local modules.

The global-locally self-attentive encoder consists of a bidirectional LSTM (Hochreiter and Schmidhuber, 1997), which captures temporal relationships within the sequence, followed by a self-attention layer to compute the summary of the sequence. Figure 3 illustrates the global-locally self-attentive encoder.

Consider the process of encoding a sequence with respect to a particular slot s. Let n denote the number of words in the sequence, d emb the dimension of the embeddings, and X ∈ R n×d emb the word embeddings corresponding to words in the sequence. We produce a global encoding H g of X using a global bidirectional LSTM.

where d rnn is the dimension of the LSTM state. We similarly produce a local encoding H s of X, taking into account the slot s, using a local bidirectional LSTM.

The outputs of the two LSTMs are combined through a mixture layer to yield a global-local encoding H of X.

Here, the scalar β s is a learned parameter between 0 and 1 that is specific to the slot s. Next, we compute a global-local self-attention context c over H. Self-attention, or intra-attention, is a very effective method of computing summary context over variable-length sequences for natural language processing tasks (Cheng et al., 2016;Vaswani et al., 2017;He et al., 2017;Lee et al., 2017). In our case, we use a global self-attention module to compute attention context useful for general-purpose state tracking, as well as a local self-attention module to compute slot-specific attention context.

For each ith element H i , we compute a scalar global self-attention score a g i which is subsequently normalized across all elements using a softmax function.

The global self-attention context c g is then the sum of each element H i , weighted by the corresponding normalized global self-attention score p g i .

We similarly compute the local self-attention context c s .

The global-local self-attention context c is the mixture

For ease of exposition, we define the multivalue encode function encode (X). encode :

This function maps the sequence X to the encoding H and the self-attention context c.

## Encoding module

Having defined the global-locally self-attentive encoder, we now build representations for the user utterance, the previous system actions, and the slot-value pair under consideration. Let U denote word embeddings of the user utterance, A j denote those of the jth previous system action (e.g. request ( price range ), and V denote those of the slot-value pair under consideration (e.g. food = french). We have

## Scoring module

Intuitively, there are two sources of contribution to whether the user has expressed the slot-value pair under consideration. The first source of contribution is the user utterance, in which the user directly states the goals and requests. An example of this is the user saying "how about a French restaurant in the centre of town?", after the system asked "how may I help you?" To handle these cases, we determine whether the utterance specifies the slot-value pair. Namely, we attend over the user utterance H utt , taking into account the slot-value pair being considered c val , and use the resulting attention context q utt to score the slot-value pair.

where m is the number of words in the user utterance. The score y utt indicates the degree to which the value was expressed by the user utterance.

The second source of contribution is the previous system actions. This source is informative when the user utterance does not present enough information and instead refers to previous system actions. An example of this is the user saying "yes", after the system asked "would you like a restaurant in the centre of town?" To handle these cases, we examine previous actions after considering the user utterance. First, we attend over the previous action representations

taking into account the current user utterance c utt . Here, l is the number of previous system actions. Then, we use the similarity between the attention context q act and the slotvalue pair c val to score the slot-value pair.

In addition to real previous system actions, we introduce a sentinel action to each turn which allows the attention mechanism to ignore previous system actions. The score y act indicates the degree to which the value was expressed by the previous actions.

The final score y is then a weighted sum between the two scores y utt and y act , normalized by the sigmoid function σ.

Here, the weight w is a learned parameter.

3 Experiments

## Dataset

The Dialogue Systems Technology Challenges (DSTC) provides a common framework for developing and evaluating dialogue systems and dialogue state trackers (Williams et al., 2013;Henderson et al., 2014a). Under this framework, dialogue semantics such as states and actions are based on a task ontology such as restaurant reservation. During each turn, the user may inform the system of particular goals (e.g. inform(food=french)), or request for more information from the system (e.g. request(address)). For instance, food and area are examples of slots in the DSTC2 task, and french and chinese are example values within the food slot. We train and evaluate our model using DSTC2 as well as the Wizard of Oz (WoZ) restaurant reservation task (Wen et al., 2017), which also adheres to the DSTC framework and has the same ontology as DSTC2.

For DSTC2, it is standard to evaluate using the N-best list of the automatic speech recognition system (ASR) that is included with the dataset. Because of this, each turn in the DSTC2 dataset contains several noisy ASR outputs instead of a noise-free user utterance. The WoZ task does not provide ASR outputs, and we instead train and evaluate using the user utterance.

## Metrics

We evaluate our model using turn-level request tracking accuracy as well as joint goal tracking accuracy. Our definition of GLAD in the previous sections describes how to obtain turn goals and requests. To compute the joint goal, we simply accumulate turn goals. In the event that the current turn goal specifies a slot that has been specified before, the new specification takes precedence. For example, suppose the user specifies a food=french restaurant during the current turn. If the joint goal has no existing food specifications, then we simply add food=french to the joint goal. Alternatively, if food=thai had been specified in a previous turn, we simply replace it with food=french.

## Implementation Details

We use fixed, pretrained GloVe embeddings (Pennington et al., 2014) as well as character n-gram embeddings (Hashimoto et al., 2017). Each model is trained using ADAM (Kingma and Ba, 2015). For regularization, we apply dropout with 0.2 drop rate (Srivastava et al., 2014) to the output of each local module and each global module. We use the development split for hyperparameter tuning and apply early stopping using the joint goal accuracy.

For the DSTC2 task, we train using transcripts of user utterances and evaluate using the noisy ASR transcriptions. During evaluation, we take the sum of the scores resulting from each ASR output as the output score of a particular slot-value. We then normalize this sum using a sigmoid function as shown in Equation ( 23). We also apply word dropout, in which the embeddings of a word is randomly set to zero with a probability of 0.3. This accounts for the poor quality of ASR outputs in DSTC2, which frequently miss several words in the user utterance. We did not find word dropout to be helpful for the WoZ task, which does not contain noisy ASR outputs.

## Comparison to Existing Methods

Table 1 shows the performance of GLAD compared to previous state-of-the-art models. The delexicalisation models, which replace slots and values in the utterance with generic tags, are from Henderson et al. (2014b) for DSTC2 and Wen et al. (2017) for WoZ. Semantic dictionaries map slot-value pairs to hand-engineered synonyms and phrases. The NBT (Mrkšić et al., 2017) applies CNN over word embeddings learned over a paraphrase database (Wieting et al., 2015) instead of delexicalised n-gram features.

On the WoZ dataset, we find that GLAD significantly improves upon previous state-of-theart performance by 3.7% on joint goal tracking accuracy and 5.5% on turn-level request tracking accuracy. On the DSTC dataset, which evaluates using noisy ASR outputs instead of user utterances, GLAD improves upon previous state of the art performance by 1.1% on joint goal tracking accuracy and 1.0% on turn-level request tracking accuracy.  (Henderson et al., 2014b), delexicalisation WoZ (Wen et al., 2017), and NBT (Mrkšić et al., 2017). We run 10 models using random seeds with early stopping on the development set, and report the mean and standard deviation test accuracies for each dataset. For "-self-attn", we use meanpooling instead of self-attention. For "-LSTM", we compute self-attention over word embeddings.

# Model

## Ablation study

We perform ablation experiments on the development set to analyze the effectiveness of different components of GLAD. The results of these experiments are shown in Table 2. In addition to the joint goal accuracy and the turn request accuracy, we also show the turn goal accuracy for reference.

Temporal order is important for state tracking. We experiment with an embedding-matching variant of GLAD with self-attention but without LSTMs. The weaker performance by this model suggests that representations that capture temporal dependencies is helpful for understanding phrases for state tracking.

Self-attention allows slot-specific, robust feature learning. We observe a consistent drop in performance for models that use mean-pooling as opposed to self-attention (Equations ( 4) to ( 6)). This stems from the flexibility in the attention context computation afforded by the self-attention mechanism, which allows the model to focus on select words relevant to the slot-value pair under consideration. Figure 4 illustrates an example in which local self-attention modules focus on rele-vant parts of the utterance. We note that the model attends to relevant phrases that n-gram and embedding matching techniques do not capture (e.g. "within 5 miles" for the "area" slot).

Global-local sharing improves goal tracking. We study the two extremes of sharing between the global module and the local module. The first uses only the local module and results in degradation in goal tracking but does not affect request tracking (e.g. β s = 1). This is because the former is a joint prediction over several slot-values with few training examples, whereas the latter predicts a single slot that has the most training examples.

The second uses only the global module and underperforms in both goal tracking and request tracking (e.g. β s = 0). This model is less expressive, as it lacks slot-specific specializations except for the final scoring modules.

Figure 5 shows the performance of the original model and the two sharing variants across different numbers of occurrences in the training data. GLAD consistently outperforms both variants for rare slot-value pairs. For slot-value pairs with an abundance of training data, there is no significant performance difference between models as there is sufficient data to generalize.

## Qualitative analysis

Table 3 shows example predictions by GLAD. In the first example, the user explicitly outlines requests and goals in a single utterance. In the second example, the model previously prompted the user for confirmation of two requests (e.g. for the restaurant's address and phone number), and the user simply answers in the affirmative. In this case, the model still obtains the correct result by leveraging the system actions in the previous turn. The last example demonstrates an error made by 

# Related Work

Dialogue State Tracking. Traditional dialogue state trackers rely on a separate SLU component that serves as the initial stage in the dialogue agent pipeline. The downstream tracker then combines the semantics extracted by the SLU with previous dialogue context in order to estimate the current dialogue state (Thomson and Young, 2010;Wang and Lemon, 2013;Williams, 2014;Perez and Liu, 2017). Recent results in dialogue state tracking show that it is beneficial to jointly learn speech understanding and dialogue tracking (Henderson et al., 2014b;Zilka and Jurcicek, 2015;Wen et al., 2017). These approaches directly take as input the N-best list produced by the ASR system. By avoiding the accumulation of errors from the initial SLU component, these joint approaches typically achieved stronger performance on tasks such as DSTC2. One drawback to these approaches is that they rely on hand-crafted features and complex domain-specific lexicon (in addition to the ontology), and consequently are difficult to extend and scale to new domains. The recent Neural Belief Tracker (NBT) by Mrkšić et al. (2017) avoids reliance on hand-crafted features and lexicon by using representation learning. The NBT employs convolutional filters over word embeddings in lieu of previously-used hand-engineered features. Moreover, to outperform previous methods, the NBT uses pretrained embeddings tailored to retain semantic relationships by injecting semantic similarity constraints from the Paraphrase Database (Wieting et al., 2015;Ganitkevitch et al., 2013). On the one hand, these specialized embeddings are more difficult to obtain than word embeddings from language modeling. On the other hand, these embeddings are not specific to any dialogue domain and are directly usable for new domains.

Neural attention models in NLP. Attention mechanisms have led to improvements on a variety of natural language processing tasks. Bahdanau et al. (2015) propose attentional sequence to sequence models for neural machine translation. Luong et al. (2015) analyze various attention techniques and highlight the effectiveness of the simple, parameterless dot product attention. Similar models have also proven successful in tasks such as summarization (See et al., 2017;Paulus et al., 2018). Self-attention, or intra-attention, has led improvements in language modeling, sentiment  analysis, natural language inference (Cheng et al., 2016), semantic role labeling (He et al., 2017), and coreference resolution (Lee et al., 2017). Deep self-attention has also achieved state-of-the-art results in machine translation (Vaswani et al., 2017). Coattention, or bidirectional attention that codependently encode two sequences, have led to significant gains in question answering (Xiong et al., 2017;Seo et al., 2017) as well as visual question answering (Lu et al., 2016).

Parameter sharing between related tasks. Sharing parameters between related tasks to improve joint performance is prominent in multitask learning (Caruana, 1998;Thrun, 1996). Early works in multi-tasking use Gaussian processes whose covariance matrix is induced from shared kernels (Lawrence and Platt, 2004;Yu et al., 2005;Seeger et al., 2005;Bonilla et al., 2008). Hashimoto et al. (2017) propose a progressively trained joint model for NLP tasks. When a new task is introduced, a new section is added to the network whose inputs are intermediate representations from sections for previous tasks. In this sense, tasks share parameters in a hierarchical manner. Johnson et al. (2016) propose a single model that jointly learns to translate between multiple language pairs, including one-to-many, many-to-one, and many-to-many translation. Kaiser et al. (2017) propose a model that jointly learns multiple tasks across modalities. Each modality has a corresponding modality net, which extracts a representation that is fed into a shared encoder.

# Conclusion

We introduced the Global-Locally Self-Attentive Dialogue State Tracker (GLAD), a new state-ofthe-art model for dialogue state tracking. At the core of GLAD is the global-locally self-attention encoder, whose global modules allow parameter sharing between slots and local modules allow slot-specific feature learning. This allows GLAD to generalize on rare slot-value pairs with few training data. GLAD achieves state-of-theart results of 88.1% goal accuracy and 97.1% request accuracy on the WoZ dialogue state tracking task, as well as 74.5% goal accuracy and 97.5% request accuracy on DSTC2.

# Acknowledgement

We thank Nikola Mrkšić for providing us with a preprocessed version of the DSTC2 dataset.

