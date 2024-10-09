# DESCRIPTION

## FIELD OF THE INVENTION

Assessment of pulmonary function in coronavirus patients includes use of a computer aided diagnostic (CAD) system to assess pulmonary function and risk of mortality in patents with coronavirus disease 2019 (COVID-19). The CAD system processes chest X-ray data from a patient, extracts imaging markers, and grades disease severity based at least in part on the extracted imaging markers, thereby distinguishing between higher risk and lower risk patients.

## BACKGROUND OF THE INVENTION

COVID-19 is caused by a novel RNA virus belonging to the Coronaviridae family. Coronaviridae is a family of nonsegmented, enveloped, positive-sense, single-stranded ribonucleic acid viruses. Six species of coronavirus had previously been identified as pathogenic in humans: four of these cause mild respiratory illnesses, whereas the other two species, severe acute respiratory syndrome coronavirus (SARS-CoV) and Middle East respiratory syndrome coronavirus (MERS-CoV), have led to epidemics with significant rates of mortality.

The clinical diagnosis of COVID-19 depends on different symptoms including fever (98% of cases), dry cough (75%), fatigue (45%), muscle aches (45%), difficulty breathing (55%), and acute respiratory distress syndrome (ARDS) (20%). Severe cases may progress to multiorgan dysfunction and even death (2.5%). The disease may be classified as (i) mild type: moderate clinical symptoms with normal chest X-ray; (ii) typical type: fever, respiratory, and other clinical findings indicating signs of pneumonia; (iii) severe type: respiratory distress signs (respiratory rate 30 breaths per minute and/or blood oxygen saturation of less than 93%); or (iv) critical type: dysfunction of respiration necessitating mechanical ventilation, shock, and organ damage requiring monitoring and treatment from an intensive care unit (ICU).

Due to the wide variations in clinical presentation and progression rate for COVID-19, laboratory confirmation of SARSCoV-2 infection is essential to initiate appropriate early treatment and to prevent further spread of the disease. The current reference standard for this purpose is real-time reverse transcription polymerase chain reaction (PCR) of viral RNA. The PCR test, according to current guidelines, is run on samples from nasopharyngeal and/or throat swabs. While PCR is the gold standard in diagnosing patients with COVID-19 infection, the sensitivity of a single PCR is suboptimal and depends on the timing of the test, sampling sites and sampling techniques.

Chest radiography is helpful for first-line evaluation of patients with a high pre-test probability of overt COVID-19 pneumonia, clinical follow up, and for the evaluation of potential complications. Chest radiography can detect areas of ground glass density, also observed on chest computed tomography (CT), which may often have a correlation with the severity of the disease, and may be intermixed with reticular pattern.

Based on recent clinical research, COVID-19 radiological forms are variable in severity using plain radiography or CT, ranging from a normal chest (albeit rarely), to patchy involvement of one or both lungs in mild or moderate cases, to diffuse infiltration (white lung) in severe cases. This is an important issue, as mild or moderate cases can be managed by medical treatment or non-invasive ventilation, while severe cases with bilateral lung infection urgently need mechanical ventilation to support respiration as patients develop ARDS. Given the paucity of mechanical ventilation units, patient selection for ventilation plays a crucial role in saving lives.

There are few preliminary studies and case reports discussing the role of artificial intelligence (AI) on plain radiography and CT for early diagnosis of patients with COVID-19. AI can be used in conjunction with radiologists to improve the results of detection of COVID-19. AI can be a powerful aid in delineating and quantifying lesions in X-ray images and in tracking longitudinal changes between exams, which is crucial for precision medicine. In essence, AI is another means of analyzing data that clinicians can draw on to inform their judgment in issues of triage, diagnosis (in combination with PCR tests and epidemiological risk), prognosis, and selection between therapeutic alternatives in patients exhibiting COVID-19 symptoms. Plain radiography involves a low radiation dose compared to CT and is better suited for routine monitoring and follow up as compared to a CT scan. AI may be capable of detecting subtle changes in the lung visible on either chest X-ray or CT, and can improve efficiency by decreasing the amount of time to return test results. This is necessary for screening the general population during the current COVID-19 pandemic and in the epicenters of any future outbreaks. Computer assisted detection alleviates the burden on radiologists and clinicians and facilitates rapid triage. Also, AI can be used for the differentiation of previous lung injury unrelated to COVID-19 from advanced lung dysfunction due to COVID-19, and assist in patient selection for ventilation. However, CAD systems for assessing lung function in COVID-19 are limited in the literature.

