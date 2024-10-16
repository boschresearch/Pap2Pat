# DESCRIPTION

## BACKGROUND OF THE INVENTION

### 1. Technical Field

An embodiment of the present invention relates to a system and method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations.

### 2. Description of the Related Art

Glaciogenic seeding refers to a technology for making artificial snow by spraying silver iodide (AgI) that creates ice crystals using cloud seeds onto cold clouds (clouds of 0° C. or less) in the winter season. Such glaciogenic seeding is performed in terms of securing water resources and divided into airborne experiments and ground experiments.

Silver iodide, that is, a seeding material, is colorless and odorless, and thus it is difficult to check where the seeding material has been spread by a naked eye. Furthermore, there is a difficulty in detecting snowfall enhancement because observation devices for measuring snowfall enhancement which may be called a seeding effect are installed on limited places.

Airborne glaciogenic seeding experiments require the topography and weather condition of an area where the experiments are to be performed, experiment equipment, and a corresponding experiment design according to the volume. In airborne experiments, pieces of information about seeding for the execution of experiments chiefly depend on a weather condition. Accordingly, it is necessary to check the path and seeding effect of a seeding material in advance by exchanging a flight path and the amount of seeding in advance using a forecast field and performing numerical simulations.

In a conventional technology, however, there is a problem in that it is difficult to predict the results of airborne experiments for artificial snow enhancement because pieces of information about seeding for the execution of experiments chiefly depends on weather conditions in such airborne experiments.

## SUMMARY OF THE INVENTION

Accordingly, the present invention has been made keeping in mind the above problem occurring in the prior art, and an object of the present invention is to determine whether to perform airborne experiments by calculating a seeding line, a seeing period, the amount of seeding and a seeding altitude with consideration taken of an average direction and velocity of the wind when the airborne experiments are performed based on a detailed forecast field provided by the weather center using a numerical model and checking the spread of a seeding material and a distribution (i.e., a target area) of snowfall enhancement attributable to the seeding and to increase a rate of success of the airborne glaciogenic seeding experiments.

In accordance with an embodiment of the present invention, a method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations includes a first step for analyzing, by a weather factor analysis unit, weather factors of a target area for airborne glaciogenic seeding experiments, a second step for determining, by an airborne experiment possibility determination unit, whether airborne experiments are possible based on the direction of the wind, the velocity of the wind, temperature and humidity in the target area, a third step for determining, by a seeding information determination unit, seeding information by taking into consideration the direction of the wind and the velocity of the wind, a fourth step for performing, by a numerical simulation execution unit, numerical simulations using the seeding information, a fifth step for displaying and calculating, by an experiment calculation unit, a seeding material spread and distribution field using the results of the numerical simulations, displaying a precipitation increment and a region, and calculating an area, and a sixth step for determining, by a seeding effect determination unit, whether a seeding effect is present or not using the displayed and calculated results.

In accordance with another embodiment of the present invention, in the first step, the weather factor analysis unit may analyze the velocity of the wind, the direction of the wind, the temperature and the humidity, that is, weather factors of an experiment area for the airborne glaciogenic seeding experiments, using the vertical time-series diagram of weather center forecast data.

In accordance with another embodiment of the present invention, in the third step, the seeding information determination unit may determine the seeding information, including a seeding line, a seeding altitude, a seeding start time, a seeding termination time and the amount of seeding, by taking into consideration the direction of the wind and the velocity of the wind.

In accordance with another embodiment of the present invention, in the fourth step, the numerical simulation execution unit may generate information about a point, time and altitude regarding the domain of the seeding information using the seeding information and may perform SEED numerical experiments and criterion experiments or NOSEED experiments numerical simulations.

In accordance with another embodiment of the present invention, in the sixth step, the seeding effect determination unit may determine whether a seeding effect is present or not based on whether the seeding material has reached the target area or not and a precipitation increment and precipitation increase area attributable to the seeding using the displayed and calculated results.

