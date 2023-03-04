CHARSETS = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
DESCRIPTIONS = ['Only uppercase letters', 'Only upper and lowercase letters']

#charset = CHARSETS[0] #Remove, when coosing charset is implemented

usg = True

def getMode():
    mode = []
    print('Do you want to ' + "\u0332".join("en") + 'crypt or ' + "\u0332".join("de") + 'crypt?')
    while mode not in ['e', 'd']:
        mode = input().lower()[:1]
        if mode in ['e', 'd']:
            return mode
        else:
            print('Please enter either "encrypt", "e", "decrypt" or "d".')

def chooseCharset():
    print('Please choose from the following character sets:')
    n = 0
    for n in range(len(CHARSETS)):
        v = n + 1
        print(str(v) + '. ' + DESCRIPTIONS[n] + ' (' + CHARSETS[n] + ')')
        n += 1

    print('Please enter the number infront of the character set to use it.')
    inp = int(input()) - 1

    while inp not in range(len(CHARSETS)):
        inp = int(input()) - 1
        if int in range(len(CHARSETS)):
            return CHARSETS[inp]
        else:
            print('Please enter a number from 1 to ' + len(CHARSETS) + '.')

    return CHARSETS[inp]

def getMessage():
    if mode == "e":
        print('Please enter the message you want to encrypt:')
    elif mode == 'd':
        print('Please enter the message you want to decrypt:')
    else:
        print('Error: Wrong Mode: ' + mode)
    message = input()
    return message

def getKey():
    go = False
    while go != True:
        print('Please enter a number from 1 to ' + str(max_len) + ':')
        key = int(input())
        if key < max_len and key > 1:
            go = True
        else:
            continue
    return key

def encrypt(inp, key):
    outp = ''

    for x in inp:
        current = charset.find(x)
        if current == -1:
            outp += x
        else:
            current += key

            if current >= len(charset):
                current -= len(charset)
            elif current < 0:
                current += len(charset)

            outp += charset[current]

    return outp

def decrypt(inp, key):
    outp = ''
    key = key * -1

    for x in inp:
        current = charset.find(x)
        if current == -1:
            outp += x
        else:
            current += key

            if current >= len(charset):
                current -= len(charset)
            elif current < 0:
                current += len(charset)

            outp += charset[current]

    return outp

while usg == True:
    mode = getMode()
    charset = chooseCharset()
    message = getMessage()
    message = message.upper() #Remove, when now charsets are added
    max_len = len(charset)
    key = getKey()

    if mode == 'e':
        print('Your encrypted message is:')
        print(encrypt(message, key))
    elif mode == 'd':
        print('Your decrypted message is:')
        print(decrypt(message, key))
    else:
        print('Error: Wrong Mode: ' + mode)

    print('Do you want to ' + "\u0332".join("co") + 'ntinue or ' + "\u0332".join("ex") + 'it?')
    ce = []
    while ce not in ['c', 'e']:
        ce = input().lower()[:1]
        if ce in ['c', 'e']:
            if ce == 'c':
                usg = True
            elif ce == 'e':
                usg = False
            else:
                print('Error: Wrong input: ' + ce)
        else:
            print('Please enter either "continue", "c", "exit" or "e".')