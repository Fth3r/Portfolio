# Frequency analysis module for vigenere cipher

# Used in modified form from inventwithpython.com/cracking/chapter19.html

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def find_letter_count(message):
    letters = {
        "A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0
    }

    for l in message.upper():
        if l in LETTERS:
            letters[l] += 1

    return letters

def index_zero(items):

    return items[0]

def freq_order(message):
    letterToFreq = find_letter_count(message)

    freqToLetter = {}
    for l in LETTERS:
        if letterToFreq[l] not in freqToLetter:
            freqToLetter[letterToFreq[l]] = [l]
        else:
            freqToLetter[letterToFreq[l]].append(l)
    
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=index_zero, reverse=True)

    freqOrder = []
    for pair in freqPairs:
        freqOrder.append(pair[1])
    
    return ''.join(freqOrder)

def match_score(message):
    freqOrder = freq_order(message)

    matchScore = 0
    for l in ETAOIN[:6]:
        if l in freqOrder[:6]:
            matchScore += 1

    for ul in ETAOIN[-6:]:
        if ul in freqOrder[-6:]:
            matchScore += 1

    return matchScore
