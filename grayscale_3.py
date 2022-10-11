import cv2 as cv
import numpy as np

#opencv , numpy 버전 확인
print(cv.__version__)
print(np.__version__)

#카메라 활성화, 만약 여는데 실패할 시 실패 메시지와 함께 프로그램 종료
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("camera open failed")
    exit()
#영상이 열리면, 영상의 속성들을 불러 온 후 오픈 완료 메시지 출력
fps = cap.get(cv.CAP_PROP_FPS)
f_width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
f_height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print("open success")
#영상 프레임을 저장할 공간을 만듬
out = cv.VideoWriter("output.avi", cv.VideoWriter_fourcc(*"DIVX"), fps,(f_width,f_height),isColor=False)

#사용자가 키 입력을 할 떄 까지 영상을 촬영
while cap.isOpened():
    #프레임 비교를 위해 연속된 두 프레임을 불러옴
    status,frame= cap.read()
    status2,frame2 = cap.read()
    #불러온 영상을 그레이스케일로 변환
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)

    #두 영상의 평균 밝기를 구함
    temp = cv.mean(gray)
    pastAve = temp[0]
    temp = cv.mean(gray2)
    curAve = temp[0]
    #평균 밝기가 30 이상 차이날시 , 상하반전,흑백반전 된 영상으로 3초간 변환
    if abs(pastAve - curAve)>30:
        #프레임을 카운트 하기 위한 변수
        count = 0
        while cap.isOpened():
            #반전된 그레이스케일 영상 생성
            st,frame3 =cap.read()
            gray3 = cv.cvtColor(frame3, cv.COLOR_BGR2GRAY)
            flip_frame = cv.flip(gray3,0)
            inverted_frame = np.invert(flip_frame)
            if st:
                cv.imshow('view', inverted_frame)
                #영상 프레임 기록
                out.write(inverted_frame)
                #프레임 카운트
                count = count + 1
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            if count>3*fps:
                #3초가 지나면 다시 원본 영상으로 변환
                break

    if status:
        cv.imshow('view',gray2)
        #영상 프레임 기록
        out.write(gray2)
    if cv.waitKey(1) & 0xFF == ord('q'):
        #q를 입력시 영상 촬영을 종료
        break
#영상 사용 종료
cap.release()
#모든 창을 닫음
cv.destroyAllWindows()

