
import cv2 
import numpy as np 
  
# Let's load a simple image with 3 black squares 
image = cv2.imread(('images/test2.jpg') )
cv2.waitKey(0) 
cv2.imwrite("image_copy.png", image)   
# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# Find Canny edges 
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
          
#cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (255, 0, 0), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow("Threshold", thresh)
cv2.imwrite("Threshold.png", thresh)
cv2.imwrite("contours.png", image)
maxSize = 0
maxIndex = 0
for i in range(len(contours)):
    cnt = contours[i]
            
    if(maxSize<cv2.arcLength(cnt,True)):
        maxSize = cv2.arcLength(cnt,True)
        maxIndex = i
if(contours):    
    cnt = contours[maxIndex]
    #x,y,w,h = cv.boundingRect(cnt)
    #cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(image,[box],0,(0,0,255),2)
    #print(box)
    x1 = box[0][0]
    x2 = box[1][0]
    y1 = box[0][1]
    y2 = box[1][1]
    edgeLen = ((y2-y1)**2 + (x2-x1)**2)**.5
    cv2.putText(image, str(round(edgeLen, 2)) ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(255,240,255),2,cv2.LINE_AA)


    x1 = box[1][0]
    x2 = box[2][0]
    y1 = box[1][1]
    y2 = box[2][1]
    edgeLen = ((y2-y1)**2 + (x2-x1)**2)**.5
    cv2.putText(image, str(round(edgeLen, 2)) ,(int((x2+x1)/2), int((y2+y1)/2)), font, .5,(255,240,255),2,cv2.LINE_AA)
    
##for i in range(len(contours)):
##    cnt = contours[i]
##    area = cv2.contourArea(cnt)
##    print(i, ": ", area)
##    epsilon = 0.1*cv2.arcLength(cnt,True)
##    cv2.drawContours(image, contours, i, (0, 255, 0), 3)
##    cv2.imshow('Contours', image)
##    cv2.waitKey(0) 


#cv2.fillPoly(image, pts =[contours], color=(255,255,255))
cv2.imshow('Contours', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
