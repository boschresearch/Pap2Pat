# DESCRIPTION

## TECHNICAL FIELD

The present invention relates to the field of brain-computer interface application research, and in particular relates to a brain-computer interface based robotic arm self-assisting system and method.

## BACKGROUND ART

There are many seriously paralyzed patients in the world who can only do some of the activities necessary for daily life, such as drinking water, by getting help from others. With the continuous development of the artificial intelligence and robot technology, and more and more research findings have been applied to assist such people in order to improve their quality of life, in which the field of Brain Computer Interface (BCI), as one branch of the field of neural engineering, is developing rapidly and has a wide prospect, which has aroused people's research upsurge in the field of brain-computer interface.

Brain-computer interface (BCI) is a new human-machine interaction technique that enables direct communication between a human brain and a computer without the conventional brain output pathway (peripheral nerves and muscle tissues), providing paralyzed patients with a new way to exchange and control information with the outside world. The BCI system may be an invasive system or a non-invasive system, the invasive system will implant electrodes into the skull, and the non-invasive system will only collect scalp electroencephalogram signals. Since the non-invasive brain-computer interface has no need for surgery and is safer and simpler than an invasive system. With the continuous improvement of signal processing methods and techniques, the processing of scalp electroencephalogram (EGG) has reached a certain level, so that it is possible for the brain-computer interface to come into practical application in life. The present invention uses a non-invasive brain-computer interface technique.

At present, some existing researches have attempted to combine the brain-computer interface technique with a robot technique. In the Chinese patent application with the publication number CN 102198660 A, entitled “A brain-machine interface based robotic arm control system and action command control scheme ( )”, in which a brain-computer interface based on motor imagery realizes control by eight commands, including moving up, moving down, moving left, moving right, moving forward, moving backward, finger grasp and finger release, of the robotic aim. The Chinese patent application with the publication number CN 102309365 A, entitled “A wearable brain-controlled intelligent prosthesis ( )”, realizes wearable detection and calculation for electroencephalogram detection and identification, and combines with the intelligent sensing technique to achieve precise adaptive intelligent control for a prosthesis, so as to improve the efficiency and accuracy of movement of the prosthesis and ideally implement the functions of a human hand In the Chinese invention patent with the publication number CN 105425963 A, entitled “A system of electroencephalogram-controlled robotic aim ( )”, electroencephalogram signals are used to acquire parameters of attention and relaxation to implement preset movements of a robotic aim.

In the invention patents described above, only some simple or even preset robotic aim movement controls are implemented through electroencephalogram signals, which does not take full use of the features and advantages of the combination of the brain-computer interface and the robotic aim self-determination control technique. The brain-computer interface based robotic aim self-assisting system and method can combine the advantages of both the brain-computer interface and the robotic aim, and better utilize the brain-computer interface to improve the quality of life of paralyzed patients and improve their ability to live independently.

## SUMMARY OF THE INVENTION

In view of the above deficiencies of the prior art, an object of the present invention is to provide a brain-computer interface based robotic arm self-assisting system.

Another object of the present invention is to provide a brain-computer interface based robotic arm self-assisting method.

The object of the present invention can be achieved by the following technical solution:

a brain-computer interface based robotic arm self-assisting system, which is set up based on a three-layer structure including a sensing layer, a decision-making layer and an execution layer, wherein the sensing layer comprises an electroencephalogram acquisition and detection module and a visual identification and positioning module, the electroencephalogram acquisition and detection module being used for acquiring an electroencephalogram signal and analyzing and identifying the intent of a user, and the visual identification and positioning module being used for identifying and locating positions of a corresponding cup and the user's mouth based on the user intent; the execution layer comprises a robotic arm control module, which is a carrier assisting in operation of a person in practice and performs trajectory planning and control for a robotic arm based on an execution instruction received from a decision-making module; and the decision-making layer comprises a decision-making module, which is connected to the electroencephalogram acquisition and detection module, the visual identification and positioning module and the robotic arm control module to implement acquisition and transmission of data, such as an electroencephalogram signal, a located position and a robotic arm status, and the sending of the execution instruction for the robotic arm.

