# Caesar Cipher
# frankbexxx

import pyperclip

# The string to be encrypted/decrypted:
message = 'guv6Jv6Jz?J6rp5r7Jzr66ntrM'
mess1 = 'Kv?uqwpfu?rncwukdng?gpqwijB'
mess2 = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

# The encryption/decryption key:
key = 0

# Whether the program encrypts or decrypts:
mode = 'decrypt'  # set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790 !?.'

# Store the encrypted/decrypted form of the message:

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in mess1:
        # Note: Only symbols in SYMBOLS string can be encrypet/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wraparound, if needed
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(key, " ", translated)