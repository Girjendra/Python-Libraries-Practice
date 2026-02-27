import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)
cv.imshow('Window1', img)

for line in lines:
    rho, theeta = line[0]
    a = np.cos(theeta)
    b = np.sin(theeta)
    x0 = rho*a
    y0 = rho*b

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))

    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow('Window2', img)

cv.waitKey(0)
cv.destroyAllWindows()



import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imshow('Window2', img)

cv.waitKey(0)
cv.destroyAllWindows()

"""
Explanation:
Hough Line Transform : The Hough Line Transform (HLT) is a classic computer vision technique
                       used to detect straight lines in images, even when the lines are broken or noisy.
Instead of finding lines in the image, we find them in a mathematical space.

❌ Problem with slope-intercept form
    y=mx+c
Fails for vertical lines (infinite slope)
✅ Hough Representation (Polar Form)
    ρ=xcosθ+ysinθ
Where:
ρ = distance from origin
θ = angle of the normal

Working Principle :
    Convert image to grayscale
    Detect edges (usually using Canny)
    For each edge point:
        Compute all possible (ρ, θ) pairs
    Store votes in an accumulator array
    Peaks in accumulator → detected lines

Types of Hough Line Transform
(a) Standard Hough Transform
    Uses full accumulator
    More accurate
    Computationally expensive
(b) Probabilistic Hough Transform (PHT)
    Uses random sampling
    Faster
    Returns line segments instead of infinite lines

Standard Hough Transform:
1. lines = cv2.HoughLines(image, rho, theta, threshold)
|   Parameter   |   Data Type     |   Description                                                                                                    |   Typical Values   |
|   image       |  numpy.ndarray  | Input   binary edge image   (usually output of Canny edge detector). Non-zero pixels are treated as edge points. |  edges             |
|   rho         |  float          | Distance resolution of the accumulator in   pixels  . It defines the precision of ρ.                             |  1                 |
|   theta       |  float          | Angle resolution of the accumulator in   radians  . Determines precision of θ.                                   |  np.pi/180  (1°)   |
|   threshold   |  int            | Minimum number of   votes   required in the accumulator to detect a line. Higher value → fewer lines detected.   |  100 - 200         |

|   Output   |   Type   |   Description                                             |
|   lines    |  array   | Each line is represented as  (ρ, θ)  in polar coordinates |
Example output:
[[[rho1, theta1]],
 [[rho2, theta2]],
 ...]

2. lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap)
|   Parameter       |   Data Type     |   Description                                                                                                    |   Typical Values   |
|   image           |  numpy.ndarray  | Input   binary edge image   (non-zero pixels are treated as edge points). Usually output of Canny edge detector. |  edges             |
|   rho             |  float          | Distance resolution of the accumulator in   pixels  . Smaller value → higher accuracy.                           |  1                 |
|   theta           |  float          | Angle resolution in   radians  . Smaller value → finer angle detection.                                          |  np.pi/180         |
|   threshold       |  int            | Minimum number of   votes   required to consider a line. Higher value → fewer detected lines.                    |  50 - 150          |
|   minLineLength   |  int            | Minimum length of a line segment (in pixels) to be accepted. Shorter lines are rejected.                         |  30 - 100          |
|   maxLineGap      |  int            | Maximum allowed gap (in pixels) between two collinear points to merge them into one line.                        |  5 - 20            |

|   Output   |   Type   |   Description                                                |
|   lines    |  array   | Each line is represented by   endpoints   (x1, y1, x2, y2)   |
Example output:
[[[x1, y1, x2, y2]],
 [[x1, y1, x2, y2]],
 ...]

Difference :
| Feature        | HoughLines | HoughLinesP      |
=| Transform Type | Standard   | Probabilistic    |
| Output         | (ρ, θ)     | (x1, y1, x2, y2) |
| Speed          | Slower     | Faster           |
| Memory         | High       | Low              |
| Lines          | Infinite   | Line segments    |
"""