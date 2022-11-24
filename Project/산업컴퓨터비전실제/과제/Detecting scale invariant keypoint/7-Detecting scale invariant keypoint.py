# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:38:57 2021

@author: JSH
"""
import cv2
import numpy as np

img0 = cv2.imread('E:\\Study\\AI\\Lena.png', cv2.IMREAD_COLOR)
img1 = cv2.imread('E:\\Study\\AI\\lena1.png', cv2.IMREAD_COLOR)
img1 = cv2.resize(img1, None, fx=0.75, fy=0.75)
img1 = np.pad(img1, ((64,)*2, (64,)*2, (0,)*2), 'constant', constant_values = 0)
imgs_list = [img0, img1]

detector = cv2.xfeatures2d.SIFT_create(50)

for i in range(len(imgs_list)):
    keypoints, descriptors = detector.detectAndCompute(imgs_list[i], None)
    
    imgs_list[i] = cv2.drawKeypoints(imgs_list[i], keypoints, None, (0,255,0),
                                     flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    cv2.imshow('SIFT keypoints', np.hstack(imgs_list))
    cv2.waitKey()
    
    cv2.destroyAllWindows()
