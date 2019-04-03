# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:32:13 2018

@author: Nagano Masatoshi
"""

import cv2
import numpy as np
import random

mean = 0
var = 0.1
sigma = 15

img = cv2.imread('lenna.bmp',1)

for i in range(2000):
    j_ = random.randint(0,255)
    k_ = random.randint(0,255)


    for j in range(len(img)):
        for k in range(len(img[0])):
            if j == j_ and k == k_:
                img[j_][k_] = 255

gray_noise = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('lenna_noise.bmp',gray_noise)