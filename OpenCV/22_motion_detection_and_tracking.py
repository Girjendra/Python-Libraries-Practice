import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:
    absdiff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(absdiff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(thresh, None, iterations=2)
    contours, _ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 900:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, "Status : Movement", (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv.imshow("Motion Detection", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    if cv.waitKey(40) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
"""
Explanation:
Motion Detection:Motion detection is the process of identifying moving objects in a video by comparing frames over time.
🔄 Video → Frame1, Frame2
        ↓
Frame Difference
        ↓
Thresholding
        ↓
Morphology (noise removal)
        ↓
Find Contours
        ↓
Draw Bounding Boxes
"""