import cv2
import numpy as np
from pyzbar.pyzbar import decode


# import math
# error when loading PyZbar
# https://github.com/NaturalHistoryMuseum/pyzbar
# fixed by installing C++ 2013
# code referenced: https://github.com/pruthvi03/Barcode-And-Qrcode-Scanner/blob/main/scanner.py

# decoder func
def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    qr = decode(gray_img)
    for obj in qr:

        points = obj.polygon
        # box the qr
        (x, y, w, h) = obj.rect
        pt = np.array(points, np.int32)
        pt = pt.reshape((-1, 1, 2))
        cv2.polylines(image, [pt], True, (128, 0, 128), 2)

        # find dimension and place of qr code in picture
        # ref point top left corner
        left = str(qr[0].rect[0])
        top = str(qr[0].rect[1])
        width = str(qr[0].rect[2])
        height = str(qr[0].rect[3])
        # dim = gray_img.shape
        # add size = {dim} in print to display camera pixel size
        location = str(f' left = {left}, top = {top}, width = {width}, height = {height}')
        # Sophia's laptop camera size: 480*640 pixel
        
        qr_data = obj.data.decode("utf-8")
        string = str(qr_data)
        # display box and qr info on the screen, print qr read and location data
        # QR data above QR code, location below QR code
        cv2.putText(frame, string, (x, y), cv2.QT_FONT_NORMAL, 0.7, (255, 255, 255), 1)
        cv2.putText(frame, location, (x, y+h), cv2.QT_FONT_NORMAL, 0.5, (255, 255, 255), 1)
        print("QR Reads:" + qr_data)
        print(f' left = {left}, top = {top}, width = {width}, height = {height}')

        # test for multi qr (not working right now)
        # qr = cv2.QRCodeDetector()
        # retval, decoded_info, points, straight_qrcode = qr.detectAndDecodeMulti(np.hstack([gray_img, gray_img]))
        # print("multiple:", retval)  # False

# OpenCV code to turn on live camera
cap = cv2.VideoCapture(0)

# main
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    # quit by entering q on keyboard
    if code == ord('q'):
        break
