# Introduction

There exists a vast amount of knowledge sources and ontologies in the medical domain. Such information is also growing and changing extremely quickly, making the information difficult for people to read, process and remember. The combination of recent developments in information extraction and the availability of unparalleled medical resources thus offers us the unique opportunity to develop new techniques to help healthcare professionals overcome the cognitive challenges they face in clinical decision making.

Relation extraction plays a key role in information extraction. Using question answering as an example (Wang et al., 2012): in question analysis, the semantic relations between the question focus and each term in the clue can be used to identify the weight of each term so that better search queries can be generated. In candidate answer generation, relations enable the background knowledge base to be used for potential candidate answer generation. In candidate answer scoring, relation-based matching algorithms can go beyond explicit lexical and syntactic information to detect implicit semantic relations shared across the question and passages.

To construct a medical relation extraction system, several challenges have to be addressed:

• The first challenge is how to identify a set of relations that has sufficient coverage in the medical domain. To address this issue, we study a real-world diagnosis related question set and identify a set of relations that has a good coverage of the clinical questions.

• The second challenge is how to efficiently detect relations in a large amount of medical text. The medical corpus underlying our relation extraction system contains 80M sentences (11 gigabytes pure text). To extract relations from a dataset at this scale, the relation detectors have to be fast. In this paper, we speed up relation detectors through parsing adaptation and replacing non-linear classifiers with linear classifiers.

• The third challenge is that the labeled relation examples are often insufficient due to the high labeling cost. When we build a naïve model to detect relations, the model tends to overfit for the labeled data. To address this issue, we develop a manifold model (Belkin et al., 2006) that encourages examples (including both labeled and unlabeled examples) with similar contents to be assigned with similar scores. Our model goes beyond regular regression models in that it applies constraints to those coefficients, such that the topology of the given data manifold will be respected. Computing the optimal weights in a regression model and preserving manifold topology are conflicting objectives, we present a closed-form solution to ideally balance these two goals.

The contributions of this paper on medical relation extraction are three-fold:

• The problem setup is new. There is a "fundamental" difference between our problem setup and the conventional setups, like i2b2 (Uzuner et al., 2011). In i2b2 relation extraction task, entity mentions are manually labeled, and each mention has 1 of 3 concepts: 'treatment', 'problem', and 'test'.

To resemble real-world medical relation extraction challenges where perfect entity mentions do not exist, our new setup requires the entity mentions to be automatically detected. The most well-known tool to detect medical entity mentions is MetaMap (Aronson, 2001), which considers all terms as entities and automatically associates each term with a number of concepts from UMLS CUI dictionary (Lindberg et al., 1993) with more than 2.7 million distinct concepts (compared to 3 in i2b2). The huge amount of entity mentions, concepts and noisy concept assignments provide a tough situation that people have to face in real-world applications.

• From the perspective of relation extraction applications, we identify "super relations"the key relations that can facilitate clinical decision making (Table 1). We also present approaches to collect training data for these relations with a small amount of labeling effort.

• From the perspective of relation extraction methodologies, we present a manifold model for relation extraction utilizing both labeled and unlabeled data. Our approach can also take the label weight into consideration.

The experimental results show that our relation detectors are fast and outperform the state-of-theart approaches on medical relation extraction by a large margin. We also apply our model to build a new medical relation knowledge base as a complement to the existing knowledge bases.

# Background

## Medical Ontologies and Sources

Medical domain has a huge amount of natural language content found in textbooks, encyclopedias, guidelines, electronic medical records, and many other sources. It is also growing at an extremely high speed. Substantial understanding of the medical domain has already been included in the Unified Medical Language System (UMLS) (Lindberg et al., 1993), which includes medical concepts, relations, definitions, etc. The 2012 version of the UMLS contains information about more than 2.7 million concepts from over 160 source vocabularies. Softwares for using this knowledge also exist: MetaMap (Aronson, 2001) is able to identify concepts in text. SEMREP (Rindflesch and Fiszman, 2003) can detect some relations using hand-crafted rules.

## Relation Extraction