In accordance with another embodiment of the present invention, the method may further include a seventh step for performing experiments or not performing experiments based on a result of the determination of whether a seeding effect is present or not.

In accordance with an embodiment of the present invention, a system for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations includes a weather factor analysis unit configured to analyze weather factors of a target area for airborne glaciogenic seeding experiments, an airborne experiment possibility determination unit configured to determine whether airborne experiments are possible based on the direction of the wind, the velocity of the wind, temperature and humidity in the target area, a seeding information determination unit configured to determine seeding information by taking into consideration the direction of the wind and the velocity of the wind, a numerical simulation execution unit configured to perform numerical simulations using the seeding information, an experiment calculation unit configured to display and calculate a seeding material spread and distribution field using the results of the numerical simulations, display a precipitation increment and a region, and calculate an area, and a seeding effect determination unit configured to determine whether a seeding effect is present or not using the displayed and calculated results.

In accordance with another embodiment of the present invention, the weather factor analysis unit may analyze the velocity of the wind, the direction of the wind, the temperature and the humidity, that is, weather factors of an experiment area for the airborne glaciogenic seeding experiments, using the vertical time-series diagram of weather center forecast data.

In accordance with another embodiment of the present invention, the seeding information determination unit may determine the seeding information including a seeding line, a seeding altitude, a seeding start time, a seeding termination time and the amount of seeding by taking into consideration the direction of the wind and the velocity of the wind.

In accordance with another embodiment of the present invention, the numerical simulation execution unit may generate information about a point, time and altitude regarding the domain of the seeding information using the seeding information and may perform SEED numerical experiments and criterion experiments or NOSEED experiments numerical simulations.

In accordance with another embodiment of the present invention, the seeding effect determination unit may determine whether a seeding effect is present or not based on whether the seeding material has reached the target area or not and a precipitation increment and precipitation increase area attributable to the seeding using the displayed and calculated results.

## DETAILED DESCRIPTION

Hereinafter, embodiments of the present invention are described in detail with reference to the accompanying drawings. However, in describing the embodiments, a detailed description of the known function or element related to the present invention will be omitted if it is deemed to make the gist of the present invention unnecessarily vague. Furthermore, it is to be noted that in the drawings, the size of each element may have been exaggerated and does not correspond to an actual size.

FIG. 1 is a flowchart illustrating a method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention. FIGS. 2 to 7 are diagrams for illustrating the method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention.

Hereinafter, the method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention is described with reference to FIG. 1.

First, a weather factor analysis unit analyzes the weather factors of an experiment area on which airborne glaciogenic seeding experiments are to be performed at step S110.

In this case, the weather factor analysis unit may analyze the velocity of the wind, the direction of the wind, temperature and humidity, that is, the weather factors of the experiment area on which airborne glaciogenic seeding experiments are to be performed using a vertical time-series diagram of weather center forecast data.

More specifically, the weather factor analysis unit may analyze whether the inflow of clouds is present or not and weather factors (e.g., the velocity of the wind, the direction of the wind, temperature and humidity) in a target area on which airborne glaciogenic seeding experiments are to be performed, for example, the Daegwallyeong district where Yongpyong ski resorts is located using the vertical time-series diagram of the weather center forecast data (UMRDAPS) shown in FIG. 2.

Thereafter, an airborne experiment possibility determination unit determines whether airborne experiments are possible or not based on the direction of the wind, the velocity of the wind, temperature and humidity of the target area at step S120.

More specifically, the airborne experiment possibility determination unit determines whether an airborne experiment is possible or not based on forecast data. In this case, a condition on the determination may be determined to be possible if all of conditions are satisfied in a condition table for determining whether an airborne experiment is possible or not in FIG. 3. For example, if it is expected that airborne experiments are possible because the velocity of the wind of 10 m/s or less, −5° C. or less and humidity of 80% or more are satisfied in the target area, a next step may be performed. If not, experiments may be determined to be not performed.

