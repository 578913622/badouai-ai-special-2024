import cv2
import numpy as np
'''
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])   
必要参数：
第一个参数是需要处理的原图像，该图像必须为单通道的灰度图；
第二个参数是低阈值；
第三个参数是高阈值。
'''
img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("canny",cv2.Canny(img,10,300))
cv2.waitKey(0)
cv2.destroyWindow()