To extract semantic relations from text, three types of approaches have been applied. Rule-based methods (Miller et al., 2000) employ a number of linguistic rules to capture relation patterns. Feature-based methods (Kambhatla, 2004;Zhao and Grishman, 2005) transform relation instances into a large amount of linguistic features like lexical, syntactic and semantic features, and capture the similarity between these feature vectors. Recent results mainly rely on kernel-based methods. Many of them focus on using tree kernels to learn parse tree structure related features (Collins and Duffy, 2001;Culotta and Sorensen, 2004;Bunescu and Mooney, 2005).

Other researchers study how different approaches can be combined to improve the extraction performance. For example, by combining tree kernels and convolution string kernels, (Zhang et al., 2006) achieved the state of the art performance on ACE data (ACE, 2004). Recently, "distant supervision" has emerged to be a popular choice for training relation extractors without using manually labeled data (Mintz et al., 2009;Jiang, 2009;Chan and Roth, 2010;Wang et al., 2011;Riedel et al., 2010;Ji et al., 2011;Hoffmann et al., 2011;Surdeanu et al., 2012;Takamatsu et al., 2012;Min et al., 2013).

Various relation extraction approaches have been adapted to the medical domain, most of which focus on designing heuristic rules targeted for diagnosis and integrating the medical ontology in the existing extraction approaches. Results of some of these approaches are reported on the i2b2 data (Uzuner et al., 2011).

# Identifying Key Medical Relations

## Super Relations in Medical Domain

The first step in building a relation extraction system for medical domain is to identify the relations that are important for clinical decision making.

Four main clinical tasks that physicians engage in are discussed in (Demner-Fushman and Lin, 2007). They are Therapyselect treatments to offer a patient, taking consideration of effectiveness, risk, cost and other factors (prevention is under the general category of Therapy), Diagnosis (including differential diagnosis based on findings and diagnostic test), Etiologyidentify the factors that cause the disease and Prognosisestimate the patient's likely course over time. These activities can be translated into "search tasks". For example, the search for therapy is usually the therapy selection given a disease.

We did an independent study regarding what clinical questions usually ask for on a set of 5,000 Doctor Dilemma (DD) questions from the American College of Physicians (ACP). This set includes questions about diseases, treatments, lab tests, and general facts 1 . Our analysis shows that about 15% of these questions ask for treatments, preventions or contraindicated drugs for a disease or another way around, 4% are about diagnosis tests, 6% are about the causes of a disease, 1% are about the locations of a disease, 25% are about the symptoms of a disease, 8% are asking for definitions, 7% are about guidelines and the remaining 34% questions either express no relations or some relations that are not very popular.

Based on the analysis in (Demner-Fushman and Lin, 2007) and our own results, we decided to focus on seven key relations in the medical domain, which are described in Table 1. We call these relations "super relations", since they cover most questions in the DD question set and align well with the analysis result in (Demner-Fushman and Lin, 2007).

## Collect Training Data

This section presents how we collect training data for each relation. The overall procedure is illustrated in Figure 1.

1 Here's an example of these questions and its answer: Question: The syndrome characterized by joint pain, abdominal pain, palpable purpura, and a nephritic sediment. Answer: Henoch-Schonlein purpura.

# Large Amount of Noisy Relation Data

Medical Text

# Relation Knowledge in Medical Domain

Training Data for Each Relation Our medical corpus has incorporated a set of medical books/journals2 and MEDLINE abstracts. We also complemented these sources with Wikipedia articles. In total, the corpus contains 80M sentences (11 gigabyte pure text).

The UMLS 2012 Release contains more than 600 relations and 50M relation instances under around 15 categories. The RO category (RO stands for "has Relationship Other than synonymous, narrower, or broader") is the most interesting one, and covers relations like "may treat", "has finding site", etc.

Each relation has a certain number of Concept Unique Identifier (CUI) pairs that are known to bear that relation. In UMLS, some relation information is redundant. Firstly, half of these relations are simply inverse of each other (e.g. the relation "may treat" and "may be treated by"). Secondly, there is a significant amount of redundancy even among non-inverse relations (e.g. the relation "has manifestation" and "disease has finding").

