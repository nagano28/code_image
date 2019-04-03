# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:13:15 2018

@author: Nagano Masatoshi
"""

import cv2

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

#sampling
#original width=256, high=256
original = 256
resize = 128
samp = int(original/resize)

orgHeight, orgWidth = img.shape[:samp]
size = (int(orgHeight/samp), int(orgWidth/samp))

#バイキュービック補間
#他にも補間方法は様々存在
CubicImg = cv2.resize(img, size, interpolation = cv2.INTER_CUBIC)

cv2.imwrite('gray_lenna%d.bmp'%(resize), CubicImg)