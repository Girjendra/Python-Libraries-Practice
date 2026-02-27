import cv2 as cv
import datetime as dt

cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    date = str(dt.datetime.now())
    font = cv.FONT_HERSHEY_DUPLEX
    frame = cv.putText(frame, date, (10, 30), font, 1, (0, 255, 57), 2)
    cv.imshow("Window", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break;
cap.release()
cv.d

"""
Explanation:
datetime Module:
1. now = dt.datetime.now() -> Get Current Date & Time
2. today = dt.date.today() -> Get today's date
3. current_time = dt.datetime.now().time() -> Current Time
"""