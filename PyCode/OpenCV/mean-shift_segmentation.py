import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs

for i in range(100):
    # load data
    suction_data_path = "/home/yumi/Datas/confidence_map/suction/{}_suction.npy".format(str(i))
    grasp_data_path = "/home/yumi/Datas/confidence_map/grasp/{}_grasp.npy".format(str(i))
    suction_data = np.load(suction_data_path)
    grasp_data = np.load(grasp_data_path)

    # Estimate bandwidth for meanshift algorithm
    bandwidth_suction = estimate_bandwidth(suction_data, quantile=0.1, n_samples=1000)
    ms_suction = MeanShift(bandwidth=bandwidth_suction, bin_seeding=True)
    bandwidth_grasp = estimate_bandwidth(grasp_data, quantile=0.1, n_samples=1000)
    ms_grasp = MeanShift(bandwidth=bandwidth_grasp, bin_seeding=True)

    ms_suction.fit(suction_data)
    ms_grasp.fit(grasp_data)

    labels_suction = ms_suction.labels_
    cluster_centers_s = ms_suction.cluster_centers_
    labels_grasp = ms_grasp.labels_
    cluster_centers_g = ms_grasp.cluster_centers_





