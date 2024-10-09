# Introduction

Anomaly detection has numerous real-world applications, including identification of manufacturing defects, network security threats, and financial fraud (Chalapathy & Chawla, 2019;Ahmed et al., 2016;Vanerio & Casas, 2017). Anomaly detection can be considered in different settings. One is the fully-supervised setting, where the labels for all samples are available, for both normal and anomalous samples (Chawla et al., 2002;Estabrooks et al., 2004;Hwang et al., 2011;Barua et al., 2012). This setting is typically addressed with specialized approaches for data imbalance, e.g. weighted loss functions or resampling methods. An important special case of this fully-supervised setting is when only labeled normal samples exist (Schölkopf et (Schölkopf et al., 1999) or auto-encoder (Ruff et al., 2018)) and Isolation Forest (Liu et al., 2008) are popular approaches. Despite being widely-studied, the challenge towards the real-world use for these supervised settings is their tedious labeling requirement. At the other extreme, there is the fully unsupervised anomaly detection setting where no labeled data is available (Breunig et al., 2000;Liu et al., 2008;Zong et al., 2018;Bergman & Hoshen, 2019;Yoon et al., 2022). While the labeling costs can be entirely eliminated for this setting, the performance degradation is often significant compared to the supervised setting (Bergman & Hoshen, 2019;Zong et al., 2018), limiting its applicability for deployment.

To achieve the best of both worlds, we focus on the semi-supervised anomaly detection setting, aiming to achieve high performance with a limited labeling budget. In previous works on semi-supervised anomaly detection (Zhang & Zuo, 2008;Bekker & Davis, 2020;Blanchard et al., 2010;Akcay et al., 2018;Görnitz et al., 2013;Ruff et al., 2020), some focus on the positive-unlabeled setting (Zhang & Zuo, 2008;Bekker & Davis, 2020), and others utilize one-class classifiers or adversarial training on semi-supervised learning (Görnitz et al., 2013;Akcay et al., 2018). Ruff et al. (2020) treats all unlabeled data as normal samples to construct an anomaly detector in semi-supervised settings. In addition, any semi-supervised learning method (even when they aren't developed for anomaly detection) can be adapted to the semi-supervised anomaly detection setting (Sohn et al., 2020;Chen et al., 2020a;Grill et al., 2020).

Most semi-supervised learning methods assume that the labeled and unlabeled data come from the same distributions (Sohn et al., 2020;Chen et al., 2020a;Grill et al., 2020). In other words, the subsets of the data are labeled such that sampling from the unlabeled data is randomly uniform. However, in practice, this assumption often does not hold: distribution mismatch commonly occur, with labeled and unlabeled data coming from different distributions. Some works (Kim et al., 2020) tackle this in a limited setting where only the label distributions are different (e.g., the anomalous ratio is 10% for training but 50% for testing), however, there are other more general real-world scenarios, as exemplified in Fig. 1. First, positive and unlabeled (PU) or negative and unlabeled (NU) settings are common, where the distributions between labeled (either positive or negative) and unlabeled (both positive and negative) samples are different (see Fig. 1(Left)) (Zhang & Zuo, 2008;Bekker & Davis, 2020). Second, additional unlabeled data can be gathered after labeling, causing distribution shift. For example, manufacturing processes may keep evolving and thus, the corresponding defects can change and the defect types at labeling differ from the defect types in unlabeled data (see Fig. 1(Middle)). In addition, for financial fraud detection and anti-money laundering applications, new anomalies can appear after the data labeling process, as the criminals adapt themselves. Lastly, human labelers are more confident on easy samples; thus, easy samples are more likely to be included in the labeled data and difficult samples are more likely to be included in the unlabeled data (see Fig. 1(Right)). For example, with some crowd-sourcing-based labeling tools, only the samples with some consensus on the labels (as a measure of confidence) are included in the labeled set.

As we experimentally demonstrate (in Sec. 5), standard semi-supervised learning methods (Sohn et al., 2020;Chen et al., 2020a;Grill et al., 2020) are sub-optimal for anomaly detection under distribution mismatch, because they are developed with the assumption that labeled and unlabeled data come from the same distribution. Generated pseudo-labels are highly dependent on a small set of labeled data; thus, the trained semi-supervised models would be biased on the labeled data distribution. Transfer learning methods or the frameworks for distribution shifts may constitute alternatives (Pan & Yang, 2009; Yu et al., 2020;Raina et al., 2007) by treating source/target data as labeled/unlabeled data. However, these have not been effective with a small number of source (labeled) samples (as shown in Sec. 5).

In this paper, we propose a novel semi-supervised anomaly detection framework SPADE, that yields strong and robust performance even under distribution mismatch. Contributions of this paper can be summarized as below:

• Motivated by the common real-world scenarios, we tackle the distribution mismatch problem for semisupervised anomaly detection which is critical but under-explored. • We propose a novel semi-supervised learning framework, SPADE. Carefully-designed components of SPADE enable robust semi-supervised learning. As such, SPADE introduces a pseudo-labeling mechanism using an ensemble of OCCs and a judicious way of combining supervised and self-supervised learning.  • SPADE reduces the dependence on the labeled data as the predictors are trained with a small number of labeled and pseudo-labeled samples. • We propose a novel approach using a partial matching method (Du Plessis & Sugiyama, 2014) to pick hyperparameters without a validation set. This innovation is critical as conventional hyperparameter selection relies on validation set, which is often unavailable in real world with limited labeled data. • We show state-of-the-art semi-supervised anomaly detection performance of SPADE in multiple settings that represent common real-world scenarios. AUC improvements of SPADE can be up to 10.6% on tabular data and 3.6% on image data. • We focus on an important real-world machine learning challenge: fraud detection with distribution shifts over time due to the adversarial nature of the environment. We show that SPADE consistently outperforms existing methods considered.

# Related Work

Semi-supervised learning. ). The shortcoming of (i) is excluding the possible positive samples from unlabeled data, whereas the shortcoming of (ii) is contamination of unlabeled data that affects model training. While being relevant, these are limited to the special case of PU setting, and sub-optimal when applied to the general semi-supervised settings.

