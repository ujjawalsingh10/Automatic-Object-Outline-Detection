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

cv.imshow('cropped image', cropped_image)

coord = [int(r[1]),int(r[1]+r[3]), 
                      int(r[0]),int(r[0]+r[2])]
print("Coordinates", coord)

cv.waitKey(0)