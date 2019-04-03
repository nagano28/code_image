# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:13:15 2018

@author: Nagano Masatoshi
"""

import cv2

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

#ここに処理を入れ込む
cv2.imwrite('gray_lenna.bmp', img)