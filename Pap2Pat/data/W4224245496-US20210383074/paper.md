# Introduction

Reinforcement Learning (RL) has been used in NLG tasks including neural machine translation (NMT) (Bahdanau et al., 2017), abstractive summarization (Paulus et al., 2018), and specifically in controlled text generation tasks such as paraphrase generation (Li et al., 2018c), sentence simplification (Zhang and Lapata, 2017) and unsupervised text style transfer (Luo et al., 2019;Gong et al., 2019).

Unsupervised text style transfer is the task of re-writing text of a given style into a target style without using a parallel corpus of source style and target style sentences for training. For example, in the case of sentiment transfer 1 , 'the pizza was 1 Similar to previous works, we use a broad socio-linguistic rather bland' can be re-written with positive sentiment as 'the pizza was quite delicious'.

RL has gained popularity in this task as it allows to directly optimize for commonly agreed upon objectives of style transfer, i.e, the generated sentences should 1) possess the target style, 2) preserve the non-stylistic parts (content) of the source sentence, and 3) be fluent and natural sounding. However these objectives are typically measured only at the level of the entire generated text and hence, any RL rewards based on them are only available as 'sparse rewards'. For example, Gong et al. (2019) use a style classifier model to provide a target style reward, which requires the complete generated text. On the other hand, generative RL models generate token-by-token, and require 'credit assignment' of reward to each individual token, based on their contribution to the overall sparse reward.

To address this problem, previous work uses different 'reward shaping' strategies over the sparse reward, of which, the 'roll-out strategy' based on Monte Carlo Tree Search (Kocsis and Szepesvári, 2006) is the commonly used approach. In the context of style transfer, Gong et al. (2019) use the roll-out strategy while Luo et al. (2019) use a naive reward shaping strategy of assigning the same discounted sparse reward to every token. However, as observed by Wu et al. (2018), the gains from these reward shaping strategies are negligible in practice. Since NLG tasks have a large action space (the vocabulary), sparse rewards leads to high variance in estimating 'returns' for each token used in policy gradient updates. This makes the training sample-inefficient, and can result in a sub-optimal policy.

In contrast to the roll-out strategy, we propose a novel approach to provide dense rewards directly to each generated token. The primary differentiating factor is that these dense rewards are obtained directly through reward models trained using the Our method of providing dense rewards is inspired by Shi et al. (2018) and Sudhakar et al. (2019). Shi et al. (2018) propose using Inverse Reinforcement Learning (IRL) (Ziebart et al., 2008) to compute dense rewards for unsupervised text generation. Their objective is to learn un-conditional generation of sentences that belong to a particular distribution for which they use a language model's token-level likelihood as a dense reward approximator. Sudhakar et al. (2019) disentangle style tokens and content tokens using self-attention scores of trained BERT style-classifier (Devlin et al., 2018). Style tokens are those that contribute to the style of the overall text. Content tokens are non-style tokens.

We propose separate dense rewards at the tokenlevel for each of target style, content preservation and fluency. a) For the style reward, we propose the use of self-attention scores of a trained style classifier (Sudhakar et al., 2019). b) For content preservation, we propose a simple n-gram based dense reward, motivated by BLEU (Papineni et al., 2002), and applicable to only content tokens. c) For the fluency reward, we use a pre-trained language model's token-level likelihood, motivated by Shi et al. (2018).

The main contribution of our work is in that we propose a method that addresses the sparse reward problem for RL-based unsupervised text style transfer. We demonstrate how the resulting dense rewards can be used in designing a state-ofart RL-based style transfer system. This method, as compared to the roll-out strategy is a) sample efficient, b) converges to a better reward and c) computes token level reward in O(T ) as against O(T 2 ), where T is the number of tokens in the output. The method we propose is extensible to other controlled text generation problems.

# Related Work

