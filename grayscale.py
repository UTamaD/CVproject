import cv2 as cv
import numpy as np

def AverageUnderZero(value,m):
    if value<m:
        value = 0
    return value

print(cv.__version__)

sample = cv.imread('sample.jpg',cv.IMREAD_GRAYSCALE)

temp = cv.mean(sample)
ave = temp[0]

print(ave)

dst = np.empty(sample.shape,dtype=sample.dtype)

for y in range(sample.shape[0]):
    for x in range(sample.shape[1]):
        dst[y,x] = AverageUnderZero(sample[y,x],ave)




cv.imshow('sample',sample)
cv.waitKey()
cv.imshow('dst',dst)
cv.waitKey()

cv.imwrite('output.jpg',dst)
cv.destroyAllWindows()
