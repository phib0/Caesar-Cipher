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

while usg == True:
    mode = getMode()
    message = getMessage()
    message = message.upper() #Remove, when now charsets are added
    key = getKey()