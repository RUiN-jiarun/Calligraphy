import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw

img_name='LantingXu.jpg'
kernel = np.ones((5, 5), np.uint8)
kernel1 = np.ones((9, 5), np.uint8)
kernel2 = np.ones((3, 5), np.uint8)
img = cv2.imread(img_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret,th1 = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY)
th1 = cv2.morphologyEx(th1, cv2.MORPH_ERODE, kernel)
# th1 = cv2.morphologyEx(th1, cv2.MORPH_DILATE, kernel1)
# th1 = cv2.morphologyEx(th1, cv2.MORPH_DILATE, kernel2)
# ret,th1 = cv2.threshold(th1, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('tmp', th1)
cv2.waitKey(0)