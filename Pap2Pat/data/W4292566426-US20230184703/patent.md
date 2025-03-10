# DESCRIPTION

## TECHNICAL FIELD

The present disclosure relates to the technical field of characterization of micron-level second phase in aluminum alloy, and more specifically, to a quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning.

## BACKGROUND

The unmelted or refractory second phase particles in aluminum alloy are usually produced during casting, which cannot be remelted during subsequent heat treatment and hot deformation. These refractory second phases will be broken and elongated during deformation. They are arranged in a straight line along the deformation direction and consist of short complementary and connected strips. These particles are hard and brittle, distributed in the grain or grain boundary, and easy to form pores and microcracks on the phase interface during plastic deformation, which can significantly reduce the fracture toughness of the material. In addition, due to the difference of micro area electrochemistry between the second phase and the substrate, localized corrosion such as pitting corrosion, intergranular corrosion and stress corrosion are prone to occur. This not only reduces the reliability of high strength aluminum alloy and its components, but also significantly shortens the service life of the material.

At present, there is no unified standard for the quantitative characterization of micron-level second phase in aluminum alloys. Most of the existing methods use manual software tags, and the amount of data is usually dozens to hundreds of images. From a statistical point of view, the material is non-uniform, and the local field of view of tens to hundreds of sheets can not represent the real situation of tissue distribution. In addition, the software sheet processing can achieve high accuracy, but it needs a long time of manual participation, so it is not suitable for processing large quantities of data. Software batch processing can process a large number of images quickly, but due to the problem of generalization ability, it can not achieve high precision at the same time. Finally, at present, the quantitative characterization parameters of the second phase in aluminum alloys are relatively single, which are only common parameters such as area fraction and number, and lack of precise quantitative characterization of spatial and location distribution information.

With the development of science and technology, deep learning has strong adaptive, self-learning and parallel processing ability, which is more and more used in the field of image segmentation. High throughput scanning electron microscope has the characteristics of high efficiency and high speed. It can obtain large-scale full field scanning images in a short time, which provides an effective way to obtain data sets and solves the problem of data set source. The combination of high throughput image data acquisition method and artificial intelligence method is the application trend of material characterization. Therefore, it is significant to strengthen the application of high throughput scanning electron microscope and deep learning algorithm in the quantitative characterization of micron-level second phase in aluminum alloy, and it is also an important research topic.

## SUMMARY

The disclosure provides a quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning. High throughput image data acquisition method and deep learning algorithm are used to realize the automatic identification of micron-level second phase in aluminum alloy. Combined with mathematical methods, a variety of characterization parameters of second phase are mined, and the distribution differences between the whole field of view and zones on the surface of materials are quantitatively counted. The problem of traditional single quantitative characterization parameters of second phase in aluminum alloy is solved. The provided method has the characteristics of large field of view, complete information, accuracy and reliability.

Technical solutions of the present disclosure are specifically described as follows.

A quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning is provided, including:

a) selecting a standard aluminum alloy sample and polishing a sample surface to obtain a micron-level second phase image of the sample surface;

b) carrying out an image segmentation based on the micron-level second phase image, screening out a feature data set, and generating a feature database;

c) training the feature database by using an image segmentation network U-Net based on deep learning, and obtaining a U-NET segmentation model;

d) inputting the original image in the untrained feature database into the obtained U-Net segmentation model; taking a binary image screened manually in the feature database as a standard, comparing and verifying an accuracy value of binary images predicted by the U-Net segmentation model; taking an intersection-union ratio IOU as an evaluation index, and evaluating an segmentation accuracy of the segmentation model; selecting parameters corresponding to an optimal accuracy and establishing an U-Net target model;

e) continuously and automatically acquiring microstructures of the polished aluminum alloy surface to be tested by using a high throughput scanning electron microscope, and obtaining aluminum alloy images to be detected;

f) clipping the single aluminum alloy image acquired in step e), inputting the clipped serial test images into the U-Net target model established in step d), segmenting and extracting second phase in the aluminum alloy to be tested, and obtaining binary images;

