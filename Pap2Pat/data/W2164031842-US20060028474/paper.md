# Rendering Deformable Surface

Reflectance Fields Tim Weyrich, Hanspeter Pfister, Senior Member, IEEE, and Markus Gross, Senior Member, IEEE

Abstract-Animation of photorealistic computer graphics models is an important goal for many applications. Image-based modeling has emerged as a promising approach to capture and visualize real-world objects. Animating image-based models, however, is still a largely unsolved problem. In this paper, we extend a popular image-based representation called surface reflectance field to animate and render deformable real-world objects under arbitrary illumination. Deforming the surface reflectance field is achieved by modifying the underlying impostor geometry. We augment the impostor by a local parameterization that allows the correct evaluation of acquired reflectance images, preserving the original light model on the deformed surface. We present a deferred shading scheme to handle the increased amount of data involved in shading the deformable surface reflectance field. We show animations of various objects that were acquired with 3D photography.

Index Terms-Computer graphics, image-based rendering.

ae

V ISUALIZATION and animation of realistic 3D computer graphics models are important for many applications, such as computer games, movies, advertisement, virtual environments, or e-commerce. Broadly speaking, there are three approaches to reproducing the visual appearance of real objects: explicit modeling with parametric representations, pure image-based approaches, and hybrid approaches that use a combination of both. In all cases, the reflectance properties of 3D objects are typically captured with methods of 3D photography.

For explicit appearance models, parametric BRDF models are fit to the acquired data. Parametric BRDFs can be efficiently rendered on modern graphics hardware and the underlying geometry can be animated and deformed using well-developed techniques such as skinning and vertex blending. However, parametric BRDFs cannot capture many effects of real-world materials, such as translucency, interreflections, self-shadowing, and subsurface scattering. Pure image-based techniques, on the other hand, are wellsuited to acquiring and representing complex object appearance. However, most of them impose restrictions on the viewpoints and the lack of a 3D geometry model makes deformations very difficult or impossible.

Consequently, hybrid approaches have become very popular. They parameterize an image-based model on an impostor geometry that can be used for animation.

This representation is commonly known as a surface light field, introduced by Miller et al. [23]. Wood et al. [31] presented a simple technique for its animation. However, surface light fields can only capture an object under fixed illumination. This is a severe limitation if the object is rendered in a new environment or under dynamically changing lights. A more general hybrid representation is the surface reflectance field, which captures the object appearance for many possible light configurations. Objects with arbitrary reflectance properties can be rendered from any viewpoint under new illumination. To date, however, there has been no publication on the animation of surface reflectance fields.

In general, animating an image-based or hybrid appearance representation requires a scheme to evaluate the image-based data set to simulate varying object deformations. A key question is how to preserve the visual appearance of the deformed object surface, that is, how to preserve the perceptual impression of material properties under different lighting conditions.

In this paper, we present a method for animating surface reflectance fields with arbitrary geometric deformations. We develop a shading scheme that aims to preserve the appearance of object materials during deformation. Our method uses a local parmeterization of the impostor geometry that enables arbitrary warps. Our shading method uses this local parameterization to approximately preserve the spatially varying BRDFs of the undeformed object. We present a cache-optimized shading strategy to minimize computation time. Our technique is applicable to other hybrid representations that contain an impostor geometry.

# PREVIOUS WORK

Three-dimensional (3D) photography loosely describes methods that capture object shape and appearance from images. Some 3D photography approaches fit a parametric BRDF model to the acquired appearance data [28], [32], [14], [13], [22], [16]. However, parametric BRDFs cannot represent many of the reflectance properties of real-life objects [11]. In contrast, image-based appearance representations (with geometry) make no assumptions about the reflection property of materials.

The lumigraph [10] is the first method to combine an impostor geometry (a visual hull of the object) with an image-based representation. Images of the object are stored as a dense light field [17] and the impostor geometry is used to improve light field interpolation, i.e., to minimize blooming and ghosting. To reduce the amount of image data, view-dependent texture mapping [27], [8], [7] uses simple geometry and sparse texture data. This method is extremely effective despite the approximate 3D shape, but it has some limitations for highly specular surfaces due to the relatively small number of textures.

