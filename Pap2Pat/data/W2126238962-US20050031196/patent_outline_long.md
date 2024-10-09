# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- motivate face modeling
- describe prior art methods
- limitations of prior art
- introduce 3D model reconstruction
- describe viewpoint importance
- introduce optimal viewpoint problem
- describe prior art solutions
- motivate optimal viewpoint determination

## SUMMARY OF THE INVENTION

- introduce optimal viewpoint problem
- describe contour-based silhouette matching
- describe view-sphere pruning and clustering
- describe multi-view optimization search
- summarize benefits of invention

## BRIEF DESCRIPTION OF THE DRAWINGS

- describe figures

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce multi-view 3D face modeling
- describe general method for constructing 3D model
- explain differences from morphable models
- describe prior modeling method
- introduce goal of determining optimal viewpoints
- describe database of scanned faces
- explain resampling and alignment of faces
- perform principal component analysis (PCA)
- describe shape parameters and optimization
- define cost function for silhouette matching
- explain boundary-weighted XOR cost function
- describe probabilistic downhill simplex method
- introduce method for determining optimal viewpoints
- describe silhouette generation
- explain merging of resampled face with prototype head
- describe view-sphere tessellation
- discard selected viewpoint cells
- cluster viewpoints based on silhouette difference
- build lookup table for silhouette distances
- merge clusters and determine new aspect viewpoints
- show resulting aspect viewpoints and silhouettes
- discard certain viewpoints due to occlusion
- search for optimal subset of viewpoints
- describe model-based shape recovery method
- describe data-driven visual hull construction method
- measure error between recovered and original shapes
- perform exhaustive search for optimal viewpoints
- show results of model-based reconstructions
- show results of visual hull reconstructions
- discuss effect of invention on 3D face recognition systems
- discuss incorporation of additional physical and operational constraints
- discuss application to video-based face acquisition
- discuss variations and modifications of the invention
- discuss scope of the invention
- conclude description of preferred embodiments

### Effect of the Invention

- summarize effect of invention on 3D face modeling
- discuss agreement with existing practice and intuition
- conclude effect of invention