X-ray images may be indicative of healthy lungs or evidence of pneumonia (bacterial or viral). Combined with prior information regarding the likelihood the patient has been exposed to the virus, an automatic diagnosis of viral pneumonia has a high true positive rate for detection of COVID-19. Currently, the primary challenge is to apply different AI-based approaches to determine the severity of chest infection in COVID-19 patients given that X-ray images vary enormously in image quality due to the wide range of X-ray machines in use across the world.

## SUMMARY

To address the identified challenges, Applicant has developed a novel CAD system using AI and machine learning techniques to assist physicians by providing an objective metric that can differentiate severe cases of COVID-19 from mild/moderate non-severe cases. The CAD system addresses the challenge of X-ray image quality by generating a diagnosis at least in part on extracted X-ray image markers that are invariant under rotation, scaling, and translation, and that capture both local and global features of the lung.

It will be appreciated that the various systems and methods described in this summary section, as well as elsewhere in this application, can be expressed as a large number of different combinations and subcombinations. All such useful, novel, and inventive combinations and subcombinations are contemplated herein, it being recognized that the explicit expression of each of these combinations is unnecessary.

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

FIG. 1 illustrates an exemplary CAD system for assessment of pulmonary function in patients with Coronaviridae infection and the method for assessing pulmonary function performed thereby. The method 10 broadly includes three sections: (i) preprocessing steps 12 to improve contrast of medical image data, such as an X-ray image, that includes image data of at least one lung and to identify the region of interest in order to enhance diagnostic accuracy of subsequent steps; (ii) modeling steps 14 model the appearance of infected unhealthy chest tissue using a new Markov-Gibbs random field (MGRF) constructed to be invariant under rotation, translation, and change of scale; and (iii) determining steps 16 performed by a neural network (NN)-based fusion and diagnostic system to determine whether the severity of lung infection is at a first state, e.g., non-severe or low severity, or a second state, e.g., severe or high severity. In other embodiments, the NN-based fusion and diagnostic system may determine whether the severity of lung infection is one of a plurality of states, e.g., mild, moderate, or severe. The CAD system receives as input for the method 10 medial image data 18, such as a thoracic X-ray image of a subject patient (FIG. 2A), which includes image data of the lung region.

### Data Preprocessing

In this exemplary embodiment, the preprocessing steps 12 include three sequential steps to improve the accuracy of the methodology. In the first preprocessing step 20, the medical image is segmented to identify the lung region (FIG. 2B). This may be performed manually using computer-based methods as described in Soliman, A., Khalifa, F., Elnakib, A., Abou EI-Ghar, M., Dunlap, N., Wang, B., Gimel'farb, G., Keynton, R. and El-Baz, A., 2016. Accurate lungs segmentation on CT chest images by adaptive appearance-guided shape modeling. IEEE transactions on medical imaging, 36(1), pp. 263-276, incorporated herein by reference, or other computer-based methods. In the second preprocessing step 22, regional dynamic histogram equalization (RDHE) is utilized to reduce the effect of certain kinds of noise and enhance lung tissue contrast. This approach divides the image into blocks x rows high by y columns wide. Then, dynamic histogram equalization is applied within each block to adaptively enhance the contrast. Therefore, the image histogram is remapped by block, and pixel values are adjusted relative to the other pixels in their x×y neighborhood. The contrast-enhanced X-ray image resulting from the RDHE approach is illustrated in FIG. 2C.

