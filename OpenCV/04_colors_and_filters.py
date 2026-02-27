import cv2 as cv

# 1. BGR vs RGB -> OpenCV loads images in BGR order, and Matplotlib in RGB order.
# img = cv.imread("lena.jpg")
# RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("BGR_Window", img)
# cv.imshow("RGB_Window", RGB)
# cv.imshow("Gray_Window", gray)


"""
Blurring (Image Smoothing) -> smooths images by averaging pixel values.

2. cv2.GaussianBlur(src, ksize, sigmaX, sigmaY=0) -> Uses a Gaussian distribution
| src     | Input image                                                |
| ksize   | Kernel size (width, height) (both odd, bigger more blur)    |
| sigmaX  | Standard deviation in X direction                          |
| sigmaY  | Standard deviation in Y (optional)                         |

3. cv2.blur(src, ksize) -> Replaces each pixel with the average of neighboring pixels.
Kernel size ex. (5, 5)

4. cv2.medianBlur(src, ksize) -> Replaces each pixel with the median value of neighbors.
Kernel size(single odd number) 5
"""
img = cv.imread("lena.jpg")
gaussian = cv.GaussianBlur(img, (5, 5), 0) 
average = cv.blur(img, (5, 5))
median = cv.medianBlur(img, 5)
cv.imshow("gaussian Window", gaussian)
cv.imshow("average Window", average)
cv.imshow("median Window", median)


cv.waitKey(0)
cv.destroyAllWindows()