The previous section refers to RL-based related work in unsupervised text style transfer. We discuss a few more aspects about these works here. Xu et al. (2018) uses a cycled RL approach where a neutralization model disentangles the content and attributes, and then passes the content to an emotionalization model. Similar to our work, Gong et al. (2019)  Non-RL based approaches too have been used for unsupervised text style transfer. Some of these works encode style and content in separate latent representations, and decode the style-dependent output from these representations (Fu et al., 2018;Hu et al., 2017;Yang et al., 2018). Other works that attempt to learn disentangled latent representations include John et al. (2019); Zhao et al. (2018); Wu et al. (2019a); Liu et al. (2019). A few others explicitly identify attribute and content words from input texts and then train models to generate target style sentences from the content (Li et al., 2018a;Sudhakar et al., 2019;Wu et al., 2019b). A few recent works (Lample et al., 2018;Luo et al., 2019) avoid style-content disentanglement altogether.

RL has also been used for unconditional text generation tasks. Shi et al. (2018) propose the use of Inverse RL (IRL), Schmidt and Hofmann (2020) use a retrieval-based method, comparing the generated sentence with the retrieved reference using contextual BERT embeddings to get compute dense rewards, while Yu et al. (2017) use the roll-out strategy.

# Problem Statement

We assume a dataset D = {(x 1 , s 1 ), ..., (x m , s m )} where each sentence x i is associated with a specific style s i ∈ S. For instance, for the task of sentiment transfer, S = {'Positive', 'Negative'}, and for formality transfer, S = {'Formal', 'Informal'}. We then aim to learn the conditional distribution P (y|x, s tgt ) such that the target (tgt) style of y is s tgt , and y's content is similar to that of x. 'Content' refers to the non-stylized part of the input.

# Our Approach

We introduce the efficient Dense (Reward) Reinforcement Learning based Style Transformer (hereby, DRL). DRL takes the source sentence x of style s src as input and generates the output sentence y of style s tgt . More formally, it learns:

The RL-based setup consists of: a) a generative model, b) the training strategy and c) the rewards.

## Model

The architecture of DRL is a decoder-only Transformer, based on the implementation of the Generative Pre-trained Transformer (Radford et al.) (hereby, GPT), and is similar to that used by Sudhakar et al. (2019). The input to the model is the source sentence, as well as a marker indicating the target style, and the output is a sentence in the target style. We use the same input representation as Sudhakar et al. (2019). Following common practice (Luo et al., 2019;Wu et al., 2018) the training takes place in two phases: a) MLE pre-training, followed by b) RL training.

## MLE Pre-training

As shown by previous work (Luo et al., 2019;Wu et al., 2018;Gong et al., 2019) supervised or pseudo-supervised training helps with faster and sample efficient convergence. We pre-train DRL on a synthetically generated parallel corpus. We create this parallel corpus by using previous style transfer models, hereby 'baseline models' (described in section 5.2) on the original non-parallel corpus. This pre-training is performed by minimizing the standard MLE objective.

## RL Training

DRL optimizes a policy using the policy gradient, to maximize a long term reward J(θ). The parameters of the model θ define a policy π θ (y t |s t ) which maps a state s t to an action y t . The state s t in our case in the input sentence x concatenated with the tokens generated by the policy till time t -1, i.e., s t = (x, y 1..t-1 ). The action y t is the token sampled from the vocabulary V . Sampling: For an input sentence x, we generate an output sentence by sampling from the vocabulary at each timestep t. Each output token (action) is sampled from the model's softmax distribution over the vocabulary (action space). We use a 'top-p sampling' (alternatively, 'nucleus sampling') (Holtzman et al., 2019) for the same. This sampling method samples a token from the set of top tokens that make up a cumulative softmax probability of p. For each input sentence x in the RLtraining set, we generate K different outputs by repeating the above process K times to get better estimation for the return.

# Policy Gradient:

We use the REINFORCE (Williams, 1992) policy gradient algorithm. RE-INFORCE relies on an estimated return by Monte-Carlo methods, using episode samples to update the policy parameter θ.

(2) Here Q π (s t , y t ) is the action-value function and is equal to the expected return of the state-action pair (s t , y t ). In the case of REINFORCE, it is estimated from the samples collected with the current policy π θ . b is the baseline, which helps to reduce the variance in return estimation. Williams (1992) discuss different methods to calculate baseline. We use a constant baseline, which is the average of Q π (s t , y t ) over all generated tokens during the batch gradient update.

