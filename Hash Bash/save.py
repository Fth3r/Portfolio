# A module to save the contents of the inbuilt dict to a .json file

from tkinter.filedialog import asksaveasfile as asaf
import json

def save_to_file(dict1):
    """This module takes a dict as input and creates a Tkinter dialog to save
        the json formatted data in a .json output file."""

    filetypes = [("JSON", "*.json")]
    saved = asaf(filetypes=filetypes,
                defaultextension=filetypes,
                initialdir="'Hash Bash'\\saved_files")
    
    # Using a try block to handle a user pressing cancel instead of saving
    # This way no error message is generated in that case
    try:
        saved.write(_prepare_json(dict1))
    
    except AttributeError:
        pass

def _prepare_json(dict1):
    return json.dumps(dict1, # json.dumps returns a formatted string as json data
                    indent=4,
                    separators=(", ", ": "),
                    sort_keys=True)