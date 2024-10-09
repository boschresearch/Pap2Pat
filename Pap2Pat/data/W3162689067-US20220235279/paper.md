# Introduction

As the world's most consumed light petroleum product, gasoline is one of the main fuels for automobiles. In 2018, global vehicle consumption is 9.5 million [1]. In the same year, the automobile industry consumes about 1.04 million ktoe of motor gasoline, while the transportation sector consumes 2.65 million ktoe oil products around the world, the automobile industry accounts for nearly half of the total consumption [2]. e exhaust gas emitted by gasoline combustion has a large negative impact on the atmospheric environment [3][4][5][6] and residents' health [7]. In 2018, greenhouse gas emissions from the transportation sector account for about 20% percent of the total global emissions [8]. erefore, the cleaning of gasoline is an important task for all countries in the world to purify air pollution. An important issue for clean gasoline production is to maintain the octane level of crude oil as its combustion performance index while reducing the sulfur and olefin content of crude oil so as to improve the quality of finished gasoline.

In the analysis and modeling of gasoline catalytic cracking, the high complexity of refining technology and the diversity of equipment have led to the nonlinear relationship between the operating variables of the control equipment and the strong coupling. e previous analysis models have fewer variables [9][10][11][12][13], and the models have higher requirements for raw materials [14][15][16], resulting in a lag in the response of the optimization process of the model; the refined oil obtained has more impurities and worse combustion performance, causing a certain economic loss. To avoid unnecessary losses, the modeling process needs to be optimized.

is article puts forward a novel idea: based on data analysis, the optimization process of gasoline catalytic cracking was modeled and actual data were collected to verify the practicability of the idea. is article intends to contribute to better modeling progress of gasoline catalytic cracking by adequately considering the impact of multiple factors, to optimize the production process and minimize the loss of gasoline octane.

is paper has seven parts. Besides the introduction, the second part is a literature review; the third part introduces the research ideas, data sources, and data dimensionality reduction processing process and constructs the prediction model; the fourth part proposes the prediction results; the fifth part analyzes the economic benefits gained after reducing octane loss; the sixth part shows the robust test with the PCA method; and the seventh part gives out the conclusion and the direction of future research.

e research idea of this article is of the following steps:

(1) Data Collection. Historical accumulated data of a petrochemical company's S-Zorb device are collected, including operating variable data, raw material data, product data, and catalyst data. After adjusting the data frequency difference, 325 samples are formed. (2) Data Cleansing. e maximum and minimum limit method, the PauTa criterion, and the null value processing method are used to deal with the values, with abnormal data and abnormal measured variables eliminated. (3) Data Dimensionality Reduction.

e dimensionalities of the processed data are reduced by the locally linear embedding method. e measured variables are retained according to the displayed weights to ensure that the selected variables are representative.

en, these variables are tested for correlation coefficients to remove redundant variables with too high correlation coefficients to ensure the independence between variables. (4) Model Building. e aforementioned dimensionality reduction variables and octane loss value are employed, a BP neural network model based on the genetic algorithm is established, and the optimal octane loss prediction model is obtained after adjusting the parameters. (5) Results Forecast. Using the optimal octane loss prediction model, after forecasting and weighted average according to the desulfurization standard, the predicted optimal operating conditions of the main operating variables are obtained. (6) Benefits Analysis. With the predicted optimal operating conditions obtained, the cost saved by reducing octane loss is compared with the cost of original operating conditions to clearly show the economic benefits. (7) Robust Test. e PCA method is employed in the step of data dimensionality reduction.

en, the GA-BP model is also constructed, and the fitting degree is tested for the robust test.

e process is shown in Figure 1.

is article puts forward an application-oriented method. Compared with previous studies, the possible innovations in this article are as follows:

(1) A locally linear embedding dimensionality reduction algorithm is used to reduce the dimensionalities of highdimensional data. Traditional linear dimensionality reduction methods, such as principal component analysis and factor analysis, are not appropriately suitable for these high-dimensional data. e locally linear embedding used in this paper can map high-dimensional variable data to low-dimensional vector space based on maintaining the relationships among data, to reduce the dimensionalities and optimize the modeling process.

