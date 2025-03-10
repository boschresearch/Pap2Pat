# Introduction

Adapting pre-trained large language models (LLMs) has advanced the progress in many NLP areas (Devlin et al., 2019;Raffel et al., 2020). This is typically done by finetuning all parameters of a model on a downstream task (i.e., MODELTUN-ING). This approach is however expensive, especially given the growing sizes of SOTA LLMs.

This limitation motivates recent research on parameter-efficient methods which only tune a small amount of parameters (Houlsby et al., 2019;Brown et al., 2020;Karimi Mahabadi et al., 2021; x , and then queries the skill latent space, resulting in a skill vector e

(1)

x . The skill vector is transformed by a simple and lightweight prompt generator, outputting prompt tokens (e.g., {P1, P2}). They are prepended to the instance tokens and modulate the pre-trained frozen model. The instance encoder and the pre-trained model are frozen in all scenarios. The skill vectors are tuned in source task training and frozen in target task training. The prompt generator is tuned in both source task and target task training. Lester et al., 2021;Li and Liang, 2021;Hambardzumyan et al., 2021). Among them, a line of research focus on the methods that modulate a frozen LLM via prompts (Liu et al., 2021). Brown et al. (2020) showed that prepending an input text with a prompt, which typically consists of a task description and/or several examples, can effectively adapt a frozen GPT-3. This approach nevertheless underperforms MODELTUNING and is sensitive to the choice of prompt wordings. Instead of actual text (or hard prompt), Lester et al. (2021) proposed PROMPTTUNING, which prepends a soft prompt, consisting of k tunable tokens, to input text. The soft prompt can be optimized with gradient-based methods. PROMPTTUNING achieves competitive performance to MODELTUNING when the model size is large (e.g., over 10B parameters) but still underperforms with smaller models.

SPOT (Vu et al., 2022) improves over PROMPT-TUNING by leveraging knowledge from source tasks. They first learn a task-specific soft prompt for each task in a set of source tasks. Given a target task, they search over the set of source prompts and use the best one or some weighted combination to initialize the prompt for the target task and then tune the prompt. It further narrows the performance gap to MODELTUNING on smaller models. But it is complicated and expensive to identify the source task that provides optimal prompts.

In this work, we propose a novel prompt-based transfer learning method, SHARPT (Shared Latent Space Prompt Tuning). Figure 1 illustrates the general idea. SHARPT assumes a shared (discrete) latent space by all source and target tasks. We call each vector in the latent space as a skill vector, since we assume each one captures a basis NLP capacity or skill after training on the source tasks. Given an instance (from either a source task or a target task), an instance encoder embeds it into an instance vector, which is then used to query the latent space to find the nearest neighbor, yielding a skill vector for this instance. A lightweight prompt generator then generates soft prompts as a function of the selected skill vector. The soft prompts condition a frozen LLM. The latent space and prompt generator are learned end-to-end on a mixture of source tasks. In target task training, the latent space is frozen and only the prompt generator is tuned.

SHARPT retains the key advantage of prior prompt methods, parameter-efficiency. It only updates approximately 0.1% to 0.3% parameters compared to MODELTUNING. Different from prior methods, we add an instance encoder to encode each instance. The instance encoder is lightweight and frozen in all scenarios.

SHARPT and SPOT both exploit a generic idea, leveraging knowledge shared across tasks. The approaches to achieve this are however distinctly different. SPOT assumes task-to-task transfer based on task-level prompts and the knowledge is encoded in task prompts. It is not straightforward to identify a source prompt for a target task. They illustrated two approaches: (1) SPOT-Oracle and (2) SPOT-Retrieval. SPOT-Oracle involves using oracle test labels and expensive search (e.g., 48 times more expensive than regular prompt tuning in their experiments). In SPOT-Retrieval, they first tuned a task prompt for each source and target task independently and retrieved a prompt based on prompt similarity. Note that the retrieval tun-ing is only for searching a source prompt, which is in addition to final prompt tuning on the target task. In contrast, SHARPT assumes the knowledge is encoded in a shared latent space and utilizes instance-level prompts, which are generated based on latent vectors from the shared space. These designs make source-to-target transfer simple. We learn the shared latent space with all source tasks in a single training run. Also, the tuning on the target task only requires a single run. Given an instance from a target task, we use the instance embedding to identify a skill vector, learned from all source tasks, which is then transformed to soft prompts.

In summary, we design an instance-promptbased method by learning a shared skill latent space. We apply SHARPT to a diverse set of tasks covering diverse domains and task categories. We find that our method outperforms prior prompt-based methods and matches full-model-tuning across model scales.

# Method

Suppose we have a task with data T = {(x, y)} and a pre-trained LLM P θ . MODELTUNING updates θ to minimize L(θ) =log P θ (y|x)1 . PROMPTTUNING prepends to x a soft prompt, p ∈ R L×d , which has L vectors of size d. It then optimizes p by minimizing L(p) =log P θ (y|p, x).

SHARPT assumes there exists a discrete latent space, consisting of a set of skill vectors E = {e i ∈ R m } K i=1 with K vectors in total. The soft prompt is a simple transformation of one of the skill vectors e i , that is, p = f α (e i ). The transformation or prompt generator (f α ) is a light-weight MLP.

