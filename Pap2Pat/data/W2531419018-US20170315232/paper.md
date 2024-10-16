# Introduction

High-frequency (HF) radars were first used for ocean observations in the 1960s. Located on the coast and transmitting vertically polarized radiations, they exploit the high conductivity of sea water to propagate their signals well beyond the visible or microwave-radar horizon. They have found widespread use for mapping surface currents and monitoring sea state.

Barrick [1] suggested in 1979 that these radars could detect tsunamis by means of their orbital wave velocity as they approach the coast. Because the distribution of radars around the world was sparse until the 1990s, this concept was not pursued until the tsunami caused by the catastrophic 2004 Banda Aceh earthquake in Indonesia claimed a quarter of a million lives. Although there were no radars in place to observe that event, work began to quantify the radar tsunami response. It was not until the 2011 Tohoku (Japan) tsunami that sufficient radars were in place to capture real tsunami data, which led to development of algorithms to provide robust detection and warning. The Japan tsunami signal was observed by many HF radars around the Pacific Rim with clear results from sites in Japan, USA, and Chile [2][3][4]. Additional weak tsunamis have also been observed: the 2012 Indonesia tsunami [5] and the 2013 US East Coast meteotsunami [6]. A database of actual HF radar tsunami observations from both strong and weak tsunamis has been accumulated, which has been used to identify the tsunami current velocity signature in the background ocean current velocity field. An empirical method for the automatic detection of a tsunami has been developed, based on pattern recognition in the velocity time series. Over 350 HF radar stations operate from many coastal locations, see, for example, http://www.codar.com/seasonde_world_locations.shtml, providing continuous measurement of surface current velocities and waves. Tsunami detection software can run in a background mode, issuing a warning before the tsunami strikes the coast.

The first possible indication of a tsunami might be the seismic detection of an earthquake. However, not all subsea earthquakes produce tsunamis, and hence the magnitude of an earthquake cannot be used to forecast the detailed generation or intensity of a resulting tsunami. At present, the only operational sensor that detects a tsunami and measures its intensity is a bottom pressure sensor connected to a buoy overhead. Developed by the National Oceanic and Atmospheric Administration (NOAA), networks of these sensors called DART ™ (Deep-ocean Assessment and Reporting of Tsunami) were deployed after the 2004 event. They observe the height of the tsunami wave as it passes above them. The tsunami height measured by these buoys is then entered into numerical tsunami models [7][8] to give rough forecasts of the tsunami arrival time and intensity at coastal points around the world. As this network is located in the deep ocean, not all tsunamis are observable by DART and then are not entered into the model before coastal impact. Furthermore, the model's forecast of intensity at the coast is often coarse, so that more accurate estimates of intensity at specific locations are needed; such local variations not captured by the models are referred to as "near field." HF radars make their areal observations over this local near field and so provide an ideal solution to this need. We describe an empirical tsunami detection algorithm that can run in the background on these radars. This can detect and warn of an approaching tsunami in the near-shore region over which these radars observe the sea surface. A total of 21 offline radar detections of tsunamis have been made to date. Many are described here and others are reported in the literature [2,3,5]. A tsunami's orbital velocity appears as part of the surface current as the wave approaches the coast. Tsunami periods lie typically between 20 and 50 min. A tsunami originates when there is a massive displacement of water: The spatial scales of water displacement are the spatial scales of water displacement are usually of great horizontal but small vertical dimensions These include subsea earthquakes where plates force each other upward/downward, respectively; subsea landslides along steep submerged mountainous slopes; or fast-moving atmospheric anomalies (e.g. low-pressure centers) that create "meteotsunamis." The sources can be thousands of kilometers from an impacted coastal area (where an HF radar might be located), or very close. As the displaced water mass leaves its source region under the influence of gravity, it becomes a freely propagating shallow-water wave. Although the origins of meteotsunamis vis-à-vis seismically generated tsunamis differ, the propagation and evolution of these shallow-water waves are the same, as are the applicable detection and warning methods. Tsunami warning times are mainly dependent on the width of the adjacent continental shelf, ranging from minutes for a narrow shelf (e.g. California) to hours when the shelf is broad (e.g. New Jersey). Some sites may be less suitable for tsunami monitoring by radar, as the tsunami signature can be masked by large, variable background currents. Tsunami detection is favored by shallow water extending far offshore and by slowly varying background current fields. We describe a method for the evaluation of a coastal site for tsunami warning based on simulated tsunami velocities superimposed on the site's measured velocities. Factors affecting radar detection of tsunamis are discussed. Difficulties that can occur in tsunami detection and methods for alleviation are described. At present, work on the evaluation of coastal sites for tsunami warning using HF radars is being performed in a partnership between Codar Ocean Sensors and NOAA.

It is often convenient to identify Codar SeaSonde ® radars by their abbreviated site names used in the field. Those referred to in this article are listed here in alphabetical order, along with their geographical locations: 

# Tsunami theory and modeling applicable to HF radar observations

In this section, we provide a brief synopsis of tsunami theory and numerical modeling, as required to explain and develop the HF radar coastal observation/warning capability. We refer to a region of interest near the coast, or within the coverage area of a coastal HF radar, as the "near field," typically of ranges up to 50 km.

## Fundamental equations describing a tsunami in the near-field region

Two equations form the basis of tsunami wave theory and propagation modeling. They are the essence of NOAA's Method of Splitting Tsunami (MOST) over near-field distances but away from the coastal run-up zone where flooding is experienced [7][8]. The first is essentially Newton's second law, that is, force = mass times acceleration, which for fluids gives the Navier-Stokes vector equation to the lowest order. For horizontal coordinates x and y and time t, this is given by:

where η(x, y, t) is the tsunami wave height, g is the acceleration due to gravity, and (, , ) is the orbital velocity of the wave. We assume, as in [7][8], that the orbital velocity at a particular location is independent of depth. The second equation is the continuity equation that expresses the incompressibility of water:

where d(x,y) is the depth below a mean datum reference, from which the tsunami wave height is measured. The left side of this equation is the net horizontal water volume transport per unit time into a vertical column. Eq. ( 2) simply expresses the fact that the net flow per unit time into the column of incompressible water must be matched by the rate of rise in the water elevation.

As it stands, Eq. ( 2) is nonlinear because the two dependent variables, height and velocity, on the left side are multiplied together. Because the tsunami elevation is small compared with the water depth (typically less than 0.5 m in deep water), the height in the left-hand side of the equation can usually be neglected, upon which the equation becomes linear.

## Reduction to partial differential equations (PDEs)

Eqs ( 1) and ( 2) represent coupled equations in the unknown tsunami wave height and orbital velocity. By differentiating with respect to time and/or space, as relevant, we eliminate one variable, arriving at the following two hyperbolic PDEs for tsunami height and velocity:

