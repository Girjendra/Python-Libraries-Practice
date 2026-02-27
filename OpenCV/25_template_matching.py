import cv2 as cv
import numpy as np

img = cv.imread('messi5.jpg')
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('messi_face.jpg', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(imggray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 2)
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
"""
Explanation:
1. result = cv.matchTemplate(image, template, method) -> It returns a 2D result matrix containing matching scores.
What happens here ?
    The template slides over the image
    At each position, a similarity score is calculated
    Output res is a 2D matrix of match scores
(result_rows, result_cols) =
(image_rows - template_rows + 1,
 image_cols - template_cols + 1)

| Method                      | Constant              | Meaning                             | Best Match        |
|   Squared Difference        |  cv.TM_SQDIFF         | Difference between image & template |   Minimum value   |
|   Normalized SqDiff         |  cv.TM_SQDIFF_NORMED  | Normalized squared difference       |   Minimum value   |
|   Cross Correlation         |  cv.TM_CCORR          | Measures similarity                 |   Maximum value   |
|   Normalized CCORR          |  cv.TM_CCORR_NORMED   | Normalized correlation              |   Maximum value   |
|   Correlation Coefficient   |  cv.TM_CCOEFF         | Correlation minus mean              |   Maximum value   |
|   Normalized CCOEFF         |  cv.TM_CCOEFF_NORMED  | Best & most stable method           |   Maximum value   |

2. loc = np.where(res >= threshold) -> This finds all locations where matching score ≥ 0.95. These positions are very strong matches
🧠 Meaning of loc
    loc[0] → row indices (y-coordinates)
    loc[1] → column indices (x-coordinates)
ex. (array([34, 35]), array([120, 121]))

loc[::-1] → swaps (rows, cols) → (x, y)
* → unpacks
zip() → creates coordinate pairs

🧠 Full Code Logic (One Flow)
    Read main image
    Convert to grayscale
    Read template
    Slide template over image
    Get match score matrix
    Find positions where match ≥ threshold
    Draw rectangles on matches
"""