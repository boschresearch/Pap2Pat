# INTRODUCTION

In contrast to the traditional modular-based ASR system that consists of an acoustic model, a language model (LM) and a rule-based decoder, the recent end-to-end (E2E) approach aims at implementing the ASR process using a single neural network model. In particular, both attention-based encoder-decoder [1][2][3][4] and recurrent neural network transducer (RNN-T) [5][6][7][8][9][10] methods achieve a coherently integrate acoustic and text information using a recurrent structure between the previous and current subword units in the output text sequence in contrast to modular-based ASR systems. Recently, RNN-T has become more prevalent due to its streaming benefits [11][12][13][14][15][16][17].

RNN-T was first proposed to extend a connectionist temporal classification (CTC) acoustic encoder [18] with a prediction network serving as an LM. Acoustic and text representations over phonemes are derived separately from the acoustic encoder and prediction network, and fused using an addition followed by a softmax function to produce the final output distributions [5]. Shortly afterward, an improvement was introduced to fuse more compressed hidden representations using concatenation and a fully connected (FC) layer with a hyperbolic tangent (tanh) function [6], which is termed as the joint network. The fused representations are further transformed by the output layer, which is another FC layer with the softmax function, into the output distributions. Since then, there has been a research focus to improve the RNN-T encoder structure, from using the long short-term memory (LSTM) model [19,20] to Transformer and Conformer [14,21], and to improve their streaming performance and ondevice efficiency [11,22,23]. More recently, many studies focus on Thanks Dr. Zhehuai Chen and Dr. Matt Shannon for useful suggestions.

