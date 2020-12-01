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


try:
    fn = sys.argv[1]
except:
    fn = 0

def nothing(*arg):
    pass


try:
    loc = input("File Location: ")
except SyntaxError:
    loc = None
unitcalibrate = 0
summation = 0
totalContours = 0
img2 = cv.imread("images/test3.jpg")
gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) 
#edges = cv.Canny(img,200,500)
#gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#gray = np.float32(gray)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh,  
cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
font = cv.FONT_HERSHEY_SIMPLEX
maxSize = 0
vidWait = 0
maxIndex = 0
totalEdgeLen = 0
totalEdges = 0
val = len(contours)
cv.drawContours(thresh,contours,-1,(0,0,255),4)
cv.drawContours(thresh,contours,-1,(255,0,0),2)
resizeCon = cv.resize(thresh, (1260, 760))
cv.imshow("contours", resizeCon)
print("Contours Found: " + str(val))
try:
    x=input('Edge Known? ')
except SyntaxError:
    x = None
if x=="Y":
    unitcalibrate = eval(input("Scale: "))
    largestSize = eval(input("Largest Size: "))
    smallestSize = eval(input("Smallest Size: "))
       
for j in range(0, 500, 1):
    
    #print(j)
    #x,y,w,h = cv.boundingRect(cnt)
    #cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    #print(maxIndex)
#    print("Total Contours" + str(len(contours)))
    maxSize = 0
    maxIndex = 0
    for i in range(len(contours)):
        cnt = contours[i]
        
        if(maxSize<cv.arcLength(cnt,True)):
            maxSize = cv.arcLength(cnt,True)
            maxIndex = i
    if(contours):
        
        cv.drawContours(img2, contours, maxIndex, (0, 255, 0), 3)
        
        cnt = contours[maxIndex]
        #print(cnt)
#        print("Length of Contour " + str(maxIndex) + ": " + str(cv.arcLength(cnt, False)))
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
        if unitcalibrate==0:
            cv.putText(img2, (str(round(edgeLen, 2)) + " px") ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(0,0,0),4,cv.LINE_AA)            
            cv.putText(img2, (str(round(edgeLen, 2)) + " px") ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(255,255,255),2,cv.LINE_AA)
            totalEdgeLen = totalEdgeLen + edgeLen
            totalEdges = totalEdges + 1
        else:
            cv.putText(img2, (str(round(edgeLen*unitcalibrate, 2)) + " u") ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(0,0,255),2,cv.LINE_AA)                
            if(smallestSize <= (edgeLen*unitcalibrate) and largestSize >= (edgeLen*unitcalibrate)):
                summation = summation + (edgeLen*unitcalibrate)
                totalContours = totalContours + 1
            else:
                print ("Contour too big; omitted.")
    #        for i in range(len(contours)):
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
    img2s = cv.resize(img2, (1260, 760))                    # Resize image
    contours.pop(maxIndex)
    cv.imshow('dst',img2s)
    if vidWait == 0:
        cv.waitKey(0)
        vidWait = 1
    ch = cv.waitKey(5)
    if ch == 27:
        print('Done')
    
    cv.waitKey(30)     
print("Average Edge Length: " + str(round(totalEdgeLen/totalEdges, 2)))
cv.imwrite('Labeled.png', img2) 