The third preprocessing step 24 is to identify and mask off the healthy lung tissues from the infected tissues. This step narrows the search space to focus only on the abnormal tissues and serves to increase the diagnostic accuracy of the CAD system. This third step is elaborated in El-Baz, A., Gimel'farb, G. & Suri, J. Stochastic Modeling for Medical Image Analysis (Boca Raton: CRC Press, 2016), incorporated herein by reference, and considers both the spatial interaction between nearby image pixels and the intensity distribution of those pixels within the lung region of interest. The instant invention follows the conventional description of the MGRF model in terms of independent signals (images) and interdependent region labels (segmentations) as described in the published article, but focuses on more accurate model identification. Each image segment corresponds to a single dominant mode of the empirical distribution (i.e. histogram) of gray levels. To identify the dominant modes, each image histogram is considered to be sampled from a linear combination of discrete Gaussians (LCDG) distribution. An initial LCDG model is fit to the empirical distribution using a modified expectation-maximization (EM) algorithm. Free parameters of the LCDG to be optimized are the number of discrete Gaussian components and their respective weights (positive and negative), shape, and scale parameters. Then, the initial LCDG-based segmentation is iteratively refined using the MGRF model with its analytically estimated potentials. FIG. 2D displays the extracted pathological tissues using the algorithm disclosed herein.

### Rotating, Scale, and Translation Invariant MGRF Model

Moving on to the modeling steps 14, the proposed MGRF model was constructed such that that the medical image need not be aligned with any particular frame of reference in order to use it to grade the severity of lung infection as first state, e.g., non-severe or low severity, or second state, e.g., severe or high severity. To construct the appearance of the infected lung regions, the X-ray images are considered as samples from a piecewise stationary MGRF with a central-symmetric system of pixel-pixel interactions. Let nv denote a set of central-symmetric pixel neighborhoods indexed by v∈{1, . . . ,N}. Each nv is a set of coordinate offsets (ξ,η) specified by a semi-open interval of interpixel distances (dv,min,dv,max) such that the nv-neighborhood of pixel (x,y) comprises all pixels (x′,y′) such that dv,min<√{square root over ((x−x′)2+(−y′)2)}≤dv,max. A neighborhood system corresponding to dv,min=v−½ and dv,max=v+½, v ∈{1,2,3}, is illustrated in FIG. 3. Associated with the neighborhood system is a set of N+1 Gibbs potential functions of gray value and gray value co-occurrences V0: Q→ and Vv: Q×Q→, v∈{1, . . . ,N}, where Q is the range of pixel gray levels, e.g. Q={0, . . . , 255} in the case of 8-bit images.

For a given image/label map pair (gt, mt) from the training set S, t∈{1, . . . ,T}, let Rt={(x,y)|mt(x,y)=ob} denote the subset of the pixel lattice supporting the infected lung region. Denote the set of nv-neighboring pixels restricted to Rt by

Cv,t={(x,y,x′,y′)|(x,y)∈RtΛ(x′,y′)∈RtΛ(x−x′,y−y′)∈nv}.

Finally, let f0,t and fv,t, v∈{1, . . . ,N} denote empirical probability distributions (i.e., relative frequency histograms) of gray values and gray value co-occurrences in the training infected region from the X-ray image gt,

f0,t(q)=|Rt|−1|{(x,y)∈Rt|gt(x,y)=q}|;   (1)

fv,t(q,q′)=|Cv,t|−1|{(x,y,x′,y′)∈Cv,t|gt(x,y)=qΛgt(x′,y′)=q′}|.   (2)

The joint probability of object pixels in image gt according to the MGRF model is given by the Gibbs distribution

\(\begin{matrix}
 & (3)
\end{matrix}\)
\(\begin{matrix}
\begin{matrix}
{P_{t} = {Z_{t}^{- 1}{\exp\left( {\sum\limits_{{({x,y})} \in R_{t}}\left( {{V_{0}\left( {g_{t}\left( {x,y} \right)} \right)} + {\sum\limits_{v = 1}^{N}{\sum\limits_{{({\xi,\eta})} \in \eta_{v}}{V_{v}\left( {{g_{t}\left( {x,y} \right)},{g_{t}\left( {{x + \xi},{y + \eta}} \right)}} \right)}}}} \right)} \right)}}} \\
{{= {Z_{t}^{- 1}{\exp\left( {{❘R_{t}❘}\left( {{V_{0,t}^{T}F_{0,t}} + {\sum\limits_{v = 1}^{N}{\rho_{v,t}V_{v,t}^{T}F_{v,t}}}} \right)} \right)}}},}
\end{matrix} & 
\end{matrix}\)

where ρv,t=|Cv,t|/|Rt| is an average cardinality of nv over the sublattice Rt.

Assuming lungs having the same pathology exhibit similar morphology in X-ray images, the previous expressions are approximated by their averages over the training set S: |Rt|≈Rob and |Cv,t|≈Cv,ob. Here