improving the recognition accuracy on long tail words/phrases and long-form utterances, which results in the use of extra model components [15,24], novel prediction network structures and decoding algorithms [7,25,26], alternative subword units to output [11,20], test-time external language model integration [27][28][29], and synthetic data augmentation and knowledge distillation methods [11,[30][31][32].

Though joint network is the component closest to the output layer and is important to RNN-T performance, there are only a few studies related to it [6,28,33]. In this paper, by viewing the function of the joint network as to fuse the representations of the acoustic and text modalities, we propose to improve the joint network implementation using different structures for information fusion, including gating and a low-rank approximation of bilinear pooling with shortcut connections and a tanh transform. A better-performing structure is further proposed by stacking bilinear pooling on top of gating. Furthermore, since text priors are often easier to learn than complex acoustic patterns, the prediction network often converges much faster than the acoustic encoder that causes the joint network overly biased towards the prediction network. To alleviate this issue, a novel regularisation method is proposed to penalise the gradients back-propagated into the prediction network in early training stages, which can improve RNN-T performance without bringing any cost to both training and test. Experiments were conducted on a large-scale multilingual ASR setup for voice search, similar to the one used in [34]. As a result, by jointly using these proposed methods, more than 4% relative word error rate (WER) reductions were achieved by only increasing a few million extra parameters.

The rest of the paper is organised as follows: Sec. 2 reviews RNN-T and the work related to joint network. Sec. 3 gives details of the proposed joint network structures and the regularisation method. Sec. 4 describes our experimental setup, followed by the discussions on the results in Sec. 5. We conclude in Sec. 6.

# BACKGROUND

## RNN Transducer

In the traditional statistical ASR framework, [35], speech is produced and encoded via a noisy channel and the ASR system is to find the most probable source text sequence y * given the acoustic feature sequence x1:T of length T observed as the output of the channel. Based on Bayes' rule, decoding follows the maximum a posteriori rule to search over each possible hypothesized text sequence y by P (y|x1:T ) ∝ p(x1:T |y)P (y),

where p(x1:T |y) is estimated by the acoustic model and is the likelihood of generating x1:T through the channel; P (y) is estimated by an LM, describing the underlying probabilistic distribution of the source text.

Instead of modelling p(x1:T |y) and P (y) by independent models in a modularised system, E2E methods, such as RNN-T, directly models P (y|x1:T ) by a single model. Let y = y1:U where U is the number of subword units in y. For a streaming setting without any look ahead frame and time reduction, h enc t , the D enc -dimensional (-dim) acoustic representation extracted by the acoustic encoder at time t, h pred u , the D pred -dim text representation of the u-th subword unit by the prediction network, and h joint t,u , the D joint -dim fused representation generated by the joint network, are calculated as follows:

where y0 refers to the special start of sentence symbol; k and W out are the k-th node and weights of the output layer. Regarding a set of subword units V, the symbol that k represents belongs to V ∪ {∅}, where ∅ is the blank symbol indicating no subword is emitted. During training, let ŷ = {ŷ1, ŷ2, . . . , ŷT +U } be an alignment sequence of y that can be converted into y by removing all occurrences of ∅, A(x1:T , y) be the reference lattice including all possible alignment sequences between y and x1:T , P (y|x1:T ) can be computed efficiently with the forward-backward procedure. There is

where ti and ui are the values of t and u corresponding to ŷi in ŷ.

In practice, AcousticEncoder(•) can be Conformer with a fixed number of look ahead frames and a fixed time reduction rate. PredictionNetwork(•) is often a multi-layer LSTM. The joint network is often defined as an FC layer [6] that

where W joint 1 and W joint 2 are weight matrices. For simplicity, bias is ignored in Eqn. (7) and the rest of the paper.

If W joint 2 is 0 D joint ×D pred and the joint network transforms only the acoustic representation, apart from their difference in A(x1:T , y) [11,28], RNN-T becomes CTC that calculates P (ŷi|x1:t i ) by making an independence assumption between any subword units in y. This reveals the importance of the joint network.

## Related work

In Eqn. (7), by enforcing h enc t = 0, the prediction network, joint network, and output layer jointly form an LSTM LM that is often referred to as the internal LM [28]. Studies showed that more WER reductions can be found from shallow fusion with external LMs by discounting the internal LM scores at test-time [27][28][29]. More recently, stateless RNN-T has been proposed to truncate the LM history embedded in the prediction network to n-gram [25].

The fusion of representations associated with different modalities plays a key role in multimodal intelligence [36]: attention, gating, and bilinear pooling are the most commonly used structures for the purpose. In RNN-T, the standard joint network implemented based on Eqn. (7) can be viewed as to fuse the acoustic representation h enc t and text representation h pred u using an FC layer. Recently, an alternative joint network structure is proposed to model the multiplicative interactions between the two representations [33]:

where is the Hadamard product.

# FUSING ACOUSTIC AND TEXT REPRESENTATIONS

Fusing acoustic and text representations is arguably a difficult task, and the standard joint network simply uses one FC layer. Sec. 3.1 and 3.2 propose more complex joint network structures, and Sec. 3.3 proposes to improve the balance between the two modalities.

## Gating mechanism

Gating has been widely used in recurrent and shortcut structures [19,37], whose most famous application is LSTM. It allows each element in each representation vector to be scaled with a different dynamic weight, before being integrated via vector addition. Specifically,

where gt,u is the gating vector, σ(•) is sigmoid function, and W gate 1 and W gate 2 are weight matrices of the gating layer. Notably a different gating vector can be computed to replace 1 -gt,u. However, we observed worse WERs when using two separate gating vectors.

## Bilinear pooling

Compared to gating, bilinear pooling is a more powerful and expensive method for fusing multimodal representations [38], which combines two vectors using the bilinear form (with bias ignored)

where where Vector(•) and ⊗ are the vectorisation and outer product operations. Compared to gating, bilinear pooling first computes the outer product of the two vectors to capture the multiplicative interactions between all possible element pairs in a more expressive D enc ×D preddim space, and then projects it into a D joint -dim vector space.

To avoid the issues when estimating a high dimensional weight tensor, a low-rank approximation

T is suggested [39], where W low 1,d and W low 2,d are D enc × D rank -dim and D pred × D rank -dim matrices, and D rank is the rank of W bi d . Therefore Eqn. (10) can be rewritten as

as W low 1 and all W low 2,d as W low 2 , and to use a projection matrix W proj to distinguish the elements in h joint t,u [40]. When a tanh function is used to transform the vectors before the Hadamard product, there is

We found using shortcut connections [41] and a final tanh transform are important for bilinear pooling for RNN-T, and thus propose

where W joint 1 h enc t and W joint 2 h pred u are the shortcut connections here.

At last, we propose a stack structure to combine gating and bilinear pooling to leverage their complementarity. It is implemented by replacing Eqn. (11) with

where h gate t,u refers to the joint representation computed by Eqn. (9).

## Prediction network regularisation

It has been observed that strong and prevalent text priors (e.g. "bananas are yellow") often caused image-text multimodal systems to overfit to the statistical biases and tendencies, and largely circumvents the need to understand visual scenes [42]. Similary in RNN-T, since text priors are often easier to learn than the acoustic patterns, it is possible that the faster converging speed of the prediction network (than the acoustic encoder) makes h pred u overly weighted in h joint u,t . In that situation, the acoustic encoder is less well trained to handle the audio samples with high internal LM scores.

In order to resolve this issue, we propose a prediction network regularisation method applied to the beginning of RNN-T training.

# It is implemented by recomputing the text representation as

where m is the index of current training step, αm is a scaling factor, sg(•) is the stop gradient function whose input tensor will have zero gradients. When 0 αm 1, the value of h pred u will not be changed but its corresponding gradients that back-propagate into the prediction network will be reduced by a factor of αm. This slows down the convergence of the prediction network and makes the joint network fuse h enc t and h pred u in a more balanced way. In this paper, a piece-wise linear scheduler is used to control the value of αm:

where m1 and m2 are two pre-defined hyper-parameters. Notably, this method is different from initialising RNN-T with a pre-trained CTC model even when αm = 0, since the prediction network serves as a random but fix-valued projection, through which RNN-T is still able to obtain yu-1. This links to the stateless RNN-T [25].

# EXPERIMENTAL SETUP

## Datasets

Experiments were conducted on a dataset with 9 language locales: US English (en-US), UK English (en-GB), French (fr-FR), Italian (it-IT), Germany (de-DE), US Spanish (es-US), ES Spanish (es-ES), Taiwan Chinese (zh-TW) and Japanese (ja-JP). All data are anonymised and hand-transcribed. There are totally 214.2M utterances which correspond to 142.3K hours of speech data collected from Google's Voice Search traffic. en-US and en-GB take about 25% and 5% of the training data, while each of the rest 7 languages takes about 10% of the data. The SpecAugment method is used to improve ASR robustness against noisy conditions [43]. The training data is mixed with all languages without using any language id information. The test sets are kept distinct for each language with each of them containing 3.3K∼15.4K utterances. The testing utterances are also sampled from Google's Voice Search traffic with a maximum duration constraint of 5.5 second long for each utterance.

The test sets have no overlapping from the training set for evaluation purpose.

## Model setup

The 80-dim log-mel filter bank features are used, which are computed using a 32ms frame length and a 10ms shift. Acoustic features from 3 contiguous frames are stacked and subsampled to form a 240-dim input representation with 30ms frame rate, which are then transformed using a linear projection to 512-dim and added with positional embeddings. Twelve Conformer [21] encoder blocks with 8-head self-attention and a convolution kernel size of 15 are used to further transform the stacked features. A concatenation operation is performed after the 3rd block to achieve a time reduction rate of 2, and the resulted 1024-dim vectors are transformed by the 4th Conformer block and then projected back to 512-dim using another linear transform. Afterwards comes with another 8 Conformer blocks followed by a final linear normalisation layer. These layers combined together form the RNN-T acoustic encoder. The prediction network consists of two layers of 2,048-dim LSTM with a 640-dim linear projection to make D pred =640. The dimension of the fused representation D joint is also set to 640. All models are trained to predict 16,384 word-piece units [44]. As a result, the final RNN-T baseline has 110M parameters in the acoustic encoder and 33M parameters in the rest of the model. All models are trained in Tensorflow using the Lingvo toolkit [45] on Google's Tensor Processing Units V3 with a global batch size of 4,096 utterances. Models are optimized using synchronized stochastic gradient descent based on the Adam optimiser with β1 = 0.9 and β2 = 0.999. During test, the models are tested in a fully E2E fashion without any external LMs.

# EXPERIMENTAL RESULTS

In this section, RNN-T systems with different joint network structures are first compared at the 200K-th training step, whose details are listed in Table 1. Next, prediction network regularisation with different hyper-parameter values are compared using S4 at the 500Kth step. Final results are presented with 800K training steps.  12) 640 640 3.36M