Surface light fields [23], [31], [3] are a more general and efficient representation because they parameterize the image data onto the object surface. Surface light fields can either be stored on accurate high-density geometry [31] or on coarse triangular meshes for objects with low geometric complexity [24]. Some techniques [25], [3] agressively compress the data such that the models can be rendered in real-time on modern graphics hardware. To improve the appearance of complex object silhouettes, surface light fields can be combined with view-dependent opacity data into opacity light fields [29]. Unstructured lumigraph rendering [2] is a very effective method for rendering both surface and opacity light fields.

Although surface light fields are capable of reproducing important global effects such as interreflections and selfshadowing, they only show the object under fixed lighting. To overcome this limitation, recent approaches have used surface reflectance fields. The reflectance field of an object is the radiant light from a surface under every possible incident field of illumination. In practice, the reflectance field is sampled sparsely and interpolated during rendering. To further reduce the amount of data, most reflectance fields are acquired for a single view [5], [11], [15]. For approximately planar geometry and diffuse surfaces, the data can be compressed further by fitting a parametric function to the reflectance field [18].

In our work, we use the surface reflectance field data acquired by the 3D photography system of Matusik et al. [20]. The system acquires reflectance fields for over 400 views using cameras, turntables, and a rotating array of lights. The acquired data also includes view-dependent opacity information, called the opacity reflectance field (not considered in this paper). The impostor geometry is the visual hull of the objects.

Although it is an important aspect for many practical applications, the animation of image-based data has received very little attention in the literature. Wood et al. [31] describe arbitrary deformations on a surface light field and produce plausible renderings of the deformed model. However, their method does not deal properly with the diffuse component of the surface color and it only works for purely reflective isotropic BRDFs. Feature-based light field morphing [33] morphs two light fields into each other, based on the concept of ray-correspondencies. The method requires substantial user input to specify corresponding feature polygons between the two objects and it is not applicable to the general animation setting. Both methods work only for static illumination. Furukawa et al. [9] presented a scanning system to capture objects and spatially varying BRDFs, also called Bidirectional Texture Functions (BTFs) [4]. They use tensor product expansion to compress the BTF data and show results with surface deformations.

Their system is the first to render deformations of a relightable, image-based object representation. However, they rely on a tight impostor geometry to support the BTF representation. Thus, the object geometry has to be acquired with a range scanning device. Moreover, their paper does not explicitely address appearance preservation under nonuniform, skewed deformations.

In this paper, we describe an animation method for surface reflectance fields mapped onto approximate geometry. Our method allows us to place the objects in new environments with arbitrary illumination, including dynamically changing lights. We carefully analyze the conditions that have to be met to preserve the appearance of the object (Section 4.1) and we present a novel method to approximately preserve spatially varying BRDFs during deformations (Section 4.2). We discuss the limitations of our approach (Section 4.4) and show results using objects that are difficult to handle for image-based approaches, including objects with specularities, transparency, and selfshadowing (Section 6).

# OVERVIEW

A surface reflectance field consists of a large set of imagebased reflectance data of an object, in conjunction with an impostor geometry used for rendering. The reflectance data is given by a collection of reflectance images. A reflectance image is a stack of camera images showing the object from the same viewpoint under varying directional illumination (Fig. 1). A surface reflectance field consists of reflectance images from many viewpoints around the object. For our objects, we use approximately 400 reflectance images, each with 60 high dynamic range images of the object under different directional illumination.

Rendering a surface reflectance field can be understood as a two step procedure. First, the reflectance images are used to compute an image of the object under the new illumination for each viewpoint (Fig. 2). These images are then rendered together using the impostor geometry with unstructured lumigraph interpolation [2]. Our impostor geometry is the visual hull of the object that can easily be determined from observed silhouette images. However, our method is independent of the choice of impostor geometry.

We animate and deform a surface reflectance field (SRF) by first applying a 3D warp to the impostor geometry. In order to preserve the warped object's appearance, it becomes necessary to blend the reflectance images invidiually for each point of the impostor geometry. We developed a new look-up function to evaluate the reflectance images of the warped SRF. This function depends on the warp and is used to shade the warped impostor geometry during image generation (Fig. 3). Shading a point on the impostor surface requires applying this look-up function to the surface point, the viewing ray, and the incident light direction. Once warped back into the acquisition frame, the point can be shaded by blending the reflectance images according to the mapped light direction and viewing ray.

