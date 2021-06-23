from pycipher import Vigenere

def encipher(message):
    key = input("Please enter a key word: ")

    en = Vigenere(key).encipher(message)

    print(en)
    return en

def decipher(message):


encipher('This is my super secret message that I dont want anyone to see')