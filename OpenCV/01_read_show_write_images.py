import cv2 as cv

"""
1. cv2.imread(filename, flags) -> Reads an image from a file and loads it into a NumPy array 
Returns None if the image is not found
| Flag                 | Value       | Meaning                                |
| cv2.IMREAD_COLOR     | 1 (default) | Load image in color (BGR)              |
| cv2.IMREAD_GRAYSCALE | 0           | Load image in grayscale                |
| cv2.IMREAD_UNCHANGED | -1          | Load image with alpha channel as it is |

2. cv2.imshow(window_name, image) -> Displays an image in a window.
window_name-> Name of the window (string)
image	   -> Image array (from imread)

3. cv2.waitKey(delay) -> Waits for a window to close for delay mili seconds
| 0    | Wait indefinitely until key is pressed |
| 1    | Wait 1 ms (used in video)              |
| 1000 | Wait 1 second                          |
Returns the ASCII code of the pressed key

4. cv2.destroyAllWindows() -> Closes all OpenCV windows that were opened.
5. cv2.destroyWindow("Image") -> Closes only a specific window
"""
# Image reading and displaying
img = cv.imread('lena.jpg', 0)
cv.imshow('first_window', img)
weight = cv.waitKey(0)
cv.destroyAllWindows()

"""
6. cv2.imwrite("output.jpg", image, params) -> Saves an image (NumPy array) to a file on disk.
Returns True if Image saved successfully else False
params (optional):
    Type: list
    Controls image quality and compression
    Format: [parameter, value]
"""
# Saving an image
cv.imwrite("low_copy.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 0])
cv.imwrite("high_copy.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 100])

if weight == 27:
    cv.destroyAllWindows()
elif weight == ord('s'):
    cv.imwrite("temp_copy.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 100])