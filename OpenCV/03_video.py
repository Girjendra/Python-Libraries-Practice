import cv2 as cv

"""
1. VideoCapture() can take: returns Ture if vidoe is opned successfully else False
File path → "video.mp4"
Camera index → 0 (webcam), 1 → External camera
"""

# Read frames from video
# cap = cv.VideoCapture("ex1.mp4")
# while cap.isOpened(): # or True
#     ret, frame = cap.read()

#     if not ret:
#         break
    
#     cv.imshow("Video", frame)
    
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
"""
Eaplanation:
ret : True if frams read successfully
frame : One image from the video
20 : delay between showing frames
"""

# Accessing Webcam
# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()

#     if not ret :
#         break
    
#     cv.imshow("Video", frame)

#     if cv.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()


# Save the video from webcam
# cap = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*'XVID') # or ('X', 'V', 'I', 'D'),  it must be matched with video formate
# out = cv.VideoWriter('recorded.avi', fourcc, 20.0, (640, 480))
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break
    
#     out.write(frame) # Adding the frame in video

#     cv.imshow("Video", frame) # Showing the video

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv.destroyAllWindows()
"""
Explanation:
| "output.avi" | Output file name              |
| fourcc       | to compress frames            |
| 20.0         | FPS                           |
| (640, 480)   | Frame size                    |
"""

# Capturing Frames (Save Images from Video)
# cap = cv.VideoCapture(0)
# count = 0
# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break
    
#     cv.imshow("Video", frame)

#     key = cv.waitKey(1) & 0xFF
#     if key == ord('s'):
#         cv.imwrite(f"image_{count+1}.jpg", frame)
#         print("Saved frame", count)
#         count += 1
#     elif key == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()

# Important VideoCapture Properties
cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv.CAP_PROP_FPS))

    cv.imshow("Video", frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()