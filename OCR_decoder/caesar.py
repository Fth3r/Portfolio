#! /usr/bin/python3

# a module to encode or decode the caesar cipher

from detectEnglish import isEnglish

uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = uppers + uppers.lower() + '1234567890 !?.'

def encode_cz(message):
    key = input('What key would you like to use? (input 1-66): ')

    translated = ''

    for i in message:
        if i in symbols:
            index = symbols.find(i)
            translatedIndex = index + int(key)

            # Handle wrap
            if translatedIndex >= len(symbols):
                translatedIndex = translatedIndex - len(symbols)
            
            translated = translated + symbols[translatedIndex]
        else:
            translated = translated + i

    return translated

def decode_cz(message):
    attempts = []
    results = []
    for key in range(len(symbols)):
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

    for attempt in attempts:
        if isEnglish(attempt):
            results.append(attempt)
        else:
            pass
    print(results)
    return results

