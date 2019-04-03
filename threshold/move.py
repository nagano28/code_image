# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:10:07 2018

@author: Nagano Masatoshi
"""

import cv2

#read image
img = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)

#moving average method
thresh_img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

#save image
cv2.imwrite('moving-average-method_lenna.bmp', thresh_img)