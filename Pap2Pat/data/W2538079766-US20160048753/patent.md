# DESCRIPTION

## STATEMENT OF GOVERNMENT SPONSORED SUPPORT

This invention was made with Government support under contracts 8DP1HD075623-04, R01NS076460 awarded by the National Institutes of Health, and under contract N66001-10-C-2010 awarded by the Defense Advanced Research Projects Agency. The Government has certain rights in the invention.

## FIELD OF THE INVENTION

This invention relates to decoders for brain machine interfaces.

## BACKGROUND OF THE INVENTION

Brain-machine interface (BMI) systems convert neural signals from motor regions of the brain into control signals to guide prosthetic devices. The ultimate goal of BMIs is to improve the quality of life for people with paralysis by providing direct neural control of prosthetic arms or computer cursors. While considerable research over the past 15 years has led to compelling BMI demonstrations, there remain several challenges to achieving clinically viable BMI systems. In this invention, we focus on the challenge of increasing BMI performance and robustness.

## SUMMARY OF THE INVENTION

The present invention provides a brain machine interface (BMI) to control a device. The BMI has a neural decoder, which is a neural to kinematic mapping function with neural signals as the input to the neural decoder and kinematics to control the device as the output of the neural decoder. The neural decoder is based on a continuous-time multiplicative recurrent neural network, which has been trained as a neural to kinematic mapping function. The device to be controlled could be a robotic arm, a prosthetic device or a cursor on a computer screen.

In one embodiment, the outputted kinematics could be normalized position over time and velocity over time.

In another embodiment, the neural training data used for training of the neural to kinematic mapping function has been modified. The neural training data could, for example, be modified by randomly adding and removing spikes such that the mean number of spikes is preserved on average.

In yet another embodiment, the neural decoder could have been trained with neural and kinematic data sets collected over multiple days.

In yet another embodiment, the neural decoder could have been trained with neural and kinematic data sets collected over five or more days.

Embodiments of the invention offer the following advantages:

1. State of the art robustness to variations and perturbations in the day-to-day and moment-to-moment neural data. This robustness may help to enable the clinical use of BMIs.

2. State of the art performance of the neural decoder.

3. The ability to improve the decoder by using data from previous days, something the previous decoders were unable to do.

## DETAILED DESCRIPTION OF THE INVENTION

The present invention also referred to as Big-Data Multiplicative Recurrent Neural Network (BD-MRNN) is a supervised neural network and training method for incorporating and modifying multiple previous days training datasets (historical data) to improve both raw performance and robustness in the daily operation of brain-machine interface (BMI) decoders.

### MRNN Definition

The generic recurrent network model is defined by an N-dimensional vector of activation variables, x, and a vector of corresponding “firing rates”, r=tan h(x). Both x and r are continuous in time and take continuous values. In a standard RNN model, the input affects the dynamics as an additive time-dependent bias in each dimension. In the MRNN model, the input instead directly parameterizes the weight matrix, allowing for multiplicative interactions between the input and the hidden state. One view of this multiplicative interation is that the hidden state of the recurrent network is selecting an appropriate decoder for the statistics of the current dataset. The equation governing the dynamics of the activation vector is of the form suggested in Suskever 2011, but adapted for this invention to continuous time

τ{dot over (x)}(t)=−x(t)+Ju(t)r(t)+bx.  (0.1)

The N×N×F tensor Ju(t) defines the values of the recurrent connections of the network, which are dependent on the I-dimensional input, u(t). In the MRNN, Ju(t) is factorized such that the input is linearly combined into F factors. Specifically, Ju(t) is factorized according to

Ju(t)=Jxf·diag(Jfuu(t))·Jfx,  (0.2)

where Jxf has dimension N×F, Jfu has dimension F×I, Jfx has dimension F×N, and diag(v) takes a vector, v, and returns a diagonal matrix with v along the diagonal. One directly controls the complexity of interactions by choosing the number of factors, F. If F=N2, we recover a full N×N×N tensor. If F=1, Ju(t) is a rank-one matrix whose singular value is function of u(t).

