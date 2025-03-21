# Introduction

When deploying deep learning in real-life scenarios, training data is often sparse. Transfer learning improves learning of such target tasks by leveraging knowledge from a source task, as shown in Figure 1. The improvement in learning could be measured by either improvement in accuracy (for example, F 1 score), or reduction in the time taken to learn the task.

With the increased popularity of the large transformer-based models Devlin et al. (2019), transfer learning in the form of fine-tuning a base model is ubiquitous in NLP. However, the performance of the learned target model depends critically on the chosen source model. Simply selecting the largest dataset can lead to sub-optimal performance, and trying all sources is computationally expensive.

We demonstrate a prediction technique for the sequence labelling task, which given a target model, selects the "best" source model from among a set of available source models, according to a novel and inexpensive metric. Then, only that single selected (trained) source model is further fine-tuned on the target dataset. We show that our selection technique is effective at selecting the source model that most improves F 1 score, over nine different tasks, with no additional training. Further, our technique results in an average gain of over 3% in F 1 over selecting a base model randomly, and over 4% in F 1 over training a model without transfer learning from any source model.

In the rest of the paper, we chronicle prior work in the area of transfer learning, describe the sequence labeling task, and follow with the description of our predictive model selection methodology.

# Prior Work

The transfer learning literature spans different topics and strategies such as few-shot learning (Socher et al., 2013), domain adaptation (Patricia and Caputo, 2014), weight synthesis (Sussillo and Abbott, 2017), and multitask learning (Jiang, 2009;Nguyen et al., 2016;Torrey and Shavlik, 2009). Some works propose novel combinations of these approaches, in order to improve transfer performance under conditions of domain transfer with limited or incomplete annotations (Luo et al., 2017).

Some prior research on optimizing source selection has focused on instance transfer techniques, like Zhou et al. (2016) and Lin et al. (2013), which select a subset of examples from a source for transfer learning. Other approaches, like Schultz et al. (2018), propose methods to select the right set of source domain datasets for a task such as sentiment classification. Yet another approach, Afridi et al. (2018), which is more popular in computer vision research, selects sub-models of the source model and re-trains only on those.

Alternatively, Bhattacharjee et al. (2020) focuses on predicting the best source model, in the domains of computer vision and of semantic relations, by measuring the similarity between the source and target datasets, using a mix of metrics like KL divergence and source dataset size. In NLP, this approach works for sentence-level classification tasks such as sentiment classification. But it does not adapt well for sequence labelling tasks, where labels span across tokens rather than sentences, and where the similarity of the label spaces need to be accounted for. Additionally, their approach requires either the entire source dataset or its feature vector representation to be available. In contrast, the method we demonstrate here only needs the source model itself.

# Task Definition

A sequence labelling task assigns a label to each member of a sequence of observed values. An example is Named Entity Recognition (NER), which identifies in unstructured text all contiguous typed references to task-specific real-world entities, such as persons, organizations, facilities, locations, etc. An example is shown in Figure 2.

We formally define the Transfer Learning task for this paper as follows: given a set M of N source models trained for sequence labelling, M = {M 1 , M 2 , . . . , M N }, and one target set t, the task is to find the best source model M k , which when used as a base model for transfer learning, would result in a model with highest performance.

We use F 1 as the metric to measure performance, and compute relative gain in F 1 to measure the improvement in performance.

# Predictive Model Selection

To select the best transfer learning base model, our method compares the target and source using a novel similarity metric. Instead of comparing the source and target datasets, our method compares the target test-set with the output of the source model on the target test-set. This comparison takes label weights into account.

To compare a target with each of the source models, we decode the target test-set through the source model. We call this output ŷ, and the original target annotation y. We next compare y and ŷ using the metrics described. The source model with the highest metric score is chosen as the best source model.

## Metrics

For predicting which model would be the best for a target dataset, we have experimented with two measures, called Span Similarity and Weighted Span Similarity, described here.

For Named Entity Recognition, an extracted span is customarily considered correct if the offset of the span matches that of the reference span, and the type of the span matches that of the reference span. In this work, however, we ignore the types of the spans. We therefore define Span Similarity (SS) based on the score computed between gold (y) and system output (ŷ) using only the offsets.

where TP = number of true positives, FP = number of false positives, and FN = number of false negatives, as decided by the above selection criteria. This is basically the Sorensen-Dice coefficient. To account for the "goodness" of the source model, we weight Span Similarity by the F 1 score of the source model on the source test-set, F 1 (s). This we call the Weighted Span Similarity (WSS).

We select the source model with the highest WSS score to be the best base model for transfer learning.

## Transfer Learning

The Once the source model with the highest WSS is selected, we use it as the base for transfer learning. To capture the knowledge of the source model, we use the context representation layer of the source model, but replace its classifier layer with a new classifier mapped to the target model space. We then fine-tune this new model on the target dataset.

# Experimental Evaluation

## Datasets and Source Models

We test our method on the various datasets shown in Table 1, all comprising of named entity annotated data, with different number of types as described in the lined citations. Alchemy1 and Alchemy2 are newswire datasets labeled internally with 47 and 54 types (person, organization, company, etc), respectively. Cybersecurity, the other dataset that is not cited, is a dataset of cybersecurity related articles (descriptions of virus attacks, etc.), labeled internally.

