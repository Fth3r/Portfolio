#! /usr/bin/python3

# A module to encode or decode the Atbash cipher


alph = 'abcdefghijklmnopqrstuvwxyz'
alph_rev = alph[::-1]

def find_atb(message):
    temp = []
    for l in message.lower():
        if l in alph:
            index = alph.find(l)
            temp.append(alph_rev[index])
        else:
            temp += l
    final = ''.join(temp)
    return final
