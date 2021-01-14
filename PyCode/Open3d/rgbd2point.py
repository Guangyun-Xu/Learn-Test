import open3d as o3d

# create rgbd image
color_raw = o3d.io.read_image("/home/xu/Data/buffer_data/texture1.png")
depth_raw = o3d.io.read_image("/home/xu/Data/buffer_data/depth1.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_raw, depth_raw)

# create point cloud from rgbd image
image_width = 671
image_height = 502
fx = 1122.375
fy = 1122.375

cx = 334.4445
cy = 264.443075

intrinsic = o3d.camera.PinholeCameraIntrinsic(
    image_width, image_height, fx, fy, cx, cy)

colored_pc = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image, intrinsic)
print(colored_pc)
o3d.visualization.draw_geometries([colored_pc])

