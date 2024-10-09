# DESCRIPTION

## BACKGROUND

### Technical Field

The description relates to harvesting radio-frequency (RF) energy.

One or more embodiments may be applied, e.g., to Radio-Frequency IDentification (RFID) devices, e.g., with the capability of operating in extreme low-power consumption conditions.

### Description of the Related Art

In its current applications, Radio-Frequency IDentification (hereinafter, briefly RFID) technology involves the use of electronic tags placed on objects, humans or animals with the capability of relaying identifying information to an electronic reader by means of radio-waves.

Automated toll payment systems or tracking systems capable of monitoring the progress of shipments, manufacturing processes and so on are exemplary of possible RFID applications.

A simple and cheap realization of an RFID tag may involve a miniaturized silicon device applied (e.g., glued) onto a laminar substrate with an antenna layout imprinted thereon.

The frequency response of the tag may vary depending on various factors.

For instance, the material of the substrate may reduce the capability to transfer information from the tag to a reader, so that certain tags may be successfully queried only at short range due to the electrical properties of the material on which they are applied.

Pursuing a more uniform and reliable coverage range may lead to designing RFID antennas with low quality factors (e.g., Q in the 5-to-10 range), which may give rise to wideband arrangements exhibiting low sensitivity to external effects at the expense of the communication range capabilities.

Conversely, higher quality factors (e.g., Q in the range of 30-50) provide the capability of extending the communication range between the RFID tag and a reader at the expense of a higher frequency selectivity and sensitivity to the environment (e.g., surrounding materials).

## BRIEF SUMMARY

Despite the increased activity in that area, further improved solutions are desirable which may facilitate, e.g., further expanding the use of RFID technology.

One or more embodiments may be based on the recognition that an automatic self-tuning system facilitates avoiding undesired resonant frequency spreading associated with handling or removing reactive impedance in parallel with an antenna.

One or more embodiments may extend the communication coverage range between an RFID tag and a reader or, more generally, increase the energy which may be collected by a combination of an antenna and an associated RF rectifier (so-called “rectantenna” or “rectenna”).

Consequently, while suited for use in connection with RFID technology, one or more embodiments may more generally facilitate designing autonomous smart sensors with complex capabilities, e.g., in sensing the environment and in providing data processing.

One or more embodiments may provide an energy-efficient solution for adjusting the self-resonance frequency of an antenna to available RF power sources (e.g., GSM, LTE, and so on) thus facilitating the use of (ultra) low-power analog sensors and memory storage elements and more generally the use of those devices where an increase in power available may lead to the number of functions available/provided being correspondingly increased.

One or more embodiments make it possible to develop “smart” RFID devices with long-range communication capability and efficient energy harvester capabilities.

One or more embodiments may involve using a high quality factor (Q) resonant antenna combined with an (ultra) low-power auto-tuning arrangement capable of tracking RF signals over the air in order to locate and exploit more/most powerful RF signals available for harvesting purposes over a certain portion of the RF spectrum (e.g., 800-900 MHz, this being otherwise a merely exemplary, non-limiting figure).

One or more embodiments may involve skipping certain frequencies and/or limiting the number of the frequencies involved in the tracking/checking process.

One or more embodiments may involve a reference clock source, a digital state machine logic circuitry and level shifters with the capability of reducing overall consumption to values below 100 nW.

One or more embodiments make it possible to provide battery-operated RFID devices adapted to be configured and kept notionally indefinitely (e.g., for periods in excess of ten years) with a certain antenna tuning configuration with virtually no losses with the exception of leakage effects.

In one or more embodiments, the antenna tuning range can be configured once or checked periodically.

With a pre-configured tuning setting, an antenna/RF rectifier combination (“rectenna”) may be configured to harvest RF energy with high efficiency and the capability of supplying sensor circuitry without having to rely on a battery.

For instance, harvester devices can be devised having a high sensitivity with the capability of switching on at (very) low input power levels, e.g., below −30 dBm (decibel-milliwatts) or just a few μW.

One or more embodiments may provide harvesters capable of accumulating energy from a remote reader or from other sources such as Wi-Fi/LTE/GSM signals and store the energy collected in a storage element such as a capacitor, possibly (but not necessarily) in conjunction with a battery thus preserving the battery from undesired discharging.

One or more embodiments can be applied to battery-less RFID devices. In such an application the “rectenna” may wake up without a specific configuration and/or with limited sensitivity during a start-up phase (e.g., with a sensitivity range of −10 dBm/−15 dBm). This may be associated with an increased time to have an operative harvester voltage (VHARV) with a higher input RF power to turn on the circuitry. Once a desired level for VHARV becomes available, an auto-tuning circuit may start tuning the antenna thus increasing the communication range, since the associated RF rectifier starts to operate in a fully efficient manner.

In one or more embodiments a DC-DC converter may be provided capable of accumulating energy into a storage element such as a capacitor for further use.

One or more embodiments thus facilitate accumulating energy “drop-by-drop” until a certain quantity becomes available which may permit activating loads such as, e.g., environment sensors (pressure, temperature, image sensors, and so on) and circuitry capable of processing/transmitting such information.

## DETAILED DESCRIPTION

In the ensuing description, one or more specific details are illustrated, aimed at providing an in-depth understanding of examples of embodiments of this description. The embodiments may be obtained without one or more of the specific details, or with other methods, components, materials, etc. In other cases, known structures, materials, or operations are not illustrated or described in detail so that certain aspects of embodiments will not be obscured.

Reference to “an embodiment” or “one embodiment” in the framework of the present description is intended to indicate that a particular configuration, structure, or characteristic described in relation to the embodiment is included in at least one embodiment. Hence, phrases such as “in an embodiment” or “in one embodiment” that may be present in one or more points of the present description do not necessarily refer to one and the same embodiment. Moreover, particular conformations, structures, or characteristics may be combined in any adequate way in one or more embodiments.

The references used herein are provided merely for convenience and hence do not define the extent of protection or the scope of the embodiments.

One or more embodiments are intended to address various issues likely to arise, e.g., in RFID (Radio-Frequency IDentification) devices, including devices of the battery-less type operating in continuous or discontinuous mode, as well as in a variety of devices, such as, e.g., Internet-of-Things (IoT) devices such as wireless sensor nodes.

These applications may benefit from low-power consumption as this facilitates achieving a long useful life (e.g., years) for batteries. Also, the capability of harvesting power from the environment may permit ultimately dispensing with batteries and providing battery-less devices.

