#!/usr/bin/env python

'''
This sample demonstrates Canny edge detection.

Usage:
  edge.py [<video source>]

  Trackbars control edge thresholds.

'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2 as cv
import numpy as np

# relative module
import video

# built-in module
import sys


def main():
    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cap = video.create_capture(fn)
    while True:
        _flag, img2 = cap.read()
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) 
        #edges = cv.Canny(img,200,500)
        #gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
        #gray = np.float32(gray)
        edged = cv.Canny(gray, 200, 500) 
        contours, hierarchy = cv.findContours(edged,  
        cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv.contourArea(cnt)
            print(i, ": ", area)  
        cv.drawContours(img2, contours, -1, (0, 255, 0), 3)
        cv.imshow('dst',img2)
        ch = cv.waitKey(5)
        if ch == 27:
            break
            print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
