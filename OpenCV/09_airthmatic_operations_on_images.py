import cv2 as cv
import numpy as np

# img = cv.imread('messi5.jpg')
# print(img.shape) # (342, 548, 3)
# print(img.size)  # 562248
# print(img.dtype) # uint8
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# cv.imwrite('messi2.jpg', img)
# cv.imshow("Window", img)
# b, g, r = cv.split(img)
# cv.imshow("bw", b)
# cv.imshow("gw", g)
# cv.imshow("rw", r)
# merged = cv.merge([b, g, r])
# cv.imshow("Merged Image", merged)
# cv.waitKey(0)
# cv.destroyAllWindows()
"""
1. b, g, r = cv2.split(img) -> Splits a multi-channel image (BGR/RGB) into individual single-channel images.
Each b, g and r output is a grayscale image showing intensity of that color.

2. merged = cv2.merge([b, g, r]) -> Combines multiple single-channel images into one multi-channel image.
"""

# img1 = cv.imread('messi5.jpg')
# img1 = cv.resize(img1, (512, 512))
# img2 = cv.imread('lena.jpg')
# img2 = cv.resize(img2, (512, 512))

# added = cv.add(img1, img2)
# cv.imshow("added Image", added)
# weightedadded = cv.addWeighted(img1, 0.9, img2, 0.3, 0)
# cv.imshow("weighted added Image", weightedadded)
# sub = cv.subtract(img1, img2)
# cv.imshow("subtracted Image", sub)
# mul = cv.multiply(img1, img2)
# cv.imshow("multiplied Image", mul)
# div = cv.divide(img1, img2)
# cv.imshow("divided Image", div)

# cv.waitKey(0)
# cv.destroyAllWindows()
"""
Explanation:
3. added = cv2.add(src1, src2) -> Adds two images pixel-by-pixel with saturation
4. weightedadded = cv2.addWeighted(img1, alpha, img2, beta, gamma) -> Blends two images using weights (used for transparency).
result = α·img1 + β·img2 + γ
5. sub = cv2.subtract(src1, src2) -> Subtracts pixel values with no negative values.
6. mul = cv2.multiply(src1, src2) -> Multiplies pixel values
7. div = cv2.divide(src1, src2) -> Divides pixel values safely.
"""