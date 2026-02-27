import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

apl = cv.imread('apple.jpg')
org = cv.imread('orange.jpg')
app_org = np.hstack((apl[:, :256], org[:, 256:]))

apple_copy = apl.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = org.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gu_ex = cv.pyrUp(gp_apple[i])
    laplasian = cv.subtract(gp_apple[i-1], gu_ex)
    lp_apple.append(laplasian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gu_ex = cv.pyrUp(gp_orange[i])
    laplasian = cv.subtract(gp_orange[i-1], gu_ex)
    lp_orange.append(laplasian)

apple_orange_pyr = []
for apple , orange in zip(lp_apple, lp_orange):
    cols, _, _ = apple.shape
    lp = np.hstack((apple[:, :int(cols/2)], orange[:, int(cols/2):]))
    apple_orange_pyr.append(lp)

apple_orange_reconstruct = apple_orange_pyr[0]
for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyr[i], apple_orange_reconstruct)

cv.imshow('apple', apl)
cv.imshow('orange', org)
cv.imshow('app_org', app_org)
cv.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
"""
Explanation:
Image blending using pyramids is an advanced image processing technique used to
smoothly combine two images without visible seams.

🧠 Concept Behind Pyramid Blending
-> Build Gaussian pyramids for both images
-> Build Laplacian pyramids
-> Blend each level
-> Reconstruct final image
"""