#! /usr/bin/python3

# A module to encode or decode the Atbash cipher

from pycipher import atbash

"""
This was me trying to encode this cipher by hand rather than use a library
alph = 'abcdefghijklmnopqrstuvwxyz'
alph_rev = alph[::-1]

def find_atb(message):
    temp = []
    for l in message.upper():
        if l in alph.upper():
            index = alph.find(l)
            temp.append(alph_rev[index])
        else:
            temp += l
    final = ''.join(temp)
    print(final)
    return final

find_atb('This is a message')"""
# index isn't finding the substring, returning -1 for every index

def find_atb(message):
    de = atbash.Atbash().decipher(message, keep_punct=True)

    return de