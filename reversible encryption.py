#  function that makes the encryption
def encryptor():
    print('enter the text that will be encrypted')
    gonnabeencrypted = input()
    # takes input and turns it to ASCII
    asciitobeencrypted = [ord(c) for c in gonnabeencrypted]
    # multiply the ASCII result with 3
    encrypted = [i * 3 for i in asciitobeencrypted]
    encryptedmessage = [chr(encrypted[i]) for i in range(0, len(encrypted))]
    print('encrypted message:')
    print(''.join(encryptedmessage))
    path()

# function that makes the decryption
def decryptor():
    # Decrypt part
    print('enter the encrypted message')
    encryptedmessage = input()
    # turns encrypted message to ascii
    cryptedascii = [ord(c) for c in encryptedmessage]
    asciisolver = [i // 3 for i in cryptedascii]
    # take the ascii result and turns it to text
    decryptedmessage = [chr(asciisolver[i]) for i in range(0, len(asciisolver))]
    print('decrypted message:')
    print(''.join(decryptedmessage))
    path()

# function that asks encrypt or decrypt
def path():
    x = int(input("for encryption press 1 --- for decryption press 2 then hit the enter"))
    if x == 1:
     encryptor()
    if x == 2:
     decryptor()
    else: print('please press only 1 or 2')
    path()

path()