# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:39:25 2021

@author: JSH
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread


img = imread('me.jpg')

plt.imshow(img)
plt.show()
