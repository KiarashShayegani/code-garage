# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 01:36:46 2026

@author: Kiarash
"""
print('-------------------------------------')
print('--- Welcome to manual Bubble Sort ---')
print('-------------------------------------\n')

#num = int(input('Enter a number(-1 to end): '))
#numList = []
#while num != -1:
#    numList.append(num)
#    num = int(input('Next number(-1 to end): '))
#print('Original list =', numList)

numList = [75,13,42,2,76,8,90,321,54,17,67,39,1]
print('Original list =', numList)

def bubbleSort(numberList):
    for _this in range(0, len(numberList)):
        for i in range(0, len(numberList)):
            for j in range(i+1, len(numberList)):
                if numberList[i] > numberList[j]:
                    numberList[i] , numberList[j] = numberList[j], numberList[i]
                    i = j
    return numberList

numList = bubbleSort(numList)

print('Sorted list =', numList)