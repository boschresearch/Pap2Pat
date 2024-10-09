# DESCRIPTION

## TECHNICAL FIELD

The subject matter described herein relates to the use of differential privacy techniques to avoid membership inference to avoid data leakage.

## BACKGROUND

Machine learning models are being increasingly adopted across different industries for a wide variety of applications to facilitate automated and intelligent classification and decision making.

## SUMMARY

In a first aspect, machine learning model data privacy can be maintained by training a machine learning model forming part of a data science process using data anonymized using each of two or more differential privacy mechanisms. Thereafter, it is determined, for each of the two or more differential privacy mechanisms, a level of accuracy and a level precision when evaluating data with known classifications. Subsequently, using the respective determined levels of precision and accuracy, a mitigation efficiency ratio is determined for each of the two or more differential privacy mechanisms. The differential privacy mechanism having a highest mitigation efficiency ratio is then incorporated into the data science process.

The mitigation efficiency ratio can be defined as φ and can be based on changes in accuracy and precisions of the machine learning model. With such a variation:

\(\phi = \frac{\frac{{{largest}\mspace{14mu} {change}\mspace{14mu} {accuracy}} - {{actual}\mspace{14mu} {change}\mspace{14mu} {accuracy}}}{{largest}\mspace{14mu} {change}\mspace{14mu} {accuracy}}}{\frac{{{largest}\mspace{14mu} {change}\mspace{14mu} {precision}} - {{actual}\mspace{14mu} {change}\mspace{14mu} {precision}}}{{largest}\mspace{14mu} {change}\mspace{14mu} {precision}}}\)

A first of the two or more differential privacy mechanisms can include local differential privacy (LDP). The LDP can be realized using local randomizers. The LDP can anonymize the training data prior to its being used to train the machine learning model.

A second of the two or more differential privacy mechanisms can include differential privacy stochastic descent gradient (DP-SGD). The DP-SGD can anonymize the training data while it is being used to train the machine learning model.

The data science process can include an automated sequence of stages including a business understanding stage, a privacy negotiation stage, a data understanding stage, a data preparation stage, a modeling stage, an evaluation stage, and a deployment stage. The differential privacy mechanism having a highest mitigation efficiency ratio can be automatically incorporated into the data science process.

Non-transitory computer program products (i.e., physically embodied computer program products) are also described that store instructions, which when executed by one or more data processors of one or more computing systems, cause at least one data processor to perform operations herein. Similarly, computer systems are also described that may include one or more data processors and memory coupled to the one or more data processors. The memory may temporarily or permanently store instructions that cause at least one processor to perform one or more of the operations described herein. In addition, methods can be implemented by one or more data processors either within a single computing system or distributed among two or more computing systems. Such computing systems can be connected and can exchange data and/or commands or other instructions or the like via one or more connections, including but not limited to a connection over a network (e.g., the Internet, a wireless wide area network, a local area network, a wide area network, a wired network, or the like), via a direct connection between one or more of the multiple computing systems, etc.

The subject matter described herein provides many technical advantages. For example, the current subject matter allows for the obfuscating of data used in training machine learning models to avoid issues associated with data leakage including membership inference.

The details of one or more variations of the subject matter described herein are set forth in the accompanying drawings and the description below. Other features and advantages of the subject matter described herein will be apparent from the description and drawings, and from the claims.

## DETAILED DESCRIPTION

The project leading to this application has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 825333.

The ability of machine learning prediction techniques to accurately fit complex functions has led to widespread adoption by data scientists. Neural networks (NN), in particular, have impacted various fields of application (e.g., image segmentation and classification, text analysis) because currently available computational resources allow for rapid training of such models. Typically, a neural network for discrimination among discrete classes is represented by a function ƒ: N→{0, . . . , k}, mapping from a multidimensional feature space to a finite set of labels (i.e., classes). As the true mapping function ƒ* is not known, ƒ must be derived by approximating the true mapping based on training data where features and corresponding classes are known. To improve the mapping ƒ predefined coefficients (weights) θ in the calculation of ƒ can be altered in order to minimize the difference between ƒ* and ƒ. To find the optimal choice for θ, numerical optimization, techniques (optimizers) can iteratively loop over the training data and update the values of θ accordingly. The steps of preparing the training data, designing ƒ learning θ, evaluating and deploying ƒ are orchestrated in various data science processes.

