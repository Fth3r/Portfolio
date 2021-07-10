This simple GUI program does the work of comparing two values from user-entered text and
storing the titles for the 4 most recent passed comparisons in a list, displaying them for the user.

While this would be fairly straightforward to do in the command line, using a GUI format gives 
the opportunity to present a more feature-rich user experience at the cost of reduced streamlining.

If the compared values don't match, HashBash will display to the user the mismatches indices and their values.

Possible features to add:
    - Using len() to compare length before comparing indices.
        # This will stop HashBash from returning all indices after an added or subtracted character as mismatched.
    - Functionality to open and read hash values stored in files rather in addition to entered text.
        # Explore whether this should be done as a popup window/filepath entry field that autofills the value
        # or as a native ability of the original entry field (checkbox or conditional logic-driven).
    - Ability to save and output the passed comparisons as a file (JSON?)
        # Even though HashBash only displays the title of the passed comparisons, adding the ability to save the
        # values associated with those titles in a dictionary would be easy.
    - Create a "HELP" button.
        # This would open a popup dialog window explaining the features of the program to save space in the window. 