# DESCRIPTION

## GOVERNMENT LICENSE RIGHTS

The U.S. Government has a paid-up license in this invention and the right in limited circumstances to require the patent owner to license others on reasonable terms as provided for by the terms of Agreement No. AGS-0753581, awarded by a National Science Foundation and National Center for Atmospheric Research cooperative agreement.

## TECHNICAL FIELD

The present application is related to the field of remote sensing, and in particular, to the study of cloud and aerosol interactions in climate atmospheric research.

## BACKGROUND OF THE INVENTION

Lidar is an acronym for Light Detection And Ranging. In the atmospheric sciences, it is a technology that may be used to measure range resolved atmospheric constituents such as wind, aerosol particles, water vapor, and others. Lidar measurements may be used in the study of cloud and aerosol interactions and their influence on the climate. Several lidar based technologies are currently used in the climate study field.

Networks of autonomous low-power, or micropulse lidars, for example MPLNet hereinafter referred to as MPL, use elastic backscatter for cloud and aerosol observation. This technology is capable of supplying qualitative observational data, but does not provide accurate quantitative data. The MPL performs two backscatter-polarization measurements, with three unknowns of polarization, backscatter and extinction. Similarly, Vaisala ceilometers perform backscatter measurements with one measurement and two unknowns (backscatter and extinction) so the two atmospheric optical parameters cannot be retrieved. This requires making certain a priori assumptions regarding the relationship between backscatter and extinction in order for atmospheric optical parameters to be determined.

Raman lidar is currently used to provide quantitative atmospheric backscatter and extinction by measuring the Raman shifted backscatter intensity of nitrogen in the atmosphere. The total backscatter and molecular backscatter measurement are used to determine calibrated backscatter and extinction. The backscatter of molecules is relatively stable and provides an optical constant employed to compare total backscattered signals. The backscatter coefficient of the target volume can be determined and deviations in the expected molecular backscatter from that actually measured provide atmospheric extinction or transmission data. Raman scattering is several orders of magnitude weaker than elastic backscatter Implementation of Raman lidar instruments therefore require powerful lasers, which, in turn are poorly suited network operation since these are generally expensive, require cooling, may not produce an eye-safe beam, and require routine maintenance such as flash lamp changes and cavity alignment.

Lidar systems that rely on elastic backscatter signals, allow the laser pulse energy to be significantly reduced, and are simpler to make into an eye-safe system. To make a quantitative measurement of aerosol properties with an elastic backscatter lidar the high spectral resolution lidar (HSRL) technique can be used. The elastic backscatter from molecules is significantly spectrally broadened compared to elastic backscatter from aerosols and clouds. The molecular backscatter can be separated from the aerosol/cloud backscatter by using a narrow band filter to block the spectrally narrow cloud and aerosol backscatter, only allowing the wings of the much broader molecular backscatter to pass. Some HSRL systems have relied on etalons to create these narrow spectral filters but they only offer a limited optical depth and restrict the etendu of the receiver system.

Etendue is defined as a property of light in an optical system, which characterizes how “spread out” the light is in area and angle. Etendue never decreases in any optical system and a perfect optical system produces an image with the same etendue as the source.

Iodine absorption cells have been used as spectral filters for frequency doubled Nd:YAG lasers operating at 532 nm, but finding lasers that are small, low maintenance and operate with sufficiently narrow line widths at 532 nm presents a significant cost and reliability challenge.

What is needed is a network of deployable cloud aerosol lidars that are low-cost, eye-safe, reliable enough to run continuously for years without maintenance, and must provide both qualitative and quantitative optical data without applying a priori assumptions.

A potential solution is to develop a diode-laser-based high-spectral-resolution-lidar (DLB-HSRL.) This option requires sufficient transmit power, proper wavelength, system reliability, component reliability and a low enough cost in order to make remote network deployment a practical option. However, to achieve the improved data products over existing commercial systems, the DLB-HSRL needs lasers with stable and narrow line-widths and a matching receiver filter with similarly narrow rejection spectra but high optical depth. This must be accomplished without significantly increasing the cost, size, or maintenance requirements of the system.

## SUMMARY OF THE INVENTION

