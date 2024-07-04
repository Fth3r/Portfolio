# playing with the GUI outline for OCR_Decoder 

import tkinter as tk
from PIL import ImageTk, Image

from decoders.atbash import find_atb

main = tk.Tk()
main.title("Project Ovaltine") # can't for the life of me remember why I called it this
main.geometry("750x500") # maybe we can set this value based on the image size
main.resizable(width=True, height=True)
main.iconphoto(True, tk.PhotoImage(file="dependencies\\cup.png",
                                    width=700,
                                    height=700
                                    ))

### This section is for the dropdown menu ###
methods = [
    "Base64",
    "Affine",
    "Atbash",
    "Caesar",
    "Vigenere",
]

### This section is for the image display ###
path = "D:\Coding\\repos\\portfolio\OCR_decoder\dependencies\\new_message.jpg"

canvas = tk.Canvas(main, width=1500, height=300)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(path))
canvas.create_image(200, 200, image=img)

display = tk.StringVar()
display.set(methods[0])

drop = tk.OptionMenu(main, display, *methods)
drop.pack()

### This section is for the decoding conditional logic ###
label2 = tk.Label(main, text="Enter Ciphertext")
ent = tk.Entry(main, width=50)
label2.pack()
ent.pack()

# Starting with just one cipher method for concept
def decode():
    cipher = ent.get()
    if display.get() == "Atbash":
        decoded = find_atb(cipher)
    else:
        decoded = f"{display.get()} not yet implemented"
    label3.config(text=decoded)

label3 = tk.Label(main, text="No value yet")
button2 = tk.Button(main, text="Decode", command=decode)
label3.pack()
button2.pack()

# Create the window and manage it
main.mainloop()