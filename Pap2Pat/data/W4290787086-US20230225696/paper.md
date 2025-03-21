# INTRODUCTION

Doppler echocardiography (echo) of the tricuspid regurgitation (TR) jet plays a central role in the noninvasive assessment of pulmonary hypertension (PH). 1 In 1984, Yock and Popp 2 showed Doppler derived estimation of right ventricular systolic pressure (RVSP) was strongly associated with invasive measurements with only a minimal bias. While its value is well recognized, more recent studies have questioned the reliability of noninvasive Doppler estimation of RVSP via peak regurgitant velocity (Vmax) 3 . For example, Fisher et al. 4 found 48% of cases had an assessment error of greater than 10 mmHg. As shown by other studies, however, reliability may be significantly improved by estimation of Vmax at the modal frequency and by avoiding interpretation of incomplete TR waveforms. 5,6 A better understanding of the Doppler TR waveform could provide additional quality control for estimation of Vmax and therefore RVSP.

While the shape of the TR waveform has generally been described as parabolic or triangular, 7 few studies have mathematically analyzed the underlying TR curvature. In right heart catheterization (RHC) measurements, Vanderpool et al. 8 recently highlighted how first and second derivatives of the RVSP waveform can be useful in identifying isovolumic contraction, ejection, and isovolumic relaxation.

The third-degree polynomial method (cubic spline) allows interpolation of skewed curves and is commonly used in the engineering field to achieve smooth boundaries. To add confidence in maximal pressure (Pmax) estimation, we coupled the method with physiologically relevant points of the TR waveform such as start and end of isovolumic phases or of ejection phase.

This study had three main objectives to define the conceptual framework of TR waveform analysis. First, we analyzed the TR waveform and its relationship with physiological metrics including but not limited to right ventricular (RV) longitudinal strain, TR severity, pulmonary vascular resistance (PVR), and heart rate. Second, we derived and validated the cubic polynomial interpolation method of estimating RVSP from different phases of the cardiac cycle. Finally, we determined whether cubic polynomial interpolation could improve estimation of RVSP in a cohort with greater bias between RVSP estimation from echo and RHC.

# METHODS

We first developed a script for extraction of TR tracings with automated analysis of normalized TR duration, skewness, kurtosis, and maximal and minimal first pressure time derivatives (dp/dt max and min). Subsequently, RV pressure curves were constructed using the Bernoulli equation by adding echoc-estimated right atrial pressure (RAP). We then derived a cubic polynomial interpolation model to guide estimation of Pmax, and RVSP.

## Clinical cohorts

Four cohorts were analyzed as part of this study: (1) a derivation cohort to evaluate cubic polynomial interpolation method, (2) a validation cohort, (3) a cohort to test the clinical applicability of the interpolation methods, (4) and a non-pulmonary arterial hypertension (PAH) cohort with and without PH (Figure 1a). The derivation cohort included 44 patients recruited between January 2007 and June 2009 with a diagnosis of PAH and in whom echo and RHC was obtained within 12 h of each other in stable clinical condition. The validation cohort (n = 71) patients were enrolled between December 2006 and December 2013, from the previously published prospective Vera Moulton Wall Center registry. 9 A third "outlier" cohort of 22 patients with advanced lung disease (ALD) and found to have a difference of greater than 30% between echocardiographic and invasive estimates. We also added a non-PAH group (n = 44) referred to RHC to assess performance of our method in another nosological context. The diagnosis of PAH was defined by the presence of mean pulmonary arterial pressure (MPAP) >20 mmHg, 10 pulmonary arterial wedge pressure ≤15 mmHg, and WHO Group 1 diagnosis. All patients were in sinus rhythm at the time of echo, presence of right bundle branch block and QRS duration were recorded. Stanford University Institutional Review Board approved the study, which was conducted in agreement with the Helsinki-II declaration.

## Echocardiography

Studies were acquired using Philips IE 33 ultrasound systems (Philips). All measurements were performed according to the latest guidelines by certified level 3 expert readers [C. V., M. A., F. H.]. 11,12 The reader only selected complete TR signals, for which the curve was interpretable for the entire cardiac cycle. Measures of RV size and function included relative RV area (right to left area ratio), RV fractional area change and RV longitudinal strain. RV free wall Lagrangian longitudinal strain (RVLS) was measured from mid-endocardial enddiastolic and end-systolic manually traced lengths and calculated as: (end-systolic lengthend-diastolic length). RAP was estimated from the inferior vena cava size and collapse according to American Society of Echocardiography guidelines. 13 

