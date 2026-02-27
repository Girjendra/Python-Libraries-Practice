import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 1.
# img = np.zeros((200, 200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
# cv.imshow('Window', img)

# 2.
# img = cv.imread('lena.jpg', 1)
# b, g, r = cv.split(img)
# cv.imshow('Window', img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# plt.hist(img.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

# 3.
img = cv.imread('lena.jpg', 0)
hist = cv.calcHist([img], [0], None, [255], [0, 255],)
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
"""
Explanation:
Image Histogram : An image histogram is a graphical representation showing the distribution of
                  pixel intensity values in an image, used to analyze brightness, contrast, and
                  intensity characteristics.
It shows:
X-axis → Pixel intensity values (0-255)
Y-axis → Number of pixels (frequency)
📌 Helps us understand brightness, contrast, and intensity distribution of an image.
🔹 Types of Image Histograms
1️⃣ Grayscale Histogram
    Single channel:Pixel range: 0-255
2️⃣ Color Histogram
    Multiple channels:Blue, Green, Red

Histogram Components (Table)
| Component | Description                  |
| Bins      | Intensity values (0-255)     |
| Frequency | Number of pixels in each bin |
| Peak      | High frequency intensity     |
| Spread    | Contrast level               |

Histogram Interpretation
| Histogram Shape | Meaning       |
| Left skewed     | Dark image    |
| Right skewed    | Bright image  |
| Narrow spread   | Low contrast  |
| Wide spread     | High contrast |

1. hist = cv2.calcHist([img], [0], None, [256], [0,256])
| Parameter | Meaning                 |
|  [img]    | Source image            |
|  [0]      | Channel (0 = grayscale) |
|  None     | No mask                 |
|  [256]    | Number of bins          |
|  [0,256]  | Pixel range             |

Histogram Equalization : A technique to improve contrast by spreading intensity values evenly.
Before:
    Low contrast
    Pixels concentrated in small range
After:
    Better contrast
    Uniform distribution
2. equalized = cv2.equalizeHist(gray_img)
"""