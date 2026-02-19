# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 19:54:59 2026

Guessing Game

@author: Kiarash
"""
import random

print('=============================')
print('=== Welcome to Guess Game ===')
print('=============================\n')

print('Summary:')
print('You choose a number between 1 - 100 and I will try to guess it!\n')

userChoice = int(input('Enter your number: '))
print('\n')

machineChoice = random.randint(1, 100)

#triesLimit = int(input('Okay, how many tries is allowed? '))
tryCount = 1
upperBound = 100
lowerBound = 1

while machineChoice != userChoice:
    
    tryCount +=1
    
    if machineChoice > userChoice:
        print(f'Is it {machineChoice}?!')
        print('Oh, my guess was higher.. :/')
        upperBound = machineChoice
        
    elif machineChoice < userChoice:
        print(f'Is it {machineChoice}?!')
        print('Nah, my guess was lower.. :|')
        lowerBound = machineChoice
    
    machineChoice = random.randint(lowerBound+1, upperBound)
        
print(f'\nYay! I guessed your number after {tryCount} tries..\nIt was {machineChoice}!')