(1) where z l ∈ R d is the position embedding for the lth token (and randomly initialized in training) and W 1 ∈ R d×m , W 2 ∈ R d×d . Then we have the soft prompt p = {p l } L l=1 . Given x, we infer its skill vector by (1) embedding it via a frozen instance encoder (e.g., SimCSE BERT-base), which yields e (0)

x ; (2) querying E to find the nearest neighbour. Formally, that is, e (1)  x = e k , k = arg min

xe i 2 .

(2)

For a target task, our method is then trained with the following loss,

In target task training aforementioned, E is known and fixed. We next specify how to learn it from source tasks. Suppose we have N source tasks, {T (s) j } N j=1 . We simply mix all tasks together, s) and its embedding e

(0)

x . E is learned with the following loss,

where sg() is a stop gradient operator and e k is defined in Equation ( 2). The overall loss in source task learning is,

In summary, the forward pass for training on source and target tasks are exactly the same (also see Figure 1). The only difference is the loss function, Equation 5(source) versus Equation 3 (target).

# Experiments

High-to-Low Resource Transfer In this setting, the target tasks are low-resource tasks (less than 10K training examples), while the source tasks are high-resource tasks. It consists of 25 tasks in total. There are 15 source tasks (e.g., DocNLI, DROP) and 10 target asks (e.g., BoolQ, ColA). Please see Appendix A for the complete list or Table 1 for the target tasks. We keep the setting to be almost the same as a major experiment in Vu et al. (2022) for a fair comparison, with the exception that we exclude C4 from the source task since it is a much larger dataset than other tasks. Excluding C4 does not affect SPOT performance since it does not provide an optimal source prompt for any target task.

Transfer across Different Task Categories We here investigate the transferability from datasets in some task categories to datasets in other heldout task categories. Following Sanh et al. (2022), we assume datasets in each category measures a general NLP ability, and use the same taxonomy defined in Sanh et al. (2022). The source tasks include (1) QA tasks: ReCoRD, SQuAD, DROP, MultiRC, and RACE; (2) sentiment analysis tasks: Yelp-2 and SST-2; (3) a paraphrase detection task: QQP; (4) a semantic similarity task: CXC. The target tasks include (1) a sentence completion task: COPA; (2) NLI tasks: CB and RTE; (3) a coreference resolution tasks: WSC; (4) a word sense disambiguation task: WiC.

Training Details As in prior works (Raffel et al., 2020;Lester et al., 2021), all datasets are converted to a text-to-text format. All experiments are conducted with T5-base-LM-adapted as the backbone unless stated otherwise. We use a SimCSE (Gao et al., 2021) model (BERT-base) as the instance encoder. Since the instance encoder is always frozen, we can pre-compute the embeddings of all instances and only keep the embeddings. However, we find that memory and time saved in this approach is negligible2 . In source task training, the model (skill latent space and prompt generator) is simply tuned on the mixture of all source tasks for each setting. The model is tuned for 80K steps. In learning and testing on target tasks, we closely follow the procedure in Vu et al. (2022). The model is tuned for 100K on each target task. We save a checkpoint every 500 steps and report results on the checkpoint with the highest validation performance. The prompt generator generates 64 soft tokens. The following hyperparameters are shared in all target and source task training: learning rate (0.3), the number of warmup steps (4000), optimizer (Adam).

# Results

High-to-Low Resource Transfer The results are shown in Table 1. We first compare our method, SHARPT, to methods with comparable computeand parameter-efficiency, PROMPTTUNING and SPOT-Retrieval. Our method has a clear improvement over the two methods across most tasks and on the average performance. We next compare SHARPT with much more expensive methods, SPOT-Oracle and MODELTUNING. Note that SPOT-Oracle is significantly more expensive than our method since it tunes on each target task with each possible task prompt (e.g., it requires roughly 48 times more training time), and utilizes oracle labels. While being much more efficient, SHARPT matches or outperforms SPOT-Oracle. Also, our method performance is on par with the MODEL-TUNING performance which requires to tune the entire model. These results indicate SHARPT is an efficient and competitive approach.

Transfer across Different Task Categories The results are shown in  The improvement over SPOT methods is larger in this setting than in the high-to-low transfer setting. This might be because SPOT relies more on knowledge shared by tasks in the same category, while SHARPT learns a shared latent space across all source tasks and is more suitable to leverage knowledge shared across datasets of different categories.   Task Relations We investigate if the latent space captures source and target task relations to allow knowledge transfer. Each instance queries the latent space and selects one latent skill. We convert this selection to a one-hot vector and treat it as an instance encoding. A task representation is the average of instance encodings in the task. The cosine similarity between two task representations is computed as their relation. The relations between source and target tasks are visualized in Figure 3. It seems that more complicated source tasks such as QA and NLI tasks transfer more knowledge to target tasks via the skill latent space.

# Conclusion

We introduce SHARPT, which learns a shared latent space which captures a set of basis NLP capacities from a mixture of source tasks. Target instance queries this space to retrieve a skill vector, which then generates prompt tokens to condition a frozen LLM. Our approach outperforms prior soft prompt methods by a significant margin on a variety of tasks. Our method also matches full-model-tuning across model scales.

# Limitations

Although our method is much simpler than SPOT, PROMPTTUNING is still arguably the simplest method for adapting LLMs to downstream tasks. It would be a fruitful research direction to design transfer learning approaches that retain (or even improve) our method's performance and meanwhile further simplify our method, getting closer to the simplicity of PROMPTTUNING.