g) processing the binary images obtained in step f) by a connected region algorithm to obtain a complete data set, wherein the data set comprises size, area and position information of each second phase;

h) carrying out a statistical distribution characterization on the data set according to mathematical statistical method, and restoring the position information in the image to be detected to the aluminum alloy surface to be tested, and obtaining a full-field quantitative statistical distribution and visualization result.

Further, in step a), the step of selecting a standard aluminum alloy sample and polishing a sample surface to obtain micron-level second phase images of the sample surface specifically includes:

grinding and polishing the standard aluminum alloy sample surface, wherein mechanical polishing is adopted, and SiO2 grinding paste is used as a polishing agent;

using a high throughput automatic scanning electron microscope of Navigator-OPA, acquiring a microstructural image of the polished standard aluminum alloy sample surface and obtaining the micron-level second phase image.

Further, in step b), the step of carrying out an image segmentation based on the micron-level second phase images, screening out a feature data set, and generating a feature database specifically comprises:

segmenting a single image by MIPAR image processing software, and establishing an accurate segmentation template; wherein the segmenting process comprises four steps of median filtering, threshold segmentation, morphology processing and interference screening;

importing the segmentation template into a batch processing area, performing a batch segmentation on the micron-level second phase image in the data set, then performing single manual screening, and generating the feature database from the screened feature data set.

Further, in step c), the left side of the image segmentation network U-Net is a lower sampling layer alternately combined by a convolution layer and a pooling layer, and an activation function adopts ReLu to shrink the path of the input image to capture global content; the right side of the image segmentation network U-Net is a upper sampling layer alternately combined by a convolution layer and a deconvolution layer, and the path of the feature image of the lower sampling layer is expanded in training process to accurately locate each pixel of the image.

Further, in step e), the aluminum alloy to be tested is treated by the same polishing and image acquisition methods as the standard aluminum alloy sample.

Further, in step e), the microstructures of the polished aluminum alloy surface to be tested are continuously and automatically acquired by using a high throughput scanning electron microscope, and an overlap area of any two consecutive images is set to 0-10%.

Further, in step h), when the second phase is characterized by a mathematical statistical method, a nearest neighbor Euclidean distance parameter is introduced to represent a minimum distance of two adjacent insoluble phases in the space.

Further, in step h), when the second phase is characterized by a mathematical statistical method, a length-width ratio parameter is introduced, and the length is Ferret diameter, and the width is the ratio of the pixel area to the Ferret diameter.

Further, in step e), the microstructures of the polished aluminum alloy surface to be tested are continuously and automatically acquired by using a high throughput scanning electron microscope, and the acquired image is 4096*4096 pixels, and there is no overlapping area between adjacent images.

According to the specific embodiments provided in the present disclosure, following beneficial effects are disclosed.

Firstly, the current methods mainly rely on artificial visual observation or the combination of artificial and image processing software to complete the evaluation and quantitative statistics. The software can achieve high accuracy for single image processing, but the efficiency is very low. The software batch processing can achieve fast statistics, but due to the poor generalization ability, the segmentation accuracy is not enough. Based on high throughput scanning electron microscope, combined with deep learning image segmentation and extraction algorithm and mathematical statistics algorithm, the segmentation model can automatically and quickly realize the segmentation and extraction of micron-level second phase in aluminum alloy, and improve the image processing efficiency.

Secondly, the current second phase statistics is the image analysis of a single field of view, the number of observation field area and microstructure is limited. The disclosure obtains a large-scale continuous feature map with an area of more than 100 square mm through large-scale full field automatic acquisition. Because of the statistical analysis of the full field of view image, the statistical error of single field of view is greatly eliminated. Therefore, the disclosure has the advantages of large field of view and complete information, and the statistical data is more accurate and reliable.

Thirdly, the current deep learning method needs complex manual marks when making labels. In the method disclosed, a single image is processed by MIPAR software to obtain an accurate segmentation template. On the basis of the template, the image is processed in batches, and then the label is made by manual single screening. the method avoids complex manual marking and saves labor time.

Fourthly, the current characterization parameters of the second phase are relatively single. In the method disclosed, through the segmentation and extraction of large-scale image features, many fine characterization results can be achieved, such as the statistics of location and spatial information, the quantitative distribution statistics of global and local regions and so on.

