# A module to enter values from a file

from tkinter.filedialog import askopenfile as aof

def enter_from_file(ent_first, ent_second):
    f = aof(mode='r',
            filetypes=[('CSV', '*.csv'), 
            ('JSON', '*.json'),
            ('Text', "*.txt"),
            ('All File Types', '*.*')])
    if f is not None:
        content = f.readlines()
        ent_first.insert(index=1, string=content[0].strip())
        ent_second.insert(index=1, string=content[1])