We first solve the scalar Eq. ( 3) for height. Then orbital velocity is obtained by integrating the left side of the linearized Eq. ( 2) as a function of time. Radars measure orbital velocity, rather than the tsunami height measured by other tsunami sensors.

These are well-known equations for waves in shallow water. They are justified when water depth is much less than the horizontal scale of the water wave, for example, its wavelength. Horizontal scales of a tsunami wave exceed tens of kilometers, so that even in water several thousand meters deep the tsunami is always a shallow-water wave everywhere on the planet. The time scales (periods) for tsunami waves that represent hazards are large, varying from 20 to 50 min.

Another useful quantity applied to shallow-water waves is their phase velocity v ph that is given in terms of the water depth by:

The phase velocity for a tsunami wave train traveling across the ocean with depths from 100 to 1000 m typically exceeds 100 km/h, while the orbital velocities encountered are tens of centimeter/s or less. The water particles themselves move at the orbital velocity, while the surface velocity that the eye would follow as the wave rushes across the ocean is the phase velocity.

We define the "near field" over which the linear model applies as ranging from about 2 km from shore (beyond first radar range cell) out to as far as the radar can see, ∼50 km from the coast. The PDEs (3) and ( 4) are exact under the accepted linearity assumptions and can handle sharp bottom depth changes and reflections or partial absorptions at coastlines. Typically, they are solved with standard finite-element methods [9]. Over near-field distances, they can be solved on personal computers.

## Ray optics and Green's Law approximations for tsunami waves

Traveling waves, such as tsunami or electromagnetic waves, sometimes follow simple ray optics approximations where they can refract, changing their direction continuously with the refractive index. The refractive index for waves of any nature propagating through media with different or changing properties is defined as the ratio of the reference phase velocity to the phase velocity at the specific point in the medium. For light or electromagnetic waves, the reference velocity is taken as the speed of light in vacuum. For acoustic waves or water waves in the shallow-depth limit, one normally selects a convenient reference velocity [10]. So, for example, if one selected the 4000-m depth which is typical of a deep ocean basin, the refractive index becomes 4000/, which is sometimes referred to as the HF asymptotic limit. This approximation applies only when refractive index varies slowly and smoothly with distance. This means that the refractive index cannot have a discontinuous jump, for example, if the bottom had a significant change in depth over scales shorter than a wavelength, say 10 km. Bottom depth fluctuations over smaller scales are not important to tsunami propagation. The tsunami wave, with its massive inertia, is like a low-pass spatial filter that effectively averages across these fine-scale features. A wave typically does not respond appreciably to perturbations with a scale much smaller than its wavelength; this is sometimes known as the Rayleigh criterion. As tsunami wavelengths exceed tens of kilometers, this implies that perturbations with smaller spatial scales (e.g.10 km) are unimportant. There is an often-asked question: "Do I need to use a bathymetry database for tsunami near-field modeling with 1-2 km resolution?"

The answer is "No: 10 km resolution is always adequate."

We now examine simplifications possible when depth varies slowly, and discuss exact alternatives that will work when depth varies abruptly.

### Ray optics approximation

When depth and refractive index vary slowly, ray tracing allows a version of Fresnel's law such that the advancing wave continuously refracts, so that its direction of propagation follows the gradient of refractive index perpendicular to the isobath depth contours. This approximation has the consequence that there is always only one set of ray paths, which end up perpendicular to the coastline. The coastline boundary will reflect; outgoing rays also cross the contours perpendicularly.

When depth and refractive index vary abruptly, it is valid to use Eqs (1-4) as an alternative. Models based on these equations, for example as described in [7][8], will predict the direction correctly and will generate components parallel to the contours and coastline, as has been observed by radars [2,5]. Incorrect use of ray tracing for these situations will show evolution with some error of the forward ray toward the region of shallower water near the coast, but can never predict a parallel component.

### Green's Law approximation

When refractive index (depth) varies slowly, Green's Law [11,12] applies. In this limit, tsunami height and orbital velocity follow simple relationships in terms of depth, as described in reference [1]. It is convenient to normalize the height to a value of the tsunami height in deeper water; we take this depth to be 4000 m, typical for an ocean basin; other depths can be used. The approximate tsunami wave height and scalar tsunami orbital speed in water of depth d are then given by:

1/ 4 4000 (4000 / )

3/ 4 4000 / (4000 / )

where η 4000 is the tsunami height in water of depth 4000 m.

## Comparison of Green's Law amplitudes with exact calculations

How accurate are the approximations in Eqs ( 6) and ( 7) for tsunami height and velocity? To get an idea of this, we compare the height approximation with solutions of the exact Eqs (1-4) for specific cases.

Case 1: A typical continental shelf with a steeply sloping edge that goes from an outer depth of1000 m to an inner depth of 50 m over a horizontal distance of 20 km. Defining the transmission coefficient as the ratio R T of the tsunami height after passing over this shelf to that before striking the shelf's lower edge, Green's Law Eq. ( 6) gives R T = 2.11. The solution of the PDEs (2) and (3), discussed further in Section 5, gives R T = 1.68. These values for R T agree to within about 25%.

Case 2: A vertical shelf edge parallel to the coast falling perpendicularly from depth 50 to 1000 m. Clearly, this fails the "slow depth change vs. tsunami wavelength" criterion required for both ray optics and Green's Law and thus is beyond the scope of these approximate models.

For normal incidence to a vertical escarpment, NOAA modelers [8] express Eqs (1-4) as a boundary-value problem requiring continuity of height and transport across the escarpment and obtain the following exact expression for the transmission coefficient of the tsunami wave height:

where D 1 and D 2 are the depths on the shelf's outer and inner edges, respectively. This is considered an exact solution for this defined geometry. Substituting D 1 = 1000 m and D 2 = 50 m yields a value for R T equal to 1.63, which is close to the prior estimate from the PDE calculation.

To conclude, the exact solutions for transmission coefficient R T for a depth change from 1000 to 50 m are (a) 1.68 over a steep slope and (b) 1.63 over a vertical step. These values differ by only about 3%, indicating that shelf slope does not have a significant effect on the transmission coefficient. Comparing these values with the Green's Law approximation of 2.11 suggests an error estimate of about 25% when using Green's Law for estimating tsunami height change due to sharp depth changes.

## Tsunami arrival time

Solving Eqs (2-3) provides both the tsunami height and orbital velocity profiles as the wave approaches the coast, as impacted by the decreasing depth on the journey toward shore. This yields the most accurate estimate for the arrival time from any offshore point along its path and is useful in near field of the coastal radar because the computational effort is manageable.

However, for an approach from much farther out, or in order to get a quick, rough estimate of the tsunami arrival time, the phase velocity v ph (d) at depth d, time t, and distance s along a tsunami great-circle ray path can be expressed as follows:

Eqs ( 5) and ( 9) lead to the following approximate solution for the elapsed time ΔT for the tsunami arrival at distance S from the start:

Because of inherent smoothing of the integration process, the depth profile need not be defined to great resolution, allowing quick use of Eq. ( 10) over large ocean distances to give rough estimates of the tsunami arrival time.

# HF radar observations of the 2011 Japan tsunami leading to an empirical detection algorithm

Radar echoes are produced by reflection of the radar wave from ocean waves with wavelengths half that of the radar; such waves have periods between 1.5 and 4.5 s. In contrast, the tsunami wave period lies between 20 and 50 min, corresponding to wavelengths between 400 and 800 km in the open ocean. Tsunami orbital velocities add to the shortwave radial velocities producing the radar echo; in deep water, tsunami velocities are too small to be seen by the radar, but they increase as the tsunami moves onto the continental shelf and the water depth decreases below 200 m and can then be observed by radars located on the coast.

Radial current velocities are obtained from the first-order radar echo spectra measured at individual radar sites [13,14]. In usual practice, several radar echo spectra are averaged over time before analysis. As time resolution is critical for local tsunami detection, unaveraged spectra are analyzed. The Doppler shift from the ideal Bragg frequency defines the radial current speed; spectral values at that frequency are interpreted to give the azimuth angles at which this speed occurs. Together with range defined by the time delay, estimates follow for the radial current velocity at locations spaced 1° apart around a circular range cell centered on the radar site.

Total current velocities are obtained by combining radial velocities from the radar sites [13]. A grid is formed over the radar coverage area and averaging circles form surrounding each grid point. Total velocity vector components are calculated by fitting to radial velocities from the different radar sites that fall within the averaging circle.

On March 11, 14:46 2011 Japan Standard Time (JST), a magnitude-9 earthquake off Sendai, Japan, unleashed a large tsunami that was observed by HF radars around the Pacific Rim, see  The radars had a transmit frequency of 42 MHz and a range increment of 0.5 km. The water depth over the entire radar coverage area is less than 200 m. The 42 MHz frequency band is used for high-resolution, short-range current observations and results in a radar range less than 15 km, due to significant attenuation of the surface wave passing across the sea at these higher HF frequencies.

## Total velocity current maps

The direction and strength of the flow were measured at approximate 4-min intervals with a cell resolution of 0.5 km × 0.5 km. Figure 2 shows total current-velocity maps, the first demonstrating the arrival of the tsunami, indicated by strong inward flow, the second an example of outward flow. Eqs ( 6) and ( 7) relate the tsunami height to the current velocity; heights are displayed in colors superimposed on the velocity vectors shown by the arrows. As noted in Section 2.3.2, the accuracy of Green's Law estimates of height decreases close to shore.

A video showing the current velocity/height flow from March 11, 14:06 JST to March 12, 13:54 JST is shown in Video 1, available at http://bit.ly/29lOdXw Time in JST is given in each frame of the movie. The video shows the tsunami arriving at 15:53 JST and then sweeping in and out of Uchiura Bay.

## Radial velocity components

As would be expected, the tsunami signal is also visible in the radar returns from a single radar site [3]. To simplify the analysis of the data with the aim of developing objective detection criteria, we group the radial velocities into rectangular area bands 2-km wide approximately parallel to the depth contours. The radial velocities are resolved into components perpendicular and parallel to the area bands. These components are averaged over the band; the averages are termed "band velocities." A time series of the band velocities is then formed, which displays the characteristic oscillations produced by the tsunami.     

## Detection of the tsunami signal in HF radar data

Two effects distinguish tsunami velocities from the background in Figures 4 and5: (a) velocities in neighboring bands are strongly correlated after the arrival of the tsunami and (b) the velocity oscillations are clearly visible above the background. These effects appear to be characteristic of tsunami band velocities, as they occur in all the radar data from Japan and the US West Coast that we have analyzed. They form the basis of a simple pattern detection procedure. At a given time, a factor (which we call the q-factor) is defined which signals the tsunami arrival when it exceeds a preset threshold. The steps in the detection algorithm are as follows:

• Step 1: Within each band, check whether the velocity increases or decreases by an amount greater than a preset level over two consecutive time intervals. If it does, increase/ decrease the q-factor level for that band.

• Step 2: Do the maximum/minimum velocities for consecutive bands coincide (within a preset value) for consecutive time intervals? If so, increase/decrease the q-factor level further for that band and time.

• Step 3: Finally, check whether the velocity increases/decreases over two consecutive time intervals for three adjacent area bands. If so, increase/decrease the q-factor level further for that band/time.

Details of the detection algorithm are given [6].

Positive q-factor values indicate the tsunami velocity at the wave peak is moving toward the radar, negative values indicate that it is moving away.

To set the operational threshold signaling a tsunami detection, an extended data set obtained under normal conditions is analyzed to produce q-factors. A threshold value is then selected.

There is a trade-off in the threshold selection: if the q-factor limit is set too low, the peak will certainly indicate a detection, but there may be many false-alarm detections. If the threshold is set too high, there will be few false alarms, but then the tsunami arrival may not be detected.

The tsunami signal can be evident for some time after arrival; however, our detection method is optimized to apply to the first arrival.

## Radar detection of the 2011 Japan tsunami

The Japan tsunami arrival was detected offline at radar sites around the northern Pacific Rim [3]. We here give examples of q-factor tsunami detections and compare arrival times at the radars with those measured by neighboring tide gauges.

### Hokkaido, Japan

Figure 6 shows the locations of two radars on the Kameda Peninsula, the neighboring tide gauge, and the offshore bathymetry. The water depth is less than 200 m over the radar coverage area; we found that the tsunami signal is visible in the current velocities out to the radar range limits.  Figure 7 shows A088 band velocities obtained over a 5-h period and the q-factors resulting from application of the analysis described in Section 3.3. About an hour after the earthquake, the tsunami arrived at A088, resulting in distinctive correlated oscillations in the perpendicular band velocities, which lead to a q-factor peak that indicates the tsunami arrival.

Close to shore, part of the tsunami flow is diverted by the steep bathymetry to move parallel to the coast, resulting in a reduced signal in the perpendicular component plotted in Figure 7. As discussed in Section 2, this effect can be shown by exact PDE modeling.

The analysis procedure was applied to A087 and A088 for all permutations of three band velocities that contained the tsunami signal, and the resulting q-factors were summed. The q-factor threshold was defined to be 500: the first q-factor to exceed this value was taken as defining the tsunami arrival time. Table 1 shows that the arrival times obtained from the radar q-factors reported are in the correct order: the tsunami arrives at Station A087 further from the earthquake location approximately 5 min after it reaches A088. Arrival times measured by the radars preceded those at the neighboring tide gauge by an average of 40 min, due both to the "quadrature relation" between velocity and height (discussed later in Section 4.1) and the tsunami propagation delay between the two observations.