\(R_{ob} = {{\frac{1}{T}{\sum_{i = 1}^{T}{{❘R_{t}❘}{and}C_{v,{ob}}}}} = {\frac{1}{T}{\sum_{i = 1}^{T}{{❘C_{v,t}❘}.}}}}\)

Under the assumption that the observations in S are statistically independent (e.g., each X-ray is taken from a different patient), the expression for joint probability of object pixels may be likewise simplified:

\(P_{S} = {\frac{1}{Z}{{\exp\left( {{TR}_{ob}\left( {{V_{0}^{T}F_{0}} + {\sum\limits_{v = 1}^{N}{\rho_{v}V_{v}^{T}F_{v}}}} \right)} \right)}.}}\)

Here, ρv=Cv,ob/Rob, and the probability vectors Fpix,ob and Fv,ob are the averages of the relative frequency histograms and normalized gray level co-occurrence matrices, respectively, over all objects in the training set. The problem of zero empirical probabilities, which can arise when a relatively small volume of the training data is available to identify the MGRF model, is dealt with using pseudocounts. Then Equations 1 and 2 are modified as follows:

\(\begin{matrix}
{{f_{0,t}(q)} = \frac{{❘\left\{ {{{\left( {x,y} \right) \in R_{t}}❘{g_{t}\left( {x,y} \right)}} = q} \right\} ❘} + \varepsilon}{{❘R_{t}❘} + {Q\varepsilon}}} & (4)
\end{matrix}\)
\(\begin{matrix}
{{f_{v,t}\left( {q,q^{\prime}} \right)} = {\frac{{❘\left\{ {{{\left( {x,y,x^{\prime},y^{\prime}} \right) \in C_{v,t}}❘{g_{t}\left( {x,y} \right)}} = {{q \land {g_{t}\left( {x^{\prime},y^{\prime}} \right)}} = q^{\prime}}} \right\} ❘} + \varepsilon}{{❘C_{v,t}❘} + {Q^{2}\varepsilon}}.}} & (5)
\end{matrix}\)

The Bayesian quadratic loss estimate suggests using the offset ε=1, while a more conservative approach suggests using ε=1/Q in Equation 4 and ε=1/Q2 in Equation 5.

Using the same analytical approach as in Gimel'farb, G. L. Image Textures and Gibbs Random Fields (Springer Netherlands, 1999), the Gibbs potential functions are approximated using the centered, training-set average, normalized histograms and co-occurrence matrices:

\(\begin{matrix}
{{{{V_{0}(q)} = \left( {{f_{0}(q)} - \frac{1}{Q}} \right)};}{{V_{v}\left( {q,q^{\prime}} \right)} = {\left( {{f_{v}\left( {q,q^{\prime}} \right)} - \frac{1}{Q^{2}}} \right).}}} & (6)
\end{matrix}\)

Using the above estimated potentials, we can calculate the Gibbs energy of the infected lung region b in an X-ray image g as follows:

\(\begin{matrix}
{{E\left( {g,b} \right)} = {{V_{0}^{T}{F_{0}\left( {g,b} \right)}} + {\sum\limits_{v \in N^{\prime}}{V_{v}^{T}{{F_{v}\left( {g,b} \right)}.}}}}} & (7)
\end{matrix}\)

Here, N′ is a selected top-rank index subset of the neighborhoods, and the empirical probability distributions Fo and Fv are calculated over the object pixels b of g.

To summarize, the training approach is as follows: (1) read all infected regions from the training data having class “severe” lung infection; (2) calculate the co-occurrence of the image signal at a plurality of different radii (in this embodiment, v1, v2, and v3); (3) normalize the co-occurrence frequency (fpix,ob(q)); (4) estimate the Gibbs potential (Vpix,ob(q)) by using Equation 6 for each radii; (5) use Equation 7 to calculate the Gibbs energy (E(g,b)) for the training subjects. Gibbs energy calculated according to Equation 7 is a statistical estimator, i.e., a function of the observed data. In FIG. 1, boxes 26, 28, and 30 represent the calculated Gibbs energy at v1, v2, and v3, respectively. CDF is used as a new scale-invariant representation of the estimated Gibbs energy, as explained below. In FIG. 1, box 32 represents the CDF for v1, box 34 represents the CDF for v2, and box 36 represents the CDF for v3. Designating neighborhood sets and calculating Gibbs energy for a plurality of different radii allow for capture of both local features (using smaller radii) and global features (using larger radii) of lung lesions in the disclosed CAD system for assessment of pulmonary function for patients with infections, such as Coronaviridae infections, and more specifically, COVID-19.

