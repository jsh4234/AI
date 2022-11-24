# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:35:32 2021

@author: JSH
"""

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('--path', default='E:/Study/AI/Lena.png', help='Image path.')
grey = cv2.imread(params.path)
color = grey

cv2.imshow('original grey', grey)
cv2.waitKey()

hist, bins = np.histogram(grey, 256, [0, 255])
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

grey_eq = cv2.equalizeHist(grey)
hist, bins = np.histogram(grey_eq, 256, [0, 255])
plt.fill_between(range(256), hist, 0)
plt.xlabel('pixel value')
plt.show()

cv2.imshow('equalized grey',grey_eq)
cv2.waitKey()

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('original color', color)
cv2.imshow('equalized color', color_eq)
cv2.waitKey()
cv2.destroyAllWindows()
