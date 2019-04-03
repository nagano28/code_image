# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:54:20 2018

@author: Nagano Masatoshi
"""

import cv2
import numpy as np

#read image
img = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)

#histgram
hist,bins = np.histogram(img.ravel(),256,[0,256])

#p-tile
p_all_hist = 0.0
ret = 0.5 #%
for i in range(len(hist)):
    p_hist = float(hist[i])/float(sum(hist))
    p_all_hist += p_hist
    #print p_all_hist
    if p_all_hist > ret:
        #print "slice"
        ret,thresh1 = cv2.threshold(img,i,255,cv2.THRESH_BINARY)

#save image
cv2.imwrite('lenna_p-tile_binary%d.bmp'%ret,thresh1)
