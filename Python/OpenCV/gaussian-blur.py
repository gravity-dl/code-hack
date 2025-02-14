import cv2
import numpy as np

image = cv2.imread('image.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian', Gaussian)
cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median', median)
cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
