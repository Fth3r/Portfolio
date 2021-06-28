# A module to encode or decode the Affine Cipher, decoding doesn't require knowledge of the key beforehand. 

from pycipher import affine
from detectEnglish import isEnglish

def encode_aff(message):

    a,b = input('Choose two keys (a b) separated by a space: ').split(' ')
    try:
        en = affine.Affine(int(a), int(b)).encipher(message, keep_punct=True)
    except AssertionError:
        print("'a' must be an odd number between 1 and 25, but not 13...")
        exit()
        
    return en

def decode_aff(message):
    possible_solutions = []
    a_list = [n for n in range(1, 27) if n%2 != 0 and n != 13]
    for j in a_list:
        for i in range(0, 26):
            de = affine.Affine(j,i).decipher(message, keep_punct=True)
            if isEnglish(de):
                possible_solutions.append(de)
            else:
                pass

    if len(possible_solutions) > 1:
        for solution in possible_solutions:
            if not isEnglish(solution, wordPercent=75):
                del possible_solutions[solution]

    return possible_solutions