Radio-frequency (RF) harvesters may include an AC/DC converter (RF rectifier) combined with a high efficiency DC-DC converter for transferring the energy from the rectifier output to a storage element such as a capacitor. The energy stored can be used to supply low-power circuits including, e.g., digital control units, various sensors to monitor temperature, pressure, humidity, and so on and circuits for transferring the related information, e.g., to a remote reader. As noted, in the case of RFID applications, the substrate onto which an RFID tag is applied can modify the characteristics of the antenna.

Energy available for RF harvesters is very limited (few μW or less). Since the RF energy is (extremely) low, an RF harvester being matched to the antenna will facilitate picking-up (all) the energy available and avoiding reflection issues.

The radio-frequency field available at a certain location is otherwise difficult to control and/or to predict in respect of various factors such as frequency allocation (that is the distribution over the RF spectrum), power intensity and presence at certain time.

One or more embodiments are based on the recognition that an auto-tuning capability in an energy-harvesting antenna may facilitate collecting in an efficient manner the radiofrequency energy available at a certain location/time.

For that purpose, one or more embodiments may involve scanning the radio-frequency spectrum available at a certain time at a certain location searching for a certain “channel” (or band) providing a highest available power, thus facilitating maximum power point tracking (MPPT) operation.

An antenna tuning capability facilitates implementing the combination of a high Q (narrow bandwidth) with an associated RF rectifier (“rectenna”) thus increasing the voltage at the output of the rectifier circuit, which facilitates supplying associated circuits such as associated electronic circuits. Devices such as C-MOS devices adapted to be powered with a supply voltage higher than a threshold voltage VT are exemplary of such circuits.

For instance (the quantitative figures referred to throughout this description are merely exemplary and non-limiting), if the lowest RF power suitable to supply a dedicated low-power circuit such as a C-MOS circuit is in the range of −20 dBm (about 10 μW) over a specific frequency band, the RF harvester circuit should desirably be low-power by itself and be able to effectively collect even very low energy levels available without appreciable losses.

Tuning the antenna/rectifier arrangement to a frequency where a highest power is available at a certain point of space and time is found to effectively contribute to achieve the goals discussed in the foregoing.

Document U.S. Pat. No. 7,167,090 B1 discloses an analog auto-tuning circuit with a linear loop implementing a frequency variation strategy based on a slope detector which compares a current RF rectifier voltage with a previous configuration voltage stored in a dedicated capacitor. Two voltage amplitude values are obtained at different resonant frequencies and then compared to control a frequency tuning direction.

Such an arrangement requires a certain amount of energy to operate and ensure stability of the entire loop. Such a system in fact checks only the voltage amplitude at the RF rectifier output, looking for its maximum value over the scanned frequency band. It is worth noticing that if the rectifier is connected to a DC-DC converter working in the discontinuous mode as described in FIG. 3, the output voltage of the rectifier itself is kept almost constant. Therefore, maximizing the output voltage of the rectifier over the scanned frequency band with the rectifier not connected to any load does not guarantee that the achieved point corresponds to the maximum power that can be delivered by the rectifier when the DC-DC converter is connected to the rectifier. Furthermore, the power available at the output of the rectifier may not be enough to permit correct operation of a DC-DC converter to accumulate energy into a “tank” capacitor. In the presence of a low RF input power, the DC-DC converter could be undesirably turned on, which may result in an amount of energy drawn from the system which is higher than the amount of energy that the system may derive from the antenna.

As noted, the RF energy available at a certain point of space and time is largely uncontrollable and unpredictable. The solution disclosed in U.S. Pat. No. 7,167,090 B1 may thus be unable to operate effectively in such a context, especially in the presence of a spiky RF signal.

Documents such as O'Driscoll, et al.: “A mm-sized implantable power receiver with adaptive link compensation”, ISSCC February 2009, pp. 294-295 disclose the possible use of a bank of capacitors in the place of a varactor for implementing a variable matching network, with an integrator replaced by an up/down counter or a digital circuit implementing a gradient-based search.

Somewhat similar arrangements are disclosed in Stoopman et al.: “A Self-Calibrating RF Energy Harvester generating 1V at −26.3 dBm”, 2013 Symposium on VLSI Circuits Digest of Technical Papers, 18-2, pp. C226-C227.

It is otherwise noted (see, e.g., Pinuela, M., et al.: “London RF Survey for Radiative Ambient RF Energy Harvesters and Efficient DC-Load Inductive Power Transfer”, 2013 7th European Conference on Antennas and Propagation (EuCAP) Gothenburg 2013, pp. 2839-2843) that the power spectrum available in a current environment (e.g., an urban environment) can be approximated as a multi-tone signal exhibiting a strong variability with respect to place and time with an expected available power in the range of −30 to −20 dBm (by assuming a value for Q of about 25-30).

The block diagram of FIG. 1 is exemplary of an RF energy harvester arrangement suitable of “harvesting” radio-frequency energy RF via an antenna 12a coupled with a (RF) rectifier 12b, the combination of the antenna 12a and the rectifier 12b being sometimes briefly referred to as “rectenna”.

The diagram of FIG. 1 shows a DC-DC (step-up) converter 14 receiving a (voltage) signal VHARV from the rectifier 12b and in turn intended to supply energy towards a storage element 16 (e.g., a low-leakage capacitor CST).

The (RF) energy harvested via the antenna 12a may thus be stored on the storage element CST with the capability of supplying a load (here generally exemplified as a resistor RL) by applying thereto an output (voltage) signal VST. This may occur, e.g., as a result of the load RL (which per se may not be a part of the embodiments) being coupled to the circuit 10, e.g., via a switch SW (e.g., a solid-state switch such as a transistor).

In FIG. 1 reference 18 denotes a control circuit (e.g., a low-power C-MOS circuit) configured to control the rectifier 12b and the converter 14 by implementing, e.g., a procedure as discussed in the following in connection with the flowcharts of FIGS. 7 and 8.

In the diagram of FIG. 1 EIN, EHARV and EST indicate:


- - the energy as harvested by the antenna **12***a,*
  - the energy transferred from the rectifier **12***b* to the converter
    **14**, and
  - the energy transferred from the converter **14** to the storage
    element **16**, respectively.

FIG. 2 provides an exemplary circuit-level representation of the arrangement of FIG. 1. Consequently, parts or elements like parts or elements already discussed in connection with FIG. 1 are indicated in FIG. 2 with like references/numerals, and a corresponding detailed description will not be repeated for the sake of brevity.

Consistently with EIN, EHARV and EST in FIG. 1, PIN, PHARV and POUT in FIG. 2 indicate the power levels transferred:


