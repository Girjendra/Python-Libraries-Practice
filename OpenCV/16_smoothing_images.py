import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opencv-logo-white.png')
# img = cv.imread('lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

gaussian = cv.GaussianBlur(img, (5, 5), 0) 
average = cv.blur(img, (5, 5))
median = cv.medianBlur(img, 5)
F2D = cv.filter2D(img, -2, kernel)
BF = cv.bilateralFilter(img, 9, 75, 75)

titles = ['img', 'gaussian', 'average', 'median', 'F2D', 'BF']
images = [img, gaussian, average, median, F2D, BF]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
"""
Explanation:
Smoothing (Blurring) -> Smoothing reduces noise by averaging pixel values with neighboring pixels.
2. cv.filter2D(src, ddepth, kernel)
ddepth -> Depth of output image
       -> -1 → output depth same as input
1. cv.bilateralFilter(src, d, sigmaColor, sigmaSpace) ->
d -> Diameter of pixel neighborhood
  -> -1 → auto calculated
sigmaColor -> Controls color similarity
sigmaSpace -> Controls spatial distance

a kernel (or filter/mask) is a small matrix of numbers that slides over an image to
apply effects like blurring, sharpening, or edge detection by performing element-wise
multiplication and summation with the surrounding pixel values, effectively transforming
the image's features.
"""