import open3d as o3d
import numpy as np
import trimesh


mesh_path = "/home/xu/D_2_full.obj"
mesh = o3d.io.read_triangle_mesh(mesh_path)
# o3d.visualization.draw_geometries([mesh])

# cover mesh to point cloud
pc = mesh.sample_points_poisson_disk(10000)
# o3d.visualization.draw_geometries([pc])

pc.normals = o3d.utility.Vector3dVector(np.zeros((1, 3)))
pc.estimate_normals()
#o3d.visualization.draw_geometries([pc], point_show_normal=True)

pc.orient_normals_consistent_tangent_plane(100)
o3d.visualization.draw_geometries([pc], point_show_normal=True)

distances = pc.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 1.5 * avg_dist

mesh_new = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pc,
                                                                           o3d.utility.DoubleVector([radius,radius*2]))
tri_mesh = trimesh.Trimesh(np.asarray(mesh_new.vertices),np.asarray(mesh_new.triangles),
                           vertex_normals=np.asarray(mesh_new.vertex_normals))

trimesh.convex.is_convex(tri_mesh)

tri_mesh.show()
tri_mesh.export('/home/xu/D_2_full_new_1.obj')