- - from the antenna **12***a* to the rectifier **12***b,*
  - from the rectifier **12***b* to the converter **14**, and
  - from the converter **14** to the storage element **16**,
    respectively.

As represented in FIG. 2, the following relationships apply

ZANT=RANT+jωLM

ZIN=RIN+jXIN

VANT(t)=VANT,peak sin(ωt)

VIN(t)=VIN,peak sin(ωt)

VHARV≈VIN,peak−ΔVRECT

VST=N·VHARV

IHARV=(N/η)·IOUT

PHARV=VHARV·IHARV=(VST/N)·(N/η)·IOUT=POUT/η

where:


- - Z_(ANT)=impedance of the antenna **12***a* (with resistive and
    inductive components R_(ANT) and jωL_(M), respectively),
  - Z_(IN)=input impedance of the rectifier **12***b* (with resistive
    and reactive (capacitive) components R_(IN) and jX_(IN),
    respectively),
  - V_(ANT)(t)=(voltage) signal generated by the antenna **12***a*
    (assumed to be sinusoidal for simplicity),
  - V_(IN)(t)=input (voltage) signal to the rectifier **12***b,*
  - V_(HARV)=voltage signal provided by the rectifier **12***b* towards
    the converter **14** (represented as across the a capacitance
    C_(HARV) therebetween),
  - I_(HARV)=current signal provided by the rectifier **12***b* towards
    the converter **14**
  - V_(ST)=(voltage) signal available at the output of the storage
    element **16** (e.g., across the capacitor C_(ST)),
  - I_(OUT)=current adapted to be supplied to the load R_(L),
  - P_(OUT)=power adapted to be supplied to the load R_(L).
  - N=step-up factor of the DC-DC converter
  - η=efficiency of the converter **14**

The rectifier 12b may exhibit a threshold loss ΔVRECT with a resistance value RRECT adapted to model power losses in the rectifier causing a power efficiency (η) lower than 100%.

The presence of the converter 14 (e.g., DC-DC) facilitates charging the storage element (e.g., capacitor CST), at a “useful” voltage level (e.g., 1.5-2.5V).

The converter 14 can be designed (“optimized”) for operation at (very) low-input power levels (in the range of μW).

The diagram of FIG. 3 is exemplary of possible operation of the converter 14 (as controlled, e.g., by the circuit block 18) involving—in a manner known per se—discontinuous mode operation depending upon the power PHARV, i.e. the power available at the output of the rectifier when its output voltage VHARV is equal to the average value of VH and VL, named VREF in FIG. 3 and equal to VTHR in FIG. 4. In operation, the DC-DC converter 14 is disconnected from the rectenna during time interval CP and the DC-DC converter is connected to the rectenna during time interval TP shown in FIG. 3. FIG. 3 shows the behavior of VHARV (ordinate scale) over time (abscissa scale) with also a voltage VBAT shown, when the DC-DC converter is controlled as shown in FIG. 9, by the comparator 18-c with VREF equal to VTHR.

The voltage VBAT (repeatedly referred to in the following) is generally representative of a supply voltage made available to various circuits as exemplified herein.

This may be provided, e.g., by a battery (e.g., a rechargeable battery coupled to the storage element 16 such as the capacitor CST) or, in the case of “battery-less” solutions by the storage element 16.

As a result of VHARV reaching an upper threshold VH, the converter 14 is activated, so that energy can be transferred from the output of the rectifier 12b (as exemplified by the capacitor CHARV in FIG. 2) to the storage element 16 (e.g., the capacitor CST).

It is observed that, if the voltage output of the converter (open-load condition) is higher than VBAT and if the capacitor CST is very large (μF), CST practically behaves as a short circuit for the converter.

As a result of VHARV reaching a lower threshold VL (due to energy transfer from CHARV to CST) the converter 14 is switched off.

With the DC-DC control described in FIGS. 3 and 9, the average input voltage the converter, i.e., the output voltage of the rectifier VHARV, is maintained equal to VREF.

Stated otherwise, this kind of operation provides for activating the converter 14 (only) if a positive net energy transfer can be obtained through the converter 14 (so that the charge available across CST is desirably increased—or at least preserved—and not reduced as a result of converter operation 14).

One or more embodiments may be based on the recognition of various factors related to operation of an arrangement as exemplified in FIGS. 1 and 2.

For instance, the (equivalent) input impedance ZIN is dependent on PIN with RIN (the resistive components thereof) exhibiting a positive derivative with respect to PIN (by neglecting a dependence on f over a mid-narrow bandwidth). Also XIN exhibits a slight dependence on PIN, while, over a frequency band of interest XIN may exhibit a capacitive-type dependence on f.

Also, for a given value of PAV (power available at the antenna 12a), PIN depends on PHARV and on the actual value of VHARV.

Also, impedance matching between the antenna 12a and input of the rectifier 12b facilitates (maximum) power transfer with the resonance frequency fC and the quality factor Q of the “rectenna” arrangement 12a, 12b playing a role insofar as an increase in the quality factor Q translates into a higher amplitude of VIN (for a given PAV) with a peak value for Q (e.g., QP) occurring at power matching conditions.

A high value for QP translates into a correspondingly smaller bandwidth so that if the “rectenna” is detuned a corresponding reduction occurs in input power.

Consequently, input matching and the quality factor represent significant parameters for the circuit 12a, 12b.

It is otherwise observed that in the case of de-tuning a lower value for QP facilitates achieving a higher value for PIN (for a given PAV).

Also, operation of the rectifier 12b was found to be facilitated by an input voltage (VIN-p) higher than a lower threshold value with a higher value for Qpeak resulting in a correspondingly higher peak value for VIN_p, namely VIN-peak, so that the benefit of a higher Q is almost completely lost if de-tuning occurs.

For instance, in the case of a full-wave rectifier with VT compensation (as disclosed, e.g., in Nakamoto, H., at al.: “A passive UHF RF Identification CMOS Tag IC using Ferroelectric RAM in 0.35-pm Technology”, IEEE JOURNAL OF SOLID-STATE CIRCUITS, vol. 42, no. 1, 1 Jan. 2007, pages 101-110) both the capacitive and the resistive components of the rectifier input impedance (CIN and RIN, respectively) were found to exhibit a dependence on PHARV, therefore on PIN.

One or more embodiments may be based on the recognition that “tuning” the antenna 12a (as exemplified by a “tuning” capacitor CTUN shown in dashed line in FIG. 2 and in full line in FIG. 4) may facilitate translating the Q(f)—that is Q as a function of the frequency f—from a generic point to a matched condition as desired.

