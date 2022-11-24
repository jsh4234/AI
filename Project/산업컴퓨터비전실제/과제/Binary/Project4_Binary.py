# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:32:07 2021

@author: JSH
"""

import cv2
import numpy as np

img = cv2.imread('E:\Study\AI\Lena.png', cv2.IMREAD_COLOR)
cv img_binary
cv2.threshold(img, img_binary, 1, cv2.THRESH_BINARY)

cv2.imshow('Img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()