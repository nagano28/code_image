# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:04:52 2018

@author: Nagano Masatoshi
"""

import cv2

#read image
img = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)

#otsu
_, thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#save image
cv2.imwrite('otsu_lenna.bmp', thresh_img)