In the remainder of this paper, we develop this look-up scheme. We discuss some shading issues and present our implementation based on a point-based impostor geometry. Section 6 shows some examples of deformed and animated surface reflectance fields.

# DEFORMABLE SURFACE REFLECTANCE FIELDS

Neglecting global light transport, a surface reflectance field can be understood as a discrete sampling of the object's BRDFs, knowing neither the exact location of the surface nor its normals. Ignoring wavelength and time, a BRDF is a scalar function BRDFðl l; v vÞ, describing the fraction of light that is reflected in direction v v as the surface is lit from direction l l. Similar to the BRDF notation, we use SRFðp p; l l; v vÞ to denote the reflectance of the SRF for an impostor point p p, a light direction l l, and a viewing direction v v. This relationship is fundamental for our analysis of appearance preservation during surface reflectance field animation.

The initial step in animating an SRF is to deform the impostor geometry. In this section, we assume the impostor warp is defined by a differentiable warp function

Shading an object includes queries to the surface reflectance field to determine the object's local reflectance. If the object is warped, the shading operation has to map a query ðp p Ã ; l l Ã ; v v Ã Þ in object space to a query ðp p; l l; v vÞ in the original acquisition space (Fig. 4). By intuition, the required mapping approximately follows the inverse warp É À1 .

However, applying É À1 to the lighting and viewing directions is not necessarily appearance preserving, especially in the case of nonuniform deformations. Section 4.1 develops a mapping L to perform this operation, leading to a new impostor parameterization presented in Section 4.2. The final shading process is discussed in Section 4.3.

## Approximate BRDF Preservation

In general, a mapping from object space to SRF acquisition space that preserves all aspects of the object's appearance cannot exist. This is due to the lack of exact object geometry and material properties in the SRF representation. Both would be needed to allow a prediction of complex nonlocal effects such as self-shadowing and interreflections.

Thus, we make the simplifying assumption, that the observed object can be described completely by its local BRDFs. We develop a look-up function that tries to preserve the main characteristics of the original object BRDFs. We do not aim at modeling changes in the BRDF due to the deformation of the material's microstructure. This would require precise knowledge of the structure, e.g., its microfacet distribution. Instead, we want to map the original BRDF to the deformed surface.

The desired look-up function is a mapping

We enforce appearance preservation by imposing three conditions:

1. Suppose the viewing ray in object space p p Ã þ sv v Ã ; s 2 IR intersects the warped object geometry at a point q q Ã  (see Fig. 5). Then, the viewing ray in acquisition space p p þ tv v; t 2 IR should intersect the original object at the corresponding point q q ¼ É À1 ðq q Ã Þ to ensure the reflected light originates from the same surface point with the same BRDF. Unfortunately, this condition cannot be guaranteed since the true object geometry is typically not known, i.e., the exact location of the points q q and q q Ã cannot be determined. However, it is a reasonable approximation to force the two viewing rays to intersect corresponding points of the impostor geometry since the impostor point p p is very likely close to q q. This can be achieved by choosing

2. l l and the surface normal m m in q q have to enclose the same angle as l l Ã and the normal m m Ã in q q Ã . This is a necessary condition to retain the reflectance characteristics of the object, as, for example, the shape of the reflectance lobes of the corresponding BRDF. The same condition applies for v v and v v Ã . Preserving the shape of the reflectance lobes requires preserving the angle between l l Ã and v v Ã as well (see Fig. 6).

# In order to preserve the effect of anisotropic object

BRDFs, l l and v v should have the same azimuthal orientation relative to the object surface as l l Ã and v v Ã on the warped object. (See Fig. 6.) As p p immediately follows from (3), the mapping ðp p Ã ; l l Ã ; v v Ã Þ7 !ðl l; v vÞ remains to be found. This can be rewritten as a locally affine mapping

of lighting and viewing directions in the vicinity of p p Ã . Note that L p p Ã is a function of p p Ã . According to the second condition, L p p Ã has to be angle preserving. By convention, l l, v v, l l Ã , and v v Ã are unit vectors, so L p p Ã needs to be length preserving as well. This implies that L p p Ã is an isometry, which means that the effect of L on l l Ã and v v Ã can be described by a rotation or a reflection, respectively, as a function of location p p Ã . In the remainder of this paper, we assume L p p Ã to be a rotation. The special case of a reflection can be handled similarly and is left out for simplicity.

