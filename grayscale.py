import cv2 as cv
import numpy as np

#입력값 value가 m보다 작을시 0으로 만드는 함수, 영상의 평균 밝기 이하의 값을 0으로 변환함
def AverageUnderZero(value,m):
    if value<m:
        value = 0
    return value
#opencv, numpy 버전 확인
print(cv.__version__)
print(np.__version__)

#영상을 그레이스케일로 불러옴
sample = cv.imread('sample.jpg',cv.IMREAD_GRAYSCALE)


#영상의 평균 밝기를 구해 ave에 저장함
temp = cv.mean(sample)
ave = temp[0]

#새로 저장할 영상을 저장할 공간을 생성, shape나 type은 sample이미지에서 가져옴
dst = np.empty(sample.shape,dtype=sample.dtype)


#영상의 픽셀들을 검사하여, 평균 밝기 이하인 값들을 0으로 치환함
for y in range(sample.shape[0]):
    for x in range(sample.shape[1]):
        dst[y,x] = AverageUnderZero(sample[y,x],ave)



#샘플 이미지와 결과 이미지를 창을 띄워 확인
cv.imshow('sample',sample)
cv.imshow('dst',dst)
cv.waitKey()
#영상 저장, 경로는 파이썬 파일이 있는 디렉토리에 저장함
cv.imwrite('output.jpg',dst)
#열린 모든창을 닫음
cv.destroyAllWindows()
