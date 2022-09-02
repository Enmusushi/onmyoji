import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pikaqiu.png', 0)

template = cv.imread('template.png', 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img, template, cv.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
left_top = min_loc
right_bottom = (left_top[0] + w, left_top[1] + h)
cv.rectangle(res, left_top, right_bottom, 255, 2)
plt.imshow(res, cmap='gray')
plt.show()
# print(res)
