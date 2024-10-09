# Introduction

Time series forecasting is a cornerstone of modern machine learning and has applications in a broad range of domains, such as operational processes (Salinas et al., 2020), energy (Lai et al., 2018), and transportation (Salinas et al., 2019). In recent years, models based on deep neural networks have shown particularly impressive results (Rangapuram et al., 2018;Salinas et al., 2019;2020;Rasul et al., 2021b) and demonstrated the effectiveness of deep feature and latent state representations. Despite this exciting progress, current time series forecasting methods often make the implicit assumption that the distribution of future observations conditioned on the input and past observations is time-invariant. In real-world applications this assumption can be violated, which poses serious practical challenges to a model's robustness and predictive power. The statistics literature studies several related concepts of (non-)stationarity for time series, with weak and strong stationarity being most widely used (Hamilton, 1994;Brockwell & Davis, 2009). Common to these variants of (non-)stationarity is that they are defined in terms of a stochastic process' joint or marginal distribution. For example, given a univariate time series {y t ∈ R} t∈Z and any subset of time points {t 1 , t 2 , . . . , t k }, the time series is strongly stationary if ∀τ ∈ Z : p(y t1 , y t2 , . . . , y t k ) = p(y t1+τ , y t2+τ , . . . , y t k +τ ).

While non-stationarity in a stochastic process' joint or marginal distribution is important and has been widely studied (Dickey & Fuller, 1979;Kwiatkowski et al., 1992;Hamilton, 1994;Kim et al., 2022), we argue that temporal forecasting relies more heavily on the properties of its conditional distribution p(y t |y t-B:t-1 , x t-B:t ), where y t-B:t-1 = (y t-B , y t-B+1 , . . . , y t-1 ), y t is a real vector of the target variable, B ∈ Z >0 is the lookback window size and can be arbitrarily large, and x t is a real vector containing auxiliary information. Most forecasting methods, from traditional approaches (e.g., Autoregressive Integrated Moving Average (ARIMA; (Box et al., 2015)), Generalized Autoregressive Conditional Heteroskedasticity (GARCH; (Engle, 1982;Bollerslev, 1986)), state-space models (SSMs; (Kalman, 1960))) to more recent models (e.g., recurrent neural networks (RNNs; (Hochreiter & Schmidhuber, 1997;Salinas et al., 2020)), temporal convolutional networks (TCNs; (Bai et al., 2018)), Transformers (Vaswani et al., 2017;Rasul et al., 2021b;Wu et al., 2021;Nie et al., 2022;Drouin et al., 2022), Neural Processes (NPs; (Garnelo et al., 2018a;b))), rely on this conditional distribution for predictions, but many of them implicitly assume its stationarity by using time-invariant model parameters. While a model with stationary conditional distribution can still handle non-stationarity in the joint or marginal distribution, such as seasonality and trend, by conditioning on extra features in x t , such as day of the week, the conditional distribution itself may also change due to (1) unobserved causes and/or (2) new causes. For example, the daily number of posts from each user on a social media platform is unlikely to be robustly predictable from historical data, even with input features like day of the week, because (1) user activity is often affected by events that are not reflected in the observable data (e.g., illness); and (2) events that have not been seen before may occur (e.g., a new functionality being added to the platform) and change the functional pattern of the input-output relation between the conditioning and target variables in an unpredictable way. How to deal with these changes in the conditional distribution is the main focus of this work.

