CHARSETS = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890']

def decrypt(inp, key):
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

def loadEnglish():
    with open('words_english.txt') as english:
        words = set(english.read().split())

    return words

def loadGerman():
    with open('words_german.txt') as german:
        words = set(german.read().lower().split())

    return words

usg = True

while usg == True:
    print('Please enter the message you want to decrypt:')
    message = input()
    translation = []
    posible = []
    app = None
    english = loadEnglish()
    german = loadGerman()

    for n in range(1, len(CHARSETS)):
        charset = CHARSETS[n - 1] 
        max_len = len(charset)
        for o in range(1, max_len):
            temp = decrypt(message, o)
            translation.append(temp)

    for n in range(len(translation)):
        current = translation[n]
        act = current.split()
        for x in range(0, len(act)):
            search = act[x].lower()
            if search in english:
                posible.append(current)
            elif search in german:
                posible.append(current)
    print('Posible decrypted versions of the test are:')
    for n in range(1, len(posible)):
        print(posible[n])

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