# Caesar Cipher
# frankbexxx

import pyperclip

# The string to be encrypted/decrypted:
message = 'This is my secret message.'
# massagem = 'guv6Jv6Jz?J6rp5r7Jzr66ntrM'

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = 'encrypt'  # set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
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

print(translated)
pyperclip.copy(translated)