Preferably, the electroencephalogram acquisition and detection module comprises an electrode cap for electroencephalogram acquisition, an electroencephalogram acquisition device and a first computer, wherein ten channels of “A1”, “T5”, “P3”, “PZ”, “P4”, “T6”, “O1”, “Oz”, “O2” and “A2” in the electrode cap are used and disposed at positions according to an international standard 10-20 system; and the first computer is used to implement P300 signal detection and a flickering visual stimulation of a function key in the screen, and the function keys for the flickering visual stimulation are regularly distributed in a 2*2 array in the computer screen, including function keys of “cup1”, “cup2”, “cup3” and “back”, and flicker at an interval of 200 ms with change in black and green colors in a random sequence.

Preferably, the visual identification and positioning module comprises two Microsoft Kinect vision sensors and a second computer, wherein the two Microsoft Kinect vision sensors are respectively disposed in front of a cup to be taken and in front of a user for identification and positioning of the cup to be taken and the user's mouth; and the second computer is used to implement a cup contour detection algorithm, a cup positioning algorithm, a template matching and identification algorithm, and a mouth identification and positioning algorithm

Preferably, the decision-making module implements, based on a TCP communication protocol, acquisition and transmission of data of an electroencephalogram intent, a located position and a robotic arm status and the sending of an execution instruction for the robotic arm by defining unified transmission data variables, including a user's electroencephalogram intent and the information of positions of the cup and the mouth and setting up a service code framework for a client and a server.

Preferably, the robotic arm control module uses a multi-degree-of-freedom robotic arm as an effector.

Another object of the present invention can be achieved by the following technical solution:

a brain-computer interface based robotic arm self-assisting method, comprising the steps as follows:

1) a user is sitting in front of a screen of a first computer, adjusts the position thereof, wears an electrode cap for electroencephalogram acquisition, opens an electroencephalogram acquisition device and the first computer, and confirms that the signal acquisition status is good;

2) a brain-computer interface based robotic arm self-assisting system is started to confirm that the Microsoft Kinect vision sensor used for identifying and locating the user's mouth can correctly capture the user's mouth, and confirm that three preset cups to be taken are correctly placed in the field of view of the Microsoft Kinect vision sensor used for identifying and locating the cups to be taken;

3) the screen of the first computer enters a function key interface of flickering visual stimulation, the function key interface comprising four function keys of “cup1”, “cup2”, “cup3” and “back”;

4) the user gazes at one of the three function keys “cup1”, “cup2” or “cup3”, that is, selecting one of the three preset cups, and once the function key is selected, the electroencephalogram intent of the user about the selection of the cup is obtained and sent to the visual identification and positioning module and the decision-making module;

5) the visual identification and positioning module identifies and locates the position of the corresponding cup and the position of the user's mouth based on the electroencephalogram intent in the step 4) and sends, based on the TCP communication protocol, the information of the positions of the cup selected by the user and the user's mouth to the decision-making module;

6) the decision-making module generates a corresponding execution instruction for the robotic arm based on the information of the positions of the cup and the user's mouth obtained in the step 5) and the electroencephalogram intent obtained in the step 4), and sends the corresponding execution instruction for the robotic arm to the robotic arm control module;

7) the robotic arm control module performs trajectory planning based on the execution instruction for the robotic arm and controls, based on the planned trajectory, the robotic arm to take the cup selected by the user and transfer the cup to the user's mouth;

8) after drinking water, the user gazes at the function key “back”, and once the function key is selected, the user's electroencephalogram intent about returning the cup will be obtained and sent to the decision-making module;

