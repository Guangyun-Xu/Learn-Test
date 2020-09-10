import cv2
import numpy as np


img = cv2.imread('/media/yumi/Datas/Blender_output/0909/bop_data/'
                 'lmo/train_pbr/000000/mask_visib/000000_000000.png',
                 cv2.IMREAD_GRAYSCALE)

# ret, thresh = cv2.threshold(img, 125, 255, 0)




contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)

# color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
# cv2.imshow("contours", color)
# cv2.waitKey(0)

# compute the center of the contour
contours = contours[0]
M = cv2.moments(contours)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.circle(color, (cX, cY), 7, (0, 255, 0), -1)  # draw circle
cv2.drawContours(color, contours, -1, (255, 0, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey(0)