### West Coast of USA

Radar spectra measured by 10 radars located along the US West Coast were analyzed to give band velocities and q-factors. Arrival times were compared with those at local tide gauges.

Figure 8 shows radar and tide gauge locations and the offshore bathymetry. As the adjoining continental shelf is narrow off California and Oregon, the tsunami is often detectable only for close-in ranges.  We illustrate the tsunami detections with two examples of measured band velocities and derived q-factors.

Our first example is the tsunami detection by the radar at YHS2, Oregon (transmit frequency 12 MHz).

Figure 9 shows the band velocities and corresponding q-factors.

The correlation is evident between the velocities in different bands starting at about 3:45 pm Coordinated Universal Time (UTC), resulting in a sharp decrease in the q-factor, which indicates the tsunami moving offshore, resulting in a decrease in water level. The neighboring South Beach tide gauge observed an initial water level increase due to the tsunami of just 0.3 m, which was inadequate to produce a radar detection. However, we note that in Figure 9(ac) the band velocities show the typical correlation due to the tsunami just before the sharp decrease.

Our second example is the tsunami detection by the radar at ESTR in Southern California (transmit frequency 13 MHz). Figure 10 shows the band velocities and q-factors for ESTR. The observed background current velocities are quite variable for this site: it is the correlations between velocities in different bands that allow the tsunami to be detected by the patternrecognition algorithm described in Section 3. Table 2 shows that listed arrival times obtained from the radar q-factors reported are normally in the correct order; thus, it arrives in Southern California after it gets to Northern California and Oregon. Arrival times measured by the radars preceded those at neighboring tide gauges by an average of 15 min, due to both the "quadrature relation" between velocity and height (discussed in Section 4.1) and the tsunami propagation delay between the two observations. We expect to be able to quantify the propagation delay using simulated tsunami velocity patterns derived from the analytical model, as discussed later in Section 5.1.

We note from Table 2 that the tsunami was detected even though water-level changes at neighboring tide gauges were not large, varying between 0.3 and 2 m.

### Chile

A WERA radar system operating at 22 MHz at a site near Concepcion, Chile, observed the Japan tsunami [4]. Current components pointing toward/away from the radar were measured within beams formed by the receiving antenna array. The orbital velocity of the shallow-water tsunami wave is therefore part of the total signal, which also includes other background contributions such as tides and geostrophic flow.  Figure 11 shows clear periodic disturbances produced by the tsunami in both radar and tide gauge observations. Obvious correlations in tsunami signatures can be seen for both measurements.

Dashed lines in Figure 11 give the depths within the main radar beam pointed offshore. The depth contours define a short continental shelf, followed by a steep slope. From a depth of about 50 m at 5 km, the depth drops to 1000 m at a distance of 34 km, that is, a steeply sloping region within a ∼29-km span. From there, the depth decreases slowly with distance beyond the shelf/slope region.

The tsunami component of these currents is identified from their typical periods that lie between 20 and 45 min, arriving at about 05:07 UTC on March 12, approximately 22 h after the Japan earthquake. This arrival time was confirmed by NOAA's tsunami model and the tide gauge data.

These observations have unexpected features as follows: (a) the tsunami peaks/troughs are seen out to 40-km range at approximately the same time regardless of distance from the shore and (b) beyond the shelf, where depths change slowly, from 760 m at 25 km to 1510 m at 40 km, the Green's Law approximation described in Section 2.3.2 should be valid. However, the observed velocity is nearly constant, which contradicts Eq. ( 7). These effects may be due to signal aliasing, as discussed later in Section 7.

# Radar observations of the 2013 US East Coast meteotsunami

An unusual storm system moved eastward across the US on June 13, 2013, commonly called a "derecho," and appears to have launched a meteotsunami that impacted the US East Coast.

The existence of the meteotsunami was confirmed by several of the 30 tide gauges along the East Coast up through New England and was seen as far away as Puerto Rico and Bermuda.

The event, which occurred during daylight hours, attracted widespread attention after several media reports were released focusing on local impacts including people being swept off a breakwater at Barnegat Light, New Jersey, some damage to boat moorings, and minor inundation.

Meteotsunamis generally do not have sufficient heights/energies to cause catastrophic loss of life, as do severe seismic tsunamis, although damage to harbors and coastal structures is common. The June 13, 2013 event, however, attracted significant attention among many agencies and scientific groups, probably due to its proximity to heavily populated areas.

## Origin of meteotsunamis and nature of the June 13, 2013 event

A meteotsunami is generated by an atmospheric pressure disturbance traveling across the sea.

An atmospheric anomaly (a low-or high-pressure center) will produce a small peak or trough moving at the same speed on the sea surface beneath it. This results in a freely propagating surface wave that increases in amplitude when the speed of atmospheric anomaly v aa matches the shallow-water wave phase velocity v ph (d). This is known as Proudman resonance, see [17].

The speed v aa of the June 13, 2013 derecho was about 21.1 m/s [15]. Substituting this value for v ph (d) into Eq. ( 5), it follows that the onset of the independent wave occurs at a depth d equal to 45 m, which lies about 60 km off the New Jersey coast.

This meteotsunami was unusual because it was generated by a frontal pressure anomaly traveling offshore. Yet coastal sensors including HF radars indicate that the meteotsunami approached the coast. Numerical models [8] indicate that a strong reflection occurred at the shelf edge about 110-120 km offshore, where the depth decreases from 100 to 1200 m over a distance of 20 km. The reflection is greater when a wave interacts with a drop-off rather than a step-up with the same slope. Data from New Jersey radars confirm the existence of a wave reflected from the shelf edge back toward the coast. This wave was also detected by coastal tide gauges.

To explain these results, we consider the interaction of the tsunami with a hard boundary, assuming a single pulse of water approaching the coast, that is, a traveling wave. The forward velocity is maximum at the wave crest. As a boundary is approached, there is a hard reflection:

the velocity goes to zero and the height doubles. This is known as the Neumann boundary condition. After a period of time from the reflection, a single wave travels outwards, with the crest velocity and height maxima in phase again.

In reality, the situation is more complex. Instead of a single wave or soliton, a series of positive and negative tsunami peaks often resemble a sine wave for height and velocity. The hard-wall boundary condition causes the height peaks to lag the velocity peaks by as much as a quarter cycle, which is termed the "quadrature effect." After reflection, the height stays positive but the velocity amplitude becomes negative. The interaction of incoming and reflected waves constitutes a more complex partial standing-wave situation, which is well handled by numerical model solutions.

## Radar detection of the 2013 US East Coast meteotsunami