## DETAILED DESCRIPTION OF EMBODIMENTS

Certain exemplary embodiments will now be described to provide an overall understanding of the principles of the structure, function, manufacture, and use of the instruments and methods disclosed herein. One or more examples of these embodiments are illustrated in the accompanying drawings. Those skilled in the art will understand that the instruments and methods specifically described herein and illustrated in the accompanying drawings are non-limiting exemplary embodiments and that the scope of the present disclosure is defined solely by the claims. The features illustrated or described in connection with one exemplary embodiment may be combined with the features of other embodiments. Such modifications and variations are intended to be included within the scope of the present disclosure.

The disclosure provides a quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning. High throughput image data acquisition method and deep learning algorithm are used to realize the automatic identification of micron-level second phase in aluminum alloy. Combined with mathematical methods, a variety of characterization parameters of second phase are mined, and the distribution differences between the whole field of view and zones on the surface of materials are quantitatively counted. The problem of traditional single quantitative characterization parameters of second phase in aluminum alloy is solved. The provided method has the characteristics of large field of view, complete information, accuracy and reliability. The method avoids the subjective error caused by manual selection of field of view, and solves the problem of low efficiency in manual measurement and statistics. The method avoids manual marking of data sets, and saves manual time. The method realizes automatic, accurate, comprehensive and rapid characterization of micron-level second phase in aluminum alloy.

In order to make the above objects, features and advantages of the disclosure more obvious and easier to understand, the disclosure will be further described in detail in combination with the drawings and the specific embodiments.

As shown in FIG. 1, a quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning is provided, including:

a) selecting a standard aluminum alloy sample and polishing a sample surface to obtain a micron-level second phase image of the sample surface;

b) carrying out an image segmentation based on the micron-level second phase image, screening out a feature data set, and generating a feature database;

c) training the feature database by using an image segmentation network U-Net based on deep learning, and obtaining a U-NET segmentation model;

d) inputting the original image in the untrained feature database into the obtained U-Net segmentation model; taking a binary image screened manually in the feature database as a standard, comparing and verifying an accuracy value of binary images predicted by the U-Net segmentation model; taking an intersection-union ratio IOU as an evaluation index, and evaluating an segmentation accuracy of the segmentation model; selecting parameters corresponding to an optimal accuracy and establishing an U-Net target model;

e) continuously and automatically acquiring microstructures of the polished aluminum alloy surface to be tested by using a high throughput scanning electron microscope, and obtaining aluminum alloy images to be detected;

f) clipping the single aluminum alloy image acquired in step e), inputting the clipped serial test images into the U-Net target model established in step d), segmenting and extracting second phase in the aluminum alloy to be tested, and obtaining binary images;

g) processing the binary images obtained in step f) by a connected region algorithm to obtain a complete data set, wherein the data set comprises size, area and position information of each second phase;

h) carrying out a statistical distribution characterization on the data set according to mathematical statistical method, and restoring the position information in the image to be detected to the aluminum alloy surface to be tested, and obtaining a full-field quantitative statistical distribution and visualization result.

In step a), the step of selecting a standard aluminum alloy sample and polishing a sample surface to obtain micron-level second phase images of the sample surface specifically includes:


- - grinding and polishing the standard aluminum alloy sample surface,
    wherein mechanical polishing is adopted, and SiO₂ grinding paste is
    used as a polishing agent;
  - using a high throughput automatic scanning electron microscope of
    Navigator-OPA, acquiring a microstructural image of the polished
    standard aluminum alloy sample surface and obtaining the
    micron-level second phase image.

In step b), the step of carrying out an image segmentation based on the micron-level second phase images, screening out a feature data set, and generating a feature database specifically comprises:


- - segmenting a single image by MIPAR image processing software, and
    establishing an accurate segmentation template; wherein the
    segmenting process comprises four steps of median filtering,
    threshold segmentation, morphology processing and interference
    screening;
  - importing the segmentation template into a batch processing area,
    performing a batch segmentation on the micron-level second phase
    image in the data set, then performing single manual screening, and
    generating the feature database from the screened feature data set.