Finally, the network has a constant bias, bx, and the neuronal time constant, T, sets the time scale of the network.

### MRNN Output Definition

The output of the network is a weighted sum of the network firing rates plus a bias, defined by

z(t)=WOTr(t)+bz,  (0.3)

where WO is an N×M matrix and bz is an M-dimensional bias.

### Network Construction for Cursor BMI Decoder

The network equations defined above are used according to the following procedures and parameters in order to build the BD-MRNN BMI decoder.

### MRNN Initialization

For our online experiments, the size of the networks are set to N=100 and N=50 with F=N in both cases (see Table 1). One subject uses a single multi-unit electrode arrays (I=96), while the second uses two (I=192). The non-zero elements of the non-sparse matrices Jxf, Jfu, Jfx are drawn independently from a Gaussian distribution with zero mean and variance gxf/F, gfu/I, and gfx/N with gxf, gfu, and gfx defined in Table 1 for the specific BMI task. The elements of WO are initialized to zero, and the bias vectors bx and bz are also initialized to 0.

### Concatenating Neural Trials for Seeding the MRNN During Training

The input u(t), to the MRNN, is the vector of binned spikes measured from neural data (see, for example, Sus sillo 2012 for details on standard preprocessing of neural signals, see Δt in Table 1 for bin sizes). By input to the MRNN, we mean in the sense of equation 0.1. This results in a data matrix, Uj, of binned spikes of size I×Tj for each actual trial, where Tj is the number of time steps for the jth trial. Five actual trials are then concatenated together to make one “training” trial. The first two actual trials in a training trial are used for seeding the hidden state of the MRNN, and are not used for learning, whereas the final 3 actual trials in the training trial are used for learning. In this way, excepting the first two actual trials in the day's dataset, the entire set of actual trials are used for learning, by incrementing the actual trial index that begins a training trial.

### Perturbing the Neural Input During Training

A key element of training robustness to nonstationarities in the neural code is the introduction of perturbations to the neural spike trains that are used to train the MRNN. The concatenated input in a given training trial, Û=[Ui, . . . , Ui+4] are perturbed by adding and removing spikes from each channel. We focus on channel c of the jth training trial, i.e., a row vector of data, Ûc,:j. Let the number of spikes in Ûc,:j be ncj before perturbation. This number is perturbed according to

{circumflex over (n)}cj=ηjηcncj,  (0.4)

where both ηj and ηc are Gaussian variables with a mean of one and standard deviations of σtrial and σchannel, respectively (see Table 1). Conceptually, ηj models a global modulation in the array across all channels (e.g. changes in subject arousal), while ηc models channel by channel perturbations, such as uncontrolled channel dropping or moving baselines in individual neurons. If ncj is less than zero or greater than 2ncj, it is resampled according to equation 0.4, which keeps the average number of perturbed spikes in a given channel and training trial the same as the average number of unperturbed spikes in the same channel and training trial. Otherwise, if {circumflex over (n)}cj is greater than ncj, then {circumflex over (n)}cj−ncj spikes are added to random time bins of the training trial. If {circumflex over (n)}cj is less than ncj, then ncj−{circumflex over (n)}cj spikes are randomly removed from time bins of the training trial that already had spikes. Finally, if {circumflex over (n)}cj=ncj, nothing is changed.

The process of perturbing the binned spiking data occurs on every iteration of the optimization algorithm. For example, in a batch gradient descent algorithm, the perturbation described by equation 0.4 happens after each update of the network parameters.

### Using Many Days Training Data

The typical methodology for training a closed-loop BMI decoder involves training on a session-by-session basis. This means that every day, the subject engages in a control task, for which both input (neural) and supervisory (kinematics) signals are collected. After this session-by-session training period, a BMI is optimized to perfrom well on this data exclusively.

