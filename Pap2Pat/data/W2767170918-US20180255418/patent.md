# DESCRIPTION

## INTRODUCTION

The subject disclosure relates to location estimation of an active speaker.

There are many situations in which determining the location of a source of sound is useful. Acoustic sensors are used to estimate the location of a seismic event, for example. In another type of application, an array of microphones may be arranged to obtain sound for amplification, recording, or transmission. In such a case, the parameters of a known beamforming algorithm that is applied to the array of microphones can be estimated based on a particular location of interest. For example, beamforming can be performed such that the microphones of the array are focused on a speaker on a panel or a soloist within an orchestra. In an exemplary vehicle application, beamforming can be performed on the array of microphones based on whichever of the vehicle occupants is currently speaking. Performing beamforming on the microphones facilitates a reduction in noise and improved voice recognition, for example. However, using a beamforming algorithm requires an accurate estimation of the position of the speaker in real time (i.e., the active speaker). Accordingly, it is desirable to provide a method and system to determine the location of a speaker in real time.

## SUMMARY

In one exemplary embodiment, a method of performing an estimation of a location of an active speaker in real time includes designating a microphone of an array of microphones as a reference microphone, and storing a relative transfer function (RTF) for each microphone of the array of microphones other than the reference microphone associated with each potential location among potential locations as a set of stored RTFs. The method also includes obtaining a voice sample of the active speaker and obtaining a speaker RTF for each microphone of the array of microphones other than the reference microphone, and performing an RTF projection of the speaker RTF for each microphone on the set of stored RTFs. One of the potential locations is determined as the location of the active speaker based on the performing the RTF projection.

In addition to one or more of the features described herein, obtaining the voice sample is performed in real time.

In addition to one or more of the features described herein, a sound is sampled from each of the potential locations to obtain the set of stored RTFs.

In addition to one or more of the features described herein, the set of stored RTFs is obtained as the RTF for each microphone of the array of microphones other than the reference microphone based on computing, for each of the potential locations, a ratio of an acoustic transfer function from one potential location among the potential locations to the microphone to an acoustic transfer function from the one potential location among the potential locations to the reference microphone.

In addition to one or more of the features described herein, obtaining the speaker RTF for each microphone of the array of microphones other than the reference microphone includes computing, for each of the potential locations, a ratio of an acoustic transfer function of the voice sample at the microphone to an acoustic transfer function of the voice sample at the reference microphone.

In addition to one or more of the features described herein, performing the RTF projection includes calculating a cosine distance between each speaker RTF and each RTF of the set of stored RTFs.

In addition to one or more of the features described herein, determining the location of the active speaker is based on the maximum of the cosine distances.

In addition to one or more of the features described herein, storing the set of stored RTFs for the potential locations includes storing the set of stored RTFs for each seat in an automobile.

In addition to one or more of the features described herein, storing the set of stored RTFs is part of a calibration process performed for the automobile.

In addition to one or more of the features described herein, storing the set of stored RTFs is part of a calibration process performed for a calibration automobile of a same model as the automobile.

In another exemplary embodiment, a system to estimate a location of an active speaker includes a memory device to store a relative transfer function (RTF) for each microphone of an array of microphones other than a reference microphone associated with each potential location among potential locations as a set of stored RTFs. The system also includes a processor to obtain a voice sample of the active speaker and obtain a speaker RTF for each microphone of the array of microphones other than the reference microphone, perform an RTF projection of the speaker RTF for each microphone on the set of stored RTFs, and determine one of the potential locations as the location of the active speaker based on the RTF projection.

In addition to one or more of the features described herein, the processor obtains the voice sample in real time.

In addition to one or more of the features described herein, the processor samples a sound from each of the potential locations to obtain the set of stored RTFs.

In addition to one or more of the features described herein, the processor obtains the set of stored RTFs as the RTF for each microphone of the array of microphones other than the reference microphone based on computing, for each of the potential locations, a ratio of an acoustic transfer function from one potential location among the potential locations to the microphone to an acoustic transfer function from the one potential location among the potential locations to the reference microphone.

