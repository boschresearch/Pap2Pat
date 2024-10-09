# | INTRODUCTION

Good mental models of co-workers are one of the important factors for successful collaboration amongst humans. [1][2][3] Similarly, for human-machine collaboration, having a good mental model can help users calibrate their expectations on machines' robustness to establish trust of machine decisions. 4 To improve users' mental models of machines, there has been a recent focus on generating "explanations" that shed light on machines' inner workings. 5 In the context of Visual Question Answering (VQA), visualizing an attention map over an image is a popular form of explanation that highlights relevant regions used by the system for answering the question. [6][7][8][9] For example, as shown in Figure 1, to explain the answer "pickup" produced by a VQA system to the question "What kind of truck is this?", an attention map is generated to highlight the vehicle region.

Users' ability to understand a VQA model's performance while using such explanations is usually tested by asking users to predict model correctness while viewing the explanations along with the input question and image. 10,11 However, in these studies, attention maps have not been shown to be very helpful [10][11][12][13] in assisting users to predict VQA system correctness.

To analyze how humans interpret explanations and why current attention maps do not help, we first observe that users generally think a VQA model will produce a correct answer when the attention maps point to the relevant evidence in the image (measured using human attention as described in Section 3 and illustrated in Figure 3). However, as shown in Figure 1, we frequently observe that attention maps point to relevant regions (the truck) even when VQA answers incorrectly ("pickup" instead of "dump"). This is misleading to a user who would intuitively guess that the system will be correct because it looked at the right locations.

To clarify cases where an incorrect answer is produced in spite of attention pointing to the relevant regions, we consider an additional mode of explanation to highlight image areas that may be processed incorrectly-we refer to this as an Error Map. Taking Figure 1 for example, the Error Map points to the relevant vehicle region indicating that the vehicle may not be processed correctly (maybe because of low illumination, complexity of the entity, similarity to confusing entities, etc.). We generate error maps by training a Justifying module to learn model correctness and then using GradCAM 14 to highlight visual evidence that contribute to a prediction of model error.

In order to measure the potential of our explanations to help users predict model correctness, we introduce a proxy helpfulness metric by simulating the way humans interpret them. The metric is based on (1) judging whether the explanation highlights information the human thinks is relevant and (2) using the relevance as an indicator to decide if the system can produce the correct answer or not. Attention maps that point to relevant regions for correct answers would be helpful according to such a metric. We also outline a few ways to optimize the visualization of attention maps to maximize these helpfulness characteristics.

Finally, we demonstrate that our new error maps, combined with attention maps, can improve users' ability to predict model performance compared to using baseline attention maps or using no explanations.

In summary, our major contributions include: (1) We introduce an automated proxy metric to evaluate the transparency of attention and error maps. Although user studies are still the gold standard to evaluate attention/error maps, our proxy metric can help reduce the need for multiple expensive and laborious user studies during development. (2)  We propose a novel mode of explanation, Error Maps, that infers the regions that might induce error in the output. We demonstrate the effectiveness of error maps, combined with attention maps, in improving helpfulness of explanations from the perspective of assisting users to predict model correctness. (3) We employ our metrics to optimize the visualization of attention maps from multiple heads of transformers, 15 which otherwise is done via manual inspection in literature. (4) We conduct user studies to verify the effectiveness of our new attention and error maps and show a 30% improvement in user accuracy for predicting model performance when using helpful attention and error maps.

In the sections below, we first describe our VQA model and how attention maps are commonly generated in literature. We then describe how users interpret these attention maps, the problem with current attention maps, how error maps can help improve helpfulness. By simulating user interpretation, we describe our proxy metric for evaluating helpfulness of these attention/error maps. We then describe how we generate error maps and their evaluation.

# | VQA-NET

We first describe our AI system of choice-a VQA model, which we use to study what makes explanations helpful to make better explanations. We build a transformer-based 15 VQA system that answers questions about images.

