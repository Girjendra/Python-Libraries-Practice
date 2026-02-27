import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('road.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.resize(img, (1000, 1100))
print(img.shape)

height = img.shape[0]
width = img.shape[1]

ROI_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]
def ROI(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)

    return masked_image


cropped_image = ROI(img, np.array([ROI_vertices], np.int32),)

plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()