Here, T is the episode length, γ ∈ [0, 1] is the discount factor and r t is the reward associated with (s t , y t ).

## Rewards

The model is provided with token-level dense rewards that indicate: 1) how well the generated text reflects target style, 2) how much of the content it preserves from the input, and 3) fluency. The final reward for each token is the weighted sum of these individual rewards. Separate rewards have also been used by Luo et al. (2019) and Gong et al. (2019).

### Target Style Reward

We train a BERT style-classifier with weights θ CLS and use its self-attention scores to provide a reward for the target style. The classifier has multiple attention heads. Sudhakar et al. (2019) isolate a single attention-head such that the self-attention scores α of this head correspond to how much a token contributes to the style of the output. To do this, they use a 'leave-one-out' approach on the dev set, computing α for each head, and then removing the top λ * |x| tokens based on α, from the input sentence x. Here λ ∈ [0, 1] is a parameter tuned for each dataset and |x| represents number of tokens in the sentence x. The head for which the classifier's score deviates the most is the one which Sudhakar et al. (2019) used to disentangle style and content tokens.

Using the same procedure, we arrive at a candidate head, and use its self-attention scores α to assign a token level reward rs t . Formally, if the attention score associated with token y t is α yt then the style reward for each token y t of the generated sentence y is,

where,

The tokens which influence the style of the sentence will be rewarded with P (s tgt |y; θ CLS ) -0.5, and purely content related tokens will receive a reward of 0.

### Content Preservation Reward

We use an n-gram based content reward to encourage the model to preserve content from the input. Let us define G t as the set of n-grams up to order 3 (set heuristically) associated with token y t of the generated sentence y and c(x t ) is the context window for the t th token in the input sentence x. G t = {{y t }, {y t-1 , y t }, {y t , y t+1 }, {y t-2 , y t-1 , y t }, {y t , y t+1 , y t+2 }} (6)

The context preservation reward rc t for token y t is,

Where mask is as described in (5). The term (1 -mask) emphasises the fact that content preservation reward should apply to content tokens only and style tokens should not receive negative rewards for not preserving the content.

### Fluency Reward

The fluency reward should apply to both attributes and content words. It should ensure that they are coherently used in context. Li et al. (2018b) observe that content preservation metrics (such as BLEU) do not correlate with human scores for fluency. Hence a separate fluency reward is necessary.

We fine-tuned a pre-trained GPT (Radford et al.) model on the training data with language modeling (LM) task. We then use it to determine the fluency of each token y t using (10). We note here that d'Autume et al. ( 2019), use a similar dense reward to ours. We design the fluency reward as the LM likelihood:

4.4.4 Overall Reward:

The overall reward (r t ) for each token is a weighted sum of the style, content and fluency rewards from equations 4, 9 and 10:

λ S , λ C and λ F are reward weights. We heuristically set λ S = 2.0, λ C = 1.0 and λ F = 0.5.

Figure 1 

## Return Estimation

It must be mentioned here that in previous work (Luo et al., 2019;Gong et al., 2019), the value of the discount factor γ is set to a non-zero value in eq. 3. This is to allow for estimation of token-level return from sparse rewards. However, the proposed method of designing dense rewards, solves the credit assignment problem directly. Consequently, there is no dependency on future rewards to estimate Q π (s t , y t ). Hence, we set the value of γ to 0.

# Experiments

## Datasets

Following are brief descriptions of the datasets we use, borrowed from works that use them previously. YELP: Each sentence is from a business review on Yelp, and is labeled as having either positive or negative sentiment (Li et al., 2018b). The task is to transfer positive sentences to negative sentences and vice-versa. Li et al. (2018b) publish a set of human reference outputs on the test set of YELP. GYAFC: Each sentence is labeled as either being formal or informal. We only use a subset of this dataset which corresponds to Yahoo answers in the Family and Relationships domain. The task is to transfer formal to informal sentences and viceversa. Rao and Tetreault (2018) publish a set of human reference outputs on the test set of GYAFC. Though GYAFC has source and target sentences aligned, we discard these alignments, since our problem setting is unsupervised. Table 1 shows train, dev and test statistics of the datasets.

## Baseline Models

