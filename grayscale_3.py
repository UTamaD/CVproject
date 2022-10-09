import cv2 as cv
import numpy as np



print(cv.__version__)

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("camera oopen failed")
    exit()