9) the decision-making module generates, based on the electroencephalogram intent for returning the cup obtained in the step 8), a corresponding execution instruction for the robotic arm and sends execution instruction for the robotic arm to the robotic arm control module; and 10) the robotic arm control module performs trajectory planning based on the execution instruction for the robotic arm and controls, based on the planned trajectory, the robotic arm to return the cup selected by the user to the original position and restore the initial position status of the robotic arm, so as to realize the self-assisting function of the robotic arm for assisting the user to drink water.

Preferably, selecting the function keys in the steps 4) and 8) is specifically implemented by the following process: the user gazes at a certain function key in the function key interface of the first computer, the electroencephalogram signal is acquired, amplified, filtered and processed by analog-to-digital conversion through an electrode cap and an electroencephalogram acquisition device, then the data is transferred to the first computer for P300 signal detection, and then the selection of the certain function key is implemented, the P300 signal detection being specifically implemented by the steps of:

(I) processing the EEG signal by 0.1-20 Hz bandpass filtering and noise reduction; and

(II) intercepting, with the amplitude of the EEG signal as a feature, data of a time window of 600 ms after a P300 function key flickers, and performing status classification using a Bayesian model, thereby realizing the P300 signal detection.

Preferably, in the step 5), identifying and locating the position of the corresponding cup is specifically implemented by the steps of:

(1) extracting the horizontal plane in which the cup is placed in the three-dimensional point cloud of the Microsoft Kinect vision sensor through a region growing algorithm;

(2) removing the horizontal plane extracted in the step (1), and performing extraction and segmentation for the object from the remaining three-dimensional point cloud;

(3) respectively matching, using a template matching algorithm, the color image corresponding to each object point cloud set obtained in the step (2) with preset images in a library to identify the point cloud set corresponding to the cup selected by the user; and

(4) performing average calculation for the point cloud set corresponding to the selected cup obtained in the step (3) so that the positioning for the cup in a coordinate system of the Microsoft Kinect vision sensor is implemented and converted into the positioning in a robotic arm coordinate system.

Preferably, in the step 5), identifying and locating the position of the user's mouth is specifically implemented by the steps of: performing human body detection using a software development kit provided by the Microsoft Kinect vision sensor itself so that a coordinate position of the user's mouth in a coordinate system of the Microsoft Kinect vision sensor is acquired and converted into coordinate positions in a robotic arm coordinate system.

Preferably, in the steps 7) and 10), performing trajectory planning and control for the robotic arm is specifically implemented by the process of: combining preset key trajectory points with coordinate points of the user's mouth and the selected cup in the robotic arm coordinate system to plan an operation trajectory of the robotic arm, and calling the corresponding API of the robotic arm to control the robotic arm to operate based on the planned trajectory, so as to realize the self-assisting function of the robotic arm for assisting the user to drink water.

As compared with the prior art, the present invention has the following advantages and beneficial effects:

1. In the present invention, based on the combination of the P300-based brain-computer interface technique and the assisting technique of a robotic arm with a self-controlled decision-making function, a user only needs to provide an electroencephalogram intent, and the rest, i.e., the control on the movement of a robotic arm, is implemented by the automatic planning and control of the system, thereby having a small burden on the user and being convenient for application.

2. The present invention combines the visual identification and positioning technology, a brain-computer interface and a robotic arm to realize the effect that a drink selected by a user can be placed anywhere in a certain range.

3. The present invention combines the visual identification and positioning technology, a brain-computer interface and a robotic arm to comprehensively utilize their advantages. Users can select a drink by themselves through the brain-computer interface in the system of the present invention, and then through the robotic arm in the present invention system and the visual identification and positioning technique, the drink selected by the user is positioned, identified, taken and carried to the user's mouth, so as to facilitate paralyzed patients to drink water by themselves, thereby improving the quality of life of the paralyzed patients and improving their ability to live independently.

## DETAILED DESCRIPTION OF EMBODIMENTS

