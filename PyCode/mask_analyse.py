import json
import os
import cv2
import math
import numpy as np


def get_mask_centroid(mask):
    # get mask contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0]
    # calculate centroid of contours
    M = cv2.moments(contours)
    c_x = int(M["m10"] / M["m00"])
    c_y = int(M["m01"] / M["m00"])

    centroid = [c_x, c_y]
    return centroid


def get_mask_area(mask_image):
    mask_pixel_value = mask_image[mask_image > 0.1]
    mask_area = len(mask_pixel_value)
    return mask_area


def get_visible_rate(mask_image, mask_visible_image):
    # get number of occluded pixel
    occlude_area = mask_image - mask_visible_image
    occlude_pixel_value = mask_image[occlude_area > 0.1]
    num_occluded = len(occlude_pixel_value)

    mask_area = get_mask_area(mask_image)
    visible_rate = 1 - (num_occluded / mask_area)
    return visible_rate

def mormalize(list):
    list = np.array(list)
    min_data = list.min()
    max_data = list.max()
    data_range = max_data - min_data
    norm_data = np.zeros(np.shape(list))





def main():
    # data directory
    data_dir = '/home/yumi/Project/Simulation/ImageGeneration-BlenderProc/output/bop_data/lmo/train_pbr'
    image_dir = os.listdir(data_dir)

    for sub_file in image_dir:
        if os.path.isdir(os.path.join(data_dir, sub_file)):
            scene_gt_path = os.path.join(data_dir, sub_file, 'scene_gt.json')
            with open(scene_gt_path, 'r') as f:
                data = json.load(f)
                for i in data:
                    scene_key = str(i)
                    scene = data[scene_key]

                    centroid_distence_grasp = []
                    centroid_distence_suction = []
                    visible_rate_list = []
                    mask_area_list = []
                    mask_visible_area_list = []
                    mask_name_list = []

                    for j, obj in enumerate(scene):
                        # get mask and depth image name
                        scene_id = "{:0>6d}".format(int(i))
                        mask_id = "{:0>6d}".format(int(j))
                        mask_name = "{}_{}.png".format(scene_id, mask_id)
                        depth_name = "{}.png".format(scene_id)

                        # grasp score
                        # grasp_score = distance to right midpoint + visible rate/mask area
                        right_midpoint = [215, 520]
                        left_midpoint = [200, 20]

                        # load mask
                        mask_path = os.path.join(data_dir, sub_file, 'mask', mask_name)
                        mask_visible_path = os.path.join(data_dir, sub_file, 'mask_visib', mask_name)

                        mask_image = cv2.imread(mask_path,
                                                cv2.IMREAD_GRAYSCALE)
                        mask_visible_image = cv2.imread(mask_visible_path,
                                                        cv2.IMREAD_GRAYSCALE)

                        # cv2.imshow("mask image", mask_image)
                        # cv2.imshow("mask visible image", mask_visible_image)
                        # cv2.waitKey(0)

                        # get centroid of mask
                        visible_mask_centroid = get_mask_centroid(mask_visible_image)

                        # distance between visible mask centroid and right midpoint
                        point_dif = visible_mask_centroid - right_midpoint
                        distance_2_right_midpoint = math.hypot(point_dif[0], point_dif[1])

                        # get visible rate
                        visible_rate = get_visible_rate(mask_image, mask_visible_image)

                        # get area of mask
                        mask_area = get_mask_area(mask_image)

                        # suction score
                        # suction_score = distance to lift midpoint + visible area
                        mask_visible_area = get_mask_area(mask_visible_image)

                        point_dif_lift = visible_mask_centroid - left_midpoint
                        distance_2_lift_midpoint = math.hypot(point_dif_lift[0], point_dif_lift[1])

                        centroid_distence_grasp.append(distance_2_right_midpoint)
                        centroid_distence_suction.append(distance_2_lift_midpoint)
                        visible_rate_list.append(visible_rate)
                        mask_area_list.append(mask_area)
                        mask_visible_area_list.append(mask_visible_area)
                        mask_name_list.append(mask_name)

                    # normalize



if __name__ == '__main__':
    main()
