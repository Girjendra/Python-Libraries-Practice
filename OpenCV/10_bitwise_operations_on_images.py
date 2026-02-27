import cv2 as cv
import numpy as np

img1 = np.zeros((500, 500, 3), np.uint8)
cv.rectangle(img1, (200, 0), (300, 150), (255, 255, 255), -1)
img2 = np.zeros((500, 500, 3), np.uint8)
img2[:, 250:] = (255, 255, 255)

And = cv.bitwise_and(img1, img2)
cv.imshow("And Image", And)
Not = cv.bitwise_not(img1)
cv.imshow("Not Image", Not)
Or = cv.bitwise_or(img1, img2)
cv.imshow("Or Image", Or)
Xor = cv.bitwise_xor(img1, img2)
cv.imshow("Xor Image", Xor)

cv.waitKey(0)
cv.destroyAllWindows()

"""
8. And = cv2.bitwise_and(img1, img2)
9. Or = cv2.bitwise_or(img1, img2)
10. Xor = cv2.bitwise_xor(img1, img2)
11. Not = cv2.bitwise_not(img)
"""