# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:39:41 2021

@author: JSH
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('E:\Study\AI\MLCC\20190814191758.bmp', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('E:\Study\AI\Lena.png', cv2.IMREAD_COLOR)


img_b, img_g, img_r = cv2.split(img)
cv2.imshow('Ori', img)

print("input r,g,b, / x= exit")

key = cv2.waitKey(0)
print(key)

Outflag = True
while Outflag:
    if key == ord('b'):
        cv2.imshow('Blue', img_b)
        hist, bins = np.histogram(img_b, 256, [0,255])
        img_equal = img_b
        Outflag = False
    elif key == ord('g'):
        cv2.imshow('Green', img_g)
        hist, bins = np.histogram(img_g, 256, [0,255])
        img_equal = img_g
        Outflag = False
    elif key == ord('r'):
        cv2.imshow('Red', img_r)
        hist, bins = np.histogram(img_r, 256, [0,255])
        img_equal = img_r
        Outflag = False
    elif key == ord('x'):
        Outflag = False
        
        

plt.fill_between(range(256), hist,0)
plt.xlabel('pixel value')
plt.show()

LastImg = cv2.equalizeHist((img_equal))

cv2.imshow('Equal Img', LastImg)

cv2.waitKey(0)
cv2.destroyAllWindows()