Using this observation and interpreting (3) as a translation of p p Ã by É À1 ðp p Ã Þ À p p Ã , the total effect of L on a local setting around p p Ã can be expressed as a rigid transformation, translating the point p p Ã onto p p while rotating lighting and viewing directions.

Condition 2 further restricts L to rigid transformations that map the warped object normal at q q Ã onto the normal at the original point q q. We do not know the exact object geometry. Instead, we refer to the impostor normal in p p as an approximation of the true surface normal. Consequently, the searched L maps the tangential plane of the warped impostor point p p Ã onto the tangential plane in p p.

According to condition 3, L should be chosen to preserve l l Ã 's and v v Ã 's orientation inside the tangential plane. The following section presents a local impostor parameterization that enables one to track the transformation of the local tangential frame in order to find a mapping L that fulfills the conditions.

## Local Impostor Parameterization

We augment the impostor geometry with a local parameterization that allows us to determine the look-up function L at each impostor point p p Ã . The parameterization is independent of the geometric representation and can be applied to triangular meshes as well as to point sampled geometry. Depending on the representation, p p Ã can be a mesh vertex or a nonconnected surface point, respectively. This section develops the set of parameters that are stored at every point p p Ã (see Table 1).

Given an arbitrary warp É: IR 3 ! IR 3 , finding an explicit inverse function É À1 is impossible in general. Constraining the SRF deformation to cases where an explicit inverse warp function exists would be too limiting. Consequently, another design goal for the parameterization was to determine L without using a closed form of É À1 .

As shown above, L can be decomposed into a translational part and a rotation. The translation moves the warped impostor point back to its original position (see (3)). Storing the original position p p 0 in each impostor point p p Ã allows the application of the translation without using É À1 .

The rotational part L p p Ã (see ( 4)) aligns the warped tangential frame of the impostor point with the corresponding Fig. 5. A viewing ray p p Ã þ sv v Ã ; s 2 IR; in object space intersects the warped object at q q Ã . The corresponding viewing ray in the surface reflectance field's acquisition frame should intersect the object at the original object point q q. However, the impostor geometry of the SRF is typically not the same as the actual object geometry, so q q Ã and q q remain unknown. Instead, we are using p p ¼ É À1 ðp p Ã Þ as the origin of the viewing ray p p þ tv v; t 2 IR in acquisition space. Fig. 6. The bidirectional reflection distribution function (BRDF) describes the fraction of light from l l that is reflected toward v v. The spatial characteristics of a BRDF can be preserved by preserving the angles # l l , # v v , and when changing to acquisition space. Anisotropic materials require the preservation of the azimuthal orientations ' l l and ' v v relative to the surface frame. # l l and # v v are relative to the surface normal m m. In an SRF, m m is not exactly known. Instead, the impostor normal n n is taken as an approximation.

tangential system in the acquisition frame (see Fig. 7). To avoid the application of É À1 , the tangential orientation R 0 in the acquisition frame must be explicitly stored in p p Ã . R 0 is defined by the rotation matrix ðu u 0 ; v v 0 ; n n 0 Þ, built by the tangential system in acquisition space. u u 0 and v v 0 must be orthogonal and can be arbitrarily chosen. To minimize its memory footprint, R 0 can be stored as a Rodrigues vector [1] 

given R 0 as a rotation of angle # around an axis k k. This definition provides a minimal (i.e., three-dimensional) parameterization of R 0 . It contains a singularity for 180 rotations that can be avoided in our context as R 0 can be arbitrarily chosen. Additionally, a tangential coordinate system ðu u; v vÞ is attached to p p Ã . While p p 0 and R 0 remain unchanged during the deformation, ðu u; v vÞ is subject to the same warp as the geometry: After a deformation by É, ðu u; v vÞ is set to Éððu u 0 ; v v 0 ÞÞ. Applying the warp function É to a local tangential system is a standard problem in differential geometry. The tangential system has to be mapped by taking directional derivatives of É. In our implementation, we use central differences to determine u u and v v:

for a small " > 0. In particular, this only restricts É to be differentiable in a vicinity of the impostor geometry. Knowing R 0 and ðu u; v vÞ, the rotation L p p Ã can be easily reconstructed during rendering. Let

