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
        #edges = cv.Canny(img,200,500)
        gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
        dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
        img2[dst>0.01*dst.max()]=[255,0,255]
        cv.imshow('dst',img2)
        ch = cv.waitKey(5)
        if ch == 27:
            break
            print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
