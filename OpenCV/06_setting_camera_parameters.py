import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 680)
cap.set(4, 500)

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    cv.imshow("Window", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

"""
Set Camera Parameters
cap.set(property_name, value) or cap.set(3, 640)  works, but NOT recommended
| Frame height  | cv2.CAP_PROP_FRAME_HEIGHT  | Height of video frame        | 480         |
| Frame width   | cv2.CAP_PROP_FRAME_WIDTH   | Width of video frame         | 640         |
| FPS           | cv2.CAP_PROP_FPS           | Frames per second            | 30          |
| Brightness    | cv2.CAP_PROP_BRIGHTNESS    | Image brightness             | 0.5         |
| Contrast      | cv2.CAP_PROP_CONTRAST      | Image contrast               | 0.5         |
| Saturation    | cv2.CAP_PROP_SATURATION    | Color saturation             | 0.5         |
"""