We analyzed data sets from three SeaSonde HF radar systems located in New Jersey: BRNT, BRMR, and BELM. Radar transmit frequencies and range cell widths were approximately 13.5 MHz and 3 km, respectively. Radar results were compared with data from NOAA tide gauges at Atlantic City and Sandy Hook, New Jersey. Figure 12 shows the locations of the radars and tide gauges, and the offshore bathymetry. The meteotsunami height at the neighboring DART buoy, located about 240 km to the east, was only 5 cm [15]. Atlantic City tide gauge data obtained from the NOAA website [16] are shown in Figure 13. Readings show a maximum negative meteotsunami signal at approximately 18:42 UTC, indicated by the sharp water-level decrease. This is followed at approximately 22:00 UTC by a sharp increase in water level and subsequent oscillations.

As described in Section 3.3, the radar coverage area is divided into rectangular area bands 2km wide and approximately parallel to the depth contours. Radial vectors within each area band were resolved parallel and perpendicular to the depth contour. These velocity components are then averaged over the bands.

Figure 14 shows time series of four perpendicular band velocities from BRNT and BRMR and the corresponding q-factors, obtained from the four bands [6].

The arrival of the meteotsunami is signaled by a marked decrease in the perpendicular band velocity component, indicating an outflow, followed by correlation between different area bands. The parallel component did not display the tsunami signature. The water level measured by closest tide gauge at Atlantic City decreases when the tsunami arrives, as shown in Figure 13, also indicating an outflow of water.

The tsunami signal at BELM was far less, which is consistent with tide gauge measurements at Sandy Hook, 30 km to the north, which barely registered the tsunami arrival.

About 4 h later, after 22:00 UTC, BRNT velocities first increase and then sharply decrease, as is also shown by the Atlantic City tide gauge (see Figure 13). This effect was not seen at BRMR or BELM. To demonstrate more clearly the meteotsunami velocity trough as it approached the coast, BRNT band velocities were further processed as follows: the band velocities were first detrended over time, removing effects with time scales longer than 1.5 h, such as those due to tides. The detrended band velocities were then low-pass filtered and, to further reduce noise, averaged over two adjacent bands.

Figure 15 shows the smoothed velocities plotted as a function of time vs. range from shore, the dashed line indicating the progression of the first tsunami trough. Tsunami hindcast modeling [15] confirms this time-distance progression of the meteotsunami as it moved toward shore.

# Figures 14 and 15

show that the tsunami arrived first at the most distant ranges and progressively later moved toward the coast. To compare these results with theory, the tsunami arrival time at BRNT was calculated using Eq. ( 10), based on an initial detection at range 23 km. The bathymetry contours offshore from BRNT shown in Figure 12 were approximated by parallel contours, giving depth as a function of distance. As discussed in Section 2, this approximation is valid, as the tsunami is not affected by perturbations in depth with spatial scales far less than its wavelength. This analysis assumes no coastal boundary and results are expected to differ somewhat from radar-observed arrival times, as the orbital velocities are affected by shallow water.   The initial velocity observed by the radars was offshore, indicating a "trough" on the ocean surface. This was also observed by closest tide gauge at Atlantic City. However, as shown in Figure 15, the tsunami wave itself approached the coast due to a strong reflection occurring at the shelf edge 110-120 km from shore, see Section 4.1.

The meteotsunami was detected by the radars 23 km from the coast. It arrived at the shore 47 min later, as indicated by the tide gauge measurement of water level shown in Figure 13. The measured tsunami height was approximately 50 cm. These observations suggest that for similar tsunami height and bathymetry conditions, HF radar can provide a three-quarter hour warning alert before the wave strikes the shore.

# Calculation of simulated tsunami velocities and heights

Tsunami simulation provides an understanding of many of the factors affecting the capability of coastal HF radars to provide tsunami observation and warning. Ultimately, this can lead to performance assessment for a radar at a given site based on local bathymetry. Orbital velocities are tracked vs. time and related to the tsunami wave intensity. Comparisons with the background current field allow the assessment of possible warning time and wave amplitude as the tsunami approaches the coast near the radar. In this section, we describe two methods for simulating tsunami velocities: the first based on solving the fundamental equations to give total velocity/height maps and the second based on application of Green's Law to give simulated band velocities.

## Simulation based on solution of the fundamental equations of motion

To simulate tsunami height and velocity, Eqs ( 2) and ( 3) are solved numerically within the radar coverage area, typically out to ∼50 km from the coast. The offshore bathymetry is included as the depth variable, d(x,y), and the coastline becomes a boundary for the domain. First, the scalar Eq. ( 3) is solved for the tsunami wave height. Then, velocity is obtained by integrating the left side of Eq. ( 2) over time, after linearization as described in Section 2.1. This establishes the relations between the orbital velocity measured by the radar and the tsunami wave height, as well as provides the time of arrival at the coast from any point in the near-field region.

### One-dimensional tsunami

We examine here how a simple one-dimensional wave approaching normally to the coast behaves when it encounters a steep continental slope starting from depth 1000 m at a distance of 70 km from shore and sloping upwards to depth 100 m, at a distance of 50 km from shore. How do both height and orbital velocity change as they traverse this shelf? How much is transmitted across the shelf and how much gets reflected? On the return of the ray reflected by the coast, is there a second reflection going back toward shore? Answers to these questions are provided by Video 2 that can be viewed at http://bit.ly/29nKuLh Elapsed time in minutes is given in each frame of the movie. Colors represent the wave height (blue) and the orbital velocities (red). The coast was taken to be a Neumann reflecting boundary, that is, velocity stops perpendicular to the coast, where its magnitude is zero. The bottom profile including the shelf is shown as the heavy black curve at the top in the video. We note several points indicated by the video:

• The normalized height wave and orbital velocity wave come in from the right, toward the coast at the left. For this exact solution, the orbital velocity grows much faster than height as the wave advances onto the shallower shelf. This also follows from the Green's Law approximation given by Eqs ( 6) and (7), which indicates that height depends on depth d as d -1/4 , while velocity varies as d -3/4 .

• After coastal reflection, the height remains positive, while the direction of the velocity for the outgoing wave reverses. This is also true of the initial reflection at the bottom of the shelfedge slope, although this is below the visibility level in the movie. Thus, the reflected velocity changes sign while the height does not.

• The offshore retreating waves after coastal reflection encounter another strong reflection as they reach the top of the shelf edge 50 km offshore. In fact, these backward-reflected waves explain the meteotsunami that was observed in June 2013 from the New Jersey coast as discussed in Section 4. The original tsunami was launched by Proudman resonance [17] from the eastward-moving low-pressure center. When an atmospheric anomaly like a lowpressure center travels across the sea at the same speed as the shallow-water phase velocity (which depends on inverse square root of depth), a match or "resonance" is achieved. This causes the mound of water uplifted by the atmospheric low to break free and propagate as a tsunami soliton wave on its own. It was the returning reflected tsunami that impacted the coast and was reported by several radars and coastal tide gages. For more details, see [6] and Section 4.

