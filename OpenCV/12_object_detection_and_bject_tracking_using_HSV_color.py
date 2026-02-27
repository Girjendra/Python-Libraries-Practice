import cv2 as cv
import numpy as np

"""
Explanation:
Object Detection (Color-based) -> Object detection using HSV color means identifying objects in an image or video based on their color range, not shape or AI.
Object Tracking -> Object tracking means detecting the object in every frame and following its movement over time.
Mask -> a mask is a binary image used to isolate a specific Region of Interest (ROI) in another image.
HSV :
| Channel        | Meaning      |
| H (Hue)        | Color type   |
| S (Saturation) | Color purity |
| V (Value)      | Brightness   |

1. lower_blue = np.array([110, 50, 50]) -> Define HSV Color Range
   upper_blue = np.array([130, 255, 255])

The HSV (Hue, Saturation, Value) range defines colors, typically with
Hue (H) from 0-179 (or 0-360°), Saturation (S) 0-255 (purity/intensity),
and Value (V) 0-255 (brightness)

2. mask = cv.inRange(hsv, lower_blue, upper_blue) -> Create Mask
Mask meaning:
| Pixel         | Value       |
| Inside range  | 255 (white) |
| Outside range | 0 (black)   |
"""
# while True:
#     frame = cv.imread('smarties.png')

#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     l_b = np.array([110, 50, 50])
#     u_b = np.array([130, 255, 255])

#     mask = cv.inRange(hsv, l_b, u_b)

#     res = cv.bitwise_and(frame, frame, mask=mask)

#     cv.imshow('frame', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('res', res)
    
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cv.destroyAllWindows()



# def nothing(x):
#     pass

# cv.namedWindow('Window')
# cv.createTrackbar('LH', 'Window', 0, 255, nothing)
# cv.createTrackbar('LS', 'Window', 0, 255, nothing)
# cv.createTrackbar('LV', 'Window', 0, 255, nothing)
# cv.createTrackbar('UH', 'Window', 0, 255, nothing)
# cv.createTrackbar('US', 'Window', 255, 255, nothing)
# cv.createTrackbar('UV', 'Window', 255, 255, nothing)

# while True:
#     frame = cv.imread('smarties.png')

#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     l_h = cv.getTrackbarPos('LH', 'Window')
#     l_s = cv.getTrackbarPos('LS', 'Window')
#     l_v = cv.getTrackbarPos('LV', 'Window')

#     u_h = cv.getTrackbarPos('UH', 'Window')
#     u_s = cv.getTrackbarPos('US', 'Window')
#     u_v = cv.getTrackbarPos('UV', 'Window')

#     l_blue = np.array([l_h, l_s, l_v])
#     u_blue = np.array([u_h, u_s, u_v])

#     mask = cv.inRange(hsv, l_blue, u_blue)

#     res = cv.bitwise_and(frame, frame, mask=mask)

#     cv.imshow('frame', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('res', res)
    
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cv.destroyAllWindows()



# def nothing(x):
#     pass
# cap = cv.VideoCapture(0)
# cv.namedWindow('Window')
# cv.createTrackbar('LH', 'Window', 0, 255, nothing)
# cv.createTrackbar('LS', 'Window', 0, 255, nothing)
# cv.createTrackbar('LV', 'Window', 0, 255, nothing)
# cv.createTrackbar('UH', 'Window', 0, 255, nothing)
# cv.createTrackbar('US', 'Window', 255, 255, nothing)
# cv.createTrackbar('UV', 'Window', 255, 255, nothing)

# while True:
#     _,frame = cap.read()

#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     l_h = cv.getTrackbarPos('LH', 'Window')
#     l_s = cv.getTrackbarPos('LS', 'Window')
#     l_v = cv.getTrackbarPos('LV', 'Window')

#     u_h = cv.getTrackbarPos('UH', 'Window')
#     u_s = cv.getTrackbarPos('US', 'Window')
#     u_v = cv.getTrackbarPos('UV', 'Window')

#     l_blue = np.array([l_h, l_s, l_v])
#     u_blue = np.array([u_h, u_s, u_v])

#     mask = cv.inRange(hsv, l_blue, u_blue)

#     res = cv.bitwise_and(frame, frame, mask=mask)

#     cv.imshow('frame', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('res', res)
    
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()




# Extra

# cap = cv.VideoCapture(0)
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#     mask = cv.inRange(hsv, lower_blue, upper_blue)

#     kernel = np.ones((5, 5), np.uint8)
#     mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
#     mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)

#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     for cnt in contours:
#         if cv.contourArea(cnt) > 500:
#             x, y, w, h = cv.boundingRect(cnt)
#             cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

#     cv.imshow("Frame", frame)
#     cv.imshow("Mask", mask)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
"""
Eplanation:
Contours -> Contours are continuous curves (boundaries) that join all the points
            along the edge of an object having the same intensity.

kernel -> is a small matrix of numbers used to perform operations on an image,
          such as blurring, sharpening, or edge detection. 

3. mask = cv.morphologyEx(src, operation, kernel) -> A general OpenCV function used to apply morphological operations
src->Input image
     Usually a binary image
     Can be grayscale
Type of morphological operation:
| Operation         | Meaning                         |
| cv.MORPH_DILATE   | Dilation                        |
| cv.MORPH_ERODE    | Erosion                         |
| cv.MORPH_OPEN     | Erosion → Dilation              |
| cv.MORPH_CLOSE    | Dilation → Erosion              |

contours, hierarchy = cv2.findContours(image, mode, method) -> detects the boundaries (outlines) of objects in a binary image.
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
"""