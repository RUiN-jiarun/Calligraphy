import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw


img_name='LantingXu.jpg'
kernel = np.ones((9, 7), np.uint8)
# kernel1 = np.ones((2, 2), np.uint8)
img = cv2.imread(img_name)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, th1 = cv2.threshold(imgray, 70, 255, cv2.THRESH_BINARY)
# th1 = cv2.morphologyEx(th1, cv2.MORPH_DILATE, kernel1)
# th1 = cv2.morphologyEx(th1, cv2.MORPH_ERODE, kernel)

# th1 = cv2.morphologyEx(th1, cv2.MORPH_ERODE, kernel1)
# ret,th1 = cv2.threshold(th1, 100, 255, cv2.THRESH_BINARY_INV)

b, g, r = cv2.split(img)
# 去除印章
ret, r_bin = cv2.threshold(r, 75, 255, cv2.THRESH_BINARY)
cv2.imshow('test', r_bin)
cv2.waitKey(0)
th1 = cv2.morphologyEx(r_bin, cv2.MORPH_ERODE, kernel)
cv2.imshow('tmp', th1)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow("img", img)
cv2.waitKey(0)


f = Image.open(img_name)
total = len(contours)
draw = ImageDraw.Draw(f)

for h, cnt in enumerate(contours): 
    if len(cnt) > 100:
        # print '%s:\t' % (total - h),
        # top_left & bottom_right
        x_list = []
        y_list = []
        for i in cnt:
            x_list.append(i[0][0])
            y_list.append(i[0][1])
        
        margin = 50
        x0 = min(x_list)
        y0 = min(y_list)
        x1 = max(x_list)
        y1 = max(y_list)
        print (x0, y0, x1, y1)
        
        draw.rectangle((x0, y0, x1, y1), outline='red')
        #draw.line(((x0+x1)/2, y0, (x0+x1)/2, y1), 
        #          fill=(255,255,255), width=1)
        #draw.line(((x0,(y0+y1)/2, x1,(y0+y1)/2)), 
        #          fill=(255,255,255), width=1)
        
        
f.save('allinone.jpg')