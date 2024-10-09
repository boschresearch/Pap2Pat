# Introduction

The whole AI community has enjoyed a superior performance boost from the emerging of deep learning technologies, thanks to the availability of big data and computing technologies. One of the most recent, realistic and emerged challenges for deep learning models on streaming data is continual learning capability. When new data is available, re-training brand new models with all the old and new data is the ideal way to achieve high performance on both tasks. However, there are several factors preventing saving old data for the entire lifetime, such as the memory restriction and data governance. When learning without all the old data, the performance on old tasks will drop dramatically, this phenomenon is called catastrophic forgetting (Mcclelland et al., 1995).

Catastrophic forgetting occurs in neural networks due to the stability-plasticity dilemma (Abraham and Robins, 2005), where the network requires sufficient plasticity to capture new tasks, but large weights variations may disrupt previous learned representations. Continual learning methods are proposed to prevent catastrophic forgetting, when only a limited size of old data is available.

Several approaches have been proposed to solve this problem in deep learning field (Awasthi and Sarawagi, 2019;Rusu et al., 2016;Zhizhong Li, 2018;Kirkpatrick et al., 2016;Riemer et al., 2019;Serra et al., 2018;Hou et al., 2018). A popular trend is to use expandable networks to store/learn old/new knowledge then acquire a task ID to select one from all the tasks during the inference stage. (Rusu et al., 2016;Mallya et al., 2018;Yoon et al., 2017;Mallya and Lazebnik, 2017).

In contrast, only a few attempts have been made to address catastrophic forgetting in natural language forgetting (NLP) field. Elastic Weight Consolidation (EWC) (Kirkpatrick et al., 2016) has been adapted to visual question answering (Greco et al., 2019) and language modeling (Wolf et al., 2019). Progressive Neural Network proposed in reinforcement learning (Rusu et al., 2016) has been adopted to semantic slot filling in (Shen et al., 2019). A continual learning architecture preventing catastrophic forgetting via block-sparsity and orthogonality constraints is presented in (Pasunuru and Bansal, 2019) on diverse sentence-pair classification tasks. To our best knowledge, none of the previous works in NLP considers the interactions between tasks at the LSTM cell level. Moreover, the requirement of task IDs in inference is infeasible and impractical in the real scenarios as shown in Fig. 1. Therefore, a novel Continual Learning Long Short Term Memory (CL-LSTM) cell is proposed to prevent catastrophic forgetting. The contributions of the paper are: (a) a novel LSTM cell for continual learning is proposed. The proposed CL-LSTM includes separate modules for different tasks; (b) each task further has a broadcast module to send its hidden states to all of the old tasks, and a collect module to take hidden states as inputs from all of the old tasks. Therefore, the output gates of each task integrates information from all tasks; (c) the proposed model doesn't require task IDs to perform inference, which is more practical in real-world scenarios. We evaluate the proposed CL-LSTM on both slot filling and intent detection of spoken language understanding. Experimental results show that the proposed CL-LSTM outperforms state-of-the-arts by a large margin. Code is available at https: //github.com/IBM-GCDO/EMNLP-CL-LSTM.

# Method

## Preliminary: LSTM

As we know, LSTM (Long Short Term Memory) (Hochreiter and Schmidhuber, 1997) operates as a parameterized function R that takes an input vector x t with a state vector (c t-1 , h t-1 ) and returns a state vector (c t , h t ) = R(x t , c t-1 , h t-1 ). (yellow) are trained for information sharing. h

out is the aggregation of all hidden states. Specifically, it incorporates a gating mechanism, taking the form:

where W s and U s are learnable matrices, bs are biases. If we integrate W s and U s into one single matrix W , combine bs into b, then by concatenating x t and h t-1 together, we have:

The outputs c t and h t can be obtained from:

where σ indicates the sigmoid function, • represents the Hadamard product, g can be either tanh or the identity function. In this paper, we are interested in the hidden states: for a standard LSTM cell with parameters {W, b} included within one module M , the update of h t can be represented as:

