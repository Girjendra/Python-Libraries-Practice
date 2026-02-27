import cv2 as cv
import numpy as np

"""
A Trackbar in OpenCV is a GUI slider used to change values dynamically while a program is running.
| cv.createTrackbar() | Create trackbar        |
| cv.getTrackbarPos() | Get current value      |
| Callback function   | Runs when slider moves |

1. cv.createTrackbar(trackbarname, winname, value, max_value, callback)
🧠 Trackbar Callback Rule
Callback function must exist
Even if unused, write:
2. cv.namedWindow(winname) -> creates a window
3. getTrackbarPos(trackbarname, winname)
"""

# def nothing(x):
#     print(x)
# cv.namedWindow('Window')
# cv.createTrackbar('B', 'Window', 0, 255, nothing)
# cv.createTrackbar('G', 'Window', 0, 255, nothing)
# cv.createTrackbar('R', 'Window', 0, 255, nothing)
# cv.createTrackbar('ON/OFF', 'Window', 0, 1, nothing)
# img = np.zeros((512, 512, 3), np.uint8)

# while True:
#     cv.imshow('Window', img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
    
#     b = cv.getTrackbarPos('B', 'Window')
#     g = cv.getTrackbarPos('G', 'Window')
#     r = cv.getTrackbarPos('R', 'Window')
#     s = cv.getTrackbarPos('ON/OFF', 'Window')
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]
# cv.destroyAllWindows()



def nothing(x):
    print(x)
cv.namedWindow('Window')
cv.createTrackbar('CP', 'Window', 10, 400, nothing)
switch = 'color/gray'
cv.createTrackbar(switch, 'Window', 0, 1, nothing)

while True:
    img = cv.imread('lena.jpg')

    pos = cv.getTrackbarPos('CP', 'Window')
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(img, str(pos), (50, 150), font, 4, (0, 255, 255), 5)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    s = cv.getTrackbarPos(switch, 'Window')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Window', img)

cv.destroyAllWindows()