In addition to one or more of the features described herein, the processor obtains the speaker RTF for each microphone of the array of microphones other than the reference microphone based on computing, for each of the potential locations, a ratio of an acoustic transfer function of the voice sample at the microphone to an acoustic transfer function of the voice sample at the reference microphone.

In addition to one or more of the features described herein, the processor performs the RTF projection by calculating a cosine distance between each speaker RTF and each RTF of the set of stored RTFs.

In addition to one or more of the features described herein, the processor determines the location of the active speaker based on the maximum of the cosine distances.

In addition to one or more of the features described herein, the memory device stores the set of stored RTFs for each seat in an automobile.

In addition to one or more of the features described herein, the memory device stores the set of stored RTFs as part of a calibration process performed for the automobile.

In addition to one or more of the features described herein, the memory device stores the set of stored RTFs as part of a calibration process performed for a calibration automobile of a same model as the automobile.

The above features and advantages, and other features and advantages of the disclosure are readily apparent from the following detailed description when taken in connection with the accompanying drawings.

## DETAILED DESCRIPTION

The following description is merely exemplary in nature and is not intended to limit the present disclosure, its application or uses.

As previously noted, estimating the location of a speaker can be useful. In an exemplary vehicle application, estimating the seat of a speaker can facilitate using a beamforming algorithm on an array of microphones. Estimating the seat location of a speaker may facilitate other applications, as well. Embodiments of the systems and methods detailed herein relate to using relative transfer functions (RTFs) to estimate the location of a speaker. For explanatory purposes, the exemplary case of determining the seat location of a speaker in an automobile is specifically detailed. However, the embodiments detailed herein are applicable to any scenario in which potential speaker locations have been identified for calibration.

In accordance with an exemplary embodiment, FIG. 1 shows a system to estimate the location of a speaker. A vehicle 101 is shown with four potential speaker locations 105w, 105x, 105y, and 105z (generally, 105). Two occupants are shown in the vehicle 101. The occupants are in locations 105w and 105z. Either of the occupants can speak at any given time. The vehicle 101 includes an array of microphones 110a, 110b, 110c, and 110d (generally, 110). While four microphones 110 arranged in a row are shown for the exemplary array in FIG. 1, any number of microphones in any arrangement can be used. However, the same arrangement of microphones 110 and potential locations 105 must be used during the calibration process discussed with reference to FIG. 2. When one of the occupants speaks, determining which one is speaking (i.e., estimating the location 105 in which the speaker is sitting) facilitates performing beamforming with the array of microphones 110. A controller 100 makes the determination according to one or more embodiments.

The controller 100 includes processing circuitry that may include an application specific integrated circuit (ASIC), an electronic circuit, a processor (e.g., processor 107) (shared, dedicated, or group) and memory (e.g., memory device 103) that executes one or more software or firmware programs, a combinational logic circuit, and/or other suitable components that provide the described functionality.

FIG. 2 is a process flow of a method of determining the location 105 of an active speaker according to one or more embodiments. The dashed line in FIG. 2 separates processes 210, 220, 230, and 240, which relate to a calibration process, from the processes beginning with block 250, which relate to real-time operation. As previously noted, the same relative arrangement of locations 105 and microphones 110 that is used in the calibration process must be present during the real-time processes. In the exemplary case in which the location 105 of a speaker is determined in a vehicle 101, the calibration process may be performed once for a model of a vehicle 101, for example. Thus, each vehicle 101 of the same model need not undergo the calibration process again.

At block 210, designating a reference microphone 110 refers to identifying one of the microphones 110 in the array as a reference microphone 110. For example, microphone 110a in the exemplary array shown in FIG. 1 may be designated as the reference microphone 110. At block 220, the processes include obtaining a sound sample at each microphone 110 for each location 105. As previously noted, the calibration may be performed once for the model of the vehicle 101. Thus, a sound sample is obtained at each microphone 110 from each location 105w, 105x, 105y, and 105z during the calibration process even though the exemplary real-time configuration shown in FIG. 1 includes occupants in only locations 105w and 105z.

