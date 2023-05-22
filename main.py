import cv2 as cv
import numpy as np
from rembg import remove
from PIL import Image

INPUT_IMAGE = r'Cropped Image.jpg'
OUTPUT_IMAGE = 'rembg.jpg'
# ORIGINAL_IMAGE = r'TEST IMAGES\1.jpg'
ORIGINAL_IMAGE = r'TEST IMAGES\2.jpg'

#Read the image
img = cv.imread(ORIGINAL_IMAGE)
img = cv.resize(img, (1024, 720))

## Selecting the ROI
r = cv.selectROI("Select the area", img)

### coordinates of r
x, y, w, h = r

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

## converting the image to RGBA 
#image = cv.cvtColor(image, cv.COLOR_BGR2RGBA)

# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
## Gaussian blur
gray = imgBlur = cv.GaussianBlur(gray, (5,5), 1)
  
# Find Canny edges
edged = cv.Canny(gray,30, 400)

##Detect and draw contours
contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(image, contours, -1, (0, 255, 0), 2)

## Empty image array
empty_image = np.zeros_like(img)
empty_image = cv.resize(empty_image, (1024, 720))

#Imposing the image
without_bg = cv.imread(OUTPUT_IMAGE)
empty_image[y:y+h, x:x+w] = image
# result = cv.addWeighted(img, 0.3, empty_image, 0.5, 0)
result = cv.addWeighted(img, 0.6, empty_image, 0.3, 0)

##Displaying the image
cv.imshow('Cropped Image', result)

cv.waitKey(0)