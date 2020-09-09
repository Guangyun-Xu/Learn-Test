
import os
import open3d as o3d
import trimesh
import numpy as np
import transforms3d as t3d


def bounding_box(bound, color):
    bound_x = bound[0]
    bound_y = bound[1]
    bound_z = bound[2]

    point_1 = [bound_x, bound_y, bound_z]
    point_2 = [-bound_x, bound_y, bound_z]
    point_3 = [-bound_x, -bound_y, bound_z]
    point_4 = [bound_x, -bound_y, bound_z]
    point_5 = [bound_x, -bound_y, -bound_z]
    point_6 = [bound_x, bound_y, -bound_z]
    point_7 = [-bound_x, bound_y, -bound_z]
    point_8 =[-bound_x, -bound_y, -bound_z]

    points = [point_1, point_2, point_3, point_4,
              point_5, point_6, point_7, point_8]

    lines = [[0, 1], [1, 2], [2, 3], [3, 0],
             [0, 5], [1, 6], [2, 7], [3, 4],
             [4, 5], [5, 6], [6, 7], [7, 4]]

    line_color = [color for i in range(len(lines))]
    line_set = o3d.LineSet()
    line_set.points = o3d.Vector3dVector(points)
    line_set.lines = o3d.Vector2iVector(lines)
    line_set.colors = o3d.Vector3dVector(line_color)

    return line_set

def main():
    unit = 'mm'

    # get mesh list
    mesh_folder_dir = "/media/yumi/Datas/Mesh/grasp_mesh_model/original_file/vv_finish_stl"
    mesh_list = os.listdir(mesh_folder_dir)
    # print(mesh_list)

    suffix = '.stl'
    for mesh_file in mesh_list:
        if (suffix in mesh_file):
            # load mesh and visualize
            mesh_path = os.path.join(mesh_folder_dir, mesh_file)

            mesh = trimesh.load_mesh(mesh_path)
            mesh.export(mesh_path.replace('.stl', '.ply'))
            mesh_o3d = o3d.read_triangle_mesh(mesh_path.replace('.stl', '.ply'))
            print(mesh_o3d)

            # unit conversion (m -> mm)
            max_bound = mesh_o3d.get_max_bound()
            if ((unit == 'mm') & (max_bound[0] < 1)):
                R = np.identity(3)
                T = np.zeros(3)
                Z = [1000.0, 1000.0, 1000.0]
                H = t3d.affines.compose(T, R, Z)
                mesh_o3d.transform(H)

            # draw object's bounding box
            new_mesh_bound = mesh_o3d.get_max_bound()
            color = [1, 0, 0]
            object_bbox = bounding_box(new_mesh_bound, color)

            # visualization, x, y, z axis will be rendered as red, green, and blue
            base_coordinate = o3d.create_mesh_coordinate_frame(size=50)

            # reference bbox
            reference_bound = [50, 50, 50]
            reference_color = [0, 1, 0]
            reference_bbox = bounding_box(reference_bound, reference_color)


            o3d.visualization.draw_geometries([reference_bbox, mesh_o3d, base_coordinate, object_bbox])

if __name__ == '__main__':
    main()