For each of the datasets, we sample a small percentage (5-20%) of examples in order to create our target sets. We use the full dataset as a source, and the small sampled sets as target sets. We train NER models using the method described in Devlin et al. ( 2019) on full source datasets, using the setup described in Section 5.4.

## Generating Ground Truth

To test our method, we need to determine which source is truly the best for a given target. We proceed as follows.

We formally denote the N source datasets as S = {s 1 , s 2 , . . . , s N }, and the N target datasets as T = {t 1 , t 2 , . . . , t N }.

To set up the evaluation of our method, we first train NER models on all source datasets, to get a set of source models M = {M 1 , M 2 , . . . , M N }. Each one of these is comprised of a context layer and a classifier layer.

Next, to get the absolute ground truth model for a given target dataset t k , we train a model G k for t k without any transfer learning.

Lastly, we train a suite of ground truth transfer models for each dataset t k . We fine-tune each of the source models M i , i = k, by retaining its context layer but adapting its classifier layer. This gives for each t k a suite of ground truth transfer models, G k = {G k,i , i = k}, where G k,i is the ground truth transfer model for t k using source M i .

For each of the models in M k we then compute the relative gain in F 1 in the usual way:

where F 1 (k, i) returns the F 1 score of the model G k,i , and where F 1 (k) does the same for G k . Therefore, the best ground truth transfer model for t k is defined to be:

## Baselines

We compare our method to the following baselines: 1. Largest Source: This method picks the source with the largest dataset size as the best base model.

2. Random Selection: This method picks a source at random as the best base model.

3. Cosine Similarity: Cosine similarity has been frequently used in distributional semantics (Mikolov et al., 2013;Peterson, 2009;Wagstaff et al., 2001). We compute the cosine similarity between a target model G k and each of the source models M i (see Section 5.2), by decoding the t k test-set with both target and source models, and using the outputs of their respective context representation layers, called A and B, to compute:

We do this for all M i , i = k, and choose the M i with highest cosine similarity with the test-set t k . 4. KL Divergence: Bhattacharjee et al. (2020) use KL divergence as selection metric in their method. To compute the KL Divergence between the source dataset s i and the target dataset t k , we decode both datasets with M i , and compare their context representation layers, called P and Q, to compute:

5. Target-only Model: We also compare our method with models trained directly with vanilla BERT over the target test-set, i.e., over t k as described in Section 5.2.

## Experimental Setup Details

The models are built using the HuggingFace Py-Torch implementation of Transformers Wolf et al. (2019). Our model uses bert-base-cased with the standard hyperparameters. We train the source and target models for 20 epochs, with a learning rate of 5e-5 and a batch of 32. We use K80 gpus to train our models.

# Results and Discussion

## Accuracy and Time Cost

Table 2 shows a summary of the F 1 gains by using our method to predict the best source model, compared to other baseline selection methods. Our SS method is able to predict the correct source model 5 out of 9 times, and our WSS method can predict the correct source model 7 out of 9 times. This is significantly better than any other baseline.

In terms of accuracy, our WSS method outperforms the baselines, as follows: largest source, 6 out of 9 times, with average gain of 3.04%; random selection, 9 out of 9 times, with average gain of 3.43%; cosine similarity, 4 out of 9 times, with average gain of 1.17%; KL divergence, 7 out of 9 times, with average gain of 1.36%; and no NER transfer learning, 8 out of 9 times, with average gain of 4.85%.

We note that some of our performance improvements can be attributed to a fundamental difference between our method and other baseline methods like Cosine Similarity, KL divergence, etc. Whereas other methods compare similarity of the input text space, our method computes similarity within the label space, taking advantage of learned contextual relationships.

Our method consistently works across diverse domains, and is able to correctly predict models particularly for news, forum, airline travel, and cybersecurity domains. None of the baselines work as well across these domains. Our method also saves substantially on computational time and resources, as it finds the best source model with fewer tries, as shown in Figure 3. In most cases, our method is able to predict the best model on the first try, whereas the largest source baseline needs four tries. With the experimental setup described in section 5.4 it takes on average 1.5 hours to train a target model, as compared to the 6 hours it takes the largest source baseline to produce the best model. This is a compute cost saving of 75%.

## Potential Application to Computer Vision

The problem of finding both a span boundary and a label is not limited to sequence labelling in NLP. Object Detection (Szegedy et al., 2013) in vision research, has similar requirements: one is expected to label objects in an image and to mark the bounding box of the objects individually. Figure 4 shows an example where the task is to detect cookies and mark the bounding boxes around them. Moreover, both Object Detection and Sequence Labelling have similar measures of accuracy. It would be interesting to expand the method proposed in this paper to determine which source object detection base model would be a good fit for a given target data set from a collection of source object detection models. We plan to explore this in future.

# Conclusion

In this paper we present a simple and effective method to predict the best source model for transfer learning in a sequence labelling task, NER. We show our method outperforms popular baselines such as the selection of the largest source, by an average relative 3 F 1 points. And, it is more than average relative 4 F 1 points better than a method that does not use NER transfer learning. Moreover, our method consistently selects the best model with fewer tries, saving computational cycles by roughly 75%.

# Acknowledgments and Disclaimer

This material is based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under Contract No. FA8750-19-C-1001.

Any opinions, findings and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).

