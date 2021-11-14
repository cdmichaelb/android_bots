// Using opencv and PIL capture screenshots from a window 5 times per second then display them in real time

def main():
    import cv2
    import numpy as np
    import time
    import os
    from PIL import Image

    # Create a window to display the images
    cv2.namedWindow("Image")

    # Create a list of images to display
    images = []

    # Create a list of images to display
    for i in range(5):
        # Capture a screenshot
        os.system("adb shell screencap -p /sdcard/screenshot.png")

        # Pull the screenshot from the device
        os.system("adb pull /sdcard/screenshot.png")

        # Load the screenshot into a numpy array
        img = cv2.imread("screenshot.png")

        # Add the image to the list of images
        images.append(img)

    # Create a list of images to display
    for i in range(5):
        # Add the image to the list of images
        images.append(images[i])

    # Create a list of images to display
    for i in range(5):
        # Add the image to the list of images
        images.append(images[i])

    # Create a list of images to display
    for i in range(5):
        # Add the image to the list of images
        images.append(images[i])



import cv2
import numpy

def find_center(mask):
    _x = 0
    _y = 0
    points = cv2.findNonZero(mask)

    for point in points:
        pnt = str(point[0])[1:][:-1].split()
        _x += int(pnt[0])
        _y += int(pnt[1])
    
    return int(_x / len(points)), int(_y / len(points))

while(True):

    img = cv2.imread("test2.png")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = numpy.array([170, 120, 180])
    upper = numpy.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("mask", mask)

    points = cv2.findNonZero(mask)

    x, y = find_center(mask)

    cv2.imshow("final", img)

    _, _, w, h = cv2.getWindowImageRect("final")

    cv2.line(img, (int(w/2), int(h/2)), (x, y), (255, 0, 0), 5)

    cv2.imshow("final", img)

    if cv2.waitKey(0) == ord("q"):
        cv2.destroyAllWindows()
        break