# Problem Formulation

We focus on the general semi-supervised anomaly detection problem with distribution mismatch. Consider the given labeled training data

x l ∼ P l X and x u ∼ P u X are the feature vectors and P l X and P u X are corresponding feature distributions of the labeled and unlabeled data, respectively. For anomaly detection, the labels y ∈ Y are either normal (0) or anomalous (1) and there are far more normal examples than anomaly, i.e., P(y = 0) P(y = 1). Most semi-supervised methods assume that both labeled and unlabeled data come from the same distribution (i.e., P l X = P u X ). In this work, we aren't limited by this assumption and allow the scenario of the distributions between labeled and unlabeled data to be different (i.e., P l X = P u X ). We exemplify such scenarios in Fig. 1. For instance, if new anomaly types are only included in the unlabeled data, P u X would be different from P l X . The labels y are determined by the unknown function f * : X → Y where x l , x u ∈ X . Our main objective is to construct an anomaly detection model f : X → Y that can minimize the test loss L(f (x), y) in the union of P l X and P u X . As a way of motivation, the conventional approaches to tackle this problem along with their limitations are summarized in Table . 1. All these are quantitatively compared with SPADE in Sec. 5. Further details can be found in Appendix A. 

## Desiderata

The core idea of our framework, Semi-supervised Pseudo-labeler Anomaly Detection with Ensembling (SPADE), is based on self-training, following recent advances in semi-supervised learning (Sohn et al., 2020; Chen et al., 2020a). We aim to train a binary classifier for normal and anomalous data by iteratively learning from labeled and pseudo-labeled data. As such, the key component is the pseudo-labeler to assign binary labels to unlabeled data. While it is common to use a trained binary classifier for pseudo-labeling (Lee et al., 2013;Sohn et al., 2020), we argue that it may be sub-optimal for anomaly detection with distribution shift as the decision boundaries of binary classifiers could be highly biased by the small labeled data. As shown in Fig. 2(b,c), this would have a negative impact when labeled and unlabeled data distributions are mismatched. Instead, we decouple the pseudo-labeler from the trained binary classifier and build it with OCCs. While this cannot utilize the labeled positive data like binary classifiers, it would prevent overfitting to the small amount of labeled data, and thus can be more robust to distribution shifts, as shown in Fig. 2(d).

