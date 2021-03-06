#! /usr/bin/python3

#GUI script to compare two values, usually sha256 or md5 hashes

import tkinter as tk

# Modules
from file_enter import enter_from_file
from save import save_to_file
from help_me import help_me

## This section contains the main logic for the program ##

#function to define the comparison action on enter and button press
def compare(event=None):
    firstHash = str(ent_first.get())
    secondHash = str(ent_second.get())
    hashTitle = str(ent_title.get())

    if not firstHash:
        lbl_result["text"] = str("please enter something in First Hash")

    elif not secondHash:
        lbl_result["text"] = str("Please enter something in Second Hash")

    elif len(firstHash) != len(secondHash):
        lbl_result["text"] = str("These values area not the same length.")

    elif firstHash == secondHash:
        lbl_result["text"] = str("Looks like a match!")
        _list_update(hashTitle)
        _list_display()

        # Add the passed title and its values to the storage dictionary for saving
        dictSecret[hashTitle] = [firstHash, secondHash, "passed"]
        
    else: # This loops through each entry and shows where they differ
        _find_mismatches(firstHash, secondHash)

# Helper function to find and display any mismatched characters
def _find_mismatches(firstHash, secondHash):
    n = 0
    temp_list = []
    for i, j in zip(firstHash, secondHash):
        if i != j:
            temp_list.append(f"{i}:{j}")
            n += 1
    lbl_result["text"] = str(f"These didn't match; {temp_list}\nThere were {n} mismatches")

# Helper function to update the list with new passed titles
def _list_update(hashTitle):
    for i in range(3, -1, -1):
        listMain[i] = listMain[i - 1]
    listMain[0] = hashTitle + " passed"

# Helper function to display the new list and clear entry fields
def _list_display():
    lbl_list_3["text"] = listMain[3]
    lbl_list_2["text"] = listMain[2]
    lbl_list_1["text"] = listMain[1]
    lbl_list_0["text"] = listMain[0]
    ent_first.delete(0, "end")
    ent_second.delete(0, "end")
    ent_title.delete(0, "end")

## This section begins the GUI creation and layout ##

listMain = ["", "", "", ""]
dictSecret = {}

#creating and labeling the window, also making it fixed size
window = tk.Tk()
window.title("Hash Bash")
window.resizable(width=False, height=False)
window.iconphoto(True, tk.PhotoImage(file="Hash Bash\\Cloud.png"))

#creating and labeling the first entry field
frm_first = tk.Frame(master=window)
lbl_first = tk.Label(master=frm_first, text="First Hash")
ent_first = tk.Entry(master=frm_first, width=64)

#creating and labeling the second entry field
frm_second = tk.Frame(master=window)
lbl_second = tk.Label(master=frm_second, text="Second Hash")
ent_second = tk.Entry(master=frm_second, width=64)

#trying to make a heading or title for each comparison
frm_title = tk.Frame(master=window)
lbl_title = tk.Label(master=frm_title, text="Enter a Label")
ent_title = tk.Entry(master=frm_title, width=20)

#creating and labeling the memory side of the program
frm_memory = tk.Frame(master=window)
lbl_memory = tk.Label(master=frm_memory, text="Most Recent Hashes Passed")
lbl_list_0 = tk.Label(master=frm_memory, text="")
lbl_list_1 = tk.Label(master=frm_memory, text="")
lbl_list_2 = tk.Label(master=frm_memory, text="")
lbl_list_3 = tk.Label(master=frm_memory, text="")

#laying out the first, second, and title entry widgets with their labels
lbl_first.grid(row=0, column=0, sticky="w")
ent_first.grid(row=0, column=1, sticky="e")
lbl_second.grid(row=1, column=0, sticky="w")
ent_second.grid(row=1, column=1, sticky="e")
lbl_title.grid(row=3, column=1)
ent_title.grid(row=4, column=1)

#laying out the memory side
lbl_memory.grid(row=0, column=0)
lbl_list_0.grid(row=1, column=0)
lbl_list_1.grid(row=2, column=0)
lbl_list_2.grid(row=3, column=0)
lbl_list_3.grid(row=4, column=0)


#create and define the button that calls the compare() function
#and the label for the result. Also allows for the Enter key to
#call the function.
btn_compare = tk.Button(
    master=window,
    text="Click or Press Return to Compare",
    width=37,
    command=compare
)
window.bind('<Return>', compare)
lbl_result = tk.Label(master=window, text="No Result Yet")

# Create a help button and call the help_me() function
btn_help = tk.Button(
    master=window,
    text="Help",
    width=37,
    command=lambda: help_me(window)
)

# Create a button to call the enter_from_file() function
btn_enter = tk.Button(
    master=window, 
    text='Enter Values From a File',
    width=37,
    command=lambda: enter_from_file(ent_first, ent_second)
)

# Create a button to call the save_to_file() function
btn_save = tk.Button(
    master=window,
    text="Export Passed Comparisons",
    width=37,
    command=lambda: save_to_file(dictSecret)
)

#lay the frames out using .grid()
frm_title.grid(row=0, column=0)
frm_first.grid(row=1, column=0, padx=50)
frm_second.grid(row=2, column=0, pady=20)
lbl_result.grid(row=3, column=0, padx=50, pady=20, sticky="nsew")
btn_compare.grid(row=4, column=0, sticky="nw")
frm_memory.grid(row=0, column=1)
btn_enter.grid(row=5, column=0, sticky="sw")
btn_save.grid(row=4, column=0, sticky="ne")
btn_help.grid(row=5, column=0, sticky="se")

#run the program
window.mainloop()