## Right Heart Catheterization

RHC was performed through the internal jugular or right femoral veins. Mixed venous saturation, RAP, systolic pulmonary artery pressure (SPAP), MPAP diastolic pulmonary arterial pressure, and pulmonary capillary wedge pressure, were measured, and PVR, and cardiac index (using the assumed Fick method) subsequently calculated. 14 

## Digitization of TR signals using a novel semiautomated analysis

The outline of the TR Doppler waveform was first manually segmented then automatically extracted with the ECG and normalized to the RR interval (Figure 1b). The TR waveform was filtered using a 2nd-order Butterworth lowpass filter using a 10 Hz cut-off. Digitization of the TR signals was reliable as assessed by the coefficient of determination for RVSP (R 2 = 0.991) and velocity time integrals (VTIs) (R 2 = 0.929) (Figure 1c,d). The analysis of the velocity profiles included the Vmax and the VTI, skewness, and kurtosis. Skewness was defined as time to Pmax normalized by the duration of TR signal. RV pressure curves were constructed using the Bernoulli equation by adding estimated RAP. The first pressure derivatives were derived to calculate dP/dt max and min.

The second derivative was used to identify the beginning and end of the ejection phase as previously described by Vanderpool et al. 8 

## Cubic polynomial interpolation

Polynomial interpolation is based on a polynomial of variable-degree p(t), where t is the time normalized over the RR interval. A second-degree polynomial interpolation would be synonymous with a parabolic fit of the TR signal, assumed in the guidelines. 15 In contrast, we use a cubic polynomial approach, which additionally captures the skewness of the TR waveform (see Supporting Information). The four parameters were calculated for each individual TR waveform based on the boundary points of specific physiological phases and their respective local first derivatives, enforcing a smooth interpolated curve. Therefore, each patient's curve interpolation was based on the TR curve only, not on an averaged interpolation from the entire cohort. The relevant parameters to define the physiological phases were found using the derivation cohort and are defined in the results section of the manuscript.

## Statistical analyses

Continuous data are presented in terms of median and interquartile ranges and were compared between cohorts using the Mann-Whitney test, while categorical data were presented as number and percentage and compared using χ 2 test between cohorts. We used Spearman correlation analysis to analyze association between variables and multivariable linear regression analysis to identify independent correlates. We also used Bland-Altman analysis to describe bias and limits of agreement between cubic polynomial interpolation and expert read echocardiographic studies and between echo and RHC measures. A paired t-test was used to analyze changes between clinical reports and cubic polynomial interpolation based on early phases of the TR signal. Results were considered significant when two-sided p values were <0.05. Analysis was performed using custom scripts in python (Python 3.0) with libraries PIL, scipy, and cv2 and using Medcalc statistical software (Version V19.8).

# RESULTS

## Patient sample population

The characteristics of the derivation and validation cohort are presented in 

## TR waveform analysis using digital extraction

In the derivation cohort, the TR waveforms obtained were representative with excellent correlation between expert read echo and RHC (r = 0.90, p < 0.001) and small negative bias -8.3 mmHg [-4.9; -11.6] (Figure 2a). After digital extraction, normalized TR duration, skewness and kurtosis were analyzed Table 2, Figure 2b). As shown in Figure 2c, the TR waveforms were non-parabolic with varying skewness. Normalized TR duration and corresponding (Bernoulli converted) peak pressure are the most closely related to RV and pulmonary vascular characteristics. Normalized TR duration was moderately associated with RVLS, PVR, and heart rate; skewness was more strongly associated with RAP and heart rate, whereas Pmax was related to relative RV relative size, RVLS, RAP, PVR, and heart rate (Figure 2c) (all p < 0.001). Kurtosis on the other hand was only related to heart rate (p < 0.001) (Figure 2c). On multivariable analysis, Pmax was associated with RV size (p = 0.0032) and PVR (p = 0.0007), overall p < 0.0001 and R 2 = 0.64; while skewness was mainly related to TR normalized duration (p = 0.0002, R 2 = 0.60).

## Interpolation of RVSP based on physiologically relevant phases

