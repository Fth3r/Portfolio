#! /usr/bin/python3

# A module to detect English in a string
# Used in a modified form from inventwithpython.com/cracking/chapter11.html


UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Characters = UPPERS + UPPERS.lower() + ' \t\n'

# Uncomment from Windows
#dirpath = 'C:\\Users\\Jake\\Documents\\Repos\\Portfolio\\OCR_decoder\\dependencies\\dictionary.txt'
# Uncomment for Linux
dirpath = '/mnt/c/Users/Jake/Documents/Repos/Portfolio/OCR_decoder/denpendencies/dictionary.txt'

def _read_dictionary():
    dictFile = open(dirpath)
    words = {}

    for word in dictFile.read().split('\n'):
        words[word] = None
    dictFile.close()
    return words

englishWords = _read_dictionary()

def _get_word_count(message):
    message = _remove_non_letters(message)
    message = message.upper()
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in englishWords:
            matches += 1
    return float(matches) / len(possibleWords)

def _remove_non_letters(message):
    lettersOnly = []
    for sym in message:
        if sym in Characters:
            lettersOnly.append(sym)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercent=50):
    wordMatch = _get_word_count(message) * 100 >= wordPercent
    #numLetters = len(_remove_non_letters(message))
    #messageLettersPercent = float(numLetters) / len(message) * 100
    #lettersMatch = messageLettersPercent >= letterPercent
    return wordMatch #and lettersMatch

