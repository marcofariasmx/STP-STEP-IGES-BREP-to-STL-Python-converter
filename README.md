# STP-STEP-IGES-BREP-to-STL-Python-converter
Really simple STP-STEP-IGES-BREP to STL Python converter script

Some parameters can be tuned and useful information can be gathered as well.

The script supports multithreading for faster results.

It works using the Trimesh and GMSH libraries

Make sure you install them both with 

`
pip install trimesh[easy]
`

`
pip install gmsh-sdk
`

Simply run the following lines of code

![Import&use](/images/img1.png)

# Visualize the mesh 

![Import&use](/images/img2.png)

## You can get some useful information after the conversion is done like mesh volume, bounding box volume, surface area etc (default output in mm)

![Import&use](/images/img3.png)

# Voilà! The new mesh is exported

![Import&use](/images/img4.png)

![Import&use](/images/img5.png)




Example 3D model files downloaded from [Grabcad](https://grabcad.com/library/helical-bevel-gear-80/details?folder_id=11502171)


For more information, ideas and tutorials visit [marcofarias.com](marcofarias.com)

And a big shoutout of thanks to the creators of [Trimesh](https://github.com/mikedh/trimesh) and [GMSH](https://gitlab.onelab.info/gmsh/gmsh)