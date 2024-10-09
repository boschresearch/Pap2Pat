# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate object detection
- limitations of current approaches

## SUMMARY

- introduce pose estimation method
- provide initial object pose
- estimate refined object pose
- define loss function
- describe iterative optimization procedure
- render 2D-3D-correspondence maps
- obtain segmentation masks
- define per-pixel loss function
- describe gradient-based method
- determine initial object pose
- apply dense pose object detector
- apply Perspective-n-Point approach

## DETAILED DESCRIPTION

- introduce pose estimation method PEM
- refine initial multi-dimensional pose Tpr(0) of object OBJ
- generate refined multi-dimensional object pose Tpr(NL) with NL≥1
- provide initial object pose Tpr(0) and 2D-3D-correspondence map Ψpri
- estimate refined object pose Tpr(NL) using iterative optimization procedure IOP
- define loss function LF(k) depending on discrepancies between Ψpri and Ψrendk,i
- render 2D-3D-correspondence map Ψrendk,i using renderer dREND
- utilize 3D model MODOBJ, assumed object pose Tpr(k), and imaging parameter PARA(i)
- obtain segmentation mask SEGrend(k, i) for each rendered 2D-3D-correspondence map Ψrendk,i
- define loss function LF(k) as per-pixel loss function
- compute loss function LF(k) using distance function ρ
- determine initial object pose Tpr(0) in step S0
- provide images IMA(i) of object OBJ with known imaging parameters PARA(i)
- process images IMA(i) in determination step DCS to determine 2D-3D-correspondence map Ψpri and segmentation mask SEGpr
- further process 2D-3D-correspondence map Ψpri in coarse pose estimation step CPES
- determine initial object pose Tpr(0) using Perspective-n-Point approach (PnP) and RANSAC
- apply differentiable renderer in inference phase
- use multiple views PER(i), POS(i), and PARA(i) as constraints
- compare provided Ψpri and rendered dense correspondences Ψrendk,i for each image IMA(i)
- transmit error back through differentiable renderer to update pose Tpr(k)
- assume availability of camera positions POS(i) or perspectives PER(i)
- obtain camera positions POS(i) or perspectives PER(i) using various methods
- use robotic arm to observe object from several viewpoints
- rely on precise relative poses between cameras provided by robotic arm
- estimate 6DoF object pose in one reference view with relative camera poses used as constraints
- provide imaging parameters PARA(i) for capturing image IMA(i)
- include camera position POS(i) and intrinsic camera parameters CAM(i) in PARA(i)
- use 3D model MODOBJ of object OBJ
- store 3D model MODOBJ in memory of control system 120
- provide 3D model MODOBJ from elsewhere when required
- apply dense pose object detector DPOD to determine 2D-3D-correspondence maps Ψpri and segmentation masks SEGpr(i)
- regress multi-class object mask and segmentation mask SEGpr(i) using DPOD
- estimate dense 2D-3D correspondence map Ψpri between image pixels and 3D model MODOBJ
- apply Perspective-n-Point approach (PnP) and RANSAC to determine initial object pose Tpr(0)
- use PnP to estimate camera pose given correspondences and intrinsic camera parameters
- use RANSAC to make camera pose prediction more robust to outliers
- include control system configured for executing pose estimation methods PEM
- refine initial multi-dimensional pose Tpr(0) of object OBJ using pose estimation system
- achieve objective of reducing discrepancy between performances of detectors trained on synthetic and real data
- introduce pose estimation method PEM
- subdivide PEM into initial pose estimation procedure PEP and pose refinement procedure PRP
- describe initial pose estimation procedure PEP
- capture images IMA(i) with parameters PARA(i)
- process images IMA(i) to determine segmentation mask SEGpr(i) and 2D-3D-correspondence map Ψpri
- apply DPOD approach to determine SEGpr(i) and Ψpri
- train DPOD for each object of interest
- describe modified DPOD approach with two substeps DCS1 and DCS2
- apply YOLO in DCS1 to detect object and output bounding box and label
- apply DPOD-like architecture in DCS2 to predict object masks and dense correspondences
- describe NOCS parameterization
- define NOCS projection operator
- apply Perspective-n-Point approach and RANSAC to determine initial object pose Tpr(0)
- utilize one or multiple 2D-3D-correspondence maps to determine Tpr(0)
- summarize initial pose estimation procedure PEP
- introduce pose refinement procedure PRP
- describe differentiable renderer dREND
- refine object pose Tpr(k) in NL iterations
- optimize loss function LF based on discrepancies between provided and rendered correspondence maps
- end iterative optimization procedure when loss function converges or falls under threshold
- render correspondence map and segmentation map for each i
- compute loss function LF(k) based on pixel-wise comparison of correspondence maps
- minimize loss function LF(k) iteratively across loops k
- apply gradient-based method to select object pose Tpr(k)
- describe advantages of approach for 6DoF pose estimation
- describe application of approach for robotic grasping
- describe use of relative camera poses as constraints
- compute camera poses in markerboard coordinate system
- estimate 6DoF object pose in one reference view
- describe use of differentiable renderer dREND in inference phase
- extend refinement procedure from single view to multiple views
- add relative camera poses as constraints to iterative optimization procedure
- overcome discrepancies between performance of detectors trained on synthetic and real data
- train DPOD detector on synthetically generated data
- refine object pose using differentiable renderer dREND
- describe advantages of approach for overcoming discrepancies
- summarize pose refinement procedure PRP
- conclude pose estimation method PEM

