ciphertext = 'Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu.'
shift = 1

def caesar_cipher_encript(text, shift):
    result = ''

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result



decripted = caesar_cipher_encript(ciphertext, shift)

print('ciphered text is:', ciphertext)
print('decripted etxt is: ', decripted)