Where, it takes about 60 s for PIPAR image processing software to segment a single image, and 0.4016 s for batch processing each image.

In step c), the left side of the image segmentation network U-Net is a lower sampling layer alternately combined by a convolution layer and a pooling layer, and an activation function adopts ReLu to shrink the path of the input image to capture global content; the right side of the image segmentation network U-Net is a upper sampling layer alternately combined by a convolution layer and a deconvolution layer, and the path of the feature image of the lower sampling layer is expanded in training process to accurately locate each pixel of the image.

In step d), the U-Net network predicts that the highest IOU of the second phase is 86.22%.

In step e), the aluminum alloy to be tested is treated by the same polishing and image acquisition methods as the standard aluminum alloy sample; the microstructures of the polished aluminum alloy surface to be tested are continuously and automatically acquired by using a high throughput scanning electron microscope, and an overlap area of any two consecutive images is set to 0-10%, and the acquired image is 4096*4096 pixels, and there is no overlapping area between adjacent images.

In the step f), the aluminum alloy test image is formed by clipping a single image into four 2048*2048 pixel sequence backscatter images according to the position; the segmentation time of the single test image is 0.4031 s.

In the step g), the acquisition area is more than 100 mm2, and the number of second phases is close to 400000.

In step h), when the second phase is characterized by a mathematical statistical method, a nearest neighbor Euclidean distance parameter and a length-width ratio parameter are introduced, where the nearest neighbor Euclidean distance parameter represents a minimum distance of two adjacent insoluble phases in the space, and the length is Ferret diameter, and the width is the ratio of the pixel area to the Ferret diameter.

In the specific embodiment, four different specifications of aluminum alloy for corbels are selected, and the composition is shown in Table 1. At present, the corbel materials of high-speed railway in China still rely on imports. Compared with imported materials, the weathering steel produced in China has low overall stability and poor durability. The fundamental reason is that the control accuracy of composition and microstructure of the materials produced in China is low and fluctuates greatly. Therefore, it is of great significance to evaluate the microstructure uniformity of aluminum alloy for corbels by high throughput characterization for the study of the stability and durability of materials for corbels.

Firstly, the micron-level second phase images of the four aluminum alloy materials obtained in step a) were shown in FIG. 2 (a)-(d), and the pixel size was 4096*4096. The standard image obtained in step a) was segmented by MIPAR image processing software, and the segmentation template was established, and the process of the segmentation template was median filtering, threshold segmentation, morphological processing and interference screening. The time of single image segmentation was about 60 s. In step b), 3200 batch images of 2048*2048 pixels were imported in the MIPAR image processing software and subjected to segmentation processing by the segmentation template. A single image took 0.4016 s. The segmented single image was manually screened, and the segmentation effect was optimized by fine tuning the parameters, and the feature database was established.

U-Net image segmentation network was established, and the network framework is shown in FIGS. 3. 800, 1600 and 2400 images with 2048*2048 pixels were used as training data respectively. After training, the parameters were saved and the target segmentation model is established. The original image in the untrained feature database was input into the established segmentation model, and the accuracy of the binary image predicted by U-Net network was compared and verified with the manually screened binary image in the feature database as the standard. The comparison of test accuracy of three different training sets is shown in Table 2.

The cross-section dimensions of the four kinds of aluminum alloy plates to be tested in the vertical rolling direction are 50 mm2, 120 mm2, 70 mm2 and 110 mm2 respectively. In the same way as step a), high throughput scanning electron microscope of Navigator-OPA was used to automatically acquired the full field microstructural characteristics of the polished samples. 3362, 11508, 7056 and 10668 original backscatter images with 4096*4096 pixels were obtained.

The images to be detected obtained in step e) were cropped into a small field of view image of 2048*2048 pixels. The clipped images to be tested were input into the U-Net image segmentation model based on deep learning established in step c) for testing.