(2) A BP neural network model optimized based on a genetic algorithm is used to predict gasoline octane loss. Previous studies are mostly implemented from the perspective of chemical mechanism, reducing the octane loss of refined oil by adjusting device configuration or chemical process, raw material properties, and so on. On the other hand, for a large number of variables and time-series data provided by the factory, the traditional regression analysis is hard to be applied because the degree of freedom loss is serious. is paper analyzes the impact of operating variables on gasoline octane loss through data analysis technology and provides enterprises with operating conditions to reduce gasoline octane loss from a new perspective and can further optimize the operation plan based on the mechanism of refined oil production.

# Literature Review

e cleaning of finished products of petroleum resources and the maximization of efficiency are currently problems facing the chemical industry. In terms of the cleaning of finished products, the main indicator is to reduce the sulfur and olefin content in the finished products. In terms of efficiency maximization, the main indicator is the retention of the octane number (Research Octane Number, RON) in the finished product, which is the most important indicator reflecting the combustion performance of gasoline and is also the brand name of gasoline.

e catalytic cracking technology used for refining petroleum is to crack heavy oil through the combined action of heat energy and catalyst to transform it into cracked gas, gasoline, and diesel [17]. During the catalytic cracking process, flue gas desulfurization is used [18][19][20], with olefins converted into liquefied petroleum gas by-products. e light oil using this technology has high productivity and good octane retention. Further improvement of catalytic cracking technology is conducive to better cleaning of finished products and maximum efficiency.

In the past, research on catalytic cracking technology focused mainly on mechanism models and technical improvements. Salazar et al. [21] proposed a process for upgrading nitrogen-rich and sulfur-rich heavy oil feedstock, which reduces the nitrogen and sulfur content while increasing the octane number. Valla et al. [15] studied the influence of various types of catalytic cracking feedstock on the distribution of sulfides in finished products and proposed the formation mechanism of sulfides on this basis. Brunet et al. [14] investigated the possible sources of sulfur impurities, discussed various factors affecting the hydrodesulfurization and olefin hydrogenation reactions, such as catalysts, carrier properties, and additives, and introduced processes for preserving the octane number of FCC gasoline. Li et al. [22] proposed selective hydrodesulfurization (RSDS-I) technology, which showed the superior desulfurization ability in industrial applications. Li et al. [23] chose CoMoP/η-Al 2 O 3 as catalyst to reduce sulfur content of coal tar light oil (CTLO), which is a potential material for the manufacture of high-octane gasoline blending component. Ayoub and Masoud [24] carried out the development of hydrodesulfurization as an alternative for cleaner production of liquefied petroleum gases. Yang et al. [16] analyzed the main factors affecting the change of gasoline octane number, such as the nature of raw materials, catalysts, and device operating conditions. Hasheminejad et al. [25] designed a new material for adsorptive desulfurization to achieve the lowering sulfur level in fuels. Qin et al. [26] established a model for the FCC process on a molecular level employing the structure-oriented lumping (SOL) method to investigate the effects of the diameter expanding reactor. e model established could calculate the molecular level product distribution from the reactor inlet to the outlet to reduce the olefins content and improve the iso-paraffins content of gasoline. Li et al. [27] put forward a high-efficient optimization of corresponding operation conditions for olefin separation. ey researched solvent extraction separating olefin and extracted sulfides simultaneously to protect the RON from a loss during hydrodesulfurization.

ere are also scholars conducting research on the use of data analysis techniques to establish related models. Qin and Chen [11] proposed a neural network prediction model for gasoline octane number, but only three influencing variables were considered: temperature, pressure, and flow rate of  continuous reforming reactor. Wei [28] used the principal component analysis and BP (back propagation) neural network to process the gas sensor array signal and analyzed the response of the array to gasoline, ethanol, and their mixtures. Yang et al. [13] used a neural network model optimized by the genetic algorithm BP (GA-BP) to establish a gasoline blending model. Paranghooshi et al. [10] used the artificial neural network (ANN) model to determine the octane number of gasoline blends produced by Tabriz refinery. Cheng and Yi [29] proposed a neural network model-based predictive control method for the etherification of FCC light oil. Zhang et al. [30] compared the accuracy of the BP model and the GA-ANN model in predicting the gasoline output of the RFCCU unit. Su et al. [31] used the GA-BP model to predict the production of coke as the main by-product in the catalytic cracking reaction.

