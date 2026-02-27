import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', 0)
canny = cv.Canny(img, 100, 200)

titles = ['img', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
"""
Explanation:
Canny Edge Detection -> Canny Edge Detection is a multi-step algorithm used to detect edges
                        (object boundaries) in an image with high accuracy and low noise. it
                        identifies sharp intensity changes in an image using gradient, non-maximum
                        suppression, and hysteresis thresholding.
1. edges = cv.Canny(image, threshold1, threshold2)
image -> Input image, Type: uint8
threshold1 (Lower Threshold) -> Lower bound for edge detection, Weak edges below this → ignored
threshold2 (Upper Threshold) -> Strong edge threshold, Edges above this → definitely edges

⚙️ Internal Steps of Canny Algorithm (Very Important) ->
Step 1: Noise Reduction -> Gaussian Blur removes noise
Step 2: Gradient Calculation -> Sobel operator finds intensity gradients
Step 3: Non-Maximum Suppression -> Keeps only strongest edges, Removes thick edges
Step 4: Double Thresholding -> Uses threshold1 and threshold2
Step 5: Edge Tracking by Hysteresis -> Weak edges connected to strong edges are kept, Others removed

"""