The second critical component to acheiving both performance and robustness in the BD-MRNN decoder is using many days of training data. In our laboratory experiments, we use multiple years of training data (see Table 1). Because of the extreme nonstationarities of the neural data, this aspect of the BD-MRNN training methodology is unintuitive. The nonlinear, multiplicative architecture of the MRNN utilizes the regularities that across many days do exist in a dataset comprising many days. In comparison, the (due to BD-MRNN, no longer) state-of-the-art linear Kalman Filter methods, including previous days data would result in potentially very poor decoders.

### Network Output

We train two MRNN networks to each output a 2-dimensional signal. One network is trained to output the normalized position through time in both the horizontal (x) and vertical (y) spatial dimensions. The other MRNN is trained to output the velocity through time, also in the x and y dimensions. We calculate the hand velocities from the positions numerically using central differences.

Since the MRNN decoder outputs both normalized position and velocity, we combine both for our final decoded position signal. The decode used during BMI mode, dx(t), dy(t) is a mix of both velocity and position, defined by

dx(t)=β(dx(t−Δt)+γvνx(t−Δt)Δt)+(1−β)γppx(t)  (0.5)

dy(t)=β(dy(t−Δt)+γvνy(t−Δt)Δt)+(1−β)γppy(t)  (0.6)

where vx, vy, px, py are the normalized velocity and positions in the x and y dimensions and γv, γp are factors that convert from the normalized velocity and position, respectively, to the physical values associated with the workspace. The parameter β sets the amount of velocity vs. position decoding (see Table 1).

### Training and Running the Networks

A network is simulated by integrating equation 0.1 using the Euler method at a time step of Δt=τ/5 and then evaluating equation 0.3.

The parameters of the network are trained offline to reduce the averaged squared error between the measured kinematic training data and the output of the network, z(t). Specifically, we use the Hessian-Free (HF) optimization method for RNNs (but adapted to the continuous-time MRNN architecture). HF is an exact 2nd order method that uses back-propagation-through-time to compute the gradient of the error with respect to the network parameters. The set of trained parameters is {Jxf, Jfu, Jfx, bx, bz}. The HF algorithm has some critical parameters, such as the minibatch size, the initial lambda setting, and the max number of CG iterations. We set these parameters to ⅕ times the total number of trials, 0.1, and 50, respectively.

After training, the networks are copied into the embedded real-time environment (xPC), and run in closed-loop, to operate online in BMI mode. Specifically, at each time point the RNN module receives binned spikes and outputs the current estimate of the hand position, which is used to display the cursor position on the screen. During BMI mode the neural spikes are not perturbed in any way. The values vx(0) and vy(0) are initialized to 0, as is the MRNN hidden state.

**Model Parameters**

The parameters of the model of an exemplary embodiment are listed in Table 1.

**Remark on the Use of Multiple Days of Training Data**

One critical aspect of the invention is using multiple days of training data. At first glance, it may seem straightforward that more data should always improve the quality of performance on some supervised system, such as a neural network. However, this is only true under a very specific and very commonly met assumption. This assumption is *not* met in the BMI setting. The assumption is that the data used to optimize (“train”) the neural network comes from the same distribution as the data used in the network during operation (during so-called “validation” or “testing”). When this assumption is met, indeed more training data leads to a better neural network that performs better on generalization testing. To reiterate, this assumption is *not* met in the neural data used to train BMIs.

As an example analogous to the BMI setting, imagine that we are interested in building a neural network to classify hand written letters from different users. Specifically, we want to classify different users based on how they write the letter ‘h’ (e.g. user 1 wrote these ‘h’ letters, while user 2 wrote those ‘h’ letters.) If our dataset contained only handwritten ‘h’ letters, then adding more and more ‘h’ letters would definitely improve our classification of user 1 from user 2, as per common understanding. However, imagine that we had access to other letters that the users wrote, such as ‘n’, and ‘x’. If our job is only to classify different users based on the letter ‘h’, then it appears that including ‘x’ as training data to an ‘h’ classifier could only hurt the it's performance on classifying the letter ‘h’.

