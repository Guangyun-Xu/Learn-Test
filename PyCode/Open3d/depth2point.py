import open3d as o3d
__all__ = [o3d]
print(o3d.__version__)

import numpy as np
depth_image_path = "/home/yumi/Project/Simulation/BlenderProc/test_depth/depth_1.png"
depth_raw = o3d.read_image(depth_image_path)
image_width = 640
image_height = 480
fx = 572.4114
fy = 573.57043

cx = 325.2611
cy = 242.04899

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
o3d.visualization.draw_geometries([pcd])