Yet, privacy concerns are emerging since NNs tend to leak information about the underlying training dataset which can be exploited by an adversary. Leveraging this information to identify individuals in the training data is known as membership inference (MI). Training anonymized neural networks with Differential Privacy (DP) as provided herein can mitigate MI. However, selecting among available DP mechanisms and interpreting the privacy guarantee (ϵ, δ) is challenging as DP can be enforced at multiple points in the data science process by different DP mechanisms. Furthermore, balancing the trade-off between utility for the analyst and privacy for the data owner is difficult due to the inherent complexity of the DP guarantee.

The current subject matter provides techniques that can identify appropriate DP mechanisms to protect against malicious actors including MI attacks. In particular, the current subject matter provides φ, a ratio expressing the efficiency of protection strategies in terms of privacy and utility. In addition, the current subject matter considers different steps at which DP may be enforced.

Differential privacy is a technique for the anonymization of data. DP perturbs the result of a query function ƒ(⋅) over a dataset  s.t. it is no longer possible to confidently determine whether ƒ(⋅) was evaluated on , or some neighboring dataset ′ differing in one individual. Mechanisms  fulfilling Definition 1 are differentially private and used for perturbation of ƒ(⋅).

Definition 1. A mechanism  gives (ϵ, δ)-Differential Privacy if for all , ′⊆ differing in at most one element, and all outputs ⊆Pr[()∈]≤eϵ·Pr[(′)∈]+δ.

ϵ-DP can be defined as as (ϵ, δ=0)-DP and the application of a mechanism  to a function ƒ(⋅) can be referred to as output perturbation. DP holds for all possible differences ƒ()−ƒ(′) by adapting to the global sensitivity of ƒ(⋅) per Definition 2.

Definition 2 (Global P2 Sensitivity). Let  and ′ be neighboring. The global P2 sensitivity of a function ƒ, denoted by Δƒ, can be defined as Δƒ=max, ′∥ƒ()−ƒ(D′)∥2.

For output perturbation, a differentially private stochastic gradient descent (DP-SGD) can be utilized which perturbs gradients with the Gaussian mechanism of Definition 3. DP-SGD bounds Δƒ by clipping norm C and adds noise to all gradient components.

Definition 3. Let ϵ∈(0, 1) be arbitrary. For

\({c^{2} > {2{\ln \left( \frac{{1.2}5}{\delta} \right)}}},\)

the Gaussian mechanism with parameter

\(\sigma \geq {c\frac{\Delta f}{\epsilon}\mspace{14mu} {is}\mspace{14mu} \left( {\epsilon,\delta} \right)}\)

-differentially private, adding noise scaled to (0,σ2).

For DP-SGD the moments accountant of Theorem 1 measures privacy decay. The accountant considers neural network update steps T, lot size L and training dataset size n. By sampling data per invocation with ratio q, ϵ can be further lowered.

Theorem 1. There exist constants c1 and c2 so that given the sampling probability

\(q = \frac{L}{n}\)

and the number of steps T, for any ϵ<c1q2T, the algorithm for deep learning with Differential Privacy is (ϵ, δ)-differentially private for any δ>0 if it is chosen as

\(\sigma \geq {c_{2}{\frac{q\sqrt{T{\ln \left( \frac{1}{\delta} \right)}}}{\epsilon}.}}\)

The replacement of an entry d∈ can be referred to as local differential privacy (LDP). In some variations, LDP can be realized by using local randomizers .

Definition 4 (Local Randomizer). An ϵ-local randomizer :→S is an ϵ-differentially private algorithm, where ϵ≥0, that takes a database of size n=1. That is, Pr[(v)=s]≤eϵ·Pr[(v′)=s]

for all possible inputs v, v′ϵ and all possible outcomes sϵ of . The probability can be taken over the coins of .

A series of  executions can compose a local algorithm  according to Definition 5. ϵ-local algorithms are ϵ-differentially private.

Definition 5 (Local Algorithm). An algorithm is ϵ-local if it accesses the database  via  with the following restriction: for all iϵ{1, . . . , |}, if 1(i), . . . , k(i) are the algorithms invocations of  on index i, where each j is an ϵj-local randomizer, then ϵl+ . . . +ϵk≤ϵ.

Randomized response can be used with LDP to achieve ϵ=ln(3) for a one-time collection of values from binary domains (e.g., {yes, no}) with two fair coins. That is, retention of the original value with probability ρ=0.5 and uniform sampling with probability 1−ρ:

\(\begin{matrix}
{\epsilon = {{\ln \left( \frac{\rho + {\left( {1 - \rho} \right) \cdot \rho}}{\left( {1 - \rho} \right)^{2}} \right)} = {{\ln \left( \frac{\Pr \left\lbrack {yes} \middle| {yes} \right\rbrack}{\Pr \left\lbrack {yes} \middle| {no} \right\rbrack} \right)}.}}} & (1)
\end{matrix}\)

As of Proposition 1 DP is immune to post-processing, i.e., the attempt to weaken DP by applying a function  to the output of .

Table 1 provides a brief overview of the notations used herein.

Proposition 1 (Post-Processing). Let :→ be a mechanism that is (ϵ, δ)-differentially private. Let :→ be an arbitrary randomized mapping. Then o:→ is (ϵ, δ)-differentially private.

MI attacks aim to determine the presence or absence of an individual in a dataset  with the help of statistics on the dataset. While there are numerous types of MI attacks, the current subject matter is directed to white-box MI where an adversary  has access to input and output, and general hyper-parameters, of a model. Within three steps, the MI attack exploits that a ML classifier tends to classify a record d from the model's training dataset targettrain with higher certainty p(x) to its true label y in comparison to a record d∉targettrain.

With reference to diagram 200 of FIG. 2, First, data owner  trains a ML model, target model, for some classification task with records from a dataset targettrain. After training  exposes the target model. Second,  trains copies of the target model, shadow models, on data statistically similar to targettrain. If  has white-box access to the target model, i.e., knows hyper-parameters and structure, the shadow models mimic the target model. Alternatively, in black-box access,  invokes shadow models by calling the same training routine as the DO (e.g., by using a Machine-Learning-as-a-Service provider, etc.) and is limited to model input and output. It applies that shadowtrain|=|shadowtest|Λshadowtrain∩shadowtrain=øΛ|shadow∩shadow|≥0 for any i≠j. After training, each shadow model predicts p(x), ∀d∉{shadowtrain, shadowtest}. As  has full control over shadowtrain and shadowtest, each shadow model's output (p(x), y) is attached with label “in” if the corresponding d∉shadowtrain. Otherwise, the label is “out”. The resulting triples (p(x), y, in/out) are used by  to train the attack model, i.e., attacktrain. Third, a binary classifier, attack model, is trained by  to exploit the imbalance between predictions on d∉targettrain and d∈targettrain. One attack model can be trained per target variable Yk to map p(x), to the indicator “in” or “out”. The attack model is tested on tuples (p(x), ŷ) outputted by the trained target model ∀d∉targettrain, which simulates the critical case where  tests membership for all training instances.

As mentioned above, the current subject matter provides enhanced techniques for providing and automating guidance for data scientists in building differentially private neural networks and mitigating MI along a data science (DS) process. FIG. 1 is a diagram illustrating a data science process in which the data owner  can perform certain activities including:


- - Engaging in business understanding, and deriving data analysis
    approaches (**105**).
  - Striving for data understanding and identifying data quality issues
    (**115**).
  - Engaging in data preparation to construct inputs for data analysis
    (**120**).
  - Modeling (i.e., training) a set of data analysis algorithms such as
    NNs (**130**).
  - Evaluating data analysis algorithms with regard to accuracy
    (**145**).
  - Deploying the best model for practical use and presenting the
    results (**15**).

In addition, various other operations can take place within the process flow 100 of FIG. 1 to integrate data privacy into a data science process. When using DP in the DS process, utility and privacy are of particular interest. The current subject matter assesses utility in relation to changes in target model test accuracy under DP, which is denoted as  test accuracy herein. In particular, privacy can be evaluated based on the stage at which DP is enforced in the DS process how such DP affects 's MI attack. This endeavor can also focus on privacy questions such as “How many records predicted as in are truly contained in the training dataset?” (i.e., precision). Effective mitigation reduces 's MI precision without losing a significant amount of 's test accuracy.