Autoregressive (AR) models, TCNs, and Transformers model p(y t |y t-B:t-1 , x t-B:t ) with time-invariant parameters (e.g., the weights and biases in the neural network) and therefore assume stationarity in p(y In this work, we take a different approach to dealing with non-stationary conditional distributions in time series. The core of our model, called DynaConF1 , is a clean decoupling of the time-variant (non-stationary) and the time-invariant (stationary) part of the distribution. The time-invariant part models a stationary conditional distribution, given a control variable, while the time-variant part focuses on modeling the changes in this conditional distribution over time through the control variable (Figure 1). Using this separation, we build a flexible model for the conditional distribution of the time series and make efficient inferences about its changes over time. At test time, our model takes both the uncertainty from the conditional distribution itself and non-stationary effects into account when making predictions and can adapt to unseen changes in the conditional distribution over time in an online manner.

# Related Work

Time series forecasting has a rich history (Hamilton, 1994;Box et al., 2015), with many recent advances due to deep neural networks (Lim & Zohren, 2021). The following paragraphs discuss different approaches to non-stationary time series modeling and their relation to our work.

# Non-Stationary Marginal Distribution.

There are three common ways of dealing with non-stationarity in the marginal distribution: (1) Data transformation. In ARIMA models, taking the difference of the time series over time can remove trend and seasonality. More advanced approaches based on exponential smoothing (Holt, 2004) or seasonal-trend decomposition (Cleveland et al., 1990) have also been combined with deep neural networks, achieving promising performance (Smyl, 2020;Bandara et al., 2020). More recently, Kim et al. (2022) propose to use reversible normalization/denormalization on the input/output of the time series model to account for (marginal) distribution shifts over time.

(2) Inductive bias. As an alternative to data transformations, the underlying ideas of exponential smoothing and decomposition can also be incorporated into deep learning models as inductive biases, which enables end-to-end handling of seasonality/trend (Lai et al., 2018;Oreshkin et al., 2019;Wu et al., 2021;Woo et al., 2022). Similarly, in models based on Gaussian processes, the inductive biases can be added as specific (e.g., periodic or linear) kernel choices (Corani et al., 2021), and in models based on temporal matrix factorization as part of the loss function (Chen et al., 2022). (3) Conditioning information. Adding features such as relative time (e.g., day of the week) and absolute time to the model input as conditioning information is commonly used in deep probabilistic forecasting models (Rangapuram et al., 2018;Salinas et al., 2019;2020;Rasul et al., 2021b;a).

In our work, we focus on proper handling of changes in the conditional distribution. To deal with marginal distribution shifts, we simply add conditioning information as in approach (3), although we could potentially utilize approach (1) and (2) as well.

Non-Stationary Conditional Distribution. State-space models (Fraccaro et al., 2017;Rangapuram et al., 2018;de Bézenac et al., 2020;Tang & Matteson, 2021;Klushyn et al., 2021) and recurrent neural networks (Salinas et al., 2019;2020;Rasul et al., 2021b;a) are among the most popular choices to model temporal dependencies in time series. When these models are applied to, and therefore conditioned on, the entire history of the time series, they can theoretically "memorize" different conditional distributions at different points in time. However, for these models to generalize and adapt to new changes in the future, it is critical to have appropriate inductive biases built into the model. A common approach is to allow state-space models to switch between a discrete set of dynamics, which can be learned from training data (Kurle et al., 2020;Ansari et al., 2021). However, the model cannot adapt to continuous changes or generalize to new changes that have not been observed in the training data. In contrast, our model has explicit inductive biases to account for both continuous and discontinuous changes, and to adapt to new changes. Yanchenko & Mukherjee (2020) proposed a nonlinear state-space model with a time-varying transition matrix for the latent state. In contrast, our model is a decoupled deep model separating the time-invariant conditional distribution modeling using a deep encoder and the non-stationary dynamics modeling.

Observation Model. The expressivity and flexibility of the observation model is a topic that is especially relevant in case of multivariate time series. Different observation models have been employed in time series models, including low-rank covariance structures (Salinas et al., 2019), auto-encoders (Fraccaro et al., 2017;Nguyen & Quanz, 2021), normalizing flows (de Bézenac et al., 2020;Rasul et al., 2021b), determinantal point processes (Le Guen & Thome, 2020), denoising diffusion models (Rasul et al., 2021a;Tashiro et al., 2021;Alcaraz & Strodthoff, 2022), and probabilistic circuits (Yu et al., 2021). In this work, we prioritize scalability by assuming a simple conditional independence structure in the output space and consider more expressive observation models as orthogonal to our work.

Online Approaches. Continual learning (Kirkpatrick et al., 2017;Nguyen et al., 2018;Kurle et al., 2019;Parisi et al., 2019;De Lange et al., 2021;Gupta et al., 2021) also addresses (conditional) distribution changes in an online manner, but usually in a multi-task supervised learning setting and not in time series. In this work, our focus is on conditional distribution changes in time series, and the conditional distribution can change either continuously or discontinuously in time.

# Method

We study the problem of modeling and forecasting time series with changes in the conditional distribution p(y t |y t-B:t-1 , x t-B:t ) over time t, where y t ∈ R Dy is the target time series, and x t ∈ R Dx is an input containing contextual information. We make the following assumption: , for t ≤ T , may contain any information known at time t, while x t , for t > T , can only contain information known in advance, such as day of the week. We do not distinguish between these two cases in notation for simplicity.

## Decoupled Model

We assume that the distribution p(y t |y t-B:t-1 , x t-B:t ) is from a distribution family parametrizable by θ t ∈ R D θ . Concretely, we assume a normal distribution N (µ t , Σ t ), so θ t := (µ t , Σ t ). Our decoupled model is not restricted to this assumption, but as we will see in Section 3.5 it allows for more efficient inference. Furthermore, we assume

so f : R B×Dy × R (B+1)×Dx → R D θ models the conditional distribution, with its own static parameters denoted collectively as ψ, and is modulated by a dynamic control variable ϕ t ∈ R D ϕ , which can change over time according to a dynamic process defined in Section 3.3. A property guaranteed in our model is that if ϕ t stays the same across time, then the conditional distribution p(y t |y t-B:t-1 , x t-B:t ) stays the same as well.

Our key idea is to separate the time-variant part of the model from the time-invariant part, instead of allowing all components to vary across time. This simplifies probabilistic inference and improves the generalization capabilities of the learned model by allowing the time-invariant part to learn from time-invariant input-output relations with time-variant modulations.

## Conditional Distribution at One Time Point

First we describe how we model the conditional distribution p(y t |y t-B:t-1 , x t-B:t ) at each time point t without accounting for non-stationary effects (Figure 1, left). We use a neural network g to encode the historical and contextual information into a vector h t ∈ R D h as h t = g(y t-B:t-1 , x t-B:t ). For example, g could be a multi-layer perceptron (MLP) or a recurrent neural network (RNN). The parameters of g are time-invariant and included in ψ (Eq. 1).

We note that a key distinction between our model's use of an RNN and a typical deep time series model using an RNN is that the latter keeps unrolling the RNN over time to model the dynamics of the time series.

In contrast, we unroll the RNN for B + 1 steps to summarize (y t-B:t-1 , x t-B:t ) in the exact same way at each time point t, i.e., we apply it in a time-invariant manner.

We construct the distribution of y t such that each dimension i of y t , denoted as y t,i , is conditionally independent of the others given h t ; this helps the learning and inference algorithms to scale better with the dimensionality of y t . First we transform

where W z,i ∈ R E×D h and b z,i ∈ R E , so z t,i corresponds to y t,i . Then, from z t,i , we obtain the distribution parameters θ t,i of y t,i . Specifically, we assume a normal distribution with a diagonal covariance for y t , so

where

and b µ,i along i, and similarly w σ , b σ , z t , µ t , σ t .

## Conditional Distributions Across Time Points

We have explained how we model the conditional distribution p(y t |y t-B:t-1 , x t-B:t ) at each time point t. To model changes in the conditional distribution over time, we first specify which parameters to include in the control variable ϕ t ∈ R D ϕ , which changes over time and modulates the conditional distribution (Figure 1, right).

We choose ϕ t := w µ . Recall that w µ transforms z t into the mean µ t of y t , where z t is a summary of the information in the conditioning variables (y t-B:t-1 , x t-B:t ). By allowing w µ to be different at each time point t, the conditional mean of y t , E[y t |y t-B:t-1 , x t-B:t ], can change accordingly. We could allow w σ to change over time as well, effectively modeling a time-variant conditional variance, but focusing on w µ reduces the dimensionality of ϕ t and enables more efficient inference utilizing Rao-Blackwellization (Section 3.5).

We propose to decompose ϕ t into a dynamic stochastic process χ t ∈ R D ϕ and a static vector b ϕ ∈ R D ϕ :

The intuition is that b ϕ captures the global information of ϕ t and acts as a baseline, while χ t captures the time-variant changes of ϕ t relative to b ϕ .

We assume that χ t follows the generative process

B and N denote the Bernoulli and normal distributions, respectively. π t ∈ {0, 1} is a binary random variable that decides whether generating the current χ t as a new sample drawn from a global distribution N (0, Σ χ ), or as a continuation from the previous χ t-1 following a simple stochastic process in the form of a random walk. The intention is to allow χ t to change both continuously (when π t = 1) through the random walk and discontinuously (when π t = 0) through the global distribution, which captures the variety of possible changes of χ t in its parameter Σ χ .

We let χ t start at t = B instead of t = 0, since it controls the conditional distribution of the time series, which requires at least B observations in the past. For the initial χ B , we assume generation from N (0, Σ χ ) as well. Our intention is that N (0, Σ χ ) should be the distribution to generate new χ t whenever there is a drastic change in the conditional distribution of y t , so at t = B it is natural to use that distribution.

Recall that

We propose to separate χ t along the dimensions of y t into D y groups. For each i = 1, . . . , D y , we define χ t,i ∈ R E as in Eq. 5. The final χ t is the concatenation of χ t,i for all i. The intuition is to allow the group of components of χ t modulating each dimension of y t to change independently of the others, corresponding to the conditional independence assumption we made in Section 3.2. We can thus sample a subset of dimensions of y t in each iteration during training to scale to high-dimensional time series. Our full model is shown in Figure 2.

## Learning

All parameters of the conditional distribution model and the prior, i.e., {ψ, b ϕ , λ, Σ χ , Σ ϵ }, are learned by fitting the model to the historical training data {(y t , x t )} T t=1 . We train our model by maximizing the marginal log-likelihood, where the latent variables χ t are marginalized out. Given a trajectory of χ B:T , the conditional log-likelihood is log p(y B+1:T |y 1:B , x 1:T , χ B:T ) = T t=B+1 log p(y t |y t-B:t-1 , x t-B:t , χ t ).

(6) Since the integral is intractable, we instead introduce a variational distribution q(χ B:T ) and maximize the following variational lower-bound L of the log-likelihood in Eq. 7:

Based on the conditional independence structure of the prior process, we construct the variational distribution q(χ B:T ) similar to an autoregressive process. However, we assume a simple normal distribution at each time step for efficient sampling and back-propagation. First, we define q(χ B ) as a normal distribution. Then, conditioning on the previous χ t-1 , we recursively define

where a t , m t , s t ∈ R D ϕ are variational parameters. Intuitively, a t is a gate that chooses between continuing from the previous χ t-1 , with noise N (0, diag(s 2 t )), and using a new distribution N (m t , diag(s 2 t )). We note that both terms in Eq. 8 factorize over time t = B + 1, . . . , T ,

where, to simplify notation, we define p(χ t |χ t-1 ) at t = B to be p(χ B ), and similarly for q. The expectations in this equation can be evaluated by Monte-Carlo sampling from q(χ) with the reparameterization trick (Kingma & Welling, 2013) for back-propagation.

In practice, sequential sampling in the autoregressive posterior could be inefficient because the sampling cannot be parallelized. We further develop a generalized posterior by replacing the autoregressive chain with multiple moving-average blocks combined with autoregressive dependencies between consecutive blocks, where sampling within each block can be carried out in parallel. Specifically, for the i-th time block, t

in parallel across t and compute

This generalizes the autoregressive posterior and is the form used in our experiments.

Utilizing our modeling assumptions from Section 3.2 and Section 3.3, we develop an SGD-based optimization protocol suitable for large datasets. Specifically, we alternate between optimizing the conditional distribution model and the prior and posterior of the dynamic model with different sampling strategies to accommodate high dimensionality and long time spans. See Appendix A for more details about our optimization process.

## Forecasting

At test time, we are given past observations y 1:T as well as input features x 1:T +H , including H future steps, to infer the conditional distribution p(y T +1:T +H |y 1:T , x 1:T +H ). We note again that x T +1:T +H only contains information known ahead, such as day of the week. Based on our modeling assumptions, the conditional distribution can be computed as p(y t |y t-B:t-1 , x t-B:t , χ t ). ( 14)

The second factor in the integrand can be further factorized into

We use Rao-Blackwellized particle filters (Doucet et al., 2000) to infer p(χ T |y 1:T , x 1:T ), so our model can keep adapting to new changes in an online manner, where the Rao-Blackwellization is possible because of our distribution assumptions made in the previous sections. We jointly infer π t and χ t , with particles representing 

# Experiments

We compare our approach with 2 univariate and 9 multivariate time series models on synthetic (Section 4.1) and real-world (Section 4.2 and 4.3) datasets; see Table 1 for an overview, including references to the relevant literature and implementations. We note that DeepVAR is also called Vec-LSTM in previous works (Salinas et al., 2019;Rasul et al., 2021b). For our own model we consider two variants: an ablated model without the ✓ ✓ ✓ ✓ GluonTS GP-Copula (Salinas et al., 2019) ✓ ✓ ✓ GluonTS LSTM-MAF (Rasul et al., 2021b) ✓ ✓ ✓ PyTorchTS TimeGrad (Rasul et al., 2021a) ✓ ✓ ✓ PyTorchTS TACTiS (Drouin et al., 2022) ✓ ✓ ✓ Authors'4 NS Tranformer (Liu et al., 2022) ✓ ✓ ✓ TSlib5 (Wu et al., 2022) DeepTime (Woo et al., 2023) ✓ ✓ ✓ Authors'6 Koopa (Liu et al., 2023) ✓ ✓ ✓ TSlib dynamic updates to the conditional distribution described in Section 3.3 (StatiConF); and our full model including those contributions (DynaConF). In both cases we experiment with different encoder architectures.

For synthetic data, we use either a two-layer MLP with 32 hidden units (*-MLP) or a point-wise linear + tanh mapping (*-PP) as the encoder. For real-world data, we use an LSTM as the encoder.

## Experiments on Synthetic Data

Datasets For our experiments on synthetic data we simulate four conditionally non-stationary stochastic processes for T = 2500 time steps, where we use the first 1000 steps as training data, the next 500 steps as validation data, and the remaining 1000 steps as test data: (AR(1)-Flip) We simulate an AR(1) process, y t = w t y t-1 + ϵ t , ϵ t ∼ N (0, 1), but resample its coefficient w t from a uniform categorical distribution over {-0.5, +0.5} every 100 steps to introduce non-stationarity. (AR(1)-Dynamic) We simulate the same process as above but now resample w t from a continuous uniform distribution U(-1, 1) every 100 steps. (AR(1)-Sin)

We simulate the same process as above but now resample w t according to w t = sin(2πt/T ). Different from the two processes above, this process has a continuously changing non-stationary conditional distribution with its own time-dependent dynamics. (VAR(1)-Dynamic) This process can be viewed as a multivariate generalization of AR(1)-Dynamic and is used in our comparisons with multivariate baselines. We use a four-dimensional VAR process with an identity noise matrix. Similar to the univariate case, we resample the entries of the coefficient matrix from a continuous uniform distribution U(-0.8, 0.8) every 250 steps.

In addition, we ensure the stability of the resulting process by computing the eigenvalues of the coefficient matrix and discard it if its largest absolute eigenvalue is greater than 1.

Experimental Setup For univariate data (AR(1)-Flip/Sin/Dynamic), we compare our approach with the univariate baselines DeepAR and DeepSSM. For multivariate data (VAR(1)-Dynamic), most baselines are redundant because their focus is on better observation models, while the underlying temporal backbone is similar. Since our synthetic observation distributions are simple, we compare with two model families that differ in their temporal backbone: DeepVAR (RNN backbone) and TransformerMAF (Transformer backbone). We use a lookback window size of 200 to give the models access to the information needed to infer the current parameter of the true conditional distribution. We tried increasing the window size to 500 on VAR(1)-Dynamic but did not see performance improvements. We also removed the unnecessary default input features of these models to prevent overfitting. Further details about our setup can be found in Appendix B.

For evaluation we use a rolling-window approach with a window size of 10 steps. The final evaluation metrics are the aggregated results from all 100 test windows. We report the mean squared error (MSE) and continuous ranked probability score (CRPS) (Matheson & Winkler, 1976), a commonly used score to measure how close 

# Results

The results on synthetic data are shown in Table 2. For univariate data, our full model (DynaConF) outperforms its ablated counterpart (StatiConF) consistently across datasets and encoders, validating the importance of our dynamic adaptation to non-stationary effects. DynaConF-PP is also superior to all univariate baselines, with its closest competitor DeepAR-10 behind by an average of 5.6% (CRPS). Furthermore, we note that our model with the pointwise encoder tends to outperform the MLP encoder, both for the ablated and full model. For multivariate data we observe similar trends. Here, our full model (DynaConF-PP) performs 24.3% (CRPS) better than the ablated model (StatiConF-PP) and 22.6% (CRPS) better than the best-performing baseline (DeepVAR-160). Since for synthetic data we also have access to the ground-truth models, we include the corresponding scores as references and upper bounds in terms of performance.

Figure 3 shows qualitative results of our model on AR(1)-Flip/Sin/Dynamic. Note that because the encoder in our model is non-linear, the encoding z t that is combined with ϕ t is not the same as y t-1 , so the inferred ϕ t may not match the sign/scale of w t , although the predictions based on ϕ t and z t can still stay close to y t = w t y t-1 + ϵ t , e.g., if the signs of z t and y t-1 are flipped, and the signs of ϕ t and w t are also flipped. Nonetheless, we can clearly see how ϕ t differs qualitatively according to w t : gradual changes (Figure 3b) vs. sudden jumps (Figure 3a and Figure 3c) as well as jumps to previous values (Figure 3a) vs. new values (Figure 3c). Furthermore, since our model only sees data for t < 1000 during training, it is remarkable that it can adapt to unseen changes for t ≥ 1000 (Figure 3b and Figure 3c).

# Datasets and Setup

We evaluate the proposed method on 6 widely-used datasets7 with published results (Lai et al., 2018;Salinas et al., 2019)  Note that because the encoder in our model is non-linear, the encoding z t that is combined with ϕ t is not the same as y t-1 , so the inferred ϕ t may not match the sign/scale of w t , but we expect it to change gradually or suddenly according to w t . splits and input features, such as time of the day, as previous works with published code and results (Salinas et al., 2019;Rasul et al., 2021b;a), from which we also retrieved the performance of the baselines. For our method, we first train StatiConF and then reuse its learned encoder in DynaConF, so the optimization of DynaConF is focused on the dynamic model. Our models use a two-layer LSTM with 128 hidden units as the encoder, except for the 8-dimensional Exchange data, where the hidden size is 8. We stress again that, different from DeepVAR or LSTM-MAF, we use LSTM as an encoder of (y t-B:t-1 , x t-B,t ) only, so we actually "restart" it at every time step. More details of our hyperparameters can be found in Appendix C.

# Results

The results are shown in Table 3 and4. We note that CRPS is only applicable to the probabilistic forecasting methods. As we can see, the relative performance of each method differs across datasets and evaluation metrics. This shows that different models may benefit from dataset-specific structure in different ways. However, DynaConF achieves the best or closest-to-the-best performance more often than the baselines.

Where it does not outperform, its performance is consistently competitive. We also note that our full model (DynaConF), which adapts to changes in the conditional distribution, performs either similarly or better than our ablated model (StatiConF), which itself differs from the baselines due to its explicit modeling of time-invariant conditional distributions. Full results including standard deviations can be found in Appendix F. 

## Experiments on Real-World Data -Set 2

Datasets and Setup We further evaluate our method against state-of-the-art baselines on two more publicly available datasets: (Walmart)11 weekly sales of 45 Walmart stores from February 2010 to October 2012; (Temperature)12 monthly average temperatures of 1000 cities from January 1980 to September 2020. We use the last 10% of the training time periods as validation sets to tune the hyperparameters for all models. For additional details about the experiment setup we refer to Appendix D.

# Results

The results are shown in Table 5 and6. On these datasets, DynaConF shows a clear advantage over the baselines in terms of both CRPS and MSE (except TACTiS on Temperature). We believe this is mainly due to more significant changes in the conditional distributions of the time series in Set 2, a hypothesis which is also supported by the superior performance of DynaConF compared to the ablated StatiConF model. It is also worth noting that the best-performing baseline models across Set 1 and Set 2 are different, while the proposed model performs more consistently. Combined with the results in the previous section, we conclude that DynaConF performs competitively if the conditional distribution remains relatively stable but outperforms the baselines if the conditional distribution does undergo dynamic changes, in line with its design and ability to account for such changes. 

# Limitations

Our model currently has the following limitations: (1) since the variational posterior model complexity scales in O(T ), it could be challenging to train the model on extremely long time series; and (2) we used a simple observation distribution family in this work to allow efficient inference, but there are cases where this may impact performance. For future work, it would be interesting to develop new variational posteriors and training algorithms that can scale better and more flexible inference algorithms that can deal with more complex observation distributions.

# Conclusion

In this work, we addressed the problem of modeling and forecasting time series with non-stationary conditional distributions. We proposed a new model, DynaConF, that explicitly decouples the time-invariant conditional distribution modeling and the time-variant non-stationarity modeling. We designed specific architectures, developed new types of variational posteriors, and employed Rao-Blackwellized particle filters to allow the model to train efficiently on large multivariate time series and adapt to unseen changes at test time. Results on synthetic and real-world data show that our model can learn and adapt to different types of changes (continuous or discontinuous) in the conditional distribution and performs competitively or better than state-of-the-art time series forecasting models.

# A Optimization Procedure

In contrast to existing time series models, we utilize a flexible variational posterior with a large number of parameters in the order of O(T ) and a structured prior model to account for conditional distribution changes over time. However, jointly optimizing over these variational parameters and the parameters in the conditional distribution model itself using stochastic gradient descent can be prohibitively demanding on the computational resources, especially GPU memory. Instead, we propose an alternative optimization procedure to learn these parameters.

Specifically, instead of optimizing by stochastic gradient descent (SGD) over all parameters in both the conditional distribution model and the prior and variational posterior model, we propose to learn the model by alternating the optimization of the parameters in the conditional distribution model and the prior and variational posterior models. For the former, we condition on the samples from the current posterior model while optimizing the conditional distribution model on randomly sampled sub-sequences from the time series using SGD. For the latter, we fix the conditional distribution model, sample from the variational posterior model over the entire time series either sequentially or in parallel, depending on the variational posterior model we use, and compute the loss using the samples through the conditional distribution, prior, and posterior models. Then we perform an update on the prior and posterior model parameters using the gradient from the loss.

When the time series is high-dimensional and GPU memory becomes a constraint during training, we randomly sample a subset of observation dimensions for each batch, since the loss decomposes over the observation dimensions in our model.

For our models, we use Adam (Kingma & Ba, 2014) as the optimizer with the default initial learning rate of 0.001 unless it is chosen using the validation set. The dimension of the latent vector z t,i (see Section 3.2) is set to E = 4 across all the experiments.

# B Synthetic Data: Details and Hyperparameters

On synthetic datasets, we use the validation set to early stop and choose the best model for both the baselines and our models. We perform 50 updates per epoch. We use 32 hidden units for our 2-layer MLP encoder. For the baselines, we report their results with different hidden sizes, including the default ones.

We keep most baseline hyperparameters to their default values but make the following changes to account for properties of our synthetic data: (1) To reduce overfitting, we remove any unnecessary input features from the models and use only past observations with time lag 1 as input. (2) To allow the models to adapt to changes in the conditional distribution we increase the lookback window size to 200. This allows the models to see enough observations generated with the latest ground-truth distribution parameters, so the models have the necessary information to adapt to the current distribution. For VAR(1)-Dynamic, we also tried extending it to 500, but it did not improve the performance. (3) DeepSSM allows modeling of trend and seasonality, but since our synthetic data do not have those, we explicitly remove those components from the model specification to avoid overfitting; (4) DeepVAR allows modeling of different covariance structures in the noise, such as diagonal, low-rank, and full-rank. Since our synthetic data follow a diagonal covariance structure in the noise, we explicitly specify it for DeepVAR.

# C Real-World Data -Set 1: Details and Hyperparameters

On real-world datasets with published results, we use the last 10% of the training time period as the validation set and choose the initial learning rate, number of training epochs, and model sizes using the performance on the validation set for StatiConF. After training StatiConF, we reuse its encoders in DynaConF, so it only needs to learn the dynamic model. For DynaConF, we use the same validation set to choose the number of training epochs and use 0.01 as the initial learning rate.

Because of the diversity of the real-world datasets, we further apply techniques to stablize training. Specifically, for all datasets, we use the mean and standard deviation to shift and scale each dimension of the time series.

For Exchange, we use the mean and standard deviation of the recent past data in a moving lookback window. For the other datasets, we simply use the global mean and standard deviation of each dimension computed using the whole training set. In all cases, for forecasting, the output from the model is inversely scaled and shifted back for evaluation. These design choices were made based on the performance on the validation sets.

On real-world datasets, extreme values or outliers may cause instability during training. We optionally apply Winsorization using the quantiles (0.025 and 0.975) computed from the recent past data in a moving lookback window on Traffic and Wikipedia. The decisions of whether to apply this transformation were based on the results on the validation sets.

For TACTiS, NS Transformer, DeepTime, and Koopa, we use the same hyperparameters as in their recommended settings for similar datasets from their published results. For the other baselines, the results are retrieved from previous publications (Rasul et al., 2021a;b).

# D Real-World Data -Set 2: Details and Hyperparameters

On the Walmart and Temperature datasets, the experiment setup is the same for all the models. For Walmart, the forecast window size is 4 weeks, and the test set consists of the last 20 weeks. For Temperature, the forecast window size is 3 months, and the test set consists of the last 24 months. We found it helpful to normalize the time series using the means and standard deviations computed from the training set for each dataset for stabilizing training, especially for LSTM-MAF and TransformerMAF. We use the last 10% of the training time period as the validation set to tune the hyperparameters, including the model size (32,128,512,2048) and initial learning rate (0.01, 0.001), and for early stopping for our models and the first 5 baseline models, which share similar encoder architectures as ours. For the baseline models, we also use it to choose whether to apply marginal transformation (Salinas et al., 2019) and mean scaling (Salinas et al., 2020). Out of all the baseline models, we found NS Transformer, DeepTime and Koopa to be sensitive to the lookback window size, which we tuned across a regular grid of multipliers of the forecast window size. For the other baselines, we found that in many cases increasing the window size resulted in worse validation performance compared to using the default size. In the other cases, it resulted in small improvements on the validation set but similar or worse performance on the test set. For consistency, we settled on using the same default lookback window size.

# E Details on Evaluation

We run all experiments for three different random seeds independently and calculate and report the mean and standard deviation of each evaluation metric for each model. On synthetic datasets, we use 1000 sample paths to empirically estimate the predicted distributions for all models. On real-world datasets, we use 100 sample paths.

We use two evaluation metrics: mean squared error (MSE) and continuous ranked probability score (CRPS) (Matheson & Winkler, 1976). Assume that we observe y at time t but a probabilistic forecasting model predicts the distribution of y to be F . MSE is widely used for time series forecasting, and for a probabilistic forecasting model, where the mean of the distribution is used for point prediction, it is defined as

for a single time point t and averaged over all the time points in the test set.

CRPS has been used for evaluating how close the predicted probability distribution is to the ground-truth distribution and is defined as

for a single time point t and averaged over all the time points in the test set, where I denotes the indicator function. Generally, F (z) can be approximated by the empirical distribution of the samples from the predicted distribution. Both MSE and CRPS can be applied to multivariate time series by computing the metric on each dimension and then averaging over all the dimensions.   

# F Additional Experiment Results

Table 7, 8, 9, and 10 show the full CRPS and MSE results of the baselines and our models on the univariate and multivariate processes respectively. Table 11 and 12 show the full CRPS and MSE results of our models with means and standard deviations on the real-world datasets. The results of the first 5 baselines on the real-world data -set 1 are from (Rasul et al., 2021a;b).

# G Qualitative Comparison of DynaConF and StatiConF

Here we show some qualitative comparison of DynaConF and StatiConF predictions to highlight the differences in their forecasting behaviors when facing changes in the distribution. Specifically, we compare their predictions on one dimension from the Electricity dataset, where there appears to be a structural change in the time series at test time. As we can see in Figure 4, as the forecast window keeps moving forward, DynaConF quickly adapts to the new distribution, while StatiConF struggles to react. We note that the encoder is shared between these two models, so the differences come from the non-stationary model part.  

