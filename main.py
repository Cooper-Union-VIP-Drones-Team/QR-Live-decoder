import cv2
import numpy as np
from pyzbar.pyzbar import decode
#error when loading pyzbar
#https://github.com/NaturalHistoryMuseum/pyzbar
#fixed by installing C++ 2013
#code referenced: https://github.com/pruthvi03/Barcode-And-Qrcode-Scanner/blob/main/scanner.py

#decoder func
def decoder(image):
    qr = decode(image)
    for obj in qr:
        points = obj.polygon
        #box the qr
        (x, y, w, h) = obj.rect
        pt = np.array(points, np.int32)
        pt = pt.reshape((-1, 1, 2))
        cv2.polylines(image, [pt], True, (128,0,128), 2)

        qrData = obj.data.decode("utf-8")
        string = str(qrData)

        cv2.putText(frame, string, (x, y), cv2.QT_FONT_NORMAL, 0.7, (255, 255, 255), 1)
        print("QR Reads:" + qrData)

#OpenCV code to turn on live camera
cap = cv2.VideoCapture(0)
#main
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break