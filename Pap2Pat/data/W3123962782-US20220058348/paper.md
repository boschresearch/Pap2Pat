# Introduction

Calibration refers to how well a classification model's confidence (reflected by its output posterior probability) aligns with its actual accuracy. As deep learning models achieve amazing accuracy in computer vision (He et al., 2015) or natural language processing (NLP) (Liu et al., 2019;Devlin et al., 2018), more research attention has been drawn to the calibration aspect of these models. As shown by Guo et al. (2017), the high accuracy from deep models does not always lead to better calibration. This motivates an important line of works attempting to achieve a better trade-off between accuracy and calibration.

Most existing calibration methods (Guo et al., 2017;Kumar et al., 2019;Zadrozny and Elkan, 2001) generally rescale the posterior distribution predicted from the classifier after training. Such post-processing methods require a held-out development set with a decent number of samples to be ˚Bryan McCann contributed to this work while he was at Salesforce Research. available. To overcome this constraint, Jung et al. (2020) uses a penalty term to encourage better calibration during training.

In another line of work, Grathwohl et al. (2019) shows that one can jointly train an energy-based model (EBM) during the standard training of a neural classifier. Although calibration is not explicitly addressed during EBM training, the calibration of the resulting model is shown to be greatly improved. Some intuitions of the underlying reasons will be given in Section 2.3. However, the training framework proposed by Grathwohl et al. (2019) is designed for image classifiers, and it can not be readily applied to discrete text data.

In this work, we propose a framework that uses noise contrastive estimation (NCE) to jointly train an energy-based model during the finetuning of pretrained text encoders (e.g., BERT (Devlin et al., 2018) or Roberta (Liu et al., 2019)) for NLU tasks. We compare several variants of energy functions that can be defined on top of the encoder. Our experiments show that the resulting models achieve competitive calibration results comparing to strong baselines, with little or no loss in accuracy.

# Framework

## Notations and Background

We focus on the finetuning of pretrained text encoder on NLU tasks. We assume samples from the data distribution P D are in the form of px, yq pairs, where x usually refers to a single or a pair of sentences, and y refers to the corresponding label. The number of classes are denoted by |Y |.

Given input x, we first use a text encoder model (e.g., BERT or Roberta) to encode it and we denote this embedding as encpxq. For the target classification task, a classifier f CLS , which could be a simple linear transform or a multi-layer perception (MLP), will be applied to encpxq. We denote the output logits as f CLS pencpxqq, whose dimension is equal to the number of possible classes |Y |. The y-th logit is denoted by f CLS pencpxqqrys. The posterior distribution P θ py|xq is obtained by applying a softmax operation to the logits, where θ refers to the parameters in the model.

In standard finetuning, the cross-entropy (CE) loss and gradient based optimizers are used to train the classifier:

px,yq"P D p´log P θ py|xqq.

(1)

In the next few sections, we discuss how we define and jointly train an EBM on top of the text encoder.

## Definitions of Energy Function

An energy-based model (LeCun et al., 2006) expresses P θ pxq as:

where Z is the normalization factor, and is usually intractable to compute. We refer to E θ pxq, which returns a scalar value, as the energy function. We now define three variants of energy functions.

Variant scalar: We introduce another linear layer g S whose output is a scalar. And we use it to define the energy function:

Êθ pxq " g S pencpxqq.

(3)

Variant hidden: As pointed out by Grathwohl et al. (2019), there's an EBM "hidden" in every neural classifier with softmax output, and the energy function for x can be derived1 as:

(4) Different from the scalar variant, here the energy function directly uses the logits for prediction (visualized in Figure 1). Hence the impact on the model's classification behavior could be larger.

Variant sharp-hidden:

The hidden variant has a potential weakness that, the correlation between input x and the prediction y is not addressed because the energy is distributed among all the logits. Motivated by this potential issue, we propose the following "sharp" variant:

Êθ pxq " ´max y f CLS pencpxqqrys.

(5)

Note that (5) can be viewed as an approximation to (4), and we find it to work well in practice. Finally, for each variant, we define the energy function to be E θ pxq " Êθ pxq ´log P N pxq, where P N is the noise distribution introduced for NCE. We will motivate this design choice below.

## NCE Training