It is from the output files of this one-dimensional simulation that we deduced the transmission coefficient cited in Section 2.4, which was compared with predictions from the Green's Law approximation.

### Two-dimensional tsunamis

We now examine two more realistic scenarios: in the first, a plane wave tsunami approaches the Portuguese West Coast and in the second, a tsunami is generated by a point source in the Alboran Sea. Videos are provided, which show tsunami height and velocity normalized by their initial values, as the tsunami is refracted by the bathymetry and reflects from the coast. In these videos, the background color represents the tsunami wave height normalized by its initial value, with the magnitude indicated by the color bar. Velocity vectors overlain on top of the height background represent the orbital velocities normalized by the initial value, with the magnitudes indicated by the vector length. Elapsed time shown on each frame indicates the time taken for the tsunami to reach various points along the coast. These simulated values can be tested against radar observations of real tsunamis. In both cases, reflection of the wave from the coast is clearly visible and the tsunami velocity increases more rapidly than the height as depth decreases, indicating that observed velocities provide a sensitive alert flag for a tsunami approaching the coast. Future work on this simulation will study results related to actual heights and velocities, rather than normalized values; output values can then be tested against radar observations of real tsunamis.

#### Portugal

The 1755 Lisbon earthquake in combination with subsequent fires and a tsunami almost totally destroyed Lisbon and adjoining areas. Tsunamis as tall as 20 m swept the coast of North Africa, and struck Martinique and Barbados across the Atlantic [18].

Using the actual offshore bathymetry, we simulated a tsunami approaching the Portuguese coastline from the west, results are shown in Video 3, available at http://bit.ly/29l4vCx Bathymetry contours are shown in order to understand the tsunami refraction. The epicenter was located more than 200 km to the west of the map. When the source is so distant, the initial condition for solving the PDE can be taken to be a plane wave, corresponding to a ridge of water traveling eastward. This approximation is reasonable whenever the source is distant from the near-field region and is convenient to model for numerical solutions. The domain for the numerical solution consists of the coastline of interest and the open box edges over the ocean. The coastline was assumed to have a Neumann (reflective) boundary condition.

This region was also selected for study because there are three 13.5-MHz SeaSonde HF radars operating at nearby locations, which are shown by green squares in the video. Tsunami observation software is being installed at these sites. The three radars would not see the tsunami if its propagation followed the line of sight from the source because the coast of southern Portugal would shadow those paths. In fact, the model output shows how the tsunami wave refracts and approaches the sites from the south. Reflection of the wave from the coast is clearly visible.

#### Alboran Sea

Another region of recent interest is the Alboran Sea, which is enclosed on three sides by Gibraltar on the west, Spain on the north and Morocco on the south. There are seismically active regions near tiny Alboran Island that could raise a localized mound of water, which would spread out under the influence of gravity, initially radiating a near-circular tsunami wave.

A point source is another initial condition that is easy to handle in the PDE solution [9].

Resulting maps are shown in Video 4 that can be viewed at http://bit.ly/29gMdPA.

The tsunami point source is located near Alboran Island (the green square marker) in water that is 1000 m deep. The tsunami radiates in all directions, intensifying in height and velocity as it moves into shallow water, as indicated by the bathymetry contours. As before, background color represents normalized height and vector length represents normalized velocity.

One can see as the movie progresses how different coastal regions are affected, as the approaching tsunami intensity increases. Offshore reflections and along-shore tsunami vectors are clearly seen from the vectors. The island is small compared to the tsunami wavelength, causing little observable effect.

## Band-velocity simulation based on Green's Law

This approximate procedure is based on the theory given in Section 2.3. To simulate velocities for a given test radar site over a period of time close to the arrival of a tsunami, band velocities from a real tsunami (termed reference velocities V Ref ) are superimposed on band velocities measured at the site (termed site velocities V Site ). Before adding to the site velocities, the reference velocities are adjusted for the site bathymetry using Eq. (7). They are then multiplied by an arbitrary factor F that can be varied to adjust the height of the simulated tsunami approaching the test site. This process is encapsulated in Eq. ( 11) for a given band:

where V Sim is the simulated velocity that for F = 1 would be observed if the reference tsunami approached the test site and Depth Site and Depth Ref are the average depths across the band for the test and reference sites. Increasing/decreasing the value of F will increase/decrease the size of the simulated velocity.

Simulated band velocities calculated using this approximate method are currently used to evaluate the suitability of radar sites for tsunami detection, as described in the next section.

# Evaluation of radar sites for tsunami detection using simulated tsunami velocities

As some sites are less suitable than others for tsunami monitoring with coastal radar systems, we are developing a site-dependent method that uses simulated tsunami velocities to estimate the size of a tsunami required to trigger a detection as a function of distance from the shore. This leads to an estimate of the warning time available. The tsunami simulation methods currently available have been discussed in the previous section. Tsunami simulation based on PDE model solutions of equations of motion is under development at this time with early results discussed in Section 5.1. As it does not yet produce actual (non-normalized) heights and velocities, as an interim measure, we use the approximate simulated velocities based on Green's Law described in Section 5.2.

## Evaluation method

The following steps are used to estimate the size of an approaching tsunami required for detection at the test site.

• Step 1: Measured tsunami band velocities obtained over a 5-h time period from the reference site V Ref are stored in a database.

# • Step 2:

The test site is assumed to be operating in its normal mode acquiring radial velocities, which are converted to band velocities V Site as described in Section 3.2 over a 5-h time period.

# • Step 3:

The reference set V Ref is adjusted for depth, multiplied by a factor F, and added to V Site using Eq. ( 11) to produce simulated velocities V Sim over the 5-h time period.

# • Step 4:

The simulated velocities V Sim are analyzed to produce q-factors, using the patternrecognition algorithm described in Section 3.3.

# • Step 5:

Steps 3 and 4 are repeated for a range of values of the factor F. The minimum value of F(F detect ) is sought that will lead to an acceptable detection of the q-factor peak, with an acceptably low false-alarm rate.

# • Step 6:

The tsunami velocity (V detect ) and height (H detect ) necessary to produce an initial detection of the tsunami follow from Green's Law, Eqs ( 6) and ( 7):

where ref init is the magnitude of reference velocity oscillation leading a detection of the tsunami arrival. Note that in these equations, V detect and H detect define the values where the band velocities are measured, not values very close to shore in the run-up zone, that can only be calculated using the highly nonlinear theory.

These steps are repeated using a sliding 5-h time window, running in the background of an operating radar system. The work described in this section is preliminary in nature and is being further developed in partnership with NOAA.

## Application at two test sites