However, you could also reason that if you included ‘n’ in your ‘h’ classifier, perhaps one could still improve the classifier because the letter ‘n’ shares some common features with the letter ‘h’. It's not at all clear what would happen if we threw in the letters from ‘a’ to ‘z’. We can summarize that adding more training data (letters different from ‘h’), when the data does not come from the test distribution (‘h’ letters), will not obviously help improve the network's performance.

The previous example is analogous to current situation in BMI research. We would like to classify different user intentions, such as moving a computer cursor up or down (analogous to classifying user 1 or user 2) based on neural data (the letters). However, each day the neural data upon which we classify changes dramatically (some days we have ‘h’ letters to classify user 1 vs user 2, some days we have ‘x’ letters). Further, the changes in neural data are not under our control. So we never know whether we are going to be looking at an ‘h’ or an ‘x’ or a ‘n’. If it's an ‘h’ day, than using a previous ‘x’ day seems like a bad idea.

It is a fact, in the BMI setting, the neural data collected using modern devices (e.g., Utah multi electrode array) varies dramatically from day-to-day, even when the subject is requested to perform the exact same task, and the experimental conditions are reproduced to as exacting conditions as the experimental environment will allow. It is unclear why the neural data varies so dramatically, although many believe it is a combination of the underlying complexities of the neural code, combined with the inevitable limitations of reading biological electrical signals with limited silicon-based hardware.

The variation in neural signals has led to the widely held view in the BMI field that using data from multiple days is in fact quite problematic. As a result, the standard—and state of the art—practice is to record training data each and every day, and perhaps more than once a day. This training data is then used to run a BMI decoder for some amount of time on that same day. Anecdotally, many researchers have tried to incorporate more data than just a single day, though it is widely held as a bad idea because it often fails to improve things. Sometimes using yesterday's data as well as today's data improves things, sometimes it does not. Surely using data from over 1 month ago is a bad idea to include in a training set for today's BMI decoder.

These widely held views about which data to use for training a closed-loop BMI decoder are based primarily on using a linear decoding method, the Kalman filter. As a linear method, the Kalman filter can only give an average response to many days of training data, so if neural data from one month ago is indeed different from today's neural data, indeed the Kalman filter trained using the old data will result in a very poor decoder on new data from today. Thus the vast majority of experts (likely all) in the field would consider it non-straightfoward to devise a method whereby previous data from three to six months ago, as we have shown empirically, is helping to decode today's neural data.

For our invention, we made a systematic study of how one day's neural data compares to another day's. We did this using an analysis technique called the principal subspace angle. The scientific result of this analysis is that some days are more similar to others, while some days are very different. Further, similar neural data tends to come in blocks of time, but oddly, data from many months ago can be quite similar to today's neural data (the exact similarity structure is beyond the scope of this introduction). Naturally, it would be desirable to use only training data from days that are similar to the day on which you were interested in running the decoder (use ‘n’s and not ‘x’s to help classify the users 1 and 2 based on how they write the letter ‘h’). However, it is very hard to know, a priori, which days will help.

To sidestep this problem, we used a highly nonlinear decoder, a multiplicative recurrent neural network (MRNN). The MRNN is powerful enough to handle the varying neural data from many days, even when the neural data is significantly different from day to day. So long as there are some similarities in the neural data between days (e.g. a ‘n’ similar to an ‘h’), the MRNN is smart enough to use this data to improve the BMI decode. If the training data bears little similarity to today's neural data (‘x’ letters are not similar to ‘h’ letters), the MRNN is smart enough to ignore it while decoding today's neural data.

Embodiments of the invention could be envisioned as a brain machine interface controlling a device such as a robotic arm, a prosthetic device or a cursor on a computer screen. The brain machine interface receives neural signals from a subject's brain, which are processed by one or more neural decoders. The neural decoders are either functionalized with method steps to execute the signal processing steps and/or are hardware systems for processing the neural signals as described herein. The neural decoders could include computer hardware and software devices/technology for its operation(s). The neural decoders are interfaced with the device to control the kinematics of the device based on the processed neural signals.

