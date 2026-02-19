# -*- coding: utf-8 -*-
"""
Spyder Editor

test learning python (650 Q's)

This is a temporary script file.
"""

# Fibonacci shit

n1 = 1
n2 = 1

userInput = int(input('Enter a number: '))
print(f'\nFibonacci sequence for n={userInput} is as below..')

if (userInput == 1):
    print(n1)
elif (userInput == 2):
    print(n1)
    print(n2)
else:
    counter = 3
    print(n1)
    print(n2)
    while counter <= userInput:
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
        counter +=1