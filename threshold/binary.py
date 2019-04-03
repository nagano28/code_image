# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:38:06 2018

@author: Nagano Masatoshi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

thresh = 127

img = cv2.imread('lenna.bmp',0)
ret,threshimg = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)

cv2.imwrite('lenna_binary-thresh%d.bmp'%thresh,threshimg)

"""
def main():
    # 閾値
    t = 127

    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 出力画像用の配列生成
    th1 = gray.copy()

    # 方法1（NumPyで実装）
    th1[gray < t] = 0
    th1[gray >= t] = 255

    # 結果を出力
    cv2.imwrite("th1.jpg", th1)

if __name__ == "__main__":
    main()
"""