We constructed RVSP pressure curves based on the TR waveforms by adding estimated RAP. In our cohort, the estimated RAP was 10.1 mmHg [9.0; 11.1] based on echo and 9.9 [8.7; 11.0] mmHg on RHC, with no significant difference (p = 0.78), correlation R 2 = 0.67, bias 0.2 mmHg.

### Derivation of the cubic polynomial interpolation method

For cubic polynomial interpolation, we used three different phases-the isovolumic phase, ejection phase, and "shoulder" phase corresponding to an inflection point in the early ejection phase (Figure 3a). These phases were identified using first and second derivatives of the digitized TR waveform. For ejection phase interpolation, we identified the beginning of ejection using the first second derivative minima corresponding to a change in the curvature associated with pulmonary valve opening. "Shoulder point" interpolation was based on the early inflection point after pulmonary valve opening. The "shoulder" point was mathematically defined as the second derivative of the TR velocity waveform d 2 v/dt 2 <200 m/s 3 after the beginning of ejection. The threshold was found iteratively in the derivation cohort.

The cubic polynomial interpolation relied on the pressure at start time point t A and end time point t B defined in the physiological phases as well as the respective derivatives of the curve (Figure 3b). We calculated local derivatives as a time-average over 3% of the cardiac cycle time, which was found to be optimal in the derivation cohort. In Figure 3c, we present a typical example of cubic polynomial interpolation according to the three physiological phases. The three interpolation methods of Pmax were strongly associated with expert estimates of RVSP (all R 2 ≥ 0.931) or SPAP or MPAP by RHC (all R 2 ≥ 0.844) (Figure 4, Supporting Information: Figure 1). While interpolation using the shoulder point provided a numerically higher coefficient of determination compared to the other methods of interpolation, the differences were not statistically different (p = 0.54 for isovolumic phase, p = 0.79 for ejection phase). The limits of agreement for isovolumic, ejection, and shoulder point interpolations were 6.03 [4.33; 7.73], -2.94 [1.47; 4.41], and -3.11 [-4.52; -1.71] mmHg, respectively (Figure 4c).  The cubic polynomial interpolation method performed well in the validation cohort. The three methods had a high coefficient of determination when compared to expert reader (R 2 isovolumic = 0.910, R 2 ejection phase = 0.930, R 2 shoulder point = 0.920) (Figure 4a,b).

### Correction factors between interpolation methods

Since the isovolumic phase interpolation is prior to pulmonary valve opening and therefore change in curvature, it is expected that the pressure will be overestimated. Therefore, a correction factor needs to be incorporated and can be addressed using a fixed correction factor defined on the derivation and validation cohort with respect to the shoulder point. Using a linear regression equation, we found RVSP shoulder = 0.893 × RVSP iso (R 2 = 0.98) and similarly RVSP shoulder = 0.926 × RVSP ej (R 2 = 1.0) (Supporting Information:Figure 2).

### Effect of TR severity on interpolation method performance

In the derivation and validation cohorts, severe TR was observed in 37% of patients. Pmax was statistically higher in patients with severe TR than in those with mild or moderate degree of TR (86 ± 17 vs. 72 ± 24 mmHg, p = 0.001). TR severity was not associated with the magnitude of difference between interpolation estimated RVSP and SPAP from RHC, regardless of the interpolation method used (isovolumic interpolation, 1.9 ± 13.3 for non-severe TR vs.

-0.19 ± 15.11 for severe TR, p = 0.43; shoulder interpolation, -6.95 ± 11.9 vs. -9.75 ± 13 mmHg, p = 0.25; ejection interpolation, -1.49 vs. -2.64 ± 14 mmHg, p = 0.65).

### Comparison with alternate linear regression model based on TR waveform parameters

As an alternative to cubic polynomial interpolation, we also tested whether linear regression based on RAP, pressure derivatives, and time intervals could provide estimates of Pmax. For RVSP estimates, we included in the multivariable model normalized TR duration, dP/ dt min and max, and RAP. Overall, the R 2 of the model was 0.78 (p < 0.0001). When compared to the alternate multivariable regression model, the cubic polynomial interpolation based on the shoulder performs better (R 2 = 0.78 vs. R 2 = 0.94, p < 0.0001). In the derivation cohort, variables retained were RVSP = 0.038 × dP/dt max -0.061 × dP/dtmin + 0.96 × RAP (R 2 = 0.66, p < 0.0001). We showed correlation between pressure at the start and end of RV ejection (P eji and P eje ), with MPAP and DPAP are respectively r = 0.68 and r = 0.75 for MPAP and r = 0.69 and r = 0.65 for DPAP. We also showed R 2 of 0.83 for linear regression based on Peji and Peje to predict Pmax (p < 0.0001). The model was then defined as follows: Pmax = 9.2 + 0.81 × P eje + 0.45 × P eji.

