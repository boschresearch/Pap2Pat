# Introduction

Hydraulic fracturing operation in horizontal wells has become the most effective stimulation technology for unconventional, low-permeability reservoirs. Real-time evaluation of the fracturing process provides important information to design the unconventional-reservoir completion and improve production (Montgomery et al., 2010). The conventional monitoring methods, such as microseismic, time-lapse seismic, and pressure monitoring, are limited to coverage and resolution. Recently, distributed acoustic sensing (DAS) is emerging as a real-time downhole sensing technology. The fiber cable is installed permanently on the outside of a casing string and measures the vibration along the wellbore. In the DAS system, the interrogator unit transmits laser pulse along the cable, and the interferometer measures the changes in the Rayleigh backscattering pattern associated with any deformation on the cable caused by incident waves (Mateeva et al., 2014;Spica et al., 2020). It is superior to other wellbore detection methods for real-time measurement, high spatial resolution and convenient deployment.

The high-density data recorded by the fiber cable in the injection well can directly show the fluid migration in the wellbore. Through the detailed surveillance of the fluid in the stimulation process, the design of commonly used plug-and-perf completion can be optimized. The operation parameters are chosen to achieve low-lost, high-efficiency production, such as fluid type, pumping method, injection volume, and adjustment of sand concentration (Jin et al., 2017;Richter et al., 2019). However, the manual analysis of DAS data is inefficient and prone to error. Applying machine learning or deep learning to this problem is an attractive solution. Jin et al. (2019) propose the artificial neural network (ANN) algorithm to identify fracture-hit signals from the DAS data recorded at offset monitor wells. Binder and Tura (2020) use convolutional neural networks (CNNs) to detect microseismic events in the downhole DAS data. Stork et al. (2020) shows the successful application of CNNs to microseismic event detection in DAS data. The purpose of this study is to identify the signal related to fluid injection in the borehole. The CNN is combined with Bidirectional Long Short-Term Memory Networks (BiLSTM) to extract the spatial and temporal features from the DAS data. The results demonstrate the feasibility and effectiveness of the proposed framework for large DAS data volume.

# Methods

Convolutional Neural Networks (CNNs) is a class of feedforward neural networks that include convolution computation and non-linear activation operators (O'Shea and Nash, 2015). It is one of the representative algorithms of deep learning. CNNs are commonly used to analyze visual images. They are also known as motion-invariant or space-invariant

## FIGURE 1

The schematic structure of the proposed network.    classification, image segmentation, medical image analysis, natural language processing, etc. (Gu et al., 2018). As for the processing of time series data, such as the DAS data, recurrent neural networks (RNNs) is a very classic structure applied to data prediction (Medsker and Jain, 2001). It is used to find the relation of the data volume and predict the data within the corresponding context. However, due to its simple structure, RNNs suffer from gradient disappearance and gradient explosion when dealing with long-term sequence problems (Salehinejad et al., 2017). The Long Short-Term Memory (LSTM) networks are a type of neural network with stronger capability for time series prediction, which is developed from the RNNs (Hochreiter and Schmidhuber, 1997;Van Houdt et al., 2020). LSTM consists of one or more functional unit modules with forgettable and memory functions. This model is proposed to solve the problem that the traditional RNNs have the disappearance of backpropagation gradient in the long-term sequence. The core components of LSTM networks include forget, input, and output gates. LSTM networks are well suited for classification, processing and forecasting problems for time series data. Conventional RNN units and deep learning networks based on LSTM units cannot save the value of the previous time series due to the limitation of their basic structure, so they are better at predicting the next time step data with current data but lack the ability to predict a previous time step. For many sequence prediction problems, the time series data are bidirectional time-dependent. Thus RNNs and LSTM become inefficient in prediction ability. To overcome this limitation, bidirectional RNNs (BRNNs) make use of previous context by processing the data in both directions with two separate hidden layers, which are then fed forwards to the same output layer (Schuster and Paliwal, 1997). Combining BRNNs with LSTM gives bidirectional LSTM (BiLSTM), which can access long-range context in both input directions (Graves et al., 2013).

CNNs is the well-known artificial neutral network and widely applied in image recognition, classification and segmentation. But it can only provide the mapping of spatial features from the input to the output. The DAS data are time series, and the temporal relations can not be learned and predicted by CNNs. RNNs are able to extract temporal dynamic characteristics but have limitations on memory cost. LSTM can be considered as an improved version of RNNs and is suitable to learn long-term dependencies. A Bidirectional LSTM (BiLSTM) is a model that consists of two LSTMs to receive the forward and backward information. It can effectively increase both preceding and subsequent information available to the network. In the processing of DAS data for signal identification, we combine the CNNs and BiLSTM to extract both the spatial and temporal features. The proposed model benefits from the advantages of CNNs and BiLSTM. The image features are captured by CNNs and the long-term dependency of the data is learned by the BiLSTM. Figure 1 shows the detailed scheme of the network architecture used in this study. The size of the input image is    The raw DAS data with high (A) and low signal-to-noise ratio (B).

in the fusion classification of space-time features is prone to errors (Tang et al., 2021), thus we add a fully connected network to improve the conversion performance. This modification can optimize computational efficiency and reduce the over-fitting phenomenon.

# Training data

The DAS system is deployed along the injection well in the shale gas field. The monitoring geometry is shown in Figure 2. The length of the cable is approximately 2.5 km. The spatial resolution is 1 m and the temporal interval is 0.25 ms. Figure 3 shows the processing steps of the raw data. The data is segmented along the time and channel axis, respectively. The datasets are selected from the recorded data of three wells at the same site in about 1 month. With the recorded data, the data are labeled manually by visual inspection to generate the training dataset. Figure 4 shows the typical labeled result of the data slice. After the manual labeling, the dataset are separated into training dataset and testing dataset with a ratio of 8:2.

# Network training

The goal of signal detection for fluid injection in hydraulic fracturing is to establish a rapid real-time evaluation and response system with high accuracy and high sensitivity. The following parameters are used to judge the performance of the trained model.

## 1) Effective detection rate (EDR)

The ratio of the effective signal detected, which is equal to the recall rate. It is calculated as follows: 

## EDR TP TP + FN

where TP is the true positives, which refers to the number of correct detections for signals triggered by the trained network. FN is the false negatives, which refers to the number of wrong identifications for noise.

### 2) False alarm rate (FAR)

The ratio of false and correct identified signals of fluid injection, which is

where FP is the false positives, which refers to the number of wrongly indication for effective injection signals.

3) F1 score A measure that combines precision and recall, which is also the harmonic mean of precision and recall Using the training dataset, we obtained the proposed model and used the testing dataset to validate its performance. The results are shown in Table 2. EDR is used to evaluate the precision of the identification model, FAR is used to indicate the missing of effective signals. F1 score is the overall evaluation using evenly weighted recall and precision. The results shows the trained model can effectively identify the signal from the raw data and the processing time can meet the requirements for real-time monitoring. On the computation node with four Nvidia Titan (Pascal) GPUs, it took about 5 days for the training.