## On joint network structures

The results of RNN-T models with different joint networks are presented in Table 2. First, S0 and S2 result in similar WERs, which validates the finding in [33]. Next, by increasing D joint from 640 (S0) to 790 (S1), the averaged WER was only slightly reduced by 0.03%. We also tried to add more FC layers to the joint network that resulted in worse training loss values and higher WERs. Both gating (S3) and bilinear pooling (S4) outperformed FC fusion systems S0 and S1, where S1 has the same amount of parameters as S3 and S4 indicating that the lower WERs of S3 and S4 do not come from the extra model parameters. Furthermore, S4 outperformed S3 meaning that bilinear pooling can produce more expressive joint representations. Another advantage of bilinear pooling is    

## On prediction network regularisation

The results of using the prediction network regularsation defined in Eqns. ( 14) and ( 15) with different m1 and m2 values are shown in Fig 1 . S4, the bilinear pooling joint network with D rank = 640, is used in this section. The best results were found with m1 =25K and m2 =200K, which improved the averaged WER by 0.09%, 0.07%, and 0.13% absolute with 200K, 500K, and 800K steps separately.

## Final results

The models are trained for 800K training steps and the final results are shown in Table 3. Comparing S4, S5, and S6 to S1, better joint network structures lead to lower WERs without requiring more parameters. The prediction network regularisation improved averaged WERs by 0.26%, 0.13% and 0.14% for S0, S4, and S6, although the improvements are not always consistent regarding each individual language. Compared to baseline system S0, our best-performing systems S4 and S6 with the regularisation method achieved 4.2% and 5.1% relative reductions in averaged WER by increasing only 1.15M and 2.63M parameters.

# CONCLUSIONS

By viewing the function of the joint network of RNN-T as to fuse the acoustic and text representations derived from the acoustic encoder and prediction network, we propose in this paper to apply the structures widely used for multimodal representation fusion, including gating and bilinear pooling, to improve the joint network implementation. These structures are modified and combined to fit into RNN-T. A novel prediction network regularisation method is also proposed to make the fusion between acoustic and text representations more balanced. When evaluated using a large-scale multilingual voice search setup, 4.2% and 5.1% relative WER reductions were found by using the bilinear pooling and the combination structure separately along with the regularisation.