## Testing the interpolation method in the outlier cohort

The interpolation method was tested in the clinical setting using an outlier cohort with more than 30% relative difference between clinical echocardiographic and invasive measures. In the outlier cohort, echo estimates of RVSP was 50 ± 21 mmHg, with mean RAP of 7 mmHg. The correction factor defined based on the validation and derivation cohorts was applied (uncorrected results presented in Supporting Information:Figure 2) to the outlier cohort to reduce overestimation of Pmax using interpolation from ejection and isovolumic phases.

In the outlier cohort, the echo report results in underestimated RVSP and showed high variability -11.0 [-15.4; 0.2] mmHg (Figure 5a,b). Interpolation methods showed decreased variability with -4.4 [-7.9; 0.7] mmHg for shoulder interpolation, -3.2 [-7.5; 0.9] mmHg for ejection phase, -3.1 [-8.6; 2.0] mmHg for isovolumic phase interpolation (Figure 5a). From the 22 patients in the outlier cohort, relative change in estimate from the shoulder interpolation and echo report of more than 20% was observed in 13 patients with 8 correcting an underestimation and 5 correcting an overestimation. When comparing to RHC, estimates by shoulder interpolation resulted in lower bias and smaller limits of agreement compared to the echo report (6 [1;  11] vs. 21 [12; 29] mmHg, p = 0.0149 for underestimation, -13.3 [-25.2; -1.3] vs. -26.2 [-46.42; -5.0] mmHg, p = 0.065 for overestimation) (Figure 5c,d).

## Testing the interpolation method in the non-PAH cohort with or without PH

We selected 44 patients presenting left heart disease as controls, 20 were without PH according to ESC guidelines with MPAP ≤20 mmHg based on RHC. Extrapolated Pmax from pressure at shoulder yielded a correlation of r = 0.98 with RVSP as measured by echo. Correlation was not modified according to the presence or absence of PH with r = 0.98 for patients with PH as previously defined versus r = 0.97 for patients without PH (Figure 6). When analyzing differences in TR waveform characteristics, we observed that skewness of the TR waveform was higher in patients without PH compared to the pooled patients with PH from all cohorts 0.69 versus 0.36, p < 0.0001. Kurtosis of the TR waveform was similar in both groups 2.25 versus 2.28, p = 0.91.

# DISCUSSION

In this study, we developed a novel physiological approach to TR waveform analysis and interpolation. Our study had two main findings. First, we found that the TR waveform was non-parabolic with significant variability in skewness. Second, cubic polynomial interpolation using isovolumic or early ejection phases (including shoulder) provided reliable interpolation of maximal RVSP. If further implemented, interpolation methods may provide additional quality control for RVSP estimates to inform diagnosis of PH (Figure 7).

## TR waveform shape

In clinical guidelines, the TR curve shape is often described as parabolic or triangular. 7,15 Our study, however, highlights the non-parabolic shape of the TR waveform with variable skewness. As we have shown, skewness appears to be more closely associated with normalized TR duration which itself depends on RV systolic function and PVR. Previous studies have highlighted the value of normalized TR duration in pulmonary arterial hypertension especially in pediatric population. 8,16,17 In the study of Cho et al., 18 normalized TR duration in CMR is closely related to RV ejection fraction and is proven to be associated with outcome in PAH. One of the additional original contributions of our study is to demonstrate that, in echo, normalized TR duration also depends on RV longitudinal strain which is also a strong prognostic marker in PAH.

## Interpolation method and confidence in RVSP estimation

