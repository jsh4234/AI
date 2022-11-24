# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:06:36 2021

@author: JSH
"""

import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='E:/Study/AI/Lena.png', help='Image path.')
params = parser.parse_args()
img = cv2.imread(params.path)

print('Shape:',img.shape)
print('Data type:', img.dtype)
cv2.imshow("original", img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print('Converted to grayscale:')
print('Shape:', gray.shape)
print('Data type:', gray.dtype)
cv2.imshow("gray-scale img", gray)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print('Converted to grayscale:')
print('Shape:', gray.shape)
print('Data type:', gray.dtype)

hsv[:,:,2] *= 2
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Converted back to BGR from HSV')
print('Shape:', from_hsv.shape)
print('Data type:', from_hsv.dtype)
cv2.imshow("from_hsv", from_hsv)

cv2.waitKey(0)
cv2.destoryAllWindows()