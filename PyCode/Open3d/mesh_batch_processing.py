
import os
import open3d as o3d
import trimesh
import numpy as np
import transforms3d as t3d

unit = 'mm'

# get mesh list
mesh_folder_dir = "/media/yumi/Datas/Mesh/grasp_mesh_model/original_file/vv_finish_stl"
mesh_list = os.listdir(mesh_folder_dir)
# print(mesh_list)

suffix = '.stl'
for mesh_file in mesh_list:
    if(suffix in mesh_file):
        # load mesh and visualize
        mesh_path = os.path.join(mesh_folder_dir, mesh_file)

        mesh = trimesh.load_mesh(mesh_path)
        mesh.export(mesh_path.replace('.stl', '.ply'))
        mesh_o3d = o3d.read_triangle_mesh(mesh_path.replace('.stl', '.ply'))
        print(mesh_o3d)

        max_bound = mesh_o3d.get_max_bound()
        if((unit == 'mm') & (max_bound[0]<1)):
            R = np.identity(3)
            T = np.zeros(3)
            Z = [1000.0, 1000.0, 1000.0]
            H = t3d.affines.compose(T, R, Z)
            mesh_o3d.transform(H)
        new_mesh_bound = mesh_o3d.get_max_bound()

        o3d.visualization.draw_geometries([mesh_o3d])