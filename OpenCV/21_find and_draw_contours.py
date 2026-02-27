import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opencv-logo-white.png')
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imggray, 127, 255, 0)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours, -1, (0, 0, 255), 2)

print(len(contours))
cv.imshow('image', img)
cv.imshow('image gray', imggray)

cv.waitKey(0)
cv.destroyAllWindows()
"""
Eplanation:
Contours -> Contours are continuous curves (boundaries) that join all the points
            along the edge of an object having the same intensity.

kernel -> is a small matrix of numbers used to perform operations on an image,
          such as blurring, sharpening, or edge detection. 

1. mask = cv.morphologyEx(src, operation, kernel) -> A general OpenCV function used to apply morphological operations
src->Input image
     Usually a binary image
     Can be grayscale
Type of morphological operation:
| Operation         | Meaning                         |
| cv.MORPH_DILATE   | Dilation                        |
| cv.MORPH_ERODE    | Erosion                         |
| cv.MORPH_OPEN     | Erosion → Dilation              |
| cv.MORPH_CLOSE    | Dilation → Erosion              |

2. contours, hierarchy = cv2.findContours(image, mode, method) -> detects the boundaries (outlines) of objects in a binary image.
| Parameter| Type         | Description                                      |
| image   | numpy.ndarray | Binary image (white objects on black background) |
| mode    | int           | Contour retrieval mode                           |
| method  | int           | Contour approximation method                     |

Mode -> Controls which contours are retrieved.
| Mode              | Description                      | Use Case             |
| cv2.RETR_EXTERNAL | Only outer contours              | Object detection     |
| cv2.RETR_LIST     | All contours, no hierarchy       | Simple cases         |
| cv2.RETR_TREE     | All contours with full hierarchy | Complex shapes       |
| cv2.RETR_CCOMP    | 2-level hierarchy                | Holes inside objects |

methods -> Controls how contour points are stored.
| Method                  | Description              | Memory            |
| cv2.CHAIN_APPROX_NONE   | Stores all points        | High              |
| cv2.CHAIN_APPROX_SIMPLE | Removes redundant points | Low (Recommended) |

Return Values:
| Return    | Type          | Meaning                   |
| contours  | list          | List of detected contours |
| hierarchy | numpy.ndarray | Parent-child relationship |

Important Contour Functions:
| Function       | Purpose        |
| findContours() | Find contours  |
| drawContours() | Draw contours  |
| contourArea()  | Find area      |
| arcLength()    | Perimeter      |
| boundingRect() | Draw rectangle |

3. cv.drawContours(image, contours, contourIdx, color, thickness)
contourIdx = -1 for all contours
4. (x, y, w, h) = cv.boundingRect(contour:array)
5. area = cv.contourArea(contour:array)
"""