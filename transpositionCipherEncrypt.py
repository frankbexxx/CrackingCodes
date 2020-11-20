# Transposition Cipher Encryption
# frankbexxx

import pyperclip


def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    """
    Print the encrypted string in ciphertext to the screen, with a | ("pipe" character)
    after it in case there are spaces at the end of the encrypted message:
    """
    print(ciphertext + '|')

    # copy the encrypted string in ciphertext to clipboard:
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column


        # keep looping until currentIndex goes past the message lenght:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key

    return ''.join(ciphertext)


# If transpositionChipherEncrypt.py is running, instead of imported as a module, call the main() function:
if __name__ == '__main__':
    main()




