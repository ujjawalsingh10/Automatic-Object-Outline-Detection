import cv2 
import numpy as np

path = r'rembg.jpg'
ORIGINAL_IMAGE = r'TEST IMAGES\1.jpg'

image = cv2.imread(path)
og_image = cv2.imread(ORIGINAL_IMAGE)
og_image = cv2.resize(og_image, (1024, 720))

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv2.Canny(gray,30, 900)

contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.drawContours(og_image, contours, -1, (0, 255, 0), 2)
cv2.drawContours()
cv2.imshow("image", image)
cv2.imshow("original image", og_image)
cv2.waitKey(0)