and

be the normal and the normalized bisecting vector of the warped tangential system spanned by u u and v v, respectively (see Fig. 7). Then,

build an orthogonalized tangential system that minimizes the squared angular differences between corresponding basis vectors of ðu u; v vÞ and ð" u u u u; " v v v vÞ. Using this orthogonalized system, the rotation L p p Ã is given by

Note that, by choosing ð" u u u u; " v v v vÞ as proposed, L p p Ã is an approximation of tangential orientation preservation in the sense of condition 3 of the previous section.

This approximation may introduce a slight rotation of the principal axis of an anisotropic BRDF when the surface is sheared. The rotation may be counterintuitive depending on the direction of the shear. In general, the effect of a shear on a real-world material effectively changes the original BRDF, depending on its microstructure. As the microstructure is not known, we decided to use the original BRDF. Thus, a tangential rotation of certain characteristics of the anisotropic BRDF cannot be avoided.

It may not be surprising that L turned out to be a rigid transformation. For rigid object transformations and cases where impostor geometry and object surface coincide, rotating the reflectance data according to the inverse object transformation is the appropriate choice. Consequently, this technique is used in many applications, e.g., for imagebased BRDF measurements [30], [19], [16], for bump mapping, for BTFs [4], [9], and for various other texturing techniques. All these techniques assume relatively accurate impostor geometry.

We assume arbitrary, in particular nonuniform, skewed deformations of an approximate impostor geometry that is different from the real object surface. The central result of our analysis is that, in these cases, again a rigid transformation of the impostor surface frame meets the requirements of appearance preservation best. Our framework allows the derivation of L for arbitrary deformations, using the local impostor parameterization. As the resulting transformation is rigid, material properties-including anisotropic BRDFs -stay the same, even for skewed object transformations.

# TABLE 1 The Local Impostor Parameterization Allows for the Determination of the Look-Up Function L during Rendering

The parameterization consists of a set of vectors ðp p 0 ; r r 0 ; u u; v vÞ in IR 3 , stored at each point of the discretized impostor geometry. p p 0 and r r 0 are fixed, while u uand v v have to be adapted whenever the geometry is deformed. Fig. 7. For each point on the impostor geometry, the local impostor parameterization provides two coordinate systems: The orthogonal tangential system R 0 in p p 0 in the acquisition frame and its warped counterpart on the rendered impostor geometry in object space, defined by p p Ã and ðu u; v vÞ. During rendering, p p 0 , R 0 , and the orthogonalized tangential system ð" u u u u; " v v v vÞ are used to determine the appearancepreserving back-projection of the SRF query.

## Shading

Once L is determined, an impostor point can be shaded as described in Section 3. However, there are some issues that should be considered when lighting a deformed surface reflectance field.

When using an environment map to light an SRF, it needs to be filtered according to the spatial resolution of the reflectance images representing the SRF (see Fig. 1). Using an unfiltered environment map may lead to aliasing artifacts if the map contains details that are finer than the spacing of the light sources used to acquire the SRF.

During rendering of a deformed SRF, L p p Ã is applied to all lighting directions incident to p p Ã . This corresponds to a rotation of the environment map before evaluating the SRF with that environment. Thus, the rotated environment map needs to be refiltered according to the reflectance field sampling. This operation would have to be performed for every surface point, which is impractical as filtering is an expensive operation for a nonuniform reflectance field sampling.

We present an alternative way to light a deformed surface reflectance field that comes without the need for refiltering. Although an SRF is acquired using directional lighting, we can simulate lighting by point light sources with only little artifacts.

Lighting an impostor point p p Ã by a point light source starts with the reflectance query ðp p Ã ; l l Ã ; v v Ã Þ describing the viewing ray to p p Ã , and direction l l Ã to the point lightsource as seen from p p Ã . Applying the look-up scheme ðp p; l l; v vÞ ¼ Lðp p Ã ; l l Ã ; v v Ã Þ transforms the query into acquisition space. SRFðp p; l l; v vÞ yields a reflectance coefficient that can be used to shade the impostor point p p with a color I p p :