As shown in Figure 2, our VQA-Net takes an image, I and a question, Q as input and outputs a probability distribution over 3129 answer choices. The image I is encoded into a 7 Â 7 Â 2048 feature map using a ResNet152 16 and further encoded into a 49 Â 512 input feature matrix, H m . We also extract 36 object-based features from the image using a Region Proposal Network, 17 which is encoded into a 36 Â 512 object feature array, H o . Finally, the question is encoded into a 30 Â 512 feature array, H q with a max word length of 30. * We employ transformer-based attention layers (referred to as AT-BERT) that jointly take in the image and question features. The input to the AT-BERT layers are concatenated image and question features (H m , H o , and H q ). Hence, the input dimension to the AT-BERT layers consists of 115 (30 þ 36 þ 49) input tokens of dimension 512 each. Our AT-BERT has four layers with 12 heads each. In each head and layer of AT-BERT, 115 input tokens generate an attention over all other 115 input tokens. Hence, a AT-BERT module with l layers and h heads produces weights, W , of dimension l Â h Â d Â d attention weights. d is the number of input tokens, which is 115 in our case. Finally, the VQA-Net predicts a softmax probability distribution over 3129 answer choices (ie, the top VQA2.0 18 answers) from the attention weighted feature values. Our VQA-Net is trained on the VQA 2.0 dataset. 19 

## | Attention map generation

Following common practice in literature, 20 we display attention by choosing the layers and heads according to a visual inspection on a held-out val-train set. Specifically, the attention is selected by averaging the attention weights on image features by all input tokens in all heads of the last layer of AT-BERT. As we will see in the section below, this sort of attention map visualization does not help users to understand model correctness.

# | HUMAN INTERPRETATION OF EXPLANATIONS

Our goal is to improve human's understanding of the model when seeing explanations such as attention maps as described in the previous section. In order to test users' understanding of the model, we conduct a user study to see how well users can predict the performance of the network when seeing these attention maps. Given an Image-Question (IQ) pair and an attention map, users needed to judge if a VQA model can produce the correct answer or not. We compare this to a group of users seeing no explanations (only image and question) while trying to predict model correctness. We provided a bonus incentive that was scaled to their accuracy in predicting the VQA performance.

## | Users get mislead by current attention maps

We observe that the users' accuracy in predicting correctness does not improve over not seeing any attention maps. In fact, we see a slight decrease (57.18% without explanations, 56.87% when seeing attention maps). This suggests that the guessing accuracy in either case (with or without attention maps) is close to random guessing (50%). To understand why we see no improvement in correctness prediction accuracy, we first analyze how humans interpret these explanations and the fault with the current visualization of the attention maps. We sample subsets of IQ pairs from our user-study set and plot the average relevance of attention in those sets to the percentage of cases users think the model will be correct at to compute Figure 3. We see that users predict the model will be correct more on average when attention maps point to "relevant" areas of the image. Our definition of "Relevance" makes use of annotated human attentions for IQ pairs from the VQA 18 dataset collected. 21 This dataset of attention maps show where humans looked to answer VQA questions. Using these human attention maps, we define the Relevance REL A of an explanation A as the Spearman rank correlation ϕ Á ð Þ of the explanation with the human attention A h for a given IQ pair † :

We choose a rank correlation over the commonly used Pearson's correlation because we want to measure whether the directions of change of attention values are similar to that of the human attention values rather than the absolute

Users believe a model will be correct when the attention points to relevant areas of the image magnitudes. Absolute magnitudes depend on the temperature of the attention distribution, which is irrelevant to the similarity we intend to measure, yet can still change the Pearson correlation significantly.

Using the fact that users associate relevance with correctness as seen in Figure 3, we can assume that users find it intuitive to understand model behavior when attention maps point to relevant regions when the system is correct and vice versa. Figure 4A illustrates this point-it is intuitive to understand machine's correctness for the upper left quadrant (the attention is relevant and the machine is correct) and for the bottom-right quadrant (the attention is irrelevant and the machine is incorrect). However, if the attention is relevant and the answer is incorrect or vice versa (quadrants 2 and 3), it is unclear why the machine is correct/incorrect.

## | Attention Maps seem to be relevant even for incorrect cases

Unfortunately, with current attention map visualizations, we observe that the attention maps often point to relevant image regions even when the model produces an incorrect answer (the counterintuitive case seen in Figure 4A, quadrant 3). If we compute the average REL A for current attention maps for correct answer cases and incorrect answer cases, we see they are 0.32 and 0.31, respectively. This indicates that there is very little visual difference between the correct and incorrect cases. Hence, we need another mode of explanation that explains why the model was incorrect despite attention pointing to similarly relevant areas as correct cases.

