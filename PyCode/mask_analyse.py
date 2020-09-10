import json
import os

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
                    for j, obj in enumerate(scene):
                        # get mask and depth image name
                        scene_id = "{:0>6d}".format(int(i))
                        mask_id = "{:0>6d}".format(int(j))
                        mask_name = "{}_{}.png".format(scene_id, mask_id)
                        depth_name = "{}.png".format(scene_id)

                        # grasp score



                        # suction score






if __name__ == '__main__':
    main()