### NN-Based Fusion and Diagnostic System

Classification steps 16 are performed by artificial intelligence. Disclosed herein is an embodiment of a NN system that can fuse the diagnostic results from the three estimated Gibbs energy at three different radii. In other embodiments, two, four, five, or more different radii may be used. The NN system conceptually includes four blocks 38, 40, 42, and 44, each representing a neural network, as illustrated in FIG. 1. Three neural networks 38, 40, 42 are fed with the three different CDFs 32, 34, 36 of the estimated Gibbs energy at each radii as input, then the output of the three neural networks 38, 40, 42 are input into a fourth neural network 44, referred to here as a fusion neural network, and fused to generate a computer aided diagnosis 46 based on the input medical image data. In this exemplary embodiment, the diagnosis 46 may be classification as a first state, e.g., a low severity infection, or a second state, e.g., a high severity infection. In some embodiments, a backpropagation approach is used to train the NN-based diagnostic system as follows: (1) randomly initialize the weights of the proposed NN-network; (2) compute the output of each neuron in the hidden and output layers; (3) update the weights of the proposed NN-network using the batch-mode backpropagation approach; and (4) repeat steps 2 and 3 until there are no significant changes in the NN-network weights.

A hyper-parameters estimation approach is used to tune the hyper-parameters used in the NN system. The parameters to be estimated are the number of bins used to calculate CDF, the number of hidden layers in the NN model, the number of neurons in the hidden layer, and the activation function used to calculate the output of each neuron. Several experiments were run using random values for these parameters to estimate their optimal values using training data. All the results that are demonstrated in the following “Experimental Results” section have been obtained using the following setting: to handle all energy values, the chosen value for the number of CDF bins is 175; the number of hidden layers in the first neural network 38, second neural network 40, and fusion neural network 44 is one, while for the third neural network 42, there are no hidden layers (searching from 0 to 10); the number of neurons per hidden layer is 50, 20, and 2 for the first, second and fusion neural networks 38, 40, 44, respectively (searching from 1 to 200); and the sigmoid activation function has been selected after also considering the tangent and softmax activation functions. A neural network including one hidden layer is the generalized case prior to tuning hyper-parameters. However, in the particular case of tuning the hyper-parameters with respect to training data of COVID-19 positive patients, as described herein, no hidden layer was found to be necessary for the third neural network 42. In other embodiments, each neural network may include zero, one, or more than one hidden layers.

### Experimental Results

To test and validate the system, data from a publicly available archive of COVID-19 positive cases, data from COVID-19 Open Research Dataset Challenge (CORD-19), and data from the University of Louisville, USA and Mansoura University, Egypt were used. These databases include 200 subjects tested as COVID-19 positive, 100 from patients who eventually died from the infection and 100 from patients who ultimately recovered. These databases comprise a heterogeneous collection of digital X-ray images, which was used to develop rotation, scale, and translation invariant MGRF model from which the imaging markers are extracted to grade the severity of lung infection in COVID-19 patients.

