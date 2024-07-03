# A module to encode or decode the Affine Cipher, decoding doesn't require knowledge of the key beforehand. 

from pycipher import affine
from detectEnglish import isEnglish

def encode_aff(message):

    # assigning both keys we will use to encipher
    a,b = input('Choose two keys (a b) separated by a space: ').split(' ')
    # If the user enters an invalid key, handle it instead of showing the error
    try:
        en = affine.Affine(int(a), int(b)).encipher(message, keep_punct=True)
    except AssertionError:
        print("'a' must be an odd number between 1 and 25, but not 13...")
        exit()
        
    return en

def decode_aff(message):
    possible_solutions = []
    # the key 'a' can't be even or 13, so we leave those out
    for j in [n for n in range(1, 27) if n%2 != 0 and n != 13]:
        # 'b' can be anything up to 25
        for i in range(0, 26):
            # Looping to brute force every possible key for affine
            de = affine.Affine(j,i).decipher(message, keep_punct=True)
            # Compare the results to see if it contains english words
            if isEnglish(de):
                possible_solutions.append(de)
            else:
                pass

    # If there are more than 1 solutions returned, run each through
    # another round of isEnglish with higher requirements
    if len(possible_solutions) > 1:
        for solution in possible_solutions:
            if not isEnglish(solution, wordPercent=75):
                possible_solutions.remove(solution)

    return possible_solutions

