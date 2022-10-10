import cv2 as cv
import numpy as np



#0~255범위를 넘어가는 값을 제한함
def saturated(value):
    if value>255:
        value = 255
    elif value<0:
        value = 0
    return value
#opencv, numpy 버전 확인
print(cv.__version__)
print(np.__version__)

#샘플 이미지를 불러옴
sample = cv.imread('sample.jpg',cv.IMREAD_GRAYSCALE)

#영상의 평균 밝기를 구해 ave에 저장함
temp = cv.mean(sample)
ave = temp[0]

#새로 저장할 영상을 저장할 공간을 생성, shape나 type은 sample이미지에서 가져옴
dst = np.empty(sample.shape,dtype=sample.dtype)

#평균 밝기를 기준값으로, 명암비를 조정,계수는 2를 사용
alpha = 2.0
for y in range(sample.shape[0]):
    for x in range(sample.shape[1]):
        dst[y,x] = saturated( sample[y,x] + (sample[y,x]-ave)*alpha )

#샘플 이미지와 결과 이미지를 창을 띄워 확인
cv.imshow('sample',sample)
cv.imshow('dst',dst)
cv.waitKey()
#영상 저장, 경로는 파이썬 파일이 있는 디렉토리에 저장함
cv.imwrite('contrast.jpg',dst)
#열려있는 모든 창을 닫음
cv.destroyAllWindows()