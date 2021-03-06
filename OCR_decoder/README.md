The idea for this project came while I was reading Kevin Mitnick's book "Ghost in the Wires." At the beginning of every chapter, he includes a phrase that is encoded in any of various cipher methods. Rather than typing each ciphertext message into prewritten decoders, I would rather take a picture of the text and have it decoded for me automatically. 

I decided to use OpenCV in conjunction with Tesseract to get a string from the text in a picture, then pass that string to a function which determines its cipher method and then decodes it using the relevant method. Finally, I will develop a GUI to contain the program, likely using PyQt5 or TKinter. 

For the time being, there will be periodic updates as I work through breaking each cipher I plan to include as well as eventually program logic to recognize cipher methods from a ciphertext sample.

For the final iteration of this project I would love to implement and train AI to recognize the cipher method instead of hardcoding it into the program. 