## | How Error Maps can help

To clarify cases where the model produces an incorrect answer even when the attention is relevant, we introduce a novel method of explanation-Error Maps, that indicate whether the attended region might be processed correctly or not. If users indeed use the relevance of the attention as a signal for when the model is correct, we can assume that users would similarly use the relevance of the error map to judge if the model will answer incorrectly or not. If an error map points to relevant areas of the image or to the attended regions, a user would assume that those areas may not be processed correctly. As illustrated in Figure 4B, it is easy to understand why a machine failed when the error map points to the relevant region needed to answer the question (bottom-left quadrant) and why a machine succeeded if it points away from the relevant regions (upper-right quadrant).

# | EVALUATING ATTENTION/ERROR MAPS-A PROXY HELPFULNESS MEASURE

Using our knowledge that humans judge model correctness based on how well the explanations point to relevant areas, we design a proxy helpfulness metric based on relevance to evaluate the potential of an attention map to help users to understand machine correctness. We can use this metric to evaluate explanations quickly during development without having to conduct repeated user studies. Note that, in this work, we focus on helpfulness of explanations rather than faithfulness of explanations to the model's inner workings.

## | Helpfulness of Attention Maps

Our helpfulness metric for Attention Maps is higher if their relevance is higher for cases where the VQA model produces correct answers than it is for cases where the VQA model produces incorrect answers. The higher the difference, the better a user can visually tell apart when a model would be incorrect based on the attention relevance. As such, it is defined on a set S of IQ pairs where sometimes the model is wrong and sometimes the model is right.

We conduct a z-test ‡ for comparing the set of correct answer Relevances to the same for incorrect answers. Higher the t-statistic of the z-test, the higher the significance of the difference and hence, the more the helpfulness. Let REL A c be the set of correct answers relevances and REL A w for wrong answers, we compute

## | This helpfulness metric indeed correlates to user accuracy on the task

As illustrated in Figure 5, we note that there is a strong positive correlation between our HELP A Z score and actual users' accuracy in predicting model correctness. To compute the graph in Figure 5, we sample subsets of our user-study set of varying user accuracies and compute the helpfulness HELP Z on those sets. We then plot the average users' accuracy in predicting model performance for these binned HELP Z values.

## | Helpfulness of Error Maps

Using the same intuition as for attention maps, we can assume that users would also use a relevance-based criteria to judge error maps. However, since error maps point to error-contributing areas, the helpfulness metric should be higher if their relevance is lower for cases where the VQA model produces a correct answers than it is for cases where the VQA model produces incorrect answers.

To account for such an inverted behavior, we simply add a negative sign to indicate that a negative correlation is more helpful in the correlation based helpfulness:

With these definitions, a higher score in any HELP metric always means that the explanation is more helpful.

## | Helpfulness of Joint Error and Attention Maps

Up to this point, our helpfulness scores rely on human attention maps being available to determine the relevance of an explanation. We also propose an automatic helpfulness metric that does not require human annotated attention when

Users' accuracy in predicting model correctness gets better on subsets that have higher helpfulness scores as evaluated by our automated metric both attention and error maps are shown together, by computing the relevance (Spearman correlation) between the Error Map and Attention Map REL EA . As shown in Figure 4C, we hypothesize that a joint error and attention map explanation is helpful if the relevance of the error map to the attention map is higher for cases where the VQA model produces wrong answers than for cases where the VQA model produces correct answers. Intuitively, this means that the explanation is helpful when the error-prone regions point to the attention regions for cases when the VQA produces an incorrect answer, and vice versa. Consequently, we can helpfulness (HELP EA Z ):

# | EXPLANATION GENERATION

In this section, we outline how we generate our error maps to improve helpfulness. We also outline a few ways we optimize our attention map visualization to maximize the proxy helpfulness characteristics.

## | Error Map generation

As shown in the right side of Figure 6, we augment our VQA model by a Justifying Module that learns to predict whether the VQA model will fail or not. The Justifying Module is conditioned on the input image features H m , word2vec 22 question features, § AT-BERT weights W , and the model's answer logits. We encode the image using a convolution layer and a fully connected layer into a 96-dim vector. The question features, AT-BERT weights and answer logits are each encoded to 96 dimension hidden vectors using two fully connected layers (96 neurons each). We concatenate the four 96-dim vectors to form a latent vector h j that describes the context needed to predict the correctness.

