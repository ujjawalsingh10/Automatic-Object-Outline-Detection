import cv2 as cv
import numpy as np
from rembg import remove
from PIL import Image

INPUT_IMAGE = r'Cropped Image.jpg'
OUTPUT_IMAGE = 'rembg.jpg'

#Read the image
img = cv.imread(r'TEST IMAGES\1.jpg')
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

##Displaying the image
disp_img = cv.imread(OUTPUT_IMAGE)
cv.imshow('Cropped Image', disp_img)

cv.waitKey(0)