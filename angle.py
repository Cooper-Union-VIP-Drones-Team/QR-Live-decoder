import cv2
import numpy as np

# read image
img = cv2.imread('3.png')

# decode and import data
decoder = cv2.QRCodeDetector()
data, points, _ = decoder.detectAndDecode(img)


if points is not None:
    print('Decoded data: ' + data)
    points = points[0]

    # separate coordinate data into 4 different points
    pt1 = [int(val) for val in points[0]]
    pt2 = [int(val) for val in points[1]]
    pt3 = [int(val) for val in points[2]]
    pt4 = [int(val) for val in points[3]]
    # use pt1 and pt2 to find the slope, arctan to find the angle
    slope = ((pt1[1]-pt2[1])/(pt1[0]-pt2[0]))
    angle = np.arctan(slope)*180/np.pi
    print(angle)
    # use to mark pt1 and pt2
    # cv2.putText(img,'1', (pt1[0],pt1[1]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 0), 1)
    # cv2.putText(img,'2', (pt2[0],pt2[1]),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 0), 1)

    #show image
    cv2.imshow('Detected QR code', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()