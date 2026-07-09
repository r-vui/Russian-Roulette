import random
import string

chars = string.ascii_lowercase + ' ' + '.' + ','


while True:
    num = input('how many characters (int): ')
    try:
        num = int(num)
    except ValueError:
        print('u have to put an integer in')
    else:
        babel = ''
        for i in range(num):
            c = random.choice(chars)
            babel += c 
        print(babel)
        break
