import cv2 as cv
# Shape of image
# 1. print(img.shape) -> (Height(rows), Width(columns), Color channels(BGR))
img = cv.imread('lena.jpg', -1)
print(img.shape)
img = cv.imread('lena.jpg', 0)
print(img.shape)
img = cv.imread('lena.jpg', 1)
print(img.shape)

# Resize the image
# 2. cv2.resize(image, (width, height))
resized = cv.resize(img, (500, 300))
cv.imshow('window1', resized)

# Crop the image -> Cropping uses NumPy slicing
# 3. image[y1:y2, x1:x2]
crop = img[100:500, 100:600]
cv.imshow('window2', crop)



weight = cv.waitKey(4000)
cv.destroyAllWindows()