# Application to field data

In the application, the collected data in different stages that are not included in the training and testing datasets are used. Figure 5 shows the data slices with relatively high and low signalto-noise ratio, respectively. Using the trained model for identification, the results are shown in Figure 6. It can be To further demonstrate the validity of the proposed model, the accumulated energy (the square of amplitude) of the recorded data is compared with the production curve. Figure 7 shows the results. In the conventional method of directly accumulating energy in the full record, the DAS response is inconsistent with the slurry rate curve, which is mainly due to the continuous background noise during the monitoring process. The results based on the identified DAS response can accurately fit with the slurry rate curve, as the extract DAS responses are directed related to fluid injection procedure. The model works effectively for the data collected at the same area as the validate data are similar to the training data. But it may need to be updated when the data have different characteristics. With more DAS data, the performance of the trained model can be further improved. The new deep learning algorithms developed for action recognition in video signals can also be introduced to improve the efficiency of the proposed method.

# Conclusion

We propose a deep-leaning approach for real-time evaluation of raw DAS data to identify the signals related to fluid injection in hydraulic fracturing. The trained model demonstrates its effectiveness and accuracy in application to field data. The effective detection rate of injection signal is 95.1%, which enables real-time evaluation of hydraulic fracturing operation from downhole DAS data. The structure combing CNNs and BiLSTM performs reasonably well in spatiotemporal signal classification. The current models can be further improved in practical applications with more DAS data and better action recognition strategies.

## Acknowledgments

We would like to thank three reviewers for their valuable comments that improved this manuscript significantly.

## Funding

This study was funded by the CAS Project for Young Scientists in Basic Research (Grant No. YSBR-020), and the National Natural Science Foundation of China (Grant No. 42025403).

# Data availability statement

The data analyzed in this study is subject to the following licenses/restrictions: Data associated with this research are confidential and cannot be released. Requests to access these datasets should be directed to zhengyk@mail.iggcas.ac.cn.

## Author contributions

YZ performed the data analysis. YZ and YW wrote and revised the manuscript. YW and XL provided the research ideas and supervised the findings of this work. QX, EL, SW, SA, YY, CL, and JM collected the original dataset and performed the preprocessing. All authors discussed the results and contributed to the final manuscript.

# Conflict of interest

Authors XL, CL and JM were employed by the company PetroChina Zhejiang Oilfield Company. Author EL was employed by the company China State Shipbuilding Corporation, Limited 715th Research Institute, Author SA was employed by the company Optical Science and Technology (Chengdu) Ltd.

The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