In that respect, it was noted that a resistance mismatch between RIN and RANT ends up by having a lower impact on PIN than a mismatch of the corresponding reactive components (e.g., for a relatively high Qp).

Also, it is observed that if the available power is not sufficient to turn on the converter 14 in order to permit a transfer of energy towards the storage element 16, the converter 14 may be kept in an off state as discussed previously in connection with the FIG. 3.

It is otherwise noted that the input impedance of the rectifier 12b depends (as discussed previously) on the power delivered towards the converter 14. This may be the case for RIN which may be (markedly) dependent on the DC-DC operating conditions, while CIN was found to be more weakly dependent thereon.

Finally, it is observed that achieving an effective tuning as desired is facilitated if implemented with the effective, actual load at the output of the rectifier 12b. Antenna auto-tuning may thus be compatible with discontinuous operation of the converter 14 as exemplified previously in connection with Figure. It is worth noting that during the auto-tuning operation, the DC-DC converter is switched off and disconnected from the rectifier. The antenna auto tuning described in FIG. 4 guarantees that the delivered power PHARV is measured at the same output voltage VHARV occurring when the DC-DC converter is connected to the rectifier and operating as in FIG. 3. As discussed previously, an RF input signal contemplated for harvesting with one or more embodiments can be approximated as a multi-tone signal.