Performing RTF estimation, at block 230, essentially refers to obtaining an RTF value for each non-reference microphone 110 associated with each location 105. The RTF estimation can be performed according to different embodiments, one of which is detailed with reference to FIG. 3. At block 240, storing the RTFs completes the calibration process.

At block 250, sampling a speaker from each microphone 110 is done when one of the occupants in the vehicle 101 starts speaking. Obtaining speaker RTFs, at block 260, refers to obtaining the RTF for each non-reference microphone 110 associated with the speaker. Performing RTF projection, at block 270, involves using the RTFs stored at block 240 as part of the calibration process and the speaker RTFs obtained at block 260. Essentially, the controller 100 calculates a cosine distance between the stored RTFs (at block 240) and obtained speaker RTFs (at block 260) and determines the location 105 of the speaker based on the cosine distances.

The cosine distance is given by:

\(\begin{matrix}
{{D_{i}\left( {l,k} \right)} = \frac{\left| {{\hat{C}\left( {l,k} \right)}^{H} \cdot {C^{i}(k)}} \right|}{{{\hat{C}\left( {l,k} \right)}^{H}} \cdot {{C^{i}(k)}}}} & \left\lbrack {{EQ}.\mspace{11mu} 1} \right\rbrack
\end{matrix}\)

D is the cosine distance, i is an index for each location 105 that was calibrated, l is the index of time, and k is the index of frequency. C is a column vector of RTFs, where Ĉ refers to the speaker RTFs obtained in the operational mode for an active speaker. H indicates a conjugate transpose. Once the cosine distance is obtained for each potential location 105, the location I(l) is determined as the location 105 that provides the maximum cosine distance location 105 of the active speaker. Specifically, assuming that only one occupant is speaking, the location, I(l), is determined as:

\(\begin{matrix}
{{I(l)} = {\underset{i}{\arg \mspace{11mu} \max}{\sum\limits_{k}\; {D_{i}\left( {l,k} \right)}}}} & \left\lbrack {{EQ}.\mspace{11mu} 2} \right\rbrack
\end{matrix}\)

FIG. 3 details processes associated with performing RTF estimation, at block 230, as part of the calibration process. The exemplary case discussed for explanatory purposes is the arrangement shown in FIG. 1 with microphone 110a designated as the reference microphone. According to the exemplary embodiment, the acoustic transfer function (ATF) is determined for every microphone 110, including the reference microphone 110a, based on a sound source at each location 105. The ATF values associated with each microphone 110a, 110b, 110c, 110d for a sound source at each location 105w, 105x, 105y, 105z are shown in table 310. Each acoustic transfer function value provides the relationship between a sound level at a given location 105 (at the source of the sound) and the sound level at a given microphone 110. Measurement of ATF according to multiple methods is known and is not further detailed herein. The ATF values associated with the reference microphone 110a for each of the locations 105w, 105x, 105y, 105z are reference ATF values ATFw-a, ATFx-a, ATFy-a, ATFz-a in table 310.

After the ATF values in table 310 are obtained, the RTF for each non-reference microphone 110 (microphones 110b, 110c, 110d) associated with each location 105w, 105x, 105y, 105z is a ratio of the acoustic transfer function to the reference acoustic transfer function associated with that same location. The RTF values are indicated in table 320. As an example, RTFx-c_a is the ratio of the ATF of microphone 110c for location 105x (ATFx-c) to the ATF of the reference microphone 110a for the same location 105x (ATFx-a).

While the above disclosure has been described with reference to exemplary embodiments, it will be understood by those skilled in the art that various changes may be made and equivalents may be substituted for elements thereof without departing from its scope. In addition, many modifications may be made to adapt a particular situation or material to the teachings of the disclosure without departing from the essential scope thereof. Therefore, it is intended that the present disclosure not be limited to the particular embodiments disclosed, but will include all embodiments falling within the scope thereof.

