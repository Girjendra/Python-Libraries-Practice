import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
"""
Morphological transformations are used to remove noise, fill gaps, separate or
join objects, and refine object shapes in binary images. Morphology cleans shapes
"""
img = cv.imread('smarties.png', 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=3) # it fills black dots or increases the size of objects or we can use below
# dilation = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel, iterations=4)

erosion = cv.erode(mask,kernel, iterations=3) # it increases the size of black dots and objects or we can use below
# erosion = cv.morphologyEx(mask, cv.MORPH_ERODE, kernel, iterations=3)

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=3)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=3)

titles = ['Original', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()