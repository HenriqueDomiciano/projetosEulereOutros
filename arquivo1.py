import matplotlib.pyplot as plt
import numpy as np
import cv2 
img= cv2.imread ("im1.jpg",1)
# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 

# showthe plotting graph of an image 
plt.plot(histr) 
plt.show() 
