# Python season 2 training projects
import random

winNum = int(input('Enter your winner number, I wanna guess it human: '))
n = random.randint(1, 99)

attempts = 0
temp1 = 1
temp2 = 99

while n != winNum :
    attempts = attempts + 1
    print('I chose number: ' + str(n))
    if n > winNum :
        print('Oh I guessed higher human, I should decrease it!\n')
        temp2 = n
        n = random.randint(temp1, temp2)

    else :
        print('Ah I guessed lower human, I should increase it!\n')
        temp1 = n
        n = random.randint(temp1, temp2)

print('YEAH!!! I guessed it right with ' + str(attempts) + ' tries human :)\n' + 'Your number was ' + str(winNum) + '!')