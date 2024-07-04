#! /usr/bin/python3

# a module to encode or decode the caesar cipher

from decoders.detectEnglish import isEnglish

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = uppers + uppers.lower() + '1234567890 !?.'

def encode_cz(message):
    # For this set of symbols, there are 66 possible keys
    key = input('What key would you like to use? (input 1-66): ')

    translated = ''

    # Loop through each character in message and compare it to symbols
    for i in message:
        if i in symbols:
            # find the new index based on the key and exchange
            index = symbols.find(i)
            translatedIndex = index + int(key)

            # Handle wrap
            if translatedIndex >= len(symbols):
                translatedIndex = translatedIndex - len(symbols)
            
            translated = translated + symbols[translatedIndex]
        else:
            # If the character isn't in symbols it's carried forward intact
            translated = translated + i

    return translated

def decode_cz(message):
    attempts = []
    results = []
    
    # The same process as encoding, but for all 66 possible keys
    for key in range(len(symbols)):
        # translated is reset to '' on every iteration
        translated = ''

        for i in message:
            if i in symbols:
                index = symbols.find(i)
                translatedIndex = index - key

                # Handle wrap
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(symbols)
                
                translated = translated + symbols[translatedIndex]
            else:
                translated = translated + i
        attempts.append(translated)

    # Check if each 'decoded' string is legible English
    # If it is, append it to the results list
    for attempt in attempts:
        if isEnglish(attempt):
            results.append(attempt)
        else:
            pass

    # If there are more than 1 solutions returned, run each through
    # another round of isEnglish with higher requirements
    while len(results) > 1:
        for solution in results:
            if not isEnglish(solution, wordPercent=75):
                results.remove(solution)

    return results[0]