The present application is designed to improve understanding of clouds and aerosols by providing quantitative data products. The present application describes a diode laser-based high spectral resolution lidar (DLB-HSRL) featuring low power consumption and electrically pumped semiconductor transmitters capable of operation for tens of thousands of hours without the requirement for water cooling. A benefit is lower operation and maintenance costs when compared to traditional quantitative lidar systems. The DLB-HSRL provides data products similar to current Raman lidar and HSRL systems but at a cost, size and complexity competitive with current commercial non-quantitative elastic backscatter lidar systems.

## ASPECTS OF THE INVENTION

In one aspect of the invention, a diode laser based high spectral resolution lidar comprises:

a diode laser emitting a laser beam, a splitter which separates the laser beam, an inline fiber isolator and a tapered semiconductor optical amplifier which receives a portion of the laser beam and amplifies it into pulses which are transmitted.

Preferably the device further comprises:

a telescope to receive reflected laser light, an interference filter to receive the reflected laser light and filter the reflected laser light, a narrow band etalon to receive the filtered reflected laser light and reduce background light, a beam splitter for splitting the reduced background light into a first portion and a second portion, a total detection channel which receives at least one of the first portion of the reduced background light and the combined molecular collected backscatter and the aerosol and cloud collected backscatter, a heated rubidium vapor cell which receives the second portion of the reduced background light and blocks a spectrally narrow cloud and aerosol collected backscatter and passes wings of molecular collected backscatter, a molecular channel detector for receiving the wings of molecular signal.

Preferably the laser uses at least one of a distributed Bragg reflector (DBR), or a distributed feedback (DFB) laser.

Preferably the laser has a wavelength of approximately 780 nanometers.

Preferably the laser beam is split into a portion that is received by the inline fiber isolator and the tapered semiconductor optical amplifier which receives a portion of the laser beam.

Preferably the portion of the laser beam not received by the inline fiber isolator and the tapered semiconductor optical amplifier is sampled and directed to at least one of a wavelength meter or a device for monitoring and controlling the wavelength of the laser.

Preferably the total detection channel further comprises a depolarization channel.

A diode laser based high spectral resolution lidar method of analysis comprises:

generate a laser beam, split a laser beam into a first portion and a second portions, generate high energy pulses from the first portion of the laser beam, expand the first portion of the laser beam, transmit the filtered portion of the laser beam, reflect the transmitted laser beam, receive the reflected laser beam; and analyze the reflected laser beam.

Preferably the laser beam is performed using at least one of a distributed Bragg reflector (DBR), or a distributed feedback (DFB) laser.

Preferably the generating high energy pulses is performed using tapered semiconductor optical amplifier.

Preferably the expanding of the laser beam is performed using an axicon pair.

Preferably transmitting the expanded portion of the laser beam is performed using the inner portion of a telescope.

Preferably the receiving the reflected laser beam is performed using the outer portion of a telescope.

Preferably the received reflected laser beam is passed through an interference filter and a narrow band etalon.

Preferably the analysis further comprises passing the reflected laser beam through a heated rubidium vapor cell.

In one aspect of the invention, a diode base high spectral resolution lidar comprises:

a laser emitting a laser beam, a splitter which separates the laser beam, an amplifier which receives a portion of the laser beam, prisms which receive and expand the laser beam; and a telescope which transmits the laser beam.

Preferably the device further comprising:

a device which receives reflected laser light, a filter to receive the reflected laser light, an etalon for receiving the filtered reflected laser light, a device for analyzing the filtered reflected laser light.

Preferably the amplifier comprises a tapered semiconductor optical amplifier.

Preferably the telescope comprises an inner portion that transmits laser light and an outer portion that receives reflected laser light.

Preferably the reflected light is analyzed using at least one of a heated rubidium vapor cell and a depolarization channel.

## DETAILED DESCRIPTION OF THE INVENTION

FIG. 1 and the following description depict specific examples to teach those skilled in the art how to make and use the best mode of the Application. For the purpose of teaching inventive principles, some conventional aspects have been simplified or omitted. Those skilled in the art will appreciate variations from these examples that fall within the scope of the Application. Those skilled in the art will appreciate that the features described below can be combined in various ways to form multiple variations of the Application. As a result, the Application is not limited to the specific examples described below, but only by the claims and their equivalents.