where I l is the color of the point light source at p p l and AðdÞ is the light attenuation factor depending on the distance to the light source. Using the impostor point p p Ã instead of a point on the real object surface introduces an error in the incident lighting direction. But, usually, this error is small compared to the resolution of the SRF.

In contrast to environment mapping, this technique introduces SRF queries for lighting directions that are not present in the reflectance images. We rely on the SRF implementation to properly interpolate novel lighting directions, as discussed in Section 5.2.

The proposed approximation of point light-sources allows for dynamic lighting effects when animating surface reflectance fields. However, as our look-up scheme ignores global illumination effects, these effects may appear wrong on deformed objects.

Point light sources can also be used to implement environment mapping without the need to refilter the map for every impostor point. This can be done by properly subsampling the environment once for a dense set of directions. Then, point light sources are defined at these directions, colored by the corresponding values of the environment. Provided the subsampling is dense enough, lighting the scene with these light sources leads to an appropriate reconstruction of the lighting environment. Note that light direction interpolation implicitly acts as a reconstruction filter. Thus, adaptively filtering the environment map is traded for interpolation. This alternative scheme is easier to implement and fits naturally into the framework of point light sources. For more flexible lighting effects, environment maps and point light sources can be combined.

## Limitations

We presented a simple technique to preserve the appearance of a surface reflectance field under arbitrary deformations However, the look-up scheme contains some approximations affecting the proper reproduction of lighting effects. There are three classes of errors that may occur.

First, our BRDF-based derivation of the look-up function ignores nonlocal effects like interobject reflection, selfshadowing, refraction, or subsurface scattering. This may lead to false shadowing and erroneous refractions. However, modeling these effects requires incorporating the exact object geometry. As an SRF contains only approximate geometry information, these global lighting effects cannot be completely preserved during the deformation.

The BRDF preserving approach itself contains some approximations. As L p p Ã is derived from the local warp around the observed impostor point instead of a point on the real object surface, the warped SRF may show some BRDFs that seem to be rotated relative to the surface frame. The effect grows as the local warp's rotational part around p p Ã is different from the rotation of the observed, real surface point q q Ã . Note that the error introduced by choosing the impostor normal to determine L p p Ã is comparatively low. In fact, the normal is only used to derive the rotational approximation of the local warp. Evaluating the SRF does not incorporate a normal anymore. In particular, this normal has no impact on the reflectance properties of the reproduced BRDFs.

A third error class affects object/impostor parallaxis in regions where the impostor geometry is distant to the object surface: For nonuniform stretches, the object texture may appear to be shifted. This happens if the corresponding viewing rays in object and acquisition space do not intersect the object at corresponding points q q and q q Ã . Fig. 5 shows such an example. Despite these limitations, the proposed scheme shows significant advantages. Its ability to preserve reflectance properties without explicit knowledge of the real surface normals is crucial for the deformation of surface reflectance fields. Moreover, it makes it suited for many other imagebased applications where the exact object normals are not known.

An important property of this look-up scheme is that, in the limit, the BRDF preservation is exact as the SRF geometry converges to the real object geometry. The proposed method directly benefits from improvements of the geometric representation, for example, for geometry acquired with laser range scanning.

# IMPLEMENTATION

We implemented an animation system for surface reflectance fields similar to the system presented by Matusik et al. [20]. We improved the impostor representation, its rendering, and the reflectance field interpolation. Finally, we present a new shading scheme that speeds up the rendering of warped SRFs.

## Surfel Representation

Previous work on surface reflectance fields [20] used a pointbased representation of the impostor geometry. In this approach, the impostor was densely sampled by surfels. Surfels, as introduced by [26], are points in IR 3 , augmented by additional attributes, such as normal, radius, and some color properties. In their representation, the normal indicates the surface orientation, whereas the radius can be understood as an approximate, circular region of influence.

Subsequently, [35], [36] presented a framework to render surfels based on Heckbert's elliptical weighted average (EWA) texture filtering, [12]. EWA surface splatting is a forward-mapping algorithm that allows for high quality, aliasing-free rendering of point sampled geometry.

Although featuring high image quality, the surfel renderer as used by [20] is not suited for our purposes. It organizes the surfels in a static layered depth cube (LDC) tree, a fixed, axis aligned spatial data structure, that cannot be warped. Instead, we use a variant of the Pointshop3D renderer [34], which is an advanced version of EWA surface splatting. The Pointshop3D renderer is able to render unorganized point-sets and, thus, can cope with dynamically changing point sets.

