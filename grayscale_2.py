import cv2 as cv
import numpy as np



def saturated(value):
    if value>255:
        value = 255
    elif value<0:
        value = 0
    return value

print(cv.__version__)

sample = cv.imread('sample.jpg',cv.IMREAD_GRAYSCALE)

n = cv.mean(sample)
m = n[0]

print(m)
dst = np.empty(sample.shape,dtype=sample.dtype)
alpha = 2.0
for y in range(sample.shape[0]):
    for x in range(sample.shape[1]):
        dst[y,x] = saturated( sample[y,x] + (sample[y,x]-m)*alpha )






cv.imshow('sample',sample)
cv.waitKey()
cv.imshow('dst',dst)
cv.waitKey()

cv.imwrite('contrast.jpg',dst)
cv.destroyAllWindows()