We predict the VQA-Net's performance from the latent embedding h j . We use a fully connected layer on h j followed by a sigmoid activation to output a binary probability for failure (output is 1 when VQA-System fails). Next, we use GradCAM, 14 which uses gradients to highlight input regions that are important for a failure output. Specifically, we apply it to the logit of the failure predictor output to highlight regions in the image that contribute to the Justifying Module predicting Failure. We use the gradient with respect to the image features H m to compute the Error Map. Note that this error map geenration requires no extra labels other than the VQA dataset labels used to train the VQA model.

## | Finding helpful Attention Maps

To produce a 2D attention map from AT-BERT layers, we previously described a hand-crafted way to generate attention maps in Section 2. Here, we outline a few ways to optimize the visualization by utilizing our HELP metrics.

F I G U R E 6 We train a Justifying Module that learns to predict VQA System's performance. We compute the visual evidence for VQA Failure from the Justifying Module that highlights the error-contributing areas in the image for the given question (referred to as ErrMap).

In the example shown, the question is "What kind of truck is this?", the ErrMap regions point to the truck, indicating that it might confuse the system. The VQA understandably answers incorrectly. VQA, Visual Question Answering

### | Most helpful AT-BERT attention (BestBERT)

We first extract heat maps from the attention weights W for each layer and head. For layer l and head h the corresponding attention map over the 7 Â 7 ¼ 49 image features is A l,h ¼ 1 115 P i W l,h,i,:49 . We compute the HELP A Z scores of attentions from each AT-BERT layer and head, A l,h on a held-out val split. We choose the A l,h with the highest HELP A Z (referred to as BestBERT). For completeness, we also generate attention by choosing the best head (and average the attention values over the layers for that head), referred to as BestBERT-H. Similarly, we also choose the best layer (and average attention over the heads), referred to as BestBERT-L.

### | Justified attention generation (J-Att)

We also learn to predict human annotated attention 21 from the Justifying Module's embedding, h j , by tacking on another head to the module in addition to the failure prediction. This is similar to the work on generating justifying statements, 13 but done for attention maps. The embedding h j is fed through a fully connected layer with a 49 dimensional sigmoid output and then reshaped into a 7 Â 7 attention map. The Justifying Attention and Performance Prediction heads are trained simultaneously with a joint loss. The first term of the loss minimizes the mean squared error between the predicted J-Att attention map and the corresponding human attention map. 21 The second term is binary cross entropy for failure prediction.

# | EXPERIMENTAL SETTINGS

We first evaluate our new attention maps and error maps on our automated proxy helpfulness metrics. We then conduct user studies as a gold standard evaluation to verify the findings from our automated metrics and show improved user performance when using our attention + error map explanations. Using this user study, we also test whether our automated helpfulness metrics for attention and error maps actually are indicative of human performance at predicting model correctness. The test split of the Human Attention Dataset 21 is used for both automatic evaluation and user studies. It consists of 3120 IQ pairs. For choosing hyperparameters and checkpoints, we use a held-out val set of 1000 IQ pairs separate from the 3120 test set.

## | Metrics shown

In the tables for automated metric-based evaluation, we show the following metrics as defined in Section 3.

• Relevance ✓/ Relevance Â: The average relevance of the explanation mode for cases when the system is correct (Relevance ✓) or incorrect (Relevance Â). Hence, it is the average value of REL A for attention maps, REL ERR for error maps, and REL EA for joint attention-error map explanations. • HELP Z : Helpfulness of the mode of explanation measured by the z-test approach as described in Section 4.

## | Baselines

We compare our new attention maps to the current standard for generating them-AT-BERT as described in Section 2. To create a baseline error map based on AT-BERT, we use the error map version of helpfulness, producing BertErr by choosing the attention A l,h that maximizes HELP ERR Z over all layers and heads.

## | User studies

