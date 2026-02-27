import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 1)

# d1 = cv.pyrDown(img)
# d2 = cv.pyrDown(d1)
# u2 = cv.pyrUp(d2)
# cv.imshow('img', img)
# cv.imshow('d1', d1)
# cv.imshow('d2', d2)
# cv.imshow('u2', u2)


cv.imshow('img', img)
layer = img.copy()
gp = [layer]
for i in range(5):
    # cv.imshow(str(i), layer)
    layer = cv.pyrDown(layer)
    gp.append(layer)

layer = gp[4]
for i in range(4, 0, -1):
    gu_ex = cv.pyrUp(gp[i])
    laplasian = cv.subtract(gp[i-1], gu_ex)
    cv.imshow(str(i), laplasian)


cv.waitKey(0)
cv.destroyAllWindows()
"""
Explanation:
Image Pyramids -> Image pyramids are a collection of images where each
                  level is a scaled (resized) version of the previous one.
Types of Image Pyramids :
1️⃣ Gaussian Pyramid ->Image is downscaled, Used for reducing image size
Each level:
        Applies Gaussian blur
        Reduces image size by half
1. down = cv.pyrDown(src)
2. up = cv.pyrUp(src)
⚠️ pyrUp() does not restore exact original image
Pyramid Levels Visualization
Level 0: 512 × 512
Level 1: 256 × 256
Level 2: 128 × 128
Level 3: 64 × 64

2️⃣ Laplacian Pyramid -> Stores difference between levels, Used for image reconstruction & blending
Laplacian Pyramid = Original - Gaussian Downscaled & Upscaled Image
"""