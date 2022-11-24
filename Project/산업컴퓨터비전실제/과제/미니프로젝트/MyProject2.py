
   
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('H:\\Study\\AI\\img\\L1.bmp', cv2.IMREAD_COLOR | cv2.WINDOW_NORMAL)
img2 = cv2.imread('H:\\Study\\AI\\img\\R1.bmp', cv2.IMREAD_COLOR | cv2.WINDOW_NORMAL)
roi = roi_back = img_ori = img.copy()

click = False    
x1,y1 = -1,-1

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x, y, flags, param):
    global x1,y1, click, roi, roi_back, w, h             

    if event == cv2.EVENT_LBUTTONDOWN:     
        click = True 
        x1, y1 = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        w = x - x1
        h = y - y1
        
        if w > 10 and h > 10:
            click = False;                                      
            cv2.rectangle(img,(x1,y1),(x,y),(0,255,0),1)
            w = x - x1
            h = y - y1
            roi = img_ori[y1:y1+h, x1:x1+w] 
            roi_back = roi.copy()
            cv2.imshow('ROI Apply', roi) 
            print("1,2,3,5,6,7")


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)             


while True:

    cv2.imshow('image', img)   
    
    k = cv2.waitKey(1) & 0xFF   

    if k == 27:               
        break
    elif k == 49: #1
            roi = cv2.Sobel(roi, cv2.CV_32F,1,0)
            cv2.imshow('ROI Apply', roi)  
    elif k == 50: #2
            roi = cv2.Sobel(roi, cv2.CV_32F,0,1)  
            cv2.imshow('ROI Apply', roi) 
    elif k == 51: #3
            ret, roi = cv2.threshold(roi, 120,255, cv2.THRESH_BINARY_INV)
            cv2.imshow('ROI Apply', roi)  
    elif k == 52: #4
           roi = img_ori[y1:y1+h, x1:x1+w] 
           hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
           hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
           color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
           cv2.imshow('ROI Apply', color_eq)  
    elif k == 53: #5
            roi = roi_back.copy()
            cv2.imshow('ROI Apply', roi)  
    elif k == 54: #6
            corners = cv2.cornerHarris(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
            corners = cv2.dilate(corners, None)
            show_img = np.copy(roi)
            show_img[corners>0.1 *corners.max()] = [0,0,255]
            corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))
            cv2.imshow('Harris corner detector', show_img)
    elif k == 55: #7
            dst = cv2.medianBlur(roi, 11)
            cv2.imshow('ROI Apply', dst)

            
            
            
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
    
fast = cv2.FastFeatureDetector_create(30, True, cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
kp = fast.detect(img)

show_img = np.copy(img)

cv2.waitKey(0)
cv2.destroyAllWindows()