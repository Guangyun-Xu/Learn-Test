# pip install open3d-python==0.5
import open3d as o3d

__all__ = [o3d]
print(o3d.__version__)

import numpy as np
import cv2

depth_image_path = "/home/yumi/Datas/sgp_dataset/train_data/train_1018/000000/depth/000011.png"
depth_raw = o3d.read_image(depth_image_path)
image_width = 671
image_height = 502
fx = 1122.375
fy = 1122.375

cx = 334.4445
cy = 264.443075

# cx = 256
# cy = 256

intrinsic = o3d.PinholeCameraIntrinsic(
    image_width, image_height, fx, fy, cx, cy)
extrinsic = np.identity(4)
print(extrinsic)
depth_scale = 10
depth_trunc = 1500.0  # 超过depth_trunc的深度值将会被设为0

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
H_base_in_camera = np.array([[0.0101817, -0.985716, -0.16811, 393.806],
                             [-0.999944, -0.00953149, -0.00467393, 274.026],
                             [0.00300482, 0.168148, -0.985757, 1340.7],
                             [0, 0, 0, 1]])
camera_coordinate_frame.transform(H_base_in_camera)
base_coordinate_frame = o3d.create_mesh_coordinate_frame(size=1000, origin=[0, 0, 0])
o3d.visualization.draw_geometries([pcd])
ply_path = "/home/yumi/Share/haonan/000011_pc.ply"
o3d.write_point_cloud(ply_path, pcd, write_ascii=True)

show_obj_pc = True
if show_obj_pc:
    obj_mask_path = "/home/yumi/Share/haonan/src/mask/000011/000011_000000.png"
    obj_mask = cv2.imread(obj_mask_path,  cv2.IMREAD_ANYDEPTH)
    obj_mask = (np.asarray(obj_mask > 0)).astype("uint8")
    # mask_idx = obj_mask > 0
    # mask_idx = mask_idx.nonzero()
    # np_depth[~mask_idx] = 0
    np_depth = np_depth * obj_mask
    obj_depth_raw = o3d.geometry.Image(np_depth)
    obj_pc = o3d.create_point_cloud_from_depth_image(
    depth=obj_depth_raw, intrinsic=intrinsic, extrinsic=extrinsic,
    depth_scale=depth_scale, depth_trunc=depth_trunc, stride=int(1))
    obj_pc, _ = o3d.statistical_outlier_removal(obj_pc, 10, 5)
    o3d.visualization.draw_geometries([obj_pc])
    obj_ply_path = "/home/yumi/Share/haonan/observed_pc.ply"
    o3d.write_point_cloud(obj_ply_path, pcd, write_ascii=True)