Ouyang et al. [9] used 19 input variables to establish a BP neural network and studied the influence of raw material preheating temperature, two reaction zone outlet temperatures, and reaction pressure on product distribution. ey also used genetic algorithms to optimize the operating variables, and the gasoline yield was significantly improved after optimization. Tian et al. [12] used the particle swarm optimization (PSO-BP) neural network to predict the law of sulfur content in refined diesel products with operating parameters and compared the performance of BP, GA-BP, and PSO-BP. Cheng et al. [32] combined the BP neural network with the PID control, optimized the parameters of the controller, and applied it to the flow control of catalytic cracking natural gas, so as to control the concentration of the final product of heavy oil. Zhang et al. [33] established a nonrandom two-liquid model and a simulation method for the FCC naphtha solvent extraction process to fully improve the structure of the components of FCC naphtha aimed at the production of ultra-low-sulfur gasoline with minimal loss of octane number. Foroughi et al. [34] applied an artificial neural network to predict the volume percentage of adulterants to protect adulteration in gasoline based on the set of an automatic distillation apparatus measuring the recovered volume and temperature. Ma et al. [35] clarified the mechanism of research octane number (RON) and motor octane number (MON) of gasoline influenced by initial thermodynamic conditions and fuel chemistry. ey proposed a hybrid analysis framework, with a combination of the transient tracking method and datadriven modeling algorithm to realize the fast-forward prediction and analysis on fuel's ONs. In summary, in terms of optimizing the process of gasoline catalytic cracking, the academic circles mainly modify the raw material properties and optimize the steps and the equipment in the gasoline catalytic cracking process from the perspective of chemical industry. When using data analysis to adjust the corresponding catalytic cracking operation variables to achieve optimization, most studies selected few variables, and it is difficult to fully consider the impact of multiple factors. is article hopes to contribute in this regard.

# Data and Methodology

## Data Sources.

e original data are the historical accumulated data of the catalytic cracking gasoline S-Zorb unit of a petrochemical company. Operating variable data come from real-time database. e collection time is from April 2017 to May 2020, with a total of 353 operating variable sites collected. From April 2017 to September 2019, the data collection frequency was 3 minutes/time; from October 2019 to May 2020, the data collection frequency was 6 minutes/ time. e data time range for raw materials, products, and catalysts was from April 2017 to May 2020.

e octane number of raw materials and products is an important modeling variable. Since the octane number is difficult to measure, the data collection frequency is twice a week. e difference in the frequency of data collection is adjusted according to the actual situation. e measured value of the octane number can be regarded as the comprehensive effect within two hours before the moment.

e value of the manipulated variable is the average value of the previous two hours, which corresponds to the measured value of the octane number at that moment, resulting in 325 samples with a fixed time interval of two weeks (see Supplemental materials: S-Table 1).

## Data Cleansing.

Since the enterprise device has been operating continuously for 4 years, it is necessary to improve the accuracy and effectiveness of the recorded data. Before modeling, the data need to be sorted out. In the original data of the sample, most of the variable data is normal, but some data of each device have problems, some variables only contain data for part of the period, and some of the variables' data are all null values or some of the data are null values.

erefore, this article will process the original data for subsequent research.

First, according to the chemical process requirements and operating experience, the original data variables have a certain operating range (see Supplemental materials: S-Table 2), with the maximum and minimum limiting method used to remove some samples that are not within this range.

Second, outliers are removed according to the PauTa criterion (the 3δcriteria).

e variable is measured with equal precision, with x 1 , x 2 , . . . , x n obtained, wheren is the number of samples. e arithmetic mean x and the residual error v i � x i -x (i � 1, 2, . . . , n) are calculated, with the standard error δ determined according to Bessel's formula as follows:

.

(1)

is considered to be a bad value with a larger error value and is eliminated.

Finally, the null values in the measured variables of the data sample are processed. After counting, the average of the number of null values in each column is calculated and defined as the critical point for judging incomplete data. If the number of null values in the measured variable exceeds this critical value, it is considered that there are too many incomplete data in this column of data, which will adversely affect the goodness of fit, so this type of measured variable is eliminated. After calculation, the critical point of incomplete data judgment is 104, and 16 measured variables are eliminated after processing (see Table 1).

## Data Dimensionality Reduction.

When modeling, the variables need to be reduced in dimensionality. Dimensionality reduction is conducive to screening out the operating variables having the greatest impact on the octane number in the catalytic cracking process, ignoring secondary variables, and improving application efficiency. Due to the large number of variables, they can be regarded as highdimensional data; there is a nonlinear relationship between each other; the nonlinear dimensionality reduction algorithm is more suitable for the above situation.

### LLE Algorithm.

is paper uses locally linear embedding (LLE) [36,37] in the nonlinear dimensionality reduction algorithm for data dimensionality reduction. Compared with the traditional PCA (principal component analysis) sample variance reduction method, it retains the local linear characteristics of the sample when reducing the dimensionality.

e principle of LLE is that high-dimensional data are approximately locally linear in a very small local neighborhood in Euclidean space, and that a certain point can be represented by linear least squares of its surrounding points. LLE uses the linear fitting coefficients as the local geometric properties of the point to find the low-dimensional projection of the data. is algorithm is widely used in the field of high-dimensional data (see Appendix A for the specific algorithm).

### Data Dimensionality Reduction Results.

After obtaining the weight coefficient matrix through the LLE algorithm, the 29 control variables with the highest weights in the weight coefficient matrix are extracted. Taking into account the actual situation in the chemical process, the "Octane number of raw materials" should be taken as one of the main variables and included in the analysis, resulting in 30 main variables. e use of the LLE algorithm for dimensionality reduction can ensure that the above main variables are representative and then can determine whether the variables are related by calculating their correlation coefficients. e thermodynamic diagram representing the correlation coefficient of the variable is shown in Figure 2.

It can be seen from Figure 2 that the correlation between some variables and other variables is too high (the absolute value of the correlation coefficient being greater than 0.8), so the seventh, 12th, and 18th variables are deleted. After the deletion, the correlation coefficient of the representative variables decreases (as shown in Figure 3), which ensures the independence between the representative variables.

After processing and testing, 27 variables were finally retained as main variables, with the specific main variables shown in Table 2.

## GA-BP Model Establishment.

With the development of intelligent machine algorithms, data analysis techniques can be used to solve the problem of excessively high data dimensions. is paper establishes a GA-BP neural network model to predict the loss of gasoline octane number, aiming to adjust operating variables and reduce the loss of octane number in the chemical process.

### Model Design.

e back propagation (BP) neural network [38][39][40][41][42][43][44][45] is based on intelligent machine learning, has nonlinear features, good classification ability, and mapping ability to multidimensional functions, and has great advantages in multivariate regression. It has an input layer, an intermediate layer, and an output layer. In essence, the square of the network error is used as the objective function, and the gradient descent method is used to obtain the minimum value of the objective function. e calculation process is divided into two parts: forward propagation and backward propagation. When calculating the error in the forward direction, it goes from the input layer to the output layer, and the reverse adjustment process is to adjust the weight and threshold of the network through the distribution of the error signal in each layer so that the network error decreases along the gradient direction. (Figure 4) e genetic algorithm (GA) [42,43] is a parallel random search optimization method based on the theory of biological evolution to simulate the genetic mechanism of nature. Based on the principle of "survival of the fittest" in nature, individuals are selected, crossed, and mutated; individuals are screened according to the selected fitness function, individuals with better fitness are retained, and individuals with poor fitness are eliminated. e new group is better than the previous generation on the basis of inheriting the information of the previous generation. ey loop iteratively until the optimization is reached.

