# Caesar Cipher Hacker
# frankbexxx

message = 'guv6Jv6Jz?J6rp5r7Jzr66ntrM'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        # Note: Only symbols in SYMBOLS string can be encrypet/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(key, " ", translated)


