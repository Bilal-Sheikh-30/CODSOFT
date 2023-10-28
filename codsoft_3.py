import string
import random

spChar = '@_*&$#'
try:
    pwStrength = input('Choose password strength (weak:w [4 characters] / medium:m [6 characters] / strong:s [8 characters]): ').lower()
    if pwStrength not in ['s','w','m']:
        raise Exception
except:
    print('please choose appropriate password strength')
else:
    if pwStrength == 'w':
        alphaCount = 1
        numCount = 1
        spCharCount = 1
    elif pwStrength == 'm':
        alphaCount = 2
        numCount = 1
        spCharCount = 1
    else:
        alphaCount = 2
        numCount = 2
        spCharCount = 2
    pw = []

    for i in range(alphaCount):
        pw.append(random.choice(string.ascii_uppercase))
        pw.append(random.choice(string.ascii_lowercase))
    for i in range(spCharCount):
        pw.append(random.choice(spChar))
    for i in range(numCount):
        pw.append(str(random.randint(0, 10)))

    reformedPw = ''
    for i in range(len(pw)):
        element = random.choice(pw)
        reformedPw += element
        pw.remove(element)
    print(f'Your password is: {reformedPw}')
