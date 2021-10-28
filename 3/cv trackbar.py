#opencv trackbar practise

import cv2
import numpy as np


def passFunction(x):
    pass

windowName = "OpenCV BGR Color Palette"
imageData = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow(windowName)

cv2.createTrackbar('Blue', windowName, 0, 255, passFunction)
cv2.createTrackbar('Green', windowName, 0, 255, passFunction)
cv2.createTrackbar('Red', windowName, 0, 255, passFunction)

while (True):
    cv2.imshow(windowName, imageData)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    blue = cv2.getTrackbarPos('Blue', windowName)
    green = cv2.getTrackbarPos('Green', windowName)
    red = cv2.getTrackbarPos('Red', windowName)

    imageData[:] = [blue, green, red]
    print(blue, green, red)

    cv2.waitKey(10000)

cv2.destroyWindow(windowName)