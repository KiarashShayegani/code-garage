# First python based game made by Kiarash
import random

print('\n\n\n****************')
print('***GUESS-GAME***')
print('****************\n\n\n')

name = input('What is your name? \n')

winNum = random.randint(1, 99)
print('I chose my number ' + name + '..!\n')

n = int(input('Try your luck, by guessing a number: '))
attempts = 0

while n != winNum :
    attempts = attempts + 1
    if n > winNum :
        print('Your number is more than mine!\n')
        print('Current attempts: ' + str(attempts))
        n = int(input('Try your luck, again: '))
    else :
        print('Your number is less than mine!\n')
        print('Current attempts: ' + str(attempts))
        n = int(input('Try your luck, again: '))

print('Congradulations ' + name + '..!')
print('You successfully guessed the number ' + str(winNum) + ' with ' + str(attempts) + ' tries!' )