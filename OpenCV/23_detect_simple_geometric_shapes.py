import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('shapes2.png')
img = cv.resize(img, (700, 700))
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imggray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, closed=True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0] - 30
    y = approx.ravel()[1] - 10

    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectratio = w / float(h)
        if 0.95 < aspectratio < 1.05:
            cv.putText(img, 'Square', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
        else:
            cv.putText(img, 'Rectangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    elif len(approx) == 6:
        cv.putText(img, 'Hexagon', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

cv.imshow('Window', img)

cv.waitKey(0)
cv.destroyAllWindows()
"""
Explanation:
1. approx = cv2.approxPolyDP(curve, epsilon, closed)
| Parameter      | Data Type     | Description                                                                                   | Typical Value / Example         |
| curve          | numpy.ndarray | Input contour (set of points) to be approximated. Usually obtained from cv2.findContours()    | cnt                             |
| epsilon        | float         | Maximum distance between the original contour and the approximated polygon. Controls accuracy | 0.01 * cv2.arcLength(cnt, True) |
| closed         | bool          | Specifies whether the contour is closed or open                                               | True (for shapes)               |
| Return Value   | numpy.ndarray | Approximated polygon with fewer vertices                                                      | approx                          |

2. lenght = cv2.arcLength(curve, closed)
|   Parameter      |   Data Type     |   Description                                                  | Typical Value / Example              |
| curve            | numpy.ndarray   | Input contour whose perimeter (arc length) is to be calculated | cnt                                  |
| closed           | bool            | Indicates whether the curve is closed or open                  | True (for shapes)                    |
| Return Value     | float           | Total perimeter (arc length) of the contour                    | perimeter = cv2.arcLength(cnt, True) |

3. approx.ravel()
|   Aspect    |   Details                                           |
| Function    | ravel()                                             |
| Library     | NumPy                                               |
| Used on     | approx (output of cv2.approxPolyDP)                 |
| Purpose     | Converts a multi-dimensional array into a 1-D array |
| Output Type | numpy.ndarray (1-D)                                 |
[[[x1, y1]],
 [[x2, y2]],
 [[x3, y3]]]
Converts it to: [x1, y1, x2, y2, x3, y3]
"""