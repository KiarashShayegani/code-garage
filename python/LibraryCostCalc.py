# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 18:30:31 2026

Reviewing python with jadi

@author: Kiarash
"""

# Library book compenstation calculator:

print('==================================') 
print('=== Library book compenstation ===')
print('==================================\n')

bookCounter=0
bookNames = []
timeBorrowed =[]
timeTaken=[]

inputStr = input('Ready to enter user info(end to finish | any key to continue):')

while inputStr.lower() != 'end': 
    bookCounter +=1
    bName = input(f"Book No.{bookCounter} name: ")
    tBorrow = int(input(f"Book No.{bookCounter} borrowed time(days): "))
    tTaken = int(input(f"Book No.{bookCounter} taken time(days): "))
    
    bookNames.append(bName)
    timeBorrowed.append(tBorrow)
    timeTaken.append(tTaken)
    
    inputStr = input('\nWant to continue? (end to finish):')
    
#print(bookNames)
#print(timeBorrowed)
#print(timeTaken)
costList = []

def bookCostCalculator(bName, tBorrow, tTaken):
    iterationLength = len(bName)
    daysDiff = int()
    
    for book in range(0, iterationLength):
        daysDiff = tBorrow[book] - tTaken[book]
        if daysDiff >= 0:
            cost = 5 * tTaken[book]
        else:
            penalty = abs(daysDiff) * 10
            cost = penalty + (5 * tBorrow[book])
        costList.append(cost)
        
def costSummarize(bName, tBorrow, tTaken, costs):
    print('Borrower Status')
    print('---------------\n')
    
    iterationLength = len(bName)
    
    for book in range(0, iterationLength):
        print(f'Book No.{book+1} status:')
        print(f"Name = {bName[book]} | Cost = ${costs[book]}\n")

#function calling     
print('\nCalculating status..')   
bookCostCalculator(bookNames , timeBorrowed , timeTaken)

print('Summarizing status..\n')
costSummarize(bookNames , timeBorrowed , timeTaken, costList)

totalCost = 0
for i in costList:
    totalCost += i

print(f'Total cost = ${totalCost}')

    