Consequently, a sort of global maximum search (that is, scanning the “environment” RF bandwidth to find out (at least) one frequency band or tone providing a highest level of RF power available may be a viable strategy.

FIG. 4 is exemplary of a possible arrangement adapted to perform a tuning action of the antenna by acting on the capacitor CTUN as already introduced in connection with FIG. 2. As exemplified herein (and merely for the sake of explanation) the capacitor CTUN can be regarded as arranged across the input nodes of the rectifier 12b.

In one or more embodiments, tuning of the capacitor CTUN (e.g., as discussed in the following in connection with FIGS. 4 and 5) may be controlled—as discussed in the following—via counter circuits 18a (power counter) and 18b (tuning counter) clocked via a clock generator 22 in cooperation with a comparator 24 sensitive to the difference between the rectifier output signal VHARV and a reference threshold VTHR set by a reference generator 26.

In one or more embodiments these circuit elements may be fed via the (voltage) signal VBAT and be (at least in part) included/implemented (in HW and/or SW form) in the control circuitry 18 of FIG. 1.

For the sake of simplicity, FIG. 4 (wherein parts/elements/entities like parts/elements/entities discussed in connection with the previous figures are indicated with like references/numerals thus making it unnecessary to repeat a corresponding description) focuses on tuning operation of the “rectenna” 12a, 12b. It will be otherwise understood that, in current operation of the circuit 10, the output from the rectifier 12b (e.g., VHARV) is intended to be supplied towards the harvester circuit output (e.g., towards the converter 14 and on towards the load RL under the control of the switch SW) as exemplified previously.

An arrangement as exemplified in FIG. 4 may implement a sort of peak-power-based tuning procedure wherein the “environment” frequency spectrum is scanned so that the available RF frequency bands are scanned, e.g., from an upper value fMAX to a lower value fMIN. As noted, one or more embodiments may involve possibly skipping certain frequency bands/tones and/or checking only a limited set of bands/tones as discussed previously.

One or more embodiments may involve implementing the tuning capacitor CTUN by means of a bank of capacitors as exemplified in FIG. 5 (e.g., CTUN-0, 2CTUN-0, . . . , 2Nf-1CTUN-0) selectively activated (as schematically represented by switches, e.g., transistors in FIG. 5) with activation of the capacitors/switches taking place as a function of control bits (b0, b1, . . . , bNf-1) provided by the tuning counter 18b in FIG. 4.

In one or more embodiments, for each tuning frequency, the load current ILOAD at the output of the rectifier 12b is progressively increased from, e.g., ILOAD,MIN to ILOAD,MAX, that is between a lower and an upper value. Such a control of the current ILOAD at the output of the rectifier 12b may occur in digital form under the control of the power counter 18a.

In one or more embodiments, increasing (e.g., by steps) ILOAD can be stopped when VHARV falls below VTHR, as detected by the comparator 24, with the last values for ILOAD and VTHR providing an estimation of the available power (at the output of the rectifier 12b) at a value of VHARV equal to the threshold voltage VTHR.

In that way, the peak power available at the output of the rectifier 12b can be estimated for each value of the (center of the) frequency band (tone) currently scanned by increasing the output of the tuning counter 18b controlling the capacitor bank as exemplified in FIG. 5.

In that way the (center) frequency (corresponding to a certain configuration of the capacitor bank, namely a certain string of control bits as exemplified in FIG. 5 assuming respective “0” and “1” values) can be selected as the “tuning” frequency providing a desired (highest) available level of RF power (corresponding to a sort of “optimum” tuning frequency).

One or more embodiments as exemplified in FIGS. 4 and 5 thus make it possible to tune the “rectenna” arrangement 12a, 12b, at a peak power level as measured at the output of the rectifier 12b.

It is observed that, while per se adapted to be performed “upwardly” from a lower frequency towards a higher value, a scanning process may be performed “downwardly” as exemplified herein, namely starting from a highest frequency fMAX towards a lowest frequency value fMIN.

The circuit diagram of FIG. 6 is exemplary of a possible arrangement wherein the reference block 26 for the generation of VTHR may be dispensed with (with a consequent advantage in terms of power saving) and the comparator 24 replaced by three inverter logic gates 241, 242, 243.

In an arrangement as exemplified in FIG. 6, a circuit 246 is included in a current line between VHARV (the output voltage from the rectifier 12b) and ground so that a current IL (namely the load current ILOAD, intended to be progressively increased) flows through a series arrangement of resistors R1, R2, . . . , Rn between a node A and ground, with the node A coupled to an input node at a voltage VHARV via two cascaded p-n junctions (e.g., diodes) D1, D2 arranged with their cathodes towards the node A. A switch, e.g., a MOSFET transistor S1 coupled across the terminals (anode-cathode) of one of the diodes D1, D2 (e.g., D1, set between D2 and VHARV), provides a hysteresis behavior as discussed in the following.

The node A is coupled to the input of a first inverter 241 in a cascaded arrangements of inverters 241, 242, 243 with the output from the last inverter 243 which drives the control terminal (gate, in the exemplary case of a field effect transistor such as a MOSFET) of the transistor S1.

The resistors R1, . . . , Rn are adapted to be shorted by respective switches (e.g., solid-state switches such as transistors) activatable as a function of bit values a0, . . . , aNp-1.

The output from the last inverter 243 is also coupled to the input of a level shifter 244 sensitive to the voltage VHARV and outputting a “measurement” signal at a node POK (e.g., towards the control circuit block 18) and supplied by the voltage VBAT.

The load current Iload drawn by the cascaded resistors R1, . . . , Rn can be selectively varied (e.g., gradually increased for each frequency in the scanning procedure discussed previously) by changing the value of the resistance between the node A (at a value VHARV minus the voltage drop VD across the diodes D1, D2, as discussed in the following) and ground by varying the values a0, . . . , aNp-1 (which may occur under the control of the power counter 18a).

It will be appreciated that, in one more embodiments, the circuit elements D1, D2 exemplified in FIG. 6 as p-n junction diodes can be implemented in various other ways known to those of skill in the art, e.g., as transistors in a diode connection (MOSFET transistors with gate shorted to drain) biased in a weak inversion region or as metal-silicon (Schottky) diodes.

The input of the first inverter 241 (VON at node A) can be expressed as VON=VHARV−(1+bHYST)·VD with bHYST belonging to the range [0, 1] (e.g., selected out of 0 and 1) where VD is the voltage drop across the diodes indicated with the same designation.

The threshold for VHARV (VTHR) is thus the threshold of the first inverter while comparator hysteresis is implemented by means of bHYST and the switch S1 (controlled by the output of the inverter 243, that is, by a delayed replica of the output from the first inverter 241 sensitive to VON) made selectively:


- - conductive, to short-circuit the diode D**1** (b_(HYST)=0),
  - non-conductive, so that the diode D**1** is coupled between V_(HARV)
    and D**2** (b_(HYST)=1).

A level shifter 244 may facilitate providing the output logical signal POK to a logic domain under VBAT.

In one or more embodiments as exemplified herein, the output logical signal POK is indicative of the point where (as discussed previously) increasing ILOAD may be stopped as result of VHARV falling below a certain threshold VTHR with the values for ILOAD and VTHR leading to such a voltage drop providing an estimation of the available power (at the output of the rectifier 12b), e.g., at a certain threshold VTHR.

For instance, the circuit exemplified in FIG. 6 may implement processing steps aiming at estimating the instantaneous power PHARV provided by the “rectenna” 12a, 12b via a sequence of iterative actions wherein a known (resistive) load is applied to the rectifier 12b by evaluating if the “measurement” voltage P_OK at the node POK is “true” or “false”.

In one or more embodiments, during measurement/evaluation operation, the converter 14 (and/or other “user” circuitry) is turned off to facilitate a condition where the (only) load current of the rectifier (e.g., IHARV in FIG. 2) is due to the circuit 246 in FIG. 6 (e.g., IL, at least approximately).

By way of (non-limiting) example, one may consider an arrangement as exemplified in FIG. 6 with a resistive load including ten resistors (that is, R1, . . . , Rn with n=10) of equal resistance values (e.g., R=25 kOhm) and a threshold value V_THRESHOLD of the digital gate 241 (i.e., inverter gate).

For instance, if the element 241 is implemented as a CMOS inverter, V_THRESHOLD depends on its supply voltage (i.e., VHARV), i.e., V_THRESHOLD=VHARV*k_INV, where k_INV is a coefficient depending on the aspect ratio of the PMOS and NMOS devices within the CMOS inverter.

One may reasonably assume that the voltage VHARV will cause a current having an intensity I_RESISTOR=VON/R_T to flow in the load resistors R1, . . . , R10, where VON indicates the voltage at the node A and R_T is the effective resistance of resistors R1, . . . , Rn (e.g., with n=10) combined (e.g., in series) via the switches a0, . . . , aNp-1.

Under these conditions, the (first) inverter 241 coupled to the node A will act as a 1-bit analog-to-digital converter (essentially as a comparator with a threshold V_THRESHOLD) with switching of the associates logic gate taking place as a result of VON≥V_THRESHOLD.

In the exemplary case discussed herein, since VON=VHARV−VD (with S1 ON, bHYST=0) and V_THRESHOLD=VHARV*k_INV, switching of the inverter gate 241 will occur at VHARV=VD/(1−k_INV).

The power provided by the RF rectifier 12b, and thus the power P_HARVESTER available (e.g., at a certain frequency band), can be thus be evaluated by step-wise (e.g., STEP_1, STEP_2, . . . ) reducing the load applied thereto, with the power adapted to be expressed as (VON/R_T) VHARV=VHARV{circumflex over ( )}2/R_T−(VHARV*VD*(1+bHYST))/R_T.

In an arrangement as exemplified in FIG. 6, this may occur by gradually reducing the resistive load between the node A and ground by progressively short-circuiting via the switches a0, . . . , aNp-1, an increased number of resistors R1, . . . , R10 in the series arrangement between the node A and ground and correspondingly checking the output of logic gate 241 (and of the level-shifter 244, POK).

In the example discussed herein, one may reasonably assume that the power consumption on the diode(s) D2 (and D1) is negligible, i.e., P_HARVESTER˜VHARV{circumflex over ( )}2/R, k_INV=0.5, VD=0.5V.

Therefore V_THRESHOLD=0.5 V (at VHARV=1V) and POK toggles from 1 to 0 (assuming inverting level shifter LS 244) when VHARV falls below 1V.

The following is an example of steps wherein an increasing number of resistors R1 is progressively (e.g., step-wise) short-circuited via the switches a0, . . . , aNp-1.

STEP1: R_T=10R, VHARV>2*VD=1V

P_OK=1 (inverting LS)

P_HARVESTER_STEP _1≥(V_THRESHOLD{circumflex over ( )}2)/10R≥1 uW

STEP2: R_T=9R, VHARV>2*VD=1V

P_OK=1 (inverting LS)

P_HARVESTER_STEP_2≥(V_THRESHOLD{circumflex over ( )}2)/9R≥1.1 uW

. . .

STEP8: R_T=3R, VHARV>2*VD=1V

P_OK=1 (inverting LS)

P_HARVESTER_STEP_8≥(V_THRESHOLD{circumflex over ( )}2)/3R≥3.3 uW

STEP9: R_T=2R, VHARV<2*VD=1V

P_OK=0 (inverting LS)

P_HARVESTER_STEP_9<=(V_THRESHOLD{circumflex over ( )}2)/2R<=5 uW

Referring to P_OK at the node POK switching from P_OK=1 to P_OK=0 may be representative of an exemplary case where, upon reaching step 9, the power provided by the rectifier 12b is no longer in a position to provide a voltage VON high enough to keep P_OK at a “high” logic value, e.g., to provide a rectified voltage VHARV>2*VD=1V.

As a result, it may be—at least approximately—evaluated that the (highest) power the rectifier 12b (that is, the rectenna 12a, 12b) is capable of providing in a certain frequency band lies between 3.3 uW and 5 uWat VHARV=1V.

Of course referring to P_OK switching, e.g., from P_OK=1 to P_OK=0 upon reaching step 9 is merely exemplary insofar as this switching may occur at (notionally) each step in the procedure described.

The power provided by the rectifier 12b (that is, the power captured by the rectenna 12a, 12b) at a certain frequency band may thus be estimated to be higher (resp. lower) than the power provided/captured at another frequency band based on the number of steps which led to P_OK switching being higher (resp. lower) in the former case than in the latter case.

In the (purely exemplary) case discussed herein, all the resistors R1, . . . , Rn are assumed to be of equal value. In one or more embodiments, different resistance values can be used to obtain, e.g., a power evaluation on a linear scale in the place of a logarithmic one.

One or more embodiments as exemplified herein make it possible to store—rather than the estimated power per se—a value (e.g., an index NPHARV as referred to in discussing the flowcharts of FIGS. 7 and 8) which is representative of the configuration of the “active”, non-shorted resistors R1, . . . , Rn (or, conversely, of the “non-active”, shorted resistors R1, . . . , Rn) which resulted in a drop of the harvesting voltage, as detected by the voltage VON reaching the threshold V_THRESHOLD.

In that way, one or more embodiments make it possible to sense respective values (such as, e.g., Power(NFREQ)=NPHARV−1) indicative of the power of radiofrequency signals captured by the antenna unit 12a, 12b at certain frequency bands in the plurality of tuning bands subject to scanning.

As noted, an index indicative of, e.g., how many resistors were shorted in order to cause VON to drop down to the threshold V_THRESHOLD and cause P_OK to switch, e.g., from P_OK=1 to P_OK=0 may be indicative of the power of radiofrequency signals captured by the antenna unit 12a, 12b at a certain frequency band.

One or more embodiments thus make it possible to identify—e.g., as a function of respective values for the index discussed previously, that is without having to store and compare values for the power levels captured by the antenna unit—(at least) one of the frequency bands scanned where a highest power of radiofrequency signals is captured by the antenna unit (rectenna).

For instance (with reference to the exemplary case discussed above in connection with FIG. 6) this may be the one frequency band for which a highest number of resistors R1, . . . , Rn were shorted in order to cause VON to drop down to the threshold and cause P_OK to switch, e.g., from P_OK=1 to P_OK=0.

In one or more embodiments, the harvester circuit 10 can thus be operated with the antenna unit 12a, 12b tuned at the frequency band thus identified.

In the case of two (or more) frequency bands being identified, one can be selected, e.g., in a pseudo-random manner.

Also, since the characteristics of the converter 14 are known, the state machine is in a position to decide whether the converter (and/or, other user circuitry) can be turned on (again) once the power estimation procedure discussed is completed.

The flowcharts of FIGS. 7 and 8 are exemplary of two possible approaches in performing the peak-power based tuning procedure as discussed in the foregoing.

The flowchart of FIG. 7 is exemplary of a “sweep load first” approach, whereas the flowchart of FIG. 8 is exemplary of a “sweep frequency first” approach.

In FIG. 7, after a START step, in a step or act 100 a frequency NFREQ is set to a default value NFREQ.DEFAULT (e.g., a value fMAX, which may occur by acting on the coefficients b0, b1, . . . , bNf-1) while the power level is set to a virtually “zero” value, e.g., in the power counter 18a, possibly by acting on the coefficients a0, . . . , aNp-1 in FIG. 6 in those embodiments adopting an implementation as exemplified therein.

The blocks 102 to 112 in FIG. 7 are exemplary of an “inner loop” on the harvester load, with, e.g., a level NPHARV set first to zero (e.g., NPHARV=0) in an act 102 followed by a check in an act 104 as to whether VHARV is higher than VTHR (see, e.g., the comparator 24 in FIG. 4 or the corresponding arrangement in FIG. 6) and whether all the contemplated steps for NPHARV have been completed (namely NPHARV≤2NP−1).

A positive outcome of the check in act 104 leads to an increase in NPHARV (++NPHARV) in an act 106 with operation returning upstream of the check 104 to implement a harvester load loop (PHARV loop).

A negative outcome of the check in act 104 leads (in an act 108) to the value of a highest available power for each frequency band (e.g., with a corresponding index, e.g., Power(NFREQ)=NPHARV−1) being stored (e.g., in the circuit block 18).

The act 108 is followed by an act 110 wherein the tuning frequency is varied (e.g., decreased or increased) according to the frequency scanning plan adopted.

As noted, in one or more embodiments the scanning process may involve, e.g., skipping certain frequencies/tones for various reasons, e.g., restricting scanning to certain frequency bands/tones expected to contain energy levels suitable for harvesting.

An act exemplified by block 112 corresponds to a check as to whether the frequency scanning schedule (possibly defined in a selective manner as discussed previously) has been completed.

In the diagram of FIG. 7, a positive outcome of the act 112 (e.g., NFREQ≤2Nf-1) may be indicative of further frequency bands/tones remaining to be scanned, thus leading the system to return upstream of the act 102.

A negative outcome of the check 112 is indicative of the frequency scanning being completed as planned thus leading to a highest (maximum) power level available, e.g., max(Power) being identified (e.g., via respective indexes [PVAL, PINDEx]) with a corresponding best frequency band/tone for harvesting purposes identified in an act 116 (e.g., via a corresponding index NFREQ=PINDEx) and processing of evolving to an END after a number of iterations Niterations≤2NF·2NP.

It will be appreciated that embodiments as exemplified in FIG. 7 lend themselves to adopting practically any desired preset frequency default value (e.g., in act 100) while also facilitating possible non-linear scanning both of load values and of frequency values (that is by adopting non-linear laws for the load and frequency variation steps in acts 106 and 110).

The diagram of FIG. 8 is exemplary of an approach where after a START act, the same actions discussed previously in connection with acts 100 and 102 in FIG. 7 are performed in an act 200 with a frequency scan loop subsequently performed in the acts exemplified by blocks 202 to 208.

For instance, an act 202 may be exemplary of a check made as to whether VHARV is higher than VTHR (see, e.g., the comparator 24 of FIG. 4 or the corresponding arrangement of FIG. 6). A positive outcome of the check of act 202 leads to a corresponding power value being stored in an act 204 (e.g., Power (NFREQ)=NPHARV) followed by a variation in the frequency performed in an act 206 (see for reference also act 112 in FIG. 7).

The act 206 may also be reached directly from the act 202 in the case this latter yields negative outcome.

In an act 208 a check is made as to whether the planned scanning of frequencies (which, again, may be planned selectively, e.g., by skipping certain frequency bands/tones and/or by limiting the scanning to certain frequency bands or tones) has been completed (e.g., NFREQ≤2NF−1). In the diagram of FIG. 8 a positive outcome of act 208 is indicative of the frequency scan loop still having to be completed, which leads processing to return upstream of act 202.

A negative outcome of the act 208 leads to an act 210 where those frequency values NFREQ for which VHARV was found to be lower than VTHR are excluded from further processing (e.g., from further frequency scanning rounds), after which the value for NPHARV (that is, the rectifier load) is increased in an act 212 (see, by way of reference act 106 in FIG. 7).

In an act 214 a check is made as to whether the harvester load loop has been completed or not (e.g., NPHARV≤2NP−1).

In the flow chart of FIG. 8, a positive outcome of act 214 is indicative of the load loop still having to be completed, which results in processing returning upstream of act 202.

A negative outcome of act 214 is indicative of the completion of the load loop which leads to identifying a highest (maximum) power level available being identified and a corresponding “best” tuning frequency being determined in acts 216 and 218. These may substantially correspond to the acts 114 and 116 in the flow chart of FIG. 7, after which processing evolves to an END.

Again, processing as exemplified in FIG. 8 may be completed in a number of iterations Niterations≤2NF·2NP with the possibility of setting arbitrarily the initial frequency default value and/or the possibility of applying non-linear laws in frequency and load sweeping (acts 206 and 212 in FIG. 8).

One or more embodiments may thus involve a dual-step start-up solution which reduces power consumption and increase the sensitivity of the RF rectifier 12b.

Embodiments as exemplified herein facilitate providing a circuit that for each frequency band/tone may identify an available power level at the output of the RF rectifier with an operative voltage large enough to keep the associated circuitry active (“on state”). Exemplary operating voltages may vary from 0.3 to 0.9 Volt.

At the end of the frequency scan, the antenna 12a can thus be tuned to a “best” sub-frequency band or tone with a highest (maximum) available energy for harvesting.

This in contrast with certain conventional arrangements (see, e.g., U.S. Pat. No. 7,167,090 B1, discussed previously) where only the presence of a voltage is checked. In fact, one or more embodiments may detect (measure) the total available power and activate a converter 14 and/or a separate charge storage circuitry, e.g., as enclosed in an independent power island (only) when the energy balance is positive.

The energy balance being positive corresponds to a condition where the energy from the antenna 12a is enough to operate the circuit so that the RF energy captured can be stored, e.g., in a storage element such as a tank capacitor (e.g., CST in the figures). A negative energy balance is a condition where (e.g., as a result of a wrong decision) certain circuit elements in the harvester device are switched on with the energy coming from the antenna 12a insufficient to sustain the overall load, so that energy is undesirably sunk from the storage element, e.g., with the capacitor CST discharged.

One or more embodiments may improve reliability by avoiding, e.g., undesired discharging of a battery (if present) or a tank capacitor.

In one or more embodiments, RF power measurements can be obtained by means of a simple low-power circuit adapted to replace a full-frequency scanner.

In certain embodiments as exemplified, the circuit may include a string of switchable resistors (see, e.g., FIG. 6) that load the RF rectifier output. The resistors are progressively short-circuited until the RF rectifier is no longer capable of sustaining a voltage at its output node (VHARV).

The combination of on-off switches that leads to such “automated” voltage drop provides an information about the available input power. While this may not represent, taken per se, quite an accurate measurement of the power available, the associated information is however reliable enough to facilitate evaluations with power measurements made in other frequency bands/tones. In that way the frequency providing a highest (peak) RF energy can be identified.

In one or more embodiments as exemplified in FIG. 6, the hysteresis circuit implemented via the diode D1 and the switch S1 facilitates stabilizing the signal POK exemplary of a desired “good” power signal by avoiding ringing phenomena such as 0/1/0 ringing. In such embodiments, the signal POK and the on/off combination of the switches a0, . . . , aNp-1 are digital signals adapted to be used by a state machine (as possibly included in the circuit block 18) to decide how to proceed.

In those embodiments where a DC-DC converter is present (see, e.g., 14 in the Figures) the possibility exists of keeping it in an “off” state during the associated calibration phase to avoid malfunctions (e.g., undesirably discharging the storage element 16, such as a battery and/or capacitor CST) and/or garbling the decisions of the power measurement unit.

It is noted that the power consumption of the DC-DC converter 14 may turn out to be higher than the RF input power available and/or the power consumption of the power measurement unit. This may be the case, e.g., with a generic power island including digital, analogue or mixed logic circuitry as may be the case with IoT devices like MEMs.

In one or more embodiments, as a result of the (possibly selective) frequency scan operation having been completed with a sufficiently high level of available RF power identified, a state machine (as included, e.g., in the circuit block 18) may switch off the frequency scan circuitry and activate the converter 14. The activation of the converter will have a negligible impact on the resonant frequency of the antenna 12a so the matching condition of the reactive component for the specific resonant frequency band/tone selected may be maintained. This is true if the DC-DC converter is controlled by a reference voltage VREF, FIG. 9, equal to the threshold voltage VTHR, FIG. 4, being used in the auto tuning procedure. This can be obtained by calibrating VREF supplied to comparator 18c by means of the circuit in FIG. 6 or by replacing the comparator 18c with the circuit of FIG. 6.

One or more embodiments may be applied to a wide variety of devices for use, e.g., in logistics, asset tracking (e.g., in manufacturing, storing, shipping and delivering goods), life sciences (medical/health), and various monitoring applications (e.g., in industry or “smart city” applications).

In one or more embodiments, a method of operating a radiofrequency harvester circuit (e.g., 10) including an antenna unit (e.g., a “rectenna” or “rectantenna” 12a, 12b) configured to capture radiofrequency signals and harvesting circuitry (e.g., 14, 16, 18) coupled to the antenna unit, the harvesting circuitry configured to collect radiofrequency energy from the radiofrequency signals captured by the antenna unit, may include:


- - configuring the antenna unit as a tunable antenna unit (e.g.,
    C_(TUN)) selectively tunable (e.g., **18**; b₀, b₁, . . . ,
    b_(Nf-1)) at a plurality of tuning bands,
  - scanning the plurality of tuning bands by selectively tuning (e.g.,
    **110**; **206**) the antenna unit at frequency bands in the
    plurality of tuning bands,
  - evaluating the power of radiofrequency signals captured by the
    antenna unit at said frequency bands in the plurality of tuning
    bands in said scanning, by sensing (e.g., **108**; **204**)
    respective values (e.g., N_(PHARV)) indicative of the power of
    radiofrequency signals captured by the antenna unit at said
    frequency bands in the plurality of tuning bands in said scanning,
  - identifying (e.g., **114**; **216**), as a function of said
    respective values, one of said frequency bands wherein a highest
    power of radiofrequency signals is captured by the antenna unit, and
  - operating (e.g., **116**; **218**) the harvester circuit with the
    antenna unit tuned at said one of said frequency bands.

One or more embodiments may include performing said scanning over a frequency range encompassing said plurality of tuning bands by selectively skipping at least one tuning band of said plurality of tuning bands and/or by limiting scanning to a subset of said plurality of tuning bands.

In one or more embodiments, sensing respective values indicative of the power of radiofrequency signals captured by the antenna unit may include:


- - increasing (e.g., **106**; **212**; **22**, **24**, **26**; **246**;
    a₀, a₁, . . . , a_(NP-1)) a load applied by the harvesting circuitry
    to the antenna unit thereby producing a drop in a signal (e.g.,
    V_(HARV), as possibly represented by V_(ON) at node A in FIG. 6)
    provided by the antenna unit to the harvesting circuitry,
  - sensing a value indicative of the power of radiofrequency signal
    captured by the antenna unit at (e.g., as a result of detecting) a
    drop of the signal provided by the antenna unit to the harvesting
    circuitry to a lower threshold (e.g., V_(THR) as possibly
    represented by V_THRESHOLD at **241** in FIG. 6).

In one or more embodiments, said scanning may include:


- - subsequently tuning (e.g., **100**, **110**) the antenna unit at
    different frequency bands in the plurality of tuning bands,
  - increasing (e.g., **102**, **106**) the load applied by the
    harvesting circuitry to the antenna unit tuned at each one of the
    different frequency bands at which the antenna unit is subsequently
    tuned thereby producing a drop in a signal provided by the antenna
    unit to the harvesting circuitry.

In one or more embodiments, said scanning may include:


- - subsequently tuning (e.g., **200**, **206**) the antenna unit at
    different frequency bands in the plurality of tuning bands in
    subsequent frequency scanning rounds (e.g., **202**, **204**,
    **206**, **208**) performed over frequency bands for which the
    signal provided by the antenna unit to the harvesting circuitry is
    in excess of said lower threshold,
  - increasing (e.g., **212**) at each scanning round the load applied
    by the harvesting circuitry to the antenna unit thereby producing a
    drop in the signal provided by the antenna unit to the harvesting
    circuitry, wherein frequency bands for which the signal provided by
    the antenna unit drops to said lower threshold are excluded (e.g.,
    **210**) from subsequent scanning rounds.

In one or more embodiments, the harvesting circuitry may include a converter circuit block (e.g., 14) activatable to transfer energy from the antenna unit to an energy storage circuit block (e.g., 16) coupleable (e.g., SW) to an harvester circuit load (e.g., RL), and the method may include operating (e.g., 116; 218) the harvester circuit with the antenna unit tuned at said one of said frequency bands and activating (e.g., TP) resp. de-activating (e.g., CP) the converter circuit block as a result of the signal provided by the antenna unit to the harvesting circuitry reaching a higher (e.g., VH) resp. lower (e.g., VL) operating threshold.

A radiofrequency harvester circuit according to one or more embodiments may include an antenna unit configured to capture radiofrequency signals and harvesting circuitry coupled to the antenna unit, the harvesting circuitry configured to collect energy from the radiofrequency signals captured by the antenna unit, wherein:


- - the antenna unit includes a tunable antenna unit selectively tunable
    at a plurality of tuning bands,
  - a control circuit block is provided coupled to the antenna unit and
    to the harvesting circuitry, the control circuit block configured to
    perform the acts of selectively tuning the antenna unit, sensing
    respective values indicative of the power of radiofrequency signals
    captured by the antenna unit, identifying said one of said frequency
    bands, and operating the harvester circuit with the antenna unit
    tuned at said one of said frequency bands, with the method of one or
    more embodiments.

A device according to one or more embodiments may include:


- - a radiofrequency harvester circuit (e.g., **10**) according to one
    or more embodiments,
  - a harvester circuit load (e.g., R_(L)), and
  - a coupling circuitry (e.g., SW) activatable to couple the harvester
    circuit load to the harvesting circuitry in the radiofrequency
    harvester circuit to be supplied thereby.

One or more embodiments may include a Radio Frequency IDentification, RFID, device.

One or more embodiments may include a battery-less device wherein the harvester circuit load is supplied integrally by the radiofrequency harvester circuit.

Without prejudice to the underlying principles, the details and embodiments may vary, even significantly, without departing from the extent of protection.

In embodiments of the present disclosure, a radiofrequency harvester circuit may be used in a battery-less RFID device. The harvester circuit includes an antenna unit that captures radiofrequency signals and harvesting circuitry coupled to the antenna unit for collecting energy from the radiofrequency signals captured by the antenna unit. The antenna unit is selectively tunable at a plurality of tuning bands that are scanned by selectively tuning the antenna unit at different frequency bands and sensing respective values indicative of the power of radiofrequency signals captured by the antenna unit at the frequency bands scanned. A highest value out of said respective values for the power of radiofrequency signals as well as the frequency band in the plurality of tuning bands of the antenna unit providing the aforesaid highest value are identified and the harvester circuit is operated with the antenna unit tuned at the frequency band providing the highest value thus identified. The power point search herein described, namely finding “highest value,” is based on the concept that the maximum power PHARV is searched over the frequency band at some value of VHARV=VTHR (VTHR=reference threshold), and varying the tuning capacitance CTUN and the load of the rectifier ILOAD. The power VHARV equals the reference threshold VTHR, where VTHR=VREF in FIGS. 3 and 9, the rectifier will deliver to the DC-DC converter the same power that was found/measured during the auto tuning procedure.

The various embodiments described above can be combined to provide further embodiments. These and other changes can be made to the embodiments in light of the above-detailed description. In general, in the following claims, the terms used should not be construed to limit the claims to the specific embodiments disclosed in the specification and the claims, but should be construed to include all possible embodiments along with the full scope of equivalents to which such claims are entitled. Accordingly, the claims are not limited by the disclosure.

