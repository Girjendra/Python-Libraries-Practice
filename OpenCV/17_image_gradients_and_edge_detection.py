import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
# img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
scharr = cv.Scharr(img, cv.CV_64F, 0, 1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
scharr = np.uint8(np.absolute(scharr))

sobelcomb = cv.bitwise_or(sobelx, sobely)
canny = cv.Canny(img, 100, 200)

titles = ['img', 'lap', 'sobelx', 'sobely', 'sobelcomb', 'scharr', 'canny']
images = [img, lap, sobelx, sobely, sobelcomb, scharr, canny]

for i in range(7):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
"""
Explanation:
Image Gradient -> An image gradient measures the change in intensity (brightness) between neighboring pixels.
1. cv2.Laplacian(src, ddepth, ksize) -> Computes second-order derivatives, Detects edges in all directions
| Parameter  | Description            |
| src        | Input image            |
| ddepth     | Output depth(datatype) |
| ksize      | Kernel size            |
2. cv2.Sobel(src, ddepth, dx, dy, ksize) -> Computes first-order derivatives, Detects edges in X or Y direction
| Parameter  | Type    | Description                                   |
| src        | ndarray | Input image (grayscale recommended)           |
| ddepth     | int     | Output image depth (cv2.CV_64F recommended) |
| dx         | int     | Order of derivative in X                      |
| dy         | int     | Order of derivative in Y                      |
| ksize      | int     | Kernel size (1,3,5,7)                         |
3. cv2.Scharr(src, ddepth, dx, dy) -> More accurate than Sobel
| Parameter  | Description     |
| src        | Input image     |
| ddepth     | Output depth    |
| dx         | X derivative    |
| dy         | Y derivative    |
"""