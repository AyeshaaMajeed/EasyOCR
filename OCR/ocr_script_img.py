# Install pytorch (if not installed)
# https://pytorch.org/get-started/locally/

# Install required libraries (if not installed)

import easyocr
import cv2
import numpy as np

# Load and saving the image
IMAGE_PATH = 'imgg.png'
OUTPUT_IMAGE_PATH = 'output.png'  

reader = easyocr.Reader(['en'])  

result = reader.readtext(IMAGE_PATH)
img = cv2.imread(IMAGE_PATH)

font = cv2.FONT_HERSHEY_SIMPLEX

if result:
    print("\n Extracted Text:\n")
    
    for detection in result:
        top_left = tuple(map(int, detection[0][0]))  
        bottom_right = tuple(map(int, detection[0][2]))
        text = detection[1]

        print(text) 

        # Draw bounding box around text
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

        # Put detected text on image
        img = cv2.putText(img, text, (top_left[0], top_left[1] - 10), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imwrite(OUTPUT_IMAGE_PATH, img)
    print(f"\n Processed image saved as: {OUTPUT_IMAGE_PATH}")

else:
    print("\n No text detected. Try improving image quality or preprocessing.")