FIG. 1 depicts a conceptual layout of the DLB-HSRL system. The DLB-HSRL uses a distributed Bragg reflector (DBR) 780 nm laser (101) which provides a source with power and frequency stability needed for accurate filtering of molecular and aerosol backscatter in an DLB-HSRL receiver.

A computer operable (118) standard diode laser controller (117) operates the DBR laser (101) at constant temperature. Approximately ten percent of the laser output (102) is sampled and directed to a wavelength meter (103) or rubidium vapor cell to monitor and lock the laser output wavelength.

The remaining ˜90 percent of the laser output (104) passes through an inline fiber isolator (105) and thereafter into a tapered semiconductor optical amplifier, hereinafter TSOA (106). The laser source is then amplified by the TSOA (106) to produce a transmitted laser pulse and to achieve high enough output power for daytime operation. The current to the TSOA (106) is modulated to produce an output pulse or output pulse encoding where higher energy pulses are generated based on the current pulses supplied by a current pulser component (119).

The output energy is monitored (107) for later signal processing. The beam is expanded through a pair of axicon prisms (108), then passes through a splitter (121) and a lens (120) to reduce energy lost from the telescope spider (109) and finally transmitted through the inner portion of the telescope (110). This design uses a shared telescope design where the inner portion is dedicated to the transmitter and the outer portion is dedicated to the receiver.

This laser-amplifier combination does not require a cooling unit and occupies a volume that is a fraction of the size of a neodymium-doped yttrium aluminum garnet lasers, also known as Nd:YAG lasers, commonly employed in Raman and HSRL systems. The semiconductor lasers used in the DLB-HSRL are lower cost and longer lifetime than the Nd:YAG. Because these lasers require no cavity alignment, or realignment, or consumables such as flash lamps, they are zero maintenance and are therefore suitable for use in a lidar network. This is a significant contrast to Nd:YAG lasers.

The received light (111) is collected by the outer portion of the telescope and reflected by a mirror (112), a beamsplitter (121), then through an interference filter (113) and a narrow band etalon for reducing background light. An etalon is an optical device which reflects incoming light repeatedly between two or more reflective surfaces. Etalons may serve as a narrow band optical filter by means of interference effects. The light then passes through a beam splitter (114) where part is coupled into the fiber for the total detection channel. The other light passes through a heated rubidium vapor cell (115) which blocks spectrally narrow cloud and aerosol returns, passing only the wings of molecular returns into the fiber for the molecular channel detector (116).

A depolarization channel is not shown in the schematic but is easily added by splitting the light on the total channel with a polarizing beam splitter. Light exiting each port is then directed onto to detectors corresponding to the total parallel and total perpendicular backscatter.

To perform the HSRL technique, a rubidium (Rb) cell of isotropic Rb 87 is heated to approximately 320 K, where the optical depth is sufficient to block strong backscatter from liquid water clouds. Optical depth is a measure of how much light is transmitted through a medium or device. It is the natural logarithm of the ratio of initial to the transmitted optical power and describes the ability of the medium or device to extinguish incident light.

Operation of the laser occurs at 780 nm wavelength, where the D2 line of rubidium is strongly absorbing. This wavelength overlaps with a well-developed line of necessary commercial components such as the DBR lasers (101), TSOA (106) and silicon-based single-photon-counting detectors. These components are available as fiber-coupled devices, an essential ingredient to maintain instrument alignment in an unattended network deployment. Thus, the rubidium filter in the lidar receiver, coupled with a fiber-coupled diode-laser-based transmitter, enables a low-cost and low-maintenance HSRL technique capable of providing quantitative lidar data products.

The detailed descriptions of the above embodiments are not exhaustive descriptions of all embodiments contemplated by the inventors to be within the scope of the Application. Indeed, persons skilled in the art will recognize that certain elements of the above-described embodiments may variously be combined or eliminated to create further embodiments, and such further embodiments fall within the scope and teachings of the Application. It will also be apparent to those of ordinary skill in the art that the above-described embodiments may be combined in whole or in part to create additional embodiments within the scope and teachings of the Application.