## Building blocks

Fig. 3 illustrates the four components of SPADE framework: (i) (data) encoder, (ii) predictor, (iii) pseudolabeler, and (iv) projection head. First, the encoder: h : X → H maps the input features x into latent representations r = h(x). As the encoder, any neural network architecture can be employed -in our experiments, we use multi-layer perceptron (MLP) for tabular data and convolutional neural networks (CNNs) for image data. The predictor q : H → Y utilizes the learned representation r to output the anomaly scores q(r). The anomaly score is determined by the encoder (h) and predictor (q) as follows: q(h(x)). Pseudo-labeler and projection head help the encoder and predictor training. Pseudo-labeler v : H → {0, 1, -1} determines the pseudo-labels of the unlabeled data x u using an ensemble of OCCs. v(h(x u )) = 1/0/ -1 represents pseudo-anomalous/pseudo-normal/unlabeled. The predictor only utilizes the labeled data and unlabeled data with v(h(x u )) = 1/0 for training. Lastly, projection head g : H → G is the block to help representation learning of the encoder. Any representation learning method can be utilized, such as contrastive learning and pretext task predictions (such as masked autoencoder).

## Pseudo-labeling via consensus

A major novel component of SPADE is the design of pseudo-labeler. The pseudo-labeler (v in Fig. 3) is composed of an ensemble of K OCCs (o  Predictor is a binary classifier. Blue line represents the inference steps.

x. We assign the positive pseudo-labels (i.e. anomalous predictions) to unlabeled data samples if all OCCs agree on them:

Similarly, we assign a negative pseudo-label (i.e., normal) if all OCCs agree on negative pseudo-labels:

Unlabeled data without consensus are annotated as unknown:

## Determining η p , η n using partial matching

In SPADE framework, thresholds η p and η n are critical parameters. One option is considering them as user-defined hyper-parameters and determining them by the hyper-parameter optimization. However, hyperparameter tuning requires extra validation data which should come from labeled training set (same impacts as reducing the number of labeled samples in training data which is critical in semi-supervised setting). Instead, we propose to learn these parameters without sacrificing the labeled data for validation. We propose adapting the partial matching method (Christoffel et al., 2016), which has been developed to estimate the marginal distribution of unlabeled data by matching the distribution to the known one-class (either positive or negative) distribution. The underlying intuition is that normal samples are closer to other normal samples, and anomalous samples are closer to other anomalous samples. In our case, we match the distribution of anomaly scores of the positive labeled data to that of unlabeled data to estimate their marginal distribution and determine η p accordingly. The same is applied to determine η n using negative labeled data. Formulations for η p and η n are given in Eqs. 3 and 4 below:

where D w is the Wasserstein distance between two distributions. That is, we determine the subsets of the unlabeled data for pseudo-labeling whose Wasserstein distance from labeled data is minimum.

In some semi-supervised settings such as PU and NU, only one-class of labeled samples are available. In that case, we employ Otsu's method (Otsu, 1979) to identify the threshold of the class without labeled samples. With Otsu's method, we can determine the threshold that minimizes intra-class anomaly score variances in an unsupervised way. For instance, in PU setting, we set η p using Eq. 3 and η n .

## Loss functions and optimization

We train the anomaly detection model q(h(•)) using three loss functions: (i) binary cross entropy (BCE) on labeled and (ii) BCE on pseudo-labeled data, and (iii) self-supervised loss on the entire data. The self-supervised module g (e.g., decoder for reconstruction loss, MLP projection head for contrastive loss) is jointly trained with an auxiliary self-supervised loss.

Next, we describe the loss formulations. The BCE loss on the labeled data is proposed as:

and the BCE loss on pseudo-labeled data as:

Here, instead of subsampling unlabeled data with known pseudo-labels, we assign a binary weight (1{v u ∈ {0, 1}}) to each unlabeled sample so that the loss contribution from pseudo-labeled data can be controlled based on the model quality.

To improve the quality of the encoder (h), we utilize auxiliary self-supervised losses with various pretext tasks depending on application domain. This may include the reconstruction objective:

or more specific objectives to data type, such as contrastive learning (Chen et al., 2020a) and CutPaste (Li et al., 2021) for image.

Overall, the encoder (h), predictor (q), and the self-supervised module (g) are trained by solving the following optimization problem: h * , g * , q * = arg min h,g,q

where α, β are hyper-parameters (we set both α and β as 1.0 for the experiments). Training loss is used for the convergence criteria -if the training loss is converged (if no improvement is observed in the loss for 5 epochs), we treat that the models are converged as well. Note that the pseudo-labeler also converges during training, often faster. The overall pseudo-code can be found in Alg. 1.

# Experiments

We conduct extensive experiments to highlight the benefits of the proposed method, SPADE, in various practical settings of semi-supervised learning with distribution mismatch. We consider multiple anomaly detection datasets for image and tabular data types. As image data, we use MVTec anomaly detection (Bergmann et al., 2019) and Magnetic tile datasets (Huang et al., 2020). As tabular data, we use Covertype, Thyroid, and Drug datasets (see Appendix for detailed data description). In Sec. 5.4, we further utilize two real-world fraud detection datasets (Kaggle credit and Xente) to evaluate the performance of SPADE.

In all experiments, unless the dataset comes with its own train and test split, we randomly divide the dataset into disjoint train and test data. Then, we further divide the training data into disjoint labeled and unlabeled data. Note that we construct labeled and unlabeled data such that they come from different distributions (more details can be found in the following subsections). We run 5 independent experiments and report average values (standard deviations can be found in Appendix C). We use AUC as the evaluation metric. More experimental details (on model architectures, training settings, and pseudo-labelers) are provided in Appendix B. Computational complexity analyses can be found in Appendix B.7.

# Algorithm 1 Semi-supervised Pseudo-labeler Anomaly Detection with Ensembling (SPADE).

Input: Labeled / unlabeled training data D l / D u Output: Trained encoder (h), predictor (q)

for k=1:K do 4:

Set η p k /η p k using partial matching with D l 1 , D l 0 using Eqs. 3 and 4.

# 6:

end for

# 7:

Build pseudo-labeler v following Eqs. 1 and 2.

# 8:

Return pseudo-labeler v. 9: end function 10: Initialize g, h, q. 11: Set positively / negatively labeled data D l 1 , D l 0 12: while g, h, q not converged do

Update g, h, q using Eq. 5.

# 15: end while

We compare SPADE to baselines from Table 1. Note that not all baselines are applicable to every scenario. More specifically, we use Gaussian Distribution Estimator (GDE) for both OCC (only using the negatively labeled data) and Negative OCC (only excluding the positively labeled data). Note that GDE performs the best in comparison to the alternatives in our experiments (including isolation forests, OC-SVM). We use SRR (Yoon et al., 2022) as the unsupervised OCC baseline and Random Forest as the supervised (only using the labeled data) and negative supervised (treat unlabeled data as negative) baselines. For image data, FixMatch is used instead of VIME as the semi-supervised baseline. We use CutPaste (Li et al., 2021) as the baseline architecture for Negative OCC, Unsupervised OCC, and SPADE for MVTec and Magnetic datasets.

## New types of anomalies

Anomalies can evolve over time in many applications. For fraud detection, criminals might invent new fraudulent approaches to trick the existing systems; or for manufacturing, modified process might yield different defects that have been never met before. Therefore, labeled data can get out-dated and newlygathered unlabeled data can come from different distributions. To mimic such scenarios, we construct datasets with multiple anomaly types. Among multiple anomaly types, we provide subsets of the anomaly types (and normal samples) as the labeled data. It means that other anomaly types only appear in the unlabeled data. Detailed experimental settings can be found in Appendix. B.2.

Tables 2 and3 (left) show that SPADE achieves consistently and significantly better performance in all 3 metrics (overall, given, and missed AUC), demonstrating its generalizability to unseen anomalies. On the other hand, supervised and semi-supervised (VIME and FixMatch) methods remain highly biased towards given anomalies and generalize poorly to new types of anomalies. Compared to the best baseline, SPADE improves overall AUC by 0.106, 0.015, and 0.031 on the three tabular datasets.

Each baseline has its own limitations. Supervised classifiers cannot utilize unlabeled data at all, and negative supervised classifier suffers from contaminated labeled data for training the predictive model. OCC models are suboptimal as they cannot utilize the anomalous label information. Semi-supervised learning baselines suffer from distribution mismatch between labeled and unlabeled data. For domain adaptation baseline, it shows poor performances with a small number of source samples. 

# Datasets

## Labeling based on the 'easiness' of samples

The difficulty for human labeling may differ across different samples -while some samples are easy to label, some samples can be misleadingly difficult to humans because they appear differently from the known cases.

To simulate this scenario, we focus on an experiment where the labeled data only includes easy-to-label samples while hard-to-label samples are included in the unlabeled dataset. To this end, we train logistic regression using the entire training data, and gather the labeled samples where confidence of the trained logistic regression outputs are larger than a certain threshold and the predictions are correct. Details can be found in Appendix. B. Tables 3 (right) and 4 show that SPADE achieves superior or similar anomaly detection performances compared to the best alternative. This constitutes a great potential in reducing human labeling costs by allowing the labelers to skip samples if they would take too long to correctly label. The experimental results with the opposite setting (only labeling the high-risk samples) can also be found in Appendix D.1.

## PU (Positive & Unlabeled) learning

With only positive samples as the labeled data and all other samples being unlabeled, i.e. the positive and unlabeled (PU) settings, the distributions between labeled (only positive samples) and unlabeled (both positive and negative samples) would be different.  Table 5 compares the performances of the proposed method (SPADE) in PU settings on multiple tabular datasets. SPADE generalizes much better and outperforms all other alternatives with significantly better AUC in missed (not given) anomaly types. Note that PU baselines severely suffer from distribution mismatches when new types of anomalies are included in the unlabeled data.

## Time-varying distributions: real-world fraud detection

We evaluate the proposed framework with two real-world fraud detection datasets: (i) Kaggle credit card fraud1 (0.17% anomaly ratio with total 284807 samples), (ii) Xente fraud detection2 (0.20% anomaly ratio with total 95662 samples). For these tasks, anomalies are evolving (i.e., their distributions are changing over time) (Grover et al., 2022). To catch the evolving anomalies, we need to keep labeling for new anomalies and retrain the anomaly detection model. However, labeling is costly and time consuming. Even without additional labeling, SPADE can improve the anomaly detection performance using both labeled data and newly-gathered unlabeled data.

In our experiments, we split the train and test data based on the measurement time. Latest samples are included in the testing data (50%) and early acquired data is included in the training data (50%). We further divide the training data as labeled and unlabeled data. Early acquired data are included in the labeled data (5%-20%), while later acquired data are included in the unlabeled data (80%-95%). We use AUC as the anomaly detection metric. As shown in 

# Discussions

Accuracy of the pseudo-labels. SPADE is based on the proposed pseudo-labeling mechanism. The accuracy of the pseudo-labeler is highly related to the robustness of semi-supervised anomaly detection. We analyze the accuracy (in precision) of the pseudo-labels vs. anomaly score percentiles for both normal and anomalous samples.  Fig. 4 shows that the proposed pseudo-labeler achieves fairly robust pseudo-labeling for normal samples. On the other hand, for anomalous samples, the precision of pseudo-labeling gets high typically when the anomaly scores are higher than 80%, however we observe drop in precision in some cases, which we attribute to imperfect OCC fitting. While this underlines the room for improvement for pseudo-labeling, due to the robustness of partial matching, the impact of imperfect precision on anomaly detection performance is low. Note that our partial matching algorithm catches this threshold fairly accurately to make pseudo-labels robust without any threshold parameter tuning.

Ablation studies. SPADE consists of multiple components and understanding the impact of each component is of high importance. In Table . 7, we demonstrate the performance impacts of 5 different components in SPADE on the Thyroid data with the setting of new anomaly types. All components of the SPADE are observed to contribute to the robust anomaly detection performance considerably. Self-supervised learning component contributes to 0.018 AUC improvements of SPADE framework. In addition, with majority votes instead of unanimous votes for pseudo-labeling, the performance of SPADE is degraded by 0.024 AUC. Additional ablation studies on other datasets can be found in Appendix D.2.

α is a critical hyper-parameter of SPADE determining the importance of pseudo-label loss in comparison to given labeled data. We analyze the impact of this hyper-parameter in Fig. 5. With α = 0, the performance is much worse than α > 0 on Thyroid (0.08 lower AUC) and on Covertype (0.06 lower AUC) datasets. This underlines the impact of utilizing the unlabeled data. In addition, the performances are similar across different α > 0, demonstrating that SPADE isn't sensitive to the hyper-parameter α. Note that, all the experiments in Sec. 5 use α = 1 as the default value. 

# Conclusions

Semi-supervised anomaly detection is a highly-important challenge in practice -in many scenarios, we cannot assume that the distributions of labeled and unlabeled samples are the same. In this paper, we focus on this and demonstrate the underperformance of standard frameworks in this setting. We propose a novel framework, SPADE, which introduces a novel pseudo-labeling mechanism using an ensemble of OCCs and a judicious way of combining supervised and self-supervised learning. In addition, our framework involves a novel approach to pick hyperparameters without a validation set, a crucial component for data-efficient anomaly detection. Overall, we show that SPADE consistently outperforms the alternatives in various scenarios -AUC improvements with SPADE can be up to 10.6% on tabular data and 3.6% on image data. In addition to anomaly detection, future work can extend this semi-supervised framework to multi-class classification or regression with distribution mismatch.

# B Detailed experimental settings B.1 Convert multi-class datasets into anomaly detection datasets

• For Thyroid data3 , there are 3 classes. The class distributions are (1: 2.47%, 2: 5.06%, 3: 92.47%). We treat label 3 as the normal samples and label 1 and 2 as the abnormal samples. We use the pre-defined training and testing dataset division.

• For Drug data 4 , there are 7 classes. The class distributions are (1: 75.27%, 2: 2.02%, 3: 4.56%, 4: 8.28%, 5: 3.29%, 6: 2.12%, 7: 4.46%). We treat label 1 as the normal samples and all the other labels as the abnormal samples. We divide the entire dataset into training (50%) and testing (50%).

• For Covertype data5 , there are 7 classes. The class distributions are (1: 36.55%, 2: 48.75%, 3: 6.14%, 4: 0.47%, 5: 1.64%, 6: 2.94%, 7: 3.50%). We treat label 1 and 2 as the normal samples and all the other labels as the abnormal samples. We divide the entire dataset into training (50%) and testing (50%).

• For MVTec data (Bergmann et al., 2021) 6 , different categories (15 categories) have different number of anomaly types. We set type 0 as the normal samples and all the other types as abnormal samples. Note that we first mix given training and testing data and divide them into training (80%) and testing (20%) to make the same abnormal ratio between training and testing sets.

• For Magnetic Tile dataset (Huang et al., 2020) 7 , there are 6 types of samples: free, blowhole, crack, break, fray, and uneven. We set the free type as the normal, and the other 5 types as anomalies. We mix given training and testing data and divide them into training (80%) and testing (20%) to have the same abnormal ratio between training and testing sets.

# B.2 Detailed experimental settings in Scenario 1: New types of anomalies

On each of the 5 datasets that we used in this paper, there are multiple types of anomalies. In such scenarios, we only provide a subset of anomaly types as the labeled data and the rest of the anomaly types as the unlabeled data. The below explains which types of anomalies are provided as the labeled data for each dataset:

• For Thyroid data, we provide label 1 anomaly type to the labeled data (label 2 anomaly type is only in the unlabeled data). • For Drug data, we provide label 2,3,4 as anomaly types to the labeled data (label 5, 6, 7 anomaly types are only in the unlabeled data). • For Covertype data, we provide label 3, 4, 5 as anomaly types to the labeled data (label 6, 7 anomaly types are only in the unlabeled data). • For MVTec and Magnetic tile datasets, different categories have different number of anomaly types. We provide the odd types as anomaly types to the labeled data. All the even types of anomalies are included in the unlabeled data.

Note that we only provide 5% of the data as labeled data for tabular datasets and 20% for image datasets, for the scenario of new types of anomalies.

# B.3 Detailed experimental settings in Scenario 2: Labeling based on the easiness of samples

To identify the easiness of the samples, we train a logistic regression model using the entire training data, and we gather the labeled samples where confidence of the trained logistic regression model outputs are larger than a certain threshold and the predictions are correct. To balance the labeled data in both normal and abnormal samples, we select top 10% confidences (from trained logistic regression) of each class as the labeled data for tabular datasets (20% confidence for image datasets). The rest of the samples are treated as the unlabeled samples.

# B.4 Detailed experimental settings in Scenario 3: PU learning

The experimental settings in PU settings are the same with scenario 1 (new types of anomaly) except the following points:

• We exclude all the normal samples from the labeled data to make the experiments in PU setting.

• We provide 50% of the given anomaly types as the labeled data. However, the number of labeled data is less than Scenario 1 because we exclude all the normal samples from the labeled data.

# B.5 Details on model architecture and training

For image data, we use ResNet-18 as the base network architecture. For representation learning, we incorporate CutPaste (Li et al., 2021) for MVTec and Magnetic Tile datasets. We follow all the training details in (Li et al., 2021) (including all the hyper-parameters).

For tabular data, we use two-layer perceptron as the base network architecture where the hidden dimensions is the half of the original feature dimensions. Pseudo-labelers consist of 5 Gaussian Distribution Estimator (GDE) based OCCs. For each epoch, we update the ensemble of OCCs for the pseudo-labels and further training the data encoder, projection head, and predictor. We set α = 1 and β = 1 for all the experiments except the ablation studies. We use the training loss as the convergence criteria. More specifically, if the training loss does not improve for 5 epochs, we stop model training.

# B.6 Baselines

We compare SPADE with various baselines in different settings. Below describes the details of the baselines used in this paper:

• Gaussian Distribution Estimator (GDE) for both OCC (only using the negatively labeled data) and Negative OCC (only excluding the positively labeled data) 8 . • Random Forests for the supervised (only using the labeled data) and negative supervised (treat all the unlabeled data as negative) 9 • VIME 10 for the tabular semi-supervised learning baseline and FixMatch 11 for the image semi-supervised learning baseline. • Domain Adversarial Neural Network (DANN) for the domain adaptation baseline 12 .

• Weighted Elkanoto 13 and BaggingPU 14 for PU learning baselines.

• CutPaste for the base architecture of image domain anomaly detection 15 .

# B.7 Computational complexity analyses

All the experiments are done on a single V100 GPU. For tabular datasets, training and inference need at most 1 hour per each experiment (with the largest dataset, Covertype). For image dataset, training and inference need at most 4 hours per each experiment, mostly due to the representation learning with CutPaste. Note that the pseudo-labeler (an ensemble of OCCs) is re-trained per an epoch (not per an iteration) and we use shallow OCCs (GDE) for the ensemble to further reduce the computational complexity.

# C Standard deviations of the experiment results

In this section, we report the standard deviations of the experimental results described in the main manuscript across 5 independent runs. 

# D.1 Labeling high-risk samples

In this subsection, we evaluate the performance of SPADE in PNU settings only with the labeled high-risk samples which is a common practical setting in fraud detection applications (including anti-money laundering). More specifically, the predictive model first estimates the anomaly scores of the unlabeled data. Then, the users manually check the samples only with high anomaly scores, and label them as either positive or negative. Thus, most labeled samples are actually high-risk samples and most unlabeled samples are low-risk samples which make the distribution differences between labeled and unlabeled data.

Similar with easiness scenario, we first train a simple logistic regression model (with the full label) and compute the anomaly scores of the unlabeled data. Then, we only extract the high risk samples (e.g., with top 2% highest anomaly scores). Then, we provide true labels for 50% (selected by uniformly random) of those high risk samples. It means that we have 1% of labeled data (either positive or negative) and 99% of unlabeled data. We exclude original OCC as the baseline because in some cases, there are too small numbers of negatively labeled samples which make OCC hard to converge.

Table 13 shows that SPADE achieves superior or similar anomaly detection performance compared to the best alternative.

# A Details of the conventional solutions A.1 Standard supervised learning

The most straightforward approach is applying the standard supervised learning framework. We can construct the supervised model g sup only with the labeled data D l as follows.

However, in this case, we cannot benefit from the unlabeled data D u which can be beneficial for further boosting the performance with various semi-supervised learning framework. Also, the training data distribution X l is different from the testing distribution X which can negatively impact on the test performance. We may treat all the unlabeled data as normal samples and apply the supervised learning framework (g sup+ ) as follows:

However, in this case, labeled normal samples are contaminated.

# A.2 Standard one-class classifiers (OCCs)

OCCs are one of the most promising methods to tackle the anomaly detection problem. Instead of using incomplete anomaly labels, we can only utilize the labeled normal samples D l 0 = {(x j , y j ) ∈ D l |y j = 0} to construct the OCC (g one ). However, in this case, we need to drop all labeled abnormal samples and unlabeled samples which may include quite critical information. We can include the unlabeled data (D u ) to construct another OCC (g one+ ) such as SRR (Yoon et al., 2022). However, it still cannot utilize the labeled abnormal samples.

# A.3 Semi-supervised learning

With both labeled and unlabeled data, we usually prioritize to apply semi-supervised learning approaches. We can utilize the semi-supervised learning framework to construct the anomaly detection model as follows.

Most semi-supervised learning frameworks assume that the labeled data D l and unlabeled data D u come from the same distribution. However, this assumption does not hold in our problem formulation. Thus, possibly-biased labeled data distribution can negatively affect on the trained semi-supervised model.

# A.4 Detailed comparison with SRR (Yoon et al., 2022)

SPADE has some resemblance with the SRR paper (Yoon et al., 2022). However, there are clear differences between SPADE and SRR. First, the problem setting is different. One of the biggest novelties of SPADE is tackling an important but under-explored problem: semi-supervised learning with distribution mismatch (e.g., common labeling bias). This has not been discussed in SRR which focused on only the fully unsupervised setting. Extension from fully unsupervised to general semi-supervised setting is not straightforward. Second, the approach to utilize the positive and negative samples is not discussed in SRR, which is critical in SPADE.

We should consider how we utilize the normal samples for improving the pseudo-labeler training (please see the ablation studies in Table 6) and how we utilize the labeled samples for determining the thresholds -Line 4 and 5 in Algorithm 1. Third, SPADE can automatically determine the thresholds parameters without true anomaly ratios or validation set by the proposed partial matching. 