First, independent of the specific DP mechanism for anonymization of data, an acceptable MI precision can be defined after business understanding 110, which can be referred to herein as privacy negotiation 110. Second,  can either enforce anonymization with LDP after data preparation (125) or anonymization during model training with DP-SGD (135). Either approach is then automatically evaluated with regard to MI precision for a vector of DP privacy guarantees (ϵ, δ). Meaning, that multiple instances of the process operations 120-140 can exist (per LDP and DP-SGD (ϵ, δ) parameter). Finally, after the DP enforcements, a new operation 140 can be provided that captures the input from the process instances 120-140 for interpreting privacy and utility of trained models before actual evaluation and deployment to production. This privacy vs. utility operation 140 can be used to identify which privacy parameters (∉, δ) efficiently address MI precision while maintaining high model accuracy. If the privacy parameters necessary for reaching the desired MI precision are inefficient, then the process can return to the privacy negotiation operation 110.

MI mitigation efficiency can be modeled as the relative difference between 's change in test accuracy to the change in 's MI precision. Let precorig be 's original MI precision and accorig be 's original test accuracy, and let prec(∉,δ) be 's MI precision and acc(∉,δ) be 's test accuracy after mitigation with DP. Also, let accbase be the minimal 's test accuracy and precbase be the minimal 's MI precision (e.g., random guessing). Normalizing yields mitigation efficiency φ:

\(\begin{matrix}
{\phi = {\frac{\left( \frac{\begin{matrix}
{{{largest}\mspace{14mu} {change}\mspace{14mu} {accuracy}} -} \\
{{actual}\mspace{14mu} {change}\mspace{14mu} {accuracy}}
\end{matrix}}{{largest}\mspace{14mu} {change}\mspace{14mu} {accuracy}} \right)}{\left( \frac{\begin{matrix}
{{{largest}\mspace{14mu} {change}\mspace{14mu} {precision}} -} \\
{{actual}\mspace{14mu} {change}\mspace{14mu} {precision}}
\end{matrix}}{{largest}\mspace{14mu} {change}\mspace{14mu} {precision}} \right)} = \frac{\frac{\left( {{acc}_{orig} - {acc}_{base}} \right) - \left( {{acc}_{orig} - {{acc}\left( {\epsilon,\delta} \right)}} \right)}{{acc}_{orig} - {acc}_{base}}}{\frac{\left( {{prec}_{orig} - {prec}_{base}} \right) - \left( {{prec}_{orig} - {{prec}\left( {\epsilon,\delta} \right)}} \right)}{{prec}_{orig} - {prec}_{base}}}}} & (2)
\end{matrix}\)

