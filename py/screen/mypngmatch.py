import cv2 as cv

img = cv.imread('pikaqiu.png', 0)

template = cv.imread('template.png', 0)

res = cv.matchTemplate(img, template, cv.TM_SQDIFF)

print(res)