Thereafter, a seeding information determination unit determines seeding information by taking into consideration the direction of the wind and the velocity of the wind at step S130.

In this case, the seeding information determination unit may determine the seeding information, including a seeding line, a seeding altitude, a seeding start time, a seeding termination time and the amount of seeding, by taking into consideration the direction of the wind and the velocity of the wind.

More specifically, as shown in FIG. 4 showing a conceptual diagram for setting a seeding line for 8 bearings, the seeding line is calculated by calculating a distance S to a target point based on 8 bearings (north, northeast, east, southeast, south, southwest, west and northwest). The distance S is calculated by Equation 1 below.

S=average velocity of wind[unit:m/s]×response time[unit:seconds(s)]  [Equation 1]

In this case, an average velocity of the wind calculated using the vertical time-series diagram of the forecast field shown in FIG. 2 is used as the average velocity of the wind. The response time refers to the time that is taken for the seeding material to enter the clouds and to become snow through an ice crystal uncleation process.

For example, assuming that the response time is 30 minutes, the response time is 1800 s, that is, 30 minutes×60. Assuming that the average velocity of the wind is 5 m/s, S=5 m/s×1800 s=9000 m=9 km.

Thereafter, a numerical simulation execution unit performs numerical simulations using the seeding information at step S210.

In this case, the numerical simulation execution unit may generate information about a point, time and an altitude regarding the domain of the seeding information using the seeding information, and may perform glaciogenic seeding experiments (i.e., seeding numerical experiments) and criterion experiments or non-seeding experiments numerical simulations.

For example, the numerical simulation execution unit selects 6 hours anterior and posterior to a determined seeding time as a simulation time, calculates an input field and a boundary field using the weather forecast data (e.g., UM LDAPS) on the basis of the seeding line, and generates a file “air.seed.txt”, that is, information about a point, time and an altitude regarding the seeding information by inputting a seeding start point S1 (latitude, longitude), a seeding end point S2 (latitude, longitude), a seeding start time, a seeding termination time and the amount of seeding, that is, pieces of information about seeding by executing aircraft.csh shell.

In this case, first, SEED numerical experiments (glaciogenic seeding experiments) are performed with 1 km resolution and NOSEED experiments (criterion experiments or non-seeding experiments) are performed at the same time. FIG. 5 is a diagram showing a concept regarding such numerical experiments.

Thereafter, an experiment calculation unit displays and calculates a seeding material spread and distribution field using the results of the numerical simulations, displays a precipitation increment and a region, and calculates areas at steps S220 and S230.

More specifically, the experiment calculation unit displays and calculates the seeding material spread and distribution field through the results of the SEED numerical experiments (glaciogenic seeding experiments). FIG. 6 shows a distribution of a spread seeding material based on the results of the SEED numerical experiments. The spread diagram of FIG. 6 shows an area regarding whether the seeding material reaches a target point after several minutes from a seeding start time.

Furthermore, the experiment calculation unit may display a precipitation increment and a region attributable to the experiments based on a difference between the amount of precipitation in the SEED numerical experiments and the amount of precipitation in the NOSEED numerical experiments, and may calculate areas, as shown in FIG. 7. In this case, the area is calculated by reading a SEED experiment file and a NOSEED experiment file, calculating a difference (SEED and NOSEED) between the accumulated amounts of precipitation in about 3 hours after the seeding is terminated, and calculating the number of pixels whose value is 0.1 mm or more. One pixel is 1 km̂2. Accordingly, the number of pixels in which a precipitation increase has occurred indicates an area.

Thereafter, a seeding effect determination unit determines whether a seeding effect is present or not using the displayed and calculated results at step S300.

In this case, the seeding effect determination unit may determine whether a seeding effect is present or not based on whether the seeding material has reached the target area or not and a precipitation increment and a precipitation increase area attributable to the seeding using the displayed and calculated results.