From UMLS relations, we manually chose a subset of them that are directly related to the super relations discussed in Section 3.1. The correspondences between them are given in Table 1. One thing to note is that super relations are more general than the UMLS relations, and one super relation might integrate multiple UMLS relations. Using the CUI pairs in the UMLS relation knowl- To collect the training data for each super relation, we need to collect sentences that express the relation. To achieve this, we parsed all 80M sentences in our medical corpus, looking for the sentences containing the terms that are associated with the CUI pairs in the knowledge base. This (distant supervision) approach resulted in a huge amount of sentences that contain the desired relations, but also brought in a lot of noise in the form of false positives. For example, we know from the knowledge base that "antibiotic drug" may treat "Lyme disease". However the sentence "This paper studies the relationship between antibiotic drug and Lyme disease" contains both terms but does not express the "treats" relation.

The most reliable way to clean the training data is to ask annotators to go through the sentences and assign the sentences with positive/negative labels. However, it will not work well when we have millions of sentences to vet. To minimize the human labeling effort, we ran a K-medoids clustering on the sentences associated with each super relation and kept the cluster centers as the most representative sentences for annotation. Depending on the number of the sentences we collected for each relation, the #clusters was chosen from 3,000 -6,000. The similarity of two sentences is defined as the bag-of-words similarity of the dependency paths connecting arguments. Part of the resulting data was manually vetted by our annotators, and the remaining was held as unlabeled data for further experiments.

