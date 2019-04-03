# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:32:32 2018

@author: Nagano Masatoshi
"""

import numpy as np
import cv2

img = cv2.imread('lenna.bmp')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#number of bit
K = 32
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imwrite('lenna_%dbit.bmp'%K,res2)
cv2.waitKey(0)
cv2.destroyAllWindows()