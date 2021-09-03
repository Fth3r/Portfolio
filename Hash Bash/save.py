# A module to save the contents of the inbuilt dict to a .json file

from tkinter.filedialog import asksaveasfile as asaf
import json

def save_to_file(dict1):
    filetypes = [("JSON", "*.json")]
    saved = asaf(filetypes=filetypes,
                defaultextension=filetypes)
    
    saved.write(_prepare_json(dict1))

def _prepare_json(dict1):
    return json.dumps(dict1,
                    indent=4,
                    separators=(", ", ": "),
                    sort_keys=True)