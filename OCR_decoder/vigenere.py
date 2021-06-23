from pycipher import Vigenere

def encipher(message):
    key = input("Please enter a key word: ")

    en = Vigenere(key).encipher(message)

    return en

def decipher_with_key(message):
    key = input("Please enter the keyword used to encipher: ")

    de = Vigenere(key).decipher(message)

    return de

#def decipher_without_key(message):

enciphered = encipher('A secret message')
print(decipher_with_key(enciphered))