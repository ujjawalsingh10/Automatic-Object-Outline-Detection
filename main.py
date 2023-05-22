import cv2 as cv
import numpy as np
from rembg import remove
from PIL import Image

INPUT_IMAGE = r'Cropped Image.jpg'
OUTPUT_IMAGE = 'rembg.jpg'
ORIGINAL_IMAGE = r'TEST IMAGES\1.jpg'

#Read the image
img = cv.imread(ORIGINAL_IMAGE)
img = cv.resize(img, (1024, 720))

## Selecting the ROI
r = cv.selectROI("Select the area", img)

#Cropping the image
cropped_image = img[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]

## Saving the cropped image
cv.imwrite("Cropped Image.jpg", cropped_image)

##Reading the cropped image
input = Image.open(INPUT_IMAGE)

##Using the rembg to remove background
output = remove(input)
output = output.convert('RGB')

## Saving the image without background
output.save(OUTPUT_IMAGE)

##### Contouring
##Read the iamge
image = cv.imread(OUTPUT_IMAGE)

# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv.Canny(gray,30, 950)

##Detect and draw contours
contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(image, contours, -1, (0, 255, 0), 2)

##Displaying the image
disp_img = cv.imread(OUTPUT_IMAGE)
cv.imshow('Cropped Image', image)

cv.waitKey(0)