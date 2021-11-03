import cv2
import keyboard
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode
import math
import time
import imutils
from imutils import perspective
from imutils import contours
from math import atan2, pi
import multiple_qr as multi
data1 = []
dataList = []
def decoder(image):
    n = 2
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    CVdecoder = cv2.QRCodeDetector()
    CVdata, CVpoints, _ = CVdecoder.detectAndDecode(gray_img)
    qr = decode(gray_img)
    # print(CVpoints)
    if CVdata != ' ':
        if CVpoints is not None:
            # for i in range(10):
            # print(data1[0])
            points = CVpoints[0]

            # Coordinate system of 4 corner and rotation
            # separate coordinate data into 4 different points
            pt1 = [int(val) for val in points[0]]
            pt2 = [int(val) for val in points[1]]
            pt3 = [int(val) for val in points[2]]
            pt4 = [int(val) for val in points[3]]

            # use pt1 and pt2 to find the slope, arctan to find the angle
            if pt1[0] == pt2[0]:
                angle = 90
            else:
                slope = ((pt1[1] - pt2[1]) / (pt1[0] - pt2[0]))
                angle = np.arctan(slope) * 180 / np.pi
            x = int(pt1[0])
            y = int(pt1[1])

            str0 = str(CVdata)
            if str0 != "":
                str1 = str0.split()
                data1.append(str1)
                print(str0)
                print(str1)
                print(data1[len(data1) - 1])
                print(len(data1))
            for word in data1:
                if word not in dataList:
                    dataList.append(word)
            print(len(dataList))
           # i += 1
    # if keyboard.is_pressed('1'):
            # print(data1[1])
                # print(data1[len(data1)-2])

    # if keyboard.is_pressed('2'):
    #    print(data1[1])
    # if keyboard.is_pressed('3'):
    #    print(data1[2])


# OpenCV code to turn on live camera
cap = cv2.VideoCapture(0)

# main
while True:
    ret, frame = cap.read()
    # time.sleep(2)
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    # quit by entering q on keyboard
    if code == ord('q'):
        break