A baseline model refers to a pre-trained version of DRL, as described in section 4.2. We pre-train   (Sudhakar et al., 2019), and c) for BGST-S B , using BGST-Small, which is BGST trained over a subset of the training data (5%).

## Reproducibility

All models described below are used from Huggingface2 (Wolf et al., 2020). Style Classifier: We train the BERT-base uncased model with the default hyper-parameter setting. Generator: We use GPT (Radford et al.) as the generator model. The Generator training is done in two phases, 1) LM pre-training and 2) RL training. Pre-training: We train over GPT's pre-trained model for our pseudo-supervised pre-training RL-training: We set learning rate to lr = 6.25e -6, and gradient clipping to 1 to avoid overflow. Other hyper-parameters are set to the default values provided.

## Evaluation Methods

### Human Evaluation

We obtain human evaluations of model outputs from crowd workers on MTurk. For each source sentence and target style, we present the outputs of all models being compared, to the same workers. They are all native English speakers from North America and were made familiar with the datasets. They were asked to rate each output on the following three criteria, each on a Likert scale from 1 to 5: a) target style match (Sty.), b) content preservation (Con.), c) fluency (Flu.). We also calculate the overall success rate (All) as the percentage of times a model received either a 4 or a 5 on all the above three criteria.

### Automatic Evaluation

To measure target style strength (Sty.) of outputs, we use a pre-trained FastText 3 (Joulin et al., 2017) style classifiers for each dataset, which achieve accuracies of 96.5% and 89.5% on the test sets of YELP and GYAFC respectively. For content preservation (Con.), we calculate the average BLEU scores of the output with respect to the human reference sentences. Fluency (Flu.) is estimated by finetuning pre-trained OpenAI GPT-2 (Radford et al., 2019) models (different from any of the GPT models used in this work) on each dataset's training set, and using them to obtain the perplexity of the output sentences. They achieve perplexities of 21.42 and 52.5 on the test sets of YELP and GYAFC respectively. We also calculate the geometric mean, GM (All), of style and content scores. It must be noted, however, that most previous works such as Li et al. (2018b) and Sudhakar et al. (2019) note that human evaluations are more reliable than automatic evaluations. Hence, in all further analysis in this work, we draw conclusions from the human evaluations.

# Results

## Improvement over Baseline Models

As mentioned in section 5.2, we further train each baseline model using dense RL rewards. We observe that our novel RL training provides significant improvement over each of these baseline models. To further distill the effects of RL separately, we consider an additional simple baseline model (SOURCE B ), trained on a parallel corpus where the target sentence is the same as the source sentence. Human evaluations of these models are presented in Table 2. These evaluations show that DRL significantly improves over a variety of baseline (BL) models on style, content as well as fluency, irrespective of their original style transfer capabilities.

## Comparison with Roll-out

We compare dense rewards with the roll-out strategy. To do so, we train a RL style transfer model which uses the roll-out strategy for reward shaping, as used by Gong et al. (2019). We keep all other factors such as pre-training and model architecture same. We compute the rolled out reward r t using the same process as Gong et al. (2019). We set mask = 1 in eq. 4 to 3 https://fasttext.cc/ calculate style reward rs t and mask = 0 in eq. 9 to calculate content reward rc t . We set γ = 1 while calculating estimated return Q π (s t , y t ) using equation 3. This allows us to train a Roll-Out model (RO) which a) has the same architecture as DRL described in section 4 and b) is pre-trained with a synthetic corpus generated by the BGST-S B baseline.

# Analysis:

We compare a) RO, b) its baseline model BGST-S B and c) DRL trained over the same baseline model. These results are presented in Table 2. The results indicate the superior performance of dense rewards in comparison to the roll-out strategy.

## Sample Efficiency

In Figure 2, we compare the sample efficiencies of our DRL and RO. The overall reward ( 11) is normalized between 0 to 1 for easy visualization as the training steps progress. The peak reward of DRL is higher than RO in both cases. On YELP, DRL reaches its peak reward after 25K episodes whereas RO takes 74K episodes. On GYAFC, DRL takes 40K episodes, whereas RO takes 83K. Since all other factors are kept same in both setups, these gains can be attributed to accurate dense rewards for each token, resulting in better estimation of Q π (s t , y t ), sample efficiency and convergence of the policy.