Referring now to FIGS. 4A-4D, the figures illustrate the estimated Gibbs energy for high severity lung infections (top panels) and low severity lung infections (bottom panels). Gibbs energy calculated at three radii (v1 in FIG. 4B, v2 in FIG. 4C, and v3 in FIG. 4D) is depicted as a color map fused over the x-ray images. These figures illustrate that the Gibbs energy in cases of high severity of COVID-19 pneumonia is high compared with the Gibbs energy for low-severity COVID-19 pneumonia. Since the collected X-ray images have different resolutions, CDF is used as a new scale-invariant representation to the estimated Gibbs energy which makes it suitable for all data collection protocols as shown in FIGS. 5A-5C. Referring now to FIGS. 6A-6C the average CDFs are calculated with a demonstration of the standard deviation at each point for both classes (high severity vs. low severity) to highlight the advantage of the proposed Gibbs energy as a new discriminatory image marker. The CDFs are rather distinctive which allows for straightforward classification by the proposed NN-based classifier. The output of the CAD system was an assessment of the severity of pneumonia in COVID-19 patients with two possible states: a first state indicating a low severity of infection (“low”) or a second state indicating a high severity of infection (“high”). This was compared to the ground truth of the 200 clinical cases collected, 100 of which were from patients who died of COVID-19 and 100 of which recovered. Accurate system outputs include an assessment of “low” in a case that recovered and an output of “high” in a case that died. To confirm the accuracy of the proposed NN classification and fusion system, leave-one-subject-out (LOSO), 10-fold, 4-fold, and a 2-fold cross-validation approaches are performed on our datasets as demonstrated in Table 1. The following objective metrics are used to measure the accuracy of the proposed NN-based fusion system: (i) sensitivity, (ii) specificity, (iii) accuracy, and (iv) Dice similarity coefficient (DSC). As demonstrated in Table 1, the proposed system has achieved 100% accuracy with the LOSO validation test and 98.00%±2.00% for a 2-fold validation test (real-life scenario), all of which confirm the efficacy of the CAD system.

An NN-based classifier was constructed using the estimated Gibbs energy at each radius to highlight the contribution of each Gibbs energy at each radius. As is clear from Table 1, the NN-classifier based on the estimated Gibbs energy at v3 demonstrates the highest accuracy compared with the classification accuracies based on the estimated Gibbs energy at v2 and v1. Also, fusing the three estimated Gibbs energies by using the NN-Based classification system achieves higher accuracy compared with classification accuracies based on each single estimated Gibbs energy. The accuracy of the proposed NN-based fusion system is further compared with support vector machine (SVM), random forest, naive Bayes, K-nearest neighbors (KNN), and decision trees classifiers. The results shown in Table 2, when compared to those shown in Table 1, illustrate that the NN-based classification and fusion system disclosed herein has achieved the highest sensitivity, specificity, DSC, and accuracy compared with other approaches.

## Automation

One or more steps in the method 10 may be implemented in an automated fashion, utilizing a computer or other electronic device to implement such steps. An exemplary apparatus within which various steps from method 10 may be implemented may be a server or multi-user computer that is coupled via a network to one or more client computers, as well as a medical imaging device. Each computer may represent practically any type of computer, computer system, data processing system or other programmable electronic device. Moreover, each computer may be implemented using one or more networked computers, e.g., in a cluster or other distributed computing system. In the alternative, the computer may be implemented within a single computer or other programmable electronic device, e.g., a desktop computer, a laptop computer, a handheld computer, a cell phone, a set top box, etc.

A computer typically includes a central processing unit including at least one microprocessor coupled to a memory, which may represent the random access memory (RAM) devices comprising the main storage of the computer, as well as any supplemental levels of memory, e.g., cache memories, non-volatile or backup memories (e.g., programmable or flash memories), read-only memories, etc. In addition, memory may be considered to include memory storage physically located elsewhere in the computer, e.g., any cache memory in a processor in the CPU, as well as any storage capacity used as a virtual memory, e.g., as stored on a mass storage device or on another computer coupled to this computer. The computer also typically receives a number of inputs and outputs for communicating information externally. For interface with a user or operator, a computer typically includes a user interface incorporating one or more user input devices (e.g., a keyboard, a mouse, a trackball, a joystick, a touchpad, and/or a microphone, among others) and a display (e.g., a CRT monitor, an LCD display panel, and/or a speaker, among others). Otherwise, user input may be received via another computer or terminal.

For additional storage, the computer may also include one or more mass storage devices, e.g., a floppy or other removable disk drive, a hard disk drive, a direct access storage device (DASD), an optical drive (e.g., a CD drive, a DVD drive, etc.), and/or a tape drive, among others. Furthermore, the computer may include an interface with one or more networks (e.g., a LAN, a WAN, a wireless network, and/or the Internet, among others) to permit the communication of information with other computers and electronic devices. Other hardware environments are contemplated within the context of the invention.

The computer operates under the control of an operating system and executes or otherwise relies upon various computer software applications, components, programs, objects, modules, data structures, etc. Moreover, various applications, components, programs, objects, modules, etc. may also execute on one or more processors in another computer coupled to the computer via a network, e.g., in a distributed or client-server computing environment, whereby the processing required to implement the functions of a computer program may be allocated to multiple computers over a network.