As a local search optimization method, the BP neural network is easy to fail in the case of nonlinear complex problems. In addition, the BP algorithm is also prone to overfitting. e genetic algorithm can optimize the neural network learning rules and improve the computational efficiency of the neural network; it is necessary to build a dynamic neural network structure to avoid the final result of the model being a local optimum instead of a global optimum. erefore, a BP neural network model is employed optimized based on a genetic algorithm, namely, the GA-BP model [44] to predict product octane loss (see Appendix B for specific algorithm design).

### Model Results.

e input layer X of the neural network is the 27 operating variables screened out above, the output layer P is the octane loss value and the product sulfur content 2 variables, and the formula of the hidden layer node is Y � ������ � n X + n P √ + L, (1 ≤ L ≤ 10), which is set to 7 here. In order to improve the accuracy of neural network prediction, the number of the training set is set to 300 and the number of the test set is set to 25. Each iteration is randomly sampled from the sample set.

After selecting and adjusting the parameters, the genetic algorithm finally sets the parameters as follows: the maximum number of iterations G max is set to 25, the population size M to 60, the crossover probability P c to 0.2, and the mutation probability P m to 0.05. e final parameters of the neural network are set as follows: the learning rate h is 0.1, the minimum error threshold E min is set to 0.00001, and the maximum number of iterations G max is set to 100.

After model construction, the overall goodness of fit of GA-BP prediction is 52.51%, the prediction error of octane number loss is small, and the prediction error of product sulfur content is large.

e error, error percentage, and fitness curve between the predicted value and the true value are shown in Figures 567. e optimized neural network model after training is saved, which is the prediction model of gasoline octane number loss.

It is assumed that the physical and chemical properties of raw materials and standby and regenerated adsorbents in the optimization process remain unchanged (the octane number of raw materials and the sulfur content of raw materials in the main variables also remain unchanged). According to China's current standard GB 18352.6-2016, the sulfur content of finished gasoline products is required to be not more than 10 μg/g. In order to leave room for business operations, the selection criteria for sulfur content in this article are not more than 5 μg/g. For the 25 main operable variables corresponding to the above samples, simulation samples are generated according to the variable range and minimum change value, simulated the debugging process of the variables, and used the octane loss reduction as the weighted average to obtain the optimal operating conditions.  

# Main Results

In summary, we have obtained the main operating variables of the petrochemical enterprise that affect the catalytic cracking gasoline S-Zorb unit, as well as the optimal operating conditions when the product sulfur content is less than 5 μg/g, as shown in Table 3. e above results provide companies using S-Zorb with reference data for optimizing the process of catalytic cracking gasoline.  

# Economic Benefit Analysis

In the process of refining gasoline with S-Zorb unit in existing petrochemical enterprises, if the octane number is reduced by 1 unit, it is equivalent to reducing the economic loss of $23.055 per ton. erefore, in this study, the average RON of the original data sample is 88.45 units, and the average octane number of the product under the optimal operating conditions is 89.70 units. After the prediction of the GA-BP model and the optimization of operating conditions, the octane number loss of the product is reduced by 1.25 units. If we take the automobile industry in 2018 as an example and calculate by the annual gasoline consumption of 1.04 million kt, the application of this research can save about 29.97 million dollars for automobile industry in the whole world.

It can be seen that reducing the octane loss of gasoline products will bring huge economic cost savings to enterprises and will also cut down air pollution and the corresponding cost of treatment, so the conclusions of this study can provide excellent economic benefits in practice.

# Robust Test

To verify the reliability of the method and conclusion in this paper, the principal component analysis (PCA) [46] 

Threshold Θb is used to reduce the dimension of the original variables and sample data, and then the GA-BP model is also constructed, and its fitting degree is tested for the robust test. PCA aims at trying to create a new set of unrelated comprehensive indicators composed of the original indicators with different weights. Since it is necessary to adjust the operating variables of the S-Zorb device to achieve the goal of reducing octane number loss, the first 26 variables are also retained according to the weight and the variable "Octane number of raw materials" is added. For the variables retained that are already representative and unrelated, the calculation of their correlation coefficients is omitted. e specific main variables are shown in Table 4.