Hereafter the present invention will be further described in detail in conjunction with embodiments and accompanying drawings, but the embodiments of the present invention are not limited thereto.

### Embodiment 1:

As shown in FIG. 1, this embodiment provides a brain-computer interface based robotic arm self-assisting system, which is set up based on a three-layer structure including a sensing layer, a decision-making layer and an execution layer, wherein the sensing layer comprises an electroencephalogram acquisition and detection module and a visual identification and positioning module, the electroencephalogram acquisition and detection module being used for acquiring an electroencephalogram signal and analyzing and identifying the intent of a user, and the visual identification and positioning module being used for identifying and locating positions of a corresponding cup and the user's mouth based on the user intent; the execution layer comprises a robotic arm control module, which is a carrier assisting in operation of a person in practice and performs trajectory planning and control for a robotic arm based on an execution instruction received from a decision-making module; and the decision-making layer comprises a decision-making module, which is connected to the electroencephalogram acquisition and detection module, the visual identification and positioning module and the robotic arm control module to implement acquisition and transmission of data, such as an electroencephalogram signal, a located position and a robotic arm status, and the sending of the execution instruction for the robotic arm.

The electroencephalogram acquisition and detection module comprises an electrode cap for electroencephalogram acquisition, an electroencephalogram acquisition device and a first computer, wherein ten channels of “A1”, “T5”, “P3”, “PZ”, “P4”, “T6”, “O1”, “Oz”, “O2” and “A2” in the electrode cap are used and disposed at positions according to an international standard 10-20 system; and the first computer is used to implement P300 signal detection and a flickering visual stimulation of a function key in the screen, and the function keys for the flickering visual stimulation are regularly distributed in a 2*2 array in the computer screen, including function keys of “cup1”, “cup2”, “cup3” and “back”, and flicker at an interval of 200 ms with change in black and green colors in a random sequence.

The visual identification and positioning module comprises two Microsoft Kinect vision sensors and a second computer, wherein the two Microsoft Kinect vision sensors are respectively disposed in front of a cup to be taken and in front of a user for identification and positioning of the cup to be taken and the user's mouth; and the second computer is used to implement a cup contour detection algorithm, a cup positioning algorithm, a template matching and identification algorithm, and a mouth identification and positioning algorithm.

The decision-making module implements, based on a TCP communication protocol, acquisition and transmission of data of an electroencephalogram intent, a located position and a robotic arm status and the sending of an execution instruction for the robotic arm by defining unified transmission data variables, including a user's electroencephalogram intent and the information of positions of the cup and the mouth and setting up a service code framework for a client and a server.

The robotic arm control module uses a multi-degree-of-freedom robotic arm as an effector.

### Embodiment 2

this embodiment provides a brain-computer interface based robotic arm self-assisting method, as shown in FIG. 2, the method comprising the steps as follows:

1) a user is sitting in front of a screen of a first computer, adjusts the position thereof, wears an electrode cap for electroencephalogram acquisition, opens an electroencephalogram acquisition device and the first computer, and confirms that the signal acquisition status is good;

2) a brain-computer interface based robotic arm self-assisting system is started to confirm that the Microsoft Kinect vision sensor used for identifying and locating the user's mouth can correctly capture the user's mouth, and confirm that three preset cups to be taken are correctly placed in the field of view of the Microsoft Kinect vision sensor used for identifying and locating the cups to be taken;

3) the screen of the first computer enters a function key interface of flickering visual stimulation, the function key interface comprising four function keys of “cup1”, “cup2”, “cup3” and “back”;

4) the user gazes at one of the three function keys “cup1”, “cup2” or “cup3”, that is, selecting one of the three preset cups, and once the function key is selected, the electroencephalogram intent of the user about the selection of the cup is obtained and sent to the visual identification and positioning module and the decision-making module;

5) the visual identification and positioning module identifies and locates the position of the corresponding cup and the position of the user's mouth based on the electroencephalogram intent in the step 4) and sends, based on the TCP communication protocol, the information of the positions of the cup selected by the user and the user's mouth to the decision-making module;

