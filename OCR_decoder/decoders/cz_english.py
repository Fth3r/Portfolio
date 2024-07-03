#! /usr/bin/python3

# Attempting to combine CZ cracker with English detector to find the actual message
# Since the Caesar cracker returns a list of 66 possible decoded strings, it is necessary
# to iterate through that list and look for the only entry that is in literate English

from detectEnglish import isEnglish
from caesar import decode_cz

if __name__ == "__main__":
    decoded = decode_cz('Wt114L1x991tL8!tt98')
    for entry in decoded:
        if isEnglish(entry):
            print(entry)
        else:
            pass