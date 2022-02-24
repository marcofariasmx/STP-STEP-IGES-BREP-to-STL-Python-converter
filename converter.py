#pip install trimesh[easy]
#pip install gmsh-sdk

import trimesh

#General info found on https://trimsh.org/trimesh.interfaces.gmsh.html
#Returns a surface mesh from CAD model in Open Cascade Breap (.brep), Step (.stp or .step) and Iges formats Or returns a surface mesh from 3D volume mesh using gmsh.
#For a list of possible options to pass to GMSH, check: http://gmsh.info/doc/texinfo/gmsh.html

mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name = 'helical bevel gear.STEP', gmsh_args = [
            ("Mesh.Algorithm", 1), #Different algorithm types, check them out
            ("Mesh.CharacteristicLengthFromCurvature", 50), #Tuning the smoothness, + smothness = + time
            ("General.NumThreads", 10), #Multithreading capability
            ("Mesh.MinimumCirclePoints", 32)])) 

## Visualize the formed mesh (applicable if on jupyter notebook)
#scene = mesh.scene()
#scene.show()

## We can also get some properties of the formed mesh like volume, bounding box volume, surface area etc (default output in mm)
print("Mesh volume: ", mesh.volume)
print("Mesh Bounding Box volume: ", mesh.bounding_box_oriented.volume)
print("Mesh Area: ", mesh.area)

## Export the new mesh in the STL format
mesh.export('helical bevel gear_converted.STL')