6) the decision-making module generates a corresponding execution instruction for the robotic arm based on the information of the positions of the cup and the user's mouth obtained in the step 5) and the electroencephalogram intent obtained in the step 4), and sends the corresponding execution instruction for the robotic arm to the robotic arm control module;

7) the robotic arm control module performs trajectory planning based on the execution instruction for the robotic arm and controls, based on the planned trajectory, the robotic arm to take the cup selected by the user and transfer the cup to the user's mouth;

8) after drinking water, the user gazes at the function key “back”, and once the function key is selected, the user's electroencephalogram intent about returning the cup will be obtained and sent to the decision-making module;

9) the decision-making module generates, based on the electroencephalogram intent for returning the cup obtained in the step 8), a corresponding execution instruction for the robotic arm and sends execution instruction for the robotic arm to the robotic arm control module; and

10) the robotic arm control module performs trajectory planning based on the execution instruction for the robotic arm and controls, based on the planned trajectory, the robotic arm to return the cup selected by the user to the original position and restore the initial position status of the robotic arm, so as to realize the self-assisting function of the robotic arm for assisting the user to drink water.

Selecting the function keys in the steps 4) and 8) is specifically implemented by the following process: the user gazes at a certain function key in the function key interface of the first computer, the electroencephalogram signal is acquired, amplified, filtered and processed by analog-to-digital conversion through an electrode cap and an electroencephalogram acquisition device, then the data is transferred to the first computer for P300 signal detection, and then the selection of the certain function key is implemented, the P300 signal detection being specifically implemented by the steps of:

(I) processing the EEG signal by 0.1-20 Hz bandpass filtering and noise reduction; and

(II) intercepting, with the amplitude of the EEG signal as a feature, data of a time window of 600 ms after a P300 function key flickers, and performing status classification using a Bayesian model, thereby realizing the P300 signal detection.

In the step 5), as shown in FIG. 3, identifying and locating the position of the corresponding cup is specifically implemented by the steps of:

(1) extracting the horizontal plane in which the cup is placed in the three-dimensional point cloud of the Microsoft Kinect vision sensor through a region growing algorithm;

(2) removing the horizontal plane extracted in the step (1), and performing extraction and segmentation for the object from the remaining three-dimensional point cloud;

(3) respectively matching, using a template matching algorithm, the color image corresponding to each object point cloud set obtained in the step (2) with preset images in a library to identify the point cloud set corresponding to the cup selected by the user; and

(4) performing average calculation for the point cloud set corresponding to the selected cup obtained in the step (3) so that the positioning for the cup in a coordinate system of the Microsoft Kinect vision sensor is implemented and converted into the positioning in a robotic arm coordinate system.

In the step 5), identifying and locating the position of the user's mouth is specifically implemented by the steps of: performing human body detection using a software development kit provided by the Microsoft Kinect vision sensor itself so that a coordinate position of the user's mouth in a coordinate system of the Microsoft Kinect vision sensor is acquired and converted into coordinate positions in a robotic arm coordinate system.

In the steps 7) and 10), as shown in FIG. 4, the trajectory planning and control for the robotic arm is specifically implemented by the process of: combining preset key trajectory points with coordinate points of the user's mouth and the selected cup in the robotic arm coordinate system to plan an operation trajectory of the robotic arm, and calling the corresponding API of the robotic arm to control the robotic arm to operate based on the planned trajectory, so as to realize the self-assisting function of the robotic arm for assisting the user to drink water.

The above description is merely of preferred embodiments of the present invention, but the scope of protection of the present invention is not limited thereto, and any equivalent replacement or variation that can be achieved by a person skilled in the art according to the technical solutions of the present invention patent and the inventive concept thereof in the scope disclosed by the present invention should fall within the scope of protection of the present invention.

