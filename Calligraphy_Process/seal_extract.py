import cv2
import numpy as np

img_name='LantingXu.jpg'
kernel = np.ones((3, 3), np.uint8)
kernel1 = np.ones((5, 5), np.uint8)
img = cv2.imread(img_name)


b, g, r = cv2.split(img)
# cv2.imshow('tmp', r)
# cv2.waitKey(0)
# cv2.imshow('tmp', g)
# cv2.waitKey(0)
# cv2.imshow('tmp', b)
# cv2.waitKey(0)
x = -(g + r)
cv2.imshow('testtest', x)
cv2.waitKey(0)
# 去除印章
ret, r_bin = cv2.threshold(x, 140, 255, cv2.THRESH_BINARY)
cv2.imshow('test', r_bin)
cv2.waitKey(0)
th1 = cv2.morphologyEx(r_bin, cv2.MORPH_DILATE, kernel)
th1 = cv2.morphologyEx(th1, cv2.MORPH_ERODE, kernel1)
cv2.imshow('tmp', th1)
cv2.waitKey(0)

cv2.imwrite('seal.jpg', th1)

# TODO: denoise