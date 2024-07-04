# cv2 in OpenCV
import cv2
import numpy as np

from decoders.b64 import decode_b64
from decoders.atbash import find_atb

# pytesseract is used here to get a string from text in an image
from pytesseract import pytesseract as pt
# Need to tell pytesseract where the compiled tesseract binary is located
pt.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Assign dir of image to be read and pass to cv2.imread below
directory = ''

try:
   img = cv2.imread('D:\Coding\Repos\Portfolio\OCR_decoder\dependencies\\new_message.jpg')
except FileNotFoundError:
   # If the file is not found, print a clean message instead of error
   print("Couldn't find that file.")

# Trying to apply some preprocessing to the image
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1,1), dtype=np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.medianBlur(img, 3)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) [1]

# Create a window to show the image being read before proceeding
# Also wait for keypress to close
cv2.imshow("Photo", img)
k = cv2.waitKey(0)

# Leverage pytesseract and assign what it returns to the 'text' var, then print
text = pt.image_to_string(img)
#text = text.replace(" ", "")
text = text.strip()


print(text)

print(find_atb(text))