Estimation of RVSP plays a central role in the assessment of PH. Typically, we can approach confidence of RVSP estimation either by signal quality (modal frequency and completeness of waveform) or through physiological correlates of RVSP with pulmonary pressures. For signal quality, recent studies by Kiranis et al. 19 and Amsallem et al. 5 point to the importance of estimating peak TR velocity at the modal frequency (estimation at the "chin" and not the "beard" of the signal). For physiological consideration, Chemla et al. 20 showed that DPAP and SPAP are closely related, with correlations greater than 0.90 indicating high confidence. Other authors have confirmed the relationship between DPAP and SPAP on large cohorts using allometric modeling relationship of peak and MPAP in PAH. 5,21 In the current study, we validated a novel interpolation novel interpolation method of the TR waveform. The method builds on the physiological relationships in the pulmonary circulation and integrates it with the TR waveform. It allows RVSP estimate not only based on a Pmax point but also upon a series of points of TR waveform physiologically relevant phases (isovolumic and ejection phases). As previously shown by Vanderpool et al., 8 analysis of the first and second derivatives of the RV pressure waveform can identify phases of the cardiac cycle. Here we applied first and second derivative analysis to the noninvasive TR waveform to identify early ejection phases. Theoretically, the RV pressure at the beginning of ejection will correspond to DPAP. Original to our study, we also used second derivative analysis to identify an ejection phase inflection point.

Our results demonstrated that interpolation of TR based on isovolumic or early ejection phases can provide reliable estimates of maximal RVSP. It also proved to be more reliable than multiple linear regression analysis based on the whole cohort. The observed limits of agreement can be explained physiologically. We observed overestimations when using isovolumic interpolation as it does not account for pulmonary valve opening and slight underestimation for ejection or shoulder methods as the insonation angle is rarely at a zero angle. The results in the outlier cohort demonstrated interpolation could improve clinical under or overestimation of RVSP.

In addition, we demonstrate that interpolation based on physiological points of the TR signal (classical model) can be useful. This builds on the observation of Chemla et al. 20  waveform where P eji corresponds to DPAP and P eje approximates MPAP. Although not as robust as thirddegree polynomial spline interpolation, our results provide a physiological basis for the cubic spline interpolation method.

## Implementation

As in any method, implementation is key to any quality improvement. [22][23][24] The interpolation method presented in this study could prove to be valuable especially if coupled with semiautomated or automated Doppler tracing signals. 22,24,25 While currently auto Doppler method rely on image contrast only, our study suggest that confidence can be increased by using the wealth of physiological information embedded in the TR signal.

As shown in Figure 7, several technical and physiological based methods can improve reliability of pressure estimates or estimations of likelihood of pulmonary vascular disease. A reliable method starts with excellent acquisition of TR waveforms with minimal insonation angle, estimation of maximal TR velocity at the modal frequency, ensuring concordance with estimated mean pulmonary artery pressure using early peak pulmonary regurgitation velocity and potentially further informing estimates by VTIs or cubic polynomial interpolation methods. One cannot also emphasize the importance of reliable estimates of RAP. Septal curvature, RV shape, enlargement, pulmonary enlargement, and pulmonary flow profiles can further inform the probability of PH or pulmonary vascular disease.

While interpolation of TR signals is not recommended by current guidelines, the current study offers the basis for future investigations and evaluation of whether interpolation on incomplete signals with clear isovolumic phases would lead to reliable estimates of RVSP. In the absence of these studies, this cannot be recommended, however.

## Limitations

The study has several limitations including the relatively small sample size. We did, however, include a derivation, validation, and outlier testing cohort. Second, the study mainly focused on patients with PAH and ALD and the findings cannot be extrapolated at this time to other causes of P. Our non-PAH cohort provides reason that interpolation is usefule in other nosological settings as well. In addition, although close in time, the RHC were not simultaneously performed simultaneously with echo.

# CONCLUSION

Our study shows that cubic polynomial interpolation of isovolumic or early ejection phase pressures could provide estimations of RVSP. If further validated, this could provide additional quality control for the assessment of PH in clinical practice.

## CONFLICTS OF INTEREST

Francois Haddad is currently the recipient of an investigator-initiated grant on surrogate end-point research in pulmonary arterial hypertension from Janssen Pharmaceutical and the principal investigator on a sensor grant on cardiac motion detection in pulmonary arterial hypertension funded by Precordior Inc. The remaining authors declare no conflict of interest.

## ETHICS STATEMENT

Stanford University Institutional Review Board approved the study, which was conducted in agreement with the Helsinki-II declaration.

## SUPPORTING INFORMATION

Additional supporting information can be found online in the Supporting Information section at the end of this article.