(2) requires (largest change−actual change)≠0⊇ and largest change≠0. If the previous is not given, the question of mitigation efficiency does not apply since 's test accuracy or 's MI precision is foregone. From now on we assume that (φ is well defined. φ reaches its maximum when the change in accuracy is close to 0 (i.e., numerator≈1) and the change in precision is close to the maximum (i.e., denominator,≈0). Desirable φ>1 state that there is an efficient trade between privacy and utility, i.e., that the relative losses of exceed 's. This work analyzes the privacy guarantee

\({\left( {\epsilon,{\delta = \frac{1}{n}}} \right)\mspace{14mu} {for}\mspace{14mu} {DP}\text{-}{SGD}},\)

and the privacy guarantee (ϵ, δ=0) for LDP. Below is an analysis of φ along customer transaction matrices for association rule learning. Due to the low domain, customer transaction matrices are suited for the application of LDP during the data preparation phase of the DS process and DP-SGD during the model training phase.

For association rule learning tasks where potentially high dimensional datasets (e.g., customer shopping carts representing purchases) are transformed to small domains with few distinct values LDP is an alternative to DP-SGD, and a comparison of privacy and utility between the two means is necessary. Therefore, LDP and DP-SGD can be evaluated and compared with regard to purchase data where the DS process is as follows: a model (artificial neural network) is provided a set of historical data labeled with customer groups. After training the model assigns new shopping carts to a customer group. To achieve DP for the , the scheme introduced in diagram 200 of FIG. 2 can be followed to evaluate increasing privacy guarantees ϵ∉{8.41, 3.72, 2.39, 1.77, 0.87} and δ=1/(n=10,000). To ensure better comparison to the later LDP experiments, in one example, the number of epochs can be fixed at 200.

As used herein, the unperturbed MI attack can be referred to as original and can provide target model train and test accuracy and MI precision in diagram 300A of FIG. 3 and diagram 400A of FIG. 4. Diagram 300A of FIG. 3 presents a foundation for  utility analysis by stating target model train and test accuracy over

\(\left( {\epsilon,{\delta = \frac{1}{10\text{,}000}}} \right).\)

While learning problems C (e.g., ‘target models discriminate between C∉{10,20,50,100} customer groups’, etc.) suffer from a decreasing test error, the decrease is close to linear for relatively easier learning problems of C∉{10, 20}. For complex learning C∉{50,100} the decrease is strong already at small perturbation and only sublinear for stronger E.

Chart 400A of FIG. 4 illustrates the changes in MI precision over privacy guarantees

\(\left( {\epsilon,{\delta = \frac{1}{10\text{,}000}}} \right).\)

Privacy comes indeed at a heavy cost in this deployment: DP-SGD weakens the  while significantly hurting the  test accuracy. In summary, it is observed that DP-SGD has to be calibrated carefully to preserve 's test accuracy (e.g., for C=50).

In the LDP setup train is protected by the application of randomized response (cf. Equation (1)) to every position in all feature vectors. Randomized response thus serves as a local randomizer  (cf. Definition 4) and we denote the series of repeated executions  (d∉train) as  (train). The target model is trained with a standard optimizer (e.g., SGD) on  (targettrain)⊂ (train). Perturbation using LDP affects  since the direct application of the MI attack against a model trained on the perturbed dataset  (targettrain) should solely provide A with information about the underlying LDP data due to the post-processing proposition (cf. Proposition 1). The privacy in our experiment is evaluated by 's MI precision on (i)  (targettrain), and (ii) original targettrain.

Again, the first evaluation aspect is 's test accuracy. A main difference to address for this analysis is, that in contrast to the DP-SGD parameters (ϵ, δ) for LDP, ϵi resulting from the execution of randomized response as  per attribute can be considered. The privacy after repeated executions of  is measured by a local algorithm LA (cf. Definition 5), yielding ϵ=Σi=1600ϵi per d∉(targettrain). Evaluation can be provided for diverse ϵi ∉{8, 5, 3, 1, 0.1}. These ϵi cover a wide range of retention probabilities p, i.e., the probability of retaining the true value (cf. Equation 1), from low ρϵ=0.1θ0.31 to high ρϵθ0.98. FIG. 300B of FIG. 3 indicates that especially simple classification tasks (e.g., C∉{10, 20}), where n is much larger than the dimensionality l of the training data, 's test accuracy seems relatively robust to noise.

Again, for privacy, the protection of 's training data is evaluated by 's MI attack precision.

For MI against (targettrain) diagram 400B of FIG. 4 demonstrates that the drop in MI precision is larger than the drop in target model accuracy (cf. diagram 300B of FIG. 3) caused by LDP. The reasons for this drop are located in the lower target model softmax confidences for classifications when LDP is applied. This decrease in confidence leads to fewer predictions overcoming the threshold exploited by , and thus, MI precision drops. For the more complex classification task C=50, a drop in MI precision as the train-test-gap closes is observed. It can be assumed that Dtrain becomes similar to Dtest due to LDP and the attacker categorizes more data entries as “in”. However, the evaluation before only indicates 's MI risk with regard to  (targettrain).

A more accurate expression of risk should address records of the original targettrain. When providing original records d∉targettrain to 's trained attack model as test records, instead of LDP training data, the intuition is that A should not be able to achieve meaningful precision on this data due to the protection of LDP. Indeed this clearly holds for C∉{10, 20} in diagram 400B of FIG. 4. Thus, the actual effect of LDP on MI is even stronger.

When comparing to DP-SGD, a striking difference is that the reason for the decrease of 's MI precision in LDP is due to the noisy (Dtargettrain), rather than the noisy gradients. Thus, the training dataset itself already enjoys DP protection and the records detected under MI do not represent original data anymore. The evaluation within this section has shown that LDP affects 's MI precision, and that the protection for original data can be even higher. The difference between LDP and DP-SGD privacy guarantees ϵ and (ϵ, δ) also suggests that the privacy guarantee should not be directly compared and a discussion is required.

The difference in utility and privacy between LDP and DP-SGD is also observable with regard to φ, where 's test accuracy is weakened more than 's MI precision when φ<1 for a given (ϵ, δ). FIG. 500A illustrates that for DP-SGD our experiments did not yield φ>1 for any (ϵ, δ). This supports our first impression that DP-SGD impacts 's test accuracy stronger than the MI precision. In contrast, chart 500B of FIG. 5 presents that when LDP is utilized for some ϵ there is φ>1. Counterintuitively, higher φ values are observed for small ∉ for C∉{10, 20} due to an increased test accuracy. Here, LDP achieves a regularization effect. In contrast, increased target model test accuracies for DP-SGD on the same data were not observed. Finally, diagram 500C of FIG. 5 points out that for C∉{10, 20} and ϵ=0.1 LDP can lead to even stronger protections for targettrain. MI precision close to φ leading to large (o values is observed. However, to achieve this LDP has to be calibrated carefully. The difference in values for φ in diagram 500B of FIG. 5 is mostly due to a different baseline line MI precision. Instead of performing random guessing, leading to a baseline MI precision of 0.5, 's attack model will label records “in” only when they are similar to the LDP data that has been used for training of the attack model. In the extreme case where LDP records are very different to the original records MI precision close to 0 was observed.

Furthermore, diagram 500 of FIG. 5 illustrates that a sole comparison of privacy parameters (ϵ, δ) is not sufficient to evaluate potential privacy risks, e.g., due to MI attacks. While utilizing larger privacy guarantees ∉, LDP is able to achieve better φ, i.e., a better ratio between privacy and model utility. This stresses 's need for key figures like φ to support the decision making process Differential Privacy protects training data by anonymization and allows quantification of the resulting privacy loss. However, a direct comparison of the DP guarantees (ϵ, δ) falls short of measuring factual privacy risks under sophisticated attacks like MI. Furthermore, the parameters (ϵ, δ) do not have the same meaning between different DP mechanisms. Extending the DS process with steps for defining acceptable MI risk, enforcing DP and interpreting the resulting efficiency of various (ϵ, δ) parameters with φ eases this constraint and gives data scientists guidance in their decision making.

As can be appreciated above, the data science process of FIG. 1 covers two machine learning development cases that are relevant for many model providers and data scientists. First, the process of FIG. 1 allows data scientists to design and interpret machine learning models that protect the training data and to communicate risks towards third-parties who are participating in the training data. These trained models can then be deployed to third parties, either as part of an application or as a prediction service, while the trade-off between privacy and utility due to the enforced mechanism is quantified by φ. Second, it enables third parties to train models that are shipped to them and interpret the respective risk that their training data is facing under MI.

FIG. 6 is a process flow diagram 600 illustrating a method for maintaining machine learning model data privacy in which, at 610, a machine learning model forming part of a data science process is trained using data anonymized using each of two or more differential privacy mechanisms. Thereafter, at 620, a level of accuracy and a level of precision are determined for each of the two or more differential privacy mechanisms when evaluating data with known classifications. It can later be determined, at 630, using the respective determined levels of precision and accuracy, a mitigation efficiency ratio for each of the two or more differential privacy mechanisms. The differential privacy mechanism having the highest mitigation efficiency can, at 640, be incorporated into the data science process along with its parameters.

FIG. 7 is a diagram 700 illustrating a sample computing device architecture for implementing various aspects described herein. A bus 704 can serve as the information highway interconnecting the other illustrated components of the hardware. A processing system 708 labeled CPU (central processing unit) (e.g., one or more computer processors/data processors at a given computer or at multiple computers), can perform calculations and logic operations required to execute a program. A non-transitory processor-readable storage medium, such as read only memory (ROM) 712 and random access memory (RAM) 716, can be in communication with the processing system 708 and can include one or more programming instructions for the operations specified here. Optionally, program instructions can be stored on a non-transitory computer-readable storage medium such as a magnetic disk, optical disk, recordable memory device, flash memory, or other physical storage medium.

In one example, a disk controller 748 can interface with one or more optional disk drives to the system bus 704. These disk drives can be external or internal floppy disk drives such as 760, external or internal CD-ROM, CD-R, CD-RW or DVD, or solid state drives such as 752, or external or internal hard drives 756. As indicated previously, these various disk drives 752, 756, 760 and disk controllers are optional devices. The system bus 704 can also include at least one communication port 720 to allow for communication with external devices either physically connected to the computing system or available externally through a wired or wireless network. In some cases, the at least one communication port 720 includes or otherwise comprises a network interface.

To provide for interaction with a user, the subject matter described herein can be implemented on a computing device having a display device 740 (e.g., a CRT (cathode ray tube) or LCD (liquid crystal display) monitor) for displaying information obtained from the bus 704 via a display interface 714 to the user and an input device 732 such as keyboard and/or a pointing device (e.g., a mouse or a trackball) and/or a touchscreen by which the user can provide input to the computer. Other kinds of input devices 732 can be used to provide for interaction with a user as well; for example, feedback provided to the user can be any form of sensory feedback (e.g., visual feedback, auditory feedback by way of a microphone 736, or tactile feedback); and input from the user can be received in any form, including acoustic, speech, or tactile input. The input device 732 and the microphone 736 can be coupled to and convey information via the bus 704 by way of an input device interface 728. Other computing devices, such as dedicated servers, can omit one or more of the display 740 and display interface 714, the input device 732, the microphone 736, and input device interface 728.

One or more aspects or features of the subject matter described herein can be realized in digital electronic circuitry, integrated circuitry, specially designed application specific integrated circuits (ASICs), field programmable gate arrays (FPGAs) computer hardware, firmware, software, and/or combinations thereof. These various aspects or features can include implementation in one or more computer programs that are executable and/or interpretable on a programmable system including at least one programmable processor, which can be special or general purpose, coupled to receive data and instructions from, and to transmit data and instructions to, a storage system, at least one input device, and at least one output device. The programmable system or computing system may include clients and servers. A client and server are generally remote from each other and typically interact through a communication network. The relationship of client and server arises by virtue of computer programs running on the respective computers and having a client-server relationship to each other.

These computer programs, which can also be referred to as programs, software, software applications, applications, components, or code, include machine instructions for a programmable processor, and can be implemented in a high-level procedural language, an object-oriented programming language, a functional programming language, a logical programming language, and/or in assembly/machine language. As used herein, the term “machine-readable medium” refers to any computer program product, apparatus and/or device, such as for example magnetic discs, optical disks, memory, and Programmable Logic Devices (PLDs), used to provide machine instructions and/or data to a programmable processor, including a machine-readable medium that receives machine instructions as a machine-readable signal. The term “machine-readable signal” refers to any signal used to provide machine instructions and/or data to a programmable processor. The machine-readable medium can store such machine instructions non-transitorily, such as for example as would a non-transient solid-state memory or a magnetic hard drive or any equivalent storage medium. The machine-readable medium can alternatively or additionally store such machine instructions in a transient manner, such as for example as would a processor cache or other random access memory associated with one or more physical processor cores.

To provide for interaction with a user, the subject matter described herein may be implemented on a computer having a display device (e.g., a CRT (cathode ray tube) or LCD (liquid crystal display) monitor) for displaying information to the user and a keyboard and a pointing device (e.g., a mouse or a trackball) and/or a touch screen by which the user may provide input to the computer. Other kinds of devices may be used to provide for interaction with a user as well; for example, feedback provided to the user may be any form of sensory feedback (e.g., visual feedback, auditory feedback, or tactile feedback); and input from the user may be received in any form, including acoustic, speech, or tactile input.

In the descriptions above and in the claims, phrases such as “at least one of” or “one or more of” may occur followed by a conjunctive list of elements or features. The term “and/or” may also occur in a list of two or more elements or features. Unless otherwise implicitly or explicitly contradicted by the context in which it is used, such a phrase is intended to mean any of the listed elements or features individually or any of the recited elements or features in combination with any of the other recited elements or features. For example, the phrases “at least one of A and B;” “one or more of A and B;” and “A and/or B” are each intended to mean “A alone, B alone, or A and B together.” A similar interpretation is also intended for lists including three or more items. For example, the phrases “at least one of A, B, and C;” “one or more of A, B, and C;” and “A, B, and/or C” are each intended to mean “A alone, B alone, C alone, A and B together, A and C together, B and C together, or A and B and C together.” In addition, use of the term “based on,” above and in the claims is intended to mean, “based at least in part on,” such that an unrecited feature or element is also permissible.

The subject matter described herein can be embodied in systems, apparatus, methods, and/or articles depending on the desired configuration. The implementations set forth in the foregoing description do not represent all implementations consistent with the subject matter described herein. Instead, they are merely some examples consistent with aspects related to the described subject matter. Although a few variations have been described in detail above, other modifications or additions are possible. In particular, further features and/or variations can be provided in addition to those set forth herein. For example, the implementations described above can be directed to various combinations and subcombinations of the disclosed features and/or combinations and subcombinations of several further features disclosed above. In addition, the logic flows depicted in the accompanying figures and/or described herein do not necessarily require the particular order shown, or sequential order, to achieve desirable results. Other implementations may be within the scope of the following claims.