Users were divided into four groups-no explanations group (None), a group that saw BaselineBERT attention maps (described in Section 3), a group that saw BestBERT Attention Maps + ErrMap Error Maps, and a group that saw J-Att + ErrMap. Workers in each group were kept separate and five independent workers predicted the performance on each IQ pair in each group to ensure the quality of our user studies. In total, we have 3300 ratings for the "None" group, 3000 for BaselineBERT, 2250 for BestBERT + ErrMap, and 3960 for J-Att + ErrMap.

# | RESULTS AND ANALYSIS

We first establish the performance of the proposed explanations according to our automated metrics, showing that our attention maps (eg, J-Att, BestBERT) and error map (ErrMap) score higher for helpfulness than baselines. We then conduct user studies to show that explanations with higher helpfulness scores indeed improve users' ability to predict model performance. Below, we describe our key takeaways.

## | Automatic evaluation of explanations

### | Our Error Map has high Helpfulness

Helpfulness scores for attention and error maps are listed in Table 1. Our error map, ErrMap (row g), has the highest HELP z score when compared to all attention maps (rows a to e) and baseline error map (row f). This is reflected in the difference in relevance for system correct vs wrong cases, which is the highest in ErrMap.

7.1.2 | Our new attention maps are also more helpful than baselines, with BestBERT being the most helpful Our relevance and helpfulness metrics for attention maps are shown in Table 1. The proposed attention maps, J-Att (row d), BestBERT (row e), BestBERTHead (row b), and BestBERTLayer (row c) all show higher Helpfulness compared to the baseline (row b). This is reflected in the relevance values, where a larger gap between correct and incorrect relevance leads to higher Helpfulness. BestBERT has the highest difference between the correct and wrong cases' relevance, and the highest Helpfulness.

### | Justifying Attention has high relevance, but relatively low helpfulness

BestBERT outperforms J-Att, which is supervisedly trained to be human-like. This shows that when we train attentions to be human-like, they seem more relevant (points to areas a human would point to for the question), but they may not be helpful for understanding model performance because they are more likely to be relevant even when the model is incorrect.

### | Error Maps used in tandem with attention maps improve helpfulness

In Table 2, we observe that the HELP EA scores of attention maps with our ErrMap are higher the attention map's HELP A scores. This is especially true for high relevance, yet low helpfulness attention maps (column HELP A vs HELP EA , Table 2). For example, BaselineBERT and J-Att which have high relevance even for wrong answers are not very helpful (row a, e, same as Table 1 numbers). When combined with ErrMap the joint helpfulness increases significantly. This is because our ErrMap points to relevant areas when the model errs, and hence, the alignment with an always-relevant attention map can easily indicate failure.

## | User-based evaluation

We first evaluate our proxy helpfulness metrics for error maps and joint error + attention maps and check whether they correlate to actual human accuracy on the task. Similar to how we tested whether our attention helpfulness metric in Figure 5, we plot the average user accuracy for sets of IQ pairs with varying HELP ERR Z and HELP EA Z values in Figure 7.

### | Our automated

Helpfulness metrics for error maps and joint error + attention maps correlate with users' accuracy to predict model performance As visualized in Figure 7A, we see a strong positive correlation (Pearson correlation > 0:9) with HELP Z scores for attention and error maps to the user prediction accuracy when using those explanations. The red line shows the attentiononly HELP A Z , the blue line shows the HELP ERR Z , and the green line shows the HELP EA Z .

### | Our explanations improve user prediction accuracy

Table 3 shows the users' overall prediction accuracy (AVG), accuracy for cases with the VQA system producing correct answers (✓), and accuracy for cases with the VQA system producing wrong answers (Â). We observe an increase in overall accuracy using ErrMap along with BestBERT (row c) or J-Att (row d) explanations than when using no explanations (row a) or when using Baseline BERT explanations (row b). Note that the HELP score on the set used in the user study is lower than that on overall val data. Hence, we also mark the user accuracy corresponding to the set that has the helpfulness scores closest to our overall test data using dotted lines for baselineBERT (attention-only) and our best performing mode, J-Att + ErrMap (joint attention-error). We note a 30% improvement in user accuracy (Figure 7A).

### | Our explanations help especially in predicting failure

We note an increase of 11% (Table 3 comparing rows a and c in column Â) in user accuracy to predict failure of the VQA system. 

### | Gameability of the automated metric

We discuss a few contrived explanations that may not reflect the model's logic for processing the QI pair, but can score high on our metric.