Deformations of the impostor geometry may lead to visible holes in the point-based reconstruction. For reasonable deformations, this can be avoided by deforming the splat geometry appropriately. As proposed by [36], we are using elliptical surface splats. Fig. 8 shows the effect on a deformed patch of a surfel geometry. In contrast to circular splats that use a position/normal parametrization, our splats are defined by a position p p and two tangential vectors u u and v v, spanning a tangential coordinate system. u u and v v are explicitly allowed to be nonorthonormal. The surfel is associated with an elliptical region of influence defined by the tangential system (see Fig. 9).

When warping the impostor geometry, the warp has to be applied on each surfel's tangential system by using an affine approximation of the local distortion. In our implementation, this approximation is determined similarly to ðu u; v vÞ in Section 4.2. This ensures surface coverage as long as the warp's first derivative does not change excessively (see Fig. 8).

The surfel's tangential vectors u u and v v provide us directly with the corresponding parameters of our local impostor parameterization. By adding the surfel's original position p p 0 and orientation r r 0 to the set of surfel attributes, all impostor parameters required for the warped SRF rendering are encoded in the surfels.

## Reflectance Image Interpolation

In general, each surface reflectance field look-up SRFðp p; l l; v vÞ, must be interpolated from the fixed set of reflectance images. Depending on the viewing ray p p þ sv v; s 2 IR, the query must be handled by interpolating between the observing camera views of the SRF. View interpolation is a common problem in image-based rendering. Like Matusik et al. [20], we use unstructured lumigraph interpolation that was introduced with unstructured lumigraph rendering (ULR) [2].

ULR interpolation has proven to be a very flexible interpolation scheme that can be controlled by an arbitrary penalty function, rating each camera's appropriateness. In our implementation, we chose the same penalty as in [20].

In previous work, the queried lighting direction l l was always chosen from the set of acquired illuminations, sampling a stationary environment map. However, since our point light-source implementation produces arbitrary lighting directions, we have to interpolate reflectance queries between the acquired lighting directions as well.

This problem has been addressed by Koudelka et al. [15] who intersected the queried light ray with a triangulated hull of the acquisition lightsource positions. The intersected triangle yielded the three closest light sources that were consequently used to interpolate between three different lighting conditions. However, this does not work for arbitrary positions of the acquisition light sources. We also found that, for slim triangles in the hull, light source interpolation was not smooth enough.

Instead, we are also using ULR to interpolate between light directions. Treating the light sources of the acquisition stage as cameras at infinite distance enables us to use ULR for light source interpolation. In our implementation, this is done by using the same penalty function as for camera interpolation.

Using ULR for camera selection affords consideration of occlusions in the scene. If the observed object point is not visible from a given camera, this camera should not be considered for interpolation. When interpolating between light sources, there are no visibility constraints since shadowing effects are already captured in the acquired reflectance images. Moreover, taking occlusion into account would change the appearance of translucent or refractive materials.

## Reordered Evaluation

Compared to the shading of static objects, substantially more reflectance images are involved during the shading of   9. A surfel is defined by its position p p and its tangential system ðu u; v vÞ. u u and v v span a skewed coordinate system that defines the surfel's elliptical region of influence. a deformed model. This is because the rendered viewing rays tend to diverge in acquisition space when the impostor is warped (see Fig. 10).

The number of reflectance images involved in the shading process increases with deformations. Since SRF data usually exceeds conventional main memory size, most SRF look-ups must be read from disk. The time needed for disk access exceeds all other computation times by orders of magnitude. This makes SRF look-up performance a critical issue, especially when producing animated SRFs.

We address this problem with two techniques: A smaller cache holds the most recently used blocks of data. Unfortunately, naively shading the geometry shows adverse cache-coherency. Thus, as a second technique, all shading operations are decomposed into minimal shading operations, each containing a single SRF look-up. Table 2 shows their detailed structure. The execution of the shading operation is deferred until a larger number of operations has been collected. Sorting them before execution in a cache-optimal way decreases shading times by an order of magnitude. Moreover, due to the the cache coherent shading execution, the cache can be kept very small. In our system, it was sufficient to dimension the cache large enough to hold three reflectance images at the time. To facilitate the deferred shading, we accumulate all surfel colors first before rendering them to frame buffer.

