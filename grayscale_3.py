import cv2 as cv
import numpy as np
import os



print(cv.__version__)
print(np.__version__)


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("camera oopen failed")
    exit()

fps = cap.get(cv.CAP_PROP_FPS)
f_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
f_width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
f_height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print("open success")

out = cv.VideoWriter("output.avi", cv.VideoWriter_fourcc(*"DIVX"), fps,(f_width,f_height),isColor=False)

while cap.isOpened():
    status,frame= cap.read()
    status2, frame2 = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    temp = cv.mean(gray)

    pastAve = temp[0]
    temp = cv.mean(gray2)
    curAve = temp[0]
    show = gray2
    print("fps",cap.get(cv.CAP_PROP_FPS))
    print("past",pastAve)
    print("cur",curAve)
    print("abs",pastAve - curAve)
    if abs(pastAve - curAve)>30:
        count = 0
        while cap.isOpened():
            st,fr =cap.read()
            gray3 = cv.cvtColor(fr, cv.COLOR_BGR2GRAY)
            flip = cv.flip(gray3,0)
            if st:
                cv.imshow('view', flip)
                out.write(flip)
                count = count + 1
                print("count",count)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            if count>90:
                break


    if status:
        cv.imshow('view',show)
        out.write(show)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

