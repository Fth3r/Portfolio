# cv2 in OpenCV
import cv2
import numpy as np

# pytesseract is used here to get a string from text in an image
from pytesseract import pytesseract as pt

def getTessOutput(image_dir):
   """
   DEPRECATED
   """

   # Need to tell pytesseract where the compiled tesseract binary is located
   pt.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

   img = cv2.imread(image_dir)

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
   cv2.imshow("Cipher Text Render - press any key to continue", img)
   k = cv2.waitKey(0)
   if k:
      cv2.destroyAllWindows()

   # Leverage pytesseract and assign what it returns to the 'text' var, then print
   text = pt.image_to_string(img)
   #text = text.replace(" ", "")
   text = text.strip()

   print(text)


getTessOutput("D:\Coding\\repos\Portfolio\OCR_decoder\dependencies\\new_message.jpg")