### Training Time

The roll-out itself is an expensive operation, requiring O(T 2 ) computations for one complete output, where T is the output length. Time complexity for self-attention based reward shaping is O(T ). In practice, training DRL is 4x faster than RO on YELP, and 10x faster on GYAFC, owing to the differences in average sentence length.

## Comparison with Fully Attention-based Reward

As an additional experiment, we explore directly using attention scores in the style and content rewards, without explicitly separating attributes and content. We modify the reward coefficient mask in equation 5 (which will reflect in the style and content rewards) to the attention weight as: mask = α t and train the attention-reward model (DRL-At) over the BGST-S B baseline model, keeping all else the same as DRL.

Analysis: We compare a) DRL-At, b) its baseline model BGST-S B and c) DRL trained over the same baseline model. These results are presented in Table 2. While DRL-At does give encouraging results, we see that it still performs narrowly worse than DRL. We surmise that this might be because a) every word is assigned both a content and style reward, even though there exists a hard separation between content and attributes in most cases, and b) raw attention scores might not be the most appropriate reward coefficients.

## Comparison with Previous Works

We compare our results with previous works that use different approaches for style transfer. We choose the state-of-art work from each approach. Multi Decoder (MD) (Fu et al., 2018) uses adversarial training to separate content and attribute. Back-Translation (BT) (Prabhumoye et al., 2018) uses back-translation that has reduced style, and then generate style-specific outputs. We also compare with RL based approaches described in previous sections. UnPaired (UnP) (Xu et al., 2018) uses a cyclic RL approach, RL-roll-out (RL-RO) (Gong et al., 2019) uses the roll-out strategy and DualRL (DuR) (Luo et al., 2019) uses a naive reward shaping. Finally, DO (Li et al., 2018b) and BGST (Sudhakar et al., 2019) both separate content and attributes, and train a generative model to reconstruct the source sentence, given only the content. Evaluations of these works and ours are presented in Table 3. In this table, DRL refers to DRL trained over the BGST B baseline model, since it is our best performing from Table 2.

# Analysis:

We see that DRL improves over previous state-of-art models by a good margin on all metrics across all datasets, according to both human and automatic evaluations. On the overall scores (All), we improve over previous state-of-the art model (DuR) by 21% each on YELP and GYAFC, according to human evaluation in Table 3. From manual inspection we observe that DRL performs better than previous state-of-art models in the following ways: 1) maintains consistent context across longer sentences, 2) maintains consistency of style even for sentences having multiple attribute words, 3) produces output sentences having appropriate and meaningful attributes, many of which the model has not observed at training time, and 4) does away with redundancy and repetition of words in output sentences, which is commonly observed in previous works.

# Sentiment versus formality:

The last row in Table 3 shows the performance of humans (H) for each of the datasets. Humans perform better on YELP as compared to GYAFC, according to human evaluations. Further, through manual annotation from crowd workers on Mturk4 , we observe that the average percentage of word changes to generate target style sentence is 23% for YELP, and 39% for GYAFC. The average sentence length is 8 words in YELP and 13 words in GYAFC. These statistics, along with manual investigations suggest that formality transfer on GYAFC is a more complex and ambiguous task than sentiment transfer on YELP. The efficacy of using dense rewards is further shown by the fact that DRL is only 6% worse than humans on GYAFC.

Table 4 shows example outputs generated by our models from the test set.

# Conclusion

We present a novel method to provide dense rewards for unsupervised text generation and compare it with the currently used roll-out strategy using ablation studies. We demonstrate the use of these dense rewards in building a state-of-art text style transfer system.  YELP (Positive to Negative) steve was professional and found exactly the right unit to fit in our space steve was rude and didn't have the right unit to fit in our space . YELP (Negative to Positive) they tried to take advantage of me because i am young .

they take great care of me because i am young . GYAFC (Formal to Informal) do not approach her and let her know that you find her looks very attractive. don't approach her and let her know that you like her . GYAFC (Informal to Formal) well that is just the way it is I guess. that is just the way it is , i would advise . 