# Input layer Hidden layer Output layer True values Error

en, the main variables above are employed by GA-BP modeling. After model construction, the overall goodness of fit is 45.36% with a similar error performance. e error, error percentage, and fitness curve between the predicted value and the true value are shown in Figures 8910.

It can be concluded that the overall fit goodness of the PCA method is inferior to that of the LLE method. For this study focused on more than 300 variables, the PCA method is not appropriately suitable for such high-dimensional data.   (2) After employing the GA-BP neural network to obtain the prediction model of gasoline octane number loss, the optimal operating conditions of the main operating variables are achieved (see Table 3) under the condition that product sulfur content is less than 5 μg/g. With the optimal operating conditions can we get the optimal effect of reducing octane loss.

e realization of the optimal operating condition calculated above is conducive to the following aspects:

(1) Improving the quality of refined oil products of chemical enterprises. By debugging the above operating points and controlling the corresponding operating conditions such as temperature, flow, or pressure difference, enterprises can improve the quality of the finished oil. (2) Saving the economic cost of chemical enterprises. By optimizing operating conditions to reduce the loss of octane number, the economic benefits of enterprises can be improved. (3) Protecting the atmospheric environment. By optimizing the operating conditions to make the refined oil meet the national standards, it is beneficial to reduce sulfide emissions and reduce air pollution.

7.2. Future Outlook. In the future, research can be carried out in the following directions. Firstly, combining the catalytic cracking process and principles based on dimensionality reduction can better select the variables of the structural model.

Secondly, the neural network has relatively high requirements for data, but the quality and accuracy of the data in the example are not enough, so the model has a low degree of fit. In the future, more data can be collected or the data preprocessing process can be optimized to obtain data with fewer empty values and outliers.

irdly, with the development of data analysis technology, other intelligent machine learning algorithms can be used in the future, and comparative analysis can be performed to select better methods [47,48].

Finally, for the automobile industry, research can be developed on how to reduce the energy consumption of automobile engines. Reducing energy consumption by improving engine performance is also an important way to reduce gasoline consumption and air pollution.

x ji is the j th nearest neighbor to x i , (1 ≤ j ≤ k), w i � [w 1i , . . . , w ki ] T and, x i � [x 1i , . . . , x Di ] T , where D is the dimension of x i Solving the weight coefficient matrix means to solve the constrained optimization problem as follows:

us, the expression of the weight coefficient matrix can be deduced as follows:

en, view S i as local covariance matrix, S i � (X i -N i ) T (X i -N i ). Eq. (A.2) can be viewed as follows:

Use the Lagrange multiplier,

where 1 k is k × 1 column vector with entries of 1. Take derivative of Eq. (A.4) as follows: 

Make M � (I -W)(I -W) T and use the Lagrange multiplier again as follows:

Take derivative of Eq. (A.9) as follows: 

# B. A BP Neural Network Based on Genetic Algorithm

BP neural network based on the genetic algorithm is [38][39][40][41][42][43][44][45] as follows.

B.1. Initialization Network. Firstly, determine the number of network nodes, training set, and test set, and the data are normalized. en, the individual in the genetic algorithm is initialized with real coding. Each individual is composed of four parts, namely, the weight matrix W a between the input layer and the hidden layer, the threshold vector q a of the hidden layer, the weight matrix W b between the hidden layer and the output layer, and the threshold vector q b of the output layer, forming a definite neural network.

# B.2. BP Neural Network. (1) Forward propagation:

e input layer is x 1 , x 2 , . . . , x n , with the weight matrix W a between the input layer and the hidden layer. Use the linear weighted sum method to obtain the net input of the i neuron of the hidden layer which is Netin i � 􏽐 n j�1 x j W a ij . e net input is compared with the threshold vector q a of the hidden layer, and then the neuron output can be obtained by activation function. Sigmod function f(x) � 1/1 + exp(-x) is selected here as the activation function to realize signal transformation. erefore, the output of i neuron of the hidden layer is as follows:

en, with the weight matrix W b between the hidden layer and the output layer, use the same linear weighted sum method to obtain the net input of the i neuron of the output layer which is Outnetin i � 􏽐 n j�1 y j W b ij . e net input is compared with the threshold vector q b of the output layer likewise, and then the i neuron output can be obtained by inverse function of Sigmod as follows:

e real output is z 1 , z 2 , . . . , z m , and the least square error of the k th prediction result is as follows:

(2) Backward propagation: e purpose of backward propagation is to reduce the prediction error E K and optimize the neural network. Here, the gradient descent method is used to update and reduce the parameters. e parameter adjustment formula is as follows:

where h is the leaning rate.

After adjusting the aforementioned parameters, the neural network is optimized by repeating iteration and adjustment. (3) Termination conditions:

When one of the following termination conditions is reached, the iteration is stopped and a neural network is obtained.

(1) e minimum error threshold E min is reached (2) e maximum number of iterations G max is reached B.3. Calculate Fitness. After running the neural network with the training set data, the prediction system output was obtained for each individual and the fitness of the individual F i is defined as the error E i between the predicted output and the real output, and the formula is as follows:

where n is the number of output nodes; p i is the predicted output of the i node, and z i is the real output of the i node. Firstly, calculate the probability that an individual will be selected:

where f i � (k/P i ) is the reciprocal of the fitness, which is positively correlated with adaptability; k is the coefficient, which is set at 1; and N is the population size. en, the interval [0, 1] is divided into N intervals, the length of which is the same as the probability of an individual will be selected. e location interval is determined by generating random numbers so that corresponding individuals could be selected to form a new population.

(2) Cross:

Cross is individuals of new populations exchange gene fragments to generate new individuals. Since individuals are real coding, the real cross method is adopted here for crossover operation. Firstly, the individual in the group is judged to carry out the cross with the set crossover probability. e formula of cross between the m individual and the n individual at the j intersection position is as follows: Mutation is changes in the individual's own gene value. Since individuals are real coding, real value mutation is adopted here for mutation operation. Firstly, the individual in the group is judged to carry out the mutation with the set mutation probability. en, the j mutation location of the i individual was selected for the mutation operation. e formula is as follows:

where a max is the upper bound of a ij , a min is the lower bound of a ij , r is the random number in [0, 1], f(g) is the mutation formula: f(g) � r 2 (1 -(g/G max )) 2 , r 2 is the random number in [0, 1], g is the current iteration number, and G max is the maximum number of iterations. When one of the following termination conditions is reached, the iteration is stopped, and the optimal initial weight and threshold are obtained.

(1) e fitness of the optimal individual and the fitness of the population stopped rising (2) e maximum number of iterations G max is reached B.5. Optimal Prediction Model Building. When the optimal initial weight and threshold are obtained by the genetic algorithm above, they are given to BP neural network for the optimal network forming. When one of termination conditions is reached, iteration is stopped, and the optimal neural network is obtained.

# Acknowledgments

is research was supported by the National Social and Scientific Fund Program of China (17BGL142 and 18ZDA052) and Natural Science Foundation of China (91546117 and 71904117).

# Data Availability

Historical accumulated data of a petrochemical company's S-Zorb device are collected, including operating variable data, raw material data, product data, and catalyst data. After adjusting the data frequency difference, 325 samples are formed.

# A. Locally Linear Embedding

Locally linear embedding is [36,37] as follows.

A.1. Locally Linear Range. Firstly, the locally linear range is solved by using the K-nearest neighbor principle. Because of locally linearity, each data point x i can be represented by a linear combination of its nearest neighbor data points. at is, x i � 􏽐 k j�1 w ji x ji , and N i � knn(x i , k), N i � [x 1i , . . . , x ki ], where w i is k × 1 column vector, w ji is row j of w i , 

# Conflicts of Interest

e authors declare that they have no conflicts of interest.

# Supplementary Materials

(1) S-Table1: the historical accumulated data of the catalytic cracking gasoline S-Zorb unit. ere are 325 samples of operating variable data, raw material data, product data, and catalyst data observed in different time intervals within 2017-2020. (2) S-Table2: the certain operating range and minimum adjustment range of operating variables. (Supplementary Materials)

