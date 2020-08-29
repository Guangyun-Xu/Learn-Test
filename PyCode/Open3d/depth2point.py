# pip install open3d-python==0.5
import open3d as o3d
__all__ = [o3d]
print(o3d.__version__)

import numpy as np

depth_image_path = "/home/yumi/Project/Simulation/BlenderProc/test_depth/depth_3.png"
depth_raw = o3d.read_image(depth_image_path)
image_width = 1032
image_height = 772
fx = 1122.375
fy = 1122.375

cx = 514.53
cy = 406.8355

# cx = 256
# cy = 256

intrinsic = o3d.PinholeCameraIntrinsic(
    image_width, image_height, fx, fy, cx, cy)
extrinsic = np.identity(4)
print(extrinsic)
depth_scale = 10
depth_trunc = 30000.0  # 超过depth_trunc的深度值将会被设为0

np_depth = np.array(depth_raw)
depth_raw = o3d.geometry.Image(np_depth)
print(depth_raw)
print(type(depth_raw))
print(type(intrinsic))

color = True
pcd = o3d.create_point_cloud_from_depth_image(
    depth=depth_raw, intrinsic=intrinsic, extrinsic=extrinsic,
    depth_scale=depth_scale, depth_trunc=depth_trunc, stride=int(1))
if not color:
    pcd.paint_uniform_color([0, 255, 0])

camera_coordinate_frame = o3d.create_mesh_coordinate_frame(size=100)
H_base_in_camera = np.array([[0.0101817,	-0.985716,	-0.16811, 393.806],
                             [-0.999944,	-0.00953149,	-0.00467393, 274.026],
                             [0.00300482,	0.168148,	-0.985757, 1340.7],
                             [0, 0, 0, 1]])
camera_coordinate_frame.transform(H_base_in_camera)
base_coordinate_frame = o3d.create_mesh_coordinate_frame(size=1000, origin=[0,0,0])
o3d.visualization.draw_geometries([base_coordinate_frame, pcd, camera_coordinate_frame])
ply_path = depth_image_path[:-4] + ".ply"
o3d.write_point_cloud(ply_path,pcd)
