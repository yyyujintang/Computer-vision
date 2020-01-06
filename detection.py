import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

font = cv2.FONT_HERSHEY_SIMPLEX  # 使用默认字体
img = cv2.imread('0108.jpg', cv2.IMREAD_UNCHANGED)
#img = cv2.meanBlur(img,11)
#img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(img, 123, 255, cv2.THRESH_BINARY_INV)
# 先将图像转化成灰度，再转化成二值图像
print(img)
contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 检测边缘

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    # 用一个最小的矩形，把找到的形状包起来,还有一个带旋转的矩形
    # 返回(x,y)为矩形左上角坐标，w,h分别是宽和高
    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)#确定对角线然后画出矩阵

    if x != 0 and y != 0 and 150> w >= 20 and 150>h > 20:

        if 1 < (w / h) < 1.1 or 0.9 < (w / h) < 1 or (w / h) == 1:
            bottle_class = "front or reverse"
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 确定对角线然后画出矩阵
            cv2.putText(img, bottle_class + ' ' + '(' + str(int(x)) + ',' + str(int(y)) + ')', (int(x), int(y)), font,
                        0.4, (255, 0, 0), 1)
            print(w)
            print(h)


    rect = cv2.minAreaRect(c)  # 找到最小矩形区域
    if 150>rect[1][0] > 20 and 150> rect[1][1] > 20:
        box = cv2.boxPoints(rect)  # 找到最小矩形的顶点
        box = np.int0(box)
        if (rect[1][0] / rect[1][1]) > 1.2 or 0 < (rect[1][0] / rect[1][1]) < 0.8:
            bottle_class = "side"
            cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
            cv2.putText(img, bottle_class + ' ' + '(' + str(int(rect[0][0])) + ',' + str(int(rect[0][1])) + ')',
                        (int(rect[0][0]), int(rect[0][1])), font, 0.4, (255, 0, 0), 1)
            #print(((rect[1][0] / math.hypot(rect[1][0],rect[1][1])),(rect[1][1] / math.hypot(rect[1][0],rect[1][1])),0))

cv2.imshow('contours', img)
cv2.imwrite("test_detection.jpg", img)
cv2.waitKey()