We use noise contrastive estimation (NCE) (Gutmann and Hyvärinen, 2010;Ma and Collins, 2018) to jointly train the energy model. NCE trains the model to discriminate between data samples and noise samples from a given noise distribution P N . We formulate the NCE loss below:

where K is the ratio of noise samples. Note that Pθ pxq does not need to be normalized by construction, therefore we set it to be Pθ pxq " expp´E θ pxqq. In our experiments, we mostly report results with noise ratio K " 8, while in some cases we find that a small ratio of K " 1 works slightly better. We have also tried with larger ratio such as 16, but the gain is minimal.

If we directly use the formulations of Êθ pxq defined in last section as the energy function, the optimization will be difficult because of the P N pxq terms (which could be of very small value) in the NCE objective. To overcome this issue, we follow Deng et al. (2020) and define E θ pxq " Êθ pxq ´log P N pxq. In this way, the P N pxq terms are canceled, and the objective is simplified to:

In training, we jointly optimize L CE and L NCE with the Adam optimizer (Kingma and Ba, 2014):

Intuitively, joint EBM training makes the model aware of P pxq, instead of only focusing on predicting P py|xq as in standard finetuning. This awareness can potentially help with calibration because the model can be more conservative when it detects the input is out-of-distribution.

## Construction of Noise Distribution

For the choice of noise distribution P N , in our preliminary trials, we finetune the GPT-2 language model (Radford et al., 2019) with samples from the target training set using the standard LM objective. However during NCE training, we find that the energy model can easily discriminate between data samples and noise samples, which makes training ineffective. To alleviate this issue, we adopt an objective similar2 to the masked language model (MLM) loss (Devlin et al., 2018) during the finetuning of the noise model (GPT-2): With a given mask ratio M , we randomly mask part of x, and train the model to complete it:

During noise sample generation, adopting the same mask ratio M , we feed a masked x m to the LM (x is from the training set), and use the generated sample as the noise sample. In this way, the noise distribution is made closer to the data distribution.

In our experiments we set M " 0.4. During generation, we use top-k (Fan et al., 2018) sampling with k " 20. More details are provided in Appendix B.

# Experiments

Setting We consider finetuning the Roberta-base model3 , on eight GLUE tasks (Wang et al., 2018).

We do not include results on STS-B because it is a regression task. For baseline or NCE training, we follow the recommended hyper-parameters (learning rate, batch size, etc.) for Roberta (Liu et al., 2019). Since NCE training requires more computation (because of the noise ratio), we have tried finetuning the baseline with more steps, but we find that gives worse ECE and very little or no improvement on accuracy. We compare EBM training with three strong baselines for calibration: posterior calibrated training (PosCal) (Jung et al., 2020), temperature scaling (T-Scal) (Guo et al., 2017), and scaling-binning calibrator (Scal-bin) (Kumar et al., 2019). For PosCal and Scal-bin, we use the published code.

Scal-bin and T-Scal require a development set for parameter learning and a test set for evaluation, but for each GLUE task we only have one labeled development set available. Therefore, in this work we treat half of the standard development set as test set, and keep the other half as development set.

# Results

In Table 1 and Table 2 we compare testset accuracy4 and ECE for different methods on the GLUE tasks. For fair comparison between Scalbin / T-Scal and EBM training (which does not use the development set), we apply them to the whole training set. We also report their performance when applied to the development set for reference.

In most tasks, all three EBM variants get substantial improvement in ECE with little or no loss in accuracy comparing to the (strong) baseline methods. Moreover, the performance of EBM training is comparable to Scal-bin / T-Scal applied to the development set, while their performance degrades when the development set is not available. Among the three variants, on average, the sharp-hidden variant achieves the best accuracy, while the hidden variant achieves best calibration. We visualize the calibration error in Figure 2.       In Figure 3, we plot how test-set ECE changes during training. It is shown as the training reaches the high-accuracy area, the calibration for baseline model becomes worse, while EBM training is able to reach a better trade-off between accuracy and calibration.

How does the model get better calibration? In Figure 4, we compute and plot the energy value Êθ pxq versus the entropy of the posterior distribution HpP θ p¨|xqq " ř |Y | y"1 ´Pθ py|xq log P θ py|xq, for samples in the SST-2 test set. It is shown that models trained with the hidden and sharphidden variants tend to assign more conservative predictions (reflected by higher entropy) for higherenergy (less likely) samples. We suspect this is due to the strong coupling between the energy function and the classification logits. We provide concrete examples in Table 3. However, we need to mention that we do not observe this interesting trend (Figure 4) in all datasets (e.g., QNLI).

