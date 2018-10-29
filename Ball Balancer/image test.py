import cv2

import numpy as np

img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv2.CV_HOUGH_GRADIENT, 1, 10)