## CL-LSTM

As discussed above, model parameters {W, b} in the standard LSTM cell keep updating once the given cell starts to learn the new task, which makes it difficult to avoid catastrophic forgetting. To mitigate this phenomena, we propose a novel cell named CL-LSTM as illustrated in Fig. 2, which is mainly composed of the following components: Task-oriented Modules. Assuming that the model is going to learn K tasks sequentially. The training data is X = {X 1 , X 2 , ..., X K }, where X k denotes the training dataset for the k th task. There are C k different classes included in task k. When the first task comes, CL-LSTM starts with a single module

1 is the hidden state at timestamp t, T represents the length of sequential data x, c k } is created for task k to collect all hidden states from all previous modules. For any 1 ≤ j ≤ k, the hidden states of module j are updated by:

where h

(t) j is the updated hidden state of module j with additional information sharing. Note that at task k, M c j and M b j are frozen for all j < k. The intuition of broadcast and collect module is: when learning a new task k, M c k can learn how to aggregate weighted previous knowledge to accelerate and improve the knowledge learning of task k. And via M b k , the knowledge of task k can broadcast to previous modules, facilitating the task separations as well as enhancing the performance of old tasks.

Hidden States and Outputs. {1, 2, • • • , k}. To avoid using task ID to select different modules for different tasks during inference, we directly feed the input data to all modules and aggregate the knowledge from ∀k ≤ K tasks, an unique output hidden state h

out k is obtained by:

Note that different from standard LSTM, here h

is the summation of all modules' hidden states.

# Experiments

In this section, CL-LSTM is evaluated on Spoken Language Understanding (SLU) tasks in continual learning framework. SLU mainly includes two goals: slot filling and intent detection. Slot filling is a sequence labelling problem which maps each sentence to a sequence of slot labels with the same length, while intent detection is a classification problem where each sentence has one intent label.

## Datasets

We evaluate the performance of the proposed CL-LSTM on five datasets (Table 1): Airline Travel Information Systems (ATIS) (Hemphill et al., 1990), Snips (Coucke et al., 2018), Weather Reminder (WR) (Wea), MIT Corpus Movie (MV) (MIT, a) and MIT Corpus Restaurant (RT) (MIT, b). ATIS, Snips and WR datasets have both slot and intent labels while RT and MV have slot labels only.

## Experimental Settings

Two experimental settings are proposed to fully utilize these multi-goal datasets to evaluate catastrophic forgetting in continual learning. Exp1: in order to perform both slot filling and intent detection simultaneously, each method is evaluated on three tasks sequentially: ATIS→SNIPS→WR, where each dataset is a task.

Exp2: in order to use all the datasets, each method is evaluated on five tasks for slot filling only with task order: ATIS→SNIPS→WR→RT→MV.

When training a new task, only N exemplars (training samples) from previous tasks are kept.

## Training Details

We use

out k } for slot filling, and the final state h (T ) out k for intent detection. Specifically, the predictions (p slot , p intent ) are made by adding fully connect layers F slot and F intent to sequential hidden outputs h out k and final hidden outputs h (T ) out k , respectively:

Model parameters are updated with cross-entropy loss. F slot , F intent are always trainable to allow information sharing among different tasks.

## Evaluation Metrics

F1-score and classification accuracy are reported for slot filling and intent detection, respectively. Semantic accuracy as defined in (Schuster and Paliwal, 1997) is used to evaluate the combined performance of both slot filling and intent detection.

In order to evaluate the overall model performance, after training the last task, averaged metrics are computed on the test datasets of all the tasks. Average metrics show models' effectiveness on preventing catastrophic forgetting, since performance drop on old tasks will lead to a lower average.

## Baseline Models

Four baseline methods including fine-tuning, joint training, Learning Without Forgetting (LWF) (Zhizhong Li, 2018) and EWC (Kirkpatrick et al., 2016) are used to compare with the proposed CL-LSTM. Specifially, fine-tuning loads trained model on previous task to initialize model parameters; Joint training trains with the training data of all the tasks in each experiment and serves as the upper bound; LWF is a state-of-the-art continual learning method which can be adapted to language understanding tasks; EWC has been adapted to natural language understanding tasks such as visual question answering and language modeling.