# Related Works

Finally, we review applications of NCE or energybased models in the NLP literature. Due to its selfnormalizing property, NCE training has been used for faster inference (Mnih and Teh, 2012;Chen et al., 2015;Labeau and Allauzen, 2018) of auto-regressive language models. It has also been used in an attempt to train a sentence-level bi-directional LM (He et al., 2016).

More closely related to our work, Deng et al. (2020) adopts NCE to train an EBM defined on top of a text encoder (the scalar variant), and uses it to improve language generation. EBM has also been recently used in non-autoregressive machine translation (Tu et al., 2020).

# Conclusion

In this work, we explore joint EBM training during the finetuning of pretrained text encoders with noise contrastive estimation. We find that joint EBM training can greatly improve the calibration of NLU models, with little or no loss on accuracy.

Text: Q: What city north of New York was settled by Huguenots? A: Huguenot immigrants did not disperse or settle in different parts of the country, but rather, formed three societies or congregations; one in the city of New York, another 21 miles north of New York in a town which they named New Rochelle, and a third further upstate in New Paltz. Label: 1 Êθ pxq: -8.48 Baseline: (.997, .003) Ñ EBM: (.995, .005) Text: Q: What is the source of oxygen production through electrocatalytic means? A: A similar method is the electrocatalytic O2 evolution from oxides and oxoacids. Label: 1 Êθ pxq: 4.22 Baseline: (.252, .748) Ñ EBM: (.472, .527) Table 5: The change of the model's confidence (posterior distribution) for low and high-energy data samples in the test set of QNLI. The EBM variant shown is sharp-hidden. 

# Appendices

A Derivation of the hidden Variant Remember from Section 2.1, the posterior distribution is obtained from a softmax operation on the logits, in other words: P θ py|xq9 exppf CLS pencpxqqrysq.

(10)

Without changing any parameters, one can reuse the logits to define an energy based model of the joint distribution of data point x and labels y via:

where Zpθq is the normalizing factor. Note that Equation 11 is consistent with Equation 10 in the sense that Equation 10 is a direct consequence of Equation 11. Now by marginalizing out y, we get:

which is equivalent to

where E θ pxq " ´LogSumExp y pf CLS pencpxqqrysq.

(14) For more intuition behind this derivation we refer readers to Grathwohl et al. (2019).

# B Details About the Noise Distribution

We show some examples of generated noise samples and the masking in Table 4. Note that the masks could be applied to a consecutive span of words (Masking is applied to each token independently with probability M ).

Input: absolutely and completely <M> (ridiculous) Gen: absolutely and completely hilarious Input: <M> (as a) young <M> (woman) of great charm, <M> (generosity) and diplomacy Gen: of a young man with a great charm, wit and diplomacy Table 4: Example of generated noise samples on SST-2. The original words that are masked are also shown.

Another possible way to get noise samples is that we can sample from BERT or Roberta with masked input. However, due to the nature of masked language modeling and the architecture of BERT / Roberta, the sampled tokens will be independent of each other, which could result in unnatural noise samples. That is why we choose to utilize an autoregressive LM (e.g., GPT-2).

# C Definition of ECE

Given an input sample x, for each label y, we say that the model predicts that x belongs to label y with confidence P θ py|xq. Assuming the test-set contains n samples, we will have n ˆ|Y | predictions.

ECE first partitions all predictions into B equally-spaced bins by its confidence. Following Jung et al. (2020); Grathwohl et al. (2019), we set B " 20, which means the width of each bin is 0.05. For example, the first bin contains all predictions that have confidence in the range of r0, 0.05q. Then for each bin ECE computes how the average of confidence is different from its actual accuracy:

where n is the number of samples in the test set, and accpB yb q is simply the ratio of samples (x) whose true label is indeed y in B yb .

# D Auxiliary Results and Examples

Examples of the model's confidence for low and high-energy data samples in QNLI are shown in Table 5. The histogram of energy values Êθ pxq for samples in the test set of QNLI and SST-2 are shown in Figure 5.

In Figure 6, we provide an enlarged version of Figure 2.