# RESULTS

For our experiments, we use the two models shown in Fig. 11 that were scanned by Matusik et al. [20], [21]. The doll SRF is well-suited to the analysis of appearance preservation as it contains many different materials. The mug SRF was chosen to show the limitations of our approach as it contains refractive effects that cannot be handled correctly by our technique.

The reflectance images of the models were captured using the high dynamic range (HDR) technique of Debevec and Malik [6]. For each viewpoint and lighting condition, four 1; 360 Â 1; 032 pictures with different exposure time were taken. Using up to 432 different viewpoints and 60 light directions, this produced a total of 432 Â 60 Â 4 ¼ 103; 680 images. Uncompressed this would correspond to 407 GB of data. All reflectance images were compressed using a PCA compression that achieved a reduction of at least a factor of 10. Fig. 11 lists the compressed size of both models.

With these optimizations, the vast part of the rendering time is spent for the ULR computation. Our current implementation assumes arbitrarily placed cameras and light sources during the acquisition. Using knowledge about the scanner geometry or a spatial data structure to locate the k-nearest light sources or cameras would speed up the rendering times significantly. However, this optimization has not been performed, resulting in rendering times of about 10 minutes per frame for the doll data set with five point light sources on a 1GHz Pentium III.

View extrapolation is an important issue when deforming surface reflectance fields as parts of the objects may become visible from directions where no data was acquired before. The extrapolation is implicitly covered by the ULR interpolation. Fig. 12 shows an example. Fig. 13 shows the quality of appearance preservation at the example of the doll data set. Note the visual preservation of the different materials of the wooden base, the diffuse fabric, and the specular braid of the skirt. All scenes were lit by three colored point light sources (red, green, and blue) from static positions. Fig. 14 shows various deformations of the beer mug model. Although our approach is not able to preserve refractive effects, the results appear realistic for reasonable deformations.

Our surfel renderer distorts surface splats in object space according to the local warp. This allows for rendering large deformations without visible holes (Fig. 15).  Section 5.3 discussed the viewing ray divergence coming with the deformation of a surface reflectance field. Fig. 16 shows an example of an SRF warp together with its corresponding camera and light source blending fields. Both blending fields were visualized by assigning random colors to cameras and light sources, respectively. Subsequently, the colors were blended together according to the ULR interpolation coefficients. The blending fields clearly show the viewing ray divergence in distorted regions.

Fig. 17 shows a number of frames of a surface reflectance field animation, including large deformations and varying lighting conditions.

# CONCLUSIONS

We developed a novel scheme to deform and relight surface reflectance fields. Our technique approximately preserves all material properties of the captured object during deformation. The method uses an enclosing impostor geometry of the rendered object. An appearance preserving data look-up scheme employs a local parameterization of the impostor geometry without relying on proper surface normals. Our method is especially suited for relighting of real-world models with complex surface properties for which normals are hard to determine.

We presented an extended surfel representation to render deformable surface reflectance fields. Using elliptical splats that follow the local deformation in object space allowed for seamless rendering of deformations while preserving optimal texture quality. At the same time, the surfel representation naturally complements the local impostor parameterization. In principle, the presented look-up scheme can be used for any other image-based approach that uses approximating impostor geometry.    Simulating global lighting effects during deformation requires knowledge of the object geometry. While surface reflectance fields only provide an approximate geometry in general, this geometry is usually close to the real object surface. Exploiting this fact may lead to approximate methods to analyze and reproduce global illumination on deformable surface reflectance fields. Another way to preserve global effects would be to collect additional information during the acquisition process of the surface reflectance field. Matusik et al [20] proposed the opacity hull to explicitly capture translucency and refraction through an SRF. This information could be used to reconstruct the internal light transport. In particular, opacity hulls may be used to detect and manipulate self-shadowing inside a surface reflectance field.

Shifted texture parallaxis can be alleviated by enhancing the impostor geometry. Stereo algorithms could be used on textured objects to improve the geometric approximation. 

# ACKNOWLEDGMENTS

The authors would like to thank Matthias Zwicker, Remo Ziegler, Wojciech Matusik, and Addy Ngan for many valuable discussions.

