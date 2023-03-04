CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_len = len(CHARSET)

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

def decrypt(inp, key):
    outp = ''
    key = key * -1

    for x in inp:
        current = CHARSET.find(x)
        if current == -1:
            outp += x
        else:
            current += key

            if current >= len(CHARSET):
                current -= len(CHARSET)
            elif current < 0:
                current += len(CHARSET)

            outp += CHARSET[current]

    return outp

while usg == True:
    mode = getMode()
    message = getMessage()
    message = message.upper() #Remove, when now charsets are added
    key = getKey()

    if mode == 'e':
        print('Your encrypted message is:')
        # Add message
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