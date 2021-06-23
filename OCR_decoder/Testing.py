# cv2 is OpenCV
import cv2 as cv
import os
import sys

# Defining a directory in which to save the image and what to name the image
# Also assigning the webcam capture variable
directory = r'C:\Users\jbeck\Documents\coding\images'
filename = 'new_image.jpg'
vid = cv.VideoCapture(0)

# A simple help menu message as a reminder of which keys do what
message = 'Press any key to take another frame.\nHold any key to continuously take frames (like video).\nPress "q" to quit. Press "s" to save the current frame.\nPress "h" to repeat this message!'
print(message)

# Starting the main loop of the program and the webcam
while True:
    ret, frame = vid.read()

    # Showing the captured image and assigning it to the 'img' variable
    # Telling opencv to wait for keypress to proceed ('k' varibale)
    img = cv.imshow('Frame', frame)
    k = cv.waitKey(0)

    # A simple series of checks to do different tasks if either the 'q', 's', or 'h' keys are pressed. No else statement is needed, as 'k' var handles all other keypresses.

    if k & 0xFF == ord('q'): # if the hex value of keypress and 0xFF match 'q'
        break
    elif k & 0xFF == ord('s'): 
        try:
            os.chdir(directory)     # Change to whatever dir is defined above
        except:
            print("Sorry, couldn't find that directory.")
            sys.exit()
        cv.imwrite(filename, frame) # Save image as filename in current dir
        break
    elif k & 0xFF == ord('h'):
        print(message)

# Once the loop is broken, stop using the webcam and close all windows created
vid.release()
cv.destroyAllWindows()

# Later, after the program uses the image, it should be deleted.
os.chdir(directory)
os.remove(filename)