Our relation annotation task is quite straightforward, since both arguments are given and the decision is a Yes-or-No decision. The noise rate of each relation (#sentences expressing the relation / #sentences) is reported in Table 1 based on the annotation results. The noise rates differ significantly from one relation to another. For "treats" relation, only 16% of the sentences are false positives. For "contraindicates" relation, the noise rate is 97%.

To grow the size of the negative training set for each super relation, we also added a small amount of the most representative examples (also coming from K-medoids clustering) from each unrelated UMLS relation to the training set as negative examples. This resulted in more than 10,000 extra negative examples for each relation.

## Parsing and Typing

The most well-known tool to detect medical entity mentions is MetaMap (Aronson, 2001), which considers all terms as entities and automatically associates each term with a number of concepts from UMLS CUI dictionary (Lindberg et al., 1993) with 2.7 million distinct concepts.

The parser used in our system is Medi-calESG, an adaptation of ESG (English Slot Grammar) (McCord et al., 2012) to the medical domain with extensions of medical lexicons integrated in the UMLS 2012 Release. Compared to MetaMap, MedicalESG is based on the same medical lexicons, 10 times faster and produces very similar parsing results.

We use the semantic types defined in UMLS (Lindberg et al., 1993) to categorize argument types. The UMLS consists of a set of 133 subject categories, or semantic types, that provide a consistent categorization of more than 2M concepts represented in the UMLS Metathesaurus. Our system assigns each relation argument with one or more UMLS semantic types through a two step process. Firstly, we use Med-icalESG to process the input sentence, identify segments of text that correspond to concepts in Most relation arguments are associated with multiple semantic types. For example, the term "tetracycline hydrochloride" has two types: "Organic Chemical" and "Antibiotic". Sometimes, the semantic types are noisy due to ambiguity of terms. For example, the term "Hepatitis b" is associated with both "Pharmacologic Substance" and "Disease or Syndrome" based on UMLS. The reason for this is that people use "Hepatitis b" to represent both "the disease of Hepatitis b" and "Hepatitis b vaccine", so UMLS assigns both types to it. This is a concern for relation extraction, since two types bear opposite meanings. Our current strategy is to integrate all associated types, and rely on the relation detector trained with the labeled data to decide how to weight different types based upon the context.

Here is an illustrative example. Consider the sentence: "Antibiotics are the standard therapy for Lyme disease": MedicalESG first generates a dependency parse tree (Figure 2) to represent grammatical relations between the words in the sentence, and then associates the words with CUIs. For example, "Antibiotics" is associated with CUI "C0003232" and "Lyme disease" is associated with two CUIs: "C0024198" and "C0717360". CUI lookup will assign "Antibiotics" with a semantic type "Antibiotic", and "Lyme disease" with three semantic types: "Disease or Syndrome", "Pharmacologic Substance" and "Immunologic Factor". This sentence expresses a "treats" relation between "Antibiotics" and "Lyme disease".

# Relation Extraction with Manifold Models

## Motivations

Given a few labeled examples and many unlabeled examples for a relation, we want to build a relation detector leveraging both labeled and unlabeled data. Following the manifold regularization idea (Belkin et al., 2006), our strategy is to learn a function that assigns a score to each example. Scores are fit so that examples (both labeled and unlabeled) with similar content get similar scores, and scores of labeled examples are close to their labels. Integration of the unlabeled data can help solve overfitting problems when the labeled data is not sufficient.

## Features

We use 8 groups of features to represent each relation example. These features are commonly used for relation extraction.

• (1) Semantic types of argument 1, such as "Antibiotic".

• (2) Semantic types of argument 2.

• (3) Syntactic features representing the dependency path between two arguments, such as "subj", "pred", "mod nprep" and "objprep" (between arguments "antibiotic" and "lyme disease") in Figure 2.

• (4) Features modeling the incoming and outgoing links of both arguments. These features are useful to determine if a relation goes from argument 1 to argument 2 or vice versa.

• (5) Topic features modeling the words in the dependency path. In the example given in Figure 2, the dependency path contains the following words: "be", "standard therapy" and "for". These features as well as the features in ( 6) are achieved by projecting the words onto a 100 dimensional LSI topic space (Deerwester et al., 1990) constructed from our medical corpus.

• (6) Topic features modeling the words in the whole sentence.

• (7) Bag-of-words features modeling the dependency path. In ( 7) and ( 8), we only consider the words that have occurred in the positive training data.

# Notations:

The input dataset X = {x 1 , • • • , x m } is represented as a feature-instance matrix.

The desired label vector

W is a weight matrix, where W i,j = e -x i -x j 2 models the similarity of x i and x j .

x i -x j stands for the Euclidean distance between x i and x j in the vector space.

∆ is a user defined l × l diagonal matrix, where ∆ i represents the weight of label y i .

µ is a weight scalar.

() + represents pseudo inverse.

# Algorithm:

1. Represent each example using features:

, where x i is the ith example.

# Construct graph Laplacian matrix L

modeling the data manifold. We represent all features in a single feature space. For example, we use a vector of 133 en-tries (UMLS contains 133 semantic types) to represent the types of argument 1. If argument 1 is associated with two types: "Organic Chemical" and "Antibiotic", we set the two corresponding entries to 1 and all the other entries to 0. Similar approaches are used to represent the other features.

# Compute projection function f for each relation

## The Main Algorithm

The problem we want to solve is formalized as follows: given a relation dataset

, where l ≤ m, we want to construct a mapping function f to project any example x i to a new space, where f T x i matches x i 's desired label y i . In addition, we also want f to preserve the manifold topology of the dataset, such that similar examples (both labeled and unlabeled) get similar scores. Here, the label is '+1' for positive examples, and '-1' for negative examples. Notations and the main algorithm to construct f for each relation are given in Figure 3.

## Justification

The solution to the problem defined in Section 4.3 is given by the mapping function f to minimize the following cost function:

The first term of C(f ) is based on labeled examples, and penalizes the difference between the mapping result of x i and its desired label y i . α i is a user specified parameter, representing the weight of label y i . The second term of C(f ) does not take label information into account. It encourages the neighborhood relationship (geometry of the manifold) within X to be preserved in the mapping. When x i and x j are similar, the corresponding W i,j is big. If f maps x i and x j to different positions, f will be penalized. The second term is useful to bound the mapping function f and prevents overfitting from happening. Here µ is the weight of the second term. When µ = 0, the model disregards the unlabeled data, and the data manifold topology is not respected.

Compared to manifold regularization (Belkin et al., 2006), we do not include the RKHS norm term. Instead, we associate each labeled example with an extra weight for label confidence. This weight is particularly useful when the training data comes from "Crowdsourcing", where we ask multiple workers to complete the same task to correct errors. In that scenario, weights can be assigned to labels based upon annotator agreement.

Theorem 1: f = (X(A + µL)X T ) + XAV T minimizes the cost function C(f ).

# Proof:

Given the input X, we want to find the optimal mapping function f such that C(f ) is minimized:

We can also verify that

So C(f ) can be written as

Using the Lagrange multiplier trick to differentiate C(f ) with respect to f , we have

# This implies that

where "+" represents pseudo inverse.

## Advantages

Our algorithm offers the following advantages:

• The algorithm exploits unlabeled data, which helps prevent "overfitting" from happening.

• The algorithm provides users with the flexibility to assign different labels with different weights. This feature is useful when the training data comes from "crowdsourcing" or "distant supervision".

• Different from many approaches in this area, our algorithm provides a closed-form solution of the result. The solution is global optimal regarding the cost function C(f ).

• The algorithm is computationally efficient at the apply time (as fast as linear regressions).

# Experiments

## Cross-Validation Test

We use a cross-validation test 3 with the relation data generated in Section 3.2 to compare our approaches against the state-of-the-art approaches.

The task is to classify the examples into positive or negative for each relation. We applied a 5-fold cross-validation. In each round of validation, we used 20% of the data for training and 80% for testing. The F 1 scores reported here are the average of all 5 rounds. We used MedicalESG to process the input text for all approaches.

### Data and Parameters

This dataset includes 7 relations. We do not consider the relation of " No parameter tuning was taken and no relation specific heuristic rules were applied in all tests. In all manifold models, µ = 1. In SVM implementations, the trade-off parameter between training error and margin was set to 1 for all experiments.

### Baseline Approaches

We compare our approaches to three state-of-theart approaches including SVM with convolution tree kernels (Collins and Duffy, 2001), linear regression and SVM with linear kernels (Sch ölkopf and Smola, 2002). To adapt the tree kernel to medical domain, we followed the approach in (Nguyen et al., 2009) to take the syntactic structures into consideration. We also added the argument types as features to the tree kernel. In the tree kernel implementation, we assigned the tree structure and the vector corresponding to the argument types 3 If we take the perfect entity mentions and the associated concepts provided by i2b2 (Uzuner et al., 2011) as the input, our system can directly apply to i2b2 relation extraction data. However, the i2b2 data has a tough data use agreement. Our legal team held several rounds of negotiations with the i2b2 data owner and then decided we should not use it due to the high legal risks. We are not aware of other available medical relation extraction datasets that fit for our evaluations. with equal weights. The SVM with linear kernels and the linear regression model used the same features as the manifold models.

### Settings for the Manifold Models

We tested our manifold model for each relation under three different settings:

(1) Manifold Unlabeled: We combined the labeled data and unlabeled set 1 in training. We set

(2) Manifold Predicted Labels: We combined labeled data and unlabeled set 2 in training. α i = 1 for i ∈ [1, l]. Different from the previous setting, we gave a label estimation to all the examples in the unlabeled set 2 based on the noise rate (Noise%) from Table 1. The label of all unlabeled examples was set to "+1" when 100% -2 • N oise% > 0, or "-1" otherwise. Two weighting strategies were applied:

• With Weights: We let label weight α i = |100% -2 • N oise%| for all x i coming from the unlabeled set 2. This setting represents an empirical rule to estimate the label and confidence of each unlabeled example based on the sampling result.

• Without Weights: α i is always set to 1.

(3) Manifold UnLabeled+Predicted Labels: a combination of setting (1) and (2). In this setting, the data from unlabeled set 1 was used as unlabeled data and the data from unlabeled set 2 was used as labeled data (With Weights).

### Results

The results are summarized in Table 2.

The tree kernel-based approach and linear regression achieved similar F 1 scores, while linear SVM made a 5% improvement over them. One thing to note is that the results from these approaches vary significantly. The reason for this is that the labeled training data is not sufficient. So the approaches that completely depend on the labeled data are likely to run into overfitting. Linear SVM performed better than the other two, since the large-margin constraint together with the linear model constraint can alleviate overfitting.

By integrating unlabeled data, the manifold model under setting (1) made a 15% improvement over linear regression model on F 1 score, where the improvement was significant across all relations.

Under setting (2), the With Weights strategy achieved a slightly worse F 1 score than the previous setting but much better result than the baseline approaches. This tells us that estimating the label of unlabeled examples based upon the sampling result is one way to utilize unlabeled data and may help improve the relation extraction results. The results also show that the label weight is important for this setting, since the Without Weights strategy did not perform very well.

Compared to setting (1) and (2), setting (3) made use of 2,500 more unlabeled examples, and achieved the best performance among all approaches. On one hand, this result shows that using more unlabeled data can further improve the result. On the other hand, the insignificant improvement over (1) and ( 2) strongly indicates that how to utilize more unlabeled data to achieve a significant improvement is non-trivial and deserves more attention. To what extensions the unlabeled data can help the learning process is an open problem. Generally speaking, when the existing data is sufficient to characterize the dataset geometry, adding more unlabeled data will not help (Singh et al., 2008).

We tested the tree kernel-based approach without integrating the medical types as well. That resulted in very poor performance: the average F 1 score was below 30%. We also applied the rules used in SEMREP (Rindflesch and Fiszman, 2003) to this dataset. Since the relations detected by SEMREP rules cannot be perfectly aligned with super relations, we cannot directly compare the results. Overall speaking, SEMREP rules are very conservative and detect very few relations from the same text.

## Knowledge Base (KB) Construction

The UMLS Metathesaurus (Lindberg et al., 1993) contains a large amount of manually extracted relation knowledge. Such knowledge is invaluable for people to collect training data to build new relation detectors. One downside of using this KB is its incompleteness. For example, it only contains the treatments for about 8,000 diseases, which are far from sufficient. Further, the medical knowledge is changing extremely quickly, making people hard to understand it, and update it in the knowledge base in a timely manner.

To address these challenges, we constructed our own relation KB as a complement to the UMLS relation KB. We directly ran our relation detectors (trained with all labeled and unlabeled examples) on our medical corpus to extract relations. Then we combined the results and put them in a new KB. The new KB covers all super relations and stores the knowledge in the format of (relation name, argument 1, argument 2, confidence), where the confidence is computed based on the relation detector confidence score and relation popularity in the corpus. The most recent version of our relation KB contains 3.4 million such entries.

We compared this new KB against UMLS KB using an answer generation task on a set of 742 Doctor Dilemma questions. We first ran our relation detectors to detect the relation(s) in the question clue involving question focus (what the question asks for). Then we searched against both KBs using the relation name and the non-focus argument for the missing argument. The search results were then generated as potential answers. We used the same relations to do KB lookup, so the results are directly comparable. Since most questions only have one correct answer, the precision number is not very important in this experiment.

If we detect multiple relations in the question, and the same answer is generated from more than one relations, we sum up all those confidence scores to make such answers more preferable. Sometimes, we may generate too many answers from KBs. For example, if the detected relation is "location of" and the non-focus argument is "skin", then thousands of answers can be generated. In this scenario, we sort the answers based upon the confidence scores and only consider up to p answers for each question. In our test, we considered three numbers for p: 20, 50 and 3,000.

From Table 3, we can see that the new KB outperforms the most popularly-used UMLS KB at all recall levels by a large margin. This result indicates that the new KB has a much better knowledge coverage. The UMLS KB is manually created and thus more precise. In our experiment, the UMLS KB generated fewer answers than the new KB. For example, when up to 20 answers were generated for each question, the UMLS KB generated around 4,700 answers for the whole question set, while the new KB generated about 7,600 answers.

Construction of the new KB cost 16 machines (using 4×2.8G cores per machine) 8 hours. The reported computation time is for the whole corpus with 11G pure text. 

# Acknowledgments

We thank Siddharth Patwardhan for help on tree kernels, Sugato Bagchi and Dr. Herbert Chase's team for categorizing the Doctor Dilemma questions. We also thank Anthony Levas, Karen Ingraffea, Mark Mergen, Katherine Modzelewski, Jonathan Hodax, Matthew Schoenfeld and Adarsh Thaker for vetting the training data.