The connected region algorithm was used to make statistics on the binary image obtained in step e) to obtain a complete data set, including the position, area, size and other information of the second phase in a large scale and full field of view. The statistical results are shown in Table 3. The surface area of the sample was divided into the upper surface area, the middle area and the lower surface area, which were represented by 1/3, 2/3 and 3/3 respectively. The statistical results between the zones are shown in Table 4, showing the quantity, area proportion and average area of the second phase respectively.

As shown in FIGS. 5 (a)-(d), it is the area distribution visualization image of the second phase in the range of 50 mm2, 120 mm2, 70 mm2 and 110 mm2 obtained by taking the area of 236 μm2 and 655 μM2 as statistical units for four kinds of aluminum alloy materials. FIGS. 6 (a)-(d) show the quantity distribution visualization images of the second phase in four kinds of aluminum alloy materials. It can be seen that the area distribution of the middle area was larger and the number was less, while the surface area was larger and the area distribution was smaller; the distribution direction was consistent with the rolling direction, and the larger the thickness was, the more obvious the trend was; in addition, the enrichment and loss phenomenon appeared in some areas.

In addition, the second phase spacing is closely related to crack resistance, fracture toughness and pitting corrosion. The location information of each image was restored to the cross section of the sample by mathematical statistical method, and the minimum Euclidean distance of adjacent features was calculated by partition to characterize the spatial distribution of the second phase. FIGS. 7 (a)-(d) show the frequency distribution of the minimum spacing of the four materials respectively. It can be seen from that the frequency distribution of the four materials was consistent, and there were two peaks, respectively in the 0-1 and 1-2 micron ranges, indicating that most insoluble phases were aggregated.

The shape of the micron-level second phase is characterized by the length-width ratio parameter, where the length is the Ferret diameter and the width is the ratio of the pixel area to the Ferret diameter. FIGS. 8 (a)-(d) show the frequency histogram of length-width ratio distribution of the four materials. It can be seen that the frequency histogram of the length-width ratio distribution of the four materials was consistent, and the peak distribution was in the range of 1.5-2.

In the step e) of the disclosure, the polished aluminum alloy surface was acquired by the high throughput scanning electron microscope, and the sequential images were continuously acquired in a short time. The overall acquisition speed was 10 times faster than that of the ordinary electron microscope, and the large-scale image information was obtained to realize the high throughput acquisition of image data. MIPAR batch processing and manual fine-tuning were combined in the process of deep learning dataset production, which greatly saves labor time. The images to be tested were input into the trained image segmentation model, and the output time was 0.4031 s and the accuracy was 86.22%. In step g), the complete global data including the size, number, area and position of the second phase in the cross section was obtained. In step h), the region with appropriate size was selected as the statistical unit to obtain the statistical distribution information of large-scale cross section and between regions, and the global data was visualized; in addition, the nearest neighbor Euclidean distance and length-width ratio were realized to characterize the spatial distribution and shape information of the second phase on the sample surface. In conclusion, the method was used for automatic identification, segmentation and quantitative statistical characterization of micron-level second phase in aluminum alloy in large scale.

The quantitative statistical characterization method of micron-level second phase in aluminum alloy based on deep learning provided in the disclosure is based on deep learning, and the second phase images are quickly acquired based on high throughput scanning electron microscope to obtain continuously distributed image data. Based on deep learning semantic segmentation algorithm, the second phase target in continuous images is subjected to automatic recognition and segmentation. Finally, the area, size, number, distribution density, shape factor and other information of the extracted second phase are mined by mathematical method, and the distribution difference between the whole field of view and the partition of the material surface is calculated quantitatively. The disclosure is able to automatically and quickly realize the full field of view positioning and extraction of the second phase, finely characterize the size, area, position, length-width ratio and distribution information of the second phase, and solve the problems of small field of view, low efficiency, low precision and single statistical information caused by manual identification, measurement and statistics of microstructure.

The above description of the disclosed embodiments enables those skilled in the art to achieve or use the disclosure. Multiple modifications to these embodiments will be apparent to those skilled in the art, and the general principles defined herein may be achieved in other embodiments without departing from the spirit or scope of the disclosure. The present disclosure will therefore not be restricted to these embodiments shown herein, but rather to comply with the broadest scope consistent with the principles and novel features disclosed herein.