As an example, the computer may include a CAD system program used to implement one or more of the steps described above in connection with method 10. For the purposes of implementing such steps, an image database storing medical image data may be implemented in the computer. It will be appreciated, however, that some steps in method 10 may be performed manually and with or without the use of a computer.

## Discussion and Conclusion

ARDS is the most common and severe pulmonary complication in COVID-19 patients. It is an acute hypoxemic respiratory failure that requires oxygen and ventilation therapy including intubation and invasive ventilation. Clinically patients may have dyspnea, tachypnea (respiratory rate≥30 breaths per minute), decreased peripheral oxygen saturation SpO2≤93%, poor oxygenation with the ratio of the partial pressure of arterial oxygen to fraction of inspired oxygen PaO2/FiO2<300 mmHg, or lung infiltrates greater than 50% within 48 h. ARDS occurred in 20% of hospitalized patients and 61% of ICU patients in one study. ARDS occurs when capillaries in the lung leak fluid into the alveoli, thereby impairing gas exchange in the lung and reducing oxygen uptake into the systemic arterial circulation. The consequent decrease in blood oxygen levels can be directly life-threatening, leading to multi-organ failure. Respiratory support of COVID-19 may use invasive or non-invasive methods to force oxygen into the airways under pressure. Invasive ventilation uses an endotracheal tube to feed oxygen directly into the lungs. Non-invasive methods employ such devices as continuous positive airway pressure (CPAP) and oxygen hoods which do not involve use of an internal tube. Non-invasive methods are typically used in the management of less severe cases.

Despite being vital for supporting respiration in patients with ARDS, ventilators are in short supply in hospitals. According to Imperial College London, 30% of patients diagnosed with COVID-19 are strongly recommended to be admitted to the hospitals, with a significant fraction of those patients also requiring respiratory support. As the pandemic spreads across the world, many countries stopped exporting ventilators. The paucity of ventilators is even more acute in under developed and developing countries in South America, Asia, and Africa.

High-pressure ventilation may cause lung injury, also called barotrauma or ventilator-induced lung injury (VILI). Even non-invasive ventilation carries some risk, as stress and strain associated with high tidal volumes may cause patient self-induced lung injury (P-SILI). The additional inflammation due to VILI or P-SILI may lead to aggravation of pulmonary edema and worsening of the very respiratory distress that ventilation was intended to treat. There is also the risk of heart failure, hypervolemia, and multi organ dysfunction, alone or in combination. Unfortunately, COVID-19 patients who are admitted to the ICU and require mechanical ventilation show strikingly high rates of mortality, ranging from 50-97% early in the pandemic. A more recent study showed lower but still dramatic mortality rates of 36% in ICU patients requiring mechanical ventilation and 30% in all COVID-19 patients admitted to the ICU.

Accurate and rapid diagnosis of COVID-19 pneumonia severity is challenging for radiologists as the disease has rapidly spread across the globe. Based on the results demonstrated in this study, AI systems, especially those based on deep learning, are promising tools to assist initial screening by radiologists. It could decrease workload, improve diagnostic accuracy, and enable appropriate treatments and ventilation management of COVID-19 patients. In the case of a pandemic as we now face, medical resources are seriously strained and must be used as efficiently as possible. Rapid diagnosis and accurate prognosis are essential. The AI-based method shows great potential to quantify disease severity and could be used to inform treatment decision-making in patients with COVID-19. AI in concert with thoracic imaging and other clinical information (epidemiology, PCR, clinical symptoms, and laboratory indicators) can effectively improve clinical outcomes. AI can increase the utility of chest X-ray imaging beyond first-line diagnostic imaging and into the areas of risk stratification, monitoring of clinical course, and selection between management approaches, such as invasive vs. non-invasive ventilation, for COVID-19 patients. Multimodal data, be they clinical, epidemiological, or potentially molecular data, can by fused with imaging data in an AI framework to build systems to detect and treat COVID-19 patients and potentially to contain its spread.

