import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
high_kernel = np.ones((45,45), np.uint8)
frame = cv2.imread('img.png')
genislik = 640
yukseklik = 480

cap = cv2.VideoCapture(0)

lower_color = np.array([0, 100, 20])
upper_color= np.array([10, 255, 255])
    
while True:
  _, frame = cap.read()

  blur = cv2.GaussianBlur(frame, (11, 11), 0) 

  hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

  mask = cv2.inRange(hsv, lower_color, upper_color)
  mask = cv2.erode(mask, None, iterations=10)
  mask = cv2.dilate(mask, None, iterations=3)
  merkezX = None
  merkezY = None
  largest_contour = None
  merkez = None
  
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  if len(contours) > 0:
      largest_contour = max(contours, key=cv2.contourArea)
      ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
      if radius > 1:
          M = cv2.moments(largest_contour)
          merkezX = int(M["m10"] / M["m00"])
          merkezY = int(M["m01"] / M["m00"])
          cv2.circle(frame, (merkezX, merkezY), 5, (255, 255, 255), -1)
          merkez = (merkezX, merkezY)
          
  cv2.imshow("mask", mask)
  cv2.imshow("frame", frame)
  if cv2.waitKey(5) & 0xFF == ord("q"):
      break
