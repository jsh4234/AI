# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:35:46 2021

@author: JSH
"""

import argparse
import cv2
import numpy as np, random

 
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='E:\Study\AI\Lena.png', help='Image path.')
parser.add_argument('--outputpath', default='E:\Study\AI\LenaRst.png', help='Image path.')
params = parser.parse_args()

image = cv2.imread(params.path)
w, h = image.shape[1], image.shape[0]
image_to_show = np.copy(image)
mouse_pressed = False
s_x = s_y = e_x = e_y = -1

def rand_pt():
    return (random.randrange(w),
            random.randrange(h))

def mouse_callback(event, x, y, flags, params):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouse Down")
        mouse_pressed = True
        s_x, s_y = x, y
        image_to_show = np.copy(image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            image_to_show = np.copy(image)

    elif event == cv2.EVENT_LBUTTONUP:
        print("mouse UP")
        mouse_pressed = False
        e_x, e_y = x, y
        
        
finish = False
while not finish:
    cv2.imshow("image", image_to_show)
    
    key = cv2.waitkey(0)
    
    if key == ord('r'):
        cv2.rectangle(image_to_show, (s_x, s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('l'):
        cv2.line(image_to_show, (s_x, s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('a'):
        cv2.arrowedLine(image_to_show, (s_x, s_y), rand_pt(), (0, 255, 0), 3)
    elif key == ord('w'):
        cv2.imwrite(params.out_png, image_to_show, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    elif key == ord('c'):
        image_to_show = np.copy(image)
    elif key == 27:
        finish = True
        
cv2.destroyAllWindows()