The results herein demonstrate the feasibility of using AI with medical imaging data, such as thoracic X-ray imaging data, to determine the severity of lung infection in cases of COVID-19. Severity of pneumonia, as indicated by chest X-ray, correlates highly with mortality and thus this CAD system may be used to predict mortality in COVID-19 patients. While the specification discusses systems and methods using X-ray thoracic X-ray imaging data as input, it should be understood that other 2D and 3D medical imaging data may be used with the neural network-based diagnostic system and methods disclosed herein.

Various aspects of different embodiments of the present disclosure are expressed in paragraphs X1, X2, and X3 as follows:

X1. An embodiment of the present disclosure includes a method for assessing pulmonary function, comprising: receiving medical image data that includes image data of at least one lung; segmenting image data of the at least one lung from other image data; modeling the segmented image data using a model with a central-symmetric system of pixel-pixel interactions; and classifying, using a neural network, pulmonary function as a first state or a second state based at least in part on the model.

X2. An further embodiment of the present disclosure includes a process for assessing pulmonary function, comprising: receiving medical image data that includes image data of at least one lung; segmenting image data of the at least one lung from other image data; modeling the segmented image data using a model with a central-symmetric system of pixel-pixel interactions; and classifying, using a neural network, pulmonary function as a first state or a second state based at least in part on the model.

X3. A further embodiment of the present disclosure includes a computer aided diagnostic system, comprising: at least one data processor; at least one memory; and program code stored on the at least one memory, the program code configured to be executed by the at least one processor to cause the at least one processor to: receive medical image data that includes image data of at least one lung, segment image data of the at least one lung from other image data, model the segmented image data using a model with a central-symmetric system of pixel-pixel interactions, and classify, using a neural network, pulmonary function as a first state or a second state based at least in part on the model.

Yet other embodiments include the features described in any of the previous paragraphs X1, X2, or X3 as combined with one or more of the following aspects:

Wherein pulmonary function is impaired by an infection.

Wherein the infection is a Coronaviridae infection.

Wherein the infection is COVID-19.

Wherein the first state is low severity infection and wherein the second state is high severity infection.

Wherein the first state is non-severe infection and wherein the second state is severe infection.

Further comprising segmenting the image data of the at least one lung into healthy regions and unhealthy regions, and wherein modeling the segmented image data comprises modeling the unhealthy regions.

Further comprising segmenting the image data of the at least one lung into uninfected regions and infected regions, and wherein modeling the segmented image data comprises modeling the infected regions.

Further comprising segmenting the image data of the at least one lung into healthy regions and unhealthy regions, and wherein the segmented image data is segmented image data of the unhealthy regions.

Wherein the unhealthy regions are infected regions.

Wherein the unhealthy regions are subject to Coronaviridae infection.

Wherein the program code is further configured upon execution to cause the at least one processor to: segment the image data of the at least one lung into healthy regions and unhealthy regions, and wherein the segmented image data is segmented image data of unhealthy regions.

Wherein the model is at least one of translation, rotation, and scale invariant.

Wherein the model is a MGRF model.

Wherein the classifying uses a plurality of neural networks, each with different input, and a fusion neural network which uses the output of the plurality of neural networks as input.

Wherein modeling the segmented image data includes designating neighborhood sets for a plurality of different radii.

Wherein the model with the central-symmetric system of pixel-pixel interactions includes designation of neighborhood sets for a plurality of different radii.

Wherein modeling the segmented image data includes designating neighborhood sets in a MGRF model for a plurality of different radii.

Wherein the modeling further comprises determining Gibbs energy for each of the plurality of different radii.

Wherein the program code is further configured upon execution to cause the at least one processor to: determine Gibbs energy for each of the plurality of different radii.

Wherein the classifying uses a plurality of neural networks, each receiving Gibbs energy from different radii as input, and a fusion neural network which uses the output of the plurality of neural networks as input.

Wherein the neural network is a plurality of neural networks, each configured to receive Gibbs energy from different radii as input, and a fusion neural network which uses the output of the plurality of neural networks as input.

Wherein the fusion neural network outputs the classification of first state or second state.

Wherein the Gibbs energy is received as input for each of the plurality of neural networks in the form of a cumulative distribution function.

The foregoing detailed description is given primarily for clearness of understanding and no unnecessary limitations are to be understood therefrom for modifications can be made by those skilled in the art upon reading this disclosure and may be made without departing from the spirit of the invention.

