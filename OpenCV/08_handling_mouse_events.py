import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

def mouse_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("Left Click at:", x, y)
        strxy = str(x) + ', ' + str(y)
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, strxy, (x, y), font, 1, (0, 255, 0), 2)
        cv.imshow('Window', img)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 20, (0, 255, 0), 2)
        cv.imshow('Window', img)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("messi5.jpg")
cv.imshow('Window', img)
cv.setMouseCallback('Window', mouse_event)

cv.waitKey(0)
cv.destroyAllWindows()

"""
Explanation:
1. cv2.setMouseCallback(window_name, callback_function) -> Key Function

Callback Function Structure ->
def mouse_event(event, x, y, flags, param):
    pass

| event   | int  | Type of mouse event           |
| x       | int  | X-coordinate of mouse         |
| y       | int  | Y-coordinate of mouse         |
| flags   | int  | Modifier keys / button states |
| param   | any  | Extra user-defined data       |

Mouse Event Types (IMPORTANT)
| cv2.EVENT_MOUSEMOVE     | Mouse movement        |
| cv2.EVENT_LBUTTONDOWN   | Left button pressed   |
| cv2.EVENT_LBUTTONUP     | Left button released  |
| cv2.EVENT_RBUTTONDOWN   | Right button pressed  |
| cv2.EVENT_RBUTTONUP     | Right button released |
| cv2.EVENT_MBUTTONDOWN   | Middle button pressed |
| cv2.EVENT_LBUTTONDBLCLK | Left double click     |
| cv2.EVENT_RBUTTONDBLCLK | Right double click    |
"""

# drawing line between last two clicked points

# def mouse_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(img, (x, y), 5, (0, 255, 0), -1)
#         point.append((x, y))
#         if len(point) >= 2:
#             cv.line(img, point[-1], point[-2], (255, 0, 0), 2)
#         cv.imshow('Window', img)

# img = np.zeros((512, 512, 3), np.uint8)
# point = []
# cv.imshow('Window', img)
# cv.setMouseCallback('Window', mouse_event)

# cv.waitKey(0)
# cv.destroyAllWindows()

"""
BGR Channels -> In OpenCV, color images are stored in BGR format, not RGB.
| 0           | Blue  |
| 1           | Green |
| 2           | Red   |

blue = img[x, y, channel] -> This line gives channel(0,1,2) intensity at pixel (x, y).

Pixel Value Range:
0   → no intensity
255 → full intensity

(0, 0, 0) → Black
(255, 255, 255) → White
(255, 0, 0) → Blue
(0, 255, 0) → Green
(0, 0, 255) → Red
"""

# clicking at a point in one window will show the color at that point in anaother window

# def mouse_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         blue = img[x, y, 0]
#         green = img[x, y, 1]
#         red = img[x, y, 2]
#         cv.circle(img, (x, y), 15, (0, 255, 0), 2)
#         cv.imshow('Window', img)
#         colorimage = np.zeros((512, 512, 3), np.uint8)
#         colorimage[:] = [blue, green, red]
#         cv.imshow('color', colorimage)

# # img = np.zeros((512, 512, 3), np.uint8)
# img = cv.imread('lena.jpg')
# cv.imshow('Window', img)
# cv.setMouseCallback('Window', mouse_event)

# cv.waitKey(0)
# cv.destroyAllWindows()