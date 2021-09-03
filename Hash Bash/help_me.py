# A module to handle the help window popup

import tkinter as tk

def help_me(window):
    """This module generates a popup window on top of the Tkinter master
        window in order to display information about the various features."""

    t = tk.Toplevel(window) # tk.Toplevel creates a popup window
    t.geometry("500x200")

    lbl_help = tk.Label(master=t, text=
    "This program is useful for comparing two values.\n"
    "Some preliminary comparisons are made on the two entries before\n"
    "they are iterated to verify that they exist and are the same length.\n\n"
    "To enter values from a file, separate the two values on separate lines\n"
    "with only two values in the file. The 'enter from a file' button will input them.\n\n"
    "All passed comparisons will be saved behind the scenes regardless of falling\n"
    "off the display list. Click the export button and pick a location/filename\n"
    "to save the passed values in a .json file. As yet no other filetypes are available.\n\n"
    "There will be more features coming, and help_me will be updated accordingly."
    )
    lbl_help.pack()