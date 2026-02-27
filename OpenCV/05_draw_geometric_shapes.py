import cv2 as cv
import numpy as np

# img = cv.imread("lena.jpg", 1)
img = np.zeros((500, 500, 3), dtype=np.uint8) # -> This image is commonly used as a blank canvas for drawing shapes

img = cv.line(img, (0, 0), (255, 255), (0, 255, 57), 10, cv.LINE_AA)
img = cv.arrowedLine(img, (0, 300), (255, 300), (0, 255, 57), 10)

img = cv.rectangle(img, (350, 0), (500, 150), (0, 0, 255), 10)
img = cv.circle(img, (400, 250), 80, (0, 255, 57), 10)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, "OpenCV",(0, 450), font, 4, (0, 255, 57), 10)
img = cv.ellipse(
        img,
        center=(250, 250),     # center of ellipse
        axes=(150, 80),        # major & minor axis
        angle=30,              # rotation angle
        startAngle=0,
        endAngle=360,          # full ellipse
        color=(0, 255, 0),     # green color (BGR)
        thickness=2
    )

pts = np.array([[(0,0), (350, 50), (300, 200), (100, 200)]])

cv.polylines(
    img,
    pts,
    isClosed=True,
    color=(0, 255, 0),
    thickness=2
)

cv.imshow("window", img)

cv.waitKey(0)
cv.destroyAllWindows()

"""
Explanation:
1. cv2.line(img, pt1, pt2, color(B, G, R), thickness=1, lineType=None, shift=None) -> Draws a straight line on an image.
| img       | numpy.ndarray | Image on which the line is drawn (modified in place) | img         |
| pt1       | (x, y)        | Starting point of the line                           | (50, 100)   |
| pt2       | (x, y)        | Ending point of the line                             | (300, 100)  |
| color     | (B, G, R)     | Line color in BGR format                             | (0, 255, 0) |
| thickness | int           | Line thickness in pixels (default = 1)               | 3           |
| lineType  | int           | Type of line drawing                                 | cv2.LINE_AA |
| shift     | int           | Number of fractional bits in coordinates (advanced)  | 0           |

2. cv2.arrowedLine(img, pt1, pt2, color, thickness=1, lineType=None, shift=None, tipLength=0.1) -> Draws a arrowed straight line on an image.
tipLength -> Length of arrow tip relative to arrow length(float)(0–1)

3. cv2.rectangle(img, pt1, pt2, color, thickness=1, lineType=None, shift=None)
| pt1       | (x, y)        | Top-left corner of the rectangle      |
| pt2       | (x, y)        | Bottom-right corner of the rectangle  |

4. cv2.circle(img, center, radius, color, thickness=1, lineType=None, shift=None)
| center    | (x, y)        | Center coordinates of the circle        |
| radius    | int           | Radius of the circle in pixels          |

5. cv2.putText(img, text, org, fontFace, fontScale, color, thickness=1, lineType=None, bottomLeftOrigin=False)
| text             | str           | Text string to be drawn                              | "OpenCV"                 |
| org              | (x, y)        | Bottom-left corner of the text                       | (50, 100)                |
| fontFace         | int           | Font type                                            | cv2.FONT_HERSHEY_SIMPLEX |
| fontScale        | float         | Size (scale) of the text                             | 1.0                      |
| color            | (B, G, R)     | Text color in BGR format                             | (0, 255, 0)              |
| thickness        | int           | Thickness of text strokes                            | 2                        |
| lineType         | int           | Type of line (`LINE_8`, `LINE_AA`)                   | cv2.LINE_AA              |
| bottomLeftOrigin | bool          | If `True`, origin is bottom-left instead of top-left | False                    |

6. cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=1, lineType=None, shift=None)
| img        | numpy.ndarray | Image on which the ellipse is drawn (modified in place) | img         |
| center     | (x, y)        | Center coordinates of the ellipse                       | (250, 250)  |
| axes       | (a, b)        | Length of major and minor axes (radius values)          | (100, 50)   |
| angle      | float         | Rotation angle of ellipse in degrees                    | 30          |
| startAngle | float         | Starting angle of the ellipse arc                       | 0           |
| endAngle   | float         | Ending angle of the ellipse arc                         | 360         |
| color      | (B, G, R)     | Ellipse color in BGR format                             | (0, 0, 255) |
| thickness  | int           | Thickness of ellipse border (`-1` fills ellipse)        | 2           |

"""