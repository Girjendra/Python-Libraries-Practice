import cv2 as cv
import numpy as np

# img = cv.imread('gradient.png')
# _, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# _, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# _, th3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
# _, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
# _, th5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)

# cv.imshow('img', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)

# cv.waitKey(0)
# cv.destroyAllWindows()
"""
Explanation:
Thresholding -> Thresholding converts a grayscale image into a binary image based on a threshold value.
Pixel ≥ threshold → white (255)
Pixel < threshold → black (0)
1. retval, dst = cv.threshold(src, thresh, maxVal, type)

src -> Input grayscale image
thresh -> Threshold value
maxVal -> Value assigned if condition is true
Type -> Type of thresholding to apply
| Binary              | cv.THRESH_BINARY              | Pixel value ≥ threshold → white (255), otherwise black (0)       |
| Binary Inverted     | cv.THRESH_BINARY_INV          | Pixel value ≥ threshold → black (0), otherwise white (255)       |
| Truncate            | cv.THRESH_TRUNC               | Pixel value > threshold → set to threshold value, else unchanged |
| To Zero             | cv.THRESH_TOZERO              | Pixel value < threshold → 0, else unchanged                      |
| To Zero Inverted    | cv.THRESH_TOZERO_INV          | Pixel value > threshold → 0, else unchanged                      |

these are global thresholding

"""



# img = cv.imread('sudoku.png')
# print(img.shape)
# img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# print(img.shape)
# _, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# cv.imshow('img', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)

# cv.waitKey(0)
# cv.destroyAllWindows()
"""
Explanation:
Adaptive Thresholding -> Threshold value changes for different image regions
Adaptive & Otsu are automatic methods
Otsu's Thresholding -> Automatic threshold selection
| Threshold Type      | OpenCV Flag                   | Meaning                                                          |
| Adaptive Mean       | cv.ADAPTIVE_THRESH_MEAN_C     | Threshold is mean of neighborhood area (handles uneven lighting) |
| Adaptive Gaussian   | cv.ADAPTIVE_THRESH_GAUSSIAN_C | Threshold is weighted sum (Gaussian) of neighborhood area        |
| Otsu's Thresholding | cv.THRESH_OTSU                | Automatically finds optimal threshold value                      |

2. cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
| Parameter      | Meaning                                            |
| src            | Input grayscale image                              |
| maxValue       | Value assigned to white pixels (usually 255)       |
| adaptiveMethod | How threshold is calculated (MEAN or GAUSSIAN)     |
| thresholdType  | Binary or Binary Inverse                           |
| blockSize      | Size of neighborhood (odd number: 3, 5, 11…)       |
| C              | Constant subtracted from mean                      |
"""