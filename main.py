import cv2
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode
import math
import time
import imutils
from imutils import perspective
from imutils import contours
from math import atan2, pi
import multiple_qr as multi # after I import multiple qr just starts working for no reason

# error when loading PyZbar
# https://github.com/NaturalHistoryMuseum/pyzbar
# fixed by installing C++ 2013
# code referenced: https://github.com/pruthvi03/Barcode-And-Qrcode-Scanner/blob/main/scanner.py

# decoder func
def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr = decode(gray_img)
    CVdecoder = cv2.QRCodeDetector()
    CVdata, CVpoints, _ = CVdecoder.detectAndDecode(gray_img)

   # if loc is not None:
        #print('Decoded data: ' + data)

    for obj in qr:
        if CVpoints is not None:
            # print('Decoded data: ' + data)
            points = CVpoints[0]

            # separate coordinate data into 4 different points
            pt1 = [int(val) for val in points[0]]
            pt2 = [int(val) for val in points[1]]
            pt3 = [int(val) for val in points[2]]
            pt4 = [int(val) for val in points[3]]
            # use pt1 and pt2 to find the slope, arctan to find the angle
            slope = ((pt1[1] - pt2[1]) / (pt1[0] - pt2[0]))
            angle = np.arctan(slope) * 180 / np.pi
            x = int(pt1[0])
            y = int(pt1[1])
            print("top left corner location is x = ",  pt1[0] , " y = ",  pt1[1])
            print('Decoded data: ' + CVdata)
            print(angle)
        points = obj.polygon
        # box the qr
        (x, y, w, h) = obj.rect
        pt = np.array(points, np.int32)
        pt = pt.reshape((-1, 1, 2))
        cv2.polylines(image, [pt], True, (128, 0, 128), 2)

        # find dimension and place of qr code in picture
        # ref point top left corner
        #left = str(qr[0].rect[0])
        #top = str(qr[0].rect[1])
        #width = str(qr[0].rect[2])
        #height = str(qr[0].rect[3])
        # dim = gray_img.shape
        # add size = {dim} in print to display camera pixel size
        #location = str(f' left = {left}, top = {top}, width = {width}, height = {height}')
        # Sophia's laptop camera size: 480*640 pixel

        qr_data = obj.data.decode("utf-8")
        qr_read = str(qr_data)
        # display box and qr info on the screen, print qr read and location data
        # QR data above QR code, location below QR code
        cv2.putText(frame, qr_read, (x, y), cv2.QT_FONT_NORMAL, 0.3, (255, 255, 255), 1)
        #cv2.putText(frame, location, (x, y+h+1), cv2.QT_FONT_NORMAL, 0.3, (255, 255, 255), 1)
        #print("QR Reads:" + qr_data)
        #print(f' left = {left}, top = {top}, width = {width}, height = {height}')


# OpenCV code to turn on live camera
cap = cv2.VideoCapture(0)

# main
while True:
    ret, frame = cap.read()
    #time.sleep(2)
    # cv2.line(img=frame, pt1=(10, 10), pt2=(100, 10), color=(255, 0, 0), thickness=5, lineType=8, shift=0)
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    # quit by entering q on keyboard
    if code == ord('q'):
        break