We demonstrate the procedure for a single 5-h time window using as reference band velocities measured by the Kinaoshi radar (A088) during the Tohoku (Japan) tsunami, see Figure 4. Test radar sites are located at Bodega Marine Laboratory (BML1) on the US West Coast and Brant Beach (BRNT) on the US East Coast. BML1 has a steep offshore bathymetry profile, that is a narrow continental shelf; it also has low background noise. In contrast, BRNT has a shallow offshore bathymetry profile, that is a wide continental shelf, but this site has higher background noise. Our analysis shows that for these two radar sites, the offshore bathymetry dominates the tsunami detection capability. We compare predictions from the simulation with detections of real tsunamis: at BML1 of the 2011 Tohoku event and at BRNT of the 2013 meteotsunami.

Figure 17 shows depth vs. distance offshore for the reference site and the two test sites.

Clearly, depths for BRNT are much less than those for BML1, which is advantageous for tsunami detection because it offers longer time from the first alert to the arrival at the coast. However, the signal-to-noise ratios for the BRNT antennas were observed to be about 20 dB less than those for BML1, indicating noisy spectra and reduced tsunami detection capability. This is an example of variations in local external noise that are sometimes seen among coastal HF radars.

As the Green's Law approximation applies only when the depth varies slowly compared to the tsunami wavelength, we consider distances from BML1 less than 19 km, which correspond to the edge of the continental shelf, see Figure 17. For BRNT, this limit does not apply, as here the continental shelf extends beyond the limits of the radar coverage.  With the empirical detection algorithm applied to noisy background velocities, a nonlinear pattern results as the multiplicative factor F is varied in Step 5 of the evaluation analysis described in Section 6.1. As F is increased from zero, the q-factor increases in stages as different components of the detection methods apply to the band velocities. When the q-factor exceeds the preset limit, this defines the value of F(F detect ) that signals a detection. Preset limits are set produce minimal false alarms while allowing detection of observed tsunamis. In Figure 18, F detect is plotted vs. range from the radar: range is defined as the central value for the five 2-km bands, for example, for bands 1-5 (distance from shore 0-10 km), the central value is 5 km.

Step 6 of the analysis procedure is then applied to estimate for each range the tsunami velocity and height necessary for the detection of the initial tsunami approach. Parameters to insert into Eqs ( 12) and ( 13) were estimated as follows: Figure 7 indicates that the amplitude of the initial A088 (the reference) tsunami velocity oscillation V 088 is about 9 cm/s averaged from 0 to 10 km from shore, where the mean depth is approximately 60 m. Substituting these values, the depths from the site and the values of F detect shown in Figure 18, into Eqs ( 12) and ( 13) leads to estimates for the tsunami velocity V detect and height H detect required for a detection of the initial simulated tsunami approach. From Table 3, the height of the simulated tsunami required to trigger a detection is generally larger for BML1 than for BRNT particularly at greater ranges where the water is deeper. This occurs in spite of the lower BRNT signal-to-noise ratio, indicating that the shallow offshore bathymetry dominates the tsunami detection capability. We note that values shown in Table 3 are noisy. Noise reduction will require the analysis of more extended data sets.

## Comparison of test predictions with prior observations of real tsunamis

In this section, we compare predicted values of tsunami velocity required for a detection (shown in Table 3) with observations of real tsunamis at BML1 and BRNT.

### BML1

About 9 h after the March 11, 2011 Japan earthquake, the Japan tsunami was detected at BML1; see Figure 19, which shows the measured band velocities and corresponding q-factors close to the tsunami arrival. Using a threshold of 250, the blue q-factor peak for bands 1-5 indicates a detection of the Japan tsunami arrival at 15:45. Figure 19(a) shows that the amplitude of the initial tsunami velocity oscillation at BML1 was about 7 cm/s. There was no detection of the initial tsunami approach further from shore.

From Table 3, the simulation test predicts that the tsunami velocity required for an initial detection at BML1 at a 5-km range is ∼8 cm/s, which is approximately consistent with the observed velocity (7 cm/s) resulting in the initial detection of the Japan tsunami. The test indicates that larger tsunami velocities are required further from shore for detection to be possible. It also gives credibility to our simulation methodology.

### BRNT

From Figure 14, the magnitude of the initial meteotsunami velocity oscillation observed at BRNT 6-12 km from shore was ∼10 cm/s. This value can be compared with the test results in Table 3: averaging from 5 to 11 km, the predictions indicate that the velocity required to produce a detection is ∼17 cm/s. This conservative estimate may reflect a difference between the characteristics of a meteotsunami and an earthquake-caused event.

# Factors affecting detectability

In this section, we summarize five factors that can affect the ability of a radar site to detect and provide warning of an approaching tsunami.

## Water depth

Tsunami orbital velocities are small in deep ocean basins, with orbital velocity below the detectability threshold for HF radars. In the deep ocean, tsunami wave amplitude is always less than 1 m and wavelengths may be hundreds of kilometers. For example, fishermen 30 km offshore did not detect the huge Japanese tsunami of June 15, 1896. The tsunami height was only about 40 cm, but when the tsunami arrived at the shore, its height after run-up was 38.2 m [19].

As the tsunami moves onto the continental shelf, both velocity and height increase. Velocity, however, grows more rapidly with decreasing depth which gives advantage to the radar sensor. As the depth decreases, the orbital velocity can exceed a detection threshold. Based on our experience with small to moderate tsunamis in 21 HF radar detections, we use the 200-m isobath as a convenient demarcation for likely detectability.

The offshore bathymetry has a strong influence on HF radar tsunami detectability that is highly radar site dependent. It must be studied in simulations that guide the selection of detectability thresholds and other parameters for any tsunami warning methodology. This can be done using numerical models for near-field tsunami propagation based on the bathymetry offshore from the radar location, as described in Section 5.1.

## Tsunami height

The orbital velocity and tsunami height of course increase with the severity of the tsunami, and this is a second factor determining detectability. We note that tsunami heights producing radar detections as measured by neighboring tide gauges were not large, varying between 0.05 and 2 m. Tsunamis with orbital velocity amplitudes of 5 cm/s have been detected [5]. Detection of larger tsunamis would of course be easier, for example, the tsunami waves that reached heights of 40.5 m in Miyako, Japan, following the 2011 Tohoku earthquake [20] would be very easy to detect.

The estimation of the tsunami height at the shore is of course of major interest and at present can only be estimated by tide gauge observations because of the breakdown of linear modeling very close to shore. More advanced modeling, as described in Section 5.1, should alleviate this problem.

## Background currents

The orbital tsunami current must be detected among the ambient background flows that depend on a number of site-specific factors. Tsunami detectability may be degraded if there are large variations in the ambient current field over the tsunami period, which for the Japan tsunami and the US East Coast meteotsunami was approximately 40 min.

