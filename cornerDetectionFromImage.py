import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
fig = plt.figure()
fig.patch.set_facecolor('xkcd:black')

fn = 'leav.jpg'
img = cv.imread(fn)
edges = cv.Canny(img,200,500)
plt.subplot(111),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv.imwrite("savedEdges.png", edges) 
#plt.show()

img2 = cv.imread("savedEdges.png")
gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img2[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('dst',img2)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()


#im = Image.open("savedEdges.png", 'r')