## Implementation Details

To perform a fair comparison, a bidirectional LSTM (Bi-LSTM) is used as the model structure for these baseline methods. All models are implemented with TensorFlow 1.  as input, and output vectors with dimensions same as the number of slot labels and intent labels, respectively.

All models are trained with Adam optimisation (Kingma and Ba, 2014) method. The learning rate is initially set to be 0.001 and updated with a decay rate of 0.05. For each task, model is trained for 100 epochs, and the best performed model on the current task is selected. Besides, using Ubuntu-18.04.1 system with 2 GPUs (NVIDIA V100-SXM2-16gb), CL-LSTM takes (i) 8 hours to run 100 epochs for 3 tasks experiment; (ii) 20 hours to run 100 epochs for 5 tasks experiment.

## Experimental Results

For Exp1, experimental results on F1-score, intent accuracy and semantic accuracy along with the exemplar size are shown in Table 2∼4, respectively. Note that the results of joint training are invariant to the number of exemplar size since it refers to the training with all the training data of all the tasks.

We also evaluate another two versions of the proposed CL-LSTM which are CL-LSTM -and  Experimental results show that CL-LSTM and CL-LSTM + outperform state-of-the-art methods (fine-tuning, LWF and EWC models). The results in Table 4 also show that the proposed CL-LSTM models outperform baseline methods on semantic accuracy by a margin of 3.42% when exemplar size is 500, and 9.67% when exemplar size is 50. As semantic accuracy evaluates joint performance of slot filling and intent detection, it indicates that CL-LSTM is promising for continual learning, especially with limited size of exemplars.

For Exp2 in Table 5, we observe CL-LSTM has best performance with the most and least exemplars, while EWC shows advantages in other cases. Compare to the results in Table 2∼4, EWC is problematic when it has to maintain the weights for both slot filling and intent detection. In addition, CL-LSTM is orthogonal to EWC, so EWC can be applied on top of CL-LSTM to further improve the performance. edge. However, both of the CL-LSTM and CL-LSTM + are better than CL-LSTM -, illustrating that rather than a simple aggregation (Eq. 11), the information sharing between tasks (Eq. 10) benefits both old and new tasks, which is important in continual learning. Using only one broadcast and one collect module for each task instead of specific models for every pair of tasks, performance of CL-LSTM is comparable to CL-LSTM + , showing that a simplified broadcast/collect design may avoid over-fitting, especially in fewer tasks.

# As listed in

## Analysis of Module Aggregation

In Eq. 11, the output of each module h (t)

i are aggregated into an unified output h (t) out k . The benefit of this design is that the fusion frees the dependence on task IDs during inference. A detailed analysis is provided here to further illustrate the superior performance of using h (t) out k , by comparing to models that directly use h (t) i as the output. Specifically, after training our model on ATIS→SNIPS→WR with Eq. 11, we predict on test sets of task 0,1,2 with h i = {h

(1) i , ..., h (T ) i } separately, the semantic accuracies for 50 exemplars are shown in Table 6. We can see: 1) h i only has predictive power for task ≤ i (as h i is trained with task ≤ i data, then being frozen); 2) Compared to h i , our h out has better average semantic accuracy (CL-LSTM achieves 50.46% in table 4 for 3 tasks), which shows that h out takes the advantage of information aggregation. Note that the recurrent architecture makes it possible for accuracy of h out greater than maximum accuracy among h i , i = 0, 1, 2.

# Conclusion

In this paper, we propose a novel CL-LSTM cell to alleviate catastrophic forgetting problem in continual learning frameworks. Experimental results have demonstrated that adding broadcast and collect modules can help keeping old knowledge as well as learning new knowledge. Superior performance is achieved by CL-LSTM over other related works on spoken language understanding tasks.