• We generate a centered gaussian attention for all images. We note that this has reasonably high helpfulness (HELP A Z ¼ 2:35). However, this is indeed a helpful explanation about VQA behavior since a high HELP A Z indicates that VQA models tend to answer correctly when the required objects are in the centered attention region.

• As a strong upperbound, we generate centered attentions when our Justifying Module predicts the system will be correct and randomized attention otherwise. Since the Justifying module is reasonably accurate at predicting VQA performance (70% accurate), attention is relevant for correct answers, and random (low relevance) for incorrect answers. Hence, this attention has high helpfulness (HELP A Z ¼ 14:51) since it gives a clear visual indicator of VQA correctness (ie, the ground truth for the user prediction task).

Note that these explanations are gamed because they are not faithful to the internal workings of the model. However, the gamed explanations can indeed provide some helpful insights to users by revealing certain biases.  In Figure 7B, we plot the user-study results with respect to the HELP A Z of attention maps along the x-axis and the HELP ERR Z of error maps along the y-axis. The color of the dots indicate the user prediction accuracy (blue is lower and red is higher). We also show the color corresponding to the accuracy for users seeing no explanations for comparison. While it is expected that the user accuracy is higher when both attention and error maps are more helpful, we note that even having either one as helpful can have reasonably high user accuracy as highlighted by the off-diagonal circles.

# | RELATED WORKS

Historically, explainable AI (XAI) spanned from medical systems 23 to using AI for educational purposes. 24,25 There has been recent thrust in developing XAI systems 5,26 for deep networks and a major goal has been to improve users' mental model of systems for better human-AI collaboration [10][11][12][13]27 or discover biases in models. 28 However, most of these works show no significant improvement of users' accuracy to predict performance with attention maps or show somewhat deleterious effects. 29 In this paper, we argue that to design helpful explanations, we need to have a modeling of users' mental model of AI (perception of AI output). We use that to develop helpful attention and error maps to improve users' ability to predict the model performance.

There have also been works on modeling AI to understand a human's mental model-their actions, motivations or mental states, [30][31][32] human interactions, 33 or anticipating their beliefs. 34 Systems have also been trained to learn how to behave in society 35 for better human-AI collaboration. 36 While they mostly focus on how to model human behavior or interactions, we focus on modeling how humans interpret system outputs to aid their mental model of the AI system.

We use VQA 18 as our choice of AI system. Most effective approaches use attention to weigh image and text features. 9,[37][38][39][40] Recently, transformer-based 15 attention is used. 20,[41][42][43] However, most of these works do not specify how to effectively visualize the high-dimensional transformer attentions. We utilize our automated helpfulness metrics to compute effective ways of displaying attention. There are also works on improving saliency-based explanations by making them more faithful, [44][45][46] using model introspection, 45 grounding to evidence, 47 or making them human-like. 48 However, we focus on how to design explanations to not just be relevant, but also be helpful to human users.

To improve helpfulness, we also introduce a error maps for pointing to error-prone regions for VQA. Predicting failures have also been proposed earlier on other domains for better human understanding [49][50][51] and to improve models. 52 This supports our motivation for introducing error maps in tandem with attention explanations to improve users' ability to predict model performance for VQA.

# | CONCLUSIONS

In this paper, we proposed Error Maps in VQA as a novel explanation method that improve helpfulness over just showing attention maps. We also revealed characteristics of heatmap-style explanations that make them helpful to users and designed an automated proxy helpfulness metric based on it. We anticipate that our automated metrics can aid rapid development of heatmap explanations without having to conduct repeated user studies, and that our proposed Error Map explanations can be applied to other AI domains to improve users' mental model of those systems for better human-AI collaboration.

# ACKNOWLEDGMENTS

The authors would like to thank Anirban Roy, Briland Hitaj, and Karan Sikka for their comments and feedback. This research was developed with funding from DARPA under the Explainable AI (XAI) program. The views, opinions and/or findings expressed are those of the authors' and should not be interpreted as representing the official views or policies of the Department of Defense or the U.S. Government.

# DATA AVAILABILITY STATEMENT

The data for the results and experiments will be publicly available at https://arijitray1993.github.io/helpfulness_ evaluation/.

# CONFLICT OF INTERESTS

The authors declare no conflict of interests.

