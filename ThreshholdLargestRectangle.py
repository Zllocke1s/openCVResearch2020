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
        imgray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        #edges = cv.Canny(img,200,500)
        #gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
        #gray = np.float32(gray)
        #edged = cv.Canny(gray, 200, 500) 
        #contours, hierarchy = cv.findContours(edged,  
        #cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        font = cv.FONT_HERSHEY_SIMPLEX
        maxSize = 0
        maxIndex = 0
        cv.imshow("Threshhold", thresh)
        for i in range(len(contours)):
            cnt = contours[i]
            
            if(maxSize<cv.arcLength(cnt,True)):
                maxSize = cv.arcLength(cnt,True)
                maxIndex = i
        
        #x,y,w,h = cv.boundingRect(cnt)
        #cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
        print(maxIndex)
        if(contours):
            cv.drawContours(img2, contours, maxIndex, (0, 255, 0), 3)
            cnt = contours[maxIndex]
            rect = cv.minAreaRect(cnt)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(img2,[box],0,(0,0,255),2)
            #print(box)
            x1 = box[0][0]
            x2 = box[1][0]
            y1 = box[0][1]
            y2 = box[1][1]
            edgeLen = ((y2-y1)**2 + (x2-x1)**2)**.5
            cv.putText(img2, str(round(edgeLen, 2)) ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(0,0,255),2,cv.LINE_AA)
            
##        for i in range(len(contours)):
##            cnt = contours[i]
##            area = cv.arcLength(cnt,True)
##            print(i, ": ", area)
##            T = "test"
##            font = cv.FONT_HERSHEY_SIMPLEX
##            print(contours[i][0][0][0])
##            cv.putText(img2, str(round(area, 2)) ,(contours[i][0][0][0], contours[i][0][0][1]), font, .5,(0,0,255),2,cv.LINE_AA)
##    
        #cv.drawContours(img2, contours, -1, (0, 255, 0), 3)
        
        #cv.fillPoly(img2, pts =[contours], color=(255,0,255))                
        cv.imshow('dst',img2)
        ch = cv.waitKey(5)
        if ch == 27:
            break
            print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