Existing networks of coastal HF radars have been installed primarily for reporting real-time currents. Such currents vary with location and time. Temporal variations may be either predictable (e.g. tides) or unpredictable (due to many causes, such as storms). Their patterns within the radar coverage where tsunami detection is desired can be quite complex. Some background flow variations may be mistaken for a tsunami and hence produce a false alarm in the absence of a good pattern-recognition algorithm.

## External background interference/noise

Man-made radio interference may lead to radar signatures similar to those produced by a tsunami, leading to false alarms. In some cases, this interference can be mitigated; in others, it may not be possible. This problem can often be solved on a case-by-case basis, having collected a database of received signals. This is the biggest factor apart from the intensity of a tsunami that limits its detection and can give rise to false alarms if the threshold is too low. Even sporadic interference can cause the q-factor pattern-recognition algorithm to give rise to false alarms. Initial radio surveys for new radar sites are required to check for interference. Selection of a clean frequency band can improve the situation for all sites.

Methods are needed to detect interference, along with filtering where possible to remove it. If it cannot be removed, then passing along to a tsunami warning center a disclaimer with any q-factor alerts during high interference periods, or raising the threshold, is critical.

## Signal aliasing

Strong echoes from close-in ranges can alias into distant range cells in systems that transmit while receiving. This "ringing" phenomenon produces spurious echoes in distant range cells that can be erroneously interpreted to be tsunami echoes. These far-out spurious echoes are easily distinguished from real tsunami echoes, as they appear at the same time as the real tsunami echoes from close-in ranges. If they were caused by a real tsunami, they would appear earlier at distant ranges. Also current amplitudes extracted from the spurious echoes are usually independent of depth. Fundamental, linear shallow-water wave physics [1,6] shows that the current amplitudes always decrease with depth. Observations from Chile of the Japan tsunami [4], discussed in Section 3.4.3, appear to show indications of "ringing."

# Dealing with false alarms

The first tsunami alert is indicated when the q-factor exceeds the preset limit. Due to the varying background current and noise/interference effects described in the last section, the detection might be a false alarm. The trade-off in the selection of the q-factor threshold is as follows: if the q-factor limit is set too low, the peak will certainly produce a q-factor alert, but many nontsunami false-alarm detections may be generated, degrading performance and operational acceptability. If it is set too high, false alarms will be eliminated, but then the first actual tsunami peak may be missed. This is the classic "probability-of-detection vs. false-alarm rate" trade-off encountered by warning sensor systems. An acceptably low false-alarm rate for a given tsunami intensity and detection distance from shore are the parameters to be optimized at each site. Judging by the strength of the q-factor signals seen in the Japan tsunami, it would appear that a tsunami having a run-up height of 1 m should easily be detectable with very low falsealarm rates in uncontaminated radar spectra, using the detection methods described earlier.

The value of the q-factor limit defining a tsunami detection is site specific and needs to be studied for the site under consideration. The most effective way to handle this for a given site is to study the background currents/extraneous effects and how the q-factor algorithm responds to them over a several month period.

We discuss two approaches for the reduction of false alarms:

## Search for correlations between q-factor alerts from adjacent HF radars

A real tsunami would be seen at two coastal locations say 30 km apart, for example, within a definable time window (say 15 min). Tsunami waves refract as they move into the evershallower water of the continental shelf near the coast. This means they tend to arrive perpendicular to the shore. This forces similar arrival times at neighboring locations along a nearly straight coastline.

Hence, if a high q-factor peak at Radar M arrives at a given range within 15 min of a high qfactor peak at Radar N, the presence of both raises the probability that a real tsunami is being seen by orders of magnitude. Likewise, if a high q-factor at Radar M has no counterpart at Radar N, this raises greatly the probability that the "alert" was in fact a false alarm. Thus, the solitary alert can be either eliminated as a false alarm or attached a flag to give it a much lower credibility.

## Search for correlations between q-factor alerts and earthquake notifications

At present, several services distribute online notifications within 2 min of an earthquake that has occurred anywhere in the world, which give latitude, longitude, time, and magnitude of the earthquake, see, for example [21]. Not all subsea earthquakes generate tsunamis. The assumption here is that any subsea earthquake with magnitude higher than 5 can be considered to be the origin of a tsunami. The approximate expected arrival time can be calculated from Eq. ( 10) using the depth profile between the earthquake origin and the radar near field of interest. A threat window can be set up within ±0.5 h of the predicted arrival time, and any q-factor candidates within this window would be given increased priority.

# Conclusions

The use of HF coastal radars to detect and warn of approaching tsunamis was proposed nearly 40 years ago [1]. Radars measure the tsunami wave's orbital velocity, unlike all other tsunami sensors that measure its height. However, it was not until the 2004 tragic Banda Aceh event that killed a quarter of a million people that attention was seriously focused on developing a local warning system. After the significant 2011 Tohoku, Japan tsunami, enough radars were in place worldwide to gather a radar-signal database that allowed the development of detection and warning methodology.

Several papers ensued demonstrating a detection algorithm and developments followed toward a methodology to capitalize on this near-field monitoring capability [2][3][5][6]. The present work presents a summary of these prior works and also covers recent work on tsunami simulation and site evaluation that has not been reported elsewhere.

In the last 5 years, tsunami events were detected by 21 SeaSonde HF coastal radars. Times between detection and arrival at shore (as confirmed by tide gages) ranged between 1 and 43 min. This alert time for a tsunami of given intensity depends principally on the offshore bathymetry. A shallow shelf edge affords a much longer alert time than a steep drop-off. We have examined and compared approximate and exact methods for estimating the arrival. The latter include the solution of exact linear partial differential equations, especially suited to near-field HF observations; in the future, this will also allow the radar-measured orbital velocity to be related to the height of the approaching wave.

We have also described steps toward simulation of tsunami height and velocity. This allows the assessment of the warning possible at a given site location based on the offshore bathymetry, background currents, and noise. False-alarm rate and probability of detection are the metrics against which performance is evaluated. Methods of increasing the latter while decreasing the former are examined. These include correlations with similar alerts from other nearby radars and with reports on seismic events that may constitute tsunamigenic sources.

After radars on the US East Coast detected a meteotsunami in 2013 that provided an alert that was missed by conventional methods, NOAA recognized the potential that the US Integrated Ocean Observing System (IOOS) could offer for tsunami warning. IOOS consists of 130 SeaSonde radars around the US coast. The NOAA Tsunami Warning Program office and IOOS entered into a partnership with Codar Ocean Sensors to optimize this capability based on steps outlined in this report and organized its transition to the two operational tsunami warning centers in Hawaii and Alaska.

It is clear that early local detection of incoming tsunamis by deployed radar systems is now within the capabilities of existing technology.

# Acknowledgements

Many thanks to Mason Kwiat for his invaluable help with the videos.

# Author details

Belinda Lipa 

