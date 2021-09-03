# A module to enter values from a file

from tkinter.filedialog import askopenfile as aof

def enter_from_file(ent_first, ent_second):
    """This module takes the 2 Tkinter entry variables as input, generates a popup
        file explorer dialog to choose a file to use in data entry, and 
        inserts the first two lines of the chosen file into the entry fields."""

    f = aof(mode='r',
            filetypes=[('CSV', '*.csv'), 
            ('JSON', '*.json'),
            ('Text', "*.txt"),
            ('All File Types', '*.*')])
    if f is not None:
        content = f.readlines()
        ent_first.insert(index=1, string=content[0].strip())
        ent_second.insert(index=1, string=content[1])