For example, a criterion for determining whether a seeding effect is present or not may include whether a seeding material has reached the target area or not and a precipitation increase of 0.1 mm or more and a precipitation increase area of 100 km2 or more attributable to the seeding. In this case, the criteria, that is, the numerical values of the precipitation increase of 0.1 mm and the area of 100 km2, may be changed.

Experiments may be performed or not based on the results of the determination of whether a seeding effect is present or not.

That is, if it is determined that a seeding effect is not present, experiments are determined to be not performed at step S310. If it is determined that a seeding effect is present, experiments are determined to be performed at step S320.

As described above, in the method for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention, a seeding line, a seeing period, the amount of seeding and a seeding altitude are calculated by taking into consideration an average direction and velocity of the wind when airborne experiments are performed based on a weather center detailed forecast field. The spread of a seeding material and a distribution (i.e., a target area) of glaciogenic seeding attributable to the seeding are checked through simulations using a numerical model. Accordingly, whether to perform experiments can be determined, and a rate of success of corresponding airborne glaciogenic seeding experiments can be improved.

FIG. 8 is a diagram showing the configuration of a system for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention.

Hereinafter, the configuration of the system for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention is described with reference to FIG. 8.

As shown in FIG. 8, the system 210 for determining whether to perform airborne glaciogenic seeding experiments through numerical simulations in accordance with an embodiment of the present invention is configured to include the weather factor analysis unit 211, the airborne experiment possibility determination unit 212, the seeding information determination unit 213, the numerical simulation execution unit 214, the experiment calculation unit 215, and the seeding effect determination unit 216.

The weather factor analysis unit 211 analyzes the weather factors of a target area on which airborne glaciogenic seeding experiments are to be performed.

In this case, the weather factor analysis unit 211 may analyze the velocity of the wind, the direction of the wind, temperature and humidity, that is, the weather factors of a target area on which airborne glaciogenic seeding experiments are to be performed, using the vertical time-series diagram of weather center forecast data.

The airborne experiment possibility determination unit 212 determines whether airborne experiments are possible based on the direction of the wind, the velocity of the wind, temperature and humidity of the target area.

The seeding information determination unit 213 determines seeding information by taking into consideration the direction of the wind and the velocity of the wind.

In this case, the seeding information determination unit 213 may determine the seeding information, including a seeding line, a seeding altitude, a seeding start time, a seeding termination time and the amount of seeding by taking into consideration the direction of the wind and the velocity of the wind.

Furthermore, the numerical simulation execution unit 214 performs numerical simulations using the seeding information.

More specifically, the numerical simulation execution unit 214 may generate information about a point, time and an altitude regarding the domain of the seeding information using the seeding information, and may perform glaciogenic seeding experiments (SEED numerical experiments) and criterion experiments or NOSEED experiments numerical simulations.

The experiment calculation unit 215 displays and calculates a seeding material spread and distribution field using the results of the numerical simulations, displays a precipitation increment and a region, and calculates an area.

Accordingly, the seeding effect determination unit 216 may determine whether a seeding effect is present or not using the displayed and calculated results.

In this case, the seeding effect determination unit 216 may be configured to determine whether a seeding effect is present or not based on whether the seeding material has reached the target area or not and a precipitation increment and a precipitation increase attributable to the seeding using the displayed and calculated results.

In accordance with an embodiment of the present invention a seeding line, a seeing period, the amount of seeding and a seeding altitude are calculated by taking into consideration an average direction and velocity of the wind when airborne experiments are performed based on a weather center detailed forecast field. The spread of a seeding material and a distribution (i.e., a target area) of glaciogenic seeding attributable to the seeding are checked through simulations using a numerical model. Accordingly, whether to perform experiments can be determined, and a rate of success of corresponding airborne glaciogenic seeding experiments can be improved.

As described above, the detailed embodiments of the present invention have been described in the detailed description. However, the present invention may be modified in various ways without departing from the category of the invention. Accordingly, the technical spirit of the present invention should not be limited to the aforementioned embodiments, but should be defined by not only the appended claims, but equivalents thereof.

